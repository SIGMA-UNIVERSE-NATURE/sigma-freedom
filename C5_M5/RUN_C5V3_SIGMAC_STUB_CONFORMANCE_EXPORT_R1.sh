#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
VM="$ROOT/native/sigma-vm.v09_candidate"
R3_SRC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
R3_BC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_R3_SRC="152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8"
EXPECTED_R3_BC="ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a"

TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_SIGMAC_STUB_AUDIT_R1_$$"
OUT="/sdcard/Download/C5V3_SIGMAC_VM_LOCAL_AUDIT_65f69217.zip"
mkdir -p "$TMP/controls" "$TMP/outputs" "$TMP/export"
trap 'rm -rf "$TMP"' EXIT

REPORT="$TMP/export/AUDIT_MANIFEST.txt"
: > "$REPORT"

log() {
    printf '%s\n' "$*" | tee -a "$REPORT"
}

sha() { sha256sum "$1" | awk '{print $1}'; }

lock() {
    local p="$1" e="$2" n="$3" a
    [ -f "$p" ] || { log "HOLD=MISSING_EXACT_PATH"; log "PATH=$p"; exit 1; }
    a="$(sha "$p")"
    log "${n}_PATH=$p"
    log "${n}_SHA256=$a"
    log "${n}_BYTES=$(wc -c < "$p")"
    [ "$a" = "$e" ] || { log "${n}_IDENTITY=FAIL"; exit 1; }
    log "${n}_IDENTITY=PASS"
}

inspect_file() {
    local p="$1" label="$2"
    python - "$p" "$label" >> "$REPORT" <<'PY'
from pathlib import Path
import hashlib, sys
p=Path(sys.argv[1]); label=sys.argv[2]
b=p.read_bytes()
print(f"{label}_BYTES={len(b)}")
print(f"{label}_SHA256={hashlib.sha256(b).hexdigest()}")
print(f"{label}_HEX={b.hex()}")
PY
    tail -n 3 "$REPORT"
}

compile_case() {
    local label="$1" src="$2" out="$TMP/outputs/${label}.sigmab" rc clog="$TMP/${label}.compiler.log"
    rm -f "$out" "$clog"
    set +e
    "$SIGMAC" "$src" "$out" >"$clog" 2>&1
    rc=$?
    set -e
    log "${label}_COMPILE_RC=$rc"
    if [ -s "$clog" ]; then
        while IFS= read -r line; do log "${label}_COMPILER_LOG=$line"; done < "$clog"
    fi
    if [ -f "$out" ]; then
        inspect_file "$out" "$label"
    else
        log "${label}_OUTPUT=ABSENT"
    fi
}

log "=== C5V3 SIGMAC STUB CONFORMANCE + LOCAL BINARY EXPORT R1 ==="
log "MODE=NON_VM_COMPILER_CONFORMANCE_AND_BINARY_EXPORT"
log "DIRECTORY_SCAN=NO"
log "VM_EXECUTION=NO"
log "CORE_EXECUTION=NO"
log "PRODUCTION_MUTATION=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" "SIGMAC"
lock "$VM" "$EXPECTED_VM" "VM"
lock "$R3_SRC" "$EXPECTED_R3_SRC" "R3_FIX1_SOURCE"
lock "$R3_BC" "$EXPECTED_R3_BC" "R3_FIX1_FROZEN_29B"

log "=== EXACT CURRENT 29-BYTE PAYLOAD ==="
inspect_file "$R3_BC" "R3_FIX1_FROZEN_29B"

: > "$TMP/controls/00_empty.sigma"
printf 'THIS IS NOT SIGMA\n' > "$TMP/controls/01_plain_text.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n' > "$TMP/controls/02_header_only.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=INVALID.DOMAIN][VERSION=INVALID]\nBROKEN_TOKEN @@@ {\n' > "$TMP/controls/03_invalid_header_broken_body.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n⟡(Σ.TEST) {\n  ⚡ print("ONE");\n}\n' > "$TMP/controls/04_minimal_a.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n⟡(Σ.TEST) {\n  ⚡ print("TWO_DIFFERENT_LITERAL");\n}\n' > "$TMP/controls/05_minimal_b.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n⟡(Σ.TEST) {\n  ⚡ print("UNBALANCED");\n' > "$TMP/controls/06_unbalanced.sigma"

log "=== CONTROL COMPILES ==="
for n in 00_empty 01_plain_text 02_header_only 03_invalid_header_broken_body 04_minimal_a 05_minimal_b 06_unbalanced; do
    compile_case "$n" "$TMP/controls/$n.sigma"
done
compile_case "07_r3_fix1" "$R3_SRC"

python - "$TMP/outputs" >> "$REPORT" <<'PY'
from pathlib import Path
import hashlib, sys
root=Path(sys.argv[1])
rows=[]
for p in sorted(root.glob('*.sigmab')):
    b=p.read_bytes(); rows.append((p.name, hashlib.sha256(b).hexdigest(), len(b)))
print("OUTPUT_FILE_COUNT="+str(len(rows)))
print("DISTINCT_OUTPUT_SHA_COUNT="+str(len({r[1] for r in rows})))
print("DISTINCT_OUTPUT_SIZE_COUNT="+str(len({r[2] for r in rows})))
for name,h,n in rows:
    print(f"OUTPUT={name}|{h}|{n}")
PY

tail -n $((10 + $(find "$TMP/outputs" -maxdepth 1 -type f | wc -l))) "$REPORT" || true

cp "$SIGMAC" "$TMP/export/sigmac"
cp "$VM" "$TMP/export/sigma-vm.v09_candidate"
cp "$R3_SRC" "$TMP/export/R3_FIX1_SOURCE.sigma"
cp "$R3_BC" "$TMP/export/R3_FIX1_29B.sigmab"
cp "$TMP/controls/"*.sigma "$TMP/export/"
cp "$TMP/outputs/"*.sigmab "$TMP/export/" 2>/dev/null || true

python - "$TMP/export" "$OUT" <<'PY'
from pathlib import Path
import sys, zipfile
src=Path(sys.argv[1]); out=Path(sys.argv[2])
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(src.iterdir()):
        if p.is_file(): z.write(p,p.name)
PY

log "=== EXPORT ==="
log "EXPORT_ZIP=$OUT"
log "EXPORT_ZIP_SHA256=$(sha "$OUT")"
log "EXPORT_ZIP_BYTES=$(wc -c < "$OUT")"
log "SIGMAC_VM_BINARY_AUDIT_EXPORT=PASS"
log "VM_EXECUTION=NO"
log "PRODUCTION_MUTATION=NO"
log "=== END ==="
