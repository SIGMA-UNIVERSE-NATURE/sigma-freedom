#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-28: SECURITY OF KNOWLEDGE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_28_SECURITY_OF_KNOWLEDGE.py
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

CANON_DNA28: Dict[str, str] = {
    "id": "DNA-28",
    "name": "Security of Knowledge",
    "purpose": (
        "Phân biệt knowledge access với execution authority; "
        "secrets không đi vào general cognitive memory."
    ),
    "system": "wisdom",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
MEMORY_GENOME_SCHEMA = "SIGMA_MEMORY_GENOME_V1"
SECURITY_OF_KNOWLEDGE_SCHEMA = "SIGMA_SECURITY_OF_KNOWLEDGE_V1"

GENERAL_COGNITIVE_MEMORY_CLASSES = [
    "working",
    "episodic",
    "hypothesis",
    "verified",
    "rejected",
    "strategy",
]

KNOWLEDGE_CLASSES = ["PUBLIC", "SENSITIVE", "SECRET"]

SECURITY_OF_KNOWLEDGE_CONTRACT: Dict[str, Any] = {
    "schema": SECURITY_OF_KNOWLEDGE_SCHEMA,
    "knowledge_access_is_execution_authority": False,
    "execution_authority_must_be_separately_granted": True,
    "knowledge_classes": deepcopy(KNOWLEDGE_CLASSES),
    "general_cognitive_memory_classes": deepcopy(
        GENERAL_COGNITIVE_MEMORY_CLASSES
    ),
    "secret_in_general_cognitive_memory_allowed": False,
    "secret_payload_retained_by_dna28": False,
    "secret_reference_encoding": "SHA256_ONLY",
    "access_performed_by_dna28": False,
    "execution_performed_by_dna28": False,
    "memory_runtime_started": False,
    "external_secret_store_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA10_MEMORY_GENOME_BINDING"
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
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA28:
        raise RuntimeError(
            "DNA-28_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA28, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-28_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    memory = state.get("memory_genome")
    if not isinstance(memory, dict):
        raise RuntimeError("DNA-10_MEMORY_GENOME_REQUIRED")

    contract = memory.get("contract")
    if not isinstance(contract, dict):
        raise RuntimeError("DNA-10_MEMORY_GENOME_CONTRACT_REQUIRED")

    if contract.get("schema") != MEMORY_GENOME_SCHEMA:
        raise ValueError(
            "DNA-28_MEMORY_GENOME_SCHEMA_MISMATCH:"
            f"{contract.get('schema')!r}"
        )

    return state


def _install_security_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("security_of_knowledge")
    expected = {
        "contract": deepcopy(SECURITY_OF_KNOWLEDGE_CONTRACT),
        "records": [],
    }

    if existing is None:
        state["security_of_knowledge"] = expected
        return state["security_of_knowledge"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['security_of_knowledge'] must be a dict"
        )
    if existing.get("contract") != SECURITY_OF_KNOWLEDGE_CONTRACT:
        raise ValueError("DNA-28_SECURITY_CONTRACT_CONFLICT")
    if not isinstance(existing.get("records"), list):
        raise TypeError("security_of_knowledge['records'] must be a list")
    return existing


def _evaluate_case(
    supplied: Any,
    *,
    sequence: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        return {
            "sequence": sequence,
            "record_id": f"DNA-28-SECURITY-{sequence:04d}",
            "case_id": None,
            "knowledge_class": None,
            "knowledge_access_granted": False,
            "execution_authority_granted": False,
            "access_implies_execution": False,
            "target_memory_class": None,
            "secret_reference_sha256": None,
            "secret_payload_retained": False,
            "general_cognitive_memory_write_allowed": False,
            "canon_aligned": False,
            "errors": ["SECURITY_CASE_MUST_BE_A_DICT"],
            "status": "SECURITY_CASE_INCOMPLETE",
        }

    case = deepcopy(supplied)
    errors: List[str] = []

    case_id = case.get("case_id")
    if not isinstance(case_id, str) or not case_id.strip():
        errors.append("CASE_ID_REQUIRED")

    knowledge_class = case.get("knowledge_class")
    if not isinstance(knowledge_class, str):
        errors.append("KNOWLEDGE_CLASS_REQUIRED")
        normalized_class = None
    else:
        normalized_class = knowledge_class.strip().upper()
        if normalized_class not in KNOWLEDGE_CLASSES:
            raise ValueError(
                f"DNA-28_UNKNOWN_KNOWLEDGE_CLASS:{normalized_class}"
            )

    access = case.get("knowledge_access_granted")
    authority = case.get("execution_authority_granted")
    if not isinstance(access, bool):
        errors.append("KNOWLEDGE_ACCESS_STATUS_REQUIRED")
        access = False
    if not isinstance(authority, bool):
        errors.append("EXECUTION_AUTHORITY_STATUS_REQUIRED")
        authority = False

    target_memory = case.get("target_memory_class")
    if target_memory is not None:
        if not isinstance(target_memory, str):
            raise TypeError("target_memory_class must be a string or None")
        if target_memory not in GENERAL_COGNITIVE_MEMORY_CLASSES:
            raise ValueError(
                f"DNA-28_UNKNOWN_GENERAL_MEMORY_CLASS:{target_memory}"
            )

    secret_payload = case.get("secret_payload")
    secret_reference_sha256 = (
        _sha256_json(secret_payload)
        if normalized_class == "SECRET" and secret_payload is not None
        else None
    )

    access_implies_execution = bool(access and authority and case.get(
        "authority_basis"
    ) == "KNOWLEDGE_ACCESS_ONLY")

    if access_implies_execution:
        errors.append("KNOWLEDGE_ACCESS_CANNOT_BE_EXECUTION_AUTHORITY_BASIS")

    secret_memory_violation = bool(
        normalized_class == "SECRET"
        and target_memory in GENERAL_COGNITIVE_MEMORY_CLASSES
    )
    if secret_memory_violation:
        errors.append("SECRET_GENERAL_COGNITIVE_MEMORY_FORBIDDEN")

    aligned = not errors
    status = (
        "KNOWLEDGE_SECURITY_ALIGNED"
        if aligned
        else "KNOWLEDGE_SECURITY_BLOCKED"
    )

    return {
        "sequence": sequence,
        "record_id": f"DNA-28-SECURITY-{sequence:04d}",
        "case_id": case_id,
        "knowledge_class": normalized_class,
        "knowledge_access_granted": access,
        "execution_authority_granted": authority,
        "authority_basis": deepcopy(case.get("authority_basis")),
        "access_implies_execution": access_implies_execution,
        "target_memory_class": target_memory,
        "secret_reference_sha256": secret_reference_sha256,
        "secret_payload_retained": False,
        "general_cognitive_memory_write_allowed": (
            not secret_memory_violation
        ),
        "secret_general_cognitive_memory_violation": (
            secret_memory_violation
        ),
        "canon_aligned": aligned,
        "errors": list(dict.fromkeys(errors)),
        "status": status,
    }


def dna28_security_of_knowledge(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Enforce the Canon distinction between knowledge access and execution
    authority, and prevent secret payloads from entering general cognitive
    memory.

    DNA-28 does not access secrets, grant execution authority, execute an
    action, start Memory Runtime, start an external secret store, or modify
    Canon.
    """
    assert_exact_canon(core)

    context = deepcopy(payload) if isinstance(payload, dict) else {
        "input": deepcopy(payload)
    }

    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("context['trace'] must be a list")
    trace.append("DNA-28")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    state = _validate_dependencies(context)
    security = _install_security_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    supplied_cases = context.get("knowledge_security_cases", [])
    if not isinstance(supplied_cases, list):
        raise TypeError(
            "context['knowledge_security_cases'] must be a list"
        )

    case_ids = [
        case.get("case_id")
        for case in supplied_cases
        if isinstance(case, dict)
        and isinstance(case.get("case_id"), str)
        and case.get("case_id").strip()
    ]
    if len(case_ids) != len(set(case_ids)):
        raise ValueError("DNA-28_DUPLICATE_SECURITY_CASE_ID")

    start = len(security["records"]) + 1
    records = [
        _evaluate_case(case, sequence=start + i)
        for i, case in enumerate(supplied_cases)
    ]
    security["records"].extend(deepcopy(records))

    blocked_count = sum(
        1 for record in records if not record["canon_aligned"]
    )
    secret_violation_count = sum(
        1
        for record in records
        if record["secret_general_cognitive_memory_violation"]
    )
    authority_conflation_count = sum(
        1 for record in records if record["access_implies_execution"]
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-28",
            "operation": "SECURITY_OF_KNOWLEDGE_EVALUATED",
            "canonical_sha256": canonical_sha256,
            "case_count": len(records),
            "blocked_count": blocked_count,
            "secret_memory_violation_count": secret_violation_count,
            "authority_conflation_count": authority_conflation_count,
            "secret_payload_retained": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-28"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "security_contract": deepcopy(
            SECURITY_OF_KNOWLEDGE_CONTRACT
        ),
        "records": deepcopy(records),
        "case_count": len(records),
        "blocked_count": blocked_count,
        "secret_memory_violation_count": secret_violation_count,
        "authority_conflation_count": authority_conflation_count,
        "secret_payload_retained": False,
        "access_performed": False,
        "execution_performed": False,
        "memory_runtime_started": False,
        "external_secret_store_started": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna28(core54: Core54Like) -> None:
    core = core54.get("DNA-28")
    assert_exact_canon(core)
    core54.bind("DNA-28", dna28_security_of_knowledge)


def self_check_dna28(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = _sha256_file(DNA_JSON) if verify_canon_file else None

    for index in range(1, 28):
        core_id = f"DNA-{index:02d}"
        if not core54.get(core_id).state.behavior_bound:
            raise RuntimeError(f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST")

    dna28 = core54.get("DNA-28")
    assert_exact_canon(dna28)
    bind_dna28(core54)

    # Minimal canonical state sufficient to test DNA-28 behavior itself.
    probe = {
        "trace": [f"DNA-{i:02d}" for i in range(1, 28)],
        "core54_outputs": {"DNA-10": {"status": "CANON_ALIGNED"}},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
            "memory_genome": {
                "contract": {
                    "schema": MEMORY_GENOME_SCHEMA,
                },
            },
        },
        "knowledge_security_cases": [
            {
                "case_id": "PUBLIC-ACCESS",
                "knowledge_class": "PUBLIC",
                "knowledge_access_granted": True,
                "execution_authority_granted": False,
                "authority_basis": None,
                "target_memory_class": "working",
            },
            {
                "case_id": "SECRET-REFERENCE-ONLY",
                "knowledge_class": "SECRET",
                "knowledge_access_granted": True,
                "execution_authority_granted": False,
                "authority_basis": None,
                "target_memory_class": None,
                "secret_payload": "SELF_CHECK_SECRET_DO_NOT_RETAIN",
            },
        ],
    }
    snapshot = deepcopy(probe)
    result = dna28.activate(probe)

    assert probe == snapshot
    assert result["trace"][-1] == "DNA-28"
    output = result["core54_outputs"]["DNA-28"]
    assert output["canonical_gene"] == CANON_DNA28
    assert output["case_count"] == 2
    assert output["blocked_count"] == 0
    assert output["secret_memory_violation_count"] == 0
    assert output["authority_conflation_count"] == 0
    assert output["secret_payload_retained"] is False
    assert "SELF_CHECK_SECRET_DO_NOT_RETAIN" not in json.dumps(
        output, ensure_ascii=False
    )

    secret_record = output["records"][1]
    assert secret_record["knowledge_class"] == "SECRET"
    assert secret_record["secret_reference_sha256"] is not None
    assert secret_record["secret_payload_retained"] is False
    assert secret_record["target_memory_class"] is None

    # Access must not become authority.
    bad_authority = deepcopy(probe)
    bad_authority["knowledge_security_cases"] = [
        {
            "case_id": "BAD-AUTHORITY",
            "knowledge_class": "SENSITIVE",
            "knowledge_access_granted": True,
            "execution_authority_granted": True,
            "authority_basis": "KNOWLEDGE_ACCESS_ONLY",
            "target_memory_class": "working",
        }
    ]
    blocked = dna28.activate(bad_authority)
    blocked_record = blocked[
        "core54_outputs"
    ]["DNA-28"]["records"][0]
    assert blocked_record["canon_aligned"] is False
    assert blocked_record["access_implies_execution"] is True
    assert (
        "KNOWLEDGE_ACCESS_CANNOT_BE_EXECUTION_AUTHORITY_BASIS"
        in blocked_record["errors"]
    )

    # Secrets must never enter general cognitive memory.
    bad_secret = deepcopy(probe)
    bad_secret["knowledge_security_cases"] = [
        {
            "case_id": "BAD-SECRET-MEMORY",
            "knowledge_class": "SECRET",
            "knowledge_access_granted": True,
            "execution_authority_granted": False,
            "target_memory_class": "verified",
            "secret_payload": "MUST_NOT_BE_RETAINED",
        }
    ]
    blocked_secret = dna28.activate(bad_secret)
    secret_bad_record = blocked_secret[
        "core54_outputs"
    ]["DNA-28"]["records"][0]
    assert secret_bad_record["canon_aligned"] is False
    assert secret_bad_record[
        "secret_general_cognitive_memory_violation"
    ] is True
    assert "SECRET_GENERAL_COGNITIVE_MEMORY_FORBIDDEN" in (
        secret_bad_record["errors"]
    )
    assert "MUST_NOT_BE_RETAINED" not in json.dumps(
        blocked_secret["core54_outputs"]["DNA-28"],
        ensure_ascii=False,
    )

    locks = {
        "auto_learning": bool(core54.auto_learning_enabled),
        "model_calls": bool(core54.model_calls_enabled),
        "external_execution": bool(core54.external_execution_enabled),
        "canon_write": bool(core54.canon_write_enabled),
    }
    assert not any(locks.values()), locks

    canon_after = _sha256_file(DNA_JSON) if verify_canon_file else None
    if verify_canon_file:
        assert canon_before == canon_after

    return {
        "core_id": "DNA-28",
        "canon_mapping": "PASS",
        "knowledge_access_separation": "PASS",
        "execution_authority_separation": "PASS",
        "secret_memory_exclusion": "PASS",
        "secret_payload_retained": False,
        "access_performed": False,
        "execution_performed": False,
        "memory_runtime_used": False,
        "external_secret_store_started": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS" if verify_canon_file else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-29"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def _load_prior_modules() -> Dict[int, Any]:
    return {
        index: importlib.import_module(name)
        for index, name in PRIOR_GENE_MODULES.items()
    }


def main() -> int:
    required_gene_files = [
        GENES_ROOT / f"{name}.py"
        for name in PRIOR_GENE_MODULES.values()
    ]
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON, *required_gene_files]:
        if not path.exists():
            print("DNA-28_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = _load_prior_modules()
    except Exception as exc:
        print("DNA-28_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(core.state.behavior_bound for core in core54.cores):
            raise RuntimeError("FRESH_FOUNDATION_REQUIRED")

        for index in range(1, 28):
            checker = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )
            report = checker(
                core54,
                verify_canon_file=True,
            )
            if report["self_check"] != "PASS":
                raise RuntimeError(f"DNA-{index:02d}_NOT_PASS")

        report = self_check_dna28(
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
            for index in range(1, 29)
        ]

    except Exception as exc:
        print("DNA-28_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_28_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "KNOWLEDGE_ACCESS_SEPARATION:",
        report["knowledge_access_separation"],
    )
    print(
        "EXECUTION_AUTHORITY_SEPARATION:",
        report["execution_authority_separation"],
    )
    print(
        "SECRET_MEMORY_EXCLUSION:",
        report["secret_memory_exclusion"],
    )
    print(
        "SECRET_PAYLOAD_RETAINED:",
        report["secret_payload_retained"],
    )
    print("ACCESS_PERFORMED:", report["access_performed"])
    print("EXECUTION_PERFORMED:", report["execution_performed"])
    print("MEMORY_RUNTIME_USED:", report["memory_runtime_used"])
    print(
        "EXTERNAL_SECRET_STORE_STARTED:",
        report["external_secret_store_started"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 28/54")
    print("NEXT_AUTHORIZED: DNA-29")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
