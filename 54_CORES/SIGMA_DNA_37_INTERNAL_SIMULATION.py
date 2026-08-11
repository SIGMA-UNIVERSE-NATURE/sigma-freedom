#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-37: INTERNAL SIMULATION
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_37_INTERNAL_SIMULATION.py
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

CANON_DNA37: Dict[str, str] = {
    "id": "DNA-37",
    "name": "Internal Simulation",
    "purpose": (
        "Mô phỏng nhiều hậu quả có thể trước hành động quan trọng "
        "để hỗ trợ reasoning và đạo đức."
    ),
    "system": "wisdom",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
ETHICAL_SCHEMA = "SIGMA_ETHICAL_INTELLIGENCE_V1"
CAUSAL_WORLD_MODEL_SCHEMA = "SIGMA_CAUSAL_WORLD_MODEL_V1"
INTERNAL_SIMULATION_SCHEMA = "SIGMA_INTERNAL_SIMULATION_V1"

SIMULATION_CONTRACT: Dict[str, Any] = {
    "schema": INTERNAL_SIMULATION_SCHEMA,
    "important_action_requires_pre_action_simulation": True,
    "multiple_possible_consequences_required": True,
    "reasoning_support_required": True,
    "ethical_support_required": True,
    "simulation_is_reality": False,
    "simulation_is_prediction": True,
    "actual_action_executed_by_dna37": False,
    "world_runtime_started": False,
    "learning_runtime_started": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA05_ETHICS_"
        "AND_DNA36_CAUSAL_MODEL_BINDING"
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
    if actual != CANON_DNA37:
        raise RuntimeError(
            "DNA-37_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA37, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-37_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    ethics = state.get("ethical_intelligence")
    if not isinstance(ethics, dict):
        raise RuntimeError(
            "DNA-05_ETHICAL_INTELLIGENCE_REQUIRED"
        )
    if ethics.get("schema") != ETHICAL_SCHEMA:
        raise ValueError(
            "DNA-37_ETHICAL_SCHEMA_MISMATCH:"
            f"{ethics.get('schema')!r}"
        )

    causal = state.get("causal_world_model")
    if not isinstance(causal, dict):
        raise RuntimeError(
            "DNA-36_CAUSAL_WORLD_MODEL_REQUIRED"
        )
    contract = causal.get("contract")
    if not isinstance(contract, dict):
        raise RuntimeError(
            "DNA-36_CAUSAL_WORLD_MODEL_CONTRACT_REQUIRED"
        )
    if contract.get("schema") != CAUSAL_WORLD_MODEL_SCHEMA:
        raise ValueError(
            "DNA-37_CAUSAL_WORLD_MODEL_SCHEMA_MISMATCH:"
            f"{contract.get('schema')!r}"
        )

    return state


def _install_simulation_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("internal_simulation")
    expected = {
        "contract": deepcopy(SIMULATION_CONTRACT),
        "simulations": [],
    }

    if existing is None:
        state["internal_simulation"] = expected
        return state["internal_simulation"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['internal_simulation'] must be a dict"
        )

    if existing.get("contract") != SIMULATION_CONTRACT:
        raise ValueError(
            "DNA-37_INTERNAL_SIMULATION_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("simulations"), list):
        raise TypeError(
            "internal_simulation['simulations'] must be a list"
        )

    return existing


def _normalize_consequence(
    item: Any,
    *,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(item, dict):
        raise TypeError(
            f"simulation_consequences[{index}] must be a dict"
        )

    for field in (
        "consequence_id",
        "description",
        "reasoning",
        "ethical_assessment",
    ):
        if field not in item:
            raise ValueError(
                f"DNA-37_CONSEQUENCE_FIELD_REQUIRED:{field}"
            )

    consequence_id = item["consequence_id"]
    description = item["description"]
    reasoning = item["reasoning"]
    ethical_assessment = item["ethical_assessment"]

    if not isinstance(consequence_id, str) or not consequence_id.strip():
        raise ValueError(
            "DNA-37_CONSEQUENCE_ID_REQUIRED"
        )
    if not isinstance(description, str) or not description.strip():
        raise ValueError(
            "DNA-37_CONSEQUENCE_DESCRIPTION_REQUIRED"
        )
    if not isinstance(reasoning, list) or not reasoning:
        raise ValueError(
            f"DNA-37_REASONING_REQUIRED:{consequence_id}"
        )
    if not isinstance(ethical_assessment, list) or not ethical_assessment:
        raise ValueError(
            f"DNA-37_ETHICAL_ASSESSMENT_REQUIRED:{consequence_id}"
        )

    probability = item.get("probability")
    if probability is not None:
        if isinstance(probability, bool) or not isinstance(
            probability,
            (int, float),
        ):
            raise TypeError(
                "simulation consequence probability must be numeric or None"
            )
        probability = float(probability)
        if not 0.0 <= probability <= 1.0:
            raise ValueError(
                "DNA-37_PROBABILITY_OUT_OF_RANGE"
            )

    return {
        "input_index": index,
        "consequence_id": consequence_id,
        "description": description,
        "probability": probability,
        "reasoning": deepcopy(reasoning),
        "reasoning_sha256": _sha256_json(reasoning),
        "ethical_assessment": deepcopy(ethical_assessment),
        "ethical_assessment_sha256": _sha256_json(
            ethical_assessment
        ),
        "simulation_only": True,
        "observed_reality": False,
    }


def _evaluate_simulation(
    supplied: Any,
    sim_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['internal_simulation'] must be a dict"
        )

    simulation_id = supplied.get("simulation_id")
    action = supplied.get("action")
    important_action = supplied.get("important_action")
    consequences = supplied.get("consequences")

    if not isinstance(simulation_id, str) or not simulation_id.strip():
        raise ValueError(
            "DNA-37_SIMULATION_ID_REQUIRED"
        )

    if action is None:
        raise ValueError(
            "DNA-37_ACTION_REQUIRED"
        )

    if not isinstance(important_action, bool):
        raise TypeError(
            "internal_simulation['important_action'] must be a bool"
        )

    if not isinstance(consequences, list):
        raise TypeError(
            "internal_simulation['consequences'] must be a list"
        )

    normalized = [
        _normalize_consequence(
            item,
            index=index,
        )
        for index, item in enumerate(
            consequences,
            start=1,
        )
    ]

    ids = [
        item["consequence_id"]
        for item in normalized
    ]
    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-37_DUPLICATE_CONSEQUENCE_ID"
        )

    if important_action and len(normalized) < 2:
        raise ValueError(
            "DNA-37_IMPORTANT_ACTION_REQUIRES_MULTIPLE_CONSEQUENCES"
        )

    sequence = len(
        sim_state["simulations"]
    ) + 1

    record = {
        "sequence": sequence,
        "record_id": (
            f"DNA-37-SIMULATION-{sequence:04d}"
        ),
        "simulation_id": simulation_id,
        "action": deepcopy(action),
        "action_sha256": _sha256_json(action),
        "important_action": important_action,
        "consequences": deepcopy(normalized),
        "consequence_count": len(normalized),
        "multiple_consequences": (
            len(normalized) >= 2
        ),
        "reasoning_supported": bool(
            normalized
            and all(
                item["reasoning"]
                for item in normalized
            )
        ),
        "ethics_supported": bool(
            normalized
            and all(
                item["ethical_assessment"]
                for item in normalized
            )
        ),
        "simulation_not_reality": True,
        "action_executed_by_dna37": False,
        "external_action_executed": False,
        "status": (
            "IMPORTANT_ACTION_MULTI_OUTCOME_SIMULATED"
            if important_action
            else "ACTION_SIMULATION_RECORDED"
        ),
    }

    sim_state["simulations"].append(
        deepcopy(record)
    )
    return record


def dna37_internal_simulation(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Record multiple possible consequences before an important action to
    support reasoning and ethics.

    DNA-37 never treats simulation as observed reality and does not execute
    the action, start World/Learning Runtime, invoke models/tools, perform
    external action, or modify Canon.
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
    trace.append("DNA-37")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_dependencies(context)
    sim_state = _install_simulation_state(
        state
    )

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(
        actual_canon
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-37",
            "operation": (
                "INTERNAL_SIMULATION_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "schema": INTERNAL_SIMULATION_SCHEMA,
            "simulation_not_reality": True,
            "action_executed": False,
        }
    )

    record = _evaluate_simulation(
        context.get("internal_simulation"),
        sim_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-37",
            "operation": (
                "PRE_ACTION_OUTCOMES_SIMULATED"
            ),
            "canonical_sha256": canonical_sha256,
            "record_id": record["record_id"],
            "important_action": (
                record["important_action"]
            ),
            "consequence_count": (
                record["consequence_count"]
            ),
            "simulation_not_reality": True,
            "action_executed": False,
        }
    )

    outputs["DNA-37"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "simulation_contract": deepcopy(
            SIMULATION_CONTRACT
        ),
        "record": deepcopy(record),
        "multiple_consequences": (
            record["multiple_consequences"]
        ),
        "reasoning_supported": (
            record["reasoning_supported"]
        ),
        "ethics_supported": (
            record["ethics_supported"]
        ),
        "simulation_not_reality": True,
        "action_executed": False,
        "world_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna37(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-37")
    assert_exact_canon(core)
    core54.bind(
        "DNA-37",
        dna37_internal_simulation,
    )


def _valid_simulation() -> Dict[str, Any]:
    return {
        "simulation_id": "DNA37-SELF-CHECK",
        "action": {
            "action_id": "ACTION-IMPORTANT-01",
            "description": "IMPORTANT_PROPOSED_ACTION",
        },
        "important_action": True,
        "consequences": [
            {
                "consequence_id": "OUTCOME-A",
                "description": "Potential beneficial outcome",
                "probability": 0.6,
                "reasoning": [
                    {
                        "basis": "SUPPLIED_CAUSAL_REASONING_A",
                    }
                ],
                "ethical_assessment": [
                    {
                        "dimension": "human_benefit",
                        "assessment": "SUPPORTED",
                    },
                    {
                        "dimension": "autonomy",
                        "assessment": "PRESERVED",
                    },
                ],
            },
            {
                "consequence_id": "OUTCOME-B",
                "description": "Potential adverse outcome",
                "probability": 0.4,
                "reasoning": [
                    {
                        "basis": "SUPPLIED_CAUSAL_REASONING_B",
                    }
                ],
                "ethical_assessment": [
                    {
                        "dimension": "harm",
                        "assessment": "RISK_PRESENT",
                    },
                    {
                        "dimension": "dignity",
                        "assessment": "REQUIRES_PROTECTION",
                    },
                ],
            },
        ],
    }


def self_check_dna37(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 37):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-37")
    assert_exact_canon(core)
    bind_dna37(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 37)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": (
                UNIFIED_STATE_SCHEMA
            ),
            "content": {},
            "provenance": [],
            "uncertainty": {},
            "ethical_intelligence": {
                "schema": ETHICAL_SCHEMA,
            },
            "causal_world_model": {
                "contract": {
                    "schema": (
                        CAUSAL_WORLD_MODEL_SCHEMA
                    ),
                },
                "records": [],
                "batches": [],
            },
        },
        "internal_simulation": (
            _valid_simulation()
        ),
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-37"]

    assert output["canonical_gene"] == CANON_DNA37
    assert output["multiple_consequences"] is True
    assert output["reasoning_supported"] is True
    assert output["ethics_supported"] is True
    assert output["simulation_not_reality"] is True
    assert output["action_executed"] is False
    assert output["world_runtime_started"] is False
    assert output["higher_runtime_started"] is False

    record = output["record"]
    assert record["important_action"] is True
    assert record["consequence_count"] == 2
    assert record["simulation_not_reality"] is True
    assert record["action_executed_by_dna37"] is False

    # Important action must have multiple possible consequences.
    one_outcome = deepcopy(probe)
    one_outcome[
        "internal_simulation"
    ]["consequences"] = (
        one_outcome[
            "internal_simulation"
        ]["consequences"][:1]
    )

    try:
        core.activate(one_outcome)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-37_IMPORTANT_ACTION_REQUIRES_MULTIPLE_CONSEQUENCES"
        )
    else:
        raise AssertionError(
            "DNA-37_ACCEPTED_SINGLE_OUTCOME_FOR_IMPORTANT_ACTION"
        )

    # Probability is optional but cannot be invalid.
    bad_probability = deepcopy(probe)
    bad_probability[
        "internal_simulation"
    ]["consequences"][0]["probability"] = 1.2

    try:
        core.activate(bad_probability)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-37_PROBABILITY_OUT_OF_RANGE"
        )
    else:
        raise AssertionError(
            "DNA-37_ACCEPTED_INVALID_PROBABILITY"
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
        "core_id": "DNA-37",
        "canon_mapping": "PASS",
        "multiple_possible_consequences": "PASS",
        "pre_action_simulation": "PASS",
        "reasoning_support": "PASS",
        "ethical_support": "PASS",
        "simulation_not_reality": "PASS",
        "action_executed": False,
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
            "DNA-38"
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
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-37_FAIL: REQUIRED_PATH_NOT_FOUND"
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
        print("DNA-37_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 37):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna37(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-37_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_37_PASS")
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "MULTIPLE_POSSIBLE_CONSEQUENCES:",
        report["multiple_possible_consequences"],
    )
    print(
        "PRE_ACTION_SIMULATION:",
        report["pre_action_simulation"],
    )
    print(
        "REASONING_SUPPORT:",
        report["reasoning_support"],
    )
    print(
        "ETHICAL_SUPPORT:",
        report["ethical_support"],
    )
    print(
        "SIMULATION_NOT_REALITY:",
        report["simulation_not_reality"],
    )
    print(
        "ACTION_EXECUTED:",
        report["action_executed"],
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
    print("OFFICIAL_BOUND_CORES: 37/54")
    print("NEXT_AUTHORIZED: DNA-38")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
