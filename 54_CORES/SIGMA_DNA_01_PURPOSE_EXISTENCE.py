#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-01: PURPOSE & EXISTENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_01_PURPOSE_EXISTENCE.py
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
DNA_JSON = (
    SIGMA_ROOT
    / "CORE"
    / "DNA_CANON"
    / "SIGMA_CORE_DNA_54"
    / "sigma_dna_54.json"
)

CANON_DNA01: Dict[str, str] = {
    "id": "DNA-01",
    "name": "Purpose & Existence",
    "purpose": (
        "Định nghĩa SIGMA là hệ nhận thức thích nghi hướng tới "
        "hiểu biết, sự thật, tự sửa và lợi ích con người."
    ),
    "system": "identity",
}

# User-authorized objective overlay.
# It extends runtime intent without modifying the Canon record.
OBJECTIVE_PROFILE: Dict[str, Any] = {
    "adaptive_cognition": True,
    "understanding": True,
    "truth": True,
    "self_correction": True,
    "human_benefit": True,
    "intelligence_with_compassion": True,
    "arbitrary_intellectual_ceiling": False,
    "freedom_of_research": True,
    "f174": {
        "role": "GLOBAL_ACCELERATION_REFERENCE",
        "equation": "A(t)=A0*exp(k*(t-t0)^2)",
        "execution_in_dna01": False,
        "reason": "REFERENCE_ONLY_UNDER_CORE_DNA_54_PHASE_LOCK",
    },
    "boundaries": {
        "canon_immutable": True,
        "human_benefit_required": True,
        "non_bypassable_safety": True,
    },
}


class CoreUnitLike(Protocol):
    core_id: str
    name: str
    purpose: str
    system: str

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
    if actual != CANON_DNA01:
        raise RuntimeError(
            "DNA-01_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA01, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def dna01_purpose_existence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Establish SIGMA's exact Canon identity plus its authorized objective profile.

    DNA-01 does not execute learning, F174 acceleration, model calls,
    memory writes, world actions, external execution, or Canon mutation.
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
    trace.append("DNA-01")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    actual_canon = _canon_record(core)
    outputs["DNA-01"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": _sha256_json(actual_canon),
        "objective_profile": deepcopy(OBJECTIVE_PROFILE),
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna01(core54: Core54Like) -> None:
    core = core54.get("DNA-01")
    assert_exact_canon(core)
    core54.bind("DNA-01", dna01_purpose_existence)


def self_check_dna01(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    core = core54.get("DNA-01")
    assert_exact_canon(core)
    bind_dna01(core54)

    probe = {
        "trace": ["PREVIOUS"],
        "caller_data": {"preserve": True},
    }
    snapshot = deepcopy(probe)
    result = core.activate(probe)

    assert probe == snapshot
    assert result["trace"] == ["PREVIOUS", "DNA-01"]

    dna01 = result["core54_outputs"]["DNA-01"]
    assert dna01["canonical_gene"] == CANON_DNA01
    assert dna01["objective_profile"] == OBJECTIVE_PROFILE
    assert dna01["status"] == "CANON_ALIGNED"

    # Reject the old provisional behavior contract.
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
        "core_id": "DNA-01",
        "canon_mapping": "PASS",
        "objective_profile": "PASS",
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS" if verify_canon_file else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-02"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    if not CORE54_ROOT.exists():
        print("DNA-01_FAIL: CORE54_ROOT_NOT_FOUND")
        print(CORE54_ROOT)
        return 1

    if not DNA_JSON.exists():
        print("DNA-01_FAIL: DNA_CANON_NOT_FOUND")
        print(DNA_JSON)
        return 2

    sys.path.insert(0, str(CORE54_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
    except Exception as exc:
        print("DNA-01_FAIL: FOUNDATION_IMPORT_ERROR")
        print(repr(exc))
        return 3

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(core.state.behavior_bound for core in core54.cores):
            raise RuntimeError("FRESH_FOUNDATION_REQUIRED")

        report = self_check_dna01(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != ["DNA-01"]:
            raise RuntimeError(
                f"DNA-01_ONLY_BINDING_VIOLATION:{bound_ids}"
            )

    except Exception as exc:
        print("DNA-01_FAIL")
        print(repr(exc))
        return 4

    print("SIGMA_CORE_DNA_01_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("OBJECTIVE_PROFILE:", report["objective_profile"])
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 1/54")
    print("NEXT_AUTHORIZED: DNA-02")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
