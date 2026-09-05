#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"

STATE="$HOME_SIGMA/SIGMA_V4PK1_PERSISTENT_SEMANTIC_HYPERGRAPH_PREFLIGHT"
SHADOW="$STATE/shadow"
BRAIN="$SHADOW/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
BASE="$E/SIGMA_V4PK1_PERSISTENT_SEMANTIC_HYPERGRAPH"
IN="$BASE/input"
STORE_DIR="$BASE/state"
STORE="$STORE_DIR/hypergraph.memory"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC_REPO="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_V4_PERSISTENT_SEMANTIC_HYPERGRAPH_V4PK1.sigma"
SRC="$E/SIGMA_V4_PERSISTENT_SEMANTIC_HYPERGRAPH_V4PK1.sigma"
BC="$E/SIGMA_V4_PERSISTENT_SEMANTIC_HYPERGRAPH_V4PK1.sigmab"
EXPECTED_SOURCE_BLOB=80e730c5a76bfe1728bffede735ae8964041fcf8

mkdir -p "$E" "$IN" "$STORE_DIR" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4PK1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
SOURCE_SHA=$(hash1 "$SRC_REPO")
SOURCE_BLOB=$("$P/bin/git" -C "$REPO" hash-object "$SRC_REPO")
RUNNER_SHA=$(hash1 "$0")

printf 'SIGMA_PHASE=V4PK1_PERSISTENT_SEMANTIC_HYPERGRAPH_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'SOURCE_GIT_BLOB=%s\n' "$SOURCE_BLOB"
printf 'SOURCE_SHA256=%s\n' "$SOURCE_SHA"
printf 'RUNNER_SHA256=%s\n' "$RUNNER_SHA"
printf 'SHADOW_BRAIN=%s\n' "$BRAIN"
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'HOST_HYPEREDGE_ADMISSION_DECISION=NO\n'
printf 'HOST_WEIGHT_DECISION=NO\n'
printf 'HOST_EVIDENCE_DECISION=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'PYTHON_USED=NO\n'

V24_PID_BEFORE=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_BEFORE=%s\n' "$V24_PID_BEFORE"

if [ "$SIGMAC_SHA" != "$EXPECTED_SIGMAC" ]; then
    printf 'HOLD=LOCKED_SIGMAC_IDENTITY_MISMATCH\n'
    exit 21
fi
if [ "$VM_SHA" != "$EXPECTED_VM" ]; then
    printf 'HOLD=LOCKED_VM_IDENTITY_MISMATCH\n'
    exit 22
fi
if [ "$SOURCE_BLOB" != "$EXPECTED_SOURCE_BLOB" ]; then
    printf 'HOLD=SOURCE_GIT_BLOB_IDENTITY_MISMATCH\n'
    exit 23
fi

for TOKEN in node-alpha edge-A evidence-A provenance-A; do
    if "$P/bin/grep" -F "$TOKEN" "$SRC_REPO" >/dev/null 2>&1; then
        printf 'HOLD=FIXTURE_TOKEN_LEAK_IN_SOURCE TOKEN=%s\n' "$TOKEN"
        exit 24
    fi
done

cp -- "$SRC_REPO" "$SRC" || { printf 'HOLD=SOURCE_INSTALL_FAILED\n'; exit 25; }
INSTALLED_SOURCE_SHA=$(hash1 "$SRC")
printf 'INSTALLED_SOURCE_SHA256=%s\n' "$INSTALLED_SOURCE_SHA"
[ "$INSTALLED_SOURCE_SHA" = "$SOURCE_SHA" ] || { printf 'HOLD=INSTALLED_SOURCE_IDENTITY_MISMATCH\n'; exit 26; }

SOURCE_SHA_BEFORE=$(hash1 "$SRC_REPO")
rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'V4PK1_SIGMAC_RC=%s\n' "$RC"
if [ "$RC" -ne 0 ] || [ ! -s "$BC.partial" ]; then
    printf 'HOLD=V4PK1_COMPILE_FAILED\n'
    exit 27
fi
mv -f -- "$BC.partial" "$BC"
chmod 0400 "$BC"
BYTECODE_SHA_BEFORE=$(hash1 "$BC")
printf 'V4PK1_BYTECODE_SHA256=%s\n' "$BYTECODE_SHA_BEFORE"

run_case() {
    NAME="$1"
    RUNLOG="$LOG/$NAME.log"
    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?
    printf '\n=== %s ===\n' "$NAME"
    printf 'VM_RC=%s\n' "$RC"
    cat "$RUNLOG"
    return "$RC"
}

write_input() {
    printf '%s' "$2" > "$IN/$1"
}

set_edge() {
    write_input case_id.txt "$1"
    write_input edge_id.txt "$2"
    write_input relation.txt "$3"
    write_input member_1.txt "$4"
    write_input member_2.txt "$5"
    write_input member_3.txt "$6"
    write_input member_4.txt "$7"
    write_input evidence_id.txt "$8"
    write_input provenance_id.txt "$9"
    shift 9
    write_input weight_bp.txt "$1"
    write_input uncertainty_bp.txt "$2"
    write_input commit_token.txt YES
}

expect_line() {
    FILE="$1"
    TEXT="$2"
    CODE="$3"
    "$P/bin/grep" -F "$TEXT" "$FILE" >/dev/null || exit "$CODE"
}

reset_store() {
    : > "$STORE"
}

reset_store
set_edge case-a edge-A rel-A node-alpha node-beta node-gamma NONE evidence-A provenance-A 8400 1600
run_case A_CREATE_3ARY || exit 50
expect_line "$LOG/A_CREATE_3ARY.log" 'V4PK1_STATUS EDGE_COMMITTED' 51
expect_line "$LOG/A_CREATE_3ARY.log" 'STATE_VALID 1' 52
expect_line "$LOG/A_CREATE_3ARY.log" 'MEMBER_COUNT 3' 53
expect_line "$LOG/A_CREATE_3ARY.log" 'MEMBERS_DISTINCT 1' 54
expect_line "$LOG/A_CREATE_3ARY.log" 'WRITE_READBACK_MATCH 1' 55
expect_line "$LOG/A_CREATE_3ARY.log" 'STATE_MUTATED 1' 56
expect_line "$LOG/A_CREATE_3ARY.log" 'EDGE_COUNT_AFTER 1' 57
expect_line "$LOG/A_CREATE_3ARY.log" 'ANCHOR_INCIDENT_EDGE_COUNT_AFTER 1' 58
expect_line "$LOG/A_CREATE_3ARY.log" 'ANCHOR_WEIGHT_SUM_BP_AFTER 8400' 59
[ -s "$STORE" ] || exit 60
STORE_SHA_AFTER_A=$(hash1 "$STORE")

run_case A_REPLAY_FRESH_VM_IDEMPOTENT || exit 61
expect_line "$LOG/A_REPLAY_FRESH_VM_IDEMPOTENT.log" 'V4PK1_STATUS ALREADY_COMMITTED_SAME_EDGE' 62
expect_line "$LOG/A_REPLAY_FRESH_VM_IDEMPOTENT.log" 'EXACT_EDGE_ALREADY_PRESENT 1' 63
expect_line "$LOG/A_REPLAY_FRESH_VM_IDEMPOTENT.log" 'STATE_MUTATED 0' 64
expect_line "$LOG/A_REPLAY_FRESH_VM_IDEMPOTENT.log" 'EDGE_COUNT_BEFORE 1' 65
expect_line "$LOG/A_REPLAY_FRESH_VM_IDEMPOTENT.log" 'EDGE_COUNT_AFTER 1' 66
[ "$(hash1 "$STORE")" = "$STORE_SHA_AFTER_A" ] || exit 67

set_edge case-conflict edge-A rel-CONFLICT node-alpha node-beta node-gamma NONE evidence-A provenance-A 8400 1600
STORE_SHA_BEFORE_CONFLICT=$(hash1 "$STORE")
run_case A_EDGE_ID_CONFLICT || exit 68
expect_line "$LOG/A_EDGE_ID_CONFLICT.log" 'V4PK1_STATUS REFUSE_EDGE_ID_CONFLICT' 69
expect_line "$LOG/A_EDGE_ID_CONFLICT.log" 'EDGE_ID_CONFLICT 1' 70
expect_line "$LOG/A_EDGE_ID_CONFLICT.log" 'WRITE_ATTEMPTED 0' 71
expect_line "$LOG/A_EDGE_ID_CONFLICT.log" 'STATE_MUTATED 0' 72
[ "$(hash1 "$STORE")" = "$STORE_SHA_BEFORE_CONFLICT" ] || exit 73

set_edge case-b edge-B rel-B node-alpha node-delta NONE NONE evidence-B provenance-B 6100 3900
run_case B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A || exit 74
expect_line "$LOG/B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A.log" 'V4PK1_STATUS EDGE_COMMITTED' 75
expect_line "$LOG/B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A.log" 'MEMBER_COUNT 2' 76
expect_line "$LOG/B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A.log" 'EDGE_COUNT_BEFORE 1' 77
expect_line "$LOG/B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A.log" 'EDGE_COUNT_AFTER 2' 78
expect_line "$LOG/B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A.log" 'ANCHOR_INCIDENT_EDGE_COUNT_BEFORE 1' 79
expect_line "$LOG/B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A.log" 'ANCHOR_INCIDENT_EDGE_COUNT_AFTER 2' 80
expect_line "$LOG/B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A.log" 'ANCHOR_WEIGHT_SUM_BP_BEFORE 8400' 81
expect_line "$LOG/B_CREATE_2ARY_FRESH_VM_WITH_PERSISTED_A.log" 'ANCHOR_WEIGHT_SUM_BP_AFTER 14500' 82
STORE_SHA_AFTER_B=$(hash1 "$STORE")

set_edge case-one-member edge-C rel-C node-alone NONE NONE NONE evidence-C provenance-C 5000 5000
run_case C_REFUSE_ONE_MEMBER || exit 83
expect_line "$LOG/C_REFUSE_ONE_MEMBER.log" 'V4PK1_STATUS REFUSE_INVALID_HYPEREDGE_SHAPE' 84
expect_line "$LOG/C_REFUSE_ONE_MEMBER.log" 'STATE_MUTATED 0' 85
[ "$(hash1 "$STORE")" = "$STORE_SHA_AFTER_B" ] || exit 86

set_edge case-duplicate edge-D rel-D node-dup node-dup NONE NONE evidence-D provenance-D 5000 5000
run_case D_REFUSE_DUPLICATE_MEMBER || exit 87
expect_line "$LOG/D_REFUSE_DUPLICATE_MEMBER.log" 'V4PK1_STATUS REFUSE_DUPLICATE_HYPEREDGE_MEMBER' 88
expect_line "$LOG/D_REFUSE_DUPLICATE_MEMBER.log" 'MEMBERS_DISTINCT 0' 89
expect_line "$LOG/D_REFUSE_DUPLICATE_MEMBER.log" 'STATE_MUTATED 0' 90
[ "$(hash1 "$STORE")" = "$STORE_SHA_AFTER_B" ] || exit 91

set_edge case-weight edge-E rel-E node-e1 node-e2 NONE NONE evidence-E provenance-E 10001 0
run_case E_REFUSE_WEIGHT_RANGE || exit 92
expect_line "$LOG/E_REFUSE_WEIGHT_RANGE.log" 'V4PK1_STATUS REFUSE_WEIGHT_RANGE' 93
expect_line "$LOG/E_REFUSE_WEIGHT_RANGE.log" 'WEIGHT_RANGE_VALID 0' 94
expect_line "$LOG/E_REFUSE_WEIGHT_RANGE.log" 'STATE_MUTATED 0' 95
[ "$(hash1 "$STORE")" = "$STORE_SHA_AFTER_B" ] || exit 96

set_edge case-uncertainty edge-F rel-F node-f1 node-f2 NONE NONE evidence-F provenance-F 0 10001
run_case F_REFUSE_UNCERTAINTY_RANGE || exit 97
expect_line "$LOG/F_REFUSE_UNCERTAINTY_RANGE.log" 'V4PK1_STATUS REFUSE_UNCERTAINTY_RANGE' 98
expect_line "$LOG/F_REFUSE_UNCERTAINTY_RANGE.log" 'UNCERTAINTY_RANGE_VALID 0' 99
expect_line "$LOG/F_REFUSE_UNCERTAINTY_RANGE.log" 'STATE_MUTATED 0' 100
[ "$(hash1 "$STORE")" = "$STORE_SHA_AFTER_B" ] || exit 101

set_edge case-delimiter edge-G 'rel||unsafe' node-g1 node-g2 NONE NONE evidence-G provenance-G 4000 6000
run_case G_REFUSE_UNSAFE_TOKEN || exit 102
expect_line "$LOG/G_REFUSE_UNSAFE_TOKEN.log" 'V4PK1_STATUS REFUSE_INVALID_INPUT' 103
expect_line "$LOG/G_REFUSE_UNSAFE_TOKEN.log" 'INPUT_TOKEN_VALID 0' 104
expect_line "$LOG/G_REFUSE_UNSAFE_TOKEN.log" 'STATE_MUTATED 0' 105
[ "$(hash1 "$STORE")" = "$STORE_SHA_AFTER_B" ] || exit 106

printf '\nBROKEN_RECORD' >> "$STORE"
STORE_SHA_AFTER_FAULT_INJECTION=$(hash1 "$STORE")
set_edge case-malformed-store edge-H rel-H node-h1 node-h2 NONE NONE evidence-H provenance-H 5000 5000
run_case H_REFUSE_MALFORMED_PERSISTENT_STORE || exit 107
expect_line "$LOG/H_REFUSE_MALFORMED_PERSISTENT_STORE.log" 'V4PK1_STATUS REFUSE_INVALID_STORE' 108
expect_line "$LOG/H_REFUSE_MALFORMED_PERSISTENT_STORE.log" 'STATE_VALID 0' 109
expect_line "$LOG/H_REFUSE_MALFORMED_PERSISTENT_STORE.log" 'INVALID_STATE_RECORD_COUNT 1' 110
expect_line "$LOG/H_REFUSE_MALFORMED_PERSISTENT_STORE.log" 'WRITE_ATTEMPTED 0' 111
expect_line "$LOG/H_REFUSE_MALFORMED_PERSISTENT_STORE.log" 'STATE_MUTATED 0' 112
[ "$(hash1 "$STORE")" = "$STORE_SHA_AFTER_FAULT_INJECTION" ] || exit 113

if "$P/bin/grep" -E -i 'step[ _-]*limit' "$LOG"/*.log >/dev/null 2>&1; then
    printf 'HOLD=STEP_LIMIT_OBSERVED\n'
    exit 114
fi

SOURCE_SHA_AFTER=$(hash1 "$SRC_REPO")
BYTECODE_SHA_AFTER=$(hash1 "$BC")
printf 'SOURCE_SHA256_AFTER_TEST=%s\n' "$SOURCE_SHA_AFTER"
printf 'BYTECODE_SHA256_AFTER_TEST=%s\n' "$BYTECODE_SHA_AFTER"
[ "$SOURCE_SHA_AFTER" = "$SOURCE_SHA_BEFORE" ] || { printf 'HOLD=SOURCE_MUTATED\n'; exit 115; }
[ "$BYTECODE_SHA_AFTER" = "$BYTECODE_SHA_BEFORE" ] || { printf 'HOLD=BYTECODE_MUTATED\n'; exit 116; }

V24_PID_AFTER=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AFTER=%s\n' "$V24_PID_AFTER"
if [ -n "$V24_PID_BEFORE" ] && [ "$V24_PID_AFTER" != "$V24_PID_BEFORE" ]; then
    printf 'HOLD=PRODUCTION_V24_PID_CHANGED\n'
    exit 117
fi

printf '\nV4PK1_PERSISTENT_SEMANTIC_HYPERGRAPH_PREFLIGHT=PASS\n'
printf 'NATIVE_HYPEREDGE_VALIDATION=PASS\n'
printf 'NATIVE_PERSISTENT_HYPEREDGE_COMMIT=PASS\n'
printf 'FRESH_VM_PERSISTENT_STATE_REUSE=PASS\n'
printf 'EXACT_REPLAY_IDEMPOTENCY=PASS\n'
printf 'EDGE_ID_CONFLICT_REFUSAL=PASS\n'
printf 'NARY_MEMBER_SHAPE_AND_DISTINCTNESS=PASS\n'
printf 'WEIGHT_UNCERTAINTY_RANGE_GATES=PASS\n'
printf 'MALFORMED_STORE_REFUSAL=PASS\n'
printf 'NATIVE_ANCHOR_INCIDENT_AGGREGATION=PASS\n'
printf 'SOURCE_AND_BYTECODE_IMMUTABLE_DURING_TEST=PASS\n'
printf 'STEP_LIMIT_NOT_OBSERVED_IN_BOUNDED_CASES=YES\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'CRASH_CONSISTENT_HYPERGRAPH_WRITE=NOT_PROVEN\n'
printf 'MULTI_HOP_REASONING=NOT_EXECUTED\n'
printf 'CONTROLLED_INFERENCE=NOT_EXECUTED\n'
printf 'PRODUCTION_BINDING=NO\n'