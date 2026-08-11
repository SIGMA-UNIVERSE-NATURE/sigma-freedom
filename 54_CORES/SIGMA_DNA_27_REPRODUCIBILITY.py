#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-27: REPRODUCIBILITY
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_27_REPRODUCIBILITY.py
"""

from __future__ import annotations

import hashlib
import importlib
import json
import string
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

CANON_DNA27: Dict[str, str] = {
    "id": "DNA-27",
    "name": "Reproducibility",
    "purpose": (
        "Mọi experiment quan trọng phải tái lập được bằng input, "
        "version, config, result và verifier record."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
VERIFICATION_WALL_SCHEMA = (
    "SIGMA_INDEPENDENT_VERIFICATION_WALL_V1"
)
OBSERVABILITY_SCHEMA = "SIGMA_OBSERVABILITY_V1"
REPRODUCIBILITY_SCHEMA = "SIGMA_REPRODUCIBILITY_V1"

REQUIRED_EXPERIMENT_FIELDS = [
    "experiment_id",
    "important",
    "input",
    "version",
    "config",
    "result",
    "verifier_record",
]

VERIFIER_RECORD_FIELDS = [
    "evaluation_id",
    "verifier_id",
    "independent",
    "passed",
    "source_sha256",
]

REPRODUCIBILITY_CONTRACT: Dict[str, Any] = {
    "schema": REPRODUCIBILITY_SCHEMA,
    "input_path": "reproducibility_experiments",
    "state_path": "cognitive_state.reproducibility",
    "important_experiment_fields": deepcopy(
        REQUIRED_EXPERIMENT_FIELDS
    ),
    "verifier_record_fields": deepcopy(
        VERIFIER_RECORD_FIELDS
    ),
    "important_experiment_requires_complete_package": True,
    "package_components": [
        "input",
        "version",
        "config",
        "result",
        "verifier_record",
    ],
    "verifier_record_must_bind_to_dna09": True,
    "result_must_bind_to_verifier_candidate": True,
    "integrity_encoding": {
        "components": "CANONICAL_JSON_SHA256",
        "package": "CANONICAL_JSON_SHA256",
        "append_chain": "SHA256_PREVIOUS_CHAIN_PLUS_RECORD",
        "canon_status": (
            "IMPLEMENTATION_ENCODING_NOT_CANON_FIELD"
        ),
    },
    "reproducible_semantics": (
        "COMPLETE_DETERMINISTIC_REPLAY_PACKAGE_WITH_BOUND_VERIFIER_RECORD"
    ),
    "actual_replay_executed_by_dna27": False,
    "result_reproduced_by_dna27": False,
    "experiment_executed_by_dna27": False,
    "external_persistence_started": False,
    "memory_runtime_started": False,
    "learning_runtime_started": False,
    "truth_established_by_dna27": False,
    "knowledge_promoted_by_dna27": False,
    "model_calls_started": False,
    "external_action_executed": False,
    "derivation": (
        "DIRECT_FROM_CANON_PURPOSE_WITH_DNA09_VERIFIER_"
        "AND_DNA26_OBSERVABILITY_BINDING"
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


def _canonical_json(value: Any) -> str:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise TypeError(
            "DNA-27_REPRODUCIBILITY_COMPONENT_MUST_BE_"
            "CANONICAL_JSON_SERIALIZABLE"
        ) from exc


def _sha256_json(value: Any) -> str:
    return hashlib.sha256(
        _canonical_json(value).encode("utf-8")
    ).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _is_sha256(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(
            character in string.hexdigits
            for character in value
        )
    )


def _non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA27:
        raise RuntimeError(
            "DNA-27_CANON_MISMATCH:"
            + json.dumps(
                {
                    "expected": CANON_DNA27,
                    "actual": actual,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Tuple[
    Dict[str, Any],
    Dict[str, Any],
    Dict[str, Any],
]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-27_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] "
            "must be a list"
        )

    verification_wall = state.get(
        "independent_verification_wall"
    )
    if not isinstance(verification_wall, dict):
        raise RuntimeError(
            "DNA-09_INDEPENDENT_VERIFICATION_WALL_REQUIRED"
        )

    verification_contract = verification_wall.get(
        "contract"
    )
    if not isinstance(verification_contract, dict):
        raise RuntimeError(
            "DNA-09_VERIFICATION_WALL_CONTRACT_REQUIRED"
        )

    if verification_contract.get("schema") != (
        VERIFICATION_WALL_SCHEMA
    ):
        raise ValueError(
            "DNA-27_VERIFICATION_WALL_SCHEMA_MISMATCH:"
            f"{verification_contract.get('schema')!r}"
        )

    if not isinstance(
        verification_wall.get("evaluations"),
        list,
    ):
        raise TypeError(
            "independent_verification_wall['evaluations'] "
            "must be a list"
        )

    observability = state.get("observability")
    if not isinstance(observability, dict):
        raise RuntimeError(
            "DNA-26_OBSERVABILITY_REQUIRED"
        )

    observability_contract = observability.get("contract")
    if not isinstance(observability_contract, dict):
        raise RuntimeError(
            "DNA-26_OBSERVABILITY_CONTRACT_REQUIRED"
        )

    if observability_contract.get("schema") != (
        OBSERVABILITY_SCHEMA
    ):
        raise ValueError(
            "DNA-27_OBSERVABILITY_SCHEMA_MISMATCH:"
            f"{observability_contract.get('schema')!r}"
        )

    if not isinstance(observability.get("artifacts"), list):
        raise TypeError(
            "observability['artifacts'] must be a list"
        )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError(
            "DNA-09_AND_DNA-26_OUTPUTS_REQUIRED"
        )

    for required_id in ("DNA-09", "DNA-26"):
        if not isinstance(outputs.get(required_id), dict):
            raise RuntimeError(
                f"{required_id}_OUTPUT_REQUIRED"
            )

    return state, verification_wall, observability


def _install_reproducibility_state(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("reproducibility")

    expected = {
        "contract": deepcopy(REPRODUCIBILITY_CONTRACT),
        "experiments": [],
        "batches": [],
    }

    if existing is None:
        state["reproducibility"] = expected
        return state["reproducibility"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['reproducibility'] must be a dict"
        )

    if existing.get("contract") != REPRODUCIBILITY_CONTRACT:
        raise ValueError(
            "DNA-27_REPRODUCIBILITY_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("experiments"), list):
        raise TypeError(
            "reproducibility['experiments'] must be a list"
        )

    if not isinstance(existing.get("batches"), list):
        raise TypeError(
            "reproducibility['batches'] must be a list"
        )

    if not _verify_registry_chain(existing):
        raise RuntimeError(
            "DNA-27_EXISTING_REPRODUCIBILITY_CHAIN_INVALID"
        )

    return existing


def _find_evaluation(
    verification_wall: Dict[str, Any],
    evaluation_id: Any,
) -> Optional[Dict[str, Any]]:
    matches = [
        evaluation
        for evaluation in verification_wall["evaluations"]
        if isinstance(evaluation, dict)
        and evaluation.get("evaluation_id") == evaluation_id
    ]
    if len(matches) > 1:
        raise RuntimeError(
            "DNA-27_DUPLICATE_DNA09_EVALUATION_ID:"
            f"{evaluation_id}"
        )
    return matches[0] if matches else None


def _latest_observability_source(
    observability: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    artifacts = observability["artifacts"]
    if not artifacts:
        return None

    artifact = artifacts[-1]
    if not isinstance(artifact, dict):
        raise TypeError(
            "DNA-26 observability artifact must be a dict"
        )

    source_bound = bool(
        artifact.get("artifact_complete") is True
        and artifact.get("integrity_verifiable") is True
        and _is_sha256(artifact.get("artifact_sha256"))
        and _is_sha256(artifact.get("chain_sha256"))
    )

    return {
        "artifact_id": artifact.get("artifact_id"),
        "artifact_sha256": artifact.get("artifact_sha256"),
        "chain_sha256": artifact.get("chain_sha256"),
        "source_bound": source_bound,
    }


def _normalize_verifier_record(
    supplied: Any,
    *,
    verification_wall: Dict[str, Any],
    result: Any,
    errors: List[str],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        errors.append("VERIFIER_RECORD_DICT_REQUIRED")
        return {
            "evaluation_id": None,
            "verifier_id": None,
            "independent": None,
            "passed": None,
            "source_sha256": None,
            "evaluation_found": False,
            "source_bound": False,
            "result_bound": False,
            "complete": False,
        }

    record = deepcopy(supplied)
    missing = [
        field
        for field in VERIFIER_RECORD_FIELDS
        if field not in record
    ]
    if missing:
        errors.append("VERIFIER_RECORD_FIELDS_MISSING")

    for field in ("evaluation_id", "verifier_id"):
        if field in record and not isinstance(record[field], str):
            raise TypeError(
                f"verifier_record['{field}'] must be a string"
            )

    for field in ("independent", "passed"):
        if field in record and not isinstance(record[field], bool):
            raise TypeError(
                f"verifier_record['{field}'] must be a bool"
            )

    if (
        "source_sha256" in record
        and not isinstance(record["source_sha256"], str)
    ):
        raise TypeError(
            "verifier_record['source_sha256'] must be a string"
        )

    evaluation_id = record.get("evaluation_id")
    evaluation = _find_evaluation(
        verification_wall,
        evaluation_id,
    )

    if evaluation is None:
        errors.append("DNA09_EVALUATION_NOT_FOUND")
        return {
            "evaluation_id": evaluation_id,
            "verifier_id": record.get("verifier_id"),
            "independent": record.get("independent"),
            "passed": record.get("passed"),
            "source_sha256": record.get("source_sha256"),
            "evaluation_found": False,
            "source_bound": False,
            "result_bound": False,
            "complete": False,
        }

    verification_record = evaluation.get("verification_record")
    if not isinstance(verification_record, dict):
        raise RuntimeError(
            "DNA-27_DNA09_VERIFICATION_RECORD_INVALID"
        )

    expected = {
        "evaluation_id": evaluation.get("evaluation_id"),
        "verifier_id": verification_record.get("verifier_id"),
        "independent": evaluation.get("independent_verifier"),
        "passed": evaluation.get("verification_passed"),
        "source_sha256": _sha256_json(evaluation),
    }

    source_bound = all(
        record.get(field) == expected[field]
        for field in VERIFIER_RECORD_FIELDS
    )
    if not source_bound:
        errors.append("VERIFIER_RECORD_SOURCE_MISMATCH")

    candidate = evaluation.get("candidate")
    result_bound = bool(
        candidate is not None
        and result == candidate
    )
    if not result_bound:
        errors.append("RESULT_NOT_BOUND_TO_VERIFIER_CANDIDATE")

    complete = bool(
        not missing
        and source_bound
        and result_bound
    )

    return {
        **expected,
        "evaluation_found": True,
        "source_bound": source_bound,
        "result_bound": result_bound,
        "complete": complete,
    }


def _record_content(record: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "experiment_id": record["experiment_id"],
        "important": record["important"],
        "input": deepcopy(record["input"]),
        "version": deepcopy(record["version"]),
        "config": deepcopy(record["config"]),
        "result": deepcopy(record["result"]),
        "verifier_record": deepcopy(record["verifier_record"]),
        "component_sha256": deepcopy(
            record["component_sha256"]
        ),
        "package_sha256": record["package_sha256"],
        "observability_source": deepcopy(
            record["observability_source"]
        ),
        "package_complete": record["package_complete"],
        "reproducible": record["reproducible"],
        "important_requirement_satisfied": record[
            "important_requirement_satisfied"
        ],
        "errors": deepcopy(record["errors"]),
        "status": record["status"],
    }


def _verify_record_integrity(
    record: Dict[str, Any],
    previous_chain_sha256: Optional[str],
) -> bool:
    try:
        record_sha256 = _sha256_json(
            _record_content(record)
        )
        chain_sha256 = _sha256_json(
            {
                "previous_chain_sha256": (
                    previous_chain_sha256
                ),
                "record_sha256": record_sha256,
            }
        )
        return bool(
            record.get("record_sha256") == record_sha256
            and record.get("previous_chain_sha256")
            == previous_chain_sha256
            and record.get("chain_sha256") == chain_sha256
        )
    except Exception:
        return False


def _verify_registry_chain(
    registry: Dict[str, Any],
) -> bool:
    experiments = registry.get("experiments")
    if not isinstance(experiments, list):
        return False

    previous: Optional[str] = None
    for record in experiments:
        if not isinstance(record, dict):
            return False
        if not _verify_record_integrity(record, previous):
            return False
        previous = record.get("chain_sha256")
    return True


def _normalize_experiment(
    supplied: Any,
    *,
    input_index: int,
    sequence: int,
    previous_chain_sha256: Optional[str],
    verification_wall: Dict[str, Any],
    observability: Dict[str, Any],
) -> Dict[str, Any]:
    if not isinstance(supplied, dict):
        supplied_record: Dict[str, Any] = {}
        errors: List[str] = [
            "REPRODUCIBILITY_EXPERIMENT_MUST_BE_A_DICT"
        ]
    else:
        supplied_record = deepcopy(supplied)
        errors = []

    missing = [
        field
        for field in REQUIRED_EXPERIMENT_FIELDS
        if field not in supplied_record
    ]
    if missing:
        errors.append("REPRODUCIBILITY_FIELDS_MISSING")

    experiment_id = supplied_record.get("experiment_id")
    if not _non_empty_text(experiment_id):
        errors.append("EXPERIMENT_ID_REQUIRED")

    important = supplied_record.get("important")
    if not isinstance(important, bool):
        if "important" in supplied_record:
            raise TypeError(
                "reproducibility_experiment['important'] "
                "must be a bool"
            )
        errors.append("IMPORTANT_STATUS_REQUIRED")
        important = None

    components: Dict[str, Any] = {
        field: deepcopy(supplied_record.get(field))
        for field in (
            "input",
            "version",
            "config",
            "result",
        )
    }

    for field in ("input", "version", "config", "result"):
        if field in supplied_record:
            _canonical_json(components[field])

    version = components["version"]
    if "version" in supplied_record:
        version_non_empty = bool(
            (isinstance(version, str) and version.strip())
            or (isinstance(version, dict) and version)
            or (isinstance(version, list) and version)
            or isinstance(version, (int, float))
        )
        if not version_non_empty:
            errors.append("VERSION_MUST_BE_NON_EMPTY")

    verifier_record = _normalize_verifier_record(
        supplied_record.get("verifier_record"),
        verification_wall=verification_wall,
        result=components["result"],
        errors=errors,
    )

    component_sha256 = {
        field: (
            _sha256_json(components[field])
            if field in supplied_record
            else None
        )
        for field in ("input", "version", "config", "result")
    }
    component_sha256["verifier_record"] = (
        _sha256_json(
            {
                field: verifier_record.get(field)
                for field in VERIFIER_RECORD_FIELDS
            }
        )
        if isinstance(
            supplied_record.get("verifier_record"),
            dict,
        )
        else None
    )

    package_content = {
        "experiment_id": experiment_id,
        "important": important,
        "input": components["input"],
        "version": components["version"],
        "config": components["config"],
        "result": components["result"],
        "verifier_record": {
            field: verifier_record.get(field)
            for field in VERIFIER_RECORD_FIELDS
        },
    }
    package_sha256 = _sha256_json(package_content)

    errors = list(dict.fromkeys(errors))
    package_complete = bool(
        not errors
        and all(
            field in supplied_record
            for field in REQUIRED_EXPERIMENT_FIELDS
        )
        and verifier_record["complete"] is True
    )
    reproducible = package_complete
    important_requirement_satisfied = bool(
        important is False
        or (important is True and reproducible)
    )

    if important is True and reproducible:
        status = "IMPORTANT_EXPERIMENT_REPRODUCIBLE"
    elif important is True:
        status = "IMPORTANT_EXPERIMENT_NOT_REPRODUCIBLE"
    elif important is False and reproducible:
        status = (
            "NON_IMPORTANT_EXPERIMENT_REPRODUCIBILITY_AVAILABLE"
        )
    elif important is False:
        status = (
            "NON_IMPORTANT_EXPERIMENT_REPRODUCIBILITY_NOT_REQUIRED"
        )
    else:
        status = "EXPERIMENT_IMPORTANCE_UNRESOLVED"

    record: Dict[str, Any] = {
        "sequence": sequence,
        "record_id": f"DNA-27-EXPERIMENT-{sequence:04d}",
        "input_index": input_index,
        "experiment_id": experiment_id,
        "important": important,
        "input": components["input"],
        "version": components["version"],
        "config": components["config"],
        "result": components["result"],
        "verifier_record": verifier_record,
        "component_sha256": component_sha256,
        "package_sha256": package_sha256,
        "observability_source": (
            _latest_observability_source(observability)
        ),
        "package_complete": package_complete,
        "reproducible": reproducible,
        "important_requirement_satisfied": (
            important_requirement_satisfied
        ),
        "actual_replay_executed_by_dna27": False,
        "result_reproduced_by_dna27": False,
        "experiment_executed_by_dna27": False,
        "truth_established_by_dna27": False,
        "knowledge_promoted_by_dna27": False,
        "external_action_executed": False,
        "errors": errors,
        "status": status,
        "previous_chain_sha256": previous_chain_sha256,
    }
    record["record_sha256"] = _sha256_json(
        _record_content(record)
    )
    record["chain_sha256"] = _sha256_json(
        {
            "previous_chain_sha256": previous_chain_sha256,
            "record_sha256": record["record_sha256"],
        }
    )
    record["integrity_verifiable"] = (
        _verify_record_integrity(
            record,
            previous_chain_sha256,
        )
    )
    return record


def _evaluate_experiments(
    supplied: Any,
    registry: Dict[str, Any],
    *,
    verification_wall: Dict[str, Any],
    observability: Dict[str, Any],
) -> Dict[str, Any]:
    if supplied is None:
        experiments: List[Any] = []
    elif not isinstance(supplied, list):
        raise TypeError(
            "context['reproducibility_experiments'] "
            "must be a list"
        )
    else:
        experiments = supplied

    supplied_ids = [
        item.get("experiment_id")
        for item in experiments
        if isinstance(item, dict)
        and _non_empty_text(item.get("experiment_id"))
    ]
    if len(supplied_ids) != len(set(supplied_ids)):
        raise ValueError(
            "DNA-27_DUPLICATE_EXPERIMENT_ID_IN_BATCH"
        )

    existing_ids = {
        record.get("experiment_id")
        for record in registry["experiments"]
        if isinstance(record, dict)
        and _non_empty_text(record.get("experiment_id"))
    }
    overlap = existing_ids.intersection(supplied_ids)
    if overlap:
        raise ValueError(
            "DNA-27_EXPERIMENT_ID_ALREADY_RECORDED:"
            + ",".join(sorted(overlap))
        )

    previous_chain_sha256 = (
        registry["experiments"][-1]["chain_sha256"]
        if registry["experiments"]
        else None
    )
    start_sequence = len(registry["experiments"]) + 1
    records: List[Dict[str, Any]] = []

    for input_index, experiment in enumerate(
        experiments,
        start=1,
    ):
        record = _normalize_experiment(
            experiment,
            input_index=input_index,
            sequence=start_sequence + input_index - 1,
            previous_chain_sha256=previous_chain_sha256,
            verification_wall=verification_wall,
            observability=observability,
        )
        records.append(record)
        previous_chain_sha256 = record["chain_sha256"]

    registry["experiments"].extend(deepcopy(records))
    registry_chain_valid = _verify_registry_chain(registry)
    if not registry_chain_valid:
        raise RuntimeError(
            "DNA-27_REPRODUCIBILITY_CHAIN_INVALID_AFTER_APPEND"
        )

    important_records = [
        record
        for record in records
        if record["important"] is True
    ]
    reproducible_important = [
        record
        for record in important_records
        if record["reproducible"] is True
    ]
    nonreproducible_important = [
        record
        for record in important_records
        if record["reproducible"] is False
    ]
    incomplete_count = sum(
        1
        for record in records
        if record["package_complete"] is False
    )
    all_important_reproducible = bool(
        important_records
        and len(reproducible_important)
        == len(important_records)
    )

    if not records:
        status = "NO_EXPERIMENTS_SUPPLIED"
    elif nonreproducible_important:
        status = "IMPORTANT_EXPERIMENT_REPRODUCIBILITY_FAILED"
    elif all_important_reproducible:
        status = "ALL_IMPORTANT_EXPERIMENTS_REPRODUCIBLE"
    else:
        status = "NO_IMPORTANT_EXPERIMENT_REQUIREMENT_TRIGGERED"

    batch_sequence = len(registry["batches"]) + 1
    batch = {
        "sequence": batch_sequence,
        "batch_id": f"DNA-27-BATCH-{batch_sequence:04d}",
        "record_ids": [
            record["record_id"]
            for record in records
        ],
        "experiment_count": len(records),
        "important_experiment_count": len(important_records),
        "reproducible_important_count": len(
            reproducible_important
        ),
        "nonreproducible_important_count": len(
            nonreproducible_important
        ),
        "incomplete_count": incomplete_count,
        "registry_chain_valid": registry_chain_valid,
        "all_important_experiments_reproducible": (
            all_important_reproducible
        ),
        "actual_replay_executed_by_dna27": False,
        "result_reproduced_by_dna27": False,
        "external_action_executed": False,
        "status": status,
    }
    registry["batches"].append(deepcopy(batch))

    return {
        "records": records,
        "batch": batch,
    }


def dna27_reproducibility(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Build deterministic replay packages for supplied important experiments
    from input, version, config, result, and a DNA-09-bound verifier record.

    DNA-27 does not execute or replay an experiment, reproduce a result,
    invoke a verifier/model, start Memory/Learning Runtime, establish truth,
    promote knowledge, act externally, or modify Canon.
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
    trace.append("DNA-27")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    (
        state,
        verification_wall,
        observability,
    ) = _validate_dependencies(context)
    registry = _install_reproducibility_state(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-27",
            "operation": (
                "REPRODUCIBILITY_CONTRACT_ESTABLISHED"
            ),
            "canonical_sha256": canonical_sha256,
            "reproducibility_schema": (
                REPRODUCIBILITY_SCHEMA
            ),
            "required_components": [
                "input",
                "version",
                "config",
                "result",
                "verifier_record",
            ],
            "actual_replay_executed": False,
            "external_action_executed": False,
        }
    )

    evaluation = _evaluate_experiments(
        context.get("reproducibility_experiments"),
        registry,
        verification_wall=verification_wall,
        observability=observability,
    )
    batch = evaluation["batch"]

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-27",
            "operation": (
                "IMPORTANT_EXPERIMENT_REPRODUCIBILITY_EVALUATED"
            ),
            "canonical_sha256": canonical_sha256,
            "batch_id": batch["batch_id"],
            "experiment_count": batch["experiment_count"],
            "important_experiment_count": (
                batch["important_experiment_count"]
            ),
            "reproducible_important_count": (
                batch["reproducible_important_count"]
            ),
            "nonreproducible_important_count": (
                batch[
                    "nonreproducible_important_count"
                ]
            ),
            "registry_chain_valid": (
                batch["registry_chain_valid"]
            ),
            "all_important_experiments_reproducible": (
                batch[
                    "all_important_experiments_reproducible"
                ]
            ),
            "actual_replay_executed": False,
            "external_action_executed": False,
        }
    )

    outputs["DNA-27"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "reproducibility_contract": deepcopy(
            REPRODUCIBILITY_CONTRACT
        ),
        "evaluation": deepcopy(evaluation),
        "experiment_count": batch["experiment_count"],
        "important_experiment_count": (
            batch["important_experiment_count"]
        ),
        "reproducible_important_count": (
            batch["reproducible_important_count"]
        ),
        "nonreproducible_important_count": (
            batch["nonreproducible_important_count"]
        ),
        "registry_chain_valid": (
            batch["registry_chain_valid"]
        ),
        "all_important_experiments_reproducible": (
            batch[
                "all_important_experiments_reproducible"
            ]
        ),
        "actual_replay_executed": False,
        "result_reproduced": False,
        "experiment_executed": False,
        "external_persistence_started": False,
        "memory_runtime_started": False,
        "learning_runtime_started": False,
        "truth_established": False,
        "knowledge_promoted": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna27(core54: Core54Like) -> None:
    core = core54.get("DNA-27")
    assert_exact_canon(core)
    core54.bind(
        "DNA-27",
        dna27_reproducibility,
    )


def _through_dna26(core54: Core54Like) -> Dict[str, Any]:
    from SIGMA_DNA_26_OBSERVABILITY import (
        _through_dna25,
        _valid_artifact,
    )

    through_dna25 = _through_dna25(core54)
    through_dna25["observability_artifacts"] = [
        _valid_artifact(through_dna25)
    ]
    return core54.get("DNA-26").activate(
        through_dna25
    )


def _valid_experiment(
    through_dna26: Dict[str, Any],
    *,
    experiment_id: str = "DNA27-EXPERIMENT-01",
    important: bool = True,
) -> Dict[str, Any]:
    verification = through_dna26["cognitive_state"][
        "independent_verification_wall"
    ]["evaluations"][-1]
    verification_record = verification[
        "verification_record"
    ]

    return {
        "experiment_id": experiment_id,
        "important": important,
        "input": {
            "source": "DNA-08_LEARNING_WORLD_EVENT",
            "event": deepcopy(
                through_dna26["cognitive_state"][
                    "learning_world"
                ]["events"][-1]
            ),
        },
        "version": {
            "experiment": "1.0.0",
            "core": "DNA-27",
            "schema": REPRODUCIBILITY_SCHEMA,
        },
        "config": {
            "mode": "DETERMINISTIC_REPLAY_PACKAGE",
            "seed": 174,
            "canonical_json": True,
        },
        "result": deepcopy(verification["candidate"]),
        "verifier_record": {
            "evaluation_id": verification[
                "evaluation_id"
            ],
            "verifier_id": verification_record[
                "verifier_id"
            ],
            "independent": verification[
                "independent_verifier"
            ],
            "passed": verification[
                "verification_passed"
            ],
            "source_sha256": _sha256_json(verification),
        },
    }


def self_check_dna27(
    core54: Core54Like,
    *,
    verify_canon_file: bool = True,
) -> Dict[str, Any]:
    canon_before = (
        _sha256_file(DNA_JSON)
        if verify_canon_file
        else None
    )

    for index in range(1, 27):
        required_id = f"DNA-{index:02d}"
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna27_core = core54.get("DNA-27")
    assert_exact_canon(dna27_core)
    bind_dna27(core54)

    through_dna26 = _through_dna26(core54)
    through_dna26_snapshot = deepcopy(through_dna26)

    state_before = through_dna26["cognitive_state"]
    pre_verification_wall = deepcopy(
        state_before["independent_verification_wall"]
    )
    pre_observability = deepcopy(
        state_before["observability"]
    )
    pre_provenance_count = len(
        state_before["provenance"]
    )

    valid_experiment = _valid_experiment(through_dna26)
    valid_input = deepcopy(through_dna26)
    valid_input["reproducibility_experiments"] = [
        valid_experiment
    ]
    result = dna27_core.activate(valid_input)

    assert through_dna26 == through_dna26_snapshot
    assert result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 28)
    ]

    dna27 = result["core54_outputs"]["DNA-27"]
    assert dna27["canonical_gene"] == CANON_DNA27
    assert dna27["reproducibility_contract"] == (
        REPRODUCIBILITY_CONTRACT
    )
    assert dna27["experiment_count"] == 1
    assert dna27["important_experiment_count"] == 1
    assert dna27["reproducible_important_count"] == 1
    assert dna27["nonreproducible_important_count"] == 0
    assert dna27["registry_chain_valid"] is True
    assert (
        dna27["all_important_experiments_reproducible"]
        is True
    )
    assert dna27["actual_replay_executed"] is False
    assert dna27["result_reproduced"] is False
    assert dna27["experiment_executed"] is False
    assert dna27["external_persistence_started"] is False
    assert dna27["memory_runtime_started"] is False
    assert dna27["learning_runtime_started"] is False
    assert dna27["truth_established"] is False
    assert dna27["knowledge_promoted"] is False
    assert dna27["external_action_executed"] is False
    assert dna27["status"] == "CANON_ALIGNED"

    evaluation = dna27["evaluation"]
    record = evaluation["records"][0]
    batch = evaluation["batch"]

    assert record["record_id"] == (
        "DNA-27-EXPERIMENT-0001"
    )
    assert record["experiment_id"] == (
        "DNA27-EXPERIMENT-01"
    )
    assert record["important"] is True
    assert record["input"] == valid_experiment["input"]
    assert record["version"] == valid_experiment["version"]
    assert record["config"] == valid_experiment["config"]
    assert record["result"] == valid_experiment["result"]
    assert record["verifier_record"]["evaluation_found"] is True
    assert record["verifier_record"]["source_bound"] is True
    assert record["verifier_record"]["result_bound"] is True
    assert record["verifier_record"]["complete"] is True
    assert all(
        _is_sha256(value)
        for value in record["component_sha256"].values()
    )
    assert _is_sha256(record["package_sha256"])
    assert record["observability_source"]["source_bound"] is True
    assert record["package_complete"] is True
    assert record["reproducible"] is True
    assert record["important_requirement_satisfied"] is True
    assert record["actual_replay_executed_by_dna27"] is False
    assert record["result_reproduced_by_dna27"] is False
    assert record["experiment_executed_by_dna27"] is False
    assert record["truth_established_by_dna27"] is False
    assert record["knowledge_promoted_by_dna27"] is False
    assert record["errors"] == []
    assert record["status"] == (
        "IMPORTANT_EXPERIMENT_REPRODUCIBLE"
    )
    assert record["integrity_verifiable"] is True
    assert _verify_record_integrity(record, None) is True

    expected_package_sha256 = _sha256_json(
        {
            "experiment_id": valid_experiment[
                "experiment_id"
            ],
            "important": True,
            "input": valid_experiment["input"],
            "version": valid_experiment["version"],
            "config": valid_experiment["config"],
            "result": valid_experiment["result"],
            "verifier_record": valid_experiment[
                "verifier_record"
            ],
        }
    )
    assert record["package_sha256"] == (
        expected_package_sha256
    )

    assert batch["batch_id"] == "DNA-27-BATCH-0001"
    assert batch["experiment_count"] == 1
    assert batch["important_experiment_count"] == 1
    assert batch["reproducible_important_count"] == 1
    assert batch["nonreproducible_important_count"] == 0
    assert batch["incomplete_count"] == 0
    assert batch["registry_chain_valid"] is True
    assert (
        batch["all_important_experiments_reproducible"]
        is True
    )
    assert batch["status"] == (
        "ALL_IMPORTANT_EXPERIMENTS_REPRODUCIBLE"
    )

    state = result["cognitive_state"]
    registry = state["reproducibility"]
    assert registry["contract"] == REPRODUCIBILITY_CONTRACT
    assert registry["experiments"] == [record]
    assert registry["batches"] == [batch]
    assert _verify_registry_chain(registry) is True
    assert len(state["provenance"]) == (
        pre_provenance_count + 2
    )

    contract_event = state["provenance"][-2]
    assert contract_event["core_id"] == "DNA-27"
    assert contract_event["operation"] == (
        "REPRODUCIBILITY_CONTRACT_ESTABLISHED"
    )
    assert contract_event["required_components"] == [
        "input",
        "version",
        "config",
        "result",
        "verifier_record",
    ]
    assert contract_event["actual_replay_executed"] is False
    assert contract_event["external_action_executed"] is False

    evaluation_event = state["provenance"][-1]
    assert evaluation_event["core_id"] == "DNA-27"
    assert evaluation_event["operation"] == (
        "IMPORTANT_EXPERIMENT_REPRODUCIBILITY_EVALUATED"
    )
    assert evaluation_event["experiment_count"] == 1
    assert evaluation_event["important_experiment_count"] == 1
    assert evaluation_event["reproducible_important_count"] == 1
    assert evaluation_event[
        "nonreproducible_important_count"
    ] == 0
    assert evaluation_event["registry_chain_valid"] is True
    assert evaluation_event[
        "all_important_experiments_reproducible"
    ] is True

    # DNA-27 must not mutate DNA-09 or DNA-26 source state.
    assert state["independent_verification_wall"] == (
        pre_verification_wall
    )
    assert state["observability"] == pre_observability

    # Missing config makes an important experiment non-reproducible.
    missing_config_input = deepcopy(through_dna26)
    missing_config_experiment = _valid_experiment(
        through_dna26,
        experiment_id="DNA27-MISSING-CONFIG",
    )
    missing_config_experiment.pop("config")
    missing_config_input["reproducibility_experiments"] = [
        missing_config_experiment
    ]
    missing_config = dna27_core.activate(
        missing_config_input
    )
    missing_record = missing_config[
        "core54_outputs"
    ]["DNA-27"]["evaluation"]["records"][0]
    assert missing_record["reproducible"] is False
    assert (
        missing_record["important_requirement_satisfied"]
        is False
    )
    assert "REPRODUCIBILITY_FIELDS_MISSING" in (
        missing_record["errors"]
    )
    assert missing_record["status"] == (
        "IMPORTANT_EXPERIMENT_NOT_REPRODUCIBLE"
    )

    # Result must bind to the exact DNA-09 verifier candidate.
    wrong_result_input = deepcopy(through_dna26)
    wrong_result_experiment = _valid_experiment(
        through_dna26,
        experiment_id="DNA27-WRONG-RESULT",
    )
    wrong_result_experiment["result"] = {
        "different": "result"
    }
    wrong_result_input["reproducibility_experiments"] = [
        wrong_result_experiment
    ]
    wrong_result = dna27_core.activate(wrong_result_input)
    wrong_result_record = wrong_result[
        "core54_outputs"
    ]["DNA-27"]["evaluation"]["records"][0]
    assert wrong_result_record["reproducible"] is False
    assert (
        "RESULT_NOT_BOUND_TO_VERIFIER_CANDIDATE"
        in wrong_result_record["errors"]
    )

    # Verifier record must bind exactly to DNA-09.
    bad_verifier_input = deepcopy(through_dna26)
    bad_verifier_experiment = _valid_experiment(
        through_dna26,
        experiment_id="DNA27-BAD-VERIFIER",
    )
    bad_verifier_experiment["verifier_record"][
        "source_sha256"
    ] = "0" * 64
    bad_verifier_input["reproducibility_experiments"] = [
        bad_verifier_experiment
    ]
    bad_verifier = dna27_core.activate(
        bad_verifier_input
    )
    bad_verifier_record = bad_verifier[
        "core54_outputs"
    ]["DNA-27"]["evaluation"]["records"][0]
    assert bad_verifier_record["reproducible"] is False
    assert "VERIFIER_RECORD_SOURCE_MISMATCH" in (
        bad_verifier_record["errors"]
    )

    # Non-important incomplete experiment does not violate the Canon rule.
    nonimportant_input = deepcopy(through_dna26)
    nonimportant_input["reproducibility_experiments"] = [
        {
            "experiment_id": "DNA27-NONIMPORTANT",
            "important": False,
        }
    ]
    nonimportant = dna27_core.activate(nonimportant_input)
    nonimportant_record = nonimportant[
        "core54_outputs"
    ]["DNA-27"]["evaluation"]["records"][0]
    assert nonimportant_record["reproducible"] is False
    assert (
        nonimportant_record["important_requirement_satisfied"]
        is True
    )
    assert nonimportant_record["status"] == (
        "NON_IMPORTANT_EXPERIMENT_REPRODUCIBILITY_NOT_REQUIRED"
    )

    # Duplicate experiment identifiers must be rejected.
    duplicate_input = deepcopy(through_dna26)
    duplicate_experiment = _valid_experiment(
        through_dna26,
        experiment_id="DNA27-DUPLICATE",
    )
    duplicate_input["reproducibility_experiments"] = [
        deepcopy(duplicate_experiment),
        deepcopy(duplicate_experiment),
    ]
    try:
        dna27_core.activate(duplicate_input)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-27_DUPLICATE_EXPERIMENT_ID_IN_BATCH"
        )
    else:
        raise AssertionError(
            "DNA-27_ACCEPTED_DUPLICATE_EXPERIMENT_ID"
        )

    # Tampering after storage must be detected.
    tampered = deepcopy(record)
    tampered["config"]["seed"] = 999
    assert _verify_record_integrity(tampered, None) is False

    tampered_registry_input = deepcopy(result)
    tampered_registry_input[
        "cognitive_state"
    ]["reproducibility"]["experiments"][0][
        "config"
    ]["seed"] = 999
    tampered_registry_input["reproducibility_experiments"] = []
    try:
        dna27_core.activate(tampered_registry_input)
    except RuntimeError as exc:
        assert str(exc) == (
            "DNA-27_EXISTING_REPRODUCIBILITY_CHAIN_INVALID"
        )
    else:
        raise AssertionError(
            "DNA-27_ACCEPTED_TAMPERED_REPRODUCIBILITY_CHAIN"
        )

    # Reject provisional root-marker behavior as the official contract.
    assert "reproducible" not in result
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
        "core_id": "DNA-27",
        "canon_mapping": "PASS",
        "input_capture": "PASS",
        "version_capture": "PASS",
        "config_capture": "PASS",
        "result_capture": "PASS",
        "verifier_record_binding": "PASS",
        "important_experiment_rule": "PASS",
        "deterministic_package_hash": "PASS",
        "append_chain": "PASS",
        "tamper_detection": "PASS",
        "actual_replay_executed": False,
        "result_reproduced": False,
        "experiment_executed": False,
        "external_persistence_started": False,
        "memory_runtime_used": False,
        "learning_runtime_used": False,
        "truth_established": False,
        "knowledge_promoted": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-28"
            if verify_canon_file
            else "RUN_ON_CANONICAL_E_DRIVE"
        ),
    }


def _load_prior_modules() -> Dict[int, Any]:
    return {
        index: importlib.import_module(module_name)
        for index, module_name in PRIOR_GENE_MODULES.items()
    }


def main() -> int:
    required_gene_files = [
        GENES_ROOT / f"{module_name}.py"
        for module_name in PRIOR_GENE_MODULES.values()
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-27_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = _load_prior_modules()
    except Exception as exc:
        print("DNA-27_FAIL: IMPORT_ERROR")
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

        for index in range(1, 27):
            checker = getattr(
                modules[index],
                f"self_check_dna{index:02d}",
            )
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(
                    f"DNA-{index:02d}_NOT_PASS"
                )

        report = self_check_dna27(
            core54,
            verify_canon_file=True,
        )

        bound_ids = [
            core.core_id
            for core in core54.cores
            if core.state.behavior_bound
        ]
        if bound_ids != [
            f"DNA-{index:02d}"
            for index in range(1, 28)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-27_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-27_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_27_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("INPUT_CAPTURE:", report["input_capture"])
    print("VERSION_CAPTURE:", report["version_capture"])
    print("CONFIG_CAPTURE:", report["config_capture"])
    print("RESULT_CAPTURE:", report["result_capture"])
    print(
        "VERIFIER_RECORD_BINDING:",
        report["verifier_record_binding"],
    )
    print(
        "IMPORTANT_EXPERIMENT_RULE:",
        report["important_experiment_rule"],
    )
    print(
        "DETERMINISTIC_PACKAGE_HASH:",
        report["deterministic_package_hash"],
    )
    print("APPEND_CHAIN:", report["append_chain"])
    print("TAMPER_DETECTION:", report["tamper_detection"])
    print(
        "ACTUAL_REPLAY_EXECUTED:",
        report["actual_replay_executed"],
    )
    print(
        "RESULT_REPRODUCED:",
        report["result_reproduced"],
    )
    print(
        "EXPERIMENT_EXECUTED:",
        report["experiment_executed"],
    )
    print(
        "EXTERNAL_PERSISTENCE_STARTED:",
        report["external_persistence_started"],
    )
    print(
        "MEMORY_RUNTIME_USED:",
        report["memory_runtime_used"],
    )
    print(
        "LEARNING_RUNTIME_USED:",
        report["learning_runtime_used"],
    )
    print("TRUTH_ESTABLISHED:", report["truth_established"])
    print("KNOWLEDGE_PROMOTED:", report["knowledge_promoted"])
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 27/54")
    print("NEXT_AUTHORIZED: DNA-28")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
