#!/data/data/com.termux/files/usr/bin/bash
set -eu
VENDOR_ROOT="${SIGMA_TERMUX_CODEC_VENDOR:-$HOME/.sigma/vendor/sigma-freedom-codec}"
START="$VENDOR_ROOT/SIGMA_TOOLS/SEMANTIC_CODEC/TERMUX/start_termux.sh"
BOOT_DIR="$HOME/.termux/boot"
BOOT_FILE="$BOOT_DIR/30-sigma-semantic-codec"

if [ ! -f "$START" ]; then
  echo '[SIGMA] Run install_termux.sh first.' >&2
  exit 10
fi
mkdir -p "$BOOT_DIR"
cat > "$BOOT_FILE" <<EOF
#!/data/data/com.termux/files/usr/bin/sh
export SIGMA_TERMUX_CODEC_VENDOR="$VENDOR_ROOT"
export SIGMA_TERMUX_CODEC_HOME="${SIGMA_TERMUX_CODEC_HOME:-$HOME/.sigma/semantic_codec}"
"$START"
EOF
chmod 700 "$BOOT_FILE"
echo "[SIGMA] BOOT HOOK WRITTEN: $BOOT_FILE"
echo '[SIGMA] Requires the official Termux:Boot add-on, launched once after installation.'
