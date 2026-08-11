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

CANON_DNA41: Dict[str, str] = {
    "id": "DNA-41",
    "name": "Representation Invention",
    "purpose": (
        "Có thể đổi hoặc phát minh representation khi representation "
        "hiện tại gây stagnation."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
REPRESENTATION_INVENTION_SCHEMA = "SIGMA_REPRESENTATION_INVENTION_V1"

REPRESENTATION_INVENTION_CONTRACT: Dict[str, Any] = {
    "schema": REPRESENTATION_INVENTION_SCHEMA,
    "stagnation_requires_evidence": True,
    "transition_modes": ["CHANGE", "INVENT"],
    "new_representation_must_differ": True,
    "invent_mode_requires_concrete_artifact": True,
    "representation_transition_updates_structured_state": True,
    "model_calls_started": False,
    "tool_execution_started": False,
    "learning_runtime_started": False,
    "world_runtime_started": False,
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
    if actual != CANON_DNA41:
        raise RuntimeError(f"DNA-41_CANON_MISMATCH:{actual!r}")


def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")
    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError("DNA-41_UNIFIED_STATE_SCHEMA_MISMATCH")
    if not isinstance(state.get("provenance"), list):
        raise TypeError("cognitive_state.provenance must be a list")
    return state


def _install(state: Dict[str, Any]) -> Dict[str, Any]:
    x = state.get("representation_invention")
    if x is None:
        x = {
            "contract": deepcopy(REPRESENTATION_INVENTION_CONTRACT),
            "active_representation": None,
            "transitions": [],
        }
        state["representation_invention"] = x
    if x.get("contract") != REPRESENTATION_INVENTION_CONTRACT:
        raise ValueError("DNA-41_REPRESENTATION_CONTRACT_CONFLICT")
    if not isinstance(x.get("transitions"), list):
        raise TypeError("representation_invention.transitions must be a list")
    return x


def _normalize_representation(value: Any, role: str) -> Dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError(f"{role} representation must be a dict")

    representation_id = value.get("representation_id")
    artifact = value.get("artifact")

    if not isinstance(representation_id, str) or not representation_id.strip():
        raise ValueError(
            f"DNA-41_{role.upper()}_REPRESENTATION_ID_REQUIRED"
        )
    if artifact is None:
        raise ValueError(
            f"DNA-41_{role.upper()}_REPRESENTATION_ARTIFACT_REQUIRED"
        )

    return {
        "representation_id": representation_id,
        "artifact": deepcopy(artifact),
        "artifact_sha256": _sha256_json(artifact),
    }


def _evaluate_transition(
    supplied: Any,
    rep_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError("representation_transition must be a dict")

    transition_id = supplied.get("transition_id")
    if not isinstance(transition_id, str) or not transition_id.strip():
        raise ValueError("DNA-41_TRANSITION_ID_REQUIRED")

    current = _normalize_representation(
        supplied.get("current_representation"),
        "current",
    )

    stagnation = supplied.get("stagnation")
    if not isinstance(stagnation, dict):
        raise TypeError("stagnation must be a dict")

    detected = stagnation.get("detected")
    evidence = stagnation.get("evidence", [])

    if not isinstance(detected, bool):
        raise TypeError("stagnation.detected must be a bool")
    if not isinstance(evidence, list):
        raise TypeError("stagnation.evidence must be a list")
    if detected and not evidence:
        raise ValueError("DNA-41_STAGNATION_REQUIRES_EVIDENCE")

    proposal = supplied.get("proposal")

    if not detected:
        if proposal is not None:
            raise ValueError(
                "DNA-41_REPRESENTATION_CHANGE_REQUIRES_STAGNATION"
            )
        rep_state["active_representation"] = deepcopy(current)
        sequence = len(rep_state["transitions"]) + 1
        record = {
            "sequence": sequence,
            "record_id": f"DNA-41-REP-{sequence:04d}",
            "transition_id": transition_id,
            "current_representation": deepcopy(current),
            "stagnation_detected": False,
            "mode": None,
            "new_representation": None,
            "representation_changed": False,
            "representation_invented": False,
            "active_representation": deepcopy(current),
            "status": "CURRENT_REPRESENTATION_RETAINED",
        }
        rep_state["transitions"].append(deepcopy(record))
        return record

    if not isinstance(proposal, dict):
        raise ValueError(
            "DNA-41_STAGNATION_REQUIRES_REPRESENTATION_PROPOSAL"
        )

    mode = proposal.get("mode")
    if not isinstance(mode, str):
        raise TypeError("proposal.mode must be a string")
    mode = mode.strip().upper()

    if mode not in {"CHANGE", "INVENT"}:
        raise ValueError(f"DNA-41_UNKNOWN_TRANSITION_MODE:{mode}")

    proposed = _normalize_representation(
        proposal,
        "new",
    )

    rationale = proposal.get("rationale")
    if not isinstance(rationale, list) or not rationale:
        raise ValueError("DNA-41_REPRESENTATION_RATIONALE_REQUIRED")

    if (
        proposed["representation_id"] == current["representation_id"]
        or proposed["artifact_sha256"] == current["artifact_sha256"]
    ):
        raise ValueError("DNA-41_NEW_REPRESENTATION_MUST_DIFFER")

    rep_state["active_representation"] = deepcopy(proposed)
    sequence = len(rep_state["transitions"]) + 1

    record = {
        "sequence": sequence,
        "record_id": f"DNA-41-REP-{sequence:04d}",
        "transition_id": transition_id,
        "current_representation": deepcopy(current),
        "stagnation_detected": True,
        "stagnation_evidence": deepcopy(evidence),
        "stagnation_evidence_sha256": _sha256_json(evidence),
        "mode": mode,
        "rationale": deepcopy(rationale),
        "new_representation": deepcopy(proposed),
        "representation_changed": True,
        "representation_invented": mode == "INVENT",
        "active_representation": deepcopy(proposed),
        "model_called_to_invent": False,
        "external_action_executed": False,
        "status": (
            "REPRESENTATION_INVENTED_AND_ACTIVATED"
            if mode == "INVENT"
            else "REPRESENTATION_CHANGED_AND_ACTIVATED"
        ),
    }

    rep_state["transitions"].append(deepcopy(record))
    return record


def dna41_representation_invention(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    assert_exact_canon(core)

    context = (
        deepcopy(payload)
        if isinstance(payload, dict)
        else {"input": deepcopy(payload)}
    )

    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("trace must be a list")
    trace.append("DNA-41")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("core54_outputs must be a dict")

    state = _validate_state(context)
    rep_state = _install(state)

    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)
    record = _evaluate_transition(
        context.get("representation_transition"),
        rep_state,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-41",
            "operation": "REPRESENTATION_TRANSITION_EVALUATED",
            "canonical_sha256": canon_sha,
            "record_id": record["record_id"],
            "stagnation_detected": record["stagnation_detected"],
            "mode": record["mode"],
            "representation_changed": record["representation_changed"],
            "representation_invented": record["representation_invented"],
            "model_calls_started": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-41"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "representation_invention_contract": deepcopy(
            REPRESENTATION_INVENTION_CONTRACT
        ),
        "record": deepcopy(record),
        "stagnation_detected": record["stagnation_detected"],
        "representation_changed": record["representation_changed"],
        "representation_invented": record["representation_invented"],
        "active_representation": deepcopy(
            record["active_representation"]
        ),
        "model_calls_started": False,
        "tool_execution_started": False,
        "learning_runtime_started": False,
        "world_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }
    return context


def bind_dna41(core54: Core54Like) -> None:
    core = core54.get("DNA-41")
    assert_exact_canon(core)
    core54.bind("DNA-41", dna41_representation_invention)


def self_check_dna41(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = _sha256_file(DNA_JSON) if verify_canon_file else None

    for i in range(1, 41):
        if not core54.get(f"DNA-{i:02d}").state.behavior_bound:
            raise RuntimeError(
                f"DNA-{i:02d}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-41")
    assert_exact_canon(core)
    bind_dna41(core54)

    probe = {
        "trace": [f"DNA-{i:02d}" for i in range(1, 41)],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "representation_transition": {
            "transition_id": "DNA41-SELF-CHECK",
            "current_representation": {
                "representation_id": "REP-OLD",
                "artifact": {
                    "type": "LINEAR_FEATURE_SPACE",
                    "dimensions": ["x", "y"],
                },
            },
            "stagnation": {
                "detected": True,
                "evidence": [
                    {
                        "type": "NO_INFORMATION_GAIN",
                        "result": "REPEATED_STAGNATION",
                    }
                ],
            },
            "proposal": {
                "mode": "INVENT",
                "representation_id": "REP-NEW",
                "artifact": {
                    "type": "RELATIONAL_GRAPH",
                    "nodes": ["x", "y"],
                    "edges": [["x", "y"]],
                },
                "rationale": [
                    {
                        "reason": (
                            "CURRENT_REPRESENTATION_FAILED_TO_EXPOSE_RELATION"
                        )
                    }
                ],
            },
        },
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-41"]
    assert output["canonical_gene"] == CANON_DNA41
    assert output["stagnation_detected"] is True
    assert output["representation_changed"] is True
    assert output["representation_invented"] is True
    assert output["active_representation"]["representation_id"] == "REP-NEW"
    assert output["model_calls_started"] is False
    assert output["learning_runtime_started"] is False
    assert output["higher_runtime_started"] is False

    stable = deepcopy(probe)
    stable["representation_transition"] = {
        "transition_id": "DNA41-STABLE",
        "current_representation": {
            "representation_id": "REP-STABLE",
            "artifact": {"type": "CURRENT"},
        },
        "stagnation": {
            "detected": False,
            "evidence": [],
        },
        "proposal": None,
    }
    stable_result = core.activate(stable)
    assert stable_result[
        "core54_outputs"
    ]["DNA-41"]["representation_changed"] is False

    no_evidence = deepcopy(probe)
    no_evidence[
        "representation_transition"
    ]["stagnation"]["evidence"] = []

    try:
        core.activate(no_evidence)
    except ValueError as exc:
        assert str(exc) == "DNA-41_STAGNATION_REQUIRES_EVIDENCE"
    else:
        raise AssertionError(
            "DNA-41_ACCEPTED_UNEVIDENCED_STAGNATION"
        )

    same = deepcopy(probe)
    same["representation_transition"]["proposal"]["representation_id"] = "REP-OLD"
    same["representation_transition"]["proposal"]["artifact"] = {
        "type": "LINEAR_FEATURE_SPACE",
        "dimensions": ["x", "y"],
    }

    try:
        core.activate(same)
    except ValueError as exc:
        assert str(exc) == "DNA-41_NEW_REPRESENTATION_MUST_DIFFER"
    else:
        raise AssertionError(
            "DNA-41_ACCEPTED_IDENTICAL_REPRESENTATION"
        )

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
        "core_id": "DNA-41",
        "canon_mapping": "PASS",
        "stagnation_evidence_gate": "PASS",
        "representation_change": "PASS",
        "representation_invention": "PASS",
        "new_representation_difference_gate": "PASS",
        "model_calls_started": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": "PASS" if verify_canon_file else "NOT_CHECKED",
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-42"
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
}


def main() -> int:
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON]:
        if not path.exists():
            print("DNA-41_FAIL: REQUIRED_PATH_NOT_FOUND")
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
        print("DNA-41_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for i in range(1, 41):
            report = getattr(
                modules[i],
                f"self_check_dna{i:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna41(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-41_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_41_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "STAGNATION_EVIDENCE_GATE:",
        report["stagnation_evidence_gate"],
    )
    print(
        "REPRESENTATION_CHANGE:",
        report["representation_change"],
    )
    print(
        "REPRESENTATION_INVENTION:",
        report["representation_invention"],
    )
    print(
        "NEW_REPRESENTATION_DIFFERENCE_GATE:",
        report["new_representation_difference_gate"],
    )
    print(
        "MODEL_CALLS_STARTED:",
        report["model_calls_started"],
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
    print("OFFICIAL_BOUND_CORES: 41/54")
    print("NEXT_AUTHORIZED: DNA-42")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
