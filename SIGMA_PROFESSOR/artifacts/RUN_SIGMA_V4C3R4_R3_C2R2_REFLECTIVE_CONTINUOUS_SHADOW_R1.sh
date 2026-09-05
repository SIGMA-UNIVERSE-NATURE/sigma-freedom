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
LOG="$STATE/log_reflective_c3r4_r3"
LOCK="$STATE/runner.lock"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

A3_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_CORPUS_WORK_ARBITER_V4A3R1.sigma"
B4_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_COMPACT_LINE_SPAN_LEARNER_V4B4R2.sigma"
C2_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_FULL_CORPUS_EVALUATION_CONTROLLER_V4C2R2.sigma"
C3_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_OPERATIONAL_REFLECTION_PLAN_CONTROLLER_V4C3R4.sigma"
R3_REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_EVIDENCE_FIRST_SELF_VIEW_REPORTER_V4C3R3.sigma"

EXPECTED_A3_BLOB=336078bde9d3407c0e75f10834e47bfe8726c40a
EXPECTED_B4_BLOB=12a9b6345786ade253fb8f72abbb20b1ca791cb5
EXPECTED_C2_BLOB=bf2134acc6a4d81e5c18ced6e0db158236eb1c40
EXPECTED_C3_BLOB=7b826ace6c6f6559a10e6fbd7e7b2d96af1a75cf
EXPECTED_R3_BLOB=c4dd4c3c0b71df46c6e75d3e1c8bc9a782af8f16

EXPECTED_A3_SHA256=5e1795b53bb8cf4633219bd789ef0c7a6a168a5102bcc0a31d922ca77333ecef
EXPECTED_B4_SHA256=18b3fc60ba86635a524a5d9268326bc7bf692a82227d86f8bd269d38e8845932
EXPECTED_C2_SHA256=5f46d32f573e87e60a813b9d4f764c783395ed6250ca88b44c463179a600013d

A3_SRC="$E/SIGMA_V4_CORPUS_WORK_ARBITER_V4A3R1.sigma"
B4_SRC="$E/SIGMA_V4_COMPACT_LINE_SPAN_LEARNER_V4B4R2.sigma"
C2_SRC="$E/SIGMA_V4_FULL_CORPUS_EVALUATION_CONTROLLER_V4C2R2.sigma"
C3_SRC="$E/SIGMA_V4_OPERATIONAL_REFLECTION_PLAN_CONTROLLER_V4C3R4.sigma"
R3_SRC="$E/SIGMA_V4_NATIVE_EVIDENCE_FIRST_SELF_VIEW_REPORTER_V4C3R3.sigma"

A3_BC="$E/SIGMA_V4_CORPUS_WORK_ARBITER_V4A3R1.sigmab"
B4_BC="$E/SIGMA_V4_COMPACT_LINE_SPAN_LEARNER_V4B4R2.sigmab"
C2_BC="$E/SIGMA_V4_FULL_CORPUS_EVALUATION_CONTROLLER_V4C2R2.sigmab"
C3_BC="$E/SIGMA_V4_OPERATIONAL_REFLECTION_PLAN_CONTROLLER_V4C3R4.sigmab"
R3_BC="$E/SIGMA_V4_NATIVE_EVIDENCE_FIRST_SELF_VIEW_REPORTER_V4C3R3.sigmab"

ACTION="$E/SIGMA_V4A3_ACTION.memory"
TARGET="$E/SIGMA_V4A3_TARGET.memory"
B4_CONTEXT="$E/SIGMA_V4B4R2_CONTEXT_ID.memory"
B4_CURSOR="$E/SIGMA_V4B4R2_TOKEN_CURSOR.memory"
B4_EVIDENCE="$E/SIGMA_V4B4R2_LAST_EVIDENCE.memory"
MANAGER_STATUS="$E/SIGMA_V4C2R2_STATUS.memory"
READ_REQ_ID="$E/SIGMA_V4C2R2_READ_REQUEST_ID.memory"
READ_DOC="$E/SIGMA_V4C2R2_READ_DOC.memory"
READ_LINE="$E/SIGMA_V4C2R2_READ_LINE.memory"
READ_PURPOSE="$E/SIGMA_V4C2R2_READ_PURPOSE.memory"
READ_RESULT_ID="$E/SIGMA_V4C2R2_READ_RESULT_ID.memory"
READ_RESULT_FOUND="$E/SIGMA_V4C2R2_READ_RESULT_FOUND.memory"
READ_RESULT_TEXT="$E/SIGMA_V4C2R2_READ_RESULT_TEXT.memory"
C3_REPORT="$E/SIGMA_V4C3R1_LAST_REPORT.memory"
C3_PLAN="$E/SIGMA_V4C3R1_PLAN.memory"
C3_STATUS="$E/SIGMA_V4C3R1_STATUS.memory"
C3_PROGRESS="$E/SIGMA_V4C3R1_PROGRESS.memory"
C3_CYCLE="$E/SIGMA_V4C3R1_CYCLE.memory"
C3_BUDGET="$E/SIGMA_V4C3R1_PROGRESS_BUDGET.memory"
C3_PAUSE="$E/SIGMA_V4C3R1_PAUSE_SECONDS.memory"

IDLE_SLEEP_SECONDS=2
HEALTH_CHECK_TURNS=100
REFLECTION_PROGRESS_BUDGET=256
OBSERVE_PAUSE_SECONDS=180

mkdir -p "$E" "$CORPUS_STATE" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C3R4_R3_C2R2_REFLECTIVE_SHADOW_ALREADY_RUNNING_OR_OLD_RUNNER_STILL_ACTIVE\n'
    exit 20
fi

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }
blob1() { git -C "$REPO" hash-object "$1"; }
make_unary() {
    N="$1"
    OUT=''
    I=0
    while [ "$I" -lt "$N" ]; do OUT="${OUT}|"; I=$((I + 1)); done
    printf '%s' "$OUT"
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
printf 'SIGMA_V4C3R4_R3_C2R2_REFLECTIVE_CONTINUOUS_SHADOW_R1=START\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'CORPUS_SOURCE=%s\n' "$RAW"
printf 'SHADOW_STATE=%s\n' "$STATE"
printf 'PRESERVE_EXISTING_C2R2_NATIVE_STATE=YES\n'
printf 'PRESERVE_EXISTING_C3_STATE_SCHEMA=YES\n'
printf 'REFLECTION_PROGRESS_BUDGET=%s\n' "$REFLECTION_PROGRESS_BUDGET"
printf 'OBSERVE_PAUSE_SECONDS=%s\n' "$OBSERVE_PAUSE_SECONDS"
printf 'R3_REPORTER_DISPATCH_EVENT=EXACT_NATIVE_REPORT_COMMITTED_BEFORE_PAUSE\n'
printf 'EXTERNAL_FETCH_ENABLED=NO\n'
printf 'HOST_DOCUMENT_SELECTION=NO\nHOST_LINE_SELECTION=NO\nHOST_WINDOW_SELECTION=NO\nHOST_CORPUS_PRIORITY=NO\nHOST_RETRY_DECISION=NO\nHOST_COMPLETION_DECISION=NO\nHOST_REFLECTION=NO\nHOST_SELF_ASSESSMENT=NO\nHOST_NEXT_WORK_SELECTION=NO\nHOST_REPORT_SUMMARIZATION=NO\nHOST_REPORT_TRANSLATION=NO\nHOST_SEMANTIC_INTERPRETATION=NO\nHOST_LEARNING=NO\nBASH_LEARNING=NO\nGPT_AS_SIGMA_COGNITION=NO\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ -d "$RAW" ] || { printf 'HOLD=PRODUCTION_RAW_CORPUS_MISSING\n'; exit 23; }

A3_REPO="$REPO/$A3_REL"
B4_REPO="$REPO/$B4_REL"
C2_REPO="$REPO/$C2_REL"
C3_REPO="$REPO/$C3_REL"
R3_REPO="$REPO/$R3_REL"

[ -f "$A3_REPO" ] || { printf 'HOLD=A3_SOURCE_MISSING\n'; exit 24; }
[ -f "$B4_REPO" ] || { printf 'HOLD=B4_SOURCE_MISSING\n'; exit 25; }
[ -f "$C2_REPO" ] || { printf 'HOLD=C2_SOURCE_MISSING\n'; exit 26; }
[ -f "$C3_REPO" ] || { printf 'HOLD=C3R4_SOURCE_MISSING\n'; exit 27; }
[ -f "$R3_REPO" ] || { printf 'HOLD=R3_SOURCE_MISSING\n'; exit 28; }

A3_BLOB=$(blob1 "$A3_REPO")
B4_BLOB=$(blob1 "$B4_REPO")
C2_BLOB=$(blob1 "$C2_REPO")
C3_BLOB=$(blob1 "$C3_REPO")
R3_BLOB=$(blob1 "$R3_REPO")
A3_SHA=$(hash1 "$A3_REPO")
B4_SHA=$(hash1 "$B4_REPO")
C2_SHA=$(hash1 "$C2_REPO")
C3_SHA=$(hash1 "$C3_REPO")
R3_SHA=$(hash1 "$R3_REPO")
printf 'A3_GIT_BLOB=%s\nB4_GIT_BLOB=%s\nC2_GIT_BLOB=%s\nC3R4_GIT_BLOB=%s\nR3_GIT_BLOB=%s\n' "$A3_BLOB" "$B4_BLOB" "$C2_BLOB" "$C3_BLOB" "$R3_BLOB"
printf 'A3_SOURCE_SHA256=%s\nB4_SOURCE_SHA256=%s\nC2_SOURCE_SHA256=%s\nC3R4_SOURCE_SHA256=%s\nR3_SOURCE_SHA256=%s\n' "$A3_SHA" "$B4_SHA" "$C2_SHA" "$C3_SHA" "$R3_SHA"
[ "$A3_BLOB" = "$EXPECTED_A3_BLOB" ] || { printf 'HOLD=A3_SOURCE_BLOB_MISMATCH\n'; exit 29; }
[ "$B4_BLOB" = "$EXPECTED_B4_BLOB" ] || { printf 'HOLD=B4_SOURCE_BLOB_MISMATCH\n'; exit 30; }
[ "$C2_BLOB" = "$EXPECTED_C2_BLOB" ] || { printf 'HOLD=C2_SOURCE_BLOB_MISMATCH\n'; exit 31; }
[ "$C3_BLOB" = "$EXPECTED_C3_BLOB" ] || { printf 'HOLD=C3R4_SOURCE_BLOB_MISMATCH\n'; exit 32; }
[ "$R3_BLOB" = "$EXPECTED_R3_BLOB" ] || { printf 'HOLD=R3_SOURCE_BLOB_MISMATCH\n'; exit 33; }
[ "$A3_SHA" = "$EXPECTED_A3_SHA256" ] || { printf 'HOLD=A3_SOURCE_SHA256_MISMATCH\n'; exit 34; }
[ "$B4_SHA" = "$EXPECTED_B4_SHA256" ] || { printf 'HOLD=B4_SOURCE_SHA256_MISMATCH\n'; exit 35; }
[ "$C2_SHA" = "$EXPECTED_C2_SHA256" ] || { printf 'HOLD=C2_SOURCE_SHA256_MISMATCH\n'; exit 36; }

FORCED_C3_COUNT=0
for TOKEN in 'SEMANTIC_UNDERSTANDING' 'UNDERSTANDING_PROXY' 'NOT_PROVEN' 'NOT_UNDERSTOOD' 'UNDERSTOOD' 'CHUA_DUOC_CHUNG_MINH'; do
    C=$("$P/bin/grep" -F -c -- "$TOKEN" "$C3_REPO" 2>/dev/null || true)
    FORCED_C3_COUNT=$((FORCED_C3_COUNT + C))
done
printf 'C3R4_FORCED_SEMANTIC_VERDICT_LITERAL_COUNT=%s\n' "$FORCED_C3_COUNT"
[ "$FORCED_C3_COUNT" -eq 0 ] || { printf 'HOLD=C3R4_FORCED_SEMANTIC_VERDICT_LITERAL_PRESENT\n'; exit 37; }

FORCED_R3_COUNT=0
for TOKEN in 'SEMANTIC_UNDERSTANDING' 'NOT_PROVEN' 'NOT_UNDERSTOOD' 'UNDERSTOOD' 'CHUA_DUOC_CHUNG_MINH'; do
    C=$("$P/bin/grep" -F -c -- "$TOKEN" "$R3_REPO" 2>/dev/null || true)
    FORCED_R3_COUNT=$((FORCED_R3_COUNT + C))
done
printf 'R3_FORCED_SEMANTIC_VERDICT_LITERAL_COUNT=%s\n' "$FORCED_R3_COUNT"
[ "$FORCED_R3_COUNT" -eq 0 ] || { printf 'HOLD=R3_FORCED_SEMANTIC_VERDICT_LITERAL_PRESENT\n'; exit 38; }

V24_PID=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AT_SHADOW_START=%s\n' "$V24_PID"
[ -n "$V24_PID" ] || { printf 'HOLD=PRODUCTION_V24_NOT_RUNNING\n'; exit 39; }

install_compile() {
    LABEL="$1"; REPO_SRC="$2"; SRC="$3"; BC="$4"; EXPECTED_BLOB="$5"; EXPECTED_SHA="$6"
    cp -- "$REPO_SRC" "$SRC" || return 1
    INSTALLED_BLOB=$(blob1 "$SRC")
    INSTALLED_SHA=$(hash1 "$SRC")
    printf '%s_INSTALLED_GIT_BLOB=%s\n%s_INSTALLED_SOURCE_SHA256=%s\n' "$LABEL" "$INSTALLED_BLOB" "$LABEL" "$INSTALLED_SHA"
    [ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || return 2
    if [ "$EXPECTED_SHA" != '-' ]; then
        [ "$INSTALLED_SHA" = "$EXPECTED_SHA" ] || return 3
    fi
    rm -f -- "$BC.partial"
    "$SIGMAC" "$SRC" "$BC.partial"
    RC=$?
    printf '%s_SIGMAC_RC=%s\n' "$LABEL" "$RC"
    [ "$RC" -eq 0 ] || return 4
    [ -s "$BC.partial" ] || return 5
    mv -f -- "$BC.partial" "$BC" || return 6
    chmod 0400 "$BC" || return 7
    printf '%s_BYTECODE_SHA256=%s\n' "$LABEL" "$(hash1 "$BC")"
}

install_compile A3 "$A3_REPO" "$A3_SRC" "$A3_BC" "$EXPECTED_A3_BLOB" "$EXPECTED_A3_SHA256" || { printf 'HOLD=A3_COMPILE_OR_INSTALL_FAILED\n'; exit 40; }
install_compile B4 "$B4_REPO" "$B4_SRC" "$B4_BC" "$EXPECTED_B4_BLOB" "$EXPECTED_B4_SHA256" || { printf 'HOLD=B4_COMPILE_OR_INSTALL_FAILED\n'; exit 41; }
install_compile C2 "$C2_REPO" "$C2_SRC" "$C2_BC" "$EXPECTED_C2_BLOB" "$EXPECTED_C2_SHA256" || { printf 'HOLD=C2_COMPILE_OR_INSTALL_FAILED\n'; exit 42; }
install_compile C3R4 "$C3_REPO" "$C3_SRC" "$C3_BC" "$EXPECTED_C3_BLOB" - || { printf 'HOLD=C3R4_COMPILE_OR_INSTALL_FAILED\n'; exit 43; }
install_compile R3 "$R3_REPO" "$R3_SRC" "$R3_BC" "$EXPECTED_R3_BLOB" - || { printf 'HOLD=R3_COMPILE_OR_INSTALL_FAILED\n'; exit 44; }

for F in \
 SIGMA_V4A3_RECOVERED_EVENT.memory SIGMA_V4A3_RECEIVED_WORK.memory SIGMA_V4A3_RETRYABLE_WORK.memory SIGMA_V4A3_CORPUS_READ_REQUEST.memory SIGMA_V4A3_LAST_SOURCE.memory SIGMA_V4A3_ACTION.memory SIGMA_V4A3_TARGET.memory \
 SIGMA_V4B4R2_CONTEXT_ID.memory SIGMA_V4B4R2_CONTEXT_TEXT.memory SIGMA_V4B4R2_TOKEN_CURSOR.memory SIGMA_V4B4R2_COMPLETION.memory SIGMA_V4B4R2_STATUS.memory SIGMA_V4B4R2_LAST_EVIDENCE.memory SIGMA_V4B4R2_BEST_WIDTH.memory SIGMA_V4B4R2_BEST_SUPPORT.memory SIGMA_V4B4R2_PAIR_OCCURRENCES.memory SIGMA_V4B4R2_TRIPLE_OCCURRENCES.memory SIGMA_V4B4R2_QUAD_OCCURRENCES.memory \
 SIGMA_V4C2R2_RAW_DIR.memory SIGMA_V4C2R2_STATE_DIR.memory SIGMA_V4C2R2_PHASE.memory SIGMA_V4C2R2_SCAN_CURSOR.memory SIGMA_V4C2R2_ACTIVE_DOC.memory SIGMA_V4C2R2_ACTIVE_PURPOSE.memory SIGMA_V4C2R2_ACTIVE_BEST_WIDTH.memory SIGMA_V4C2R2_ACTIVE_BEST_SUPPORT.memory SIGMA_V4C2R2_PRIORITY_BEST_DOC.memory SIGMA_V4C2R2_PRIORITY_BEST_WIDTH.memory SIGMA_V4C2R2_PRIORITY_BEST_SUPPORT.memory SIGMA_V4C2R2_PRIORITY_UNPROFILED.memory SIGMA_V4C2R2_READ_REQUEST_ID.memory SIGMA_V4C2R2_READ_DOC.memory SIGMA_V4C2R2_READ_LINE.memory SIGMA_V4C2R2_READ_PURPOSE.memory SIGMA_V4C2R2_READ_RESULT_ID.memory SIGMA_V4C2R2_READ_RESULT_FOUND.memory SIGMA_V4C2R2_READ_RESULT_TEXT.memory SIGMA_V4C2R2_STATUS.memory \
 SIGMA_V4C3R1_INITIALIZED.memory SIGMA_V4C3R1_LAST_SEEN_PROGRESS_KEY.memory SIGMA_V4C3R1_PROGRESS.memory SIGMA_V4C3R1_CYCLE.memory SIGMA_V4C3R1_PROGRESS_BUDGET.memory SIGMA_V4C3R1_PAUSE_SECONDS.memory SIGMA_V4C3R1_LAST_REPORT.memory SIGMA_V4C3R1_PLAN.memory SIGMA_V4C3R1_STATUS.memory
do
    [ -e "$E/$F" ] || : > "$E/$F"
done

printf '%s' "$RAW" > "$E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$CORPUS_STATE" > "$E/SIGMA_V4C2R2_STATE_DIR.memory"
if [ ! -s "$C3_BUDGET" ]; then make_unary "$REFLECTION_PROGRESS_BUDGET" > "$C3_BUDGET"; fi
if [ ! -s "$C3_PAUSE" ]; then make_unary "$OBSERVE_PAUSE_SECONDS" > "$C3_PAUSE"; fi
BUDGET_LEN=$(wc -c < "$C3_BUDGET" | tr -d ' ')
PAUSE_LEN=$(wc -c < "$C3_PAUSE" | tr -d ' ')
[ "$BUDGET_LEN" -eq "$REFLECTION_PROGRESS_BUDGET" ] || { printf 'HOLD=C3_PROGRESS_BUDGET_STATE_MISMATCH ACTUAL=%s EXPECTED=%s\n' "$BUDGET_LEN" "$REFLECTION_PROGRESS_BUDGET"; exit 45; }
[ "$PAUSE_LEN" -eq "$OBSERVE_PAUSE_SECONDS" ] || { printf 'HOLD=C3_PAUSE_STATE_MISMATCH ACTUAL=%s EXPECTED=%s\n' "$PAUSE_LEN" "$OBSERVE_PAUSE_SECONDS"; exit 46; }

run_vm() {
    LABEL="$1"; BC="$2"; RUNLOG="$3"
    ( cd "$BRAIN" || exit 70; "$VM" "$BC" ) > "$RUNLOG" 2>&1
    RC=$?
    [ "$RC" -eq 0 ] || { printf 'HOLD=%s_VM_FAILURE RC=%s LOG=%s\n' "$LABEL" "$RC" "$RUNLOG"; return "$RC"; }
}

transport_exact_native_line_request() {
    TURN="$1"; EXPECTED_TARGET="$2"
    REQ_ID=$(cat "$READ_REQ_ID")
    DOC_ID=$(cat "$READ_DOC")
    LINE_U=$(cat "$READ_LINE")
    PURPOSE=$(cat "$READ_PURPOSE")
    printf 'CORPUS_TRANSPORT TURN=%s REQUEST_ID=%s DOC=%s LINE_UNARY_LEN=%s PURPOSE=%s\n' "$TURN" "$REQ_ID" "$DOC_ID" "${#LINE_U}" "$PURPOSE"
    [ -n "$REQ_ID" ] || return 80
    [ "$EXPECTED_TARGET" = "$REQ_ID" ] || return 81
    [ -n "$DOC_ID" ] || return 82
    case "$DOC_ID" in *'/'*|*'..'*) return 83 ;; esac
    case "$PURPOSE" in PROFILE|LEARN) ;; *) return 84 ;; esac
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
        printf '%s' YES > "$READ_RESULT_FOUND" || return 88
    else
        : > "$TMP_RESULT"
        printf '%s' NO > "$READ_RESULT_FOUND" || return 89
    fi
    mv -f -- "$TMP_RESULT" "$READ_RESULT_TEXT" || return 90
    printf '%s' "$REQ_ID" > "$READ_RESULT_ID" || return 91
}

run_c3r4_with_r3_observer() {
    TURN="$1"; C3LOG="$2"
    OLD_HASH=EMPTY
    [ ! -s "$C3_REPORT" ] || OLD_HASH=$(hash1 "$C3_REPORT")
    REPORTER_DISPATCHED=0
    REPORTER_OK=0

    ( cd "$BRAIN" || exit 71; "$VM" "$C3_BC" ) > "$C3LOG" 2>&1 &
    C3_PID=$!

    while "$P/bin/kill" -0 "$C3_PID" >/dev/null 2>&1; do
        if [ "$REPORTER_DISPATCHED" -eq 0 ] && [ -s "$C3_REPORT" ]; then
            NEW_HASH=$(hash1 "$C3_REPORT")
            STATUS_NOW=$(cat "$C3_STATUS")
            if [ "$NEW_HASH" != "$OLD_HASH" ] && [ "$STATUS_NOW" = 'REPORT_AND_PLAN_COMMITTED_BEFORE_PAUSE' ]; then
                REPORTER_DISPATCHED=1
                R3LOG="$LOG/$("$P/bin/date" -u +%Y%m%dT%H%M%SZ).$TURN.r3_reporter.log"
                printf '\nSIGMA_V4C3R4_NATIVE_REPORT_EVENT_BEGIN TURN=%s\n' "$TURN"
                "$P/bin/cat" "$C3_REPORT"
                printf '\nSIGMA_V4C3R4_NATIVE_REPORT_EVENT_END\n'
                printf 'HOST_EXACT_NATIVE_EVENT_DISPATCH=REPORT_AND_PLAN_COMMITTED_BEFORE_PAUSE\n'
                printf 'HOST_REPORT_SUMMARIZATION=NO\nHOST_REPORT_TRANSLATION=NO\nHOST_SELF_ASSESSMENT=NO\n'
                ( cd "$BRAIN" || exit 72; "$VM" "$R3_BC" ) > "$R3LOG" 2>&1
                R3_RC=$?
                printf 'R3_REPORTER_VM_RC=%s LOG=%s\n' "$R3_RC" "$R3LOG"
                "$P/bin/cat" "$R3LOG"
                [ "$R3_RC" -eq 0 ] || { printf 'HOLD=R3_REPORTER_VM_FAILURE_DURING_NATIVE_PAUSE TURN=%s RC=%s LOG=%s\n' "$TURN" "$R3_RC" "$R3LOG"; return 3; }
                "$P/bin/grep" -F -x 'REPORTER_STATUS EVIDENCE_FIRST_SELF_VIEW_REPORT_EMITTED' "$R3LOG" >/dev/null 2>&1 || { printf 'HOLD=R3_REPORTER_STATUS_NOT_EMITTED TURN=%s LOG=%s\n' "$TURN" "$R3LOG"; return 4; }
                REPORTER_OK=1
                printf 'R3_REPORTER_EXACT_OUTPUT_DISPLAYED_DURING_NATIVE_PAUSE=YES\n'
            fi
        fi
        "$P/bin/sleep" 1
    done

    wait "$C3_PID"
    C3_RC=$?
    "$P/bin/cat" "$C3LOG"
    [ "$C3_RC" -eq 0 ] || { printf 'HOLD=C3R4_VM_FAILURE TURN=%s RC=%s LOG=%s\n' "$TURN" "$C3_RC" "$C3LOG"; return 1; }
    if "$P/bin/grep" -F 'V4C3R4_STATUS REFUSE_' "$C3LOG" >/dev/null 2>&1; then
        printf 'HOLD=C3R4_NATIVE_REFLECTION_REFUSAL TURN=%s LOG=%s\n' "$TURN" "$C3LOG"
        return 2
    fi

    if [ "$REPORTER_DISPATCHED" -eq 1 ]; then
        [ "$REPORTER_OK" -eq 1 ] || { printf 'HOLD=R3_REPORTER_DISPATCH_INCOMPLETE TURN=%s\n' "$TURN"; return 5; }
        FINAL_STATUS=$(cat "$C3_STATUS")
        [ "$FINAL_STATUS" = 'OBSERVE_PAUSE_COMPLETE_RESUME_LEARN' ] || { printf 'HOLD=C3R4_DID_NOT_RESUME_AFTER_NATIVE_PAUSE TURN=%s STATUS=%s\n' "$TURN" "$FINAL_STATUS"; return 6; }
        printf 'SIGMA_V4C3R4_R3_REFLECTION_CYCLE_COMPLETE TURN=%s STATUS=%s PLAN=%s\n' "$TURN" "$FINAL_STATUS" "$(cat "$C3_PLAN")"
        printf 'REAL_C2R2_CONTINUOUS_C3R4_R3_REFLECTION=PASS_IN_THIS_OBSERVED_CYCLE_SCOPE\n'
        printf 'NATIVE_C3R4_REPORT_COMMIT_BEFORE_R3_DISPATCH=PASS_IN_THIS_OBSERVED_CYCLE_SCOPE\n'
        printf 'R3_REPORT_VISIBLE_DURING_NATIVE_180_SECOND_PAUSE=PASS_IN_THIS_OBSERVED_CYCLE_SCOPE\n'
        printf 'NATIVE_C3R4_RESUME_AFTER_R3_OBSERVATION=PASS_IN_THIS_OBSERVED_CYCLE_SCOPE\n'
    fi
}

START_PROFILE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.profile' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
START_COMPLETE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.complete' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
START_HOLD_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.hold' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
START_EVIDENCE_COUNT=$("$P/bin/find" "$CORPUS_STATE" -maxdepth 1 -type f -name '*.evidence' | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
C3_CYCLE_TEXT=$(cat "$C3_CYCLE")
C3_PROGRESS_TEXT=$(cat "$C3_PROGRESS")
printf 'RESUME_PROFILE_COUNT=%s\nRESUME_COMPLETE_COUNT=%s\nRESUME_HOLD_COUNT=%s\nRESUME_EVIDENCE_COUNT=%s\n' "$START_PROFILE_COUNT" "$START_COMPLETE_COUNT" "$START_HOLD_COUNT" "$START_EVIDENCE_COUNT"
printf 'RESUME_C3_CYCLE_UNARY_LEN=%s\nRESUME_C3_PROGRESS_UNARY_LEN=%s\n' "${#C3_CYCLE_TEXT}" "${#C3_PROGRESS_TEXT}"
[ "$START_HOLD_COUNT" -eq 0 ] || { printf 'HOLD=PREEXISTING_NATIVE_DOCUMENT_HOLD COUNT=%s\n' "$START_HOLD_COUNT"; exit 47; }

if [ ! -s "$E/SIGMA_V4C3R1_INITIALIZED.memory" ]; then
    START_C3_LOG="$LOG/startup.c3r4.log"
    run_vm C3R4_BASELINE "$C3_BC" "$START_C3_LOG" || exit 48
    "$P/bin/cat" "$START_C3_LOG"
fi

TURN=0
while :; do
    TS=$("$P/bin/date" -u +%Y%m%dT%H%M%SZ)
    MLOG="$LOG/$TS.$TURN.manager.log"
    ALOG="$LOG/$TS.$TURN.arbiter.log"
    BLOG="$LOG/$TS.$TURN.learner.log"
    C3LOG="$LOG/$TS.$TURN.c3r4.log"

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
    printf 'V4C3R4_R3_C2R2_TURN=%s ACTION=%s TARGET=%s\n' "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET"

    case "$NATIVE_ACTION" in
        DISPATCH_NATIVE_CORPUS_READ_REQUEST)
            transport_exact_native_line_request "$TURN" "$NATIVE_TARGET" || { RC=$?; printf 'HOLD=CORPUS_TRANSPORT_FAILURE TURN=%s RC=%s TARGET=%s\n' "$TURN" "$RC" "$NATIVE_TARGET"; exit 54; }
            ;;
        LEARN_RECEIVED_CONTEXT|RESUME_RETRYABLE_CONTEXT)
            ACTIVE_CONTEXT=$(cat "$B4_CONTEXT")
            [ "$NATIVE_TARGET" = "$ACTIVE_CONTEXT" ] || { printf 'HOLD=NATIVE_TARGET_CONTEXT_MISMATCH TURN=%s ACTION=%s TARGET=%s ACTIVE=%s\n' "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET" "$ACTIVE_CONTEXT"; exit 55; }
            run_vm LEARNER "$B4_BC" "$BLOG" || exit 56
            ;;
        WAIT_NO_ELIGIBLE_WORK)
            "$P/bin/sleep" "$IDLE_SLEEP_SECONDS"
            ;;
        *)
            printf 'HOLD=UNSUPPORTED_NATIVE_ACTION TURN=%s ACTION=%s TARGET=%s\n' "$TURN" "$NATIVE_ACTION" "$NATIVE_TARGET"
            exit 57
            ;;
    esac

    run_c3r4_with_r3_observer "$TURN" "$C3LOG" || exit 58

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
        C3_CYCLE_TEXT=$(cat "$C3_CYCLE")
        C3_PROGRESS_TEXT=$(cat "$C3_PROGRESS")
        printf 'V4C3R4_R3_C2R2_HEALTH TURN=%s PHASE=%s PROFILE_DOCS=%s COMPLETE_DOCS=%s HOLD_DOCS=%s EVIDENCE_DOCS=%s ACTIVE_DOC=%s MANAGER_STATUS=%s C3_CYCLE_UNARY_LEN=%s C3_PROGRESS_UNARY_LEN=%s C3_STATUS=%s C3_PLAN=%s V24_PID=%s\n' "$TURN" "$PHASE" "$PROFILE_COUNT" "$COMPLETE_COUNT" "$HOLD_COUNT" "$EVIDENCE_COUNT" "$ACTIVE_DOC" "$STATUS" "${#C3_CYCLE_TEXT}" "${#C3_PROGRESS_TEXT}" "$(cat "$C3_STATUS")" "$(cat "$C3_PLAN")" "$V24_NOW"
        [ "$V24_NOW" = "$V24_PID" ] || { printf 'HOLD=PRODUCTION_V24_PID_CHANGED_OR_STOPPED EXPECTED=%s ACTUAL=%s\n' "$V24_PID" "$V24_NOW"; exit 59; }
        [ "$HOLD_COUNT" -eq 0 ] || { printf 'HOLD=REAL_CORPUS_DOCUMENT_HOLD_OBSERVED COUNT=%s\n' "$HOLD_COUNT"; exit 60; }
    fi
done
