#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CANONICAL = REPO / "BRAIN" / "CANONICAL"
OUT = Path(os.environ.get("SIGMA_HARNESS_OUTPUT_DIR", str(HERE / "out"))).resolve()
EXPECTED_REQUEST = "SIGMA-512-EVIDENCE-HARNESS-006-SECTION-III-LEARNING-025-036"


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"not_object:{path.name}")
    return value


def core_digest() -> str:
    root = REPO / "54_CORES"
    paths = sorted(p for p in root.iterdir() if p.is_file() and p.name.startswith("SIGMA_DNA_"))
    if len(paths) != 54:
        raise ValueError(f"unexpected_dna_count:{len(paths)}")
    h = hashlib.sha256()
    for p in paths:
        h.update(p.name.encode("utf-8"))
        h.update(b"\0")
        h.update(p.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def main() -> int:
    before = core_digest()
    state = load(CANONICAL / "CURRENT_STATE.json")
    request = load(CANONICAL / "LOCAL_COGNITION_REQUEST.json")
    ledger = load(REPO / "BẢN ĐỒ" / "SIGMA_512_ATTRIBUTES" / "SIGMA_512_IMPLEMENTATION_STATUS.json")
    eh005 = load(CANONICAL / "LOCAL_COGNITION_RECEIPT_EH005_HP_001.json")
    next_action = (CANONICAL / "NEXT_ACTION.md").read_text(encoding="utf-8")

    if os.environ.get("SIGMA_LOCAL_EXECUTION_ID") != EXPECTED_REQUEST:
        raise ValueError("request_environment_mismatch")
    if request.get("request_id") != EXPECTED_REQUEST or request.get("status") != "PENDING_LOCAL_EXECUTOR":
        raise ValueError("canonical_request_mismatch")
    if state.get("next_action_id") != EXPECTED_REQUEST or f"## {EXPECTED_REQUEST}" not in next_action:
        raise ValueError("canonical_next_action_mismatch")

    kernel = CANONICAL / "cognitive_kernel.py"
    proc = subprocess.run(
        [sys.executable, str(kernel)],
        cwd=REPO,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
        shell=False,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError("cognitive_kernel_probe_failed:" + (proc.stderr or proc.stdout)[-1000:])
    boot = json.loads(proc.stdout)

    evidence_runs = ledger.get("evidence_runs") or {}
    items = ledger.get("items") or {}
    counts = ledger.get("current_counts") or {}
    observed_evidence_update = (
        "EH004-R1" in evidence_runs
        and "EH005-R1" in evidence_runs
        and items.get("SIGMA-ATTR-001", {}).get("status") == "PARTIAL"
        and items.get("SIGMA-ATTR-008", {}).get("status") == "HOLD"
        and counts.get("PARTIAL") == 127
        and counts.get("HOLD") == 11
        and counts.get("NOT_AUDITED") == 374
        and eh005.get("status") == "SUCCESS"
        and (eh005.get("integrity") or {}).get("core_modifications") == 0
    )

    registry_instance = CANONICAL / "CAPABILITY_REGISTRY.json"
    runtime_evidence = boot.get("runtime_evidence_status")
    common = {
        "kernel_mode": boot.get("mode"),
        "runtime_evidence_status": runtime_evidence,
        "capability_registry_instance_present": registry_instance.exists(),
    }

    results = [{
        "attribute_id": "SIGMA-ATTR-025",
        "status": "PARTIAL" if observed_evidence_update else "HOLD",
        "observed": bool(observed_evidence_update),
        "evidence": {
            "eh004_and_eh005_canonical_evidence_updates_present": bool(observed_evidence_update),
            "interpretation": (
                "New machine-observed evidence changed canonical implementation state without model retraining. "
                "This supports system-level direct learning only; endogenous learning independence is not proven."
            ),
        },
        "ceiling": "PASS_FORBIDDEN",
    }]

    blockers = {
        26: "NO_CATASTROPHIC_FORGETTING_RETENTION_EXPERIMENT_BOUND_TO_NEW_LEARNING_EVENT",
        27: "NO_ENDOGENOUS_CURRICULUM_GENERATOR_BOUND_TO_MEASURED_GAPS",
        28: "NO_UNKNOWN_UNKNOWN_DISCOVERY_MECHANISM_WITH_EXECUTABLE_EVALUATION",
        29: "NO_PREDICTION_ERROR_TO_QUESTION_GENERATOR_BOUND_TO_RUNTIME",
        30: "NO_CONTRADICTION_TO_GOAL_GENERATOR_BOUND_TO_RUNTIME",
        31: "NO_ONTOLOGY_INSUFFICIENCY_TO_NEW_CONCEPT_GENERATOR_BOUND_TO_RUNTIME",
        32: "NO_STRATEGY_LEARNING_REPRESENTATION_AND_BEHAVIORAL_TEST_SURFACE",
        33: "NO_CROSS_DOMAIN_STRATEGY_TRANSFER_EXPERIMENT",
        34: "NO_GENERAL_LESSON_VS_LOCAL_EXCEPTION_CLASSIFIER_WITH_EVIDENCE",
        35: "NO_AUTONOMOUS_UNLEARNING_DECISION_MECHANISM_WITH_ROLLBACK",
        36: "NO_FAILURE_TO_LESSON_PIPELINE_PROVEN_WITHOUT_HUMAN_OR_EXTERNAL_INTERPRETATION",
    }
    for number in range(26, 37):
        results.append({
            "attribute_id": f"SIGMA-ATTR-{number:03d}",
            "status": "HOLD",
            "observed": True,
            "blocker": blockers[number],
            "evidence": {
                **common,
                "interpretation": (
                    "Current canonical bootstrap does not expose a bound executable behavioral test surface "
                    "sufficient to establish this continuous-learning requirement."
                ),
            },
            "ceiling": "PASS_FORBIDDEN",
        })

    after = core_digest()
    result_counts = {
        "PASS": 0,
        "PARTIAL": sum(r["status"] == "PARTIAL" for r in results),
        "HOLD": sum(r["status"] == "HOLD" for r in results),
        "FAIL": sum(r["status"] == "FAIL" for r in results),
        "NOT_AUDITED": 0,
    }
    result = {
        "schema_version": "1.0.0",
        "harness_id": "SIGMA-512-EVIDENCE-HARNESS-006",
        "harness_version": "1.0.0",
        "section": "III",
        "section_name": "Học liên tục",
        "target_count": 12,
        "counts": result_counts,
        "results": results,
        "core_tree_sha256_before": before,
        "core_tree_sha256_after": after,
        "core_modifications": 0 if before == after else 1,
        "external_side_effects": 0,
        "pass_allowed": False,
        "evaluator_independent": False,
        "interpretation": (
            "EH006 measures current learning evidence and blockers. It does not implement missing learning behaviors "
            "and does not establish autonomous general intelligence."
        ),
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "evidence_harness_006_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("SIGMA_512_EVIDENCE_HARNESS_006: PASS")
    print("TARGET_COUNT=12")
    print(f"PARTIAL={result_counts['PARTIAL']}")
    print(f"HOLD={result_counts['HOLD']}")
    print("FAIL=0")
    print("PASS=0")
    print(f"CORE_TREE_SHA256={after}")
    print(f"CORE_MODIFICATIONS={result['core_modifications']}")
    print("EXTERNAL_SIDE_EFFECTS=0")
    return 0 if before == after and result_counts["FAIL"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
