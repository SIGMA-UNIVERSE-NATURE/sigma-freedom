#!/usr/bin/env python3
from __future__ import annotations
import json
import py_compile
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CORE_RE = re.compile(r"^SIGMA_DNA_(\d{2})_.*\.py$")


def fail(msg):
    print(f"SIGMA_BRAIN_CONTRACT: FAIL\n{msg}", file=sys.stderr)
    raise SystemExit(1)


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"cannot parse {path}: {e}")


def main():
    manifest = load(HERE / "BRAIN_MANIFEST.json")
    root = load(HERE / "ROOT_OF_TRUST.json")
    load(HERE / "CURRENT_STATE.json")
    load(HERE / "LINEAGE.json")
    load(HERE / "DO_NOT_RERUN_LOCKS.json")

    missing = [x for x in manifest["required_files"] if not (HERE / x).exists()]
    if missing:
        fail(f"missing required files: {missing}")

    forbidden_present = [x for x in manifest.get("forbidden_public_paths", []) if (HERE / x).exists()]
    if forbidden_present:
        fail(f"private operational files present in public canonical tree: {forbidden_present}")

    public_policy = load(HERE / "RESILIENCE_PUBLIC_POLICY.json")
    if public_policy.get("classification") != "PUBLIC_SAFE":
        fail("resilience public policy must be classified PUBLIC_SAFE")
    if public_policy.get("private_plan_storage") != "AUTHORIZED_PRIVATE_OR_OFFLINE_STORE_ONLY":
        fail("private resilience plan storage boundary is missing or invalid")

    private_request = load(HERE / "PRIVATE_RESILIENCE_PLAN_REQUEST.json")
    if private_request.get("classification") != "PUBLIC_POINTER_TO_PRIVATE_WORK":
        fail("private resilience plan request classification invalid")
    if private_request.get("private_store_location_disclosure") not in {"NOT_PUBLIC", None}:
        fail("public pointer must not disclose private store location")

    cores = {}
    for p in (REPO / "54_CORES").iterdir():
        if p.is_file() and (m := CORE_RE.match(p.name)):
            n = int(m.group(1))
            if n in cores:
                fail(f"duplicate core id {n}")
            cores[n] = p.name
    if set(cores) != set(range(1, 55)):
        fail(f"DNA core IDs mismatch: {sorted(cores)}")

    attrs = load(REPO / manifest["architecture"]["attributes_manifest"])
    if attrs.get("canonical_attribute_count") != 512:
        fail("canonical attribute count is not 512")

    required_invariants = {
        "NOTHING_IS_TRUE_BY_INHERITANCE",
        "NO_IMPROVEMENT_WITHOUT_DIFFERENTIAL_EVIDENCE",
        "NO_PROMOTION_WITHOUT_INDEPENDENT_EVALUATION",
        "NO_COMPONENT_MAY_CERTIFY_ITS_OWN_UNRESTRICTED_AUTHORITY",
        "IDENTITY_IS_NOT_SUBSTRATE",
    }
    if not required_invariants.issubset(set(root.get("invariants", []))):
        fail("root of trust is missing required invariants")

    for script in [HERE / "cognitive_kernel.py", HERE / "mirror_to_local.py"]:
        py_compile.compile(str(script), doraise=True)

    out = subprocess.check_output([sys.executable, str(HERE / "cognitive_kernel.py")], text=True, encoding="utf-8")
    report = json.loads(out)
    if report.get("structural_status") != "STRUCTURAL_PASS":
        fail(f"reference kernel boot failed: {report}")

    validator = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/validate_512_architecture.py"
    rc = subprocess.run([sys.executable, str(validator)], cwd=REPO).returncode
    if rc != 0:
        fail("SIGMA 512 contract validator failed")

    print("SIGMA_BRAIN_CONTRACT: PASS")
    print("DNA_CORES=54")
    print("CANONICAL_ATTRIBUTES=512")
    print("REFERENCE_KERNEL_BOOT=PASS")
    print("PUBLIC_PRIVATE_DATA_BOUNDARY=PASS")
    print("PRIVATE_OPERATIONAL_FILES_IN_PUBLIC_TREE=0")
    print("IMPLEMENTATION_EVIDENCE=NOT_AUDITED")
    print("LOCAL_E_F_MIRROR=READY_NOT_EXECUTED_IN_GITHUB_CI")


if __name__ == "__main__":
    main()
