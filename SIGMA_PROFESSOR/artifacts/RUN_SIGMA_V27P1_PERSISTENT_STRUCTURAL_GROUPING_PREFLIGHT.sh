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

SRC="$E/SIGMA_STRUCTURAL_GROUPING_V2_7P_1.sigma"
BC="$E/SIGMA_STRUCTURAL_GROUPING_V2_7P_1.sigmab"
EXPECTED_SOURCE=9c28165037a2a7952bdb06444c99fa379d450a68cef83319276e93d5cea2e9af

STATE_ROOT="$HOME_SIGMA/SIGMA_V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT"
LOG="$STATE_ROOT/log"
LOCK="$STATE_ROOT/preflight.lock"

INPUT="$E/SIGMA_V27P1_NEW_PROFILES.memory"
PROFILE_STATE="$E/SIGMA_V27P1_PROFILE_STATE.memory"
OUTPUT="$E/SIGMA_V27P1_GROUP_ASSIGNMENTS.memory"

mkdir -p "$STATE_ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V27P1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_GROUP_SELECTION=NO\n'
printf 'HOST_TOPIC_CLASSIFICATION=NO\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'NEGATIVE_TEST=YES\n'
printf 'PERSISTENT_STATE_TEST=YES\n'
printf 'STEP_LIMIT_BOUNDEDNESS_TEST=YES\n'
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
    printf 'HOLD=V27P1_SOURCE_IDENTITY_MISMATCH\n'
    exit 23
}

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 24
[ -s "$BC.partial" ] || exit 25
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 26
"$P/bin/chmod" 0400 "$BC" || exit 27

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

    [ "$RC" -eq 0 ] || return 50
    "$P/bin/grep" -F 'HOST_GROUP_SELECTION NO' "$RUNLOG" >/dev/null || return 51
    "$P/bin/grep" -F 'HOST_TOPIC_CLASSIFICATION NO' "$RUNLOG" >/dev/null || return 52
    "$P/bin/grep" -F 'HOST_LEARNING NO' "$RUNLOG" >/dev/null || return 53
    "$P/bin/grep" -F 'SEMANTIC_UNDERSTANDING NOT_PROVEN' "$RUNLOG" >/dev/null || return 54
    return 0
}

expect_log() {
    CASE_NAME="$1"
    EXPECT="$2"
    "$P/bin/grep" -F "$EXPECT" "$LOG/$CASE_NAME.log" >/dev/null || {
        printf 'V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
        printf 'FAILURE_CASE=%s\n' "$CASE_NAME"
        printf 'MISSING_EXPECTATION=%s\n' "$EXPECT"
        exit 60
    }
}

# Positive persistence phase 1: one document is a singleton.
: > "$PROFILE_STATE"
: > "$OUTPUT"
"$P/bin/printf" '%s' 'DOC=A || ANCHOR=in => the' > "$INPUT"
run_vm POSITIVE_PHASE1 || exit $?
expect_log POSITIVE_PHASE1 'PERSISTED_PROFILE_COUNT 0'
expect_log POSITIVE_PHASE1 'PERSISTED_STATE_USED NO'
expect_log POSITIVE_PHASE1 'NEW_COMMITTED_PROFILE_COUNT 1'
expect_log POSITIVE_PHASE1 'MULTI_MEMBER_GROUP_COUNT 0'
expect_log POSITIVE_PHASE1 'GROUPED_DOCUMENT_COUNT 0'
expect_log POSITIVE_PHASE1 'SINGLETON_DOCUMENT_COUNT 1'

POS1_STATE_SHA=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
printf 'POSITIVE_PHASE1_STATE_SHA256=%s\n' "$POS1_STATE_SHA"

# Positive persistence phase 2: a fresh VM process sees A from persisted state;
# B with the same anchor changes the native assignment to SHARED.
"$P/bin/printf" '%s' 'DOC=B || ANCHOR=in => the' > "$INPUT"
run_vm POSITIVE_PHASE2_FRESH_VM || exit $?
expect_log POSITIVE_PHASE2_FRESH_VM 'PERSISTED_PROFILE_COUNT 1'
expect_log POSITIVE_PHASE2_FRESH_VM 'PERSISTED_STATE_USED YES'
expect_log POSITIVE_PHASE2_FRESH_VM 'NEW_COMMITTED_PROFILE_COUNT 1'
expect_log POSITIVE_PHASE2_FRESH_VM 'MULTI_MEMBER_GROUP_COUNT 1'
expect_log POSITIVE_PHASE2_FRESH_VM 'GROUPED_DOCUMENT_COUNT 2'
expect_log POSITIVE_PHASE2_FRESH_VM 'SINGLETON_DOCUMENT_COUNT 0'

POS2_STATE_SHA=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
POS2_OUTPUT_SHA=$("$P/bin/sha256sum" "$OUTPUT" | "$P/bin/awk" '{print $1}')
printf 'POSITIVE_PHASE2_STATE_SHA256=%s\n' "$POS2_STATE_SHA"
printf 'POSITIVE_PHASE2_ASSIGNMENT_SHA256=%s\n' "$POS2_OUTPUT_SHA"

[ "$POS1_STATE_SHA" != "$POS2_STATE_SHA" ] || {
    printf 'V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE=PERSISTED_STATE_DID_NOT_CHANGE_AFTER_NEW_EVIDENCE\n'
    exit 61
}

# Replay same B evidence: state must not grow and assignment must be identical.
"$P/bin/printf" '%s' 'DOC=B || ANCHOR=in => the' > "$INPUT"
run_vm POSITIVE_REPLAY_FRESH_VM || exit $?
expect_log POSITIVE_REPLAY_FRESH_VM 'PERSISTED_PROFILE_COUNT 2'
expect_log POSITIVE_REPLAY_FRESH_VM 'NEW_COMMITTED_PROFILE_COUNT 0'
expect_log POSITIVE_REPLAY_FRESH_VM 'DUPLICATE_INPUT_PROFILE_COUNT 1'
expect_log POSITIVE_REPLAY_FRESH_VM 'MULTI_MEMBER_GROUP_COUNT 1'
expect_log POSITIVE_REPLAY_FRESH_VM 'GROUPED_DOCUMENT_COUNT 2'

REPLAY_STATE_SHA=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
REPLAY_OUTPUT_SHA=$("$P/bin/sha256sum" "$OUTPUT" | "$P/bin/awk" '{print $1}')
printf 'REPLAY_STATE_SHA256=%s\n' "$REPLAY_STATE_SHA"
printf 'REPLAY_ASSIGNMENT_SHA256=%s\n' "$REPLAY_OUTPUT_SHA"

[ "$REPLAY_STATE_SHA" = "$POS2_STATE_SHA" ] || {
    printf 'V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE=REPLAY_MUTATED_DEDUPED_STATE\n'
    exit 62
}
[ "$REPLAY_OUTPUT_SHA" = "$POS2_OUTPUT_SHA" ] || {
    printf 'V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE=REPLAY_ASSIGNMENT_MISMATCH\n'
    exit 63
}

# Negative: duplicate evidence from the same document must not create a group.
: > "$PROFILE_STATE"
: > "$OUTPUT"
"$P/bin/printf" '%s' 'DOC=A || ANCHOR=in => the' > "$INPUT"
run_vm NEGATIVE_SEED || exit $?

NEG_SEED_STATE_SHA=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
"$P/bin/printf" '%s' 'DOC=A || ANCHOR=in => the' > "$INPUT"
run_vm NEGATIVE_DUPLICATE_SAME_DOC || exit $?
expect_log NEGATIVE_DUPLICATE_SAME_DOC 'PERSISTED_PROFILE_COUNT 1'
expect_log NEGATIVE_DUPLICATE_SAME_DOC 'NEW_COMMITTED_PROFILE_COUNT 0'
expect_log NEGATIVE_DUPLICATE_SAME_DOC 'DUPLICATE_INPUT_PROFILE_COUNT 1'
expect_log NEGATIVE_DUPLICATE_SAME_DOC 'MULTI_MEMBER_GROUP_COUNT 0'
expect_log NEGATIVE_DUPLICATE_SAME_DOC 'GROUPED_DOCUMENT_COUNT 0'
expect_log NEGATIVE_DUPLICATE_SAME_DOC 'SINGLETON_DOCUMENT_COUNT 1'

NEG_DUP_STATE_SHA=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
[ "$NEG_DUP_STATE_SHA" = "$NEG_SEED_STATE_SHA" ] || {
    printf 'V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE=SAME_DOC_DUPLICATE_MUTATED_STATE\n'
    exit 64
}

# Negative dynamic input: different anchor remains two singletons.
"$P/bin/printf" '%s' 'DOC=B || ANCHOR=Phi => Sigma' > "$INPUT"
run_vm NEGATIVE_DIFFERENT_ANCHOR || exit $?
expect_log NEGATIVE_DIFFERENT_ANCHOR 'PERSISTED_PROFILE_COUNT 1'
expect_log NEGATIVE_DIFFERENT_ANCHOR 'NEW_COMMITTED_PROFILE_COUNT 1'
expect_log NEGATIVE_DIFFERENT_ANCHOR 'MULTI_MEMBER_GROUP_COUNT 0'
expect_log NEGATIVE_DIFFERENT_ANCHOR 'GROUPED_DOCUMENT_COUNT 0'
expect_log NEGATIVE_DIFFERENT_ANCHOR 'SINGLETON_DOCUMENT_COUNT 2'

# Failure-state filter: malformed/uncommitted historical state must be ignored.
"$P/bin/cat" > "$PROFILE_STATE" <<'EOF_PARTIAL'
DOC=A || ANCHOR=in => the || COMMIT=YES
DOC=Z || ANCHOR=in => the || COMMIT=
EOF_PARTIAL
"$P/bin/printf" '%s' 'DOC=B || ANCHOR=in => the' > "$INPUT"
run_vm PARTIAL_STATE_FILTER || exit $?
expect_log PARTIAL_STATE_FILTER 'PERSISTED_PROFILE_COUNT 1'
expect_log PARTIAL_STATE_FILTER 'IGNORED_STATE_RECORD_COUNT 1'
expect_log PARTIAL_STATE_FILTER 'NEW_COMMITTED_PROFILE_COUNT 1'
expect_log PARTIAL_STATE_FILTER 'MULTI_MEMBER_GROUP_COUNT 1'
expect_log PARTIAL_STATE_FILTER 'GROUPED_DOCUMENT_COUNT 2'

# Boundedness: state above the native budget must be refused without mutation.
: > "$PROFILE_STATE"
i=1
while [ "$i" -le 66 ]; do
    "$P/bin/printf" 'DOC=Q%03d || ANCHOR=A%03d || COMMIT=YES\n' "$i" "$i" >> "$PROFILE_STATE"
    i=$((i + 1))
done
"$P/bin/printf" '%s' 'DOC=X || ANCHOR=in => the' > "$INPUT"
STATE_LIMIT_SHA_BEFORE=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
run_vm STATE_LIMIT_REFUSAL || exit $?
expect_log STATE_LIMIT_REFUSAL 'STATE_LIMIT_EXCEEDED 1'
expect_log STATE_LIMIT_REFUSAL 'STATE_MUTATION_ALLOWED NO'
expect_log STATE_LIMIT_REFUSAL 'COMPUTATION_BOUNDED YES'
STATE_LIMIT_SHA_AFTER=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
[ "$STATE_LIMIT_SHA_BEFORE" = "$STATE_LIMIT_SHA_AFTER" ] || {
    printf 'V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE=STATE_LIMIT_REFUSAL_MUTATED_STATE\n'
    exit 65
}

# Boundedness: dynamic input above the native budget must also be refused.
: > "$PROFILE_STATE"
: > "$INPUT"
i=1
while [ "$i" -le 17 ]; do
    if [ "$i" -gt 1 ]; then
        "$P/bin/printf" '\n' >> "$INPUT"
    fi
    "$P/bin/printf" 'DOC=I%03d || ANCHOR=R%03d' "$i" "$i" >> "$INPUT"
    i=$((i + 1))
done
INPUT_LIMIT_STATE_SHA_BEFORE=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
run_vm INPUT_LIMIT_REFUSAL || exit $?
expect_log INPUT_LIMIT_REFUSAL 'INPUT_LIMIT_EXCEEDED 1'
expect_log INPUT_LIMIT_REFUSAL 'STATE_MUTATION_ALLOWED NO'
expect_log INPUT_LIMIT_REFUSAL 'COMPUTATION_BOUNDED YES'
INPUT_LIMIT_STATE_SHA_AFTER=$("$P/bin/sha256sum" "$PROFILE_STATE" | "$P/bin/awk" '{print $1}')
[ "$INPUT_LIMIT_STATE_SHA_BEFORE" = "$INPUT_LIMIT_STATE_SHA_AFTER" ] || {
    printf 'V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE=INPUT_LIMIT_REFUSAL_MUTATED_STATE\n'
    exit 66
}

printf '\nV27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT=PASS\n'
printf 'NATIVE_INCREMENTAL_STRUCTURAL_GROUPING=PROVEN_IN_QA_SCOPE\n'
printf 'DYNAMIC_INPUT_DEPENDENCE=PASS\n'
printf 'NEGATIVE_COUNTEREXAMPLE=PASS\n'
printf 'PERSISTENT_STATE_INFLUENCES_LATER_VM_RUN=PASS\n'
printf 'FRESH_VM_PROCESS_REUSE=PASS\n'
printf 'DETERMINISTIC_REPLAY=PASS\n'
printf 'PARTIAL_STATE_COMMIT_FILTER=PASS\n'
printf 'STEP_LIMIT_STATUS=BOUNDED\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'HOST_GROUP_SELECTION=NO\n'
printf 'HOST_TOPIC_CLASSIFICATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'SEMANTIC_GROUPING=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'NEXT_ACTION=CHECKPOINT_V27P1_THEN_BUILD_V28_CURRICULUM_PRIORITY_PREFLIGHT\n'
