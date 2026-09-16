#!/usr/bin/env bash
set -euo pipefail
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$HERE"
[ -f MANIFEST.sha256 ] || { echo 'BUNDLE_MANIFEST_VERIFY=FAIL_MISSING'; exit 2; }
sha256sum -c MANIFEST.sha256
printf 'BUNDLE_MANIFEST_VERIFY=PASS\n'
