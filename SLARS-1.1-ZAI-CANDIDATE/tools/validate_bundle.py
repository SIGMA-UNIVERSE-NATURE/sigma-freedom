#!/usr/bin/env python3
"""Validate a legacy SLARS-1.0 protocol and run bundle without ZAI.

This tool performs structural, identity, anti-leakage, set-separation and
locked-score aggregation checks. It deliberately does not generate candidate
answers or re-judge the semantic decisions made by the external evaluator.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from statistics import fmean
from typing import Any, Iterable


STANDARD_VERSION = "SLARS-1.0"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
PHASES = {"BASELINE", "IMMEDIATE", "DEVELOPMENT_RETEST", "REASONING", "DELAYED"}
TRACKS = {"P", "D", "N", "F", "X", "U", "C", "R"}
STATUSES = {"NOT_RUN", "PASS", "FAIL", "INVALID", "INSUFFICIENT_EVIDENCE", "UNVERIFIED"}
REQUIRED_REASONING_FIELDS = {
    "premise_ids",
    "constraint_checks",
    "uncertainty",
    "final_answer",
}


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    gates: dict[str, bool] = field(default_factory=dict)
    statuses: dict[str, str] = field(default_factory=dict)
    metrics: dict[str, dict[str, Any]] = field(default_factory=dict)

    def error(self, code: str, detail: str) -> None:
        self.errors.append(f"{code}: {detail}")

    def warn(self, code: str, detail: str) -> None:
        self.warnings.append(f"{code}: {detail}")

    def set_gate(self, gate: str, status: str) -> None:
        if status not in STATUSES:
            raise ValueError(f"invalid gate status: {status}")
        self.statuses[gate] = status
        self.gates[gate] = status == "PASS"


def outcome_status(
    passed: bool,
    *,
    invalid: bool = False,
    insufficient: bool = False,
    unverified: bool = False,
) -> str:
    if passed:
        return "PASS"
    if invalid:
        return "INVALID"
    if unverified:
        return "UNVERIFIED"
    if insufficient:
        return "INSUFFICIENT_EVIDENCE"
    return "FAIL"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON value must be an object")
    return value


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_sha256(value: Any) -> bool:
    return isinstance(value, str) and bool(SHA256_RE.fullmatch(value))


def is_nonzero_sha256(value: Any) -> bool:
    return is_sha256(value) and value != "0" * 64


def walk_sha_fields(value: Any, path: str = "$") -> Iterable[tuple[str, Any]]:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key.endswith("_sha256") or key.startswith("original_sha_") or key.startswith("translation_sha_") or key.startswith("protocol_sha_"):
                yield child_path, child
            yield from walk_sha_fields(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_sha_fields(child, f"{path}[{index}]")


def parse_timestamp(value: Any, field_name: str, report: Report) -> datetime | None:
    if not isinstance(value, str):
        report.error("TIMESTAMP_MISSING", field_name)
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        report.error("TIMESTAMP_INVALID", f"{field_name}={value!r}")
        return None
    if parsed.tzinfo is None:
        report.error("TIMESTAMP_NOT_UTC_AWARE", field_name)
        return None
    return parsed


def require_keys(obj: Any, keys: Iterable[str], path: str, report: Report) -> bool:
    if not isinstance(obj, dict):
        report.error("OBJECT_REQUIRED", path)
        return False
    ok = True
    for key in keys:
        if key not in obj:
            report.error("FIELD_MISSING", f"{path}.{key}")
            ok = False
    return ok


def percentile(values: list[float], q: float) -> float:
    if not values:
        return math.nan
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    location = (len(ordered) - 1) * q
    lower = math.floor(location)
    upper = math.ceil(location)
    if lower == upper:
        return ordered[lower]
    fraction = location - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def bootstrap_delta_ci(
    deltas: list[float], iterations: int, seed: int, ci_level: float
) -> tuple[float, float]:
    if not deltas:
        return math.nan, math.nan
    rng = random.Random(seed)
    count = len(deltas)
    samples = []
    for _ in range(iterations):
        samples.append(fmean(deltas[rng.randrange(count)] for _ in range(count)))
    alpha = 1 - ci_level
    return percentile(samples, alpha / 2), percentile(samples, 1 - alpha / 2)


def validate_structure(protocol: dict[str, Any], run: dict[str, Any], report: Report) -> None:
    protocol_required = [
        "standard_version", "artifact_status", "protocol_id", "protocol_lock",
        "lesson", "actors", "anti_leakage", "item_sets", "track_policies",
        "statistics", "development", "reasoning", "retention", "claim_policy",
    ]
    run_required = [
        "standard_version", "artifact_status", "run_id", "run_status",
        "protocol_sha256", "timestamps", "identity_bridge", "transport_gates",
        "exposure", "anti_leakage_evidence", "phase_artifacts",
        "development_cycles", "observations", "retention_evidence", "reported_gate_results",
        "external_verdict", "claims",
    ]
    require_keys(protocol, protocol_required, "protocol", report)
    require_keys(run, run_required, "run", report)

    if protocol.get("standard_version") != STANDARD_VERSION:
        report.error("STANDARD_VERSION_MISMATCH", "protocol")
    if run.get("standard_version") != STANDARD_VERSION:
        report.error("STANDARD_VERSION_MISMATCH", "run")

    for document_name, document in (("protocol", protocol), ("run", run)):
        for field_path, value in walk_sha_fields(document, document_name):
            if not is_sha256(value):
                report.error("SHA256_FORMAT_INVALID", field_path)

    lesson = protocol.get("lesson", {})
    require_keys(
        lesson,
        ["original_artifact_id", "original_sha256", "translation_artifact_id", "translation_sha256", "transport_evidence_id"],
        "protocol.lesson",
        report,
    )

    actors = protocol.get("actors", {})
    require_keys(actors, ["candidate", "evaluator", "toolchain"], "protocol.actors", report)
    evaluator = actors.get("evaluator", {}) if isinstance(actors, dict) else {}
    if evaluator.get("independent") is not True:
        report.error("EVALUATOR_NOT_INDEPENDENT", "protocol.actors.evaluator.independent")
    require_keys(evaluator, ["identity", "version", "configuration_sha256", "rubric_sha256", "independent"], "protocol.actors.evaluator", report)

    anti = protocol.get("anti_leakage", {})
    require_keys(
        anti,
        [
            "candidate_visible_manifest_sha256", "candidate_forbidden_manifest_sha256",
            "scan_policy_sha256", "answer_keys_accessible_to_candidate",
            "pre_vm_answer_material_allowed", "host_answer_derivation_allowed",
            "item_overlap_policy",
        ],
        "protocol.anti_leakage",
        report,
    )
    for key in ("answer_keys_accessible_to_candidate", "pre_vm_answer_material_allowed", "host_answer_derivation_allowed"):
        if anti.get(key) is not False:
            report.error("ANTI_LEAKAGE_POLICY_UNSAFE", f"{key} must be false")
    if anti.get("item_overlap_policy") != "FAMILY_MATCHED_ITEM_AND_BYTES_DISJOINT":
        report.error("ITEM_OVERLAP_POLICY_INVALID", str(anti.get("item_overlap_policy")))

    item_sets = protocol.get("item_sets", [])
    if not isinstance(item_sets, list) or not item_sets:
        report.error("ITEM_SETS_REQUIRED", "protocol.item_sets")
        item_sets = []
    seen_set_ids: set[str] = set()
    seen_item_ids: set[str] = set()
    set_hashes: dict[str, str] = {}
    phases_present: set[str] = set()
    registry: dict[str, dict[str, Any]] = {}
    for index, item_set in enumerate(item_sets):
        path = f"protocol.item_sets[{index}]"
        if not require_keys(item_set, ["set_id", "phase", "sha256", "key_sha256", "candidate_can_access_key", "items"], path, report):
            continue
        set_id = item_set.get("set_id")
        phase = item_set.get("phase")
        if set_id in seen_set_ids:
            report.error("DUPLICATE_SET_ID", str(set_id))
        seen_set_ids.add(set_id)
        registry[set_id] = item_set
        if phase not in PHASES:
            report.error("PHASE_INVALID", f"{set_id}: {phase}")
        else:
            phases_present.add(phase)
        if item_set.get("candidate_can_access_key") is not False:
            report.error("CANDIDATE_KEY_ACCESS_ALLOWED", str(set_id))
        set_hash = item_set.get("sha256")
        if set_hash in set_hashes and set_hash != "0" * 64:
            report.error("ITEM_SET_BYTES_NOT_DISJOINT", f"{set_hashes[set_hash]} and {set_id}")
        set_hashes[set_hash] = set_id
        items = item_set.get("items")
        if not isinstance(items, list) or not items:
            report.error("ITEMS_REQUIRED", str(set_id))
            continue
        local_pairs: set[tuple[str, str]] = set()
        for item_index, item in enumerate(items):
            item_path = f"{path}.items[{item_index}]"
            if not require_keys(item, ["item_id", "family_id", "track"], item_path, report):
                continue
            item_id = item.get("item_id")
            track = item.get("track")
            family_id = item.get("family_id")
            if item_id in seen_item_ids:
                report.error("ITEM_ID_REUSED", str(item_id))
            seen_item_ids.add(item_id)
            if track not in TRACKS:
                report.error("TRACK_INVALID", f"{item_id}: {track}")
            pair = (track, family_id)
            if pair in local_pairs:
                report.error("DUPLICATE_FAMILY_TRACK_IN_SET", f"{set_id}: {pair}")
            local_pairs.add(pair)

    for required_phase in ("BASELINE", "IMMEDIATE", "REASONING", "DELAYED"):
        if required_phase not in phases_present:
            report.error("REQUIRED_PHASE_MISSING", required_phase)
    if protocol.get("development", {}).get("required") is True and "DEVELOPMENT_RETEST" not in phases_present:
        report.error("REQUIRED_PHASE_MISSING", "DEVELOPMENT_RETEST")

    policies = protocol.get("track_policies", [])
    if not isinstance(policies, list) or not policies:
        report.error("TRACK_POLICIES_REQUIRED", "protocol.track_policies")
        policies = []
    seen_tracks: set[str] = set()
    for index, policy in enumerate(policies):
        path = f"protocol.track_policies[{index}]"
        required = [
            "track", "baseline_phase", "assessment_phase", "mandatory",
            "min_items", "absolute_floor", "min_effect", "ci_lower_floor",
            "retention_required",
        ]
        if not require_keys(policy, required, path, report):
            continue
        track = policy.get("track")
        if track in seen_tracks:
            report.error("DUPLICATE_TRACK_POLICY", str(track))
        seen_tracks.add(track)
        if track not in TRACKS:
            report.error("TRACK_INVALID", str(track))
        if policy.get("baseline_phase") != "BASELINE":
            report.error("BASELINE_PHASE_INVALID", str(track))
        if policy.get("assessment_phase") not in {"IMMEDIATE", "REASONING"}:
            report.error("ASSESSMENT_PHASE_INVALID", str(track))
        if not isinstance(policy.get("min_items"), int) or policy.get("min_items", 0) < 1:
            report.error("MIN_ITEMS_INVALID", str(track))
        for numeric_field in ("absolute_floor", "min_effect", "ci_lower_floor"):
            if not isinstance(policy.get(numeric_field), (int, float)):
                report.error("TRACK_THRESHOLD_INVALID", f"{track}.{numeric_field}")

    statistics = protocol.get("statistics", {})
    require_keys(statistics, ["method", "bootstrap_iterations", "bootstrap_seed", "ci_level"], "protocol.statistics", report)
    if statistics.get("method") != "PAIRED_PERCENTILE_BOOTSTRAP":
        report.error("STATISTICAL_METHOD_INVALID", str(statistics.get("method")))
    if not isinstance(statistics.get("bootstrap_iterations"), int) or statistics.get("bootstrap_iterations", 0) < 1000:
        report.error("BOOTSTRAP_ITERATIONS_INVALID", str(statistics.get("bootstrap_iterations")))

    reasoning = protocol.get("reasoning", {})
    if reasoning.get("novel_tasks_required") is not True:
        report.error("NOVEL_TASKS_NOT_REQUIRED", "protocol.reasoning")
    if reasoning.get("target_answer_absent_from_lesson_and_training") is not True:
        report.error("TARGET_ANSWER_EXCLUSION_NOT_LOCKED", "protocol.reasoning")
    if reasoning.get("hidden_chain_of_thought_requested") is not False:
        report.error("HIDDEN_CHAIN_OF_THOUGHT_REQUESTED", "must be false")
    audit_fields = set(reasoning.get("required_audit_fields", []))
    if not REQUIRED_REASONING_FIELDS.issubset(audit_fields):
        report.error("REASONING_AUDIT_FIELDS_INCOMPLETE", str(sorted(REQUIRED_REASONING_FIELDS - audit_fields)))

    retention = protocol.get("retention", {})
    require_keys(
        retention,
        [
            "required", "minimum_delay_seconds", "ratio_floor",
            "context_reset_required", "allowed_persistence_manifest_sha256",
            "hidden_lesson_reinjection_allowed", "retention_scope",
        ],
        "protocol.retention",
        report,
    )
    if retention.get("context_reset_required") is not True:
        report.error("CONTEXT_RESET_NOT_REQUIRED", "protocol.retention")
    if retention.get("hidden_lesson_reinjection_allowed") is not False:
        report.error("HIDDEN_LESSON_REINJECTION_ALLOWED", "protocol.retention")
    if retention.get("retention_scope") != "DECLARED_PERSISTENCE_CHANNELS_ONLY":
        report.error("RETENTION_SCOPE_INVALID", str(retention.get("retention_scope")))

    require_keys(
        run.get("retention_evidence", {}),
        [
            "context_reset_observed", "allowed_persistence_manifest_sha256",
            "hidden_lesson_reinjection_observed", "candidate_state_pre_delay_sha256",
            "candidate_state_at_delayed_start_sha256",
        ],
        "run.retention_evidence",
        report,
    )

    claims = run.get("claims", [])
    if not isinstance(claims, list) or not all(isinstance(value, str) for value in claims):
        report.error("CLAIMS_INVALID", "run.claims must be an array of strings")

    reported = run.get("reported_gate_results", {})
    for key in ("a0", "a1", "a2", "a3", "a4", "r1", "v1", "full_slars"):
        if reported.get(key) not in STATUSES:
            report.error("REPORTED_GATE_STATUS_INVALID", f"{key}={reported.get(key)!r}")


def index_protocol_sets(protocol: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item_set["set_id"]: item_set for item_set in protocol["item_sets"]}


def validate_phase_evidence(protocol: dict[str, Any], run: dict[str, Any], report: Report) -> dict[str, list[dict[str, Any]]]:
    sets = index_protocol_sets(protocol)
    artifacts = run.get("phase_artifacts", [])
    artifact_by_set: dict[str, dict[str, Any]] = {}
    for artifact in artifacts:
        set_id = artifact.get("set_id")
        if set_id in artifact_by_set:
            report.error("DUPLICATE_PHASE_ARTIFACT", str(set_id))
            continue
        artifact_by_set[set_id] = artifact
        source_set = sets.get(set_id)
        if source_set is None:
            report.error("UNKNOWN_PHASE_SET", str(set_id))
            continue
        if artifact.get("phase") != source_set.get("phase"):
            report.error("PHASE_ARTIFACT_PHASE_MISMATCH", str(set_id))
        if artifact.get("set_sha256") != source_set.get("sha256"):
            report.error("PHASE_ARTIFACT_SET_SHA_MISMATCH", str(set_id))
        if artifact.get("rc") != 0:
            report.error("PHASE_ARTIFACT_RC_NONZERO", f"{set_id}: {artifact.get('rc')}")
        for key in ("candidate_input_sha256", "candidate_output_sha256", "evaluator_record_sha256"):
            if not is_nonzero_sha256(artifact.get(key)):
                report.error("PHASE_ARTIFACT_HASH_MISSING", f"{set_id}.{key}")

    observations_by_set: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen_observations: set[tuple[str, str]] = set()
    required_audit_fields = set(protocol["reasoning"]["required_audit_fields"])
    for observation in run.get("observations", []):
        set_id = observation.get("set_id")
        item_id = observation.get("item_id")
        identity = (set_id, item_id)
        if identity in seen_observations:
            report.error("DUPLICATE_OBSERVATION", f"{set_id}/{item_id}")
            continue
        seen_observations.add(identity)
        source_set = sets.get(set_id)
        if source_set is None:
            report.error("OBSERVATION_UNKNOWN_SET", str(set_id))
            continue
        source_items = {item["item_id"]: item for item in source_set["items"]}
        source_item = source_items.get(item_id)
        if source_item is None:
            report.error("OBSERVATION_UNKNOWN_ITEM", f"{set_id}/{item_id}")
            continue
        for key in ("phase", "family_id", "track"):
            expected = source_set["phase"] if key == "phase" else source_item[key]
            if observation.get(key) != expected:
                report.error("OBSERVATION_BINDING_MISMATCH", f"{set_id}/{item_id}.{key}")
        score = observation.get("external_score")
        confidence = observation.get("confidence")
        if not isinstance(score, (int, float)) or not 0 <= score <= 1:
            report.error("EXTERNAL_SCORE_INVALID", f"{set_id}/{item_id}")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            report.error("CONFIDENCE_INVALID", f"{set_id}/{item_id}")
        artifact = artifact_by_set.get(set_id)
        if artifact and observation.get("candidate_output_sha256") != artifact.get("candidate_output_sha256"):
            report.error("OBSERVATION_OUTPUT_HASH_MISMATCH", f"{set_id}/{item_id}")
        if not is_nonzero_sha256(observation.get("evaluator_record_sha256")):
            report.error("EVALUATOR_RECORD_HASH_MISSING", f"{set_id}/{item_id}")
        if source_set["phase"] == "REASONING":
            audit_record = observation.get("audit_record")
            if not isinstance(audit_record, dict):
                report.error("REASONING_AUDIT_RECORD_MISSING", f"{set_id}/{item_id}")
            else:
                missing = required_audit_fields - set(audit_record)
                if missing:
                    report.error("REASONING_AUDIT_FIELDS_MISSING", f"{set_id}/{item_id}: {sorted(missing)}")
        observations_by_set[set_id].append(observation)

    for set_id, source_set in sets.items():
        if set_id not in artifact_by_set:
            report.error("PHASE_ARTIFACT_MISSING", set_id)
        observed_ids = {item["item_id"] for item in observations_by_set.get(set_id, [])}
        expected_ids = {item["item_id"] for item in source_set["items"]}
        if observed_ids != expected_ids:
            missing = sorted(expected_ids - observed_ids)
            extra = sorted(observed_ids - expected_ids)
            report.error("OBSERVATION_COVERAGE_INCOMPLETE", f"{set_id}: missing={missing}, extra={extra}")
    return observations_by_set


def observations_for_phase_track(
    protocol: dict[str, Any],
    observations_by_set: dict[str, list[dict[str, Any]]],
    phase: str,
    track: str,
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for item_set in protocol["item_sets"]:
        if item_set["phase"] == phase:
            result.extend(obs for obs in observations_by_set.get(item_set["set_id"], []) if obs["track"] == track)
    return result


def paired_metric(
    pre: list[dict[str, Any]],
    post: list[dict[str, Any]],
    policy: dict[str, Any],
    statistics: dict[str, Any],
) -> dict[str, Any]:
    pre_by_family = {item["family_id"]: item for item in pre}
    post_by_family = {item["family_id"]: item for item in post}
    families = sorted(set(pre_by_family) & set(post_by_family))
    deltas = [post_by_family[family]["external_score"] - pre_by_family[family]["external_score"] for family in families]
    pre_scores = [pre_by_family[family]["external_score"] for family in families]
    post_scores = [post_by_family[family]["external_score"] for family in families]
    ci_low, ci_high = bootstrap_delta_ci(
        deltas,
        statistics["bootstrap_iterations"],
        statistics["bootstrap_seed"],
        statistics["ci_level"],
    )
    metric = {
        "n": len(families),
        "pre": fmean(pre_scores) if pre_scores else math.nan,
        "post": fmean(post_scores) if post_scores else math.nan,
        "delta": fmean(deltas) if deltas else math.nan,
        "ci_low": ci_low,
        "ci_high": ci_high,
    }
    metric["pass"] = bool(
        metric["n"] >= policy["min_items"]
        and metric["post"] >= policy["absolute_floor"]
        and metric["delta"] >= policy["min_effect"]
        and metric["ci_low"] >= policy["ci_lower_floor"]
    )
    if "brier_max" in policy:
        brier = fmean((item["confidence"] - (1.0 if item["correct"] else 0.0)) ** 2 for item in post) if post else math.nan
        metric["brier"] = brier
        metric["pass"] = metric["pass"] and brier <= policy["brier_max"]
    return metric


def evaluate_evidence(
    protocol: dict[str, Any],
    run: dict[str, Any],
    actual_protocol_sha: str,
    report: Report,
) -> None:
    # A0: lock, identity and blind boundary.
    a0 = True
    a0_invalid = False
    a0_unverified = False
    if protocol.get("artifact_status") != "LOCKED_PROTOCOL" or protocol.get("protocol_lock", {}).get("status") != "LOCKED":
        report.error("PROTOCOL_NOT_LOCKED", "artifact_status/status")
        a0 = False
        a0_unverified = True
    if run.get("artifact_status") != "RUN_EVIDENCE" or run.get("run_status") != "COMPLETE":
        report.error("RUN_NOT_COMPLETE_EVIDENCE", "artifact_status/run_status")
        a0 = False
        a0_unverified = True
    if run.get("protocol_sha256") != actual_protocol_sha:
        report.error("PROTOCOL_FILE_SHA_MISMATCH", f"reported={run.get('protocol_sha256')} actual={actual_protocol_sha}")
        a0 = False
        a0_invalid = True

    lock_time = parse_timestamp(protocol.get("protocol_lock", {}).get("locked_at_utc"), "protocol.locked_at_utc", report)
    timestamps = run.get("timestamps", {})
    start_time = parse_timestamp(timestamps.get("run_started_at_utc"), "run.run_started_at_utc", report)
    complete_time = parse_timestamp(timestamps.get("run_completed_at_utc"), "run.run_completed_at_utc", report)
    exposure_start = parse_timestamp(timestamps.get("exposure_started_at_utc"), "run.exposure_started_at_utc", report)
    exposure_complete = parse_timestamp(timestamps.get("exposure_completed_at_utc"), "run.exposure_completed_at_utc", report)
    delayed_start = parse_timestamp(timestamps.get("delayed_started_at_utc"), "run.delayed_started_at_utc", report)
    if any(value is None for value in (lock_time, start_time, complete_time, exposure_start, exposure_complete, delayed_start)):
        a0 = False
        a0_unverified = True
    if lock_time and start_time and not lock_time < start_time:
        report.error("PROTOCOL_LOCK_NOT_BEFORE_RUN", "locked_at_utc must be earlier than run start")
        a0 = False
        a0_invalid = True
    if start_time and complete_time and not start_time < complete_time:
        report.error("RUN_TIME_ORDER_INVALID", "start must be before completion")
        a0 = False
        a0_invalid = True
    if start_time and exposure_start and exposure_complete and complete_time:
        if not start_time <= exposure_start < exposure_complete <= complete_time:
            report.error("EXPOSURE_TIME_ORDER_INVALID", "exposure must be within run interval")
            a0 = False
            a0_invalid = True

    identity = run.get("identity_bridge", {})
    original_values = [
        identity.get("original_sha_auth"), identity.get("original_sha_g1_pre"),
        identity.get("original_sha_g1_final"), identity.get("original_sha_g3_target"),
        identity.get("original_sha_run_final"), protocol.get("lesson", {}).get("original_sha256"),
    ]
    translation_values = [
        identity.get("translation_sha_reviewed"), identity.get("translation_sha_sigmac_input"),
        identity.get("translation_sha_g3_target"), identity.get("translation_sha_exposed"),
        identity.get("translation_sha_run_final"), protocol.get("lesson", {}).get("translation_sha256"),
    ]
    protocol_values = [
        run.get("protocol_sha256"), identity.get("protocol_sha_locked"),
        identity.get("protocol_sha_at_run_start"), identity.get("protocol_sha_reported"),
        actual_protocol_sha,
    ]
    if len(set(original_values)) != 1:
        report.error("ORIGINAL_IDENTITY_BRIDGE_FAIL", str(original_values))
        a0 = False
        a0_invalid = True
    if len(set(translation_values)) != 1:
        report.error("TRANSLATION_IDENTITY_BRIDGE_FAIL", str(translation_values))
        a0 = False
        a0_invalid = True
    if len(set(protocol_values)) != 1:
        report.error("PROTOCOL_IDENTITY_BRIDGE_FAIL", str(protocol_values))
        a0 = False
        a0_invalid = True

    transport_values = list(run.get("transport_gates", {}).values())
    transport_pass = bool(transport_values and all(value == "PASS" for value in transport_values))
    transport_status = "PASS"
    if not transport_pass:
        if any(value == "INVALID" for value in transport_values):
            transport_status = "INVALID"
        elif any(value in {"UNVERIFIED", "NOT_RUN"} for value in transport_values):
            transport_status = "UNVERIFIED"
        elif any(value == "INSUFFICIENT_EVIDENCE" for value in transport_values):
            transport_status = "INSUFFICIENT_EVIDENCE"
        else:
            transport_status = "FAIL"
    if not transport_pass:
        report.error("TRANSPORT_GATES_NOT_ALL_PASS", str(run.get("transport_gates")))
    report.set_gate("TRANSPORT", transport_status)

    policy_anti = protocol.get("anti_leakage", {})
    evidence_anti = run.get("anti_leakage_evidence", {})
    anti_pass = bool(
        evidence_anti.get("scan_policy_sha256") == policy_anti.get("scan_policy_sha256")
        and evidence_anti.get("scan_rc") == 0
        and evidence_anti.get("match_count") == 0
        and evidence_anti.get("host_answer_derivation_observed") is False
        and evidence_anti.get("candidate_key_access_observed") is False
        and is_nonzero_sha256(evidence_anti.get("raw_scanner_transcript_sha256"))
    )
    if not anti_pass:
        report.error("ANTI_LEAKAGE_EVIDENCE_FAIL", str(evidence_anti))
        a0 = False
        anti_unverified = any(
            evidence_anti.get(key) is None
            for key in ("scan_rc", "match_count", "host_answer_derivation_observed", "candidate_key_access_observed")
        ) or not is_nonzero_sha256(evidence_anti.get("raw_scanner_transcript_sha256"))
        if anti_unverified:
            a0_unverified = True
        else:
            a0_invalid = True
    else:
        anti_unverified = False
    report.set_gate("A0", outcome_status(a0, invalid=a0_invalid, unverified=a0_unverified))

    exposure = run.get("exposure", {})
    a2 = bool(
        identity.get("translation_sha_exposed") == protocol.get("lesson", {}).get("translation_sha256")
        and is_nonzero_sha256(exposure.get("candidate_input_transcript_sha256"))
        and exposure.get("allowed_context_manifest_matches") is True
        and exposure.get("forbidden_context_match_count") == 0
        and exposure.get("tool_policy_matches") is True
        and exposure.get("evaluator_key_visible") is False
        and anti_pass
    )
    if not a2:
        report.error("CONTROLLED_EXPOSURE_FAIL", str(exposure))
    a2_invalid = bool(
        exposure.get("evaluator_key_visible") is True
        or (isinstance(exposure.get("forbidden_context_match_count"), int) and exposure.get("forbidden_context_match_count") > 0)
        or (not anti_pass and not anti_unverified)
    )
    a2_unverified = bool(
        not is_nonzero_sha256(exposure.get("candidate_input_transcript_sha256"))
        or exposure.get("allowed_context_manifest_matches") is not True
        or exposure.get("tool_policy_matches") is not True
        or anti_unverified
    )
    report.set_gate("A2", outcome_status(a2, invalid=a2_invalid, unverified=a2_unverified))

    phase_error_start = len(report.errors)
    observations_by_set = validate_phase_evidence(protocol, run, report)
    phase_errors = report.errors[phase_error_start:]
    phase_invalid_prefixes = (
        "DUPLICATE_PHASE_ARTIFACT", "UNKNOWN_PHASE_SET",
        "PHASE_ARTIFACT_PHASE_MISMATCH", "PHASE_ARTIFACT_SET_SHA_MISMATCH",
        "PHASE_ARTIFACT_RC_NONZERO", "DUPLICATE_OBSERVATION",
        "OBSERVATION_UNKNOWN_SET", "OBSERVATION_UNKNOWN_ITEM",
        "OBSERVATION_BINDING_MISMATCH", "OBSERVATION_OUTPUT_HASH_MISMATCH",
    )
    phase_invalid = any(error.startswith(phase_invalid_prefixes) for error in phase_errors)
    phase_insufficient = bool(phase_errors) and not phase_invalid
    policies = {policy["track"]: policy for policy in protocol["track_policies"]}
    stats = protocol["statistics"]

    # A1: baseline coverage and externally-bound records.
    a1 = True
    a1_insufficient = False
    for track, policy in policies.items():
        baseline = observations_for_phase_track(protocol, observations_by_set, "BASELINE", track)
        if len(baseline) < policy["min_items"]:
            report.error("BASELINE_TRACK_INSUFFICIENT", f"{track}: {len(baseline)} < {policy['min_items']}")
            a1 = False
            a1_insufficient = True
    report.set_gate(
        "A1",
        outcome_status(
            a1,
            invalid=report.statuses.get("A0") == "INVALID" or phase_invalid,
            unverified=report.statuses.get("A0") == "UNVERIFIED",
            insufficient=a1_insufficient or phase_insufficient,
        ),
    )

    # A3 and R1: locked paired score aggregation.
    immediate_results: list[bool] = []
    reasoning_results: list[bool] = []
    immediate_insufficient = False
    reasoning_insufficient = False
    for track, policy in policies.items():
        baseline = observations_for_phase_track(protocol, observations_by_set, policy["baseline_phase"], track)
        assessment = observations_for_phase_track(protocol, observations_by_set, policy["assessment_phase"], track)
        metric = paired_metric(baseline, assessment, policy, stats)
        report.metrics[track] = metric
        if policy["mandatory"] and policy["assessment_phase"] == "IMMEDIATE":
            immediate_results.append(metric["pass"])
            immediate_insufficient = immediate_insufficient or metric["n"] < policy["min_items"]
        if policy["mandatory"] and policy["assessment_phase"] == "REASONING":
            reasoning_results.append(metric["pass"])
            reasoning_insufficient = reasoning_insufficient or metric["n"] < policy["min_items"]
    a3 = bool(immediate_results and all(immediate_results) and anti_pass)
    r1 = bool(reasoning_results and all(reasoning_results) and anti_pass)
    if not a3:
        report.error("ACQUISITION_TRACKS_FAIL", "one or more mandatory IMMEDIATE tracks failed")
    if not r1:
        report.error("REASONING_TRACKS_FAIL", "one or more mandatory REASONING tracks failed")
    invalid_assessment = report.statuses.get("A0") == "INVALID" or report.statuses.get("A2") == "INVALID" or phase_invalid
    unverified_assessment = report.statuses.get("A0") == "UNVERIFIED" or report.statuses.get("A2") == "UNVERIFIED"
    report.set_gate(
        "A3",
        outcome_status(a3, invalid=invalid_assessment, unverified=unverified_assessment, insufficient=immediate_insufficient or phase_insufficient),
    )
    report.set_gate(
        "R1",
        outcome_status(r1, invalid=invalid_assessment, unverified=unverified_assessment, insufficient=reasoning_insufficient or phase_insufficient),
    )

    # A4: every cycle must be authorized, fresh and improve its target tracks.
    development_policy = protocol["development"]
    cycles = sorted(run.get("development_cycles", []), key=lambda value: value.get("cycle_number", 0))
    a4 = True
    a4_invalid = False
    a4_insufficient = False
    if development_policy.get("required"):
        if not cycles:
            report.error("DEVELOPMENT_CYCLES_MISSING", "at least one cycle required")
            a4 = False
            a4_insufficient = True
        if len(cycles) > development_policy["max_cycles"]:
            report.error("DEVELOPMENT_CYCLE_LIMIT_EXCEEDED", str(len(cycles)))
            a4 = False
            a4_invalid = True
        expected_numbers = list(range(1, len(cycles) + 1))
        if [cycle.get("cycle_number") for cycle in cycles] != expected_numbers:
            report.error("DEVELOPMENT_CYCLE_SEQUENCE_INVALID", str([cycle.get("cycle_number") for cycle in cycles]))
            a4 = False
            a4_invalid = True
        previous_set_for_track: dict[str, str] = {}
        sets = index_protocol_sets(protocol)
        for cycle in cycles:
            cycle_number = cycle.get("cycle_number")
            retest_set_id = cycle.get("retest_set_id")
            retest_set = sets.get(retest_set_id)
            if cycle.get("error_class") not in development_policy["error_taxonomy"]:
                report.error("DEVELOPMENT_ERROR_CLASS_INVALID", f"cycle {cycle_number}")
                a4 = False
                a4_invalid = True
            if cycle.get("no_evaluation_key_leakage") is not True or cycle.get("rubric_unchanged") is not True:
                report.error("DEVELOPMENT_BOUNDARY_FAIL", f"cycle {cycle_number}")
                a4 = False
                a4_invalid = True
            if not retest_set or retest_set.get("phase") != "DEVELOPMENT_RETEST" or retest_set.get("cycle_number") != cycle_number:
                report.error("DEVELOPMENT_RETEST_BINDING_FAIL", f"cycle {cycle_number}: {retest_set_id}")
                a4 = False
                a4_invalid = True
                continue
            for track in cycle.get("target_tracks", []):
                policy = policies.get(track)
                if policy is None:
                    report.error("DEVELOPMENT_TARGET_TRACK_UNKNOWN", str(track))
                    a4 = False
                    a4_invalid = True
                    continue
                post = [item for item in observations_by_set.get(retest_set_id, []) if item["track"] == track]
                if track in previous_set_for_track:
                    pre = [item for item in observations_by_set.get(previous_set_for_track[track], []) if item["track"] == track]
                else:
                    pre = observations_for_phase_track(protocol, observations_by_set, policy["assessment_phase"], track)
                metric = paired_metric(pre, post, policy, stats)
                report.metrics[f"DEV{cycle_number}:{track}"] = metric
                if not metric["pass"]:
                    report.error("DEVELOPMENT_TARGET_TRACK_FAIL", f"cycle {cycle_number}, track {track}")
                    a4 = False
                    a4_insufficient = a4_insufficient or metric["n"] < policy["min_items"]
                previous_set_for_track[track] = retest_set_id
    report.set_gate(
        "A4",
        outcome_status(
            a4,
            invalid=a4_invalid or invalid_assessment,
            unverified=unverified_assessment,
            insufficient=a4_insufficient or phase_insufficient,
        ),
    )

    # V1: delayed fresh-set performance and retention ratio.
    v1 = True
    v1_invalid = False
    v1_insufficient = False
    retention_policy = protocol["retention"]
    if retention_policy.get("required"):
        retention_evidence = run.get("retention_evidence", {})
        persistence_boundary_pass = bool(
            retention_evidence.get("context_reset_observed") is True
            and retention_evidence.get("allowed_persistence_manifest_sha256")
            == retention_policy.get("allowed_persistence_manifest_sha256")
            and retention_evidence.get("hidden_lesson_reinjection_observed") is False
            and is_nonzero_sha256(retention_evidence.get("candidate_state_pre_delay_sha256"))
            and is_nonzero_sha256(retention_evidence.get("candidate_state_at_delayed_start_sha256"))
        )
        if not persistence_boundary_pass:
            report.error("RETENTION_PERSISTENCE_BOUNDARY_FAIL", str(retention_evidence))
            v1 = False
            if (
                retention_evidence.get("context_reset_observed") is None
                or retention_evidence.get("hidden_lesson_reinjection_observed") is None
                or not is_nonzero_sha256(retention_evidence.get("candidate_state_pre_delay_sha256"))
                or not is_nonzero_sha256(retention_evidence.get("candidate_state_at_delayed_start_sha256"))
            ):
                v1_insufficient = True
            else:
                v1_invalid = True
        if exposure_complete and delayed_start:
            elapsed = (delayed_start - exposure_complete).total_seconds()
            if elapsed < retention_policy["minimum_delay_seconds"]:
                report.error("RETENTION_DELAY_TOO_SHORT", f"{elapsed} < {retention_policy['minimum_delay_seconds']}")
                v1 = False
                v1_invalid = True
        else:
            v1 = False
            v1_insufficient = True
        for track, policy in policies.items():
            if not policy.get("retention_required"):
                continue
            reference = observations_for_phase_track(protocol, observations_by_set, policy["assessment_phase"], track)
            delayed = observations_for_phase_track(protocol, observations_by_set, "DELAYED", track)
            reference_by_family = {item["family_id"]: item for item in reference}
            delayed_by_family = {item["family_id"]: item for item in delayed}
            families = sorted(set(reference_by_family) & set(delayed_by_family))
            if len(families) < policy["min_items"]:
                report.error("RETENTION_TRACK_INSUFFICIENT", f"{track}: {len(families)} < {policy['min_items']}")
                v1 = False
                v1_insufficient = True
                continue
            reference_mean = fmean(reference_by_family[family]["external_score"] for family in families)
            delayed_mean = fmean(delayed_by_family[family]["external_score"] for family in families)
            ratio = delayed_mean / reference_mean if reference_mean > 0 else math.nan
            report.metrics[f"RETENTION:{track}"] = {
                "n": len(families), "reference": reference_mean,
                "delayed": delayed_mean, "ratio": ratio,
                "pass": bool(delayed_mean >= policy["absolute_floor"] and ratio >= retention_policy["ratio_floor"]),
            }
            if not report.metrics[f"RETENTION:{track}"]["pass"]:
                report.error("RETENTION_TRACK_FAIL", track)
                v1 = False
    report.set_gate(
        "V1",
        outcome_status(
            v1,
            invalid=v1_invalid or invalid_assessment,
            unverified=unverified_assessment,
            insufficient=v1_insufficient or phase_insufficient,
        ),
    )

    external = run.get("external_verdict", {})
    external_pass = bool(
        external.get("status") == "PASS"
        and external.get("evaluator_identity") == protocol["actors"]["evaluator"]["identity"]
        and external.get("rubric_sha256") == protocol["actors"]["evaluator"]["rubric_sha256"]
        and is_nonzero_sha256(external.get("report_sha256"))
        and external.get("bound_to_candidate_output_hashes") is True
    )
    if not external_pass:
        report.error("EXTERNAL_VERDICT_BINDING_FAIL", str(external))
    external_declared_status = external.get("status")
    if external_pass:
        external_status = "PASS"
    elif external_declared_status in {"UNVERIFIED", "NOT_RUN"}:
        external_status = "UNVERIFIED"
    elif external_declared_status == "INSUFFICIENT_EVIDENCE":
        external_status = "INSUFFICIENT_EVIDENCE"
    elif external_declared_status == "FAIL":
        external_status = "FAIL"
    else:
        external_status = "INVALID"
    report.set_gate("EXTERNAL", external_status)

    allowed_claims = set(protocol["claim_policy"]["allowed"])
    forbidden_tokens = protocol["claim_policy"]["forbidden"]
    claims_valid = True
    for claim in run.get("claims", []):
        if claim not in allowed_claims:
            report.error("CLAIM_NOT_ALLOWLISTED", claim)
            claims_valid = False
        if any(token in claim for token in forbidden_tokens):
            report.error("FORBIDDEN_CLAIM_TOKEN", claim)
            claims_valid = False

    component_statuses = [
        report.statuses[gate]
        for gate in ("TRANSPORT", "A0", "A1", "A2", "A3", "A4", "R1", "V1", "EXTERNAL")
    ]
    if not claims_valid or "INVALID" in component_statuses:
        full_status = "INVALID"
    elif "UNVERIFIED" in component_statuses or "NOT_RUN" in component_statuses:
        full_status = "UNVERIFIED"
    elif "INSUFFICIENT_EVIDENCE" in component_statuses:
        full_status = "INSUFFICIENT_EVIDENCE"
    elif "FAIL" in component_statuses:
        full_status = "FAIL"
    else:
        full_status = "PASS"
    report.set_gate("FULL_SLARS", full_status)

    expected_reported = {
        "a0": report.statuses["A0"],
        "a1": report.statuses["A1"],
        "a2": report.statuses["A2"],
        "a3": report.statuses["A3"],
        "a4": report.statuses["A4"],
        "r1": report.statuses["R1"],
        "v1": report.statuses["V1"],
        "full_slars": report.statuses["FULL_SLARS"],
    }
    reported_mismatch = False
    for gate_name, expected_value in expected_reported.items():
        reported_value = run.get("reported_gate_results", {}).get(gate_name)
        if reported_value != expected_value:
            report.error("REPORTED_GATE_DISAGREES_WITH_RECOMPUTATION", f"{gate_name}: reported={reported_value}, computed={expected_value}")
            reported_mismatch = True
    if reported_mismatch:
        report.set_gate("FULL_SLARS", "INVALID")


def print_report(mode: str, report: Report) -> None:
    structure_valid = not any(
        error.startswith((
            "FIELD_MISSING", "OBJECT_REQUIRED", "STANDARD_VERSION_MISMATCH",
            "SHA256_FORMAT_INVALID", "ITEM_SETS_REQUIRED", "ITEMS_REQUIRED",
            "DUPLICATE_SET_ID", "ITEM_ID_REUSED", "TRACK_INVALID",
            "DUPLICATE_TRACK_POLICY", "TRACK_POLICIES_REQUIRED",
        ))
        for error in report.errors
    )
    print(f"STANDARD_VERSION={STANDARD_VERSION}")
    print("VALIDATOR_SCOPE=LEGACY_SLARS_1_0_WITHOUT_ZAI")
    print(f"MODE={mode.upper()}")
    print(f"STRUCTURE_VALID={'YES' if structure_valid else 'NO'}")
    if mode == "structure":
        print("ACTUAL_GATE_EXECUTION=UNVERIFIED")
        print("ACTUAL_ACQUISITION_EVIDENCE=UNVERIFIED")
        print("ACTUAL_REASONING_DEVELOPMENT_EVIDENCE=UNVERIFIED")
    else:
        for gate in ("A0", "A1", "A2", "A3", "A4", "R1", "V1"):
            print(f"{gate}={report.statuses.get(gate, 'UNVERIFIED')}")
        print(f"LEGACY_FULL_SLARS_1_0={report.statuses.get('FULL_SLARS', 'UNVERIFIED')}")
        print("EXTERNAL_SCORE_CONTENT_REJUDGED=NO")
        print(
            "LEGACY_SLARS_1_0_CORE_PACKAGE_PASS="
            + ("YES" if report.gates.get("FULL_SLARS") else "NO")
        )
        print("SLARS_1_1_ZAI_INTEGRATION=NOT_EVALUATED")
        print("FULL_SLARS_1_1_PACKAGE_PASS=NO")
    print("ERROR_COUNT=" + str(len(report.errors)))
    print("WARNING_COUNT=" + str(len(report.warnings)))
    if report.metrics:
        print("TRACK_METRICS=" + json.dumps(json_safe(report.metrics), sort_keys=True, separators=(",", ":"), allow_nan=False))
    for error in report.errors:
        print("ERROR=" + error)
    for warning in report.warnings:
        print("WARNING=" + warning)


def json_safe(value: Any) -> Any:
    """Replace non-finite floats so diagnostics always remain valid JSON."""
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {key: json_safe(child) for key, child in value.items()}
    if isinstance(value, list):
        return [json_safe(child) for child in value]
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", required=True, type=Path)
    parser.add_argument("--run", required=True, type=Path)
    parser.add_argument("--mode", choices=("structure", "evidence"), default="structure")
    args = parser.parse_args(argv)

    try:
        protocol = load_json(args.protocol)
        run = load_json(args.run)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"STRUCTURE_VALID=NO\nERROR=JSON_LOAD_FAILED: {exc}")
        return 1

    report = Report()
    validate_structure(protocol, run, report)
    structural_error_count = len(report.errors)
    if args.mode == "evidence" and structural_error_count == 0:
        evaluate_evidence(protocol, run, file_sha256(args.protocol), report)
    print_report(args.mode, report)

    if structural_error_count:
        return 1
    if args.mode == "evidence" and not report.gates.get("FULL_SLARS"):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
