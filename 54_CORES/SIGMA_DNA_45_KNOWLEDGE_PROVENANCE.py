#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-45: KNOWLEDGE PROVENANCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_45_KNOWLEDGE_PROVENANCE.py
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

CANON_DNA45: Dict[str, str] = {
    "id": "DNA-45",
    "name": "Knowledge Provenance",
    "purpose": (
        "Mọi knowledge có origin, evidence, verification method, time, "
        "version, confidence và contradictions."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
KNOWLEDGE_PROVENANCE_SCHEMA = "SIGMA_KNOWLEDGE_PROVENANCE_V1"

CANON_PROVENANCE_FIELDS = [
    "origin",
    "evidence",
    "verification_method",
    "time",
    "version",
    "confidence",
    "contradictions",
]

KNOWLEDGE_PROVENANCE_CONTRACT: Dict[str, Any] = {
    "schema": KNOWLEDGE_PROVENANCE_SCHEMA,
    "required_fields": deepcopy(CANON_PROVENANCE_FIELDS),
    "required_field_count": 7,
    "origin_required": True,
    "evidence_required": True,
    "verification_method_required": True,
    "time_required": True,
    "version_required": True,
    "confidence_required": True,
    "contradictions_required": True,
    "missing_contradictions_means_none": False,
    "missing_field_is_not_invented": True,
    "knowledge_truth_claimed_by_dna45": False,
    "knowledge_promotion_executed": False,
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
    if actual != CANON_DNA45:
        raise RuntimeError(
            "DNA-45_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA45, "actual": actual},
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
            "DNA-45_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )
    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )
    return state


def _install_provenance_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("knowledge_provenance")
    expected = {
        "contract": deepcopy(KNOWLEDGE_PROVENANCE_CONTRACT),
        "records": [],
    }

    if existing is None:
        state["knowledge_provenance"] = expected
        return state["knowledge_provenance"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['knowledge_provenance'] must be a dict"
        )

    if existing.get("contract") != KNOWLEDGE_PROVENANCE_CONTRACT:
        raise ValueError(
            "DNA-45_KNOWLEDGE_PROVENANCE_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("records"), list):
        raise TypeError(
            "knowledge_provenance['records'] must be a list"
        )

    return existing


def _normalize_confidence(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            "knowledge provenance confidence must be numeric"
        )

    confidence = float(value)

    if not math.isfinite(confidence):
        raise ValueError(
            "DNA-45_CONFIDENCE_NOT_FINITE"
        )

    if not 0.0 <= confidence <= 1.0:
        raise ValueError(
            "DNA-45_CONFIDENCE_OUT_OF_RANGE"
        )

    return confidence


def _require_nonempty_string(
    value: Any,
    field: str,
) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(
            f"DNA-45_{field.upper()}_REQUIRED"
        )
    return value


def _normalize_record(
    supplied: Any,
    *,
    index: int,
    sequence: int,
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            f"knowledge_records[{index}] must be a dict"
        )

    knowledge_id = supplied.get("knowledge_id")
    knowledge = supplied.get("knowledge")

    if not isinstance(knowledge_id, str) or not knowledge_id.strip():
        raise ValueError(
            "DNA-45_KNOWLEDGE_ID_REQUIRED"
        )

    if knowledge is None:
        raise ValueError(
            f"DNA-45_KNOWLEDGE_REQUIRED:{knowledge_id}"
        )

    missing = [
        field
        for field in CANON_PROVENANCE_FIELDS
        if field not in supplied
    ]

    if missing:
        raise ValueError(
            "DNA-45_PROVENANCE_FIELDS_MISSING:"
            + ",".join(missing)
        )

    origin = supplied["origin"]
    evidence = supplied["evidence"]
    verification_method = supplied["verification_method"]
    time_value = supplied["time"]
    version = supplied["version"]
    confidence = supplied["confidence"]
    contradictions = supplied["contradictions"]

    if origin is None:
        raise ValueError(
            f"DNA-45_ORIGIN_REQUIRED:{knowledge_id}"
        )

    if not isinstance(evidence, list) or not evidence:
        raise ValueError(
            f"DNA-45_EVIDENCE_REQUIRED:{knowledge_id}"
        )

    if verification_method is None:
        raise ValueError(
            f"DNA-45_VERIFICATION_METHOD_REQUIRED:{knowledge_id}"
        )

    _require_nonempty_string(
        time_value,
        "time",
    )
    _require_nonempty_string(
        version,
        "version",
    )

    normalized_confidence = _normalize_confidence(
        confidence
    )

    if not isinstance(contradictions, list):
        raise TypeError(
            "knowledge provenance contradictions must be a list"
        )

    return {
        "sequence": sequence,
        "record_id": (
            f"DNA-45-KNOWLEDGE-{sequence:04d}"
        ),
        "input_index": index,
        "knowledge_id": knowledge_id,
        "knowledge": deepcopy(knowledge),
        "knowledge_sha256": _sha256_json(knowledge),
        "origin": deepcopy(origin),
        "origin_sha256": _sha256_json(origin),
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(evidence),
        "verification_method": deepcopy(
            verification_method
        ),
        "verification_method_sha256": _sha256_json(
            verification_method
        ),
        "time": time_value,
        "version": version,
        "confidence": normalized_confidence,
        "contradictions": deepcopy(contradictions),
        "contradictions_sha256": _sha256_json(
            contradictions
        ),
        "provenance_complete": True,
        "knowledge_truth_claimed_by_dna45": False,
        "knowledge_promoted_by_dna45": False,
        "status": "KNOWLEDGE_PROVENANCE_COMPLETE",
    }


def _evaluate_records(
    supplied: Any,
    provenance_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, list):
        raise TypeError(
            "context['knowledge_records'] must be a list"
        )

    start = len(
        provenance_state["records"]
    ) + 1

    records = [
        _normalize_record(
            item,
            index=index,
            sequence=start + index - 1,
        )
        for index, item in enumerate(
            supplied,
            start=1,
        )
    ]

    ids = [
        record["knowledge_id"]
        for record in records
    ]

    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-45_DUPLICATE_KNOWLEDGE_ID"
        )

    provenance_state["records"].extend(
        deepcopy(records)
    )

    return {
        "records": records,
        "record_count": len(records),
        "all_provenance_complete": all(
            record["provenance_complete"]
            for record in records
        ),
    }


def dna45_knowledge_provenance(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Require every supplied knowledge record to carry:
    origin, evidence, verification method, time, version, confidence,
    and contradictions.

    DNA-45 records provenance only. It does not claim truth, promote
    knowledge, start Memory/Learning Runtime, call models, perform external
    actions, or modify Canon.
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
    trace.append("DNA-45")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    provenance_state = _install_provenance_state(
        state
    )

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(
        actual_canon
    )

    evaluation = _evaluate_records(
        context.get("knowledge_records"),
        provenance_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-45",
            "operation": (
                "KNOWLEDGE_PROVENANCE_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "record_count": evaluation[
                "record_count"
            ],
            "all_provenance_complete": (
                evaluation[
                    "all_provenance_complete"
                ]
            ),
            "knowledge_truth_claimed": False,
            "knowledge_promoted": False,
            "memory_runtime_started": False,
        }
    )

    outputs["DNA-45"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "knowledge_provenance_contract": deepcopy(
            KNOWLEDGE_PROVENANCE_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "origin": "PASS",
        "evidence": "PASS",
        "verification_method": "PASS",
        "time": "PASS",
        "version": "PASS",
        "confidence": "PASS",
        "contradictions": "PASS",
        "seven_field_provenance_gate": (
            evaluation[
                "all_provenance_complete"
            ]
        ),
        "knowledge_truth_claimed": False,
        "knowledge_promotion_executed": False,
        "memory_runtime_started": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna45(
    core54: Core54Like,
) -> None:
    core = core54.get("DNA-45")
    assert_exact_canon(core)
    core54.bind(
        "DNA-45",
        dna45_knowledge_provenance,
    )


def _valid_record() -> Dict[str, Any]:
    return {
        "knowledge_id": "K-001",
        "knowledge": {
            "claim": "CLAIM_ALPHA",
        },
        "origin": {
            "source": "OBSERVATION_SET_A",
            "source_id": "SRC-A",
        },
        "evidence": [
            {
                "evidence_id": "EV-1",
                "result": "SUPPORTS_CLAIM_ALPHA",
            }
        ],
        "verification_method": {
            "method": "INDEPENDENT_CHECK",
            "verifier_id": "VERIFIER-A",
        },
        "time": "2026-08-10T00:00:00Z",
        "version": "v1",
        "confidence": 0.8,
        "contradictions": [
            {
                "contradiction_id": "C-1",
                "status": "OPEN",
            }
        ],
    }


def self_check_dna45(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 45):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-45")
    assert_exact_canon(core)
    bind_dna45(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 45)
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
        "knowledge_records": [
            _valid_record(),
        ],
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-45"]

    assert output[
        "canonical_gene"
    ] == CANON_DNA45

    assert output["origin"] == "PASS"
    assert output["evidence"] == "PASS"
    assert output[
        "verification_method"
    ] == "PASS"
    assert output["time"] == "PASS"
    assert output["version"] == "PASS"
    assert output["confidence"] == "PASS"
    assert output["contradictions"] == "PASS"
    assert (
        output[
            "seven_field_provenance_gate"
        ]
        is True
    )

    record = output[
        "evaluation"
    ]["records"][0]

    assert (
        record[
            "provenance_complete"
        ]
        is True
    )
    assert (
        record[
            "knowledge_truth_claimed_by_dna45"
        ]
        is False
    )
    assert (
        record[
            "knowledge_promoted_by_dna45"
        ]
        is False
    )

    # Every Canon field is mandatory.
    for field in CANON_PROVENANCE_FIELDS:
        missing = deepcopy(probe)
        del missing[
            "knowledge_records"
        ][0][field]

        try:
            core.activate(missing)
        except ValueError as exc:
            assert str(exc) == (
                "DNA-45_PROVENANCE_FIELDS_MISSING:"
                + field
            )
        else:
            raise AssertionError(
                f"DNA-45_ACCEPTED_MISSING_FIELD:{field}"
            )

    # Empty contradiction list is valid and explicit.
    explicit_none = deepcopy(probe)
    explicit_none[
        "knowledge_records"
    ][0]["contradictions"] = []

    explicit_result = core.activate(
        explicit_none
    )
    explicit_record = explicit_result[
        "core54_outputs"
    ]["DNA-45"]["evaluation"]["records"][0]

    assert explicit_record[
        "contradictions"
    ] == []
    assert (
        explicit_record[
            "provenance_complete"
        ]
        is True
    )

    # Confidence must be calibrated to [0,1].
    bad_confidence = deepcopy(probe)
    bad_confidence[
        "knowledge_records"
    ][0]["confidence"] = 1.25

    try:
        core.activate(
            bad_confidence
        )
    except ValueError as exc:
        assert str(exc) == (
            "DNA-45_CONFIDENCE_OUT_OF_RANGE"
        )
    else:
        raise AssertionError(
            "DNA-45_ACCEPTED_INVALID_CONFIDENCE"
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

    assert not any(
        locks.values()
    ), locks

    after = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    if verify_canon_file:
        assert before == after

    return {
        "core_id": "DNA-45",
        "canon_mapping": "PASS",
        "origin": "PASS",
        "evidence": "PASS",
        "verification_method": "PASS",
        "time": "PASS",
        "version": "PASS",
        "confidence": "PASS",
        "contradictions": "PASS",
        "seven_field_provenance_gate": "PASS",
        "knowledge_truth_claimed": False,
        "knowledge_promotion_executed": False,
        "memory_runtime_started": False,
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
            "DNA-46"
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
    44: "SIGMA_DNA_44_ADVERSARIAL_SELF_TESTING",
}


def main() -> int:
    for path in [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
    ]:
        if not path.exists():
            print(
                "DNA-45_FAIL: REQUIRED_PATH_NOT_FOUND"
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
            "DNA-45_FAIL: IMPORT_ERROR"
        )
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for index in range(1, 45):
            report = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna45(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-45_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_45_PASS")
    print(
        "CANON_MAPPING:",
        report["canon_mapping"],
    )
    print(
        "ORIGIN:",
        report["origin"],
    )
    print(
        "EVIDENCE:",
        report["evidence"],
    )
    print(
        "VERIFICATION_METHOD:",
        report["verification_method"],
    )
    print(
        "TIME:",
        report["time"],
    )
    print(
        "VERSION:",
        report["version"],
    )
    print(
        "CONFIDENCE:",
        report["confidence"],
    )
    print(
        "CONTRADICTIONS:",
        report["contradictions"],
    )
    print(
        "SEVEN_FIELD_PROVENANCE_GATE:",
        report[
            "seven_field_provenance_gate"
        ],
    )
    print(
        "KNOWLEDGE_TRUTH_CLAIMED:",
        report["knowledge_truth_claimed"],
    )
    print(
        "KNOWLEDGE_PROMOTION_EXECUTED:",
        report[
            "knowledge_promotion_executed"
        ],
    )
    print(
        "MEMORY_RUNTIME_STARTED:",
        report["memory_runtime_started"],
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
        "OFFICIAL_BOUND_CORES: 45/54"
    )
    print(
        "NEXT_AUTHORIZED: DNA-46"
    )
    print(
        "NEXT_PHASE: FORBIDDEN"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
