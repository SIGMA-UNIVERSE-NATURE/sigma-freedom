#!/usr/bin/env python3
"""Bind canonical .sigma_ail to the current R3 head under mechanical locks.

Host role: file bytes, locks, hashing, atomic persistence. No host cognition.
"""

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone

SIGMAC_SHA256 = "65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
SIGMA_VM_SHA256 = "029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
DEFAULT_CORE = "SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1"
DEFAULT_EXEC = "SIGMA_INTEGRAL_OWNER_R3"


def now():
    return datetime.now(timezone.utc).isoformat()


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def read_text_file(path, limit=8192):
    item = {
        "path": str(path),
        "exists": path.exists(),
        "is_symlink": path.is_symlink(),
        "bytes": None,
        "sha256": None,
        "value": None,
        "status": "UNREAD",
    }
    if path.is_symlink():
        item["status"] = "HOLD_SYMLINK"
        return item
    if not path.is_file():
        item["status"] = "HOLD_MISSING"
        return item
    data = path.read_bytes()
    item["bytes"] = len(data)
    item["sha256"] = sha_bytes(data)
    if len(data) < 1 or len(data) > limit:
        item["status"] = "HOLD_SIZE"
        return item
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


def atomic_text(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(value)
            if not value.endswith("\n"):
                stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, path)
        try:
            dfd = os.open(str(path.parent), os.O_RDONLY)
            try:
                os.fsync(dfd)
            finally:
                os.close(dfd)
        except OSError:
            pass
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def atomic_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, path)
        try:
            dfd = os.open(str(path.parent), os.O_RDONLY)
            try:
                os.fsync(dfd)
            finally:
                os.close(dfd)
        except OSError:
            pass
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def open_lock(path):
    if path.is_symlink():
        raise RuntimeError("LOCK_SYMLINK:" + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.open("a+b")
    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    return lock


def main():
    parser = argparse.ArgumentParser(description="G2B bind .sigma_ail to active R3 head")
    parser.add_argument("runtime_root")
    parser.add_argument("--active-core", default=DEFAULT_CORE)
    parser.add_argument("--exec-name", default=DEFAULT_EXEC)
    parser.add_argument("--model-generation", default="0")
    parser.add_argument("--state-version", default=None)
    parser.add_argument("--out-dir", type=Path)
    args = parser.parse_args()

    runtime_root = Path(args.runtime_root).expanduser().resolve()
    legacy_root = runtime_root / args.active_core
    legacy_workspace = legacy_root / "workspace"
    legacy_state = legacy_workspace / "work" / ".sigma_exec" / args.exec_name / "state"
    legacy_head = legacy_state / "HEAD"
    canonical = runtime_root / ".sigma_ail"

    receipt = {
        "schema": "SIGMA_AIL_G2B_CANONICAL_BIND_RECEIPT_1",
        "handoff_id": "G2B_SIGMA_AIL_CANONICAL_BIND_T27_20260915",
        "gate_id": "G2B_BIND_CANONICAL_DOT_SIGMA_AIL_UNDER_LOCK",
        "created_at": now(),
        "runtime_root": str(runtime_root),
        "legacy_writer_lock": str(legacy_workspace / "writer.lock"),
        "canonical_root": str(canonical),
        "legacy_head": str(legacy_head),
        "host_cognition": "NO",
        "anti_hardcode": "MANDATORY",
        "runtime_truth_source": "EVIDENCE_OR_MACHINE_RECEIPT",
        "sigmac_sha256": SIGMAC_SHA256,
        "sigma_vm_sha256": SIGMA_VM_SHA256,
        "values": {},
        "checks": {},
        "result": "RUNNING",
        "reason": None,
    }
    reasons = []
    locks = []

    try:
        if runtime_root.is_symlink() or not runtime_root.is_dir():
            reasons.append("RUNTIME_ROOT_UNAVAILABLE")
        if legacy_workspace.is_symlink() or not legacy_workspace.is_dir():
            reasons.append("LEGACY_WORKSPACE_UNAVAILABLE")
        if canonical.exists() and (canonical.is_symlink() or not canonical.is_dir()):
            reasons.append("CANONICAL_ROOT_NOT_DIRECTORY")
        if not reasons:
            try:
                locks.append(open_lock(legacy_workspace / "writer.lock"))
                receipt["checks"]["legacy_writer_lock_held"] = "PASS"
            except BlockingIOError:
                reasons.append("LEGACY_WRITER_ACTIVE")
                receipt["checks"]["legacy_writer_lock_held"] = "HOLD_LEGACY_WRITER_ACTIVE"
            except OSError as exc:
                reasons.append("LEGACY_WRITER_LOCK_ERROR")
                receipt["checks"]["legacy_writer_lock_error"] = repr(exc)

        if not reasons:
            canonical.mkdir(mode=0o700, exist_ok=True)
            try:
                locks.append(open_lock(canonical / "WRITER.lock"))
                receipt["checks"]["canonical_writer_lock_held"] = "PASS"
            except BlockingIOError:
                reasons.append("CANONICAL_WRITER_ACTIVE")
                receipt["checks"]["canonical_writer_lock_held"] = "HOLD_CANONICAL_WRITER_ACTIVE"
            except OSError as exc:
                reasons.append("CANONICAL_WRITER_LOCK_ERROR")
                receipt["checks"]["canonical_writer_lock_error"] = repr(exc)

        if not reasons:
            head = read_text_file(legacy_head, limit=128)
            receipt["checks"]["legacy_head"] = head
            if head["status"] != "READ":
                reasons.append("LEGACY_HEAD_" + head["status"])
            elif len(head["value"]) != 32:
                reasons.append("LEGACY_HEAD_NOT_32_HEX_CHARS")
            else:
                int(head["value"], 16)
                state_version = args.state_version
                previous_state_version = read_text_file(canonical / "STATE_VERSION", limit=128)
                receipt["checks"]["previous_state_version"] = previous_state_version
                if state_version is None:
                    if previous_state_version["status"] == "READ" and previous_state_version["value"].isdigit():
                        state_version = str(int(previous_state_version["value"]) + 1)
                    else:
                        state_version = "1"

                values = {
                    "IDENTITY": "SIGMA.AIL",
                    "ACTIVE_REVISION": "R3",
                    "ACTIVE_CORE": args.active_core,
                    "BRAIN_HEAD": head["value"],
                    "MODEL_GENERATION": args.model_generation,
                    "STATE_VERSION": state_version,
                }
                for name, value in values.items():
                    atomic_text(canonical / name, value)
                receipt["values"] = {
                    "SYSTEM_IDENTITY": values["IDENTITY"],
                    "ACTIVE_REVISION": values["ACTIVE_REVISION"],
                    "ACTIVE_CORE": values["ACTIVE_CORE"],
                    "ACTIVE_BRAIN_HEAD": values["BRAIN_HEAD"],
                    "MODEL_GENERATION": values["MODEL_GENERATION"],
                    "STATE_VERSION": values["STATE_VERSION"],
                }
                receipt["checks"]["active_brain_head_source"] = str(legacy_head)
                receipt["checks"]["model_generation_policy"] = "CONSERVATIVE_G1_INITIAL_ZERO_UNLESS_OVERRIDE"
                receipt["checks"]["state_version_policy"] = "INITIAL_ONE_OR_INCREMENT_EXISTING"

    except ValueError:
        reasons.append("LEGACY_HEAD_NOT_HEX")
    finally:
        for lock in reversed(locks):
            lock.close()

    if reasons:
        receipt["result"] = "G2B_BIND_HOLD"
        receipt["reason"] = ";".join(reasons)
    else:
        receipt["result"] = "G2B_BIND_PRODUCER_RECEIPT_READY_FOR_REVIEW"

    digest = dict(receipt)
    digest["receipt_sha256"] = None
    receipt["receipt_sha256"] = sha_bytes(json.dumps(digest, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))

    suffix = "g2b_bind_" + receipt["created_at"].replace(":", "").replace("+", "Z")
    out_dir = args.out_dir.resolve() if args.out_dir else (canonical / "checkpoints" / suffix).resolve()
    if out_dir.is_symlink():
        raise SystemExit("G2B_BIND_HOLD:OUT_DIR_SYMLINK")
    atomic_json(out_dir / "g2b_bind_receipt.json", receipt)

    lines = [
        "RESULT=" + receipt["result"],
        "REASON=" + str(receipt["reason"]),
        "HANDOFF_ID=" + receipt["handoff_id"],
        "GATE_ID=" + receipt["gate_id"],
        "SYSTEM_IDENTITY=" + receipt["values"].get("SYSTEM_IDENTITY", "UNAVAILABLE"),
        "ACTIVE_REVISION=" + receipt["values"].get("ACTIVE_REVISION", "UNAVAILABLE"),
        "ACTIVE_CORE=" + receipt["values"].get("ACTIVE_CORE", "UNAVAILABLE"),
        "ACTIVE_BRAIN_HEAD=" + receipt["values"].get("ACTIVE_BRAIN_HEAD", "UNAVAILABLE"),
        "MODEL_GENERATION=" + receipt["values"].get("MODEL_GENERATION", "UNAVAILABLE"),
        "STATE_VERSION=" + receipt["values"].get("STATE_VERSION", "UNAVAILABLE"),
        "RECEIPT_SHA256=" + receipt["receipt_sha256"],
        "RECEIPT_JSON=" + str(out_dir / "g2b_bind_receipt.json"),
    ]
    (out_dir / "g2b_bind_receipt.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0 if receipt["result"].startswith("G2B_BIND_PRODUCER") else 3


if __name__ == "__main__":
    raise SystemExit(main())
