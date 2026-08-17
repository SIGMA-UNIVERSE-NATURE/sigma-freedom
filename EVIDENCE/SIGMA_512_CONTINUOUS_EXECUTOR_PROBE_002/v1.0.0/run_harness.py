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
EXPECTED_REQUEST = "SIGMA-512-CONTINUOUS-LOCAL-EXECUTOR-PROBE-002"
PRIOR_REQUEST = "SIGMA-512-CONTINUOUS-LOCAL-EXECUTOR-PROBE-001"
PRIOR_RECEIPT = "LOCAL_COGNITION_RECEIPT_CONTINUOUS_001.json"


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


def main() -> int:
    before = core_digest()
    state = load(CANONICAL / "CURRENT_STATE.json")
    request = load(CANONICAL / "LOCAL_COGNITION_REQUEST.json")
    bridge = load(CANONICAL / "LOCAL_EXECUTION_BRIDGE_STATUS.json")
    schema = load(CANONICAL / "LOCAL_COGNITION_RECEIPT.schema.json")
    prior = load(CANONICAL / PRIOR_RECEIPT)
    next_action = (CANONICAL / "NEXT_ACTION.md").read_text(encoding="utf-8")

    execution = request.get("execution") or {}
    autodiscovery = request.get("autodiscovery") or {}
    request_env = os.environ.get("SIGMA_LOCAL_EXECUTION_ID", "")
    prior_notes = set(prior.get("notes") or [])
    prior_integrity = prior.get("integrity") or {}
    prior_counts = (prior.get("result") or {}).get("counts") or {}
    continuous = bridge.get("continuous_executor_evidence") or {}

    checks = [
        ("ENV_REQUEST_MATCH", request_env == EXPECTED_REQUEST == request.get("request_id")),
        (
            "STATE_NEXT_ACTION_MATCH",
            state.get("next_action_id") == EXPECTED_REQUEST
            and f"## {EXPECTED_REQUEST}" in next_action,
        ),
        (
            "REQUEST_PENDING",
            request.get("status") == "PENDING_LOCAL_EXECUTOR"
            and bridge.get("pending_request_id") == EXPECTED_REQUEST,
        ),
        (
            "AUTODISCOVERY_REQUIRED",
            autodiscovery.get("required") is True
            and autodiscovery.get("human_request_id_relay_allowed") is False
            and autodiscovery.get("remote_command_file_required") is False,
        ),
        (
            "SAFETY_FLAGS_CLOSED",
            execution.get("paid_api_allowed") is False
            and execution.get("website_actions_allowed") is False
            and execution.get("dna_core_mutation_allowed") is False
            and execution.get("external_side_effects_allowed") is False
            and execution.get("network_required") is False,
        ),
        (
            "RECEIPT_SCHEMA_BOUND",
            request.get("receipt", {}).get("schema") == "LOCAL_COGNITION_RECEIPT.schema.json"
            and schema.get("title") == "SIGMA Local Cognition Receipt",
        ),
        (
            "PRIOR_AUTODISCOVERY_RECEIPT_VERIFIED",
            prior.get("request_id") == PRIOR_REQUEST
            and prior.get("status") == "SUCCESS"
            and (prior.get("executor") or {}).get("runtime_version") == "0.6.0"
            and prior_counts.get("TARGET_COUNT") == 8
            and prior_counts.get("PASS") == 0
            and prior_counts.get("FAIL") == 0
            and prior_integrity.get("core_tree_before_sha256") == prior_integrity.get("core_tree_after_sha256")
            and prior_integrity.get("core_modifications") == 0
            and prior_integrity.get("external_side_effects") == 0
            and "AUTO_DISCOVERED_FROM_CANONICAL_REQUEST=true" in prior_notes
            and "REMOTE_COMMAND_FILE_USED=false" in prior_notes
            and "CANONICAL_REQUEST_ID_NOT_HARDCODED=true" in prior_notes
            and "ARBITRARY_SHELL_USED=false" in prior_notes,
        ),
        (
            "PRIOR_REQUEST_CLOSED_BEFORE_SUCCESSOR",
            continuous.get("probe_001_request_id") == PRIOR_REQUEST
            and continuous.get("probe_001_receipt_file") == PRIOR_RECEIPT
            and continuous.get("probe_001_status") == "MACHINE_RECEIPT_VERIFIED_SINGLE_REQUEST",
        ),
        (
            "DNA_CORE_COUNT_AND_INTEGRITY",
            len([
                p for p in (REPO / "54_CORES").iterdir()
                if p.is_file() and p.name.startswith("SIGMA_DNA_")
            ]) == 54,
        ),
    ]

    after = core_digest()
    results = []
    for name, ok in checks:
        results.append({
            "probe": name,
            "observed": bool(ok),
            "status": "PARTIAL" if ok else "FAIL",
            "interpretation": (
                "Mechanism observed in second bounded successor probe; not an implementation PASS."
                if ok else
                "Required successor continuous-executor condition was not observed."
            ),
        })

    counts = {
        "PASS": 0,
        "PARTIAL": sum(1 for row in results if row["status"] == "PARTIAL"),
        "HOLD": 0,
        "FAIL": sum(1 for row in results if row["status"] == "FAIL"),
        "NOT_AUDITED": 0,
    }
    result = {
        "schema_version": "1.0.0",
        "harness_id": "SIGMA-512-CONTINUOUS-LOCAL-EXECUTOR-PROBE-002",
        "harness_version": "1.0.0",
        "scope": "SECOND_SUCCESSOR_READ_ONLY_AUTODISCOVERY_PROBE",
        "target_count": len(results),
        "counts": counts,
        "results": results,
        "core_tree_sha256_before": before,
        "core_tree_sha256_after": after,
        "core_modifications": 0 if before == after else 1,
        "external_side_effects": 0,
        "pass_allowed": False,
        "promotion_allowed": False,
    }

    OUT.mkdir(parents=True, exist_ok=True)
    result_file = OUT / "continuous_executor_probe_002_result.json"
    result_file.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("SIGMA_512_CONTINUOUS_EXECUTOR_PROBE_002: " + (
        "PASS" if counts["FAIL"] == 0 and before == after else "FAIL"
    ))
    print(f"TARGET_COUNT={len(results)}")
    print(f"PARTIAL={counts['PARTIAL']}")
    print(f"FAIL={counts['FAIL']}")
    print("PASS=0")
    print(f"CORE_TREE_SHA256={after}")
    print(f"CORE_MODIFICATIONS={result['core_modifications']}")
    print("EXTERNAL_SIDE_EFFECTS=0")
    return 0 if counts["FAIL"] == 0 and before == after else 1


if __name__ == "__main__":
    raise SystemExit(main())
