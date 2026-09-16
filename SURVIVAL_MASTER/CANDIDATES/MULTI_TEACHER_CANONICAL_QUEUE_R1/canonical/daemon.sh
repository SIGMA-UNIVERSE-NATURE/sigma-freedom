#!/usr/bin/env bash
set -euo pipefail
umask 077

HERE="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SLEEP_SECONDS="${SIGMA_QUEUE_SLEEP_SECONDS:-10}"
case "$SLEEP_SECONDS" in ''|*[!0-9]*) echo 'HOLD=INVALID_SLEEP_SECONDS'; exit 2;; esac

printf 'MULTI_TEACHER_CANONICAL_QUEUE_DAEMON=START\nPID=%s\n' "$$"
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
    # Exactly one packet is handled per drain invocation; loop to re-read current
    # canonical head/generation before touching the next candidate.
    continue
  fi

  # HOLD/failure is evidence. Do not skip to another candidate because doing so
  # would be a host-side learning/scheduling policy decision.
  printf 'MULTI_TEACHER_CANONICAL_QUEUE_DAEMON=HOLD\nDRAIN_RC=%s\n' "$RC"
  exit "$RC"
done
