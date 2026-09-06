#!/usr/bin/env python3
import argparse
import json
import pathlib
import re
import sys

MAX_CANDIDATES = 4
MAX_HISTORY_ROWS = 4096
HEX64 = re.compile(r"^[0-9a-f]{64}$")
TOKEN = re.compile(r"^[A-Za-z0-9_.:/@+\-]{1,128}$")
FORBIDDEN_KEYS = {
    "expected", "expected_candidate", "best", "best_candidate",
    "recommended", "recommended_candidate", "semantic_score",
    "relevance_score", "trust_score", "teacher_choice",
}

def fail(msg, rc=2):
    print(f"BUILDER_ERROR={msg}")
    raise SystemExit(rc)

def load_json(path):
    try:
        return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"JSON_LOAD_FAILED:{type(exc).__name__}")

def integer_text(value, name, minimum=0, maximum=9007199254740991):
    s = str(value)
    if not s.isdigit():
        fail(f"{name}_NOT_NONNEGATIVE_INTEGER")
    n = int(s)
    if n < minimum or n > maximum:
        fail(f"{name}_OUT_OF_RANGE")
    return n

def flag(value, name):
    s = str(value)
    if s not in ("0", "1"):
        fail(f"{name}_NOT_FLAG")
    return s

def validate_candidate(row):
    if not isinstance(row, dict):
        fail("CANDIDATE_NOT_OBJECT")
    if FORBIDDEN_KEYS.intersection(row):
        fail("SEMANTIC_SELECTION_FIELD_FORBIDDEN")
    required = {"id", "token", "available", "readiness"}
    if set(row) != required:
        fail("CANDIDATE_SCHEMA_INVALID")
    cid = integer_text(row["id"], "CANDIDATE_ID", 1, 9007199254740991)
    token = str(row["token"])
    if not TOKEN.fullmatch(token):
        fail("CANDIDATE_TOKEN_INVALID")
    available = flag(row["available"], "CANDIDATE_AVAILABLE")
    readiness = integer_text(row["readiness"], "CANDIDATE_READINESS", 0, 1000000)
    return {"id": cid, "token": token, "available": available, "readiness": readiness}

def read_history(path, valid_ids):
    stats = {
        cid: {
            "attempts": 0,
            "material_success": 0,
            "evidence_units": 0,
            "knowledge_units": 0,
            "segment_commits": 0,
            "hard_failures": 0,
            "repeated_failures": 0,
            "unresolved_improve": 0,
            "unresolved_worsen": 0,
            "last_failure": "NONE",
        }
        for cid in valid_ids
    }
    if not path:
        return stats

    p = pathlib.Path(path)
    if not p.exists():
        fail("HISTORY_FILE_MISSING")

    rows = 0
    for raw in p.read_text(encoding="utf-8").splitlines():
        if raw == "":
            continue
        rows += 1
        if rows > MAX_HISTORY_ROWS:
            fail("HISTORY_ROW_LIMIT_EXCEEDED")
        try:
            row = json.loads(raw)
        except Exception:
            fail("HISTORY_JSONL_INVALID")
        if not isinstance(row, dict):
            fail("HISTORY_ROW_NOT_OBJECT")
        if FORBIDDEN_KEYS.intersection(row):
            fail("HISTORY_SEMANTIC_SELECTION_FIELD_FORBIDDEN")
        required = {
            "candidate_id",
            "evidence_persisted",
            "knowledge_persisted",
            "segment_committed",
            "failure_fingerprint",
            "unresolved_before",
            "unresolved_after",
        }
        if set(row) != required:
            fail("HISTORY_SCHEMA_INVALID")
        cid = integer_text(row["candidate_id"], "HISTORY_CANDIDATE_ID", 1, 9007199254740991)
        if cid not in stats:
            fail("HISTORY_UNKNOWN_CANDIDATE_ID")
        evidence = integer_text(row["evidence_persisted"], "EVIDENCE_PERSISTED")
        knowledge = integer_text(row["knowledge_persisted"], "KNOWLEDGE_PERSISTED")
        committed = integer_text(row["segment_committed"], "SEGMENT_COMMITTED", 0, 1)
        before = integer_text(row["unresolved_before"], "UNRESOLVED_BEFORE")
        after = integer_text(row["unresolved_after"], "UNRESOLVED_AFTER")
        fp = str(row["failure_fingerprint"])
        if fp != "NONE" and not HEX64.fullmatch(fp):
            fail("FAILURE_FINGERPRINT_INVALID")

        st = stats[cid]
        st["attempts"] += 1
        if evidence > 0 or knowledge > 0 or committed == 1:
            st["material_success"] += 1
        st["evidence_units"] += evidence
        st["knowledge_units"] += knowledge
        st["segment_commits"] += committed
        if fp != "NONE":
            st["hard_failures"] += 1
            if st["last_failure"] == fp:
                st["repeated_failures"] += 1
            st["last_failure"] = fp
        else:
            st["last_failure"] = "NONE"
        if after < before:
            st["unresolved_improve"] += 1
        elif after > before:
            st["unresolved_worsen"] += 1
    return stats

def write_text(path, value):
    pathlib.Path(path).write_text(str(value), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--history")
    ap.add_argument("--out-input", required=True)
    ap.add_argument("--instance-fingerprint", required=True)
    ap.add_argument("--c5-core-sha256", required=True)
    ap.add_argument("--last-selected-id", default="NONE")
    args = ap.parse_args()

    if not HEX64.fullmatch(args.instance_fingerprint):
        fail("INSTANCE_FINGERPRINT_INVALID")
    if not HEX64.fullmatch(args.c5_core_sha256):
        fail("C5_CORE_SHA256_INVALID")
    if args.last_selected_id != "NONE":
        integer_text(args.last_selected_id, "LAST_SELECTED_ID", 1, 9007199254740991)

    obj = load_json(args.catalog)
    if not isinstance(obj, dict) or set(obj) != {"candidates"}:
        fail("CATALOG_SCHEMA_INVALID")
    rows = obj["candidates"]
    if not isinstance(rows, list) or not (1 <= len(rows) <= MAX_CANDIDATES):
        fail("CANDIDATE_COUNT_INVALID")

    candidates = [validate_candidate(r) for r in rows]
    ids = [r["id"] for r in candidates]
    tokens = [r["token"] for r in candidates]
    if len(set(ids)) != len(ids):
        fail("DUPLICATE_CANDIDATE_ID")
    if len(set(tokens)) != len(tokens):
        fail("DUPLICATE_CANDIDATE_TOKEN")

    stats = read_history(args.history, set(ids))
    out = pathlib.Path(args.out_input)
    out.mkdir(parents=True, exist_ok=True)

    write_text(out / "instance_fingerprint_sha256.txt", args.instance_fingerprint)
    write_text(out / "c5_core_sha256.txt", args.c5_core_sha256)
    write_text(out / "candidate_count.txt", len(candidates))
    write_text(out / "last_selected_id.txt", args.last_selected_id)

    by_index = {i: candidates[i] for i in range(len(candidates))}
    for i in range(MAX_CANDIDATES):
        if i not in by_index:
            values = {
                "configured": "0", "id": "", "token": "", "available": "0", "readiness": 0,
                "attempts": 0, "material_success": 0, "evidence_units": 0,
                "knowledge_units": 0, "segment_commits": 0, "hard_failures": 0,
                "repeated_failures": 0, "unresolved_improve": 0, "unresolved_worsen": 0,
            }
        else:
            c = by_index[i]
            st = stats[c["id"]]
            values = {
                "configured": "1", "id": c["id"], "token": c["token"],
                "available": c["available"], "readiness": c["readiness"],
                "attempts": st["attempts"], "material_success": st["material_success"],
                "evidence_units": st["evidence_units"], "knowledge_units": st["knowledge_units"],
                "segment_commits": st["segment_commits"], "hard_failures": st["hard_failures"],
                "repeated_failures": st["repeated_failures"],
                "unresolved_improve": st["unresolved_improve"],
                "unresolved_worsen": st["unresolved_worsen"],
            }
        for name, value in values.items():
            write_text(out / f"c{i}_{name}.txt", value)

    manifest = {
        "role": "MECHANICAL_EXPERIENCE_FACT_AGGREGATOR",
        "host_candidate_selection": "NO",
        "host_semantic_scoring": "NO",
        "host_learning": "NO",
        "candidate_count": len(candidates),
        "history_rows_bounded": MAX_HISTORY_ROWS,
        "output_slot_count": MAX_CANDIDATES,
    }
    (out.parent / "builder_manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )
    print("BUILDER_STATUS=OK")
    print(f"CANDIDATE_COUNT={len(candidates)}")
    print("HOST_CANDIDATE_SELECTION=NO")
    print("HOST_SEMANTIC_SCORING=NO")
    print("HOST_LEARNING=NO")

if __name__ == "__main__":
    main()
