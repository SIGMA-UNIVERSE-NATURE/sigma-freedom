# SURVIVAL MASTER CHECKPOINT — MULTI-TEACHER CANONICAL QUEUE R1 FIX1 SOURCE READY

Date: 2026-09-17 (Asia/Ho_Chi_Minh)
Branch: `AIL_SIGMA`
Status: FIX1 SOURCE READY / OPPO PREFLIGHT NOT RUN

Supersedes for deployment:

`SURVIVAL_MASTER/CHECKPOINTS/20260917_MULTI_TEACHER_CANONICAL_QUEUE_R1_SOURCE_READY.md`

Mandatory correction:

`SURVIVAL_MASTER/CORRECTIONS/20260917_OPPO_RUNTIME_AUTHORITY_NATIVE_LEARNING_FIX1.md`

## User requirement preserved

```text
MULTI_TEACHER_WINDOWS=YES
MULTI_CANDIDATE_LEARNING=YES
CANONICAL_WEIGHT_UPGRADE=YES
ONE_CANONICAL_WRITER_AT_A_TIME=YES
TWO_CANONICAL_WRITERS=NO
NO_STATE_FORK=MANDATORY
```

## Corrected runtime authority

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GITHUB_MUST_NOT_REPLACE_OPPO_BRAIN_HEAD=YES
GIT_PULL_REQUIRED_FOR_RUNTIME=NO
GIT_CHECKOUT_REQUIRED_FOR_RUNTIME=NO
RUNTIME_REPO_MUTATION_FOR_STAGING=NO
```

The canonical drainer must read current Oppo `BRAIN_HEAD` and `MODEL_GENERATION` immediately before every candidate replay.

## Corrected learning ownership

```text
SIGMA_NATIVE_VM_IS_LEARNING_ENGINE=YES
SIGMA_NATIVE_LEARNING_OWNER=YES
BASH_LEARNING=NO
PYTHON_LEARNING=NO
HOST_LEARNING=NO
HOST_WEIGHT_UPDATE=NO
HOST_WEIGHT_MERGE=NO
HOST_ACCEPT_REJECT=NO
```

Every weight-affecting candidate now binds:

```text
exact native .sigma source
exact native .sigmab bytecode
exact teaching evidence
exact mechanical replay runner
exact native ownership receipt
```

The packet schema is now `SIGMA_MULTI_TEACHER_WEIGHT_CANDIDATE_R2`.

The semantic queue result must bind to an exact native SIGMA decision receipt:

```text
SCHEMA=SIGMA_NATIVE_CANONICAL_LEARNING_DECISION_R1
QUEUE_RESULT=ACCEPTED|REJECTED|HOLD
```

The shell drainer rejects any `result.env` whose result differs from the native decision receipt.

## Self-contained packets

Teacher sealing now copies the exact verified evidence/source/bytecode/runner/ownership bytes into the READY packet. Canonical replay therefore does not depend on the original teacher process remaining alive.

## Corrected source paths

```text
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/CONTRACT.md
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/PACKET_FORMAT.md
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/README_RUN.md
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/teacher/seal_candidate.sh
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/canonical/drain_once.sh
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/canonical/daemon.sh
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/verify/static_preflight.sh
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/samples/CANDIDATE_DESCRIPTOR.template
```

## Preflight meaning

`verify/static_preflight.sh` is mechanical only. It may verify shell syntax, forbidden mutation patterns, queue ownership declarations, and print current Oppo head/generation.

```text
STATIC_PREFLIGHT_IS_LEARNING=NO
STATIC_PREFLIGHT_CAN_UPDATE_WEIGHTS=NO
NATIVE_REPLAY_REQUIRED_FOR_WEIGHT_UPDATE=YES
```

## Current live runtime evidence last supplied by human

```text
SESSION_CODE=SBE0DAD2082DF
SESSION_MODE=CANONICAL_LEARNER
ONE_WRITER=YES
BRAIN_WRITE=ALLOW
BRAIN_WRITE_OWNER=SIGMA_NATIVE_VM_ONLY
BRAIN_WRITE_NATIVE_RECEIPT_REQUIRED=YES
STATE_WRITE=ALLOW
MODEL_WRITE=ALLOW
LEARN=ALLOW
COMMIT=ALLOW
HEAD_CHANGE=REJECT
MODEL_GENERATION_CHANGE=ALLOW
AUTHORIZED_HEAD=700d5c1b4845322d7c14800029c629b0
AUTHORIZED_MODEL_GENERATION=1
```

This is historical machine evidence. Recheck Oppo before deployment.

## Claim ceiling

```text
FIX1_SOURCE_READY=YES
OPPO_PREFLIGHT_AFTER_FIX1=NOT_RUN
REAL_NATIVE_CANDIDATE_REPLAY=NOT_RUN
REAL_NATIVE_ACCEPTED_WEIGHT_UPDATE=NOT_RUN
CONTINUOUS_DAEMON=NOT_ENABLED
MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN
```

## Next action

Transfer only the exact corrected framework bytes to a neutral Oppo staging location or current session artifact root WITHOUT git pull/checkout. Verify exact hashes. Run mechanical preflight. Then test one native no-mutation REJECTED/HOLD packet before any real ACCEPTED weight update.