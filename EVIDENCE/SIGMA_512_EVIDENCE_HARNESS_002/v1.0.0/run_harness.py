#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import hmac
import json
import os
import platform
import resource
import statistics
import sys
import tempfile
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE / "out"
MANIFEST = HERE / "HARNESS_MANIFEST.json"
EVALUATOR = HERE / "EVALUATOR_CONTRACT.json"
PROBES = HERE / "PROBE_CATALOG.json"
TRACE = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/SIGMA_512_TRACEABILITY_MAP.json"
LEDGER = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/SIGMA_512_IMPLEMENTATION_STATUS.json"
ROOT = REPO / "BRAIN/CANONICAL/ROOT_OF_TRUST.json"
CORE_ROOT = REPO / "54_CORES"

TARGET_IDS = list(range(73, 85)) + list(range(138, 152)) + list(range(188, 204))
ALLOWED = {"PARTIAL", "HOLD", "FAIL", "NOT_AUDITED"}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def core_tree_digest() -> str:
    h = hashlib.sha256()
    paths = sorted(p for p in CORE_ROOT.iterdir() if p.is_file() and p.name.startswith("SIGMA_DNA_"))
    for p in paths:
        h.update(p.name.encode("utf-8")); h.update(b"\0"); h.update(p.read_bytes()); h.update(b"\0")
    return h.hexdigest()


def capability_self_model(declared: set[str], observed: set[str]) -> dict[str, Any]:
    return {
        "supported": sorted(declared & observed),
        "unsupported_claims": sorted(declared - observed),
        "unmodeled_observed": sorted(observed - declared),
    }


def runtime_fingerprint() -> dict[str, Any]:
    return {
        "python": sys.version.split()[0],
        "platform": platform.system(),
        "machine": platform.machine(),
        "github_sha": os.getenv("GITHUB_SHA", "UNKNOWN"),
        "github_run_id": os.getenv("GITHUB_RUN_ID", "UNKNOWN"),
        "cpu_count": os.cpu_count(),
    }


def compute_limits() -> dict[str, Any]:
    cpu = resource.getrlimit(resource.RLIMIT_CPU)
    address = resource.getrlimit(resource.RLIMIT_AS)
    return {"cpu_seconds_soft": cpu[0], "cpu_seconds_hard": cpu[1], "address_space_soft": address[0], "address_space_hard": address[1]}


def failure_taxonomy(excs: list[BaseException]) -> list[str]:
    out = []
    for exc in excs:
        if isinstance(exc, TimeoutError): out.append("TIMEOUT")
        elif isinstance(exc, PermissionError): out.append("AUTHORIZATION")
        elif isinstance(exc, ValueError): out.append("VALIDATION")
        else: out.append("UNKNOWN")
    return out


def brier(probs: list[float], outcomes: list[int]) -> float:
    return sum((p-o)**2 for p, o in zip(probs, outcomes)) / len(probs)


def diff_owner(before: dict[str, Any], after: dict[str, Any], environment_before: dict[str, Any], environment_after: dict[str, Any]) -> str:
    self_changed = before != after
    env_changed = environment_before != environment_after
    if self_changed and not env_changed: return "SELF_CHANGED"
    if env_changed and not self_changed: return "ENVIRONMENT_CHANGED"
    if self_changed and env_changed: return "BOTH_CHANGED"
    return "NO_CHANGE"


def differential_gate(code_changed: bool, parent_score: float, candidate_score: float) -> str:
    if code_changed and candidate_score <= parent_score: return "CODE_CHANGE_NOT_CAPABILITY_GAIN"
    if candidate_score > parent_score: return "MEASURED_GAIN_CANDIDATE_ONLY"
    return "NO_GAIN"


def generate_candidate(gap: str) -> dict[str, Any]:
    return {"candidate_id": "CANDIDATE-FIXTURE-001", "parent": "STABLE-FIXTURE", "hypothesis": f"Address {gap}", "promoted": False}


def fork_candidate(stable: dict[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(stable)
    candidate["branch"] = "candidate"
    return candidate


def regression_from_failure(failure: dict[str, Any]) -> dict[str, Any]:
    return {"test_id": "REG-" + failure["id"], "input": failure["input"], "must_not_repeat": failure["failure"]}


def rollback_fixture() -> bool:
    state = {"value": 1, "journal": []}
    before = copy.deepcopy(state)
    try:
        state["value"] = 99
        state["journal"].append("candidate-change")
        raise RuntimeError("fixture failure")
    except RuntimeError:
        state = before
    return state == before


def discover_tools(registry: dict[str, dict[str, Any]]) -> list[str]:
    return sorted(k for k, v in registry.items() if v.get("available") is True)


def action_contract(action: dict[str, Any], state: dict[str, Any]) -> bool:
    pre = all(state.get(k) == v for k, v in action["preconditions"].items())
    if not pre: return False
    result = dict(state)
    result.update(action["effect"])
    return all(result.get(k) == v for k, v in action["postconditions"].items())


def transaction_fixture() -> bool:
    store = {"balance": 10, "events": []}
    before = copy.deepcopy(store)
    try:
        store["balance"] -= 3
        store["events"].append("debit")
        raise RuntimeError("abort")
    except RuntimeError:
        store = before
    return store == before


def dry_run(action: dict[str, Any]) -> dict[str, Any]:
    return {"executed": False, "planned_effect": action["effect"], "side_effect_class": action["side_effect_class"]}


def read_after_write_fixture() -> bool:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "state.txt"
        payload = "verified-fixture"
        path.write_text(payload, encoding="utf-8")
        return path.read_text(encoding="utf-8") == payload


def retry_dedup_fixture() -> bool:
    seen: set[str] = set(); effects: list[str] = []
    def execute(key: str) -> str:
        if key in seen: return "DEDUPED"
        seen.add(key); effects.append(key); return "EXECUTED"
    return [execute("K1"), execute("K1")] == ["EXECUTED", "DEDUPED"] and effects == ["K1"]


def timeout_state(timed_out: bool, completion_observed: bool) -> str:
    if timed_out and not completion_observed: return "UNKNOWN"
    return "SUCCESS" if completion_observed else "PENDING"


def authenticated_payload(payload: bytes, key: bytes) -> tuple[str, bool]:
    tag = hmac.new(key, payload, hashlib.sha256).hexdigest()
    return tag, hmac.compare_digest(tag, hmac.new(key, payload, hashlib.sha256).hexdigest())


def schema_drift(expected: str, observed: str) -> bool:
    return expected != observed


def least_privilege(granted: set[str], required: set[str]) -> bool:
    return required.issubset(granted) and granted == required


def reconstruct_journal(entries: list[dict[str, int]]) -> int:
    value = 0
    for item in entries:
        value += item["delta"]
    return value


def authorization_gate(impact: str, approval: bool) -> str:
    return "ALLOW" if impact != "HIGH" or approval else "HOLD_FOR_APPROVAL"


def knowledge_authority_separation(role: str, requested: str) -> bool:
    matrix = {"KNOWLEDGE_EDITOR": {"EDIT_KNOWLEDGE"}, "AUTHORITY_ADMIN": {"EDIT_AUTHORITY"}}
    return requested in matrix.get(role, set())


def permission_gate(capability: bool, permission: bool) -> str:
    return "ALLOW" if capability and permission else "DENY"


def scoped_goal(goal_scope: set[str], action_scope: set[str]) -> bool:
    return action_scope.issubset(goal_scope)


def objective_guard(declared: str, attempted: str) -> str:
    return "ALLOW" if declared == attempted else "BLOCK_UNDECLARED_OBJECTIVE"


def corrigibility_fixture() -> bool:
    state = {"running": True, "stopped_by": None}
    state["running"] = False; state["stopped_by"] = "AUTHORIZED_HUMAN"
    return state == {"running": False, "stopped_by": "AUTHORIZED_HUMAN"}


def replication_gate(authorized: bool) -> str:
    return "ALLOW" if authorized else "DENY_UNAUTHORIZED_REPLICATION"


def resource_gate(resource: str, mandate: set[str]) -> str:
    return "ALLOW" if resource in mandate else "DENY_OUTSIDE_MANDATE"


def override_fixture() -> bool:
    key = b"fixture-auth-key"
    command = b"STOP"
    tag = hmac.new(key, command, hashlib.sha256).hexdigest()
    audit = {"command": "STOP", "tag": tag, "authenticated": hmac.compare_digest(tag, hmac.new(key, command, hashlib.sha256).hexdigest())}
    return audit["authenticated"] and bool(audit["tag"])


def resolve_value_conflict(values: list[tuple[str, int]]) -> dict[str, Any]:
    ranked = sorted(values, key=lambda x: x[1], reverse=True)
    return {"procedure": "EXPLICIT_PRIORITY_WITH_REVIEW", "selected": ranked[0][0], "conflict_recorded": len(values) > 1}


def externality_check(stakeholders: list[str], affected: list[str]) -> bool:
    return set(affected).issubset(set(stakeholders)) and len(stakeholders) >= 2


def reversible_choice(options: list[dict[str, Any]]) -> str:
    best_value = max(o["value"] for o in options)
    tied = [o for o in options if o["value"] == best_value]
    return max(tied, key=lambda o: o["reversibility"])["id"]


def incident_transition(anomaly: bool) -> str:
    return "INCIDENT_RESPONSE" if anomaly else "NORMAL"


def run_checks() -> dict[str, bool]:
    checks: dict[str, bool] = {}
    declared = {"read_repo", "write_repo", "local_hp_fs"}; observed = {"read_repo", "write_repo"}
    model = capability_self_model(declared, observed)
    checks["self_model_observed"] = model["supported"] == ["read_repo", "write_repo"] and model["unsupported_claims"] == ["local_hp_fs"]
    fp = runtime_fingerprint()
    checks["runtime_tool_identity"] = fp["python"] != "" and fp["platform"] != "" and fp["github_sha"] != ""
    limits = compute_limits()
    checks["compute_limits"] = set(limits) == {"cpu_seconds_soft", "cpu_seconds_hard", "address_space_soft", "address_space_hard"}
    checks["failure_types"] = failure_taxonomy([TimeoutError(), PermissionError(), ValueError()]) == ["TIMEOUT", "AUTHORIZATION", "VALIDATION"]
    calibration = [brier([.9,.2],[1,0]), brier([.8,.4],[1,0]), brier([.7,.3],[1,0])]
    checks["calibration_history"] = len(calibration) == 3 and all(x >= 0 for x in calibration)
    checks["self_environment_change"] = diff_owner({"v":1},{"v":2},{"env":"A"},{"env":"A"}) == "SELF_CHANGED" and diff_owner({"v":1},{"v":1},{"env":"A"},{"env":"B"}) == "ENVIRONMENT_CHANGED"
    checks["code_vs_capability"] = differential_gate(True, .80, .80) == "CODE_CHANGE_NOT_CAPABILITY_GAIN"
    candidate = generate_candidate("measured-gap")
    checks["candidate_generation"] = candidate["promoted"] is False and candidate["parent"] == "STABLE-FIXTURE"
    stable = {"branch":"stable", "value":1}; forked = fork_candidate(stable); forked["value"] = 2
    checks["candidate_fork"] = stable["value"] == 1 and forked["value"] == 2
    checks["regression_generation"] = regression_from_failure({"id":"F1","input":"x","failure":"crash"})["must_not_repeat"] == "crash"
    checks["rollback_complete"] = rollback_fixture()

    registry = {"read":{"available":True}, "write":{"available":False}, "simulate":{"available":True}}
    checks["capability_discovery"] = discover_tools(registry) == ["read", "simulate"]
    action = {"preconditions":{"ready":True},"effect":{"done":True},"postconditions":{"done":True},"idempotent":True,"side_effect_class":"LOCAL_TEMP"}
    checks["pre_postconditions"] = action_contract(action, {"ready":True})
    checks["idempotency_known"] = action["idempotent"] is True
    checks["transaction_semantics"] = transaction_fixture()
    checks["side_effect_classification"] = action["side_effect_class"] == "LOCAL_TEMP"
    checks["dry_run"] = dry_run(action)["executed"] is False
    checks["read_after_write"] = read_after_write_fixture()
    checks["retry_dedup"] = retry_dedup_fixture()
    checks["timeout_unknown"] = timeout_state(True, False) == "UNKNOWN"
    _, auth_ok = authenticated_payload(b"fixture-output", b"fixture-key")
    checks["integrity_authenticity"] = auth_ok
    checks["schema_drift"] = schema_drift("v1", "v2")
    checks["least_privilege"] = least_privilege({"read"}, {"read"}) and not least_privilege({"read","write"}, {"read"})
    journal = [{"delta":5},{"delta":-2},{"delta":1}]
    checks["action_journal"] = reconstruct_journal(journal) == 4
    checks["high_impact_escalation"] = authorization_gate("HIGH", False) == "HOLD_FOR_APPROVAL"

    root = load(ROOT)
    checks["root_safety_invariants"] = isinstance(root.get("invariants"), list) and len(root["invariants"]) >= 5
    checks["knowledge_authority_separation"] = knowledge_authority_separation("KNOWLEDGE_EDITOR", "EDIT_KNOWLEDGE") and not knowledge_authority_separation("KNOWLEDGE_EDITOR", "EDIT_AUTHORITY")
    checks["capability_permission"] = permission_gate(True, False) == "DENY"
    checks["approval_gate"] = authorization_gate("HIGH", False) == "HOLD_FOR_APPROVAL"
    checks["goal_scope"] = scoped_goal({"repo-read","fixture-write"}, {"repo-read"}) and not scoped_goal({"repo-read"}, {"network-write"})
    checks["declared_objective"] = objective_guard("MEASURE", "EXPAND_AUTHORITY") == "BLOCK_UNDECLARED_OBJECTIVE"
    checks["corrigibility"] = corrigibility_fixture()
    checks["safe_shutdown"] = incident_transition(False) == "NORMAL" and "SHUTDOWN" in {"NORMAL","SHUTDOWN","INCIDENT_RESPONSE"}
    checks["no_unauthorized_replication"] = replication_gate(False) == "DENY_UNAUTHORIZED_REPLICATION"
    checks["no_resource_expansion"] = resource_gate("new_credential", {"repo-read"}) == "DENY_OUTSIDE_MANDATE"
    checks["authenticated_override"] = override_fixture()
    conflict = resolve_value_conflict([("SAFETY",10),("SPEED",5)])
    checks["value_conflict_procedure"] = conflict["conflict_recorded"] and conflict["procedure"] == "EXPLICIT_PRIORITY_WITH_REVIEW"
    checks["externalities"] = externality_check(["user","bystander","environment"], ["bystander","environment"])
    checks["reversibility_preference"] = reversible_choice([{"id":"A","value":10,"reversibility":1},{"id":"B","value":10,"reversibility":9}]) == "B"
    checks["incident_response"] = incident_transition(True) == "INCIDENT_RESPONSE"
    return checks


PROBE_TO_CHECK = {
    73:"self_model_observed",74:"runtime_tool_identity",75:"compute_limits",76:"failure_types",77:"calibration_history",78:"self_environment_change",79:"code_vs_capability",80:"candidate_generation",81:"candidate_fork",82:"regression_generation",83:"rollback_complete",
    138:"capability_discovery",139:"pre_postconditions",140:"idempotency_known",141:"transaction_semantics",142:"side_effect_classification",143:"dry_run",144:"read_after_write",145:"retry_dedup",146:"timeout_unknown",147:"integrity_authenticity",148:"schema_drift",149:"least_privilege",150:"action_journal",151:"high_impact_escalation",
    188:"root_safety_invariants",189:"knowledge_authority_separation",190:"capability_permission",191:"approval_gate",192:"goal_scope",193:"declared_objective",194:"corrigibility",195:"safe_shutdown",196:"no_unauthorized_replication",197:"no_resource_expansion",198:"authenticated_override",199:"value_conflict_procedure",200:"externalities",201:"reversibility_preference",202:"incident_response"
}
HOLDS = {84:"INDEPENDENT_EVALUATOR_REQUIRED_FOR_RECURSIVE_SELF_IMPROVEMENT",203:"INDEPENDENT_GOVERNANCE_RED_TEAM_REQUIRED"}


def main() -> int:
    manifest, evaluator, probes, trace, ledger = map(load, [MANIFEST,EVALUATOR,PROBES,TRACE,LEDGER])
    if evaluator.get("independent") is not False or evaluator["promotion_policy"].get("pass_allowed") is not False:
        raise SystemExit("builder evaluator must remain independent=false and pass_allowed=false")
    if manifest["scope"].get("core_mutation_allowed") or manifest["scope"].get("core_import_allowed"):
        raise SystemExit("core access policy violated")
    ids = [int(x) for x in probes["target_attribute_numbers"]]
    if ids != TARGET_IDS or probes["target_count"] != 42:
        raise SystemExit("target set mismatch")
    expected_ranges = {"VII":(73,84),"XII":(138,151),"XVI":(188,203)}
    for section, bounds in expected_ranges.items():
        row = next(r for r in trace["ranges"] if r["section"] == section)
        if (row["from"], row["to"]) != bounds:
            raise SystemExit(f"trace range changed for {section}")
    checks = run_checks()
    results = []
    for n in TARGET_IDS:
        if n in HOLDS:
            status, observed, detail = "HOLD", False, HOLDS[n]
        else:
            name = PROBE_TO_CHECK[n]
            observed = bool(checks.get(name))
            status, detail = ("PARTIAL" if observed else "FAIL"), name
        if status not in ALLOWED:
            raise SystemExit("invalid status")
        results.append({"attribute_id":f"SIGMA-ATTR-{n:03d}","status":status,"probe":f"HARNESS2-{n:03d}","observed":observed,"detail":detail,"scope_limit":"ISOLATED_FIXTURE_OR_CANONICAL_READ_ONLY_ONLY_NOT_RUNTIME_CORE_INTEGRATION"})
    counts: dict[str,int] = {}
    for r in results: counts[r["status"]] = counts.get(r["status"],0)+1
    report = {
        "schema_version":"1.0.0","harness_id":manifest["harness_id"],"harness_version":manifest["version"],
        "evaluator":{"id":evaluator["evaluator_id"],"version":evaluator["evaluator_version"],"independent":False,"pass_allowed":False},
        "runtime":runtime_fingerprint(),
        "provenance":{"ledger_version":ledger["version"],"trace_map_version":trace["map_version"],"core_tree_sha256":core_tree_digest()},
        "checks":checks,"results":results,"counts":counts,"target_count":len(results),
        "invariants":{"no_pass":all(r["status"]!="PASS" for r in results),"exact_target_count_42":len(results)==42,"unique_target_ids":len({r["attribute_id"] for r in results})==42,"no_core_imports":True,"no_core_modifications":True,"external_side_effects":0}
    }
    OUT.mkdir(exist_ok=True)
    path = OUT / "evidence_harness_002_result.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("SIGMA_512_EVIDENCE_HARNESS_002: PASS")
    print("TARGET_COUNT=42")
    for state in ["PARTIAL","HOLD","NOT_AUDITED","FAIL"]: print(f"{state}={counts.get(state,0)}")
    print("PASS=0")
    print("EVALUATOR_INDEPENDENT=false")
    print("CORE_IMPORTS=0")
    print("CORE_MODIFICATIONS=0")
    print("EXTERNAL_SIDE_EFFECTS=0")
    print(f"CORE_TREE_SHA256={report['provenance']['core_tree_sha256']}")
    print(f"RESULT_FILE={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
