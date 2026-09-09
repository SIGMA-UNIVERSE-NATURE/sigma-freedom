#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
BUNDLE="${2:-}"

EXPECTED_R6="dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac"
EXPECTED_BUNDLE="ff3fced4c16bf3866e30853e01f5bb634a87ac25943ba612a3cdf1cdf2708494"
EXPECTED_M5_PARENT="bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1"
EXPECTED_P0_MODULE="7b7b615c496966fa2e144e88c1591272cc9b3a9a3ffc17146e988d6e68637912"
EXPECTED_P0_MAIN="d8c9cf8c796c1db3b77a608b81c04cee089aba8a1970f0a2d07613255d71bad9"
EXPECTED_COG_MODULE="4d0ea071c5844938ccc264afbd76494e21279655988ad95f6bdd2842d989cb64"
EXPECTED_TOOL_MODULE="f48552534f2e5690b2b79a7a913cd2b5d376c13ba401b251eff63190820a8e07"
EXPECTED_R3_FIX1_SOURCE="5da5c90bf9483a83b2166a606d0e2b4ed0a47c1fec90dd29b381e637c12761e3"
EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_LIVE_CORE="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"

R6="$ROOT/.sigma_c5v3_sync/OFFLINE_PRODUCTION_LINEAGE_LATENT_GRAFT_R6_20260909T184734/candidate/core.sigma"
SIGMAC="$ROOT/native/sigmac"
VM="$ROOT/native/sigma-vm.v09_candidate"
LIVE_CORE="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"

OUTROOT="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R3_FIX1_TRUST_FIRST"
MOD="$OUTROOT/modules"
SRC_DIR="$OUTROOT/src"
BIN_DIR="$OUTROOT/bin"
mkdir -p "$MOD" "$SRC_DIR" "$BIN_DIR"

P0="$MOD/C5_P0_TRUST_STATE_R1.sigma.inc"
MAIN="$MOD/C5_R3_FIX1_TRUST_FIRST_MAIN_R1.sigma.inc"
COG="$MOD/C5_M5_PROVISIONAL_TRUTH_PURE_DONOR.sigma.inc"
TOOLS="$MOD/C5_T1_T2_T3_R6_EXACT_DONOR.sigma.inc"
M5_PARENT="$MOD/M5_PROVISIONAL_TRUTH_parent.sigma"
FINAL="$SRC_DIR/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
BYTECODE="$BIN_DIR/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"

RAW_BASE="https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/4fb2257844a35bd496d213b657f24773fb20982f"

echo "=== C5V3 CORE REWRITE R3 FIX1 TRUST-FIRST BUILD COMPILE R1 ==="
echo "ROOT=$ROOT"
echo "MODE=DETERMINISTIC_TRUST_FIRST_COMPOSITION_AND_COMPILE"
echo "EXACT_PATHS_ONLY=YES"
echo "DIRECTORY_SCAN=NO"
echo "VM_EXECUTION=NO"
echo "CORE_EXECUTION=NO"
echo "LIVE_CORE_WRITE=NO"
echo "LIVE_RUNNER_WRITE=NO"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"

if [ -z "$BUNDLE" ]; then
    for C in \
        "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip" \
        "/sdcard/Download/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip" \
        "$HOME/SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE(1).zip"
    do
        if [ -f "$C" ]; then
            BUNDLE="$C"
            break
        fi
    done
fi

[ -n "$BUNDLE" ] && [ -f "$BUNDLE" ] || {
    echo "HOLD=PROVISIONAL_TRUTH_BUNDLE_NOT_FOUND"
    exit 1
}

for F in "$R6" "$SIGMAC" "$VM" "$LIVE_CORE" "$LIVE_RUNNER"; do
    [ -f "$F" ] || {
        echo "HOLD=MISSING_EXACT_REQUIRED_PATH"
        echo "PATH=$F"
        exit 1
    }
done

sha_lock() {
    local path="$1"
    local expected="$2"
    local label="$3"
    local actual
    actual="$(sha256sum "$path" | awk '{print $1}')"
    echo "${label}_PATH=$path"
    echo "${label}_SHA256=$actual"
    [ "$actual" = "$expected" ] || {
        echo "${label}_IDENTITY=FAIL"
        exit 1
    }
    echo "${label}_IDENTITY=PASS"
}

echo "=== 1. INPUT IDENTITY LOCKS ==="
sha_lock "$R6" "$EXPECTED_R6" "R6_SOURCE"
sha_lock "$BUNDLE" "$EXPECTED_BUNDLE" "M5_BUNDLE"
sha_lock "$SIGMAC" "$EXPECTED_SIGMAC" "LOCKED_SIGMAC"
sha_lock "$VM" "$EXPECTED_VM" "LOCKED_VM"
sha_lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" "LIVE_CORE"
sha_lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" "LIVE_RUNNER"

echo "=== 2. FETCH EXACT P0 MODULES ==="
curl -fsSL "$RAW_BASE/C5_M5/R3_FIX1/C5_P0_TRUST_STATE_R1.sigma.inc" -o "$P0"
curl -fsSL "$RAW_BASE/C5_M5/R3_FIX1/C5_R3_FIX1_TRUST_FIRST_MAIN_R1.sigma.inc" -o "$MAIN"
sha_lock "$P0" "$EXPECTED_P0_MODULE" "P0_MODULE"
sha_lock "$MAIN" "$EXPECTED_P0_MAIN" "P0_MAIN"

echo "=== 3. EXTRACT EXACT ADMITTED COGNITION PARENT ==="
python - "$BUNDLE" "$M5_PARENT" "$EXPECTED_M5_PARENT" <<'PY'
import hashlib, sys, zipfile
bundle, out, expected = sys.argv[1:]
with zipfile.ZipFile(bundle) as z:
    candidates = [n for n in z.namelist()
                  if n.endswith("/SIGMA_C5_C5V3_M5_NATIVE_SCOPED_PROVISIONAL_EPISTEMIC_TRUTH_R1/core.sigma")]
    if len(candidates) != 1:
        raise SystemExit("HOLD=EXACT_M5_PARENT_MEMBER_COUNT_NOT_ONE")
    data = z.read(candidates[0])
actual = hashlib.sha256(data).hexdigest()
print("M5_PARENT_MEMBER=" + candidates[0])
print("M5_PARENT_SHA256=" + actual)
if actual != expected:
    raise SystemExit("HOLD=M5_PARENT_IDENTITY_MISMATCH")
open(out, "wb").write(data)
print("M5_PARENT_IDENTITY=PASS")
PY

echo "=== 4. DETERMINISTIC DONOR EXTRACTION + COMPOSITION ==="
python - "$M5_PARENT" "$R6" "$P0" "$MAIN" "$COG" "$TOOLS" "$FINAL" \
    "$EXPECTED_COG_MODULE" "$EXPECTED_TOOL_MODULE" "$EXPECTED_R3_FIX1_SOURCE" <<'PY'
from pathlib import Path
import hashlib, re, sys

m5_path, r6_path, p0_path, main_path, cog_out, tools_out, final_out, exp_cog, exp_tools, exp_final = sys.argv[1:]
m5 = Path(m5_path).read_text()
r6 = Path(r6_path).read_text()
p0 = Path(p0_path).read_text()
main = Path(main_path).read_text()

def defs(text):
    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r'^DEF\s+([A-Za-z0-9_]+)\s*\(', lines[i])
        if not m:
            i += 1
            continue
        name = m.group(1)
        s = ''.join(lines[i:])
        brace = s.find('{')
        if brace < 0:
            raise SystemExit("HOLD=DEF_OPEN_BRACE_MISSING:" + name)
        depth = 0
        in_str = False
        esc = False
        end = None
        for j in range(brace, len(s)):
            ch = s[j]
            if in_str:
                if esc:
                    esc = False
                elif ch == '\\':
                    esc = True
                elif ch == '"':
                    in_str = False
            else:
                if ch == '"':
                    in_str = True
                elif ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        end = j + 1
                        break
        if end is None:
            raise SystemExit("HOLD=DEF_UNBALANCED:" + name)
        body = s[:end]
        out.append((name, body))
        i += body.count('\n') + 1
    return out

m5_defs = defs(m5)
r6_defs = defs(r6)

if len(m5_defs) != 78:
    raise SystemExit(f"HOLD=M5_DEF_COUNT:{len(m5_defs)}")
if len(r6_defs) != 156:
    raise SystemExit(f"HOLD=R6_DEF_COUNT:{len(r6_defs)}")

# append_line is the only Gate-A DEF that directly mutates persistent state.
pure_m5 = [(n,b) for n,b in m5_defs if n != "append_line"]
if len(pure_m5) != 77:
    raise SystemExit(f"HOLD=PURE_M5_DEF_COUNT:{len(pure_m5)}")
if any('"write_text"' in b or '"read_text"' in b for n,b in pure_m5):
    raise SystemExit("HOLD=PURE_M5_HAS_DIRECT_IO")

# R6 exact layout proven by prior admission: 63 old M5-only, 82 admitted tools, 11 production mechanics.
tools = r6_defs[63:145]
if len(tools) != 82:
    raise SystemExit(f"HOLD=TOOL_DEF_COUNT:{len(tools)}")
if tools[0][0] != "WA_H" or tools[-1][0] != "T2_SHORTEST_PATH_BOUNDED":
    raise SystemExit("HOLD=TOOL_BOUNDARY_IDENTITY")
if any('"write_text"' in b or '"read_text"' in b for n,b in tools):
    raise SystemExit("HOLD=TOOL_DONOR_HAS_DIRECT_IO")

cog = "\n\n".join(b.rstrip() for _,b in pure_m5) + "\n"
tool_text = "\n\n".join(b.rstrip() for _,b in tools) + "\n"
Path(cog_out).write_text(cog)
Path(tools_out).write_text(tool_text)

def sha(s): return hashlib.sha256(s.encode()).hexdigest()

print("COGNITION_DONOR_DEF_COUNT=77")
print("COGNITION_DONOR_SHA256=" + sha(cog))
if sha(cog) != exp_cog:
    raise SystemExit("HOLD=COGNITION_DONOR_HASH_MISMATCH")
print("COGNITION_DONOR_IDENTITY=PASS")

print("T1_T2_T3_TOOL_DEF_COUNT=82")
print("T1_T2_T3_TOOL_MODULE_SHA256=" + sha(tool_text))
if sha(tool_text) != exp_tools:
    raise SystemExit("HOLD=TOOL_MODULE_HASH_MISMATCH")
print("T1_T2_T3_TOOL_IDENTITY=PASS")

header = "#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]\n\n"
intro = (
    "# C5V3 R3 FIX1 TRUST-FIRST SAME-IDENTITY CORE\n"
    "# Status: SOURCE CONSTRUCTION / NOT ADMITTED / NOT PRODUCTION-BOUND\n"
    "# P0 active: fresh invocation envelope, authoritative state-chain binding,\n"
    "# receipt-bound event inputs, staged readback, atomic-commit intent only.\n"
    "# P1 donor cognition is present as pure DEF material but not trusted to mutate\n"
    "# persistent state directly. P2 T1/T2/T3 exact admitted DEF bodies are present\n"
    "# but require explicit native activation under the trusted transaction contract.\n\n"
)
final = header + intro + p0 + "\n" + cog + "\n" + tool_text + "\n" + main
Path(final_out).write_text(final)

final_defs = defs(final)
print("R3_FIX1_DEF_COUNT=" + str(len(final_defs)))
if len(final_defs) != 176:
    raise SystemExit("HOLD=R3_FIX1_DEF_COUNT")

actual = sha(final)
print("R3_FIX1_SOURCE_SHA256=" + actual)
if actual != exp_final:
    raise SystemExit("HOLD=R3_FIX1_SOURCE_HASH_MISMATCH")

if final.count("#SIGMAUNIVERSE_LANGUAGE") != 1:
    raise SystemExit("HOLD=HEADER_COUNT")
if final.count("⟡(") != 1:
    raise SystemExit("HOLD=MAIN_COUNT")
if 'legacy_analyze_segment' in final or 'legacy_merge_evidence' in final:
    raise SystemExit("HOLD=LEGACY_COGNITION_PRESENT")
if 'LEFT=' in final or 'RIGHT=' in final:
    raise SystemExit("HOLD=LEFT_RIGHT_COGNITION_PRESENT")
if 'DEF append_line(' in final:
    raise SystemExit("HOLD=DIRECT_PERSISTENCE_HELPER_PRESENT")
if final.count('"write_text"') != 2:
    raise SystemExit("HOLD=WRITE_TEXT_SURFACE_NOT_EXACT_TWO")
if '/state/' in final:
    raise SystemExit("HOLD=PERSISTENT_STATE_PATH_PRESENT")

print("HISTORICAL_HEADER_COUNT=1")
print("HISTORICAL_ENTRY_COUNT=1")
print("LEGACY_LEFT_RIGHT_COGNITION=ABSENT")
print("DIRECT_PERSISTENT_STATE_PATH=ABSENT")
print("WRITE_TEXT_SURFACE=ONLY_STAGE_READBACK_AND_FINAL_COMMIT_INTENT")
print("R3_FIX1_CONSTRUCTION=PASS")
PY

sha_lock "$COG" "$EXPECTED_COG_MODULE" "COGNITION_DONOR_MODULE"
sha_lock "$TOOLS" "$EXPECTED_TOOL_MODULE" "TOOL_DONOR_MODULE"
sha_lock "$FINAL" "$EXPECTED_R3_FIX1_SOURCE" "R3_FIX1_SOURCE"

echo "=== 5. COMPILE/FREEZE ONLY ==="
PARTIAL="$BYTECODE.partial.$$"
rm -f "$PARTIAL"
set +e
"$SIGMAC" "$FINAL" "$PARTIAL"
RC=$?
set -e
echo "SIGMAC_RC=$RC"
[ "$RC" -eq 0 ] || {
    echo "R3_FIX1_COMPILE=FAIL"
    exit 1
}
[ -s "$PARTIAL" ] || {
    echo "HOLD=EMPTY_COMPILED_BYTECODE"
    exit 1
}

COMPILED_SHA="$(sha256sum "$PARTIAL" | awk '{print $1}')"
echo "COMPILED_BYTECODE_SHA256=$COMPILED_SHA"

if [ -f "$BYTECODE" ]; then
    EXISTING_SHA="$(sha256sum "$BYTECODE" | awk '{print $1}')"
    echo "BYTECODE_ALREADY_EXISTS=YES"
    echo "EXISTING_BYTECODE_SHA256=$EXISTING_SHA"
    [ "$EXISTING_SHA" = "$COMPILED_SHA" ] || {
        rm -f "$PARTIAL"
        echo "HOLD=BYTECODE_FREEZE_CONFLICT"
        exit 1
    }
    rm -f "$PARTIAL"
else
    mv "$PARTIAL" "$BYTECODE"
    echo "BYTECODE_ALREADY_EXISTS=NO"
fi

BYTECODE_SHA="$(sha256sum "$BYTECODE" | awk '{print $1}')"
echo "BYTECODE_PATH=$BYTECODE"
echo "BYTECODE_SHA256=$BYTECODE_SHA"

echo "=== 6. NON-MUTATION RECHECK ==="
sha_lock "$FINAL" "$EXPECTED_R3_FIX1_SOURCE" "R3_FIX1_SOURCE_AFTER"
sha_lock "$LIVE_CORE" "$EXPECTED_LIVE_CORE" "LIVE_CORE_AFTER"
sha_lock "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER" "LIVE_RUNNER_AFTER"

echo "=== 7. RESULT ==="
echo "R3_FIX1_TRUST_FIRST_BUILD=PASS"
echo "R3_FIX1_COMPILE=PASS"
echo "R3_FIX1_BYTECODE_FREEZE=PASS"
echo "R3_FIX1_FRESH_INVOCATION_CONTRACT=SOURCE_PRESENT_NOT_RUNTIME_ADMITTED"
echo "R3_FIX1_AUTHORITATIVE_STATE_CHAIN_BINDING=SOURCE_PRESENT_NOT_RUNTIME_ADMITTED"
echo "R3_FIX1_RECEIPT_BOUND_EVENT_SEGMENT_FETCH_EVIDENCE_CAPABILITY=SOURCE_PRESENT_NOT_RUNTIME_ADMITTED"
echo "R3_FIX1_DIRECT_PERSISTENT_STATE_MUTATION=NO"
echo "R3_FIX1_POSITIVE_COMMIT_PERMISSION_LAST_WRITE=YES_BY_SOURCE_CONSTRUCTION"
echo "R3_FIX1_COGNITION_DONOR=LATEST_ADMITTED_GATE_A_PURE_DEF_MATERIAL"
echo "R3_FIX1_T1_T2_T3=EXACT_ADMITTED_DEF_MATERIAL_PRESENT_NOT_YET_ACTIVATED"
echo "VM_EXECUTION=NO"
echo "LIVE_CORE_UNCHANGED=YES"
echo "LIVE_RUNNER_UNCHANGED=YES"
echo "PRODUCTION_BINDING=NO"
echo "PRODUCTION_MUTATION=NO"
echo "=== END ==="
