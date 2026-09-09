#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
R0_ROOT="$ROOT/.sigma_exec/HH_AUTO_INTERNET_LESSONS/V1_R21_SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0"
R0_SRC="$R0_ROOT/15_SIGMA_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0.sigma"
R0_BC="$R0_ROOT/engines/proposition_span_candidate_formation_v18_r0.sigmab"
R3_SRC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_R0_SRC="81523feb7c59a90b6bb5d284c65a679d3fd76ad692f84b0a6685c4d2693dcb7a"
EXPECTED_R0_BC="e800eab3dc6abcbddf0b9c9e0de9d76af2fba6ba1bd49c87157c62fe126a7300"
EXPECTED_R3_SRC="152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8"
EXPECTED_GATEA_SRC="bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1"
EXPECTED_GATEA_BC="569411458b1bff9c0c9894fd95374a87db6e6e5c04030dc8e8900e1cb0d38ea2"
EXPECTED_29B="ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a"

FULL_HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'
GATEA_HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5M5SCOPEDPROVISIONALEPISTEMICTRUTH1]'

TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R0_GATEA_PROFILE_ORACLE_R1_$$"
mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT

sha() { sha256sum "$1" | awk '{print $1}'; }
lock() {
  local p="$1" e="$2" n="$3" a
  [ -f "$p" ] || { echo "HOLD=MISSING_EXACT_PATH"; echo "PATH=$p"; exit 1; }
  a="$(sha "$p")"
  echo "${n}_PATH=$p"
  echo "${n}_SHA256=$a"
  echo "${n}_BYTES=$(wc -c < "$p")"
  [ "$a" = "$e" ] || { echo "${n}_IDENTITY=FAIL"; exit 1; }
  echo "${n}_IDENTITY=PASS"
}

compile_case() {
  local label src out log rc
  label="$1"
  src="$2"
  out="$TMP/${label}.sigmab"
  log="$TMP/${label}.log"
  rm -f "$out" "$log"
  set +e
  "$SIGMAC" "$src" "$out" >"$log" 2>&1
  rc=$?
  set -e
  echo "${label}_COMPILE_RC=$rc"
  if [ -s "$log" ]; then sed "s/^/${label}_LOG=/" "$log"; fi
  if [ -f "$out" ]; then
    echo "${label}_BYTECODE_SHA256=$(sha "$out")"
    echo "${label}_BYTECODE_BYTES=$(wc -c < "$out")"
    if [ "$(sha "$out")" = "$EXPECTED_29B" ]; then
      echo "${label}_BYTECODE_CLASS=HEADER_ONLY_29B"
    else
      echo "${label}_BYTECODE_CLASS=NONTRIVIAL"
    fi
  else
    echo "${label}_BYTECODE=ABSENT"
  fi
}

replace_header() {
  local src="$1" out="$2" new_header="$3"
  python - "$src" "$out" "$new_header" <<'PY'
from pathlib import Path
import sys
src,out,new=sys.argv[1:]
s=Path(src).read_text()
lines=s.splitlines(True)
if not lines or not lines[0].startswith('#SIGMAUNIVERSE_LANGUAGE['):
    raise SystemExit('HOLD=SOURCE_HEADER_NOT_FIRST_LINE')
eol='\n' if lines[0].endswith('\n') else ''
lines[0]=new+eol
Path(out).write_text(''.join(lines))
print('MUTATED_HEADER='+new)
PY
}

echo "=== C5V3 R0 + GATE-A VERSION PROFILE COMPILER ORACLE R1 ==="
echo "MODE=FRESH_COMPILE_EXACT_R0_GATEA_R3_WITH_HEADER_COUNTERFACTUALS"
echo "VM_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"
echo "DIRECTORY_SCAN=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" "SIGMAC"
lock "$R0_SRC" "$EXPECTED_R0_SRC" "R0_SOURCE"
lock "$R0_BC" "$EXPECTED_R0_BC" "R0_FROZEN_BYTECODE"
lock "$R3_SRC" "$EXPECTED_R3_SRC" "R3_FIX1_SOURCE"

echo "=== 1. RESOLVE EXACT GATE-A PARENT FROM KNOWN BUNDLE PATHS ==="
BUNDLE=""
for p in \
  "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip" \
  "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip" \
  "$HOME/storage/downloads/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip" \
  "$HOME/storage/downloads/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip"
do
  if [ -f "$p" ]; then BUNDLE="$p"; break; fi
done
[ -n "$BUNDLE" ] || { echo "HOLD=GATEA_BUNDLE_NOT_FOUND_AT_EXACT_PATHS"; exit 1; }
echo "GATEA_BUNDLE_PATH=$BUNDLE"
echo "GATEA_BUNDLE_SHA256=$(sha "$BUNDLE")"
GATEA_SRC="$TMP/gatea_original.sigma"
python - "$BUNDLE" "$GATEA_SRC" "$EXPECTED_GATEA_SRC" <<'PY'
import hashlib,sys,zipfile
bundle,out,expected=sys.argv[1:]
with zipfile.ZipFile(bundle) as z:
    hits=[]
    for n in z.namelist():
        if n.endswith('/core.sigma'):
            b=z.read(n)
            if hashlib.sha256(b).hexdigest()==expected:
                hits.append((n,b))
if not hits:
    raise SystemExit('HOLD=GATEA_PARENT_SHA_NOT_FOUND')
hits.sort(key=lambda x:x[0])
open(out,'wb').write(hits[0][1])
print('GATEA_MEMBER='+hits[0][0])
print('GATEA_MATCH_COUNT='+str(len(hits)))
print('GATEA_SOURCE_SHA256='+hashlib.sha256(hits[0][1]).hexdigest())
PY
lock "$GATEA_SRC" "$EXPECTED_GATEA_SRC" "GATEA_SOURCE"

echo "=== 2. ORIGINAL HEADERS / ENTRY COUNTS ==="
python - "$R0_SRC" "$GATEA_SRC" "$R3_SRC" <<'PY'
from pathlib import Path
import sys,re
for label,p in zip(('R0','GATEA','R3_FIX1'),sys.argv[1:]):
    s=Path(p).read_text()
    print(f'{label}_HEADER={s.splitlines()[0] if s.splitlines() else ""}')
    print(f'{label}_ENTRY_COUNT={sum(1 for line in s.splitlines() if line.startswith("⟡("))}')
    print(f'{label}_DEF_COUNT={len(re.findall(r"^DEF\s+",s,flags=re.M))}')
PY

echo "=== 3. FRESH ORIGINAL COMPILES ==="
compile_case "R0_ORIGINAL" "$R0_SRC"
compile_case "GATEA_ORIGINAL" "$GATEA_SRC"
compile_case "R3_ORIGINAL" "$R3_SRC"

echo "R0_FRESH_MATCHES_FROZEN=$([ -f "$TMP/R0_ORIGINAL.sigmab" ] && [ "$(sha "$TMP/R0_ORIGINAL.sigmab")" = "$EXPECTED_R0_BC" ] && echo YES || echo NO)"
echo "GATEA_FRESH_MATCHES_HISTORICAL=$([ -f "$TMP/GATEA_ORIGINAL.sigmab" ] && [ "$(sha "$TMP/GATEA_ORIGINAL.sigmab")" = "$EXPECTED_GATEA_BC" ] && echo YES || echo NO)"

echo "=== 4. HEADER PROFILE COUNTERFACTUALS ==="
R0_FULL="$TMP/r0_forced_c5fullr1.sigma"
GATEA_FULL="$TMP/gatea_forced_c5fullr1.sigma"
R3_GATEA="$TMP/r3_forced_gatea_version.sigma"
replace_header "$R0_SRC" "$R0_FULL" "$FULL_HEADER"
replace_header "$GATEA_SRC" "$GATEA_FULL" "$FULL_HEADER"
replace_header "$R3_SRC" "$R3_GATEA" "$GATEA_HEADER"
compile_case "R0_FORCED_C5FULLR1" "$R0_FULL"
compile_case "GATEA_FORCED_C5FULLR1" "$GATEA_FULL"
compile_case "R3_FORCED_GATEA_VERSION" "$R3_GATEA"

echo "=== 5. CLASSIFICATION ==="
getsha() { [ -f "$1" ] && sha "$1" || echo ABSENT; }
R0O="$(getsha "$TMP/R0_ORIGINAL.sigmab")"
R0F="$(getsha "$TMP/R0_FORCED_C5FULLR1.sigmab")"
GAO="$(getsha "$TMP/GATEA_ORIGINAL.sigmab")"
GAF="$(getsha "$TMP/GATEA_FORCED_C5FULLR1.sigmab")"
R3O="$(getsha "$TMP/R3_ORIGINAL.sigmab")"
R3G="$(getsha "$TMP/R3_FORCED_GATEA_VERSION.sigmab")"

echo "R0_ORIGINAL_SHA=$R0O"
echo "R0_FORCED_C5FULLR1_SHA=$R0F"
echo "GATEA_ORIGINAL_SHA=$GAO"
echo "GATEA_FORCED_C5FULLR1_SHA=$GAF"
echo "R3_ORIGINAL_SHA=$R3O"
echo "R3_FORCED_GATEA_VERSION_SHA=$R3G"

if [ "$GAO" != "$EXPECTED_29B" ] && [ "$GAF" = "$EXPECTED_29B" ]; then
  echo "GATEA_VERSION_PROFILE_EFFECT=PROVEN_C5FULLR1_COLLAPSES_GATEA_TO_HEADER_ONLY"
elif [ "$GAO" != "$GAF" ]; then
  echo "GATEA_VERSION_PROFILE_EFFECT=YES_BUT_NOT_SIMPLE_29B_COLLAPSE"
else
  echo "GATEA_VERSION_PROFILE_EFFECT=NO_OBSERVED"
fi

if [ "$R0O" != "$EXPECTED_29B" ] && [ "$R0F" = "$EXPECTED_29B" ]; then
  echo "R0_VERSION_PROFILE_EFFECT=PROVEN_C5FULLR1_COLLAPSES_R0_TO_HEADER_ONLY"
elif [ "$R0O" != "$R0F" ]; then
  echo "R0_VERSION_PROFILE_EFFECT=YES_BUT_NOT_SIMPLE_29B_COLLAPSE"
else
  echo "R0_VERSION_PROFILE_EFFECT=NO_OBSERVED"
fi

if [ "$R3O" = "$EXPECTED_29B" ] && [ "$R3G" != "$EXPECTED_29B" ] && [ "$R3G" != "ABSENT" ]; then
  echo "R3_GATEA_VERSION_RESTORES_NONTRIVIAL_EMISSION=YES"
else
  echo "R3_GATEA_VERSION_RESTORES_NONTRIVIAL_EMISSION=NO"
fi

echo "PRODUCTION_MUTATION=NO"
echo "VM_EXECUTION=NO"
echo "=== END ==="
