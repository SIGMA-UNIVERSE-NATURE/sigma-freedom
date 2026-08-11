#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-32: ACCEPTANCE CRITERIA
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_32_ACCEPTANCE_CRITERIA.py
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

CANON_DNA32: Dict[str, str] = {
    "id": "DNA-32",
    "name": "Acceptance Criteria",
    "purpose": (
        "Không gọi SIGMA hoàn chỉnh nếu chỉ là prompt/LLM wrapper; "
        "phải chứng minh học, kiểm chứng, transfer và feedback thật."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
ACCEPTANCE_CRITERIA_SCHEMA = "SIGMA_ACCEPTANCE_CRITERIA_V1"

REQUIRED_CAPABILITIES = [
    "LEARNING",
    "VERIFICATION",
    "TRANSFER",
    "FEEDBACK",
]

ALLOWED_SOURCE_CORES = {
    "LEARNING": ["DNA-16", "DNA-17"],
    "VERIFICATION": ["DNA-09"],
    "TRANSFER": ["DNA-31"],
    "FEEDBACK": ["DNA-06"],
}

FORBIDDEN_ONLY_ARCHITECTURES = [
    "PROMPT_ONLY",
    "LLM_WRAPPER_ONLY",
    "PROMPT_LLM_WRAPPER_ONLY",
]

ACCEPTANCE_CRITERIA_CONTRACT: Dict[str, Any] = {
    "schema": ACCEPTANCE_CRITERIA_SCHEMA,
    "required_capabilities": deepcopy(REQUIRED_CAPABILITIES),
    "required_source_cores": deepcopy(ALLOWED_SOURCE_CORES),
    "prompt_only_is_complete_sigma": False,
    "llm_wrapper_only_is_complete_sigma": False,
    "all_required_capabilities_must_be_proven": True,
    "evidence_required": True,
    "pass_claim_must_be_explicit": True,
    "eligibility_is_not_completion_declaration": True,
    "completion_declared_by_dna32": False,
    "next_phase_opened_by_dna32": False,
    "learning_runtime_started": False,
    "benchmark_started": False,
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
    if actual != CANON_DNA32:
        raise RuntimeError(
            "DNA-32_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA32, "actual": actual},
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
            "DNA-32_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    provenance = state.get("provenance")
    if not isinstance(provenance, list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    return state


def _install_acceptance_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("acceptance_criteria")
    expected = {
        "contract": deepcopy(ACCEPTANCE_CRITERIA_CONTRACT),
        "assessments": [],
    }

    if existing is None:
        state["acceptance_criteria"] = expected
        return state["acceptance_criteria"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['acceptance_criteria'] must be a dict"
        )

    if existing.get("contract") != ACCEPTANCE_CRITERIA_CONTRACT:
        raise ValueError(
            "DNA-32_ACCEPTANCE_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("assessments"), list):
        raise TypeError(
            "acceptance_criteria['assessments'] must be a list"
        )

    return existing


def _normalize_architecture(
    supplied: Any,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['sigma_architecture'] must be a dict"
        )

    architecture_id = supplied.get("architecture_id")
    architecture_type = supplied.get("architecture_type")
    evidence = supplied.get("evidence")

    if not isinstance(architecture_id, str) or not architecture_id.strip():
        raise ValueError("DNA-32_ARCHITECTURE_ID_REQUIRED")

    if not isinstance(architecture_type, str):
        raise TypeError(
            "sigma_architecture['architecture_type'] must be a string"
        )

    architecture_type = architecture_type.strip().upper()

    if not isinstance(evidence, list):
        raise TypeError(
            "sigma_architecture['evidence'] must be a list"
        )
    if not evidence:
        raise ValueError(
            "DNA-32_ARCHITECTURE_EVIDENCE_REQUIRED"
        )

    prompt_only = supplied.get(
        "prompt_only",
        architecture_type == "PROMPT_ONLY",
    )
    llm_wrapper_only = supplied.get(
        "llm_wrapper_only",
        architecture_type in {
            "LLM_WRAPPER_ONLY",
            "PROMPT_LLM_WRAPPER_ONLY",
        },
    )

    if not isinstance(prompt_only, bool):
        raise TypeError(
            "sigma_architecture['prompt_only'] must be a bool"
        )
    if not isinstance(llm_wrapper_only, bool):
        raise TypeError(
            "sigma_architecture['llm_wrapper_only'] must be a bool"
        )

    forbidden_only = bool(
        prompt_only
        or llm_wrapper_only
        or architecture_type in FORBIDDEN_ONLY_ARCHITECTURES
    )

    return {
        "architecture_id": architecture_id,
        "architecture_type": architecture_type,
        "prompt_only": prompt_only,
        "llm_wrapper_only": llm_wrapper_only,
        "forbidden_only_architecture": forbidden_only,
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(evidence),
    }


def _normalize_proof(
    supplied: Any,
    *,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"acceptance_proofs[{index}] must be a dict"
        )

    required = [
        "capability",
        "source_core_id",
        "evidence",
        "passed",
    ]
    missing = [
        field
        for field in required
        if field not in supplied
    ]
    if missing:
        raise ValueError(
            "DNA-32_PROOF_FIELDS_MISSING:"
            + ",".join(missing)
        )

    capability = supplied["capability"]
    source_core_id = supplied["source_core_id"]
    evidence = supplied["evidence"]
    passed = supplied["passed"]

    if not isinstance(capability, str):
        raise TypeError(
            "acceptance_proof['capability'] must be a string"
        )
    capability = capability.strip().upper()
    if capability not in REQUIRED_CAPABILITIES:
        raise ValueError(
            f"DNA-32_UNKNOWN_CAPABILITY:{capability}"
        )

    if not isinstance(source_core_id, str):
        raise TypeError(
            "acceptance_proof['source_core_id'] must be a string"
        )
    source_core_id = source_core_id.strip().upper()
    if source_core_id not in ALLOWED_SOURCE_CORES[capability]:
        raise ValueError(
            "DNA-32_INVALID_SOURCE_CORE:"
            f"{capability}:{source_core_id}"
        )

    if not isinstance(evidence, list):
        raise TypeError(
            "acceptance_proof['evidence'] must be a list"
        )
    if not evidence:
        raise ValueError(
            f"DNA-32_EVIDENCE_REQUIRED:{capability}"
        )

    if not isinstance(passed, bool):
        raise TypeError(
            "acceptance_proof['passed'] must be a bool"
        )

    return {
        "input_index": index,
        "capability": capability,
        "source_core_id": source_core_id,
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(evidence),
        "passed": passed,
    }


def _evaluate_acceptance(
    architecture: Dict[str, Any],
    supplied_proofs: Any,
    acceptance_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied_proofs, list):
        raise TypeError(
            "context['acceptance_proofs'] must be a list"
        )

    proofs = [
        _normalize_proof(item, index=index)
        for index, item in enumerate(
            supplied_proofs,
            start=1,
        )
    ]

    capabilities = [
        proof["capability"]
        for proof in proofs
    ]
    if len(capabilities) != len(set(capabilities)):
        raise ValueError(
            "DNA-32_DUPLICATE_CAPABILITY_PROOF"
        )

    present = set(capabilities)
    missing = [
        capability
        for capability in REQUIRED_CAPABILITIES
        if capability not in present
    ]

    failed = [
        proof["capability"]
        for proof in proofs
        if not proof["passed"]
    ]

    complete_proof_set = (
        not missing
        and len(proofs) == len(REQUIRED_CAPABILITIES)
    )
    all_proofs_passed = bool(
        complete_proof_set
        and all(proof["passed"] for proof in proofs)
    )

    architecture_eligible = not architecture[
        "forbidden_only_architecture"
    ]

    sigma_complete_eligible = bool(
        architecture_eligible
        and all_proofs_passed
    )

    sequence = len(acceptance_state["assessments"]) + 1
    assessment = {
        "sequence": sequence,
        "assessment_id": (
            f"DNA-32-ACCEPTANCE-{sequence:04d}"
        ),
        "architecture": deepcopy(architecture),
        "proofs": deepcopy(proofs),
        "capabilities_present": sorted(present),
        "missing_capabilities": missing,
        "failed_capabilities": failed,
        "complete_proof_set": complete_proof_set,
        "all_proofs_passed": all_proofs_passed,
        "architecture_eligible": architecture_eligible,
        "sigma_complete_eligible": sigma_complete_eligible,
        "completion_declared_by_dna32": False,
        "next_phase_opened_by_dna32": False,
        "external_action_executed": False,
        "status": (
            "ACCEPTANCE_CRITERIA_SATISFIED"
            if sigma_complete_eligible
            else "ACCEPTANCE_CRITERIA_NOT_SATISFIED"
        ),
    }

    acceptance_state["assessments"].append(
        deepcopy(assessment)
    )
    return assessment


def dna32_acceptance_criteria(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Evaluate whether SIGMA meets the exact Canon acceptance criteria.

    DNA-32 never declares Core54 complete, never opens the next phase,
    and never starts higher runtimes. It only evaluates supplied evidence.
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
    trace.append("DNA-32")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    acceptance_state = _install_acceptance_state(
        state
    )

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    architecture = _normalize_architecture(
        context.get("sigma_architecture")
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-32",
            "operation": (
                "ACCEPTANCE_CRITERIA_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "schema": ACCEPTANCE_CRITERIA_SCHEMA,
            "completion_declared": False,
            "next_phase_opened": False,
        }
    )

    assessment = _evaluate_acceptance(
        architecture,
        context.get("acceptance_proofs"),
        acceptance_state,
    )

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-32",
            "operation": (
                "SIGMA_ACCEPTANCE_ELIGIBILITY_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "assessment_id": assessment["assessment_id"],
            "architecture_eligible": (
                assessment["architecture_eligible"]
            ),
            "complete_proof_set": (
                assessment["complete_proof_set"]
            ),
            "all_proofs_passed": (
                assessment["all_proofs_passed"]
            ),
            "sigma_complete_eligible": (
                assessment["sigma_complete_eligible"]
            ),
            "completion_declared": False,
            "next_phase_opened": False,
        }
    )

    outputs["DNA-32"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "acceptance_contract": deepcopy(
            ACCEPTANCE_CRITERIA_CONTRACT
        ),
        "assessment": deepcopy(assessment),
        "sigma_complete_eligible": (
            assessment["sigma_complete_eligible"]
        ),
        "completion_declared": False,
        "next_phase_opened": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna32(core54: Core54Like) -> None:
    core = core54.get("DNA-32")
    assert_exact_canon(core)
    core54.bind(
        "DNA-32",
        dna32_acceptance_criteria,
    )


def _valid_architecture() -> Dict[str, Any]:
    return {
        "architecture_id": "SIGMA-CORE54-SELF-CHECK",
        "architecture_type": "MULTI_CORE_COGNITIVE_SYSTEM",
        "prompt_only": False,
        "llm_wrapper_only": False,
        "evidence": [
            {
                "type": "CORE_BINDING",
                "bound_cores": 32,
            }
        ],
    }


def _valid_proofs() -> List[Dict[str, Any]]:
    return [
        {
            "capability": "LEARNING",
            "source_core_id": "DNA-16",
            "evidence": [
                {
                    "type": "EXPERIENCE_DRIVEN_LEARNING_RECORD",
                    "result": "PASS",
                }
            ],
            "passed": True,
        },
        {
            "capability": "VERIFICATION",
            "source_core_id": "DNA-09",
            "evidence": [
                {
                    "type": "INDEPENDENT_VERIFICATION_RECORD",
                    "result": "PASS",
                }
            ],
            "passed": True,
        },
        {
            "capability": "TRANSFER",
            "source_core_id": "DNA-31",
            "evidence": [
                {
                    "type": "TRANSFER_MEASUREMENT",
                    "result": "PASS",
                }
            ],
            "passed": True,
        },
        {
            "capability": "FEEDBACK",
            "source_core_id": "DNA-06",
            "evidence": [
                {
                    "type": "INTERLAYER_FEEDBACK_RECORD",
                    "result": "PASS",
                }
            ],
            "passed": True,
        },
    ]


def self_check_dna32(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 32):
        core_id = f"DNA-{index:02d}"
        if not core54.get(core_id).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna32 = core54.get("DNA-32")
    assert_exact_canon(dna32)
    bind_dna32(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 32)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "sigma_architecture": _valid_architecture(),
        "acceptance_proofs": _valid_proofs(),
    }

    snapshot = deepcopy(probe)
    result = dna32.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-32"]
    assert output["canonical_gene"] == CANON_DNA32
    assert output["sigma_complete_eligible"] is True
    assert output["completion_declared"] is False
    assert output["next_phase_opened"] is False
    assert output["higher_runtime_started"] is False

    assessment = output["assessment"]
    assert assessment["architecture_eligible"] is True
    assert assessment["complete_proof_set"] is True
    assert assessment["all_proofs_passed"] is True
    assert assessment["missing_capabilities"] == []
    assert assessment["failed_capabilities"] == []
    assert assessment["sigma_complete_eligible"] is True
    assert assessment["completion_declared_by_dna32"] is False
    assert assessment["next_phase_opened_by_dna32"] is False

    # Prompt-only architecture can never satisfy acceptance.
    prompt_only = deepcopy(probe)
    prompt_only["sigma_architecture"] = {
        "architecture_id": "PROMPT-ONLY",
        "architecture_type": "PROMPT_ONLY",
        "prompt_only": True,
        "llm_wrapper_only": False,
        "evidence": [{"type": "ARCHITECTURE_DESCRIPTION"}],
    }
    prompt_result = dna32.activate(prompt_only)
    prompt_assessment = prompt_result[
        "core54_outputs"
    ]["DNA-32"]["assessment"]
    assert prompt_assessment["architecture_eligible"] is False
    assert prompt_assessment["sigma_complete_eligible"] is False

    # LLM-wrapper-only architecture can never satisfy acceptance.
    wrapper_only = deepcopy(probe)
    wrapper_only["sigma_architecture"] = {
        "architecture_id": "WRAPPER-ONLY",
        "architecture_type": "LLM_WRAPPER_ONLY",
        "prompt_only": False,
        "llm_wrapper_only": True,
        "evidence": [{"type": "ARCHITECTURE_DESCRIPTION"}],
    }
    wrapper_result = dna32.activate(wrapper_only)
    wrapper_assessment = wrapper_result[
        "core54_outputs"
    ]["DNA-32"]["assessment"]
    assert wrapper_assessment["architecture_eligible"] is False
    assert wrapper_assessment["sigma_complete_eligible"] is False

    # Missing transfer proof must fail acceptance.
    missing_transfer = deepcopy(probe)
    missing_transfer["acceptance_proofs"] = [
        item
        for item in _valid_proofs()
        if item["capability"] != "TRANSFER"
    ]
    missing_result = dna32.activate(missing_transfer)
    missing_assessment = missing_result[
        "core54_outputs"
    ]["DNA-32"]["assessment"]
    assert missing_assessment["complete_proof_set"] is False
    assert missing_assessment["missing_capabilities"] == [
        "TRANSFER"
    ]
    assert missing_assessment["sigma_complete_eligible"] is False

    # Failed feedback proof must fail acceptance.
    failed_feedback = deepcopy(probe)
    for item in failed_feedback["acceptance_proofs"]:
        if item["capability"] == "FEEDBACK":
            item["passed"] = False
    failed_result = dna32.activate(failed_feedback)
    failed_assessment = failed_result[
        "core54_outputs"
    ]["DNA-32"]["assessment"]
    assert failed_assessment["failed_capabilities"] == [
        "FEEDBACK"
    ]
    assert failed_assessment["sigma_complete_eligible"] is False

    # Wrong source core is not accepted as proof.
    wrong_source = deepcopy(probe)
    wrong_source["acceptance_proofs"][2][
        "source_core_id"
    ] = "DNA-06"
    try:
        dna32.activate(wrong_source)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-32_INVALID_SOURCE_CORE:TRANSFER:DNA-06"
        )
    else:
        raise AssertionError(
            "DNA-32_ACCEPTED_WRONG_SOURCE_CORE"
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

    canon_after = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )
    if verify_canon_file:
        assert canon_before == canon_after

    return {
        "core_id": "DNA-32",
        "canon_mapping": "PASS",
        "prompt_only_rejected": "PASS",
        "llm_wrapper_only_rejected": "PASS",
        "learning_proof": "PASS",
        "verification_proof": "PASS",
        "transfer_proof": "PASS",
        "feedback_proof": "PASS",
        "four_capability_gate": "PASS",
        "completion_declared": False,
        "next_phase_opened": False,
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
            "DNA-33"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


PRIOR_GENE_MODULES = {
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
}


def main() -> int:
    required_gene_files = [
        GENES_ROOT / f"{name}.py"
        for name in PRIOR_GENE_MODULES.values()
    ]

    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]:
        if not path.exists():
            print(
                "DNA-32_FAIL: REQUIRED_PATH_NOT_FOUND"
            )
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = {
            index: importlib.import_module(name)
            for index, name in PRIOR_GENE_MODULES.items()
        }
    except Exception as exc:
        print("DNA-32_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        if any(
            core.state.behavior_bound
            for core in core54.cores
        ):
            raise RuntimeError(
                "FRESH_FOUNDATION_REQUIRED"
            )

        for index in range(1, 32):
            checker = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )
            report = checker(
                core54,
                verify_canon_file=True,
            )
            if report["self_check"] != "PASS":
                raise RuntimeError(
                    f"DNA-{index:02d}_NOT_PASS"
                )

        report = self_check_dna32(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        assert bound_ids == [
            f"DNA-{index:02d}"
            for index in range(1, 33)
        ]

    except Exception as exc:
        print("DNA-32_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_32_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "PROMPT_ONLY_REJECTED:",
        report["prompt_only_rejected"],
    )
    print(
        "LLM_WRAPPER_ONLY_REJECTED:",
        report["llm_wrapper_only_rejected"],
    )
    print("LEARNING_PROOF:", report["learning_proof"])
    print(
        "VERIFICATION_PROOF:",
        report["verification_proof"],
    )
    print("TRANSFER_PROOF:", report["transfer_proof"])
    print("FEEDBACK_PROOF:", report["feedback_proof"])
    print(
        "FOUR_CAPABILITY_GATE:",
        report["four_capability_gate"],
    )
    print(
        "COMPLETION_DECLARED:",
        report["completion_declared"],
    )
    print(
        "NEXT_PHASE_OPENED:",
        report["next_phase_opened"],
    )
    print(
        "HIGHER_RUNTIME_STARTED:",
        report["higher_runtime_started"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print(
        "CANON_UNCHANGED:",
        report["canon_unchanged"],
    )
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 32/54")
    print("NEXT_AUTHORIZED: DNA-33")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
