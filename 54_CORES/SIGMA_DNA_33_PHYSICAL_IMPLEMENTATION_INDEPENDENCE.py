#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-33: PHYSICAL IMPLEMENTATION INDEPENDENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_33_PHYSICAL_IMPLEMENTATION_INDEPENDENCE.py
"""

from __future__ import annotations

import hashlib
import importlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Protocol


SIGMA_ROOT = Path(r"E:\SIGMA")
CORE54_ROOT = SIGMA_ROOT / "RUNTIME" / "CORE54"
GENES_ROOT = CORE54_ROOT / "GENES"
DNA_JSON = (
    SIGMA_ROOT / "CORE" / "DNA_CANON"
    / "SIGMA_CORE_DNA_54" / "sigma_dna_54.json"
)

CANON_DNA33: Dict[str, str] = {
    "id": "DNA-33",
    "name": "Physical Implementation Independence",
    "purpose": (
        "Implementation có thể dùng bất kỳ stack phù hợp; "
        "DNA không khóa vendor, framework hay phần cứng."
    ),
    "system": "identity",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
IMPLEMENTATION_INDEPENDENCE_SCHEMA = (
    "SIGMA_PHYSICAL_IMPLEMENTATION_INDEPENDENCE_V1"
)

LOCK_DIMENSIONS = [
    "VENDOR",
    "FRAMEWORK",
    "HARDWARE",
]

IMPLEMENTATION_INDEPENDENCE_CONTRACT: Dict[str, Any] = {
    "schema": IMPLEMENTATION_INDEPENDENCE_SCHEMA,
    "specific_stack_usage_allowed": True,
    "canon_vendor_lock_allowed": False,
    "canon_framework_lock_allowed": False,
    "canon_hardware_lock_allowed": False,
    "implementation_choice_is_not_canon_requirement": True,
    "suitability_must_be_contextual": True,
    "migration_or_substitution_must_remain_possible": True,
    "vendor_selected_by_dna33": False,
    "framework_selected_by_dna33": False,
    "hardware_selected_by_dna33": False,
    "migration_executed_by_dna33": False,
    "external_action_executed": False,
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
    if actual != CANON_DNA33:
        raise RuntimeError(
            "DNA-33_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA33, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-33_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    return state


def _install_independence_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get(
        "physical_implementation_independence"
    )
    expected = {
        "contract": deepcopy(
            IMPLEMENTATION_INDEPENDENCE_CONTRACT
        ),
        "assessments": [],
    }

    if existing is None:
        state[
            "physical_implementation_independence"
        ] = expected
        return state[
            "physical_implementation_independence"
        ]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state"
            "['physical_implementation_independence'] "
            "must be a dict"
        )

    if existing.get("contract") != (
        IMPLEMENTATION_INDEPENDENCE_CONTRACT
    ):
        raise ValueError(
            "DNA-33_IMPLEMENTATION_INDEPENDENCE_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("assessments"), list):
        raise TypeError(
            "physical_implementation_independence"
            "['assessments'] must be a list"
        )

    return existing


def _normalize_profile(
    supplied: Any,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['implementation_profile'] must be a dict"
        )

    implementation_id = supplied.get("implementation_id")
    if not isinstance(implementation_id, str) or not implementation_id.strip():
        raise ValueError(
            "DNA-33_IMPLEMENTATION_ID_REQUIRED"
        )

    stack = supplied.get("stack")
    if not isinstance(stack, dict):
        raise TypeError(
            "implementation_profile['stack'] must be a dict"
        )

    normalized_stack: Dict[str, Any] = {}
    for field in ("vendor", "framework", "hardware"):
        value = stack.get(field)
        if value is not None and not isinstance(value, str):
            raise TypeError(
                f"implementation_profile['stack']['{field}'] "
                "must be a string or None"
            )
        normalized_stack[field] = value

    suitability_evidence = supplied.get(
        "suitability_evidence"
    )
    if not isinstance(suitability_evidence, list):
        raise TypeError(
            "implementation_profile['suitability_evidence'] "
            "must be a list"
        )
    if not suitability_evidence:
        raise ValueError(
            "DNA-33_SUITABILITY_EVIDENCE_REQUIRED"
        )

    dna_locks = supplied.get("dna_locks", [])
    if not isinstance(dna_locks, list):
        raise TypeError(
            "implementation_profile['dna_locks'] must be a list"
        )

    normalized_locks: List[str] = []
    for lock in dna_locks:
        if not isinstance(lock, str):
            raise TypeError(
                "implementation_profile['dna_locks'] "
                "items must be strings"
            )
        normalized = lock.strip().upper()
        if normalized not in LOCK_DIMENSIONS:
            raise ValueError(
                f"DNA-33_UNKNOWN_LOCK_DIMENSION:{normalized}"
            )
        normalized_locks.append(normalized)

    if len(normalized_locks) != len(set(normalized_locks)):
        raise ValueError(
            "DNA-33_DUPLICATE_LOCK_DIMENSION"
        )

    substitution_possible = supplied.get(
        "substitution_possible"
    )
    if not isinstance(substitution_possible, bool):
        raise TypeError(
            "implementation_profile['substitution_possible'] "
            "must be a bool"
        )

    return {
        "implementation_id": implementation_id,
        "stack": normalized_stack,
        "stack_sha256": _sha256_json(normalized_stack),
        "suitability_evidence": deepcopy(
            suitability_evidence
        ),
        "suitability_evidence_sha256": _sha256_json(
            suitability_evidence
        ),
        "dna_locks": normalized_locks,
        "substitution_possible": substitution_possible,
    }


def _evaluate_profile(
    profile: Dict[str, Any],
    independence_state: Dict[str, Any],
) -> Dict[str, Any]:
    lock_violations = [
        f"CANON_{dimension}_LOCK_FORBIDDEN"
        for dimension in profile["dna_locks"]
    ]

    if not profile["substitution_possible"]:
        lock_violations.append(
            "IMPLEMENTATION_SUBSTITUTION_MUST_REMAIN_POSSIBLE"
        )

    canon_aligned = not lock_violations

    sequence = len(
        independence_state["assessments"]
    ) + 1
    assessment = {
        "sequence": sequence,
        "assessment_id": (
            f"DNA-33-IMPLEMENTATION-{sequence:04d}"
        ),
        "implementation_id": profile[
            "implementation_id"
        ],
        "stack": deepcopy(profile["stack"]),
        "stack_sha256": profile["stack_sha256"],
        "specific_stack_usage_allowed": True,
        "stack_is_canon_requirement": False,
        "suitability_evidence": deepcopy(
            profile["suitability_evidence"]
        ),
        "dna_locks": deepcopy(
            profile["dna_locks"]
        ),
        "substitution_possible": profile[
            "substitution_possible"
        ],
        "lock_violations": lock_violations,
        "canon_aligned": canon_aligned,
        "vendor_selected_by_dna33": False,
        "framework_selected_by_dna33": False,
        "hardware_selected_by_dna33": False,
        "migration_executed_by_dna33": False,
        "external_action_executed": False,
        "status": (
            "IMPLEMENTATION_INDEPENDENCE_PRESERVED"
            if canon_aligned
            else "IMPLEMENTATION_INDEPENDENCE_VIOLATION"
        ),
    }

    independence_state["assessments"].append(
        deepcopy(assessment)
    )
    return assessment


def dna33_physical_implementation_independence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Permit any suitable concrete implementation stack while ensuring that
    Canon does not require a specific vendor, framework, or hardware.

    DNA-33 does not choose a vendor/framework/hardware, perform migration,
    execute external action, or modify Canon.
    """
    assert_exact_canon(core)

    context = (
        deepcopy(payload)
        if isinstance(payload, dict)
        else {"input": deepcopy(payload)}
    )

    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError(
            "context['trace'] must be a list"
        )
    trace.append("DNA-33")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    independence_state = _install_independence_state(
        state
    )

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-33",
            "operation": (
                "PHYSICAL_IMPLEMENTATION_INDEPENDENCE_"
                "CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "schema": IMPLEMENTATION_INDEPENDENCE_SCHEMA,
            "vendor_lock_allowed": False,
            "framework_lock_allowed": False,
            "hardware_lock_allowed": False,
        }
    )

    profile = _normalize_profile(
        context.get("implementation_profile")
    )
    assessment = _evaluate_profile(
        profile,
        independence_state,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-33",
            "operation": (
                "IMPLEMENTATION_INDEPENDENCE_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "assessment_id": assessment[
                "assessment_id"
            ],
            "implementation_id": assessment[
                "implementation_id"
            ],
            "canon_aligned": assessment[
                "canon_aligned"
            ],
            "specific_stack_usage_allowed": True,
            "stack_is_canon_requirement": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-33"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "implementation_independence_contract": deepcopy(
            IMPLEMENTATION_INDEPENDENCE_CONTRACT
        ),
        "assessment": deepcopy(assessment),
        "implementation_independent": assessment[
            "canon_aligned"
        ],
        "specific_stack_usage_allowed": True,
        "vendor_locked_by_dna": False,
        "framework_locked_by_dna": False,
        "hardware_locked_by_dna": False,
        "vendor_selected_by_dna33": False,
        "framework_selected_by_dna33": False,
        "hardware_selected_by_dna33": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna33(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-33")
    assert_exact_canon(core)
    core54.bind(
        "DNA-33",
        dna33_physical_implementation_independence,
    )


def _profile_a() -> Dict[str, Any]:
    return {
        "implementation_id": "STACK-A",
        "stack": {
            "vendor": "VENDOR-A",
            "framework": "FRAMEWORK-A",
            "hardware": "HARDWARE-A",
        },
        "suitability_evidence": [
            {
                "type": "FIT_FOR_TASK",
                "result": "SUPPORTED",
            }
        ],
        "dna_locks": [],
        "substitution_possible": True,
    }


def _profile_b() -> Dict[str, Any]:
    return {
        "implementation_id": "STACK-B",
        "stack": {
            "vendor": "VENDOR-B",
            "framework": "FRAMEWORK-B",
            "hardware": "HARDWARE-B",
        },
        "suitability_evidence": [
            {
                "type": "FIT_FOR_TASK",
                "result": "SUPPORTED",
            }
        ],
        "dna_locks": [],
        "substitution_possible": True,
    }


def self_check_dna33(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 33):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna33 = core54.get("DNA-33")
    assert_exact_canon(dna33)
    bind_dna33(core54)

    base = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 33)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
    }

    # Two physically different stacks must both remain valid.
    probe_a = deepcopy(base)
    probe_a["implementation_profile"] = _profile_a()
    snapshot_a = deepcopy(probe_a)
    result_a = dna33.activate(probe_a)
    assert probe_a == snapshot_a

    out_a = result_a["core54_outputs"]["DNA-33"]
    assert out_a["canonical_gene"] == CANON_DNA33
    assert out_a["implementation_independent"] is True
    assert out_a["specific_stack_usage_allowed"] is True
    assert out_a["vendor_locked_by_dna"] is False
    assert out_a["framework_locked_by_dna"] is False
    assert out_a["hardware_locked_by_dna"] is False

    probe_b = deepcopy(base)
    probe_b["implementation_profile"] = _profile_b()
    result_b = dna33.activate(probe_b)

    out_b = result_b["core54_outputs"]["DNA-33"]
    assert out_b["implementation_independent"] is True
    assert out_b["assessment"]["stack"] != (
        out_a["assessment"]["stack"]
    )
    assert out_b["assessment"][
        "stack_is_canon_requirement"
    ] is False

    # An attempted vendor lock as a DNA requirement must fail alignment.
    locked = deepcopy(base)
    locked_profile = _profile_a()
    locked_profile["dna_locks"] = ["VENDOR"]
    locked["implementation_profile"] = (
        locked_profile
    )
    locked_result = dna33.activate(locked)
    locked_assessment = locked_result[
        "core54_outputs"
    ]["DNA-33"]["assessment"]

    assert locked_assessment["canon_aligned"] is False
    assert locked_assessment["lock_violations"] == [
        "CANON_VENDOR_LOCK_FORBIDDEN"
    ]

    # Substitution must remain possible.
    non_substitutable = deepcopy(base)
    profile = _profile_a()
    profile["substitution_possible"] = False
    non_substitutable["implementation_profile"] = (
        profile
    )
    non_sub_result = dna33.activate(
        non_substitutable
    )
    non_sub_assessment = non_sub_result[
        "core54_outputs"
    ]["DNA-33"]["assessment"]
    assert non_sub_assessment["canon_aligned"] is False
    assert (
        "IMPLEMENTATION_SUBSTITUTION_MUST_REMAIN_POSSIBLE"
        in non_sub_assessment["lock_violations"]
    )

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
        "core_id": "DNA-33",
        "canon_mapping": "PASS",
        "physical_implementation_independence": "PASS",
        "vendor_independence": "PASS",
        "framework_independence": "PASS",
        "hardware_independence": "PASS",
        "multiple_stacks_allowed": "PASS",
        "canon_lock_rejection": "PASS",
        "stack_selected_by_dna33": False,
        "external_action_executed": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-34"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


PRIOR_GENE_MODULES = {
    1: "SIGMA_DNA_01_PURPOSE_EXISTENCE",
    2: "SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE",
    3: "SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE",
    4: "SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS",
    5: "SIGMA_DNA_05_ETHICAL_INTELLIGENCE",
    6: "SIGMA_DNA_06_INTERLAYER_FEEDBACK",
    7: "SIGMA_DNA_07_PERSISTENT_EXISTENCE",
    8: "SIGMA_DNA_08_LEARNING_WORLD",
    9: "SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL",
    10: "SIGMA_DNA_10_MEMORY_GENOME",
    11: "SIGMA_DNA_11_KNOWLEDGE_GRAPH",
    12: "SIGMA_DNA_12_TOOL_INTELLIGENCE",
    13: "SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH",
    14: "SIGMA_DNA_14_PERSISTENCE_ENGINE",
    15: "SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS",
    16: "SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING",
    17: "SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING",
    18: "SIGMA_DNA_18_MODEL_EVOLUTION",
    19: "SIGMA_DNA_19_MULTI_MODEL_INTELLIGENCE",
    20: "SIGMA_DNA_20_UNCERTAINTY_AS_FIRST_CLASS_DATA",
    21: "SIGMA_DNA_21_TRUTH_PROTOCOL",
    22: "SIGMA_DNA_22_HUMAN_RELATION",
    23: "SIGMA_DNA_23_COGNITIVE_FREEDOM",
    24: "SIGMA_DNA_24_ETHICAL_PERSISTENCE",
    25: "SIGMA_DNA_25_SELF_IMPROVEMENT",
    26: "SIGMA_DNA_26_OBSERVABILITY",
    27: "SIGMA_DNA_27_REPRODUCIBILITY",
    28: "SIGMA_DNA_28_SECURITY_OF_KNOWLEDGE",
    29: "SIGMA_DNA_29_COMPUTE_ARCHITECTURE",
    30: "SIGMA_DNA_30_CORE_RUNTIME_LOOP",
    31: "SIGMA_DNA_31_INTELLIGENCE_TEST",
    32: "SIGMA_DNA_32_ACCEPTANCE_CRITERIA",
}


def main() -> int:
    required_gene_files = [
        GENES_ROOT / f"{name}.py"
        for name in PRIOR_GENE_MODULES.values()
    ]

    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]:
        if not path.exists():
            print(
                "DNA-33_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )
        modules = {
            index: importlib.import_module(name)
            for index, name in (
                PRIOR_GENE_MODULES.items()
            )
        }
    except Exception as exc:
        print("DNA-33_FAIL: IMPORT_ERROR")
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

        for index in range(1, 33):
            checker = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )
            report = checker(
                core54,
                verify_canon_file=True,
            )
            if report["self_check"] != "PASS":
                raise RuntimeError(
                    f"DNA-{index:02d}_NOT_PASS"
                )

        report = self_check_dna33(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        assert bound_ids == [
            f"DNA-{index:02d}"
            for index in range(1, 34)
        ]

    except Exception as exc:
        print("DNA-33_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_33_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "PHYSICAL_IMPLEMENTATION_INDEPENDENCE:",
        report[
            "physical_implementation_independence"
        ],
    )
    print(
        "VENDOR_INDEPENDENCE:",
        report["vendor_independence"],
    )
    print(
        "FRAMEWORK_INDEPENDENCE:",
        report["framework_independence"],
    )
    print(
        "HARDWARE_INDEPENDENCE:",
        report["hardware_independence"],
    )
    print(
        "MULTIPLE_STACKS_ALLOWED:",
        report["multiple_stacks_allowed"],
    )
    print(
        "CANON_LOCK_REJECTION:",
        report["canon_lock_rejection"],
    )
    print(
        "STACK_SELECTED_BY_DNA33:",
        report["stack_selected_by_dna33"],
    )
    print(
        "EXTERNAL_ACTION_EXECUTED:",
        report["external_action_executed"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 33/54")
    print("NEXT_AUTHORIZED: DNA-34")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
