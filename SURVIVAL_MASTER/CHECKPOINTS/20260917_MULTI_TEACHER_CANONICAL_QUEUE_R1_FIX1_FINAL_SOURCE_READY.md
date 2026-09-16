# SURVIVAL MASTER CHECKPOINT — MULTI-TEACHER CANONICAL QUEUE R1 FIX1 FINAL SOURCE READY

Date: 2026-09-17 (Asia/Ho_Chi_Minh)
Branch: `AIL_SIGMA`
Status: CORRECTED SOURCE READY / OPPO PREFLIGHT NOT RUN

Supersedes for deployment:

- `20260917_MULTI_TEACHER_CANONICAL_QUEUE_R1_SOURCE_READY.md`
- `20260917_MULTI_TEACHER_CANONICAL_QUEUE_R1_FIX1_SOURCE_READY.md`

Mandatory correction:

`SURVIVAL_MASTER/CORRECTIONS/20260917_OPPO_RUNTIME_AUTHORITY_NATIVE_LEARNING_FIX1.md`

## Final architecture

```text
MULTI_TEACHER_WINDOWS=YES
MULTI_CANDIDATE_LEARNING=YES
TEACHER_CANONICAL_WRITE=NO
ONE_CANONICAL_LEARNER=YES
CANONICAL_WEIGHT_UPGRADE=YES
ONE_CANONICAL_WRITER_AT_A_TIME=YES
TWO_CANONICAL_WRITERS=NO
NO_STATE_FORK=MANDATORY
```

## Runtime authority

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GITHUB_MUST_NOT_REPLACE_OPPO_BRAIN_HEAD=YES
GIT_PULL_REQUIRED_FOR_RUNTIME=NO
GIT_CHECKOUT_REQUIRED_FOR_RUNTIME=NO
RUNTIME_REPO_MUTATION_FOR_STAGING=NO
```

## Learning ownership

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

A shell script may stage, verify, serialize, launch, capture and recover exact work. It is never the learner.

## Corrected packet contract

Packet schema:

```text
SCHEMA=SIGMA_MULTI_TEACHER_WEIGHT_CANDIDATE_R2
```

Every candidate is self-contained and binds exact:

```text
teaching evidence
native .sigma learning source
native .sigmab bytecode
mechanical replay runner
native ownership receipt
locked SIGMAC identity
locked VM identity
```

The ownership receipt must bind source hash, bytecode hash, runner hash, SIGMAC hash and VM hash.

## Native decision binding

Every replay must preserve:

```text
SCHEMA=SIGMA_NATIVE_CANONICAL_LEARNING_DECISION_R1
QUEUE_RESULT=ACCEPTED|REJECTED|HOLD
```

The mechanical result wrapper is rejected if its result differs from the exact native decision receipt.

`ACCEPTED` additionally requires a real model-generation advance and exact native commit receipt.

`REJECTED` / `HOLD` require no canonical mutation.

## Current-model replay

Before every replay the drainer reads the CURRENT Oppo:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_ail/BRAIN_HEAD
$HOME/SIGMA/sigma_genesis1/.sigma_ail/MODEL_GENERATION
```

A stale candidate is not blindly applied. Native SIGMA re-evaluates against the current model.

## Corrected files

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

No-git staging guide:

`SURVIVAL_MASTER/SAMPLES/OPPO_NO_GIT_STAGING_R1.md`

## Locked runtime identities

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Both are equality-gated by the corrected drainer/preflight before replay.

## Last human-supplied live canonical learner evidence

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

This is historical evidence only; recheck current Oppo status before use.

## Claim ceiling

```text
FIX1_FINAL_SOURCE_READY=YES
STATIC_PREFLIGHT_IS_LEARNING=NO
OPPO_PREFLIGHT_AFTER_FIX1=NOT_RUN
REAL_NATIVE_CANDIDATE_REPLAY=NOT_RUN
REAL_NATIVE_ACCEPTED_WEIGHT_UPDATE=NOT_RUN
CONTINUOUS_DAEMON=NOT_ENABLED
MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN
```

## Next action

Do not git-pull the Oppo runtime. First produce/transfer one small exact FIX1 bundle, verify manifest in the current canonical learner's artifact staging area, run `verify/static_preflight.sh`, then run one no-mutation native REJECTED/HOLD packet before any real ACCEPTED weight update.