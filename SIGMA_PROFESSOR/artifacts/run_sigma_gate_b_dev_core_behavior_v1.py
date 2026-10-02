#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import secrets
import subprocess
import sys
import time
from pathlib import Path

from validate_sigma_gate_b_dev_core_behavior_v1 import ValidationError, sha256_file, validate_manifest, validate_receipt


def write_json(path, obj):
    tmp = str(path) + ".partial"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def expand_arg(arg, mapping):
    out = arg
    for k, v in mapping.items():
        out = out.replace(k, v)
    return out


def snapshot_bound_hashes(resolved):
    out = {}
    for name, binding in resolved["bindings"].items():
        out["binding:" + name] = sha256_file(binding["path"])
    for name in ("train_source", "dev", "core"):
        pair = resolved["worksets"][name]
        out["workset:%s:artifact" % name] = sha256_file(pair["artifact"]["path"])
        out["workset:%s:provenance" % name] = sha256_file(pair["provenance"]["path"])
    for idx, item in enumerate(resolved["worksets"]["behavior"], 1):
        out["behavior:%d:artifact" % idx] = sha256_file(item["artifact"]["path"])
        out["behavior:%d:provenance" % idx] = sha256_file(item["provenance"]["path"])
    out["split:builder"] = sha256_file(resolved["split_builder"]["path"])
    out["split:receipt"] = sha256_file(resolved["split_receipt"]["path"])
    return out


def build_runtime_input(resolved, run_id):
    m = resolved["manifest"]
    behavior = []
    for item in resolved["worksets"]["behavior"]:
        behavior.append({
            "capability_id": item["capability_id"],
            "workset_path": item["artifact"]["path"],
            "workset_sha256": item["artifact"]["sha256"],
            "provenance_path": item["provenance"]["path"],
            "provenance_sha256": item["provenance"]["sha256"],
        })
    return {
        "schema": "SIGMA_GATE_B_DEV_CORE_BEHAVIOR_NATIVE_INPUT_V1",
        "run_id": run_id,
        "proof_scope": "TINY",
        "identity": m["evidence"]["one_sigma_identity"],
        "parent_model_ref": m["evidence"]["r57"]["parent_model"],
        "model_ref": m["evidence"]["r57"]["child_model"],
        "parent_opt_ref": m["evidence"]["r57"]["parent_opt"],
        "child_opt_ref": m["evidence"]["r57"]["child_opt"],
        "txid": m["evidence"]["r57"]["txid"],
        "tx_receipt": m["evidence"]["r57"]["receipt"],
        "rb57_state_sha256": m["evidence"]["r57"]["rb57_state_sha256"],
        "bindings": {k + "_sha256": v["sha256"] for k, v in resolved["bindings"].items() if k != "vm"},
        "worksets": {
            "train_source": resolved["worksets"]["train_source"]["artifact"],
            "dev": resolved["worksets"]["dev"]["artifact"],
            "core": resolved["worksets"]["core"]["artifact"],
            "behavior": behavior,
            "train_dev_split_receipt": resolved["split_receipt"],
        },
        "ownership": {
            "transformer_does_semantic_exam": True,
            "grounding_answers_for_model": False,
            "host_semantic_answer": False,
            "host_semantic_score": False,
        },
        "policy": m["policy"],
        "requested_runtime_action": resolved["runtime"]["action_id"],
        "max_steps": 10000000,
    }


def main():
    ap = argparse.ArgumentParser(description="Runnable, fail-closed SIGMA Gate B source-bound proof harness.")
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--run-root", default=None)
    args = ap.parse_args()

    try:
        resolved = validate_manifest(args.manifest)
    except ValidationError as e:
        print("HOLD=" + str(e))
        return 20

    base = args.run_root or os.path.join(os.path.expanduser("~"), "SIGMA_GATE_B_DEV_CORE_BEHAVIOR_PROOF")
    os.makedirs(base, mode=0o700, exist_ok=True)
    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + "_" + secrets.token_hex(8)
    run_dir = os.path.join(base, run_id)
    os.makedirs(run_dir, mode=0o700, exist_ok=False)

    input_path = os.path.join(run_dir, "gate_b_input.json")
    output_path = os.path.join(run_dir, "gate_b_native_receipt.json")
    stdout_path = os.path.join(run_dir, "runtime.stdout.log")
    stderr_path = os.path.join(run_dir, "runtime.stderr.log")
    summary_path = os.path.join(run_dir, "harness_summary.json")

    write_json(input_path, build_runtime_input(resolved, run_id))
    before = snapshot_bound_hashes(resolved)

    mapping = {
        "{VM}": resolved["bindings"]["vm"]["path"],
        "{BYTECODE}": resolved["bindings"]["unified_bytecode"]["path"],
        "{INPUT}": input_path,
        "{OUTPUT}": output_path,
        "{RUN_DIR}": run_dir,
        "{ACTION}": resolved["runtime"]["action_id"],
    }
    argv = [expand_arg(x, mapping) for x in resolved["runtime"]["argv"]]
    if argv[0] != resolved["bindings"]["vm"]["path"]:
        print("HOLD=RUNTIME_ARGV_VM_BINDING_BROKEN_AFTER_EXPANSION")
        return 21
    if resolved["bindings"]["unified_bytecode"]["path"] not in argv:
        print("HOLD=RUNTIME_ARGV_BYTECODE_BINDING_BROKEN_AFTER_EXPANSION")
        return 22

    env = os.environ.copy()
    env.update({
        "SIGMA_GATE_B_RUN_ID": run_id,
        "SIGMA_GATE_B_INPUT": input_path,
        "SIGMA_GATE_B_OUTPUT": output_path,
        "SIGMA_MAX_STEPS": "10000000",
        "SIGMA_LIVE_MUTATION": "NO",
        "SIGMA_SERVER_SEED": "NO",
        "SIGMA_ADMISSION": "NO",
        "SIGMA_CUTOVER": "NO",
        "SIGMA_FINAL": "NO",
        "SIGMA_RESERVE": "NO",
        "SIGMA_RETRAIN": "NO",
        "SIGMA_NEW_PROPOSAL": "NO",
        "SIGMA_HOST_SEMANTIC_ANSWER": "NO",
        "SIGMA_HOST_SEMANTIC_SCORE": "NO",
    })

    try:
        with open(stdout_path, "wb") as out, open(stderr_path, "wb") as err:
            proc = subprocess.run(argv, cwd=run_dir, env=env, stdin=subprocess.DEVNULL, stdout=out, stderr=err, shell=False)
    except OSError as e:
        print("HOLD=RUNTIME_EXEC_FAILED:%s" % e)
        return 23

    after = snapshot_bound_hashes(resolved)
    if before != after:
        print("HOLD=BOUND_INPUT_OR_SOURCE_MUTATED_DURING_RUN")
        return 24
    if proc.returncode != 0:
        print("HOLD=RUNTIME_RC_%d" % proc.returncode)
        return 25
    if not os.path.isfile(output_path) or os.path.getsize(output_path) <= 0:
        print("HOLD=NATIVE_RECEIPT_MISSING")
        return 26

    try:
        validate_receipt(output_path, resolved, run_id)
    except ValidationError as e:
        print("HOLD=" + str(e))
        return 27

    summary = {
        "schema": "SIGMA_GATE_B_DEV_CORE_BEHAVIOR_HARNESS_SUMMARY_V1",
        "run_id": run_id,
        "native_receipt_sha256": sha256_file(output_path),
        "runtime_stdout_sha256": sha256_file(stdout_path),
        "runtime_stderr_sha256": sha256_file(stderr_path),
        "gate_b_native_receipt_validated": True,
        "live_mutation": False,
        "server_seed": False,
        "admission": False,
        "cutover": False,
        "final": False,
        "reserve": False,
    }
    write_json(summary_path, summary)
    print("GATE_B_SOURCE_BOUND_HARNESS=VALIDATED_NATIVE_PASS")
    print("RUN_ID=" + run_id)
    print("RUN_DIR=" + run_dir)
    print("NATIVE_RECEIPT_SHA256=" + summary["native_receipt_sha256"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
