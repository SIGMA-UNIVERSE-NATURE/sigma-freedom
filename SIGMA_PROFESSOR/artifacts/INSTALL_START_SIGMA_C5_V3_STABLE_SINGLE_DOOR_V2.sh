#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

ROOT="${SIGMA_ROOT:-$HOME/SIGMA/sigma_genesis1}"
OPS="$ROOT/.sigma_ops"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

WATCHER_SRC="$SRC_DIR/SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.py"
SUP_SRC="$SRC_DIR/RUN_SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.sh"

WATCHER_DST="$OPS/SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.py"
SUP_DST="$OPS/RUN_SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.sh"

WATCHER_SHA="cea1bd96d2ebd80538d066467bdceac9ef3053fd09c80c8eac6181173fc3f286"
SUP_SHA="c57838b59d855886943de164fdf8272dc8f6f66a650d280ae3b32287a122aed6"

LOG="$ROOT/SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.log"
STATUS="$ROOT/.sigma_supervisor/stable_single_door_v2/status.txt"
WATCHER_STATUS="$OPS/SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.status"

mkdir -p "$OPS"

hash1() { sha256sum "$1" | awk '{print $1}'; }

[ -f "$WATCHER_SRC" ] || {
    echo "HOLD=WATCHER_SOURCE_MISSING path=$WATCHER_SRC"
    exit 20
}
[ -f "$SUP_SRC" ] || {
    echo "HOLD=SUPERVISOR_SOURCE_MISSING path=$SUP_SRC"
    exit 21
}

[ "$(hash1 "$WATCHER_SRC")" = "$WATCHER_SHA" ] || {
    echo "HOLD=WATCHER_SOURCE_SHA_MISMATCH"
    exit 22
}
[ "$(hash1 "$SUP_SRC")" = "$SUP_SHA" ] || {
    echo "HOLD=SUPERVISOR_SOURCE_SHA_MISMATCH"
    exit 23
}

stop_named_control_process() {
    NAME="$1"
    for D in /proc/[0-9]*; do
        [ -r "$D/cmdline" ] || continue
        P="${D##*/}"
        [ "$P" = "$$" ] && continue
        CMD="$(tr '\000' ' ' < "$D/cmdline" 2>/dev/null || true)"
        case "$CMD" in
            *"$NAME"*)
                echo "STOP_CONTROL_PROCESS name=$NAME pid=$P"
                kill -TERM "$P" 2>/dev/null || true
                ;;
        esac
    done
}

# Stop only old control-plane processes. Never kill the C5 V3 runner here.
stop_named_control_process "SIGMA_C5_REBIRTH_SUPERVISOR_V1.sh"
stop_named_control_process "SIGMA_SINGLE_DOOR_SUPERVISOR_V1.sh"
stop_named_control_process "RUN_SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.sh"
stop_named_control_process "SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.py"

sleep 3

install -m 700 "$WATCHER_SRC" "$WATCHER_DST"
install -m 700 "$SUP_SRC" "$SUP_DST"

echo "WATCHER_INSTALLED_SHA256=$(hash1 "$WATCHER_DST")"
echo "SUPERVISOR_INSTALLED_SHA256=$(hash1 "$SUP_DST")"

[ "$(hash1 "$WATCHER_DST")" = "$WATCHER_SHA" ] || exit 24
[ "$(hash1 "$SUP_DST")" = "$SUP_SHA" ] || exit 25

if command -v termux-wake-lock >/dev/null 2>&1; then
    termux-wake-lock >/dev/null 2>&1 || true
    echo "TERMUX_WAKE_LOCK=REQUESTED"
fi

nohup "$SUP_DST" >> "$LOG" 2>&1 &
SPID=$!
echo "STABLE_SINGLE_DOOR_SUPERVISOR_PID=$SPID"

# Install a reboot hook. It is used automatically only when the Termux:Boot app
# is installed and enabled by the user.
BOOTDIR="$HOME/.termux/boot"
mkdir -p "$BOOTDIR"
cat > "$BOOTDIR/90-sigma-c5-v3-stable-single-door.sh" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
sleep 10
ROOT="\$HOME/SIGMA/sigma_genesis1"
SUP="\$ROOT/.sigma_ops/RUN_SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.sh"
LOG="\$ROOT/SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.log"
if command -v termux-wake-lock >/dev/null 2>&1; then
  termux-wake-lock >/dev/null 2>&1 || true
fi
[ -x "\$SUP" ] && nohup "\$SUP" >> "\$LOG" 2>&1 &
EOF
chmod 700 "$BOOTDIR/90-sigma-c5-v3-stable-single-door.sh"
echo "TERMUX_BOOT_HOOK_INSTALLED=YES"

sleep 25

echo
echo "=== STREAM COHERENCE ==="
cat "$WATCHER_STATUS" 2>/dev/null || true

echo
echo "=== STABLE SINGLE DOOR STATUS ==="
cat "$STATUS" 2>/dev/null || true

echo
echo "=== RECENT CONTROL LOG ==="
tail -n 160 "$LOG" 2>/dev/null || true

echo
echo "=== INSTALL FINAL ==="
echo "C5_V3_RUNNER_MODIFIED=NO"
echo "NATIVE_CORE_MODIFIED=NO"
echo "SIGMAC_MODIFIED=NO"
echo "VM_MODIFIED=NO"
echo "STREAM_COHERENCE_RUNTIME_GUARD=ENABLED"
echo "LOCAL_AND_INTERNET_SINGLE_COORDINATED_DOOR=ENABLED"
echo "GLOBAL_TURN_LIMIT=NONE"
echo "GLOBAL_FETCH_LIMIT=NONE"
