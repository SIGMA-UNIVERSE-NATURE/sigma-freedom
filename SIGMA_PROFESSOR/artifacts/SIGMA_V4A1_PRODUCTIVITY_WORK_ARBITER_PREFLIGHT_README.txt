SIGMA V4-A.1 — NATIVE PRODUCTIVITY / WORK ARBITER

Purpose:
Start the V4 production-successor efficiency upgrade while V2.4 keeps running unchanged.

Native policy:
- recovered continuation first;
- otherwise round-robin structural sources using persistent last-source ledger:
  RECEIVED -> RETRYABLE -> LOCAL -> FETCH;
- fetch is eligible only when native `time_now` reaches `NEXT_FETCH_NOT_BEFORE`;
- when fetch is rate-limited, eligible received/retryable/local work continues;
- WAIT only when no productive source is eligible.

This module does not perform semantic ranking.

Observed pre-runtime admission failure:
- `SIGMAC_SHA256` matched locked compiler;
- `VM_SHA256` matched locked VM;
- `SOURCE_SHA256` was empty;
- `HOLD=LOCKED_IDENTITY_MISMATCH`;
- root cause: the first runner revision hashed `$BRAIN/.sigma_exec/SIGMA_V4_PRODUCTIVITY_WORK_ARBITER_V4A1.sigma` before mechanically installing the pinned repository artifact there.

Correction:
- hash/equality-gate the pinned repo artifact first;
- copy exact source bytes mechanically into `.sigma_exec` only after equality passes;
- hash/equality-gate the installed copy;
- only then invoke locked `sigmac` and locked VM.

This failure is harness/setup evidence only. It does not prove or disprove V4-A runtime capability because the VM was not reached.

Claim after PASS:
`NATIVE_PRODUCTIVITY_WORK_ARBITRATION=PROVEN_IN_BOUNDED_TESTED_SCOPE`

Still:
`V4_PRODUCTION_PROMOTION_ALLOWED=NO`
`SEMANTIC_UNDERSTANDING=NOT_PROVEN`
`BOUNDED_FILE_IO=NOT_PROVEN`
`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

Next:
V4-B segmented received-context learner so fetched material can resume across bounded segments instead of becoming permanent HOLD after whole-context rc=9 pressure.

Source SHA256:
12c32f07d39bacedf8dd1a2371f9b33801106d256d6166fed03fbaa224416ed2

Corrected runner SHA256:
9cd9a4e735c49f8124b1d78ced2ab2c8d689421e9a5ce6b5b57d9329fb494626

Corrected runner Git blob:
6afbc9ed91a25f5ee2a27353286abbd23d20c8d1

Corrected runner commit:
e24210e60cb3a6721dfcf80a9a14cfe8a868403e

Static after correction:
H_CALL_ARITY_AUDIT=PASS
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0
