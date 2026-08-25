#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
"""Copy the supportor experiment/reference seed into Termux private state.

This does not promote anything into verified SIGMA knowledge. It preserves the
source files byte-for-byte and records SHA-256 + Git commit provenance.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
CODEC_ROOT = HERE.parent
STATE_ROOT = Path(
    os.environ.get(
        "SIGMA_TERMUX_CODEC_HOME",
        str(Path.home() / ".sigma" / "semantic_codec"),
    )
).expanduser()
SEED_ROOT = STATE_ROOT / "seed"

SOURCES = [
    CODEC_ROOT / "examples_10_domains.json",
    CODEC_ROOT / "multilingual_mapping_demo.json",
    CODEC_ROOT / "SIGMA_TRANSFER_MANIFEST.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(HERE), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return None


def main() -> None:
    missing = [str(path) for path in SOURCES if not path.is_file()]
    if missing:
        raise SystemExit("SEED_SOURCE_MISSING:" + "|".join(missing))

    SEED_ROOT.mkdir(parents=True, exist_ok=True)
    try:
        SEED_ROOT.chmod(0o700)
    except OSError:
        pass

    records = []
    for source in SOURCES:
        target = SEED_ROOT / source.name
        shutil.copy2(source, target)
        if sha256(source) != sha256(target):
            raise RuntimeError(f"SEED_COPY_SHA256_MISMATCH:{source.name}")
        try:
            target.chmod(0o600)
        except OSError:
            pass
        records.append({
            "name": source.name,
            "source_path": str(source),
            "target_path": str(target),
            "sha256": sha256(target),
            "bytes": target.stat().st_size,
        })

    manifest = {
        "schema": "SIGMA_TERMUX_SEED_MANIFEST_V0.1",
        "status": "SUPPORTOR_SEED_UNVERIFIED_NOT_PROMOTED",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_commit(),
        "reference_version": "SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825",
        "claim_rule": "CLAIM<=EVIDENCE",
        "knowledge_promoted": False,
        "files": records,
    }
    output = SEED_ROOT / "seed_manifest.json"
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    try:
        output.chmod(0o600)
    except OSError:
        pass

    print("PASS termux_seed_copy")
    print(f"SEED_ROOT={SEED_ROOT}")
    print(f"FILES={len(records)}")
    print("KNOWLEDGE_PROMOTED=false")


if __name__ == "__main__":
    main()
