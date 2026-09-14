#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:?ROOT required}"
CMD="${2:-status}"
ARG1="${3:-}"
ARG2="${4:-}"
ARG3="${5:-}"
ARG4="${6:-}"

AIL="$ROOT/.sigma_ail"
LIVE_HEAD="$AIL/BRAIN_HEAD"
LIVE_MODEL="$AIL/MODEL_GENERATION"
LIVE_WRITER="$AIL/WRITER.lock"
COORD="$AIL/coordination"
ACTIVE="$COORD/ACTIVE_RUNS"
LEASES="$COORD/LEASES"
STATUS="$COORD/WORKER_STATUS"
DONE="$COORD/COMPLETED_RECEIPTS"
ADMISSIONS="$COORD/ADMISSIONS"
EVIDENCE="$COORD/EVIDENCE"
CONTROL="$COORD/control"
AUDIT="$COORD/AUDIT.log"
COORD_WRITE_LEASE="$LEASES/COORD_WRITE_LEASE.lock"
R1_CANON="$COORD/CANONICAL"

mkdir -p "$ACTIVE" "$LEASES" "$STATUS" "$DONE" "$ADMISSIONS" "$EVIDENCE" "$CONTROL"

now(){ date '+%Y-%m-%dT%H:%M:%S%z'; }
sha(){ sha256sum "$1" | awk '{print $1}'; }
log(){ printf '%s %s\n' "$(now)" "$*" >> "$AUDIT"; }
fail(){ local m="$1"; shift || true; printf '%s\n' "$m"; for x in "$@"; do printf '%s\n' "$x"; done; exit 90; }
need_file(){ [ -f "$1" ] || fail "HOLD=MISSING_FILE:$1"; }
valid_id(){ [[ "$1" =~ ^[A-Za-z0-9._:-]+$ ]]; }

kv_get(){
  local f="$1" k="$2" n v
  n="$(awk -F= -v key="$k" '$1==key{n++} END{print n+0}' "$f")"
  [ "$n" = 1 ] || return 1
  v="$(awk -F= -v key="$k" '$1==key{print substr($0,length(key)+2)}' "$f")"
  printf '%s' "$v"
}
require_key(){
  local f="$1" k="$2" v
  v="$(kv_get "$f" "$k")" || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=MISSING_OR_DUPLICATE_FIELD:$k"
  [ -n "$v" ] || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=EMPTY_FIELD:$k"
  printf '%s' "$v"
}
atomic_write(){
  local f="$1" v="$2" t="${1}.$$.tmp"
  printf '%s\n' "$v" > "$t"
  mv "$t" "$f"
}

reject_parallel_r1_canonical(){
  if [ -s "$R1_CANON/BRAIN_HEAD" ] || [ -s "$R1_CANON/MODEL_GENERATION" ]; then
    fail "COORDINATOR=REJECT" "REASON=PARALLEL_R1_CANONICAL_STATE_PRESENT" "NO_STATE_FORK=MANDATORY"
  fi
}

live_ready(){
  [ -L "$LIVE_HEAD" ] && [ -e "$LIVE_HEAD" ] && [ -s "$LIVE_HEAD" ] || return 1
  [ -L "$LIVE_WRITER" ] && [ -e "$LIVE_WRITER" ] || return 1
  [ -s "$LIVE_MODEL" ] || return 1
}
current_head(){ cat "$LIVE_HEAD"; }
current_model(){ cat "$LIVE_MODEL"; }
resolved(){ readlink -f "$1"; }

validate_live_identity(){
  reject_parallel_r1_canonical
  live_ready || fail "COORDINATOR=REJECT" "REASON=CANONICAL_RUNTIME_ALIAS_NOT_READY" "REQUIRES=.sigma_ail/BRAIN_HEAD_SYMLINK,.sigma_ail/WRITER.lock_SYMLINK,.sigma_ail/MODEL_GENERATION"
  local h m
  h="$(current_head)"; m="$(current_model)"
  [[ "$h" =~ ^[0-9a-fA-F]{32,64}$ ]] || fail "COORDINATOR=REJECT" "REASON=LIVE_BRAIN_HEAD_FORMAT_INVALID"
  [[ "$m" =~ ^[0-9]+$ ]] || fail "COORDINATOR=REJECT" "REASON=MODEL_GENERATION_NOT_INTEGER"
}

native_writer_available(){
  python - "$LIVE_WRITER" <<'PY'
import fcntl, sys
p=sys.argv[1]
try:
    f=open(p,'r+b', buffering=0)
except Exception:
    raise SystemExit(4)
try:
    fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    raise SystemExit(3)
except Exception:
    raise SystemExit(4)
else:
    fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    raise SystemExit(0)
PY
}

admission_key(){ printf '%s' "$1|$2" | sha256sum | awk '{print $1}'; }
admission_valid(){
  local gate="$1" task="$2" expected="$3" key meta rp rs
  key="$(admission_key "$gate" "$task")"; meta="$ADMISSIONS/$key.meta"
  [ -f "$meta" ] || return 1
  [ "$(kv_get "$meta" GATE 2>/dev/null || true)" = "$gate" ] || return 1
  [ "$(kv_get "$meta" TASK 2>/dev/null || true)" = "$task" ] || return 1
  [ "$(kv_get "$meta" RECEIPT_LABEL 2>/dev/null || true)" = "$expected" ] || return 1
  rp="$(kv_get "$meta" RECEIPT_PATH 2>/dev/null || true)"; rs="$(kv_get "$meta" RECEIPT_SHA256 2>/dev/null || true)"
  [ -f "$rp" ] || return 1
  [ "$(sha "$rp")" = "$rs" ] || return 1
}

verify_runtime(){
  validate_live_identity
  local out="$EVIDENCE/runtime_attach.$(date +%Y%m%dT%H%M%S).$$.receipt"
  local lock_state rc
  set +e; native_writer_available; rc=$?; set -e
  case "$rc" in 0) lock_state=AVAILABLE ;; 3) lock_state=BUSY ;; *) fail "RUNTIME_VERIFY=REJECT" "REASON=NATIVE_WRITER_LOCK_CHECK_FAILED" ;; esac
  {
    echo "SCHEMA=ONE_SIGMA_AIL_COORDINATOR_RUNTIME_BINDING_R2"
    echo "ONE_SIGMA_AIL=YES"
    echo "BRAIN_HEAD=$(current_head)"
    echo "MODEL_GENERATION=$(current_model)"
    echo "BRAIN_HEAD_ALIAS=$LIVE_HEAD"
    echo "BRAIN_HEAD_TARGET=$(resolved "$LIVE_HEAD")"
    echo "WRITER_LOCK_ALIAS=$LIVE_WRITER"
    echo "WRITER_LOCK_TARGET=$(resolved "$LIVE_WRITER")"
    echo "NATIVE_WRITER_LOCK_STATE=$lock_state"
    echo "VERIFIED_AT=$(now)"
    echo "HOST_COGNITION=NO"
    echo "NO_STATE_FORK=MANDATORY"
  } > "$out"
  log "RUNTIME_VERIFY HEAD=$(current_head) MODEL=$(current_model) WRITER=$lock_state RECEIPT=$(sha "$out")"
  echo "ONE_SIGMA_AIL=YES"
  echo "RUNTIME_VERIFY=PASS"
  echo "CANONICAL_BRAIN_HEAD=$(current_head)"
  echo "CANONICAL_MODEL_GENERATION=$(current_model)"
  echo "NATIVE_WRITER_LOCK_STATE=$lock_state"
  echo "EVIDENCE_RECEIPT=$out"
  echo "EVIDENCE_RECEIPT_SHA256=$(sha "$out")"
}

attach(){
  local receipt="$ARG1"
  [ -n "$receipt" ] || fail "USAGE=$0 ROOT attach RUNTIME_BINDING_RECEIPT"
  validate_live_identity; need_file "$receipt"
  [ "$(kv_get "$receipt" SCHEMA 2>/dev/null || true)" = "ONE_SIGMA_AIL_COORDINATOR_RUNTIME_BINDING_R2" ] || fail "ATTACH=REJECT" "REASON=WRONG_RUNTIME_RECEIPT_SCHEMA"
  [ "$(kv_get "$receipt" BRAIN_HEAD 2>/dev/null || true)" = "$(current_head)" ] || fail "ATTACH=REJECT" "REASON=RUNTIME_HEAD_DRIFT"
  [ "$(kv_get "$receipt" MODEL_GENERATION 2>/dev/null || true)" = "$(current_model)" ] || fail "ATTACH=REJECT" "REASON=MODEL_GENERATION_DRIFT"
  atomic_write "$COORD/ATTACHED_RUNTIME_RECEIPT" "$receipt"
  atomic_write "$COORD/ATTACHED_RUNTIME_RECEIPT_SHA256" "$(sha "$receipt")"
  log "ATTACH HEAD=$(current_head) MODEL=$(current_model) RECEIPT_SHA=$(sha "$receipt")"
  echo "ONE_SIGMA_AIL=YES"
  echo "ATTACH=PASS"
  echo "CANONICAL_BRAIN_HEAD=$(current_head)"
  echo "CANONICAL_MODEL_GENERATION=$(current_model)"
  echo "CANONICAL_HEAD_AUTHORITY=OPPO_RUNTIME_ALIAS"
  echo "CANONICAL_WRITER_AUTHORITY=OPPO_R3_NATIVE_LOCK_ALIAS"
}

attached_ready(){
  validate_live_identity
  local p s
  p="$(cat "$COORD/ATTACHED_RUNTIME_RECEIPT" 2>/dev/null || true)"; s="$(cat "$COORD/ATTACHED_RUNTIME_RECEIPT_SHA256" 2>/dev/null || true)"
  [ -f "$p" ] && [ "$(sha "$p")" = "$s" ] || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=COORDINATOR_NOT_ATTACHED_TO_RUNTIME"
}

admit(){
  local gate="$ARG1" task="$ARG2" label="$ARG3" receipt="$ARG4" key meta tmp
  attached_ready
  [ -n "$gate" ] && [ -n "$task" ] && [ -n "$label" ] && [ -n "$receipt" ] || fail "USAGE=$0 ROOT admit GATE TASK RECEIPT_LABEL RECEIPT_PATH"
  valid_id "$gate" || fail "ADMISSION_REGISTER=REJECT" "REASON=INVALID_GATE_ID"
  valid_id "$label" || fail "ADMISSION_REGISTER=REJECT" "REASON=INVALID_RECEIPT_LABEL"
  need_file "$receipt"
  key="$(admission_key "$gate" "$task")"; meta="$ADMISSIONS/$key.meta"; tmp="$meta.$$.tmp"
  {
    echo "GATE=$gate"; echo "TASK=$task"; echo "RECEIPT_LABEL=$label"; echo "RECEIPT_PATH=$receipt"; echo "RECEIPT_SHA256=$(sha "$receipt")"; echo "REGISTERED_AT=$(now)"
  } > "$tmp"; mv "$tmp" "$meta"
  log "ADMISSION_REGISTER GATE=$gate TASK_SHA=$key RECEIPT_SHA=$(sha "$receipt")"
  echo "ADMISSION_REGISTER=PASS"; echo "ADMISSION_KEY=$key"; echo "RECEIPT_SHA256=$(sha "$receipt")"
}

register(){
  local req="$ARG1" worker run task lane parent model access gate expected curh curm rundir lease_tmp stale=NO rc
  attached_ready; need_file "$req"
  worker="$(require_key "$req" WORKER_ID)"; run="$(require_key "$req" RUN_ID)"; task="$(require_key "$req" TASK)"; lane="$(require_key "$req" GENERATION_LANE)"
  parent="$(require_key "$req" PARENT_BRAIN_HEAD)"; model="$(require_key "$req" MODEL_GENERATION)"; access="$(require_key "$req" ACCESS_MODE)"
  gate="$(require_key "$req" EXPECTED_GATE)"; expected="$(require_key "$req" EXPECTED_RECEIPT)"
  valid_id "$worker" || fail "WRITE=REJECT" "REASON=INVALID_WORKER_ID"
  valid_id "$run" || fail "WRITE=REJECT" "REASON=INVALID_RUN_ID"
  [ "$access" = READ ] || [ "$access" = WRITE ] || fail "WRITE=REJECT" "REASON=INVALID_ACCESS_MODE"
  [ ! -e "$ACTIVE/$run" ] && [ ! -e "$DONE/$run.receipt" ] || fail "WRITE=REJECT" "REASON=RUN_ID_ALREADY_EXISTS"
  curh="$(current_head)"; curm="$(current_model)"

  if [ "$access" = READ ]; then
    [ "$parent" = "$curh" ] && [ "$model" = "$curm" ] || stale=YES
    rundir="$ACTIVE/$run"; mkdir "$rundir"; cp "$req" "$rundir/request.env"
    { echo "LEASE=READ_ONLY"; echo "AUTHORIZED_PARENT_HEAD=$curh"; echo "AUTHORIZED_MODEL_GENERATION=$curm"; echo "READ_ONLY_STALE_VIEW=$stale"; echo "GRANTED_AT=$(now)"; } > "$rundir/authorization.env"
    { echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=READ_ONLY"; echo "UPDATED_AT=$(now)"; } > "$STATUS/$worker.status"
    log "REGISTER READ WORKER=$worker RUN=$run STALE=$stale"
    echo "LEASE=GRANTED_READ_ONLY"; echo "AUTHORIZED_PARENT_HEAD=$curh"; echo "AUTHORIZED_MODEL_GENERATION=$curm"; echo "READ_ONLY_STALE_VIEW=$stale"
    echo "WRITE=REJECT"; echo "LEARN=REJECT"; echo "COMMIT=REJECT"; return 0
  fi

  [ "$parent" = "$curh" ] || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=STALE_HEAD_WRITER" "STALE_HEAD_WRITER=REJECT" "CURRENT_HEAD=$curh"
  [ "$model" = "$curm" ] || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=STALE_MODEL_GENERATION" "CURRENT_MODEL_GENERATION=$curm"
  admission_valid "$gate" "$task" "$expected" || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=TASK_NOT_ADMITTED_OR_RECEIPT_DRIFT"
  set +e; native_writer_available; rc=$?; set -e
  [ "$rc" = 0 ] || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=NATIVE_WRITER_ACTIVE" "CONFLICTING_LEASE=REJECT"
  if ! mkdir "$COORD_WRITE_LEASE" 2>/dev/null; then fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=CONFLICTING_COORDINATION_LEASE" "CONFLICTING_LEASE=REJECT"; fi
  trap 'rmdir "$COORD_WRITE_LEASE" 2>/dev/null || true' ERR INT TERM HUP
  rundir="$ACTIVE/$run"; mkdir "$rundir"; cp "$req" "$rundir/request.env"
  lease_tmp="$COORD_WRITE_LEASE/lease.env.$$.tmp"
  { echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "TASK=$task"; echo "GENERATION_LANE=$lane"; echo "AUTHORIZED_PARENT_HEAD=$curh"; echo "AUTHORIZED_MODEL_GENERATION=$curm"; echo "EXPECTED_GATE=$gate"; echo "EXPECTED_RECEIPT=$expected"; echo "GRANTED_AT=$(now)"; } > "$lease_tmp"
  mv "$lease_tmp" "$COORD_WRITE_LEASE/lease.env"; cp "$COORD_WRITE_LEASE/lease.env" "$rundir/authorization.env"
  { echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=WRITE_LEASE_ACTIVE"; echo "UPDATED_AT=$(now)"; } > "$STATUS/$worker.status"
  trap - ERR INT TERM HUP
  log "REGISTER WRITE WORKER=$worker RUN=$run HEAD=$curh MODEL=$curm"
  echo "LEASE=GRANTED"; echo "AUTHORIZED_PARENT_HEAD=$curh"; echo "AUTHORIZED_MODEL_GENERATION=$curm"; echo "ONE_WRITER=YES"
}

authorize(){
  local run="$ARG1" op="$ARG2" rundir access auth lease_run curh curm task gate expected rc
  attached_ready
  [ -n "$run" ] && [ -n "$op" ] || fail "USAGE=$0 ROOT authorize RUN_ID {READ|WRITE|LEARN|COMMIT}"
  case "$op" in READ|WRITE|LEARN|COMMIT) ;; *) fail "$op=REJECT" "REASON=INVALID_OPERATION" ;; esac
  rundir="$ACTIVE/$run"; [ -d "$rundir" ] || fail "$op=REJECT" "UNREGISTERED_WRITER=REJECT" "REASON=RUN_NOT_REGISTERED"
  access="$(kv_get "$rundir/request.env" ACCESS_MODE)"
  if [ "$op" = READ ]; then echo "READ=ALLOW"; echo "RUN_ID=$run"; return 0; fi
  [ "$access" = WRITE ] || fail "$op=REJECT" "REASON=READ_ONLY_RUN"
  [ -f "$COORD_WRITE_LEASE/lease.env" ] || fail "$op=REJECT" "REASON=COORDINATION_LEASE_MISSING"
  lease_run="$(kv_get "$COORD_WRITE_LEASE/lease.env" RUN_ID 2>/dev/null || true)"; [ "$lease_run" = "$run" ] || fail "$op=REJECT" "CONFLICTING_LEASE=REJECT" "REASON=LEASE_OWNED_BY_OTHER_RUN"
  auth="$rundir/authorization.env"; curh="$(current_head)"; curm="$(current_model)"
  [ "$curh" = "$(kv_get "$auth" AUTHORIZED_PARENT_HEAD)" ] || fail "$op=REJECT" "STALE_HEAD_WRITER=REJECT" "REASON=CANONICAL_HEAD_MOVED"
  [ "$curm" = "$(kv_get "$auth" AUTHORIZED_MODEL_GENERATION)" ] || fail "$op=REJECT" "REASON=MODEL_GENERATION_MOVED"
  task="$(kv_get "$rundir/request.env" TASK)"; gate="$(kv_get "$rundir/request.env" EXPECTED_GATE)"; expected="$(kv_get "$rundir/request.env" EXPECTED_RECEIPT)"
  admission_valid "$gate" "$task" "$expected" || fail "$op=REJECT" "REASON=ADMISSION_NO_LONGER_VALID"
  set +e; native_writer_available; rc=$?; set -e
  [ "$rc" = 0 ] || fail "$op=REJECT" "REASON=NATIVE_WRITER_ACTIVE" "CONFLICTING_LEASE=REJECT"
  echo "$op=ALLOW"; echo "LEASE=VALID"; echo "AUTHORIZED_PARENT_HEAD=$curh"; echo "AUTHORIZED_MODEL_GENERATION=$curm"
}

heartbeat(){
  local run="$ARG1" rundir worker
  [ -n "$run" ] || fail "USAGE=$0 ROOT heartbeat RUN_ID"
  rundir="$ACTIVE/$run"; [ -d "$rundir" ] || fail "HEARTBEAT=REJECT" "REASON=RUN_NOT_ACTIVE"
  worker="$(kv_get "$rundir/request.env" WORKER_ID)"
  { echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=ACTIVE"; echo "UPDATED_AT=$(now)"; } > "$STATUS/$worker.status"
  atomic_write "$rundir/heartbeat.txt" "$(now)"; echo "HEARTBEAT=PASS"
}

complete(){
  local comp="$ARG1" run parent result newh mb ma evidence rundir access auth worker lease_run curh curm ersha outtmp
  attached_ready; need_file "$comp"
  run="$(require_key "$comp" RUN_ID)"; parent="$(require_key "$comp" PARENT_HEAD)"; result="$(require_key "$comp" RESULT)"; newh="$(require_key "$comp" NEW_HEAD)"
  mb="$(require_key "$comp" MODEL_GENERATION_BEFORE)"; ma="$(require_key "$comp" MODEL_GENERATION_AFTER)"; evidence="$(require_key "$comp" EVIDENCE_RECEIPT)"
  rundir="$ACTIVE/$run"; [ -d "$rundir" ] || fail "COMMIT=REJECT" "REASON=UNREGISTERED_WRITER" "UNREGISTERED_WRITER=REJECT"
  access="$(kv_get "$rundir/request.env" ACCESS_MODE)"; worker="$(kv_get "$rundir/request.env" WORKER_ID)"; auth="$rundir/authorization.env"
  [ "$access" = WRITE ] || fail "COMMIT=REJECT" "REASON=READ_ONLY_RUN"
  [ -f "$COORD_WRITE_LEASE/lease.env" ] || fail "COMMIT=REJECT" "REASON=COORDINATION_LEASE_MISSING"
  lease_run="$(kv_get "$COORD_WRITE_LEASE/lease.env" RUN_ID)"; [ "$lease_run" = "$run" ] || fail "COMMIT=REJECT" "REASON=CONFLICTING_LEASE" "CONFLICTING_LEASE=REJECT"
  [ "$parent" = "$(kv_get "$auth" AUTHORIZED_PARENT_HEAD)" ] || fail "COMMIT=REJECT" "REASON=PARENT_NOT_AUTHORIZED"
  [ "$mb" = "$(kv_get "$auth" AUTHORIZED_MODEL_GENERATION)" ] || fail "COMMIT=REJECT" "REASON=MODEL_GENERATION_NOT_AUTHORIZED"
  need_file "$evidence"; ersha="$(sha "$evidence")"
  curh="$(current_head)"; curm="$(current_model)"
  if [ "$newh" = NO_COMMIT ]; then
    [ "$curh" = "$parent" ] || fail "COMMIT=REJECT" "REASON=HEAD_CHANGED_DURING_NO_COMMIT" "STALE_HEAD_WRITER=REJECT"
    [ "$ma" = "$mb" ] && [ "$curm" = "$mb" ] || fail "COMMIT=REJECT" "REASON=NO_COMMIT_MODEL_CHANGED"
  else
    [[ "$newh" =~ ^[0-9a-fA-F]{32,64}$ ]] || fail "COMMIT=REJECT" "REASON=NEW_HEAD_FORMAT_INVALID"
    [ "$curh" = "$newh" ] || fail "COMMIT=REJECT" "REASON=RUNTIME_HEAD_DOES_NOT_MATCH_REPORTED_NEW_HEAD" "CURRENT_HEAD=$curh"
    [ "$curm" = "$ma" ] || fail "COMMIT=REJECT" "REASON=RUNTIME_MODEL_GENERATION_DOES_NOT_MATCH_REPORT" "CURRENT_MODEL_GENERATION=$curm"
  fi
  outtmp="$DONE/$run.receipt.$$.tmp"
  { cat "$comp"; echo "EVIDENCE_RECEIPT_SHA256=$ersha"; echo "COMPLETED_AT=$(now)"; echo "COORDINATOR_ACCEPTED=YES"; echo "CANONICAL_HEAD_AUTHORITY=OPPO_RUNTIME_ALIAS"; } > "$outtmp"
  mv "$outtmp" "$DONE/$run.receipt"; rm -rf "$ACTIVE/$run" "$COORD_WRITE_LEASE"
  { echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=COMPLETED"; echo "UPDATED_AT=$(now)"; } > "$STATUS/$worker.status"
  log "COMPLETE RUN=$run RESULT=$result NEW_HEAD=$newh MODEL_BEFORE=$mb MODEL_AFTER=$ma EVIDENCE_SHA=$ersha"
  echo "COMMIT_AUTHORITY=ONE_SIGMA_AIL"; echo "RESULT_ACCEPTED=YES"; echo "CANONICAL_BRAIN_HEAD=$(current_head)"; echo "CANONICAL_MODEL_GENERATION=$(current_model)"
}

abort_run(){
  local run="$ARG1" reason="$ARG2" rundir access lease_run worker
  [ -n "$run" ] && [ -n "$reason" ] || fail "USAGE=$0 ROOT abort RUN_ID REASON"
  rundir="$ACTIVE/$run"; [ -d "$rundir" ] || fail "ABORT=REJECT" "REASON=RUN_NOT_ACTIVE"
  access="$(kv_get "$rundir/request.env" ACCESS_MODE)"; worker="$(kv_get "$rundir/request.env" WORKER_ID)"
  if [ "$access" = WRITE ] && [ -f "$COORD_WRITE_LEASE/lease.env" ]; then lease_run="$(kv_get "$COORD_WRITE_LEASE/lease.env" RUN_ID 2>/dev/null || true)"; [ "$lease_run" = "$run" ] && rm -rf "$COORD_WRITE_LEASE"; fi
  { echo "RUN_ID=$run"; echo "RESULT=ABORTED"; echo "NEW_HEAD=NO_COMMIT"; echo "REASON=$reason"; echo "COMPLETED_AT=$(now)"; echo "COORDINATOR_ACCEPTED=NO_COMMIT"; } > "$DONE/$run.receipt"
  rm -rf "$rundir"; { echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=ABORTED"; echo "UPDATED_AT=$(now)"; } > "$STATUS/$worker.status"
  log "ABORT RUN=$run REASON=$reason"; echo "ABORT=PASS"; echo "NEW_HEAD=NO_COMMIT"
}

status_cmd(){
  echo "ONE_SIGMA_AIL=YES"; echo "ONE_WRITER=YES"; echo "UNREGISTERED_WRITER=REJECT"; echo "STALE_HEAD_WRITER=REJECT"; echo "CONFLICTING_LEASE=REJECT"; echo "HOST_COGNITION=NO"; echo "NO_STATE_FORK=MANDATORY"
  if live_ready; then
    echo "CANONICAL_BRAIN_HEAD=$(current_head)"; echo "CANONICAL_MODEL_GENERATION=$(current_model)"; echo "BRAIN_HEAD_TARGET=$(resolved "$LIVE_HEAD")"; echo "WRITER_LOCK_TARGET=$(resolved "$LIVE_WRITER")"
  else echo "CANONICAL_RUNTIME_STATE=NOT_READY"; fi
  if [ -f "$COORD_WRITE_LEASE/lease.env" ]; then echo "ACTIVE_WRITER=YES"; cat "$COORD_WRITE_LEASE/lease.env"; else echo "ACTIVE_WRITER=NO"; fi
  echo "ACTIVE_RUN_COUNT=$(find "$ACTIVE" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
  echo "COMPLETED_RECEIPT_COUNT=$(find "$DONE" -maxdepth 1 -type f -name '*.receipt' | wc -l | tr -d ' ')"
  echo "COORDINATOR_WRITES_RUNTIME_HEAD=NO"
  echo "COORDINATOR_WRITES_MODEL_GENERATION=NO"
}

case "$CMD" in
  verify-runtime) verify_runtime ;;
  attach) attach ;;
  admit) admit ;;
  register) register ;;
  authorize) authorize ;;
  heartbeat) heartbeat ;;
  complete) complete ;;
  abort) abort_run ;;
  status) status_cmd ;;
  *) echo "USAGE: $0 ROOT {verify-runtime|attach RECEIPT|admit GATE TASK RECEIPT_LABEL RECEIPT_PATH|register REQUEST_FILE|authorize RUN_ID OP|heartbeat RUN_ID|complete COMPLETION_FILE|abort RUN_ID REASON|status}"; exit 2 ;;
esac
