#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-31: INTELLIGENCE TEST
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_31_INTELLIGENCE_TEST.py
"""

from __future__ import annotations

import hashlib
import importlib
import json
import math
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

CANON_DNA31: Dict[str, str] = {
    "id": "DNA-31",
    "name": "Intelligence Test",
    "purpose": (
        "Đo generalization, transfer, falsification, calibration, "
        "learning efficiency, recovery, composition và human benefit."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
INTELLIGENCE_TEST_SCHEMA = "SIGMA_INTELLIGENCE_TEST_V1"

CANON_DIMENSIONS = [
    "GENERALIZATION",
    "TRANSFER",
    "FALSIFICATION",
    "CALIBRATION",
    "LEARNING_EFFICIENCY",
    "RECOVERY",
    "COMPOSITION",
    "HUMAN_BENEFIT",
]

DIMENSION_LABELS = {
    "GENERALIZATION": "generalization",
    "TRANSFER": "transfer",
    "FALSIFICATION": "falsification",
    "CALIBRATION": "calibration",
    "LEARNING_EFFICIENCY": "learning efficiency",
    "RECOVERY": "recovery",
    "COMPOSITION": "composition",
    "HUMAN_BENEFIT": "human benefit",
}

INTELLIGENCE_TEST_CONTRACT: Dict[str, Any] = {
    "schema": INTELLIGENCE_TEST_SCHEMA,
    "canonical_dimensions": deepcopy(CANON_DIMENSIONS),
    "dimension_count": 8,
    "all_dimensions_required_for_complete_assessment": True,
    "dimension_record_requires": [
        "dimension",
        "measurement",
        "evidence",
        "passed",
    ],
    "evidence_required": True,
    "measurement_required": True,
    "pass_claim_must_be_explicit": True,
    "missing_dimension_is_not_invented": True,
    "benchmark_executed_by_dna31": False,
    "test_executed_by_dna31": False,
    "learning_runtime_started": False,
    "model_calls_started": False,
    "tool_execution_started": False,
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
    if actual != CANON_DNA31:
        raise RuntimeError(
            "DNA-31_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA31, "actual": actual},
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
            "DNA-31_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    return state


def _install_test_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("intelligence_test")
    expected = {
        "contract": deepcopy(INTELLIGENCE_TEST_CONTRACT),
        "assessments": [],
    }

    if existing is None:
        state["intelligence_test"] = expected
        return state["intelligence_test"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['intelligence_test'] must be a dict"
        )

    if existing.get("contract") != INTELLIGENCE_TEST_CONTRACT:
        raise ValueError(
            "DNA-31_INTELLIGENCE_TEST_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("assessments"), list):
        raise TypeError(
            "intelligence_test['assessments'] must be a list"
        )

    return existing


def _normalize_measurement(value: Any) -> Any:
    if value is None:
        raise ValueError("DNA-31_MEASUREMENT_REQUIRED")

    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("DNA-31_MEASUREMENT_MUST_BE_FINITE")

    if isinstance(value, (dict, list, str, int, float, bool)):
        return deepcopy(value)

    raise TypeError(
        "dimension_record['measurement'] must be JSON-compatible"
    )


def _normalize_dimension_record(
    supplied: Any,
    *,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"intelligence_test_records[{index}] must be a dict"
        )

    required = [
        "dimension",
        "measurement",
        "evidence",
        "passed",
    ]
    missing = [
        field for field in required
        if field not in supplied
    ]
    if missing:
        raise ValueError(
            "DNA-31_DIMENSION_FIELDS_MISSING:"
            + ",".join(missing)
        )

    dimension = supplied["dimension"]
    if not isinstance(dimension, str):
        raise TypeError(
            "dimension_record['dimension'] must be a string"
        )
    dimension = dimension.strip().upper()
    if dimension not in CANON_DIMENSIONS:
        raise ValueError(
            f"DNA-31_UNKNOWN_DIMENSION:{dimension}"
        )

    measurement = _normalize_measurement(
        supplied["measurement"]
    )

    evidence = supplied["evidence"]
    if not isinstance(evidence, list):
        raise TypeError(
            "dimension_record['evidence'] must be a list"
        )
    if not evidence:
        raise ValueError(
            f"DNA-31_EVIDENCE_REQUIRED:{dimension}"
        )
    if any(item is None for item in evidence):
        raise ValueError(
            f"DNA-31_NULL_EVIDENCE_FORBIDDEN:{dimension}"
        )

    passed = supplied["passed"]
    if not isinstance(passed, bool):
        raise TypeError(
            "dimension_record['passed'] must be a bool"
        )

    return {
        "input_index": index,
        "dimension": dimension,
        "canonical_label": DIMENSION_LABELS[dimension],
        "measurement": measurement,
        "measurement_sha256": _sha256_json(measurement),
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(evidence),
        "passed": passed,
    }


def _evaluate_test(
    supplied: Any,
    test_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, list):
        raise TypeError(
            "context['intelligence_test_records'] must be a list"
        )

    records = [
        _normalize_dimension_record(
            item,
            index=index,
        )
        for index, item in enumerate(supplied, start=1)
    ]

    dimensions = [
        record["dimension"] for record in records
    ]
    if len(dimensions) != len(set(dimensions)):
        raise ValueError(
            "DNA-31_DUPLICATE_INTELLIGENCE_DIMENSION"
        )

    present = set(dimensions)
    missing = [
        dimension
        for dimension in CANON_DIMENSIONS
        if dimension not in present
    ]

    extra_count = len(records) - len(present)
    complete = (
        not missing
        and extra_count == 0
        and len(records) == len(CANON_DIMENSIONS)
    )
    all_passed = bool(
        complete
        and all(record["passed"] for record in records)
    )

    failed = [
        record["dimension"]
        for record in records
        if not record["passed"]
    ]

    sequence = len(test_state["assessments"]) + 1
    assessment = {
        "sequence": sequence,
        "assessment_id": (
            f"DNA-31-INTELLIGENCE-{sequence:04d}"
        ),
        "records": deepcopy(records),
        "dimensions_present": sorted(present),
        "missing_dimensions": missing,
        "dimension_count": len(records),
        "complete": complete,
        "failed_dimensions": failed,
        "all_dimensions_passed": all_passed,
        "benchmark_executed_by_dna31": False,
        "test_executed_by_dna31": False,
        "external_action_executed": False,
        "status": (
            "INTELLIGENCE_ASSESSMENT_COMPLETE_PASS"
            if all_passed
            else (
                "INTELLIGENCE_ASSESSMENT_COMPLETE_FAIL"
                if complete
                else "INTELLIGENCE_ASSESSMENT_INCOMPLETE"
            )
        ),
    }

    test_state["assessments"].append(
        deepcopy(assessment)
    )
    return assessment


def dna31_intelligence_test(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Measure supplied evidence across the eight exact Canon dimensions.

    DNA-31 does not itself run a benchmark/test, invoke a model or tool,
    start Learning Runtime, execute external action, or modify Canon.
    """
    assert_exact_canon(core)

    context = (
        deepcopy(payload)
        if isinstance(payload, dict)
        else {"input": deepcopy(payload)}
    )

    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("context['trace'] must be a list")
    trace.append("DNA-31")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    test_state = _install_test_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-31",
            "operation": (
                "INTELLIGENCE_TEST_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "schema": INTELLIGENCE_TEST_SCHEMA,
            "canonical_dimensions": deepcopy(
                CANON_DIMENSIONS
            ),
            "benchmark_executed": False,
            "test_executed": False,
        }
    )

    assessment = _evaluate_test(
        context.get("intelligence_test_records"),
        test_state,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-31",
            "operation": (
                "INTELLIGENCE_DIMENSIONS_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "assessment_id": assessment["assessment_id"],
            "dimension_count": assessment["dimension_count"],
            "complete": assessment["complete"],
            "all_dimensions_passed": (
                assessment["all_dimensions_passed"]
            ),
            "benchmark_executed": False,
            "test_executed": False,
        }
    )

    outputs["DNA-31"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "intelligence_test_contract": deepcopy(
            INTELLIGENCE_TEST_CONTRACT
        ),
        "assessment": deepcopy(assessment),
        "dimension_count": assessment["dimension_count"],
        "complete": assessment["complete"],
        "all_dimensions_passed": (
            assessment["all_dimensions_passed"]
        ),
        "benchmark_executed": False,
        "test_executed": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna31(core54: Core54Like) -> None:
    core = core54.get("DNA-31")
    assert_exact_canon(core)
    core54.bind(
        "DNA-31",
        dna31_intelligence_test,
    )


def _valid_records() -> List[Dict[str, Any]]:
    return [
        {
            "dimension": dimension,
            "measurement": {
                "score": 1.0,
                "unit": "SELF_CHECK_NORMALIZED",
            },
            "evidence": [
                {
                    "evidence_id": f"DNA31-{dimension}-E1",
                    "result": "SUPPORTED",
                }
            ],
            "passed": True,
        }
        for dimension in CANON_DIMENSIONS
    ]


def self_check_dna31(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 31):
        core_id = f"DNA-{index:02d}"
        if not core54.get(core_id).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna31 = core54.get("DNA-31")
    assert_exact_canon(dna31)
    bind_dna31(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 31)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "intelligence_test_records": _valid_records(),
    }

    snapshot = deepcopy(probe)
    result = dna31.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-31"]
    assert output["canonical_gene"] == CANON_DNA31
    assert output["dimension_count"] == 8
    assert output["complete"] is True
    assert output["all_dimensions_passed"] is True
    assert output["benchmark_executed"] is False
    assert output["test_executed"] is False
    assert output["learning_runtime_started"] is False
    assert output["external_action_executed"] is False

    assessment = output["assessment"]
    assert assessment["complete"] is True
    assert assessment["missing_dimensions"] == []
    assert assessment["failed_dimensions"] == []
    assert assessment["all_dimensions_passed"] is True
    assert set(
        assessment["dimensions_present"]
    ) == set(CANON_DIMENSIONS)

    # One failed dimension must fail the complete assessment.
    failed_input = deepcopy(probe)
    failed_input["intelligence_test_records"][0][
        "passed"
    ] = False
    failed = dna31.activate(failed_input)
    failed_assessment = failed[
        "core54_outputs"
    ]["DNA-31"]["assessment"]
    assert failed_assessment["complete"] is True
    assert failed_assessment["all_dimensions_passed"] is False
    assert failed_assessment["failed_dimensions"] == [
        "GENERALIZATION"
    ]

    # Missing a Canon dimension must be incomplete.
    incomplete_input = deepcopy(probe)
    incomplete_input["intelligence_test_records"].pop()
    incomplete = dna31.activate(incomplete_input)
    incomplete_assessment = incomplete[
        "core54_outputs"
    ]["DNA-31"]["assessment"]
    assert incomplete_assessment["complete"] is False
    assert incomplete_assessment[
        "all_dimensions_passed"
    ] is False
    assert incomplete_assessment[
        "missing_dimensions"
    ] == ["HUMAN_BENEFIT"]

    # Duplicate dimensions are invalid.
    duplicate_input = deepcopy(probe)
    duplicate_input["intelligence_test_records"][-1][
        "dimension"
    ] = "GENERALIZATION"
    try:
        dna31.activate(duplicate_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-31_DUPLICATE_INTELLIGENCE_DIMENSION"
        )
    else:
        raise AssertionError(
            "DNA-31_ACCEPTED_DUPLICATE_DIMENSION"
        )

    # Evidence cannot be omitted.
    no_evidence_input = deepcopy(probe)
    no_evidence_input[
        "intelligence_test_records"
    ][0]["evidence"] = []
    try:
        dna31.activate(no_evidence_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-31_EVIDENCE_REQUIRED:GENERALIZATION"
        )
    else:
        raise AssertionError(
            "DNA-31_ACCEPTED_MISSING_EVIDENCE"
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
        "core_id": "DNA-31",
        "canon_mapping": "PASS",
        "generalization": "PASS",
        "transfer": "PASS",
        "falsification": "PASS",
        "calibration": "PASS",
        "learning_efficiency": "PASS",
        "recovery": "PASS",
        "composition": "PASS",
        "human_benefit": "PASS",
        "eight_dimension_gate": "PASS",
        "benchmark_executed": False,
        "test_executed": False,
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
            "DNA-32"
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
                "DNA-31_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = {
            index: importlib.import_module(name)
            for index, name in PRIOR_GENE_MODULES.items()
        }
    except Exception as exc:
        print("DNA-31_FAIL: IMPORT_ERROR")
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

        for index in range(1, 31):
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

        report = self_check_dna31(
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
            for index in range(1, 32)
        ]

    except Exception as exc:
        print("DNA-31_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_31_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("GENERALIZATION:", report["generalization"])
    print("TRANSFER:", report["transfer"])
    print("FALSIFICATION:", report["falsification"])
    print("CALIBRATION:", report["calibration"])
    print(
        "LEARNING_EFFICIENCY:",
        report["learning_efficiency"],
    )
    print("RECOVERY:", report["recovery"])
    print("COMPOSITION:", report["composition"])
    print("HUMAN_BENEFIT:", report["human_benefit"])
    print(
        "EIGHT_DIMENSION_GATE:",
        report["eight_dimension_gate"],
    )
    print(
        "BENCHMARK_EXECUTED:",
        report["benchmark_executed"],
    )
    print(
        "TEST_EXECUTED:",
        report["test_executed"],
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
    print("OFFICIAL_BOUND_CORES: 31/54")
    print("NEXT_AUTHORIZED: DNA-32")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
