#!/usr/bin/env bash
set -euo pipefail
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
OUT="${1:-$PWD/SIGMA_SURVIVAL_INTERNET_AUTOLEARN_R1.tgz}"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
TOP="$TMP/SIGMA_SURVIVAL_INTERNET_AUTOLEARN_R1"
mkdir -p "$TOP"
cp -a "$HERE"/. "$TOP"/
# Deterministic metadata: fixed ordering, owner, group, mtime; gzip without timestamp/name.
tar --sort=name --mtime='UTC 2026-09-17' --owner=0 --group=0 --numeric-owner -C "$TMP" -cf - SIGMA_SURVIVAL_INTERNET_AUTOLEARN_R1 | gzip -n > "$OUT"
sha256sum "$OUT"
