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

SRC="$E/SIGMA_FULL_DOCUMENT_SEGMENT_CURSOR_V2_6F.sigma"
BC="$E/SIGMA_FULL_DOCUMENT_SEGMENT_CURSOR_V2_6F.sigmab"
EXPECTED_SOURCE=adfadcb91e71a38272d09dfc27997faf915ab71666993c67e9288e69b5b3a366

V25_STATE="$HOME_SIGMA/SIGMA_V25_FULL_CORPUS_SURVEY"
SNAPSHOT="$V25_STATE/corpus_snapshot"
FIXTURE_SHA=ccfdecb4cd296cd18d5d44c53be4638b027b212a2c6df2372abd350e2782efac
FIXTURE="$SNAPSHOT/$FIXTURE_SHA.document"

STATE="$HOME_SIGMA/SIGMA_V26_FULL_DOCUMENT_SEGMENT_CURSOR"
LOG="$STATE/log"
LOCK="$STATE/full_document.lock"
INIT="$STATE/INITIALIZED"

DOC_PATH_MEMORY="$E/SIGMA_V26F_DOCUMENT_PATH.memory"
DOC_ID_MEMORY="$E/SIGMA_V26F_DOCUMENT_ID.memory"
CURSOR_MEMORY="$E/SIGMA_V26F_CURSOR.memory"

BATCH_LIMIT=3
EXPECTED_COMPLETE_CURSOR_BYTES=8

mkdir -p "$STATE" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V26F_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V26F_FULL_DOCUMENT_SEGMENT_CURSOR_BATCHED\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'SEGMENT_LINE_BUDGET=8\n'
printf 'BATCH_LIMIT=%s\n' "$BATCH_LIMIT"
printf 'WHOLE_FILE_READ_CURRENT_ABI=YES\n'
printf 'MID_COMMIT_CRASH_ATOMICITY=NOT_PROVEN\n'
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
    printf 'HOLD=V26F_SOURCE_IDENTITY_MISMATCH\n'
    exit 23
}
[ -f "$FIXTURE" ] || {
    printf 'HOLD=MISSING_V26F_FIXTURE path=%s\n' "$FIXTURE"
    exit 24
}

if [ ! -f "$INIT" ]; then
    "$P/bin/printf" '%s' "$FIXTURE" > "$DOC_PATH_MEMORY" || exit 25
    "$P/bin/printf" '%s' "$FIXTURE_SHA" > "$DOC_ID_MEMORY" || exit 26
    : > "$CURSOR_MEMORY" || exit 27
    "$P/bin/printf" 'initialized\n' > "$INIT" || exit 28
    printf 'V26F_INITIALIZATION=FRESH\n'
else
    printf 'V26F_INITIALIZATION=REUSE_PERSISTED_CURSOR\n'
fi

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 29
[ -s "$BC.partial" ] || exit 30
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 31
"$P/bin/chmod" 0400 "$BC" || exit 32

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

CURSOR_BYTES_START=$("$P/bin/wc" -c < "$CURSOR_MEMORY" | "$P/bin/tr" -d ' ')
printf 'CURSOR_BYTES_AT_START=%s\n' "$CURSOR_BYTES_START"

if [ "$CURSOR_BYTES_START" -gt "$EXPECTED_COMPLETE_CURSOR_BYTES" ]; then
    printf 'HOLD=CURSOR_BEYOND_EXPECTED_TEST_SCOPE cursor_bytes=%s\n' "$CURSOR_BYTES_START"
    exit 33
fi

CYCLE=1
COMPLETE=0
LASTLOG=""

while [ "$CYCLE" -le "$BATCH_LIMIT" ]; do
    CURRENT_BYTES=$("$P/bin/wc" -c < "$CURSOR_MEMORY" | "$P/bin/tr" -d ' ')
    RUNLOG="$LOG/cursor_${CURRENT_BYTES}_batch_cycle_${CYCLE}.log"
    LASTLOG="$RUNLOG"

    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?

    printf '\n=== V26F_CYCLE_%s ===\n' "$CYCLE"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"

    if [ "$RC" -ne 0 ]; then
        printf 'V26F_FULL_DOCUMENT_TRAVERSAL=FAIL\n'
        printf 'FAILURE_CYCLE=%s\n' "$CYCLE"
        printf 'CURSOR_BYTES_BEFORE_FAILURE=%s\n' "$CURRENT_BYTES"
        printf 'NEXT_ACTION=PRESERVE_CURSOR_AND_INSPECT_FAILED_SEGMENT\n'
        exit 50
    fi

    if "$P/bin/grep" -F 'DOCUMENT_SEGMENTS_COMPLETE YES' "$RUNLOG" >/dev/null 2>&1; then
        COMPLETE=1
        break
    fi

    AFTER_BYTES=$("$P/bin/wc" -c < "$CURSOR_MEMORY" | "$P/bin/tr" -d ' ')
    EXPECTED_AFTER=$((CURRENT_BYTES + 1))
    printf 'CURSOR_BYTES_AFTER_CYCLE=%s\n' "$AFTER_BYTES"

    [ "$AFTER_BYTES" -eq "$EXPECTED_AFTER" ] || {
        printf 'V26F_FULL_DOCUMENT_TRAVERSAL=FAIL\n'
        printf 'FAILURE=CURSOR_DID_NOT_ADVANCE_EXACTLY_ONE\n'
        exit 51
    }

    CYCLE=$((CYCLE + 1))
done

CURSOR_BYTES_END=$("$P/bin/wc" -c < "$CURSOR_MEMORY" | "$P/bin/tr" -d ' ')

printf '\n=== V26F_BATCH_STATE ===\n'
printf 'CURSOR_BYTES_AT_START=%s\n' "$CURSOR_BYTES_START"
printf 'CURSOR_BYTES_AT_END=%s\n' "$CURSOR_BYTES_END"
printf 'DOCUMENT_COMPLETE_SENTINEL=%s\n' "$COMPLETE"
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'SEGMENT_COMPUTATION_BOUNDED=YES\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'MID_COMMIT_CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'

if [ "$COMPLETE" -eq 1 ]; then
    [ "$CURSOR_BYTES_END" -eq "$EXPECTED_COMPLETE_CURSOR_BYTES" ] || {
        printf 'V26F_FULL_DOCUMENT_TRAVERSAL=FAIL\n'
        printf 'FAILURE=COMPLETE_WITH_UNEXPECTED_CURSOR_BYTES\n'
        exit 52
    }

    "$P/bin/grep" -F 'SEGMENT_INDEX 8' "$LASTLOG" >/dev/null || {
        printf 'V26F_FULL_DOCUMENT_TRAVERSAL=FAIL\n'
        printf 'FAILURE=COMPLETE_SENTINEL_WITHOUT_SEGMENT_INDEX_8\n'
        exit 53
    }

    printf 'V26F_FULL_DOCUMENT_TRAVERSAL=PASS\n'
    printf 'NATIVE_COMPLETE_FIXED_WINDOW_TRAVERSAL=PROVEN_IN_FIXTURE_SCOPE\n'
    printf 'NEXT_ACTION=BUILD_V27_STRUCTURAL_GROUPING_PREFLIGHT\n'
    exit 0
fi

printf 'V26F_FULL_DOCUMENT_TRAVERSAL=BATCH_COMPLETE\n'
printf 'NEXT_ACTION=RERUN_SAME_RUNNER_TO_RESUME_NEXT_SEGMENT_BATCH\n'
exit 0
