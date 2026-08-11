#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-18: MODEL EVOLUTION
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_18_MODEL_EVOLUTION.py
"""

from __future__ import annotations

import hashlib
import json
import string
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol, Tuple


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

CANON_DNA18: Dict[str, str] = {
    "id": "DNA-18",
    "name": "Model Evolution",
    "purpose": (
        "Model/adapters mới phải qua benchmark độc lập, held-out tests, "
        "promotion và rollback."
    ),
    "system": "evolution",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
VERIFICATION_WALL_SCHEMA = (
    "SIGMA_INDEPENDENT_VERIFICATION_WALL_V1"
)
TWO_LEVELS_SCHEMA = "SIGMA_TWO_LEVELS_OF_LEARNING_V1"
MODEL_EVOLUTION_SCHEMA = "SIGMA_MODEL_EVOLUTION_V1"

SUPPORTED_CANDIDATE_TYPES = [
    "MODEL",
    "ADAPTER",
]

REQUIRED_GATES = [
    "INDEPENDENT_BENCHMARK",
    "HELD_OUT_TESTS",
    "PROMOTION",
    "ROLLBACK",
]

CANDIDATE_IDENTITY_FIELDS = [
    "candidate_id",
    "candidate_type",
    "producer_id",
    "baseline_version",
    "candidate_version",
    "artifact_sha256",
]

INDEPENDENT_BENCHMARK_FIELDS = [
    "benchmark_id",
    "runner_id",
    "runner_independent",
    "independence_basis",
    "candidate_sha256",
    "suite",
    "metrics",
    "evidence",
    "passed",
]

HELD_OUT_TEST_FIELDS = [
    "test_id",
    "candidate_sha256",
    "dataset_id",
    "held_out",
    "training_excluded",
    "results",
    "evidence",
    "passed",
]

PROMOTION_FIELDS = [
    "decision_id",
    "candidate_sha256",
    "approver_id",
    "criteria",
    "approved",
]

ROLLBACK_FIELDS = [
    "rollback_id",
    "candidate_sha256",
    "ready",
    "target_version",
    "procedure",
    "trigger_conditions",
]

MODEL_EVOLUTION_CONTRACT: Dict[str, Any] = {
    "schema": MODEL_EVOLUTION_SCHEMA,
    "candidate_types": deepcopy(
        SUPPORTED_CANDIDATE_TYPES
    ),
    "required_gates": deepcopy(REQUIRED_GATES),
    "all_gates_required": True,
    "independent_benchmark_required": True,
    "held_out_tests_required": True,
    "promotion_gate_required": True,
    "rollback_readiness_required": True,
    "candidate_binding": {
        "method": "CANONICAL_JSON_SHA256",
        "bound_objects": [
            "INDEPENDENT_BENCHMARK",
            "HELD_OUT_TESTS",
            "PROMOTION",
            "ROLLBACK",
        ],
        "canon_status": (
            "IMPLEMENTATION_ENCODING_NOT_CANON_FIELD"
        ),
    },
    "dna17_neural_evidence_alone_sufficient": False,
    "benchmark_execution_started": False,
    "held_out_test_execution_started": False,
    "promotion_executed_by_dna18": False,
    "rollback_executed_by_dna18": False,
    "model_or_adapter_modified_by_dna18": False,
    "learning_runtime_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA09_AND_DNA17_BINDING"
    ),
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


def _is_sha256(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(
            character in string.hexdigits
            for character in value
        )
    )


def _non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _non_empty_list(value: Any) -> bool:
    return isinstance(value, list) and len(value) > 0


def _non_empty_mapping(value: Any) -> bool:
    return isinstance(value, dict) and len(value) > 0


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA18:
        raise RuntimeError(
            "DNA-18_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA18,
                    "actual": actual,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Tuple[
    Dict[str, Any],
    Dict[str, Any],
    Dict[str, Any],
]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-18_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    verification_wall = state.get(
        "independent_verification_wall"
    )
    if not isinstance(verification_wall, dict):
        raise RuntimeError(
            "DNA-09_INDEPENDENT_VERIFICATION_WALL_REQUIRED"
        )

    verification_contract = verification_wall.get(
        "contract"
    )
    if not isinstance(verification_contract, dict):
        raise RuntimeError(
            "DNA-09_VERIFICATION_WALL_CONTRACT_REQUIRED"
        )

    if verification_contract.get("schema") != (
        VERIFICATION_WALL_SCHEMA
    ):
        raise ValueError(
            "DNA-18_VERIFICATION_WALL_SCHEMA_MISMATCH:"
            f"{verification_contract.get('schema')!r}"
        )

    two_levels = state.get("two_levels_of_learning")
    if not isinstance(two_levels, dict):
        raise RuntimeError(
            "DNA-17_TWO_LEVELS_OF_LEARNING_REQUIRED"
        )

    two_levels_contract = two_levels.get("contract")
    if not isinstance(two_levels_contract, dict):
        raise RuntimeError(
            "DNA-17_TWO_LEVELS_CONTRACT_REQUIRED"
        )

    if two_levels_contract.get("schema") != (
        TWO_LEVELS_SCHEMA
    ):
        raise ValueError(
            "DNA-18_TWO_LEVELS_SCHEMA_MISMATCH:"
            f"{two_levels_contract.get('schema')!r}"
        )

    if not isinstance(
        two_levels.get("classifications"),
        list,
    ):
        raise TypeError(
            "two_levels_of_learning['classifications'] "
            "must be a list"
        )

    if not isinstance(
        two_levels.get("neural_change_records"),
        list,
    ):
        raise TypeError(
            "two_levels_of_learning['neural_change_records'] "
            "must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-17_OUTPUT_REQUIRED")

    dna17_output = outputs.get("DNA-17")
    if not isinstance(dna17_output, dict):
        raise RuntimeError("DNA-17_OUTPUT_REQUIRED")

    return state, verification_wall, two_levels


def _install_model_evolution_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("model_evolution")

    expected = {
        "contract": deepcopy(
            MODEL_EVOLUTION_CONTRACT
        ),
        "evaluations": [],
    }

    if existing is None:
        state["model_evolution"] = expected
        return state["model_evolution"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['model_evolution'] "
            "must be a dict"
        )

    if existing.get("contract") != (
        MODEL_EVOLUTION_CONTRACT
    ):
        raise ValueError(
            "DNA-18_MODEL_EVOLUTION_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("evaluations"), list):
        raise TypeError(
            "model_evolution['evaluations'] must be a list"
        )

    return existing


def _candidate_identity(
    candidate: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        field: deepcopy(candidate.get(field))
        for field in CANDIDATE_IDENTITY_FIELDS
    }


def _validate_candidate_types(
    candidate: Dict[str, Any],
) -> None:
    text_fields = [
        "candidate_id",
        "candidate_type",
        "producer_id",
        "baseline_version",
        "candidate_version",
        "artifact_sha256",
    ]
    for field in text_fields:
        if field in candidate and not isinstance(
            candidate[field],
            str,
        ):
            raise TypeError(
                f"model_evolution_candidate['{field}'] "
                "must be a string"
            )

    nested_fields = [
        "independent_benchmark",
        "held_out_tests",
        "promotion",
        "rollback",
    ]
    for field in nested_fields:
        if field in candidate and not isinstance(
            candidate[field],
            dict,
        ):
            raise TypeError(
                f"model_evolution_candidate['{field}'] "
                "must be a dict"
            )


def _missing_candidate_fields(
    candidate: Dict[str, Any],
) -> List[str]:
    required = [
        *CANDIDATE_IDENTITY_FIELDS,
        "independent_benchmark",
        "held_out_tests",
        "promotion",
        "rollback",
    ]
    return [
        field
        for field in required
        if field not in candidate
    ]


def _gate_result(
    *,
    gate: str,
    passed: bool,
    reasons: List[str],
    record: Any,
) -> Dict[str, Any]:
    return {
        "gate": gate,
        "passed": passed,
        "reasons": list(dict.fromkeys(reasons)),
        "record": deepcopy(record),
    }


def _evaluate_independent_benchmark(
    record: Any,
    *,
    producer_id: Any,
    candidate_sha256: Optional[str],
) -> Dict[str, Any]:
    reasons: List[str] = []

    if not isinstance(record, dict):
        return _gate_result(
            gate="INDEPENDENT_BENCHMARK",
            passed=False,
            reasons=["INDEPENDENT_BENCHMARK_RECORD_REQUIRED"],
            record=record,
        )

    missing = [
        field
        for field in INDEPENDENT_BENCHMARK_FIELDS
        if field not in record
    ]
    if missing:
        reasons.append(
            "INDEPENDENT_BENCHMARK_FIELDS_MISSING"
        )

    for field in (
        "runner_independent",
        "passed",
    ):
        if field in record and not isinstance(
            record[field],
            bool,
        ):
            raise TypeError(
                f"independent_benchmark['{field}'] "
                "must be a bool"
            )

    for field in (
        "benchmark_id",
        "runner_id",
        "candidate_sha256",
        "suite",
    ):
        if field in record and not isinstance(
            record[field],
            str,
        ):
            raise TypeError(
                f"independent_benchmark['{field}'] "
                "must be a string"
            )

    for field in (
        "independence_basis",
        "evidence",
    ):
        if field in record and not isinstance(
            record[field],
            list,
        ):
            raise TypeError(
                f"independent_benchmark['{field}'] "
                "must be a list"
            )

    if "metrics" in record and not isinstance(
        record["metrics"],
        dict,
    ):
        raise TypeError(
            "independent_benchmark['metrics'] must be a dict"
        )

    runner_id = record.get("runner_id")
    if not (
        _non_empty_text(producer_id)
        and _non_empty_text(runner_id)
        and runner_id != producer_id
    ):
        reasons.append(
            "BENCHMARK_RUNNER_NOT_SEPARATED_FROM_PRODUCER"
        )

    if record.get("runner_independent") is not True:
        reasons.append(
            "INDEPENDENT_BENCHMARK_REQUIRED"
        )

    if not _non_empty_list(
        record.get("independence_basis")
    ):
        reasons.append(
            "BENCHMARK_INDEPENDENCE_BASIS_REQUIRED"
        )

    if (
        candidate_sha256 is None
        or record.get("candidate_sha256")
        != candidate_sha256
    ):
        reasons.append(
            "BENCHMARK_NOT_BOUND_TO_CANDIDATE"
        )

    if not _non_empty_text(record.get("suite")):
        reasons.append("BENCHMARK_SUITE_REQUIRED")

    if not _non_empty_mapping(record.get("metrics")):
        reasons.append("BENCHMARK_METRICS_REQUIRED")

    if not _non_empty_list(record.get("evidence")):
        reasons.append("BENCHMARK_EVIDENCE_REQUIRED")

    if record.get("passed") is not True:
        reasons.append("BENCHMARK_PASS_REQUIRED")

    unique = list(dict.fromkeys(reasons))
    return _gate_result(
        gate="INDEPENDENT_BENCHMARK",
        passed=not unique,
        reasons=unique,
        record=record,
    )


def _evaluate_held_out_tests(
    record: Any,
    *,
    candidate_sha256: Optional[str],
) -> Dict[str, Any]:
    reasons: List[str] = []

    if not isinstance(record, dict):
        return _gate_result(
            gate="HELD_OUT_TESTS",
            passed=False,
            reasons=["HELD_OUT_TEST_RECORD_REQUIRED"],
            record=record,
        )

    missing = [
        field
        for field in HELD_OUT_TEST_FIELDS
        if field not in record
    ]
    if missing:
        reasons.append("HELD_OUT_TEST_FIELDS_MISSING")

    for field in (
        "held_out",
        "training_excluded",
        "passed",
    ):
        if field in record and not isinstance(
            record[field],
            bool,
        ):
            raise TypeError(
                f"held_out_tests['{field}'] must be a bool"
            )

    for field in (
        "test_id",
        "candidate_sha256",
        "dataset_id",
    ):
        if field in record and not isinstance(
            record[field],
            str,
        ):
            raise TypeError(
                f"held_out_tests['{field}'] must be a string"
            )

    if "evidence" in record and not isinstance(
        record["evidence"],
        list,
    ):
        raise TypeError(
            "held_out_tests['evidence'] must be a list"
        )

    if "results" in record and not isinstance(
        record["results"],
        (dict, list),
    ):
        raise TypeError(
            "held_out_tests['results'] must be a dict or list"
        )

    if (
        candidate_sha256 is None
        or record.get("candidate_sha256")
        != candidate_sha256
    ):
        reasons.append(
            "HELD_OUT_TEST_NOT_BOUND_TO_CANDIDATE"
        )

    if not _non_empty_text(record.get("dataset_id")):
        reasons.append("HELD_OUT_DATASET_REQUIRED")

    if record.get("held_out") is not True:
        reasons.append("HELD_OUT_STATUS_REQUIRED")

    if record.get("training_excluded") is not True:
        reasons.append(
            "TRAINING_EXCLUSION_REQUIRED"
        )

    results = record.get("results")
    results_present = (
        _non_empty_mapping(results)
        or _non_empty_list(results)
    )
    if not results_present:
        reasons.append("HELD_OUT_RESULTS_REQUIRED")

    if not _non_empty_list(record.get("evidence")):
        reasons.append("HELD_OUT_EVIDENCE_REQUIRED")

    if record.get("passed") is not True:
        reasons.append("HELD_OUT_PASS_REQUIRED")

    unique = list(dict.fromkeys(reasons))
    return _gate_result(
        gate="HELD_OUT_TESTS",
        passed=not unique,
        reasons=unique,
        record=record,
    )


def _evaluate_promotion(
    record: Any,
    *,
    candidate_sha256: Optional[str],
) -> Dict[str, Any]:
    reasons: List[str] = []

    if not isinstance(record, dict):
        return _gate_result(
            gate="PROMOTION",
            passed=False,
            reasons=["PROMOTION_RECORD_REQUIRED"],
            record=record,
        )

    missing = [
        field
        for field in PROMOTION_FIELDS
        if field not in record
    ]
    if missing:
        reasons.append("PROMOTION_FIELDS_MISSING")

    if "approved" in record and not isinstance(
        record["approved"],
        bool,
    ):
        raise TypeError(
            "promotion['approved'] must be a bool"
        )

    for field in (
        "decision_id",
        "candidate_sha256",
        "approver_id",
    ):
        if field in record and not isinstance(
            record[field],
            str,
        ):
            raise TypeError(
                f"promotion['{field}'] must be a string"
            )

    if "criteria" in record and not isinstance(
        record["criteria"],
        list,
    ):
        raise TypeError(
            "promotion['criteria'] must be a list"
        )

    if (
        candidate_sha256 is None
        or record.get("candidate_sha256")
        != candidate_sha256
    ):
        reasons.append(
            "PROMOTION_NOT_BOUND_TO_CANDIDATE"
        )

    if not _non_empty_text(record.get("decision_id")):
        reasons.append("PROMOTION_DECISION_ID_REQUIRED")

    if not _non_empty_text(record.get("approver_id")):
        reasons.append("PROMOTION_APPROVER_REQUIRED")

    if not _non_empty_list(record.get("criteria")):
        reasons.append("PROMOTION_CRITERIA_REQUIRED")

    if record.get("approved") is not True:
        reasons.append("PROMOTION_APPROVAL_REQUIRED")

    unique = list(dict.fromkeys(reasons))
    return _gate_result(
        gate="PROMOTION",
        passed=not unique,
        reasons=unique,
        record=record,
    )


def _evaluate_rollback(
    record: Any,
    *,
    candidate_sha256: Optional[str],
    baseline_version: Any,
) -> Dict[str, Any]:
    reasons: List[str] = []

    if not isinstance(record, dict):
        return _gate_result(
            gate="ROLLBACK",
            passed=False,
            reasons=["ROLLBACK_RECORD_REQUIRED"],
            record=record,
        )

    missing = [
        field
        for field in ROLLBACK_FIELDS
        if field not in record
    ]
    if missing:
        reasons.append("ROLLBACK_FIELDS_MISSING")

    if "ready" in record and not isinstance(
        record["ready"],
        bool,
    ):
        raise TypeError(
            "rollback['ready'] must be a bool"
        )

    for field in (
        "rollback_id",
        "candidate_sha256",
        "target_version",
        "procedure",
    ):
        if field in record and not isinstance(
            record[field],
            str,
        ):
            raise TypeError(
                f"rollback['{field}'] must be a string"
            )

    if (
        "trigger_conditions" in record
        and not isinstance(
            record["trigger_conditions"],
            list,
        )
    ):
        raise TypeError(
            "rollback['trigger_conditions'] must be a list"
        )

    if (
        candidate_sha256 is None
        or record.get("candidate_sha256")
        != candidate_sha256
    ):
        reasons.append(
            "ROLLBACK_NOT_BOUND_TO_CANDIDATE"
        )

    if not _non_empty_text(record.get("rollback_id")):
        reasons.append("ROLLBACK_ID_REQUIRED")

    if record.get("ready") is not True:
        reasons.append("ROLLBACK_READINESS_REQUIRED")

    if (
        not _non_empty_text(baseline_version)
        or record.get("target_version")
        != baseline_version
    ):
        reasons.append(
            "ROLLBACK_TARGET_MUST_MATCH_BASELINE"
        )

    if not _non_empty_text(record.get("procedure")):
        reasons.append("ROLLBACK_PROCEDURE_REQUIRED")

    if not _non_empty_list(
        record.get("trigger_conditions")
    ):
        reasons.append(
            "ROLLBACK_TRIGGER_CONDITIONS_REQUIRED"
        )

    unique = list(dict.fromkeys(reasons))
    return _gate_result(
        gate="ROLLBACK",
        passed=not unique,
        reasons=unique,
        record=record,
    )


def _evaluate_model_candidate(
    supplied: Any,
    model_evolution: Dict[str, Any],
    two_levels: Dict[str, Any],
) -> Dict[str, Any]:
    reasons: List[str] = []

    if not isinstance(supplied, dict):
        candidate: Dict[str, Any] = {}
        reasons.append(
            "MODEL_OR_ADAPTER_CANDIDATE_REQUIRED"
        )
    else:
        candidate = deepcopy(supplied)
        _validate_candidate_types(candidate)

    missing_fields = _missing_candidate_fields(candidate)
    if missing_fields:
        reasons.append("CANDIDATE_FIELDS_MISSING")

    identity = _candidate_identity(candidate)

    for field in (
        "candidate_id",
        "producer_id",
        "baseline_version",
        "candidate_version",
    ):
        if not _non_empty_text(identity.get(field)):
            reasons.append(
                f"{field.upper()}_REQUIRED"
            )

    candidate_type = identity.get("candidate_type")
    type_supported = (
        candidate_type in SUPPORTED_CANDIDATE_TYPES
    )
    if not type_supported:
        reasons.append(
            "CANDIDATE_TYPE_MUST_BE_MODEL_OR_ADAPTER"
        )

    if (
        _non_empty_text(identity.get("baseline_version"))
        and identity.get("candidate_version")
        == identity.get("baseline_version")
    ):
        reasons.append(
            "CANDIDATE_VERSION_MUST_DIFFER_FROM_BASELINE"
        )

    if not _is_sha256(identity.get("artifact_sha256")):
        reasons.append(
            "ARTIFACT_SHA256_REQUIRED"
        )

    identity_complete = not any(
        field not in candidate
        for field in CANDIDATE_IDENTITY_FIELDS
    ) and not any(
        reason
        in {
            "CANDIDATE_ID_REQUIRED",
            "CANDIDATE_TYPE_MUST_BE_MODEL_OR_ADAPTER",
            "PRODUCER_ID_REQUIRED",
            "BASELINE_VERSION_REQUIRED",
            "CANDIDATE_VERSION_REQUIRED",
            "CANDIDATE_VERSION_MUST_DIFFER_FROM_BASELINE",
            "ARTIFACT_SHA256_REQUIRED",
        }
        for reason in reasons
    )

    candidate_sha256 = (
        _sha256_json(identity)
        if identity_complete
        else None
    )

    benchmark = _evaluate_independent_benchmark(
        candidate.get("independent_benchmark"),
        producer_id=identity.get("producer_id"),
        candidate_sha256=candidate_sha256,
    )
    held_out = _evaluate_held_out_tests(
        candidate.get("held_out_tests"),
        candidate_sha256=candidate_sha256,
    )
    promotion = _evaluate_promotion(
        candidate.get("promotion"),
        candidate_sha256=candidate_sha256,
    )
    rollback = _evaluate_rollback(
        candidate.get("rollback"),
        candidate_sha256=candidate_sha256,
        baseline_version=identity.get(
            "baseline_version"
        ),
    )

    gates = {
        "independent_benchmark": benchmark,
        "held_out_tests": held_out,
        "promotion": promotion,
        "rollback": rollback,
    }

    for gate_result in gates.values():
        reasons.extend(gate_result["reasons"])

    all_gates_passed = all(
        gate_result["passed"]
        for gate_result in gates.values()
    )

    # DNA-17 evidence is visible but cannot replace any DNA-18 gate.
    neural_record_ids = [
        record.get("record_id")
        for record in two_levels["neural_change_records"]
        if isinstance(record, dict)
    ]

    unique_reasons = list(dict.fromkeys(reasons))
    eligible = bool(
        identity_complete
        and type_supported
        and all_gates_passed
        and not unique_reasons
    )

    sequence = len(model_evolution["evaluations"]) + 1
    evaluation = {
        "sequence": sequence,
        "evaluation_id": (
            f"DNA-18-EVOLUTION-{sequence:04d}"
        ),
        "candidate_identity": identity,
        "candidate_sha256": candidate_sha256,
        "candidate_type_supported": type_supported,
        "missing_fields": missing_fields,
        "gates": gates,
        "all_gates_passed": all_gates_passed,
        "dna17_neural_record_ids_observed": neural_record_ids,
        "dna17_neural_evidence_used_as_gate_substitute": False,
        "promotion_eligible": eligible,
        "benchmark_executed_by_dna18": False,
        "held_out_tests_executed_by_dna18": False,
        "promotion_executed_by_dna18": False,
        "rollback_executed_by_dna18": False,
        "model_or_adapter_modified_by_dna18": False,
        "rejection_reasons": unique_reasons,
        "status": (
            "ELIGIBLE_FOR_CONTROLLED_PROMOTION"
            if eligible
            else "MODEL_EVOLUTION_BLOCKED"
        ),
    }
    model_evolution["evaluations"].append(evaluation)
    return evaluation


def dna18_model_evolution(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Evaluate whether a supplied model/adapter candidate has passed all four
    exact Canon gates: independent benchmark, held-out tests, promotion,
    and rollback.

    DNA-18 does not run a benchmark, run held-out tests, promote or roll
    back a model/adapter, modify persistent capability, start Learning
    Runtime, invoke a model, execute external action, or modify Canon.
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
    trace.append("DNA-18")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    (
        state,
        _verification_wall,
        two_levels,
    ) = _validate_dependencies(context)

    model_evolution = _install_model_evolution_state(
        state
    )

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-18",
            "operation": (
                "MODEL_EVOLUTION_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "model_evolution_schema": MODEL_EVOLUTION_SCHEMA,
            "required_gates": deepcopy(REQUIRED_GATES),
            "benchmark_executed": False,
            "promotion_executed": False,
            "rollback_executed": False,
        }
    )

    evaluation = _evaluate_model_candidate(
        context.get("model_evolution_candidate"),
        model_evolution,
        two_levels,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-18",
            "operation": (
                "MODEL_EVOLUTION_GATES_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "evaluation_id": evaluation["evaluation_id"],
            "all_gates_passed": (
                evaluation["all_gates_passed"]
            ),
            "promotion_eligible": (
                evaluation["promotion_eligible"]
            ),
            "benchmark_executed": False,
            "promotion_executed": False,
            "rollback_executed": False,
        }
    )

    outputs["DNA-18"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "model_evolution_contract": deepcopy(
            MODEL_EVOLUTION_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "all_gates_passed": (
            evaluation["all_gates_passed"]
        ),
        "promotion_eligible": (
            evaluation["promotion_eligible"]
        ),
        "benchmark_executed": False,
        "held_out_tests_executed": False,
        "promotion_executed": False,
        "rollback_executed": False,
        "model_or_adapter_modified": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna18(core54: Core54Like) -> None:
    core = core54.get("DNA-18")
    assert_exact_canon(core)
    core54.bind(
        "DNA-18",
        dna18_model_evolution,
    )


def _run_through(
    core54: Core54Like,
    context: Dict[str, Any],
    final_index: int,
) -> Dict[str, Any]:
    result = deepcopy(context)
    for index in range(1, final_index + 1):
        result = core54.get(
            f"DNA-{index:02d}"
        ).activate(result)
    return result


def _candidate_binding_identity(
    *,
    candidate_id: str,
    candidate_type: str,
    producer_id: str,
    baseline_version: str,
    candidate_version: str,
    artifact_sha256: str,
) -> Dict[str, Any]:
    return {
        "candidate_id": candidate_id,
        "candidate_type": candidate_type,
        "producer_id": producer_id,
        "baseline_version": baseline_version,
        "candidate_version": candidate_version,
        "artifact_sha256": artifact_sha256,
    }


def _valid_model_evolution_candidate(
    candidate_type: str = "MODEL",
) -> Dict[str, Any]:
    identity = _candidate_binding_identity(
        candidate_id=(
            "MODEL-DNA18-01"
            if candidate_type == "MODEL"
            else "ADAPTER-DNA18-01"
        ),
        candidate_type=candidate_type,
        producer_id="PRODUCER-DNA18",
        baseline_version="VERSION-1",
        candidate_version="VERSION-2",
        artifact_sha256=hashlib.sha256(
            (
                f"DNA18-{candidate_type}-ARTIFACT"
            ).encode("utf-8")
        ).hexdigest(),
    )
    candidate_sha256 = _sha256_json(identity)

    return {
        **deepcopy(identity),
        "independent_benchmark": {
            "benchmark_id": "BENCHMARK-DNA18-01",
            "runner_id": "INDEPENDENT-RUNNER-DNA18",
            "runner_independent": True,
            "independence_basis": [
                "SEPARATE_ROLE",
                "NO_SHARED_DECISION_AUTHORITY",
            ],
            "candidate_sha256": candidate_sha256,
            "suite": "MODEL-EVOLUTION-SUITE-V1",
            "metrics": {
                "primary_metric": 0.91,
                "baseline_metric": 0.72,
            },
            "evidence": [
                {
                    "type": "BENCHMARK_REPORT",
                    "result": "PASS",
                }
            ],
            "passed": True,
        },
        "held_out_tests": {
            "test_id": "HELDOUT-DNA18-01",
            "candidate_sha256": candidate_sha256,
            "dataset_id": "HELDOUT-SET-V1",
            "held_out": True,
            "training_excluded": True,
            "results": {
                "primary_metric": 0.88,
                "failure_count": 0,
            },
            "evidence": [
                {
                    "type": "HELD_OUT_REPORT",
                    "result": "PASS",
                }
            ],
            "passed": True,
        },
        "promotion": {
            "decision_id": "PROMOTION-DNA18-01",
            "candidate_sha256": candidate_sha256,
            "approver_id": "PROMOTION-AUTHORITY-DNA18",
            "criteria": deepcopy(REQUIRED_GATES),
            "approved": True,
        },
        "rollback": {
            "rollback_id": "ROLLBACK-DNA18-01",
            "candidate_sha256": candidate_sha256,
            "ready": True,
            "target_version": "VERSION-1",
            "procedure": "RESTORE_BASELINE_VERSION",
            "trigger_conditions": [
                "POST_PROMOTION_REGRESSION",
                "VERIFICATION_FAILURE",
            ],
        },
    }


def self_check_dna18(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 18):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna18_core = core54.get("DNA-18")
    assert_exact_canon(dna18_core)
    bind_dna18(core54)

    from SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING import (
        _complete_probe as dna16_complete_probe,
    )
    from SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING import (
        _valid_persistent_capability_change,
    )

    probe = dna16_complete_probe(core54)
    probe["persistent_capability_change"] = (
        _valid_persistent_capability_change()
    )
    snapshot = deepcopy(probe)

    through_dna17 = _run_through(
        core54,
        probe,
        17,
    )

    pre_verification_wall = deepcopy(
        through_dna17["cognitive_state"][
            "independent_verification_wall"
        ]
    )
    pre_two_levels = deepcopy(
        through_dna17["cognitive_state"][
            "two_levels_of_learning"
        ]
    )
    pre_provenance_count = len(
        through_dna17["cognitive_state"][
            "provenance"
        ]
    )

    valid_candidate = _valid_model_evolution_candidate(
        "MODEL"
    )
    valid_input = deepcopy(through_dna17)
    valid_input["model_evolution_candidate"] = (
        valid_candidate
    )
    result = dna18_core.activate(valid_input)

    assert probe == snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 19)
    ]

    dna18 = result["core54_outputs"]["DNA-18"]
    assert dna18["canonical_gene"] == CANON_DNA18
    assert dna18["model_evolution_contract"] == (
        MODEL_EVOLUTION_CONTRACT
    )
    assert dna18["all_gates_passed"] is True
    assert dna18["promotion_eligible"] is True
    assert dna18["benchmark_executed"] is False
    assert dna18["held_out_tests_executed"] is False
    assert dna18["promotion_executed"] is False
    assert dna18["rollback_executed"] is False
    assert dna18["model_or_adapter_modified"] is False
    assert dna18["status"] == "CANON_ALIGNED"

    evaluation = dna18["evaluation"]
    assert evaluation["evaluation_id"] == (
        "DNA-18-EVOLUTION-0001"
    )
    assert evaluation["candidate_identity"] == (
        _candidate_identity(valid_candidate)
    )
    assert evaluation["candidate_type_supported"] is True
    assert evaluation["missing_fields"] == []
    assert evaluation["all_gates_passed"] is True
    assert evaluation["promotion_eligible"] is True
    assert evaluation["rejection_reasons"] == []
    assert evaluation["status"] == (
        "ELIGIBLE_FOR_CONTROLLED_PROMOTION"
    )
    assert (
        evaluation[
            "dna17_neural_evidence_used_as_gate_substitute"
        ]
        is False
    )
    assert len(
        evaluation["dna17_neural_record_ids_observed"]
    ) == 1

    for gate_name in (
        "independent_benchmark",
        "held_out_tests",
        "promotion",
        "rollback",
    ):
        gate = evaluation["gates"][gate_name]
        assert gate["passed"] is True
        assert gate["reasons"] == []

    state = result["cognitive_state"]
    model_evolution = state["model_evolution"]
    assert model_evolution["contract"] == (
        MODEL_EVOLUTION_CONTRACT
    )
    assert model_evolution["evaluations"] == [
        evaluation
    ]
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-18"
    assert contract_event["operation"] == (
        "MODEL_EVOLUTION_CONTRACT_ESTABLISHED"
    )
    assert contract_event["required_gates"] == (
        REQUIRED_GATES
    )
    assert contract_event["benchmark_executed"] is False
    assert contract_event["promotion_executed"] is False
    assert contract_event["rollback_executed"] is False

    evaluation_event = state["provenance"][-1]
    assert evaluation_event["core_id"] == "DNA-18"
    assert evaluation_event["operation"] == (
        "MODEL_EVOLUTION_GATES_EVALUATED"
    )
    assert evaluation_event["all_gates_passed"] is True
    assert evaluation_event["promotion_eligible"] is True
    assert evaluation_event["benchmark_executed"] is False
    assert evaluation_event["promotion_executed"] is False
    assert evaluation_event["rollback_executed"] is False

    # DNA-18 must not mutate prior verification or learning state.
    assert (
        state["independent_verification_wall"]
        == pre_verification_wall
    )
    assert (
        state["two_levels_of_learning"]
        == pre_two_levels
    )

    # ADAPTER must pass through the same four gates.
    adapter_input = deepcopy(through_dna17)
    adapter_input["model_evolution_candidate"] = (
        _valid_model_evolution_candidate("ADAPTER")
    )
    adapter = dna18_core.activate(adapter_input)
    adapter_evaluation = adapter[
        "core54_outputs"
    ]["DNA-18"]["evaluation"]
    assert (
        adapter_evaluation["candidate_identity"][
            "candidate_type"
        ]
        == "ADAPTER"
    )
    assert adapter_evaluation["promotion_eligible"] is True

    # The producer cannot independently benchmark its own candidate.
    self_benchmark_input = deepcopy(through_dna17)
    self_benchmark_candidate = (
        _valid_model_evolution_candidate("MODEL")
    )
    self_benchmark_candidate[
        "independent_benchmark"
    ]["runner_id"] = "PRODUCER-DNA18"
    self_benchmark_input[
        "model_evolution_candidate"
    ] = self_benchmark_candidate
    self_benchmark = dna18_core.activate(
        self_benchmark_input
    )
    self_benchmark_eval = self_benchmark[
        "core54_outputs"
    ]["DNA-18"]["evaluation"]
    assert self_benchmark_eval["promotion_eligible"] is False
    assert (
        "BENCHMARK_RUNNER_NOT_SEPARATED_FROM_PRODUCER"
        in self_benchmark_eval["rejection_reasons"]
    )

    # Held-out tests must truly be excluded from training.
    not_held_out_input = deepcopy(through_dna17)
    not_held_out_candidate = (
        _valid_model_evolution_candidate("MODEL")
    )
    not_held_out_candidate[
        "held_out_tests"
    ]["training_excluded"] = False
    not_held_out_input[
        "model_evolution_candidate"
    ] = not_held_out_candidate
    not_held_out = dna18_core.activate(
        not_held_out_input
    )
    not_held_out_eval = not_held_out[
        "core54_outputs"
    ]["DNA-18"]["evaluation"]
    assert not_held_out_eval["promotion_eligible"] is False
    assert (
        "TRAINING_EXCLUSION_REQUIRED"
        in not_held_out_eval["rejection_reasons"]
    )

    # Every gate must bind to the exact candidate.
    wrong_binding_input = deepcopy(through_dna17)
    wrong_binding_candidate = (
        _valid_model_evolution_candidate("MODEL")
    )
    wrong_binding_candidate["promotion"][
        "candidate_sha256"
    ] = "0" * 64
    wrong_binding_input[
        "model_evolution_candidate"
    ] = wrong_binding_candidate
    wrong_binding = dna18_core.activate(
        wrong_binding_input
    )
    wrong_binding_eval = wrong_binding[
        "core54_outputs"
    ]["DNA-18"]["evaluation"]
    assert wrong_binding_eval["promotion_eligible"] is False
    assert (
        "PROMOTION_NOT_BOUND_TO_CANDIDATE"
        in wrong_binding_eval["rejection_reasons"]
    )

    # Promotion approval is mandatory.
    no_promotion_input = deepcopy(through_dna17)
    no_promotion_candidate = (
        _valid_model_evolution_candidate("MODEL")
    )
    no_promotion_candidate["promotion"]["approved"] = False
    no_promotion_input[
        "model_evolution_candidate"
    ] = no_promotion_candidate
    no_promotion = dna18_core.activate(
        no_promotion_input
    )
    no_promotion_eval = no_promotion[
        "core54_outputs"
    ]["DNA-18"]["evaluation"]
    assert no_promotion_eval["promotion_eligible"] is False
    assert (
        "PROMOTION_APPROVAL_REQUIRED"
        in no_promotion_eval["rejection_reasons"]
    )

    # Rollback readiness and baseline target are mandatory.
    no_rollback_input = deepcopy(through_dna17)
    no_rollback_candidate = (
        _valid_model_evolution_candidate("MODEL")
    )
    no_rollback_candidate["rollback"]["ready"] = False
    no_rollback_input[
        "model_evolution_candidate"
    ] = no_rollback_candidate
    no_rollback = dna18_core.activate(
        no_rollback_input
    )
    no_rollback_eval = no_rollback[
        "core54_outputs"
    ]["DNA-18"]["evaluation"]
    assert no_rollback_eval["promotion_eligible"] is False
    assert (
        "ROLLBACK_READINESS_REQUIRED"
        in no_rollback_eval["rejection_reasons"]
    )

    # Missing candidate must never become eligible.
    missing_candidate = dna18_core.activate(
        deepcopy(through_dna17)
    )
    missing_evaluation = missing_candidate[
        "core54_outputs"
    ]["DNA-18"]["evaluation"]
    assert missing_evaluation["promotion_eligible"] is False
    assert (
        "MODEL_OR_ADAPTER_CANDIDATE_REQUIRED"
        in missing_evaluation["rejection_reasons"]
    )

    # Reject provisional root markers as the official contract.
    assert "model_promotion_allowed" not in result
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result

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
        "core_id": "DNA-18",
        "canon_mapping": "PASS",
        "independent_benchmark_gate": "PASS",
        "held_out_test_gate": "PASS",
        "promotion_gate": "PASS",
        "rollback_gate": "PASS",
        "model_and_adapter_supported": "PASS",
        "benchmark_executed": False,
        "held_out_tests_executed": False,
        "promotion_executed": False,
        "rollback_executed": False,
        "model_or_adapter_modified": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-19"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def main() -> int:
    names = {
        1: "PURPOSE_EXISTENCE",
        2: "FOUNDATION_INTELLIGENCE_SUBSTRATE",
        3: "UNIFIED_COGNITIVE_STATE",
        4: "EIGHT_COGNITIVE_LAYERS",
        5: "ETHICAL_INTELLIGENCE",
        6: "INTERLAYER_FEEDBACK",
        7: "PERSISTENT_EXISTENCE",
        8: "LEARNING_WORLD",
        9: "INDEPENDENT_VERIFICATION_WALL",
        10: "MEMORY_GENOME",
        11: "KNOWLEDGE_GRAPH",
        12: "TOOL_INTELLIGENCE",
        13: "ADAPTIVE_COGNITIVE_DEPTH",
        14: "PERSISTENCE_ENGINE",
        15: "F174_DEVELOPMENT_DYNAMICS",
        16: "EXPERIENCE_DRIVEN_LEARNING",
        17: "TWO_LEVELS_OF_LEARNING",
    }
    required_gene_files = [
        (
            GENES_ROOT
            / f"SIGMA_DNA_{index:02d}_{names[index]}.py"
        )
        for index in range(1, 18)
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print(
                "DNA-18_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )
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
        from SIGMA_DNA_08_LEARNING_WORLD import (
            self_check_dna08,
        )
        from SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL import (
            self_check_dna09,
        )
        from SIGMA_DNA_10_MEMORY_GENOME import (
            self_check_dna10,
        )
        from SIGMA_DNA_11_KNOWLEDGE_GRAPH import (
            self_check_dna11,
        )
        from SIGMA_DNA_12_TOOL_INTELLIGENCE import (
            self_check_dna12,
        )
        from SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH import (
            self_check_dna13,
        )
        from SIGMA_DNA_14_PERSISTENCE_ENGINE import (
            self_check_dna14,
        )
        from SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS import (
            self_check_dna15,
        )
        from SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING import (
            self_check_dna16,
        )
        from SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING import (
            self_check_dna17,
        )
    except Exception as exc:
        print("DNA-18_FAIL: IMPORT_ERROR")
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

        prior_checks = (
            ("DNA-01", self_check_dna01),
            ("DNA-02", self_check_dna02),
            ("DNA-03", self_check_dna03),
            ("DNA-04", self_check_dna04),
            ("DNA-05", self_check_dna05),
            ("DNA-06", self_check_dna06),
            ("DNA-07", self_check_dna07),
            ("DNA-08", self_check_dna08),
            ("DNA-09", self_check_dna09),
            ("DNA-10", self_check_dna10),
            ("DNA-11", self_check_dna11),
            ("DNA-12", self_check_dna12),
            ("DNA-13", self_check_dna13),
            ("DNA-14", self_check_dna14),
            ("DNA-15", self_check_dna15),
            ("DNA-16", self_check_dna16),
            ("DNA-17", self_check_dna17),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(
                    f"{core_id}_NOT_PASS"
                )

        report = self_check_dna18(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != [
            f"DNA-{index:02d}"
            for index in range(1, 19)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-18_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-18_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_18_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "INDEPENDENT_BENCHMARK_GATE:",
        report["independent_benchmark_gate"],
    )
    print(
        "HELD_OUT_TEST_GATE:",
        report["held_out_test_gate"],
    )
    print(
        "PROMOTION_GATE:",
        report["promotion_gate"],
    )
    print(
        "ROLLBACK_GATE:",
        report["rollback_gate"],
    )
    print(
        "MODEL_AND_ADAPTER_SUPPORTED:",
        report["model_and_adapter_supported"],
    )
    print(
        "BENCHMARK_EXECUTED:",
        report["benchmark_executed"],
    )
    print(
        "HELD_OUT_TESTS_EXECUTED:",
        report["held_out_tests_executed"],
    )
    print(
        "PROMOTION_EXECUTED:",
        report["promotion_executed"],
    )
    print(
        "ROLLBACK_EXECUTED:",
        report["rollback_executed"],
    )
    print(
        "MODEL_OR_ADAPTER_MODIFIED:",
        report["model_or_adapter_modified"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 18/54")
    print("NEXT_AUTHORIZED: DNA-19")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
