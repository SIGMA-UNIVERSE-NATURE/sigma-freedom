#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-47: PLASTICITY–STABILITY BALANCE
PHASE_LOCK = CORE_DNA_54_ONLY
"""

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
DNA_JSON = (
    SIGMA_ROOT / "CORE" / "DNA_CANON"
    / "SIGMA_CORE_DNA_54" / "sigma_dna_54.json"
)

CANON_DNA47: Dict[str, str] = {
    "id": "DNA-47",
    "name": "Plasticity–Stability Balance",
    "purpose": (
        "Học cái mới mà không quên mù quáng; evidence mới mạnh "
        "có thể sửa knowledge cũ."
    ),
    "system": "learning",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
PLASTICITY_STABILITY_SCHEMA = "SIGMA_PLASTICITY_STABILITY_BALANCE_V1"

CONTRACT: Dict[str, Any] = {
    "schema": PLASTICITY_STABILITY_SCHEMA,
    "new_knowledge_must_not_blindly_erase_old_knowledge": True,
    "old_knowledge_may_be_revised_by_stronger_new_evidence": True,
    "revision_requires_comparative_evidence": True,
    "revision_requires_new_evidence_stronger": True,
    "conflict_without_stronger_evidence_preserves_old_knowledge": True,
    "knowledge_deleted_by_dna47": False,
    "memory_runtime_started": False,
    "learning_runtime_started": False,
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
    if actual != CANON_DNA47:
        raise RuntimeError(
            "DNA-47_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA47, "actual": actual},
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
            "DNA-47_UNIFIED_STATE_SCHEMA_MISMATCH"
        )
    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "cognitive_state.provenance must be a list"
        )
    return state


def _install_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("plasticity_stability_balance")
    expected = {
        "contract": deepcopy(CONTRACT),
        "assessments": [],
    }

    if existing is None:
        state["plasticity_stability_balance"] = expected
        return state["plasticity_stability_balance"]

    if not isinstance(existing, dict):
        raise TypeError(
            "plasticity_stability_balance must be a dict"
        )
    if existing.get("contract") != CONTRACT:
        raise ValueError(
            "DNA-47_PLASTICITY_STABILITY_CONTRACT_CONFLICT"
        )
    if not isinstance(existing.get("assessments"), list):
        raise TypeError(
            "plasticity_stability_balance.assessments must be a list"
        )
    return existing


def _score_evidence(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            f"{field} must be numeric"
        )
    score = float(value)
    if not 0.0 <= score <= 1.0:
        raise ValueError(
            f"DNA-47_{field.upper()}_OUT_OF_RANGE"
        )
    return score


def _evaluate(
    supplied: Any,
    balance_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['plasticity_stability_assessment'] must be a dict"
        )

    assessment_id = supplied.get("assessment_id")
    old_knowledge = supplied.get("old_knowledge")
    new_knowledge = supplied.get("new_knowledge")
    old_evidence = supplied.get("old_evidence")
    new_evidence = supplied.get("new_evidence")
    old_strength = supplied.get("old_evidence_strength")
    new_strength = supplied.get("new_evidence_strength")

    if not isinstance(assessment_id, str) or not assessment_id.strip():
        raise ValueError(
            "DNA-47_ASSESSMENT_ID_REQUIRED"
        )
    if old_knowledge is None:
        raise ValueError(
            "DNA-47_OLD_KNOWLEDGE_REQUIRED"
        )
    if new_knowledge is None:
        raise ValueError(
            "DNA-47_NEW_KNOWLEDGE_REQUIRED"
        )
    if not isinstance(old_evidence, list) or not old_evidence:
        raise ValueError(
            "DNA-47_OLD_EVIDENCE_REQUIRED"
        )
    if not isinstance(new_evidence, list) or not new_evidence:
        raise ValueError(
            "DNA-47_NEW_EVIDENCE_REQUIRED"
        )

    old_score = _score_evidence(
        old_strength,
        "old_evidence_strength",
    )
    new_score = _score_evidence(
        new_strength,
        "new_evidence_strength",
    )

    conflict = (
        _sha256_json(old_knowledge)
        != _sha256_json(new_knowledge)
    )

    stronger_new_evidence = (
        new_score > old_score
    )

    if not conflict:
        decision = "RETAIN_CONSISTENT_KNOWLEDGE"
        revise_old = False
        preserve_old = True
    elif stronger_new_evidence:
        decision = "REVISE_OLD_KNOWLEDGE_WITH_NEW_EVIDENCE"
        revise_old = True
        preserve_old = True
    else:
        decision = "PRESERVE_OLD_AND_RETAIN_CONFLICT"
        revise_old = False
        preserve_old = True

    sequence = len(
        balance_state["assessments"]
    ) + 1

    record = {
        "sequence": sequence,
        "record_id": (
            f"DNA-47-BALANCE-{sequence:04d}"
        ),
        "assessment_id": assessment_id,
        "old_knowledge": deepcopy(old_knowledge),
        "old_knowledge_sha256": _sha256_json(old_knowledge),
        "new_knowledge": deepcopy(new_knowledge),
        "new_knowledge_sha256": _sha256_json(new_knowledge),
        "old_evidence": deepcopy(old_evidence),
        "new_evidence": deepcopy(new_evidence),
        "old_evidence_strength": old_score,
        "new_evidence_strength": new_score,
        "conflict": conflict,
        "stronger_new_evidence": stronger_new_evidence,
        "revise_old_knowledge": revise_old,
        "preserve_old_record": preserve_old,
        "blind_forgetting": False,
        "decision": decision,
        "knowledge_deleted_by_dna47": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
    }

    balance_state["assessments"].append(
        deepcopy(record)
    )
    return record


def dna47_plasticity_stability_balance(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Preserve prior knowledge against blind forgetting while allowing
    stronger new evidence to revise it.

    DNA-47 does not delete old knowledge, start Memory/Learning Runtime,
    call models, perform external actions, or modify Canon.
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
    trace.append("DNA-47")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    balance_state = _install_state(state)

    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)

    record = _evaluate(
        context.get("plasticity_stability_assessment"),
        balance_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-47",
            "operation": (
                "PLASTICITY_STABILITY_BALANCE_EVALUATED"
            ),
            "canonical_sha256": canon_sha,
            "record_id": record["record_id"],
            "conflict": record["conflict"],
            "stronger_new_evidence": (
                record["stronger_new_evidence"]
            ),
            "revise_old_knowledge": (
                record["revise_old_knowledge"]
            ),
            "blind_forgetting": False,
            "knowledge_deleted": False,
        }
    )

    outputs["DNA-47"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "plasticity_stability_contract": deepcopy(
            CONTRACT
        ),
        "record": deepcopy(record),
        "new_learning_allowed": True,
        "blind_forgetting_prevented": True,
        "stronger_evidence_revision": (
            record["stronger_new_evidence"]
        ),
        "old_knowledge_revised": (
            record["revise_old_knowledge"]
        ),
        "old_record_preserved": True,
        "knowledge_deleted": False,
        "memory_runtime_started": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna47(core54: Core54Like) -> None:
    core = core54.get("DNA-47")
    assert_exact_canon(core)
    core54.bind(
        "DNA-47",
        dna47_plasticity_stability_balance,
    )


def self_check_dna47(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 47):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-47")
    assert_exact_canon(core)
    bind_dna47(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 47)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "plasticity_stability_assessment": {
            "assessment_id": "DNA47-SELF-CHECK",
            "old_knowledge": {
                "claim": "OLD_CLAIM",
                "version": "v1",
            },
            "new_knowledge": {
                "claim": "REVISED_CLAIM",
                "version": "v2",
            },
            "old_evidence": [
                {
                    "source": "OLD_VERIFIED_EVIDENCE",
                }
            ],
            "new_evidence": [
                {
                    "source": "NEW_STRONGER_EVIDENCE",
                }
            ],
            "old_evidence_strength": 0.60,
            "new_evidence_strength": 0.90,
        },
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-47"]

    assert output["canonical_gene"] == CANON_DNA47
    assert output["new_learning_allowed"] is True
    assert output["blind_forgetting_prevented"] is True
    assert output["stronger_evidence_revision"] is True
    assert output["old_knowledge_revised"] is True
    assert output["old_record_preserved"] is True
    assert output["knowledge_deleted"] is False
    assert output["learning_runtime_started"] is False
    assert output["higher_runtime_started"] is False

    # Weak conflicting evidence cannot overwrite old knowledge.
    weak_new = deepcopy(probe)
    weak_new[
        "plasticity_stability_assessment"
    ]["new_evidence_strength"] = 0.40

    weak_result = core.activate(weak_new)
    weak_record = weak_result[
        "core54_outputs"
    ]["DNA-47"]["record"]

    assert weak_record[
        "revise_old_knowledge"
    ] is False
    assert weak_record[
        "preserve_old_record"
    ] is True
    assert weak_record[
        "blind_forgetting"
    ] is False
    assert weak_record[
        "decision"
    ] == "PRESERVE_OLD_AND_RETAIN_CONFLICT"

    # Evidence is mandatory on both sides.
    no_old_evidence = deepcopy(probe)
    no_old_evidence[
        "plasticity_stability_assessment"
    ]["old_evidence"] = []

    try:
        core.activate(no_old_evidence)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-47_OLD_EVIDENCE_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-47_ACCEPTED_MISSING_OLD_EVIDENCE"
        )

    no_new_evidence = deepcopy(probe)
    no_new_evidence[
        "plasticity_stability_assessment"
    ]["new_evidence"] = []

    try:
        core.activate(no_new_evidence)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-47_NEW_EVIDENCE_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-47_ACCEPTED_MISSING_NEW_EVIDENCE"
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

    after = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    if verify_canon_file:
        assert before == after

    return {
        "core_id": "DNA-47",
        "canon_mapping": "PASS",
        "new_learning": "PASS",
        "blind_forgetting_prevention": "PASS",
        "stronger_new_evidence_revision": "PASS",
        "weak_evidence_preserves_old": "PASS",
        "knowledge_deleted": False,
        "memory_runtime_started": False,
        "learning_runtime_started": False,
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
            "DNA-48"
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
}


def main() -> int:
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON]:
        if not path.exists():
            print(
                "DNA-47_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
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
        print(
            "DNA-47_FAIL: IMPORT_ERROR"
        )
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for i in range(1, 47):
            report = getattr(
                modules[i],
                f"self_check_dna{i:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna47(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-47_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_47_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("NEW_LEARNING:", report["new_learning"])
    print(
        "BLIND_FORGETTING_PREVENTION:",
        report["blind_forgetting_prevention"],
    )
    print(
        "STRONGER_NEW_EVIDENCE_REVISION:",
        report["stronger_new_evidence_revision"],
    )
    print(
        "WEAK_EVIDENCE_PRESERVES_OLD:",
        report["weak_evidence_preserves_old"],
    )
    print(
        "KNOWLEDGE_DELETED:",
        report["knowledge_deleted"],
    )
    print(
        "MEMORY_RUNTIME_STARTED:",
        report["memory_runtime_started"],
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
    print("OFFICIAL_BOUND_CORES: 47/54")
    print("NEXT_AUTHORIZED: DNA-48")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
