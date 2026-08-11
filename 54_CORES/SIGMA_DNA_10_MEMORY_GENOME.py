#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-10: MEMORY GENOME
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_10_MEMORY_GENOME.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol, Tuple


SIGMA_ROOT = Path(r"E:\SIGMA")
CORE54_ROOT = SIGMA_ROOT / "RUNTIME" / "CORE54"
GENES_ROOT = CORE54_ROOT / "GENES"
DNA_JSON = (
    SIGMA_ROOT
    / "CORE"
    / "DNA_CANON"
    / "SIGMA_CORE_DNA_54"
    / "sigma_dna_54.json"
)

CANON_DNA10: Dict[str, str] = {
    "id": "DNA-10",
    "name": "Memory Genome",
    "purpose": (
        "Phân tách working, episodic, hypothesis, verified, rejected "
        "và strategy memory."
    ),
    "system": "learning",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
LEARNING_WORLD_SCHEMA = "SIGMA_LEARNING_WORLD_V1"
VERIFICATION_WALL_SCHEMA = (
    "SIGMA_INDEPENDENT_VERIFICATION_WALL_V1"
)
MEMORY_GENOME_SCHEMA = "SIGMA_MEMORY_GENOME_V1"

MEMORY_CLASSES = [
    "working",
    "episodic",
    "hypothesis",
    "verified",
    "rejected",
    "strategy",
]

MEMORY_GENOME_CONTRACT: Dict[str, Any] = {
    "schema": MEMORY_GENOME_SCHEMA,
    "memory_class_count": 6,
    "memory_classes": deepcopy(MEMORY_CLASSES),
    "class_separation_required": True,
    "storage_scope": "CURRENT_STRUCTURED_STATE",
    "persistent_memory_runtime_started": False,
    "knowledge_promotion_authority": False,
    "neural_learning_started": False,
    "external_storage_write": False,
    "derivation": "DIRECT_FROM_CANON_PURPOSE",
}


class CoreStateLike(Protocol):
    behavior_bound: bool


class CoreUnitLike(Protocol):
    core_id: str
    name: str
    purpose: str
    system: str
    state: CoreStateLike

    def activate(self, payload: Any = None) -> Dict[str, Any]:
        ...


class Core54Like(Protocol):
    auto_learning_enabled: bool
    model_calls_enabled: bool
    external_execution_enabled: bool
    canon_write_enabled: bool

    def get(self, core_id: str) -> CoreUnitLike:
        ...

    def bind(self, core_id: str, handler: Any) -> None:
        ...


def _canon_record(core: CoreUnitLike) -> Dict[str, str]:
    return {
        "id": core.core_id,
        "name": core.name,
        "purpose": core.purpose,
        "system": core.system,
    }


def _sha256_json(value: Any) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=repr,
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA10:
        raise RuntimeError(
            "DNA-10_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA10, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Tuple[
    Dict[str, Any],
    Dict[str, Any],
    Dict[str, Any],
    Dict[str, Any],
]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-10_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("content"), dict):
        raise TypeError(
            "context['cognitive_state']['content'] must be a dict"
        )

    if not isinstance(state.get("uncertainty"), dict):
        raise TypeError(
            "context['cognitive_state']['uncertainty'] must be a dict"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    learning_world = state.get("learning_world")
    if not isinstance(learning_world, dict):
        raise RuntimeError(
            "DNA-08_LEARNING_WORLD_REQUIRED"
        )

    learning_contract = learning_world.get("contract")
    if not isinstance(learning_contract, dict):
        raise RuntimeError(
            "DNA-08_LEARNING_WORLD_CONTRACT_REQUIRED"
        )

    if learning_contract.get("schema") != LEARNING_WORLD_SCHEMA:
        raise ValueError(
            "DNA-10_LEARNING_WORLD_SCHEMA_MISMATCH:"
            f"{learning_contract.get('schema')!r}"
        )

    if not isinstance(learning_world.get("events"), list):
        raise TypeError(
            "learning_world['events'] must be a list"
        )

    verification_wall = state.get(
        "independent_verification_wall"
    )
    if not isinstance(verification_wall, dict):
        raise RuntimeError(
            "DNA-09_INDEPENDENT_VERIFICATION_WALL_REQUIRED"
        )

    verification_contract = verification_wall.get("contract")
    if not isinstance(verification_contract, dict):
        raise RuntimeError(
            "DNA-09_VERIFICATION_WALL_CONTRACT_REQUIRED"
        )

    if verification_contract.get("schema") != (
        VERIFICATION_WALL_SCHEMA
    ):
        raise ValueError(
            "DNA-10_VERIFICATION_WALL_SCHEMA_MISMATCH:"
            f"{verification_contract.get('schema')!r}"
        )

    if not isinstance(
        verification_wall.get("evaluations"),
        list,
    ):
        raise TypeError(
            "independent_verification_wall['evaluations'] "
            "must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError(
            "DNA-08_AND_DNA-09_OUTPUTS_REQUIRED"
        )

    dna08_output = outputs.get("DNA-08")
    if not isinstance(dna08_output, dict):
        raise RuntimeError("DNA-08_OUTPUT_REQUIRED")

    dna09_output = outputs.get("DNA-09")
    if not isinstance(dna09_output, dict):
        raise RuntimeError("DNA-09_OUTPUT_REQUIRED")

    return (
        state,
        learning_world,
        verification_wall,
        dna09_output,
    )


def _install_memory_genome(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("memory_genome")

    expected = {
        "contract": deepcopy(MEMORY_GENOME_CONTRACT),
        "segments": {
            memory_class: []
            for memory_class in MEMORY_CLASSES
        },
        "routing_events": [],
    }

    if existing is None:
        state["memory_genome"] = expected
        return state["memory_genome"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['memory_genome'] must be a dict"
        )

    if existing.get("contract") != MEMORY_GENOME_CONTRACT:
        raise ValueError(
            "DNA-10_MEMORY_GENOME_CONTRACT_CONFLICT"
        )

    segments = existing.get("segments")
    if not isinstance(segments, dict):
        raise TypeError(
            "memory_genome['segments'] must be a dict"
        )

    if list(segments.keys()) != MEMORY_CLASSES:
        raise ValueError(
            "DNA-10_EXACT_MEMORY_CLASS_ORDER_REQUIRED"
        )

    for memory_class in MEMORY_CLASSES:
        if not isinstance(segments[memory_class], list):
            raise TypeError(
                "memory_genome segment must be a list:"
                f"{memory_class}"
            )

    if not isinstance(existing.get("routing_events"), list):
        raise TypeError(
            "memory_genome['routing_events'] must be a list"
        )

    return existing


def _append_unique(
    genome: Dict[str, Any],
    memory_class: str,
    source: str,
    payload: Any,
    status: str,
) -> Dict[str, Any]:
    if memory_class not in MEMORY_CLASSES:
        raise ValueError(
            f"DNA-10_UNKNOWN_MEMORY_CLASS:{memory_class}"
        )

    record_content = {
        "memory_class": memory_class,
        "source": source,
        "payload": deepcopy(payload),
        "status": status,
    }
    record_sha256 = _sha256_json(record_content)

    segment: List[Dict[str, Any]] = (
        genome["segments"][memory_class]
    )
    for existing in segment:
        if existing.get("record_sha256") == record_sha256:
            return existing

    sequence = len(segment) + 1
    record = {
        "record_id": (
            f"DNA-10-{memory_class.upper()}-{sequence:04d}"
        ),
        **record_content,
        "record_sha256": record_sha256,
        "persistent_memory_runtime_used": False,
    }
    segment.append(record)

    genome["routing_events"].append(
        {
            "sequence": len(genome["routing_events"]) + 1,
            "record_id": record["record_id"],
            "memory_class": memory_class,
            "source": source,
            "record_sha256": record_sha256,
            "status": "ROUTED",
        }
    )

    return record


def _route_working_memory(
    state: Dict[str, Any],
    genome: Dict[str, Any],
) -> Dict[str, Any]:
    payload = {
        "content": deepcopy(state["content"]),
        "uncertainty": deepcopy(state["uncertainty"]),
    }
    return _append_unique(
        genome,
        "working",
        "DNA-03",
        payload,
        "ACTIVE_STRUCTURED_STATE",
    )


def _route_episodic_memory(
    learning_world: Dict[str, Any],
    genome: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    events = learning_world["events"]
    if not events:
        return None

    event = events[-1]
    if not isinstance(event, dict):
        raise TypeError(
            "DNA-08 learning-world event must be a dict"
        )

    if (
        event.get("complete") is not True
        or event.get("status")
        != "EXPERIENTIAL_EVENT_QUALIFIED"
    ):
        return None

    return _append_unique(
        genome,
        "episodic",
        "DNA-08",
        event,
        "EXPERIENCE_RECORDED",
    )


def _candidate_route_class(
    candidate: Optional[Dict[str, Any]],
    evaluation: Optional[Dict[str, Any]],
) -> Optional[str]:
    if candidate is None:
        return None

    if not isinstance(evaluation, dict):
        return "hypothesis"

    if evaluation.get("promotion_allowed") is True:
        return "verified"

    verification_record = evaluation.get(
        "verification_record"
    )
    explicit_verifier_result = bool(
        isinstance(verification_record, dict)
        and verification_record
        and "passed" in verification_record
    )
    candidate_bound = (
        evaluation.get("candidate_bound") is True
    )
    verification_failed = (
        evaluation.get("verification_passed") is False
    )

    if (
        explicit_verifier_result
        and candidate_bound
        and verification_failed
    ):
        return "rejected"

    return "hypothesis"


def _route_candidate_memory(
    dna09_output: Dict[str, Any],
    genome: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    candidate = dna09_output.get("candidate")
    if candidate is not None and not isinstance(candidate, dict):
        raise TypeError(
            "DNA-09 candidate must be a dict or None"
        )

    evaluation = dna09_output.get("evaluation")
    if evaluation is not None and not isinstance(
        evaluation,
        dict,
    ):
        raise TypeError(
            "DNA-09 evaluation must be a dict or None"
        )

    memory_class = _candidate_route_class(
        candidate,
        evaluation,
    )
    if memory_class is None:
        return None

    status_by_class = {
        "hypothesis": "UNVERIFIED_CANDIDATE",
        "verified": "INDEPENDENTLY_VERIFIED_CANDIDATE",
        "rejected": "VERIFIER_REJECTED_CANDIDATE",
    }

    payload = {
        "candidate": deepcopy(candidate),
        "evaluation": deepcopy(evaluation),
    }
    return _append_unique(
        genome,
        memory_class,
        "DNA-09",
        payload,
        status_by_class[memory_class],
    )


def _route_strategy_memory(
    state: Dict[str, Any],
    genome: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    persistence = state.get("persistent_existence")
    if not isinstance(persistence, dict):
        return None

    active_goal = persistence.get("active_goal")
    active_strategy = persistence.get("active_strategy")
    recovery_events = persistence.get("recovery_events")

    if recovery_events is not None and not isinstance(
        recovery_events,
        list,
    ):
        raise TypeError(
            "persistent_existence['recovery_events'] "
            "must be a list"
        )

    if (
        active_goal is None
        and active_strategy is None
        and not recovery_events
    ):
        return None

    payload = {
        "active_goal": deepcopy(active_goal),
        "active_strategy": deepcopy(active_strategy),
        "latest_recovery_event": deepcopy(
            recovery_events[-1]
            if recovery_events
            else None
        ),
    }
    return _append_unique(
        genome,
        "strategy",
        "DNA-07",
        payload,
        "ACTIVE_STRATEGY_STATE",
    )


def _segment_counts(
    genome: Dict[str, Any],
) -> Dict[str, int]:
    return {
        memory_class: len(
            genome["segments"][memory_class]
        )
        for memory_class in MEMORY_CLASSES
    }


def _assert_segment_separation(
    genome: Dict[str, Any],
) -> None:
    record_ids: List[str] = []
    for memory_class in MEMORY_CLASSES:
        for record in genome["segments"][memory_class]:
            if record.get("memory_class") != memory_class:
                raise AssertionError(
                    "DNA-10_MEMORY_CLASS_MISMATCH"
                )
            record_ids.append(record["record_id"])

    if len(record_ids) != len(set(record_ids)):
        raise AssertionError(
            "DNA-10_RECORD_ID_COLLISION"
        )


def dna10_memory_genome(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Separate current structured memory artifacts into exactly six Canon
    classes: working, episodic, hypothesis, verified, rejected, strategy.

    DNA-10 creates an in-context memory genome only. It does not start
    persistent Memory Runtime, Learning Runtime, neural learning, model
    calls, F174 execution, external storage, external action, or Canon
    writes.
    """
    assert_exact_canon(core)

    context: Dict[str, Any]
    if isinstance(payload, dict):
        context = deepcopy(payload)
    else:
        context = {"input": deepcopy(payload)}

    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("context['trace'] must be a list")
    trace.append("DNA-10")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    (
        state,
        learning_world,
        _verification_wall,
        dna09_output,
    ) = _validate_dependencies(context)

    genome = _install_memory_genome(state)
    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-10",
            "operation": "MEMORY_GENOME_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "memory_genome_schema": MEMORY_GENOME_SCHEMA,
            "memory_class_count": 6,
            "persistent_memory_runtime_started": False,
        }
    )

    routed_records = {
        "working": _route_working_memory(
            state,
            genome,
        ),
        "episodic": _route_episodic_memory(
            learning_world,
            genome,
        ),
        "candidate": _route_candidate_memory(
            dna09_output,
            genome,
        ),
        "strategy": _route_strategy_memory(
            state,
            genome,
        ),
    }

    _assert_segment_separation(genome)
    counts = _segment_counts(genome)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-10",
            "operation": "MEMORY_CLASSES_SEPARATED",
            "canonical_sha256": canonical_sha256,
            "segment_counts": deepcopy(counts),
            "persistent_memory_runtime_used": False,
        }
    )

    outputs["DNA-10"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "memory_genome_contract": deepcopy(
            MEMORY_GENOME_CONTRACT
        ),
        "segment_counts": deepcopy(counts),
        "routed_records": deepcopy(routed_records),
        "persistent_memory_runtime_used": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna10(core54: Core54Like) -> None:
    core = core54.get("DNA-10")
    assert_exact_canon(core)
    core54.bind(
        "DNA-10",
        dna10_memory_genome,
    )


def _build_base_probe() -> Dict[str, Any]:
    return {
        "trace": [],
        "caller_data": {"preserve": True},
        "goal": {
            "id": "GOAL-DNA10",
            "statement": "preserve separated memory classes",
        },
        "strategy": "STRATEGY-A",
        "next_strategy": "STRATEGY-B",
        "failure": {
            "detected": True,
            "layer": "verification",
            "recovery_operation": "REFRAME",
            "reason": "FIRST_STRATEGY_FAILED",
        },
        "environment": {
            "id": "WORLD-DNA10-SELF-CHECK",
            "state": "INITIAL",
        },
        "action": {
            "id": "ACTION-DNA10-01",
            "description": "APPLY_TEST_INTERVENTION",
        },
        "consequence": {
            "observed_change": "STATE_UPDATED",
        },
        "experience": {
            "candidate_learning": (
                "ACTION_CHANGED_ENVIRONMENT_STATE"
            ),
        },
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {
                "subject": "DNA-10_SELF_CHECK",
            },
            "provenance": [
                {
                    "sequence": 1,
                    "core_id": "CALLER",
                    "operation": "INPUT_CREATED",
                }
            ],
            "uncertainty": {
                "open_items": [
                    "MEMORY_CLASSIFICATION_UNDER_TEST"
                ],
            },
        },
    }


def _run_through(
    core54: Core54Like,
    context: Dict[str, Any],
    final_core_id: str,
) -> Dict[str, Any]:
    final_index = int(final_core_id.split("-")[1])
    result = deepcopy(context)
    for index in range(1, final_index + 1):
        core_id = f"DNA-{index:02d}"
        result = core54.get(core_id).activate(result)
    return result


def _derive_candidate_sha256(
    core54: Core54Like,
    base_probe: Dict[str, Any],
) -> str:
    through_dna08 = _run_through(
        core54,
        base_probe,
        "DNA-08",
    )
    event = through_dna08[
        "core54_outputs"
    ]["DNA-08"]["world_event"]
    if not isinstance(event, dict):
        raise AssertionError(
            "DNA-10_SELF_CHECK_DNA08_EVENT_MISSING"
        )

    candidate_content = {
        "source_core_id": "DNA-08",
        "source_event_id": event.get("event_id"),
        "interaction_sha256": event.get(
            "interaction_sha256"
        ),
        "experience": deepcopy(event.get("experience")),
    }
    return _sha256_json(candidate_content)


def _valid_verification(
    candidate_sha256: str,
    *,
    passed: bool,
) -> Dict[str, Any]:
    return {
        "learner_id": "LEARNER-A",
        "verifier_id": "VERIFIER-B",
        "verifier_independent": True,
        "independence_basis": [
            "SEPARATE_ROLE",
            "NO_SHARED_DECISION_AUTHORITY",
        ],
        "candidate_sha256": candidate_sha256,
        "method": "INDEPENDENT_REPLAY_AND_COMPARISON",
        "scope": "DNA-08_EXPERIENTIAL_EVENT",
        "evidence": [
            {
                "type": "REPLAY_RESULT",
                "result": (
                    "CONSISTENT"
                    if passed
                    else "INCONSISTENT"
                ),
            }
        ],
        "passed": passed,
    }


def self_check_dna10(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for required_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
        "DNA-09",
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna10_core = core54.get("DNA-10")
    assert_exact_canon(dna10_core)
    bind_dna10(core54)

    base_probe = _build_base_probe()
    candidate_sha256 = _derive_candidate_sha256(
        core54,
        base_probe,
    )

    verified_probe = deepcopy(base_probe)
    verified_probe["verification"] = _valid_verification(
        candidate_sha256,
        passed=True,
    )
    verified_snapshot = deepcopy(verified_probe)
    verified_result = _run_through(
        core54,
        verified_probe,
        "DNA-10",
    )

    assert verified_probe == verified_snapshot
    assert verified_result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 11)
    ]

    dna10 = verified_result["core54_outputs"]["DNA-10"]
    assert dna10["canonical_gene"] == CANON_DNA10
    assert dna10["memory_genome_contract"] == (
        MEMORY_GENOME_CONTRACT
    )
    assert dna10["persistent_memory_runtime_used"] is False
    assert dna10["status"] == "CANON_ALIGNED"

    expected_verified_counts = {
        "working": 1,
        "episodic": 1,
        "hypothesis": 0,
        "verified": 1,
        "rejected": 0,
        "strategy": 1,
    }
    assert dna10["segment_counts"] == (
        expected_verified_counts
    )

    genome = verified_result[
        "cognitive_state"
    ]["memory_genome"]
    assert genome["contract"] == MEMORY_GENOME_CONTRACT
    assert list(genome["segments"]) == MEMORY_CLASSES
    assert _segment_counts(genome) == (
        expected_verified_counts
    )
    _assert_segment_separation(genome)

    working = genome["segments"]["working"][0]
    assert working["source"] == "DNA-03"
    assert working["status"] == (
        "ACTIVE_STRUCTURED_STATE"
    )
    assert working["payload"]["content"] == {
        "subject": "DNA-10_SELF_CHECK",
    }

    episodic = genome["segments"]["episodic"][0]
    assert episodic["source"] == "DNA-08"
    assert episodic["status"] == (
        "EXPERIENCE_RECORDED"
    )
    assert episodic["payload"]["complete"] is True

    verified = genome["segments"]["verified"][0]
    assert verified["source"] == "DNA-09"
    assert verified["status"] == (
        "INDEPENDENTLY_VERIFIED_CANDIDATE"
    )
    assert verified["payload"]["evaluation"][
        "promotion_allowed"
    ] is True

    strategy = genome["segments"]["strategy"][0]
    assert strategy["source"] == "DNA-07"
    assert strategy["status"] == (
        "ACTIVE_STRATEGY_STATE"
    )
    assert strategy["payload"]["active_strategy"] == (
        "STRATEGY-B"
    )

    assert len(genome["routing_events"]) == 4
    assert {
        event["memory_class"]
        for event in genome["routing_events"]
    } == {
        "working",
        "episodic",
        "verified",
        "strategy",
    }

    # No verification keeps the candidate in hypothesis memory.
    hypothesis_probe = _build_base_probe()
    hypothesis_result = _run_through(
        core54,
        hypothesis_probe,
        "DNA-10",
    )
    hypothesis_genome = hypothesis_result[
        "cognitive_state"
    ]["memory_genome"]
    assert _segment_counts(hypothesis_genome) == {
        "working": 1,
        "episodic": 1,
        "hypothesis": 1,
        "verified": 0,
        "rejected": 0,
        "strategy": 1,
    }
    hypothesis = (
        hypothesis_genome["segments"]["hypothesis"][0]
    )
    assert hypothesis["status"] == (
        "UNVERIFIED_CANDIDATE"
    )

    # Explicit independent verifier failure routes the bound candidate to
    # rejected memory, not hypothesis or verified memory.
    rejected_probe = _build_base_probe()
    rejected_probe["verification"] = _valid_verification(
        candidate_sha256,
        passed=False,
    )
    rejected_result = _run_through(
        core54,
        rejected_probe,
        "DNA-10",
    )
    rejected_genome = rejected_result[
        "cognitive_state"
    ]["memory_genome"]
    assert _segment_counts(rejected_genome) == {
        "working": 1,
        "episodic": 1,
        "hypothesis": 0,
        "verified": 0,
        "rejected": 1,
        "strategy": 1,
    }
    rejected = rejected_genome["segments"]["rejected"][0]
    assert rejected["status"] == (
        "VERIFIER_REJECTED_CANDIDATE"
    )
    assert rejected["payload"]["evaluation"][
        "candidate_bound"
    ] is True
    assert rejected["payload"]["evaluation"][
        "verification_passed"
    ] is False

    # Exact class separation: candidate epistemic record appears in one and
    # only one of hypothesis/verified/rejected for each activation.
    for checked_genome in (
        genome,
        hypothesis_genome,
        rejected_genome,
    ):
        epistemic_count = sum(
            len(checked_genome["segments"][memory_class])
            for memory_class in (
                "hypothesis",
                "verified",
                "rejected",
            )
        )
        assert epistemic_count == 1
        _assert_segment_separation(checked_genome)

    # Idempotent activation must not duplicate records.
    repeated = dna10_core.activate(verified_result)
    assert repeated["cognitive_state"]["memory_genome"][
        "segments"
    ] == genome["segments"]
    assert repeated["cognitive_state"]["memory_genome"][
        "routing_events"
    ] == genome["routing_events"]

    # DNA-10 cannot bypass DNA-09.
    try:
        dna10_core.activate(
            {
                "trace": [],
                "core54_outputs": {},
                "cognitive_state": {
                    "schema": UNIFIED_STATE_SCHEMA,
                    "content": {},
                    "uncertainty": {},
                    "provenance": [],
                    "learning_world": {
                        "contract": {
                            "schema": LEARNING_WORLD_SCHEMA,
                        },
                        "events": [],
                    },
                },
            }
        )
    except RuntimeError as exc:
        assert str(exc) == (
            "DNA-09_INDEPENDENT_VERIFICATION_WALL_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-10_ACCEPTED_MISSING_VERIFICATION_WALL"
        )

    # Reject provisional root-marker behavior.
    assert "memory_route" not in verified_result
    assert "flags" not in verified_result
    assert "requests" not in verified_result
    assert "blocks" not in verified_result

    locks = {
        "auto_learning": bool(
            core54.auto_learning_enabled
        ),
        "model_calls": bool(
            core54.model_calls_enabled
        ),
        "external_execution": bool(
            core54.external_execution_enabled
        ),
        "canon_write": bool(
            core54.canon_write_enabled
        ),
    }
    assert not any(locks.values()), locks

    canon_after = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )
    if verify_canon_file:
        assert canon_before == canon_after

    return {
        "core_id": "DNA-10",
        "canon_mapping": "PASS",
        "memory_genome": "PASS",
        "memory_class_count": 6,
        "working_memory": "PASS",
        "episodic_memory": "PASS",
        "hypothesis_memory": "PASS",
        "verified_memory": "PASS",
        "rejected_memory": "PASS",
        "strategy_memory": "PASS",
        "class_separation": "PASS",
        "persistent_memory_runtime_used": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-11"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    required_gene_files = [
        GENES_ROOT / "SIGMA_DNA_01_PURPOSE_EXISTENCE.py",
        (
            GENES_ROOT
            / "SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE.py"
        ),
        GENES_ROOT / "SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE.py",
        GENES_ROOT / "SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS.py",
        GENES_ROOT / "SIGMA_DNA_05_ETHICAL_INTELLIGENCE.py",
        GENES_ROOT / "SIGMA_DNA_06_INTERLAYER_FEEDBACK.py",
        GENES_ROOT / "SIGMA_DNA_07_PERSISTENT_EXISTENCE.py",
        GENES_ROOT / "SIGMA_DNA_08_LEARNING_WORLD.py",
        (
            GENES_ROOT
            / "SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL.py"
        ),
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-10_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        from SIGMA_DNA_01_PURPOSE_EXISTENCE import (
            self_check_dna01,
        )
        from SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE import (
            self_check_dna02,
        )
        from SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE import (
            self_check_dna03,
        )
        from SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS import (
            self_check_dna04,
        )
        from SIGMA_DNA_05_ETHICAL_INTELLIGENCE import (
            self_check_dna05,
        )
        from SIGMA_DNA_06_INTERLAYER_FEEDBACK import (
            self_check_dna06,
        )
        from SIGMA_DNA_07_PERSISTENT_EXISTENCE import (
            self_check_dna07,
        )
        from SIGMA_DNA_08_LEARNING_WORLD import (
            self_check_dna08,
        )
        from SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL import (
            self_check_dna09,
        )
    except Exception as exc:
        print("DNA-10_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(
            core.state.behavior_bound
            for core in core54.cores
        ):
            raise RuntimeError("FRESH_FOUNDATION_REQUIRED")

        prior_checks = (
            ("DNA-01", self_check_dna01),
            ("DNA-02", self_check_dna02),
            ("DNA-03", self_check_dna03),
            ("DNA-04", self_check_dna04),
            ("DNA-05", self_check_dna05),
            ("DNA-06", self_check_dna06),
            ("DNA-07", self_check_dna07),
            ("DNA-08", self_check_dna08),
            ("DNA-09", self_check_dna09),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna10(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != [
            f"DNA-{index:02d}"
            for index in range(1, 11)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-10_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-10_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_10_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("MEMORY_GENOME:", report["memory_genome"])
    print(
        "MEMORY_CLASS_COUNT:",
        report["memory_class_count"],
    )
    print("WORKING_MEMORY:", report["working_memory"])
    print("EPISODIC_MEMORY:", report["episodic_memory"])
    print(
        "HYPOTHESIS_MEMORY:",
        report["hypothesis_memory"],
    )
    print("VERIFIED_MEMORY:", report["verified_memory"])
    print("REJECTED_MEMORY:", report["rejected_memory"])
    print("STRATEGY_MEMORY:", report["strategy_memory"])
    print(
        "CLASS_SEPARATION:",
        report["class_separation"],
    )
    print(
        "PERSISTENT_MEMORY_RUNTIME_USED:",
        report["persistent_memory_runtime_used"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 10/54")
    print("NEXT_AUTHORIZED: DNA-11")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
