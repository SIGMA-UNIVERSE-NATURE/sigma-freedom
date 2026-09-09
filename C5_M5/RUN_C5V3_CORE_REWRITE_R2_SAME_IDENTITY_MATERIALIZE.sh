#!/data/data/com.termux/files/usr/bin/bash
set -eu

# C5V3 Core Rewrite R2 — same identity materialization
# Purpose: derive the rewritten successor as the exact historical C5 core
# identity. No live-core write, no VM/core execution, no directory scan.

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SYNC_ROOT="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R2"
SRC="$SYNC_ROOT/source_template/SIGMA_C5V3_COGNITIVE_KERNEL_SUCCESSOR_R1_DRAFT.sigma"
DST="$SYNC_ROOT/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"

TEMPLATE_URL="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/a22161127ef8105e11cb067bdecb4c0b13637f68/C5_M5/SIGMA_C5V3_COGNITIVE_KERNEL_SUCCESSOR_R1_DRAFT.sigma"
EXPECTED_TEMPLATE_GIT_BLOB="188f1df348291758147abd438004b35a88372639"
EXPECTED_HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'

printf '%s\n' '=== C5V3 CORE REWRITE R2 SAME IDENTITY MATERIALIZE ==='
printf 'ROOT=%s\n' "$ROOT"
printf 'MODE=SUCCESSOR_SOURCE_MATERIALIZE_ONLY\n'
printf 'LIVE_CORE_WRITE=NO\n'
printf 'VM_EXECUTION=NO\n'
printf 'CORE_EXECUTION=NO\n'
printf 'DIRECTORY_SCAN=NO\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'

mkdir -p "$SYNC_ROOT/source_template" "$SYNC_ROOT/src" "$SYNC_ROOT/evidence"

if [ ! -f "$SRC" ]; then
    CURL="$(command -v curl 2>/dev/null || true)"
    [ -n "$CURL" ] || { echo 'HOLD=CURL_MISSING_FOR_EXACT_GITHUB_SOURCE_FETCH'; exit 1; }
    "$CURL" -fsSL "$TEMPLATE_URL" -o "$SRC.partial"
    mv "$SRC.partial" "$SRC"
fi

GIT="$(command -v git 2>/dev/null || true)"
[ -n "$GIT" ] || { echo 'HOLD=GIT_MISSING_FOR_BLOB_IDENTITY'; exit 1; }
TEMPLATE_BLOB="$($GIT hash-object "$SRC")"
printf 'TEMPLATE_GIT_BLOB=%s\n' "$TEMPLATE_BLOB"
[ "$TEMPLATE_BLOB" = "$EXPECTED_TEMPLATE_GIT_BLOB" ] || {
    echo 'HOLD=TEMPLATE_GIT_BLOB_MISMATCH'
    exit 1
}

python - "$SRC" "$DST.partial" <<'PY'
from pathlib import Path
import sys

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
text = src.read_text(encoding='utf-8')
lines = text.splitlines()
if not lines:
    raise SystemExit('empty source')

lines[0] = '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'
text = '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
text = text.replace('⟡(Σ.C5V3_COGNITIVE_KERNEL_R1)', '⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1)')
text = text.replace('print("SIGMA_C5V3_COGNITIVE_KERNEL_R1")', 'print("SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1")')
text = text.replace('⚡ STATUS: "C5V3_READY";', '⚡ STATUS: "C5_READY";')
dst.write_text(text, encoding='utf-8')
PY

FIRST_LINE="$(sed -n '1p' "$DST.partial")"
ENTRY_COUNT="$(grep -Fxc '⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1) {' "$DST.partial" || true)"
OLD_ENTRY_COUNT="$(grep -Fxc '⟡(Σ.C5V3_COGNITIVE_KERNEL_R1) {' "$DST.partial" || true)"
PRINT_COUNT="$(grep -Fc 'print("SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1")' "$DST.partial" || true)"
OLD_HEADER_COUNT="$(grep -Fc 'DOMAIN=SIGMA.C5V3.COGNITIVE.KERNEL' "$DST.partial" || true)"

printf 'HEADER=%s\n' "$FIRST_LINE"
printf 'HISTORICAL_ENTRY_ID_COUNT=%s\n' "$ENTRY_COUNT"
printf 'NEW_ENTRY_ID_REMAINING_COUNT=%s\n' "$OLD_ENTRY_COUNT"
printf 'HISTORICAL_PRINT_ID_COUNT=%s\n' "$PRINT_COUNT"
printf 'ALTERNATE_DOMAIN_HEADER_REMAINING_COUNT=%s\n' "$OLD_HEADER_COUNT"

[ "$FIRST_LINE" = "$EXPECTED_HEADER" ] || { echo 'HOLD=HEADER_IDENTITY_MISMATCH'; exit 1; }
[ "$ENTRY_COUNT" -eq 1 ] || { echo 'HOLD=CORE_ENTRY_IDENTITY_MISMATCH'; exit 1; }
[ "$OLD_ENTRY_COUNT" -eq 0 ] || { echo 'HOLD=ALTERNATE_CORE_ENTRY_REMAINS'; exit 1; }
[ "$PRINT_COUNT" -eq 1 ] || { echo 'HOLD=CORE_PRINT_IDENTITY_MISMATCH'; exit 1; }
[ "$OLD_HEADER_COUNT" -eq 0 ] || { echo 'HOLD=ALTERNATE_DOMAIN_HEADER_REMAINS'; exit 1; }

if [ -f "$DST" ]; then
    OLD_SHA="$(sha256sum "$DST" | awk '{print $1}')"
    NEW_SHA="$(sha256sum "$DST.partial" | awk '{print $1}')"
    [ "$OLD_SHA" = "$NEW_SHA" ] || { echo 'HOLD=EXISTING_SUCCESSOR_DIFFERS'; exit 1; }
    rm -f "$DST.partial"
    printf 'SUCCESSOR_ALREADY_EXISTS=YES\n'
else
    mv "$DST.partial" "$DST"
    chmod 0400 "$DST"
    printf 'SUCCESSOR_ALREADY_EXISTS=NO\n'
fi

printf 'SUCCESSOR_SOURCE=%s\n' "$DST"
printf 'SUCCESSOR_SOURCE_SHA256=%s\n' "$(sha256sum "$DST" | awk '{print $1}')"
printf 'SUCCESSOR_SOURCE_LINES=%s\n' "$(wc -l < "$DST")"
printf 'SUCCESSOR_DEF_COUNT=%s\n' "$(grep -Ec '^DEF[[:space:]]+' "$DST")"
printf 'CORE_IDENTITY_CONTINUITY=PASS\n'
printf 'CAPABILITY_NATIVE_ARCHITECTURE_IN_SAME_C5_CORE=YES\n'
printf 'LIVE_CORE_WRITE=NO\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf '%s\n' '=== END ==='
