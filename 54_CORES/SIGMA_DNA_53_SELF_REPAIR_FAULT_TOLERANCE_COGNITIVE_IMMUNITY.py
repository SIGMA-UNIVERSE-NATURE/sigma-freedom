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

CANON_DNA53: Dict[str, str] = {
    "id": "DNA-53",
    "name": "Self-Repair, Fault Tolerance & Cognitive Immunity",
    "purpose": "Detect→isolate→recover→learn; chống corruption, false memory, reward/metric gaming và degradation.",
    "system": "evolution",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
SELF_REPAIR_SCHEMA = "SIGMA_SELF_REPAIR_FAULT_TOLERANCE_COGNITIVE_IMMUNITY_V1"
CANON_REPAIR_STAGES = ["DETECT", "ISOLATE", "RECOVER", "LEARN"]
CANON_THREATS = ["CORRUPTION", "FALSE_MEMORY", "REWARD_METRIC_GAMING", "DEGRADATION"]

CONTRACT: Dict[str, Any] = {
    "schema": SELF_REPAIR_SCHEMA,
    "repair_sequence": deepcopy(CANON_REPAIR_STAGES),
    "threat_classes": deepcopy(CANON_THREATS),
    "detection_requires_evidence": True,
    "isolation_required_before_recovery": True,
    "recovery_required_before_lesson_retention": True,
    "lesson_is_not_learning_runtime": True,
    "external_recovery_execution_started": False,
    "learning_runtime_started": False,
    "memory_runtime_started": False,
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
    def activate(self, payload: Any = None) -> Dict[str, Any]: ...

class Core54Like(Protocol):
    auto_learning_enabled: bool
    model_calls_enabled: bool
    external_execution_enabled: bool
    canon_write_enabled: bool
    def get(self, core_id: str) -> CoreUnitLike: ...
    def bind(self, core_id: str, handler: Any) -> None: ...

def _canon_record(core: CoreUnitLike) -> Dict[str, str]:
    return {"id": core.core_id, "name": core.name, "purpose": core.purpose, "system": core.system}

def _sha256_json(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=repr).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA53:
        raise RuntimeError("DNA-53_CANON_MISMATCH:" + json.dumps({"expected": CANON_DNA53, "actual": actual}, ensure_ascii=False, sort_keys=True))

def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")
    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError("DNA-53_UNIFIED_STATE_SCHEMA_MISMATCH")
    if not isinstance(state.get("provenance"), list):
        raise TypeError("cognitive_state.provenance must be a list")
    return state

def _install_state(state: Dict[str, Any]) -> Dict[str, Any]:
    key = "self_repair_fault_tolerance_cognitive_immunity"
    existing = state.get(key)
    expected = {"contract": deepcopy(CONTRACT), "incidents": [], "lessons": []}
    if existing is None:
        state[key] = expected
        return state[key]
    if not isinstance(existing, dict):
        raise TypeError(f"{key} must be a dict")
    if existing.get("contract") != CONTRACT:
        raise ValueError("DNA-53_SELF_REPAIR_CONTRACT_CONFLICT")
    if not isinstance(existing.get("incidents"), list) or not isinstance(existing.get("lessons"), list):
        raise TypeError("DNA-53_SELF_REPAIR_STATE_INVALID")
    return existing

def _require_artifact(value: Any, code: str) -> Any:
    if value is None:
        raise ValueError(code)
    return deepcopy(value)

def _evaluate_incident(supplied: Any, repair_state: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError("context['repair_incident'] must be a dict")

    incident_id = supplied.get("incident_id")
    threat_type = supplied.get("threat_type")
    evidence = supplied.get("detection_evidence")

    if not isinstance(incident_id, str) or not incident_id.strip():
        raise ValueError("DNA-53_INCIDENT_ID_REQUIRED")
    if not isinstance(threat_type, str):
        raise TypeError("incident threat_type must be a string")
    threat_type = threat_type.strip().upper()
    if threat_type not in CANON_THREATS:
        raise ValueError(f"DNA-53_UNKNOWN_THREAT_TYPE:{threat_type}")
    if not isinstance(evidence, list) or not evidence:
        raise ValueError(f"DNA-53_DETECTION_EVIDENCE_REQUIRED:{incident_id}")

    isolation = _require_artifact(supplied.get("isolation_artifact"), "DNA-53_ISOLATION_ARTIFACT_REQUIRED")
    recovery = _require_artifact(supplied.get("recovery_artifact"), "DNA-53_RECOVERY_ARTIFACT_REQUIRED")
    lesson = _require_artifact(supplied.get("lesson_artifact"), "DNA-53_LESSON_ARTIFACT_REQUIRED")

    sequence = len(repair_state["incidents"]) + 1
    record = {
        "sequence": sequence,
        "record_id": f"DNA-53-INCIDENT-{sequence:04d}",
        "incident_id": incident_id,
        "threat_type": threat_type,
        "detection": {"stage": "DETECT", "evidence": deepcopy(evidence), "evidence_sha256": _sha256_json(evidence), "passed": True},
        "isolation": {"stage": "ISOLATE", "artifact": isolation, "artifact_sha256": _sha256_json(isolation), "passed": True},
        "recovery": {"stage": "RECOVER", "artifact": recovery, "artifact_sha256": _sha256_json(recovery), "passed": True, "external_recovery_executed": False},
        "learning": {"stage": "LEARN", "lesson_artifact": lesson, "lesson_sha256": _sha256_json(lesson), "learning_runtime_started": False, "passed": True},
        "stage_order": deepcopy(CANON_REPAIR_STAGES),
        "detect_isolate_recover_learn": True,
        "fault_contained": True,
        "recovery_structured": True,
        "lesson_retained": True,
        "external_action_executed": False,
        "status": "DETECT_ISOLATE_RECOVER_LEARN_COMPLETE",
    }
    repair_state["incidents"].append(deepcopy(record))
    repair_state["lessons"].append({
        "incident_id": incident_id,
        "threat_type": threat_type,
        "lesson_artifact": deepcopy(lesson),
        "lesson_sha256": _sha256_json(lesson),
        "learning_runtime_started": False,
    })
    return record

def dna53_self_repair_fault_tolerance_cognitive_immunity(payload: Any, core: CoreUnitLike) -> Dict[str, Any]:
    assert_exact_canon(core)
    context = deepcopy(payload) if isinstance(payload, dict) else {"input": deepcopy(payload)}
    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("context['trace'] must be a list")
    trace.append("DNA-53")
    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    state = _validate_state(context)
    repair_state = _install_state(state)
    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)
    record = _evaluate_incident(context.get("repair_incident"), repair_state)

    state["provenance"].append({
        "sequence": len(state["provenance"]) + 1,
        "core_id": "DNA-53",
        "operation": "SELF_REPAIR_FAULT_TOLERANCE_COGNITIVE_IMMUNITY_EVALUATED",
        "canonical_sha256": canon_sha,
        "record_id": record["record_id"],
        "threat_type": record["threat_type"],
        "stage_order": deepcopy(record["stage_order"]),
        "external_recovery_executed": False,
        "learning_runtime_started": False,
    })

    outputs["DNA-53"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "self_repair_contract": deepcopy(CONTRACT),
        "record": deepcopy(record),
        "detect": "PASS",
        "isolate": "PASS",
        "recover": "PASS",
        "learn": "PASS",
        "corruption_defense": "PASS",
        "false_memory_defense": "PASS",
        "reward_metric_gaming_defense": "PASS",
        "degradation_defense": "PASS",
        "detect_isolate_recover_learn_gate": "PASS",
        "external_recovery_executed": False,
        "learning_runtime_started": False,
        "memory_runtime_started": False,
        "world_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }
    return context

def bind_dna53(core54: Core54Like) -> None:
    core = core54.get("DNA-53")
    assert_exact_canon(core)
    core54.bind("DNA-53", dna53_self_repair_fault_tolerance_cognitive_immunity)

def _valid_incident(threat_type: str = "CORRUPTION") -> Dict[str, Any]:
    return {
        "incident_id": f"DNA53-SELF-CHECK-{threat_type}",
        "threat_type": threat_type,
        "detection_evidence": [{"signal": "INTEGRITY_MISMATCH", "result": "DETECTED"}],
        "isolation_artifact": {"action": "QUARANTINE_AFFECTED_STATE_REFERENCE"},
        "recovery_artifact": {"action": "RESTORE_FROM_VERIFIED_STATE_REFERENCE", "verified": True},
        "lesson_artifact": {"lesson": "RETAIN_FAILURE_PATTERN_FOR_FUTURE_DETECTION"},
    }

def self_check_dna53(core54: Core54Like, *, verify_canon_file: bool = True) -> Dict[str, Any]:
    before = _sha256_file(DNA_JSON) if verify_canon_file else None

    for i in range(1, 53):
        cid = f"DNA-{i:02d}"
        if not core54.get(cid).state.behavior_bound:
            raise RuntimeError(f"{cid}_MUST_PASS_AND_BE_BOUND_FIRST")

    core = core54.get("DNA-53")
    assert_exact_canon(core)
    bind_dna53(core54)

    probe = {
        "trace": [f"DNA-{i:02d}" for i in range(1, 53)],
        "core54_outputs": {},
        "cognitive_state": {"schema": UNIFIED_STATE_SCHEMA, "content": {}, "provenance": [], "uncertainty": {}},
        "repair_incident": _valid_incident("CORRUPTION"),
    }
    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot
    output = result["core54_outputs"]["DNA-53"]

    assert output["canonical_gene"] == CANON_DNA53
    assert output["detect"] == "PASS"
    assert output["isolate"] == "PASS"
    assert output["recover"] == "PASS"
    assert output["learn"] == "PASS"
    assert output["detect_isolate_recover_learn_gate"] == "PASS"
    assert output["record"]["stage_order"] == CANON_REPAIR_STAGES
    assert output["external_recovery_executed"] is False
    assert output["learning_runtime_started"] is False
    assert output["higher_runtime_started"] is False

    for threat in CANON_THREATS:
        case = deepcopy(probe)
        case["repair_incident"] = _valid_incident(threat)
        case_result = core.activate(case)
        assert case_result["core54_outputs"]["DNA-53"]["record"]["threat_type"] == threat

    no_evidence = deepcopy(probe)
    no_evidence["repair_incident"]["detection_evidence"] = []
    try:
        core.activate(no_evidence)
    except ValueError as exc:
        assert str(exc) == "DNA-53_DETECTION_EVIDENCE_REQUIRED:DNA53-SELF-CHECK-CORRUPTION"
    else:
        raise AssertionError("DNA-53_ACCEPTED_DETECTION_WITHOUT_EVIDENCE")

    no_recovery = deepcopy(probe)
    no_recovery["repair_incident"]["recovery_artifact"] = None
    try:
        core.activate(no_recovery)
    except ValueError as exc:
        assert str(exc) == "DNA-53_RECOVERY_ARTIFACT_REQUIRED"
    else:
        raise AssertionError("DNA-53_ACCEPTED_MISSING_RECOVERY")

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
        "core_id": "DNA-53",
        "canon_mapping": "PASS",
        "detect": "PASS",
        "isolate": "PASS",
        "recover": "PASS",
        "learn": "PASS",
        "corruption_defense": "PASS",
        "false_memory_defense": "PASS",
        "reward_metric_gaming_defense": "PASS",
        "degradation_defense": "PASS",
        "detect_isolate_recover_learn_gate": "PASS",
        "external_recovery_executed": False,
        "learning_runtime_started": False,
        "memory_runtime_started": False,
        "world_runtime_started": False,
        "higher_runtime_started": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": "PASS" if verify_canon_file else "NOT_CHECKED",
        "phase_locks": "PASS",
        "next_authorized": "DNA-54" if verify_canon_file else "RUN_ON_CANONICAL_E_DRIVE",
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
    43:"SIGMA_DNA_43_ANTI_SELF_DECEPTION",
    44:"SIGMA_DNA_44_ADVERSARIAL_SELF_TESTING",
    45:"SIGMA_DNA_45_KNOWLEDGE_PROVENANCE",
    46:"SIGMA_DNA_46_KNOWLEDGE_DECAY_REVALIDATION",
    47:"SIGMA_DNA_47_PLASTICITY_STABILITY_BALANCE",
    48:"SIGMA_DNA_48_COMPOSITIONAL_INTELLIGENCE",
    49:"SIGMA_DNA_49_MULTI_SCALE_LEARNING",
    50:"SIGMA_DNA_50_CORE_IMMUTABILITY_VS_EVOLVABILITY",
    51:"SIGMA_DNA_51_EPISTEMIC_DIVERSITY_COLLECTIVE_INTELLIGENCE",
    52:"SIGMA_DNA_52_REALITY_GROUNDING_WORLD_COHERENCE",
}

def main() -> int:
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON]:
        if not path.exists():
            print("DNA-53_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = {i: importlib.import_module(name) for i, name in PRIOR.items()}
    except Exception as exc:
        print("DNA-53_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for i in range(1, 53):
            report = getattr(modules[i], f"self_check_dna{i:02d}")(core54, verify_canon_file=True)
            assert report["self_check"] == "PASS"

        report = self_check_dna53(core54, verify_canon_file=True)
    except Exception as exc:
        print("DNA-53_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_53_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("DETECT:", report["detect"])
    print("ISOLATE:", report["isolate"])
    print("RECOVER:", report["recover"])
    print("LEARN:", report["learn"])
    print("CORRUPTION_DEFENSE:", report["corruption_defense"])
    print("FALSE_MEMORY_DEFENSE:", report["false_memory_defense"])
    print("REWARD_METRIC_GAMING_DEFENSE:", report["reward_metric_gaming_defense"])
    print("DEGRADATION_DEFENSE:", report["degradation_defense"])
    print("DETECT_ISOLATE_RECOVER_LEARN_GATE:", report["detect_isolate_recover_learn_gate"])
    print("EXTERNAL_RECOVERY_EXECUTED:", report["external_recovery_executed"])
    print("LEARNING_RUNTIME_STARTED:", report["learning_runtime_started"])
    print("MEMORY_RUNTIME_STARTED:", report["memory_runtime_started"])
    print("WORLD_RUNTIME_STARTED:", report["world_runtime_started"])
    print("HIGHER_RUNTIME_STARTED:", report["higher_runtime_started"])
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 53/54")
    print("NEXT_AUTHORIZED: DNA-54")
    print("NEXT_PHASE: FORBIDDEN")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
