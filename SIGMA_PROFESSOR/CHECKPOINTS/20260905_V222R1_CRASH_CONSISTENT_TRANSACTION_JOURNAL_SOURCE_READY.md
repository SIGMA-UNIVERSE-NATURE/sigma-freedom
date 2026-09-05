# V2.22R.1 CRASH-CONSISTENT TRANSACTION JOURNAL — SOURCE READY

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`RUNTIME_ADMISSION=NOT_PROVEN`

This checkpoint records exact candidate identities and static readiness only.

## Candidate

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_CRASH_CONSISTENT_TRANSACTION_JOURNAL_V2_22R1.sigma`

Source SHA256:
`643c6f534777193951d772e9653463b5d97ceebb7c35f14b21390a3308ef4c64`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V222R1_CRASH_CONSISTENT_TRANSACTION_JOURNAL_PREFLIGHT.sh`

Runner SHA256:
`6038ba6d2a6d4a16cc67c98386227c130fdc2f659c6dd850457b5c0ce4a4be9e`

README:
`SIGMA_PROFESSOR/artifacts/SIGMA_V222R1_CRASH_CONSISTENT_TRANSACTION_JOURNAL_PREFLIGHT_README.txt`

## Static gates

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n` RC = 0

`str_len` is used by the native protocol for unary self-validation. V2.22 runtime admission must itself prove this dependency works on the locked VM. No host semantic substitute is allowed if it fails.

## Protocol contract

Each critical transaction is represented by separate append-only PREPARE and COMMIT records containing the exact same TX and PAYLOAD plus unary TX/payload lengths and an exact phase end sentinel.

Recovery accepts a transaction only if both complete records are valid and consistent. Malformed, truncated, unpaired, payload-mismatched or conflicting records are ignored/refused according to the native policy.

Every native append begins with a newline so a previously truncated tail can be delimited by a retry and remain an ignored malformed line.

## Admission fault model

The runner injects:

- PREPARE-only restart;
- torn PREPARE tail;
- torn COMMIT tail;
- garbage tail;
- conflicting prepares;
- invalid delimiter payload;
- journal over-limit state;
- deterministic replay and fresh-VM idempotency.

## Claim boundary

A future PASS may establish:

`CRASH_CONSISTENT_JOURNAL_RECOVERY=PROVEN_UNDER_INJECTED_TRUNCATED_TAIL_FAULTS`

It must NOT establish:

- `MID_APPEND_CRASH_ATOMICITY`;
- physical filesystem atomicity;
- bounded file I/O;
- semantic understanding.

`PRODUCTION_PROMOTION_ALLOWED=NO` until this protocol is admitted and integrated around real shadow scheduled-intent state.

## Production discipline

Keep V2.4 running unchanged.
