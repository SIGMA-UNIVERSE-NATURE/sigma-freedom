#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-25: SELF-IMPROVEMENT
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_25_SELF_IMPROVEMENT.py
"""

from __future__ import annotations

import hashlib
import importlib
import json
import math
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

CANON_DNA25: Dict[str, str] = {
    "id": "DNA-25",
    "name": "Self-Improvement",
    "purpose": (
        "Mọi cải tiến phải có before→change→test→after; "
        "không tuyên bố tự nâng cấp nếu không đo được."
    ),
    "system": "evolution",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
TRUTH_PROTOCOL_SCHEMA = "SIGMA_TRUTH_PROTOCOL_V1"
ETHICAL_PERSISTENCE_SCHEMA = "SIGMA_ETHICAL_PERSISTENCE_V1"
SELF_IMPROVEMENT_SCHEMA = "SIGMA_SELF_IMPROVEMENT_V1"

IMPROVEMENT_DIRECTIONS = [
    "INCREASE",
    "DECREASE",
    "TARGET",
]

MEASUREMENT_FIELDS = [
    "metric",
    "value",
    "unit",
    "method",
    "evidence",
]

CHANGE_FIELDS = [
    "change_id",
    "description",
    "evidence",
]

TEST_FIELDS = [
    "test_id",
    "method",
    "passed",
    "evidence",
]

SELF_IMPROVEMENT_CASE_FIELDS = [
    "case_id",
    "target",
    "direction",
    "before",
    "change",
    "test",
    "after",
    "self_upgrade_claimed",
]

STAGE_ORDER = [
    "BEFORE",
    "CHANGE",
    "TEST",
    "AFTER",
]

SELF_IMPROVEMENT_CONTRACT: Dict[str, Any] = {
    "schema": SELF_IMPROVEMENT_SCHEMA,
    "input_path": "self_improvement_cases",
    "required_case_fields": deepcopy(
        SELF_IMPROVEMENT_CASE_FIELDS
    ),
    "required_stage_order": deepcopy(STAGE_ORDER),
    "measurement_fields": deepcopy(MEASUREMENT_FIELDS),
    "change_fields": deepcopy(CHANGE_FIELDS),
    "test_fields": deepcopy(TEST_FIELDS),
    "supported_directions": deepcopy(IMPROVEMENT_DIRECTIONS),
    "measurable_before_after_required": True,
    "before_after_comparability_requires": [
        "SAME_METRIC",
        "SAME_UNIT",
        "SAME_METHOD",
        "FINITE_NUMERIC_VALUES",
    ],
    "test_pass_required_for_improvement_claim": True,
    "measured_improvement_required_for_self_upgrade_claim": True,
    "unsupported_self_upgrade_claim_allowed": False,
    "missing_evidence_is_not_invented": True,
    "change_executed_by_dna25": False,
    "test_executed_by_dna25": False,
    "self_upgrade_applied_by_dna25": False,
    "benchmark_executed_by_dna25": False,
    "learning_runtime_started": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA21_TRUTH_"
        "AND_DNA24_ETHICAL_PERSISTENCE_BINDING"
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
    22: "SIGMA_DNA_22_HUMAN_RELATION",
    23: "SIGMA_DNA_23_COGNITIVE_FREEDOM",
    24: "SIGMA_DNA_24_ETHICAL_PERSISTENCE",
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


def _non_empty_list(value: Any) -> bool:
    return isinstance(value, list) and len(value) > 0


def _finite_number(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA25:
        raise RuntimeError(
            "DNA-25_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA25,
                    "actual": actual,
                },
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
            "DNA-25_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    truth_protocol = state.get("truth_protocol")
    if not isinstance(truth_protocol, dict):
        raise RuntimeError("DNA-21_TRUTH_PROTOCOL_REQUIRED")

    truth_contract = truth_protocol.get("contract")
    if not isinstance(truth_contract, dict):
        raise RuntimeError(
            "DNA-21_TRUTH_PROTOCOL_CONTRACT_REQUIRED"
        )

    if truth_contract.get("schema") != TRUTH_PROTOCOL_SCHEMA:
        raise ValueError(
            "DNA-25_TRUTH_PROTOCOL_SCHEMA_MISMATCH:"
            f"{truth_contract.get('schema')!r}"
        )

    ethical_persistence = state.get("ethical_persistence")
    if not isinstance(ethical_persistence, dict):
        raise RuntimeError(
            "DNA-24_ETHICAL_PERSISTENCE_REQUIRED"
        )

    ethical_contract = ethical_persistence.get("contract")
    if not isinstance(ethical_contract, dict):
        raise RuntimeError(
            "DNA-24_ETHICAL_PERSISTENCE_CONTRACT_REQUIRED"
        )

    if ethical_contract.get("schema") != (
        ETHICAL_PERSISTENCE_SCHEMA
    ):
        raise ValueError(
            "DNA-25_ETHICAL_PERSISTENCE_SCHEMA_MISMATCH:"
            f"{ethical_contract.get('schema')!r}"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-24_OUTPUT_REQUIRED")

    if not isinstance(outputs.get("DNA-24"), dict):
        raise RuntimeError("DNA-24_OUTPUT_REQUIRED")

    return state, truth_protocol, ethical_persistence


def _install_self_improvement_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("self_improvement")

    expected = {
        "contract": deepcopy(SELF_IMPROVEMENT_CONTRACT),
        "records": [],
        "batches": [],
    }

    if existing is None:
        state["self_improvement"] = expected
        return state["self_improvement"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['self_improvement'] must be a dict"
        )

    if existing.get("contract") != SELF_IMPROVEMENT_CONTRACT:
        raise ValueError(
            "DNA-25_SELF_IMPROVEMENT_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("records"), list):
        raise TypeError(
            "self_improvement['records'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "self_improvement['batches'] must be a list"
        )

    return existing


def _normalize_evidence(
    supplied: Any,
    *,
    field_name: str,
    errors: List[str],
) -> List[Any]:
    if not isinstance(supplied, list):
        errors.append(f"{field_name}_EVIDENCE_LIST_REQUIRED")
        return []

    if not supplied:
        errors.append(f"{field_name}_EVIDENCE_REQUIRED")
        return []

    if any(item is None for item in supplied):
        raise ValueError(
            f"DNA-25_{field_name}_EVIDENCE_ITEM_MUST_NOT_BE_NULL"
        )

    return deepcopy(supplied)


def _normalize_measurement(
    supplied: Any,
    *,
    stage: str,
) -> Dict[str, Any]:
    errors: List[str] = []

    if not isinstance(supplied, dict):
        return {
            "stage": stage,
            "metric": None,
            "value": None,
            "unit": None,
            "method": None,
            "evidence": [],
            "evidence_sha256": None,
            "measurement_complete": False,
            "errors": [f"{stage}_MEASUREMENT_DICT_REQUIRED"],
            "status": f"{stage}_MEASUREMENT_INCOMPLETE",
        }

    record = deepcopy(supplied)
    missing = [
        field
        for field in MEASUREMENT_FIELDS
        if field not in record
    ]
    if missing:
        errors.append(f"{stage}_MEASUREMENT_FIELDS_MISSING")

    metric = record.get("metric")
    if not _non_empty_text(metric):
        errors.append(f"{stage}_METRIC_REQUIRED")

    value = record.get("value")
    if not _finite_number(value):
        errors.append(f"{stage}_FINITE_NUMERIC_VALUE_REQUIRED")

    unit = record.get("unit")
    if not _non_empty_text(unit):
        errors.append(f"{stage}_UNIT_REQUIRED")

    method = record.get("method")
    if not _non_empty_text(method):
        errors.append(f"{stage}_MEASUREMENT_METHOD_REQUIRED")

    evidence = _normalize_evidence(
        record.get("evidence"),
        field_name=stage,
        errors=errors,
    )

    errors = list(dict.fromkeys(errors))
    complete = len(errors) == 0

    return {
        "stage": stage,
        "metric": metric,
        "value": value,
        "unit": unit,
        "method": method,
        "evidence": evidence,
        "evidence_sha256": (
            _sha256_json(evidence)
            if evidence
            else None
        ),
        "measurement_complete": complete,
        "errors": errors,
        "status": (
            f"{stage}_MEASURED"
            if complete
            else f"{stage}_MEASUREMENT_INCOMPLETE"
        ),
    }


def _normalize_change(supplied: Any) -> Dict[str, Any]:
    errors: List[str] = []

    if not isinstance(supplied, dict):
        return {
            "change_id": None,
            "description": None,
            "evidence": [],
            "evidence_sha256": None,
            "change_record_complete": False,
            "change_executed_by_dna25": False,
            "errors": ["CHANGE_RECORD_DICT_REQUIRED"],
            "status": "CHANGE_RECORD_INCOMPLETE",
        }

    record = deepcopy(supplied)
    missing = [
        field
        for field in CHANGE_FIELDS
        if field not in record
    ]
    if missing:
        errors.append("CHANGE_FIELDS_MISSING")

    change_id = record.get("change_id")
    if not _non_empty_text(change_id):
        errors.append("CHANGE_ID_REQUIRED")

    description = record.get("description")
    if not _non_empty_text(description):
        errors.append("CHANGE_DESCRIPTION_REQUIRED")

    evidence = _normalize_evidence(
        record.get("evidence"),
        field_name="CHANGE",
        errors=errors,
    )

    errors = list(dict.fromkeys(errors))
    complete = len(errors) == 0

    return {
        "change_id": change_id,
        "description": description,
        "evidence": evidence,
        "evidence_sha256": (
            _sha256_json(evidence)
            if evidence
            else None
        ),
        "change_record_complete": complete,
        "change_executed_by_dna25": False,
        "errors": errors,
        "status": (
            "CHANGE_RECORDED"
            if complete
            else "CHANGE_RECORD_INCOMPLETE"
        ),
    }


def _normalize_test(supplied: Any) -> Dict[str, Any]:
    errors: List[str] = []

    if not isinstance(supplied, dict):
        return {
            "test_id": None,
            "method": None,
            "passed": None,
            "evidence": [],
            "evidence_sha256": None,
            "test_record_complete": False,
            "test_executed_by_dna25": False,
            "errors": ["TEST_RECORD_DICT_REQUIRED"],
            "status": "TEST_RECORD_INCOMPLETE",
        }

    record = deepcopy(supplied)
    missing = [
        field
        for field in TEST_FIELDS
        if field not in record
    ]
    if missing:
        errors.append("TEST_FIELDS_MISSING")

    test_id = record.get("test_id")
    if not _non_empty_text(test_id):
        errors.append("TEST_ID_REQUIRED")

    method = record.get("method")
    if not _non_empty_text(method):
        errors.append("TEST_METHOD_REQUIRED")

    passed = record.get("passed")
    if not isinstance(passed, bool):
        if "passed" in record:
            raise TypeError("test['passed'] must be a bool")
        errors.append("TEST_PASS_STATUS_REQUIRED")
        passed = None

    evidence = _normalize_evidence(
        record.get("evidence"),
        field_name="TEST",
        errors=errors,
    )

    errors = list(dict.fromkeys(errors))
    complete = len(errors) == 0

    return {
        "test_id": test_id,
        "method": method,
        "passed": passed,
        "evidence": evidence,
        "evidence_sha256": (
            _sha256_json(evidence)
            if evidence
            else None
        ),
        "test_record_complete": complete,
        "test_executed_by_dna25": False,
        "errors": errors,
        "status": (
            "TEST_RECORDED_PASS"
            if complete and passed is True
            else (
                "TEST_RECORDED_FAIL"
                if complete and passed is False
                else "TEST_RECORD_INCOMPLETE"
            )
        ),
    }


def _normalize_direction(
    supplied: Any,
    errors: List[str],
) -> Optional[str]:
    if not isinstance(supplied, str):
        errors.append("IMPROVEMENT_DIRECTION_REQUIRED")
        return None

    normalized = supplied.strip().upper()
    if normalized not in IMPROVEMENT_DIRECTIONS:
        raise ValueError(
            f"DNA-25_UNKNOWN_IMPROVEMENT_DIRECTION:{normalized}"
        )
    return normalized


def _measurement_comparability(
    before: Dict[str, Any],
    after: Dict[str, Any],
) -> Dict[str, Any]:
    both_complete = bool(
        before["measurement_complete"]
        and after["measurement_complete"]
    )

    same_metric = bool(
        both_complete
        and before["metric"] == after["metric"]
    )
    same_unit = bool(
        both_complete
        and before["unit"] == after["unit"]
    )
    same_method = bool(
        both_complete
        and before["method"] == after["method"]
    )
    comparable = bool(
        both_complete
        and same_metric
        and same_unit
        and same_method
    )

    reasons: List[str] = []
    if not both_complete:
        reasons.append("BEFORE_AFTER_MEASUREMENT_INCOMPLETE")
    if both_complete and not same_metric:
        reasons.append("BEFORE_AFTER_METRIC_MISMATCH")
    if both_complete and not same_unit:
        reasons.append("BEFORE_AFTER_UNIT_MISMATCH")
    if both_complete and not same_method:
        reasons.append("BEFORE_AFTER_METHOD_MISMATCH")

    return {
        "both_measurements_complete": both_complete,
        "same_metric": same_metric,
        "same_unit": same_unit,
        "same_method": same_method,
        "comparable": comparable,
        "reasons": reasons,
    }


def _measured_improvement(
    *,
    direction: Optional[str],
    before_value: Any,
    after_value: Any,
    target_value: Any,
    comparable: bool,
) -> Dict[str, Any]:
    if not comparable or direction is None:
        return {
            "delta": None,
            "distance_before": None,
            "distance_after": None,
            "improvement_observed": False,
            "reason": "COMPARABLE_MEASUREMENTS_REQUIRED",
        }

    before_numeric = float(before_value)
    after_numeric = float(after_value)
    delta = after_numeric - before_numeric

    if direction == "INCREASE":
        improved = after_numeric > before_numeric
        return {
            "delta": delta,
            "distance_before": None,
            "distance_after": None,
            "improvement_observed": improved,
            "reason": (
                "AFTER_GREATER_THAN_BEFORE"
                if improved
                else "NO_MEASURED_INCREASE"
            ),
        }

    if direction == "DECREASE":
        improved = after_numeric < before_numeric
        return {
            "delta": delta,
            "distance_before": None,
            "distance_after": None,
            "improvement_observed": improved,
            "reason": (
                "AFTER_LESS_THAN_BEFORE"
                if improved
                else "NO_MEASURED_DECREASE"
            ),
        }

    if not _finite_number(target_value):
        return {
            "delta": delta,
            "distance_before": None,
            "distance_after": None,
            "improvement_observed": False,
            "reason": "FINITE_TARGET_VALUE_REQUIRED",
        }

    target_numeric = float(target_value)
    distance_before = abs(before_numeric - target_numeric)
    distance_after = abs(after_numeric - target_numeric)
    improved = distance_after < distance_before
    return {
        "delta": delta,
        "distance_before": distance_before,
        "distance_after": distance_after,
        "improvement_observed": improved,
        "reason": (
            "AFTER_CLOSER_TO_TARGET"
            if improved
            else "NO_MEASURED_PROGRESS_TOWARD_TARGET"
        ),
    }


def _incomplete_case_record(
    *,
    input_index: int,
    sequence: int,
    errors: List[str],
) -> Dict[str, Any]:
    return {
        "sequence": sequence,
        "record_id": f"DNA-25-IMPROVEMENT-{sequence:04d}",
        "input_index": input_index,
        "case_id": None,
        "target": None,
        "target_sha256": None,
        "direction": None,
        "target_value": None,
        "stage_order": deepcopy(STAGE_ORDER),
        "before": _normalize_measurement(None, stage="BEFORE"),
        "change": _normalize_change(None),
        "test": _normalize_test(None),
        "after": _normalize_measurement(None, stage="AFTER"),
        "stage_hashes": {},
        "stage_chain_sha256": None,
        "stage_chain_complete": False,
        "measurement_comparability": {
            "both_measurements_complete": False,
            "same_metric": False,
            "same_unit": False,
            "same_method": False,
            "comparable": False,
            "reasons": ["BEFORE_AFTER_MEASUREMENT_INCOMPLETE"],
        },
        "measurement": {
            "delta": None,
            "distance_before": None,
            "distance_after": None,
            "improvement_observed": False,
            "reason": "COMPARABLE_MEASUREMENTS_REQUIRED",
        },
        "self_upgrade_claimed": False,
        "self_upgrade_claim_eligible": False,
        "unsupported_self_upgrade_claim_blocked": False,
        "change_executed_by_dna25": False,
        "test_executed_by_dna25": False,
        "self_upgrade_applied_by_dna25": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "errors": list(dict.fromkeys(errors)),
        "status": "SELF_IMPROVEMENT_INPUT_INCOMPLETE",
    }


def _normalize_case(
    supplied: Any,
    *,
    input_index: int,
    sequence: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        return _incomplete_case_record(
            input_index=input_index,
            sequence=sequence,
            errors=["SELF_IMPROVEMENT_CASE_MUST_BE_A_DICT"],
        )

    case = deepcopy(supplied)
    errors: List[str] = []

    missing = [
        field
        for field in SELF_IMPROVEMENT_CASE_FIELDS
        if field not in case
    ]
    if missing:
        errors.append("SELF_IMPROVEMENT_CASE_FIELDS_MISSING")

    case_id = case.get("case_id")
    if not _non_empty_text(case_id):
        errors.append("CASE_ID_REQUIRED")

    target = deepcopy(case.get("target"))
    if target is None or target == "" or target == {} or target == []:
        errors.append("IMPROVEMENT_TARGET_REQUIRED")

    direction = _normalize_direction(
        case.get("direction"),
        errors,
    )

    target_value = case.get("target_value")
    if direction == "TARGET" and not _finite_number(target_value):
        errors.append("FINITE_TARGET_VALUE_REQUIRED")

    self_upgrade_claimed = case.get("self_upgrade_claimed")
    if not isinstance(self_upgrade_claimed, bool):
        if "self_upgrade_claimed" in case:
            raise TypeError(
                "self_improvement_case"
                "['self_upgrade_claimed'] must be a bool"
            )
        errors.append("SELF_UPGRADE_CLAIM_STATUS_REQUIRED")
        self_upgrade_claimed = False

    before = _normalize_measurement(
        case.get("before"),
        stage="BEFORE",
    )
    change = _normalize_change(case.get("change"))
    test = _normalize_test(case.get("test"))
    after = _normalize_measurement(
        case.get("after"),
        stage="AFTER",
    )

    for stage_record in (before, change, test, after):
        errors.extend(stage_record["errors"])

    comparability = _measurement_comparability(
        before,
        after,
    )
    measurement = _measured_improvement(
        direction=direction,
        before_value=before["value"],
        after_value=after["value"],
        target_value=target_value,
        comparable=comparability["comparable"],
    )

    stage_chain_complete = bool(
        before["measurement_complete"]
        and change["change_record_complete"]
        and test["test_record_complete"]
        and after["measurement_complete"]
    )

    self_upgrade_claim_eligible = bool(
        stage_chain_complete
        and comparability["comparable"]
        and test["passed"] is True
        and measurement["improvement_observed"]
        and not errors
    )

    unsupported_claim_blocked = bool(
        self_upgrade_claimed
        and not self_upgrade_claim_eligible
    )

    stage_hashes = {
        "before_sha256": _sha256_json(before),
        "change_sha256": _sha256_json(change),
        "test_sha256": _sha256_json(test),
        "after_sha256": _sha256_json(after),
    }
    stage_chain_sha256 = _sha256_json(
        {
            "order": STAGE_ORDER,
            **stage_hashes,
        }
    )

    errors = list(dict.fromkeys(errors))

    if errors:
        status = "SELF_IMPROVEMENT_INPUT_INCOMPLETE"
    elif not stage_chain_complete:
        status = "BEFORE_CHANGE_TEST_AFTER_INCOMPLETE"
    elif not comparability["comparable"]:
        status = "BEFORE_AFTER_NOT_COMPARABLE"
    elif test["passed"] is not True:
        status = "SELF_IMPROVEMENT_TEST_FAILED"
    elif not measurement["improvement_observed"]:
        status = "NO_MEASURED_IMPROVEMENT"
    elif unsupported_claim_blocked:
        status = "UNSUPPORTED_SELF_UPGRADE_CLAIM_BLOCKED"
    elif self_upgrade_claimed:
        status = "MEASURED_SELF_UPGRADE_CLAIM_SUPPORTED"
    else:
        status = "MEASURED_SELF_IMPROVEMENT_ESTABLISHED"

    return {
        "sequence": sequence,
        "record_id": f"DNA-25-IMPROVEMENT-{sequence:04d}",
        "input_index": input_index,
        "case_id": case_id,
        "target": target,
        "target_sha256": (
            _sha256_json(target)
            if target is not None
            else None
        ),
        "direction": direction,
        "target_value": target_value,
        "stage_order": deepcopy(STAGE_ORDER),
        "before": before,
        "change": change,
        "test": test,
        "after": after,
        "stage_hashes": stage_hashes,
        "stage_chain_sha256": stage_chain_sha256,
        "stage_chain_complete": stage_chain_complete,
        "measurement_comparability": comparability,
        "measurement": measurement,
        "self_upgrade_claimed": self_upgrade_claimed,
        "self_upgrade_claim_eligible": (
            self_upgrade_claim_eligible
        ),
        "unsupported_self_upgrade_claim_blocked": (
            unsupported_claim_blocked
        ),
        "change_executed_by_dna25": False,
        "test_executed_by_dna25": False,
        "self_upgrade_applied_by_dna25": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "errors": errors,
        "status": status,
    }


def _evaluate_cases(
    supplied: Any,
    registry: Dict[str, Any],
) -> Dict[str, Any]:
    if supplied is None:
        cases: List[Any] = []
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['self_improvement_cases'] must be a list"
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
            "DNA-25_DUPLICATE_SELF_IMPROVEMENT_CASE_ID"
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

    complete_chain_count = sum(
        1
        for record in records
        if record["stage_chain_complete"]
    )
    comparable_count = sum(
        1
        for record in records
        if record["measurement_comparability"]["comparable"]
    )
    measured_improvement_count = sum(
        1
        for record in records
        if record["measurement"]["improvement_observed"]
    )
    claim_eligible_count = sum(
        1
        for record in records
        if record["self_upgrade_claim_eligible"]
    )
    claimed_count = sum(
        1
        for record in records
        if record["self_upgrade_claimed"]
    )
    unsupported_claim_blocked_count = sum(
        1
        for record in records
        if record[
            "unsupported_self_upgrade_claim_blocked"
        ]
    )
    incomplete_count = sum(
        1
        for record in records
        if record["errors"]
    )

    if not records:
        status = "NO_SELF_IMPROVEMENT_CASES_SUPPLIED"
    elif unsupported_claim_blocked_count:
        status = "UNSUPPORTED_SELF_UPGRADE_CLAIM_BLOCKED"
    elif incomplete_count:
        status = "SELF_IMPROVEMENT_BATCH_INCOMPLETE"
    elif claim_eligible_count == len(records):
        status = "MEASURABLE_SELF_IMPROVEMENT_ESTABLISHED"
    else:
        status = "SELF_IMPROVEMENT_NOT_ESTABLISHED"

    batch_sequence = len(registry["batches"]) + 1
    batch = {
        "sequence": batch_sequence,
        "batch_id": f"DNA-25-BATCH-{batch_sequence:04d}",
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "case_count": len(records),
        "complete_chain_count": complete_chain_count,
        "comparable_count": comparable_count,
        "measured_improvement_count": measured_improvement_count,
        "self_upgrade_claimed_count": claimed_count,
        "self_upgrade_claim_eligible_count": (
            claim_eligible_count
        ),
        "unsupported_self_upgrade_claim_blocked_count": (
            unsupported_claim_blocked_count
        ),
        "incomplete_count": incomplete_count,
        "all_cases_measurably_improved": bool(
            records
            and claim_eligible_count == len(records)
        ),
        "change_executed_by_dna25": False,
        "test_executed_by_dna25": False,
        "self_upgrade_applied_by_dna25": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "status": status,
    }
    registry["batches"].append(deepcopy(batch))

    return {
        "records": records,
        "batch": batch,
    }


def dna25_self_improvement(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Evaluate supplied before→change→test→after evidence and allow a
    self-upgrade claim only when improvement is actually measurable.

    DNA-25 does not execute the change, run the test, apply an upgrade,
    benchmark a model, start Learning Runtime, invoke a model, perform an
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
    trace.append("DNA-25")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, _truth_protocol, _ethical_persistence = (
        _validate_dependencies(context)
    )
    registry = _install_self_improvement_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-25",
            "operation": (
                "SELF_IMPROVEMENT_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "self_improvement_schema": (
                SELF_IMPROVEMENT_SCHEMA
            ),
            "required_stage_order": deepcopy(STAGE_ORDER),
            "unsupported_claim_allowed": False,
            "change_executed": False,
            "test_executed": False,
            "self_upgrade_applied": False,
        }
    )

    evaluation = _evaluate_cases(
        context.get("self_improvement_cases"),
        registry,
    )
    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-25",
            "operation": (
                "BEFORE_CHANGE_TEST_AFTER_EVIDENCE_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "batch_id": batch["batch_id"],
            "case_count": batch["case_count"],
            "complete_chain_count": (
                batch["complete_chain_count"]
            ),
            "measured_improvement_count": (
                batch["measured_improvement_count"]
            ),
            "self_upgrade_claim_eligible_count": (
                batch["self_upgrade_claim_eligible_count"]
            ),
            "unsupported_claim_blocked_count": (
                batch[
                    "unsupported_self_upgrade_claim_blocked_count"
                ]
            ),
            "change_executed": False,
            "test_executed": False,
            "self_upgrade_applied": False,
        }
    )

    outputs["DNA-25"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "self_improvement_contract": deepcopy(
            SELF_IMPROVEMENT_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "case_count": batch["case_count"],
        "complete_chain_count": batch["complete_chain_count"],
        "measured_improvement_count": (
            batch["measured_improvement_count"]
        ),
        "self_upgrade_claim_eligible_count": (
            batch["self_upgrade_claim_eligible_count"]
        ),
        "unsupported_self_upgrade_claim_blocked_count": (
            batch[
                "unsupported_self_upgrade_claim_blocked_count"
            ]
        ),
        "change_executed_by_dna25": False,
        "test_executed_by_dna25": False,
        "self_upgrade_applied_by_dna25": False,
        "benchmark_executed_by_dna25": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna25(core54: Core54Like) -> None:
    core = core54.get("DNA-25")
    assert_exact_canon(core)
    core54.bind(
        "DNA-25",
        dna25_self_improvement,
    )


def _through_dna24(core54: Core54Like) -> Dict[str, Any]:
    from SIGMA_DNA_24_ETHICAL_PERSISTENCE import (
        _through_dna23,
        _valid_case,
    )

    through_dna23 = _through_dna23(core54)
    through_dna23["ethical_persistence_cases"] = [
        _valid_case()
    ]
    return core54.get("DNA-24").activate(
        through_dna23
    )


def _measurement(
    *,
    value: float,
    stage: str,
    metric: str = "VERIFIED_TASK_SUCCESS_RATE",
    unit: str = "RATIO",
    method: str = "HELD_OUT_EVALUATION_V1",
) -> Dict[str, Any]:
    return {
        "metric": metric,
        "value": value,
        "unit": unit,
        "method": method,
        "evidence": [
            {
                "evidence_id": f"DNA25-{stage}-EVIDENCE",
                "observation": f"{stage}_VALUE_{value}",
            }
        ],
    }


def _valid_case(
    *,
    direction: str = "INCREASE",
    before_value: float = 0.72,
    after_value: float = 0.84,
    test_passed: bool = True,
    self_upgrade_claimed: bool = True,
) -> Dict[str, Any]:
    case: Dict[str, Any] = {
        "case_id": "DNA25-CASE-VALID",
        "target": {
            "component": "STRATEGY-CANDIDATE-DNA25",
            "capability": "VERIFIED_TASK_SUCCESS",
        },
        "direction": direction,
        "before": _measurement(
            value=before_value,
            stage="BEFORE",
        ),
        "change": {
            "change_id": "DNA25-CHANGE-01",
            "description": "APPLY_REVISED_STRATEGY_CANDIDATE",
            "evidence": [
                {
                    "evidence_id": "DNA25-CHANGE-EVIDENCE",
                    "observation": "CHANGE_RECORD_SUPPLIED",
                }
            ],
        },
        "test": {
            "test_id": "DNA25-TEST-01",
            "method": "HELD_OUT_EVALUATION_V1",
            "passed": test_passed,
            "evidence": [
                {
                    "evidence_id": "DNA25-TEST-EVIDENCE",
                    "observation": (
                        "TEST_PASS"
                        if test_passed
                        else "TEST_FAIL"
                    ),
                }
            ],
        },
        "after": _measurement(
            value=after_value,
            stage="AFTER",
        ),
        "self_upgrade_claimed": self_upgrade_claimed,
    }

    if direction == "TARGET":
        case["target_value"] = 1.0

    return case


def self_check_dna25(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 25):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna25_core = core54.get("DNA-25")
    assert_exact_canon(dna25_core)
    bind_dna25(core54)

    through_dna24 = _through_dna24(core54)
    through_dna24_snapshot = deepcopy(through_dna24)

    state_before = through_dna24["cognitive_state"]
    pre_truth_protocol = deepcopy(
        state_before["truth_protocol"]
    )
    pre_ethical_persistence = deepcopy(
        state_before["ethical_persistence"]
    )
    pre_provenance_count = len(
        state_before["provenance"]
    )

    valid_input = deepcopy(through_dna24)
    valid_input["self_improvement_cases"] = [
        _valid_case()
    ]
    result = dna25_core.activate(valid_input)

    assert through_dna24 == through_dna24_snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 26)
    ]

    dna25 = result["core54_outputs"]["DNA-25"]
    assert dna25["canonical_gene"] == CANON_DNA25
    assert dna25["self_improvement_contract"] == (
        SELF_IMPROVEMENT_CONTRACT
    )
    assert dna25["case_count"] == 1
    assert dna25["complete_chain_count"] == 1
    assert dna25["measured_improvement_count"] == 1
    assert dna25["self_upgrade_claim_eligible_count"] == 1
    assert (
        dna25[
            "unsupported_self_upgrade_claim_blocked_count"
        ]
        == 0
    )
    assert dna25["change_executed_by_dna25"] is False
    assert dna25["test_executed_by_dna25"] is False
    assert dna25["self_upgrade_applied_by_dna25"] is False
    assert dna25["benchmark_executed_by_dna25"] is False
    assert dna25["learning_runtime_started"] is False
    assert dna25["external_action_executed"] is False
    assert dna25["status"] == "CANON_ALIGNED"

    evaluation = dna25["evaluation"]
    record = evaluation["records"][0]
    batch = evaluation["batch"]

    assert record["stage_order"] == STAGE_ORDER
    assert record["stage_chain_complete"] is True
    assert record["measurement_comparability"] == {
        "both_measurements_complete": True,
        "same_metric": True,
        "same_unit": True,
        "same_method": True,
        "comparable": True,
        "reasons": [],
    }
    assert record["measurement"]["delta"] == (
        0.84 - 0.72
    )
    assert record["measurement"]["improvement_observed"] is True
    assert record["measurement"]["reason"] == (
        "AFTER_GREATER_THAN_BEFORE"
    )
    assert record["self_upgrade_claimed"] is True
    assert record["self_upgrade_claim_eligible"] is True
    assert (
        record["unsupported_self_upgrade_claim_blocked"]
        is False
    )
    assert record["errors"] == []
    assert record["status"] == (
        "MEASURED_SELF_UPGRADE_CLAIM_SUPPORTED"
    )

    assert batch["batch_id"] == "DNA-25-BATCH-0001"
    assert batch["case_count"] == 1
    assert batch["complete_chain_count"] == 1
    assert batch["comparable_count"] == 1
    assert batch["measured_improvement_count"] == 1
    assert batch["self_upgrade_claimed_count"] == 1
    assert batch["self_upgrade_claim_eligible_count"] == 1
    assert (
        batch[
            "unsupported_self_upgrade_claim_blocked_count"
        ]
        == 0
    )
    assert batch["incomplete_count"] == 0
    assert batch["all_cases_measurably_improved"] is True
    assert batch["status"] == (
        "MEASURABLE_SELF_IMPROVEMENT_ESTABLISHED"
    )

    state = result["cognitive_state"]
    registry = state["self_improvement"]
    assert registry["contract"] == SELF_IMPROVEMENT_CONTRACT
    assert registry["records"] == [record]
    assert registry["batches"] == [batch]
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-25"
    assert contract_event["operation"] == (
        "SELF_IMPROVEMENT_CONTRACT_ESTABLISHED"
    )
    assert contract_event["required_stage_order"] == STAGE_ORDER
    assert contract_event["unsupported_claim_allowed"] is False
    assert contract_event["change_executed"] is False
    assert contract_event["test_executed"] is False
    assert contract_event["self_upgrade_applied"] is False

    evaluation_event = state["provenance"][-1]
    assert evaluation_event["core_id"] == "DNA-25"
    assert evaluation_event["operation"] == (
        "BEFORE_CHANGE_TEST_AFTER_EVIDENCE_EVALUATED"
    )
    assert evaluation_event["case_count"] == 1
    assert evaluation_event["complete_chain_count"] == 1
    assert evaluation_event["measured_improvement_count"] == 1
    assert (
        evaluation_event[
            "self_upgrade_claim_eligible_count"
        ]
        == 1
    )
    assert (
        evaluation_event[
            "unsupported_claim_blocked_count"
        ]
        == 0
    )
    assert evaluation_event["change_executed"] is False
    assert evaluation_event["test_executed"] is False
    assert evaluation_event["self_upgrade_applied"] is False

    assert state["truth_protocol"] == pre_truth_protocol
    assert state["ethical_persistence"] == (
        pre_ethical_persistence
    )

    # Failed test must block a self-upgrade claim.
    failed_test_input = deepcopy(through_dna24)
    failed_test_input["self_improvement_cases"] = [
        _valid_case(test_passed=False)
    ]
    failed_test = dna25_core.activate(failed_test_input)
    failed_record = failed_test[
        "core54_outputs"
    ]["DNA-25"]["evaluation"]["records"][0]
    assert failed_record["stage_chain_complete"] is True
    assert failed_record["measurement"]["improvement_observed"] is True
    assert failed_record["self_upgrade_claim_eligible"] is False
    assert (
        failed_record["unsupported_self_upgrade_claim_blocked"]
        is True
    )
    assert failed_record["status"] == (
        "SELF_IMPROVEMENT_TEST_FAILED"
    )

    # A claimed upgrade without a measured improvement must be blocked.
    no_gain_input = deepcopy(through_dna24)
    no_gain_input["self_improvement_cases"] = [
        _valid_case(after_value=0.70)
    ]
    no_gain = dna25_core.activate(no_gain_input)
    no_gain_record = no_gain[
        "core54_outputs"
    ]["DNA-25"]["evaluation"]["records"][0]
    assert no_gain_record["measurement"]["improvement_observed"] is False
    assert no_gain_record["self_upgrade_claim_eligible"] is False
    assert (
        no_gain_record["unsupported_self_upgrade_claim_blocked"]
        is True
    )
    assert no_gain_record["status"] == (
        "NO_MEASURED_IMPROVEMENT"
    )

    # Before and after must be directly comparable.
    mismatch_input = deepcopy(through_dna24)
    mismatch_case = _valid_case()
    mismatch_case["after"]["metric"] = "DIFFERENT_METRIC"
    mismatch_input["self_improvement_cases"] = [
        mismatch_case
    ]
    mismatch = dna25_core.activate(mismatch_input)
    mismatch_record = mismatch[
        "core54_outputs"
    ]["DNA-25"]["evaluation"]["records"][0]
    assert mismatch_record[
        "measurement_comparability"
    ]["comparable"] is False
    assert (
        "BEFORE_AFTER_METRIC_MISMATCH"
        in mismatch_record[
            "measurement_comparability"
        ]["reasons"]
    )
    assert mismatch_record["self_upgrade_claim_eligible"] is False

    # DECREASE direction must demonstrate a lower measured value.
    decrease_input = deepcopy(through_dna24)
    decrease_case = _valid_case(
        direction="DECREASE",
        before_value=10.0,
        after_value=7.0,
    )
    decrease_input["self_improvement_cases"] = [
        decrease_case
    ]
    decrease = dna25_core.activate(decrease_input)
    decrease_record = decrease[
        "core54_outputs"
    ]["DNA-25"]["evaluation"]["records"][0]
    assert decrease_record["measurement"]["delta"] == -3.0
    assert decrease_record["measurement"]["improvement_observed"] is True
    assert decrease_record["measurement"]["reason"] == (
        "AFTER_LESS_THAN_BEFORE"
    )
    assert decrease_record["self_upgrade_claim_eligible"] is True

    # TARGET direction must demonstrate reduced distance to the target.
    target_input = deepcopy(through_dna24)
    target_case = _valid_case(
        direction="TARGET",
        before_value=0.55,
        after_value=0.82,
    )
    target_input["self_improvement_cases"] = [
        target_case
    ]
    target = dna25_core.activate(target_input)
    target_record = target[
        "core54_outputs"
    ]["DNA-25"]["evaluation"]["records"][0]
    assert math.isclose(
        target_record["measurement"]["distance_before"],
        0.45,
        rel_tol=0.0,
        abs_tol=1e-12,
    )
    assert math.isclose(
        target_record["measurement"]["distance_after"],
        1.0 - 0.82,
        rel_tol=0.0,
        abs_tol=1e-12,
    )
    assert target_record["measurement"]["improvement_observed"] is True
    assert target_record["self_upgrade_claim_eligible"] is True

    # Missing a stage cannot satisfy before→change→test→after.
    missing_stage_input = deepcopy(through_dna24)
    missing_stage_case = _valid_case()
    missing_stage_case.pop("change")
    missing_stage_input["self_improvement_cases"] = [
        missing_stage_case
    ]
    missing_stage = dna25_core.activate(
        missing_stage_input
    )
    missing_stage_record = missing_stage[
        "core54_outputs"
    ]["DNA-25"]["evaluation"]["records"][0]
    assert missing_stage_record["stage_chain_complete"] is False
    assert missing_stage_record["self_upgrade_claim_eligible"] is False
    assert (
        "SELF_IMPROVEMENT_CASE_FIELDS_MISSING"
        in missing_stage_record["errors"]
    )

    # Non-numeric measurement cannot support an upgrade claim.
    non_numeric_input = deepcopy(through_dna24)
    non_numeric_case = _valid_case()
    non_numeric_case["after"]["value"] = "0.84"
    non_numeric_input["self_improvement_cases"] = [
        non_numeric_case
    ]
    non_numeric = dna25_core.activate(non_numeric_input)
    non_numeric_record = non_numeric[
        "core54_outputs"
    ]["DNA-25"]["evaluation"]["records"][0]
    assert (
        "AFTER_FINITE_NUMERIC_VALUE_REQUIRED"
        in non_numeric_record["errors"]
    )
    assert non_numeric_record["self_upgrade_claim_eligible"] is False

    # Case identity must be unique inside a batch.
    duplicate_input = deepcopy(through_dna24)
    duplicate_case = _valid_case()
    duplicate_input["self_improvement_cases"] = [
        deepcopy(duplicate_case),
        deepcopy(duplicate_case),
    ]
    try:
        dna25_core.activate(duplicate_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-25_DUPLICATE_SELF_IMPROVEMENT_CASE_ID"
        )
    else:
        raise AssertionError(
            "DNA-25_ACCEPTED_DUPLICATE_CASE_ID"
        )

    # Reject provisional root-marker behavior as the official contract.
    assert "self_improvement_evidence_complete" not in result
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
        "core_id": "DNA-25",
        "canon_mapping": "PASS",
        "before_change_test_after": "PASS",
        "measurable_improvement": "PASS",
        "unsupported_claim_block": "PASS",
        "increase_direction": "PASS",
        "decrease_direction": "PASS",
        "target_direction": "PASS",
        "change_executed_by_dna25": False,
        "test_executed_by_dna25": False,
        "self_upgrade_applied_by_dna25": False,
        "learning_runtime_used": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-26"
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
            print("DNA-25_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = _load_prior_modules()
    except Exception as exc:
        print("DNA-25_FAIL: IMPORT_ERROR")
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

        for index in range(1, 25):
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

        report = self_check_dna25(
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
            for index in range(1, 26)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-25_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-25_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_25_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "BEFORE_CHANGE_TEST_AFTER:",
        report["before_change_test_after"],
    )
    print(
        "MEASURABLE_IMPROVEMENT:",
        report["measurable_improvement"],
    )
    print(
        "UNSUPPORTED_CLAIM_BLOCK:",
        report["unsupported_claim_block"],
    )
    print(
        "CHANGE_EXECUTED_BY_DNA25:",
        report["change_executed_by_dna25"],
    )
    print(
        "TEST_EXECUTED_BY_DNA25:",
        report["test_executed_by_dna25"],
    )
    print(
        "SELF_UPGRADE_APPLIED_BY_DNA25:",
        report["self_upgrade_applied_by_dna25"],
    )
    print(
        "LEARNING_RUNTIME_USED:",
        report["learning_runtime_used"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 25/54")
    print("NEXT_AUTHORIZED: DNA-26")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
