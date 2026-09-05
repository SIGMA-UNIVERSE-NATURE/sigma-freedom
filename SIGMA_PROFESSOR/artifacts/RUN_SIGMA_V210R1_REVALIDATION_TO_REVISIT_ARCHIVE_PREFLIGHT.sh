#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BRAIN="$REPO/BRAIN/EXTRA BRAIN_OPPO_24826"
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

REVAL_SRC="$E/SIGMA_DEEP_RELEARN_STRUCTURAL_REVALIDATION_V2_9R1.sigma"
REVAL_BC="$E/SIGMA_DEEP_RELEARN_STRUCTURAL_REVALIDATION_V2_9R1.sigmab"
EXPECTED_REVAL_SOURCE=94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b
EXPECTED_REVAL_BYTECODE=c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8

SRC="$E/SIGMA_REVALIDATION_TO_REVISIT_ARCHIVE_V2_10R1.sigma"
BC="$E/SIGMA_REVALIDATION_TO_REVISIT_ARCHIVE_V2_10R1.sigmab"
EXPECTED_SOURCE=67fb7234c0cd9e84c602a6dadb55f6e1ced6265406745ba6b3b9a7a95e0c4993

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

V210_SELECTED="$E/SIGMA_V210R1_SELECTED_WORK.memory"
V210_REVALIDATION_PATH="$E/SIGMA_V210R1_REVALIDATION_PATH.memory"
V210_LIFECYCLE_STATE="$E/SIGMA_V210R1_LIFECYCLE_STATE.memory"

STATE="$HOME_SIGMA/SIGMA_V210R1_REVALIDATION_LIFECYCLE_PREFLIGHT"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"
SYNTH_REVAL="$STATE/synth_revalidation.memory"
OVER_REVAL="$STATE/over_revalidation.memory"

EXPECTED_SELECTED=0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b
EXPECTED_REAL_REVALIDATION_STATE_SHA=bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac

mkdir -p "$STATE" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V210R1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_bridge_source=$("$P/bin/sha256sum" "$BRIDGE_SRC" | "$P/bin/awk" '{print $1}')
actual_deep_source=$("$P/bin/sha256sum" "$DEEP_SRC" | "$P/bin/awk" '{print $1}')
actual_reval_source=$("$P/bin/sha256sum" "$REVAL_SRC" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V210R1_REVALIDATION_TO_REVISIT_ARCHIVE_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_LIFECYCLE_DECISION=NO\n'
printf 'HOST_REVISIT_DECISION=NO\n'
printf 'HOST_ARCHIVE_DECISION=NO\n'
printf 'HOST_TRUTH_DECISION=NO\n'
printf 'REAL_REVALIDATION_REGENERATION=YES\n'
printf 'FRESH_VM_STATE_REUSE_TEST=YES\n'
printf 'DETERMINISTIC_REPLAY_TEST=YES\n'
printf 'SYNTHETIC_ARCHIVE_BRANCH_TEST=YES\n'
printf 'WAIT_FOR_REVALIDATION_TEST=YES\n'
printf 'CONFLICT_TEST=YES\n'
printf 'PARTIAL_LIFECYCLE_FILTER_TEST=YES\n'
printf 'STEP_LIMIT_BOUNDEDNESS_TEST=YES\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || exit 21
[ "$actual_vm" = "$EXPECTED_VM" ] || exit 22
[ "$actual_bridge_source" = "$EXPECTED_BRIDGE_SOURCE" ] || exit 23
[ "$actual_deep_source" = "$EXPECTED_DEEP_SOURCE" ] || exit 24
[ "$actual_reval_source" = "$EXPECTED_REVAL_SOURCE" ] || exit 25
[ "$actual_source" = "$EXPECTED_SOURCE" ] || exit 26
[ -f "$REAL_SURVEY" ] || exit 27
[ -d "$SNAPSHOT" ] || exit 28

REAL_SURVEY_SHA_BEFORE=$("$P/bin/sha256sum" "$REAL_SURVEY" | "$P/bin/awk" '{print $1}')

compile_exact() {
    CSRC="$1"
    CBC="$2"
    EXPECTED_BC="$3"
    LABEL="$4"

    "$P/bin/rm" -f -- "$CBC.partial"
    "$SIGMAC" "$CSRC" "$CBC.partial"
    RC=$?
    printf '%s_SIGMAC_RC=%s\n' "$LABEL" "$RC"
    [ "$RC" -eq 0 ] || return 1

    SHA=$("$P/bin/sha256sum" "$CBC.partial" | "$P/bin/awk" '{print $1}')
    printf '%s_BYTECODE_SHA256=%s\n' "$LABEL" "$SHA"
    [ "$SHA" = "$EXPECTED_BC" ] || return 2

    "$P/bin/mv" -f -- "$CBC.partial" "$CBC"
    "$P/bin/chmod" 0400 "$CBC"
    return 0
}

compile_exact "$BRIDGE_SRC" "$BRIDGE_BC" "$EXPECTED_BRIDGE_BYTECODE" BRIDGE || exit 30
compile_exact "$DEEP_SRC" "$DEEP_BC" "$EXPECTED_DEEP_BYTECODE" DEEP || exit 31
compile_exact "$REVAL_SRC" "$REVAL_BC" "$EXPECTED_REVAL_BYTECODE" REVALIDATION || exit 32

"$P/bin/printf" '%s' "$REAL_SURVEY" > "$BRIDGE_SURVEY_PATH"
: > "$BRIDGE_STATE"
: > "$BRIDGE_SELECTED"
(
    cd "$BRAIN" || exit 40
    "$VM" "$BRIDGE_BC"
) > "$LOG/bridge_real_selection.log" 2>&1
RC=$?
printf '\n=== REAL_NATIVE_CURRICULUM_SELECTION ===\n'
printf 'VM_RC=%s\n' "$RC"
"$P/bin/cat" "$LOG/bridge_real_selection.log"
[ "$RC" -eq 0 ] || exit 50

SELECTED=$("$P/bin/cat" "$BRIDGE_SELECTED")
printf 'NATIVE_SELECTED_WORK=%s\n' "$SELECTED"
[ "$SELECTED" = "$EXPECTED_SELECTED" ] || exit 51

REAL_DOC="$SNAPSHOT/$SELECTED.document"
REAL_DOC_SHA_BEFORE=$("$P/bin/sha256sum" "$REAL_DOC" | "$P/bin/awk" '{print $1}')

"$P/bin/printf" '%s' "$SNAPSHOT" > "$D1_SNAPSHOT_DIR"
: > "$D1_ACTIVE_WORK"
: > "$D1_CURSOR"
: > "$D1_EVIDENCE"

run_bc() {
    CASE_NAME="$1"
    BYTECODE="$2"
    RUNLOG="$LOG/$CASE_NAME.log"
    (
        cd "$BRAIN" || exit 60
        "$VM" "$BYTECODE"
    ) >"$RUNLOG" 2>&1
    RC=$?
    printf '\n=== %s ===\n' "$CASE_NAME"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"
    return "$RC"
}

run_bc REGENERATE_REAL_SEGMENT0 "$DEEP_BC"
[ "$?" -eq 0 ] || exit 52
run_bc REGENERATE_REAL_SEGMENT1 "$DEEP_BC"
[ "$?" -eq 0 ] || exit 53
run_bc REGENERATE_REAL_COMPLETE "$DEEP_BC"
[ "$?" -eq 0 ] || exit 54

REAL_EVIDENCE_SHA=$("$P/bin/sha256sum" "$D1_EVIDENCE" | "$P/bin/awk" '{print $1}')
[ "$REAL_EVIDENCE_SHA" = '9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a' ] || exit 55

"$P/bin/printf" '%s' "$SELECTED" > "$V29_SELECTED"
"$P/bin/printf" '%s' "$REAL_SURVEY" > "$V29_SURVEY_PATH"
"$P/bin/printf" '%s' "$D1_EVIDENCE" > "$V29_EVIDENCE_PATH"
"$P/bin/printf" '%s' "$SNAPSHOT" > "$V29_SNAPSHOT_DIR"
"$P/bin/printf" '%s' "$D1_ACTIVE_WORK" > "$V29_ACTIVE_WORK_PATH"
"$P/bin/printf" '%s' "$D1_CURSOR" > "$V29_CURSOR_PATH"
: > "$V29_STATE"

run_bc REGENERATE_REAL_REVALIDATION "$REVAL_BC"
[ "$?" -eq 0 ] || exit 56
"$P/bin/grep" -F 'REVALIDATION_RESULT NOT_REOBSERVED' "$LOG/REGENERATE_REAL_REVALIDATION.log" >/dev/null || exit 57

REAL_REVAL_SHA=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')
printf 'REGENERATED_REAL_REVALIDATION_SHA256=%s\n' "$REAL_REVAL_SHA"
[ "$REAL_REVAL_SHA" = "$EXPECTED_REAL_REVALIDATION_STATE_SHA" ] || exit 58

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'LIFECYCLE_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || exit 59
[ -s "$BC.partial" ] || exit 60
"$P/bin/mv" -f -- "$BC.partial" "$BC"
"$P/bin/chmod" 0400 "$BC"
LIFECYCLE_BC_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'LIFECYCLE_BYTECODE_SHA256=%s\n' "$LIFECYCLE_BC_SHA"

run_lifecycle() {
    CASE_NAME="$1"
    run_bc "$CASE_NAME" "$BC"
}

"$P/bin/printf" '%s' "$SELECTED" > "$V210_SELECTED"
"$P/bin/printf" '%s' "$V29_STATE" > "$V210_REVALIDATION_PATH"
: > "$V210_LIFECYCLE_STATE"

run_lifecycle REAL_NOT_REOBSERVED_TO_REVISIT
[ "$?" -eq 0 ] || exit 61
"$P/bin/grep" -F 'REVALIDATION_RESULT NOT_REOBSERVED' "$LOG/REAL_NOT_REOBSERVED_TO_REVISIT.log" >/dev/null || exit 62
"$P/bin/grep" -F 'LIFECYCLE_ACTION REVISIT' "$LOG/REAL_NOT_REOBSERVED_TO_REVISIT.log" >/dev/null || exit 63
"$P/bin/grep" -F 'LIFECYCLE_READY 1' "$LOG/REAL_NOT_REOBSERVED_TO_REVISIT.log" >/dev/null || exit 64
"$P/bin/grep" -F 'LIFECYCLE_APPEND_RC 0' "$LOG/REAL_NOT_REOBSERVED_TO_REVISIT.log" >/dev/null || exit 65

REAL_LIFECYCLE_SHA=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')
printf 'REAL_LIFECYCLE_STATE_SHA256=%s\n' "$REAL_LIFECYCLE_SHA"

run_lifecycle REAL_REVISIT_FRESH_VM_REUSE
[ "$?" -eq 0 ] || exit 66
"$P/bin/grep" -F 'LIFECYCLE_ALREADY_COMMITTED 1' "$LOG/REAL_REVISIT_FRESH_VM_REUSE.log" >/dev/null || exit 67
REUSE_SHA=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')
[ "$REUSE_SHA" = "$REAL_LIFECYCLE_SHA" ] || exit 68

: > "$V210_LIFECYCLE_STATE"
run_lifecycle REAL_REVISIT_REPLAY
[ "$?" -eq 0 ] || exit 69
REPLAY_SHA=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')
printf 'REAL_LIFECYCLE_REPLAY_SHA256=%s\n' "$REPLAY_SHA"
[ "$REPLAY_SHA" = "$REAL_LIFECYCLE_SHA" ] || exit 70

"$P/bin/cat" > "$SYNTH_REVAL" <<'EOF_ARCHIVE'
WORK=Q || RESULT=REOBSERVED || BASELINE=alpha => beta || COMMIT=YES
EOF_ARCHIVE
"$P/bin/printf" 'Q' > "$V210_SELECTED"
"$P/bin/printf" '%s' "$SYNTH_REVAL" > "$V210_REVALIDATION_PATH"
: > "$V210_LIFECYCLE_STATE"

run_lifecycle SYNTHETIC_REOBSERVED_TO_ARCHIVE
[ "$?" -eq 0 ] || exit 71
"$P/bin/grep" -F 'LIFECYCLE_ACTION ARCHIVE_FOR_NOW' "$LOG/SYNTHETIC_REOBSERVED_TO_ARCHIVE.log" >/dev/null || exit 72
"$P/bin/grep" -F 'ARCHIVE_FOR_NOW_DELETES_EVIDENCE NO' "$LOG/SYNTHETIC_REOBSERVED_TO_ARCHIVE.log" >/dev/null || exit 73

"$P/bin/cat" > "$SYNTH_REVAL" <<'EOF_WAIT'
WORK=Q || RESULT=NOT_REOBSERVED || BASELINE=alpha => beta
EOF_WAIT
: > "$V210_LIFECYCLE_STATE"
WAIT_SHA_BEFORE=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')

run_lifecycle UNCOMMITTED_REVALIDATION_WAIT
[ "$?" -eq 0 ] || exit 74
"$P/bin/grep" -F 'LIFECYCLE_ACTION WAIT_FOR_REVALIDATION' "$LOG/UNCOMMITTED_REVALIDATION_WAIT.log" >/dev/null || exit 75
"$P/bin/grep" -F 'LIFECYCLE_READY 0' "$LOG/UNCOMMITTED_REVALIDATION_WAIT.log" >/dev/null || exit 76
WAIT_SHA_AFTER=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')
[ "$WAIT_SHA_AFTER" = "$WAIT_SHA_BEFORE" ] || exit 77

"$P/bin/cat" > "$SYNTH_REVAL" <<'EOF_CONFLICT'
WORK=Q || RESULT=REOBSERVED || BASELINE=alpha => beta || COMMIT=YES
WORK=Q || RESULT=NOT_REOBSERVED || BASELINE=alpha => beta || COMMIT=YES
EOF_CONFLICT
: > "$V210_LIFECYCLE_STATE"
CONFLICT_SHA_BEFORE=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')

run_lifecycle CONFLICT_WAIT
[ "$?" -eq 0 ] || exit 78
"$P/bin/grep" -F 'REVALIDATION_CONFLICT 1' "$LOG/CONFLICT_WAIT.log" >/dev/null || exit 79
"$P/bin/grep" -F 'LIFECYCLE_ACTION WAIT_FOR_REVALIDATION' "$LOG/CONFLICT_WAIT.log" >/dev/null || exit 80
"$P/bin/grep" -F 'LIFECYCLE_READY 0' "$LOG/CONFLICT_WAIT.log" >/dev/null || exit 81
CONFLICT_SHA_AFTER=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')
[ "$CONFLICT_SHA_AFTER" = "$CONFLICT_SHA_BEFORE" ] || exit 82

"$P/bin/cat" > "$SYNTH_REVAL" <<'EOF_REVISIT'
WORK=Q || RESULT=NOT_REOBSERVED || BASELINE=alpha => beta || COMMIT=YES
EOF_REVISIT
"$P/bin/cat" > "$V210_LIFECYCLE_STATE" <<'EOF_PARTIAL_LIFECYCLE'
WORK=Q || ACTION=REVISIT || FROM_RESULT=NOT_REOBSERVED
EOF_PARTIAL_LIFECYCLE

run_lifecycle PARTIAL_LIFECYCLE_FILTER
[ "$?" -eq 0 ] || exit 83
"$P/bin/grep" -F 'IGNORED_LIFECYCLE_RECORD_COUNT 1' "$LOG/PARTIAL_LIFECYCLE_FILTER.log" >/dev/null || exit 84
"$P/bin/grep" -F 'LIFECYCLE_ALREADY_COMMITTED 0' "$LOG/PARTIAL_LIFECYCLE_FILTER.log" >/dev/null || exit 85
"$P/bin/grep" -F 'LIFECYCLE_APPEND_RC 0' "$LOG/PARTIAL_LIFECYCLE_FILTER.log" >/dev/null || exit 86

: > "$V210_LIFECYCLE_STATE"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'WORK=S%s || ACTION=REVISIT || FROM_RESULT=NOT_REOBSERVED || COMMIT=YES\n' "$I" >> "$V210_LIFECYCLE_STATE"
    I=$((I + 1))
done
LIFE_LIMIT_SHA_BEFORE=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')

run_lifecycle LIFECYCLE_LIMIT_REFUSAL
[ "$?" -eq 0 ] || exit 87
"$P/bin/grep" -F 'LIFECYCLE_LIMIT_EXCEEDED 1' "$LOG/LIFECYCLE_LIMIT_REFUSAL.log" >/dev/null || exit 88
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/LIFECYCLE_LIMIT_REFUSAL.log" >/dev/null || exit 89
LIFE_LIMIT_SHA_AFTER=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')
[ "$LIFE_LIMIT_SHA_AFTER" = "$LIFE_LIMIT_SHA_BEFORE" ] || exit 90

: > "$OVER_REVAL"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'WORK=Q || RESULT=NOT_REOBSERVED || BASELINE=x%s => y || COMMIT=YES\n' "$I" >> "$OVER_REVAL"
    I=$((I + 1))
done
"$P/bin/printf" '%s' "$OVER_REVAL" > "$V210_REVALIDATION_PATH"
: > "$V210_LIFECYCLE_STATE"
REVAL_LIMIT_SHA_BEFORE=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')

run_lifecycle REVALIDATION_LIMIT_REFUSAL
[ "$?" -eq 0 ] || exit 91
"$P/bin/grep" -F 'REVALIDATION_LIMIT_EXCEEDED 1' "$LOG/REVALIDATION_LIMIT_REFUSAL.log" >/dev/null || exit 92
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/REVALIDATION_LIMIT_REFUSAL.log" >/dev/null || exit 93
REVAL_LIMIT_SHA_AFTER=$("$P/bin/sha256sum" "$V210_LIFECYCLE_STATE" | "$P/bin/awk" '{print $1}')
[ "$REVAL_LIMIT_SHA_AFTER" = "$REVAL_LIMIT_SHA_BEFORE" ] || exit 94

REAL_SURVEY_SHA_AFTER=$("$P/bin/sha256sum" "$REAL_SURVEY" | "$P/bin/awk" '{print $1}')
REAL_DOC_SHA_AFTER=$("$P/bin/sha256sum" "$REAL_DOC" | "$P/bin/awk" '{print $1}')
REAL_EVIDENCE_SHA_AFTER=$("$P/bin/sha256sum" "$D1_EVIDENCE" | "$P/bin/awk" '{print $1}')
REAL_REVAL_SHA_AFTER=$("$P/bin/sha256sum" "$V29_STATE" | "$P/bin/awk" '{print $1}')

printf 'REAL_SURVEY_SHA256_AFTER=%s\n' "$REAL_SURVEY_SHA_AFTER"
printf 'REAL_DOCUMENT_SHA256_AFTER=%s\n' "$REAL_DOC_SHA_AFTER"
printf 'REAL_DEEP_EVIDENCE_SHA256_AFTER=%s\n' "$REAL_EVIDENCE_SHA_AFTER"
printf 'REAL_REVALIDATION_SHA256_AFTER=%s\n' "$REAL_REVAL_SHA_AFTER"

[ "$REAL_SURVEY_SHA_AFTER" = "$REAL_SURVEY_SHA_BEFORE" ] || exit 95
[ "$REAL_DOC_SHA_AFTER" = "$REAL_DOC_SHA_BEFORE" ] || exit 96
[ "$REAL_EVIDENCE_SHA_AFTER" = "$REAL_EVIDENCE_SHA" ] || exit 97
[ "$REAL_REVAL_SHA_AFTER" = "$EXPECTED_REAL_REVALIDATION_STATE_SHA" ] || exit 98

printf '\nV210R1_REVALIDATION_TO_REVISIT_ARCHIVE_PREFLIGHT=PASS\n'
printf 'REAL_NOT_REOBSERVED_TO_REVISIT=PASS\n'
printf 'SYNTHETIC_REOBSERVED_TO_ARCHIVE_FOR_NOW=PASS\n'
printf 'WAIT_FOR_REVALIDATION_UNCOMMITTED=PASS\n'
printf 'CONFLICT_BLOCKS_LIFECYCLE_COMMIT=PASS\n'
printf 'PERSISTENT_LIFECYCLE_STATE_REUSE=PASS\n'
printf 'DETERMINISTIC_LIFECYCLE_REPLAY=PASS\n'
printf 'PARTIAL_LIFECYCLE_COMMIT_FILTER=PASS\n'
printf 'STEP_LIMIT_STATUS=BOUNDED\n'
printf 'ARCHIVE_FOR_NOW_DELETES_EVIDENCE=NO\n'
printf 'HOST_LIFECYCLE_DECISION=NO\n'
printf 'HOST_REVISIT_DECISION=NO\n'
printf 'HOST_ARCHIVE_DECISION=NO\n'
printf 'HOST_TRUTH_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'STRUCTURAL_LIFECYCLE_ONLY=YES\n'
printf 'SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'NEXT_ACTION=CHECKPOINT_V210R1_THEN_BUILD_REVISIT_EXECUTION_AND_ARCHIVE_REENTRY_POLICY\n'
