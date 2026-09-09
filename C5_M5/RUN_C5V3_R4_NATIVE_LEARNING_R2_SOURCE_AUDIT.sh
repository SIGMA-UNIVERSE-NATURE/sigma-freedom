#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
OUTROOT="$ROOT/.sigma_c5v3_sync/C5V3_R4_NATIVE_LEARNING_R2"
MOD="$OUTROOT/modules"
mkdir -p "$MOD"

STATE="$MOD/C5_NATIVE_LEARNING_STATE_R2.sigma.inc"
TRANS="$MOD/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc"
ADAPTER="$MOD/C5_GATEA_R4_LEARNING_ADAPTER_R2.sigma.inc"
COMBINED="$OUTROOT/C5_R4_NATIVE_LEARNING_R2_COMBINED.sigma.inc"

STATE_COMMIT="ca6d9504f5e75c4d5ccf48ab7c574614a8b019be"
TRANS_COMMIT="3debd57e8f0ac3dce7bba540cb912c0ffbadef29"
ADAPTER_COMMIT="59e656106cd8a5c497ecda2780efa0958a252afa"
BASE="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom"
STATE_URL="$BASE/$STATE_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R2.sigma.inc"
TRANS_URL="$BASE/$TRANS_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc"
ADAPTER_URL="$BASE/$ADAPTER_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_GATEA_R4_LEARNING_ADAPTER_R2.sigma.inc"

EXPECTED_STATE="83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33"
EXPECTED_TRANS="3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9"
EXPECTED_ADAPTER="43e22c9b9140dfb0b1882d34d85ffd1e460854f20bd61420f93098052cd0aa89"
EXPECTED_COMBINED="84d064435fdba01ccd6c700f5efd266b39e297f51fedc7cfddbf9c05489fe209"

sha() { sha256sum "$1" | awk '{print $1}'; }

echo "=== C5V3 R4 NATIVE LEARNING R2 SOURCE AUDIT ==="
echo "MODE=EXACT_SCHEMA_NATIVE_CHOICE_STATIC_GOVERNANCE"
echo "VM_EXECUTION=NO"
echo "CORE_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"

curl -fsSL "$STATE_URL" -o "$STATE"
curl -fsSL "$TRANS_URL" -o "$TRANS"
curl -fsSL "$ADAPTER_URL" -o "$ADAPTER"

for spec in \
  "STATE|$STATE|$EXPECTED_STATE" \
  "TRANSITIONS|$TRANS|$EXPECTED_TRANS" \
  "ADAPTER|$ADAPTER|$EXPECTED_ADAPTER"
do
  IFS='|' read -r label path expected <<EOF2
$spec
EOF2
  actual="$(sha "$path")"
  echo "${label}_SHA256=$actual"
  [ "$actual" = "$expected" ] || { echo "HOLD=${label}_IDENTITY_MISMATCH"; exit 1; }
  echo "${label}_IDENTITY=PASS"
done

cat "$STATE" "$TRANS" "$ADAPTER" > "$COMBINED"
ACTUAL_COMBINED="$(sha "$COMBINED")"
echo "R4_R2_COMBINED_SHA256=$ACTUAL_COMBINED"
[ "$ACTUAL_COMBINED" = "$EXPECTED_COMBINED" ] || { echo "HOLD=COMBINED_IDENTITY_MISMATCH"; exit 1; }

python - "$STATE" "$TRANS" "$ADAPTER" "$COMBINED" <<'PY'
from pathlib import Path
import re,sys
state,trans,adapter,combined=map(Path,sys.argv[1:])
S=state.read_text(); T=trans.read_text(); A=adapter.read_text(); C=combined.read_text()

def names(s): return re.findall(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',s,re.M)
def arities(s):
    out=[]
    for m in re.finditer(r'^DEF\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)',s,re.M):
        args=[x.strip() for x in m.group(2).split(',') if x.strip()]
        out.append((m.group(1),len(args)))
    return out

print('STATE_DEF_COUNT='+str(len(names(S))))
print('TRANSITIONS_DEF_COUNT='+str(len(names(T))))
print('ADAPTER_DEF_COUNT='+str(len(names(A))))
print('R4_R2_COMBINED_DEF_COUNT='+str(len(names(C))))
if len(names(S))!=28: raise SystemExit('HOLD=STATE_DEF_COUNT')
if len(names(T))!=12: raise SystemExit('HOLD=TRANSITIONS_DEF_COUNT')
if len(names(A))!=12: raise SystemExit('HOLD=ADAPTER_DEF_COUNT')
if len(names(C))!=52: raise SystemExit('HOLD=COMBINED_DEF_COUNT')
if len(set(names(C)))!=len(names(C)): raise SystemExit('HOLD=DUPLICATE_DEF_NAME')

for token,label in [
    ('LEFT=','LEFT_EQ'),('RIGHT=','RIGHT_EQ'),
    ('legacy_analyze_segment','LEGACY_ANALYZE_SEGMENT'),
    ('legacy_merge_evidence','LEGACY_MERGE_EVIDENCE'),
    ('"write_text"','DIRECT_WRITE_TEXT'),('"read_text"','DIRECT_READ_TEXT'),
    ('c5l_capability_registry_select','R1_AUTO_CAPABILITY_SELECT')]:
    n=C.count(token); print(f'{label}_COUNT={n}')
    if n: raise SystemExit('HOLD=FORBIDDEN_SURFACE:'+label)

required=['c5l2_capability_registry_has','c5l2_field','c5l2_record_part_count','c5l2_memory_pack','c5a2_relation_gap_signal']
for token in required:
    n=C.count('DEF '+token+'('); print('REQUIRED_'+token+'_COUNT='+str(n))
    if n!=1: raise SystemExit('HOLD=REQUIRED_DEF:'+token)

ars=arities(C)
print('MAX_DEF_ARITY='+str(max(a for _,a in ars)))
if any(a>6 for _,a in ars): raise SystemExit('HOLD=DEF_ARITY_GT6')
mult=[]
for i,line in enumerate(C.splitlines(),1):
    if re.match(r'^DEF\s+[A-Za-z0-9_]+\s*\(',line) and '{' not in line:
        mult.append((i,line))
print('MULTILINE_DEF_SIGNATURE_COUNT='+str(len(mult)))
if mult: raise SystemExit('HOLD=MULTILINE_DEF_SIGNATURE')

if 'H("str_split", FIELD, "=", NULL)' not in S: raise SystemExit('HOLD=EXACT_FIELD_SPLIT_MISSING')
if 'IF (KN != 2)' not in S: raise SystemExit('HOLD=EXACT_FIELD_PART_COUNT_MISSING')
if 'IF (K != key)' not in S: raise SystemExit('HOLD=EXACT_FIELD_KEY_MATCH_MISSING')
if 'H("str_replace", value, "=", "")' not in S: raise SystemExit('HOLD=SAFE_ATOM_EQUALS_REJECTION_MISSING')
if 'c5l2_capability_registry_has(registry, capability_id, need_family)' not in S: raise SystemExit('HOLD=NATIVE_CAPABILITY_VALIDATION_MISSING')
print('EXACT_SCHEMA_FIELD_PARSE=PASS')
print('SAFE_ATOM_EQUALS_REJECTION=PASS')
print('NATIVE_SUPPLIED_CAPABILITY_ID_REQUIRED=PASS')
print('R4_R1_RUNTIME_ADMISSION=NO_SUPERSEDED_BEFORE_RUNTIME')
print('R4_R2_STATIC_GOVERNANCE=PASS')
PY

echo "R4_R2_COMBINED_PATH=$COMBINED"
echo "R4_R2_COMBINED_SHA256=$(sha "$COMBINED")"
echo "R4_R2_SOURCE_AUDIT=PASS"
echo "RUNTIME_ADMISSION=NO"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"
echo "=== END ==="
