#!/data/data/com.termux/files/usr/bin/bash
set -eu
STATE_ROOT="${SIGMA_TERMUX_CODEC_HOME:-$HOME/.sigma/semantic_codec}"
PID_FILE="$STATE_ROOT/state/service.pid"

if [ ! -f "$PID_FILE" ]; then
  echo '[SIGMA] NO PID FILE; nothing stopped.'
  exit 0
fi
PID="$(cat "$PID_FILE" 2>/dev/null || true)"
if [ -z "$PID" ] || ! kill -0 "$PID" 2>/dev/null; then
  rm -f "$PID_FILE"
  echo '[SIGMA] STALE PID FILE REMOVED.'
  exit 0
fi

CMDLINE="$(tr '\000' ' ' < "/proc/$PID/cmdline" 2>/dev/null || true)"
case "$CMDLINE" in
  *sigma_semantic_codec_termux.py*) ;;
  *)
    echo "[SIGMA] REFUSING TO KILL PID $PID: command is not the semantic codec." >&2
    echo "[SIGMA] CMD=$CMDLINE" >&2
    exit 8
    ;;
esac

kill "$PID"
N=0
while kill -0 "$PID" 2>/dev/null && [ "$N" -lt 10 ]; do
  N=$((N + 1))
  sleep 1
done
if kill -0 "$PID" 2>/dev/null; then
  echo "[SIGMA] PID $PID did not stop; no SIGKILL was issued automatically." >&2
  exit 9
fi
rm -f "$PID_FILE"
if [ "${SIGMA_TERMUX_WAKE_LOCK:-0}" = "1" ] && command -v termux-wake-unlock >/dev/null 2>&1; then
  termux-wake-unlock || true
fi
echo '[SIGMA] STOP PASS'
