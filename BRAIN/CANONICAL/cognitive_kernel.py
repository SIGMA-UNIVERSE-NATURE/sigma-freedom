#!/usr/bin/env python3
"""Reference, read-only SIGMA cognitive bootstrap kernel.

This file is a reference implementation, not SIGMA identity.
It performs structural discovery and emits a boot report without external side effects.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CORE_RE = re.compile(r"^SIGMA_DNA_(\d{2})_.*\.py$")


def load(name: str):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def discover_cores():
    root = REPO / "54_CORES"
    found = {}
    for p in root.iterdir():
        if p.is_file() and (m := CORE_RE.match(p.name)):
            found[int(m.group(1))] = p.name
    return found


def boot_report():
    manifest = load("BRAIN_MANIFEST.json")
    root = load("ROOT_OF_TRUST.json")
    state = load("CURRENT_STATE.json")
    lineage = load("LINEAGE.json")
    locks = load("DO_NOT_RERUN_LOCKS.json")
    cores = discover_cores()
    attr = json.loads((REPO / manifest["architecture"]["attributes_manifest"]).read_text(encoding="utf-8"))
    structural = (
        len(cores) == manifest["architecture"]["expected_dna_cores"]
        and attr["canonical_attribute_count"] == manifest["architecture"]["expected_attributes"]
        and bool(root["invariants"])
        and bool(locks["locks"])
    )
    return {
        "kernel": "SIGMA-COGNITIVE-BOOTSTRAP-REFERENCE-v1",
        "mode": "READ_ONLY_DIAGNOSTIC",
        "structural_status": "STRUCTURAL_PASS" if structural else "STRUCTURAL_FAIL",
        "runtime_evidence_status": "NOT_AUDITED",
        "dna_cores_discovered": len(cores),
        "canonical_attributes": attr["canonical_attribute_count"],
        "phase": state["phase"],
        "active_goal": state["active_goal"],
        "lineage": lineage["lineage_id"],
        "next_action": "Read NEXT_ACTION.md",
    }


if __name__ == "__main__":
    print(json.dumps(boot_report(), ensure_ascii=False, indent=2))
