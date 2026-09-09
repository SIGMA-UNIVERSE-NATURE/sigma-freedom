#!/data/data/com.termux/files/usr/bin/bash
set -eu

# C5V3 Core Rewrite R3 — same C5 identity, latest admitted Gate-A cognition,
# exact admitted T1/T2/T3 tool DEF substrate. Build + compile only.
# No VM/core execution. No production write/binding. Exact known files only.

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
BUNDLE="${2:-}"
SYNC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3"
SRC_DIR="$SYNC/src"
BIN_DIR="$SYNC/bin"
EVID_DIR="$SYNC/evidence"
OUT_SRC="$SRC_DIR/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
OUT_BIN="$BIN_DIR/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"

R6="$ROOT/.sigma_c5v3_sync/OFFLINE_PRODUCTION_LINEAGE_LATENT_GRAFT_R6_20260909T184734/candidate/core.sigma"
SIGMAC="$ROOT/native/sigmac"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"

EXPECTED_BUNDLE_SHA256="ff3fced4c16bf3866e30853e01f5bb634a87ac25943ba612a3cdf1cdf2708494"
EXPECTED_M5_CORE_SHA256="bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1"
EXPECTED_R6_SHA256="dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac"
EXPECTED_R3_SOURCE_SHA256="7a9dc693f8cc3481bd5e550f7fbbe8c0ad356f9d2b0be5011f4ace39134bf5e8"
EXPECTED_SIGMAC_SHA256="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_LIVE_CORE_SHA256="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER_SHA256="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"
EXPECTED_HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'

hash1() { sha256sum "$1" | awk '{print $1}'; }
hold() {
  printf 'R3_BUILD_COMPILE=HOLD_%s\n' "$1"
  printf 'VM_EXECUTION=NO\nLIVE_CORE_WRITE=NO\nPRODUCTION_BINDING=NO\nPRODUCTION_MUTATION=NO\n'
  exit 0
}
require_hash() {
  label="$1"; path="$2"; expected="$3"
  [ -f "$path" ] || hold "${label}_MISSING"
  actual="$(hash1 "$path")"
  printf '%s_PATH=%s\n%s_SHA256=%s\n' "$label" "$path" "$label" "$actual"
  [ "$actual" = "$expected" ] || hold "${label}_IDENTITY_MISMATCH"
  printf '%s_IDENTITY=PASS\n' "$label"
}

if [ -z "$BUNDLE" ]; then
  for p in \
    "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip" \
    "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip" \
    "$HOME/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip" \
    "$HOME/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip"
  do
    if [ -f "$p" ]; then BUNDLE="$p"; break; fi
  done
fi

printf '%s\n' '=== C5V3 CORE REWRITE R3 M5 EPISTEMIC + T1/T2/T3 BUILD COMPILE R1 ==='
printf 'ROOT=%s\n' "$ROOT"
printf 'MODE=SAME_IDENTITY_COGNITIVE_PURGE_BUILD_AND_COMPILE_ONLY\n'
printf 'EXACT_KNOWN_FILES_ONLY=YES\nDIRECTORY_SCAN=NO\nVM_EXECUTION=NO\nCORE_EXECUTION=NO\nLIVE_CORE_WRITE=NO\nLIVE_RUNNER_WRITE=NO\nPRODUCTION_BINDING=NO\nPRODUCTION_MUTATION=NO\n'

[ -n "$BUNDLE" ] || hold M5_BUNDLE_PATH_REQUIRED
require_hash M5_GATE_A_BUNDLE "$BUNDLE" "$EXPECTED_BUNDLE_SHA256"
require_hash R6_SOURCE "$R6" "$EXPECTED_R6_SHA256"
require_hash LOCKED_SIGMAC "$SIGMAC" "$EXPECTED_SIGMAC_SHA256"
require_hash LIVE_CORE "$LIVE_CORE" "$EXPECTED_LIVE_CORE_SHA256"
require_hash LIVE_RUNNER "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER_SHA256"

mkdir -p "$SRC_DIR" "$BIN_DIR" "$EVID_DIR"
TMP_M5="$SRC_DIR/.m5_parent.partial.$$"
TMP_SRC="$SRC_DIR/.r3_source.partial.$$"
TMP_BIN="$BIN_DIR/.r3_bytecode.partial.$$"
rm -f "$TMP_M5" "$TMP_SRC" "$TMP_BIN"

python - "$BUNDLE" "$R6" "$TMP_M5" "$TMP_SRC" <<'PY'
import sys, zipfile, hashlib, re
from pathlib import Path

bundle, r6_path, m5_out, r3_out = map(Path, sys.argv[1:])
EXPECTED_M5='bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1'
EXPECTED_R3='7a9dc693f8cc3481bd5e550f7fbbe8c0ad356f9d2b0be5011f4ace39134bf5e8'
HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n'

def h(b): return hashlib.sha256(b).hexdigest()
def parse_blocks(s):
    lines=s.splitlines(True); out=[]; i=0
    while i < len(lines):
        m=re.match(r'^DEF\s+([A-Za-z0-9_]+)\s*\(', lines[i])
        if not m: i += 1; continue
        start=i; depth=0; seen=False; j=i
        while j < len(lines):
            for ch in lines[j]:
                if ch == '{': depth += 1; seen=True
                elif ch == '}': depth -= 1
            if seen and depth == 0: break
            j += 1
        out.append((m.group(1), ''.join(lines[start:j+1])))
        i=j+1
    return out

with zipfile.ZipFile(bundle) as z:
    candidates=[]
    for n in z.namelist():
        if n.endswith('/core.sigma'):
            b=z.read(n)
            if h(b)==EXPECTED_M5:
                candidates.append((n,b))
    if len(candidates)!=2:
        raise SystemExit(f'HOLD_M5_CORE_MATCH_COUNT={len(candidates)}')
    # Admission and blind copies are byte-identical. Use lexical first deterministically.
    candidates.sort(key=lambda x:x[0])
    m5_bytes=candidates[0][1]

m5_out.write_bytes(m5_bytes)
m5=m5_bytes.decode('utf-8')
r6=r6_path.read_text()

m5defs=parse_blocks(m5)
r6defs=parse_blocks(r6)
if len(m5defs)!=78: raise SystemExit(f'HOLD_M5_DEF_COUNT={len(m5defs)}')
if len(r6defs)!=156: raise SystemExit(f'HOLD_R6_DEF_COUNT={len(r6defs)}')

tools=r6defs[63:145]
if len(tools)!=82: raise SystemExit(f'HOLD_TOOL_DEF_COUNT={len(tools)}')
if tools[0][0] != 'WA_H' or tools[-1][0] != 'T2_SHORTEST_PATH_BOUNDED':
    raise SystemExit('HOLD_TOOL_BOUNDARY_IDENTITY')

m5_names={n for n,_ in m5defs}
coll=[n for n,_ in tools if n in m5_names]
if coll: raise SystemExit('HOLD_DEF_COLLISION=' + ','.join(coll))

lines=m5.splitlines(True)
entry_idx=next((i for i,l in enumerate(lines) if l.startswith('⟡(')), None)
if entry_idx is None: raise SystemExit('HOLD_M5_UNIVERSE_MISSING')
lines[0]=HEADER
marker=(
    '\n# C5V3 SAME-IDENTITY CORE REWRITE R3\n'
    '# Cognitive parent: exact admitted+independent-blind-PASS M5 scoped provisional epistemic truth.\n'
    '# Tool substrate: exact admitted T1/T2/T3 DEF bodies from frozen R6.\n'
    '# Legacy adjacent-token LEFT/RIGHT support learner is not part of this core.\n'
    '# T4-T11 enter only after exact offline admission handoff.\n\n'
)
tool_text=''.join(body for _,body in tools)
r3=''.join(lines[:entry_idx]) + marker + tool_text + ''.join(lines[entry_idx:])
r3_bytes=r3.encode('utf-8')
r3_out.write_bytes(r3_bytes)

if h(r3_bytes)!=EXPECTED_R3: raise SystemExit('HOLD_R3_DETERMINISTIC_SOURCE_HASH_MISMATCH=' + h(r3_bytes))

r3defs=parse_blocks(r3)
if len(r3defs)!=160: raise SystemExit(f'HOLD_R3_DEF_COUNT={len(r3defs)}')
if sum(1 for l in r3.splitlines() if l.startswith('⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1)')) != 1:
    raise SystemExit('HOLD_ENTRY_ID_COUNT')
if r3.splitlines()[0] != HEADER.rstrip('\n'):
    raise SystemExit('HOLD_HEADER_IDENTITY')

for forbidden in ('legacy_analyze_segment','legacy_merge_evidence','LEFT=','RIGHT=','LOCAL_U='):
    if forbidden in r3: raise SystemExit('HOLD_LEGACY_COGNITION_REMAINS=' + forbidden)

M5=dict(m5defs); R6=dict(r6defs); R3=dict(r3defs)
for n,b in M5.items():
    if h(R3[n].encode()) != h(b.encode()):
        raise SystemExit('HOLD_M5_DEF_BODY_CHANGED=' + n)
for n,_ in tools:
    if h(R3[n].encode()) != h(R6[n].encode()):
        raise SystemExit('HOLD_TOOL_DEF_BODY_CHANGED=' + n)

print('M5_PARENT_SOURCE_SHA256=' + h(m5_bytes))
print('M5_PARENT_DEF_COUNT=78')
print('R6_DEF_COUNT=156')
print('R3_M5_DEF_BODY_HASHES_PRESERVED=PASS')
print('R3_T1_T2_T3_TOOL_DEF_BODY_HASHES_PRESERVED=PASS')
print('R3_TOOL_DEF_COUNT=82')
print('R3_DEF_COUNT=160')
print('R3_LEGACY_LEFT_RIGHT_COGNITION=ABSENT')
print('R3_HEADER_IDENTITY=PASS')
print('R3_ENTRY_IDENTITY=PASS')
print('R3_SOURCE_SHA256=' + h(r3_bytes))
print('R3_SOURCE_LINES=' + str(len(r3.splitlines())))
PY
PY_RC=$?
[ "$PY_RC" -eq 0 ] || hold PYTHON_R3_CONSTRUCTION_FAILED

require_hash M5_PARENT_EXTRACTED "$TMP_M5" "$EXPECTED_M5_CORE_SHA256"
require_hash R3_SOURCE_CONSTRUCTED "$TMP_SRC" "$EXPECTED_R3_SOURCE_SHA256"

if [ -f "$OUT_SRC" ]; then
  [ "$(hash1 "$OUT_SRC")" = "$EXPECTED_R3_SOURCE_SHA256" ] || hold EXISTING_R3_SOURCE_MISMATCH
  rm -f "$TMP_SRC"
  printf 'R3_SOURCE_ALREADY_EXISTS=YES\n'
else
  mv "$TMP_SRC" "$OUT_SRC"
  chmod 0400 "$OUT_SRC"
  printf 'R3_SOURCE_ALREADY_EXISTS=NO\n'
fi
rm -f "$TMP_M5"

printf 'R3_SOURCE_PATH=%s\nR3_SOURCE_SHA256=%s\n' "$OUT_SRC" "$(hash1 "$OUT_SRC")"
printf 'R3_SOURCE_LINES=%s\nR3_DEF_COUNT=%s\n' "$(wc -l < "$OUT_SRC")" "$(grep -Ec '^DEF[[:space:]]+' "$OUT_SRC")"
printf 'SUCCESSOR_HEADER=%s\n' "$(sed -n '1p' "$OUT_SRC")"
[ "$(sed -n '1p' "$OUT_SRC")" = "$EXPECTED_HEADER" ] || hold R3_HEADER_MISMATCH

printf '%s\n' '=== COMPILE / BYTECODE FREEZE ==='
"$SIGMAC" "$OUT_SRC" "$TMP_BIN"
RC=$?
printf 'SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || hold SIGMAC_COMPILE_FAILED
[ -s "$TMP_BIN" ] || hold BYTECODE_EMPTY
NEW_BIN_SHA="$(hash1 "$TMP_BIN")"
printf 'COMPILED_BYTECODE_SHA256=%s\n' "$NEW_BIN_SHA"

if [ -f "$OUT_BIN" ]; then
  EXISTING_BIN_SHA="$(hash1 "$OUT_BIN")"
  [ "$EXISTING_BIN_SHA" = "$NEW_BIN_SHA" ] || hold EXISTING_R3_BYTECODE_DIFFERS
  rm -f "$TMP_BIN"
  printf 'R3_BYTECODE_ALREADY_EXISTS=YES\n'
else
  mv "$TMP_BIN" "$OUT_BIN"
  chmod 0400 "$OUT_BIN"
  printf 'R3_BYTECODE_ALREADY_EXISTS=NO\n'
fi
printf 'R3_BYTECODE_PATH=%s\nR3_BYTECODE_SHA256=%s\n' "$OUT_BIN" "$(hash1 "$OUT_BIN")"

printf '%s\n' '=== LIVE NON-MUTATION RECHECK ==='
require_hash LIVE_CORE_AFTER "$LIVE_CORE" "$EXPECTED_LIVE_CORE_SHA256"
require_hash LIVE_RUNNER_AFTER "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER_SHA256"

cat > "$EVID_DIR/R3_BUILD_COMPILE_MANIFEST.txt" <<EOF
ONE_SIGMA=YES
SYSTEM=C5V3
R3_CLASS=SAME_IDENTITY_C5_CORE_REWRITE
COGNITIVE_PARENT_SHA256=$EXPECTED_M5_CORE_SHA256
COGNITIVE_PARENT_SCOPE=SCOPED_PROVISIONAL_EPISTEMIC_TRUTH_ADMISSION_AND_BLIND_PASS
R6_SOURCE_SHA256=$EXPECTED_R6_SHA256
R3_SOURCE_SHA256=$EXPECTED_R3_SOURCE_SHA256
R3_BYTECODE_SHA256=$(hash1 "$OUT_BIN")
R3_DEF_COUNT=160
M5_COGNITIVE_DEF_COUNT=78
T1_T2_T3_TOOL_DEF_COUNT=82
LEGACY_ADJACENT_TOKEN_COGNITION=ABSENT
HEADER=$EXPECTED_HEADER
ENTRY_ID=Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1
T4_T11_INTEGRATION=PENDING_OFFLINE_EXACT_HANDOFF
VM_EXECUTION=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
EOF

printf '%s\n' '=== RESULT ==='
printf 'R3_BUILD=PASS\nR3_COMPILE=PASS\nR3_BYTECODE_FREEZE=PASS\n'
printf 'R3_LATEST_ADMITTED_GATE_A_COGNITION_IN_SAME_C5_CORE=YES\n'
printf 'R3_T1_T2_T3_EXACT_TOOL_SUBSTRATE_IN_SAME_C5_CORE=YES\n'
printf 'R3_LEGACY_ADJACENT_TOKEN_COGNITION=ABSENT\n'
printf 'CORE_IDENTITY_CONTINUITY=PASS\n'
printf 'T4_T11=PENDING_OFFLINE_HANDOFF\n'
printf 'VM_EXECUTION=NO\nLIVE_CORE_UNCHANGED=YES\nLIVE_RUNNER_UNCHANGED=YES\nPRODUCTION_BINDING=NO\nPRODUCTION_MUTATION=NO\n'
printf '%s\n' '=== END ==='
