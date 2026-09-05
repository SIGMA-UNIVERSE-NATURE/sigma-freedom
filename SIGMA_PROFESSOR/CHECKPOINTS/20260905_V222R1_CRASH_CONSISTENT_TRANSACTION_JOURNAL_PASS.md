# V2.22R.1 CRASH-CONSISTENT TRANSACTION JOURNAL — RUNTIME PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Status: ADMITTED IN EXACT TESTED DURABILITY SCOPE

## Mandatory bootstrap

All future work must first read `/AGENTS.md` and `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`.

Native capability implementation remains native `.sigma` only. Bash/host is external mechanical harness only and must not implement SIGMA cognition, recovery decisions, transaction decisions, learning, semantic interpretation, work selection, stage selection, or truth decisions.

## Candidate identity

Native source:
`SIGMA_CRASH_CONSISTENT_TRANSACTION_JOURNAL_V2_22R1.sigma`

Source SHA256:
`643c6f534777193951d772e9653463b5d97ceebb7c35f14b21390a3308ef4c64`

Admission runner:
`RUN_SIGMA_V222R1_CRASH_CONSISTENT_TRANSACTION_JOURNAL_PREFLIGHT.sh`

Runner SHA256:
`6038ba6d2a6d4a16cc67c98386227c130fdc2f659c6dd850457b5c0ce4a4be9e`

Locked runtime identities remain:

- SIGMAC SHA256 `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM v09 candidate SHA256 `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

The user-provided final tail did not include the V2.22 runtime bytecode SHA line; do not invent it.

## Runtime result

Final sentinel:

`V222R1_CRASH_CONSISTENT_TRANSACTION_JOURNAL_PREFLIGHT=PASS`

Admitted gates from the locked-VM run:

- `PREPARE_ONLY_NOT_VISIBLE_AS_COMMITTED=PASS`
- `PREPARED_TRANSACTION_RESUMES_TO_COMMIT_AFTER_RESTART=PASS`
- `TORN_PREPARE_TAIL_IGNORED=PASS`
- `TORN_PREPARE_RETRY_RECOVERS=PASS`
- `TORN_COMMIT_TAIL_IGNORED=PASS`
- `TORN_COMMIT_RETRY_RECOVERS=PASS`
- `GARBAGE_TAIL_IGNORED=PASS`
- `CONFLICTING_PREPARE_BLOCKS_TRANSACTION=PASS`
- `IDEMPOTENT_COMMIT_FRESH_VM=PASS`
- `DETERMINISTIC_JOURNAL_REPLAY=PASS`
- `INVALID_PAYLOAD_DELIMITER_REFUSAL=PASS`
- `STEP_LIMIT_STATUS=BOUNDED`

Runtime transcript also showed deterministic replay where A then B recovered B, invalid payload delimiter refusal with `STATE_MUTATION_ALLOWED NO`, and journal over-limit refusal with `JOURNAL_LIMIT_EXCEEDED 1` and no mutation admission.

## Admitted claim

`CRASH_CONSISTENT_JOURNAL_RECOVERY=PROVEN_UNDER_INJECTED_TRUNCATED_TAIL_FAULTS`

This means SIGMA native recovery accepted only structurally complete committed transactions under the tested injected-tail fault model. Prepare-only and malformed/torn tails did not become visible committed state; retry recovered cleanly.

## Non-claims that remain locked

- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`
- `PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `PRODUCTION_PROMOTION_ALLOWED=NO`

Do not reinterpret V2.22 as proof that `append_text`, fwrite, the filesystem, Android storage, or Termux writes are physically atomic.

## Host boundary

Runtime output preserved:

- `HOST_TRANSACTION_DECISION=NO`
- `HOST_RECOVERY_DECISION=NO`
- `HOST_LEARNING=NO`

Host fault injection is admission-fixture mechanics only. Native SIGMA decides what is valid/recoverable.

## Production

`PRODUCTION_LEARNER_MEMORY_MUTATED=NO`

Keep production V2.4 running unchanged unless it emits a real VM failure. Do not promote in place.

## Next action

Integrate V2.22 around the real shadow scheduler scheduled-intent path. The next gate must prove that a real fairness defer/resume event is journaled and recovered through injected torn PREPARE/COMMIT tails before exact mechanical dispatch, while all cognition/decision logic remains native SIGMA.
