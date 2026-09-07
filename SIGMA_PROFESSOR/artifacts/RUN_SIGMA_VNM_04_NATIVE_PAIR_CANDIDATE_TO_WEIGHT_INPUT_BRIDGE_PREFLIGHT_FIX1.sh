#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

PARENT_REL=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_PREFLIGHT.sh
PARENT="$REPO/$PARENT_REL"
EXPECTED_PARENT_SHA256=b8cb66256a47a351339649cf9f021bfb283c8616894a25641bba93ec7cf12122

ROOT="$HOME_SIGMA/SIGMA_VNM_04_FIX1_RUNNER_MATERIALIZATION"
MAT="$ROOT/RUN_SIGMA_VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_PREFLIGHT_FIX1.materialized.sh"
LOCK="$ROOT/materialize.lock"

mkdir -p "$ROOT"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=VNM04_FIX1_MATERIALIZATION_ALREADY_RUNNING\n'
    exit 20
}

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

actual_parent=$(sha_of "$PARENT")

printf 'SIGMA_PHASE=VNM04_FIX1_NEWLINE_FREE_HYPOTHESIS_ROUTING_WRAPPER\n'
printf 'REPAIR_CLASS=B_RUNNER_HARNESS_DEFECT\n'
printf 'NATIVE_VNM01_SOURCE_CHANGED=NO\n'
printf 'NATIVE_VNM04_SOURCE_CHANGED=NO\n'
printf 'COGNITIVE_POLICY_CHANGED=NO\n'
printf 'TEST_MATRIX_CHANGED=NO\n'
printf 'PASS_DEFINITION_CHANGED=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'PARENT_RUNNER_SHA256=%s\n' "$actual_parent"

[ "$actual_parent" = "$EXPECTED_PARENT_SHA256" ] || {
    printf 'HOLD=VNM04_PARENT_RUNNER_IDENTITY_MISMATCH\n'
    exit 21
}

OLD_LINE="    \"\$P/bin/sed\" -n '1p' \"\$V4_BUNDLE\" > \"\$V1_HYP\""
NEW_LINE="    \"\$P/bin/awk\" 'NR == 1 { printf \"%s\", \$0 }' \"\$V4_BUNDLE\" > \"\$V1_HYP\""

MATCH_COUNT=$("$P/bin/grep" -F -x "$OLD_LINE" "$PARENT" | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
printf 'OLD_ROUTING_LINE_MATCH_COUNT=%s\n' "$MATCH_COUNT"
[ "$MATCH_COUNT" -eq 1 ] || {
    printf 'HOLD=VNM04_FIX1_PARENT_ROUTING_LINE_NOT_UNIQUE\n'
    exit 22
}

LINE_NO=$("$P/bin/grep" -n -F -x "$OLD_LINE" "$PARENT" | "$P/bin/awk" -F: 'NR == 1 {print $1}')
[ -n "$LINE_NO" ] || {
    printf 'HOLD=VNM04_FIX1_PARENT_ROUTING_LINE_NOT_FOUND\n'
    exit 23
}

"$P/bin/rm" -f -- "$MAT.partial" "$MAT"

if [ "$LINE_NO" -gt 1 ]; then
    "$P/bin/head" -n "$((LINE_NO - 1))" "$PARENT" > "$MAT.partial" || exit 24
else
    : > "$MAT.partial"
fi

printf '%s\n' "$NEW_LINE" >> "$MAT.partial"
"$P/bin/tail" -n "+$((LINE_NO + 1))" "$PARENT" >> "$MAT.partial" || exit 25

"$P/bin/mv" -f -- "$MAT.partial" "$MAT" || exit 26
"$P/bin/chmod" 0500 "$MAT" || exit 27

"$P/bin/bash" -n "$MAT" || {
    printf 'HOLD=VNM04_FIX1_MATERIALIZED_RUNNER_BASH_SYNTAX_FAIL\n'
    exit 28
}

OLD_AFTER=$("$P/bin/grep" -F -x "$OLD_LINE" "$MAT" | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')
NEW_AFTER=$("$P/bin/grep" -F -x "$NEW_LINE" "$MAT" | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}')

printf 'OLD_ROUTING_LINE_COUNT_AFTER=%s\n' "$OLD_AFTER"
printf 'NEW_ROUTING_LINE_COUNT_AFTER=%s\n' "$NEW_AFTER"

[ "$OLD_AFTER" -eq 0 ] || {
    printf 'HOLD=VNM04_FIX1_OLD_ROUTING_LINE_REMAINS\n'
    exit 29
}
[ "$NEW_AFTER" -eq 1 ] || {
    printf 'HOLD=VNM04_FIX1_NEW_ROUTING_LINE_COUNT_INVALID\n'
    exit 30
}

MAT_SHA=$(sha_of "$MAT")
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$MAT_SHA"
printf 'FIX1_ROUTING_POLICY=FIRST_BUNDLE_RECORD_WITHOUT_RECORD_SEPARATOR_NEWLINE\n'
printf 'FULL_REQUIRED_SUITE_RERUN=YES\n'

"$P/bin/bash" "$MAT"
RC=$?

printf '\n=== VNM04 FIX1 WRAPPER RESULT ===\n'
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$MAT_SHA"
printf 'FULL_GATE_RC=%s\n' "$RC"

exit "$RC"
