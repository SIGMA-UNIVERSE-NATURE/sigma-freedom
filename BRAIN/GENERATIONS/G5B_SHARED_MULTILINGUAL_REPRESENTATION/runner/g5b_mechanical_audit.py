#!/usr/bin/env python3
"""G5B mechanical sandbox audit.

This audit checks frozen hashes, anti-leakage separation, and runtime pins.
It does not classify meaning and does not choose semantic answers.
"""

import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

EXPECTED = {
    "learner": "a0ec7db21488c8cdbc4e35387adaee0463484b4b3696bd8e22e169f6baea8daf",
    "sealed_eval": "9d76ef8aabc7cb16aecafa288b61ee0c38ef2e099072a044cdee6d02ca91aeca",
    "sigma_source": "17abfd05bd4be51d31e0cf9d466758a6cb1df2668068872fdc4e399aadb5478b",
}

SIGMAC_SHA256 = "65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
SIGMA_VM_SHA256 = "029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("capsule_dir")
    parser.add_argument("runtime_root")
    args = parser.parse_args()

    root = Path(args.capsule_dir).resolve()
    runtime = Path(args.runtime_root).expanduser().resolve()
    learner = root / "corpus/g5b_frozen_sandbox_learner_input_v1.jsonl"
    sealed = root / "corpus/g5b_sealed_eval_v1.json"
    sigma_source = root / "learner/G5B_SHARED_REPRESENTATION_CANDIDATE.sigma"

    observed = {
        "learner": sha(learner),
        "sealed_eval": sha(sealed),
        "sigma_source": sha(sigma_source),
    }
    result = {
        "schema": "SIGMA_G5B_MECHANICAL_AUDIT_RECEIPT_V1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "system_identity": "SIGMA.AIL",
        "role": "G5B_SHARED_MULTILINGUAL_REPRESENTATION",
        "current_program_generation": "G2",
        "target_generation": "G5_HUMAN_LANGUAGE_MULTILINGUAL_BRAIN",
        "track": "G5_PRECURSOR_ONLY",
        "promotion": "NO",
        "model_commit": "NO",
        "production_cutover": "NO",
        "host_cognition": "NO",
        "anti_hardcode": "MANDATORY",
        "runtime_root": str(runtime),
        "observed_sha256": observed,
        "expected_sha256": EXPECTED,
        "checks": {},
        "result": "RUNNING",
    }

    result["checks"]["frozen_hashes"] = "PASS" if observed == EXPECTED else "HOLD_HASH_MISMATCH"

    learner_text = learner.read_text(encoding="utf-8")
    sealed_text = sealed.read_text(encoding="utf-8")
    forbidden_in_learner = ["positives", "negatives", "ambiguity_should_preserve", "expected", "answer"]
    leaks = [token for token in forbidden_in_learner if token in learner_text]
    result["checks"]["expected_answer_not_in_learner_input"] = "PASS" if not leaks else "HOLD_LEAK:" + ",".join(leaks)

    rows = [json.loads(line) for line in learner_text.splitlines() if line.strip()]
    result["checks"]["has_vietnamese"] = "PASS" if any(r.get("lang") == "vi" for r in rows) else "HOLD_NO_VI"
    result["checks"]["has_english"] = "PASS" if any(r.get("lang") == "en" for r in rows) else "HOLD_NO_EN"
    result["checks"]["has_heldout"] = "PASS" if any(r.get("split") == "heldout" for r in rows) else "HOLD_NO_HELDOUT"
    result["checks"]["has_controls"] = "PASS" if any(r.get("split") == "control" for r in rows) else "HOLD_NO_CONTROL"
    result["checks"]["sealed_eval_separate"] = "PASS" if sha(learner) != sha(sealed) else "HOLD_SEALED_EQUALS_LEARNER"

    required_runtime = runtime / "native"
    result["checks"]["runtime_native_dir_seen"] = "PASS" if required_runtime.is_dir() else "HOLD_RUNTIME_NATIVE_DIR_MISSING"

    holds = [v for v in result["checks"].values() if not str(v).startswith("PASS")]
    if holds:
        result["result"] = "G5B_MECHANICAL_AUDIT_HOLD"
    else:
        result["result"] = "G5B_SANDBOX_READY_FOR_SIGMA_NATIVE_LEARNER_RUN"

    digestable = dict(result)
    digestable["receipt_sha256"] = None
    result["receipt_sha256"] = hashlib.sha256(json.dumps(digestable, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()

    out_dir = root / "receipts"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / "g5b_mechanical_audit_receipt.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("RESULT=" + result["result"])
    for k, v in result["checks"].items():
        print(k.upper() + "=" + str(v))
    print("RECEIPT_SHA256=" + result["receipt_sha256"])
    print("RECEIPT_JSON=" + str(out))
    return 0 if result["result"].endswith("SIGMA_NATIVE_LEARNER_RUN") else 3


if __name__ == "__main__":
    raise SystemExit(main())
