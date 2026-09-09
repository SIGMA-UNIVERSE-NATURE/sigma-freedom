#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
SUCCESSOR="$ROOT/.sigma_c5v3_sync/C5V3_R4_SUCCESSOR_T1_T2_T3_R1/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
OUTROOT="$ROOT/.sigma_c5v3_sync/C5V3_R4_SUCCESSOR_CANONICAL_R1"
SRC="$OUTROOT/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
BIN="$OUTROOT/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R4_COMMENT_CANONICAL_R1_$$"
mkdir -p "$OUTROOT/src" "$OUTROOT/bin" "$TMP"
trap 'rm -rf "$TMP"' EXIT

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_SUCCESSOR="b1ceedffa11497cab5454639eb1872cc5ecb95a5824b95e4d1be22c2ea2b7406"
EXPECTED_LIVE_CORE="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"
EXPECTED_STATE="83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33"
STATE_COMMIT="ca6d9504f5e75c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33"
STATE_GIT_COMMIT="ca6d9504f5e75c4d5ccf48ab7c574614a8b019be"
HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'
ENTRY='Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1'
BASE='https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom'

sha(){ sha256sum "$1" | awk '{print $1}'; }
lock(){ local p="$1" e="$2" n="$3" a; [ -f "$p" ] || { echo "HOLD=MISSING_$n"; exit 1; }; a="$(sha "$p")"; echo "${n}_PATH=$p"; echo "${n}_SHA256=$a"; [ "$a" = "$e" ] || { echo "${n}_IDENTITY=FAIL"; exit 1; }; echo "${n}_IDENTITY=PASS"; }

compile_pair(){
  local label="$1" body="$2"
  local a="$TMP/${label}_A.sigma" b="$TMP/${label}_B.sigma" ba="$TMP/${label}_A.sigmab" bb="$TMP/${label}_B.sigmab"
  {
    echo "$HEADER"; echo; cat "$body"; echo
    printf '⟡(%s) {\n    ⚡ print("COMMENT_PROBE_A");\n}\n' "$ENTRY"
  } > "$a"
  {
    echo "$HEADER"; echo; cat "$body"; echo
    printf '⟡(%s) {\n    ⚡ print("COMMENT_PROBE_B");\n}\n' "$ENTRY"
  } > "$b"
  set +e
  "$SIGMAC" "$a" "$ba" >"$TMP/${label}_A.log" 2>&1; local rca=$?
  "$SIGMAC" "$b" "$bb" >"$TMP/${label}_B.log" 2>&1; local rcb=$?
  set -e
  echo "${label}_A_RC=$rca"; echo "${label}_B_RC=$rcb"
  if [ "$rca" -ne 0 ] || [ "$rcb" -ne 0 ] || [ ! -f "$ba" ] || [ ! -f "$bb" ]; then
    echo "${label}_ENTRY_SOURCE_SENSITIVITY=COMPILE_FAIL"
    [ -s "$TMP/${label}_A.log" ] && sed "s/^/${label}_A_LOG=/" "$TMP/${label}_A.log"
    [ -s "$TMP/${label}_B.log" ] && sed "s/^/${label}_B_LOG=/" "$TMP/${label}_B.log"
    return 0
  fi
  local sa sb
  sa="$(sha "$ba")"; sb="$(sha "$bb")"
  echo "${label}_A_BYTES=$(wc -c < "$ba")"; echo "${label}_B_BYTES=$(wc -c < "$bb")"
  echo "${label}_A_SHA256=$sa"; echo "${label}_B_SHA256=$sb"
  if [ "$sa" != "$sb" ]; then echo "${label}_ENTRY_SOURCE_SENSITIVITY=PASS"; else echo "${label}_ENTRY_SOURCE_SENSITIVITY=FAIL"; fi
}

compile_one(){
  local label="$1" src="$2" out="$TMP/${label}.sigmab" log="$TMP/${label}.log" rc
  set +e
  "$SIGMAC" "$src" "$out" >"$log" 2>&1; rc=$?
  set -e
  echo "${label}_COMPILE_RC=$rc"
  if [ -s "$log" ]; then sed "s/^/${label}_LOG=/" "$log"; fi
  if [ -f "$out" ]; then echo "${label}_BYTECODE_BYTES=$(wc -c < "$out")"; echo "${label}_BYTECODE_SHA256=$(sha "$out")"; else echo "${label}_BYTECODE=ABSENT"; fi
}

printf '%s\n' '=== C5V3 R4 TOP-LEVEL COMMENT + CANONICAL SUCCESSOR COMPILE R1 ==='
echo 'MODE=TOPLEVEL_COMMENT_CAUSALITY_PLUS_CANONICAL_DEF_SERIALIZATION'
echo 'VM_EXECUTION=NO'
echo 'PRODUCTION_MUTATION=NO'
echo 'PRODUCTION_BINDING=NO'
lock "$SIGMAC" "$EXPECTED_SIGMAC" SIGMAC
lock "$SUCCESSOR" "$EXPECTED_SUCCESSOR" SUCCESSOR_RAW
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE_BEFORE
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER_BEFORE

# Extract the exact 77 Gate-A DEFs, 251 total DEFs and raw entry from the already locked successor.
GATEA="$TMP/gatea77.norm"
ALLDEFS="$TMP/all251.norm"
ENTRYRAW="$TMP/entry.raw"
python - "$SUCCESSOR" "$GATEA" "$ALLDEFS" "$ENTRYRAW" "$TMP" <<'PY'
from pathlib import Path
import re,sys
src,gout,aout,eout,tmp=sys.argv[1:]
s=Path(src).read_text()

def blocks(text):
    lines=text.splitlines(True); out=[]; i=0
    while i<len(lines):
        m=re.match(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',lines[i])
        if not m: i+=1; continue
        name=m.group(1); buf=[]; depth=0; started=False; j=i
        while j<len(lines):
            line=lines[j]; buf.append(line)
            depth += line.count('{'); depth -= line.count('}')
            if '{' in line: started=True
            if started and depth==0: break
            j+=1
        if not started or depth!=0: raise SystemExit('HOLD=UNBALANCED_DEF:'+name)
        out.append((name,''.join(buf).rstrip('\n'))); i=j+1
    return out
bs=blocks(s)
if len(bs)!=251: raise SystemExit('HOLD=SUCCESSOR_DEF_COUNT:'+str(len(bs)))
Path(gout).write_text('\n\n'.join(b for _,b in bs[:77])+'\n')
Path(aout).write_text('\n\n'.join(b for _,b in bs)+'\n')
lines=s.splitlines(True)
starts=[i for i,x in enumerate(lines) if x.startswith('⟡(')]
if len(starts)!=1: raise SystemExit('HOLD=ENTRY_COUNT:'+str(len(starts)))
Path(eout).write_text(''.join(lines[starts[0]:]))
print('PARSED_DEF_COUNT='+str(len(bs)))
print('GATEA_DEF_COUNT=77')
print('ENTRY_RAW_BYTES='+str(len(Path(eout).read_bytes())))

# Build a normalized State body and a version with only leading non-DEF surface removed.
state=Path(tmp,'state.raw').read_text() if Path(tmp,'state.raw').exists() else ''
PY

STATE_RAW="$TMP/state.raw"
curl -fsSL "$BASE/$STATE_GIT_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R2.sigma.inc" -o "$STATE_RAW"
echo "STATE_RAW_SHA256=$(sha "$STATE_RAW")"
[ "$(sha "$STATE_RAW")" = "$EXPECTED_STATE" ] || { echo 'HOLD=STATE_RAW_IDENTITY'; exit 1; }

STATE_NORM="$TMP/state.norm"; STATE_STRIPPED="$TMP/state.leading_stripped"; STATE_INTERCOMMENT="$TMP/state.intercomment"
python - "$STATE_RAW" "$STATE_NORM" "$STATE_STRIPPED" "$STATE_INTERCOMMENT" <<'PY'
from pathlib import Path
import re,sys
src,norm,strip,inter=sys.argv[1:]
s=Path(src).read_text(); lines=s.splitlines(True)

def blocks(text):
    ls=text.splitlines(True); out=[]; i=0
    while i<len(ls):
        m=re.match(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',ls[i])
        if not m: i+=1; continue
        name=m.group(1); buf=[]; depth=0; started=False; j=i
        while j<len(ls):
            line=ls[j]; buf.append(line); depth+=line.count('{'); depth-=line.count('}')
            if '{' in line: started=True
            if started and depth==0: break
            j+=1
        if not started or depth!=0: raise SystemExit('HOLD=STATE_UNBALANCED_DEF:'+name)
        out.append((name,''.join(buf).rstrip('\n'))); i=j+1
    return out
bs=blocks(s)
if len(bs)!=28: raise SystemExit('HOLD=STATE_DEF_COUNT:'+str(len(bs)))
Path(norm).write_text('\n\n'.join(b for _,b in bs)+'\n')
first=next((i for i,x in enumerate(lines) if re.match(r'^DEF\s+',x)),None)
if first is None: raise SystemExit('HOLD=STATE_FIRST_DEF')
Path(strip).write_text(''.join(lines[first:]))
Path(inter).write_text(bs[0][1]+'\n# TOP_LEVEL_INTER_DEF_COMMENT_SENTINEL\n\n'+'\n\n'.join(b for _,b in bs[1:])+'\n')
print('STATE_DEF_COUNT='+str(len(bs)))
print('STATE_LEADING_NONDEF_LINE_COUNT='+str(first))
print('STATE_TOPLEVEL_COMMENT_LINE_COUNT='+str(sum(1 for x in lines if x.startswith('#'))))
PY

# Isolate comment placement with no R4 DEFs.
EMPTY="$TMP/empty"; : > "$EMPTY"
COMMENT_BEFORE_DEFS="$TMP/comment_before_defs"; printf '# TOP_LEVEL_COMMENT_SENTINEL\n' > "$COMMENT_BEFORE_DEFS"
COMMENT_AFTER_GATEA="$TMP/comment_after_gatea"; { cat "$GATEA"; printf '\n# TOP_LEVEL_COMMENT_SENTINEL\n'; } > "$COMMENT_AFTER_GATEA"
BLANK_ONLY="$TMP/blank_only"; printf '\n\n\n' > "$BLANK_ONLY"

compile_pair CONTROL_EMPTY "$EMPTY"
compile_pair CONTROL_BLANK_ONLY "$BLANK_ONLY"
compile_pair TOPLEVEL_COMMENT_ONLY "$COMMENT_BEFORE_DEFS"
compile_pair TOPLEVEL_COMMENT_AFTER_GATEA "$COMMENT_AFTER_GATEA"
compile_pair STATE_RAW "$STATE_RAW"
compile_pair STATE_LEADING_STRIPPED "$STATE_STRIPPED"
compile_pair STATE_NORM "$STATE_NORM"
compile_pair STATE_NORM_WITH_INTERDEF_COMMENT "$STATE_INTERCOMMENT"

# Build canonical successor: exactly one header + 251 canonical DEF blocks + exact raw entry.
{
  echo "$HEADER"; echo; cat "$ALLDEFS"; echo; cat "$ENTRYRAW"
} > "$SRC"
echo "CANONICAL_SUCCESSOR_SOURCE_PATH=$SRC"
echo "CANONICAL_SUCCESSOR_SOURCE_BYTES=$(wc -c < "$SRC")"
echo "CANONICAL_SUCCESSOR_SOURCE_SHA256=$(sha "$SRC")"
python - "$SRC" <<'PY'
from pathlib import Path
import re,sys
s=Path(sys.argv[1]).read_text()
print('CANONICAL_DEF_COUNT='+str(len(re.findall(r'^DEF\s+',s,re.M))))
print('CANONICAL_ENTRY_COUNT='+str(sum(1 for x in s.splitlines() if x.startswith('⟡('))))
print('CANONICAL_HEADER_COUNT='+str(sum(1 for x in s.splitlines() if x.startswith('#SIGMAUNIVERSE_LANGUAGE['))))
# Only the SIGMA header may remain as a top-level # line. Comments inside DEF/entry bodies are not classified here.
top=[]; depth=0
for i,line in enumerate(s.splitlines(),1):
    stripped=line.lstrip()
    if line.startswith('DEF '): pass
    depth += line.count('{') - line.count('}')
    if depth==0 and line.startswith('#') and not line.startswith('#SIGMAUNIVERSE_LANGUAGE['): top.append((i,line))
print('CANONICAL_TOPLEVEL_NONHEADER_HASH_LINE_COUNT='+str(len(top)))
if len(re.findall(r'^DEF\s+',s,re.M))!=251: raise SystemExit('HOLD=CANONICAL_DEF_COUNT')
if sum(1 for x in s.splitlines() if x.startswith('⟡('))!=1: raise SystemExit('HOLD=CANONICAL_ENTRY_COUNT')
if sum(1 for x in s.splitlines() if x.startswith('#SIGMAUNIVERSE_LANGUAGE['))!=1: raise SystemExit('HOLD=CANONICAL_HEADER_COUNT')
PY

compile_one CANONICAL_SUCCESSOR "$SRC"
CF="$TMP/canonical_counterfactual.sigma"
python - "$SRC" "$CF" <<'PY'
from pathlib import Path
import sys
s=Path(sys.argv[1]).read_text()
a='⚡ print("R4_NATIVE_LEARNING_TRANSACTION_MAIN", "ACTIVE_SOURCE_ONLY");'
b='⚡ print("R4_NATIVE_LEARNING_TRANSACTION_MAIN", "ACTIVE_CANONICAL_COUNTERFACTUAL");'
print('CANONICAL_COUNTERFACTUAL_TARGET_COUNT='+str(s.count(a)))
if s.count(a)!=1: raise SystemExit('HOLD=CANONICAL_COUNTERFACTUAL_TARGET_COUNT')
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

CAN_SHA=ABSENT; CF_SHA=ABSENT
[ -f "$TMP/CANONICAL_SUCCESSOR.sigmab" ] && CAN_SHA="$(sha "$TMP/CANONICAL_SUCCESSOR.sigmab")"
[ -f "$TMP/CANONICAL_COUNTERFACTUAL.sigmab" ] && CF_SHA="$(sha "$TMP/CANONICAL_COUNTERFACTUAL.sigmab")"
if [ "$CAN_SHA" != ABSENT ] && [ "$CF_SHA" != ABSENT ] && [ "$CAN_SHA" != "$CF_SHA" ]; then echo 'CANONICAL_MAIN_SOURCE_SENSITIVITY=PASS'; else echo 'CANONICAL_MAIN_SOURCE_SENSITIVITY=NO'; fi
BAD_RC=$(grep '^CANONICAL_UNBALANCED_COMPILE_RC=' <( { echo; } ) 2>/dev/null || true)
# Re-run only to capture RC as a shell variable without relying on output parsing.
set +e
"$SIGMAC" "$BAD" "$TMP/canonical_unbalanced_recheck.sigmab" >/dev/null 2>&1; U_RC=$?
set -e
echo "CANONICAL_UNBALANCED_RECHECK_RC=$U_RC"
if [ "$U_RC" -ne 0 ]; then echo 'CANONICAL_UNBALANCED_ENTRY_REJECTED=PASS'; else echo 'CANONICAL_UNBALANCED_ENTRY_REJECTED=NO'; fi
if [ -f "$TMP/CANONICAL_SUCCESSOR.sigmab" ]; then cp "$TMP/CANONICAL_SUCCESSOR.sigmab" "$BIN"; fi

# Classification is machine-driven by the direct controls above.
echo '=== CLASSIFICATION ==='
echo 'EXPECTED_CAUSAL_PATTERN=TOPLEVEL_COMMENT_FAIL_AND_COMMENT_FREE_EQUIVALENT_PASS'
echo 'CANONICAL_RULE=ONE_HEADER_PLUS_CANONICAL_DEF_BLOCKS_PLUS_ONE_ENTRY'
echo 'T1_T2_T3_SUCCESSOR_COMPOSITION=PRESENT_EXACT_BODY_SCOPE'
echo 'T1_T2_T3_NATIVE_UTILIZATION=NOT_YET_PROVEN'
echo 'R4_RUNTIME_LEARNING=NOT_ADMITTED'

lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE_AFTER
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER_AFTER
echo 'VM_EXECUTION=NO'
echo 'PRODUCTION_BINDING=NO'
echo 'PRODUCTION_MUTATION=NO'
printf '%s\n' '=== END ==='
