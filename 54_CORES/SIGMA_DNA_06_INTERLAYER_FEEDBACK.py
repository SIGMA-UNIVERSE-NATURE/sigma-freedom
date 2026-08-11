#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-06: INTERLAYER FEEDBACK
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_06_INTERLAYER_FEEDBACK.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol


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

CANON_DNA06: Dict[str, str] = {
    "id": "DNA-06",
    "name": "Interlayer Feedback",
    "purpose": (
        "Nhận thức là mạng hồi tiếp, không pipeline một chiều; "
        "failure phải kích hoạt reframe/retry thích hợp."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
LAYER_SCHEMA = "SIGMA_EIGHT_COGNITIVE_LAYERS_V1"
ETHICAL_SCHEMA = "SIGMA_ETHICAL_INTELLIGENCE_V1"
FEEDBACK_SCHEMA = "SIGMA_INTERLAYER_FEEDBACK_V1"

EXPECTED_LAYER_KEYS = [
    "perception",
    "meaning",
    "critical_reasoning",
    "discovery",
    "verification",
    "ethics",
    "feedback",
    "lifecycle",
]

RECOVERY_OPERATIONS = [
    "REFRAME",
    "RETRY",
]

INTERLAYER_FEEDBACK_CONTRACT: Dict[str, Any] = {
    "schema": FEEDBACK_SCHEMA,
    "architecture": "FEEDBACK_NETWORK",
    "one_way_pipeline": False,
    "layer_count": 8,
    "layer_keys": deepcopy(EXPECTED_LAYER_KEYS),
    "feedback_layer": "feedback",
    "failure_rule": {
        "trigger_required": True,
        "allowed_recovery_operations": deepcopy(
            RECOVERY_OPERATIONS
        ),
        "selection_basis": "FAILURE_CONTEXT",
    },
    "execution_authority": False,
    "runtime_processing_started": False,
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
    if actual != CANON_DNA06:
        raise RuntimeError(
            "DNA-06_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA06, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _failure_detected(context: Dict[str, Any]) -> bool:
    failure = context.get("failure", False)

    if isinstance(failure, bool):
        return failure

    if isinstance(failure, dict):
        detected = failure.get("detected", True)
        if not isinstance(detected, bool):
            raise TypeError(
                "context['failure']['detected'] must be a bool"
            )
        return detected

    raise TypeError(
        "context['failure'] must be a bool or dict when supplied"
    )


def _failure_layer(
    context: Dict[str, Any],
    layer_keys: List[str],
) -> Optional[str]:
    failure = context.get("failure")
    value: Any = None

    if isinstance(failure, dict):
        value = failure.get("layer")

    if value is None:
        value = context.get("failure_layer")

    if value is None:
        return None

    if not isinstance(value, str):
        raise TypeError("failure layer must be a string")

    if value not in layer_keys:
        raise ValueError(
            f"DNA-06_UNKNOWN_FAILURE_LAYER:{value}"
        )

    return value


def _requested_recovery_operation(
    context: Dict[str, Any],
) -> Optional[str]:
    failure = context.get("failure")
    value: Any = None

    if isinstance(failure, dict):
        value = failure.get("recovery_operation")

    if value is None:
        value = context.get("recovery_operation")

    if value is None:
        return None

    if not isinstance(value, str):
        raise TypeError(
            "recovery_operation must be a string"
        )

    normalized = value.strip().upper()
    if normalized not in RECOVERY_OPERATIONS:
        raise ValueError(
            "DNA-06_RECOVERY_OPERATION_MUST_BE_REFRAME_OR_RETRY"
        )

    return normalized


def _validate_required_state(
    context: Dict[str, Any],
) -> tuple[Dict[str, Any], List[str]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-06_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    layers = state.get("cognitive_layers")
    if not isinstance(layers, dict):
        raise RuntimeError(
            "DNA-04_EIGHT_COGNITIVE_LAYERS_REQUIRED"
        )

    if layers.get("schema") != LAYER_SCHEMA:
        raise ValueError(
            "DNA-06_COGNITIVE_LAYER_SCHEMA_MISMATCH:"
            f"{layers.get('schema')!r}"
        )

    layer_items = layers.get("layers")
    if not isinstance(layer_items, list):
        raise TypeError(
            "context['cognitive_state']['cognitive_layers']"
            "['layers'] must be a list"
        )

    layer_keys = [
        item.get("key")
        for item in layer_items
        if isinstance(item, dict)
    ]
    if layer_keys != EXPECTED_LAYER_KEYS:
        raise RuntimeError(
            "DNA-06_EXACT_EIGHT_LAYER_ORDER_REQUIRED"
        )

    ethical = state.get("ethical_intelligence")
    if not isinstance(ethical, dict):
        raise RuntimeError(
            "DNA-05_ETHICAL_INTELLIGENCE_REQUIRED"
        )

    if ethical.get("schema") != ETHICAL_SCHEMA:
        raise ValueError(
            "DNA-06_ETHICAL_SCHEMA_MISMATCH:"
            f"{ethical.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    return state, layer_keys


def _install_feedback_network(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("interlayer_feedback")

    expected = {
        "contract": deepcopy(
            INTERLAYER_FEEDBACK_CONTRACT
        ),
        "events": [],
    }

    if existing is None:
        state["interlayer_feedback"] = expected
        return state["interlayer_feedback"]

    if not isinstance(existing, dict):
        raise TypeError(
            "context['cognitive_state']['interlayer_feedback'] "
            "must be a dict"
        )

    if existing.get("contract") != (
        INTERLAYER_FEEDBACK_CONTRACT
    ):
        raise ValueError(
            "DNA-06_FEEDBACK_CONTRACT_CONFLICT"
        )

    events = existing.get("events")
    if not isinstance(events, list):
        raise TypeError(
            "interlayer_feedback['events'] must be a list"
        )

    return existing


def _activate_failure_feedback(
    context: Dict[str, Any],
    feedback_state: Dict[str, Any],
    layer_keys: List[str],
) -> Optional[Dict[str, Any]]:
    if not _failure_detected(context):
        return None

    source_layer = _failure_layer(
        context,
        layer_keys,
    )
    selected_operation = (
        _requested_recovery_operation(context)
    )

    event = {
        "sequence": len(feedback_state["events"]) + 1,
        "trigger": "FAILURE",
        "source_layer": source_layer,
        "route_type": "INTERLAYER_FEEDBACK",
        "mediated_by": "feedback",
        "allowed_recovery_operations": deepcopy(
            RECOVERY_OPERATIONS
        ),
        "selected_recovery_operation": (
            selected_operation
        ),
        "selection_status": (
            "SELECTED_FROM_FAILURE_CONTEXT"
            if selected_operation is not None
            else "CONTEXTUAL_SELECTION_REQUIRED"
        ),
        "status": "ACTIVATED",
    }
    feedback_state["events"].append(event)
    return event


def dna06_interlayer_feedback(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Establish cognition as an interlayer feedback network.

    When failure is present, activate a feedback event requiring an
    appropriate REFRAME or RETRY selection. DNA-06 does not execute either
    operation, start a higher runtime, invoke a model, learn, write Memory
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
    trace.append("DNA-06")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, layer_keys = _validate_required_state(
        context
    )
    feedback_state = _install_feedback_network(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-06",
            "operation": (
                "INTERLAYER_FEEDBACK_NETWORK_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "feedback_schema": FEEDBACK_SCHEMA,
            "one_way_pipeline": False,
        }
    )

    feedback_event = _activate_failure_feedback(
        context,
        feedback_state,
        layer_keys,
    )

    if feedback_event is not None:
        state["provenance"].append(
            {
                "sequence": (
                    len(state["provenance"]) + 1
                ),
                "core_id": "DNA-06",
                "operation": (
                    "FAILURE_FEEDBACK_ACTIVATED"
                ),
                "canonical_sha256": canonical_sha256,
                "feedback_event_sequence": (
                    feedback_event["sequence"]
                ),
                "selection_status": (
                    feedback_event["selection_status"]
                ),
            }
        )

    outputs["DNA-06"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "feedback_contract": deepcopy(
            INTERLAYER_FEEDBACK_CONTRACT
        ),
        "failure_detected": (
            feedback_event is not None
        ),
        "feedback_event": deepcopy(feedback_event),
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna06(core54: Core54Like) -> None:
    core = core54.get("DNA-06")
    assert_exact_canon(core)
    core54.bind(
        "DNA-06",
        dna06_interlayer_feedback,
    )


def self_check_dna06(
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
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna06_core = core54.get("DNA-06")
    assert_exact_canon(dna06_core)
    bind_dna06(core54)

    probe = {
        "trace": [],
        "caller_data": {"preserve": True},
        "failure": {
            "detected": True,
            "layer": "verification",
            "recovery_operation": "REFRAME",
        },
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {
                "subject": "DNA-06_SELF_CHECK",
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
                    "FAILED_HYPOTHESIS_REQUIRES_FEEDBACK"
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
    ]

    dna06 = result["core54_outputs"]["DNA-06"]
    assert dna06["canonical_gene"] == CANON_DNA06
    assert (
        dna06["feedback_contract"]
        == INTERLAYER_FEEDBACK_CONTRACT
    )
    assert dna06["failure_detected"] is True
    assert dna06["status"] == "CANON_ALIGNED"

    event = dna06["feedback_event"]
    assert event == {
        "sequence": 1,
        "trigger": "FAILURE",
        "source_layer": "verification",
        "route_type": "INTERLAYER_FEEDBACK",
        "mediated_by": "feedback",
        "allowed_recovery_operations": [
            "REFRAME",
            "RETRY",
        ],
        "selected_recovery_operation": "REFRAME",
        "selection_status": (
            "SELECTED_FROM_FAILURE_CONTEXT"
        ),
        "status": "ACTIVATED",
    }

    state = result["cognitive_state"]
    assert state["schema"] == UNIFIED_STATE_SCHEMA
    assert state["content"] == {
        "subject": "DNA-06_SELF_CHECK",
    }
    assert state["uncertainty"] == {
        "open_items": [
            "FAILED_HYPOTHESIS_REQUIRES_FEEDBACK"
        ],
    }

    feedback = state["interlayer_feedback"]
    assert (
        feedback["contract"]
        == INTERLAYER_FEEDBACK_CONTRACT
    )
    assert feedback["events"] == [event]
    assert (
        feedback["contract"]["architecture"]
        == "FEEDBACK_NETWORK"
    )
    assert (
        feedback["contract"]["one_way_pipeline"]
        is False
    )
    assert feedback["contract"]["layer_count"] == 8
    assert (
        feedback["contract"]["layer_keys"]
        == EXPECTED_LAYER_KEYS
    )
    assert len(state["provenance"]) == 6

    network_event = state["provenance"][-2]
    assert network_event["sequence"] == 5
    assert network_event["core_id"] == "DNA-06"
    assert network_event["operation"] == (
        "INTERLAYER_FEEDBACK_NETWORK_ESTABLISHED"
    )
    assert network_event["feedback_schema"] == (
        FEEDBACK_SCHEMA
    )
    assert network_event["one_way_pipeline"] is False

    failure_event = state["provenance"][-1]
    assert failure_event["sequence"] == 6
    assert failure_event["core_id"] == "DNA-06"
    assert failure_event["operation"] == (
        "FAILURE_FEEDBACK_ACTIVATED"
    )
    assert (
        failure_event["feedback_event_sequence"]
        == 1
    )
    assert failure_event["selection_status"] == (
        "SELECTED_FROM_FAILURE_CONTEXT"
    )
    assert (
        network_event["canonical_sha256"]
        == dna06["canonical_sha256"]
    )
    assert (
        failure_event["canonical_sha256"]
        == dna06["canonical_sha256"]
    )

    # Failure without enough context must still activate the required
    # REFRAME/RETRY choice, but must not invent a selection.
    contextual = dna06_core.activate(
        {
            "trace": [],
            "core54_outputs": {},
            "failure": True,
            "cognitive_state": {
                "schema": UNIFIED_STATE_SCHEMA,
                "content": {},
                "provenance": [],
                "uncertainty": {},
                "cognitive_layers": deepcopy(
                    state["cognitive_layers"]
                ),
                "ethical_intelligence": deepcopy(
                    state["ethical_intelligence"]
                ),
            },
        }
    )
    contextual_event = contextual[
        "core54_outputs"
    ]["DNA-06"]["feedback_event"]
    assert contextual_event["status"] == "ACTIVATED"
    assert (
        contextual_event["selected_recovery_operation"]
        is None
    )
    assert contextual_event["selection_status"] == (
        "CONTEXTUAL_SELECTION_REQUIRED"
    )

    # No failure means no recovery event.
    no_failure = dna06_core.activate(
        {
            "trace": [],
            "core54_outputs": {},
            "cognitive_state": {
                "schema": UNIFIED_STATE_SCHEMA,
                "content": {},
                "provenance": [],
                "uncertainty": {},
                "cognitive_layers": deepcopy(
                    state["cognitive_layers"]
                ),
                "ethical_intelligence": deepcopy(
                    state["ethical_intelligence"]
                ),
            },
        }
    )
    no_failure_output = no_failure[
        "core54_outputs"
    ]["DNA-06"]
    assert no_failure_output["failure_detected"] is False
    assert no_failure_output["feedback_event"] is None
    assert no_failure[
        "cognitive_state"
    ]["interlayer_feedback"]["events"] == []

    # DNA-06 must not bypass the exact eight-layer state.
    try:
        dna06_core.activate(
            {
                "trace": [],
                "core54_outputs": {},
                "failure": True,
                "cognitive_state": {
                    "schema": UNIFIED_STATE_SCHEMA,
                    "content": {},
                    "provenance": [],
                    "uncertainty": {},
                    "ethical_intelligence": deepcopy(
                        state["ethical_intelligence"]
                    ),
                },
            }
        )
    except RuntimeError as exc:
        assert str(exc) == (
            "DNA-04_EIGHT_COGNITIVE_LAYERS_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-06_ACCEPTED_MISSING_COGNITIVE_LAYERS"
        )

    # Reject a recovery choice outside the exact Canon pair.
    try:
        dna06_core.activate(
            {
                "trace": [],
                "core54_outputs": {},
                "failure": {
                    "detected": True,
                    "recovery_operation": "ABANDON",
                },
                "cognitive_state": {
                    "schema": UNIFIED_STATE_SCHEMA,
                    "content": {},
                    "provenance": [],
                    "uncertainty": {},
                    "cognitive_layers": deepcopy(
                        state["cognitive_layers"]
                    ),
                    "ethical_intelligence": deepcopy(
                        state["ethical_intelligence"]
                    ),
                },
            }
        )
    except ValueError as exc:
        assert str(exc) == (
            "DNA-06_RECOVERY_OPERATION_MUST_BE_"
            "REFRAME_OR_RETRY"
        )
    else:
        raise AssertionError(
            "DNA-06_ACCEPTED_NON_CANON_RECOVERY_OPERATION"
        )

    # Reject provisional markers as the official Canon contract.
    assert "feedback_route" not in result
    assert "requests" not in result
    assert "flags" not in result
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
        "core_id": "DNA-06",
        "canon_mapping": "PASS",
        "feedback_network": "PASS",
        "one_way_pipeline": False,
        "failure_reframe_retry": "PASS",
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-07"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    required_gene_files = [
        (
            GENES_ROOT
            / "SIGMA_DNA_01_PURPOSE_EXISTENCE.py"
        ),
        (
            GENES_ROOT
            / "SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE.py"
        ),
        (
            GENES_ROOT
            / "SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE.py"
        ),
        (
            GENES_ROOT
            / "SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS.py"
        ),
        (
            GENES_ROOT
            / "SIGMA_DNA_05_ETHICAL_INTELLIGENCE.py"
        ),
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-06_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )
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
    except Exception as exc:
        print("DNA-06_FAIL: IMPORT_ERROR")
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

        prior_checks = (
            ("DNA-01", self_check_dna01),
            ("DNA-02", self_check_dna02),
            ("DNA-03", self_check_dna03),
            ("DNA-04", self_check_dna04),
            ("DNA-05", self_check_dna05),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(
                    f"{core_id}_NOT_PASS"
                )

        report = self_check_dna06(
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
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-06_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-06_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_06_PASS")
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "FEEDBACK_NETWORK:",
        report["feedback_network"],
    )
    print(
        "ONE_WAY_PIPELINE:",
        report["one_way_pipeline"],
    )
    print(
        "FAILURE_REFRAME_RETRY:",
        report["failure_reframe_retry"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print(
        "PHASE_LOCKS:",
        report["phase_locks"],
    )
    print("OFFICIAL_BOUND_CORES: 6/54")
    print("NEXT_AUTHORIZED: DNA-07")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
