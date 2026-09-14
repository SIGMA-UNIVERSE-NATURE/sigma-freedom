#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
C="$HERE/control/SIGMA_AIL_BRAIN_COORDINATOR_R2.sh"
run_c(){ bash "$C" "$@"; }
T="${TMPDIR:-/tmp}/sigma_coord_r2_test.$$"
ROOT="$T/root"; mkdir -p "$ROOT/.sigma_ail" "$T/runtime/state" "$T/runtime"
trap 'rm -rf "$T"' EXIT
printf '%s\n' aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa > "$T/runtime/state/HEAD"
: > "$T/runtime/writer.lock"
ln -s "$T/runtime/state/HEAD" "$ROOT/.sigma_ail/BRAIN_HEAD"
ln -s "$T/runtime/writer.lock" "$ROOT/.sigma_ail/WRITER.lock"
printf '%s\n' 0 > "$ROOT/.sigma_ail/MODEL_GENERATION"

vout="$(run_c "$ROOT" verify-runtime)"; grep -q 'RUNTIME_VERIFY=PASS' <<<"$vout"
receipt="$(awk -F= '$1=="EVIDENCE_RECEIPT"{print substr($0,length($1)+2)}' <<<"$vout")"
run_c "$ROOT" attach "$receipt" >/dev/null

gate_receipt="$T/gate.receipt"; echo PASS > "$gate_receipt"
TASK='NATIVE_LEARN_TRANSACTION'
run_c "$ROOT" admit GATE1 "$TASK" RECEIPT1 "$gate_receipt" >/dev/null

req="$T/req.env"
cat > "$req" <<REQ
WORKER_ID=G3A
RUN_ID=R1
TASK=$TASK
GENERATION_LANE=G3A
PARENT_BRAIN_HEAD=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
MODEL_GENERATION=0
ACCESS_MODE=WRITE
EXPECTED_GATE=GATE1
EXPECTED_RECEIPT=RECEIPT1
REQ
run_c "$ROOT" register "$req" > "$T/reg.out"
grep -q 'LEASE=GRANTED' "$T/reg.out"
run_c "$ROOT" authorize R1 LEARN | grep -q 'LEARN=ALLOW'

req2="$T/req2.env"; sed 's/RUN_ID=R1/RUN_ID=R2/; s/WORKER_ID=G3A/WORKER_ID=G3B/' "$req" > "$req2"
set +e; run_c "$ROOT" register "$req2" > "$T/conf.out" 2>&1; rc=$?; set -e
[ "$rc" -ne 0 ]; grep -q 'CONFLICTING_LEASE=REJECT' "$T/conf.out"

printf '%s\n' bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb > "$T/runtime/state/HEAD"
echo evidence > "$T/native.receipt"
comp="$T/comp.env"
cat > "$comp" <<COMP
RUN_ID=R1
PARENT_HEAD=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
RESULT=COMMITTED
NEW_HEAD=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
MODEL_GENERATION_BEFORE=0
MODEL_GENERATION_AFTER=0
EVIDENCE_RECEIPT=$T/native.receipt
COMP
run_c "$ROOT" complete "$comp" > "$T/complete.out"
grep -q 'RESULT_ACCEPTED=YES' "$T/complete.out"
[ "$(cat "$T/runtime/state/HEAD")" = bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ]

req3="$T/req3.env"; sed 's/RUN_ID=R1/RUN_ID=R3/; s/WORKER_ID=G3A/WORKER_ID=G3C/' "$req" > "$req3"
set +e; run_c "$ROOT" register "$req3" > "$T/stale.out" 2>&1; rc=$?; set -e
[ "$rc" -ne 0 ]; grep -q 'STALE_HEAD_WRITER=REJECT' "$T/stale.out"

set +e; run_c "$ROOT" authorize NEVER COMMIT > "$T/unreg.out" 2>&1; rc=$?; set -e
[ "$rc" -ne 0 ]; grep -q 'UNREGISTERED_WRITER=REJECT' "$T/unreg.out"

python - "$T/runtime/writer.lock" "$T/held" <<'PY' &
import fcntl,sys,time,pathlib
f=open(sys.argv[1],'r+b',buffering=0)
fcntl.flock(f.fileno(),fcntl.LOCK_EX)
pathlib.Path(sys.argv[2]).write_text('held')
time.sleep(4)
PY
hp=$!
for _ in 1 2 3 4 5 6 7 8; do [ -f "$T/held" ] && break; sleep .1; done
req4="$T/req4.env"
cat > "$req4" <<REQ
WORKER_ID=GX
RUN_ID=R4
TASK=$TASK
GENERATION_LANE=GX
PARENT_BRAIN_HEAD=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
MODEL_GENERATION=0
ACCESS_MODE=WRITE
EXPECTED_GATE=GATE1
EXPECTED_RECEIPT=RECEIPT1
REQ
set +e; run_c "$ROOT" register "$req4" > "$T/nativebusy.out" 2>&1; rc=$?; set -e
[ "$rc" -ne 0 ]; grep -q 'NATIVE_WRITER_ACTIVE' "$T/nativebusy.out"
wait "$hp"

echo ONE_SIGMA_AIL_COORDINATOR_R2_SELFTEST=PASS
echo LIVE_RUNTIME_HEAD_ALIAS=PASS
echo NATIVE_WRITER_ALIAS_CONFLICT=PASS
echo CONFLICTING_COORDINATION_LEASE_REJECT=PASS
echo STALE_HEAD_WRITER_REJECT=PASS
echo UNREGISTERED_WRITER_REJECT=PASS
echo COORDINATOR_DOES_NOT_ADVANCE_RUNTIME_HEAD=PASS
echo HOST_COGNITION=NO
echo NO_STATE_FORK=MANDATORY
