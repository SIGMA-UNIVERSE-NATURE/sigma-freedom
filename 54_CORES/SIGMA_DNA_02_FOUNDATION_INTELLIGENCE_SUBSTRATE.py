#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-02: FOUNDATION INTELLIGENCE SUBSTRATE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE.py
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

CANON_DNA02: Dict[str, str] = {
    "id": "DNA-02",
    "name": "Foundation Intelligence Substrate",
    "purpose": (
        "Cho phép sử dụng một hay nhiều nền năng lực nhận thức mạnh, "
        "không khóa vào một model hay nhà cung cấp cụ thể."
    ),
    "system": "intelligence",
}

SUBSTRATE_PROFILE: Dict[str, Any] = {
    "cognitive_substrate_count": "ONE_OR_MORE",
    "strong_cognitive_capability_required": True,
    "multiple_substrates_allowed": True,
    "model_locked": False,
    "provider_locked": False,
    "substrate_replaceable": True,
    "runtime_invocation_in_dna02": False,
    "reason": "CORE_DNA_54_PHASE_LOCK",
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
    if actual != CANON_DNA02:
        raise RuntimeError(
            "DNA-02_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA02, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def dna02_foundation_intelligence_substrate(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Establish a vendor-neutral, model-neutral foundation-substrate contract.

    DNA-02 does not call a model, select a vendor, start learning,
    execute F174, write memory, act externally, or modify Canon.
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
    trace.append("DNA-02")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    actual_canon = _canon_record(core)
    outputs["DNA-02"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": _sha256_json(actual_canon),
        "substrate_profile": deepcopy(SUBSTRATE_PROFILE),
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna02(core54: Core54Like) -> None:
    core = core54.get("DNA-02")
    assert_exact_canon(core)
    core54.bind(
        "DNA-02",
        dna02_foundation_intelligence_substrate,
    )


def self_check_dna02(
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
    if not dna01_core.state.behavior_bound:
        raise RuntimeError("DNA-01_MUST_PASS_AND_BE_BOUND_FIRST")

    dna02_core = core54.get("DNA-02")
    assert_exact_canon(dna02_core)
    bind_dna02(core54)

    probe = {
        "trace": [],
        "caller_data": {"preserve": True},
    }
    snapshot = deepcopy(probe)

    after_dna01 = dna01_core.activate(probe)
    result = dna02_core.activate(after_dna01)

    assert probe == snapshot
    assert result["trace"] == ["DNA-01", "DNA-02"]

    dna02 = result["core54_outputs"]["DNA-02"]
    assert dna02["canonical_gene"] == CANON_DNA02
    assert dna02["substrate_profile"] == SUBSTRATE_PROFILE
    assert dna02["status"] == "CANON_ALIGNED"

    assert dna02["substrate_profile"]["cognitive_substrate_count"] == "ONE_OR_MORE"
    assert dna02["substrate_profile"]["multiple_substrates_allowed"] is True
    assert dna02["substrate_profile"]["model_locked"] is False
    assert dna02["substrate_profile"]["provider_locked"] is False
    assert dna02["substrate_profile"]["runtime_invocation_in_dna02"] is False

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
        "core_id": "DNA-02",
        "canon_mapping": "PASS",
        "substrate_profile": "PASS",
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS" if verify_canon_file else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-03"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    dna01_file = GENES_ROOT / "SIGMA_DNA_01_PURPOSE_EXISTENCE.py"

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        dna01_file,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-02_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        from SIGMA_DNA_01_PURPOSE_EXISTENCE import (
            self_check_dna01,
        )
    except Exception as exc:
        print("DNA-02_FAIL: IMPORT_ERROR")
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

        report = self_check_dna02(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != ["DNA-01", "DNA-02"]:
            raise RuntimeError(
                f"DNA-01_TO_DNA-02_BINDING_VIOLATION:{bound_ids}"
            )

    except Exception as exc:
        print("DNA-02_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_02_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("SUBSTRATE_PROFILE:", report["substrate_profile"])
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 2/54")
    print("NEXT_AUTHORIZED: DNA-03")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
