#!/usr/bin/env bash
set -euo pipefail
umask 077

HERE="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SLEEP_SECONDS="${SIGMA_QUEUE_SLEEP_SECONDS:-10}"
case "$SLEEP_SECONDS" in ''|*[!0-9]*) echo 'HOLD=INVALID_SLEEP_SECONDS'; exit 2;; esac

printf 'MULTI_TEACHER_CANONICAL_QUEUE_DAEMON=START\nPID=%s\nBASH_ROLE=MECHANICAL_ONLY\nBASH_LEARNING=NO\nRUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME\n' "$$"
while :; do
  set +e
  OUT="$("$HERE/drain_once.sh" 2>&1)"
  RC=$?
  set -e
  printf '%s\n' "$OUT"

  if printf '%s\n' "$OUT" | grep -Fqx 'QUEUE_DRAIN=EMPTY'; then
    sleep "$SLEEP_SECONDS"
    continue
  fi
  if printf '%s\n' "$OUT" | grep -Fqx 'QUEUE_DRAIN=NO_UNPROCESSED_PACKET'; then
    sleep "$SLEEP_SECONDS"
    continue
  fi
  if [ "$RC" -eq 0 ]; then
    # Exactly one packet is mechanically serialized per invocation. The next
    # invocation re-reads the CURRENT Oppo canonical state before any replay.
    continue
  fi

  # HOLD/failure is evidence. Never skip to a different candidate as a host-side
  # semantic/scheduling workaround.
  printf 'MULTI_TEACHER_CANONICAL_QUEUE_DAEMON=HOLD\nDRAIN_RC=%s\n' "$RC"
  exit "$RC"
done
