# V4-B2R.2 REAL V2.4 RC9 REPLAY — TOKEN LIMIT FAILURE

Observed runtime evidence from real held production context:

- context: `49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`
- V4-B2R.2 harness reached native SIGMA execution on the real context.
- final native status: `REFUSE_TOKEN_LIMIT`
- `CURSOR_COMMIT_COUNT=0`
- `EVIDENCE_COMMIT_COUNT=0`
- `COMPLETION_COMMIT_COUNT=0`
- final harness evidence: `HOLD=REAL_CONTEXT_NOT_COMPLETED ... status=REFUSE_TOKEN_LIMIT`

Classification:

`V4B2R2_REAL_RC9_REPLAY=FAIL_ON_NATIVE_TOKEN_LIMIT`
`HARNESS_FILESYSTEM_PERMISSION_BLOCKER=RESOLVED_BEFORE_THIS_RUN`
`REAL_CONTEXT_NATIVE_VM_REACHED=YES`
`PARTIAL_LEARNING_MUTATION=NO`
`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`
`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Root cause in V4-B1 design:

- segmentation cursor advances by context line;
- selected lines are split into all tokens in that line;
- `MAX_TOKENS_PER_LINE=65` is an admission bound;
- at least one line in the first selected segment of the real context exceeded that bound;
- native SIGMA correctly refused mutation instead of risking VM step-limit pressure.

Required successor behavior:

- do NOT simply raise/remove the token bound;
- add native persisted token-window cursor inside a line;
- bounded token window per VM invocation;
- preserve within-line structural bigram continuity across token-window boundaries;
- fresh-VM resume;
- crash/idempotency evidence;
- no host token-window selection, retry decision, completion decision, or learning;
- production V2.4 remains unchanged/running.

Next action:

`BUILD_V4B3_NATIVE_TOKEN_WINDOW_RESUMABLE_SEGMENTED_LEARNER`
