#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
RUNTIME_ROOT="$HOME/SIGMA/sigma_genesis1"
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
CHMOD="$P/bin/chmod"
RM="$P/bin/rm"

hold() {
    printf 'HOLD=%s\n' "$1"
    return "${2:-20}"
}

main() {
    for x in "$SHA" "$AWK" "$GREP" "$SED" "$CHMOD" "$RM"; do
        [ -x "$x" ] || { hold "REQUIRED_EXECUTABLE_MISSING path=$x" 20; return 20; }
    done

    [ -d "$RUNTIME_ROOT" ] || { hold "SIGMA_GENESIS1_RUNTIME_ROOT_MISSING" 21; return 21; }
    [ -f "$BASE_RUNNER" ] || { hold "BASE_ADMISSION_RUNNER_MISSING" 22; return 22; }
    [ -f "$SRC" ] || { hold "ROUTER_SOURCE_MISSING_IN_REPO_WORKTREE" 23; return 23; }

    ACTUAL_SOURCE_SHA="$($SHA "$SRC" | $AWK '{print $1}')"

    printf '=== C5 ROUTER ADMISSION FIX2 ===\n'
    printf 'ROLE=RUNTIME_REPO_PATH_SEPARATION_AND_PROVENANCE_CORRECTION\n'
    printf 'SIGMA_RUNTIME_ROOT=%s\n' "$RUNTIME_ROOT"
    printf 'REPO_ROOT=%s\n' "$REPO_ROOT"
    printf 'NATIVE_SOURCE_MODIFICATION=NO\n'
    printf 'BUILDER_MODIFICATION=NO\n'
    printf 'TEST_LOGIC_MODIFICATION=NO\n'
    printf 'PRODUCTION_BINDING=NO\n'
    printf 'NETWORK_REQUEST=NO\n'
    printf 'C5_RESTART=NO\n'
    printf 'ROUTER_SOURCE_SHA256=%s\n' "$ACTUAL_SOURCE_SHA"

    [ "$ACTUAL_SOURCE_SHA" = "$CORRECT_SOURCE_SHA" ] || {
        hold "ROUTER_SOURCE_BYTES_NOT_CORRECTED_IDENTITY" 24
        return 24
    }

    OLD_COUNT="$($GREP -F -c "$OLD_SOURCE_SHA" "$BASE_RUNNER" 2>/dev/null || true)"
    NEW_COUNT="$($GREP -F -c "$CORRECT_SOURCE_SHA" "$BASE_RUNNER" 2>/dev/null || true)"
    printf 'BASE_RUNNER_OLD_HASH_COUNT=%s\n' "$OLD_COUNT"
    printf 'BASE_RUNNER_CORRECT_HASH_COUNT=%s\n' "$NEW_COUNT"

    if [ "$OLD_COUNT" = "0" ] && [ "$NEW_COUNT" = "1" ]; then
        printf 'BASE_RUNNER_ALREADY_CORRECTED=YES\n'
        bash "$BASE_RUNNER"
        return $?
    fi

    [ "$OLD_COUNT" = "1" ] || {
        hold "STALE_HASH_OCCURRENCE_COUNT_UNEXPECTED" 25
        return 25
    }
    [ "$NEW_COUNT" = "0" ] || {
        hold "CORRECT_HASH_ALREADY_PRESENT_WITH_STALE_HASH" 26
        return 26
    }

    # Critical FIX2 rule: keep patched runner beside the original runner.
    # The admission runner derives REPO_ROOT from its own location.
    PATCHED="$SCRIPT_DIR/.RUN_C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1_ADMISSION_FIX2.$$"

    "$SED" "s/$OLD_SOURCE_SHA/$CORRECT_SOURCE_SHA/" "$BASE_RUNNER" > "$PATCHED" || {
        hold "FIX2_PATCH_FAILED" 27
        return 27
    }
    "$CHMOD" 0700 "$PATCHED" || {
        "$RM" -f -- "$PATCHED"
        hold "FIX2_CHMOD_FAILED" 28
        return 28
    }

    PATCHED_OLD_COUNT="$($GREP -F -c "$OLD_SOURCE_SHA" "$PATCHED" 2>/dev/null || true)"
    PATCHED_NEW_COUNT="$($GREP -F -c "$CORRECT_SOURCE_SHA" "$PATCHED" 2>/dev/null || true)"
    printf 'PATCHED_RUNNER_PATH=%s\n' "$PATCHED"
    printf 'PATCHED_RUNNER_OLD_HASH_COUNT=%s\n' "$PATCHED_OLD_COUNT"
    printf 'PATCHED_RUNNER_CORRECT_HASH_COUNT=%s\n' "$PATCHED_NEW_COUNT"

    if [ "$PATCHED_OLD_COUNT" != "0" ] || [ "$PATCHED_NEW_COUNT" != "1" ]; then
        "$RM" -f -- "$PATCHED"
        hold "FIX2_PATCH_IDENTITY_INVALID" 29
        return 29
    fi

    bash -n "$PATCHED" || {
        "$RM" -f -- "$PATCHED"
        hold "FIX2_PATCHED_RUNNER_BASH_SYNTAX_FAILED" 30
        return 30
    }

    printf 'RUNTIME_REPO_PATH_SEPARATION=PASS\n'
    printf 'PROVENANCE_CORRECTION_APPLIED=YES\n'
    printf 'EXECUTING_ORIGINAL_ADMISSION_LOGIC=YES\n'

    bash "$PATCHED"
    RC=$?

    "$RM" -f -- "$PATCHED"
    printf 'FIX2_WRAPPED_ADMISSION_RC=%s\n' "$RC"
    return "$RC"
}

main "$@"
