#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
ROOT="$HOME/SIGMA/sigma_genesis1"
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." 2>/dev/null && pwd)"
BASE_RUNNER="$SCRIPT_DIR/RUN_C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1_ADMISSION.sh"
SRC="$REPO_ROOT/SIGMA_PROFESSOR/artifacts/SOURCES/C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1.sigma"

OLD_SOURCE_SHA="2285aae5efb948b073d4f62c7531f12dd8b9d5a2f01dee1401dbab74eb3cfc01"
CORRECT_SOURCE_SHA="8460912fdc63e99e576da5485929d6eff1af6afda213bb0ad7f95cd0ef7b7a0f"

SHA="$P/bin/sha256sum"
AWK="$P/bin/awk"
GREP="$P/bin/grep"
SED="$P/bin/sed"
CP="$P/bin/cp"
CHMOD="$P/bin/chmod"
MKDIR="$P/bin/mkdir"

hold() {
    printf 'HOLD=%s\n' "$1"
    return "${2:-20}"
}

for x in "$SHA" "$AWK" "$GREP" "$SED" "$CP" "$CHMOD" "$MKDIR"; do
    [ -x "$x" ] || { hold "REQUIRED_EXECUTABLE_MISSING path=$x" 20; return 20 2>/dev/null || true; }
done

[ -f "$BASE_RUNNER" ] || { hold "BASE_ADMISSION_RUNNER_MISSING" 21; return 21 2>/dev/null || true; }
[ -f "$SRC" ] || { hold "ROUTER_SOURCE_MISSING" 22; return 22 2>/dev/null || true; }

ACTUAL_SOURCE_SHA="$($SHA "$SRC" | $AWK '{print $1}')"
printf '=== C5 ROUTER ADMISSION FIX1 ===\n'
printf 'ROLE=MECHANICAL_PROVENANCE_CORRECTION_ONLY\n'
printf 'NATIVE_SOURCE_MODIFICATION=NO\n'
printf 'BUILDER_MODIFICATION=NO\n'
printf 'TEST_LOGIC_MODIFICATION=NO\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'NETWORK_REQUEST=NO\n'
printf 'C5_RESTART=NO\n'
printf 'ROUTER_SOURCE_SHA256=%s\n' "$ACTUAL_SOURCE_SHA"

[ "$ACTUAL_SOURCE_SHA" = "$CORRECT_SOURCE_SHA" ] || {
    hold "ROUTER_SOURCE_BYTES_NOT_CORRECTED_IDENTITY" 23
    return 23 2>/dev/null || true
}

OLD_COUNT="$($GREP -F -c "$OLD_SOURCE_SHA" "$BASE_RUNNER" 2>/dev/null || true)"
NEW_COUNT="$($GREP -F -c "$CORRECT_SOURCE_SHA" "$BASE_RUNNER" 2>/dev/null || true)"
printf 'BASE_RUNNER_OLD_HASH_COUNT=%s\n' "$OLD_COUNT"
printf 'BASE_RUNNER_CORRECT_HASH_COUNT=%s\n' "$NEW_COUNT"

if [ "$OLD_COUNT" = "0" ] && [ "$NEW_COUNT" = "1" ]; then
    printf 'BASE_RUNNER_ALREADY_CORRECTED=YES\n'
    "$BASE_RUNNER"
    return $? 2>/dev/null || true
fi

[ "$OLD_COUNT" = "1" ] || {
    hold "STALE_HASH_OCCURRENCE_COUNT_UNEXPECTED" 24
    return 24 2>/dev/null || true
}
[ "$NEW_COUNT" = "0" ] || {
    hold "CORRECT_HASH_ALREADY_PRESENT_WITH_STALE_HASH" 25
    return 25 2>/dev/null || true
}

FIX_ROOT="$ROOT/.sigma_admission/C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1/FIX1"
$MKDIR -p "$FIX_ROOT" || {
    hold "FIX1_DIRECTORY_CREATE_FAILED" 26
    return 26 2>/dev/null || true
}

PATCHED="$FIX_ROOT/RUN_C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1_ADMISSION_FIX1.$$"
$SED "s/$OLD_SOURCE_SHA/$CORRECT_SOURCE_SHA/" "$BASE_RUNNER" > "$PATCHED" || {
    hold "FIX1_PATCH_FAILED" 27
    return 27 2>/dev/null || true
}
$CHMOD 0700 "$PATCHED" || {
    hold "FIX1_CHMOD_FAILED" 28
    return 28 2>/dev/null || true
}

PATCHED_OLD_COUNT="$($GREP -F -c "$OLD_SOURCE_SHA" "$PATCHED" 2>/dev/null || true)"
PATCHED_NEW_COUNT="$($GREP -F -c "$CORRECT_SOURCE_SHA" "$PATCHED" 2>/dev/null || true)"
printf 'PATCHED_RUNNER_OLD_HASH_COUNT=%s\n' "$PATCHED_OLD_COUNT"
printf 'PATCHED_RUNNER_CORRECT_HASH_COUNT=%s\n' "$PATCHED_NEW_COUNT"

[ "$PATCHED_OLD_COUNT" = "0" ] || {
    hold "FIX1_STALE_HASH_REMAINS" 29
    return 29 2>/dev/null || true
}
[ "$PATCHED_NEW_COUNT" = "1" ] || {
    hold "FIX1_CORRECT_HASH_COUNT_INVALID" 30
    return 30 2>/dev/null || true
}

printf 'PROVENANCE_CORRECTION_APPLIED=YES\n'
printf 'EXECUTING_ORIGINAL_ADMISSION_LOGIC=YES\n'
"$PATCHED"
RC=$?
printf 'FIX1_WRAPPED_ADMISSION_RC=%s\n' "$RC"
return "$RC" 2>/dev/null || true
