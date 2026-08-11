#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-03: UNIFIED COGNITIVE STATE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Protocol


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

CANON_DNA03: Dict[str, str] = {
    "id": "DNA-03",
    "name": "Unified Cognitive State",
    "purpose": (
        "Mọi lớp nhận thức cùng làm việc trên một trạng thái có cấu trúc, "
        "truy nguyên được và mang uncertainty."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_PROFILE: Dict[str, Any] = {
    "state_path": "cognitive_state",
    "single_shared_state": True,
    "shared_by_all_cognitive_layers": True,
    "structured_state_required": True,
    "traceability_required": True,
    "uncertainty_carried": True,
    "cognitive_layers_instantiated_in_dna03": False,
    "memory_runtime_started_in_dna03": False,
    "learning_runtime_started_in_dna03": False,
    "derivation": "DIRECT_FROM_CANON_PURPOSE",
}

STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"


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
    if actual != CANON_DNA03:
        raise RuntimeError(
            "DNA-03_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA03, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _ensure_unified_state(
    context: Dict[str, Any],
    *,
    canonical_sha256: str,
) -> Dict[str, Any]:
    state = context.setdefault("cognitive_state", {})
    if not isinstance(state, dict):
        raise TypeError("context['cognitive_state'] must be a dict")

    schema = state.setdefault("schema", STATE_SCHEMA)
    if schema != STATE_SCHEMA:
        raise ValueError(
            f"DNA-03_STATE_SCHEMA_MISMATCH:{schema!r}"
        )

    content = state.setdefault("content", {})
    if not isinstance(content, dict):
        raise TypeError(
            "context['cognitive_state']['content'] must be a dict"
        )

    provenance = state.setdefault("provenance", [])
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    uncertainty = state.setdefault("uncertainty", {})
    if not isinstance(uncertainty, dict):
        raise TypeError(
            "context['cognitive_state']['uncertainty'] must be a dict"
        )

    provenance.append(
        {
            "sequence": len(provenance) + 1,
            "core_id": "DNA-03",
            "operation": "UNIFIED_COGNITIVE_STATE_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
        }
    )

    return state


def dna03_unified_cognitive_state(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Establish one structured, traceable state that carries uncertainty.

    DNA-03 creates the shared state contract only. It does not instantiate
    the cognitive layers, start Memory/Learning/World runtimes, call models,
    execute F174, act externally, or modify Canon.
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
    trace.append("DNA-03")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)
    state = _ensure_unified_state(
        context,
        canonical_sha256=canonical_sha256,
    )

    outputs["DNA-03"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "unified_state_profile": deepcopy(UNIFIED_STATE_PROFILE),
        "state_schema": state["schema"],
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna03(core54: Core54Like) -> None:
    core = core54.get("DNA-03")
    assert_exact_canon(core)
    core54.bind(
        "DNA-03",
        dna03_unified_cognitive_state,
    )


def self_check_dna03(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    dna01_core = core54.get("DNA-01")
    dna02_core = core54.get("DNA-02")
    if not dna01_core.state.behavior_bound:
        raise RuntimeError("DNA-01_MUST_PASS_AND_BE_BOUND_FIRST")
    if not dna02_core.state.behavior_bound:
        raise RuntimeError("DNA-02_MUST_PASS_AND_BE_BOUND_FIRST")

    dna03_core = core54.get("DNA-03")
    assert_exact_canon(dna03_core)
    bind_dna03(core54)

    probe = {
        "trace": [],
        "caller_data": {"preserve": True},
        "cognitive_state": {
            "schema": STATE_SCHEMA,
            "content": {
                "subject": "DNA-03_SELF_CHECK",
            },
            "provenance": [
                {
                    "sequence": 1,
                    "core_id": "CALLER",
                    "operation": "INPUT_CREATED",
                }
            ],
            "uncertainty": {
                "open_items": ["UNRESOLVED_TEST_ITEM"],
            },
        },
    }
    snapshot = deepcopy(probe)

    after_dna01 = dna01_core.activate(probe)
    after_dna02 = dna02_core.activate(after_dna01)
    result = dna03_core.activate(after_dna02)

    assert probe == snapshot
    assert result["trace"] == ["DNA-01", "DNA-02", "DNA-03"]

    dna03 = result["core54_outputs"]["DNA-03"]
    assert dna03["canonical_gene"] == CANON_DNA03
    assert dna03["unified_state_profile"] == UNIFIED_STATE_PROFILE
    assert dna03["state_schema"] == STATE_SCHEMA
    assert dna03["status"] == "CANON_ALIGNED"

    state = result["cognitive_state"]
    assert state["schema"] == STATE_SCHEMA
    assert state["content"] == {
        "subject": "DNA-03_SELF_CHECK",
    }
    assert state["uncertainty"] == {
        "open_items": ["UNRESOLVED_TEST_ITEM"],
    }
    assert len(state["provenance"]) == 2
    assert state["provenance"][0] == snapshot[
        "cognitive_state"
    ]["provenance"][0]

    final_event = state["provenance"][-1]
    assert final_event["sequence"] == 2
    assert final_event["core_id"] == "DNA-03"
    assert (
        final_event["operation"]
        == "UNIFIED_COGNITIVE_STATE_ESTABLISHED"
    )
    assert (
        final_event["canonical_sha256"]
        == dna03["canonical_sha256"]
    )

    default_result = dna03_core.activate(
        {
            "trace": [],
            "core54_outputs": {},
        }
    )
    default_state = default_result["cognitive_state"]
    assert default_state["schema"] == STATE_SCHEMA
    assert default_state["content"] == {}
    assert default_state["uncertainty"] == {}
    assert len(default_state["provenance"]) == 1

    # Reject provisional marker behavior as the official Canon contract.
    assert "flags" not in result
    assert "requests" not in result

    locks = {
        "auto_learning": bool(core54.auto_learning_enabled),
        "model_calls": bool(core54.model_calls_enabled),
        "external_execution": bool(core54.external_execution_enabled),
        "canon_write": bool(core54.canon_write_enabled),
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
        "core_id": "DNA-03",
        "canon_mapping": "PASS",
        "unified_state_profile": "PASS",
        "structured_state": "PASS",
        "traceability": "PASS",
        "uncertainty_carried": "PASS",
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS" if verify_canon_file else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-04"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    dna01_file = (
        GENES_ROOT
        / "SIGMA_DNA_01_PURPOSE_EXISTENCE.py"
    )
    dna02_file = (
        GENES_ROOT
        / "SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE.py"
    )

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        dna01_file,
        dna02_file,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-03_FAIL: REQUIRED_PATH_NOT_FOUND")
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
    except Exception as exc:
        print("DNA-03_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(core.state.behavior_bound for core in core54.cores):
            raise RuntimeError("FRESH_FOUNDATION_REQUIRED")

        dna01_report = self_check_dna01(
            core54,
            verify_canon_file=True,
        )
        if dna01_report["self_check"] != "PASS":
            raise RuntimeError("DNA-01_NOT_PASS")

        dna02_report = self_check_dna02(
            core54,
            verify_canon_file=True,
        )
        if dna02_report["self_check"] != "PASS":
            raise RuntimeError("DNA-02_NOT_PASS")

        report = self_check_dna03(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != ["DNA-01", "DNA-02", "DNA-03"]:
            raise RuntimeError(
                "DNA-01_TO_DNA-03_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-03_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_03_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "UNIFIED_STATE_PROFILE:",
        report["unified_state_profile"],
    )
    print("STRUCTURED_STATE:", report["structured_state"])
    print("TRACEABILITY:", report["traceability"])
    print(
        "UNCERTAINTY_CARRIED:",
        report["uncertainty_carried"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 3/54")
    print("NEXT_AUTHORIZED: DNA-04")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
