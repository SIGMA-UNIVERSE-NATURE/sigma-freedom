#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
SUCCESSOR="$ROOT/.sigma_c5v3_sync/C5V3_R4_SUCCESSOR_T1_T2_T3_R1/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_SUCCESSOR="b1ceedffa11497cab5454639eb1872cc5ecb95a5824b95e4d1be22c2ea2b7406"
EXPECTED_LIVE_CORE="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"

sha() { sha256sum "$1" | awk '{print $1}'; }
lock() {
  local p="$1" e="$2" n="$3" a
  [ -f "$p" ] || { echo "HOLD=MISSING_$n"; echo "PATH=$p"; exit 1; }
  a="$(sha "$p")"
  echo "${n}_PATH=$p"
  echo "${n}_SHA256=$a"
  [ "$a" = "$e" ] || { echo "${n}_IDENTITY=FAIL"; exit 1; }
  echo "${n}_IDENTITY=PASS"
}

echo "=== C5V3 R4 SUCCESSOR R4-PREFIX ENTRY VISIBILITY BINARY SEARCH R1 ==="
echo "MODE=SOURCE_SENSITIVITY_PREFIX_BINARY_SEARCH"
echo "VM_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"
echo "PRODUCTION_BINDING=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" SIGMAC
lock "$SUCCESSOR" "$EXPECTED_SUCCESSOR" SUCCESSOR_SOURCE
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE_BEFORE
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER_BEFORE

python - "$SIGMAC" "$SUCCESSOR" <<'PY'
from pathlib import Path
import hashlib, re, subprocess, sys, tempfile

sigmac=Path(sys.argv[1]); src_path=Path(sys.argv[2])
s=src_path.read_text()
HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'
ENTRY='Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1'

# Extract exact DEF blocks with a small lexical brace scanner that ignores strings/comments.
def extract_defs(text):
    starts=list(re.finditer(r'(?m)^DEF\s+([A-Za-z0-9_]+)\s*\(', text))
    out=[]
    for m in starts:
        name=m.group(1); i=m.start(); j=m.end(); in_str=False; esc=False; comment=False; depth=0; begun=False
        while j < len(text):
            ch=text[j]
            if comment:
                if ch=='\n': comment=False
                j+=1; continue
            if in_str:
                if esc: esc=False
                elif ch=='\\': esc=True
                elif ch=='"': in_str=False
                j+=1; continue
            if ch=='#': comment=True; j+=1; continue
            if ch=='"': in_str=True; j+=1; continue
            if ch=='{': depth+=1; begun=True
            elif ch=='}' and begun:
                depth-=1
                if depth==0:
                    j+=1
                    while j < len(text) and text[j] in ' \t\r': j+=1
                    if j < len(text) and text[j]=='\n': j+=1
                    out.append((name,text[i:j].rstrip('\n')))
                    break
            j+=1
        else:
            raise SystemExit('HOLD=UNTERMINATED_DEF:'+name)
    return out

def norm(bs): return '\n\n'.join(b for _,b in bs)+'\n'

def make_source(defs, literal, balanced=True):
    body=HEADER+'\n\n'+norm(defs)+'\n⟡('+ENTRY+') {\n    ⚡ print("'+literal+'");\n}\n'
    if not balanced:
        t=body.rstrip()
        if not t.endswith('}'): raise RuntimeError('final brace missing')
        body=t[:-1]+'\n'
    return body

def compile_one(tmp, label, source):
    sp=tmp/(label+'.sigma'); bp=tmp/(label+'.sigmab'); lp=tmp/(label+'.log')
    sp.write_text(source)
    p=subprocess.run([str(sigmac),str(sp),str(bp)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    lp.write_text(p.stdout)
    if not bp.exists(): return {'rc':p.returncode,'sha':'ABSENT','bytes':0,'log':p.stdout.strip()}
    data=bp.read_bytes()
    return {'rc':p.returncode,'sha':hashlib.sha256(data).hexdigest(),'bytes':len(data),'log':p.stdout.strip()}

def pair(tmp, label, defs):
    a=compile_one(tmp,label+'_A',make_source(defs,'ENTRY_SENTINEL_A'))
    b=compile_one(tmp,label+'_B',make_source(defs,'ENTRY_SENTINEL_B'))
    visible=(a['rc']==0 and b['rc']==0 and a['sha']!='ABSENT' and b['sha']!='ABSENT' and a['sha']!=b['sha'])
    print(f'{label}_DEF_COUNT={len(defs)}')
    print(f'{label}_A_RC={a["rc"]}')
    print(f'{label}_A_BYTES={a["bytes"]}')
    print(f'{label}_A_SHA256={a["sha"]}')
    print(f'{label}_B_RC={b["rc"]}')
    print(f'{label}_B_BYTES={b["bytes"]}')
    print(f'{label}_B_SHA256={b["sha"]}')
    print(f'{label}_ENTRY_SOURCE_SENSITIVITY={"PASS" if visible else "NO"}')
    return visible,a,b

all_defs=extract_defs(s)
names=[n for n,_ in all_defs]
print('PARSED_SUCCESSOR_DEF_COUNT='+str(len(all_defs)))
if len(all_defs)!=251 or len(set(names))!=251: raise SystemExit('HOLD=SUCCESSOR_DEF_PARSE')
if names[77] != 'c5l2_present': raise SystemExit('HOLD=R4_FIRST_DEF:'+names[77])
if names[168] != 'p0r4_zero_state': raise SystemExit('HOLD=R4_LAST_DEF:'+names[168])
if names[169] != 'WA_H': raise SystemExit('HOLD=T123_FIRST_DEF:'+names[169])
if names[250] != 'T2_SHORTEST_PATH_BOUNDED': raise SystemExit('HOLD=T123_LAST_DEF:'+names[250])

gatea=all_defs[:77]
r4=all_defs[77:169]
tools=all_defs[169:]
print('GATEA_DEF_COUNT='+str(len(gatea)))
print('R4_DEF_COUNT='+str(len(r4)))
print('R4_FIRST_DEF='+r4[0][0])
print('R4_LAST_DEF='+r4[-1][0])
print('T1_T2_T3_DEF_COUNT='+str(len(tools)))
print('T1_T2_T3_FIRST_DEF='+tools[0][0])
print('T1_T2_T3_LAST_DEF='+tools[-1][0])

with tempfile.TemporaryDirectory(prefix='C5V3_R4_PREFIX_VIS_') as td:
    tmp=Path(td)
    print('=== CONTROLS ===')
    base_visible,_,_=pair(tmp,'CONTROL_GATEA77',gatea)
    if not base_visible: raise SystemExit('HOLD=GATEA_BASE_ENTRY_NOT_VISIBLE')

    dummy_upper=('R4PROBE_DUMMY','DEF R4PROBE_DUMMY(value) {\n    RETURN value;\n}')
    dummy_lower=('c5probe_dummy','DEF c5probe_dummy(value) {\n    IF (value == "") { RETURN 0; }\n    RETURN 1;\n}')
    upper_visible,_,_=pair(tmp,'CONTROL_GATEA_PLUS_DUMMY_UPPER',gatea+[dummy_upper])
    lower_visible,_,_=pair(tmp,'CONTROL_GATEA_PLUS_DUMMY_LOWER',gatea+[dummy_lower])

    full_visible,_,_=pair(tmp,'CONTROL_GATEA_PLUS_R4_92',gatea+r4)
    print('R4_FULL_ENTRY_VISIBILITY='+('PASS' if full_visible else 'NO'))
    if full_visible:
        print('RESULT=R4_92_NOT_CAUSAL_UNDER_PREFIX_TEST')
        raise SystemExit(0)

    # Binary-search first R4 prefix that makes the entry literal invisible.
    lo=0; hi=len(r4)
    cache={0:True,len(r4):False}
    while hi-lo>1:
        mid=(lo+hi)//2
        visible,_,_=pair(tmp,f'PREFIX_{mid}',gatea+r4[:mid])
        cache[mid]=visible
        if visible: lo=mid
        else: hi=mid

    suspect=r4[hi-1]
    print('LAST_VISIBLE_R4_PREFIX_COUNT='+str(lo))
    print('FIRST_INVISIBLE_R4_PREFIX_COUNT='+str(hi))
    print('FIRST_SUSPECT_R4_DEF_INDEX='+str(hi))
    print('FIRST_SUSPECT_R4_DEF_NAME='+suspect[0])
    print('FIRST_SUSPECT_SUCCESSOR_DEF_INDEX='+str(77+hi))
    print('FIRST_SUSPECT_DEF_SHA256='+hashlib.sha256((suspect[1]+'\n').encode()).hexdigest())

    # Confirm first bad boundary and isolate the suspect DEF without its preceding R4 prefix.
    prev_visible,_,_=pair(tmp,'BOUNDARY_PREVIOUS',gatea+r4[:lo])
    bad_visible,_,_=pair(tmp,'BOUNDARY_FIRST_BAD',gatea+r4[:hi])
    single_visible,_,_=pair(tmp,'SUSPECT_SINGLE_WITH_GATEA',gatea+[suspect])
    print('BOUNDARY_PREVIOUS_VISIBLE='+('YES' if prev_visible else 'NO'))
    print('BOUNDARY_FIRST_BAD_VISIBLE='+('YES' if bad_visible else 'NO'))
    print('SUSPECT_SINGLE_WITH_GATEA_VISIBLE='+('YES' if single_visible else 'NO'))

    # Negative syntax controls at the visibility boundary.
    neg_good=compile_one(tmp,'NEG_PREVIOUS_UNBALANCED',make_source(gatea+r4[:lo],'NEG_GOOD',False))
    neg_bad=compile_one(tmp,'NEG_BAD_UNBALANCED',make_source(gatea+r4[:hi],'NEG_BAD',False))
    print('PREVIOUS_VISIBLE_UNBALANCED_RC='+str(neg_good['rc']))
    print('FIRST_BAD_UNBALANCED_RC='+str(neg_bad['rc']))

    print('DUMMY_UPPER_ENTRY_VISIBILITY='+('PASS' if upper_visible else 'NO'))
    print('DUMMY_LOWER_ENTRY_VISIBILITY='+('PASS' if lower_visible else 'NO'))
    print('RESULT=FIRST_R4_ENTRY_VISIBILITY_BOUNDARY_ISOLATED')
PY

lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE_AFTER
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER_AFTER
echo "VM_EXECUTION=NO"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"
echo "=== END ==="
