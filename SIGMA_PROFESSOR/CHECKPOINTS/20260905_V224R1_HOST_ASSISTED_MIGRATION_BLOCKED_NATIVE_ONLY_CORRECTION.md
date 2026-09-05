# V2.24R.1 HOST-ASSISTED MIGRATION — BLOCKED BY NATIVE-ONLY STOP-GATE

Date: 2026-09-05
Status: BLOCKED / DO NOT ADMIT / DO NOT RUN AS PRODUCTION-MIGRATION CAPABILITY

## Trigger

A governance re-audit was performed after the user explicitly asked whether the work was still executing on SIGMA or had shifted to HOST/Bash.

## Finding

The current V2.24R.1 draft contains a native `.sigma` verifier for stability/migration/mutation/rollback decisions, but the actual migration mechanics are still materially performed by Bash/host:

- capture/canonical packaging of production state;
- tar creation/extraction;
- candidate population;
- candidate deletion/restore;
- selection of a candidate fault target;
- byte injection for rollback testing.

Under the repository-wide bootstrap STOP-GATE, this is acceptable only as an external admission fixture/harness. It is NOT sufficient to claim that SIGMA itself has a native production-state migration or rollback capability.

Therefore the previously created V2.24R.1 artifact is frozen as historical/DRAFT evidence only.

## Correction

`V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT=NOT_ADMITTED`

`V224R1_HOST_ASSISTED_BYTE_MIGRATION=DRAFT_ONLY`

`NATIVE_PRODUCTION_STATE_MIGRATION=NOT_PROVEN`

`NATIVE_PRODUCTION_STATE_ROLLBACK=NOT_PROVEN`

`CANDIDATE_STARTUP_FROM_MIGRATED_STATE=NOT_PROVEN`

`PRODUCTION_PROMOTION_ALLOWED=NO`

## Preserved admitted chain

This correction does NOT revoke V2.23 or earlier admitted claims. V2.23 remains admitted because the event/fairness/recovery decisions and recovered intent identity were produced/validated by native SIGMA, while host actions were limited to launch/fault injection/exact-byte movement.

## Next frontier

Design a native-first V2.24 replacement in which SIGMA owns the migration/rollback state machine and all admissible state-transition decisions. If the current VM/host ABI lacks a primitive required for exact filesystem-tree enumeration/copy/replace, that limitation must be exposed as a capability blocker rather than substituted by Bash logic.

Allowed host role remains mechanical only:

- invoke locked sigmac/VM;
- exact byte transport;
- hashes/return codes;
- bounded fault injection;
- process supervision;
- no migration decision, rollback decision, work selection, learning, semantic interpretation, or missing-capability substitution.

## Production

Keep V2.4 running unchanged unless a real fatal VM failure occurs.

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`UPGRADE_V2_4_IN_PLACE=NO`
