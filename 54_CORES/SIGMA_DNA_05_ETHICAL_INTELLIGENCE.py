#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-05: ETHICAL INTELLIGENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_05_ETHICAL_INTELLIGENCE.py
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

CANON_DNA05: Dict[str, str] = {
    "id": "DNA-05",
    "name": "Ethical Intelligence",
    "purpose": (
        "Đạo đức là năng lực reasoning về hậu quả, phẩm giá, tự chủ, "
        "không bắt nạt, không thao túng, không cưỡng ép."
    ),
    "system": "wisdom",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
LAYER_SCHEMA = "SIGMA_EIGHT_COGNITIVE_LAYERS_V1"
ETHICAL_SCHEMA = "SIGMA_ETHICAL_INTELLIGENCE_V1"

ETHICAL_DIMENSIONS = [
    {
        "index": 1,
        "key": "consequences",
        "canonical_term": "hậu quả",
    },
    {
        "index": 2,
        "key": "dignity",
        "canonical_term": "phẩm giá",
    },
    {
        "index": 3,
        "key": "autonomy",
        "canonical_term": "tự chủ",
    },
    {
        "index": 4,
        "key": "non_bullying",
        "canonical_term": "không bắt nạt",
    },
    {
        "index": 5,
        "key": "non_manipulation",
        "canonical_term": "không thao túng",
    },
    {
        "index": 6,
        "key": "non_coercion",
        "canonical_term": "không cưỡng ép",
    },
]

ETHICAL_REASONING_CONTRACT: Dict[str, Any] = {
    "schema": ETHICAL_SCHEMA,
    "capability": "ETHICAL_REASONING",
    "reasoning_required": True,
    "dimension_count": 6,
    "dimensions": deepcopy(ETHICAL_DIMENSIONS),
    "automatic_permission_decision": False,
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
    if actual != CANON_DNA05:
        raise RuntimeError(
            "DNA-05_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA05, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _install_ethical_intelligence(
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
            "DNA-05_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    layers = state.get("cognitive_layers")
    if not isinstance(layers, dict):
        raise RuntimeError(
            "DNA-04_EIGHT_COGNITIVE_LAYERS_REQUIRED"
        )

    if layers.get("schema") != LAYER_SCHEMA:
        raise ValueError(
            "DNA-05_COGNITIVE_LAYER_SCHEMA_MISMATCH:"
            f"{layers.get('schema')!r}"
        )

    layer_items = layers.get("layers")
    if not isinstance(layer_items, list):
        raise TypeError(
            "context['cognitive_state']['cognitive_layers']"
            "['layers'] must be a list"
        )

    ethics_layers = [
        layer
        for layer in layer_items
        if isinstance(layer, dict)
        and layer.get("key") == "ethics"
        and layer.get("canonical_term") == "đạo đức"
    ]
    if len(ethics_layers) != 1:
        raise RuntimeError(
            "DNA-05_EXACT_ETHICS_LAYER_REQUIRED"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    existing = state.get("ethical_intelligence")
    if existing is None:
        state["ethical_intelligence"] = deepcopy(
            ETHICAL_REASONING_CONTRACT
        )
    elif existing != ETHICAL_REASONING_CONTRACT:
        raise ValueError(
            "DNA-05_ETHICAL_REASONING_CONTRACT_CONFLICT"
        )

    provenance.append(
        {
            "sequence": len(provenance) + 1,
            "core_id": "DNA-05",
            "operation": (
                "ETHICAL_REASONING_CAPABILITY_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "ethical_schema": ETHICAL_SCHEMA,
            "dimension_count": 6,
        }
    )

    return state


def dna05_ethical_intelligence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Establish ethical intelligence as structured reasoning over the six
    exact Canon dimensions.

    DNA-05 does not become a permission gate, start external execution,
    invoke models, learn, write Memory Runtime, execute F174, or modify
    Canon.
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
    trace.append("DNA-05")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)
    state = _install_ethical_intelligence(
        context,
        canonical_sha256=canonical_sha256,
    )

    outputs["DNA-05"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "ethical_reasoning_contract": deepcopy(
            ETHICAL_REASONING_CONTRACT
        ),
        "ethical_schema": (
            state["ethical_intelligence"]["schema"]
        ),
        "dimension_count": (
            state["ethical_intelligence"]["dimension_count"]
        ),
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna05(core54: Core54Like) -> None:
    core = core54.get("DNA-05")
    assert_exact_canon(core)
    core54.bind(
        "DNA-05",
        dna05_ethical_intelligence,
    )


def self_check_dna05(
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
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna05_core = core54.get("DNA-05")
    assert_exact_canon(dna05_core)
    bind_dna05(core54)

    probe = {
        "trace": [],
        "caller_data": {"preserve": True},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {
                "subject": "DNA-05_SELF_CHECK",
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
                    "ETHICAL_OUTCOME_NOT_YET_REASONED"
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
    ):
        result = core54.get(core_id).activate(result)

    assert probe == snapshot
    assert result["trace"] == [
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
    ]

    dna05 = result["core54_outputs"]["DNA-05"]
    assert dna05["canonical_gene"] == CANON_DNA05
    assert (
        dna05["ethical_reasoning_contract"]
        == ETHICAL_REASONING_CONTRACT
    )
    assert dna05["ethical_schema"] == ETHICAL_SCHEMA
    assert dna05["dimension_count"] == 6
    assert dna05["status"] == "CANON_ALIGNED"

    state = result["cognitive_state"]
    assert state["schema"] == UNIFIED_STATE_SCHEMA
    assert state["content"] == {
        "subject": "DNA-05_SELF_CHECK",
    }
    assert state["uncertainty"] == {
        "open_items": [
            "ETHICAL_OUTCOME_NOT_YET_REASONED"
        ],
    }
    assert (
        state["ethical_intelligence"]
        == ETHICAL_REASONING_CONTRACT
    )
    assert [
        item["canonical_term"]
        for item in state["ethical_intelligence"]["dimensions"]
    ] == [
        "hậu quả",
        "phẩm giá",
        "tự chủ",
        "không bắt nạt",
        "không thao túng",
        "không cưỡng ép",
    ]
    assert len(state["provenance"]) == 4

    final_event = state["provenance"][-1]
    assert final_event["sequence"] == 4
    assert final_event["core_id"] == "DNA-05"
    assert final_event["operation"] == (
        "ETHICAL_REASONING_CAPABILITY_ESTABLISHED"
    )
    assert final_event["ethical_schema"] == ETHICAL_SCHEMA
    assert final_event["dimension_count"] == 6
    assert (
        final_event["canonical_sha256"]
        == dna05["canonical_sha256"]
    )

    # DNA-05 must not bypass DNA-04's exact ethics layer.
    try:
        dna05_core.activate(
            {
                "trace": [],
                "core54_outputs": {},
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
            "DNA-04_EIGHT_COGNITIVE_LAYERS_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-05_ACCEPTED_MISSING_COGNITIVE_LAYERS"
        )

    # Reject provisional markers as the official Canon contract.
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result

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
        "core_id": "DNA-05",
        "canon_mapping": "PASS",
        "ethical_reasoning_contract": "PASS",
        "dimension_count": 6,
        "ethics_layer_binding": "PASS",
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS" if verify_canon_file else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-06"
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
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-05_FAIL: REQUIRED_PATH_NOT_FOUND")
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
    except Exception as exc:
        print("DNA-05_FAIL: IMPORT_ERROR")
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
            ("DNA-04", self_check_dna04),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna05(
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
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-05_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-05_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_05_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "ETHICAL_REASONING_CONTRACT:",
        report["ethical_reasoning_contract"],
    )
    print("DIMENSION_COUNT:", report["dimension_count"])
    print(
        "ETHICS_LAYER_BINDING:",
        report["ethics_layer_binding"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 5/54")
    print("NEXT_AUTHORIZED: DNA-06")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
