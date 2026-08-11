#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-38: GOAL ARCHITECTURE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_38_GOAL_ARCHITECTURE.py
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

CANON_DNA38: Dict[str, str] = {
    "id": "DNA-38",
    "name": "Goal Architecture",
    "purpose": (
        "Purpose→Goal→Subgoal→Task→Action; failure đổi action/plan, "
        "goal sai thì được xem xét lại."
    ),
    "system": "evolution",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
GOAL_ARCHITECTURE_SCHEMA = "SIGMA_GOAL_ARCHITECTURE_V1"

CANON_LEVELS = [
    "PURPOSE",
    "GOAL",
    "SUBGOAL",
    "TASK",
    "ACTION",
]

GOAL_ARCHITECTURE_CONTRACT: Dict[str, Any] = {
    "schema": GOAL_ARCHITECTURE_SCHEMA,
    "ordered_levels": deepcopy(CANON_LEVELS),
    "level_count": 5,
    "failure_changes_action_or_plan_first": True,
    "goal_reconsideration_allowed_when_goal_is_wrong": True,
    "goal_reconsideration_requires_evidence": True,
    "failure_alone_does_not_invalidate_goal": True,
    "goal_changed_by_dna38": False,
    "action_executed_by_dna38": False,
    "planning_runtime_started": False,
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
    if actual != CANON_DNA38:
        raise RuntimeError(
            "DNA-38_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA38, "actual": actual},
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
            "DNA-38_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )
    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )
    return state


def _install_goal_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("goal_architecture")
    expected = {
        "contract": deepcopy(GOAL_ARCHITECTURE_CONTRACT),
        "architectures": [],
        "failure_reviews": [],
    }

    if existing is None:
        state["goal_architecture"] = expected
        return state["goal_architecture"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['goal_architecture'] must be a dict"
        )
    if existing.get("contract") != GOAL_ARCHITECTURE_CONTRACT:
        raise ValueError(
            "DNA-38_GOAL_ARCHITECTURE_CONTRACT_CONFLICT"
        )
    if not isinstance(existing.get("architectures"), list):
        raise TypeError(
            "goal_architecture['architectures'] must be a list"
        )
    if not isinstance(existing.get("failure_reviews"), list):
        raise TypeError(
            "goal_architecture['failure_reviews'] must be a list"
        )
    return existing


def _normalize_node(
    supplied: Any,
    *,
    level: str,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"goal_architecture['chain'][{index}] must be a dict"
        )

    node_level = supplied.get("level")
    node_id = supplied.get("id")
    content = supplied.get("content")

    if not isinstance(node_level, str):
        raise TypeError(
            f"goal node {index} level must be a string"
        )

    node_level = node_level.strip().upper()
    if node_level != level:
        raise ValueError(
            "DNA-38_LEVEL_ORDER_MISMATCH:"
            f"expected={level}:actual={node_level}"
        )

    if not isinstance(node_id, str) or not node_id.strip():
        raise ValueError(
            f"DNA-38_NODE_ID_REQUIRED:{level}"
        )

    if content is None:
        raise ValueError(
            f"DNA-38_NODE_CONTENT_REQUIRED:{level}"
        )

    return {
        "index": index + 1,
        "level": level,
        "id": node_id,
        "content": deepcopy(content),
        "content_sha256": _sha256_json(content),
    }


def _normalize_architecture(
    supplied: Any,
    state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['goal_architecture_input'] must be a dict"
        )

    architecture_id = supplied.get("architecture_id")
    chain = supplied.get("chain")

    if not isinstance(architecture_id, str) or not architecture_id.strip():
        raise ValueError(
            "DNA-38_ARCHITECTURE_ID_REQUIRED"
        )
    if not isinstance(chain, list):
        raise TypeError(
            "goal_architecture_input['chain'] must be a list"
        )
    if len(chain) != 5:
        raise ValueError(
            "DNA-38_EXACT_FIVE_LEVELS_REQUIRED"
        )

    normalized = [
        _normalize_node(
            item,
            level=CANON_LEVELS[index],
            index=index,
        )
        for index, item in enumerate(chain)
    ]

    sequence = len(state["architectures"]) + 1
    record = {
        "sequence": sequence,
        "record_id": (
            f"DNA-38-GOAL-ARCH-{sequence:04d}"
        ),
        "architecture_id": architecture_id,
        "chain": deepcopy(normalized),
        "level_order": [
            item["level"]
            for item in normalized
        ],
        "purpose_id": normalized[0]["id"],
        "goal_id": normalized[1]["id"],
        "subgoal_id": normalized[2]["id"],
        "task_id": normalized[3]["id"],
        "action_id": normalized[4]["id"],
        "chain_sha256": _sha256_json(normalized),
        "status": "GOAL_ARCHITECTURE_VALID",
    }

    state["architectures"].append(deepcopy(record))
    return record


def _evaluate_failure(
    supplied: Any,
    architecture: Dict[str, Any],
    goal_state: Dict[str, Any],
) -> Dict[str, Any]:
    if supplied is None:
        return {
            "failure_present": False,
            "action_or_plan_change_required": False,
            "goal_review_required": False,
            "goal_changed_by_dna38": False,
            "status": "NO_FAILURE_SUPPLIED",
        }

    if not isinstance(supplied, dict):
        raise TypeError(
            "context['goal_failure'] must be a dict or None"
        )

    failure_id = supplied.get("failure_id")
    failed_level = supplied.get("failed_level")
    evidence = supplied.get("evidence", [])
    goal_invalid = supplied.get("goal_invalid", False)

    if not isinstance(failure_id, str) or not failure_id.strip():
        raise ValueError(
            "DNA-38_FAILURE_ID_REQUIRED"
        )

    if not isinstance(failed_level, str):
        raise TypeError(
            "goal_failure['failed_level'] must be a string"
        )
    failed_level = failed_level.strip().upper()

    if failed_level not in {
        "ACTION",
        "TASK",
        "SUBGOAL",
        "GOAL",
    }:
        raise ValueError(
            f"DNA-38_INVALID_FAILED_LEVEL:{failed_level}"
        )

    if not isinstance(evidence, list):
        raise TypeError(
            "goal_failure['evidence'] must be a list"
        )

    if not isinstance(goal_invalid, bool):
        raise TypeError(
            "goal_failure['goal_invalid'] must be a bool"
        )

    if goal_invalid and not evidence:
        raise ValueError(
            "DNA-38_GOAL_INVALIDATION_REQUIRES_EVIDENCE"
        )

    action_or_plan_change_required = True
    goal_review_required = bool(goal_invalid)

    sequence = len(
        goal_state["failure_reviews"]
    ) + 1

    review = {
        "sequence": sequence,
        "review_id": (
            f"DNA-38-FAILURE-REVIEW-{sequence:04d}"
        ),
        "failure_id": failure_id,
        "architecture_id": architecture["architecture_id"],
        "failed_level": failed_level,
        "evidence": deepcopy(evidence),
        "evidence_sha256": (
            _sha256_json(evidence)
            if evidence
            else None
        ),
        "goal_invalid": goal_invalid,
        "action_or_plan_change_required": (
            action_or_plan_change_required
        ),
        "goal_review_required": goal_review_required,
        "goal_changed_by_dna38": False,
        "action_executed_by_dna38": False,
        "status": (
            "GOAL_REVIEW_REQUIRED"
            if goal_review_required
            else "CHANGE_ACTION_OR_PLAN_KEEP_GOAL"
        ),
    }

    goal_state["failure_reviews"].append(
        deepcopy(review)
    )

    return {
        "failure_present": True,
        **deepcopy(review),
    }


def dna38_goal_architecture(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Enforce Purpose→Goal→Subgoal→Task→Action.

    Failure changes action/plan first. A goal is only sent to review when
    supplied evidence explicitly indicates the goal is wrong. DNA-38 never
    changes the goal by itself and executes no external action.
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
    trace.append("DNA-38")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    cognitive = _validate_state(context)
    goal_state = _install_goal_state(cognitive)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    architecture = _normalize_architecture(
        context.get("goal_architecture_input"),
        goal_state,
    )

    failure_review = _evaluate_failure(
        context.get("goal_failure"),
        architecture,
        goal_state,
    )

    cognitive["provenance"].append(
        {
            "sequence": len(
                cognitive["provenance"]
            ) + 1,
            "core_id": "DNA-38",
            "operation": (
                "GOAL_ARCHITECTURE_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "architecture_id": (
                architecture["architecture_id"]
            ),
            "level_order": deepcopy(
                architecture["level_order"]
            ),
            "failure_present": (
                failure_review["failure_present"]
            ),
            "goal_review_required": (
                failure_review[
                    "goal_review_required"
                ]
            ),
            "goal_changed_by_dna38": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-38"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "goal_architecture_contract": deepcopy(
            GOAL_ARCHITECTURE_CONTRACT
        ),
        "architecture": deepcopy(architecture),
        "failure_review": deepcopy(failure_review),
        "purpose_goal_subgoal_task_action": "PASS",
        "failure_changes_action_or_plan_first": True,
        "goal_review_allowed": True,
        "goal_changed_by_dna38": False,
        "action_executed": False,
        "planning_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna38(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-38")
    assert_exact_canon(core)
    core54.bind(
        "DNA-38",
        dna38_goal_architecture,
    )


def _valid_architecture() -> Dict[str, Any]:
    return {
        "architecture_id": "DNA38-SELF-CHECK",
        "chain": [
            {
                "level": "PURPOSE",
                "id": "P1",
                "content": "Human benefit",
            },
            {
                "level": "GOAL",
                "id": "G1",
                "content": "Achieve verified outcome",
            },
            {
                "level": "SUBGOAL",
                "id": "SG1",
                "content": "Resolve prerequisite",
            },
            {
                "level": "TASK",
                "id": "T1",
                "content": "Run next task",
            },
            {
                "level": "ACTION",
                "id": "A1",
                "content": "Attempt method A",
            },
        ],
    }


def self_check_dna38(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 38):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-38")
    assert_exact_canon(core)
    bind_dna38(core54)

    base = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 38)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "goal_architecture_input": (
            _valid_architecture()
        ),
    }

    # Failure alone changes action/plan, not goal.
    probe = deepcopy(base)
    probe["goal_failure"] = {
        "failure_id": "F1",
        "failed_level": "ACTION",
        "evidence": [
            {
                "type": "ACTION_FAILURE",
                "result": "METHOD_A_FAILED",
            }
        ],
        "goal_invalid": False,
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-38"]

    assert output["canonical_gene"] == CANON_DNA38
    assert output[
        "purpose_goal_subgoal_task_action"
    ] == "PASS"
    assert output[
        "failure_changes_action_or_plan_first"
    ] is True
    assert output["goal_changed_by_dna38"] is False
    assert output["action_executed"] is False
    assert output["higher_runtime_started"] is False

    architecture = output["architecture"]
    assert architecture["level_order"] == CANON_LEVELS

    review = output["failure_review"]
    assert review["failure_present"] is True
    assert (
        review["action_or_plan_change_required"]
        is True
    )
    assert review["goal_review_required"] is False
    assert review["goal_changed_by_dna38"] is False
    assert review["status"] == (
        "CHANGE_ACTION_OR_PLAN_KEEP_GOAL"
    )

    # Evidence that goal itself is wrong allows goal review.
    wrong_goal = deepcopy(base)
    wrong_goal["goal_failure"] = {
        "failure_id": "F2",
        "failed_level": "GOAL",
        "evidence": [
            {
                "type": "GOAL_INVALIDATION_EVIDENCE",
                "result": "GOAL_CONFLICTS_WITH_PURPOSE",
            }
        ],
        "goal_invalid": True,
    }

    wrong_result = core.activate(
        wrong_goal
    )
    wrong_review = wrong_result[
        "core54_outputs"
    ]["DNA-38"]["failure_review"]

    assert wrong_review[
        "goal_review_required"
    ] is True
    assert wrong_review[
        "goal_changed_by_dna38"
    ] is False
    assert wrong_review["status"] == (
        "GOAL_REVIEW_REQUIRED"
    )

    # Goal invalidation without evidence is forbidden.
    invalid_claim = deepcopy(base)
    invalid_claim["goal_failure"] = {
        "failure_id": "F3",
        "failed_level": "GOAL",
        "evidence": [],
        "goal_invalid": True,
    }

    try:
        core.activate(invalid_claim)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-38_GOAL_INVALIDATION_REQUIRES_EVIDENCE"
        )
    else:
        raise AssertionError(
            "DNA-38_ACCEPTED_UNEVIDENCED_GOAL_INVALIDATION"
        )

    # Exact hierarchy order is mandatory.
    wrong_order = deepcopy(base)
    chain = wrong_order[
        "goal_architecture_input"
    ]["chain"]
    chain[1], chain[2] = chain[2], chain[1]

    try:
        core.activate(wrong_order)
    except ValueError as exc:
        assert str(exc).startswith(
            "DNA-38_LEVEL_ORDER_MISMATCH:"
        )
    else:
        raise AssertionError(
            "DNA-38_ACCEPTED_WRONG_HIERARCHY_ORDER"
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
        "core_id": "DNA-38",
        "canon_mapping": "PASS",
        "purpose_goal_subgoal_task_action": "PASS",
        "failure_action_plan_change": "PASS",
        "goal_review_when_wrong": "PASS",
        "goal_invalidation_evidence_gate": "PASS",
        "goal_changed_by_dna38": False,
        "action_executed": False,
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
            "DNA-39"
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
}


def main() -> int:
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON]:
        if not path.exists():
            print(
                "DNA-38_FAIL: REQUIRED_PATH_NOT_FOUND"
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
        print("DNA-38_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 38):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna38(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-38_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_38_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "PURPOSE_GOAL_SUBGOAL_TASK_ACTION:",
        report["purpose_goal_subgoal_task_action"],
    )
    print(
        "FAILURE_ACTION_PLAN_CHANGE:",
        report["failure_action_plan_change"],
    )
    print(
        "GOAL_REVIEW_WHEN_WRONG:",
        report["goal_review_when_wrong"],
    )
    print(
        "GOAL_INVALIDATION_EVIDENCE_GATE:",
        report["goal_invalidation_evidence_gate"],
    )
    print(
        "GOAL_CHANGED_BY_DNA38:",
        report["goal_changed_by_dna38"],
    )
    print(
        "ACTION_EXECUTED:",
        report["action_executed"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 38/54")
    print("NEXT_AUTHORIZED: DNA-39")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
