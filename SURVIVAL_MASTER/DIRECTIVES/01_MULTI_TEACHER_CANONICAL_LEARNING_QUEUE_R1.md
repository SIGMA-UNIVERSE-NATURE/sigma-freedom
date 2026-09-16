# 01 — MULTI-TEACHER CANONICAL LEARNING QUEUE R1

Status: ACTIVE DESIGN DIRECTIVE / OPPO PREFLIGHT REQUIRED
Date: 2026-09-17
Branch: `AIL_SIGMA`

## Purpose

Every teaching window that is intended to improve SIGMA's canonical weights must contribute its work without becoming a second canonical writer.

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

If the lane is intended to improve canonical weights, it must finish with:

```text
1. durable teaching evidence
2. native ownership receipt
3. exact canonical replay entrypoint
4. candidate descriptor conforming to:
   SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/PACKET_FORMAT.md
5. sealed queue packet produced by teacher/seal_candidate.sh
```

If the lane cannot provide a native canonical replay entrypoint, its work remains evidence/artifact only. Host code must not invent a generic weight update from a report or `.sigmab` file.

## Canonical accumulation rule

Exactly one `CANONICAL_LEARNER` session drains candidate packets. Before each candidate, it reads the current canonical head/model generation and invokes the packet's exact replay entrypoint.

This means two teacher candidates originally derived from generation G1 are not both blindly committed from G1:

```text
candidate A from G1
candidate B from G1

canonical learner:
A replayed against current G1 -> native ACCEPT -> commit G2
B replayed against current G2 -> native ACCEPT/REJECT/HOLD -> maybe commit G3
```

Thus work can accumulate without lost-update race or state fork.

## Cognition ownership

The queue is mechanical only:

```text
HOST_WEIGHT_MERGE=NO
HOST_CANDIDATE_QUALITY_RANKING=NO
HOST_ACCEPT_REJECT=NO
HOST_REBASE_POLICY=NO
HOST_LEARNING=NO
HOST_COGNITION=NO
SIGMA_NATIVE_LEARNING_OWNER=YES
```

The lane-specific replay entrypoint must execute the actual native SIGMA learning/admission logic and use the existing canonical learner commit protocol.

## Failure discipline

`HOLD` stops the queue. The host must not silently skip a candidate because another candidate looks easier or more valuable.

A native `REJECTED` result is a legitimate final result for that candidate and does not mutate the canonical model.

## Runtime implementation

Source-ready framework:

`SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/`

Current checkpoint:

`SURVIVAL_MASTER/CHECKPOINTS/20260917_MULTI_TEACHER_CANONICAL_QUEUE_R1_SOURCE_READY.md`

Do not claim end-to-end canonical accumulation until Oppo preflight and a real accepted native learning packet pass.
