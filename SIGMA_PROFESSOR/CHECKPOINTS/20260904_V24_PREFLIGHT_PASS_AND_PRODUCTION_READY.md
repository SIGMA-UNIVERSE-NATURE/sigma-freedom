# SIGMA_PROFESSOR CHECKPOINT — V2.4 PREFLIGHT PASS / PRODUCTION READY

Date: 2026-09-04 (Asia/Ho_Chi_Minh)

## Result

V2.4 recurrent-support-frontier preflight PASSED against both:

- short/reconsider context `0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4`
- previously failing long context `d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de`

Observed:

- `SHORT_VM_RC=0`
- `LONG_D891_VM_RC=0`
- `V24_1_STEP_LIMIT_PREFLIGHT=PASS`
- `SIGMA_C_VM_STEP_LIMIT_REPRODUCED=NO`
- `PRODUCTION_MEMORY_MUTATED=NO`

Long context measurements at test time:

- `INPUT_LINE_COUNT=9`
- `HISTORY_LINE_COUNT=17270`
- `NEW_CONTEXT_RELATION_COUNT=668`
- `SELECTED_PATTERN=is => a`
- `SELECTED_CONTEXT_SUPPORT=35`
- `LEARNING_GAP=Moon => is`
- `FETCH_REQUEST=Moon is`
- `FETCH_REQUEST_SUPPORT=2`

## Why V2.4 differs from V2.3

V2.3 hit `SIGMA C VM: step limit` because each candidate performed full-history endpoint-load scans in addition to recurrence support scans.

V2.4 removes endpoint TOKEN_LOAD entirely.

Native request policy:

1. SIGMA computes relation recurrence support.
2. Only relations with `CONTEXT_SUPPORT > 1` are eligible for self-directed fetch.
3. Among eligible not-yet-fetched relations, SIGMA selects the lowest-support recurrent frontier.
4. Tie behavior is deterministic first-candidate retention.

No stopword list, lesson list, topic list, host scoring, host candidate generation, or host selection.

## Locked toolchain

- SIGMAC SHA-256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA-256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- mechanical transport decoder SHA-256: `c8d10c640d32d23d3998590a291d187de0936368d0cd3559706ed6509fd31705`

## V2.4 production artifacts

- `SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma`
  - local build SHA-256: `6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`
- `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh`
  - local build SHA-256: `01c6e54cd384e7c931d66bea69c9da1a39553965cc08279df9a28e9392129067`

Runner safety additions:

- atomic replacement of current input (avoids read-only overwrite failures)
- bytecode-scoped `hold/` quarantine after a VM execution failure
- held contexts automatically become retryable when bytecode changes
- HTTP 429 backoff retained
- minimum fetch interval retained

## State lineage

V2.4 intentionally reuses the clean V2.2 lineage:

- state directory: `~/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2`
- SIGMA memory namespace: `SIGMA_CL22_*`

Do not import V2.1 JSON-polluted state.

## Proven / not proven

Proven in exact tested scopes:

- dynamic structural learning
- persistent recurrence
- native self-selection
- cross-context support
- native gap -> fetch request -> Internet transport -> plaintext -> native learning
- V2.4 long-context execution without the V2.3 step-limit failure

Still NOT proven:

- semantic understanding
- semantic curiosity
- general autonomous reasoning

## Next action

Install V2.4 source + runner, ensure no prior continuous runner holds the shared lock, start V2.4, then observe 2–3 request/fetch/learn cycles.

If any context fails VM execution, do not hot-retry manually. Inspect its `hold/<sha>.hold` and log; runner will quarantine it for the current bytecode.
