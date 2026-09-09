#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_R4_SUCCESSOR_COMPOSE_FIX1_$$"
mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT

ORIGINAL_COMMIT="5b97501a3f9f84e690d4bc57caa09242ddb25e6e"
ORIGINAL_URL="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/$ORIGINAL_COMMIT/C5_M5/RUN_C5V3_R4_SUCCESSOR_T1_T2_T3_COMPOSE_COMPILE_R1.sh"
SCRIPT="$TMP/original.sh"
FIXED="$TMP/fixed.sh"

OLD_GATEA="986465097126d33598ebb83ec9f0af331eadb3a2443f9605dded3a1e4ab04d52"
OLD_T123="8b6f231a23c2ab5cd19e2ba2806ced29e9ed6bb8c9590c0559e9532a9feb7d06"
NEW_GATEA="4d0ea071c5844938ccc264afbd76494e21279655988ad95f6bdd2842d989cb64"
NEW_T123="f48552534f2e5690b2b79a7a913cd2b5d376c13ba401b251eff63190820a8e07"

curl -fsSL "$ORIGINAL_URL" -o "$SCRIPT"

[ "$(grep -Foc "$OLD_GATEA" "$SCRIPT")" = "1" ] || { echo "HOLD=ORIGINAL_GATEA_CONSTANT_COUNT"; exit 1; }
[ "$(grep -Foc "$OLD_T123" "$SCRIPT")" = "1" ] || { echo "HOLD=ORIGINAL_T123_CONSTANT_COUNT"; exit 1; }

sed \
  -e "s/$OLD_GATEA/$NEW_GATEA/" \
  -e "s/$OLD_T123/$NEW_T123/" \
  "$SCRIPT" > "$FIXED"

[ "$(grep -Foc "$NEW_GATEA" "$FIXED")" = "1" ] || { echo "HOLD=FIXED_GATEA_CONSTANT_COUNT"; exit 1; }
[ "$(grep -Foc "$NEW_T123" "$FIXED")" = "1" ] || { echo "HOLD=FIXED_T123_CONSTANT_COUNT"; exit 1; }
[ "$(grep -Foc "$OLD_GATEA" "$FIXED")" = "0" ] || { echo "HOLD=OLD_GATEA_CONSTANT_REMAINS"; exit 1; }
[ "$(grep -Foc "$OLD_T123" "$FIXED")" = "0" ] || { echo "HOLD=OLD_T123_CONSTANT_REMAINS"; exit 1; }

echo "=== C5V3 R4 SUCCESSOR COMPOSE / COMPILE R1 FIX1 ==="
echo "FIX_SCOPE=HARNESS_DONOR_NORMALIZED_IDENTITY_CONSTANTS_ONLY"
echo "SOURCE_MODULE_MUTATION=NO"
echo "GATEA_PURE_EXPECTED_SHA256=$NEW_GATEA"
echo "T1_T2_T3_EXPECTED_SHA256=$NEW_T123"
echo "VM_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"

exec bash "$FIXED" "$ROOT"
