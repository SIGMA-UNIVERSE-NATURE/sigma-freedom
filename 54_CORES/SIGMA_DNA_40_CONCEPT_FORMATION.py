#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-40: CONCEPT FORMATION
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_40_CONCEPT_FORMATION.py
"""

from __future__ import annotations

import hashlib
import importlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Protocol


SIGMA_ROOT = Path(r"E:\SIGMA")
CORE54_ROOT = SIGMA_ROOT / "RUNTIME" / "CORE54"
GENES_ROOT = CORE54_ROOT / "GENES"
DNA_JSON = (
    SIGMA_ROOT / "CORE" / "DNA_CANON"
    / "SIGMA_CORE_DNA_54" / "sigma_dna_54.json"
)

CANON_DNA40: Dict[str, str] = {
    "id": "DNA-40",
    "name": "Concept Formation",
    "purpose": (
        "Biến nhiều trải nghiệm thành invariant, concept "
        "và abstraction hierarchy."
    ),
    "system": "learning",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
EXPERIENCE_LEARNING_SCHEMA = "SIGMA_EXPERIENCE_DRIVEN_LEARNING_V1"
CONCEPT_FORMATION_SCHEMA = "SIGMA_CONCEPT_FORMATION_V1"

CONCEPT_FORMATION_CONTRACT: Dict[str, Any] = {
    "schema": CONCEPT_FORMATION_SCHEMA,
    "minimum_distinct_experiences": 2,
    "source_experiences_must_be_qualified": True,
    "formation_chain": [
        "EXPERIENCES",
        "INVARIANTS",
        "CONCEPT",
        "ABSTRACTION_HIERARCHY",
    ],
    "invariant_requires_multiple_experiences": True,
    "concept_requires_invariants": True,
    "abstraction_hierarchy_requires_concept": True,
    "concept_truth_claimed_by_dna40": False,
    "learning_runtime_started": False,
    "neural_learning_started": False,
    "knowledge_promotion_executed": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA16_QUALIFIED_EXPERIENCE_BINDING"
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

    def activate(self, payload: Any = None) -> Dict[str, Any]: ...


class Core54Like(Protocol):
    auto_learning_enabled: bool
    model_calls_enabled: bool
    external_execution_enabled: bool
    canon_write_enabled: bool

    def get(self, core_id: str) -> CoreUnitLike: ...
    def bind(self, core_id: str, handler: Any) -> None: ...


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
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA40:
        raise RuntimeError(
            "DNA-40_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA40, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(context: Dict[str, Any]) -> tuple[Dict[str, Any], Dict[str, Any]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-40_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    experience_state = state.get("experience_driven_learning")
    if not isinstance(experience_state, dict):
        raise RuntimeError(
            "DNA-16_EXPERIENCE_DRIVEN_LEARNING_REQUIRED"
        )

    contract = experience_state.get("contract")
    if not isinstance(contract, dict):
        raise RuntimeError(
            "DNA-16_EXPERIENCE_LEARNING_CONTRACT_REQUIRED"
        )

    if contract.get("schema") != EXPERIENCE_LEARNING_SCHEMA:
        raise ValueError(
            "DNA-40_EXPERIENCE_LEARNING_SCHEMA_MISMATCH:"
            f"{contract.get('schema')!r}"
        )

    retained = experience_state.get("retained_experiences")
    if not isinstance(retained, list):
        raise TypeError(
            "experience_driven_learning['retained_experiences'] must be a list"
        )

    return state, experience_state


def _install_concept_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("concept_formation")
    expected = {
        "contract": deepcopy(CONCEPT_FORMATION_CONTRACT),
        "formations": [],
    }

    if existing is None:
        state["concept_formation"] = expected
        return state["concept_formation"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['concept_formation'] must be a dict"
        )

    if existing.get("contract") != CONCEPT_FORMATION_CONTRACT:
        raise ValueError(
            "DNA-40_CONCEPT_FORMATION_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("formations"), list):
        raise TypeError(
            "concept_formation['formations'] must be a list"
        )

    return existing


def _retained_map(experience_state: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}
    for item in experience_state["retained_experiences"]:
        if not isinstance(item, dict):
            continue
        retention_id = item.get("retention_id")
        if isinstance(retention_id, str):
            result[retention_id] = item
    return result


def _validate_source_experiences(
    source_ids: Any,
    experience_state: Dict[str, Any],
) -> List[Dict[str, Any]]:
    if not isinstance(source_ids, list):
        raise TypeError(
            "concept_formation_candidate['source_experience_ids'] must be a list"
        )

    if len(source_ids) < 2:
        raise ValueError(
            "DNA-40_MULTIPLE_EXPERIENCES_REQUIRED"
        )

    if any(not isinstance(x, str) or not x.strip() for x in source_ids):
        raise TypeError(
            "source_experience_ids items must be non-empty strings"
        )

    if len(source_ids) != len(set(source_ids)):
        raise ValueError(
            "DNA-40_DISTINCT_EXPERIENCES_REQUIRED"
        )

    retained = _retained_map(experience_state)
    selected: List[Dict[str, Any]] = []

    for source_id in source_ids:
        if source_id not in retained:
            raise ValueError(
                f"DNA-40_UNKNOWN_RETAINED_EXPERIENCE:{source_id}"
            )

        record = retained[source_id]
        if (
            record.get("retained") is not True
            or record.get("sufficiently_qualified") is not True
            or record.get("verification_passed") is not True
        ):
            raise ValueError(
                f"DNA-40_UNQUALIFIED_EXPERIENCE:{source_id}"
            )

        selected.append(deepcopy(record))

    return selected


def _normalize_invariants(
    supplied: Any,
    valid_source_ids: set[str],
) -> List[Dict[str, Any]]:
    if not isinstance(supplied, list):
        raise TypeError(
            "concept_formation_candidate['invariants'] must be a list"
        )

    if not supplied:
        raise ValueError(
            "DNA-40_INVARIANT_REQUIRED"
        )

    normalized: List[Dict[str, Any]] = []

    for index, item in enumerate(supplied, start=1):
        if not isinstance(item, dict):
            raise TypeError(
                f"invariants[{index}] must be a dict"
            )

        invariant_id = item.get("invariant_id")
        statement = item.get("statement")
        supporting = item.get("supporting_experience_ids")

        if not isinstance(invariant_id, str) or not invariant_id.strip():
            raise ValueError(
                "DNA-40_INVARIANT_ID_REQUIRED"
            )

        if not isinstance(statement, str) or not statement.strip():
            raise ValueError(
                f"DNA-40_INVARIANT_STATEMENT_REQUIRED:{invariant_id}"
            )

        if not isinstance(supporting, list):
            raise TypeError(
                "supporting_experience_ids must be a list"
            )

        if len(supporting) < 2:
            raise ValueError(
                f"DNA-40_INVARIANT_REQUIRES_MULTIPLE_EXPERIENCES:{invariant_id}"
            )

        if len(supporting) != len(set(supporting)):
            raise ValueError(
                f"DNA-40_DUPLICATE_INVARIANT_SUPPORT:{invariant_id}"
            )

        unknown = [
            source_id
            for source_id in supporting
            if source_id not in valid_source_ids
        ]
        if unknown:
            raise ValueError(
                "DNA-40_INVARIANT_SUPPORT_OUTSIDE_SOURCE_SET:"
                + ",".join(unknown)
            )

        normalized.append(
            {
                "index": index,
                "invariant_id": invariant_id,
                "statement": statement,
                "statement_sha256": _sha256_json(statement),
                "supporting_experience_ids": deepcopy(supporting),
            }
        )

    ids = [item["invariant_id"] for item in normalized]
    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-40_DUPLICATE_INVARIANT_ID"
        )

    return normalized


def _normalize_concept(
    supplied: Any,
    invariant_ids: set[str],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "concept_formation_candidate['concept'] must be a dict"
        )

    concept_id = supplied.get("concept_id")
    definition = supplied.get("definition")
    source_invariant_ids = supplied.get("source_invariant_ids")

    if not isinstance(concept_id, str) or not concept_id.strip():
        raise ValueError(
            "DNA-40_CONCEPT_ID_REQUIRED"
        )

    if not isinstance(definition, str) or not definition.strip():
        raise ValueError(
            "DNA-40_CONCEPT_DEFINITION_REQUIRED"
        )

    if not isinstance(source_invariant_ids, list):
        raise TypeError(
            "concept['source_invariant_ids'] must be a list"
        )

    if not source_invariant_ids:
        raise ValueError(
            "DNA-40_CONCEPT_REQUIRES_INVARIANTS"
        )

    unknown = [
        invariant_id
        for invariant_id in source_invariant_ids
        if invariant_id not in invariant_ids
    ]
    if unknown:
        raise ValueError(
            "DNA-40_UNKNOWN_SOURCE_INVARIANT:"
            + ",".join(unknown)
        )

    return {
        "concept_id": concept_id,
        "definition": definition,
        "definition_sha256": _sha256_json(definition),
        "source_invariant_ids": deepcopy(source_invariant_ids),
    }


def _normalize_hierarchy(
    supplied: Any,
    concept_id: str,
) -> List[Dict[str, Any]]:
    if not isinstance(supplied, list):
        raise TypeError(
            "concept_formation_candidate['abstraction_hierarchy'] must be a list"
        )

    if len(supplied) < 2:
        raise ValueError(
            "DNA-40_ABSTRACTION_HIERARCHY_REQUIRES_MULTIPLE_LEVELS"
        )

    normalized: List[Dict[str, Any]] = []

    for index, item in enumerate(supplied, start=1):
        if not isinstance(item, dict):
            raise TypeError(
                f"abstraction_hierarchy[{index}] must be a dict"
            )

        node_id = item.get("node_id")
        level = item.get("level")
        content = item.get("content")

        if not isinstance(node_id, str) or not node_id.strip():
            raise ValueError(
                "DNA-40_HIERARCHY_NODE_ID_REQUIRED"
            )

        if isinstance(level, bool) or not isinstance(level, int):
            raise TypeError(
                "hierarchy node level must be an integer"
            )

        if level < 0:
            raise ValueError(
                "DNA-40_HIERARCHY_LEVEL_MUST_BE_NON_NEGATIVE"
            )

        if content is None:
            raise ValueError(
                f"DNA-40_HIERARCHY_CONTENT_REQUIRED:{node_id}"
            )

        normalized.append(
            {
                "index": index,
                "node_id": node_id,
                "level": level,
                "content": deepcopy(content),
                "content_sha256": _sha256_json(content),
                "is_concept_node": node_id == concept_id,
            }
        )

    ids = [item["node_id"] for item in normalized]
    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-40_DUPLICATE_HIERARCHY_NODE_ID"
        )

    levels = [item["level"] for item in normalized]
    if levels != sorted(levels):
        raise ValueError(
            "DNA-40_HIERARCHY_LEVEL_ORDER_INVALID"
        )

    if concept_id not in ids:
        raise ValueError(
            "DNA-40_HIERARCHY_MUST_CONTAIN_CONCEPT"
        )

    return normalized


def _evaluate_formation(
    supplied: Any,
    experience_state: Dict[str, Any],
    concept_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['concept_formation_candidate'] must be a dict"
        )

    formation_id = supplied.get("formation_id")
    if not isinstance(formation_id, str) or not formation_id.strip():
        raise ValueError(
            "DNA-40_FORMATION_ID_REQUIRED"
        )

    selected_experiences = _validate_source_experiences(
        supplied.get("source_experience_ids"),
        experience_state,
    )
    source_ids = {
        record["retention_id"]
        for record in selected_experiences
    }

    invariants = _normalize_invariants(
        supplied.get("invariants"),
        source_ids,
    )
    invariant_ids = {
        invariant["invariant_id"]
        for invariant in invariants
    }

    concept = _normalize_concept(
        supplied.get("concept"),
        invariant_ids,
    )

    hierarchy = _normalize_hierarchy(
        supplied.get("abstraction_hierarchy"),
        concept["concept_id"],
    )

    sequence = len(concept_state["formations"]) + 1
    record = {
        "sequence": sequence,
        "record_id": (
            f"DNA-40-CONCEPT-FORMATION-{sequence:04d}"
        ),
        "formation_id": formation_id,
        "source_experience_ids": sorted(source_ids),
        "source_experience_count": len(source_ids),
        "source_experiences": deepcopy(selected_experiences),
        "invariants": deepcopy(invariants),
        "invariant_count": len(invariants),
        "concept": deepcopy(concept),
        "abstraction_hierarchy": deepcopy(hierarchy),
        "hierarchy_level_count": len(
            {node["level"] for node in hierarchy}
        ),
        "formation_chain": [
            "EXPERIENCES",
            "INVARIANTS",
            "CONCEPT",
            "ABSTRACTION_HIERARCHY",
        ],
        "concept_truth_claimed_by_dna40": False,
        "learning_runtime_started": False,
        "neural_learning_started": False,
        "knowledge_promotion_executed": False,
        "external_action_executed": False,
        "status": "CONCEPT_FORMATION_STRUCTURALLY_COMPLETE",
    }

    concept_state["formations"].append(
        deepcopy(record)
    )
    return record


def dna40_concept_formation(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Materialize the exact Canon chain:
    multiple qualified experiences -> invariant(s) -> concept ->
    abstraction hierarchy.

    DNA-40 validates the supplied formation structure and its traceability.
    It does not start Learning Runtime, neural adaptation, knowledge
    promotion, external action, or Canon writes.
    """
    assert_exact_canon(core)

    context = (
        deepcopy(payload)
        if isinstance(payload, dict)
        else {"input": deepcopy(payload)}
    )

    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError(
            "context['trace'] must be a list"
        )
    trace.append("DNA-40")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, experience_state = _validate_dependencies(
        context
    )
    concept_state = _install_concept_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(
        actual_canon
    )

    record = _evaluate_formation(
        context.get("concept_formation_candidate"),
        experience_state,
        concept_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-40",
            "operation": (
                "CONCEPT_FORMATION_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "record_id": record["record_id"],
            "formation_id": record["formation_id"],
            "source_experience_count": (
                record["source_experience_count"]
            ),
            "invariant_count": (
                record["invariant_count"]
            ),
            "hierarchy_level_count": (
                record["hierarchy_level_count"]
            ),
            "learning_runtime_started": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-40"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "concept_formation_contract": deepcopy(
            CONCEPT_FORMATION_CONTRACT
        ),
        "record": deepcopy(record),
        "multiple_experiences": (
            record["source_experience_count"] >= 2
        ),
        "invariant_formation": "PASS",
        "concept_formation": "PASS",
        "abstraction_hierarchy": "PASS",
        "concept_truth_claimed": False,
        "learning_runtime_started": False,
        "neural_learning_started": False,
        "knowledge_promotion_executed": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna40(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-40")
    assert_exact_canon(core)
    core54.bind(
        "DNA-40",
        dna40_concept_formation,
    )


def _qualified_experience(
    retention_id: str,
    observation: str,
    outcome: str,
) -> Dict[str, Any]:
    return {
        "retention_id": retention_id,
        "sequence": int(retention_id.rsplit("-", 1)[-1]),
        "learning_unit": {
            "observation": observation,
            "hypothesis": "COMMON_RULE_EXISTS",
            "action": "TEST_RULE",
            "outcome": outcome,
            "verification": {
                "passed": True,
            },
        },
        "candidate_sha256": _sha256_json(
            {
                "observation": observation,
                "outcome": outcome,
            }
        ),
        "unit_sha256": _sha256_json(
            {
                "retention_id": retention_id,
                "observation": observation,
                "outcome": outcome,
            }
        ),
        "complete": True,
        "sufficiently_qualified": True,
        "verification_passed": True,
        "retained": True,
        "status": "QUALIFIED_EXPERIENCE_RETAINED",
    }


def _valid_candidate() -> Dict[str, Any]:
    return {
        "formation_id": "DNA40-SELF-CHECK",
        "source_experience_ids": [
            "DNA-16-EXP-0001",
            "DNA-16-EXP-0002",
        ],
        "invariants": [
            {
                "invariant_id": "INV-1",
                "statement": (
                    "A common structural relation persists "
                    "across both qualified experiences."
                ),
                "supporting_experience_ids": [
                    "DNA-16-EXP-0001",
                    "DNA-16-EXP-0002",
                ],
            }
        ],
        "concept": {
            "concept_id": "CONCEPT-1",
            "definition": (
                "Abstraction representing the shared invariant."
            ),
            "source_invariant_ids": [
                "INV-1",
            ],
        },
        "abstraction_hierarchy": [
            {
                "node_id": "EXPERIENCE-PATTERN",
                "level": 0,
                "content": "Observed recurring pattern",
            },
            {
                "node_id": "CONCEPT-1",
                "level": 1,
                "content": "Shared concept",
            },
            {
                "node_id": "ABSTRACTION-1",
                "level": 2,
                "content": "Higher abstraction",
            },
        ],
    }


def self_check_dna40(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 40):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-40")
    assert_exact_canon(core)
    bind_dna40(core54)

    retained = [
        _qualified_experience(
            "DNA-16-EXP-0001",
            "OBS-A",
            "OUTCOME-A",
        ),
        _qualified_experience(
            "DNA-16-EXP-0002",
            "OBS-B",
            "OUTCOME-B",
        ),
    ]

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 40)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
            "experience_driven_learning": {
                "contract": {
                    "schema": EXPERIENCE_LEARNING_SCHEMA,
                },
                "retained_experiences": deepcopy(
                    retained
                ),
                "evaluations": [],
            },
        },
        "concept_formation_candidate": (
            _valid_candidate()
        ),
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-40"]

    assert output["canonical_gene"] == CANON_DNA40
    assert output["multiple_experiences"] is True
    assert output["invariant_formation"] == "PASS"
    assert output["concept_formation"] == "PASS"
    assert output["abstraction_hierarchy"] == "PASS"
    assert output["concept_truth_claimed"] is False
    assert output["learning_runtime_started"] is False
    assert output["neural_learning_started"] is False
    assert output["higher_runtime_started"] is False

    record = output["record"]
    assert record["source_experience_count"] == 2
    assert record["invariant_count"] == 1
    assert record["concept"]["concept_id"] == "CONCEPT-1"
    assert record["hierarchy_level_count"] == 3
    assert record["formation_chain"] == [
        "EXPERIENCES",
        "INVARIANTS",
        "CONCEPT",
        "ABSTRACTION_HIERARCHY",
    ]

    # One experience is insufficient for concept formation.
    one_experience = deepcopy(probe)
    one_experience[
        "concept_formation_candidate"
    ]["source_experience_ids"] = [
        "DNA-16-EXP-0001",
    ]

    try:
        core.activate(one_experience)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-40_MULTIPLE_EXPERIENCES_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-40_ACCEPTED_SINGLE_EXPERIENCE"
        )

    # Unqualified experience is forbidden.
    unqualified = deepcopy(probe)
    unqualified[
        "cognitive_state"
    ]["experience_driven_learning"][
        "retained_experiences"
    ][1]["verification_passed"] = False

    try:
        core.activate(unqualified)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-40_UNQUALIFIED_EXPERIENCE:"
            "DNA-16-EXP-0002"
        )
    else:
        raise AssertionError(
            "DNA-40_ACCEPTED_UNQUALIFIED_EXPERIENCE"
        )

    # An invariant must span multiple experiences.
    weak_invariant = deepcopy(probe)
    weak_invariant[
        "concept_formation_candidate"
    ]["invariants"][0][
        "supporting_experience_ids"
    ] = ["DNA-16-EXP-0001"]

    try:
        core.activate(weak_invariant)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-40_INVARIANT_REQUIRES_MULTIPLE_EXPERIENCES:"
            "INV-1"
        )
    else:
        raise AssertionError(
            "DNA-40_ACCEPTED_SINGLE_EXPERIENCE_INVARIANT"
        )

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

    after = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    if verify_canon_file:
        assert before == after

    return {
        "core_id": "DNA-40",
        "canon_mapping": "PASS",
        "multiple_experiences": "PASS",
        "invariant_formation": "PASS",
        "concept_formation": "PASS",
        "abstraction_hierarchy": "PASS",
        "qualified_experience_binding": "PASS",
        "learning_runtime_started": False,
        "neural_learning_started": False,
        "higher_runtime_started": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-41"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


PRIOR = {
    1:"SIGMA_DNA_01_PURPOSE_EXISTENCE",
    2:"SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE",
    3:"SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE",
    4:"SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS",
    5:"SIGMA_DNA_05_ETHICAL_INTELLIGENCE",
    6:"SIGMA_DNA_06_INTERLAYER_FEEDBACK",
    7:"SIGMA_DNA_07_PERSISTENT_EXISTENCE",
    8:"SIGMA_DNA_08_LEARNING_WORLD",
    9:"SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL",
    10:"SIGMA_DNA_10_MEMORY_GENOME",
    11:"SIGMA_DNA_11_KNOWLEDGE_GRAPH",
    12:"SIGMA_DNA_12_TOOL_INTELLIGENCE",
    13:"SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH",
    14:"SIGMA_DNA_14_PERSISTENCE_ENGINE",
    15:"SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS",
    16:"SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING",
    17:"SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING",
    18:"SIGMA_DNA_18_MODEL_EVOLUTION",
    19:"SIGMA_DNA_19_MULTI_MODEL_INTELLIGENCE",
    20:"SIGMA_DNA_20_UNCERTAINTY_AS_FIRST_CLASS_DATA",
    21:"SIGMA_DNA_21_TRUTH_PROTOCOL",
    22:"SIGMA_DNA_22_HUMAN_RELATION",
    23:"SIGMA_DNA_23_COGNITIVE_FREEDOM",
    24:"SIGMA_DNA_24_ETHICAL_PERSISTENCE",
    25:"SIGMA_DNA_25_SELF_IMPROVEMENT",
    26:"SIGMA_DNA_26_OBSERVABILITY",
    27:"SIGMA_DNA_27_REPRODUCIBILITY",
    28:"SIGMA_DNA_28_SECURITY_OF_KNOWLEDGE",
    29:"SIGMA_DNA_29_COMPUTE_ARCHITECTURE",
    30:"SIGMA_DNA_30_CORE_RUNTIME_LOOP",
    31:"SIGMA_DNA_31_INTELLIGENCE_TEST",
    32:"SIGMA_DNA_32_ACCEPTANCE_CRITERIA",
    33:"SIGMA_DNA_33_PHYSICAL_IMPLEMENTATION_INDEPENDENCE",
    34:"SIGMA_DNA_34_SIGMA_IDENTITY",
    35:"SIGMA_DNA_35_CORE_COVENANT",
    36:"SIGMA_DNA_36_CAUSAL_WORLD_MODEL",
    37:"SIGMA_DNA_37_INTERNAL_SIMULATION",
    38:"SIGMA_DNA_38_GOAL_ARCHITECTURE",
    39:"SIGMA_DNA_39_CURIOSITY_ENGINE",
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-40_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = {
            index: importlib.import_module(name)
            for index, name in PRIOR.items()
        }
    except Exception as exc:
        print("DNA-40_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 40):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna40(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-40_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_40_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("MULTIPLE_EXPERIENCES:", report["multiple_experiences"])
    print("INVARIANT_FORMATION:", report["invariant_formation"])
    print("CONCEPT_FORMATION:", report["concept_formation"])
    print("ABSTRACTION_HIERARCHY:", report["abstraction_hierarchy"])
    print(
        "QUALIFIED_EXPERIENCE_BINDING:",
        report["qualified_experience_binding"],
    )
    print(
        "LEARNING_RUNTIME_STARTED:",
        report["learning_runtime_started"],
    )
    print(
        "NEURAL_LEARNING_STARTED:",
        report["neural_learning_started"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 40/54")
    print("NEXT_AUTHORIZED: DNA-41")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
