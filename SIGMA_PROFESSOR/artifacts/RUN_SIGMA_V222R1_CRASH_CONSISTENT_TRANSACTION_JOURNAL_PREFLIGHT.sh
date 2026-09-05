#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BRAIN="$REPO/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC="$E/SIGMA_CRASH_CONSISTENT_TRANSACTION_JOURNAL_V2_22R1.sigma"
BC="$E/SIGMA_CRASH_CONSISTENT_TRANSACTION_JOURNAL_V2_22R1.sigmab"
EXPECTED_SOURCE=643c6f534777193951d772e9653463b5d97ceebb7c35f14b21390a3308ef4c64

MODE_MEM="$E/SIGMA_V222R1_MODE.memory"
TX_ID_MEM="$E/SIGMA_V222R1_TX_ID.memory"
TX_PAYLOAD_MEM="$E/SIGMA_V222R1_TX_PAYLOAD.memory"
JOURNAL_PATH_MEM="$E/SIGMA_V222R1_JOURNAL_PATH.memory"
RECOVERED_MEM="$E/SIGMA_V222R1_RECOVERED_PAYLOAD.memory"

STATE="$HOME_SIGMA/SIGMA_V222R1_CRASH_CONSISTENT_TRANSACTION_PREFLIGHT"
LOG="$STATE/log"
JOURNAL="$STATE/transaction.journal"
REPLAY="$STATE/replay.journal"
CONFLICT="$STATE/conflict.journal"
OVER="$STATE/overlimit.journal"
LOCK="$STATE/preflight.lock"

mkdir -p "$STATE" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V222R1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
SOURCE_SHA=$(hash1 "$SRC")

printf 'SIGMA_PHASE=V222R1_CRASH_CONSISTENT_TRANSACTION_JOURNAL_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'SOURCE_SHA256=%s\n' "$SOURCE_SHA"
printf 'HOST_TRANSACTION_DECISION=NO\n'
printf 'HOST_RECOVERY_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'TORN_PREPARE_TAIL_TEST=YES\n'
printf 'TORN_COMMIT_TAIL_TEST=YES\n'
printf 'PREPARE_ONLY_RESTART_TEST=YES\n'
printf 'IDEMPOTENT_COMMIT_RESTART_TEST=YES\n'
printf 'CONFLICT_REFUSAL_TEST=YES\n'
printf 'PHYSICAL_APPEND_ATOMICITY_CLAIMED=NO\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || exit 21
[ "$VM_SHA" = "$EXPECTED_VM" ] || exit 22
[ "$SOURCE_SHA" = "$EXPECTED_SOURCE" ] || exit 23

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'V222_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || exit 24
[ -s "$BC.partial" ] || exit 25
"$P/bin/mv" -f -- "$BC.partial" "$BC"
"$P/bin/chmod" 0400 "$BC"
BC_SHA=$(hash1 "$BC")
printf 'V222_BYTECODE_SHA256=%s\n' "$BC_SHA"

run_v222() {
    CASE_NAME="$1"
    RUNLOG="$LOG/$CASE_NAME.log"
    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?
    printf '\n=== %s ===\n' "$CASE_NAME"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"
    return "$RC"
}

set_inputs() {
    MODE="$1"; TX="$2"; PAYLOAD="$3"; JP="$4"
    "$P/bin/printf" '%s' "$MODE" > "$MODE_MEM"
    "$P/bin/printf" '%s' "$TX" > "$TX_ID_MEM"
    "$P/bin/printf" '%s' "$PAYLOAD" > "$TX_PAYLOAD_MEM"
    "$P/bin/printf" '%s' "$JP" > "$JOURNAL_PATH_MEM"
}

: > "$JOURNAL"
set_inputs COMMIT_TRANSACTION A 'event-A' "$JOURNAL"
run_v222 BASELINE_COMMIT_A || exit 50
"$P/bin/grep" -F 'FINAL_RECOVERED_TX A' "$LOG/BASELINE_COMMIT_A.log" >/dev/null || exit 51
"$P/bin/grep" -F 'FINAL_RECOVERED_PAYLOAD event-A' "$LOG/BASELINE_COMMIT_A.log" >/dev/null || exit 52
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'event-A' ] || exit 53
BASE_A_SHA=$(hash1 "$JOURNAL")
printf 'BASELINE_A_JOURNAL_SHA256=%s\n' "$BASE_A_SHA"

run_v222 BASELINE_A_FRESH_VM_IDEMPOTENT || exit 54
"$P/bin/grep" -F 'INPUT_ALREADY_COMMITTED 1' "$LOG/BASELINE_A_FRESH_VM_IDEMPOTENT.log" >/dev/null || exit 55
"$P/bin/grep" -F 'PREPARE_APPEND_PERFORMED 0' "$LOG/BASELINE_A_FRESH_VM_IDEMPOTENT.log" >/dev/null || exit 56
"$P/bin/grep" -F 'COMMIT_APPEND_PERFORMED 0' "$LOG/BASELINE_A_FRESH_VM_IDEMPOTENT.log" >/dev/null || exit 57
[ "$(hash1 "$JOURNAL")" = "$BASE_A_SHA" ] || exit 58

set_inputs PREPARE_ONLY B 'event-B' "$JOURNAL"
run_v222 PREPARE_ONLY_B || exit 59
"$P/bin/grep" -F 'PREPARE_APPEND_PERFORMED 1' "$LOG/PREPARE_ONLY_B.log" >/dev/null || exit 60
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'event-A' ] || exit 61
PREP_B_SHA=$(hash1 "$JOURNAL")

set_inputs RECOVER_ONLY '' '' "$JOURNAL"
run_v222 RECOVER_AFTER_PREPARE_ONLY_B || exit 62
"$P/bin/grep" -F 'FINAL_RECOVERED_TX A' "$LOG/RECOVER_AFTER_PREPARE_ONLY_B.log" >/dev/null || exit 63
"$P/bin/grep" -F 'FINAL_RECOVERED_PAYLOAD event-A' "$LOG/RECOVER_AFTER_PREPARE_ONLY_B.log" >/dev/null || exit 64
[ "$(hash1 "$JOURNAL")" = "$PREP_B_SHA" ] || exit 65

set_inputs COMMIT_TRANSACTION B 'event-B' "$JOURNAL"
run_v222 COMMIT_B_AFTER_PREPARED_RESTART || exit 66
"$P/bin/grep" -F 'INPUT_PREPARED 1' "$LOG/COMMIT_B_AFTER_PREPARED_RESTART.log" >/dev/null || exit 67
"$P/bin/grep" -F 'PREPARE_APPEND_PERFORMED 0' "$LOG/COMMIT_B_AFTER_PREPARED_RESTART.log" >/dev/null || exit 68
"$P/bin/grep" -F 'COMMIT_APPEND_PERFORMED 1' "$LOG/COMMIT_B_AFTER_PREPARED_RESTART.log" >/dev/null || exit 69
"$P/bin/grep" -F 'FINAL_RECOVERED_TX B' "$LOG/COMMIT_B_AFTER_PREPARED_RESTART.log" >/dev/null || exit 70
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'event-B' ] || exit 71
COMMIT_B_SHA=$(hash1 "$JOURNAL")

"$P/bin/printf" '\nTX=C || PHASE=PREPARE || PAYLOAD=event-C' >> "$JOURNAL"
TORN_PREP_SHA=$(hash1 "$JOURNAL")
set_inputs RECOVER_ONLY '' '' "$JOURNAL"
run_v222 RECOVER_WITH_TORN_PREPARE_C || exit 72
"$P/bin/grep" -F 'IGNORED_MALFORMED_RECORD_COUNT 1' "$LOG/RECOVER_WITH_TORN_PREPARE_C.log" >/dev/null || exit 73
"$P/bin/grep" -F 'FINAL_RECOVERED_TX B' "$LOG/RECOVER_WITH_TORN_PREPARE_C.log" >/dev/null || exit 74
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'event-B' ] || exit 75
[ "$(hash1 "$JOURNAL")" = "$TORN_PREP_SHA" ] || exit 76

set_inputs COMMIT_TRANSACTION C 'event-C' "$JOURNAL"
run_v222 RETRY_AFTER_TORN_PREPARE_C || exit 77
"$P/bin/grep" -F 'PREPARE_APPEND_PERFORMED 1' "$LOG/RETRY_AFTER_TORN_PREPARE_C.log" >/dev/null || exit 78
"$P/bin/grep" -F 'COMMIT_APPEND_PERFORMED 1' "$LOG/RETRY_AFTER_TORN_PREPARE_C.log" >/dev/null || exit 79
"$P/bin/grep" -F 'FINAL_RECOVERED_TX C' "$LOG/RETRY_AFTER_TORN_PREPARE_C.log" >/dev/null || exit 80
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'event-C' ] || exit 81

set_inputs PREPARE_ONLY D 'event-D' "$JOURNAL"
run_v222 PREPARE_D || exit 82
"$P/bin/printf" '\nTX=D || PHASE=COMMIT || PAYLOAD=event-D || TXLEN=|' >> "$JOURNAL"
TORN_COMMIT_SHA=$(hash1 "$JOURNAL")

set_inputs RECOVER_ONLY '' '' "$JOURNAL"
run_v222 RECOVER_WITH_TORN_COMMIT_D || exit 83
"$P/bin/grep" -F 'FINAL_RECOVERED_TX C' "$LOG/RECOVER_WITH_TORN_COMMIT_D.log" >/dev/null || exit 84
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'event-C' ] || exit 85
[ "$(hash1 "$JOURNAL")" = "$TORN_COMMIT_SHA" ] || exit 86

set_inputs COMMIT_TRANSACTION D 'event-D' "$JOURNAL"
run_v222 RETRY_AFTER_TORN_COMMIT_D || exit 87
"$P/bin/grep" -F 'INPUT_PREPARED 1' "$LOG/RETRY_AFTER_TORN_COMMIT_D.log" >/dev/null || exit 88
"$P/bin/grep" -F 'PREPARE_APPEND_PERFORMED 0' "$LOG/RETRY_AFTER_TORN_COMMIT_D.log" >/dev/null || exit 89
"$P/bin/grep" -F 'COMMIT_APPEND_PERFORMED 1' "$LOG/RETRY_AFTER_TORN_COMMIT_D.log" >/dev/null || exit 90
"$P/bin/grep" -F 'FINAL_RECOVERED_TX D' "$LOG/RETRY_AFTER_TORN_COMMIT_D.log" >/dev/null || exit 91
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'event-D' ] || exit 92

"$P/bin/printf" '\nGARBAGE_PARTIAL_TAIL_WITHOUT_PROTOCOL' >> "$JOURNAL"
set_inputs RECOVER_ONLY '' '' "$JOURNAL"
run_v222 RECOVER_WITH_GARBAGE_TAIL || exit 93
"$P/bin/grep" -F 'FINAL_RECOVERED_TX D' "$LOG/RECOVER_WITH_GARBAGE_TAIL.log" >/dev/null || exit 94
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'event-D' ] || exit 95

: > "$CONFLICT"
"$P/bin/cat" >> "$CONFLICT" <<'EOF_CONFLICT'

TX=A || PHASE=PREPARE || PAYLOAD=good || TXLEN=| || PLEN=|||| || END=PREPARE
TX=A || PHASE=COMMIT || PAYLOAD=good || TXLEN=| || PLEN=|||| || END=COMMIT
TX=X || PHASE=PREPARE || PAYLOAD=one || TXLEN=| || PLEN=||| || END=PREPARE
TX=X || PHASE=PREPARE || PAYLOAD=two || TXLEN=| || PLEN=||| || END=PREPARE
TX=X || PHASE=COMMIT || PAYLOAD=one || TXLEN=| || PLEN=||| || END=COMMIT
EOF_CONFLICT

set_inputs RECOVER_ONLY '' '' "$CONFLICT"
run_v222 CONFLICTING_PREPARE_REFUSAL || exit 96
"$P/bin/grep" -F 'CONFLICTING_PREPARE_RECORD_COUNT 1' "$LOG/CONFLICTING_PREPARE_REFUSAL.log" >/dev/null || exit 97
"$P/bin/grep" -F 'FINAL_RECOVERED_TX A' "$LOG/CONFLICTING_PREPARE_REFUSAL.log" >/dev/null || exit 98
[ "$("$P/bin/cat" "$RECOVERED_MEM")" = 'good' ] || exit 99

CONFLICT_SHA=$(hash1 "$CONFLICT")
set_inputs COMMIT_TRANSACTION X 'one' "$CONFLICT"
run_v222 INPUT_TX_CONFLICT_BLOCKS_APPEND || exit 100
"$P/bin/grep" -F 'INPUT_PREPARE_CONFLICT 1' "$LOG/INPUT_TX_CONFLICT_BLOCKS_APPEND.log" >/dev/null || exit 101
"$P/bin/grep" -F 'PREPARE_APPEND_PERFORMED 0' "$LOG/INPUT_TX_CONFLICT_BLOCKS_APPEND.log" >/dev/null || exit 102
"$P/bin/grep" -F 'COMMIT_APPEND_PERFORMED 0' "$LOG/INPUT_TX_CONFLICT_BLOCKS_APPEND.log" >/dev/null || exit 103
[ "$(hash1 "$CONFLICT")" = "$CONFLICT_SHA" ] || exit 104

: > "$REPLAY"
set_inputs COMMIT_TRANSACTION A 'event-A' "$REPLAY"
run_v222 REPLAY_A || exit 105
set_inputs COMMIT_TRANSACTION B 'event-B' "$REPLAY"
run_v222 REPLAY_B || exit 106
REPLAY_SHA=$(hash1 "$REPLAY")
printf 'REPLAY_AB_JOURNAL_SHA256=%s\n' "$REPLAY_SHA"

REPLAY2="$STATE/replay2.journal"
: > "$REPLAY2"
set_inputs COMMIT_TRANSACTION A 'event-A' "$REPLAY2"
run_v222 REPLAY2_A || exit 107
set_inputs COMMIT_TRANSACTION B 'event-B' "$REPLAY2"
run_v222 REPLAY2_B || exit 108
[ "$(hash1 "$REPLAY2")" = "$REPLAY_SHA" ] || exit 109

set_inputs COMMIT_TRANSACTION BAD 'event || injected' "$REPLAY"
INVALID_SHA=$(hash1 "$REPLAY")
run_v222 INVALID_PAYLOAD_DELIMITER_REFUSAL || exit 110
"$P/bin/grep" -F 'TX_INPUT_VALID 0' "$LOG/INVALID_PAYLOAD_DELIMITER_REFUSAL.log" >/dev/null || exit 111
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/INVALID_PAYLOAD_DELIMITER_REFUSAL.log" >/dev/null || exit 112
[ "$(hash1 "$REPLAY")" = "$INVALID_SHA" ] || exit 113

: > "$OVER"
I=0
while [ "$I" -lt 66 ]; do
    "$P/bin/printf" 'garbage-%s\n' "$I" >> "$OVER"
    I=$((I + 1))
done
set_inputs RECOVER_ONLY '' '' "$OVER"
OVER_SHA=$(hash1 "$OVER")
run_v222 JOURNAL_LIMIT_REFUSAL || exit 114
"$P/bin/grep" -F 'JOURNAL_LIMIT_EXCEEDED 1' "$LOG/JOURNAL_LIMIT_REFUSAL.log" >/dev/null || exit 115
"$P/bin/grep" -F 'STATE_MUTATION_ALLOWED NO' "$LOG/JOURNAL_LIMIT_REFUSAL.log" >/dev/null || exit 116
[ "$(hash1 "$OVER")" = "$OVER_SHA" ] || exit 117

printf '\nV222R1_CRASH_CONSISTENT_TRANSACTION_JOURNAL_PREFLIGHT=PASS\n'
printf 'PREPARE_ONLY_NOT_VISIBLE_AS_COMMITTED=PASS\n'
printf 'PREPARED_TRANSACTION_RESUMES_TO_COMMIT_AFTER_RESTART=PASS\n'
printf 'TORN_PREPARE_TAIL_IGNORED=PASS\n'
printf 'TORN_PREPARE_RETRY_RECOVERS=PASS\n'
printf 'TORN_COMMIT_TAIL_IGNORED=PASS\n'
printf 'TORN_COMMIT_RETRY_RECOVERS=PASS\n'
printf 'GARBAGE_TAIL_IGNORED=PASS\n'
printf 'CONFLICTING_PREPARE_BLOCKS_TRANSACTION=PASS\n'
printf 'IDEMPOTENT_COMMIT_FRESH_VM=PASS\n'
printf 'DETERMINISTIC_JOURNAL_REPLAY=PASS\n'
printf 'INVALID_PAYLOAD_DELIMITER_REFUSAL=PASS\n'
printf 'STEP_LIMIT_STATUS=BOUNDED\n'
printf 'HOST_TRANSACTION_DECISION=NO\n'
printf 'HOST_RECOVERY_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'CRASH_CONSISTENT_JOURNAL_RECOVERY=PROVEN_UNDER_INJECTED_TRUNCATED_TAIL_FAULTS\n'
printf 'MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED\n'
printf 'PRODUCTION_PROMOTION_ALLOWED=NO\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'NEXT_ACTION=CHECKPOINT_V222R1_THEN_WRAP_SHADOW_SCHEDULED_INTENT_IN_TRANSACTION_JOURNAL\n'
