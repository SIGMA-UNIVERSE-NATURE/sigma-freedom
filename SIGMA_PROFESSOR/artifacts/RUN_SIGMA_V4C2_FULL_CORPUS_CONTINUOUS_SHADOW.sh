#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
PROD_STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
RAW="$PROD_STATE/raw"

STATE="$HOME_SIGMA/SIGMA_V4C2_FULL_CORPUS_CONTINUOUS_SHADOW"
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
B4_CONTEXT="$E/SIGMA_V4B4_CONTEXT_ID.memory"

IDLE_SLEEP_SECONDS=${IDLE_SLEEP_SECONDS:-2}
HEALTH_CHECK_TURNS=${HEALTH_CHECK_TURNS:-100}

mkdir -p "$E" "$CORPUS_STATE" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C2_CONTINUOUS_SHADOW_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
A2_REPO_SHA=$(hash1 "$REPO/$A2_REL")
B4_REPO_SHA=$(hash1 "$REPO/$B4_REL")
C2_REPO_SHA=$(hash1 "$REPO/$C2_REL")

printf 'SIGMA_V4C2_FULL_CORPUS_CONTINUOUS_SHADOW=START\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'A2_SOURCE_SHA256=%s\n' "$A2_REPO_SHA"
printf 'B4_SOURCE_SHA256=%s\n' "$B4_REPO_SHA"
printf 'C2_SOURCE_SHA256=%s\n' "$C2_REPO_SHA"
printf 'CORPUS_SOURCE=%s\n' "$RAW"
printf 'SHADOW_STATE=%s\n' "$STATE"
printf 'EXISTING_STORED_CORPUS_PRIMARY=YES\n'
printf 'EXTERNAL_FETCH_ENABLED=NO\n'
printf 'HOST_DOCUMENT_SELECTION=NO\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_WINDOW_SELECTION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'PRODUCTION_RAW_READ_ONLY_SOURCE=YES\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$A2_REPO_SHA" = "$EXPECTED_A2_SOURCE" ] || { printf 'HOLD=A2_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$B4_REPO_SHA" = "$EXPECTED_B4_SOURCE" ] || { printf 'HOLD=B4_SOURCE_IDENTITY_MISMATCH\n'; exit 24; }
[ "$C2_REPO_SHA" = "$EXPECTED_C2_SOURCE" ] || { printf 'HOLD=C2_SOURCE_IDENTITY_MISMATCH\n'; exit 25; }
[ -d "$RAW" ] || { printf 'HOLD=PRODUCTION_RAW_CORPUS_MISSING\n'; exit 26; }

V24_PID=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AT_SHADOW_START=%s\n' "$V24_PID"
[ -n "$V24_PID" ] || { printf 'HOLD=PRODUCTION_V24_NOT_RUNNING\n'; exit 27; }

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
    [ -e "$E/$F" ] || : > "$E/$F"
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

    if [ "$RC" -ne 0 ]; then
        printf 'HOLD=%s_VM_FAILURE RC=%s LOG=%s\n' "$LABEL" "$RC" "$RUNLOG"
        return "$RC"
    fi
    return 0
}

TURN=0
while :; do
    TS=$("$P/bin/date" -u +%Y%m%dT%H%M%SZ)
    MLOG="$LOG/$TS.$TURN.manager.log"
    ALOG="$LOG/$TS.$TURN.arbiter.log"
    BLOG="$LOG/$TS.$TURN.learner.log"

    run_vm MANAGER "$C2_BC" "$MLOG" || exit 41
    run_vm ARBITER "$A2_BC" "$ALOG" || exit 42

    NATIVE_ACTION=$(cat "$ACTION")
    NATIVE_TARGET=$(cat "$TARGET")

    printf 'V4C2_TURN=%s ACTION=%s TARGET=%s\n' "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET"

    case "$NATIVE_ACTION" in
        LEARN_RECEIVED_CONTEXT|RESUME_RETRYABLE_CONTEXT)
            ACTIVE_CONTEXT=$(cat "$B4_CONTEXT")
            [ "$NATIVE_TARGET" = "$ACTIVE_CONTEXT" ] || {
                printf 'HOLD=NATIVE_TARGET_CONTEXT_MISMATCH TURN=%s ACTION=%s TARGET=%s ACTIVE=%s\n' \
                    "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET" "$ACTIVE_CONTEXT"
                exit 43
            }
            run_vm LEARNER "$B4_BC" "$BLOG" || exit 44
            "$P/bin/tail" -n 10 "$BLOG"
            ;;
        WAIT_NO_ELIGIBLE_WORK)
            "$P/bin/sleep" "$IDLE_SLEEP_SECONDS"
            ;;
        *)
            printf 'HOLD=UNSUPPORTED_NATIVE_ACTION TURN=%s ACTION=%s TARGET=%s\n' \
                "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET"
            exit 45
            ;;
    esac

    TURN=$((TURN + 1))

    if [ $((TURN % HEALTH_CHECK_TURNS)) -eq 0 ]; then
        V24_NOW=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
        COMPLETE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.complete' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
        HOLD_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.hold' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
        ACTIVE_DOC=$(cat "$E/SIGMA_V4C2_ACTIVE_DOC.memory")
        printf 'V4C2_HEALTH TURN=%s COMPLETE_DOCS=%s HOLD_DOCS=%s ACTIVE_DOC=%s V24_PID=%s\n' \
            "$TURN" "$COMPLETE_COUNT" "$HOLD_COUNT" "$ACTIVE_DOC" "$V24_NOW"

        [ "$V24_NOW" = "$V24_PID" ] || {
            printf 'HOLD=PRODUCTION_V24_PID_CHANGED_OR_STOPPED EXPECTED=%s ACTUAL=%s\n' "$V24_PID" "$V24_NOW"
            exit 46
        }
    fi
done
