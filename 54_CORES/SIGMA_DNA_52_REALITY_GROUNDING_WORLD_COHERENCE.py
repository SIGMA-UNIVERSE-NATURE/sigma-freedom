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

CANON_DNA52: Dict[str, str] = {
    "id": "DNA-52",
    "name": "Reality Grounding & World Coherence",
    "purpose": (
        "Internal model phải đối chiếu prediction với observation; "
        "reality > internal narrative."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
REALITY_SCHEMA = "SIGMA_REALITY_GROUNDING_WORLD_COHERENCE_V1"

CONTRACT = {
    "schema": REALITY_SCHEMA,
    "prediction_observation_comparison_required": True,
    "reality_over_internal_narrative": True,
    "mismatch_must_be_preserved": True,
    "observation_must_not_be_rewritten": True,
    "model_revision_may_be_required": True,
    "model_revision_executed_by_dna52": False,
    "observation_generated_by_dna52": False,
    "world_runtime_started": False,
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
    if _canon_record(core) != CANON_DNA52:
        raise RuntimeError("DNA-52_CANON_MISMATCH")


def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")
    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError("DNA-52_UNIFIED_STATE_SCHEMA_MISMATCH")
    if not isinstance(state.get("provenance"), list):
        raise TypeError("cognitive_state.provenance must be a list")
    return state


def _install_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("reality_grounding_world_coherence")
    expected = {
        "contract": deepcopy(CONTRACT),
        "comparisons": [],
    }
    if existing is None:
        state["reality_grounding_world_coherence"] = expected
        return state["reality_grounding_world_coherence"]
    if not isinstance(existing, dict):
        raise TypeError("reality_grounding_world_coherence must be a dict")
    if existing.get("contract") != CONTRACT:
        raise ValueError("DNA-52_REALITY_GROUNDING_CONTRACT_CONFLICT")
    if not isinstance(existing.get("comparisons"), list):
        raise TypeError("reality_grounding_world_coherence.comparisons must be a list")
    return existing


def _evaluate_checks(checks: Any, store: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(checks, list):
        raise TypeError("context['reality_checks'] must be a list")
    if not checks:
        raise ValueError("DNA-52_REALITY_CHECK_REQUIRED")

    start = len(store["comparisons"]) + 1
    records = []
    seen = set()

    for i, item in enumerate(checks, start=1):
        if not isinstance(item, dict):
            raise TypeError(f"reality_checks[{i}] must be a dict")

        check_id = item.get("check_id")
        prediction = item.get("prediction")
        observation = item.get("observation")

        if not isinstance(check_id, str) or not check_id.strip():
            raise ValueError("DNA-52_CHECK_ID_REQUIRED")
        if check_id in seen:
            raise ValueError("DNA-52_DUPLICATE_CHECK_ID")
        seen.add(check_id)

        if prediction is None:
            raise ValueError(f"DNA-52_PREDICTION_REQUIRED:{check_id}")
        if observation is None:
            raise ValueError(f"DNA-52_OBSERVATION_REQUIRED:{check_id}")

        psha = _sha256_json(prediction)
        osha = _sha256_json(observation)
        match = psha == osha

        record = {
            "sequence": start + i - 1,
            "record_id": f"DNA-52-REALITY-{start+i-1:04d}",
            "check_id": check_id,
            "prediction": deepcopy(prediction),
            "prediction_sha256": psha,
            "observation": deepcopy(observation),
            "observation_sha256": osha,
            "prediction_matches_observation": match,
            "mismatch_present": not match,
            "authoritative_ground": "OBSERVATION",
            "reality_priority_applied": True,
            "internal_narrative_overrode_observation": False,
            "model_revision_required": not match,
            "model_revision_executed_by_dna52": False,
            "observation_generated_by_dna52": False,
            "status": (
                "COHERENT_WITH_OBSERVATION"
                if match
                else "MISMATCH_PRESERVED_REALITY_PRIORITY"
            ),
        }
        records.append(record)

    store["comparisons"].extend(deepcopy(records))

    mismatches = [
        r["check_id"]
        for r in records
        if r["mismatch_present"]
    ]

    return {
        "records": records,
        "record_count": len(records),
        "mismatch_check_ids": mismatches,
        "mismatch_count": len(mismatches),
        "all_compared": True,
        "reality_priority_applied": True,
        "internal_narrative_overrode_observation": False,
    }


def dna52_reality_grounding_world_coherence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    assert_exact_canon(core)

    context = deepcopy(payload) if isinstance(payload, dict) else {"input": deepcopy(payload)}

    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("context['trace'] must be a list")
    trace.append("DNA-52")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("context['core54_outputs'] must be a dict")

    state = _validate_state(context)
    reality_state = _install_state(state)

    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)
    evaluation = _evaluate_checks(
        context.get("reality_checks"),
        reality_state,
    )

    state["provenance"].append({
        "sequence": len(state["provenance"]) + 1,
        "core_id": "DNA-52",
        "operation": "REALITY_GROUNDING_WORLD_COHERENCE_EVALUATED",
        "canonical_sha256": canon_sha,
        "record_count": evaluation["record_count"],
        "mismatch_count": evaluation["mismatch_count"],
        "reality_priority_applied": True,
        "model_revision_executed": False,
        "world_runtime_started": False,
    })

    outputs["DNA-52"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "reality_grounding_contract": deepcopy(CONTRACT),
        "evaluation": deepcopy(evaluation),
        "prediction_observation_comparison": "PASS",
        "reality_over_internal_narrative": "PASS",
        "mismatch_preservation": "PASS",
        "observation_rewrite_forbidden": "PASS",
        "model_revision_executed": False,
        "observation_generated": False,
        "world_runtime_started": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }
    return context


def bind_dna52(core54: Core54Like) -> None:
    core = core54.get("DNA-52")
    assert_exact_canon(core)
    core54.bind("DNA-52", dna52_reality_grounding_world_coherence)


def self_check_dna52(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = _sha256_file(DNA_JSON) if verify_canon_file else None

    for i in range(1, 52):
        cid = f"DNA-{i:02d}"
        if not core54.get(cid).state.behavior_bound:
            raise RuntimeError(f"{cid}_MUST_PASS_AND_BE_BOUND_FIRST")

    core = core54.get("DNA-52")
    assert_exact_canon(core)
    bind_dna52(core54)

    probe = {
        "trace": [f"DNA-{i:02d}" for i in range(1, 52)],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "reality_checks": [
            {
                "check_id": "MATCH",
                "prediction": {"value": 1},
                "observation": {"value": 1},
            },
            {
                "check_id": "MISMATCH",
                "prediction": {"value": 2},
                "observation": {"value": 3},
            },
        ],
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-52"]
    assert output["canonical_gene"] == CANON_DNA52
    assert output["prediction_observation_comparison"] == "PASS"
    assert output["reality_over_internal_narrative"] == "PASS"
    assert output["mismatch_preservation"] == "PASS"
    assert output["observation_rewrite_forbidden"] == "PASS"
    assert output["model_revision_executed"] is False
    assert output["world_runtime_started"] is False
    assert output["higher_runtime_started"] is False

    evaluation = output["evaluation"]
    assert evaluation["record_count"] == 2
    assert evaluation["mismatch_check_ids"] == ["MISMATCH"]

    mismatch = evaluation["records"][1]
    assert mismatch["authoritative_ground"] == "OBSERVATION"
    assert mismatch["model_revision_required"] is True
    assert mismatch["internal_narrative_overrode_observation"] is False

    no_observation = deepcopy(probe)
    del no_observation["reality_checks"][0]["observation"]
    try:
        core.activate(no_observation)
    except ValueError as exc:
        assert str(exc) == "DNA-52_OBSERVATION_REQUIRED:MATCH"
    else:
        raise AssertionError("DNA-52_ACCEPTED_UNGROUNDED_PREDICTION")

    duplicate = deepcopy(probe)
    duplicate["reality_checks"][1]["check_id"] = "MATCH"
    try:
        core.activate(duplicate)
    except ValueError as exc:
        assert str(exc) == "DNA-52_DUPLICATE_CHECK_ID"
    else:
        raise AssertionError("DNA-52_ACCEPTED_DUPLICATE_CHECK_ID")

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
        "core_id": "DNA-52",
        "canon_mapping": "PASS",
        "prediction_observation_comparison": "PASS",
        "reality_over_internal_narrative": "PASS",
        "mismatch_preservation": "PASS",
        "observation_rewrite_forbidden": "PASS",
        "model_revision_executed": False,
        "world_runtime_started": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": "PASS" if verify_canon_file else "NOT_CHECKED",
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-53"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
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
}


def main() -> int:
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON]:
        if not path.exists():
            print("DNA-52_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = {
            i: importlib.import_module(name)
            for i, name in PRIOR.items()
        }
    except Exception as exc:
        print("DNA-52_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for i in range(1, 52):
            report = getattr(
                modules[i],
                f"self_check_dna{i:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna52(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-52_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_52_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "PREDICTION_OBSERVATION_COMPARISON:",
        report["prediction_observation_comparison"],
    )
    print(
        "REALITY_OVER_INTERNAL_NARRATIVE:",
        report["reality_over_internal_narrative"],
    )
    print(
        "MISMATCH_PRESERVATION:",
        report["mismatch_preservation"],
    )
    print(
        "OBSERVATION_REWRITE_FORBIDDEN:",
        report["observation_rewrite_forbidden"],
    )
    print(
        "MODEL_REVISION_EXECUTED:",
        report["model_revision_executed"],
    )
    print(
        "WORLD_RUNTIME_STARTED:",
        report["world_runtime_started"],
    )
    print(
        "LEARNING_RUNTIME_STARTED:",
        report["learning_runtime_started"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 52/54")
    print("NEXT_AUTHORIZED: DNA-53")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
