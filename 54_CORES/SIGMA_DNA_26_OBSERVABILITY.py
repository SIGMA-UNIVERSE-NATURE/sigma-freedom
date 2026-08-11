#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-26: OBSERVABILITY
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_26_OBSERVABILITY.py
"""

from __future__ import annotations

import hashlib
import importlib
import json
import string
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

CANON_DNA26: Dict[str, str] = {
    "id": "DNA-26",
    "name": "Observability",
    "purpose": (
        "Lưu artifact kiểm chứng được: decisions, hypotheses, tools, "
        "verifier results, confidence, lineage."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
VERIFICATION_WALL_SCHEMA = (
    "SIGMA_INDEPENDENT_VERIFICATION_WALL_V1"
)
TOOL_INTELLIGENCE_SCHEMA = "SIGMA_TOOL_INTELLIGENCE_V1"
UNCERTAINTY_FIRST_CLASS_SCHEMA = (
    "SIGMA_UNCERTAINTY_FIRST_CLASS_DATA_V1"
)
SELF_IMPROVEMENT_SCHEMA = "SIGMA_SELF_IMPROVEMENT_V1"
OBSERVABILITY_SCHEMA = "SIGMA_OBSERVABILITY_V1"

OBSERVABILITY_ARTIFACT_FIELDS = [
    "artifact_id",
    "decisions",
    "hypotheses",
    "tools",
    "verifier_results",
    "confidence",
    "lineage",
]

DECISION_FIELDS = [
    "decision_id",
    "statement",
    "rationale",
    "evidence",
]

HYPOTHESIS_FIELDS = [
    "hypothesis_id",
    "statement",
    "status",
    "evidence",
]

HYPOTHESIS_STATUSES = [
    "PROPOSED",
    "TESTED",
    "SUPPORTED",
    "REJECTED",
    "UNRESOLVED",
]

TOOL_FIELDS = [
    "decision_id",
    "used",
    "source_sha256",
]

VERIFIER_RESULT_FIELDS = [
    "evaluation_id",
    "verifier_id",
    "independent",
    "passed",
    "source_sha256",
]

CONFIDENCE_FIELDS = [
    "conclusion_id",
    "value",
    "evidence_coverage",
    "unresolved_uncertainty",
    "source_sha256",
]

LINEAGE_FIELDS = [
    "source_kind",
    "source_id",
    "source_sha256",
    "relation",
]

LINEAGE_SOURCE_KINDS = [
    "CORE_OUTPUT",
    "OBSERVABILITY_ARTIFACT",
]

OBSERVABILITY_CONTRACT: Dict[str, Any] = {
    "schema": OBSERVABILITY_SCHEMA,
    "input_path": "observability_artifacts",
    "state_path": "cognitive_state.observability",
    "required_artifact_fields": deepcopy(
        OBSERVABILITY_ARTIFACT_FIELDS
    ),
    "canonical_categories": [
        "decisions",
        "hypotheses",
        "tools",
        "verifier_results",
        "confidence",
        "lineage",
    ],
    "decision_fields": deepcopy(DECISION_FIELDS),
    "hypothesis_fields": deepcopy(HYPOTHESIS_FIELDS),
    "tool_fields": deepcopy(TOOL_FIELDS),
    "verifier_result_fields": deepcopy(
        VERIFIER_RESULT_FIELDS
    ),
    "confidence_fields": deepcopy(CONFIDENCE_FIELDS),
    "lineage_fields": deepcopy(LINEAGE_FIELDS),
    "integrity_encoding": {
        "artifact": "CANONICAL_JSON_SHA256",
        "append_chain": "SHA256_PREVIOUS_CHAIN_PLUS_ARTIFACT",
        "canon_status": (
            "IMPLEMENTATION_ENCODING_NOT_CANON_FIELD"
        ),
    },
    "confidence_binding": "DNA-20_FIRST_CLASS_DATA",
    "tool_binding": "DNA-12_TOOL_INTELLIGENCE",
    "verifier_binding": "DNA-09_INDEPENDENT_VERIFICATION_WALL",
    "lineage_source_kinds": deepcopy(
        LINEAGE_SOURCE_KINDS
    ),
    "incomplete_artifacts_remain_visible": True,
    "artifact_integrity_is_not_truth": True,
    "artifact_storage_scope": "CURRENT_STRUCTURED_STATE",
    "external_persistence_started": False,
    "memory_runtime_started": False,
    "truth_established_by_dna26": False,
    "knowledge_promoted_by_dna26": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA09_VERIFIER_"
        "DNA12_TOOL_DNA20_CONFIDENCE_AND_DNA25_LINEAGE_BINDING"
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
    25: "SIGMA_DNA_25_SELF_IMPROVEMENT",
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


def _is_sha256(value: Any) -> bool:
    return bool(
        isinstance(value, str)
        and len(value) == 64
        and all(
            character in string.hexdigits
            for character in value
        )
    )


def _non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _non_empty_list(value: Any) -> bool:
    return isinstance(value, list) and len(value) > 0


def _valid_probability(value: Any) -> bool:
    return bool(
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and 0.0 <= float(value) <= 1.0
    )


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA26:
        raise RuntimeError(
            "DNA-26_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA26,
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
            "DNA-26_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
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
            "DNA-26_VERIFICATION_WALL_SCHEMA_MISMATCH:"
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

    tool_intelligence = state.get("tool_intelligence")
    if not isinstance(tool_intelligence, dict):
        raise RuntimeError(
            "DNA-12_TOOL_INTELLIGENCE_REQUIRED"
        )
    tool_contract = tool_intelligence.get("contract")
    if not isinstance(tool_contract, dict):
        raise RuntimeError(
            "DNA-12_TOOL_INTELLIGENCE_CONTRACT_REQUIRED"
        )
    if tool_contract.get("schema") != TOOL_INTELLIGENCE_SCHEMA:
        raise ValueError(
            "DNA-26_TOOL_INTELLIGENCE_SCHEMA_MISMATCH:"
            f"{tool_contract.get('schema')!r}"
        )
    if not isinstance(
        tool_intelligence.get("decisions"),
        list,
    ):
        raise TypeError(
            "tool_intelligence['decisions'] must be a list"
        )
    if not isinstance(
        tool_intelligence.get("tool_outputs"),
        list,
    ):
        raise TypeError(
            "tool_intelligence['tool_outputs'] must be a list"
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
    uncertainty_contract = first_class.get("contract")
    if not isinstance(uncertainty_contract, dict):
        raise RuntimeError(
            "DNA-20_UNCERTAINTY_CONTRACT_REQUIRED"
        )
    if uncertainty_contract.get("schema") != (
        UNCERTAINTY_FIRST_CLASS_SCHEMA
    ):
        raise ValueError(
            "DNA-26_UNCERTAINTY_SCHEMA_MISMATCH:"
            f"{uncertainty_contract.get('schema')!r}"
        )
    if not isinstance(first_class.get("records"), list):
        raise TypeError(
            "uncertainty.first_class_data['records'] "
            "must be a list"
        )

    self_improvement = state.get("self_improvement")
    if not isinstance(self_improvement, dict):
        raise RuntimeError(
            "DNA-25_SELF_IMPROVEMENT_REQUIRED"
        )
    self_improvement_contract = self_improvement.get(
        "contract"
    )
    if not isinstance(self_improvement_contract, dict):
        raise RuntimeError(
            "DNA-25_SELF_IMPROVEMENT_CONTRACT_REQUIRED"
        )
    if self_improvement_contract.get("schema") != (
        SELF_IMPROVEMENT_SCHEMA
    ):
        raise ValueError(
            "DNA-26_SELF_IMPROVEMENT_SCHEMA_MISMATCH:"
            f"{self_improvement_contract.get('schema')!r}"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError(
            "DNA-09_DNA12_DNA20_DNA25_OUTPUTS_REQUIRED"
        )

    for required_id in (
        "DNA-09",
        "DNA-12",
        "DNA-20",
        "DNA-25",
    ):
        if not isinstance(outputs.get(required_id), dict):
            raise RuntimeError(
                f"{required_id}_OUTPUT_REQUIRED"
            )

    return (
        state,
        verification_wall,
        tool_intelligence,
        first_class,
        outputs,
    )


def _install_observability_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("observability")

    expected = {
        "contract": deepcopy(OBSERVABILITY_CONTRACT),
        "artifacts": [],
        "batches": [],
    }

    if existing is None:
        state["observability"] = expected
        return state["observability"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['observability'] must be a dict"
        )

    if existing.get("contract") != OBSERVABILITY_CONTRACT:
        raise ValueError(
            "DNA-26_OBSERVABILITY_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("artifacts"), list):
        raise TypeError(
            "observability['artifacts'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "observability['batches'] must be a list"
        )

    if not _verify_registry_chain(existing):
        raise RuntimeError(
            "DNA-26_EXISTING_ARTIFACT_CHAIN_INVALID"
        )

    return existing


def _find_record(
    records: List[Any],
    key: str,
    value: Any,
) -> Optional[Dict[str, Any]]:
    matches = [
        record
        for record in records
        if isinstance(record, dict)
        and record.get(key) == value
    ]
    if len(matches) > 1:
        raise RuntimeError(
            f"DNA-26_DUPLICATE_SOURCE_RECORD:{key}:{value}"
        )
    return matches[0] if matches else None


def _normalize_evidence(
    supplied: Any,
    *,
    prefix: str,
    errors: List[str],
) -> List[Any]:
    if not isinstance(supplied, list):
        errors.append(f"{prefix}_EVIDENCE_LIST_REQUIRED")
        return []

    if not supplied:
        errors.append(f"{prefix}_EVIDENCE_REQUIRED")
        return []

    if any(item is None for item in supplied):
        raise ValueError(
            f"DNA-26_{prefix}_EVIDENCE_ITEM_MUST_NOT_BE_NULL"
        )

    return deepcopy(supplied)


def _normalize_decisions(
    supplied: Any,
) -> Tuple[List[Dict[str, Any]], List[str]]:
    if not isinstance(supplied, list):
        return [], ["DECISIONS_LIST_REQUIRED"]

    records: List[Dict[str, Any]] = []
    errors: List[str] = []
    ids: List[str] = []

    for index, item in enumerate(supplied, start=1):
        item_errors: List[str] = []
        if not isinstance(item, dict):
            errors.append(
                f"DECISION_{index}_MUST_BE_A_DICT"
            )
            continue

        missing = [
            field
            for field in DECISION_FIELDS
            if field not in item
        ]
        if missing:
            item_errors.append(
                f"DECISION_{index}_FIELDS_MISSING"
            )

        decision_id = item.get("decision_id")
        if not _non_empty_text(decision_id):
            item_errors.append(
                f"DECISION_{index}_ID_REQUIRED"
            )
        else:
            ids.append(decision_id)

        statement = item.get("statement")
        if not _non_empty_text(statement):
            item_errors.append(
                f"DECISION_{index}_STATEMENT_REQUIRED"
            )

        rationale = item.get("rationale")
        if not _non_empty_text(rationale):
            item_errors.append(
                f"DECISION_{index}_RATIONALE_REQUIRED"
            )

        evidence = _normalize_evidence(
            item.get("evidence"),
            prefix=f"DECISION_{index}",
            errors=item_errors,
        )

        item_errors = list(dict.fromkeys(item_errors))
        records.append(
            {
                "decision_id": decision_id,
                "statement": statement,
                "rationale": rationale,
                "evidence": evidence,
                "evidence_sha256": (
                    _sha256_json(evidence)
                    if evidence
                    else None
                ),
                "complete": not item_errors,
                "errors": item_errors,
            }
        )
        errors.extend(item_errors)

    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-26_DUPLICATE_DECISION_ID"
        )

    return records, list(dict.fromkeys(errors))


def _normalize_hypotheses(
    supplied: Any,
) -> Tuple[List[Dict[str, Any]], List[str]]:
    if not isinstance(supplied, list):
        return [], ["HYPOTHESES_LIST_REQUIRED"]

    records: List[Dict[str, Any]] = []
    errors: List[str] = []
    ids: List[str] = []

    for index, item in enumerate(supplied, start=1):
        item_errors: List[str] = []
        if not isinstance(item, dict):
            errors.append(
                f"HYPOTHESIS_{index}_MUST_BE_A_DICT"
            )
            continue

        missing = [
            field
            for field in HYPOTHESIS_FIELDS
            if field not in item
        ]
        if missing:
            item_errors.append(
                f"HYPOTHESIS_{index}_FIELDS_MISSING"
            )

        hypothesis_id = item.get("hypothesis_id")
        if not _non_empty_text(hypothesis_id):
            item_errors.append(
                f"HYPOTHESIS_{index}_ID_REQUIRED"
            )
        else:
            ids.append(hypothesis_id)

        statement = item.get("statement")
        if not _non_empty_text(statement):
            item_errors.append(
                f"HYPOTHESIS_{index}_STATEMENT_REQUIRED"
            )

        status = item.get("status")
        if not isinstance(status, str):
            item_errors.append(
                f"HYPOTHESIS_{index}_STATUS_REQUIRED"
            )
            normalized_status = None
        else:
            normalized_status = status.strip().upper()
            if normalized_status not in HYPOTHESIS_STATUSES:
                raise ValueError(
                    "DNA-26_UNKNOWN_HYPOTHESIS_STATUS:"
                    f"{normalized_status}"
                )

        evidence = _normalize_evidence(
            item.get("evidence"),
            prefix=f"HYPOTHESIS_{index}",
            errors=item_errors,
        )

        item_errors = list(dict.fromkeys(item_errors))
        records.append(
            {
                "hypothesis_id": hypothesis_id,
                "statement": statement,
                "status": normalized_status,
                "evidence": evidence,
                "evidence_sha256": (
                    _sha256_json(evidence)
                    if evidence
                    else None
                ),
                "complete": not item_errors,
                "errors": item_errors,
            }
        )
        errors.extend(item_errors)

    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-26_DUPLICATE_HYPOTHESIS_ID"
        )

    return records, list(dict.fromkeys(errors))


def _normalize_tools(
    supplied: Any,
    tool_intelligence: Dict[str, Any],
) -> Tuple[List[Dict[str, Any]], List[str]]:
    if not isinstance(supplied, list):
        return [], ["TOOLS_LIST_REQUIRED"]

    records: List[Dict[str, Any]] = []
    errors: List[str] = []
    decision_ids: List[str] = []

    decisions = tool_intelligence["decisions"]
    tool_outputs = tool_intelligence["tool_outputs"]

    for index, item in enumerate(supplied, start=1):
        item_errors: List[str] = []
        if not isinstance(item, dict):
            errors.append(f"TOOL_{index}_MUST_BE_A_DICT")
            continue

        missing = [
            field
            for field in TOOL_FIELDS
            if field not in item
        ]
        if missing:
            item_errors.append(f"TOOL_{index}_FIELDS_MISSING")

        decision_id = item.get("decision_id")
        if not _non_empty_text(decision_id):
            item_errors.append(
                f"TOOL_{index}_DECISION_ID_REQUIRED"
            )
        else:
            decision_ids.append(decision_id)

        used = item.get("used")
        if not isinstance(used, bool):
            if "used" in item:
                raise TypeError(
                    f"tools[{index - 1}]['used'] must be a bool"
                )
            item_errors.append(
                f"TOOL_{index}_USED_STATUS_REQUIRED"
            )
            used = None

        source_sha256 = item.get("source_sha256")
        if not _is_sha256(source_sha256):
            item_errors.append(
                f"TOOL_{index}_SOURCE_SHA256_REQUIRED"
            )

        decision = _find_record(
            decisions,
            "decision_id",
            decision_id,
        )
        if decision is None:
            item_errors.append(
                f"TOOL_{index}_DNA12_DECISION_NOT_FOUND"
            )

        tool_output_id = item.get("tool_output_id")
        source_record: Optional[Dict[str, Any]] = None
        source_kind: Optional[str] = None

        if used is True:
            if not _non_empty_text(tool_output_id):
                item_errors.append(
                    f"TOOL_{index}_OUTPUT_ID_REQUIRED_WHEN_USED"
                )
            else:
                source_record = _find_record(
                    tool_outputs,
                    "tool_output_id",
                    tool_output_id,
                )
                if source_record is None:
                    item_errors.append(
                        f"TOOL_{index}_DNA12_OUTPUT_NOT_FOUND"
                    )
                elif (
                    decision_id is not None
                    and source_record.get("decision_id")
                    != decision_id
                ):
                    item_errors.append(
                        f"TOOL_{index}_DECISION_OUTPUT_BINDING_MISMATCH"
                    )
                source_kind = "DNA12_TOOL_OUTPUT"
        elif used is False:
            if tool_output_id is not None:
                item_errors.append(
                    f"TOOL_{index}_OUTPUT_ID_FORBIDDEN_WHEN_UNUSED"
                )
            source_record = decision
            source_kind = "DNA12_TOOL_DECISION"

        source_bound = bool(
            source_record is not None
            and _is_sha256(source_sha256)
            and _sha256_json(source_record) == source_sha256
        )
        if source_record is not None and not source_bound:
            item_errors.append(
                f"TOOL_{index}_SOURCE_HASH_MISMATCH"
            )

        item_errors = list(dict.fromkeys(item_errors))
        records.append(
            {
                "decision_id": decision_id,
                "used": used,
                "tool_output_id": tool_output_id,
                "source_kind": source_kind,
                "source_sha256": source_sha256,
                "source_bound": source_bound,
                "complete": not item_errors,
                "errors": item_errors,
            }
        )
        errors.extend(item_errors)

    if len(decision_ids) != len(set(decision_ids)):
        raise ValueError(
            "DNA-26_DUPLICATE_TOOL_DECISION_ID"
        )

    return records, list(dict.fromkeys(errors))


def _normalize_verifier_results(
    supplied: Any,
    verification_wall: Dict[str, Any],
) -> Tuple[List[Dict[str, Any]], List[str]]:
    if not isinstance(supplied, list):
        return [], ["VERIFIER_RESULTS_LIST_REQUIRED"]

    records: List[Dict[str, Any]] = []
    errors: List[str] = []
    evaluation_ids: List[str] = []

    evaluations = verification_wall["evaluations"]

    for index, item in enumerate(supplied, start=1):
        item_errors: List[str] = []
        if not isinstance(item, dict):
            errors.append(
                f"VERIFIER_RESULT_{index}_MUST_BE_A_DICT"
            )
            continue

        missing = [
            field
            for field in VERIFIER_RESULT_FIELDS
            if field not in item
        ]
        if missing:
            item_errors.append(
                f"VERIFIER_RESULT_{index}_FIELDS_MISSING"
            )

        evaluation_id = item.get("evaluation_id")
        if not _non_empty_text(evaluation_id):
            item_errors.append(
                f"VERIFIER_RESULT_{index}_EVALUATION_ID_REQUIRED"
            )
        else:
            evaluation_ids.append(evaluation_id)

        verifier_id = item.get("verifier_id")
        if not _non_empty_text(verifier_id):
            item_errors.append(
                f"VERIFIER_RESULT_{index}_VERIFIER_ID_REQUIRED"
            )

        independent = item.get("independent")
        if not isinstance(independent, bool):
            if "independent" in item:
                raise TypeError(
                    "verifier_results"
                    f"[{index - 1}]['independent'] must be a bool"
                )
            item_errors.append(
                f"VERIFIER_RESULT_{index}_INDEPENDENCE_REQUIRED"
            )
            independent = None

        passed = item.get("passed")
        if not isinstance(passed, bool):
            if "passed" in item:
                raise TypeError(
                    "verifier_results"
                    f"[{index - 1}]['passed'] must be a bool"
                )
            item_errors.append(
                f"VERIFIER_RESULT_{index}_PASS_STATUS_REQUIRED"
            )
            passed = None

        source_sha256 = item.get("source_sha256")
        if not _is_sha256(source_sha256):
            item_errors.append(
                f"VERIFIER_RESULT_{index}_SOURCE_SHA256_REQUIRED"
            )

        evaluation = _find_record(
            evaluations,
            "evaluation_id",
            evaluation_id,
        )
        if evaluation is None:
            item_errors.append(
                f"VERIFIER_RESULT_{index}_DNA09_EVALUATION_NOT_FOUND"
            )

        source_bound = bool(
            evaluation is not None
            and _is_sha256(source_sha256)
            and _sha256_json(evaluation) == source_sha256
        )
        if evaluation is not None and not source_bound:
            item_errors.append(
                f"VERIFIER_RESULT_{index}_SOURCE_HASH_MISMATCH"
            )

        if evaluation is not None:
            source_verifier_id = evaluation.get(
                "verification_record",
                {},
            ).get("verifier_id")
            if source_verifier_id != verifier_id:
                item_errors.append(
                    f"VERIFIER_RESULT_{index}_VERIFIER_ID_MISMATCH"
                )
            if evaluation.get("independent_verifier") != independent:
                item_errors.append(
                    f"VERIFIER_RESULT_{index}_INDEPENDENCE_MISMATCH"
                )
            if evaluation.get("verification_passed") != passed:
                item_errors.append(
                    f"VERIFIER_RESULT_{index}_PASS_MISMATCH"
                )

        item_errors = list(dict.fromkeys(item_errors))
        records.append(
            {
                "evaluation_id": evaluation_id,
                "verifier_id": verifier_id,
                "independent": independent,
                "passed": passed,
                "source_sha256": source_sha256,
                "source_bound": source_bound,
                "complete": not item_errors,
                "errors": item_errors,
            }
        )
        errors.extend(item_errors)

    if len(evaluation_ids) != len(set(evaluation_ids)):
        raise ValueError(
            "DNA-26_DUPLICATE_VERIFIER_EVALUATION_ID"
        )

    return records, list(dict.fromkeys(errors))


def _normalize_confidence(
    supplied: Any,
    first_class: Dict[str, Any],
) -> Tuple[Dict[str, Any], List[str]]:
    errors: List[str] = []

    if not isinstance(supplied, dict):
        return {
            "conclusion_id": None,
            "value": None,
            "evidence_coverage": None,
            "unresolved_uncertainty": [],
            "source_sha256": None,
            "source_bound": False,
            "complete": False,
            "errors": ["CONFIDENCE_DICT_REQUIRED"],
        }, ["CONFIDENCE_DICT_REQUIRED"]

    missing = [
        field
        for field in CONFIDENCE_FIELDS
        if field not in supplied
    ]
    if missing:
        errors.append("CONFIDENCE_FIELDS_MISSING")

    conclusion_id = supplied.get("conclusion_id")
    if not _non_empty_text(conclusion_id):
        errors.append("CONFIDENCE_CONCLUSION_ID_REQUIRED")

    value = supplied.get("value")
    if not _valid_probability(value):
        errors.append(
            "CONFIDENCE_VALUE_MUST_BE_BETWEEN_ZERO_AND_ONE"
        )

    evidence_coverage = supplied.get("evidence_coverage")
    if not _valid_probability(evidence_coverage):
        errors.append(
            "CONFIDENCE_EVIDENCE_COVERAGE_MUST_BE_BETWEEN_ZERO_AND_ONE"
        )

    unresolved = supplied.get("unresolved_uncertainty")
    if not isinstance(unresolved, list):
        errors.append(
            "CONFIDENCE_UNRESOLVED_UNCERTAINTY_LIST_REQUIRED"
        )
        unresolved = []
    elif any(
        not _non_empty_text(item)
        for item in unresolved
    ):
        errors.append(
            "CONFIDENCE_UNRESOLVED_UNCERTAINTY_ITEMS_INVALID"
        )

    source_sha256 = supplied.get("source_sha256")
    if not _is_sha256(source_sha256):
        errors.append("CONFIDENCE_SOURCE_SHA256_REQUIRED")

    source = _find_record(
        first_class["records"],
        "conclusion_id",
        conclusion_id,
    )
    if source is None:
        errors.append(
            "CONFIDENCE_DNA20_SOURCE_NOT_FOUND"
        )

    source_bound = bool(
        source is not None
        and _is_sha256(source_sha256)
        and _sha256_json(source) == source_sha256
    )
    if source is not None and not source_bound:
        errors.append("CONFIDENCE_SOURCE_HASH_MISMATCH")

    if source is not None:
        if source.get("confidence") != value:
            errors.append("CONFIDENCE_VALUE_SOURCE_MISMATCH")
        if source.get("evidence_coverage") != evidence_coverage:
            errors.append(
                "CONFIDENCE_EVIDENCE_COVERAGE_SOURCE_MISMATCH"
            )
        if source.get("unresolved_uncertainty") != unresolved:
            errors.append(
                "CONFIDENCE_UNRESOLVED_SOURCE_MISMATCH"
            )

    errors = list(dict.fromkeys(errors))
    return {
        "conclusion_id": conclusion_id,
        "value": value,
        "evidence_coverage": evidence_coverage,
        "unresolved_uncertainty": deepcopy(unresolved),
        "source_sha256": source_sha256,
        "source_bound": source_bound,
        "complete": not errors,
        "errors": errors,
    }, errors


def _normalize_lineage(
    supplied: Any,
    outputs: Dict[str, Any],
    registry: Dict[str, Any],
) -> Tuple[List[Dict[str, Any]], List[str]]:
    if not isinstance(supplied, list):
        return [], ["LINEAGE_LIST_REQUIRED"]

    if not supplied:
        return [], ["LINEAGE_REQUIRED"]

    records: List[Dict[str, Any]] = []
    errors: List[str] = []
    identities: List[Tuple[Any, Any]] = []

    for index, item in enumerate(supplied, start=1):
        item_errors: List[str] = []
        if not isinstance(item, dict):
            errors.append(
                f"LINEAGE_{index}_MUST_BE_A_DICT"
            )
            continue

        missing = [
            field
            for field in LINEAGE_FIELDS
            if field not in item
        ]
        if missing:
            item_errors.append(
                f"LINEAGE_{index}_FIELDS_MISSING"
            )

        source_kind = item.get("source_kind")
        if not isinstance(source_kind, str):
            item_errors.append(
                f"LINEAGE_{index}_SOURCE_KIND_REQUIRED"
            )
            normalized_kind = None
        else:
            normalized_kind = source_kind.strip().upper()
            if normalized_kind not in LINEAGE_SOURCE_KINDS:
                raise ValueError(
                    "DNA-26_UNKNOWN_LINEAGE_SOURCE_KIND:"
                    f"{normalized_kind}"
                )

        source_id = item.get("source_id")
        if not _non_empty_text(source_id):
            item_errors.append(
                f"LINEAGE_{index}_SOURCE_ID_REQUIRED"
            )

        source_sha256 = item.get("source_sha256")
        if not _is_sha256(source_sha256):
            item_errors.append(
                f"LINEAGE_{index}_SOURCE_SHA256_REQUIRED"
            )

        relation = item.get("relation")
        if not _non_empty_text(relation):
            item_errors.append(
                f"LINEAGE_{index}_RELATION_REQUIRED"
            )

        source: Any = None
        if normalized_kind == "CORE_OUTPUT":
            source = outputs.get(source_id)
            if not isinstance(source, dict):
                item_errors.append(
                    f"LINEAGE_{index}_CORE_OUTPUT_NOT_FOUND"
                )
        elif normalized_kind == "OBSERVABILITY_ARTIFACT":
            source = _find_record(
                registry["artifacts"],
                "artifact_id",
                source_id,
            )
            if source is None:
                item_errors.append(
                    f"LINEAGE_{index}_ARTIFACT_NOT_FOUND"
                )

        if normalized_kind == "CORE_OUTPUT":
            expected_hash = (
                _sha256_json(source)
                if isinstance(source, dict)
                else None
            )
        elif normalized_kind == "OBSERVABILITY_ARTIFACT":
            expected_hash = (
                source.get("artifact_sha256")
                if isinstance(source, dict)
                else None
            )
        else:
            expected_hash = None

        source_verified = bool(
            expected_hash is not None
            and _is_sha256(source_sha256)
            and source_sha256 == expected_hash
        )
        if source is not None and not source_verified:
            item_errors.append(
                f"LINEAGE_{index}_SOURCE_HASH_MISMATCH"
            )

        identities.append((normalized_kind, source_id))
        item_errors = list(dict.fromkeys(item_errors))
        records.append(
            {
                "source_kind": normalized_kind,
                "source_id": source_id,
                "source_sha256": source_sha256,
                "relation": relation,
                "source_verified": source_verified,
                "complete": not item_errors,
                "errors": item_errors,
            }
        )
        errors.extend(item_errors)

    if len(identities) != len(set(identities)):
        raise ValueError(
            "DNA-26_DUPLICATE_LINEAGE_SOURCE"
        )

    return records, list(dict.fromkeys(errors))


def _artifact_content(record: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "artifact_id": record["artifact_id"],
        "decisions": deepcopy(record["decisions"]),
        "hypotheses": deepcopy(record["hypotheses"]),
        "tools": deepcopy(record["tools"]),
        "verifier_results": deepcopy(
            record["verifier_results"]
        ),
        "confidence": deepcopy(record["confidence"]),
        "lineage": deepcopy(record["lineage"]),
    }


def _verify_artifact_integrity(
    record: Dict[str, Any],
    previous_chain_sha256: Optional[str],
) -> bool:
    try:
        artifact_sha256 = _sha256_json(
            _artifact_content(record)
        )
        chain_sha256 = _sha256_json(
            {
                "previous_chain_sha256": (
                    previous_chain_sha256
                ),
                "artifact_sha256": artifact_sha256,
            }
        )
        return bool(
            record.get("artifact_sha256")
            == artifact_sha256
            and record.get("previous_chain_sha256")
            == previous_chain_sha256
            and record.get("chain_sha256")
            == chain_sha256
        )
    except Exception:
        return False


def _verify_registry_chain(
    registry: Dict[str, Any],
) -> bool:
    artifacts = registry.get("artifacts")
    if not isinstance(artifacts, list):
        return False

    previous: Optional[str] = None
    for record in artifacts:
        if not isinstance(record, dict):
            return False
        if not _verify_artifact_integrity(
            record,
            previous,
        ):
            return False
        previous = record.get("chain_sha256")
    return True


def _incomplete_artifact(
    *,
    input_index: int,
    sequence: int,
    errors: List[str],
    previous_chain_sha256: Optional[str],
) -> Dict[str, Any]:
    record = {
        "sequence": sequence,
        "record_id": f"DNA-26-ARTIFACT-{sequence:04d}",
        "input_index": input_index,
        "artifact_id": None,
        "decisions": [],
        "hypotheses": [],
        "tools": [],
        "verifier_results": [],
        "confidence": {
            "conclusion_id": None,
            "value": None,
            "evidence_coverage": None,
            "unresolved_uncertainty": [],
            "source_sha256": None,
            "source_bound": False,
            "complete": False,
            "errors": ["CONFIDENCE_DICT_REQUIRED"],
        },
        "lineage": [],
        "category_hashes": {},
        "artifact_sha256": None,
        "previous_chain_sha256": previous_chain_sha256,
        "chain_sha256": None,
        "artifact_complete": False,
        "integrity_verifiable": False,
        "independent_verifier_result_count": 0,
        "passed_independent_verifier_result_count": 0,
        "truth_established": False,
        "knowledge_promoted": False,
        "external_persistence_started": False,
        "memory_runtime_started": False,
        "external_action_executed": False,
        "errors": list(dict.fromkeys(errors)),
        "status": "OBSERVABILITY_ARTIFACT_INCOMPLETE",
    }

    # Incomplete artifacts remain visible and tamper-evident.
    record["artifact_sha256"] = _sha256_json(
        _artifact_content(record)
    )
    record["chain_sha256"] = _sha256_json(
        {
            "previous_chain_sha256": previous_chain_sha256,
            "artifact_sha256": record["artifact_sha256"],
        }
    )
    return record


def _normalize_artifact(
    supplied: Any,
    *,
    input_index: int,
    sequence: int,
    previous_chain_sha256: Optional[str],
    verification_wall: Dict[str, Any],
    tool_intelligence: Dict[str, Any],
    first_class: Dict[str, Any],
    outputs: Dict[str, Any],
    registry: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        return _incomplete_artifact(
            input_index=input_index,
            sequence=sequence,
            errors=["OBSERVABILITY_ARTIFACT_MUST_BE_A_DICT"],
            previous_chain_sha256=previous_chain_sha256,
        )

    artifact = deepcopy(supplied)
    errors: List[str] = []

    missing = [
        field
        for field in OBSERVABILITY_ARTIFACT_FIELDS
        if field not in artifact
    ]
    if missing:
        errors.append(
            "OBSERVABILITY_ARTIFACT_FIELDS_MISSING"
        )

    artifact_id = artifact.get("artifact_id")
    if not _non_empty_text(artifact_id):
        errors.append("ARTIFACT_ID_REQUIRED")

    decisions, decision_errors = _normalize_decisions(
        artifact.get("decisions")
    )
    hypotheses, hypothesis_errors = _normalize_hypotheses(
        artifact.get("hypotheses")
    )
    tools, tool_errors = _normalize_tools(
        artifact.get("tools"),
        tool_intelligence,
    )
    verifier_results, verifier_errors = (
        _normalize_verifier_results(
            artifact.get("verifier_results"),
            verification_wall,
        )
    )
    confidence, confidence_errors = _normalize_confidence(
        artifact.get("confidence"),
        first_class,
    )
    lineage, lineage_errors = _normalize_lineage(
        artifact.get("lineage"),
        outputs,
        registry,
    )

    errors.extend(decision_errors)
    errors.extend(hypothesis_errors)
    errors.extend(tool_errors)
    errors.extend(verifier_errors)
    errors.extend(confidence_errors)
    errors.extend(lineage_errors)
    errors = list(dict.fromkeys(errors))

    artifact_complete = len(errors) == 0
    independent_count = sum(
        1
        for record in verifier_results
        if record["independent"] is True
    )
    passed_independent_count = sum(
        1
        for record in verifier_results
        if (
            record["independent"] is True
            and record["passed"] is True
            and record["source_bound"] is True
        )
    )

    record = {
        "sequence": sequence,
        "record_id": f"DNA-26-ARTIFACT-{sequence:04d}",
        "input_index": input_index,
        "artifact_id": artifact_id,
        "decisions": decisions,
        "hypotheses": hypotheses,
        "tools": tools,
        "verifier_results": verifier_results,
        "confidence": confidence,
        "lineage": lineage,
        "category_hashes": {
            "decisions_sha256": _sha256_json(decisions),
            "hypotheses_sha256": _sha256_json(hypotheses),
            "tools_sha256": _sha256_json(tools),
            "verifier_results_sha256": _sha256_json(
                verifier_results
            ),
            "confidence_sha256": _sha256_json(confidence),
            "lineage_sha256": _sha256_json(lineage),
        },
        "artifact_sha256": None,
        "previous_chain_sha256": previous_chain_sha256,
        "chain_sha256": None,
        "artifact_complete": artifact_complete,
        "integrity_verifiable": False,
        "independent_verifier_result_count": independent_count,
        "passed_independent_verifier_result_count": (
            passed_independent_count
        ),
        "truth_established": False,
        "knowledge_promoted": False,
        "external_persistence_started": False,
        "memory_runtime_started": False,
        "external_action_executed": False,
        "errors": errors,
        "status": (
            "OBSERVABILITY_ARTIFACT_VERIFIABLE"
            if artifact_complete
            else "OBSERVABILITY_ARTIFACT_INCOMPLETE"
        ),
    }

    record["artifact_sha256"] = _sha256_json(
        _artifact_content(record)
    )
    record["chain_sha256"] = _sha256_json(
        {
            "previous_chain_sha256": previous_chain_sha256,
            "artifact_sha256": record["artifact_sha256"],
        }
    )
    record["integrity_verifiable"] = bool(
        artifact_complete
        and _verify_artifact_integrity(
            record,
            previous_chain_sha256,
        )
    )

    if artifact_complete and not record["integrity_verifiable"]:
        record["errors"].append(
            "ARTIFACT_INTEGRITY_VERIFICATION_FAILED"
        )
        record["status"] = (
            "OBSERVABILITY_ARTIFACT_INTEGRITY_FAILED"
        )

    return record


def _evaluate_artifacts(
    supplied: Any,
    registry: Dict[str, Any],
    verification_wall: Dict[str, Any],
    tool_intelligence: Dict[str, Any],
    first_class: Dict[str, Any],
    outputs: Dict[str, Any],
) -> Dict[str, Any]:
    if supplied is None:
        artifacts: List[Any] = []
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['observability_artifacts'] must be a list"
        )
    else:
        artifacts = supplied

    artifact_ids = [
        item.get("artifact_id")
        for item in artifacts
        if isinstance(item, dict)
        and _non_empty_text(item.get("artifact_id"))
    ]
    if len(artifact_ids) != len(set(artifact_ids)):
        raise ValueError(
            "DNA-26_DUPLICATE_OBSERVABILITY_ARTIFACT_ID"
        )

    existing_ids = {
        record.get("artifact_id")
        for record in registry["artifacts"]
        if isinstance(record, dict)
    }
    duplicate_existing = [
        artifact_id
        for artifact_id in artifact_ids
        if artifact_id in existing_ids
    ]
    if duplicate_existing:
        raise ValueError(
            "DNA-26_OBSERVABILITY_ARTIFACT_ID_ALREADY_EXISTS"
        )

    start_sequence = len(registry["artifacts"]) + 1
    previous_chain = (
        registry["artifacts"][-1]["chain_sha256"]
        if registry["artifacts"]
        else None
    )

    records: List[Dict[str, Any]] = []
    for index, item in enumerate(artifacts, start=1):
        record = _normalize_artifact(
            item,
            input_index=index,
            sequence=start_sequence + index - 1,
            previous_chain_sha256=previous_chain,
            verification_wall=verification_wall,
            tool_intelligence=tool_intelligence,
            first_class=first_class,
            outputs=outputs,
            registry=registry,
        )
        records.append(record)
        registry["artifacts"].append(deepcopy(record))
        previous_chain = record["chain_sha256"]

    complete_count = sum(
        1
        for record in records
        if record["artifact_complete"]
    )
    verifiable_count = sum(
        1
        for record in records
        if record["integrity_verifiable"]
    )
    incomplete_count = len(records) - complete_count
    independent_result_count = sum(
        record["independent_verifier_result_count"]
        for record in records
    )
    passed_independent_result_count = sum(
        record[
            "passed_independent_verifier_result_count"
        ]
        for record in records
    )
    chain_valid = _verify_registry_chain(registry)

    if not records:
        status = "NO_OBSERVABILITY_ARTIFACTS_SUPPLIED"
    elif not chain_valid:
        status = "OBSERVABILITY_CHAIN_INVALID"
    elif incomplete_count:
        status = "OBSERVABILITY_BATCH_INCOMPLETE"
    elif verifiable_count == len(records):
        status = "OBSERVABILITY_ARTIFACTS_VERIFIABLE"
    else:
        status = "OBSERVABILITY_ARTIFACTS_NOT_VERIFIABLE"

    batch_sequence = len(registry["batches"]) + 1
    batch = {
        "sequence": batch_sequence,
        "batch_id": f"DNA-26-BATCH-{batch_sequence:04d}",
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "artifact_ids": [
            record["artifact_id"]
            for record in records
        ],
        "artifact_count": len(records),
        "complete_count": complete_count,
        "verifiable_count": verifiable_count,
        "incomplete_count": incomplete_count,
        "independent_verifier_result_count": (
            independent_result_count
        ),
        "passed_independent_verifier_result_count": (
            passed_independent_result_count
        ),
        "registry_chain_valid": chain_valid,
        "all_artifacts_verifiable": bool(
            records
            and verifiable_count == len(records)
            and chain_valid
        ),
        "external_persistence_started": False,
        "memory_runtime_started": False,
        "truth_established": False,
        "knowledge_promoted": False,
        "external_action_executed": False,
        "status": status,
    }
    registry["batches"].append(deepcopy(batch))

    return {
        "records": records,
        "batch": batch,
    }


def dna26_observability(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Store tamper-evident, verifiable observability artifacts containing the
    exact Canon categories: decisions, hypotheses, tools, verifier results,
    confidence, and lineage.

    DNA-26 stores artifacts in the current structured cognitive state only.
    It does not establish truth, promote knowledge, start Memory Runtime,
    write external persistence, invoke a model, act externally, or modify
    Canon.
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
    trace.append("DNA-26")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    (
        state,
        verification_wall,
        tool_intelligence,
        first_class,
        outputs,
    ) = _validate_dependencies(context)

    registry = _install_observability_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-26",
            "operation": (
                "OBSERVABILITY_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "observability_schema": OBSERVABILITY_SCHEMA,
            "canonical_categories": [
                "decisions",
                "hypotheses",
                "tools",
                "verifier_results",
                "confidence",
                "lineage",
            ],
            "external_persistence_started": False,
            "memory_runtime_started": False,
        }
    )

    evaluation = _evaluate_artifacts(
        context.get("observability_artifacts"),
        registry,
        verification_wall,
        tool_intelligence,
        first_class,
        outputs,
    )
    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-26",
            "operation": (
                "OBSERVABILITY_ARTIFACTS_STORED_AND_VERIFIED"
            ),
            "canonical_sha256": canonical_sha256,
            "batch_id": batch["batch_id"],
            "artifact_count": batch["artifact_count"],
            "verifiable_count": batch["verifiable_count"],
            "incomplete_count": batch["incomplete_count"],
            "registry_chain_valid": (
                batch["registry_chain_valid"]
            ),
            "truth_established": False,
            "knowledge_promoted": False,
            "external_persistence_started": False,
        }
    )

    outputs["DNA-26"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "observability_contract": deepcopy(
            OBSERVABILITY_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "artifact_count": batch["artifact_count"],
        "complete_count": batch["complete_count"],
        "verifiable_count": batch["verifiable_count"],
        "incomplete_count": batch["incomplete_count"],
        "registry_chain_valid": (
            batch["registry_chain_valid"]
        ),
        "all_artifacts_verifiable": (
            batch["all_artifacts_verifiable"]
        ),
        "external_persistence_started": False,
        "memory_runtime_started": False,
        "truth_established": False,
        "knowledge_promoted": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna26(core54: Core54Like) -> None:
    core = core54.get("DNA-26")
    assert_exact_canon(core)
    core54.bind(
        "DNA-26",
        dna26_observability,
    )


def _through_dna25(core54: Core54Like) -> Dict[str, Any]:
    from SIGMA_DNA_25_SELF_IMPROVEMENT import (
        _through_dna24,
        _valid_case,
    )

    through_dna24 = _through_dna24(core54)
    through_dna24["self_improvement_cases"] = [
        _valid_case()
    ]
    return core54.get("DNA-25").activate(
        through_dna24
    )


def _valid_artifact(
    through_dna25: Dict[str, Any],
    *,
    artifact_id: str = "DNA26-OBSERVABILITY-01",
) -> Dict[str, Any]:
    state = through_dna25["cognitive_state"]
    outputs = through_dna25["core54_outputs"]

    decision = state["tool_intelligence"]["decisions"][-1]
    verification = state[
        "independent_verification_wall"
    ]["evaluations"][-1]
    uncertainty = state["uncertainty"][
        "first_class_data"
    ]["records"][-1]

    return {
        "artifact_id": artifact_id,
        "decisions": [
            {
                "decision_id": "DNA26-DECISION-01",
                "statement": (
                    "RETAIN_ONLY_MEASURABLE_SELF_IMPROVEMENT_CLAIMS"
                ),
                "rationale": (
                    "DNA25_REQUIRES_BEFORE_CHANGE_TEST_AFTER_EVIDENCE"
                ),
                "evidence": [
                    {
                        "source_core_id": "DNA-25",
                        "source_sha256": _sha256_json(
                            outputs["DNA-25"]
                        ),
                    }
                ],
            }
        ],
        "hypotheses": [
            {
                "hypothesis_id": "DNA26-HYPOTHESIS-01",
                "statement": (
                    "THE_REVISED_STRATEGY_IMPROVES_VERIFIED_TASK_SUCCESS"
                ),
                "status": "SUPPORTED",
                "evidence": [
                    {
                        "source_record_id": (
                            state["self_improvement"][
                                "records"
                            ][-1]["record_id"]
                        ),
                        "stage_chain_sha256": (
                            state["self_improvement"][
                                "records"
                            ][-1]["stage_chain_sha256"]
                        ),
                    }
                ],
            }
        ],
        "tools": [
            {
                "decision_id": decision["decision_id"],
                "used": False,
                "source_sha256": _sha256_json(decision),
            }
        ],
        "verifier_results": [
            {
                "evaluation_id": verification[
                    "evaluation_id"
                ],
                "verifier_id": verification[
                    "verification_record"
                ]["verifier_id"],
                "independent": verification[
                    "independent_verifier"
                ],
                "passed": verification[
                    "verification_passed"
                ],
                "source_sha256": _sha256_json(
                    verification
                ),
            }
        ],
        "confidence": {
            "conclusion_id": uncertainty[
                "conclusion_id"
            ],
            "value": uncertainty["confidence"],
            "evidence_coverage": uncertainty[
                "evidence_coverage"
            ],
            "unresolved_uncertainty": deepcopy(
                uncertainty["unresolved_uncertainty"]
            ),
            "source_sha256": _sha256_json(uncertainty),
        },
        "lineage": [
            {
                "source_kind": "CORE_OUTPUT",
                "source_id": core_id,
                "source_sha256": _sha256_json(
                    outputs[core_id]
                ),
                "relation": relation,
            }
            for core_id, relation in (
                ("DNA-09", "VERIFIER_RESULT_SOURCE"),
                ("DNA-12", "TOOL_DECISION_SOURCE"),
                ("DNA-20", "CONFIDENCE_SOURCE"),
                ("DNA-25", "SELF_IMPROVEMENT_SOURCE"),
            )
        ],
    }


def self_check_dna26(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 26):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna26_core = core54.get("DNA-26")
    assert_exact_canon(dna26_core)
    bind_dna26(core54)

    through_dna25 = _through_dna25(core54)
    through_dna25_snapshot = deepcopy(through_dna25)

    state_before = through_dna25["cognitive_state"]
    pre_verification_wall = deepcopy(
        state_before["independent_verification_wall"]
    )
    pre_tool_intelligence = deepcopy(
        state_before["tool_intelligence"]
    )
    pre_uncertainty = deepcopy(
        state_before["uncertainty"]
    )
    pre_self_improvement = deepcopy(
        state_before["self_improvement"]
    )
    pre_provenance_count = len(
        state_before["provenance"]
    )

    valid_input = deepcopy(through_dna25)
    valid_input["observability_artifacts"] = [
        _valid_artifact(through_dna25)
    ]
    result = dna26_core.activate(valid_input)

    assert through_dna25 == through_dna25_snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 27)
    ]

    dna26 = result["core54_outputs"]["DNA-26"]
    assert dna26["canonical_gene"] == CANON_DNA26
    assert dna26["observability_contract"] == (
        OBSERVABILITY_CONTRACT
    )
    assert dna26["artifact_count"] == 1
    assert dna26["complete_count"] == 1
    assert dna26["verifiable_count"] == 1
    assert dna26["incomplete_count"] == 0
    assert dna26["registry_chain_valid"] is True
    assert dna26["all_artifacts_verifiable"] is True
    assert dna26["external_persistence_started"] is False
    assert dna26["memory_runtime_started"] is False
    assert dna26["truth_established"] is False
    assert dna26["knowledge_promoted"] is False
    assert dna26["external_action_executed"] is False
    assert dna26["status"] == "CANON_ALIGNED"

    evaluation = dna26["evaluation"]
    record = evaluation["records"][0]
    batch = evaluation["batch"]

    assert record["record_id"] == "DNA-26-ARTIFACT-0001"
    assert record["artifact_id"] == "DNA26-OBSERVABILITY-01"
    assert len(record["decisions"]) == 1
    assert len(record["hypotheses"]) == 1
    assert len(record["tools"]) == 1
    assert len(record["verifier_results"]) == 1
    assert record["confidence"]["complete"] is True
    assert len(record["lineage"]) == 4
    assert all(
        item["source_verified"]
        for item in record["lineage"]
    )
    assert record["artifact_complete"] is True
    assert record["integrity_verifiable"] is True
    assert record["independent_verifier_result_count"] == 1
    assert (
        record[
            "passed_independent_verifier_result_count"
        ]
        == 1
    )
    assert record["truth_established"] is False
    assert record["knowledge_promoted"] is False
    assert record["errors"] == []
    assert record["status"] == (
        "OBSERVABILITY_ARTIFACT_VERIFIABLE"
    )
    assert _verify_artifact_integrity(record, None) is True

    assert batch["batch_id"] == "DNA-26-BATCH-0001"
    assert batch["artifact_count"] == 1
    assert batch["complete_count"] == 1
    assert batch["verifiable_count"] == 1
    assert batch["incomplete_count"] == 0
    assert batch["registry_chain_valid"] is True
    assert batch["all_artifacts_verifiable"] is True
    assert batch["status"] == (
        "OBSERVABILITY_ARTIFACTS_VERIFIABLE"
    )

    state = result["cognitive_state"]
    observability = state["observability"]
    assert observability["contract"] == OBSERVABILITY_CONTRACT
    assert observability["artifacts"] == [record]
    assert observability["batches"] == [batch]
    assert _verify_registry_chain(observability) is True
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-26"
    assert contract_event["operation"] == (
        "OBSERVABILITY_CONTRACT_ESTABLISHED"
    )
    assert contract_event["canonical_categories"] == [
        "decisions",
        "hypotheses",
        "tools",
        "verifier_results",
        "confidence",
        "lineage",
    ]
    assert contract_event["external_persistence_started"] is False
    assert contract_event["memory_runtime_started"] is False

    storage_event = state["provenance"][-1]
    assert storage_event["core_id"] == "DNA-26"
    assert storage_event["operation"] == (
        "OBSERVABILITY_ARTIFACTS_STORED_AND_VERIFIED"
    )
    assert storage_event["artifact_count"] == 1
    assert storage_event["verifiable_count"] == 1
    assert storage_event["incomplete_count"] == 0
    assert storage_event["registry_chain_valid"] is True
    assert storage_event["truth_established"] is False
    assert storage_event["knowledge_promoted"] is False
    assert storage_event["external_persistence_started"] is False

    # DNA-26 must not mutate the source systems it observes.
    assert state["independent_verification_wall"] == (
        pre_verification_wall
    )
    assert state["tool_intelligence"] == (
        pre_tool_intelligence
    )
    assert state["uncertainty"] == pre_uncertainty
    assert state["self_improvement"] == (
        pre_self_improvement
    )

    # A second artifact must chain to the first artifact.
    second_input = deepcopy(result)
    second_input["observability_artifacts"] = [
        _valid_artifact(
            result,
            artifact_id="DNA26-OBSERVABILITY-02",
        )
    ]
    second_input["observability_artifacts"][0][
        "lineage"
    ].append(
        {
            "source_kind": "OBSERVABILITY_ARTIFACT",
            "source_id": record["artifact_id"],
            "source_sha256": record["artifact_sha256"],
            "relation": "PREVIOUS_OBSERVABILITY_ARTIFACT",
        }
    )
    second = dna26_core.activate(second_input)
    second_record = second[
        "core54_outputs"
    ]["DNA-26"]["evaluation"]["records"][0]
    assert second_record["previous_chain_sha256"] == (
        record["chain_sha256"]
    )
    assert _verify_artifact_integrity(
        second_record,
        record["chain_sha256"],
    ) is True
    assert _verify_registry_chain(
        second["cognitive_state"]["observability"]
    ) is True

    # A wrong lineage hash must make the artifact incomplete.
    bad_lineage_input = deepcopy(through_dna25)
    bad_lineage = _valid_artifact(through_dna25)
    bad_lineage["lineage"][0]["source_sha256"] = "0" * 64
    bad_lineage_input["observability_artifacts"] = [
        bad_lineage
    ]
    bad_lineage_result = dna26_core.activate(
        bad_lineage_input
    )
    bad_lineage_record = bad_lineage_result[
        "core54_outputs"
    ]["DNA-26"]["evaluation"]["records"][0]
    assert bad_lineage_record["artifact_complete"] is False
    assert bad_lineage_record["integrity_verifiable"] is False
    assert (
        "LINEAGE_1_SOURCE_HASH_MISMATCH"
        in bad_lineage_record["errors"]
    )

    # Confidence must bind exactly to DNA-20.
    bad_confidence_input = deepcopy(through_dna25)
    bad_confidence = _valid_artifact(through_dna25)
    bad_confidence["confidence"]["value"] = 0.99
    bad_confidence_input["observability_artifacts"] = [
        bad_confidence
    ]
    bad_confidence_result = dna26_core.activate(
        bad_confidence_input
    )
    bad_confidence_record = bad_confidence_result[
        "core54_outputs"
    ]["DNA-26"]["evaluation"]["records"][0]
    assert bad_confidence_record["artifact_complete"] is False
    assert (
        "CONFIDENCE_VALUE_SOURCE_MISMATCH"
        in bad_confidence_record["errors"]
    )

    # Verifier result must bind exactly to the DNA-09 evaluation.
    bad_verifier_input = deepcopy(through_dna25)
    bad_verifier = _valid_artifact(through_dna25)
    bad_verifier["verifier_results"][0]["passed"] = False
    bad_verifier_input["observability_artifacts"] = [
        bad_verifier
    ]
    bad_verifier_result = dna26_core.activate(
        bad_verifier_input
    )
    bad_verifier_record = bad_verifier_result[
        "core54_outputs"
    ]["DNA-26"]["evaluation"]["records"][0]
    assert bad_verifier_record["artifact_complete"] is False
    assert (
        "VERIFIER_RESULT_1_PASS_MISMATCH"
        in bad_verifier_record["errors"]
    )

    # Tool use must bind to an existing DNA-12 decision/output record.
    bad_tool_input = deepcopy(through_dna25)
    bad_tool = _valid_artifact(through_dna25)
    bad_tool["tools"][0]["decision_id"] = (
        "DNA-12-DECISION-NOT-FOUND"
    )
    bad_tool_input["observability_artifacts"] = [
        bad_tool
    ]
    bad_tool_result = dna26_core.activate(bad_tool_input)
    bad_tool_record = bad_tool_result[
        "core54_outputs"
    ]["DNA-26"]["evaluation"]["records"][0]
    assert bad_tool_record["artifact_complete"] is False
    assert (
        "TOOL_1_DNA12_DECISION_NOT_FOUND"
        in bad_tool_record["errors"]
    )

    # Missing one canonical category cannot form a complete artifact.
    missing_category_input = deepcopy(through_dna25)
    missing_category = _valid_artifact(through_dna25)
    missing_category.pop("hypotheses")
    missing_category_input["observability_artifacts"] = [
        missing_category
    ]
    missing_category_result = dna26_core.activate(
        missing_category_input
    )
    missing_record = missing_category_result[
        "core54_outputs"
    ]["DNA-26"]["evaluation"]["records"][0]
    assert missing_record["artifact_complete"] is False
    assert (
        "OBSERVABILITY_ARTIFACT_FIELDS_MISSING"
        in missing_record["errors"]
    )

    # Tampering after storage must be detectable.
    tampered = deepcopy(record)
    tampered["decisions"][0]["statement"] = (
        "TAMPERED_DECISION"
    )
    assert _verify_artifact_integrity(tampered, None) is False

    tampered_registry_input = deepcopy(result)
    tampered_registry_input[
        "cognitive_state"
    ]["observability"]["artifacts"][0][
        "decisions"
    ][0]["statement"] = "TAMPERED_DECISION"
    tampered_registry_input["observability_artifacts"] = []
    try:
        dna26_core.activate(tampered_registry_input)
    except RuntimeError as exc:
        assert str(exc) == (
            "DNA-26_EXISTING_ARTIFACT_CHAIN_INVALID"
        )
    else:
        raise AssertionError(
            "DNA-26_ACCEPTED_TAMPERED_ARTIFACT_CHAIN"
        )

    # Artifact identifiers must remain unique.
    duplicate_input = deepcopy(through_dna25)
    duplicate_artifact = _valid_artifact(through_dna25)
    duplicate_input["observability_artifacts"] = [
        deepcopy(duplicate_artifact),
        deepcopy(duplicate_artifact),
    ]
    try:
        dna26_core.activate(duplicate_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-26_DUPLICATE_OBSERVABILITY_ARTIFACT_ID"
        )
    else:
        raise AssertionError(
            "DNA-26_ACCEPTED_DUPLICATE_ARTIFACT_ID"
        )

    # Reject provisional root-marker behavior as the official contract.
    assert "observability_artifact" not in result
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
        "core_id": "DNA-26",
        "canon_mapping": "PASS",
        "decisions_artifact": "PASS",
        "hypotheses_artifact": "PASS",
        "tools_artifact": "PASS",
        "verifier_results_artifact": "PASS",
        "confidence_artifact": "PASS",
        "lineage_artifact": "PASS",
        "artifact_integrity": "PASS",
        "append_chain": "PASS",
        "tamper_detection": "PASS",
        "external_persistence_started": False,
        "memory_runtime_used": False,
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
            "DNA-27"
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
            print("DNA-26_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = _load_prior_modules()
    except Exception as exc:
        print("DNA-26_FAIL: IMPORT_ERROR")
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

        for index in range(1, 26):
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

        report = self_check_dna26(
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
            for index in range(1, 27)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-26_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-26_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_26_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "DECISIONS_ARTIFACT:",
        report["decisions_artifact"],
    )
    print(
        "HYPOTHESES_ARTIFACT:",
        report["hypotheses_artifact"],
    )
    print(
        "TOOLS_ARTIFACT:",
        report["tools_artifact"],
    )
    print(
        "VERIFIER_RESULTS_ARTIFACT:",
        report["verifier_results_artifact"],
    )
    print(
        "CONFIDENCE_ARTIFACT:",
        report["confidence_artifact"],
    )
    print(
        "LINEAGE_ARTIFACT:",
        report["lineage_artifact"],
    )
    print(
        "ARTIFACT_INTEGRITY:",
        report["artifact_integrity"],
    )
    print("APPEND_CHAIN:", report["append_chain"])
    print(
        "TAMPER_DETECTION:",
        report["tamper_detection"],
    )
    print(
        "EXTERNAL_PERSISTENCE_STARTED:",
        report["external_persistence_started"],
    )
    print(
        "MEMORY_RUNTIME_USED:",
        report["memory_runtime_used"],
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
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 26/54")
    print("NEXT_AUTHORIZED: DNA-27")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
