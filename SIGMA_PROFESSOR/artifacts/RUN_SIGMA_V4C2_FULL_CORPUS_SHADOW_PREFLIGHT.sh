#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
PROD_STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
RAW="$PROD_STATE/raw"

BASE="$HOME_SIGMA/SIGMA_V4C2_FULL_CORPUS_SHADOW_PREFLIGHT"
LOCK="$BASE/preflight.lock"
RUN_ID="$("$P/bin/date" +%s).$$"
STATE="$BASE/run.$RUN_ID"
SHADOW="$STATE/shadow"
BRAIN="$SHADOW/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
CORPUS_STATE="$STATE/corpus_state"
LOG="$STATE/log"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

A2_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_PRODUCTIVITY_WORK_ARBITER_V4A2.sigma"
B4_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_COMPACT_TOKEN_WINDOW_SPAN_LEARNER_V4B4R1.sigma"
C2_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_CORPUS_WORK_MANAGER_V4C2R1.sigma"

EXPECTED_A2_SOURCE=72fa9dee55fa350c68482ad110d431b090efb1d41fe5ecb76a623ea8518d406e
EXPECTED_B4_SOURCE=c4a9828a45964917b75df23ec9b33885462119d26b7d1cfe37923c61c40b852c
EXPECTED_C2_SOURCE=bb7153866c65dddaaee2d426dd6276fe925b16f564f6f4b7395816953b3a914a

A2_SRC="$E/SIGMA_V4_PRODUCTIVITY_WORK_ARBITER_V4A2.sigma"
B4_SRC="$E/SIGMA_V4_COMPACT_TOKEN_WINDOW_SPAN_LEARNER_V4B4R1.sigma"
C2_SRC="$E/SIGMA_V4_CORPUS_WORK_MANAGER_V4C2R1.sigma"

A2_BC="$E/SIGMA_V4_PRODUCTIVITY_WORK_ARBITER_V4A2.sigmab"
B4_BC="$E/SIGMA_V4_COMPACT_TOKEN_WINDOW_SPAN_LEARNER_V4B4R1.sigmab"
C2_BC="$E/SIGMA_V4_CORPUS_WORK_MANAGER_V4C2R1.sigmab"

ACTION="$E/SIGMA_V4A2_ACTION.memory"
TARGET="$E/SIGMA_V4A2_TARGET.memory"
MANAGER_STATUS="$E/SIGMA_V4C2_STATUS.memory"
B4_CONTEXT="$E/SIGMA_V4B4_CONTEXT_ID.memory"

FIXED_CONTROLLER_TURNS=256

mkdir -p "$BASE" "$E" "$CORPUS_STATE" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C2_FULL_CORPUS_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

corpus_manifest() {
    "$P/bin/find" "$RAW" -maxdepth 1 -type f -name '*.document' -exec "$P/bin/sha256sum" '{}' + \
        | "$P/bin/sort" \
        | "$P/bin/sha256sum" \
        | "$P/bin/awk" '{print $1}'
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
A2_REPO_SHA=$(hash1 "$REPO/$A2_REL")
B4_REPO_SHA=$(hash1 "$REPO/$B4_REL")
C2_REPO_SHA=$(hash1 "$REPO/$C2_REL")

printf 'SIGMA_PHASE=V4C2_FULL_CORPUS_SHADOW_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'A2_SOURCE_SHA256=%s\n' "$A2_REPO_SHA"
printf 'B4_SOURCE_SHA256=%s\n' "$B4_REPO_SHA"
printf 'C2_SOURCE_SHA256=%s\n' "$C2_REPO_SHA"
printf 'FIXED_CONTROLLER_TURNS=%s\n' "$FIXED_CONTROLLER_TURNS"
printf 'CORPUS_SOURCE=%s\n' "$RAW"
printf 'SHADOW_BRAIN=%s\n' "$BRAIN"
printf 'SHADOW_CORPUS_STATE=%s\n' "$CORPUS_STATE"
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'PRODUCTION_RAW_READ_ONLY_SOURCE=YES\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_WINDOW_SELECTION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$A2_REPO_SHA" = "$EXPECTED_A2_SOURCE" ] || { printf 'HOLD=A2_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$B4_REPO_SHA" = "$EXPECTED_B4_SOURCE" ] || { printf 'HOLD=B4_SOURCE_IDENTITY_MISMATCH\n'; exit 24; }
[ "$C2_REPO_SHA" = "$EXPECTED_C2_SOURCE" ] || { printf 'HOLD=C2_SOURCE_IDENTITY_MISMATCH\n'; exit 25; }
[ -d "$RAW" ] || { printf 'HOLD=PRODUCTION_RAW_CORPUS_MISSING\n'; exit 26; }

RAW_DOC_COUNT_BEFORE=$("$P/bin/find" "$RAW" -maxdepth 1 -type f -name '*.document' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
printf 'RAW_DOCUMENT_COUNT_BEFORE=%s\n' "$RAW_DOC_COUNT_BEFORE"
[ "$RAW_DOC_COUNT_BEFORE" -gt 0 ] || { printf 'HOLD=NO_STORED_DOCUMENTS\n'; exit 27; }

V24_PID_BEFORE=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_BEFORE=%s\n' "$V24_PID_BEFORE"
[ -n "$V24_PID_BEFORE" ] || { printf 'HOLD=PRODUCTION_V24_NOT_RUNNING\n'; exit 28; }

CORPUS_MANIFEST_BEFORE=$(corpus_manifest)
printf 'CORPUS_MANIFEST_SHA256_BEFORE=%s\n' "$CORPUS_MANIFEST_BEFORE"

install_compile() {
    LABEL="$1"
    REL="$2"
    SRC="$3"
    BC="$4"
    EXPECTED="$5"

    cp -- "$REPO/$REL" "$SRC" || return 1
    INSTALLED=$(hash1 "$SRC")
    printf '%s_INSTALLED_SOURCE_SHA256=%s\n' "$LABEL" "$INSTALLED"
    [ "$INSTALLED" = "$EXPECTED" ] || return 2

    rm -f -- "$BC.partial"
    "$SIGMAC" "$SRC" "$BC.partial"
    RC=$?
    printf '%s_SIGMAC_RC=%s\n' "$LABEL" "$RC"
    [ "$RC" -eq 0 ] || return 3
    [ -s "$BC.partial" ] || return 4

    mv -f -- "$BC.partial" "$BC" || return 5
    chmod 0400 "$BC" || return 6
    printf '%s_BYTECODE_SHA256=%s\n' "$LABEL" "$(hash1 "$BC")"
    return 0
}

install_compile A2 "$A2_REL" "$A2_SRC" "$A2_BC" "$EXPECTED_A2_SOURCE" || { printf 'HOLD=A2_COMPILE_OR_INSTALL_FAILED\n'; exit 31; }
install_compile B4 "$B4_REL" "$B4_SRC" "$B4_BC" "$EXPECTED_B4_SOURCE" || { printf 'HOLD=B4_COMPILE_OR_INSTALL_FAILED\n'; exit 32; }
install_compile C2 "$C2_REL" "$C2_SRC" "$C2_BC" "$EXPECTED_C2_SOURCE" || { printf 'HOLD=C2_COMPILE_OR_INSTALL_FAILED\n'; exit 33; }

for F in \
    SIGMA_V4A2_RECOVERED_EVENT.memory \
    SIGMA_V4A2_RECEIVED_WORK.memory \
    SIGMA_V4A2_RETRYABLE_WORK.memory \
    SIGMA_V4A2_LOCAL_WORK.memory \
    SIGMA_V4A2_FETCH_REQUEST.memory \
    SIGMA_V4A2_NEXT_FETCH_NOT_BEFORE.memory \
    SIGMA_V4A2_LAST_SOURCE.memory \
    SIGMA_V4A2_ACTION.memory \
    SIGMA_V4A2_TARGET.memory \
    SIGMA_V4B4_CONTEXT_ID.memory \
    SIGMA_V4B4_CONTEXT_TEXT.memory \
    SIGMA_V4B4_CURSOR.memory \
    SIGMA_V4B4_COMPLETION.memory \
    SIGMA_V4B4_STATUS.memory \
    SIGMA_V4B4_LAST_EVIDENCE.memory \
    SIGMA_V4C2_RAW_DIR.memory \
    SIGMA_V4C2_STATE_DIR.memory \
    SIGMA_V4C2_CORPUS_CURSOR.memory \
    SIGMA_V4C2_ACTIVE_DOC.memory \
    SIGMA_V4C2_STATUS.memory
do
    : > "$E/$F"
done

printf '%s' "$RAW" > "$E/SIGMA_V4C2_RAW_DIR.memory"
printf '%s' "$CORPUS_STATE" > "$E/SIGMA_V4C2_STATE_DIR.memory"
printf '%s' '4102444800' > "$E/SIGMA_V4A2_NEXT_FETCH_NOT_BEFORE.memory"

run_vm() {
    LABEL="$1"
    BC="$2"
    RUNLOG="$3"

    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?

    printf '%s_VM_RC=%s LOG=%s\n' "$LABEL" "$RC" "$RUNLOG"
    return "$RC"
}

MANAGER_CALLS=0
ARBITER_CALLS=0
LEARNER_CALLS=0
WAIT_CALLS=0
RECEIVED_DISPATCHES=0
RETRYABLE_DISPATCHES=0

I=0
while [ "$I" -lt "$FIXED_CONTROLLER_TURNS" ]; do
    MLOG="$LOG/turn.$I.manager.log"
    ALOG="$LOG/turn.$I.arbiter.log"
    BLOG="$LOG/turn.$I.learner.log"

    run_vm MANAGER "$C2_BC" "$MLOG" || {
        printf 'HOLD=MANAGER_VM_FAILURE TURN=%s\n' "$I"
        exit 41
    }
    MANAGER_CALLS=$((MANAGER_CALLS + 1))

    run_vm ARBITER "$A2_BC" "$ALOG" || {
        printf 'HOLD=ARBITER_VM_FAILURE TURN=%s\n' "$I"
        exit 42
    }
    ARBITER_CALLS=$((ARBITER_CALLS + 1))

    NATIVE_ACTION=$(cat "$ACTION")
    NATIVE_TARGET=$(cat "$TARGET")

    printf 'CONTROLLER_TURN=%s ACTION=%s TARGET=%s\n' "$I" "$NATIVE_ACTION" "$NATIVE_TARGET"

    case "$NATIVE_ACTION" in
        LEARN_RECEIVED_CONTEXT)
            ACTIVE_CONTEXT=$(cat "$B4_CONTEXT")
            [ "$NATIVE_TARGET" = "$ACTIVE_CONTEXT" ] || {
                printf 'HOLD=NATIVE_TARGET_CONTEXT_MISMATCH TURN=%s ACTION=%s\n' "$I" "$NATIVE_ACTION"
                exit 43
            }
            RECEIVED_DISPATCHES=$((RECEIVED_DISPATCHES + 1))
            run_vm LEARNER "$B4_BC" "$BLOG" || {
                printf 'HOLD=LEARNER_VM_FAILURE TURN=%s\n' "$I"
                exit 44
            }
            LEARNER_CALLS=$((LEARNER_CALLS + 1))
            ;;
        RESUME_RETRYABLE_CONTEXT)
            ACTIVE_CONTEXT=$(cat "$B4_CONTEXT")
            [ "$NATIVE_TARGET" = "$ACTIVE_CONTEXT" ] || {
                printf 'HOLD=NATIVE_TARGET_CONTEXT_MISMATCH TURN=%s ACTION=%s\n' "$I" "$NATIVE_ACTION"
                exit 45
            }
            RETRYABLE_DISPATCHES=$((RETRYABLE_DISPATCHES + 1))
            run_vm LEARNER "$B4_BC" "$BLOG" || {
                printf 'HOLD=LEARNER_VM_FAILURE TURN=%s\n' "$I"
                exit 46
            }
            LEARNER_CALLS=$((LEARNER_CALLS + 1))
            ;;
        WAIT_NO_ELIGIBLE_WORK)
            WAIT_CALLS=$((WAIT_CALLS + 1))
            ;;
        *)
            printf 'HOLD=UNSUPPORTED_NATIVE_ACTION TURN=%s ACTION=%s TARGET=%s\n' "$I" "$NATIVE_ACTION" "$NATIVE_TARGET"
            exit 47
            ;;
    esac

    I=$((I + 1))
done

COMPLETE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.complete' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
HOLD_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.hold' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
EVIDENCE_FILE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.evidence' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
EVIDENCE_COMMIT_COUNT=$("$P/bin/grep" -h -c 'COMMIT=YES' "$CORPUS_STATE"/*.evidence 2>/dev/null | "$P/bin/awk" '{s+=$1} END {print s+0}')

printf 'MANAGER_CALLS=%s\n' "$MANAGER_CALLS"
printf 'ARBITER_CALLS=%s\n' "$ARBITER_CALLS"
printf 'LEARNER_CALLS=%s\n' "$LEARNER_CALLS"
printf 'WAIT_CALLS=%s\n' "$WAIT_CALLS"
printf 'RECEIVED_DISPATCHES=%s\n' "$RECEIVED_DISPATCHES"
printf 'RETRYABLE_DISPATCHES=%s\n' "$RETRYABLE_DISPATCHES"
printf 'SHADOW_COMPLETE_DOCUMENT_COUNT=%s\n' "$COMPLETE_COUNT"
printf 'SHADOW_HELD_DOCUMENT_COUNT=%s\n' "$HOLD_COUNT"
printf 'SHADOW_EVIDENCE_FILE_COUNT=%s\n' "$EVIDENCE_FILE_COUNT"
printf 'SHADOW_EVIDENCE_COMMIT_COUNT=%s\n' "$EVIDENCE_COMMIT_COUNT"
printf 'FINAL_MANAGER_STATUS=%s\n' "$(cat "$MANAGER_STATUS")"

[ "$LEARNER_CALLS" -gt 0 ] || { printf 'HOLD=NO_NATIVE_CORPUS_LEARNING_OCCURRED\n'; exit 50; }
[ "$EVIDENCE_COMMIT_COUNT" -gt 0 ] || { printf 'HOLD=NO_NATIVE_EVIDENCE_ARCHIVED\n'; exit 51; }

CORPUS_MANIFEST_AFTER=$(corpus_manifest)
RAW_DOC_COUNT_AFTER=$("$P/bin/find" "$RAW" -maxdepth 1 -type f -name '*.document' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
printf 'CORPUS_MANIFEST_SHA256_AFTER=%s\n' "$CORPUS_MANIFEST_AFTER"
printf 'RAW_DOCUMENT_COUNT_AFTER=%s\n' "$RAW_DOC_COUNT_AFTER"

[ "$CORPUS_MANIFEST_AFTER" = "$CORPUS_MANIFEST_BEFORE" ] || { printf 'HOLD=PRODUCTION_RAW_CORPUS_CHANGED\n'; exit 52; }
[ "$RAW_DOC_COUNT_AFTER" = "$RAW_DOC_COUNT_BEFORE" ] || { printf 'HOLD=PRODUCTION_RAW_DOCUMENT_COUNT_CHANGED\n'; exit 53; }

V24_PID_AFTER=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AFTER=%s\n' "$V24_PID_AFTER"
[ "$V24_PID_AFTER" = "$V24_PID_BEFORE" ] || { printf 'HOLD=PRODUCTION_V24_PID_CHANGED\n'; exit 54; }

printf '\nV4C2_FULL_CORPUS_SHADOW_PREFLIGHT=PASS\n'
printf 'EXISTING_STORED_CORPUS_NATIVE_DOCUMENT_SELECTION=PASS_IN_REAL_CORPUS_PREFLIGHT_SCOPE\n'
printf 'NATIVE_PER_DOCUMENT_SEGMENT_CURSOR=PASS_IN_REAL_CORPUS_PREFLIGHT_SCOPE\n'
printf 'COMPACT_ARBITER_STATE_NO_65_RECORD_LEDGER=PASS_IN_COMPOSED_RUNTIME_SCOPE\n'
printf 'COMPACT_LEARNER_CURSOR_NO_128_RECORD_PROGRESS_LEDGER=PASS_IN_COMPOSED_RUNTIME_SCOPE\n'
printf 'MULTI_SPAN_2_3_4_TOKEN_STRUCTURAL_LEARNING=PASS_IN_EXECUTED_WINDOWS_SCOPE\n'
printf 'PRODUCTION_RAW_BYTES_PRESERVED=PASS\n'
printf 'SHADOW_STATE_NAMESPACE_ISOLATION=PASS\n'
printf 'PRODUCTION_V24_REMAINED_RUNNING_SAME_PID=PASS\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_WINDOW_SELECTION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'FULL_CORPUS_COMPLETION=NOT_REQUIRED_BY_THIS_FIXED_TURN_PREFLIGHT\n'
printf 'DIRECTORY_SCALE_STEP_LIMIT=OBSERVED_ONLY_FOR_THIS_REAL_CORPUS_RUN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'V4_PRODUCTION_PROMOTION_ALLOWED=NO\n'
printf 'NEXT_ACTION=CHECKPOINT_THEN_LAUNCH_PERSISTENT_V4C2_FULL_CORPUS_CONTINUOUS_SHADOW\n'
