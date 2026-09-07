#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

PARENT="$REPO/SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_PREFLIGHT.sh"
EXPECTED_PARENT=ddf7cc3bcf6a4eeb94705739885961a1f15393506261dd5d8cecd56325a1355b

ROOT="$HOME_SIGMA/SIGMA_VNM_01_FIX2_RUNNER_MATERIALIZATION"
PATCHED="$ROOT/RUN_SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_PREFLIGHT_FIX2_MATERIALIZED.sh"

mkdir -p "$ROOT"

actual_parent=$("$P/bin/sha256sum" "$PARENT" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=VNM_01_FIX2_REPLAY_FINGERPRINT_HARNESS_MATERIALIZATION\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'NATIVE_SOURCE_CHANGED=NO\n'
printf 'TEST_MATRIX_CHANGED=NO\n'
printf 'PASS_DEFINITION_CHANGED=NO\n'
printf 'PARENT_RUNNER_SHA256=%s\n' "$actual_parent"

[ "$actual_parent" = "$EXPECTED_PARENT" ] || {
    printf 'HOLD=VNM01_FIX2_PARENT_RUNNER_IDENTITY_MISMATCH\n'
    exit 20
}

A_COUNT=$("$P/bin/grep" -c '^INPUT_A=' "$PARENT")
B_COUNT=$("$P/bin/grep" -c '^INPUT_B=' "$PARENT")

printf 'INPUT_A_PATCH_TARGET_COUNT=%s\n' "$A_COUNT"
printf 'INPUT_B_PATCH_TARGET_COUNT=%s\n' "$B_COUNT"

[ "$A_COUNT" -eq 1 ] || {
    printf 'HOLD=VNM01_FIX2_INPUT_A_PATCH_TARGET_COUNT_INVALID\n'
    exit 21
}

[ "$B_COUNT" -eq 1 ] || {
    printf 'HOLD=VNM01_FIX2_INPUT_B_PATCH_TARGET_COUNT_INVALID\n'
    exit 22
}

"$P/bin/rm" -f -- "$PATCHED.partial" "$PATCHED"

"$P/bin/sed" \
  -e '/^INPUT_A=/c\
INPUT_A=$(cd "$IN" && "$P/bin/sha256sum" hypothesis.memory evidence.memory | "$P/bin/sha256sum" | "$P/bin/head" -c 64)
' \
  -e '/^INPUT_B=/c\
INPUT_B=$(cd "$IN" && "$P/bin/sha256sum" hypothesis.memory evidence.memory | "$P/bin/sha256sum" | "$P/bin/head" -c 64)
' \
  "$PARENT" > "$PATCHED.partial" || exit 23

"$P/bin/bash" -n "$PATCHED.partial" || {
    printf 'HOLD=VNM01_FIX2_MATERIALIZED_RUNNER_BASH_SYNTAX_FAIL\n'
    exit 24
}

"$P/bin/mv" -f -- "$PATCHED.partial" "$PATCHED" || exit 25
"$P/bin/chmod" 0500 "$PATCHED" || exit 26

patched_sha=$("$P/bin/sha256sum" "$PATCHED" | "$P/bin/awk" '{print $1}')

printf 'PATCHED_RUNNER_PATH=%s\n' "$PATCHED"
printf 'PATCHED_RUNNER_SHA256=%s\n' "$patched_sha"
printf 'REPLAY_FINGERPRINT_POLICY=ORDERED_FIXED_BASENAME_CONTENT_HASH\n'
printf 'REPLAY_FINGERPRINT_PATH_DEPENDENT=NO\n'
printf 'FIX2_MATERIALIZATION=PASS\n'
printf 'FIX2_FULL_GATE_BEGIN=YES\n'

"$P/bin/bash" "$PATCHED"
RC=$?

printf '\n=== VNM-01 FIX2 WRAPPER RESULT ===\n'
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$patched_sha"
printf 'FULL_GATE_RC=%s\n' "$RC"

exit "$RC"
