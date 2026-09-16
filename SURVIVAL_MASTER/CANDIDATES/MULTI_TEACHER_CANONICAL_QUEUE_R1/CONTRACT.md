# SIGMA MULTI-TEACHER CANONICAL QUEUE R1 — CONTRACT

Status: CANDIDATE / STATIC SOURCE READY / OPPO PREFLIGHT REQUIRED
Date: 2026-09-17
Branch: `AIL_SIGMA`

## Goal

Allow many SIGMA teaching windows to work in parallel while preserving one canonical model lineage and exactly one canonical writer.

```text
MULTI_TEACHER_WINDOWS=YES
MULTI_CANDIDATE_LEARNING=YES
CANONICAL_WEIGHT_UPGRADE=YES
ONE_CANONICAL_WRITER_AT_A_TIME=YES
TWO_CANONICAL_WRITERS=NO
NO_STATE_FORK=MANDATORY
```

Teacher windows remain ordinary artifact-only sessions. They may execute native SIGMA learning/evaluation and produce a sealed candidate packet, but they do not mutate the canonical model.

One `CANONICAL_LEARNER` session drains sealed packets one at a time. For every packet it re-invokes the exact lane-specific canonical replay entrypoint under the current canonical head/model generation. That replay entrypoint — not the queue host — must run the native SIGMA learning/admission logic and perform any canonical commit through the existing canonical-learner protocol.

## Required chain

```text
TEACHER WINDOW A --native SIGMA--> sealed candidate A --\
TEACHER WINDOW B --native SIGMA--> sealed candidate B ----> mechanical queue
TEACHER WINDOW C --native SIGMA--> sealed candidate C --/

mechanical queue
-> ONE canonical learner session
-> exact candidate replay entrypoint
-> SIGMA native re-evaluates against CURRENT canonical model
-> SIGMA native ACCEPT / REJECT / HOLD
-> if ACCEPT: existing canonical commit protocol
-> verified new HEAD/model generation
-> next candidate
```

A candidate derived from an older generation is NEVER blindly applied. The canonical replay entrypoint receives the current head/generation and must recompute/re-evaluate the candidate under native SIGMA before any commit.

## Cognition boundary

```text
SIGMA_NATIVE_LEARNING_OWNER=YES
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_TEST_ORACLE=NO_FOR_SEMANTIC_VERDICT
HOST_CANDIDATE_QUALITY_RANKING=NO
HOST_ACCEPT_REJECT=NO
HOST_WEIGHT_MERGE=NO
HOST_REBASE_POLICY=NO
```

The host may only:

```text
verify session mode/permissions
verify hashes and paths
seal a packet in the teacher's own artifact root
mechanically enumerate READY packets
serialize replay execution with flock
invoke the exact hash-bound replay entrypoint
capture stdout/stderr/RC
verify exact result fields and receipt hashes
mark an already-native ACCEPT/REJECT as processed
sleep/restart the mechanical daemon
```

The host must not create a weight delta, merge two deltas, choose a semantic winner, reinterpret a HOLD, or modify `BRAIN_HEAD`, `MODEL_GENERATION`, `WRITER.lock`, or the canonical model directly.

## Teacher session policy

Required when sealing a packet:

```text
SESSION_MODE=STANDARD
ACCESS=READ_PLUS_ARTIFACT_WRITE
BRAIN_WRITE=REJECT
STATE_WRITE=REJECT
MODEL_WRITE=REJECT
LEARN=REJECT
COMMIT=REJECT
HEAD_CHANGE=REJECT
MODEL_GENERATION_CHANGE=REJECT
HOST_COGNITION=NO
HOST_LEARNING=NO
```

The teaching computation may still execute native SIGMA and produce artifacts/candidate state. It simply cannot commit canonical mutation from that session.

## Canonical drainer policy

Required before drain:

```text
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
HOST_COGNITION=NO
HOST_LEARNING=NO
```

`HEAD_CHANGE=REJECT` remains intentional. A native canonical commit may advance model generation and produce a new canonical brain/model state only through the admitted writer protocol; no shell script may manually rewrite the head pointer.

## Candidate replay entrypoint

Every queued item must bind one exact executable replay entrypoint by SHA256. The entrypoint is lane-specific and must already know how to rerun that teaching/weight-upgrade computation against the current canonical model. It must preserve:

```text
SIGMA_NATIVE_LEARNING_OWNER=YES
HOST_COGNITION=NO
HOST_LEARNING=NO
ONE_WRITER=YES
```

The queue framework does not invent a generic weight merge algorithm.

## Result contract

The replay entrypoint writes `$SIGMA_QUEUE_ATTEMPT_ROOT/result.env`.

Allowed terminal results:

```text
QUEUE_RESULT=ACCEPTED
QUEUE_RESULT=REJECTED
QUEUE_RESULT=HOLD
```

For `ACCEPTED`, required fields include before/after head and model generation, native commit receipt path/hash, and `CANONICAL_MUTATION_OBSERVED=YES`.

For `REJECTED`, `CANONICAL_MUTATION_OBSERVED=NO` is required.

For `HOLD`, the packet remains unprocessed and may be retried only through the same exact replay entrypoint; the host may not substitute another learning strategy.

## Survival behavior

All packets are content-addressed and sealed with atomic rename + `READY`. Processed receipts are durable. A crash before processed receipt causes the same packet to be re-verified. The replay entrypoint itself remains responsible for canonical commit idempotency/recovery under its native learning contract.

```text
TASK_NEVER_LOSES_COMMITTED_PROGRESS=TARGET
PROCESS_NEVER_DIES=NOT_CLAIMED
RECOVERY_REPLAYS_MECHANICS_NOT_COGNITION=YES
```

## Current claim ceiling

```text
QUEUE_MECHANICS_SOURCE_READY=YES
OPPO_PREFLIGHT=NOT_RUN
MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN_UNTIL_DEVICE_TEST
GENERAL_WEIGHT_DELTA_MERGE=NOT_IMPLEMENTED
MULTI_WRITER_CANONICAL_COMMIT=FORBIDDEN
```
