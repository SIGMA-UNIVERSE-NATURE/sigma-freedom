#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BASE="$HOME_SIGMA/SIGMA_V4C3T1R3_NATIVE_SLEEP_CLOCK_PREFLIGHT"
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

REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_SLEEP_CLOCK_PROBE_V4C3T1R3.sigma"
EXPECTED_BLOB=5fe99ed5f0017209676babe7319479c38b14d05d
REPO_SRC="$REPO/$REL"
SRC="$E/SIGMA_V4_NATIVE_SLEEP_CLOCK_PROBE_V4C3T1R3.sigma"
BC="$E/SIGMA_V4_NATIVE_SLEEP_CLOCK_PROBE_V4C3T1R3.sigmab"

mkdir -p "$E" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C3T1R3_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
printf 'SIGMA_PHASE=V4C3T1R3_NATIVE_SLEEP_CLOCK_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_TIME_DECISION=NO\n'
printf 'HOST_SLEEP=NO\n'
printf 'R1_FAILURE_PRESERVED=YES\n'
printf 'R2_FAILURE_PRESERVED=YES\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ -f "$REPO_SRC" ] || { printf 'HOLD=SOURCE_MISSING\n'; exit 23; }

ACTUAL_BLOB=$(git -C "$REPO" hash-object "$REPO_SRC")
printf 'SOURCE_GIT_BLOB=%s\n' "$ACTUAL_BLOB"
printf 'SOURCE_SHA256=%s\n' "$(hash1 "$REPO_SRC")"
[ "$ACTUAL_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=SOURCE_BLOB_MISMATCH\n'; exit 24; }

cp -- "$REPO_SRC" "$SRC" || { printf 'HOLD=SOURCE_COPY_FAILED\n'; exit 25; }
INSTALLED_BLOB=$(git -C "$REPO" hash-object "$SRC")
printf 'INSTALLED_GIT_BLOB=%s\n' "$INSTALLED_BLOB"
[ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=INSTALLED_BLOB_MISMATCH\n'; exit 26; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || { printf 'HOLD=SIGMAC_FAILED\n'; exit 30; }
[ -s "$BC.partial" ] || { printf 'HOLD=BYTECODE_EMPTY\n'; exit 31; }
mv -f -- "$BC.partial" "$BC" || exit 32
chmod 0400 "$BC" || exit 33
printf 'BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

VM_LOG="$LOG/vm.log"
(
    cd "$BRAIN" || exit 40
    "$VM" "$BC"
) > "$VM_LOG" 2>&1
VM_RC=$?
printf 'VM_RC=%s LOG=%s\n' "$VM_RC" "$VM_LOG"
"$P/bin/cat" "$VM_LOG"
[ "$VM_RC" -eq 0 ] || { printf 'HOLD=NATIVE_SLEEP_VM_FAILED\n'; exit 41; }

"$P/bin/grep" -F -x 'TIME_STATUS NATIVE_SLEEP_CLOCK_PROGRESS_PROVEN' "$VM_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_SLEEP_CLOCK_PROGRESS_NOT_PROVEN\n'
    exit 42
}
"$P/bin/grep" -F -x 'HOST_SLEEP NO' "$VM_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=HOST_SLEEP_AUDIT_NOT_OBSERVED\n'
    exit 43
}

printf '\nV4C3T1R3_NATIVE_SLEEP_CLOCK_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'NATIVE_TIME_NOW_EXECUTION=PASS_IN_SINGLE_INVOCATION_SCOPE\n'
printf 'NATIVE_TIME_SLEEP_EXECUTION=PASS_IN_TWO_SECOND_MINIMUM_PROGRESS_SCOPE\n'
printf 'HOST_TIME_DECISION=NO\n'
printf 'HOST_SLEEP=NO\n'
printf 'FRESH_VM_CLOCK_PERSISTENCE=NOT_PROVEN\n'
printf 'THREE_MINUTE_OBSERVE_PAUSE=NOT_YET_PROVEN\n'
printf 'NEXT_ACTION=BUILD_PROGRESS_BUDGET_REFLECTION_REPORT_PLAN_CONTROLLER_THEN_REAL_180_SECOND_NATIVE_PAUSE_GATE\n'
