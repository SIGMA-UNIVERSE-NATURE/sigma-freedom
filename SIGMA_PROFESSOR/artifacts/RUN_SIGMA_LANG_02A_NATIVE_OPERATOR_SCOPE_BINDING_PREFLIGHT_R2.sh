#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
EXPECTED_SOURCE=7a40e92e11c7c89574d3b975bb3210a7a7a23690251951da68be9e7edbfe292b
EXPECTED_R1_RUNNER=720148bb4d22acb23e47118139095b4e73816491029ea2555448641779fc5bc4

EXPECTED_DEP_CHECKPOINT_BLOB=d2d6a29c55561170dc19b6aec3c666e7e26011c6
EXPECTED_DEP_SOURCE=a47142af96dcbc47f0181f38952d29a5fa6fffeeb6c24b466b6b3a5acc759310
EXPECTED_DEP_BYTECODE=bb584206f8db16d832e2c20a027c4673e34ab9484ad062cd0f7bbe01206eafc9
DEP_CAP='LANG-01A_NATIVE_DISTRIBUTIONAL_EVENT_FRAME_HYPOTHESIS_INDUCTION'
DEP_STATUS='ADMITTED_IN_EXACT_TESTED_SCOPE'

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_V1.sigma"
R1="$REPO/SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_PREFLIGHT.sh"
DEP_REL="SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md"
DEP="$REPO/$DEP_REL"

RUN_ID="$(date +%Y%m%d_%H%M%S)$$"
ROOT="$HOME_SIGMA/SIGMA_LANG_02A_OPERATOR_SCOPE_BINDING_R2_PREFLIGHT_$RUN_ID"
LOG="$ROOT/log"
DYN="$ROOT/dynamic_unseen"
DYN_BASE="$DYN/.sigma_exec/SIGMA_LANG_02A_OPERATOR_SCOPE_BINDING_V1"
DYN_IN="$DYN_BASE/input"
R1_ROOT="$HOME_SIGMA/SIGMA_LANG_02A_OPERATOR_SCOPE_BINDING_V1_PREFLIGHT"
R1_BC="$R1_ROOT/SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_V1.sigmab"
LOCK="$HOME_SIGMA/SIGMA_LANG_02A_OPERATOR_SCOPE_BINDING_R2_PREFLIGHT.lock"

mkdir -p "$ROOT" "$LOG"
exec 9>"$LOCK"
"$P/bin/flock" -n 9 || { printf 'HOLD=LANG_02A_R2_PREFLIGHT_ALREADY_RUNNING\n'; exit 20; }

printf 'SIGMA_PHASE=LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_PREFLIGHT_R2\n'
printf 'RUN_ID=%s\n' "$RUN_ID"
printf 'NATIVE_SOURCE_CHANGED_FROM_R1=NO\n'
printf 'R1_ORACLE_CASES_CHANGED=NO\n'
printf 'R2_REPAIR_CLASS=RUNNER_ONLY_DEPENDENCY_LOCK_AND_DYNAMIC_EVIDENCE_HARDENING\n'
printf 'HOST_SCOPE_SELECTION=NO\n'
printf 'HOST_OPERATOR_INTERPRETATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'

# 1. Exact runtime/source/R1-runner identities.
actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
source_before=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
r1_runner_actual=$("$P/bin/sha256sum" "$R1" | "$P/bin/awk" '{print $1}')
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$source_before"
printf 'R1_RUNNER_SHA256=%s\n' "$r1_runner_actual"
[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$source_before" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=LANG_02A_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$r1_runner_actual" = "$EXPECTED_R1_RUNNER" ] || { printf 'HOLD=LANG_02A_R1_RUNNER_IDENTITY_MISMATCH\n'; exit 24; }

# 2. Exact admitted dependency record lock. This must PASS before R1 is allowed
#    to write its dependency ABI fixture strings.
[ -f "$DEP" ] || { printf 'HOLD=LANG_01A_DEPENDENCY_CHECKPOINT_MISSING\n'; exit 30; }
dep_blob=$("$P/bin/git" -C "$REPO" rev-parse "HEAD:$DEP_REL" 2>/dev/null) || {
    printf 'HOLD=LANG_01A_DEPENDENCY_CHECKPOINT_GIT_IDENTITY_UNAVAILABLE\n'; exit 31;
}
printf 'DEPENDENCY_CHECKPOINT_GIT_BLOB=%s\n' "$dep_blob"
[ "$dep_blob" = "$EXPECTED_DEP_CHECKPOINT_BLOB" ] || {
    printf 'HOLD=LANG_01A_DEPENDENCY_CHECKPOINT_GIT_BLOB_MISMATCH\n'; exit 32;
}

need_dep_line() {
    if ! "$P/bin/grep" -F -x -- "$1" "$DEP" >/dev/null; then
        printf 'HOLD=LANG_01A_DEPENDENCY_ADMISSION_RECORD_MISMATCH\n'
        printf 'MISSING_DEPENDENCY_RECORD=%s\n' "$1"
        exit 33
    fi
}
need_dep_line '### LANG-01A — Native Distributional Event-Frame Hypothesis Induction — ADMITTED'
need_dep_line "- \`SOURCE_SHA256=$EXPECTED_DEP_SOURCE\`"
need_dep_line "- \`BYTECODE_SHA256=$EXPECTED_DEP_BYTECODE\`"
need_dep_line '- `TOTAL_VM_INVOCATIONS=10`'
need_dep_line '- persistence/restart/negative/bounded input refusal PASS.'
printf 'DEPENDENCY_EXACT_ADMISSION_RECORD_LOCK=PASS\n'
printf 'DEPENDENCY_SOURCE_SHA256=%s\n' "$EXPECTED_DEP_SOURCE"
printf 'DEPENDENCY_BYTECODE_SHA256=%s\n' "$EXPECTED_DEP_BYTECODE"

# 3. Run the exact, hash-locked R1 20-case suite unchanged.
R1_TRANSCRIPT="$LOG/R1_full_transcript.log"
(
    cd "$REPO" || exit 90
    SIGMA_REPO="$REPO" "$P/bin/bash" "$R1"
) 2>&1 | "$P/bin/tee" "$R1_TRANSCRIPT"
r1_rc=${PIPESTATUS[0]}
printf 'R1_WRAPPER_RC=%s\n' "$r1_rc"
[ "$r1_rc" -eq 0 ] || { printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=R1_FULL_SUITE_NONZERO\n'; exit 40; }

need_r1_summary() {
    if ! "$P/bin/grep" -F -x -- "$1" "$R1_TRANSCRIPT" >/dev/null; then
        printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=R1_HARD_GATE_MISSING\nMISSING=%s\n' "$1"
        exit 41
    fi
}
need_r1_summary 'TOTAL_VM_INVOCATIONS=20'
need_r1_summary 'POST_VM_ALIGNMENT_PASS_COUNT=20'
need_r1_summary 'POST_VM_ALIGNMENT_FAIL_COUNT=0'
need_r1_summary 'VM_NONZERO_COUNT=0'
need_r1_summary 'STEP_LIMIT_HIT_COUNT=0'
need_r1_summary 'NEGATIVE_TEST=PASS'
need_r1_summary 'RESTART_REPLAY_TEST=PASS'
need_r1_summary 'IDENTICAL_INPUT_REPLAY=YES'
need_r1_summary 'HOST_SCOPE_SELECTION=NO'
need_r1_summary 'HOST_OPERATOR_INTERPRETATION=NO'
need_r1_summary 'HOST_LEARNING=NO'
need_r1_summary 'HOST_SEMANTIC_INTERPRETATION=NO'
need_r1_summary 'PRODUCTION_STATE_MUTATED=NO'
need_r1_summary 'LANG_02A_PREFLIGHT=PASS'
need_r1_summary 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE'

# Bind the bytecode that R1 actually compiled, then freeze its identity for R2.
[ -s "$R1_BC" ] || { printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=R1_BYTECODE_MISSING\n'; exit 42; }
r1_printed_bc=$("$P/bin/grep" -F 'BYTECODE_SHA256=' "$R1_TRANSCRIPT" | "$P/bin/head" -n 1 | "$P/bin/cut" -d= -f2-)
r1_bc_before=$("$P/bin/sha256sum" "$R1_BC" | "$P/bin/awk" '{print $1}')
printf 'R1_PRINTED_BYTECODE_SHA256=%s\n' "$r1_printed_bc"
printf 'R1_OBSERVED_BYTECODE_SHA256=%s\n' "$r1_bc_before"
[ -n "$r1_printed_bc" ] || { printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=R1_BYTECODE_SHA_NOT_PRINTED\n'; exit 43; }
[ "$r1_printed_bc" = "$r1_bc_before" ] || { printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=R1_BYTECODE_IDENTITY_MISMATCH\n'; exit 44; }

# 4. Extra post-compile unseen/high-entropy dynamic case. Host creates the
#    structural fixture only; native SIGMA performs scope binding. Oracle starts
#    strictly after raw VM stdout/stderr are captured.
"$P/bin/rm" -rf -- "$DYN"
"$P/bin/mkdir" -p "$DYN_IN"
nonce=$(printf '%s' "$RUN_ID-$PPID-$RANDOM-$RANDOM" | "$P/bin/sha256sum" | "$P/bin/awk" '{print substr($1,1,12)}')
op_id="OP-$nonce"
outer_id="SC-O-$nonce"
inner_id="SC-I-$nonce"
far_id="SC-F-$nonce"
base=$((700 + RANDOM % 100))
pos=$((base + 31))
outer_end=$((base + 60))
inner_start=$((base + 24))
inner_end=$((base + 39))
far_start=$((base + 100))
far_end=$((base + 120))
inner_width=$((inner_end - inner_start))

printf '%s' "$DEP_CAP" > "$DYN_IN/dependency_capability.txt"
printf '%s' "$DEP_STATUS" > "$DYN_IN/dependency_status.txt"
printf 'OPERATOR||%s||%s||CLASS||SCOPE_OPERATOR||SOURCE||SRC-OP-%s\n' "$op_id" "$pos" "$nonce" > "$DYN_IN/operators.memory"
printf 'SCOPE||%s||%s||%s||SOURCE||SRC-O-%s\n' "$outer_id" "$base" "$outer_end" "$nonce" > "$DYN_IN/scopes.memory"
printf 'SCOPE||%s||%s||%s||SOURCE||SRC-I-%s\n' "$inner_id" "$inner_start" "$inner_end" "$nonce" >> "$DYN_IN/scopes.memory"
printf 'SCOPE||%s||%s||%s||SOURCE||SRC-F-%s\n' "$far_id" "$far_start" "$far_end" "$nonce" >> "$DYN_IN/scopes.memory"

leaks=0
for token in "$op_id" "$outer_id" "$inner_id" "$far_id"; do
    "$P/bin/grep" -a -F -- "$token" "$SRC" >/dev/null 2>&1 && leaks=$((leaks + 1))
    "$P/bin/grep" -a -F -- "$token" "$R1_BC" >/dev/null 2>&1 && leaks=$((leaks + 1))
done
printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=%s\n' "$leaks"
[ "$leaks" -eq 0 ] || { printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=DYNAMIC_TOKEN_LEAK\n'; exit 50; }

DYN_STDOUT="$LOG/CASE_021_DYNAMIC_UNSEEN.stdout"
DYN_STDERR="$LOG/CASE_021_DYNAMIC_UNSEEN.stderr"
(
    cd "$DYN" || exit 90
    "$VM" "$R1_BC"
) >"$DYN_STDOUT" 2>"$DYN_STDERR"
dyn_rc=$?
printf '%s\n' '--- RAW SIGMA VM CASE_021_DYNAMIC_UNSEEN STDOUT ---'
"$P/bin/cat" "$DYN_STDOUT"
printf '%s\n' '--- RAW SIGMA VM CASE_021_DYNAMIC_UNSEEN STDERR ---'
"$P/bin/cat" "$DYN_STDERR"
printf 'CASE_021_DYNAMIC_UNSEEN_VM_RC=%s\n' "$dyn_rc"
[ "$dyn_rc" -eq 0 ] || { printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=DYNAMIC_VM_NONZERO\n'; exit 51; }
if "$P/bin/grep" -F 'Step limit exceeded' "$DYN_STDOUT" "$DYN_STDERR" >/dev/null 2>&1; then
    printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=DYNAMIC_STEP_LIMIT_HIT\n'; exit 52
fi

printf 'CASE_021_POST_VM_TEST_ORACLE_STARTED=YES\n'
expect_dyn() {
    if ! "$P/bin/grep" -F -x -- "$1" "$DYN_STDOUT" >/dev/null; then
        printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=DYNAMIC_POST_VM_ALIGNMENT\nEXPECTED=%s\n' "$1"
        exit 53
    fi
}
expect_dyn 'SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING'
expect_dyn 'DEPENDENCY_BINDING_VALID 1'
expect_dyn 'INPUT_ACCEPTED 1'
expect_dyn 'ENCLOSING_SCOPE_COUNT 2'
expect_dyn "SELECTED_SCOPE_ID $inner_id"
expect_dyn "SELECTED_SCOPE_WIDTH $inner_width"
expect_dyn 'SCOPE_BINDING_STATUS SELECTED_STRUCTURAL_SCOPE'
expect_dyn 'HOST_SCOPE_SELECTION NO'
expect_dyn 'HOST_OPERATOR_INTERPRETATION NO'
expect_dyn 'HOST_LEARNING NO'
expect_dyn 'HOST_SEMANTIC_INTERPRETATION NO'
expect_dyn 'SURFACE_NEGATION_RECOGNITION NOT_PROVEN'
expect_dyn 'LOGICAL_NEGATION NOT_PROVEN'
expect_dyn 'PROPOSITION_TRUTH NOT_PROVEN'
expect_dyn 'SEMANTIC_SCOPE NOT_PROVEN'
expect_dyn 'SEMANTIC_UNDERSTANDING NOT_PROVEN'
expect_dyn 'PRODUCTION_STATE_MUTATED NO'
printf 'CASE_021_DYNAMIC_UNSEEN_POST_VM_ALIGNMENT=PASS\n'

# 5. End-of-suite identity freeze checks.
source_after=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
r1_bc_after=$("$P/bin/sha256sum" "$R1_BC" | "$P/bin/awk" '{print $1}')
[ "$source_after" = "$source_before" ] || { printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=SOURCE_MUTATED\n'; exit 60; }
[ "$r1_bc_after" = "$r1_bc_before" ] || { printf 'LANG_02A_R2_PREFLIGHT=FAIL\nFAILURE=BYTECODE_MUTATED\n'; exit 61; }

printf '\n=== LANG-02A R2 SUMMARY ===\n'
printf 'DEPENDENCY_EXACT_ADMISSION_RECORD_LOCK=PASS\n'
printf 'R1_EXACT_20_CASE_SUITE=PASS\n'
printf 'R1_TOTAL_VM_INVOCATIONS=20\n'
printf 'R2_ADDITIONAL_DYNAMIC_VM_INVOCATIONS=1\n'
printf 'R2_TOTAL_VM_INVOCATIONS=21\n'
printf 'R2_DYNAMIC_UNSEEN_POST_VM_ALIGNMENT=PASS\n'
printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'NATIVE_SCOPE_BINDING=PASS_IN_R2_PREFLIGHT_SCOPE\n'
printf 'HOST_SCOPE_SELECTION=NO\n'
printf 'HOST_OPERATOR_INTERPRETATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'PERSISTENT_STATE=NA\n'
printf 'SURFACE_NEGATION_RECOGNITION=NOT_PROVEN\n'
printf 'LOGICAL_NEGATION=NOT_PROVEN\n'
printf 'PROPOSITION_TRUTH=NOT_PROVEN\n'
printf 'SEMANTIC_SCOPE=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'LANG_02A_R2_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_R2_PREFLIGHT_SCOPE\n'
