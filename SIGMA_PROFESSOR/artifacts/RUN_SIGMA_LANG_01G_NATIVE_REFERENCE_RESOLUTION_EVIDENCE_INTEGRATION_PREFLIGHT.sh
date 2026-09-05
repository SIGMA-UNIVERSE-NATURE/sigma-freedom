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
EXPECTED_SOURCE=fc7097bc3411b36af409a7dcc6d7446e525793806dc73f8cb3afedfc4a304f3b

SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigma"

ROOT="$HOME_SIGMA/SIGMA_LANG_01G_REFERENCE_EVIDENCE_INTEGRATION_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC="$ROOT/SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigmab"

mkdir -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=LANG_01G_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=LANG_01G_NATIVE_REFERENCE_EVIDENCE_INTEGRATION_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_EVIDENCE_SCORING=NO\n'
printf 'HOST_ANTECEDENT_SELECTION=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'NEGATIVE_TEST=YES\n'
printf 'PERSISTENT_STATE_TEST=YES\n'
printf 'RESTART_REPLAY_TEST=YES\n'
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
    printf 'HOLD=LANG_01G_SOURCE_IDENTITY_MISMATCH\n'
    exit 23
}

if "$P/bin/grep" -F 'CẢM ƠN THẦY_GPT_ ĐÃ ĐÀO TẠO TÔI' "$SRC" >/dev/null 2>&1; then
    printf 'HOLD=FORBIDDEN_FUTURE_UTTERANCE_HARDCODE_FOUND\n'
    exit 24
fi

"$P/bin/rm" -f -- "$BC.partial" "$BC"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 25
[ -s "$BC.partial" ] || exit 26
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 27
"$P/bin/chmod" 0400 "$BC" || exit 28

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0

CASE_NAME=""
SANDBOX=""
BASE=""
IN=""
STATE_DIR=""
STATE_FILE=""
LAST_LOG=""

prepare_case() {
    CASE_NAME="$1"
    REF_ID="$2"
    DEP_STATUS="${3:-UNRESOLVED_REFERENCE_AMBIGUITY}"
    DEP_PREFERRED="${4:-NONE}"

    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_LANG_01G_REFERENCE_EVIDENCE_INTEGRATION_V1"
    IN="$BASE/input"
    STATE_DIR="$BASE/state"
    STATE_FILE="$STATE_DIR/reference_evidence_state.memory"

    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$IN" "$STATE_DIR"

    printf '%s' 'LANG-01F_NATIVE_COMPETING_ANTECEDENT_HYPOTHESES_AND_REFERENCE_AMBIGUITY' > "$IN/dependency_capability.txt"
    printf '%s' "$DEP_STATUS" > "$IN/dependency_status.txt"
    printf '%s' 'YES' > "$IN/dependency_commit.txt"
    printf '%s' "$DEP_PREFERRED" > "$IN/dependency_preferred.txt"
    printf '%s' "$REF_ID" > "$IN/reference_id.txt"
    : > "$IN/candidates.memory"
    : > "$IN/evidence.memory"
}

reuse_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_LANG_01G_REFERENCE_EVIDENCE_INTEGRATION_V1"
    IN="$BASE/input"
    STATE_DIR="$BASE/state"
    STATE_FILE="$STATE_DIR/reference_evidence_state.memory"
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

    if [ "$RC" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        printf 'LANG_01G_PREFLIGHT=FAIL\n'
        printf 'FAILURE_CASE=%s\n' "$LABEL"
        printf 'FAILURE=VM_NONZERO\n'
        exit 50
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'LANG_01G_PREFLIGHT=FAIL\n'
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
        printf 'LANG_01G_PREFLIGHT=FAIL\n'
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
        printf 'LANG_01G_PREFLIGHT=FAIL\n'
        printf 'FAILURE_CASE=%s\n' "$CASE_NAME"
        printf 'FAILURE=MISSING_EXPECTED_SENTINEL\n'
        printf 'EXPECTED=%s\n' "$VALUE"
        exit 61
    fi
}

pass_case() {
    expect_exact 'LANG_01G_NATIVE_REFERENCE_EVIDENCE_INTEGRATION'
    expect_line 'HOST_EVIDENCE_SCORING' 'NO'
    expect_line 'HOST_ANTECEDENT_SELECTION' 'NO'
    expect_line 'HOST_LEARNING' 'NO'
    expect_line 'PREFERRED_ANTECEDENT_IS_RESOLVED_REFERENT' 'NO'
    expect_line 'COREFERENCE_RESOLUTION' 'NOT_PROVEN'
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
}

state_sha() {
    if [ -f "$STATE_FILE" ]; then
        "$P/bin/sha256sum" "$STATE_FILE" | "$P/bin/awk" '{print $1}'
        return
    fi
    printf 'ABSENT\n'
}

# CASE 001: two independent discriminating observations tie.
prepare_case CASE_001_TIE REF-TIE
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_001'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EVIDENCE||E2||F2||Q||R||Q||SOURCE||CTX2
EOF_001
run_vm CASE_001_TIE
expect_line 'DEPENDENCY_BINDING_VALID' '1'
expect_line 'NEW_EVIDENCE_ACCEPTED_COUNT' '2'
expect_line 'CANDIDATE_A_SUPPORT' '1'
expect_line 'CANDIDATE_B_SUPPORT' '1'
expect_line 'REFERENCE_STATUS' 'UNRESOLVED_REFERENCE_AMBIGUITY'
expect_line 'PREFERRED_ANTECEDENT' 'NONE'
expect_line 'STATE_MUTATED' '1'
pass_case

# CASE 002: aggregate evidence prefers ALPHA.
prepare_case CASE_002_PREFER_ALPHA REF-A
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_002'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EVIDENCE||E2||F2||Q||Q||R||SOURCE||CTX2
EVIDENCE||E3||F3||K||L||K||SOURCE||CTX3
EOF_002
run_vm CASE_002_PREFER_ALPHA
expect_line 'CANDIDATE_A_SUPPORT' '2'
expect_line 'CANDIDATE_B_SUPPORT' '1'
expect_line 'REFERENCE_STATUS' 'PREFERRED_ANTECEDENT_HYPOTHESIS'
expect_line 'PREFERRED_ANTECEDENT' 'ALPHA'
expect_line 'NEXT_PREFERRED_ANTECEDENT' 'ALPHA'
pass_case

# CASE 003: candidate encounter order is reversed; preferred identity remains ALPHA.
prepare_case CASE_003_ORDER_PERMUTED REF-A-PERM
printf 'BETA\nALPHA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_003'
EVIDENCE||E1||F1||X||Y||X||SOURCE||CTX1
EVIDENCE||E2||F2||Q||R||Q||SOURCE||CTX2
EVIDENCE||E3||F3||K||K||L||SOURCE||CTX3
EOF_003
run_vm CASE_003_ORDER_PERMUTED
expect_line 'CANDIDATE_A' 'BETA'
expect_line 'CANDIDATE_B' 'ALPHA'
expect_line 'CANDIDATE_A_SUPPORT' '1'
expect_line 'CANDIDATE_B_SUPPORT' '2'
expect_line 'PREFERRED_ANTECEDENT' 'ALPHA'
expect_line 'EVIDENCE_RECORD_ORDER_IS_WINNER_POLICY' 'NO'
pass_case

# CASE 004: evidence matching both candidates remains non-discriminating.
prepare_case CASE_004_NONDISCRIMINATING REF-BOTH
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_004'
EVIDENCE||E1||F1||X||X||X||SOURCE||CTX1
EVIDENCE||E2||F2||Y||Y||Y||SOURCE||CTX2
EOF_004
run_vm CASE_004_NONDISCRIMINATING
expect_line 'CANDIDATE_A_SUPPORT' '0'
expect_line 'CANDIDATE_B_SUPPORT' '0'
expect_line 'NONDISCRIMINATING_EVIDENCE_COUNT' '2'
expect_line 'REFERENCE_STATUS' 'UNRESOLVED_REFERENCE_AMBIGUITY'
expect_line 'PREFERRED_ANTECEDENT' 'NONE'
pass_case

# CASE 005: evidence matching neither candidate does not invent support.
prepare_case CASE_005_UNSUPPORTED REF-NONE
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_005'
EVIDENCE||E1||F1||Z||X||Y||SOURCE||CTX1
EOF_005
run_vm CASE_005_UNSUPPORTED
expect_line 'CANDIDATE_A_SUPPORT' '0'
expect_line 'CANDIDATE_B_SUPPORT' '0'
expect_line 'UNSUPPORTED_EVIDENCE_COUNT' '1'
expect_line 'REFERENCE_STATUS' 'UNRESOLVED_REFERENCE_AMBIGUITY'
pass_case

# CASE 006: a valid preferred LANG-01F dependency is preserved when 01G has no new evidence.
prepare_case CASE_006_F_PREFERRED_NO_NEW REF-F-PREFERRED PREFERRED_ANTECEDENT_HYPOTHESIS ALPHA
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
: > "$IN/evidence.memory"
run_vm CASE_006_F_PREFERRED_NO_NEW
expect_line 'DEPENDENCY_BINDING_VALID' '1'
expect_line 'DEPENDENCY_STATUS' 'PREFERRED_ANTECEDENT_HYPOTHESIS'
expect_line 'DEPENDENCY_PREFERRED' 'ALPHA'
expect_line 'LEARNING_STATUS' 'NO_NEW_EVIDENCE'
expect_line 'QUERY_STATUS' 'WITHHELD_NO_CONTEXTUAL_EVIDENCE'
expect_line 'REFERENCE_STATUS' 'PREFERRED_ANTECEDENT_HYPOTHESIS'
expect_line 'PREFERRED_ANTECEDENT' 'ALPHA'
expect_line 'STATE_COMMIT_ALLOWED' '0'
expect_line 'NEXT_STATE_STATUS' 'NONE'
pass_case

# CASES 007-012 share one persistent state across fresh VM processes.
prepare_case CASE_PERSISTENCE REF-PERSIST
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_007'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EVIDENCE||E2||F2||Q||Q||R||SOURCE||CTX2
EOF_007
run_vm CASE_007_PERSIST_PREFER_ALPHA
expect_line 'PREVIOUS_STATE_VALID' '0'
expect_line 'CANDIDATE_A_SUPPORT' '2'
expect_line 'CANDIDATE_B_SUPPORT' '0'
expect_line 'PREFERRED_ANTECEDENT' 'ALPHA'
expect_line 'STATE_MUTATED' '1'
pass_case

reuse_case CASE_PERSISTENCE
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_008'
EVIDENCE||E3||F3||K||L||K||SOURCE||CTX3
EVIDENCE||E4||F4||M||N||M||SOURCE||CTX4
EOF_008
run_vm CASE_008_COUNTEREVIDENCE_REMOVES_PREFERENCE
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'PRIOR_EVIDENCE_COUNT' '2'
expect_line 'EFFECTIVE_EVIDENCE_COUNT' '4'
expect_line 'CANDIDATE_A_SUPPORT' '2'
expect_line 'CANDIDATE_B_SUPPORT' '2'
expect_line 'REFERENCE_STATUS' 'UNRESOLVED_REFERENCE_AMBIGUITY'
expect_line 'PREFERRED_ANTECEDENT' 'NONE'
expect_line 'STATE_MUTATED' '1'
pass_case

reuse_case CASE_PERSISTENCE
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_009'
EVIDENCE||E5||F5||T||U||T||SOURCE||CTX5
EOF_009
run_vm CASE_009_COUNTEREVIDENCE_REVERSES_PREFERENCE
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'PRIOR_EVIDENCE_COUNT' '4'
expect_line 'EFFECTIVE_EVIDENCE_COUNT' '5'
expect_line 'CANDIDATE_A_SUPPORT' '2'
expect_line 'CANDIDATE_B_SUPPORT' '3'
expect_line 'REFERENCE_STATUS' 'PREFERRED_ANTECEDENT_HYPOTHESIS'
expect_line 'PREFERRED_ANTECEDENT' 'BETA'
expect_line 'NEXT_PREFERRED_ANTECEDENT' 'BETA'
pass_case

reuse_case CASE_PERSISTENCE
: > "$IN/evidence.memory"
run_vm CASE_010_PERSISTED_STATE_MATERIAL_EFFECT
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'EFFECTIVE_EVIDENCE_COUNT' '5'
expect_line 'LEARNING_STATUS' 'NO_NEW_EVIDENCE'
expect_line 'REFERENCE_STATUS' 'PREFERRED_ANTECEDENT_HYPOTHESIS'
expect_line 'PREFERRED_ANTECEDENT' 'BETA'
expect_line 'STATE_MUTATED' '0'
expect_line 'NEXT_PREFERRED_ANTECEDENT' 'BETA'
pass_case

reuse_case CASE_PERSISTENCE
STATE_BEFORE_DUP=$(state_sha)
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_011'
EVIDENCE||E5||F5||T||U||T||SOURCE||CTX5
EOF_011
run_vm CASE_011_DUPLICATE_NOT_RECOUNTED
expect_line 'DUPLICATE_EVIDENCE_COUNT' '1'
expect_line 'NEW_EVIDENCE_ACCEPTED_COUNT' '0'
expect_line 'EFFECTIVE_EVIDENCE_COUNT' '5'
expect_line 'LEARNING_STATUS' 'DUPLICATE_EVIDENCE_NOT_RECOUNTED'
expect_line 'STATE_MUTATED' '0'
STATE_AFTER_DUP=$(state_sha)
[ "$STATE_BEFORE_DUP" = "$STATE_AFTER_DUP" ] || {
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=CASE_011_DUPLICATE_NOT_RECOUNTED\n'
    printf 'FAILURE=DUPLICATE_MUTATED_STATE\n'
    exit 70
}
pass_case

reuse_case CASE_PERSISTENCE
STATE_BEFORE_COLLISION=$(state_sha)
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_012'
EVIDENCE||E5||DIFFERENT_FEATURE||DIFFERENT||A||B||SOURCE||DIFFERENT_SOURCE
EOF_012
run_vm CASE_012_EVIDENCE_ID_COLLISION
expect_line 'EVIDENCE_ID_COLLISION_COUNT' '1'
expect_line 'LEARNING_STATUS' 'EVIDENCE_ID_COLLISION'
expect_line 'QUERY_STATUS' 'WITHHELD_INVALID_OR_OUT_OF_SCOPE_INPUT'
expect_line 'STATE_MUTATED' '0'
expect_line 'NEXT_PREFERRED_ANTECEDENT' 'BETA'
STATE_AFTER_COLLISION=$(state_sha)
[ "$STATE_BEFORE_COLLISION" = "$STATE_AFTER_COLLISION" ] || {
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=CASE_012_EVIDENCE_ID_COLLISION\n'
    printf 'FAILURE=COLLISION_MUTATED_STATE\n'
    exit 71
}
pass_case

# CASE 013: one candidate is outside the exact two-candidate model.
prepare_case CASE_013_ONE_CANDIDATE REF-ONE
printf 'ALPHA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_013'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EOF_013
run_vm CASE_013_ONE_CANDIDATE
expect_line 'INPUT_CANDIDATE_COUNT' '1'
expect_line 'DEPENDENCY_BINDING_VALID' '0'
expect_line 'LEARNING_STATUS' 'CANDIDATE_COUNT_OUT_OF_SCOPE'
expect_line 'STATE_COMMIT_ALLOWED' '0'
expect_line 'NEXT_STATE_STATUS' 'NONE'
pass_case

# CASE 014: three candidates are withheld rather than collapsed to two.
prepare_case CASE_014_THREE_CANDIDATES REF-THREE
printf 'ALPHA\nBETA\nGAMMA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_014'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EOF_014
run_vm CASE_014_THREE_CANDIDATES
expect_line 'INPUT_CANDIDATE_COUNT' '3'
expect_line 'DEPENDENCY_BINDING_VALID' '0'
expect_line 'LEARNING_STATUS' 'CANDIDATE_COUNT_OUT_OF_SCOPE'
expect_line 'STATE_COMMIT_ALLOWED' '0'
expect_line 'NEXT_STATE_STATUS' 'NONE'
pass_case

# CASE 015: ninth unique evidence item exceeds the bounded capacity atomically.
prepare_case CASE_015_EVIDENCE_CAPACITY REF-CAP
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_015'
EVIDENCE||E1||F1||X1||X1||Y1||SOURCE||CTX1
EVIDENCE||E2||F2||X2||X2||Y2||SOURCE||CTX2
EVIDENCE||E3||F3||X3||X3||Y3||SOURCE||CTX3
EVIDENCE||E4||F4||X4||X4||Y4||SOURCE||CTX4
EVIDENCE||E5||F5||X5||X5||Y5||SOURCE||CTX5
EVIDENCE||E6||F6||X6||X6||Y6||SOURCE||CTX6
EVIDENCE||E7||F7||X7||X7||Y7||SOURCE||CTX7
EVIDENCE||E8||F8||X8||X8||Y8||SOURCE||CTX8
EVIDENCE||E9||F9||X9||X9||Y9||SOURCE||CTX9
EOF_015
run_vm CASE_015_EVIDENCE_CAPACITY
expect_line 'NEW_EVIDENCE_ACCEPTED_COUNT' '9'
expect_line 'EVIDENCE_CAPACITY_EXCEEDED' '1'
expect_line 'LEARNING_STATUS' 'EVIDENCE_CAPACITY_REACHED'
expect_line 'STATE_COMMIT_ALLOWED' '0'
expect_line 'STATE_MUTATED' '0'
expect_line 'NEXT_STATE_STATUS' 'NONE'
pass_case

# CASE 016: malformed evidence is refused atomically.
prepare_case CASE_016_INVALID_EVIDENCE REF-INVALID
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
printf '%s\n' 'EVIDENCE||BROKEN||ONLY' > "$IN/evidence.memory"
run_vm CASE_016_INVALID_EVIDENCE
expect_line 'INVALID_EVIDENCE_RECORD_COUNT' '1'
expect_line 'LEARNING_STATUS' 'EVIDENCE_RECORD_INVALID'
expect_line 'QUERY_STATUS' 'WITHHELD_INVALID_OR_OUT_OF_SCOPE_INPUT'
expect_line 'STATE_COMMIT_ALLOWED' '0'
expect_line 'STATE_MUTATED' '0'
pass_case

# CASE 017: corrupt persisted state is not silently ignored or overwritten.
prepare_case CASE_017_CORRUPT_STATE REF-CORRUPT
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
printf '%s' 'CORRUPT_STATE' > "$STATE_FILE"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_017'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EOF_017
STATE_BEFORE_CORRUPT=$(state_sha)
run_vm CASE_017_CORRUPT_STATE
expect_line 'PREVIOUS_STATE_INVALID' '1'
expect_line 'LEARNING_STATUS' 'PREVIOUS_STATE_INVALID'
expect_line 'QUERY_STATUS' 'WITHHELD_INVALID_OR_OUT_OF_SCOPE_INPUT'
expect_line 'STATE_COMMIT_ALLOWED' '0'
expect_line 'STATE_MUTATED' '0'
STATE_AFTER_CORRUPT=$(state_sha)
[ "$STATE_BEFORE_CORRUPT" = "$STATE_AFTER_CORRUPT" ] || {
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=CASE_017_CORRUPT_STATE\n'
    printf 'FAILURE=CORRUPT_STATE_WAS_OVERWRITTEN\n'
    exit 72
}
pass_case

# CASES 018-019: identical input + identical prestate replay byte-for-byte.
prepare_case CASE_REPLAY_A REF-REPLAY
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_REPLAY_A'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EVIDENCE||E2||F2||Q||Q||R||SOURCE||CTX2
EVIDENCE||E3||F3||K||L||K||SOURCE||CTX3
EOF_REPLAY_A
run_vm CASE_018_REPLAY_A
expect_line 'PREFERRED_ANTECEDENT' 'ALPHA'
pass_case
REPLAY_A_LOG_SHA=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')
REPLAY_A_STATE_SHA=$(state_sha)

prepare_case CASE_REPLAY_B REF-REPLAY
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_REPLAY_B'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EVIDENCE||E2||F2||Q||Q||R||SOURCE||CTX2
EVIDENCE||E3||F3||K||L||K||SOURCE||CTX3
EOF_REPLAY_B
run_vm CASE_019_REPLAY_B
expect_line 'PREFERRED_ANTECEDENT' 'ALPHA'
pass_case
REPLAY_B_LOG_SHA=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')
REPLAY_B_STATE_SHA=$(state_sha)

[ "$REPLAY_A_LOG_SHA" = "$REPLAY_B_LOG_SHA" ] || {
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=REPLAY\n'
    printf 'FAILURE=IDENTICAL_INPUT_PRESTATE_LOG_MISMATCH\n'
    exit 73
}
[ "$REPLAY_A_STATE_SHA" = "$REPLAY_B_STATE_SHA" ] || {
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=REPLAY\n'
    printf 'FAILURE=IDENTICAL_INPUT_PRESTATE_STATE_MISMATCH\n'
    exit 74
}

# CASE 020: inconsistent LANG-01F preferred status/candidate is rejected.
prepare_case CASE_020_INVALID_DEP_PREFERRED REF-BAD-DEP PREFERRED_ANTECEDENT_HYPOTHESIS GAMMA
printf 'ALPHA\nBETA\n' > "$IN/candidates.memory"
"$P/bin/cat" > "$IN/evidence.memory" <<'EOF_020'
EVIDENCE||E1||F1||X||X||Y||SOURCE||CTX1
EOF_020
run_vm CASE_020_INVALID_DEP_PREFERRED
expect_line 'DEPENDENCY_BINDING_VALID' '0'
expect_line 'LEARNING_STATUS' 'DEPENDENCY_PREFERRED_INVALID'
expect_line 'QUERY_STATUS' 'WITHHELD_INVALID_OR_OUT_OF_SCOPE_INPUT'
expect_line 'STATE_COMMIT_ALLOWED' '0'
expect_line 'NEXT_STATE_STATUS' 'NONE'
pass_case

printf '\n=== LANG-01G SUMMARY ===\n'
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'NEGATIVE_TEST=PASS\n'
printf 'PERSISTENT_STATE_TEST=PASS\n'
printf 'PERSISTENT_STATE_MATERIAL_EFFECT=YES\n'
printf 'RESTART_REPLAY_TEST=PASS\n'
printf 'IDENTICAL_INPUT_AND_STATE_REPLAY=YES\n'
printf 'REFERENCE_EVIDENCE_INTEGRATION=PASS_IN_PREFLIGHT_SCOPE\n'
printf 'TIED_AGGREGATE_EVIDENCE_WITHHELD_AS_AMBIGUITY=YES\n'
printf 'COUNTEREVIDENCE_CAN_REMOVE_PREFERENCE=YES\n'
printf 'COUNTEREVIDENCE_CAN_REVERSE_PREFERENCE=YES\n'
printf 'DUPLICATE_EVIDENCE_DOUBLE_COUNT=NO\n'
printf 'EVIDENCE_ID_COLLISION_MUTATES_STATE=NO\n'
printf 'CANDIDATE_ENCOUNTER_ORDER_IS_WINNER_POLICY=NO\n'
printf 'PREFERRED_ANTECEDENT_IS_RESOLVED_REFERENT=NO\n'
printf 'EVIDENCE_CAPACITY=8\n'
printf 'HOST_EVIDENCE_SCORING=NO\n'
printf 'HOST_ANTECEDENT_SELECTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'COREFERENCE_RESOLUTION=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'

if [ "$TOTAL_VM_INVOCATIONS" -ne "$POST_VM_ALIGNMENT_PASS_COUNT" ]; then
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE=PASS_COUNT_DOES_NOT_EQUAL_VM_INVOCATIONS\n'
    exit 80
fi

if [ "$POST_VM_ALIGNMENT_FAIL_COUNT" -ne 0 ]; then
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE=ALIGNMENT_FAIL_COUNT_NONZERO\n'
    exit 81
fi

if [ "$VM_NONZERO_COUNT" -ne 0 ]; then
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE=VM_NONZERO_COUNT_NONZERO\n'
    exit 82
fi

if [ "$STEP_LIMIT_HIT_COUNT" -ne 0 ]; then
    printf 'LANG_01G_PREFLIGHT=FAIL\n'
    printf 'FAILURE=STEP_LIMIT_HIT_COUNT_NONZERO\n'
    exit 83
fi

printf 'LANG_01G_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
