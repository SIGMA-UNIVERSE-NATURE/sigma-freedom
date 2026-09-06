#!/usr/bin/env python3
'''
C5_MECHANICAL_EXTERNAL_TOOL_INPUT_BUILDER_V1.py

Mechanical protocol builder only:
- reads the exact current C5 native external request bytes;
- tokenizes mechanically with a fixed separator set and preserves token order;
- decodes a bounded capability catalog;
- aggregates factual transport/decode/material outcomes by stable tool id;
- writes slot-based input files for C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1.

It does not generate/rewrite the query, rank tools, select a source, select a resource,
interpret meaning, decide truth, or write C5 cognitive state.
'''

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

MAX_TOOLS = 8
MAX_QUERY_TOKENS = 12
FORBIDDEN_CATALOG_KEYS = {
    "best_source",
    "relevance_score",
    "trust_score",
    "recommended_source",
    "recommended",
    "topic_source_mapping",
    "semantic_rank",
}

TOKEN_SPLIT_RE = re.compile(r"[\s\|\t\r\n,;:/\\()\[\]{}=+*<>!?~]+", re.UNICODE)


def fail(msg: str, rc: int = 2) -> None:
    print(f"HOLD={msg}")
    raise SystemExit(rc)


def write_text(path: Path, value: str) -> None:
    path.write_text(value, encoding="utf-8")


def is_digits(v: str) -> bool:
    return bool(v) and v.isdigit()


def load_catalog(path: Path) -> list[dict]:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"CATALOG_JSON_INVALID type={type(exc).__name__}", 20)

    if not isinstance(obj, dict) or not isinstance(obj.get("tools"), list):
        fail("CATALOG_SCHEMA_INVALID", 21)

    tools = obj["tools"]
    if len(tools) > MAX_TOOLS:
        fail(f"CATALOG_TOOL_BOUND_EXCEEDED count={len(tools)} max={MAX_TOOLS}", 22)

    seen_ids: set[str] = set()
    seen_tokens: set[str] = set()
    out: list[dict] = []

    for idx, row in enumerate(tools):
        if not isinstance(row, dict):
            fail(f"CATALOG_ROW_NOT_OBJECT index={idx}", 23)

        bad = FORBIDDEN_CATALOG_KEYS.intersection(row)
        if bad:
            fail("CATALOG_FORBIDDEN_SEMANTIC_FIELD fields=" + ",".join(sorted(bad)), 24)

        required = ("id", "token", "available", "readiness", "descriptor", "languages", "media")
        if any(k not in row for k in required):
            fail(f"CATALOG_REQUIRED_FIELD_MISSING index={idx}", 25)

        normalized = {k: str(row[k]) for k in required}

        if not is_digits(normalized["id"]):
            fail(f"CATALOG_ID_INVALID index={idx}", 26)
        if not normalized["token"]:
            fail(f"CATALOG_TOKEN_EMPTY index={idx}", 27)
        if normalized["available"] not in ("0", "1"):
            fail(f"CATALOG_AVAILABLE_INVALID index={idx}", 28)
        if not is_digits(normalized["readiness"]):
            fail(f"CATALOG_READINESS_INVALID index={idx}", 29)

        if normalized["id"] in seen_ids:
            fail(f"CATALOG_DUPLICATE_ID id={normalized['id']}", 30)
        if normalized["token"] in seen_tokens:
            fail("CATALOG_DUPLICATE_TOKEN", 31)

        seen_ids.add(normalized["id"])
        seen_tokens.add(normalized["token"])
        out.append(normalized)

    return out


def load_history(path: Path | None) -> tuple[dict[str, dict[str, int]], str]:
    stats: dict[str, dict[str, int]] = {}
    last_tool_id = ""

    if path is None or not path.exists():
        return stats, last_tool_id

    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except Exception as exc:
                fail(f"HISTORY_JSON_INVALID line={line_no} type={type(exc).__name__}", 40)

            if not isinstance(row, dict):
                fail(f"HISTORY_ROW_NOT_OBJECT line={line_no}", 41)

            tool_id = str(row.get("tool_id", ""))
            if not is_digits(tool_id):
                fail(f"HISTORY_TOOL_ID_INVALID line={line_no}", 42)

            def iv(name: str) -> int:
                v = row.get(name)
                if isinstance(v, bool):
                    fail(f"HISTORY_FIELD_INVALID line={line_no} field={name}", 43)
                try:
                    n = int(v)
                except Exception:
                    fail(f"HISTORY_FIELD_INVALID line={line_no} field={name}", 43)
                if n < 0:
                    fail(f"HISTORY_FIELD_NEGATIVE line={line_no} field={name}", 44)
                return n

            transport_rc = iv("transport_rc")
            http_code = iv("http_code")
            decode_rc = iv("decode_rc")
            payload_bytes = iv("payload_bytes")

            s = stats.setdefault(
                tool_id,
                {
                    "prior_selected": 0,
                    "material_success": 0,
                    "no_material": 0,
                    "transport_failure": 0,
                    "http_failure": 0,
                    "decode_failure": 0,
                },
            )
            s["prior_selected"] += 1
            last_tool_id = tool_id

            if transport_rc != 0:
                s["transport_failure"] += 1
            elif http_code != 200:
                s["http_failure"] += 1
            elif decode_rc != 0:
                s["decode_failure"] += 1
            elif payload_bytes > 0:
                s["material_success"] += 1
            else:
                s["no_material"] += 1

    return stats, last_tool_id


def query_tokens_exact(text: str) -> list[str]:
    # Fixed mechanical token boundaries only. No lowercase, translation, stemming,
    # ranking, synonym expansion, or semantic filtering.
    return [tok for tok in TOKEN_SPLIT_RE.split(text) if tok][:MAX_QUERY_TOKENS]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--request-file", required=True)
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--history")
    ap.add_argument("--out-input", required=True)
    ap.add_argument("--instance-fingerprint", required=True)
    ap.add_argument("--c5-core-sha256", required=True)
    args = ap.parse_args()

    request_file = Path(args.request_file)
    catalog_file = Path(args.catalog)
    history_file = Path(args.history) if args.history else None
    out = Path(args.out_input)

    if not request_file.is_file():
        fail("REQUEST_FILE_MISSING", 10)

    query_bytes = request_file.read_bytes().rstrip(b"\r\n")
    if not query_bytes:
        fail("REQUEST_EMPTY", 11)

    try:
        query_text = query_bytes.decode("utf-8")
    except UnicodeDecodeError:
        fail("REQUEST_NOT_UTF8", 12)

    fp = str(args.instance_fingerprint)
    core = str(args.c5_core_sha256)
    if not re.fullmatch(r"[0-9a-f]{64}", fp):
        fail("INSTANCE_FINGERPRINT_INVALID", 13)
    if not re.fullmatch(r"[0-9a-f]{64}", core):
        fail("C5_CORE_SHA256_INVALID", 14)

    tools = load_catalog(catalog_file)
    history, last_tool_id = load_history(history_file)

    out.mkdir(parents=True, exist_ok=True)

    qsha = hashlib.sha256(query_bytes).hexdigest()
    write_text(out / "instance_fingerprint_sha256.txt", fp)
    write_text(out / "c5_core_sha256.txt", core)
    write_text(out / "query_sha256.txt", qsha)
    write_text(out / "query.txt", query_text)
    write_text(out / "last_selected_tool_id.txt", last_tool_id)

    toks = query_tokens_exact(query_text)
    for i in range(MAX_QUERY_TOKENS):
        write_text(out / f"query_token_{i}.txt", toks[i] if i < len(toks) else "")

    empty_stats = {
        "prior_selected": 0,
        "material_success": 0,
        "no_material": 0,
        "transport_failure": 0,
        "http_failure": 0,
        "decode_failure": 0,
    }

    for i in range(MAX_TOOLS):
        if i < len(tools):
            row = tools[i]
            s = history.get(row["id"], empty_stats)
        else:
            row = {
                "id": "",
                "token": "",
                "available": "0",
                "readiness": "0",
                "descriptor": "",
                "languages": "",
                "media": "",
            }
            s = empty_stats

        write_text(out / f"tool{i}_id.txt", row["id"])
        write_text(out / f"tool{i}_token.txt", row["token"])
        write_text(out / f"tool{i}_available.txt", row["available"])
        write_text(out / f"tool{i}_readiness.txt", row["readiness"])
        write_text(out / f"tool{i}_prior_selected.txt", str(s["prior_selected"]))
        write_text(out / f"tool{i}_material_success.txt", str(s["material_success"]))
        write_text(out / f"tool{i}_no_material.txt", str(s["no_material"]))
        write_text(out / f"tool{i}_transport_failure.txt", str(s["transport_failure"]))
        write_text(out / f"tool{i}_http_failure.txt", str(s["http_failure"]))
        write_text(out / f"tool{i}_decode_failure.txt", str(s["decode_failure"]))
        write_text(out / f"tool{i}_descriptor.txt", row["descriptor"])
        write_text(out / f"tool{i}_languages.txt", row["languages"])
        write_text(out / f"tool{i}_media.txt", row["media"])

    manifest = {
        "query_sha256": qsha,
        "query_bytes": len(query_bytes),
        "query_token_count": len(toks),
        "catalog_sha256": hashlib.sha256(catalog_file.read_bytes()).hexdigest(),
        "history_sha256": (
            hashlib.sha256(history_file.read_bytes()).hexdigest()
            if history_file is not None and history_file.exists()
            else "NONE"
        ),
        "tool_rows": len(tools),
        "role": "MECHANICAL_PROTOCOL_BUILD_ONLY",
    }
    (out / "builder_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )

    print("C5_EXTERNAL_TOOL_INPUT_BUILDER=PASS")
    print(f"QUERY_SHA256={qsha}")
    print(f"QUERY_BYTES={len(query_bytes)}")
    print(f"QUERY_TOKEN_COUNT={len(toks)}")
    print(f"CATALOG_TOOL_ROWS={len(tools)}")
    print("HOST_QUERY_GENERATION=NO")
    print("HOST_QUERY_REWRITE=NO")
    print("HOST_SOURCE_SELECTION=NO")
    print("HOST_RESOURCE_SELECTION=NO")
    print("HOST_TRUTH_DECISION=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
