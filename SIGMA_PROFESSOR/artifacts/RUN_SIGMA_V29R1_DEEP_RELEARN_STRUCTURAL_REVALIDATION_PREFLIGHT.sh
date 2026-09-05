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

DEEP_SRC="$E/SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigma"
DEEP_BC="$E/SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigmab"
EXPECTED_DEEP_SOURCE=3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce
EXPECTED_DEEP_BYTECODE=e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff

SRC="$E/SIGMA_DEEP_RELEARN_STRUCTURAL_REVALIDATION_V2_9R1.sigma"
BC="$E/SIGMA_DEEP_RELEARN_STRUCTURAL_REVALIDATION_V2_9R1.sigmab"
EXPECTED_SOURCE=94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b

V25_STATE="$HOME_SIGMA/SIGMA_V25_FULL_CORPUS_SURVEY"
SNAPSHOT="$V25_STATE/corpus_snapshot"
REAL_SURVEY="$E/SIGMA_V25B2_DOCUMENT_SURVEY.memory"

BRIDGE_SURVEY_PATH="$E/SIGMA_V28R1_SURVEY_PATH.memory"
BRIDGE_STATE="$E/SIGMA_V28R1_CURRICULUM_STATE.memory"
BRIDGE_SELECTED="$E/SIGMA_V28R1_SELECTED_WORK.memory"

D1_SNAPSHOT_DIR="$E/SIGMA_V28D1_SNAPSHOT_DIR.memory"
D1_ACTIVE_WORK="$E/SIGMA_V28D1_ACTIVE_WORK.memory"
D1_CURSOR="$E/SIGMA_V28D1_CURSOR.memory"
D1_EVIDENCE="$E/SIGMA_V28D1_DEEP_EVIDENCE.memory"

V29_SELECTED="$E/SIGMA_V29R1_SELECTED_WORK.memory"
V29_SURVEY_PATH="$E/SIGMA_V29R1_SURVEY_PATH.memory"
V29_EVIDENCE_PATH="$E/SIGMA_V29R1_EVIDENCE_PATH.memory"
V29_SNAPSHOT_DIR="$E/SIGMA_V29R1_SNAPSHOT_DIR.memory"
V29_ACTIVE_WORK_PATH="$E/SIGMA_V29R1_ACTIVE_WORK_PATH.memory"
V29_CURSOR_PATH="$E/SIGMA_V29R1_CURSOR_PATH.memory"
V29_STATE="$E/SIGMA_V29R1_REVALIDATION_STATE.memory"

STATE="$HOME_SIGMA/SIGMA_V29R1_STRUCTURAL_REVALIDATION_PREFLIGHT"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"

SYNTH_DIR="$STATE/synth_snapshot"
SYNTH_SURVEY="$STATE/synth_survey.memory"
SYNTH_EVIDENCE="$STATE/synth_evidence.memory"
SYNTH_ACTIVE="$STATE/synth_active.memory"
SYNTH_CURSOR="$STATE/synth_cursor.memory"
OVER_SURVEY="$STATE/over_survey.memory"
OVER_EVIDENCE="$STATE/over_evidence.memory"

EXPECTED_SELECTED=0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b
EXPECTED_REAL_BASELINE='in => the'

mkdir -p "$STATE" "$LOG" "$SYNTH_DIR"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V29R1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_bridge_source=$("$P/bin/sha256sum" "$BRIDGE_SRC" | "$P/bin/awk" '{print $1}')
actual_deep_source=$("$P/bin/sha256sum" "$DEEP_SRC" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V29R1_DEEP_RELEARN_TO_STRUCTURAL_REVALIDATION_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_REVALIDATION_DECISION=NO\n'
printf 'HOST_TRUTH_DECISION=NO\n'
printf 'REAL_SURVEY_INPUT=YES\n'
printf 'REAL_DEEP_EVIDENCE_REGENERATION=YES\n'
printf 'FRESH_VM_STATE_REUSE_TEST=YES\n'
printf 'NEGATIVE_COUNTEREXAMPLE_TEST=YES\n'
printf 'INCOMPLETE_DEEP_RELEARN_TEST=YES\n'
printf 'PARTIAL_EVIDENCE_FILTER_TEST=YES\n'
printf 'STEP_LIMIT_BOUNDEDNESS_TEST=YES\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'BRIDGE_SOURCE_SHA256=%s\n' "$actual_bridge_source"
printf 'DEEP_SOURCE_SHA256=%s\n' "$actual_deep_source"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || exit 21
[ "$actual_vm" = "$EXPECTED_VM" ] || exit 22
[ "$actual_bridge_source" = "$EXPECTED_BRIDGE_SOURCE" ] || exit 23
[ "$actual_deep_source" = "$EXPECTED_DEEP_SOURCE" ] || exit 24
[ "$actual_source" = "$EXPECTED_SOURCE" ] || exit 25
[ -f "$REAL_SURVEY" ] || exit 26
[ -d "$SNAPSHOT" ] || exit 27

REAL_SURVEY_SHA_BEFORE=$("$P/bin/sha256sum" "$REAL_SURVEY" | "$P/bin/awk" '{print $1}')

if [ -f "$D1_EVIDENCE" ]; then
    "$P/bin/cp" -- "$D1_EVIDENCE" "$STATE/v28d1_terminal_evidence_state.reference"
    "$P/bin/sha256sum" "$STATE/v28d1_terminal_evidence_state.reference" > "$STATE/v28d1_terminal_evidence_state.reference.sha256"
fi
if [ -f "$D1_CURSOR" ]; then
    "$P/bin/cp" -- "$D1_CURSOR" "$STATE/v28d1_terminal_cursor_state.reference"
fi
if [ -f "$D1_ACTIVE_WORK" ]; then
    "$P/bin/cp" -- "$D1_ACTIVE_WORK" "$STATE/v28d1_terminal_active_work_state.reference"
fi
printf 'V28D1_TERMINAL_QA_STATE_PRESERVED=YES\n'

"$P/bin/rm" -f -- "$BRIDGE_BC.partial"
"$SIGMAC" "$BRIDGE_SRC" "$BRIDGE_BC.partial"
BRC=$?
printf 'BRIDGE_SIGMAC_RC=%s\n' "$BRC"
[ "$BRC" -eq 0 ] || exit 28
BRIDGE_BC_SHA=$("$P/bin/sha256sum" "$BRIDGE_BC.partial" | "$P/bin/awk" '{print $1}')
printf 'BRIDGE_BYTECODE_SHA256=%s\n' "$BRIDGE_BC_SHA"
[ "$BRIDGE_BC_SHA" = "$EXPECTED_BRIDGE_BYTECODE" ] || exit 29
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
[ "$SELECTED" = "$EXPECTED_SELECTED" ] || exit 51

REAL_DOC="$SNAPSHOT/$SELECTED.document"
[ -f "$REAL_DOC" ] || exit 52
REAL_DOC_SHA_BEFORE=$("$P/bin/sha256sum" "$REAL_DOC" | "$P/bin/awk" '{print $1}')

"$P/bin/rm" -f -- "$DEEP_BC.partial"
"$SIGMAC" "$DEEP_SRC" "$DEEP_BC.partial"
DRC=$?
printf 'DEEP_SIGMAC_RC=%s\n' "$DRC"
[ "$DRC" -eq 0 ] || exit 53
DEEP_BC_SHA=$("$P/bin/sha256sum" "$DEEP_BC.partial" | "$P/bin/awk" '{print $1}')
printf 'DEEP_BYTECODE_SHA256=%s\n' "$DEEP_BC_SHA"
[ "$DEEP_BC_SHA" = "$EXPECTED_DEEP_BYTECODE" ] || exit 54
"$P/bin/mv" -f -- "$DEEP_BC.partial" "$DEEP_BC"
"$P/bin/chmod" 0400 "$DEEP_BC"

"$P/bin/printf" '%s' "$SNAPSHOT" > "$D1_SNAPSHOT_DIR"
: > "$D1_ACTIVE_WORK"
: > "$D1_CURSOR"
: > "$D1_EVIDENCE"

run_d1() {
    CASE_NAME="$1"
    RUNLOG="$LOG/$CASE_NAME.log"
    (
        cd "$BRAIN" || exit 60
        "$VM" "$DEEP_BC"
    ) >"$RUNLOG" 2>&1
    RC=$?
    printf '\n=== %s ===\n' "$CASE_NAME"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"
    return "$RC"
}

run_d1 REGENERATE_REAL_SEGMENT0
RC=$?
[ "$RC" -eq 0 ] || exit 61
"$P/bin/grep" -F 'SEGMENT_INDEX 0' "$LOG/REGENERATE_REAL_SEGMENT0.log" >/dev/null || exit 62
run_d1 REGENERATE_REAL_SEGMENT1
RC=$?
[ "$RC" -eq 0 ] || exit 63
"$P/bin/grep" -F 'SEGMENT_INDEX 1' "$LOG/REGENERATE_REAL_SEGMENT1.log" >/dev/null || exit 64
run_d1 REGENERATE_REAL_COMPLETE
RC=$?
[ "$RC" -eq 0 ] || exit 65
"$P/bin/grep" -F 'DEEP_RELEARN_COMPLETE YES' "$LOG/REGENERATE_REAL_COMPLETE.log" >/dev/null || exit 66

REAL_EVIDENCE_SHA=$("$P/bin/sha256sum" "$D1_EVIDENCE" | "$P/bin/awk" '{print $1}')
REAL_EVIDENCE_COMMIT_COUNT=$("$P/bin/grep" -c ' || COMMIT=YES$' "$D1_EVIDENCE" 2>/dev/null || true)
printf 'REGENERATED_REAL_EVIDENCE_SHA256=%s\n' "$REAL_EVIDENCE_SHA"
printf 'REGENERATED_REAL_EVIDENCE_COMMIT_COUNT=%s\n' "$REAL_EVIDENCE_COMMIT_COUNT"
[ "$REAL_EVIDENCE_SHA" = '9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a' ] || exit 67
[ "$REAL_EVIDENCE_COMMIT_COUNT" -eq 2 ] || exit 68

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'REVALIDATION_SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 69
[ -s "$BC.partial" ] || exit 70
"$P/bin/mv" -f -- "$BC.partial" "$BC"
"$P/bin/chmod" 0400 "$BC"
BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'REVALIDATION_BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

run_v29() {
    CASE_NAME="$1"
    RUNLOG="$LOG/$CASE_NAME.log"
    (
        cd "$BRAIN" || exit 80
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?
    printf '\n=== %s ===\n' "$CASE_NAME"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"
    return "$RC"
}

"$P/bin/printf" '%s' "$SELECTED" > "$V29_SELECTED"
"$P/bin/printf" '%s' "$REAL_SURVEY" > "$V29_SURVEY_PATH"
"$P/bin/printf" '%s' "$D1_EVIDENCE" > "$V29_EVIDENCE_PATH"
"$P/bin/printf" '%s' "$SNAPSHOT" > "$V29_SNAPSHOT_DIR"
"$P/bin/printf" '%s' "$D1_ACTIVE_WORK" > "$V29_ACTIVE_WORK_PATH"
"$P/bin/printf" '%s' "$D1_CURSOR" > "$V29_CURSOR_PATH"
: > "$V29_STATE"

run_v29 REAL_REVALIDATION
RC=$?
[ "$RC" -eq 0 ] || exit 81
"$P/bin/grep" -F 'DEEP_RELEARN_COMPLETE 1' "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 82
"$P/bin/grep" -F 'ACTIVE_WORK_MATCH 1' "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 83
"$P/bin/grep" -F "BASELINE_ANCHOR $EXPECTED_REAL_BASELINE" "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 84
"$P/bin/grep" -F 'COMMITTED_DEEP_SEGMENT_COUNT 2' "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 85
"$P/bin/grep" -F 'MATCHING_BASELINE_SEGMENT_COUNT 1' "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 86
"$P/bin/grep" -F 'DISTINCT_DEEP_ANCHOR_COUNT 2' "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 87
"$P/bin/grep" -F 'REVALIDATION_READY 1' "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 88
"$P/bin/grep" -F 'REVALIDATION_RESULT REOBSERVED' "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 89
"$P/bin/grep" -F 'REVALIDATION_APPEND_RC 0' "$LOG/REAL_REVALIDATION.log" >/dev/null || exit 90

REAL_REVALIDATION_SHA=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
printf 'REAL_REVALIDATION_STATE_SHA256=%s\n' "$REAL_REVALIDATION_SHA"

run_v29 REAL_REVALIDATION_FRESH_VM_REUSE
RC=$?
[ "$RC" -eq 0 ] || exit 91
"$P/bin/grep" -F 'REVALIDATION_ALREADY_COMMITTED 1' "$LOG/REAL_REVALIDATION_FRESH_VM_REUSE.log" >/dev/null || exit 92
REUSE_SHA=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
[ "$REUSE_SHA" = "$REAL_REVALIDATION_SHA" ] || exit 93

: > "$V29_STATE"
run_v29 REAL_REVALIDATION_REPLAY
RC=$?
[ "$RC" -eq 0 ] || exit 94
REPLAY_SHA=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
printf 'REAL_REVALIDATION_REPLAY_SHA256=%s\n' "$REPLAY_SHA"
[ "$REPLAY_SHA" = "$REAL_REVALIDATION_SHA" ] || exit 95

"$P/bin/printf" 'one two\nthree four' > "$SYNTH_DIR/Q.document"
"$P/bin/cat" > "$SYNTH_SURVEY" <<'EOF_SYN_SURVEY'
DOC=Q || SURVEY_STATUS=COMPLETE || BEST_LOCAL_RELATION=alpha => beta || COMMIT=YES
EOF_SYN_SURVEY
"$P/bin/cat" > "$SYNTH_EVIDENCE" <<'EOF_SYN_EVIDENCE'
WORK=Q || CURSOR= || BEST_LOCAL_RELATION=gamma => delta || COMMIT=YES
EOF_SYN_EVIDENCE
"$P/bin/printf" 'Q' > "$SYNTH_ACTIVE"
"$P/bin/printf" '|' > "$SYNTH_CURSOR"
"$P/bin/printf" 'Q' > "$V29_SELECTED"
"$P/bin/printf" '%s' "$SYNTH_SURVEY" > "$V29_SURVEY_PATH"
"$P/bin/printf" '%s' "$SYNTH_EVIDENCE" > "$V29_EVIDENCE_PATH"
"$P/bin/printf" '%s' "$SYNTH_DIR" > "$V29_SNAPSHOT_DIR"
"$P/bin/printf" '%s' "$SYNTH_ACTIVE" > "$V29_ACTIVE_WORK_PATH"
"$P/bin/printf" '%s' "$SYNTH_CURSOR" > "$V29_CURSOR_PATH"
: > "$V29_STATE"

run_v29 NEGATIVE_NOT_REOBSERVED
RC=$?
[ "$RC" -eq 0 ] || exit 96
"$P/bin/grep" -F 'DEEP_RELEARN_COMPLETE 1' "$LOG/NEGATIVE_NOT_REOBSERVED.log" >/dev/null || exit 97
"$P/bin/grep" -F 'MATCHING_BASELINE_SEGMENT_COUNT 0' "$LOG/NEGATIVE_NOT_REOBSERVED.log" >/dev/null || exit 98
"$P/bin/grep" -F 'REVALIDATION_RESULT NOT_REOBSERVED' "$LOG/NEGATIVE_NOT_REOBSERVED.log" >/dev/null || exit 99

: > "$SYNTH_CURSOR"
: > "$V29_STATE"
STATE_INCOMPLETE_BEFORE=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
run_v29 INCOMPLETE_DEEP_RELEARN
RC=$?
[ "$RC" -eq 0 ] || exit 100
"$P/bin/grep" -F 'DEEP_RELEARN_COMPLETE 0' "$LOG/INCOMPLETE_DEEP_RELEARN.log" >/dev/null || exit 101
"$P/bin/grep" -F 'REVALIDATION_READY 0' "$LOG/INCOMPLETE_DEEP_RELEARN.log" >/dev/null || exit 102
"$P/bin/grep" -F 'REVALIDATION_RESULT PENDING' "$LOG/INCOMPLETE_DEEP_RELEARN.log" >/dev/null || exit 103
STATE_INCOMPLETE_AFTER=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
[ "$STATE_INCOMPLETE_AFTER" = "$STATE_INCOMPLETE_BEFORE" ] || exit 104

"$P/bin/printf" '|' > "$SYNTH_CURSOR"
"$P/bin/cat" > "$SYNTH_EVIDENCE" <<'EOF_PARTIAL_EVIDENCE'
WORK=Q || CURSOR= || BEST_LOCAL_RELATION=alpha => beta
WORK=Q || CURSOR= || BEST_LOCAL_RELATION=gamma => delta || COMMIT=YES
EOF_PARTIAL_EVIDENCE
: > "$V29_STATE"
run_v29 PARTIAL_EVIDENCE_FILTER
RC=$?
[ "$RC" -eq 0 ] || exit 105
"$P/bin/grep" -F 'IGNORED_EVIDENCE_RECORD_COUNT 1' "$LOG/PARTIAL_EVIDENCE_FILTER.log" >/dev/null || exit 106
"$P/bin/grep" -F 'MATCHING_BASELINE_SEGMENT_COUNT 0' "$LOG/PARTIAL_EVIDENCE_FILTER.log" >/dev/null || exit 107
"$P/bin/grep" -F 'REVALIDATION_RESULT NOT_REOBSERVED' "$LOG/PARTIAL_EVIDENCE_FILTER.log" >/dev/null || exit 108

: > "$V29_STATE"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'WORK=S%s || RESULT=REOBSERVED || BASELINE=a => b || COMMIT=YES\n' "$I" >> "$V29_STATE"
    I=$((I + 1))
done
STATE_LIMIT_SHA_BEFORE=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
run_v29 STATE_LIMIT_REFUSAL
RC=$?
[ "$RC" -eq 0 ] || exit 109
"$P/bin/grep" -F 'STATE_LIMIT_EXCEEDED 1' "$LOG/STATE_LIMIT_REFUSAL.log" >/dev/null || exit 110
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/STATE_LIMIT_REFUSAL.log" >/dev/null || exit 111
STATE_LIMIT_SHA_AFTER=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
[ "$STATE_LIMIT_SHA_AFTER" = "$STATE_LIMIT_SHA_BEFORE" ] || exit 112

: > "$OVER_EVIDENCE"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'WORK=Q || CURSOR=x%s || BEST_LOCAL_RELATION=a => b || COMMIT=YES\n' "$I" >> "$OVER_EVIDENCE"
    I=$((I + 1))
done
"$P/bin/printf" '%s' "$OVER_EVIDENCE" > "$V29_EVIDENCE_PATH"
: > "$V29_STATE"
EVIDENCE_LIMIT_STATE_SHA_BEFORE=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
run_v29 EVIDENCE_LIMIT_REFUSAL
RC=$?
[ "$RC" -eq 0 ] || exit 113
"$P/bin/grep" -F 'EVIDENCE_LIMIT_EXCEEDED 1' "$LOG/EVIDENCE_LIMIT_REFUSAL.log" >/dev/null || exit 114
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/EVIDENCE_LIMIT_REFUSAL.log" >/dev/null || exit 115
EVIDENCE_LIMIT_STATE_SHA_AFTER=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
[ "$EVIDENCE_LIMIT_STATE_SHA_AFTER" = "$EVIDENCE_LIMIT_STATE_SHA_BEFORE" ] || exit 116

: > "$OVER_SURVEY"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'DOC=Q%s || SURVEY_STATUS=COMPLETE || BEST_LOCAL_RELATION=a => b || COMMIT=YES\n' "$I" >> "$OVER_SURVEY"
    I=$((I + 1))
done
"$P/bin/printf" '%s' "$OVER_SURVEY" > "$V29_SURVEY_PATH"
"$P/bin/printf" '%s' "$SYNTH_EVIDENCE" > "$V29_EVIDENCE_PATH"
: > "$V29_STATE"
SURVEY_LIMIT_STATE_SHA_BEFORE=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
run_v29 SURVEY_LIMIT_REFUSAL
RC=$?
[ "$RC" -eq 0 ] || exit 117
"$P/bin/grep" -F 'SURVEY_LIMIT_EXCEEDED 1' "$LOG/SURVEY_LIMIT_REFUSAL.log" >/dev/null || exit 118
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/SURVEY_LIMIT_REFUSAL.log" >/dev/null || exit 119
SURVEY_LIMIT_STATE_SHA_AFTER=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
[ "$SURVEY_LIMIT_STATE_SHA_AFTER" = "$SURVEY_LIMIT_STATE_SHA_BEFORE" ] || exit 120

"$P/bin/printf" '%s' "$SELECTED" > "$V29_SELECTED"
"$P/bin/printf" '%s' "$REAL_SURVEY" > "$V29_SURVEY_PATH"
"$P/bin/printf" '%s' "$D1_EVIDENCE" > "$V29_EVIDENCE_PATH"
"$P/bin/printf" '%s' "$SNAPSHOT" > "$V29_SNAPSHOT_DIR"
"$P/bin/printf" '%s' "$D1_ACTIVE_WORK" > "$V29_ACTIVE_WORK_PATH"
"$P/bin/printf" '%s' "$D1_CURSOR" > "$V29_CURSOR_PATH"

REAL_SURVEY_SHA_AFTER=$("$P/bin/sha256sum" "$REAL_SURVEY" | "$P/bin/awk" '{print $1}')
REAL_DOC_SHA_AFTER=$("$P/bin/sha256sum" "$REAL_DOC" | "$P/bin/awk" '{print $1}')
REAL_EVIDENCE_SHA_AFTER=$("$P/bin/sha256sum" "$D1_EVIDENCE" | "$P/bin/awk" '{print $1}')

printf 'REAL_SURVEY_SHA256_AFTER=%s\n' "$REAL_SURVEY_SHA_AFTER"
printf 'REAL_DOCUMENT_SHA256_AFTER=%s\n' "$REAL_DOC_SHA_AFTER"
printf 'REAL_DEEP_EVIDENCE_SHA256_AFTER=%s\n' "$REAL_EVIDENCE_SHA_AFTER"

[ "$REAL_SURVEY_SHA_AFTER" = "$REAL_SURVEY_SHA_BEFORE" ] || exit 121
[ "$REAL_DOC_SHA_AFTER" = "$REAL_DOC_SHA_BEFORE" ] || exit 122
[ "$REAL_EVIDENCE_SHA_AFTER" = "$REAL_EVIDENCE_SHA" ] || exit 123

printf '\nV29R1_DEEP_RELEARN_STRUCTURAL_REVALIDATION_PREFLIGHT=PASS\n'
printf 'REAL_DEEP_EVIDENCE_REGENERATED_BY_NATIVE_D1=PASS\n'
printf 'REAL_STRUCTURAL_BASELINE_REOBSERVED=PASS\n'
printf 'NATIVE_STRUCTURAL_REVALIDATION=PROVEN_IN_SELECTED_DOCUMENT_SCOPE\n'
printf 'PERSISTENT_REVALIDATION_STATE_REUSE=PASS\n'
printf 'DETERMINISTIC_REVALIDATION_REPLAY=PASS\n'
printf 'NEGATIVE_NOT_REOBSERVED=PASS\n'
printf 'INCOMPLETE_DEEP_RELEARN_BLOCKS_REVALIDATION=PASS\n'
printf 'PARTIAL_EVIDENCE_COMMIT_FILTER=PASS\n'
printf 'STEP_LIMIT_STATUS=BOUNDED\n'
printf 'REAL_SURVEY_MUTATED=NO\n'
printf 'REAL_SELECTED_DOCUMENT_MUTATED=NO\n'
printf 'REAL_DEEP_EVIDENCE_MUTATED_AFTER_REGENERATION=NO\n'
printf 'HOST_REVALIDATION_DECISION=NO\n'
printf 'HOST_TRUTH_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'STRUCTURAL_REVALIDATION_ONLY=YES\n'
printf 'SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'NEXT_ACTION=BUILD_REVALIDATION_TO_REVISIT_OR_ARCHIVE_FOR_NOW_PREFLIGHT\n'
