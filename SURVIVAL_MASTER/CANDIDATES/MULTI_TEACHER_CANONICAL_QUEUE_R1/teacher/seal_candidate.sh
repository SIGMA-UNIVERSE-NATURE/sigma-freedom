#!/usr/bin/env bash
set -euo pipefail
umask 077

hold(){ printf 'HOLD=%s\n' "$1"; exit 2; }
sha(){ sha256sum "$1" | awk '{print $1}'; }
field_text(){ printf '%s\n' "$2" | awk -F= -v K="$1" '$1==K{sub(/^[^=]*=/,"");print;exit}'; }
field_file(){ awk -F= -v K="$1" '$1==K{sub(/^[^=]*=/,"");print;exit}' "$2"; }
under(){ case "$1" in "$2"|"$2"/*) return 0;; *) return 1;; esac; }

[ "$#" -eq 1 ] || hold USAGE_SEAL_CANDIDATE_DESCRIPTOR_REQUIRED
DESC="$(realpath "$1")"
[ -f "$DESC" ] || hold DESCRIPTOR_MISSING

ROOT="${ROOT:-$HOME/SIGMA/sigma_genesis1}"
API="$ROOT/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
[ -f "$API" ] || hold SESSION_API_MISSING
# shellcheck disable=SC1090
source "$API"
STATUS="$(sigma-session status 2>/dev/null || true)"
printf '%s\n' "$STATUS"
[ "$(field_text SESSION "$STATUS")" = GRANTED ] || hold SESSION_NOT_GRANTED
[ "$(field_text SESSION_MODE "$STATUS")" = STANDARD ] || hold TEACHER_MUST_BE_STANDARD_SESSION
[ "$(field_text ACCESS "$STATUS")" = READ_PLUS_ARTIFACT_WRITE ] || hold TEACHER_ACCESS_NOT_ARTIFACT_ONLY
[ "$(field_text HOST_COGNITION "$STATUS")" = NO ] || hold HOST_COGNITION_NOT_NO
[ "$(field_text HOST_LEARNING "$STATUS")" = NO ] || hold HOST_LEARNING_NOT_NO
for K in BRAIN_WRITE STATE_WRITE MODEL_WRITE LEARN COMMIT HEAD_CHANGE MODEL_GENERATION_CHANGE; do
  [ "$(field_text "$K" "$STATUS")" = REJECT ] || hold "TEACHER_${K}_MUST_REJECT"
done

SESSION_CODE="$(field_text SESSION_CODE "$STATUS")"
RUN_ID="$(field_text RUN_ID "$STATUS")"
OPEN_HEAD="$(field_text OPEN_HEAD "$STATUS")"
OPEN_MODEL="$(field_text OPEN_MODEL_GENERATION "$STATUS")"
ARTIFACT_ROOT="$(realpath "$(field_text ARTIFACT_ROOT "$STATUS")")"
under "$DESC" "$ARTIFACT_ROOT" || hold DESCRIPTOR_OUTSIDE_CURRENT_ARTIFACT_ROOT

[ "$(field_file SCHEMA "$DESC")" = SIGMA_MULTI_TEACHER_WEIGHT_CANDIDATE_R1 ] || hold DESCRIPTOR_SCHEMA_MISMATCH
[ "$(field_file SOURCE_SESSION_CODE "$DESC")" = "$SESSION_CODE" ] || hold SOURCE_SESSION_MISMATCH
[ "$(field_file SOURCE_RUN_ID "$DESC")" = "$RUN_ID" ] || hold SOURCE_RUN_MISMATCH
[ "$(field_file PARENT_HEAD "$DESC")" = "$OPEN_HEAD" ] || hold PARENT_HEAD_MISMATCH
[ "$(field_file PARENT_MODEL_GENERATION "$DESC")" = "$OPEN_MODEL" ] || hold PARENT_MODEL_GENERATION_MISMATCH
[ "$(field_file CANONICAL_MUTATION_REQUEST "$DESC")" = QUEUE_FOR_NATIVE_REEVALUATION ] || hold CANONICAL_MUTATION_REQUEST_INVALID
[ "$(field_file HOST_COGNITION "$DESC")" = NO ] || hold DESCRIPTOR_HOST_COGNITION_NOT_NO
[ "$(field_file HOST_LEARNING "$DESC")" = NO ] || hold DESCRIPTOR_HOST_LEARNING_NOT_NO
[ "$(field_file SIGMA_NATIVE_LEARNING_OWNER "$DESC")" = YES ] || hold DESCRIPTOR_NATIVE_LEARNING_OWNER_NOT_YES

EVID="$(field_file TEACHING_EVIDENCE_PATH "$DESC")"
EVID_SHA="$(field_file TEACHING_EVIDENCE_SHA256 "$DESC")"
ENTRY="$(field_file CANONICAL_REPLAY_ENTRYPOINT "$DESC")"
ENTRY_SHA="$(field_file CANONICAL_REPLAY_ENTRYPOINT_SHA256 "$DESC")"
OWN="$(field_file NATIVE_OWNERSHIP_RECEIPT "$DESC")"
OWN_SHA="$(field_file NATIVE_OWNERSHIP_RECEIPT_SHA256 "$DESC")"

for P in "$EVID" "$ENTRY" "$OWN"; do
  [ -n "$P" ] || hold REQUIRED_PATH_EMPTY
  RP="$(realpath "$P")"
  under "$RP" "$ARTIFACT_ROOT" || hold REFERENCED_PATH_OUTSIDE_CURRENT_ARTIFACT_ROOT
done
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

DESC_SHA="$(sha "$DESC")"
CID="$DESC_SHA"
OUTBOX="$ARTIFACT_ROOT/CANONICAL_CANDIDATE_QUEUE_OUTBOX"
FINAL="$OUTBOX/$CID"
TMP="$OUTBOX/.partial.$CID.$$"
mkdir -p "$OUTBOX"
if [ -f "$FINAL/READY" ]; then
  printf 'QUEUE_SEAL=IDEMPOTENT_REUSE\nCANDIDATE_ID=%s\nPACKET=%s\n' "$CID" "$FINAL"
  exit 0
fi
[ ! -e "$FINAL" ] || hold EXISTING_UNSEALED_FINAL_PACKET
rm -rf "$TMP"
mkdir -p "$TMP"
cp -f "$DESC" "$TMP/descriptor.env"
printf '%s  %s\n' "$DESC_SHA" descriptor.env > "$TMP/MANIFEST.sha256"
printf 'CANDIDATE_ID=%s\nSOURCE_SESSION_CODE=%s\nSOURCE_RUN_ID=%s\nSEALED_AT=%s\n' \
  "$CID" "$SESSION_CODE" "$RUN_ID" "$(date +%Y-%m-%dT%H:%M:%S%z)" > "$TMP/packet.meta"
(
  cd "$TMP"
  sha256sum descriptor.env packet.meta > PACKET_CONTENT.sha256
  sha256sum -c MANIFEST.sha256 >/dev/null
)
mv "$TMP" "$FINAL"
printf 'READY\n' > "$FINAL/.READY.partial"
mv "$FINAL/.READY.partial" "$FINAL/READY"
printf 'QUEUE_SEAL=PASS\nCANDIDATE_ID=%s\nPACKET=%s\n' "$CID" "$FINAL"
