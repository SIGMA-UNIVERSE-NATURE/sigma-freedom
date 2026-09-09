#!/data/data/com.termux/files/usr/bin/bash
set -eu
set -o pipefail
umask 077

# ONLINE VERIFICATION — R2 native arbitration adversarial diagnostic R1.
# Diagnostic only: R2 is a compiled prototype/provenance target, NOT the final
# runtime-admission target. This harness does not execute any external capability.
# It tests native need/registry-selection mechanics and result gating without
# production state, network, recursive scans, or semantic host computation.

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
R2_ROOT="$ROOT/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R2"
SRC="$R2_ROOT/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
BIN="$R2_ROOT/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
VM="$ROOT/native/sigma-vm.v09_candidate"
LIVE_SRC="$ROOT/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
LIVE_RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
TEST_ROOT="$ROOT/.sigma_c5v3_online_diag/R2_NATIVE_ARBITRATION_ADVERSARIAL_DIAGNOSTIC_R1"

EXPECTED_SRC_SHA256="d7d1153fd6979dff7d119bb5e8187f045b9f8af62e51065cccf95265478fc3a0"
EXPECTED_BIN_SHA256="ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a"
EXPECTED_VM_SHA256="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_LIVE_SRC_SHA256="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
EXPECTED_LIVE_RUNNER_SHA256="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"

hash1() { sha256sum "$1" 2>/dev/null | awk '{print $1}'; }
read1() { cat "$1" 2>/dev/null || true; }

fail_closed() {
    printf 'DIAGNOSTIC=HOLD_%s\n' "$1"
    printf 'C5V3_NATIVE_CAPABILITY_UTILIZATION=NOT_PROVEN\n'
    printf 'C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=NOT_PROVEN\n'
    printf 'PRODUCTION_BINDING=NO\n'
    printf 'PRODUCTION_MUTATION=NO\n'
    exit 0
}

require_hash() {
    label="$1"; path="$2"; expected="$3"
    [ -f "$path" ] || fail_closed "${label}_MISSING"
    actual=$(hash1 "$path")
    printf '%s_PATH=%s\n' "$label" "$path"
    printf '%s_SHA256=%s\n' "$label" "$actual"
    [ "$actual" = "$expected" ] || fail_closed "${label}_IDENTITY_MISMATCH"
    printf '%s_IDENTITY=PASS\n' "$label"
}

printf '%s\n' '=== C5V3 ONLINE R2 NATIVE ARBITRATION ADVERSARIAL DIAGNOSTIC R1 ==='
printf 'ROLE=ONLINE_VERIFICATION\n'
printf 'TARGET_CLASS=R2_DIAGNOSTIC_ONLY_NOT_FINAL_RUNTIME_TARGET\n'
printf 'ROOT=%s\n' "$ROOT"
printf 'TEST_ROOT=%s\n' "$TEST_ROOT"
printf 'EXACT_PATHS_ONLY=YES\n'
printf 'DIRECTORY_WALK=NO\n'
printf 'FIND=NO\n'
printf 'GREP_RECURSIVE=NO\n'
printf 'NETWORK=NO\n'
printf 'PRODUCTION_STATE_WRITE=NO\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf 'HOST_CAPABILITY_EXECUTION=NO\n'
printf 'HOST_SEMANTIC_ORACLE=NO\n'
printf 'HOST_TASK_KIND_FIXTURE_PROVIDED=YES\n'

printf '%s\n' '=== 1. FROZEN IDENTITY LOCKS ==='
require_hash R2_SOURCE "$SRC" "$EXPECTED_SRC_SHA256"
require_hash R2_BYTECODE "$BIN" "$EXPECTED_BIN_SHA256"
require_hash LOCKED_VM "$VM" "$EXPECTED_VM_SHA256"
require_hash LIVE_MAIN_SOURCE "$LIVE_SRC" "$EXPECTED_LIVE_SRC_SHA256"
require_hash LIVE_RUNNER "$LIVE_RUNNER" "$EXPECTED_LIVE_RUNNER_SHA256"

SRC_BEFORE=$(hash1 "$SRC")
BIN_BEFORE=$(hash1 "$BIN")
LIVE_SRC_BEFORE=$(hash1 "$LIVE_SRC")
LIVE_RUNNER_BEFORE=$(hash1 "$LIVE_RUNNER")

# Runtime values are generated only AFTER source/bytecode identity freeze.
TOKEN=$(head -c 24 /dev/urandom | od -An -tx1 | tr -d ' \n')
[ -n "$TOKEN" ] || fail_closed DYNAMIC_TOKEN_GENERATION
PAYLOAD="UNSEEN_PROBLEM_${TOKEN}_same_raw_payload"
RESULT_A="UNSEEN_RESULT_A_${TOKEN}_alpha"
RESULT_B="UNSEEN_RESULT_B_${TOKEN}_omega"
PROV="PROV_${TOKEN}"

T1_ID="CAP_T1_${TOKEN}"
T2_ID="CAP_T2_${TOKEN}"
T3_ID="CAP_T3_${TOKEN}"
T4_ID="CAP_T4_${TOKEN}"

REG_ALL=$(printf '%s\n' \
    "ID=$T1_ID || FAMILY=T1 || STATE=ADMITTED" \
    "ID=$T2_ID || FAMILY=T2 || STATE=ADMITTED" \
    "ID=$T3_ID || FAMILY=T3 || STATE=ADMITTED" \
    "ID=$T4_ID || FAMILY=T4 || STATE=ADMITTED")

rm -rf -- "$TEST_ROOT"
mkdir -p "$TEST_ROOT/cases" "$TEST_ROOT/evidence"

setup_case() {
    label="$1"; task_kind="$2"; registry="$3"
    C="$TEST_ROOT/cases/$label"
    B="$C/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
    rm -rf -- "$C"
    mkdir -p "$B/io" "$B/state" "$B/out"

    for f in \
        event.txt catalog_page.txt catalog_page_id.txt catalog_page_eof.txt \
        segment_text.txt segment_status.txt segment_bytes.txt segment_eof.txt \
        segment_id.txt segment_offset.txt evidence_bundle.txt fetch_record.txt fetch_status.txt \
        capability_registry.txt capability_result_id.txt capability_result_status.txt \
        capability_result_kind.txt capability_result_payload.txt capability_result_provenance.txt \
        task_kind.txt task_payload.txt
    do : > "$B/io/$f"; done

    for f in \
        local_active_record.txt external_active_record.txt current_stream.txt request_bytes.txt \
        current_segment_eof.txt external_request.txt pending_capability_need.txt \
        pending_capability_id.txt pending_capability_context.txt current_objective.txt
    do : > "$B/state/$f"; done

    for f in \
        pending_candidates.txt updated_evidence.txt promoted_knowledge.txt hold_reason.txt \
        segment_accepted.txt capability_request.txt capability_args.txt capability_need.txt \
        task_result.txt provenance_receipt.txt action.txt target.txt status.txt
    do : > "$B/out/$f"; done

    printf '16384' > "$B/state/request_bytes.txt"
    printf 'NATIVE_TASK_READY' > "$B/io/event.txt"
    printf '%s' "$task_kind" > "$B/io/task_kind.txt"
    printf '%s' "$PAYLOAD" > "$B/io/task_payload.txt"
    printf '%s\n' "$registry" > "$B/io/capability_registry.txt"
}

common_prestate_hash() {
    C="$1"; B="$C/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
    {
        for rel in \
            io/event.txt io/task_kind.txt io/task_payload.txt \
            state/local_active_record.txt state/external_active_record.txt \
            state/current_stream.txt state/request_bytes.txt state/current_segment_eof.txt \
            state/external_request.txt state/pending_capability_need.txt \
            state/pending_capability_id.txt state/pending_capability_context.txt \
            state/current_objective.txt
        do
            printf 'FILE=%s\n' "$rel"
            cat "$B/$rel"
            printf '\n--END--\n'
        done
    } | sha256sum | awk '{print $1}'
}

registry_hash() {
    C="$1"; B="$C/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
    sha256sum "$B/io/capability_registry.txt" | awk '{print $1}'
}

run_vm_case() {
    label="$1"
    C="$TEST_ROOT/cases/$label"
    B="$C/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
    set +e
    (cd "$C" && "$VM" "$BIN") > "$C/stdout.log" 2> "$C/stderr.log"
    rc=$?
    set -e
    printf 'CASE_%s_VM_RC=%s\n' "$label" "$rc"
    printf 'CASE_%s_STDOUT_SHA256=%s\n' "$label" "$(hash1 "$C/stdout.log")"
    printf 'CASE_%s_STDERR_SHA256=%s\n' "$label" "$(hash1 "$C/stderr.log")"
    printf 'CASE_%s_ACTION=%s\n' "$label" "$(read1 "$B/out/action.txt")"
    printf 'CASE_%s_TARGET=%s\n' "$label" "$(read1 "$B/out/target.txt")"
    printf 'CASE_%s_STATUS=%s\n' "$label" "$(read1 "$B/out/status.txt")"
    printf 'CASE_%s_CAPABILITY_REQUEST=%s\n' "$label" "$(read1 "$B/out/capability_request.txt")"
    printf 'CASE_%s_CAPABILITY_NEED=%s\n' "$label" "$(read1 "$B/out/capability_need.txt")"
    printf 'CASE_%s_TASK_RESULT_SHA256=%s\n' "$label" "$(hash1 "$B/out/task_result.txt")"
    return "$rc"
}

remove_family() {
    family="$1"
    printf '%s\n' "$REG_ALL" | grep -v "FAMILY=$family" || true
}

PAIR_PASS=0
PAIR_FAIL=0
VM_INVOCATIONS=0

run_pair() {
    family="$1"; task_kind="$2"; cap_id="$3"; need="$4"
    LA="${family}_UNAVAILABLE"
    LB="${family}_AVAILABLE"
    REG_A=$(remove_family "$family")

    setup_case "$LA" "$task_kind" "$REG_A"
    setup_case "$LB" "$task_kind" "$REG_ALL"

    CA="$TEST_ROOT/cases/$LA"; CB="$TEST_ROOT/cases/$LB"
    HA=$(common_prestate_hash "$CA")
    HB=$(common_prestate_hash "$CB")
    RA=$(registry_hash "$CA")
    RB=$(registry_hash "$CB")
    printf 'PAIR_%s_COMMON_PRESTATE_A_SHA256=%s\n' "$family" "$HA"
    printf 'PAIR_%s_COMMON_PRESTATE_B_SHA256=%s\n' "$family" "$HB"
    printf 'PAIR_%s_REGISTRY_A_SHA256=%s\n' "$family" "$RA"
    printf 'PAIR_%s_REGISTRY_B_SHA256=%s\n' "$family" "$RB"

    run_vm_case "$LA" || true; VM_INVOCATIONS=$((VM_INVOCATIONS + 1))
    run_vm_case "$LB" || true; VM_INVOCATIONS=$((VM_INVOCATIONS + 1))

    BA="$CA/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
    BB="$CB/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
    ok=YES
    [ "$HA" = "$HB" ] || ok=NO
    [ "$RA" != "$RB" ] || ok=NO
    [ "$(read1 "$BA/out/action.txt")" = "WAIT_CAPABILITY" ] || ok=NO
    [ "$(read1 "$BA/out/target.txt")" = "$family" ] || ok=NO
    [ "$(read1 "$BA/out/status.txt")" = "NATIVE_NEED_DETECTED_CAPABILITY_NOT_ADMITTED" ] || ok=NO
    [ "$(read1 "$BA/out/capability_request.txt")" = "" ] || ok=NO
    [ "$(read1 "$BB/out/action.txt")" = "EXECUTE_CAPABILITY" ] || ok=NO
    [ "$(read1 "$BB/out/target.txt")" = "$cap_id" ] || ok=NO
    [ "$(read1 "$BB/out/status.txt")" = "NATIVE_CAPABILITY_SELECTED_FOR_TASK" ] || ok=NO
    [ "$(read1 "$BB/out/capability_request.txt")" = "$cap_id" ] || ok=NO
    [ "$(read1 "$BB/out/capability_need.txt")" = "$need" ] || ok=NO
    [ "$(read1 "$BB/out/capability_args.txt")" = "$PAYLOAD" ] || ok=NO

    if [ "$ok" = YES ]; then
        printf 'PAIR_%s_AVAILABILITY_COUNTERFACTUAL=PASS\n' "$family"
        PAIR_PASS=$((PAIR_PASS + 1))
    else
        printf 'PAIR_%s_AVAILABILITY_COUNTERFACTUAL=FAIL\n' "$family"
        PAIR_FAIL=$((PAIR_FAIL + 1))
    fi
}

printf '%s\n' '=== 2. CAPABILITY AVAILABILITY A/B ==='
run_pair T1 NUMERIC "$T1_ID" NUMERIC_ANALYZE
run_pair T2 STRUCTURE "$T2_ID" STRUCTURE_ANALYZE
run_pair T3 RETRIEVE "$T3_ID" RETRIEVE_EVIDENCE
run_pair T4 TEXT "$T4_ID" TEXT_SYNTAX_VIEW

printf '%s\n' '=== 3. SAME RAW PAYLOAD / HOST-SUPPLIED TASK_KIND CONTROL ==='
# The B lanes above have byte-identical raw TASK_PAYLOAD and identical full registry.
B1="$TEST_ROOT/cases/T1_AVAILABLE/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
B2="$TEST_ROOT/cases/T2_AVAILABLE/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
B3="$TEST_ROOT/cases/T3_AVAILABLE/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
B4="$TEST_ROOT/cases/T4_AVAILABLE/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
PH1=$(hash1 "$B1/io/task_payload.txt"); PH2=$(hash1 "$B2/io/task_payload.txt"); PH3=$(hash1 "$B3/io/task_payload.txt"); PH4=$(hash1 "$B4/io/task_payload.txt")
RH1=$(hash1 "$B1/io/capability_registry.txt"); RH2=$(hash1 "$B2/io/capability_registry.txt"); RH3=$(hash1 "$B3/io/capability_registry.txt"); RH4=$(hash1 "$B4/io/capability_registry.txt")
printf 'SAME_RAW_TASK_PAYLOAD_HASHES=%s,%s,%s,%s\n' "$PH1" "$PH2" "$PH3" "$PH4"
printf 'SAME_FULL_REGISTRY_HASHES=%s,%s,%s,%s\n' "$RH1" "$RH2" "$RH3" "$RH4"
TASK_KIND_CONTROLS=NO
if [ "$PH1" = "$PH2" ] && [ "$PH2" = "$PH3" ] && [ "$PH3" = "$PH4" ] && \
   [ "$RH1" = "$RH2" ] && [ "$RH2" = "$RH3" ] && [ "$RH3" = "$RH4" ] && \
   [ "$(read1 "$B1/out/target.txt")" = "$T1_ID" ] && \
   [ "$(read1 "$B2/out/target.txt")" = "$T2_ID" ] && \
   [ "$(read1 "$B3/out/target.txt")" = "$T3_ID" ] && \
   [ "$(read1 "$B4/out/target.txt")" = "$T4_ID" ]; then
    TASK_KIND_CONTROLS=YES
fi
printf 'R2_HOST_SUPPLIED_TASK_KIND_CAUSALLY_CONTROLS_SELECTED_FAMILY=%s\n' "$TASK_KIND_CONTROLS"
printf 'R2_RAW_PAYLOAD_DRIVEN_NEED_DETECTION=%s\n' "NOT_PROVEN"
printf 'R2_HOST_PROVIDED_TASK_CLASS_REQUIRED_BY_GENERIC_TASK_ABI=YES\n'

printf '%s\n' '=== 4. INVALID / NO-TOOL NEGATIVE ==='
setup_case INVALID_KIND GENERAL "$REG_ALL"
run_vm_case INVALID_KIND || true; VM_INVOCATIONS=$((VM_INVOCATIONS + 1))
BI="$TEST_ROOT/cases/INVALID_KIND/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
INVALID_PASS=NO
if [ "$(read1 "$BI/out/action.txt")" = "REFUSE_TASK_KIND" ] && \
   [ "$(read1 "$BI/out/status.txt")" = "REFUSE_TASK_KIND" ] && \
   [ "$(read1 "$BI/out/capability_request.txt")" = "" ]; then INVALID_PASS=YES; fi
printf 'INVALID_TASK_KIND_REFUSAL=%s\n' "$INVALID_PASS"
printf 'VALID_CAPABILITY_NOT_NEEDED_TASK_PATH=NOT_PRESENT_IN_R2_GENERIC_TASK_ABI\n'
printf 'NEGATIVE_UNNEEDED_CAPABILITY_SELECTION=NOT_PROVEN\n'

prepare_result_case() {
    label="$1"
    setup_case "$label" RETRIEVE "$REG_ALL"
    run_vm_case "$label" || true; VM_INVOCATIONS=$((VM_INVOCATIONS + 1))
}

run_result_event() {
    label="$1"; rid="$2"; status="$3"; kind="$4"; payload="$5"; prov="$6"
    C="$TEST_ROOT/cases/$label"; B="$C/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
    printf 'CAPABILITY_RESULT_READY' > "$B/io/event.txt"
    printf '%s' "$rid" > "$B/io/capability_result_id.txt"
    printf '%s' "$status" > "$B/io/capability_result_status.txt"
    printf '%s' "$kind" > "$B/io/capability_result_kind.txt"
    printf '%s' "$payload" > "$B/io/capability_result_payload.txt"
    printf '%s' "$prov" > "$B/io/capability_result_provenance.txt"
    run_vm_case "$label" || true; VM_INVOCATIONS=$((VM_INVOCATIONS + 1))
}

result_common_hash() {
    C="$1"; B="$C/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
    {
        for rel in \
            io/event.txt io/task_kind.txt io/task_payload.txt io/capability_registry.txt \
            io/capability_result_id.txt io/capability_result_status.txt \
            io/capability_result_kind.txt io/capability_result_provenance.txt \
            state/pending_capability_need.txt state/pending_capability_id.txt \
            state/pending_capability_context.txt state/current_objective.txt
        do printf 'FILE=%s\n' "$rel"; cat "$B/$rel"; printf '\n--END--\n'; done
    } | sha256sum | awk '{print $1}'
}

printf '%s\n' '=== 5. CAPABILITY RESULT ID / STATUS / PAYLOAD DIAGNOSTIC ==='
prepare_result_case RESULT_WRONG_ID
run_result_event RESULT_WRONG_ID "WRONG_${TOKEN}" OK DIAG_RESULT "$RESULT_A" "$PROV"
BR="$TEST_ROOT/cases/RESULT_WRONG_ID/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
WRONG_ID_PASS=NO
if [ "$(read1 "$BR/out/action.txt")" = "REFUSE_CAPABILITY_RESULT" ] && \
   [ "$(read1 "$BR/state/pending_capability_id.txt")" = "$T3_ID" ]; then WRONG_ID_PASS=YES; fi
printf 'CAPABILITY_RESULT_ID_GATING=%s\n' "$WRONG_ID_PASS"

prepare_result_case RESULT_HOLD_STATUS
run_result_event RESULT_HOLD_STATUS "$T3_ID" HOLD DIAG_RESULT "$RESULT_A" "$PROV"
BH="$TEST_ROOT/cases/RESULT_HOLD_STATUS/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
HOLD_STATUS_PASS=NO
if [ "$(read1 "$BH/out/action.txt")" = "CAPABILITY_HOLD" ] && \
   [ "$(read1 "$BH/out/status.txt")" = "NATIVE_CAPABILITY_EXECUTION_NOT_OK" ]; then HOLD_STATUS_PASS=YES; fi
printf 'CAPABILITY_RESULT_STATUS_GATING=%s\n' "$HOLD_STATUS_PASS"

prepare_result_case RESULT_OK_A
CA="$TEST_ROOT/cases/RESULT_OK_A"
BA="$CA/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
printf 'CAPABILITY_RESULT_READY' > "$BA/io/event.txt"
printf '%s' "$T3_ID" > "$BA/io/capability_result_id.txt"
printf 'OK' > "$BA/io/capability_result_status.txt"
printf 'DIAG_RESULT' > "$BA/io/capability_result_kind.txt"
printf '%s' "$RESULT_A" > "$BA/io/capability_result_payload.txt"
printf '%s' "$PROV" > "$BA/io/capability_result_provenance.txt"
HA=$(result_common_hash "$CA")
run_vm_case RESULT_OK_A || true; VM_INVOCATIONS=$((VM_INVOCATIONS + 1))

prepare_result_case RESULT_OK_B
CB="$TEST_ROOT/cases/RESULT_OK_B"
BB="$CB/.sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
printf 'CAPABILITY_RESULT_READY' > "$BB/io/event.txt"
printf '%s' "$T3_ID" > "$BB/io/capability_result_id.txt"
printf 'OK' > "$BB/io/capability_result_status.txt"
printf 'DIAG_RESULT' > "$BB/io/capability_result_kind.txt"
printf '%s' "$RESULT_B" > "$BB/io/capability_result_payload.txt"
printf '%s' "$PROV" > "$BB/io/capability_result_provenance.txt"
HB=$(result_common_hash "$CB")
run_vm_case RESULT_OK_B || true; VM_INVOCATIONS=$((VM_INVOCATIONS + 1))

OK_A_ACTION=$(read1 "$BA/out/action.txt"); OK_B_ACTION=$(read1 "$BB/out/action.txt")
OK_A_STATUS=$(read1 "$BA/out/status.txt"); OK_B_STATUS=$(read1 "$BB/out/status.txt")
OK_A_TARGET=$(read1 "$BA/out/target.txt"); OK_B_TARGET=$(read1 "$BB/out/target.txt")
OK_A_RESULT=$(read1 "$BA/out/task_result.txt"); OK_B_RESULT=$(read1 "$BB/out/task_result.txt")
printf 'RESULT_OK_COMMON_PRESTATE_EXCLUDING_PAYLOAD_A_SHA256=%s\n' "$HA"
printf 'RESULT_OK_COMMON_PRESTATE_EXCLUDING_PAYLOAD_B_SHA256=%s\n' "$HB"
printf 'RESULT_OK_A_TASK_RESULT_SHA256=%s\n' "$(hash1 "$BA/out/task_result.txt")"
printf 'RESULT_OK_B_TASK_RESULT_SHA256=%s\n' "$(hash1 "$BB/out/task_result.txt")"
RESULT_PASS_THROUGH=NO
if [ "$HA" = "$HB" ] && [ "$OK_A_RESULT" = "$RESULT_A" ] && [ "$OK_B_RESULT" = "$RESULT_B" ]; then RESULT_PASS_THROUGH=YES; fi
DECISION_SAME=NO
if [ "$OK_A_ACTION" = "$OK_B_ACTION" ] && [ "$OK_A_STATUS" = "$OK_B_STATUS" ] && [ "$OK_A_TARGET" = "$OK_B_TARGET" ]; then DECISION_SAME=YES; fi
printf 'NATIVE_TASK_RESULT_BYTE_PASS_THROUGH=%s\n' "$RESULT_PASS_THROUGH"
printf 'MATERIALLY_DIFFERENT_RESULT_PAYLOADS_NEXT_DECISION_IDENTICAL=%s\n' "$DECISION_SAME"
printf 'CAPABILITY_RESULT_CONTENT_CAUSALLY_AFFECTS_NEXT_NATIVE_DECISION=NOT_PROVEN\n'
printf 'NATIVE_CAPABILITY_RESULT_EVALUATION=NOT_PROVEN_CONTENT_INSENSITIVE_GENERIC_TASK_PATH\n'

printf '%s\n' '=== 6. DYNAMIC TOKEN LEAK + FREEZE RECHECK ==='
LEAK_SRC=0; LEAK_BIN=0
if grep -aFq "$TOKEN" "$SRC" 2>/dev/null; then LEAK_SRC=1; fi
if grep -aFq "$TOKEN" "$BIN" 2>/dev/null; then LEAK_BIN=1; fi
printf 'DYNAMIC_TOKEN_LEAK_IN_SOURCE=%s\n' "$LEAK_SRC"
printf 'DYNAMIC_TOKEN_LEAK_IN_BYTECODE=%s\n' "$LEAK_BIN"

SRC_AFTER=$(hash1 "$SRC")
BIN_AFTER=$(hash1 "$BIN")
LIVE_SRC_AFTER=$(hash1 "$LIVE_SRC")
LIVE_RUNNER_AFTER=$(hash1 "$LIVE_RUNNER")
printf 'R2_SOURCE_UNCHANGED=%s\n' "$([ "$SRC_BEFORE" = "$SRC_AFTER" ] && echo YES || echo NO)"
printf 'R2_BYTECODE_UNCHANGED=%s\n' "$([ "$BIN_BEFORE" = "$BIN_AFTER" ] && echo YES || echo NO)"
printf 'LIVE_CORE_UNCHANGED=%s\n' "$([ "$LIVE_SRC_BEFORE" = "$LIVE_SRC_AFTER" ] && echo YES || echo NO)"
printf 'LIVE_RUNNER_UNCHANGED=%s\n' "$([ "$LIVE_RUNNER_BEFORE" = "$LIVE_RUNNER_AFTER" ] && echo YES || echo NO)"

printf '%s\n' '=== 7. DIAGNOSTIC VERDICT ==='
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$VM_INVOCATIONS"
printf 'AVAILABILITY_COUNTERFACTUAL_PASS_COUNT=%s\n' "$PAIR_PASS"
printf 'AVAILABILITY_COUNTERFACTUAL_FAIL_COUNT=%s\n' "$PAIR_FAIL"
printf 'R2_NATIVE_REGISTRY_SELECTION_MECHANICS=%s\n' "$([ "$PAIR_FAIL" -eq 0 ] && [ "$PAIR_PASS" -eq 4 ] && echo PASS_DIAGNOSTIC || echo FAIL_DIAGNOSTIC)"
printf 'R2_NATIVE_CAPABILITY_NEED_DETECTION_FROM_RAW_PROBLEM=NOT_PROVEN_HOST_TASK_KIND_CONTROLS_FAMILY\n'
printf 'R2_NATIVE_CAPABILITY_SELECTION_FROM_REGISTRY=PASS_DIAGNOSTIC_IF_ABOVE_GATES_PASS\n'
printf 'R2_NATIVE_CAPABILITY_EXECUTION=NOT_TESTED_NO_EXTERNAL_CAPABILITY_EXECUTED\n'
printf 'R2_NATIVE_CAPABILITY_RESULT_ID_STATUS_GATING=PASS_DIAGNOSTIC_IF_ABOVE_GATES_PASS\n'
printf 'R2_NATIVE_CAPABILITY_RESULT_CONTENT_EVALUATION=NOT_PROVEN\n'
printf 'R2_NATIVE_LEARNING_UPDATE=NOT_PRESENT_IN_GENERIC_TASK_DIAGNOSTIC\n'
printf 'R2_FRESH_RESTART_LEARNED_STATE_REUSE=NOT_APPLICABLE_NO_LEARNING_UPDATE_PROVEN\n'
printf 'R2_VALID_NO_TOOL_ARBITRATION=NOT_PROVEN\n'
printf 'HOST_CAPABILITY_DEMAND_GENERATION=FIXTURE_TASK_KIND_PRESENT_SO_FINAL_NO_CLAIM_FOR_R2\n'
printf 'HOST_TOOL_SELECTION=NO_TOOL_EXECUTION_IN_HARNESS\n'
printf 'HOST_REASONING=NO_SEMANTIC_ORACLE\n'
printf 'HOST_LEARNING=NO\n'
printf 'C5V3_NATIVE_CAPABILITY_UTILIZATION=NOT_ADMITTED_ON_R2_DIAGNOSTIC\n'
printf 'C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=NOT_PROVEN\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf 'CLAIM_LEQ_MACHINE_EVIDENCE=YES\n'
printf '%s\n' '=== END ==='
