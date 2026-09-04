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

SRC="$E/SIGMA_DOCUMENT_SURVEY_V2_5B_2.sigma"
BC="$E/SIGMA_DOCUMENT_SURVEY_V2_5B_2.sigmab"
EXPECTED_SOURCE=b260544d4afdf8787a2653ee4b3350a6b76663c4377252623638db82e2502d3b

PROD_STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
PROD_RAW="$PROD_STATE/raw"

STATE="$HOME_SIGMA/SIGMA_V25_FULL_CORPUS_SURVEY"
SNAPSHOT="$STATE/corpus_snapshot"
SNAPSHOT_READY="$STATE/SNAPSHOT_READY"
LOG="$STATE/log"
LOCK="$STATE/survey.lock"

RAW_DIR_MEMORY="$E/SIGMA_V25B_RAW_DIR.memory"
SURVEY_MEMORY="$E/SIGMA_V25B2_DOCUMENT_SURVEY.memory"

mkdir -p "$STATE" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V25B_FULL_CORPUS_SURVEY_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V25B_2_FULL_CORPUS_DOCUMENT_SURVEY_BATCHED\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'HOST_CORPUS_SNAPSHOT=MECHANICAL_ALL_DOCUMENT_FILES_PRESENT_AT_INITIALIZATION\n'
printf 'PRODUCTION_RAW_MUTATED=NO\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'SURVEY_COMPUTATION_LINE_BUDGET=32\n'
printf 'WHOLE_FILE_READ_CURRENT_ABI=YES\n'
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
    printf 'HOLD=V25B_SOURCE_IDENTITY_MISMATCH\n'
    exit 23
}

if [ ! -f "$SNAPSHOT_READY" ]; then
    TMP="$STATE/corpus_snapshot.partial.$$"
    "$P/bin/rm" -rf -- "$TMP"
    "$P/bin/mkdir" -p "$TMP" || exit 24

    SNAPSHOT_COUNT=0
    for DOC in "$PROD_RAW"/*.document; do
        [ -f "$DOC" ] || continue
        NAME=${DOC##*/}
        PART="$TMP/$NAME.partial"
        "$P/bin/cp" -- "$DOC" "$PART" || exit 25
        "$P/bin/chmod" 0400 "$PART" || exit 26
        "$P/bin/mv" -f -- "$PART" "$TMP/$NAME" || exit 27
        SNAPSHOT_COUNT=$((SNAPSHOT_COUNT + 1))
    done

    [ "$SNAPSHOT_COUNT" -gt 0 ] || {
        printf 'HOLD=NO_DOCUMENTS_IN_PRODUCTION_RAW\n'
        exit 28
    }

    "$P/bin/rm" -rf -- "$SNAPSHOT"
    "$P/bin/mv" -- "$TMP" "$SNAPSHOT" || exit 29
    "$P/bin/printf" '%s\n' "$SNAPSHOT_COUNT" > "$SNAPSHOT_READY" || exit 30
    printf 'SNAPSHOT_CREATED=YES\n'
    printf 'SNAPSHOT_DOCUMENT_COUNT=%s\n' "$SNAPSHOT_COUNT"
else
    SNAPSHOT_COUNT=$("$P/bin/head" -n1 "$SNAPSHOT_READY")
    printf 'SNAPSHOT_CREATED=NO_REUSE_EXISTING\n'
    printf 'SNAPSHOT_DOCUMENT_COUNT=%s\n' "$SNAPSHOT_COUNT"
fi

"$P/bin/printf" '%s' "$SNAPSHOT" > "$RAW_DIR_MEMORY" || exit 31
[ -f "$SURVEY_MEMORY" ] || : > "$SURVEY_MEMORY"

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 32
[ -s "$BC.partial" ] || exit 33
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 34
"$P/bin/chmod" 0400 "$BC" || exit 35

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

START_COMMITTED=$("$P/bin/grep" -c ' || COMMIT=YES$' "$SURVEY_MEMORY" 2>/dev/null || true)
printf 'COMMITTED_AT_START=%s\n' "$START_COMMITTED"

BATCH_LIMIT=5
CYCLE=1
COMPLETE=0

printf 'BATCH_LIMIT=%s\n' "$BATCH_LIMIT"

while [ "$CYCLE" -le "$BATCH_LIMIT" ]; do
    RUNLOG="$LOG/cycle_$CYCLE.log"

    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?

    printf '\n=== V25B_CYCLE_%s ===\n' "$CYCLE"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"

    if [ "$RC" -ne 0 ]; then
        printf 'V25B_2_FULL_CORPUS_SURVEY=FAIL\n'
        printf 'FAILURE_CYCLE=%s\n' "$CYCLE"
        printf 'NEXT_ACTION=INSPECT_FAILED_VM_CYCLE_AND_PRESERVE_SURVEY_STATE\n'
        exit 50
    fi

    if "$P/bin/grep" -F 'SURVEY_COMPLETE YES' "$RUNLOG" >/dev/null 2>&1; then
        COMPLETE=1
        break
    fi

    CYCLE=$((CYCLE + 1))
done

FINAL_COMMITTED=$("$P/bin/grep" -c ' || COMMIT=YES$' "$SURVEY_MEMORY" 2>/dev/null || true)
printf '\n=== V25B_FINAL_STATE ===\n'
printf 'SNAPSHOT_DOCUMENT_COUNT=%s\n' "$SNAPSHOT_COUNT"
printf 'COMMITTED_SURVEY_COUNT=%s\n' "$FINAL_COMMITTED"
printf 'SURVEY_COMPLETE_SENTINEL=%s\n' "$COMPLETE"
printf 'PRODUCTION_RAW_MUTATED=NO\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'

if [ "$COMPLETE" -eq 1 ] && [ "$FINAL_COMMITTED" -eq "$SNAPSHOT_COUNT" ]; then
    printf 'V25B_2_FULL_CORPUS_SURVEY=PASS\n'
    printf 'NEXT_ACTION=BUILD_V26_BOUNDED_SEGMENT_CURSOR_PREFLIGHT\n'
    exit 0
fi

printf 'V25B_2_FULL_CORPUS_SURVEY=BATCH_COMPLETE\n'
printf 'NEXT_ACTION=RERUN_SAME_RUNNER_TO_RESUME_NEXT_BATCH\n'
exit 0
