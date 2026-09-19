#!/usr/bin/env python3
"""
R7 language feeder R1.

Mechanical-only ingress for C5V4/R7:
local UTF-8 document -> content-addressed document + provenance -> READY.manifest.

This program MUST NOT invoke SIGMA VM, model, AIL, canonical state, or semantic
scoring. C5V4 remains the sole learner / sole canonical writer.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

SCHEMA = "SIGMA_R7_LANGUAGE_FEEDER_R1"
PROV_SCHEMA = "SIGMA_R7_LANGUAGE_FEEDER_PROVENANCE_V1"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def atomic_write_new(path: Path, data: bytes) -> str:
    """Create path atomically; if already present, require exact byte identity."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_bytes()
        if existing != data:
            raise RuntimeError(f"CONTENT_ADDRESS_CONFLICT:{path}")
        return "ALREADY_PRESENT"

    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
    )
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        try:
            os.link(tmp, path)
            status = "CREATED"
        except FileExistsError:
            existing = path.read_bytes()
            if existing != data:
                raise RuntimeError(f"CONTENT_ADDRESS_CONFLICT:{path}")
            status = "ALREADY_PRESENT"
        finally:
            tmp.unlink(missing_ok=True)
        fsync_dir(path.parent)
        return status
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def manifest_add(inbox: Path, digest: str, rel_path: str) -> str:
    manifest = inbox / "READY.manifest"
    lock_path = inbox / ".READY.manifest.lock"
    inbox.mkdir(parents=True, exist_ok=True)

    with open(lock_path, "a+b") as lockf:
        fcntl.flock(lockf.fileno(), fcntl.LOCK_EX)

        lines: list[str] = []
        if manifest.exists():
            lines = manifest.read_text(encoding="utf-8").splitlines()

        seen: dict[str, str] = {}
        for line in lines:
            if not line:
                continue
            parts = line.split("\t", 1)
            if len(parts) != 2:
                raise RuntimeError("READY_MANIFEST_MALFORMED_RECORD")
            old_sha, old_rel = parts
            if len(old_sha) != 64:
                raise RuntimeError("READY_MANIFEST_INVALID_SHA_FIELD")
            seen[old_sha] = old_rel

        if digest in seen:
            if seen[digest] != rel_path:
                raise RuntimeError("READY_MANIFEST_DIGEST_PATH_CONFLICT")
            return "ALREADY_PRESENT"

        lines.append(f"{digest}\t{rel_path}")
        payload = ("\n".join(lines) + "\n").encode("utf-8")

        fd, tmp_name = tempfile.mkstemp(
            prefix=".READY.manifest.",
            suffix=".tmp",
            dir=str(inbox),
        )
        tmp = Path(tmp_name)
        try:
            with os.fdopen(fd, "wb") as f:
                f.write(payload)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, manifest)
            fsync_dir(inbox)
        finally:
            tmp.unlink(missing_ok=True)

        return "ADDED"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("source_file", type=Path)
    p.add_argument("--root", type=Path,
                   default=Path.home() / "SIGMA" / "sigma_genesis1")
    p.add_argument("--source-id", required=True)
    p.add_argument("--source-url", default="")
    p.add_argument("--language", default="UNKNOWN")
    p.add_argument("--title", default="")
    p.add_argument("--doc-type", default="HUMAN_WRITTEN_DOCUMENT")
    p.add_argument("--license", default="UNKNOWN")
    p.add_argument("--min-bytes", type=int, default=1)
    p.add_argument("--max-bytes", type=int, default=849999)
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def main() -> int:
    a = parse_args()
    src = a.source_file.expanduser().resolve()
    root = a.root.expanduser().resolve()
    inbox = root / ".sigma_sources" / "LOCAL_LEARNING_INBOX"

    if not src.is_file():
        print("FEEDER_RESULT=REJECT")
        print("REASON=SOURCE_FILE_NOT_FOUND")
        return 20

    payload = src.read_bytes()
    size = len(payload)

    if size < a.min_bytes:
        print("FEEDER_RESULT=REJECT")
        print("REASON=BELOW_MIN_BYTES")
        print(f"SOURCE_BYTES={size}")
        return 21

    if size > a.max_bytes:
        print("FEEDER_RESULT=REJECT")
        print("REASON=ABOVE_MAX_BYTES")
        print(f"SOURCE_BYTES={size}")
        return 22

    if b"\x00" in payload:
        print("FEEDER_RESULT=REJECT")
        print("REASON=NUL_BYTE_PRESENT")
        return 23

    try:
        payload.decode("utf-8", "strict")
    except UnicodeDecodeError:
        print("FEEDER_RESULT=REJECT")
        print("REASON=INVALID_UTF8")
        return 24

    digest = sha256_bytes(payload)
    rel_doc = f"documents/{digest}.document"
    doc_path = inbox / rel_doc
    prov_path = inbox / "provenance" / f"{digest}.json"

    provenance = {
        "schema": PROV_SCHEMA,
        "source_sha256": digest,
        "source_id": a.source_id,
        "source_url": a.source_url,
        "source_path": str(src),
        "language_hint": a.language,
        "language_hint_only": True,
        "title": a.title,
        "doc_type": a.doc_type,
        "license": a.license,
        "cleaned_utf8_bytes": size,
        "payload_mode": "FULL_CLEANED_DOCUMENT",
        "content_transform": "NONE_EXACT_SOURCE_BYTES",
        "semantic_summary_created": False,
        "semantic_scoring_created": False,
        "model_used": False,
        "ail_used": False,
        "vm_used": False,
        "canon_written": False,
        "cognition_owner": "SIGMA_NATIVE",
        "host_role": "MECHANICAL_ONLY",
    }
    prov_bytes = (
        json.dumps(provenance, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")

    print(f"SCHEMA={SCHEMA}")
    print("ROLE=R7_LANGUAGE_FEEDER_ONLY")
    print("MODEL=NONE")
    print("AIL=NONE")
    print("VM=NONE")
    print("CANON_WRITE=NO")
    print("HEAD_WRITE=NO")
    print("R7_MUTATION=NO")
    print("HOST_ROLE=MECHANICAL_ONLY")
    print("COGNITION_OWNER=SIGMA_NATIVE")
    print(f"SOURCE_ID={a.source_id}")
    print(f"SOURCE_BYTES={size}")
    print(f"LEARNING_DOCUMENT_SHA256={digest}")
    print(f"DOCUMENT_PATH={doc_path}")
    print(f"PROVENANCE_PATH={prov_path}")
    print(f"READY_MANIFEST={inbox / 'READY.manifest'}")

    if a.dry_run:
        print("FEEDER_RESULT=DRY_RUN_PASS")
        print("LEARNING_STATE=NOT_QUEUED")
        return 0

    doc_status = atomic_write_new(doc_path, payload)
    prov_status = atomic_write_new(prov_path, prov_bytes)
    manifest_status = manifest_add(inbox, digest, rel_doc)

    print(f"DOCUMENT_WRITE={doc_status}")
    print(f"PROVENANCE_WRITE={prov_status}")
    print(f"MANIFEST_ADDED={'YES' if manifest_status == 'ADDED' else 'ALREADY_PRESENT'}")
    print("LEARNING_STATE=QUEUED_FOR_C5V4")
    print("C5V4_ROLE_CONTRACT=SOLE_LEARNER_SOLE_CANON_WRITER")
    print("FEEDER_RESULT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
