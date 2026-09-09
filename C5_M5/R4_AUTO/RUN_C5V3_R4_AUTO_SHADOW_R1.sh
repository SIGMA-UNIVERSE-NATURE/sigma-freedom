#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
CMD="${2:-status}"
ARG1="${3:-}"
ARG2="${4:-}"
AUTO_ROOT="$ROOT/.sigma_c5v3_auto"
CORE_BIN="$ROOT/.sigma_c5v3_sync/C5V3_R4_AUTO_CORE_R1/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
CORE_SRC="$ROOT/.sigma_c5v3_sync/C5V3_R4_AUTO_CORE_R1/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
EXPECTED_CORE_BIN="c9492320f21e22a30372949307e753ec362f62301ddfce35254ea1493f6029e6"
EXPECTED_CORE_SRC="531ebcc9e692a35d7ec31076bfc7889dd8ce2355cd7f327aad9e5a37045f9af1"
EXPECTED_VM="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_LIVE_CORE="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"
POLL_SECONDS="${SIGMA_AUTO_POLL_SECONDS:-2}"
TRANSPORT_HOOK="${SIGMA_AUTO_TRANSPORT_HOOK:-$AUTO_ROOT/control/transport_exact_request.sh}"

sha(){ sha256sum "$1" | awk '{print $1}'; }
need_file(){ [ -f "$1" ] || { echo "HOLD=MISSING_FILE:$1"; exit 1; }; }
hex64(){ [[ "$1" =~ ^[0-9a-fA-F]{64}$ ]]; }
writev(){ mkdir -p "$(dirname "$1")"; printf '%s' "$2" > "$1"; }
readv(){ [ -f "$1" ] && cat "$1" || true; }

ensure_layout(){
  mkdir -p \
    "$AUTO_ROOT/control" \
    "$AUTO_ROOT/state/objects" \
    "$AUTO_ROOT/chain" \
    "$AUTO_ROOT/invocations" \
    "$AUTO_ROOT/inbox/learning" \
    "$AUTO_ROOT/inbox/evidence" \
    "$AUTO_ROOT/inbox/processed" \
    "$AUTO_ROOT/inbox/failed" \
    "$AUTO_ROOT/outbound/requests" \
    "$AUTO_ROOT/work" \
    "$AUTO_ROOT/memory" \
    "$AUTO_ROOT/restarts" \
    "$AUTO_ROOT/logs"
}

lock_exact(){
  local p="$1" e="$2" n="$3" a
  need_file "$p"
  a="$(sha "$p")"
  [ "$a" = "$e" ] || { echo "HOLD=${n}_IDENTITY"; echo "${n}_SHA256=$a"; exit 1; }
}

verify_fixed_inputs(){
  lock_exact "$CORE_BIN" "$EXPECTED_CORE_BIN" AUTO_CORE_BYTECODE
  lock_exact "$CORE_SRC" "$EXPECTED_CORE_SRC" AUTO_CORE_SOURCE
  lock_exact "$LIVE_CORE" "$EXPECTED_LIVE_CORE" LIVE_CORE
  lock_exact "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" LIVE_RUNNER
}

find_vm(){
  local f
  VM=""
  if [ -n "${SIGMA_VM_BIN:-}" ]; then
    need_file "$SIGMA_VM_BIN"
    [ "$(sha "$SIGMA_VM_BIN")" = "$EXPECTED_VM" ] || { echo "HOLD=SIGMA_VM_BIN_IDENTITY"; exit 1; }
    VM="$SIGMA_VM_BIN"
    return 0
  fi
  for f in "$ROOT/native/vm" "$ROOT/native/sigma_vm" "$ROOT/native/sigma-vm"; do
    if [ -f "$f" ] && [ "$(sha "$f")" = "$EXPECTED_VM" ]; then VM="$f"; return 0; fi
  done
  while IFS= read -r f; do
    if [ -f "$f" ] && [ "$(sha "$f")" = "$EXPECTED_VM" ]; then VM="$f"; return 0; fi
  done < <(find "$ROOT/native" -maxdepth 2 -type f 2>/dev/null | sort)
  echo "HOLD=EXACT_VM_NOT_FOUND"
  exit 1
}

state_get_file(){
  local f="$1" k="$2"
  awk -v key="$k" 'index($0,key"=")==1 { n++; print substr($0,length(key)+2) } END { if(n!=1) exit 1 }' "$f"
}

current_state_check(){
  need_file "$AUTO_ROOT/state/current.txt"
  need_file "$AUTO_ROOT/state/current.sha256"
  local declared actual
  declared="$(cat "$AUTO_ROOT/state/current.sha256")"
  actual="$(sha "$AUTO_ROOT/state/current.txt")"
  [ "$declared" = "$actual" ] || { echo "HOLD=CURRENT_STATE_SHA_MISMATCH"; exit 1; }
  [ -f "$AUTO_ROOT/state/objects/$actual.txt" ] || { echo "HOLD=CURRENT_STATE_OBJECT_MISSING"; exit 1; }
  [ "$(sha "$AUTO_ROOT/state/objects/$actual.txt")" = "$actual" ] || { echo "HOLD=CURRENT_STATE_OBJECT_CORRUPT"; exit 1; }
  CURRENT_SHA="$actual"
  CURRENT_PHASE="$(state_get_file "$AUTO_ROOT/state/current.txt" PHASE)"
}

new_invocation_id(){
  printf 'AUTO_%s_%s_%s' "$(date +%Y%m%dT%H%M%S)" "$$" "$RANDOM"
}

event_kind(){
  case "$1" in
    BOOTSTRAP) echo GENESIS ;;
    TICK) echo TICK ;;
    LEARNING_INPUT_READY) echo LEARNING_INPUT ;;
    REQUEST_BOUND) echo REQUEST_BIND ;;
    EVIDENCE_READY) echo EVIDENCE ;;
    MEMORY_BOUND) echo MEMORY_BIND ;;
    RESTART_READY) echo RESTART ;;
    CAPABILITY_RESULT_READY) echo CAPABILITY_RESULT ;;
    *) echo "" ;;
  esac
}

reset_event_fields(){
  R_ARTIFACT_SHA="NONE"
  R_SUBJECT_ID="NONE"
  R_REQUEST_ID="NONE"
  R_SOURCE_ID="NONE"
  R_SOURCE_VERSION_SHA="NONE"
  R_EVIDENCE_ID="NONE"
  R_REQUEST_ARTIFACT_SHA="NONE"
  R_EPISTEMIC_STATE_SHA="NONE"
  INPUT_PAYLOAD_SHA=""
  BOUND_REQUEST_ARTIFACT_SHA=""
  BOUND_EPISTEMIC_STATE_SHA=""
  BOUND_MEMORY_SHA=""
}

init_io_defaults(){
  local io="$1" f
  for f in \
    invocation_id fresh_root_marker event_type expected_phase authoritative_state_chain_head parent_state_sha parent_state_snapshot_sha parent_state_snapshot \
    receipt_sha receipt_kind receipt_invocation_id receipt_event_type receipt_phase receipt_parent_state_sha receipt_action_id receipt_artifact_sha receipt_subject_id receipt_request_id receipt_source_id receipt_source_version_sha receipt_evidence_id receipt_request_artifact_sha receipt_epistemic_state_sha \
    action_id input_payload_sha bound_request_artifact_sha bound_epistemic_state_sha bound_memory_sha \
    subject_id candidate_a candidate_b neutral_ledger revision_ledger seed_objective seed_gap seed_claim_a seed_claim_b memory_text recall_claim_id recall_gap_id; do
    : > "$io/$f.txt"
  done
}

copy_overlay(){
  local src="$1" io="$2" f
  [ -n "$src" ] || return 0
  [ -d "$src" ] || { echo "HOLD=OVERLAY_NOT_DIRECTORY:$src"; exit 1; }
  for f in subject_id candidate_a candidate_b neutral_ledger revision_ledger seed_objective seed_gap seed_claim_a seed_claim_b memory_text recall_claim_id recall_gap_id; do
    [ -f "$src/$f.txt" ] && cp "$src/$f.txt" "$io/$f.txt"
  done
}

acquire_lock(){
  if ! mkdir "$AUTO_ROOT/.commit_lock" 2>/dev/null; then echo "HOLD=AUTO_COMMIT_LOCK_BUSY"; exit 1; fi
}
release_lock(){ rmdir "$AUTO_ROOT/.commit_lock" 2>/dev/null || true; }

commit_staged_state(){
  local invroot="$1" parent="$2" receipt="$3" event="$4" action="$5" status="$6"
  local out="$invroot/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING/out"
  [ "$(readv "$out/native_commit_intent.txt")" = "ALLOW_EXACT_STAGED_STATE" ] || return 1
  need_file "$out/stage_next_state.txt"
  [ "$(readv "$out/commit_parent_state_sha.txt")" = "$parent" ] || { echo "HOLD=COMMIT_PARENT_MISMATCH"; exit 1; }
  [ "$(readv "$out/commit_receipt_sha.txt")" = "$receipt" ] || { echo "HOLD=COMMIT_RECEIPT_MISMATCH"; exit 1; }
  [ "$(wc -l < "$out/stage_next_state.txt")" -ge 19 ] || { echo "HOLD=STAGED_STATE_TOO_SHORT"; exit 1; }
  [ "$(state_get_file "$out/stage_next_state.txt" STATE_VERSION)" = "2" ] || { echo "HOLD=STAGED_STATE_VERSION"; exit 1; }
  local newsha tmp chain_tmp
  newsha="$(sha "$out/stage_next_state.txt")"
  acquire_lock
  if [ "$parent" != "GENESIS" ]; then
    current_state_check
    [ "$CURRENT_SHA" = "$parent" ] || { release_lock; echo "HOLD=STATE_CAS_FAILED"; exit 1; }
  else
    [ ! -f "$AUTO_ROOT/state/current.txt" ] || { release_lock; echo "HOLD=GENESIS_WITH_EXISTING_STATE"; exit 1; }
  fi
  if [ -f "$AUTO_ROOT/state/objects/$newsha.txt" ]; then
    [ "$(sha "$AUTO_ROOT/state/objects/$newsha.txt")" = "$newsha" ] || { release_lock; echo "HOLD=STATE_OBJECT_COLLISION"; exit 1; }
  else
    tmp="$AUTO_ROOT/state/objects/.${newsha}.$$.tmp"
    cp "$out/stage_next_state.txt" "$tmp"
    [ "$(sha "$tmp")" = "$newsha" ] || { rm -f "$tmp"; release_lock; echo "HOLD=STATE_STAGE_READBACK"; exit 1; }
    mv "$tmp" "$AUTO_ROOT/state/objects/$newsha.txt"
  fi
  tmp="$AUTO_ROOT/state/.current.$$.tmp"
  cp "$AUTO_ROOT/state/objects/$newsha.txt" "$tmp"
  mv "$tmp" "$AUTO_ROOT/state/current.txt"
  tmp="$AUTO_ROOT/state/.current_sha.$$.tmp"
  printf '%s' "$newsha" > "$tmp"
  mv "$tmp" "$AUTO_ROOT/state/current.sha256"
  chain_tmp="$AUTO_ROOT/chain/.${newsha}.$$.tmp"
  {
    printf 'INVOCATION_ID=%s\n' "$(basename "$invroot")"
    printf 'EVENT=%s\n' "$event"
    printf 'PARENT_STATE_SHA=%s\n' "$parent"
    printf 'RECEIPT_SHA=%s\n' "$receipt"
    printf 'ACTION=%s\n' "$action"
    printf 'STATUS=%s\n' "$status"
    printf 'NEXT_STATE_SHA=%s\n' "$newsha"
  } > "$chain_tmp"
  mv "$chain_tmp" "$AUTO_ROOT/chain/${newsha}.$(basename "$invroot").txt"
  release_lock
  LAST_COMMITTED_SHA="$newsha"
  return 0
}

invoke_event(){
  local event="$1" expected_phase="$2" action_id="$3" overlay="${4:-}"
  local kind inv invroot base io out parent snapshot receipt_manifest receipt rc
  kind="$(event_kind "$event")"
  [ -n "$kind" ] || { echo "HOLD=UNKNOWN_EVENT:$event"; exit 1; }
  inv="$(new_invocation_id)"
  invroot="$AUTO_ROOT/invocations/$inv"
  base="$invroot/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
  io="$base/io"
  out="$base/out"
  mkdir -p "$io" "$out"
  init_io_defaults "$io"
  if [ "$event" = "BOOTSTRAP" ]; then
    parent="GENESIS"
    snapshot=""
    writev "$io/authoritative_state_chain_head.txt" GENESIS
    writev "$io/parent_state_sha.txt" GENESIS
    writev "$io/parent_state_snapshot_sha.txt" GENESIS
    : > "$io/parent_state_snapshot.txt"
  else
    current_state_check
    parent="$CURRENT_SHA"
    snapshot="$AUTO_ROOT/state/current.txt"
    [ "$CURRENT_PHASE" = "$expected_phase" ] || { echo "HOLD=PHASE_EXPECTED_${expected_phase}_ACTUAL_${CURRENT_PHASE}"; exit 1; }
    writev "$io/authoritative_state_chain_head.txt" "$parent"
    writev "$io/parent_state_sha.txt" "$parent"
    writev "$io/parent_state_snapshot_sha.txt" "$parent"
    cp "$snapshot" "$io/parent_state_snapshot.txt"
  fi
  writev "$io/invocation_id.txt" "$inv"
  writev "$io/fresh_root_marker.txt" "$inv"
  writev "$io/event_type.txt" "$event"
  writev "$io/expected_phase.txt" "$expected_phase"
  writev "$io/action_id.txt" "$action_id"
  writev "$io/input_payload_sha.txt" "$INPUT_PAYLOAD_SHA"
  writev "$io/bound_request_artifact_sha.txt" "$BOUND_REQUEST_ARTIFACT_SHA"
  writev "$io/bound_epistemic_state_sha.txt" "$BOUND_EPISTEMIC_STATE_SHA"
  writev "$io/bound_memory_sha.txt" "$BOUND_MEMORY_SHA"
  copy_overlay "$overlay" "$io"
  writev "$io/receipt_kind.txt" "$kind"
  writev "$io/receipt_invocation_id.txt" "$inv"
  writev "$io/receipt_event_type.txt" "$event"
  writev "$io/receipt_phase.txt" "$expected_phase"
  writev "$io/receipt_parent_state_sha.txt" "$parent"
  writev "$io/receipt_action_id.txt" "$action_id"
  writev "$io/receipt_artifact_sha.txt" "$R_ARTIFACT_SHA"
  writev "$io/receipt_subject_id.txt" "$R_SUBJECT_ID"
  writev "$io/receipt_request_id.txt" "$R_REQUEST_ID"
  writev "$io/receipt_source_id.txt" "$R_SOURCE_ID"
  writev "$io/receipt_source_version_sha.txt" "$R_SOURCE_VERSION_SHA"
  writev "$io/receipt_evidence_id.txt" "$R_EVIDENCE_ID"
  writev "$io/receipt_request_artifact_sha.txt" "$R_REQUEST_ARTIFACT_SHA"
  writev "$io/receipt_epistemic_state_sha.txt" "$R_EPISTEMIC_STATE_SHA"
  receipt_manifest="$invroot/receipt.manifest"
  {
    printf 'KIND=%s\n' "$kind"
    printf 'INVOCATION_ID=%s\n' "$inv"
    printf 'EVENT=%s\n' "$event"
    printf 'PHASE=%s\n' "$expected_phase"
    printf 'PARENT_STATE_SHA=%s\n' "$parent"
    printf 'ACTION_ID=%s\n' "$action_id"
    printf 'ARTIFACT_SHA=%s\n' "$R_ARTIFACT_SHA"
    printf 'SUBJECT_ID=%s\n' "$R_SUBJECT_ID"
    printf 'REQUEST_ID=%s\n' "$R_REQUEST_ID"
    printf 'SOURCE_ID=%s\n' "$R_SOURCE_ID"
    printf 'SOURCE_VERSION_SHA=%s\n' "$R_SOURCE_VERSION_SHA"
    printf 'EVIDENCE_ID=%s\n' "$R_EVIDENCE_ID"
    printf 'REQUEST_ARTIFACT_SHA=%s\n' "$R_REQUEST_ARTIFACT_SHA"
    printf 'EPISTEMIC_STATE_SHA=%s\n' "$R_EPISTEMIC_STATE_SHA"
  } > "$receipt_manifest"
  receipt="$(sha "$receipt_manifest")"
  writev "$io/receipt_sha.txt" "$receipt"
  set +e
  ( cd "$invroot" && "$VM" "$CORE_BIN" ) > "$invroot/vm.stdout" 2> "$invroot/vm.stderr"
  rc=$?
  set -e
  echo "AUTO_EVENT=$event"
  echo "AUTO_INVOCATION_ID=$inv"
  echo "AUTO_VM_RC=$rc"
  if [ "$rc" -ne 0 ]; then
    [ -s "$invroot/vm.stderr" ] && sed 's/^/AUTO_VM_STDERR=/' "$invroot/vm.stderr"
    echo "HOLD=AUTO_VM_NONZERO"
    exit 1
  fi
  LAST_INV_ROOT="$invroot"
  LAST_ACTION="$(readv "$out/action.txt")"
  LAST_STATUS="$(readv "$out/status.txt")"
  LAST_RECEIPT_SHA="$receipt"
  LAST_COMMITTED_SHA="NONE"
  echo "AUTO_ACTION=$LAST_ACTION"
  echo "AUTO_STATUS=$LAST_STATUS"
  if commit_staged_state "$invroot" "$parent" "$receipt" "$event" "$LAST_ACTION" "$LAST_STATUS"; then
    echo "AUTO_STATE_COMMIT=PASS"
    echo "AUTO_NEXT_STATE_SHA=$LAST_COMMITTED_SHA"
  else
    echo "AUTO_STATE_COMMIT=NO_INTENT"
  fi
  writev "$AUTO_ROOT/logs/last_invocation.txt" "$invroot"
  writev "$AUTO_ROOT/logs/last_action.txt" "$LAST_ACTION"
  writev "$AUTO_ROOT/logs/last_status.txt" "$LAST_STATUS"
}

bootstrap(){
  [ ! -f "$AUTO_ROOT/state/current.txt" ] || { current_state_check; echo "AUTO_INIT=ALREADY_INITIALIZED"; echo "AUTO_PHASE=$CURRENT_PHASE"; return 0; }
  reset_event_fields
  invoke_event BOOTSTRAP GENESIS NONE ""
  current_state_check
  [ "$CURRENT_PHASE" = IDLE ] || { echo "HOLD=BOOTSTRAP_NOT_IDLE"; exit 1; }
  echo "AUTO_INIT=PASS"
}

input_manifest_sha(){
  local d="$1" m="$2" f
  : > "$m"
  for f in subject_id candidate_a candidate_b neutral_ledger revision_ledger; do
    need_file "$d/$f.txt"
    printf '%s  %s.txt\n' "$(sha "$d/$f.txt")" "$f" >> "$m"
  done
  sha "$m"
}

submit_input(){
  local src="$1" id tmp dst f
  [ -d "$src" ] || { echo "HOLD=INPUT_SOURCE_DIR_MISSING"; exit 1; }
  for f in subject_id candidate_a candidate_b neutral_ledger; do need_file "$src/$f.txt"; done
  id="IN_$(date +%Y%m%dT%H%M%S)_$RANDOM"
  tmp="$AUTO_ROOT/inbox/learning/.${id}.tmp"
  dst="$AUTO_ROOT/inbox/learning/${id}.ready"
  mkdir -p "$tmp"
  for f in subject_id candidate_a candidate_b neutral_ledger; do cp "$src/$f.txt" "$tmp/$f.txt"; done
  if [ -f "$src/revision_ledger.txt" ]; then cp "$src/revision_ledger.txt" "$tmp/revision_ledger.txt"; else : > "$tmp/revision_ledger.txt"; fi
  mv "$tmp" "$dst"
  echo "AUTO_INPUT_QUEUED=$dst"
}

persist_work_from_input(){
  local inputdir="$1" work_id="$2" invroot="$3" wtmp="$AUTO_ROOT/work/.${work_id}.$$.tmp" w="$AUTO_ROOT/work/$work_id" f
  [ ! -e "$w" ] || { echo "HOLD=WORK_ALREADY_EXISTS:$work_id"; exit 1; }
  mkdir -p "$wtmp/input" "$wtmp/native_seed" "$wtmp/revisions"
  for f in subject_id candidate_a candidate_b neutral_ledger revision_ledger; do cp "$inputdir/$f.txt" "$wtmp/input/$f.txt"; done
  for f in native_objective native_gap native_claim_a native_claim_b native_request_payload native_epistemic_seed; do
    need_file "$invroot/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING/out/$f.txt"
    cp "$invroot/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING/out/$f.txt" "$wtmp/native_seed/$f.txt"
  done
  writev "$wtmp/input_event_invocation.txt" "$(basename "$invroot")"
  mv "$wtmp" "$w"
}

bind_request(){
  current_state_check
  [ "$CURRENT_PHASE" = WAIT_REQUEST_BIND ] || { echo "HOLD=REQUEST_BIND_WRONG_PHASE:$CURRENT_PHASE"; exit 1; }
  local state="$AUTO_ROOT/state/current.txt" work_id req subject action work payload seed reqsha seedsha outtmp outdir
  work_id="$(state_get_file "$state" OBJECTIVE_ID)"
  req="$(state_get_file "$state" PENDING_REQUEST_ID)"
  subject="$(state_get_file "$state" PENDING_SUBJECT_ID)"
  action="$(state_get_file "$state" PENDING_ACTION_ID)"
  work="$AUTO_ROOT/work/$work_id"
  payload="$work/native_seed/native_request_payload.txt"
  seed="$work/native_seed/native_epistemic_seed.txt"
  need_file "$payload"; need_file "$seed"
  reqsha="$(sha "$payload")"; seedsha="$(sha "$seed")"
  outdir="$AUTO_ROOT/outbound/requests/$req"
  if [ ! -d "$outdir" ]; then
    outtmp="$AUTO_ROOT/outbound/requests/.${req}.$$.tmp"
    mkdir -p "$outtmp"
    cp "$payload" "$outtmp/payload.txt"
    cp "$seed" "$outtmp/epistemic_seed.txt"
    writev "$outtmp/request_id.txt" "$req"
    writev "$outtmp/subject_id.txt" "$subject"
    writev "$outtmp/action_id.txt" "$action"
    writev "$outtmp/request_artifact_sha256.txt" "$reqsha"
    writev "$outtmp/epistemic_state_sha256.txt" "$seedsha"
    mv "$outtmp" "$outdir"
  fi
  reset_event_fields
  R_ARTIFACT_SHA="$reqsha"
  R_SUBJECT_ID="$subject"
  R_REQUEST_ID="$req"
  R_REQUEST_ARTIFACT_SHA="$reqsha"
  R_EPISTEMIC_STATE_SHA="$seedsha"
  BOUND_REQUEST_ARTIFACT_SHA="$reqsha"
  BOUND_EPISTEMIC_STATE_SHA="$seedsha"
  invoke_event REQUEST_BOUND WAIT_REQUEST_BIND "$action" ""
  current_state_check
  [ "$CURRENT_PHASE" = WAIT_EVIDENCE ] || { echo "HOLD=REQUEST_BOUND_NOT_WAIT_EVIDENCE"; exit 1; }
  echo "AUTO_OUTBOUND_REQUEST=$outdir"
  if [ -x "$TRANSPORT_HOOK" ]; then
    "$TRANSPORT_HOOK" "$outdir" "$AUTO_ROOT/inbox/evidence" "$req"
    echo "AUTO_TRANSPORT_HOOK=INVOKED"
  else
    echo "AUTO_TRANSPORT_HOOK=NOT_INSTALLED"
  fi
}

process_input(){
  local d="$1" manifest inputsha subject phase work_id processed
  current_state_check
  [ "$CURRENT_PHASE" = IDLE ] || { echo "HOLD=INPUT_WRONG_PHASE:$CURRENT_PHASE"; exit 1; }
  manifest="$d/input.manifest"
  inputsha="$(input_manifest_sha "$d" "$manifest")"
  subject="$(cat "$d/subject_id.txt")"
  reset_event_fields
  R_ARTIFACT_SHA="$inputsha"
  R_SUBJECT_ID="$subject"
  INPUT_PAYLOAD_SHA="$inputsha"
  invoke_event LEARNING_INPUT_READY IDLE NONE "$d"
  if [ "$LAST_COMMITTED_SHA" != NONE ]; then
    current_state_check
    if [ "$CURRENT_PHASE" = WAIT_REQUEST_BIND ]; then
      work_id="$(state_get_file "$AUTO_ROOT/state/current.txt" OBJECTIVE_ID)"
      persist_work_from_input "$d" "$work_id" "$LAST_INV_ROOT"
      processed="$AUTO_ROOT/inbox/processed/$(basename "$d").input"
      mv "$d" "$processed"
      bind_request
      return 0
    fi
  fi
  processed="$AUTO_ROOT/inbox/processed/$(basename "$d").no_commit"
  mv "$d" "$processed"
  echo "AUTO_INPUT_RESULT=$LAST_STATUS"
}

submit_evidence(){
  local req="$1" src="$2" tmp dst f asserted actual
  [ -n "$req" ] || { echo "HOLD=REQUEST_ID_REQUIRED"; exit 1; }
  [ -d "$src" ] || { echo "HOLD=EVIDENCE_SOURCE_DIR_MISSING"; exit 1; }
  for f in subject_id source_id source_version_sha evidence_id revision_ledger; do need_file "$src/$f.txt"; done
  need_file "$src/artifact.bin"
  hex64 "$(cat "$src/source_version_sha.txt")" || { echo "HOLD=SOURCE_VERSION_SHA_NOT_HEX64"; exit 1; }
  actual="$(sha "$src/artifact.bin")"
  if [ -f "$src/artifact_sha256.txt" ]; then
    asserted="$(cat "$src/artifact_sha256.txt")"
    [ "$asserted" = "$actual" ] || { echo "HOLD=EVIDENCE_ARTIFACT_SHA_MISMATCH"; exit 1; }
  fi
  tmp="$AUTO_ROOT/inbox/evidence/.${req}.$$.tmp"
  dst="$AUTO_ROOT/inbox/evidence/${req}.ready"
  [ ! -e "$dst" ] || { echo "HOLD=EVIDENCE_ALREADY_QUEUED:$req"; exit 1; }
  mkdir -p "$tmp"
  cp "$src/artifact.bin" "$tmp/artifact.bin"
  for f in subject_id source_id source_version_sha evidence_id revision_ledger; do cp "$src/$f.txt" "$tmp/$f.txt"; done
  writev "$tmp/artifact_sha256.txt" "$actual"
  mv "$tmp" "$dst"
  echo "AUTO_EVIDENCE_QUEUED=$dst"
}

persist_revision_outputs(){
  local work="$1" invroot="$2" revdir="$work/revisions/$(basename "$invroot")" f
  mkdir -p "$revdir"
  for f in source_stance evidence_ref evaluation_a evaluation_b truth_posture revised_claim_a revised_claim_b next_relation_gap conflict_gap native_compact_memory; do
    if [ -f "$invroot/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING/out/$f.txt" ]; then
      cp "$invroot/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING/out/$f.txt" "$revdir/$f.txt"
    fi
  done
  writev "$work/latest_revision_dir.txt" "$revdir"
}

bind_memory(){
  local work="$1" memory="$2" memsha="$3" state subject action req
  current_state_check
  [ "$CURRENT_PHASE" = WAIT_MEMORY_BIND ] || { echo "HOLD=MEMORY_BIND_WRONG_PHASE:$CURRENT_PHASE"; exit 1; }
  state="$AUTO_ROOT/state/current.txt"
  subject="$(state_get_file "$state" PENDING_SUBJECT_ID)"
  action="$(state_get_file "$state" PENDING_ACTION_ID)"
  req="$(state_get_file "$state" PENDING_REQUEST_ID)"
  reset_event_fields
  R_ARTIFACT_SHA="$memsha"
  R_SUBJECT_ID="$subject"
  R_REQUEST_ID="$req"
  BOUND_MEMORY_SHA="$memsha"
  invoke_event MEMORY_BOUND WAIT_MEMORY_BIND "$action" ""
  current_state_check
  [ "$CURRENT_PHASE" = IDLE ] || { echo "HOLD=MEMORY_BOUND_NOT_IDLE"; exit 1; }
  writev "$work/completed_memory_sha256.txt" "$memsha"
  writev "$work/completed_state_sha256.txt" "$CURRENT_SHA"
  echo "AUTO_LEARNING_CYCLE=COMPLETE"
  echo "AUTO_MEMORY_SHA256=$memsha"
}

process_evidence(){
  local d="$1" state req subject action work_id work artsha source sourcever evid overlay mem memsha memobj processed
  current_state_check
  [ "$CURRENT_PHASE" = WAIT_EVIDENCE ] || { echo "HOLD=EVIDENCE_WRONG_PHASE:$CURRENT_PHASE"; exit 1; }
  state="$AUTO_ROOT/state/current.txt"
  req="$(state_get_file "$state" PENDING_REQUEST_ID)"
  [ "$(basename "$d")" = "${req}.ready" ] || { echo "HOLD=EVIDENCE_REQUEST_DIRECTORY_MISMATCH"; exit 1; }
  subject="$(state_get_file "$state" PENDING_SUBJECT_ID)"
  [ "$(cat "$d/subject_id.txt")" = "$subject" ] || { echo "HOLD=EVIDENCE_SUBJECT_MISMATCH"; exit 1; }
  action="$(state_get_file "$state" PENDING_ACTION_ID)"
  work_id="$(state_get_file "$state" OBJECTIVE_ID)"
  work="$AUTO_ROOT/work/$work_id"
  [ -d "$work" ] || { echo "HOLD=WORK_MISSING:$work_id"; exit 1; }
  artsha="$(sha "$d/artifact.bin")"
  [ "$(cat "$d/artifact_sha256.txt")" = "$artsha" ] || { echo "HOLD=EVIDENCE_ARTIFACT_READBACK"; exit 1; }
  source="$(cat "$d/source_id.txt")"
  sourcever="$(cat "$d/source_version_sha.txt")"
  evid="$(cat "$d/evidence_id.txt")"
  hex64 "$sourcever" || { echo "HOLD=SOURCE_VERSION_SHA_NOT_HEX64"; exit 1; }
  overlay="$AUTO_ROOT/work/.overlay.${work_id}.$$.tmp"
  mkdir -p "$overlay"
  cp "$work/input/subject_id.txt" "$overlay/subject_id.txt"
  cp "$work/input/candidate_a.txt" "$overlay/candidate_a.txt"
  cp "$work/input/candidate_b.txt" "$overlay/candidate_b.txt"
  cp "$work/input/neutral_ledger.txt" "$overlay/neutral_ledger.txt"
  cp "$d/revision_ledger.txt" "$overlay/revision_ledger.txt"
  cp "$work/native_seed/native_objective.txt" "$overlay/seed_objective.txt"
  cp "$work/native_seed/native_gap.txt" "$overlay/seed_gap.txt"
  cp "$work/native_seed/native_claim_a.txt" "$overlay/seed_claim_a.txt"
  cp "$work/native_seed/native_claim_b.txt" "$overlay/seed_claim_b.txt"
  reset_event_fields
  R_ARTIFACT_SHA="$artsha"
  R_SUBJECT_ID="$subject"
  R_REQUEST_ID="$req"
  R_SOURCE_ID="$source"
  R_SOURCE_VERSION_SHA="$sourcever"
  R_EVIDENCE_ID="$evid"
  R_REQUEST_ARTIFACT_SHA="$(state_get_file "$state" PENDING_PAYLOAD_SHA)"
  R_EPISTEMIC_STATE_SHA="$(state_get_file "$state" EPISTEMIC_STATE_SHA)"
  invoke_event EVIDENCE_READY WAIT_EVIDENCE "$action" "$overlay"
  rm -rf "$overlay"
  current_state_check
  [ "$CURRENT_PHASE" = WAIT_MEMORY_BIND ] || { echo "HOLD=EVIDENCE_NOT_WAIT_MEMORY_BIND"; exit 1; }
  persist_revision_outputs "$work" "$LAST_INV_ROOT"
  mem="$LAST_INV_ROOT/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING/out/native_compact_memory.txt"
  need_file "$mem"
  memsha="$(sha "$mem")"
  memobj="$AUTO_ROOT/memory/$memsha.txt"
  if [ -f "$memobj" ]; then
    [ "$(sha "$memobj")" = "$memsha" ] || { echo "HOLD=MEMORY_OBJECT_COLLISION"; exit 1; }
  else
    cp "$mem" "$memobj"
    [ "$(sha "$memobj")" = "$memsha" ] || { echo "HOLD=MEMORY_READBACK"; exit 1; }
  fi
  writev "$work/pending_memory_sha256.txt" "$memsha"
  bind_memory "$work" "$memobj" "$memsha"
  processed="$AUTO_ROOT/inbox/processed/$(basename "$d").evidence"
  mv "$d" "$processed"
}

restart_memory(){
  local claim="$1" gap="$2" state memsha mem overlay outdir
  current_state_check
  [ "$CURRENT_PHASE" = IDLE ] || { echo "HOLD=RESTART_WRONG_PHASE:$CURRENT_PHASE"; exit 1; }
  state="$AUTO_ROOT/state/current.txt"
  memsha="$(state_get_file "$state" MEMORY_STATE_SHA)"
  hex64 "$memsha" || { echo "HOLD=NO_DURABLE_MEMORY_FOR_RESTART"; exit 1; }
  mem="$AUTO_ROOT/memory/$memsha.txt"
  need_file "$mem"
  overlay="$AUTO_ROOT/restarts/.overlay.$$.tmp"
  mkdir -p "$overlay"
  cp "$mem" "$overlay/memory_text.txt"
  writev "$overlay/recall_claim_id.txt" "$claim"
  writev "$overlay/recall_gap_id.txt" "$gap"
  reset_event_fields
  R_ARTIFACT_SHA="$memsha"
  invoke_event RESTART_READY IDLE NONE "$overlay"
  rm -rf "$overlay"
  if [ "$LAST_COMMITTED_SHA" = NONE ]; then echo "HOLD=RESTART_NO_COMMIT"; exit 1; fi
  outdir="$AUTO_ROOT/restarts/$(basename "$LAST_INV_ROOT")"
  mkdir -p "$outdir"
  for f in recalled_claim recalled_gap recalled_evaluations recalled_evidence_posture; do
    [ -f "$LAST_INV_ROOT/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING/out/$f.txt" ] && cp "$LAST_INV_ROOT/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING/out/$f.txt" "$outdir/$f.txt"
  done
  echo "AUTO_RESTART_REUSE=PASS_PATH"
  echo "AUTO_RESTART_OUTPUT=$outdir"
}

recover_memory_bind(){
  current_state_check
  local work_id work memsha mem
  work_id="$(state_get_file "$AUTO_ROOT/state/current.txt" OBJECTIVE_ID)"
  work="$AUTO_ROOT/work/$work_id"
  need_file "$work/pending_memory_sha256.txt"
  memsha="$(cat "$work/pending_memory_sha256.txt")"
  mem="$AUTO_ROOT/memory/$memsha.txt"
  need_file "$mem"
  bind_memory "$work" "$mem" "$memsha"
}

once_impl(){
  if [ ! -f "$AUTO_ROOT/state/current.txt" ]; then bootstrap; return 0; fi
  current_state_check
  case "$CURRENT_PHASE" in
    IDLE)
      local q
      q="$(find "$AUTO_ROOT/inbox/learning" -maxdepth 1 -type d -name '*.ready' 2>/dev/null | sort | head -n 1 || true)"
      if [ -n "$q" ]; then process_input "$q"; else
        reset_event_fields
        invoke_event TICK IDLE NONE ""
        echo "AUTO_WAIT=NO_INPUT"
      fi
      ;;
    WAIT_REQUEST_BIND) bind_request ;;
    WAIT_EVIDENCE)
      local req ev
      req="$(state_get_file "$AUTO_ROOT/state/current.txt" PENDING_REQUEST_ID)"
      ev="$AUTO_ROOT/inbox/evidence/${req}.ready"
      if [ -d "$ev" ]; then process_evidence "$ev"; else echo "AUTO_WAIT=EVIDENCE"; echo "AUTO_PENDING_REQUEST_ID=$req"; fi
      ;;
    WAIT_MEMORY_BIND) recover_memory_bind ;;
    WAIT_CAPABILITY) echo "AUTO_WAIT=CAPABILITY_PATH_NOT_ACTIVATED" ;;
    *) echo "HOLD=UNKNOWN_PHASE:$CURRENT_PHASE"; exit 1 ;;
  esac
}

status(){
  echo "AUTO_CORE_SOURCE_SHA256=$(sha "$CORE_SRC")"
  echo "AUTO_CORE_BYTECODE_SHA256=$(sha "$CORE_BIN")"
  echo "AUTO_VM_PATH=$VM"
  echo "AUTO_VM_SHA256=$(sha "$VM")"
  if [ -f "$AUTO_ROOT/state/current.txt" ]; then
    current_state_check
    echo "AUTO_INITIALIZED=YES"
    echo "AUTO_STATE_SHA256=$CURRENT_SHA"
    echo "AUTO_PHASE=$CURRENT_PHASE"
    echo "AUTO_OBJECTIVE_ID=$(state_get_file "$AUTO_ROOT/state/current.txt" OBJECTIVE_ID)"
    echo "AUTO_ACTIVE_GAP_ID=$(state_get_file "$AUTO_ROOT/state/current.txt" ACTIVE_GAP_ID)"
    echo "AUTO_PENDING_ACTION_ID=$(state_get_file "$AUTO_ROOT/state/current.txt" PENDING_ACTION_ID)"
    echo "AUTO_PENDING_REQUEST_ID=$(state_get_file "$AUTO_ROOT/state/current.txt" PENDING_REQUEST_ID)"
    echo "AUTO_MEMORY_STATE_SHA=$(state_get_file "$AUTO_ROOT/state/current.txt" MEMORY_STATE_SHA)"
  else
    echo "AUTO_INITIALIZED=NO"
  fi
  echo "AUTO_TRANSPORT_HOOK=$TRANSPORT_HOOK"
  if [ -x "$TRANSPORT_HOOK" ]; then echo "AUTO_TRANSPORT_HOOK_STATE=READY"; else echo "AUTO_TRANSPORT_HOOK_STATE=ABSENT"; fi
  echo "PRODUCTION_BINDING=NO"
  echo "PRODUCTION_MUTATION=NO"
}

ensure_layout
verify_fixed_inputs
find_vm

case "$CMD" in
  init) bootstrap ;;
  once) once_impl ;;
  loop)
    bootstrap
    echo "AUTO_LOOP=START"
    while true; do once_impl; sleep "$POLL_SECONDS"; done
    ;;
  submit-input)
    [ -n "$ARG1" ] || { echo "USAGE: $0 ROOT submit-input INPUT_DIR"; exit 2; }
    submit_input "$ARG1"
    ;;
  submit-evidence)
    [ -n "$ARG1" ] && [ -n "$ARG2" ] || { echo "USAGE: $0 ROOT submit-evidence REQUEST_ID EVIDENCE_DIR"; exit 2; }
    submit_evidence "$ARG1" "$ARG2"
    ;;
  restart)
    [ -n "$ARG1" ] && [ -n "$ARG2" ] || { echo "USAGE: $0 ROOT restart CLAIM_ID GAP_ID"; exit 2; }
    restart_memory "$ARG1" "$ARG2"
    ;;
  status) status ;;
  *) echo "USAGE: $0 ROOT {init|once|loop|submit-input DIR|submit-evidence REQUEST_ID DIR|restart CLAIM_ID GAP_ID|status}"; exit 2 ;;
esac
