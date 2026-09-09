#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
OUTROOT="$ROOT/.sigma_c5v3_sync/C5V3_R4_DURABLE_TRANSACTION_SUBSTRATE_R1"
MOD="$OUTROOT/modules"
mkdir -p "$MOD"

BASE="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom"

STATE="$MOD/C5_NATIVE_LEARNING_STATE_R2.sigma.inc"
TRANS="$MOD/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc"
ADAPTER="$MOD/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc"
DURABLE="$MOD/C5_R4_DURABLE_LEARNING_MODEL_R1.sigma.inc"
KERNEL="$MOD/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R3.sigma.inc"
P0="$MOD/C5_R4_P0_TRANSACTION_TRUST_R1.sigma.inc"
COMBINED="$OUTROOT/C5_R4_DURABLE_TRANSACTION_SUBSTRATE_R1_COMBINED.sigma.inc"

STATE_COMMIT="ca6d9504f5e75c4d5ccf48ab7c574614a8b019be"
TRANS_COMMIT="3debd57e8f0ac3dce7bba540cb912c0ffbadef29"
ADAPTER_COMMIT="02bb0c6d60f2568583211b16baa8fbbd3de0e77f"
DURABLE_COMMIT="b334a1ff23d068551d46b1f114b8ad45afbf46e3"
KERNEL_COMMIT="89019543f98b39cd34ea95535a14c77f050360ea"
P0_COMMIT="ba42087f602baf274c6ed5c90ae3f7a92d647eba"

curl -fsSL "$BASE/$STATE_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R2.sigma.inc" -o "$STATE"
curl -fsSL "$BASE/$TRANS_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc" -o "$TRANS"
curl -fsSL "$BASE/$ADAPTER_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc" -o "$ADAPTER"
curl -fsSL "$BASE/$DURABLE_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_R4_DURABLE_LEARNING_MODEL_R1.sigma.inc" -o "$DURABLE"
curl -fsSL "$BASE/$KERNEL_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R3.sigma.inc" -o "$KERNEL"
curl -fsSL "$BASE/$P0_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_R4_P0_TRANSACTION_TRUST_R1.sigma.inc" -o "$P0"

sha() { sha256sum "$1" | awk '{print $1}'; }

EXPECTED_STATE="83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33"
EXPECTED_TRANS="3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9"
EXPECTED_ADAPTER="223aeb84c4d4fcc8e1cbdbf62943a38382efa8250de72eb4df4ba3df79e5b02b"
EXPECTED_DURABLE="514c52fcc2e8e1fc5ea64e78b664b7651c8c0ce20c2d463b5fe505c95f9becd2"
EXPECTED_KERNEL="db2a0454fc429d58b9617a40a6e4283f632b35df2c6190e6389820402e1035b1"
EXPECTED_P0="cad40e8ded7138d7e56c8cbb219eba5e43d10d78fc18e7f335073f048f1bad82"

echo "=== C5V3 R4 DURABLE + TRANSACTION SUBSTRATE SOURCE AUDIT R1 ==="
echo "MODE=STATIC_DURABILITY_TRUST_AND_SOURCE_IDENTITY"
echo "VM_EXECUTION=NO"
echo "CORE_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"

for spec in \
  "STATE|$STATE|$EXPECTED_STATE" \
  "TRANSITIONS|$TRANS|$EXPECTED_TRANS" \
  "ADAPTER_R3|$ADAPTER|$EXPECTED_ADAPTER" \
  "DURABLE_R1|$DURABLE|$EXPECTED_DURABLE" \
  "KERNEL_R3|$KERNEL|$EXPECTED_KERNEL" \
  "P0_R4|$P0|$EXPECTED_P0"
do
  IFS='|' read -r label path expected <<< "$spec"
  actual="$(sha "$path")"
  echo "${label}_SHA256=$actual"
  [ "$actual" = "$expected" ] || { echo "HOLD=${label}_IDENTITY_MISMATCH"; exit 1; }
  echo "${label}_IDENTITY=PASS"
done

python - "$STATE" "$TRANS" "$ADAPTER" "$DURABLE" "$KERNEL" "$P0" "$COMBINED" <<'PY'
from pathlib import Path
import hashlib,re,sys
paths=sys.argv[1:7]; out=Path(sys.argv[7])
parts=[Path(p).read_text() for p in paths]
combined='\n\n'.join(x.rstrip() for x in parts)+'\n'
out.write_text(combined)
labels=['STATE','TRANSITIONS','ADAPTER_R3','DURABLE_R1','KERNEL_R3','P0_R4']
expected=[28,12,16,10,12,14]

def defs(t): return re.findall(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',t,re.M)
def arities(t):
    r=[]
    for m in re.finditer(r'^DEF\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)',t,re.M):
        r.append((m.group(1),len([x for x in m.group(2).split(',') if x.strip()])))
    return r

counts=[len(defs(x)) for x in parts]
for l,c in zip(labels,counts): print(f'{l}_DEF_COUNT={c}')
if counts!=expected: raise SystemExit('HOLD=DEF_COUNTS:'+repr(counts))
all_defs=defs(combined)
print('R4_DURABLE_TRANSACTION_DEF_COUNT='+str(len(all_defs)))
if len(all_defs)!=92: raise SystemExit('HOLD=COMBINED_DEF_COUNT')
if len(set(all_defs))!=92: raise SystemExit('HOLD=DUPLICATE_DEF_NAME')
mx=max(a for _,a in arities(combined)); print('MAX_DEF_ARITY='+str(mx))
if mx>6: raise SystemExit('HOLD=DEF_ARITY_GT6')
mult=[l for l in combined.splitlines() if re.match(r'^DEF\s+[A-Za-z0-9_]+\s*\(',l) and '{' not in l]
print('MULTILINE_DEF_SIGNATURE_COUNT='+str(len(mult)))
if mult: raise SystemExit('HOLD=MULTILINE_DEF_SIGNATURE')

pure='\n'.join(parts[:5])
for tok,label in [('LEFT=','LEFT_EQ'),('RIGHT=','RIGHT_EQ'),('legacy_analyze_segment','LEGACY_ANALYZE_SEGMENT'),('legacy_merge_evidence','LEGACY_MERGE_EVIDENCE'),('"write_text"','PURE_DIRECT_WRITE_TEXT'),('"read_text"','PURE_DIRECT_READ_TEXT'),('c5l_capability_registry_select','AUTO_CAPABILITY_SELECT')]:
    c=pure.count(tok); print(f'{label}_COUNT={c}')
    if c: raise SystemExit('HOLD=FORBIDDEN_PURE_SURFACE:'+label)

p0=parts[5]
print('P0_WRITE_TEXT_LITERAL_COUNT='+str(p0.count('"write_text"')))
print('P0_READ_TEXT_LITERAL_COUNT='+str(p0.count('"read_text"')))
if p0.count('"write_text"')!=1 or p0.count('"read_text"')!=1: raise SystemExit('HOLD=P0_IO_SURFACE_NOT_EXACT')

durable=parts[3]; kernel=parts[4]
required_durable=[
 'TYPE=DURABLE_CLAIM || CLAIM_ID=',
 'CONTENT=" + content + " || CLASS=',
 'EVALUATIONS_BEGIN\\n',
 'DEF c5d1_memory_recall_evaluations(',
 'DEF c5d1_memory_evidence_posture('
]
for x in required_durable:
    c=durable.count(x); print('DURABLE_REQUIRED_'+hashlib.sha256(x.encode()).hexdigest()[:12]+'_COUNT='+str(c))
    if c<1: raise SystemExit('HOLD=DURABLE_REQUIRED_SURFACE:'+x)
required_kernel=[
 'IF (ACONTENT != candidate_a) { RETURN 0; }',
 'IF (BCONTENT != candidate_b) { RETURN 0; }',
 'RETURN c5d1_memory_pack(work_id, claim_bank, gap_bank, evidence_ref_bank, evaluation_bank, revision);',
 'DEF c5c4_restart_recall_evaluations(',
 'DEF c5c4_restart_evidence_posture('
]
for x in required_kernel:
    c=kernel.count(x); print('KERNEL_REQUIRED_'+hashlib.sha256(x.encode()).hexdigest()[:12]+'_COUNT='+str(c))
    if c!=1: raise SystemExit('HOLD=KERNEL_REQUIRED_SURFACE:'+x)

print('DURABLE_CLAIM_CONTENT_RETENTION=PASS')
print('DURABLE_EVALUATION_HISTORY_RETENTION=PASS')
print('RESTART_EVIDENCE_POSTURE_REUSE_SURFACE=PASS')
print('P0_TRANSACTION_STATE_SCHEMA=PASS_STATIC')
print('NATIVE_CAPABILITY_AUTO_SELECTION=ABSENT')
print('R4_DURABLE_TRANSACTION_COMBINED_SHA256='+hashlib.sha256(combined.encode()).hexdigest())
print('R4_DURABLE_TRANSACTION_STATIC_GOVERNANCE=PASS')
PY

echo "R4_DURABLE_TRANSACTION_COMBINED_PATH=$COMBINED"
echo "R4_DURABLE_TRANSACTION_COMBINED_SHA256=$(sha "$COMBINED")"
echo "R4_DURABLE_TRANSACTION_SUBSTRATE_SOURCE_AUDIT=PASS"
echo "RUNTIME_ADMISSION=NO"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"
echo "=== END ==="
