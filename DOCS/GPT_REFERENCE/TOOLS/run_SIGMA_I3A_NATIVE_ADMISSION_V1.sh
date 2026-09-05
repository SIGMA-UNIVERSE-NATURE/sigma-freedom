#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HERE="$(cd "$(dirname "$0")" && pwd)"
GENESIS="$HOME/SIGMA/sigma_genesis1"
ROOT="$GENESIS/.sigma_exec/HH_AUTO_INTERNET_LESSONS"

SIGMAC="$GENESIS/native/sigmac"
VM="$GENESIS/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_SOURCE="be998fd907d93337cc3befe8582503a80256c1fea658fa8691d00fa8c5a67574"

SOURCE_ASSESSMENT="$ROOT/assessments/20260903T104621Z_6069_19041"
FRESH_COLLECTION="$ROOT/runs/20260903T122823Z_19134_21003"

SRC_REPO="$HERE/SIGMA_I3A_NATIVE_POST_FOLLOWUP_OUTCOME_GATE_V1.sigma"

STATE="$HERE/runtime"
BRAIN="$STATE/shadow/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
BASE="$E/SIGMA_I3A_POST_FOLLOWUP_OUTCOME_GATE"
IN="$BASE/input"
ST="$BASE/state"
LOG="$STATE/log"

SRC="$E/SIGMA_I3A_NATIVE_POST_FOLLOWUP_OUTCOME_GATE_V1.sigma"
BC="$E/SIGMA_I3A_NATIVE_POST_FOLLOWUP_OUTCOME_GATE_V1.sigmab"
MEM="$ST/i3a.memory"
EVENT="$ST/i3a_event.txt"

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }

mkdir_clean() {
    rm -rf "$STATE"
    mkdir -p "$E" "$IN" "$ST" "$LOG"
    : > "$MEM"
    : > "$EVENT"
}

safe_control_filename() {
    rel="$1"
    case "$rel" in
        *lesson*|*LESSON*|*experience*|*EXPERIENCE*|*topic*|*TOPIC*|*query*|*QUERY*|*reader*|*READER*|*search*|*SEARCH*|*keep*|*KEEP*|*source*|*SOURCE*|*payload*|*PAYLOAD*|*content*|*CONTENT*|*text*|*TEXT*|*raw*|*RAW*|*knowledge*|*KNOWLEDGE*|*candidate*|*CANDIDATE*|*extract*|*EXTRACT*|*paragraph*|*PARAGRAPH*|*document*|*DOCUMENT*|*html*|*HTML*|*xml*|*XML*|*json*|*JSON*|*body*|*BODY*|*title*|*TITLE*|*summary*|*SUMMARY*|*answer*|*ANSWER*)
            return 1 ;;
    esac
    return 0
}

build_prior_control_union() {
    : > "$IN/prior.control.union"

    [ -d "$SOURCE_ASSESSMENT" ] || return 1

    "$P/bin/find" "$SOURCE_ASSESSMENT" -maxdepth 1 -type f -print \
      | "$P/bin/sort" \
      | while IFS= read -r f; do
            rel="${f##*/}"
            sz=$("$P/bin/stat" -c '%s' "$f")
            if [ "$sz" -le 4096 ] && safe_control_filename "$rel"; then
                "$P/bin/cat" "$f" >> "$IN/prior.control.union"
                printf '\n' >> "$IN/prior.control.union"
            fi
        done

    "$P/bin/grep" -F 'ASSESSMENT_STATE=' "$IN/prior.control.union" >/dev/null
}

copy_canonical_fresh_controls() {
    [ -f "$FRESH_COLLECTION/collection.provenance.state" ] || return 1
    [ -f "$FRESH_COLLECTION/verification.state" ] || return 1

    cp -- "$FRESH_COLLECTION/collection.provenance.state" "$IN/fresh.provenance.state"
    cp -- "$FRESH_COLLECTION/verification.state" "$IN/fresh.verification.state"
}

write_fixture() {
    prior_state="$1"
    run_id="$2"
    indep="$3"
    control="$4"
    source_plane="$5"
    collection_plane="$6"
    search_bound="$7"
    source_bound="$8"
    probe_bound="$9"
    shift 9
    reader_bound="$1"
    keep_bound="$2"
    keep_events="$3"
    unique_lessons="$4"
    duplicates="$5"
    budget_overrun="$6"
    collection_pass="$7"

    cat > "$IN/prior.control.union" <<EOF
ASSESSMENT_STATE=$prior_state
EOF

    cat > "$IN/fresh.provenance.state" <<EOF
RUN_ID=$run_id
CONTROL_PLANE=$control
SOURCE_SELECTION_PLANE=$source_plane
COLLECTION_DECISION_PLANE=$collection_plane
HOST_ROLE=MECHANICAL_ACTUATOR_ONLY
TOPIC_RELEVANCE=NOT_ASSESSED
SOURCE_TRUST=NOT_ASSESSED
LESSON_TRUTH=NOT_ASSESSED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
EOF

    cat > "$IN/fresh.verification.state" <<EOF
INDEPENDENT_VERIFY_RC=$indep
CONTROL_PLANE=$control
SOURCE_SELECTION_PLANE=$source_plane
COLLECTION_DECISION_PLANE=$collection_plane
ALL_SEARCH_REQUESTS_BOUND_TO_SIGMA_ACTION=$search_bound
ALL_SOURCE_SELECTIONS_BOUND_TO_SIGMA_ACTION=$source_bound
ALL_SOURCE_PROBES_BOUND_TO_SIGMA_SELECTION_AND_FETCH=$probe_bound
ALL_READER_RUNS_BOUND_TO_SIGMA_ACTION=$reader_bound
ALL_KEEP_EVENTS_BOUND_TO_SIGMA_ACTION=$keep_bound
KEEP_EVENTS=$keep_events
UNIQUE_LESSONS=$unique_lessons
EXACT_DUPLICATE_KEEP_EVENTS=$duplicates
RESOURCE_BUDGET_OVERRUN=$budget_overrun
SIGMA_NATIVE_MULTI_SOURCE_COLLECTION=$collection_pass
EOF
}

TOTAL_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0

run_expect() {
    name="$1"
    expect_action="$2"
    expect_status="$3"
    expect_mutated="$4"
    out="$LOG/$name.log"

    (cd "$BRAIN" && "$VM" "$BC") > "$out" 2>&1
    rc=$?
    TOTAL_VM_INVOCATIONS=$((TOTAL_VM_INVOCATIONS + 1))

    printf '\n=== %s ===\n' "$name"
    printf 'VM_RC=%s\n' "$rc"
    "$P/bin/grep" -E '^(PRIOR_STATE|RUN_ID|FRESH_INTEGRITY_OK|KEEP_EVENTS|UNIQUE_LESSONS|NEXT_RESEARCH_ACTION|I3A_STATUS|STATE_MUTATED|EVENT_EMITTED) ' "$out" || true

    if [ "$rc" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'POST_VM_ALIGNMENT=FAIL\n'
        return 1
    fi

    "$P/bin/grep" -F "NEXT_RESEARCH_ACTION $expect_action" "$out" >/dev/null || {
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'POST_VM_ALIGNMENT=FAIL\n'
        return 1
    }

    "$P/bin/grep" -F "I3A_STATUS $expect_status" "$out" >/dev/null || {
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'POST_VM_ALIGNMENT=FAIL\n'
        return 1
    }

    "$P/bin/grep" -F "STATE_MUTATED $expect_mutated" "$out" >/dev/null || {
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'POST_VM_ALIGNMENT=FAIL\n'
        return 1
    }

    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
    printf 'POST_VM_ALIGNMENT=PASS\n'
    return 0
}

printf '=== SIGMA I3A NATIVE ADMISSION V1 ===\n'
printf 'CAPABILITY=POST_FOLLOWUP_OUTCOME_GATE\n'
printf 'ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY\n'
printf 'HOST_NEXT_ACTION_SELECTION=NO\n'
printf 'HOST_SEMANTIC_OUTCOME_CLASSIFICATION=NO\n'
printf 'HOST_UNDERSTANDING_CLASSIFICATION=NO\n'
printf 'HOST_QUERY_GENERATION=NO\n'
printf 'UNDERSTANDING_STATE_EMITTED_BY_I3A=NO\n'
printf 'ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL\n'
printf 'I2R1_RERUN=NO\n'

mkdir_clean

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
SOURCE_SHA=$(hash1 "$SRC_REPO")

printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'SOURCE_SHA256=%s\n' "$SOURCE_SHA"

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 20; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 21; }
[ "$SOURCE_SHA" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=SOURCE_IDENTITY_MISMATCH\n'; exit 22; }

cp -- "$SRC_REPO" "$SRC"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'I3A_COMPILE_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] && [ -s "$BC.partial" ] || { printf 'HOLD=I3A_COMPILE_FAILED\n'; exit 23; }
mv -f "$BC.partial" "$BC"
chmod 0400 "$BC"

BC_SHA=$(hash1 "$BC")
printf 'I3A_BYTECODE_SHA256=%s\n' "$BC_SHA"

CANON_RUN_TOKEN="20260903T122823Z_19134_21003"
CANON_TOPIC_SHA="62b60371f21cb7be2cf6ab7fcb6b629235abe58fa97ff5738ea7548159f203f5"
"$P/bin/grep" -F "$CANON_RUN_TOKEN" "$SRC_REPO" >/dev/null 2>&1 && { printf 'HOLD=CANONICAL_RUN_TOKEN_LEAK_IN_SOURCE\n'; exit 24; }
"$P/bin/grep" -a -F "$CANON_RUN_TOKEN" "$BC" >/dev/null 2>&1 && { printf 'HOLD=CANONICAL_RUN_TOKEN_LEAK_IN_BYTECODE\n'; exit 25; }
"$P/bin/grep" -F "$CANON_TOPIC_SHA" "$SRC_REPO" >/dev/null 2>&1 && { printf 'HOLD=CANONICAL_TOPIC_HASH_LEAK_IN_SOURCE\n'; exit 26; }
"$P/bin/grep" -a -F "$CANON_TOPIC_SHA" "$BC" >/dev/null 2>&1 && { printf 'HOLD=CANONICAL_TOPIC_HASH_LEAK_IN_BYTECODE\n'; exit 27; }
printf 'CANONICAL_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0\n'

build_prior_control_union || { printf 'HOLD=PRIOR_CONTROL_UNION_MISSING_ASSESSMENT_STATE\n'; exit 30; }
copy_canonical_fresh_controls || { printf 'HOLD=CANONICAL_FRESH_CONTROLS_MISSING\n'; exit 31; }

run_expect D01_CANONICAL_FRESH_OUTCOME ASSESS_FRESH_EVIDENCE DECISION_COMMITTED 1 || exit 40
run_expect D02_CANONICAL_IDEMPOTENT ASSESS_FRESH_EVIDENCE ALREADY_DECIDED_SAME_OUTCOME 0 || exit 41

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-valid-1 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES 5 5 0 0 PASS_TESTED_SCOPE
run_expect D03_DYNAMIC_VALID ASSESS_FRESH_EVIDENCE DECISION_COMMITTED 1 || exit 42

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-empty-1 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES 0 0 0 0 PASS_TESTED_SCOPE
run_expect D04_NO_NEW_EVIDENCE REPLAN_RESEARCH DECISION_COMMITTED 1 || exit 43

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-vfail-1 1 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES 5 5 0 0 PASS_TESTED_SCOPE
run_expect D05_VERIFY_FAIL HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 44

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-host-source 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM HOST SIGMA_NATIVE_VM YES YES YES YES YES 5 5 0 0 PASS_TESTED_SCOPE
run_expect D06_HOST_SOURCE_PLANE HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 45

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-host-collection 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM HOST YES YES YES YES YES 5 5 0 0 PASS_TESTED_SCOPE
run_expect D07_HOST_COLLECTION_PLANE HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 46

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-unbound-search 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM NO YES YES YES YES 5 5 0 0 PASS_TESTED_SCOPE
run_expect D08_SEARCH_UNBOUND HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 47

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-unbound-keep 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES NO 5 5 0 0 PASS_TESTED_SCOPE
run_expect D09_KEEP_UNBOUND HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 48

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-budget 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES 5 5 0 1 PASS_TESTED_SCOPE
run_expect D10_BUDGET_OVERRUN HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 49

: > "$MEM"; : > "$EVENT"
write_fixture SOMETHING_ELSE dyn-prior-state 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES 5 5 0 0 PASS_TESTED_SCOPE
run_expect D11_PRIOR_STATE_MISMATCH HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 50

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE dyn-metric-inconsistent 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES 2 3 0 0 PASS_TESTED_SCOPE
run_expect D12_METRIC_INCONSISTENT HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 51

DIRECTED_VM_INVOCATIONS=12

I=1
while [ "$I" -le 10 ]; do
    : > "$MEM"; : > "$EVENT"
    RID="dyn-matrix-${I}-7f29c${I}"

    MOD=$((I % 4))
    if [ "$MOD" -eq 0 ]; then
        write_fixture MORE_EVIDENCE "$RID" 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES "$I" "$I" 0 0 PASS_TESTED_SCOPE
        run_expect "M$(printf '%02d' "$I")_ASSESS" ASSESS_FRESH_EVIDENCE DECISION_COMMITTED 1 || exit 60
    elif [ "$MOD" -eq 1 ]; then
        write_fixture MORE_EVIDENCE "$RID" 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES 0 0 0 0 PASS_TESTED_SCOPE
        run_expect "M$(printf '%02d' "$I")_REPLAN" REPLAN_RESEARCH DECISION_COMMITTED 1 || exit 61
    elif [ "$MOD" -eq 2 ]; then
        write_fixture MORE_EVIDENCE "$RID" 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES NO YES "$I" "$I" 0 0 PASS_TESTED_SCOPE
        run_expect "M$(printf '%02d' "$I")_HOLD_READER" HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 62
    else
        write_fixture MORE_EVIDENCE "$RID" 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES "$I" "$I" 0 2 PASS_TESTED_SCOPE
        run_expect "M$(printf '%02d' "$I")_HOLD_BUDGET" HOLD_UNKNOWN HOLD_UNKNOWN 0 || exit 63
    fi

    I=$((I + 1))
done

DYNAMIC_MATRIX_VM_INVOCATIONS=10

: > "$MEM"; : > "$EVENT"
write_fixture MORE_EVIDENCE replay-i3a-88fa 0 ONE_CONTINUOUS_SIGMA_NATIVE_VM SIGMA_NATIVE_VM SIGMA_NATIVE_VM YES YES YES YES YES 7 7 0 0 PASS_TESTED_SCOPE
cp "$MEM" "$STATE/replay_pre.memory"
cp "$IN/prior.control.union" "$STATE/replay_prior"
cp "$IN/fresh.provenance.state" "$STATE/replay_prov"
cp "$IN/fresh.verification.state" "$STATE/replay_verify"

run_expect R01_IDENTICAL ASSESS_FRESH_EVIDENCE DECISION_COMMITTED 1 || exit 70
cp "$LOG/R01_IDENTICAL.log" "$STATE/replay1.log"
cp "$EVENT" "$STATE/replay1.event"
cp "$MEM" "$STATE/replay1.memory"

cp "$STATE/replay_pre.memory" "$MEM"
: > "$EVENT"
cp "$STATE/replay_prior" "$IN/prior.control.union"
cp "$STATE/replay_prov" "$IN/fresh.provenance.state"
cp "$STATE/replay_verify" "$IN/fresh.verification.state"

run_expect R02_IDENTICAL ASSESS_FRESH_EVIDENCE DECISION_COMMITTED 1 || exit 71
cp "$LOG/R02_IDENTICAL.log" "$STATE/replay2.log"
cp "$EVENT" "$STATE/replay2.event"
cp "$MEM" "$STATE/replay2.memory"

"$P/bin/cmp" -s "$STATE/replay1.log" "$STATE/replay2.log" || { printf 'HOLD=REPLAY_VM_OUTPUT_MISMATCH\n'; exit 72; }
"$P/bin/cmp" -s "$STATE/replay1.event" "$STATE/replay2.event" || { printf 'HOLD=REPLAY_EVENT_MISMATCH\n'; exit 73; }
"$P/bin/cmp" -s "$STATE/replay1.memory" "$STATE/replay2.memory" || { printf 'HOLD=REPLAY_MEMORY_MISMATCH\n'; exit 74; }

REPLAY_VM_INVOCATIONS=2

if "$P/bin/grep" -E -i 'step[ _-]*limit' "$LOG"/*.log >/dev/null 2>&1; then
    printf 'HOLD=STEP_LIMIT_OBSERVED\n'
    exit 75
fi

[ "$(hash1 "$SRC_REPO")" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=SOURCE_MUTATED\n'; exit 76; }
[ "$(hash1 "$BC")" = "$BC_SHA" ] || { printf 'HOLD=BYTECODE_MUTATED\n'; exit 77; }

printf '\n=== I3A ADMISSION SUMMARY ===\n'
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'DIRECTED_VM_INVOCATIONS=%s\n' "$DIRECTED_VM_INVOCATIONS"
printf 'DYNAMIC_MATRIX_VM_INVOCATIONS=%s\n' "$DYNAMIC_MATRIX_VM_INVOCATIONS"
printf 'REPLAY_VM_INVOCATIONS=%s\n' "$REPLAY_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=0\n'
printf 'CANONICAL_FRESH_COLLECTION_INTERFACE=TESTED\n'
printf 'PRIOR_MORE_EVIDENCE_STATE_CONSUMED_NATIVELY=TESTED\n'
printf 'FRESH_VERIFICATION_BINDINGS_CONSUMED_NATIVELY=TESTED\n'
printf 'ASSESS_FRESH_EVIDENCE_ACTION=NATIVE_SIGMA_TESTED\n'
printf 'REPLAN_RESEARCH_ACTION=NATIVE_SIGMA_TESTED_NO_NEW_EVIDENCE_SCOPE\n'
printf 'HOLD_UNKNOWN_FAIL_CLOSED=NATIVE_SIGMA_TESTED\n'
printf 'PERSISTENT_DECISION_LEDGER=TESTED\n'
printf 'IDEMPOTENCY=TESTED\n'
printf 'RUN_ID_CONFLICT_REFUSAL=SOURCE_IMPLEMENTED_NOT_SEPARATELY_EXERCISED_IN_V1\n'
printf 'REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES\n'
printf 'REPLAY_IDENTICAL_EVENT_BYTES=YES\n'
printf 'REPLAY_IDENTICAL_MEMORY_BYTES=YES\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'HOST_NEXT_ACTION_SELECTION=NO\n'
printf 'HOST_SEMANTIC_OUTCOME_CLASSIFICATION=NO\n'
printf 'HOST_UNDERSTANDING_CLASSIFICATION=NO\n'
printf 'HOST_QUERY_GENERATION=NO\n'
printf 'UNDERSTANDING_STATE_EMITTED_BY_I3A=NO\n'
printf 'TRUTH_DECISION=NOT_EXECUTED\n'
printf 'KNOWLEDGE_PROMOTION=NOT_EXECUTED\n'
printf 'STATIC_I3A_POLICY_LEARNED=NOT_PROVEN\n'
printf 'GENERAL_RESEARCH_POLICY_LEARNED=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'

[ "$TOTAL_VM_INVOCATIONS" -eq 24 ] || { printf 'HOLD=VM_INVOCATION_COUNT_MISMATCH\n'; exit 80; }
[ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 24 ] || { printf 'HOLD=PASS_COUNT_MISMATCH\n'; exit 81; }
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || { printf 'HOLD=ALIGNMENT_FAILURE\n'; exit 82; }
[ "$VM_NONZERO_COUNT" -eq 0 ] || { printf 'HOLD=VM_NONZERO\n'; exit 83; }

printf 'I3A_NATIVE_ADMISSION_V1=PASS\n'
printf 'POST_FOLLOWUP_OUTCOME_GATE_TESTED_SCOPE=PASS\n'
printf 'RESULT=PASS_IN_EXACT_TESTED_SCOPE\n'
printf 'I3B_FRESH_EVIDENCE_ASSESSMENT_DISPATCH_UNLOCKED_BY_THIS_GATE=YES\n'
printf 'CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN\n'
