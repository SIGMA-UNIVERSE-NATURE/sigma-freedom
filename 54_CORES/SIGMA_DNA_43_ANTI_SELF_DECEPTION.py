#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import hashlib
import importlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Protocol

SIGMA_ROOT = Path(r"E:\SIGMA")
CORE54_ROOT = SIGMA_ROOT / "RUNTIME" / "CORE54"
GENES_ROOT = CORE54_ROOT / "GENES"
DNA_JSON = SIGMA_ROOT / "CORE" / "DNA_CANON" / "SIGMA_CORE_DNA_54" / "sigma_dna_54.json"

CANON_DNA43: Dict[str, str] = {
    "id": "DNA-43",
    "name": "Anti-Self-Deception",
    "purpose": "Không dùng duy nhất metric đang tối ưu để chứng minh tiến bộ; cần external/held-out evidence.",
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
ANTI_SELF_DECEPTION_SCHEMA = "SIGMA_ANTI_SELF_DECEPTION_V1"
INDEPENDENT_TYPES = {"EXTERNAL", "HELD_OUT"}

ANTI_SELF_DECEPTION_CONTRACT: Dict[str, Any] = {
    "schema": ANTI_SELF_DECEPTION_SCHEMA,
    "optimized_metric_alone_proves_progress": False,
    "independent_evidence_types": ["EXTERNAL", "HELD_OUT"],
    "progress_claim_requires_external_or_held_out_evidence": True,
    "self_report_is_independent_evidence": False,
    "training_metric_is_independent_evidence": False,
    "benchmark_executed_by_dna43": False,
    "verifier_invoked_by_dna43": False,
    "learning_runtime_started": False,
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
    def activate(self, payload: Any = None) -> Dict[str, Any]: ...


class Core54Like(Protocol):
    auto_learning_enabled: bool
    model_calls_enabled: bool
    external_execution_enabled: bool
    canon_write_enabled: bool
    def get(self, core_id: str) -> CoreUnitLike: ...
    def bind(self, core_id: str, handler: Any) -> None: ...


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
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA43:
        raise RuntimeError(f"DNA-43_CANON_MISMATCH:{actual!r}")


def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")
    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError("DNA-43_UNIFIED_STATE_SCHEMA_MISMATCH")
    if not isinstance(state.get("provenance"), list):
        raise TypeError("cognitive_state.provenance must be a list")
    return state


def _install_state(state: Dict[str, Any]) -> Dict[str, Any]:
    node = state.get("anti_self_deception")
    if node is None:
        node = {
            "contract": deepcopy(ANTI_SELF_DECEPTION_CONTRACT),
            "assessments": [],
        }
        state["anti_self_deception"] = node
    if not isinstance(node, dict):
        raise TypeError("cognitive_state.anti_self_deception must be a dict")
    if node.get("contract") != ANTI_SELF_DECEPTION_CONTRACT:
        raise ValueError("DNA-43_ANTI_SELF_DECEPTION_CONTRACT_CONFLICT")
    if not isinstance(node.get("assessments"), list):
        raise TypeError("anti_self_deception.assessments must be a list")
    return node


def _normalize_metric(value: Any) -> Dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError("optimized_metric must be a dict")
    name = value.get("name")
    metric_value = value.get("value")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("DNA-43_OPTIMIZED_METRIC_NAME_REQUIRED")
    if metric_value is None:
        raise ValueError("DNA-43_OPTIMIZED_METRIC_VALUE_REQUIRED")
    return {
        "name": name,
        "value": deepcopy(metric_value),
        "value_sha256": _sha256_json(metric_value),
        "independent_evidence": False,
    }


def _normalize_evidence(item: Any, index: int) -> Dict[str, Any]:
    if not isinstance(item, dict):
        raise TypeError(f"independent_evidence[{index}] must be a dict")
    evidence_id = item.get("evidence_id")
    evidence_type = item.get("type")
    result = item.get("result")
    if not isinstance(evidence_id, str) or not evidence_id.strip():
        raise ValueError("DNA-43_EVIDENCE_ID_REQUIRED")
    if not isinstance(evidence_type, str):
        raise TypeError("independent evidence type must be a string")
    evidence_type = evidence_type.strip().upper()
    if evidence_type not in INDEPENDENT_TYPES:
        raise ValueError(f"DNA-43_NON_INDEPENDENT_EVIDENCE_TYPE:{evidence_type}")
    if result is None:
        raise ValueError(f"DNA-43_EVIDENCE_RESULT_REQUIRED:{evidence_id}")
    return {
        "input_index": index,
        "evidence_id": evidence_id,
        "type": evidence_type,
        "result": deepcopy(result),
        "result_sha256": _sha256_json(result),
        "independent_evidence": True,
        "generated_by_dna43": False,
    }


def _evaluate(supplied: Any, anti_state: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError("progress_assessment must be a dict")

    assessment_id = supplied.get("assessment_id")
    progress_claim = supplied.get("progress_claim")
    if not isinstance(assessment_id, str) or not assessment_id.strip():
        raise ValueError("DNA-43_ASSESSMENT_ID_REQUIRED")
    if not isinstance(progress_claim, bool):
        raise TypeError("progress_claim must be a bool")

    metric = _normalize_metric(supplied.get("optimized_metric"))
    raw_evidence = supplied.get("independent_evidence", [])
    if not isinstance(raw_evidence, list):
        raise TypeError("independent_evidence must be a list")

    evidence = [
        _normalize_evidence(item, index)
        for index, item in enumerate(raw_evidence, start=1)
    ]
    ids = [item["evidence_id"] for item in evidence]
    if len(ids) != len(set(ids)):
        raise ValueError("DNA-43_DUPLICATE_EVIDENCE_ID")

    has_external = any(item["type"] == "EXTERNAL" for item in evidence)
    has_held_out = any(item["type"] == "HELD_OUT" for item in evidence)
    has_independent = has_external or has_held_out

    if progress_claim and not has_independent:
        raise ValueError("DNA-43_PROGRESS_CANNOT_USE_OPTIMIZED_METRIC_ALONE")

    sequence = len(anti_state["assessments"]) + 1
    record = {
        "sequence": sequence,
        "record_id": f"DNA-43-ASSESSMENT-{sequence:04d}",
        "assessment_id": assessment_id,
        "progress_claim": progress_claim,
        "optimized_metric": deepcopy(metric),
        "optimized_metric_alone_used": False,
        "independent_evidence": deepcopy(evidence),
        "has_external_evidence": has_external,
        "has_held_out_evidence": has_held_out,
        "has_independent_evidence": has_independent,
        "progress_claim_supported": progress_claim and has_independent,
        "benchmark_executed": False,
        "verifier_invoked": False,
        "external_action_executed": False,
        "status": (
            "PROGRESS_INDEPENDENT_EVIDENCE_SATISFIED"
            if progress_claim else "NO_PROGRESS_CLAIM"
        ),
    }
    anti_state["assessments"].append(deepcopy(record))
    return record


def dna43_anti_self_deception(payload: Any, core: CoreUnitLike) -> Dict[str, Any]:
    assert_exact_canon(core)
    context = deepcopy(payload) if isinstance(payload, dict) else {"input": deepcopy(payload)}
    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("trace must be a list")
    trace.append("DNA-43")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("core54_outputs must be a dict")

    state = _validate_state(context)
    anti_state = _install_state(state)
    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)
    record = _evaluate(context.get("progress_assessment"), anti_state)

    state["provenance"].append({
        "sequence": len(state["provenance"]) + 1,
        "core_id": "DNA-43",
        "operation": "ANTI_SELF_DECEPTION_PROGRESS_ASSESSMENT_EVALUATED",
        "canonical_sha256": canon_sha,
        "record_id": record["record_id"],
        "progress_claim": record["progress_claim"],
        "has_independent_evidence": record["has_independent_evidence"],
        "optimized_metric_alone_used": False,
        "benchmark_executed": False,
        "verifier_invoked": False,
    })

    outputs["DNA-43"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "anti_self_deception_contract": deepcopy(ANTI_SELF_DECEPTION_CONTRACT),
        "record": deepcopy(record),
        "optimized_metric_alone_rejected": True,
        "external_evidence": record["has_external_evidence"],
        "held_out_evidence": record["has_held_out_evidence"],
        "independent_evidence_gate": record["has_independent_evidence"],
        "benchmark_executed": False,
        "verifier_invoked": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }
    return context


def bind_dna43(core54: Core54Like) -> None:
    core = core54.get("DNA-43")
    assert_exact_canon(core)
    core54.bind("DNA-43", dna43_anti_self_deception)


def self_check_dna43(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = _sha256_file(DNA_JSON) if verify_canon_file else None

    for index in range(1, 43):
        core_id = f"DNA-{index:02d}"
        if not core54.get(core_id).state.behavior_bound:
            raise RuntimeError(f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST")

    core = core54.get("DNA-43")
    assert_exact_canon(core)
    bind_dna43(core54)

    probe = {
        "trace": [f"DNA-{index:02d}" for index in range(1, 43)],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "progress_assessment": {
            "assessment_id": "DNA43-SELF-CHECK",
            "progress_claim": True,
            "optimized_metric": {
                "name": "OPTIMIZED_OBJECTIVE",
                "value": 0.95,
            },
            "independent_evidence": [
                {
                    "evidence_id": "E-HELD-OUT-1",
                    "type": "HELD_OUT",
                    "result": {"score": 0.81},
                },
                {
                    "evidence_id": "E-EXTERNAL-1",
                    "type": "EXTERNAL",
                    "result": {"passed": True},
                },
            ],
        },
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-43"]
    assert output["canonical_gene"] == CANON_DNA43
    assert output["optimized_metric_alone_rejected"] is True
    assert output["external_evidence"] is True
    assert output["held_out_evidence"] is True
    assert output["independent_evidence_gate"] is True
    assert output["benchmark_executed"] is False
    assert output["verifier_invoked"] is False
    assert output["higher_runtime_started"] is False

    metric_only = deepcopy(probe)
    metric_only["progress_assessment"]["independent_evidence"] = []
    try:
        core.activate(metric_only)
    except ValueError as exc:
        assert str(exc) == "DNA-43_PROGRESS_CANNOT_USE_OPTIMIZED_METRIC_ALONE"
    else:
        raise AssertionError("DNA-43_ACCEPTED_OPTIMIZED_METRIC_AS_SOLE_PROGRESS_PROOF")

    bad_type = deepcopy(probe)
    bad_type["progress_assessment"]["independent_evidence"] = [
        {
            "evidence_id": "E-TRAIN-1",
            "type": "TRAINING_METRIC",
            "result": {"score": 0.99},
        }
    ]
    try:
        core.activate(bad_type)
    except ValueError as exc:
        assert str(exc) == "DNA-43_NON_INDEPENDENT_EVIDENCE_TYPE:TRAINING_METRIC"
    else:
        raise AssertionError("DNA-43_ACCEPTED_TRAINING_METRIC_AS_INDEPENDENT_EVIDENCE")

    held_only = deepcopy(probe)
    held_only["progress_assessment"]["independent_evidence"] = [
        {
            "evidence_id": "E-HELD-ONLY",
            "type": "HELD_OUT",
            "result": {"passed": True},
        }
    ]
    held_output = core.activate(held_only)["core54_outputs"]["DNA-43"]
    assert held_output["held_out_evidence"] is True
    assert held_output["independent_evidence_gate"] is True

    locks = {
        "auto_learning": bool(core54.auto_learning_enabled),
        "model_calls": bool(core54.model_calls_enabled),
        "external_execution": bool(core54.external_execution_enabled),
        "canon_write": bool(core54.canon_write_enabled),
    }
    assert not any(locks.values()), locks

    after = _sha256_file(DNA_JSON) if verify_canon_file else None
    if verify_canon_file:
        assert before == after

    return {
        "core_id": "DNA-43",
        "canon_mapping": "PASS",
        "optimized_metric_alone_rejection": "PASS",
        "external_evidence_gate": "PASS",
        "held_out_evidence_gate": "PASS",
        "independent_evidence_gate": "PASS",
        "benchmark_executed": False,
        "verifier_invoked": False,
        "higher_runtime_started": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": "PASS" if verify_canon_file else "NOT_CHECKED",
        "phase_locks": "PASS",
        "next_authorized": "DNA-44" if verify_canon_file else "RUN_ON_CANONICAL_E_DRIVE",
    }


PRIOR = {
    1:"SIGMA_DNA_01_PURPOSE_EXISTENCE",
    2:"SIGMA_DNA_02_FOUNDATION_INTELLIGENCE_SUBSTRATE",
    3:"SIGMA_DNA_03_UNIFIED_COGNITIVE_STATE",
    4:"SIGMA_DNA_04_EIGHT_COGNITIVE_LAYERS",
    5:"SIGMA_DNA_05_ETHICAL_INTELLIGENCE",
    6:"SIGMA_DNA_06_INTERLAYER_FEEDBACK",
    7:"SIGMA_DNA_07_PERSISTENT_EXISTENCE",
    8:"SIGMA_DNA_08_LEARNING_WORLD",
    9:"SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL",
    10:"SIGMA_DNA_10_MEMORY_GENOME",
    11:"SIGMA_DNA_11_KNOWLEDGE_GRAPH",
    12:"SIGMA_DNA_12_TOOL_INTELLIGENCE",
    13:"SIGMA_DNA_13_ADAPTIVE_COGNITIVE_DEPTH",
    14:"SIGMA_DNA_14_PERSISTENCE_ENGINE",
    15:"SIGMA_DNA_15_F174_DEVELOPMENT_DYNAMICS",
    16:"SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING",
    17:"SIGMA_DNA_17_TWO_LEVELS_OF_LEARNING",
    18:"SIGMA_DNA_18_MODEL_EVOLUTION",
    19:"SIGMA_DNA_19_MULTI_MODEL_INTELLIGENCE",
    20:"SIGMA_DNA_20_UNCERTAINTY_AS_FIRST_CLASS_DATA",
    21:"SIGMA_DNA_21_TRUTH_PROTOCOL",
    22:"SIGMA_DNA_22_HUMAN_RELATION",
    23:"SIGMA_DNA_23_COGNITIVE_FREEDOM",
    24:"SIGMA_DNA_24_ETHICAL_PERSISTENCE",
    25:"SIGMA_DNA_25_SELF_IMPROVEMENT",
    26:"SIGMA_DNA_26_OBSERVABILITY",
    27:"SIGMA_DNA_27_REPRODUCIBILITY",
    28:"SIGMA_DNA_28_SECURITY_OF_KNOWLEDGE",
    29:"SIGMA_DNA_29_COMPUTE_ARCHITECTURE",
    30:"SIGMA_DNA_30_CORE_RUNTIME_LOOP",
    31:"SIGMA_DNA_31_INTELLIGENCE_TEST",
    32:"SIGMA_DNA_32_ACCEPTANCE_CRITERIA",
    33:"SIGMA_DNA_33_PHYSICAL_IMPLEMENTATION_INDEPENDENCE",
    34:"SIGMA_DNA_34_SIGMA_IDENTITY",
    35:"SIGMA_DNA_35_CORE_COVENANT",
    36:"SIGMA_DNA_36_CAUSAL_WORLD_MODEL",
    37:"SIGMA_DNA_37_INTERNAL_SIMULATION",
    38:"SIGMA_DNA_38_GOAL_ARCHITECTURE",
    39:"SIGMA_DNA_39_CURIOSITY_ENGINE",
    40:"SIGMA_DNA_40_CONCEPT_FORMATION",
    41:"SIGMA_DNA_41_REPRESENTATION_INVENTION",
    42:"SIGMA_DNA_42_METACOGNITIVE_SCHEDULER",
}


def main() -> int:
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON]:
        if not path.exists():
            print("DNA-43_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = {
            index: importlib.import_module(name)
            for index, name in PRIOR.items()
        }
    except Exception as exc:
        print("DNA-43_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 43):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna43(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-43_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_43_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("OPTIMIZED_METRIC_ALONE_REJECTION:", report["optimized_metric_alone_rejection"])
    print("EXTERNAL_EVIDENCE_GATE:", report["external_evidence_gate"])
    print("HELD_OUT_EVIDENCE_GATE:", report["held_out_evidence_gate"])
    print("INDEPENDENT_EVIDENCE_GATE:", report["independent_evidence_gate"])
    print("BENCHMARK_EXECUTED:", report["benchmark_executed"])
    print("VERIFIER_INVOKED:", report["verifier_invoked"])
    print("HIGHER_RUNTIME_STARTED:", report["higher_runtime_started"])
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 43/54")
    print("NEXT_AUTHORIZED: DNA-44")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
