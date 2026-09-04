#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
BRAIN="$HOME_SIGMA/sigma-freedom-write/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC="$E/SIGMA_V24_PREFLIGHT_RECURRENT_FRONTIER.sigma"
BC="$E/SIGMA_V24_PREFLIGHT_RECURRENT_FRONTIER.sigmab"

STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
RAW="$STATE/raw"

SHORT_CONTEXT=0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4
LONG_CONTEXT=d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de

SHORT_DOC="$RAW/$SHORT_CONTEXT.document"
LONG_DOC="$RAW/$LONG_CONTEXT.document"

PROD_HISTORY="$E/SIGMA_CL22_CONTEXT_RELATION_HISTORY.memory"
PROD_KNOWLEDGE="$E/SIGMA_CL22_SELECTED_KNOWLEDGE.memory"
PROD_REQUESTS="$E/SIGMA_CL22_FETCHED_REQUESTS.memory"

T_CONTEXT="$E/SIGMA_V24T_CURRENT_CONTEXT.memory"
T_INPUT="$E/SIGMA_V24T_CURRENT_EXPERIENCE.memory"
T_HISTORY="$E/SIGMA_V24T_CONTEXT_RELATION_HISTORY.memory"
T_KNOWLEDGE="$E/SIGMA_V24T_SELECTED_KNOWLEDGE.memory"
T_REQUESTS="$E/SIGMA_V24T_FETCHED_REQUESTS.memory"
T_SELECTED="$E/SIGMA_V24T_SELECTED_PATTERN.memory"
T_FETCH="$E/SIGMA_V24T_FETCH_REQUEST.memory"

LOGDIR="$STATE/log"
SHORT_LOG="$LOGDIR/V24_PREFLIGHT_SHORT.log"
LONG_LOG="$LOGDIR/V24_PREFLIGHT_LONG_d891.log"

printf 'SIGMA_PHASE=V24_STEP_LIMIT_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'PRODUCTION_MEMORY_MUTATED=NO\n'
printf 'POLICY=RECURRENT_SUPPORT_FRONTIER_ONLY\n'
printf 'ENDPOINT_LOAD_REMOVED=YES\n'
printf 'SOURCE_EXPECTED_SHA256=bbcba488e30fd22a638017195b5a7b63900a1da8fba0c3bfaf140df3628d00a7\n'

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')

printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || exit 60
[ "$actual_vm" = "$EXPECTED_VM" ] || exit 61

[ -f "$SRC" ] || {
    printf 'HOLD=V24_SOURCE_MISSING\n'
    exit 62
}

actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_source" = "bbcba488e30fd22a638017195b5a7b63900a1da8fba0c3bfaf140df3628d00a7" ] || {
    printf 'HOLD=V24_SOURCE_IDENTITY_MISMATCH\n'
    exit 63
}

for F in "$SHORT_DOC" "$LONG_DOC" "$PROD_HISTORY" "$PROD_KNOWLEDGE" "$PROD_REQUESTS"; do
    [ -f "$F" ] || {
        printf 'HOLD=MISSING_INPUT:%s\n' "$F"
        exit 64
    }
done

"$P/bin/cp" -- "$PROD_HISTORY" "$T_HISTORY" || exit 65
"$P/bin/cp" -- "$PROD_KNOWLEDGE" "$T_KNOWLEDGE" || exit 66
"$P/bin/cp" -- "$PROD_REQUESTS" "$T_REQUESTS" || exit 67
: > "$T_SELECTED"
: > "$T_FETCH"

rm -f -- "$BC" "$BC.partial"

"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?

printf 'SIGMAC_RC=%s\n' "$CRC"

[ "$CRC" -eq 0 ] || {
    printf 'HOLD=V24_PREFLIGHT_COMPILE_FAILED\n'
    exit 68
}

"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 69
"$P/bin/chmod" 0400 "$BC" || exit 70

printf 'BYTECODE_SHA256=%s\n' "$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')"

run_case() {
    NAME=$1
    CONTEXT=$2
    DOC=$3
    LOG=$4

    "$P/bin/printf" '%s' "$CONTEXT" > "$T_CONTEXT" || return 71
    "$P/bin/cp" -- "$DOC" "$T_INPUT" || return 72

    printf '\n=== V24_%s ===\n' "$NAME"

    (
        cd "$BRAIN" || exit 73
        "$VM" "$BC"
    ) >"$LOG" 2>&1

    RC=$?

    printf '%s_VM_RC=%s\n' "$NAME" "$RC"
    "$P/bin/tail" -n 25 "$LOG"

    return "$RC"
}

run_case SHORT "$SHORT_CONTEXT" "$SHORT_DOC" "$SHORT_LOG"
SHORT_RC=$?

[ "$SHORT_RC" -eq 0 ] || {
    printf 'HOLD=V24_SHORT_CONTEXT_FAILED\n'
    exit 74
}

run_case LONG_D891 "$LONG_CONTEXT" "$LONG_DOC" "$LONG_LOG"
LONG_RC=$?

[ "$LONG_RC" -eq 0 ] || {
    printf 'HOLD=V24_LONG_CONTEXT_FAILED\n'
    exit 75
}

printf '\nV24_STEP_LIMIT_PREFLIGHT=PASS\n'
printf 'SHORT_CONTEXT_RC=0\n'
printf 'PREVIOUSLY_FAILING_LONG_CONTEXT_RC=0\n'
printf 'SIGMA_C_VM_STEP_LIMIT_REPRODUCED=NO\n'
printf 'PRODUCTION_MEMORY_MUTATED=NO\n'
printf 'NEXT_ACTION=BUILD_V24_CONTINUOUS_RUNNER\n'
