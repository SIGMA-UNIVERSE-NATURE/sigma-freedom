#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
R3="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
OUTROOT="$ROOT/.sigma_c5v3_sync/C5V3_R4_SUCCESSOR_T1_T2_T3_R1"
MOD="$OUTROOT/modules"
SRC="$OUTROOT/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
BIN="$OUTROOT/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R4_SUCCESSOR_COMPOSE_R1_$$"
mkdir -p "$MOD" "$OUTROOT/src" "$OUTROOT/bin" "$TMP"
trap 'rm -rf "$TMP"' EXIT

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_R3="152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8"
EXPECTED_GATEA_BUNDLE="ff3fced4c16bf3866e30853e01f5bb634a87ac25943ba612a3cdf1cdf2708494"
EXPECTED_GATEA_SOURCE="bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1"
EXPECTED_GATEA_PURE_NORMALIZED="986465097126d33598ebb83ec9f0af331eadb3a2443f9605dded3a1e4ab04d52"
EXPECTED_T123_NORMALIZED="8b6f231a23c2ab5cd19e2ba2806ced29e9ed6bb8c9590c0559e9532a9feb7d06"
EXPECTED_29B="ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a"

HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'
ENTRY='Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1'

STATE_COMMIT="ca6d9504f5e75c4d5ccf48ab7c574614a8b019be"
TRANS_COMMIT="3debd57e8f0ac3dce7bba540cb912c0ffbadef29"
ADAPTER_COMMIT="02bb0c6d60f2568583211b16baa8fbbd3de0e77f"
DURABLE_COMMIT="b334a1ff23d068551d46b1f114b8ad45afbf46e3"
KERNEL_COMMIT="89019543f98b39cd34ea95535a14c77f050360ea"
P0_COMMIT="ba42087f602baf274c6ed5c90ae3f7a92d647eba"
MAIN_COMMIT="79aed87a074b72f2576aa6b0bb6253cef9df5537"

EXPECTED_STATE="83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33"
EXPECTED_TRANS="3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9"
EXPECTED_ADAPTER="223aeb84c4d4fcc8e1cbdbf62943a38382efa8250de72eb4df4ba3df79e5b02b"
EXPECTED_DURABLE="514c52fcc2e8e1fc5ea64e78b664b7651c8c0ce20c2d463b5fe505c95f9becd2"
EXPECTED_KERNEL="db2a0454fc429d58b9617a40a6e4283f632b35df2c6190e6389820402e1035b1"
EXPECTED_P0="cad40e8ded7138d7e56c8cbb219eba5e43d10d78fc18e7f335073f048f1bad82"
EXPECTED_MAIN="eef4227d9e4151e3f280c315b862249cf345a2cd719ceca4b05658e9bc85b28a"

sha() { sha256sum "$1" | awk '{print $1}'; }
lock() {
  local p="$1" e="$2" n="$3" a
  [ -f "$p" ] || { echo "HOLD=MISSING_$n"; echo "PATH=$p"; exit 1; }
  a="$(sha "$p")"
  echo "${n}_PATH=$p"
  echo "${n}_SHA256=$a"
  [ "$a" = "$e" ] || { echo "${n}_IDENTITY=FAIL"; exit 1; }
  echo "${n}_IDENTITY=PASS"
}
fetch_exact() {
  local commit="$1" path="$2" out="$3" expected="$4" label="$5"
  local url="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/$commit/$path"
  curl -fsSL "$url" -o "$out"
  echo "${label}_SHA256=$(sha "$out")"
  [ "$(sha "$out")" = "$expected" ] || { echo "HOLD=${label}_IDENTITY_MISMATCH"; exit 1; }
  echo "${label}_IDENTITY=PASS"
}
compile_case() {
  local label="$1" source="$2"
  local out="$TMP/${label}.sigmab" log="$TMP/${label}.log" rc bytes sh
  rm -f "$out" "$log"
  set +e
  "$SIGMAC" "$source" "$out" >"$log" 2>&1
  rc=$?
  set -e
  echo "${label}_COMPILE_RC=$rc"
  if [ -s "$log" ]; then sed "s/^/${label}_LOG=/" "$log"; fi
  if [ -f "$out" ]; then
    bytes="$(wc -c < "$out")"; sh="$(sha "$out")"
    echo "${label}_BYTECODE_BYTES=$bytes"
    echo "${label}_BYTECODE_SHA256=$sh"
    if [ "$sh" = "$EXPECTED_29B" ]; then echo "${label}_BYTECODE_CLASS=HEADER_ONLY_29B"; else echo "${label}_BYTECODE_CLASS=NONTRIVIAL"; fi
  else
    echo "${label}_BYTECODE=ABSENT"
  fi
}

printf '%s\n' '=== C5V3 R4 SUCCESSOR + T1/T2/T3 COMPOSE / COMPILE R1 ==='
echo "MODE=DETERMINISTIC_SOURCE_COMPOSITION_PLUS_COMPILER_BOUNDARY_AUDIT"
echo "VM_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"
echo "PRODUCTION_BINDING=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" "SIGMAC"
lock "$R3" "$EXPECTED_R3" "R3_FIX1_DONOR"

BUNDLE=""
for p in \
  "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip" \
  "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip"; do
  if [ -f "$p" ]; then
    if [ "$(sha "$p")" = "$EXPECTED_GATEA_BUNDLE" ]; then BUNDLE="$p"; break; fi
  fi
done
[ -n "$BUNDLE" ] || { echo "HOLD=EXACT_GATEA_BUNDLE_NOT_FOUND_AT_CANONICAL_PATHS"; exit 1; }
echo "GATEA_BUNDLE_PATH=$BUNDLE"
echo "GATEA_BUNDLE_SHA256=$(sha "$BUNDLE")"

GATEA_CORE="$TMP/gatea_core.sigma"
MEMBER='SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2/SIGMA_C5_C5V3_M5_BLIND_SCOPED_PROVISIONAL_EPISTEMIC_TRUTH_R1/core.sigma'
unzip -p "$BUNDLE" "$MEMBER" > "$GATEA_CORE"
lock "$GATEA_CORE" "$EXPECTED_GATEA_SOURCE" "GATEA_SOURCE"

BASE='https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom'
STATE="$MOD/C5_NATIVE_LEARNING_STATE_R2.sigma.inc"
TRANS="$MOD/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc"
ADAPTER="$MOD/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc"
DURABLE="$MOD/C5_R4_DURABLE_LEARNING_MODEL_R1.sigma.inc"
KERNEL="$MOD/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R3.sigma.inc"
P0="$MOD/C5_R4_P0_TRANSACTION_TRUST_R1.sigma.inc"
MAIN="$MOD/C5_R4_TRANSACTION_CYCLE_MAIN_R1.sigma.inc"

fetch_exact "$STATE_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R2.sigma.inc' "$STATE" "$EXPECTED_STATE" STATE_R2
fetch_exact "$TRANS_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc' "$TRANS" "$EXPECTED_TRANS" TRANSITIONS_R2
fetch_exact "$ADAPTER_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc' "$ADAPTER" "$EXPECTED_ADAPTER" ADAPTER_R3
fetch_exact "$DURABLE_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_DURABLE_LEARNING_MODEL_R1.sigma.inc' "$DURABLE" "$EXPECTED_DURABLE" DURABLE_R1
fetch_exact "$KERNEL_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R3.sigma.inc' "$KERNEL" "$EXPECTED_KERNEL" KERNEL_R3
fetch_exact "$P0_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_P0_TRANSACTION_TRUST_R1.sigma.inc' "$P0" "$EXPECTED_P0" P0_R4
fetch_exact "$MAIN_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_TRANSACTION_CYCLE_MAIN_R1.sigma.inc' "$MAIN" "$EXPECTED_MAIN" MAIN_R1

GATEA_PURE="$MOD/C5_GATEA_PURE_DONOR_EXACT_R1.sigma.inc"
TOOLS="$MOD/C5_T1_T2_T3_ADMITTED_R6_EXACT_R1.sigma.inc"
R4_PURE="$TMP/r4_92.sigma.inc"
cat "$STATE" "$TRANS" "$ADAPTER" "$DURABLE" "$KERNEL" "$P0" > "$R4_PURE"

python - "$GATEA_CORE" "$R3" "$GATEA_PURE" "$TOOLS" "$EXPECTED_GATEA_PURE_NORMALIZED" "$EXPECTED_T123_NORMALIZED" <<'PY'
from pathlib import Path
import hashlib,re,sys
gatea_path,r3_path,gout,tout,eg,et=sys.argv[1:]

def blocks(text):
    lines=text.splitlines(True); out=[]; i=0
    while i < len(lines):
        m=re.match(r'^DEF\s+([A-Za-z0-9_]+)\s*\(', lines[i])
        if not m: i+=1; continue
        name=m.group(1); depth=0; started=False; buf=[]; j=i
        while j < len(lines):
            line=lines[j]; buf.append(line)
            # SIGMA admitted donor defs contain no brace-bearing string literals in the tested slices.
            depth += line.count('{'); depth -= line.count('}')
            if '{' in line: started=True
            if started and depth==0: break
            j+=1
        if not started or depth!=0: raise SystemExit('HOLD=UNBALANCED_DEF:'+name)
        out.append((name,''.join(buf).rstrip('\n'))); i=j+1
    return out

def normalized(bs): return '\n\n'.join(b for _,b in bs)+'\n'

g=blocks(Path(gatea_path).read_text())
if len(g)!=78: raise SystemExit('HOLD=GATEA_DEF_COUNT:'+str(len(g)))
if sum(1 for n,_ in g if n=='append_line')!=1: raise SystemExit('HOLD=GATEA_APPEND_LINE_COUNT')
gp=[x for x in g if x[0]!='append_line']
gtxt=normalized(gp); gh=hashlib.sha256(gtxt.encode()).hexdigest()
print('GATEA_PURE_DEF_COUNT='+str(len(gp))); print('GATEA_PURE_NORMALIZED_SHA256='+gh)
if gh!=eg: raise SystemExit('HOLD=GATEA_PURE_NORMALIZED_IDENTITY')
Path(gout).write_text(gtxt)

r=blocks(Path(r3_path).read_text())
print('R3_PARSED_DEF_COUNT='+str(len(r)))
if len(r)!=176: raise SystemExit('HOLD=R3_PARSED_DEF_COUNT')
names=[n for n,_ in r]
try: a=names.index('WA_H'); b=names.index('T2_SHORTEST_PATH_BOUNDED')
except ValueError as e: raise SystemExit('HOLD=T123_BOUNDARY_NAME_MISSING')
if a!=94 or b!=175 or b-a+1!=82: raise SystemExit(f'HOLD=T123_POSITION_BOUNDARY:{a+1}:{b+1}')
tb=r[a:b+1]; ttxt=normalized(tb); th=hashlib.sha256(ttxt.encode()).hexdigest()
print('T1_T2_T3_DEF_COUNT='+str(len(tb))); print('T1_T2_T3_NORMALIZED_SHA256='+th)
print('T1_T2_T3_FIRST_DEF='+tb[0][0]); print('T1_T2_T3_LAST_DEF='+tb[-1][0])
if th!=et: raise SystemExit('HOLD=T123_NORMALIZED_IDENTITY')
Path(tout).write_text(ttxt)
PY

echo "GATEA_PURE_SHA256=$(sha "$GATEA_PURE")"
echo "T1_T2_T3_SHA256=$(sha "$TOOLS")"

python - "$HEADER" "$GATEA_PURE" "$STATE" "$TRANS" "$ADAPTER" "$DURABLE" "$KERNEL" "$P0" "$TOOLS" "$MAIN" "$SRC" <<'PY'
from pathlib import Path
import hashlib,re,sys
header=sys.argv[1]; paths=sys.argv[2:-1]; out=sys.argv[-1]
parts=[Path(p).read_text().rstrip() for p in paths]
s=header+'\n\n'+'\n\n'.join(parts)+'\n'
Path(out).write_text(s)
names=re.findall(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',s,re.M)
print('SUCCESSOR_DEF_COUNT='+str(len(names)))
print('SUCCESSOR_UNIQUE_DEF_COUNT='+str(len(set(names))))
print('SUCCESSOR_ENTRY_COUNT='+str(sum(1 for x in s.splitlines() if x.startswith('⟡('))))
print('SUCCESSOR_HEADER_COUNT='+str(sum(1 for x in s.splitlines() if x.startswith('#SIGMAUNIVERSE_LANGUAGE['))))
print('SUCCESSOR_SOURCE_BYTES='+str(len(s.encode())))
print('SUCCESSOR_SOURCE_SHA256='+hashlib.sha256(s.encode()).hexdigest())
if len(names)!=251 or len(set(names))!=251: raise SystemExit('HOLD=SUCCESSOR_DEF_IDENTITY')
if sum(1 for x in s.splitlines() if x.startswith('⟡('))!=1: raise SystemExit('HOLD=SUCCESSOR_ENTRY_COUNT')
if sum(1 for x in s.splitlines() if x.startswith('#SIGMAUNIVERSE_LANGUAGE['))!=1: raise SystemExit('HOLD=SUCCESSOR_HEADER_COUNT')
for token in ('legacy_analyze_segment','legacy_merge_evidence','LEFT=','RIGHT='):
    c=s.count(token); print('FORBIDDEN_'+token.replace('=','_EQ')+'_COUNT='+str(c))
    if c: raise SystemExit('HOLD=FORBIDDEN:'+token)
if 'DEF append_line(' in s: raise SystemExit('HOLD=GATEA_APPEND_LINE_PRESENT')
print('SUCCESSOR_STATIC_COMPOSITION=PASS')
PY

echo "SUCCESSOR_SOURCE_PATH=$SRC"
echo "SUCCESSOR_SOURCE_SHA256=$(sha "$SRC")"

make_sentinel() {
  local out="$1"; shift
  { echo "$HEADER"; echo; for p in "$@"; do cat "$p"; echo; done; cat <<EOF
⟡($ENTRY) {
    ⚡ print("COMPILER_BOUNDARY_SENTINEL");
}
EOF
  } > "$out"
}

S1="$TMP/S1_GATEA.sigma"; make_sentinel "$S1" "$GATEA_PURE"
S2="$TMP/S2_GATEA_P0.sigma"; make_sentinel "$S2" "$GATEA_PURE" "$P0"
S3="$TMP/S3_GATEA_R4_NO_P0.sigma"; make_sentinel "$S3" "$GATEA_PURE" "$STATE" "$TRANS" "$ADAPTER" "$DURABLE" "$KERNEL"
S4="$TMP/S4_GATEA_TOOLS.sigma"; make_sentinel "$S4" "$GATEA_PURE" "$TOOLS"
S5="$TMP/S5_GATEA_R4.sigma"; make_sentinel "$S5" "$GATEA_PURE" "$STATE" "$TRANS" "$ADAPTER" "$DURABLE" "$KERNEL" "$P0"
S6="$TMP/S6_ALL_DEFS.sigma"; make_sentinel "$S6" "$GATEA_PURE" "$STATE" "$TRANS" "$ADAPTER" "$DURABLE" "$KERNEL" "$P0" "$TOOLS"

printf '%s\n' '=== COMPILER BOUNDARY MATRIX ==='
compile_case S1_GATEA77 "$S1"
compile_case S2_GATEA77_P0_14 "$S2"
compile_case S3_GATEA77_R4_NO_P0_78 "$S3"
compile_case S4_GATEA77_TOOLS82 "$S4"
compile_case S5_GATEA77_R4_92 "$S5"
compile_case S6_ALL_251_DEFS "$S6"
compile_case FINAL_SUCCESSOR "$SRC"

CF="$TMP/final_counterfactual.sigma"
python - "$SRC" "$CF" <<'PY'
from pathlib import Path
import sys
s=Path(sys.argv[1]).read_text()
a='⚡ print("R4_NATIVE_LEARNING_TRANSACTION_MAIN", "ACTIVE_SOURCE_ONLY");'
b='⚡ print("R4_NATIVE_LEARNING_TRANSACTION_MAIN", "ACTIVE_SOURCE_COUNTERFACTUAL");'
if s.count(a)!=1: raise SystemExit('HOLD=MAIN_COUNTERFACTUAL_TARGET_COUNT')
Path(sys.argv[2]).write_text(s.replace(a,b,1))
PY
compile_case FINAL_COUNTERFACTUAL "$CF"

BAD="$TMP/final_unbalanced.sigma"
python - "$SRC" "$BAD" <<'PY'
from pathlib import Path
import sys
s=Path(sys.argv[1]).read_text().rstrip()
if not s.endswith('}'): raise SystemExit('HOLD=FINAL_BRACE_NOT_FOUND')
Path(sys.argv[2]).write_text(s[:-1]+'\n')
PY
compile_case FINAL_UNBALANCED "$BAD"

if [ -f "$TMP/FINAL_SUCCESSOR.sigmab" ]; then cp "$TMP/FINAL_SUCCESSOR.sigmab" "$BIN"; fi

FINAL_SHA="ABSENT"; CF_SHA="ABSENT"
[ -f "$TMP/FINAL_SUCCESSOR.sigmab" ] && FINAL_SHA="$(sha "$TMP/FINAL_SUCCESSOR.sigmab")"
[ -f "$TMP/FINAL_COUNTERFACTUAL.sigmab" ] && CF_SHA="$(sha "$TMP/FINAL_COUNTERFACTUAL.sigmab")"
if [ "$FINAL_SHA" != "ABSENT" ] && [ "$FINAL_SHA" != "$EXPECTED_29B" ]; then echo "SUCCESSOR_NONTRIVIAL_EMISSION=PASS"; else echo "SUCCESSOR_NONTRIVIAL_EMISSION=NO"; fi
if [ "$FINAL_SHA" != "ABSENT" ] && [ "$CF_SHA" != "ABSENT" ] && [ "$FINAL_SHA" != "$CF_SHA" ]; then echo "SUCCESSOR_MAIN_SOURCE_SENSITIVITY=PASS"; else echo "SUCCESSOR_MAIN_SOURCE_SENSITIVITY=NO"; fi

echo "T1_T2_T3_SUCCESSOR_COMPOSITION=PRESENT_EXACT_BODY_SCOPE"
echo "T1_T2_T3_NATIVE_UTILIZATION=NOT_YET_PROVEN"
echo "R4_RUNTIME_LEARNING=NOT_ADMITTED"
echo "VM_EXECUTION=NO"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"
printf '%s\n' '=== END ==='
