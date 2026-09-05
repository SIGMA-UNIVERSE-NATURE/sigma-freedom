# V4-A.1 pre-runtime failure + shadow isolation correction

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`V4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT=NOT_YET_ADMITTED`

`NATIVE_PRODUCTIVITY_WORK_ARBITRATION=NOT_YET_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Production V2.4 remains running unchanged.

## Observed user transcript

The preflight printed locked SIGMAC/VM hashes correctly but printed an empty `SOURCE_SHA256`, then:

`HOLD=LOCKED_IDENTITY_MISMATCH`

This occurred before native compile/VM runtime evidence.

## Root cause 1

The first runner revision attempted to hash the V4-A source under BRAIN `.sigma_exec` before mechanically installing the pinned repository artifact there.

Correction commit:
`e24210e60cb3a6721dfcf80a9a14cfe8a868403e`

## Root cause 2 found during audit before rerun

The corrected runner still pointed its test BRAIN at the production BRAIN path. Had that revision progressed beyond the identity gate, it would have written admission fixtures/ledger/action/bytecode into production learner memory, violating shadow-isolation policy.

The observed HOLD occurred before source install or fixture mutation, so the failed user run did not mutate production learner memory.

## Mandatory isolation correction

Current V4-A admission state lives only under:

`$HOME/SIGMA/SIGMA_V4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT/shadow/BRAIN/EXTRA BRAIN_OPPO_24826/.sigma_exec`

Production BRAIN is not a test write target.

Current runner commit:
`381f6168a32ead9af7b529706d5b9cb19901aca0`

Current runner Git blob:
`c71f1248b2f2c33a7918488913661c8e5f371530`

Pinned native source SHA256 remains:
`12c32f07d39bacedf8dd1a2371f9b33801106d256d6166fed03fbaa224416ed2`

Prior runner blobs `4eb9286d...` and `6afbc9ed...` are superseded and MUST NOT be used for admission.

## Claim boundary

No V4-A capability claim may be admitted until the current isolated runner reaches locked `sigmac` + locked VM and all runtime gates PASS.

Keep:
- `HOST_WORK_SELECTION=NO`
- `HOST_STAGE_DECISION=NO`
- `HOST_RETRY_POLICY=NO`
- `HOST_LEARNING=NO`
- `PRODUCTION_LEARNER_MEMORY_MUTATED_BY_V4A_ADMISSION=NO`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
