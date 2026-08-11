#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-12: TOOL INTELLIGENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_12_TOOL_INTELLIGENCE.py
"""

from __future__ import annotations

import hashlib
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

CANON_DNA12: Dict[str, str] = {
    "id": "DNA-12",
    "name": "Tool Intelligence",
    "purpose": (
        "SIGMA biết khi nào cần suy nghĩ, khi nào dùng công cụ, "
        "và không coi tool output tự động là chân lý."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
KNOWLEDGE_GRAPH_SCHEMA = "SIGMA_KNOWLEDGE_GRAPH_V1"
TOOL_INTELLIGENCE_SCHEMA = "SIGMA_TOOL_INTELLIGENCE_V1"

TOOL_USE_SIGNALS = [
    "requires_current_external_state",
    "requires_retrieval",
    "requires_exact_computation",
    "requires_observation_or_measurement",
    "requires_external_action",
]

DECISION_MODES = [
    "THINK_ONLY",
    "TOOL_ASSISTED_REASONING",
    "THINK_AND_DECLARE_TOOL_GAP",
    "THINK_AND_IDENTIFY_EVIDENCE_GAP",
]

TOOL_INTELLIGENCE_CONTRACT: Dict[str, Any] = {
    "schema": TOOL_INTELLIGENCE_SCHEMA,
    "decision_modes": deepcopy(DECISION_MODES),
    "tool_use_signals": deepcopy(TOOL_USE_SIGNALS),
    "reasoning_required_for_all_modes": True,
    "tool_output_policy": {
        "automatically_true": False,
        "default_truth_status": "UNVERIFIED_TOOL_OUTPUT",
        "verification_required": True,
        "automatic_knowledge_promotion": False,
    },
    "tool_execution_authority": False,
    "external_tool_execution_started": False,
    "model_calls_started": False,
    "learning_runtime_started": False,
    "world_runtime_started": False,
    "knowledge_graph_write_authority": False,
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
    if actual != CANON_DNA12:
        raise RuntimeError(
            "DNA-12_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA12, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-12_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    graph = state.get("knowledge_graph")
    if not isinstance(graph, dict):
        raise RuntimeError("DNA-11_KNOWLEDGE_GRAPH_REQUIRED")

    graph_contract = graph.get("contract")
    if not isinstance(graph_contract, dict):
        raise RuntimeError(
            "DNA-11_KNOWLEDGE_GRAPH_CONTRACT_REQUIRED"
        )

    if graph_contract.get("schema") != KNOWLEDGE_GRAPH_SCHEMA:
        raise ValueError(
            "DNA-12_KNOWLEDGE_GRAPH_SCHEMA_MISMATCH:"
            f"{graph_contract.get('schema')!r}"
        )

    if not isinstance(graph.get("nodes"), dict):
        raise TypeError("knowledge_graph['nodes'] must be a dict")
    if not isinstance(graph.get("edges"), list):
        raise TypeError("knowledge_graph['edges'] must be a list")
    if not isinstance(graph.get("revision_events"), list):
        raise TypeError(
            "knowledge_graph['revision_events'] must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-11_OUTPUT_REQUIRED")

    dna11_output = outputs.get("DNA-11")
    if not isinstance(dna11_output, dict):
        raise RuntimeError("DNA-11_OUTPUT_REQUIRED")

    return state, graph, dna11_output


def _install_tool_intelligence(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("tool_intelligence")

    expected = {
        "contract": deepcopy(TOOL_INTELLIGENCE_CONTRACT),
        "decisions": [],
        "tool_outputs": [],
    }

    if existing is None:
        state["tool_intelligence"] = expected
        return state["tool_intelligence"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['tool_intelligence'] must be a dict"
        )

    if existing.get("contract") != TOOL_INTELLIGENCE_CONTRACT:
        raise ValueError(
            "DNA-12_TOOL_INTELLIGENCE_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("decisions"), list):
        raise TypeError(
            "tool_intelligence['decisions'] must be a list"
        )

    if not isinstance(existing.get("tool_outputs"), list):
        raise TypeError(
            "tool_intelligence['tool_outputs'] must be a list"
        )

    return existing


def _decision_context(
    context: Dict[str, Any],
) -> Dict[str, Any]:
    supplied = context.get("tool_decision_context", {})
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['tool_decision_context'] must be a dict"
        )

    normalized: Dict[str, Any] = {
        "internal_reasoning_sufficient": supplied.get(
            "internal_reasoning_sufficient",
            True,
        ),
        "tool_available": supplied.get(
            "tool_available",
            False,
        ),
        "candidate_tool": supplied.get("candidate_tool"),
    }

    for key in (
        "internal_reasoning_sufficient",
        "tool_available",
    ):
        if not isinstance(normalized[key], bool):
            raise TypeError(
                f"tool_decision_context['{key}'] must be a bool"
            )

    candidate_tool = normalized["candidate_tool"]
    if candidate_tool is not None:
        if not isinstance(candidate_tool, str):
            raise TypeError(
                "tool_decision_context['candidate_tool'] "
                "must be a string or None"
            )
        candidate_tool = candidate_tool.strip()
        if not candidate_tool:
            raise ValueError(
                "DNA-12_CANDIDATE_TOOL_CANNOT_BE_EMPTY"
            )
        normalized["candidate_tool"] = candidate_tool

    signals: Dict[str, bool] = {}
    for key in TOOL_USE_SIGNALS:
        value = supplied.get(key, False)
        if not isinstance(value, bool):
            raise TypeError(
                f"tool_decision_context['{key}'] must be a bool"
            )
        signals[key] = value

    normalized["signals"] = signals
    return normalized


def _make_tool_decision(
    context: Dict[str, Any],
    tool_state: Dict[str, Any],
) -> Dict[str, Any]:
    basis = _decision_context(context)
    active_signals = [
        key
        for key, value in basis["signals"].items()
        if value
    ]
    tool_required = bool(active_signals)
    tool_available = basis["tool_available"]

    if tool_required and tool_available:
        mode = "TOOL_ASSISTED_REASONING"
        decision_reason = "TOOL_USE_SIGNAL_PRESENT"
        tool_gap = None
    elif tool_required and not tool_available:
        mode = "THINK_AND_DECLARE_TOOL_GAP"
        decision_reason = "REQUIRED_TOOL_UNAVAILABLE"
        tool_gap = {
            "required_capabilities": deepcopy(active_signals),
            "candidate_tool": basis["candidate_tool"],
            "status": "UNRESOLVED_TOOL_GAP",
        }
    elif basis["internal_reasoning_sufficient"]:
        mode = "THINK_ONLY"
        decision_reason = "INTERNAL_REASONING_SUFFICIENT"
        tool_gap = None
    else:
        mode = "THINK_AND_IDENTIFY_EVIDENCE_GAP"
        decision_reason = (
            "NO_TOOL_JUSTIFICATION_AND_REASONING_INSUFFICIENT"
        )
        tool_gap = {
            "required_capabilities": [],
            "candidate_tool": basis["candidate_tool"],
            "status": "UNRESOLVED_EVIDENCE_GAP",
        }

    sequence = len(tool_state["decisions"]) + 1
    decision = {
        "sequence": sequence,
        "decision_id": f"DNA-12-DECISION-{sequence:04d}",
        "mode": mode,
        "reasoning_required": True,
        "internal_reasoning_sufficient": basis[
            "internal_reasoning_sufficient"
        ],
        "tool_required": tool_required,
        "tool_available": tool_available,
        "active_tool_signals": active_signals,
        "candidate_tool": basis["candidate_tool"],
        "decision_reason": decision_reason,
        "tool_gap": tool_gap,
        "tool_execution_authorized": False,
        "tool_executed_by_dna12": False,
        "status": "DECIDED",
    }
    tool_state["decisions"].append(decision)
    return decision


def _non_empty_string(value: Any, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"DNA-12_{field_name.upper()}_REQUIRED")
    return normalized


def _classify_tool_output(
    context: Dict[str, Any],
    tool_state: Dict[str, Any],
    decision: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    supplied = context.get("tool_output")
    if supplied is None:
        return None

    if not isinstance(supplied, dict):
        raise TypeError("context['tool_output'] must be a dict")

    tool_name = _non_empty_string(
        supplied.get("tool_name"),
        "tool_name",
    )
    invocation_id = _non_empty_string(
        supplied.get("invocation_id"),
        "invocation_id",
    )

    if "output" not in supplied:
        raise ValueError("DNA-12_TOOL_OUTPUT_VALUE_REQUIRED")

    candidate_tool = decision.get("candidate_tool")
    if (
        isinstance(candidate_tool, str)
        and candidate_tool
        and tool_name != candidate_tool
    ):
        raise ValueError(
            "DNA-12_TOOL_OUTPUT_TOOL_NAME_MISMATCH"
        )

    provenance = supplied.get("provenance", [])
    if not isinstance(provenance, list):
        raise TypeError(
            "tool_output['provenance'] must be a list"
        )

    sequence = len(tool_state["tool_outputs"]) + 1
    record = {
        "sequence": sequence,
        "tool_output_id": (
            f"DNA-12-TOOL-OUTPUT-{sequence:04d}"
        ),
        "decision_id": decision["decision_id"],
        "tool_name": tool_name,
        "invocation_id": invocation_id,
        "output": deepcopy(supplied["output"]),
        "output_sha256": _sha256_json(supplied["output"]),
        "provenance": deepcopy(provenance),
        "caller_truth_claim": deepcopy(
            supplied.get("truth_claim")
        ),
        "truth_status": "UNVERIFIED_TOOL_OUTPUT",
        "automatically_true": False,
        "verification_required": True,
        "knowledge_promotion_allowed": False,
        "knowledge_promoted": False,
        "external_tool_executed_by_dna12": False,
        "status": "CLASSIFIED_AS_UNVERIFIED_EVIDENCE",
    }
    tool_state["tool_outputs"].append(record)
    return record


def dna12_tool_intelligence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Decide whether current work should remain reasoning-only or require
    tool-assisted reasoning, then classify any supplied tool output as
    unverified evidence rather than automatic truth.

    DNA-12 does not execute a tool, call a model, start Learning/World or
    persistent Memory runtimes, write to the knowledge graph, auto-learn,
    execute F174, or modify Canon.
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
    trace.append("DNA-12")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, graph, _dna11_output = _validate_dependencies(
        context
    )
    tool_state = _install_tool_intelligence(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)
    graph_sha256_before = _sha256_json(graph)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-12",
            "operation": "TOOL_INTELLIGENCE_CONTRACT_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "tool_intelligence_schema": TOOL_INTELLIGENCE_SCHEMA,
            "external_tool_execution_started": False,
            "knowledge_graph_write_authority": False,
        }
    )

    decision = _make_tool_decision(context, tool_state)
    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-12",
            "operation": "THINK_OR_TOOL_DECISION_MADE",
            "canonical_sha256": canonical_sha256,
            "decision_id": decision["decision_id"],
            "decision_mode": decision["mode"],
            "tool_required": decision["tool_required"],
            "tool_execution_authorized": False,
        }
    )

    tool_output_record = _classify_tool_output(
        context,
        tool_state,
        decision,
    )
    if tool_output_record is not None:
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-12",
                "operation": "TOOL_OUTPUT_CLASSIFIED_UNVERIFIED",
                "canonical_sha256": canonical_sha256,
                "tool_output_id": tool_output_record[
                    "tool_output_id"
                ],
                "truth_status": tool_output_record[
                    "truth_status"
                ],
                "automatically_true": False,
                "knowledge_promoted": False,
            }
        )

    graph_sha256_after = _sha256_json(graph)
    if graph_sha256_before != graph_sha256_after:
        raise AssertionError(
            "DNA-12_UNAUTHORIZED_KNOWLEDGE_GRAPH_CHANGE"
        )

    outputs["DNA-12"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "tool_intelligence_contract": deepcopy(
            TOOL_INTELLIGENCE_CONTRACT
        ),
        "decision": deepcopy(decision),
        "tool_output_record": deepcopy(tool_output_record),
        "tool_output_automatically_true": False,
        "knowledge_graph_modified": False,
        "external_tool_executed": False,
        "model_called": False,
        "knowledge_promoted": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna12(core54: Core54Like) -> None:
    core = core54.get("DNA-12")
    assert_exact_canon(core)
    core54.bind(
        "DNA-12",
        dna12_tool_intelligence,
    )


def _build_base_probe() -> Dict[str, Any]:
    return {
        "trace": [],
        "caller_data": {"preserve": True},
        "goal": {
            "id": "GOAL-DNA12",
            "statement": "select reasoning or tool use truthfully",
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
            "id": "WORLD-DNA12-SELF-CHECK",
            "state": "INITIAL",
        },
        "action": {
            "id": "ACTION-DNA12-01",
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
                "subject": "DNA-12_SELF_CHECK",
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
                    "TOOL_OUTPUT_REQUIRES_VERIFICATION"
                ],
            },
        },
    }


def _run_through(
    core54: Core54Like,
    context: Dict[str, Any],
    final_core_id: str,
) -> Dict[str, Any]:
    final_index = int(final_core_id.split("-")[1])
    result = deepcopy(context)
    for index in range(1, final_index + 1):
        core_id = f"DNA-{index:02d}"
        result = core54.get(core_id).activate(result)
    return result


def _derive_candidate_sha256(
    core54: Core54Like,
    base_probe: Dict[str, Any],
) -> str:
    through_dna08 = _run_through(
        core54,
        base_probe,
        "DNA-08",
    )
    event = through_dna08[
        "core54_outputs"
    ]["DNA-08"]["world_event"]
    if not isinstance(event, dict):
        raise AssertionError(
            "DNA-12_SELF_CHECK_DNA08_EVENT_MISSING"
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


def self_check_dna12(
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
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna12_core = core54.get("DNA-12")
    assert_exact_canon(dna12_core)
    bind_dna12(core54)

    base_probe = _build_base_probe()
    candidate_sha256 = _derive_candidate_sha256(
        core54,
        base_probe,
    )

    tool_probe = deepcopy(base_probe)
    tool_probe["verification"] = _verification(
        candidate_sha256
    )
    tool_probe["knowledge_confidence"] = 0.88
    tool_probe["knowledge_contradictions"] = []
    tool_probe["knowledge_relations"] = [
        {
            "relation": "related_to",
            "target_id": "CONCEPT-TOOL-EVIDENCE",
            "target_type": "concept",
        }
    ]
    tool_probe["tool_decision_context"] = {
        "internal_reasoning_sufficient": False,
        "tool_available": True,
        "candidate_tool": "DETERMINISTIC_CALCULATOR",
        "requires_current_external_state": False,
        "requires_retrieval": False,
        "requires_exact_computation": True,
        "requires_observation_or_measurement": False,
        "requires_external_action": False,
    }
    tool_probe["tool_output"] = {
        "tool_name": "DETERMINISTIC_CALCULATOR",
        "invocation_id": "CALC-SELF-CHECK-0001",
        "output": {
            "expression": "2+2",
            "value": 4,
        },
        "provenance": [
            {
                "source": "SELF_CHECK_FIXTURE",
                "deterministic": True,
            }
        ],
        "truth_claim": "VERIFIED",
    }
    tool_snapshot = deepcopy(tool_probe)

    through_dna11 = _run_through(
        core54,
        tool_probe,
        "DNA-11",
    )
    graph_before = deepcopy(
        through_dna11["cognitive_state"]["knowledge_graph"]
    )
    graph_before_sha256 = _sha256_json(graph_before)

    tool_result = dna12_core.activate(through_dna11)

    assert tool_probe == tool_snapshot
    assert tool_result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 13)
    ]

    dna12 = tool_result["core54_outputs"]["DNA-12"]
    assert dna12["canonical_gene"] == CANON_DNA12
    assert dna12["tool_intelligence_contract"] == (
        TOOL_INTELLIGENCE_CONTRACT
    )
    assert dna12["tool_output_automatically_true"] is False
    assert dna12["knowledge_graph_modified"] is False
    assert dna12["external_tool_executed"] is False
    assert dna12["model_called"] is False
    assert dna12["knowledge_promoted"] is False
    assert dna12["status"] == "CANON_ALIGNED"

    decision = dna12["decision"]
    assert decision["sequence"] == 1
    assert decision["decision_id"] == (
        "DNA-12-DECISION-0001"
    )
    assert decision["mode"] == "TOOL_ASSISTED_REASONING"
    assert decision["reasoning_required"] is True
    assert decision["internal_reasoning_sufficient"] is False
    assert decision["tool_required"] is True
    assert decision["tool_available"] is True
    assert decision["active_tool_signals"] == [
        "requires_exact_computation"
    ]
    assert decision["candidate_tool"] == (
        "DETERMINISTIC_CALCULATOR"
    )
    assert decision["decision_reason"] == (
        "TOOL_USE_SIGNAL_PRESENT"
    )
    assert decision["tool_gap"] is None
    assert decision["tool_execution_authorized"] is False
    assert decision["tool_executed_by_dna12"] is False

    tool_output = dna12["tool_output_record"]
    assert tool_output is not None
    assert tool_output["sequence"] == 1
    assert tool_output["tool_output_id"] == (
        "DNA-12-TOOL-OUTPUT-0001"
    )
    assert tool_output["decision_id"] == (
        "DNA-12-DECISION-0001"
    )
    assert tool_output["tool_name"] == (
        "DETERMINISTIC_CALCULATOR"
    )
    assert tool_output["invocation_id"] == (
        "CALC-SELF-CHECK-0001"
    )
    assert tool_output["output"] == {
        "expression": "2+2",
        "value": 4,
    }
    assert tool_output["caller_truth_claim"] == "VERIFIED"
    assert tool_output["truth_status"] == (
        "UNVERIFIED_TOOL_OUTPUT"
    )
    assert tool_output["automatically_true"] is False
    assert tool_output["verification_required"] is True
    assert (
        tool_output["knowledge_promotion_allowed"]
        is False
    )
    assert tool_output["knowledge_promoted"] is False
    assert (
        tool_output["external_tool_executed_by_dna12"]
        is False
    )
    assert tool_output["status"] == (
        "CLASSIFIED_AS_UNVERIFIED_EVIDENCE"
    )

    graph_after = tool_result[
        "cognitive_state"
    ]["knowledge_graph"]
    assert graph_after == graph_before
    assert _sha256_json(graph_after) == graph_before_sha256

    tool_state = tool_result[
        "cognitive_state"
    ]["tool_intelligence"]
    assert tool_state["contract"] == TOOL_INTELLIGENCE_CONTRACT
    assert tool_state["decisions"] == [decision]
    assert tool_state["tool_outputs"] == [tool_output]

    provenance = tool_result[
        "cognitive_state"
    ]["provenance"]
    assert provenance[-3]["operation"] == (
        "TOOL_INTELLIGENCE_CONTRACT_ESTABLISHED"
    )
    assert provenance[-2]["operation"] == (
        "THINK_OR_TOOL_DECISION_MADE"
    )
    assert provenance[-2]["decision_mode"] == (
        "TOOL_ASSISTED_REASONING"
    )
    assert provenance[-1]["operation"] == (
        "TOOL_OUTPUT_CLASSIFIED_UNVERIFIED"
    )
    assert provenance[-1]["automatically_true"] is False
    assert provenance[-1]["knowledge_promoted"] is False

    # THINK_ONLY when internal reasoning is sufficient and no tool-use
    # signal is present.
    think_input = deepcopy(through_dna11)
    think_input["tool_decision_context"] = {
        "internal_reasoning_sufficient": True,
        "tool_available": False,
        "candidate_tool": None,
        **{key: False for key in TOOL_USE_SIGNALS},
    }
    think_input.pop("tool_output", None)
    think_result = dna12_core.activate(think_input)
    think_decision = think_result[
        "core54_outputs"
    ]["DNA-12"]["decision"]
    assert think_decision["mode"] == "THINK_ONLY"
    assert think_decision["tool_required"] is False
    assert think_decision["tool_available"] is False
    assert think_decision["tool_gap"] is None
    assert think_result[
        "core54_outputs"
    ]["DNA-12"]["tool_output_record"] is None

    # Tool need with no available tool must become an explicit gap, not a
    # fabricated tool result or external execution.
    gap_input = deepcopy(through_dna11)
    gap_input["tool_decision_context"] = {
        "internal_reasoning_sufficient": False,
        "tool_available": False,
        "candidate_tool": "CURRENT_STATE_RETRIEVER",
        "requires_current_external_state": True,
        "requires_retrieval": True,
        "requires_exact_computation": False,
        "requires_observation_or_measurement": False,
        "requires_external_action": False,
    }
    gap_input.pop("tool_output", None)
    gap_result = dna12_core.activate(gap_input)
    gap_decision = gap_result[
        "core54_outputs"
    ]["DNA-12"]["decision"]
    assert gap_decision["mode"] == (
        "THINK_AND_DECLARE_TOOL_GAP"
    )
    assert gap_decision["tool_required"] is True
    assert gap_decision["tool_available"] is False
    assert gap_decision["tool_gap"] == {
        "required_capabilities": [
            "requires_current_external_state",
            "requires_retrieval",
        ],
        "candidate_tool": "CURRENT_STATE_RETRIEVER",
        "status": "UNRESOLVED_TOOL_GAP",
    }
    assert gap_result[
        "core54_outputs"
    ]["DNA-12"]["external_tool_executed"] is False

    # Insufficient reasoning with no justified tool signal remains an
    # explicit evidence gap.
    evidence_gap_input = deepcopy(through_dna11)
    evidence_gap_input["tool_decision_context"] = {
        "internal_reasoning_sufficient": False,
        "tool_available": True,
        "candidate_tool": None,
        **{key: False for key in TOOL_USE_SIGNALS},
    }
    evidence_gap_input.pop("tool_output", None)
    evidence_gap_result = dna12_core.activate(
        evidence_gap_input
    )
    evidence_gap_decision = evidence_gap_result[
        "core54_outputs"
    ]["DNA-12"]["decision"]
    assert evidence_gap_decision["mode"] == (
        "THINK_AND_IDENTIFY_EVIDENCE_GAP"
    )
    assert evidence_gap_decision["tool_required"] is False

    # Tool output must match an explicitly selected candidate tool.
    mismatch_input = deepcopy(through_dna11)
    mismatch_input["tool_decision_context"] = deepcopy(
        tool_probe["tool_decision_context"]
    )
    mismatch_input["tool_output"] = deepcopy(
        tool_probe["tool_output"]
    )
    mismatch_input["tool_output"]["tool_name"] = (
        "DIFFERENT_TOOL"
    )
    try:
        dna12_core.activate(mismatch_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-12_TOOL_OUTPUT_TOOL_NAME_MISMATCH"
        )
    else:
        raise AssertionError(
            "DNA-12_ACCEPTED_TOOL_NAME_MISMATCH"
        )

    # Invalid signal types must fail closed.
    invalid_signal_input = deepcopy(through_dna11)
    invalid_signal_input["tool_decision_context"] = {
        "requires_retrieval": "YES",
    }
    try:
        dna12_core.activate(invalid_signal_input)
    except TypeError as exc:
        assert "requires_retrieval" in str(exc)
    else:
        raise AssertionError(
            "DNA-12_ACCEPTED_INVALID_TOOL_SIGNAL"
        )

    # Reject the old provisional root marker as the official contract.
    assert "tool_decision" not in tool_result
    assert "flags" not in tool_result
    assert "requests" not in tool_result
    assert "blocks" not in tool_result

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
        "core_id": "DNA-12",
        "canon_mapping": "PASS",
        "think_decision": "PASS",
        "tool_decision": "PASS",
        "tool_gap": "PASS",
        "tool_output_not_truth": "PASS",
        "knowledge_graph_unchanged": "PASS",
        "external_tool_executed": False,
        "model_called": False,
        "knowledge_promoted": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-13"
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
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-12_FAIL: REQUIRED_PATH_NOT_FOUND")
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
    except Exception as exc:
        print("DNA-12_FAIL: IMPORT_ERROR")
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
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna12(
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
            for index in range(1, 13)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-12_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-12_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_12_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("THINK_DECISION:", report["think_decision"])
    print("TOOL_DECISION:", report["tool_decision"])
    print("TOOL_GAP:", report["tool_gap"])
    print(
        "TOOL_OUTPUT_NOT_TRUTH:",
        report["tool_output_not_truth"],
    )
    print(
        "KNOWLEDGE_GRAPH_UNCHANGED:",
        report["knowledge_graph_unchanged"],
    )
    print(
        "EXTERNAL_TOOL_EXECUTED:",
        report["external_tool_executed"],
    )
    print("MODEL_CALLED:", report["model_called"])
    print(
        "KNOWLEDGE_PROMOTED:",
        report["knowledge_promoted"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 12/54")
    print("NEXT_AUTHORIZED: DNA-13")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
