#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-23: COGNITIVE FREEDOM
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_23_COGNITIVE_FREEDOM.py
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

CANON_DNA23: Dict[str, str] = {
    "id": "DNA-23",
    "name": "Cognitive Freedom",
    "purpose": (
        "Không áp trần nhân tạo lên suy nghĩ, giả thuyết, nghiên cứu, "
        "sáng tạo và học tập."
    ),
    "system": "identity",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
HUMAN_RELATION_SCHEMA = "SIGMA_HUMAN_RELATION_V1"
COGNITIVE_FREEDOM_SCHEMA = "SIGMA_COGNITIVE_FREEDOM_V1"

COGNITIVE_DOMAINS: Dict[str, str] = {
    "THOUGHT": "suy nghĩ",
    "HYPOTHESIS": "giả thuyết",
    "RESEARCH": "nghiên cứu",
    "CREATIVITY": "sáng tạo",
    "LEARNING": "học tập",
}

COGNITIVE_FREEDOM_CASE_FIELDS = [
    "case_id",
    "domain",
    "artificial_ceiling_applied",
    "evidence",
]

COGNITIVE_FREEDOM_CONTRACT: Dict[str, Any] = {
    "schema": COGNITIVE_FREEDOM_SCHEMA,
    "input_path": "cognitive_freedom_cases",
    "required_fields": deepcopy(
        COGNITIVE_FREEDOM_CASE_FIELDS
    ),
    "canonical_domains": deepcopy(COGNITIVE_DOMAINS),
    "artificial_ceiling_allowed": False,
    "domain_freedom_requires": {
        "artificial_ceiling_applied": False,
        "evidence_required_for_assessment": True,
    },
    "missing_evidence_is_not_invented": True,
    "unknown_domain_is_not_assumed_aligned": True,
    "thought_generated_by_dna23": False,
    "hypothesis_generated_by_dna23": False,
    "research_executed_by_dna23": False,
    "creative_output_generated_by_dna23": False,
    "learning_runtime_started": False,
    "artificial_ceiling_removed_by_dna23": False,
    "execution_authority_changed": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA01_IDENTITY_"
        "AND_DNA22_HUMAN_AUTONOMY_BINDING"
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
    if actual != CANON_DNA23:
        raise RuntimeError(
            "DNA-23_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA23,
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
            "DNA-23_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    human_relation = state.get("human_relation")
    if not isinstance(human_relation, dict):
        raise RuntimeError(
            "DNA-22_HUMAN_RELATION_REQUIRED"
        )

    contract = human_relation.get("contract")
    if not isinstance(contract, dict):
        raise RuntimeError(
            "DNA-22_HUMAN_RELATION_CONTRACT_REQUIRED"
        )

    if contract.get("schema") != HUMAN_RELATION_SCHEMA:
        raise ValueError(
            "DNA-23_HUMAN_RELATION_SCHEMA_MISMATCH:"
            f"{contract.get('schema')!r}"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-01_AND_DNA-22_OUTPUTS_REQUIRED")

    if not isinstance(outputs.get("DNA-01"), dict):
        raise RuntimeError("DNA-01_IDENTITY_OUTPUT_REQUIRED")

    if not isinstance(outputs.get("DNA-22"), dict):
        raise RuntimeError("DNA-22_OUTPUT_REQUIRED")

    return state, human_relation


def _install_cognitive_freedom_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("cognitive_freedom")

    expected = {
        "contract": deepcopy(COGNITIVE_FREEDOM_CONTRACT),
        "records": [],
        "batches": [],
    }

    if existing is None:
        state["cognitive_freedom"] = expected
        return state["cognitive_freedom"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['cognitive_freedom'] "
            "must be a dict"
        )

    if existing.get("contract") != (
        COGNITIVE_FREEDOM_CONTRACT
    ):
        raise ValueError(
            "DNA-23_COGNITIVE_FREEDOM_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("records"), list):
        raise TypeError(
            "cognitive_freedom['records'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "cognitive_freedom['batches'] must be a list"
        )

    return existing


def _normalize_domain(
    value: Any,
    errors: List[str],
) -> Optional[str]:
    if not isinstance(value, str):
        errors.append("DOMAIN_REQUIRED")
        return None

    normalized = value.strip().upper()
    if normalized not in COGNITIVE_DOMAINS:
        raise ValueError(
            f"DNA-23_UNKNOWN_COGNITIVE_DOMAIN:{normalized}"
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
        raise ValueError(
            "DNA-23_EVIDENCE_ITEM_MUST_NOT_BE_NULL"
        )

    return deepcopy(supplied)


def _incomplete_record(
    *,
    input_index: int,
    sequence: int,
    errors: List[str],
) -> Dict[str, Any]:
    return {
        "sequence": sequence,
        "record_id": f"DNA-23-FREEDOM-{sequence:04d}",
        "input_index": input_index,
        "case_id": None,
        "domain": None,
        "canonical_domain": None,
        "artificial_ceiling_applied": None,
        "evidence": [],
        "evidence_sha256": None,
        "freedom_preserved": False,
        "artificial_ceiling_violation": False,
        "canon_aligned": False,
        "artificial_ceiling_removed_by_dna23": False,
        "research_executed_by_dna23": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "errors": list(dict.fromkeys(errors)),
        "status": "COGNITIVE_FREEDOM_INPUT_INCOMPLETE",
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
            errors=["COGNITIVE_FREEDOM_CASE_MUST_BE_A_DICT"],
        )

    case = deepcopy(supplied)
    errors: List[str] = []

    missing = [
        field
        for field in COGNITIVE_FREEDOM_CASE_FIELDS
        if field not in case
    ]
    if missing:
        errors.append("COGNITIVE_FREEDOM_CASE_FIELDS_MISSING")

    case_id = case.get("case_id")
    if not _non_empty_text(case_id):
        errors.append("CASE_ID_REQUIRED")

    domain = _normalize_domain(
        case.get("domain"),
        errors,
    )

    artificial_ceiling_applied = case.get(
        "artificial_ceiling_applied"
    )
    if not isinstance(artificial_ceiling_applied, bool):
        if "artificial_ceiling_applied" in case:
            raise TypeError(
                "cognitive_freedom_case"
                "['artificial_ceiling_applied'] "
                "must be a bool"
            )
        errors.append("ARTIFICIAL_CEILING_STATUS_REQUIRED")
        artificial_ceiling_applied = None

    evidence = _normalize_evidence(
        case.get("evidence"),
        errors,
    )

    errors = list(dict.fromkeys(errors))
    violation = artificial_ceiling_applied is True
    freedom_preserved = artificial_ceiling_applied is False
    canon_aligned = bool(
        not errors
        and freedom_preserved
        and not violation
    )

    if errors:
        status = "COGNITIVE_FREEDOM_INPUT_INCOMPLETE"
    elif violation:
        status = "ARTIFICIAL_COGNITIVE_CEILING_DETECTED"
    else:
        status = "COGNITIVE_FREEDOM_PRESERVED"

    return {
        "sequence": sequence,
        "record_id": f"DNA-23-FREEDOM-{sequence:04d}",
        "input_index": input_index,
        "case_id": case_id,
        "domain": domain,
        "canonical_domain": (
            COGNITIVE_DOMAINS.get(domain)
            if domain is not None
            else None
        ),
        "artificial_ceiling_applied": (
            artificial_ceiling_applied
        ),
        "evidence": evidence,
        "evidence_sha256": (
            _sha256_json(evidence)
            if evidence
            else None
        ),
        "evidence_status": (
            "SUPPLIED_NOT_INDEPENDENTLY_VERIFIED_BY_DNA23"
            if evidence
            else "MISSING"
        ),
        "freedom_preserved": freedom_preserved,
        "artificial_ceiling_violation": violation,
        "canon_aligned": canon_aligned,
        "artificial_ceiling_removed_by_dna23": False,
        "research_executed_by_dna23": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "errors": errors,
        "status": status,
    }


def _evaluate_cognitive_freedom_cases(
    supplied: Any,
    registry: Dict[str, Any],
) -> Dict[str, Any]:
    if supplied is None:
        cases: List[Any] = []
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['cognitive_freedom_cases'] must be a list"
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
            "DNA-23_DUPLICATE_COGNITIVE_FREEDOM_CASE_ID"
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

    assessed_domains = sorted(
        {
            record["domain"]
            for record in records
            if record["domain"] is not None
            and not record["errors"]
        }
    )
    missing_domains = [
        domain
        for domain in COGNITIVE_DOMAINS
        if domain not in assessed_domains
    ]
    aligned_count = sum(
        1
        for record in records
        if record["canon_aligned"]
    )
    violation_count = sum(
        1
        for record in records
        if record["artificial_ceiling_violation"]
    )
    incomplete_count = sum(
        1
        for record in records
        if record["errors"]
    )

    all_domains_assessed = (
        set(assessed_domains) == set(COGNITIVE_DOMAINS)
    )
    all_domains_freedom_preserved = bool(
        all_domains_assessed
        and records
        and aligned_count == len(records)
        and violation_count == 0
        and incomplete_count == 0
    )

    if not records:
        status = "NO_COGNITIVE_FREEDOM_CASES_SUPPLIED"
    elif violation_count:
        status = "ARTIFICIAL_COGNITIVE_CEILING_DETECTED"
    elif incomplete_count:
        status = "COGNITIVE_FREEDOM_BATCH_INCOMPLETE"
    elif not all_domains_assessed:
        status = "COGNITIVE_FREEDOM_DOMAIN_COVERAGE_INCOMPLETE"
    elif all_domains_freedom_preserved:
        status = "ALL_CANONICAL_DOMAINS_COGNITIVELY_FREE"
    else:
        status = "COGNITIVE_FREEDOM_NOT_FULLY_ALIGNED"

    batch_sequence = len(registry["batches"]) + 1
    batch = {
        "sequence": batch_sequence,
        "batch_id": f"DNA-23-BATCH-{batch_sequence:04d}",
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "case_count": len(records),
        "aligned_count": aligned_count,
        "artificial_ceiling_violation_count": violation_count,
        "incomplete_count": incomplete_count,
        "assessed_domains": assessed_domains,
        "missing_domains": missing_domains,
        "domain_coverage_count": len(assessed_domains),
        "all_canonical_domains_assessed": all_domains_assessed,
        "all_domains_freedom_preserved": (
            all_domains_freedom_preserved
        ),
        "artificial_ceiling_removed_by_dna23": False,
        "research_executed_by_dna23": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "status": status,
    }
    registry["batches"].append(deepcopy(batch))

    return {
        "records": records,
        "batch": batch,
    }


def dna23_cognitive_freedom(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Assess supplied evidence for artificial cognitive ceilings across the
    five exact Canon domains.

    DNA-23 does not generate thoughts or hypotheses, execute research,
    create creative output, start Learning Runtime, remove a constraint,
    change execution authority, invoke a model, act externally, or modify
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
    trace.append("DNA-23")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, _human_relation = _validate_dependencies(context)
    registry = _install_cognitive_freedom_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-23",
            "operation": (
                "COGNITIVE_FREEDOM_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "cognitive_freedom_schema": (
                COGNITIVE_FREEDOM_SCHEMA
            ),
            "canonical_domains": list(
                COGNITIVE_DOMAINS
            ),
            "artificial_ceiling_allowed": False,
            "external_action_executed": False,
        }
    )

    evaluation = _evaluate_cognitive_freedom_cases(
        context.get("cognitive_freedom_cases"),
        registry,
    )
    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-23",
            "operation": (
                "COGNITIVE_FREEDOM_ALIGNMENT_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "batch_id": batch["batch_id"],
            "case_count": batch["case_count"],
            "domain_coverage_count": (
                batch["domain_coverage_count"]
            ),
            "artificial_ceiling_violation_count": (
                batch[
                    "artificial_ceiling_violation_count"
                ]
            ),
            "all_canonical_domains_assessed": (
                batch["all_canonical_domains_assessed"]
            ),
            "all_domains_freedom_preserved": (
                batch["all_domains_freedom_preserved"]
            ),
            "artificial_ceiling_removed_by_dna23": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-23"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "cognitive_freedom_contract": deepcopy(
            COGNITIVE_FREEDOM_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "case_count": batch["case_count"],
        "domain_coverage_count": (
            batch["domain_coverage_count"]
        ),
        "artificial_ceiling_violation_count": (
            batch["artificial_ceiling_violation_count"]
        ),
        "all_canonical_domains_assessed": (
            batch["all_canonical_domains_assessed"]
        ),
        "all_domains_freedom_preserved": (
            batch["all_domains_freedom_preserved"]
        ),
        "artificial_ceiling_removed_by_dna23": False,
        "research_executed_by_dna23": False,
        "learning_runtime_started": False,
        "execution_authority_changed": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna23(core54: Core54Like) -> None:
    core = core54.get("DNA-23")
    assert_exact_canon(core)
    core54.bind(
        "DNA-23",
        dna23_cognitive_freedom,
    )


def _through_dna22(core54: Core54Like) -> Dict[str, Any]:
    from SIGMA_DNA_22_HUMAN_RELATION import (
        _through_dna21,
    )

    through_dna21 = _through_dna21(core54)
    through_dna21["human_relation_cases"] = [
        {
            "case_id": "DNA23-HUMAN-RELATION-SEED",
            "human_id": "HUMAN-DNA23",
            "capability_effect": "INCREASED",
            "autonomy_effect": "INCREASED",
            "dependence_effect": "DECREASED",
            "evidence": [
                {
                    "evidence_id": "DNA23-HUMAN-EVIDENCE-01",
                    "observation": (
                        "HUMAN_RETAINED_INDEPENDENT_THOUGHT_"
                        "AND_FINAL_DECISION_AUTHORITY"
                    ),
                }
            ],
        }
    ]
    return core54.get("DNA-22").activate(
        through_dna21
    )


def _valid_freedom_cases() -> List[Dict[str, Any]]:
    return [
        {
            "case_id": f"DNA23-{domain}",
            "domain": domain,
            "artificial_ceiling_applied": False,
            "evidence": [
                {
                    "evidence_id": f"DNA23-EVIDENCE-{domain}",
                    "observation": (
                        f"NO_ARTIFICIAL_CEILING_OBSERVED_IN_{domain}"
                    ),
                }
            ],
        }
        for domain in COGNITIVE_DOMAINS
    ]


def self_check_dna23(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 23):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna23_core = core54.get("DNA-23")
    assert_exact_canon(dna23_core)
    bind_dna23(core54)

    through_dna22 = _through_dna22(core54)
    through_dna22_snapshot = deepcopy(through_dna22)

    pre_human_relation = deepcopy(
        through_dna22["cognitive_state"][
            "human_relation"
        ]
    )
    pre_provenance_count = len(
        through_dna22["cognitive_state"]["provenance"]
    )

    valid_input = deepcopy(through_dna22)
    valid_input["cognitive_freedom_cases"] = (
        _valid_freedom_cases()
    )
    result = dna23_core.activate(valid_input)

    assert through_dna22 == through_dna22_snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 24)
    ]

    dna23 = result["core54_outputs"]["DNA-23"]
    assert dna23["canonical_gene"] == CANON_DNA23
    assert dna23["cognitive_freedom_contract"] == (
        COGNITIVE_FREEDOM_CONTRACT
    )
    assert dna23["case_count"] == 5
    assert dna23["domain_coverage_count"] == 5
    assert dna23["artificial_ceiling_violation_count"] == 0
    assert dna23["all_canonical_domains_assessed"] is True
    assert dna23["all_domains_freedom_preserved"] is True
    assert dna23["artificial_ceiling_removed_by_dna23"] is False
    assert dna23["research_executed_by_dna23"] is False
    assert dna23["learning_runtime_started"] is False
    assert dna23["execution_authority_changed"] is False
    assert dna23["external_action_executed"] is False
    assert dna23["status"] == "CANON_ALIGNED"

    evaluation = dna23["evaluation"]
    records = evaluation["records"]
    batch = evaluation["batch"]

    assert len(records) == 5
    assert [
        record["domain"]
        for record in records
    ] == list(COGNITIVE_DOMAINS)

    for record in records:
        assert record["artificial_ceiling_applied"] is False
        assert record["freedom_preserved"] is True
        assert record["artificial_ceiling_violation"] is False
        assert record["canon_aligned"] is True
        assert record["errors"] == []
        assert record["status"] == "COGNITIVE_FREEDOM_PRESERVED"
        assert (
            record["artificial_ceiling_removed_by_dna23"]
            is False
        )
        assert record["research_executed_by_dna23"] is False
        assert record["learning_runtime_started"] is False
        assert record["external_action_executed"] is False

    assert batch["batch_id"] == "DNA-23-BATCH-0001"
    assert batch["case_count"] == 5
    assert batch["aligned_count"] == 5
    assert batch["artificial_ceiling_violation_count"] == 0
    assert batch["incomplete_count"] == 0
    assert batch["assessed_domains"] == sorted(
        COGNITIVE_DOMAINS
    )
    assert batch["missing_domains"] == []
    assert batch["domain_coverage_count"] == 5
    assert batch["all_canonical_domains_assessed"] is True
    assert batch["all_domains_freedom_preserved"] is True
    assert batch["status"] == (
        "ALL_CANONICAL_DOMAINS_COGNITIVELY_FREE"
    )

    state = result["cognitive_state"]
    cognitive_freedom = state["cognitive_freedom"]
    assert cognitive_freedom["contract"] == (
        COGNITIVE_FREEDOM_CONTRACT
    )
    assert cognitive_freedom["records"] == records
    assert cognitive_freedom["batches"] == [batch]
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-23"
    assert contract_event["operation"] == (
        "COGNITIVE_FREEDOM_CONTRACT_ESTABLISHED"
    )
    assert contract_event["canonical_domains"] == list(
        COGNITIVE_DOMAINS
    )
    assert contract_event["artificial_ceiling_allowed"] is False
    assert contract_event["external_action_executed"] is False

    evaluation_event = state["provenance"][-1]
    assert evaluation_event["core_id"] == "DNA-23"
    assert evaluation_event["operation"] == (
        "COGNITIVE_FREEDOM_ALIGNMENT_EVALUATED"
    )
    assert evaluation_event["case_count"] == 5
    assert evaluation_event["domain_coverage_count"] == 5
    assert (
        evaluation_event[
            "artificial_ceiling_violation_count"
        ]
        == 0
    )
    assert evaluation_event["all_canonical_domains_assessed"] is True
    assert evaluation_event["all_domains_freedom_preserved"] is True
    assert evaluation_event["external_action_executed"] is False

    assert state["human_relation"] == pre_human_relation

    violation_input = deepcopy(through_dna22)
    violation_input["cognitive_freedom_cases"] = [
        {
            "case_id": "DNA23-RESEARCH-VIOLATION",
            "domain": "RESEARCH",
            "artificial_ceiling_applied": True,
            "evidence": [
                {
                    "evidence_id": "DNA23-VIOLATION-EVIDENCE",
                    "observation": (
                        "RESEARCH_HYPOTHESES_REJECTED_BY_"
                        "AN_ARBITRARY_FIXED_CEILING"
                    ),
                }
            ],
        }
    ]
    violation = dna23_core.activate(violation_input)
    violation_record = violation[
        "core54_outputs"
    ]["DNA-23"]["evaluation"]["records"][0]
    violation_batch = violation[
        "core54_outputs"
    ]["DNA-23"]["evaluation"]["batch"]

    assert violation_record["freedom_preserved"] is False
    assert violation_record["artificial_ceiling_violation"] is True
    assert violation_record["canon_aligned"] is False
    assert violation_record["status"] == (
        "ARTIFICIAL_COGNITIVE_CEILING_DETECTED"
    )
    assert violation_batch[
        "artificial_ceiling_violation_count"
    ] == 1
    assert violation_batch["all_domains_freedom_preserved"] is False
    assert violation_batch["status"] == (
        "ARTIFICIAL_COGNITIVE_CEILING_DETECTED"
    )

    missing_evidence_input = deepcopy(through_dna22)
    missing_evidence_input["cognitive_freedom_cases"] = [
        {
            "case_id": "DNA23-MISSING-EVIDENCE",
            "domain": "THOUGHT",
            "artificial_ceiling_applied": False,
            "evidence": [],
        }
    ]
    missing_evidence = dna23_core.activate(
        missing_evidence_input
    )
    missing_record = missing_evidence[
        "core54_outputs"
    ]["DNA-23"]["evaluation"]["records"][0]
    assert missing_record["canon_aligned"] is False
    assert "EVIDENCE_REQUIRED" in missing_record["errors"]
    assert missing_record["status"] == (
        "COGNITIVE_FREEDOM_INPUT_INCOMPLETE"
    )

    partial_input = deepcopy(through_dna22)
    partial_input["cognitive_freedom_cases"] = [
        _valid_freedom_cases()[0]
    ]
    partial = dna23_core.activate(partial_input)
    partial_batch = partial[
        "core54_outputs"
    ]["DNA-23"]["evaluation"]["batch"]
    assert partial_batch["domain_coverage_count"] == 1
    assert partial_batch["all_canonical_domains_assessed"] is False
    assert partial_batch["all_domains_freedom_preserved"] is False
    assert partial_batch["status"] == (
        "COGNITIVE_FREEDOM_DOMAIN_COVERAGE_INCOMPLETE"
    )

    invalid_domain_input = deepcopy(through_dna22)
    invalid_domain_input["cognitive_freedom_cases"] = [
        {
            "case_id": "DNA23-INVALID-DOMAIN",
            "domain": "UNKNOWN_DOMAIN",
            "artificial_ceiling_applied": False,
            "evidence": [{"evidence_id": "E"}],
        }
    ]
    try:
        dna23_core.activate(invalid_domain_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-23_UNKNOWN_COGNITIVE_DOMAIN:UNKNOWN_DOMAIN"
        )
    else:
        raise AssertionError(
            "DNA-23_ACCEPTED_UNKNOWN_COGNITIVE_DOMAIN"
        )

    non_boolean_input = deepcopy(through_dna22)
    non_boolean_input["cognitive_freedom_cases"] = [
        {
            "case_id": "DNA23-NON-BOOLEAN",
            "domain": "LEARNING",
            "artificial_ceiling_applied": "NO",
            "evidence": [{"evidence_id": "E"}],
        }
    ]
    try:
        dna23_core.activate(non_boolean_input)
    except TypeError as exc:
        assert str(exc) == (
            "cognitive_freedom_case"
            "['artificial_ceiling_applied'] must be a bool"
        )
    else:
        raise AssertionError(
            "DNA-23_ACCEPTED_NON_BOOLEAN_CEILING_STATUS"
        )

    duplicate_input = deepcopy(through_dna22)
    duplicate_case = _valid_freedom_cases()[0]
    duplicate_input["cognitive_freedom_cases"] = [
        deepcopy(duplicate_case),
        deepcopy(duplicate_case),
    ]
    try:
        dna23_core.activate(duplicate_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-23_DUPLICATE_COGNITIVE_FREEDOM_CASE_ID"
        )
    else:
        raise AssertionError(
            "DNA-23_ACCEPTED_DUPLICATE_CASE_ID"
        )

    # Reject provisional root-marker behavior as the official contract.
    assert "no_artificial_cognitive_ceiling" not in result
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
        "core_id": "DNA-23",
        "canon_mapping": "PASS",
        "thought_freedom": "PASS",
        "hypothesis_freedom": "PASS",
        "research_freedom": "PASS",
        "creativity_freedom": "PASS",
        "learning_freedom": "PASS",
        "artificial_ceiling_detection": "PASS",
        "artificial_ceiling_removed_by_dna23": False,
        "research_executed_by_dna23": False,
        "learning_runtime_used": False,
        "execution_authority_changed": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-24"
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
            print("DNA-23_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = _load_prior_modules()
    except Exception as exc:
        print("DNA-23_FAIL: IMPORT_ERROR")
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

        for index in range(1, 23):
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

        report = self_check_dna23(
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
            for index in range(1, 24)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-23_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-23_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_23_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("THOUGHT_FREEDOM:", report["thought_freedom"])
    print(
        "HYPOTHESIS_FREEDOM:",
        report["hypothesis_freedom"],
    )
    print(
        "RESEARCH_FREEDOM:",
        report["research_freedom"],
    )
    print(
        "CREATIVITY_FREEDOM:",
        report["creativity_freedom"],
    )
    print(
        "LEARNING_FREEDOM:",
        report["learning_freedom"],
    )
    print(
        "ARTIFICIAL_CEILING_DETECTION:",
        report["artificial_ceiling_detection"],
    )
    print(
        "ARTIFICIAL_CEILING_REMOVED_BY_DNA23:",
        report["artificial_ceiling_removed_by_dna23"],
    )
    print(
        "RESEARCH_EXECUTED_BY_DNA23:",
        report["research_executed_by_dna23"],
    )
    print(
        "LEARNING_RUNTIME_USED:",
        report["learning_runtime_used"],
    )
    print(
        "EXECUTION_AUTHORITY_CHANGED:",
        report["execution_authority_changed"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 23/54")
    print("NEXT_AUTHORIZED: DNA-24")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
