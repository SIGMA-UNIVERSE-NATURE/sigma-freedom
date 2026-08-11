#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-19: MULTI-MODEL INTELLIGENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_19_MULTI_MODEL_INTELLIGENCE.py
"""

from __future__ import annotations

import hashlib
import importlib
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

CANON_DNA19: Dict[str, str] = {
    "id": "DNA-19",
    "name": "Multi-Model Intelligence",
    "purpose": (
        "Cho phép reasoner, critic, verifier, retriever và specialist "
        "phối hợp; consensus không đồng nghĩa truth."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
VERIFICATION_WALL_SCHEMA = (
    "SIGMA_INDEPENDENT_VERIFICATION_WALL_V1"
)
MODEL_EVOLUTION_SCHEMA = "SIGMA_MODEL_EVOLUTION_V1"
MULTI_MODEL_SCHEMA = "SIGMA_MULTI_MODEL_INTELLIGENCE_V1"

SUPPORTED_ROLES = [
    "REASONER",
    "CRITIC",
    "VERIFIER",
    "RETRIEVER",
    "SPECIALIST",
]

REQUIRED_CONTRIBUTION_FIELDS = [
    "participant_id",
    "role",
    "claim",
]

MULTI_MODEL_CONTRACT: Dict[str, Any] = {
    "schema": MULTI_MODEL_SCHEMA,
    "supported_roles": deepcopy(SUPPORTED_ROLES),
    "coordination_allowed": True,
    "multi_model_minimum_distinct_participants": 2,
    "full_role_coverage_requires_all_supported_roles": True,
    "contributions_remain_attributed": True,
    "consensus_rule": {
        "encoding": "UNANIMOUS_VALID_CONTRIBUTION_CLAIM_HASH",
        "canon_status": "IMPLEMENTATION_ENCODING_NOT_CANON_FIELD",
    },
    "consensus_equals_truth": False,
    "consensus_can_promote_knowledge": False,
    "independent_verification_remains_required": True,
    "model_calls_started": False,
    "external_verifier_invoked": False,
    "knowledge_promoted": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA09_AND_DNA18_BINDING"
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


def _non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA19:
        raise RuntimeError(
            "DNA-19_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA19,
                    "actual": actual,
                },
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
]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-19_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
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

    verification_contract = verification_wall.get(
        "contract"
    )
    if not isinstance(verification_contract, dict):
        raise RuntimeError(
            "DNA-09_VERIFICATION_WALL_CONTRACT_REQUIRED"
        )

    if verification_contract.get("schema") != (
        VERIFICATION_WALL_SCHEMA
    ):
        raise ValueError(
            "DNA-19_VERIFICATION_WALL_SCHEMA_MISMATCH:"
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

    model_evolution = state.get("model_evolution")
    if not isinstance(model_evolution, dict):
        raise RuntimeError(
            "DNA-18_MODEL_EVOLUTION_REQUIRED"
        )

    model_contract = model_evolution.get("contract")
    if not isinstance(model_contract, dict):
        raise RuntimeError(
            "DNA-18_MODEL_EVOLUTION_CONTRACT_REQUIRED"
        )

    if model_contract.get("schema") != MODEL_EVOLUTION_SCHEMA:
        raise ValueError(
            "DNA-19_MODEL_EVOLUTION_SCHEMA_MISMATCH:"
            f"{model_contract.get('schema')!r}"
        )

    if not isinstance(
        model_evolution.get("evaluations"),
        list,
    ):
        raise TypeError(
            "model_evolution['evaluations'] must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-18_OUTPUT_REQUIRED")

    dna18_output = outputs.get("DNA-18")
    if not isinstance(dna18_output, dict):
        raise RuntimeError("DNA-18_OUTPUT_REQUIRED")

    return state, verification_wall, model_evolution


def _install_multi_model_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("multi_model_intelligence")

    expected = {
        "contract": deepcopy(MULTI_MODEL_CONTRACT),
        "coordination_records": [],
    }

    if existing is None:
        state["multi_model_intelligence"] = expected
        return state["multi_model_intelligence"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['multi_model_intelligence'] "
            "must be a dict"
        )

    if existing.get("contract") != MULTI_MODEL_CONTRACT:
        raise ValueError(
            "DNA-19_MULTI_MODEL_CONTRACT_CONFLICT"
        )

    if not isinstance(
        existing.get("coordination_records"),
        list,
    ):
        raise TypeError(
            "multi_model_intelligence['coordination_records'] "
            "must be a list"
        )

    return existing


def _validate_contribution_types(
    contribution: Dict[str, Any],
) -> None:
    if (
        "participant_id" in contribution
        and not isinstance(
            contribution["participant_id"],
            str,
        )
    ):
        raise TypeError(
            "multi_model_contribution['participant_id'] "
            "must be a string"
        )

    if "role" in contribution and not isinstance(
        contribution["role"],
        str,
    ):
        raise TypeError(
            "multi_model_contribution['role'] must be a string"
        )

    if "evidence" in contribution and not isinstance(
        contribution["evidence"],
        list,
    ):
        raise TypeError(
            "multi_model_contribution['evidence'] must be a list"
        )

    if "confidence" in contribution:
        confidence = contribution["confidence"]
        if not isinstance(confidence, (int, float)):
            raise TypeError(
                "multi_model_contribution['confidence'] "
                "must be numeric"
            )
        if not 0.0 <= float(confidence) <= 1.0:
            raise ValueError(
                "DNA-19_CONFIDENCE_OUT_OF_RANGE"
            )


def _normalize_contribution(
    contribution: Any,
    index: int,
) -> Dict[str, Any]:
    errors: List[str] = []

    if not isinstance(contribution, dict):
        return {
            "index": index,
            "valid": False,
            "errors": ["CONTRIBUTION_MUST_BE_A_DICT"],
            "participant_id": None,
            "role": None,
            "claim": None,
            "claim_sha256": None,
            "evidence": [],
            "confidence": None,
            "contribution_sha256": None,
        }

    record = deepcopy(contribution)
    _validate_contribution_types(record)

    missing = [
        field
        for field in REQUIRED_CONTRIBUTION_FIELDS
        if field not in record
    ]
    if missing:
        errors.append("CONTRIBUTION_FIELDS_MISSING")

    participant_id = record.get("participant_id")
    if not _non_empty_text(participant_id):
        errors.append("PARTICIPANT_ID_REQUIRED")

    supplied_role = record.get("role")
    role = (
        supplied_role.strip().upper()
        if isinstance(supplied_role, str)
        else None
    )
    if role not in SUPPORTED_ROLES:
        errors.append("UNSUPPORTED_MULTI_MODEL_ROLE")

    claim_present = (
        "claim" in record
        and record.get("claim") is not None
    )
    if not claim_present:
        errors.append("CLAIM_REQUIRED")

    evidence = deepcopy(record.get("evidence", []))
    confidence = record.get("confidence")

    claim = deepcopy(record.get("claim"))
    claim_sha256 = (
        _sha256_json(claim)
        if claim_present
        else None
    )

    normalized_identity = {
        "participant_id": participant_id,
        "role": role,
        "claim_sha256": claim_sha256,
        "evidence": evidence,
        "confidence": confidence,
    }

    valid = not errors
    return {
        "index": index,
        "valid": valid,
        "errors": list(dict.fromkeys(errors)),
        "participant_id": participant_id,
        "role": role,
        "claim": claim,
        "claim_sha256": claim_sha256,
        "evidence": evidence,
        "confidence": confidence,
        "contribution_sha256": (
            _sha256_json(normalized_identity)
            if valid
            else None
        ),
    }


def _claim_groups(
    valid_contributions: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    groups: Dict[str, Dict[str, Any]] = {}

    for contribution in valid_contributions:
        claim_sha256 = contribution["claim_sha256"]
        group = groups.setdefault(
            claim_sha256,
            {
                "claim_sha256": claim_sha256,
                "claim": deepcopy(contribution["claim"]),
                "participant_ids": [],
                "roles": [],
                "contribution_count": 0,
            },
        )
        group["participant_ids"].append(
            contribution["participant_id"]
        )
        group["roles"].append(contribution["role"])
        group["contribution_count"] += 1

    return sorted(
        groups.values(),
        key=lambda item: (
            -item["contribution_count"],
            item["claim_sha256"],
        ),
    )


def _latest_positive_verification(
    verification_wall: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    for evaluation in reversed(
        verification_wall["evaluations"]
    ):
        if (
            isinstance(evaluation, dict)
            and evaluation.get("promotion_allowed") is True
            and evaluation.get("appropriate_verification") is True
        ):
            return deepcopy(evaluation)
    return None


def _latest_model_evolution_evaluation(
    model_evolution: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    evaluations = model_evolution["evaluations"]
    if not evaluations:
        return None
    latest = evaluations[-1]
    if not isinstance(latest, dict):
        raise TypeError(
            "DNA-18 model-evolution evaluation must be a dict"
        )
    return deepcopy(latest)


def _coordinate_contributions(
    supplied: Any,
    multi_model: Dict[str, Any],
    verification_wall: Dict[str, Any],
    model_evolution: Dict[str, Any],
) -> Dict[str, Any]:
    input_errors: List[str] = []

    if supplied is None:
        contributions: List[Any] = []
        input_errors.append(
            "MULTI_MODEL_CONTRIBUTIONS_REQUIRED"
        )
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['multi_model_contributions'] must be a list"
        )
    else:
        contributions = supplied

    normalized = [
        _normalize_contribution(
            contribution,
            index,
        )
        for index, contribution in enumerate(
            contributions,
            start=1,
        )
    ]

    valid = [
        contribution
        for contribution in normalized
        if contribution["valid"]
    ]
    invalid = [
        contribution
        for contribution in normalized
        if not contribution["valid"]
    ]

    participant_ids = [
        contribution["participant_id"]
        for contribution in valid
    ]
    distinct_participant_ids = sorted(
        set(participant_ids)
    )
    role_coverage = [
        role
        for role in SUPPORTED_ROLES
        if any(
            contribution["role"] == role
            for contribution in valid
        )
    ]
    missing_roles = [
        role
        for role in SUPPORTED_ROLES
        if role not in role_coverage
    ]

    multi_model_present = (
        len(distinct_participant_ids) >= 2
    )
    multi_role_present = len(role_coverage) >= 2
    coordination_ready = bool(
        multi_model_present
        and multi_role_present
        and len(valid) >= 2
    )
    full_role_coverage = not missing_roles

    groups = _claim_groups(valid)
    consensus_observed = bool(
        coordination_ready
        and len(groups) == 1
        and len(valid) >= 2
    )

    consensus_claim_sha256 = (
        groups[0]["claim_sha256"]
        if consensus_observed
        else None
    )
    consensus_claim = (
        deepcopy(groups[0]["claim"])
        if consensus_observed
        else None
    )

    if not valid:
        consensus_status = "NO_VALID_CONTRIBUTIONS"
    elif not multi_model_present:
        consensus_status = (
            "INSUFFICIENT_DISTINCT_MODELS"
        )
    elif len(valid) < 2:
        consensus_status = (
            "INSUFFICIENT_CONTRIBUTIONS"
        )
    elif len(groups) == 1:
        consensus_status = "CONSENSUS_OBSERVED"
    else:
        consensus_status = "DIVERGENCE_PRESENT"

    latest_verification = _latest_positive_verification(
        verification_wall
    )
    latest_model_evolution = (
        _latest_model_evolution_evaluation(
            model_evolution
        )
    )

    rejection_reasons = deepcopy(input_errors)
    rejection_reasons.extend(
        error
        for contribution in invalid
        for error in contribution["errors"]
    )
    if not multi_model_present:
        rejection_reasons.append(
            "MULTI_MODEL_MINIMUM_NOT_MET"
        )
    if not multi_role_present:
        rejection_reasons.append(
            "MULTI_ROLE_COORDINATION_NOT_MET"
        )

    sequence = len(
        multi_model["coordination_records"]
    ) + 1
    record = {
        "sequence": sequence,
        "coordination_id": (
            f"DNA-19-COORD-{sequence:04d}"
        ),
        "contributions": normalized,
        "valid_contribution_count": len(valid),
        "invalid_contribution_count": len(invalid),
        "distinct_participant_ids": (
            distinct_participant_ids
        ),
        "distinct_participant_count": len(
            distinct_participant_ids
        ),
        "role_coverage": role_coverage,
        "missing_roles": missing_roles,
        "multi_model_present": multi_model_present,
        "multi_role_present": multi_role_present,
        "coordination_ready": coordination_ready,
        "full_role_coverage": full_role_coverage,
        "claim_groups": groups,
        "consensus_observed": consensus_observed,
        "consensus_status": consensus_status,
        "consensus_claim": consensus_claim,
        "consensus_claim_sha256": (
            consensus_claim_sha256
        ),
        "consensus_establishes_truth": False,
        "truth_established": False,
        "truth_status": (
            "CONSENSUS_IS_NOT_TRUTH"
            if consensus_observed
            else "TRUTH_NOT_ESTABLISHED"
        ),
        "independent_verification_required": True,
        "latest_positive_verification_evaluation_id": (
            latest_verification.get("evaluation_id")
            if latest_verification is not None
            else None
        ),
        "latest_model_evolution_evaluation_id": (
            latest_model_evolution.get("evaluation_id")
            if latest_model_evolution is not None
            else None
        ),
        "prior_verification_used_as_consensus_truth": False,
        "knowledge_promoted": False,
        "model_calls_executed": False,
        "external_verifier_invoked": False,
        "rejection_reasons": list(
            dict.fromkeys(rejection_reasons)
        ),
        "status": (
            "MULTI_MODEL_COORDINATED"
            if coordination_ready
            else "MULTI_MODEL_COORDINATION_INCOMPLETE"
        ),
    }

    multi_model["coordination_records"].append(record)
    return record


def dna19_multi_model_intelligence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Coordinate attributed contributions from reasoner, critic, verifier,
    retriever, and specialist roles while explicitly refusing to equate
    agreement with truth.

    DNA-19 evaluates supplied contributions only. It does not call models,
    invoke an external verifier, promote knowledge, start a higher runtime,
    execute external action, or modify Canon.
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
    trace.append("DNA-19")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    (
        state,
        verification_wall,
        model_evolution,
    ) = _validate_dependencies(context)

    multi_model = _install_multi_model_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-19",
            "operation": (
                "MULTI_MODEL_INTELLIGENCE_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "multi_model_schema": MULTI_MODEL_SCHEMA,
            "supported_roles": deepcopy(SUPPORTED_ROLES),
            "consensus_equals_truth": False,
            "model_calls_started": False,
        }
    )

    coordination = _coordinate_contributions(
        context.get("multi_model_contributions"),
        multi_model,
        verification_wall,
        model_evolution,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-19",
            "operation": (
                "MULTI_MODEL_CONTRIBUTIONS_COORDINATED"
            ),
            "canonical_sha256": canonical_sha256,
            "coordination_id": (
                coordination["coordination_id"]
            ),
            "role_coverage": deepcopy(
                coordination["role_coverage"]
            ),
            "multi_model_present": (
                coordination["multi_model_present"]
            ),
            "consensus_observed": (
                coordination["consensus_observed"]
            ),
            "consensus_establishes_truth": False,
            "truth_established": False,
            "knowledge_promoted": False,
        }
    )

    outputs["DNA-19"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "multi_model_contract": deepcopy(
            MULTI_MODEL_CONTRACT
        ),
        "coordination": deepcopy(coordination),
        "coordination_ready": (
            coordination["coordination_ready"]
        ),
        "full_role_coverage": (
            coordination["full_role_coverage"]
        ),
        "consensus_observed": (
            coordination["consensus_observed"]
        ),
        "consensus_establishes_truth": False,
        "truth_established": False,
        "knowledge_promoted": False,
        "model_calls_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna19(core54: Core54Like) -> None:
    core = core54.get("DNA-19")
    assert_exact_canon(core)
    core54.bind(
        "DNA-19",
        dna19_multi_model_intelligence,
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


def _five_role_contributions(
    claim: Any,
) -> List[Dict[str, Any]]:
    return [
        {
            "participant_id": "MODEL-REASONER-01",
            "role": "reasoner",
            "claim": deepcopy(claim),
            "evidence": [
                {
                    "type": "REASONING_TRACE_REFERENCE",
                    "reference": "TRACE-01",
                }
            ],
            "confidence": 0.82,
        },
        {
            "participant_id": "MODEL-CRITIC-01",
            "role": "critic",
            "claim": deepcopy(claim),
            "evidence": [
                {
                    "type": "CRITIQUE_REFERENCE",
                    "reference": "CRITIQUE-01",
                }
            ],
            "confidence": 0.74,
        },
        {
            "participant_id": "MODEL-VERIFIER-01",
            "role": "verifier",
            "claim": deepcopy(claim),
            "evidence": [
                {
                    "type": "VERIFIER_REFERENCE",
                    "reference": "VERIFY-01",
                }
            ],
            "confidence": 0.91,
        },
        {
            "participant_id": "MODEL-RETRIEVER-01",
            "role": "retriever",
            "claim": deepcopy(claim),
            "evidence": [
                {
                    "type": "RETRIEVAL_REFERENCE",
                    "reference": "RETRIEVAL-01",
                }
            ],
            "confidence": 0.88,
        },
        {
            "participant_id": "MODEL-SPECIALIST-01",
            "role": "specialist",
            "claim": deepcopy(claim),
            "evidence": [
                {
                    "type": "SPECIALIST_REFERENCE",
                    "reference": "SPECIALIST-01",
                }
            ],
            "confidence": 0.86,
        },
    ]


def self_check_dna19(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 19):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna19_core = core54.get("DNA-19")
    assert_exact_canon(dna19_core)
    bind_dna19(core54)

    from SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING import (
        _complete_probe as dna16_complete_probe,
    )
    from SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING import (
        _valid_persistent_capability_change,
    )
    from SIGMA_DNA_18_MODEL_EVOLUTION import (
        _valid_model_evolution_candidate,
    )

    probe = dna16_complete_probe(core54)
    probe["persistent_capability_change"] = (
        _valid_persistent_capability_change()
    )
    snapshot = deepcopy(probe)

    through_dna17 = _run_through(core54, probe, 17)
    through_dna17["model_evolution_candidate"] = (
        _valid_model_evolution_candidate("MODEL")
    )
    through_dna18 = core54.get("DNA-18").activate(
        through_dna17
    )

    model_evaluation = through_dna18[
        "core54_outputs"
    ]["DNA-18"]["evaluation"]
    claim = {
        "statement": (
            "MODEL_CANDIDATE_PASSED_DNA18_GATES"
        ),
        "candidate_sha256": model_evaluation[
            "candidate_sha256"
        ],
        "promotion_eligible": model_evaluation[
            "promotion_eligible"
        ],
    }

    pre_verification_wall = deepcopy(
        through_dna18["cognitive_state"][
            "independent_verification_wall"
        ]
    )
    pre_model_evolution = deepcopy(
        through_dna18["cognitive_state"][
            "model_evolution"
        ]
    )
    pre_provenance_count = len(
        through_dna18["cognitive_state"][
            "provenance"
        ]
    )

    consensus_input = deepcopy(through_dna18)
    consensus_input["multi_model_contributions"] = (
        _five_role_contributions(claim)
    )
    result = dna19_core.activate(consensus_input)

    assert probe == snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 20)
    ]

    dna19 = result["core54_outputs"]["DNA-19"]
    assert dna19["canonical_gene"] == CANON_DNA19
    assert dna19["multi_model_contract"] == (
        MULTI_MODEL_CONTRACT
    )
    assert dna19["coordination_ready"] is True
    assert dna19["full_role_coverage"] is True
    assert dna19["consensus_observed"] is True
    assert (
        dna19["consensus_establishes_truth"]
        is False
    )
    assert dna19["truth_established"] is False
    assert dna19["knowledge_promoted"] is False
    assert dna19["model_calls_executed"] is False
    assert dna19["status"] == "CANON_ALIGNED"

    coordination = dna19["coordination"]
    assert coordination["coordination_id"] == (
        "DNA-19-COORD-0001"
    )
    assert coordination["valid_contribution_count"] == 5
    assert coordination["invalid_contribution_count"] == 0
    assert coordination["distinct_participant_count"] == 5
    assert coordination["role_coverage"] == SUPPORTED_ROLES
    assert coordination["missing_roles"] == []
    assert coordination["multi_model_present"] is True
    assert coordination["multi_role_present"] is True
    assert coordination["coordination_ready"] is True
    assert coordination["full_role_coverage"] is True
    assert coordination["consensus_observed"] is True
    assert coordination["consensus_status"] == (
        "CONSENSUS_OBSERVED"
    )
    assert coordination["consensus_claim"] == claim
    assert coordination["consensus_claim_sha256"] == (
        _sha256_json(claim)
    )
    assert coordination["consensus_establishes_truth"] is False
    assert coordination["truth_established"] is False
    assert coordination["truth_status"] == (
        "CONSENSUS_IS_NOT_TRUTH"
    )
    assert (
        coordination["independent_verification_required"]
        is True
    )
    assert (
        coordination[
            "prior_verification_used_as_consensus_truth"
        ]
        is False
    )
    assert coordination["knowledge_promoted"] is False
    assert coordination["model_calls_executed"] is False
    assert coordination["rejection_reasons"] == []
    assert coordination["status"] == (
        "MULTI_MODEL_COORDINATED"
    )

    state = result["cognitive_state"]
    multi_model = state["multi_model_intelligence"]
    assert multi_model["contract"] == MULTI_MODEL_CONTRACT
    assert multi_model["coordination_records"] == [
        coordination
    ]
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-19"
    assert contract_event["operation"] == (
        "MULTI_MODEL_INTELLIGENCE_CONTRACT_ESTABLISHED"
    )
    assert contract_event["supported_roles"] == (
        SUPPORTED_ROLES
    )
    assert contract_event["consensus_equals_truth"] is False
    assert contract_event["model_calls_started"] is False

    coordination_event = state["provenance"][-1]
    assert coordination_event["core_id"] == "DNA-19"
    assert coordination_event["operation"] == (
        "MULTI_MODEL_CONTRIBUTIONS_COORDINATED"
    )
    assert coordination_event["role_coverage"] == (
        SUPPORTED_ROLES
    )
    assert coordination_event["multi_model_present"] is True
    assert coordination_event["consensus_observed"] is True
    assert (
        coordination_event["consensus_establishes_truth"]
        is False
    )
    assert coordination_event["truth_established"] is False
    assert coordination_event["knowledge_promoted"] is False

    # DNA-19 must not mutate prior verification or model-evolution state.
    assert (
        state["independent_verification_wall"]
        == pre_verification_wall
    )
    assert state["model_evolution"] == pre_model_evolution

    # Divergence must remain visible and must not be converted to truth.
    divergent_input = deepcopy(through_dna18)
    divergent_contributions = _five_role_contributions(
        claim
    )
    divergent_contributions[1]["claim"] = {
        "statement": "CRITIC_DISAGREES",
        "candidate_sha256": model_evaluation[
            "candidate_sha256"
        ],
    }
    divergent_input["multi_model_contributions"] = (
        divergent_contributions
    )
    divergent = dna19_core.activate(divergent_input)
    divergent_record = divergent[
        "core54_outputs"
    ]["DNA-19"]["coordination"]
    assert divergent_record["coordination_ready"] is True
    assert divergent_record["consensus_observed"] is False
    assert divergent_record["consensus_status"] == (
        "DIVERGENCE_PRESENT"
    )
    assert divergent_record["truth_established"] is False
    assert divergent_record["truth_status"] == (
        "TRUTH_NOT_ESTABLISHED"
    )

    # Five roles played by one participant are not multi-model intelligence.
    single_model_input = deepcopy(through_dna18)
    single_model_contributions = _five_role_contributions(
        claim
    )
    for contribution in single_model_contributions:
        contribution["participant_id"] = "MODEL-SINGLE-01"
    single_model_input["multi_model_contributions"] = (
        single_model_contributions
    )
    single_model = dna19_core.activate(single_model_input)
    single_model_record = single_model[
        "core54_outputs"
    ]["DNA-19"]["coordination"]
    assert single_model_record["full_role_coverage"] is True
    assert single_model_record["multi_model_present"] is False
    assert single_model_record["coordination_ready"] is False
    assert single_model_record["consensus_observed"] is False
    assert single_model_record["consensus_status"] == (
        "INSUFFICIENT_DISTINCT_MODELS"
    )
    assert (
        "MULTI_MODEL_MINIMUM_NOT_MET"
        in single_model_record["rejection_reasons"]
    )

    # Unknown roles cannot silently enter the coordination contract.
    invalid_role_input = deepcopy(through_dna18)
    invalid_role_contributions = _five_role_contributions(
        claim
    )
    invalid_role_contributions[4]["role"] = "ORACLE"
    invalid_role_input["multi_model_contributions"] = (
        invalid_role_contributions
    )
    invalid_role = dna19_core.activate(invalid_role_input)
    invalid_role_record = invalid_role[
        "core54_outputs"
    ]["DNA-19"]["coordination"]
    assert invalid_role_record["invalid_contribution_count"] == 1
    assert "SPECIALIST" in invalid_role_record["missing_roles"]
    assert invalid_role_record["full_role_coverage"] is False
    assert (
        "UNSUPPORTED_MULTI_MODEL_ROLE"
        in invalid_role_record["rejection_reasons"]
    )

    # No supplied contributions cannot be presented as coordination.
    no_contributions = dna19_core.activate(
        deepcopy(through_dna18)
    )
    no_contributions_record = no_contributions[
        "core54_outputs"
    ]["DNA-19"]["coordination"]
    assert no_contributions_record["coordination_ready"] is False
    assert no_contributions_record["consensus_observed"] is False
    assert no_contributions_record["truth_established"] is False
    assert (
        "MULTI_MODEL_CONTRIBUTIONS_REQUIRED"
        in no_contributions_record["rejection_reasons"]
    )

    # Reject the old provisional root-marker contract.
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result
    assert "consensus_is_not_truth" not in result

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
        "core_id": "DNA-19",
        "canon_mapping": "PASS",
        "reasoner_role": "PASS",
        "critic_role": "PASS",
        "verifier_role": "PASS",
        "retriever_role": "PASS",
        "specialist_role": "PASS",
        "multi_model_coordination": "PASS",
        "consensus_not_truth": "PASS",
        "model_calls_executed": False,
        "knowledge_promoted": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-20"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    names = {
        1: "PURPOSE_EXISTENCE",
        2: "FOUNDATION_INTELLIGENCE_SUBSTRATE",
        3: "UNIFIED_COGNITIVE_STATE",
        4: "EIGHT_COGNITIVE_LAYERS",
        5: "ETHICAL_INTELLIGENCE",
        6: "INTERLAYER_FEEDBACK",
        7: "PERSISTENT_EXISTENCE",
        8: "LEARNING_WORLD",
        9: "INDEPENDENT_VERIFICATION_WALL",
        10: "MEMORY_GENOME",
        11: "KNOWLEDGE_GRAPH",
        12: "TOOL_INTELLIGENCE",
        13: "ADAPTIVE_COGNITIVE_DEPTH",
        14: "PERSISTENCE_ENGINE",
        15: "F174_DEVELOPMENT_DYNAMICS",
        16: "EXPERIENCE_DRIVEN_LEARNING",
        17: "TWO_LEVELS_OF_LEARNING",
        18: "MODEL_EVOLUTION",
    }
    required_gene_files = [
        (
            GENES_ROOT
            / f"SIGMA_DNA_{index:02d}_{names[index]}.py"
        )
        for index in range(1, 19)
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
                "DNA-19_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    module_names = {
        index: f"SIGMA_DNA_{index:02d}_{names[index]}"
        for index in range(1, 19)
    }

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )
        modules = {
            index: importlib.import_module(module_name)
            for index, module_name in module_names.items()
        }
    except Exception as exc:
        print("DNA-19_FAIL: IMPORT_ERROR")
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

        for index in range(1, 19):
            checker = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(
                    f"DNA-{index:02d}_NOT_PASS"
                )

        report = self_check_dna19(
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
            for index in range(1, 20)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-19_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-19_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_19_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("REASONER_ROLE:", report["reasoner_role"])
    print("CRITIC_ROLE:", report["critic_role"])
    print("VERIFIER_ROLE:", report["verifier_role"])
    print("RETRIEVER_ROLE:", report["retriever_role"])
    print("SPECIALIST_ROLE:", report["specialist_role"])
    print(
        "MULTI_MODEL_COORDINATION:",
        report["multi_model_coordination"],
    )
    print(
        "CONSENSUS_NOT_TRUTH:",
        report["consensus_not_truth"],
    )
    print(
        "MODEL_CALLS_EXECUTED:",
        report["model_calls_executed"],
    )
    print(
        "KNOWLEDGE_PROMOTED:",
        report["knowledge_promoted"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 19/54")
    print("NEXT_AUTHORIZED: DNA-20")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
