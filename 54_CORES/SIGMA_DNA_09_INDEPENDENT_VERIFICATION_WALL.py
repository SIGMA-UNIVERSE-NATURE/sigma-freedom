#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-09: INDEPENDENT VERIFICATION WALL
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL.py
"""

from __future__ import annotations

import hashlib
import json
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

CANON_DNA09: Dict[str, str] = {
    "id": "DNA-09",
    "name": "Independent Verification Wall",
    "purpose": (
        "Tách learner khỏi verifier; knowledge chỉ được nâng khi có "
        "kiểm chứng độc lập thích hợp."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
LEARNING_WORLD_SCHEMA = "SIGMA_LEARNING_WORLD_V1"
VERIFICATION_WALL_SCHEMA = (
    "SIGMA_INDEPENDENT_VERIFICATION_WALL_V1"
)

REQUIRED_VERIFICATION_FIELDS = [
    "learner_id",
    "verifier_id",
    "verifier_independent",
    "independence_basis",
    "candidate_sha256",
    "method",
    "scope",
    "evidence",
    "passed",
]

INDEPENDENT_VERIFICATION_CONTRACT: Dict[str, Any] = {
    "schema": VERIFICATION_WALL_SCHEMA,
    "learner_verifier_separation_required": True,
    "independent_verification_required": True,
    "appropriate_verification_requires": [
        "DISTINCT_LEARNER_AND_VERIFIER",
        "EXPLICIT_INDEPENDENCE",
        "INDEPENDENCE_BASIS",
        "CANDIDATE_BINDING",
        "NON_EMPTY_METHOD",
        "NON_EMPTY_SCOPE",
        "NON_EMPTY_EVIDENCE",
        "VERIFIER_PASS",
    ],
    "promotion_without_verification": False,
    "promotion_is_eligibility_only": True,
    "knowledge_promotion_executed": False,
    "learning_runtime_started": False,
    "external_verifier_invoked": False,
    "execution_authority": False,
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
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA09:
        raise RuntimeError(
            "DNA-09_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA09, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_state(
    context: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-09_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    learning_world = state.get("learning_world")
    if not isinstance(learning_world, dict):
        raise RuntimeError(
            "DNA-08_LEARNING_WORLD_REQUIRED"
        )

    contract = learning_world.get("contract")
    if not isinstance(contract, dict):
        raise RuntimeError(
            "DNA-08_LEARNING_WORLD_CONTRACT_REQUIRED"
        )

    if contract.get("schema") != LEARNING_WORLD_SCHEMA:
        raise ValueError(
            "DNA-09_LEARNING_WORLD_SCHEMA_MISMATCH:"
            f"{contract.get('schema')!r}"
        )

    if not isinstance(learning_world.get("events"), list):
        raise TypeError(
            "learning_world['events'] must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-08_OUTPUT_REQUIRED")

    dna08_output = outputs.get("DNA-08")
    if not isinstance(dna08_output, dict):
        raise RuntimeError("DNA-08_OUTPUT_REQUIRED")

    return state, learning_world


def _install_verification_wall(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("independent_verification_wall")

    expected = {
        "contract": deepcopy(
            INDEPENDENT_VERIFICATION_CONTRACT
        ),
        "evaluations": [],
    }

    if existing is None:
        state["independent_verification_wall"] = expected
        return state["independent_verification_wall"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['independent_verification_wall'] "
            "must be a dict"
        )

    if existing.get("contract") != (
        INDEPENDENT_VERIFICATION_CONTRACT
    ):
        raise ValueError(
            "DNA-09_VERIFICATION_WALL_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("evaluations"), list):
        raise TypeError(
            "independent_verification_wall['evaluations'] "
            "must be a list"
        )

    return existing


def _latest_candidate(
    learning_world: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    events = learning_world["events"]
    if not events:
        return None

    event = events[-1]
    if not isinstance(event, dict):
        raise TypeError(
            "DNA-08 learning-world event must be a dict"
        )

    if event.get("complete") is not True:
        return None

    if event.get("status") != (
        "EXPERIENTIAL_EVENT_QUALIFIED"
    ):
        return None

    candidate_content = {
        "source_core_id": "DNA-08",
        "source_event_id": event.get("event_id"),
        "interaction_sha256": event.get(
            "interaction_sha256"
        ),
        "experience": deepcopy(event.get("experience")),
    }

    return {
        **candidate_content,
        "candidate_sha256": _sha256_json(
            candidate_content
        ),
        "knowledge_status": "CANDIDATE_UNVERIFIED",
    }


def _non_empty_text(
    value: Any,
) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _non_empty_list(
    value: Any,
) -> bool:
    return isinstance(value, list) and len(value) > 0


def _validate_verification_types(
    verification: Dict[str, Any],
) -> None:
    for key in (
        "verifier_independent",
        "passed",
    ):
        if key in verification and not isinstance(
            verification[key],
            bool,
        ):
            raise TypeError(
                f"verification['{key}'] must be a bool"
            )

    for key in (
        "learner_id",
        "verifier_id",
        "candidate_sha256",
        "method",
        "scope",
    ):
        if key in verification and not isinstance(
            verification[key],
            str,
        ):
            raise TypeError(
                f"verification['{key}'] must be a string"
            )

    for key in (
        "independence_basis",
        "evidence",
    ):
        if key in verification and not isinstance(
            verification[key],
            list,
        ):
            raise TypeError(
                f"verification['{key}'] must be a list"
            )


def _evaluate_verification(
    candidate: Optional[Dict[str, Any]],
    verification: Any,
    wall: Dict[str, Any],
) -> Dict[str, Any]:
    reasons: List[str] = []

    if candidate is None:
        reasons.append("NO_KNOWLEDGE_CANDIDATE")

    if not isinstance(verification, dict):
        verification_record: Dict[str, Any] = {}
        reasons.append("VERIFICATION_RECORD_REQUIRED")
    else:
        verification_record = deepcopy(verification)
        _validate_verification_types(
            verification_record
        )

    missing_fields = [
        key
        for key in REQUIRED_VERIFICATION_FIELDS
        if key not in verification_record
    ]
    if missing_fields:
        reasons.append("VERIFICATION_FIELDS_MISSING")

    learner_id = verification_record.get("learner_id")
    verifier_id = verification_record.get("verifier_id")

    identities_present = (
        _non_empty_text(learner_id)
        and _non_empty_text(verifier_id)
    )
    separated = bool(
        identities_present
        and learner_id != verifier_id
    )
    if not separated:
        reasons.append(
            "LEARNER_VERIFIER_NOT_SEPARATED"
        )

    independent = (
        verification_record.get(
            "verifier_independent"
        )
        is True
    )
    if not independent:
        reasons.append(
            "INDEPENDENT_VERIFIER_REQUIRED"
        )

    independence_basis = verification_record.get(
        "independence_basis"
    )
    if not _non_empty_list(independence_basis):
        reasons.append(
            "INDEPENDENCE_BASIS_REQUIRED"
        )

    method = verification_record.get("method")
    if not _non_empty_text(method):
        reasons.append(
            "VERIFICATION_METHOD_REQUIRED"
        )

    scope = verification_record.get("scope")
    if not _non_empty_text(scope):
        reasons.append(
            "VERIFICATION_SCOPE_REQUIRED"
        )

    evidence = verification_record.get("evidence")
    if not _non_empty_list(evidence):
        reasons.append(
            "VERIFICATION_EVIDENCE_REQUIRED"
        )

    passed = verification_record.get("passed") is True
    if not passed:
        reasons.append("VERIFIER_PASS_REQUIRED")

    expected_candidate_sha256 = (
        candidate.get("candidate_sha256")
        if candidate is not None
        else None
    )
    candidate_bound = bool(
        expected_candidate_sha256 is not None
        and verification_record.get(
            "candidate_sha256"
        )
        == expected_candidate_sha256
    )
    if not candidate_bound:
        reasons.append(
            "VERIFICATION_NOT_BOUND_TO_CANDIDATE"
        )

    unique_reasons = list(dict.fromkeys(reasons))
    promotion_allowed = len(unique_reasons) == 0

    sequence = len(wall["evaluations"]) + 1
    evaluation = {
        "sequence": sequence,
        "evaluation_id": (
            f"DNA-09-VERIFY-{sequence:04d}"
        ),
        "candidate": deepcopy(candidate),
        "verification_record": verification_record,
        "learner_verifier_separated": separated,
        "independent_verifier": independent,
        "candidate_bound": candidate_bound,
        "verification_passed": passed,
        "appropriate_verification": (
            promotion_allowed
        ),
        "promotion_allowed": promotion_allowed,
        "promotion_executed": False,
        "rejection_reasons": unique_reasons,
        "status": (
            "ELIGIBLE_FOR_KNOWLEDGE_PROMOTION"
            if promotion_allowed
            else "KNOWLEDGE_PROMOTION_BLOCKED"
        ),
    }
    wall["evaluations"].append(evaluation)
    return evaluation


def dna09_independent_verification_wall(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Separate learner output from independent verification and determine
    knowledge-promotion eligibility.

    DNA-09 evaluates supplied verification evidence only. It does not invoke
    a verifier, promote knowledge, start Learning Runtime, write Memory
    Runtime, call a model, execute F174, act externally, or modify Canon.
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
    trace.append("DNA-09")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, learning_world = _validate_state(context)
    wall = _install_verification_wall(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-09",
            "operation": (
                "INDEPENDENT_VERIFICATION_WALL_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "verification_wall_schema": (
                VERIFICATION_WALL_SCHEMA
            ),
            "promotion_without_verification": False,
        }
    )

    candidate = _latest_candidate(learning_world)
    evaluation = _evaluate_verification(
        candidate,
        context.get("verification"),
        wall,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-09",
            "operation": (
                "KNOWLEDGE_PROMOTION_ELIGIBILITY_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "evaluation_id": evaluation["evaluation_id"],
            "learner_verifier_separated": (
                evaluation[
                    "learner_verifier_separated"
                ]
            ),
            "independent_verifier": (
                evaluation["independent_verifier"]
            ),
            "promotion_allowed": (
                evaluation["promotion_allowed"]
            ),
            "promotion_executed": False,
        }
    )

    outputs["DNA-09"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "verification_wall_contract": deepcopy(
            INDEPENDENT_VERIFICATION_CONTRACT
        ),
        "candidate": deepcopy(candidate),
        "evaluation": deepcopy(evaluation),
        "promotion_allowed": (
            evaluation["promotion_allowed"]
        ),
        "promotion_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna09(core54: Core54Like) -> None:
    core = core54.get("DNA-09")
    assert_exact_canon(core)
    core54.bind(
        "DNA-09",
        dna09_independent_verification_wall,
    )


def self_check_dna09(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for required_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna09_core = core54.get("DNA-09")
    assert_exact_canon(dna09_core)
    bind_dna09(core54)

    base_probe = {
        "trace": [],
        "caller_data": {"preserve": True},
        "environment": {
            "id": "WORLD-DNA09-SELF-CHECK",
            "state": "INITIAL",
        },
        "action": {
            "id": "LEARNER-ACTION-01",
            "description": "APPLY_TEST_INTERVENTION",
        },
        "consequence": {
            "observed_change": "STATE_UPDATED",
        },
        "experience": {
            "candidate_learning": (
                "ACTION_CHANGED_ENVIRONMENT_STATE"
            ),
        },
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {
                "subject": "DNA-09_SELF_CHECK",
            },
            "provenance": [
                {
                    "sequence": 1,
                    "core_id": "CALLER",
                    "operation": "INPUT_CREATED",
                }
            ],
            "uncertainty": {
                "open_items": [
                    "KNOWLEDGE_NOT_YET_PROMOTED"
                ],
            },
        },
    }

    # First derive the exact DNA-08 candidate binding without invoking DNA-09.
    candidate_context = deepcopy(base_probe)
    for core_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
    ):
        candidate_context = core54.get(
            core_id
        ).activate(candidate_context)

    candidate = _latest_candidate(
        candidate_context["cognitive_state"][
            "learning_world"
        ]
    )
    assert candidate is not None

    probe = deepcopy(base_probe)
    probe["verification"] = {
        "learner_id": "LEARNER-A",
        "verifier_id": "VERIFIER-B",
        "verifier_independent": True,
        "independence_basis": [
            "SEPARATE_ROLE",
            "NO_SHARED_DECISION_AUTHORITY",
        ],
        "candidate_sha256": (
            candidate["candidate_sha256"]
        ),
        "method": "INDEPENDENT_REPLAY_AND_COMPARISON",
        "scope": "DNA-08_EXPERIENTIAL_EVENT",
        "evidence": [
            {
                "type": "REPLAY_RESULT",
                "result": "CONSISTENT",
            },
            {
                "type": "COMPARISON_RESULT",
                "result": "SUPPORTED",
            },
        ],
        "passed": True,
    }
    snapshot = deepcopy(probe)

    result = probe
    pre_dna09: Optional[Dict[str, Any]] = None
    for core_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
        "DNA-09",
    ):
        if core_id == "DNA-09":
            pre_dna09 = deepcopy(result)
        result = core54.get(core_id).activate(result)

    assert pre_dna09 is not None
    assert probe == snapshot
    assert result["trace"] == [
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
        "DNA-09",
    ]

    dna09 = result["core54_outputs"]["DNA-09"]
    assert dna09["canonical_gene"] == CANON_DNA09
    assert dna09["verification_wall_contract"] == (
        INDEPENDENT_VERIFICATION_CONTRACT
    )
    assert dna09["candidate"] == candidate
    assert dna09["promotion_allowed"] is True
    assert dna09["promotion_executed"] is False
    assert dna09["status"] == "CANON_ALIGNED"

    evaluation = dna09["evaluation"]
    assert evaluation["sequence"] == 1
    assert evaluation["evaluation_id"] == (
        "DNA-09-VERIFY-0001"
    )
    assert evaluation["candidate"] == candidate
    assert (
        evaluation["verification_record"]
        == probe["verification"]
    )
    assert (
        evaluation["learner_verifier_separated"]
        is True
    )
    assert evaluation["independent_verifier"] is True
    assert evaluation["candidate_bound"] is True
    assert evaluation["verification_passed"] is True
    assert evaluation["appropriate_verification"] is True
    assert evaluation["promotion_allowed"] is True
    assert evaluation["promotion_executed"] is False
    assert evaluation["rejection_reasons"] == []
    assert evaluation["status"] == (
        "ELIGIBLE_FOR_KNOWLEDGE_PROMOTION"
    )

    state = result["cognitive_state"]
    wall = state["independent_verification_wall"]
    assert wall["contract"] == (
        INDEPENDENT_VERIFICATION_CONTRACT
    )
    assert wall["evaluations"] == [evaluation]
    assert len(state["provenance"]) == 10

    wall_event = state["provenance"][-2]
    assert wall_event["sequence"] == 9
    assert wall_event["core_id"] == "DNA-09"
    assert wall_event["operation"] == (
        "INDEPENDENT_VERIFICATION_WALL_ESTABLISHED"
    )
    assert (
        wall_event["promotion_without_verification"]
        is False
    )

    evaluation_event = state["provenance"][-1]
    assert evaluation_event["sequence"] == 10
    assert evaluation_event["core_id"] == "DNA-09"
    assert evaluation_event["operation"] == (
        "KNOWLEDGE_PROMOTION_ELIGIBILITY_EVALUATED"
    )
    assert (
        evaluation_event["learner_verifier_separated"]
        is True
    )
    assert evaluation_event["independent_verifier"] is True
    assert evaluation_event["promotion_allowed"] is True
    assert evaluation_event["promotion_executed"] is False

    # Learner cannot verify its own candidate.
    same_actor_input = deepcopy(pre_dna09)
    same_actor_input["verification"] = deepcopy(
        probe["verification"]
    )
    same_actor_input["verification"]["verifier_id"] = (
        "LEARNER-A"
    )
    same_actor = dna09_core.activate(same_actor_input)
    same_actor_eval = same_actor[
        "core54_outputs"
    ]["DNA-09"]["evaluation"]
    assert same_actor_eval["promotion_allowed"] is False
    assert (
        "LEARNER_VERIFIER_NOT_SEPARATED"
        in same_actor_eval["rejection_reasons"]
    )

    # A non-independent verifier cannot authorize promotion.
    dependent_input = deepcopy(pre_dna09)
    dependent_input["verification"] = deepcopy(
        probe["verification"]
    )
    dependent_input["verification"][
        "verifier_independent"
    ] = False
    dependent = dna09_core.activate(dependent_input)
    dependent_eval = dependent[
        "core54_outputs"
    ]["DNA-09"]["evaluation"]
    assert dependent_eval["promotion_allowed"] is False
    assert (
        "INDEPENDENT_VERIFIER_REQUIRED"
        in dependent_eval["rejection_reasons"]
    )

    # Verification must be bound to the exact candidate.
    wrong_candidate_input = deepcopy(pre_dna09)
    wrong_candidate_input["verification"] = deepcopy(
        probe["verification"]
    )
    wrong_candidate_input["verification"][
        "candidate_sha256"
    ] = "WRONG-CANDIDATE-HASH"
    wrong_candidate = dna09_core.activate(
        wrong_candidate_input
    )
    wrong_candidate_eval = wrong_candidate[
        "core54_outputs"
    ]["DNA-09"]["evaluation"]
    assert (
        wrong_candidate_eval["promotion_allowed"]
        is False
    )
    assert (
        "VERIFICATION_NOT_BOUND_TO_CANDIDATE"
        in wrong_candidate_eval["rejection_reasons"]
    )

    # A failed verification must block promotion.
    verifier_fail_input = deepcopy(pre_dna09)
    verifier_fail_input["verification"] = deepcopy(
        probe["verification"]
    )
    verifier_fail_input["verification"]["passed"] = False
    verifier_fail = dna09_core.activate(
        verifier_fail_input
    )
    verifier_fail_eval = verifier_fail[
        "core54_outputs"
    ]["DNA-09"]["evaluation"]
    assert verifier_fail_eval["promotion_allowed"] is False
    assert (
        "VERIFIER_PASS_REQUIRED"
        in verifier_fail_eval["rejection_reasons"]
    )

    # Missing appropriate method/evidence must block promotion.
    insufficient_input = deepcopy(pre_dna09)
    insufficient_input["verification"] = deepcopy(
        probe["verification"]
    )
    insufficient_input["verification"]["method"] = ""
    insufficient_input["verification"]["evidence"] = []
    insufficient = dna09_core.activate(
        insufficient_input
    )
    insufficient_eval = insufficient[
        "core54_outputs"
    ]["DNA-09"]["evaluation"]
    assert insufficient_eval["promotion_allowed"] is False
    assert (
        "VERIFICATION_METHOD_REQUIRED"
        in insufficient_eval["rejection_reasons"]
    )
    assert (
        "VERIFICATION_EVIDENCE_REQUIRED"
        in insufficient_eval["rejection_reasons"]
    )

    # No verifier record means no promotion.
    no_verification_input = deepcopy(pre_dna09)
    no_verification_input.pop("verification", None)
    no_verification = dna09_core.activate(
        no_verification_input
    )
    no_verification_eval = no_verification[
        "core54_outputs"
    ]["DNA-09"]["evaluation"]
    assert (
        no_verification_eval["promotion_allowed"]
        is False
    )
    assert (
        "VERIFICATION_RECORD_REQUIRED"
        in no_verification_eval["rejection_reasons"]
    )

    # A ready-made answer with no experiential candidate cannot be promoted.
    answer_only = deepcopy(base_probe)
    for key in (
        "environment",
        "action",
        "consequence",
        "experience",
    ):
        answer_only.pop(key, None)
    answer_only["answer"] = "READY_MADE_ANSWER"
    for core_id in (
        "DNA-01",
        "DNA-02",
        "DNA-03",
        "DNA-04",
        "DNA-05",
        "DNA-06",
        "DNA-07",
        "DNA-08",
    ):
        answer_only = core54.get(
            core_id
        ).activate(answer_only)
    answer_only["verification"] = deepcopy(
        probe["verification"]
    )
    answer_only_result = dna09_core.activate(
        answer_only
    )
    answer_only_eval = answer_only_result[
        "core54_outputs"
    ]["DNA-09"]["evaluation"]
    assert answer_only_eval["candidate"] is None
    assert answer_only_eval["promotion_allowed"] is False
    assert (
        "NO_KNOWLEDGE_CANDIDATE"
        in answer_only_eval["rejection_reasons"]
    )

    # Reject provisional root-marker behavior as the Canon contract.
    assert "promotion_allowed" not in result
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
        "core_id": "DNA-09",
        "canon_mapping": "PASS",
        "learner_verifier_separation": "PASS",
        "independent_verification": "PASS",
        "candidate_binding": "PASS",
        "promotion_wall": "PASS",
        "promotion_executed": False,
        "learning_runtime_used": False,
        "external_verifier_invoked": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-10"
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
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-09_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
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
    except Exception as exc:
        print("DNA-09_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(
            core.state.behavior_bound
            for core in core54.cores
        ):
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
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna09(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != [
            "DNA-01",
            "DNA-02",
            "DNA-03",
            "DNA-04",
            "DNA-05",
            "DNA-06",
            "DNA-07",
            "DNA-08",
            "DNA-09",
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-09_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-09_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_09_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "LEARNER_VERIFIER_SEPARATION:",
        report["learner_verifier_separation"],
    )
    print(
        "INDEPENDENT_VERIFICATION:",
        report["independent_verification"],
    )
    print(
        "CANDIDATE_BINDING:",
        report["candidate_binding"],
    )
    print("PROMOTION_WALL:", report["promotion_wall"])
    print(
        "PROMOTION_EXECUTED:",
        report["promotion_executed"],
    )
    print(
        "LEARNING_RUNTIME_USED:",
        report["learning_runtime_used"],
    )
    print(
        "EXTERNAL_VERIFIER_INVOKED:",
        report["external_verifier_invoked"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 9/54")
    print("NEXT_AUTHORIZED: DNA-10")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
