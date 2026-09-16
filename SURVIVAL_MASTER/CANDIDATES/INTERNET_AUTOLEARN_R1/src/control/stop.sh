#!/usr/bin/env bash
set -euo pipefail
# R1 has no production daemon enablement. Stop is deliberately non-destructive.
# It never kills by pattern and never removes canonical locks.
[ "$#" -eq 1 ] || { echo 'HOLD=CANDIDATE_PIDFILE_REQUIRED'; exit 2; }
P="$1"
[ -f "$P" ] || { echo 'STOP=NO_CANDIDATE_PIDFILE'; exit 0; }
PID="$(cat "$P")"
[[ "$PID" =~ ^[0-9]+$ ]] || { echo 'HOLD=PIDFILE_INVALID'; exit 2; }
if kill -0 "$PID" 2>/dev/null; then
  kill -TERM "$PID"
  echo "STOP_SIGNAL_SENT_PID=$PID"
else
  echo 'STOP=CANDIDATE_PROCESS_NOT_ALIVE'
fi
