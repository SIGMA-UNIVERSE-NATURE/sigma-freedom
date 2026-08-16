#!/usr/bin/env python3
"""Validate and expand the SIGMA 512 -> 54 core architecture contract.

This validator intentionally distinguishes:
- specification existence,
- responsibility mapping,
- implementation evidence.

It MUST NOT infer implementation PASS from filenames, documents, classes,
functions, comments, or self-reports.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
MANIFEST_PATH = HERE / "SIGMA_512_CANONICAL_MANIFEST.json"
TRACE_PATH = HERE / "SIGMA_512_TRACEABILITY_MAP.json"
STATUS_PATH = HERE / "SIGMA_512_IMPLEMENTATION_STATUS.json"
DEFAULT_OUTPUT = HERE / "SIGMA_512_EXPANDED_REGISTRY.generated.json"
ATTRIBUTE_RE = re.compile(r"^\s*(\d{1,3})\.\s+(.+?)\s*$")
CORE_RE = re.compile(r"^SIGMA_DNA_(\d{2})_.*\.py$")


class ContractError(RuntimeError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ContractError(f"Cannot read JSON {path}: {exc}") from exc


def working_tree_blob_sha(path: Path) -> str:
    """Fallback Git blob SHA from local bytes."""
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def repository_blob_sha(path: Path) -> str:
    """Read the committed blob SHA when possible.

    Using HEAD:path avoids false integrity failures caused by CRLF checkout
    conversion on Windows. If the file is not in a Git checkout, fall back to
    hashing the working-tree bytes using Git's blob format.
    """
    try:
        rel = path.relative_to(REPO).as_posix()
        proc = subprocess.run(
            ["git", "-C", str(REPO), "rev-parse", f"HEAD:{rel}"],
            check=True,
            capture_output=True,
            text=True,
        )
        value = proc.stdout.strip()
        if re.fullmatch(r"[0-9a-fA-F]{40,64}", value):
            return value.lower()
    except Exception:
        pass
    return working_tree_blob_sha(path)


def parse_numbered_attributes(path: Path) -> dict[int, list[str]]:
    found: dict[int, list[str]] = {}
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        match = ATTRIBUTE_RE.match(raw)
        if not match:
            continue
        number = int(match.group(1))
        text = match.group(2).strip()
        if 1 <= number <= 512:
            found.setdefault(number, []).append(text)
    return found


def validate_manifest(manifest: dict[str, Any]) -> dict[int, dict[str, Any]]:
    records: dict[int, dict[str, Any]] = {}
    errors: list[str] = []

    expected = int(manifest["canonical_attribute_count"])
    if expected != 512:
        errors.append(f"canonical_attribute_count must be 512, got {expected}")

    for segment in sorted(manifest["segments"], key=lambda x: x["order"]):
        path = REPO / segment["path"]
        if not path.exists():
            errors.append(f"missing canonical source segment: {segment['path']}")
            continue

        actual_sha = repository_blob_sha(path)
        expected_sha = segment.get("source_blob_sha")
        if expected_sha and actual_sha != expected_sha:
            errors.append(
                f"source blob changed without manifest update: {segment['path']} "
                f"expected={expected_sha} actual={actual_sha}"
            )

        parsed = parse_numbered_attributes(path)
        low, high = int(segment["canonical_from"]), int(segment["canonical_to"])
        for number in range(low, high + 1):
            values = parsed.get(number, [])
            if not values:
                errors.append(f"attribute {number:03d} missing from {segment['path']}")
                continue
            unique_values = list(dict.fromkeys(values))
            if len(unique_values) != 1:
                errors.append(
                    f"attribute {number:03d} has conflicting definitions inside {segment['path']}: {unique_values}"
                )
                continue
            if number in records:
                errors.append(f"canonical attribute {number:03d} selected more than once")
                continue
            records[number] = {
                "attribute_id": f"SIGMA-ATTR-{number:03d}",
                "number": number,
                "requirement": unique_values[0],
                "source_path": segment["path"],
                "source_blob_sha": actual_sha,
            }

    expected_numbers = set(range(1, 513))
    actual_numbers = set(records)
    missing = sorted(expected_numbers - actual_numbers)
    extra = sorted(actual_numbers - expected_numbers)
    if missing:
        errors.append(f"canonical coverage missing: {missing}")
    if extra:
        errors.append(f"canonical coverage contains out-of-range items: {extra}")

    sections = manifest.get("sections", [])
    section_coverage: list[int] = []
    for section in sections:
        section_coverage.extend(range(int(section["from"]), int(section["to"]) + 1))
    if section_coverage != list(range(1, 513)):
        errors.append("manifest section ranges must cover 1..512 exactly once and in order")

    if errors:
        raise ContractError("\n".join(errors))
    return records


def discover_cores(manifest: dict[str, Any]) -> dict[int, str]:
    root = REPO / manifest["implementation_contract"]["core_root"]
    if not root.is_dir():
        raise ContractError(f"core root missing: {root}")

    cores: dict[int, str] = {}
    duplicates: dict[int, list[str]] = {}
    for path in sorted(root.iterdir()):
        if not path.is_file():
            continue
        match = CORE_RE.match(path.name)
        if not match:
            continue
        core_id = int(match.group(1))
        if core_id in cores:
            duplicates.setdefault(core_id, [cores[core_id]]).append(str(path.relative_to(REPO)))
        else:
            cores[core_id] = str(path.relative_to(REPO))

    expected_count = int(manifest["implementation_contract"]["expected_core_count"])
    expected_ids = set(range(1, expected_count + 1))
    actual_ids = set(cores)
    if duplicates:
        raise ContractError(f"duplicate DNA core IDs: {duplicates}")
    if actual_ids != expected_ids:
        missing = sorted(expected_ids - actual_ids)
        extra = sorted(actual_ids - expected_ids)
        raise ContractError(f"54-core catalog mismatch; missing={missing}, extra={extra}")
    return cores


def validate_traceability(trace: dict[str, Any], cores: dict[int, str]) -> dict[int, dict[str, Any]]:
    ranges = trace.get("ranges", [])
    coverage: list[int] = []
    per_attribute: dict[int, dict[str, Any]] = {}
    errors: list[str] = []

    for item in ranges:
        low, high = int(item["from"]), int(item["to"])
        if low > high:
            errors.append(f"invalid traceability range {low}-{high}")
            continue
        primary = [int(x) for x in item.get("primary_cores", [])]
        support = [int(x) for x in item.get("supporting_cores", [])]
        if not primary:
            errors.append(f"section {item.get('section')} has no primary core")
        unknown = sorted(set(primary + support) - set(cores))
        if unknown:
            errors.append(f"section {item.get('section')} references unknown cores {unknown}")
        for number in range(low, high + 1):
            coverage.append(number)
            if number in per_attribute:
                errors.append(f"attribute {number:03d} mapped by overlapping traceability ranges")
                continue
            per_attribute[number] = {
                "section": item["section"],
                "domain": item["domain"],
                "primary_cores": [{"id": x, "path": cores.get(x)} for x in primary],
                "supporting_cores": [{"id": x, "path": cores.get(x)} for x in support],
                "required_evidence_classes": item.get("required_evidence", []),
            }

    if coverage != list(range(1, 513)):
        errors.append("traceability ranges must cover 1..512 exactly once and in order")
    if errors:
        raise ContractError("\n".join(errors))
    return per_attribute


def validate_status_ledger(status: dict[str, Any]) -> dict[str, dict[str, Any]]:
    allowed = set(status["allowed_statuses"])
    required_for_pass = list(status["pass_contract"]["required_fields"])
    items = status.get("items", {})
    errors: list[str] = []

    for key, entry in items.items():
        match = re.fullmatch(r"SIGMA-ATTR-(\d{3})", key)
        if not match or not (1 <= int(match.group(1)) <= 512):
            errors.append(f"invalid status ledger key: {key}")
            continue
        state = entry.get("status", status["default_status"])
        if state not in allowed:
            errors.append(f"{key}: invalid status {state}")
            continue
        if state == "PASS":
            missing = [field for field in required_for_pass if not entry.get(field)]
            if missing:
                errors.append(f"{key}: PASS missing required fields {missing}")
            evaluator = entry.get("evaluator")
            if not isinstance(evaluator, dict) or evaluator.get("independent") is not True:
                errors.append(f"{key}: PASS requires evaluator.independent=true")
        if state == "NOT_APPLICABLE" and not entry.get("rationale"):
            errors.append(f"{key}: NOT_APPLICABLE requires rationale")

    if errors:
        raise ContractError("\n".join(errors))
    return items


def section_for(number: int, manifest: dict[str, Any]) -> dict[str, Any]:
    for section in manifest["sections"]:
        if int(section["from"]) <= number <= int(section["to"]):
            return section
    raise ContractError(f"no section for attribute {number}")


def build_registry() -> dict[str, Any]:
    manifest = load_json(MANIFEST_PATH)
    trace = load_json(TRACE_PATH)
    status = load_json(STATUS_PATH)

    records = validate_manifest(manifest)
    cores = discover_cores(manifest)
    mapped = validate_traceability(trace, cores)
    ledger = validate_status_ledger(status)

    expanded: list[dict[str, Any]] = []
    counts: dict[str, int] = {}
    for number in range(1, 513):
        base = records[number]
        section = section_for(number, manifest)
        mapping = mapped[number]
        item_key = base["attribute_id"]
        evidence_state = ledger.get(item_key, {})
        implementation_status = evidence_state.get("status", status["default_status"])
        counts[implementation_status] = counts.get(implementation_status, 0) + 1
        expanded.append({
            **base,
            "section": {"id": section["id"], "name": section["name"]},
            "traceability": mapping,
            "status": {
                "specification": "SPEC_PASS",
                "responsibility": "MAPPED",
                "implementation": implementation_status,
            },
            "implementation_evidence": evidence_state,
        })

    return {
        "schema_version": "1.0.0",
        "registry_id": "SIGMA-512-EXPANDED-REGISTRY",
        "generated_from": {
            "manifest": MANIFEST_PATH.name,
            "traceability": TRACE_PATH.name,
            "status_ledger": STATUS_PATH.name,
        },
        "invariants": {
            "canonical_count": len(expanded),
            "core_count": len(cores),
            "canonical_contiguous_1_to_512": True,
            "traceability_complete": True,
            "implementation_pass_is_never_inferred": True,
        },
        "implementation_status_counts": counts,
        "cores": [{"id": k, "path": v} for k, v in sorted(cores.items())],
        "attributes": expanded,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write expanded registry JSON")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    try:
        registry = build_registry()
    except ContractError as exc:
        print("SIGMA_512_CONTRACT: FAIL", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1

    if args.write:
        args.output.write_text(
            json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print("SIGMA_512_CONTRACT: PASS")
    print(f"CANONICAL_ATTRIBUTES={registry['invariants']['canonical_count']}")
    print(f"DNA_CORES={registry['invariants']['core_count']}")
    print("TRACEABILITY=COMPLETE")
    print("IMPLEMENTATION_PASS_INFERENCE=FORBIDDEN")
    for state, count in sorted(registry["implementation_status_counts"].items()):
        print(f"IMPLEMENTATION_{state}={count}")
    if args.write:
        print(f"EXPANDED_REGISTRY={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
