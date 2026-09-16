# README — SIGMA MULTI-TEACHER CANONICAL QUEUE R1 FIX1

Status: corrected candidate source ready; Oppo preflight required before continuous use.

Read first:

`SURVIVAL_MASTER/CORRECTIONS/20260917_OPPO_RUNTIME_AUTHORITY_NATIVE_LEARNING_FIX1.md`

## What this solves

Many teaching windows may run at once and produce native SIGMA learning candidates. Only one session holds the canonical learner lease and commits model/state changes.

```text
many teacher windows
-> many sealed native-bound candidates
-> one canonical learner
-> replay against CURRENT Oppo model
-> native SIGMA decision
-> sequential canonical commit when accepted
```

## Critical ownership rule

The `.sh` files in this framework do not learn.

```text
BASH_ROLE=MECHANICAL_ONLY
BASH_LEARNING=NO
PYTHON_LEARNING=NO
SIGMA_NATIVE_VM_IS_LEARNING_ENGINE=YES
```

Shell may verify hashes/session state, seal/copy exact bytes, invoke a hash-bound runner, capture VM evidence, serialize one writer, and verify native receipts. It may not calculate a weight update or choose ACCEPT/REJECT/HOLD.

Every weight-affecting candidate must bind exact native `.sigma` source and `.sigmab` bytecode identities. Its semantic learning result must trace to an exact native SIGMA decision receipt.

## Oppo is runtime authority

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GIT_PULL_REQUIRED=NO
GIT_CHECKOUT_REQUIRED=NO
```

Before each replay the canonical drainer reads the CURRENT Oppo:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_ail/BRAIN_HEAD
$HOME/SIGMA/sigma_genesis1/.sigma_ail/MODEL_GENERATION
```

Do not replace these values from GitHub.

## Staging without changing Oppo repo state

Do not run `git pull`, `git checkout`, `git reset`, or branch replacement just to obtain this tool.

Transfer only the exact reviewed framework bytes into either:

```text
current session ARTIFACT_ROOT/tools/MULTI_TEACHER_CANONICAL_QUEUE_R1_FIX1
```

or another neutral non-canonical staging directory.

Then verify exact hashes/manifest before running preflight. Staging the tool must not mutate the Oppo repository checkout, canonical model, BRAIN_HEAD, MODEL_GENERATION, or writer/learner locks.

## Teacher window usage

Teacher stays `SESSION_MODE=STANDARD` with canonical mutation rejected.

After its native SIGMA teaching runner has produced:

- durable teaching evidence;
- exact native `.sigma` learning/re-evaluation source;
- exact native `.sigmab` bytecode;
- native ownership receipt binding those hashes;
- a mechanically transparent replay runner;

create the source descriptor described by `PACKET_FORMAT.md`, then run mechanically:

```bash
bash teacher/seal_candidate.sh /absolute/path/to/candidate_descriptor.env
```

Expected result:

```text
QUEUE_SEAL=PASS
CANDIDATE_ID=<content-addressed id>
PACKET=<teacher artifact path>/CANONICAL_CANDIDATE_QUEUE_OUTBOX/<id>
BASH_LEARNING=NO
```

The sealed packet is self-contained. Sealing never grants canonical write permission.

## Canonical learner usage

Exactly one shell/session must already have:

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
MODEL_GENERATION_CHANGE=ALLOW
HEAD_CHANGE=REJECT
HOST_COGNITION=NO
HOST_LEARNING=NO
```

First run the mechanical preflight from the staged tool copy:

```bash
bash verify/static_preflight.sh
```

This does not teach or update weights. It only verifies source/control boundaries and prints the current Oppo head/model generation.

Process one candidate mechanically:

```bash
bash canonical/drain_once.sh
```

Continuous mechanical serialization, only after one-candidate device proof:

```bash
bash canonical/daemon.sh
```

The daemon handles one packet per drain invocation, then re-reads current Oppo state before the next candidate.

## Replay contract

The packet-local `mechanical_replay_runner` receives:

```text
mechanical_replay_runner <descriptor.env> <attempt-root>
```

It is not allowed to make the learning decision. It must execute/capture the exact native SIGMA program bound by:

```text
native_learning.sigma
native_learning.sigmab
```

and preserve:

```text
<attempt-root>/native_decision.receipt
<attempt-root>/result.env
raw VM stdout/stderr/RC as applicable
```

`result.env` must mechanically match the exact native decision receipt. The drainer rejects any mismatch.

## Result behavior

`ACCEPTED`:

- exact native SIGMA decision receipt says ACCEPTED;
- canonical generation advances through existing native writer protocol;
- exact native commit receipt exists and hash-matches;
- queue writes a mechanical processed receipt.

`REJECTED`:

- exact native SIGMA decision receipt says REJECTED;
- current Oppo head/generation remain unchanged;
- queue records native rejection mechanically.

`HOLD`:

- exact native SIGMA decision receipt says HOLD;
- no canonical mutation occurs;
- daemon stops rather than selecting a semantic alternative.

## Crash behavior

Teacher packets become visible only after `READY` is committed. The canonical drainer uses a dedicated flock and durable per-candidate attempt/processed records.

The lane-specific native commit protocol remains responsible for canonical transaction idempotency if a crash occurs inside its own commit.

## Current claim ceiling

```text
FIX1_SOURCE_READY=YES
STATIC_PREFLIGHT_IS_LEARNING=NO
OPPO_NATIVE_REPLAY=NOT_RUN
MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN
CONTINUOUS_DAEMON=NOT_ENABLED
```
