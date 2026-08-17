#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


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


def require_sha(value: object, regex: re.Pattern[str], label: str) -> str:
    text = str(value or "")
    if not regex.fullmatch(text):
        fail(f"invalid {label}: {text!r}")
    return text


def main() -> None:
    manifest = load("BRAIN_MANIFEST.json")
    status = load("LOCAL_EXECUTION_BRIDGE_STATUS.json")
    schema = load("LOCAL_COGNITION_RECEIPT.schema.json")
    transfer = load("WINDOW_TRANSFER_PROTOCOL.json")
    request = load("LOCAL_COGNITION_REQUEST.json")
    locks = load("DO_NOT_RERUN_LOCKS.json")
    window_boot = (HERE / "MINH_WINDOW_BOOT.md").read_text(encoding="utf-8")

    required = set(manifest.get("required_files", []))
    for name in [
        "LOCAL_EXECUTION_BRIDGE_STATUS.json",
        "LOCAL_COGNITION_RECEIPT.schema.json",
        "validate_local_execution_bridge.py",
        "LOCAL_COGNITION_REQUEST.json",
    ]:
        if name not in required:
            fail(f"manifest does not require {name}")

    invariants = manifest.get("invariants", {})
    if invariants.get("local_execution_bridge_requires_machine_receipt_before_verified") is not True:
        fail("manifest does not enforce machine receipt before bridge VERIFIED")
    if invariants.get("verified_bridge_capability_must_not_be_overgeneralized") is not True:
        fail("manifest does not constrain verified bridge scope")
    if invariants.get("legacy_learning_automation_must_remain_disabled") is not True:
        fail("manifest does not lock legacy learning automation off")

    legacy_paths = [
        REPO / ".github/workflows/sigma_heartbeat.yml",
        REPO / ".github/workflows/SIGMA_LIFE_CYCLE.yml",
        REPO / ".github/workflows/sigma-run.yml",
    ]
    active_legacy = [str(p.relative_to(REPO)) for p in legacy_paths if p.exists()]
    if active_legacy:
        fail(f"legacy active workflows present: {active_legacy}")

    lock_set = set(locks.get("locks", []))
    for lock in [
        "DO_NOT_REENABLE_LEGACY_AUTO_LEARN_HOURLY",
        "DO_NOT_REENABLE_LEGACY_LIFE_CYCLE_HEARTBEAT_AS_COGNITION",
        "DO_NOT_REENABLE_ISSUE_BODY_ARBITRARY_SHELL",
        "DO_NOT_REENABLE_LEGACY_SELF_STUDY_OR_K_CYCLE",
    ]:
        if lock not in lock_set:
            fail(f"missing legacy shutdown lock: {lock}")

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

    epistemic = status.get("epistemic_status")
    verified = status.get("verified_by_this_window")
    if epistemic == "MACHINE_RECEIPT_VERIFIED":
        if verified is not True:
            fail("machine-receipt-verified bridge must set verified_by_this_window=true")
    elif verified is not False:
        fail("bridge cannot be verified_by_this_window without machine receipt verification")

    if status.get("machine_receipt_required_before_verified") is not True:
        fail("machine receipt gate is not enforced")

    source = status.get("source", {})
    if source.get("operational_details_disclosure") != "PRIVATE_NOT_RECORDED_PUBLICLY":
        fail("private bridge operational details disclosure boundary missing")

    forbidden = ["REMOTE_WORKSPACE", "SIGMA_AI_BRIDGE", "WEBSITE_AUTONOMY", "\\\\SIGMA\\\\REMOTE", "C:\\\\"]
    public_text = json.dumps(status, ensure_ascii=False)
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
    if "READ_LOCAL_COGNITION_REQUEST_IF_ACTIVE" not in transfer.get("incoming_window_checklist", []):
        fail("incoming transfer checklist does not read local cognition request when active")

    if request.get("classification") != "PUBLIC_SAFE_REQUEST_POINTER":
        fail("local cognition request classification invalid")
    if request.get("canonical_repository") != "SIGMA-UNIVERSE-NATURE/sigma-freedom" or request.get("canonical_branch") != "SIGMA_LIFE":
        fail("local cognition request canonical source mismatch")
    execution = request.get("execution", {})
    if execution.get("paid_api_allowed") is not False or execution.get("dna_core_mutation_allowed") is not False or execution.get("external_side_effects_allowed") is not False:
        fail("local cognition request violates read-only safety gates")
    if request.get("receipt", {}).get("schema") != "LOCAL_COGNITION_RECEIPT.schema.json":
        fail("local cognition request does not bind the canonical receipt schema")
    request_text = json.dumps(request, ensure_ascii=False)
    if any(token in request_text for token in forbidden):
        fail("private local operational detail leaked into public local cognition request")

    request_status = request.get("status")
    receipt = None
    if request_status == "PENDING_LOCAL_EXECUTOR":
        if request.get("request_id") != current_program.get("next_action"):
            fail("pending local cognition request_id does not match transfer next_action")
        if status.get("pending_request_id") != request.get("request_id"):
            fail("pending request is not bound by bridge status")
        if epistemic == "MACHINE_RECEIPT_VERIFIED":
            fail("pending request cannot coexist with machine-receipt-verified completion state")
    elif request_status == "COMPLETED_MACHINE_RECEIPT_VERIFIED":
        evaluation = request.get("receipt_evaluation", {})
        if evaluation.get("status") != "VERIFIED":
            fail("completed local cognition request lacks VERIFIED receipt evaluation")
        receipt_name = str(evaluation.get("receipt_file") or "")
        if not receipt_name or receipt_name not in required:
            fail("verified receipt is not required by brain manifest")
        if status.get("receipt_file") != receipt_name:
            fail("bridge status receipt_file does not match request receipt evaluation")
        if current_program.get("local_cognition_request_status") != request_status:
            fail("window transfer does not record completed local cognition request status")
        if request.get("next_action") != current_program.get("next_action"):
            fail("completed request next_action does not match transfer next_action")
        if status.get("pending_request_id") is not None:
            fail("completed verified request must clear bridge pending_request_id")
        receipt = load(receipt_name)
    else:
        fail(f"unsupported local cognition request status: {request_status}")

    if epistemic == "MACHINE_RECEIPT_VERIFIED":
        if receipt is None:
            receipt_name = str(status.get("receipt_file") or "")
            if not receipt_name or receipt_name not in required:
                fail("verified bridge has no manifest-bound receipt")
            receipt = load(receipt_name)

        missing_receipt = [name for name in expected_required if name not in receipt]
        if missing_receipt:
            fail(f"receipt missing required fields: {missing_receipt}")
        if receipt.get("schema_version") != "1.0.0":
            fail("unexpected receipt schema_version")
        if receipt.get("status") != "SUCCESS":
            fail("verified bridge requires SUCCESS receipt")
        if receipt.get("request_id") != request.get("request_id"):
            fail("receipt request_id mismatch")
        if receipt.get("canonical_repository") != "SIGMA-UNIVERSE-NATURE/sigma-freedom" or receipt.get("canonical_branch") != "SIGMA_LIFE":
            fail("receipt canonical source mismatch")
        resolved_head = require_sha(receipt.get("resolved_head_sha"), SHA40_RE, "receipt resolved_head_sha")

        result = receipt.get("result", {})
        result_sha = require_sha(result.get("result_sha256"), SHA256_RE, "receipt result_sha256")
        if result.get("harness_id") != "SIGMA-512-EVIDENCE-HARNESS-003":
            fail("verified receipt harness_id mismatch")
        counts = result.get("counts", {})
        if counts.get("TARGET_COUNT") != 44 or counts.get("PASS") != 0:
            fail("verified EH003 receipt target/pass boundary mismatch")

        integrity = receipt.get("integrity", {})
        before = require_sha(integrity.get("core_tree_before_sha256"), SHA256_RE, "receipt core_tree_before_sha256")
        after = require_sha(integrity.get("core_tree_after_sha256"), SHA256_RE, "receipt core_tree_after_sha256")
        if before != after:
            fail("verified receipt core tree changed")
        if integrity.get("core_modifications") != 0:
            fail("verified receipt reports DNA core modifications")
        if integrity.get("external_side_effects") != 0:
            fail("verified receipt reports external side effects")

        safety = receipt.get("safety", {})
        if safety.get("paid_api_used") is not False or safety.get("secrets_disclosed") is not False or safety.get("external_network_side_effects") != 0:
            fail("verified receipt violates safety contract")

        cap = status.get("verified_capability", {})
        if cap.get("request_id") != receipt.get("request_id"):
            fail("verified capability request_id does not bind receipt")
        if cap.get("resolved_head_sha") != resolved_head:
            fail("verified capability resolved_head does not bind receipt")
        if cap.get("result_sha256") != result_sha:
            fail("verified capability result hash does not bind receipt")
        if cap.get("core_tree_sha256") != before:
            fail("verified capability core hash does not bind receipt")
        if cap.get("scope") != "EH003_READ_ONLY_CANONICAL_EXECUTION_ON_AUTHORIZED_WINDOWS_SUBSTRATE":
            fail("verified bridge capability scope is not bounded")

        receipt_text = json.dumps(receipt, ensure_ascii=False)
        if any(token in receipt_text for token in forbidden):
            fail("private local operational detail leaked into public receipt")

    if current_program.get("legacy_learning_automation") != "DISABLED_AND_LOCKED":
        fail("window transfer does not preserve legacy automation shutdown")

    print("SIGMA_LOCAL_EXECUTION_BRIDGE_CONTRACT: PASS")
    print(f"BRIDGE_STATE={status['bridge_state']}")
    print(f"EPISTEMIC_STATUS={status['epistemic_status']}")
    print(f"REQUEST_STATUS={request_status}")
    print("MACHINE_RECEIPT_REQUIRED_BEFORE_VERIFIED=true")
    print("PRIVATE_OPERATIONAL_DETAILS_IN_PUBLIC_STATUS=0")
    print("LEGACY_LEARNING_AUTOMATION_ACTIVE=0")


if __name__ == "__main__":
    main()
