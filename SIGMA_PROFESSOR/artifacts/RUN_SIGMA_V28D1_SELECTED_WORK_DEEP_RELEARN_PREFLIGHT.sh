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

BRIDGE_SRC="$E/SIGMA_REAL_SURVEY_CURRICULUM_BRIDGE_V2_8R1.sigma"
BRIDGE_BC="$E/SIGMA_REAL_SURVEY_CURRICULUM_BRIDGE_V2_8R1.sigmab"
EXPECTED_BRIDGE_SOURCE=8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8
EXPECTED_BRIDGE_BYTECODE=0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5

SRC="$E/SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigma"
BC="$E/SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigmab"
EXPECTED_SOURCE=3dfc25c5f6e9cdbabd193bb7c3d8845ba025cb12e1b3824430a1a6ec280ec74f

V25_STATE="$HOME_SIGMA/SIGMA_V25_FULL_CORPUS_SURVEY"
SNAPSHOT="$V25_STATE/corpus_snapshot"
REAL_SURVEY="$E/SIGMA_V25B2_DOCUMENT_SURVEY.memory"

BRIDGE_SURVEY_PATH="$E/SIGMA_V28R1_SURVEY_PATH.memory"
BRIDGE_STATE="$E/SIGMA_V28R1_CURRICULUM_STATE.memory"
BRIDGE_SELECTED="$E/SIGMA_V28R1_SELECTED_WORK.memory"

SNAPSHOT_DIR_MEMORY="$E/SIGMA_V28D1_SNAPSHOT_DIR.memory"
ACTIVE_WORK="$E/SIGMA_V28D1_ACTIVE_WORK.memory"
CURSOR="$E/SIGMA_V28D1_CURSOR.memory"
EVIDENCE="$E/SIGMA_V28D1_DEEP_EVIDENCE.memory"

STATE="$HOME_SIGMA/SIGMA_V28D1_SELECTED_WORK_DEEP_RELEARN_PREFLIGHT"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"

EXPECTED_SELECTED=0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b
EXPECTED_SELECTED_LINE_TOTAL=10

mkdir -p "$STATE" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V28D1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_bridge_source=$("$P/bin/sha256sum" "$BRIDGE_SRC" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V28D1_SELECTED_WORK_TO_DEEP_RELEARN_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_CURRICULUM_PRIORITY=NO\n'
printf 'REAL_CURRICULUM_SELECTION=YES\n'
printf 'REAL_SNAPSHOT_DOCUMENT=YES\n'
printf 'FRESH_VM_PROCESS_REUSE_TEST=YES\n'
printf 'DETERMINISTIC_REPLAY_TEST=YES\n'
printf 'NEGATIVE_EMPTY_SELECTION_TEST=YES\n'
printf 'EVIDENCE_STATE_BOUNDEDNESS_TEST=YES\n'
printf 'FILE_EXISTS_LOCKED_VM_RUNTIME_PROOF_REQUIRED=YES\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'BRIDGE_SOURCE_SHA256=%s\n' "$actual_bridge_source"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || exit 21
[ "$actual_vm" = "$EXPECTED_VM" ] || exit 22
[ "$actual_bridge_source" = "$EXPECTED_BRIDGE_SOURCE" ] || exit 23
[ "$actual_source" = "$EXPECTED_SOURCE" ] || exit 24
[ -f "$REAL_SURVEY" ] || exit 25
[ -d "$SNAPSHOT" ] || exit 26

REAL_SURVEY_SHA_BEFORE=$("$P/bin/sha256sum" "$REAL_SURVEY" | "$P/bin/awk" '{print $1}')

"$P/bin/rm" -f -- "$BRIDGE_BC.partial"
"$SIGMAC" "$BRIDGE_SRC" "$BRIDGE_BC.partial"
BRC=$?
printf 'BRIDGE_SIGMAC_RC=%s\n' "$BRC"
[ "$BRC" -eq 0 ] || exit 27
BRIDGE_BC_SHA=$("$P/bin/sha256sum" "$BRIDGE_BC.partial" | "$P/bin/awk" '{print $1}')
printf 'BRIDGE_BYTECODE_SHA256=%s\n' "$BRIDGE_BC_SHA"
[ "$BRIDGE_BC_SHA" = "$EXPECTED_BRIDGE_BYTECODE" ] || exit 28
"$P/bin/mv" -f -- "$BRIDGE_BC.partial" "$BRIDGE_BC"
"$P/bin/chmod" 0400 "$BRIDGE_BC"

"$P/bin/printf" '%s' "$REAL_SURVEY" > "$BRIDGE_SURVEY_PATH"
: > "$BRIDGE_STATE"
: > "$BRIDGE_SELECTED"

(
    cd "$BRAIN" || exit 40
    "$VM" "$BRIDGE_BC"
) > "$LOG/bridge_real_selection.log" 2>&1
BRVM=$?

printf '\n=== REAL_NATIVE_CURRICULUM_SELECTION ===\n'
printf 'VM_RC=%s\n' "$BRVM"
"$P/bin/cat" "$LOG/bridge_real_selection.log"
[ "$BRVM" -eq 0 ] || exit 50

SELECTED=$("$P/bin/cat" "$BRIDGE_SELECTED")
printf 'NATIVE_SELECTED_WORK=%s\n' "$SELECTED"
[ "$SELECTED" = "$EXPECTED_SELECTED" ] || {
    printf 'V28D1_PREFLIGHT=FAIL\n'
    printf 'FAILURE=UNEXPECTED_REAL_CURRICULUM_SELECTION\n'
    exit 51
}

SELECTED_DOC="$SNAPSHOT/$SELECTED.document"
[ -f "$SELECTED_DOC" ] || exit 52
SELECTED_DOC_SHA_BEFORE=$("$P/bin/sha256sum" "$SELECTED_DOC" | "$P/bin/awk" '{print $1}')
printf 'SELECTED_DOCUMENT_SHA256_BEFORE=%s\n' "$SELECTED_DOC_SHA_BEFORE"

"$P/bin/printf" '%s' "$SNAPSHOT" > "$SNAPSHOT_DIR_MEMORY"

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'DEEP_SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 53
[ -s "$BC.partial" ] || exit 54
"$P/bin/mv" -f -- "$BC.partial" "$BC"
"$P/bin/chmod" 0400 "$BC"
BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'DEEP_BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

run_deep() {
    CASE_NAME="$1"
    RUNLOG="$LOG/$CASE_NAME.log"

    (
        cd "$BRAIN" || exit 60
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?

    printf '\n=== %s ===\n' "$CASE_NAME"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"
    return "$RC"
}

: > "$ACTIVE_WORK"
: > "$CURSOR"
: > "$EVIDENCE"

run_deep REAL_SELECTED_SEGMENT0
RC=$?
[ "$RC" -eq 0 ] || exit 61
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null && exit 62
"$P/bin/grep" -F 'DOCUMENT_EXISTS 1' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null || exit 63
"$P/bin/grep" -F 'WORK_SWITCHED 1' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null || exit 64
"$P/bin/grep" -F 'LINE_TOTAL 10' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null || exit 65
"$P/bin/grep" -F 'SEGMENT_INDEX 0' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null || exit 66
"$P/bin/grep" -F 'SEGMENT_START_LINE 0' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null || exit 67
"$P/bin/grep" -F 'SEGMENT_END_LINE 8' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null || exit 68
"$P/bin/grep" -F 'EVIDENCE_READY 1' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null || exit 69
"$P/bin/grep" -F 'CURSOR_APPEND_RC 0' "$LOG/REAL_SELECTED_SEGMENT0.log" >/dev/null || exit 70
CURSOR1=$("$P/bin/wc" -c < "$CURSOR" | "$P/bin/tr" -d ' ')
[ "$CURSOR1" -eq 1 ] || exit 71

run_deep REAL_SELECTED_SEGMENT1_FRESH_VM
RC=$?
[ "$RC" -eq 0 ] || exit 72
"$P/bin/grep" -F 'WORK_SWITCHED 0' "$LOG/REAL_SELECTED_SEGMENT1_FRESH_VM.log" >/dev/null || exit 73
"$P/bin/grep" -F 'SEGMENT_INDEX 1' "$LOG/REAL_SELECTED_SEGMENT1_FRESH_VM.log" >/dev/null || exit 74
"$P/bin/grep" -F 'SEGMENT_START_LINE 8' "$LOG/REAL_SELECTED_SEGMENT1_FRESH_VM.log" >/dev/null || exit 75
"$P/bin/grep" -F 'SEGMENT_END_LINE 10' "$LOG/REAL_SELECTED_SEGMENT1_FRESH_VM.log" >/dev/null || exit 76
"$P/bin/grep" -F 'CURSOR_APPEND_RC 0' "$LOG/REAL_SELECTED_SEGMENT1_FRESH_VM.log" >/dev/null || exit 77
CURSOR2=$("$P/bin/wc" -c < "$CURSOR" | "$P/bin/tr" -d ' ')
[ "$CURSOR2" -eq 2 ] || exit 78

run_deep REAL_SELECTED_COMPLETE_FRESH_VM
RC=$?
[ "$RC" -eq 0 ] || exit 79
"$P/bin/grep" -F 'DEEP_RELEARN_COMPLETE YES' "$LOG/REAL_SELECTED_COMPLETE_FRESH_VM.log" >/dev/null || exit 80
"$P/bin/grep" -F 'SEGMENT_INDEX 2' "$LOG/REAL_SELECTED_COMPLETE_FRESH_VM.log" >/dev/null || exit 81

EVIDENCE_COMMITTED=$("$P/bin/grep" -c ' || COMMIT=YES$' "$EVIDENCE" 2>/dev/null || true)
printf 'DEEP_EVIDENCE_COMMITTED_RECORDS=%s\n' "$EVIDENCE_COMMITTED"
[ "$EVIDENCE_COMMITTED" -eq 2 ] || exit 82

FIRST_EVIDENCE_SHA=$("$P/bin/sha256sum" "$EVIDENCE" | "$P/bin/awk" '{print $1}')
printf 'DEEP_EVIDENCE_SHA256=%s\n' "$FIRST_EVIDENCE_SHA"

: > "$ACTIVE_WORK"
: > "$CURSOR"
: > "$EVIDENCE"

run_deep DEEP_REPLAY_SEGMENT0
RC=$?
[ "$RC" -eq 0 ] || exit 83
run_deep DEEP_REPLAY_SEGMENT1
RC=$?
[ "$RC" -eq 0 ] || exit 84
run_deep DEEP_REPLAY_COMPLETE
RC=$?
[ "$RC" -eq 0 ] || exit 85

REPLAY_EVIDENCE_SHA=$("$P/bin/sha256sum" "$EVIDENCE" | "$P/bin/awk" '{print $1}')
printf 'DEEP_REPLAY_EVIDENCE_SHA256=%s\n' "$REPLAY_EVIDENCE_SHA"
[ "$REPLAY_EVIDENCE_SHA" = "$FIRST_EVIDENCE_SHA" ] || exit 86

"$P/bin/printf" 'ACTIVE_SENTINEL' > "$ACTIVE_WORK"
"$P/bin/printf" 'CURSOR_SENTINEL' > "$CURSOR"
"$P/bin/printf" 'EVIDENCE_SENTINEL' > "$EVIDENCE"
ACTIVE_NEG_SHA=$("$P/bin/sha256sum" "$ACTIVE_WORK" | "$P/bin/awk" '{print $1}')
CURSOR_NEG_SHA=$("$P/bin/sha256sum" "$CURSOR" | "$P/bin/awk" '{print $1}')
EVIDENCE_NEG_SHA=$("$P/bin/sha256sum" "$EVIDENCE" | "$P/bin/awk" '{print $1}')
: > "$BRIDGE_SELECTED"

run_deep NEGATIVE_EMPTY_SELECTION
RC=$?
[ "$RC" -eq 0 ] || exit 87
"$P/bin/grep" -F 'SELECTED_WORK_VALID 0' "$LOG/NEGATIVE_EMPTY_SELECTION.log" >/dev/null || exit 88
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/NEGATIVE_EMPTY_SELECTION.log" >/dev/null || exit 89
[ "$("$P/bin/sha256sum" "$ACTIVE_WORK" | "$P/bin/awk" '{print $1}')" = "$ACTIVE_NEG_SHA" ] || exit 90
[ "$("$P/bin/sha256sum" "$CURSOR" | "$P/bin/awk" '{print $1}')" = "$CURSOR_NEG_SHA" ] || exit 91
[ "$("$P/bin/sha256sum" "$EVIDENCE" | "$P/bin/awk" '{print $1}')" = "$EVIDENCE_NEG_SHA" ] || exit 92

"$P/bin/printf" '%s' "$EXPECTED_SELECTED" > "$BRIDGE_SELECTED"
: > "$EVIDENCE"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'WORK=X%s || CURSOR= || BEST_LOCAL_RELATION=a => b || COMMIT=YES\n' "$I" >> "$EVIDENCE"
    I=$((I + 1))
done
"$P/bin/printf" 'ACTIVE_SENTINEL2' > "$ACTIVE_WORK"
"$P/bin/printf" 'CURSOR_SENTINEL2' > "$CURSOR"
ACTIVE_LIMIT_SHA=$("$P/bin/sha256sum" "$ACTIVE_WORK" | "$P/bin/awk" '{print $1}')
CURSOR_LIMIT_SHA=$("$P/bin/sha256sum" "$CURSOR" | "$P/bin/awk" '{print $1}')
EVIDENCE_LIMIT_SHA=$("$P/bin/sha256sum" "$EVIDENCE" | "$P/bin/awk" '{print $1}')

run_deep EVIDENCE_LIMIT_REFUSAL
RC=$?
[ "$RC" -eq 0 ] || exit 93
"$P/bin/grep" -F 'EVIDENCE_LIMIT_EXCEEDED 1' "$LOG/EVIDENCE_LIMIT_REFUSAL.log" >/dev/null || exit 94
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/EVIDENCE_LIMIT_REFUSAL.log" >/dev/null || exit 95
[ "$("$P/bin/sha256sum" "$ACTIVE_WORK" | "$P/bin/awk" '{print $1}')" = "$ACTIVE_LIMIT_SHA" ] || exit 96
[ "$("$P/bin/sha256sum" "$CURSOR" | "$P/bin/awk" '{print $1}')" = "$CURSOR_LIMIT_SHA" ] || exit 97
[ "$("$P/bin/sha256sum" "$EVIDENCE" | "$P/bin/awk" '{print $1}')" = "$EVIDENCE_LIMIT_SHA" ] || exit 98

"$P/bin/printf" '%s' "$EXPECTED_SELECTED" > "$BRIDGE_SELECTED"
SELECTED_DOC_SHA_AFTER=$("$P/bin/sha256sum" "$SELECTED_DOC" | "$P/bin/awk" '{print $1}')
REAL_SURVEY_SHA_AFTER=$("$P/bin/sha256sum" "$REAL_SURVEY" | "$P/bin/awk" '{print $1}')
printf 'SELECTED_DOCUMENT_SHA256_AFTER=%s\n' "$SELECTED_DOC_SHA_AFTER"
printf 'REAL_SURVEY_SHA256_AFTER=%s\n' "$REAL_SURVEY_SHA_AFTER"
[ "$SELECTED_DOC_SHA_AFTER" = "$SELECTED_DOC_SHA_BEFORE" ] || exit 99
[ "$REAL_SURVEY_SHA_AFTER" = "$REAL_SURVEY_SHA_BEFORE" ] || exit 100

printf '\nV28D1_SELECTED_WORK_TO_DEEP_RELEARN_PREFLIGHT=PASS\n'
printf 'REAL_NATIVE_CURRICULUM_SELECTED_DOCUMENT=PASS\n'
printf 'NATIVE_SELECTED_WORK_DOCUMENT_RESOLUTION=PASS\n'
printf 'FILE_EXISTS_LOCKED_VM_RUNTIME=PASS\n'
printf 'NATIVE_REAL_SELECTED_WORK_SEGMENT_RELEARN=PROVEN_IN_SELECTED_DOCUMENT_SCOPE\n'
printf 'PERSISTED_CURSOR_INFLUENCES_LATER_FRESH_VM=PASS\n'
printf 'DETERMINISTIC_DEEP_EVIDENCE_REPLAY=PASS\n'
printf 'DEEP_EVIDENCE_PROVENANCE_PERSISTENCE=PASS\n'
printf 'NEGATIVE_EMPTY_SELECTION=PASS\n'
printf 'EVIDENCE_STATE_STEP_LIMIT_STATUS=BOUNDED\n'
printf 'REAL_SURVEY_MUTATED=NO\n'
printf 'SELECTED_DOCUMENT_MUTATED=NO\n'
printf 'HOST_CURRICULUM_PRIORITY=NO\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'SEMANTIC_IMPORTANCE=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'NEXT_ACTION=BUILD_DEEP_RELEARN_COMPLETION_TO_REVALIDATION_PREFLIGHT\n'
