#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
CMD="${2:-status}"
AUTO_ROOT="$ROOT/.sigma_c5v3_auto"
SUP="$AUTO_ROOT/control/RUN_C5V3_R4_AUTO_PERSISTENT_SUPERVISOR_R2.sh"
REC="$AUTO_ROOT/recovery"
ANCHOR_PID="$REC/anchor.pid"
ANCHOR_LOCK="$REC/anchor.lock"
ANCHOR_LOG="$REC/anchor.log"
ANCHOR_HEARTBEAT="$REC/anchor_heartbeat.txt"
DISABLED="$REC/recovery.disabled"
SURVIVE="$AUTO_ROOT/survival"
SUP_PID="$SURVIVE/supervisor.pid"
WORK_PID="$SURVIVE/worker.pid"
ANCHOR_POLL_SECONDS="${SIGMA_R4_ANCHOR_POLL_SECONDS:-5}"
JOB_ID="${SIGMA_R4_RECOVERY_JOB_ID:-54004}"
JOB_PERIOD_MS="${SIGMA_R4_RECOVERY_JOB_PERIOD_MS:-900000}"
JOB_SCRIPT="$REC/android_recovery_job.sh"
BOOT_SCRIPT="$HOME/.termux/boot/05-sigma-c5v3-r4-recovery"

mkdir -p "$REC"

read_pid(){
  local f="$1"
  [ -f "$f" ] && tr -dc '0-9' < "$f" || true
}

pid_alive(){
  local p="$1"
  [ -n "$p" ] && kill -0 "$p" 2>/dev/null
}

pid_cmdline(){
  local p="$1"
  [ -r "/proc/$p/cmdline" ] && tr '\0' ' ' < "/proc/$p/cmdline" || true
}

anchor_valid(){
  local p
  p="$(read_pid "$ANCHOR_PID")"
  pid_alive "$p" || return 1
  case "$(pid_cmdline "$p")" in
    *RUN_C5V3_R4_AUTO_RECOVERY_ANCHOR_R1.sh*" $ROOT anchor"*) return 0 ;;
    *) return 1 ;;
  esac
}

supervisor_valid(){
  local p
  p="$(read_pid "$SUP_PID")"
  pid_alive "$p" || return 1
  case "$(pid_cmdline "$p")" in
    *RUN_C5V3_R4_AUTO_PERSISTENT_SUPERVISOR_R2.sh*" $ROOT supervise"*) return 0 ;;
    *) return 1 ;;
  esac
}

worker_alive(){
  local p
  p="$(read_pid "$WORK_PID")"
  pid_alive "$p"
}

log(){
  printf '%s %s\n' "$(date '+%Y-%m-%dT%H:%M:%S%z')" "$*" >> "$ANCHOR_LOG"
}

heartbeat(){
  printf '%s\n' "$(date '+%Y-%m-%dT%H:%M:%S%z')" > "$ANCHOR_HEARTBEAT"
}

require_supervisor(){
  [ -f "$SUP" ] || { echo "HOLD=R4_AUTO_SUPERVISOR_R2_MISSING:$SUP"; exit 1; }
  [ -x "$SUP" ] || { echo "HOLD=R4_AUTO_SUPERVISOR_R2_NOT_EXECUTABLE:$SUP"; exit 1; }
}

ensure_supervisor(){
  require_supervisor
  [ ! -f "$DISABLED" ] || { echo "AUTO_RECOVERY=DISABLED"; return 0; }
  if supervisor_valid; then
    echo "AUTO_RECOVERY_SUPERVISOR=ALREADY_RUNNING"
    return 0
  fi
  log "SUPERVISOR=ABSENT RESTART=BEGIN"
  "$SUP" "$ROOT" start >> "$ANCHOR_LOG" 2>&1
  if supervisor_valid; then
    log "SUPERVISOR=RECOVERED PID=$(read_pid "$SUP_PID")"
    echo "AUTO_RECOVERY_SUPERVISOR=RECOVERED"
    echo "AUTO_RECOVERY_SUPERVISOR_PID=$(read_pid "$SUP_PID")"
    if worker_alive; then echo "AUTO_RECOVERY_WORKER_PID=$(read_pid "$WORK_PID")"; fi
  else
    log "SUPERVISOR=RECOVERY_FAILED"
    echo "HOLD=SUPERVISOR_RECOVERY_FAILED"
    return 1
  fi
}

cleanup_anchor(){
  rm -f "$ANCHOR_PID"
  rm -rf "$ANCHOR_LOCK"
  log "ANCHOR=STOPPED"
}

anchor(){
  require_supervisor
  if ! mkdir "$ANCHOR_LOCK" 2>/dev/null; then
    if anchor_valid; then
      echo "AUTO_RECOVERY_ANCHOR=ALREADY_RUNNING"
      exit 0
    fi
    rm -rf "$ANCHOR_LOCK"
    mkdir "$ANCHOR_LOCK"
  fi
  printf '%s\n' "$$" > "$ANCHOR_PID"
  trap cleanup_anchor EXIT INT TERM HUP
  log "ANCHOR=START PID=$$ ROOT=$ROOT"
  while [ ! -f "$DISABLED" ]; do
    heartbeat
    if ! supervisor_valid; then
      ensure_supervisor >> "$ANCHOR_LOG" 2>&1 || true
    fi
    sleep "$ANCHOR_POLL_SECONDS"
  done
}

start(){
  require_supervisor
  rm -f "$DISABLED"
  ensure_supervisor >/dev/null
  if anchor_valid; then
    echo "AUTO_RECOVERY_ANCHOR=ALREADY_RUNNING"
    echo "AUTO_RECOVERY_ANCHOR_PID=$(read_pid "$ANCHOR_PID")"
    return 0
  fi
  rm -f "$ANCHOR_PID"
  rm -rf "$ANCHOR_LOCK"
  if command -v setsid >/dev/null 2>&1; then
    nohup setsid "$0" "$ROOT" anchor >> "$ANCHOR_LOG" 2>&1 < /dev/null &
  else
    nohup "$0" "$ROOT" anchor >> "$ANCHOR_LOG" 2>&1 < /dev/null &
  fi
  launcher=$!
  disown "$launcher" 2>/dev/null || true
  for _ in 1 2 3 4 5; do
    anchor_valid && break
    sleep 1
  done
  if anchor_valid; then
    echo "AUTO_RECOVERY_ANCHOR=STARTED"
    echo "AUTO_RECOVERY_ANCHOR_PID=$(read_pid "$ANCHOR_PID")"
    echo "AUTO_RECOVERY_ANCHOR_LOG=$ANCHOR_LOG"
  else
    echo "HOLD=AUTO_RECOVERY_ANCHOR_START_FAILED"
    tail -n 40 "$ANCHOR_LOG" 2>/dev/null || true
    exit 1
  fi
}

stop(){
  local p
  touch "$DISABLED"
  p="$(read_pid "$ANCHOR_PID")"
  if pid_alive "$p"; then kill "$p" 2>/dev/null || true; fi
  echo "AUTO_RECOVERY_ANCHOR=STOP_REQUESTED"
  echo "AUTO_RECOVERY_DISABLED=YES"
}

status(){
  if anchor_valid; then
    echo "AUTO_RECOVERY_ANCHOR=RUNNING"
    echo "AUTO_RECOVERY_ANCHOR_PID=$(read_pid "$ANCHOR_PID")"
  else
    echo "AUTO_RECOVERY_ANCHOR=NOT_RUNNING"
  fi
  echo "AUTO_RECOVERY_ANCHOR_HEARTBEAT=$(cat "$ANCHOR_HEARTBEAT" 2>/dev/null || echo NONE)"
  if supervisor_valid; then
    echo "AUTO_RECOVERY_SUPERVISOR=RUNNING"
    echo "AUTO_RECOVERY_SUPERVISOR_PID=$(read_pid "$SUP_PID")"
  else
    echo "AUTO_RECOVERY_SUPERVISOR=NOT_RUNNING"
  fi
  if worker_alive; then
    echo "AUTO_RECOVERY_WORKER=RUNNING"
    echo "AUTO_RECOVERY_WORKER_PID=$(read_pid "$WORK_PID")"
  else
    echo "AUTO_RECOVERY_WORKER=NOT_RUNNING"
  fi
  if [ -f "$DISABLED" ]; then echo "AUTO_RECOVERY_DISABLED=YES"; else echo "AUTO_RECOVERY_DISABLED=NO"; fi
  if command -v termux-job-scheduler >/dev/null 2>&1; then
    echo "AUTO_ANDROID_JOB_SCHEDULER=AVAILABLE"
  else
    echo "AUTO_ANDROID_JOB_SCHEDULER=UNAVAILABLE"
  fi
  echo "AUTO_RECOVERY_JOB_ID=$JOB_ID"
  echo "AUTO_RECOVERY_JOB_PERIOD_MS=$JOB_PERIOD_MS"
  echo "AUTO_RECOVERY_LOG=$ANCHOR_LOG"
}

write_job_script(){
  cat > "$JOB_SCRIPT" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
ROOT="$ROOT"
ANCHOR="$AUTO_ROOT/control/RUN_C5V3_R4_AUTO_RECOVERY_ANCHOR_R1.sh"
[ -x "\$ANCHOR" ] || exit 1
exec "\$ANCHOR" "\$ROOT" ensure
EOF
  chmod 700 "$JOB_SCRIPT"
}

install_android_job(){
  command -v termux-job-scheduler >/dev/null 2>&1 || {
    echo "HOLD=TERMUX_JOB_SCHEDULER_UNAVAILABLE"
    echo "REQUIRES=TERMUX_API_APP_AND_TERMUX_API_PACKAGE"
    exit 1
  }
  write_job_script
  termux-job-scheduler \
    --script "$JOB_SCRIPT" \
    --job-id "$JOB_ID" \
    --period-ms "$JOB_PERIOD_MS" \
    --network none \
    --battery-not-low false \
    --storage-not-low false \
    --charging false \
    --persisted true
  echo "AUTO_ANDROID_RECOVERY_JOB=INSTALLED"
  echo "AUTO_RECOVERY_JOB_ID=$JOB_ID"
  echo "AUTO_RECOVERY_JOB_PERIOD_MS=$JOB_PERIOD_MS"
}

cancel_android_job(){
  command -v termux-job-scheduler >/dev/null 2>&1 || { echo "HOLD=TERMUX_JOB_SCHEDULER_UNAVAILABLE"; exit 1; }
  termux-job-scheduler --cancel --job-id "$JOB_ID"
  echo "AUTO_ANDROID_RECOVERY_JOB=CANCELLED"
}

install_boot(){
  mkdir -p "$(dirname "$BOOT_SCRIPT")"
  cat > "$BOOT_SCRIPT" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
exec "$0" "$ROOT" ensure
EOF
  chmod 700 "$BOOT_SCRIPT"
  echo "AUTO_RECOVERY_BOOT_SCRIPT_INSTALLED=$BOOT_SCRIPT"
  echo "AUTO_RECOVERY_BOOT_REQUIRES_TERMUX_BOOT_APP=YES"
}

uninstall_boot(){
  rm -f "$BOOT_SCRIPT"
  echo "AUTO_RECOVERY_BOOT_SCRIPT_REMOVED=$BOOT_SCRIPT"
}

case "$CMD" in
  anchor) anchor ;;
  start) start ;;
  ensure)
    rm -f "$DISABLED"
    ensure_supervisor >/dev/null
    if ! anchor_valid; then start >/dev/null; fi
    echo "AUTO_RECOVERY_ENSURE=PASS"
    ;;
  stop) stop ;;
  status) status ;;
  install-android-job) install_android_job ;;
  cancel-android-job) cancel_android_job ;;
  install-boot) install_boot ;;
  uninstall-boot) uninstall_boot ;;
  *)
    echo "USAGE: $0 ROOT {start|ensure|stop|status|install-android-job|cancel-android-job|install-boot|uninstall-boot}"
    exit 2
    ;;
esac
