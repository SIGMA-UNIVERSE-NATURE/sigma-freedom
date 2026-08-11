#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-39: CURIOSITY ENGINE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_39_CURIOSITY_ENGINE.py
"""

from __future__ import annotations

import hashlib
import importlib
import json
import math
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

CANON_DNA39: Dict[str, str] = {
    "id": "DNA-39",
    "name": "Curiosity Engine",
    "purpose": (
        "Tự phát hiện khoảng trống tri thức và chọn experiment "
        "có expected information gain cao."
    ),
    "system": "learning",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
CURIOSITY_ENGINE_SCHEMA = "SIGMA_CURIOSITY_ENGINE_V1"

CURIOSITY_ENGINE_CONTRACT: Dict[str, Any] = {
    "schema": CURIOSITY_ENGINE_SCHEMA,
    "gap_source": "UNRESOLVED_UNCERTAINTY_IN_CURRENT_STRUCTURED_STATE",
    "knowledge_gap_detection_required": True,
    "experiment_selection_objective": "MAX_EXPECTED_INFORMATION_GAIN",
    "experiment_execution_started": False,
    "learning_runtime_started": False,
    "world_runtime_started": False,
    "model_calls_started": False,
    "tool_execution_started": False,
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
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA39:
        raise RuntimeError(
            "DNA-39_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA39, "actual": actual},
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
            "DNA-39_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )
    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )
    if not isinstance(state.get("uncertainty"), dict):
        raise TypeError(
            "context['cognitive_state']['uncertainty'] must be a dict"
        )
    return state


def _install_curiosity_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("curiosity_engine")
    expected = {
        "contract": deepcopy(CURIOSITY_ENGINE_CONTRACT),
        "cycles": [],
    }

    if existing is None:
        state["curiosity_engine"] = expected
        return state["curiosity_engine"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['curiosity_engine'] must be a dict"
        )
    if existing.get("contract") != CURIOSITY_ENGINE_CONTRACT:
        raise ValueError(
            "DNA-39_CURIOSITY_ENGINE_CONTRACT_CONFLICT"
        )
    if not isinstance(existing.get("cycles"), list):
        raise TypeError(
            "curiosity_engine['cycles'] must be a list"
        )
    return existing


def _extract_open_items(
    uncertainty: Dict[str, Any],
) -> List[Any]:
    gaps: List[Any] = []

    open_items = uncertainty.get("open_items", [])
    if open_items is not None:
        if not isinstance(open_items, list):
            raise TypeError(
                "cognitive_state.uncertainty.open_items must be a list"
            )
        gaps.extend(deepcopy(open_items))

    first_class = uncertainty.get("first_class_data")
    if first_class is not None:
        if not isinstance(first_class, dict):
            raise TypeError(
                "cognitive_state.uncertainty.first_class_data "
                "must be a dict"
            )
        records = first_class.get("records", [])
        if not isinstance(records, list):
            raise TypeError(
                "uncertainty.first_class_data.records must be a list"
            )
        for record in records:
            if not isinstance(record, dict):
                continue
            unresolved = record.get(
                "unresolved_uncertainty",
                [],
            )
            if not isinstance(unresolved, list):
                raise TypeError(
                    "unresolved_uncertainty must be a list"
                )
            gaps.extend(deepcopy(unresolved))

    # De-duplicate without losing structured values.
    seen = set()
    unique: List[Any] = []
    for gap in gaps:
        key = _sha256_json(gap)
        if key not in seen:
            seen.add(key)
            unique.append(gap)

    return unique


def _materialize_gaps(
    uncertainty: Dict[str, Any],
) -> List[Dict[str, Any]]:
    raw = _extract_open_items(uncertainty)
    return [
        {
            "gap_id": f"DNA-39-GAP-{index:04d}",
            "gap": deepcopy(gap),
            "gap_sha256": _sha256_json(gap),
            "source": "UNRESOLVED_UNCERTAINTY",
            "status": "DETECTED",
        }
        for index, gap in enumerate(raw, start=1)
    ]


def _finite_gain(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(
        value,
        (int, float),
    ):
        raise TypeError(
            "experiment_candidate['expected_information_gain'] "
            "must be a number"
        )
    gain = float(value)
    if not math.isfinite(gain):
        raise ValueError(
            "DNA-39_EXPECTED_INFORMATION_GAIN_NOT_FINITE"
        )
    if gain < 0.0:
        raise ValueError(
            "DNA-39_EXPECTED_INFORMATION_GAIN_MUST_BE_NON_NEGATIVE"
        )
    return gain


def _normalize_experiment(
    item: Any,
    *,
    index: int,
    valid_gap_ids: set[str],
) -> Dict[str, Any]:
    if not isinstance(item, dict):
        raise TypeError(
            f"experiment_candidates[{index}] must be a dict"
        )

    experiment_id = item.get("experiment_id")
    target_gap_ids = item.get("target_gap_ids")
    expected_gain = item.get(
        "expected_information_gain"
    )
    design = item.get("design")

    if not isinstance(
        experiment_id,
        str,
    ) or not experiment_id.strip():
        raise ValueError(
            "DNA-39_EXPERIMENT_ID_REQUIRED"
        )

    if not isinstance(target_gap_ids, list):
        raise TypeError(
            "experiment_candidate['target_gap_ids'] "
            "must be a list"
        )
    if not target_gap_ids:
        raise ValueError(
            f"DNA-39_TARGET_GAP_REQUIRED:{experiment_id}"
        )

    normalized_gap_ids: List[str] = []
    for gap_id in target_gap_ids:
        if not isinstance(gap_id, str):
            raise TypeError(
                "target_gap_ids items must be strings"
            )
        if gap_id not in valid_gap_ids:
            raise ValueError(
                f"DNA-39_UNKNOWN_TARGET_GAP:{gap_id}"
            )
        normalized_gap_ids.append(gap_id)

    if len(normalized_gap_ids) != len(
        set(normalized_gap_ids)
    ):
        raise ValueError(
            "DNA-39_DUPLICATE_TARGET_GAP"
        )

    gain = _finite_gain(expected_gain)

    if design is None:
        raise ValueError(
            f"DNA-39_EXPERIMENT_DESIGN_REQUIRED:{experiment_id}"
        )

    return {
        "input_index": index,
        "experiment_id": experiment_id,
        "target_gap_ids": normalized_gap_ids,
        "expected_information_gain": gain,
        "design": deepcopy(design),
        "design_sha256": _sha256_json(design),
        "executed_by_dna39": False,
    }


def _select_experiment(
    candidates: Any,
    gaps: List[Dict[str, Any]],
) -> Dict[str, Any] | None:
    if not isinstance(candidates, list):
        raise TypeError(
            "context['experiment_candidates'] must be a list"
        )

    if not gaps:
        if candidates:
            raise ValueError(
                "DNA-39_EXPERIMENT_WITHOUT_KNOWLEDGE_GAP_FORBIDDEN"
            )
        return None

    valid_gap_ids = {
        gap["gap_id"]
        for gap in gaps
    }

    normalized = [
        _normalize_experiment(
            item,
            index=index,
            valid_gap_ids=valid_gap_ids,
        )
        for index, item in enumerate(
            candidates,
            start=1,
        )
    ]

    if not normalized:
        return None

    ids = [
        item["experiment_id"]
        for item in normalized
    ]
    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-39_DUPLICATE_EXPERIMENT_ID"
        )

    # Primary objective is exactly Canon: highest expected information gain.
    # Lexicographic ID is only deterministic tie-break encoding.
    selected = sorted(
        normalized,
        key=lambda item: (
            -item["expected_information_gain"],
            item["experiment_id"],
        ),
    )[0]

    return {
        "candidates": normalized,
        "selected_experiment": deepcopy(selected),
        "selected_experiment_id": selected[
            "experiment_id"
        ],
        "selection_objective": (
            "MAX_EXPECTED_INFORMATION_GAIN"
        ),
        "selected_expected_information_gain": (
            selected[
                "expected_information_gain"
            ]
        ),
        "experiment_executed": False,
    }


def dna39_curiosity_engine(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Detect knowledge gaps from unresolved uncertainty in the current
    structured state, then select the supplied experiment candidate with
    highest expected information gain.

    DNA-39 does not execute the experiment, start Learning/World Runtime,
    invoke a model/tool, perform external action, or modify Canon.
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
    trace.append("DNA-39")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    curiosity = _install_curiosity_state(
        state
    )

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(
        actual_canon
    )

    gaps = _materialize_gaps(
        state["uncertainty"]
    )

    selection = _select_experiment(
        context.get(
            "experiment_candidates",
            [],
        ),
        gaps,
    )

    sequence = len(curiosity["cycles"]) + 1
    cycle = {
        "sequence": sequence,
        "cycle_id": (
            f"DNA-39-CURIOSITY-{sequence:04d}"
        ),
        "knowledge_gaps": deepcopy(gaps),
        "gap_count": len(gaps),
        "gap_detection_source": (
            "UNRESOLVED_UNCERTAINTY"
        ),
        "selection": deepcopy(selection),
        "experiment_selected": (
            selection is not None
        ),
        "experiment_executed": False,
        "learning_runtime_started": False,
        "world_runtime_started": False,
        "external_action_executed": False,
        "status": (
            "KNOWLEDGE_GAP_EXPERIMENT_SELECTED"
            if selection is not None
            else (
                "KNOWLEDGE_GAP_DETECTED_NO_EXPERIMENT"
                if gaps
                else "NO_KNOWLEDGE_GAP_DETECTED"
            )
        ),
    }
    curiosity["cycles"].append(
        deepcopy(cycle)
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-39",
            "operation": (
                "CURIOSITY_GAP_AND_EXPERIMENT_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "cycle_id": cycle["cycle_id"],
            "gap_count": cycle["gap_count"],
            "experiment_selected": (
                cycle["experiment_selected"]
            ),
            "experiment_executed": False,
            "learning_runtime_started": False,
        }
    )

    outputs["DNA-39"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "curiosity_engine_contract": deepcopy(
            CURIOSITY_ENGINE_CONTRACT
        ),
        "cycle": deepcopy(cycle),
        "knowledge_gap_detection": "PASS",
        "gap_count": len(gaps),
        "selected_experiment_id": (
            selection[
                "selected_experiment_id"
            ]
            if selection is not None
            else None
        ),
        "selection_objective": (
            "MAX_EXPECTED_INFORMATION_GAIN"
        ),
        "experiment_executed": False,
        "learning_runtime_started": False,
        "world_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna39(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-39")
    assert_exact_canon(core)
    core54.bind(
        "DNA-39",
        dna39_curiosity_engine,
    )


def self_check_dna39(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 39):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-39")
    assert_exact_canon(core)
    bind_dna39(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 39)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {
                "open_items": [
                    "UNKNOWN_CAUSAL_MECHANISM",
                    "UNCERTAIN_BOUNDARY_CASE",
                ],
            },
        },
        "experiment_candidates": [
            {
                "experiment_id": "EXP-LOW",
                "target_gap_ids": [
                    "DNA-39-GAP-0001",
                ],
                "expected_information_gain": 0.2,
                "design": {
                    "type": "OBSERVATIONAL_PROBE",
                },
            },
            {
                "experiment_id": "EXP-HIGH",
                "target_gap_ids": [
                    "DNA-39-GAP-0001",
                    "DNA-39-GAP-0002",
                ],
                "expected_information_gain": 0.9,
                "design": {
                    "type": "DISCRIMINATING_EXPERIMENT",
                },
            },
        ],
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-39"]

    assert output["canonical_gene"] == CANON_DNA39
    assert output["knowledge_gap_detection"] == "PASS"
    assert output["gap_count"] == 2
    assert output[
        "selected_experiment_id"
    ] == "EXP-HIGH"
    assert output[
        "selection_objective"
    ] == "MAX_EXPECTED_INFORMATION_GAIN"
    assert output["experiment_executed"] is False
    assert output["learning_runtime_started"] is False
    assert output["world_runtime_started"] is False
    assert output["higher_runtime_started"] is False

    cycle = output["cycle"]
    assert cycle["gap_count"] == 2
    assert cycle["experiment_selected"] is True
    assert cycle["selection"][
        "selected_expected_information_gain"
    ] == 0.9

    # No uncertainty means no invented knowledge gap.
    no_gap = deepcopy(probe)
    no_gap["cognitive_state"]["uncertainty"] = {
        "open_items": [],
    }
    no_gap["experiment_candidates"] = []
    no_gap_result = core.activate(no_gap)
    no_gap_cycle = no_gap_result[
        "core54_outputs"
    ]["DNA-39"]["cycle"]
    assert no_gap_cycle["gap_count"] == 0
    assert no_gap_cycle["experiment_selected"] is False
    assert no_gap_cycle["status"] == (
        "NO_KNOWLEDGE_GAP_DETECTED"
    )

    # Experiment cannot be selected when no gap exists.
    invalid = deepcopy(no_gap)
    invalid["experiment_candidates"] = [
        {
            "experiment_id": "EXP-NO-GAP",
            "target_gap_ids": [
                "DNA-39-GAP-0001",
            ],
            "expected_information_gain": 1.0,
            "design": {"type": "INVALID"},
        }
    ]
    try:
        core.activate(invalid)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-39_EXPERIMENT_WITHOUT_KNOWLEDGE_GAP_FORBIDDEN"
        )
    else:
        raise AssertionError(
            "DNA-39_ACCEPTED_EXPERIMENT_WITHOUT_GAP"
        )

    # Highest EIG must win even if listed later.
    reverse = deepcopy(probe)
    reverse["experiment_candidates"] = list(
        reversed(
            reverse[
                "experiment_candidates"
            ]
        )
    )
    reverse_result = core.activate(reverse)
    assert reverse_result[
        "core54_outputs"
    ]["DNA-39"][
        "selected_experiment_id"
    ] == "EXP-HIGH"

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
        "core_id": "DNA-39",
        "canon_mapping": "PASS",
        "knowledge_gap_detection": "PASS",
        "expected_information_gain_selection": "PASS",
        "highest_eig_gate": "PASS",
        "experiment_executed": False,
        "learning_runtime_started": False,
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
            "DNA-40"
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
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-39_FAIL: REQUIRED_PATH_NOT_FOUND"
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
        print(
            "DNA-39_FAIL: IMPORT_ERROR"
        )
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 39):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna39(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-39_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_39_PASS")
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "KNOWLEDGE_GAP_DETECTION:",
        report["knowledge_gap_detection"],
    )
    print(
        "EXPECTED_INFORMATION_GAIN_SELECTION:",
        report[
            "expected_information_gain_selection"
        ],
    )
    print(
        "HIGHEST_EIG_GATE:",
        report["highest_eig_gate"],
    )
    print(
        "EXPERIMENT_EXECUTED:",
        report["experiment_executed"],
    )
    print(
        "LEARNING_RUNTIME_STARTED:",
        report["learning_runtime_started"],
    )
    print(
        "WORLD_RUNTIME_STARTED:",
        report["world_runtime_started"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
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
        "OFFICIAL_BOUND_CORES: 39/54"
    )
    print(
        "NEXT_AUTHORIZED: DNA-40"
    )
    print(
        "NEXT_PHASE: FORBIDDEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
