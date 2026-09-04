#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
WORK="$HOME_SIGMA/sigma-freedom-write"
BRAIN="$WORK/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC="$E/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma"
BC="$E/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigmab"
EXPECTED_SOURCE=6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2

DECODER="$HOME_SIGMA/SIGMA_WIKIMEDIA_TRANSPORT_DECODE_V1.py"
EXPECTED_DECODER=c8d10c640d32d23d3998590a291d187de0936368d0cd3559706ed6509fd31705

STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
RAW="$STATE/raw"
DONE="$STATE/done"
HOLD="$STATE/hold"
LOG="$STATE/log"
LOCK="$STATE/runner.lock"

FETCH_REQUEST="$E/SIGMA_CL22_FETCH_REQUEST.memory"
FETCHED_REQUESTS="$E/SIGMA_CL22_FETCHED_REQUESTS.memory"
CURRENT_CONTEXT="$E/SIGMA_CL22_CURRENT_CONTEXT.memory"
CURRENT_INPUT="$E/SIGMA_CL22_CURRENT_EXPERIENCE.memory"
CURRENT_GAP="$E/SIGMA_CL22_CURRENT_GAP.memory"
LAST_CONTEXT="$E/SIGMA_CL22_LAST_CONTEXT.memory"

IDLE_SLEEP_SECONDS=${IDLE_SLEEP_SECONDS:-20}
RECONSIDER_INTERVAL_SECONDS=${RECONSIDER_INTERVAL_SECONDS:-120}
MIN_FETCH_INTERVAL_SECONDS=${MIN_FETCH_INTERVAL_SECONDS:-300}
RATE_LIMIT_BACKOFF_SECONDS=${RATE_LIMIT_BACKOFF_SECONDS:-900}
FETCH_FAILURE_BACKOFF_SECONDS=${FETCH_FAILURE_BACKOFF_SECONDS:-300}

SEARCH_ENDPOINT=${SEARCH_ENDPOINT:-https://en.wikipedia.org/w/api.php}

mkdir -p "$STATE" "$RAW" "$DONE" "$HOLD" "$LOG"

for F in \
    "$FETCH_REQUEST" \
    "$FETCHED_REQUESTS" \
    "$CURRENT_CONTEXT" \
    "$CURRENT_INPUT" \
    "$CURRENT_GAP" \
    "$LAST_CONTEXT"
do
    [ -e "$F" ] || : > "$F"
done

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V2_4_OR_PRIOR_CONTINUOUS_RUNNER_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_decoder=$("$P/bin/sha256sum" "$DECODER" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"
printf 'TRANSPORT_DECODER_SHA256=%s\n' "$actual_decoder"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || {
    printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'
    exit 21
}
[ "$actual_vm" = "$EXPECTED_VM" ] || {
    printf 'HOLD=VM_IDENTITY_MISMATCH\n'
    exit 22
}
[ "$actual_source" = "$EXPECTED_SOURCE" ] || {
    printf 'HOLD=V2_4_SOURCE_IDENTITY_MISMATCH\n'
    exit 23
}
[ "$actual_decoder" = "$EXPECTED_DECODER" ] || {
    printf 'HOLD=TRANSPORT_DECODER_IDENTITY_MISMATCH\n'
    exit 24
}

PYTHON=$(command -v python 2>/dev/null || true)
[ -n "$PYTHON" ] && [ -x "$PYTHON" ] || {
    printf 'HOLD=PYTHON_REQUIRED_FOR_MECHANICAL_PROTOCOL_DECODE\n'
    exit 25
}

if [ ! -s "$BC" ] || [ "$SRC" -nt "$BC" ]; then
    "$P/bin/rm" -f -- "$BC.partial"
    "$SIGMAC" "$SRC" "$BC.partial" || exit 31
    [ -s "$BC.partial" ] || exit 32
    "$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 33
    "$P/bin/chmod" 0400 "$BC" || exit 34
    printf 'BYTECODE_COMPILED=YES\n'
fi

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

context_is_held_for_current_bytecode() {
    SHA=$1
    MARK="$HOLD/$SHA.hold"
    [ -f "$MARK" ] || return 1
    "$P/bin/grep" -F -x "BYTECODE_SHA256=$BYTECODE_SHA" "$MARK" >/dev/null 2>&1
}

hold_failed_context() {
    SHA=$1
    MODE=$2
    RC=$3
    RUNLOG=$4

    TMP="$HOLD/$SHA.hold.partial.$$"
    {
        printf 'CONTEXT_SHA256=%s\n' "$SHA"
        printf 'MODE=%s\n' "$MODE"
        printf 'VM_RC=%s\n' "$RC"
        printf 'VM_SHA256=%s\n' "$actual_vm"
        printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"
        printf 'RUN_LOG=%s\n' "$RUNLOG"
        printf 'HOST_LEARNING=NO\n'
        printf 'REASON=VM_EXECUTION_FAILED_QUARANTINE_UNTIL_BYTECODE_CHANGES\n'
    } > "$TMP" || return 1

    "$P/bin/mv" -f -- "$TMP" "$HOLD/$SHA.hold" || return 1
    "$P/bin/chmod" 0400 "$HOLD/$SHA.hold" || return 1
}

replace_current_input() {
    DOC=$1
    PART="$CURRENT_INPUT.partial.$$"
    "$P/bin/rm" -f -- "$PART" || return 1
    "$P/bin/cp" -- "$DOC" "$PART" || return 1
    "$P/bin/chmod" 0400 "$PART" || return 1
    "$P/bin/mv" -f -- "$PART" "$CURRENT_INPUT" || return 1
}

run_sigma_on_document() {
    DOC=$1
    MODE=$2

    SHA=${DOC##*/}
    SHA=${SHA%.document}

    if context_is_held_for_current_bytecode "$SHA"; then
        printf 'SIGMA_CONTEXT_HELD context=%s bytecode=%s\n' "$SHA" "$BYTECODE_SHA"
        return 2
    fi

    "$P/bin/printf" '%s' "$SHA" > "$CURRENT_CONTEXT" || return 40
    replace_current_input "$DOC" || return 41

    RUNLOG="$LOG/$SHA.V24.$("$P/bin/date" -u +%Y%m%dT%H%M%SZ).$MODE.log"

    (
        cd "$BRAIN" || exit 42
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1

    RC=$?

    if [ "$RC" -ne 0 ]; then
        printf 'SIGMA_LEARN_FAILED context=%s mode=%s rc=%s log=%s\n' \
            "$SHA" "$MODE" "$RC" "$RUNLOG"
        hold_failed_context "$SHA" "$MODE" "$RC" "$RUNLOG" || true
        return 43
    fi

    "$P/bin/rm" -f -- "$HOLD/$SHA.hold" 2>/dev/null || true

    printf 'SIGMA_NATIVE_V24_CYCLE context=%s mode=%s\n' "$SHA" "$MODE"
    "$P/bin/tail" -n 14 "$RUNLOG"

    if [ "$MODE" = "NEW" ]; then
        MARK="$DONE/$SHA.done"

        if [ ! -e "$MARK" ]; then
            TMPMARK="$DONE/$SHA.done.partial.$$"
            {
                printf 'CONTEXT_SHA256=%s\n' "$SHA"
                printf 'DOCUMENT_SHA256=%s\n' "$("$P/bin/sha256sum" "$DOC" | "$P/bin/awk" '{print $1}')"
                printf 'VM_SHA256=%s\n' "$actual_vm"
                printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"
                printf 'RUN_LOG=%s\n' "$RUNLOG"
            } > "$TMPMARK" || return 44

            "$P/bin/mv" -f -- "$TMPMARK" "$MARK" || return 45
            "$P/bin/chmod" 0400 "$MARK" || return 46
        fi
    fi

    return 0
}

learn_new_backlog() {
    FOUND=0

    for DOC in "$RAW"/*.document; do
        [ -f "$DOC" ] || continue

        SHA=${DOC##*/}
        SHA=${SHA%.document}

        [ ! -e "$DONE/$SHA.done" ] || continue

        if context_is_held_for_current_bytecode "$SHA"; then
            continue
        fi

        FOUND=1
        run_sigma_on_document "$DOC" NEW || {
            RC=$?
            [ "$RC" -eq 2 ] || return "$RC"
        }
    done

    [ "$FOUND" -eq 1 ] || return 1
}

reconsider_all_contexts_for_request() {
    [ ! -s "$FETCH_REQUEST" ] || return 0

    for MARK in "$DONE"/*.done; do
        [ -f "$MARK" ] || continue

        SHA=${MARK##*/}
        SHA=${SHA%.done}
        DOC="$RAW/$SHA.document"

        [ -f "$DOC" ] || continue

        if context_is_held_for_current_bytecode "$SHA"; then
            continue
        fi

        run_sigma_on_document "$DOC" RECONSIDER || {
            RC=$?
            [ "$RC" -eq 2 ] && continue
            return "$RC"
        }

        if [ -s "$FETCH_REQUEST" ]; then
            printf 'SIGMA_REQUEST_SOURCE_CONTEXT=%s\n' "$SHA"
            return 0
        fi
    done

    return 1
}

request_is_fetched() {
    REQUEST=$1
    "$P/bin/grep" -F -x -- "$REQUEST" "$FETCHED_REQUESTS" >/dev/null 2>&1
}

append_fetched_request() {
    REQUEST=$1
    request_is_fetched "$REQUEST" && return 0

    TMP="$FETCHED_REQUESTS.partial.$$"
    "$P/bin/cat" "$FETCHED_REQUESTS" > "$TMP" || return 50
    "$P/bin/printf" '%s\n' "$REQUEST" >> "$TMP" || return 51
    "$P/bin/mv" -f -- "$TMP" "$FETCHED_REQUESTS" || return 52
}

fetch_sigma_request() {
    [ -s "$FETCH_REQUEST" ] || return 1

    REQUEST=$("$P/bin/cat" "$FETCH_REQUEST")
    [ -n "$REQUEST" ] || return 1

    if request_is_fetched "$REQUEST"; then
        "$P/bin/printf" '' > "$FETCH_REQUEST"
        return 2
    fi

    TMPJSON=$("$P/bin/mktemp" "$STATE/.v24-json.XXXXXX") || return 4
    TMPTEXT=$("$P/bin/mktemp" "$STATE/.v24-text.XXXXXX") || {
        "$P/bin/rm" -f -- "$TMPJSON"
        return 4
    }

    printf 'SIGMA_FETCH_REQUEST=%s\n' "$REQUEST"
    printf 'HOST_ROLE=QUERY_TRANSPORT_AND_PROTOCOL_DECODE_ONLY\n'
    printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'

    HTTP_CODE=$(
        curl -LsS \
            --connect-timeout 10 \
            --max-time 90 \
            --get \
            --data-urlencode 'action=query' \
            --data-urlencode 'generator=search' \
            --data-urlencode 'prop=extracts' \
            --data-urlencode 'explaintext=1' \
            --data-urlencode 'exintro=1' \
            --data-urlencode 'gsrlimit=3' \
            --data-urlencode 'format=json' \
            --data-urlencode 'formatversion=2' \
            --data-urlencode "gsrsearch=$REQUEST" \
            --output "$TMPJSON" \
            --write-out '%{http_code}' \
            "$SEARCH_ENDPOINT"
    )
    CURL_RC=$?

    printf 'FETCH_HTTP_CODE=%s\n' "$HTTP_CODE"

    if [ "$CURL_RC" -ne 0 ]; then
        "$P/bin/rm" -f -- "$TMPJSON" "$TMPTEXT"
        return 8
    fi

    if [ "$HTTP_CODE" = "429" ]; then
        "$P/bin/rm" -f -- "$TMPJSON" "$TMPTEXT"
        return 29
    fi

    [ "$HTTP_CODE" = "200" ] || {
        "$P/bin/rm" -f -- "$TMPJSON" "$TMPTEXT"
        return 28
    }

    "$PYTHON" "$DECODER" "$TMPJSON" "$TMPTEXT"
    DRC=$?

    if [ "$DRC" -eq 0 ] && [ -s "$TMPTEXT" ]; then
        SHA=$("$P/bin/sha256sum" "$TMPTEXT" | "$P/bin/awk" '{print $1}')
        DEST="$RAW/$SHA.document"

        if [ ! -e "$DEST" ]; then
            "$P/bin/mv" -- "$TMPTEXT" "$DEST" || return 5
            "$P/bin/chmod" 0400 "$DEST" || return 6
            printf 'FETCHED_DECODED_CONTEXT=%s\n' "$SHA"
        else
            "$P/bin/rm" -f -- "$TMPTEXT"
            printf 'FETCH_RESULT_ALREADY_PRESENT=%s\n' "$SHA"
        fi

        append_fetched_request "$REQUEST" || return 7
        "$P/bin/printf" '' > "$FETCH_REQUEST"
        "$P/bin/rm" -f -- "$TMPJSON"
        return 0
    fi

    "$P/bin/rm" -f -- "$TMPJSON" "$TMPTEXT"
    return 9
}

printf 'SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4=START\n'
printf 'HOST_LEARNING=NO\n'
printf 'SELF_DIRECTION_POLICY=NATIVE_RECURRENT_SUPPORT_FRONTIER\n'
printf 'ELIGIBILITY=CONTEXT_SUPPORT_GT_1\n'
printf 'ENDPOINT_LOAD_REMOVED=YES\n'
printf 'VM_FAILURE_HOLD=BYTECODE_SCOPED\n'
printf 'STATE_NAMESPACE=SIGMA_CL22_CONTINUED\n'
printf 'MIN_FETCH_INTERVAL_SECONDS=%s\n' "$MIN_FETCH_INTERVAL_SECONDS"
printf 'RATE_LIMIT_BACKOFF_SECONDS=%s\n' "$RATE_LIMIT_BACKOFF_SECONDS"

last_fetch_at=0
next_fetch_not_before=0
last_reconsider=0

while :; do
    DID_WORK=0

    if learn_new_backlog; then
        DID_WORK=1
    fi

    now=$("$P/bin/date" +%s)

    if [ ! -s "$FETCH_REQUEST" ] && \
       [ $((now - last_reconsider)) -ge "$RECONSIDER_INTERVAL_SECONDS" ]
    then
        if reconsider_all_contexts_for_request; then
            DID_WORK=1
        fi
        last_reconsider=$now
    fi

    now=$("$P/bin/date" +%s)

    if [ -s "$FETCH_REQUEST" ] && \
       [ "$now" -ge "$next_fetch_not_before" ] && \
       [ $((now - last_fetch_at)) -ge "$MIN_FETCH_INTERVAL_SECONDS" ]
    then
        fetch_sigma_request
        FRC=$?

        if [ "$FRC" -eq 0 ]; then
            DID_WORK=1
            last_fetch_at=$now
            next_fetch_not_before=$((now + MIN_FETCH_INTERVAL_SECONDS))
        elif [ "$FRC" -eq 29 ]; then
            printf 'FETCH_BACKOFF=HTTP_429 seconds=%s\n' "$RATE_LIMIT_BACKOFF_SECONDS"
            next_fetch_not_before=$((now + RATE_LIMIT_BACKOFF_SECONDS))
        elif [ "$FRC" -eq 8 ] || [ "$FRC" -eq 28 ] || [ "$FRC" -eq 9 ]; then
            printf 'FETCH_BACKOFF=TRANSPORT_FAILURE seconds=%s\n' "$FETCH_FAILURE_BACKOFF_SECONDS"
            next_fetch_not_before=$((now + FETCH_FAILURE_BACKOFF_SECONDS))
        fi
    fi

    if [ "$DID_WORK" -eq 0 ]; then
        RAW_COUNT=$("$P/bin/find" "$RAW" -maxdepth 1 -type f -name '*.document' 2>/dev/null | "$P/bin/wc" -l)
        DONE_COUNT=$("$P/bin/find" "$DONE" -maxdepth 1 -type f -name '*.done' 2>/dev/null | "$P/bin/wc" -l)
        HOLD_COUNT=$("$P/bin/find" "$HOLD" -maxdepth 1 -type f -name '*.hold' 2>/dev/null | "$P/bin/wc" -l)
        now=$("$P/bin/date" +%s)

        if [ -s "$FETCH_REQUEST" ]; then
            REQUEST=$("$P/bin/cat" "$FETCH_REQUEST")
            printf 'SIGMA_STATE=PENDING_NATIVE_REQUEST REQUEST=%s NEXT_FETCH_NOT_BEFORE=%s NOW=%s RAW=%s DONE=%s HOLD=%s\n' \
                "$REQUEST" "$next_fetch_not_before" "$now" "$RAW_COUNT" "$DONE_COUNT" "$HOLD_COUNT"
        else
            printf 'SIGMA_STATE=WAITING_FOR_RECURRENT_FRONTIER RAW=%s DONE=%s HOLD=%s\n' \
                "$RAW_COUNT" "$DONE_COUNT" "$HOLD_COUNT"
        fi

        "$P/bin/sleep" "$IDLE_SLEEP_SECONDS"
    fi
done
