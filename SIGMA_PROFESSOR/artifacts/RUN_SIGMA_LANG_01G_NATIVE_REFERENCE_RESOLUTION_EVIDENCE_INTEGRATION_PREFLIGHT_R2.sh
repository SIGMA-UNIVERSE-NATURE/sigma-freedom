#!/data/data/com.termux/files/usr/bin/bash
set -eu
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

BASE_RUNNER="$REPO/SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_PREFLIGHT.sh"
SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigma"

EXPECTED_BASE_RUNNER=d5f7ae2561a3f1955a9375f5eb855a133c9a9e5c7dd176064b01b7eff12035e2
EXPECTED_SOURCE=33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087
OLD_RECORDED_SOURCE=21219f66fc7970615d9a98647bfc63229780390bfa993730e2e326b3c493ee0e

ROOT="$HOME_SIGMA/SIGMA_LANG_01G_REFERENCE_EVIDENCE_INTEGRATION_V1_PREFLIGHT"
PATCHED="$ROOT/RUN_SIGMA_LANG_01G_PREFLIGHT_R2_PATCHED.sh"

mkdir -p "$ROOT"

actual_base=$("$P/bin/sha256sum" "$BASE_RUNNER" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=LANG_01G_RUNNER_IDENTITY_REPAIR_R2\n'
printf 'REPAIR_CLASS=RUNNER_ONLY_ARTIFACT_IDENTITY_METADATA\n'
printf 'NATIVE_SOURCE_CHANGED=NO\n'
printf 'COGNITIVE_POLICY_CHANGED=NO\n'
printf 'ORACLE_CASES_CHANGED=NO\n'
printf 'HOST_COGNITION=NO\n'
printf 'BASE_RUNNER_SHA256=%s\n' "$actual_base"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_base" = "$EXPECTED_BASE_RUNNER" ] || {
    printf 'HOLD=LANG_01G_BASE_RUNNER_IDENTITY_MISMATCH\n'
    exit 30
}

[ "$actual_source" = "$EXPECTED_SOURCE" ] || {
    printf 'HOLD=LANG_01G_SOURCE_IDENTITY_MISMATCH\n'
    exit 31
}

old_count=$("$P/bin/grep" -F -x -c "EXPECTED_SOURCE=$OLD_RECORDED_SOURCE" "$BASE_RUNNER" || true)
[ "$old_count" -eq 1 ] || {
    printf 'HOLD=LANG_01G_OLD_SOURCE_PIN_OCCURRENCE_NOT_EXACTLY_ONE\n'
    exit 32
}

"$P/bin/sed" \
    "s/^EXPECTED_SOURCE=$OLD_RECORDED_SOURCE$/EXPECTED_SOURCE=$EXPECTED_SOURCE/" \
    "$BASE_RUNNER" > "$PATCHED"

new_count=$("$P/bin/grep" -F -x -c "EXPECTED_SOURCE=$EXPECTED_SOURCE" "$PATCHED" || true)
old_after=$("$P/bin/grep" -F -x -c "EXPECTED_SOURCE=$OLD_RECORDED_SOURCE" "$PATCHED" || true)

[ "$new_count" -eq 1 ] || {
    printf 'HOLD=LANG_01G_CORRECTED_SOURCE_PIN_OCCURRENCE_NOT_EXACTLY_ONE\n'
    exit 33
}

[ "$old_after" -eq 0 ] || {
    printf 'HOLD=LANG_01G_OLD_SOURCE_PIN_REMAINS_AFTER_REPAIR\n'
    exit 34
}

"$P/bin/chmod" 0700 "$PATCHED"
printf 'PATCHED_RUNNER_SHA256='
"$P/bin/sha256sum" "$PATCHED" | "$P/bin/awk" '{print $1}'
printf 'RUNNER_IDENTITY_REPAIR=PASS\n'

exec "$P/bin/bash" "$PATCHED"
