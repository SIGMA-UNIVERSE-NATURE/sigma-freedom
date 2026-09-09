#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
VM="$ROOT/native/sigma-vm.v09_candidate"
R3_BC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_29B="ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a"
EXPECTED_LIVE_CORE="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"

TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_VM_29B_SOURCE_COUPLING_R1_$$"
mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT

sha() { sha256sum "$1" | awk '{print $1}'; }
lock() {
    local p="$1" e="$2" n="$3" a
    [ -f "$p" ] || { echo "HOLD=MISSING_EXACT_PATH"; echo "PATH=$p"; exit 1; }
    a="$(sha "$p")"
    echo "${n}_PATH=$p"
    echo "${n}_SHA256=$a"
    [ "$a" = "$e" ] || { echo "${n}_IDENTITY=FAIL"; exit 1; }
    echo "${n}_IDENTITY=PASS"
}

run_vm() {
    local label="$1"
    local artifact="$2"
    local cwd="$3"
    local out="$TMP/${label}.stdout"
    local err="$TMP/${label}.stderr"
    local rc
    mkdir -p "$cwd/home" "$cwd/tmp"
    : > "$out"
    : > "$err"
    set +e
    (
        cd "$cwd"
        HOME="$cwd/home" TMPDIR="$cwd/tmp" timeout 5s "$VM" "$artifact" >"$out" 2>"$err"
    )
    rc=$?
    set -e
    echo "${label}_VM_RC=$rc"
    echo "${label}_STDOUT_BYTES=$(wc -c < "$out")"
    echo "${label}_STDERR_BYTES=$(wc -c < "$err")"
    echo "${label}_STDOUT_SHA256=$(sha "$out")"
    echo "${label}_STDERR_SHA256=$(sha "$err")"
    python - "$out" "$err" "$label" <<'PY'
from pathlib import Path
import sys
out, err, label = map(Path, sys.argv[1:3]) + [sys.argv[3]] if False else (Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3])
def esc(b):
    return b.decode('utf-8','backslashreplace').replace('\\','\\\\').replace('\n','\\n').replace('\r','\\r')
print(f"{label}_STDOUT_TEXT={esc(out.read_bytes())}")
print(f"{label}_STDERR_TEXT={esc(err.read_bytes())}")
PY
}

echo "=== C5V3 VM 29B CAPSULE SOURCE-COUPLING PROBE R1 ==="
echo "MODE=ISOLATED_VM_CAPSULE_VS_SIBLING_SOURCE_COUNTERFACTUAL"
echo "DIRECTORY_SCAN=NO"
echo "LIVE_RUNNER_EXECUTION=NO"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" "SIGMAC"
lock "$VM" "$EXPECTED_VM" "VM"
lock "$R3_BC" "$EXPECTED_29B" "CANONICAL_29B"
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" "LIVE_CORE_BEFORE"
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" "LIVE_RUNNER_BEFORE"

echo "=== 1. PREPARE TWO IDENTICAL CAPSULE PATHS WITH DIFFERENT SIBLING SOURCES ==="
NAME="SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1"
HEADER='#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]'
for C in A B NONE; do
    mkdir -p "$TMP/$C/src" "$TMP/$C/bin" "$TMP/$C/run"
    cp "$R3_BC" "$TMP/$C/bin/$NAME.sigmab"
done
printf '%s\n⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1) {\n  ⚡ print("SOURCE_A_SIDELOAD_SENTINEL");\n}\n' "$HEADER" > "$TMP/A/src/$NAME.sigma"
printf '%s\n⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1) {\n  ⚡ print("SOURCE_B_SIDELOAD_SENTINEL");\n}\n' "$HEADER" > "$TMP/B/src/$NAME.sigma"

echo "A_CAPSULE_SHA256=$(sha "$TMP/A/bin/$NAME.sigmab")"
echo "B_CAPSULE_SHA256=$(sha "$TMP/B/bin/$NAME.sigmab")"
echo "NONE_CAPSULE_SHA256=$(sha "$TMP/NONE/bin/$NAME.sigmab")"
echo "A_SOURCE_SHA256=$(sha "$TMP/A/src/$NAME.sigma")"
echo "B_SOURCE_SHA256=$(sha "$TMP/B/src/$NAME.sigma")"

run_vm "CAPSULE_WITH_SOURCE_A" "$TMP/A/bin/$NAME.sigmab" "$TMP/A/run"
run_vm "CAPSULE_WITH_SOURCE_B" "$TMP/B/bin/$NAME.sigmab" "$TMP/B/run"
run_vm "CAPSULE_WITHOUT_SOURCE" "$TMP/NONE/bin/$NAME.sigmab" "$TMP/NONE/run"

echo "=== 2. POSITIVE CONTROL: REAL EMITTED BYTECODE A/B ==="
printf '%s\n⟡(Σ.TEST) {\n  ⚡ print("BYTECODE_A_SENTINEL");\n}\n' "$HEADER" > "$TMP/bytecode_a.sigma"
printf '%s\n⟡(Σ.TEST) {\n  ⚡ print("BYTECODE_B_SENTINEL");\n}\n' "$HEADER" > "$TMP/bytecode_b.sigma"
"$SIGMAC" "$TMP/bytecode_a.sigma" "$TMP/bytecode_a.sigmab"
"$SIGMAC" "$TMP/bytecode_b.sigma" "$TMP/bytecode_b.sigmab"
echo "BYTECODE_A_SHA256=$(sha "$TMP/bytecode_a.sigmab")"
echo "BYTECODE_B_SHA256=$(sha "$TMP/bytecode_b.sigmab")"
echo "BYTECODE_A_BYTES=$(wc -c < "$TMP/bytecode_a.sigmab")"
echo "BYTECODE_B_BYTES=$(wc -c < "$TMP/bytecode_b.sigmab")"
run_vm "REAL_BYTECODE_A" "$TMP/bytecode_a.sigmab" "$TMP"
run_vm "REAL_BYTECODE_B" "$TMP/bytecode_b.sigmab" "$TMP"

echo "=== 3. CLASSIFICATION ==="
A_TEXT="$(cat "$TMP/CAPSULE_WITH_SOURCE_A.stdout")"
B_TEXT="$(cat "$TMP/CAPSULE_WITH_SOURCE_B.stdout")"
N_TEXT="$(cat "$TMP/CAPSULE_WITHOUT_SOURCE.stdout")"
PA_TEXT="$(cat "$TMP/REAL_BYTECODE_A.stdout")"
PB_TEXT="$(cat "$TMP/REAL_BYTECODE_B.stdout")"

if printf '%s' "$A_TEXT" | grep -q 'SOURCE_A_SIDELOAD_SENTINEL' && printf '%s' "$B_TEXT" | grep -q 'SOURCE_B_SIDELOAD_SENTINEL'; then
    echo "VM_SIBLING_SOURCE_COUPLING=YES"
    echo "CURRENT_29B_CLASS=SOURCE_RESOLVING_LOADER_OR_REFERENCE_CAPSULE"
elif [ "$A_TEXT" = "$B_TEXT" ] && [ "$B_TEXT" = "$N_TEXT" ]; then
    echo "VM_SIBLING_SOURCE_COUPLING=NO_OBSERVED"
    echo "CURRENT_29B_CLASS=EMPTY_OR_GENERIC_EXECUTION_CAPSULE_UNDER_TESTED_ENVIRONMENT"
else
    echo "VM_SIBLING_SOURCE_COUPLING=UNRESOLVED"
    echo "CURRENT_29B_CLASS=UNRESOLVED_EXTERNAL_DEPENDENCY"
fi

if printf '%s' "$PA_TEXT" | grep -q 'BYTECODE_A_SENTINEL' && printf '%s' "$PB_TEXT" | grep -q 'BYTECODE_B_SENTINEL'; then
    echo "VM_REAL_BYTECODE_EXECUTION_CONTROL=PASS"
else
    echo "VM_REAL_BYTECODE_EXECUTION_CONTROL=FAIL_OR_DIFFERENT_OUTPUT_CONTRACT"
fi

echo "SELF_COMPRESSION_OF_FULL_R2_R3_IN_29B=NOT_SUPPORTED_BY_CURRENT_BYTE_EVIDENCE"

echo "=== 4. NON-MUTATION RECHECK ==="
lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" "LIVE_CORE_AFTER"
lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" "LIVE_RUNNER_AFTER"
echo "PRODUCTION_MUTATION=NO"
echo "=== END ==="
