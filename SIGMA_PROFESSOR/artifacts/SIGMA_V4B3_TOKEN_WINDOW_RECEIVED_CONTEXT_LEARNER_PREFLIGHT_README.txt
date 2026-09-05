SIGMA V4-B3 — NATIVE TOKEN-WINDOW RECEIVED-CONTEXT LEARNER

Purpose
-------
Resolve the real V4-B2 production counterexample in which context
49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382
contained a 209-token line and native V4-B1 correctly refused its 65-token
selected-line limit.

Observed counterexample
-----------------------
Document bytes: 3948
Document lines: 10
Maximum tokens on one mechanically characterized line: 209
Total whitespace fields across the 10 observed lines: 659
A 16-token window requires 45 non-empty-line windows for that document.

Native V4-B3 behavior
---------------------
- persistent native cursor is a pair: line index + token offset;
- 16 selected-line tokens per native VM invocation;
- nonzero-offset windows include previous-token -> first-window-token relation,
  preserving cross-window bigram continuity;
- progress ledger unifies structural evidence and next cursor;
- malformed/foreign progress records are ignored;
- progress-at-end with missing completion recovers completion idempotently;
- out-of-range line/token cursor is refused;
- host does not split tokens, choose windows, decide completion, decide retry,
  or perform learning.

ABI/resource boundary
---------------------
The current runtime still whole-file reads context text and `str_split`s the
selected line. `MAX_SELECTED_LINE_TOKENS_CURRENT_ABI=4096` is a structural
resource-safety ceiling, not a semantic/result rule and not proof of bounded
file I/O. Actual structural relation computation is limited to a 16-token
window per invocation.

Source
------
SIGMA_PROFESSOR/artifacts/SIGMA_V4_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_V4B3.sigma
SHA256:
8a5687b4e83d74947dd9b1ca1a2729be104eff3d4b935cc64c6ef800f628af83
Git blob:
a20279d529422c3c380fc832babd89fd6fe6e34b
Source commit:
45c8f8f3d926d8d9040b86fcb6c51a4bedc28365

Runner
------
SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4B3_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_PREFLIGHT.sh
Git blob:
411d281dfcebd30a24c4c71234fad230936cb177
Runner commit:
87bb51ea149c0be459cd415790ef9d15547ce8fa

Runner additionally refuses preflight if production V2.4 is not running.

Static
------
H_CALL_ARITY_AUDIT=PASS_50_OF_50
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BRACE_PAREN_BALANCE=PASS
RUNNER_BASH_N=PASS

Claim only after runtime PASS
-----------------------------
TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_209_TOKEN_LINE_BOUNDED_TEST_SCOPE

Still
-----
REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN
BOUNDED_FILE_IO=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
V4_PRODUCTION_PROMOTION_ALLOWED=NO

Next after PASS
---------------
Replay exact real context 49c16c... bytes through V4-B3 shadow before testing the remaining observed V2.4 rc9-held contexts.
