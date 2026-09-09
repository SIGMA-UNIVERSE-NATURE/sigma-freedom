#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
R3_SRC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_R3="152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8"
EXPECTED_29B="ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a"
EXPECTED_LIVE_CORE="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"
HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'

TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R3_MULTILINE_DEF_PROBE_R1_$$"
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

echo "=== C5V3 R3 MULTILINE DEF SIGNATURE EMISSION PROBE R1 ==="
echo "MODE=EXACT_R3_SINGLE_GRAMMAR_DELTA_PLUS_MINIMAL_CONTROLS"
echo "VM_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"
echo "DIRECTORY_SCAN=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" "SIGMAC"
lock "$R3_SRC" "$EXPECTED_R3" "R3_SOURCE"
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" "LIVE_CORE_BEFORE"
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" "LIVE_RUNNER_BEFORE"

echo "=== 1. EXACT SOURCE STRUCTURE ==="
python - "$R3_SRC" <<'PY'
from pathlib import Path
import re, sys
s=Path(sys.argv[1]).read_text()
mult=[]
lines=s.splitlines()
for i,line in enumerate(lines):
    if re.match(r'^DEF\s+[A-Za-z0-9_]+\s*\(', line) and '{' not in line:
        mult.append((i+1,line))
print('R3_DEF_COUNT='+str(len(re.findall(r'^DEF\s+',s,flags=re.M))))
print('R3_ENTRY_COUNT='+str(sum(1 for x in lines if x.startswith('⟡('))))
print('R3_MULTILINE_DEF_SIGNATURE_COUNT='+str(len(mult)))
for n,line in mult:
    print(f'R3_MULTILINE_DEF_SIGNATURE={n}|{line}')
PY

echo "=== 2. MINIMAL GRAMMAR CONTROLS ==="
ONE="$TMP/one_line_def.sigma"
MULTI="$TMP/multiline_def.sigma"
cat > "$ONE" <<EOF
$HEADER
DEF pair(a, b) { RETURN a + b; }
⟡(Σ.TEST) {
    ⚡ print(pair("A", "B"));
}
EOF
cat > "$MULTI" <<EOF
$HEADER
DEF pair(
    a,
    b
) {
    RETURN a + b;
}
⟡(Σ.TEST) {
    ⚡ print(pair("A", "B"));
}
EOF
compile_case "MINIMAL_ONE_LINE_DEF" "$ONE"
compile_case "MINIMAL_MULTILINE_DEF" "$MULTI"

echo "=== 3. EXACT R3 SINGLE-DELTA FOLD ==="
FOLDED="$TMP/r3_folded_signature.sigma"
python - "$R3_SRC" "$FOLDED" <<'PY'
from pathlib import Path
import sys
src,out=sys.argv[1:]
s=Path(src).read_text()
old='''DEF p0_receipt_envelope_shape_valid(\n    invocation_id,\n    event_type,\n    expected_phase,\n    parent_state_sha,\n    action_id,\n    receipt_kind\n) {'''
new='DEF p0_receipt_envelope_shape_valid(invocation_id, event_type, expected_phase, parent_state_sha, action_id, receipt_kind) {'
count=s.count(old)
print('EXACT_MULTILINE_SIGNATURE_TARGET_COUNT='+str(count))
if count != 1:
    raise SystemExit('HOLD=EXACT_MULTILINE_SIGNATURE_TARGET_COUNT_NOT_ONE')
s2=s.replace(old,new,1)
Path(out).write_text(s2)
print('FOLDED_SOURCE_BYTES='+str(len(s2.encode())))
print('FOLDED_ENTRY_COUNT='+str(sum(1 for x in s2.splitlines() if x.startswith('⟡('))))
PY
compile_case "R3_FOLDED_SIGNATURE" "$FOLDED"

echo "=== 4. FOLDED-R3 ENTRY VISIBILITY CONTROLS ==="
FOLDED_MUT="$TMP/r3_folded_literal_mutation.sigma"
FOLDED_BAD="$TMP/r3_folded_unbalanced.sigma"
python - "$FOLDED" "$FOLDED_MUT" "$FOLDED_BAD" <<'PY'
from pathlib import Path
import sys
src,mut,bad=sys.argv[1:]
s=Path(src).read_text()
old='⚡ print("R3_FIX1_P0_TRUST_STATE", "ACTIVE");'
new='⚡ print("R3_FIX1_P0_TRUST_STATE", "ACTIVE_COUNTERFACTUAL");'
print('FOLDED_COUNTERFACTUAL_TARGET_COUNT='+str(s.count(old)))
if s.count(old)!=1:
    raise SystemExit('HOLD=FOLDED_COUNTERFACTUAL_TARGET_COUNT_NOT_ONE')
Path(mut).write_text(s.replace(old,new,1))
t=s.rstrip()
if not t.endswith('}'):
    raise SystemExit('HOLD=FOLDED_FINAL_BRACE_NOT_FOUND')
Path(bad).write_text(t[:-1]+'\n')
PY
compile_case "R3_FOLDED_COUNTERFACTUAL" "$FOLDED_MUT"
compile_case "R3_FOLDED_UNBALANCED" "$FOLDED_BAD"

echo "=== 5. CLASSIFICATION ==="
getsha() { [ -f "$1" ] && sha "$1" || echo ABSENT; }
ONE_SHA="$(getsha "$TMP/MINIMAL_ONE_LINE_DEF.sigmab")"
MULTI_SHA="$(getsha "$TMP/MINIMAL_MULTILINE_DEF.sigmab")"
FOLD_SHA="$(getsha "$TMP/R3_FOLDED_SIGNATURE.sigmab")"
MUT_SHA="$(getsha "$TMP/R3_FOLDED_COUNTERFACTUAL.sigmab")"

if [ "$ONE_SHA" != "$EXPECTED_29B" ] && [ "$MULTI_SHA" = "$EXPECTED_29B" ]; then
  echo "MULTILINE_DEF_SIGNATURE_PARSER_QUIRK=PROVEN_BY_MINIMAL_CONTROL"
elif [ "$ONE_SHA" != "$MULTI_SHA" ]; then
  echo "MULTILINE_DEF_SIGNATURE_PARSER_QUIRK=BEHAVIOR_DIFFERS"
else
  echo "MULTILINE_DEF_SIGNATURE_PARSER_QUIRK=NO_OBSERVED"
fi

if [ "$FOLD_SHA" != "$EXPECTED_29B" ] && [ "$FOLD_SHA" != "ABSENT" ]; then
  echo "R3_ZERO_CODE_ROOT_CAUSE_SINGLE_MULTILINE_DEF_SIGNATURE=PROVEN_BY_EXACT_SINGLE_DELTA"
else
  echo "R3_ZERO_CODE_ROOT_CAUSE_SINGLE_MULTILINE_DEF_SIGNATURE=NOT_PROVEN"
fi

if [ "$FOLD_SHA" != "ABSENT" ] && [ "$MUT_SHA" != "ABSENT" ] && [ "$FOLD_SHA" != "$MUT_SHA" ]; then
  echo "FOLDED_R3_MAIN_LITERAL_SENSITIVITY=PASS"
else
  echo "FOLDED_R3_MAIN_LITERAL_SENSITIVITY=FAIL_OR_NOT_REACHED"
fi

echo "NEXT_IF_NOT_PROVEN=DEF_COMPOSITION_VS_MAIN_BINARY_SEARCH"

echo "=== 6. NON-MUTATION RECHECK ==="
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" "LIVE_CORE_AFTER"
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" "LIVE_RUNNER_AFTER"
echo "PRODUCTION_MUTATION=NO"
echo "VM_EXECUTION=NO"
echo "=== END ==="
