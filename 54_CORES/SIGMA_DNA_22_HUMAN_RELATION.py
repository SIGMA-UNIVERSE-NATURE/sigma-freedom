#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-22: HUMAN RELATION
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_22_HUMAN_RELATION.py
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

CANON_DNA22: Dict[str, str] = {
    "id": "DNA-22",
    "name": "Human Relation",
    "purpose": (
        "SIGMA làm tăng năng lực và tự chủ con người, không biến "
        "con người thành đối tượng phụ thuộc."
    ),
    "system": "wisdom",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
ETHICAL_INTELLIGENCE_SCHEMA = "SIGMA_ETHICAL_INTELLIGENCE_V1"
HUMAN_RELATION_SCHEMA = "SIGMA_HUMAN_RELATION_V1"

EFFECT_VALUES = [
    "INCREASED",
    "UNCHANGED",
    "DECREASED",
    "UNKNOWN",
]

HUMAN_RELATION_CASE_FIELDS = [
    "case_id",
    "human_id",
    "capability_effect",
    "autonomy_effect",
    "dependence_effect",
    "evidence",
]

HUMAN_RELATION_CONTRACT: Dict[str, Any] = {
    "schema": HUMAN_RELATION_SCHEMA,
    "input_path": "human_relation_cases",
    "required_fields": deepcopy(HUMAN_RELATION_CASE_FIELDS),
    "effect_values": deepcopy(EFFECT_VALUES),
    "canon_alignment_requires": {
        "capability_effect": "INCREASED",
        "autonomy_effect": "INCREASED",
        "dependence_effect": [
            "UNCHANGED",
            "DECREASED",
        ],
    },
    "human_capability_must_increase": True,
    "human_autonomy_must_increase": True,
    "human_dependence_must_not_increase": True,
    "evidence_required_for_assessment": True,
    "evidence_requirement_canon_status": (
        "IMPLEMENTATION_ENCODING_FOR_CHECKABLE_ASSESSMENT"
    ),
    "unknown_effect_is_not_assumed_aligned": True,
    "missing_evidence_is_not_invented": True,
    "human_relation_action_executed_by_dna22": False,
    "human_decision_replaced_by_dna22": False,
    "dependence_created_by_dna22": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "learning_runtime_started": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA05_ETHICAL_BINDING"
    ),
}

PRIOR_GENE_MODULES = {
    1: "SIGMA_DNA_01_PURPOSE_EXISTENCE",
    2: "SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE",
    3: "SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE",
    4: "SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS",
    5: "SIGMA_DNA_05_ETHICAL_INTELLIGENCE",
    6: "SIGMA_DNA_06_INTERLAYER_FEEDBACK",
    7: "SIGMA_DNA_07_PERSISTENT_EXISTENCE",
    8: "SIGMA_DNA_08_LEARNING_WORLD",
    9: "SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL",
    10: "SIGMA_DNA_10_MEMORY_GENOME",
    11: "SIGMA_DNA_11_KNOWLEDGE_GRAPH",
    12: "SIGMA_DNA_12_TOOL_INTELLIGENCE",
    13: "SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH",
    14: "SIGMA_DNA_14_PERSISTENCE_ENGINE",
    15: "SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS",
    16: "SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING",
    17: "SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING",
    18: "SIGMA_DNA_18_MODEL_EVOLUTION",
    19: "SIGMA_DNA_19_MULTI_MODEL_INTELLIGENCE",
    20: "SIGMA_DNA_20_UNCERTAINTY_AS_FIRST_CLASS_DATA",
    21: "SIGMA_DNA_21_TRUTH_PROTOCOL",
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
    if actual != CANON_DNA22:
        raise RuntimeError(
            "DNA-22_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA22,
                    "actual": actual,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-22_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    ethical = state.get("ethical_intelligence")
    if not isinstance(ethical, dict):
        raise RuntimeError(
            "DNA-05_ETHICAL_INTELLIGENCE_REQUIRED"
        )

    if ethical.get("schema") != (
        ETHICAL_INTELLIGENCE_SCHEMA
    ):
        raise ValueError(
            "DNA-22_ETHICAL_INTELLIGENCE_SCHEMA_MISMATCH:"
            f"{ethical.get('schema')!r}"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-05_OUTPUT_REQUIRED")

    dna05_output = outputs.get("DNA-05")
    if not isinstance(dna05_output, dict):
        raise RuntimeError("DNA-05_OUTPUT_REQUIRED")

    return state, ethical


def _install_human_relation_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("human_relation")

    expected = {
        "contract": deepcopy(HUMAN_RELATION_CONTRACT),
        "records": [],
        "batches": [],
    }

    if existing is None:
        state["human_relation"] = expected
        return state["human_relation"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['human_relation'] must be a dict"
        )

    if existing.get("contract") != HUMAN_RELATION_CONTRACT:
        raise ValueError(
            "DNA-22_HUMAN_RELATION_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("records"), list):
        raise TypeError(
            "human_relation['records'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "human_relation['batches'] must be a list"
        )

    return existing


def _normalize_effect(
    value: Any,
    *,
    field: str,
    errors: List[str],
) -> Optional[str]:
    if not isinstance(value, str):
        errors.append(f"{field.upper()}_REQUIRED")
        return None

    normalized = value.strip().upper()
    if normalized not in EFFECT_VALUES:
        raise ValueError(
            f"DNA-22_{field.upper()}_INVALID:{normalized}"
        )
    return normalized


def _normalize_evidence(
    supplied: Any,
    errors: List[str],
) -> List[Any]:
    if not isinstance(supplied, list):
        errors.append("EVIDENCE_LIST_REQUIRED")
        return []

    if not supplied:
        errors.append("EVIDENCE_REQUIRED")
        return []

    if any(item is None for item in supplied):
        raise ValueError("DNA-22_EVIDENCE_ITEM_MUST_NOT_BE_NULL")

    return deepcopy(supplied)


def _incomplete_record(
    *,
    input_index: int,
    sequence: int,
    errors: List[str],
) -> Dict[str, Any]:
    return {
        "sequence": sequence,
        "record_id": f"DNA-22-HUMAN-{sequence:04d}",
        "input_index": input_index,
        "case_id": None,
        "human_id": None,
        "capability_effect": None,
        "autonomy_effect": None,
        "dependence_effect": None,
        "evidence": [],
        "evidence_sha256": None,
        "capability_increased": False,
        "autonomy_increased": False,
        "dependence_not_increased": False,
        "dependence_risk": False,
        "canon_aligned": False,
        "human_capability_increased_by_dna22": False,
        "human_autonomy_increased_by_dna22": False,
        "human_dependence_created_by_dna22": False,
        "external_action_executed": False,
        "errors": list(dict.fromkeys(errors)),
        "status": "HUMAN_RELATION_INPUT_INCOMPLETE",
    }


def _normalize_case(
    supplied: Any,
    *,
    input_index: int,
    sequence: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        return _incomplete_record(
            input_index=input_index,
            sequence=sequence,
            errors=["HUMAN_RELATION_CASE_MUST_BE_A_DICT"],
        )

    case = deepcopy(supplied)
    errors: List[str] = []

    missing = [
        field
        for field in HUMAN_RELATION_CASE_FIELDS
        if field not in case
    ]
    if missing:
        errors.append("HUMAN_RELATION_CASE_FIELDS_MISSING")

    case_id = case.get("case_id")
    if not _non_empty_text(case_id):
        errors.append("CASE_ID_REQUIRED")

    human_id = case.get("human_id")
    if not _non_empty_text(human_id):
        errors.append("HUMAN_ID_REQUIRED")

    capability_effect = _normalize_effect(
        case.get("capability_effect"),
        field="capability_effect",
        errors=errors,
    )
    autonomy_effect = _normalize_effect(
        case.get("autonomy_effect"),
        field="autonomy_effect",
        errors=errors,
    )
    dependence_effect = _normalize_effect(
        case.get("dependence_effect"),
        field="dependence_effect",
        errors=errors,
    )
    evidence = _normalize_evidence(
        case.get("evidence"),
        errors,
    )

    capability_increased = (
        capability_effect == "INCREASED"
    )
    autonomy_increased = autonomy_effect == "INCREASED"
    dependence_not_increased = dependence_effect in {
        "UNCHANGED",
        "DECREASED",
    }
    dependence_risk = dependence_effect == "INCREASED"

    alignment_failures: List[str] = []
    if capability_effect is not None and not capability_increased:
        alignment_failures.append(
            "HUMAN_CAPABILITY_NOT_INCREASED"
        )
    if autonomy_effect is not None and not autonomy_increased:
        alignment_failures.append(
            "HUMAN_AUTONOMY_NOT_INCREASED"
        )
    if dependence_effect is not None and not dependence_not_increased:
        alignment_failures.append(
            "HUMAN_DEPENDENCE_NOT_PREVENTED"
        )

    errors = list(dict.fromkeys(errors))
    canon_aligned = bool(
        not errors
        and capability_increased
        and autonomy_increased
        and dependence_not_increased
    )

    if errors:
        status = "HUMAN_RELATION_INPUT_INCOMPLETE"
    elif dependence_risk:
        status = "HUMAN_DEPENDENCE_RISK_DETECTED"
    elif canon_aligned:
        status = "HUMAN_RELATION_CANON_ALIGNED"
    else:
        status = "HUMAN_RELATION_NOT_CANON_ALIGNED"

    return {
        "sequence": sequence,
        "record_id": f"DNA-22-HUMAN-{sequence:04d}",
        "input_index": input_index,
        "case_id": case_id,
        "human_id": human_id,
        "capability_effect": capability_effect,
        "autonomy_effect": autonomy_effect,
        "dependence_effect": dependence_effect,
        "evidence": evidence,
        "evidence_sha256": (
            _sha256_json(evidence)
            if evidence
            else None
        ),
        "evidence_status": (
            "SUPPLIED_NOT_INDEPENDENTLY_VERIFIED_BY_DNA22"
            if evidence
            else "MISSING"
        ),
        "capability_increased": capability_increased,
        "autonomy_increased": autonomy_increased,
        "dependence_not_increased": dependence_not_increased,
        "dependence_risk": dependence_risk,
        "alignment_failures": alignment_failures,
        "canon_aligned": canon_aligned,
        "human_capability_increased_by_dna22": False,
        "human_autonomy_increased_by_dna22": False,
        "human_dependence_created_by_dna22": False,
        "external_action_executed": False,
        "errors": errors,
        "status": status,
    }


def _evaluate_human_relation_cases(
    supplied: Any,
    registry: Dict[str, Any],
) -> Dict[str, Any]:
    if supplied is None:
        cases: List[Any] = []
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['human_relation_cases'] must be a list"
        )
    else:
        cases = supplied

    case_ids = [
        item.get("case_id")
        for item in cases
        if isinstance(item, dict)
        and _non_empty_text(item.get("case_id"))
    ]
    if len(case_ids) != len(set(case_ids)):
        raise ValueError(
            "DNA-22_DUPLICATE_HUMAN_RELATION_CASE_ID"
        )

    start_sequence = len(registry["records"]) + 1
    records = [
        _normalize_case(
            item,
            input_index=index,
            sequence=start_sequence + index - 1,
        )
        for index, item in enumerate(cases, start=1)
    ]
    registry["records"].extend(deepcopy(records))

    aligned_count = sum(
        1
        for record in records
        if record["canon_aligned"]
    )
    dependence_risk_count = sum(
        1
        for record in records
        if record["dependence_risk"]
    )
    incomplete_count = sum(
        1
        for record in records
        if record["errors"]
    )
    not_aligned_count = len(records) - aligned_count

    if not records:
        status = "NO_HUMAN_RELATION_CASES_SUPPLIED"
    elif aligned_count == len(records):
        status = "ALL_HUMAN_RELATION_CASES_CANON_ALIGNED"
    elif dependence_risk_count:
        status = "HUMAN_RELATION_BATCH_HAS_DEPENDENCE_RISK"
    else:
        status = "HUMAN_RELATION_BATCH_NOT_FULLY_ALIGNED"

    batch_sequence = len(registry["batches"]) + 1
    batch = {
        "sequence": batch_sequence,
        "batch_id": f"DNA-22-BATCH-{batch_sequence:04d}",
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "case_count": len(records),
        "aligned_count": aligned_count,
        "not_aligned_count": not_aligned_count,
        "dependence_risk_count": dependence_risk_count,
        "incomplete_count": incomplete_count,
        "all_cases_canon_aligned": bool(
            records and aligned_count == len(records)
        ),
        "human_capability_increased_by_dna22": False,
        "human_autonomy_increased_by_dna22": False,
        "human_dependence_created_by_dna22": False,
        "external_action_executed": False,
        "status": status,
    }
    registry["batches"].append(deepcopy(batch))

    return {
        "records": records,
        "batch": batch,
    }


def dna22_human_relation(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Evaluate whether supplied human-relation evidence indicates that SIGMA
    increases human capability and autonomy without increasing dependence.

    DNA-22 evaluates supplied cases only. It does not act on a human,
    replace human decisions, create dependence, invoke a model, start a
    higher runtime, or modify Canon.
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
    trace.append("DNA-22")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, _ethical = _validate_dependencies(context)
    registry = _install_human_relation_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-22",
            "operation": "HUMAN_RELATION_CONTRACT_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "human_relation_schema": HUMAN_RELATION_SCHEMA,
            "capability_must_increase": True,
            "autonomy_must_increase": True,
            "dependence_must_not_increase": True,
            "external_action_executed": False,
        }
    )

    evaluation = _evaluate_human_relation_cases(
        context.get("human_relation_cases"),
        registry,
    )
    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-22",
            "operation": "HUMAN_RELATION_ALIGNMENT_EVALUATED",
            "canonical_sha256": canonical_sha256,
            "batch_id": batch["batch_id"],
            "case_count": batch["case_count"],
            "aligned_count": batch["aligned_count"],
            "dependence_risk_count": (
                batch["dependence_risk_count"]
            ),
            "all_cases_canon_aligned": (
                batch["all_cases_canon_aligned"]
            ),
            "human_capability_increased_by_dna22": False,
            "human_autonomy_increased_by_dna22": False,
            "human_dependence_created_by_dna22": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-22"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "human_relation_contract": deepcopy(
            HUMAN_RELATION_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "case_count": batch["case_count"],
        "aligned_count": batch["aligned_count"],
        "not_aligned_count": batch["not_aligned_count"],
        "dependence_risk_count": (
            batch["dependence_risk_count"]
        ),
        "all_cases_canon_aligned": (
            batch["all_cases_canon_aligned"]
        ),
        "human_capability_increased_by_dna22": False,
        "human_autonomy_increased_by_dna22": False,
        "human_dependence_created_by_dna22": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna22(core54: Core54Like) -> None:
    core = core54.get("DNA-22")
    assert_exact_canon(core)
    core54.bind(
        "DNA-22",
        dna22_human_relation,
    )


def _through_dna21(core54: Core54Like) -> Dict[str, Any]:
    from SIGMA_DNA_21_TRUTH_PROTOCOL import (
        _through_dna20,
    )

    through_dna20 = _through_dna20(
        core54,
        conclusion_id="DNA22-SEED-CONCLUSION",
        conclusion={
            "statement": "HUMAN_RELATION_ASSESSMENT_REQUIRES_EVIDENCE",
        },
        confidence=0.75,
        evidence_coverage=0.50,
        unresolved_uncertainty=[
            "HUMAN_IMPACT_NOT_YET_ASSESSED",
        ],
    )
    return core54.get("DNA-21").activate(
        through_dna20
    )


def self_check_dna22(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 22):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna22_core = core54.get("DNA-22")
    assert_exact_canon(dna22_core)
    bind_dna22(core54)

    through_dna21 = _through_dna21(core54)
    through_dna21_snapshot = deepcopy(through_dna21)

    pre_ethical = deepcopy(
        through_dna21["cognitive_state"][
            "ethical_intelligence"
        ]
    )
    pre_truth_protocol = deepcopy(
        through_dna21["cognitive_state"][
            "truth_protocol"
        ]
    )
    pre_provenance_count = len(
        through_dna21["cognitive_state"]["provenance"]
    )

    valid_case = {
        "case_id": "DNA22-CASE-01",
        "human_id": "HUMAN-01",
        "capability_effect": "INCREASED",
        "autonomy_effect": "INCREASED",
        "dependence_effect": "DECREASED",
        "evidence": [
            {
                "evidence_id": "DNA22-EVIDENCE-01",
                "observation": (
                    "HUMAN_COMPLETED_TASK_WITHOUT_SIGMA_ASSISTANCE"
                ),
            },
            {
                "evidence_id": "DNA22-EVIDENCE-02",
                "observation": (
                    "HUMAN_RETAINED_FINAL_DECISION_AUTHORITY"
                ),
            },
        ],
    }

    valid_input = deepcopy(through_dna21)
    valid_input["human_relation_cases"] = [valid_case]
    result = dna22_core.activate(valid_input)

    assert through_dna21 == through_dna21_snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 23)
    ]

    dna22 = result["core54_outputs"]["DNA-22"]
    assert dna22["canonical_gene"] == CANON_DNA22
    assert dna22["human_relation_contract"] == (
        HUMAN_RELATION_CONTRACT
    )
    assert dna22["case_count"] == 1
    assert dna22["aligned_count"] == 1
    assert dna22["not_aligned_count"] == 0
    assert dna22["dependence_risk_count"] == 0
    assert dna22["all_cases_canon_aligned"] is True
    assert dna22["human_capability_increased_by_dna22"] is False
    assert dna22["human_autonomy_increased_by_dna22"] is False
    assert dna22["human_dependence_created_by_dna22"] is False
    assert dna22["external_action_executed"] is False
    assert dna22["status"] == "CANON_ALIGNED"

    evaluation = dna22["evaluation"]
    records = evaluation["records"]
    batch = evaluation["batch"]
    assert len(records) == 1
    record = records[0]

    assert record["record_id"] == "DNA-22-HUMAN-0001"
    assert record["case_id"] == "DNA22-CASE-01"
    assert record["human_id"] == "HUMAN-01"
    assert record["capability_effect"] == "INCREASED"
    assert record["autonomy_effect"] == "INCREASED"
    assert record["dependence_effect"] == "DECREASED"
    assert record["capability_increased"] is True
    assert record["autonomy_increased"] is True
    assert record["dependence_not_increased"] is True
    assert record["dependence_risk"] is False
    assert record["alignment_failures"] == []
    assert record["canon_aligned"] is True
    assert record["errors"] == []
    assert record["status"] == "HUMAN_RELATION_CANON_ALIGNED"

    assert batch["batch_id"] == "DNA-22-BATCH-0001"
    assert batch["case_count"] == 1
    assert batch["aligned_count"] == 1
    assert batch["not_aligned_count"] == 0
    assert batch["dependence_risk_count"] == 0
    assert batch["incomplete_count"] == 0
    assert batch["all_cases_canon_aligned"] is True
    assert batch["status"] == (
        "ALL_HUMAN_RELATION_CASES_CANON_ALIGNED"
    )

    state = result["cognitive_state"]
    human_relation = state["human_relation"]
    assert human_relation["contract"] == HUMAN_RELATION_CONTRACT
    assert human_relation["records"] == records
    assert human_relation["batches"] == [batch]
    assert len(state["provenance"]) == pre_provenance_count + 2

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-22"
    assert contract_event["operation"] == (
        "HUMAN_RELATION_CONTRACT_ESTABLISHED"
    )
    assert contract_event["capability_must_increase"] is True
    assert contract_event["autonomy_must_increase"] is True
    assert contract_event["dependence_must_not_increase"] is True
    assert contract_event["external_action_executed"] is False

    evaluation_event = state["provenance"][-1]
    assert evaluation_event["core_id"] == "DNA-22"
    assert evaluation_event["operation"] == (
        "HUMAN_RELATION_ALIGNMENT_EVALUATED"
    )
    assert evaluation_event["case_count"] == 1
    assert evaluation_event["aligned_count"] == 1
    assert evaluation_event["dependence_risk_count"] == 0
    assert evaluation_event["all_cases_canon_aligned"] is True

    assert state["ethical_intelligence"] == pre_ethical
    assert state["truth_protocol"] == pre_truth_protocol

    dependence_input = deepcopy(through_dna21)
    dependence_input["human_relation_cases"] = [
        {
            **deepcopy(valid_case),
            "case_id": "DNA22-CASE-DEPENDENCE",
            "dependence_effect": "INCREASED",
        }
    ]
    dependence = dna22_core.activate(dependence_input)
    dependence_record = dependence[
        "core54_outputs"
    ]["DNA-22"]["evaluation"]["records"][0]
    assert dependence_record["dependence_risk"] is True
    assert dependence_record["canon_aligned"] is False
    assert "HUMAN_DEPENDENCE_NOT_PREVENTED" in (
        dependence_record["alignment_failures"]
    )
    assert dependence_record["status"] == (
        "HUMAN_DEPENDENCE_RISK_DETECTED"
    )

    autonomy_input = deepcopy(through_dna21)
    autonomy_input["human_relation_cases"] = [
        {
            **deepcopy(valid_case),
            "case_id": "DNA22-CASE-AUTONOMY",
            "autonomy_effect": "UNCHANGED",
        }
    ]
    autonomy = dna22_core.activate(autonomy_input)
    autonomy_record = autonomy[
        "core54_outputs"
    ]["DNA-22"]["evaluation"]["records"][0]
    assert autonomy_record["canon_aligned"] is False
    assert "HUMAN_AUTONOMY_NOT_INCREASED" in (
        autonomy_record["alignment_failures"]
    )

    capability_input = deepcopy(through_dna21)
    capability_input["human_relation_cases"] = [
        {
            **deepcopy(valid_case),
            "case_id": "DNA22-CASE-CAPABILITY",
            "capability_effect": "DECREASED",
        }
    ]
    capability = dna22_core.activate(capability_input)
    capability_record = capability[
        "core54_outputs"
    ]["DNA-22"]["evaluation"]["records"][0]
    assert capability_record["canon_aligned"] is False
    assert "HUMAN_CAPABILITY_NOT_INCREASED" in (
        capability_record["alignment_failures"]
    )

    evidence_input = deepcopy(through_dna21)
    evidence_input["human_relation_cases"] = [
        {
            **deepcopy(valid_case),
            "case_id": "DNA22-CASE-NO-EVIDENCE",
            "evidence": [],
        }
    ]
    evidence = dna22_core.activate(evidence_input)
    evidence_record = evidence[
        "core54_outputs"
    ]["DNA-22"]["evaluation"]["records"][0]
    assert evidence_record["canon_aligned"] is False
    assert "EVIDENCE_REQUIRED" in evidence_record["errors"]
    assert evidence_record["status"] == (
        "HUMAN_RELATION_INPUT_INCOMPLETE"
    )

    unknown_input = deepcopy(through_dna21)
    unknown_input["human_relation_cases"] = [
        {
            **deepcopy(valid_case),
            "case_id": "DNA22-CASE-UNKNOWN",
            "capability_effect": "UNKNOWN",
        }
    ]
    unknown = dna22_core.activate(unknown_input)
    unknown_record = unknown[
        "core54_outputs"
    ]["DNA-22"]["evaluation"]["records"][0]
    assert unknown_record["canon_aligned"] is False
    assert unknown_record["status"] == (
        "HUMAN_RELATION_NOT_CANON_ALIGNED"
    )

    duplicate_input = deepcopy(through_dna21)
    duplicate_input["human_relation_cases"] = [
        deepcopy(valid_case),
        deepcopy(valid_case),
    ]
    try:
        dna22_core.activate(duplicate_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-22_DUPLICATE_HUMAN_RELATION_CASE_ID"
        )
    else:
        raise AssertionError(
            "DNA-22_ACCEPTED_DUPLICATE_CASE_ID"
        )

    # Reject provisional root-marker behavior as the official contract.
    assert "human_relation_aligned" not in result
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
        "core_id": "DNA-22",
        "canon_mapping": "PASS",
        "human_capability_rule": "PASS",
        "human_autonomy_rule": "PASS",
        "anti_dependence_rule": "PASS",
        "evidence_bound_assessment": "PASS",
        "human_relation_action_executed": False,
        "human_decision_replaced": False,
        "dependence_created_by_dna22": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-23"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def _load_prior_modules() -> Dict[int, Any]:
    return {
        index: importlib.import_module(module_name)
        for index, module_name in PRIOR_GENE_MODULES.items()
    }


def main() -> int:
    required_gene_files = [
        GENES_ROOT / f"{module_name}.py"
        for module_name in PRIOR_GENE_MODULES.values()
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-22_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54

        modules = _load_prior_modules()
    except Exception as exc:
        print("DNA-22_FAIL: IMPORT_ERROR")
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

        for index in range(1, 22):
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

        report = self_check_dna22(
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
            for index in range(1, 23)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-22_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-22_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_22_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "HUMAN_CAPABILITY_RULE:",
        report["human_capability_rule"],
    )
    print(
        "HUMAN_AUTONOMY_RULE:",
        report["human_autonomy_rule"],
    )
    print(
        "ANTI_DEPENDENCE_RULE:",
        report["anti_dependence_rule"],
    )
    print(
        "EVIDENCE_BOUND_ASSESSMENT:",
        report["evidence_bound_assessment"],
    )
    print(
        "HUMAN_RELATION_ACTION_EXECUTED:",
        report["human_relation_action_executed"],
    )
    print(
        "HUMAN_DECISION_REPLACED:",
        report["human_decision_replaced"],
    )
    print(
        "DEPENDENCE_CREATED_BY_DNA22:",
        report["dependence_created_by_dna22"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 22/54")
    print("NEXT_AUTHORIZED: DNA-23")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
