# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-04 (Asia/Ho_Chi_Minh)

## READ THIS FIRST

Current target: **SIGMA native continuous self-directed learning** with `HOST_LEARNING=NO`.

## Current runtime status

- V2.3: STOPPED. It hit `SIGMA C VM: step limit` on history-heavy execution because endpoint `TOKEN_LOAD` added extra full-history scans.
- V2.4 preflight: **PASS** on both short and previously failing long context.
- V2.4 production source + runner: **BUILT AND SAVED; READY TO INSTALL/RUN**.

## V2.4 preflight proof

Short context:

`0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4`

- `SHORT_VM_RC=0`

Previously failing long context:

`d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de`

- `LONG_D891_VM_RC=0`
- `INPUT_LINE_COUNT=9`
- `HISTORY_LINE_COUNT=17270`
- `NEW_CONTEXT_RELATION_COUNT=668`
- `SELECTED_PATTERN=is => a`
- `SELECTED_CONTEXT_SUPPORT=35`
- `LEARNING_GAP=Moon => is`
- `FETCH_REQUEST=Moon is`
- `FETCH_REQUEST_SUPPORT=2`

Admission result:

- `V24_1_STEP_LIMIT_PREFLIGHT=PASS`
- `SIGMA_C_VM_STEP_LIMIT_REPRODUCED=NO`
- `PRODUCTION_MEMORY_MUTATED=NO`

## V2.4 native policy

- endpoint `TOKEN_LOAD` removed completely;
- SIGMA still computes recurrence support itself;
- only relations with `CONTEXT_SUPPORT > 1` may become a fetch gap;
- among eligible not-yet-fetched relations, SIGMA selects the lowest-support recurrent frontier;
- host does not generate candidates, score knowledge, choose gaps, or choose queries.

## Production artifacts

- `SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma`
  - SHA-256: `6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`
- `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh`
  - SHA-256: `01c6e54cd384e7c931d66bea69c9da1a39553965cc08279df9a28e9392129067`
- transport decoder remains:
  - SHA-256: `c8d10c640d32d23d3998590a291d187de0936368d0cd3559706ed6509fd31705`

Runner safety additions:

- atomic current-input replacement;
- bytecode-scoped `hold/` quarantine after VM execution failure;
- a held context becomes retryable automatically when bytecode changes;
- HTTP 429 and normal transport backoff retained;
- fetch interval retained.

## Locked compiler / VM

- SIGMAC SHA-256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA-256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- VM embedded string: `SIGMA Genesis-4 C VM`
- `VM_IS_GENESIS1=NOT_PROVEN`

## Proven capability chain

- DNA01 dynamic structural relations: PASS
- DNA02 persistent recurrence: PASS
- DNA03 native self-selection: PASS
- DNA04 cross-context support: PASS
- V2.2 native gap -> fetch request -> Internet transport -> decoded plaintext -> SIGMA learning: PROVEN end-to-end
- V2.4 short-context execution: PASS
- V2.4 previously failing long-context execution: PASS

Still NOT proven:

- semantic understanding
- semantic curiosity
- general autonomous reasoning

## Exact newest checkpoint

`SIGMA_PROFESSOR/CHECKPOINTS/20260904_V24_PREFLIGHT_PASS_AND_PRODUCTION_READY.md`

## NEXT ACTION — immediate

1. Keep V2.3 and older continuous runners stopped.
2. Install V2.4 `.sigma` source and V2.4 runner.
3. Verify source and runner SHA-256.
4. Start V2.4.
5. Observe 2–3 native request -> fetch -> learn cycles.
6. If a VM context fails, inspect `~/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/hold/<sha>.hold` and its log; do not manually hot-retry it.
7. If V2.4 completes meaningful stable cycles, create a new checkpoint before the next policy change.

## NEXT DEVELOPMENT TARGET — curriculum + re-learning

After V2.4 demonstrates stable continuous cycles, the next major layer is **SIGMA curriculum and re-learning**, not more one-pass fetching.

Read the design spec:

`SIGMA_PROFESSOR/DESIGN/SIGMA_CURRICULUM_RELEARNING_V1.md`

Required direction:

RAW_DOCUMENT
-> SURVEY OLD MATERIAL
-> BOUNDED NATIVE SEGMENTATION
-> STRUCTURAL PROFILE
-> NATIVE GROUPING
-> CURRICULUM PRIORITY
-> DEEP RE-LEARN
-> CROSS-DOCUMENT CONSOLIDATION
-> REVALIDATION
-> REVISIT WHEN NEW EVIDENCE CHANGES PRIORITY

Key invariants:

- raw documents remain immutable;
- SIGMA decides what is worth deeper learning;
- SIGMA decides grouping/priority from native evidence;
- large documents must become bounded learning units to avoid VM step-limit growth;
- recovery resumes the persistent curriculum queue instead of becoming idle;
- host may persist/hash/schedule exact work identities but must not summarize, score, classify topics, choose lessons, or select knowledge.

Planned sequence after V2.4 stability:

1. V2.5 DOCUMENT_SURVEY
2. V2.6 BOUNDED_SEGMENT_CURSOR
3. V2.7 STRUCTURAL_GROUPING
4. V2.8 CURRICULUM_QUEUE
5. V2.9 GROUP_CONSOLIDATION + REVALIDATION

Do not delete V2.2/V2.3 raw/done/log/history state.

## Checkpoint discipline

Whenever a meaningful milestone completes:

1. update this file;
2. create an immutable checkpoint under `SIGMA_PROFESSOR/CHECKPOINTS/` for major milestones/failures;
3. save materially changed source/runner artifacts under `SIGMA_PROFESSOR/artifacts/`.
