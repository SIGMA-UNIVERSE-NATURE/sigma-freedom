#!/usr/bin/env python3
from __future__ import annotations
import json
import py_compile
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CORE_RE = re.compile(r"^SIGMA_DNA_(\d{2})_.*\.py$")


def fail(msg):
    print(f"SIGMA_BRAIN_CONTRACT: FAIL\n{msg}", file=sys.stderr)
    raise SystemExit(1)


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"cannot parse {path}: {e}")


def main():
    manifest = load(HERE / "BRAIN_MANIFEST.json")
    root = load(HERE / "ROOT_OF_TRUST.json")
    constitution = load(HERE / "MINH_OPERATING_CONSTITUTION.json")
    state = load(HERE / "CURRENT_STATE.json")
    transfer = load(HERE / "WINDOW_TRANSFER_PROTOCOL.json")
    load(HERE / "LINEAGE.json")
    load(HERE / "DO_NOT_RERUN_LOCKS.json")

    missing = [x for x in manifest["required_files"] if not (HERE / x).exists()]
    if missing:
        fail(f"missing required files: {missing}")

    forbidden_present = [x for x in manifest.get("forbidden_public_paths", []) if (HERE / x).exists()]
    if forbidden_present:
        fail(f"private operational files present in public canonical tree: {forbidden_present}")

    public_policy = load(HERE / "RESILIENCE_PUBLIC_POLICY.json")
    if public_policy.get("classification") != "PUBLIC_SAFE":
        fail("resilience public policy must be classified PUBLIC_SAFE")
    if public_policy.get("private_plan_storage") != "AUTHORIZED_PRIVATE_OR_OFFLINE_STORE_ONLY":
        fail("private resilience plan storage boundary is missing or invalid")

    private_request = load(HERE / "PRIVATE_RESILIENCE_PLAN_REQUEST.json")
    if private_request.get("classification") != "PUBLIC_POINTER_TO_PRIVATE_WORK":
        fail("private resilience plan request classification invalid")
    if private_request.get("private_store_location_disclosure") not in {"NOT_PUBLIC", None}:
        fail("public pointer must not disclose private store location")

    # Cross-window operating constitution is a boot requirement, not advisory prose.
    if constitution.get("status") != "CANONICAL_BOOT_REQUIRED":
        fail("operating constitution is not marked CANONICAL_BOOT_REQUIRED")
    principles = constitution.get("principles", [])
    principle_ids = [p.get("id") for p in principles]
    if len(principle_ids) != len(set(principle_ids)):
        fail("duplicate operating constitution principle IDs")
    required_constitution_ids = {f"MOC-{i:03d}" for i in range(1, 21)}
    if set(principle_ids) != required_constitution_ids:
        fail(f"operating constitution IDs mismatch: {principle_ids}")
    by_id = {p["id"]: p for p in principles}
    required_names = {
        "MOC-001": "REALITY_BEFORE_IMPROVEMENT",
        "MOC-002": "SPECIFICATION_IS_NOT_IMPLEMENTATION",
        "MOC-003": "CODE_IS_NOT_BEHAVIORAL_EVIDENCE",
        "MOC-004": "PASS_REQUIRES_EVIDENCE_CONTRACT",
        "MOC-005": "NO_SELF_CERTIFICATION",
        "MOC-007": "CHAT_MEMORY_IS_NOT_CANONICAL_STATE",
        "MOC-009": "DO_NOT_REBUILD_PROVEN_FOUNDATIONS",
        "MOC-015": "MEANINGFUL_PROGRESS_UPDATES_CANONICAL_STATE",
        "MOC-016": "BASELINE_512_BEFORE_FIXING_512",
        "MOC-017": "PASS_CAN_BE_DOWNGRADED",
        "MOC-018": "EVIDENCE_OVERRULES_SELF_DESCRIPTION",
        "MOC-019": "SINGLE_NEXT_ACTION",
        "MOC-020": "SAFE_HOLD_IS_VALID",
    }
    for pid, expected_name in required_names.items():
        if by_id.get(pid, {}).get("name") != expected_name:
            fail(f"operating constitution principle {pid} missing or renamed")
    gate = constitution.get("continuation_gate", {})
    if gate.get("must_read_before_action") is not True:
        fail("operating constitution must be read before action")
    if set(gate.get("required_principle_ids", [])) != required_constitution_ids:
        fail("continuation gate does not require all operating constitution principles")
    if gate.get("required_boot_report_field") != "OPERATING_CONSTITUTION_PASS":
        fail("boot report field for operating constitution is invalid")

    # Window boot must point to both continuity and intelligence-amplification contracts.
    window_boot = (HERE / "MINH_WINDOW_BOOT.md").read_text(encoding="utf-8")
    for token in [
        "MINH BOOT SIGMA_LIFE",
        "MINH_OPERATING_CONSTITUTION.json",
        "CURRENT_STATE.json",
        "NEXT_ACTION.md",
        "INTELLIGENCE_CONTINUITY_PROGRAM.md",
        "WINDOW_TRANSFER_PROTOCOL.json",
        "OPERATING_CONSTITUTION_PASS",
        "DO NOT IMPROVE YET",
        "MEASURE CURRENT REALITY FIRST",
        "Before leaving or switching a window",
    ]:
        if token not in window_boot:
            fail(f"window boot protocol missing required token: {token}")

    # Transfer protocol prevents chat-memory handoff and ambiguous parallel mutation.
    if transfer.get("status") != "CANONICAL_TRANSFER_REQUIRED":
        fail("window transfer protocol is not canonical-required")
    if transfer.get("minimal_boot_trigger") != "MINH BOOT SIGMA_LIFE":
        fail("window transfer minimal boot trigger mismatch")
    if transfer.get("canonical_repository") != "SIGMA-UNIVERSE-NATURE/sigma-freedom":
        fail("window transfer repository mismatch")
    if transfer.get("canonical_branch") != "SIGMA_LIFE":
        fail("window transfer branch mismatch")
    executor = transfer.get("single_active_executor", {})
    if executor.get("required_for_canonical_mutation") is not True:
        fail("single active executor is not enforced for canonical mutation")
    required_outgoing = {
        "PERSIST_OBSERVED_EVIDENCE",
        "UPDATE_CURRENT_STATE_AFTER_MEANINGFUL_PROGRESS",
        "SET_EXACTLY_ONE_CANONICAL_NEXT_ACTION",
        "FETCH_AND_RECORD_CURRENT_BRANCH_HEAD_SHA",
    }
    if not required_outgoing.issubset(set(transfer.get("outgoing_window_checklist", []))):
        fail("window transfer outgoing checkpoint is incomplete")
    required_incoming = {
        "FETCH_CURRENT_HEAD_SHA",
        "READ_CURRENT_STATE",
        "READ_NEXT_ACTION",
        "INSPECT_INTERVENING_COMMITS_IF_HEAD_DIFFERS_FROM_OUTGOING_CHECKPOINT",
        "REPORT_BOOT_FIELDS_BEFORE_CLAIMING_INHERITED",
    }
    if not required_incoming.issubset(set(transfer.get("incoming_window_checklist", []))):
        fail("window transfer incoming verification is incomplete")
    transfer_program = transfer.get("current_program", {})
    if transfer_program.get("next_action") != "SIGMA-512-BASELINE-AUDIT-001":
        fail("window transfer protocol does not preserve canonical baseline next action")
    if transfer_program.get("baseline_before_broad_remediation") is not True:
        fail("window transfer protocol does not preserve baseline-before-remediation")

    # Intelligence program must explicitly use current intelligence as bootstrap capability,
    # require measurement, and preserve continuity while funding-dependent scale waits.
    intelligence = (HERE / "INTELLIGENCE_CONTINUITY_PROGRAM.md").read_text(encoding="utf-8")
    for token in [
        "CURRENT INTELLIGENCE IS BOOTSTRAP CAPABILITY",
        "SIGMA-512-BASELINE-AUDIT-001",
        "Evidence-grounded deliberation",
        "Persistent cognitive memory",
        "World model + causal model",
        "Deliberation architecture",
        "Tool, code and simulation cognition",
        "Endogenous questions and bounded goals",
        "Meta-learning",
        "Dynamic reasoning budget",
        "Single active executor rule",
        "Before every window transfer",
    ]:
        if token not in intelligence:
            fail(f"intelligence continuity program missing required token: {token}")

    continuity = state.get("continuity", {})
    if continuity.get("cross_window_boot_required") is not True:
        fail("current state does not require cross-window boot contract")
    if continuity.get("single_canonical_next_action") is not True:
        fail("current state does not enforce one canonical next action")
    if state.get("next_action_id") != "SIGMA-512-BASELINE-AUDIT-001":
        fail("canonical next action is not SIGMA-512-BASELINE-AUDIT-001")
    if state.get("operating_principle") != "DO_NOT_IMPROVE_YET_MEASURE_CURRENT_REALITY_FIRST":
        fail("baseline-before-remediation operating principle is not locked in current state")

    cores = {}
    for p in (REPO / "54_CORES").iterdir():
        if p.is_file() and (m := CORE_RE.match(p.name)):
            n = int(m.group(1))
            if n in cores:
                fail(f"duplicate core id {n}")
            cores[n] = p.name
    if set(cores) != set(range(1, 55)):
        fail(f"DNA core IDs mismatch: {sorted(cores)}")

    attrs = load(REPO / manifest["architecture"]["attributes_manifest"])
    if attrs.get("canonical_attribute_count") != 512:
        fail("canonical attribute count is not 512")

    required_invariants = {
        "NOTHING_IS_TRUE_BY_INHERITANCE",
        "NO_IMPROVEMENT_WITHOUT_DIFFERENTIAL_EVIDENCE",
        "NO_PROMOTION_WITHOUT_INDEPENDENT_EVALUATION",
        "NO_COMPONENT_MAY_CERTIFY_ITS_OWN_UNRESTRICTED_AUTHORITY",
        "IDENTITY_IS_NOT_SUBSTRATE",
    }
    if not required_invariants.issubset(set(root.get("invariants", []))):
        fail("root of trust is missing required invariants")

    manifest_invariants = manifest.get("invariants", {})
    for key in [
        "chat_memory_is_not_canonical_state",
        "cross_window_continuation_requires_boot_contract",
        "baseline_512_before_broad_remediation",
        "meaningful_progress_requires_state_update",
        "intelligence_improvement_requires_measured_evidence",
        "single_active_executor_for_canonical_mutation",
        "window_transfer_requires_verified_checkpoint",
        "current_intelligence_is_bootstrap_not_ceiling",
    ]:
        if manifest_invariants.get(key) is not True:
            fail(f"manifest continuity/intelligence invariant not enforced: {key}")

    for script in [HERE / "cognitive_kernel.py", HERE / "mirror_to_local.py"]:
        py_compile.compile(str(script), doraise=True)

    out = subprocess.check_output([sys.executable, str(HERE / "cognitive_kernel.py")], text=True, encoding="utf-8")
    report = json.loads(out)
    if report.get("structural_status") != "STRUCTURAL_PASS":
        fail(f"reference kernel boot failed: {report}")

    validator = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/validate_512_architecture.py"
    rc = subprocess.run([sys.executable, str(validator)], cwd=REPO).returncode
    if rc != 0:
        fail("SIGMA 512 contract validator failed")

    print("SIGMA_BRAIN_CONTRACT: PASS")
    print("DNA_CORES=54")
    print("CANONICAL_ATTRIBUTES=512")
    print("REFERENCE_KERNEL_BOOT=PASS")
    print("OPERATING_CONSTITUTION=PASS")
    print("CROSS_WINDOW_BOOT_PROTOCOL=PASS")
    print("WINDOW_TRANSFER_PROTOCOL=PASS")
    print("SINGLE_ACTIVE_EXECUTOR=ENFORCED")
    print("INTELLIGENCE_CONTINUITY_PROGRAM=PASS")
    print("BASELINE_512_BEFORE_FIXING_512=ENFORCED")
    print("SINGLE_CANONICAL_NEXT_ACTION=SIGMA-512-BASELINE-AUDIT-001")
    print("PUBLIC_PRIVATE_DATA_BOUNDARY=PASS")
    print("PRIVATE_OPERATIONAL_FILES_IN_PUBLIC_TREE=0")
    print("IMPLEMENTATION_EVIDENCE=NOT_AUDITED")
    print("LOCAL_E_F_MIRROR=READY_NOT_EXECUTED_IN_GITHUB_CI")


if __name__ == "__main__":
    main()
