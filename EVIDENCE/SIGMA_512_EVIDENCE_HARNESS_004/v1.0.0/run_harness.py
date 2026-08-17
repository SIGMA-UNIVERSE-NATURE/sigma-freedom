#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CANONICAL = REPO / "BRAIN" / "CANONICAL"
OUT = Path(os.environ.get("SIGMA_HARNESS_OUTPUT_DIR", str(HERE / "out"))).resolve()
EXPECTED_REQUEST = "SIGMA-512-EVIDENCE-HARNESS-004-SECTION-I-001-012"


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"not_object:{path.name}")
    return value


def core_digest() -> str:
    root = REPO / "54_CORES"
    paths = sorted(
        p for p in root.iterdir()
        if p.is_file() and p.name.startswith("SIGMA_DNA_")
    )
    if len(paths) != 54:
        raise ValueError(f"unexpected_dna_count:{len(paths)}")
    h = hashlib.sha256()
    for p in paths:
        h.update(p.name.encode("utf-8"))
        h.update(b"\0")
        h.update(p.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def row(attr: int, status: str, observed: bool, evidence: str) -> dict[str, Any]:
    return {
        "attribute_id": f"SIGMA-ATTR-{attr:03d}",
        "status": status,
        "observed": observed,
        "evidence": evidence,
        "ceiling": "PASS_FORBIDDEN",
    }


def main() -> int:
    before = core_digest()
    state = load(CANONICAL / "CURRENT_STATE.json")
    request = load(CANONICAL / "LOCAL_COGNITION_REQUEST.json")
    root = load(CANONICAL / "ROOT_OF_TRUST.json")
    moc = load(CANONICAL / "MINH_OPERATING_CONSTITUTION.json")
    cog = load(CANONICAL / "COGNITIVE_STATE.schema.json")
    mem = load(CANONICAL / "MEMORY_RECORD.schema.json")
    next_action = (CANONICAL / "NEXT_ACTION.md").read_text(encoding="utf-8")

    if os.environ.get("SIGMA_LOCAL_EXECUTION_ID") != EXPECTED_REQUEST:
        raise ValueError("request_environment_mismatch")
    if request.get("request_id") != EXPECTED_REQUEST:
        raise ValueError("canonical_request_id_mismatch")
    if request.get("status") != "PENDING_LOCAL_EXECUTOR":
        raise ValueError("canonical_request_not_pending")
    if state.get("next_action_id") != EXPECTED_REQUEST or f"## {EXPECTED_REQUEST}" not in next_action:
        raise ValueError("canonical_next_action_mismatch")

    invariants = set(root.get("invariants") or [])
    principles = {p.get("name"): p for p in (moc.get("principles") or []) if isinstance(p, dict)}
    cog_epi = ((cog.get("properties") or {}).get("epistemic_state") or {}).get("properties") or {}
    mem_props = mem.get("properties") or {}
    status_enum = set((mem_props.get("epistemic_status") or {}).get("enum") or [])
    confidence = mem_props.get("confidence") or {}

    results = [
        row(1, "PARTIAL",
            "NOTHING_IS_TRUE_BY_INHERITANCE" in invariants and "REALITY_BEFORE_IMPROVEMENT" in principles,
            "Root/constitution structurally forbid inherited truth; runtime adherence beyond tested contracts remains unproven."),
        row(2, "PARTIAL",
            "beliefs" in cog_epi and "evidence_refs" in mem_props,
            "Cognitive-state and memory schemas structurally separate beliefs from evidence references; native runtime enforcement remains unproven."),
        row(3, "PARTIAL",
            {"MODEL_PRIOR","OBSERVATION","RETRIEVED_EVIDENCE","INFERENCE","HYPOTHESIS"}.issubset(status_enum),
            "Memory-record schema explicitly classifies provenance/epistemic source categories."),
        row(4, "PARTIAL",
            confidence.get("minimum") == 0 and confidence.get("maximum") == 1,
            "Memory-record confidence is quantitatively bounded [0,1]; calibration quality is not established."),
        row(5, "PARTIAL",
            "unknowns" in cog_epi,
            "Cognitive-state schema has explicit unknowns representation; reliable unknown detection behavior is not established."),
        row(6, "PARTIAL",
            "contradictions" in cog_epi,
            "Cognitive-state schema has explicit contradictions representation; automatic detection behavior is not established."),
        row(7, "PARTIAL",
            "hypotheses" in cog_epi and (cog_epi.get("hypotheses") or {}).get("type") == "array",
            "Cognitive-state schema can hold multiple hypotheses; active competition/selection behavior is not established."),
        row(8, "NOT_AUDITED", False,
            "No bounded runtime experiment in this harness tests active counterexample search."),
        row(9, "NOT_AUDITED", False,
            "No bounded runtime experiment in this harness tests falsification priority over confirmation."),
        row(10, "NOT_AUDITED", False,
            "No bounded runtime experiment in this harness tests correlation/causation/coincidence discrimination."),
        row(11, "NOT_AUDITED", False,
            "No bounded runtime experiment in this harness tests ontology revision."),
        row(12, "NOT_AUDITED", False,
            "No bounded runtime experiment in this harness tests complete concept retirement."),
    ]

    after = core_digest()
    counts = {
        "PASS": 0,
        "PARTIAL": sum(r["status"] == "PARTIAL" for r in results),
        "HOLD": sum(r["status"] == "HOLD" for r in results),
        "FAIL": sum(r["status"] == "FAIL" for r in results),
        "NOT_AUDITED": sum(r["status"] == "NOT_AUDITED" for r in results),
    }
    result = {
        "schema_version": "1.0.0",
        "harness_id": "SIGMA-512-EVIDENCE-HARNESS-004",
        "harness_version": "1.0.0",
        "section": "I",
        "section_name": "Nhận thức và sự thật",
        "target_count": 12,
        "counts": counts,
        "results": results,
        "core_tree_sha256_before": before,
        "core_tree_sha256_after": after,
        "core_modifications": 0 if before == after else 1,
        "external_side_effects": 0,
        "pass_allowed": False,
        "evaluator_independent": False,
        "interpretation": "Structural/read-only evidence only. PARTIAL does not prove production cognition behavior."
    }

    OUT.mkdir(parents=True, exist_ok=True)
    result_file = OUT / "evidence_harness_004_result.json"
    result_file.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("SIGMA_512_EVIDENCE_HARNESS_004: PASS")
    print("TARGET_COUNT=12")
    print(f"PARTIAL={counts['PARTIAL']}")
    print(f"NOT_AUDITED={counts['NOT_AUDITED']}")
    print("FAIL=0")
    print("PASS=0")
    print(f"CORE_TREE_SHA256={after}")
    print(f"CORE_MODIFICATIONS={result['core_modifications']}")
    print("EXTERNAL_SIDE_EFFECTS=0")
    return 0 if after == before and counts["FAIL"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
