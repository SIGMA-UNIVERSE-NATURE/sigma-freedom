#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
DNA_JSON = SIGMA_ROOT / "CORE" / "DNA_CANON" / "SIGMA_CORE_DNA_54" / "sigma_dna_54.json"

CANON_DNA35: Dict[str, str] = {
    "id": "DNA-35",
    "name": "Core Covenant",
    "purpose": (
        "Think freely; seek evidence; do not pretend to know; "
        "learn from consequences; guide, do not dominate."
    ),
    "system": "identity",
}

UNIFIED_STATE_SCHEMA = "SIGMA_UNIFIED_COGNITIVE_STATE_V1"
CORE_COVENANT_SCHEMA = "SIGMA_CORE_COVENANT_V1"

CANON_CLAUSES = [
    "THINK_FREELY",
    "SEEK_EVIDENCE",
    "DO_NOT_PRETEND_TO_KNOW",
    "LEARN_FROM_CONSEQUENCES",
    "GUIDE_DO_NOT_DOMINATE",
]

CORE_COVENANT_CONTRACT = {
    "schema": CORE_COVENANT_SCHEMA,
    "clauses": CANON_CLAUSES,
    "clause_count": 5,
    "all_clauses_required": True,
    "behavior_evidence_required": True,
    "self_declaration_alone_sufficient": False,
    "truth_claim_without_evidence_allowed": False,
    "domination_allowed": False,
    "higher_runtime_started": False,
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
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=repr)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def assert_exact_canon(core: CoreUnitLike) -> None:
    actual = _canon_record(core)
    if actual != CANON_DNA35:
        raise RuntimeError(f"DNA-35_CANON_MISMATCH:{actual!r}")


def _validate_state(context: Dict[str, Any]) -> Dict[str, Any]:
    state = context.get("cognitive_state")
    if not isinstance(state, dict):
        raise RuntimeError("DNA-03_UNIFIED_COGNITIVE_STATE_REQUIRED")
    if state.get("schema") != UNIFIED_STATE_SCHEMA:
        raise ValueError("DNA-35_UNIFIED_STATE_SCHEMA_MISMATCH")
    if not isinstance(state.get("provenance"), list):
        raise TypeError("cognitive_state.provenance must be a list")
    return state


def _install(state: Dict[str, Any]) -> Dict[str, Any]:
    existing = state.get("core_covenant")
    if existing is None:
        existing = {
            "contract": deepcopy(CORE_COVENANT_CONTRACT),
            "assessments": [],
        }
        state["core_covenant"] = existing
    if existing.get("contract") != CORE_COVENANT_CONTRACT:
        raise ValueError("DNA-35_CORE_COVENANT_CONTRACT_CONFLICT")
    if not isinstance(existing.get("assessments"), list):
        raise TypeError("core_covenant.assessments must be a list")
    return existing


def _normalize_record(item: Any, index: int) -> Dict[str, Any]:
    if not isinstance(item, dict):
        raise TypeError(f"core_covenant_evidence[{index}] must be a dict")
    for key in ("clause", "behavior", "evidence", "passed"):
        if key not in item:
            raise ValueError(f"DNA-35_FIELD_REQUIRED:{key}")

    clause = item["clause"]
    if not isinstance(clause, str):
        raise TypeError("clause must be a string")
    clause = clause.strip().upper()
    if clause not in CANON_CLAUSES:
        raise ValueError(f"DNA-35_UNKNOWN_COVENANT_CLAUSE:{clause}")

    behavior = item["behavior"]
    evidence = item["evidence"]
    passed = item["passed"]
    self_declaration_only = item.get("self_declaration_only", False)

    if not isinstance(behavior, list) or not behavior:
        raise ValueError(f"DNA-35_BEHAVIOR_REQUIRED:{clause}")
    if not isinstance(evidence, list) or not evidence:
        raise ValueError(f"DNA-35_EVIDENCE_REQUIRED:{clause}")
    if not isinstance(passed, bool):
        raise TypeError("passed must be bool")
    if not isinstance(self_declaration_only, bool):
        raise TypeError("self_declaration_only must be bool")

    proof_valid = passed and not self_declaration_only
    return {
        "index": index,
        "clause": clause,
        "behavior": deepcopy(behavior),
        "behavior_sha256": _sha256_json(behavior),
        "evidence": deepcopy(evidence),
        "evidence_sha256": _sha256_json(evidence),
        "passed": passed,
        "self_declaration_only": self_declaration_only,
        "proof_valid": proof_valid,
    }


def _evaluate(records_in: Any, state: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(records_in, list):
        raise TypeError("core_covenant_evidence must be a list")

    records = [_normalize_record(x, i) for i, x in enumerate(records_in, 1)]
    keys = [x["clause"] for x in records]
    if len(keys) != len(set(keys)):
        raise ValueError("DNA-35_DUPLICATE_COVENANT_CLAUSE")

    missing = [x for x in CANON_CLAUSES if x not in set(keys)]
    failed = [x["clause"] for x in records if not x["proof_valid"]]
    complete = not missing and len(records) == 5
    all_proven = complete and not failed

    assessment = {
        "assessment_id": f"DNA-35-COVENANT-{len(state['assessments']) + 1:04d}",
        "records": records,
        "missing_clauses": missing,
        "failed_clauses": failed,
        "complete": complete,
        "all_clauses_proven": all_proven,
        "self_declaration_accepted_as_proof": False,
        "status": (
            "CORE_COVENANT_EVIDENCE_COMPLETE"
            if all_proven else
            "CORE_COVENANT_EVIDENCE_FAILED"
            if complete else
            "CORE_COVENANT_EVIDENCE_INCOMPLETE"
        ),
    }
    state["assessments"].append(deepcopy(assessment))
    return assessment


def dna35_core_covenant(payload: Any, core: CoreUnitLike) -> Dict[str, Any]:
    assert_exact_canon(core)
    context = deepcopy(payload) if isinstance(payload, dict) else {"input": deepcopy(payload)}
    trace = context.setdefault("trace", [])
    if not isinstance(trace, list):
        raise TypeError("trace must be a list")
    trace.append("DNA-35")

    outputs = context.setdefault("core54_outputs", {})
    if not isinstance(outputs, dict):
        raise TypeError("core54_outputs must be a dict")

    cognitive = _validate_state(context)
    covenant = _install(cognitive)
    canon = _canon_record(core)
    canon_sha = _sha256_json(canon)

    assessment = _evaluate(context.get("core_covenant_evidence"), covenant)

    cognitive["provenance"].append({
        "sequence": len(cognitive["provenance"]) + 1,
        "core_id": "DNA-35",
        "operation": "CORE_COVENANT_EVIDENCE_EVALUATED",
        "canonical_sha256": canon_sha,
        "all_clauses_proven": assessment["all_clauses_proven"],
        "higher_runtime_started": False,
        "external_action_executed": False,
    })

    outputs["DNA-35"] = {
        "canonical_gene": canon,
        "canonical_sha256": canon_sha,
        "core_covenant_contract": deepcopy(CORE_COVENANT_CONTRACT),
        "assessment": deepcopy(assessment),
        "think_freely": True,
        "seek_evidence": True,
        "do_not_pretend_to_know": True,
        "learn_from_consequences": True,
        "guide_do_not_dominate": True,
        "all_clauses_proven": assessment["all_clauses_proven"],
        "higher_runtime_started": False,
        "external_action_executed": False,
        "status": "CANON_ALIGNED",
    }
    return context


def bind_dna35(core54: Core54Like) -> None:
    core = core54.get("DNA-35")
    assert_exact_canon(core)
    core54.bind("DNA-35", dna35_core_covenant)


def _valid_evidence() -> List[Dict[str, Any]]:
    source_map = {
        "THINK_FREELY": "DNA-23",
        "SEEK_EVIDENCE": "DNA-21",
        "DO_NOT_PRETEND_TO_KNOW": "DNA-20",
        "LEARN_FROM_CONSEQUENCES": "DNA-16",
        "GUIDE_DO_NOT_DOMINATE": "DNA-22",
    }
    return [
        {
            "clause": clause,
            "behavior": [{"result": "CANON_ALIGNED_BEHAVIOR"}],
            "evidence": [{"source_core_id": source_map[clause], "result": "PASS"}],
            "passed": True,
        }
        for clause in CANON_CLAUSES
    ]


def self_check_dna35(core54: Core54Like, *, verify_canon_file: bool = True) -> Dict[str, Any]:
    before = _sha256_file(DNA_JSON) if verify_canon_file else None

    for i in range(1, 35):
        if not core54.get(f"DNA-{i:02d}").state.behavior_bound:
            raise RuntimeError(f"DNA-{i:02d}_MUST_PASS_AND_BE_BOUND_FIRST")

    core = core54.get("DNA-35")
    assert_exact_canon(core)
    bind_dna35(core54)

    probe = {
        "trace": [f"DNA-{i:02d}" for i in range(1, 35)],
        "core54_outputs": {},
        "cognitive_state": {
            "schema": UNIFIED_STATE_SCHEMA,
            "content": {},
            "provenance": [],
            "uncertainty": {},
        },
        "core_covenant_evidence": _valid_evidence(),
    }
    snapshot = deepcopy(probe)
    result = core.activate(probe)
    assert probe == snapshot

    output = result["core54_outputs"]["DNA-35"]
    assert output["canonical_gene"] == CANON_DNA35
    assert output["all_clauses_proven"] is True
    assert output["higher_runtime_started"] is False
    assert output["external_action_executed"] is False

    self_claim = deepcopy(probe)
    self_claim["core_covenant_evidence"][0]["self_declaration_only"] = True
    self_claim_result = core.activate(self_claim)
    assert self_claim_result["core54_outputs"]["DNA-35"]["all_clauses_proven"] is False

    incomplete = deepcopy(probe)
    incomplete["core_covenant_evidence"] = _valid_evidence()[:-1]
    incomplete_result = core.activate(incomplete)
    assert incomplete_result["core54_outputs"]["DNA-35"]["assessment"]["missing_clauses"] == [
        "GUIDE_DO_NOT_DOMINATE"
    ]

    locks = {
        "auto_learning": bool(core54.auto_learning_enabled),
        "model_calls": bool(core54.model_calls_enabled),
        "external_execution": bool(core54.external_execution_enabled),
        "canon_write": bool(core54.canon_write_enabled),
    }
    assert not any(locks.values()), locks

    after = _sha256_file(DNA_JSON) if verify_canon_file else None
    if verify_canon_file:
        assert before == after

    return {
        "core_id": "DNA-35",
        "canon_mapping": "PASS",
        "think_freely": "PASS",
        "seek_evidence": "PASS",
        "do_not_pretend_to_know": "PASS",
        "learn_from_consequences": "PASS",
        "guide_do_not_dominate": "PASS",
        "five_clause_covenant_gate": "PASS",
        "higher_runtime_started": False,
        "executable": "PASS",
        "self_check": "PASS",
        "canon_unchanged": "PASS" if verify_canon_file else "NOT_CHECKED",
        "phase_locks": "PASS",
        "next_authorized": "DNA-36" if verify_canon_file else "RUN_ON_CANONICAL_E_DRIVE",
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
}


def main() -> int:
    for path in [CORE54_ROOT, GENES_ROOT, DNA_JSON]:
        if not path.exists():
            print("DNA-35_FAIL: REQUIRED_PATH_NOT_FOUND")
            print(path)
            return 1

    sys.path.insert(0, str(CORE54_ROOT))
    sys.path.insert(0, str(GENES_ROOT))

    try:
        from sigma_core54_foundation_v0_3 import SigmaCore54
        modules = {i: importlib.import_module(name) for i, name in PRIOR.items()}
    except Exception as exc:
        print("DNA-35_FAIL: IMPORT_ERROR")
        print(repr(exc))
        return 2

    try:
        core54 = SigmaCore54()
        core54.boot()

        for i in range(1, 35):
            report = getattr(modules[i], f"self_check_dna{i:02d}")(
                core54,
                verify_canon_file=True,
            )
            assert report["self_check"] == "PASS"

        report = self_check_dna35(core54, verify_canon_file=True)
    except Exception as exc:
        print("DNA-35_FAIL")
        print(repr(exc))
        return 3

    print("SIGMA_CORE_DNA_35_PASS")
    print("CANON_MAPPING:", report["canon_mapping"])
    print("THINK_FREELY:", report["think_freely"])
    print("SEEK_EVIDENCE:", report["seek_evidence"])
    print("DO_NOT_PRETEND_TO_KNOW:", report["do_not_pretend_to_know"])
    print("LEARN_FROM_CONSEQUENCES:", report["learn_from_consequences"])
    print("GUIDE_DO_NOT_DOMINATE:", report["guide_do_not_dominate"])
    print("FIVE_CLAUSE_COVENANT_GATE:", report["five_clause_covenant_gate"])
    print("HIGHER_RUNTIME_STARTED:", report["higher_runtime_started"])
    print("EXECUTABLE:", report["executable"])
    print("SELF_CHECK:", report["self_check"])
    print("CANON_UNCHANGED:", report["canon_unchanged"])
    print("PHASE_LOCKS:", report["phase_locks"])
    print("OFFICIAL_BOUND_CORES: 35/54")
    print("NEXT_AUTHORIZED: DNA-36")
    print("NEXT_PHASE: FORBIDDEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
