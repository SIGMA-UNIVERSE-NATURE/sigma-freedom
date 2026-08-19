# SIGMA VM EXPERIMENT MAP - PERSISTENCE RECEIPT

Map ID: `SIGMA-VM-EXPERIMENT-MAP-20260818-001`

Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`

Branch: `agent/sigma-experiment-map-20260818`

Branch origin: `agent/sigma-experiment-ledger-20260818` at commit `8c290d2ec579c3b398b331ff96a67f1aa1f94ab9`.

## Persistence commits

1. `c4cd2520c9b804fd641b83277114fee8438c3c34`
   - message: `map SIGMA VM experiments and window ownership`
   - tree: `e9ccfc43dedd0d6896d06f4a1046758c2776b703`

2. `f7fc46b88f75c05c6f650a90fd75480fc7978da8`
   - message: `repair SIGMA VM window assignments encoding`
   - tree: `865b805bbfea5b3a53eb930f2378394b77954881`

## Verified package

The branch contains:

- human-readable experiment map;
- one-task-per-window assignments;
- control policy;
- nodes E00-E13;
- dependency edges;
- window registry;
- SHA-256 manifest and checksum inventory.

Current activation:

- `W00_CUA2_INTEGRATOR = ACTIVE`
- `W01_BOUNDARY_AUDITOR = READY_TO_OPEN`
- `W02_F64_CORPUS_CURATOR = READY_TO_OPEN`
- `W03..W10 = BLOCKED`

Only W01 and W02 are parallel-safe at the current frontier. W03 must not open until both return SHA-pinned PASS/FROZEN_PASS handoffs.

## Mutation boundary

`SIGMA_LIFE_DIRECT_MUTATION = FALSE`

`CANONICAL_MERGE = NONE`

`FOUNDATION_MERGE = NONE`

`PHASE2_REOPEN = NONE`

`512_PROMOTION = NONE`

The experiment map coordinates evidence work only. It does not itself promote a capability.
