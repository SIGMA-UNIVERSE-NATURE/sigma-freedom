#!/data/data/com.termux/files/usr/bin/bash
set -eu

VENDOR_ROOT="${SIGMA_TERMUX_CODEC_VENDOR:-$HOME/.sigma/vendor/sigma-freedom-codec}"
TOOL_DIR="$VENDOR_ROOT/SIGMA_TOOLS/SEMANTIC_CODEC/TERMUX"
STATE_ROOT="${SIGMA_TERMUX_CODEC_HOME:-$HOME/.sigma/semantic_codec}"
HOST="${SIGMA_TERMUX_CODEC_HOST:-127.0.0.1}"
PORT="${SIGMA_TERMUX_CODEC_PORT:-8765}"
PID_FILE="$STATE_ROOT/state/service.pid"
LOG_FILE="$STATE_ROOT/logs/service.log"
SERVICE="$TOOL_DIR/sigma_semantic_codec_termux.py"

mkdir -p "$STATE_ROOT/state" "$STATE_ROOT/logs" "$STATE_ROOT/packages"
chmod 700 "$STATE_ROOT" "$STATE_ROOT/state" "$STATE_ROOT/logs" "$STATE_ROOT/packages" 2>/dev/null || true

if [ "$HOST" != "127.0.0.1" ] && [ "$HOST" != "localhost" ] && [ "$HOST" != "::1" ] && [ -z "${SIGMA_CODEC_API_KEY:-}" ]; then
  echo '[SIGMA] REFUSING NON-LOOPBACK WITHOUT SIGMA_CODEC_API_KEY' >&2
  exit 4
fi

if curl -fsS --max-time 2 "http://127.0.0.1:$PORT/v1/health" >/dev/null 2>&1; then
  echo "[SIGMA] ALREADY RUNNING: http://127.0.0.1:$PORT"
  exit 0
fi

if [ -f "$PID_FILE" ]; then
  PID="$(cat "$PID_FILE" 2>/dev/null || true)"
  if [ -n "$PID" ] && kill -0 "$PID" 2>/dev/null; then
    echo "[SIGMA] REFUSING DUPLICATE: PID $PID exists but health is not ready." >&2
    echo "[SIGMA] Inspect $LOG_FILE and use stop_termux.sh only if it is this codec." >&2
    exit 5
  fi
  rm -f "$PID_FILE"
fi

if [ "${SIGMA_TERMUX_WAKE_LOCK:-0}" = "1" ] && command -v termux-wake-lock >/dev/null 2>&1; then
  termux-wake-lock || true
fi

export SIGMA_TERMUX_CODEC_HOME="$STATE_ROOT"
nohup python "$SERVICE" --host "$HOST" --port "$PORT" >>"$LOG_FILE" 2>&1 &
PID=$!
printf '%s\n' "$PID" > "$PID_FILE"
chmod 600 "$PID_FILE" 2>/dev/null || true

N=0
while [ "$N" -lt 15 ]; do
  if curl -fsS --max-time 2 "http://127.0.0.1:$PORT/v1/health" >/dev/null 2>&1; then
    echo "[SIGMA] START PASS pid=$PID url=http://127.0.0.1:$PORT"
    exit 0
  fi
  if ! kill -0 "$PID" 2>/dev/null; then
    echo "[SIGMA] START FAILED. See: $LOG_FILE" >&2
    rm -f "$PID_FILE"
    exit 6
  fi
  N=$((N + 1))
  sleep 1
done

echo "[SIGMA] START TIMEOUT. See: $LOG_FILE" >&2
exit 7
