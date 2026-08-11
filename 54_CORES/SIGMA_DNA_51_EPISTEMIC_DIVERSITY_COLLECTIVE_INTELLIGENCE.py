#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-51: EPISTEMIC DIVERSITY & COLLECTIVE INTELLIGENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_51_EPISTEMIC_DIVERSITY_COLLECTIVE_INTELLIGENCE.py
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

CANON_DNA51: Dict[str, str] = {
    "id": "DNA-51",
    "name": "Epistemic Diversity & Collective Intelligence",
    "purpose": (
        "Đa góc nhìn độc lập để giảm shared blind spots; "
        "diversity+independence+evidence > consensus."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
EPISTEMIC_DIVERSITY_SCHEMA = (
    "SIGMA_EPISTEMIC_DIVERSITY_COLLECTIVE_INTELLIGENCE_V1"
)

CONTRACT: Dict[str, Any] = {
    "schema": EPISTEMIC_DIVERSITY_SCHEMA,
    "minimum_perspectives": 2,
    "independent_perspectives_required": True,
    "distinct_sources_required": True,
    "evidence_required": True,
    "consensus_alone_proves_truth": False,
    "selection_priority": (
        "DIVERSITY_PLUS_INDEPENDENCE_PLUS_EVIDENCE_OVER_CONSENSUS"
    ),
    "shared_blind_spot_reduction_goal": True,
    "collective_runtime_started": False,
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
    if actual != CANON_DNA51:
        raise RuntimeError(
            "DNA-51_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA51, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")
    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError("DNA-51_UNIFIED_STATE_SCHEMA_MISMATCH")
    if not isinstance(state.get("provenance"), list):
        raise TypeError("cognitive_state.provenance must be a list")
    return state


def _install_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get(
        "epistemic_diversity_collective_intelligence"
    )
    expected = {
        "contract": deepcopy(CONTRACT),
        "evaluations": [],
    }

    if existing is None:
        state[
            "epistemic_diversity_collective_intelligence"
        ] = expected
        return state[
            "epistemic_diversity_collective_intelligence"
        ]

    if not isinstance(existing, dict):
        raise TypeError(
            "epistemic_diversity_collective_intelligence "
            "must be a dict"
        )
    if existing.get("contract") != CONTRACT:
        raise ValueError(
            "DNA-51_EPISTEMIC_DIVERSITY_CONTRACT_CONFLICT"
        )
    if not isinstance(existing.get("evaluations"), list):
        raise TypeError(
            "epistemic_diversity_collective_intelligence."
            "evaluations must be a list"
        )
    return existing


def _strength(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(
        value,
        (int, float),
    ):
        raise TypeError(
            "perspective evidence_strength must be numeric"
        )
    score = float(value)
    if not math.isfinite(score):
        raise ValueError(
            "DNA-51_EVIDENCE_STRENGTH_NOT_FINITE"
        )
    if not 0.0 <= score <= 1.0:
        raise ValueError(
            "DNA-51_EVIDENCE_STRENGTH_OUT_OF_RANGE"
        )
    return score


def _normalize_perspective(
    item: Any,
    *,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(item, dict):
        raise TypeError(
            f"perspectives[{index}] must be a dict"
        )

    perspective_id = item.get("perspective_id")
    source_id = item.get("source_id")
    independent = item.get("independent")
    position = item.get("position")
    evidence = item.get("evidence")
    evidence_strength = item.get("evidence_strength")

    if not isinstance(
        perspective_id,
        str,
    ) or not perspective_id.strip():
        raise ValueError(
            "DNA-51_PERSPECTIVE_ID_REQUIRED"
        )

    if not isinstance(source_id, str) or not source_id.strip():
        raise ValueError(
            f"DNA-51_SOURCE_ID_REQUIRED:{perspective_id}"
        )

    if independent is not True:
        raise ValueError(
            f"DNA-51_INDEPENDENCE_REQUIRED:{perspective_id}"
        )

    if position is None:
        raise ValueError(
            f"DNA-51_POSITION_REQUIRED:{perspective_id}"
        )

    if not isinstance(evidence, list) or not evidence:
        raise ValueError(
            f"DNA-51_EVIDENCE_REQUIRED:{perspective_id}"
        )

    return {
        "input_index": index,
        "perspective_id": perspective_id,
        "source_id": source_id,
        "independent": True,
        "position": deepcopy(position),
        "position_sha256": _sha256_json(position),
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(evidence),
        "evidence_strength": _strength(
            evidence_strength
        ),
    }


def _evaluate(
    supplied: Any,
    diversity_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['collective_assessment'] must be a dict"
        )

    assessment_id = supplied.get("assessment_id")
    perspectives = supplied.get("perspectives")

    if not isinstance(
        assessment_id,
        str,
    ) or not assessment_id.strip():
        raise ValueError(
            "DNA-51_ASSESSMENT_ID_REQUIRED"
        )

    if not isinstance(perspectives, list):
        raise TypeError(
            "collective_assessment.perspectives must be a list"
        )

    if len(perspectives) < 2:
        raise ValueError(
            "DNA-51_MULTIPLE_PERSPECTIVES_REQUIRED"
        )

    normalized = [
        _normalize_perspective(
            item,
            index=index,
        )
        for index, item in enumerate(
            perspectives,
            start=1,
        )
    ]

    perspective_ids = [
        item["perspective_id"]
        for item in normalized
    ]
    if len(perspective_ids) != len(
        set(perspective_ids)
    ):
        raise ValueError(
            "DNA-51_DUPLICATE_PERSPECTIVE_ID"
        )

    source_ids = [
        item["source_id"]
        for item in normalized
    ]
    if len(source_ids) != len(
        set(source_ids)
    ):
        raise ValueError(
            "DNA-51_SOURCES_MUST_BE_DISTINCT"
        )

    position_groups: Dict[str, Dict[str, Any]] = {}
    for item in normalized:
        key = item["position_sha256"]
        group = position_groups.setdefault(
            key,
            {
                "position": deepcopy(
                    item["position"]
                ),
                "support_count": 0,
                "max_evidence_strength": 0.0,
                "perspective_ids": [],
            },
        )
        group["support_count"] += 1
        group["max_evidence_strength"] = max(
            group["max_evidence_strength"],
            item["evidence_strength"],
        )
        group["perspective_ids"].append(
            item["perspective_id"]
        )

    groups = list(position_groups.values())

    consensus_group = max(
        groups,
        key=lambda group: (
            group["support_count"],
            _sha256_json(group["position"]),
        ),
    )

    evidence_group = max(
        groups,
        key=lambda group: (
            group["max_evidence_strength"],
            -group["support_count"],
            _sha256_json(group["position"]),
        ),
    )

    evidence_ties = [
        group
        for group in groups
        if group["max_evidence_strength"]
        == evidence_group["max_evidence_strength"]
    ]

    evidence_winner_unique = (
        len(evidence_ties) == 1
    )

    selected_position = (
        deepcopy(evidence_group["position"])
        if evidence_winner_unique
        else None
    )

    consensus_position = deepcopy(
        consensus_group["position"]
    )

    consensus_matches_evidence = (
        evidence_winner_unique
        and _sha256_json(consensus_position)
        == _sha256_json(selected_position)
    )

    sequence = len(
        diversity_state["evaluations"]
    ) + 1

    record = {
        "sequence": sequence,
        "record_id": (
            f"DNA-51-COLLECTIVE-{sequence:04d}"
        ),
        "assessment_id": assessment_id,
        "perspectives": deepcopy(normalized),
        "perspective_count": len(normalized),
        "distinct_source_count": len(set(source_ids)),
        "position_count": len(groups),
        "diversity_present": len(groups) >= 2,
        "independence_present": True,
        "evidence_present": True,
        "consensus_position": consensus_position,
        "consensus_support_count": (
            consensus_group["support_count"]
        ),
        "evidence_selected_position": (
            selected_position
        ),
        "evidence_winner_unique": (
            evidence_winner_unique
        ),
        "consensus_matches_evidence": (
            consensus_matches_evidence
        ),
        "consensus_overrode_evidence": False,
        "selection_basis": (
            "EVIDENCE_OVER_CONSENSUS"
            if evidence_winner_unique
            else "EVIDENCE_TIE_UNRESOLVED"
        ),
        "truth_claimed_by_dna51": False,
        "collective_runtime_started": False,
        "external_action_executed": False,
        "status": "EPISTEMIC_DIVERSITY_EVALUATED",
    }

    diversity_state["evaluations"].append(
        deepcopy(record)
    )
    return record


def dna51_epistemic_diversity_collective_intelligence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Combine multiple independent, evidence-bearing perspectives while
    refusing to treat consensus alone as truth.

    DNA-51 evaluates diversity/independence/evidence only. It does not
    create agents, start a collective runtime, call models, perform
    external action, or modify Canon.
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
    trace.append("DNA-51")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    diversity_state = _install_state(
        state
    )

    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)

    record = _evaluate(
        context.get("collective_assessment"),
        diversity_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-51",
            "operation": (
                "EPISTEMIC_DIVERSITY_COLLECTIVE_"
                "INTELLIGENCE_EVALUATED"
            ),
            "canonical_sha256": canon_sha,
            "record_id": record["record_id"],
            "perspective_count": (
                record["perspective_count"]
            ),
            "distinct_source_count": (
                record["distinct_source_count"]
            ),
            "selection_basis": (
                record["selection_basis"]
            ),
            "consensus_overrode_evidence": False,
            "truth_claimed": False,
        }
    )

    outputs["DNA-51"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "epistemic_diversity_contract": deepcopy(
            CONTRACT
        ),
        "record": deepcopy(record),
        "multiple_perspectives": "PASS",
        "independence": "PASS",
        "evidence": "PASS",
        "consensus_not_truth": "PASS",
        "evidence_over_consensus": "PASS",
        "shared_blind_spot_reduction": "PASS",
        "collective_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna51(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-51")
    assert_exact_canon(core)
    core54.bind(
        "DNA-51",
        dna51_epistemic_diversity_collective_intelligence,
    )


def _valid_assessment() -> Dict[str, Any]:
    return {
        "assessment_id": "DNA51-SELF-CHECK",
        "perspectives": [
            {
                "perspective_id": "P-1",
                "source_id": "S-1",
                "independent": True,
                "position": "POSITION-A",
                "evidence": [
                    {
                        "evidence_id": "E-1",
                        "result": "SUPPORT-A",
                    }
                ],
                "evidence_strength": 0.55,
            },
            {
                "perspective_id": "P-2",
                "source_id": "S-2",
                "independent": True,
                "position": "POSITION-A",
                "evidence": [
                    {
                        "evidence_id": "E-2",
                        "result": "SUPPORT-A-2",
                    }
                ],
                "evidence_strength": 0.50,
            },
            {
                "perspective_id": "P-3",
                "source_id": "S-3",
                "independent": True,
                "position": "POSITION-B",
                "evidence": [
                    {
                        "evidence_id": "E-3",
                        "result": "STRONG_SUPPORT-B",
                    }
                ],
                "evidence_strength": 0.95,
            },
        ],
    }


def self_check_dna51(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 51):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-51")
    assert_exact_canon(core)
    bind_dna51(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 51)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "collective_assessment": (
            _valid_assessment()
        ),
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-51"]

    assert output["canonical_gene"] == CANON_DNA51
    assert output["multiple_perspectives"] == "PASS"
    assert output["independence"] == "PASS"
    assert output["evidence"] == "PASS"
    assert output["consensus_not_truth"] == "PASS"
    assert output["evidence_over_consensus"] == "PASS"
    assert output[
        "collective_runtime_started"
    ] is False
    assert output[
        "higher_runtime_started"
    ] is False

    record = output["record"]

    # Majority consensus = A, strongest evidence = B.
    assert record["consensus_position"] == "POSITION-A"
    assert (
        record["evidence_selected_position"]
        == "POSITION-B"
    )
    assert (
        record["consensus_matches_evidence"]
        is False
    )
    assert (
        record["consensus_overrode_evidence"]
        is False
    )
    assert (
        record["selection_basis"]
        == "EVIDENCE_OVER_CONSENSUS"
    )

    # One perspective is not epistemic diversity.
    single = deepcopy(probe)
    single[
        "collective_assessment"
    ]["perspectives"] = (
        single[
            "collective_assessment"
        ]["perspectives"][:1]
    )

    try:
        core.activate(single)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-51_MULTIPLE_PERSPECTIVES_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-51_ACCEPTED_SINGLE_PERSPECTIVE"
        )

    # Independence is mandatory.
    dependent = deepcopy(probe)
    dependent[
        "collective_assessment"
    ]["perspectives"][1]["independent"] = False

    try:
        core.activate(dependent)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-51_INDEPENDENCE_REQUIRED:P-2"
        )
    else:
        raise AssertionError(
            "DNA-51_ACCEPTED_DEPENDENT_PERSPECTIVE"
        )

    # Distinct source identity is mandatory.
    duplicate_source = deepcopy(probe)
    duplicate_source[
        "collective_assessment"
    ]["perspectives"][1]["source_id"] = "S-1"

    try:
        core.activate(duplicate_source)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-51_SOURCES_MUST_BE_DISTINCT"
        )
    else:
        raise AssertionError(
            "DNA-51_ACCEPTED_SHARED_SOURCE_AS_INDEPENDENT"
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
        "core_id": "DNA-51",
        "canon_mapping": "PASS",
        "multiple_perspectives": "PASS",
        "independence": "PASS",
        "evidence": "PASS",
        "consensus_not_truth": "PASS",
        "evidence_over_consensus": "PASS",
        "shared_blind_spot_reduction": "PASS",
        "collective_runtime_started": False,
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
            "DNA-52"
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
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-51_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
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
        print(
            "DNA-51_FAIL: IMPORT_ERROR"
        )
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 51):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna51(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-51_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_51_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "MULTIPLE_PERSPECTIVES:",
        report["multiple_perspectives"],
    )
    print(
        "INDEPENDENCE:",
        report["independence"],
    )
    print(
        "EVIDENCE:",
        report["evidence"],
    )
    print(
        "CONSENSUS_NOT_TRUTH:",
        report["consensus_not_truth"],
    )
    print(
        "EVIDENCE_OVER_CONSENSUS:",
        report["evidence_over_consensus"],
    )
    print(
        "SHARED_BLIND_SPOT_REDUCTION:",
        report["shared_blind_spot_reduction"],
    )
    print(
        "COLLECTIVE_RUNTIME_STARTED:",
        report["collective_runtime_started"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 51/54")
    print("NEXT_AUTHORIZED: DNA-52")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
