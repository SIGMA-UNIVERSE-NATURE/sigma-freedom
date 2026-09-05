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

Runner SHA256:
58387b5843f8b58b3321564a4e9356478eba19f1ae9553baa4c33bf2c8aefcbb

Static:
H_CALL_ARITY_AUDIT=PASS
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0
