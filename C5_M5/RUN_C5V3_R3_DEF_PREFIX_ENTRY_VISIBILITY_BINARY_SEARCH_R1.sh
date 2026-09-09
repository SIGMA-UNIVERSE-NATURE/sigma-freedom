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

TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R3_DEF_PREFIX_ENTRY_R1_$$"
mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT

sha() { sha256sum "$1" | awk '{print $1}'; }
lock() {
  local p e n a
  p="$1"; e="$2"; n="$3"
  [ -f "$p" ] || { echo "HOLD=MISSING_EXACT_PATH"; echo "PATH=$p"; exit 1; }
  a="$(sha "$p")"
  echo "${n}_PATH=$p"
  echo "${n}_SHA256=$a"
  echo "${n}_BYTES=$(wc -c < "$p")"
  [ "$a" = "$e" ] || { echo "${n}_IDENTITY=FAIL"; exit 1; }
  echo "${n}_IDENTITY=PASS"
}

make_variant() {
  local mode n out
  mode="$1"; n="$2"; out="$3"
  python - "$R3_SRC" "$mode" "$n" "$out" <<'PY'
from pathlib import Path
import re, sys
src, mode, n_s, out = sys.argv[1:]
n = int(n_s)
s = Path(src).read_text()
lines = s.splitlines(keepends=True)
if not lines or not lines[0].startswith('#SIGMAUNIVERSE_LANGUAGE['):
    raise SystemExit('HOLD=HEADER_NOT_FIRST_LINE')
header = lines[0].rstrip('\n')

def scan_block(start_offset):
    brace = s.find('{', start_offset)
    if brace < 0:
        raise SystemExit('HOLD=OPEN_BRACE_MISSING')
    depth=0; in_str=False; esc=False
    i=brace
    while i < len(s):
        ch=s[i]
        if in_str:
            if esc: esc=False
            elif ch=='\\': esc=True
            elif ch=='"': in_str=False
        else:
            if ch=='"': in_str=True
            elif ch=='{': depth += 1
            elif ch=='}':
                depth -= 1
                if depth==0:
                    return s[start_offset:i+1]
        i += 1
    raise SystemExit('HOLD=UNBALANCED_BLOCK')

# Locate DEF starts only at beginning of physical lines.
def_starts=[]
off=0
for line in lines:
    m=re.match(r'^DEF\s+([A-Za-z0-9_]+)\s*\(', line)
    if m:
        def_starts.append((off,m.group(1)))
    off += len(line)

defs=[]
for start,name in def_starts:
    defs.append((name,scan_block(start)))
if len(defs)!=176:
    raise SystemExit('HOLD=DEF_COUNT:'+str(len(defs)))
entry_start=s.find('⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1)')
if entry_start<0:
    raise SystemExit('HOLD=ENTRY_NOT_FOUND')
main=scan_block(entry_start)

if mode=='prefix':
    chosen=defs[:n]
elif mode=='p0':
    chosen=defs[:17]
elif mode=='cognition':
    chosen=defs[17:94]
elif mode=='tools':
    chosen=defs[94:176]
elif mode=='all':
    chosen=defs
else:
    raise SystemExit('HOLD=UNKNOWN_MODE')

if mode=='p0' and n==1:
    entry=main
else:
    entry=(
        '⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1) {\n'
        f'    ⚡ print("DEF_PREFIX_ENTRY_SENTINEL_{mode}_{n}");\n'
        '}\n'
    )
text=header+'\n\n'+'\n\n'.join(b.rstrip() for _,b in chosen)+'\n\n'+entry
Path(out).write_text(text)
print('VARIANT_MODE='+mode)
print('VARIANT_PARAM='+str(n))
print('VARIANT_DEF_COUNT='+str(len(chosen)))
print('VARIANT_FIRST_DEF='+(chosen[0][0] if chosen else 'NONE'))
print('VARIANT_LAST_DEF='+(chosen[-1][0] if chosen else 'NONE'))
print('VARIANT_BYTES='+str(len(text.encode())))
PY
}

compile_variant() {
  local label src out log rc h bytes klass
  label="$1"; src="$2"
  out="$TMP/${label}.sigmab"
  log="$TMP/${label}.log"
  rm -f "$out" "$log"
  set +e
  "$SIGMAC" "$src" "$out" >"$log" 2>&1
  rc=$?
  set -e
  echo "${label}_COMPILE_RC=$rc"
  if [ -s "$log" ]; then sed "s/^/${label}_LOG=/" "$log"; fi
  if [ ! -f "$out" ]; then
    echo "${label}_BYTECODE=ABSENT"
    echo "${label}_CLASS=ABSENT"
    return 0
  fi
  h="$(sha "$out")"
  bytes="$(wc -c < "$out")"
  if [ "$h" = "$EXPECTED_29B" ]; then klass="HEADER_ONLY_29B"; else klass="NONTRIVIAL"; fi
  echo "${label}_BYTECODE_SHA256=$h"
  echo "${label}_BYTECODE_BYTES=$bytes"
  echo "${label}_CLASS=$klass"
}

class_of() {
  local label="$1" src="$2" out="$TMP/${label}.sigmab" log="$TMP/${label}.log" rc h
  rm -f "$out" "$log"
  set +e
  "$SIGMAC" "$src" "$out" >"$log" 2>&1
  rc=$?
  set -e
  if [ "$rc" -ne 0 ] || [ ! -f "$out" ]; then echo "ERROR"; return 0; fi
  h="$(sha "$out")"
  if [ "$h" = "$EXPECTED_29B" ]; then echo "HEADER_ONLY_29B"; else echo "NONTRIVIAL"; fi
}

echo "=== C5V3 R3 DEF PREFIX ENTRY VISIBILITY BINARY SEARCH R1 ==="
echo "MODE=EXACT_R3_DEF_PREFIX_PLUS_MINIMAL_SENTINEL_ENTRY"
echo "VM_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"
echo "DIRECTORY_SCAN=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" "SIGMAC"
lock "$R3_SRC" "$EXPECTED_R3" "R3_SOURCE"
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" "LIVE_CORE_BEFORE"
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" "LIVE_RUNNER_BEFORE"

echo "=== 1. STRUCTURE LOCK ==="
python - "$R3_SRC" <<'PY'
from pathlib import Path
import re,sys
s=Path(sys.argv[1]).read_text()
names=re.findall(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',s,flags=re.M)
print('R3_DEF_COUNT='+str(len(names)))
print('P0_DEF_RANGE=1..17')
print('COGNITION_DEF_RANGE=18..94')
print('TOOLS_DEF_RANGE=95..176')
print('DEF_17='+names[16])
print('DEF_18='+names[17])
print('DEF_94='+names[93])
print('DEF_95='+names[94])
print('DEF_176='+names[175])
PY

echo "=== 2. GROUP / PREFIX CONTROLS ==="
for spec in "prefix:0" "prefix:17" "prefix:94" "prefix:176" "cognition:0" "tools:0"; do
  mode="${spec%%:*}"; n="${spec##*:}"
  label="GROUP_${mode}_${n}"
  src="$TMP/${label}.sigma"
  make_variant "$mode" "$n" "$src"
  compile_variant "$label" "$src"
done

echo "=== 3. P0 EXACT MAIN ISOLATION ==="
P0MAIN="$TMP/P0_DEFS_EXACT_P0_MAIN.sigma"
make_variant "p0" 1 "$P0MAIN"
compile_variant "P0_DEFS_EXACT_P0_MAIN" "$P0MAIN"

ALL_SENT="$TMP/GROUP_prefix_176.sigma"
ALL_CLASS="$(class_of CHECK_ALL "$ALL_SENT")"
echo "ALL_176_DEFS_PLUS_SENTINEL_CLASS=$ALL_CLASS"

if [ "$ALL_CLASS" = "HEADER_ONLY_29B" ]; then
  echo "=== 4. MONOTONIC PREFIX BINARY SEARCH ==="
  lo=0
  hi=176
  # prefix 0 is expected nontrivial from the sentinel control.
  while [ $((hi-lo)) -gt 1 ]; do
    mid=$(((lo+hi)/2))
    src="$TMP/BSEARCH_${mid}.sigma"
    make_variant "prefix" "$mid" "$src" >/dev/null
    cls="$(class_of "BSEARCH_${mid}" "$src")"
    echo "BSEARCH_PREFIX_${mid}_CLASS=$cls"
    if [ "$cls" = "NONTRIVIAL" ]; then
      lo="$mid"
    elif [ "$cls" = "HEADER_ONLY_29B" ]; then
      hi="$mid"
    else
      echo "BSEARCH_PREFIX_${mid}_CLASSIFICATION=ERROR"
      break
    fi
  done
  echo "LAST_NONTRIVIAL_PREFIX_COUNT=$lo"
  echo "FIRST_HEADER_ONLY_PREFIX_COUNT=$hi"
  python - "$R3_SRC" "$hi" <<'PY'
from pathlib import Path
import re,sys
s=Path(sys.argv[1]).read_text(); idx=int(sys.argv[2])
names=re.findall(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',s,flags=re.M)
if 1 <= idx <= len(names):
    print('FIRST_SUSPECT_DEF_INDEX='+str(idx))
    print('FIRST_SUSPECT_DEF_NAME='+names[idx-1])
else:
    print('FIRST_SUSPECT_DEF_INDEX=UNRESOLVED')
PY
  echo "RESULT=DEF_PREFIX_CAUSES_ENTRY_INVISIBILITY_OR_ZERO_CODE"
elif [ "$ALL_CLASS" = "NONTRIVIAL" ]; then
  echo "DEF_PREFIX_176_ENTRY_VISIBILITY=PASS"
  echo "RESULT=ALL_DEFS_PARSE_WITH_MINIMAL_ENTRY_ROOT_CAUSE_MOVES_TO_P0_MAIN"
else
  echo "RESULT=HOLD_ALL_DEF_SENTINEL_CONTROL_ERROR"
fi

echo "=== 5. NON-MUTATION RECHECK ==="
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" "LIVE_CORE_AFTER"
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" "LIVE_RUNNER_AFTER"
echo "PRODUCTION_MUTATION=NO"
echo "VM_EXECUTION=NO"
echo "=== END ==="
