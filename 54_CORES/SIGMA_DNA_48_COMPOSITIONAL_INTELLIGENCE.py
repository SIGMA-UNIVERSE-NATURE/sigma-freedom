#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-48: COMPOSITIONAL INTELLIGENCE
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_48_COMPOSITIONAL_INTELLIGENCE.py
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

CANON_DNA48: Dict[str, str] = {
    "id": "DNA-48",
    "name": "Compositional Intelligence",
    "purpose": (
        "Ghép skills/concepts để sinh năng lực mới có tính tổ hợp."
    ),
    "system": "intelligence",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
COMPOSITIONAL_INTELLIGENCE_SCHEMA = "SIGMA_COMPOSITIONAL_INTELLIGENCE_V1"

CONTRACT: Dict[str, Any] = {
    "schema": COMPOSITIONAL_INTELLIGENCE_SCHEMA,
    "minimum_components": 2,
    "allowed_component_types": ["SKILL", "CONCEPT"],
    "composition_requires_traceable_components": True,
    "new_capability_requires_composition_artifact": True,
    "single_component_is_not_composition": True,
    "component_duplication_is_not_composition": True,
    "capability_execution_started": False,
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
    if actual != CANON_DNA48:
        raise RuntimeError(
            "DNA-48_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA48, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")
    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError("DNA-48_UNIFIED_STATE_SCHEMA_MISMATCH")
    if not isinstance(state.get("provenance"), list):
        raise TypeError("cognitive_state.provenance must be a list")
    return state


def _install_state(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("compositional_intelligence")
    expected = {
        "contract": deepcopy(CONTRACT),
        "compositions": [],
    }

    if existing is None:
        state["compositional_intelligence"] = expected
        return state["compositional_intelligence"]

    if not isinstance(existing, dict):
        raise TypeError(
            "compositional_intelligence must be a dict"
        )
    if existing.get("contract") != CONTRACT:
        raise ValueError(
            "DNA-48_COMPOSITIONAL_INTELLIGENCE_CONTRACT_CONFLICT"
        )
    if not isinstance(existing.get("compositions"), list):
        raise TypeError(
            "compositional_intelligence.compositions must be a list"
        )
    return existing


def _normalize_component(
    item: Any,
    *,
    index: int,
) -> Dict[str, Any]:
    if not isinstance(item, dict):
        raise TypeError(
            f"components[{index}] must be a dict"
        )

    component_id = item.get("component_id")
    component_type = item.get("type")
    artifact = item.get("artifact")

    if not isinstance(component_id, str) or not component_id.strip():
        raise ValueError(
            "DNA-48_COMPONENT_ID_REQUIRED"
        )

    if not isinstance(component_type, str):
        raise TypeError(
            "component type must be a string"
        )

    component_type = component_type.strip().upper()
    if component_type not in {"SKILL", "CONCEPT"}:
        raise ValueError(
            f"DNA-48_UNKNOWN_COMPONENT_TYPE:{component_type}"
        )

    if artifact is None:
        raise ValueError(
            f"DNA-48_COMPONENT_ARTIFACT_REQUIRED:{component_id}"
        )

    return {
        "input_index": index,
        "component_id": component_id,
        "type": component_type,
        "artifact": deepcopy(artifact),
        "artifact_sha256": _sha256_json(artifact),
    }


def _evaluate(
    supplied: Any,
    composition_state: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        raise TypeError(
            "context['composition_candidate'] must be a dict"
        )

    composition_id = supplied.get("composition_id")
    components = supplied.get("components")
    capability = supplied.get("new_capability")
    composition_artifact = supplied.get(
        "composition_artifact"
    )

    if not isinstance(
        composition_id,
        str,
    ) or not composition_id.strip():
        raise ValueError(
            "DNA-48_COMPOSITION_ID_REQUIRED"
        )

    if not isinstance(components, list):
        raise TypeError(
            "composition_candidate.components must be a list"
        )

    if len(components) < 2:
        raise ValueError(
            "DNA-48_MULTIPLE_COMPONENTS_REQUIRED"
        )

    normalized = [
        _normalize_component(
            item,
            index=index,
        )
        for index, item in enumerate(
            components,
            start=1,
        )
    ]

    ids = [
        item["component_id"]
        for item in normalized
    ]
    if len(ids) != len(set(ids)):
        raise ValueError(
            "DNA-48_DUPLICATE_COMPONENT_ID"
        )

    hashes = [
        item["artifact_sha256"]
        for item in normalized
    ]
    if len(set(hashes)) < 2:
        raise ValueError(
            "DNA-48_DISTINCT_COMPONENTS_REQUIRED"
        )

    if capability is None:
        raise ValueError(
            "DNA-48_NEW_CAPABILITY_REQUIRED"
        )

    if composition_artifact is None:
        raise ValueError(
            "DNA-48_COMPOSITION_ARTIFACT_REQUIRED"
        )

    sequence = len(
        composition_state["compositions"]
    ) + 1

    record = {
        "sequence": sequence,
        "record_id": (
            f"DNA-48-COMPOSITION-{sequence:04d}"
        ),
        "composition_id": composition_id,
        "components": deepcopy(normalized),
        "component_count": len(normalized),
        "component_types": sorted(
            {
                item["type"]
                for item in normalized
            }
        ),
        "new_capability": deepcopy(capability),
        "new_capability_sha256": _sha256_json(capability),
        "composition_artifact": deepcopy(
            composition_artifact
        ),
        "composition_artifact_sha256": _sha256_json(
            composition_artifact
        ),
        "compositional_capability_formed": True,
        "capability_execution_started": False,
        "learning_runtime_started": False,
        "external_action_executed": False,
        "status": "COMPOSITIONAL_CAPABILITY_STRUCTURED",
    }

    composition_state["compositions"].append(
        deepcopy(record)
    )
    return record


def dna48_compositional_intelligence(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Compose multiple distinct skill/concept artifacts into a traceable
    new compositional capability artifact.

    DNA-48 structures and validates the composition only. It does not run
    the new capability, start Learning Runtime, call models/tools, perform
    external actions, or modify Canon.
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
    trace.append("DNA-48")

    outputs = context.setdefault(
        "core54_outputs",
        {},
    )
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state = _validate_state(context)
    composition_state = _install_state(state)

    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)

    record = _evaluate(
        context.get("composition_candidate"),
        composition_state,
    )

    state["provenance"].append(
        {
            "sequence": len(
                state["provenance"]
            ) + 1,
            "core_id": "DNA-48",
            "operation": (
                "COMPOSITIONAL_INTELLIGENCE_EVALUATED"
            ),
            "canonical_sha256": canon_sha,
            "record_id": record["record_id"],
            "component_count": record[
                "component_count"
            ],
            "component_types": deepcopy(
                record["component_types"]
            ),
            "compositional_capability_formed": True,
            "capability_execution_started": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-48"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "compositional_intelligence_contract": deepcopy(
            CONTRACT
        ),
        "record": deepcopy(record),
        "multiple_components": "PASS",
        "skills_concepts_composition": "PASS",
        "new_compositional_capability": "PASS",
        "traceable_composition": "PASS",
        "capability_execution_started": False,
        "learning_runtime_started": False,
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna48(core54: Core54Like) -> None:
    core = core54.get("DNA-48")
    assert_exact_canon(core)
    core54.bind(
        "DNA-48",
        dna48_compositional_intelligence,
    )


def self_check_dna48(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 48):
        core_id = f"DNA-{index:02d}"
        if not core54.get(
            core_id
        ).state.behavior_bound:
            raise RuntimeError(
                f"{core_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    core = core54.get("DNA-48")
    assert_exact_canon(core)
    bind_dna48(core54)

    probe = {
        "trace": [
            f"DNA-{index:02d}"
            for index in range(1, 48)
        ],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "composition_candidate": {
            "composition_id": "DNA48-SELF-CHECK",
            "components": [
                {
                    "component_id": "SKILL-A",
                    "type": "SKILL",
                    "artifact": {
                        "operation": "DETECT_PATTERN",
                    },
                },
                {
                    "component_id": "CONCEPT-B",
                    "type": "CONCEPT",
                    "artifact": {
                        "concept": "CAUSAL_RELATION",
                    },
                },
            ],
            "new_capability": {
                "capability_id": "CAP-COMPOSED-1",
                "description": (
                    "Use pattern detection with a causal concept "
                    "to structure a new combined capability."
                ),
            },
            "composition_artifact": {
                "composition": [
                    "SKILL-A",
                    "CONCEPT-B",
                ],
                "relation": "COMPOSED_TO_FORM",
                "output": "CAP-COMPOSED-1",
            },
        },
    }

    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result[
        "core54_outputs"
    ]["DNA-48"]

    assert output["canonical_gene"] == CANON_DNA48
    assert output["multiple_components"] == "PASS"
    assert output[
        "skills_concepts_composition"
    ] == "PASS"
    assert output[
        "new_compositional_capability"
    ] == "PASS"
    assert output["traceable_composition"] == "PASS"
    assert output[
        "capability_execution_started"
    ] is False
    assert output[
        "learning_runtime_started"
    ] is False
    assert output[
        "higher_runtime_started"
    ] is False

    record = output["record"]
    assert record["component_count"] == 2
    assert set(record["component_types"]) == {
        "SKILL",
        "CONCEPT",
    }
    assert (
        record["compositional_capability_formed"]
        is True
    )

    # One component is not compositional intelligence.
    single = deepcopy(probe)
    single[
        "composition_candidate"
    ]["components"] = single[
        "composition_candidate"
    ]["components"][:1]

    try:
        core.activate(single)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-48_MULTIPLE_COMPONENTS_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-48_ACCEPTED_SINGLE_COMPONENT"
        )

    # Duplicate component IDs are forbidden.
    duplicate = deepcopy(probe)
    duplicate[
        "composition_candidate"
    ]["components"][1][
        "component_id"
    ] = "SKILL-A"

    try:
        core.activate(duplicate)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-48_DUPLICATE_COMPONENT_ID"
        )
    else:
        raise AssertionError(
            "DNA-48_ACCEPTED_DUPLICATE_COMPONENT"
        )

    # Composition artifact is mandatory.
    no_artifact = deepcopy(probe)
    no_artifact[
        "composition_candidate"
    ]["composition_artifact"] = None

    try:
        core.activate(no_artifact)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-48_COMPOSITION_ARTIFACT_REQUIRED"
        )
    else:
        raise AssertionError(
            "DNA-48_ACCEPTED_MISSING_COMPOSITION_ARTIFACT"
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
        "core_id": "DNA-48",
        "canon_mapping": "PASS",
        "multiple_components": "PASS",
        "skills_concepts_composition": "PASS",
        "new_compositional_capability": "PASS",
        "traceable_composition": "PASS",
        "capability_execution_started": False,
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
            "DNA-49"
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
}


def main() -> int:
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON]:
        if not path.exists():
            print(
                "DNA-48_FAIL: REQUIRED_PATH_NOT_FOUND"
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
            "DNA-48_FAIL: IMPORT_ERROR"
        )
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for i in range(1, 48):
            report = getattr(
                modules[i],
                f"self_check_dna{i:02d}",
            )(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna48(
            core54,
            verify_canon_file=True,
        )

    except Exception as exc:
        print("DNA-48_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_48_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print(
        "MULTIPLE_COMPONENTS:",
        report["multiple_components"],
    )
    print(
        "SKILLS_CONCEPTS_COMPOSITION:",
        report["skills_concepts_composition"],
    )
    print(
        "NEW_COMPOSITIONAL_CAPABILITY:",
        report["new_compositional_capability"],
    )
    print(
        "TRACEABLE_COMPOSITION:",
        report["traceable_composition"],
    )
    print(
        "CAPABILITY_EXECUTION_STARTED:",
        report["capability_execution_started"],
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
    print("OFFICIAL_BOUND_CORES: 48/54")
    print("NEXT_AUTHORIZED: DNA-49")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
