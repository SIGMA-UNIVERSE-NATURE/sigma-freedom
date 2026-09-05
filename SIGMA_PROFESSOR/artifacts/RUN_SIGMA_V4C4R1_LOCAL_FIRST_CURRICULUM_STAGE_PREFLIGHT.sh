#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
SRC_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_LOCAL_FIRST_CURRICULUM_STAGE_CONTROLLER_V4C4R1.sigma"
EXPECTED_SRC_BLOB=9c55b842b321feba5d755ef7021ba5a3067ff6e1
SRC_REPO="$REPO/$SRC_REL"

BASE="$HOME_SIGMA/SIGMA_V4C4R1_LOCAL_FIRST_CURRICULUM_STAGE_PREFLIGHT"
COMPILER="$BASE/compiler"
BC="$COMPILER/SIGMA_V4_LOCAL_FIRST_CURRICULUM_STAGE_CONTROLLER_V4C4R1.sigmab"
SRC="$COMPILER/SIGMA_V4_LOCAL_FIRST_CURRICULUM_STAGE_CONTROLLER_V4C4R1.sigma"

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }
blob1() { git -C "$REPO" hash-object "$1"; }

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")

printf 'SIGMA_PHASE=V4C4R1_LOCAL_FIRST_CURRICULUM_STAGE_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_STAGE_DECISION=NO\n'
printf 'HOST_CURRICULUM_PRIORITY=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'BASH_LEARNING=NO\n'
printf 'GPT_AS_SIGMA_COGNITION=NO\n'
printf 'FIXTURE_ROLE=MECHANICAL_DYNAMIC_DIRECTORY_STATE_ONLY\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 20; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 21; }
[ -f "$SRC_REPO" ] || { printf 'HOLD=V4C4_SOURCE_MISSING\n'; exit 22; }

SRC_BLOB=$(blob1 "$SRC_REPO")
SRC_SHA=$(hash1 "$SRC_REPO")
printf 'V4C4_SOURCE_GIT_BLOB=%s\n' "$SRC_BLOB"
printf 'V4C4_SOURCE_SHA256=%s\n' "$SRC_SHA"
[ "$SRC_BLOB" = "$EXPECTED_SRC_BLOB" ] || { printf 'HOLD=V4C4_SOURCE_BLOB_MISMATCH\n'; exit 23; }

FORCED_COUNT=0
for TOKEN in 'SEMANTIC_UNDERSTANDING' 'UNDERSTANDING_PROXY' 'NOT_PROVEN' 'NOT_UNDERSTOOD' 'UNDERSTOOD' 'CHUA_DUOC_CHUNG_MINH'; do
    C=$("$P/bin/grep" -F -c -- "$TOKEN" "$SRC_REPO" 2>/dev/null || true)
    FORCED_COUNT=$((FORCED_COUNT + C))
done
printf 'FORCED_SEMANTIC_VERDICT_LITERAL_COUNT=%s\n' "$FORCED_COUNT"
[ "$FORCED_COUNT" -eq 0 ] || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_LITERAL_PRESENT\n'; exit 24; }

rm -rf -- "$BASE"
mkdir -p "$COMPILER"
cp -- "$SRC_REPO" "$SRC" || exit 25
INSTALLED_BLOB=$(blob1 "$SRC")
printf 'V4C4_INSTALLED_GIT_BLOB=%s\n' "$INSTALLED_BLOB"
[ "$INSTALLED_BLOB" = "$EXPECTED_SRC_BLOB" ] || { printf 'HOLD=INSTALLED_SOURCE_BLOB_MISMATCH\n'; exit 26; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
SIGMAC_RC=$?
printf 'V4C4_SIGMAC_RC=%s\n' "$SIGMAC_RC"
[ "$SIGMAC_RC" -eq 0 ] || { printf 'HOLD=V4C4_SIGMAC_FAILED\n'; exit 27; }
[ -s "$BC.partial" ] || { printf 'HOLD=V4C4_BYTECODE_EMPTY\n'; exit 28; }
mv -f -- "$BC.partial" "$BC" || exit 29
chmod 0400 "$BC" || exit 30
BC_SHA=$(hash1 "$BC")
printf 'V4C4_BYTECODE_SHA256=%s\n' "$BC_SHA"

FORCED_BC_COUNT=0
for TOKEN in 'SEMANTIC_UNDERSTANDING' 'UNDERSTANDING_PROXY' 'NOT_PROVEN' 'NOT_UNDERSTOOD' 'UNDERSTOOD' 'CHUA_DUOC_CHUNG_MINH'; do
    C=$("$P/bin/grep" -a -F -c -- "$TOKEN" "$BC" 2>/dev/null || true)
    FORCED_BC_COUNT=$((FORCED_BC_COUNT + C))
done
printf 'FORCED_SEMANTIC_VERDICT_TOKEN_IN_BYTECODE_COUNT=%s\n' "$FORCED_BC_COUNT"
[ "$FORCED_BC_COUNT" -eq 0 ] || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_TOKEN_IN_BYTECODE\n'; exit 31; }

TOKEN="$("$P/bin/date" +%s).$$.$RANDOM"
printf 'DYNAMIC_FIXTURE_TOKEN=%s\n' "$TOKEN"

make_case() {
    NAME="$1"
    ROOT="$BASE/$NAME"
    BRAIN="$ROOT/BRAIN/EXTRA BRAIN_OPPO_24826"
    E="$BRAIN/.sigma_exec"
    LRAW="$ROOT/local_raw"
    LSTATE="$ROOT/local_state"
    XRAW="$ROOT/external_raw"
    XSTATE="$ROOT/external_state"
    mkdir -p "$E" "$LRAW" "$LSTATE" "$XRAW" "$XSTATE"

    for F in \
      SIGMA_V4C4_LOCAL_RAW_DIR.memory SIGMA_V4C4_LOCAL_STATE_DIR.memory SIGMA_V4C4_EXTERNAL_RAW_DIR.memory SIGMA_V4C4_EXTERNAL_STATE_DIR.memory SIGMA_V4C4_MODE.memory SIGMA_V4C4_ACTION.memory SIGMA_V4C4_STATUS.memory \
      SIGMA_V4C2R2_RAW_DIR.memory SIGMA_V4C2R2_STATE_DIR.memory SIGMA_V4C2R2_PHASE.memory SIGMA_V4C2R2_SCAN_CURSOR.memory SIGMA_V4C2R2_ACTIVE_DOC.memory SIGMA_V4C2R2_ACTIVE_PURPOSE.memory SIGMA_V4C2R2_ACTIVE_BEST_WIDTH.memory SIGMA_V4C2R2_ACTIVE_BEST_SUPPORT.memory SIGMA_V4C2R2_PRIORITY_BEST_DOC.memory SIGMA_V4C2R2_PRIORITY_BEST_WIDTH.memory SIGMA_V4C2R2_PRIORITY_BEST_SUPPORT.memory SIGMA_V4C2R2_PRIORITY_UNPROFILED.memory SIGMA_V4C2R2_READ_REQUEST_ID.memory SIGMA_V4C2R2_READ_DOC.memory SIGMA_V4C2R2_READ_LINE.memory SIGMA_V4C2R2_READ_PURPOSE.memory SIGMA_V4C2R2_READ_RESULT_ID.memory SIGMA_V4C2R2_READ_RESULT_FOUND.memory SIGMA_V4C2R2_READ_RESULT_TEXT.memory \
      SIGMA_V4B4R2_CONTEXT_ID.memory SIGMA_V4B4R2_CONTEXT_TEXT.memory SIGMA_V4B4R2_TOKEN_CURSOR.memory SIGMA_V4B4R2_COMPLETION.memory SIGMA_V4B4R2_STATUS.memory SIGMA_V4B4R2_LAST_EVIDENCE.memory SIGMA_V4B4R2_BEST_WIDTH.memory SIGMA_V4B4R2_BEST_SUPPORT.memory SIGMA_V4B4R2_PAIR_OCCURRENCES.memory SIGMA_V4B4R2_TRIPLE_OCCURRENCES.memory SIGMA_V4B4R2_QUAD_OCCURRENCES.memory
    do
        : > "$E/$F"
    done

    printf '%s' "$LRAW" > "$E/SIGMA_V4C4_LOCAL_RAW_DIR.memory"
    printf '%s' "$LSTATE" > "$E/SIGMA_V4C4_LOCAL_STATE_DIR.memory"
    printf '%s' "$XRAW" > "$E/SIGMA_V4C4_EXTERNAL_RAW_DIR.memory"
    printf '%s' "$XSTATE" > "$E/SIGMA_V4C4_EXTERNAL_STATE_DIR.memory"

    printf '%s\n' "$ROOT|$BRAIN|$E|$LRAW|$LSTATE|$XRAW|$XSTATE"
}

run_vm_case() {
    NAME="$1"
    BRAIN="$2"
    LOGFILE="$BASE/$NAME.vm.log"
    ( cd "$BRAIN" || exit 70; "$VM" "$BC" ) > "$LOGFILE" 2>&1
    RC=$?
    printf '%s_VM_RC=%s LOG=%s\n' "$NAME" "$RC" "$LOGFILE"
    "$P/bin/cat" "$LOGFILE"
    [ "$RC" -eq 0 ] || return 1
}

assert_file_eq() {
    FILE="$1"
    EXPECTED="$2"
    LABEL="$3"
    ACTUAL=$(cat "$FILE")
    if [ "$ACTUAL" != "$EXPECTED" ]; then
        printf 'ASSERT_FAIL=%s EXPECTED=%s ACTUAL=%s\n' "$LABEL" "$EXPECTED" "$ACTUAL"
        return 1
    fi
    printf 'ASSERT_PASS=%s VALUE=%s\n' "$LABEL" "$ACTUAL"
}

A_INFO=$(make_case CASE_A_LOCAL_INCOMPLETE)
IFS='|' read -r A_ROOT A_BRAIN A_E A_LRAW A_LSTATE A_XRAW A_XSTATE <<EOF
$A_INFO
EOF
A1="${TOKEN}.a1"
A2="${TOKEN}.a2"
printf 'alpha local one\n' > "$A_LRAW/$A1.document"
printf 'beta local two\n' > "$A_LRAW/$A2.document"
printf 'WIDTH=| || SUPPORT=| || PROFILE=YES' > "$A_LSTATE/$A1.profile"
printf 'DOC=%s || COMPLETE=YES || COMMIT=YES' "$A1" > "$A_LSTATE/$A1.complete"
run_vm_case CASE_A_LOCAL_INCOMPLETE "$A_BRAIN" || { printf 'HOLD=CASE_A_VM_FAILURE\n'; exit 40; }
assert_file_eq "$A_E/SIGMA_V4C4_MODE.memory" LOCAL CASE_A_MODE || exit 41
assert_file_eq "$A_E/SIGMA_V4C4_ACTION.memory" PLAN_CONTINUE_LOCAL_STORED_TEACHING_CORPUS CASE_A_ACTION || exit 42
assert_file_eq "$A_E/SIGMA_V4C2R2_RAW_DIR.memory" "$A_LRAW" CASE_A_RAW_BINDING || exit 43

B_INFO=$(make_case CASE_B_LOCAL_PASS_COMPLETE)
IFS='|' read -r B_ROOT B_BRAIN B_E B_LRAW B_LSTATE B_XRAW B_XSTATE <<EOF
$B_INFO
EOF
B1="${TOKEN}.b1"
B2="${TOKEN}.b2"
printf 'gamma local one\n' > "$B_LRAW/$B1.document"
printf 'delta local two\n' > "$B_LRAW/$B2.document"
for D in "$B1" "$B2"; do
    printf 'WIDTH=| || SUPPORT=| || PROFILE=YES' > "$B_LSTATE/$D.profile"
    printf 'DOC=%s || COMPLETE=YES || COMMIT=YES' "$D" > "$B_LSTATE/$D.complete"
done
printf 'LOCAL' > "$B_E/SIGMA_V4C4_MODE.memory"
printf '%s' "$B_LRAW" > "$B_E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$B_LSTATE" > "$B_E/SIGMA_V4C2R2_STATE_DIR.memory"
run_vm_case CASE_B_LOCAL_PASS_COMPLETE "$B_BRAIN" || { printf 'HOLD=CASE_B_VM_FAILURE\n'; exit 44; }
assert_file_eq "$B_E/SIGMA_V4C4_MODE.memory" EXTERNAL CASE_B_MODE || exit 45
assert_file_eq "$B_E/SIGMA_V4C4_ACTION.memory" PLAN_ACTIVATE_EXISTING_NATIVE_EXTERNAL_FEED CASE_B_ACTION || exit 46
assert_file_eq "$B_E/SIGMA_V4C2R2_RAW_DIR.memory" "$B_XRAW" CASE_B_RAW_BINDING || exit 47
assert_file_eq "$B_E/SIGMA_V4C2R2_STATE_DIR.memory" "$B_XSTATE" CASE_B_STATE_BINDING || exit 48

C_INFO=$(make_case CASE_C_NEW_LOCAL_PREEMPTS_EXTERNAL)
IFS='|' read -r C_ROOT C_BRAIN C_E C_LRAW C_LSTATE C_XRAW C_XSTATE <<EOF
$C_INFO
EOF
C1="${TOKEN}.c1"
C2="${TOKEN}.c2"
C3="${TOKEN}.c3"
for D in "$C1" "$C2" "$C3"; do printf '%s local\n' "$D" > "$C_LRAW/$D.document"; done
for D in "$C1" "$C2"; do
    printf 'WIDTH=| || SUPPORT=| || PROFILE=YES' > "$C_LSTATE/$D.profile"
    printf 'DOC=%s || COMPLETE=YES || COMMIT=YES' "$D" > "$C_LSTATE/$D.complete"
done
printf 'EXTERNAL' > "$C_E/SIGMA_V4C4_MODE.memory"
printf '%s' "$C_XRAW" > "$C_E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$C_XSTATE" > "$C_E/SIGMA_V4C2R2_STATE_DIR.memory"
run_vm_case CASE_C_NEW_LOCAL_PREEMPTS_EXTERNAL "$C_BRAIN" || { printf 'HOLD=CASE_C_VM_FAILURE\n'; exit 49; }
assert_file_eq "$C_E/SIGMA_V4C4_MODE.memory" LOCAL CASE_C_MODE || exit 50
assert_file_eq "$C_E/SIGMA_V4C4_ACTION.memory" PLAN_CONTINUE_LOCAL_STORED_TEACHING_CORPUS CASE_C_ACTION || exit 51
assert_file_eq "$C_E/SIGMA_V4C2R2_RAW_DIR.memory" "$C_LRAW" CASE_C_RAW_BINDING || exit 52

D_INFO=$(make_case CASE_D_SWITCH_WAITS_SAFE_BOUNDARY)
IFS='|' read -r D_ROOT D_BRAIN D_E D_LRAW D_LSTATE D_XRAW D_XSTATE <<EOF
$D_INFO
EOF
D1="${TOKEN}.d1"
D2="${TOKEN}.d2"
printf 'one\n' > "$D_LRAW/$D1.document"
printf 'two\n' > "$D_LRAW/$D2.document"
printf 'WIDTH=| || SUPPORT=| || PROFILE=YES' > "$D_LSTATE/$D1.profile"
printf 'DOC=%s || COMPLETE=YES || COMMIT=YES' "$D1" > "$D_LSTATE/$D1.complete"
printf 'EXTERNAL' > "$D_E/SIGMA_V4C4_MODE.memory"
printf '%s' "$D_XRAW" > "$D_E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$D_XSTATE" > "$D_E/SIGMA_V4C2R2_STATE_DIR.memory"
printf 'external-active-doc' > "$D_E/SIGMA_V4C2R2_ACTIVE_DOC.memory"
printf 'external-active-doc::LINE=' > "$D_E/SIGMA_V4B4R2_CONTEXT_ID.memory"
run_vm_case CASE_D_SWITCH_WAITS_SAFE_BOUNDARY "$D_BRAIN" || { printf 'HOLD=CASE_D_VM_FAILURE\n'; exit 53; }
assert_file_eq "$D_E/SIGMA_V4C4_MODE.memory" EXTERNAL CASE_D_MODE_STAYS_EXTERNAL || exit 54
assert_file_eq "$D_E/SIGMA_V4C4_STATUS.memory" NATIVE_CURRICULUM_MODE_SWITCH_PENDING_ACTIVE_CONTEXT CASE_D_PENDING_STATUS || exit 55
assert_file_eq "$D_E/SIGMA_V4C2R2_RAW_DIR.memory" "$D_XRAW" CASE_D_EXTERNAL_BINDING_PRESERVED || exit 56

E_INFO=$(make_case CASE_E_LOCAL_HOLD_BLOCKS_EXTERNAL)
IFS='|' read -r E_ROOT E_BRAIN E_E E_LRAW E_LSTATE E_XRAW E_XSTATE <<EOF
$E_INFO
EOF
E1="${TOKEN}.e1"
E2="${TOKEN}.e2"
printf 'hold one\n' > "$E_LRAW/$E1.document"
printf 'hold two\n' > "$E_LRAW/$E2.document"
printf 'WIDTH=| || SUPPORT=| || PROFILE=YES' > "$E_LSTATE/$E1.profile"
printf 'DOC=%s || COMPLETE=YES || COMMIT=YES' "$E1" > "$E_LSTATE/$E1.complete"
printf 'DOC=%s || HOLD=FIXTURE || COMMIT=YES' "$E2" > "$E_LSTATE/$E2.hold"
printf 'EXTERNAL' > "$E_E/SIGMA_V4C4_MODE.memory"
printf '%s' "$E_XRAW" > "$E_E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$E_XSTATE" > "$E_E/SIGMA_V4C2R2_STATE_DIR.memory"
run_vm_case CASE_E_LOCAL_HOLD_BLOCKS_EXTERNAL "$E_BRAIN" || { printf 'HOLD=CASE_E_VM_FAILURE\n'; exit 57; }
assert_file_eq "$E_E/SIGMA_V4C4_MODE.memory" LOCAL CASE_E_MODE || exit 58
assert_file_eq "$E_E/SIGMA_V4C4_ACTION.memory" PLAN_LOCAL_NATIVE_HOLD_RECOVERY_REQUIRED CASE_E_ACTION || exit 59

F_INFO=$(make_case CASE_F_INVALID_MODE_REFUSAL)
IFS='|' read -r F_ROOT F_BRAIN F_E F_LRAW F_LSTATE F_XRAW F_XSTATE <<EOF
$F_INFO
EOF
printf 'invalid\n' > "$F_LRAW/${TOKEN}.f1.document"
printf 'INVALID_MODE' > "$F_E/SIGMA_V4C4_MODE.memory"
run_vm_case CASE_F_INVALID_MODE_REFUSAL "$F_BRAIN" || { printf 'HOLD=CASE_F_VM_FAILURE\n'; exit 60; }
assert_file_eq "$F_E/SIGMA_V4C4_STATUS.memory" REFUSE_INVALID_CURRICULUM_STATE CASE_F_STATUS || exit 61
assert_file_eq "$F_E/SIGMA_V4C4_ACTION.memory" REFUSE_INVALID_CURRICULUM_STATE CASE_F_ACTION || exit 62

G_INFO=$(make_case CASE_G_EMPTY_LOCAL_REFUSAL)
IFS='|' read -r G_ROOT G_BRAIN G_E G_LRAW G_LSTATE G_XRAW G_XSTATE <<EOF
$G_INFO
EOF
run_vm_case CASE_G_EMPTY_LOCAL_REFUSAL "$G_BRAIN" || { printf 'HOLD=CASE_G_VM_FAILURE\n'; exit 63; }
assert_file_eq "$G_E/SIGMA_V4C4_STATUS.memory" REFUSE_LOCAL_CORPUS_EMPTY CASE_G_STATUS || exit 64
assert_file_eq "$G_E/SIGMA_V4C4_ACTION.memory" REFUSE_LOCAL_CORPUS_EMPTY CASE_G_ACTION || exit 65

SRC_SHA_AFTER=$(hash1 "$SRC_REPO")
BC_SHA_AFTER=$(hash1 "$BC")
printf 'SOURCE_SHA256_AFTER_DYNAMIC_TEST=%s\n' "$SRC_SHA_AFTER"
printf 'BYTECODE_SHA256_AFTER_DYNAMIC_TEST=%s\n' "$BC_SHA_AFTER"
[ "$SRC_SHA_AFTER" = "$SRC_SHA" ] || { printf 'HOLD=SOURCE_CHANGED_DURING_TEST\n'; exit 66; }
[ "$BC_SHA_AFTER" = "$BC_SHA" ] || { printf 'HOLD=BYTECODE_CHANGED_DURING_TEST\n'; exit 67; }

TOKEN_LEAK_SRC=$("$P/bin/grep" -F -c -- "$TOKEN" "$SRC_REPO" 2>/dev/null || true)
TOKEN_LEAK_BC=$("$P/bin/grep" -a -F -c -- "$TOKEN" "$BC" 2>/dev/null || true)
printf 'DYNAMIC_TOKEN_LEAK_SOURCE_COUNT=%s\n' "$TOKEN_LEAK_SRC"
printf 'DYNAMIC_TOKEN_LEAK_BYTECODE_COUNT=%s\n' "$TOKEN_LEAK_BC"
[ "$TOKEN_LEAK_SRC" -eq 0 ] || exit 68
[ "$TOKEN_LEAK_BC" -eq 0 ] || exit 69

printf '\nV4C4R1_LOCAL_FIRST_CURRICULUM_STAGE_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'NATIVE_LOCAL_FIRST_MODE_SELECTION=PASS_IN_DYNAMIC_FIXTURE_SCOPE\n'
printf 'NATIVE_EXTERNAL_FEED_ACTIVATION_AFTER_LOCAL_OPERATIONAL_PASS=PASS_IN_FIXTURE_SCOPE\n'
printf 'NATIVE_NEW_LOCAL_DATA_PREEMPTS_EXTERNAL_AT_SAFE_BOUNDARY=PASS_IN_FIXTURE_SCOPE\n'
printf 'NATIVE_ACTIVE_CONTEXT_SAFE_BOUNDARY=PASS_IN_FIXTURE_SCOPE\n'
printf 'NATIVE_LOCAL_HOLD_BLOCKS_EXTERNAL=PASS_IN_FIXTURE_SCOPE\n'
printf 'NEGATIVE_INVALID_MODE_REFUSAL=PASS\n'
printf 'NEGATIVE_EMPTY_LOCAL_REFUSAL=PASS\n'
printf 'FORCED_SEMANTIC_VERDICT_LITERAL_IN_SOURCE=NO\n'
printf 'FORCED_SEMANTIC_VERDICT_TOKEN_IN_BYTECODE=NO\n'
printf 'HOST_STAGE_DECISION=NO\n'
printf 'HOST_CURRICULUM_PRIORITY=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'BASH_LEARNING=NO\n'
printf 'GPT_AS_SIGMA_COGNITION=NO\n'
printf 'LOCAL_OPERATIONAL_PASS_IS_SEMANTIC_MASTERY_CLAIM=NO\n'
printf 'PRODUCTION_BINDING=NO\n'
