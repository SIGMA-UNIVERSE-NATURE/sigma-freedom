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

SRC="$E/SIGMA_REAL_SURVEY_CURRICULUM_BRIDGE_V2_8R1.sigma"
BC="$E/SIGMA_REAL_SURVEY_CURRICULUM_BRIDGE_V2_8R1.sigmab"
EXPECTED_SOURCE=8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8

REAL_SURVEY="$E/SIGMA_V25B2_DOCUMENT_SURVEY.memory"

STATE="$HOME_SIGMA/SIGMA_V28R1_REAL_SURVEY_CURRICULUM_BRIDGE_PREFLIGHT"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"
OVER_LIMIT_SURVEY="$STATE/over_limit_survey.memory"

SURVEY_PATH_MEMORY="$E/SIGMA_V28R1_SURVEY_PATH.memory"
CURRICULUM_STATE="$E/SIGMA_V28R1_CURRICULUM_STATE.memory"
SELECTED_WORK="$E/SIGMA_V28R1_SELECTED_WORK.memory"

mkdir -p "$STATE" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V28R1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V28R1_REAL_SURVEY_CURRICULUM_BRIDGE_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_WORK_PROFILE_GENERATION=NO\n'
printf 'HOST_CURRICULUM_PRIORITY=NO\n'
printf 'HOST_LESSON_SELECTION=NO\n'
printf 'REAL_SURVEY_INPUT=YES\n'
printf 'PERSISTENT_STATE_TEST=YES\n'
printf 'FRESH_VM_PROCESS_REUSE_TEST=YES\n'
printf 'REPLAY_TEST=YES\n'
printf 'PARTIAL_STATE_FILTER_TEST=YES\n'
printf 'STEP_LIMIT_BOUNDEDNESS_TEST=YES\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || exit 21
[ "$actual_vm" = "$EXPECTED_VM" ] || exit 22
[ "$actual_source" = "$EXPECTED_SOURCE" ] || exit 23
[ -f "$REAL_SURVEY" ] || {
    printf 'HOLD=MISSING_REAL_V25B2_SURVEY path=%s\n' "$REAL_SURVEY"
    exit 24
}

REAL_SURVEY_SHA_BEFORE=$("$P/bin/sha256sum" "$REAL_SURVEY" | "$P/bin/awk" '{print $1}')
REAL_SURVEY_COMMIT_LINES=$("$P/bin/grep" -c ' || COMMIT=YES$' "$REAL_SURVEY" 2>/dev/null || true)
printf 'REAL_SURVEY_SHA256_BEFORE=%s\n' "$REAL_SURVEY_SHA_BEFORE"
printf 'REAL_SURVEY_COMMIT_LINES_MECHANICAL=%s\n' "$REAL_SURVEY_COMMIT_LINES"

[ "$REAL_SURVEY_COMMIT_LINES" -eq 56 ] || {
    printf 'HOLD=REAL_SURVEY_COMMIT_COUNT_NOT_56\n'
    exit 25
}

"$P/bin/printf" '%s' "$REAL_SURVEY" > "$SURVEY_PATH_MEMORY" || exit 26

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 27
[ -s "$BC.partial" ] || exit 28
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 29
"$P/bin/chmod" 0400 "$BC" || exit 30

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

run_vm() {
    CASE_NAME="$1"
    RUNLOG="$LOG/$CASE_NAME.log"

    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?

    printf '\n=== %s ===\n' "$CASE_NAME"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"
    return "$RC"
}

extract_selected() {
    RUNLOG="$1"
    "$P/bin/grep" '^SELECTED_WORK ' "$RUNLOG" | "$P/bin/head" -n1 | "$P/bin/sed" 's/^SELECTED_WORK //'
}

: > "$CURRICULUM_STATE"
: > "$SELECTED_WORK"

run_vm REAL_SURVEY_PHASE1
RC=$?
[ "$RC" -eq 0 ] || exit 50
"$P/bin/grep" -F 'REAL_SURVEY_COMMITTED_DOC_COUNT 56' "$LOG/REAL_SURVEY_PHASE1.log" >/dev/null || exit 51
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED YES' "$LOG/REAL_SURVEY_PHASE1.log" >/dev/null || exit 52
"$P/bin/grep" -F 'DISPATCH_APPEND_RC 0' "$LOG/REAL_SURVEY_PHASE1.log" >/dev/null || exit 53
SEL1=$(extract_selected "$LOG/REAL_SURVEY_PHASE1.log")
[ -n "$SEL1" ] || exit 54

PHASE1_STATE_SHA=$("$P/bin/sha256sum" "$CURRICULUM_STATE" | "$P/bin/awk" '{print $1}')
PHASE1_SELECTED_SHA=$("$P/bin/sha256sum" "$SELECTED_WORK" | "$P/bin/awk" '{print $1}')
printf 'REAL_PHASE1_SELECTED_WORK=%s\n' "$SEL1"
printf 'REAL_PHASE1_STATE_SHA256=%s\n' "$PHASE1_STATE_SHA"
printf 'REAL_PHASE1_SELECTED_SHA256=%s\n' "$PHASE1_SELECTED_SHA"

run_vm REAL_SURVEY_PHASE2_FRESH_VM
RC=$?
[ "$RC" -eq 0 ] || exit 55
"$P/bin/grep" -F 'REAL_SURVEY_COMMITTED_DOC_COUNT 56' "$LOG/REAL_SURVEY_PHASE2_FRESH_VM.log" >/dev/null || exit 56
"$P/bin/grep" -F 'PERSISTED_DISPATCH_COUNT 1' "$LOG/REAL_SURVEY_PHASE2_FRESH_VM.log" >/dev/null || exit 57
SEL2=$(extract_selected "$LOG/REAL_SURVEY_PHASE2_FRESH_VM.log")
[ -n "$SEL2" ] || exit 58
[ "$SEL2" != "$SEL1" ] || exit 59
printf 'REAL_PHASE2_SELECTED_WORK=%s\n' "$SEL2"

: > "$CURRICULUM_STATE"
: > "$SELECTED_WORK"
run_vm REAL_SURVEY_PHASE1_REPLAY
RC=$?
[ "$RC" -eq 0 ] || exit 60
SEL_REPLAY=$(extract_selected "$LOG/REAL_SURVEY_PHASE1_REPLAY.log")
[ "$SEL_REPLAY" = "$SEL1" ] || exit 61

REPLAY_STATE_SHA=$("$P/bin/sha256sum" "$CURRICULUM_STATE" | "$P/bin/awk" '{print $1}')
REPLAY_SELECTED_SHA=$("$P/bin/sha256sum" "$SELECTED_WORK" | "$P/bin/awk" '{print $1}')
[ "$REPLAY_STATE_SHA" = "$PHASE1_STATE_SHA" ] || exit 62
[ "$REPLAY_SELECTED_SHA" = "$PHASE1_SELECTED_SHA" ] || exit 63
printf 'REAL_REPLAY_STATE_SHA256=%s\n' "$REPLAY_STATE_SHA"
printf 'REAL_REPLAY_SELECTED_SHA256=%s\n' "$REPLAY_SELECTED_SHA"

"$P/bin/printf" 'WORK=%s || DISPATCHED=YES' "$SEL1" > "$CURRICULUM_STATE"
: > "$SELECTED_WORK"
run_vm PARTIAL_STATE_FILTER
RC=$?
[ "$RC" -eq 0 ] || exit 64
"$P/bin/grep" -F 'IGNORED_STATE_RECORD_COUNT 1' "$LOG/PARTIAL_STATE_FILTER.log" >/dev/null || exit 65
SEL_PARTIAL=$(extract_selected "$LOG/PARTIAL_STATE_FILTER.log")
[ "$SEL_PARTIAL" = "$SEL1" ] || exit 66

: > "$CURRICULUM_STATE"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'WORK=S%s || DISPATCHED=YES || COMMIT=YES\n' "$I" >> "$CURRICULUM_STATE"
    I=$((I + 1))
done
"$P/bin/printf" 'SENTINEL' > "$SELECTED_WORK"
SELECTED_SENTINEL_SHA=$("$P/bin/sha256sum" "$SELECTED_WORK" | "$P/bin/awk" '{print $1}')

run_vm STATE_LIMIT_REFUSAL
RC=$?
[ "$RC" -eq 0 ] || exit 67
"$P/bin/grep" -F 'STATE_LIMIT_EXCEEDED 1' "$LOG/STATE_LIMIT_REFUSAL.log" >/dev/null || exit 68
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/STATE_LIMIT_REFUSAL.log" >/dev/null || exit 69
SELECTED_AFTER_STATE_LIMIT_SHA=$("$P/bin/sha256sum" "$SELECTED_WORK" | "$P/bin/awk" '{print $1}')
[ "$SELECTED_AFTER_STATE_LIMIT_SHA" = "$SELECTED_SENTINEL_SHA" ] || exit 70

: > "$OVER_LIMIT_SURVEY"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'DOC=T%s || SURVEY_STATUS=COMPLETE || BEST_LOCAL_RELATION=a => b || COMMIT=YES\n' "$I" >> "$OVER_LIMIT_SURVEY"
    I=$((I + 1))
done

"$P/bin/printf" '%s' "$OVER_LIMIT_SURVEY" > "$SURVEY_PATH_MEMORY"
: > "$CURRICULUM_STATE"
"$P/bin/printf" 'SENTINEL' > "$SELECTED_WORK"
SELECTED_SENTINEL_SHA2=$("$P/bin/sha256sum" "$SELECTED_WORK" | "$P/bin/awk" '{print $1}')

run_vm SURVEY_LIMIT_REFUSAL
RC=$?
[ "$RC" -eq 0 ] || exit 71
"$P/bin/grep" -F 'SURVEY_LIMIT_EXCEEDED 1' "$LOG/SURVEY_LIMIT_REFUSAL.log" >/dev/null || exit 72
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/SURVEY_LIMIT_REFUSAL.log" >/dev/null || exit 73
SELECTED_AFTER_SURVEY_LIMIT_SHA=$("$P/bin/sha256sum" "$SELECTED_WORK" | "$P/bin/awk" '{print $1}')
[ "$SELECTED_AFTER_SURVEY_LIMIT_SHA" = "$SELECTED_SENTINEL_SHA2" ] || exit 74

"$P/bin/printf" '%s' "$REAL_SURVEY" > "$SURVEY_PATH_MEMORY"
REAL_SURVEY_SHA_AFTER=$("$P/bin/sha256sum" "$REAL_SURVEY" | "$P/bin/awk" '{print $1}')
printf 'REAL_SURVEY_SHA256_AFTER=%s\n' "$REAL_SURVEY_SHA_AFTER"
[ "$REAL_SURVEY_SHA_AFTER" = "$REAL_SURVEY_SHA_BEFORE" ] || exit 75

printf '\nV28R1_REAL_SURVEY_CURRICULUM_BRIDGE_PREFLIGHT=PASS\n'
printf 'REAL_SURVEY_56_DOCUMENT_INPUT=PASS\n'
printf 'NATIVE_REAL_SURVEY_STRUCTURAL_FRONTIER=PROVEN_IN_FROZEN_SNAPSHOT_SCOPE\n'
printf 'PERSISTENT_DISPATCH_STATE_INFLUENCES_LATER_FRESH_VM=PASS\n'
printf 'DETERMINISTIC_REAL_SURVEY_REPLAY=PASS\n'
printf 'PARTIAL_STATE_COMMIT_FILTER=PASS\n'
printf 'STEP_LIMIT_STATUS=BOUNDED\n'
printf 'REAL_SURVEY_MUTATED=NO\n'
printf 'HOST_WORK_PROFILE_GENERATION=NO\n'
printf 'HOST_CURRICULUM_PRIORITY=NO\n'
printf 'HOST_LESSON_SELECTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'STRUCTURAL_FRONTIER_ONLY=YES\n'
printf 'SEMANTIC_IMPORTANCE=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'NEXT_ACTION=BUILD_SELECTED_WORK_TO_DEEP_RELEARN_SEGMENT_CURSOR_PREFLIGHT\n'