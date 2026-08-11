#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-17: TWO LEVELS OF LEARNING
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING.py
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

CANON_DNA17: Dict[str, str] = {
    "id": "DNA-17",
    "name": "Two Levels of Learning",
    "purpose": (
        "Tách cognitive learning (memory/strategy) khỏi neural learning "
        "(thay đổi persistent capability)."
    ),
    "system": "learning",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
VERIFICATION_WALL_SCHEMA = (
    "SIGMA_INDEPENDENT_VERIFICATION_WALL_V1"
)
MEMORY_GENOME_SCHEMA = "SIGMA_MEMORY_GENOME_V1"
PERSISTENCE_ENGINE_SCHEMA = "SIGMA_PERSISTENCE_ENGINE_V1"
EXPERIENCE_LEARNING_SCHEMA = (
    "SIGMA_EXPERIENCE_DRIVEN_LEARNING_V1"
)
TWO_LEVELS_SCHEMA = "SIGMA_TWO_LEVELS_OF_LEARNING_V1"

NEURAL_CHANGE_FIELDS = [
    "capability_id",
    "before",
    "after",
    "persistence_evidence",
    "verification",
]

VERIFICATION_FIELDS = [
    "learner_id",
    "verifier_id",
    "verifier_independent",
    "independence_basis",
    "candidate_sha256",
    "method",
    "scope",
    "evidence",
    "passed",
]

TWO_LEVELS_OF_LEARNING_CONTRACT: Dict[str, Any] = {
    "schema": TWO_LEVELS_SCHEMA,
    "levels": {
        "cognitive": {
            "definition": "MEMORY_OR_STRATEGY_CHANGE",
            "persistent_capability_change_required": False,
        },
        "neural": {
            "definition": "PERSISTENT_CAPABILITY_CHANGE",
            "persistent_capability_change_required": True,
        },
    },
    "level_separation_required": True,
    "cognitive_learning_is_not_neural_learning": True,
    "memory_or_strategy_change_does_not_prove_neural_change": True,
    "neural_change_requires_persistence_evidence": True,
    "neural_change_requires_independent_verification": True,
    "simultaneous_levels_remain_separately_reported": True,
    "classification_values": [
        "NONE",
        "COGNITIVE",
        "NEURAL",
        "COGNITIVE_AND_NEURAL",
    ],
    "learning_runtime_started": False,
    "neural_learning_started": False,
    "persistent_capability_modified_by_dna17": False,
    "model_or_adapter_promotion_executed": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA09_EVIDENCE_BINDING"
    ),
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
    if actual != CANON_DNA17:
        raise RuntimeError(
            "DNA-17_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA17, "actual": actual},
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
    Dict[str, Any],
]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-17_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
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
            "DNA-17_VERIFICATION_WALL_SCHEMA_MISMATCH:"
            f"{verification_contract.get('schema')!r}"
        )

    memory_genome = state.get("memory_genome")
    if not isinstance(memory_genome, dict):
        raise RuntimeError("DNA-10_MEMORY_GENOME_REQUIRED")

    memory_contract = memory_genome.get("contract")
    if not isinstance(memory_contract, dict):
        raise RuntimeError(
            "DNA-10_MEMORY_GENOME_CONTRACT_REQUIRED"
        )

    if memory_contract.get("schema") != MEMORY_GENOME_SCHEMA:
        raise ValueError(
            "DNA-17_MEMORY_GENOME_SCHEMA_MISMATCH:"
            f"{memory_contract.get('schema')!r}"
        )

    segments = memory_genome.get("segments")
    if not isinstance(segments, dict):
        raise TypeError(
            "memory_genome['segments'] must be a dict"
        )

    persistence_engine = state.get("persistence_engine")
    if not isinstance(persistence_engine, dict):
        raise RuntimeError(
            "DNA-14_PERSISTENCE_ENGINE_REQUIRED"
        )

    persistence_contract = persistence_engine.get("contract")
    if not isinstance(persistence_contract, dict):
        raise RuntimeError(
            "DNA-14_PERSISTENCE_ENGINE_CONTRACT_REQUIRED"
        )

    if persistence_contract.get("schema") != (
        PERSISTENCE_ENGINE_SCHEMA
    ):
        raise ValueError(
            "DNA-17_PERSISTENCE_ENGINE_SCHEMA_MISMATCH:"
            f"{persistence_contract.get('schema')!r}"
        )

    if not isinstance(
        persistence_engine.get("evaluations"),
        list,
    ):
        raise TypeError(
            "persistence_engine['evaluations'] must be a list"
        )

    experience_learning = state.get(
        "experience_driven_learning"
    )
    if not isinstance(experience_learning, dict):
        raise RuntimeError(
            "DNA-16_EXPERIENCE_DRIVEN_LEARNING_REQUIRED"
        )

    experience_contract = experience_learning.get("contract")
    if not isinstance(experience_contract, dict):
        raise RuntimeError(
            "DNA-16_EXPERIENCE_LEARNING_CONTRACT_REQUIRED"
        )

    if experience_contract.get("schema") != (
        EXPERIENCE_LEARNING_SCHEMA
    ):
        raise ValueError(
            "DNA-17_EXPERIENCE_LEARNING_SCHEMA_MISMATCH:"
            f"{experience_contract.get('schema')!r}"
        )

    if not isinstance(
        experience_learning.get("retained_experiences"),
        list,
    ):
        raise TypeError(
            "experience_driven_learning['retained_experiences'] "
            "must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-16_OUTPUT_REQUIRED")

    dna16_output = outputs.get("DNA-16")
    if not isinstance(dna16_output, dict):
        raise RuntimeError("DNA-16_OUTPUT_REQUIRED")

    return (
        state,
        verification_wall,
        memory_genome,
        persistence_engine,
        experience_learning,
    )


def _install_two_levels_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("two_levels_of_learning")

    expected = {
        "contract": deepcopy(
            TWO_LEVELS_OF_LEARNING_CONTRACT
        ),
        "classifications": [],
        "neural_change_records": [],
    }

    if existing is None:
        state["two_levels_of_learning"] = expected
        return state["two_levels_of_learning"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['two_levels_of_learning'] "
            "must be a dict"
        )

    if existing.get("contract") != (
        TWO_LEVELS_OF_LEARNING_CONTRACT
    ):
        raise ValueError(
            "DNA-17_TWO_LEVELS_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("classifications"), list):
        raise TypeError(
            "two_levels_of_learning['classifications'] "
            "must be a list"
        )

    if not isinstance(
        existing.get("neural_change_records"),
        list,
    ):
        raise TypeError(
            "two_levels_of_learning['neural_change_records'] "
            "must be a list"
        )

    return existing


def _collect_cognitive_evidence(
    memory_genome: Dict[str, Any],
    persistence_engine: Dict[str, Any],
    experience_learning: Dict[str, Any],
) -> Dict[str, Any]:
    memory_records: List[Dict[str, Any]] = []

    for memory_class, records in (
        memory_genome["segments"].items()
    ):
        if not isinstance(records, list):
            raise TypeError(
                "memory_genome segment must be a list:"
                f"{memory_class}"
            )

        for record in records:
            if not isinstance(record, dict):
                raise TypeError(
                    "memory_genome record must be a dict"
                )
            memory_records.append(
                {
                    "memory_class": memory_class,
                    "record_id": record.get("record_id"),
                    "record_sha256": record.get(
                        "record_sha256"
                    ),
                }
            )

    qualifying_strategy_evaluations: List[
        Dict[str, Any]
    ] = []
    for evaluation in persistence_engine["evaluations"]:
        if not isinstance(evaluation, dict):
            raise TypeError(
                "persistence_engine evaluation must be a dict"
            )
        if evaluation.get("learning_claim_allowed") is True:
            qualifying_strategy_evaluations.append(
                {
                    "evaluation_id": evaluation.get(
                        "evaluation_id"
                    ),
                    "strategy_changed": evaluation.get(
                        "strategy_changed"
                    ),
                    "information_gain_detected": (
                        evaluation.get(
                            "information_gain_detected"
                        )
                    ),
                }
            )

    retained_experience_ids = [
        record.get("retention_id")
        for record in (
            experience_learning["retained_experiences"]
        )
        if isinstance(record, dict)
        and record.get("retained") is True
    ]

    memory_change_detected = len(memory_records) > 0
    strategy_change_detected = (
        len(qualifying_strategy_evaluations) > 0
    )
    detected = (
        memory_change_detected
        or strategy_change_detected
    )

    return {
        "detected": detected,
        "definition": "MEMORY_OR_STRATEGY_CHANGE",
        "memory_change_detected": (
            memory_change_detected
        ),
        "memory_record_count": len(memory_records),
        "memory_records": memory_records,
        "strategy_change_detected": (
            strategy_change_detected
        ),
        "qualifying_strategy_evaluation_count": len(
            qualifying_strategy_evaluations
        ),
        "qualifying_strategy_evaluations": (
            qualifying_strategy_evaluations
        ),
        "supporting_retained_experience_ids": (
            retained_experience_ids
        ),
        "persistent_capability_change_inferred": False,
        "neural_learning_claimed": False,
        "status": (
            "COGNITIVE_LEARNING_EVIDENCED"
            if detected
            else "NO_COGNITIVE_LEARNING_EVIDENCE"
        ),
    }


def _non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _non_empty_list(value: Any) -> bool:
    return isinstance(value, list) and len(value) > 0


def _validate_verification_types(
    verification: Dict[str, Any],
) -> None:
    for field in (
        "verifier_independent",
        "passed",
    ):
        if field in verification and not isinstance(
            verification[field],
            bool,
        ):
            raise TypeError(
                f"persistent capability verification['{field}'] "
                "must be a bool"
            )

    for field in (
        "learner_id",
        "verifier_id",
        "candidate_sha256",
        "method",
        "scope",
    ):
        if field in verification and not isinstance(
            verification[field],
            str,
        ):
            raise TypeError(
                f"persistent capability verification['{field}'] "
                "must be a string"
            )

    for field in (
        "independence_basis",
        "evidence",
    ):
        if field in verification and not isinstance(
            verification[field],
            list,
        ):
            raise TypeError(
                f"persistent capability verification['{field}'] "
                "must be a list"
            )


def _evaluate_verification(
    candidate_sha256: str,
    verification: Any,
) -> List[str]:
    reasons: List[str] = []

    if not isinstance(verification, dict):
        return ["VERIFICATION_RECORD_REQUIRED"]

    _validate_verification_types(verification)

    missing = [
        field
        for field in VERIFICATION_FIELDS
        if field not in verification
    ]
    if missing:
        reasons.append("VERIFICATION_FIELDS_MISSING")

    learner_id = verification.get("learner_id")
    verifier_id = verification.get("verifier_id")
    if not (
        _non_empty_text(learner_id)
        and _non_empty_text(verifier_id)
        and learner_id != verifier_id
    ):
        reasons.append(
            "LEARNER_VERIFIER_NOT_SEPARATED"
        )

    if verification.get("verifier_independent") is not True:
        reasons.append(
            "INDEPENDENT_VERIFIER_REQUIRED"
        )

    if not _non_empty_list(
        verification.get("independence_basis")
    ):
        reasons.append(
            "INDEPENDENCE_BASIS_REQUIRED"
        )

    if verification.get("candidate_sha256") != (
        candidate_sha256
    ):
        reasons.append(
            "VERIFICATION_NOT_BOUND_TO_CAPABILITY_CHANGE"
        )

    if not _non_empty_text(verification.get("method")):
        reasons.append(
            "VERIFICATION_METHOD_REQUIRED"
        )

    if not _non_empty_text(verification.get("scope")):
        reasons.append(
            "VERIFICATION_SCOPE_REQUIRED"
        )

    if not _non_empty_list(verification.get("evidence")):
        reasons.append(
            "VERIFICATION_EVIDENCE_REQUIRED"
        )

    if verification.get("passed") is not True:
        reasons.append("VERIFIER_PASS_REQUIRED")

    return list(dict.fromkeys(reasons))


def _evaluate_neural_change(
    context: Dict[str, Any],
) -> Dict[str, Any]:
    supplied = context.get("persistent_capability_change")

    if supplied is None:
        return {
            "supplied": False,
            "complete": False,
            "established": False,
            "candidate": None,
            "candidate_sha256": None,
            "missing_fields": deepcopy(
                NEURAL_CHANGE_FIELDS
            ),
            "rejection_reasons": [],
            "status": (
                "NO_PERSISTENT_CAPABILITY_CHANGE_SUPPLIED"
            ),
        }

    if not isinstance(supplied, dict):
        raise TypeError(
            "context['persistent_capability_change'] "
            "must be a dict"
        )

    missing = [
        field
        for field in NEURAL_CHANGE_FIELDS
        if field not in supplied
        or supplied[field] is None
    ]
    if missing:
        return {
            "supplied": True,
            "complete": False,
            "established": False,
            "candidate": None,
            "candidate_sha256": None,
            "missing_fields": missing,
            "rejection_reasons": [
                "PERSISTENT_CAPABILITY_CHANGE_FIELDS_MISSING"
            ],
            "status": (
                "PERSISTENT_CAPABILITY_CHANGE_NOT_ESTABLISHED"
            ),
        }

    capability_id = supplied["capability_id"]
    if not _non_empty_text(capability_id):
        raise ValueError(
            "DNA-17_CAPABILITY_ID_MUST_BE_NON_EMPTY"
        )

    persistence_evidence = supplied[
        "persistence_evidence"
    ]
    if not isinstance(persistence_evidence, list):
        raise TypeError(
            "persistent_capability_change"
            "['persistence_evidence'] must be a list"
        )

    candidate = {
        "capability_id": capability_id,
        "before": deepcopy(supplied["before"]),
        "after": deepcopy(supplied["after"]),
        "persistence_evidence": deepcopy(
            persistence_evidence
        ),
    }
    candidate_sha256 = _sha256_json(candidate)

    reasons: List[str] = []

    if _sha256_json(candidate["before"]) == _sha256_json(
        candidate["after"]
    ):
        reasons.append(
            "PERSISTENT_CAPABILITY_BEFORE_AFTER_UNCHANGED"
        )

    if not _non_empty_list(persistence_evidence):
        reasons.append(
            "PERSISTENCE_EVIDENCE_REQUIRED"
        )

    reasons.extend(
        _evaluate_verification(
            candidate_sha256,
            supplied["verification"],
        )
    )
    reasons = list(dict.fromkeys(reasons))
    established = len(reasons) == 0

    return {
        "supplied": True,
        "complete": True,
        "established": established,
        "candidate": candidate,
        "candidate_sha256": candidate_sha256,
        "missing_fields": [],
        "rejection_reasons": reasons,
        "status": (
            "PERSISTENT_CAPABILITY_CHANGE_EVIDENCED"
            if established
            else (
                "PERSISTENT_CAPABILITY_CHANGE_NOT_ESTABLISHED"
            )
        ),
    }


def _retain_neural_change_if_established(
    two_levels_state: Dict[str, Any],
    neural_evaluation: Dict[str, Any],
) -> Tuple[Optional[Dict[str, Any]], bool]:
    if neural_evaluation["established"] is not True:
        return None, False

    candidate_sha256 = neural_evaluation[
        "candidate_sha256"
    ]
    records = two_levels_state["neural_change_records"]

    for existing in records:
        if existing.get("candidate_sha256") == (
            candidate_sha256
        ):
            return existing, False

    sequence = len(records) + 1
    candidate = neural_evaluation["candidate"]
    record = {
        "record_id": (
            f"DNA-17-NEURAL-{sequence:04d}"
        ),
        "sequence": sequence,
        "capability_id": candidate["capability_id"],
        "before_sha256": _sha256_json(
            candidate["before"]
        ),
        "after_sha256": _sha256_json(
            candidate["after"]
        ),
        "persistence_evidence": deepcopy(
            candidate["persistence_evidence"]
        ),
        "candidate_sha256": candidate_sha256,
        "persistent_capability_change": True,
        "independently_verified": True,
        "capability_improvement_claimed": False,
        "neural_learning_executed_by_dna17": False,
        "persistent_capability_modified_by_dna17": False,
        "model_or_adapter_promoted": False,
        "status": (
            "NEURAL_LEVEL_EVIDENCE_RECORDED"
        ),
    }
    records.append(record)
    return record, True


def _learning_level(
    cognitive_detected: bool,
    neural_established: bool,
) -> str:
    if cognitive_detected and neural_established:
        return "COGNITIVE_AND_NEURAL"
    if cognitive_detected:
        return "COGNITIVE"
    if neural_established:
        return "NEURAL"
    return "NONE"


def dna17_two_levels_of_learning(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Keep cognitive learning (memory/strategy) separate from neural learning
    (evidenced persistent capability change).

    DNA-17 classifies supplied/current evidence only. It does not perform
    neural adaptation, start Learning Runtime, change persistent capability,
    promote a model/adapter, invoke a model, execute F174, act externally,
    or modify Canon.
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
    trace.append("DNA-17")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    (
        state,
        _verification_wall,
        memory_genome,
        persistence_engine,
        experience_learning,
    ) = _validate_dependencies(context)

    two_levels_state = _install_two_levels_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-17",
            "operation": (
                "TWO_LEVELS_OF_LEARNING_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "two_levels_schema": TWO_LEVELS_SCHEMA,
            "level_separation_required": True,
            "neural_learning_started": False,
        }
    )

    cognitive_evidence = _collect_cognitive_evidence(
        memory_genome,
        persistence_engine,
        experience_learning,
    )
    neural_evaluation = _evaluate_neural_change(context)
    neural_record, neural_record_new = (
        _retain_neural_change_if_established(
            two_levels_state,
            neural_evaluation,
        )
    )

    level = _learning_level(
        cognitive_evidence["detected"],
        neural_evaluation["established"],
    )

    classification_sequence = len(
        two_levels_state["classifications"]
    ) + 1
    classification = {
        "sequence": classification_sequence,
        "classification_id": (
            f"DNA-17-CLASS-{classification_sequence:04d}"
        ),
        "learning_level": level,
        "cognitive_learning_detected": (
            cognitive_evidence["detected"]
        ),
        "neural_learning_established": (
            neural_evaluation["established"]
        ),
        "levels_separately_reported": True,
        "memory_record_count": (
            cognitive_evidence["memory_record_count"]
        ),
        "qualifying_strategy_evaluation_count": (
            cognitive_evidence[
                "qualifying_strategy_evaluation_count"
            ]
        ),
        "neural_candidate_sha256": (
            neural_evaluation["candidate_sha256"]
        ),
        "neural_record_id": (
            neural_record["record_id"]
            if neural_record is not None
            else None
        ),
        "neural_record_new": neural_record_new,
        "neural_learning_executed": False,
        "persistent_capability_modified": False,
        "model_or_adapter_promoted": False,
        "status": "LEARNING_LEVELS_CLASSIFIED",
    }
    two_levels_state["classifications"].append(
        classification
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-17",
            "operation": "LEARNING_LEVELS_CLASSIFIED",
            "canonical_sha256": canonical_sha256,
            "classification_id": (
                classification["classification_id"]
            ),
            "learning_level": level,
            "cognitive_learning_detected": (
                classification[
                    "cognitive_learning_detected"
                ]
            ),
            "neural_learning_established": (
                classification[
                    "neural_learning_established"
                ]
            ),
            "levels_separately_reported": True,
            "neural_learning_executed": False,
            "persistent_capability_modified": False,
        }
    )

    outputs["DNA-17"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "two_levels_contract": deepcopy(
            TWO_LEVELS_OF_LEARNING_CONTRACT
        ),
        "learning_level": level,
        "cognitive_learning": deepcopy(
            cognitive_evidence
        ),
        "neural_learning": deepcopy(
            neural_evaluation
        ),
        "neural_record": deepcopy(neural_record),
        "neural_record_new": neural_record_new,
        "classification": deepcopy(classification),
        "neural_change_record_count": len(
            two_levels_state["neural_change_records"]
        ),
        "learning_runtime_used": False,
        "neural_learning_executed": False,
        "persistent_capability_modified": False,
        "model_or_adapter_promoted": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna17(core54: Core54Like) -> None:
    core = core54.get("DNA-17")
    assert_exact_canon(core)
    core54.bind(
        "DNA-17",
        dna17_two_levels_of_learning,
    )


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


def _valid_persistent_capability_change() -> Dict[str, Any]:
    candidate = {
        "capability_id": "CAPABILITY-DNA17-01",
        "before": {
            "version": "CAP-V1",
            "persistent_success_rate": 0.40,
        },
        "after": {
            "version": "CAP-V2",
            "persistent_success_rate": 0.75,
        },
        "persistence_evidence": [
            {
                "timepoint": "T+1",
                "result": "CHANGE_RETAINED",
            },
            {
                "timepoint": "T+2",
                "result": "CHANGE_RETAINED",
            },
        ],
    }
    candidate_sha256 = _sha256_json(candidate)

    return {
        **deepcopy(candidate),
        "verification": {
            "learner_id": "LEARNER-DNA17",
            "verifier_id": (
                "VERIFIER-DNA17-INDEPENDENT"
            ),
            "verifier_independent": True,
            "independence_basis": [
                "SEPARATE_ROLE",
                "NO_SHARED_DECISION_AUTHORITY",
            ],
            "candidate_sha256": candidate_sha256,
            "method": (
                "INDEPENDENT_PERSISTENCE_REPLAY_AND_"
                "CAPABILITY_COMPARISON"
            ),
            "scope": (
                "DNA-17_PERSISTENT_CAPABILITY_CHANGE"
            ),
            "evidence": [
                {
                    "type": "PERSISTENCE_REPLAY",
                    "result": "SUPPORTED",
                },
                {
                    "type": "BEFORE_AFTER_COMPARISON",
                    "result": "CHANGE_CONFIRMED",
                },
            ],
            "passed": True,
        },
    }


def _clear_cognitive_evidence(
    context: Dict[str, Any],
) -> Dict[str, Any]:
    cleared = deepcopy(context)
    state = cleared["cognitive_state"]

    for records in (
        state["memory_genome"]["segments"].values()
    ):
        records.clear()

    state["persistence_engine"]["evaluations"].clear()
    state["experience_driven_learning"][
        "retained_experiences"
    ].clear()

    return cleared


def self_check_dna17(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 17):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna17_core = core54.get("DNA-17")
    assert_exact_canon(dna17_core)
    bind_dna17(core54)

    from SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING import (
        _complete_probe as dna16_complete_probe,
    )

    probe = dna16_complete_probe(core54)
    snapshot = deepcopy(probe)
    through_dna16 = _run_through(
        core54,
        probe,
        16,
    )

    pre_memory_genome = deepcopy(
        through_dna16["cognitive_state"][
            "memory_genome"
        ]
    )
    pre_persistence_engine = deepcopy(
        through_dna16["cognitive_state"][
            "persistence_engine"
        ]
    )
    pre_experience_learning = deepcopy(
        through_dna16["cognitive_state"][
            "experience_driven_learning"
        ]
    )
    pre_verification_wall = deepcopy(
        through_dna16["cognitive_state"][
            "independent_verification_wall"
        ]
    )
    pre_provenance_count = len(
        through_dna16["cognitive_state"][
            "provenance"
        ]
    )

    combined_input = deepcopy(through_dna16)
    combined_input["persistent_capability_change"] = (
        _valid_persistent_capability_change()
    )
    result = dna17_core.activate(combined_input)

    assert probe == snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 18)
    ]

    dna17 = result["core54_outputs"]["DNA-17"]
    assert dna17["canonical_gene"] == CANON_DNA17
    assert dna17["two_levels_contract"] == (
        TWO_LEVELS_OF_LEARNING_CONTRACT
    )
    assert dna17["learning_level"] == (
        "COGNITIVE_AND_NEURAL"
    )
    assert (
        dna17["cognitive_learning"]["detected"]
        is True
    )
    assert (
        dna17["cognitive_learning"][
            "memory_change_detected"
        ]
        is True
    )
    assert (
        dna17["cognitive_learning"][
            "memory_record_count"
        ]
        >= 1
    )
    assert (
        dna17["cognitive_learning"][
            "strategy_change_detected"
        ]
        is True
    )
    assert (
        dna17["cognitive_learning"][
            "qualifying_strategy_evaluation_count"
        ]
        >= 1
    )
    assert (
        dna17["cognitive_learning"][
            "persistent_capability_change_inferred"
        ]
        is False
    )
    assert (
        dna17["neural_learning"]["established"]
        is True
    )
    assert (
        dna17["neural_learning"]["status"]
        == "PERSISTENT_CAPABILITY_CHANGE_EVIDENCED"
    )
    assert dna17["neural_record_new"] is True
    assert dna17["neural_change_record_count"] == 1
    assert dna17["learning_runtime_used"] is False
    assert dna17["neural_learning_executed"] is False
    assert dna17["persistent_capability_modified"] is False
    assert dna17["model_or_adapter_promoted"] is False
    assert dna17["status"] == "CANON_ALIGNED"

    neural_record = dna17["neural_record"]
    assert neural_record["record_id"] == (
        "DNA-17-NEURAL-0001"
    )
    assert (
        neural_record["persistent_capability_change"]
        is True
    )
    assert neural_record["independently_verified"] is True
    assert (
        neural_record[
            "capability_improvement_claimed"
        ]
        is False
    )
    assert (
        neural_record[
            "neural_learning_executed_by_dna17"
        ]
        is False
    )
    assert (
        neural_record[
            "persistent_capability_modified_by_dna17"
        ]
        is False
    )
    assert (
        neural_record["model_or_adapter_promoted"]
        is False
    )

    classification = dna17["classification"]
    assert classification["learning_level"] == (
        "COGNITIVE_AND_NEURAL"
    )
    assert (
        classification[
            "cognitive_learning_detected"
        ]
        is True
    )
    assert (
        classification[
            "neural_learning_established"
        ]
        is True
    )
    assert (
        classification[
            "levels_separately_reported"
        ]
        is True
    )
    assert (
        classification[
            "persistent_capability_modified"
        ]
        is False
    )

    state = result["cognitive_state"]
    two_levels_state = state[
        "two_levels_of_learning"
    ]
    assert two_levels_state["contract"] == (
        TWO_LEVELS_OF_LEARNING_CONTRACT
    )
    assert two_levels_state["classifications"] == [
        classification
    ]
    assert two_levels_state["neural_change_records"] == [
        neural_record
    ]

    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )
    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-17"
    assert contract_event["operation"] == (
        "TWO_LEVELS_OF_LEARNING_CONTRACT_ESTABLISHED"
    )
    assert contract_event["level_separation_required"] is True
    assert contract_event["neural_learning_started"] is False

    classification_event = state["provenance"][-1]
    assert classification_event["core_id"] == "DNA-17"
    assert classification_event["operation"] == (
        "LEARNING_LEVELS_CLASSIFIED"
    )
    assert classification_event["learning_level"] == (
        "COGNITIVE_AND_NEURAL"
    )
    assert (
        classification_event[
            "levels_separately_reported"
        ]
        is True
    )
    assert (
        classification_event[
            "neural_learning_executed"
        ]
        is False
    )
    assert (
        classification_event[
            "persistent_capability_modified"
        ]
        is False
    )

    # DNA-17 must not mutate earlier memory, strategy, experience, or wall.
    assert state["memory_genome"] == pre_memory_genome
    assert (
        state["persistence_engine"]
        == pre_persistence_engine
    )
    assert (
        state["experience_driven_learning"]
        == pre_experience_learning
    )
    assert (
        state["independent_verification_wall"]
        == pre_verification_wall
    )

    # Replaying the same neural evidence must not duplicate its record.
    replay = dna17_core.activate(result)
    replay_output = replay["core54_outputs"]["DNA-17"]
    assert replay_output["learning_level"] == (
        "COGNITIVE_AND_NEURAL"
    )
    assert replay_output["neural_record_new"] is False
    assert replay_output["neural_change_record_count"] == 1
    assert len(
        replay["cognitive_state"][
            "two_levels_of_learning"
        ]["neural_change_records"]
    ) == 1

    # Cognitive-only evidence must never be mislabeled as neural.
    cognitive_only = dna17_core.activate(
        deepcopy(through_dna16)
    )
    cognitive_only_output = cognitive_only[
        "core54_outputs"
    ]["DNA-17"]
    assert cognitive_only_output["learning_level"] == (
        "COGNITIVE"
    )
    assert (
        cognitive_only_output["cognitive_learning"][
            "detected"
        ]
        is True
    )
    assert (
        cognitive_only_output["neural_learning"][
            "established"
        ]
        is False
    )
    assert (
        cognitive_only_output["neural_change_record_count"]
        == 0
    )

    # Neural-only evidence remains distinct from cognitive learning.
    neural_only_input = _clear_cognitive_evidence(
        through_dna16
    )
    neural_only_input["persistent_capability_change"] = (
        _valid_persistent_capability_change()
    )
    neural_only = dna17_core.activate(
        neural_only_input
    )
    neural_only_output = neural_only[
        "core54_outputs"
    ]["DNA-17"]
    assert neural_only_output["learning_level"] == (
        "NEURAL"
    )
    assert (
        neural_only_output["cognitive_learning"][
            "detected"
        ]
        is False
    )
    assert (
        neural_only_output["neural_learning"][
            "established"
        ]
        is True
    )

    # No evidence at either level must produce NONE.
    none_input = _clear_cognitive_evidence(
        through_dna16
    )
    none_input.pop(
        "persistent_capability_change",
        None,
    )
    none_result = dna17_core.activate(none_input)
    none_output = none_result[
        "core54_outputs"
    ]["DNA-17"]
    assert none_output["learning_level"] == "NONE"
    assert (
        none_output["cognitive_learning"]["detected"]
        is False
    )
    assert (
        none_output["neural_learning"]["established"]
        is False
    )

    # A before/after record with no actual change cannot be neural learning.
    unchanged_input = deepcopy(through_dna16)
    unchanged_change = (
        _valid_persistent_capability_change()
    )
    unchanged_change["after"] = deepcopy(
        unchanged_change["before"]
    )
    unchanged_candidate = {
        "capability_id": unchanged_change["capability_id"],
        "before": deepcopy(unchanged_change["before"]),
        "after": deepcopy(unchanged_change["after"]),
        "persistence_evidence": deepcopy(
            unchanged_change["persistence_evidence"]
        ),
    }
    unchanged_change["verification"][
        "candidate_sha256"
    ] = _sha256_json(unchanged_candidate)
    unchanged_input["persistent_capability_change"] = (
        unchanged_change
    )
    unchanged = dna17_core.activate(
        unchanged_input
    )
    unchanged_output = unchanged[
        "core54_outputs"
    ]["DNA-17"]
    assert unchanged_output["learning_level"] == (
        "COGNITIVE"
    )
    assert (
        "PERSISTENT_CAPABILITY_BEFORE_AFTER_UNCHANGED"
        in unchanged_output["neural_learning"][
            "rejection_reasons"
        ]
    )

    # Persistence evidence is mandatory for a neural-level claim.
    no_persistence_input = deepcopy(through_dna16)
    no_persistence_change = (
        _valid_persistent_capability_change()
    )
    no_persistence_change["persistence_evidence"] = []
    no_persistence_candidate = {
        "capability_id": (
            no_persistence_change["capability_id"]
        ),
        "before": deepcopy(
            no_persistence_change["before"]
        ),
        "after": deepcopy(
            no_persistence_change["after"]
        ),
        "persistence_evidence": [],
    }
    no_persistence_change["verification"][
        "candidate_sha256"
    ] = _sha256_json(no_persistence_candidate)
    no_persistence_input[
        "persistent_capability_change"
    ] = no_persistence_change
    no_persistence = dna17_core.activate(
        no_persistence_input
    )
    no_persistence_output = no_persistence[
        "core54_outputs"
    ]["DNA-17"]
    assert no_persistence_output["learning_level"] == (
        "COGNITIVE"
    )
    assert (
        "PERSISTENCE_EVIDENCE_REQUIRED"
        in no_persistence_output["neural_learning"][
            "rejection_reasons"
        ]
    )

    # Learner/verifier separation remains mandatory.
    self_verified_input = deepcopy(through_dna16)
    self_verified_change = (
        _valid_persistent_capability_change()
    )
    self_verified_change["verification"][
        "verifier_id"
    ] = "LEARNER-DNA17"
    self_verified_input[
        "persistent_capability_change"
    ] = self_verified_change
    self_verified = dna17_core.activate(
        self_verified_input
    )
    self_verified_output = self_verified[
        "core54_outputs"
    ]["DNA-17"]
    assert self_verified_output["learning_level"] == (
        "COGNITIVE"
    )
    assert (
        "LEARNER_VERIFIER_NOT_SEPARATED"
        in self_verified_output["neural_learning"][
            "rejection_reasons"
        ]
    )

    # Verification must bind to the exact capability-change candidate.
    wrong_binding_input = deepcopy(through_dna16)
    wrong_binding_change = (
        _valid_persistent_capability_change()
    )
    wrong_binding_change["verification"][
        "candidate_sha256"
    ] = "WRONG-CANDIDATE-HASH"
    wrong_binding_input[
        "persistent_capability_change"
    ] = wrong_binding_change
    wrong_binding = dna17_core.activate(
        wrong_binding_input
    )
    wrong_binding_output = wrong_binding[
        "core54_outputs"
    ]["DNA-17"]
    assert wrong_binding_output["learning_level"] == (
        "COGNITIVE"
    )
    assert (
        "VERIFICATION_NOT_BOUND_TO_CAPABILITY_CHANGE"
        in wrong_binding_output["neural_learning"][
            "rejection_reasons"
        ]
    )

    # Reject provisional root-marker behavior as the official contract.
    assert "learning_level" not in result
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result

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
        "core_id": "DNA-17",
        "canon_mapping": "PASS",
        "cognitive_neural_separation": "PASS",
        "cognitive_level": "PASS",
        "neural_level": "PASS",
        "persistent_capability_evidence": "PASS",
        "simultaneous_levels_separated": "PASS",
        "learning_runtime_used": False,
        "neural_learning_executed": False,
        "persistent_capability_modified": False,
        "model_or_adapter_promoted": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-18"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    required_gene_files = [
        (
            GENES_ROOT
            / f"SIGMA_DNA_{index:02d}_{name}.py"
        )
        for index, name in (
            (1, "PURPOSE_EXISTENCE"),
            (2, "FOUNDATION_INTELLIGENCE_SUBSTRATE"),
            (3, "UNIFIED_COGNITIVE_STATE"),
            (4, "EIGHT_COGNITIVE_LAYERS"),
            (5, "ETHICAL_INTELLIGENCE"),
            (6, "INTERLAYER_FEEDBACK"),
            (7, "PERSISTENT_EXISTENCE"),
            (8, "LEARNING_WORLD"),
            (9, "INDEPENDENT_VERIFICATION_WALL"),
            (10, "MEMORY_GENOME"),
            (11, "KNOWLEDGE_GRAPH"),
            (12, "TOOL_INTELLIGENCE"),
            (13, "ADAPTIVE_COGNITIVE_DEPTH"),
            (14, "PERSISTENCE_ENGINE"),
            (15, "F174_DEVELOPMENT_DYNAMICS"),
            (16, "EXPERIENCE_DRIVEN_LEARNING"),
        )
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print(
                "DNA-17_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )
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
        from SIGMA_DNA_14_PERSISTENCE_ENGINE import (
            self_check_dna14,
        )
        from SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS import (
            self_check_dna15,
        )
        from SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING import (
            self_check_dna16,
        )
    except Exception as exc:
        print("DNA-17_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(
            core.state.behavior_bound
            for core in core54.cores
        ):
            raise RuntimeError(
                "FRESH_FOUNDATION_REQUIRED"
            )

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
            ("DNA-14", self_check_dna14),
            ("DNA-15", self_check_dna15),
            ("DNA-16", self_check_dna16),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(
                    f"{core_id}_NOT_PASS"
                )

        report = self_check_dna17(
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
            for index in range(1, 18)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-17_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-17_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_17_PASS")
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "COGNITIVE_NEURAL_SEPARATION:",
        report["cognitive_neural_separation"],
    )
    print(
        "COGNITIVE_LEVEL:",
        report["cognitive_level"],
    )
    print(
        "NEURAL_LEVEL:",
        report["neural_level"],
    )
    print(
        "PERSISTENT_CAPABILITY_EVIDENCE:",
        report["persistent_capability_evidence"],
    )
    print(
        "SIMULTANEOUS_LEVELS_SEPARATED:",
        report["simultaneous_levels_separated"],
    )
    print(
        "LEARNING_RUNTIME_USED:",
        report["learning_runtime_used"],
    )
    print(
        "NEURAL_LEARNING_EXECUTED:",
        report["neural_learning_executed"],
    )
    print(
        "PERSISTENT_CAPABILITY_MODIFIED:",
        report["persistent_capability_modified"],
    )
    print(
        "MODEL_OR_ADAPTER_PROMOTED:",
        report["model_or_adapter_promoted"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print(
        "PHASE_LOCKS:",
        report["phase_locks"],
    )
    print("OFFICIAL_BOUND_CORES: 17/54")
    print("NEXT_AUTHORIZED: DNA-18")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
