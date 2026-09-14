#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
C="$HERE/control/SIGMA_AIL_BRAIN_COORDINATOR_R1.sh"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
ROOT="$TMP/root"; mkdir -p "$ROOT" "$TMP/evidence"
echo BOOTSTRAP_OK > "$TMP/evidence/bootstrap.receipt"
echo GATE_PASS > "$TMP/evidence/gate.receipt"
echo RESULT_OK > "$TMP/evidence/run.receipt"
HEAD0=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
HEAD1=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

O="$(bash "$C" "$ROOT" bootstrap "$HEAD0" M1 "$TMP/evidence/bootstrap.receipt")"; grep -q 'BOOTSTRAP=PASS' <<<"$O"
O="$(bash "$C" "$ROOT" admit GATE_A TASK_ALPHA RECEIPT_A "$TMP/evidence/gate.receipt")"; grep -q 'ADMISSION_REGISTER=PASS' <<<"$O"

cat > "$TMP/w1.req" <<REQ
WORKER_ID=W1
RUN_ID=R1
TASK=TASK_ALPHA
GENERATION_LANE=G3A
PARENT_BRAIN_HEAD=$HEAD0
MODEL_GENERATION=M1
ACCESS_MODE=WRITE
EXPECTED_GATE=GATE_A
EXPECTED_RECEIPT=RECEIPT_A
REQ
O="$(bash "$C" "$ROOT" register "$TMP/w1.req")"; grep -q 'LEASE=GRANTED' <<<"$O"
O="$(bash "$C" "$ROOT" authorize R1 WRITE)"; grep -q 'WRITE=ALLOW' <<<"$O"
O="$(bash "$C" "$ROOT" authorize R1 LEARN)"; grep -q 'LEARN=ALLOW' <<<"$O"

cat > "$TMP/w2.req" <<REQ
WORKER_ID=W2
RUN_ID=R2
TASK=TASK_ALPHA
GENERATION_LANE=G3B
PARENT_BRAIN_HEAD=$HEAD0
MODEL_GENERATION=M1
ACCESS_MODE=WRITE
EXPECTED_GATE=GATE_A
EXPECTED_RECEIPT=RECEIPT_A
REQ
set +e
O="$(bash "$C" "$ROOT" register "$TMP/w2.req" 2>&1)"; RC=$?
set -e
[ "$RC" -ne 0 ]; grep -q 'CONFLICTING_LEASE=REJECT' <<<"$O"

cat > "$TMP/done1.env" <<DONE
RUN_ID=R1
PARENT_HEAD=$HEAD0
RESULT=PASS
NEW_HEAD=$HEAD1
MODEL_GENERATION_BEFORE=M1
MODEL_GENERATION_AFTER=M2
EVIDENCE_RECEIPT=$TMP/evidence/run.receipt
DONE
O="$(bash "$C" "$ROOT" complete "$TMP/done1.env")"; grep -q "CANONICAL_BRAIN_HEAD=$HEAD1" <<<"$O"

cat > "$TMP/stale.req" <<REQ
WORKER_ID=W3
RUN_ID=R3
TASK=TASK_ALPHA
GENERATION_LANE=G3C
PARENT_BRAIN_HEAD=$HEAD0
MODEL_GENERATION=M1
ACCESS_MODE=WRITE
EXPECTED_GATE=GATE_A
EXPECTED_RECEIPT=RECEIPT_A
REQ
set +e
O="$(bash "$C" "$ROOT" register "$TMP/stale.req" 2>&1)"; RC=$?
set -e
[ "$RC" -ne 0 ]; grep -q 'STALE_HEAD_WRITER=REJECT' <<<"$O"

cat > "$TMP/read.req" <<REQ
WORKER_ID=RDR
RUN_ID=RR
TASK=READ_ANY
GENERATION_LANE=GX
PARENT_BRAIN_HEAD=$HEAD0
MODEL_GENERATION=M1
ACCESS_MODE=READ
EXPECTED_GATE=NONE
EXPECTED_RECEIPT=NONE
REQ
O="$(bash "$C" "$ROOT" register "$TMP/read.req")"; grep -q 'LEASE=GRANTED_READ_ONLY' <<<"$O"

cat > "$TMP/unreg.done" <<DONE
RUN_ID=NO_SUCH_RUN
PARENT_HEAD=$HEAD1
RESULT=PASS
NEW_HEAD=cccccccccccccccccccccccccccccccccccccccc
MODEL_GENERATION_BEFORE=M2
MODEL_GENERATION_AFTER=M3
EVIDENCE_RECEIPT=$TMP/evidence/run.receipt
DONE
set +e
O="$(bash "$C" "$ROOT" complete "$TMP/unreg.done" 2>&1)"; RC=$?
set -e
[ "$RC" -ne 0 ]; grep -q 'UNREGISTERED_WRITER=REJECT' <<<"$O"
set +e
O="$(bash "$C" "$ROOT" authorize NO_SUCH_RUN WRITE 2>&1)"; RC=$?
set -e
[ "$RC" -ne 0 ]; grep -q 'UNREGISTERED_WRITER=REJECT' <<<"$O"

O="$(bash "$C" "$ROOT" status)"; grep -q 'ONE_SIGMA_AIL=YES' <<<"$O"
grep -q 'ONE_WRITER=YES' <<<"$O"
grep -q 'NO_STATE_FORK=MANDATORY' <<<"$O"

echo "ONE_SIGMA_AIL_COORDINATOR_SELFTEST=PASS"
echo "CONFLICTING_LEASE_REJECT=PASS"
echo "STALE_HEAD_WRITER_REJECT=PASS"
echo "UNREGISTERED_WRITER_REJECT=PASS"
echo "READ_ONLY_STALE_ALLOWED=PASS"
echo "CANONICAL_HEAD_ADVANCE_BY_COORDINATOR=PASS"
echo "PER_OPERATION_AUTHORIZATION=PASS"
