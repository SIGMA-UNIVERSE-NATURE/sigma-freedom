#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-04: EIGHT COGNITIVE LAYERS
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS.py
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

CANON_DNA04: Dict[str, str] = {
    "id": "DNA-04",
    "name": "Eight Cognitive Layers",
    "purpose": (
        "Tổ chức nhận thức qua cảm nhận, ý nghĩa, phản biện, khám phá, "
        "kiểm chứng, đạo đức, hồi tiếp và vòng đời."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
LAYER_SCHEMA = "SIGMA_EIGHT_COGNITIVE_LAYERS_V1"

LAYER_DEFINITIONS = [
    {
        "index": 1,
        "key": "perception",
        "canonical_term": "cảm nhận",
    },
    {
        "index": 2,
        "key": "meaning",
        "canonical_term": "ý nghĩa",
    },
    {
        "index": 3,
        "key": "critical_reasoning",
        "canonical_term": "phản biện",
    },
    {
        "index": 4,
        "key": "discovery",
        "canonical_term": "khám phá",
    },
    {
        "index": 5,
        "key": "verification",
        "canonical_term": "kiểm chứng",
    },
    {
        "index": 6,
        "key": "ethics",
        "canonical_term": "đạo đức",
    },
    {
        "index": 7,
        "key": "feedback",
        "canonical_term": "hồi tiếp",
    },
    {
        "index": 8,
        "key": "lifecycle",
        "canonical_term": "vòng đời",
    },
]

EIGHT_LAYER_CONTRACT: Dict[str, Any] = {
    "schema": LAYER_SCHEMA,
    "layer_count": 8,
    "shared_state": True,
    "layers": deepcopy(LAYER_DEFINITIONS),
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
    if actual != CANON_DNA04:
        raise RuntimeError(
            "DNA-04_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA04, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _install_layer_contract(
    context: Dict[str, Any],
    *,
    canonical_sha256: str,
) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-04_UNIFIED_STATE_SCHEMA_MISMATCH:"
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

    existing = state.get("cognitive_layers")
    if existing is None:
        state["cognitive_layers"] = deepcopy(
            EIGHT_LAYER_CONTRACT
        )
    elif existing != EIGHT_LAYER_CONTRACT:
        raise ValueError("DNA-04_LAYER_CONTRACT_CONFLICT")

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-04",
            "operation": "EIGHT_COGNITIVE_LAYERS_ORGANIZED",
            "canonical_sha256": canonical_sha256,
            "layer_schema": LAYER_SCHEMA,
            "layer_count": 8,
        }
    )

    return state


def dna04_eight_cognitive_layers(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Organize the shared DNA-03 cognitive state into exactly eight
    Canon-derived layers.

    This core establishes the layer contract only. It does not start the
    cognitive runtime, Memory/Learning/World runtimes, model calls, F174
    execution, external action, or Canon writes.
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
    trace.append("DNA-04")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)
    state = _install_layer_contract(
        context,
        canonical_sha256=canonical_sha256,
    )

    outputs["DNA-04"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "layer_contract": deepcopy(EIGHT_LAYER_CONTRACT),
        "layer_schema": state["cognitive_layers"]["schema"],
        "layer_count": state["cognitive_layers"]["layer_count"],
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna04(core54: Core54Like) -> None:
    core = core54.get("DNA-04")
    assert_exact_canon(core)
    core54.bind(
        "DNA-04",
        dna04_eight_cognitive_layers,
    )


def self_check_dna04(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for required_id in ("DNA-01", "DNA-02", "DNA-03"):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna04_core = core54.get("DNA-04")
    assert_exact_canon(dna04_core)
    bind_dna04(core54)

    probe = {
        "trace": [],
        "caller_data": {"preserve": True},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {
                "subject": "DNA-04_SELF_CHECK",
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

    result = probe
    for core_id in ("DNA-01", "DNA-02", "DNA-03", "DNA-04"):
        result = core54.get(core_id).activate(result)

    assert probe == snapshot
    assert result["trace"] == [
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
    ]

    dna04 = result["core54_outputs"]["DNA-04"]
    assert dna04["canonical_gene"] == CANON_DNA04
    assert dna04["layer_contract"] == EIGHT_LAYER_CONTRACT
    assert dna04["layer_schema"] == LAYER_SCHEMA
    assert dna04["layer_count"] == 8
    assert dna04["status"] == "CANON_ALIGNED"

    state = result["cognitive_state"]
    assert state["schema"] == UNIFIED_STATE_SCHEMA
    assert state["content"] == {
        "subject": "DNA-04_SELF_CHECK",
    }
    assert state["uncertainty"] == {
        "open_items": ["UNRESOLVED_TEST_ITEM"],
    }
    assert state["cognitive_layers"] == EIGHT_LAYER_CONTRACT
    assert [
        item["canonical_term"]
        for item in state["cognitive_layers"]["layers"]
    ] == [
        "cảm nhận",
        "ý nghĩa",
        "phản biện",
        "khám phá",
        "kiểm chứng",
        "đạo đức",
        "hồi tiếp",
        "vòng đời",
    ]
    assert len(state["provenance"]) == 3

    final_event = state["provenance"][-1]
    assert final_event["sequence"] == 3
    assert final_event["core_id"] == "DNA-04"
    assert (
        final_event["operation"]
        == "EIGHT_COGNITIVE_LAYERS_ORGANIZED"
    )
    assert final_event["layer_schema"] == LAYER_SCHEMA
    assert final_event["layer_count"] == 8
    assert (
        final_event["canonical_sha256"]
        == dna04["canonical_sha256"]
    )

    # DNA-04 must refuse to bypass DNA-03's shared state.
    try:
        dna04_core.activate(
            {
                "trace": [],
                "core54_outputs": {},
            }
        )
    except RuntimeError as exc:
        assert str(exc) == (
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-04_ACCEPTED_MISSING_UNIFIED_STATE"
        )

    # Reject provisional marker behavior.
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
        "core_id": "DNA-04",
        "canon_mapping": "PASS",
        "eight_layer_contract": "PASS",
        "layer_count": 8,
        "shared_state_binding": "PASS",
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS" if verify_canon_file else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-05"
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
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-04_FAIL: REQUIRED_PATH_NOT_FOUND")
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
    except Exception as exc:
        print("DNA-04_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(core.state.behavior_bound for core in core54.cores):
            raise RuntimeError("FRESH_FOUNDATION_REQUIRED")

        prior_checks = (
            ("DNA-01", self_check_dna01),
            ("DNA-02", self_check_dna02),
            ("DNA-03", self_check_dna03),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna04(
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
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-04_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-04_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_04_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "EIGHT_LAYER_CONTRACT:",
        report["eight_layer_contract"],
    )
    print("LAYER_COUNT:", report["layer_count"])
    print(
        "SHARED_STATE_BINDING:",
        report["shared_state_binding"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 4/54")
    print("NEXT_AUTHORIZED: DNA-05")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
