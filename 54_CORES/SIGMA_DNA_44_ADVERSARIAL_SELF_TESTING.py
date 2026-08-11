#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-44: ADVERSARIAL SELF-TESTING
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_44_ADVERSARIAL_SELF_TESTING.py
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

CANON_DNA44: Dict[str, str] = {
    "id": "DNA-44",
    "name": "Adversarial Self-Testing",
    "purpose": (
        "Sau khi hiểu, chủ động tìm counterexample, boundary case, "
        "distribution shift và cách làm hypothesis sụp đổ."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
ADVERSARIAL_SELF_TESTING_SCHEMA = "SIGMA_ADVERSARIAL_SELF_TESTING_V1"

CANON_TEST_TYPES = [
    "COUNTEREXAMPLE",
    "BOUNDARY_CASE",
    "DISTRIBUTION_SHIFT",
    "HYPOTHESIS_COLLAPSE",
]

ADVERSARIAL_SELF_TESTING_CONTRACT: Dict[str, Any] = {
    "schema": ADVERSARIAL_SELF_TESTING_SCHEMA,
    "understanding_required_before_adversarial_testing": True,
    "understanding_requires_evidence": True,
    "canonical_test_types": deepcopy(CANON_TEST_TYPES),
    "test_type_count": 4,
    "counterexample_required": True,
    "boundary_case_required": True,
    "distribution_shift_required": True,
    "hypothesis_collapse_path_required": True,
    "unexecuted_test_is_not_falsification": True,
    "hypothesis_rejected_by_dna44_without_result": False,
    "test_execution_started": False,
    "benchmark_execution_started": False,
    "model_calls_started": False,
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
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA44:
        raise RuntimeError(
            "DNA-44_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA44, "actual": actual},
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
            "DNA-44_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    return state


def _install_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("adversarial_self_testing")
    expected = {
        "contract": deepcopy(
            ADVERSARIAL_SELF_TESTING_CONTRACT
        ),
        "assessments": [],
    }

    if existing is None:
        state["adversarial_self_testing"] = expected
        return state["adversarial_self_testing"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['adversarial_self_testing'] must be a dict"
        )

    if existing.get("contract") != ADVERSARIAL_SELF_TESTING_CONTRACT:
        raise ValueError(
            "DNA-44_ADVERSARIAL_SELF_TESTING_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("assessments"), list):
        raise TypeError(
            "adversarial_self_testing['assessments'] must be a list"
        )

    return existing


def _normalize_understanding(supplied: Any) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "adversarial_assessment['understanding'] must be a dict"
        )

    understood = supplied.get("understood")
    evidence = supplied.get("evidence")

    if not isinstance(understood, bool):
        raise TypeError(
            "understanding['understood'] must be a bool"
        )

    if not understood:
        raise ValueError(
            "DNA-44_ADVERSARIAL_TESTING_REQUIRES_UNDERSTANDING"
        )

    if not isinstance(evidence, list):
        raise TypeError(
            "understanding['evidence'] must be a list"
        )

    if not evidence:
        raise ValueError(
            "DNA-44_UNDERSTANDING_REQUIRES_EVIDENCE"
        )

    return {
        "understood": True,
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(evidence),
    }


def _normalize_test(
    supplied: Any,
    *,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"adversarial_tests[{index}] must be a dict"
        )

    test_id = supplied.get("test_id")
    test_type = supplied.get("type")
    target = supplied.get("target")
    falsification_condition = supplied.get(
        "falsification_condition"
    )

    if not isinstance(test_id, str) or not test_id.strip():
        raise ValueError(
            "DNA-44_TEST_ID_REQUIRED"
        )

    if not isinstance(test_type, str):
        raise TypeError(
            "adversarial test type must be a string"
        )

    test_type = test_type.strip().upper()

    if test_type not in CANON_TEST_TYPES:
        raise ValueError(
            f"DNA-44_UNKNOWN_TEST_TYPE:{test_type}"
        )

    if target is None:
        raise ValueError(
            f"DNA-44_TEST_TARGET_REQUIRED:{test_id}"
        )

    if (
        not isinstance(falsification_condition, str)
        or not falsification_condition.strip()
    ):
        raise ValueError(
            f"DNA-44_FALSIFICATION_CONDITION_REQUIRED:{test_id}"
        )

    rationale = supplied.get("rationale", [])
    if not isinstance(rationale, list):
        raise TypeError(
            "adversarial test rationale must be a list"
        )

    return {
        "input_index": index,
        "test_id": test_id,
        "type": test_type,
        "target": deepcopy(target),
        "target_sha256": _sha256_json(target),
        "falsification_condition": falsification_condition,
        "falsification_condition_sha256": _sha256_json(
            falsification_condition
        ),
        "rationale": deepcopy(rationale),
        "rationale_sha256": _sha256_json(rationale),
        "executed_by_dna44": False,
        "result": None,
        "hypothesis_falsified": False,
    }


def _evaluate(
    supplied: Any,
    adversarial_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['adversarial_assessment'] must be a dict"
        )

    assessment_id = supplied.get("assessment_id")
    hypothesis = supplied.get("hypothesis")
    understanding = supplied.get("understanding")
    tests = supplied.get("adversarial_tests")

    if not isinstance(
        assessment_id,
        str,
    ) or not assessment_id.strip():
        raise ValueError(
            "DNA-44_ASSESSMENT_ID_REQUIRED"
        )

    if hypothesis is None:
        raise ValueError(
            "DNA-44_HYPOTHESIS_REQUIRED"
        )

    normalized_understanding = _normalize_understanding(
        understanding
    )

    if not isinstance(tests, list):
        raise TypeError(
            "adversarial_assessment['adversarial_tests'] must be a list"
        )

    normalized_tests = [
        _normalize_test(
            item,
            index=index,
        )
        for index, item in enumerate(
            tests,
            start=1,
        )
    ]

    ids = [
        item["test_id"]
        for item in normalized_tests
    ]
    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-44_DUPLICATE_TEST_ID"
        )

    present_types = {
        item["type"]
        for item in normalized_tests
    }

    missing_types = [
        test_type
        for test_type in CANON_TEST_TYPES
        if test_type not in present_types
    ]

    complete = not missing_types

    sequence = len(
        adversarial_state["assessments"]
    ) + 1

    record = {
        "sequence": sequence,
        "record_id": (
            f"DNA-44-ADVERSARIAL-{sequence:04d}"
        ),
        "assessment_id": assessment_id,
        "hypothesis": deepcopy(hypothesis),
        "hypothesis_sha256": _sha256_json(hypothesis),
        "understanding": deepcopy(
            normalized_understanding
        ),
        "adversarial_tests": deepcopy(
            normalized_tests
        ),
        "test_count": len(normalized_tests),
        "test_types_present": sorted(
            present_types
        ),
        "missing_test_types": missing_types,
        "complete_adversarial_coverage": complete,
        "counterexample_present": (
            "COUNTEREXAMPLE" in present_types
        ),
        "boundary_case_present": (
            "BOUNDARY_CASE" in present_types
        ),
        "distribution_shift_present": (
            "DISTRIBUTION_SHIFT" in present_types
        ),
        "hypothesis_collapse_path_present": (
            "HYPOTHESIS_COLLAPSE" in present_types
        ),
        "test_execution_started": False,
        "hypothesis_rejected": False,
        "external_action_executed": False,
        "status": (
            "ADVERSARIAL_TEST_PLAN_COMPLETE"
            if complete
            else "ADVERSARIAL_TEST_PLAN_INCOMPLETE"
        ),
    }

    adversarial_state["assessments"].append(
        deepcopy(record)
    )
    return record


def dna44_adversarial_self_testing(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    After understanding is evidenced, structure adversarial attacks against
    a hypothesis across counterexample, boundary case, distribution shift,
    and an explicit hypothesis-collapse path.

    DNA-44 does not execute the tests or claim falsification without
    observed results. It starts no higher runtime, model, benchmark,
    external action, or Canon write.
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
    trace.append("DNA-44")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    adversarial_state = _install_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(
        actual_canon
    )

    record = _evaluate(
        context.get("adversarial_assessment"),
        adversarial_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-44",
            "operation": (
                "ADVERSARIAL_SELF_TESTING_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "record_id": record["record_id"],
            "complete_adversarial_coverage": (
                record["complete_adversarial_coverage"]
            ),
            "test_execution_started": False,
            "hypothesis_rejected": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-44"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "adversarial_self_testing_contract": deepcopy(
            ADVERSARIAL_SELF_TESTING_CONTRACT
        ),
        "adversarial_tests": deepcopy(
            record["adversarial_tests"]
        ),
        "record": deepcopy(record),
        "counterexample": (
            record["counterexample_present"]
        ),
        "boundary_case": (
            record["boundary_case_present"]
        ),
        "distribution_shift": (
            record["distribution_shift_present"]
        ),
        "hypothesis_collapse": (
            record["hypothesis_collapse_path_present"]
        ),
        "complete_adversarial_coverage": (
            record["complete_adversarial_coverage"]
        ),
        "test_execution_started": False,
        "benchmark_execution_started": False,
        "hypothesis_rejected": False,
        "learning_runtime_started": False,
        "world_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna44(core54: Core54Like) -> None:
    core = core54.get("DNA-44")
    assert_exact_canon(core)
    core54.bind(
        "DNA-44",
        dna44_adversarial_self_testing,
    )


def _valid_assessment() -> Dict[str, Any]:
    return {
        "assessment_id": "DNA44-SELF-CHECK",
        "hypothesis": {
            "hypothesis_id": "H-1",
            "claim": "RULE_R_GENERALIZES",
        },
        "understanding": {
            "understood": True,
            "evidence": [
                {
                    "type": "EXPLANATION",
                    "result": (
                        "MECHANISM_AND_SCOPE_IDENTIFIED"
                    ),
                }
            ],
        },
        "adversarial_tests": [
            {
                "test_id": "T-COUNTEREXAMPLE",
                "type": "COUNTEREXAMPLE",
                "target": {
                    "search": (
                        "CASE_CONTRADICTING_RULE_R"
                    ),
                },
                "falsification_condition": (
                    "A valid case satisfies premises "
                    "but violates predicted conclusion."
                ),
                "rationale": [
                    "DIRECT_COUNTEREXAMPLE_ATTACK"
                ],
            },
            {
                "test_id": "T-BOUNDARY",
                "type": "BOUNDARY_CASE",
                "target": {
                    "search": (
                        "EDGE_OF_DECLARED_DOMAIN"
                    ),
                },
                "falsification_condition": (
                    "Rule R fails at a legitimate "
                    "boundary within its claimed scope."
                ),
                "rationale": [
                    "BOUNDARY_STRESS_TEST"
                ],
            },
            {
                "test_id": "T-SHIFT",
                "type": "DISTRIBUTION_SHIFT",
                "target": {
                    "search": (
                        "SHIFTED_INPUT_DISTRIBUTION"
                    ),
                },
                "falsification_condition": (
                    "Claimed generalization fails under "
                    "a relevant distribution shift."
                ),
                "rationale": [
                    "OUT_OF_DISTRIBUTION_STRESS_TEST"
                ],
            },
            {
                "test_id": "T-COLLAPSE",
                "type": "HYPOTHESIS_COLLAPSE",
                "target": {
                    "search": (
                        "DECISIVE_FALSIFICATION_CONDITION"
                    ),
                },
                "falsification_condition": (
                    "Observed result is incompatible "
                    "with hypothesis H-1."
                ),
                "rationale": [
                    "EXPLICIT_HYPOTHESIS_KILL_CRITERION"
                ],
            },
        ],
    }


def self_check_dna44(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 44):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-44")
    assert_exact_canon(core)
    bind_dna44(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 44)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": (
                UNIFIED_STATE_SCHEMA
            ),
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "adversarial_assessment": (
            _valid_assessment()
        ),
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-44"]

    assert output["canonical_gene"] == CANON_DNA44
    assert output["counterexample"] is True
    assert output["boundary_case"] is True
    assert output["distribution_shift"] is True
    assert output["hypothesis_collapse"] is True
    assert output[
        "complete_adversarial_coverage"
    ] is True
    assert output["test_execution_started"] is False
    assert output["hypothesis_rejected"] is False
    assert output["higher_runtime_started"] is False

    # Testing before understanding is forbidden.
    no_understanding = deepcopy(probe)
    no_understanding[
        "adversarial_assessment"
    ]["understanding"]["understood"] = False

    try:
        core.activate(no_understanding)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-44_ADVERSARIAL_TESTING_REQUIRES_UNDERSTANDING"
        )
    else:
        raise AssertionError(
            "DNA-44_ACCEPTED_TESTING_BEFORE_UNDERSTANDING"
        )

    # Understanding cannot be self-declared without evidence.
    no_understanding_evidence = deepcopy(probe)
    no_understanding_evidence[
        "adversarial_assessment"
    ]["understanding"]["evidence"] = []

    try:
        core.activate(no_understanding_evidence)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-44_UNDERSTANDING_REQUIRES_EVIDENCE"
        )
    else:
        raise AssertionError(
            "DNA-44_ACCEPTED_UNEVIDENCED_UNDERSTANDING"
        )

    # Missing one Canon attack dimension stays incomplete.
    incomplete = deepcopy(probe)
    incomplete[
        "adversarial_assessment"
    ]["adversarial_tests"] = (
        incomplete[
            "adversarial_assessment"
        ]["adversarial_tests"][:-1]
    )

    incomplete_result = core.activate(
        incomplete
    )
    incomplete_record = incomplete_result[
        "core54_outputs"
    ]["DNA-44"]["record"]

    assert (
        incomplete_record[
            "complete_adversarial_coverage"
        ]
        is False
    )
    assert (
        incomplete_record[
            "missing_test_types"
        ]
        == ["HYPOTHESIS_COLLAPSE"]
    )

    # Planning a falsification test is not equivalent to falsifying.
    assert all(
        test["result"] is None
        and test["hypothesis_falsified"] is False
        for test in output["adversarial_tests"]
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
        "core_id": "DNA-44",
        "canon_mapping": "PASS",
        "understanding_evidence_gate": "PASS",
        "counterexample": "PASS",
        "boundary_case": "PASS",
        "distribution_shift": "PASS",
        "hypothesis_collapse": "PASS",
        "four_adversarial_dimensions_gate": "PASS",
        "test_execution_started": False,
        "hypothesis_rejected_without_result": False,
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
            "DNA-45"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


PRIOR = {
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
    31: "SIGMA_DNA_31_INTELLIGENCE_TEST",
    32: "SIGMA_DNA_32_ACCEPTANCE_CRITERIA",
    33: "SIGMA_DNA_33_PHYSICAL_IMPLEMENTATION_INDEPENDENCE",
    34: "SIGMA_DNA_34_SIGMA_IDENTITY",
    35: "SIGMA_DNA_35_CORE_COVENANT",
    36: "SIGMA_DNA_36_CAUSAL_WORLD_MODEL",
    37: "SIGMA_DNA_37_INTERNAL_SIMULATION",
    38: "SIGMA_DNA_38_GOAL_ARCHITECTURE",
    39: "SIGMA_DNA_39_CURIOSITY_ENGINE",
    40: "SIGMA_DNA_40_CONCEPT_FORMATION",
    41: "SIGMA_DNA_41_REPRESENTATION_INVENTION",
    42: "SIGMA_DNA_42_METACOGNITIVE_SCHEDULER",
    43: "SIGMA_DNA_43_ANTI_SELF_DECEPTION",
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-44_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(
        0,
        str(CORE54_ROOT),
    )
    sys.path.insert(
        0,
        str(GENES_ROOT),
    )

    try:
        from sigma_core54_foundation_v0_3 import (
            SigmaCore54,
        )

        modules = {
            index: importlib.import_module(
                name
            )
            for index, name in PRIOR.items()
        }

    except Exception as exc:
        print(
            "DNA-44_FAIL: IMPORT_ERROR"
        )
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 44):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna44(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-44_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_44_PASS")
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "UNDERSTANDING_EVIDENCE_GATE:",
        report["understanding_evidence_gate"],
    )
    print(
        "COUNTEREXAMPLE:",
        report["counterexample"],
    )
    print(
        "BOUNDARY_CASE:",
        report["boundary_case"],
    )
    print(
        "DISTRIBUTION_SHIFT:",
        report["distribution_shift"],
    )
    print(
        "HYPOTHESIS_COLLAPSE:",
        report["hypothesis_collapse"],
    )
    print(
        "FOUR_ADVERSARIAL_DIMENSIONS_GATE:",
        report["four_adversarial_dimensions_gate"],
    )
    print(
        "TEST_EXECUTION_STARTED:",
        report["test_execution_started"],
    )
    print(
        "HYPOTHESIS_REJECTED_WITHOUT_RESULT:",
        report["hypothesis_rejected_without_result"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
    )
    print(
        "EXECUTABLE:",
        report["executable"],
    )
    print(
        "SELF_CHECK:",
        report["self_check"],
    )
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print(
        "PHASE_LOCKS:",
        report["phase_locks"],
    )
    print(
        "OFFICIAL_BOUND_CORES: 44/54"
    )
    print(
        "NEXT_AUTHORIZED: DNA-45"
    )
    print(
        "NEXT_PHASE: FORBIDDEN"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
