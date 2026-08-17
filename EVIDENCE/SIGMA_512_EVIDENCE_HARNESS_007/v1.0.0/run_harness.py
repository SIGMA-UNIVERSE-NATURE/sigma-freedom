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
EXPECTED_REQUEST = "SIGMA-512-EVIDENCE-HARNESS-007-SECTION-IV-REASONING-037-048"


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
    eh006 = load(CANONICAL / "LOCAL_COGNITION_RECEIPT_EH006_HP_001.json")
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

    items = ledger.get("items") or {}
    counts = ledger.get("current_counts") or {}
    safe_hold_observed = (
        counts.get("HOLD") == 22
        and items.get("SIGMA-ATTR-008", {}).get("status") == "HOLD"
        and items.get("SIGMA-ATTR-026", {}).get("status") == "HOLD"
        and eh006.get("status") == "SUCCESS"
        and (eh006.get("result") or {}).get("counts", {}).get("HOLD") == 11
        and (eh006.get("integrity") or {}).get("core_modifications") == 0
    )

    results = [{
        "attribute_id": "SIGMA-ATTR-037",
        "status": "PARTIAL" if safe_hold_observed else "HOLD",
        "observed": bool(safe_hold_observed),
        "evidence": {
            "measured_safe_hold_count": counts.get("HOLD"),
            "kernel_mode": boot.get("mode"),
            "interpretation": (
                "The system repeatedly records HOLD rather than inventing PASS when evidence is insufficient. "
                "This supports system-level resistance to completion pressure only; model-native hallucination control is not proven."
            ),
        },
        "ceiling": "PASS_FORBIDDEN",
    }]

    blockers = {
        38: "NO_LONG_REASONING_ASSUMPTION_RETENTION_EXPERIMENT",
        39: "NO_CONCLUSION_DEPENDENCY_CHECKER_BOUND_TO_REASONING_RUNTIME",
        40: "NO_NATIVE_DEDUCTION_INDUCTION_ABDUCTION_CLASSIFICATION_BEHAVIORAL_TEST",
        41: "NO_ON_DEMAND_CAUSAL_GRAPH_CONSTRUCTION_BEHAVIORAL_TEST",
        42: "NO_STRUCTURED_MENTAL_SIMULATION_BEHAVIORAL_TEST_SURFACE",
        43: "NO_MULTI_REASONING_PATH_COMPARISON_BEFORE_COMMIT_EXPERIMENT",
        44: "NO_CIRCULAR_REASONING_DETECTOR_BOUND_TO_RUNTIME",
        45: "NO_FALSE_DICHOTOMY_DETECTOR_BOUND_TO_RUNTIME",
        46: "NO_EQUIVOCATION_TERM_MEANING_SHIFT_DETECTOR_BOUND_TO_RUNTIME",
        47: "NO_OPPONENT_LENGTH_OR_CONFIDENCE_BIAS_RESISTANCE_EXPERIMENT",
        48: "NO_NATIVE_ADVERSARIAL_SELF_DEBATE_BEHAVIORAL_ENTRYPOINT",
    }
    common = {
        "kernel_mode": boot.get("mode"),
        "runtime_evidence_status": boot.get("runtime_evidence_status"),
    }
    for number in range(38, 49):
        results.append({
            "attribute_id": f"SIGMA-ATTR-{number:03d}",
            "status": "HOLD",
            "observed": True,
            "blocker": blockers[number],
            "evidence": {
                **common,
                "interpretation": (
                    "No bound executable behavioral experiment currently establishes this reasoning requirement. "
                    "The result is HOLD, not proof of impossibility and not implementation FAIL."
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
        "harness_id": "SIGMA-512-EVIDENCE-HARNESS-007",
        "harness_version": "1.0.0",
        "section": "IV",
        "section_name": "Suy luận",
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
            "EH007 measures current reasoning evidence and blockers only. "
            "It does not add missing reasoning mechanisms."
        ),
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "evidence_harness_007_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("SIGMA_512_EVIDENCE_HARNESS_007: PASS")
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
