# OFFLINE WINDOW -> SYNCHRONIZATION WINDOW PUBLISH CONTRACT R1

Status: MANDATORY HANDOFF CONTRACT
Branch: `SIGMA_LIFE`

## Purpose

The offline knowledge/capability window may advance beyond the synchronization baseline, but the synchronization window may only ingest new state from exact published machine evidence.

Chat narration alone is not a synchronization source.

## Required publication for every new offline PASS or invalidation

For each T-stage / R-stage that changes synchronization-relevant capability state, publish an immutable checkpoint containing at minimum:

```text
STAGE=<Tn/Rn exact name>
RESULT=<PASS/FAIL exact tested scope>
SOURCE_SHA256=<exact if source exists>
BYTECODE_SHA256=<exact if bytecode exists>
RUNNER_SHA256=<exact when applicable>
DEPENDENCY_IDENTITIES=<exact>
VM_INVOCATIONS=<exact>
POST_VM_ALIGNMENT=<exact>
NEGATIVE_COUNTERFACTUAL_GATES=<exact>
SOURCE_BYTECODE_INVARIANCE=<PASS/FAIL>
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_MUTATION=NO
PRODUCTION_BINDING=NO
CLAIM_LEQ_MACHINE_EVIDENCE=PASS
```

If a prior PASS is invalidated or superseded, say so explicitly and preserve the old result as historical evidence.

## Publication location

Preferred canonical branch for handoff is `SIGMA_LIFE`.

If the offline window uses a separate handoff branch, publish:

```text
HANDOFF_BRANCH=<branch>
HANDOFF_HEAD=<commit>
CHECKPOINT_PATH=<path>
CHECKPOINT_BLOB_OR_SHA=<exact>
```

The synchronization window will fetch that exact checkpoint and then write/reconcile the canonical state on `SIGMA_LIFE`.

## T7-T10 current note

At the time this contract was created, the synchronization window could not find published `T7`, `T8`, `T9`, or `T10` checkpoints/commits in the connected GitHub repository.

Therefore:

```text
OFFLINE_WINDOW_REPORTED_PROGRESS_TO_T10=YES_BY_USER_REPORT
T7_TO_T10_CANONICAL_SYNC=BLOCKED_UNTIL_EXACT_GITHUB_CHECKPOINTS_EXIST
```

Do not silently synchronize T7-T10 from chat summaries.

## Ownership split

```text
OFFLINE_WINDOW:
  explores new knowledge/capabilities
  runs machine tests
  publishes immutable checkpoints
  does not synchronize production

SYNC_WINDOW:
  reads exact published checkpoints
  reconciles canonical baseline
  never reruns already-admitted stages without damage evidence
  never imports test cognition/results as knowledge

ONLINE_WINDOW:
  tests whether synchronized capabilities are actually visible/used/learned from
  does not add new capability state
  does not bind production
```

## Non-negotiable synchronization rule

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
TEST_KNOWLEDGE_IMPORTED=NO
PRODUCTION_KNOWLEDGE_IMPORTED=NO
```

A new offline PASS may advance the canonical synchronization baseline only after its exact machine evidence is published and reconciled.
