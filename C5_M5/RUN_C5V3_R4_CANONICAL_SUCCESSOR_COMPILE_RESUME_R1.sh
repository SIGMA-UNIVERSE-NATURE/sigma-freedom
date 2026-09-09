#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
SRC="$ROOT/.sigma_c5v3_sync/C5V3_R4_SUCCESSOR_CANONICAL_R1/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
BIN="$ROOT/.sigma_c5v3_sync/C5V3_R4_SUCCESSOR_CANONICAL_R1/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R4_CANONICAL_RESUME_R1_$$"
mkdir -p "$(dirname "$BIN")" "$TMP"
trap 'rm -rf "$TMP"' EXIT

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_CANONICAL_SOURCE="48e1255637a70eb0c9cec0aa60ed7d8e6dfe4de0cfdc011dbeace94bc449cf6c"
EXPECTED_LIVE_CORE="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"

sha(){ sha256sum "$1" | awk '{print $1}'; }
lock(){
  local p="$1"
  local e="$2"
  local n="$3"
  local a
  [ -f "$p" ] || { echo "HOLD=MISSING_$n"; echo "PATH=$p"; exit 1; }
  a="$(sha "$p")"
  echo "${n}_PATH=$p"
  echo "${n}_SHA256=$a"
  [ "$a" = "$e" ] || { echo "${n}_IDENTITY=FAIL"; exit 1; }
  echo "${n}_IDENTITY=PASS"
}
compile_one(){
  local label="$1"
  local source="$2"
  local out="$TMP/${label}.sigmab"
  local log="$TMP/${label}.log"
  local rc
  rm -f "$out" "$log"
  set +e
  "$SIGMAC" "$source" "$out" >"$log" 2>&1
  rc=$?
  set -e
  echo "${label}_COMPILE_RC=$rc"
  if [ -s "$log" ]; then sed "s/^/${label}_LOG=/" "$log"; fi
  if [ -f "$out" ]; then
    echo "${label}_BYTECODE_BYTES=$(wc -c < "$out")"
    echo "${label}_BYTECODE_SHA256=$(sha "$out")"
  else
    echo "${label}_BYTECODE=ABSENT"
  fi
  return 0
}

printf '%s\n' '=== C5V3 R4 CANONICAL SUCCESSOR COMPILE RESUME R1 ==='
echo 'MODE=CANONICAL_FINAL_SOURCE_SENSITIVITY_AND_NEGATIVE_CONTROL'
echo 'PRIOR_COMMENT_CAUSALITY=PASS_FROM_OPERATOR_RUN'
echo 'VM_EXECUTION=NO'
echo 'PRODUCTION_MUTATION=NO'
echo 'PRODUCTION_BINDING=NO'

lock "$SIGMAC" "$EXPECTED_SIGMAC" SIGMAC
lock "$SRC" "$EXPECTED_CANONICAL_SOURCE" CANONICAL_SOURCE
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE_BEFORE
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER_BEFORE

python - "$SRC" <<'PY'
from pathlib import Path
import re,sys
s=Path(sys.argv[1]).read_text()
defs=len(re.findall(r'^DEF\s+',s,re.M))
entries=sum(1 for x in s.splitlines() if x.startswith('⟡('))
headers=sum(1 for x in s.splitlines() if x.startswith('#SIGMAUNIVERSE_LANGUAGE['))
# Track only top-level non-header # lines.
top=[]; depth=0
for i,line in enumerate(s.splitlines(),1):
    before=depth
    depth += line.count('{')-line.count('}')
    if before==0 and line.startswith('#') and not line.startswith('#SIGMAUNIVERSE_LANGUAGE['): top.append((i,line))
print('CANONICAL_DEF_COUNT='+str(defs))
print('CANONICAL_ENTRY_COUNT='+str(entries))
print('CANONICAL_HEADER_COUNT='+str(headers))
print('CANONICAL_TOPLEVEL_NONHEADER_HASH_LINE_COUNT='+str(len(top)))
if defs!=251: raise SystemExit('HOLD=CANONICAL_DEF_COUNT')
if entries!=1: raise SystemExit('HOLD=CANONICAL_ENTRY_COUNT')
if headers!=1: raise SystemExit('HOLD=CANONICAL_HEADER_COUNT')
if top: raise SystemExit('HOLD=CANONICAL_TOPLEVEL_COMMENT_REMAINS')
PY

compile_one CANONICAL_SUCCESSOR "$SRC"

CF="$TMP/canonical_counterfactual.sigma"
python - "$SRC" "$CF" <<'PY'
from pathlib import Path
import sys
s=Path(sys.argv[1]).read_text()
a='⚡ print("R4_NATIVE_LEARNING_TRANSACTION_MAIN", "ACTIVE_SOURCE_ONLY");'
b='⚡ print("R4_NATIVE_LEARNING_TRANSACTION_MAIN", "ACTIVE_CANONICAL_COUNTERFACTUAL");'
c=s.count(a)
print('CANONICAL_COUNTERFACTUAL_TARGET_COUNT='+str(c))
if c!=1: raise SystemExit('HOLD=CANONICAL_COUNTERFACTUAL_TARGET_COUNT')
Path(sys.argv[2]).write_text(s.replace(a,b,1))
PY
compile_one CANONICAL_COUNTERFACTUAL "$CF"

BAD="$TMP/canonical_unbalanced.sigma"
python - "$SRC" "$BAD" <<'PY'
from pathlib import Path
import sys
s=Path(sys.argv[1]).read_text().rstrip()
if not s.endswith('}'): raise SystemExit('HOLD=CANONICAL_FINAL_BRACE_NOT_FOUND')
Path(sys.argv[2]).write_text(s[:-1]+'\n')
PY
compile_one CANONICAL_UNBALANCED "$BAD"

CAN_B="$TMP/CANONICAL_SUCCESSOR.sigmab"
CF_B="$TMP/CANONICAL_COUNTERFACTUAL.sigmab"
CAN_SHA=ABSENT
CF_SHA=ABSENT
[ -f "$CAN_B" ] && CAN_SHA="$(sha "$CAN_B")"
[ -f "$CF_B" ] && CF_SHA="$(sha "$CF_B")"
if [ "$CAN_SHA" != ABSENT ] && [ "$CF_SHA" != ABSENT ] && [ "$CAN_SHA" != "$CF_SHA" ]; then
  echo 'CANONICAL_MAIN_SOURCE_SENSITIVITY=PASS'
else
  echo 'CANONICAL_MAIN_SOURCE_SENSITIVITY=NO'
fi

set +e
"$SIGMAC" "$BAD" "$TMP/canonical_unbalanced_recheck.sigmab" >/dev/null 2>&1
U_RC=$?
set -e
echo "CANONICAL_UNBALANCED_RECHECK_RC=$U_RC"
if [ "$U_RC" -ne 0 ]; then
  echo 'CANONICAL_UNBALANCED_ENTRY_REJECTED=PASS'
else
  echo 'CANONICAL_UNBALANCED_ENTRY_REJECTED=NO'
fi

if [ -f "$CAN_B" ]; then cp "$CAN_B" "$BIN"; fi
if [ -f "$BIN" ]; then
  echo "CANONICAL_FROZEN_BYTECODE_PATH=$BIN"
  echo "CANONICAL_FROZEN_BYTECODE_BYTES=$(wc -c < "$BIN")"
  echo "CANONICAL_FROZEN_BYTECODE_SHA256=$(sha "$BIN")"
fi

echo 'TOPLEVEL_COMMENT_CAUSALITY=PASS_FROM_PRIOR_OPERATOR_EVIDENCE'
echo 'CANONICAL_SERIALIZATION_RULE=ONE_HEADER_PLUS_251_DEF_BLOCKS_PLUS_ONE_ENTRY'
echo 'T1_T2_T3_SUCCESSOR_COMPOSITION=PRESENT_EXACT_BODY_SCOPE'
echo 'T1_T2_T3_NATIVE_UTILIZATION=NOT_YET_PROVEN'
echo 'R4_RUNTIME_LEARNING=NOT_ADMITTED'

lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE_AFTER
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER_AFTER
echo 'VM_EXECUTION=NO'
echo 'PRODUCTION_BINDING=NO'
echo 'PRODUCTION_MUTATION=NO'
printf '%s\n' '=== END ==='
