#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
EXPECTED_SOURCE_GIT_BLOB=78a93cc6f61bd7b49362297e79441fa64f1e3f67

SRC_REL=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_04_CASE001_VNM01_EQUALITY_DIAG_V1.sigma
SRC="$REPO/$SRC_REL"

FAILED_ROOT="$HOME_SIGMA/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1_PREFLIGHT"
FAILED_CASE="$FAILED_ROOT/cases/CASE_001_FULL_CHAIN_SUPPORT2"
FAILED_B1="$FAILED_CASE/.sigma_exec/SIGMA_VNM_01_SURFACE_FORM_EVIDENCE_WEIGHTING_V1"
FAILED_HYP="$FAILED_B1/input/hypothesis.memory"
FAILED_EVID="$FAILED_B1/input/evidence.memory"

ROOT="$HOME_SIGMA/SIGMA_VNM_04_CASE001_VNM01_EQUALITY_DIAG_V1_PREFLIGHT"
SANDBOX="$ROOT/sandbox"
BASE="$SANDBOX/.sigma_exec/SIGMA_VNM_04_CASE001_VNM01_EQUALITY_DIAG_V1"
IN="$BASE/input"
BC="$ROOT/SIGMA_VNM_04_CASE001_VNM01_EQUALITY_DIAG_V1.sigmab"
LOG="$ROOT/native.log"
LOCK="$ROOT/diag.lock"

mkdir -p "$ROOT"
exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=VNM04_CASE001_EQUALITY_DIAG_ALREADY_RUNNING\n'
    exit 20
}

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

actual_sigmac=$(sha_of "$SIGMAC")
actual_vm=$(sha_of "$VM")
actual_source_sha=$(sha_of "$SRC")
actual_source_blob=$(cd "$REPO" && git hash-object "$SRC_REL")

printf 'SIGMA_PHASE=VNM04_CASE001_VNM01_EQUALITY_DIAG_V1\n'
printf 'DIAGNOSTIC_ONLY=YES\n'
printf 'DIAGNOSTIC_MUTATES_FAILED_CASE=NO\n'
printf 'DIAGNOSTIC_MUTATES_PRODUCTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'DIAG_SOURCE_GIT_BLOB=%s\n' "$actual_source_blob"
printf 'DIAG_SOURCE_SHA256=%s\n' "$actual_source_sha"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_source_blob" = "$EXPECTED_SOURCE_GIT_BLOB" ] || { printf 'HOLD=DIAG_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }

for F in "$FAILED_HYP" "$FAILED_EVID"; do
    [ -f "$F" ] || { printf 'HOLD=FAILED_CASE_INPUT_MISSING\nMISSING_FILE=%s\n' "$F"; exit 24; }
done

FAILED_HYP_SHA=$(sha_of "$FAILED_HYP")
FAILED_EVID_SHA=$(sha_of "$FAILED_EVID")
printf 'FAILED_HYPOTHESIS_SHA256=%s\n' "$FAILED_HYP_SHA"
printf 'FAILED_EVIDENCE_SHA256=%s\n' "$FAILED_EVID_SHA"

"$P/bin/rm" -rf -- "$SANDBOX"
"$P/bin/mkdir" -p "$IN"
"$P/bin/cp" -f -- "$FAILED_HYP" "$IN/hypothesis.memory" || exit 25
"$P/bin/cp" -f -- "$FAILED_EVID" "$IN/evidence.memory" || exit 26

COPIED_HYP_SHA=$(sha_of "$IN/hypothesis.memory")
COPIED_EVID_SHA=$(sha_of "$IN/evidence.memory")
printf 'COPIED_HYPOTHESIS_SHA256=%s\n' "$COPIED_HYP_SHA"
printf 'COPIED_EVIDENCE_SHA256=%s\n' "$COPIED_EVID_SHA"

[ "$FAILED_HYP_SHA" = "$COPIED_HYP_SHA" ] || { printf 'HOLD=HYPOTHESIS_COPY_MISMATCH\n'; exit 27; }
[ "$FAILED_EVID_SHA" = "$COPIED_EVID_SHA" ] || { printf 'HOLD=EVIDENCE_COPY_MISMATCH\n'; exit 28; }

"$P/bin/rm" -f -- "$BC.partial" "$BC"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 29
[ -s "$BC.partial" ] || exit 30
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 31
"$P/bin/chmod" 0400 "$BC" || exit 32
printf 'DIAG_BYTECODE_SHA256=%s\n' "$(sha_of "$BC")"

(
    cd "$SANDBOX" || exit 90
    "$VM" "$BC"
) >"$LOG" 2>&1
RC=$?

printf '\n=== NATIVE DIAGNOSTIC ===\n'
printf 'VM_RC=%s\n' "$RC"
"$P/bin/cat" "$LOG"

printf '\n=== POST DIAGNOSTIC IMMUTABILITY ===\n'
printf 'FAILED_HYPOTHESIS_UNCHANGED=%s\n' "$([ "$(sha_of "$FAILED_HYP")" = "$FAILED_HYP_SHA" ] && printf YES || printf NO)"
printf 'FAILED_EVIDENCE_UNCHANGED=%s\n' "$([ "$(sha_of "$FAILED_EVID")" = "$FAILED_EVID_SHA" ] && printf YES || printf NO)"
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'DIAGNOSTIC_VM_RC=%s\n' "$RC"

exit "$RC"
