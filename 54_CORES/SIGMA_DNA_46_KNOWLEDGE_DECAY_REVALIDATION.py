#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-46: KNOWLEDGE DECAY & REVALIDATION
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_46_KNOWLEDGE_DECAY_REVALIDATION.py
"""

from __future__ import annotations

import hashlib
import importlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Protocol


SIGMA_ROOT = Path(r"E:\SIGMA")
CORE54_ROOT = SIGMA_ROOT / "RUNTIME" / "CORE54"
GENES_ROOT = CORE54_ROOT / "GENES"
DNA_JSON = (
    SIGMA_ROOT / "CORE" / "DNA_CANON"
    / "SIGMA_CORE_DNA_54" / "sigma_dna_54.json"
)

CANON_DNA46: Dict[str, str] = {
    "id": "DNA-46",
    "name": "Knowledge Decay & Revalidation",
    "purpose": (
        "Tri thức động phải được revalidate; hệ thống biết tri thức nào "
        "có thể lỗi thời."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
KNOWLEDGE_PROVENANCE_SCHEMA = "SIGMA_KNOWLEDGE_PROVENANCE_V1"
KNOWLEDGE_DECAY_SCHEMA = "SIGMA_KNOWLEDGE_DECAY_REVALIDATION_V1"

KNOWLEDGE_DECAY_CONTRACT: Dict[str, Any] = {
    "schema": KNOWLEDGE_DECAY_SCHEMA,
    "dynamic_knowledge_requires_revalidation": True,
    "staleness_risk_must_be_explicit": True,
    "static_knowledge_is_not_forced_dynamic": True,
    "missing_revalidation_result_is_not_invented": True,
    "revalidation_execution_started": False,
    "knowledge_replaced_by_dna46": False,
    "knowledge_deleted_by_dna46": False,
    "memory_runtime_started": False,
    "learning_runtime_started": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA45_PROVENANCE_BINDING"
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
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA46:
        raise RuntimeError(
            "DNA-46_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA46, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> tuple[Dict[str, Any], Dict[str, Any]]:
    state = context.get("cognitive_state")

    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-46_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    provenance_state = state.get("knowledge_provenance")

    if not isinstance(provenance_state, dict):
        raise RuntimeError(
            "DNA-45_KNOWLEDGE_PROVENANCE_REQUIRED"
        )

    contract = provenance_state.get("contract")
    if not isinstance(contract, dict):
        raise RuntimeError(
            "DNA-45_KNOWLEDGE_PROVENANCE_CONTRACT_REQUIRED"
        )

    if contract.get("schema") != KNOWLEDGE_PROVENANCE_SCHEMA:
        raise ValueError(
            "DNA-46_KNOWLEDGE_PROVENANCE_SCHEMA_MISMATCH:"
            f"{contract.get('schema')!r}"
        )

    if not isinstance(provenance_state.get("records"), list):
        raise TypeError(
            "knowledge_provenance['records'] must be a list"
        )

    return state, provenance_state


def _install_decay_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get(
        "knowledge_decay_revalidation"
    )

    expected = {
        "contract": deepcopy(
            KNOWLEDGE_DECAY_CONTRACT
        ),
        "assessments": [],
    }

    if existing is None:
        state[
            "knowledge_decay_revalidation"
        ] = expected
        return state[
            "knowledge_decay_revalidation"
        ]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['knowledge_decay_revalidation'] "
            "must be a dict"
        )

    if existing.get("contract") != KNOWLEDGE_DECAY_CONTRACT:
        raise ValueError(
            "DNA-46_KNOWLEDGE_DECAY_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("assessments"), list):
        raise TypeError(
            "knowledge_decay_revalidation['assessments'] "
            "must be a list"
        )

    return existing


def _provenance_by_knowledge_id(
    provenance_state: Dict[str, Any],
) -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}

    for record in provenance_state["records"]:
        if not isinstance(record, dict):
            continue

        knowledge_id = record.get("knowledge_id")
        if isinstance(knowledge_id, str):
            result[knowledge_id] = record

    return result


def _normalize_assessment(
    supplied: Any,
    *,
    index: int,
    sequence: int,
    provenance_map: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"knowledge_decay_assessments[{index}] must be a dict"
        )

    assessment_id = supplied.get("assessment_id")
    knowledge_id = supplied.get("knowledge_id")
    dynamic = supplied.get("dynamic")
    stale_possible = supplied.get("stale_possible")
    stale_evidence = supplied.get("stale_evidence", [])
    revalidation_required = supplied.get(
        "revalidation_required"
    )
    revalidation_result = supplied.get(
        "revalidation_result"
    )

    if not isinstance(
        assessment_id,
        str,
    ) or not assessment_id.strip():
        raise ValueError(
            "DNA-46_ASSESSMENT_ID_REQUIRED"
        )

    if not isinstance(
        knowledge_id,
        str,
    ) or not knowledge_id.strip():
        raise ValueError(
            "DNA-46_KNOWLEDGE_ID_REQUIRED"
        )

    if knowledge_id not in provenance_map:
        raise ValueError(
            f"DNA-46_UNKNOWN_PROVENANCE_KNOWLEDGE:{knowledge_id}"
        )

    if not isinstance(dynamic, bool):
        raise TypeError(
            "knowledge decay dynamic must be a bool"
        )

    if not isinstance(stale_possible, bool):
        raise TypeError(
            "knowledge decay stale_possible must be a bool"
        )

    if not isinstance(stale_evidence, list):
        raise TypeError(
            "knowledge decay stale_evidence must be a list"
        )

    if stale_possible and not stale_evidence:
        raise ValueError(
            f"DNA-46_STALENESS_REQUIRES_EVIDENCE:{knowledge_id}"
        )

    if not isinstance(revalidation_required, bool):
        raise TypeError(
            "knowledge decay revalidation_required must be a bool"
        )

    if dynamic and not revalidation_required:
        raise ValueError(
            f"DNA-46_DYNAMIC_KNOWLEDGE_MUST_REVALIDATE:{knowledge_id}"
        )

    if (
        revalidation_result is not None
        and not isinstance(revalidation_result, dict)
    ):
        raise TypeError(
            "knowledge decay revalidation_result "
            "must be a dict or None"
        )

    source = provenance_map[knowledge_id]

    return {
        "sequence": sequence,
        "record_id": (
            f"DNA-46-DECAY-{sequence:04d}"
        ),
        "input_index": index,
        "assessment_id": assessment_id,
        "knowledge_id": knowledge_id,
        "source_provenance_record_id": (
            source.get("record_id")
        ),
        "source_version": (
            source.get("version")
        ),
        "source_time": (
            source.get("time")
        ),
        "dynamic": dynamic,
        "stale_possible": stale_possible,
        "stale_evidence": deepcopy(
            stale_evidence
        ),
        "stale_evidence_sha256": (
            _sha256_json(stale_evidence)
            if stale_evidence
            else None
        ),
        "revalidation_required": revalidation_required,
        "revalidation_result": deepcopy(
            revalidation_result
        ),
        "revalidation_complete": (
            revalidation_result is not None
        ),
        "revalidation_execution_started": False,
        "knowledge_replaced_by_dna46": False,
        "knowledge_deleted_by_dna46": False,
        "status": (
            "REVALIDATION_RESULT_SUPPLIED"
            if revalidation_result is not None
            else (
                "REVALIDATION_REQUIRED"
                if revalidation_required
                else "REVALIDATION_NOT_REQUIRED"
            )
        ),
    }


def _evaluate(
    supplied: Any,
    provenance_state: Dict[str, Any],
    decay_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, list):
        raise TypeError(
            "context['knowledge_decay_assessments'] must be a list"
        )

    provenance_map = _provenance_by_knowledge_id(
        provenance_state
    )

    start = len(
        decay_state["assessments"]
    ) + 1

    records = [
        _normalize_assessment(
            item,
            index=index,
            sequence=start + index - 1,
            provenance_map=provenance_map,
        )
        for index, item in enumerate(
            supplied,
            start=1,
        )
    ]

    ids = [
        record["assessment_id"]
        for record in records
    ]

    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-46_DUPLICATE_ASSESSMENT_ID"
        )

    decay_state["assessments"].extend(
        deepcopy(records)
    )

    dynamic_ids = [
        record["knowledge_id"]
        for record in records
        if record["dynamic"]
    ]

    stale_possible_ids = [
        record["knowledge_id"]
        for record in records
        if record["stale_possible"]
    ]

    revalidation_required_ids = [
        record["knowledge_id"]
        for record in records
        if record["revalidation_required"]
    ]

    return {
        "records": records,
        "record_count": len(records),
        "dynamic_knowledge_ids": dynamic_ids,
        "stale_possible_knowledge_ids": (
            stale_possible_ids
        ),
        "revalidation_required_knowledge_ids": (
            revalidation_required_ids
        ),
        "dynamic_revalidation_gate": all(
            (
                not record["dynamic"]
                or record["revalidation_required"]
            )
            for record in records
        ),
    }


def dna46_knowledge_decay_revalidation(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Identify which provenance-backed knowledge is dynamic, which may become
    stale, and which therefore requires revalidation.

    DNA-46 records supplied revalidation results but does not execute
    revalidation, replace/delete knowledge, start Memory/Learning Runtime,
    call models, perform external actions, or modify Canon.
    """
    assert_exact_canon(core)

    context = (
        deepcopy(payload)
        if isinstance(payload, dict)
        else {"input": deepcopy(payload)}
    )

    trace = context.setdefault(
        "trace",
        [],
    )
    if not isinstance(trace, list):
        raise TypeError(
            "context['trace'] must be a list"
        )
    trace.append("DNA-46")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] "
            "must be a dict"
        )

    state, provenance_state = (
        _validate_dependencies(
            context
        )
    )

    decay_state = _install_decay_state(
        state
    )

    actual_canon = _canon_record(
        core
    )
    canonical_sha256 = _sha256_json(
        actual_canon
    )

    evaluation = _evaluate(
        context.get(
            "knowledge_decay_assessments"
        ),
        provenance_state,
        decay_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-46",
            "operation": (
                "KNOWLEDGE_DECAY_AND_REVALIDATION_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "record_count": evaluation[
                "record_count"
            ],
            "dynamic_knowledge_ids": deepcopy(
                evaluation[
                    "dynamic_knowledge_ids"
                ]
            ),
            "stale_possible_knowledge_ids": deepcopy(
                evaluation[
                    "stale_possible_knowledge_ids"
                ]
            ),
            "revalidation_required_ids": deepcopy(
                evaluation[
                    "revalidation_required_knowledge_ids"
                ]
            ),
            "revalidation_execution_started": False,
            "knowledge_modified": False,
        }
    )

    outputs["DNA-46"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "knowledge_decay_contract": deepcopy(
            KNOWLEDGE_DECAY_CONTRACT
        ),
        "evaluation": deepcopy(
            evaluation
        ),
        "dynamic_knowledge_detection": "PASS",
        "staleness_awareness": "PASS",
        "revalidation_requirement": "PASS",
        "dynamic_revalidation_gate": (
            evaluation[
                "dynamic_revalidation_gate"
            ]
        ),
        "revalidation_execution_started": False,
        "knowledge_replaced": False,
        "knowledge_deleted": False,
        "memory_runtime_started": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna46(
    core54: Core54Like,
) -> None:
    core = core54.get(
        "DNA-46"
    )
    assert_exact_canon(
        core
    )
    core54.bind(
        "DNA-46",
        dna46_knowledge_decay_revalidation,
    )


def _provenance_record(
    knowledge_id: str,
    *,
    sequence: int,
    version: str,
) -> Dict[str, Any]:
    return {
        "sequence": sequence,
        "record_id": (
            f"DNA-45-KNOWLEDGE-{sequence:04d}"
        ),
        "knowledge_id": knowledge_id,
        "knowledge": {
            "claim": knowledge_id,
        },
        "origin": {
            "source": "SELF_CHECK_SOURCE",
        },
        "evidence": [
            {
                "result": "VERIFIED_AT_SOURCE_TIME",
            }
        ],
        "verification_method": {
            "method": "SELF_CHECK_VERIFIER",
        },
        "time": "2026-08-10T00:00:00Z",
        "version": version,
        "confidence": 0.8,
        "contradictions": [],
        "provenance_complete": True,
    }


def self_check_dna46(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(
            DNA_JSON
        )
        if verify_canon_file
        else None
    )

    for index in range(
        1,
        46,
    ):
        core_id = (
            f"DNA-{index:02d}"
        )
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get(
        "DNA-46"
    )
    assert_exact_canon(
        core
    )
    bind_dna46(
        core54
    )

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(
                1,
                46,
            )
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
            "knowledge_provenance": {
                "contract": {
                    "schema": (
                        KNOWLEDGE_PROVENANCE_SCHEMA
                    ),
                },
                "records": [
                    _provenance_record(
                        "K-DYNAMIC",
                        sequence=1,
                        version="v1",
                    ),
                    _provenance_record(
                        "K-STABLE",
                        sequence=2,
                        version="v1",
                    ),
                ],
            },
        },
        "knowledge_decay_assessments": [
            {
                "assessment_id": "A-DYNAMIC",
                "knowledge_id": "K-DYNAMIC",
                "dynamic": True,
                "stale_possible": True,
                "stale_evidence": [
                    {
                        "reason": (
                            "SOURCE_STATE_CAN_CHANGE_OVER_TIME"
                        )
                    }
                ],
                "revalidation_required": True,
                "revalidation_result": None,
            },
            {
                "assessment_id": "A-STABLE",
                "knowledge_id": "K-STABLE",
                "dynamic": False,
                "stale_possible": False,
                "stale_evidence": [],
                "revalidation_required": False,
                "revalidation_result": None,
            },
        ],
    }

    snapshot = deepcopy(
        probe
    )
    result = core.activate(
        probe
    )

    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-46"]

    assert (
        output["canonical_gene"]
        == CANON_DNA46
    )
    assert (
        output[
            "dynamic_knowledge_detection"
        ]
        == "PASS"
    )
    assert (
        output[
            "staleness_awareness"
        ]
        == "PASS"
    )
    assert (
        output[
            "revalidation_requirement"
        ]
        == "PASS"
    )
    assert (
        output[
            "dynamic_revalidation_gate"
        ]
        is True
    )

    evaluation = output[
        "evaluation"
    ]

    assert (
        evaluation[
            "dynamic_knowledge_ids"
        ]
        == ["K-DYNAMIC"]
    )
    assert (
        evaluation[
            "stale_possible_knowledge_ids"
        ]
        == ["K-DYNAMIC"]
    )
    assert (
        evaluation[
            "revalidation_required_knowledge_ids"
        ]
        == ["K-DYNAMIC"]
    )

    # Dynamic knowledge cannot opt out of revalidation.
    illegal_dynamic = deepcopy(
        probe
    )
    illegal_dynamic[
        "knowledge_decay_assessments"
    ][0][
        "revalidation_required"
    ] = False

    try:
        core.activate(
            illegal_dynamic
        )
    except ValueError as exc:
        assert str(
            exc
        ) == (
            "DNA-46_DYNAMIC_KNOWLEDGE_MUST_REVALIDATE:"
            "K-DYNAMIC"
        )
    else:
        raise AssertionError(
            "DNA-46_ACCEPTED_DYNAMIC_WITHOUT_REVALIDATION"
        )

    # Staleness must not be invented without evidence.
    no_evidence = deepcopy(
        probe
    )
    no_evidence[
        "knowledge_decay_assessments"
    ][0][
        "stale_evidence"
    ] = []

    try:
        core.activate(
            no_evidence
        )
    except ValueError as exc:
        assert str(
            exc
        ) == (
            "DNA-46_STALENESS_REQUIRES_EVIDENCE:"
            "K-DYNAMIC"
        )
    else:
        raise AssertionError(
            "DNA-46_ACCEPTED_UNEVIDENCED_STALENESS"
        )

    # A supplied revalidation result may be recorded, never executed.
    with_result = deepcopy(
        probe
    )
    with_result[
        "knowledge_decay_assessments"
    ][0][
        "revalidation_result"
    ] = {
        "status": "CURRENTLY_VALID",
        "evidence": [
            "FRESH_INDEPENDENT_CHECK",
        ],
    }

    result_with_result = core.activate(
        with_result
    )
    dynamic_record = result_with_result[
        "core54_outputs"
    ]["DNA-46"][
        "evaluation"
    ]["records"][0]

    assert (
        dynamic_record[
            "revalidation_complete"
        ]
        is True
    )
    assert (
        dynamic_record[
            "revalidation_execution_started"
        ]
        is False
    )
    assert (
        dynamic_record[
            "knowledge_replaced_by_dna46"
        ]
        is False
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

    assert not any(
        locks.values()
    ), locks

    after = (
        _sha256_file(
            DNA_JSON
        )
        if verify_canon_file
        else None
    )

    if verify_canon_file:
        assert before == after

    return {
        "core_id": "DNA-46",
        "canon_mapping": "PASS",
        "dynamic_knowledge_detection": "PASS",
        "staleness_awareness": "PASS",
        "dynamic_revalidation_gate": "PASS",
        "staleness_evidence_gate": "PASS",
        "revalidation_execution_started": False,
        "knowledge_replaced": False,
        "knowledge_deleted": False,
        "memory_runtime_started": False,
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
            "DNA-47"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


PRIOR = {
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
    26: "SIGMA_DNA_26_OBSERVABILITY",
    27: "SIGMA_DNA_27_REPRODUCIBILITY",
    28: "SIGMA_DNA_28_SECURITY_OF_KNOWLEDGE",
    29: "SIGMA_DNA_29_COMPUTE_ARCHITECTURE",
    30: "SIGMA_DNA_30_CORE_RUNTIME_LOOP",
    31: "SIGMA_DNA_31_INTELLIGENCE_TEST",
    32: "SIGMA_DNA_32_ACCEPTANCE_CRITERIA",
    33: "SIGMA_DNA_33_PHYSICAL_IMPLEMENTATION_INDEPENDENCE",
    34: "SIGMA_DNA_34_SIGMA_IDENTITY",
    35: "SIGMA_DNA_35_CORE_COVENANT",
    36: "SIGMA_DNA_36_CAUSAL_WORLD_MODEL",
    37: "SIGMA_DNA_37_INTERNAL_SIMULATION",
    38: "SIGMA_DNA_38_GOAL_ARCHITECTURE",
    39: "SIGMA_DNA_39_CURIOSITY_ENGINE",
    40: "SIGMA_DNA_40_CONCEPT_FORMATION",
    41: "SIGMA_DNA_41_REPRESENTATION_INVENTION",
    42: "SIGMA_DNA_42_METACOGNITIVE_SCHEDULER",
    43: "SIGMA_DNA_43_ANTI_SELF_DECEPTION",
    44: "SIGMA_DNA_44_ADVERSARIAL_SELF_TESTING",
    45: "SIGMA_DNA_45_KNOWLEDGE_PROVENANCE",
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-46_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(
        0,
        str(CORE54_ROOT),
    )
    sys.path.insert(
        0,
        str(GENES_ROOT),
    )

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )

        modules = {
            index: importlib.import_module(
                name
            )
            for index, name in PRIOR.items()
        }

    except Exception as exc:
        print(
            "DNA-46_FAIL: IMPORT_ERROR"
        )
        print(
            repr(exc)
        )
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(
            1,
            46,
        ):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )

            assert (
                report["self_check"]
                == "PASS"
            )

        report = self_check_dna46(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print(
            "DNA-46_FAIL"
        )
        print(
            repr(exc)
        )
        return 3

    print(
        "SIGMA_CORE_DNA_46_PASS"
    )
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "DYNAMIC_KNOWLEDGE_DETECTION:",
        report[
            "dynamic_knowledge_detection"
        ],
    )
    print(
        "STALENESS_AWARENESS:",
        report[
            "staleness_awareness"
        ],
    )
    print(
        "DYNAMIC_REVALIDATION_GATE:",
        report[
            "dynamic_revalidation_gate"
        ],
    )
    print(
        "STALENESS_EVIDENCE_GATE:",
        report[
            "staleness_evidence_gate"
        ],
    )
    print(
        "REVALIDATION_EXECUTION_STARTED:",
        report[
            "revalidation_execution_started"
        ],
    )
    print(
        "KNOWLEDGE_REPLACED:",
        report[
            "knowledge_replaced"
        ],
    )
    print(
        "KNOWLEDGE_DELETED:",
        report[
            "knowledge_deleted"
        ],
    )
    print(
        "MEMORY_RUNTIME_STARTED:",
        report[
            "memory_runtime_started"
        ],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report[
            "higher_runtime_started"
        ],
    )
    print(
        "EXECUTABLE:",
        report["executable"],
    )
    print(
        "SELF_CHECK:",
        report["self_check"],
    )
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print(
        "PHASE_LOCKS:",
        report["phase_locks"],
    )
    print(
        "OFFICIAL_BOUND_CORES: 46/54"
    )
    print(
        "NEXT_AUTHORIZED: DNA-47"
    )
    print(
        "NEXT_PHASE: FORBIDDEN"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
