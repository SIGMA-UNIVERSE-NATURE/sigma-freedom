#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-30: CORE RUNTIME LOOP
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_30_CORE_RUNTIME_LOOP.py
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

CANON_DNA30: Dict[str, str] = {
    "id": "DNA-30",
    "name": "Core Runtime Loop",
    "purpose": (
        "Observe→Represent→Hypothesize→Critique→Experiment→Verify→"
        "Ethics→Feedback→Retain/Revise."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
CORE_RUNTIME_LOOP_SCHEMA = "SIGMA_CORE_RUNTIME_LOOP_V1"

CANON_STAGES = [
    "OBSERVE",
    "REPRESENT",
    "HYPOTHESIZE",
    "CRITIQUE",
    "EXPERIMENT",
    "VERIFY",
    "ETHICS",
    "FEEDBACK",
    "RETAIN_OR_REVISE",
]

FINAL_DISPOSITIONS = [
    "RETAIN",
    "REVISE",
]

CORE_RUNTIME_LOOP_CONTRACT: Dict[str, Any] = {
    "schema": CORE_RUNTIME_LOOP_SCHEMA,
    "ordered_stages": deepcopy(CANON_STAGES),
    "stage_count": 9,
    "order_is_mandatory": True,
    "final_dispositions": deepcopy(FINAL_DISPOSITIONS),
    "cycle_must_be_traceable": True,
    "missing_stage_is_not_invented": True,
    "experiment_executed_by_dna30": False,
    "verification_executed_by_dna30": False,
    "learning_runtime_started": False,
    "world_runtime_started": False,
    "memory_runtime_started": False,
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
    h = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA30:
        raise RuntimeError(
            "DNA-30_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA30, "actual": actual},
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
            "DNA-30_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    return state


def _install_loop_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("core_runtime_loop")
    expected = {
        "contract": deepcopy(CORE_RUNTIME_LOOP_CONTRACT),
        "cycles": [],
    }

    if existing is None:
        state["core_runtime_loop"] = expected
        return state["core_runtime_loop"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['core_runtime_loop'] must be a dict"
        )

    if existing.get("contract") != CORE_RUNTIME_LOOP_CONTRACT:
        raise ValueError(
            "DNA-30_CORE_RUNTIME_LOOP_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("cycles"), list):
        raise TypeError(
            "core_runtime_loop['cycles'] must be a list"
        )

    return existing


def _normalize_stage(
    supplied: Any,
    *,
    expected_stage: str,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"core_loop_cycle['stages'][{index}] must be a dict"
        )

    stage = supplied.get("stage")
    if not isinstance(stage, str):
        raise TypeError(
            f"core_loop_cycle['stages'][{index}]['stage'] "
            "must be a string"
        )

    normalized = stage.strip().upper()
    if normalized != expected_stage:
        raise ValueError(
            "DNA-30_STAGE_ORDER_MISMATCH:"
            f"expected={expected_stage}:actual={normalized}"
        )

    if "artifact" not in supplied:
        raise ValueError(
            f"DNA-30_STAGE_ARTIFACT_REQUIRED:{expected_stage}"
        )

    artifact = deepcopy(supplied["artifact"])

    return {
        "index": index + 1,
        "stage": normalized,
        "artifact": artifact,
        "artifact_sha256": _sha256_json(artifact),
    }


def _evaluate_cycle(
    supplied: Any,
    loop_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['core_loop_cycle'] must be a dict"
        )

    cycle_id = supplied.get("cycle_id")
    if not isinstance(cycle_id, str) or not cycle_id.strip():
        raise ValueError("DNA-30_CYCLE_ID_REQUIRED")

    stages = supplied.get("stages")
    if not isinstance(stages, list):
        raise TypeError(
            "core_loop_cycle['stages'] must be a list"
        )

    if len(stages) != len(CANON_STAGES):
        raise ValueError(
            "DNA-30_EXACT_NINE_STAGES_REQUIRED"
        )

    normalized_stages = [
        _normalize_stage(
            stage,
            expected_stage=CANON_STAGES[index],
            index=index,
        )
        for index, stage in enumerate(stages)
    ]

    final_artifact = normalized_stages[-1]["artifact"]
    if not isinstance(final_artifact, dict):
        raise TypeError(
            "RETAIN_OR_REVISE artifact must be a dict"
        )

    disposition = final_artifact.get("disposition")
    if not isinstance(disposition, str):
        raise TypeError(
            "RETAIN_OR_REVISE artifact['disposition'] "
            "must be a string"
        )

    disposition = disposition.strip().upper()
    if disposition not in FINAL_DISPOSITIONS:
        raise ValueError(
            "DNA-30_DISPOSITION_MUST_BE_RETAIN_OR_REVISE"
        )

    sequence = len(loop_state["cycles"]) + 1
    cycle = {
        "sequence": sequence,
        "cycle_id": cycle_id,
        "stage_count": 9,
        "stages": normalized_stages,
        "stage_order": [
            stage["stage"]
            for stage in normalized_stages
        ],
        "cycle_sha256": _sha256_json(
            {
                "cycle_id": cycle_id,
                "stages": normalized_stages,
            }
        ),
        "final_disposition": disposition,
        "complete": True,
        "traceable": True,
        "experiment_executed_by_dna30": False,
        "verification_executed_by_dna30": False,
        "external_action_executed": False,
        "status": (
            "CORE_RUNTIME_LOOP_COMPLETE_RETAIN"
            if disposition == "RETAIN"
            else "CORE_RUNTIME_LOOP_COMPLETE_REVISE"
        ),
    }

    loop_state["cycles"].append(deepcopy(cycle))
    return cycle


def dna30_core_runtime_loop(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Validate and materialize one exact Canon-ordered cognitive cycle:
    Observe→Represent→Hypothesize→Critique→Experiment→Verify→Ethics→
    Feedback→Retain/Revise.

    DNA-30 does not itself run an experiment, verifier, model, tool,
    Learning/World/Memory Runtime, external action, or Canon write.
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
    trace.append("DNA-30")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    loop_state = _install_loop_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-30",
            "operation": "CORE_RUNTIME_LOOP_CONTRACT_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "schema": CORE_RUNTIME_LOOP_SCHEMA,
            "ordered_stages": deepcopy(CANON_STAGES),
            "external_action_executed": False,
        }
    )

    cycle = _evaluate_cycle(
        context.get("core_loop_cycle"),
        loop_state,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-30",
            "operation": "CORE_RUNTIME_LOOP_CYCLE_VALIDATED",
            "canonical_sha256": canonical_sha256,
            "cycle_id": cycle["cycle_id"],
            "cycle_sha256": cycle["cycle_sha256"],
            "stage_count": cycle["stage_count"],
            "final_disposition": cycle["final_disposition"],
            "external_action_executed": False,
        }
    )

    outputs["DNA-30"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "core_runtime_loop_contract": deepcopy(
            CORE_RUNTIME_LOOP_CONTRACT
        ),
        "cycle": deepcopy(cycle),
        "stage_order": deepcopy(cycle["stage_order"]),
        "final_disposition": cycle["final_disposition"],
        "complete": True,
        "experiment_executed_by_dna30": False,
        "verification_executed_by_dna30": False,
        "learning_runtime_started": False,
        "world_runtime_started": False,
        "memory_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna30(core54: Core54Like) -> None:
    core = core54.get("DNA-30")
    assert_exact_canon(core)
    core54.bind(
        "DNA-30",
        dna30_core_runtime_loop,
    )


def _valid_cycle(
    disposition: str = "RETAIN",
) -> Dict[str, Any]:
    artifacts = {
        "OBSERVE": {"observation": "O1"},
        "REPRESENT": {"representation": "R1"},
        "HYPOTHESIZE": {"hypothesis": "H1"},
        "CRITIQUE": {"critique": "C1"},
        "EXPERIMENT": {"experiment_record": "E1"},
        "VERIFY": {"verification_record": "V1"},
        "ETHICS": {"ethical_reasoning_record": "ETH1"},
        "FEEDBACK": {"feedback_record": "F1"},
        "RETAIN_OR_REVISE": {
            "disposition": disposition,
            "reason": "SELF_CHECK",
        },
    }
    return {
        "cycle_id": f"DNA30-{disposition}",
        "stages": [
            {
                "stage": stage,
                "artifact": deepcopy(artifacts[stage]),
            }
            for stage in CANON_STAGES
        ],
    }


def self_check_dna30(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 30):
        core_id = f"DNA-{index:02d}"
        if not core54.get(core_id).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna30 = core54.get("DNA-30")
    assert_exact_canon(dna30)
    bind_dna30(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 30)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "core_loop_cycle": _valid_cycle("RETAIN"),
    }

    snapshot = deepcopy(probe)
    result = dna30.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-30"]
    assert output["canonical_gene"] == CANON_DNA30
    assert output["stage_order"] == CANON_STAGES
    assert output["final_disposition"] == "RETAIN"
    assert output["complete"] is True
    assert output["experiment_executed_by_dna30"] is False
    assert output["verification_executed_by_dna30"] is False
    assert output["learning_runtime_started"] is False
    assert output["world_runtime_started"] is False
    assert output["memory_runtime_started"] is False

    cycle = output["cycle"]
    assert cycle["stage_count"] == 9
    assert cycle["stage_order"] == CANON_STAGES
    assert cycle["traceable"] is True
    assert cycle["final_disposition"] == "RETAIN"

    revise_probe = deepcopy(probe)
    revise_probe["core_loop_cycle"] = _valid_cycle("REVISE")
    revise = dna30.activate(revise_probe)
    assert revise[
        "core54_outputs"
    ]["DNA-30"]["final_disposition"] == "REVISE"

    wrong_order = deepcopy(probe)
    wrong_order["core_loop_cycle"]["stages"][0], (
        wrong_order["core_loop_cycle"]["stages"][1]
    ) = (
        wrong_order["core_loop_cycle"]["stages"][1],
        wrong_order["core_loop_cycle"]["stages"][0],
    )
    try:
        dna30.activate(wrong_order)
    except ValueError as exc:
        assert str(exc).startswith(
            "DNA-30_STAGE_ORDER_MISMATCH:"
        )
    else:
        raise AssertionError(
            "DNA-30_ACCEPTED_WRONG_STAGE_ORDER"
        )

    missing_stage = deepcopy(probe)
    missing_stage["core_loop_cycle"]["stages"].pop()
    try:
        dna30.activate(missing_stage)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-30_EXACT_NINE_STAGES_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-30_ACCEPTED_MISSING_STAGE"
        )

    invalid_disposition = deepcopy(probe)
    invalid_disposition[
        "core_loop_cycle"
    ]["stages"][-1]["artifact"]["disposition"] = "DROP"
    try:
        dna30.activate(invalid_disposition)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-30_DISPOSITION_MUST_BE_RETAIN_OR_REVISE"
        )
    else:
        raise AssertionError(
            "DNA-30_ACCEPTED_INVALID_DISPOSITION"
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
        "core_id": "DNA-30",
        "canon_mapping": "PASS",
        "ordered_stage_contract": "PASS",
        "exact_nine_stage_gate": "PASS",
        "retain_or_revise_gate": "PASS",
        "traceability": "PASS",
        "experiment_executed_by_dna30": False,
        "verification_executed_by_dna30": False,
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
            "DNA-31"
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
    29: "SIGMA_DNA_29_COMPUTE_ARCHITECTURE",
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
                "DNA-30_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = {
            index: importlib.import_module(name)
            for index, name in PRIOR_GENE_MODULES.items()
        }
    except Exception as exc:
        print("DNA-30_FAIL: IMPORT_ERROR")
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

        for index in range(1, 30):
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

        report = self_check_dna30(
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
            for index in range(1, 31)
        ]

    except Exception as exc:
        print("DNA-30_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_30_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "ORDERED_STAGE_CONTRACT:",
        report["ordered_stage_contract"],
    )
    print(
        "EXACT_NINE_STAGE_GATE:",
        report["exact_nine_stage_gate"],
    )
    print(
        "RETAIN_OR_REVISE_GATE:",
        report["retain_or_revise_gate"],
    )
    print("TRACEABILITY:", report["traceability"])
    print(
        "EXPERIMENT_EXECUTED_BY_DNA30:",
        report["experiment_executed_by_dna30"],
    )
    print(
        "VERIFICATION_EXECUTED_BY_DNA30:",
        report["verification_executed_by_dna30"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 30/54")
    print("NEXT_AUTHORIZED: DNA-31")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
