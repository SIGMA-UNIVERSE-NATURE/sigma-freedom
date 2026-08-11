#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-08: LEARNING WORLD
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_08_LEARNING_WORLD.py
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

CANON_DNA08: Dict[str, str] = {
    "id": "DNA-08",
    "name": "Learning World",
    "purpose": (
        "SIGMA học qua môi trường, hành động, hậu quả và trải nghiệm; "
        "không chỉ qua câu trả lời có sẵn."
    ),
    "system": "learning",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
LEARNING_WORLD_SCHEMA = "SIGMA_LEARNING_WORLD_V1"

WORLD_EVENT_COMPONENTS = [
    "environment",
    "action",
    "consequence",
    "experience",
]

LEARNING_WORLD_CONTRACT: Dict[str, Any] = {
    "schema": LEARNING_WORLD_SCHEMA,
    "learning_basis": deepcopy(WORLD_EVENT_COMPONENTS),
    "ready_made_answer_alone_sufficient": False,
    "complete_event_requires_all_components": True,
    "event_is_verified_knowledge": False,
    "knowledge_promotion_authority": False,
    "learning_runtime_started": False,
    "world_runtime_started": False,
    "external_action_executed": False,
    "capture_scope": "CURRENT_STRUCTURED_STATE",
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
    if actual != CANON_DNA08:
        raise RuntimeError(
            "DNA-08_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA08, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_unified_state(
    context: Dict[str, Any],
) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-08_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("content"), dict):
        raise TypeError(
            "context['cognitive_state']['content'] must be a dict"
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


def _install_learning_world_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("learning_world")

    expected = {
        "contract": deepcopy(LEARNING_WORLD_CONTRACT),
        "events": [],
    }

    if existing is None:
        state["learning_world"] = expected
        return state["learning_world"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['learning_world'] must be a dict"
        )

    if existing.get("contract") != LEARNING_WORLD_CONTRACT:
        raise ValueError(
            "DNA-08_LEARNING_WORLD_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("events"), list):
        raise TypeError(
            "learning_world['events'] must be a list"
        )

    return existing


def _component_presence(
    context: Dict[str, Any],
) -> Dict[str, bool]:
    return {
        key: key in context and context[key] is not None
        for key in WORLD_EVENT_COMPONENTS
    }


def _qualify_world_event(
    context: Dict[str, Any],
    learning_world: Dict[str, Any],
) -> tuple[
    Optional[Dict[str, Any]],
    List[str],
    Optional[str],
]:
    presence = _component_presence(context)
    present_count = sum(presence.values())
    missing = [
        key
        for key, present in presence.items()
        if not present
    ]

    answer_present = (
        ("answer" in context and context["answer"] is not None)
        or (
            "ready_made_answer" in context
            and context["ready_made_answer"] is not None
        )
    )

    if present_count == 0:
        reason = (
            "READY_MADE_ANSWER_ALONE_INSUFFICIENT"
            if answer_present
            else "NO_WORLD_INTERACTION_SUPPLIED"
        )
        return None, missing, reason

    if missing:
        return (
            None,
            missing,
            "INCOMPLETE_WORLD_INTERACTION",
        )

    interaction = {
        key: deepcopy(context[key])
        for key in WORLD_EVENT_COMPONENTS
    }
    sequence = len(learning_world["events"]) + 1
    event = {
        "sequence": sequence,
        "event_id": f"DNA-08-WORLD-{sequence:04d}",
        "environment": interaction["environment"],
        "action": interaction["action"],
        "consequence": interaction["consequence"],
        "experience": interaction["experience"],
        "interaction_sha256": _sha256_json(interaction),
        "ready_made_answer_only": False,
        "complete": True,
        "verified_knowledge": False,
        "learning_runtime_used": False,
        "world_runtime_used": False,
        "external_action_executed_by_dna08": False,
        "status": "EXPERIENTIAL_EVENT_QUALIFIED",
    }
    learning_world["events"].append(event)
    return event, [], None


def dna08_learning_world(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Qualify an experiential world-learning event from the exact Canon
    components: environment, action, consequence, and experience.

    DNA-08 captures supplied interaction evidence only. It does not execute
    an action, start Learning/World Runtime, promote knowledge, invoke a
    model, auto-learn, execute F174, or modify Canon.
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
    trace.append("DNA-08")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_unified_state(context)
    learning_world = _install_learning_world_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-08",
            "operation": "LEARNING_WORLD_CONTRACT_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "learning_world_schema": LEARNING_WORLD_SCHEMA,
            "learning_runtime_started": False,
            "world_runtime_started": False,
        }
    )

    event, missing, insufficiency_reason = (
        _qualify_world_event(
            context,
            learning_world,
        )
    )

    if event is not None:
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-08",
                "operation": "EXPERIENTIAL_EVENT_QUALIFIED",
                "canonical_sha256": canonical_sha256,
                "event_id": event["event_id"],
                "interaction_sha256": (
                    event["interaction_sha256"]
                ),
                "knowledge_promoted": False,
            }
        )

    outputs["DNA-08"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "learning_world_contract": deepcopy(
            LEARNING_WORLD_CONTRACT
        ),
        "world_event_complete": event is not None,
        "world_event": deepcopy(event),
        "missing_components": deepcopy(missing),
        "insufficiency_reason": insufficiency_reason,
        "knowledge_promoted": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna08(core54: Core54Like) -> None:
    core = core54.get("DNA-08")
    assert_exact_canon(core)
    core54.bind(
        "DNA-08",
        dna08_learning_world,
    )


def self_check_dna08(
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
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna08_core = core54.get("DNA-08")
    assert_exact_canon(dna08_core)
    bind_dna08(core54)

    probe = {
        "trace": [],
        "caller_data": {"preserve": True},
        "environment": {
            "id": "WORLD-SELF-CHECK",
            "state": "INITIAL",
        },
        "action": {
            "id": "ACTION-01",
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
                "subject": "DNA-08_SELF_CHECK",
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
                    "EVENT_NOT_INDEPENDENTLY_VERIFIED"
                ],
            },
        },
    }
    snapshot = deepcopy(probe)

    result = probe
    pre_dna08: Optional[Dict[str, Any]] = None
    for core_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
    ):
        if core_id == "DNA-08":
            pre_dna08 = deepcopy(result)
        result = core54.get(core_id).activate(result)

    assert pre_dna08 is not None
    assert probe == snapshot
    assert result["trace"] == [
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
    ]

    dna08 = result["core54_outputs"]["DNA-08"]
    assert dna08["canonical_gene"] == CANON_DNA08
    assert (
        dna08["learning_world_contract"]
        == LEARNING_WORLD_CONTRACT
    )
    assert dna08["world_event_complete"] is True
    assert dna08["missing_components"] == []
    assert dna08["insufficiency_reason"] is None
    assert dna08["knowledge_promoted"] is False
    assert dna08["status"] == "CANON_ALIGNED"

    event = dna08["world_event"]
    assert event["sequence"] == 1
    assert event["event_id"] == "DNA-08-WORLD-0001"
    assert event["environment"] == probe["environment"]
    assert event["action"] == probe["action"]
    assert event["consequence"] == probe["consequence"]
    assert event["experience"] == probe["experience"]
    assert event["ready_made_answer_only"] is False
    assert event["complete"] is True
    assert event["verified_knowledge"] is False
    assert event["learning_runtime_used"] is False
    assert event["world_runtime_used"] is False
    assert (
        event["external_action_executed_by_dna08"]
        is False
    )
    assert event["status"] == (
        "EXPERIENTIAL_EVENT_QUALIFIED"
    )

    state = result["cognitive_state"]
    learning_world = state["learning_world"]
    assert (
        learning_world["contract"]
        == LEARNING_WORLD_CONTRACT
    )
    assert learning_world["events"] == [event]
    assert len(state["provenance"]) == 8

    contract_event = state["provenance"][-2]
    assert contract_event["sequence"] == 7
    assert contract_event["core_id"] == "DNA-08"
    assert contract_event["operation"] == (
        "LEARNING_WORLD_CONTRACT_ESTABLISHED"
    )
    assert (
        contract_event["learning_world_schema"]
        == LEARNING_WORLD_SCHEMA
    )
    assert (
        contract_event["learning_runtime_started"]
        is False
    )
    assert contract_event["world_runtime_started"] is False

    qualified_event = state["provenance"][-1]
    assert qualified_event["sequence"] == 8
    assert qualified_event["core_id"] == "DNA-08"
    assert qualified_event["operation"] == (
        "EXPERIENTIAL_EVENT_QUALIFIED"
    )
    assert qualified_event["event_id"] == (
        "DNA-08-WORLD-0001"
    )
    assert qualified_event["knowledge_promoted"] is False
    assert qualified_event["interaction_sha256"] == (
        event["interaction_sha256"]
    )

    # A ready-made answer alone must not become a world-learning event.
    answer_only_input = deepcopy(pre_dna08)
    for key in WORLD_EVENT_COMPONENTS:
        answer_only_input.pop(key, None)
    answer_only_input["answer"] = "READY_MADE_ANSWER"

    answer_only = dna08_core.activate(answer_only_input)
    answer_only_output = answer_only[
        "core54_outputs"
    ]["DNA-08"]
    assert (
        answer_only_output["world_event_complete"]
        is False
    )
    assert answer_only_output["world_event"] is None
    assert answer_only_output["missing_components"] == (
        WORLD_EVENT_COMPONENTS
    )
    assert answer_only_output["insufficiency_reason"] == (
        "READY_MADE_ANSWER_ALONE_INSUFFICIENT"
    )
    assert answer_only[
        "cognitive_state"
    ]["learning_world"]["events"] == []

    # Partial interaction must not be claimed complete.
    partial_input = deepcopy(pre_dna08)
    for key in WORLD_EVENT_COMPONENTS:
        partial_input.pop(key, None)
    partial_input["environment"] = {"id": "WORLD-PARTIAL"}
    partial_input["action"] = {"id": "ACTION-PARTIAL"}

    partial = dna08_core.activate(partial_input)
    partial_output = partial[
        "core54_outputs"
    ]["DNA-08"]
    assert partial_output["world_event_complete"] is False
    assert partial_output["world_event"] is None
    assert partial_output["missing_components"] == [
        "consequence",
        "experience",
    ]
    assert partial_output["insufficiency_reason"] == (
        "INCOMPLETE_WORLD_INTERACTION"
    )

    # Reject the provisional marker contract.
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result
    assert "world_learning_event_complete" not in result

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
        "core_id": "DNA-08",
        "canon_mapping": "PASS",
        "learning_world_contract": "PASS",
        "experiential_event": "PASS",
        "answer_only_rejected": "PASS",
        "knowledge_promoted": False,
        "learning_runtime_used": False,
        "world_runtime_used": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-09"
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
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-08_FAIL: REQUIRED_PATH_NOT_FOUND")
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
    except Exception as exc:
        print("DNA-08_FAIL: IMPORT_ERROR")
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
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna08(
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
            "DNA-08",
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-08_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-08_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_08_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "LEARNING_WORLD_CONTRACT:",
        report["learning_world_contract"],
    )
    print(
        "EXPERIENTIAL_EVENT:",
        report["experiential_event"],
    )
    print(
        "ANSWER_ONLY_REJECTED:",
        report["answer_only_rejected"],
    )
    print(
        "KNOWLEDGE_PROMOTED:",
        report["knowledge_promoted"],
    )
    print(
        "LEARNING_RUNTIME_USED:",
        report["learning_runtime_used"],
    )
    print(
        "WORLD_RUNTIME_USED:",
        report["world_runtime_used"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 8/54")
    print("NEXT_AUTHORIZED: DNA-09")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
