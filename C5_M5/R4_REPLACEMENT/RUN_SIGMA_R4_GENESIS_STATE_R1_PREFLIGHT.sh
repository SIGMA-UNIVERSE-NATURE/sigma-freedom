#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA

if [ -n "${SIGMA_REPO:-}" ]; then
    REPO="$SIGMA_REPO"
elif [ -f "$HOME_SIGMA/sigma-freedom-write/C5_M5/R4_REPLACEMENT/SIGMA_R4_GENESIS_STATE_R1.sigma" ]; then
    REPO="$HOME_SIGMA/sigma-freedom-write"
else
    REPO="$HOME_SIGMA/sigma_genesis1"
fi

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
EXPECTED_SOURCE_GIT_BLOB=fe158389a60315849d9752d9676e983b74acab35

SRC="$REPO/C5_M5/R4_REPLACEMENT/SIGMA_R4_GENESIS_STATE_R1.sigma"
ROOT="$HOME_SIGMA/SIGMA_R4_GENESIS_STATE_R1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC="$ROOT/SIGMA_R4_GENESIS_STATE_R1.sigmab"

"$P/bin/mkdir" -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=R4_GENESIS_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

[ -f "$SRC" ] || { printf 'HOLD=R4_GENESIS_SOURCE_MISSING\n'; exit 21; }
[ -x "$SIGMAC" ] || { printf 'HOLD=SIGMAC_MISSING\n'; exit 22; }
[ -x "$VM" ] || { printf 'HOLD=SIGMA_VM_MISSING\n'; exit 23; }

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
source_sha_before=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
source_git_blob=$("$P/bin/git" -C "$REPO" hash-object "$SRC" 2>/dev/null || true)

printf 'SIGMA_PHASE=R4_GENESIS_STATE_R1_PREFLIGHT\n'
printf 'R4_REPLACEMENT_CLEANLINE=YES\n'
printf 'HOST_COGNITION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'DYNAMIC_INPUT_GENERATED_AFTER_COMPILE=YES\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256_BEFORE=%s\n' "$source_sha_before"
printf 'SOURCE_GIT_BLOB=%s\n' "$source_git_blob"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 24; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 25; }
[ "$source_git_blob" = "$EXPECTED_SOURCE_GIT_BLOB" ] || { printf 'HOLD=R4_GENESIS_SOURCE_GIT_BLOB_MISMATCH\n'; exit 26; }

# Static cleanline checks. Machine receipt labels are allowed; non-empty hardcoded
# cognitive payload/learned-state literals are not.
if "$P/bin/grep" -E 'COGNITIVE_PAYLOAD:[[:space:]]*"[^"[:space:]][^"]*"' "$SRC" >/dev/null 2>&1; then
    printf 'HOLD=NONEMPTY_HARDCODED_COGNITIVE_PAYLOAD_FOUND\n'
    exit 27
fi
if "$P/bin/grep" -E 'NATIVE_LEARNED_STATE:[[:space:]]*"[^"[:space:]][^"]*"' "$SRC" >/dev/null 2>&1; then
    printf 'HOLD=NONEMPTY_HARDCODED_LEARNED_STATE_FOUND\n'
    exit 28
fi

"$P/bin/rm" -f -- "$BC.partial" "$BC"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || { printf 'R4_GENESIS_PREFLIGHT=FAIL_COMPILE\n'; exit 30; }
[ -s "$BC.partial" ] || { printf 'R4_GENESIS_PREFLIGHT=FAIL_EMPTY_BYTECODE\n'; exit 31; }
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 32
"$P/bin/chmod" 0400 "$BC" || exit 33

bytecode_sha_before=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256_BEFORE=%s\n' "$bytecode_sha_before"

# Dynamic fixture identities are created only after source/bytecode freeze.
dynamic_hex() {
    "$P/bin/od" -An -N16 -tx1 /dev/urandom | "$P/bin/tr" -d ' \n'
}

LINEAGE_A="r4-lineage-$(dynamic_hex)"
LINEAGE_B="r4-lineage-$(dynamic_hex)"
RUNTIME_PROFILE="r4-runtime-$(dynamic_hex)"
CAPABILITY_REGISTRY="r4-registry-$(dynamic_hex)"
FORBIDDEN_TOKEN="r4-forbidden-$(dynamic_hex)"

printf 'DYNAMIC_LINEAGE_A=%s\n' "$LINEAGE_A"
printf 'DYNAMIC_LINEAGE_B=%s\n' "$LINEAGE_B"
printf 'DYNAMIC_RUNTIME_PROFILE=%s\n' "$RUNTIME_PROFILE"
printf 'DYNAMIC_CAPABILITY_REGISTRY=%s\n' "$CAPABILITY_REGISTRY"
printf 'DYNAMIC_FORBIDDEN_TOKEN=%s\n' "$FORBIDDEN_TOKEN"

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
CASE_NAME=""
SANDBOX=""
IN=""
LAST_LOG=""

prepare_case() {
    CASE_NAME="$1"
    LINEAGE="$2"
    SANDBOX="$CASES/$CASE_NAME"
    IN="$SANDBOX/.sigma_exec/R4_GENESIS_STATE_R1/input"
    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$IN"

    printf '%s' "$LINEAGE" > "$IN/lineage_id.txt"
    printf '%s' "$RUNTIME_PROFILE" > "$IN/runtime_profile_id.txt"
    printf '%s' "$CAPABILITY_REGISTRY" > "$IN/capability_registry_id.txt"

    : > "$IN/legacy_c5_semantic_state.txt"
    : > "$IN/left_right_seed.txt"
    : > "$IN/lexical_relation_seed.txt"
    : > "$IN/predefined_concept_seed.txt"
    : > "$IN/predefined_response_vocabulary.txt"
    : > "$IN/predefined_cognitive_utterance.txt"
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
        printf 'R4_GENESIS_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=VM_NONZERO\n' "$LABEL"
        exit 50
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'R4_GENESIS_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=STEP_LIMIT_HIT\n' "$LABEL"
        exit 51
    fi
}

expect_line() {
    KEY="$1"
    VALUE="$2"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'R4_GENESIS_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_EXPECTED_OUTPUT\nEXPECTED=%s %s\n' "$CASE_NAME" "$KEY" "$VALUE"
        exit 60
    fi
}

expect_exact() {
    VALUE="$1"
    if ! "$P/bin/grep" -F -x "$VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'R4_GENESIS_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_SENTINEL\nEXPECTED=%s\n' "$CASE_NAME" "$VALUE"
        exit 61
    fi
}

post_vm_common() {
    printf 'CASE_POST_VM_TEST_ORACLE_STARTED=YES\n'
    expect_exact 'SIGMA_R4_GENESIS_STATE_R1'
    expect_line 'NATIVE_LEARNED_STATE_LEN' '0'
    expect_line 'COGNITIVE_PAYLOAD_LEN' '0'
}

pass_case() {
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
    printf 'CASE_POST_VM_ALIGNMENT=YES\n'
}

# CASE 001 — clean genesis, dynamic lineage A.
prepare_case CASE_001_CLEAN_A "$LINEAGE_A"
run_vm CASE_001_CLEAN_A
post_vm_common
expect_line 'GENESIS_ACCEPTED' '1'
expect_line 'REQUIRED_BINDINGS_VALID' '1'
expect_line 'FORBIDDEN_SEED_COUNT' '0'
expect_line 'LINEAGE_ID' "$LINEAGE_A"
pass_case
LOG_CLEAN_A="$LAST_LOG"

# CASE 002 — materially different dynamic lineage B must bind exactly.
prepare_case CASE_002_CLEAN_B "$LINEAGE_B"
run_vm CASE_002_CLEAN_B
post_vm_common
expect_line 'GENESIS_ACCEPTED' '1'
expect_line 'REQUIRED_BINDINGS_VALID' '1'
expect_line 'FORBIDDEN_SEED_COUNT' '0'
expect_line 'LINEAGE_ID' "$LINEAGE_B"
pass_case

# CASE 003 — legacy semantic state import fails closed.
prepare_case CASE_003_LEGACY_IMPORT "$LINEAGE_A"
printf '%s' "$FORBIDDEN_TOKEN" > "$IN/legacy_c5_semantic_state.txt"
run_vm CASE_003_LEGACY_IMPORT
post_vm_common
expect_line 'GENESIS_ACCEPTED' '0'
expect_line 'FORBIDDEN_SEED_COUNT' '1'
pass_case

# CASE 004 — LEFT/RIGHT legacy seed fails closed.
prepare_case CASE_004_LEFT_RIGHT "$LINEAGE_A"
printf '%s' "$FORBIDDEN_TOKEN" > "$IN/left_right_seed.txt"
run_vm CASE_004_LEFT_RIGHT
post_vm_common
expect_line 'GENESIS_ACCEPTED' '0'
expect_line 'FORBIDDEN_SEED_COUNT' '1'
pass_case

# CASE 005 — predefined response vocabulary fails closed.
prepare_case CASE_005_RESPONSE_VOCAB "$LINEAGE_A"
printf '%s' "$FORBIDDEN_TOKEN" > "$IN/predefined_response_vocabulary.txt"
run_vm CASE_005_RESPONSE_VOCAB
post_vm_common
expect_line 'GENESIS_ACCEPTED' '0'
expect_line 'FORBIDDEN_SEED_COUNT' '1'
pass_case

# CASE 006 — predefined cognitive utterance fails closed.
prepare_case CASE_006_UTTERANCE "$LINEAGE_A"
printf '%s' "$FORBIDDEN_TOKEN" > "$IN/predefined_cognitive_utterance.txt"
run_vm CASE_006_UTTERANCE
post_vm_common
expect_line 'GENESIS_ACCEPTED' '0'
expect_line 'FORBIDDEN_SEED_COUNT' '1'
pass_case

# CASE 007 — multiple semantic seed surfaces are all counted/rejected.
prepare_case CASE_007_MULTI_SEED "$LINEAGE_A"
printf '%s' "$FORBIDDEN_TOKEN" > "$IN/lexical_relation_seed.txt"
printf '%s' "$FORBIDDEN_TOKEN" > "$IN/predefined_concept_seed.txt"
run_vm CASE_007_MULTI_SEED
post_vm_common
expect_line 'GENESIS_ACCEPTED' '0'
expect_line 'FORBIDDEN_SEED_COUNT' '2'
pass_case

# CASE 008 — missing required mechanical binding fails closed.
prepare_case CASE_008_MISSING_REGISTRY "$LINEAGE_A"
: > "$IN/capability_registry_id.txt"
run_vm CASE_008_MISSING_REGISTRY
post_vm_common
expect_line 'GENESIS_ACCEPTED' '0'
expect_line 'REQUIRED_BINDINGS_VALID' '0'
pass_case

# CASE 009 — oversized binding fails boundedness validation.
prepare_case CASE_009_OVERSIZED_LINEAGE "$LINEAGE_A"
"$P/bin/awk" 'BEGIN { for (i=0; i<300; i++) printf "x" }' > "$IN/lineage_id.txt"
run_vm CASE_009_OVERSIZED_LINEAGE
post_vm_common
expect_line 'GENESIS_ACCEPTED' '0'
expect_line 'REQUIRED_BINDINGS_VALID' '0'
pass_case

# CASE 010 — byte-identical replay of CASE 001.
prepare_case CASE_010_REPLAY_A "$LINEAGE_A"
run_vm CASE_010_REPLAY_A
post_vm_common
expect_line 'GENESIS_ACCEPTED' '1'
expect_line 'REQUIRED_BINDINGS_VALID' '1'
expect_line 'FORBIDDEN_SEED_COUNT' '0'
expect_line 'LINEAGE_ID' "$LINEAGE_A"
pass_case
LOG_REPLAY_A="$LAST_LOG"

REPLAY_IDENTICAL_OUTPUT=NO
if "$P/bin/cmp" -s "$LOG_CLEAN_A" "$LOG_REPLAY_A"; then
    REPLAY_IDENTICAL_OUTPUT=YES
fi

source_sha_after=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
bytecode_sha_after=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')

SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
[ "$source_sha_before" = "$source_sha_after" ] && SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
[ "$bytecode_sha_before" = "$bytecode_sha_after" ] && BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES

TOKEN_LEAK_COUNT=0
for tok in "$LINEAGE_A" "$LINEAGE_B" "$RUNTIME_PROFILE" "$CAPABILITY_REGISTRY" "$FORBIDDEN_TOKEN"; do
    if "$P/bin/grep" -a -F "$tok" "$SRC" "$BC" >/dev/null 2>&1; then
        TOKEN_LEAK_COUNT=$((TOKEN_LEAK_COUNT + 1))
    fi
done

printf '\n=== R4 GENESIS AGGREGATE ===\n'
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'REPLAY_IDENTICAL_OUTPUT=%s\n' "$REPLAY_IDENTICAL_OUTPUT"
printf 'SOURCE_SHA256_AFTER=%s\n' "$source_sha_after"
printf 'BYTECODE_SHA256_AFTER=%s\n' "$bytecode_sha_after"
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=%s\n' "$TOKEN_LEAK_COUNT"
printf 'HOST_COGNITION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'PERSISTENT_STATE_TEST=NOT_RUN\n'
printf 'T5_T9_BINDING=NOT_YET_RUN\n'
printf 'RESURRECTION_TEST=NOT_RUN\n'
printf 'HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN\n'
printf 'AUTONOMOUS_WEB_LEARNING=NOT_PROVEN\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'

[ "$TOTAL_VM_INVOCATIONS" -eq 10 ] || exit 70
[ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 10 ] || exit 71
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || exit 72
[ "$VM_NONZERO_COUNT" -eq 0 ] || exit 73
[ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] || exit 74
[ "$REPLAY_IDENTICAL_OUTPUT" = YES ] || exit 75
[ "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || exit 76
[ "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || exit 77
[ "$TOKEN_LEAK_COUNT" -eq 0 ] || exit 78

printf 'R4_GENESIS_STATE_R1_PREFLIGHT=PASS_IN_EXACT_TESTED_SCOPE\n'
printf 'R4_GENESIS_RUNTIME_ADMISSION=SOURCE_READY_PENDING_TERMUX_MACHINE_RUN\n'
