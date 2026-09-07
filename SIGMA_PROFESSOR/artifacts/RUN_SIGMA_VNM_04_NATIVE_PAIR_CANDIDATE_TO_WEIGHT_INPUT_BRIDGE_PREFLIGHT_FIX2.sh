#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

PARENT_REL=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_PREFLIGHT.sh
PARENT="$REPO/$PARENT_REL"
FIX1_REL=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_PREFLIGHT_FIX1.sh
FIX1="$REPO/$FIX1_REL"

EXPECTED_PARENT_SHA256=b8cb66256a47a351339649cf9f021bfb283c8616894a25641bba93ec7cf12122
EXPECTED_FIX1_SHA256=19d51fe17a1416b0f4d08b34f5e923382d19c99e5ebd8a51c5d7866219cf525a

ROOT="$HOME_SIGMA/SIGMA_VNM_04_FIX2_RUNNER_MATERIALIZATION"
MAT="$ROOT/RUN_SIGMA_VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_PREFLIGHT_FIX2.materialized.sh"
LOCK="$ROOT/materialize.lock"

mkdir -p "$ROOT"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=VNM04_FIX2_MATERIALIZATION_ALREADY_RUNNING\n'
    exit 20
}

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

count_exact() {
    NEEDLE="$1"
    FILE="$2"
    "$P/bin/grep" -F -x "$NEEDLE" "$FILE" | "$P/bin/wc" -l | "$P/bin/awk" '{print $1}'
}

replace_exact() {
    INFILE="$1"
    OUTFILE="$2"
    OLD="$3"
    NEW="$4"
    "$P/bin/awk" -v old="$OLD" -v new="$NEW" '
        $0 == old { print new; next }
        { print }
    ' "$INFILE" > "$OUTFILE"
}

actual_parent=$(sha_of "$PARENT")
actual_fix1=$(sha_of "$FIX1")

printf 'SIGMA_PHASE=VNM04_FIX2_VARIABLE_NAMESPACE_REPAIR_WRAPPER\n'
printf 'REPAIR_CLASS=B_RUNNER_HARNESS_DEFECT\n'
printf 'DEFECT_SUBCLASS=BASH_GLOBAL_VARIABLE_NAMESPACE_COLLISION_B2_DYNAMIC_FORM_VS_VNM02_BASE_PATH\n'
printf 'FIX1_NEWLINE_ROUTING_REPAIR_RETAINED=YES\n'
printf 'NATIVE_VNM01_SOURCE_CHANGED=NO\n'
printf 'NATIVE_VNM02_SOURCE_CHANGED=NO\n'
printf 'NATIVE_VNM03_SOURCE_CHANGED=NO\n'
printf 'NATIVE_VNM04_SOURCE_CHANGED=NO\n'
printf 'COGNITIVE_POLICY_CHANGED=NO\n'
printf 'TEST_MATRIX_CHANGED=NO\n'
printf 'PASS_DEFINITION_CHANGED=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'PARENT_RUNNER_SHA256=%s\n' "$actual_parent"
printf 'FIX1_WRAPPER_SHA256=%s\n' "$actual_fix1"

[ "$actual_parent" = "$EXPECTED_PARENT_SHA256" ] || {
    printf 'HOLD=VNM04_PARENT_RUNNER_IDENTITY_MISMATCH\n'
    exit 21
}
[ "$actual_fix1" = "$EXPECTED_FIX1_SHA256" ] || {
    printf 'HOLD=VNM04_FIX1_WRAPPER_IDENTITY_MISMATCH\n'
    exit 22
}

OLD_ROUTE="    \"\$P/bin/sed\" -n '1p' \"\$V4_BUNDLE\" > \"\$V1_HYP\""
NEW_ROUTE="    \"\$P/bin/awk\" 'NR == 1 { printf \"%s\", \$0 }' \"\$V4_BUNDLE\" > \"\$V1_HYP\""

OLD_FORM='B2="hoc-${DYN_TAG_2}"'
NEW_FORM='FORM_B2="hoc-${DYN_TAG_2}"'

OLD_CASE2='build_support2_native "$A2" "$B2" "$Q1" "$Z1" "$Q2" "$Z2" T1 "SRC2-${DYN_TAG_2}-"'
NEW_CASE2='build_support2_native "$A2" "$FORM_B2" "$Q1" "$Z1" "$Q2" "$Z2" T1 "SRC2-${DYN_TAG_2}-"'

OLD_REPLAY='build_support2_native "$A2" "$B2" "$Q1" "$Z1" "$Q2" "$Z2" Z1 "REPLAY-"'
NEW_REPLAY='build_support2_native "$A2" "$FORM_B2" "$Q1" "$Z1" "$Q2" "$Z2" Z1 "REPLAY-"'

ROUTE_MATCH=$(count_exact "$OLD_ROUTE" "$PARENT")
FORM_MATCH=$(count_exact "$OLD_FORM" "$PARENT")
CASE2_MATCH=$(count_exact "$OLD_CASE2" "$PARENT")
REPLAY_MATCH=$(count_exact "$OLD_REPLAY" "$PARENT")

printf 'OLD_ROUTING_LINE_MATCH_COUNT=%s\n' "$ROUTE_MATCH"
printf 'OLD_DYNAMIC_FORM_ASSIGN_MATCH_COUNT=%s\n' "$FORM_MATCH"
printf 'OLD_CASE002_DYNAMIC_PAIR_CALL_MATCH_COUNT=%s\n' "$CASE2_MATCH"
printf 'OLD_REPLAY_DYNAMIC_PAIR_CALL_MATCH_COUNT=%s\n' "$REPLAY_MATCH"

[ "$ROUTE_MATCH" -eq 1 ] || { printf 'HOLD=VNM04_FIX2_ROUTING_LINE_MATCH_INVALID\n'; exit 23; }
[ "$FORM_MATCH" -eq 1 ] || { printf 'HOLD=VNM04_FIX2_DYNAMIC_FORM_ASSIGN_MATCH_INVALID\n'; exit 24; }
[ "$CASE2_MATCH" -eq 1 ] || { printf 'HOLD=VNM04_FIX2_CASE002_CALL_MATCH_INVALID\n'; exit 25; }
[ "$REPLAY_MATCH" -eq 2 ] || { printf 'HOLD=VNM04_FIX2_REPLAY_CALL_MATCH_INVALID\n'; exit 26; }

T1="$ROOT/step1.partial"
T2="$ROOT/step2.partial"
T3="$ROOT/step3.partial"
T4="$ROOT/step4.partial"

"$P/bin/rm" -f -- "$MAT" "$T1" "$T2" "$T3" "$T4"

replace_exact "$PARENT" "$T1" "$OLD_ROUTE" "$NEW_ROUTE" || exit 27
replace_exact "$T1" "$T2" "$OLD_FORM" "$NEW_FORM" || exit 28
replace_exact "$T2" "$T3" "$OLD_CASE2" "$NEW_CASE2" || exit 29
replace_exact "$T3" "$T4" "$OLD_REPLAY" "$NEW_REPLAY" || exit 30

"$P/bin/mv" -f -- "$T4" "$MAT" || exit 31
"$P/bin/rm" -f -- "$T1" "$T2" "$T3"
"$P/bin/chmod" 0500 "$MAT" || exit 32

"$P/bin/bash" -n "$MAT" || {
    printf 'HOLD=VNM04_FIX2_MATERIALIZED_RUNNER_BASH_SYNTAX_FAIL\n'
    exit 33
}

OLD_ROUTE_AFTER=$(count_exact "$OLD_ROUTE" "$MAT")
NEW_ROUTE_AFTER=$(count_exact "$NEW_ROUTE" "$MAT")
OLD_FORM_AFTER=$(count_exact "$OLD_FORM" "$MAT")
NEW_FORM_AFTER=$(count_exact "$NEW_FORM" "$MAT")
OLD_CASE2_AFTER=$(count_exact "$OLD_CASE2" "$MAT")
NEW_CASE2_AFTER=$(count_exact "$NEW_CASE2" "$MAT")
OLD_REPLAY_AFTER=$(count_exact "$OLD_REPLAY" "$MAT")
NEW_REPLAY_AFTER=$(count_exact "$NEW_REPLAY" "$MAT")

printf 'OLD_ROUTING_LINE_COUNT_AFTER=%s\n' "$OLD_ROUTE_AFTER"
printf 'NEW_ROUTING_LINE_COUNT_AFTER=%s\n' "$NEW_ROUTE_AFTER"
printf 'OLD_DYNAMIC_FORM_ASSIGN_COUNT_AFTER=%s\n' "$OLD_FORM_AFTER"
printf 'NEW_DYNAMIC_FORM_ASSIGN_COUNT_AFTER=%s\n' "$NEW_FORM_AFTER"
printf 'OLD_CASE002_DYNAMIC_PAIR_CALL_COUNT_AFTER=%s\n' "$OLD_CASE2_AFTER"
printf 'NEW_CASE002_DYNAMIC_PAIR_CALL_COUNT_AFTER=%s\n' "$NEW_CASE2_AFTER"
printf 'OLD_REPLAY_DYNAMIC_PAIR_CALL_COUNT_AFTER=%s\n' "$OLD_REPLAY_AFTER"
printf 'NEW_REPLAY_DYNAMIC_PAIR_CALL_COUNT_AFTER=%s\n' "$NEW_REPLAY_AFTER"

[ "$OLD_ROUTE_AFTER" -eq 0 ] || { printf 'HOLD=VNM04_FIX2_OLD_ROUTING_LINE_REMAINS\n'; exit 34; }
[ "$NEW_ROUTE_AFTER" -eq 1 ] || { printf 'HOLD=VNM04_FIX2_NEW_ROUTING_LINE_COUNT_INVALID\n'; exit 35; }
[ "$OLD_FORM_AFTER" -eq 0 ] || { printf 'HOLD=VNM04_FIX2_OLD_DYNAMIC_FORM_ASSIGN_REMAINS\n'; exit 36; }
[ "$NEW_FORM_AFTER" -eq 1 ] || { printf 'HOLD=VNM04_FIX2_NEW_DYNAMIC_FORM_ASSIGN_COUNT_INVALID\n'; exit 37; }
[ "$OLD_CASE2_AFTER" -eq 0 ] || { printf 'HOLD=VNM04_FIX2_OLD_CASE002_CALL_REMAINS\n'; exit 38; }
[ "$NEW_CASE2_AFTER" -eq 1 ] || { printf 'HOLD=VNM04_FIX2_NEW_CASE002_CALL_COUNT_INVALID\n'; exit 39; }
[ "$OLD_REPLAY_AFTER" -eq 0 ] || { printf 'HOLD=VNM04_FIX2_OLD_REPLAY_CALL_REMAINS\n'; exit 40; }
[ "$NEW_REPLAY_AFTER" -eq 2 ] || { printf 'HOLD=VNM04_FIX2_NEW_REPLAY_CALL_COUNT_INVALID\n'; exit 41; }

MAT_SHA=$(sha_of "$MAT")
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$MAT_SHA"
printf 'FIX2_DYNAMIC_FORM_B2_NAMESPACE=FORM_B2\n'
printf 'VNM02_BASE_PATH_NAMESPACE=B2_UNCHANGED\n'
printf 'FULL_REQUIRED_SUITE_RERUN=YES\n'

"$P/bin/bash" "$MAT"
RC=$?

printf '\n=== VNM04 FIX2 WRAPPER RESULT ===\n'
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$MAT_SHA"
printf 'FULL_GATE_RC=%s\n' "$RC"

exit "$RC"
