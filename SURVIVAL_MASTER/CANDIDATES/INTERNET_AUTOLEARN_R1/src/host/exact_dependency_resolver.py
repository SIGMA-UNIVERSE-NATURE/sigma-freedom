#!/usr/bin/env python3
"""Mechanical SHA256 resolver. Never reconstructs missing capability bytes."""
from __future__ import annotations
import argparse, hashlib, os, sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--sha256', required=True)
    ap.add_argument('--root', action='append', required=True)
    args = ap.parse_args()
    wanted = args.sha256.lower()
    if len(wanted) != 64 or any(c not in '0123456789abcdef' for c in wanted):
        print('HOLD=INVALID_EXPECTED_SHA256')
        return 2
    matches = []
    for root_text in args.root:
        root = Path(os.path.expandvars(os.path.expanduser(root_text))).resolve()
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
            dirnames[:] = sorted(d for d in dirnames if not Path(dirpath, d).is_symlink())
            for name in sorted(filenames):
                p = Path(dirpath, name)
                if p.is_symlink() or not p.is_file():
                    continue
                try:
                    if sha256_file(p) == wanted:
                        matches.append(str(p.resolve()))
                except (OSError, PermissionError):
                    continue
    matches = sorted(set(matches))
    if not matches:
        print('HOLD=DEPENDENCY_MISSING')
        print(f'EXPECTED_SHA256={wanted}')
        return 2
    if len(matches) != 1:
        print('HOLD=DEPENDENCY_SHA256_AMBIGUOUS_MULTIPLE_PATHS')
        for p in matches:
            print(f'MATCH={p}')
        return 2
    print('DEPENDENCY_RESOLUTION=PASS')
    print(f'EXPECTED_SHA256={wanted}')
    print(f'PATH={matches[0]}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
