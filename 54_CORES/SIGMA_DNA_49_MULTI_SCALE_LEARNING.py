#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-49: MULTI-SCALE LEARNING
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_49_MULTI_SCALE_LEARNING.py
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

CANON_DNA49: Dict[str, str] = {
    "id": "DNA-49",
    "name": "Multi-Scale Learning",
    "purpose": (
        "Phân tách reasoning nhanh, episodic learning, "
        "concept consolidation và neural adaptation dài hạn."
    ),
    "system": "learning",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
MULTI_SCALE_LEARNING_SCHEMA = "SIGMA_MULTI_SCALE_LEARNING_V1"

CANON_SCALES = [
    "FAST_REASONING",
    "EPISODIC_LEARNING",
    "CONCEPT_CONSOLIDATION",
    "LONG_TERM_NEURAL_ADAPTATION",
]

MULTI_SCALE_LEARNING_CONTRACT: Dict[str, Any] = {
    "schema": MULTI_SCALE_LEARNING_SCHEMA,
    "canonical_scales": deepcopy(CANON_SCALES),
    "scale_count": 4,
    "scales_must_remain_distinct": True,
    "fast_reasoning_is_not_persistent_learning": True,
    "episodic_learning_is_not_concept_consolidation": True,
    "concept_consolidation_is_not_neural_adaptation": True,
    "neural_adaptation_requires_explicit_scale": True,
    "missing_scale_is_not_invented": True,
    "learning_execution_started": False,
    "neural_adaptation_started": False,
    "memory_runtime_started": False,
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
    if actual != CANON_DNA49:
        raise RuntimeError(
            "DNA-49_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA49,
                    "actual": actual,
                },
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
            "DNA-49_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    return state


def _install_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("multi_scale_learning")
    expected = {
        "contract": deepcopy(
            MULTI_SCALE_LEARNING_CONTRACT
        ),
        "routes": [],
    }

    if existing is None:
        state["multi_scale_learning"] = expected
        return state["multi_scale_learning"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['multi_scale_learning'] "
            "must be a dict"
        )

    if existing.get("contract") != (
        MULTI_SCALE_LEARNING_CONTRACT
    ):
        raise ValueError(
            "DNA-49_MULTI_SCALE_LEARNING_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("routes"), list):
        raise TypeError(
            "multi_scale_learning['routes'] must be a list"
        )

    return existing


def _normalize_unit(
    supplied: Any,
    *,
    index: int,
    sequence: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"learning_units[{index}] must be a dict"
        )

    unit_id = supplied.get("unit_id")
    scale = supplied.get("scale")
    artifact = supplied.get("artifact")
    rationale = supplied.get("rationale")

    if not isinstance(unit_id, str) or not unit_id.strip():
        raise ValueError(
            "DNA-49_UNIT_ID_REQUIRED"
        )

    if not isinstance(scale, str):
        raise TypeError(
            "learning unit scale must be a string"
        )

    scale = scale.strip().upper()

    if scale not in CANON_SCALES:
        raise ValueError(
            f"DNA-49_UNKNOWN_LEARNING_SCALE:{scale}"
        )

    if artifact is None:
        raise ValueError(
            f"DNA-49_ARTIFACT_REQUIRED:{unit_id}"
        )

    if not isinstance(rationale, list) or not rationale:
        raise ValueError(
            f"DNA-49_SCALE_RATIONALE_REQUIRED:{unit_id}"
        )

    return {
        "sequence": sequence,
        "record_id": (
            f"DNA-49-SCALE-{sequence:04d}"
        ),
        "input_index": index,
        "unit_id": unit_id,
        "scale": scale,
        "artifact": deepcopy(artifact),
        "artifact_sha256": _sha256_json(artifact),
        "rationale": deepcopy(rationale),
        "rationale_sha256": _sha256_json(rationale),
        "persistent_learning": (
            scale
            != "FAST_REASONING"
        ),
        "neural_adaptation": (
            scale
            == "LONG_TERM_NEURAL_ADAPTATION"
        ),
        "learning_execution_started": False,
        "neural_adaptation_started": False,
        "status": "LEARNING_SCALE_SEPARATED",
    }


def _evaluate(
    supplied: Any,
    scale_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, list):
        raise TypeError(
            "context['learning_units'] must be a list"
        )

    start = len(
        scale_state["routes"]
    ) + 1

    records = [
        _normalize_unit(
            item,
            index=index,
            sequence=start + index - 1,
        )
        for index, item in enumerate(
            supplied,
            start=1,
        )
    ]

    ids = [
        record["unit_id"]
        for record in records
    ]

    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-49_DUPLICATE_UNIT_ID"
        )

    scale_state["routes"].extend(
        deepcopy(records)
    )

    present = {
        record["scale"]
        for record in records
    }

    missing = [
        scale
        for scale in CANON_SCALES
        if scale not in present
    ]

    complete = (
        not missing
        and len(records) >= 4
    )

    return {
        "records": records,
        "record_count": len(records),
        "scales_present": sorted(present),
        "missing_scales": missing,
        "complete_scale_coverage": complete,
        "fast_reasoning_units": [
            record["unit_id"]
            for record in records
            if record["scale"] == "FAST_REASONING"
        ],
        "episodic_learning_units": [
            record["unit_id"]
            for record in records
            if record["scale"] == "EPISODIC_LEARNING"
        ],
        "concept_consolidation_units": [
            record["unit_id"]
            for record in records
            if record["scale"] == "CONCEPT_CONSOLIDATION"
        ],
        "long_term_neural_adaptation_units": [
            record["unit_id"]
            for record in records
            if record["scale"]
            == "LONG_TERM_NEURAL_ADAPTATION"
        ],
    }


def dna49_multi_scale_learning(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Separate supplied learning artifacts into four Canon scales:
    fast reasoning, episodic learning, concept consolidation, and
    long-term neural adaptation.

    DNA-49 routes/classifies only. It does not execute learning, mutate
    neural capability, start Memory/Learning Runtime, call models, perform
    external actions, or modify Canon.
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
    trace.append("DNA-49")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    scale_state = _install_state(state)

    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)

    evaluation = _evaluate(
        context.get("learning_units"),
        scale_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-49",
            "operation": (
                "MULTI_SCALE_LEARNING_ROUTED"
            ),
            "canonical_sha256": canon_sha,
            "record_count": evaluation[
                "record_count"
            ],
            "scales_present": deepcopy(
                evaluation[
                    "scales_present"
                ]
            ),
            "complete_scale_coverage": (
                evaluation[
                    "complete_scale_coverage"
                ]
            ),
            "learning_execution_started": False,
            "neural_adaptation_started": False,
        }
    )

    outputs["DNA-49"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "multi_scale_learning_contract": deepcopy(
            MULTI_SCALE_LEARNING_CONTRACT
        ),
        "evaluation": deepcopy(
            evaluation
        ),
        "fast_reasoning": (
            "FAST_REASONING"
            in evaluation["scales_present"]
        ),
        "episodic_learning": (
            "EPISODIC_LEARNING"
            in evaluation["scales_present"]
        ),
        "concept_consolidation": (
            "CONCEPT_CONSOLIDATION"
            in evaluation["scales_present"]
        ),
        "long_term_neural_adaptation": (
            "LONG_TERM_NEURAL_ADAPTATION"
            in evaluation["scales_present"]
        ),
        "four_scale_separation_gate": (
            evaluation[
                "complete_scale_coverage"
            ]
        ),
        "learning_execution_started": False,
        "neural_adaptation_started": False,
        "memory_runtime_started": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna49(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-49")
    assert_exact_canon(core)
    core54.bind(
        "DNA-49",
        dna49_multi_scale_learning,
    )


def _valid_units() -> list[dict[str, Any]]:
    return [
        {
            "unit_id": "U-FAST",
            "scale": "FAST_REASONING",
            "artifact": {
                "type": "TRANSIENT_REASONING_STEP",
            },
            "rationale": [
                "Immediate reasoning; no persistent learning."
            ],
        },
        {
            "unit_id": "U-EPISODE",
            "scale": "EPISODIC_LEARNING",
            "artifact": {
                "type": "QUALIFIED_EXPERIENCE_EPISODE",
            },
            "rationale": [
                "Episode-specific learning artifact."
            ],
        },
        {
            "unit_id": "U-CONCEPT",
            "scale": "CONCEPT_CONSOLIDATION",
            "artifact": {
                "type": "CONCEPT_CONSOLIDATION_CANDIDATE",
            },
            "rationale": [
                "Cross-experience abstraction/consolidation."
            ],
        },
        {
            "unit_id": "U-NEURAL",
            "scale": "LONG_TERM_NEURAL_ADAPTATION",
            "artifact": {
                "type": "PERSISTENT_CAPABILITY_CHANGE_CANDIDATE",
            },
            "rationale": [
                "Long-term neural adaptation class only."
            ],
        },
    ]


def self_check_dna49(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 49):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-49")
    assert_exact_canon(core)
    bind_dna49(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 49)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "learning_units": _valid_units(),
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-49"]

    assert output["canonical_gene"] == CANON_DNA49
    assert output["fast_reasoning"] is True
    assert output["episodic_learning"] is True
    assert output["concept_consolidation"] is True
    assert output[
        "long_term_neural_adaptation"
    ] is True
    assert output[
        "four_scale_separation_gate"
    ] is True
    assert output[
        "learning_execution_started"
    ] is False
    assert output[
        "neural_adaptation_started"
    ] is False
    assert output[
        "learning_runtime_started"
    ] is False
    assert output[
        "higher_runtime_started"
    ] is False

    evaluation = output["evaluation"]

    assert set(
        evaluation["scales_present"]
    ) == set(CANON_SCALES)

    assert evaluation[
        "fast_reasoning_units"
    ] == ["U-FAST"]

    assert evaluation[
        "episodic_learning_units"
    ] == ["U-EPISODE"]

    assert evaluation[
        "concept_consolidation_units"
    ] == ["U-CONCEPT"]

    assert evaluation[
        "long_term_neural_adaptation_units"
    ] == ["U-NEURAL"]

    # Missing one scale is not silently invented.
    incomplete = deepcopy(probe)
    incomplete[
        "learning_units"
    ] = _valid_units()[:-1]

    incomplete_result = core.activate(
        incomplete
    )

    incomplete_evaluation = incomplete_result[
        "core54_outputs"
    ]["DNA-49"]["evaluation"]

    assert (
        incomplete_evaluation[
            "complete_scale_coverage"
        ]
        is False
    )
    assert (
        incomplete_evaluation[
            "missing_scales"
        ]
        == ["LONG_TERM_NEURAL_ADAPTATION"]
    )

    # Unknown scale is forbidden.
    unknown = deepcopy(probe)
    unknown[
        "learning_units"
    ][0]["scale"] = "GENERIC_LEARNING"

    try:
        core.activate(unknown)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-49_UNKNOWN_LEARNING_SCALE:"
            "GENERIC_LEARNING"
        )
    else:
        raise AssertionError(
            "DNA-49_ACCEPTED_UNKNOWN_SCALE"
        )

    # Duplicate unit IDs are forbidden.
    duplicate = deepcopy(probe)
    duplicate[
        "learning_units"
    ][1]["unit_id"] = "U-FAST"

    try:
        core.activate(duplicate)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-49_DUPLICATE_UNIT_ID"
        )
    else:
        raise AssertionError(
            "DNA-49_ACCEPTED_DUPLICATE_UNIT_ID"
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
        "core_id": "DNA-49",
        "canon_mapping": "PASS",
        "fast_reasoning": "PASS",
        "episodic_learning": "PASS",
        "concept_consolidation": "PASS",
        "long_term_neural_adaptation": "PASS",
        "four_scale_separation_gate": "PASS",
        "learning_execution_started": False,
        "neural_adaptation_started": False,
        "memory_runtime_started": False,
        "learning_runtime_started": False,
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
            "DNA-50"
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
    40:"SIGMA_DNA_40_CONCEPT_FORMATION",
    41:"SIGMA_DNA_41_REPRESENTATION_INVENTION",
    42:"SIGMA_DNA_42_METACOGNITIVE_SCHEDULER",
    43:"SIGMA_DNA_43_ANTI_SELF_DECEPTION",
    44:"SIGMA_DNA_44_ADVERSARIAL_SELF_TESTING",
    45:"SIGMA_DNA_45_KNOWLEDGE_PROVENANCE",
    46:"SIGMA_DNA_46_KNOWLEDGE_DECAY_REVALIDATION",
    47:"SIGMA_DNA_47_PLASTICITY_STABILITY_BALANCE",
    48:"SIGMA_DNA_48_COMPOSITIONAL_INTELLIGENCE",
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-49_FAIL: REQUIRED_PATH_NOT_FOUND"
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
            "DNA-49_FAIL: IMPORT_ERROR"
        )
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 49):
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

        report = self_check_dna49(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-49_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_49_PASS")
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "FAST_REASONING:",
        report["fast_reasoning"],
    )
    print(
        "EPISODIC_LEARNING:",
        report["episodic_learning"],
    )
    print(
        "CONCEPT_CONSOLIDATION:",
        report["concept_consolidation"],
    )
    print(
        "LONG_TERM_NEURAL_ADAPTATION:",
        report[
            "long_term_neural_adaptation"
        ],
    )
    print(
        "FOUR_SCALE_SEPARATION_GATE:",
        report[
            "four_scale_separation_gate"
        ],
    )
    print(
        "LEARNING_EXECUTION_STARTED:",
        report[
            "learning_execution_started"
        ],
    )
    print(
        "NEURAL_ADAPTATION_STARTED:",
        report[
            "neural_adaptation_started"
        ],
    )
    print(
        "MEMORY_RUNTIME_STARTED:",
        report[
            "memory_runtime_started"
        ],
    )
    print(
        "LEARNING_RUNTIME_STARTED:",
        report[
            "learning_runtime_started"
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
        "OFFICIAL_BOUND_CORES: 49/54"
    )
    print(
        "NEXT_AUTHORIZED: DNA-50"
    )
    print(
        "NEXT_PHASE: FORBIDDEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
