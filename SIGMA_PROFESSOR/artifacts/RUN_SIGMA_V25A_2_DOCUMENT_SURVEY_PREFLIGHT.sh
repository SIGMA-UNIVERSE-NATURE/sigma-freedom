#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
WORK="$HOME_SIGMA/sigma-freedom-write"
BRAIN="$WORK/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC="$E/SIGMA_DOCUMENT_SURVEY_V2_5A_2.sigma"
BC="$E/SIGMA_DOCUMENT_SURVEY_V2_5A_2.sigmab"
EXPECTED_SOURCE=153431aa3f78e282ddf0b2ddd73be993440abd9ce4118d4e717aa5ce83f14eb8

PROD_STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
PROD_RAW="$PROD_STATE/raw"

STATE="$HOME_SIGMA/SIGMA_V25_DOCUMENT_SURVEY_PREFLIGHT"
TEST_RAW="$STATE/raw"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"

RAW_DIR_MEMORY="$E/SIGMA_V25T_RAW_DIR.memory"
SURVEYED_MEMORY="$E/SIGMA_V25T_SURVEYED_DOCUMENTS.memory"
SURVEY_MEMORY="$E/SIGMA_V25T_DOCUMENT_SURVEY.memory"

SHORT_SHA=0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4
LONG_SHA=d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de
CURRENT_SHA=c40f0bb8c9ca36d2f5b9a62a8c5a488a12b32ac3f7bac4e03b7037f9ff236930

mkdir -p "$STATE" "$TEST_RAW" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V25A_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V25A_2_DOCUMENT_SURVEY_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'PRODUCTION_LEARNER_MUTATION=NO_BY_NAMESPACE_ISOLATION\n'
printf 'SURVEY_POLICY=FIRST_UNSURVEYED_SORTED_CORPUS_ENTRY_NATIVE\n'
printf 'SURVEY_LINE_BUDGET=32\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || {
    printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'
    exit 21
}
[ "$actual_vm" = "$EXPECTED_VM" ] || {
    printf 'HOLD=VM_IDENTITY_MISMATCH\n'
    exit 22
}
[ "$actual_source" = "$EXPECTED_SOURCE" ] || {
    printf 'HOLD=V25A_SOURCE_IDENTITY_MISMATCH\n'
    exit 23
}

for SHA in "$SHORT_SHA" "$LONG_SHA" "$CURRENT_SHA"; do
    SRC_DOC="$PROD_RAW/$SHA.document"
    [ -f "$SRC_DOC" ] || {
        printf 'HOLD=MISSING_QA_DOCUMENT sha=%s path=%s\n' "$SHA" "$SRC_DOC"
        exit 24
    }

    DEST="$TEST_RAW/$SHA.document"
    PART="$DEST.partial.$$"
    "$P/bin/rm" -f -- "$PART"
    "$P/bin/cp" -- "$SRC_DOC" "$PART" || exit 25
    "$P/bin/chmod" 0400 "$PART" || exit 26
    "$P/bin/mv" -f -- "$PART" "$DEST" || exit 27
done

"$P/bin/printf" '%s' "$TEST_RAW" > "$RAW_DIR_MEMORY" || exit 28
: > "$SURVEYED_MEMORY" || exit 29
: > "$SURVEY_MEMORY" || exit 30

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 31
[ -s "$BC.partial" ] || exit 32
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 33
"$P/bin/chmod" 0400 "$BC" || exit 34

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

PASS=1

for N in 1 2 3 4; do
    RUNLOG="$LOG/run_$N.log"
    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?

    printf '\n=== V25A_RUN_%s ===\n' "$N"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"

    if [ "$RC" -ne 0 ]; then
        PASS=0
        break
    fi
done

printf '\n=== V25A_PERSISTED_SURVEY ===\n'
"$P/bin/cat" "$SURVEY_MEMORY"

printf '\n=== V25A_SURVEYED_DOCUMENTS ===\n'
"$P/bin/cat" "$SURVEYED_MEMORY"

SURVEYED_COUNT=$("$P/bin/grep" -c '.document$' "$SURVEYED_MEMORY" 2>/dev/null || true)
RECORD_COUNT=$("$P/bin/grep" -c '^DOC=' "$SURVEY_MEMORY" 2>/dev/null || true)
COMPLETE_SEEN=0
if [ -f "$LOG/run_4.log" ]; then
    "$P/bin/grep" -F 'SURVEY_COMPLETE YES' "$LOG/run_4.log" >/dev/null 2>&1 && COMPLETE_SEEN=1
fi

printf '\nV25A_SURVEYED_COUNT=%s\n' "$SURVEYED_COUNT"
printf 'V25A_RECORD_COUNT=%s\n' "$RECORD_COUNT"
printf 'V25A_COMPLETE_SENTINEL=%s\n' "$COMPLETE_SEEN"
printf 'V25A_WRITES_PRODUCTION_NAMESPACE=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'

if [ "$PASS" -eq 1 ] && [ "$SURVEYED_COUNT" -eq 3 ] && [ "$RECORD_COUNT" -eq 3 ] && [ "$COMPLETE_SEEN" -eq 1 ]; then
    printf 'V25A_2_DOCUMENT_SURVEY_PREFLIGHT=PASS\n'
    printf 'NEXT_ACTION=BUILD_V25_FULL_CORPUS_SURVEY_RUNNER\n'
    exit 0
fi

printf 'V25A_2_DOCUMENT_SURVEY_PREFLIGHT=FAIL\n'
printf 'NEXT_ACTION=INSPECT_FIRST_FAILED_VM_OP_OR_STATE_TRANSITION\n'
exit 50
