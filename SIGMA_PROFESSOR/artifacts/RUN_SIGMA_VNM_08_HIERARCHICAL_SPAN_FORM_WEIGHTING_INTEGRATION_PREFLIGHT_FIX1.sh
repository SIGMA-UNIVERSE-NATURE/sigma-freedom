#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

PARENT_REL="SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT.sh"
VNM07_REL="SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_PREFLIGHT.sh"
PARENT="$REPO/$PARENT_REL"
VNM07="$REPO/$VNM07_REL"

EXPECTED_PARENT_GIT_BLOB=ebb17737ce9119e609ef9d83e29db4039f0ac6eb
EXPECTED_VNM07_GIT_BLOB=840d6d86e11b7bc8fc8e881ee7dc5cb26e9c5ee3
OLD_WRONG_VNM07_SHA256=ef2fe0776de85622b737a9161b4959ff4b6bba28832ac483a6a129d42463327a
CORRECT_VNM07_SHA256=53fe674e377439146078994c4ba6af3215c96bd966f470d9bbac74bc383e1921

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

blob_of() {
    git -C "$REPO" hash-object "$1"
}

printf 'SIGMA_PHASE=VNM_08_FIX1_VNM07_RUNNER_SHA256_METADATA_REPAIR\n'
printf 'REPAIR_CLASS=RUNNER_ONLY_DEPENDENCY_IDENTITY_METADATA_CORRECTION\n'
printf 'NATIVE_SOURCE_CHANGED=NO\n'
printf 'VNM07_RUNNER_BYTES_CHANGED=NO\n'
printf 'VNM08_PARENT_RUNNER_CHANGED=NO\n'
printf 'FULL_REQUIRED_SUITE_RERUN=YES\n'

[ -f "$PARENT" ] || { printf 'HOLD=VNM08_PARENT_RUNNER_MISSING\n'; exit 20; }
[ -f "$VNM07" ] || { printf 'HOLD=VNM07_RUNNER_MISSING\n'; exit 21; }

parent_blob=$(blob_of "$PARENT")
vnm07_blob=$(blob_of "$VNM07")
vnm07_sha=$(sha_of "$VNM07")

printf 'PARENT_GIT_BLOB=%s\n' "$parent_blob"
printf 'VNM07_RUNNER_GIT_BLOB=%s\n' "$vnm07_blob"
printf 'VNM07_RUNNER_SHA256=%s\n' "$vnm07_sha"

[ "$parent_blob" = "$EXPECTED_PARENT_GIT_BLOB" ] || {
    printf 'HOLD=VNM08_PARENT_RUNNER_IDENTITY_MISMATCH\n'
    exit 22
}
[ "$vnm07_blob" = "$EXPECTED_VNM07_GIT_BLOB" ] || {
    printf 'HOLD=VNM07_RUNNER_GIT_BLOB_MISMATCH\n'
    exit 23
}
[ "$vnm07_sha" = "$CORRECT_VNM07_SHA256" ] || {
    printf 'HOLD=VNM07_RUNNER_SHA256_NOT_CORRECTED_CANONICAL\n'
    exit 24
}

OLD_LINE="EXPECTED_VNM07_RUNNER=$OLD_WRONG_VNM07_SHA256"
NEW_LINE="EXPECTED_VNM07_RUNNER=$CORRECT_VNM07_SHA256"

old_count=$("$P/bin/grep" -F -x -c "$OLD_LINE" "$PARENT" || true)
new_count_before=$("$P/bin/grep" -F -x -c "$NEW_LINE" "$PARENT" || true)

printf 'OLD_METADATA_LINE_MATCH_COUNT=%s\n' "$old_count"
printf 'CORRECTED_METADATA_LINE_MATCH_COUNT_BEFORE=%s\n' "$new_count_before"

[ "$old_count" -eq 1 ] || {
    printf 'HOLD=OLD_METADATA_LINE_MATCH_COUNT_NOT_ONE\n'
    exit 25
}
[ "$new_count_before" -eq 0 ] || {
    printf 'HOLD=CORRECTED_METADATA_ALREADY_PRESENT_IN_PARENT\n'
    exit 26
}

FIXROOT="$HOME_SIGMA/SIGMA_VNM_08_FIX1_VNM07_RUNNER_SHA256_METADATA_REPAIR"
MAT="$FIXROOT/RUN_SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT_FIX1_MATERIALIZED.sh"
"$P/bin/mkdir" -p "$FIXROOT"

"$P/bin/awk" -v old="$OLD_LINE" -v new="$NEW_LINE" '
    $0 == old { print new; next }
    { print }
' "$PARENT" > "$MAT" || {
    printf 'HOLD=MATERIALIZATION_FAILED\n'
    exit 27
}

"$P/bin/chmod" 0700 "$MAT" || exit 28

old_after=$("$P/bin/grep" -F -x -c "$OLD_LINE" "$MAT" || true)
new_after=$("$P/bin/grep" -F -x -c "$NEW_LINE" "$MAT" || true)

printf 'OLD_METADATA_LINE_COUNT_AFTER=%s\n' "$old_after"
printf 'CORRECTED_METADATA_LINE_COUNT_AFTER=%s\n' "$new_after"

[ "$old_after" -eq 0 ] || {
    printf 'HOLD=OLD_METADATA_LINE_REMAINS_AFTER\n'
    exit 29
}
[ "$new_after" -eq 1 ] || {
    printf 'HOLD=CORRECTED_METADATA_LINE_COUNT_AFTER_NOT_ONE\n'
    exit 30
}

bash -n "$MAT" || {
    printf 'HOLD=MATERIALIZED_RUNNER_BASH_SYNTAX_FAIL\n'
    exit 31
}

mat_sha=$(sha_of "$MAT")
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$mat_sha"
printf 'CORRECTED_VNM07_RUNNER_SHA256=%s\n' "$CORRECT_VNM07_SHA256"
printf 'FULL_29_VM_GATE_START=YES\n'

bash "$MAT"
RC=$?

printf '\n=== VNM08 FIX1 WRAPPER RESULT ===\n'
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$mat_sha"
printf 'FULL_GATE_RC=%s\n' "$RC"

exit "$RC"
