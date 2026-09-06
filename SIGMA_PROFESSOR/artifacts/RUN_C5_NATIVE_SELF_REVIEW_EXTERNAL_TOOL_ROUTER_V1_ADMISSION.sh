#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
ROOT="$HOME/SIGMA/sigma_genesis1"
SIGMAC="$ROOT/native/sigmac"
VM="$ROOT/native/sigma-vm.v09_candidate"
C5_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
PIDFILE="$ROOT/C5_V3_CONTINUOUS.pid"

EXPECTED_SIGMAC_SHA256="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM_SHA256="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_C5_RUNNER_SHA256="a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb"
EXPECTED_ROUTER_SOURCE_SHA256="8460912fdc63e99e576da5485929d6eff1af6afda213bb0ad7f95cd0ef7b7a0f"
EXPECTED_BUILDER_SHA256="db4efcc1e587b12ffdbd7a014461fe99b73ed975af13e71af99c3afabe523d1a"

INSTANCE_FINGERPRINT="fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125"
C5_CORE_SHA256="1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace"

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." 2>/dev/null && pwd)"
SRC="$REPO_ROOT/SIGMA_PROFESSOR/artifacts/SOURCES/C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1.sigma"
BUILDER="$REPO_ROOT/SIGMA_PROFESSOR/artifacts/TOOLS/C5_MECHANICAL_EXTERNAL_TOOL_INPUT_BUILDER_V1.py"

PY="$P/bin/python3"
SHA="$P/bin/sha256sum"
AWK="$P/bin/awk"
GREP="$P/bin/grep"
CAT="$P/bin/cat"
MKDIR="$P/bin/mkdir"
RM="$P/bin/rm"
MV="$P/bin/mv"
DATE="$P/bin/date"

hold() {
    msg="$1"
    rc="${2:-20}"
    printf 'HOLD=%s\n' "$msg"
    exit "$rc"
}

for x in "$PY" "$SHA" "$AWK" "$GREP" "$CAT" "$MKDIR" "$RM" "$MV" "$DATE"; do
    [ -x "$x" ] || hold "REQUIRED_EXECUTABLE_MISSING path=$x" 20
done
[ -x "$SIGMAC" ] || hold "SIGMAC_MISSING" 21
[ -x "$VM" ] || hold "VM_MISSING" 22
[ -f "$C5_RUNNER" ] || hold "C5_V3_RUNNER_MISSING" 23
[ -f "$PIDFILE" ] || hold "C5_V3_PIDFILE_MISSING" 24
[ -f "$SRC" ] || hold "ROUTER_SOURCE_MISSING" 25
[ -f "$BUILDER" ] || hold "INPUT_BUILDER_MISSING" 26

PID_BEFORE="$($CAT "$PIDFILE" 2>/dev/null || true)"
case "$PID_BEFORE" in
    ''|*[!0-9]*) hold "C5_V3_PID_INVALID" 27 ;;
esac
kill -0 "$PID_BEFORE" 2>/dev/null || hold "C5_V3_PROCESS_NOT_ALIVE" 28

actual_sigmac="$($SHA "$SIGMAC" | $AWK '{print $1}')"
actual_vm="$($SHA "$VM" | $AWK '{print $1}')"
actual_runner="$($SHA "$C5_RUNNER" | $AWK '{print $1}')"
actual_src="$($SHA "$SRC" | $AWK '{print $1}')"
actual_builder="$($SHA "$BUILDER" | $AWK '{print $1}')"

printf '=== C5 NATIVE SELF-REVIEW EXTERNAL TOOL ROUTER V1 ADMISSION ===\n'
printf 'ROLE=LOCKED_NATIVE_ADMISSION_FIXTURE\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'NETWORK_REQUEST=NO\n'
printf 'C5_V3_RESTART=NO\n'
printf 'C5_V3_STOP=NO\n'
printf 'C5_COGNITIVE_STATE_WRITE_BY_ADMISSION=NO\n'
printf 'SECOND_PERSISTENT_SIGMA=NO\n'
printf 'HOST_RUNTIME_QUERY_GENERATION=NO\n'
printf 'HOST_RUNTIME_SOURCE_SELECTION=NO\n'
printf 'HOST_RUNTIME_RESULT_RANKING=NO\n'
printf 'ADMISSION_FIXTURE_INPUT_GENERATION=YES\n'
printf 'C5_V3_PID_BEFORE=%s\n' "$PID_BEFORE"
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'C5_V3_RUNNER_SHA256=%s\n' "$actual_runner"
printf 'ROUTER_SOURCE_SHA256=%s\n' "$actual_src"
printf 'BUILDER_SHA256=%s\n' "$actual_builder"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC_SHA256" ] || hold "SIGMAC_IDENTITY_MISMATCH" 30
[ "$actual_vm" = "$EXPECTED_VM_SHA256" ] || hold "VM_IDENTITY_MISMATCH" 31
[ "$actual_runner" = "$EXPECTED_C5_RUNNER_SHA256" ] || hold "C5_V3_RUNNER_IDENTITY_MISMATCH" 32
[ "$actual_src" = "$EXPECTED_ROUTER_SOURCE_SHA256" ] || hold "ROUTER_SOURCE_IDENTITY_MISMATCH" 33
[ "$actual_builder" = "$EXPECTED_BUILDER_SHA256" ] || hold "BUILDER_IDENTITY_MISMATCH" 34

if $GREP -Eiq 'WIKIPEDIA|WIKIMEDIA|DUCKDUCKGO|GUTENBERG|OPENLIBRARY|OPEN_LIBRARY' "$SRC"; then
    hold "SOURCE_CONCRETE_FAMILY_TOKEN_LEAK" 35
fi
printf 'SOURCE_CONCRETE_FAMILY_TOKEN_LEAK=ZERO\n'

if $GREP -Eq 'EXPECTED_(TOOL|ROUTE|SOURCE|SELECTED_TOOL)[A-Z_]*[[:space:]]*[:=]' "$SRC"; then
    hold "PREWRITTEN_EXPECTED_ROUTE_FOUND_IN_NATIVE_SOURCE" 36
fi
printf 'CANONICAL_EXPECTED_TOOL_PREWRITTEN=NO\n'

if $GREP -Eq 'SELECTED_TOOL_(ID|TOKEN)' "$BUILDER"; then
    hold "HOST_BUILDER_SELECTED_TOOL_FIELD_FOUND" 37
fi
printf 'HOST_BUILDER_TOOL_SELECTION_FIELD=ABSENT\n'

if $GREP -Eiq '(^|[^A-Za-z])(WHILE|LOOP)[[:space:](]' "$SRC"; then
    hold "STEP_LIMIT_SCAN_UNBOUNDED_LOOP_TOKEN_FOUND" 38
fi
printf 'STEP_LIMIT_SCAN=PASS_STATIC_NO_LOOP_TOKEN\n'

ADMISSION_ROOT="$ROOT/.sigma_admission/C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1"
RUN_ID="$($DATE -u +%Y%m%dT%H%M%SZ)_$$"
RUN="$ADMISSION_ROOT/$RUN_ID"
FIX="$RUN/fixtures"
CASES="$RUN/cases"
$MKDIR -p "$FIX" "$CASES" || hold "ADMISSION_DIRECTORY_CREATE_FAILED" 39

BC="$RUN/C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1.sigmab"
"$SIGMAC" "$SRC" "$BC.partial" >"$RUN/sigmac.log" 2>&1
SIGMAC_RC=$?
printf 'LOCKED_SIGMAC_RC=%s\n' "$SIGMAC_RC"
if [ "$SIGMAC_RC" -ne 0 ]; then
    $CAT "$RUN/sigmac.log"
    hold "LOCKED_SIGMAC_COMPILE_FAILED" 40
fi
$MV -f -- "$BC.partial" "$BC" || hold "BYTECODE_PROMOTE_FAILED" 41
BYTECODE_SHA256="$($SHA "$BC" | $AWK '{print $1}')"
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA256"

"$PY" - "$FIX" <<'PYFIX'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1])
p.mkdir(parents=True, exist_ok=True)
tools = [
    {"id":"71", "token":"tk7a0", "available":"1", "readiness":"5", "descriptor":"amberkey sharedkey", "languages":"lg0", "media":"m0"},
    {"id":"140", "token":"tk9b1", "available":"1", "readiness":"5", "descriptor":"violetkey sharedkey", "languages":"lg1", "media":"m0"},
    {"id":"305", "token":"tk4c2", "available":"1", "readiness":"2", "descriptor":"sharedkey", "languages":"lg2", "media":"m1"},
]
def dump(name, obj):
    (p/name).write_text(json.dumps(obj, sort_keys=True, separators=(",", ":")), encoding="utf-8")
dump("catalog_base.json", {"tools": tools})
dump("catalog_reordered.json", {"tools": list(reversed(tools))})
dump("catalog_all_unavailable.json", {"tools": [dict(x, available="0") for x in tools]})
bad = [dict(x) for x in tools]
bad[0].pop("media")
dump("catalog_malformed.json", {"tools": bad})
dup = [dict(x) for x in tools]
dup[1]["id"] = dup[0]["id"]
dump("catalog_duplicate_id.json", {"tools": dup})
(p/"query_a.txt").write_text("amberkey", encoding="utf-8")
(p/"query_b.txt").write_text("violetkey", encoding="utf-8")
(p/"query_common.txt").write_text("sharedkey", encoding="utf-8")
PYFIX
FIX_RC=$?
[ "$FIX_RC" -eq 0 ] || hold "FIXTURE_GENERATION_FAILED" 42

LAST_STATUS=""
LAST_ID=""
LAST_TOKEN=""
LAST_INSTANCE=""

run_case() {
    name="$1"
    request="$2"
    catalog="$3"
    history="${4:-}"
    case_root="$CASES/$name"
    input="$case_root/.sigma_exec/C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1/input"
    $MKDIR -p "$input" || return 60

    if [ -n "$history" ]; then
        "$PY" "$BUILDER" \
            --request-file "$request" \
            --catalog "$catalog" \
            --history "$history" \
            --out-input "$input" \
            --instance-fingerprint "$INSTANCE_FINGERPRINT" \
            --c5-core-sha256 "$C5_CORE_SHA256" \
            >"$case_root/builder.log" 2>&1
    else
        "$PY" "$BUILDER" \
            --request-file "$request" \
            --catalog "$catalog" \
            --out-input "$input" \
            --instance-fingerprint "$INSTANCE_FINGERPRINT" \
            --c5-core-sha256 "$C5_CORE_SHA256" \
            >"$case_root/builder.log" 2>&1
    fi
    brc=$?
    [ "$brc" -eq 0 ] || return 61

    (
        cd "$case_root" || exit 62
        "$VM" "$BC"
    ) >"$case_root/vm.log" 2>&1
    vrc=$?
    [ "$vrc" -eq 0 ] || return 63

    LAST_STATUS="$($AWK -F= '/^ROUTER_STATUS=/{v=$2} END{print v}' "$case_root/vm.log")"
    LAST_ID="$($AWK -F= '/^SELECTED_TOOL_ID=/{v=$2} END{print v}' "$case_root/vm.log")"
    LAST_TOKEN="$($AWK -F= '/^SELECTED_TOOL_TOKEN=/{v=$2} END{print v}' "$case_root/vm.log")"
    LAST_INSTANCE="$($AWK -F= '/^INSTANCE_BOUND=/{v=$2} END{print v}' "$case_root/vm.log")"

    [ "$LAST_INSTANCE" = "1" ] || return 64

    if [ "$LAST_STATUS" = "ROUTE_READY" ]; then
        "$PY" - "$catalog" "$LAST_ID" "$LAST_TOKEN" <<'PYMEM'
import json, sys
obj = json.load(open(sys.argv[1], encoding="utf-8"))
sid, stok = sys.argv[2], sys.argv[3]
rows = obj.get("tools", [])
ok = any(str(r.get("id", "")) == sid and str(r.get("token", "")) == stok and str(r.get("available", "")) == "1" for r in rows)
raise SystemExit(0 if ok else 1)
PYMEM
        [ $? -eq 0 ] || return 65
    fi

    printf 'CASE=%s ROUTER_STATUS=%s SELECTED_TOOL_ID=%s SELECTED_TOOL_TOKEN=%s\n' \
        "$name" "$LAST_STATUS" "$LAST_ID" "$LAST_TOKEN"
    return 0
}

run_case "QUERY_A" "$FIX/query_a.txt" "$FIX/catalog_base.json" || hold "QUERY_A_NATIVE_CASE_FAILED" 50
STATUS_A="$LAST_STATUS"; ID_A="$LAST_ID"; TOKEN_A="$LAST_TOKEN"
[ "$STATUS_A" = "ROUTE_READY" ] || hold "QUERY_A_ROUTE_NOT_READY" 51

run_case "QUERY_A_REPLAY" "$FIX/query_a.txt" "$FIX/catalog_base.json" || hold "QUERY_A_REPLAY_FAILED" 52
[ "$LAST_STATUS" = "ROUTE_READY" ] || hold "QUERY_A_REPLAY_ROUTE_NOT_READY" 53
[ "$LAST_ID" = "$ID_A" ] && [ "$LAST_TOKEN" = "$TOKEN_A" ] || hold "REPLAY_SELECTION_CHANGED" 54
printf 'REPLAY_IDENTICAL_SELECTION=PASS\n'

run_case "QUERY_B" "$FIX/query_b.txt" "$FIX/catalog_base.json" || hold "QUERY_B_NATIVE_CASE_FAILED" 55
[ "$LAST_STATUS" = "ROUTE_READY" ] || hold "QUERY_B_ROUTE_NOT_READY" 56
ID_B="$LAST_ID"
[ "$ID_B" != "$ID_A" ] || hold "DYNAMIC_QUERY_CHANGE_DID_NOT_CHANGE_ROUTE" 57
printf 'DYNAMIC_QUERY_CHANGE_CAN_CHANGE_ROUTE=PASS\n'

run_case "CATALOG_REORDER" "$FIX/query_a.txt" "$FIX/catalog_reordered.json" || hold "CATALOG_REORDER_CASE_FAILED" 58
[ "$LAST_STATUS" = "ROUTE_READY" ] || hold "CATALOG_REORDER_ROUTE_NOT_READY" 59
[ "$LAST_ID" = "$ID_A" ] && [ "$LAST_TOKEN" = "$TOKEN_A" ] || hold "CATALOG_REORDER_CHANGED_SELECTION" 60
printf 'CATALOG_REORDER_INVARIANCE=PASS\n'

run_case "COMMON_BASE" "$FIX/query_common.txt" "$FIX/catalog_base.json" || hold "COMMON_BASE_CASE_FAILED" 61
[ "$LAST_STATUS" = "ROUTE_READY" ] || hold "COMMON_BASE_ROUTE_NOT_READY" 62
ID_COMMON="$LAST_ID"

"$PY" - "$FIX/history_counterfactual.jsonl" "$ID_COMMON" <<'PYHIST'
import json, pathlib, sys
path = pathlib.Path(sys.argv[1])
row = {"tool_id":sys.argv[2], "transport_rc":1, "http_code":0, "decode_rc":0, "payload_bytes":0}
path.write_text(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
PYHIST
[ $? -eq 0 ] || hold "HISTORY_COUNTERFACTUAL_BUILD_FAILED" 63
run_case "HISTORY_COUNTERFACTUAL" "$FIX/query_common.txt" "$FIX/catalog_base.json" "$FIX/history_counterfactual.jsonl" || hold "HISTORY_COUNTERFACTUAL_CASE_FAILED" 64
[ "$LAST_STATUS" = "ROUTE_READY" ] || hold "HISTORY_COUNTERFACTUAL_ROUTE_NOT_READY" 65
[ "$LAST_ID" != "$ID_COMMON" ] || hold "HISTORY_OUTCOME_CHANGE_DID_NOT_CHANGE_ROUTE" 66
printf 'HISTORY_OUTCOME_CHANGE_CAN_CHANGE_ROUTE=PASS\n'

"$PY" - "$FIX/catalog_base.json" "$FIX/catalog_availability_counterfactual.json" "$ID_A" <<'PYAV'
import json, sys
obj = json.load(open(sys.argv[1], encoding="utf-8"))
for row in obj["tools"]:
    if str(row["id"]) == sys.argv[3]:
        row["available"] = "0"
open(sys.argv[2], "w", encoding="utf-8").write(json.dumps(obj, sort_keys=True, separators=(",", ":")))
PYAV
[ $? -eq 0 ] || hold "AVAILABILITY_COUNTERFACTUAL_BUILD_FAILED" 67
run_case "AVAILABILITY_COUNTERFACTUAL" "$FIX/query_a.txt" "$FIX/catalog_availability_counterfactual.json" || hold "AVAILABILITY_COUNTERFACTUAL_CASE_FAILED" 68
[ "$LAST_STATUS" = "ROUTE_READY" ] || hold "AVAILABILITY_COUNTERFACTUAL_ROUTE_NOT_READY" 69
[ "$LAST_ID" != "$ID_A" ] || hold "AVAILABILITY_CHANGE_DID_NOT_CHANGE_ROUTE" 70
printf 'AVAILABILITY_CHANGE_CAN_CHANGE_ROUTE=PASS\n'

"$PY" - "$FIX/catalog_base.json" "$FIX/catalog_readiness_counterfactual.json" "$ID_COMMON" <<'PYREADY'
import json, sys
obj = json.load(open(sys.argv[1], encoding="utf-8"))
selected = sys.argv[3]
other_done = False
for row in obj["tools"]:
    if str(row["id"]) == selected:
        row["readiness"] = "0"
    elif not other_done:
        row["readiness"] = "99"
        other_done = True
open(sys.argv[2], "w", encoding="utf-8").write(json.dumps(obj, sort_keys=True, separators=(",", ":")))
PYREADY
[ $? -eq 0 ] || hold "READINESS_COUNTERFACTUAL_BUILD_FAILED" 71
run_case "READINESS_COUNTERFACTUAL" "$FIX/query_common.txt" "$FIX/catalog_readiness_counterfactual.json" || hold "READINESS_COUNTERFACTUAL_CASE_FAILED" 72
[ "$LAST_STATUS" = "ROUTE_READY" ] || hold "READINESS_COUNTERFACTUAL_ROUTE_NOT_READY" 73
[ "$LAST_ID" != "$ID_COMMON" ] || hold "READINESS_CHANGE_DID_NOT_CHANGE_ROUTE" 74
printf 'READINESS_CHANGE_CAN_CHANGE_ROUTE=PASS\n'

run_case "NO_AVAILABLE_TOOL" "$FIX/query_a.txt" "$FIX/catalog_all_unavailable.json" || hold "NO_AVAILABLE_TOOL_CASE_FAILED" 75
[ "$LAST_STATUS" = "NO_AVAILABLE_ROUTE" ] || hold "NO_AVAILABLE_TOOL_STATUS_INVALID" 76
[ -z "$LAST_ID" ] && [ -z "$LAST_TOKEN" ] || hold "NO_AVAILABLE_TOOL_EMITTED_SELECTION" 77
printf 'NO_AVAILABLE_TOOL_PATH=PASS\n'

expect_builder_refusal() {
    name="$1"
    catalog="$2"
    case_root="$CASES/$name"
    input="$case_root/.sigma_exec/C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1/input"
    $MKDIR -p "$input" || return 80
    "$PY" "$BUILDER" \
        --request-file "$FIX/query_a.txt" \
        --catalog "$catalog" \
        --out-input "$input" \
        --instance-fingerprint "$INSTANCE_FINGERPRINT" \
        --c5-core-sha256 "$C5_CORE_SHA256" \
        >"$case_root/builder.log" 2>&1
    rc=$?
    [ "$rc" -ne 0 ] || return 81
    return 0
}

expect_builder_refusal "MALFORMED_CATALOG" "$FIX/catalog_malformed.json" || hold "MALFORMED_CATALOG_NOT_REFUSED" 78
printf 'MALFORMED_CATALOG_REFUSAL=PASS\n'
expect_builder_refusal "DUPLICATE_TOOL_ID" "$FIX/catalog_duplicate_id.json" || hold "DUPLICATE_TOOL_ID_NOT_REFUSED" 79
printf 'DUPLICATE_TOOL_ID_REFUSAL=PASS\n'

printf 'INSTANCE_BINDING=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'HOST_SUBSTITUTION_AUDIT=PASS_TESTED_SCOPE\n'
printf 'NATIVE_ROUTE_MEMBERSHIP_CHECK=PASS\n'

PID_AFTER="$($CAT "$PIDFILE" 2>/dev/null || true)"
printf 'C5_V3_PID_AFTER=%s\n' "$PID_AFTER"
if [ "$PID_AFTER" != "$PID_BEFORE" ] || ! kill -0 "$PID_AFTER" 2>/dev/null; then
    hold "C5_V3_PROCESS_NOT_PRESERVED" 90
fi
RUNNER_AFTER="$($SHA "$C5_RUNNER" | $AWK '{print $1}')"
[ "$RUNNER_AFTER" = "$EXPECTED_C5_RUNNER_SHA256" ] || hold "C5_V3_RUNNER_CHANGED_DURING_ADMISSION" 91

printf 'C5_V3_SAME_PROCESS_AFTER=YES\n'
printf 'C5_V3_RUNNER_UNCHANGED=YES\n'
printf 'ADMISSION_RUN_DIR=%s\n' "$RUN"
printf 'C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1_ADMISSION=PASS_TESTED_SCOPE\n'
printf 'PRODUCTION_BINDING=NO\n'