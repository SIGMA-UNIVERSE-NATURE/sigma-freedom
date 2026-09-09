#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
PKG="$ROOT/.sigma_exec/HH_AUTO_INTERNET_LESSONS/V1_R21_SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0"
RUN="$ROOT/.sigma_exec/HH_AUTO_INTERNET_LESSONS/proposition_span_candidate_formations/20260903T041145Z_19479_11375"
OUT="/sdcard/Download/C5V3_V18_R0_RECOVERY_81523feb.zip"
TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_V18_R0_RECOVERY_R1_$$"
mkdir -p "$TMP/export"
trap 'rm -rf "$TMP"' EXIT

EXP_SOURCE="81523feb7c59a90b6bb5d284c65a679d3fd76ad692f84b0a6685c4d2693dcb7a"
EXP_BYTECODE="e800eab3dc6abcbddf0b9c9e0de9d76af2fba6ba1bd49c87157c62fe126a7300"
EXP_VERIFIER_PY="a6664245d02e92dc78f8c7c73b07a58aca27d3dfa989ec9dd675b61aa45f2104"
EXP_RUNNER="747e98334b12e4efff8c11d48cea70a03952c167563d27b27eaf18626c06cb5f"
EXP_VERIFIER="6c7e65cf12ec169186b71bb2260c67d88edb425613eab17905c60513e035a027"
EXP_WRAPPER="d1926a7496a3a77c60832d433f421892bac6882e28e8156dc0554ea894aa5fe3"
EXP_INSTALLER="55c1df76afa8b3b5f7cd39d476f2d8809b4508bfa817bd94202945491d13043f"

printf '%s\n' '=== C5V3 V18 R0 EXACT ARTIFACT RECOVERY R1 ==='
printf 'ROOT=%s\n' "$ROOT"
printf 'SEARCH_SCOPE=ONLY_TWO_CANONICAL_R0_ROOTS\n'
printf 'PACKAGE_ROOT=%s\n' "$PKG"
printf 'RUN_ROOT=%s\n' "$RUN"
printf 'BROAD_HOME_SCAN=NO\nPRODUCTION_MUTATION=NO\nVM_EXECUTION=NO\n'

python - "$PKG" "$RUN" "$TMP/export" \
  "$EXP_SOURCE" "$EXP_BYTECODE" "$EXP_VERIFIER_PY" "$EXP_RUNNER" "$EXP_VERIFIER" "$EXP_WRAPPER" "$EXP_INSTALLER" <<'PY'
from pathlib import Path
import hashlib, os, shutil, sys, json
pkg, run, out = map(Path, sys.argv[1:4])
labels = [
    ('V18_R0_ENGINE_SOURCE', sys.argv[4]),
    ('V18_R0_ENGINE_BYTECODE', sys.argv[5]),
    ('V18_R0_VERIFIER_PY', sys.argv[6]),
    ('V18_R0_RUNNER', sys.argv[7]),
    ('V18_R0_VERIFIER', sys.argv[8]),
    ('V18_R0_WRAPPER', sys.argv[9]),
    ('V18_R0_INSTALLER', sys.argv[10]),
]
expected = {h:l for l,h in labels}
roots = [('PACKAGE',pkg), ('RUN',run)]
found = {}
manifest=[]
for root_label, root in roots:
    print(f'{root_label}_ROOT_EXISTS=' + ('YES' if root.is_dir() else 'NO'))
    if not root.is_dir():
        continue
    for base, dirs, files in os.walk(root):
        # Scope is already one exact canonical R0 tree. Do not follow symlinks.
        dirs[:] = [d for d in dirs if not Path(base,d).is_symlink()]
        for name in files:
            p=Path(base,name)
            if p.is_symlink() or not p.is_file():
                continue
            try:
                b=p.read_bytes()
            except Exception:
                continue
            h=hashlib.sha256(b).hexdigest()
            rel=str(p.relative_to(root))
            if h in expected:
                label=expected[h]
                print(f'MATCH={label}|{root_label}|{rel}|{h}|{len(b)}')
                manifest.append({'label':label,'root':root_label,'relative_path':rel,'sha256':h,'bytes':len(b)})
                if label not in found:
                    safe=label + '__' + name
                    dst=out/safe
                    dst.write_bytes(b)
                    found[label]=str(dst)

(out/'RECOVERY_MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
for label,h in labels:
    print(f'{label}_EXPECTED_SHA256={h}')
    print(f'{label}_RECOVERED=' + ('YES' if label in found else 'NO'))

required=['V18_R0_ENGINE_SOURCE','V18_R0_ENGINE_BYTECODE']
if all(x in found for x in required):
    print('R0_SOURCE_AND_BYTECODE_RECOVERY=PASS')
else:
    print('R0_SOURCE_AND_BYTECODE_RECOVERY=HOLD_NOT_FOUND_AT_CANONICAL_ROOTS')
PY

python - "$TMP/export" "$OUT" <<'PY'
from pathlib import Path
import sys, zipfile
src=Path(sys.argv[1]); out=Path(sys.argv[2])
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(src.iterdir()):
        if p.is_file(): z.write(p,p.name)
PY

printf 'RECOVERY_ZIP=%s\n' "$OUT"
printf 'RECOVERY_ZIP_SHA256=%s\n' "$(sha256sum "$OUT" | awk '{print $1}')"
printf 'RECOVERY_ZIP_BYTES=%s\n' "$(wc -c < "$OUT")"
printf 'PRODUCTION_MUTATION=NO\nVM_EXECUTION=NO\n'
printf '%s\n' '=== END ==='
