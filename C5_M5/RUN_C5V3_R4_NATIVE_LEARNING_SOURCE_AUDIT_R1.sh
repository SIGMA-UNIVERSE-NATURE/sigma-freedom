#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
OUTROOT="$ROOT/.sigma_c5v3_sync/C5V3_R4_NATIVE_LEARNING_SOURCE_R1"
MOD="$OUTROOT/modules"
mkdir -p "$MOD"

STATE="$MOD/C5_NATIVE_LEARNING_STATE_R1.sigma.inc"
TRANS="$MOD/C5_NATIVE_LEARNING_TRANSITIONS_R1.sigma.inc"
COMBINED="$OUTROOT/C5_R4_NATIVE_LEARNING_MODULES_R1.sigma.inc"

STATE_COMMIT="1a636d034571db0b6cf912532f4fe072bcaea56c"
TRANS_COMMIT="75596c055bcc815e0abeab872f8f2b06b0898b24"
STATE_URL="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/$STATE_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R1.sigma.inc"
TRANS_URL="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/$TRANS_COMMIT/C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_TRANSITIONS_R1.sigma.inc"

EXPECTED_STATE="05807ba4a1534323c2358a7362af8f4ad370a47a676f61d96d51161113bb11cc"
EXPECTED_TRANS="cad80440430a8aa83babb4a336050d3089e51242bc5ef74f41d84d8b56166f58"
EXPECTED_COMBINED="f3847c082e27c7fb2cca9f79b6f1963ad5da2205b58e1e410cb54c600598a791"

sha() { sha256sum "$1" | awk '{print $1}'; }

printf '%s\n' '=== C5V3 R4 NATIVE LEARNING SOURCE AUDIT R1 ==='
echo "MODE=SOURCE_IDENTITY_AND_STATIC_GOVERNANCE_ONLY"
echo "VM_EXECUTION=NO"
echo "CORE_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"

curl -fsSL "$STATE_URL" -o "$STATE"
curl -fsSL "$TRANS_URL" -o "$TRANS"

STATE_SHA="$(sha "$STATE")"
TRANS_SHA="$(sha "$TRANS")"
echo "LEARNING_STATE_SHA256=$STATE_SHA"
echo "LEARNING_TRANSITIONS_SHA256=$TRANS_SHA"
[ "$STATE_SHA" = "$EXPECTED_STATE" ] || { echo "HOLD=LEARNING_STATE_IDENTITY_MISMATCH"; exit 1; }
[ "$TRANS_SHA" = "$EXPECTED_TRANS" ] || { echo "HOLD=LEARNING_TRANSITIONS_IDENTITY_MISMATCH"; exit 1; }
echo "LEARNING_STATE_IDENTITY=PASS"
echo "LEARNING_TRANSITIONS_IDENTITY=PASS"

python - "$STATE" "$TRANS" "$COMBINED" "$EXPECTED_COMBINED" <<'PY'
from pathlib import Path
import hashlib,re,sys
state_path,trans_path,out_path,expected=sys.argv[1:]
s1=Path(state_path).read_text()
s2=Path(trans_path).read_text()
combined=s1.rstrip()+"\n\n"+s2.rstrip()+"\n"
Path(out_path).write_text(combined)

def names(text):
    return re.findall(r'^DEF\s+([A-Za-z0-9_]+)\s*\(',text,re.M)

def arities(text):
    out=[]
    for m in re.finditer(r'^DEF\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)',text,re.M):
        args=[x.strip() for x in m.group(2).split(',') if x.strip()]
        out.append((m.group(1),len(args)))
    return out

n1=names(s1); n2=names(s2); alln=names(combined)
print('LEARNING_STATE_DEF_COUNT='+str(len(n1)))
print('LEARNING_TRANSITIONS_DEF_COUNT='+str(len(n2)))
print('R4_LEARNING_COMBINED_DEF_COUNT='+str(len(alln)))
if len(n1)!=23: raise SystemExit('HOLD=LEARNING_STATE_DEF_COUNT')
if len(n2)!=12: raise SystemExit('HOLD=LEARNING_TRANSITIONS_DEF_COUNT')
if len(alln)!=35: raise SystemExit('HOLD=COMBINED_DEF_COUNT')
if len(set(alln))!=len(alln): raise SystemExit('HOLD=DUPLICATE_DEF_NAME')

for token in ('LEFT=','RIGHT=','legacy_analyze_segment','legacy_merge_evidence','"write_text"','"read_text"'):
    count=combined.count(token)
    print('FORBIDDEN_'+token.replace('"','').replace('=','_EQ').replace(' ','_')+'_COUNT='+str(count))
    if count: raise SystemExit('HOLD=FORBIDDEN_SURFACE:'+token)

bad=[(n,a) for n,a in arities(combined) if a>6]
print('MAX_DEF_ARITY='+str(max(a for _,a in arities(combined))))
if bad: raise SystemExit('HOLD=DEF_ARITY_GT6:'+repr(bad))

mult=[]
for i,line in enumerate(combined.splitlines(),1):
    if re.match(r'^DEF\s+[A-Za-z0-9_]+\s*\(',line) and '{' not in line:
        mult.append((i,line))
print('MULTILINE_DEF_SIGNATURE_COUNT='+str(len(mult)))
if mult: raise SystemExit('HOLD=MULTILINE_DEF_SIGNATURE')

actual=hashlib.sha256(combined.encode()).hexdigest()
print('R4_LEARNING_COMBINED_SHA256='+actual)
if actual!=expected: raise SystemExit('HOLD=COMBINED_IDENTITY_MISMATCH')
print('R4_LEARNING_STATIC_GOVERNANCE=PASS')
PY

echo "R4_LEARNING_COMBINED_PATH=$COMBINED"
echo "R4_LEARNING_COMBINED_SHA256=$(sha "$COMBINED")"
echo "R4_NATIVE_LEARNING_SOURCE_AUDIT=PASS"
echo "RUNTIME_ADMISSION=NO"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"
echo '=== END ==='
