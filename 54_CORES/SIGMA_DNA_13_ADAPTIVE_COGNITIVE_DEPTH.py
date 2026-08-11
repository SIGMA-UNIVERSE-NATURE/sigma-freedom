#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-13: ADAPTIVE COGNITIVE DEPTH
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH.py
"""

from __future__ import annotations

import hashlib
import json
import math
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

CANON_DNA13: Dict[str, str] = {
    "id": "DNA-13",
    "name": "Adaptive Cognitive Depth",
    "purpose": (
        "Độ sâu suy luận thích nghi theo uncertainty, risk, novelty, "
        "contradiction và expected value."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
TOOL_INTELLIGENCE_SCHEMA = "SIGMA_TOOL_INTELLIGENCE_V1"
ADAPTIVE_DEPTH_SCHEMA = "SIGMA_ADAPTIVE_COGNITIVE_DEPTH_V1"

CANONICAL_DEPTH_FACTORS = [
    "uncertainty",
    "risk",
    "novelty",
    "contradiction",
    "expected_value",
]

ADAPTIVE_DEPTH_CONTRACT: Dict[str, Any] = {
    "schema": ADAPTIVE_DEPTH_SCHEMA,
    "canonical_factors": deepcopy(CANONICAL_DEPTH_FACTORS),
    "factor_range": {
        "minimum": 0.0,
        "maximum": 1.0,
    },
    "all_factors_considered": True,
    "aggregation": {
        "method": "NON_COMPENSATORY_MAXIMUM",
        "result_range": [0.0, 1.0],
        "property": (
            "A_HIGH_CANON_FACTOR_CANNOT_BE_CANCELLED_BY_LOW_OTHERS"
        ),
        "canon_status": "IMPLEMENTATION_ENCODING_NOT_CANON_FIELD",
    },
    "adaptive_rule": (
        "INCREASING_ANY_CANON_FACTOR_MUST_NOT_DECREASE_DEPTH"
    ),
    "reasoning_execution_authority": False,
    "compute_allocation_authority": False,
    "tool_execution_authority": False,
    "model_calls_started": False,
    "learning_runtime_started": False,
    "world_runtime_started": False,
    "f174_execution_started": False,
    "external_action_started": False,
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
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA13:
        raise RuntimeError(
            "DNA-13_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA13, "actual": actual},
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
            "DNA-13_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    tool_state = state.get("tool_intelligence")
    if not isinstance(tool_state, dict):
        raise RuntimeError(
            "DNA-12_TOOL_INTELLIGENCE_REQUIRED"
        )

    tool_contract = tool_state.get("contract")
    if not isinstance(tool_contract, dict):
        raise RuntimeError(
            "DNA-12_TOOL_INTELLIGENCE_CONTRACT_REQUIRED"
        )

    if tool_contract.get("schema") != TOOL_INTELLIGENCE_SCHEMA:
        raise ValueError(
            "DNA-13_TOOL_INTELLIGENCE_SCHEMA_MISMATCH:"
            f"{tool_contract.get('schema')!r}"
        )

    if not isinstance(tool_state.get("decisions"), list):
        raise TypeError(
            "tool_intelligence['decisions'] must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-12_OUTPUT_REQUIRED")

    dna12_output = outputs.get("DNA-12")
    if not isinstance(dna12_output, dict):
        raise RuntimeError("DNA-12_OUTPUT_REQUIRED")

    return state, dna12_output


def _install_adaptive_depth_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("adaptive_cognitive_depth")

    expected = {
        "contract": deepcopy(ADAPTIVE_DEPTH_CONTRACT),
        "assessments": [],
    }

    if existing is None:
        state["adaptive_cognitive_depth"] = expected
        return state["adaptive_cognitive_depth"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['adaptive_cognitive_depth'] must be a dict"
        )

    if existing.get("contract") != ADAPTIVE_DEPTH_CONTRACT:
        raise ValueError(
            "DNA-13_ADAPTIVE_DEPTH_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("assessments"), list):
        raise TypeError(
            "adaptive_cognitive_depth['assessments'] must be a list"
        )

    return existing


def _normalize_factor_value(
    factor: str,
    value: Any,
) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            f"cognitive_depth_signals['{factor}'] must be a number"
        )

    normalized = float(value)
    if not math.isfinite(normalized):
        raise ValueError(
            f"DNA-13_FACTOR_NOT_FINITE:{factor}"
        )

    if not 0.0 <= normalized <= 1.0:
        raise ValueError(
            f"DNA-13_FACTOR_OUT_OF_RANGE:{factor}"
        )

    return normalized


def _parse_depth_signals(
    context: Dict[str, Any],
) -> Tuple[Optional[Dict[str, float]], List[str]]:
    supplied = context.get("cognitive_depth_signals")

    if supplied is None:
        return None, deepcopy(CANONICAL_DEPTH_FACTORS)

    if not isinstance(supplied, dict):
        raise TypeError(
            "context['cognitive_depth_signals'] must be a dict"
        )

    unknown = sorted(
        set(supplied) - set(CANONICAL_DEPTH_FACTORS)
    )
    if unknown:
        raise ValueError(
            "DNA-13_UNKNOWN_DEPTH_FACTORS:"
            + ",".join(unknown)
        )

    missing = [
        factor
        for factor in CANONICAL_DEPTH_FACTORS
        if factor not in supplied
    ]
    if missing:
        return None, missing

    normalized = {
        factor: _normalize_factor_value(
            factor,
            supplied[factor],
        )
        for factor in CANONICAL_DEPTH_FACTORS
    }
    return normalized, []


def _make_depth_assessment(
    signals: Dict[str, float],
    depth_state: Dict[str, Any],
) -> Dict[str, Any]:
    depth_score = max(signals.values())
    dominant_factors = [
        factor
        for factor in CANONICAL_DEPTH_FACTORS
        if signals[factor] == depth_score
    ]

    sequence = len(depth_state["assessments"]) + 1
    assessment = {
        "sequence": sequence,
        "assessment_id": (
            f"DNA-13-DEPTH-{sequence:04d}"
        ),
        "signals": deepcopy(signals),
        "aggregation_method": "NON_COMPENSATORY_MAXIMUM",
        "normalized_depth": depth_score,
        "dominant_factors": dominant_factors,
        "factor_mean": (
            sum(signals.values())
            / len(CANONICAL_DEPTH_FACTORS)
        ),
        "adaptive": True,
        "reasoning_execution_started": False,
        "compute_allocated": False,
        "tool_executed": False,
        "model_called": False,
        "status": "DEPTH_REQUIREMENT_ASSESSED",
    }
    depth_state["assessments"].append(assessment)
    return assessment


def dna13_adaptive_cognitive_depth(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Assess required reasoning depth from the five exact Canon factors.

    DNA-13 emits a normalized depth requirement. It does not execute deeper
    reasoning, allocate compute, invoke tools/models, start Learning/World
    Runtime, execute F174, act externally, or modify Canon.
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
    trace.append("DNA-13")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, _dna12_output = _validate_dependencies(context)
    depth_state = _install_adaptive_depth_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-13",
            "operation": (
                "ADAPTIVE_COGNITIVE_DEPTH_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "adaptive_depth_schema": ADAPTIVE_DEPTH_SCHEMA,
            "reasoning_execution_started": False,
            "compute_allocated": False,
        }
    )

    signals, missing = _parse_depth_signals(context)
    assessment: Optional[Dict[str, Any]] = None

    if signals is not None:
        assessment = _make_depth_assessment(
            signals,
            depth_state,
        )
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-13",
                "operation": (
                    "ADAPTIVE_DEPTH_REQUIREMENT_ASSESSED"
                ),
                "canonical_sha256": canonical_sha256,
                "assessment_id": assessment["assessment_id"],
                "normalized_depth": assessment[
                    "normalized_depth"
                ],
                "dominant_factors": deepcopy(
                    assessment["dominant_factors"]
                ),
                "reasoning_execution_started": False,
            }
        )
    else:
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-13",
                "operation": (
                    "ADAPTIVE_DEPTH_SIGNALS_INCOMPLETE"
                ),
                "canonical_sha256": canonical_sha256,
                "missing_factors": deepcopy(missing),
                "reasoning_execution_started": False,
            }
        )

    outputs["DNA-13"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "adaptive_depth_contract": deepcopy(
            ADAPTIVE_DEPTH_CONTRACT
        ),
        "signals_complete": signals is not None,
        "missing_factors": deepcopy(missing),
        "depth_assessment": deepcopy(assessment),
        "reasoning_executed": False,
        "compute_allocated": False,
        "tool_executed": False,
        "model_called": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna13(core54: Core54Like) -> None:
    core = core54.get("DNA-13")
    assert_exact_canon(core)
    core54.bind(
        "DNA-13",
        dna13_adaptive_cognitive_depth,
    )


def _build_base_probe() -> Dict[str, Any]:
    return {
        "trace": [],
        "caller_data": {"preserve": True},
        "goal": {
            "id": "GOAL-DNA13",
            "statement": "adapt reasoning depth to canonical signals",
        },
        "strategy": "STRATEGY-A",
        "next_strategy": "STRATEGY-B",
        "failure": {
            "detected": True,
            "layer": "verification",
            "recovery_operation": "REFRAME",
            "reason": "FIRST_STRATEGY_FAILED",
        },
        "environment": {
            "id": "WORLD-DNA13-SELF-CHECK",
            "state": "INITIAL",
        },
        "action": {
            "id": "ACTION-DNA13-01",
            "description": "APPLY_TEST_INTERVENTION",
        },
        "consequence": {
            "observed_change": "STATE_UPDATED",
        },
        "experience": {
            "candidate_learning": (
                "ACTION_CHANGED_ENVIRONMENT_STATE"
            ),
        },
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {
                "subject": "DNA-13_SELF_CHECK",
            },
            "provenance": [
                {
                    "sequence": 1,
                    "core_id": "CALLER",
                    "operation": "INPUT_CREATED",
                }
            ],
            "uncertainty": {
                "open_items": [
                    "DEPTH_REQUIRES_CANONICAL_SIGNAL_ASSESSMENT"
                ],
            },
        },
    }


def _run_through(
    core54: Core54Like,
    context: Dict[str, Any],
    final_index: int,
) -> Dict[str, Any]:
    result = deepcopy(context)
    for index in range(1, final_index + 1):
        result = core54.get(
            f"DNA-{index:02d}"
        ).activate(result)
    return result


def _derive_candidate_sha256(
    core54: Core54Like,
    base_probe: Dict[str, Any],
) -> str:
    through_dna08 = _run_through(
        core54,
        base_probe,
        8,
    )
    event = through_dna08[
        "core54_outputs"
    ]["DNA-08"]["world_event"]
    if not isinstance(event, dict):
        raise AssertionError(
            "DNA-13_SELF_CHECK_DNA08_EVENT_MISSING"
        )

    candidate_content = {
        "source_core_id": "DNA-08",
        "source_event_id": event.get("event_id"),
        "interaction_sha256": event.get(
            "interaction_sha256"
        ),
        "experience": deepcopy(event.get("experience")),
    }
    return _sha256_json(candidate_content)


def _verification(
    candidate_sha256: str,
) -> Dict[str, Any]:
    return {
        "learner_id": "LEARNER-A",
        "verifier_id": "VERIFIER-B",
        "verifier_independent": True,
        "independence_basis": [
            "SEPARATE_ROLE",
            "NO_SHARED_DECISION_AUTHORITY",
        ],
        "candidate_sha256": candidate_sha256,
        "method": "INDEPENDENT_REPLAY_AND_COMPARISON",
        "scope": "DNA-08_EXPERIENTIAL_EVENT",
        "evidence": [
            {
                "type": "REPLAY_RESULT",
                "result": "CONSISTENT",
            }
        ],
        "passed": True,
    }


def _complete_probe(
    core54: Core54Like,
) -> Dict[str, Any]:
    base_probe = _build_base_probe()
    candidate_sha256 = _derive_candidate_sha256(
        core54,
        base_probe,
    )

    probe = deepcopy(base_probe)
    probe["verification"] = _verification(
        candidate_sha256
    )
    probe["knowledge_confidence"] = 0.88
    probe["knowledge_contradictions"] = []
    probe["knowledge_relations"] = [
        {
            "relation": "related_to",
            "target_id": "CONCEPT-ADAPTIVE-DEPTH",
            "target_type": "concept",
        }
    ]
    probe["tool_decision_context"] = {
        "internal_reasoning_sufficient": True,
        "tool_available": False,
        "candidate_tool": None,
        "requires_current_external_state": False,
        "requires_retrieval": False,
        "requires_exact_computation": False,
        "requires_observation_or_measurement": False,
        "requires_external_action": False,
    }
    probe["cognitive_depth_signals"] = {
        "uncertainty": 0.91,
        "risk": 0.76,
        "novelty": 0.42,
        "contradiction": 0.88,
        "expected_value": 0.67,
    }
    return probe


def self_check_dna13(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for required_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
        "DNA-09",
        "DNA-10",
        "DNA-11",
        "DNA-12",
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna13_core = core54.get("DNA-13")
    assert_exact_canon(dna13_core)
    bind_dna13(core54)

    probe = _complete_probe(core54)
    snapshot = deepcopy(probe)

    through_dna12 = _run_through(
        core54,
        probe,
        12,
    )
    result = dna13_core.activate(through_dna12)

    assert probe == snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 14)
    ]

    dna13 = result["core54_outputs"]["DNA-13"]
    assert dna13["canonical_gene"] == CANON_DNA13
    assert dna13["adaptive_depth_contract"] == (
        ADAPTIVE_DEPTH_CONTRACT
    )
    assert dna13["signals_complete"] is True
    assert dna13["missing_factors"] == []
    assert dna13["reasoning_executed"] is False
    assert dna13["compute_allocated"] is False
    assert dna13["tool_executed"] is False
    assert dna13["model_called"] is False
    assert dna13["status"] == "CANON_ALIGNED"

    assessment = dna13["depth_assessment"]
    assert assessment is not None
    assert assessment["sequence"] == 1
    assert assessment["assessment_id"] == (
        "DNA-13-DEPTH-0001"
    )
    assert assessment["signals"] == (
        probe["cognitive_depth_signals"]
    )
    assert assessment["aggregation_method"] == (
        "NON_COMPENSATORY_MAXIMUM"
    )
    assert assessment["normalized_depth"] == 0.91
    assert assessment["dominant_factors"] == [
        "uncertainty"
    ]
    assert assessment["adaptive"] is True
    assert assessment["reasoning_execution_started"] is False
    assert assessment["compute_allocated"] is False
    assert assessment["tool_executed"] is False
    assert assessment["model_called"] is False
    assert assessment["status"] == (
        "DEPTH_REQUIREMENT_ASSESSED"
    )

    depth_state = result[
        "cognitive_state"
    ]["adaptive_cognitive_depth"]
    assert depth_state["contract"] == ADAPTIVE_DEPTH_CONTRACT
    assert depth_state["assessments"] == [assessment]

    provenance = result["cognitive_state"]["provenance"]
    assert provenance[-2]["operation"] == (
        "ADAPTIVE_COGNITIVE_DEPTH_CONTRACT_ESTABLISHED"
    )
    assert provenance[-2]["compute_allocated"] is False
    assert provenance[-1]["operation"] == (
        "ADAPTIVE_DEPTH_REQUIREMENT_ASSESSED"
    )
    assert provenance[-1]["normalized_depth"] == 0.91
    assert provenance[-1]["dominant_factors"] == [
        "uncertainty"
    ]
    assert provenance[-1]["reasoning_execution_started"] is False

    # Increasing any Canon factor must never reduce assessed depth.
    low_signals = {
        factor: 0.20
        for factor in CANONICAL_DEPTH_FACTORS
    }
    low_input = deepcopy(through_dna12)
    low_input["cognitive_depth_signals"] = low_signals
    low_result = dna13_core.activate(low_input)
    low_score = low_result[
        "core54_outputs"
    ]["DNA-13"]["depth_assessment"]["normalized_depth"]
    assert low_score == 0.20

    for factor in CANONICAL_DEPTH_FACTORS:
        raised_input = deepcopy(through_dna12)
        raised_signals = deepcopy(low_signals)
        raised_signals[factor] = 0.90
        raised_input["cognitive_depth_signals"] = raised_signals
        raised_result = dna13_core.activate(raised_input)
        raised_assessment = raised_result[
            "core54_outputs"
        ]["DNA-13"]["depth_assessment"]
        assert raised_assessment["normalized_depth"] == 0.90
        assert raised_assessment["normalized_depth"] >= low_score
        assert factor in raised_assessment["dominant_factors"]

    # Missing factors must remain explicit; DNA-13 must not invent scores.
    incomplete_input = deepcopy(through_dna12)
    incomplete_input["cognitive_depth_signals"] = {
        "uncertainty": 0.7,
        "risk": 0.6,
    }
    incomplete = dna13_core.activate(incomplete_input)
    incomplete_output = incomplete[
        "core54_outputs"
    ]["DNA-13"]
    assert incomplete_output["signals_complete"] is False
    assert incomplete_output["missing_factors"] == [
        "novelty",
        "contradiction",
        "expected_value",
    ]
    assert incomplete_output["depth_assessment"] is None
    assert incomplete[
        "cognitive_state"
    ]["provenance"][-1]["operation"] == (
        "ADAPTIVE_DEPTH_SIGNALS_INCOMPLETE"
    )

    # Invalid factor values must fail closed.
    invalid_range = deepcopy(through_dna12)
    invalid_range["cognitive_depth_signals"] = deepcopy(
        probe["cognitive_depth_signals"]
    )
    invalid_range["cognitive_depth_signals"]["risk"] = 1.1
    try:
        dna13_core.activate(invalid_range)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-13_FACTOR_OUT_OF_RANGE:risk"
        )
    else:
        raise AssertionError(
            "DNA-13_ACCEPTED_OUT_OF_RANGE_FACTOR"
        )

    invalid_bool = deepcopy(through_dna12)
    invalid_bool["cognitive_depth_signals"] = deepcopy(
        probe["cognitive_depth_signals"]
    )
    invalid_bool["cognitive_depth_signals"]["novelty"] = True
    try:
        dna13_core.activate(invalid_bool)
    except TypeError as exc:
        assert "novelty" in str(exc)
    else:
        raise AssertionError(
            "DNA-13_ACCEPTED_BOOLEAN_FACTOR"
        )

    unknown_factor = deepcopy(through_dna12)
    unknown_factor["cognitive_depth_signals"] = deepcopy(
        probe["cognitive_depth_signals"]
    )
    unknown_factor["cognitive_depth_signals"]["eloquence"] = 1.0
    try:
        dna13_core.activate(unknown_factor)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-13_UNKNOWN_DEPTH_FACTORS:eloquence"
        )
    else:
        raise AssertionError(
            "DNA-13_ACCEPTED_NON_CANON_FACTOR"
        )

    # Reject the old provisional root marker as the official contract.
    assert "cognitive_depth" not in result
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
        "core_id": "DNA-13",
        "canon_mapping": "PASS",
        "five_factor_contract": "PASS",
        "adaptive_depth": "PASS",
        "monotonicity": "PASS",
        "missing_factors_explicit": "PASS",
        "reasoning_executed": False,
        "compute_allocated": False,
        "f174_executed": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-14"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    required_gene_files = [
        GENES_ROOT / "SIGMA_DNA_01_PURPOSE_EXISTENCE.py",
        (
            GENES_ROOT
            / "SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE.py"
        ),
        GENES_ROOT / "SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE.py",
        GENES_ROOT / "SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS.py",
        GENES_ROOT / "SIGMA_DNA_05_ETHICAL_INTELLIGENCE.py",
        GENES_ROOT / "SIGMA_DNA_06_INTERLAYER_FEEDBACK.py",
        GENES_ROOT / "SIGMA_DNA_07_PERSISTENT_EXISTENCE.py",
        GENES_ROOT / "SIGMA_DNA_08_LEARNING_WORLD.py",
        (
            GENES_ROOT
            / "SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL.py"
        ),
        GENES_ROOT / "SIGMA_DNA_10_MEMORY_GENOME.py",
        GENES_ROOT / "SIGMA_DNA_11_KNOWLEDGE_GRAPH.py",
        GENES_ROOT / "SIGMA_DNA_12_TOOL_INTELLIGENCE.py",
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-13_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        from SIGMA_DNA_01_PURPOSE_EXISTENCE import (
            self_check_dna01,
        )
        from SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE import (
            self_check_dna02,
        )
        from SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE import (
            self_check_dna03,
        )
        from SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS import (
            self_check_dna04,
        )
        from SIGMA_DNA_05_ETHICAL_INTELLIGENCE import (
            self_check_dna05,
        )
        from SIGMA_DNA_06_INTERLAYER_FEEDBACK import (
            self_check_dna06,
        )
        from SIGMA_DNA_07_PERSISTENT_EXISTENCE import (
            self_check_dna07,
        )
        from SIGMA_DNA_08_LEARNING_WORLD import (
            self_check_dna08,
        )
        from SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL import (
            self_check_dna09,
        )
        from SIGMA_DNA_10_MEMORY_GENOME import (
            self_check_dna10,
        )
        from SIGMA_DNA_11_KNOWLEDGE_GRAPH import (
            self_check_dna11,
        )
        from SIGMA_DNA_12_TOOL_INTELLIGENCE import (
            self_check_dna12,
        )
    except Exception as exc:
        print("DNA-13_FAIL: IMPORT_ERROR")
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

        prior_checks = (
            ("DNA-01", self_check_dna01),
            ("DNA-02", self_check_dna02),
            ("DNA-03", self_check_dna03),
            ("DNA-04", self_check_dna04),
            ("DNA-05", self_check_dna05),
            ("DNA-06", self_check_dna06),
            ("DNA-07", self_check_dna07),
            ("DNA-08", self_check_dna08),
            ("DNA-09", self_check_dna09),
            ("DNA-10", self_check_dna10),
            ("DNA-11", self_check_dna11),
            ("DNA-12", self_check_dna12),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna13(
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
            for index in range(1, 14)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-13_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-13_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_13_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "FIVE_FACTOR_CONTRACT:",
        report["five_factor_contract"],
    )
    print("ADAPTIVE_DEPTH:", report["adaptive_depth"])
    print("MONOTONICITY:", report["monotonicity"])
    print(
        "MISSING_FACTORS_EXPLICIT:",
        report["missing_factors_explicit"],
    )
    print(
        "REASONING_EXECUTED:",
        report["reasoning_executed"],
    )
    print(
        "COMPUTE_ALLOCATED:",
        report["compute_allocated"],
    )
    print("F174_EXECUTED:", report["f174_executed"])
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 13/54")
    print("NEXT_AUTHORIZED: DNA-14")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
