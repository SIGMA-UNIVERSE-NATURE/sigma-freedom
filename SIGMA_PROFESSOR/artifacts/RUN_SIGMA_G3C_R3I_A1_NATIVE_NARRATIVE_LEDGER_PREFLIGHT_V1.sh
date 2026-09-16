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
EXPECTED_SOURCE=582e7c32514093808e9be870a73669fd0c3280a4ea28a92f2828b710625bf035

SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_G3C_R3I_A1_NATIVE_NARRATIVE_LEDGER_STATE_REVISION_V1.sigma"

SESSION_ARTIFACT_ROOT="${ARTIFACT_ROOT:-}"
if [ -z "$SESSION_ARTIFACT_ROOT" ]; then
    printf 'HOLD=ARTIFACT_ROOT_NOT_EXPORTED_BY_GRANTED_SIGMA_SESSION\n'
    exit 20
fi

ROOT="$SESSION_ARTIFACT_ROOT/SIGMA_G3C_R3I_A1_NATIVE_NARRATIVE_LEDGER_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC="$ROOT/SIGMA_G3C_R3I_A1_NATIVE_NARRATIVE_LEDGER_STATE_REVISION_V1.sigmab"

mkdir -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=R3I_A1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 21
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=G3C_R3I_A1_NATIVE_NARRATIVE_LEDGER_PREFLIGHT\n'
printf 'SESSION_ARTIFACT_ROOT=%s\n' "$SESSION_ARTIFACT_ROOT"
printf 'HOST_COGNITION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_STATE_REVISION_DECISION=NO\n'
printf 'DYNAMIC_INPUT_GENERATED_AFTER_COMPILE=YES\n'
printf 'NEGATIVE_TEST=YES\n'
printf 'PERSISTENT_STATE_TEST=YES\n'
printf 'RESTART_REPLAY_TEST=YES\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || {
    printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'
    exit 22
}
[ "$actual_vm" = "$EXPECTED_VM" ] || {
    printf 'HOLD=VM_IDENTITY_MISMATCH\n'
    exit 23
}
[ "$actual_source" = "$EXPECTED_SOURCE" ] || {
    printf 'HOLD=R3I_A1_SOURCE_IDENTITY_MISMATCH\n'
    exit 24
}

# Static anti-hardcode sanity: human semantic role labels are not allowed as
# runtime role answers in this structural capability.
for forbidden in '||AGENT||' '||PATIENT||' '||EXPERIENCER||'; do
    if "$P/bin/grep" -F "$forbidden" "$SRC" >/dev/null 2>&1; then
        printf 'HOLD=FORBIDDEN_HUMAN_ROLE_LABEL_FOUND\n'
        exit 25
    fi
done

"$P/bin/rm" -f -- "$BC.partial" "$BC"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 26
[ -s "$BC.partial" ] || exit 27
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 28
"$P/bin/chmod" 0400 "$BC" || exit 29

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

# Only after source/bytecode freeze do we generate high-entropy fixture IDs.
DYNAMIC_SEED=$(printf '%s:%s:%s' "$$" "$("$P/bin/date" +%s)" "$("$P/bin/date" +%N)" \
    | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')
DYNAMIC_TOKEN=${DYNAMIC_SEED%%????????????????????????????????????????????????}
printf 'DYNAMIC_TOKEN_SHA256=%s\n' \
    "$(printf '%s' "$DYNAMIC_TOKEN" | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')"

STORY="STORY_$DYNAMIC_TOKEN"
STATE_KEY="STATE_$DYNAMIC_TOKEN"
A="VALUE_A_$DYNAMIC_TOKEN"
B="VALUE_B_$DYNAMIC_TOKEN"
C="VALUE_C_$DYNAMIC_TOKEN"
E1="EVENT_1_$DYNAMIC_TOKEN"
E2="EVENT_2_$DYNAMIC_TOKEN"
P1="PARTICIPANT_1_$DYNAMIC_TOKEN"
ROLE="ROLE_SLOT_$DYNAMIC_TOKEN"
SRC1="SOURCE_1_$DYNAMIC_TOKEN"
SRC2="SOURCE_2_$DYNAMIC_TOKEN"

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
STATE_IMMUTABILITY_PASS_COUNT=0

CASE_NAME=""
SANDBOX=""
BASE=""
IN=""
STATE_DIR=""
STATE_FILE=""
LAST_LOG=""

prepare_case() {
    CASE_NAME="$1"
    STORY_VALUE="${2:-$STORY}"

    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_G3C_R3I_A1_NARRATIVE_LEDGER_STATE_REVISION_V1"
    IN="$BASE/input"
    STATE_DIR="$BASE/state"
    STATE_FILE="$STATE_DIR/narrative_ledger.memory"

    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$IN" "$STATE_DIR"

    # Mechanical fresh-state representation: zero-length file, matching the
    # proven locked-VM handling pattern for read_text + str_split pipelines.
    : > "$STATE_FILE"
    printf '%s' "$STORY_VALUE" > "$IN/story_id.txt"
    printf '%s' "$STATE_KEY" > "$IN/query_state_key.txt"
    printf '%s\n%s\n' "$A" "$B" > "$IN/query_candidates.memory"
    : > "$IN/records.memory"
}

reuse_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_G3C_R3I_A1_NARRATIVE_LEDGER_STATE_REVISION_V1"
    IN="$BASE/input"
    STATE_DIR="$BASE/state"
    STATE_FILE="$STATE_DIR/narrative_ledger.memory"
}

run_vm() {
    LABEL="$1"
    LAST_LOG="$LOG/$LABEL.log"
    TOTAL_VM_INVOCATIONS=$((TOTAL_VM_INVOCATIONS + 1))

    (
        cd "$SANDBOX" || exit 90
        "$VM" "$BC"
    ) >"$LAST_LOG" 2>&1
    RC=$?

    printf '\n=== %s ===\n' "$LABEL"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$LAST_LOG"
    printf 'CASE_%s_POST_VM_TEST_ORACLE_STARTED=YES\n' "$LABEL"

    if [ "$RC" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        printf 'R3I_A1_PREFLIGHT=FAIL\n'
        printf 'FAILURE_CASE=%s\n' "$LABEL"
        printf 'FAILURE=VM_NONZERO\n'
        exit 50
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'R3I_A1_PREFLIGHT=FAIL\n'
        printf 'FAILURE_CASE=%s\n' "$LABEL"
        printf 'FAILURE=STEP_LIMIT_HIT\n'
        exit 51
    fi
}

expect_line() {
    KEY="$1"
    VALUE="$2"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'R3I_A1_PREFLIGHT=FAIL\n'
        printf 'FAILURE_CASE=%s\n' "$CASE_NAME"
        printf 'FAILURE=MISSING_EXPECTED_OUTPUT\n'
        printf 'EXPECTED=%s %s\n' "$KEY" "$VALUE"
        exit 60
    fi
}

expect_exact() {
    VALUE="$1"
    if ! "$P/bin/grep" -F -x "$VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'R3I_A1_PREFLIGHT=FAIL\n'
        printf 'FAILURE_CASE=%s\n' "$CASE_NAME"
        printf 'FAILURE=MISSING_EXPECTED_SENTINEL\n'
        printf 'EXPECTED=%s\n' "$VALUE"
        exit 61
    fi
}

pass_case() {
    expect_exact 'G3C_R3I_A1_NATIVE_NARRATIVE_LEDGER_STATE_REVISION'
    expect_line 'ORDER_EDGE_IS_CAUSAL_EDGE' 'NO'
    expect_line 'ROLE_SLOT_IS_HUMAN_SEMANTIC_ROLE' 'NO'
    expect_line 'PREFERRED_STATE_IS_PROVEN_TRUTH' 'NO'
    expect_line 'HOST_COGNITION' 'NO'
    expect_line 'HOST_STATE_REVISION_DECISION' 'NO'
    expect_line 'HOST_SEMANTIC_INTERPRETATION' 'NO'
    expect_line 'SEMANTIC_UNDERSTANDING' 'NOT_PROVEN'
    expect_line 'WHOLE_STORY_UNDERSTANDING' 'NOT_PROVEN'
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
}

state_sha() {
    if [ -f "$STATE_FILE" ]; then
        "$P/bin/sha256sum" "$STATE_FILE" | "$P/bin/awk" '{print $1}'
        return
    fi
    printf 'ABSENT\n'
}

# CASE 001: initialize a structural story ledger and a preferred state.
prepare_case CASE_PERSISTENCE
"$P/bin/cat" > "$IN/records.memory" <<EOF_001
EVENT||R_EVT1_$DYNAMIC_TOKEN||$E1||SOURCE||$SRC1
EVENT||R_EVT2_$DYNAMIC_TOKEN||$E2||SOURCE||$SRC2
PARTICIPANT||R_P1_$DYNAMIC_TOKEN||$P1||SOURCE||$SRC1
ROLE_BINDING||R_ROLE1_$DYNAMIC_TOKEN||$E1||$P1||$ROLE||SOURCE||$SRC1
ORDER_EDGE||R_ORDER1_$DYNAMIC_TOKEN||$E1||$E2||SOURCE||$SRC2
STATE_EVIDENCE||R_SA1_$DYNAMIC_TOKEN||$STATE_KEY||$A||$E1||SOURCE||$SRC1
STATE_EVIDENCE||R_SA2_$DYNAMIC_TOKEN||$STATE_KEY||$A||$E2||SOURCE||$SRC2
STATE_EVIDENCE||R_SB1_$DYNAMIC_TOKEN||$STATE_KEY||$B||$E2||SOURCE||$SRC2
EOF_001
run_vm CASE_001_INITIAL_STATE
expect_line 'QUERY_BINDING_VALID' '1'
expect_line 'NEW_RECORD_ACCEPTED_COUNT' '8'
expect_line 'NEW_REFERENCE_INVALID_COUNT' '0'
expect_line 'CURRENT_QUERY_A_SUPPORT' '2'
expect_line 'CURRENT_QUERY_B_SUPPORT' '1'
expect_line 'CURRENT_PREFERRED_STATE' "$A"
expect_line 'REVISION_KIND' 'INITIAL_STATE_HYPOTHESIS'
expect_line 'STATE_MUTATED' '1'
pass_case

# CASE 002: fresh VM + persisted state; counterevidence reopens uncertainty.
reuse_case CASE_PERSISTENCE
"$P/bin/cat" > "$IN/records.memory" <<EOF_002
STATE_EVIDENCE||R_SB2_$DYNAMIC_TOKEN||$STATE_KEY||$B||$E2||SOURCE||$SRC2
EOF_002
run_vm CASE_002_COUNTEREVIDENCE_REOPENS
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'PRIOR_QUERY_A_SUPPORT' '2'
expect_line 'PRIOR_QUERY_B_SUPPORT' '1'
expect_line 'CURRENT_QUERY_A_SUPPORT' '2'
expect_line 'CURRENT_QUERY_B_SUPPORT' '2'
expect_line 'CURRENT_STATE_STATUS' 'UNRESOLVED_STATE_COMPETITION'
expect_line 'CURRENT_PREFERRED_STATE' 'NONE'
expect_line 'REVISION_KIND' 'PREFERENCE_REOPENED'
expect_line 'STATE_MUTATED' '1'
pass_case

# CASE 003: additional counterevidence reverses the preferred state hypothesis.
reuse_case CASE_PERSISTENCE
"$P/bin/cat" > "$IN/records.memory" <<EOF_003
STATE_EVIDENCE||R_SB3_$DYNAMIC_TOKEN||$STATE_KEY||$B||$E1||SOURCE||$SRC1
EOF_003
run_vm CASE_003_COUNTEREVIDENCE_REVERSES
expect_line 'PRIOR_STATE_STATUS' 'UNRESOLVED_STATE_COMPETITION'
expect_line 'CURRENT_QUERY_A_SUPPORT' '2'
expect_line 'CURRENT_QUERY_B_SUPPORT' '3'
expect_line 'CURRENT_STATE_STATUS' 'PREFERRED_STATE_HYPOTHESIS'
expect_line 'CURRENT_PREFERRED_STATE' "$B"
expect_line 'REVISION_KIND' 'PREFERENCE_EMERGED'
expect_line 'STATE_MUTATED' '1'
pass_case

# CASE 004: exact duplicate is idempotent and does not mutate state.
reuse_case CASE_PERSISTENCE
before_sha=$(state_sha)
"$P/bin/cat" > "$IN/records.memory" <<EOF_004
STATE_EVIDENCE||R_SB3_$DYNAMIC_TOKEN||$STATE_KEY||$B||$E1||SOURCE||$SRC1
EOF_004
run_vm CASE_004_DUPLICATE_IDEMPOTENT
after_sha=$(state_sha)
expect_line 'DUPLICATE_RECORD_COUNT' '1'
expect_line 'NEW_RECORD_ACCEPTED_COUNT' '0'
expect_line 'STATE_MUTATED' '0'
expect_line 'CURRENT_PREFERRED_STATE' "$B"
[ "$before_sha" = "$after_sha" ] || {
    printf 'R3I_A1_PREFLIGHT=FAIL\nFAILURE_CASE=CASE_004_DUPLICATE_IDEMPOTENT\nFAILURE=STATE_CHANGED_ON_DUPLICATE\n'
    exit 62
}
STATE_IMMUTABILITY_PASS_COUNT=$((STATE_IMMUTABILITY_PASS_COUNT + 1))
pass_case

# CASE 005: same record ID with different fingerprint fails closed.
reuse_case CASE_PERSISTENCE
before_sha=$(state_sha)
"$P/bin/cat" > "$IN/records.memory" <<EOF_005
STATE_EVIDENCE||R_SB3_$DYNAMIC_TOKEN||$STATE_KEY||$A||$E1||SOURCE||$SRC1
EOF_005
run_vm CASE_005_RECORD_ID_COLLISION
after_sha=$(state_sha)
expect_line 'RECORD_ID_COLLISION_COUNT' '1'
expect_line 'BATCH_VALID' '0'
expect_line 'INFERENCE_ALLOWED' '0'
expect_line 'STATE_MUTATED' '0'
[ "$before_sha" = "$after_sha" ] || {
    printf 'R3I_A1_PREFLIGHT=FAIL\nFAILURE_CASE=CASE_005_RECORD_ID_COLLISION\nFAILURE=STATE_CHANGED_ON_COLLISION\n'
    exit 63
}
STATE_IMMUTABILITY_PASS_COUNT=$((STATE_IMMUTABILITY_PASS_COUNT + 1))
pass_case

# CASE 006: role binding to an unknown participant fails closed.
reuse_case CASE_PERSISTENCE
before_sha=$(state_sha)
"$P/bin/cat" > "$IN/records.memory" <<EOF_006
ROLE_BINDING||R_BAD_ROLE_$DYNAMIC_TOKEN||$E1||MISSING_PARTICIPANT_$DYNAMIC_TOKEN||$ROLE||SOURCE||$SRC1
EOF_006
run_vm CASE_006_UNKNOWN_PARTICIPANT
after_sha=$(state_sha)
expect_line 'NEW_REFERENCE_INVALID_COUNT' '1'
expect_line 'BATCH_VALID' '0'
expect_line 'STATE_MUTATED' '0'
[ "$before_sha" = "$after_sha" ] || exit 64
STATE_IMMUTABILITY_PASS_COUNT=$((STATE_IMMUTABILITY_PASS_COUNT + 1))
pass_case

# CASE 007: state evidence tied to an unknown event fails closed.
reuse_case CASE_PERSISTENCE
before_sha=$(state_sha)
"$P/bin/cat" > "$IN/records.memory" <<EOF_007
STATE_EVIDENCE||R_BAD_STATE_$DYNAMIC_TOKEN||$STATE_KEY||$A||MISSING_EVENT_$DYNAMIC_TOKEN||SOURCE||$SRC1
EOF_007
run_vm CASE_007_UNKNOWN_EVENT_STATE_EVIDENCE
after_sha=$(state_sha)
expect_line 'NEW_REFERENCE_INVALID_COUNT' '1'
expect_line 'BATCH_VALID' '0'
expect_line 'STATE_MUTATED' '0'
[ "$before_sha" = "$after_sha" ] || exit 65
STATE_IMMUTABILITY_PASS_COUNT=$((STATE_IMMUTABILITY_PASS_COUNT + 1))
pass_case

# CASE 008: order edge to an unknown event fails closed.
reuse_case CASE_PERSISTENCE
before_sha=$(state_sha)
"$P/bin/cat" > "$IN/records.memory" <<EOF_008
ORDER_EDGE||R_BAD_ORDER_$DYNAMIC_TOKEN||$E1||MISSING_EVENT_$DYNAMIC_TOKEN||SOURCE||$SRC1
EOF_008
run_vm CASE_008_UNKNOWN_EVENT_ORDER_EDGE
after_sha=$(state_sha)
expect_line 'NEW_REFERENCE_INVALID_COUNT' '1'
expect_line 'BATCH_VALID' '0'
expect_line 'STATE_MUTATED' '0'
[ "$before_sha" = "$after_sha" ] || exit 66
STATE_IMMUTABILITY_PASS_COUNT=$((STATE_IMMUTABILITY_PASS_COUNT + 1))
pass_case

# CASE 009: reflexive order edge is rejected; order is not causality.
reuse_case CASE_PERSISTENCE
before_sha=$(state_sha)
"$P/bin/cat" > "$IN/records.memory" <<EOF_009
ORDER_EDGE||R_SELF_ORDER_$DYNAMIC_TOKEN||$E1||$E1||SOURCE||$SRC1
EOF_009
run_vm CASE_009_REFLEXIVE_ORDER_REJECTED
after_sha=$(state_sha)
expect_line 'NEW_REFERENCE_INVALID_COUNT' '1'
expect_line 'STATE_MUTATED' '0'
expect_line 'ORDER_EDGE_IS_CAUSAL_EDGE' 'NO'
[ "$before_sha" = "$after_sha" ] || exit 67
STATE_IMMUTABILITY_PASS_COUNT=$((STATE_IMMUTABILITY_PASS_COUNT + 1))
pass_case

# CASE 010: query candidate encounter order changes, preferred identity does not.
reuse_case CASE_PERSISTENCE
printf '%s\n%s\n' "$B" "$A" > "$IN/query_candidates.memory"
: > "$IN/records.memory"
run_vm CASE_010_QUERY_ORDER_PERMUTED
expect_line 'QUERY_CANDIDATE_A' "$B"
expect_line 'QUERY_CANDIDATE_B' "$A"
expect_line 'CURRENT_QUERY_A_SUPPORT' '3'
expect_line 'CURRENT_QUERY_B_SUPPORT' '2'
expect_line 'CURRENT_PREFERRED_STATE' "$B"
expect_line 'STATE_MUTATED' '0'
pass_case
printf '%s\n%s\n' "$A" "$B" > "$IN/query_candidates.memory"

# CASE 011: evidence for a third opaque value preserves A/B uncertainty.
prepare_case CASE_OTHER_VALUE
"$P/bin/cat" > "$IN/records.memory" <<EOF_011
EVENT||R_EVT_OTHER_$DYNAMIC_TOKEN||$E1||SOURCE||$SRC1
STATE_EVIDENCE||R_SC1_$DYNAMIC_TOKEN||$STATE_KEY||$C||$E1||SOURCE||$SRC1
EOF_011
run_vm CASE_011_OTHER_VALUE_UNRESOLVED
expect_line 'CURRENT_QUERY_EVIDENCE_COUNT' '1'
expect_line 'CURRENT_QUERY_A_SUPPORT' '0'
expect_line 'CURRENT_QUERY_B_SUPPORT' '0'
expect_line 'CURRENT_QUERY_OTHER_SUPPORT' '1'
expect_line 'CURRENT_STATE_STATUS' 'UNRESOLVED_STATE_COMPETITION'
expect_line 'CURRENT_PREFERRED_STATE' 'NONE'
pass_case

# CASE 012: persisted story state refuses a different story ID.
reuse_case CASE_PERSISTENCE
before_sha=$(state_sha)
printf '%s' "OTHER_STORY_$DYNAMIC_TOKEN" > "$IN/story_id.txt"
: > "$IN/records.memory"
run_vm CASE_012_STORY_ID_MISMATCH
after_sha=$(state_sha)
expect_line 'PREVIOUS_STATE_INVALID' '1'
expect_line 'INFERENCE_ALLOWED' '0'
expect_line 'STATE_MUTATED' '0'
[ "$before_sha" = "$after_sha" ] || exit 68
STATE_IMMUTABILITY_PASS_COUNT=$((STATE_IMMUTABILITY_PASS_COUNT + 1))
pass_case
printf '%s' "$STORY" > "$IN/story_id.txt"

# CASE 013: malformed record is rejected with no state mutation.
reuse_case CASE_PERSISTENCE
before_sha=$(state_sha)
printf '%s\n' "EVENT||BROKEN_$DYNAMIC_TOKEN" > "$IN/records.memory"
run_vm CASE_013_MALFORMED_RECORD
after_sha=$(state_sha)
expect_line 'INVALID_NEW_RECORD_COUNT' '1'
expect_line 'BATCH_VALID' '0'
expect_line 'STATE_MUTATED' '0'
[ "$before_sha" = "$after_sha" ] || exit 69
STATE_IMMUTABILITY_PASS_COUNT=$((STATE_IMMUTABILITY_PASS_COUNT + 1))
pass_case

# CASE 014: exact same complete input/state replay is deterministic.
reuse_case CASE_PERSISTENCE
: > "$IN/records.memory"
run_vm CASE_014_REPLAY_A
replay_a_sha=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')
run_vm CASE_014_REPLAY_B
replay_b_sha=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')
# Log filenames differ, contents must be byte-identical.
[ "$replay_a_sha" = "$replay_b_sha" ] || {
    printf 'R3I_A1_PREFLIGHT=FAIL\nFAILURE_CASE=CASE_014_REPLAY\nFAILURE=NONDETERMINISTIC_IDENTICAL_STATE_INPUT\n'
    exit 70
}
expect_line 'CURRENT_PREFERRED_STATE' "$B"
expect_line 'STATE_MUTATED' '0'
pass_case
REPLAY_IDENTICAL_INPUT_STATE_OUTPUT=YES

SOURCE_AFTER=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
BYTECODE_AFTER=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')

SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
[ "$SOURCE_AFTER" = "$EXPECTED_SOURCE" ] && SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
[ "$BYTECODE_AFTER" = "$BYTECODE_SHA" ] && BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES

TOKEN_LEAK_SOURCE=$("$P/bin/grep" -aF -c "$DYNAMIC_TOKEN" "$SRC" 2>/dev/null || true)
TOKEN_LEAK_BYTECODE=$("$P/bin/grep" -aF -c "$DYNAMIC_TOKEN" "$BC" 2>/dev/null || true)
TOKEN_LEAK_TOTAL=$((TOKEN_LEAK_SOURCE + TOKEN_LEAK_BYTECODE))

printf '\n=== R3I A1 PREFLIGHT SUMMARY ===\n'
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'STATE_IMMUTABILITY_PASS_COUNT=%s\n' "$STATE_IMMUTABILITY_PASS_COUNT"
printf 'REPLAY_IDENTICAL_INPUT_STATE_OUTPUT=%s\n' "$REPLAY_IDENTICAL_INPUT_STATE_OUTPUT"
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=%s\n' "$TOKEN_LEAK_TOTAL"
printf 'HOST_COGNITION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'CANONICAL_MUTATION=NO\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'WHOLE_STORY_UNDERSTANDING=NOT_PROVEN\n'
printf 'G3_PROMOTION=NO\n'

[ "$TOTAL_VM_INVOCATIONS" -eq 15 ] || exit 80
[ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 14 ] || exit 81
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || exit 82
[ "$VM_NONZERO_COUNT" -eq 0 ] || exit 83
[ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] || exit 84
[ "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || exit 85
[ "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || exit 86
[ "$TOKEN_LEAK_TOTAL" -eq 0 ] || exit 87
[ "$REPLAY_IDENTICAL_INPUT_STATE_OUTPUT" = YES ] || exit 88

printf 'R3I_A1_PREFLIGHT=PASS_IN_EXACT_TESTED_STRUCTURAL_SCOPE\n'
