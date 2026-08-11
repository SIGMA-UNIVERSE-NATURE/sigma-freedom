#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-29: COMPUTE ARCHITECTURE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_29_COMPUTE_ARCHITECTURE.py
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol


SIGMA_ROOT = Path(r"E:\SIGMA")
CORE54_ROOT = SIGMA_ROOT / "RUNTIME" / "CORE54"
GENES_ROOT = CORE54_ROOT / "GENES"
DNA_JSON = (
    SIGMA_ROOT / "CORE" / "DNA_CANON"
    / "SIGMA_CORE_DNA_54" / "sigma_dna_54.json"
)

CANON_DNA29: Dict[str, str] = {
    "id": "DNA-29",
    "name": "Compute Architecture",
    "purpose": (
        "Compute co giãn theo nhiệm vụ, tối ưu theo information gain "
        "và chi phí thay vì phô diễn độ sâu."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
ADAPTIVE_DEPTH_SCHEMA = "SIGMA_ADAPTIVE_COGNITIVE_DEPTH_V1"
COMPUTE_ARCHITECTURE_SCHEMA = "SIGMA_COMPUTE_ARCHITECTURE_V1"

COMPUTE_OPTION_FIELDS = [
    "option_id",
    "task_id",
    "compute_units",
    "expected_information_gain",
    "cost",
    "depth",
]

COMPUTE_ARCHITECTURE_CONTRACT: Dict[str, Any] = {
    "schema": COMPUTE_ARCHITECTURE_SCHEMA,
    "task_adaptive_compute_required": True,
    "optimization_targets": [
        "EXPECTED_INFORMATION_GAIN",
        "COST",
    ],
    "depth_display_is_not_objective": True,
    "candidate_score": {
        "method": "EXPECTED_INFORMATION_GAIN_PER_COST",
        "formula": "expected_information_gain / cost",
        "tie_breakers": [
            "LOWER_COST",
            "LOWER_DEPTH",
            "LOWER_COMPUTE_UNITS",
            "OPTION_ID",
        ],
        "canon_status": "IMPLEMENTATION_ENCODING_NOT_CANON_FIELD",
    },
    "dna13_depth_signal_is_context_not_objective": True,
    "compute_execution_started": False,
    "compute_allocated": False,
    "model_calls_started": False,
    "tool_execution_started": False,
    "learning_runtime_started": False,
    "world_runtime_started": False,
    "f174_execution_started": False,
    "external_action_started": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA13_ADAPTIVE_DEPTH_BINDING"
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


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA29:
        raise RuntimeError(
            "DNA-29_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA29, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _finite_non_negative(
    value: Any,
    field: str,
    *,
    strictly_positive: bool = False,
) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            f"compute_option['{field}'] must be a number"
        )

    normalized = float(value)
    if not math.isfinite(normalized):
        raise ValueError(f"DNA-29_NOT_FINITE:{field}")

    if strictly_positive:
        if normalized <= 0.0:
            raise ValueError(f"DNA-29_MUST_BE_POSITIVE:{field}")
    elif normalized < 0.0:
        raise ValueError(f"DNA-29_MUST_BE_NON_NEGATIVE:{field}")

    return normalized


def _validate_dependencies(
    context: Dict[str, Any],
) -> tuple[Dict[str, Any], Optional[Dict[str, Any]]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-29_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    depth_state = state.get("adaptive_cognitive_depth")
    if not isinstance(depth_state, dict):
        raise RuntimeError(
            "DNA-13_ADAPTIVE_COGNITIVE_DEPTH_REQUIRED"
        )

    depth_contract = depth_state.get("contract")
    if not isinstance(depth_contract, dict):
        raise RuntimeError(
            "DNA-13_ADAPTIVE_DEPTH_CONTRACT_REQUIRED"
        )

    if depth_contract.get("schema") != ADAPTIVE_DEPTH_SCHEMA:
        raise ValueError(
            "DNA-29_ADAPTIVE_DEPTH_SCHEMA_MISMATCH:"
            f"{depth_contract.get('schema')!r}"
        )

    assessments = depth_state.get("assessments")
    if not isinstance(assessments, list):
        raise TypeError(
            "adaptive_cognitive_depth['assessments'] must be a list"
        )

    latest_depth = (
        deepcopy(assessments[-1])
        if assessments
        else None
    )

    return state, latest_depth


def _install_compute_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("compute_architecture")
    expected = {
        "contract": deepcopy(
            COMPUTE_ARCHITECTURE_CONTRACT
        ),
        "decisions": [],
    }

    if existing is None:
        state["compute_architecture"] = expected
        return state["compute_architecture"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['compute_architecture'] must be a dict"
        )

    if existing.get("contract") != (
        COMPUTE_ARCHITECTURE_CONTRACT
    ):
        raise ValueError(
            "DNA-29_COMPUTE_ARCHITECTURE_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("decisions"), list):
        raise TypeError(
            "compute_architecture['decisions'] must be a list"
        )

    return existing


def _normalize_option(
    supplied: Any,
    *,
    input_index: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"compute_options[{input_index}] must be a dict"
        )

    missing = [
        field
        for field in COMPUTE_OPTION_FIELDS
        if field not in supplied
    ]
    if missing:
        raise ValueError(
            "DNA-29_COMPUTE_OPTION_FIELDS_MISSING:"
            + ",".join(missing)
        )

    option_id = supplied["option_id"]
    task_id = supplied["task_id"]

    if not isinstance(option_id, str) or not option_id.strip():
        raise ValueError("DNA-29_OPTION_ID_REQUIRED")
    if not isinstance(task_id, str) or not task_id.strip():
        raise ValueError("DNA-29_TASK_ID_REQUIRED")

    compute_units = _finite_non_negative(
        supplied["compute_units"],
        "compute_units",
        strictly_positive=True,
    )
    information_gain = _finite_non_negative(
        supplied["expected_information_gain"],
        "expected_information_gain",
    )
    cost = _finite_non_negative(
        supplied["cost"],
        "cost",
        strictly_positive=True,
    )
    depth = _finite_non_negative(
        supplied["depth"],
        "depth",
    )

    score = information_gain / cost

    return {
        "input_index": input_index,
        "option_id": option_id,
        "task_id": task_id,
        "compute_units": compute_units,
        "expected_information_gain": information_gain,
        "cost": cost,
        "depth": depth,
        "information_gain_per_cost": score,
    }


def _rank_key(option: Dict[str, Any]) -> tuple[Any, ...]:
    return (
        -option["information_gain_per_cost"],
        option["cost"],
        option["depth"],
        option["compute_units"],
        option["option_id"],
    )


def _evaluate_options(
    supplied: Any,
    compute_state: Dict[str, Any],
    latest_depth: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    if supplied is None:
        options: List[Any] = []
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['compute_options'] must be a list"
        )
    else:
        options = supplied

    normalized = [
        _normalize_option(item, input_index=index)
        for index, item in enumerate(options, start=1)
    ]

    ids = [item["option_id"] for item in normalized]
    if len(ids) != len(set(ids)):
        raise ValueError("DNA-29_DUPLICATE_OPTION_ID")

    task_ids = sorted(
        {item["task_id"] for item in normalized}
    )
    if len(task_ids) > 1:
        raise ValueError(
            "DNA-29_COMPUTE_OPTIONS_MUST_SHARE_ONE_TASK_ID"
        )

    ranked = sorted(
        normalized,
        key=_rank_key,
    )
    selected = deepcopy(ranked[0]) if ranked else None

    # Canon says depth must not be the display objective.
    depth_max = max(
        (item["depth"] for item in normalized),
        default=None,
    )
    deepest_ids = sorted(
        [
            item["option_id"]
            for item in normalized
            if depth_max is not None
            and item["depth"] == depth_max
        ]
    )

    sequence = len(compute_state["decisions"]) + 1
    decision = {
        "sequence": sequence,
        "decision_id": (
            f"DNA-29-COMPUTE-{sequence:04d}"
        ),
        "task_id": (
            task_ids[0]
            if len(task_ids) == 1
            else None
        ),
        "candidate_count": len(normalized),
        "candidates": deepcopy(normalized),
        "ranking": [
            item["option_id"]
            for item in ranked
        ],
        "selected_option": selected,
        "selected_option_id": (
            selected["option_id"]
            if selected is not None
            else None
        ),
        "deepest_option_ids": deepest_ids,
        "selected_because_deepest": bool(
            selected is not None
            and selected["option_id"] in deepest_ids
            and all(
                candidate["information_gain_per_cost"]
                <= selected["information_gain_per_cost"]
                for candidate in normalized
            )
        ),
        "selection_objective": (
            "EXPECTED_INFORMATION_GAIN_PER_COST"
        ),
        "latest_dna13_depth_assessment": deepcopy(
            latest_depth
        ),
        "dna13_depth_used_as_context": (
            latest_depth is not None
        ),
        "depth_used_as_primary_objective": False,
        "compute_allocated": False,
        "compute_executed": False,
        "status": (
            "COMPUTE_OPTION_SELECTED"
            if selected is not None
            else "NO_COMPUTE_OPTIONS_SUPPLIED"
        ),
    }

    compute_state["decisions"].append(
        deepcopy(decision)
    )
    return decision


def dna29_compute_architecture(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Select a task-specific compute option by expected information gain
    relative to cost, with depth explicitly not treated as the primary
    objective.

    DNA-29 evaluates supplied compute options only. It does not allocate or
    execute compute, invoke a model/tool, start Learning/World Runtime,
    execute F174, act externally, or modify Canon.
    """
    assert_exact_canon(core)

    context = (
        deepcopy(payload)
        if isinstance(payload, dict)
        else {"input": deepcopy(payload)}
    )

    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("context['trace'] must be a list")
    trace.append("DNA-29")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, latest_depth = _validate_dependencies(
        context
    )
    compute_state = _install_compute_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-29",
            "operation": (
                "COMPUTE_ARCHITECTURE_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "compute_architecture_schema": (
                COMPUTE_ARCHITECTURE_SCHEMA
            ),
            "compute_allocated": False,
            "compute_executed": False,
        }
    )

    decision = _evaluate_options(
        context.get("compute_options"),
        compute_state,
        latest_depth,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-29",
            "operation": (
                "TASK_ADAPTIVE_COMPUTE_OPTION_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "decision_id": decision["decision_id"],
            "task_id": decision["task_id"],
            "selected_option_id": (
                decision["selected_option_id"]
            ),
            "selection_objective": (
                decision["selection_objective"]
            ),
            "depth_used_as_primary_objective": False,
            "compute_allocated": False,
            "compute_executed": False,
        }
    )

    outputs["DNA-29"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "compute_architecture_contract": deepcopy(
            COMPUTE_ARCHITECTURE_CONTRACT
        ),
        "decision": deepcopy(decision),
        "selected_option_id": (
            decision["selected_option_id"]
        ),
        "selection_objective": (
            decision["selection_objective"]
        ),
        "depth_used_as_primary_objective": False,
        "compute_allocated": False,
        "compute_executed": False,
        "model_called": False,
        "tool_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna29(core54: Core54Like) -> None:
    core = core54.get("DNA-29")
    assert_exact_canon(core)
    core54.bind(
        "DNA-29",
        dna29_compute_architecture,
    )


def self_check_dna29(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 29):
        core_id = f"DNA-{index:02d}"
        if not core54.get(core_id).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna29 = core54.get("DNA-29")
    assert_exact_canon(dna29)
    bind_dna29(core54)

    depth_assessment = {
        "assessment_id": "DNA-13-DEPTH-SELF-CHECK",
        "normalized_depth": 0.7,
        "dominant_factors": ["uncertainty"],
    }

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 29)
        ],
        "core54_outputs": {
            "DNA-13": {
                "status": "CANON_ALIGNED",
            }
        },
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
            "adaptive_cognitive_depth": {
                "contract": {
                    "schema": ADAPTIVE_DEPTH_SCHEMA,
                },
                "assessments": [
                    deepcopy(depth_assessment)
                ],
            },
        },
        "compute_options": [
            {
                "option_id": "DEEP-BUT-EXPENSIVE",
                "task_id": "TASK-29",
                "compute_units": 100,
                "expected_information_gain": 10,
                "cost": 100,
                "depth": 10,
            },
            {
                "option_id": "EFFICIENT",
                "task_id": "TASK-29",
                "compute_units": 25,
                "expected_information_gain": 8,
                "cost": 20,
                "depth": 4,
            },
            {
                "option_id": "CHEAP-LOW-GAIN",
                "task_id": "TASK-29",
                "compute_units": 5,
                "expected_information_gain": 1,
                "cost": 5,
                "depth": 2,
            },
        ],
    }

    snapshot = deepcopy(probe)
    result = dna29.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-29"]
    assert output["canonical_gene"] == CANON_DNA29
    assert output["selected_option_id"] == "EFFICIENT"
    assert output["selection_objective"] == (
        "EXPECTED_INFORMATION_GAIN_PER_COST"
    )
    assert output[
        "depth_used_as_primary_objective"
    ] is False
    assert output["compute_allocated"] is False
    assert output["compute_executed"] is False

    decision = output["decision"]
    assert decision["task_id"] == "TASK-29"
    assert decision["candidate_count"] == 3
    assert decision["ranking"][0] == "EFFICIENT"
    assert decision["deepest_option_ids"] == [
        "DEEP-BUT-EXPENSIVE"
    ]
    assert decision["selected_option_id"] != (
        decision["deepest_option_ids"][0]
    )
    assert decision[
        "depth_used_as_primary_objective"
    ] is False
    assert decision[
        "latest_dna13_depth_assessment"
    ] == depth_assessment
    assert decision[
        "dna13_depth_used_as_context"
    ] is True

    # Higher depth alone must not win.
    selected = decision["selected_option"]
    assert selected["depth"] == 4.0
    assert (
        selected["information_gain_per_cost"]
        == 0.4
    )

    # Cost must be positive.
    bad_cost = deepcopy(probe)
    bad_cost["compute_options"][0]["cost"] = 0
    try:
        dna29.activate(bad_cost)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-29_MUST_BE_POSITIVE:cost"
        )
    else:
        raise AssertionError(
            "DNA-29_ACCEPTED_ZERO_COST"
        )

    # Options in one decision must belong to one task.
    mixed_task = deepcopy(probe)
    mixed_task["compute_options"][1]["task_id"] = (
        "OTHER-TASK"
    )
    try:
        dna29.activate(mixed_task)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-29_COMPUTE_OPTIONS_MUST_SHARE_ONE_TASK_ID"
        )
    else:
        raise AssertionError(
            "DNA-29_ACCEPTED_MIXED_TASK_OPTIONS"
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

    canon_after = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )
    if verify_canon_file:
        assert canon_before == canon_after

    return {
        "core_id": "DNA-29",
        "canon_mapping": "PASS",
        "task_adaptive_compute": "PASS",
        "information_gain_cost_optimization": "PASS",
        "depth_not_primary_objective": "PASS",
        "dna13_depth_context": "PASS",
        "compute_allocated": False,
        "compute_executed": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-30"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
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
    26: "SIGMA_DNA_26_OBSERVABILITY",
    27: "SIGMA_DNA_27_REPRODUCIBILITY",
    28: "SIGMA_DNA_28_SECURITY_OF_KNOWLEDGE",
}


def main() -> int:
    required_gene_files = [
        GENES_ROOT / f"{name}.py"
        for name in PRIOR_GENE_MODULES.values()
    ]

    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]:
        if not path.exists():
            print(
                "DNA-29_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )
        modules = {
            index: __import__(name)
            for index, name in (
                PRIOR_GENE_MODULES.items()
            )
        }
    except Exception as exc:
        print("DNA-29_FAIL: IMPORT_ERROR")
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

        for index in range(1, 29):
            checker = getattr(
                modules[index],
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

        report = self_check_dna29(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        assert bound_ids == [
            f"DNA-{index:02d}"
            for index in range(1, 30)
        ]

    except Exception as exc:
        print("DNA-29_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_29_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "TASK_ADAPTIVE_COMPUTE:",
        report["task_adaptive_compute"],
    )
    print(
        "INFORMATION_GAIN_COST_OPTIMIZATION:",
        report["information_gain_cost_optimization"],
    )
    print(
        "DEPTH_NOT_PRIMARY_OBJECTIVE:",
        report["depth_not_primary_objective"],
    )
    print(
        "DNA13_DEPTH_CONTEXT:",
        report["dna13_depth_context"],
    )
    print(
        "COMPUTE_ALLOCATED:",
        report["compute_allocated"],
    )
    print(
        "COMPUTE_EXECUTED:",
        report["compute_executed"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 29/54")
    print("NEXT_AUTHORIZED: DNA-30")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
