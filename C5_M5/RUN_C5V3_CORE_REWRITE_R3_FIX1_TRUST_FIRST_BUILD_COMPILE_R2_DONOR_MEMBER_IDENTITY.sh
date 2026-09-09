#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
DONOR="${2:-}"

EXPECTED_M5_PARENT="bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1"
BASE_SCRIPT_COMMIT="11b45bd748f924e413ffc4eb8b8f183ea9a47e3e"
BASE_SCRIPT_URL="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/${BASE_SCRIPT_COMMIT}/C5_M5/RUN_C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST_BUILD_COMPILE_R1.sh"

TMP_BASE="$TMPDIR/RUN_C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST_BUILD_COMPILE_R1.base.sh"
TMP_RUN="$TMPDIR/RUN_C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST_BUILD_COMPILE_R2.local.sh"

printf '%s\n' '=== C5V3 R3 FIX1 DONOR MEMBER IDENTITY RESOLUTION ==='
echo "ROOT=$ROOT"
echo "CONTAINER_IDENTITY_AUTHORITY=NO"
echo "EXACT_COGNITION_MEMBER_IDENTITY_AUTHORITY=YES"
echo "EXPECTED_M5_PARENT_SHA256=$EXPECTED_M5_PARENT"
echo "DIRECTORY_SCAN=NO"
echo "EXACT_PATHS_ONLY=YES"

if [ -z "$DONOR" ]; then
    for C in \
        "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip" \
        "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip" \
        "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H1_BUNDLE(1).zip" \
        "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H1_BUNDLE.zip" \
        "$HOME/storage/downloads/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip" \
        "$HOME/storage/downloads/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip" \
        "$HOME/storage/downloads/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H1_BUNDLE(1).zip" \
        "$HOME/storage/downloads/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H1_BUNDLE.zip" \
        "$HOME/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip" \
        "$HOME/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip" \
        "$HOME/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H1_BUNDLE(1).zip" \
        "$HOME/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H1_BUNDLE.zip"
    do
        if [ -f "$C" ]; then
            DONOR="$C"
            break
        fi
    done
fi

[ -n "$DONOR" ] && [ -f "$DONOR" ] || {
    echo "HOLD=COGNITION_DONOR_CONTAINER_NOT_FOUND"
    echo "REQUIRED_MEMBER_SHA256=$EXPECTED_M5_PARENT"
    exit 1
}

DONOR_SHA="$(sha256sum "$DONOR" | awk '{print $1}')"
echo "DONOR_CONTAINER=$DONOR"
echo "DONOR_CONTAINER_SHA256=$DONOR_SHA"

python - "$DONOR" "$EXPECTED_M5_PARENT" <<'PY'
import hashlib, sys, zipfile
path, expected = sys.argv[1:]
try:
    z = zipfile.ZipFile(path)
except Exception as e:
    raise SystemExit("HOLD=DONOR_CONTAINER_NOT_VALID_ZIP:" + str(e))
with z:
    members = [n for n in z.namelist()
               if n.endswith("/SIGMA_C5_C5V3_M5_NATIVE_SCOPED_PROVISIONAL_EPISTEMIC_TRUTH_R1/core.sigma")]
    if len(members) != 1:
        raise SystemExit("HOLD=EXACT_M5_PARENT_MEMBER_COUNT_NOT_ONE")
    data = z.read(members[0])
actual = hashlib.sha256(data).hexdigest()
print("M5_PARENT_MEMBER=" + members[0])
print("M5_PARENT_SHA256=" + actual)
if actual != expected:
    raise SystemExit("HOLD=M5_PARENT_IDENTITY_MISMATCH")
print("M5_PARENT_IDENTITY=PASS")
print("DONOR_CONTAINER_ACCEPTED_AS_TRANSPORT_ONLY=YES")
PY

curl -fsSL "$BASE_SCRIPT_URL" -o "$TMP_BASE"

python - "$TMP_BASE" "$TMP_RUN" "$DONOR_SHA" <<'PY'
from pathlib import Path
import sys
src, dst, donor_sha = sys.argv[1:]
s = Path(src).read_text()
old = 'EXPECTED_BUNDLE="ff3fced4c16bf3866e30853e01f5bb634a87ac25943ba612a3cdf1cdf2708494"'
new = f'EXPECTED_BUNDLE="{donor_sha}"'
if s.count(old) != 1:
    raise SystemExit("HOLD=BASE_SCRIPT_EXPECTED_BUNDLE_PATCH_COUNT_NOT_ONE")
s = s.replace(old, new)
Path(dst).write_text(s)
PY

chmod 700 "$TMP_RUN"
echo "LOCAL_GATE_CONTAINER_SHA_LOCK=$DONOR_SHA"
echo "LOCAL_GATE_MEMBER_SHA_LOCK=$EXPECTED_M5_PARENT"

exec bash "$TMP_RUN" "$ROOT" "$DONOR"
