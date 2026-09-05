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

Observed pre-runtime admission failures

1. SOURCE identity before install
- locked SIGMAC hash matched;
- locked VM hash matched;
- `SOURCE_SHA256` was empty;
- `HOLD=LOCKED_IDENTITY_MISMATCH`;
- root cause: first runner revision hashed `$BRAIN/.sigma_exec/...V4A1.sigma` before installing the pinned repository source.

2. Production namespace audit correction
- before rerunning the corrected source-install revision, audit found its `BRAIN` still pointed at production `BRAIN/EXTRA BRAIN_OPPO_24826`;
- the observed HOLD happened before any source copy or test-state mutation, so that failed run did not mutate production memory;
- nevertheless, any V4-A admission runner that writes fixtures/ledger/action/bytecode into production BRAIN is forbidden;
- runner was therefore corrected again before runtime admission.

Current correction
- source artifact is hashed/equality-gated from the repository first;
- source bytes are copied mechanically only into an isolated shadow BRAIN;
- all V4-A fixture memory, ledger, action, target, source copy and bytecode live under:
  `$HOME/SIGMA/SIGMA_V4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT/shadow/BRAIN/EXTRA BRAIN_OPPO_24826/.sigma_exec`;
- production BRAIN is not a write target;
- production V2.4 PID is observed before/after as isolation evidence;
- only locked sigmac + locked VM execute the native capability.

Current runner Git blob:
`c71f1248b2f2c33a7918488913661c8e5f371530`

Current runner commit:
`381f6168a32ead9af7b529706d5b9cb19901aca0`

Do not use prior runner blobs `4eb9286d...` or `6afbc9ed...` for admission.

This failure history is harness/setup evidence only. V4-A native runtime capability remains NOT PROVEN until a locked-VM PASS transcript is obtained.

Claim after PASS:
`NATIVE_PRODUCTIVITY_WORK_ARBITRATION=PROVEN_IN_BOUNDED_TESTED_SCOPE`

Still:
`V4_PRODUCTION_PROMOTION_ALLOWED=NO`
`SEMANTIC_UNDERSTANDING=NOT_PROVEN`
`BOUNDED_FILE_IO=NOT_PROVEN`
`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

Next after PASS:
V4-B segmented received-context learner so fetched material can resume across bounded segments instead of becoming permanent HOLD after whole-context rc=9 pressure.

Source SHA256:
`12c32f07d39bacedf8dd1a2371f9b33801106d256d6166fed03fbaa224416ed2`

Static source audits:
H_CALL_ARITY_AUDIT=PASS
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE

Current runner `bash -n` was checked before commit and passed.
