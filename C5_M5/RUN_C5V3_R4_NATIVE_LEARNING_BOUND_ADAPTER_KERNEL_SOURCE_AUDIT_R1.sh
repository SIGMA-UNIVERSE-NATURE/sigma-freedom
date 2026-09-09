#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
OUTROOT="$ROOT/.sigma_c5v3_sync/C5V3_R4_NATIVE_LEARNING_BOUND_R1"
MOD="$OUTROOT/modules"
mkdir -p "$MOD"

STATE="$MOD/C5_NATIVE_LEARNING_STATE_R2.sigma.inc"
TRANS="$MOD/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc"
ADAPTER="$MOD/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc"
KERNEL="$MOD/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R2.sigma.inc"
COMBINED="$OUTROOT/C5_R4_NATIVE_LEARNING_BOUND_R1_COMBINED.sigma.inc"

STATE_COMMIT="ca6d9504f5e75c4d5ccf48ab7c574614a8b019be"
TRANS_COMMIT="3debd57e8f0ac3dce7bba540cb912c0ffbadef29"
ADAPTER_COMMIT="02bb0c6d60f2568583211b16baa8fbbd3de0e77f"
KERNEL_COMMIT="b3fc9cfa25a4cd09bca98e4f5718d76c637f1259"

BASE="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom"
STATE_URL="$BASE/$STATE_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R2.sigma.inc"
TRANS_URL="$BASE/$TRANS_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc"
ADAPTER_URL="$BASE/$ADAPTER_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc"
KERNEL_URL="$BASE/$KERNEL_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R2.sigma.inc"

EXPECTED_STATE="83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33"
EXPECTED_TRANS="3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9"
EXPECTED_ADAPTER="223aeb84c4d4fcc8e1cbdbf62943a38382efa8250de72eb4df4ba3df79e5b02b"
EXPECTED_KERNEL="91d660902bc400ec967904d21aab3be876006777926dee55f7b8b2ec4f01e2f6"

sha() { sha256sum "$1" | awk '{print $1}'; }

printf '%s\n' '=== C5V3 R4 BOUND ADAPTER + ONE-CYCLE KERNEL SOURCE AUDIT R1 FIX1 ==='
echo "MODE=STATIC_SEMANTIC_BINDING_AND_SOURCE_IDENTITY"
echo "VM_EXECUTION=NO"
echo "CORE_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"

curl -fsSL "$STATE_URL" -o "$STATE"
curl -fsSL "$TRANS_URL" -o "$TRANS"
curl -fsSL "$ADAPTER_URL" -o "$ADAPTER"
curl -fsSL "$KERNEL_URL" -o "$KERNEL"

STATE_SHA="$(sha "$STATE")"
TRANS_SHA="$(sha "$TRANS")"
ADAPTER_SHA="$(sha "$ADAPTER")"
KERNEL_SHA="$(sha "$KERNEL")"

echo "STATE_SHA256=$STATE_SHA"
echo "TRANSITIONS_SHA256=$TRANS_SHA"
echo "ADAPTER_R3_SHA256=$ADAPTER_SHA"
echo "KERNEL_R2_SHA256=$KERNEL_SHA"
[ "$STATE_SHA" = "$EXPECTED_STATE" ] || { echo "HOLD=STATE_IDENTITY_MISMATCH"; exit 1; }
[ "$TRANS_SHA" = "$EXPECTED_TRANS" ] || { echo "HOLD=TRANSITIONS_IDENTITY_MISMATCH"; exit 1; }
[ "$ADAPTER_SHA" = "$EXPECTED_ADAPTER" ] || { echo "HOLD=ADAPTER_R3_IDENTITY_MISMATCH"; exit 1; }
[ "$KERNEL_SHA" = "$EXPECTED_KERNEL" ] || { echo "HOLD=KERNEL_R2_IDENTITY_MISMATCH"; exit 1; }
echo "STATE_IDENTITY=PASS"
echo "TRANSITIONS_IDENTITY=PASS"
echo "ADAPTER_R3_IDENTITY=PASS"
echo "KERNEL_R2_IDENTITY=PASS"

python - "$STATE" "$TRANS" "$ADAPTER" "$KERNEL" "$COMBINED" <<'PY'
from pathlib import Path
import hashlib,re,sys
state_path,trans_path,adapter_path,kernel_path,out_path=sys.argv[1:]
parts=[Path(p).read_text() for p in (state_path,trans_path,adapter_path,kernel_path)]
combined='\n\n'.join(x.rstrip() for x in parts)+'\n'
Path(out_path).write_text(combined)

def defs(text):
    return re.findall(r'^DEF\s+([A-Za-z0-9_]+)\s*\(', text, re.M)

def arities(text):
    out=[]
    for m in re.finditer(r'^DEF\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)', text, re.M):
        args=[x.strip() for x in m.group(2).split(',') if x.strip()]
        out.append((m.group(1),len(args)))
    return out

def def_body(text,name):
    m=re.search(r'^DEF\s+'+re.escape(name)+r'\s*\([^)]*\)\s*\{', text, re.M)
    if not m:
        raise SystemExit('HOLD=DEF_NOT_FOUND:'+name)
    start=m.start(); brace=text.find('{',m.start(),m.end())
    depth=0; in_str=False; esc=False
    for i in range(brace,len(text)):
        ch=text[i]
        if in_str:
            if esc: esc=False
            elif ch=='\\': esc=True
            elif ch=='"': in_str=False
        else:
            if ch=='"': in_str=True
            elif ch=='{': depth+=1
            elif ch=='}':
                depth-=1
                if depth==0:
                    return text[start:i+1]
    raise SystemExit('HOLD=DEF_UNBALANCED:'+name)

counts=[len(defs(x)) for x in parts]
labels=['STATE','TRANSITIONS','ADAPTER_R3','KERNEL_R2']
for label,count in zip(labels,counts): print(f'{label}_DEF_COUNT={count}')
print('R4_BOUND_COMBINED_DEF_COUNT='+str(len(defs(combined))))
if counts != [28,12,16,10]: raise SystemExit('HOLD=DEF_COUNTS:'+repr(counts))
if len(defs(combined)) != 66: raise SystemExit('HOLD=COMBINED_DEF_COUNT')
if len(set(defs(combined))) != 66: raise SystemExit('HOLD=DUPLICATE_DEF_NAME')

ars=arities(combined)
mx=max(a for _,a in ars)
print('MAX_DEF_ARITY='+str(mx))
if mx>6: raise SystemExit('HOLD=DEF_ARITY_GT6')

mult=[]
for i,line in enumerate(combined.splitlines(),1):
    if re.match(r'^DEF\s+[A-Za-z0-9_]+\s*\(',line) and '{' not in line:
        mult.append((i,line))
print('MULTILINE_DEF_SIGNATURE_COUNT='+str(len(mult)))
if mult: raise SystemExit('HOLD=MULTILINE_DEF_SIGNATURE')

for tok,label in [
    ('LEFT=','LEFT_EQ'),('RIGHT=','RIGHT_EQ'),
    ('legacy_analyze_segment','LEGACY_ANALYZE_SEGMENT'),
    ('legacy_merge_evidence','LEGACY_MERGE_EVIDENCE'),
    ('"write_text"','DIRECT_WRITE_TEXT'),('"read_text"','DIRECT_READ_TEXT'),
    ('c5l_capability_registry_select','R1_AUTO_CAPABILITY_SELECT')]:
    c=combined.count(tok); print(f'{label}_COUNT={c}')
    if c: raise SystemExit('HOLD=FORBIDDEN_SURFACE:'+label)

adapter=parts[2]; kernel=parts[3]
required_adapter=[
    'IF (source_stance == claim_side) { RETURN "SUPPORT"; }',
    'IF (source_stance == "A") { RETURN "CONTRARY"; }',
    'IF (source_stance == "B") { RETURN "CONTRARY"; }',
    'DEF c5a3_make_source_stance_record(',
    'DEF c5a3_source_stance_record_valid(',
    'DEF c5a3_make_truth_posture(',
    'DEF c5a3_truth_posture_valid('
]
for x in required_adapter:
    c=adapter.count(x); print('ADAPTER_REQUIRED_'+hashlib.sha256(x.encode()).hexdigest()[:12]+'_COUNT='+str(c))
    if c!=1: raise SystemExit('HOLD=ADAPTER_REQUIRED_SURFACE:'+x)

required_kernel_once=[
    'IF (CLAIM_SUBJECT != EVIDENCE_SUBJECT) { RETURN ""; }',
    'IF (SOURCE_ID != STANCE_SOURCE_ID) { RETURN ""; }',
    'IF (c5a3_source_stance_record_valid(stance_record) == 0) { RETURN ""; }',
    'RETURN c5l2_memory_pack(work_id, claim_bank, gap_bank, evidence_ref_bank, revision);',
    'RETURN c5t2_memory_recall_claim(memory, claim_id);',
    'RETURN c5t2_memory_recall_gap(memory, gap_id);'
]
for x in required_kernel_once:
    c=kernel.count(x); print('KERNEL_REQUIRED_'+hashlib.sha256(x.encode()).hexdigest()[:12]+'_COUNT='+str(c))
    if c!=1: raise SystemExit('HOLD=KERNEL_REQUIRED_SURFACE:'+x)

posture_guard='IF (c5a3_truth_posture_valid(posture_record) == 0) { RETURN ""; }'
pg=kernel.count(posture_guard)
print('KERNEL_TRUTH_POSTURE_GUARD_TOTAL_COUNT='+str(pg))
if pg!=2: raise SystemExit('HOLD=KERNEL_TRUTH_POSTURE_GUARD_TOTAL_COUNT')
for name in ('c5c3_revise_claim_from_posture','c5c3_open_conflict_gap'):
    body=def_body(kernel,name)
    c=body.count(posture_guard)
    print('KERNEL_TRUTH_POSTURE_GUARD_'+name+'_COUNT='+str(c))
    if c!=1: raise SystemExit('HOLD=KERNEL_TRUTH_POSTURE_GUARD_DEF:'+name)

print('CONTRARY_EVIDENCE_MAPPING=PASS')
print('CLAIM_EVIDENCE_SUBJECT_BINDING=PASS')
print('STANCE_SOURCE_BINDING=PASS')
print('GATEA_TRUTH_POSTURE_INTERNALIZATION=PASS')
print('TRUTH_POSTURE_GUARD_PER_TRANSITION=PASS')
print('NATIVE_CAPABILITY_AUTO_SELECTION=ABSENT')
print('R4_BOUND_COMBINED_SHA256='+hashlib.sha256(combined.encode()).hexdigest())
print('R4_BOUND_STATIC_GOVERNANCE=PASS')
PY

echo "R4_BOUND_COMBINED_PATH=$COMBINED"
echo "R4_BOUND_COMBINED_SHA256=$(sha "$COMBINED")"
echo "R4_BOUND_ADAPTER_KERNEL_SOURCE_AUDIT=PASS"
echo "RUNTIME_ADMISSION=NO"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"
printf '%s\n' '=== END ==='
