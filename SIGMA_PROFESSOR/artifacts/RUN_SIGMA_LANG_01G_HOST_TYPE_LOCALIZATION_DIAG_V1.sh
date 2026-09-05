#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_LANG_01G_HOST_TYPE_LOCALIZATION_DIAG_V1.sigma"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
EXPECTED_SOURCE_GIT_BLOB=53ca847aa3eebe77e18c404e8dad8b717c9234cb

ROOT="$HOME_SIGMA/SIGMA_LANG_01G_HOST_TYPE_LOCALIZATION_DIAG_V1"
SANDBOX="$ROOT/sandbox"
BASE="$SANDBOX/.sigma_exec/SIGMA_LANG_01G_HOST_TYPE_DIAG_V1"
IN="$BASE/input"
STATE="$BASE/state"
BC="$ROOT/SIGMA_LANG_01G_HOST_TYPE_LOCALIZATION_DIAG_V1.sigmab"
LOG="$ROOT/diag.log"

mkdir -p "$ROOT"

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source_sha=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
actual_source_blob=$("$P/bin/git" -C "$REPO" hash-object "$SRC")

printf 'SIGMA_PHASE=LANG_01G_HOST_TYPE_LOCALIZATION_DIAG_V1\n'
printf 'DIAGNOSTIC_ONLY=YES\n'
printf 'HOST_COGNITION=NO\n'
printf 'HOST_EVIDENCE_SCORING=NO\n'
printf 'HOST_ANTECEDENT_SELECTION=NO\n'
printf 'CANONICAL_ADMISSION_ORACLE_CHANGED=NO\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'DIAG_SOURCE_GIT_BLOB=%s\n' "$actual_source_blob"
printf 'DIAG_SOURCE_SHA256=%s\n' "$actual_source_sha"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || {
    printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'
    exit 21
}
[ "$actual_vm" = "$EXPECTED_VM" ] || {
    printf 'HOLD=VM_IDENTITY_MISMATCH\n'
    exit 22
}
[ "$actual_source_blob" = "$EXPECTED_SOURCE_GIT_BLOB" ] || {
    printf 'HOLD=DIAG_SOURCE_GIT_BLOB_MISMATCH\n'
    exit 23
}

"$P/bin/rm" -rf -- "$SANDBOX"
"$P/bin/mkdir" -p "$IN" "$STATE"

printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_EVIDENCE'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EVIDENCE||E2||F2||Q||R||Q||SOURCE||CTX2
EOF_EVIDENCE

"$P/bin/rm" -f -- "$BC.partial" "$BC"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'DIAG_SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 24
[ -s "$BC.partial" ] || exit 25
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 26

printf 'DIAG_BYTECODE_SHA256='
"$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}'

(
    cd "$SANDBOX" || exit 90
    "$VM" "$BC"
) > "$LOG" 2>&1
RC=$?

printf 'DIAG_VM_RC=%s\n' "$RC"
"$P/bin/cat" "$LOG"

if [ "$RC" -eq 0 ]; then
    if "$P/bin/grep" -F -x 'TRACE_999_COMPLETE' "$LOG" >/dev/null 2>&1; then
        printf 'LANG_01G_HOST_TYPE_LOCALIZATION_DIAG=COMPLETE\n'
        exit 0
    fi
    printf 'LANG_01G_HOST_TYPE_LOCALIZATION_DIAG=FAIL_MISSING_FINAL_TRACE\n'
    exit 40
fi

printf 'LANG_01G_HOST_TYPE_LOCALIZATION_DIAG=STOPPED_AT_FIRST_VM_TYPE_FAILURE\n'
exit 41
