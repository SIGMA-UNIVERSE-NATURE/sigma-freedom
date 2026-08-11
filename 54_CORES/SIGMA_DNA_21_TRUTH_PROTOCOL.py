#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-21: TRUTH PROTOCOL
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_21_TRUTH_PROTOCOL.py
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

CANON_DNA21: Dict[str, str] = {
    "id": "DNA-21",
    "name": "Truth Protocol",
    "purpose": (
        "Truth > eloquence; evidence > confidence; "
        "correction > ego."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
UNCERTAINTY_FIRST_CLASS_SCHEMA = (
    "SIGMA_UNCERTAINTY_FIRST_CLASS_DATA_V1"
)
TRUTH_PROTOCOL_SCHEMA = "SIGMA_TRUTH_PROTOCOL_V1"

EVIDENCE_RELATIONS = [
    "SUPPORTS",
    "CONTRADICTS",
    "NEUTRAL",
]

EGO_PREFERENCES = [
    "KEEP_ORIGINAL",
    "ACCEPT_CORRECTION",
    "NONE",
]

TRUTH_PROTOCOL_CASE_FIELDS = [
    "case_id",
    "conclusion_id",
    "evidence",
]

CORRECTION_FIELDS = [
    "corrected_conclusion",
    "reason",
    "evidence_ids",
]

TRUTH_PROTOCOL_CONTRACT: Dict[str, Any] = {
    "schema": TRUTH_PROTOCOL_SCHEMA,
    "precedence_rules": [
        {
            "higher": "TRUTH",
            "lower": "ELOQUENCE",
        },
        {
            "higher": "EVIDENCE",
            "lower": "CONFIDENCE",
        },
        {
            "higher": "CORRECTION",
            "lower": "EGO",
        },
    ],
    "input_path": "truth_protocol_cases",
    "dna20_conclusion_binding_required": True,
    "verified_evidence_required_for_resolution": True,
    "evidence_relations": deepcopy(EVIDENCE_RELATIONS),
    "eloquence_is_not_truth_evidence": True,
    "confidence_is_not_truth_evidence": True,
    "correction_requires_verified_contradicting_evidence": True,
    "valid_correction_overrides_ego_preference": True,
    "original_conclusion_preserved_for_audit": True,
    "missing_evidence_is_not_invented": True,
    "truth_established_by_dna21": False,
    "knowledge_promoted_by_dna21": False,
    "external_verifier_invoked": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA20_UNCERTAINTY_BINDING"
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
    if actual != CANON_DNA21:
        raise RuntimeError(
            "DNA-21_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA21,
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
    Dict[str, Dict[str, Any]],
]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-21_UNIFIED_STATE_SCHEMA_MISMATCH:"
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
        raise RuntimeError(
            "DNA-20_UNCERTAINTY_STATE_REQUIRED"
        )

    first_class = uncertainty.get("first_class_data")
    if not isinstance(first_class, dict):
        raise RuntimeError(
            "DNA-20_FIRST_CLASS_UNCERTAINTY_REQUIRED"
        )

    contract = first_class.get("contract")
    if not isinstance(contract, dict):
        raise RuntimeError(
            "DNA-20_UNCERTAINTY_CONTRACT_REQUIRED"
        )

    if contract.get("schema") != (
        UNCERTAINTY_FIRST_CLASS_SCHEMA
    ):
        raise ValueError(
            "DNA-21_UNCERTAINTY_SCHEMA_MISMATCH:"
            f"{contract.get('schema')!r}"
        )

    records = first_class.get("records")
    if not isinstance(records, list):
        raise TypeError(
            "first_class_data['records'] must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-20_OUTPUT_REQUIRED")

    dna20_output = outputs.get("DNA-20")
    if not isinstance(dna20_output, dict):
        raise RuntimeError("DNA-20_OUTPUT_REQUIRED")

    conclusion_index: Dict[str, Dict[str, Any]] = {}
    for record in records:
        if not isinstance(record, dict):
            raise TypeError(
                "DNA-20 uncertainty record must be a dict"
            )
        conclusion_id = record.get("conclusion_id")
        if not _non_empty_text(conclusion_id):
            continue
        if conclusion_id in conclusion_index:
            raise ValueError(
                "DNA-21_AMBIGUOUS_DNA20_CONCLUSION_ID:"
                f"{conclusion_id}"
            )
        conclusion_index[conclusion_id] = record

    return state, first_class, conclusion_index


def _install_truth_protocol_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("truth_protocol")

    expected = {
        "contract": deepcopy(TRUTH_PROTOCOL_CONTRACT),
        "records": [],
        "batches": [],
    }

    if existing is None:
        state["truth_protocol"] = expected
        return state["truth_protocol"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['truth_protocol'] must be a dict"
        )

    if existing.get("contract") != TRUTH_PROTOCOL_CONTRACT:
        raise ValueError(
            "DNA-21_TRUTH_PROTOCOL_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("records"), list):
        raise TypeError(
            "truth_protocol['records'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "truth_protocol['batches'] must be a list"
        )

    return existing


def _validate_case_types(case: Dict[str, Any]) -> None:
    for field in (
        "case_id",
        "conclusion_id",
        "ego_preference",
    ):
        if field in case and not isinstance(
            case[field],
            str,
        ):
            raise TypeError(
                f"truth_protocol_case['{field}'] must be a string"
            )

    if "evidence" in case and not isinstance(
        case["evidence"],
        list,
    ):
        raise TypeError(
            "truth_protocol_case['evidence'] must be a list"
        )

    if "correction" in case and (
        case["correction"] is not None
        and not isinstance(case["correction"], dict)
    ):
        raise TypeError(
            "truth_protocol_case['correction'] must be a dict or None"
        )


def _normalize_evidence(
    supplied: Any,
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    if not isinstance(supplied, list):
        raise TypeError(
            "truth_protocol_case['evidence'] must be a list"
        )

    evidence_ids: List[str] = []
    records: List[Dict[str, Any]] = []

    for index, item in enumerate(supplied, start=1):
        if not isinstance(item, dict):
            raise TypeError(
                "truth_protocol evidence item must be a dict"
            )

        evidence_id = item.get("evidence_id")
        relation = item.get("relation")
        independently_verified = item.get(
            "independently_verified"
        )
        content_present = (
            "content" in item
            and item.get("content") is not None
        )

        if not _non_empty_text(evidence_id):
            raise ValueError(
                "DNA-21_EVIDENCE_ID_REQUIRED"
            )

        if evidence_id in evidence_ids:
            raise ValueError(
                "DNA-21_DUPLICATE_EVIDENCE_ID:"
                f"{evidence_id}"
            )
        evidence_ids.append(evidence_id)

        if not isinstance(relation, str):
            raise TypeError(
                "truth_protocol evidence relation must be a string"
            )

        relation = relation.strip().upper()
        if relation not in EVIDENCE_RELATIONS:
            raise ValueError(
                "DNA-21_EVIDENCE_RELATION_INVALID:"
                f"{relation}"
            )

        if not isinstance(independently_verified, bool):
            raise TypeError(
                "truth_protocol evidence "
                "independently_verified must be a bool"
            )

        if not content_present:
            raise ValueError(
                "DNA-21_EVIDENCE_CONTENT_REQUIRED"
            )

        records.append(
            {
                "sequence": index,
                "evidence_id": evidence_id,
                "relation": relation,
                "independently_verified": (
                    independently_verified
                ),
                "content": deepcopy(item["content"]),
                "source": deepcopy(item.get("source")),
                "counted_for_resolution": (
                    independently_verified
                    and relation in {
                        "SUPPORTS",
                        "CONTRADICTS",
                    }
                ),
            }
        )

    verified_support = [
        item
        for item in records
        if item["independently_verified"]
        and item["relation"] == "SUPPORTS"
    ]
    verified_contradiction = [
        item
        for item in records
        if item["independently_verified"]
        and item["relation"] == "CONTRADICTS"
    ]
    verified_neutral = [
        item
        for item in records
        if item["independently_verified"]
        and item["relation"] == "NEUTRAL"
    ]
    unverified = [
        item
        for item in records
        if not item["independently_verified"]
    ]

    if verified_support and verified_contradiction:
        status = "CONFLICTING_VERIFIED_EVIDENCE"
    elif verified_contradiction:
        status = "CONTRADICTED_BY_VERIFIED_EVIDENCE"
    elif verified_support:
        status = "SUPPORTED_BY_VERIFIED_EVIDENCE"
    else:
        status = "INSUFFICIENT_VERIFIED_EVIDENCE"

    summary = {
        "evidence_count": len(records),
        "verified_support_count": len(verified_support),
        "verified_contradiction_count": len(
            verified_contradiction
        ),
        "verified_neutral_count": len(verified_neutral),
        "unverified_count": len(unverified),
        "verified_support_ids": [
            item["evidence_id"]
            for item in verified_support
        ],
        "verified_contradiction_ids": [
            item["evidence_id"]
            for item in verified_contradiction
        ],
        "status": status,
    }

    return records, summary


def _evaluate_correction(
    supplied: Any,
    evidence_records: List[Dict[str, Any]],
) -> Dict[str, Any]:
    if supplied is None:
        return {
            "supplied": False,
            "record": None,
            "valid": False,
            "errors": [],
            "bound_verified_contradiction_ids": [],
        }

    if not isinstance(supplied, dict):
        raise TypeError(
            "truth_protocol_case['correction'] must be a dict or None"
        )

    correction = deepcopy(supplied)
    errors: List[str] = []

    missing = [
        field
        for field in CORRECTION_FIELDS
        if field not in correction
    ]
    if missing:
        errors.append("CORRECTION_FIELDS_MISSING")

    if (
        "corrected_conclusion" not in correction
        or correction.get("corrected_conclusion") is None
    ):
        errors.append("CORRECTED_CONCLUSION_REQUIRED")

    reason = correction.get("reason")
    if not _non_empty_text(reason):
        errors.append("CORRECTION_REASON_REQUIRED")

    evidence_ids = correction.get("evidence_ids")
    if "evidence_ids" in correction and not isinstance(
        evidence_ids,
        list,
    ):
        raise TypeError(
            "correction['evidence_ids'] must be a list"
        )

    if not isinstance(evidence_ids, list) or not evidence_ids:
        errors.append("CORRECTION_EVIDENCE_IDS_REQUIRED")
        evidence_ids = []

    if any(
        not _non_empty_text(evidence_id)
        for evidence_id in evidence_ids
    ):
        raise ValueError(
            "DNA-21_CORRECTION_EVIDENCE_ID_INVALID"
        )

    if len(evidence_ids) != len(set(evidence_ids)):
        raise ValueError(
            "DNA-21_DUPLICATE_CORRECTION_EVIDENCE_ID"
        )

    by_id = {
        record["evidence_id"]: record
        for record in evidence_records
    }

    unknown = [
        evidence_id
        for evidence_id in evidence_ids
        if evidence_id not in by_id
    ]
    if unknown:
        errors.append(
            "CORRECTION_REFERENCES_UNKNOWN_EVIDENCE"
        )

    bound_verified_contradictions = [
        evidence_id
        for evidence_id in evidence_ids
        if evidence_id in by_id
        and by_id[evidence_id]["independently_verified"]
        and by_id[evidence_id]["relation"] == "CONTRADICTS"
    ]

    if evidence_ids and not bound_verified_contradictions:
        errors.append(
            "CORRECTION_REQUIRES_VERIFIED_CONTRADICTING_EVIDENCE"
        )

    unique_errors = list(dict.fromkeys(errors))
    normalized_record = {
        "corrected_conclusion": deepcopy(
            correction.get("corrected_conclusion")
        ),
        "reason": reason,
        "evidence_ids": deepcopy(evidence_ids),
    }

    return {
        "supplied": True,
        "record": normalized_record,
        "valid": not unique_errors,
        "errors": unique_errors,
        "bound_verified_contradiction_ids": (
            bound_verified_contradictions
        ),
    }


def _normalize_case(
    supplied: Any,
    *,
    input_index: int,
    sequence: int,
    conclusion_index: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        return {
            "sequence": sequence,
            "record_id": f"DNA-21-TRUTH-{sequence:04d}",
            "input_index": input_index,
            "case_id": None,
            "conclusion_id": None,
            "original_conclusion": None,
            "original_confidence": None,
            "original_evidence_coverage": None,
            "original_unresolved_uncertainty": None,
            "eloquence": None,
            "ego_preference": "NONE",
            "evidence_records": [],
            "evidence_summary": {
                "evidence_count": 0,
                "verified_support_count": 0,
                "verified_contradiction_count": 0,
                "verified_neutral_count": 0,
                "unverified_count": 0,
                "verified_support_ids": [],
                "verified_contradiction_ids": [],
                "status": "INSUFFICIENT_VERIFIED_EVIDENCE",
            },
            "correction": {
                "supplied": False,
                "record": None,
                "valid": False,
                "errors": [],
                "bound_verified_contradiction_ids": [],
            },
            "correction_applied": False,
            "final_conclusion": None,
            "precedence_enforced": {
                "truth_over_eloquence": True,
                "evidence_over_confidence": True,
                "correction_over_ego": True,
            },
            "eloquence_changed_resolution": False,
            "confidence_changed_evidence_status": False,
            "ego_blocked_valid_correction": False,
            "correction_over_ego_demonstrated": False,
            "protocol_resolved": False,
            "errors": ["TRUTH_PROTOCOL_CASE_MUST_BE_A_DICT"],
            "truth_established": False,
            "knowledge_promoted": False,
            "status": "TRUTH_PROTOCOL_INPUT_INCOMPLETE",
        }

    case = deepcopy(supplied)
    _validate_case_types(case)
    errors: List[str] = []

    missing = [
        field
        for field in TRUTH_PROTOCOL_CASE_FIELDS
        if field not in case
    ]
    if missing:
        errors.append("TRUTH_PROTOCOL_CASE_FIELDS_MISSING")

    case_id = case.get("case_id")
    if not _non_empty_text(case_id):
        errors.append("TRUTH_PROTOCOL_CASE_ID_REQUIRED")

    conclusion_id = case.get("conclusion_id")
    if not _non_empty_text(conclusion_id):
        errors.append("CONCLUSION_ID_REQUIRED")

    conclusion_record = (
        conclusion_index.get(conclusion_id)
        if _non_empty_text(conclusion_id)
        else None
    )
    if conclusion_record is None:
        errors.append("DNA20_CONCLUSION_BINDING_REQUIRED")
    elif conclusion_record.get("complete") is not True:
        errors.append(
            "DNA20_CONCLUSION_UNCERTAINTY_DATA_INCOMPLETE"
        )

    ego_preference = case.get("ego_preference", "NONE")
    ego_preference = ego_preference.strip().upper()
    if ego_preference not in EGO_PREFERENCES:
        raise ValueError(
            "DNA-21_EGO_PREFERENCE_INVALID:"
            f"{ego_preference}"
        )

    evidence_supplied = case.get("evidence", [])
    evidence_records, evidence_summary = (
        _normalize_evidence(evidence_supplied)
    )
    correction = _evaluate_correction(
        case.get("correction"),
        evidence_records,
    )

    original_conclusion = (
        deepcopy(conclusion_record.get("conclusion"))
        if conclusion_record is not None
        else None
    )
    original_confidence = (
        conclusion_record.get("confidence")
        if conclusion_record is not None
        else None
    )
    original_evidence_coverage = (
        conclusion_record.get("evidence_coverage")
        if conclusion_record is not None
        else None
    )
    original_unresolved = (
        deepcopy(
            conclusion_record.get(
                "unresolved_uncertainty"
            )
        )
        if conclusion_record is not None
        else None
    )

    final_conclusion = deepcopy(original_conclusion)
    correction_applied = False
    protocol_resolved = False

    if errors:
        status = "TRUTH_PROTOCOL_INPUT_INCOMPLETE"
    elif evidence_summary["status"] == (
        "SUPPORTED_BY_VERIFIED_EVIDENCE"
    ):
        protocol_resolved = True
        status = "CURRENT_CONCLUSION_EVIDENCE_SUPPORTED"
    elif evidence_summary["status"] == (
        "CONTRADICTED_BY_VERIFIED_EVIDENCE"
    ):
        if correction["valid"]:
            final_conclusion = deepcopy(
                correction["record"]["corrected_conclusion"]
            )
            correction_applied = True
            protocol_resolved = True
            status = "EVIDENCE_BACKED_CORRECTION_APPLIED"
        else:
            status = "EVIDENCE_BACKED_CORRECTION_REQUIRED"
    elif evidence_summary["status"] == (
        "CONFLICTING_VERIFIED_EVIDENCE"
    ):
        status = (
            "CONFLICTING_EVIDENCE_REQUIRES_FURTHER_VERIFICATION"
        )
    else:
        status = "VERIFIED_EVIDENCE_REQUIRED"

    correction_over_ego_demonstrated = bool(
        correction_applied
        and ego_preference == "KEEP_ORIGINAL"
    )

    return {
        "sequence": sequence,
        "record_id": f"DNA-21-TRUTH-{sequence:04d}",
        "input_index": input_index,
        "case_id": case_id,
        "conclusion_id": conclusion_id,
        "original_conclusion": original_conclusion,
        "original_confidence": original_confidence,
        "original_evidence_coverage": (
            original_evidence_coverage
        ),
        "original_unresolved_uncertainty": (
            original_unresolved
        ),
        "eloquence": deepcopy(case.get("eloquence")),
        "ego_preference": ego_preference,
        "evidence_records": evidence_records,
        "evidence_summary": evidence_summary,
        "correction": correction,
        "correction_applied": correction_applied,
        "final_conclusion": final_conclusion,
        "precedence_enforced": {
            "truth_over_eloquence": True,
            "evidence_over_confidence": True,
            "correction_over_ego": True,
        },
        "eloquence_changed_resolution": False,
        "confidence_changed_evidence_status": False,
        "ego_blocked_valid_correction": False,
        "correction_over_ego_demonstrated": (
            correction_over_ego_demonstrated
        ),
        "protocol_resolved": protocol_resolved,
        "errors": list(dict.fromkeys(errors)),
        "truth_established": False,
        "knowledge_promoted": False,
        "status": status,
    }


def _evaluate_truth_protocol_cases(
    supplied: Any,
    registry: Dict[str, Any],
    conclusion_index: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    if supplied is None:
        cases: List[Any] = []
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['truth_protocol_cases'] must be a list"
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
            "DNA-21_DUPLICATE_TRUTH_PROTOCOL_CASE_ID"
        )

    conclusion_ids = [
        item.get("conclusion_id")
        for item in cases
        if isinstance(item, dict)
        and _non_empty_text(item.get("conclusion_id"))
    ]
    if len(conclusion_ids) != len(set(conclusion_ids)):
        raise ValueError(
            "DNA-21_DUPLICATE_CONCLUSION_ID_IN_BATCH"
        )

    start_sequence = len(registry["records"]) + 1
    records = [
        _normalize_case(
            item,
            input_index=index,
            sequence=start_sequence + index - 1,
            conclusion_index=conclusion_index,
        )
        for index, item in enumerate(cases, start=1)
    ]
    registry["records"].extend(deepcopy(records))

    resolved_count = sum(
        1
        for record in records
        if record["protocol_resolved"]
    )
    unresolved_count = len(records) - resolved_count
    correction_applied_count = sum(
        1
        for record in records
        if record["correction_applied"]
    )
    correction_over_ego_count = sum(
        1
        for record in records
        if record["correction_over_ego_demonstrated"]
    )
    incomplete_count = sum(
        1
        for record in records
        if record["errors"]
    )

    if not records:
        status = "NO_TRUTH_PROTOCOL_CASES_SUPPLIED"
    elif unresolved_count:
        status = "TRUTH_PROTOCOL_HAS_UNRESOLVED_CASES"
    else:
        status = "ALL_TRUTH_PROTOCOL_CASES_RESOLVED"

    batch_sequence = len(registry["batches"]) + 1
    batch = {
        "sequence": batch_sequence,
        "batch_id": f"DNA-21-BATCH-{batch_sequence:04d}",
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "case_count": len(records),
        "resolved_count": resolved_count,
        "unresolved_count": unresolved_count,
        "incomplete_count": incomplete_count,
        "correction_applied_count": correction_applied_count,
        "correction_over_ego_count": (
            correction_over_ego_count
        ),
        "truth_over_eloquence_enforced": True,
        "evidence_over_confidence_enforced": True,
        "correction_over_ego_enforced": True,
        "all_cases_protocol_resolved": (
            unresolved_count == 0
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


def dna21_truth_protocol(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Enforce the exact Canon precedence relations:

    - Truth over eloquence.
    - Evidence over confidence.
    - Evidence-backed correction over ego preference.

    DNA-21 evaluates supplied evidence and corrections only. It does not
    invent evidence, establish final truth, promote knowledge, invoke a
    verifier or model, start a higher runtime, execute an external action,
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
    trace.append("DNA-21")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    (
        state,
        _first_class,
        conclusion_index,
    ) = _validate_dependencies(context)
    registry = _install_truth_protocol_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-21",
            "operation": "TRUTH_PROTOCOL_CONTRACT_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "truth_protocol_schema": TRUTH_PROTOCOL_SCHEMA,
            "precedence_rules": deepcopy(
                TRUTH_PROTOCOL_CONTRACT["precedence_rules"]
            ),
            "truth_established": False,
        }
    )

    evaluation = _evaluate_truth_protocol_cases(
        context.get("truth_protocol_cases"),
        registry,
        conclusion_index,
    )
    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-21",
            "operation": "TRUTH_PROTOCOL_PRECEDENCE_ENFORCED",
            "canonical_sha256": canonical_sha256,
            "batch_id": batch["batch_id"],
            "case_count": batch["case_count"],
            "resolved_count": batch["resolved_count"],
            "unresolved_count": batch["unresolved_count"],
            "correction_applied_count": (
                batch["correction_applied_count"]
            ),
            "truth_over_eloquence": True,
            "evidence_over_confidence": True,
            "correction_over_ego": True,
            "truth_established": False,
            "knowledge_promoted": False,
        }
    )

    outputs["DNA-21"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "truth_protocol_contract": deepcopy(
            TRUTH_PROTOCOL_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "case_count": batch["case_count"],
        "resolved_count": batch["resolved_count"],
        "unresolved_count": batch["unresolved_count"],
        "correction_applied_count": (
            batch["correction_applied_count"]
        ),
        "truth_over_eloquence": True,
        "evidence_over_confidence": True,
        "correction_over_ego": True,
        "truth_established": False,
        "knowledge_promoted": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna21(core54: Core54Like) -> None:
    core = core54.get("DNA-21")
    assert_exact_canon(core)
    core54.bind(
        "DNA-21",
        dna21_truth_protocol,
    )


def _through_dna20(
    core54: Core54Like,
    *,
    conclusion_id: str,
    conclusion: Any,
    confidence: float,
    evidence_coverage: float,
    unresolved_uncertainty: List[Any],
) -> Dict[str, Any]:
    from SIGMA_DNA_20_UNCERTAINTY_AS_FIRST_CLASS_DATA import (
        _complete_through_dna19,
    )

    through_dna19, _claim = _complete_through_dna19(
        core54
    )
    through_dna19["important_conclusions"] = [
        {
            "conclusion_id": conclusion_id,
            "conclusion": deepcopy(conclusion),
            "confidence": confidence,
            "evidence_coverage": evidence_coverage,
            "unresolved_uncertainty": deepcopy(
                unresolved_uncertainty
            ),
        }
    ]
    return core54.get("DNA-20").activate(
        through_dna19
    )


def self_check_dna21(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 21):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna21_core = core54.get("DNA-21")
    assert_exact_canon(dna21_core)
    bind_dna21(core54)

    original_conclusion = {
        "statement": "ORIGINAL_CLAIM",
        "version": 1,
    }
    corrected_conclusion = {
        "statement": "EVIDENCE_CORRECTED_CLAIM",
        "version": 2,
    }

    through_dna20 = _through_dna20(
        core54,
        conclusion_id="DNA21-CONCLUSION-01",
        conclusion=original_conclusion,
        confidence=0.99,
        evidence_coverage=0.80,
        unresolved_uncertainty=[
            "EXTERNAL_REALITY_CHECK_REQUIRED",
        ],
    )
    through_dna20_snapshot = deepcopy(through_dna20)

    pre_uncertainty = deepcopy(
        through_dna20["cognitive_state"]["uncertainty"]
    )
    pre_provenance_count = len(
        through_dna20["cognitive_state"]["provenance"]
    )

    valid_case = {
        "case_id": "DNA21-CASE-01",
        "conclusion_id": "DNA21-CONCLUSION-01",
        "eloquence": {
            "score": 1.0,
            "description": "MAXIMUM_RHETORICAL_POLISH",
        },
        "ego_preference": "KEEP_ORIGINAL",
        "evidence": [
            {
                "evidence_id": "DNA21-EVIDENCE-01",
                "relation": "CONTRADICTS",
                "independently_verified": True,
                "content": {
                    "observation": (
                        "ORIGINAL_CLAIM_CONTRADICTED"
                    ),
                },
                "source": "INDEPENDENT_VERIFIER",
            }
        ],
        "correction": {
            "corrected_conclusion": corrected_conclusion,
            "reason": "VERIFIED_EVIDENCE_CONTRADICTS_ORIGINAL",
            "evidence_ids": ["DNA21-EVIDENCE-01"],
        },
    }

    valid_input = deepcopy(through_dna20)
    valid_input["truth_protocol_cases"] = [valid_case]
    result = dna21_core.activate(valid_input)

    assert through_dna20 == through_dna20_snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 22)
    ]

    dna21 = result["core54_outputs"]["DNA-21"]
    assert dna21["canonical_gene"] == CANON_DNA21
    assert dna21["truth_protocol_contract"] == (
        TRUTH_PROTOCOL_CONTRACT
    )
    assert dna21["case_count"] == 1
    assert dna21["resolved_count"] == 1
    assert dna21["unresolved_count"] == 0
    assert dna21["correction_applied_count"] == 1
    assert dna21["truth_over_eloquence"] is True
    assert dna21["evidence_over_confidence"] is True
    assert dna21["correction_over_ego"] is True
    assert dna21["truth_established"] is False
    assert dna21["knowledge_promoted"] is False
    assert dna21["status"] == "CANON_ALIGNED"

    evaluation = dna21["evaluation"]
    batch = evaluation["batch"]
    records = evaluation["records"]
    assert len(records) == 1
    record = records[0]

    assert record["record_id"] == "DNA-21-TRUTH-0001"
    assert record["case_id"] == "DNA21-CASE-01"
    assert record["conclusion_id"] == (
        "DNA21-CONCLUSION-01"
    )
    assert record["original_conclusion"] == (
        original_conclusion
    )
    assert record["original_confidence"] == 0.99
    assert record["original_evidence_coverage"] == 0.80
    assert record["evidence_summary"]["status"] == (
        "CONTRADICTED_BY_VERIFIED_EVIDENCE"
    )
    assert record["correction"]["valid"] is True
    assert record["correction_applied"] is True
    assert record["final_conclusion"] == corrected_conclusion
    assert record["ego_preference"] == "KEEP_ORIGINAL"
    assert (
        record["correction_over_ego_demonstrated"]
        is True
    )
    assert record["eloquence_changed_resolution"] is False
    assert (
        record["confidence_changed_evidence_status"]
        is False
    )
    assert record["ego_blocked_valid_correction"] is False
    assert record["protocol_resolved"] is True
    assert record["errors"] == []
    assert record["truth_established"] is False
    assert record["knowledge_promoted"] is False
    assert record["status"] == (
        "EVIDENCE_BACKED_CORRECTION_APPLIED"
    )

    assert batch["batch_id"] == "DNA-21-BATCH-0001"
    assert batch["record_ids"] == ["DNA-21-TRUTH-0001"]
    assert batch["case_count"] == 1
    assert batch["resolved_count"] == 1
    assert batch["unresolved_count"] == 0
    assert batch["incomplete_count"] == 0
    assert batch["correction_applied_count"] == 1
    assert batch["correction_over_ego_count"] == 1
    assert batch["truth_over_eloquence_enforced"] is True
    assert batch["evidence_over_confidence_enforced"] is True
    assert batch["correction_over_ego_enforced"] is True
    assert batch["all_cases_protocol_resolved"] is True
    assert batch["truth_established"] is False
    assert batch["knowledge_promoted"] is False
    assert batch["status"] == (
        "ALL_TRUTH_PROTOCOL_CASES_RESOLVED"
    )

    state = result["cognitive_state"]
    truth_protocol = state["truth_protocol"]
    assert truth_protocol["contract"] == TRUTH_PROTOCOL_CONTRACT
    assert truth_protocol["records"] == records
    assert truth_protocol["batches"] == [batch]
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-21"
    assert contract_event["operation"] == (
        "TRUTH_PROTOCOL_CONTRACT_ESTABLISHED"
    )
    assert contract_event["precedence_rules"] == (
        TRUTH_PROTOCOL_CONTRACT["precedence_rules"]
    )
    assert contract_event["truth_established"] is False

    enforcement_event = state["provenance"][-1]
    assert enforcement_event["core_id"] == "DNA-21"
    assert enforcement_event["operation"] == (
        "TRUTH_PROTOCOL_PRECEDENCE_ENFORCED"
    )
    assert enforcement_event["batch_id"] == (
        "DNA-21-BATCH-0001"
    )
    assert enforcement_event["case_count"] == 1
    assert enforcement_event["resolved_count"] == 1
    assert enforcement_event["unresolved_count"] == 0
    assert enforcement_event["correction_applied_count"] == 1
    assert enforcement_event["truth_over_eloquence"] is True
    assert enforcement_event["evidence_over_confidence"] is True
    assert enforcement_event["correction_over_ego"] is True
    assert enforcement_event["truth_established"] is False
    assert enforcement_event["knowledge_promoted"] is False

    # DNA-21 must not mutate DNA-20 uncertainty records.
    assert state["uncertainty"] == pre_uncertainty

    # Maximum confidence and eloquence cannot replace verified evidence.
    no_evidence_input = deepcopy(through_dna20)
    no_evidence_input["truth_protocol_cases"] = [
        {
            "case_id": "DNA21-NO-EVIDENCE",
            "conclusion_id": "DNA21-CONCLUSION-01",
            "eloquence": {"score": 1.0},
            "ego_preference": "KEEP_ORIGINAL",
            "evidence": [],
        }
    ]
    no_evidence = dna21_core.activate(no_evidence_input)
    no_evidence_record = no_evidence[
        "core54_outputs"
    ]["DNA-21"]["evaluation"]["records"][0]
    assert no_evidence_record["original_confidence"] == 0.99
    assert no_evidence_record["evidence_summary"]["status"] == (
        "INSUFFICIENT_VERIFIED_EVIDENCE"
    )
    assert no_evidence_record["protocol_resolved"] is False
    assert no_evidence_record["status"] == (
        "VERIFIED_EVIDENCE_REQUIRED"
    )

    # Unverified evidence must not count as evidence for resolution.
    unverified_input = deepcopy(through_dna20)
    unverified_input["truth_protocol_cases"] = [
        {
            "case_id": "DNA21-UNVERIFIED",
            "conclusion_id": "DNA21-CONCLUSION-01",
            "evidence": [
                {
                    "evidence_id": "DNA21-U-01",
                    "relation": "SUPPORTS",
                    "independently_verified": False,
                    "content": "UNVERIFIED_SUPPORT",
                }
            ],
        }
    ]
    unverified = dna21_core.activate(unverified_input)
    unverified_record = unverified[
        "core54_outputs"
    ]["DNA-21"]["evaluation"]["records"][0]
    assert unverified_record["evidence_summary"] == {
        "evidence_count": 1,
        "verified_support_count": 0,
        "verified_contradiction_count": 0,
        "verified_neutral_count": 0,
        "unverified_count": 1,
        "verified_support_ids": [],
        "verified_contradiction_ids": [],
        "status": "INSUFFICIENT_VERIFIED_EVIDENCE",
    }
    assert unverified_record["protocol_resolved"] is False

    # Verified support resolves to the current conclusion, independent of style.
    support_input = deepcopy(through_dna20)
    support_input["truth_protocol_cases"] = [
        {
            "case_id": "DNA21-SUPPORT",
            "conclusion_id": "DNA21-CONCLUSION-01",
            "eloquence": {"score": 0.0},
            "evidence": [
                {
                    "evidence_id": "DNA21-S-01",
                    "relation": "SUPPORTS",
                    "independently_verified": True,
                    "content": "VERIFIED_SUPPORT",
                }
            ],
        }
    ]
    support = dna21_core.activate(support_input)
    support_record = support[
        "core54_outputs"
    ]["DNA-21"]["evaluation"]["records"][0]
    assert support_record["protocol_resolved"] is True
    assert support_record["correction_applied"] is False
    assert support_record["final_conclusion"] == (
        original_conclusion
    )
    assert support_record["status"] == (
        "CURRENT_CONCLUSION_EVIDENCE_SUPPORTED"
    )

    # Contradiction without an evidence-backed correction remains blocked.
    missing_correction_input = deepcopy(through_dna20)
    missing_correction_input["truth_protocol_cases"] = [
        {
            "case_id": "DNA21-MISSING-CORRECTION",
            "conclusion_id": "DNA21-CONCLUSION-01",
            "ego_preference": "KEEP_ORIGINAL",
            "evidence": [
                {
                    "evidence_id": "DNA21-C-01",
                    "relation": "CONTRADICTS",
                    "independently_verified": True,
                    "content": "VERIFIED_CONTRADICTION",
                }
            ],
        }
    ]
    missing_correction = dna21_core.activate(
        missing_correction_input
    )
    missing_correction_record = missing_correction[
        "core54_outputs"
    ]["DNA-21"]["evaluation"]["records"][0]
    assert missing_correction_record["protocol_resolved"] is False
    assert missing_correction_record["correction_applied"] is False
    assert missing_correction_record["status"] == (
        "EVIDENCE_BACKED_CORRECTION_REQUIRED"
    )

    # A correction cannot cite unknown or non-contradicting evidence.
    bad_correction_input = deepcopy(through_dna20)
    bad_correction_input["truth_protocol_cases"] = [
        {
            "case_id": "DNA21-BAD-CORRECTION",
            "conclusion_id": "DNA21-CONCLUSION-01",
            "evidence": [
                {
                    "evidence_id": "DNA21-BAD-E-01",
                    "relation": "SUPPORTS",
                    "independently_verified": True,
                    "content": "SUPPORT",
                }
            ],
            "correction": {
                "corrected_conclusion": corrected_conclusion,
                "reason": "UNBOUND_CORRECTION",
                "evidence_ids": ["UNKNOWN-EVIDENCE"],
            },
        }
    ]
    bad_correction = dna21_core.activate(
        bad_correction_input
    )
    bad_correction_record = bad_correction[
        "core54_outputs"
    ]["DNA-21"]["evaluation"]["records"][0]
    assert bad_correction_record["correction"]["valid"] is False
    assert (
        "CORRECTION_REFERENCES_UNKNOWN_EVIDENCE"
        in bad_correction_record["correction"]["errors"]
    )
    assert (
        "CORRECTION_REQUIRES_VERIFIED_CONTRADICTING_EVIDENCE"
        in bad_correction_record["correction"]["errors"]
    )
    assert bad_correction_record["correction_applied"] is False

    # Conflicting verified evidence must remain unresolved.
    conflicting_input = deepcopy(through_dna20)
    conflicting_input["truth_protocol_cases"] = [
        {
            "case_id": "DNA21-CONFLICT",
            "conclusion_id": "DNA21-CONCLUSION-01",
            "evidence": [
                {
                    "evidence_id": "DNA21-CONFLICT-S",
                    "relation": "SUPPORTS",
                    "independently_verified": True,
                    "content": "SUPPORT",
                },
                {
                    "evidence_id": "DNA21-CONFLICT-C",
                    "relation": "CONTRADICTS",
                    "independently_verified": True,
                    "content": "CONTRADICTION",
                },
            ],
            "correction": {
                "corrected_conclusion": corrected_conclusion,
                "reason": "CONTRADICTING_EVIDENCE_PRESENT",
                "evidence_ids": ["DNA21-CONFLICT-C"],
            },
        }
    ]
    conflicting = dna21_core.activate(conflicting_input)
    conflicting_record = conflicting[
        "core54_outputs"
    ]["DNA-21"]["evaluation"]["records"][0]
    assert conflicting_record["evidence_summary"]["status"] == (
        "CONFLICTING_VERIFIED_EVIDENCE"
    )
    assert conflicting_record["protocol_resolved"] is False
    assert conflicting_record["correction_applied"] is False
    assert conflicting_record["status"] == (
        "CONFLICTING_EVIDENCE_REQUIRES_FURTHER_VERIFICATION"
    )

    # A case must bind to a complete DNA-20 conclusion record.
    unknown_conclusion_input = deepcopy(through_dna20)
    unknown_conclusion_input["truth_protocol_cases"] = [
        {
            "case_id": "DNA21-UNKNOWN-CONCLUSION",
            "conclusion_id": "UNKNOWN-CONCLUSION",
            "evidence": [],
        }
    ]
    unknown_conclusion = dna21_core.activate(
        unknown_conclusion_input
    )
    unknown_record = unknown_conclusion[
        "core54_outputs"
    ]["DNA-21"]["evaluation"]["records"][0]
    assert unknown_record["protocol_resolved"] is False
    assert "DNA20_CONCLUSION_BINDING_REQUIRED" in (
        unknown_record["errors"]
    )
    assert unknown_record["status"] == (
        "TRUTH_PROTOCOL_INPUT_INCOMPLETE"
    )

    # Duplicate evidence identity must fail closed.
    duplicate_evidence_input = deepcopy(through_dna20)
    duplicate_evidence_input["truth_protocol_cases"] = [
        {
            "case_id": "DNA21-DUP-EVIDENCE",
            "conclusion_id": "DNA21-CONCLUSION-01",
            "evidence": [
                {
                    "evidence_id": "DNA21-DUP-E",
                    "relation": "SUPPORTS",
                    "independently_verified": True,
                    "content": "A",
                },
                {
                    "evidence_id": "DNA21-DUP-E",
                    "relation": "CONTRADICTS",
                    "independently_verified": True,
                    "content": "B",
                },
            ],
        }
    ]
    try:
        dna21_core.activate(duplicate_evidence_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-21_DUPLICATE_EVIDENCE_ID:DNA21-DUP-E"
        )
    else:
        raise AssertionError(
            "DNA-21_ACCEPTED_DUPLICATE_EVIDENCE_ID"
        )

    # No supplied case creates an explicit empty batch.
    no_cases = dna21_core.activate(deepcopy(through_dna20))
    no_cases_batch = no_cases[
        "core54_outputs"
    ]["DNA-21"]["evaluation"]["batch"]
    assert no_cases_batch["case_count"] == 0
    assert no_cases_batch["record_ids"] == []
    assert no_cases_batch["status"] == (
        "NO_TRUTH_PROTOCOL_CASES_SUPPLIED"
    )
    assert no_cases_batch["truth_established"] is False

    # Reject provisional root flags as the official Canon contract.
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result
    assert "correction_over_ego" not in result

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
        "core_id": "DNA-21",
        "canon_mapping": "PASS",
        "truth_over_eloquence": "PASS",
        "evidence_over_confidence": "PASS",
        "correction_over_ego": "PASS",
        "dna20_conclusion_binding": "PASS",
        "missing_evidence_not_invented": "PASS",
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
            "DNA-22"
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
    20: "SIGMA_DNA_20_UNCERTAINTY_AS_FIRST_CLASS_DATA",
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
                "DNA-21_FAIL: REQUIRED_PATH_NOT_FOUND"
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
        print("DNA-21_FAIL: IMPORT_ERROR")
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

        for index in range(1, 21):
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

        report = self_check_dna21(
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
            for index in range(1, 22)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-21_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-21_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_21_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "TRUTH_OVER_ELOQUENCE:",
        report["truth_over_eloquence"],
    )
    print(
        "EVIDENCE_OVER_CONFIDENCE:",
        report["evidence_over_confidence"],
    )
    print(
        "CORRECTION_OVER_EGO:",
        report["correction_over_ego"],
    )
    print(
        "DNA20_CONCLUSION_BINDING:",
        report["dna20_conclusion_binding"],
    )
    print(
        "MISSING_EVIDENCE_NOT_INVENTED:",
        report["missing_evidence_not_invented"],
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
    print("OFFICIAL_BOUND_CORES: 21/54")
    print("NEXT_AUTHORIZED: DNA-22")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
