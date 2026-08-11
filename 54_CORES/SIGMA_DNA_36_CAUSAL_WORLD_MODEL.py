#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-36: CAUSAL WORLD MODEL
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_36_CAUSAL_WORLD_MODEL.py
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

CANON_DNA36: Dict[str, str] = {
    "id": "DNA-36",
    "name": "Causal World Model",
    "purpose": (
        "Phân biệt correlation, causation, mechanism, intervention "
        "và counterfactual."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
CAUSAL_WORLD_MODEL_SCHEMA = "SIGMA_CAUSAL_WORLD_MODEL_V1"

CANON_RELATION_TYPES = [
    "CORRELATION",
    "CAUSATION",
    "MECHANISM",
    "INTERVENTION",
    "COUNTERFACTUAL",
]

RELATION_LABELS = {
    "CORRELATION": "correlation",
    "CAUSATION": "causation",
    "MECHANISM": "mechanism",
    "INTERVENTION": "intervention",
    "COUNTERFACTUAL": "counterfactual",
}

CAUSAL_WORLD_MODEL_CONTRACT: Dict[str, Any] = {
    "schema": CAUSAL_WORLD_MODEL_SCHEMA,
    "canonical_relation_types": deepcopy(
        CANON_RELATION_TYPES
    ),
    "relation_type_count": 5,
    "relation_type_must_be_explicit": True,
    "correlation_is_causation": False,
    "causation_is_mechanism": False,
    "observation_is_intervention": False,
    "factual_is_counterfactual": False,
    "evidence_required": True,
    "missing_relation_type_is_not_invented": True,
    "causal_inference_executed_by_dna36": False,
    "intervention_executed_by_dna36": False,
    "world_runtime_started": False,
    "learning_runtime_started": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": "DIRECT_FROM_CANON_PURPOSE",
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
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(
            lambda: handle.read(1024 * 1024),
            b"",
        ):
            digest.update(chunk)
    return digest.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA36:
        raise RuntimeError(
            "DNA-36_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA36, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-36_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    return state


def _install_causal_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("causal_world_model")
    expected = {
        "contract": deepcopy(
            CAUSAL_WORLD_MODEL_CONTRACT
        ),
        "records": [],
        "batches": [],
    }

    if existing is None:
        state["causal_world_model"] = expected
        return state["causal_world_model"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['causal_world_model'] "
            "must be a dict"
        )

    if existing.get("contract") != (
        CAUSAL_WORLD_MODEL_CONTRACT
    ):
        raise ValueError(
            "DNA-36_CAUSAL_WORLD_MODEL_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("records"), list):
        raise TypeError(
            "causal_world_model['records'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "causal_world_model['batches'] must be a list"
        )

    return existing


def _normalize_record(
    supplied: Any,
    *,
    index: int,
    sequence: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"causal_world_model_records[{index}] "
            "must be a dict"
        )

    required = [
        "relation_id",
        "relation_type",
        "statement",
        "evidence",
    ]
    missing = [
        field
        for field in required
        if field not in supplied
    ]
    if missing:
        raise ValueError(
            "DNA-36_RELATION_FIELDS_MISSING:"
            + ",".join(missing)
        )

    relation_id = supplied["relation_id"]
    relation_type = supplied["relation_type"]
    statement = supplied["statement"]
    evidence = supplied["evidence"]

    if not isinstance(
        relation_id,
        str,
    ) or not relation_id.strip():
        raise ValueError(
            "DNA-36_RELATION_ID_REQUIRED"
        )

    if not isinstance(relation_type, str):
        raise TypeError(
            "causal_record['relation_type'] "
            "must be a string"
        )

    relation_type = relation_type.strip().upper()
    if relation_type not in CANON_RELATION_TYPES:
        raise ValueError(
            f"DNA-36_UNKNOWN_RELATION_TYPE:{relation_type}"
        )

    if not isinstance(
        statement,
        str,
    ) or not statement.strip():
        raise ValueError(
            "DNA-36_STATEMENT_REQUIRED"
        )

    if not isinstance(evidence, list):
        raise TypeError(
            "causal_record['evidence'] must be a list"
        )
    if not evidence:
        raise ValueError(
            f"DNA-36_EVIDENCE_REQUIRED:{relation_type}"
        )

    details = supplied.get("details", {})
    if not isinstance(details, dict):
        raise TypeError(
            "causal_record['details'] must be a dict"
        )

    return {
        "sequence": sequence,
        "record_id": (
            f"DNA-36-RELATION-{sequence:04d}"
        ),
        "input_index": index,
        "relation_id": relation_id,
        "relation_type": relation_type,
        "canonical_label": RELATION_LABELS[
            relation_type
        ],
        "statement": statement,
        "statement_sha256": _sha256_json(
            statement
        ),
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(
            evidence
        ),
        "details": deepcopy(details),
        "details_sha256": _sha256_json(
            details
        ),
        "correlation_promoted_to_causation": False,
        "causal_inference_executed_by_dna36": False,
        "intervention_executed_by_dna36": False,
        "external_action_executed": False,
        "status": "RELATION_TYPE_DISTINGUISHED",
    }


def _evaluate_records(
    supplied: Any,
    causal_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, list):
        raise TypeError(
            "context['causal_world_model_records'] "
            "must be a list"
        )

    start = len(causal_state["records"]) + 1

    records = [
        _normalize_record(
            item,
            index=index,
            sequence=start + index - 1,
        )
        for index, item in enumerate(
            supplied,
            start=1,
        )
    ]

    relation_ids = [
        record["relation_id"]
        for record in records
    ]
    if len(relation_ids) != len(
        set(relation_ids)
    ):
        raise ValueError(
            "DNA-36_DUPLICATE_RELATION_ID"
        )

    present = {
        record["relation_type"]
        for record in records
    }
    missing = [
        relation_type
        for relation_type in CANON_RELATION_TYPES
        if relation_type not in present
    ]

    complete_type_coverage = (
        not missing
        and len(records) >= 5
    )

    batch_sequence = len(
        causal_state["batches"]
    ) + 1

    batch = {
        "sequence": batch_sequence,
        "batch_id": (
            f"DNA-36-BATCH-{batch_sequence:04d}"
        ),
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "relation_count": len(records),
        "relation_types_present": sorted(
            present
        ),
        "missing_relation_types": missing,
        "complete_type_coverage": (
            complete_type_coverage
        ),
        "correlation_promoted_to_causation": False,
        "causal_inference_executed_by_dna36": False,
        "intervention_executed_by_dna36": False,
        "external_action_executed": False,
        "status": (
            "CAUSAL_RELATION_TYPES_COMPLETE"
            if complete_type_coverage
            else "CAUSAL_RELATION_TYPES_INCOMPLETE"
        ),
    }

    causal_state["records"].extend(
        deepcopy(records)
    )
    causal_state["batches"].append(
        deepcopy(batch)
    )

    return {
        "records": records,
        "batch": batch,
    }


def dna36_causal_world_model(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Distinguish correlation, causation, mechanism, intervention, and
    counterfactual as separate Canon relation types.

    DNA-36 does not infer causation from correlation, execute an
    intervention, start World/Learning Runtime, invoke a model, execute
    external action, or modify Canon.
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
    trace.append("DNA-36")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] "
            "must be a dict"
        )

    state = _validate_state(context)
    causal_state = _install_causal_state(
        state
    )

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(
        actual_canon
    )

    state["provenance"].append(
        {
            "sequence": (
                len(state["provenance"]) + 1
            ),
            "core_id": "DNA-36",
            "operation": (
                "CAUSAL_WORLD_MODEL_CONTRACT_"
                "ESTABLISHED"
            ),
            "canonical_sha256": (
                canonical_sha256
            ),
            "schema": (
                CAUSAL_WORLD_MODEL_SCHEMA
            ),
            "relation_types": deepcopy(
                CANON_RELATION_TYPES
            ),
            "world_runtime_started": False,
            "external_action_executed": False,
        }
    )

    evaluation = _evaluate_records(
        context.get(
            "causal_world_model_records"
        ),
        causal_state,
    )

    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": (
                len(state["provenance"]) + 1
            ),
            "core_id": "DNA-36",
            "operation": (
                "CAUSAL_RELATION_TYPES_EVALUATED"
            ),
            "canonical_sha256": (
                canonical_sha256
            ),
            "batch_id": batch["batch_id"],
            "relation_count": (
                batch["relation_count"]
            ),
            "complete_type_coverage": (
                batch[
                    "complete_type_coverage"
                ]
            ),
            "correlation_promoted_to_causation": (
                False
            ),
            "world_runtime_started": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-36"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "causal_world_model_contract": deepcopy(
            CAUSAL_WORLD_MODEL_CONTRACT
        ),
        "evaluation": deepcopy(
            evaluation
        ),
        "correlation_distinguished": (
            "CORRELATION"
            in batch["relation_types_present"]
        ),
        "causation_distinguished": (
            "CAUSATION"
            in batch["relation_types_present"]
        ),
        "mechanism_distinguished": (
            "MECHANISM"
            in batch["relation_types_present"]
        ),
        "intervention_distinguished": (
            "INTERVENTION"
            in batch["relation_types_present"]
        ),
        "counterfactual_distinguished": (
            "COUNTERFACTUAL"
            in batch["relation_types_present"]
        ),
        "correlation_promoted_to_causation": (
            False
        ),
        "causal_inference_executed": False,
        "intervention_executed": False,
        "world_runtime_started": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna36(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-36")
    assert_exact_canon(core)
    core54.bind(
        "DNA-36",
        dna36_causal_world_model,
    )


def _valid_records() -> List[Dict[str, Any]]:
    return [
        {
            "relation_id": "R-CORR",
            "relation_type": "CORRELATION",
            "statement": (
                "X and Y vary together."
            ),
            "evidence": [
                {"type": "OBSERVATION"}
            ],
            "details": {
                "variables": ["X", "Y"],
            },
        },
        {
            "relation_id": "R-CAUSE",
            "relation_type": "CAUSATION",
            "statement": (
                "X is represented as a causal "
                "claim about Y."
            ),
            "evidence": [
                {
                    "type": (
                        "SUPPLIED_CAUSAL_EVIDENCE"
                    )
                }
            ],
            "details": {
                "cause": "X",
                "effect": "Y",
            },
        },
        {
            "relation_id": "R-MECH",
            "relation_type": "MECHANISM",
            "statement": (
                "A supplied mechanism links X "
                "to Y."
            ),
            "evidence": [
                {
                    "type": (
                        "SUPPLIED_MECHANISM_EVIDENCE"
                    )
                }
            ],
            "details": {
                "mechanism": ["M1", "M2"],
            },
        },
        {
            "relation_id": "R-INT",
            "relation_type": "INTERVENTION",
            "statement": (
                "A supplied intervention record "
                "changes X and observes Y."
            ),
            "evidence": [
                {
                    "type": (
                        "SUPPLIED_INTERVENTION_RECORD"
                    )
                }
            ],
            "details": {
                "intervention": "do(X)",
                "outcome": "Y",
            },
        },
        {
            "relation_id": "R-CF",
            "relation_type": "COUNTERFACTUAL",
            "statement": (
                "A supplied counterfactual asks "
                "what Y would be if X differed."
            ),
            "evidence": [
                {
                    "type": (
                        "SUPPLIED_COUNTERFACTUAL_BASIS"
                    )
                }
            ],
            "details": {
                "factual": "X",
                "counterfactual": "not-X",
            },
        },
    ]


def self_check_dna36(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 36):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-36")
    assert_exact_canon(core)
    bind_dna36(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 36)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": (
                UNIFIED_STATE_SCHEMA
            ),
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "causal_world_model_records": (
            _valid_records()
        ),
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-36"]

    assert output["canonical_gene"] == (
        CANON_DNA36
    )
    assert (
        output[
            "correlation_distinguished"
        ]
        is True
    )
    assert (
        output[
            "causation_distinguished"
        ]
        is True
    )
    assert (
        output[
            "mechanism_distinguished"
        ]
        is True
    )
    assert (
        output[
            "intervention_distinguished"
        ]
        is True
    )
    assert (
        output[
            "counterfactual_distinguished"
        ]
        is True
    )
    assert (
        output[
            "correlation_promoted_to_causation"
        ]
        is False
    )
    assert (
        output["causal_inference_executed"]
        is False
    )
    assert (
        output["intervention_executed"]
        is False
    )
    assert (
        output["world_runtime_started"]
        is False
    )

    batch = output[
        "evaluation"
    ]["batch"]

    assert (
        batch["complete_type_coverage"]
        is True
    )
    assert set(
        batch["relation_types_present"]
    ) == set(CANON_RELATION_TYPES)

    # Correlation remains correlation.
    correlation_record = output[
        "evaluation"
    ]["records"][0]
    assert (
        correlation_record[
            "relation_type"
        ]
        == "CORRELATION"
    )
    assert (
        correlation_record[
            "correlation_promoted_to_causation"
        ]
        is False
    )

    # Unknown type is rejected.
    bad = deepcopy(probe)
    bad[
        "causal_world_model_records"
    ][0]["relation_type"] = "ASSOCIATION_CAUSES"
    try:
        core.activate(bad)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-36_UNKNOWN_RELATION_TYPE:"
            "ASSOCIATION_CAUSES"
        )
    else:
        raise AssertionError(
            "DNA-36_ACCEPTED_UNKNOWN_RELATION_TYPE"
        )

    # Missing one type remains incomplete.
    incomplete = deepcopy(probe)
    incomplete[
        "causal_world_model_records"
    ] = _valid_records()[:-1]

    incomplete_result = core.activate(
        incomplete
    )
    incomplete_batch = incomplete_result[
        "core54_outputs"
    ]["DNA-36"]["evaluation"]["batch"]

    assert (
        incomplete_batch[
            "complete_type_coverage"
        ]
        is False
    )
    assert (
        incomplete_batch[
            "missing_relation_types"
        ]
        == ["COUNTERFACTUAL"]
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
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    if verify_canon_file:
        assert before == after

    return {
        "core_id": "DNA-36",
        "canon_mapping": "PASS",
        "correlation": "PASS",
        "causation": "PASS",
        "mechanism": "PASS",
        "intervention": "PASS",
        "counterfactual": "PASS",
        "correlation_not_causation": "PASS",
        "five_relation_type_gate": "PASS",
        "causal_inference_executed": False,
        "intervention_executed": False,
        "world_runtime_started": False,
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
            "DNA-37"
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
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-36_FAIL: "
                "REQUIRED_PATH_NOT_FOUND"
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
            "DNA-36_FAIL: IMPORT_ERROR"
        )
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 36):
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

        report = self_check_dna36(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-36_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_36_PASS")
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "CORRELATION:",
        report["correlation"],
    )
    print(
        "CAUSATION:",
        report["causation"],
    )
    print(
        "MECHANISM:",
        report["mechanism"],
    )
    print(
        "INTERVENTION:",
        report["intervention"],
    )
    print(
        "COUNTERFACTUAL:",
        report["counterfactual"],
    )
    print(
        "CORRELATION_NOT_CAUSATION:",
        report[
            "correlation_not_causation"
        ],
    )
    print(
        "FIVE_RELATION_TYPE_GATE:",
        report[
            "five_relation_type_gate"
        ],
    )
    print(
        "CAUSAL_INFERENCE_EXECUTED:",
        report[
            "causal_inference_executed"
        ],
    )
    print(
        "INTERVENTION_EXECUTED:",
        report[
            "intervention_executed"
        ],
    )
    print(
        "WORLD_RUNTIME_STARTED:",
        report["world_runtime_started"],
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
        "OFFICIAL_BOUND_CORES: 36/54"
    )
    print(
        "NEXT_AUTHORIZED: DNA-37"
    )
    print(
        "NEXT_PHASE: FORBIDDEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
