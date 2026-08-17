#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def fail(message: str) -> None:
    print("SIGMA_LOCAL_EXECUTION_BRIDGE_CONTRACT: FAIL", file=sys.stderr)
    print(message, file=sys.stderr)
    raise SystemExit(1)


def load(name: str) -> dict:
    path = HERE / name
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {name}: {exc}")


def main() -> None:
    manifest = load("BRAIN_MANIFEST.json")
    status = load("LOCAL_EXECUTION_BRIDGE_STATUS.json")
    schema = load("LOCAL_COGNITION_RECEIPT.schema.json")
    transfer = load("WINDOW_TRANSFER_PROTOCOL.json")
    window_boot = (HERE / "MINH_WINDOW_BOOT.md").read_text(encoding="utf-8")

    required = set(manifest.get("required_files", []))
    for name in [
        "LOCAL_EXECUTION_BRIDGE_STATUS.json",
        "LOCAL_COGNITION_RECEIPT.schema.json",
        "validate_local_execution_bridge.py",
    ]:
        if name not in required:
            fail(f"manifest does not require {name}")

    invariants = manifest.get("invariants", {})
    if invariants.get("local_execution_bridge_requires_machine_receipt_before_verified") is not True:
        fail("manifest does not enforce machine receipt before bridge VERIFIED")

    if status.get("classification") != "PUBLIC_SAFE":
        fail("bridge status must be PUBLIC_SAFE")
    if status.get("bridge_state") not in {"REPORTED_RESTORED", "AVAILABLE", "UNAVAILABLE", "HOLD"}:
        fail("invalid bridge_state")
    if status.get("epistemic_status") not in {
        "AUTHORIZED_HUMAN_REPORTED_OBSERVATION_PENDING_MACHINE_RECEIPT",
        "MACHINE_RECEIPT_VERIFIED",
        "UNVERIFIED",
        "HOLD",
    }:
        fail("invalid bridge epistemic_status")

    verified = status.get("verified_by_this_window")
    epistemic = status.get("epistemic_status")
    if epistemic != "MACHINE_RECEIPT_VERIFIED" and verified is not False:
        fail("bridge cannot be verified_by_this_window without machine receipt verification")
    if status.get("machine_receipt_required_before_verified") is not True:
        fail("machine receipt gate is not enforced")

    source = status.get("source", {})
    if source.get("operational_details_disclosure") != "PRIVATE_NOT_RECORDED_PUBLICLY":
        fail("private bridge operational details disclosure boundary missing")

    public_text = json.dumps(status, ensure_ascii=False)
    forbidden = ["REMOTE_WORKSPACE", "SIGMA_AI_BRIDGE", "WEBSITE_AUTONOMY", "\\\\SIGMA\\\\REMOTE", "C:\\\\"]
    if any(token in public_text for token in forbidden):
        fail("private local operational detail leaked into public bridge status")

    schema_required = set(schema.get("required", []))
    expected_required = {
        "schema_version", "receipt_id", "request_id", "status", "recorded_at",
        "canonical_repository", "canonical_branch", "resolved_head_sha",
        "executor", "result", "integrity", "safety",
    }
    if not expected_required.issubset(schema_required):
        fail("local cognition receipt schema missing required top-level fields")

    props = schema.get("properties", {})
    integrity_required = set(props.get("integrity", {}).get("required", []))
    if not {
        "core_tree_before_sha256", "core_tree_after_sha256", "core_modifications", "external_side_effects"
    }.issubset(integrity_required):
        fail("receipt schema missing integrity binding fields")

    safety_props = props.get("safety", {}).get("properties", {})
    if safety_props.get("paid_api_used", {}).get("const") is not False:
        fail("local cognition receipt must assert paid_api_used=false")
    if safety_props.get("secrets_disclosed", {}).get("const") is not False:
        fail("local cognition receipt must assert secrets_disclosed=false")

    if "LOCAL_EXECUTION_BRIDGE_STATUS.json" not in window_boot:
        fail("window boot does not load bridge status")
    if "LOCAL_EXECUTION_BRIDGE_STATUS / EPISTEMIC_STATUS" not in window_boot:
        fail("window boot report omits bridge epistemic status")

    current_program = transfer.get("current_program", {})
    if current_program.get("bridge_machine_receipt_required_before_verified") is not True:
        fail("window transfer does not preserve bridge receipt gate")
    if current_program.get("local_execution_bridge_status_file") != "LOCAL_EXECUTION_BRIDGE_STATUS.json":
        fail("window transfer does not point to bridge status file")
    if "READ_LOCAL_EXECUTION_BRIDGE_STATUS" not in transfer.get("incoming_window_checklist", []):
        fail("incoming transfer checklist does not read bridge status")

    print("SIGMA_LOCAL_EXECUTION_BRIDGE_CONTRACT: PASS")
    print(f"BRIDGE_STATE={status['bridge_state']}")
    print(f"EPISTEMIC_STATUS={status['epistemic_status']}")
    print("MACHINE_RECEIPT_REQUIRED_BEFORE_VERIFIED=true")
    print("PRIVATE_OPERATIONAL_DETAILS_IN_PUBLIC_STATUS=0")


if __name__ == "__main__":
    main()
