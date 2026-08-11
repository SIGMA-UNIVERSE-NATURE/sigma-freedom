#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-16: EXPERIENCE-DRIVEN LEARNING
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING.py
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

CANON_DNA16: Dict[str, str] = {
    "id": "DNA-16",
    "name": "Experience-Driven Learning",
    "purpose": (
        "Đơn vị học là observation+hypothesis+action+outcome+verification; "
        "chỉ trải nghiệm đủ chuẩn mới được giữ."
    ),
    "system": "learning",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
VERIFICATION_WALL_SCHEMA = (
    "SIGMA_INDEPENDENT_VERIFICATION_WALL_V1"
)
MEMORY_GENOME_SCHEMA = "SIGMA_MEMORY_GENOME_V1"
F174_SCHEMA = "SIGMA_F174_DEVELOPMENT_DYNAMICS_V1"
EXPERIENCE_LEARNING_SCHEMA = (
    "SIGMA_EXPERIENCE_DRIVEN_LEARNING_V1"
)

LEARNING_UNIT_COMPONENTS = [
    "observation",
    "hypothesis",
    "action",
    "outcome",
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

EXPERIENCE_DRIVEN_LEARNING_CONTRACT: Dict[str, Any] = {
    "schema": EXPERIENCE_LEARNING_SCHEMA,
    "learning_unit": deepcopy(LEARNING_UNIT_COMPONENTS),
    "learning_unit_component_count": 5,
    "all_components_required": True,
    "verification_required": True,
    "independent_verification_binding": "DNA-09",
    "retain_only_sufficient_experience": True,
    "incomplete_experience_retained": False,
    "failed_verification_experience_retained": False,
    "retention_scope": "CURRENT_STRUCTURED_STATE",
    "persistent_memory_runtime_started": False,
    "learning_runtime_started": False,
    "neural_learning_started": False,
    "knowledge_promotion_executed": False,
    "external_action_executed": False,
    "derivation": "DIRECT_FROM_CANON_PURPOSE_WITH_DNA09_BINDING",
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
    if actual != CANON_DNA16:
        raise RuntimeError(
            "DNA-16_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA16, "actual": actual},
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
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-16_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    verification_wall = state.get("independent_verification_wall")
    if not isinstance(verification_wall, dict):
        raise RuntimeError(
            "DNA-09_INDEPENDENT_VERIFICATION_WALL_REQUIRED"
        )

    verification_contract = verification_wall.get("contract")
    if not isinstance(verification_contract, dict):
        raise RuntimeError("DNA-09_VERIFICATION_WALL_CONTRACT_REQUIRED")

    if verification_contract.get("schema") != VERIFICATION_WALL_SCHEMA:
        raise ValueError(
            "DNA-16_VERIFICATION_WALL_SCHEMA_MISMATCH:"
            f"{verification_contract.get('schema')!r}"
        )

    if not isinstance(verification_wall.get("evaluations"), list):
        raise TypeError(
            "independent_verification_wall['evaluations'] must be a list"
        )

    memory_genome = state.get("memory_genome")
    if not isinstance(memory_genome, dict):
        raise RuntimeError("DNA-10_MEMORY_GENOME_REQUIRED")

    memory_contract = memory_genome.get("contract")
    if not isinstance(memory_contract, dict):
        raise RuntimeError("DNA-10_MEMORY_GENOME_CONTRACT_REQUIRED")

    if memory_contract.get("schema") != MEMORY_GENOME_SCHEMA:
        raise ValueError(
            "DNA-16_MEMORY_GENOME_SCHEMA_MISMATCH:"
            f"{memory_contract.get('schema')!r}"
        )

    f174_state = state.get("f174_development_dynamics")
    if not isinstance(f174_state, dict):
        raise RuntimeError("DNA-15_F174_DEVELOPMENT_DYNAMICS_REQUIRED")

    f174_contract = f174_state.get("contract")
    if not isinstance(f174_contract, dict):
        raise RuntimeError("DNA-15_F174_CONTRACT_REQUIRED")

    if f174_contract.get("schema") != F174_SCHEMA:
        raise ValueError(
            "DNA-16_F174_SCHEMA_MISMATCH:"
            f"{f174_contract.get('schema')!r}"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-15_OUTPUT_REQUIRED")

    dna15_output = outputs.get("DNA-15")
    if not isinstance(dna15_output, dict):
        raise RuntimeError("DNA-15_OUTPUT_REQUIRED")

    return state, verification_wall, memory_genome, dna15_output


def _install_experience_learning_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("experience_driven_learning")

    expected = {
        "contract": deepcopy(EXPERIENCE_DRIVEN_LEARNING_CONTRACT),
        "retained_experiences": [],
        "evaluations": [],
    }

    if existing is None:
        state["experience_driven_learning"] = expected
        return state["experience_driven_learning"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['experience_driven_learning'] must be a dict"
        )

    if existing.get("contract") != EXPERIENCE_DRIVEN_LEARNING_CONTRACT:
        raise ValueError("DNA-16_EXPERIENCE_LEARNING_CONTRACT_CONFLICT")

    if not isinstance(existing.get("retained_experiences"), list):
        raise TypeError(
            "experience_driven_learning['retained_experiences'] "
            "must be a list"
        )

    if not isinstance(existing.get("evaluations"), list):
        raise TypeError(
            "experience_driven_learning['evaluations'] must be a list"
        )

    return existing


def _non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _non_empty_list(value: Any) -> bool:
    return isinstance(value, list) and len(value) > 0


def _validate_verification_types(
    verification: Dict[str, Any],
) -> None:
    for field in ("verifier_independent", "passed"):
        if field in verification and not isinstance(
            verification[field], bool
        ):
            raise TypeError(
                f"experience verification['{field}'] must be a bool"
            )

    for field in (
        "learner_id",
        "verifier_id",
        "candidate_sha256",
        "method",
        "scope",
    ):
        if field in verification and not isinstance(
            verification[field], str
        ):
            raise TypeError(
                f"experience verification['{field}'] must be a string"
            )

    for field in ("independence_basis", "evidence"):
        if field in verification and not isinstance(
            verification[field], list
        ):
            raise TypeError(
                f"experience verification['{field}'] must be a list"
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
        reasons.append("LEARNER_VERIFIER_NOT_SEPARATED")

    if verification.get("verifier_independent") is not True:
        reasons.append("INDEPENDENT_VERIFIER_REQUIRED")

    if not _non_empty_list(verification.get("independence_basis")):
        reasons.append("INDEPENDENCE_BASIS_REQUIRED")

    if verification.get("candidate_sha256") != candidate_sha256:
        reasons.append("VERIFICATION_NOT_BOUND_TO_LEARNING_UNIT")

    if not _non_empty_text(verification.get("method")):
        reasons.append("VERIFICATION_METHOD_REQUIRED")

    if not _non_empty_text(verification.get("scope")):
        reasons.append("VERIFICATION_SCOPE_REQUIRED")

    if not _non_empty_list(verification.get("evidence")):
        reasons.append("VERIFICATION_EVIDENCE_REQUIRED")

    if verification.get("passed") is not True:
        reasons.append("VERIFIER_PASS_REQUIRED")

    return list(dict.fromkeys(reasons))


def _evaluate_learning_unit(
    context: Dict[str, Any],
) -> Dict[str, Any]:
    supplied = context.get("experience_learning_unit")

    if supplied is None:
        return {
            "normalized_unit": None,
            "candidate_sha256": None,
            "unit_sha256": None,
            "complete": False,
            "qualified": False,
            "missing_components": deepcopy(LEARNING_UNIT_COMPONENTS),
            "rejection_reasons": ["EXPERIENCE_LEARNING_UNIT_REQUIRED"],
        }

    if not isinstance(supplied, dict):
        raise TypeError("context['experience_learning_unit'] must be a dict")

    missing = [
        component
        for component in LEARNING_UNIT_COMPONENTS
        if component not in supplied or supplied[component] is None
    ]

    if missing:
        return {
            "normalized_unit": None,
            "candidate_sha256": None,
            "unit_sha256": None,
            "complete": False,
            "qualified": False,
            "missing_components": missing,
            "rejection_reasons": ["LEARNING_UNIT_COMPONENTS_MISSING"],
        }

    normalized = {
        component: deepcopy(supplied[component])
        for component in LEARNING_UNIT_COMPONENTS
    }
    candidate_content = {
        component: deepcopy(normalized[component])
        for component in (
            "observation",
            "hypothesis",
            "action",
            "outcome",
        )
    }
    candidate_sha256 = _sha256_json(candidate_content)
    verification_reasons = _evaluate_verification(
        candidate_sha256,
        normalized["verification"],
    )
    qualified = len(verification_reasons) == 0

    return {
        "normalized_unit": normalized,
        "candidate_sha256": candidate_sha256,
        "unit_sha256": _sha256_json(normalized),
        "complete": True,
        "qualified": qualified,
        "missing_components": [],
        "rejection_reasons": verification_reasons,
    }


def _retain_if_qualified(
    learning_state: Dict[str, Any],
    evaluation: Dict[str, Any],
) -> Tuple[Optional[Dict[str, Any]], bool]:
    if evaluation["qualified"] is not True:
        return None, False

    unit_sha256 = evaluation["unit_sha256"]
    retained = learning_state["retained_experiences"]

    for existing in retained:
        if existing.get("unit_sha256") == unit_sha256:
            return existing, False

    sequence = len(retained) + 1
    record = {
        "retention_id": f"DNA-16-EXP-{sequence:04d}",
        "sequence": sequence,
        "learning_unit": deepcopy(evaluation["normalized_unit"]),
        "candidate_sha256": evaluation["candidate_sha256"],
        "unit_sha256": unit_sha256,
        "complete": True,
        "sufficiently_qualified": True,
        "verification_passed": True,
        "retained": True,
        "retention_scope": "CURRENT_STRUCTURED_STATE",
        "persistent_memory_runtime_used": False,
        "learning_runtime_used": False,
        "knowledge_promotion_executed": False,
        "status": "QUALIFIED_EXPERIENCE_RETAINED",
    }
    retained.append(record)
    return record, True


def dna16_experience_driven_learning(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Form the exact five-part learning unit and retain it only when complete
    and independently verified.

    DNA-16 does not start Learning Runtime, persistent Memory Runtime,
    neural adaptation, model calls, F174 experiments, external execution,
    knowledge promotion, or Canon writes.
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
    trace.append("DNA-16")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    state, _wall, _genome, _dna15_output = _validate_dependencies(context)
    learning_state = _install_experience_learning_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-16",
            "operation": "EXPERIENCE_LEARNING_CONTRACT_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "experience_learning_schema": EXPERIENCE_LEARNING_SCHEMA,
            "learning_unit_component_count": 5,
            "retain_only_sufficient_experience": True,
            "learning_runtime_started": False,
        }
    )

    evaluation = _evaluate_learning_unit(context)
    retained_record, retained_new = _retain_if_qualified(
        learning_state,
        evaluation,
    )

    evaluation_sequence = len(learning_state["evaluations"]) + 1
    evaluation_event = {
        "sequence": evaluation_sequence,
        "evaluation_id": f"DNA-16-EVAL-{evaluation_sequence:04d}",
        "candidate_sha256": evaluation["candidate_sha256"],
        "unit_sha256": evaluation["unit_sha256"],
        "complete": evaluation["complete"],
        "sufficiently_qualified": evaluation["qualified"],
        "missing_components": deepcopy(evaluation["missing_components"]),
        "rejection_reasons": deepcopy(evaluation["rejection_reasons"]),
        "retained": retained_record is not None,
        "retained_new": retained_new,
        "retention_id": (
            retained_record["retention_id"]
            if retained_record is not None
            else None
        ),
        "status": (
            "QUALIFIED_EXPERIENCE_RETAINED"
            if retained_new
            else (
                "QUALIFIED_EXPERIENCE_ALREADY_RETAINED"
                if retained_record is not None
                else "EXPERIENCE_NOT_RETAINED"
            )
        ),
    }
    learning_state["evaluations"].append(evaluation_event)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-16",
            "operation": "EXPERIENCE_RETENTION_EVALUATED",
            "canonical_sha256": canonical_sha256,
            "evaluation_id": evaluation_event["evaluation_id"],
            "complete": evaluation_event["complete"],
            "sufficiently_qualified": evaluation_event[
                "sufficiently_qualified"
            ],
            "retained": evaluation_event["retained"],
            "retained_new": evaluation_event["retained_new"],
            "retention_id": evaluation_event["retention_id"],
            "learning_runtime_used": False,
            "persistent_memory_runtime_used": False,
        }
    )

    outputs["DNA-16"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "experience_learning_contract": deepcopy(
            EXPERIENCE_DRIVEN_LEARNING_CONTRACT
        ),
        "experience_complete": evaluation["complete"],
        "sufficiently_qualified": evaluation["qualified"],
        "missing_components": deepcopy(evaluation["missing_components"]),
        "rejection_reasons": deepcopy(evaluation["rejection_reasons"]),
        "candidate_sha256": evaluation["candidate_sha256"],
        "unit_sha256": evaluation["unit_sha256"],
        "retained": retained_record is not None,
        "retained_new": retained_new,
        "retained_record": deepcopy(retained_record),
        "retention_count": len(learning_state["retained_experiences"]),
        "learning_runtime_used": False,
        "persistent_memory_runtime_used": False,
        "knowledge_promotion_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna16(core54: Core54Like) -> None:
    core = core54.get("DNA-16")
    assert_exact_canon(core)
    core54.bind("DNA-16", dna16_experience_driven_learning)


def _run_through(
    core54: Core54Like,
    context: Dict[str, Any],
    final_index: int,
) -> Dict[str, Any]:
    result = deepcopy(context)
    for index in range(1, final_index + 1):
        result = core54.get(f"DNA-{index:02d}").activate(result)
    return result


def _complete_probe(core54: Core54Like) -> Dict[str, Any]:
    from SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS import (
        _complete_probe as dna15_complete_probe,
    )

    probe = dna15_complete_probe(core54)
    candidate_content = {
        "observation": {
            "id": "OBS-DNA16-01",
            "value": "INTERVENTION_PRECEDED_OBSERVED_CHANGE",
        },
        "hypothesis": {
            "id": "HYP-DNA16-01",
            "statement": "INTERVENTION_CAUSES_STATE_CHANGE",
        },
        "action": {
            "id": "ACT-DNA16-01",
            "description": "REPEAT_CONTROLLED_INTERVENTION",
        },
        "outcome": {
            "id": "OUT-DNA16-01",
            "observed": "STATE_CHANGE_REPRODUCED",
        },
    }
    candidate_sha256 = _sha256_json(candidate_content)
    probe["experience_learning_unit"] = {
        **deepcopy(candidate_content),
        "verification": {
            "learner_id": "LEARNER-DNA16",
            "verifier_id": "VERIFIER-DNA16-INDEPENDENT",
            "verifier_independent": True,
            "independence_basis": [
                "SEPARATE_ROLE",
                "NO_SHARED_DECISION_AUTHORITY",
            ],
            "candidate_sha256": candidate_sha256,
            "method": "INDEPENDENT_REPLAY_AND_EVIDENCE_CHECK",
            "scope": "DNA-16_EXPERIENCE_LEARNING_UNIT",
            "evidence": [
                {
                    "type": "INDEPENDENT_REPLAY",
                    "result": "CONSISTENT",
                },
                {
                    "type": "OUTCOME_CHECK",
                    "result": "SUPPORTED",
                },
            ],
            "passed": True,
        },
    }
    return probe


def self_check_dna16(
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
        "DNA-14",
        "DNA-15",
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna16_core = core54.get("DNA-16")
    assert_exact_canon(dna16_core)
    bind_dna16(core54)

    probe = _complete_probe(core54)
    snapshot = deepcopy(probe)
    through_dna15 = _run_through(core54, probe, 15)
    pre_provenance_count = len(
        through_dna15["cognitive_state"]["provenance"]
    )
    pre_memory_genome = deepcopy(
        through_dna15["cognitive_state"]["memory_genome"]
    )
    pre_verification_wall = deepcopy(
        through_dna15["cognitive_state"][
            "independent_verification_wall"
        ]
    )
    result = dna16_core.activate(through_dna15)

    assert probe == snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 17)
    ]

    dna16 = result["core54_outputs"]["DNA-16"]
    assert dna16["canonical_gene"] == CANON_DNA16
    assert dna16["experience_learning_contract"] == (
        EXPERIENCE_DRIVEN_LEARNING_CONTRACT
    )
    assert dna16["experience_complete"] is True
    assert dna16["sufficiently_qualified"] is True
    assert dna16["missing_components"] == []
    assert dna16["rejection_reasons"] == []
    assert dna16["retained"] is True
    assert dna16["retained_new"] is True
    assert dna16["retention_count"] == 1
    assert dna16["learning_runtime_used"] is False
    assert dna16["persistent_memory_runtime_used"] is False
    assert dna16["knowledge_promotion_executed"] is False
    assert dna16["status"] == "CANON_ALIGNED"

    retained = dna16["retained_record"]
    assert retained["retention_id"] == "DNA-16-EXP-0001"
    assert retained["sequence"] == 1
    assert retained["complete"] is True
    assert retained["sufficiently_qualified"] is True
    assert retained["verification_passed"] is True
    assert retained["retained"] is True
    assert retained["retention_scope"] == "CURRENT_STRUCTURED_STATE"
    assert retained["persistent_memory_runtime_used"] is False
    assert retained["learning_runtime_used"] is False
    assert retained["knowledge_promotion_executed"] is False
    assert retained["status"] == "QUALIFIED_EXPERIENCE_RETAINED"
    assert list(retained["learning_unit"]) == LEARNING_UNIT_COMPONENTS
    assert retained["candidate_sha256"] == dna16["candidate_sha256"]
    assert retained["unit_sha256"] == dna16["unit_sha256"]

    state = result["cognitive_state"]
    learning_state = state["experience_driven_learning"]
    assert learning_state["contract"] == (
        EXPERIENCE_DRIVEN_LEARNING_CONTRACT
    )
    assert learning_state["retained_experiences"] == [retained]
    assert len(learning_state["evaluations"]) == 1

    evaluation = learning_state["evaluations"][0]
    assert evaluation["complete"] is True
    assert evaluation["sufficiently_qualified"] is True
    assert evaluation["missing_components"] == []
    assert evaluation["rejection_reasons"] == []
    assert evaluation["retained"] is True
    assert evaluation["retained_new"] is True
    assert evaluation["retention_id"] == "DNA-16-EXP-0001"
    assert evaluation["status"] == "QUALIFIED_EXPERIENCE_RETAINED"

    assert len(state["provenance"]) == pre_provenance_count + 2
    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-16"
    assert contract_event["operation"] == (
        "EXPERIENCE_LEARNING_CONTRACT_ESTABLISHED"
    )
    assert contract_event["learning_unit_component_count"] == 5
    assert contract_event["retain_only_sufficient_experience"] is True
    assert contract_event["learning_runtime_started"] is False

    retention_event = state["provenance"][-1]
    assert retention_event["core_id"] == "DNA-16"
    assert retention_event["operation"] == (
        "EXPERIENCE_RETENTION_EVALUATED"
    )
    assert retention_event["complete"] is True
    assert retention_event["sufficiently_qualified"] is True
    assert retention_event["retained"] is True
    assert retention_event["retained_new"] is True
    assert retention_event["retention_id"] == "DNA-16-EXP-0001"
    assert retention_event["learning_runtime_used"] is False
    assert retention_event["persistent_memory_runtime_used"] is False

    # DNA-16 must not mutate the earlier Memory Genome or DNA-09 wall.
    assert state["memory_genome"] == pre_memory_genome
    assert state["independent_verification_wall"] == pre_verification_wall

    # Replaying the same qualified unit must not duplicate retention.
    replay = dna16_core.activate(result)
    replay_output = replay["core54_outputs"]["DNA-16"]
    assert replay_output["retained"] is True
    assert replay_output["retained_new"] is False
    assert replay_output["retention_count"] == 1
    assert len(
        replay["cognitive_state"]["experience_driven_learning"]
        ["retained_experiences"]
    ) == 1
    assert replay[
        "cognitive_state"
    ]["experience_driven_learning"]["evaluations"][-1]["status"] == (
        "QUALIFIED_EXPERIENCE_ALREADY_RETAINED"
    )

    # Missing a component must never be retained.
    incomplete_input = deepcopy(through_dna15)
    incomplete_input["experience_learning_unit"] = deepcopy(
        probe["experience_learning_unit"]
    )
    incomplete_input["experience_learning_unit"].pop("verification")
    incomplete = dna16_core.activate(incomplete_input)
    incomplete_output = incomplete["core54_outputs"]["DNA-16"]
    assert incomplete_output["experience_complete"] is False
    assert incomplete_output["sufficiently_qualified"] is False
    assert incomplete_output["missing_components"] == ["verification"]
    assert incomplete_output["retained"] is False
    assert incomplete_output["retention_count"] == 0

    # A failed verifier result must never be retained.
    failed_input = deepcopy(through_dna15)
    failed_input["experience_learning_unit"] = deepcopy(
        probe["experience_learning_unit"]
    )
    failed_input["experience_learning_unit"]["verification"][
        "passed"
    ] = False
    failed = dna16_core.activate(failed_input)
    failed_output = failed["core54_outputs"]["DNA-16"]
    assert failed_output["experience_complete"] is True
    assert failed_output["sufficiently_qualified"] is False
    assert "VERIFIER_PASS_REQUIRED" in failed_output["rejection_reasons"]
    assert failed_output["retained"] is False
    assert failed_output["retention_count"] == 0

    # Learner and verifier must remain separated.
    self_verified_input = deepcopy(through_dna15)
    self_verified_input["experience_learning_unit"] = deepcopy(
        probe["experience_learning_unit"]
    )
    self_verified_input["experience_learning_unit"]["verification"][
        "verifier_id"
    ] = "LEARNER-DNA16"
    self_verified = dna16_core.activate(self_verified_input)
    self_verified_output = self_verified["core54_outputs"]["DNA-16"]
    assert self_verified_output["sufficiently_qualified"] is False
    assert "LEARNER_VERIFIER_NOT_SEPARATED" in (
        self_verified_output["rejection_reasons"]
    )
    assert self_verified_output["retained"] is False

    # Verification must bind to the exact four-part candidate.
    wrong_binding_input = deepcopy(through_dna15)
    wrong_binding_input["experience_learning_unit"] = deepcopy(
        probe["experience_learning_unit"]
    )
    wrong_binding_input["experience_learning_unit"]["verification"][
        "candidate_sha256"
    ] = "WRONG-CANDIDATE-HASH"
    wrong_binding = dna16_core.activate(wrong_binding_input)
    wrong_binding_output = wrong_binding["core54_outputs"]["DNA-16"]
    assert wrong_binding_output["sufficiently_qualified"] is False
    assert "VERIFICATION_NOT_BOUND_TO_LEARNING_UNIT" in (
        wrong_binding_output["rejection_reasons"]
    )
    assert wrong_binding_output["retained"] is False

    # No supplied learning unit means no retention.
    absent_input = deepcopy(through_dna15)
    absent_input.pop("experience_learning_unit", None)
    absent = dna16_core.activate(absent_input)
    absent_output = absent["core54_outputs"]["DNA-16"]
    assert absent_output["experience_complete"] is False
    assert absent_output["sufficiently_qualified"] is False
    assert absent_output["retained"] is False
    assert absent_output["retention_count"] == 0

    # Reject provisional root marker behavior as the official contract.
    assert "experience_complete" not in result
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result

    locks = {
        "auto_learning": bool(core54.auto_learning_enabled),
        "model_calls": bool(core54.model_calls_enabled),
        "external_execution": bool(core54.external_execution_enabled),
        "canon_write": bool(core54.canon_write_enabled),
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
        "core_id": "DNA-16",
        "canon_mapping": "PASS",
        "learning_unit_components": "PASS",
        "sufficient_experience_gate": "PASS",
        "qualified_retention": "PASS",
        "unqualified_retention": False,
        "independent_verification_binding": "PASS",
        "learning_runtime_used": False,
        "persistent_memory_runtime_used": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS" if verify_canon_file else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-17"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    required_gene_files = [
        GENES_ROOT / "SIGMA_DNA_01_PURPOSE_EXISTENCE.py",
        GENES_ROOT / "SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE.py",
        GENES_ROOT / "SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE.py",
        GENES_ROOT / "SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS.py",
        GENES_ROOT / "SIGMA_DNA_05_ETHICAL_INTELLIGENCE.py",
        GENES_ROOT / "SIGMA_DNA_06_INTERLAYER_FEEDBACK.py",
        GENES_ROOT / "SIGMA_DNA_07_PERSISTENT_EXISTENCE.py",
        GENES_ROOT / "SIGMA_DNA_08_LEARNING_WORLD.py",
        GENES_ROOT / "SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL.py",
        GENES_ROOT / "SIGMA_DNA_10_MEMORY_GENOME.py",
        GENES_ROOT / "SIGMA_DNA_11_KNOWLEDGE_GRAPH.py",
        GENES_ROOT / "SIGMA_DNA_12_TOOL_INTELLIGENCE.py",
        GENES_ROOT / "SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH.py",
        GENES_ROOT / "SIGMA_DNA_14_PERSISTENCE_ENGINE.py",
        GENES_ROOT / "SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS.py",
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-16_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        from SIGMA_DNA_01_PURPOSE_EXISTENCE import self_check_dna01
        from SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE import (
            self_check_dna02,
        )
        from SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE import self_check_dna03
        from SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS import self_check_dna04
        from SIGMA_DNA_05_ETHICAL_INTELLIGENCE import self_check_dna05
        from SIGMA_DNA_06_INTERLAYER_FEEDBACK import self_check_dna06
        from SIGMA_DNA_07_PERSISTENT_EXISTENCE import self_check_dna07
        from SIGMA_DNA_08_LEARNING_WORLD import self_check_dna08
        from SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL import (
            self_check_dna09,
        )
        from SIGMA_DNA_10_MEMORY_GENOME import self_check_dna10
        from SIGMA_DNA_11_KNOWLEDGE_GRAPH import self_check_dna11
        from SIGMA_DNA_12_TOOL_INTELLIGENCE import self_check_dna12
        from SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH import self_check_dna13
        from SIGMA_DNA_14_PERSISTENCE_ENGINE import self_check_dna14
        from SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS import self_check_dna15
    except Exception as exc:
        print("DNA-16_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(core.state.behavior_bound for core in core54.cores):
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
            ("DNA-14", self_check_dna14),
            ("DNA-15", self_check_dna15),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(core54, verify_canon_file=True)
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna16(core54, verify_canon_file=True)

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != [
            f"DNA-{index:02d}"
            for index in range(1, 17)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-16_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-16_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_16_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "LEARNING_UNIT_COMPONENTS:",
        report["learning_unit_components"],
    )
    print(
        "SUFFICIENT_EXPERIENCE_GATE:",
        report["sufficient_experience_gate"],
    )
    print("QUALIFIED_RETENTION:", report["qualified_retention"])
    print(
        "UNQUALIFIED_RETENTION:",
        report["unqualified_retention"],
    )
    print(
        "INDEPENDENT_VERIFICATION_BINDING:",
        report["independent_verification_binding"],
    )
    print("LEARNING_RUNTIME_USED:", report["learning_runtime_used"])
    print(
        "PERSISTENT_MEMORY_RUNTIME_USED:",
        report["persistent_memory_runtime_used"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 16/54")
    print("NEXT_AUTHORIZED: DNA-17")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
