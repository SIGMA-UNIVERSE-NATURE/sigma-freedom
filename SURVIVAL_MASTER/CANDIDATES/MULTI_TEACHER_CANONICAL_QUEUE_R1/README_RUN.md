# README — SIGMA MULTI-TEACHER CANONICAL QUEUE R1

Status: candidate source ready; Oppo preflight required before continuous use.

## What this solves

Many teaching windows may run at once and produce native SIGMA learning candidates. Only one session holds the canonical learner lease and commits model/state changes. Therefore teacher work is not thrown away, but two writers never race on the canonical model.

```text
many teacher windows -> many sealed candidates -> one canonical learner -> sequential native replay/commit
```

## Important limitation

This framework does not manufacture a generic weight-update algorithm. Every teaching lane that wants canonical accumulation must provide an exact `CANONICAL_REPLAY_ENTRYPOINT` capable of replaying/re-evaluating that lane's native SIGMA learning against the current canonical model under the canonical learner session.

A teacher that only produced an arbitrary `.sigmab` or report, with no native weight-learning replay path, cannot be converted into canonical weight learning by the host.

## Install/stage for preflight

Do not overwrite Session R4 coordinator files. Stage this directory read-only or copy it into a dedicated runtime tool location after hash review.

Recommended runtime tool path:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/tools/MULTI_TEACHER_CANONICAL_QUEUE_R1
```

The queue code must not edit `BRAIN_HEAD`, `MODEL_GENERATION`, `WRITER.lock`, or learner lease files.

## Teacher window usage

The teacher window stays `SESSION_MODE=STANDARD` with canonical mutation rejected.

After its native SIGMA teaching runner has produced:

- durable teaching evidence;
- exact native ownership receipt;
- an executable canonical replay entrypoint;

create the descriptor described by `PACKET_FORMAT.md`, then run:

```bash
bash teacher/seal_candidate.sh /absolute/path/to/candidate_descriptor.env
```

Expected terminal result:

```text
QUEUE_SEAL=PASS
CANDIDATE_ID=<sha256 of descriptor>
PACKET=<teacher artifact path>/CANONICAL_CANDIDATE_QUEUE_OUTBOX/<id>
```

Sealing never grants canonical write permission.

## Canonical learner usage

Exactly one shell/session must already have:

```text
SESSION_MODE=CANONICAL_LEARNER
ONE_WRITER=YES
BRAIN_WRITE=ALLOW
BRAIN_WRITE_OWNER=SIGMA_NATIVE_VM_ONLY
STATE_WRITE=ALLOW
MODEL_WRITE=ALLOW
LEARN=ALLOW
COMMIT=ALLOW
MODEL_GENERATION_CHANGE=ALLOW
HEAD_CHANGE=REJECT
```

Process one candidate:

```bash
bash canonical/drain_once.sh
```

Continuous mechanical drain:

```bash
bash canonical/daemon.sh
```

The daemon handles exactly one candidate per drain invocation, then re-reads current canonical state before the next candidate.

If any packet returns `HOLD`, the daemon stops rather than silently skipping to a different learning candidate.

## Replay entrypoint contract

The replay entrypoint receives:

```bash
replay_entrypoint.sh <descriptor.env> <attempt-root>
```

and environment variables documented in `PACKET_FORMAT.md`.

It must run the lane's native SIGMA learning/admission logic against `SIGMA_QUEUE_CURRENT_HEAD` / `SIGMA_QUEUE_CURRENT_MODEL_GENERATION` and write `<attempt-root>/result.env`.

It must use the existing canonical learner protocol for any commit/model generation advance. It must not manually edit canonical head/generation or writer locks.

## Result behavior

`ACCEPTED`:

- native SIGMA accepted the replayed learning update;
- canonical generation must advance;
- exact native commit receipt must exist and hash-match;
- drainer writes a durable processed receipt.

`REJECTED`:

- native SIGMA rejected it;
- canonical head/generation must remain unchanged;
- drainer records the candidate as natively rejected.

`HOLD`:

- no canonical mutation may be observed;
- candidate remains pending;
- daemon stops for diagnosis.

## Crash behavior

Teacher packets become visible only after `READY` is atomically committed. The canonical drainer uses a dedicated flock and durable per-candidate attempt/processed records.

The lane-specific replay entrypoint remains responsible for commit idempotency if a crash occurs inside its own canonical transaction.

## What future teaching windows should do

A teaching bundle that is intended to improve canonical weights should ship its own replay entrypoint and ownership receipt producer. It should not request a second canonical learner lease.

Target architecture:

```text
MULTI_TEACHER_WINDOWS=YES
TEACHER_WINDOWS_CAN_GENERATE_WEIGHT_CANDIDATES=YES
TEACHER_CANONICAL_WRITE=NO
CANONICAL_REPLAY_AND_NATIVE_DECISION=YES
CANONICAL_WEIGHT_UPGRADE=YES
ONE_CANONICAL_WRITER_AT_A_TIME=YES
```
