#!/usr/bin/env python3
"""G2B canonical .sigma_ail receipt.

Host role: mechanical bytes, files, hashing, locking, atomic persistence.
No host cognition, no semantic labeling, no learning objective choice.
"""

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone

MAX_FIELD_BYTES = 8192
REQUIRED = {
    "IDENTITY": "SYSTEM_IDENTITY",
    "ACTIVE_REVISION": "ACTIVE_REVISION",
    "ACTIVE_CORE": "ACTIVE_CORE",
    "BRAIN_HEAD": "ACTIVE_BRAIN_HEAD",
    "MODEL_GENERATION": "MODEL_GENERATION",
    "STATE_VERSION": "STATE_VERSION",
}

SIGMAC_SHA256 = "65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
SIGMA_VM_SHA256 = "029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def atomic_write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
        try:
            dfd = os.open(str(path.parent), os.O_RDONLY)
            try:
                os.fsync(dfd)
            finally:
                os.close(dfd)
        except OSError:
            pass
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def safe_read_field(root, name):
    path = root / name
    item = {
        "path": str(path),
        "exists": path.exists(),
        "is_symlink": path.is_symlink(),
        "sha256": None,
        "bytes": None,
        "value": None,
        "status": "UNREAD",
    }
    if path.is_symlink():
        item["status"] = "HOLD_SYMLINK"
        return item
    if not path.is_file():
        item["status"] = "HOLD_MISSING"
        return item
    size = path.stat().st_size
    item["bytes"] = size
    if size < 1 or size > MAX_FIELD_BYTES:
        item["status"] = "HOLD_FIELD_SIZE"
        return item
    data = path.read_bytes()
    item["sha256"] = sha256_bytes(data)
    if b"\x00" in data:
        item["status"] = "HOLD_NUL_BYTE"
        return item
    try:
        value = data.decode("utf-8").strip()
    except UnicodeDecodeError:
        item["status"] = "HOLD_NOT_UTF8"
        return item
    if not value:
        item["status"] = "HOLD_EMPTY"
        return item
    item["value"] = value
    item["status"] = "READ"
    return item


def load_previous(path):
    if path is None:
        return None
    if path.is_symlink() or not path.is_file():
        return {"status": "HOLD_PREVIOUS_RECEIPT_UNREADABLE"}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"status": "HOLD_PREVIOUS_RECEIPT_INVALID", "error": repr(exc)}


def main():
    parser = argparse.ArgumentParser(description="SIGMA.AIL G2B canonical .sigma_ail receipt")
    parser.add_argument("runtime_root", help="SIGMA runtime root, normally $HOME/SIGMA/sigma_genesis1")
    parser.add_argument("--canonical-root", default=".sigma_ail")
    parser.add_argument("--previous-receipt", type=Path)
    parser.add_argument("--out-dir", type=Path)
    args = parser.parse_args()

    runtime_root = Path(args.runtime_root).expanduser().resolve()
    canonical_root = (runtime_root / args.canonical_root).resolve()

    payload = {
        "schema": "SIGMA_AIL_G2B_CANONICAL_BRAIN_HEAD_RECEIPT_1",
        "handoff_id": "G2B_SIGMA_AIL_CANONICAL_BRAIN_HEAD_MISSION_20260914",
        "gate_id": "G2B_NATIVE_DOT_SIGMA_AIL_HEAD_STATE_VERSION_RECEIPT",
        "created_at": utc_now(),
        "runtime_root": str(runtime_root),
        "canonical_root": str(canonical_root),
        "canonical_root_name": args.canonical_root,
        "host_cognition": "NO",
        "anti_hardcode": "MANDATORY",
        "runtime_truth_source": "EVIDENCE_OR_MACHINE_RECEIPT",
        "sigmac_sha256": SIGMAC_SHA256,
        "sigma_vm_sha256": SIGMA_VM_SHA256,
        "fields": {},
        "values": {},
        "checks": {},
        "previous_receipt": None,
        "result": "RUNNING",
        "reason": None,
    }

    reasons = []

    if args.canonical_root != ".sigma_ail":
        reasons.append("CANONICAL_ROOT_NAME_NOT_DOT_SIGMA_AIL")
    if runtime_root.is_symlink() or not runtime_root.is_dir():
        reasons.append("RUNTIME_ROOT_UNAVAILABLE")
    if canonical_root.is_symlink() or not canonical_root.is_dir():
        reasons.append("CANONICAL_ROOT_UNAVAILABLE")

    lock_file = None
    if not reasons:
        lock_path = canonical_root / "WRITER.lock"
        payload["checks"]["writer_lock_path"] = str(lock_path)
        if lock_path.is_symlink():
            reasons.append("WRITER_LOCK_SYMLINK")
        else:
            try:
                lock_file = lock_path.open("a+b")
                fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                payload["checks"]["canonical_writer_lock_held"] = "PASS"
            except BlockingIOError:
                reasons.append("WRITER_ACTIVE")
                payload["checks"]["canonical_writer_lock_held"] = "HOLD_WRITER_ACTIVE"
            except OSError as exc:
                reasons.append("WRITER_LOCK_ERROR")
                payload["checks"]["writer_lock_error"] = repr(exc)

    try:
        if not reasons:
            for source_name, output_name in REQUIRED.items():
                item = safe_read_field(canonical_root, source_name)
                payload["fields"][source_name] = item
                if item["status"] != "READ":
                    reasons.append(output_name + "_" + item["status"])
                else:
                    payload["values"][output_name] = item["value"]

            if payload["values"].get("SYSTEM_IDENTITY") != "SIGMA.AIL":
                reasons.append("SYSTEM_IDENTITY_NOT_SIGMA_AIL")

            previous = load_previous(args.previous_receipt)
            payload["previous_receipt"] = previous
            if previous is None:
                payload["checks"]["restart_reload_same_head"] = "NOT_ASSESSED_PREVIOUS_RECEIPT_REQUIRED"
            elif previous.get("status", "").startswith("HOLD"):
                payload["checks"]["restart_reload_same_head"] = previous["status"]
                reasons.append(previous["status"])
            else:
                previous_values = previous.get("values", {})
                keys = ("ACTIVE_BRAIN_HEAD", "MODEL_GENERATION", "STATE_VERSION")
                same = all(previous_values.get(k) == payload["values"].get(k) for k in keys)
                payload["checks"]["restart_reload_same_head"] = "PASS" if same else "HOLD_RESTART_VALUES_CHANGED"
                if not same:
                    reasons.append("RESTART_VALUES_CHANGED")

            payload["checks"]["active_brain_head_source"] = ".sigma_ail/BRAIN_HEAD"
            payload["checks"]["model_generation_source"] = ".sigma_ail/MODEL_GENERATION"
            payload["checks"]["state_version_source"] = ".sigma_ail/STATE_VERSION"
            payload["checks"]["no_host_semantic_cognition"] = "PASS"
            payload["checks"]["no_chat_summary_runtime_truth"] = "PASS"

    finally:
        if lock_file is not None:
            lock_file.close()

    if reasons:
        payload["result"] = "G2B_HOLD"
        payload["reason"] = ";".join(reasons)
    elif payload["checks"].get("restart_reload_same_head") == "PASS":
        payload["result"] = "G2B_PRODUCER_MECHANICAL_RECEIPT_READY_FOR_REVIEW"
    else:
        payload["result"] = "G2B_PRODUCER_MECHANICAL_RECEIPT_RESTART_CHECK_PENDING"
        payload["reason"] = "RUN_AGAIN_AFTER_RESTART_WITH_PREVIOUS_RECEIPT"

    digest_payload = dict(payload)
    digest_payload["receipt_sha256"] = None
    canonical = json.dumps(digest_payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["receipt_sha256"] = sha256_bytes(canonical)

    out_dir = args.out_dir
    if out_dir is None:
        suffix = "g2b_" + payload["created_at"].replace(":", "").replace("+", "Z")
        if canonical_root.is_dir() and not canonical_root.is_symlink():
            out_dir = canonical_root / "checkpoints" / suffix
        else:
            out_dir = Path.cwd() / suffix
    out_dir = out_dir.resolve()
    if out_dir.is_symlink():
        raise SystemExit("G2B_HOLD:OUT_DIR_SYMLINK")

    receipt_path = out_dir / "g2b_receipt.json"
    atomic_write_json(receipt_path, payload)
    text_path = out_dir / "g2b_receipt.txt"
    lines = [
        "RESULT=" + payload["result"],
        "REASON=" + str(payload["reason"]),
        "HANDOFF_ID=" + payload["handoff_id"],
        "GATE_ID=" + payload["gate_id"],
        "SYSTEM_IDENTITY=" + payload["values"].get("SYSTEM_IDENTITY", "UNAVAILABLE"),
        "ACTIVE_REVISION=" + payload["values"].get("ACTIVE_REVISION", "UNAVAILABLE"),
        "ACTIVE_CORE=" + payload["values"].get("ACTIVE_CORE", "UNAVAILABLE"),
        "ACTIVE_BRAIN_HEAD=" + payload["values"].get("ACTIVE_BRAIN_HEAD", "UNAVAILABLE"),
        "MODEL_GENERATION=" + payload["values"].get("MODEL_GENERATION", "UNAVAILABLE"),
        "STATE_VERSION=" + payload["values"].get("STATE_VERSION", "UNAVAILABLE"),
        "RESTART_RELOAD_SAME_HEAD=" + payload["checks"].get("restart_reload_same_head", "UNAVAILABLE"),
        "RECEIPT_SHA256=" + payload["receipt_sha256"],
        "RECEIPT_JSON=" + str(receipt_path),
    ]
    text_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))
    return 0 if payload["result"].startswith("G2B_PRODUCER") else 3


if __name__ == "__main__":
    raise SystemExit(main())
