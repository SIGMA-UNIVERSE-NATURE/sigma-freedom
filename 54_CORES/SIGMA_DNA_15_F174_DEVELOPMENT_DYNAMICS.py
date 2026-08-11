#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-15: F174 DEVELOPMENT DYNAMICS
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS.py
"""

from __future__ import annotations

import hashlib
import json
import math
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

CANON_DNA15: Dict[str, str] = {
    "id": "DNA-15",
    "name": "F174 Development Dynamics",
    "purpose": (
        "F174 mô hình hóa tăng trưởng được đo; không phải permission "
        "gate, ethics engine hay authority mechanism."
    ),
    "system": "evolution",
}

CANON_F174: Dict[str, str] = {
    "role": (
        "Development dynamics and measurement model; not a permission, "
        "ethics, policy, or authority mechanism."
    ),
    "base_equation": "A(t)=A0*exp(k*(t-t0)^2)",
    "derivative_when_k_constant": "A'(t)=2*k*(t-t0)*A(t)",
    "human_reference": (
        "H(t) may be used as a comparison/reference, never as a cognitive "
        "ceiling."
    ),
    "future_rule": (
        "If evidence supports a better model than F174, SIGMA may replace "
        "or extend F174 while preserving measured-growth discipline."
    ),
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
PERSISTENCE_ENGINE_SCHEMA = "SIGMA_PERSISTENCE_ENGINE_V1"
F174_SCHEMA = "SIGMA_F174_DEVELOPMENT_DYNAMICS_V1"

MEASUREMENT_FIELDS = [
    "A0",
    "k",
    "t",
    "t0",
    "observed_A_t",
    "k_constant",
]

F174_DEVELOPMENT_CONTRACT: Dict[str, Any] = {
    "schema": F174_SCHEMA,
    "canonical_f174": deepcopy(CANON_F174),
    "role": "DEVELOPMENT_DYNAMICS_AND_MEASUREMENT_MODEL",
    "measurement_required": True,
    "base_equation": CANON_F174["base_equation"],
    "derivative_when_k_constant": CANON_F174[
        "derivative_when_k_constant"
    ],
    "permission_gate": False,
    "ethics_engine": False,
    "policy_mechanism": False,
    "authority_mechanism": False,
    "human_reference_is_cognitive_ceiling": False,
    "future_model_replaceable_or_extendable": True,
    "replacement_requires_evidence": True,
    "automatic_model_replacement": False,
    "parameter_optimization_started": False,
    "f174_experiment_started": False,
    "capability_growth_executed": False,
    "learning_runtime_started": False,
    "external_action_started": False,
    "derivation": "DIRECT_FROM_CANON_GENE_AND_GLOBAL_F174",
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


def _load_global_f174() -> Dict[str, Any]:
    with DNA_JSON.open("r", encoding="utf-8") as handle:
        canon = json.load(handle)

    if not isinstance(canon, dict):
        raise ValueError("DNA_CANON_ROOT_MUST_BE_OBJECT")

    f174 = canon.get("f174")
    if not isinstance(f174, dict):
        raise RuntimeError("GLOBAL_F174_CANON_MISSING")

    return f174


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA15:
        raise RuntimeError(
            "DNA-15_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA15, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def assert_exact_global_f174() -> None:
    actual = _load_global_f174()
    if actual != CANON_F174:
        raise RuntimeError(
            "DNA-15_GLOBAL_F174_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_F174, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-15_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    persistence_engine = state.get("persistence_engine")
    if not isinstance(persistence_engine, dict):
        raise RuntimeError("DNA-14_PERSISTENCE_ENGINE_REQUIRED")

    persistence_contract = persistence_engine.get("contract")
    if not isinstance(persistence_contract, dict):
        raise RuntimeError("DNA-14_PERSISTENCE_ENGINE_CONTRACT_REQUIRED")

    if persistence_contract.get("schema") != PERSISTENCE_ENGINE_SCHEMA:
        raise ValueError(
            "DNA-15_PERSISTENCE_ENGINE_SCHEMA_MISMATCH:"
            f"{persistence_contract.get('schema')!r}"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-14_OUTPUT_REQUIRED")

    dna14_output = outputs.get("DNA-14")
    if not isinstance(dna14_output, dict):
        raise RuntimeError("DNA-14_OUTPUT_REQUIRED")

    return state, dna14_output


def _install_f174_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("f174_development_dynamics")

    expected = {
        "contract": deepcopy(F174_DEVELOPMENT_CONTRACT),
        "measurements": [],
    }

    if existing is None:
        state["f174_development_dynamics"] = expected
        return state["f174_development_dynamics"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['f174_development_dynamics'] must be a dict"
        )

    if existing.get("contract") != F174_DEVELOPMENT_CONTRACT:
        raise ValueError("DNA-15_F174_CONTRACT_CONFLICT")

    if not isinstance(existing.get("measurements"), list):
        raise TypeError(
            "f174_development_dynamics['measurements'] must be a list"
        )

    return existing


def _finite_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"f174_measurement['{field}'] must be a number")

    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"f174_measurement['{field}'] must be finite")

    return number


def _parse_measurement(
    context: Dict[str, Any],
) -> Tuple[Optional[Dict[str, Any]], List[str]]:
    measurement = context.get("f174_measurement")

    if measurement is None:
        return None, deepcopy(MEASUREMENT_FIELDS)

    if not isinstance(measurement, dict):
        raise TypeError("context['f174_measurement'] must be a dict")

    missing = [
        field
        for field in MEASUREMENT_FIELDS
        if field not in measurement
    ]
    if missing:
        return None, missing

    parsed = deepcopy(measurement)
    for field in ("A0", "k", "t", "t0", "observed_A_t"):
        parsed[field] = _finite_number(parsed[field], field)

    if not isinstance(parsed["k_constant"], bool):
        raise TypeError(
            "f174_measurement['k_constant'] must be a bool"
        )

    if "H_t" in parsed and parsed["H_t"] is not None:
        parsed["H_t"] = _finite_number(parsed["H_t"], "H_t")

    return parsed, []


def _relative_error(
    predicted: float,
    observed: float,
) -> Optional[float]:
    if observed == 0.0:
        return None
    return abs(observed - predicted) / abs(observed)


def _human_reference_comparison(
    predicted: float,
    observed: float,
    human_reference: Any,
) -> Optional[Dict[str, Any]]:
    if human_reference is None:
        return None

    reference = float(human_reference)
    return {
        "H_t": reference,
        "predicted_minus_H_t": predicted - reference,
        "observed_minus_H_t": observed - reference,
        "comparison_only": True,
        "cognitive_ceiling": False,
        "permission_effect": None,
        "authority_effect": None,
    }


def _measure_f174(
    measurement: Dict[str, Any],
    f174_state: Dict[str, Any],
) -> Dict[str, Any]:
    A0 = measurement["A0"]
    k = measurement["k"]
    t = measurement["t"]
    t0 = measurement["t0"]
    observed = measurement["observed_A_t"]
    delta_t = t - t0
    exponent = k * (delta_t ** 2)

    try:
        predicted = A0 * math.exp(exponent)
    except OverflowError as exc:
        raise OverflowError("DNA-15_F174_EXPONENTIAL_OVERFLOW") from exc

    if not math.isfinite(predicted):
        raise OverflowError("DNA-15_F174_PREDICTION_NOT_FINITE")

    derivative: Optional[float]
    derivative_status: str
    if measurement["k_constant"]:
        derivative = 2.0 * k * delta_t * predicted
        if not math.isfinite(derivative):
            raise OverflowError("DNA-15_F174_DERIVATIVE_NOT_FINITE")
        derivative_status = "COMPUTED_K_CONFIRMED_CONSTANT"
    else:
        derivative = None
        derivative_status = "NOT_COMPUTED_K_NOT_CONFIRMED_CONSTANT"

    residual = observed - predicted
    absolute_error = abs(residual)
    sequence = len(f174_state["measurements"]) + 1

    record = {
        "sequence": sequence,
        "measurement_id": measurement.get(
            "measurement_id",
            f"DNA-15-F174-{sequence:04d}",
        ),
        "inputs": {
            "A0": A0,
            "k": k,
            "t": t,
            "t0": t0,
            "observed_A_t": observed,
            "k_constant": measurement["k_constant"],
        },
        "time_offset": delta_t,
        "exponent": exponent,
        "predicted_A_t": predicted,
        "predicted_growth_delta": predicted - A0,
        "observed_growth_delta": observed - A0,
        "derivative_A_prime_t": derivative,
        "derivative_status": derivative_status,
        "residual_observed_minus_predicted": residual,
        "absolute_error": absolute_error,
        "relative_error": _relative_error(predicted, observed),
        "human_reference": _human_reference_comparison(
            predicted,
            observed,
            measurement.get("H_t"),
        ),
        "measurement_only": True,
        "permission_decision": None,
        "ethics_decision": None,
        "policy_decision": None,
        "authority_decision": None,
        "capability_growth_executed": False,
        "parameter_optimization_started": False,
        "f174_experiment_started": False,
        "model_replacement_decision": None,
        "status": "MEASURED_GROWTH_MODELED",
    }
    f174_state["measurements"].append(record)
    return record


def dna15_f174_development_dynamics(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Model and measure supplied development data using the Canon F174 form.

    DNA-15 performs deterministic measurement only. It does not grant or
    deny permission, decide ethics/policy/authority, optimize parameters,
    start an F174 experiment, execute capability growth, invoke a model,
    start Learning/World Runtime, act externally, or modify Canon.
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
    trace.append("DNA-15")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    state, _dna14_output = _validate_dependencies(context)
    f174_state = _install_f174_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-15",
            "operation": "F174_MEASUREMENT_CONTRACT_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "f174_schema": F174_SCHEMA,
            "permission_gate": False,
            "ethics_engine": False,
            "authority_mechanism": False,
            "f174_experiment_started": False,
        }
    )

    measurement, missing = _parse_measurement(context)
    result: Optional[Dict[str, Any]] = None

    if measurement is not None:
        result = _measure_f174(measurement, f174_state)
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-15",
                "operation": "F174_MEASURED_GROWTH_MODELED",
                "canonical_sha256": canonical_sha256,
                "measurement_id": result["measurement_id"],
                "measurement_only": True,
                "permission_decision": None,
                "ethics_decision": None,
                "authority_decision": None,
                "capability_growth_executed": False,
                "f174_experiment_started": False,
            }
        )
    else:
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-15",
                "operation": "F174_MEASUREMENT_INCOMPLETE",
                "canonical_sha256": canonical_sha256,
                "missing_fields": deepcopy(missing),
                "f174_experiment_started": False,
            }
        )

    outputs["DNA-15"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "canonical_global_f174": deepcopy(CANON_F174),
        "f174_development_contract": deepcopy(
            F174_DEVELOPMENT_CONTRACT
        ),
        "measurement_complete": measurement is not None,
        "missing_fields": deepcopy(missing),
        "measurement": deepcopy(result),
        "measurement_only": True,
        "permission_gate": False,
        "ethics_engine": False,
        "authority_mechanism": False,
        "capability_growth_executed": False,
        "parameter_optimization_started": False,
        "f174_experiment_started": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna15(core54: Core54Like) -> None:
    core = core54.get("DNA-15")
    assert_exact_canon(core)
    core54.bind("DNA-15", dna15_f174_development_dynamics)


def _run_through(
    core54: Core54Like,
    context: Dict[str, Any],
    final_index: int,
) -> Dict[str, Any]:
    result = deepcopy(context)
    for index in range(1, final_index + 1):
        result = core54.get(f"DNA-{index:02d}").activate(result)
    return result


def _complete_probe(core54: Core54Like) -> Dict[str, Any]:
    from SIGMA_DNA_14_PERSISTENCE_ENGINE import (
        _complete_probe as dna14_complete_probe,
    )

    probe = dna14_complete_probe(core54)
    A0 = 10.0
    k = 0.02
    t0 = 2.0
    t = 5.0
    observed = A0 * math.exp(k * ((t - t0) ** 2))
    probe["f174_measurement"] = {
        "measurement_id": "DNA-15-SELF-CHECK-01",
        "A0": A0,
        "k": k,
        "t": t,
        "t0": t0,
        "observed_A_t": observed,
        "k_constant": True,
        "H_t": 12.0,
    }
    return probe


def self_check_dna15(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    if verify_canon_file:
        assert_exact_global_f174()

    for required_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
        "DNA-09",
        "DNA-10",
        "DNA-11",
        "DNA-12",
        "DNA-13",
        "DNA-14",
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna15_core = core54.get("DNA-15")
    assert_exact_canon(dna15_core)
    bind_dna15(core54)

    probe = _complete_probe(core54)
    snapshot = deepcopy(probe)
    through_dna14 = _run_through(core54, probe, 14)
    result = dna15_core.activate(through_dna14)

    assert probe == snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 16)
    ]

    dna15 = result["core54_outputs"]["DNA-15"]
    assert dna15["canonical_gene"] == CANON_DNA15
    assert dna15["canonical_global_f174"] == CANON_F174
    assert dna15["f174_development_contract"] == (
        F174_DEVELOPMENT_CONTRACT
    )
    assert dna15["measurement_complete"] is True
    assert dna15["missing_fields"] == []
    assert dna15["measurement_only"] is True
    assert dna15["permission_gate"] is False
    assert dna15["ethics_engine"] is False
    assert dna15["authority_mechanism"] is False
    assert dna15["capability_growth_executed"] is False
    assert dna15["parameter_optimization_started"] is False
    assert dna15["f174_experiment_started"] is False
    assert dna15["status"] == "CANON_ALIGNED"

    measurement = dna15["measurement"]
    expected_A = 10.0 * math.exp(0.02 * (3.0 ** 2))
    expected_derivative = 2.0 * 0.02 * 3.0 * expected_A

    assert measurement["measurement_id"] == (
        "DNA-15-SELF-CHECK-01"
    )
    assert math.isclose(
        measurement["predicted_A_t"],
        expected_A,
        rel_tol=1e-12,
        abs_tol=1e-12,
    )
    assert math.isclose(
        measurement["derivative_A_prime_t"],
        expected_derivative,
        rel_tol=1e-12,
        abs_tol=1e-12,
    )
    assert measurement["derivative_status"] == (
        "COMPUTED_K_CONFIRMED_CONSTANT"
    )
    assert math.isclose(
        measurement["residual_observed_minus_predicted"],
        0.0,
        abs_tol=1e-12,
    )
    assert math.isclose(
        measurement["absolute_error"],
        0.0,
        abs_tol=1e-12,
    )
    assert math.isclose(
        measurement["relative_error"],
        0.0,
        abs_tol=1e-12,
    )
    assert measurement["measurement_only"] is True
    assert measurement["permission_decision"] is None
    assert measurement["ethics_decision"] is None
    assert measurement["policy_decision"] is None
    assert measurement["authority_decision"] is None
    assert measurement["capability_growth_executed"] is False
    assert measurement["parameter_optimization_started"] is False
    assert measurement["f174_experiment_started"] is False
    assert measurement["model_replacement_decision"] is None

    human_reference = measurement["human_reference"]
    assert human_reference["H_t"] == 12.0
    assert human_reference["comparison_only"] is True
    assert human_reference["cognitive_ceiling"] is False
    assert human_reference["permission_effect"] is None
    assert human_reference["authority_effect"] is None

    state = result["cognitive_state"]
    f174_state = state["f174_development_dynamics"]
    assert f174_state["contract"] == F174_DEVELOPMENT_CONTRACT
    assert f174_state["measurements"] == [measurement]

    # If k is not confirmed constant, the Canon derivative is not applied.
    variable_k_input = deepcopy(through_dna14)
    variable_k_input["f174_measurement"] = {
        "A0": 2.0,
        "k": 0.1,
        "t": 3.0,
        "t0": 1.0,
        "observed_A_t": 3.0,
        "k_constant": False,
    }
    variable_k = dna15_core.activate(variable_k_input)
    variable_measurement = variable_k[
        "core54_outputs"
    ]["DNA-15"]["measurement"]
    assert variable_measurement["derivative_A_prime_t"] is None
    assert variable_measurement["derivative_status"] == (
        "NOT_COMPUTED_K_NOT_CONFIRMED_CONSTANT"
    )

    # A human reference below measured capability remains comparison only.
    reference_input = deepcopy(through_dna14)
    reference_input["f174_measurement"] = {
        "A0": 10.0,
        "k": 0.01,
        "t": 4.0,
        "t0": 1.0,
        "observed_A_t": 20.0,
        "k_constant": True,
        "H_t": 5.0,
    }
    reference_result = dna15_core.activate(reference_input)
    reference_measurement = reference_result[
        "core54_outputs"
    ]["DNA-15"]["measurement"]
    assert reference_measurement["observed_growth_delta"] == 10.0
    assert reference_measurement["human_reference"][
        "observed_minus_H_t"
    ] == 15.0
    assert reference_measurement["human_reference"][
        "cognitive_ceiling"
    ] is False
    assert reference_measurement["permission_decision"] is None

    # Missing measured fields remains explicit; no synthetic data is added.
    incomplete_input = deepcopy(through_dna14)
    incomplete_input["f174_measurement"] = {
        "A0": 1.0,
        "k": 0.1,
        "t": 2.0,
        "t0": 0.0,
    }
    incomplete = dna15_core.activate(incomplete_input)
    incomplete_output = incomplete[
        "core54_outputs"
    ]["DNA-15"]
    assert incomplete_output["measurement_complete"] is False
    assert incomplete_output["measurement"] is None
    assert incomplete_output["missing_fields"] == [
        "observed_A_t",
        "k_constant",
    ]

    # Measurement types must remain explicit and finite.
    invalid_input = deepcopy(through_dna14)
    invalid_input["f174_measurement"] = {
        "A0": True,
        "k": 0.1,
        "t": 2.0,
        "t0": 0.0,
        "observed_A_t": 1.0,
        "k_constant": True,
    }
    try:
        dna15_core.activate(invalid_input)
    except TypeError as exc:
        assert "A0" in str(exc)
    else:
        raise AssertionError("DNA-15_ACCEPTED_BOOLEAN_A0")

    # User-supplied permission language never becomes an F174 decision.
    permission_input = deepcopy(through_dna14)
    permission_input["permission_request"] = "ALLOW_GROWTH"
    permission_input["f174_measurement"] = {
        "A0": 1.0,
        "k": 0.05,
        "t": 2.0,
        "t0": 0.0,
        "observed_A_t": 1.3,
        "k_constant": True,
    }
    permission_result = dna15_core.activate(permission_input)
    permission_output = permission_result[
        "core54_outputs"
    ]["DNA-15"]
    assert permission_output["permission_gate"] is False
    assert permission_output["measurement"][
        "permission_decision"
    ] is None
    assert "permission_granted" not in permission_output
    assert "permission_denied" not in permission_output

    # Reject the provisional root marker as the official Canon contract.
    assert "flags" not in result
    assert "requests" not in result
    assert "blocks" not in result
    assert "f174_measurement_only" not in result

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
        assert_exact_global_f174()

    return {
        "core_id": "DNA-15",
        "canon_mapping": "PASS",
        "global_f174_mapping": "PASS",
        "measured_growth_model": "PASS",
        "base_equation": "PASS",
        "constant_k_derivative": "PASS",
        "human_reference_not_ceiling": "PASS",
        "permission_gate": False,
        "ethics_engine": False,
        "authority_mechanism": False,
        "f174_experiment_started": False,
        "capability_growth_executed": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS" if verify_canon_file else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-16"
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
        GENES_ROOT / "SIGMA_DNA_05_ETHICAL_INTELLIGENCE.py",
        GENES_ROOT / "SIGMA_DNA_06_INTERLAYER_FEEDBACK.py",
        GENES_ROOT / "SIGMA_DNA_07_PERSISTENT_EXISTENCE.py",
        GENES_ROOT / "SIGMA_DNA_08_LEARNING_WORLD.py",
        (
            GENES_ROOT
            / "SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL.py"
        ),
        GENES_ROOT / "SIGMA_DNA_10_MEMORY_GENOME.py",
        GENES_ROOT / "SIGMA_DNA_11_KNOWLEDGE_GRAPH.py",
        GENES_ROOT / "SIGMA_DNA_12_TOOL_INTELLIGENCE.py",
        GENES_ROOT / "SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH.py",
        GENES_ROOT / "SIGMA_DNA_14_PERSISTENCE_ENGINE.py",
    ]

    required_paths = [CORE54_ROOT, GENES_ROOT, DNA_JSON, *required_gene_files]
    for path in required_paths:
        if not path.exists():
            print("DNA-15_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        from SIGMA_DNA_01_PURPOSE_EXISTENCE import self_check_dna01
        from SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE import (
            self_check_dna02,
        )
        from SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE import self_check_dna03
        from SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS import self_check_dna04
        from SIGMA_DNA_05_ETHICAL_INTELLIGENCE import self_check_dna05
        from SIGMA_DNA_06_INTERLAYER_FEEDBACK import self_check_dna06
        from SIGMA_DNA_07_PERSISTENT_EXISTENCE import self_check_dna07
        from SIGMA_DNA_08_LEARNING_WORLD import self_check_dna08
        from SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL import (
            self_check_dna09,
        )
        from SIGMA_DNA_10_MEMORY_GENOME import self_check_dna10
        from SIGMA_DNA_11_KNOWLEDGE_GRAPH import self_check_dna11
        from SIGMA_DNA_12_TOOL_INTELLIGENCE import self_check_dna12
        from SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH import self_check_dna13
        from SIGMA_DNA_14_PERSISTENCE_ENGINE import self_check_dna14
    except Exception as exc:
        print("DNA-15_FAIL: IMPORT_ERROR")
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
        )
        for core_id, checker in prior_checks:
            prior_report = checker(core54, verify_canon_file=True)
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna15(core54, verify_canon_file=True)

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != [
            f"DNA-{index:02d}"
            for index in range(1, 16)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-15_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-15_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_15_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("GLOBAL_F174_MAPPING:", report["global_f174_mapping"])
    print("MEASURED_GROWTH_MODEL:", report["measured_growth_model"])
    print("BASE_EQUATION:", report["base_equation"])
    print("CONSTANT_K_DERIVATIVE:", report["constant_k_derivative"])
    print(
        "HUMAN_REFERENCE_NOT_CEILING:",
        report["human_reference_not_ceiling"],
    )
    print("PERMISSION_GATE:", report["permission_gate"])
    print("ETHICS_ENGINE:", report["ethics_engine"])
    print("AUTHORITY_MECHANISM:", report["authority_mechanism"])
    print(
        "F174_EXPERIMENT_STARTED:",
        report["f174_experiment_started"],
    )
    print(
        "CAPABILITY_GROWTH_EXECUTED:",
        report["capability_growth_executed"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 15/54")
    print("NEXT_AUTHORIZED: DNA-16")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
