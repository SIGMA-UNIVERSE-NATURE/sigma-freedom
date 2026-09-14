# ONE SIGMA.AIL Brain Coordinator R1

Deterministic coordination/commit-authority layer for `.sigma_ail`.

## Invariants

- `ONE_SIGMA_AIL=YES`
- `ONE_WRITER=YES`
- `UNREGISTERED_WRITER=REJECT`
- `STALE_HEAD_WRITER=REJECT`
- `CONFLICTING_LEASE=REJECT`
- `HOST_COGNITION=NO`
- `NO_STATE_FORK=MANDATORY`

The coordinator does not perform cognition, learning, semantic ranking, tool selection, or model training. It authorizes one writer at a time and advances only the canonical coordination HEAD/model-generation pointer after a registered run reports evidence.

## Required worker registration fields

`WORKER_ID`, `RUN_ID`, `TASK`, `GENERATION_LANE`, `PARENT_BRAIN_HEAD`, `MODEL_GENERATION`, `ACCESS_MODE`, `EXPECTED_GATE`, `EXPECTED_RECEIPT`.

WRITE registration requires current HEAD/model generation, no conflicting write lease, and a matching admission record whose underlying evidence receipt still hashes byte-identically. READ can be granted on a stale view but is always `WRITE=REJECT`, `LEARN=REJECT`, `COMMIT=REJECT`.

## Completion fields

`RUN_ID`, `PARENT_HEAD`, `RESULT`, `NEW_HEAD` (or `NO_COMMIT`), `MODEL_GENERATION_BEFORE`, `MODEL_GENERATION_AFTER`, `EVIDENCE_RECEIPT`.

Before every WRITE, LEARN, or COMMIT operation, a worker must call `authorize RUN_ID OP`; the coordinator revalidates lease ownership, canonical HEAD/model generation, and admission evidence.

Only the coordinator advances `.sigma_ail/coordination/CANONICAL/BRAIN_HEAD` and `MODEL_GENERATION`.

## Important boundary

This is the canonical coordination authority, not a filesystem sandbox. Existing legacy writers that ignore the coordinator must be integrated to call `register` before any WRITE/LEARN and `complete` before canonical commit. Until each writer is wired to this gate, the coordinator cannot physically prevent that legacy script from writing elsewhere under the same Unix account. Canonical brain acceptance remains fail-closed through this coordinator.
