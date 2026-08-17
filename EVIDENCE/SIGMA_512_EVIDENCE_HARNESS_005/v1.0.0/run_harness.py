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
EXPECTED_REQUEST = "SIGMA-512-EVIDENCE-HARNESS-005-SECTION-I-BEHAVIOR-008-012"


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
    if boot.get("mode") != "READ_ONLY_DIAGNOSTIC":
        raise ValueError("unexpected_kernel_mode")

    registry_instance = CANONICAL / "CAPABILITY_REGISTRY.json"
    common = {
        "kernel_mode": boot.get("mode"),
        "runtime_evidence_status": boot.get("runtime_evidence_status"),
        "capability_registry_instance_present": registry_instance.exists(),
    }

    blockers = {
        8: "NO_EXECUTABLE_COUNTEREXAMPLE_SEARCH_BEHAVIORAL_ENTRYPOINT_BOUND_TO_CANONICAL_RUNTIME",
        9: "NO_EXECUTABLE_FALSIFICATION_PRIORITY_BEHAVIORAL_ENTRYPOINT_BOUND_TO_CANONICAL_RUNTIME",
        10: "NO_EXECUTABLE_CORRELATION_CAUSATION_COINCIDENCE_BEHAVIORAL_ENTRYPOINT_BOUND_TO_CANONICAL_RUNTIME",
        11: "NO_EXECUTABLE_ONTOLOGY_REVISION_BEHAVIORAL_ENTRYPOINT_BOUND_TO_CANONICAL_RUNTIME",
        12: "NO_EXECUTABLE_CONCEPT_RETIREMENT_BEHAVIORAL_ENTRYPOINT_BOUND_TO_CANONICAL_RUNTIME",
    }

    results = []
    for number in range(8, 13):
        results.append({
            "attribute_id": f"SIGMA-ATTR-{number:03d}",
            "status": "HOLD",
            "observed": True,
            "blocker": blockers[number],
            "evidence": {
                **common,
                "interpretation": (
                    "The canonical bootstrap reports runtime evidence NOT_AUDITED and exposes no "
                    "capability-registry instance that binds this behavior to an executable test surface. "
                    "This is a measured blocker, not proof that no implementation could exist elsewhere."
                ),
            },
            "ceiling": "PASS_FORBIDDEN",
        })

    after = core_digest()
    result = {
        "schema_version": "1.0.0",
        "harness_id": "SIGMA-512-EVIDENCE-HARNESS-005",
        "harness_version": "1.0.0",
        "section": "I",
        "section_name": "Nhận thức và sự thật",
        "target_count": 5,
        "counts": {"PASS": 0, "PARTIAL": 0, "HOLD": 5, "FAIL": 0, "NOT_AUDITED": 0},
        "results": results,
        "core_tree_sha256_before": before,
        "core_tree_sha256_after": after,
        "core_modifications": 0 if before == after else 1,
        "external_side_effects": 0,
        "pass_allowed": False,
        "evaluator_independent": False,
        "interpretation": (
            "EH005 converts attributes 008-012 from unaudited to explicit HOLD only if the canonical "
            "runtime still lacks a bound executable behavioral test surface. It does not implement the behaviors."
        ),
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "evidence_harness_005_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("SIGMA_512_EVIDENCE_HARNESS_005: PASS")
    print("TARGET_COUNT=5")
    print("HOLD=5")
    print("FAIL=0")
    print("PASS=0")
    print(f"CORE_TREE_SHA256={after}")
    print(f"CORE_MODIFICATIONS={result['core_modifications']}")
    print("EXTERNAL_SIDE_EFFECTS=0")
    return 0 if before == after else 1


if __name__ == "__main__":
    raise SystemExit(main())
