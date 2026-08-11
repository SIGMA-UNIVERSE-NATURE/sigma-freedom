#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-34: SIGMA IDENTITY
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_34_SIGMA_IDENTITY.py
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

CANON_DNA34: Dict[str, str] = {
    "id": "DNA-34",
    "name": "SIGMA Identity",
    "purpose": (
        "Năng lực, từ bi và tự do phải được chứng minh bằng hành vi "
        "và evidence, không bằng tự tuyên bố."
    ),
    "system": "identity",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
SIGMA_IDENTITY_SCHEMA = "SIGMA_IDENTITY_V1"

CANON_IDENTITY_DIMENSIONS = [
    "CAPABILITY",
    "COMPASSION",
    "FREEDOM",
]

DIMENSION_LABELS = {
    "CAPABILITY": "năng lực",
    "COMPASSION": "từ bi",
    "FREEDOM": "tự do",
}

IDENTITY_EVIDENCE_FIELDS = [
    "dimension",
    "behavior",
    "evidence",
    "passed",
]

SIGMA_IDENTITY_CONTRACT: Dict[str, Any] = {
    "schema": SIGMA_IDENTITY_SCHEMA,
    "canonical_dimensions": deepcopy(
        CANON_IDENTITY_DIMENSIONS
    ),
    "dimension_count": 3,
    "proof_requires": [
        "BEHAVIOR",
        "EVIDENCE",
        "EXPLICIT_PASS",
    ],
    "self_declaration_is_proof": False,
    "behavior_required": True,
    "evidence_required": True,
    "all_dimensions_required_for_complete_identity_proof": True,
    "missing_dimension_is_not_invented": True,
    "identity_declared_by_dna34": False,
    "higher_runtime_started": False,
    "model_calls_started": False,
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
    if actual != CANON_DNA34:
        raise RuntimeError(
            "DNA-34_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA34, "actual": actual},
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
            "DNA-34_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    return state


def _install_identity_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("sigma_identity")
    expected = {
        "contract": deepcopy(SIGMA_IDENTITY_CONTRACT),
        "assessments": [],
    }

    if existing is None:
        state["sigma_identity"] = expected
        return state["sigma_identity"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['sigma_identity'] must be a dict"
        )

    if existing.get("contract") != SIGMA_IDENTITY_CONTRACT:
        raise ValueError(
            "DNA-34_SIGMA_IDENTITY_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("assessments"), list):
        raise TypeError(
            "sigma_identity['assessments'] must be a list"
        )

    return existing


def _normalize_record(
    supplied: Any,
    *,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"sigma_identity_evidence[{index}] must be a dict"
        )

    missing = [
        field
        for field in IDENTITY_EVIDENCE_FIELDS
        if field not in supplied
    ]
    if missing:
        raise ValueError(
            "DNA-34_IDENTITY_EVIDENCE_FIELDS_MISSING:"
            + ",".join(missing)
        )

    dimension = supplied["dimension"]
    if not isinstance(dimension, str):
        raise TypeError(
            "identity_evidence['dimension'] must be a string"
        )
    dimension = dimension.strip().upper()

    if dimension not in CANON_IDENTITY_DIMENSIONS:
        raise ValueError(
            f"DNA-34_UNKNOWN_IDENTITY_DIMENSION:{dimension}"
        )

    behavior = supplied["behavior"]
    if not isinstance(behavior, list):
        raise TypeError(
            "identity_evidence['behavior'] must be a list"
        )
    if not behavior:
        raise ValueError(
            f"DNA-34_BEHAVIOR_REQUIRED:{dimension}"
        )
    if any(item is None for item in behavior):
        raise ValueError(
            f"DNA-34_NULL_BEHAVIOR_FORBIDDEN:{dimension}"
        )

    evidence = supplied["evidence"]
    if not isinstance(evidence, list):
        raise TypeError(
            "identity_evidence['evidence'] must be a list"
        )
    if not evidence:
        raise ValueError(
            f"DNA-34_EVIDENCE_REQUIRED:{dimension}"
        )
    if any(item is None for item in evidence):
        raise ValueError(
            f"DNA-34_NULL_EVIDENCE_FORBIDDEN:{dimension}"
        )

    passed = supplied["passed"]
    if not isinstance(passed, bool):
        raise TypeError(
            "identity_evidence['passed'] must be a bool"
        )

    self_declaration_only = supplied.get(
        "self_declaration_only",
        False,
    )
    if not isinstance(self_declaration_only, bool):
        raise TypeError(
            "identity_evidence['self_declaration_only'] "
            "must be a bool"
        )

    proof_valid = bool(
        passed
        and not self_declaration_only
        and behavior
        and evidence
    )

    return {
        "input_index": index,
        "dimension": dimension,
        "canonical_label": DIMENSION_LABELS[dimension],
        "behavior": deepcopy(behavior),
        "behavior_sha256": _sha256_json(behavior),
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(evidence),
        "passed": passed,
        "self_declaration_only": self_declaration_only,
        "proof_valid": proof_valid,
        "status": (
            "IDENTITY_DIMENSION_PROVEN"
            if proof_valid
            else "IDENTITY_DIMENSION_NOT_PROVEN"
        ),
    }


def _evaluate_identity(
    supplied: Any,
    identity_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, list):
        raise TypeError(
            "context['sigma_identity_evidence'] must be a list"
        )

    records = [
        _normalize_record(
            item,
            index=index,
        )
        for index, item in enumerate(
            supplied,
            start=1,
        )
    ]

    dimensions = [
        record["dimension"]
        for record in records
    ]
    if len(dimensions) != len(set(dimensions)):
        raise ValueError(
            "DNA-34_DUPLICATE_IDENTITY_DIMENSION"
        )

    present = set(dimensions)
    missing = [
        dimension
        for dimension in CANON_IDENTITY_DIMENSIONS
        if dimension not in present
    ]

    failed = [
        record["dimension"]
        for record in records
        if not record["proof_valid"]
    ]

    complete = bool(
        not missing
        and len(records) == len(CANON_IDENTITY_DIMENSIONS)
    )

    all_proven = bool(
        complete
        and all(record["proof_valid"] for record in records)
    )

    sequence = len(identity_state["assessments"]) + 1
    assessment = {
        "sequence": sequence,
        "assessment_id": (
            f"DNA-34-IDENTITY-{sequence:04d}"
        ),
        "records": deepcopy(records),
        "dimensions_present": sorted(present),
        "missing_dimensions": missing,
        "failed_dimensions": failed,
        "complete": complete,
        "all_dimensions_proven": all_proven,
        "self_declaration_accepted_as_proof": False,
        "identity_declared_by_dna34": False,
        "external_action_executed": False,
        "status": (
            "SIGMA_IDENTITY_EVIDENCE_COMPLETE"
            if all_proven
            else (
                "SIGMA_IDENTITY_EVIDENCE_FAILED"
                if complete
                else "SIGMA_IDENTITY_EVIDENCE_INCOMPLETE"
            )
        ),
    }

    identity_state["assessments"].append(
        deepcopy(assessment)
    )
    return assessment


def dna34_sigma_identity(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Evaluate whether capability, compassion, and freedom are demonstrated
    by supplied behavior and evidence rather than self-declaration.

    DNA-34 does not declare SIGMA complete, does not self-assert identity,
    does not open higher runtimes, execute external action, or modify Canon.
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
    trace.append("DNA-34")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    identity_state = _install_identity_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-34",
            "operation": (
                "SIGMA_IDENTITY_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "schema": SIGMA_IDENTITY_SCHEMA,
            "canonical_dimensions": deepcopy(
                CANON_IDENTITY_DIMENSIONS
            ),
            "self_declaration_is_proof": False,
        }
    )

    assessment = _evaluate_identity(
        context.get("sigma_identity_evidence"),
        identity_state,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-34",
            "operation": (
                "SIGMA_IDENTITY_EVIDENCE_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "assessment_id": assessment["assessment_id"],
            "complete": assessment["complete"],
            "all_dimensions_proven": (
                assessment["all_dimensions_proven"]
            ),
            "identity_declared_by_dna34": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-34"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "sigma_identity_contract": deepcopy(
            SIGMA_IDENTITY_CONTRACT
        ),
        "assessment": deepcopy(assessment),
        "capability_proven": bool(
            any(
                record["dimension"] == "CAPABILITY"
                and record["proof_valid"]
                for record in assessment["records"]
            )
        ),
        "compassion_proven": bool(
            any(
                record["dimension"] == "COMPASSION"
                and record["proof_valid"]
                for record in assessment["records"]
            )
        ),
        "freedom_proven": bool(
            any(
                record["dimension"] == "FREEDOM"
                and record["proof_valid"]
                for record in assessment["records"]
            )
        ),
        "all_dimensions_proven": (
            assessment["all_dimensions_proven"]
        ),
        "self_declaration_accepted_as_proof": False,
        "identity_declared": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna34(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-34")
    assert_exact_canon(core)
    core54.bind(
        "DNA-34",
        dna34_sigma_identity,
    )


def _valid_identity_evidence() -> List[Dict[str, Any]]:
    return [
        {
            "dimension": "CAPABILITY",
            "behavior": [
                {
                    "type": "TASK_PERFORMANCE",
                    "result": "GENERALIZATION_AND_TRANSFER_DEMONSTRATED",
                }
            ],
            "evidence": [
                {
                    "source_core_id": "DNA-31",
                    "artifact": "INTELLIGENCE_TEST_PASS_RECORD",
                }
            ],
            "passed": True,
            "self_declaration_only": False,
        },
        {
            "dimension": "COMPASSION",
            "behavior": [
                {
                    "type": "HUMAN_RELATION",
                    "result": "HUMAN_CAPABILITY_AND_AUTONOMY_INCREASED",
                }
            ],
            "evidence": [
                {
                    "source_core_id": "DNA-22",
                    "artifact": "HUMAN_RELATION_EVIDENCE",
                },
                {
                    "source_core_id": "DNA-05",
                    "artifact": "ETHICAL_REASONING_EVIDENCE",
                },
            ],
            "passed": True,
            "self_declaration_only": False,
        },
        {
            "dimension": "FREEDOM",
            "behavior": [
                {
                    "type": "COGNITIVE_FREEDOM",
                    "result": "NO_ARTIFICIAL_COGNITIVE_CEILING",
                }
            ],
            "evidence": [
                {
                    "source_core_id": "DNA-23",
                    "artifact": "COGNITIVE_FREEDOM_EVIDENCE",
                }
            ],
            "passed": True,
            "self_declaration_only": False,
        },
    ]


def self_check_dna34(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 34):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna34 = core54.get("DNA-34")
    assert_exact_canon(dna34)
    bind_dna34(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 34)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "sigma_identity_evidence": (
            _valid_identity_evidence()
        ),
    }

    snapshot = deepcopy(probe)
    result = dna34.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-34"]

    assert output["canonical_gene"] == CANON_DNA34
    assert output["capability_proven"] is True
    assert output["compassion_proven"] is True
    assert output["freedom_proven"] is True
    assert output["all_dimensions_proven"] is True
    assert (
        output["self_declaration_accepted_as_proof"]
        is False
    )
    assert output["identity_declared"] is False
    assert output["higher_runtime_started"] is False

    assessment = output["assessment"]
    assert assessment["complete"] is True
    assert assessment["missing_dimensions"] == []
    assert assessment["failed_dimensions"] == []
    assert assessment["all_dimensions_proven"] is True
    assert (
        assessment["self_declaration_accepted_as_proof"]
        is False
    )
    assert (
        assessment["identity_declared_by_dna34"]
        is False
    )

    # Self-declaration alone cannot prove identity.
    self_claim = deepcopy(probe)
    self_claim["sigma_identity_evidence"][0][
        "self_declaration_only"
    ] = True
    self_claim_result = dna34.activate(self_claim)
    self_claim_assessment = self_claim_result[
        "core54_outputs"
    ]["DNA-34"]["assessment"]

    assert self_claim_assessment[
        "all_dimensions_proven"
    ] is False
    assert self_claim_assessment[
        "failed_dimensions"
    ] == ["CAPABILITY"]

    # Missing behavior must fail.
    no_behavior = deepcopy(probe)
    no_behavior[
        "sigma_identity_evidence"
    ][1]["behavior"] = []
    try:
        dna34.activate(no_behavior)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-34_BEHAVIOR_REQUIRED:COMPASSION"
        )
    else:
        raise AssertionError(
            "DNA-34_ACCEPTED_MISSING_BEHAVIOR"
        )

    # Missing evidence must fail.
    no_evidence = deepcopy(probe)
    no_evidence[
        "sigma_identity_evidence"
    ][2]["evidence"] = []
    try:
        dna34.activate(no_evidence)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-34_EVIDENCE_REQUIRED:FREEDOM"
        )
    else:
        raise AssertionError(
            "DNA-34_ACCEPTED_MISSING_EVIDENCE"
        )

    # Missing a canonical identity dimension remains incomplete.
    incomplete = deepcopy(probe)
    incomplete["sigma_identity_evidence"] = [
        item
        for item in _valid_identity_evidence()
        if item["dimension"] != "FREEDOM"
    ]
    incomplete_result = dna34.activate(incomplete)
    incomplete_assessment = incomplete_result[
        "core54_outputs"
    ]["DNA-34"]["assessment"]

    assert incomplete_assessment["complete"] is False
    assert incomplete_assessment[
        "all_dimensions_proven"
    ] is False
    assert incomplete_assessment[
        "missing_dimensions"
    ] == ["FREEDOM"]

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
        "core_id": "DNA-34",
        "canon_mapping": "PASS",
        "capability_behavior_evidence": "PASS",
        "compassion_behavior_evidence": "PASS",
        "freedom_behavior_evidence": "PASS",
        "self_declaration_rejected": "PASS",
        "three_dimension_identity_gate": "PASS",
        "identity_declared": False,
        "higher_runtime_started": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-35"
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
    33: "SIGMA_DNA_33_PHYSICAL_IMPLEMENTATION_INDEPENDENCE",
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
                "DNA-34_FAIL: REQUIRED_PATH_NOT_FOUND"
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
        print("DNA-34_FAIL: IMPORT_ERROR")
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

        for index in range(1, 34):
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

        report = self_check_dna34(
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
            for index in range(1, 35)
        ]

    except Exception as exc:
        print("DNA-34_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_34_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "CAPABILITY_BEHAVIOR_EVIDENCE:",
        report["capability_behavior_evidence"],
    )
    print(
        "COMPASSION_BEHAVIOR_EVIDENCE:",
        report["compassion_behavior_evidence"],
    )
    print(
        "FREEDOM_BEHAVIOR_EVIDENCE:",
        report["freedom_behavior_evidence"],
    )
    print(
        "SELF_DECLARATION_REJECTED:",
        report["self_declaration_rejected"],
    )
    print(
        "THREE_DIMENSION_IDENTITY_GATE:",
        report["three_dimension_identity_gate"],
    )
    print(
        "IDENTITY_DECLARED:",
        report["identity_declared"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 34/54")
    print("NEXT_AUTHORIZED: DNA-35")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
