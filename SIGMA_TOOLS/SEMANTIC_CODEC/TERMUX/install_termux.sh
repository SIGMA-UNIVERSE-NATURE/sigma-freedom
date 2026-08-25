#!/data/data/com.termux/files/usr/bin/bash
set -eu

REPO_URL="https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom.git"
BRANCH="SIGMA_LIFE"
VENDOR_ROOT="${SIGMA_TERMUX_CODEC_VENDOR:-$HOME/.sigma/vendor/sigma-freedom-codec}"
STATE_ROOT="${SIGMA_TERMUX_CODEC_HOME:-$HOME/.sigma/semantic_codec}"

printf '%s\n' '[SIGMA] Installing Termux Semantic Codec prerequisites...'
pkg install -y python git curl

mkdir -p "$HOME/.sigma/vendor" "$STATE_ROOT/state" "$STATE_ROOT/packages" "$STATE_ROOT/logs"
chmod 700 "$HOME/.sigma" "$HOME/.sigma/vendor" "$STATE_ROOT" "$STATE_ROOT/state" "$STATE_ROOT/packages" "$STATE_ROOT/logs" 2>/dev/null || true

if [ -d "$VENDOR_ROOT/.git" ]; then
  printf '%s\n' "[SIGMA] Existing managed vendor checkout: $VENDOR_ROOT"
  if ! git -C "$VENDOR_ROOT" diff --quiet || ! git -C "$VENDOR_ROOT" diff --cached --quiet; then
    printf '%s\n' '[SIGMA] REFUSING UPDATE: managed vendor checkout has local modifications.' >&2
    printf '%s\n' '[SIGMA] Preserve them or set SIGMA_TERMUX_CODEC_VENDOR to a new directory.' >&2
    exit 2
  fi
  git -C "$VENDOR_ROOT" fetch origin "$BRANCH"
  git -C "$VENDOR_ROOT" checkout "$BRANCH"
  git -C "$VENDOR_ROOT" merge --ff-only "origin/$BRANCH"
else
  printf '%s\n' "[SIGMA] Cloning supportor tool into: $VENDOR_ROOT"
  git clone --branch "$BRANCH" --single-branch "$REPO_URL" "$VENDOR_ROOT"
fi

TOOL_DIR="$VENDOR_ROOT/SIGMA_TOOLS/SEMANTIC_CODEC/TERMUX"
if [ ! -f "$TOOL_DIR/sigma_semantic_codec_termux.py" ]; then
  printf '%s\n' "[SIGMA] TERMUX TOOL MISSING: $TOOL_DIR" >&2
  exit 3
fi

chmod 700 "$TOOL_DIR"/*.sh "$TOOL_DIR"/*.py 2>/dev/null || true
export SIGMA_TERMUX_CODEC_HOME="$STATE_ROOT"
python "$TOOL_DIR/termux_self_test.py"

printf '%s\n' '[SIGMA] INSTALL PASS'
printf '%s\n' "[SIGMA] Source: $TOOL_DIR"
printf '%s\n' "[SIGMA] State:  $STATE_ROOT"
printf '%s\n' "[SIGMA] Start:  $TOOL_DIR/start_termux.sh"
