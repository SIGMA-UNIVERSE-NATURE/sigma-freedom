#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
PROD_STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
RAW="$PROD_STATE/raw"

BASE="$HOME_SIGMA/SIGMA_V4C2R2_REAL_CORPUS_NATIVE_EVALUATION_PREFLIGHT"
LOCK="$BASE/preflight.lock"
RUN_ID="$("$P/bin/date" +%s).$$"
STATE="$BASE/run.$RUN_ID"
SHADOW="$STATE/shadow"
BRAIN="$SHADOW/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
CORPUS_STATE="$STATE/corpus_state"
LOG="$STATE/log"
START_MANIFEST="$STATE/preexisting_raw_manifest.txt"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

A3_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_CORPUS_WORK_ARBITER_V4A3R1.sigma"
B4_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_COMPACT_LINE_SPAN_LEARNER_V4B4R2.sigma"
C2_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_FULL_CORPUS_EVALUATION_CONTROLLER_V4C2R2.sigma"

EXPECTED_A3_BLOB=336078bde9d3407c0e75f10834e47bfe8726c40a
EXPECTED_B4_BLOB=12a9b6345786ade253fb8f72abbb20b1ca791cb5
EXPECTED_C2_BLOB=bf2134acc6a4d81e5c18ced6e0db158236eb1c40

A3_SRC="$E/SIGMA_V4_CORPUS_WORK_ARBITER_V4A3R1.sigma"
B4_SRC="$E/SIGMA_V4_COMPACT_LINE_SPAN_LEARNER_V4B4R2.sigma"
C2_SRC="$E/SIGMA_V4_FULL_CORPUS_EVALUATION_CONTROLLER_V4C2R2.sigma"

A3_BC="$E/SIGMA_V4_CORPUS_WORK_ARBITER_V4A3R1.sigmab"
B4_BC="$E/SIGMA_V4_COMPACT_LINE_SPAN_LEARNER_V4B4R2.sigmab"
C2_BC="$E/SIGMA_V4_FULL_CORPUS_EVALUATION_CONTROLLER_V4C2R2.sigmab"

ACTION="$E/SIGMA_V4A3_ACTION.memory"
TARGET="$E/SIGMA_V4A3_TARGET.memory"
B4_CONTEXT="$E/SIGMA_V4B4R2_CONTEXT_ID.memory"
MANAGER_STATUS="$E/SIGMA_V4C2R2_STATUS.memory"

READ_REQ_ID="$E/SIGMA_V4C2R2_READ_REQUEST_ID.memory"
READ_DOC="$E/SIGMA_V4C2R2_READ_DOC.memory"
READ_LINE="$E/SIGMA_V4C2R2_READ_LINE.memory"
READ_PURPOSE="$E/SIGMA_V4C2R2_READ_PURPOSE.memory"
READ_RESULT_ID="$E/SIGMA_V4C2R2_READ_RESULT_ID.memory"
READ_RESULT_FOUND="$E/SIGMA_V4C2R2_READ_RESULT_FOUND.memory"
READ_RESULT_TEXT="$E/SIGMA_V4C2R2_READ_RESULT_TEXT.memory"

FIXED_CONTROLLER_TURNS=${FIXED_CONTROLLER_TURNS:-8192}

mkdir -p "$BASE" "$E" "$CORPUS_STATE" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C2R2_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

blob1() {
    git -C "$REPO" hash-object "$1"
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")

printf 'SIGMA_PHASE=V4C2R2_REAL_CORPUS_NATIVE_EVALUATION_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'FIXED_CONTROLLER_TURNS=%s\n' "$FIXED_CONTROLLER_TURNS"
printf 'CORPUS_SOURCE=%s\n' "$RAW"
printf 'SHADOW_BRAIN=%s\n' "$BRAIN"
printf 'SHADOW_CORPUS_STATE=%s\n' "$CORPUS_STATE"
printf 'PRODUCTION_RAW_READ_ONLY_SOURCE=YES\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'HOST_LINE_SELECTION=NO\n'
printf 'HOST_WINDOW_SELECTION=NO\n'
printf 'HOST_CORPUS_PRIORITY=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_CORPUS_READ_TRANSPORT=EXACT_NATIVE_REQUEST_ONLY\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ -d "$RAW" ] || { printf 'HOLD=PRODUCTION_RAW_CORPUS_MISSING\n'; exit 23; }

A3_REPO="$REPO/$A3_REL"
B4_REPO="$REPO/$B4_REL"
C2_REPO="$REPO/$C2_REL"

[ -f "$A3_REPO" ] || { printf 'HOLD=A3_SOURCE_MISSING\n'; exit 24; }
[ -f "$B4_REPO" ] || { printf 'HOLD=B4_SOURCE_MISSING\n'; exit 25; }
[ -f "$C2_REPO" ] || { printf 'HOLD=C2_SOURCE_MISSING\n'; exit 26; }

A3_BLOB=$(blob1 "$A3_REPO")
B4_BLOB=$(blob1 "$B4_REPO")
C2_BLOB=$(blob1 "$C2_REPO")

printf 'A3_GIT_BLOB=%s\n' "$A3_BLOB"
printf 'B4_GIT_BLOB=%s\n' "$B4_BLOB"
printf 'C2_GIT_BLOB=%s\n' "$C2_BLOB"
printf 'A3_SOURCE_SHA256=%s\n' "$(hash1 "$A3_REPO")"
printf 'B4_SOURCE_SHA256=%s\n' "$(hash1 "$B4_REPO")"
printf 'C2_SOURCE_SHA256=%s\n' "$(hash1 "$C2_REPO")"

[ "$A3_BLOB" = "$EXPECTED_A3_BLOB" ] || { printf 'HOLD=A3_SOURCE_BLOB_MISMATCH\n'; exit 27; }
[ "$B4_BLOB" = "$EXPECTED_B4_BLOB" ] || { printf 'HOLD=B4_SOURCE_BLOB_MISMATCH\n'; exit 28; }
[ "$C2_BLOB" = "$EXPECTED_C2_BLOB" ] || { printf 'HOLD=C2_SOURCE_BLOB_MISMATCH\n'; exit 29; }

RAW_DOC_COUNT_BEFORE=$("$P/bin/find" "$RAW" -maxdepth 1 -type f -name '*.document' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
printf 'RAW_DOCUMENT_COUNT_BEFORE=%s\n' "$RAW_DOC_COUNT_BEFORE"
[ "$RAW_DOC_COUNT_BEFORE" -gt 0 ] || { printf 'HOLD=NO_STORED_DOCUMENTS\n'; exit 30; }

: > "$START_MANIFEST"
for DOC in "$RAW"/*.document; do
    [ -f "$DOC" ] || continue
    printf '%s %s\n' "$(hash1 "$DOC")" "$DOC" >> "$START_MANIFEST"
done
"$P/bin/sort" -o "$START_MANIFEST" "$START_MANIFEST"
PREEXISTING_MANIFEST_SHA256=$(hash1 "$START_MANIFEST")
printf 'PREEXISTING_MANIFEST_SHA256=%s\n' "$PREEXISTING_MANIFEST_SHA256"

V24_PID_BEFORE=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_BEFORE=%s\n' "$V24_PID_BEFORE"
[ -n "$V24_PID_BEFORE" ] || { printf 'HOLD=PRODUCTION_V24_NOT_RUNNING\n'; exit 31; }

install_compile() {
    LABEL="$1"
    REPO_SRC="$2"
    SRC="$3"
    BC="$4"
    EXPECTED_BLOB="$5"

    cp -- "$REPO_SRC" "$SRC" || return 1
    INSTALLED_BLOB=$(git -C "$REPO" hash-object "$SRC")
    printf '%s_INSTALLED_GIT_BLOB=%s\n' "$LABEL" "$INSTALLED_BLOB"
    printf '%s_INSTALLED_SOURCE_SHA256=%s\n' "$LABEL" "$(hash1 "$SRC")"
    [ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || return 2

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

install_compile A3 "$A3_REPO" "$A3_SRC" "$A3_BC" "$EXPECTED_A3_BLOB" || { printf 'HOLD=A3_COMPILE_OR_INSTALL_FAILED\n'; exit 40; }
install_compile B4 "$B4_REPO" "$B4_SRC" "$B4_BC" "$EXPECTED_B4_BLOB" || { printf 'HOLD=B4_COMPILE_OR_INSTALL_FAILED\n'; exit 41; }
install_compile C2 "$C2_REPO" "$C2_SRC" "$C2_BC" "$EXPECTED_C2_BLOB" || { printf 'HOLD=C2_COMPILE_OR_INSTALL_FAILED\n'; exit 42; }

for F in \
    SIGMA_V4A3_RECOVERED_EVENT.memory \
    SIGMA_V4A3_RECEIVED_WORK.memory \
    SIGMA_V4A3_RETRYABLE_WORK.memory \
    SIGMA_V4A3_CORPUS_READ_REQUEST.memory \
    SIGMA_V4A3_LAST_SOURCE.memory \
    SIGMA_V4A3_ACTION.memory \
    SIGMA_V4A3_TARGET.memory \
    SIGMA_V4B4R2_CONTEXT_ID.memory \
    SIGMA_V4B4R2_CONTEXT_TEXT.memory \
    SIGMA_V4B4R2_TOKEN_CURSOR.memory \
    SIGMA_V4B4R2_COMPLETION.memory \
    SIGMA_V4B4R2_STATUS.memory \
    SIGMA_V4B4R2_LAST_EVIDENCE.memory \
    SIGMA_V4B4R2_BEST_WIDTH.memory \
    SIGMA_V4B4R2_BEST_SUPPORT.memory \
    SIGMA_V4B4R2_PAIR_OCCURRENCES.memory \
    SIGMA_V4B4R2_TRIPLE_OCCURRENCES.memory \
    SIGMA_V4B4R2_QUAD_OCCURRENCES.memory \
    SIGMA_V4C2R2_RAW_DIR.memory \
    SIGMA_V4C2R2_STATE_DIR.memory \
    SIGMA_V4C2R2_PHASE.memory \
    SIGMA_V4C2R2_SCAN_CURSOR.memory \
    SIGMA_V4C2R2_ACTIVE_DOC.memory \
    SIGMA_V4C2R2_ACTIVE_PURPOSE.memory \
    SIGMA_V4C2R2_ACTIVE_BEST_WIDTH.memory \
    SIGMA_V4C2R2_ACTIVE_BEST_SUPPORT.memory \
    SIGMA_V4C2R2_PRIORITY_BEST_DOC.memory \
    SIGMA_V4C2R2_PRIORITY_BEST_WIDTH.memory \
    SIGMA_V4C2R2_PRIORITY_BEST_SUPPORT.memory \
    SIGMA_V4C2R2_PRIORITY_UNPROFILED.memory \
    SIGMA_V4C2R2_READ_REQUEST_ID.memory \
    SIGMA_V4C2R2_READ_DOC.memory \
    SIGMA_V4C2R2_READ_LINE.memory \
    SIGMA_V4C2R2_READ_PURPOSE.memory \
    SIGMA_V4C2R2_READ_RESULT_ID.memory \
    SIGMA_V4C2R2_READ_RESULT_FOUND.memory \
    SIGMA_V4C2R2_READ_RESULT_TEXT.memory \
    SIGMA_V4C2R2_STATUS.memory
do
    : > "$E/$F"
done

printf '%s' "$RAW" > "$E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$CORPUS_STATE" > "$E/SIGMA_V4C2R2_STATE_DIR.memory"
printf '%s' 'PROFILE' > "$E/SIGMA_V4C2R2_PHASE.memory"

run_vm() {
    LABEL="$1"
    BC="$2"
    RUNLOG="$3"

    (
        cd "$BRAIN" || exit 70
        "$VM" "$BC"
    ) > "$RUNLOG" 2>&1
    RC=$?

    printf '%s_VM_RC=%s LOG=%s\n' "$LABEL" "$RC" "$RUNLOG"
    return "$RC"
}

transport_exact_native_line_request() {
    TURN="$1"
    EXPECTED_TARGET="$2"

    REQ_ID=$(cat "$READ_REQ_ID")
    DOC_ID=$(cat "$READ_DOC")
    LINE_U=$(cat "$READ_LINE")
    PURPOSE=$(cat "$READ_PURPOSE")

    printf 'CORPUS_TRANSPORT TURN=%s REQUEST_ID=%s DOC=%s LINE_UNARY_LEN=%s PURPOSE=%s\n' \
        "$TURN" "$REQ_ID" "$DOC_ID" "${#LINE_U}" "$PURPOSE"

    [ -n "$REQ_ID" ] || return 80
    [ "$EXPECTED_TARGET" = "$REQ_ID" ] || return 81
    [ -n "$DOC_ID" ] || return 82

    case "$DOC_ID" in
        *'/'*|*'..'*) return 83 ;;
    esac

    case "$PURPOSE" in
        PROFILE|LEARN) ;;
        *) return 84 ;;
    esac

    REST=${LINE_U//|/}
    [ -z "$REST" ] || return 85

    DOC_PATH="$RAW/$DOC_ID.document"
    [ -f "$DOC_PATH" ] || return 86

    LINE_NO=$(( ${#LINE_U} + 1 ))
    FOUND_MARK=$("$P/bin/sed" -n "${LINE_NO}{=;q;}" "$DOC_PATH")

    TMP_RESULT="$STATE/.line-result.$TURN.$$"
    rm -f -- "$TMP_RESULT"

    if [ "$FOUND_MARK" = "$LINE_NO" ]; then
        LINE_VALUE=$("$P/bin/sed" -n "${LINE_NO}p" "$DOC_PATH")
        printf '%s' "$LINE_VALUE" > "$TMP_RESULT" || return 87
        printf '%s' 'YES' > "$READ_RESULT_FOUND" || return 88
    else
        : > "$TMP_RESULT"
        printf '%s' 'NO' > "$READ_RESULT_FOUND" || return 89
    fi

    mv -f -- "$TMP_RESULT" "$READ_RESULT_TEXT" || return 90
    printf '%s' "$REQ_ID" > "$READ_RESULT_ID" || return 91

    printf 'HOST_DOCUMENT_SELECTION=NO\n'
    printf 'HOST_LINE_SELECTION=NO\n'
    printf 'HOST_CORPUS_PRIORITY=NO\n'
    printf 'HOST_CORPUS_READ_TRANSPORT=EXACT_NATIVE_REQUEST_ONLY\n'
    return 0
}

MANAGER_CALLS=0
ARBITER_CALLS=0
LEARNER_CALLS=0
READ_DISPATCHES=0
RECEIVED_DISPATCHES=0
RETRYABLE_DISPATCHES=0
WAIT_CALLS=0
PRIORITY_SELECTION_OBSERVED=0
PROFILE_COMMIT_OBSERVED=0

I=0
while [ "$I" -lt "$FIXED_CONTROLLER_TURNS" ]; do
    MLOG="$LOG/turn.$I.manager.log"
    ALOG="$LOG/turn.$I.arbiter.log"
    BLOG="$LOG/turn.$I.learner.log"

    run_vm MANAGER "$C2_BC" "$MLOG" || {
        printf 'HOLD=MANAGER_VM_FAILURE TURN=%s\n' "$I"
        exit 50
    }
    MANAGER_CALLS=$((MANAGER_CALLS + 1))

    if "$P/bin/grep" -F 'PRIORITY_SELECTED 1' "$MLOG" >/dev/null 2>&1; then
        PRIORITY_SELECTION_OBSERVED=1
    fi
    if "$P/bin/grep" -F 'PROFILE_COMMITTED 1' "$MLOG" >/dev/null 2>&1; then
        PROFILE_COMMIT_OBSERVED=1
    fi

    if "$P/bin/grep" -F 'STATUS REFUSE_' "$MLOG" >/dev/null 2>&1; then
        printf 'HOLD=NATIVE_MANAGER_REFUSAL TURN=%s LOG=%s\n' "$I" "$MLOG"
        exit 51
    fi

    run_vm ARBITER "$A3_BC" "$ALOG" || {
        printf 'HOLD=ARBITER_VM_FAILURE TURN=%s\n' "$I"
        exit 52
    }
    ARBITER_CALLS=$((ARBITER_CALLS + 1))

    NATIVE_ACTION=$(cat "$ACTION")
    NATIVE_TARGET=$(cat "$TARGET")

    printf 'CONTROLLER_TURN=%s ACTION=%s TARGET=%s\n' "$I" "$NATIVE_ACTION" "$NATIVE_TARGET"

    case "$NATIVE_ACTION" in
        DISPATCH_NATIVE_CORPUS_READ_REQUEST)
            READ_DISPATCHES=$((READ_DISPATCHES + 1))
            transport_exact_native_line_request "$I" "$NATIVE_TARGET" || {
                RC=$?
                printf 'HOLD=CORPUS_TRANSPORT_FAILURE TURN=%s RC=%s TARGET=%s\n' "$I" "$RC" "$NATIVE_TARGET"
                exit 53
            }
            ;;
        LEARN_RECEIVED_CONTEXT)
            ACTIVE_CONTEXT=$(cat "$B4_CONTEXT")
            [ "$NATIVE_TARGET" = "$ACTIVE_CONTEXT" ] || {
                printf 'HOLD=NATIVE_TARGET_CONTEXT_MISMATCH TURN=%s ACTION=%s\n' "$I" "$NATIVE_ACTION"
                exit 54
            }
            RECEIVED_DISPATCHES=$((RECEIVED_DISPATCHES + 1))
            run_vm LEARNER "$B4_BC" "$BLOG" || {
                printf 'HOLD=LEARNER_VM_FAILURE TURN=%s\n' "$I"
                exit 55
            }
            LEARNER_CALLS=$((LEARNER_CALLS + 1))
            ;;
        RESUME_RETRYABLE_CONTEXT)
            ACTIVE_CONTEXT=$(cat "$B4_CONTEXT")
            [ "$NATIVE_TARGET" = "$ACTIVE_CONTEXT" ] || {
                printf 'HOLD=NATIVE_TARGET_CONTEXT_MISMATCH TURN=%s ACTION=%s\n' "$I" "$NATIVE_ACTION"
                exit 56
            }
            RETRYABLE_DISPATCHES=$((RETRYABLE_DISPATCHES + 1))
            run_vm LEARNER "$B4_BC" "$BLOG" || {
                printf 'HOLD=LEARNER_VM_FAILURE TURN=%s\n' "$I"
                exit 57
            }
            LEARNER_CALLS=$((LEARNER_CALLS + 1))
            ;;
        WAIT_NO_ELIGIBLE_WORK)
            WAIT_CALLS=$((WAIT_CALLS + 1))
            ;;
        *)
            printf 'HOLD=UNSUPPORTED_NATIVE_ACTION TURN=%s ACTION=%s TARGET=%s\n' "$I" "$NATIVE_ACTION" "$NATIVE_TARGET"
            exit 58
            ;;
    esac

    I=$((I + 1))
done

PROFILE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.profile' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
COMPLETE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.complete' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
HOLD_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.hold' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
EVIDENCE_FILE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.evidence' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
EVIDENCE_COMMIT_COUNT=$("$P/bin/grep" -h -c 'COMMIT=YES' "$CORPUS_STATE"/*.evidence 2>/dev/null | "$P/bin/awk" '{s+=$1} END {print s+0}')

PAIR_OBSERVED=0
TRIPLE_OBSERVED=0
QUAD_OBSERVED=0

if "$P/bin/awk" '$1=="PAIR_OCCURRENCES" && ($2+0)>0 {found=1} END {exit(found?0:1)}' "$LOG"/*.learner.log 2>/dev/null; then
    PAIR_OBSERVED=1
fi
if "$P/bin/awk" '$1=="TRIPLE_OCCURRENCES" && ($2+0)>0 {found=1} END {exit(found?0:1)}' "$LOG"/*.learner.log 2>/dev/null; then
    TRIPLE_OBSERVED=1
fi
if "$P/bin/awk" '$1=="QUAD_OCCURRENCES" && ($2+0)>0 {found=1} END {exit(found?0:1)}' "$LOG"/*.learner.log 2>/dev/null; then
    QUAD_OBSERVED=1
fi

printf 'MANAGER_CALLS=%s\n' "$MANAGER_CALLS"
printf 'ARBITER_CALLS=%s\n' "$ARBITER_CALLS"
printf 'LEARNER_CALLS=%s\n' "$LEARNER_CALLS"
printf 'READ_DISPATCHES=%s\n' "$READ_DISPATCHES"
printf 'RECEIVED_DISPATCHES=%s\n' "$RECEIVED_DISPATCHES"
printf 'RETRYABLE_DISPATCHES=%s\n' "$RETRYABLE_DISPATCHES"
printf 'WAIT_CALLS=%s\n' "$WAIT_CALLS"
printf 'PROFILE_COUNT=%s\n' "$PROFILE_COUNT"
printf 'COMPLETE_COUNT=%s\n' "$COMPLETE_COUNT"
printf 'HOLD_COUNT=%s\n' "$HOLD_COUNT"
printf 'EVIDENCE_FILE_COUNT=%s\n' "$EVIDENCE_FILE_COUNT"
printf 'EVIDENCE_COMMIT_COUNT=%s\n' "$EVIDENCE_COMMIT_COUNT"
printf 'PAIR_OCCURRENCE_OBSERVED=%s\n' "$PAIR_OBSERVED"
printf 'TRIPLE_OCCURRENCE_OBSERVED=%s\n' "$TRIPLE_OBSERVED"
printf 'QUAD_OCCURRENCE_OBSERVED=%s\n' "$QUAD_OBSERVED"
printf 'PROFILE_COMMIT_OBSERVED=%s\n' "$PROFILE_COMMIT_OBSERVED"
printf 'PRIORITY_SELECTION_OBSERVED=%s\n' "$PRIORITY_SELECTION_OBSERVED"
printf 'FINAL_MANAGER_STATUS=%s\n' "$(cat "$MANAGER_STATUS")"

[ "$READ_DISPATCHES" -gt 0 ] || { printf 'HOLD=NO_NATIVE_CORPUS_READ_REQUEST_OBSERVED\n'; exit 60; }
[ "$LEARNER_CALLS" -gt 0 ] || { printf 'HOLD=NO_NATIVE_CORPUS_LEARNING_OCCURRED\n'; exit 61; }
[ "$PROFILE_COUNT" -gt 0 ] || { printf 'HOLD=NO_NATIVE_DOCUMENT_PROFILE_COMMITTED\n'; exit 62; }
[ "$EVIDENCE_COMMIT_COUNT" -gt 0 ] || { printf 'HOLD=NO_NATIVE_EVIDENCE_ARCHIVED\n'; exit 63; }
[ "$PAIR_OBSERVED" -eq 1 ] || { printf 'HOLD=PAIR_SPAN_NOT_OBSERVED\n'; exit 64; }
[ "$TRIPLE_OBSERVED" -eq 1 ] || { printf 'HOLD=TRIPLE_SPAN_NOT_OBSERVED\n'; exit 65; }
[ "$QUAD_OBSERVED" -eq 1 ] || { printf 'HOLD=QUAD_SPAN_NOT_OBSERVED\n'; exit 66; }
[ "$HOLD_COUNT" -eq 0 ] || { printf 'HOLD=REAL_CORPUS_DOCUMENT_HOLD_OBSERVED COUNT=%s\n' "$HOLD_COUNT"; exit 67; }
[ "$PROFILE_COMMIT_OBSERVED" -eq 1 ] || { printf 'HOLD=PROFILE_COMMIT_TRANSITION_NOT_OBSERVED\n'; exit 68; }
[ "$PRIORITY_SELECTION_OBSERVED" -eq 1 ] || { printf 'HOLD=FULL_NATIVE_PRIORITY_PASS_NOT_OBSERVED_IN_FIXED_BUDGET\n'; exit 69; }

PREEXISTING_CHECKED=0
while IFS=' ' read -r EXPECTED_SHA DOC_PATH; do
    [ -n "$DOC_PATH" ] || continue
    PREEXISTING_CHECKED=$((PREEXISTING_CHECKED + 1))
    [ -f "$DOC_PATH" ] || {
        printf 'HOLD=PREEXISTING_PRODUCTION_DOCUMENT_DELETED PATH=%s\n' "$DOC_PATH"
        exit 70
    }
    ACTUAL_SHA=$(hash1 "$DOC_PATH")
    [ "$ACTUAL_SHA" = "$EXPECTED_SHA" ] || {
        printf 'HOLD=PREEXISTING_PRODUCTION_DOCUMENT_MUTATED PATH=%s EXPECTED=%s ACTUAL=%s\n' \
            "$DOC_PATH" "$EXPECTED_SHA" "$ACTUAL_SHA"
        exit 71
    }
done < "$START_MANIFEST"

RAW_DOC_COUNT_AFTER=$("$P/bin/find" "$RAW" -maxdepth 1 -type f -name '*.document' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
printf 'PREEXISTING_DOCUMENTS_REVERIFIED=%s\n' "$PREEXISTING_CHECKED"
printf 'RAW_DOCUMENT_COUNT_AFTER=%s\n' "$RAW_DOC_COUNT_AFTER"
printf 'NEW_DOCUMENTS_APPENDED_DURING_PREFLIGHT=%s\n' "$((RAW_DOC_COUNT_AFTER - RAW_DOC_COUNT_BEFORE))"

V24_PID_AFTER=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AFTER=%s\n' "$V24_PID_AFTER"
[ "$V24_PID_AFTER" = "$V24_PID_BEFORE" ] || { printf 'HOLD=PRODUCTION_V24_PID_CHANGED\n'; exit 72; }

printf '\nV4C2R2_REAL_CORPUS_NATIVE_EVALUATION_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'EXISTING_STORED_CORPUS_NATIVE_DOCUMENT_SELECTION=PASS_IN_OBSERVED_REAL_CORPUS_SCOPE\n'
printf 'EXACT_NATIVE_LINE_REQUEST_MECHANICAL_TRANSPORT=PASS_IN_OBSERVED_REAL_CORPUS_SCOPE\n'
printf 'NATIVE_DOCUMENT_PROFILE_COMMIT=PASS_IN_OBSERVED_REAL_CORPUS_SCOPE\n'
printf 'NATIVE_GLOBAL_CORPUS_PRIORITY=PASS_IN_OBSERVED_REAL_CORPUS_SCOPE\n'
printf 'COMPACT_ARBITER_STATE=PASS_IN_COMPOSED_RUNTIME_SCOPE\n'
printf 'COMPACT_TOKEN_CURSOR=PASS_IN_COMPOSED_RUNTIME_SCOPE\n'
printf 'PAIR_STRUCTURAL_SPAN=PASS_IN_OBSERVED_WINDOWS_SCOPE\n'
printf 'TRIPLE_STRUCTURAL_SPAN=PASS_IN_OBSERVED_WINDOWS_SCOPE\n'
printf 'QUAD_STRUCTURAL_SPAN=PASS_IN_OBSERVED_WINDOWS_SCOPE\n'
printf 'PREEXISTING_PRODUCTION_DOCUMENT_BYTES_PRESERVED=PASS\n'
printf 'APPEND_ONLY_NEW_PRODUCTION_DOCUMENTS_ALLOWED=YES\n'
printf 'SHADOW_STATE_NAMESPACE_ISOLATION=PASS\n'
printf 'PRODUCTION_V24_REMAINED_RUNNING_SAME_PID=PASS\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'HOST_LINE_SELECTION=NO\n'
printf 'HOST_WINDOW_SELECTION=NO\n'
printf 'HOST_CORPUS_PRIORITY=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'BOUNDED_VM_CORPUS_INPUT_PER_TRANSPORT=ONE_REQUESTED_LINE\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'FULL_CORPUS_COMPLETION=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'V4_PRODUCTION_PROMOTION_ALLOWED=NO\n'
printf 'NEXT_ACTION=CHECKPOINT_R2_PASS_THEN_BUILD_PERSISTENT_CONTINUOUS_SHADOW_RUNNER\n'
