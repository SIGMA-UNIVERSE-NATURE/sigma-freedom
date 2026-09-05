#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
PROD_BRAIN="$REPO/BRAIN/EXTRA BRAIN_OPPO_24826"
PROD_E="$PROD_BRAIN/.sigma_exec"
PROD_STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
EXPECTED_V24_SOURCE=6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2

SRC_REPO="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_PRODUCTION_STATE_MIGRATION_ROLLBACK_VERIFIER_V2_24R1.sigma"
EXPECTED_SOURCE=17cfd479bd0ede1e7cd8aa8d73dc58a7a94bcc74e6279bb4d6724375c2ed8057

STATE="$HOME_SIGMA/SIGMA_V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK"
VERIFIER_BRAIN="$STATE/verifier/BRAIN/EXTRA BRAIN_OPPO_24826"
VE="$VERIFIER_BRAIN/.sigma_exec"
SRC="$VE/SIGMA_PRODUCTION_STATE_MIGRATION_ROLLBACK_VERIFIER_V2_24R1.sigma"
BC="$VE/SIGMA_PRODUCTION_STATE_MIGRATION_ROLLBACK_VERIFIER_V2_24R1.sigmab"
LOG="$STATE/log"
CAP="$STATE/captures"
CANDIDATE="$STATE/candidate_package"
BASELINE_TAR="$STATE/immutable_migration_baseline.tar"
LOCK="$STATE/preflight.lock"

MODE_MEM="$VE/SIGMA_V224R1_MODE.memory"
BEFORE_D="$VE/SIGMA_V224R1_SOURCE_BEFORE_DIGEST.memory"
BEFORE_C="$VE/SIGMA_V224R1_SOURCE_BEFORE_COUNT.memory"
SNAP_D="$VE/SIGMA_V224R1_SNAPSHOT_DIGEST.memory"
SNAP_C="$VE/SIGMA_V224R1_SNAPSHOT_COUNT.memory"
AFTER_D="$VE/SIGMA_V224R1_SOURCE_AFTER_DIGEST.memory"
AFTER_C="$VE/SIGMA_V224R1_SOURCE_AFTER_COUNT.memory"
CAND_D="$VE/SIGMA_V224R1_CANDIDATE_DIGEST.memory"
CAND_C="$VE/SIGMA_V224R1_CANDIDATE_COUNT.memory"
BASE_D="$VE/SIGMA_V224R1_BASELINE_DIGEST.memory"
BASE_C="$VE/SIGMA_V224R1_BASELINE_COUNT.memory"
MUT_D="$VE/SIGMA_V224R1_MUTATED_DIGEST.memory"
MUT_C="$VE/SIGMA_V224R1_MUTATED_COUNT.memory"
REST_D="$VE/SIGMA_V224R1_RESTORED_DIGEST.memory"
REST_C="$VE/SIGMA_V224R1_RESTORED_COUNT.memory"
DECISION_MEM="$VE/SIGMA_V224R1_DECISION.memory"

mkdir -p "$VE" "$LOG" "$CAP"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=V224R1_MIGRATION_ROLLBACK_ALREADY_RUNNING\n'
    exit 20
}

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }
entry_count() { "$P/bin/tar" -tf "$1" | "$P/bin/wc" -l | "$P/bin/tr" -d ' '; }

canonical_prod_capture() {
    OUT="$1"
    "$P/bin/rm" -f -- "$OUT"
    "$P/bin/tar" \
        --sort=name \
        --mtime='@0' \
        --owner=0 \
        --group=0 \
        --numeric-owner \
        --format=posix \
        --pax-option=delete=atime,delete=ctime \
        --exclude='SIGMA_CONTINUOUS_NATIVE_V2_2/log' \
        --exclude='SIGMA_CONTINUOUS_NATIVE_V2_2/log/*' \
        -cf "$OUT" \
        -C "$PROD_BRAIN" .sigma_exec \
        -C "$HOME_SIGMA" SIGMA_CONTINUOUS_NATIVE_V2_2
}

canonical_candidate_capture() {
    OUT="$1"
    "$P/bin/rm" -f -- "$OUT"
    "$P/bin/tar" \
        --sort=name \
        --mtime='@0' \
        --owner=0 \
        --group=0 \
        --numeric-owner \
        --format=posix \
        --pax-option=delete=atime,delete=ctime \
        -cf "$OUT" \
        -C "$CANDIDATE" .sigma_exec SIGMA_CONTINUOUS_NATIVE_V2_2
}

write_all_inputs() {
    MODE="$1"
    "$P/bin/printf" '%s' "$MODE" > "$MODE_MEM"
    "$P/bin/printf" '%s' "${SOURCE_BEFORE_DIGEST:-}" > "$BEFORE_D"
    "$P/bin/printf" '%s' "${SOURCE_BEFORE_COUNT:-}" > "$BEFORE_C"
    "$P/bin/printf" '%s' "${SNAPSHOT_DIGEST:-}" > "$SNAP_D"
    "$P/bin/printf" '%s' "${SNAPSHOT_COUNT:-}" > "$SNAP_C"
    "$P/bin/printf" '%s' "${SOURCE_AFTER_DIGEST:-}" > "$AFTER_D"
    "$P/bin/printf" '%s' "${SOURCE_AFTER_COUNT:-}" > "$AFTER_C"
    "$P/bin/printf" '%s' "${CANDIDATE_DIGEST:-}" > "$CAND_D"
    "$P/bin/printf" '%s' "${CANDIDATE_COUNT:-}" > "$CAND_C"
    "$P/bin/printf" '%s' "${BASELINE_DIGEST:-}" > "$BASE_D"
    "$P/bin/printf" '%s' "${BASELINE_COUNT:-}" > "$BASE_C"
    "$P/bin/printf" '%s' "${MUTATED_DIGEST:-}" > "$MUT_D"
    "$P/bin/printf" '%s' "${MUTATED_COUNT:-}" > "$MUT_C"
    "$P/bin/printf" '%s' "${RESTORED_DIGEST:-}" > "$REST_D"
    "$P/bin/printf" '%s' "${RESTORED_COUNT:-}" > "$REST_C"
}

run_verifier() {
    CASE_NAME="$1"
    RUNLOG="$LOG/$CASE_NAME.log"
    (
        cd "$VERIFIER_BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?
    printf '\n=== %s ===\n' "$CASE_NAME"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$RUNLOG"
    return "$RC"
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
V24_SOURCE_SHA=$(hash1 "$PROD_E/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma")
SOURCE_SHA=$(hash1 "$SRC_REPO")

printf 'SIGMA_PHASE=V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'PRODUCTION_V24_SOURCE_SHA256=%s\n' "$V24_SOURCE_SHA"
printf 'SOURCE_SHA256=%s\n' "$SOURCE_SHA"
printf 'MIGRATION_SCOPE=PRODUCTION_BRAIN_DOT_SIGMA_EXEC_PLUS_V24_STATE_EXCLUDING_OPERATIONAL_LOG_DIRECTORY\n'
printf 'PRODUCTION_STOP_REQUIRED=NO\n'
printf 'PRODUCTION_WRITE_TARGET_FROM_ADMISSION=NO\n'
printf 'HOST_MIGRATION_DECISION=NO\n'
printf 'HOST_ROLLBACK_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || exit 21
[ "$VM_SHA" = "$EXPECTED_VM" ] || exit 22
[ "$V24_SOURCE_SHA" = "$EXPECTED_V24_SOURCE" ] || exit 23
[ "$SOURCE_SHA" = "$EXPECTED_SOURCE" ] || exit 24
[ -d "$PROD_E" ] || exit 25
[ -d "$PROD_STATE" ] || exit 26

V24_PID=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_BEFORE=%s\n' "$V24_PID"
[ -n "$V24_PID" ] || exit 27

"$P/bin/cp" -- "$SRC_REPO" "$SRC"
"$P/bin/rm" -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'V224_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || exit 28
[ -s "$BC.partial" ] || exit 29
"$P/bin/mv" -f -- "$BC.partial" "$BC"
"$P/bin/chmod" 0400 "$BC"
printf 'V224_BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

STABLE=0
ATTEMPT=1
while [ "$ATTEMPT" -le 8 ]; do
    BEFORE_TAR="$CAP/attempt_${ATTEMPT}_before.tar"
    SNAP_TAR="$CAP/attempt_${ATTEMPT}_snapshot.tar"
    AFTER_TAR="$CAP/attempt_${ATTEMPT}_after.tar"

    canonical_prod_capture "$BEFORE_TAR" || exit 30
    canonical_prod_capture "$SNAP_TAR" || exit 31
    canonical_prod_capture "$AFTER_TAR" || exit 32

    SOURCE_BEFORE_DIGEST=$(hash1 "$BEFORE_TAR")
    SOURCE_BEFORE_COUNT=$(entry_count "$BEFORE_TAR")
    SNAPSHOT_DIGEST=$(hash1 "$SNAP_TAR")
    SNAPSHOT_COUNT=$(entry_count "$SNAP_TAR")
    SOURCE_AFTER_DIGEST=$(hash1 "$AFTER_TAR")
    SOURCE_AFTER_COUNT=$(entry_count "$AFTER_TAR")

    CANDIDATE_DIGEST=""
    CANDIDATE_COUNT=""
    BASELINE_DIGEST=""
    BASELINE_COUNT=""
    MUTATED_DIGEST=""
    MUTATED_COUNT=""
    RESTORED_DIGEST=""
    RESTORED_COUNT=""

    write_all_inputs VERIFY_SOURCE_STABILITY
    run_verifier "SOURCE_STABILITY_ATTEMPT_${ATTEMPT}" || exit 33

    NATIVE_DECISION=$("$P/bin/cat" "$DECISION_MEM")
    printf 'SOURCE_STABILITY_ATTEMPT=%s NATIVE_DECISION=%s\n' "$ATTEMPT" "$NATIVE_DECISION"

    if [ "$NATIVE_DECISION" = 'SOURCE_STABLE' ]; then
        STABLE=1
        "$P/bin/cp" -- "$SNAP_TAR" "$BASELINE_TAR.tmp"
        "$P/bin/mv" -f -- "$BASELINE_TAR.tmp" "$BASELINE_TAR"
        "$P/bin/chmod" 0400 "$BASELINE_TAR"
        break
    fi

    ATTEMPT=$((ATTEMPT + 1))
done

[ "$STABLE" -eq 1 ] || {
    printf 'HOLD=NO_NATIVE_CONFIRMED_STABLE_PRODUCTION_SNAPSHOT_WITHIN_BOUND\n'
    exit 34
}

BASELINE_DIGEST=$(hash1 "$BASELINE_TAR")
BASELINE_COUNT=$(entry_count "$BASELINE_TAR")
[ "$BASELINE_DIGEST" = "$SNAPSHOT_DIGEST" ] || exit 35
[ "$BASELINE_COUNT" = "$SNAPSHOT_COUNT" ] || exit 36
printf 'IMMUTABLE_BASELINE_SHA256=%s\n' "$BASELINE_DIGEST"
printf 'IMMUTABLE_BASELINE_ENTRY_COUNT=%s\n' "$BASELINE_COUNT"

"$P/bin/rm" -rf -- "$CANDIDATE"
"$P/bin/mkdir" -p "$CANDIDATE"
"$P/bin/tar" -xf "$BASELINE_TAR" -C "$CANDIDATE" || exit 37

CAND_TAR="$CAP/candidate_after_migration.tar"
canonical_candidate_capture "$CAND_TAR" || exit 38
CANDIDATE_DIGEST=$(hash1 "$CAND_TAR")
CANDIDATE_COUNT=$(entry_count "$CAND_TAR")
MUTATED_DIGEST=""
MUTATED_COUNT=""
RESTORED_DIGEST=""
RESTORED_COUNT=""

write_all_inputs VERIFY_MIGRATION
run_verifier VERIFY_EXACT_MIGRATION || exit 39
[ "$("$P/bin/cat" "$DECISION_MEM")" = 'MIGRATION_READY' ] || exit 40

REAL_CANDIDATE_DIGEST="$CANDIDATE_DIGEST"
CANDIDATE_DIGEST="0000000000000000000000000000000000000000000000000000000000000000"
write_all_inputs VERIFY_MIGRATION
run_verifier MIGRATION_DIGEST_MISMATCH_REFUSAL || exit 41
[ "$("$P/bin/cat" "$DECISION_MEM")" = 'MIGRATION_REFUSED' ] || exit 42
CANDIDATE_DIGEST="$REAL_CANDIDATE_DIGEST"

FAULT_FILE=$("$P/bin/find" "$CANDIDATE" -type f -print | "$P/bin/sort" | "$P/bin/head" -n1)
[ -n "$FAULT_FILE" ] || exit 43
printf 'CANDIDATE_FAULT_FILE=%s\n' "$FAULT_FILE"
"$P/bin/chmod" u+w "$FAULT_FILE" || exit 43
"$P/bin/printf" '\nV224R1_INJECTED_CANDIDATE_FAULT' >> "$FAULT_FILE" || exit 43

MUT_TAR="$CAP/candidate_mutated.tar"
canonical_candidate_capture "$MUT_TAR" || exit 44
MUTATED_DIGEST=$(hash1 "$MUT_TAR")
MUTATED_COUNT=$(entry_count "$MUT_TAR")

write_all_inputs VERIFY_MUTATION
run_verifier VERIFY_CANDIDATE_MUTATION_DETECTED || exit 45
[ "$("$P/bin/cat" "$DECISION_MEM")" = 'MUTATION_DETECTED' ] || exit 46

"$P/bin/rm" -rf -- "$CANDIDATE"
"$P/bin/mkdir" -p "$CANDIDATE"
"$P/bin/tar" -xf "$BASELINE_TAR" -C "$CANDIDATE" || exit 47

REST_TAR="$CAP/candidate_after_rollback.tar"
canonical_candidate_capture "$REST_TAR" || exit 48
RESTORED_DIGEST=$(hash1 "$REST_TAR")
RESTORED_COUNT=$(entry_count "$REST_TAR")

write_all_inputs VERIFY_ROLLBACK
run_verifier VERIFY_EXACT_ROLLBACK || exit 49
[ "$("$P/bin/cat" "$DECISION_MEM")" = 'ROLLBACK_READY' ] || exit 50

V24_PID_AFTER=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AFTER=%s\n' "$V24_PID_AFTER"
[ "$V24_PID_AFTER" = "$V24_PID" ] || exit 51

printf '\nV224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT=PASS\n'
printf 'LIVE_PRODUCTION_STABLE_SNAPSHOT_NATIVE_CONFIRMED=PASS\n'
printf 'PRODUCTION_STOPPED_FOR_SNAPSHOT=NO\n'
printf 'EXACT_CANDIDATE_MIGRATION_NATIVE_VERIFIED=PASS\n'
printf 'MIGRATION_DIGEST_MISMATCH_REFUSAL=PASS\n'
printf 'CANDIDATE_FAULT_DETECTED_NATIVELY=PASS\n'
printf 'IMMUTABLE_BASELINE_ROLLBACK_NATIVE_VERIFIED=PASS\n'
printf 'PRODUCTION_V24_REMAINED_RUNNING_SAME_PID=PASS\n'
printf 'PRODUCTION_ADMISSION_WRITE_TARGET=NO\n'
printf 'HOST_MIGRATION_DECISION=NO\n'
printf 'HOST_ROLLBACK_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'LIVE_PRODUCTION_STATE_SNAPSHOT=PROVEN_IN_DECLARED_PACKAGE_SCOPE\n'
printf 'SHADOW_STATE_MIGRATION_BYTE_IDENTITY=PROVEN_IN_DECLARED_PACKAGE_SCOPE\n'
printf 'SHADOW_ROLLBACK_BYTE_IDENTITY=PROVEN_AFTER_INJECTED_CANDIDATE_FAULT\n'
printf 'CANDIDATE_STARTUP_FROM_MIGRATED_STATE=NOT_PROVEN\n'
printf 'PRODUCTION_PROMOTION_ALLOWED=NO\n'
printf 'PROMOTION_BLOCKER=CANDIDATE_STARTUP_AND_SUPERVISOR_CUTOVER_ROLLBACK_NOT_PROVEN\n'
printf 'MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN\n'
printf 'PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'NEXT_ACTION=CHECKPOINT_V224R1_THEN_PROVE_CANDIDATE_STARTUP_FROM_MIGRATED_STATE_AND_REVERSIBLE_SUPERVISOR_CUTOVER\n'
