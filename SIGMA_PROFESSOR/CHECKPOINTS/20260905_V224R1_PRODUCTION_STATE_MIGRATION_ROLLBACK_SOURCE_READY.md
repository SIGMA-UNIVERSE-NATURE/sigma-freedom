# V2.24R.1 — Production state migration + rollback — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Prior admitted milestone

V2.23R.1 journal-wrapped real shadow scheduled intent passed and was checkpointed at:

`07fc590844c6440d5d67c8719fbf15aa3f9463c3`

Admitted V2.23 claims:

`REAL_SHADOW_SCHEDULED_INTENT_JOURNAL_INTEGRATION=PROVEN_IN_DEFER_RESUME_REDEFER_SCOPE`

`CRASH_CONSISTENT_SCHEDULED_INTENT_RECOVERY=PROVEN_UNDER_INJECTED_TORN_PREPARE_COMMIT_FAULTS`

## V2.24R.1 purpose

Prove exact migration and rollback of a stable live V2.4 state package without stopping V2.4 and without any admission write target inside production state.

This R1 gate does NOT yet prove candidate startup from migrated state or supervisor cutover.

## Native source

`SIGMA_PROFESSOR/artifacts/SIGMA_PRODUCTION_STATE_MIGRATION_ROLLBACK_VERIFIER_V2_24R1.sigma`

SHA256:

`17cfd479bd0ede1e7cd8aa8d73dc58a7a94bcc74e6279bb4d6724375c2ed8057`

Source commit:

`6d1bbacade749f1e3f21db46e8378f9ad11b752a`

## Runner

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT.sh`

SHA256:

`4446dc072a7e523a7a94554856b7d548247ff5db59bfb4b540671d624fdfab0d`

Runner commit:

`efaad627b80b3c6b659766676b49714fa606b8f2`

Runner `bash -n` RC = 0.

## README

`SIGMA_PROFESSOR/artifacts/SIGMA_V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT_README.txt`

README commit:

`b059fc4e1029a8e044f87aad5f9cc8732cac8475`

## Static native audit

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`

## Declared migration package scope

The canonical package contains:

1. production BRAIN `.sigma_exec` tree;
2. `$HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2` tree;
3. operational `SIGMA_CONTINUOUS_NATIVE_V2_2/log/**` is excluded as observability output rather than learner state.

## Native decision protocol

The host captures canonical package bytes and hashes them mechanically. Native V2.24 decides whether:

- source BEFORE / SNAPSHOT / AFTER are stable by exact digest + entry-count equality;
- migrated candidate exactly matches the accepted snapshot;
- injected candidate drift is detected;
- rollback exactly matches the immutable baseline.

No host migration or rollback decision is admitted.

## Required gates

- locked SIGMAC and VM equality gates;
- production V2.4 source equality gate;
- production V2.4 PID present before test;
- stable live source snapshot confirmed natively within bounded attempts;
- production not stopped for snapshot;
- exact candidate migration verified natively;
- deliberate wrong candidate digest refused natively;
- candidate-only fault detected natively;
- immutable-baseline rollback verified natively;
- same V2.4 PID after test;
- no production admission write target;
- host migration/rollback/learning decisions all NO.

## Claim boundary after a future PASS

May admit only:

`LIVE_PRODUCTION_STATE_SNAPSHOT=PROVEN_IN_DECLARED_PACKAGE_SCOPE`

`SHADOW_STATE_MIGRATION_BYTE_IDENTITY=PROVEN_IN_DECLARED_PACKAGE_SCOPE`

`SHADOW_ROLLBACK_BYTE_IDENTITY=PROVEN_AFTER_INJECTED_CANDIDATE_FAULT`

Must still keep:

`CANDIDATE_STARTUP_FROM_MIGRATED_STATE=NOT_PROVEN`

`PRODUCTION_PROMOTION_ALLOWED=NO`

`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

`PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED`

`BOUNDED_FILE_IO=NOT_PROVEN`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

## Next action after PASS

Prove candidate startup from migrated state and reversible supervisor cutover/rollback while production V2.4 remains protected until the cutover gate itself explicitly authorizes transition.
