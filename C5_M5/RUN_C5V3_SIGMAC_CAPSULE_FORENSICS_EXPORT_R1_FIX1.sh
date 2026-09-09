#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
VM="$ROOT/native/sigma-vm.v09_candidate"
RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
R2_SRC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R2/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
R2_BC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R2/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
R3_SRC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
R3_BC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"
EXPECTED_R2_SRC="d7d1153fd6979dff7d119bb5e8187f045b9f8af62e51065cccf95265478fc3a0"
EXPECTED_R3_SRC="152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8"
EXPECTED_29B="ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a"

TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_SIGMAC_CAPSULE_FORENSICS_R1_$$"
OUT="/sdcard/Download/C5V3_SIGMAC_CAPSULE_FORENSICS_65f69217.zip"
mkdir -p "$TMP/controls" "$TMP/outputs" "$TMP/export"
trap 'rm -rf "$TMP"' EXIT
REPORT="$TMP/export/AUDIT_MANIFEST.txt"
: > "$REPORT"

log() { printf '%s\n' "$*" | tee -a "$REPORT"; }
sha() { sha256sum "$1" | awk '{print $1}'; }

lock() {
  local p e n a
  p="$1"; e="$2"; n="$3"
  [ -f "$p" ] || { log "HOLD=MISSING_EXACT_PATH"; log "PATH=$p"; exit 1; }
  a="$(sha "$p")"
  log "${n}_PATH=$p"
  log "${n}_SHA256=$a"
  log "${n}_BYTES=$(wc -c < "$p")"
  [ "$a" = "$e" ] || { log "${n}_IDENTITY=FAIL"; exit 1; }
  log "${n}_IDENTITY=PASS"
}

inspect_capsule() {
  local p label
  p="$1"; label="$2"
  python - "$p" "$label" <<'PY' | tee -a "$REPORT"
from pathlib import Path
import hashlib, struct, sys
p=Path(sys.argv[1]); label=sys.argv[2]; b=p.read_bytes()
print(f"{label}_BYTES={len(b)}")
print(f"{label}_SHA256={hashlib.sha256(b).hexdigest()}")
print(f"{label}_HEX={b.hex()}")
print(f"{label}_ASCII="+''.join(chr(x) if 32 <= x < 127 else '.' for x in b))
print(f"{label}_MAGIC_ASCII={b[:8].decode('ascii','replace')}")
for off in (8,12,16,20,24):
    if off+4 <= len(b):
        print(f"{label}_U32LE_AT_{off}={struct.unpack_from('<I',b,off)[0]}")
if b:
    print(f"{label}_LAST_BYTE={b[-1]}")
PY
}

compile_case() {
  local label src out clog rc
  label="$1"
  src="$2"
  out="$TMP/outputs/${label}.sigmab"
  clog="$TMP/${label}.compiler.log"
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
    inspect_capsule "$out" "$label"
  else
    log "${label}_OUTPUT=ABSENT"
  fi
}

binary_metadata() {
  local p label out
  p="$1"; label="$2"; out="$3"
  python - "$p" "$label" "$out" <<'PY'
from pathlib import Path
import hashlib, sys
p=Path(sys.argv[1]); label=sys.argv[2]; out=Path(sys.argv[3]); b=p.read_bytes()
lines=[]
lines.append(f"{label}_BYTES={len(b)}")
lines.append(f"{label}_SHA256={hashlib.sha256(b).hexdigest()}")
lines.append(f"{label}_ELF_MAGIC={'YES' if b[:4]==bytes([0x7f,0x45,0x4c,0x46]) else 'NO'}")
if b[:4]==bytes([0x7f,0x45,0x4c,0x46]) and len(b)>=20:
    lines.append(f"{label}_ELF_CLASS_BYTE={b[4]}")
    lines.append(f"{label}_ELF_DATA_BYTE={b[5]}")
    lines.append(f"{label}_ELF_OSABI_BYTE={b[7]}")
# printable ASCII strings, minimum 4 bytes
strings=[]; cur=[]
for x in b:
    if 32 <= x < 127:
        cur.append(chr(x))
    else:
        if len(cur)>=4: strings.append(''.join(cur))
        cur=[]
if len(cur)>=4: strings.append(''.join(cur))
lines.append(f"{label}_PRINTABLE_STRING_COUNT={len(strings)}")
out.write_text('\n'.join(lines)+'\n\n'+'\n'.join(strings)+'\n')
print('\n'.join(lines))
PY
}

log "=== C5V3 SIGMAC CAPSULE FORENSICS EXPORT R1 FIX1 ==="
log "MODE=STATIC_COMPILER_CONFORMANCE_CAPSULE_AND_BINARY_FORENSICS"
log "DIRECTORY_SCAN=NO"
log "VM_EXECUTION=NO"
log "CORE_EXECUTION=NO"
log "PRODUCTION_MUTATION=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" "SIGMAC"
lock "$VM" "$EXPECTED_VM" "VM"
lock "$RUNNER" "$EXPECTED_RUNNER" "RUNNER"
lock "$R2_SRC" "$EXPECTED_R2_SRC" "R2_SOURCE"
lock "$R3_SRC" "$EXPECTED_R3_SRC" "R3_FIX1_SOURCE"
lock "$R2_BC" "$EXPECTED_29B" "R2_FROZEN_29B"
lock "$R3_BC" "$EXPECTED_29B" "R3_FIX1_FROZEN_29B"

log "=== 1. EXACT 29-BYTE CAPSULE DECODE ==="
inspect_capsule "$R3_BC" "R3_FIX1_FROZEN_29B"

log "=== 2. CONTROL SOURCE MATRIX ==="
: > "$TMP/controls/00_empty.sigma"
printf 'THIS IS NOT SIGMA\n' > "$TMP/controls/01_plain_text.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n' > "$TMP/controls/02_header_only.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=INVALID.DOMAIN][VERSION=INVALID]\nBROKEN_TOKEN @@@ {\n' > "$TMP/controls/03_invalid_header_broken_body.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n⟡(Σ.TEST) {\n  ⚡ print("ONE");\n}\n' > "$TMP/controls/04_minimal_a.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n⟡(Σ.TEST) {\n  ⚡ print("TWO_DIFFERENT_LITERAL");\n}\n' > "$TMP/controls/05_minimal_b.sigma"
printf '#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n⟡(Σ.TEST) {\n  ⚡ print("UNBALANCED");\n' > "$TMP/controls/06_unbalanced.sigma"
for n in 00_empty 01_plain_text 02_header_only 03_invalid_header_broken_body 04_minimal_a 05_minimal_b 06_unbalanced; do
  compile_case "$n" "$TMP/controls/$n.sigma"
done
compile_case "07_r2_full" "$R2_SRC"
compile_case "08_r3_fix1_full" "$R3_SRC"

python - "$TMP/outputs" <<'PY' | tee -a "$REPORT"
from pathlib import Path
import hashlib, sys
root=Path(sys.argv[1]); rows=[]
for p in sorted(root.glob('*.sigmab')):
    b=p.read_bytes(); rows.append((p.name,hashlib.sha256(b).hexdigest(),len(b),b.hex()))
print('OUTPUT_FILE_COUNT='+str(len(rows)))
print('DISTINCT_OUTPUT_SHA_COUNT='+str(len({r[1] for r in rows})))
print('DISTINCT_OUTPUT_SIZE_COUNT='+str(len({r[2] for r in rows})))
print('ALL_OUTPUTS_BYTE_IDENTICAL='+('YES' if rows and len({r[3] for r in rows})==1 else 'NO'))
for r in rows: print('OUTPUT='+'|'.join(map(str,r[:3])))
PY

log "=== 3. STATIC BINARY METADATA / STRINGS ==="
binary_metadata "$SIGMAC" "SIGMAC" "$TMP/export/SIGMAC_STRINGS_AND_META.txt" | tee -a "$REPORT"
binary_metadata "$VM" "VM" "$TMP/export/VM_STRINGS_AND_META.txt" | tee -a "$REPORT"

log "=== 4. EXACT RUNNER COMPILER/VM INVOCATION LINES ==="
grep -nE '\$SIGMAC|\$VM|"\$SIGMAC"|"\$VM"|SIGMAC_RC|VM_RC|\.sigmab|\.sigma' "$RUNNER" 2>/dev/null | tee "$TMP/export/RUNNER_INVOCATION_LINES.txt" | tee -a "$REPORT" || true

cp "$SIGMAC" "$TMP/export/sigmac"
cp "$VM" "$TMP/export/sigma-vm.v09_candidate"
cp "$RUNNER" "$TMP/export/live_runner.sh"
cp "$R2_SRC" "$TMP/export/R2_SOURCE.sigma"
cp "$R3_SRC" "$TMP/export/R3_FIX1_SOURCE.sigma"
cp "$R2_BC" "$TMP/export/R2_29B.sigmab"
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

log "=== 5. EXPORT ==="
log "EXPORT_ZIP=$OUT"
log "EXPORT_ZIP_SHA256=$(sha "$OUT")"
log "EXPORT_ZIP_BYTES=$(wc -c < "$OUT")"
log "FORENSICS_EXPORT=PASS"
log "VM_EXECUTION=NO"
log "PRODUCTION_MUTATION=NO"
log "=== END ==="
