# SIGMA MULTI-TEACHER CANONICAL QUEUE R1 — CONTRACT FIX1

Status: CANDIDATE / FIX1 SOURCE READY / OPPO PREFLIGHT REQUIRED
Date: 2026-09-17
Branch: `AIL_SIGMA`

Read first:

`SURVIVAL_MASTER/CORRECTIONS/20260917_OPPO_RUNTIME_AUTHORITY_NATIVE_LEARNING_FIX1.md`

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

Teacher windows remain ordinary artifact-only sessions. They may run native SIGMA learning/evaluation and produce sealed candidate packets, but they do not mutate the canonical model.

One `CANONICAL_LEARNER` session drains sealed packets one at a time. For every packet it uses the CURRENT Oppo canonical head/model generation and invokes a hash-bound mechanical replay runner whose only purpose is to launch/capture the packet's exact native SIGMA learning program.

## Runtime authority

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
RUNTIME_HEAD_FILE=$HOME/SIGMA/sigma_genesis1/.sigma_ail/BRAIN_HEAD
RUNTIME_MODEL_GENERATION_FILE=$HOME/SIGMA/sigma_genesis1/.sigma_ail/MODEL_GENERATION
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GIT_PULL_REQUIRED_FOR_RUNTIME=NO
GIT_CHECKOUT_REQUIRED_FOR_RUNTIME=NO
```

The queue must never compare Oppo against a GitHub HEAD to decide whether current canonical state is valid. GitHub commit identities are source/provenance references only.

## Required chain

```text
TEACHER WINDOW A --native SIGMA--> sealed candidate A --\
TEACHER WINDOW B --native SIGMA--> sealed candidate B ----> mechanical queue
TEACHER WINDOW C --native SIGMA--> sealed candidate C --/

mechanical queue
-> ONE canonical learner session
-> read CURRENT Oppo head/model generation
-> verify exact candidate native .sigma + bytecode + mechanical runner hashes
-> mechanical runner launches exact native SIGMA program
-> SIGMA native re-evaluates against CURRENT canonical model
-> SIGMA native emits ACCEPT / REJECT / HOLD decision receipt
-> host verifies exact native receipt bytes only
-> if ACCEPT: existing native canonical commit protocol
-> verify resulting current Oppo generation/receipts
-> next candidate
```

A candidate derived from an older generation is NEVER blindly applied.

## Cognition boundary

```text
SIGMA_NATIVE_VM_IS_LEARNING_ENGINE=YES
SIGMA_NATIVE_LEARNING_OWNER=YES
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_TEST_ORACLE=NO_FOR_SEMANTIC_VERDICT
HOST_CANDIDATE_QUALITY_RANKING=NO
HOST_ACCEPT_REJECT=NO
HOST_WEIGHT_MERGE=NO
HOST_REBASE_POLICY=NO
BASH_LEARNING=NO
PYTHON_LEARNING=NO
```

The host may only:

```text
verify session mode/permissions
read current Oppo head/model generation
verify hashes and paths
seal exact candidate bytes
mechanically enumerate READY packets
serialize replay execution with flock
invoke the exact hash-bound mechanical replay runner
capture stdout/stderr/RC
verify exact native result/commit receipts and hashes
mark an already-native ACCEPT/REJECT as processed
sleep/restart the mechanical daemon
```

The host must not create a weight delta, merge two deltas, choose a semantic winner, reinterpret a HOLD, or directly modify `BRAIN_HEAD`, `MODEL_GENERATION`, `WRITER.lock`, learner lease, or canonical model bytes.

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

Native SIGMA may execute the teaching computation and produce candidate artifacts in the teacher workspace. It simply cannot commit canonical mutation from that session.

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

`HEAD_CHANGE=REJECT` remains intentional: shell/host may not directly change the head pointer. Any canonical state transition must occur through the admitted native writer protocol.

## Candidate packet requirements

Every queued item must bind exact identities for:

```text
TEACHING_EVIDENCE
NATIVE_LEARNING_SOURCE=.sigma
NATIVE_LEARNING_BYTECODE=.sigmab
MECHANICAL_REPLAY_RUNNER
NATIVE_OWNERSHIP_RECEIPT
```

The runner is not the learner. It must mechanically execute the native program and preserve raw VM evidence plus the native decision receipt.

The queue framework does not invent a generic weight merge algorithm.

## Result contract

The replay path writes `$SIGMA_QUEUE_ATTEMPT_ROOT/result.env`, but the semantic `QUEUE_RESULT` must byte-bind to an exact native SIGMA decision receipt.

Allowed terminal results:

```text
QUEUE_RESULT=ACCEPTED
QUEUE_RESULT=REJECTED
QUEUE_RESULT=HOLD
```

For `ACCEPTED`, required evidence includes native decision receipt, current-before/current-after Oppo runtime identities, model-generation advance, and exact native commit receipt.

For `REJECTED`, native decision receipt must say REJECTED and no canonical mutation may occur.

For `HOLD`, native decision receipt must say HOLD, no canonical mutation may occur, and the mechanical daemon stops instead of selecting an alternative.

## Mechanical ordering

READY packets may be serialized in deterministic content-addressed order. This is mechanical ordering only, not a semantic ranking or curriculum claim. Each packet is natively re-evaluated against the current canonical state.

## Survival behavior

Packets are self-contained and content-addressed. Processed receipts are durable. A crash before processed receipt causes the same packet to be re-verified. The lane-specific native commit protocol remains responsible for canonical transaction idempotency/recovery.

```text
TASK_NEVER_LOSES_COMMITTED_PROGRESS=TARGET
PROCESS_NEVER_DIES=NOT_CLAIMED
RECOVERY_REPLAYS_MECHANICS_NOT_COGNITION=YES
```

## Oppo staging

Do not `git pull` or `git checkout` merely to stage this queue. Transfer only exact reviewed bytes into a neutral staging directory or current session artifact root and verify their manifest/hash against the reviewed source package.

## Current claim ceiling

```text
QUEUE_FIX1_SOURCE_READY=YES
OPPO_PREFLIGHT=NOT_RUN
MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN_UNTIL_DEVICE_TEST
GENERAL_WEIGHT_DELTA_MERGE=NOT_IMPLEMENTED
MULTI_WRITER_CANONICAL_COMMIT=FORBIDDEN
```