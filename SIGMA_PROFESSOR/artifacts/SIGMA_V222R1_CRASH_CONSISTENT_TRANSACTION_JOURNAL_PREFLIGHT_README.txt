SIGMA V2.22R.1 — CRASH-CONSISTENT TRANSACTION JOURNAL

This introduces a native `.sigma` transaction/recovery protocol without claiming filesystem append atomicity.

Native record format:

PREPARE:
TX=<id> || PHASE=PREPARE || PAYLOAD=<payload> || TXLEN=<unary> || PLEN=<unary> || END=PREPARE

COMMIT:
TX=<id> || PHASE=COMMIT || PAYLOAD=<payload> || TXLEN=<unary> || PLEN=<unary> || END=COMMIT

Both records contain the exact payload. Recovery requires:
- a syntactically complete PREPARE;
- a syntactically complete COMMIT;
- exact TX match;
- exact payload match;
- unary TX length match;
- unary payload length match;
- exact phase end sentinel;
- no conflicting valid PREPARE payloads for the same TX.

Each native append begins with a newline. Therefore a prior truncated tail can be delimited on retry and remains an ignored malformed line instead of merging with the next full record.

Modes:
- RECOVER_ONLY
- PREPARE_ONLY
- COMMIT_TRANSACTION

Admission faults:
- clean commit + fresh-VM idempotency;
- crash-point simulation after PREPARE_ONLY;
- torn PREPARE tail;
- torn COMMIT tail;
- garbage tail;
- conflicting prepares;
- invalid delimiter input;
- journal line bound refusal;
- deterministic journal replay.

Important claim boundary:
A PASS proves native crash-consistent recovery under injected truncated-tail fault models.
It does NOT prove that the underlying filesystem or `append_text` primitive is physically atomic.

Claim after PASS:
`CRASH_CONSISTENT_JOURNAL_RECOVERY=PROVEN_UNDER_INJECTED_TRUNCATED_TAIL_FAULTS`

Still:
`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`
`PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED`
`PRODUCTION_PROMOTION_ALLOWED=NO`

Next integration:
wrap the shadow scheduler's persisted continuation intent in this journal before considering migration/promotion.

Source SHA256:
643c6f534777193951d772e9653463b5d97ceebb7c35f14b21390a3308ef4c64

Runner SHA256:
6038ba6d2a6d4a16cc67c98386227c130fdc2f659c6dd850457b5c0ce4a4be9e

Static:
H_CALL_ARITY_AUDIT=PASS
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0
