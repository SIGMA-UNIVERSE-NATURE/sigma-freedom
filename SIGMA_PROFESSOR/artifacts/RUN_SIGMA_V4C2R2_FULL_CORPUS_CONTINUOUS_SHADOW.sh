#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
PROD_STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
RAW="$PROD_STATE/raw"

STATE="$HOME_SIGMA/SIGMA_V4C2R2_FULL_CORPUS_CONTINUOUS_SHADOW"
SHADOW="$STATE/shadow"
BRAIN="$SHADOW/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
CORPUS_STATE="$STATE/corpus_state"
LOG="$STATE/log"
LOCK="$STATE/runner.lock"

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

EXPECTED_A3_SHA256=5e1795b53bb8cf4633219bd789ef0c7a6a168a5102bcc0a31d922ca77333ecef
EXPECTED_B4_SHA256=18b3fc60ba86635a524a5d9268326bc7bf692a82227d86f8bd269d38e8845932
EXPECTED_C2_SHA256=5f46d32f573e87e60a813b9d4f764c783395ed6250ca88b44c463179a600013d

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

IDLE_SLEEP_SECONDS=${IDLE_SLEEP_SECONDS:-2}
HEALTH_CHECK_TURNS=${HEALTH_CHECK_TURNS:-100}

mkdir -p "$E" "$CORPUS_STATE" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C2R2_CONTINUOUS_SHADOW_ALREADY_RUNNING\n'
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

printf 'SIGMA_V4C2R2_FULL_CORPUS_CONTINUOUS_SHADOW=START\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'CORPUS_SOURCE=%s\n' "$RAW"
printf 'SHADOW_STATE=%s\n' "$STATE"
printf 'SHADOW_CORPUS_STATE=%s\n' "$CORPUS_STATE"
printf 'PERSISTENT_NATIVE_STATE_ACROSS_RUNNER_RESTART=YES\n'
printf 'EXISTING_STORED_CORPUS_PRIMARY=YES\n'
printf 'EXTERNAL_FETCH_ENABLED=NO\n'
printf 'PRODUCTION_RAW_READ_ONLY_SOURCE=YES\n'
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
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
A3_SHA=$(hash1 "$A3_REPO")
B4_SHA=$(hash1 "$B4_REPO")
C2_SHA=$(hash1 "$C2_REPO")

printf 'A3_GIT_BLOB=%s\n' "$A3_BLOB"
printf 'B4_GIT_BLOB=%s\n' "$B4_BLOB"
printf 'C2_GIT_BLOB=%s\n' "$C2_BLOB"
printf 'A3_SOURCE_SHA256=%s\n' "$A3_SHA"
printf 'B4_SOURCE_SHA256=%s\n' "$B4_SHA"
printf 'C2_SOURCE_SHA256=%s\n' "$C2_SHA"

[ "$A3_BLOB" = "$EXPECTED_A3_BLOB" ] || { printf 'HOLD=A3_SOURCE_BLOB_MISMATCH\n'; exit 27; }
[ "$B4_BLOB" = "$EXPECTED_B4_BLOB" ] || { printf 'HOLD=B4_SOURCE_BLOB_MISMATCH\n'; exit 28; }
[ "$C2_BLOB" = "$EXPECTED_C2_BLOB" ] || { printf 'HOLD=C2_SOURCE_BLOB_MISMATCH\n'; exit 29; }
[ "$A3_SHA" = "$EXPECTED_A3_SHA256" ] || { printf 'HOLD=A3_SOURCE_SHA256_MISMATCH\n'; exit 30; }
[ "$B4_SHA" = "$EXPECTED_B4_SHA256" ] || { printf 'HOLD=B4_SOURCE_SHA256_MISMATCH\n'; exit 31; }
[ "$C2_SHA" = "$EXPECTED_C2_SHA256" ] || { printf 'HOLD=C2_SOURCE_SHA256_MISMATCH\n'; exit 32; }

V24_PID=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AT_SHADOW_START=%s\n' "$V24_PID"
[ -n "$V24_PID" ] || { printf 'HOLD=PRODUCTION_V24_NOT_RUNNING\n'; exit 33; }

install_compile() {
    LABEL="$1"
    REPO_SRC="$2"
    SRC="$3"
    BC="$4"
    EXPECTED_BLOB="$5"
    EXPECTED_SHA="$6"

    cp -- "$REPO_SRC" "$SRC" || return 1
    INSTALLED_BLOB=$(git -C "$REPO" hash-object "$SRC")
    INSTALLED_SHA=$(hash1 "$SRC")
    printf '%s_INSTALLED_GIT_BLOB=%s\n' "$LABEL" "$INSTALLED_BLOB"
    printf '%s_INSTALLED_SOURCE_SHA256=%s\n' "$LABEL" "$INSTALLED_SHA"
    [ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || return 2
    [ "$INSTALLED_SHA" = "$EXPECTED_SHA" ] || return 3

    rm -f -- "$BC.partial"
    "$SIGMAC" "$SRC" "$BC.partial"
    RC=$?
    printf '%s_SIGMAC_RC=%s\n' "$LABEL" "$RC"
    [ "$RC" -eq 0 ] || return 4
    [ -s "$BC.partial" ] || return 5
    mv -f -- "$BC.partial" "$BC" || return 6
    chmod 0400 "$BC" || return 7
    printf '%s_BYTECODE_SHA256=%s\n' "$LABEL" "$(hash1 "$BC")"
    return 0
}

install_compile A3 "$A3_REPO" "$A3_SRC" "$A3_BC" "$EXPECTED_A3_BLOB" "$EXPECTED_A3_SHA256" || { printf 'HOLD=A3_COMPILE_OR_INSTALL_FAILED\n'; exit 40; }
install_compile B4 "$B4_REPO" "$B4_SRC" "$B4_BC" "$EXPECTED_B4_BLOB" "$EXPECTED_B4_SHA256" || { printf 'HOLD=B4_COMPILE_OR_INSTALL_FAILED\n'; exit 41; }
install_compile C2 "$C2_REPO" "$C2_SRC" "$C2_BC" "$EXPECTED_C2_BLOB" "$EXPECTED_C2_SHA256" || { printf 'HOLD=C2_COMPILE_OR_INSTALL_FAILED\n'; exit 42; }

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
    [ -e "$E/$F" ] || : > "$E/$F"
done

# Mechanical wiring only. Native C2 owns phase, scan cursor, active document,
# priority, retry and completion state. Existing state is never reset here.
printf '%s' "$RAW" > "$E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$CORPUS_STATE" > "$E/SIGMA_V4C2R2_STATE_DIR.memory"

run_vm() {
    LABEL="$1"
    BC="$2"
    RUNLOG="$3"

    (
        cd "$BRAIN" || exit 70
        "$VM" "$BC"
    ) > "$RUNLOG" 2>&1
    RC=$?

    if [ "$RC" -ne 0 ]; then
        printf 'HOLD=%s_VM_FAILURE RC=%s LOG=%s\n' "$LABEL" "$RC" "$RUNLOG"
        return "$RC"
    fi
    return 0
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

START_PROFILE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.profile' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
START_COMPLETE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.complete' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
START_HOLD_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.hold' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
printf 'RESUME_PROFILE_COUNT=%s\n' "$START_PROFILE_COUNT"
printf 'RESUME_COMPLETE_COUNT=%s\n' "$START_COMPLETE_COUNT"
printf 'RESUME_HOLD_COUNT=%s\n' "$START_HOLD_COUNT"
[ "$START_HOLD_COUNT" -eq 0 ] || { printf 'HOLD=PREEXISTING_NATIVE_DOCUMENT_HOLD COUNT=%s\n' "$START_HOLD_COUNT"; exit 43; }

TURN=0
while :; do
    TS=$("$P/bin/date" -u +%Y%m%dT%H%M%SZ)
    MLOG="$LOG/$TS.$TURN.manager.log"
    ALOG="$LOG/$TS.$TURN.arbiter.log"
    BLOG="$LOG/$TS.$TURN.learner.log"

    run_vm MANAGER "$C2_BC" "$MLOG" || exit 50

    if "$P/bin/grep" -F 'STATUS REFUSE_' "$MLOG" >/dev/null 2>&1; then
        printf 'HOLD=NATIVE_MANAGER_REFUSAL TURN=%s LOG=%s\n' "$TURN" "$MLOG"
        exit 51
    fi

    if "$P/bin/grep" -F 'DOCUMENT_HELD 1' "$MLOG" >/dev/null 2>&1; then
        printf 'HOLD=NATIVE_DOCUMENT_HOLD TURN=%s LOG=%s\n' "$TURN" "$MLOG"
        exit 52
    fi

    run_vm ARBITER "$A3_BC" "$ALOG" || exit 53

    NATIVE_ACTION=$(cat "$ACTION")
    NATIVE_TARGET=$(cat "$TARGET")

    printf 'V4C2R2_TURN=%s ACTION=%s TARGET=%s\n' "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET"

    case "$NATIVE_ACTION" in
        DISPATCH_NATIVE_CORPUS_READ_REQUEST)
            transport_exact_native_line_request "$TURN" "$NATIVE_TARGET" || {
                RC=$?
                printf 'HOLD=CORPUS_TRANSPORT_FAILURE TURN=%s RC=%s TARGET=%s\n' "$TURN" "$RC" "$NATIVE_TARGET"
                exit 54
            }
            ;;
        LEARN_RECEIVED_CONTEXT|RESUME_RETRYABLE_CONTEXT)
            ACTIVE_CONTEXT=$(cat "$B4_CONTEXT")
            [ "$NATIVE_TARGET" = "$ACTIVE_CONTEXT" ] || {
                printf 'HOLD=NATIVE_TARGET_CONTEXT_MISMATCH TURN=%s ACTION=%s TARGET=%s ACTIVE=%s\n' \
                    "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET" "$ACTIVE_CONTEXT"
                exit 55
            }
            run_vm LEARNER "$B4_BC" "$BLOG" || exit 56
            ;;
        WAIT_NO_ELIGIBLE_WORK)
            "$P/bin/sleep" "$IDLE_SLEEP_SECONDS"
            ;;
        *)
            printf 'HOLD=UNSUPPORTED_NATIVE_ACTION TURN=%s ACTION=%s TARGET=%s\n' \
                "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET"
            exit 57
            ;;
    esac

    TURN=$((TURN + 1))

    if [ $((TURN % HEALTH_CHECK_TURNS)) -eq 0 ]; then
        V24_NOW=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
        PROFILE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.profile' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
        COMPLETE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.complete' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
        HOLD_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.hold' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
        EVIDENCE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.evidence' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
        PHASE=$(cat "$E/SIGMA_V4C2R2_PHASE.memory")
        ACTIVE_DOC=$(cat "$E/SIGMA_V4C2R2_ACTIVE_DOC.memory")
        STATUS=$(cat "$MANAGER_STATUS")

        printf 'V4C2R2_HEALTH TURN=%s PHASE=%s PROFILE_DOCS=%s COMPLETE_DOCS=%s HOLD_DOCS=%s EVIDENCE_DOCS=%s ACTIVE_DOC=%s MANAGER_STATUS=%s V24_PID=%s\n' \
            "$TURN" "$PHASE" "$PROFILE_COUNT" "$COMPLETE_COUNT" "$HOLD_COUNT" "$EVIDENCE_COUNT" "$ACTIVE_DOC" "$STATUS" "$V24_NOW"

        [ "$V24_NOW" = "$V24_PID" ] || {
            printf 'HOLD=PRODUCTION_V24_PID_CHANGED_OR_STOPPED EXPECTED=%s ACTUAL=%s\n' "$V24_PID" "$V24_NOW"
            exit 58
        }

        [ "$HOLD_COUNT" -eq 0 ] || {
            printf 'HOLD=REAL_CORPUS_DOCUMENT_HOLD_OBSERVED COUNT=%s\n' "$HOLD_COUNT"
            exit 59
        }
    fi
done
