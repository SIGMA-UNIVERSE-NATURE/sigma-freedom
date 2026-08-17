#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
RESULT_RE = re.compile(r"^[A-Za-z0-9_.-]+\.json$")
EVIDENCE_SCRIPT_RE = re.compile(
    r"^EVIDENCE/[A-Za-z0-9_.-]+/v[0-9][A-Za-z0-9_.-]*/run_harness\.py$"
)


def fail(message: str) -> None:
    print("SIGMA_LOCAL_EXECUTION_BRIDGE_CONTRACT: FAIL", file=sys.stderr)
    print(message, file=sys.stderr)
    raise SystemExit(1)


def load(name: str) -> dict:
    path = HERE / name
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {name}: {exc}")
    if not isinstance(value, dict):
        fail(f"{name} is not a JSON object")
    return value


def require_sha(value: object, regex: re.Pattern[str], label: str) -> str:
    text = str(value or "")
    if not regex.fullmatch(text):
        fail(f"invalid {label}: {text!r}")
    return text


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def validate_verified_capability(status: dict, required: set[str], schema_required: set[str]) -> dict:
    receipt_name = str(status.get("receipt_file") or "")
    if not receipt_name or receipt_name not in required:
        fail("machine-verified bridge has no manifest-bound receipt")
    receipt = load(receipt_name)
    missing = [name for name in schema_required if name not in receipt]
    if missing:
        fail(f"verified receipt missing required fields: {missing}")
    if receipt.get("schema_version") != "1.0.0" or receipt.get("status") != "SUCCESS":
        fail("verified bridge receipt must be schema 1.0.0 SUCCESS")
    if receipt.get("canonical_repository") != "SIGMA-UNIVERSE-NATURE/sigma-freedom":
        fail("verified receipt repository mismatch")
    if receipt.get("canonical_branch") != "SIGMA_LIFE":
        fail("verified receipt branch mismatch")

    resolved_head = require_sha(receipt.get("resolved_head_sha"), SHA40_RE, "verified receipt resolved_head_sha")
    result = receipt.get("result") or {}
    result_sha = require_sha(result.get("result_sha256"), SHA256_RE, "verified receipt result_sha256")
    if result.get("harness_id") != "SIGMA-512-EVIDENCE-HARNESS-003":
        fail("existing verified capability receipt must remain EH003")
    counts = result.get("counts") or {}
    if counts.get("TARGET_COUNT") != 44 or counts.get("PASS") != 0:
        fail("existing verified EH003 receipt count boundary changed")

    integrity = receipt.get("integrity") or {}
    before = require_sha(integrity.get("core_tree_before_sha256"), SHA256_RE, "verified core before")
    after = require_sha(integrity.get("core_tree_after_sha256"), SHA256_RE, "verified core after")
    if before != after or integrity.get("core_modifications") != 0:
        fail("existing verified capability changed DNA core integrity")
    if integrity.get("external_side_effects") != 0:
        fail("existing verified capability reports side effects")

    safety = receipt.get("safety") or {}
    if safety.get("paid_api_used") is not False or safety.get("secrets_disclosed") is not False or safety.get("external_network_side_effects") != 0:
        fail("existing verified capability violates safety receipt")

    cap = status.get("verified_capability") or {}
    if cap.get("scope") != "EH003_READ_ONLY_CANONICAL_EXECUTION_ON_AUTHORIZED_WINDOWS_SUBSTRATE":
        fail("verified capability scope changed or overgeneralized")
    if cap.get("request_id") != receipt.get("request_id"):
        fail("verified capability request does not bind receipt")
    if cap.get("resolved_head_sha") != resolved_head:
        fail("verified capability HEAD does not bind receipt")
    if cap.get("result_sha256") != result_sha:
        fail("verified capability result hash does not bind receipt")
    if cap.get("core_tree_sha256") != before:
        fail("verified capability core hash does not bind receipt")
    return receipt


def validate_pending_request(request: dict, status: dict, current_program: dict) -> None:
    request_id = str(request.get("request_id") or "")
    if not request_id:
        fail("pending request has no request_id")
    if request_id != current_program.get("next_action"):
        fail("pending request_id does not match transfer next_action")
    if current_program.get("local_cognition_request_status") != "PENDING_LOCAL_EXECUTOR":
        fail("window transfer does not record pending local request status")
    if status.get("pending_request_id") != request_id:
        fail("bridge pending_request_id does not bind pending request")

    execution = request.get("execution") or {}
    for key in ["paid_api_allowed", "website_actions_allowed", "dna_core_mutation_allowed", "external_side_effects_allowed", "network_required"]:
        if execution.get(key) is not False:
            fail(f"pending request safety field must be false: {key}")

    script = str(execution.get("script") or "").replace("\\", "/")
    if not EVIDENCE_SCRIPT_RE.fullmatch(script):
        fail("pending request script is outside bounded EVIDENCE run_harness path")
    if PurePosixPath(script).is_absolute() or ".." in PurePosixPath(script).parts:
        fail("pending request script path traversal")
    script_path = (REPO / script).resolve()
    try:
        script_path.relative_to(REPO.resolve())
    except ValueError:
        fail("pending request script escapes repository")
    if not script_path.is_file():
        fail("pending request script missing")

    script_sha = require_sha(execution.get("script_sha256"), SHA256_RE, "pending request script_sha256")
    if file_sha256(script_path) != script_sha:
        fail("pending request script SHA256 does not match canonical file")

    command = str(execution.get("command") or "").replace("\\", "/")
    if command not in {f"python {script}", f"python3 {script}"}:
        fail("pending request command is not exact bounded Python harness command")

    result_file = str(execution.get("result_file") or "")
    if not RESULT_RE.fullmatch(result_file) or "/" in result_file or "\\" in result_file:
        fail("pending request result_file is unsafe")

    autodiscovery = request.get("autodiscovery") or {}
    if autodiscovery.get("required") is not True:
        fail("pending request does not require auto-discovery")
    if autodiscovery.get("human_request_id_relay_allowed") is not False:
        fail("human request ID relay is not disabled")
    if autodiscovery.get("remote_command_file_required") is not False:
        fail("Remote Operator command file is not disabled")
    if autodiscovery.get("expected_executor_min_version") != "0.6.0":
        fail("pending continuous executor minimum version is not 0.6.0")
    require_sha(autodiscovery.get("expected_remote_operator_candidate_commit"), SHA40_RE, "pending remote operator candidate commit")

    receipt = request.get("receipt") or {}
    if receipt.get("schema") != "LOCAL_COGNITION_RECEIPT.schema.json":
        fail("pending request does not bind receipt schema")
    required_notes = set(receipt.get("required_notes") or [])
    for note in {
        "AUTO_DISCOVERED_FROM_CANONICAL_REQUEST=true",
        "REMOTE_COMMAND_FILE_USED=false",
        "CANONICAL_REQUEST_ID_NOT_HARDCODED=true",
        "ARBITRARY_SHELL_USED=false",
    }:
        if note not in required_notes:
            fail(f"pending receipt contract missing note: {note}")


def main() -> None:
    manifest = load("BRAIN_MANIFEST.json")
    status = load("LOCAL_EXECUTION_BRIDGE_STATUS.json")
    schema = load("LOCAL_COGNITION_RECEIPT.schema.json")
    transfer = load("WINDOW_TRANSFER_PROTOCOL.json")
    request = load("LOCAL_COGNITION_REQUEST.json")
    locks = load("DO_NOT_RERUN_LOCKS.json")
    window_boot = (HERE / "MINH_WINDOW_BOOT.md").read_text(encoding="utf-8")

    required = set(manifest.get("required_files") or [])
    for name in ["LOCAL_EXECUTION_BRIDGE_STATUS.json", "LOCAL_COGNITION_RECEIPT.schema.json", "validate_local_execution_bridge.py", "LOCAL_COGNITION_REQUEST.json", "LOCAL_COGNITION_RECEIPT_EH003_HP_001.json"]:
        if name not in required:
            fail(f"manifest does not require {name}")

    invariants = manifest.get("invariants") or {}
    for key in [
        "local_execution_bridge_requires_machine_receipt_before_verified",
        "verified_bridge_capability_must_not_be_overgeneralized",
        "legacy_learning_automation_must_remain_disabled",
        "continuous_local_request_requires_sha256_pinned_evidence_script",
        "continuous_local_executor_must_not_use_remote_command_file",
        "continuous_local_executor_must_not_use_arbitrary_shell",
        "continuous_local_executor_must_not_self_promote_or_invent_next_action",
    ]:
        if invariants.get(key) is not True:
            fail(f"manifest bridge/continuous invariant not enforced: {key}")

    legacy_paths = [REPO / ".github/workflows/sigma_heartbeat.yml", REPO / ".github/workflows/SIGMA_LIFE_CYCLE.yml", REPO / ".github/workflows/sigma-run.yml"]
    if any(p.exists() for p in legacy_paths):
        fail("legacy learning or arbitrary-shell workflow is active")

    lock_set = set(locks.get("locks") or [])
    for lock in [
        "DO_NOT_REENABLE_LEGACY_AUTO_LEARN_HOURLY",
        "DO_NOT_REENABLE_LEGACY_LIFE_CYCLE_HEARTBEAT_AS_COGNITION",
        "DO_NOT_REENABLE_ISSUE_BODY_ARBITRARY_SHELL",
        "DO_NOT_REENABLE_LEGACY_SELF_STUDY_OR_K_CYCLE",
        "DO_NOT_USE_REMOTE_OPERATOR_COMMAND_FILE_AS_CONTINUOUS_512_WORK_AUTHORITY",
        "DO_NOT_HARDCODE_CANONICAL_REQUEST_ID_IN_CONTINUOUS_REMOTE_OPERATOR",
        "DO_NOT_SELF_PROMOTE_CONTINUOUS_EXECUTOR_PROBE_RESULT",
    ]:
        if lock not in lock_set:
            fail(f"missing shutdown/continuous lock: {lock}")

    if status.get("classification") != "PUBLIC_SAFE":
        fail("bridge status must be PUBLIC_SAFE")
    if status.get("bridge_state") != "AVAILABLE":
        fail("bridge must remain AVAILABLE")
    if status.get("epistemic_status") != "MACHINE_RECEIPT_VERIFIED":
        fail("existing bounded bridge capability must remain machine verified")
    if status.get("verified_by_this_window") is not True:
        fail("machine-verified bridge must be verified_by_this_window")
    if status.get("machine_receipt_required_before_verified") is not True:
        fail("machine receipt gate is not enforced")

    source = status.get("source") or {}
    if source.get("operational_details_disclosure") != "PRIVATE_NOT_RECORDED_PUBLICLY":
        fail("private bridge disclosure boundary missing")

    forbidden = ["REMOTE_WORKSPACE", "SIGMA_AI_BRIDGE", "WEBSITE_AUTONOMY", "\\\\SIGMA\\\\REMOTE", "C:\\\\"]
    for obj, label in [(status, "bridge status"), (request, "local cognition request")]:
        text = json.dumps(obj, ensure_ascii=False)
        if any(token in text for token in forbidden):
            fail(f"private local operational detail leaked into public {label}")

    schema_required = set(schema.get("required") or [])
    expected_required = {
        "schema_version", "receipt_id", "request_id", "status", "recorded_at",
        "canonical_repository", "canonical_branch", "resolved_head_sha",
        "executor", "result", "integrity", "safety",
    }
    if not expected_required.issubset(schema_required):
        fail("receipt schema missing required top-level fields")

    props = schema.get("properties") or {}
    safety_props = (props.get("safety") or {}).get("properties") or {}
    if safety_props.get("paid_api_used", {}).get("const") is not False:
        fail("receipt schema does not force paid_api_used=false")
    if safety_props.get("secrets_disclosed", {}).get("const") is not False:
        fail("receipt schema does not force secrets_disclosed=false")

    if "LOCAL_EXECUTION_BRIDGE_STATUS.json" not in window_boot:
        fail("window boot does not load bridge status")
    if "LOCAL_EXECUTION_BRIDGE_STATUS / EPISTEMIC_STATUS" not in window_boot:
        fail("window boot report omits bridge epistemic status")

    current_program = transfer.get("current_program") or {}
    if current_program.get("bridge_machine_receipt_required_before_verified") is not True:
        fail("window transfer does not preserve bridge receipt gate")
    if current_program.get("local_execution_bridge_status_file") != "LOCAL_EXECUTION_BRIDGE_STATUS.json":
        fail("window transfer bridge status pointer mismatch")
    if current_program.get("legacy_learning_automation") != "DISABLED_AND_LOCKED":
        fail("window transfer does not preserve legacy shutdown")
    if current_program.get("human_request_id_relay_allowed") is not False:
        fail("window transfer allows human request ID relay")
    if current_program.get("remote_command_file_required") is not False:
        fail("window transfer requires a Remote Operator command file")

    if request.get("classification") != "PUBLIC_SAFE_REQUEST_POINTER":
        fail("local cognition request classification invalid")
    if request.get("canonical_repository") != "SIGMA-UNIVERSE-NATURE/sigma-freedom" or request.get("canonical_branch") != "SIGMA_LIFE":
        fail("local cognition request canonical source mismatch")

    validate_verified_capability(status, required, expected_required)

    request_status = request.get("status")
    if request_status == "PENDING_LOCAL_EXECUTOR":
        validate_pending_request(request, status, current_program)
    elif request_status == "COMPLETED_MACHINE_RECEIPT_VERIFIED":
        evaluation = request.get("receipt_evaluation") or {}
        if evaluation.get("status") != "VERIFIED":
            fail("completed request lacks verified receipt evaluation")
        if status.get("pending_request_id") is not None:
            fail("completed request must clear pending_request_id")
    else:
        fail(f"unsupported local cognition request status: {request_status}")

    print("SIGMA_LOCAL_EXECUTION_BRIDGE_CONTRACT: PASS")
    print(f"BRIDGE_STATE={status['bridge_state']}")
    print(f"EPISTEMIC_STATUS={status['epistemic_status']}")
    print(f"REQUEST_STATUS={request_status}")
    print(f"PENDING_REQUEST_ID={status.get('pending_request_id')}")
    print("EXISTING_VERIFIED_CAPABILITY_PRESERVED=true")
    print("CONTINUOUS_REQUEST_SHA256_PINNED=true")
    print("HUMAN_REQUEST_ID_RELAY_ALLOWED=false")
    print("REMOTE_COMMAND_FILE_REQUIRED=false")
    print("ARBITRARY_SHELL_ALLOWED=false")
    print("LEGACY_LEARNING_AUTOMATION_ACTIVE=0")
    print("PRIVATE_OPERATIONAL_DETAILS_IN_PUBLIC_STATUS=0")


if __name__ == "__main__":
    main()
