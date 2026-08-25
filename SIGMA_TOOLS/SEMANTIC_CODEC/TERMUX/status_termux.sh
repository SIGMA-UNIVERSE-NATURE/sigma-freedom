#!/data/data/com.termux/files/usr/bin/bash
set -eu
STATE_ROOT="${SIGMA_TERMUX_CODEC_HOME:-$HOME/.sigma/semantic_codec}"
PORT="${SIGMA_TERMUX_CODEC_PORT:-8765}"
PID_FILE="$STATE_ROOT/state/service.pid"

if curl -fsS --max-time 2 "http://127.0.0.1:$PORT/v1/health"; then
  echo
  [ -f "$PID_FILE" ] && echo "PID=$(cat "$PID_FILE")"
  exit 0
fi

echo '[SIGMA] CODEC NOT HEALTHY' >&2
[ -f "$PID_FILE" ] && echo "PID_FILE=$(cat "$PID_FILE")" >&2
exit 1
