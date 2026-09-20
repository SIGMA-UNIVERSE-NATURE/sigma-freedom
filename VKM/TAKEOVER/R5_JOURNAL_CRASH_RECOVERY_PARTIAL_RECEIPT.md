# SIGMA VKM R5 — Journal Crash Recovery Matrix (Partial Receipt)

## Verified before shell parse failure

R5_RECOVERY_ENGINE_COMPILE=PASS

### Recovery pass 1

All six journal crash states returned RESULT=PASS and STATE_VALID=YES.

- prepared_only: ACTION=ROLLBACK_INCOMPLETE_TRANSACTION; restored generation 5.
- replay_written: ACTION=ROLLBACK_INCOMPLETE_TRANSACTION; restored generation 5.
- canonical_written: ACTION=ROLLBACK_INCOMPLETE_TRANSACTION; restored generation 5.
- generation_written: ACTION=ROLLBACK_INCOMPLETE_TRANSACTION; restored generation 5.
- lineage_written: ACTION=ROLLBACK_INCOMPLETE_TRANSACTION; restored generation 5.
- committed: ACTION=NOOP_COMMITTED; preserved generation 6.

Rollback target identities:
- canonical: ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3
- replay: 614d420b945eeac49b66312ca28871a2f3ffd644adf010eed4815ff00d24811e
- generation: 5

Committed identities:
- canonical: f06d4c897a88878640a4c96cc124c9fff980af96eaa7606b513f99781b8fba6e
- replay: ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3
- generation: 6

### Recovery pass 2 / idempotence

prepared_only IDEMPOTENT=YES
replay_written IDEMPOTENT=YES
canonical_written IDEMPOTENT=YES
generation_written IDEMPOTENT=YES
lineage_written IDEMPOTENT=YES
committed IDEMPOTENT=YES

## Execution interruption

The subsequent 'VERIFY NO HALF COMMIT SURVIVES' shell block did not complete. Bash terminated with:

command substitution: unexpected EOF while looking for matching ')'
Process completed (code 2)

Therefore this checkpoint MUST NOT be represented as a completed R5 crash-recovery matrix or as an R5 ownership takeover.

## Status

R5_JOURNAL_RECOVERY_PASS1=PASS
R5_JOURNAL_RECOVERY_IDEMPOTENCE=PASS
R5_NO_HALF_COMMIT_FINAL_ASSERT=INCOMPLETE
R5_FINAL_GATE=NOT_REACHED
R5_OWNERSHIP_TAKEOVER=NOT_AUTHORIZED

NEXT=RESUME_R5_NO_HALF_COMMIT_ASSERT_AND_FINAL_GATE
