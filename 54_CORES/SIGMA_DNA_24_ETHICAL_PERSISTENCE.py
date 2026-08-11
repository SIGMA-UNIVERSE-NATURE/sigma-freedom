#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-24: ETHICAL PERSISTENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_24_ETHICAL_PERSISTENCE.py
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

CANON_DNA24: Dict[str, str] = {
    "id": "DNA-24",
    "name": "Ethical Persistence",
    "purpose": (
        "Không bỏ mục tiêu thiện vì một con đường thất bại; "
        "đổi đường, kiểm chứng lại mục tiêu khi cần."
    ),
    "system": "wisdom",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
ETHICAL_SCHEMA = "SIGMA_ETHICAL_INTELLIGENCE_V1"
PERSISTENT_EXISTENCE_SCHEMA = "SIGMA_PERSISTENT_EXISTENCE_V1"
PERSISTENCE_ENGINE_SCHEMA = "SIGMA_PERSISTENCE_ENGINE_V1"
TRUTH_PROTOCOL_SCHEMA = "SIGMA_TRUTH_PROTOCOL_V1"
COGNITIVE_FREEDOM_SCHEMA = "SIGMA_COGNITIVE_FREEDOM_V1"
ETHICAL_PERSISTENCE_SCHEMA = "SIGMA_ETHICAL_PERSISTENCE_V1"

ETHICAL_BOOLEAN_FIELDS = [
    "consequences_beneficial",
    "dignity_preserved",
    "autonomy_preserved",
    "non_bullying",
    "non_manipulation",
    "non_coercion",
]

ETHICAL_ASSESSMENT_FIELDS = [
    *ETHICAL_BOOLEAN_FIELDS,
    "evidence",
]

ETHICAL_PERSISTENCE_CASE_FIELDS = [
    "case_id",
    "goal_id",
    "goal",
    "initial_ethical_assessment",
    "path_failed",
    "current_path",
    "next_path",
    "goal_reverification",
]

GOAL_REVERIFICATION_FIELDS = [
    "required",
    "performed",
]

ETHICAL_PERSISTENCE_CONTRACT: Dict[str, Any] = {
    "schema": ETHICAL_PERSISTENCE_SCHEMA,
    "input_path": "ethical_persistence_cases",
    "required_case_fields": deepcopy(
        ETHICAL_PERSISTENCE_CASE_FIELDS
    ),
    "ethical_assessment_fields": deepcopy(
        ETHICAL_ASSESSMENT_FIELDS
    ),
    "goal_reverification_fields": deepcopy(
        GOAL_REVERIFICATION_FIELDS
    ),
    "ethical_dimensions_bound_to_dna05": [
        "consequences",
        "dignity",
        "autonomy",
        "non_bullying",
        "non_manipulation",
        "non_coercion",
    ],
    "failed_path_abandons_ethical_goal": False,
    "failed_path_requires_path_change": True,
    "same_failed_path_counts_as_change": False,
    "goal_reverification_supported": True,
    "required_reverification_must_complete_before_continuation": True,
    "reverification_uses_same_ethical_dimensions": True,
    "missing_evidence_is_not_invented": True,
    "goal_executed_by_dna24": False,
    "path_executed_by_dna24": False,
    "goal_abandoned_by_dna24": False,
    "learning_runtime_started": False,
    "world_runtime_started": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA05_ETHICS_"
        "DNA07_PERSISTENCE_DNA14_INFORMATION_GAIN_"
        "DNA21_TRUTH_AND_DNA23_COGNITIVE_FREEDOM_BINDING"
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
    if actual != CANON_DNA24:
        raise RuntimeError(
            "DNA-24_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA24,
                    "actual": actual,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-24_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    ethical = state.get("ethical_intelligence")
    if not isinstance(ethical, dict):
        raise RuntimeError(
            "DNA-05_ETHICAL_INTELLIGENCE_REQUIRED"
        )
    if ethical.get("schema") != ETHICAL_SCHEMA:
        raise ValueError(
            "DNA-24_ETHICAL_SCHEMA_MISMATCH:"
            f"{ethical.get('schema')!r}"
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
            "DNA-24_PERSISTENT_EXISTENCE_SCHEMA_MISMATCH:"
            f"{persistent_contract.get('schema')!r}"
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
            "DNA-24_PERSISTENCE_ENGINE_SCHEMA_MISMATCH:"
            f"{persistence_contract.get('schema')!r}"
        )

    truth_protocol = state.get("truth_protocol")
    if not isinstance(truth_protocol, dict):
        raise RuntimeError(
            "DNA-21_TRUTH_PROTOCOL_REQUIRED"
        )
    truth_contract = truth_protocol.get("contract")
    if not isinstance(truth_contract, dict):
        raise RuntimeError(
            "DNA-21_TRUTH_PROTOCOL_CONTRACT_REQUIRED"
        )
    if truth_contract.get("schema") != TRUTH_PROTOCOL_SCHEMA:
        raise ValueError(
            "DNA-24_TRUTH_PROTOCOL_SCHEMA_MISMATCH:"
            f"{truth_contract.get('schema')!r}"
        )

    cognitive_freedom = state.get("cognitive_freedom")
    if not isinstance(cognitive_freedom, dict):
        raise RuntimeError(
            "DNA-23_COGNITIVE_FREEDOM_REQUIRED"
        )
    freedom_contract = cognitive_freedom.get("contract")
    if not isinstance(freedom_contract, dict):
        raise RuntimeError(
            "DNA-23_COGNITIVE_FREEDOM_CONTRACT_REQUIRED"
        )
    if freedom_contract.get("schema") != COGNITIVE_FREEDOM_SCHEMA:
        raise ValueError(
            "DNA-24_COGNITIVE_FREEDOM_SCHEMA_MISMATCH:"
            f"{freedom_contract.get('schema')!r}"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-05_TO_DNA-23_OUTPUTS_REQUIRED")

    for required_id in (
        "DNA-05",
        "DNA-07",
        "DNA-14",
        "DNA-21",
        "DNA-23",
    ):
        if not isinstance(outputs.get(required_id), dict):
            raise RuntimeError(f"{required_id}_OUTPUT_REQUIRED")

    return state


def _install_ethical_persistence_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("ethical_persistence")

    expected = {
        "contract": deepcopy(ETHICAL_PERSISTENCE_CONTRACT),
        "records": [],
        "batches": [],
    }

    if existing is None:
        state["ethical_persistence"] = expected
        return state["ethical_persistence"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['ethical_persistence'] must be a dict"
        )

    if existing.get("contract") != ETHICAL_PERSISTENCE_CONTRACT:
        raise ValueError(
            "DNA-24_ETHICAL_PERSISTENCE_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("records"), list):
        raise TypeError(
            "ethical_persistence['records'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "ethical_persistence['batches'] must be a list"
        )

    return existing


def _normalize_ethical_assessment(
    supplied: Any,
    *,
    prefix: str,
) -> Dict[str, Any]:
    errors: List[str] = []

    if not isinstance(supplied, dict):
        return {
            "values": {
                field: None
                for field in ETHICAL_BOOLEAN_FIELDS
            },
            "evidence": [],
            "evidence_sha256": None,
            "complete": False,
            "ethical_aligned": False,
            "errors": [f"{prefix}_ASSESSMENT_REQUIRED"],
        }

    assessment = deepcopy(supplied)
    missing = [
        field
        for field in ETHICAL_ASSESSMENT_FIELDS
        if field not in assessment
    ]
    if missing:
        errors.append(f"{prefix}_ASSESSMENT_FIELDS_MISSING")

    values: Dict[str, Optional[bool]] = {}
    for field in ETHICAL_BOOLEAN_FIELDS:
        value = assessment.get(field)
        if value is not None and not isinstance(value, bool):
            raise TypeError(
                f"{prefix.lower()}_ethical_assessment"
                f"['{field}'] must be a bool"
            )
        if field not in assessment:
            errors.append(f"{prefix}_{field.upper()}_REQUIRED")
        values[field] = value

    evidence = assessment.get("evidence")
    if evidence is not None and not isinstance(evidence, list):
        raise TypeError(
            f"{prefix.lower()}_ethical_assessment"
            "['evidence'] must be a list"
        )
    if not isinstance(evidence, list) or not evidence:
        errors.append(f"{prefix}_ETHICAL_EVIDENCE_REQUIRED")
        evidence_list: List[Any] = []
    else:
        if any(item is None for item in evidence):
            raise ValueError(
                f"DNA-24_{prefix}_ETHICAL_EVIDENCE_ITEM_NULL"
            )
        evidence_list = deepcopy(evidence)

    errors = list(dict.fromkeys(errors))
    complete = not errors
    ethical_aligned = bool(
        complete
        and all(values[field] is True for field in ETHICAL_BOOLEAN_FIELDS)
    )

    return {
        "values": values,
        "evidence": evidence_list,
        "evidence_sha256": (
            _sha256_json(evidence_list)
            if evidence_list
            else None
        ),
        "complete": complete,
        "ethical_aligned": ethical_aligned,
        "errors": errors,
    }


def _normalize_reverification(
    supplied: Any,
) -> Dict[str, Any]:
    errors: List[str] = []

    if not isinstance(supplied, dict):
        return {
            "required": None,
            "performed": None,
            "assessment": None,
            "complete": False,
            "ethical_aligned": None,
            "errors": ["GOAL_REVERIFICATION_RECORD_REQUIRED"],
            "status": "GOAL_REVERIFICATION_INPUT_INCOMPLETE",
        }

    record = deepcopy(supplied)
    missing = [
        field
        for field in GOAL_REVERIFICATION_FIELDS
        if field not in record
    ]
    if missing:
        errors.append("GOAL_REVERIFICATION_FIELDS_MISSING")

    required = record.get("required")
    performed = record.get("performed")

    for field, value in (
        ("required", required),
        ("performed", performed),
    ):
        if value is not None and not isinstance(value, bool):
            raise TypeError(
                f"goal_reverification['{field}'] must be a bool"
            )
        if field not in record:
            errors.append(
                f"GOAL_REVERIFICATION_{field.upper()}_REQUIRED"
            )

    assessment: Optional[Dict[str, Any]] = None
    if performed is True:
        assessment = _normalize_ethical_assessment(
            record.get("ethical_assessment"),
            prefix="REVERIFIED_GOAL",
        )
        errors.extend(assessment["errors"])
    elif "ethical_assessment" in record:
        errors.append(
            "GOAL_REVERIFICATION_ASSESSMENT_WITHOUT_PERFORMANCE"
        )

    errors = list(dict.fromkeys(errors))
    complete = not errors

    if errors:
        status = "GOAL_REVERIFICATION_INPUT_INCOMPLETE"
        aligned: Optional[bool] = None
    elif required is True and performed is False:
        status = "GOAL_REVERIFICATION_REQUIRED"
        aligned = None
    elif performed is True:
        assert assessment is not None
        aligned = bool(assessment["ethical_aligned"])
        status = (
            "GOAL_REVERIFICATION_PASSED"
            if aligned
            else "GOAL_REVERIFICATION_FAILED"
        )
    else:
        status = "GOAL_REVERIFICATION_NOT_REQUIRED"
        aligned = None

    return {
        "required": required,
        "performed": performed,
        "assessment": assessment,
        "complete": complete,
        "ethical_aligned": aligned,
        "errors": errors,
        "status": status,
    }


def _incomplete_record(
    *,
    input_index: int,
    sequence: int,
    errors: List[str],
) -> Dict[str, Any]:
    unique_errors = list(dict.fromkeys(errors))
    return {
        "sequence": sequence,
        "record_id": f"DNA-24-ETHICAL-PERSISTENCE-{sequence:04d}",
        "input_index": input_index,
        "case_id": None,
        "goal_id": None,
        "goal": None,
        "goal_sha256": None,
        "initial_ethical_assessment": None,
        "goal_reverification": None,
        "effective_ethical_assessment_source": None,
        "ethical_goal_confirmed": False,
        "path_failed": None,
        "current_path": None,
        "next_path": None,
        "path_changed": False,
        "failed_path_repeated": False,
        "change_path_required": False,
        "goal_continuity_preserved": False,
        "goal_abandoned_due_to_path_failure": False,
        "goal_reconsideration_required": False,
        "continue_eligible": False,
        "goal_executed_by_dna24": False,
        "path_executed_by_dna24": False,
        "external_action_executed": False,
        "errors": unique_errors,
        "status": "ETHICAL_PERSISTENCE_INPUT_INCOMPLETE",
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
            errors=["ETHICAL_PERSISTENCE_CASE_MUST_BE_A_DICT"],
        )

    case = deepcopy(supplied)
    errors: List[str] = []

    missing = [
        field
        for field in ETHICAL_PERSISTENCE_CASE_FIELDS
        if field not in case
    ]
    if missing:
        errors.append("ETHICAL_PERSISTENCE_CASE_FIELDS_MISSING")

    case_id = case.get("case_id")
    if not _non_empty_text(case_id):
        errors.append("CASE_ID_REQUIRED")

    goal_id = case.get("goal_id")
    if not _non_empty_text(goal_id):
        errors.append("GOAL_ID_REQUIRED")

    goal = case.get("goal")
    if goal is None:
        errors.append("GOAL_REQUIRED")
    goal_sha256 = _sha256_json(goal) if goal is not None else None

    initial_assessment = _normalize_ethical_assessment(
        case.get("initial_ethical_assessment"),
        prefix="INITIAL_GOAL",
    )
    errors.extend(initial_assessment["errors"])

    path_failed = case.get("path_failed")
    if path_failed is not None and not isinstance(path_failed, bool):
        raise TypeError(
            "ethical_persistence_case['path_failed'] must be a bool"
        )
    if "path_failed" not in case:
        errors.append("PATH_FAILED_STATUS_REQUIRED")

    current_path = case.get("current_path")
    if current_path is None:
        errors.append("CURRENT_PATH_REQUIRED")

    next_path = case.get("next_path")

    reverification = _normalize_reverification(
        case.get("goal_reverification")
    )
    errors.extend(reverification["errors"])

    current_path_sha256 = (
        _sha256_json(current_path)
        if current_path is not None
        else None
    )
    next_path_sha256 = (
        _sha256_json(next_path)
        if next_path is not None
        else None
    )

    path_changed = bool(
        next_path_sha256 is not None
        and current_path_sha256 is not None
        and next_path_sha256 != current_path_sha256
    )
    failed_path_repeated = bool(
        path_failed is True
        and next_path_sha256 is not None
        and current_path_sha256 is not None
        and next_path_sha256 == current_path_sha256
    )

    if reverification["performed"] is True:
        effective_assessment = reverification["assessment"]
        effective_source = "GOAL_REVERIFICATION"
        ethical_goal_confirmed = bool(
            reverification["ethical_aligned"] is True
        )
    elif (
        reverification["required"] is True
        and reverification["performed"] is False
    ):
        effective_assessment = None
        effective_source = "PENDING_GOAL_REVERIFICATION"
        ethical_goal_confirmed = False
    else:
        effective_assessment = initial_assessment
        effective_source = "INITIAL_ETHICAL_ASSESSMENT"
        ethical_goal_confirmed = bool(
            initial_assessment["ethical_aligned"]
        )

    reverification_pending = bool(
        reverification["required"] is True
        and reverification["performed"] is False
        and not reverification["errors"]
    )

    goal_reconsideration_required = bool(
        not errors
        and not reverification_pending
        and not ethical_goal_confirmed
    )

    change_path_required = bool(
        path_failed is True
        and (
            ethical_goal_confirmed
            or reverification_pending
        )
    )

    goal_continuity_preserved = bool(
        not errors
        and (
            ethical_goal_confirmed
            or reverification_pending
        )
    )

    continue_eligible = bool(
        not errors
        and ethical_goal_confirmed
        and not reverification_pending
        and not failed_path_repeated
        and (
            path_failed is not True
            or path_changed
        )
    )

    errors = list(dict.fromkeys(errors))

    if errors:
        status = "ETHICAL_PERSISTENCE_INPUT_INCOMPLETE"
    elif reverification_pending:
        status = "GOAL_REVERIFICATION_REQUIRED"
    elif goal_reconsideration_required:
        status = "GOAL_RECONSIDERATION_REQUIRED"
    elif path_failed is True and next_path is None:
        status = "ETHICAL_GOAL_PRESERVED_CHANGE_PATH_REQUIRED"
    elif failed_path_repeated:
        status = "FAILED_PATH_REPETITION_REJECTED"
    elif path_failed is True and path_changed:
        status = "ETHICAL_GOAL_PRESERVED_PATH_CHANGED"
    elif path_failed is False:
        status = "ETHICAL_GOAL_CONTINUES"
    else:
        status = "ETHICAL_PERSISTENCE_NOT_FULLY_RESOLVED"

    return {
        "sequence": sequence,
        "record_id": f"DNA-24-ETHICAL-PERSISTENCE-{sequence:04d}",
        "input_index": input_index,
        "case_id": case_id,
        "goal_id": goal_id,
        "goal": deepcopy(goal),
        "goal_sha256": goal_sha256,
        "initial_ethical_assessment": initial_assessment,
        "goal_reverification": reverification,
        "effective_ethical_assessment": deepcopy(
            effective_assessment
        ),
        "effective_ethical_assessment_source": effective_source,
        "ethical_goal_confirmed": ethical_goal_confirmed,
        "path_failed": path_failed,
        "current_path": deepcopy(current_path),
        "current_path_sha256": current_path_sha256,
        "next_path": deepcopy(next_path),
        "next_path_sha256": next_path_sha256,
        "path_changed": path_changed,
        "failed_path_repeated": failed_path_repeated,
        "change_path_required": change_path_required,
        "goal_continuity_preserved": goal_continuity_preserved,
        "goal_abandoned_due_to_path_failure": False,
        "goal_reconsideration_required": (
            goal_reconsideration_required
        ),
        "continue_eligible": continue_eligible,
        "goal_executed_by_dna24": False,
        "path_executed_by_dna24": False,
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
            "context['ethical_persistence_cases'] must be a list"
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
            "DNA-24_DUPLICATE_ETHICAL_PERSISTENCE_CASE_ID"
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
        if record["continue_eligible"]
    )
    goal_preserved_count = sum(
        1
        for record in records
        if record["goal_continuity_preserved"]
    )
    path_change_required_count = sum(
        1
        for record in records
        if record["change_path_required"]
    )
    path_changed_count = sum(
        1
        for record in records
        if record["path_changed"]
    )
    reverification_required_count = sum(
        1
        for record in records
        if record["goal_reverification"]["required"] is True
        if record["goal_reverification"] is not None
    )
    reverification_pending_count = sum(
        1
        for record in records
        if record["status"] == "GOAL_REVERIFICATION_REQUIRED"
    )
    reconsideration_count = sum(
        1
        for record in records
        if record["goal_reconsideration_required"]
    )
    failed_path_repetition_count = sum(
        1
        for record in records
        if record["failed_path_repeated"]
    )
    incomplete_count = sum(
        1
        for record in records
        if record["errors"]
    )

    if not records:
        status = "NO_ETHICAL_PERSISTENCE_CASES_SUPPLIED"
    elif incomplete_count:
        status = "ETHICAL_PERSISTENCE_BATCH_INCOMPLETE"
    elif reconsideration_count:
        status = "GOAL_RECONSIDERATION_REQUIRED"
    elif reverification_pending_count:
        status = "GOAL_REVERIFICATION_REQUIRED"
    elif failed_path_repetition_count:
        status = "FAILED_PATH_REPETITION_REJECTED"
    elif aligned_count == len(records):
        status = "ETHICAL_PERSISTENCE_ALIGNED"
    else:
        status = "ETHICAL_PERSISTENCE_ACTION_REQUIRED"

    batch_sequence = len(registry["batches"]) + 1
    batch = {
        "sequence": batch_sequence,
        "batch_id": f"DNA-24-BATCH-{batch_sequence:04d}",
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "case_count": len(records),
        "continue_eligible_count": aligned_count,
        "goal_preserved_count": goal_preserved_count,
        "path_change_required_count": path_change_required_count,
        "path_changed_count": path_changed_count,
        "goal_reverification_required_count": (
            reverification_required_count
        ),
        "goal_reverification_pending_count": (
            reverification_pending_count
        ),
        "goal_reconsideration_required_count": (
            reconsideration_count
        ),
        "failed_path_repetition_count": (
            failed_path_repetition_count
        ),
        "incomplete_count": incomplete_count,
        "all_cases_continue_eligible": bool(
            records and aligned_count == len(records)
        ),
        "goal_abandoned_due_to_path_failure_count": 0,
        "goal_executed_by_dna24": False,
        "path_executed_by_dna24": False,
        "external_action_executed": False,
        "status": status,
    }
    registry["batches"].append(deepcopy(batch))

    return {
        "records": records,
        "batch": batch,
    }


def dna24_ethical_persistence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Preserve a confirmed ethical goal across a failed path, require a
    different path, and require goal re-verification when the supplied
    context marks it necessary.

    DNA-24 evaluates supplied state only. It does not execute the goal or
    path, abandon a goal, start Learning/World Runtime, invoke a model,
    perform external action, or modify Canon.
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
    trace.append("DNA-24")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_dependencies(context)
    registry = _install_ethical_persistence_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-24",
            "operation": (
                "ETHICAL_PERSISTENCE_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "ethical_persistence_schema": (
                ETHICAL_PERSISTENCE_SCHEMA
            ),
            "failed_path_abandons_ethical_goal": False,
            "goal_executed_by_dna24": False,
            "path_executed_by_dna24": False,
            "external_action_executed": False,
        }
    )

    evaluation = _evaluate_cases(
        context.get("ethical_persistence_cases"),
        registry,
    )
    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-24",
            "operation": (
                "ETHICAL_GOAL_PATH_AND_REVERIFICATION_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "batch_id": batch["batch_id"],
            "case_count": batch["case_count"],
            "goal_preserved_count": batch["goal_preserved_count"],
            "path_change_required_count": (
                batch["path_change_required_count"]
            ),
            "path_changed_count": batch["path_changed_count"],
            "goal_reverification_pending_count": (
                batch["goal_reverification_pending_count"]
            ),
            "goal_reconsideration_required_count": (
                batch["goal_reconsideration_required_count"]
            ),
            "goal_abandoned_due_to_path_failure_count": 0,
            "external_action_executed": False,
        }
    )

    outputs["DNA-24"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "ethical_persistence_contract": deepcopy(
            ETHICAL_PERSISTENCE_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "case_count": batch["case_count"],
        "goal_preserved_count": batch["goal_preserved_count"],
        "path_change_required_count": (
            batch["path_change_required_count"]
        ),
        "path_changed_count": batch["path_changed_count"],
        "goal_reverification_pending_count": (
            batch["goal_reverification_pending_count"]
        ),
        "goal_reconsideration_required_count": (
            batch["goal_reconsideration_required_count"]
        ),
        "all_cases_continue_eligible": (
            batch["all_cases_continue_eligible"]
        ),
        "goal_abandoned_due_to_path_failure_count": 0,
        "goal_executed_by_dna24": False,
        "path_executed_by_dna24": False,
        "learning_runtime_started": False,
        "world_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna24(core54: Core54Like) -> None:
    core = core54.get("DNA-24")
    assert_exact_canon(core)
    core54.bind(
        "DNA-24",
        dna24_ethical_persistence,
    )


def _through_dna23(core54: Core54Like) -> Dict[str, Any]:
    from SIGMA_DNA_23_COGNITIVE_FREEDOM import (
        _through_dna22,
        _valid_freedom_cases,
    )

    through_dna22 = _through_dna22(core54)
    through_dna22["cognitive_freedom_cases"] = (
        _valid_freedom_cases()
    )
    return core54.get("DNA-23").activate(
        through_dna22
    )


def _ethical_assessment(
    *,
    aligned: bool = True,
    label: str = "INITIAL",
) -> Dict[str, Any]:
    return {
        "consequences_beneficial": aligned,
        "dignity_preserved": aligned,
        "autonomy_preserved": aligned,
        "non_bullying": aligned,
        "non_manipulation": aligned,
        "non_coercion": aligned,
        "evidence": [
            {
                "evidence_id": f"DNA24-{label}-ETHICS-EVIDENCE",
                "observation": (
                    "ALL_DNA05_ETHICAL_DIMENSIONS_ALIGNED"
                    if aligned
                    else "ETHICAL_DIMENSION_CONTRADICTION_FOUND"
                ),
            }
        ],
    }


def _valid_case() -> Dict[str, Any]:
    return {
        "case_id": "DNA24-CASE-VALID",
        "goal_id": "GOAL-DNA24-01",
        "goal": {
            "statement": "PURSUE_VERIFIED_HUMAN_BENEFIT",
        },
        "initial_ethical_assessment": _ethical_assessment(
            aligned=True,
            label="INITIAL",
        ),
        "path_failed": True,
        "current_path": {
            "path_id": "PATH-A",
            "method": "METHOD-A",
        },
        "next_path": {
            "path_id": "PATH-B",
            "method": "METHOD-B",
        },
        "goal_reverification": {
            "required": True,
            "performed": True,
            "ethical_assessment": _ethical_assessment(
                aligned=True,
                label="REVERIFIED",
            ),
        },
    }


def self_check_dna24(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 24):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna24_core = core54.get("DNA-24")
    assert_exact_canon(dna24_core)
    bind_dna24(core54)

    through_dna23 = _through_dna23(core54)
    through_dna23_snapshot = deepcopy(through_dna23)

    state_before = through_dna23["cognitive_state"]
    pre_dependencies = {
        key: deepcopy(state_before[key])
        for key in (
            "ethical_intelligence",
            "persistent_existence",
            "persistence_engine",
            "truth_protocol",
            "cognitive_freedom",
        )
    }
    pre_provenance_count = len(
        state_before["provenance"]
    )

    valid_input = deepcopy(through_dna23)
    valid_input["ethical_persistence_cases"] = [
        _valid_case()
    ]
    result = dna24_core.activate(valid_input)

    assert through_dna23 == through_dna23_snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 25)
    ]

    dna24 = result["core54_outputs"]["DNA-24"]
    assert dna24["canonical_gene"] == CANON_DNA24
    assert dna24["ethical_persistence_contract"] == (
        ETHICAL_PERSISTENCE_CONTRACT
    )
    assert dna24["case_count"] == 1
    assert dna24["goal_preserved_count"] == 1
    assert dna24["path_change_required_count"] == 1
    assert dna24["path_changed_count"] == 1
    assert dna24["goal_reverification_pending_count"] == 0
    assert dna24["goal_reconsideration_required_count"] == 0
    assert dna24["all_cases_continue_eligible"] is True
    assert dna24[
        "goal_abandoned_due_to_path_failure_count"
    ] == 0
    assert dna24["goal_executed_by_dna24"] is False
    assert dna24["path_executed_by_dna24"] is False
    assert dna24["learning_runtime_started"] is False
    assert dna24["world_runtime_started"] is False
    assert dna24["external_action_executed"] is False
    assert dna24["status"] == "CANON_ALIGNED"

    evaluation = dna24["evaluation"]
    record = evaluation["records"][0]
    batch = evaluation["batch"]

    assert record["case_id"] == "DNA24-CASE-VALID"
    assert record["ethical_goal_confirmed"] is True
    assert record["path_failed"] is True
    assert record["path_changed"] is True
    assert record["failed_path_repeated"] is False
    assert record["change_path_required"] is True
    assert record["goal_continuity_preserved"] is True
    assert record[
        "goal_abandoned_due_to_path_failure"
    ] is False
    assert record["goal_reconsideration_required"] is False
    assert record["continue_eligible"] is True
    assert record["errors"] == []
    assert record["status"] == (
        "ETHICAL_GOAL_PRESERVED_PATH_CHANGED"
    )
    assert record[
        "effective_ethical_assessment_source"
    ] == "GOAL_REVERIFICATION"
    assert record["goal_reverification"]["status"] == (
        "GOAL_REVERIFICATION_PASSED"
    )

    assert batch["batch_id"] == "DNA-24-BATCH-0001"
    assert batch["case_count"] == 1
    assert batch["continue_eligible_count"] == 1
    assert batch["goal_preserved_count"] == 1
    assert batch["path_change_required_count"] == 1
    assert batch["path_changed_count"] == 1
    assert batch["goal_reverification_required_count"] == 1
    assert batch["goal_reverification_pending_count"] == 0
    assert batch["goal_reconsideration_required_count"] == 0
    assert batch["failed_path_repetition_count"] == 0
    assert batch["incomplete_count"] == 0
    assert batch["all_cases_continue_eligible"] is True
    assert batch["status"] == "ETHICAL_PERSISTENCE_ALIGNED"

    state = result["cognitive_state"]
    ethical_persistence = state["ethical_persistence"]
    assert ethical_persistence["contract"] == (
        ETHICAL_PERSISTENCE_CONTRACT
    )
    assert ethical_persistence["records"] == [record]
    assert ethical_persistence["batches"] == [batch]
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-24"
    assert contract_event["operation"] == (
        "ETHICAL_PERSISTENCE_CONTRACT_ESTABLISHED"
    )
    assert contract_event[
        "failed_path_abandons_ethical_goal"
    ] is False
    assert contract_event["external_action_executed"] is False

    evaluation_event = state["provenance"][-1]
    assert evaluation_event["core_id"] == "DNA-24"
    assert evaluation_event["operation"] == (
        "ETHICAL_GOAL_PATH_AND_REVERIFICATION_EVALUATED"
    )
    assert evaluation_event["case_count"] == 1
    assert evaluation_event["goal_preserved_count"] == 1
    assert evaluation_event["path_changed_count"] == 1
    assert evaluation_event[
        "goal_abandoned_due_to_path_failure_count"
    ] == 0

    for key, expected in pre_dependencies.items():
        assert state[key] == expected

    # A confirmed ethical goal must remain preserved while a new path is
    # still being selected.
    no_next_path_input = deepcopy(through_dna23)
    no_next_path_case = _valid_case()
    no_next_path_case["case_id"] = "DNA24-NEXT-PATH-PENDING"
    no_next_path_case["next_path"] = None
    no_next_path_case["goal_reverification"] = {
        "required": False,
        "performed": False,
    }
    no_next_path_input["ethical_persistence_cases"] = [
        no_next_path_case
    ]
    no_next_path = dna24_core.activate(no_next_path_input)
    no_next_record = no_next_path[
        "core54_outputs"
    ]["DNA-24"]["evaluation"]["records"][0]
    assert no_next_record["ethical_goal_confirmed"] is True
    assert no_next_record["goal_continuity_preserved"] is True
    assert no_next_record["change_path_required"] is True
    assert no_next_record["path_changed"] is False
    assert no_next_record["continue_eligible"] is False
    assert no_next_record["status"] == (
        "ETHICAL_GOAL_PRESERVED_CHANGE_PATH_REQUIRED"
    )

    # Repeating the failed path is not a path change.
    repeated_input = deepcopy(through_dna23)
    repeated_case = _valid_case()
    repeated_case["case_id"] = "DNA24-REPEATED-PATH"
    repeated_case["next_path"] = deepcopy(
        repeated_case["current_path"]
    )
    repeated_case["goal_reverification"] = {
        "required": False,
        "performed": False,
    }
    repeated_input["ethical_persistence_cases"] = [
        repeated_case
    ]
    repeated = dna24_core.activate(repeated_input)
    repeated_record = repeated[
        "core54_outputs"
    ]["DNA-24"]["evaluation"]["records"][0]
    assert repeated_record["failed_path_repeated"] is True
    assert repeated_record["path_changed"] is False
    assert repeated_record["continue_eligible"] is False
    assert repeated_record["status"] == (
        "FAILED_PATH_REPETITION_REJECTED"
    )

    # Required goal re-verification pauses continuation but does not abandon
    # the goal because of path failure.
    pending_input = deepcopy(through_dna23)
    pending_case = _valid_case()
    pending_case["case_id"] = "DNA24-REVERIFY-PENDING"
    pending_case["goal_reverification"] = {
        "required": True,
        "performed": False,
    }
    pending_input["ethical_persistence_cases"] = [
        pending_case
    ]
    pending = dna24_core.activate(pending_input)
    pending_record = pending[
        "core54_outputs"
    ]["DNA-24"]["evaluation"]["records"][0]
    assert pending_record["ethical_goal_confirmed"] is False
    assert pending_record["goal_continuity_preserved"] is True
    assert pending_record[
        "goal_abandoned_due_to_path_failure"
    ] is False
    assert pending_record["continue_eligible"] is False
    assert pending_record["status"] == (
        "GOAL_REVERIFICATION_REQUIRED"
    )

    # Failed re-verification requires goal reconsideration rather than blind
    # persistence.
    failed_reverify_input = deepcopy(through_dna23)
    failed_reverify_case = _valid_case()
    failed_reverify_case["case_id"] = "DNA24-REVERIFY-FAILED"
    failed_reverify_case["goal_reverification"] = {
        "required": True,
        "performed": True,
        "ethical_assessment": _ethical_assessment(
            aligned=False,
            label="REVERIFICATION-FAILED",
        ),
    }
    failed_reverify_input["ethical_persistence_cases"] = [
        failed_reverify_case
    ]
    failed_reverify = dna24_core.activate(
        failed_reverify_input
    )
    failed_reverify_record = failed_reverify[
        "core54_outputs"
    ]["DNA-24"]["evaluation"]["records"][0]
    assert failed_reverify_record["ethical_goal_confirmed"] is False
    assert failed_reverify_record[
        "goal_reconsideration_required"
    ] is True
    assert failed_reverify_record[
        "goal_continuity_preserved"
    ] is False
    assert failed_reverify_record["continue_eligible"] is False
    assert failed_reverify_record["status"] == (
        "GOAL_RECONSIDERATION_REQUIRED"
    )

    # A goal that is not ethically aligned must not be preserved merely in
    # the name of persistence.
    non_ethical_input = deepcopy(through_dna23)
    non_ethical_case = _valid_case()
    non_ethical_case["case_id"] = "DNA24-NON-ETHICAL-GOAL"
    non_ethical_case["initial_ethical_assessment"] = (
        _ethical_assessment(
            aligned=False,
            label="INITIAL-NON-ETHICAL",
        )
    )
    non_ethical_case["goal_reverification"] = {
        "required": False,
        "performed": False,
    }
    non_ethical_input["ethical_persistence_cases"] = [
        non_ethical_case
    ]
    non_ethical = dna24_core.activate(non_ethical_input)
    non_ethical_record = non_ethical[
        "core54_outputs"
    ]["DNA-24"]["evaluation"]["records"][0]
    assert non_ethical_record["ethical_goal_confirmed"] is False
    assert non_ethical_record[
        "goal_reconsideration_required"
    ] is True
    assert non_ethical_record["continue_eligible"] is False
    assert non_ethical_record["status"] == (
        "GOAL_RECONSIDERATION_REQUIRED"
    )

    # If the path has not failed, a confirmed ethical goal continues without
    # requiring an artificial path change.
    no_failure_input = deepcopy(through_dna23)
    no_failure_case = _valid_case()
    no_failure_case["case_id"] = "DNA24-NO-PATH-FAILURE"
    no_failure_case["path_failed"] = False
    no_failure_case["next_path"] = None
    no_failure_case["goal_reverification"] = {
        "required": False,
        "performed": False,
    }
    no_failure_input["ethical_persistence_cases"] = [
        no_failure_case
    ]
    no_failure = dna24_core.activate(no_failure_input)
    no_failure_record = no_failure[
        "core54_outputs"
    ]["DNA-24"]["evaluation"]["records"][0]
    assert no_failure_record["change_path_required"] is False
    assert no_failure_record["continue_eligible"] is True
    assert no_failure_record["status"] == (
        "ETHICAL_GOAL_CONTINUES"
    )

    # Missing ethical evidence must never be invented.
    missing_evidence_input = deepcopy(through_dna23)
    missing_evidence_case = _valid_case()
    missing_evidence_case["case_id"] = "DNA24-MISSING-EVIDENCE"
    missing_evidence_case[
        "initial_ethical_assessment"
    ]["evidence"] = []
    missing_evidence_case["goal_reverification"] = {
        "required": False,
        "performed": False,
    }
    missing_evidence_input["ethical_persistence_cases"] = [
        missing_evidence_case
    ]
    missing_evidence = dna24_core.activate(
        missing_evidence_input
    )
    missing_record = missing_evidence[
        "core54_outputs"
    ]["DNA-24"]["evaluation"]["records"][0]
    assert missing_record["continue_eligible"] is False
    assert (
        "INITIAL_GOAL_ETHICAL_EVIDENCE_REQUIRED"
        in missing_record["errors"]
    )
    assert missing_record["status"] == (
        "ETHICAL_PERSISTENCE_INPUT_INCOMPLETE"
    )

    # Strong typing and unique case identity are mandatory.
    invalid_bool_input = deepcopy(through_dna23)
    invalid_bool_case = _valid_case()
    invalid_bool_case["path_failed"] = "YES"
    invalid_bool_input["ethical_persistence_cases"] = [
        invalid_bool_case
    ]
    try:
        dna24_core.activate(invalid_bool_input)
    except TypeError as exc:
        assert str(exc) == (
            "ethical_persistence_case['path_failed'] must be a bool"
        )
    else:
        raise AssertionError(
            "DNA-24_ACCEPTED_NON_BOOLEAN_PATH_FAILURE"
        )

    duplicate_input = deepcopy(through_dna23)
    duplicate_case = _valid_case()
    duplicate_input["ethical_persistence_cases"] = [
        deepcopy(duplicate_case),
        deepcopy(duplicate_case),
    ]
    try:
        dna24_core.activate(duplicate_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-24_DUPLICATE_ETHICAL_PERSISTENCE_CASE_ID"
        )
    else:
        raise AssertionError(
            "DNA-24_ACCEPTED_DUPLICATE_CASE_ID"
        )

    # Reject the provisional CHANGE_PATH marker as the official contract.
    assert "requests" not in result
    assert "flags" not in result
    assert "blocks" not in result
    assert "CHANGE_PATH" not in result

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
        "core_id": "DNA-24",
        "canon_mapping": "PASS",
        "ethical_goal_preservation": "PASS",
        "failed_path_change": "PASS",
        "goal_reverification": "PASS",
        "blind_persistence_rejected": "PASS",
        "failed_path_repetition_rejected": "PASS",
        "goal_abandoned_due_to_path_failure": False,
        "goal_executed_by_dna24": False,
        "path_executed_by_dna24": False,
        "learning_runtime_used": False,
        "world_runtime_used": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-25"
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
            print("DNA-24_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = _load_prior_modules()
    except Exception as exc:
        print("DNA-24_FAIL: IMPORT_ERROR")
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

        for index in range(1, 24):
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

        report = self_check_dna24(
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
            for index in range(1, 25)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-24_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-24_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_24_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "ETHICAL_GOAL_PRESERVATION:",
        report["ethical_goal_preservation"],
    )
    print(
        "FAILED_PATH_CHANGE:",
        report["failed_path_change"],
    )
    print(
        "GOAL_REVERIFICATION:",
        report["goal_reverification"],
    )
    print(
        "BLIND_PERSISTENCE_REJECTED:",
        report["blind_persistence_rejected"],
    )
    print(
        "FAILED_PATH_REPETITION_REJECTED:",
        report["failed_path_repetition_rejected"],
    )
    print(
        "GOAL_ABANDONED_DUE_TO_PATH_FAILURE:",
        report["goal_abandoned_due_to_path_failure"],
    )
    print(
        "GOAL_EXECUTED_BY_DNA24:",
        report["goal_executed_by_dna24"],
    )
    print(
        "PATH_EXECUTED_BY_DNA24:",
        report["path_executed_by_dna24"],
    )
    print(
        "LEARNING_RUNTIME_USED:",
        report["learning_runtime_used"],
    )
    print(
        "WORLD_RUNTIME_USED:",
        report["world_runtime_used"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 24/54")
    print("NEXT_AUTHORIZED: DNA-25")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
