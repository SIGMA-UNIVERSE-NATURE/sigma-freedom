#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

ROOT="${SIGMA_ROOT:-$HOME/SIGMA/sigma_genesis1}"
STATE="${C5_STATE_ROOT:-$ROOT/.sigma_c5_real_shadow_v2}"
PIDFILE="$ROOT/C5_V3_CONTINUOUS.pid"
LOG="$ROOT/C5_V3_CONTINUOUS.log"
DB="$STATE/state/state.sqlite3"
CATALOG="$STATE/catalog/catalog_v2.sqlite3"
HEAD="$ROOT/.sigma_native/knowledge_v2/HEAD"
REPORTS="$STATE/review/reports"
ERROR_VAULT="$STATE/error_vault"
REFRESH_SECONDS="${1:-0}"

case "$REFRESH_SECONDS" in
  ''|*[!0-9]*) printf 'USAGE=%s [refresh_seconds_integer]\n' "$0"; exit 2 ;;
esac

PYTHON="$(command -v python 2>/dev/null || true)"
[ -n "$PYTHON" ] || { printf 'HOLD=PYTHON_NOT_FOUND\n'; exit 3; }

snapshot() {
    printf '=== SIGMA C5 LIVE OBSERVER V1 ===\n'
    printf 'OBSERVER_ROLE=MECHANICAL_READ_ONLY\n'
    printf 'OBSERVER_WRITES_C5_STATE=NO\n'
    printf 'STATE_ROOT=%s\n' "$STATE"

    if [ -f "$PIDFILE" ]; then
        PID="$(cat "$PIDFILE" 2>/dev/null || true)"
        printf 'PIDFILE_PID=%s\n' "$PID"
        if [ -n "$PID" ] && kill -0 "$PID" 2>/dev/null; then
            printf 'SIGMA_RUNNING=YES\n'
            ps -p "$PID" -o pid=,ppid=,etime=,stat=,cmd= 2>/dev/null | sed 's/^/PROCESS /' || true
        else
            printf 'SIGMA_RUNNING=NO\n'
        fi
    else
        printf 'PIDFILE=MISSING\nSIGMA_RUNNING=UNKNOWN\n'
    fi

    if [ -f "$LOG" ]; then
        LAST_TURN="$(grep -o 'C5_TURN=[0-9][0-9]*' "$LOG" 2>/dev/null | tail -n 1 | cut -d= -f2 || true)"
        printf 'LAST_OBSERVED_C5_TURN=%s\n' "${LAST_TURN:-NONE}"
        LAST_EVENT="$(grep 'C5_TURN=' "$LOG" 2>/dev/null | tail -n 1 || true)"
        [ -n "$LAST_EVENT" ] && printf 'LAST_TURN_LINE=%s\n' "$LAST_EVENT"

        printf '%s\n' '--- RECENT MACHINE EVENTS ---'
        grep -E 'C5_TURN=|^EVENT |^ACTION |^STATUS |^CURRENT_STREAM |^SEGMENT_ENTRY_ID=|^SEGMENT_OFFSET=|^SEGMENT_BYTES=|EXTERNAL_QUERY|EXTERNAL_FETCH|REVIEW|PAUSE|RESUME|ERROR_VAULT|HOLD=' "$LOG" 2>/dev/null | tail -n 80 || true
    else
        printf 'C5_V3_LOG=MISSING\n'
    fi

    printf '%s\n' '--- PERSISTENT STATE / RECENT NATIVE RECORDS ---'
    "$PYTHON" - "$DB" "$CATALOG" <<'PY'
import base64, hashlib, os, sqlite3, sys

db, catalog = sys.argv[1], sys.argv[2]

def ro(path):
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=2)
    con.execute("PRAGMA query_only=ON")
    con.execute("PRAGMA busy_timeout=2000")
    return con

def safe(v, lim=500):
    if v is None:
        return "NULL"
    if isinstance(v, bytes):
        v = "B64:" + base64.b64encode(v).decode("ascii")
    else:
        v = str(v)
    v = v.replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")
    return v if len(v) <= lim else v[:lim] + "...<TRUNCATED>"

def parse_record(text):
    out = {}
    for f in str(text or "").split(" || "):
        if "=" in f:
            k, v = f.split("=", 1)
            out[k] = v
    return out

if not os.path.isfile(db):
    print("STATE_DB=MISSING")
    raise SystemExit(0)

try:
    c = ro(db)
except Exception as e:
    print("STATE_DB_OPEN=FAILED", type(e).__name__)
    raise SystemExit(0)

for table in ("entry_state","segment_commits","evidence","knowledge","requests","backup_queue"):
    try:
        n = c.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
        print(f"COUNT_{table.upper()}={n}")
    except Exception as e:
        print(f"COUNT_{table.upper()}=READ_ERROR:{type(e).__name__}")

try:
    n = c.execute("SELECT COUNT(*) FROM entry_state WHERE state='HOLD'").fetchone()[0]
    print(f"COUNT_HOLD_ENTRIES={n}")
except Exception as e:
    print("COUNT_HOLD_ENTRIES=READ_ERROR:" + type(e).__name__)

try:
    n = c.execute("SELECT COUNT(*) FROM evidence e LEFT JOIN knowledge k ON k.key_sha=e.key_sha WHERE k.key_sha IS NULL").fetchone()[0]
    print(f"COUNT_UNRESOLVED_EVIDENCE={n}")
except Exception as e:
    print("COUNT_UNRESOLVED_EVIDENCE=READ_ERROR:" + type(e).__name__)

print("RECENT_KNOWLEDGE_BEGIN")
try:
    rows = c.execute("SELECT key_sha,record FROM knowledge ORDER BY updated_ns DESC,key_sha DESC LIMIT 8").fetchall()
    for key, record in rows:
        f = parse_record(record)
        print("RECENT_KNOWLEDGE"
              f" || KEY={safe(key,128)}"
              f" || LEFT={safe(f.get('LEFT','NONE'),160)}"
              f" || RIGHT={safe(f.get('RIGHT','NONE'),160)}"
              f" || SUPPORT_U_LEN={len(f.get('SUPPORT_U',''))}"
              f" || RECORD={safe(record,500)}")
except Exception as e:
    print("RECENT_KNOWLEDGE_READ_ERROR=" + type(e).__name__)
print("RECENT_KNOWLEDGE_END")

print("RECENT_REQUESTS_BEGIN")
try:
    cols = [r[1] for r in c.execute("PRAGMA table_info(requests)").fetchall()]
    if cols:
        order = "updated_ns" if "updated_ns" in cols else "rowid"
        rows = c.execute(f"SELECT * FROM requests ORDER BY {order} DESC LIMIT 8").fetchall()
        for row in rows:
            fields = " || ".join(f"{name}={safe(val,240)}" for name,val in zip(cols,row))
            print("RECENT_REQUEST || " + fields)
except Exception as e:
    print("RECENT_REQUESTS_READ_ERROR=" + type(e).__name__)
print("RECENT_REQUESTS_END")

print("RECENT_ERRORS_BEGIN")
try:
    rows = c.execute("SELECT entry_id,reason,target_record FROM entry_state WHERE state='HOLD' ORDER BY updated_ns DESC,entry_id DESC LIMIT 8").fetchall()
    for eid, reason, target in rows:
        print(f"RECENT_ERROR || ENTRY_ID={safe(eid,128)} || REASON={safe(reason,240)} || TARGET={safe(target,500)}")
except Exception as e:
    print("RECENT_ERRORS_READ_ERROR=" + type(e).__name__)
print("RECENT_ERRORS_END")

# Resolve the most recently committed local entry to an exact catalog path if schema supports it.
latest_entry = None
try:
    cols = [r[1] for r in c.execute("PRAGMA table_info(segment_commits)").fetchall()]
    if "entry_id" in cols:
        order = "committed_ns" if "committed_ns" in cols else ("updated_ns" if "updated_ns" in cols else "rowid")
        r = c.execute(f"SELECT entry_id FROM segment_commits ORDER BY {order} DESC LIMIT 1").fetchone()
        if r: latest_entry = r[0]
except Exception:
    pass
c.close()

if latest_entry:
    print("LATEST_COMMITTED_ENTRY_ID=" + safe(latest_entry,128))
    if os.path.isfile(catalog):
        try:
            cc = ro(catalog)
            cols = [r[1] for r in cc.execute("PRAGMA table_info(entries)").fetchall()]
            if "entry_id" in cols and "path_b64" in cols:
                r = cc.execute("SELECT path_b64 FROM entries WHERE entry_id=? LIMIT 1", (latest_entry,)).fetchone()
                if r and r[0]:
                    raw = base64.b64decode(r[0])
                    print("LATEST_COMMITTED_PATH=" + safe(raw.decode("utf-8","surrogateescape"),800))
            cc.close()
        except Exception as e:
            print("LATEST_COMMITTED_PATH_READ_ERROR=" + type(e).__name__)
PY

    printf '%s\n' '--- REVIEW STATE ---'
    if [ -d "$REPORTS" ]; then
        LATEST_REPORT="$(find "$REPORTS" -maxdepth 1 -type f -print 2>/dev/null | sort | tail -n 1 || true)"
        REPORT_COUNT="$(find "$REPORTS" -maxdepth 1 -type f -print 2>/dev/null | wc -l | tr -d ' ')"
        printf 'REVIEW_REPORT_FILE_COUNT=%s\n' "$REPORT_COUNT"
        if [ -n "$LATEST_REPORT" ]; then
            printf 'LATEST_REVIEW_REPORT=%s\n' "$LATEST_REPORT"
            sed -n '1,80p' "$LATEST_REPORT" 2>/dev/null | sed 's/^/REVIEW_REPORT /'
        else
            printf 'LATEST_REVIEW_REPORT=NONE\n'
        fi
    else
        printf 'REVIEW_REPORT_DIR=MISSING\n'
    fi

    if [ -d "$ERROR_VAULT" ]; then
        ERROR_COUNT="$(find "$ERROR_VAULT" -maxdepth 1 -type f -print 2>/dev/null | wc -l | tr -d ' ')"
        printf 'ERROR_VAULT_FILE_COUNT=%s\n' "$ERROR_COUNT"
        find "$ERROR_VAULT" -maxdepth 1 -type f -print 2>/dev/null | sort | tail -n 8 | sed 's/^/ERROR_VAULT_RECORD /'
    else
        printf 'ERROR_VAULT=MISSING\n'
    fi

    printf '%s\n' '--- LEGACY PRODUCTION HEAD (READ ONLY) ---'
    if [ -f "$HEAD" ]; then
        printf 'KNOWLEDGE_V2_HEAD='; cat "$HEAD" 2>/dev/null; printf '\n'
    else
        printf 'KNOWLEDGE_V2_HEAD=MISSING\n'
    fi
}

if [ "$REFRESH_SECONDS" -eq 0 ]; then
    snapshot
    exit 0
fi

while :; do
    printf '\033[2J\033[H'
    snapshot
    printf '\nOBSERVER_REFRESH_SECONDS=%s\n' "$REFRESH_SECONDS"
    printf 'CTRL_C_STOPS_OBSERVER_ONLY=YES\n'
    sleep "$REFRESH_SECONDS"
done
