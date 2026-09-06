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
EXPECTED_SOURCE_SHA256="b9dc078b2898c58b6af88b3eed22976fffb59dc1dbe5f950babb6b18bab2e33e"
EXPECTED_BUILDER_SHA256="f23487fdf0eafb0ad86977ed0119bd56aba51c28aec0c4461e07a06cf9605f2e"

INSTANCE_FINGERPRINT="fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125"
C5_CORE_SHA256="1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace"

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." 2>/dev/null && pwd)"
SRC="$REPO_ROOT/SIGMA_PROFESSOR/artifacts/SOURCES/C5_NATIVE_EXPERIENCE_TO_STRATEGY_ADVISER_V1.sigma"
BUILDER="$REPO_ROOT/SIGMA_PROFESSOR/artifacts/TOOLS/C5_MECHANICAL_EXPERIENCE_TO_STRATEGY_INPUT_BUILDER_V1.py"

PY="$P/bin/python3"
SHA="$P/bin/sha256sum"
AWK="$P/bin/awk"
GREP="$P/bin/grep"
CAT="$P/bin/cat"
MKDIR="$P/bin/mkdir"
MV="$P/bin/mv"
DATE="$P/bin/date"

hold() {
    printf 'HOLD=%s\n' "$1"
    exit "${2:-20}"
}

for x in "$PY" "$SHA" "$AWK" "$GREP" "$CAT" "$MKDIR" "$MV" "$DATE"; do
    [ -x "$x" ] || hold "REQUIRED_EXECUTABLE_MISSING path=$x" 20
done
[ -x "$SIGMAC" ] || hold "SIGMAC_MISSING" 21
[ -x "$VM" ] || hold "VM_MISSING" 22
[ -f "$C5_RUNNER" ] || hold "C5_V3_RUNNER_MISSING" 23
[ -f "$PIDFILE" ] || hold "C5_V3_PIDFILE_MISSING" 24
[ -f "$SRC" ] || hold "SOURCE_MISSING" 25
[ -f "$BUILDER" ] || hold "BUILDER_MISSING" 26

PID_BEFORE="$($CAT "$PIDFILE" 2>/dev/null || true)"
case "$PID_BEFORE" in ''|*[!0-9]*) hold "C5_V3_PID_INVALID" 27 ;; esac
kill -0 "$PID_BEFORE" 2>/dev/null || hold "C5_V3_PROCESS_NOT_ALIVE" 28

actual_sigmac="$($SHA "$SIGMAC" | $AWK '{print $1}')"
actual_vm="$($SHA "$VM" | $AWK '{print $1}')"
actual_runner="$($SHA "$C5_RUNNER" | $AWK '{print $1}')"
actual_src="$($SHA "$SRC" | $AWK '{print $1}')"
actual_builder="$($SHA "$BUILDER" | $AWK '{print $1}')"

printf '%s\n' '=== C5 NATIVE EXPERIENCE-TO-STRATEGY ADVISER V1 ADMISSION ==='
printf 'ROLE=LOCKED_NATIVE_ADMISSION_FIXTURE\n'
printf 'PRODUCTION_BINDING=NO\nNETWORK_REQUEST=NO\nC5_V3_RESTART=NO\nC5_V3_STOP=NO\n'
printf 'C5_COGNITIVE_STATE_WRITE_BY_ADMISSION=NO\nSECOND_PERSISTENT_SIGMA=NO\n'
printf 'HOST_CANDIDATE_SELECTION=NO\nHOST_SEMANTIC_SCORING=NO\nHOST_LEARNING=NO\n'
printf 'C5_V3_PID_BEFORE=%s\n' "$PID_BEFORE"
printf 'SIGMAC_SHA256=%s\nVM_SHA256=%s\nC5_V3_RUNNER_SHA256=%s\n' "$actual_sigmac" "$actual_vm" "$actual_runner"
printf 'SOURCE_SHA256=%s\nBUILDER_SHA256=%s\n' "$actual_src" "$actual_builder"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC_SHA256" ] || hold "SIGMAC_IDENTITY_MISMATCH" 30
[ "$actual_vm" = "$EXPECTED_VM_SHA256" ] || hold "VM_IDENTITY_MISMATCH" 31
[ "$actual_runner" = "$EXPECTED_C5_RUNNER_SHA256" ] || hold "C5_V3_RUNNER_IDENTITY_MISMATCH" 32
[ "$actual_src" = "$EXPECTED_SOURCE_SHA256" ] || hold "SOURCE_IDENTITY_MISMATCH" 33
[ "$actual_builder" = "$EXPECTED_BUILDER_SHA256" ] || hold "BUILDER_IDENTITY_MISMATCH" 34

if $GREP -Eiq 'BINARY_OR_UTF16_UNSUPPORTED|SEGMENT_DENSITY_LIMIT|EXPECTED_(CANDIDATE|STRATEGY)|RECOMMENDED_CANDIDATE|TEACHER_CHOICE' "$SRC"; then
    hold "NATIVE_SOURCE_PRELOADED_RUNTIME_ANSWER_OR_CONCRETE_FAILURE_MAPPING" 35
fi
printf 'CONCRETE_FAILURE_TO_ACTION_MAPPING=ABSENT\nPRELOADED_SELECTED_CANDIDATE=NO\n'

if $GREP -Eiq '(^|[^A-Za-z])(WHILE|LOOP)[[:space:](]' "$SRC"; then
    hold "STEP_LIMIT_SCAN_UNBOUNDED_LOOP_TOKEN_FOUND" 36
fi
printf 'STEP_LIMIT_SCAN=PASS_STATIC_NO_LOOP_TOKEN\n'

ADMISSION_ROOT="$HOME/SIGMA_ADMISSION/C5_NATIVE_EXPERIENCE_TO_STRATEGY_ADVISER_V1"
RUN_ID="$($DATE -u +%Y%m%dT%H%M%SZ)_$$"
RUN="$ADMISSION_ROOT/$RUN_ID"
FIX="$RUN/fixtures"
CASES="$RUN/cases"
$MKDIR -p "$FIX" "$CASES" || hold "ADMISSION_DIRECTORY_CREATE_FAILED" 37
printf 'ADMISSION_RUN_DIR=%s\n' "$RUN"

BC="$RUN/C5_NATIVE_EXPERIENCE_TO_STRATEGY_ADVISER_V1.sigmab"
"$SIGMAC" "$SRC" "$BC.partial" >"$RUN/sigmac.log" 2>&1
SIGMAC_RC=$?
printf 'LOCKED_SIGMAC_RC=%s\n' "$SIGMAC_RC"
if [ "$SIGMAC_RC" -ne 0 ]; then
    $CAT "$RUN/sigmac.log"
    hold "LOCKED_SIGMAC_COMPILE_FAILED" 40
fi
$MV -f -- "$BC.partial" "$BC" || hold "BYTECODE_PROMOTE_FAILED" 41
printf 'BYTECODE_SHA256=%s\n' "$($SHA "$BC" | $AWK '{print $1}')"

"$PY" - "$FIX" <<'PYFIX'
import json, pathlib, sys
p=pathlib.Path(sys.argv[1])
p.mkdir(parents=True, exist_ok=True)
base=[
 {"id":"11","token":"p7a","available":"1","readiness":"5"},
 {"id":"22","token":"p8b","available":"1","readiness":"5"},
 {"id":"33","token":"p9c","available":"1","readiness":"5"},
]
def dump(name,obj):
    (p/name).write_text(json.dumps(obj,sort_keys=True,separators=(",",":")),encoding="utf-8")
dump("catalog_base.json",{"candidates":base})
dump("catalog_reordered.json",{"candidates":list(reversed(base))})
dump("catalog_none.json",{"candidates":[dict(x,available="0") for x in base]})
dump("catalog_malformed.json",{"candidates":[{"id":"11","token":"p7a","available":"1"}]})
dup_id=[dict(x) for x in base]; dup_id[1]["id"]=dup_id[0]["id"]; dump("catalog_dup_id.json",{"candidates":dup_id})
dup_tok=[dict(x) for x in base]; dup_tok[1]["token"]=dup_tok[0]["token"]; dump("catalog_dup_token.json",{"candidates":dup_tok})
bad=[dict(x) for x in base]; bad[0]["teacher_choice"]="1"; dump("catalog_semantic_key.json",{"candidates":bad})
PYFIX
[ $? -eq 0 ] || hold "FIXTURE_GENERATION_FAILED" 42

LAST_STATUS=""
LAST_ID=""
LAST_TOKEN=""

run_case() {
    name="$1"
    catalog="$2"
    history="${3:-}"
    last="${4:-NONE}"
    case_root="$CASES/$name"
    base="$case_root/.sigma_exec/C5_NATIVE_EXPERIENCE_TO_STRATEGY_ADVISER_V1"
    input="$base/input"
    output="$base/output"
    $MKDIR -p "$input" "$output" || return 60

    if [ -n "$history" ]; then
        "$PY" "$BUILDER" --catalog "$catalog" --history "$history" --out-input "$input" \
            --instance-fingerprint "$INSTANCE_FINGERPRINT" --c5-core-sha256 "$C5_CORE_SHA256" \
            --last-selected-id "$last" >"$case_root/builder.log" 2>&1
    else
        "$PY" "$BUILDER" --catalog "$catalog" --out-input "$input" \
            --instance-fingerprint "$INSTANCE_FINGERPRINT" --c5-core-sha256 "$C5_CORE_SHA256" \
            --last-selected-id "$last" >"$case_root/builder.log" 2>&1
    fi
    brc=$?
    if [ "$brc" -ne 0 ]; then
        printf 'CASE=%s CASE_STAGE=MECHANICAL_INPUT_BUILD BUILDER_RC=%s\n' "$name" "$brc"
        $CAT "$case_root/builder.log" 2>/dev/null || true
        return 61
    fi

    (
        cd "$case_root" || exit 62
        "$VM" "$BC"
    ) >"$case_root/vm.log" 2>&1
    vrc=$?
    if [ "$vrc" -ne 0 ]; then
        printf 'CASE=%s CASE_STAGE=LOCKED_VM_EXECUTION VM_RC=%s\n' "$name" "$vrc"
        $CAT "$case_root/vm.log" 2>/dev/null || true
        return 63
    fi

    LAST_STATUS="$($CAT "$output/adviser_status.txt" 2>/dev/null || true)"
    LAST_ID="$($CAT "$output/selected_candidate_id.txt" 2>/dev/null || true)"
    LAST_TOKEN="$($CAT "$output/selected_candidate_token.txt" 2>/dev/null || true)"
    bound="$($CAT "$output/instance_bound.txt" 2>/dev/null || true)"
    if [ "$bound" != "1" ] && [ "$bound" != "1.0" ]; then
        printf 'CASE=%s CASE_STAGE=INSTANCE_BINDING OUTPUT_INSTANCE_BOUND=%s\n' "$name" "$bound"
        $CAT "$case_root/vm.log" 2>/dev/null || true
        return 64
    fi

    if [ "$LAST_STATUS" = "ADVICE_READY" ]; then
        "$PY" - "$catalog" "$LAST_ID" "$LAST_TOKEN" <<'PYMEM'
import json, sys
obj=json.load(open(sys.argv[1],encoding="utf-8"))
sid=sys.argv[2]
if sid.endswith(".0"): sid=sid[:-2]
tok=sys.argv[3]
ok=any(str(x["id"])==sid and x["token"]==tok and str(x["available"])=="1" for x in obj["candidates"])
raise SystemExit(0 if ok else 1)
PYMEM
        [ $? -eq 0 ] || return 65
    fi
    printf 'CASE=%s ADVISER_STATUS=%s SELECTED_CANDIDATE_ID=%s SELECTED_CANDIDATE_TOKEN=%s\n' \
        "$name" "$LAST_STATUS" "$LAST_ID" "$LAST_TOKEN"
    return 0
}

run_case BASE "$FIX/catalog_base.json" || hold "BASE_NATIVE_CASE_FAILED" 50
[ "$LAST_STATUS" = "ADVICE_READY" ] || hold "BASE_NOT_ADVICE_READY" 51
BASE_ID="$LAST_ID"; BASE_TOKEN="$LAST_TOKEN"

run_case REPLAY "$FIX/catalog_base.json" || hold "REPLAY_NATIVE_CASE_FAILED" 52
[ "$LAST_STATUS" = "ADVICE_READY" ] || hold "REPLAY_NOT_ADVICE_READY" 53
[ "$LAST_ID" = "$BASE_ID" ] && [ "$LAST_TOKEN" = "$BASE_TOKEN" ] || hold "REPLAY_SELECTION_CHANGED" 54
printf 'REPLAY_IDENTICAL_SELECTION=PASS\n'

run_case REORDER "$FIX/catalog_reordered.json" || hold "REORDER_NATIVE_CASE_FAILED" 55
[ "$LAST_STATUS" = "ADVICE_READY" ] || hold "REORDER_NOT_ADVICE_READY" 56
[ "$LAST_ID" = "$BASE_ID" ] && [ "$LAST_TOKEN" = "$BASE_TOKEN" ] || hold "CATALOG_REORDER_CHANGED_SELECTION" 57
printf 'CATALOG_REORDER_INVARIANCE=PASS\n'

"$PY" - "$FIX/catalog_base.json" "$FIX/history_counterfactual.jsonl" "$BASE_ID" <<'PYH'
import json,sys
obj=json.load(open(sys.argv[1],encoding="utf-8"))
sel=sys.argv[3].removesuffix(".0")
ids=[str(x["id"]) for x in obj["candidates"]]
alt=next(x for x in ids if x!=sel)
fp="a"*64
rows=[
 {"candidate_id":sel,"evidence_persisted":0,"knowledge_persisted":0,"segment_committed":0,"failure_fingerprint":fp,"unresolved_before":100,"unresolved_after":101},
 {"candidate_id":sel,"evidence_persisted":0,"knowledge_persisted":0,"segment_committed":0,"failure_fingerprint":fp,"unresolved_before":101,"unresolved_after":102},
 {"candidate_id":alt,"evidence_persisted":4,"knowledge_persisted":3,"segment_committed":1,"failure_fingerprint":"NONE","unresolved_before":102,"unresolved_after":99},
]
open(sys.argv[2],"w",encoding="utf-8").write("\n".join(json.dumps(r,sort_keys=True,separators=(",",":")) for r in rows)+"\n")
PYH
[ $? -eq 0 ] || hold "HISTORY_COUNTERFACTUAL_BUILD_FAILED" 58
run_case HISTORY_COUNTERFACTUAL "$FIX/catalog_base.json" "$FIX/history_counterfactual.jsonl" "$BASE_ID" || hold "HISTORY_COUNTERFACTUAL_NATIVE_CASE_FAILED" 59
[ "$LAST_STATUS" = "ADVICE_READY" ] || hold "HISTORY_COUNTERFACTUAL_NOT_READY" 60
[ "$LAST_ID" != "$BASE_ID" ] || hold "HISTORY_OUTCOME_CHANGE_DID_NOT_CHANGE_SELECTION" 61
printf 'HISTORY_OUTCOME_CHANGE_CAN_CHANGE_SELECTION=PASS\n'

"$PY" - "$FIX/catalog_base.json" "$FIX/catalog_availability.json" "$BASE_ID" <<'PYAV'
import json,sys
obj=json.load(open(sys.argv[1],encoding="utf-8")); sel=sys.argv[3].removesuffix(".0")
for x in obj["candidates"]:
    if str(x["id"])==sel: x["available"]="0"
open(sys.argv[2],"w",encoding="utf-8").write(json.dumps(obj,sort_keys=True,separators=(",",":")))
PYAV
[ $? -eq 0 ] || hold "AVAILABILITY_COUNTERFACTUAL_BUILD_FAILED" 62
run_case AVAILABILITY "$FIX/catalog_availability.json" || hold "AVAILABILITY_NATIVE_CASE_FAILED" 63
[ "$LAST_STATUS" = "ADVICE_READY" ] || hold "AVAILABILITY_NOT_READY" 64
[ "$LAST_ID" != "$BASE_ID" ] || hold "AVAILABILITY_CHANGE_DID_NOT_CHANGE_SELECTION" 65
printf 'AVAILABILITY_CHANGE_CAN_CHANGE_SELECTION=PASS\n'

"$PY" - "$FIX/catalog_base.json" "$FIX/catalog_readiness.json" "$BASE_ID" <<'PYR'
import json,sys
obj=json.load(open(sys.argv[1],encoding="utf-8")); sel=sys.argv[3].removesuffix(".0")
other=False
for x in obj["candidates"]:
    x["readiness"]="1"
for x in obj["candidates"]:
    if str(x["id"])==sel: x["readiness"]="0"
    elif not other:
        x["readiness"]="99"; other=True
open(sys.argv[2],"w",encoding="utf-8").write(json.dumps(obj,sort_keys=True,separators=(",",":")))
PYR
[ $? -eq 0 ] || hold "READINESS_COUNTERFACTUAL_BUILD_FAILED" 66
run_case READINESS "$FIX/catalog_readiness.json" || hold "READINESS_NATIVE_CASE_FAILED" 67
[ "$LAST_STATUS" = "ADVICE_READY" ] || hold "READINESS_NOT_READY" 68
[ "$LAST_ID" != "$BASE_ID" ] || hold "READINESS_CHANGE_DID_NOT_CHANGE_SELECTION" 69
printf 'READINESS_CHANGE_CAN_CHANGE_SELECTION=PASS\n'

run_case NONE "$FIX/catalog_none.json" || hold "NO_AVAILABLE_NATIVE_CASE_FAILED" 70
[ "$LAST_STATUS" = "NO_AVAILABLE_CANDIDATE" ] || hold "NO_AVAILABLE_STATUS_INVALID" 71
printf 'NO_AVAILABLE_CANDIDATE_PATH=PASS\n'

expect_builder_refusal() {
    name="$1"; catalog="$2"
    out="$CASES/$name/.sigma_exec/C5_NATIVE_EXPERIENCE_TO_STRATEGY_ADVISER_V1/input"
    $MKDIR -p "$out" || return 80
    "$PY" "$BUILDER" --catalog "$catalog" --out-input "$out" \
        --instance-fingerprint "$INSTANCE_FINGERPRINT" --c5-core-sha256 "$C5_CORE_SHA256" \
        >"$CASES/$name/builder.log" 2>&1
    [ $? -ne 0 ]
}
expect_builder_refusal MALFORMED "$FIX/catalog_malformed.json" || hold "MALFORMED_CATALOG_NOT_REFUSED" 72
expect_builder_refusal DUP_ID "$FIX/catalog_dup_id.json" || hold "DUPLICATE_ID_NOT_REFUSED" 73
expect_builder_refusal DUP_TOKEN "$FIX/catalog_dup_token.json" || hold "DUPLICATE_TOKEN_NOT_REFUSED" 74
expect_builder_refusal SEMANTIC_KEY "$FIX/catalog_semantic_key.json" || hold "SEMANTIC_SELECTION_KEY_NOT_REFUSED" 75
printf 'MALFORMED_AND_DUPLICATE_REFUSAL=PASS\nSEMANTIC_SELECTION_KEY_REFUSAL=PASS\n'

PID_AFTER="$($CAT "$PIDFILE" 2>/dev/null || true)"
printf 'C5_V3_PID_AFTER=%s\n' "$PID_AFTER"
[ "$PID_AFTER" = "$PID_BEFORE" ] && kill -0 "$PID_AFTER" 2>/dev/null || hold "C5_V3_PROCESS_NOT_PRESERVED" 90
[ "$($SHA "$C5_RUNNER" | $AWK '{print $1}')" = "$EXPECTED_C5_RUNNER_SHA256" ] || hold "C5_V3_RUNNER_CHANGED" 91

printf 'INSTANCE_BINDING=PASS\nLOCKED_VM_EXECUTION=PASS\nNATIVE_SELECTION_MEMBERSHIP=PASS\n'
printf 'C5_V3_SAME_PROCESS_AFTER=YES\nC5_V3_RUNNER_UNCHANGED=YES\n'
printf 'C5_NATIVE_EXPERIENCE_TO_STRATEGY_ADVISER_V1_ADMISSION=PASS_TESTED_SCOPE\n'
printf 'PRODUCTION_BINDING=NO\n'
