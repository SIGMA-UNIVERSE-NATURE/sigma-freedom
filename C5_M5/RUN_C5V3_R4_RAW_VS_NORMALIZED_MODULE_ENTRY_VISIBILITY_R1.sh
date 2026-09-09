#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
SUCCESSOR="$ROOT/.sigma_c5v3_sync/C5V3_R4_SUCCESSOR_T1_T2_T3_R1/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R4_RAW_NORMALIZED_VIS_R1_$$"
mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_SUCCESSOR="b1ceedffa11497cab5454639eb1872cc5ecb95a5824b95e4d1be22c2ea2b7406"
HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'
ENTRY='Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1'
BASE='https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom'

STATE_COMMIT="ca6d9504f5e75c4d5ccf48ab7c574614a8b019be"
TRANS_COMMIT="3debd57e8f0ac3dce7bba540cb912c0ffbadef29"
ADAPTER_COMMIT="02bb0c6d60f2568583211b16baa8fbbd3de0e77f"
DURABLE_COMMIT="b334a1ff23d068551d46b1f114b8ad45afbf46e3"
KERNEL_COMMIT="89019543f98b39cd34ea95535a14c77f050360ea"
P0_COMMIT="ba42087f602baf274c6ed5c90ae3f7a92d647eba"

EXPECTED_STATE="83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33"
EXPECTED_TRANS="3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9"
EXPECTED_ADAPTER="223aeb84c4d4fcc8e1cbdbf62943a38382efa8250de72eb4df4ba3df79e5b02b"
EXPECTED_DURABLE="514c52fcc2e8e1fc5ea64e78b664b7651c8c0ce20c2d463b5fe505c95f9becd2"
EXPECTED_KERNEL="db2a0454fc429d58b9617a40a6e4283f632b35df2c6190e6389820402e1035b1"
EXPECTED_P0="cad40e8ded7138d7e56c8cbb219eba5e43d10d78fc18e7f335073f048f1bad82"

sha(){ sha256sum "$1" | awk '{print $1}'; }
lock(){ local p="$1" e="$2" n="$3" a; [ -f "$p" ] || { echo "HOLD=MISSING_$n"; exit 1; }; a="$(sha "$p")"; echo "${n}_SHA256=$a"; [ "$a" = "$e" ] || { echo "HOLD=${n}_IDENTITY"; exit 1; }; echo "${n}_IDENTITY=PASS"; }
fetch_exact(){ local commit="$1" path="$2" out="$3" expected="$4" label="$5"; curl -fsSL "$BASE/$commit/$path" -o "$out"; echo "${label}_SHA256=$(sha "$out")"; [ "$(sha "$out")" = "$expected" ] || { echo "HOLD=${label}_IDENTITY"; exit 1; }; echo "${label}_IDENTITY=PASS"; }

# Compile two source variants that differ only in the final sentinel literal.
# Entry visibility is PASS only when the resulting bytecode differs.
visibility_case(){
  local label="$1" body="$2"
  local a="$TMP/${label}_A.sigma" b="$TMP/${label}_B.sigma"
  local ba="$TMP/${label}_A.sigmab" bb="$TMP/${label}_B.sigmab"
  {
    echo "$HEADER"; echo; cat "$GATEA"; echo; cat "$body"; echo
    printf '⟡(%s) {\n    ⚡ print("ENTRY_VIS_A");\n}\n' "$ENTRY"
  } > "$a"
  {
    echo "$HEADER"; echo; cat "$GATEA"; echo; cat "$body"; echo
    printf '⟡(%s) {\n    ⚡ print("ENTRY_VIS_B");\n}\n' "$ENTRY"
  } > "$b"
  set +e
  "$SIGMAC" "$a" "$ba" >"$TMP/${label}_A.log" 2>&1; local rca=$?
  "$SIGMAC" "$b" "$bb" >"$TMP/${label}_B.log" 2>&1; local rcb=$?
  set -e
  echo "${label}_A_RC=$rca"
  echo "${label}_B_RC=$rcb"
  if [ "$rca" -ne 0 ] || [ "$rcb" -ne 0 ] || [ ! -f "$ba" ] || [ ! -f "$bb" ]; then
    echo "${label}_ENTRY_SOURCE_SENSITIVITY=COMPILE_FAIL"
    [ -s "$TMP/${label}_A.log" ] && sed "s/^/${label}_A_LOG=/" "$TMP/${label}_A.log"
    [ -s "$TMP/${label}_B.log" ] && sed "s/^/${label}_B_LOG=/" "$TMP/${label}_B.log"
    return 0
  fi
  local sha_a sha_b bytes_a bytes_b
  sha_a="$(sha "$ba")"; sha_b="$(sha "$bb")"
  bytes_a="$(wc -c < "$ba")"; bytes_b="$(wc -c < "$bb")"
  echo "${label}_A_BYTES=$bytes_a"
  echo "${label}_B_BYTES=$bytes_b"
  echo "${label}_A_SHA256=$sha_a"
  echo "${label}_B_SHA256=$sha_b"
  if [ "$sha_a" != "$sha_b" ]; then
    echo "${label}_ENTRY_SOURCE_SENSITIVITY=PASS"
  else
    echo "${label}_ENTRY_SOURCE_SENSITIVITY=FAIL"
  fi
}

printf '%s\n' '=== C5V3 R4 RAW VS NORMALIZED MODULE ENTRY VISIBILITY R1 ==='
echo 'MODE=RAW_NON_DEF_SURFACE_ISOLATION_BY_SOURCE_SENSITIVITY'
echo 'VM_EXECUTION=NO'
echo 'PRODUCTION_MUTATION=NO'
echo 'PRODUCTION_BINDING=NO'
lock "$SIGMAC" "$EXPECTED_SIGMAC" SIGMAC
lock "$SUCCESSOR" "$EXPECTED_SUCCESSOR" SUCCESSOR

STATE="$TMP/state.raw"; TRANS="$TMP/trans.raw"; ADAPTER="$TMP/adapter.raw"; DURABLE="$TMP/durable.raw"; KERNEL="$TMP/kernel.raw"; P0="$TMP/p0.raw"
fetch_exact "$STATE_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R2.sigma.inc' "$STATE" "$EXPECTED_STATE" STATE
fetch_exact "$TRANS_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc' "$TRANS" "$EXPECTED_TRANS" TRANSITIONS
fetch_exact "$ADAPTER_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc' "$ADAPTER" "$EXPECTED_ADAPTER" ADAPTER
fetch_exact "$DURABLE_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_DURABLE_LEARNING_MODEL_R1.sigma.inc' "$DURABLE" "$EXPECTED_DURABLE" DURABLE
fetch_exact "$KERNEL_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R3.sigma.inc' "$KERNEL" "$EXPECTED_KERNEL" KERNEL
fetch_exact "$P0_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_P0_TRANSACTION_TRUST_R1.sigma.inc' "$P0" "$EXPECTED_P0" P0

GATEA="$TMP/gatea77.norm"
python - "$SUCCESSOR" "$GATEA" "$TMP" <<'PY'
from pathlib import Path
import re,sys
src,out,tmp=sys.argv[1:]
s=Path(src).read_text()

def blocks(text):
    lines=text.splitlines(True); out=[]; i=0
    while i<len(lines):
        m=re.match(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',lines[i])
        if not m: i+=1; continue
        name=m.group(1); buf=[]; depth=0; started=False; j=i
        while j<len(lines):
            line=lines[j]; buf.append(line)
            depth+=line.count('{'); depth-=line.count('}')
            if '{' in line: started=True
            if started and depth==0: break
            j+=1
        if not started or depth!=0: raise SystemExit('HOLD=UNBALANCED_DEF:'+name)
        out.append((name,''.join(buf).rstrip('\n'))); i=j+1
    return out
bs=blocks(s)
if len(bs)!=251: raise SystemExit('HOLD=SUCCESSOR_DEF_COUNT')
# Exact known ordering: Gate-A 77, R4 92, T1/T2/T3 82.
g=bs[:77]; r4=bs[77:169]
Path(out).write_text('\n\n'.join(b for _,b in g)+'\n')
# Normalize each R4 module by known DEF-count boundaries.
bounds=[('STATE',0,28),('TRANS',28,40),('ADAPTER',40,56),('DURABLE',56,66),('KERNEL',66,78),('P0',78,92)]
for name,a,b in bounds:
    Path(tmp,f'{name}.norm').write_text('\n\n'.join(x[1] for x in r4[a:b])+'\n')
print('GATEA_DEF_COUNT='+str(len(g)))
print('R4_DEF_COUNT='+str(len(r4)))
for name,a,b in bounds: print(f'{name}_NORM_DEF_COUNT={b-a}')
PY

EMPTY="$TMP/empty"; : > "$EMPTY"
visibility_case CONTROL_GATEA_ONLY "$EMPTY"

# Individual raw-vs-normalized module isolation.
for item in \
  "STATE:$STATE:$TMP/STATE.norm" \
  "TRANS:$TRANS:$TMP/TRANS.norm" \
  "ADAPTER:$ADAPTER:$TMP/ADAPTER.norm" \
  "DURABLE:$DURABLE:$TMP/DURABLE.norm" \
  "KERNEL:$KERNEL:$TMP/KERNEL.norm" \
  "P0:$P0:$TMP/P0.norm"; do
  IFS=: read -r label raw norm <<< "$item"
  visibility_case "RAW_${label}" "$raw"
  visibility_case "NORM_${label}" "$norm"
done

# Cumulative raw modules vs cumulative normalized modules.
RAW_CUM="$TMP/raw.cum"; NORM_CUM="$TMP/norm.cum"; : > "$RAW_CUM"; : > "$NORM_CUM"
idx=0
for item in \
  "STATE:$STATE:$TMP/STATE.norm" \
  "TRANS:$TRANS:$TMP/TRANS.norm" \
  "ADAPTER:$ADAPTER:$TMP/ADAPTER.norm" \
  "DURABLE:$DURABLE:$TMP/DURABLE.norm" \
  "KERNEL:$KERNEL:$TMP/KERNEL.norm" \
  "P0:$P0:$TMP/P0.norm"; do
  IFS=: read -r label raw norm <<< "$item"
  idx=$((idx+1))
  cat "$raw" >> "$RAW_CUM"; printf '\n' >> "$RAW_CUM"
  cat "$norm" >> "$NORM_CUM"; printf '\n' >> "$NORM_CUM"
  visibility_case "RAW_CUM_${idx}_${label}" "$RAW_CUM"
  visibility_case "NORM_CUM_${idx}_${label}" "$NORM_CUM"
done

# Strip only top-level comments/blank text by replacing each raw module with its DEF-only normalized form.
# Classification is determined from the first raw individual/cumulative FAIL whose normalized peer PASSes.
echo '=== CLASSIFICATION ==='
python - "$TMP" <<'PY'
from pathlib import Path
import re,sys
# Results are emitted to stdout by bash; this marker documents interpretation only.
print('INTERPRETATION=RAW_FAIL_WITH_NORMALIZED_PASS_MEANS_NON_DEF_MODULE_SURFACE_CAUSAL_IN_TESTED_SCOPE')
print('INTERPRETATION=ALL_RAW_PASS_MEANS_PREVIOUS_COMPOSITION_DIFFERENCE_LIES_OUTSIDE_R4_MODULE_BODIES')
PY

echo 'VM_EXECUTION=NO'
echo 'PRODUCTION_BINDING=NO'
echo 'PRODUCTION_MUTATION=NO'
printf '%s\n' '=== END ==='
