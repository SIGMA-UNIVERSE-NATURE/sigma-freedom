#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-07: PERSISTENT EXISTENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_07_PERSISTENT_EXISTENCE.py
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

CANON_DNA07: Dict[str, str] = {
    "id": "DNA-07",
    "name": "Persistent Existence",
    "purpose": (
        "Không bỏ mục tiêu vì thất bại đầu tiên; lưu checkpoint, "
        "đổi chiến lược, phục hồi và tiếp tục."
    ),
    "system": "evolution",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
FEEDBACK_SCHEMA = "SIGMA_INTERLAYER_FEEDBACK_V1"
PERSISTENCE_SCHEMA = "SIGMA_PERSISTENT_EXISTENCE_V1"

PERSISTENT_EXISTENCE_CONTRACT: Dict[str, Any] = {
    "schema": PERSISTENCE_SCHEMA,
    "first_failure_abandons_goal": False,
    "failure_cycle": [
        "SAVE_CHECKPOINT",
        "CHANGE_STRATEGY",
        "RECOVER",
        "CONTINUE",
    ],
    "checkpoint_storage_scope": "CURRENT_STRUCTURED_STATE",
    "memory_runtime_used": False,
    "strategy_must_change": True,
    "goal_must_be_preserved_on_first_failure": True,
    "execution_authority": False,
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


def _sha256_json(value: Dict[str, Any]) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
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
    if actual != CANON_DNA07:
        raise RuntimeError(
            "DNA-07_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA07, "actual": actual},
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
            "DNA-07_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    feedback = state.get("interlayer_feedback")
    if not isinstance(feedback, dict):
        raise RuntimeError(
            "DNA-06_INTERLAYER_FEEDBACK_REQUIRED"
        )

    feedback_contract = feedback.get("contract")
    if not isinstance(feedback_contract, dict):
        raise RuntimeError(
            "DNA-06_FEEDBACK_CONTRACT_REQUIRED"
        )

    if feedback_contract.get("schema") != FEEDBACK_SCHEMA:
        raise ValueError(
            "DNA-07_FEEDBACK_SCHEMA_MISMATCH:"
            f"{feedback_contract.get('schema')!r}"
        )

    feedback_events = feedback.get("events")
    if not isinstance(feedback_events, list):
        raise TypeError(
            "interlayer_feedback['events'] must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError(
            "DNA-06_OUTPUT_REQUIRED"
        )

    dna06_output = outputs.get("DNA-06")
    if not isinstance(dna06_output, dict):
        raise RuntimeError(
            "DNA-06_OUTPUT_REQUIRED"
        )

    return state, dna06_output


def _install_persistence_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("persistent_existence")

    expected = {
        "contract": deepcopy(
            PERSISTENT_EXISTENCE_CONTRACT
        ),
        "active_goal": None,
        "active_strategy": None,
        "checkpoints": [],
        "recovery_events": [],
    }

    if existing is None:
        state["persistent_existence"] = expected
        return state["persistent_existence"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['persistent_existence'] must be a dict"
        )

    if existing.get("contract") != (
        PERSISTENT_EXISTENCE_CONTRACT
    ):
        raise ValueError(
            "DNA-07_PERSISTENCE_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("checkpoints"), list):
        raise TypeError(
            "persistent_existence['checkpoints'] must be a list"
        )

    if not isinstance(existing.get("recovery_events"), list):
        raise TypeError(
            "persistent_existence['recovery_events'] must be a list"
        )

    return existing


def _failure_detected(
    dna06_output: Dict[str, Any],
) -> bool:
    detected = dna06_output.get("failure_detected")
    if not isinstance(detected, bool):
        raise TypeError(
            "DNA-06 failure_detected must be a bool"
        )
    return detected


def _latest_feedback_event(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    events = state["interlayer_feedback"]["events"]
    if not events:
        raise RuntimeError(
            "DNA-07_FAILURE_REQUIRES_DNA-06_FEEDBACK_EVENT"
        )

    event = events[-1]
    if not isinstance(event, dict):
        raise TypeError(
            "DNA-06 feedback event must be a dict"
        )

    if event.get("trigger") != "FAILURE":
        raise RuntimeError(
            "DNA-07_FAILURE_FEEDBACK_TRIGGER_REQUIRED"
        )

    if event.get("status") != "ACTIVATED":
        raise RuntimeError(
            "DNA-07_ACTIVE_FAILURE_FEEDBACK_REQUIRED"
        )

    return event


def _resolve_goal(
    context: Dict[str, Any],
    persistence: Dict[str, Any],
) -> Any:
    supplied = context.get("goal")
    active = persistence.get("active_goal")

    if supplied is None and active is None:
        raise RuntimeError(
            "DNA-07_GOAL_REQUIRED_ON_FAILURE"
        )

    if active is None:
        persistence["active_goal"] = deepcopy(supplied)
        return deepcopy(supplied)

    if supplied is not None and supplied != active:
        raise ValueError(
            "DNA-07_GOAL_CONTINUITY_CONFLICT"
        )

    return deepcopy(active)


def _resolve_strategy(
    context: Dict[str, Any],
    persistence: Dict[str, Any],
) -> Any:
    supplied = context.get("strategy")
    active = persistence.get("active_strategy")

    if supplied is None and active is None:
        raise RuntimeError(
            "DNA-07_CURRENT_STRATEGY_REQUIRED_ON_FAILURE"
        )

    if active is None:
        persistence["active_strategy"] = deepcopy(supplied)
        return deepcopy(supplied)

    if supplied is not None and supplied != active:
        raise ValueError(
            "DNA-07_ACTIVE_STRATEGY_CONFLICT"
        )

    return deepcopy(active)


def _save_checkpoint(
    context: Dict[str, Any],
    state: Dict[str, Any],
    persistence: Dict[str, Any],
    feedback_event: Dict[str, Any],
    goal: Any,
    strategy: Any,
) -> Dict[str, Any]:
    sequence = len(persistence["checkpoints"]) + 1
    checkpoint = {
        "sequence": sequence,
        "checkpoint_id": f"DNA-07-CP-{sequence:04d}",
        "goal": deepcopy(goal),
        "strategy": deepcopy(strategy),
        "failure": deepcopy(context.get("failure")),
        "cognitive_content": deepcopy(state.get("content")),
        "uncertainty": deepcopy(state.get("uncertainty")),
        "source_feedback_event_sequence": (
            feedback_event.get("sequence")
        ),
        "trace_at_failure": deepcopy(
            context.get("trace", [])
        ),
        "storage_scope": "CURRENT_STRUCTURED_STATE",
        "memory_runtime_used": False,
        "status": "SAVED",
    }
    persistence["checkpoints"].append(checkpoint)
    return checkpoint


def _recover_and_continue(
    context: Dict[str, Any],
    persistence: Dict[str, Any],
    checkpoint: Dict[str, Any],
    goal: Any,
    current_strategy: Any,
) -> Dict[str, Any]:
    next_strategy = context.get("next_strategy")
    first_failure = checkpoint["sequence"] == 1

    if next_strategy is None:
        event = {
            "sequence": (
                len(persistence["recovery_events"]) + 1
            ),
            "failure_sequence": checkpoint["sequence"],
            "first_failure": first_failure,
            "checkpoint_id": checkpoint["checkpoint_id"],
            "goal_preserved": True,
            "goal_abandoned": False,
            "strategy_change": {
                "from": deepcopy(current_strategy),
                "to": None,
                "status": "SELECTION_REQUIRED",
            },
            "recovery_status": (
                "WAITING_FOR_CHANGED_STRATEGY"
            ),
            "continuation_status": (
                "PAUSED_NOT_ABANDONED"
            ),
        }
        persistence["recovery_events"].append(event)
        return event

    if next_strategy == current_strategy:
        raise ValueError(
            "DNA-07_NEXT_STRATEGY_MUST_DIFFER"
        )

    persistence["active_goal"] = deepcopy(goal)
    persistence["active_strategy"] = deepcopy(
        next_strategy
    )

    event = {
        "sequence": (
            len(persistence["recovery_events"]) + 1
        ),
        "failure_sequence": checkpoint["sequence"],
        "first_failure": first_failure,
        "checkpoint_id": checkpoint["checkpoint_id"],
        "goal_preserved": True,
        "goal_abandoned": False,
        "strategy_change": {
            "from": deepcopy(current_strategy),
            "to": deepcopy(next_strategy),
            "status": "CHANGED",
        },
        "recovery_status": "RECOVERED_FROM_CHECKPOINT",
        "continuation_status": "READY_TO_CONTINUE",
    }
    persistence["recovery_events"].append(event)
    return event


def dna07_persistent_existence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Preserve the goal after an initial failure, save an in-context
    checkpoint, require a changed strategy, recover, and continue.

    This core does not create Memory Runtime, learn, invoke a model,
    execute F174, perform external action, or modify Canon.
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
    trace.append("DNA-07")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, dna06_output = _validate_dependencies(
        context
    )
    persistence = _install_persistence_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)
    detected = _failure_detected(dna06_output)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-07",
            "operation": (
                "PERSISTENT_EXISTENCE_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "persistence_schema": PERSISTENCE_SCHEMA,
            "memory_runtime_used": False,
        }
    )

    checkpoint: Optional[Dict[str, Any]] = None
    recovery_event: Optional[Dict[str, Any]] = None

    if detected:
        feedback_event = _latest_feedback_event(state)
        goal = _resolve_goal(context, persistence)
        current_strategy = _resolve_strategy(
            context,
            persistence,
        )
        checkpoint = _save_checkpoint(
            context,
            state,
            persistence,
            feedback_event,
            goal,
            current_strategy,
        )
        recovery_event = _recover_and_continue(
            context,
            persistence,
            checkpoint,
            goal,
            current_strategy,
        )

        state["provenance"].append(
            {
                "sequence": (
                    len(state["provenance"]) + 1
                ),
                "core_id": "DNA-07",
                "operation": (
                    "CHECKPOINT_SAVED_STRATEGY_CHANGED_"
                    "RECOVERY_CONTINUATION_EVALUATED"
                ),
                "canonical_sha256": canonical_sha256,
                "checkpoint_id": (
                    checkpoint["checkpoint_id"]
                ),
                "goal_preserved": (
                    recovery_event["goal_preserved"]
                ),
                "strategy_change_status": (
                    recovery_event[
                        "strategy_change"
                    ]["status"]
                ),
                "recovery_status": (
                    recovery_event["recovery_status"]
                ),
                "continuation_status": (
                    recovery_event[
                        "continuation_status"
                    ]
                ),
            }
        )

    outputs["DNA-07"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "persistence_contract": deepcopy(
            PERSISTENT_EXISTENCE_CONTRACT
        ),
        "failure_detected": detected,
        "checkpoint": deepcopy(checkpoint),
        "recovery_event": deepcopy(recovery_event),
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna07(core54: Core54Like) -> None:
    core = core54.get("DNA-07")
    assert_exact_canon(core)
    core54.bind(
        "DNA-07",
        dna07_persistent_existence,
    )


def self_check_dna07(
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
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna07_core = core54.get("DNA-07")
    assert_exact_canon(dna07_core)
    bind_dna07(core54)

    probe = {
        "trace": [],
        "caller_data": {"preserve": True},
        "goal": {
            "id": "GOAL-01",
            "statement": "continue verified inquiry",
        },
        "strategy": "STRATEGY-A",
        "next_strategy": "STRATEGY-B",
        "failure": {
            "detected": True,
            "layer": "verification",
            "recovery_operation": "REFRAME",
            "reason": "FIRST_APPROACH_FAILED",
        },
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {
                "subject": "DNA-07_SELF_CHECK",
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
                    "NEW_STRATEGY_REQUIRES_VERIFICATION"
                ],
            },
        },
    }
    snapshot = deepcopy(probe)

    result = probe
    for core_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
    ):
        result = core54.get(core_id).activate(result)

    assert probe == snapshot
    assert result["trace"] == [
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
    ]

    dna07 = result["core54_outputs"]["DNA-07"]
    assert dna07["canonical_gene"] == CANON_DNA07
    assert (
        dna07["persistence_contract"]
        == PERSISTENT_EXISTENCE_CONTRACT
    )
    assert dna07["failure_detected"] is True
    assert dna07["status"] == "CANON_ALIGNED"

    checkpoint = dna07["checkpoint"]
    assert checkpoint["sequence"] == 1
    assert checkpoint["checkpoint_id"] == (
        "DNA-07-CP-0001"
    )
    assert checkpoint["goal"] == probe["goal"]
    assert checkpoint["strategy"] == "STRATEGY-A"
    assert checkpoint["status"] == "SAVED"
    assert (
        checkpoint["storage_scope"]
        == "CURRENT_STRUCTURED_STATE"
    )
    assert checkpoint["memory_runtime_used"] is False

    recovery = dna07["recovery_event"]
    assert recovery == {
        "sequence": 1,
        "failure_sequence": 1,
        "first_failure": True,
        "checkpoint_id": "DNA-07-CP-0001",
        "goal_preserved": True,
        "goal_abandoned": False,
        "strategy_change": {
            "from": "STRATEGY-A",
            "to": "STRATEGY-B",
            "status": "CHANGED",
        },
        "recovery_status": "RECOVERED_FROM_CHECKPOINT",
        "continuation_status": "READY_TO_CONTINUE",
    }

    state = result["cognitive_state"]
    persistence = state["persistent_existence"]
    assert (
        persistence["contract"]
        == PERSISTENT_EXISTENCE_CONTRACT
    )
    assert persistence["active_goal"] == probe["goal"]
    assert persistence["active_strategy"] == (
        "STRATEGY-B"
    )
    assert persistence["checkpoints"] == [checkpoint]
    assert persistence["recovery_events"] == [recovery]
    assert len(state["provenance"]) == 8

    contract_event = state["provenance"][-2]
    assert contract_event["sequence"] == 7
    assert contract_event["core_id"] == "DNA-07"
    assert contract_event["operation"] == (
        "PERSISTENT_EXISTENCE_CONTRACT_ESTABLISHED"
    )
    assert contract_event["memory_runtime_used"] is False

    transition_event = state["provenance"][-1]
    assert transition_event["sequence"] == 8
    assert transition_event["core_id"] == "DNA-07"
    assert transition_event["checkpoint_id"] == (
        "DNA-07-CP-0001"
    )
    assert transition_event["goal_preserved"] is True
    assert transition_event["strategy_change_status"] == (
        "CHANGED"
    )
    assert transition_event["recovery_status"] == (
        "RECOVERED_FROM_CHECKPOINT"
    )
    assert transition_event["continuation_status"] == (
        "READY_TO_CONTINUE"
    )

    # Missing next strategy preserves the goal and checkpoint, but does not
    # invent a strategy.
    pending_input = deepcopy(result)
    pending_input["failure"] = {
        "detected": True,
        "layer": "verification",
        "recovery_operation": "RETRY",
        "reason": "SECOND_APPROACH_FAILED",
    }
    pending_input["strategy"] = "STRATEGY-B"
    pending_input.pop("next_strategy", None)
    pending = core54.get("DNA-06").activate(
        pending_input
    )
    pending = dna07_core.activate(pending)

    pending_recovery = pending[
        "core54_outputs"
    ]["DNA-07"]["recovery_event"]
    assert pending_recovery["failure_sequence"] == 2
    assert pending_recovery["goal_preserved"] is True
    assert pending_recovery["goal_abandoned"] is False
    assert pending_recovery["strategy_change"] == {
        "from": "STRATEGY-B",
        "to": None,
        "status": "SELECTION_REQUIRED",
    }
    assert pending_recovery["recovery_status"] == (
        "WAITING_FOR_CHANGED_STRATEGY"
    )
    assert pending_recovery["continuation_status"] == (
        "PAUSED_NOT_ABANDONED"
    )

    # A claimed new strategy must actually differ.
    same_strategy_input = deepcopy(result)
    same_strategy_input["failure"] = {
        "detected": True,
        "layer": "verification",
        "recovery_operation": "RETRY",
    }
    same_strategy_input["strategy"] = "STRATEGY-B"
    same_strategy_input["next_strategy"] = "STRATEGY-B"
    same_strategy_input = core54.get("DNA-06").activate(
        same_strategy_input
    )
    try:
        dna07_core.activate(same_strategy_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-07_NEXT_STRATEGY_MUST_DIFFER"
        )
    else:
        raise AssertionError(
            "DNA-07_ACCEPTED_UNCHANGED_STRATEGY"
        )

    # Failure cannot bypass DNA-06 feedback.
    try:
        dna07_core.activate(
            {
                "trace": [],
                "core54_outputs": {
                    "DNA-06": {
                        "failure_detected": True,
                    }
                },
                "goal": "G",
                "strategy": "A",
                "next_strategy": "B",
                "cognitive_state": {
                    "schema": UNIFIED_STATE_SCHEMA,
                    "content": {},
                    "provenance": [],
                    "uncertainty": {},
                },
            }
        )
    except RuntimeError as exc:
        assert str(exc) == (
            "DNA-06_INTERLAYER_FEEDBACK_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-07_ACCEPTED_MISSING_FEEDBACK_STATE"
        )

    # No failure creates no checkpoint or recovery transition.
    no_failure_input = deepcopy(result)
    no_failure_input["failure"] = False
    no_failure_input.pop("next_strategy", None)
    no_failure_input = core54.get("DNA-06").activate(
        no_failure_input
    )
    no_failure = dna07_core.activate(
        no_failure_input
    )
    no_failure_output = no_failure[
        "core54_outputs"
    ]["DNA-07"]
    assert no_failure_output["failure_detected"] is False
    assert no_failure_output["checkpoint"] is None
    assert no_failure_output["recovery_event"] is None

    # Reject old provisional marker contracts.
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result
    assert "persist_goal" not in result

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
        "core_id": "DNA-07",
        "canon_mapping": "PASS",
        "checkpoint": "PASS",
        "strategy_change": "PASS",
        "recovery": "PASS",
        "continuation": "PASS",
        "goal_preserved": "PASS",
        "memory_runtime_used": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-08"
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
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-07_FAIL: REQUIRED_PATH_NOT_FOUND")
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
    except Exception as exc:
        print("DNA-07_FAIL: IMPORT_ERROR")
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
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna07(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != [
            "DNA-01",
            "DNA-02",
            "DNA-03",
            "DNA-04",
            "DNA-05",
            "DNA-06",
            "DNA-07",
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-07_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-07_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_07_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("CHECKPOINT:", report["checkpoint"])
    print("STRATEGY_CHANGE:", report["strategy_change"])
    print("RECOVERY:", report["recovery"])
    print("CONTINUATION:", report["continuation"])
    print("GOAL_PRESERVED:", report["goal_preserved"])
    print(
        "MEMORY_RUNTIME_USED:",
        report["memory_runtime_used"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 7/54")
    print("NEXT_AUTHORIZED: DNA-08")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
