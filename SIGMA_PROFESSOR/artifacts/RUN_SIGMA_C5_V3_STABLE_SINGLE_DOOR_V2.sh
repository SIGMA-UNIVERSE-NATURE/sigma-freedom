#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

ROOT="${SIGMA_ROOT:-$HOME/SIGMA/sigma_genesis1}"
STATE="${C5_STATE_ROOT:-$ROOT/.sigma_c5_real_shadow_v2}"
OPS="$ROOT/.sigma_ops"
RESOLVER="$OPS/SIGMA_RUNTIME_RESOLVER_V2.sh"

WATCHER="$OPS/SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.py"
WATCHER_EXPECTED_SHA="cea1bd96d2ebd80538d066467bdceac9ef3053fd09c80c8eac6181173fc3f286"
WATCHER_PIDFILE="$OPS/SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.pid"
WATCHER_STATUS="$OPS/SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.status"

SUPROOT="$ROOT/.sigma_supervisor/stable_single_door_v2"
SUPPID="$SUPROOT/supervisor.pid"
SUPLOCK="$SUPROOT/supervisor.lock"
STATUS="$SUPROOT/status.txt"
LOG="$ROOT/SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.log"

V3LOG="$ROOT/C5_V3_CONTINUOUS.log"
V3PIDFILE="$ROOT/C5_V3_CONTINUOUS.pid"

INET_NAME="RUN_SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.sh"
INET_EXPECTED_SHA="a24eb7445068161518b1875b2925b90848b9548e4904b19eb1c4e6b2edec2d0a"
INETLOG="$ROOT/C5_INTERNET_INGRESS_V2.log"

FIX4_BIN="$HOME/.sigma_c5_general_web_fix4/bin"
FIX4="$FIX4_BIN/curl"
FIX4_EXPECTED_SHA="d171c9c4ed0e0c50b18ba65a82b8380aeb7ae79ea761fb7f767042e75c4142a9"
PYCOMPAT="$HOME/.sigma_c5_oppo_python_compat_v2b"

EXEC="$STATE/runtime/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
ST="$EXEC/state"
IO="$EXEC/io"
LOCAL_ACTIVE="$ST/local_active_record.txt"
EXTERNAL_ACTIVE="$ST/external_active_record.txt"
CURRENT_STREAM="$IO/current_stream.txt"
DB="$STATE/state/state.sqlite3"

mkdir -p "$SUPROOT" "$OPS"

ts() { date -u '+%Y-%m-%dT%H:%M:%SZ'; }
hash1() { sha256sum "$1" 2>/dev/null | awk '{print $1}'; }
log() {
    printf '%s %s\n' "$(ts)" "$*" >> "$LOG"
}

cleanup() {
    rm -f "$SUPLOCK" "$SUPPID"
}
trap 'cleanup; exit 0' INT TERM
trap 'cleanup' EXIT

if ( set -o noclobber; printf '%s\n' "$$" > "$SUPLOCK" ) 2>/dev/null; then
    :
else
    OLD="$(cat "$SUPLOCK" 2>/dev/null || true)"
    if [ -n "$OLD" ] && kill -0 "$OLD" 2>/dev/null; then
        printf 'HOLD=STABLE_SINGLE_DOOR_ALREADY_RUNNING pid=%s\n' "$OLD"
        exit 80
    fi
    rm -f "$SUPLOCK"
    printf '%s\n' "$$" > "$SUPLOCK"
fi
printf '%s\n' "$$" > "$SUPPID"

[ -f "$RESOLVER" ] || {
    log "HOLD=RESOLVER_MISSING"
    exit 81
}
. "$RESOLVER" || {
    log "HOLD=RESOLVER_LOAD_FAILED"
    exit 82
}

sigma_verify_locked_identity >> "$LOG" 2>&1 || {
    log "HOLD=SIGMA_IDENTITY_MISMATCH"
    exit 83
}
sigma_assert_state_not_regressed >> "$LOG" 2>&1 || {
    log "HOLD=STATE_REGRESSION_AT_START"
    exit 84
}

[ -f "$WATCHER" ] || {
    log "HOLD=STREAM_COHERENCE_WATCHER_MISSING"
    exit 85
}
WH="$(hash1 "$WATCHER")"
[ "$WH" = "$WATCHER_EXPECTED_SHA" ] || {
    log "HOLD=STREAM_COHERENCE_WATCHER_SHA_MISMATCH actual=$WH"
    exit 86
}

if command -v termux-wake-lock >/dev/null 2>&1; then
    termux-wake-lock >/dev/null 2>&1 || true
fi

proc_pids() {
    NEEDLE="$1"
    for D in /proc/[0-9]*; do
        [ -r "$D/cmdline" ] || continue
        P="${D##*/}"
        [ "$P" = "$$" ] && continue
        CMD="$(tr '\000' ' ' < "$D/cmdline" 2>/dev/null || true)"
        case "$CMD" in
            *"$NEEDLE"*) printf '%s\n' "$P" ;;
        esac
    done
}

count_proc() {
    proc_pids "$1" | awk 'NF{n++} END{print n+0}'
}

stop_exact_name() {
    NAME="$1"
    while IFS= read -r P; do
        [ -n "$P" ] || continue
        kill -TERM "$P" 2>/dev/null || true
    done < <(proc_pids "$NAME")
    sleep 2
}

archive_empty_marker() {
    P="$1"
    LABEL="$2"
    [ -f "$P" ] || return 0
    if [ ! -s "$P" ] || ! grep -q '[^[:space:]]' "$P" 2>/dev/null; then
        STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
        R="$STATE/recovery/empty_runtime_marker/$STAMP"
        mkdir -p "$R"
        sha256sum "$P" > "$R/${LABEL}.sha256" 2>/dev/null || true
        mv "$P" "$R/${LABEL}.empty"
        log "EMPTY_RUNTIME_MARKER_ARCHIVED=$LABEL archive=$R"
    fi
}

archive_empty_marker "$LOCAL_ACTIVE" "local_active_record"
archive_empty_marker "$EXTERNAL_ACTIVE" "external_active_record"

ensure_watcher() {
    N="$(count_proc "SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.py")"
    if [ "$N" -eq 1 ]; then
        return 0
    fi
    if [ "$N" -gt 1 ]; then
        log "HOLD=MULTIPLE_STREAM_COHERENCE_WATCHERS count=$N"
        return 1
    fi
    nohup python "$WATCHER" >> "$LOG" 2>&1 &
    WP=$!
    printf '%s\n' "$WP" > "$WATCHER_PIDFILE"
    sleep 1
    N="$(count_proc "SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.py")"
    [ "$N" -eq 1 ] || {
        log "HOLD=STREAM_COHERENCE_WATCHER_START_FAILED count=$N"
        return 1
    }
    log "STREAM_COHERENCE_WATCHER_STARTED=YES pid=$WP"
    return 0
}

exact_c5_count() {
    count_proc "RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
}
exact_c5_pid() {
    proc_pids "RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh" | head -n1
}

find_inet_runner() {
    while IFS= read -r F; do
        [ -f "$F" ] || continue
        H="$(hash1 "$F")"
        if [ "$H" = "$INET_EXPECTED_SHA" ]; then
            printf '%s\n' "$F"
            return 0
        fi
    done < <(
        find "$ROOT/.sigma_c5" -maxdepth 8 -type f \
          -name "$INET_NAME" -print 2>/dev/null
    )
    return 1
}

inet_count() {
    count_proc "$INET_NAME"
}
inet_pid() {
    proc_pids "$INET_NAME" | head -n1
}

stop_internet() {
    N="$(inet_count)"
    [ "$N" -eq 0 ] && return 0
    stop_exact_name "$INET_NAME"
    N="$(inet_count)"
    if [ "$N" -ne 0 ]; then
        log "INTERNET_STOP_INCOMPLETE count=$N"
        return 1
    fi
    log "INTERNET_FEEDER_STOPPED=YES"
}

recover_proven_stale_eof() {
STATE="$STATE" python - <<'PY'
import os, re, sqlite3, sys
from datetime import datetime, timezone

state=os.environ["STATE"]
marker=os.path.join(
    state,"runtime",".sigma_exec",
    "SIGMA_C5_AUTONOMOUS_SELF_LEARNING",
    "state","local_active_record.txt"
)
db=os.path.join(state,"state","state.sqlite3")

if not os.path.isfile(marker):
    print("STALE_EOF_RECOVERY=NOT_APPLICABLE")
    sys.exit(10)

raw=open(marker,"rb").read()
text=raw.decode("utf-8","replace")
ids=list(dict.fromkeys(re.findall(r"\b[0-9a-fA-F]{64}\b",text)))
if not ids:
    print("STALE_EOF_RECOVERY=NOT_PROVEN")
    sys.exit(11)

con=sqlite3.connect("file:"+db+"?mode=ro", uri=True)
proved=[]
for entry in ids:
    p=con.execute(
        "SELECT offset_bytes FROM progress WHERE entry_id=?",(entry,)
    ).fetchone()
    s=con.execute(
        """SELECT offset_bytes,segment_bytes,next_offset_bytes,eof
           FROM segment_commits WHERE entry_id=?
           ORDER BY committed_ns DESC LIMIT 1""",(entry,)
    ).fetchone()
    if not p or not s:
        continue
    progress=int(p[0]); off=int(s[0]); size=int(s[1]); nxt=int(s[2])
    eof=str(s[3]).upper()
    if eof=="YES" and progress==nxt and off+size==nxt:
        proved.append(entry)
con.close()

if len(proved)!=1:
    print("STALE_EOF_RECOVERY=NOT_PROVEN")
    sys.exit(12)

stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
dest=os.path.join(state,"recovery","stable_single_door_stale_eof",stamp)
os.makedirs(dest,mode=0o700)
os.replace(marker,os.path.join(dest,"local_active_record.stale_eof"))
with open(os.path.join(dest,"proof.txt"),"w",encoding="utf-8") as f:
    f.write("ENTRY_ID="+proved[0]+"\n")
    f.write("SQLITE_ROWS_MODIFIED=0\n")
print("STALE_EOF_RECOVERY=PASS")
print("ENTRY_ID="+proved[0])
print("ARCHIVE="+dest)
PY
}

V3_LOG_MARK=0

start_c5_once() {
    N="$(exact_c5_count)"
    if [ "$N" -eq 1 ]; then
        return 0
    fi
    if [ "$N" -gt 1 ]; then
        log "HOLD=MULTIPLE_C5_V3_PROCESSES count=$N"
        return 1
    fi

    ensure_watcher || return 1
    sleep 1

    V3_LOG_MARK="$(wc -l < "$V3LOG" 2>/dev/null || echo 0)"

    nohup env \
      C5_STATE_ROOT="$STATE" \
      C5_MAX_TURNS=0 \
      C5_MAX_FETCHES=0 \
      C5_ENABLE_LIVE_NETWORK=YES \
      bash "$C5_V3_RUNNER" >> "$V3LOG" 2>&1 &
    P=$!
    printf '%s\n' "$P" > "$V3PIDFILE"
    log "C5_V3_START_ATTEMPT pid=$P"

    sleep 5
    N="$(exact_c5_count)"
    if [ "$N" -ne 1 ]; then
        log "C5_V3_START_RESULT=FAILED count=$N"
        return 1
    fi
    P="$(exact_c5_pid)"
    log "C5_V3_START_RESULT=PASS pid=$P"
    return 0
}

start_internet_once() {
    [ "$(exact_c5_count)" -eq 1 ] || return 1
    N="$(inet_count)"
    if [ "$N" -eq 1 ]; then
        return 0
    fi
    if [ "$N" -gt 1 ]; then
        log "INTERNET_DUPLICATE_PROCESSES count=$N"
        stop_internet || return 1
    fi

    [ -f "$FIX4" ] || {
        log "INTERNET_HOLD=FIX4_MISSING"
        return 1
    }
    H="$(hash1 "$FIX4")"
    [ "$H" = "$FIX4_EXPECTED_SHA" ] || {
        log "INTERNET_HOLD=FIX4_SHA_MISMATCH actual=$H"
        return 1
    }
    [ -d "$PYCOMPAT" ] || {
        log "INTERNET_HOLD=PYTHON_COMPAT_MISSING"
        return 1
    }
    RUN="$(find_inet_runner || true)"
    [ -n "$RUN" ] || {
        log "INTERNET_HOLD=EXACT_RUNNER_NOT_FOUND"
        return 1
    }

    nohup env \
      SIGMA_ROOT="$ROOT" \
      C5_STATE_ROOT="$STATE" \
      PATH="$FIX4_BIN:$PATH" \
      PYTHONPATH="$PYCOMPAT${PYTHONPATH:+:$PYTHONPATH}" \
      bash "$RUN" >> "$INETLOG" 2>&1 &
    P=$!
    log "INTERNET_START_ATTEMPT pid=$P"
    sleep 4
    N="$(inet_count)"
    if [ "$N" -ne 1 ]; then
        log "INTERNET_START_RESULT=FAILED count=$N"
        return 1
    fi
    log "INTERNET_START_RESULT=PASS pid=$(inet_pid)"
    return 0
}

read_counts() {
DB="$DB" python - <<'PY'
import os,sqlite3
db=os.environ["DB"]
con=sqlite3.connect("file:"+db+"?mode=ro",uri=True)
vals=[]
for t in ("segment_commits","evidence","knowledge"):
    vals.append(con.execute('SELECT COUNT(*) FROM "'+t+'"').fetchone()[0])
con.close()
print(*vals)
PY
}

read -r BASE_SEG BASE_EVID BASE_KNOW <<<"$(read_counts)"
log "GROWTH_BASELINE segment_commits=$BASE_SEG evidence=$BASE_EVID knowledge=$BASE_KNOW"

ensure_watcher || exit 87

# Prewarm CURRENT_STREAM from actual runtime markers before the runner starts.
sleep 1

REFUSE_WINDOW_START=0
REFUSE_RESTARTS=0
INET_BACKOFF=15
INET_NEXT=0
C5_STABLE_SINCE=0
LAST_STATUS=0
LAST_GROWTH=0

start_c5_once || true

while :; do
    NOW="$(date +%s)"
    C5N="$(exact_c5_count)"

    if [ "$C5N" -eq 1 ]; then
        if [ "$C5_STABLE_SINCE" -eq 0 ]; then
            C5_STABLE_SINCE="$NOW"
            log "C5_V3_ALIVE=YES pid=$(exact_c5_pid)"
        fi

        if [ $((NOW - C5_STABLE_SINCE)) -ge 120 ]; then
            REFUSE_WINDOW_START=0
            REFUSE_RESTARTS=0
        fi

        # Internet is subordinate: only attach after V3 remains alive for 15 s.
        if [ $((NOW - C5_STABLE_SINCE)) -ge 15 ]; then
            if [ "$(inet_count)" -eq 0 ] && [ "$NOW" -ge "$INET_NEXT" ]; then
                if start_internet_once; then
                    INET_BACKOFF=15
                    INET_NEXT=0
                else
                    INET_NEXT=$((NOW + INET_BACKOFF))
                    if [ "$INET_BACKOFF" -lt 300 ]; then
                        INET_BACKOFF=$((INET_BACKOFF * 2))
                        [ "$INET_BACKOFF" -gt 300 ] && INET_BACKOFF=300
                    fi
                fi
            fi
        fi
    else
        C5_STABLE_SINCE=0
        stop_internet || true

        if [ "$C5N" -gt 1 ]; then
            log "HOLD=MULTIPLE_C5_V3_PROCESSES count=$C5N"
            sleep 30
            continue
        fi

        # Known safe recovery class 1: a committed stale EOF marker.
        REC="$(recover_proven_stale_eof 2>&1)"
        RRC=$?
        printf '%s\n' "$REC" >> "$LOG"
        if [ "$RRC" -eq 0 ]; then
            start_c5_once || true
            sleep 5
            continue
        fi

        # Known recoverable runtime protocol class:
        # REFUSE_STREAM_STATE with deterministic coherence watcher.
        LAST_REFUSAL="$(
            sed -n "$((V3_LOG_MARK + 1)),\$p" "$V3LOG" 2>/dev/null |
            grep 'HOLD=C5_NATIVE_REFUSAL action=REFUSE_STREAM_STATE' |
            tail -n1 || true
        )"

        DESIRED="$(
            awk -F= '$1=="CURRENT_STREAM_DESIRED"{print $2}' \
              "$WATCHER_STATUS" 2>/dev/null | tail -n1
        )"

        if [ -n "$LAST_REFUSAL" ] && {
            [ "$DESIRED" = "LOCAL" ] || [ "$DESIRED" = "EXTERNAL" ];
        }; then
            if [ "$REFUSE_WINDOW_START" -eq 0 ] ||
               [ $((NOW - REFUSE_WINDOW_START)) -gt 600 ]; then
                REFUSE_WINDOW_START="$NOW"
                REFUSE_RESTARTS=0
            fi
            REFUSE_RESTARTS=$((REFUSE_RESTARTS + 1))
            log "STREAM_REFUSAL_SELF_HEAL attempt=$REFUSE_RESTARTS desired=$DESIRED"

            if [ "$REFUSE_RESTARTS" -gt 5 ]; then
                log "HOLD=STREAM_REFUSAL_CIRCUIT_BREAKER attempts=$REFUSE_RESTARTS window_seconds=600"
                sleep 60
                continue
            fi

            sleep 1
            start_c5_once || true
        else
            log "HOLD=UNPROVEN_C5_STOP_NO_AUTOREPAIR watcher_desired=${DESIRED:-NONE}"
            sleep 60
        fi
    fi

    if [ $((NOW - LAST_GROWTH)) -ge 60 ]; then
        LAST_GROWTH="$NOW"
        read -r SEG EVID KNOW <<<"$(read_counts)"
        if [ "$SEG" -lt "$BASE_SEG" ] ||
           [ "$EVID" -lt "$BASE_EVID" ] ||
           [ "$KNOW" -lt "$BASE_KNOW" ]; then
            log "HOLD=STATE_COUNTER_REGRESSION segment_commits=$SEG evidence=$EVID knowledge=$KNOW"
            stop_internet || true
        else
            log "GROWTH_SNAPSHOT segment_commits=$SEG evidence=$EVID knowledge=$KNOW delta_segments=$((SEG-BASE_SEG)) delta_evidence=$((EVID-BASE_EVID)) delta_knowledge=$((KNOW-BASE_KNOW))"
        fi
    fi

    if [ $((NOW - LAST_STATUS)) -ge 15 ]; then
        LAST_STATUS="$NOW"
        {
            printf 'SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2=ACTIVE\n'
            printf 'C5_V3_COUNT=%s\n' "$(exact_c5_count)"
            printf 'C5_V3_PID=%s\n' "$(exact_c5_pid 2>/dev/null || true)"
            printf 'INTERNET_FEEDER_COUNT=%s\n' "$(inet_count)"
            printf 'INTERNET_FEEDER_PID=%s\n' "$(inet_pid 2>/dev/null || true)"
            printf 'C5_COGNITIVE_WRITER_COUNT_REQUIRED=1\n'
            printf 'STREAM_COHERENCE_WATCHER=REQUIRED\n'
            printf 'INTERNET_COGNITIVE_WRITER=NO\n'
            printf 'GLOBAL_TURN_LIMIT=NONE\n'
            printf 'GLOBAL_FETCH_LIMIT=NONE\n'
            printf 'HOST_SEMANTIC_SELECTION=NO\n'
        } > "$STATUS"
    fi

    sleep 5
done
