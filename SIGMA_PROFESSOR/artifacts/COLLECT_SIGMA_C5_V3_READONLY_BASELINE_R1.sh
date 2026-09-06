#!/data/data/com.termux/files/usr/bin/bash
# External observation only. Never source this file. No SIGMA/VM is started.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
    printf 'HOLD=RUN_OBSERVER_AS_SEPARATE_PROCESS\n'
    return 2
fi
set -u
set -o pipefail
umask 077
export LC_ALL=C
ROOT="$HOME/SIGMA/sigma_genesis1"
STATE="$ROOT/.sigma_c5_real_shadow_v2"
RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
PIDFILE="$ROOT/C5_V3_CONTINUOUS.pid"
LOG="$ROOT/C5_V3_CONTINUOUS.log"
DB="$STATE/state/state.sqlite3"
OUTBASE="$HOME/SIGMA_OBSERVATIONS"
EXPECTED_FP=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125
EXPECTED_RUNNER=a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb
EXPECTED_CORE=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
EXPECTED_CC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
for cmd in date readlink mktemp mkdir cat tail sed grep tr awk sha256sum find sort head od sleep; do
    command -v "$cmd" >/dev/null || { printf 'HOLD=MISSING_TOOL tool=%s\n' "$cmd"; exit 3; }
done
[[ -d "$ROOT" ]] || { printf 'HOLD=CANONICAL_ROOT_MISSING\n'; exit 4; }
[[ "$(readlink -f -- "$ROOT")" == "$ROOT" ]] || { printf 'HOLD=ROOT_PATH_REDIRECTED\n'; exit 5; }
[[ -d "$STATE" && "$(readlink -f -- "$STATE")" == "$STATE" ]] || { printf 'HOLD=STATE_PATH_MISSING_OR_REDIRECTED\n'; exit 6; }
[[ ! -L "$OUTBASE" ]] || { printf 'HOLD=REPORT_DIRECTORY_IS_SYMLINK\n'; exit 7; }
mkdir -p -- "$OUTBASE" || exit 8
case "$(readlink -f -- "$OUTBASE")/" in "$ROOT/"*) printf 'HOLD=REPORT_DIRECTORY_INSIDE_RUNTIME\n'; exit 9 ;; esac
OUT="$(mktemp -d "$OUTBASE/c5-v3-readonly.XXXXXX")" || exit 10
trap 'printf "OBSERVATION_INTERRUPTED=YES REPORT_DIR=%s\n" "$OUT"; exit 130' INT TERM
hash_observation() {
    local label="$1" file="$2" expected="$3" actual
    printf '%s_PATH=%s\n%s_EXPECTED_SHA256=%s\n' "$label" "$file" "$label" "$expected"
    if [[ -f "$file" && -r "$file" ]]; then
        actual="$(sha256sum -- "$file")" || { printf '%s_READ_ERROR=YES\n' "$label"; return; }
        actual="${actual%% *}"
        printf '%s_ACTUAL_SHA256=%s\n' "$label" "$actual"
        [[ "$actual" == "$expected" ]] && printf '%s_HASH_MATCH=YES\n' "$label" || printf '%s_HASH_MATCH=NO\n' "$label"
    else
        printf '%s_FILE=MISSING_OR_UNREADABLE\n' "$label"
    fi
}
process_observation() {
    local pid="$1" arg raw count=0 found=0
    case "$pid" in ''|*[!0-9]*) printf 'PIDFILE_VALUE=INVALID_OR_MISSING\n'; return ;; esac
    printf 'PIDFILE_PID=%s\n' "$pid"
    if [[ ! -r "/proc/$pid/stat" ]]; then printf 'PID_PROC=ABSENT_OR_UNREADABLE\n'; return; fi
    raw="$(cat "/proc/$pid/stat")" || return
    printf 'PROC_START_TICKS=%s\n' "$(printf '%s\n' "${raw##*) }" | awk '{print $20}')"
    if [[ -r /proc/sys/kernel/random/boot_id ]]; then printf 'BOOT_ID=%s\n' "$(cat /proc/sys/kernel/random/boot_id)"; fi
    printf 'PROC_CWD=%s\n' "$(readlink "/proc/$pid/cwd" 2>/dev/null || true)"
    printf 'PROC_EXE=%s\n' "$(readlink "/proc/$pid/exe" 2>/dev/null || true)"
    if [[ -r "/proc/$pid/cmdline" ]]; then
        while IFS= read -r -d '' arg; do
            printf 'PROC_ARG_%s=%q\n' "$count" "$arg"
            [[ "$arg" == "$RUNNER" ]] && found=1
            count=$((count + 1))
        done < "/proc/$pid/cmdline"
    fi
    printf 'EXACT_RUNNER_PATH_IN_ARGV=%s\n' "$found"
    if [[ -r "/proc/$pid/environ" ]]; then
        tr '\000' '\n' < "/proc/$pid/environ" | grep -E '^(SIGMA_ROOT|C5_STATE_ROOT|C5_MAX_TURNS|C5_MAX_FETCHES|C5_ENABLE_LIVE_NETWORK)=' || true
    else
        printf 'PROC_ALLOWED_ENV=UNREADABLE\n'
    fi
    if command -v ps >/dev/null; then ps -p "$pid" -o pid=,ppid=,etime=,stat=,args= 2>/dev/null || true; fi
    printf 'PROCESS_ARGV_AND_FILES_ARE_OBSERVATIONS_NOT_LOADED_CODE_ATTESTATION=YES\n'
}
read_database() {
    local rc header actual_db
    printf '\n--- DATABASE OBSERVATIONS ---\nDB_PATH=%s\n' "$DB"
    if ! command -v sqlite3 >/dev/null || ! command -v timeout >/dev/null; then
        printf 'DATABASE_OBSERVATION=SKIPPED_SQLITE3_OR_TIMEOUT_UNAVAILABLE\n'; return
    fi
    [[ -f "$DB" && -r "$DB" ]] || { printf 'DATABASE_OBSERVATION=MISSING_OR_UNREADABLE\n'; return; }
    actual_db="$(readlink -f -- "$DB")"
    [[ "$actual_db" == "$DB" ]] || { printf 'DATABASE_OBSERVATION=SKIPPED_PATH_REDIRECTED\n'; return; }
    header="$(od -An -tu1 -j18 -N2 "$DB" | awk '{$1=$1;print}')"
    if [[ "$header" == '2 2' && ( ! -f "$DB-wal" || ! -f "$DB-shm" ) ]]; then
        printf 'DATABASE_OBSERVATION=SKIPPED_WAL_SIDECAR_MISSING\n'; return
    fi
    if [[ -s "$DB-journal" ]]; then printf 'DATABASE_OBSERVATION=SKIPPED_ROLLBACK_JOURNAL_PRESENT\n'; return; fi
    printf 'SQLITE_VERSION='; sqlite3 -version
    # SELECT-only transaction. WAL coordination metadata may change.
    timeout -k 2s 8s sqlite3 -batch -readonly -init /dev/null "$DB" <<'SQL'
.timeout 1500
.bail on
.mode list
PRAGMA query_only=ON;
PRAGMA temp_store=MEMORY;
BEGIN;
SELECT 'SQLITE_READ_BEGIN=' || strftime('%Y-%m-%dT%H:%M:%SZ','now');
SELECT 'SCHEMA|' || name || '|' || sql FROM sqlite_master WHERE type='table' AND name IN ('entry_state','segment_commits','evidence','knowledge','requests','backup_queue') ORDER BY name;
SELECT 'COUNT_SEGMENT_COMMITS=' || COUNT(*) FROM segment_commits;
SELECT 'COUNT_EVIDENCE=' || COUNT(*) FROM evidence;
SELECT 'COUNT_KNOWLEDGE=' || COUNT(*) FROM knowledge;
SELECT 'COUNT_REQUESTS=' || COUNT(*) FROM requests;
SELECT 'COUNT_ENTRY_STATE=' || COUNT(*) FROM entry_state;
SELECT 'ENTRY_STATE_COUNT|' || quote(state) || '|' || COUNT(*) FROM entry_state GROUP BY state;
SELECT 'HOLD_REASON_COUNT|' || quote(reason) || '|' || COUNT(*) FROM entry_state WHERE state='HOLD' GROUP BY reason ORDER BY COUNT(*) DESC LIMIT 12;
SELECT 'LATEST_KNOWLEDGE_UPDATED_NS=' || COALESCE(MAX(updated_ns),'NULL') FROM knowledge;
SELECT 'LATEST_ENTRY_UPDATED_NS=' || COALESCE(MAX(updated_ns),'NULL') FROM entry_state;
.mode quote
SELECT 'RECENT_ENTRY',entry_id,state,reason,updated_ns,substr(target_record,1,1000) FROM entry_state ORDER BY updated_ns DESC,entry_id DESC LIMIT 5;
SELECT 'RECENT_KNOWLEDGE',key_sha,updated_ns,substr(record,1,1000) FROM knowledge ORDER BY updated_ns DESC,key_sha DESC LIMIT 3;
COMMIT;
.mode list
SELECT 'SQLITE_READ_FINISHED=YES';
SQL
    rc=$?
    printf 'SQLITE_READ_RC=%s\n' "$rc"
    if [[ "$rc" -ne 0 ]]; then printf 'DATABASE_OBSERVATION=PARTIAL_OR_FAILED_NOT_ZERO_COUNTERS\n'; fi
}
snapshot() {
    local sample="$1" pid p matches=0 f
    printf '\n=== C5_V3_READONLY_SAMPLE_%s ===\n' "$sample"
    printf 'SAMPLE_UTC=%s\nSAMPLE_EPOCH=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$(date +%s)"
    printf 'ROOT=%s\nDECLARED_STATE_LINEAGE=%s\n' "$ROOT" "$STATE"
    pid="$(cat "$PIDFILE" 2>/dev/null || true)"
    process_observation "$pid"
    printf '\n--- RUNNER PROCESS CANDIDATES ---\n'
    if command -v pgrep >/dev/null; then
        while IFS= read -r p; do
            [[ -r "/proc/$p/cmdline" ]] || continue
            printf 'RUNNER_NAME_CANDIDATE_PID=%s ARGV=' "$p"
            tr '\000' ' ' < "/proc/$p/cmdline"; printf '\n'
            matches=$((matches + 1))
        done < <(pgrep -f '[R]UN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE[.]sh' || true)
        printf 'RUNNER_NAME_CANDIDATE_COUNT=%s\n' "$matches"
        printf 'COGNITIVE_WRITER_COUNT=NOT_PROVEN_BY_PROCESS_NAMES\n'
    fi
    printf '\n--- RAW LOG TAIL: AT MOST 32768 BYTES / 80 LINES ---\n'
    if [[ -r "$LOG" ]]; then tail -c 32768 -- "$LOG" | tail -n 80; else printf 'LOG=MISSING_OR_UNREADABLE\n'; fi
    read_database
    for f in "$STATE/review/reports" "$STATE/error_vault"; do
        printf '\n--- RECENT FILES %s ---\n' "$f"
        if [[ -d "$f" ]] && command -v timeout >/dev/null; then
            timeout -k 1s 5s find "$f" -maxdepth 1 -type f -printf '%T@ %f\n' | sort -nr | head -n 8 || true
        else printf 'FILE_LIST=SKIPPED_MISSING_DIRECTORY_OR_TIMEOUT\n'; fi
    done
    printf 'SAMPLE_END_UTC=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
{
    printf 'OBSERVATION_ONLY=YES\nPYTHON_USED=NO\nSIGMA_VM_LAUNCHES_BY_THIS_COLLECTOR=0\n'
    printf 'NATIVE_CAPABILITY_ADMISSION=NOT_PERFORMED\nAUTOMATED_HEALTH_VERDICT=NOT_EMITTED\n'
    printf 'APPLICATION_TABLE_WRITES_REQUESTED=NO\nRESTART_OR_REPAIR_REQUESTED=NO\n'
    printf 'SAMPLE_COUNT=3\nPAUSE_BETWEEN_SAMPLES_SECONDS=30\n'
    hash_observation RUNNER "$RUNNER" "$EXPECTED_RUNNER"
    hash_observation CORE "$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma" "$EXPECTED_CORE"
    hash_observation SIGMAC "$ROOT/native/sigmac" "$EXPECTED_CC"
    hash_observation VM "$ROOT/native/sigma-vm.v09_candidate" "$EXPECTED_VM"
    printf '\nEXPECTED_INSTANCE_FINGERPRINT=%s\n' "$EXPECTED_FP"
    printf 'MANIFEST_DISCOVERY_SCOPE=ROOT_DEPTH1_AND_DOT_SIGMA_C5_DEPTH5\n'
    manifest_count=0
    while IFS= read -r -d '' f; do
        manifest_count=$((manifest_count + 1))
        hash_observation IDENTITY_MANIFEST "$f" "$EXPECTED_FP"
    done < <(find "$ROOT" -maxdepth 1 -type f -name SIGMA_INSTANCE_IDENTITY_V1.txt -print0; if [[ -d "$ROOT/.sigma_c5" ]]; then find "$ROOT/.sigma_c5" -maxdepth 5 -type f -name SIGMA_INSTANCE_IDENTITY_V1.txt -print0; fi)
    printf 'IDENTITY_MANIFEST_CANDIDATE_COUNT=%s\n' "$manifest_count"
    printf 'LIVE_INSTANCE_BINDING=NOT_ATTESTED_BY_THIS_COLLECTOR\n'
} > "$OUT/identity.txt" 2>&1
cat "$OUT/identity.txt"
for sample in 1 2 3; do
    snapshot "$sample" > "$OUT/sample_$sample.txt" 2>&1
    # Escape terminal control bytes in the display; raw output remains in files.
    sed 's/[\x00-\x08\x0b-\x1f\x7f]/?/g' "$OUT/sample_$sample.txt"
    [[ "$sample" == 3 ]] || sleep 30
done
printf '\nOBSERVATION_CAPTURE_FINISHED=YES\nREPORT_DIR=%s\n' "$OUT"
printf 'NO_SIGMA_HEALTH_PASS_OR_SELF_REPAIR_CLAIM_WAS_MADE=YES\n'
