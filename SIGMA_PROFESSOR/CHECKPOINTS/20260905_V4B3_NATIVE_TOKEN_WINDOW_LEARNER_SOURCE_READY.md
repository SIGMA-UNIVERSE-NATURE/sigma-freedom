# V4-B3 native token-window learner — SOURCE READY

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Triggering real evidence

V4-B2R.2 reached native VM on real V2.4 rc9-held context
`49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`
and returned `REFUSE_TOKEN_LIMIT` with zero cursor/evidence/completion commits.

Mechanical characterization of the exact raw document:

- bytes: 3948
- lines: 10
- maximum tokens on one line: 209
- total observed whitespace fields: 659
- 16-token windows needed across non-empty lines: 45

## V4-B3 source

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_V4B3.sigma`

SHA256:
`8a5687b4e83d74947dd9b1ca1a2729be104eff3d4b935cc64c6ef800f628af83`

Git blob:
`a20279d529422c3c380fc832babd89fd6fe6e34b`

Source commit:
`45c8f8f3d926d8d9040b86fcb6c51a4bedc28365`

## V4-B3 preflight runner

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4B3_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_PREFLIGHT.sh`

Git blob:
`411d281dfcebd30a24c4c71234fad230936cb177`

Runner commit:
`87bb51ea149c0be459cd415790ef9d15547ce8fa`

The runner refuses if production V2.4 is not running before admission begins.

## Native design

- native persistent cursor pair `(line_index, token_offset)`;
- fixed structural computation window of 16 selected-line tokens per VM invocation;
- cross-window bigram boundary included exactly by starting later windows with previous-token -> first-window-token;
- progress ledger carries structural profile plus next cursor;
- completion ledger remains separate and recoverable;
- malformed progress tail ignored;
- cursor pair out of range refused;
- host window selection/completion/retry/learning all NO.

Current ABI still reads the whole context and splits the selected line. Therefore:

`WHOLE_FILE_READ_CURRENT_ABI=YES`
`WHOLE_SELECTED_LINE_SPLIT_CURRENT_ABI=YES`
`BOUNDED_FILE_IO=NOT_PROVEN`

`MAX_SELECTED_LINE_TOKENS_CURRENT_ABI=4096` is a structural resource-safety ceiling, not a semantic/result rule.

## Static admission

`H_CALL_ARITY_AUDIT=PASS_50_OF_50`
`NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
`STR_STARTS_DEPENDENCY=NONE`
`DIRECT_STR_DEPENDENCY=NONE`
`BRACE_PAREN_BALANCE=PASS`
`RUNNER_BASH_N=PASS`

## Runtime status

`V4B3_LOCKED_SIGMAC_COMPILE=NOT_RUN`
`V4B3_TOTAL_VM_INVOCATIONS=0`
`V4B3_ADMISSION=NOT_RUN`

No runtime claim may be made yet.

Still:

`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`
`SEMANTIC_UNDERSTANDING=NOT_PROVEN`
`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Next action

Install exact source/runner blobs from `origin/SIGMA_LIFE`, run V4-B3 preflight in isolated shadow state, preserve compiler/VM/source/bytecode identities and all failure evidence. If PASS, checkpoint runtime proof, then replay exact real context `49c16...` through V4-B3 shadow.
