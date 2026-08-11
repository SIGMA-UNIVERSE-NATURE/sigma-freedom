#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-14: PERSISTENCE ENGINE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_14_PERSISTENCE_ENGINE.py
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

CANON_DNA14: Dict[str, str] = {
    "id": "DNA-14",
    "name": "Persistence Engine",
    "purpose": (
        "Kiên trì phải tạo information gain; lặp lại cùng một cách "
        "không được gọi là học."
    ),
    "system": "evolution",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
PERSISTENT_EXISTENCE_SCHEMA = "SIGMA_PERSISTENT_EXISTENCE_V1"
ADAPTIVE_DEPTH_SCHEMA = "SIGMA_ADAPTIVE_COGNITIVE_DEPTH_V1"
PERSISTENCE_ENGINE_SCHEMA = "SIGMA_PERSISTENCE_ENGINE_V1"

ATTEMPT_FIELDS = [
    "strategy_before",
    "strategy_after",
    "information_before",
    "information_after",
]

PERSISTENCE_ENGINE_CONTRACT: Dict[str, Any] = {
    "schema": PERSISTENCE_ENGINE_SCHEMA,
    "information_gain_required": True,
    "same_path_repetition_counts_as_learning": False,
    "evaluation_basis": {
        "strategy_change": "CANONICAL_JSON_FINGERPRINT_COMPARISON",
        "information_gain": "NEW_UNIQUE_INFORMATION_ITEMS",
        "canon_status": "IMPLEMENTATION_ENCODING_NOT_CANON_FIELD",
    },
    "learning_claim_requires": [
        "INFORMATION_GAIN",
        "NON_REPEATED_STRATEGY",
    ],
    "strategy_change_required_when": [
        "NO_INFORMATION_GAIN",
        "SAME_PATH_REPEATED",
    ],
    "learning_runtime_started": False,
    "strategy_execution_started": False,
    "model_calls_started": False,
    "world_runtime_started": False,
    "f174_execution_started": False,
    "external_action_started": False,
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
    if actual != CANON_DNA14:
        raise RuntimeError(
            "DNA-14_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA14, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-14_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    persistent = state.get("persistent_existence")
    if not isinstance(persistent, dict):
        raise RuntimeError(
            "DNA-07_PERSISTENT_EXISTENCE_REQUIRED"
        )

    persistent_contract = persistent.get("contract")
    if not isinstance(persistent_contract, dict):
        raise RuntimeError(
            "DNA-07_PERSISTENT_EXISTENCE_CONTRACT_REQUIRED"
        )

    if persistent_contract.get("schema") != (
        PERSISTENT_EXISTENCE_SCHEMA
    ):
        raise ValueError(
            "DNA-14_PERSISTENT_EXISTENCE_SCHEMA_MISMATCH:"
            f"{persistent_contract.get('schema')!r}"
        )

    if not isinstance(persistent.get("recovery_events"), list):
        raise TypeError(
            "persistent_existence['recovery_events'] must be a list"
        )

    adaptive_depth = state.get("adaptive_cognitive_depth")
    if not isinstance(adaptive_depth, dict):
        raise RuntimeError(
            "DNA-13_ADAPTIVE_COGNITIVE_DEPTH_REQUIRED"
        )

    adaptive_contract = adaptive_depth.get("contract")
    if not isinstance(adaptive_contract, dict):
        raise RuntimeError(
            "DNA-13_ADAPTIVE_DEPTH_CONTRACT_REQUIRED"
        )

    if adaptive_contract.get("schema") != ADAPTIVE_DEPTH_SCHEMA:
        raise ValueError(
            "DNA-14_ADAPTIVE_DEPTH_SCHEMA_MISMATCH:"
            f"{adaptive_contract.get('schema')!r}"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-13_OUTPUT_REQUIRED")

    dna13_output = outputs.get("DNA-13")
    if not isinstance(dna13_output, dict):
        raise RuntimeError("DNA-13_OUTPUT_REQUIRED")

    return state, persistent, dna13_output


def _install_persistence_engine_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("persistence_engine")

    expected = {
        "contract": deepcopy(PERSISTENCE_ENGINE_CONTRACT),
        "evaluations": [],
    }

    if existing is None:
        state["persistence_engine"] = expected
        return state["persistence_engine"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['persistence_engine'] must be a dict"
        )

    if existing.get("contract") != PERSISTENCE_ENGINE_CONTRACT:
        raise ValueError(
            "DNA-14_PERSISTENCE_ENGINE_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("evaluations"), list):
        raise TypeError(
            "persistence_engine['evaluations'] must be a list"
        )

    return existing


def _parse_attempt(
    context: Dict[str, Any],
) -> Tuple[Optional[Dict[str, Any]], List[str]]:
    attempt = context.get("persistence_attempt")

    if attempt is None:
        return None, deepcopy(ATTEMPT_FIELDS)

    if not isinstance(attempt, dict):
        raise TypeError(
            "context['persistence_attempt'] must be a dict"
        )

    missing = [
        field
        for field in ATTEMPT_FIELDS
        if field not in attempt
    ]
    if missing:
        return None, missing

    for field in (
        "information_before",
        "information_after",
    ):
        if not isinstance(attempt[field], list):
            raise TypeError(
                f"persistence_attempt['{field}'] must be a list"
            )

    if attempt["strategy_before"] is None:
        raise ValueError(
            "DNA-14_STRATEGY_BEFORE_MUST_NOT_BE_NULL"
        )
    if attempt["strategy_after"] is None:
        raise ValueError(
            "DNA-14_STRATEGY_AFTER_MUST_NOT_BE_NULL"
        )

    return deepcopy(attempt), []


def _unique_information(
    values: List[Any],
) -> Tuple[List[str], Dict[str, Any]]:
    hashes: List[str] = []
    first_by_hash: Dict[str, Any] = {}

    for value in values:
        fingerprint = _sha256_json(value)
        if fingerprint not in first_by_hash:
            first_by_hash[fingerprint] = deepcopy(value)
            hashes.append(fingerprint)

    return hashes, first_by_hash


def _latest_strategy_transition(
    persistent: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    events = persistent["recovery_events"]
    if not events:
        return None

    latest = events[-1]
    if not isinstance(latest, dict):
        raise TypeError(
            "DNA-07 recovery event must be a dict"
        )

    transition = latest.get("strategy_change")
    if not isinstance(transition, dict):
        return None

    return deepcopy(transition)


def _status(
    *,
    information_gain_detected: bool,
    same_path_repeated: bool,
) -> str:
    if information_gain_detected and not same_path_repeated:
        return "INFORMATION_GAINING_PERSISTENCE"
    if information_gain_detected and same_path_repeated:
        return "INFORMATION_GAIN_WITH_REPEATED_PATH_NOT_LEARNING"
    if not information_gain_detected and not same_path_repeated:
        return "STRATEGY_CHANGED_WITHOUT_INFORMATION_GAIN"
    return "STAGNANT_REPETITION"


def _evaluate_attempt(
    attempt: Dict[str, Any],
    engine: Dict[str, Any],
    persistent: Dict[str, Any],
) -> Dict[str, Any]:
    strategy_before_sha256 = _sha256_json(
        attempt["strategy_before"]
    )
    strategy_after_sha256 = _sha256_json(
        attempt["strategy_after"]
    )
    strategy_changed = (
        strategy_before_sha256 != strategy_after_sha256
    )
    same_path_repeated = not strategy_changed

    before_hashes, _before_items = _unique_information(
        attempt["information_before"]
    )
    after_hashes, after_items = _unique_information(
        attempt["information_after"]
    )

    before_set = set(before_hashes)
    new_hashes = [
        fingerprint
        for fingerprint in after_hashes
        if fingerprint not in before_set
    ]
    new_information = [
        deepcopy(after_items[fingerprint])
        for fingerprint in new_hashes
    ]
    information_gain_detected = len(new_hashes) > 0

    latest_transition = _latest_strategy_transition(
        persistent
    )
    transition_bound: Optional[bool] = None
    if latest_transition is not None:
        transition_bound = (
            latest_transition.get("from")
            == attempt["strategy_before"]
            and latest_transition.get("to")
            == attempt["strategy_after"]
        )

    learning_claim_allowed = (
        information_gain_detected
        and not same_path_repeated
    )
    strategy_change_required = not learning_claim_allowed

    sequence = len(engine["evaluations"]) + 1
    evaluation = {
        "sequence": sequence,
        "evaluation_id": (
            f"DNA-14-PERSIST-{sequence:04d}"
        ),
        "attempt_id": attempt.get(
            "attempt_id",
            f"ATTEMPT-{sequence:04d}",
        ),
        "strategy_before": deepcopy(
            attempt["strategy_before"]
        ),
        "strategy_after": deepcopy(
            attempt["strategy_after"]
        ),
        "strategy_before_sha256": strategy_before_sha256,
        "strategy_after_sha256": strategy_after_sha256,
        "strategy_changed": strategy_changed,
        "same_path_repeated": same_path_repeated,
        "information_before_unique_count": len(before_hashes),
        "information_after_unique_count": len(after_hashes),
        "information_gain_count": len(new_hashes),
        "information_gain_detected": information_gain_detected,
        "new_information_sha256": deepcopy(new_hashes),
        "new_information": new_information,
        "dna07_strategy_transition": latest_transition,
        "dna07_transition_bound": transition_bound,
        "learning_claim_allowed": learning_claim_allowed,
        "strategy_change_required": strategy_change_required,
        "learning_runtime_used": False,
        "strategy_executed_by_dna14": False,
        "status": _status(
            information_gain_detected=(
                information_gain_detected
            ),
            same_path_repeated=same_path_repeated,
        ),
    }
    engine["evaluations"].append(evaluation)
    return evaluation


def dna14_persistence_engine(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Evaluate whether persistence creates information gain and whether a
    strategy path is genuinely changed rather than merely repeated.

    DNA-14 does not execute a strategy, start Learning/World Runtime,
    promote knowledge, invoke a model, execute F174, act externally, or
    modify Canon.
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
    trace.append("DNA-14")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, persistent, _dna13_output = (
        _validate_dependencies(context)
    )
    engine = _install_persistence_engine_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-14",
            "operation": (
                "PERSISTENCE_ENGINE_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "persistence_engine_schema": (
                PERSISTENCE_ENGINE_SCHEMA
            ),
            "learning_runtime_started": False,
            "strategy_execution_started": False,
        }
    )

    attempt, missing = _parse_attempt(context)
    evaluation: Optional[Dict[str, Any]] = None

    if attempt is not None:
        evaluation = _evaluate_attempt(
            attempt,
            engine,
            persistent,
        )
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-14",
                "operation": (
                    "PERSISTENCE_INFORMATION_GAIN_EVALUATED"
                ),
                "canonical_sha256": canonical_sha256,
                "evaluation_id": evaluation["evaluation_id"],
                "information_gain_detected": (
                    evaluation[
                        "information_gain_detected"
                    ]
                ),
                "same_path_repeated": evaluation[
                    "same_path_repeated"
                ],
                "learning_claim_allowed": evaluation[
                    "learning_claim_allowed"
                ],
                "strategy_change_required": evaluation[
                    "strategy_change_required"
                ],
                "learning_runtime_used": False,
            }
        )
    else:
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-14",
                "operation": (
                    "PERSISTENCE_ATTEMPT_INCOMPLETE"
                ),
                "canonical_sha256": canonical_sha256,
                "missing_fields": deepcopy(missing),
                "learning_runtime_used": False,
            }
        )

    outputs["DNA-14"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "persistence_engine_contract": deepcopy(
            PERSISTENCE_ENGINE_CONTRACT
        ),
        "attempt_complete": attempt is not None,
        "missing_fields": deepcopy(missing),
        "evaluation": deepcopy(evaluation),
        "learning_runtime_used": False,
        "strategy_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna14(core54: Core54Like) -> None:
    core = core54.get("DNA-14")
    assert_exact_canon(core)
    core54.bind(
        "DNA-14",
        dna14_persistence_engine,
    )


def _build_base_probe() -> Dict[str, Any]:
    return {
        "trace": [],
        "caller_data": {"preserve": True},
        "goal": {
            "id": "GOAL-DNA14",
            "statement": (
                "persist only through information-gaining change"
            ),
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
            "id": "WORLD-DNA14-SELF-CHECK",
            "state": "INITIAL",
        },
        "action": {
            "id": "ACTION-DNA14-01",
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
                "subject": "DNA-14_SELF_CHECK",
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
                    "PERSISTENCE_REQUIRES_INFORMATION_GAIN"
                ],
            },
        },
    }


def _run_through(
    core54: Core54Like,
    context: Dict[str, Any],
    final_index: int,
) -> Dict[str, Any]:
    result = deepcopy(context)
    for index in range(1, final_index + 1):
        result = core54.get(
            f"DNA-{index:02d}"
        ).activate(result)
    return result


def _derive_candidate_sha256(
    core54: Core54Like,
    base_probe: Dict[str, Any],
) -> str:
    through_dna08 = _run_through(
        core54,
        base_probe,
        8,
    )
    event = through_dna08[
        "core54_outputs"
    ]["DNA-08"]["world_event"]
    if not isinstance(event, dict):
        raise AssertionError(
            "DNA-14_SELF_CHECK_DNA08_EVENT_MISSING"
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


def _verification(
    candidate_sha256: str,
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
                "result": "CONSISTENT",
            }
        ],
        "passed": True,
    }


def _complete_probe(
    core54: Core54Like,
) -> Dict[str, Any]:
    base_probe = _build_base_probe()
    candidate_sha256 = _derive_candidate_sha256(
        core54,
        base_probe,
    )

    probe = deepcopy(base_probe)
    probe["verification"] = _verification(
        candidate_sha256
    )
    probe["knowledge_confidence"] = 0.88
    probe["knowledge_contradictions"] = []
    probe["knowledge_relations"] = [
        {
            "relation": "related_to",
            "target_id": "CONCEPT-PERSISTENCE-ENGINE",
            "target_type": "concept",
        }
    ]
    probe["tool_decision_context"] = {
        "internal_reasoning_sufficient": True,
        "tool_available": False,
        "candidate_tool": None,
        "requires_current_external_state": False,
        "requires_retrieval": False,
        "requires_exact_computation": False,
        "requires_observation_or_measurement": False,
        "requires_external_action": False,
    }
    probe["cognitive_depth_signals"] = {
        "uncertainty": 0.82,
        "risk": 0.61,
        "novelty": 0.74,
        "contradiction": 0.57,
        "expected_value": 0.91,
    }
    probe["persistence_attempt"] = {
        "attempt_id": "ATTEMPT-DNA14-01",
        "strategy_before": "STRATEGY-A",
        "strategy_after": "STRATEGY-B",
        "information_before": [
            {
                "id": "INFO-01",
                "claim": "FIRST_STRATEGY_FAILED",
            }
        ],
        "information_after": [
            {
                "id": "INFO-01",
                "claim": "FIRST_STRATEGY_FAILED",
            },
            {
                "id": "INFO-02",
                "claim": (
                    "CHANGED_STRATEGY_PRODUCED_NEW_OBSERVATION"
                ),
            },
        ],
    }
    return probe


def self_check_dna14(
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
        "DNA-10",
        "DNA-11",
        "DNA-12",
        "DNA-13",
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna14_core = core54.get("DNA-14")
    assert_exact_canon(dna14_core)
    bind_dna14(core54)

    probe = _complete_probe(core54)
    snapshot = deepcopy(probe)

    through_dna13 = _run_through(
        core54,
        probe,
        13,
    )
    result = dna14_core.activate(through_dna13)

    assert probe == snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 15)
    ]

    dna14 = result["core54_outputs"]["DNA-14"]
    assert dna14["canonical_gene"] == CANON_DNA14
    assert dna14["persistence_engine_contract"] == (
        PERSISTENCE_ENGINE_CONTRACT
    )
    assert dna14["attempt_complete"] is True
    assert dna14["missing_fields"] == []
    assert dna14["learning_runtime_used"] is False
    assert dna14["strategy_executed"] is False
    assert dna14["status"] == "CANON_ALIGNED"

    evaluation = dna14["evaluation"]
    assert evaluation is not None
    assert evaluation["sequence"] == 1
    assert evaluation["evaluation_id"] == (
        "DNA-14-PERSIST-0001"
    )
    assert evaluation["attempt_id"] == (
        "ATTEMPT-DNA14-01"
    )
    assert evaluation["strategy_before"] == "STRATEGY-A"
    assert evaluation["strategy_after"] == "STRATEGY-B"
    assert evaluation["strategy_changed"] is True
    assert evaluation["same_path_repeated"] is False
    assert evaluation[
        "information_before_unique_count"
    ] == 1
    assert evaluation[
        "information_after_unique_count"
    ] == 2
    assert evaluation["information_gain_count"] == 1
    assert evaluation[
        "information_gain_detected"
    ] is True
    assert evaluation["new_information"] == [
        {
            "id": "INFO-02",
            "claim": (
                "CHANGED_STRATEGY_PRODUCED_NEW_OBSERVATION"
            ),
        }
    ]
    assert evaluation["dna07_strategy_transition"] == {
        "from": "STRATEGY-A",
        "to": "STRATEGY-B",
        "status": "CHANGED",
    }
    assert evaluation["dna07_transition_bound"] is True
    assert evaluation["learning_claim_allowed"] is True
    assert evaluation["strategy_change_required"] is False
    assert evaluation["learning_runtime_used"] is False
    assert (
        evaluation["strategy_executed_by_dna14"]
        is False
    )
    assert evaluation["status"] == (
        "INFORMATION_GAINING_PERSISTENCE"
    )

    engine = result[
        "cognitive_state"
    ]["persistence_engine"]
    assert engine["contract"] == PERSISTENCE_ENGINE_CONTRACT
    assert engine["evaluations"] == [evaluation]

    provenance = result["cognitive_state"]["provenance"]
    assert provenance[-2]["operation"] == (
        "PERSISTENCE_ENGINE_CONTRACT_ESTABLISHED"
    )
    assert provenance[-2]["learning_runtime_started"] is False
    assert provenance[-2]["strategy_execution_started"] is False
    assert provenance[-1]["operation"] == (
        "PERSISTENCE_INFORMATION_GAIN_EVALUATED"
    )
    assert provenance[-1]["information_gain_detected"] is True
    assert provenance[-1]["same_path_repeated"] is False
    assert provenance[-1]["learning_claim_allowed"] is True
    assert provenance[-1]["strategy_change_required"] is False

    # Repeating the same strategy with no new information is stagnation,
    # not learning.
    stagnant_input = deepcopy(through_dna13)
    stagnant_input["persistence_attempt"] = {
        "attempt_id": "ATTEMPT-STAGNANT",
        "strategy_before": "STRATEGY-B",
        "strategy_after": "STRATEGY-B",
        "information_before": ["OBSERVATION-X"],
        "information_after": ["OBSERVATION-X"],
    }
    stagnant = dna14_core.activate(stagnant_input)
    stagnant_eval = stagnant[
        "core54_outputs"
    ]["DNA-14"]["evaluation"]
    assert stagnant_eval["information_gain_detected"] is False
    assert stagnant_eval["same_path_repeated"] is True
    assert stagnant_eval["learning_claim_allowed"] is False
    assert stagnant_eval["strategy_change_required"] is True
    assert stagnant_eval["status"] == "STAGNANT_REPETITION"

    # New information on an unchanged path still cannot be labelled
    # learning under the exact second Canon clause.
    same_path_gain_input = deepcopy(through_dna13)
    same_path_gain_input["persistence_attempt"] = {
        "attempt_id": "ATTEMPT-SAME-PATH-GAIN",
        "strategy_before": "STRATEGY-B",
        "strategy_after": "STRATEGY-B",
        "information_before": ["OBSERVATION-X"],
        "information_after": [
            "OBSERVATION-X",
            "OBSERVATION-Y",
        ],
    }
    same_path_gain = dna14_core.activate(
        same_path_gain_input
    )
    same_path_gain_eval = same_path_gain[
        "core54_outputs"
    ]["DNA-14"]["evaluation"]
    assert same_path_gain_eval[
        "information_gain_detected"
    ] is True
    assert same_path_gain_eval[
        "same_path_repeated"
    ] is True
    assert same_path_gain_eval[
        "learning_claim_allowed"
    ] is False
    assert same_path_gain_eval[
        "strategy_change_required"
    ] is True
    assert same_path_gain_eval["status"] == (
        "INFORMATION_GAIN_WITH_REPEATED_PATH_NOT_LEARNING"
    )

    # Changing strategy without information gain does not satisfy
    # persistence.
    no_gain_input = deepcopy(through_dna13)
    no_gain_input["persistence_attempt"] = {
        "attempt_id": "ATTEMPT-CHANGED-NO-GAIN",
        "strategy_before": "STRATEGY-B",
        "strategy_after": "STRATEGY-C",
        "information_before": ["OBSERVATION-X"],
        "information_after": ["OBSERVATION-X"],
    }
    no_gain = dna14_core.activate(no_gain_input)
    no_gain_eval = no_gain[
        "core54_outputs"
    ]["DNA-14"]["evaluation"]
    assert no_gain_eval["strategy_changed"] is True
    assert no_gain_eval["information_gain_detected"] is False
    assert no_gain_eval["learning_claim_allowed"] is False
    assert no_gain_eval["strategy_change_required"] is True
    assert no_gain_eval["status"] == (
        "STRATEGY_CHANGED_WITHOUT_INFORMATION_GAIN"
    )

    # Incomplete evidence remains explicit; DNA-14 invents nothing.
    incomplete_input = deepcopy(through_dna13)
    incomplete_input["persistence_attempt"] = {
        "strategy_before": "STRATEGY-A",
        "strategy_after": "STRATEGY-B",
        "information_before": [],
    }
    incomplete = dna14_core.activate(incomplete_input)
    incomplete_output = incomplete[
        "core54_outputs"
    ]["DNA-14"]
    assert incomplete_output["attempt_complete"] is False
    assert incomplete_output["missing_fields"] == [
        "information_after"
    ]
    assert incomplete_output["evaluation"] is None
    assert incomplete[
        "cognitive_state"
    ]["provenance"][-1]["operation"] == (
        "PERSISTENCE_ATTEMPT_INCOMPLETE"
    )

    # Information collections must be explicit lists.
    invalid_input = deepcopy(through_dna13)
    invalid_input["persistence_attempt"] = {
        "strategy_before": "STRATEGY-A",
        "strategy_after": "STRATEGY-B",
        "information_before": {"not": "a list"},
        "information_after": [],
    }
    try:
        dna14_core.activate(invalid_input)
    except TypeError as exc:
        assert "information_before" in str(exc)
    else:
        raise AssertionError(
            "DNA-14_ACCEPTED_NON_LIST_INFORMATION"
        )

    # Reject the old provisional request marker as the official contract.
    assert "requests" not in result
    assert "flags" not in result
    assert "blocks" not in result
    assert "same_path_repeated" not in result
    assert "information_gain" not in result

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
        "core_id": "DNA-14",
        "canon_mapping": "PASS",
        "information_gain": "PASS",
        "same_path_not_learning": "PASS",
        "strategy_change_signal": "PASS",
        "dna07_transition_binding": "PASS",
        "learning_runtime_used": False,
        "strategy_executed": False,
        "f174_executed": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-15"
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
        GENES_ROOT / "SIGMA_DNA_10_MEMORY_GENOME.py",
        GENES_ROOT / "SIGMA_DNA_11_KNOWLEDGE_GRAPH.py",
        GENES_ROOT / "SIGMA_DNA_12_TOOL_INTELLIGENCE.py",
        GENES_ROOT / "SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH.py",
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-14_FAIL: REQUIRED_PATH_NOT_FOUND")
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
        from SIGMA_DNA_10_MEMORY_GENOME import (
            self_check_dna10,
        )
        from SIGMA_DNA_11_KNOWLEDGE_GRAPH import (
            self_check_dna11,
        )
        from SIGMA_DNA_12_TOOL_INTELLIGENCE import (
            self_check_dna12,
        )
        from SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH import (
            self_check_dna13,
        )
    except Exception as exc:
        print("DNA-14_FAIL: IMPORT_ERROR")
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
            ("DNA-10", self_check_dna10),
            ("DNA-11", self_check_dna11),
            ("DNA-12", self_check_dna12),
            ("DNA-13", self_check_dna13),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna14(
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
            for index in range(1, 15)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-14_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-14_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_14_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("INFORMATION_GAIN:", report["information_gain"])
    print(
        "SAME_PATH_NOT_LEARNING:",
        report["same_path_not_learning"],
    )
    print(
        "STRATEGY_CHANGE_SIGNAL:",
        report["strategy_change_signal"],
    )
    print(
        "DNA07_TRANSITION_BINDING:",
        report["dna07_transition_binding"],
    )
    print(
        "LEARNING_RUNTIME_USED:",
        report["learning_runtime_used"],
    )
    print(
        "STRATEGY_EXECUTED:",
        report["strategy_executed"],
    )
    print("F174_EXECUTED:", report["f174_executed"])
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 14/54")
    print("NEXT_AUTHORIZED: DNA-15")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
