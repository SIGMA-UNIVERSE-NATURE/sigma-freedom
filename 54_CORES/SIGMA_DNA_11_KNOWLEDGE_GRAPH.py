#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
SIGMA CORE DNA 54 — DNA-11: KNOWLEDGE GRAPH
PHASE_LOCK = CORE_DNA_54_ONLY

CANON SOURCE:
E:\SIGMA\CORE\DNA_CANON\SIGMA_CORE_DNA_54\sigma_dna_54.json

SAVE AS:
E:\SIGMA\RUNTIME\CORE54\GENES\SIGMA_DNA_11_KNOWLEDGE_GRAPH.py
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

CANON_DNA11: Dict[str, str] = {
    "id": "DNA-11",
    "name": "Knowledge Graph",
    "purpose": (
        "Tri thức phải có quan hệ, provenance, evidence, confidence, "
        "contradictions và khả năng sửa đổi."
    ),
    "system": "truth",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
MEMORY_GENOME_SCHEMA = "SIGMA_MEMORY_GENOME_V1"
KNOWLEDGE_GRAPH_SCHEMA = "SIGMA_KNOWLEDGE_GRAPH_V1"

MEMORY_CLASSES = [
    "working",
    "episodic",
    "hypothesis",
    "verified",
    "rejected",
    "strategy",
]

KNOWLEDGE_SOURCE_PRIORITY = [
    "verified",
    "hypothesis",
    "rejected",
]

REQUIRED_NODE_FIELDS = [
    "node_id",
    "claim",
    "knowledge_status",
    "relations",
    "provenance",
    "evidence",
    "confidence",
    "contradictions",
    "revision",
    "node_sha256",
]

KNOWLEDGE_GRAPH_CONTRACT: Dict[str, Any] = {
    "schema": KNOWLEDGE_GRAPH_SCHEMA,
    "required_node_fields": deepcopy(REQUIRED_NODE_FIELDS),
    "relationships_required": True,
    "provenance_required": True,
    "evidence_required": True,
    "confidence_required": True,
    "contradictions_required": True,
    "modifiable_required": True,
    "source_memory_priority": deepcopy(KNOWLEDGE_SOURCE_PRIORITY),
    "storage_scope": "CURRENT_STRUCTURED_STATE",
    "persistent_knowledge_runtime_started": False,
    "persistent_memory_runtime_started": False,
    "knowledge_promotion_authority": False,
    "external_graph_write": False,
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
    if actual != CANON_DNA11:
        raise RuntimeError(
            "DNA-11_CANON_MISMATCH:"
            + json.dumps(
                {"expected": CANON_DNA11, "actual": actual},
                ensure_ascii=False,
                sort_keys=True,
            )
        )


def _validate_dependencies(
    context: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError(
            "DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED"
        )

    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError(
            "DNA-11_UNIFIED_STATE_SCHEMA_MISMATCH:"
            f"{state.get('schema')!r}"
        )

    if not isinstance(state.get("provenance"), list):
        raise TypeError(
            "context['cognitive_state']['provenance'] must be a list"
        )

    genome = state.get("memory_genome")
    if not isinstance(genome, dict):
        raise RuntimeError("DNA-10_MEMORY_GENOME_REQUIRED")

    genome_contract = genome.get("contract")
    if not isinstance(genome_contract, dict):
        raise RuntimeError(
            "DNA-10_MEMORY_GENOME_CONTRACT_REQUIRED"
        )

    if genome_contract.get("schema") != MEMORY_GENOME_SCHEMA:
        raise ValueError(
            "DNA-11_MEMORY_GENOME_SCHEMA_MISMATCH:"
            f"{genome_contract.get('schema')!r}"
        )

    segments = genome.get("segments")
    if not isinstance(segments, dict):
        raise TypeError(
            "memory_genome['segments'] must be a dict"
        )

    if list(segments.keys()) != MEMORY_CLASSES:
        raise ValueError(
            "DNA-11_EXACT_MEMORY_CLASS_ORDER_REQUIRED"
        )

    for memory_class in MEMORY_CLASSES:
        if not isinstance(segments[memory_class], list):
            raise TypeError(
                "memory_genome segment must be a list:"
                f"{memory_class}"
            )

    outputs = context.get("core54_outputs")
    if not isinstance(outputs, dict):
        raise RuntimeError("DNA-10_OUTPUT_REQUIRED")

    dna10_output = outputs.get("DNA-10")
    if not isinstance(dna10_output, dict):
        raise RuntimeError("DNA-10_OUTPUT_REQUIRED")

    return state, genome, dna10_output


def _install_knowledge_graph(
    state: Dict[str, Any],
) -> Dict[str, Any]:
    existing = state.get("knowledge_graph")

    expected = {
        "contract": deepcopy(KNOWLEDGE_GRAPH_CONTRACT),
        "nodes": {},
        "edges": [],
        "revision_events": [],
    }

    if existing is None:
        state["knowledge_graph"] = expected
        return state["knowledge_graph"]

    if not isinstance(existing, dict):
        raise TypeError(
            "cognitive_state['knowledge_graph'] must be a dict"
        )

    if existing.get("contract") != KNOWLEDGE_GRAPH_CONTRACT:
        raise ValueError(
            "DNA-11_KNOWLEDGE_GRAPH_CONTRACT_CONFLICT"
        )

    if not isinstance(existing.get("nodes"), dict):
        raise TypeError("knowledge_graph['nodes'] must be a dict")

    if not isinstance(existing.get("edges"), list):
        raise TypeError("knowledge_graph['edges'] must be a list")

    if not isinstance(existing.get("revision_events"), list):
        raise TypeError(
            "knowledge_graph['revision_events'] must be a list"
        )

    return existing


def _select_source_record(
    genome: Dict[str, Any],
) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    for memory_class in KNOWLEDGE_SOURCE_PRIORITY:
        segment = genome["segments"][memory_class]
        if not segment:
            continue

        record = segment[-1]
        if not isinstance(record, dict):
            raise TypeError(
                "DNA-10 knowledge memory record must be a dict"
            )

        if record.get("memory_class") != memory_class:
            raise ValueError(
                "DNA-11_MEMORY_CLASS_RECORD_MISMATCH"
            )

        return memory_class, record

    return None, None


def _validate_confidence_value(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(
        value,
        (int, float),
    ):
        raise TypeError(
            "knowledge confidence must be a number in [0, 1]"
        )

    normalized = float(value)
    if not 0.0 <= normalized <= 1.0:
        raise ValueError(
            "DNA-11_CONFIDENCE_MUST_BE_BETWEEN_0_AND_1"
        )
    return normalized


def _confidence_record(
    context: Dict[str, Any],
    memory_class: str,
    *,
    field_name: str = "knowledge_confidence",
) -> Dict[str, Any]:
    if field_name in context:
        value = _validate_confidence_value(
            context[field_name]
        )
        return {
            "value": value,
            "status": "EXPLICIT",
            "basis": [
                "CALLER_SUPPLIED_CONFIDENCE",
                f"SOURCE_MEMORY_CLASS:{memory_class}",
            ],
            "calibrated": False,
        }

    return {
        "value": None,
        "status": "UNRESOLVED",
        "basis": [
            f"SOURCE_MEMORY_CLASS:{memory_class}",
            "NO_NUMERIC_CONFIDENCE_SUPPLIED",
        ],
        "calibrated": False,
    }


def _normalize_list_field(
    context: Dict[str, Any],
    field_name: str,
) -> List[Any]:
    value = context.get(field_name, [])
    if not isinstance(value, list):
        raise TypeError(
            f"context['{field_name}'] must be a list"
        )
    return deepcopy(value)


def _normalize_relations(
    value: Any,
) -> List[Dict[str, Any]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise TypeError("knowledge relations must be a list")

    normalized: List[Dict[str, Any]] = []
    for index, item in enumerate(value, start=1):
        if not isinstance(item, dict):
            raise TypeError(
                "each knowledge relation must be a dict"
            )

        relation = item.get("relation")
        target_id = item.get("target_id")
        target_type = item.get("target_type", "KNOWLEDGE")

        if not isinstance(relation, str) or not relation.strip():
            raise ValueError(
                f"DNA-11_RELATION_{index}_NAME_REQUIRED"
            )
        if not isinstance(target_id, str) or not target_id.strip():
            raise ValueError(
                f"DNA-11_RELATION_{index}_TARGET_REQUIRED"
            )
        if not isinstance(target_type, str) or not target_type.strip():
            raise ValueError(
                f"DNA-11_RELATION_{index}_TARGET_TYPE_REQUIRED"
            )

        normalized.append(
            {
                "relation": relation.strip().upper(),
                "target_id": target_id.strip(),
                "target_type": target_type.strip().upper(),
                "source": "CALLER_SUPPLIED_RELATION",
            }
        )

    return normalized


def _extract_claim(
    context: Dict[str, Any],
    record: Dict[str, Any],
) -> Any:
    if "knowledge_claim" in context:
        supplied = context["knowledge_claim"]
        if supplied is None:
            raise ValueError(
                "DNA-11_KNOWLEDGE_CLAIM_CANNOT_BE_NONE"
            )
        return deepcopy(supplied)

    payload = record.get("payload")
    if isinstance(payload, dict):
        candidate = payload.get("candidate")
        if isinstance(candidate, dict):
            experience = candidate.get("experience")
            if isinstance(experience, dict):
                if "candidate_learning" in experience:
                    return deepcopy(
                        experience["candidate_learning"]
                    )
                return deepcopy(experience)
            if experience is not None:
                return deepcopy(experience)

        if "claim" in payload:
            return deepcopy(payload["claim"])

    return deepcopy(payload)


def _extract_provenance(
    memory_class: str,
    record: Dict[str, Any],
) -> List[Dict[str, Any]]:
    provenance: List[Dict[str, Any]] = [
        {
            "origin_type": "MEMORY_GENOME_RECORD",
            "origin_core_id": "DNA-10",
            "memory_class": memory_class,
            "record_id": record.get("record_id"),
            "record_sha256": record.get("record_sha256"),
            "source": record.get("source"),
        }
    ]

    payload = record.get("payload")
    if isinstance(payload, dict):
        candidate = payload.get("candidate")
        if isinstance(candidate, dict):
            provenance.append(
                {
                    "origin_type": "KNOWLEDGE_CANDIDATE",
                    "origin_core_id": candidate.get(
                        "source_core_id"
                    ),
                    "source_event_id": candidate.get(
                        "source_event_id"
                    ),
                    "candidate_sha256": candidate.get(
                        "candidate_sha256"
                    ),
                    "interaction_sha256": candidate.get(
                        "interaction_sha256"
                    ),
                }
            )

        evaluation = payload.get("evaluation")
        if isinstance(evaluation, dict):
            verification_record = evaluation.get(
                "verification_record"
            )
            provenance.append(
                {
                    "origin_type": "VERIFICATION_EVALUATION",
                    "origin_core_id": "DNA-09",
                    "evaluation_id": evaluation.get(
                        "evaluation_id"
                    ),
                    "verifier_id": (
                        verification_record.get("verifier_id")
                        if isinstance(
                            verification_record,
                            dict,
                        )
                        else None
                    ),
                    "verification_passed": evaluation.get(
                        "verification_passed"
                    ),
                    "candidate_bound": evaluation.get(
                        "candidate_bound"
                    ),
                }
            )

    return provenance


def _append_unique_evidence(
    target: List[Any],
    value: Any,
) -> None:
    digest = _sha256_json(value)
    for existing in target:
        if _sha256_json(existing) == digest:
            return
    target.append(deepcopy(value))


def _extract_evidence(
    context: Dict[str, Any],
    record: Dict[str, Any],
) -> List[Any]:
    evidence: List[Any] = []

    _append_unique_evidence(
        evidence,
        {
            "type": "MEMORY_RECORD_REFERENCE",
            "record_id": record.get("record_id"),
            "record_sha256": record.get("record_sha256"),
        },
    )

    payload = record.get("payload")
    if isinstance(payload, dict):
        candidate = payload.get("candidate")
        if isinstance(candidate, dict):
            _append_unique_evidence(
                evidence,
                {
                    "type": "EXPERIENTIAL_INTERACTION",
                    "source_event_id": candidate.get(
                        "source_event_id"
                    ),
                    "interaction_sha256": candidate.get(
                        "interaction_sha256"
                    ),
                    "experience": deepcopy(
                        candidate.get("experience")
                    ),
                },
            )

        evaluation = payload.get("evaluation")
        if isinstance(evaluation, dict):
            verification_record = evaluation.get(
                "verification_record"
            )
            if isinstance(verification_record, dict):
                verifier_evidence = verification_record.get(
                    "evidence",
                    [],
                )
                if not isinstance(verifier_evidence, list):
                    raise TypeError(
                        "verification evidence must be a list"
                    )
                for item in verifier_evidence:
                    _append_unique_evidence(
                        evidence,
                        {
                            "type": "INDEPENDENT_VERIFIER_EVIDENCE",
                            "verifier_id": verification_record.get(
                                "verifier_id"
                            ),
                            "method": verification_record.get(
                                "method"
                            ),
                            "scope": verification_record.get(
                                "scope"
                            ),
                            "value": deepcopy(item),
                        },
                    )

            rejection_reasons = evaluation.get(
                "rejection_reasons",
                [],
            )
            if not isinstance(rejection_reasons, list):
                raise TypeError(
                    "evaluation rejection_reasons must be a list"
                )
            if rejection_reasons:
                _append_unique_evidence(
                    evidence,
                    {
                        "type": "VERIFICATION_REJECTION_REASONS",
                        "value": deepcopy(rejection_reasons),
                    },
                )

    supplied = _normalize_list_field(
        context,
        "knowledge_evidence",
    )
    for item in supplied:
        _append_unique_evidence(evidence, item)

    return evidence


def _base_relations(
    record: Dict[str, Any],
) -> List[Dict[str, Any]]:
    relations: List[Dict[str, Any]] = [
        {
            "relation": "DERIVED_FROM",
            "target_id": str(record.get("record_id")),
            "target_type": "MEMORY_RECORD",
            "source": "DNA-10_MEMORY_GENOME",
        }
    ]

    payload = record.get("payload")
    if isinstance(payload, dict):
        candidate = payload.get("candidate")
        if isinstance(candidate, dict) and candidate.get(
            "source_event_id"
        ):
            relations.append(
                {
                    "relation": "SUPPORTED_BY",
                    "target_id": str(
                        candidate["source_event_id"]
                    ),
                    "target_type": "EXPERIENTIAL_EVENT",
                    "source": "DNA-08_LEARNING_WORLD",
                }
            )

        evaluation = payload.get("evaluation")
        if isinstance(evaluation, dict) and evaluation.get(
            "evaluation_id"
        ):
            relations.append(
                {
                    "relation": "EVALUATED_BY",
                    "target_id": str(
                        evaluation["evaluation_id"]
                    ),
                    "target_type": "VERIFICATION_EVALUATION",
                    "source": "DNA-09_VERIFICATION_WALL",
                }
            )

    return relations


def _knowledge_status(memory_class: str) -> str:
    mapping = {
        "verified": "VERIFIED",
        "hypothesis": "HYPOTHESIS",
        "rejected": "REJECTED",
    }
    return mapping[memory_class]


def _stable_node_id(record: Dict[str, Any]) -> str:
    source_hash = record.get("record_sha256")
    if not isinstance(source_hash, str) or not source_hash:
        source_hash = _sha256_json(record)
    return f"DNA-11-KNOWLEDGE-{source_hash[:16].upper()}"


def _node_sha256(node: Dict[str, Any]) -> str:
    content = deepcopy(node)
    content.pop("node_sha256", None)
    return _sha256_json(content)


def _assert_complete_node(node: Dict[str, Any]) -> None:
    missing = [
        field
        for field in REQUIRED_NODE_FIELDS
        if field not in node
    ]
    if missing:
        raise AssertionError(
            f"DNA-11_NODE_FIELDS_MISSING:{missing}"
        )

    if not isinstance(node["relations"], list) or not node[
        "relations"
    ]:
        raise AssertionError(
            "DNA-11_NODE_RELATION_REQUIRED"
        )
    if not isinstance(node["provenance"], list) or not node[
        "provenance"
    ]:
        raise AssertionError(
            "DNA-11_NODE_PROVENANCE_REQUIRED"
        )
    if not isinstance(node["evidence"], list) or not node[
        "evidence"
    ]:
        raise AssertionError(
            "DNA-11_NODE_EVIDENCE_REQUIRED"
        )
    if not isinstance(node["confidence"], dict):
        raise AssertionError(
            "DNA-11_NODE_CONFIDENCE_REQUIRED"
        )
    if not isinstance(node["contradictions"], list):
        raise AssertionError(
            "DNA-11_NODE_CONTRADICTIONS_REQUIRED"
        )
    if not isinstance(node["revision"], dict):
        raise AssertionError(
            "DNA-11_NODE_REVISION_REQUIRED"
        )
    if node["revision"].get("modifiable") is not True:
        raise AssertionError(
            "DNA-11_NODE_MUST_BE_MODIFIABLE"
        )
    if node["node_sha256"] != _node_sha256(node):
        raise AssertionError("DNA-11_NODE_HASH_MISMATCH")


def _create_or_get_node(
    context: Dict[str, Any],
    graph: Dict[str, Any],
    memory_class: str,
    record: Dict[str, Any],
) -> Tuple[Dict[str, Any], bool]:
    node_id = _stable_node_id(record)
    existing = graph["nodes"].get(node_id)
    if existing is not None:
        if not isinstance(existing, dict):
            raise TypeError(
                "knowledge graph node must be a dict"
            )
        _assert_complete_node(existing)
        return existing, False

    relations = _base_relations(record)
    relations.extend(
        _normalize_relations(
            context.get("knowledge_relations")
        )
    )

    node: Dict[str, Any] = {
        "node_id": node_id,
        "claim": _extract_claim(context, record),
        "knowledge_status": _knowledge_status(
            memory_class
        ),
        "source_memory_class": memory_class,
        "source_memory_record_id": record.get("record_id"),
        "relations": relations,
        "provenance": _extract_provenance(
            memory_class,
            record,
        ),
        "evidence": _extract_evidence(
            context,
            record,
        ),
        "confidence": _confidence_record(
            context,
            memory_class,
        ),
        "contradictions": _normalize_list_field(
            context,
            "knowledge_contradictions",
        ),
        "revision": {
            "modifiable": True,
            "version": 1,
            "supersedes_sha256": None,
            "revision_history": [],
        },
        "status": "ACTIVE",
    }
    node["node_sha256"] = _node_sha256(node)
    _assert_complete_node(node)
    graph["nodes"][node_id] = node
    return node, True


def _edge_from_relation(
    node_id: str,
    relation: Dict[str, Any],
) -> Dict[str, Any]:
    content = {
        "source_node_id": node_id,
        "relation": relation["relation"],
        "target_id": relation["target_id"],
        "target_type": relation["target_type"],
        "source": relation["source"],
    }
    return {
        "edge_id": f"DNA-11-EDGE-{_sha256_json(content)[:16].upper()}",
        **content,
    }


def _sync_node_edges(
    graph: Dict[str, Any],
    node: Dict[str, Any],
) -> None:
    node_id = node["node_id"]
    graph["edges"] = [
        edge
        for edge in graph["edges"]
        if not (
            isinstance(edge, dict)
            and edge.get("source_node_id") == node_id
        )
    ]

    seen: set[str] = set()
    for relation in node["relations"]:
        edge = _edge_from_relation(node_id, relation)
        if edge["edge_id"] in seen:
            continue
        seen.add(edge["edge_id"])
        graph["edges"].append(edge)


def _revision_confidence(
    revision: Dict[str, Any],
    memory_class: str,
    current: Dict[str, Any],
) -> Dict[str, Any]:
    if "confidence" not in revision:
        return deepcopy(current)

    value = _validate_confidence_value(
        revision["confidence"]
    )
    return {
        "value": value,
        "status": "EXPLICIT",
        "basis": [
            "REVISION_SUPPLIED_CONFIDENCE",
            f"SOURCE_MEMORY_CLASS:{memory_class}",
        ],
        "calibrated": False,
    }


def _apply_revision(
    context: Dict[str, Any],
    graph: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    revision = context.get("knowledge_revision")
    if revision is None:
        return None
    if not isinstance(revision, dict):
        raise TypeError(
            "context['knowledge_revision'] must be a dict"
        )

    target_node_id = revision.get("target_node_id")
    if not isinstance(target_node_id, str) or not target_node_id:
        raise ValueError(
            "DNA-11_REVISION_TARGET_NODE_REQUIRED"
        )

    node = graph["nodes"].get(target_node_id)
    if not isinstance(node, dict):
        raise KeyError(
            f"DNA-11_REVISION_TARGET_NOT_FOUND:{target_node_id}"
        )
    _assert_complete_node(node)

    if "replacement_claim" not in revision:
        raise ValueError(
            "DNA-11_REPLACEMENT_CLAIM_REQUIRED"
        )
    if revision["replacement_claim"] is None:
        raise ValueError(
            "DNA-11_REPLACEMENT_CLAIM_CANNOT_BE_NONE"
        )

    reason = revision.get("reason")
    if not isinstance(reason, str) or not reason.strip():
        raise ValueError("DNA-11_REVISION_REASON_REQUIRED")

    previous_version = node["revision"].get("version")
    if not isinstance(previous_version, int):
        raise TypeError(
            "DNA-11_NODE_REVISION_VERSION_MUST_BE_INT"
        )

    previous_snapshot = deepcopy(node)
    previous_hash = node["node_sha256"]

    node["claim"] = deepcopy(revision["replacement_claim"])

    if "evidence" in revision:
        if not isinstance(revision["evidence"], list):
            raise TypeError(
                "knowledge revision evidence must be a list"
            )
        node["evidence"] = deepcopy(revision["evidence"])
        if not node["evidence"]:
            raise ValueError(
                "DNA-11_REVISION_EVIDENCE_CANNOT_BE_EMPTY"
            )

    node["confidence"] = _revision_confidence(
        revision,
        node["source_memory_class"],
        node["confidence"],
    )

    if "contradictions" in revision:
        if not isinstance(revision["contradictions"], list):
            raise TypeError(
                "knowledge revision contradictions must be a list"
            )
        node["contradictions"] = deepcopy(
            revision["contradictions"]
        )

    if "relations" in revision:
        base = [
            relation
            for relation in node["relations"]
            if relation.get("source") != (
                "CALLER_SUPPLIED_RELATION"
            )
        ]
        base.extend(
            _normalize_relations(revision["relations"])
        )
        node["relations"] = base

    history = node["revision"].get("revision_history")
    if not isinstance(history, list):
        raise TypeError(
            "DNA-11_REVISION_HISTORY_MUST_BE_LIST"
        )

    history_entry = {
        "revision_sequence": len(history) + 1,
        "from_version": previous_version,
        "to_version": previous_version + 1,
        "reason": reason.strip(),
        "previous_node_sha256": previous_hash,
        "previous_claim": deepcopy(
            previous_snapshot["claim"]
        ),
    }
    history.append(history_entry)

    node["revision"]["version"] = previous_version + 1
    node["revision"]["supersedes_sha256"] = previous_hash
    node["status"] = "ACTIVE_REVISED"
    node["node_sha256"] = _node_sha256(node)
    _assert_complete_node(node)

    event = {
        "sequence": len(graph["revision_events"]) + 1,
        "revision_id": (
            f"DNA-11-REVISION-{len(graph['revision_events']) + 1:04d}"
        ),
        "node_id": target_node_id,
        "from_version": previous_version,
        "to_version": previous_version + 1,
        "reason": reason.strip(),
        "previous_node_sha256": previous_hash,
        "new_node_sha256": node["node_sha256"],
        "status": "APPLIED",
    }
    graph["revision_events"].append(event)
    _sync_node_edges(graph, node)
    return event


def dna11_knowledge_graph(
    payload: Any,
    core: CoreUnitLike,
) -> Dict[str, Any]:
    """
    Build an in-context knowledge graph whose nodes carry relations,
    provenance, evidence, confidence, contradictions, and revision state.

    DNA-11 does not start persistent Memory/Learning/World runtimes, invoke
    a model or verifier, auto-learn, execute F174, perform an external graph
    write, promote knowledge, or modify Canon.
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
    trace.append("DNA-11")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError(
            "context['core54_outputs'] must be a dict"
        )

    state, genome, _dna10_output = _validate_dependencies(
        context
    )
    graph = _install_knowledge_graph(state)

    actual_canon = _canon_record(core)
    canonical_sha256 = _sha256_json(actual_canon)

    state["provenance"].append(
        {
            "sequence": len(state["provenance"]) + 1,
            "core_id": "DNA-11",
            "operation": "KNOWLEDGE_GRAPH_CONTRACT_ESTABLISHED",
            "canonical_sha256": canonical_sha256,
            "knowledge_graph_schema": KNOWLEDGE_GRAPH_SCHEMA,
            "persistent_knowledge_runtime_started": False,
        }
    )

    memory_class, source_record = _select_source_record(
        genome
    )
    node: Optional[Dict[str, Any]] = None
    node_created = False

    if memory_class is not None and source_record is not None:
        node, node_created = _create_or_get_node(
            context,
            graph,
            memory_class,
            source_record,
        )
        _sync_node_edges(graph, node)

        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-11",
                "operation": (
                    "KNOWLEDGE_NODE_CREATED"
                    if node_created
                    else "KNOWLEDGE_NODE_REUSED"
                ),
                "canonical_sha256": canonical_sha256,
                "node_id": node["node_id"],
                "knowledge_status": node[
                    "knowledge_status"
                ],
                "source_memory_class": memory_class,
                "node_sha256": node["node_sha256"],
            }
        )

    revision_event = _apply_revision(context, graph)
    if revision_event is not None:
        revised_node = graph["nodes"][
            revision_event["node_id"]
        ]
        node = revised_node
        state["provenance"].append(
            {
                "sequence": len(state["provenance"]) + 1,
                "core_id": "DNA-11",
                "operation": "KNOWLEDGE_NODE_REVISED",
                "canonical_sha256": canonical_sha256,
                "revision_id": revision_event[
                    "revision_id"
                ],
                "node_id": revision_event["node_id"],
                "from_version": revision_event[
                    "from_version"
                ],
                "to_version": revision_event[
                    "to_version"
                ],
                "new_node_sha256": revision_event[
                    "new_node_sha256"
                ],
            }
        )

    for graph_node in graph["nodes"].values():
        if not isinstance(graph_node, dict):
            raise TypeError(
                "knowledge graph node must be a dict"
            )
        _assert_complete_node(graph_node)

    outputs["DNA-11"] = {
        "canonical_gene": actual_canon,
        "canonical_sha256": canonical_sha256,
        "knowledge_graph_contract": deepcopy(
            KNOWLEDGE_GRAPH_CONTRACT
        ),
        "node_created": node_created,
        "active_node": deepcopy(node),
        "revision_event": deepcopy(revision_event),
        "node_count": len(graph["nodes"]),
        "edge_count": len(graph["edges"]),
        "persistent_knowledge_runtime_used": False,
        "persistent_memory_runtime_used": False,
        "external_graph_write": False,
        "status": "CANON_ALIGNED",
    }

    return context


def bind_dna11(core54: Core54Like) -> None:
    core = core54.get("DNA-11")
    assert_exact_canon(core)
    core54.bind(
        "DNA-11",
        dna11_knowledge_graph,
    )


def _build_base_probe() -> Dict[str, Any]:
    return {
        "trace": [],
        "caller_data": {"preserve": True},
        "goal": {
            "id": "GOAL-DNA11",
            "statement": "build traceable revisable knowledge",
        },
        "strategy": "STRATEGY-A",
        "next_strategy": "STRATEGY-B",
        "failure": {
            "detected": True,
            "layer": "verification",
            "recovery_operation": "REFRAME",
            "reason": "FIRST_STRATEGY_FAILED",
        },
        "environment": {
            "id": "WORLD-DNA11-SELF-CHECK",
            "state": "INITIAL",
        },
        "action": {
            "id": "ACTION-DNA11-01",
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
                "subject": "DNA-11_SELF_CHECK",
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
                    "KNOWLEDGE_GRAPH_UNDER_TEST"
                ],
            },
        },
    }


def _run_through(
    core54: Core54Like,
    context: Dict[str, Any],
    final_core_id: str,
) -> Dict[str, Any]:
    final_index = int(final_core_id.split("-")[1])
    result = deepcopy(context)
    for index in range(1, final_index + 1):
        core_id = f"DNA-{index:02d}"
        result = core54.get(core_id).activate(result)
    return result


def _derive_candidate_sha256(
    core54: Core54Like,
    base_probe: Dict[str, Any],
) -> str:
    through_dna08 = _run_through(
        core54,
        base_probe,
        "DNA-08",
    )
    event = through_dna08[
        "core54_outputs"
    ]["DNA-08"]["world_event"]
    if not isinstance(event, dict):
        raise AssertionError(
            "DNA-11_SELF_CHECK_DNA08_EVENT_MISSING"
        )

    candidate_content = {
        "source_core_id": "DNA-08",
        "source_event_id": event.get("event_id"),
        "interaction_sha256": event.get(
            "interaction_sha256"
        ),
        "experience": deepcopy(event.get("experience")),
    }
    return _sha256_json(candidate_content)


def _verification(
    candidate_sha256: str,
    *,
    passed: bool,
) -> Dict[str, Any]:
    return {
        "learner_id": "LEARNER-A",
        "verifier_id": "VERIFIER-B",
        "verifier_independent": True,
        "independence_basis": [
            "SEPARATE_ROLE",
            "NO_SHARED_DECISION_AUTHORITY",
        ],
        "candidate_sha256": candidate_sha256,
        "method": "INDEPENDENT_REPLAY_AND_COMPARISON",
        "scope": "DNA-08_EXPERIENTIAL_EVENT",
        "evidence": [
            {
                "type": "REPLAY_RESULT",
                "result": (
                    "CONSISTENT"
                    if passed
                    else "INCONSISTENT"
                ),
            }
        ],
        "passed": passed,
    }


def self_check_dna11(
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
        "DNA-09",
        "DNA-10",
    ):
        if not core54.get(required_id).state.behavior_bound:
            raise RuntimeError(
                f"{required_id}_MUST_PASS_AND_BE_BOUND_FIRST"
            )

    dna11_core = core54.get("DNA-11")
    assert_exact_canon(dna11_core)
    bind_dna11(core54)

    base_probe = _build_base_probe()
    candidate_sha256 = _derive_candidate_sha256(
        core54,
        base_probe,
    )

    verified_probe = deepcopy(base_probe)
    verified_probe["verification"] = _verification(
        candidate_sha256,
        passed=True,
    )
    verified_probe["knowledge_confidence"] = 0.86
    verified_probe["knowledge_contradictions"] = [
        {
            "claim": "NO_STATE_CHANGE_OCCURRED",
            "status": "UNRESOLVED_COUNTERCLAIM",
        }
    ]
    verified_probe["knowledge_relations"] = [
        {
            "relation": "related_to",
            "target_id": "CONCEPT-ADAPTIVE-CHANGE",
            "target_type": "concept",
        }
    ]
    verified_snapshot = deepcopy(verified_probe)

    verified_result = _run_through(
        core54,
        verified_probe,
        "DNA-11",
    )

    assert verified_probe == verified_snapshot
    assert verified_result["trace"] == [
        f"DNA-{index:02d}"
        for index in range(1, 12)
    ]

    dna11 = verified_result["core54_outputs"]["DNA-11"]
    assert dna11["canonical_gene"] == CANON_DNA11
    assert dna11["knowledge_graph_contract"] == (
        KNOWLEDGE_GRAPH_CONTRACT
    )
    assert dna11["node_created"] is True
    assert dna11["revision_event"] is None
    assert dna11["node_count"] == 1
    assert dna11["edge_count"] == 4
    assert (
        dna11["persistent_knowledge_runtime_used"]
        is False
    )
    assert (
        dna11["persistent_memory_runtime_used"]
        is False
    )
    assert dna11["external_graph_write"] is False
    assert dna11["status"] == "CANON_ALIGNED"

    node = dna11["active_node"]
    assert node is not None
    _assert_complete_node(node)
    assert node["claim"] == (
        "ACTION_CHANGED_ENVIRONMENT_STATE"
    )
    assert node["knowledge_status"] == "VERIFIED"
    assert node["source_memory_class"] == "verified"
    assert node["confidence"] == {
        "value": 0.86,
        "status": "EXPLICIT",
        "basis": [
            "CALLER_SUPPLIED_CONFIDENCE",
            "SOURCE_MEMORY_CLASS:verified",
        ],
        "calibrated": False,
    }
    assert node["contradictions"] == (
        verified_probe["knowledge_contradictions"]
    )
    assert node["revision"] == {
        "modifiable": True,
        "version": 1,
        "supersedes_sha256": None,
        "revision_history": [],
    }
    assert len(node["provenance"]) == 3
    assert len(node["evidence"]) == 3
    assert [
        relation["relation"]
        for relation in node["relations"]
    ] == [
        "DERIVED_FROM",
        "SUPPORTED_BY",
        "EVALUATED_BY",
        "RELATED_TO",
    ]

    graph = verified_result[
        "cognitive_state"
    ]["knowledge_graph"]
    assert graph["contract"] == KNOWLEDGE_GRAPH_CONTRACT
    assert list(graph["nodes"]) == [node["node_id"]]
    assert graph["nodes"][node["node_id"]] == node
    assert len(graph["edges"]) == 4
    assert graph["revision_events"] == []

    # Knowledge must remain revisable with lineage preserved.
    revision_input = deepcopy(verified_result)
    revision_input["knowledge_revision"] = {
        "target_node_id": node["node_id"],
        "replacement_claim": (
            "ACTION_CHANGED_ENVIRONMENT_STATE_UNDER_"
            "THE_TESTED_CONDITIONS"
        ),
        "reason": "NARROW_CLAIM_TO_OBSERVED_SCOPE",
        "evidence": deepcopy(node["evidence"]),
        "confidence": 0.92,
        "contradictions": [],
        "relations": [
            {
                "relation": "related_to",
                "target_id": "CONCEPT-CONDITIONAL-CHANGE",
                "target_type": "concept",
            }
        ],
    }
    revised = dna11_core.activate(revision_input)
    revised_output = revised[
        "core54_outputs"
    ]["DNA-11"]
    revision_event = revised_output["revision_event"]
    assert revision_event is not None
    assert revision_event["status"] == "APPLIED"
    assert revision_event["from_version"] == 1
    assert revision_event["to_version"] == 2

    revised_node = revised_output["active_node"]
    assert revised_node is not None
    assert revised_node["node_id"] == node["node_id"]
    assert revised_node["claim"] == (
        "ACTION_CHANGED_ENVIRONMENT_STATE_UNDER_"
        "THE_TESTED_CONDITIONS"
    )
    assert revised_node["confidence"]["value"] == 0.92
    assert revised_node["contradictions"] == []
    assert revised_node["revision"]["version"] == 2
    assert revised_node["revision"][
        "supersedes_sha256"
    ] == node["node_sha256"]
    assert len(
        revised_node["revision"]["revision_history"]
    ) == 1
    assert revised_node["status"] == "ACTIVE_REVISED"
    _assert_complete_node(revised_node)
    assert len(
        revised["cognitive_state"]["knowledge_graph"][
            "revision_events"
        ]
    ) == 1

    # Without independent verification, the graph retains a hypothesis.
    hypothesis_probe = _build_base_probe()
    hypothesis_result = _run_through(
        core54,
        hypothesis_probe,
        "DNA-11",
    )
    hypothesis_node = hypothesis_result[
        "core54_outputs"
    ]["DNA-11"]["active_node"]
    assert hypothesis_node is not None
    assert hypothesis_node["knowledge_status"] == "HYPOTHESIS"
    assert hypothesis_node["source_memory_class"] == (
        "hypothesis"
    )
    assert hypothesis_node["confidence"]["value"] is None
    assert hypothesis_node["confidence"]["status"] == (
        "UNRESOLVED"
    )
    _assert_complete_node(hypothesis_node)

    # Explicit verifier failure remains represented as rejected knowledge.
    rejected_probe = _build_base_probe()
    rejected_probe["verification"] = _verification(
        candidate_sha256,
        passed=False,
    )
    rejected_result = _run_through(
        core54,
        rejected_probe,
        "DNA-11",
    )
    rejected_node = rejected_result[
        "core54_outputs"
    ]["DNA-11"]["active_node"]
    assert rejected_node is not None
    assert rejected_node["knowledge_status"] == "REJECTED"
    assert rejected_node["source_memory_class"] == "rejected"
    assert any(
        item.get("type") == "VERIFICATION_REJECTION_REASONS"
        for item in rejected_node["evidence"]
        if isinstance(item, dict)
    )
    _assert_complete_node(rejected_node)

    # Confidence cannot be fabricated outside the valid interval.
    invalid_confidence = deepcopy(verified_result)
    invalid_confidence["cognitive_state"].pop(
        "knowledge_graph",
        None,
    )
    invalid_confidence["knowledge_confidence"] = 1.5
    try:
        dna11_core.activate(invalid_confidence)
    except ValueError as exc:
        assert str(exc) == (
            "DNA-11_CONFIDENCE_MUST_BE_BETWEEN_0_AND_1"
        )
    else:
        raise AssertionError(
            "DNA-11_ACCEPTED_INVALID_CONFIDENCE"
        )

    # Revision cannot target a non-existent knowledge node.
    missing_target = deepcopy(verified_result)
    missing_target["knowledge_revision"] = {
        "target_node_id": "DNA-11-MISSING",
        "replacement_claim": "X",
        "reason": "TEST",
    }
    try:
        dna11_core.activate(missing_target)
    except KeyError as exc:
        assert "DNA-11_REVISION_TARGET_NOT_FOUND" in str(exc)
    else:
        raise AssertionError(
            "DNA-11_ACCEPTED_MISSING_REVISION_TARGET"
        )

    # Reject the provisional root marker as the official Canon contract.
    assert "knowledge_node" not in verified_result
    assert "flags" not in verified_result
    assert "requests" not in verified_result
    assert "blocks" not in verified_result

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
        "core_id": "DNA-11",
        "canon_mapping": "PASS",
        "relationships": "PASS",
        "provenance": "PASS",
        "evidence": "PASS",
        "confidence": "PASS",
        "contradictions": "PASS",
        "modifiability": "PASS",
        "revision_lineage": "PASS",
        "persistent_knowledge_runtime_used": False,
        "persistent_memory_runtime_used": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": (
            "PASS"
            if verify_canon_file
            else "NOT_CHECKED"
        ),
        "phase_locks": "PASS",
        "next_authorized": (
            "DNA-12"
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
        (
            GENES_ROOT
            / "SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL.py"
        ),
        GENES_ROOT / "SIGMA_DNA_10_MEMORY_GENOME.py",
    ]

    required_paths = [
        CORE54_ROOT,
        GENES_ROOT,
        DNA_JSON,
        *required_gene_files,
    ]
    for path in required_paths:
        if not path.exists():
            print("DNA-11_FAIL: REQUIRED_PATH_NOT_FOUND")
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
        from SIGMA_DNA_09_INDEPENDENT_VERIFICATION_WALL import (
            self_check_dna09,
        )
        from SIGMA_DNA_10_MEMORY_GENOME import (
            self_check_dna10,
        )
    except Exception as exc:
        print("DNA-11_FAIL: IMPORT_ERROR")
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
            ("DNA-09", self_check_dna09),
            ("DNA-10", self_check_dna10),
        )
        for core_id, checker in prior_checks:
            prior_report = checker(
                core54,
                verify_canon_file=True,
            )
            if prior_report["self_check"] != "PASS":
                raise RuntimeError(f"{core_id}_NOT_PASS")

        report = self_check_dna11(
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
            for index in range(1, 12)
        ]:
            raise RuntimeError(
                "DNA-01_TO_DNA-11_BINDING_VIOLATION:"
                f"{bound_ids}"
            )

    except Exception as exc:
        print("DNA-11_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_11_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("RELATIONSHIPS:", report["relationships"])
    print("PROVENANCE:", report["provenance"])
    print("EVIDENCE:", report["evidence"])
    print("CONFIDENCE:", report["confidence"])
    print("CONTRADICTIONS:", report["contradictions"])
    print("MODIFIABILITY:", report["modifiability"])
    print("REVISION_LINEAGE:", report["revision_lineage"])
    print(
        "PERSISTENT_KNOWLEDGE_RUNTIME_USED:",
        report["persistent_knowledge_runtime_used"],
    )
    print(
        "PERSISTENT_MEMORY_RUNTIME_USED:",
        report["persistent_memory_runtime_used"],
    )
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 11/54")
    print("NEXT_AUTHORIZED: DNA-12")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
