#!/usr/bin/env bash
set -euo pipefail
umask 077

hold(){ printf 'HOLD=%s\n' "$1"; exit 2; }
sha(){ sha256sum "$1" | awk '{print $1}'; }
kv(){ awk -F= -v K="$1" '$1==K{sub(/^[^=]*=/,"");print;exit}' "$2"; }

[ "$#" -eq 1 ] || hold DESCRIPTOR_ARGUMENT_REQUIRED
DESC="$1"
[ -f "$DESC" ] || hold RECOVERY_DESCRIPTOR_MISSING
[ -f "$DESC.sha256" ] || hold RECOVERY_DESCRIPTOR_HASH_MISSING
( cd "$(dirname "$DESC")" && sha256sum -c "$(basename "$DESC").sha256" >/dev/null ) || hold RECOVERY_DESCRIPTOR_HASH_MISMATCH

WORK_ID="$(kv WORK_ID "$DESC")"
ENTRYPOINT="$(kv ENTRYPOINT "$DESC")"
ENTRY_SHA="$(kv ENTRYPOINT_SHA256 "$DESC")"
COMPLETION="$(kv COMPLETION_RECEIPT "$DESC")"
LOCK_PATH="$(kv RECOVERY_LOCK_PATH "$DESC")"
MAX_RESTARTS="$(kv MAX_RESTARTS "$DESC")"
CANON="$(kv CANONICAL_MUTATION "$DESC")"

[ -n "$WORK_ID" ] || hold WORK_ID_MISSING
[ "$CANON" = NO ] || hold CANONICAL_MUTATION_NOT_NO
[ -f "$ENTRYPOINT" ] || hold ENTRYPOINT_MISSING
[ "$(sha "$ENTRYPOINT")" = "$ENTRY_SHA" ] || hold ENTRYPOINT_HASH_MISMATCH
[[ "$MAX_RESTARTS" =~ ^[0-9]+$ ]] || hold MAX_RESTARTS_INVALID
mkdir -p "$(dirname "$LOCK_PATH")"
exec 9>"$LOCK_PATH"
flock -n 9 || hold SAME_WORK_ALREADY_SUPERVISED

if [ -f "$COMPLETION" ]; then
  printf 'RECOVERY=NO_RESTART_ALREADY_COMPLETE\nWORK_ID=%s\n' "$WORK_ID"
  exit 0
fi

attempt=0
while [ "$attempt" -le "$MAX_RESTARTS" ]; do
  attempt=$((attempt+1))
  printf 'SURVIVAL_ATTEMPT=%s\nWORK_ID=%s\n' "$attempt" "$WORK_ID"
  set +e
  "$ENTRYPOINT" "$DESC"
  rc=$?
  set -e
  if [ -f "$COMPLETION" ]; then
    printf 'SURVIVAL_RESULT=COMPLETE\nWORK_ID=%s\nCHILD_RC=%s\n' "$WORK_ID" "$rc"
    exit 0
  fi
  if [ "$rc" -eq 0 ]; then
    hold CHILD_EXITED_ZERO_WITHOUT_COMPLETION_RECEIPT
  fi
  if [ "$attempt" -gt "$MAX_RESTARTS" ]; then
    hold MECHANICAL_RESTART_BOUND_REACHED
  fi
  sleep 1
done
hold UNREACHABLE_SUPERVISOR_STATE
