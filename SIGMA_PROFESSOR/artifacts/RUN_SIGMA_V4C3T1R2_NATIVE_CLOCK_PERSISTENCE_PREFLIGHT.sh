#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BASE="$HOME_SIGMA/SIGMA_V4C3T1R2_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT"
LOCK="$BASE/preflight.lock"
RUN_ID="$("$P/bin/date" +%s).$$"
STATE="$BASE/run.$RUN_ID"
BRAIN="$STATE/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
LOG="$STATE/log"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_CLOCK_PERSISTENCE_PROBE_V4C3T1R2.sigma"
EXPECTED_BLOB=ea2049170bcb072b9a12906b74d7bc3903d816a9
REPO_SRC="$REPO/$REL"
SRC="$E/SIGMA_V4_NATIVE_CLOCK_PERSISTENCE_PROBE_V4C3T1R2.sigma"
BC="$E/SIGMA_V4_NATIVE_CLOCK_PERSISTENCE_PROBE_V4C3T1R2.sigmab"
PREV="$E/SIGMA_V4C3T1R2_PREVIOUS_TIME_JSON.memory"
STATUS="$E/SIGMA_V4C3T1R2_STATUS.memory"

mkdir -p "$E" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C3T1R2_CLOCK_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
printf 'SIGMA_PHASE=V4C3T1R2_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_TIME_DECISION=NO\n'
printf 'HOST_SLEEP_ROLE=MECHANICAL_TIME_PASSAGE_FIXTURE_ONLY\n'
printf 'R1_FAILURE_PRESERVED=YES\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ -f "$REPO_SRC" ] || { printf 'HOLD=CLOCK_SOURCE_MISSING\n'; exit 23; }

ACTUAL_BLOB=$(git -C "$REPO" hash-object "$REPO_SRC")
printf 'CLOCK_SOURCE_GIT_BLOB=%s\n' "$ACTUAL_BLOB"
printf 'CLOCK_SOURCE_SHA256=%s\n' "$(hash1 "$REPO_SRC")"
[ "$ACTUAL_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=CLOCK_SOURCE_BLOB_MISMATCH\n'; exit 24; }

cp -- "$REPO_SRC" "$SRC" || { printf 'HOLD=CLOCK_SOURCE_COPY_FAILED\n'; exit 25; }
INSTALLED_BLOB=$(git -C "$REPO" hash-object "$SRC")
printf 'CLOCK_INSTALLED_GIT_BLOB=%s\n' "$INSTALLED_BLOB"
[ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=CLOCK_INSTALLED_BLOB_MISMATCH\n'; exit 26; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'CLOCK_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || { printf 'HOLD=CLOCK_SIGMAC_FAILED\n'; exit 30; }
[ -s "$BC.partial" ] || { printf 'HOLD=CLOCK_BYTECODE_EMPTY\n'; exit 31; }
mv -f -- "$BC.partial" "$BC" || exit 32
chmod 0400 "$BC" || exit 33
printf 'CLOCK_BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

: > "$PREV"
: > "$STATUS"

FIRST_LOG="$LOG/first.log"
SECOND_LOG="$LOG/second.log"

(
    cd "$BRAIN" || exit 40
    "$VM" "$BC"
) > "$FIRST_LOG" 2>&1
FIRST_RC=$?
printf 'CLOCK_FIRST_VM_RC=%s LOG=%s\n' "$FIRST_RC" "$FIRST_LOG"
"$P/bin/cat" "$FIRST_LOG"
[ "$FIRST_RC" -eq 0 ] || { printf 'HOLD=CLOCK_FIRST_VM_FAILED\n'; exit 41; }
"$P/bin/grep" -F -x 'TIME_STATUS CLOCK_FIRST_OBSERVATION' "$FIRST_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_CLOCK_FIRST_OBSERVATION_NOT_PROVEN\n'
    exit 42
}
"$P/bin/grep" -F -x 'NATIVE_TIME_SERIALIZATION JSON_MECHANICAL_ONLY' "$FIRST_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_CLOCK_JSON_SERIALIZATION_NOT_OBSERVED\n'
    exit 43
}

"$P/bin/sleep" 2

(
    cd "$BRAIN" || exit 44
    "$VM" "$BC"
) > "$SECOND_LOG" 2>&1
SECOND_RC=$?
printf 'CLOCK_SECOND_VM_RC=%s LOG=%s\n' "$SECOND_RC" "$SECOND_LOG"
"$P/bin/cat" "$SECOND_LOG"
[ "$SECOND_RC" -eq 0 ] || { printf 'HOLD=CLOCK_SECOND_VM_FAILED\n'; exit 45; }
"$P/bin/grep" -F -x 'TIME_STATUS CLOCK_PROGRESS_PROVEN' "$SECOND_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_CLOCK_PROGRESS_NOT_PROVEN\n'
    exit 46
}

FINAL_STATUS=$("$P/bin/cat" "$STATUS")
[ "$FINAL_STATUS" = "CLOCK_PROGRESS_PROVEN" ] || {
    printf 'HOLD=NATIVE_CLOCK_PERSISTED_STATUS_MISMATCH ACTUAL=%s\n' "$FINAL_STATUS"
    exit 47
}

printf '\nV4C3T1R2_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'NATIVE_TIME_NOW_EXECUTION=PASS_IN_TWO_OBSERVATION_SCOPE\n'
printf 'NATIVE_TIME_JSON_PERSISTENCE_ROUNDTRIP=PASS_IN_TWO_OBSERVATION_SCOPE\n'
printf 'NATIVE_TIME_PROGRESS_DECISION=PASS_IN_TWO_OBSERVATION_SCOPE\n'
printf 'HOST_TIME_DECISION=NO\n'
printf 'ONE_HOUR_DUTY_CYCLE=NOT_YET_PROVEN\n'
printf 'THREE_MINUTE_OBSERVE_PAUSE=NOT_YET_PROVEN\n'
printf 'NEXT_ACTION=BUILD_V4C3_NATIVE_DUTY_CYCLE_REFLECTION_REPORTER_AND_PLAN\n'
