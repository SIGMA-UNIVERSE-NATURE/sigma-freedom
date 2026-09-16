# 01 — MULTI-TEACHER CANONICAL LEARNING QUEUE R1

Status: ACTIVE DESIGN DIRECTIVE / FIX1 CORRECTED / OPPO PREFLIGHT REQUIRED
Date: 2026-09-17
Branch: `AIL_SIGMA`

Read first:

`SURVIVAL_MASTER/CORRECTIONS/20260917_OPPO_RUNTIME_AUTHORITY_NATIVE_LEARNING_FIX1.md`

## Purpose

Every teaching window intended to improve SIGMA's canonical weights must contribute its work without becoming a second canonical writer.

Required architecture:

```text
MULTI_TEACHER_WINDOWS=YES
TEACHER_WINDOWS_CAN_RUN_NATIVE_SIGMA_LEARNING=YES
TEACHER_WINDOWS_CAN_PRODUCE_WEIGHT_CANDIDATES=YES
TEACHER_CANONICAL_WRITE=NO
CANONICAL_CANDIDATE_QUEUE=YES
ONE_CANONICAL_LEARNER=YES
CANONICAL_NATIVE_REPLAY_AND_DECISION=YES
CANONICAL_WEIGHT_UPGRADE=YES
ONE_CANONICAL_WRITER_AT_A_TIME=YES
```

## Runtime authority

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GIT_PULL_REQUIRED_FOR_RUNTIME=NO
GIT_CHECKOUT_REQUIRED_FOR_RUNTIME=NO
```

The canonical learner must read the CURRENT Oppo `BRAIN_HEAD` and `MODEL_GENERATION` immediately before each replay. A GitHub branch/commit may document source identity; it may not replace or override the current Oppo canonical runtime state.

## Rule for future teaching windows

Do NOT ask for a canonical learner lease merely because your lane produces a learned candidate.

Stay in ordinary artifact-only mode while teaching/testing:

```text
SESSION_MODE=STANDARD
READ=ALLOW
ARTIFACT_WRITE=ALLOW
BRAIN_WRITE=REJECT
STATE_WRITE=REJECT
MODEL_WRITE=REJECT
LEARN=REJECT
COMMIT=REJECT
HEAD_CHANGE=REJECT
MODEL_GENERATION_CHANGE=REJECT
```

Native SIGMA may still execute the teaching computation and produce candidate artifacts. The restriction is only against committing those artifacts into the single canonical model from that teacher session.

## Required output of a weight-affecting teaching lane

A lane intended to affect canonical weights must finish with:

```text
1. durable teaching evidence
2. exact native .sigma source identity
3. exact native bytecode identity
4. native ownership receipt
5. exact MECHANICAL replay runner identity
6. candidate descriptor conforming to:
   SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/PACKET_FORMAT.md
7. sealed queue packet produced mechanically by teacher/seal_candidate.sh
```

The replay runner is not the learner. It may only launch/transport/hash/capture the exact native SIGMA computation. If a lane cannot provide an exact native learning/re-evaluation path, its work remains evidence/artifact only.

## Canonical accumulation rule

Exactly one `CANONICAL_LEARNER` session drains candidate packets. Before each candidate it reads the current Oppo canonical head/model generation, verifies the exact native source/bytecode and mechanical runner identities, then invokes the lane-specific mechanical replay runner.

The runner must execute native SIGMA learning/admission against the current canonical model and preserve an exact native decision receipt.

Example:

```text
candidate A originally from G1
candidate B originally from G1

canonical learner:
A native replay against CURRENT G1 -> SIGMA native ACCEPT -> commit G2
B native replay against CURRENT G2 -> SIGMA native ACCEPT/REJECT/HOLD -> maybe commit G3
```

Thus work can accumulate without lost-update race or state fork.

## Cognition ownership

```text
SIGMA_NATIVE_VM_IS_LEARNING_ENGINE=YES
HOST_WEIGHT_MERGE=NO
HOST_CANDIDATE_QUALITY_RANKING=NO
HOST_ACCEPT_REJECT=NO
HOST_REBASE_POLICY=NO
HOST_LEARNING=NO
HOST_COGNITION=NO
SIGMA_NATIVE_LEARNING_OWNER=YES
```

Bash/Python may verify, launch, serialize, hash, persist, and recover. They may not derive a weight update, choose a learning result, rewrite a native decision, or select a semantic alternative.

A queue result `ACCEPTED|REJECTED|HOLD` must byte-bind to an exact native SIGMA decision receipt from the replayed native program.

## Mechanical queue ordering

If multiple READY packets exist, the queue may serialize them using a deterministic content-addressed mechanical order only. This is not a semantic ranking and must not be claimed as curriculum selection. Every candidate is re-evaluated natively against the current model before any commit.

`HOLD` stops the queue. The host must not skip to another candidate because it looks easier or more valuable.

A native `REJECTED` result is a legitimate final result and performs no canonical mutation.

## Staging on Oppo

Do not require `git pull`, branch checkout, reset, or replacement of the Oppo runtime tree.

Transfer only the exact reviewed queue/tool bytes into a neutral staging location or current session artifact root, verify hashes, and run preflight against the existing Oppo runtime.

## Runtime implementation

Corrected framework path:

`SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/`

Current corrected checkpoint must supersede the original source-ready checkpoint before deployment.

Do not claim end-to-end canonical accumulation until Oppo preflight and at least one real native accepted learning packet pass.