#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
CMD="${2:-status}"
AUTO_ROOT="$ROOT/.sigma_c5v3_auto"
RUNNER="$AUTO_ROOT/control/RUN_C5V3_R4_AUTO_SHADOW_R1.sh"
SURVIVE="$AUTO_ROOT/survival"
SUP_PID="$SURVIVE/supervisor.pid"
WORK_PID="$SURVIVE/worker.pid"
STOP_FILE="$SURVIVE/stop.requested"
LOCK_DIR="$SURVIVE/supervisor.lock"
SUP_LOG="$SURVIVE/supervisor.log"
WORK_LOG="$SURVIVE/auto_continuous.log"
HEARTBEAT="$SURVIVE/heartbeat.txt"
WAKE_STATE="$SURVIVE/wake_lock_state.txt"
RESTART_DELAY="${SIGMA_R4_RESTART_DELAY_SECONDS:-3}"
POLL_SECONDS="${SIGMA_AUTO_POLL_SECONDS:-5}"
BOOT_SCRIPT="$HOME/.termux/boot/10-sigma-c5v3-r4-auto"

mkdir -p "$SURVIVE"

read_pid(){
  local f="$1"
  [ -f "$f" ] && tr -dc '0-9' < "$f" || true
}

alive_pidfile(){
  local f="$1" p
  p="$(read_pid "$f")"
  [ -n "$p" ] && kill -0 "$p" 2>/dev/null
}

log(){
  printf '%s %s\n' "$(date '+%Y-%m-%dT%H:%M:%S%z')" "$*" >> "$SUP_LOG"
}

require_runner(){
  [ -f "$RUNNER" ] || { echo "HOLD=R4_AUTO_RUNNER_MISSING:$RUNNER"; exit 1; }
  [ -x "$RUNNER" ] || { echo "HOLD=R4_AUTO_RUNNER_NOT_EXECUTABLE:$RUNNER"; exit 1; }
}

acquire_wake_lock(){
  if command -v termux-wake-lock >/dev/null 2>&1; then
    if termux-wake-lock >/dev/null 2>&1; then
      printf 'HELD\n' > "$WAKE_STATE"
      log "WAKE_LOCK=HELD"
    else
      printf 'FAILED\n' > "$WAKE_STATE"
      log "WAKE_LOCK=FAILED"
    fi
  else
    printf 'UNAVAILABLE\n' > "$WAKE_STATE"
    log "WAKE_LOCK=UNAVAILABLE"
  fi
}

release_wake_lock(){
  if [ "$(cat "$WAKE_STATE" 2>/dev/null || true)" = "HELD" ] && command -v termux-wake-unlock >/dev/null 2>&1; then
    termux-wake-unlock >/dev/null 2>&1 || true
  fi
  printf 'RELEASED\n' > "$WAKE_STATE"
}

cleanup_supervisor(){
  local w
  w="$(read_pid "$WORK_PID")"
  if [ -n "$w" ] && kill -0 "$w" 2>/dev/null; then
    kill "$w" 2>/dev/null || true
  fi
  rm -f "$WORK_PID" "$SUP_PID"
  rm -rf "$LOCK_DIR"
  release_wake_lock
  log "SUPERVISOR=STOPPED"
}

supervise(){
  require_runner
  if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    if alive_pidfile "$SUP_PID"; then
      echo "AUTO_PERSISTENT_SUPERVISOR=ALREADY_RUNNING"
      exit 0
    fi
    rm -rf "$LOCK_DIR"
    mkdir "$LOCK_DIR"
  fi
  printf '%s\n' "$$" > "$SUP_PID"
  rm -f "$STOP_FILE"
  trap cleanup_supervisor EXIT INT TERM HUP
  acquire_wake_lock
  log "SUPERVISOR=START PID=$$ ROOT=$ROOT"

  while [ ! -f "$STOP_FILE" ]; do
    printf '%s\n' "$(date '+%Y-%m-%dT%H:%M:%S%z')" > "$HEARTBEAT"
    log "WORKER=START"
    set +e
    SIGMA_AUTO_POLL_SECONDS="$POLL_SECONDS" "$RUNNER" "$ROOT" loop >> "$WORK_LOG" 2>&1 &
    worker=$!
    printf '%s\n' "$worker" > "$WORK_PID"
    wait "$worker"
    rc=$?
    set -e
    rm -f "$WORK_PID"
    printf '%s\n' "$(date '+%Y-%m-%dT%H:%M:%S%z')" > "$HEARTBEAT"
    log "WORKER=EXIT RC=$rc"
    [ -f "$STOP_FILE" ] && break
    sleep "$RESTART_DELAY"
  done
}

start(){
  require_runner
  if alive_pidfile "$SUP_PID"; then
    echo "AUTO_PERSISTENT_SUPERVISOR=ALREADY_RUNNING"
    echo "AUTO_SUPERVISOR_PID=$(read_pid "$SUP_PID")"
    return 0
  fi
  rm -f "$SUP_PID" "$WORK_PID" "$STOP_FILE"
  rm -rf "$LOCK_DIR"
  if command -v setsid >/dev/null 2>&1; then
    nohup setsid "$0" "$ROOT" supervise >> "$SUP_LOG" 2>&1 < /dev/null &
  else
    nohup "$0" "$ROOT" supervise >> "$SUP_LOG" 2>&1 < /dev/null &
  fi
  launcher=$!
  disown "$launcher" 2>/dev/null || true
  for _ in 1 2 3 4 5; do
    alive_pidfile "$SUP_PID" && break
    sleep 1
  done
  if alive_pidfile "$SUP_PID"; then
    echo "AUTO_PERSISTENT_SUPERVISOR=STARTED"
    echo "AUTO_SUPERVISOR_PID=$(read_pid "$SUP_PID")"
    echo "AUTO_CONTINUOUS_LOG=$WORK_LOG"
  else
    echo "HOLD=AUTO_PERSISTENT_SUPERVISOR_START_FAILED"
    [ -f "$SUP_LOG" ] && tail -n 40 "$SUP_LOG"
    exit 1
  fi
}

stop(){
  touch "$STOP_FILE"
  w="$(read_pid "$WORK_PID")"
  s="$(read_pid "$SUP_PID")"
  if [ -n "$w" ] && kill -0 "$w" 2>/dev/null; then kill "$w" 2>/dev/null || true; fi
  if [ -n "$s" ] && kill -0 "$s" 2>/dev/null; then kill "$s" 2>/dev/null || true; fi
  echo "AUTO_PERSISTENT_SUPERVISOR=STOP_REQUESTED"
}

status(){
  require_runner
  if alive_pidfile "$SUP_PID"; then
    echo "AUTO_PERSISTENT_SUPERVISOR=RUNNING"
    echo "AUTO_SUPERVISOR_PID=$(read_pid "$SUP_PID")"
  else
    echo "AUTO_PERSISTENT_SUPERVISOR=STOPPED"
  fi
  if alive_pidfile "$WORK_PID"; then
    echo "AUTO_WORKER=RUNNING"
    echo "AUTO_WORKER_PID=$(read_pid "$WORK_PID")"
  else
    echo "AUTO_WORKER=NOT_RUNNING"
  fi
  echo "AUTO_WAKE_LOCK_STATE=$(cat "$WAKE_STATE" 2>/dev/null || echo UNKNOWN)"
  echo "AUTO_HEARTBEAT=$(cat "$HEARTBEAT" 2>/dev/null || echo NONE)"
  echo "AUTO_CONTINUOUS_LOG=$WORK_LOG"
  "$RUNNER" "$ROOT" status
}

install_boot(){
  mkdir -p "$(dirname "$BOOT_SCRIPT")"
  cat > "$BOOT_SCRIPT" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
exec "$0" "$ROOT" start
EOF
  chmod 700 "$BOOT_SCRIPT"
  echo "AUTO_BOOT_SCRIPT_INSTALLED=$BOOT_SCRIPT"
  echo "AUTO_BOOT_REQUIRES_TERMUX_BOOT_APP=YES"
}

uninstall_boot(){
  rm -f "$BOOT_SCRIPT"
  echo "AUTO_BOOT_SCRIPT_REMOVED=$BOOT_SCRIPT"
}

case "$CMD" in
  supervise) supervise ;;
  start) start ;;
  stop) stop ;;
  restart-supervisor) stop; sleep 1; rm -f "$STOP_FILE"; start ;;
  status) status ;;
  install-boot) install_boot ;;
  uninstall-boot) uninstall_boot ;;
  *)
    echo "USAGE: $0 ROOT {start|stop|restart-supervisor|status|install-boot|uninstall-boot}"
    exit 2
    ;;
esac
