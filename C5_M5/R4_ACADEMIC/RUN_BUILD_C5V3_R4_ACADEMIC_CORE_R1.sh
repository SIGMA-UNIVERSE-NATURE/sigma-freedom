#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
R3="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
OUTROOT="$ROOT/.sigma_c5v3_sync/C5V3_R4_ACADEMIC_CORE_R1"
MOD="$OUTROOT/modules"
SRC="$OUTROOT/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
BIN="$OUTROOT/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R4_ACADEMIC_BUILD_R1_$$"
mkdir -p "$MOD" "$OUTROOT/src" "$OUTROOT/bin" "$TMP"
trap 'rm -rf "$TMP"' EXIT

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_R3="152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8"
EXPECTED_LIVE_CORE="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"
EXPECTED_GATEA_BUNDLE="ff3fced4c16bf3866e30853e01f5bb634a87ac25943ba612a3cdf1cdf2708494"
EXPECTED_GATEA_SOURCE="bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1"
EXPECTED_STATE="83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33"
EXPECTED_TRANS="3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9"
EXPECTED_ADAPTER="223aeb84c4d4fcc8e1cbdbf62943a38382efa8250de72eb4df4ba3df79e5b02b"
EXPECTED_DURABLE="514c52fcc2e8e1fc5ea64e78b664b7651c8c0ce20c2d463b5fe505c95f9becd2"
EXPECTED_KERNEL="db2a0454fc429d58b9617a40a6e4283f632b35df2c6190e6389820402e1035b1"
EXPECTED_P0="cad40e8ded7138d7e56c8cbb219eba5e43d10d78fc18e7f335073f048f1bad82"

STATE_COMMIT="ca6d9504f5e75c4d5ccf48ab7c574614a8b019be"
TRANS_COMMIT="3debd57e8f0ac3dce7bba540cb912c0ffbadef29"
ADAPTER_COMMIT="02bb0c6d60f2568583211b16baa8fbbd3de0e77f"
DURABLE_COMMIT="b334a1ff23d068551d46b1f114b8ad45afbf46e3"
KERNEL_COMMIT="89019543f98b39cd34ea95535a14c77f050360ea"
P0_COMMIT="ba42087f602baf274c6ed5c90ae3f7a92d647eba"
ACADEMIC_STATE_COMMIT="4827021d47d3bb4694c92983b0291e0492da41c7"
ACADEMIC_DOCUMENT_COMMIT="5fcb584e84231c62fa8e1988de4bfe39da2b9689"
ACADEMIC_REASONING_COMMIT="711a76d36ec68b1d209872ce39e2ba1b889353dd"
ACADEMIC_CAPABILITY_COMMIT="59ef15a404e57c7207136e9a6460a3d44598a3b3"
ACADEMIC_MEMORY_COMMIT="fdb8fe26cc319973d130ea590c5a3fa4b0654d49"
ACADEMIC_MAIN_COMMIT="e522b5b1563c354d123ec97044e3a0209554852a"
BASE="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom"
HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'
ENTRY='Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1'

sha(){ sha256sum "$1" | awk '{print $1}'; }
lock(){
  local p="$1" e="$2" n="$3" a
  [ -f "$p" ] || { echo "HOLD=MISSING_$n"; echo "PATH=$p"; exit 1; }
  a="$(sha "$p")"
  echo "${n}_SHA256=$a"
  [ "$a" = "$e" ] || { echo "HOLD=${n}_IDENTITY"; exit 1; }
  echo "${n}_IDENTITY=PASS"
}
fetch_exact(){
  local commit="$1" path="$2" out="$3" expected="$4" label="$5"
  curl -fsSL "$BASE/$commit/$path" -o "$out"
  echo "${label}_SHA256=$(sha "$out")"
  [ "$(sha "$out")" = "$expected" ] || { echo "HOLD=${label}_IDENTITY"; exit 1; }
  echo "${label}_IDENTITY=PASS"
}
fetch_pinned(){
  local commit="$1" path="$2" out="$3" label="$4"
  curl -fsSL "$BASE/$commit/$path" -o "$out"
  [ -s "$out" ] || { echo "HOLD=${label}_EMPTY"; exit 1; }
  echo "${label}_COMMIT=$commit"
  echo "${label}_SHA256=$(sha "$out")"
  echo "${label}_COMMIT_PIN=PASS"
}

printf '%s\n' '=== BUILD C5V3 R4 ACADEMIC CORE R1 ==='
echo 'MODE=CANONICAL_ACADEMIC_CORE_BUILD'
echo 'PRODUCTION_MUTATION=NO'
echo 'PRODUCTION_BINDING=NO'
lock "$SIGMAC" "$EXPECTED_SIGMAC" SIGMAC
lock "$R3" "$EXPECTED_R3" R3_FIX1_DONOR
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE_BEFORE
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER_BEFORE

BUNDLE=""
for p in \
  "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip" \
  "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip"; do
  if [ -f "$p" ] && [ "$(sha "$p")" = "$EXPECTED_GATEA_BUNDLE" ]; then BUNDLE="$p"; break; fi
done
[ -n "$BUNDLE" ] || { echo 'HOLD=EXACT_GATEA_BUNDLE_NOT_FOUND'; exit 1; }
GATEA="$TMP/gatea.sigma"
MEMBER='SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2/SIGMA_C5_C5V3_M5_BLIND_SCOPED_PROVISIONAL_EPISTEMIC_TRUTH_R1/core.sigma'
unzip -p "$BUNDLE" "$MEMBER" > "$GATEA"
lock "$GATEA" "$EXPECTED_GATEA_SOURCE" GATEA_SOURCE

STATE="$MOD/C5_NATIVE_LEARNING_STATE_R2.sigma.inc"
TRANS="$MOD/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc"
ADAPTER="$MOD/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc"
DURABLE="$MOD/C5_R4_DURABLE_LEARNING_MODEL_R1.sigma.inc"
KERNEL="$MOD/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R3.sigma.inc"
P0="$MOD/C5_R4_P0_TRANSACTION_TRUST_R1.sigma.inc"
AS="$MOD/C5_R4_ACADEMIC_STATE_R1.sigma.inc"
AD="$MOD/C5_R4_ACADEMIC_DOCUMENT_MODEL_R1.sigma.inc"
AK="$MOD/C5_R4_ACADEMIC_REASONING_KERNEL_R1.sigma.inc"
AC="$MOD/C5_R4_ACADEMIC_CAPABILITY_CONTRACT_R1.sigma.inc"
AM="$MOD/C5_R4_ACADEMIC_MEMORY_R1.sigma.inc"
MAIN="$MOD/C5_R4_ACADEMIC_TRANSACTION_MAIN_R1.sigma.inc"

fetch_exact "$STATE_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R2.sigma.inc' "$STATE" "$EXPECTED_STATE" STATE
fetch_exact "$TRANS_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc' "$TRANS" "$EXPECTED_TRANS" TRANSITIONS
fetch_exact "$ADAPTER_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc' "$ADAPTER" "$EXPECTED_ADAPTER" ADAPTER
fetch_exact "$DURABLE_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_DURABLE_LEARNING_MODEL_R1.sigma.inc' "$DURABLE" "$EXPECTED_DURABLE" DURABLE
fetch_exact "$KERNEL_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R3.sigma.inc' "$KERNEL" "$EXPECTED_KERNEL" KERNEL
fetch_exact "$P0_COMMIT" 'C5_M5/R4_NATIVE_LEARNING/C5_R4_P0_TRANSACTION_TRUST_R1.sigma.inc' "$P0" "$EXPECTED_P0" P0
fetch_pinned "$ACADEMIC_STATE_COMMIT" 'C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_STATE_R1.sigma.inc' "$AS" ACADEMIC_STATE
fetch_pinned "$ACADEMIC_DOCUMENT_COMMIT" 'C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_DOCUMENT_MODEL_R1.sigma.inc' "$AD" ACADEMIC_DOCUMENT
fetch_pinned "$ACADEMIC_REASONING_COMMIT" 'C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_REASONING_KERNEL_R1.sigma.inc' "$AK" ACADEMIC_REASONING
fetch_pinned "$ACADEMIC_CAPABILITY_COMMIT" 'C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_CAPABILITY_CONTRACT_R1.sigma.inc' "$AC" ACADEMIC_CAPABILITY
fetch_pinned "$ACADEMIC_MEMORY_COMMIT" 'C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_MEMORY_R1.sigma.inc' "$AM" ACADEMIC_MEMORY
fetch_pinned "$ACADEMIC_MAIN_COMMIT" 'C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_TRANSACTION_MAIN_R1.sigma.inc' "$MAIN" ACADEMIC_MAIN

python - "$HEADER" "$ENTRY" "$GATEA" "$R3" "$STATE" "$TRANS" "$ADAPTER" "$DURABLE" "$KERNEL" "$P0" "$AS" "$AD" "$AK" "$AC" "$AM" "$MAIN" "$SRC" <<'PY'
from pathlib import Path
import hashlib,re,sys
(header,entry,gatea_path,r3_path,state_path,trans_path,adapter_path,durable_path,kernel_path,p0_path,
 academic_state_path,academic_doc_path,academic_kernel_path,academic_cap_path,academic_mem_path,main_path,out_path)=sys.argv[1:]

def blocks(text):
    lines=text.splitlines(True); out=[]; i=0
    while i<len(lines):
        m=re.match(r'^DEF\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)\s*\{',lines[i])
        if not m: i+=1; continue
        name=m.group(1); args=[x.strip() for x in m.group(2).split(',') if x.strip()]
        buf=[]; depth=0; started=False; j=i
        while j<len(lines):
            line=lines[j]; buf.append(line)
            depth += line.count('{'); depth -= line.count('}')
            if '{' in line: started=True
            if started and depth==0: break
            j+=1
        if not started or depth!=0: raise SystemExit('HOLD=UNBALANCED_DEF:'+name)
        body=''.join(x for x in buf if not x.lstrip().startswith('#')).rstrip('\n')
        out.append((name,args,body)); i=j+1
    return out

g=blocks(Path(gatea_path).read_text())
if len(g)!=78: raise SystemExit('HOLD=GATEA_DEF_COUNT:'+str(len(g)))
if sum(1 for n,_,_ in g if n=='append_line')!=1: raise SystemExit('HOLD=GATEA_APPEND_LINE_COUNT')
g=[x for x in g if x[0]!='append_line']

r=blocks(Path(r3_path).read_text())
if len(r)!=176: raise SystemExit('HOLD=R3_DEF_COUNT:'+str(len(r)))
rnames=[n for n,_,_ in r]
a=rnames.index('WA_H'); b=rnames.index('T2_SHORTEST_PATH_BOUNDED')
t123=r[a:b+1]
if a!=94 or b!=175 or len(t123)!=82: raise SystemExit('HOLD=T123_BOUNDARY')

base=[]
for p,expected in [(state_path,28),(trans_path,12),(adapter_path,16),(durable_path,10),(kernel_path,12),(p0_path,14)]:
    bs=blocks(Path(p).read_text())
    if len(bs)!=expected: raise SystemExit('HOLD=R4_MODULE_DEF_COUNT:'+p+':'+str(len(bs)))
    base.extend(bs)
if len(base)!=92: raise SystemExit('HOLD=R4_DEF_COUNT')

academic=[]
module_counts=[]
for p in [academic_state_path,academic_doc_path,academic_kernel_path,academic_cap_path,academic_mem_path]:
    bs=blocks(Path(p).read_text()); module_counts.append(len(bs)); academic.extend(bs)
if module_counts != [19,24,23,7,11]: raise SystemExit('HOLD=ACADEMIC_MODULE_DEF_COUNTS:'+repr(module_counts))
if len(academic)!=84: raise SystemExit('HOLD=ACADEMIC_DEF_COUNT:'+str(len(academic)))
if any('read_text' in body or 'write_text' in body for _,_,body in academic): raise SystemExit('HOLD=ACADEMIC_PURE_DIRECT_IO')
if any(len(args)>6 for _,args,_ in academic): raise SystemExit('HOLD=ACADEMIC_DEF_ARITY_GT6')

main_lines=Path(main_path).read_text().splitlines(True)
main=''.join(x for x in main_lines if not x.lstrip().startswith('#')).strip()+'\n'
if sum(1 for x in main.splitlines() if x.startswith('⟡('))!=1: raise SystemExit('HOLD=MAIN_ENTRY_COUNT')
if not main.startswith('⟡('+entry+') {'): raise SystemExit('HOLD=MAIN_ENTRY_ID')
if any(x.lstrip().startswith('#') for x in main.splitlines()): raise SystemExit('HOLD=MAIN_HASH_COMMENT_REMAINS')

all_defs=g+base+t123+academic
names=[n for n,_,_ in all_defs]
if len(names)!=335: raise SystemExit('HOLD=TOTAL_DEF_COUNT:'+str(len(names)))
if len(set(names))!=len(names):
    dup=sorted({n for n in names if names.count(n)>1})
    raise SystemExit('HOLD=DUPLICATE_DEF:'+','.join(dup))
source=header+'\n\n'+'\n\n'.join(body for _,_,body in all_defs)+'\n\n'+main
lines=source.splitlines()
if sum(1 for x in lines if x.startswith('#SIGMAUNIVERSE_LANGUAGE['))!=1: raise SystemExit('HOLD=HEADER_COUNT')
if sum(1 for x in lines if x.startswith('⟡('))!=1: raise SystemExit('HOLD=ENTRY_COUNT')
if any(x.lstrip().startswith('#') and not x.startswith('#SIGMAUNIVERSE_LANGUAGE[') for x in lines): raise SystemExit('HOLD=EXECUTABLE_COMMENT_REMAINS')
for token in ('legacy_analyze_segment','legacy_merge_evidence','LEFT=','RIGHT='):
    if token in source: raise SystemExit('HOLD=FORBIDDEN:'+token)
if 'UNDERSTOOD' in source: raise SystemExit('HOLD=EOF_UNDERSTOOD_COUPLING_PRESENT')
for required in ('ACADEMIC_DOCUMENT','ACADEMIC_PASSAGE','ACADEMIC_CITATION','ACADEMIC_OBSERVATION','ACADEMIC_SYNTHESIS','NATIVE_ACADEMIC_MEMORY_R1','EXECUTE_EXACT_NATIVE_CAPABILITY','CAPABILITY_RESULT_READY','EVIDENCE_SEARCH'):
    if required not in source: raise SystemExit('HOLD=MISSING_ACADEMIC_SURFACE:'+required)
if 'CANDIDATE_A' in main or 'CANDIDATE_B' in main: raise SystemExit('HOLD=ACADEMIC_MAIN_HOST_CANDIDATE_SURFACE')
Path(out_path).write_text(source)
print('ACADEMIC_GATEA_DEF_COUNT='+str(len(g)))
print('ACADEMIC_R4_BASE_DEF_COUNT='+str(len(base)))
print('ACADEMIC_T1_T2_T3_DEF_COUNT='+str(len(t123)))
print('ACADEMIC_NEW_DEF_COUNT='+str(len(academic)))
print('ACADEMIC_MODULE_DEF_COUNTS='+','.join(map(str,module_counts)))
print('ACADEMIC_TOTAL_DEF_COUNT='+str(len(names)))
print('ACADEMIC_TOTAL_UNIQUE_DEF_COUNT='+str(len(set(names))))
print('ACADEMIC_ENTRY_COUNT=1')
print('ACADEMIC_EXECUTABLE_COMMENT_COUNT=0')
print('ACADEMIC_PURE_DIRECT_READ_TEXT_COUNT=0')
print('ACADEMIC_PURE_DIRECT_WRITE_TEXT_COUNT=0')
print('ACADEMIC_MAX_DEF_ARITY='+str(max(len(args) for _,args,_ in academic)))
print('ACADEMIC_EOF_UNDERSTOOD_COUPLING=ABSENT')
print('ACADEMIC_HOST_CANDIDATE_SURFACE=ABSENT')
print('ACADEMIC_NATIVE_CAPABILITY_SELECTION_SURFACE=PASS_STATIC')
print('ACADEMIC_SOURCE_BYTES='+str(len(source.encode())))
print('ACADEMIC_SOURCE_SHA256='+hashlib.sha256(source.encode()).hexdigest())
PY

echo "ACADEMIC_CORE_SOURCE_PATH=$SRC"
echo "ACADEMIC_CORE_SOURCE_SHA256=$(sha "$SRC")"
rm -f "$BIN" "$TMP/compile.log"
set +e
"$SIGMAC" "$SRC" "$BIN" >"$TMP/compile.log" 2>&1
RC=$?
set -e
echo "ACADEMIC_CORE_COMPILE_RC=$RC"
[ -s "$TMP/compile.log" ] && sed 's/^/ACADEMIC_CORE_COMPILE_LOG=/' "$TMP/compile.log"
[ "$RC" -eq 0 ] || { echo 'ACADEMIC_CORE_BUILD=HOLD_COMPILE'; exit 1; }
[ -f "$BIN" ] || { echo 'ACADEMIC_CORE_BUILD=HOLD_NO_BYTECODE'; exit 1; }
echo "ACADEMIC_CORE_BYTECODE_PATH=$BIN"
echo "ACADEMIC_CORE_BYTECODE_BYTES=$(wc -c < "$BIN")"
echo "ACADEMIC_CORE_BYTECODE_SHA256=$(sha "$BIN")"
echo 'ACADEMIC_CORE_BUILD=PASS'
echo 'ACADEMIC_CORE_RUNTIME_ADMISSION=NOT_YET_RUN'
echo 'ACADEMIC_TEXT_CAPABILITY_RUNTIME=REQUIRES_EXACT_ADMITTED_CAPABILITY'
echo 'ACADEMIC_EXTERNAL_EVIDENCE_LOOP=NOT_YET_ACTIVATED'
echo 'T1_T2_T3_PRESENT_EXACT_BODY_SCOPE=YES'
echo 'T1_T2_T3_NATIVE_UTILIZATION=NOT_YET_PROVEN'
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE_AFTER
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER_AFTER
echo 'PRODUCTION_BINDING=NO'
echo 'PRODUCTION_MUTATION=NO'
printf '%s\n' '=== END ==='
