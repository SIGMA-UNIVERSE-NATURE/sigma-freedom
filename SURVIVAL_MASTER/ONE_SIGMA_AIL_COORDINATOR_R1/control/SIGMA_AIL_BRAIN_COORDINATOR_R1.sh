#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:?ROOT required}"
CMD="${2:-status}"
ARG1="${3:-}"
ARG2="${4:-}"
ARG3="${5:-}"
ARG4="${6:-}"
AIL="$ROOT/.sigma_ail"
COORD="$AIL/coordination"
CANON="$COORD/CANONICAL"
ACTIVE="$COORD/ACTIVE_RUNS"
LEASES="$COORD/LEASES"
STATUS="$COORD/WORKER_STATUS"
DONE="$COORD/COMPLETED_RECEIPTS"
ADMISSIONS="$COORD/ADMISSIONS"
CONTROL="$COORD/control"
AUDIT="$COORD/AUDIT.log"
WRITE_LOCK="$LEASES/WRITE.lock"

mkdir -p "$CANON" "$ACTIVE" "$LEASES" "$STATUS" "$DONE" "$ADMISSIONS" "$CONTROL"

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
  v="$(kv_get "$f" "$k")" || fail "WRITE=REJECT" "REASON=MISSING_OR_DUPLICATE_FIELD:$k"
  [ -n "$v" ] || fail "WRITE=REJECT" "REASON=EMPTY_FIELD:$k"
  printf '%s' "$v"
}

atomic_write(){
  local f v t
  f="$1"; v="$2"; t="${f}.$$.tmp"
  printf '%s\n' "$v" > "$t"
  mv "$t" "$f"
}

canonical_ready(){ [ -s "$CANON/BRAIN_HEAD" ] && [ -s "$CANON/MODEL_GENERATION" ]; }
current_head(){ cat "$CANON/BRAIN_HEAD"; }
current_model(){ cat "$CANON/MODEL_GENERATION"; }

admission_key(){
  local gate="$1" task="$2"
  printf '%s' "$gate|$task" | sha256sum | awk '{print $1}'
}

admission_valid(){
  local gate="$1" task="$2" expected="$3" key meta
  key="$(admission_key "$gate" "$task")"
  meta="$ADMISSIONS/$key.meta"
  [ -f "$meta" ] || return 1
  [ "$(kv_get "$meta" GATE 2>/dev/null || true)" = "$gate" ] || return 1
  [ "$(kv_get "$meta" TASK 2>/dev/null || true)" = "$task" ] || return 1
  [ "$(kv_get "$meta" RECEIPT_LABEL 2>/dev/null || true)" = "$expected" ] || return 1
  local rp rs
  rp="$(kv_get "$meta" RECEIPT_PATH 2>/dev/null || true)"
  rs="$(kv_get "$meta" RECEIPT_SHA256 2>/dev/null || true)"
  [ -f "$rp" ] || return 1
  [ "$(sha "$rp")" = "$rs" ] || return 1
}

bootstrap(){
  local head="$ARG1" model="$ARG2" receipt="$ARG3"
  [ -n "$head" ] && [ -n "$model" ] && [ -n "$receipt" ] || fail "USAGE=$0 ROOT bootstrap HEAD MODEL_GENERATION EVIDENCE_RECEIPT"
  [ ! -e "$CANON/BRAIN_HEAD" ] && [ ! -e "$CANON/MODEL_GENERATION" ] || fail "BOOTSTRAP=REJECT" "REASON=CANONICAL_ALREADY_INITIALIZED"
  need_file "$receipt"
  atomic_write "$CANON/BRAIN_HEAD" "$head"
  atomic_write "$CANON/MODEL_GENERATION" "$model"
  atomic_write "$CANON/BOOTSTRAP_EVIDENCE_PATH" "$receipt"
  atomic_write "$CANON/BOOTSTRAP_EVIDENCE_SHA256" "$(sha "$receipt")"
  log "BOOTSTRAP HEAD=$head MODEL=$model RECEIPT_SHA=$(sha "$receipt")"
  echo "ONE_SIGMA_AIL=YES"
  echo "BOOTSTRAP=PASS"
  echo "CANONICAL_BRAIN_HEAD=$head"
  echo "CANONICAL_MODEL_GENERATION=$model"
}

admit(){
  local gate="$ARG1" task="$ARG2" label="$ARG3" receipt="$ARG4" key meta tmp
  [ -n "$gate" ] && [ -n "$task" ] && [ -n "$label" ] && [ -n "$receipt" ] || fail "USAGE=$0 ROOT admit GATE TASK RECEIPT_LABEL RECEIPT_PATH"
  valid_id "$gate" || fail "ADMISSION_REGISTER=REJECT" "REASON=INVALID_GATE_ID"
  valid_id "$label" || fail "ADMISSION_REGISTER=REJECT" "REASON=INVALID_RECEIPT_LABEL"
  need_file "$receipt"
  key="$(admission_key "$gate" "$task")"; meta="$ADMISSIONS/$key.meta"; tmp="$meta.$$.tmp"
  {
    echo "GATE=$gate"
    echo "TASK=$task"
    echo "RECEIPT_LABEL=$label"
    echo "RECEIPT_PATH=$receipt"
    echo "RECEIPT_SHA256=$(sha "$receipt")"
    echo "REGISTERED_AT=$(now)"
  } > "$tmp"
  mv "$tmp" "$meta"
  log "ADMISSION_REGISTER GATE=$gate TASK_SHA=$key RECEIPT_SHA=$(sha "$receipt")"
  echo "ADMISSION_REGISTER=PASS"
  echo "ADMISSION_KEY=$key"
  echo "RECEIPT_SHA256=$(sha "$receipt")"
}

register(){
  local req="$ARG1"
  need_file "$req"; canonical_ready || fail "WRITE=REJECT" "REASON=CANONICAL_NOT_INITIALIZED"
  local worker run task lane parent model access gate expected curh curm rundir lease_tmp stale=NO
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
    rundir="$ACTIVE/$run"; mkdir "$rundir"
    cp "$req" "$rundir/request.env"
    {
      echo "LEASE=READ_ONLY"
      echo "AUTHORIZED_PARENT_HEAD=$curh"
      echo "AUTHORIZED_MODEL_GENERATION=$curm"
      echo "READ_ONLY_STALE_VIEW=$stale"
      echo "GRANTED_AT=$(now)"
    } > "$rundir/authorization.env"
    {
      echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=READ_ONLY"; echo "UPDATED_AT=$(now)"
    } > "$STATUS/$worker.status"
    log "REGISTER READ WORKER=$worker RUN=$run STALE=$stale"
    echo "LEASE=GRANTED_READ_ONLY"
    echo "AUTHORIZED_PARENT_HEAD=$curh"
    echo "AUTHORIZED_MODEL_GENERATION=$curm"
    echo "READ_ONLY_STALE_VIEW=$stale"
    echo "WRITE=REJECT"
    echo "LEARN=REJECT"
    echo "COMMIT=REJECT"
    return 0
  fi

  [ "$parent" = "$curh" ] || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=STALE_HEAD_WRITER" "STALE_HEAD_WRITER=REJECT" "CURRENT_HEAD=$curh"
  [ "$model" = "$curm" ] || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=STALE_MODEL_GENERATION" "CURRENT_MODEL_GENERATION=$curm"
  admission_valid "$gate" "$task" "$expected" || fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=TASK_NOT_ADMITTED_OR_RECEIPT_DRIFT"

  if ! mkdir "$WRITE_LOCK" 2>/dev/null; then
    fail "WRITE=REJECT" "LEARN=REJECT" "COMMIT=REJECT" "REASON=CONFLICTING_LEASE" "CONFLICTING_LEASE=REJECT"
  fi
  trap 'rmdir "$WRITE_LOCK" 2>/dev/null || true' ERR INT TERM HUP
  rundir="$ACTIVE/$run"; mkdir "$rundir"
  cp "$req" "$rundir/request.env"
  lease_tmp="$WRITE_LOCK/lease.env.$$.tmp"
  {
    echo "WORKER_ID=$worker"
    echo "RUN_ID=$run"
    echo "TASK=$task"
    echo "GENERATION_LANE=$lane"
    echo "AUTHORIZED_PARENT_HEAD=$curh"
    echo "AUTHORIZED_MODEL_GENERATION=$curm"
    echo "EXPECTED_GATE=$gate"
    echo "EXPECTED_RECEIPT=$expected"
    echo "GRANTED_AT=$(now)"
  } > "$lease_tmp"
  mv "$lease_tmp" "$WRITE_LOCK/lease.env"
  cp "$WRITE_LOCK/lease.env" "$rundir/authorization.env"
  {
    echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=WRITE_LEASE_ACTIVE"; echo "UPDATED_AT=$(now)"
  } > "$STATUS/$worker.status"
  trap - ERR INT TERM HUP
  log "REGISTER WRITE WORKER=$worker RUN=$run HEAD=$curh MODEL=$curm"
  echo "LEASE=GRANTED"
  echo "AUTHORIZED_PARENT_HEAD=$curh"
  echo "AUTHORIZED_MODEL_GENERATION=$curm"
  echo "ONE_WRITER=YES"
}


authorize(){
  local run="$ARG1" op="$ARG2" rundir access auth lease_run curh curm task gate expected
  [ -n "$run" ] && [ -n "$op" ] || fail "USAGE=$0 ROOT authorize RUN_ID {READ|WRITE|LEARN|COMMIT}"
  case "$op" in READ|WRITE|LEARN|COMMIT) ;; *) fail "$op=REJECT" "REASON=INVALID_OPERATION" ;; esac
  rundir="$ACTIVE/$run"
  [ -d "$rundir" ] || fail "$op=REJECT" "UNREGISTERED_WRITER=REJECT" "REASON=RUN_NOT_REGISTERED"
  access="$(kv_get "$rundir/request.env" ACCESS_MODE)"
  if [ "$op" = READ ]; then
    echo "READ=ALLOW"
    echo "RUN_ID=$run"
    return 0
  fi
  [ "$access" = WRITE ] || fail "$op=REJECT" "REASON=READ_ONLY_RUN"
  [ -f "$WRITE_LOCK/lease.env" ] || fail "$op=REJECT" "REASON=WRITE_LEASE_MISSING"
  lease_run="$(kv_get "$WRITE_LOCK/lease.env" RUN_ID 2>/dev/null || true)"
  [ "$lease_run" = "$run" ] || fail "$op=REJECT" "CONFLICTING_LEASE=REJECT" "REASON=LEASE_OWNED_BY_OTHER_RUN"
  auth="$rundir/authorization.env"
  curh="$(current_head)"; curm="$(current_model)"
  [ "$curh" = "$(kv_get "$auth" AUTHORIZED_PARENT_HEAD)" ] || fail "$op=REJECT" "STALE_HEAD_WRITER=REJECT" "REASON=CANONICAL_HEAD_MOVED"
  [ "$curm" = "$(kv_get "$auth" AUTHORIZED_MODEL_GENERATION)" ] || fail "$op=REJECT" "REASON=MODEL_GENERATION_MOVED"
  task="$(kv_get "$rundir/request.env" TASK)"; gate="$(kv_get "$rundir/request.env" EXPECTED_GATE)"; expected="$(kv_get "$rundir/request.env" EXPECTED_RECEIPT)"
  admission_valid "$gate" "$task" "$expected" || fail "$op=REJECT" "REASON=ADMISSION_NO_LONGER_VALID"
  echo "$op=ALLOW"
  echo "LEASE=VALID"
  echo "AUTHORIZED_PARENT_HEAD=$curh"
  echo "AUTHORIZED_MODEL_GENERATION=$curm"
}

heartbeat(){
  local run="$ARG1" rundir worker
  [ -n "$run" ] || fail "USAGE=$0 ROOT heartbeat RUN_ID"
  rundir="$ACTIVE/$run"; [ -d "$rundir" ] || fail "HEARTBEAT=REJECT" "REASON=RUN_NOT_ACTIVE"
  worker="$(kv_get "$rundir/request.env" WORKER_ID)"
  {
    echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=ACTIVE"; echo "UPDATED_AT=$(now)"
  } > "$STATUS/$worker.status"
  atomic_write "$rundir/heartbeat.txt" "$(now)"
  echo "HEARTBEAT=PASS"
}

complete(){
  local comp="$ARG1" run parent result newh mb ma evidence rundir access auth worker lease_run curh curm ersha outtmp
  need_file "$comp"; canonical_ready || fail "COMMIT=REJECT" "REASON=CANONICAL_NOT_INITIALIZED"
  run="$(require_key "$comp" RUN_ID)"; parent="$(require_key "$comp" PARENT_HEAD)"; result="$(require_key "$comp" RESULT)"; newh="$(require_key "$comp" NEW_HEAD)"
  mb="$(require_key "$comp" MODEL_GENERATION_BEFORE)"; ma="$(require_key "$comp" MODEL_GENERATION_AFTER)"; evidence="$(require_key "$comp" EVIDENCE_RECEIPT)"
  rundir="$ACTIVE/$run"; [ -d "$rundir" ] || fail "COMMIT=REJECT" "REASON=UNREGISTERED_WRITER" "UNREGISTERED_WRITER=REJECT"
  access="$(kv_get "$rundir/request.env" ACCESS_MODE)"; worker="$(kv_get "$rundir/request.env" WORKER_ID)"; auth="$rundir/authorization.env"
  [ "$access" = WRITE ] || fail "COMMIT=REJECT" "REASON=READ_ONLY_RUN"
  [ -f "$WRITE_LOCK/lease.env" ] || fail "COMMIT=REJECT" "REASON=WRITE_LEASE_MISSING"
  lease_run="$(kv_get "$WRITE_LOCK/lease.env" RUN_ID)"; [ "$lease_run" = "$run" ] || fail "COMMIT=REJECT" "REASON=CONFLICTING_LEASE" "CONFLICTING_LEASE=REJECT"
  [ "$parent" = "$(kv_get "$auth" AUTHORIZED_PARENT_HEAD)" ] || fail "COMMIT=REJECT" "REASON=PARENT_NOT_AUTHORIZED"
  [ "$mb" = "$(kv_get "$auth" AUTHORIZED_MODEL_GENERATION)" ] || fail "COMMIT=REJECT" "REASON=MODEL_GENERATION_NOT_AUTHORIZED"
  curh="$(current_head)"; curm="$(current_model)"
  [ "$curh" = "$parent" ] || fail "COMMIT=REJECT" "REASON=STALE_HEAD_AT_COMMIT" "STALE_HEAD_WRITER=REJECT" "CURRENT_HEAD=$curh"
  [ "$curm" = "$mb" ] || fail "COMMIT=REJECT" "REASON=MODEL_GENERATION_CHANGED_DURING_RUN"
  need_file "$evidence"; ersha="$(sha "$evidence")"

  if [ "$newh" = NO_COMMIT ]; then
    [ "$ma" = "$mb" ] || fail "COMMIT=REJECT" "REASON=NO_COMMIT_MODEL_CHANGED"
  else
    [[ "$newh" =~ ^[0-9a-fA-F]{40,64}$ ]] || fail "COMMIT=REJECT" "REASON=NEW_HEAD_FORMAT_INVALID"
    # Coordinator is the sole authority that advances the canonical coordination head/model pointer.
    atomic_write "$CANON/BRAIN_HEAD" "$newh"
    atomic_write "$CANON/MODEL_GENERATION" "$ma"
  fi

  outtmp="$DONE/$run.receipt.$$.tmp"
  {
    cat "$comp"
    echo "EVIDENCE_RECEIPT_SHA256=$ersha"
    echo "COMPLETED_AT=$(now)"
    echo "COORDINATOR_ACCEPTED=YES"
  } > "$outtmp"
  mv "$outtmp" "$DONE/$run.receipt"
  rm -rf "$ACTIVE/$run"
  rm -rf "$WRITE_LOCK"
  {
    echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=COMPLETED"; echo "UPDATED_AT=$(now)"
  } > "$STATUS/$worker.status"
  log "COMPLETE RUN=$run RESULT=$result NEW_HEAD=$newh MODEL_BEFORE=$mb MODEL_AFTER=$ma EVIDENCE_SHA=$ersha"
  echo "COMMIT_AUTHORITY=ONE_SIGMA_AIL"
  echo "RESULT_ACCEPTED=YES"
  echo "CANONICAL_BRAIN_HEAD=$(current_head)"
  echo "CANONICAL_MODEL_GENERATION=$(current_model)"
}

abort_run(){
  local run="$ARG1" reason="$ARG2" rundir access lease_run worker
  [ -n "$run" ] && [ -n "$reason" ] || fail "USAGE=$0 ROOT abort RUN_ID REASON"
  rundir="$ACTIVE/$run"; [ -d "$rundir" ] || fail "ABORT=REJECT" "REASON=RUN_NOT_ACTIVE"
  access="$(kv_get "$rundir/request.env" ACCESS_MODE)"; worker="$(kv_get "$rundir/request.env" WORKER_ID)"
  if [ "$access" = WRITE ] && [ -f "$WRITE_LOCK/lease.env" ]; then
    lease_run="$(kv_get "$WRITE_LOCK/lease.env" RUN_ID 2>/dev/null || true)"
    [ "$lease_run" = "$run" ] && rm -rf "$WRITE_LOCK"
  fi
  {
    echo "RUN_ID=$run"; echo "RESULT=ABORTED"; echo "NEW_HEAD=NO_COMMIT"; echo "REASON=$reason"; echo "COMPLETED_AT=$(now)"; echo "COORDINATOR_ACCEPTED=NO_COMMIT"
  } > "$DONE/$run.receipt"
  rm -rf "$rundir"
  {
    echo "WORKER_ID=$worker"; echo "RUN_ID=$run"; echo "STATE=ABORTED"; echo "UPDATED_AT=$(now)"
  } > "$STATUS/$worker.status"
  log "ABORT RUN=$run REASON=$reason"
  echo "ABORT=PASS"
  echo "NEW_HEAD=NO_COMMIT"
}

status_cmd(){
  echo "ONE_SIGMA_AIL=YES"
  echo "ONE_WRITER=YES"
  echo "UNREGISTERED_WRITER=REJECT"
  echo "STALE_HEAD_WRITER=REJECT"
  echo "CONFLICTING_LEASE=REJECT"
  echo "HOST_COGNITION=NO"
  echo "NO_STATE_FORK=MANDATORY"
  if canonical_ready; then
    echo "CANONICAL_BRAIN_HEAD=$(current_head)"
    echo "CANONICAL_MODEL_GENERATION=$(current_model)"
  else
    echo "CANONICAL_STATE=UNINITIALIZED"
  fi
  if [ -f "$WRITE_LOCK/lease.env" ]; then
    echo "ACTIVE_WRITER=YES"
    cat "$WRITE_LOCK/lease.env"
  else
    echo "ACTIVE_WRITER=NO"
  fi
  echo "ACTIVE_RUN_COUNT=$(find "$ACTIVE" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
  echo "COMPLETED_RECEIPT_COUNT=$(find "$DONE" -maxdepth 1 -type f -name '*.receipt' | wc -l | tr -d ' ')"
}

case "$CMD" in
  bootstrap) bootstrap ;;
  admit) admit ;;
  register) register ;;
  authorize) authorize ;;
  heartbeat) heartbeat ;;
  complete) complete ;;
  abort) abort_run ;;
  status) status_cmd ;;
  *)
    echo "USAGE: $0 ROOT {bootstrap HEAD MODEL EVIDENCE_RECEIPT|admit GATE TASK RECEIPT_LABEL RECEIPT_PATH|register REQUEST_FILE|authorize RUN_ID OP|heartbeat RUN_ID|complete COMPLETION_FILE|abort RUN_ID REASON|status}"
    exit 2
    ;;
esac
