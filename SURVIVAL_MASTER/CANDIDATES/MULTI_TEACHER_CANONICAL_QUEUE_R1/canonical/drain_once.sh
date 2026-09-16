#!/usr/bin/env bash
set -euo pipefail
umask 077

hold(){ printf 'HOLD=%s\n' "$1"; exit 2; }
sha(){ sha256sum "$1" | awk '{print $1}'; }
field_text(){ printf '%s\n' "$2" | awk -F= -v K="$1" '$1==K{sub(/^[^=]*=/,"");print;exit}'; }
field_file(){ awk -F= -v K="$1" '$1==K{sub(/^[^=]*=/,"");print;exit}' "$2"; }

ROOT="${ROOT:-$HOME/SIGMA/sigma_genesis1}"
API="$ROOT/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
[ -f "$API" ] || hold SESSION_API_MISSING
# shellcheck disable=SC1090
source "$API"
STATUS="$(sigma-session status 2>/dev/null || true)"
printf '%s\n' "$STATUS"
[ "$(field_text SESSION "$STATUS")" = GRANTED ] || hold SESSION_NOT_GRANTED
[ "$(field_text SESSION_MODE "$STATUS")" = CANONICAL_LEARNER ] || hold CURRENT_SESSION_NOT_CANONICAL_LEARNER
[ "$(field_text ONE_WRITER "$STATUS")" = YES ] || hold ONE_WRITER_NOT_YES
[ "$(field_text HOST_COGNITION "$STATUS")" = NO ] || hold HOST_COGNITION_NOT_NO
[ "$(field_text HOST_LEARNING "$STATUS")" = NO ] || hold HOST_LEARNING_NOT_NO
[ "$(field_text BRAIN_WRITE "$STATUS")" = ALLOW ] || hold BRAIN_WRITE_NOT_ALLOW
[ "$(field_text BRAIN_WRITE_OWNER "$STATUS")" = SIGMA_NATIVE_VM_ONLY ] || hold BRAIN_WRITE_OWNER_INVALID
[ "$(field_text BRAIN_WRITE_NATIVE_RECEIPT_REQUIRED "$STATUS")" = YES ] || hold NATIVE_RECEIPT_NOT_REQUIRED
for K in STATE_WRITE MODEL_WRITE LEARN COMMIT MODEL_GENERATION_CHANGE; do
  [ "$(field_text "$K" "$STATUS")" = ALLOW ] || hold "${K}_NOT_ALLOW"
done
[ "$(field_text HEAD_CHANGE "$STATUS")" = REJECT ] || hold HEAD_CHANGE_MUST_REMAIN_REJECT

SESSION_CODE="$(field_text SESSION_CODE "$STATUS")"
ARTIFACT_ROOT="$(realpath "$(field_text ARTIFACT_ROOT "$STATUS")")"
WORKSPACES="$ROOT/.sigma_ail/coordination/SESSION_R4/WORKSPACES"
BRAIN_HEAD_FILE="$ROOT/.sigma_ail/BRAIN_HEAD"
MODEL_GEN_FILE="$ROOT/.sigma_ail/MODEL_GENERATION"
[ -f "$BRAIN_HEAD_FILE" ] || hold BRAIN_HEAD_MISSING
[ -f "$MODEL_GEN_FILE" ] || hold MODEL_GENERATION_MISSING

STATE_ROOT="$ARTIFACT_ROOT/MULTI_TEACHER_CANONICAL_QUEUE_R1"
mkdir -p "$STATE_ROOT/attempts" "$STATE_ROOT/processed" "$STATE_ROOT/rejected"
exec 9>"$STATE_ROOT/drain.lock"
flock -n 9 || hold CANONICAL_QUEUE_DRAIN_ALREADY_RUNNING

mapfile -t READY_FILES < <(find "$WORKSPACES" -type f -path '*/artifacts/CANONICAL_CANDIDATE_QUEUE_OUTBOX/*/READY' -print 2>/dev/null | sort)
[ "${#READY_FILES[@]}" -gt 0 ] || { echo 'QUEUE_DRAIN=EMPTY'; exit 0; }

for READY in "${READY_FILES[@]}"; do
  PACKET="$(dirname "$READY")"
  CID="$(basename "$PACKET")"
  [ -f "$STATE_ROOT/processed/$CID.receipt" ] && continue
  [ -f "$STATE_ROOT/rejected/$CID.receipt" ] && continue

  DESC="$PACKET/descriptor.env"
  [ -f "$DESC" ] || hold PACKET_DESCRIPTOR_MISSING
  [ -f "$PACKET/MANIFEST.sha256" ] || hold PACKET_MANIFEST_MISSING
  (cd "$PACKET" && sha256sum -c MANIFEST.sha256 >/dev/null) || hold PACKET_MANIFEST_HASH_MISMATCH
  [ "$(sha "$DESC")" = "$CID" ] || hold PACKET_ID_DESCRIPTOR_HASH_MISMATCH
  [ "$(field_file SCHEMA "$DESC")" = SIGMA_MULTI_TEACHER_WEIGHT_CANDIDATE_R1 ] || hold PACKET_SCHEMA_MISMATCH
  [ "$(field_file HOST_COGNITION "$DESC")" = NO ] || hold PACKET_HOST_COGNITION_INVALID
  [ "$(field_file HOST_LEARNING "$DESC")" = NO ] || hold PACKET_HOST_LEARNING_INVALID
  [ "$(field_file SIGMA_NATIVE_LEARNING_OWNER "$DESC")" = YES ] || hold PACKET_NATIVE_OWNER_INVALID

  EVID="$(field_file TEACHING_EVIDENCE_PATH "$DESC")"
  EVID_SHA="$(field_file TEACHING_EVIDENCE_SHA256 "$DESC")"
  ENTRY="$(field_file CANONICAL_REPLAY_ENTRYPOINT "$DESC")"
  ENTRY_SHA="$(field_file CANONICAL_REPLAY_ENTRYPOINT_SHA256 "$DESC")"
  OWN="$(field_file NATIVE_OWNERSHIP_RECEIPT "$DESC")"
  OWN_SHA="$(field_file NATIVE_OWNERSHIP_RECEIPT_SHA256 "$DESC")"
  [ -f "$EVID" ] || hold TEACHING_EVIDENCE_MISSING
  [ -f "$ENTRY" ] || hold CANONICAL_REPLAY_ENTRYPOINT_MISSING
  [ -x "$ENTRY" ] || hold CANONICAL_REPLAY_ENTRYPOINT_NOT_EXECUTABLE
  [ -f "$OWN" ] || hold NATIVE_OWNERSHIP_RECEIPT_MISSING
  [ "$(sha "$EVID")" = "$EVID_SHA" ] || hold TEACHING_EVIDENCE_HASH_MISMATCH
  [ "$(sha "$ENTRY")" = "$ENTRY_SHA" ] || hold CANONICAL_REPLAY_ENTRYPOINT_HASH_MISMATCH
  [ "$(sha "$OWN")" = "$OWN_SHA" ] || hold NATIVE_OWNERSHIP_RECEIPT_HASH_MISMATCH
  grep -Fqx 'SIGMA_NATIVE_LEARNING_OWNER=YES' "$OWN" || hold OWNERSHIP_RECEIPT_NATIVE_OWNER_MISSING
  grep -Fqx 'HOST_COGNITION=NO' "$OWN" || hold OWNERSHIP_RECEIPT_HOST_COGNITION_INVALID
  grep -Fqx 'HOST_LEARNING=NO' "$OWN" || hold OWNERSHIP_RECEIPT_HOST_LEARNING_INVALID
  grep -Fqx 'CANONICAL_REPLAY_SAFE=YES' "$OWN" || hold OWNERSHIP_RECEIPT_REPLAY_SAFE_MISSING

  BEFORE_HEAD="$(cat "$BRAIN_HEAD_FILE")"
  BEFORE_GEN="$(cat "$MODEL_GEN_FILE")"
  ATTEMPT="$STATE_ROOT/attempts/$CID.$(date +%s).$$"
  mkdir -p "$ATTEMPT"
  cp "$DESC" "$ATTEMPT/descriptor.env"
  printf 'CANDIDATE_ID=%s\nBEFORE_HEAD=%s\nBEFORE_MODEL_GENERATION=%s\nCANONICAL_SESSION_CODE=%s\n' \
    "$CID" "$BEFORE_HEAD" "$BEFORE_GEN" "$SESSION_CODE" > "$ATTEMPT/invocation.env"

  export SIGMA_QUEUE_DESCRIPTOR="$DESC"
  export SIGMA_QUEUE_ATTEMPT_ROOT="$ATTEMPT"
  export SIGMA_QUEUE_CURRENT_HEAD="$BEFORE_HEAD"
  export SIGMA_QUEUE_CURRENT_MODEL_GENERATION="$BEFORE_GEN"
  export SIGMA_QUEUE_CANONICAL_SESSION_CODE="$SESSION_CODE"

  set +e
  "$ENTRY" "$DESC" "$ATTEMPT" >"$ATTEMPT/replay.stdout" 2>"$ATTEMPT/replay.stderr"
  RC=$?
  set -e
  printf 'REPLAY_RC=%s\n' "$RC" > "$ATTEMPT/replay.rc"
  sha256sum "$ATTEMPT/replay.stdout" "$ATTEMPT/replay.stderr" "$ATTEMPT/replay.rc" > "$ATTEMPT/replay.hashes"

  RESULT="$ATTEMPT/result.env"
  [ -f "$RESULT" ] || { printf 'QUEUE_DRAIN=HOLD\nCANDIDATE_ID=%s\nREASON=REPLAY_RESULT_MISSING\nATTEMPT=%s\n' "$CID" "$ATTEMPT"; exit 2; }
  [ "$(field_file SCHEMA "$RESULT")" = SIGMA_MULTI_TEACHER_CANONICAL_RESULT_R1 ] || hold RESULT_SCHEMA_MISMATCH
  [ "$(field_file SOURCE_CANDIDATE_ID "$RESULT")" = "$CID" ] || hold RESULT_CANDIDATE_ID_MISMATCH
  [ "$(field_file SIGMA_NATIVE_LEARNING_OWNER "$RESULT")" = YES ] || hold RESULT_NATIVE_OWNER_INVALID
  [ "$(field_file HOST_COGNITION "$RESULT")" = NO ] || hold RESULT_HOST_COGNITION_INVALID
  [ "$(field_file HOST_LEARNING "$RESULT")" = NO ] || hold RESULT_HOST_LEARNING_INVALID
  [ "$(field_file BEFORE_HEAD "$RESULT")" = "$BEFORE_HEAD" ] || hold RESULT_BEFORE_HEAD_MISMATCH
  [ "$(field_file BEFORE_MODEL_GENERATION "$RESULT")" = "$BEFORE_GEN" ] || hold RESULT_BEFORE_GENERATION_MISMATCH

  QRESULT="$(field_file QUEUE_RESULT "$RESULT")"
  AFTER_HEAD="$(cat "$BRAIN_HEAD_FILE")"
  AFTER_GEN="$(cat "$MODEL_GEN_FILE")"

  case "$QRESULT" in
    ACCEPTED)
      [ "$RC" -eq 0 ] || hold ACCEPTED_WITH_NONZERO_REPLAY_RC
      [ "$(field_file CANONICAL_MUTATION_OBSERVED "$RESULT")" = YES ] || hold ACCEPTED_WITHOUT_CANONICAL_MUTATION
      [ "$(field_file AFTER_HEAD "$RESULT")" = "$AFTER_HEAD" ] || hold ACCEPTED_AFTER_HEAD_MISMATCH
      [ "$(field_file AFTER_MODEL_GENERATION "$RESULT")" = "$AFTER_GEN" ] || hold ACCEPTED_AFTER_GENERATION_MISMATCH
      [ "$AFTER_GEN" != "$BEFORE_GEN" ] || hold ACCEPTED_WITHOUT_MODEL_GENERATION_ADVANCE
      RECEIPT="$(field_file NATIVE_COMMIT_RECEIPT_PATH "$RESULT")"
      RECEIPT_SHA="$(field_file NATIVE_COMMIT_RECEIPT_SHA256 "$RESULT")"
      [ -f "$RECEIPT" ] || hold NATIVE_COMMIT_RECEIPT_MISSING
      [ "$(sha "$RECEIPT")" = "$RECEIPT_SHA" ] || hold NATIVE_COMMIT_RECEIPT_HASH_MISMATCH
      {
        echo 'QUEUE_PROCESSED=ACCEPTED'
        echo "CANDIDATE_ID=$CID"
        echo "BEFORE_HEAD=$BEFORE_HEAD"
        echo "BEFORE_MODEL_GENERATION=$BEFORE_GEN"
        echo "AFTER_HEAD=$AFTER_HEAD"
        echo "AFTER_MODEL_GENERATION=$AFTER_GEN"
        echo "NATIVE_COMMIT_RECEIPT_SHA256=$RECEIPT_SHA"
        echo "ATTEMPT=$ATTEMPT"
      } > "$STATE_ROOT/processed/$CID.receipt.partial"
      mv "$STATE_ROOT/processed/$CID.receipt.partial" "$STATE_ROOT/processed/$CID.receipt"
      printf 'QUEUE_DRAIN=ACCEPTED\nCANDIDATE_ID=%s\nAFTER_MODEL_GENERATION=%s\n' "$CID" "$AFTER_GEN"
      exit 0
      ;;
    REJECTED)
      [ "$(field_file CANONICAL_MUTATION_OBSERVED "$RESULT")" = NO ] || hold REJECTED_WITH_CANONICAL_MUTATION
      [ "$AFTER_HEAD" = "$BEFORE_HEAD" ] || hold REJECTED_BUT_HEAD_CHANGED
      [ "$AFTER_GEN" = "$BEFORE_GEN" ] || hold REJECTED_BUT_GENERATION_CHANGED
      {
        echo 'QUEUE_PROCESSED=REJECTED_BY_NATIVE_SIGMA'
        echo "CANDIDATE_ID=$CID"
        echo "HEAD=$BEFORE_HEAD"
        echo "MODEL_GENERATION=$BEFORE_GEN"
        echo "ATTEMPT=$ATTEMPT"
      } > "$STATE_ROOT/rejected/$CID.receipt.partial"
      mv "$STATE_ROOT/rejected/$CID.receipt.partial" "$STATE_ROOT/rejected/$CID.receipt"
      printf 'QUEUE_DRAIN=REJECTED_BY_NATIVE_SIGMA\nCANDIDATE_ID=%s\n' "$CID"
      exit 0
      ;;
    HOLD)
      [ "$(field_file CANONICAL_MUTATION_OBSERVED "$RESULT")" = NO ] || hold HOLD_WITH_CANONICAL_MUTATION
      [ "$AFTER_HEAD" = "$BEFORE_HEAD" ] || hold HOLD_BUT_HEAD_CHANGED
      [ "$AFTER_GEN" = "$BEFORE_GEN" ] || hold HOLD_BUT_GENERATION_CHANGED
      printf 'QUEUE_DRAIN=HOLD\nCANDIDATE_ID=%s\nATTEMPT=%s\n' "$CID" "$ATTEMPT"
      exit 2
      ;;
    *) hold UNKNOWN_QUEUE_RESULT ;;
  esac
done

echo 'QUEUE_DRAIN=NO_UNPROCESSED_PACKET'
