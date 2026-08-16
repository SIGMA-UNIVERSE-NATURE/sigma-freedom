#!/usr/bin/env python3
"""Mirror canonical SIGMA brain material to Windows E:/F: targets.

No network access, no secrets, no deletion of older material. Intended to be
executed by a local SIGMA runtime with filesystem access to the host drives.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
MIRROR_DIRS = [Path("BRAIN/CANONICAL"), Path("54_CORES"), Path("BẢN ĐỒ")]
TARGET_REL = Path("SIGMA/BRAIN/SIGMA_CANONICAL_BRAIN_v1.0")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_commit() -> str | None:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    except Exception:
        return None


def copy_atomic(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_name(dst.name + ".tmp")
    shutil.copy2(src, tmp)
    os.replace(tmp, dst)
    if sha256(src) != sha256(dst):
        raise RuntimeError(f"verification failed: {dst}")


def mirror_drive(letter: str) -> dict:
    drive = Path(f"{letter.upper()}:\\")
    if not drive.exists():
        return {"drive": letter.upper(), "status": "MISSING"}
    target = drive / TARGET_REL
    copied = 0
    for rel_root in MIRROR_DIRS:
        src_root = REPO / rel_root
        if not src_root.exists():
            continue
        for src in src_root.rglob("*"):
            if src.is_file():
                rel = src.relative_to(REPO)
                copy_atomic(src, target / rel)
                copied += 1
    receipt = {
        "schema_version": "1.0.0",
        "status": "PASS",
        "drive": letter.upper(),
        "target": str(target),
        "files_copied": copied,
        "source_commit": git_commit(),
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }
    (target / "MIRROR_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return receipt


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--drive", action="append", default=[])
    args = p.parse_args()
    drives = args.drive or ["E", "F"]
    results = [mirror_drive(d) for d in drives]
    print(json.dumps({"results": results}, ensure_ascii=False, indent=2))
    if not any(r["status"] == "PASS" for r in results):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
