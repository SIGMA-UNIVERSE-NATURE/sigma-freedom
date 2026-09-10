#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
BASE_COMMIT="efe2ecfa07c130a1c73a680818987b5eefbf076a"
BUILDER_PATH="C5_M5/R4_ACADEMIC/RUN_BUILD_C5V3_R4_ACADEMIC_CORE_R1.sh"
EXPECTED_BLOB_SHA="56a6a2ec2d82d2566a7793094915bf1e0c0387d6"
RAW="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/$BASE_COMMIT/$BUILDER_PATH"
TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R4_ACADEMIC_BUILD_FIX1_$$"
mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT

ORIG="$TMP/RUN_BUILD_C5V3_R4_ACADEMIC_CORE_R1.sh"
PATCHED="$TMP/RUN_BUILD_C5V3_R4_ACADEMIC_CORE_R1_FIX1.materialized.sh"
curl -fsSL "$RAW" -o "$ORIG"

python - "$ORIG" "$PATCHED" "$EXPECTED_BLOB_SHA" <<'PY'
from pathlib import Path
import hashlib,sys
src,dst,expected=sys.argv[1:]
data=Path(src).read_bytes()
blob=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
print("ACADEMIC_BUILDER_BASE_GIT_BLOB_SHA="+blob)
if blob != expected:
    raise SystemExit("HOLD=ACADEMIC_BUILDER_BASE_BLOB_IDENTITY")
text=data.decode()
old="m=re.match(r'^DEF\\s+([A-Za-z0-9_]+)\\s*\\(([^)]*)\\)\\s*\\{',lines[i])"
new="m=re.match(r'^DEF\\s+([A-Za-z0-9_]+)\\s*\\(([^)]*)\\)',lines[i])"
count=text.count(old)
print("ACADEMIC_BUILDER_FIX1_MATCH_COUNT="+str(count))
if count != 1:
    raise SystemExit("HOLD=ACADEMIC_BUILDER_FIX1_PATCH_SITE")
text=text.replace(old,new,1)
Path(dst).write_text(text)
print("ACADEMIC_BUILDER_FIX1=PATCHED")
print("ACADEMIC_BUILDER_FIX1_REASON=ALLOW_DEF_BRACE_ON_FOLLOWING_LINE")
print("ACADEMIC_BUILDER_FIX1_DONOR_IDENTITY_POLICY=UNCHANGED")
print("ACADEMIC_BUILDER_FIX1_T123_BOUNDARY_POLICY=UNCHANGED")
PY

chmod 700 "$PATCHED"
exec "$PATCHED" "$ROOT"
