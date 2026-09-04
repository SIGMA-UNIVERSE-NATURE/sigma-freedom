#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
WORK="$HOME_SIGMA/sigma-freedom-write"
BRAIN="$WORK/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC="$E/SIGMA_STRUCTURAL_GROUPING_V2_7P.sigma"
BC="$E/SIGMA_STRUCTURAL_GROUPING_V2_7P.sigmab"
EXPECTED_SOURCE=ab6eb3bf5e8796f2ec4b772159d70c648458fd85895f59f521407ab4209d6419

STATE="$HOME_SIGMA/SIGMA_V27_STRUCTURAL_GROUPING_PREFLIGHT"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"

INPUT="$E/SIGMA_V27T_STRUCTURAL_PROFILES.memory"
OUTPUT="$E/SIGMA_V27T_GROUP_ASSIGNMENTS.memory"

mkdir -p "$STATE" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V27_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=V27_STRUCTURAL_GROUPING_PREFLIGHT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_GROUP_SELECTION=NO\n'
printf 'HOST_TOPIC_CLASSIFICATION=NO\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'NEGATIVE_TEST=YES\n'
printf 'REPLAY_TEST=YES\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || {
    printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'
    exit 21
}
[ "$actual_vm" = "$EXPECTED_VM" ] || {
    printf 'HOLD=VM_IDENTITY_MISMATCH\n'
    exit 22
}
[ "$actual_source" = "$EXPECTED_SOURCE" ] || {
    printf 'HOLD=V27_SOURCE_IDENTITY_MISMATCH\n'
    exit 23
}

"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 24
[ -s "$BC.partial" ] || exit 25
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 26
"$P/bin/chmod" 0400 "$BC" || exit 27

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

run_case() {
    CASE_NAME="$1"
    EXPECT_GROUPS="$2"
    EXPECT_GROUPED="$3"
    EXPECT_SINGLETON="$4"
    EXPECT_DUPLICATES="$5"

    RUNLOG="$LOG/$CASE_NAME.log"

    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?

    printf '\n=== %s ===\n' "$CASE_NAME"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"

    [ "$RC" -eq 0 ] || return 50
    "$P/bin/grep" -F "MULTI_MEMBER_GROUP_COUNT $EXPECT_GROUPS" "$RUNLOG" >/dev/null || return 51
    "$P/bin/grep" -F "GROUPED_DOCUMENT_COUNT $EXPECT_GROUPED" "$RUNLOG" >/dev/null || return 52
    "$P/bin/grep" -F "SINGLETON_DOCUMENT_COUNT $EXPECT_SINGLETON" "$RUNLOG" >/dev/null || return 53
    "$P/bin/grep" -F "DUPLICATE_PROFILE_COUNT $EXPECT_DUPLICATES" "$RUNLOG" >/dev/null || return 54
    "$P/bin/grep" -F 'HOST_GROUP_SELECTION NO' "$RUNLOG" >/dev/null || return 55
    "$P/bin/grep" -F 'HOST_TOPIC_CLASSIFICATION NO' "$RUNLOG" >/dev/null || return 56
    "$P/bin/grep" -F 'STRUCTURAL_GROUPING_ONLY YES' "$RUNLOG" >/dev/null || return 57

    return 0
}

"$P/bin/cat" > "$INPUT" <<'EOF_POSITIVE'
DOC=A || ANCHOR=in => the
DOC=B || ANCHOR=Phi => Sigma
DOC=A || ANCHOR=in => the
DOC=C || ANCHOR=in => the
DOC=D || ANCHOR=Six => Sigma
DOC=E || ANCHOR=Phi => Sigma
EOF_POSITIVE

: > "$OUTPUT"
run_case POSITIVE_SHARED_ANCHORS 2 4 1 1
CASE_RC=$?
if [ "$CASE_RC" -ne 0 ]; then
    printf 'V27_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=POSITIVE_SHARED_ANCHORS\n'
    printf 'FAILURE_RC=%s\n' "$CASE_RC"
    exit "$CASE_RC"
fi

POSITIVE_SHA=$("$P/bin/sha256sum" "$OUTPUT" | "$P/bin/awk" '{print $1}')
"$P/bin/cp" -- "$OUTPUT" "$STATE/positive_assignments.reference"
printf 'POSITIVE_ASSIGNMENT_SHA256=%s\n' "$POSITIVE_SHA"

printf '\n=== POSITIVE_ASSIGNMENTS ===\n'
"$P/bin/cat" "$OUTPUT"
printf '\n'

"$P/bin/cat" > "$INPUT" <<'EOF_NEGATIVE'
DOC=A || ANCHOR=in => the
DOC=A || ANCHOR=in => the
DOC=B || ANCHOR=Phi => Sigma
DOC=C || ANCHOR=the => Moon
DOC=D || ANCHOR=Six => Sigma
DOC=E || ANCHOR=such => as
EOF_NEGATIVE

: > "$OUTPUT"
run_case NEGATIVE_NO_SHARED_ANCHORS 0 0 5 1
CASE_RC=$?
if [ "$CASE_RC" -ne 0 ]; then
    printf 'V27_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=NEGATIVE_NO_SHARED_ANCHORS\n'
    printf 'FAILURE_RC=%s\n' "$CASE_RC"
    exit "$CASE_RC"
fi

NEGATIVE_SHA=$("$P/bin/sha256sum" "$OUTPUT" | "$P/bin/awk" '{print $1}')
printf 'NEGATIVE_ASSIGNMENT_SHA256=%s\n' "$NEGATIVE_SHA"

printf '\n=== NEGATIVE_ASSIGNMENTS ===\n'
"$P/bin/cat" "$OUTPUT"
printf '\n'

[ "$POSITIVE_SHA" != "$NEGATIVE_SHA" ] || {
    printf 'V27_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE=DYNAMIC_INPUT_DID_NOT_CHANGE_ASSIGNMENTS\n'
    exit 60
}

"$P/bin/cat" > "$INPUT" <<'EOF_POSITIVE_REPLAY'
DOC=A || ANCHOR=in => the
DOC=B || ANCHOR=Phi => Sigma
DOC=A || ANCHOR=in => the
DOC=C || ANCHOR=in => the
DOC=D || ANCHOR=Six => Sigma
DOC=E || ANCHOR=Phi => Sigma
EOF_POSITIVE_REPLAY

: > "$OUTPUT"
run_case POSITIVE_REPLAY 2 4 1 1
CASE_RC=$?
if [ "$CASE_RC" -ne 0 ]; then
    printf 'V27_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=POSITIVE_REPLAY\n'
    printf 'FAILURE_RC=%s\n' "$CASE_RC"
    exit "$CASE_RC"
fi

REPLAY_SHA=$("$P/bin/sha256sum" "$OUTPUT" | "$P/bin/awk" '{print $1}')
printf 'REPLAY_ASSIGNMENT_SHA256=%s\n' "$REPLAY_SHA"

[ "$REPLAY_SHA" = "$POSITIVE_SHA" ] || {
    printf 'V27_STRUCTURAL_GROUPING_PREFLIGHT=FAIL\n'
    printf 'FAILURE=REPLAY_ASSIGNMENT_MISMATCH\n'
    exit 61
}

printf '\nV27_STRUCTURAL_GROUPING_PREFLIGHT=PASS\n'
printf 'NATIVE_STRUCTURAL_GROUPING=PROVEN_IN_QA_SCOPE\n'
printf 'DISTINCT_DOC_ANCHOR_DEDUP=PROVEN_IN_QA_SCOPE\n'
printf 'DYNAMIC_INPUT_DEPENDENCE=PASS\n'
printf 'NEGATIVE_COUNTEREXAMPLE=PASS\n'
printf 'DETERMINISTIC_REPLAY=PASS\n'
printf 'PERSISTED_GROUP_ASSIGNMENTS=PASS\n'
printf 'HOST_GROUP_SELECTION=NO\n'
printf 'HOST_TOPIC_CLASSIFICATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'SEMANTIC_GROUPING=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'PRODUCTION_LEARNER_MEMORY_MUTATED=NO\n'
printf 'NEXT_ACTION=BUILD_V28_CURRICULUM_PRIORITY_PREFLIGHT\n'