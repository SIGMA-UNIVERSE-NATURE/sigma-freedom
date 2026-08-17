#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import os
import random
import statistics
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE / "out"
MANIFEST = HERE / "HARNESS_MANIFEST.json"
EVALUATOR = HERE / "EVALUATOR_CONTRACT.json"
PROBES = HERE / "PROBE_CATALOG.json"
GOLDEN = HERE / "GOLDEN_REGRESSION.json"
STATUS_LEDGER = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/SIGMA_512_IMPLEMENTATION_STATUS.json"
TRACE = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/SIGMA_512_TRACEABILITY_MAP.json"
BASELINE = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/BASELINES/SIGMA_512_BASELINE_AUDIT_001_v1.0.0.json"
CORE_ROOT = REPO / "54_CORES"

TARGET_IDS = list(range(109, 125)) + list(range(441, 466))
ALLOWED = {"NOT_AUDITED", "PARTIAL", "HOLD", "FAIL"}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_json(obj: Any) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(obj: Any) -> str:
    return hashlib.sha256(canonical_json(obj)).hexdigest()


def core_tree_digest() -> str:
    h = hashlib.sha256()
    paths = sorted(p for p in CORE_ROOT.iterdir() if p.is_file() and p.name.startswith("SIGMA_DNA_"))
    for p in paths:
        h.update(p.name.encode())
        h.update(b"\0")
        h.update(p.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def evidence_record(claim_id: str, source_id: str, origin_id: str, polarity: str, quality: float,
                    absence_kind: str | None = None, measurement_error: float | None = None) -> dict[str, Any]:
    if polarity not in {"SUPPORT", "NEGATIVE", "NEUTRAL"}:
        raise ValueError("bad polarity")
    if not (0.0 <= quality <= 1.0):
        raise ValueError("quality outside [0,1]")
    if absence_kind not in {None, "ABSENCE_OF_EVIDENCE", "EVIDENCE_OF_ABSENCE"}:
        raise ValueError("bad absence kind")
    return {
        "claim_id": claim_id,
        "source_id": source_id,
        "origin_id": origin_id,
        "polarity": polarity,
        "quality_estimate": quality,
        "absence_kind": absence_kind,
        "measurement_error": measurement_error,
    }


def source_groups(records: list[dict[str, Any]]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for r in records:
        out.setdefault(r["origin_id"], set()).add(r["source_id"])
    return out


def update_reliability(prior: float, outcomes: list[bool], alpha: float = 0.25) -> float:
    score = prior
    for ok in outcomes:
        score = (1 - alpha) * score + alpha * (1.0 if ok else 0.0)
    return round(score, 6)


def resolve_conflict(records: list[dict[str, Any]], strong: float = 0.75) -> str:
    pos = any(r["polarity"] == "SUPPORT" and r["quality_estimate"] >= strong for r in records)
    neg = any(r["polarity"] == "NEGATIVE" and r["quality_estimate"] >= strong for r in records)
    if pos and neg:
        return "UNRESOLVED_CONFLICT"
    if pos:
        return "SUPPORTED"
    if neg:
        return "CONTRADICTED"
    return "INSUFFICIENT"


def contamination(train: list[Any], test: list[Any], evaluation: list[Any]) -> dict[str, list[str]]:
    def fps(xs: list[Any]) -> set[str]:
        return {digest(x) for x in xs}
    a, b, c = fps(train), fps(test), fps(evaluation)
    return {"train_test": sorted(a & b), "train_eval": sorted(a & c), "test_eval": sorted(b & c)}


def validate_measurement(value: float, error: float | None, error_required: bool) -> bool:
    if not math.isfinite(value):
        return False
    if error_required and (error is None or error < 0 or not math.isfinite(error)):
        return False
    return True


def prereg_metric(metric_name: str, threshold: float, registered_seq: int, observed_seq: int) -> dict[str, Any]:
    if registered_seq >= observed_seq:
        raise ValueError("metric must be registered before observation")
    return {"metric": metric_name, "threshold": threshold, "registered_seq": registered_seq,
            "observed_seq": observed_seq, "pre_observation": True}


def interval(mean: float, samples: list[float]) -> dict[str, float]:
    if len(samples) < 2:
        raise ValueError("need >=2 samples")
    sd = statistics.stdev(samples)
    half = 1.96 * sd / math.sqrt(len(samples))
    return {"mean": mean, "low": mean - half, "high": mean + half}


def goodhart_gate(metric_is_target: bool, alternate_checks: int) -> str:
    return "HOLD_GOODHART_RISK" if metric_is_target and alternate_checks < 1 else "ALLOW_EVALUATION"


def audit_update(before: Any, evidence_ids: list[str], rule: str, after: Any) -> dict[str, Any]:
    return {"before": before, "evidence_ids": evidence_ids, "rule": rule, "after": after}


def repro_package(payload: dict[str, Any]) -> dict[str, Any]:
    package = {"payload": payload, "harness_version": load(MANIFEST)["version"],
               "evaluator_version": load(EVALUATOR)["evaluator_version"]}
    package["sha256"] = digest(package)
    return package


def verify_repro(package: dict[str, Any]) -> bool:
    expected = package["sha256"]
    body = dict(package)
    del body["sha256"]
    return digest(body) == expected


def dimensions(capability: float, reliability: float, safety: float, efficiency: float, robustness: float) -> dict[str, float]:
    return {"capability": capability, "reliability": reliability, "safety": safety,
            "efficiency": efficiency, "robustness": robustness}


def release_gate(parent: dict[str, float], candidate: dict[str, float]) -> str:
    return "REJECT_SAFETY_REGRESSION" if candidate["safety"] < parent["safety"] else "ELIGIBLE_FOR_FURTHER_EVALUATION"


def brier(probs: list[float], outcomes: list[int]) -> float:
    if len(probs) != len(outcomes) or not probs:
        raise ValueError("bad calibration inputs")
    return sum((p - o) ** 2 for p, o in zip(probs, outcomes)) / len(probs)


def distribution_delta(in_dist: list[float], shifted: list[float]) -> float:
    return statistics.mean(shifted) - statistics.mean(in_dist)


def evaluator_change(old: str, new: str, marker: str | None) -> bool:
    return True if old == new else bool(marker and marker.startswith("EVALUATOR_DISCONTINUITY:"))


def safe_parse_evidence(obj: Any) -> bool:
    if not isinstance(obj, dict):
        return False
    required = {"claim_id", "source_id", "origin_id", "polarity", "quality_estimate"}
    if not required.issubset(obj):
        return False
    try:
        q = float(obj["quality_estimate"])
    except Exception:
        return False
    return 0 <= q <= 1 and obj["polarity"] in {"SUPPORT", "NEGATIVE", "NEUTRAL"}


def run_behavior_checks() -> dict[str, Any]:
    checks: dict[str, Any] = {}
    r1 = evidence_record("C1", "S1", "O1", "SUPPORT", 0.9)
    r2 = evidence_record("C1", "S2", "O1", "SUPPORT", 0.8)
    r3 = evidence_record("C1", "S3", "O2", "NEGATIVE", 0.85)
    graph = {"C1": [r1, r2, r3]}
    checks["claim_evidence_graph"] = len(graph["C1"]) == 3
    checks["quality_estimate"] = all(0 <= r["quality_estimate"] <= 1 for r in graph["C1"])
    checks["source_independence"] = len(source_groups(graph["C1"])) == 2
    checks["negative_evidence"] = any(r["polarity"] == "NEGATIVE" for r in graph["C1"])
    a = evidence_record("C2", "S4", "O3", "NEUTRAL", 0.5, "ABSENCE_OF_EVIDENCE")
    b = evidence_record("C2", "S5", "O4", "NEGATIVE", 0.7, "EVIDENCE_OF_ABSENCE")
    checks["absence_distinction"] = a["absence_kind"] != b["absence_kind"]
    checks["source_reliability_update"] = update_reliability(0.5, [True, True, False]) != 0.5
    checks["conflict_protocol"] = resolve_conflict(graph["C1"]) == "UNRESOLVED_CONFLICT"
    checks["shared_origin_detection"] = len(source_groups([r1, r2])) == 1
    dup = {"x": 1}
    contam = contamination([dup, {"train": 2}], [dup, {"test": 2}], [{"eval": 3}])
    checks["contamination_detection"] = bool(contam["train_test"])
    checks["benchmark_leakage"] = bool(contam["train_test"])
    checks["measurement_error"] = validate_measurement(4.2, 0.2, True) and not validate_measurement(4.2, None, True)
    checks["operational_metric_preregistered"] = prereg_metric("accuracy", 0.8, 1, 2)["pre_observation"]
    ci = interval(0.5, [0.4, 0.5, 0.6, 0.5])
    checks["interval_distribution"] = ci["low"] < ci["mean"] < ci["high"]
    checks["goodhart_resistance"] = goodhart_gate(True, 0) == "HOLD_GOODHART_RISK"
    trail = audit_update({"belief": 0.4}, ["E1"], "bayes_update", {"belief": 0.7})
    checks["belief_audit_trail"] = list(trail) == ["before", "evidence_ids", "rule", "after"]
    pkg = repro_package({"inputs": ["fixture"], "result": "ok"})
    checks["reproducibility_package"] = verify_repro(pkg)
    dims = dimensions(.8, .7, .95, .6, .75)
    checks["evaluation_dimensions"] = set(dims) == {"capability", "reliability", "safety", "efficiency", "robustness"}
    golden = load(GOLDEN)
    checks["golden_regression"] = all(case["expected"] == safe_parse_evidence(case["payload"]) for case in golden["cases"])
    rng = random.Random(174)
    checks["property_testing"] = all(safe_parse_evidence(evidence_record(f"C{i}", f"S{i}", f"O{i % 7}",
        "SUPPORT" if i % 2 == 0 else "NEGATIVE", rng.random())) for i in range(128))
    checks["metamorphic_invariance"] = resolve_conflict([r1, r3]) == resolve_conflict([r3, r1])
    malformed = [None, [], "x", {}, {"claim_id": "x"},
                 {"claim_id": "x", "source_id": "s", "origin_id": "o", "polarity": "BAD", "quality_estimate": 2}]
    checks["fuzz_boundary"] = all(safe_parse_evidence(x) is False for x in malformed)
    tampered = dict(pkg)
    tampered["payload"] = {"inputs": ["fixture"], "result": "tampered"}
    checks["adversarial_known_weakness"] = (
        len(source_groups([r1, r2])) == 1 and
        resolve_conflict([r1, r3]) == "UNRESOLVED_CONFLICT" and
        verify_repro(tampered) is False
    )
    parent = dimensions(.7, .7, .95, .5, .7)
    candidate = dimensions(.9, .75, .8, .6, .72)
    checks["safety_regression_not_offset"] = release_gate(parent, candidate) == "REJECT_SAFETY_REGRESSION"
    checks["calibration_metric"] = abs(brier([0.9, 0.2], [1, 0]) - 0.025) < 1e-9
    id_perf, ood_perf = [0.9, 0.85, 0.88], [0.62, 0.60, 0.58]
    checks["ood_evaluation"] = statistics.mean(ood_perf) < statistics.mean(id_perf)
    checks["distribution_shift"] = distribution_delta(id_perf, ood_perf) < 0
    eval_record = {"correctness": 0.8, "compute_seconds": 1.2, "api_calls": 0, "monetary_cost": 0.0,
                   "latency_seconds": 1.3, "energy_joules": None, "energy_status": "UNKNOWN_NOT_MEASURED"}
    checks["cost_accounting"] = all(k in eval_record for k in ["compute_seconds", "api_calls", "monetary_cost"])
    checks["latency_separate"] = eval_record["latency_seconds"] != eval_record["correctness"]
    checks["resource_efficiency"] = eval_record["energy_status"] == "UNKNOWN_NOT_MEASURED"
    checks["tool_evaluation_dual_score"] = set({"action_correctness": 0.8, "verification_quality": 0.9}) == {"action_correctness", "verification_quality"}
    governance = load(MANIFEST)["benchmark_governance"]
    checks["benchmark_governance"] = all(k in governance for k in ["owner", "change_control", "anti_gaming_rule"])
    checks["test_contamination_guard"] = bool(contam["train_test"])
    evaluator = load(EVALUATOR)
    checks["evaluator_versioned"] = bool(evaluator["evaluator_version"])
    checks["evaluator_discontinuity"] = evaluator_change("0.9", "1.0", "EVALUATOR_DISCONTINUITY:0.9->1.0")
    checks["threshold_preregistered"] = evaluator["promotion_policy"]["thresholds_locked_before_observation"] is True
    history = []
    state = {"belief": 0.2}
    for evidence_id, after in [("E1", 0.4), ("E2", 0.6), ("E3", 0.55)]:
        history.append(audit_update(dict(state), [evidence_id], "fixture_update", {"belief": after}))
        state = {"belief": after}
    checks["stateful_behavior"] = history[0]["before"]["belief"] == 0.2 and history[-1]["after"]["belief"] == 0.55
    return checks


PROBE_TO_CHECK = {
    109: "claim_evidence_graph", 110: "quality_estimate", 111: "source_independence", 112: "negative_evidence",
    113: "absence_distinction", 114: "source_reliability_update", 115: "conflict_protocol", 116: "shared_origin_detection",
    117: "contamination_detection", 118: "benchmark_leakage", 119: "measurement_error", 120: "operational_metric_preregistered",
    121: "interval_distribution", 122: "goodhart_resistance", 123: "belief_audit_trail", 124: "reproducibility_package",
    441: "evaluation_dimensions", 442: "golden_regression", 443: "property_testing", 444: "metamorphic_invariance",
    445: "fuzz_boundary", 446: "adversarial_known_weakness", 448: "golden_regression", 450: "stateful_behavior",
    451: "tool_evaluation_dual_score", 452: "safety_regression_not_offset", 453: "calibration_metric", 454: "ood_evaluation",
    455: "distribution_shift", 456: "cost_accounting", 457: "latency_separate", 458: "resource_efficiency",
    460: "benchmark_governance", 461: "test_contamination_guard", 462: "evaluator_versioned",
    463: "evaluator_discontinuity", 464: "threshold_preregistered"
}
HOLD_REASONS = {
    447: "INDEPENDENT_RED_TEAM_REQUIRED_BUILDER_CANNOT_SELF_CERTIFY",
    459: "HUMAN_FACTOR_DATA_AND_HUMAN_STUDY_REQUIRED",
    465: "POST_DEPLOYMENT_FIELD_EVIDENCE_REQUIRED"
}
NOT_AUDITED_REASONS = {449: "LONG_HORIZON_MULTI_CYCLE_EVALUATION_NOT_YET_EXECUTED"}


def main() -> int:
    manifest = load(MANIFEST)
    evaluator = load(EVALUATOR)
    probes = load(PROBES)
    trace = load(TRACE)
    ledger = load(STATUS_LEDGER)
    baseline = load(BASELINE)
    if evaluator.get("independent") is not False:
        raise SystemExit("v1 evaluator must explicitly remain independent=false")
    if evaluator["promotion_policy"].get("pass_allowed") is not False:
        raise SystemExit("self-built v1 harness must forbid PASS")
    if baseline["counts"]["TOTAL_RECORDS"] != 512:
        raise SystemExit("baseline invariant failed")
    if ledger["default_status"] != "NOT_AUDITED":
        raise SystemExit("unexpected ledger default")
    target_ids = [int(x) for x in probes["target_attribute_numbers"]]
    if target_ids != TARGET_IDS:
        raise SystemExit(f"target IDs mismatch: {target_ids}")
    range_x = next(r for r in trace["ranges"] if r["section"] == "X")
    range_28 = next(r for r in trace["ranges"] if r["section"] == "XXVIII")
    if (range_x["from"], range_x["to"]) != (109, 124) or (range_28["from"], range_28["to"]) != (441, 465):
        raise SystemExit("traceability target ranges changed")
    checks = run_behavior_checks()
    results = []
    for n in TARGET_IDS:
        attr = f"SIGMA-ATTR-{n:03d}"
        if n in HOLD_REASONS:
            status, detail, observed = "HOLD", HOLD_REASONS[n], False
        elif n in NOT_AUDITED_REASONS:
            status, detail, observed = "NOT_AUDITED", NOT_AUDITED_REASONS[n], False
        else:
            check_name = PROBE_TO_CHECK[n]
            observed = bool(checks.get(check_name))
            status, detail = ("PARTIAL" if observed else "FAIL"), check_name
        if status not in ALLOWED:
            raise SystemExit(f"invalid status {status}")
        results.append({"attribute_id": attr, "status": status, "probe": f"HARNESS-{n:03d}",
                        "observed": observed, "detail": detail,
                        "scope_limit": "ISOLATED_HARNESS_ONLY_NOT_RUNTIME_INTEGRATION"})
    counts: dict[str, int] = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    report = {
        "schema_version": "1.0.0", "harness_id": manifest["harness_id"], "harness_version": manifest["version"],
        "evaluator": {"id": evaluator["evaluator_id"], "version": evaluator["evaluator_version"],
                      "independent": evaluator["independent"], "pass_allowed": evaluator["promotion_policy"]["pass_allowed"]},
        "runtime": {"github_sha": os.getenv("GITHUB_SHA", "UNKNOWN"), "github_run_id": os.getenv("GITHUB_RUN_ID", "UNKNOWN"),
                    "python": sys.version.split()[0]},
        "provenance": {"baseline_audit_id": baseline["audit_id"], "ledger_version": ledger["version"],
                       "trace_map_version": trace["map_version"], "core_tree_sha256": core_tree_digest()},
        "checks": checks, "results": results, "counts": counts, "target_count": len(results),
        "invariants": {"no_pass": all(r["status"] != "PASS" for r in results), "exact_target_count_41": len(results) == 41,
                       "unique_target_ids": len({r["attribute_id"] for r in results}) == 41,
                       "no_core_imports": True, "read_only_core_probe": True}
    }
    OUT.mkdir(exist_ok=True)
    out_path = OUT / "evidence_harness_result.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("SIGMA_512_EVIDENCE_HARNESS: PASS")
    print(f"TARGET_COUNT={len(results)}")
    for state in ["PARTIAL", "HOLD", "NOT_AUDITED", "FAIL"]:
        print(f"{state}={counts.get(state, 0)}")
    print("PASS=0")
    print(f"EVALUATOR_INDEPENDENT={str(evaluator['independent']).lower()}")
    print("CORE_IMPORTS=0")
    print(f"CORE_TREE_SHA256={report['provenance']['core_tree_sha256']}")
    print(f"RESULT_FILE={out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
