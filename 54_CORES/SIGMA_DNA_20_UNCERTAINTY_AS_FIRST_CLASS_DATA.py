#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-20: UNCERTAINTY AS FIRST-CLASS DATA
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_20_UNCERTAINTY_AS_FIRST_CLASS_DATA.py
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

CANON_DNA20: Dict[str, str] = {
    "id": "DNA-20",
    "name": "Uncertainty as First-Class Data",
    "purpose": (
        "Mọi kết luận quan trọng mang confidence, evidence coverage "
        "và unresolved uncertainty."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
UNCERTAINTY_FIRST_CLASS_SCHEMA = (
    "SIGMA_UNCERTAINTY_FIRST_CLASS_DATA_V1"
)

IMPORTANT_CONCLUSION_FIELDS = [
    "conclusion_id",
    "conclusion",
    "confidence",
    "evidence_coverage",
    "unresolved_uncertainty",
]

UNCERTAINTY_FIRST_CLASS_CONTRACT: Dict[str, Any] = {
    "schema": UNCERTAINTY_FIRST_CLASS_SCHEMA,
    "important_conclusion_input_path": "important_conclusions",
    "state_path": (
        "cognitive_state.uncertainty.first_class_data"
    ),
    "required_fields": deepcopy(
        IMPORTANT_CONCLUSION_FIELDS
    ),
    "canon_required_data": [
        "confidence",
        "evidence_coverage",
        "unresolved_uncertainty",
    ],
    "numeric_encoding": {
        "confidence": {
            "minimum": 0.0,
            "maximum": 1.0,
        },
        "evidence_coverage": {
            "minimum": 0.0,
            "maximum": 1.0,
        },
        "canon_status": (
            "IMPLEMENTATION_ENCODING_NOT_CANON_FIELD"
        ),
    },
    "unresolved_uncertainty_encoding": "LIST",
    "missing_data_is_not_invented": True,
    "incomplete_records_remain_visible": True,
    "confidence_equals_truth": False,
    "evidence_coverage_equals_truth": False,
    "empty_unresolved_uncertainty_equals_truth": False,
    "truth_established_by_dna20": False,
    "knowledge_promoted_by_dna20": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA03_STATE_BINDING"
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


def _valid_probability(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and 0.0 <= float(value) <= 1.0
    )


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA20:
        raise RuntimeError(
            "DNA-20_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA20,
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
            "DNA-20_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    uncertainty = state.get("uncertainty")
    if not isinstance(uncertainty, dict):
        raise TypeError(
            "context['cognitive_state']['uncertainty'] "
            "must be a dict"
        )

    return state, uncertainty


def _install_first_class_uncertainty(
    uncertainty: Dict[str, Any],
) -> Dict[str, Any]:
    existing = uncertainty.get("first_class_data")

    expected = {
        "contract": deepcopy(
            UNCERTAINTY_FIRST_CLASS_CONTRACT
        ),
        "records": [],
        "batches": [],
    }

    if existing is None:
        uncertainty["first_class_data"] = expected
        return uncertainty["first_class_data"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['uncertainty']"
            "['first_class_data'] must be a dict"
        )

    if existing.get("contract") != (
        UNCERTAINTY_FIRST_CLASS_CONTRACT
    ):
        raise ValueError(
            "DNA-20_UNCERTAINTY_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("records"), list):
        raise TypeError(
            "first_class_data['records'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "first_class_data['batches'] must be a list"
        )

    return existing


def _validate_record_types(
    supplied: Dict[str, Any],
) -> None:
    if (
        "conclusion_id" in supplied
        and not isinstance(
            supplied["conclusion_id"],
            str,
        )
    ):
        raise TypeError(
            "important_conclusion['conclusion_id'] "
            "must be a string"
        )

    for field in (
        "confidence",
        "evidence_coverage",
    ):
        if field in supplied and (
            not isinstance(supplied[field], (int, float))
            or isinstance(supplied[field], bool)
        ):
            raise TypeError(
                f"important_conclusion['{field}'] "
                "must be numeric"
            )

    if (
        "unresolved_uncertainty" in supplied
        and not isinstance(
            supplied["unresolved_uncertainty"],
            list,
        )
    ):
        raise TypeError(
            "important_conclusion"
            "['unresolved_uncertainty'] must be a list"
        )


def _normalize_important_conclusion(
    supplied: Any,
    *,
    input_index: int,
    sequence: int,
) -> Dict[str, Any]:
    errors: List[str] = []

    if not isinstance(supplied, dict):
        return {
            "sequence": sequence,
            "record_id": (
                f"DNA-20-UNCERTAINTY-{sequence:04d}"
            ),
            "input_index": input_index,
            "conclusion_id": None,
            "conclusion": None,
            "conclusion_sha256": None,
            "confidence": None,
            "evidence_coverage": None,
            "unresolved_uncertainty": None,
            "unresolved_uncertainty_count": None,
            "complete": False,
            "errors": [
                "IMPORTANT_CONCLUSION_MUST_BE_A_DICT"
            ],
            "truth_established": False,
            "knowledge_promoted": False,
            "status": (
                "IMPORTANT_CONCLUSION_DATA_INCOMPLETE"
            ),
        }

    record = deepcopy(supplied)
    _validate_record_types(record)

    missing = [
        field
        for field in IMPORTANT_CONCLUSION_FIELDS
        if field not in record
    ]
    if missing:
        errors.append(
            "IMPORTANT_CONCLUSION_FIELDS_MISSING"
        )

    conclusion_id = record.get("conclusion_id")
    if not _non_empty_text(conclusion_id):
        errors.append("CONCLUSION_ID_REQUIRED")

    conclusion_present = (
        "conclusion" in record
        and record.get("conclusion") is not None
    )
    if not conclusion_present:
        errors.append("CONCLUSION_REQUIRED")

    confidence = record.get("confidence")
    if "confidence" not in record:
        errors.append("CONFIDENCE_REQUIRED")
    elif not _valid_probability(confidence):
        raise ValueError(
            "DNA-20_CONFIDENCE_OUT_OF_RANGE"
        )

    evidence_coverage = record.get(
        "evidence_coverage"
    )
    if "evidence_coverage" not in record:
        errors.append("EVIDENCE_COVERAGE_REQUIRED")
    elif not _valid_probability(evidence_coverage):
        raise ValueError(
            "DNA-20_EVIDENCE_COVERAGE_OUT_OF_RANGE"
        )

    unresolved = record.get(
        "unresolved_uncertainty"
    )
    if "unresolved_uncertainty" not in record:
        errors.append(
            "UNRESOLVED_UNCERTAINTY_REQUIRED"
        )

    unique_errors = list(dict.fromkeys(errors))
    complete = not unique_errors

    if not complete:
        uncertainty_status = (
            "IMPORTANT_CONCLUSION_DATA_INCOMPLETE"
        )
    elif unresolved:
        uncertainty_status = (
            "UNRESOLVED_UNCERTAINTY_PRESENT"
        )
    else:
        uncertainty_status = (
            "NO_UNRESOLVED_UNCERTAINTY_DECLARED"
        )

    conclusion = deepcopy(record.get("conclusion"))
    return {
        "sequence": sequence,
        "record_id": (
            f"DNA-20-UNCERTAINTY-{sequence:04d}"
        ),
        "input_index": input_index,
        "conclusion_id": conclusion_id,
        "conclusion": conclusion,
        "conclusion_sha256": (
            _sha256_json(conclusion)
            if conclusion_present
            else None
        ),
        "confidence": (
            float(confidence)
            if "confidence" in record
            else None
        ),
        "evidence_coverage": (
            float(evidence_coverage)
            if "evidence_coverage" in record
            else None
        ),
        "unresolved_uncertainty": (
            deepcopy(unresolved)
            if "unresolved_uncertainty" in record
            else None
        ),
        "unresolved_uncertainty_count": (
            len(unresolved)
            if isinstance(unresolved, list)
            else None
        ),
        "complete": complete,
        "errors": unique_errors,
        "truth_established": False,
        "knowledge_promoted": False,
        "status": uncertainty_status,
    }


def _evaluate_important_conclusions(
    supplied: Any,
    registry: Dict[str, Any],
) -> Dict[str, Any]:
    if supplied is None:
        conclusions: List[Any] = []
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['important_conclusions'] must be a list"
        )
    else:
        conclusions = supplied

    conclusion_ids = [
        item.get("conclusion_id")
        for item in conclusions
        if isinstance(item, dict)
        and _non_empty_text(item.get("conclusion_id"))
    ]
    if len(conclusion_ids) != len(set(conclusion_ids)):
        raise ValueError(
            "DNA-20_DUPLICATE_CONCLUSION_ID"
        )

    start_sequence = len(registry["records"]) + 1
    records = [
        _normalize_important_conclusion(
            item,
            input_index=index,
            sequence=start_sequence + index - 1,
        )
        for index, item in enumerate(
            conclusions,
            start=1,
        )
    ]
    registry["records"].extend(
        deepcopy(records)
    )

    complete_count = sum(
        1 for record in records if record["complete"]
    )
    incomplete_count = len(records) - complete_count
    unresolved_item_count = sum(
        record["unresolved_uncertainty_count"] or 0
        for record in records
        if record["complete"]
    )
    records_with_unresolved_uncertainty = sum(
        1
        for record in records
        if record["complete"]
        and (
            record["unresolved_uncertainty_count"]
            or 0
        )
        > 0
    )

    if not records:
        status = "NO_IMPORTANT_CONCLUSIONS_SUPPLIED"
    elif incomplete_count:
        status = (
            "IMPORTANT_CONCLUSION_UNCERTAINTY_DATA_INCOMPLETE"
        )
    else:
        status = (
            "ALL_IMPORTANT_CONCLUSIONS_CARRY_UNCERTAINTY_DATA"
        )

    batch_sequence = len(registry["batches"]) + 1
    batch = {
        "sequence": batch_sequence,
        "batch_id": (
            f"DNA-20-BATCH-{batch_sequence:04d}"
        ),
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "important_conclusion_count": len(records),
        "complete_count": complete_count,
        "incomplete_count": incomplete_count,
        "records_with_unresolved_uncertainty": (
            records_with_unresolved_uncertainty
        ),
        "unresolved_item_count": unresolved_item_count,
        "all_important_conclusions_complete": (
            incomplete_count == 0
        ),
        "truth_established": False,
        "knowledge_promoted": False,
        "status": status,
    }
    registry["batches"].append(deepcopy(batch))

    return {
        "records": records,
        "batch": batch,
    }


def dna20_uncertainty_as_first_class_data(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Record confidence, evidence coverage, and unresolved uncertainty for
    every supplied important conclusion.

    DNA-20 does not infer missing uncertainty data, establish truth,
    promote knowledge, call a model, start a higher runtime, execute an
    external action, or modify Canon.
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
    trace.append("DNA-20")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, uncertainty = _validate_dependencies(context)
    registry = _install_first_class_uncertainty(
        uncertainty
    )

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-20",
            "operation": (
                "UNCERTAINTY_FIRST_CLASS_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "uncertainty_schema": (
                UNCERTAINTY_FIRST_CLASS_SCHEMA
            ),
            "required_data": [
                "confidence",
                "evidence_coverage",
                "unresolved_uncertainty",
            ],
            "truth_established": False,
        }
    )

    evaluation = _evaluate_important_conclusions(
        context.get("important_conclusions"),
        registry,
    )
    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-20",
            "operation": (
                "IMPORTANT_CONCLUSION_UNCERTAINTY_RECORDED"
            ),
            "canonical_sha256": canonical_sha256,
            "batch_id": batch["batch_id"],
            "important_conclusion_count": (
                batch["important_conclusion_count"]
            ),
            "complete_count": batch["complete_count"],
            "incomplete_count": batch["incomplete_count"],
            "unresolved_item_count": (
                batch["unresolved_item_count"]
            ),
            "truth_established": False,
            "knowledge_promoted": False,
        }
    )

    outputs["DNA-20"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "uncertainty_first_class_contract": deepcopy(
            UNCERTAINTY_FIRST_CLASS_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "important_conclusion_count": (
            batch["important_conclusion_count"]
        ),
        "complete_count": batch["complete_count"],
        "incomplete_count": batch["incomplete_count"],
        "all_important_conclusions_complete": (
            batch["all_important_conclusions_complete"]
        ),
        "truth_established": False,
        "knowledge_promoted": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna20(core54: Core54Like) -> None:
    core = core54.get("DNA-20")
    assert_exact_canon(core)
    core54.bind(
        "DNA-20",
        dna20_uncertainty_as_first_class_data,
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


def _complete_through_dna19(
    core54: Core54Like,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    from SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING import (
        _complete_probe as dna16_complete_probe,
    )
    from SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING import (
        _valid_persistent_capability_change,
    )
    from SIGMA_DNA_18_MODEL_EVOLUTION import (
        _valid_model_evolution_candidate,
    )
    from SIGMA_DNA_19_MULTI_MODEL_INTELLIGENCE import (
        _five_role_contributions,
    )

    probe = dna16_complete_probe(core54)
    probe["persistent_capability_change"] = (
        _valid_persistent_capability_change()
    )

    through_dna17 = _run_through(
        core54,
        probe,
        17,
    )
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

    through_dna18["multi_model_contributions"] = (
        _five_role_contributions(claim)
    )
    through_dna19 = core54.get("DNA-19").activate(
        through_dna18
    )

    return through_dna19, claim


def self_check_dna20(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 20):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna20_core = core54.get("DNA-20")
    assert_exact_canon(dna20_core)
    bind_dna20(core54)

    through_dna19, claim = _complete_through_dna19(
        core54
    )
    through_dna19_snapshot = deepcopy(through_dna19)

    pre_multi_model = deepcopy(
        through_dna19["cognitive_state"][
            "multi_model_intelligence"
        ]
    )
    pre_provenance_count = len(
        through_dna19["cognitive_state"][
            "provenance"
        ]
    )

    important_conclusion = {
        "conclusion_id": "DNA20-CONCLUSION-01",
        "conclusion": deepcopy(claim),
        "confidence": 0.84,
        "evidence_coverage": 0.75,
        "unresolved_uncertainty": [
            "CONSENSUS_DOES_NOT_ESTABLISH_TRUTH",
            "REALITY_GROUNDING_NOT_YET_EXECUTED",
        ],
    }
    valid_input = deepcopy(through_dna19)
    valid_input["important_conclusions"] = [
        important_conclusion
    ]
    result = dna20_core.activate(valid_input)

    assert through_dna19 == through_dna19_snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 21)
    ]

    dna20 = result["core54_outputs"]["DNA-20"]
    assert dna20["canonical_gene"] == CANON_DNA20
    assert dna20["uncertainty_first_class_contract"] == (
        UNCERTAINTY_FIRST_CLASS_CONTRACT
    )
    assert dna20["important_conclusion_count"] == 1
    assert dna20["complete_count"] == 1
    assert dna20["incomplete_count"] == 0
    assert (
        dna20["all_important_conclusions_complete"]
        is True
    )
    assert dna20["truth_established"] is False
    assert dna20["knowledge_promoted"] is False
    assert dna20["status"] == "CANON_ALIGNED"

    evaluation = dna20["evaluation"]
    batch = evaluation["batch"]
    records = evaluation["records"]
    assert len(records) == 1
    record = records[0]

    assert record["record_id"] == (
        "DNA-20-UNCERTAINTY-0001"
    )
    assert record["conclusion_id"] == (
        "DNA20-CONCLUSION-01"
    )
    assert record["conclusion"] == claim
    assert record["confidence"] == 0.84
    assert record["evidence_coverage"] == 0.75
    assert record["unresolved_uncertainty"] == [
        "CONSENSUS_DOES_NOT_ESTABLISH_TRUTH",
        "REALITY_GROUNDING_NOT_YET_EXECUTED",
    ]
    assert record["unresolved_uncertainty_count"] == 2
    assert record["complete"] is True
    assert record["errors"] == []
    assert record["truth_established"] is False
    assert record["knowledge_promoted"] is False
    assert record["status"] == (
        "UNRESOLVED_UNCERTAINTY_PRESENT"
    )

    assert batch["batch_id"] == "DNA-20-BATCH-0001"
    assert batch["record_ids"] == [
        "DNA-20-UNCERTAINTY-0001"
    ]
    assert batch["important_conclusion_count"] == 1
    assert batch["complete_count"] == 1
    assert batch["incomplete_count"] == 0
    assert batch["records_with_unresolved_uncertainty"] == 1
    assert batch["unresolved_item_count"] == 2
    assert batch["all_important_conclusions_complete"] is True
    assert batch["truth_established"] is False
    assert batch["knowledge_promoted"] is False
    assert batch["status"] == (
        "ALL_IMPORTANT_CONCLUSIONS_CARRY_UNCERTAINTY_DATA"
    )

    state = result["cognitive_state"]
    registry = state["uncertainty"]["first_class_data"]
    assert registry["contract"] == (
        UNCERTAINTY_FIRST_CLASS_CONTRACT
    )
    assert registry["records"] == records
    assert registry["batches"] == [batch]
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-20"
    assert contract_event["operation"] == (
        "UNCERTAINTY_FIRST_CLASS_CONTRACT_ESTABLISHED"
    )
    assert contract_event["required_data"] == [
        "confidence",
        "evidence_coverage",
        "unresolved_uncertainty",
    ]
    assert contract_event["truth_established"] is False

    record_event = state["provenance"][-1]
    assert record_event["core_id"] == "DNA-20"
    assert record_event["operation"] == (
        "IMPORTANT_CONCLUSION_UNCERTAINTY_RECORDED"
    )
    assert record_event["batch_id"] == (
        "DNA-20-BATCH-0001"
    )
    assert record_event["important_conclusion_count"] == 1
    assert record_event["complete_count"] == 1
    assert record_event["incomplete_count"] == 0
    assert record_event["unresolved_item_count"] == 2
    assert record_event["truth_established"] is False
    assert record_event["knowledge_promoted"] is False

    # DNA-20 must not mutate the DNA-19 coordination state.
    assert (
        state["multi_model_intelligence"]
        == pre_multi_model
    )

    # Missing uncertainty data must remain visible and must not be invented.
    incomplete_input = deepcopy(through_dna19)
    incomplete_input["important_conclusions"] = [
        {
            "conclusion_id": "DNA20-INCOMPLETE-01",
            "conclusion": {
                "statement": "INCOMPLETE_CONCLUSION",
            },
            "evidence_coverage": 0.4,
            "unresolved_uncertainty": [
                "CONFIDENCE_NOT_SUPPLIED",
            ],
        }
    ]
    incomplete = dna20_core.activate(incomplete_input)
    incomplete_output = incomplete[
        "core54_outputs"
    ]["DNA-20"]
    incomplete_record = incomplete_output[
        "evaluation"
    ]["records"][0]
    assert incomplete_output["complete_count"] == 0
    assert incomplete_output["incomplete_count"] == 1
    assert (
        incomplete_output[
            "all_important_conclusions_complete"
        ]
        is False
    )
    assert incomplete_record["confidence"] is None
    assert incomplete_record["complete"] is False
    assert "CONFIDENCE_REQUIRED" in (
        incomplete_record["errors"]
    )
    assert incomplete_record["status"] == (
        "IMPORTANT_CONCLUSION_DATA_INCOMPLETE"
    )

    # An empty unresolved-uncertainty list is explicit data, not proof of truth.
    explicit_empty_input = deepcopy(through_dna19)
    explicit_empty_input["important_conclusions"] = [
        {
            "conclusion_id": "DNA20-EMPTY-01",
            "conclusion": {
                "statement": "NO_OPEN_ITEM_DECLARED",
            },
            "confidence": 1.0,
            "evidence_coverage": 1.0,
            "unresolved_uncertainty": [],
        }
    ]
    explicit_empty = dna20_core.activate(
        explicit_empty_input
    )
    explicit_record = explicit_empty[
        "core54_outputs"
    ]["DNA-20"]["evaluation"]["records"][0]
    assert explicit_record["complete"] is True
    assert explicit_record["unresolved_uncertainty"] == []
    assert explicit_record["status"] == (
        "NO_UNRESOLVED_UNCERTAINTY_DECLARED"
    )
    assert explicit_record["truth_established"] is False
    assert explicit_empty[
        "core54_outputs"
    ]["DNA-20"]["truth_established"] is False

    # Confidence and evidence coverage must be calibrated to [0, 1].
    out_of_range_confidence = deepcopy(through_dna19)
    out_of_range_confidence["important_conclusions"] = [
        {
            "conclusion_id": "DNA20-RANGE-01",
            "conclusion": "C",
            "confidence": 1.01,
            "evidence_coverage": 0.5,
            "unresolved_uncertainty": [],
        }
    ]
    try:
        dna20_core.activate(out_of_range_confidence)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-20_CONFIDENCE_OUT_OF_RANGE"
        )
    else:
        raise AssertionError(
            "DNA-20_ACCEPTED_OUT_OF_RANGE_CONFIDENCE"
        )

    out_of_range_coverage = deepcopy(through_dna19)
    out_of_range_coverage["important_conclusions"] = [
        {
            "conclusion_id": "DNA20-RANGE-02",
            "conclusion": "C",
            "confidence": 0.5,
            "evidence_coverage": -0.01,
            "unresolved_uncertainty": [],
        }
    ]
    try:
        dna20_core.activate(out_of_range_coverage)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-20_EVIDENCE_COVERAGE_OUT_OF_RANGE"
        )
    else:
        raise AssertionError(
            "DNA-20_ACCEPTED_OUT_OF_RANGE_EVIDENCE_COVERAGE"
        )

    # Unresolved uncertainty must be explicit structured data.
    wrong_uncertainty_type = deepcopy(through_dna19)
    wrong_uncertainty_type["important_conclusions"] = [
        {
            "conclusion_id": "DNA20-TYPE-01",
            "conclusion": "C",
            "confidence": 0.5,
            "evidence_coverage": 0.5,
            "unresolved_uncertainty": "UNKNOWN",
        }
    ]
    try:
        dna20_core.activate(wrong_uncertainty_type)
    except TypeError as exc:
        assert str(exc) == (
            "important_conclusion"
            "['unresolved_uncertainty'] must be a list"
        )
    else:
        raise AssertionError(
            "DNA-20_ACCEPTED_NON_LIST_UNRESOLVED_UNCERTAINTY"
        )

    # Duplicate identities cannot silently overwrite first-class records.
    duplicate_input = deepcopy(through_dna19)
    duplicate_input["important_conclusions"] = [
        {
            "conclusion_id": "DNA20-DUPLICATE",
            "conclusion": "A",
            "confidence": 0.5,
            "evidence_coverage": 0.5,
            "unresolved_uncertainty": [],
        },
        {
            "conclusion_id": "DNA20-DUPLICATE",
            "conclusion": "B",
            "confidence": 0.5,
            "evidence_coverage": 0.5,
            "unresolved_uncertainty": [],
        },
    ]
    try:
        dna20_core.activate(duplicate_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-20_DUPLICATE_CONCLUSION_ID"
        )
    else:
        raise AssertionError(
            "DNA-20_ACCEPTED_DUPLICATE_CONCLUSION_ID"
        )

    # No supplied important conclusion creates an explicit empty batch.
    no_conclusions = dna20_core.activate(
        deepcopy(through_dna19)
    )
    no_conclusions_batch = no_conclusions[
        "core54_outputs"
    ]["DNA-20"]["evaluation"]["batch"]
    assert no_conclusions_batch[
        "important_conclusion_count"
    ] == 0
    assert no_conclusions_batch["record_ids"] == []
    assert no_conclusions_batch["status"] == (
        "NO_IMPORTANT_CONCLUSIONS_SUPPLIED"
    )
    assert no_conclusions_batch["truth_established"] is False

    # Reject the old provisional marker contract.
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result
    assert "uncertainty_first_class" not in result

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
        "core_id": "DNA-20",
        "canon_mapping": "PASS",
        "confidence_first_class": "PASS",
        "evidence_coverage_first_class": "PASS",
        "unresolved_uncertainty_first_class": "PASS",
        "missing_data_not_invented": "PASS",
        "confidence_not_truth": "PASS",
        "truth_established": False,
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
            "DNA-21"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


PRIOR_MODULE_NAMES: Dict[int, str] = {
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
}


def main() -> int:
    required_gene_files = [
        GENES_ROOT / f"{module_name}.py"
        for module_name in PRIOR_MODULE_NAMES.values()
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
                "DNA-20_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )

        prior_modules = {
            index: importlib.import_module(module_name)
            for index, module_name in (
                PRIOR_MODULE_NAMES.items()
            )
        }
    except Exception as exc:
        print("DNA-20_FAIL: IMPORT_ERROR")
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

        for index in range(1, 20):
            checker = getattr(
                prior_modules[index],
                f"self_check_dna{index:02d}",
            )
            report = checker(
                core54,
                verify_canon_file=True,
            )
            if report["self_check"] != "PASS":
                raise RuntimeError(
                    f"DNA-{index:02d}_NOT_PASS"
                )

        report = self_check_dna20(
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
            for index in range(1, 21)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-20_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-20_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_20_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "CONFIDENCE_FIRST_CLASS:",
        report["confidence_first_class"],
    )
    print(
        "EVIDENCE_COVERAGE_FIRST_CLASS:",
        report["evidence_coverage_first_class"],
    )
    print(
        "UNRESOLVED_UNCERTAINTY_FIRST_CLASS:",
        report[
            "unresolved_uncertainty_first_class"
        ],
    )
    print(
        "MISSING_DATA_NOT_INVENTED:",
        report["missing_data_not_invented"],
    )
    print(
        "CONFIDENCE_NOT_TRUTH:",
        report["confidence_not_truth"],
    )
    print(
        "TRUTH_ESTABLISHED:",
        report["truth_established"],
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
    print("OFFICIAL_BOUND_CORES: 20/54")
    print("NEXT_AUTHORIZED: DNA-21")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
