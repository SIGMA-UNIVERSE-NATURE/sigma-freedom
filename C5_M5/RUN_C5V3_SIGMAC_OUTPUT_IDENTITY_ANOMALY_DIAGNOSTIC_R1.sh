#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
SIGMAC="$ROOT/native/sigmac"
R2_SRC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R2/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
R2_BC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R2/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
R3_SRC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
R3_BC="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_R2_SRC="d7d1153fd6979dff7d119bb5e8187f045b9f8af62e51065cccf95265478fc3a0"
EXPECTED_R3_SRC="152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8"
EXPECTED_SHARED_BC="ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a"

TMP="${TMPDIR:-/data/data/com.termux/files/usr/tmp}/C5V3_SIGMAC_IDENTITY_DIAG_R1_$$"
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

compile_one() {
    local src="$1" out="$2" label="$3" rc
    rm -f "$out"
    set +e
    "$SIGMAC" "$src" "$out"
    rc=$?
    set -e
    echo "${label}_RC=$rc"
    if [ "$rc" -eq 0 ] && [ -s "$out" ]; then
        echo "${label}_SHA256=$(sha "$out")"
        echo "${label}_BYTES=$(wc -c < "$out")"
    else
        echo "${label}_OUTPUT=ABSENT_OR_EMPTY"
    fi
    return "$rc"
}

echo "=== C5V3 SIGMAC OUTPUT IDENTITY ANOMALY DIAGNOSTIC R1 ==="
echo "MODE=EXACT_PATH_FRESH_RECOMPILE_COUNTERFACTUAL_NEGATIVE_CONTROL"
echo "DIRECTORY_SCAN=NO"
echo "VM_EXECUTION=NO"
echo "CORE_EXECUTION=NO"
echo "PRODUCTION_MUTATION=NO"

lock "$SIGMAC" "$EXPECTED_SIGMAC" "LOCKED_SIGMAC"
lock "$R2_SRC" "$EXPECTED_R2_SRC" "R2_SOURCE"
lock "$R3_SRC" "$EXPECTED_R3_SRC" "R3_FIX1_SOURCE"
lock "$R2_BC" "$EXPECTED_SHARED_BC" "R2_FROZEN_BYTECODE"
lock "$R3_BC" "$EXPECTED_SHARED_BC" "R3_FIX1_FROZEN_BYTECODE"

echo "=== 1. SOURCE STRUCTURE DIFFERENCE ==="
python - "$R2_SRC" "$R3_SRC" <<'PY'
from pathlib import Path
import hashlib, re, sys
for label, path in (("R2", sys.argv[1]), ("R3_FIX1", sys.argv[2])):
    text = Path(path).read_text()
    main_i = text.find("⟡(")
    if main_i < 0:
        raise SystemExit("HOLD=MAIN_BLOCK_NOT_FOUND:" + label)
    main = text[main_i:]
    print(f"{label}_SOURCE_BYTES={len(text.encode())}")
    print(f"{label}_DEF_COUNT={len(re.findall(r'^DEF\\s+', text, flags=re.M))}")
    print(f"{label}_MAIN_SHA256={hashlib.sha256(main.encode()).hexdigest()}")
PY
if cmp -s "$R2_SRC" "$R3_SRC"; then
    echo "R2_R3_SOURCE_BYTE_IDENTICAL=YES"
    echo "HOLD=SOURCE_IDENTITY_ASSUMPTION_BROKEN"
    exit 1
else
    echo "R2_R3_SOURCE_BYTE_IDENTICAL=NO"
    echo "R2_R3_SOURCE_DISTINCT=PASS"
fi

if cmp -s "$R2_BC" "$R3_BC"; then
    echo "R2_R3_FROZEN_BYTECODE_BYTE_IDENTICAL=YES"
else
    echo "R2_R3_FROZEN_BYTECODE_BYTE_IDENTICAL=NO"
fi

echo "=== 2. FRESH RECOMPILE BOTH SOURCES ==="
R2_FRESH="$TMP/r2_fresh.sigmab"
R3_FRESH="$TMP/r3_fresh.sigmab"
compile_one "$R2_SRC" "$R2_FRESH" "R2_FRESH_COMPILE" || { echo "RESULT=HOLD_R2_FRESH_COMPILE_FAILED"; exit 1; }
compile_one "$R3_SRC" "$R3_FRESH" "R3_FIX1_FRESH_COMPILE" || { echo "RESULT=HOLD_R3_FRESH_COMPILE_FAILED"; exit 1; }

R2_FRESH_SHA="$(sha "$R2_FRESH")"
R3_FRESH_SHA="$(sha "$R3_FRESH")"
if cmp -s "$R2_FRESH" "$R3_FRESH"; then
    echo "R2_R3_FRESH_BYTECODE_BYTE_IDENTICAL=YES"
else
    echo "R2_R3_FRESH_BYTECODE_BYTE_IDENTICAL=NO"
fi

echo "=== 3. OBSERVABLE MAIN-LITERAL COUNTERFACTUAL ==="
R3_MUT="$TMP/r3_main_literal_mutation.sigma"
R3_MUT_BC="$TMP/r3_main_literal_mutation.sigmab"
python - "$R3_SRC" "$R3_MUT" <<'PY'
from pathlib import Path
import sys
src, out = sys.argv[1:]
text = Path(src).read_text()
old = '⚡ STATUS: "TRUST_ENVELOPE_NOT_ADMITTED";'
new = '⚡ STATUS: "TRUST_ENVELOPE_NOT_ADMITTED_COUNTERFACTUAL_R3_FIX1";'
count = text.count(old)
print("COUNTERFACTUAL_TARGET_COUNT=" + str(count))
if count != 1:
    raise SystemExit("HOLD=COUNTERFACTUAL_TARGET_COUNT_NOT_ONE")
Path(out).write_text(text.replace(old, new, 1))
PY
compile_one "$R3_MUT" "$R3_MUT_BC" "R3_COUNTERFACTUAL_COMPILE" || { echo "RESULT=HOLD_COUNTERFACTUAL_COMPILE_FAILED"; exit 1; }
R3_MUT_SHA="$(sha "$R3_MUT_BC")"
if cmp -s "$R3_FRESH" "$R3_MUT_BC"; then
    echo "R3_COUNTERFACTUAL_BYTECODE_CHANGED=NO"
else
    echo "R3_COUNTERFACTUAL_BYTECODE_CHANGED=YES"
fi

echo "=== 4. NEGATIVE PARSER CONTROL: REMOVE FINAL MAIN BRACE ==="
R3_BAD="$TMP/r3_unbalanced_main_negative_control.sigma"
R3_BAD_BC="$TMP/r3_unbalanced_main_negative_control.sigmab"
python - "$R3_SRC" "$R3_BAD" <<'PY'
from pathlib import Path
import sys
src, out = sys.argv[1:]
text = Path(src).read_text()
trim = text.rstrip()
if not trim.endswith('}'):
    raise SystemExit("HOLD=NEGATIVE_CONTROL_FINAL_BRACE_NOT_FOUND")
trim = trim[:-1]
Path(out).write_text(trim + "\n")
print("NEGATIVE_CONTROL_CREATED=YES")
PY
set +e
"$SIGMAC" "$R3_BAD" "$R3_BAD_BC"
BAD_RC=$?
set -e
echo "R3_NEGATIVE_UNBALANCED_COMPILE_RC=$BAD_RC"
if [ "$BAD_RC" -ne 0 ]; then
    echo "R3_NEGATIVE_UNBALANCED_REJECTED=YES"
else
    echo "R3_NEGATIVE_UNBALANCED_REJECTED=NO"
    if [ -s "$R3_BAD_BC" ]; then
        echo "R3_NEGATIVE_UNBALANCED_BYTECODE_SHA256=$(sha "$R3_BAD_BC")"
    fi
fi

echo "=== 5. DIAGNOSTIC CLASSIFICATION ==="
if [ "$R2_FRESH_SHA" != "$R3_FRESH_SHA" ]; then
    echo "FRESH_R2_R3_BYTECODE_DISTINCT=YES"
    echo "RESULT=HOLD_PREVIOUS_BYTECODE_FREEZE_OR_PATH_RECONCILIATION_REQUIRED"
    exit 0
fi

echo "FRESH_R2_R3_BYTECODE_DISTINCT=NO"
if [ "$R3_MUT_SHA" = "$R3_FRESH_SHA" ]; then
    echo "COMPILER_MAIN_LITERAL_SENSITIVITY=FAIL"
    echo "RESULT=HOLD_COMPILER_OUTPUT_INSENSITIVE_TO_OBSERVABLE_MAIN_COUNTERFACTUAL"
    exit 0
fi

echo "COMPILER_MAIN_LITERAL_SENSITIVITY=PASS"
if [ "$BAD_RC" -eq 0 ]; then
    echo "COMPILER_NEGATIVE_SYNTAX_CONTROL=FAIL"
    echo "RESULT=HOLD_COMPILER_ACCEPTS_UNBALANCED_MAIN_NEGATIVE_CONTROL"
    exit 0
fi

echo "COMPILER_NEGATIVE_SYNTAX_CONTROL=PASS"
echo "RESULT=HOLD_R2_R3_DISTINCT_MAIN_SOURCES_COMPILE_TO_IDENTICAL_BYTECODE_UNEXPLAINED"
echo "=== END ==="
