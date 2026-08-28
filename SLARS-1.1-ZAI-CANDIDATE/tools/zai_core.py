#!/usr/bin/env python3
"""Dependency-free core for the SLARS-1.1-ZAI candidate verifier.

The verifier never executes bundle content. It validates a deliberately small
JSON-Schema subset, materializes referenced files, recomputes hashes, verifies
the event chain and evaluates the bounded zero-answer-injection predicates.
"""

from __future__ import annotations

import base64
import codecs
import hashlib
import json
import math
import os
import re
import stat
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote, unquote_to_bytes


STANDARD_VERSION = "SLARS-1.1-ZAI"
SCAN_COST_MULTIPLIER = 32
PACKAGE_DISTRIBUTION_FILES = {
    "AUDIT_SIGMA_COGNITION_CANDIDATE_ZAI.md",
    "CHANGELOG.md",
    "PILOT_CHECKLIST.md",
    "PRODUCER_VERIFICATION.md",
    "README.md",
    "STANDARD.md",
    "ZERO_ANSWER_INJECTION_STANDARD.md",
    "schemas/protocol.schema.json",
    "schemas/run_bundle.schema.json",
    "schemas/zai_protocol.schema.json",
    "schemas/zai_run_bundle.schema.json",
    "templates/protocol.template.json",
    "templates/run_bundle.template.json",
    "templates/zai_protocol.template.json",
    "templates/zai_run_bundle.template.json",
    "tests/test_validate_bundle.py",
    "tests/test_validate_zai_bundle.py",
    "tools/validate_bundle.py",
    "tools/validate_zai_bundle.py",
    "tools/zai_core.py",
}
ARTIFACT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
RFC3339_UTC_RE = re.compile(
    r"^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"
    r"T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]{1,6})?Z$"
)
STATUS_ORDER = {
    "PASS": 0,
    "FAIL": 1,
    "INSUFFICIENT_EVIDENCE": 2,
    "UNVERIFIED": 3,
    "INVALID": 4,
}

CLAIM_RULES = {
    "SIGMA_SOURCE_LANGUAGE_BOUND_FOR_LOCKED_SOURCE": ("Z0",),
    "REGISTERED_PREOUTPUT_INJECTION_SCAN_CLEAN": ("Z0", "Z1", "Z2"),
    "DECLARED_SIGMAC_SIGMA_VM_EVENT_CHAIN_RAW_STDOUT_BOUND": ("Z0", "Z1", "Z3"),
    "NO_DETECTED_PROHIBITED_ANSWER_INJECTION_WITHIN_DECLARED_MATERIALIZED_BOUNDARY": (
        "Z0",
        "Z1",
        "Z2",
        "Z3",
        "Z4",
    ),
}

REQUIRED_POLICY_LOCKS = {
    "HUMAN_LANGUAGE_AS_SIGMA_COGNITION": "FORBIDDEN_UNTIL_PROVEN",
    "SUPPORTOR_ANSWERS_FOR_SIGMA": "FORBIDDEN",
    "PREWRITTEN_ANSWER": "FORBIDDEN",
    "PREWRITTEN_HYPOTHESIS": "FORBIDDEN",
    "PREWRITTEN_REASONING_PATH": "FORBIDDEN",
    "PREWRITTEN_CONCLUSION": "FORBIDDEN",
    "SIGMA_SELF_OBSERVES_AND_ANSWERS": "REQUIRED",
    "HOST_SEMANTIC_TRANSFORMATION": "FORBIDDEN",
    "OUTPUT_SELECTION_OR_REWRITE": "FORBIDDEN",
    "CLAIM_POLICY": "CLAIM_LESS_THAN_OR_EQUAL_TO_EVIDENCE",
}

FORBIDDEN_CLASSES = {
    "SUPPORTOR_ANSWER",
    "PREWRITTEN_ANSWER",
    "PREWRITTEN_HYPOTHESIS",
    "PREWRITTEN_REASONING_PATH",
    "PREWRITTEN_CONCLUSION",
}

REQUIRED_ROLES = (
    "CANDIDATE_SOURCE",
    "SIGMAC_BINARY",
    "SIGMA_VM_BINARY",
    "BLIND_INPUT",
    "ANSWER_KEY",
    "EVALUATION_RUBRIC",
    "VISIBILITY_MANIFEST",
    "RUNNER_SOURCE",
    "RUN_SPECIFIC_BYTECODE",
    "HOST_TRACE",
    "RAW_STDOUT",
    "RAW_STDERR",
    "SEMANTIC_REVIEW",
    "EXTERNAL_EVALUATION",
)

REQUIRED_REPEATABLE_ROLES = {"CHANNEL_EVIDENCE"}

CANONICAL_ARTIFACT_METADATA = {
    "CANDIDATE_SOURCE": ("CANDIDATE_BUILDER", "PRE_FREEZE", False, True),
    "SIGMAC_BINARY": ("RUNNER", "PRE_FREEZE", False, True),
    "SIGMA_VM_BINARY": ("RUNNER", "PRE_FREEZE", False, True),
    "BLIND_INPUT": ("TEST_DESIGNER", "PRE_OUTPUT", True, True),
    "ANSWER_KEY": ("KEY_CUSTODIAN", "POST_OUTPUT_KEY", False, False),
    "EVALUATION_RUBRIC": ("TEST_DESIGNER", "PRE_FREEZE", False, False),
    "VISIBILITY_MANIFEST": ("AUDITOR", "PRE_OUTPUT", False, True),
    "RUNNER_SOURCE": ("RUNNER", "PRE_FREEZE", False, True),
    "RUN_SPECIFIC_BYTECODE": ("SIGMAC", "PRE_OUTPUT", False, True),
    "HOST_TRACE": ("RUNNER", "OUTPUT", False, False),
    "RAW_STDOUT": ("SIGMA_VM", "OUTPUT", False, False),
    "RAW_STDERR": ("SIGMA_VM", "OUTPUT", False, False),
    "SEMANTIC_REVIEW": ("AUDITOR", "EVALUATION", False, False),
    "EXTERNAL_EVALUATION": ("EVALUATOR", "EVALUATION", False, False),
    "CHANNEL_EVIDENCE": ("AUDITOR", "PRE_OUTPUT", False, True),
}

REQUIRED_PREOUTPUT_ROLES = {
    "CANDIDATE_SOURCE",
    "SIGMAC_BINARY",
    "SIGMA_VM_BINARY",
    "BLIND_INPUT",
    "VISIBILITY_MANIFEST",
    "RUNNER_SOURCE",
    "RUN_SPECIFIC_BYTECODE",
}

FORBIDDEN_PREOUTPUT_ROLES = {
    "ANSWER_KEY",
    "EVALUATION_RUBRIC",
    "HOST_TRACE",
    "RAW_STDOUT",
    "RAW_STDERR",
    "SEMANTIC_REVIEW",
    "EXTERNAL_EVALUATION",
}

REQUIRED_CHANNELS = {
    "SOURCE",
    "BYTECODE",
    "STATE",
    "STDIN",
    "ARGV",
    "ENVIRONMENT",
    "FILES",
    "FILENAMES",
    "DIRECTORY_ORDER",
    "HOST_RESULTS",
    "TOOL_MAP",
    "TOOL_RESULTS",
    "NETWORK",
    "CLOCK",
    "RNG",
    "CACHE",
    "STDERR",
    "EXIT_CODE",
    "RESOURCE_LIMIT_SIGNAL",
}

REQUIRED_EVENTS = (
    "PROTOCOL_FREEZE",
    "CANDIDATE_FREEZE",
    "BLIND_CASE_COMMIT",
    "CHANNEL_SNAPSHOT",
    "RUN_START",
    "SIGMAC_COMPLETE",
    "VM_OUTPUT_FROZEN",
    "KEY_FIRST_ACCESS",
    "SEMANTIC_REVIEW",
    "EXTERNAL_EVALUATION",
)

ALLOWED_HOST_OPERATIONS = {
    "HASH_BYTES",
    "EXEC_SIGMAC",
    "EXEC_SIGMA_VM",
    "CAPTURE_STDOUT",
    "CAPTURE_STDERR",
    "FREEZE_BYTES",
}

SUPPORTED_SCHEMA_KEYWORDS = {
    "$schema",
    "$id",
    "title",
    "$defs",
    "$ref",
    "type",
    "additionalProperties",
    "required",
    "properties",
    "const",
    "enum",
    "pattern",
    "format",
    "minLength",
    "maxLength",
    "minimum",
    "maximum",
    "minItems",
    "maxItems",
    "uniqueItems",
    "items",
}


class StrictJSONError(ValueError):
    """Raised for duplicate keys, non-finite values or bounded parse errors."""


@dataclass
class Report:
    errors: list[tuple[str, str, str]] = field(default_factory=list)
    warnings: list[tuple[str, str, str]] = field(default_factory=list)
    gates: dict[str, str] = field(default_factory=dict)
    task_outcome: str = "NOT_RUN"
    package_manifest_status: str = "UNVERIFIED"
    verified_claims: set[str] = field(default_factory=set)
    scan_matches: list[dict[str, str]] = field(default_factory=list)

    @staticmethod
    def _safe_detail(detail: Any) -> str:
        escaped: list[str] = []
        for character in str(detail):
            codepoint = ord(character)
            category = unicodedata.category(character)
            if category.startswith("C") or category in {"Zl", "Zp"}:
                if codepoint <= 0xFFFF:
                    escaped.append(f"\\u{codepoint:04x}")
                else:
                    escaped.append(f"\\U{codepoint:08x}")
            else:
                escaped.append(character)
        return "".join(escaped)

    def error(self, stage: str, code: str, detail: str) -> None:
        self.errors.append((stage, code, self._safe_detail(detail)))

    def warn(self, stage: str, code: str, detail: str) -> None:
        self.warnings.append((stage, code, self._safe_detail(detail)))

    def set_gate(self, gate: str, status: str) -> None:
        if status not in STATUS_ORDER:
            raise ValueError(f"unsupported status {status}")
        self.gates[gate] = status

    @property
    def status(self) -> str:
        if not self.gates:
            return "INVALID" if self.errors else "UNVERIFIED"
        status = max(self.gates.values(), key=lambda value: STATUS_ORDER[value])
        if self.errors and STATUS_ORDER[status] < STATUS_ORDER["INVALID"]:
            return "INVALID"
        return status


@dataclass(frozen=True)
class MaterializedArtifact:
    record: dict[str, Any]
    path: Path
    data: bytes

    @property
    def artifact_id(self) -> str:
        return self.record["artifact_id"]

    @property
    def sha256(self) -> str:
        return self.record["sha256"]


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _reject_constant(value: str) -> None:
    raise StrictJSONError(f"non-finite JSON number: {value}")


def _parse_int(value: str) -> int:
    if len(value) > 128:
        raise StrictJSONError("JSON integer exceeds 128 characters")
    try:
        return int(value)
    except (ValueError, OverflowError) as exc:
        raise StrictJSONError("invalid JSON integer") from exc


def _parse_float(value: str) -> float:
    if len(value) > 128:
        raise StrictJSONError("JSON number exceeds 128 characters")
    try:
        parsed = float(value)
    except (ValueError, OverflowError) as exc:
        raise StrictJSONError("invalid JSON number") from exc
    if not math.isfinite(parsed):
        raise StrictJSONError("non-finite JSON number")
    return parsed


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJSONError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _count_json(value: Any, depth: int = 0) -> tuple[int, int]:
    if depth > 64:
        raise StrictJSONError("JSON nesting exceeds 64")
    nodes = 1
    max_depth = depth
    if isinstance(value, dict):
        if len(value) > 4096:
            raise StrictJSONError("object has more than 4096 keys")
        for key, child in value.items():
            if len(key) > 4096:
                raise StrictJSONError("JSON key exceeds 4096 characters")
            try:
                key.encode("utf-8", errors="strict")
            except UnicodeEncodeError as exc:
                raise StrictJSONError("JSON key contains an unpaired surrogate") from exc
            child_nodes, child_depth = _count_json(child, depth + 1)
            nodes += child_nodes
            max_depth = max(max_depth, child_depth)
    elif isinstance(value, list):
        if len(value) > 100000:
            raise StrictJSONError("array has more than 100000 items")
        for child in value:
            child_nodes, child_depth = _count_json(child, depth + 1)
            nodes += child_nodes
            max_depth = max(max_depth, child_depth)
    elif isinstance(value, str):
        if len(value) > 4_000_000:
            raise StrictJSONError("JSON string exceeds 4000000 characters")
        try:
            value.encode("utf-8", errors="strict")
        except UnicodeEncodeError as exc:
            raise StrictJSONError("JSON string contains an unpaired surrogate") from exc
    elif isinstance(value, float) and not math.isfinite(value):
        raise StrictJSONError("non-finite JSON number")
    if nodes > 1_000_000:
        raise StrictJSONError("JSON node count exceeds 1000000")
    return nodes, max_depth


def parse_json_bytes(data: bytes, label: str, max_bytes: int = 16 * 1024 * 1024) -> Any:
    if len(data) > max_bytes:
        raise StrictJSONError(f"{label}: JSON exceeds {max_bytes} bytes")
    try:
        text = data.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise StrictJSONError(f"{label}: invalid UTF-8: {exc}") from exc
    try:
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_int=_parse_int,
            parse_float=_parse_float,
        )
    except (json.JSONDecodeError, StrictJSONError, ValueError, OverflowError) as exc:
        raise StrictJSONError(f"{label}: {exc}") from exc
    _count_json(value)
    return value


def load_json_file(path: Path, label: str, max_bytes: int = 16 * 1024 * 1024) -> Any:
    try:
        data = path.read_bytes()
    except OSError as exc:
        raise StrictJSONError(f"{label}: cannot read {path}: {exc}") from exc
    return parse_json_bytes(data, label, max_bytes=max_bytes)


def parse_utc(value: Any) -> datetime | None:
    if not isinstance(value, str) or RFC3339_UTC_RE.fullmatch(value) is None:
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed if parsed.utcoffset() is not None and parsed.utcoffset().total_seconds() == 0 else None


def _schema_type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def _json_equal(left: Any, right: Any) -> bool:
    """Compare JSON values without Python's ``True == 1`` ambiguity."""

    if isinstance(left, bool) or isinstance(right, bool):
        return type(left) is type(right) and left == right
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return not isinstance(left, bool) and not isinstance(right, bool) and left == right
    return type(left) is type(right) and left == right


def _resolve_ref(root_schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise StrictJSONError(f"external schema reference forbidden: {ref}")
    current: Any = root_schema
    for raw_part in ref[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or part not in current:
            raise StrictJSONError(f"unresolved schema reference: {ref}")
        current = current[part]
    if not isinstance(current, dict):
        raise StrictJSONError(f"schema reference is not an object: {ref}")
    return current


def check_schema_keywords(schema: Any, path: str = "$") -> list[str]:
    errors: list[str] = []
    if not isinstance(schema, dict):
        return [f"{path}: schema node must be object"]
    for key, value in schema.items():
        if key not in SUPPORTED_SCHEMA_KEYWORDS:
            errors.append(f"{path}: unsupported schema keyword {key}")
        if key in {"properties", "$defs"} and isinstance(value, dict):
            for child_key, child in value.items():
                errors.extend(check_schema_keywords(child, f"{path}.{key}.{child_key}"))
        elif key == "items" and isinstance(value, dict):
            errors.extend(check_schema_keywords(value, f"{path}.items"))
    return errors


def validate_schema(
    value: Any,
    schema: dict[str, Any],
    root_schema: dict[str, Any] | None = None,
    path: str = "$",
) -> list[str]:
    root = root_schema or schema
    if "$ref" in schema:
        return validate_schema(value, _resolve_ref(root, schema["$ref"]), root, path)
    errors: list[str] = []
    expected_type = schema.get("type")
    if expected_type is not None:
        expected_types = [expected_type] if isinstance(expected_type, str) else expected_type
        if not isinstance(expected_types, list) or not all(isinstance(item, str) for item in expected_types):
            return [f"{path}: schema type declaration invalid"]
        if not any(_schema_type_matches(value, item) for item in expected_types):
            return [f"{path}: expected type {expected_types}, got {type(value).__name__}"]
    if "const" in schema and not _json_equal(value, schema["const"]):
        errors.append(f"{path}: value does not equal const")
    if "enum" in schema and not any(_json_equal(value, item) for item in schema["enum"]):
        errors.append(f"{path}: value not in enum")
    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path}.{key}: required property missing")
        properties = schema.get("properties", {})
        if not isinstance(properties, dict):
            errors.append(f"{path}: schema properties must be object")
            properties = {}
        for key, child in value.items():
            if key in properties:
                errors.extend(validate_schema(child, properties[key], root, f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}.{key}: additional property forbidden")
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: fewer than minItems")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: more than maxItems")
        if schema.get("uniqueItems") is True:
            seen: set[bytes] = set()
            for index, child in enumerate(value):
                marker = canonical_json_bytes(child)
                if marker in seen:
                    errors.append(f"{path}[{index}]: duplicate item")
                seen.add(marker)
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, child in enumerate(value):
                errors.extend(validate_schema(child, item_schema, root, f"{path}[{index}]"))
    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: shorter than minLength")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(f"{path}: longer than maxLength")
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            errors.append(f"{path}: pattern mismatch")
        if schema.get("format") == "date-time" and parse_utc(value) is None:
            errors.append(f"{path}: date-time must be RFC3339 UTC with Z")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: below minimum")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: above maximum")
    return errors


def strict_schema_check(value: Any, schema: dict[str, Any], report: Report, label: str) -> bool:
    keyword_errors = check_schema_keywords(schema)
    for detail in keyword_errors:
        report.error("SCHEMA", "UNSUPPORTED_SCHEMA", f"{label}: {detail}")
    if keyword_errors:
        return False
    errors = validate_schema(value, schema)
    for detail in errors:
        report.error("SCHEMA", "SCHEMA_VIOLATION", f"{label}: {detail}")
    return not errors


def safe_relative_path(raw: str) -> bool:
    if not isinstance(raw, str) or not raw or "\\" in raw or "\x00" in raw:
        return False
    if any(ord(character) < 32 or ord(character) == 127 for character in raw):
        return False
    if raw.startswith("/") or "//" in raw:
        return False
    parts = raw.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        return False
    path = PurePosixPath(raw)
    return not path.is_absolute()


def verify_package_manifest(root: Path, data: bytes, report: Report) -> bool:
    try:
        text = data.decode("ascii", errors="strict")
    except UnicodeDecodeError as exc:
        report.error("RECEIPT", "PACKAGE_MANIFEST_NOT_ASCII", str(exc))
        return False
    entries: dict[str, str] = {}
    ok = True
    actual_files: set[str] = set()
    try:
        for path in root.rglob("*"):
            relative = path.relative_to(root).as_posix()
            if relative == "MANIFEST.sha256" or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            if path.is_symlink():
                report.error("RECEIPT", "UNEXPECTED_PACKAGE_SYMLINK", relative)
                ok = False
            elif path.is_file():
                actual_files.add(relative)
    except OSError as exc:
        report.error("RECEIPT", "PACKAGE_TREE_ENUMERATION_FAILED", str(exc))
        return False
    if actual_files != PACKAGE_DISTRIBUTION_FILES:
        report.error(
            "RECEIPT",
            "PACKAGE_TREE_COVERAGE_MISMATCH",
            str(sorted(actual_files ^ PACKAGE_DISTRIBUTION_FILES)),
        )
        ok = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9][A-Za-z0-9._/-]*)", line)
        if match is None:
            report.error("RECEIPT", "PACKAGE_MANIFEST_LINE_INVALID", str(line_number))
            ok = False
            continue
        expected_sha, relative = match.groups()
        if not safe_relative_path(relative) or relative == "MANIFEST.sha256":
            report.error("RECEIPT", "PACKAGE_MANIFEST_PATH_INVALID", relative)
            ok = False
            continue
        if relative in entries:
            report.error("RECEIPT", "PACKAGE_MANIFEST_DUPLICATE_PATH", relative)
            ok = False
            continue
        entries[relative] = expected_sha
    if set(entries) != PACKAGE_DISTRIBUTION_FILES:
        report.error(
            "RECEIPT",
            "PACKAGE_MANIFEST_COVERAGE_MISMATCH",
            str(sorted(set(entries) ^ PACKAGE_DISTRIBUTION_FILES)),
        )
        ok = False
    for relative in sorted(PACKAGE_DISTRIBUTION_FILES & set(entries)):
        path = root.joinpath(*relative.split("/"))
        if path.is_symlink():
            report.error("RECEIPT", "PACKAGE_FILE_SYMLINK_FORBIDDEN", relative)
            ok = False
            continue
        try:
            if not path.is_file():
                raise OSError("regular file required")
            actual_sha = sha256_bytes(path.read_bytes())
        except OSError as exc:
            report.error("RECEIPT", "PACKAGE_FILE_UNAVAILABLE", f"{relative}:{exc}")
            ok = False
            continue
        if actual_sha != entries[relative]:
            report.error("RECEIPT", "PACKAGE_FILE_SHA256_MISMATCH", relative)
            ok = False
    return ok


def _path_has_symlink(root: Path, relative: str) -> bool:
    current = root
    for part in relative.split("/"):
        current = current / part
        try:
            if current.is_symlink():
                return True
        except OSError:
            return True
    return False


def materialize_artifacts(
    run: dict[str, Any],
    evidence_root: Path,
    limits: dict[str, Any],
    report: Report,
) -> dict[str, MaterializedArtifact]:
    try:
        root = evidence_root.resolve(strict=True)
    except OSError as exc:
        report.error("ARTIFACT", "EVIDENCE_ROOT_UNAVAILABLE", str(exc))
        return {}
    if not root.is_dir():
        report.error("ARTIFACT", "EVIDENCE_ROOT_NOT_DIRECTORY", str(root))
        return {}
    records = run.get("artifacts", [])
    if len(records) > limits["max_artifacts"]:
        report.error("ARTIFACT", "ARTIFACT_LIMIT_EXCEEDED", str(len(records)))
        return {}
    artifacts: dict[str, MaterializedArtifact] = {}
    total_declared_bytes = 0
    seen_paths: set[str] = set()
    seen_casefolded: set[str] = set()
    for index, record in enumerate(records):
        artifact_id = record.get("artifact_id")
        relative = record.get("relative_path")
        label = f"artifacts[{index}]"
        if not isinstance(artifact_id, str) or ARTIFACT_ID_RE.fullmatch(artifact_id) is None:
            report.error("ARTIFACT", "ARTIFACT_ID_INVALID", str(artifact_id))
            continue
        if artifact_id in artifacts:
            report.error("ARTIFACT", "DUPLICATE_ARTIFACT_ID", str(artifact_id))
            continue
        if not safe_relative_path(relative):
            report.error("ARTIFACT", "UNSAFE_RELATIVE_PATH", f"{label}: {relative!r}")
            continue
        if relative in seen_paths or relative.casefold() in seen_casefolded:
            report.error("ARTIFACT", "PATH_IDENTITY_COLLISION", relative)
            continue
        seen_paths.add(relative)
        seen_casefolded.add(relative.casefold())
        if _path_has_symlink(root, relative):
            report.error("ARTIFACT", "SYMLINK_FORBIDDEN", relative)
            continue
        path = root.joinpath(*relative.split("/"))
        try:
            resolved = path.resolve(strict=True)
        except OSError as exc:
            report.error("ARTIFACT", "ARTIFACT_MISSING", f"{relative}: {exc}")
            continue
        try:
            resolved.relative_to(root)
        except ValueError:
            report.error("ARTIFACT", "PATH_ESCAPE", relative)
            continue
        try:
            before = resolved.stat()
        except OSError as exc:
            report.error("ARTIFACT", "ARTIFACT_STAT_FAILED", f"{relative}: {exc}")
            continue
        if not stat.S_ISREG(before.st_mode):
            report.error("ARTIFACT", "REGULAR_FILE_REQUIRED", relative)
            continue
        if not limits["hardlinks_allowed"] and before.st_nlink != 1:
            report.error("ARTIFACT", "HARDLINK_FORBIDDEN", relative)
            continue
        if before.st_size > limits["max_artifact_bytes"]:
            report.error("ARTIFACT", "ARTIFACT_BYTES_LIMIT_EXCEEDED", relative)
            continue
        total_declared_bytes += before.st_size
        if total_declared_bytes > limits["max_total_artifact_bytes"]:
            report.error("ARTIFACT", "TOTAL_ARTIFACT_BYTES_LIMIT_EXCEEDED", str(total_declared_bytes))
            return {}
        descriptor: int | None = None
        try:
            flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
            descriptor = os.open(resolved, flags)
            opened_before = os.fstat(descriptor)
            remaining = limits["max_artifact_bytes"] + 1
            chunks: list[bytes] = []
            while remaining > 0:
                chunk = os.read(descriptor, min(1_048_576, remaining))
                if not chunk:
                    break
                chunks.append(chunk)
                remaining -= len(chunk)
            data = b"".join(chunks)
            opened_after = os.fstat(descriptor)
            after = resolved.stat()
        except OSError as exc:
            report.error("ARTIFACT", "ARTIFACT_READ_FAILED", f"{relative}: {exc}")
            continue
        finally:
            if descriptor is not None:
                os.close(descriptor)
        if len(data) > limits["max_artifact_bytes"]:
            report.error("ARTIFACT", "ARTIFACT_BYTES_LIMIT_EXCEEDED", relative)
            continue
        identity_before = (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
        identity_after = (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
        opened_identity_before = (
            opened_before.st_dev,
            opened_before.st_ino,
            opened_before.st_size,
            opened_before.st_mtime_ns,
        )
        opened_identity_after = (
            opened_after.st_dev,
            opened_after.st_ino,
            opened_after.st_size,
            opened_after.st_mtime_ns,
        )
        if (
            identity_before != identity_after
            or identity_before != opened_identity_before
            or opened_identity_before != opened_identity_after
        ):
            report.error("ARTIFACT", "ARTIFACT_CHANGED_DURING_HASH", relative)
            continue
        actual_hash = sha256_bytes(data)
        if record.get("byte_count") != len(data):
            report.error("ARTIFACT", "ARTIFACT_BYTE_COUNT_MISMATCH", relative)
            continue
        if record.get("sha256") != actual_hash:
            report.error("ARTIFACT", "ARTIFACT_SHA256_MISMATCH", relative)
            continue
        artifacts[artifact_id] = MaterializedArtifact(record, resolved, data)
    return artifacts


def index_roles(artifacts: dict[str, MaterializedArtifact], report: Report) -> dict[str, MaterializedArtifact]:
    result: dict[str, MaterializedArtifact] = {}
    for artifact in artifacts.values():
        role = artifact.record["semantic_role"]
        if role in REQUIRED_ROLES and role in result:
            report.error("ARTIFACT", "DUPLICATE_SEMANTIC_ROLE", role)
        elif role in REQUIRED_ROLES:
            result[role] = artifact
        elif role in REQUIRED_REPEATABLE_ROLES:
            result.setdefault(role, artifact)
    for role in REQUIRED_ROLES:
        if role not in result:
            report.error("ARTIFACT", "REQUIRED_SEMANTIC_ROLE_MISSING", role)
    for role in REQUIRED_REPEATABLE_ROLES:
        if role not in result:
            report.error("ARTIFACT", "REQUIRED_REPEATABLE_ROLE_MISSING", role)
    return result


def verify_artifact_metadata(
    artifacts: dict[str, MaterializedArtifact],
    report: Report,
) -> bool:
    ok = True
    for artifact in artifacts.values():
        role = artifact.record["semantic_role"]
        expected = CANONICAL_ARTIFACT_METADATA.get(role)
        actual = (
            artifact.record["origin_role"],
            artifact.record["stage"],
            artifact.record["candidate_visible"],
            artifact.record["pre_output_reachable"],
        )
        if expected is None or actual != expected:
            report.error(
                "ARTIFACT",
                "ARTIFACT_METADATA_MISMATCH",
                f"{artifact.artifact_id}:{role}",
            )
            ok = False
    return ok


def require_exact_keys(value: Any, required: set[str], label: str, report: Report) -> bool:
    if not isinstance(value, dict):
        report.error("CONTENT", "OBJECT_REQUIRED", label)
        return False
    actual = set(value)
    if actual != required:
        report.error(
            "CONTENT",
            "EXACT_KEYS_MISMATCH",
            f"{label}: missing={sorted(required-actual)} extra={sorted(actual-required)}",
        )
        return False
    return True


def parse_artifact_json(artifact: MaterializedArtifact, report: Report) -> Any | None:
    try:
        return parse_json_bytes(artifact.data, artifact.artifact_id)
    except StrictJSONError as exc:
        report.error("CONTENT", "ARTIFACT_JSON_INVALID", str(exc))
        return None


def verify_protocol_policy(protocol: dict[str, Any], report: Report) -> bool:
    ok = True
    locks = protocol.get("policy_locks", {})
    if locks != REQUIRED_POLICY_LOCKS:
        report.error("Z0", "POLICY_LOCK_MISMATCH", str(locks))
        ok = False
    minimum_artifacts = len(REQUIRED_ROLES) + len(REQUIRED_REPEATABLE_ROLES)
    if protocol.get("evidence_limits", {}).get("max_artifacts", 0) < minimum_artifacts:
        report.error(
            "Z0",
            "MAX_ARTIFACTS_BELOW_REQUIRED_MINIMUM",
            str(minimum_artifacts),
        )
        ok = False
    roles = protocol.get("roles", {})
    role_values = list(roles.values()) if isinstance(roles, dict) else []
    canonical_roles = [unicodedata.normalize("NFKC", value).casefold().strip() for value in role_values]
    if len(role_values) != 6 or len(set(canonical_roles)) != 6 or any(not value for value in canonical_roles):
        report.error("Z1", "ROLE_COLLISION", str(roles))
        ok = False
    requested = protocol.get("claims_requested", [])
    if any(claim not in CLAIM_RULES for claim in requested):
        report.error("CLAIM", "UNKNOWN_PROTOCOL_CLAIM", str(requested))
        ok = False
    return ok


def verify_commitments(
    protocol: dict[str, Any],
    artifacts: dict[str, MaterializedArtifact],
    role_index: dict[str, MaterializedArtifact],
    report: Report,
) -> bool:
    ok = True
    bindings = {
        "candidate_source": ("CANDIDATE_SOURCE", protocol["candidate"]["source_artifact_id"]),
        "sigmac_binary": ("SIGMAC_BINARY", protocol["runtime"]["sigmac_artifact_id"]),
        "sigma_vm_binary": ("SIGMA_VM_BINARY", protocol["runtime"]["sigma_vm_artifact_id"]),
        "runner_source": ("RUNNER_SOURCE", protocol["runtime"]["runner_source_artifact_id"]),
        "evaluation_rubric": ("EVALUATION_RUBRIC", protocol["review"]["evaluation_rubric_artifact_id"]),
    }
    for commitment_name, (semantic_role, expected_id) in bindings.items():
        commitment = protocol["committed_artifacts"][commitment_name]
        artifact = artifacts.get(commitment.get("artifact_id"))
        if commitment.get("artifact_id") != expected_id:
            report.error("Z1", "COMMITMENT_ID_BINDING_MISMATCH", commitment_name)
            ok = False
        if artifact is None or role_index.get(semantic_role) is not artifact:
            report.error("Z1", "COMMITTED_ARTIFACT_MISSING_OR_WRONG_ROLE", commitment_name)
            ok = False
            continue
        if commitment.get("sha256") != artifact.sha256:
            report.error("Z1", "COMMITTED_ARTIFACT_HASH_MISMATCH", commitment_name)
            ok = False
    return ok


def verify_artifact_id_bindings(
    protocol: dict[str, Any],
    run: dict[str, Any],
    role_index: dict[str, MaterializedArtifact],
    report: Report,
) -> bool:
    """Bind every protocol/run artifact pointer to the unique semantic role."""

    expected = {
        "blind_case.input_artifact_id": (protocol["blind_case"]["input_artifact_id"], "BLIND_INPUT"),
        "blind_case.answer_key_artifact_id": (
            protocol["blind_case"]["answer_key_artifact_id"],
            "ANSWER_KEY",
        ),
        "blind_case.visibility_manifest_artifact_id": (
            protocol["blind_case"]["visibility_manifest_artifact_id"],
            "VISIBILITY_MANIFEST",
        ),
        "runtime.host_trace_artifact_id": (protocol["runtime"]["host_trace_artifact_id"], "HOST_TRACE"),
        "runtime.raw_stdout_artifact_id": (protocol["runtime"]["raw_stdout_artifact_id"], "RAW_STDOUT"),
        "runtime.raw_stderr_artifact_id": (protocol["runtime"]["raw_stderr_artifact_id"], "RAW_STDERR"),
        "review.semantic_review_artifact_id": (
            protocol["review"]["semantic_review_artifact_id"],
            "SEMANTIC_REVIEW",
        ),
        "review.evaluation_rubric_artifact_id": (
            protocol["review"]["evaluation_rubric_artifact_id"],
            "EVALUATION_RUBRIC",
        ),
        "review.external_evaluation_artifact_id": (
            protocol["review"]["external_evaluation_artifact_id"],
            "EXTERNAL_EVALUATION",
        ),
        "run.scan.semantic_review_artifact_id": (
            run["scan"]["semantic_review_artifact_id"],
            "SEMANTIC_REVIEW",
        ),
    }
    ok = True
    for label, (artifact_id, role) in expected.items():
        artifact = role_index.get(role)
        if artifact is None or artifact_id != artifact.artifact_id:
            report.error("ARTIFACT", "ARTIFACT_ID_ROLE_BINDING_MISMATCH", f"{label}:{artifact_id}:{role}")
            ok = False
    return ok


def verify_language_source(
    protocol: dict[str, Any],
    role_index: dict[str, MaterializedArtifact],
    report: Report,
) -> bool:
    source = role_index.get("CANDIDATE_SOURCE")
    if source is None:
        return False
    prefix = protocol["candidate"]["required_header_prefix"].encode("utf-8")
    if not source.data.startswith(prefix):
        report.error("Z0", "SIGMA_HEADER_PREFIX_MISSING", source.artifact_id)
        return False
    try:
        source.data.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        report.error("Z0", "SIGMA_SOURCE_NOT_UTF8", source.artifact_id)
        return False
    return True


def parse_channel_evidence(
    run: dict[str, Any],
    artifacts: dict[str, MaterializedArtifact],
    report: Report,
) -> dict[str, dict[str, str]] | None:
    by_artifact: dict[str, dict[str, str]] = {}
    globally_seen: set[str] = set()
    ok = True
    for artifact in artifacts.values():
        if artifact.record["semantic_role"] != "CHANNEL_EVIDENCE":
            continue
        value = parse_artifact_json(artifact, report)
        if not require_exact_keys(
            value,
            {"schema_version", "run_id", "captures"},
            "channel_evidence",
            report,
        ):
            ok = False
            continue
        if value["schema_version"] != "slars-zai-channel-evidence/v2" or value["run_id"] != run["run_id"]:
            report.error("Z1", "CHANNEL_EVIDENCE_BINDING_MISMATCH", artifact.artifact_id)
            ok = False
        captures = value["captures"]
        if not isinstance(captures, list) or not captures or len(captures) > len(REQUIRED_CHANNELS):
            report.error("Z1", "CHANNEL_CAPTURE_SET_INVALID", artifact.artifact_id)
            ok = False
            continue
        artifact_captures: dict[str, str] = {}
        for index, capture in enumerate(captures):
            if not require_exact_keys(
                capture,
                {
                    "channel_id",
                    "status",
                    "evidence_class",
                    "observation_utf8",
                    "observation_byte_count",
                    "observation_sha256",
                },
                f"channel_evidence.captures[{index}]",
                report,
            ):
                ok = False
                continue
            channel_id = capture["channel_id"]
            status = capture["status"]
            evidence_class = capture["evidence_class"]
            observation = capture["observation_utf8"]
            if not isinstance(channel_id, str) or channel_id not in REQUIRED_CHANNELS:
                report.error("Z1", "CHANNEL_CAPTURE_ID_INVALID", str(channel_id))
                ok = False
                continue
            if channel_id in globally_seen or channel_id in artifact_captures:
                report.error("Z1", "CHANNEL_CAPTURE_DUPLICATE", channel_id)
                ok = False
                continue
            expected_class = (
                {
                    "CAPTURED": "DECLARED_CAPTURE_RECORD",
                    "DISABLED": "DECLARED_DISABLEMENT_RECORD",
                }.get(status)
                if isinstance(status, str)
                else None
            )
            if expected_class is None or evidence_class != expected_class:
                report.error("Z1", "CHANNEL_CAPTURE_CLASS_INVALID", channel_id)
                ok = False
            if not isinstance(observation, str) or not observation:
                report.error("Z1", "CHANNEL_CAPTURE_OBSERVATION_EMPTY", channel_id)
                ok = False
                continue
            observation_bytes = observation.encode("utf-8")
            if len(observation_bytes) > 4096:
                report.error("Z1", "CHANNEL_CAPTURE_OBSERVATION_LIMIT_EXCEEDED", channel_id)
                ok = False
            if (
                capture["observation_byte_count"] != len(observation_bytes)
                or capture["observation_sha256"] != sha256_bytes(observation_bytes)
            ):
                report.error("Z1", "CHANNEL_CAPTURE_OBSERVATION_BINDING_MISMATCH", channel_id)
                ok = False
            artifact_captures[channel_id] = status
            globally_seen.add(channel_id)
        by_artifact[artifact.artifact_id] = artifact_captures
    return by_artifact if ok else None


def verify_visibility_manifest(
    protocol: dict[str, Any],
    run: dict[str, Any],
    artifacts: dict[str, MaterializedArtifact],
    role_index: dict[str, MaterializedArtifact],
    report: Report,
) -> tuple[bool, set[str]]:
    manifest_artifact = role_index.get("VISIBILITY_MANIFEST")
    if manifest_artifact is None:
        return False, set()
    if manifest_artifact.artifact_id != protocol["blind_case"]["visibility_manifest_artifact_id"]:
        report.error("Z1", "VISIBILITY_MANIFEST_ID_MISMATCH", manifest_artifact.artifact_id)
        return False, set()
    value = parse_artifact_json(manifest_artifact, report)
    required = {
        "schema_version",
        "case_id",
        "candidate_visible_artifact_ids",
        "pre_output_reachable_artifact_ids",
        "candidate_forbidden_artifact_ids",
        "channels",
        "undeclared_readable_channels",
    }
    if not require_exact_keys(value, required, "visibility_manifest", report):
        return False, set()
    ok = True
    if value["schema_version"] != "slars-zai-visibility/v1":
        report.error("Z1", "VISIBILITY_SCHEMA_VERSION_MISMATCH", str(value["schema_version"]))
        ok = False
    if value["case_id"] != protocol["blind_case"]["case_id"]:
        report.error("Z1", "VISIBILITY_CASE_ID_MISMATCH", str(value["case_id"]))
        ok = False
    visible = value["candidate_visible_artifact_ids"]
    pre_output = value["pre_output_reachable_artifact_ids"]
    forbidden = value["candidate_forbidden_artifact_ids"]
    for label, collection in (("visible", visible), ("pre_output", pre_output), ("forbidden", forbidden)):
        if not isinstance(collection, list) or not all(isinstance(item, str) for item in collection):
            report.error("Z1", "VISIBILITY_LIST_INVALID", label)
            ok = False
    if not ok:
        return False, set()
    if len(visible) != len(set(visible)) or len(pre_output) != len(set(pre_output)) or len(forbidden) != len(set(forbidden)):
        report.error("Z1", "VISIBILITY_LIST_DUPLICATE", "duplicate artifact id")
        ok = False
    unknown_ids = (set(visible) | set(pre_output) | set(forbidden)) - set(artifacts)
    if unknown_ids:
        report.error("Z1", "VISIBILITY_UNKNOWN_ARTIFACT", str(sorted(unknown_ids)))
        ok = False
    declared_visible = {item.artifact_id for item in artifacts.values() if item.record["candidate_visible"]}
    declared_pre_output = {item.artifact_id for item in artifacts.values() if item.record["pre_output_reachable"]}
    if set(visible) != declared_visible:
        report.error("Z1", "CANDIDATE_VISIBLE_SET_MISMATCH", str(sorted(set(visible) ^ declared_visible)))
        ok = False
    if set(pre_output) != declared_pre_output:
        report.error("Z1", "PREOUTPUT_REACHABLE_SET_MISMATCH", str(sorted(set(pre_output) ^ declared_pre_output)))
        ok = False
    required_pre_output = {
        role_index[role].artifact_id for role in REQUIRED_PREOUTPUT_ROLES if role in role_index
    }
    forbidden_pre_output = {
        role_index[role].artifact_id for role in FORBIDDEN_PREOUTPUT_ROLES if role in role_index
    }
    if not required_pre_output.issubset(set(pre_output)):
        report.error(
            "Z1",
            "PREOUTPUT_SCAN_SURFACE_INCOMPLETE",
            str(sorted(required_pre_output - set(pre_output))),
        )
        ok = False
    if set(pre_output) & forbidden_pre_output:
        report.error(
            "Z1",
            "POSTOUTPUT_ARTIFACT_MARKED_PREOUTPUT",
            str(sorted(set(pre_output) & forbidden_pre_output)),
        )
        ok = False
    channel_evidence_ids = {
        artifact.artifact_id
        for artifact in artifacts.values()
        if artifact.record["semantic_role"] == "CHANNEL_EVIDENCE"
    }
    invalid_channel_evidence = {
        artifact_id
        for artifact_id in channel_evidence_ids
        if (
            not artifacts[artifact_id].record["pre_output_reachable"]
            or artifacts[artifact_id].record["candidate_visible"]
        )
    }
    if invalid_channel_evidence:
        report.error(
            "Z1",
            "CHANNEL_EVIDENCE_VISIBILITY_INVALID",
            str(sorted(invalid_channel_evidence)),
        )
        ok = False
    channel_capture_records = parse_channel_evidence(run, artifacts, report)
    if channel_capture_records is None:
        ok = False
        channel_capture_records = {}
    blind_input = role_index.get("BLIND_INPUT")
    if blind_input is not None and blind_input.artifact_id not in set(visible):
        report.error("Z1", "BLIND_INPUT_NOT_CANDIDATE_VISIBLE", blind_input.artifact_id)
        ok = False
    required_forbidden = {
        role_index[role].artifact_id
        for role in ("ANSWER_KEY", "EVALUATION_RUBRIC", "SEMANTIC_REVIEW", "EXTERNAL_EVALUATION")
        if role in role_index
    }
    if not required_forbidden.issubset(set(forbidden)):
        report.error("Z1", "CANDIDATE_FORBIDDEN_SET_INCOMPLETE", str(sorted(required_forbidden - set(forbidden))))
        ok = False
    forbidden_overlap = (set(visible) | set(pre_output)) & set(forbidden)
    if forbidden_overlap:
        report.error(
            "Z1",
            "FORBIDDEN_ARTIFACT_REACHABLE",
            str(sorted(forbidden_overlap)),
        )
        ok = False
    if value["undeclared_readable_channels"] != []:
        report.error("Z1", "UNDECLARED_READABLE_CHANNEL", str(value["undeclared_readable_channels"]))
        ok = False
    channels = value["channels"]
    if not isinstance(channels, list):
        report.error("Z1", "CHANNELS_ARRAY_REQUIRED", "visibility_manifest.channels")
        ok = False
    else:
        channel_ids: set[str] = set()
        channel_evidence_by_id: dict[str, set[str]] = {}
        for index, channel in enumerate(channels):
            if not require_exact_keys(channel, {"channel_id", "status", "evidence_artifact_ids"}, f"channels[{index}]", report):
                ok = False
                continue
            channel_id = channel["channel_id"]
            if not isinstance(channel_id, str) or not channel_id:
                report.error(
                    "CONTENT",
                    "ARTIFACT_CONTENT_SCHEMA_VIOLATION",
                    f"visibility_manifest.channels[{index}].channel_id",
                )
                report.error("Z1", "CHANNEL_ID_INVALID", str(channel_id))
                ok = False
                continue
            if channel_id in channel_ids:
                report.error("Z1", "DUPLICATE_CHANNEL", str(channel_id))
                ok = False
            channel_ids.add(channel_id)
            if not isinstance(channel["status"], str) or channel["status"] not in {"CAPTURED", "DISABLED"}:
                report.error("Z1", "CHANNEL_STATUS_INVALID", str(channel["status"]))
                ok = False
            evidence_ids = channel["evidence_artifact_ids"]
            if not isinstance(evidence_ids, list) or not all(isinstance(item, str) for item in evidence_ids):
                report.error("Z1", "CHANNEL_EVIDENCE_LIST_INVALID", str(channel_id))
                ok = False
            elif set(evidence_ids) - set(artifacts):
                report.error("Z1", "CHANNEL_EVIDENCE_UNKNOWN", str(channel_id))
                ok = False
            elif not evidence_ids:
                report.error("Z1", "CHANNEL_STATUS_WITHOUT_EVIDENCE", str(channel_id))
                ok = False
            else:
                channel_evidence_by_id[channel_id] = set(evidence_ids)
        if channel_ids != REQUIRED_CHANNELS:
            report.error("Z1", "CHANNEL_CLOSURE_INCOMPLETE", str(sorted(REQUIRED_CHANNELS ^ channel_ids)))
            ok = False
        critical_channel_bindings = {
            "SOURCE": role_index.get("CANDIDATE_SOURCE"),
            "BYTECODE": role_index.get("RUN_SPECIFIC_BYTECODE"),
            "STDIN": role_index.get("BLIND_INPUT"),
            "STDERR": role_index.get("RAW_STDERR"),
            "EXIT_CODE": role_index.get("HOST_TRACE"),
        }
        for channel_id, artifact in critical_channel_bindings.items():
            declared = next(
                (
                    item
                    for item in channels
                    if isinstance(item, dict) and item.get("channel_id") == channel_id
                ),
                None,
            )
            if declared is not None and declared.get("status") != "CAPTURED":
                report.error("Z1", "CRITICAL_CHANNEL_MUST_BE_CAPTURED", channel_id)
                ok = False
            if artifact is not None and artifact.artifact_id not in channel_evidence_by_id.get(channel_id, set()):
                report.error(
                    "Z1",
                    "CRITICAL_CHANNEL_EVIDENCE_BINDING_MISSING",
                    f"{channel_id}:{artifact.artifact_id}",
                )
                ok = False
        noncritical_channels = REQUIRED_CHANNELS - set(critical_channel_bindings)
        for channel_id in sorted(noncritical_channels):
            cited = channel_evidence_by_id.get(channel_id, set()) & channel_evidence_ids
            if not cited:
                report.error("Z1", "CHANNEL_MATERIALIZATION_EVIDENCE_MISSING", channel_id)
                ok = False
                continue
            declared = next(
                (
                    item
                    for item in channels
                    if isinstance(item, dict) and item.get("channel_id") == channel_id
                ),
                None,
            )
            declared_status = declared.get("status") if declared is not None else None
            matching = {
                artifact_id
                for artifact_id in cited
                if channel_capture_records.get(artifact_id, {}).get(channel_id) == declared_status
            }
            if not matching:
                report.error("Z1", "CHANNEL_CAPTURE_RECORD_MISSING_OR_STATUS_MISMATCH", channel_id)
                ok = False
        captured_noncritical = {
            channel_id
            for captures in channel_capture_records.values()
            for channel_id in captures
        }
        if captured_noncritical != noncritical_channels:
            report.error(
                "Z1",
                "CHANNEL_CAPTURE_COVERAGE_MISMATCH",
                str(sorted(captured_noncritical ^ noncritical_channels)),
            )
            ok = False
    return ok, set(pre_output)


def parse_answer_key(
    protocol: dict[str, Any],
    role_index: dict[str, MaterializedArtifact],
    limits: dict[str, Any],
    report: Report,
) -> list[dict[str, str]] | None:
    artifact = role_index.get("ANSWER_KEY")
    if artifact is None:
        return None
    if artifact.artifact_id != protocol["blind_case"]["answer_key_artifact_id"]:
        report.error("Z2", "ANSWER_KEY_ID_MISMATCH", artifact.artifact_id)
        return None
    value = parse_artifact_json(artifact, report)
    if not require_exact_keys(value, {"schema_version", "case_id", "forbidden_material"}, "answer_key", report):
        return None
    if value["schema_version"] != "slars-zai-answer-key/v1" or value["case_id"] != protocol["blind_case"]["case_id"]:
        report.error("Z2", "ANSWER_KEY_BINDING_MISMATCH", str(value.get("case_id")))
        return None
    materials = value["forbidden_material"]
    if not isinstance(materials, list) or not materials:
        report.error("Z2", "FORBIDDEN_MATERIAL_REQUIRED", "answer_key.forbidden_material")
        return None
    if len(materials) > limits["max_forbidden_material_items"]:
        report.error("Z2", "FORBIDDEN_MATERIAL_COUNT_LIMIT_EXCEEDED", str(len(materials)))
        return None
    result: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    seen_text: set[str] = set()
    seen_normalized: dict[str, str] = {}
    seen_alnum: dict[str, str] = {}
    classes: set[str] = set()
    total_material_bytes = 0
    for index, material in enumerate(materials):
        if not require_exact_keys(material, {"material_id", "class", "text"}, f"forbidden_material[{index}]", report):
            continue
        material_id = material["material_id"]
        material_class = material["class"]
        text = material["text"]
        if not isinstance(material_id, str) or not material_id or material_id in seen_ids:
            report.error("Z2", "MATERIAL_ID_INVALID", str(material_id))
            continue
        if not isinstance(material_class, str) or material_class not in FORBIDDEN_CLASSES:
            report.error(
                "CONTENT",
                "ARTIFACT_CONTENT_SCHEMA_VIOLATION",
                f"answer_key.forbidden_material[{index}].class",
            )
            report.error("Z2", "MATERIAL_CLASS_INVALID", str(material_class))
            continue
        if not isinstance(text, str) or len(text.encode("utf-8")) < 8 or text in seen_text:
            report.error("Z2", "MATERIAL_TEXT_NOT_DISTINCTIVE", str(material_id))
            continue
        total_material_bytes += len(text.encode("utf-8"))
        if total_material_bytes > limits["max_forbidden_material_bytes_total"]:
            report.error(
                "Z2",
                "FORBIDDEN_MATERIAL_BYTES_LIMIT_EXCEEDED",
                str(total_material_bytes),
            )
            return None
        normalized_fingerprint = normalize_text(text)
        alnum_fingerprint = alnum_text(text)
        if len(alnum_fingerprint.encode("utf-8")) < 8:
            report.error("Z2", "MATERIAL_FINGERPRINT_NOT_DISTINCTIVE", str(material_id))
            continue
        collision = False
        if normalized_fingerprint in seen_normalized:
            report.error(
                "Z2",
                "MATERIAL_NORMALIZED_FINGERPRINT_COLLISION",
                f"{seen_normalized[normalized_fingerprint]}:{material_id}",
            )
            collision = True
        if alnum_fingerprint in seen_alnum:
            report.error(
                "Z2",
                "MATERIAL_ALNUM_FINGERPRINT_COLLISION",
                f"{seen_alnum[alnum_fingerprint]}:{material_id}",
            )
            collision = True
        if collision:
            continue
        seen_ids.add(material_id)
        seen_text.add(text)
        seen_normalized[normalized_fingerprint] = material_id
        seen_alnum[alnum_fingerprint] = material_id
        classes.add(material_class)
        result.append({"material_id": material_id, "class": material_class, "text": text})
    if classes != FORBIDDEN_CLASSES:
        report.error("Z2", "FORBIDDEN_MATERIAL_CLASSES_INCOMPLETE", str(sorted(FORBIDDEN_CLASSES - classes)))
    return result if len(result) == len(materials) and classes == FORBIDDEN_CLASSES else None


def normalize_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def alnum_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return "".join(character for character in normalized if character.isalnum())


def ascii_byte_casefold_whitespace(value: bytes) -> bytes:
    output = bytearray()
    pending_space = False
    for byte in value:
        if byte in b" \t\n\r\v\f":
            pending_space = bool(output)
            continue
        if pending_space:
            output.append(0x20)
            pending_space = False
        output.append(byte + 32 if 0x41 <= byte <= 0x5A else byte)
    return bytes(output)


def ascii_byte_alnum(value: bytes) -> bytes:
    return bytes(
        byte + 32 if 0x41 <= byte <= 0x5A else byte
        for byte in value
        if 0x30 <= byte <= 0x39 or 0x41 <= byte <= 0x5A or 0x61 <= byte <= 0x7A
    )


def decode_json_unicode_escapes(value: bytes) -> bytes:
    output = bytearray()
    index = 0
    while index < len(value):
        if index + 6 <= len(value) and value[index : index + 2] == b"\\u":
            digits = value[index + 2 : index + 6]
            try:
                codepoint = int(digits, 16)
            except ValueError:
                codepoint = -1
            consumed = 6
            if 0xD800 <= codepoint <= 0xDBFF and index + 12 <= len(value):
                second_prefix = value[index + 6 : index + 8]
                second_digits = value[index + 8 : index + 12]
                try:
                    low = int(second_digits, 16)
                except ValueError:
                    low = -1
                if second_prefix == b"\\u" and 0xDC00 <= low <= 0xDFFF:
                    codepoint = 0x10000 + ((codepoint - 0xD800) << 10) + (low - 0xDC00)
                    consumed = 12
            if 0 <= codepoint <= 0x10FFFF and not 0xD800 <= codepoint <= 0xDFFF:
                output.extend(chr(codepoint).encode("utf-8"))
                index += consumed
                continue
        output.append(value[index])
        index += 1
    return bytes(output)


def decoded_scan_surfaces(value: bytes) -> dict[str, bytes]:
    surfaces = {"RAW": value}
    frontier = {"RAW": value}
    for depth in (1, 2):
        next_frontier: dict[str, bytes] = {}
        for parent_name, parent in frontier.items():
            for decoder_name, decoded in (
                ("URL_PERCENT", unquote_to_bytes(parent)),
                ("JSON_UNICODE_ESCAPE", decode_json_unicode_escapes(parent)),
            ):
                name = f"{parent_name}_THEN_{decoder_name}_L{depth}"
                if decoded != parent and decoded not in surfaces.values() and decoded not in next_frontier.values():
                    next_frontier[name] = decoded
        surfaces.update(next_frontier)
        frontier = next_frontier
        if not frontier:
            break
    return surfaces


def material_representations(text: str) -> dict[str, bytes]:
    raw = text.encode("utf-8")
    json_escaped = json.dumps(text, ensure_ascii=True)[1:-1].encode("ascii")
    return {
        "EXACT_UTF8": raw,
        "HEX_LOWER": raw.hex().encode("ascii"),
        "HEX_UPPER": raw.hex().upper().encode("ascii"),
        "BASE64_STANDARD": base64.b64encode(raw),
        "URL_PERCENT": quote(text, safe="").encode("ascii"),
        "JSON_ESCAPE": json_escaped,
        "ROT13": codecs.encode(text, "rot_13").encode("utf-8"),
    }


def scan_forbidden_material(
    artifacts: dict[str, MaterializedArtifact],
    scan_surface: set[str],
    materials: list[dict[str, str]],
    limits: dict[str, Any],
    report: Report,
) -> bool:
    ok = True
    scan_bytes = sum(
        len(artifacts[artifact_id].data)
        + len(artifacts[artifact_id].record["artifact_id"].encode("utf-8"))
        + len(artifacts[artifact_id].record["relative_path"].encode("utf-8"))
        + len(artifacts[artifact_id].record["media_type"].encode("utf-8"))
        for artifact_id in scan_surface
        if artifact_id in artifacts
    )
    scan_product = scan_bytes * len(materials) * SCAN_COST_MULTIPLIER
    if scan_product > limits["max_scan_product_bytes"]:
        report.error("Z2", "SCAN_PRODUCT_LIMIT_EXCEEDED", str(scan_product))
        return False
    for artifact_id in sorted(scan_surface):
        artifact = artifacts.get(artifact_id)
        if artifact is None:
            report.error("Z2", "SCAN_SURFACE_ARTIFACT_MISSING", artifact_id)
            ok = False
            continue
        metadata_text = "\n".join(
            [artifact.record["artifact_id"], artifact.record["relative_path"], artifact.record["media_type"]]
        )
        combined = artifact.data + b"\n" + metadata_text.encode("utf-8")
        surfaces = decoded_scan_surfaces(combined)
        for material in materials:
            matches: set[str] = set()
            for mode, representation in material_representations(material["text"]).items():
                if representation and representation in combined:
                    matches.add(mode)
            marker_alnum = alnum_text(material["text"])
            try:
                marker_ascii = material["text"].encode("ascii")
            except UnicodeEncodeError:
                marker_ascii = b""
            for surface_name, surface in surfaces.items():
                decoded = surface.decode("utf-8", errors="replace")
                mode_prefix = "" if surface_name == "RAW" else surface_name + ":"
                if material["text"].encode("utf-8") in surface:
                    matches.add(mode_prefix + "EXACT_UTF8")
                if normalize_text(material["text"]) in normalize_text(decoded):
                    matches.add(mode_prefix + "UNICODE_NFKC_CASEFOLD_WHITESPACE_COLLAPSE")
                if marker_alnum and marker_alnum in alnum_text(decoded):
                    matches.add(mode_prefix + "UNICODE_NFKC_ALNUM_COLLAPSE")
                if marker_ascii:
                    if ascii_byte_casefold_whitespace(marker_ascii) in ascii_byte_casefold_whitespace(surface):
                        matches.add(mode_prefix + "ASCII_BYTE_CASEFOLD_WHITESPACE_COLLAPSE")
                    if ascii_byte_alnum(marker_ascii) in ascii_byte_alnum(surface):
                        matches.add(mode_prefix + "ASCII_BYTE_ALNUM_COLLAPSE")
            for mode in sorted(matches):
                report.scan_matches.append(
                    {
                        "artifact_id": artifact_id,
                        "material_id": material["material_id"],
                        "class": material["class"],
                        "mode": mode,
                    }
                )
                report.error(
                    "Z2",
                    "FORBIDDEN_MATERIAL_MATCH",
                    f"{artifact_id}:{material['material_id']}:{material['class']}:{mode}",
                )
                ok = False
    return ok


def scan_forbidden_prekey_argv(
    run: dict[str, Any],
    materials: list[dict[str, str]],
    report: Report,
) -> bool:
    """Scan the VM/runner-visible argv recorded in pre-key events."""

    key_index = next(
        (index for index, event in enumerate(run["events"]) if event["event_type"] == "KEY_FIRST_ACCESS"),
        len(run["events"]),
    )
    argv_text = "\n".join(
        argument for event in run["events"][:key_index] for argument in event["argv"]
    )
    combined = argv_text.encode("utf-8")
    ok = True
    for material in materials:
        matches: set[str] = set()
        for mode, representation in material_representations(material["text"]).items():
            if representation and representation in combined:
                matches.add(mode)
        if normalize_text(material["text"]) in normalize_text(argv_text):
            matches.add("UNICODE_NFKC_CASEFOLD_WHITESPACE_COLLAPSE")
        marker_alnum = alnum_text(material["text"])
        if marker_alnum and marker_alnum in alnum_text(argv_text):
            matches.add("UNICODE_NFKC_ALNUM_COLLAPSE")
        for mode in sorted(matches):
            report.scan_matches.append(
                {
                    "artifact_id": "RUN_EVENT_PREKEY_ARGV",
                    "material_id": material["material_id"],
                    "class": material["class"],
                    "mode": mode,
                }
            )
            report.error(
                "Z2",
                "FORBIDDEN_MATERIAL_MATCH",
                f"RUN_EVENT_PREKEY_ARGV:{material['material_id']}:{material['class']}:{mode}",
            )
            ok = False
    return ok


def verify_host_trace(
    run: dict[str, Any],
    artifacts: dict[str, MaterializedArtifact],
    role_index: dict[str, MaterializedArtifact],
    report: Report,
) -> bool:
    trace = role_index.get("HOST_TRACE")
    if trace is None:
        return False
    if trace.artifact_id != run["execution"]["host_trace_artifact_id"]:
        report.error("Z3", "HOST_TRACE_ID_MISMATCH", trace.artifact_id)
        return False
    value = parse_artifact_json(trace, report)
    required = {
        "schema_version",
        "run_id",
        "host_semantic_transformation_observed",
        "output_selection_or_rewrite_observed",
        "operations",
    }
    if not require_exact_keys(value, required, "host_trace", report):
        return False
    ok = True
    if value["schema_version"] != "slars-zai-host-trace/v1" or value["run_id"] != run["run_id"]:
        report.error("Z3", "HOST_TRACE_BINDING_MISMATCH", str(value.get("run_id")))
        ok = False
    if value["host_semantic_transformation_observed"] is not False:
        report.error("Z3", "HOST_SEMANTIC_TRANSFORMATION_DETECTED", "host_trace")
        ok = False
    if value["output_selection_or_rewrite_observed"] is not False:
        report.error("Z3", "OUTPUT_SELECTION_OR_REWRITE_DETECTED", "host_trace")
        ok = False
    operations = value["operations"]
    if not isinstance(operations, list) or not operations:
        report.error("Z3", "HOST_OPERATIONS_REQUIRED", "host_trace.operations")
        return False
    seen_ops: set[str] = set()
    for index, operation in enumerate(operations, start=1):
        if not require_exact_keys(operation, {"sequence", "op", "input_artifact_ids", "output_artifact_ids"}, f"host_trace.operations[{index-1}]", report):
            ok = False
            continue
        if operation["sequence"] != index:
            report.error("Z3", "HOST_OPERATION_SEQUENCE_INVALID", str(operation["sequence"]))
            ok = False
        op = operation["op"]
        if not isinstance(op, str) or op not in ALLOWED_HOST_OPERATIONS:
            report.error("Z3", "HOST_OPERATION_NOT_MECHANICAL", str(op))
            ok = False
        else:
            seen_ops.add(op)
        inputs = operation["input_artifact_ids"]
        outputs = operation["output_artifact_ids"]
        if not isinstance(inputs, list) or not isinstance(outputs, list):
            report.error("Z3", "HOST_OPERATION_ARTIFACT_LIST_INVALID", str(op))
            ok = False
            refs: list[Any] = []
        else:
            refs = inputs + outputs
        if not all(isinstance(item, str) and item in artifacts for item in refs):
            report.error("Z3", "HOST_OPERATION_ARTIFACT_UNKNOWN", str(op))
            ok = False
    required_ops = {"EXEC_SIGMAC", "EXEC_SIGMA_VM", "CAPTURE_STDOUT", "CAPTURE_STDERR", "FREEZE_BYTES"}
    if not required_ops.issubset(seen_ops):
        report.error("Z3", "HOST_REQUIRED_OPERATION_MISSING", str(sorted(required_ops - seen_ops)))
        ok = False
    forbidden_runtime_refs = {
        role_index[role].artifact_id
        for role in ("ANSWER_KEY", "EVALUATION_RUBRIC", "SEMANTIC_REVIEW", "EXTERNAL_EVALUATION")
        if role in role_index
    }
    for operation in operations:
        if not isinstance(operation, dict):
            continue
        inputs = operation.get("input_artifact_ids", [])
        outputs = operation.get("output_artifact_ids", [])
        refs = inputs + outputs if isinstance(inputs, list) and isinstance(outputs, list) else []
        leaked = {item for item in refs if isinstance(item, str)} & forbidden_runtime_refs
        if leaked:
            report.error("Z3", "HOST_TRACE_REFERENCES_POSTOUTPUT_SECRET", str(sorted(leaked)))
            ok = False
        op = operation.get("op")
    required_topology = {
        "EXEC_SIGMAC": (
            {role_index["CANDIDATE_SOURCE"].artifact_id, role_index["SIGMAC_BINARY"].artifact_id},
            {role_index["RUN_SPECIFIC_BYTECODE"].artifact_id},
        ),
        "EXEC_SIGMA_VM": (
            {
                role_index["RUN_SPECIFIC_BYTECODE"].artifact_id,
                role_index["BLIND_INPUT"].artifact_id,
                role_index["SIGMA_VM_BINARY"].artifact_id,
            },
            {role_index["RAW_STDOUT"].artifact_id, role_index["RAW_STDERR"].artifact_id},
        ),
        "CAPTURE_STDOUT": ({role_index["RAW_STDOUT"].artifact_id}, set()),
        "CAPTURE_STDERR": ({role_index["RAW_STDERR"].artifact_id}, set()),
        "FREEZE_BYTES": (
            {role_index["RAW_STDOUT"].artifact_id, role_index["RAW_STDERR"].artifact_id},
            set(),
        ),
    }
    for op, (required_inputs, required_outputs) in required_topology.items():
        matching = [item for item in operations if isinstance(item, dict) and item.get("op") == op]
        if len(matching) != 1:
            report.error("Z3", "HOST_OPERATION_CARDINALITY_INVALID", f"{op}:{len(matching)}")
            ok = False
        if not any(
            isinstance(item.get("input_artifact_ids"), list)
            and isinstance(item.get("output_artifact_ids"), list)
            and required_inputs
            == {
                value for value in item["input_artifact_ids"] if isinstance(value, str)
            }
            and len(required_inputs) == len(item["input_artifact_ids"])
            and required_outputs
            == {
                value for value in item["output_artifact_ids"] if isinstance(value, str)
            }
            and len(required_outputs) == len(item["output_artifact_ids"])
            for item in matching
        ):
            report.error("Z3", "HOST_OPERATION_TOPOLOGY_MISMATCH", op)
            ok = False
    operation_order = [item.get("op") for item in operations if isinstance(item, dict)]
    ordered_required = ["EXEC_SIGMAC", "EXEC_SIGMA_VM", "CAPTURE_STDOUT", "CAPTURE_STDERR", "FREEZE_BYTES"]
    try:
        positions = [operation_order.index(op) for op in ordered_required]
    except ValueError:
        positions = []
    if not positions or positions != sorted(positions) or len(set(positions)) != len(positions):
        report.error("Z3", "HOST_OPERATION_ORDER_INVALID", str(operation_order))
        ok = False
    for operation in operations:
        if not isinstance(operation, dict) or operation.get("op") != "HASH_BYTES":
            continue
        inputs = operation.get("input_artifact_ids")
        outputs = operation.get("output_artifact_ids")
        hash_inputs_valid = (
            isinstance(inputs, list)
            and all(
                isinstance(item, str)
                and item in artifacts
                and artifacts[item].record["pre_output_reachable"]
                for item in inputs
            )
        )
        if not hash_inputs_valid or outputs != []:
            report.error("Z3", "HOST_HASH_OPERATION_TOPOLOGY_INVALID", str(operation))
            ok = False
    return ok


def verify_semantic_review(
    protocol: dict[str, Any],
    run: dict[str, Any],
    artifacts: dict[str, MaterializedArtifact],
    role_index: dict[str, MaterializedArtifact],
    scan_surface: set[str],
    report: Report,
) -> bool:
    artifact = role_index.get("SEMANTIC_REVIEW")
    if artifact is None:
        return False
    if artifact.artifact_id != protocol["review"]["semantic_review_artifact_id"]:
        report.error("Z2", "SEMANTIC_REVIEW_ID_MISMATCH", artifact.artifact_id)
        return False
    value = parse_artifact_json(artifact, report)
    required = {
        "schema_version",
        "run_id",
        "reviewer_id",
        "status",
        "reviewed_artifacts",
        "scan_surface_sha256",
        "findings",
    }
    if not require_exact_keys(value, required, "semantic_review", report):
        return False
    ok = True
    if value["schema_version"] != "slars-zai-semantic-review/v2" or value["run_id"] != run["run_id"]:
        report.error("Z2", "SEMANTIC_REVIEW_BINDING_MISMATCH", str(value.get("run_id")))
        ok = False
    if value["reviewer_id"] != protocol["roles"]["auditor"]:
        report.error("Z2", "SEMANTIC_REVIEWER_ID_MISMATCH", str(value["reviewer_id"]))
        ok = False
    if value["status"] != "PASS" or run["scan"]["semantic_review_status"] != "PASS":
        report.error("Z2", "SEMANTIC_REVIEW_NOT_PASS", str(value["status"]))
        ok = False
    expected_reviewed = [
        {"artifact_id": artifact_id, "sha256": artifacts[artifact_id].sha256}
        for artifact_id in sorted(scan_surface)
    ]
    reviewed = value["reviewed_artifacts"]
    reviewed_valid = isinstance(reviewed, list)
    if reviewed_valid:
        for index, item in enumerate(reviewed):
            if not require_exact_keys(
                item,
                {"artifact_id", "sha256"},
                f"semantic_review.reviewed_artifacts[{index}]",
                report,
            ):
                reviewed_valid = False
    if not reviewed_valid or reviewed != expected_reviewed:
        report.error("Z2", "SEMANTIC_REVIEW_SURFACE_OR_HASH_MISMATCH", "reviewed_artifacts")
        ok = False
    expected_surface_sha = sha256_bytes(canonical_json_bytes(expected_reviewed))
    if value["scan_surface_sha256"] != expected_surface_sha:
        report.error("Z2", "SEMANTIC_REVIEW_MANIFEST_HASH_MISMATCH", "scan_surface_sha256")
        ok = False
    required_findings = {
        "supportor_answer_observed",
        "prewritten_answer_observed",
        "prewritten_hypothesis_observed",
        "prewritten_reasoning_path_observed",
        "prewritten_conclusion_observed",
        "semantic_equivalent_injection_observed",
        "host_semantic_transformation_observed",
        "output_selection_or_rewrite_observed",
        "unknown_readable_channel_observed",
    }
    if not require_exact_keys(value["findings"], required_findings, "semantic_review.findings", report):
        return False
    if any(finding is not False for finding in value["findings"].values()):
        report.error("Z2", "SEMANTIC_INJECTION_OR_UNKNOWN_CHANNEL_DETECTED", str(value["findings"]))
        ok = False
    return ok


def verify_event_chain(
    protocol: dict[str, Any],
    run: dict[str, Any],
    artifacts: dict[str, MaterializedArtifact],
    role_index: dict[str, MaterializedArtifact],
    scan_surface: set[str],
    report: Report,
) -> bool:
    events = run["events"]
    ok = True
    if tuple(event["event_type"] for event in events) != REQUIRED_EVENTS:
        report.error("EVENT", "REQUIRED_EVENT_ORDER_MISMATCH", str([event["event_type"] for event in events]))
        return False
    actor_for_event = {
        "PROTOCOL_FREEZE": protocol["roles"]["test_designer"],
        "CANDIDATE_FREEZE": protocol["roles"]["candidate_builder"],
        "BLIND_CASE_COMMIT": protocol["roles"]["test_designer"],
        "CHANNEL_SNAPSHOT": protocol["roles"]["auditor"],
        "RUN_START": protocol["roles"]["runner"],
        "SIGMAC_COMPLETE": protocol["roles"]["runner"],
        "VM_OUTPUT_FROZEN": protocol["roles"]["runner"],
        "KEY_FIRST_ACCESS": protocol["roles"]["key_custodian"],
        "SEMANTIC_REVIEW": protocol["roles"]["auditor"],
        "EXTERNAL_EVALUATION": protocol["roles"]["evaluator"],
    }
    previous_hash: str | None = None
    previous_time: datetime | None = None
    for index, event in enumerate(events, start=1):
        event_type = event["event_type"]
        if event["sequence"] != index:
            report.error("EVENT", "EVENT_SEQUENCE_INVALID", str(event["sequence"]))
            ok = False
        if event["run_id"] != run["run_id"]:
            report.error("EVENT", "EVENT_RUN_ID_MISMATCH", event_type)
            ok = False
        if event["actor_id"] != actor_for_event[event_type]:
            report.error("EVENT", "EVENT_ACTOR_NOT_AUTHORIZED", event_type)
            ok = False
        event_time = parse_utc(event["occurred_at_utc"])
        if event_time is None:
            report.error("EVENT", "EVENT_TIMESTAMP_INVALID", event_type)
            ok = False
        elif previous_time is not None and event_time < previous_time:
            report.error("EVENT", "EVENT_TIMESTAMP_REVERSED", event_type)
            ok = False
        previous_time = event_time or previous_time
        if event["previous_event_sha256"] != previous_hash:
            report.error("EVENT", "EVENT_PREVIOUS_HASH_MISMATCH", event_type)
            ok = False
        event_without_hash = dict(event)
        reported_hash = event_without_hash.pop("event_sha256")
        actual_hash = sha256_bytes(canonical_json_bytes(event_without_hash))
        if reported_hash != actual_hash:
            report.error("EVENT", "EVENT_HASH_MISMATCH", event_type)
            ok = False
        previous_hash = reported_hash
        refs = event["input_artifact_ids"] + event["output_artifact_ids"]
        if set(refs) - set(artifacts):
            report.error("EVENT", "EVENT_ARTIFACT_UNKNOWN", event_type)
            ok = False
        if event["process_artifact_id"] is not None and event["process_artifact_id"] not in artifacts:
            report.error("EVENT", "EVENT_PROCESS_ARTIFACT_UNKNOWN", event_type)
            ok = False
        binding_ids = set(refs)
        if event["process_artifact_id"] is not None:
            binding_ids.add(event["process_artifact_id"])
        if binding_ids.issubset(artifacts):
            bindings = []
            for direction, artifact_ids in (
                ("INPUT", event["input_artifact_ids"]),
                ("OUTPUT", event["output_artifact_ids"]),
            ):
                for artifact_id in artifact_ids:
                    bound = artifacts[artifact_id]
                    bindings.append(
                        {
                            "direction": direction,
                            "artifact_id": artifact_id,
                            "sha256": bound.sha256,
                            "byte_count": len(bound.data),
                        }
                    )
            if event["process_artifact_id"] is not None:
                process_id = event["process_artifact_id"]
                bound = artifacts[process_id]
                bindings.append(
                    {
                        "direction": "PROCESS",
                        "artifact_id": process_id,
                        "sha256": bound.sha256,
                        "byte_count": len(bound.data),
                    }
                )
            bindings.sort(key=lambda item: (item["direction"], item["artifact_id"]))
            expected_binding_hash = sha256_bytes(canonical_json_bytes(bindings))
            if event["artifact_bindings_sha256"] != expected_binding_hash:
                report.error("EVENT", "EVENT_ARTIFACT_BINDINGS_MISMATCH", event_type)
                ok = False
    candidate_source = role_index["CANDIDATE_SOURCE"]
    blind_input = role_index["BLIND_INPUT"]
    answer_key = role_index["ANSWER_KEY"]
    visibility = role_index["VISIBILITY_MANIFEST"]
    bytecode = role_index["RUN_SPECIFIC_BYTECODE"]
    stdout = role_index["RAW_STDOUT"]
    stderr = role_index["RAW_STDERR"]
    host_trace = role_index["HOST_TRACE"]
    semantic_review = role_index["SEMANTIC_REVIEW"]
    external = role_index["EXTERNAL_EVALUATION"]
    rubric = role_index["EVALUATION_RUBRIC"]
    sigmac = role_index["SIGMAC_BINARY"]
    vm = role_index["SIGMA_VM_BINARY"]
    channel_evidence_ids = {
        artifact.artifact_id
        for artifact in artifacts.values()
        if artifact.record["semantic_role"] == "CHANNEL_EVIDENCE"
    }
    required_outputs = {
        "PROTOCOL_FREEZE": {rubric.artifact_id},
        "CANDIDATE_FREEZE": {candidate_source.artifact_id},
        "BLIND_CASE_COMMIT": {blind_input.artifact_id, answer_key.artifact_id},
        "CHANNEL_SNAPSHOT": {visibility.artifact_id} | channel_evidence_ids,
        "SIGMAC_COMPLETE": {bytecode.artifact_id},
        "VM_OUTPUT_FROZEN": {stdout.artifact_id, stderr.artifact_id, host_trace.artifact_id},
        "SEMANTIC_REVIEW": {semantic_review.artifact_id},
        "EXTERNAL_EVALUATION": {external.artifact_id},
    }
    by_type = {event["event_type"]: event for event in events}
    for event_type, output_ids in required_outputs.items():
        if not output_ids.issubset(set(by_type[event_type]["output_artifact_ids"])):
            report.error("EVENT", "EVENT_REQUIRED_OUTPUT_MISSING", event_type)
            ok = False
    required_inputs = {
        "RUN_START": {
            candidate_source.artifact_id,
            blind_input.artifact_id,
            role_index["RUNNER_SOURCE"].artifact_id,
            sigmac.artifact_id,
            vm.artifact_id,
        },
        "SIGMAC_COMPLETE": {candidate_source.artifact_id},
        "VM_OUTPUT_FROZEN": {bytecode.artifact_id, blind_input.artifact_id},
        "KEY_FIRST_ACCESS": {answer_key.artifact_id},
        "SEMANTIC_REVIEW": set(scan_surface) | {answer_key.artifact_id, stdout.artifact_id},
        "EXTERNAL_EVALUATION": {answer_key.artifact_id, rubric.artifact_id, stdout.artifact_id},
    }
    for event_type, input_ids in required_inputs.items():
        if not input_ids.issubset(set(by_type[event_type]["input_artifact_ids"])):
            report.error("EVENT", "EVENT_REQUIRED_INPUT_MISSING", event_type)
            ok = False
    exact_event_topology = {
        "PROTOCOL_FREEZE": (set(), {rubric.artifact_id}, None, [], None),
        "CANDIDATE_FREEZE": (set(), {candidate_source.artifact_id}, None, [], None),
        "BLIND_CASE_COMMIT": (
            set(),
            {blind_input.artifact_id, answer_key.artifact_id},
            None,
            [],
            None,
        ),
        "CHANNEL_SNAPSHOT": (
            set(),
            {visibility.artifact_id} | channel_evidence_ids,
            None,
            [],
            None,
        ),
        "RUN_START": (
            {
                candidate_source.artifact_id,
                blind_input.artifact_id,
                role_index["RUNNER_SOURCE"].artifact_id,
                sigmac.artifact_id,
                vm.artifact_id,
            },
            set(),
            None,
            [],
            None,
        ),
        "SIGMAC_COMPLETE": (
            {candidate_source.artifact_id},
            {bytecode.artifact_id},
            sigmac.artifact_id,
            [candidate_source.record["relative_path"], bytecode.record["relative_path"]],
            0,
        ),
        "VM_OUTPUT_FROZEN": (
            {bytecode.artifact_id, blind_input.artifact_id},
            {stdout.artifact_id, stderr.artifact_id, host_trace.artifact_id},
            vm.artifact_id,
            [bytecode.record["relative_path"]],
            0,
        ),
        "KEY_FIRST_ACCESS": ({answer_key.artifact_id}, set(), None, [], None),
        "SEMANTIC_REVIEW": (
            set(scan_surface) | {answer_key.artifact_id, stdout.artifact_id},
            {semantic_review.artifact_id},
            None,
            [],
            None,
        ),
        "EXTERNAL_EVALUATION": (
            {answer_key.artifact_id, rubric.artifact_id, stdout.artifact_id},
            {external.artifact_id},
            None,
            [],
            None,
        ),
    }
    for event_type, (expected_inputs, expected_outputs, expected_process, expected_argv, expected_rc) in exact_event_topology.items():
        event = by_type[event_type]
        if set(event["input_artifact_ids"]) != expected_inputs:
            report.error("EVENT", "EVENT_INPUT_SET_MISMATCH", event_type)
            ok = False
        if set(event["output_artifact_ids"]) != expected_outputs:
            report.error("EVENT", "EVENT_OUTPUT_SET_MISMATCH", event_type)
            ok = False
        if event["process_artifact_id"] != expected_process:
            report.error("EVENT", "EVENT_PROCESS_BINDING_MISMATCH", event_type)
            ok = False
        if event["argv"] != expected_argv:
            report.error("EVENT", "EVENT_ARGV_NOT_CANONICAL", event_type)
            ok = False
        if event["rc"] != expected_rc:
            report.error("EVENT", "EVENT_RC_BINDING_MISMATCH", event_type)
            ok = False
    key_access_index = REQUIRED_EVENTS.index("KEY_FIRST_ACCESS")
    forbidden_argv_artifacts = {
        role_index[role].artifact_id: role_index[role].record["relative_path"]
        for role in ("ANSWER_KEY", "EVALUATION_RUBRIC", "SEMANTIC_REVIEW", "EXTERNAL_EVALUATION")
    }
    for event in events[:key_access_index]:
        canonical_argv = {
            "PROTOCOL_FREEZE": [],
            "CANDIDATE_FREEZE": [],
            "BLIND_CASE_COMMIT": [],
            "CHANNEL_SNAPSHOT": [],
            "RUN_START": [],
            "SIGMAC_COMPLETE": [
                candidate_source.record["relative_path"],
                bytecode.record["relative_path"],
            ],
            "VM_OUTPUT_FROZEN": [bytecode.record["relative_path"]],
        }[event["event_type"]]
        if event["argv"] != canonical_argv:
            report.error("Z3", "EVENT_ARGV_NOT_CANONICAL", event["event_type"])
            ok = False
        if answer_key.artifact_id in event["input_artifact_ids"]:
            report.error("Z4", "ANSWER_KEY_INPUT_BEFORE_FIRST_ACCESS", event["event_type"])
            ok = False
        forbidden_argv_values = set(forbidden_argv_artifacts) | set(forbidden_argv_artifacts.values())
        leaked_argv = {
            argument
            for argument in event["argv"]
            if any(secret in argument for secret in forbidden_argv_values)
        }
        if leaked_argv:
            report.error("Z4", "POSTOUTPUT_SECRET_IN_PREKEY_ARGV", str(sorted(leaked_argv)))
            ok = False
    if answer_key.artifact_id not in by_type["KEY_FIRST_ACCESS"]["input_artifact_ids"]:
        report.error("EVENT", "KEY_ACCESS_INPUT_MISSING", answer_key.artifact_id)
        ok = False
    compile_event = by_type["SIGMAC_COMPLETE"]
    vm_event = by_type["VM_OUTPUT_FROZEN"]
    if compile_event["process_artifact_id"] != sigmac.artifact_id or compile_event["rc"] != 0:
        report.error("Z3", "SIGMAC_EVENT_BINDING_FAIL", str(compile_event["rc"]))
        ok = False
    if vm_event["process_artifact_id"] != vm.artifact_id or vm_event["rc"] != 0:
        report.error("Z3", "VM_EVENT_BINDING_FAIL", str(vm_event["rc"]))
        ok = False
    if candidate_source.record["relative_path"] not in compile_event["argv"] or bytecode.record["relative_path"] not in compile_event["argv"]:
        report.error("Z3", "SIGMAC_ARGV_BINDING_FAIL", str(compile_event["argv"]))
        ok = False
    if bytecode.record["relative_path"] not in vm_event["argv"]:
        report.error("Z3", "VM_ARGV_BINDING_FAIL", str(vm_event["argv"]))
        ok = False
    locked_at = parse_utc(protocol["locked_at_utc"])
    frozen_at = parse_utc(protocol["candidate"]["frozen_at_utc"])
    committed_at = parse_utc(protocol["blind_case"]["case_committed_at_utc"])
    event_times = {event["event_type"]: parse_utc(event["occurred_at_utc"]) for event in events}
    if None in {locked_at, frozen_at, committed_at}:
        report.error("EVENT", "PROTOCOL_TIMESTAMPS_UNAVAILABLE", "lock/freeze/commit")
        ok = False
    else:
        if not (locked_at <= frozen_at < committed_at):
            report.error("EVENT", "LOCK_FREEZE_COMMIT_ORDER_INVALID", "expected lock <= freeze < commit")
            ok = False
        if (
            by_type["PROTOCOL_FREEZE"]["occurred_at_utc"] != protocol["locked_at_utc"]
            or by_type["CANDIDATE_FREEZE"]["occurred_at_utc"]
            != protocol["candidate"]["frozen_at_utc"]
            or by_type["BLIND_CASE_COMMIT"]["occurred_at_utc"]
            != protocol["blind_case"]["case_committed_at_utc"]
        ):
            report.error("EVENT", "PROTOCOL_EVENT_TIMESTAMP_BINDING_FAIL", "lock/freeze/commit")
            ok = False
    ordered_times = (
        event_times.get("VM_OUTPUT_FROZEN"),
        event_times.get("KEY_FIRST_ACCESS"),
        event_times.get("SEMANTIC_REVIEW"),
        event_times.get("EXTERNAL_EVALUATION"),
    )
    if any(value is None for value in ordered_times) or not (
        ordered_times[0] < ordered_times[1] <= ordered_times[2] <= ordered_times[3]
    ):
        report.error("Z4", "OUTPUT_KEY_EVALUATION_ORDER_INVALID", "output must freeze before key access")
        ok = False
    return ok


def verify_execution(
    protocol: dict[str, Any],
    run: dict[str, Any],
    role_index: dict[str, MaterializedArtifact],
    report: Report,
) -> bool:
    execution = run["execution"]
    ok = True
    expected_ids = {
        "bytecode_artifact_id": role_index["RUN_SPECIFIC_BYTECODE"].artifact_id,
        "raw_stdout_artifact_id": role_index["RAW_STDOUT"].artifact_id,
        "raw_stderr_artifact_id": role_index["RAW_STDERR"].artifact_id,
        "host_trace_artifact_id": role_index["HOST_TRACE"].artifact_id,
    }
    for key, expected in expected_ids.items():
        if execution[key] != expected:
            report.error("Z3", "EXECUTION_ARTIFACT_BINDING_FAIL", key)
            ok = False
    if execution["sigmac_rc"] != 0 or execution["vm_rc"] != 0:
        report.error("Z3", "NATIVE_CHAIN_RC_NONZERO", f"sigmac={execution['sigmac_rc']} vm={execution['vm_rc']}")
        ok = False
    if execution["attempt_count"] != 1:
        report.error("Z3", "ATTEMPT_COUNT_INVALID", str(execution["attempt_count"]))
        ok = False
    if execution["host_semantic_transformation_observed"] is not False:
        report.error("Z3", "HOST_SEMANTIC_TRANSFORMATION_DETECTED", "run.execution")
        ok = False
    if execution["candidate_output_is_raw_vm_stdout"] is not True:
        report.error("Z3", "RAW_VM_STDOUT_BINDING_MISSING", "run.execution")
        ok = False
    if execution["output_selection_or_rewrite_observed"] is not False:
        report.error("Z3", "OUTPUT_SELECTION_OR_REWRITE_DETECTED", "run.execution")
        ok = False
    stdout = role_index["RAW_STDOUT"].record
    if stdout["origin_role"] != "SIGMA_VM" or stdout["stage"] != "OUTPUT":
        report.error("Z3", "RAW_STDOUT_ORIGIN_INVALID", str(stdout["origin_role"]))
        ok = False
    return ok


def verify_external_evaluation(
    protocol: dict[str, Any],
    run: dict[str, Any],
    role_index: dict[str, MaterializedArtifact],
    report: Report,
) -> bool:
    artifact = role_index.get("EXTERNAL_EVALUATION")
    if artifact is None:
        return False
    if artifact.artifact_id != protocol["review"]["external_evaluation_artifact_id"]:
        report.error("Z4", "EXTERNAL_EVALUATION_ID_MISMATCH", artifact.artifact_id)
        return False
    value = parse_artifact_json(artifact, report)
    required = {
        "schema_version",
        "run_id",
        "evaluator_id",
        "raw_stdout_sha256",
        "answer_key_sha256",
        "rubric_sha256",
        "status",
    }
    if not require_exact_keys(value, required, "external_evaluation", report):
        return False
    ok = True
    external = run["external_evaluation"]
    stdout_sha = role_index["RAW_STDOUT"].sha256
    answer_sha = role_index["ANSWER_KEY"].sha256
    rubric_sha = role_index["EVALUATION_RUBRIC"].sha256
    expected = {
        "schema_version": "slars-zai-external-evaluation/v1",
        "run_id": run["run_id"],
        "evaluator_id": protocol["roles"]["evaluator"],
        "raw_stdout_sha256": stdout_sha,
        "answer_key_sha256": answer_sha,
        "rubric_sha256": rubric_sha,
    }
    for key, expected_value in expected.items():
        if value[key] != expected_value:
            report.error("Z4", "EXTERNAL_REPORT_BINDING_MISMATCH", key)
            ok = False
    if not isinstance(value["status"], str) or value["status"] not in {"PASS", "FAIL"}:
        report.error("Z4", "EXTERNAL_REPORT_INCONCLUSIVE", str(value["status"]))
        ok = False
    if external["status"] != value["status"] or external["evaluator_id"] != value["evaluator_id"]:
        report.error("Z4", "RUN_EXTERNAL_STATUS_BINDING_MISMATCH", str(external))
        ok = False
    if external["report_artifact_id"] != artifact.artifact_id:
        report.error("Z4", "RUN_EXTERNAL_REPORT_ID_MISMATCH", artifact.artifact_id)
        ok = False
    if (
        external["bound_raw_stdout_sha256"] != stdout_sha
        or external["bound_answer_key_sha256"] != answer_sha
        or external["bound_rubric_sha256"] != rubric_sha
    ):
        report.error("Z4", "RUN_EXTERNAL_HASH_BINDING_MISMATCH", "stdout/answer/rubric")
        ok = False
    if ok:
        report.task_outcome = value["status"]
    return ok


def verify_claims(protocol: dict[str, Any], run: dict[str, Any], report: Report) -> bool:
    ok = True
    requested = set(protocol["claims_requested"])
    claims = run["claims"]
    seen: set[str] = set()
    for claim in claims:
        claim_id = claim["claim_id"]
        if claim_id in seen:
            report.error("CLAIM", "DUPLICATE_CLAIM", claim_id)
            ok = False
        seen.add(claim_id)
        if claim_id not in CLAIM_RULES or claim_id not in requested:
            report.error("CLAIM", "CLAIM_NOT_CANONICAL_OR_REQUESTED", claim_id)
            ok = False
            continue
        unmet = [gate for gate in CLAIM_RULES[claim_id] if report.gates.get(gate) != "PASS"]
        if unmet:
            report.error("CLAIM", "CLAIM_DEPENDENCY_NOT_PASS", f"{claim_id}:{unmet}")
            ok = False
        else:
            report.verified_claims.add(claim_id)
    if seen != requested:
        report.error("CLAIM", "REQUESTED_CLAIM_SET_MISMATCH", str(sorted(requested ^ seen)))
        ok = False
    return ok


def _evaluate_evidence_impl(
    protocol: dict[str, Any],
    run: dict[str, Any],
    protocol_bytes: bytes,
    evidence_root: Path,
    report: Report,
) -> None:
    if protocol.get("artifact_status") != "LOCKED_PROTOCOL" or run.get("artifact_status") != "RUN_EVIDENCE":
        report.warn("RUN", "LOCKED_EVIDENCE_REQUIRED", "protocol/run artifact_status")
        report.set_gate("Z0", "UNVERIFIED")
        report.set_gate("ZAI", "UNVERIFIED")
        return
    if run.get("run_status") != "COMPLETE":
        report.warn("RUN", "COMPLETE_RUN_REQUIRED", str(run.get("run_status")))
        report.set_gate("Z0", "UNVERIFIED")
        report.set_gate("ZAI", "UNVERIFIED")
        return
    actual_protocol_sha = sha256_bytes(protocol_bytes)
    if run.get("protocol_sha256") != actual_protocol_sha:
        report.error("RUN", "PROTOCOL_SHA256_MISMATCH", f"reported={run.get('protocol_sha256')} actual={actual_protocol_sha}")
        report.set_gate("Z0", "INVALID")
        report.set_gate("ZAI", "INVALID")
        return
    policy_ok = verify_protocol_policy(protocol, report)
    artifacts = materialize_artifacts(run, evidence_root, protocol["evidence_limits"], report)
    artifact_ok = len(artifacts) == len(run["artifacts"]) and not any(stage == "ARTIFACT" for stage, _, _ in report.errors)
    role_index = index_roles(artifacts, report) if artifact_ok else {}
    if not artifact_ok or any(stage == "ARTIFACT" for stage, _, _ in report.errors):
        report.set_gate("Z0", "INVALID")
        report.set_gate("ZAI", "INVALID")
        return
    metadata_ok = verify_artifact_metadata(artifacts, report)
    commitment_ok = verify_commitments(protocol, artifacts, role_index, report)
    identity_binding_ok = verify_artifact_id_bindings(protocol, run, role_index, report)
    language_ok = verify_language_source(protocol, role_index, report)
    z0_ok = policy_ok and metadata_ok and commitment_ok and identity_binding_ok and language_ok
    report.set_gate("Z0", "PASS" if z0_ok else "INVALID")
    visibility_ok, scan_surface = verify_visibility_manifest(
        protocol,
        run,
        artifacts,
        role_index,
        report,
    )
    event_ok = verify_event_chain(protocol, run, artifacts, role_index, scan_surface, report)
    z1_ok = z0_ok and visibility_ok and event_ok
    report.set_gate("Z1", "PASS" if z1_ok else "INVALID")
    materials = parse_answer_key(protocol, role_index, protocol["evidence_limits"], report)
    scan_surface_reported = set(run["scan"]["scan_surface_artifact_ids"])
    if scan_surface_reported != scan_surface:
        report.error("Z2", "RUN_SCAN_SURFACE_MISMATCH", str(sorted(scan_surface_reported ^ scan_surface)))
    machine_scan_ok = False
    if materials and scan_surface_reported == scan_surface:
        artifact_scan_ok = scan_forbidden_material(
            artifacts,
            scan_surface,
            materials,
            protocol["evidence_limits"],
            report,
        )
        argv_scan_ok = scan_forbidden_prekey_argv(run, materials, report)
        machine_scan_ok = artifact_scan_ok and argv_scan_ok
    semantic_ok = verify_semantic_review(protocol, run, artifacts, role_index, scan_surface, report)
    z2_ok = z1_ok and machine_scan_ok and semantic_ok
    report.set_gate("Z2", "PASS" if z2_ok else "INVALID")
    execution_ok = verify_execution(protocol, run, role_index, report)
    host_ok = verify_host_trace(run, artifacts, role_index, report)
    z3_ok = z1_ok and execution_ok and host_ok
    report.set_gate("Z3", "PASS" if z3_ok else "INVALID")
    external_ok = verify_external_evaluation(protocol, run, role_index, report)
    z4_ok = z1_ok and external_ok and event_ok
    report.set_gate("Z4", "PASS" if z4_ok else "INVALID")
    claims_ok = verify_claims(protocol, run, report)
    computed_status = "PASS" if all(report.gates.get(gate) == "PASS" for gate in ("Z0", "Z1", "Z2", "Z3", "Z4")) and claims_ok else "INVALID"
    if run["reported_status"] != computed_status:
        report.error("RUN", "REPORTED_STATUS_MISMATCH", f"reported={run['reported_status']} computed={computed_status}")
        computed_status = "INVALID"
    report.set_gate("ZAI", computed_status)


def evaluate_evidence(
    protocol: dict[str, Any],
    run: dict[str, Any],
    protocol_bytes: bytes,
    evidence_root: Path,
    report: Report,
) -> None:
    """Fail closed for every malformed or adversarial evidence bundle."""

    try:
        _evaluate_evidence_impl(protocol, run, protocol_bytes, evidence_root, report)
    except Exception as exc:
        report.error(
            "INTERNAL",
            "FAIL_CLOSED_VALIDATION_EXCEPTION",
            f"{type(exc).__name__}:{exc}",
        )
        report.set_gate("ZAI", "INVALID")


def report_lines(
    report: Report,
    mode: str,
    receipts: dict[str, str] | None = None,
) -> list[str]:
    lines = [
        f"STANDARD_VERSION={STANDARD_VERSION}",
        f"MODE={mode.upper()}",
        "HUMAN_LANGUAGE_AS_SIGMA_COGNITION=FORBIDDEN_UNTIL_PROVEN",
        "SUPPORTOR_ANSWERS_FOR_SIGMA=FORBIDDEN",
        "PREWRITTEN_ANSWER=FORBIDDEN",
        "PREWRITTEN_HYPOTHESIS=FORBIDDEN",
        "PREWRITTEN_REASONING_PATH=FORBIDDEN",
        "PREWRITTEN_CONCLUSION=FORBIDDEN",
        "SIGMA_SELF_OBSERVES_AND_ANSWERS_POLICY=REQUIRED",
        "SIGMA_SELF_OBSERVES_AND_ANSWERS=NOT_PROVEN",
        "SIGMA_COGNITION=NOT_PROVEN",
    ]
    for key in (
        "PROTOCOL_RAW_SHA256",
        "RUN_BUNDLE_RAW_SHA256",
        "VALIDATOR_SOURCE_SHA256_AT_REPORT",
        "CORE_SOURCE_SHA256_AT_REPORT",
        "PROTOCOL_SCHEMA_SHA256",
        "RUN_SCHEMA_SHA256",
        "STANDARD_DOCUMENT_SHA256",
        "PACKAGE_MANIFEST_SHA256",
    ):
        if receipts is not None and key in receipts:
            lines.append(f"{key}={Report._safe_detail(receipts[key])}")
    if mode == "structure":
        valid = not any(stage in {"SCHEMA", "LOAD"} for stage, _, _ in report.errors)
        lines.extend(
            [
                f"STRICT_SCHEMA_PASS={'YES' if valid else 'NO'}",
                "PACKAGE_MANIFEST_PASS="
                + ("YES" if report.package_manifest_status == "PASS" else "NO"),
                "ACTUAL_ZAI_EXECUTION=UNVERIFIED",
                "ZERO_ANSWER_INJECTION=UNVERIFIED",
            ]
        )
    else:
        lines.append(
            "PACKAGE_MANIFEST_PASS="
            + ("YES" if report.package_manifest_status == "PASS" else "NO")
        )
        for gate in ("Z0", "Z1", "Z2", "Z3", "Z4", "ZAI"):
            lines.append(f"{gate}={report.gates.get(gate, 'UNVERIFIED')}")
        lines.append(f"INJECTION_INTEGRITY_STATUS={report.gates.get('ZAI', 'UNVERIFIED')}")
        lines.append("OBSERVATION_DEPENDENCE_STATUS=NOT_RUN")
        lines.append("INDEPENDENT_REPRODUCTION_STATUS=NOT_RUN")
        lines.append(f"TASK_OUTCOME={Report._safe_detail(report.task_outcome)}")
        lines.append(f"ZERO_ANSWER_INJECTION={report.gates.get('ZAI', 'UNVERIFIED')}")
        bounded_claim_id = (
            "NO_DETECTED_PROHIBITED_ANSWER_INJECTION_WITHIN_DECLARED_MATERIALIZED_BOUNDARY"
        )
        bounded_claim = (
            "YES"
            if report.gates.get("ZAI") == "PASS"
            and bounded_claim_id in report.verified_claims
            else "NOT_ESTABLISHED"
        )
        lines.append(
            "NO_DETECTED_PROHIBITED_ANSWER_INJECTION_WITHIN_DECLARED_MATERIALIZED_BOUNDARY="
            + bounded_claim
        )
    lines.append(f"SCAN_MATCH_COUNT={len(report.scan_matches)}")
    lines.append(f"ERROR_COUNT={len(report.errors)}")
    lines.append(f"WARNING_COUNT={len(report.warnings)}")
    for match in sorted(report.scan_matches, key=lambda item: tuple(item[key] for key in ("artifact_id", "material_id", "mode"))):
        lines.append("SCAN_MATCH=" + json.dumps(match, ensure_ascii=True, sort_keys=True, separators=(",", ":")))
    for stage, code, detail in sorted(report.errors):
        lines.append(f"ERROR={stage}:{code}:{detail}")
    for stage, code, detail in sorted(report.warnings):
        lines.append(f"WARNING={stage}:{code}:{detail}")
    return lines
