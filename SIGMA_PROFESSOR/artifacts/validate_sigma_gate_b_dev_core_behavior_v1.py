#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

SCHEMA_MANIFEST = "SIGMA_GATE_B_DEV_CORE_BEHAVIOR_PREREQUISITES_V1"
SCHEMA_SPLIT = "SIGMA_GATE_B_TRAIN_DEV_SPLIT_RECEIPT_V1"
SCHEMA_RECEIPT = "SIGMA_GATE_B_DEV_CORE_BEHAVIOR_NATIVE_RECEIPT_V1"

EXPECTED = {
    "gate_a_anchor_commit": "2475befc0261217fea910284b1035fcbfeda0627",
    "behavior_eval_commit": "289f597188e6028988ed972842dca9e262ef6edb",
    "sigma_life_observed_commit": "a789793f43513f62ca6806ad46bf27ca3fce02d9",
    "one_sigma_identity": "c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222",
    "parent_model": "2be5bedf284e4c304547510063a32726",
    "child_model": "12cc5d5d11c7054d727c78284d00ca3f",
    "parent_opt": "744330c0193d97100c0f6f452ba7b510",
    "child_opt": "6b219217402bfcf15d583f37645b9fcb",
    "txid": "3bccae2e73d5ae807f69869d4fefad05",
    "receipt": "4262d090265757d74ac5d9772e648859",
    "tx_proposal_sha256": "853f71e7b3320c1549f6435bbf285fd271b7da74f35cbc00d5cd985dffbddea4",
    "rb57_state_sha256": "591c936b61cae15c2cd443a70aadd0078bfc34a0273da5d5a0af264fb8a69a04",
    "module97_sha256": "90baaf5f358dc62bea1318a7b3f12e958215210b1d72a1c3d68df11be3cad584",
    "module98_sha256": "75abe2dc57241f3aea6f79352616138d97b77a733a33a74d56dc890ff0477ce8",
    "unified_source_sha256": "93a9eb672f1ba0dad6617fcf6e49b3c98449ec9e0210f620739a1dcd9fa3ce57",
    "unified_bytecode_sha256": "b7fa471631b9ad9bad23335f0b5f356c40c1199375cc946e7bd9df24072eb469",
}

POLICY_FALSE_KEYS = (
    "live_mutation",
    "server_seed",
    "admission",
    "cutover",
    "final",
    "reserve",
    "retrain",
    "new_proposal",
    "host_semantic_answer",
    "host_semantic_score",
)

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
UNBOUND_MARKERS = ("<", "UNBOUND", "TODO", "UNKNOWN", "PENDING", "REQUIRED")
ALLOWED_ARG_PLACEHOLDERS = {"{VM}", "{BYTECODE}", "{INPUT}", "{OUTPUT}", "{RUN_DIR}", "{ACTION}"}


class ValidationError(Exception):
    pass


def fail(message):
    raise ValidationError(message)


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        fail("FILE_MISSING:" + str(path))
    except json.JSONDecodeError as e:
        fail("JSON_INVALID:%s:%s" % (path, e))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_bound_string(value):
    if not isinstance(value, str):
        return False
    s = value.strip()
    if not s:
        return False
    up = s.upper()
    return not any(marker in up for marker in UNBOUND_MARKERS)


def require_equal(actual, expected, label):
    if actual != expected:
        fail("%s_MISMATCH" % label)


def require_false_map(obj, label):
    if not isinstance(obj, dict):
        fail(label + "_MISSING")
    for key in POLICY_FALSE_KEYS:
        if obj.get(key) is not False:
            fail("%s_%s_NOT_FALSE" % (label, key.upper()))


def normalize_path(value, label):
    if not is_bound_string(value):
        fail(label + "_UNBOUND")
    path = os.path.expandvars(os.path.expanduser(value))
    if not os.path.isabs(path):
        fail(label + "_NOT_ABSOLUTE")
    if not os.path.isfile(path):
        fail(label + "_FILE_MISSING")
    if os.path.getsize(path) <= 0:
        fail(label + "_EMPTY")
    return os.path.realpath(path)


def validate_sha(value, label):
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        fail(label + "_SHA256_UNBOUND_OR_INVALID")
    return value


def validate_binding(binding, label, expected_sha=None):
    if not isinstance(binding, dict):
        fail(label + "_BINDING_MISSING")
    path = normalize_path(binding.get("path"), label + "_PATH")
    expected = validate_sha(binding.get("sha256"), label)
    if expected_sha is not None and expected != expected_sha:
        fail(label + "_EXPECTED_SHA256_MISMATCH")
    actual = sha256_file(path)
    if actual != expected:
        fail(label + "_CONTENT_SHA256_MISMATCH")
    return {"path": path, "sha256": actual}


def validate_provenance_pair(entry, label):
    primary = validate_binding(entry, label)
    prov = validate_binding(
        {"path": entry.get("provenance_path"), "sha256": entry.get("provenance_sha256")},
        label + "_PROVENANCE",
    )
    return {"artifact": primary, "provenance": prov}


def validate_split_receipt(manifest, train_binding, dev_binding, split_builder_binding):
    split = manifest.get("train_dev_split")
    if not isinstance(split, dict):
        fail("TRAIN_DEV_SPLIT_MISSING")
    rec_binding = validate_binding(split.get("receipt"), "TRAIN_DEV_SPLIT_RECEIPT")
    rec = load_json(rec_binding["path"])
    require_equal(rec.get("schema"), SCHEMA_SPLIT, "TRAIN_DEV_SPLIT_SCHEMA")
    if rec.get("source_bound") is not True:
        fail("TRAIN_DEV_SPLIT_SOURCE_BOUND_NOT_TRUE")
    if rec.get("disjoint") is not True:
        fail("TRAIN_DEV_SPLIT_DISJOINT_NOT_TRUE")
    if rec.get("host_semantic_selection") is not False:
        fail("TRAIN_DEV_SPLIT_HOST_SEMANTIC_SELECTION_NOT_FALSE")
    require_equal(rec.get("train_sha256"), train_binding["sha256"], "TRAIN_DEV_SPLIT_TRAIN_SHA256")
    require_equal(rec.get("dev_sha256"), dev_binding["sha256"], "TRAIN_DEV_SPLIT_DEV_SHA256")
    require_equal(
        rec.get("builder_source_sha256"), split_builder_binding["sha256"], "TRAIN_DEV_SPLIT_BUILDER_SHA256"
    )
    return rec_binding


def read_text(path, label):
    try:
        return Path(path).read_text(encoding="utf-8", errors="strict")
    except UnicodeDecodeError:
        fail(label + "_NOT_UTF8_TEXT")


def validate_runtime(manifest, bindings, module_text):
    runtime = manifest.get("runtime")
    if not isinstance(runtime, dict):
        fail("RUNTIME_MISSING")
    require_equal(runtime.get("max_steps"), 10000000, "RUNTIME_MAX_STEPS")
    action = runtime.get("action_id")
    if not is_bound_string(action):
        fail("RUNTIME_ACTION_ID_UNBOUND")
    if action not in module_text:
        fail("RUNTIME_ACTION_ID_NOT_SOURCE_BOUND")
    argv = runtime.get("argv")
    if not isinstance(argv, list) or not argv or not all(isinstance(x, str) and x for x in argv):
        fail("RUNTIME_ARGV_UNBOUND")
    joined = "\n".join(argv)
    for token in ("{VM}", "{BYTECODE}", "{INPUT}", "{OUTPUT}", "{ACTION}"):
        if token not in joined:
            fail("RUNTIME_ARGV_MISSING_" + token.strip("{}").upper())
    for item in argv:
        for match in re.findall(r"\{[A-Z_]+\}", item):
            if match not in ALLOWED_ARG_PLACEHOLDERS:
                fail("RUNTIME_ARGV_UNKNOWN_PLACEHOLDER:" + match)
    if argv[0] != "{VM}":
        fail("RUNTIME_ARGV_FIRST_ARG_MUST_BE_VM")
    if runtime.get("shell") is not False:
        fail("RUNTIME_SHELL_MUST_BE_FALSE")
    return {"action_id": action, "argv": argv}


def validate_manifest(manifest_path):
    manifest = load_json(manifest_path)
    require_equal(manifest.get("schema"), SCHEMA_MANIFEST, "MANIFEST_SCHEMA")

    evidence = manifest.get("evidence")
    if not isinstance(evidence, dict):
        fail("EVIDENCE_MISSING")
    for key in ("gate_a_anchor_commit", "behavior_eval_commit", "sigma_life_observed_commit", "one_sigma_identity"):
        require_equal(evidence.get(key), EXPECTED[key], "EVIDENCE_" + key.upper())
    require_equal(evidence.get("gate_a_decision"), "GATE_A_TINY_DATA_DRIVEN_PASS", "EVIDENCE_GATE_A_DECISION")
    if evidence.get("train_decision") not in ("TRAIN_IMPROVES_DATA_PRESENT", "TRAIN_IMPROVES_YES"):
        fail("EVIDENCE_TRAIN_DECISION_INVALID")

    r57 = evidence.get("r57")
    if not isinstance(r57, dict):
        fail("R57_EVIDENCE_MISSING")
    for key in ("parent_model", "child_model", "parent_opt", "child_opt", "txid", "receipt", "tx_proposal_sha256", "rb57_state_sha256"):
        require_equal(r57.get(key), EXPECTED[key], "R57_" + key.upper())
    require_equal(r57.get("model_generation"), 1, "R57_MODEL_GENERATION")
    require_equal(r57.get("opt_step"), 1, "R57_OPT_STEP")

    require_false_map(manifest.get("policy"), "POLICY")

    raw_bindings = manifest.get("bindings")
    if not isinstance(raw_bindings, dict):
        fail("BINDINGS_MISSING")
    bindings = {}
    bindings["vm"] = validate_binding(raw_bindings.get("vm"), "VM")
    bindings["unified_source"] = validate_binding(
        raw_bindings.get("unified_source"), "UNIFIED_SOURCE", EXPECTED["unified_source_sha256"]
    )
    bindings["unified_bytecode"] = validate_binding(
        raw_bindings.get("unified_bytecode"), "UNIFIED_BYTECODE", EXPECTED["unified_bytecode_sha256"]
    )
    bindings["module97"] = validate_binding(raw_bindings.get("module97"), "MODULE97", EXPECTED["module97_sha256"])
    bindings["module98"] = validate_binding(raw_bindings.get("module98"), "MODULE98", EXPECTED["module98_sha256"])
    bindings["module99"] = validate_binding(raw_bindings.get("module99"), "MODULE99")

    module_text = "\n".join(
        read_text(bindings[k]["path"], k.upper()) for k in ("module97", "module98", "module99")
    )

    worksets = manifest.get("worksets")
    if not isinstance(worksets, dict):
        fail("WORKSETS_MISSING")
    train = validate_provenance_pair(worksets.get("train_source") or {}, "TRAIN_SOURCE")
    dev = validate_provenance_pair(worksets.get("dev") or {}, "DEV_WORKSET")
    core = validate_provenance_pair(worksets.get("core") or {}, "CORE_WORKSET")
    if train["artifact"]["sha256"] == dev["artifact"]["sha256"]:
        fail("TRAIN_DEV_ARTIFACT_SHA256_EQUAL")
    if dev["artifact"]["sha256"] == core["artifact"]["sha256"]:
        fail("DEV_CORE_ARTIFACT_SHA256_EQUAL")

    split_builder = validate_binding((manifest.get("train_dev_split") or {}).get("builder_source"), "TRAIN_DEV_SPLIT_BUILDER")
    split_receipt = validate_split_receipt(manifest, train["artifact"], dev["artifact"], split_builder)

    behavior = worksets.get("behavior")
    if not isinstance(behavior, list) or len(behavior) != 6:
        fail("BEHAVIOR_WORKSET_COUNT_NOT_6")
    seen_caps = set()
    behavior_resolved = []
    for idx, item in enumerate(behavior, 1):
        if not isinstance(item, dict):
            fail("BEHAVIOR_%d_INVALID" % idx)
        cap = item.get("capability_id")
        if not is_bound_string(cap):
            fail("BEHAVIOR_%d_CAPABILITY_ID_UNBOUND" % idx)
        if cap in seen_caps:
            fail("BEHAVIOR_CAPABILITY_ID_DUPLICATE:" + cap)
        if cap not in module_text:
            fail("BEHAVIOR_CAPABILITY_ID_NOT_SOURCE_BOUND:" + cap)
        seen_caps.add(cap)
        pair = validate_provenance_pair(item, "BEHAVIOR_%d_WORKSET" % idx)
        behavior_resolved.append({"capability_id": cap, **pair})

    runtime = validate_runtime(manifest, bindings, module_text)

    return {
        "manifest": manifest,
        "manifest_path": os.path.realpath(manifest_path),
        "bindings": bindings,
        "worksets": {"train_source": train, "dev": dev, "core": core, "behavior": behavior_resolved},
        "split_builder": split_builder,
        "split_receipt": split_receipt,
        "runtime": runtime,
    }


def validate_receipt(receipt_path, resolved, run_id):
    receipt = load_json(receipt_path)
    require_equal(receipt.get("schema"), SCHEMA_RECEIPT, "RECEIPT_SCHEMA")
    require_equal(receipt.get("run_id"), run_id, "RECEIPT_RUN_ID")
    require_equal(receipt.get("proof_scope"), "TINY", "RECEIPT_PROOF_SCOPE")

    evidence = resolved["manifest"]["evidence"]
    r57 = evidence["r57"]
    require_equal(receipt.get("model_ref"), r57["child_model"], "RECEIPT_MODEL_REF")
    require_equal(receipt.get("parent_model_ref"), r57["parent_model"], "RECEIPT_PARENT_MODEL_REF")
    require_equal(receipt.get("txid"), r57["txid"], "RECEIPT_TXID")
    require_equal(receipt.get("tx_receipt"), r57["receipt"], "RECEIPT_TX_RECEIPT")
    require_equal(receipt.get("rb57_state_sha256"), r57["rb57_state_sha256"], "RECEIPT_RB57_STATE_SHA256")

    ownership = receipt.get("ownership")
    if not isinstance(ownership, dict):
        fail("RECEIPT_OWNERSHIP_MISSING")
    if ownership.get("transformer_does_semantic_exam") is not True:
        fail("RECEIPT_TRANSFORMER_SEMANTIC_EXAM_NOT_TRUE")
    for key in ("grounding_answers_for_model", "host_semantic_answer", "host_semantic_score"):
        if ownership.get(key) is not False:
            fail("RECEIPT_OWNERSHIP_%s_NOT_FALSE" % key.upper())

    require_false_map(receipt.get("policy"), "RECEIPT_POLICY")

    rb = receipt.get("bindings")
    if not isinstance(rb, dict):
        fail("RECEIPT_BINDINGS_MISSING")
    for key in ("unified_source", "unified_bytecode", "module97", "module98", "module99"):
        require_equal(rb.get(key + "_sha256"), resolved["bindings"][key]["sha256"], "RECEIPT_BINDING_" + key.upper())
    require_equal(rb.get("train_source_sha256"), resolved["worksets"]["train_source"]["artifact"]["sha256"], "RECEIPT_TRAIN_SHA256")
    require_equal(rb.get("dev_workset_sha256"), resolved["worksets"]["dev"]["artifact"]["sha256"], "RECEIPT_DEV_SHA256")
    require_equal(rb.get("core_workset_sha256"), resolved["worksets"]["core"]["artifact"]["sha256"], "RECEIPT_CORE_SHA256")
    require_equal(rb.get("train_dev_split_receipt_sha256"), resolved["split_receipt"]["sha256"], "RECEIPT_SPLIT_RECEIPT_SHA256")

    gates = receipt.get("gates")
    if not isinstance(gates, dict):
        fail("RECEIPT_GATES_MISSING")
    dev = gates.get("dev")
    if not isinstance(dev, dict) or dev.get("source_bound") is not True or dev.get("held_out") is not True or dev.get("decision") != "PASS":
        fail("RECEIPT_DEV_GATE_NOT_PASS_SOURCE_BOUND_HELD_OUT")
    core = gates.get("core")
    if not isinstance(core, dict) or core.get("source_bound") is not True or core.get("no_regression") is not True or core.get("decision") != "PASS":
        fail("RECEIPT_CORE_GATE_NOT_PASS_SOURCE_BOUND_NO_REGRESSION")
    behavior = gates.get("behavior")
    if not isinstance(behavior, dict):
        fail("RECEIPT_BEHAVIOR_GATE_MISSING")
    if behavior.get("source_bound") is not True or behavior.get("decision") != "PASS" or behavior.get("capability_count") != 6:
        fail("RECEIPT_BEHAVIOR_GATE_NOT_PASS_SOURCE_BOUND_6")
    results = behavior.get("capabilities")
    if not isinstance(results, list) or len(results) != 6:
        fail("RECEIPT_BEHAVIOR_CAPABILITY_RESULT_COUNT_NOT_6")
    expected_caps = {x["capability_id"]: x["artifact"]["sha256"] for x in resolved["worksets"]["behavior"]}
    seen = set()
    for item in results:
        if not isinstance(item, dict):
            fail("RECEIPT_BEHAVIOR_CAPABILITY_RESULT_INVALID")
        cap = item.get("capability_id")
        if cap not in expected_caps or cap in seen:
            fail("RECEIPT_BEHAVIOR_CAPABILITY_ID_INVALID_OR_DUPLICATE")
        seen.add(cap)
        require_equal(item.get("workset_sha256"), expected_caps[cap], "RECEIPT_BEHAVIOR_WORKSET_SHA256")
        if item.get("decision") != "PASS":
            fail("RECEIPT_BEHAVIOR_CAPABILITY_NOT_PASS:" + cap)
    if seen != set(expected_caps):
        fail("RECEIPT_BEHAVIOR_CAPABILITY_SET_MISMATCH")
    if receipt.get("gate_b_decision") != "PASS":
        fail("RECEIPT_GATE_B_DECISION_NOT_PASS")
    return receipt


def cli():
    p = argparse.ArgumentParser(description="Fail-closed validator for SIGMA Gate B source-bound DEV/CORE/behavior proof.")
    sub = p.add_subparsers(dest="cmd", required=True)
    p_manifest = sub.add_parser("manifest")
    p_manifest.add_argument("manifest")
    p_receipt = sub.add_parser("receipt")
    p_receipt.add_argument("manifest")
    p_receipt.add_argument("receipt")
    p_receipt.add_argument("--run-id", required=True)
    args = p.parse_args()
    try:
        resolved = validate_manifest(args.manifest)
        if args.cmd == "manifest":
            print("MANIFEST_BINDING=VALID")
            return 0
        validate_receipt(args.receipt, resolved, args.run_id)
        print("NATIVE_RECEIPT_BINDING=VALID")
        return 0
    except ValidationError as e:
        print("HOLD=" + str(e))
        return 20


if __name__ == "__main__":
    sys.exit(cli())
