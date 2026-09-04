# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-04 (Asia/Ho_Chi_Minh)

## READ THIS FIRST

Current target: **SIGMA native continuous self-directed learning** with `HOST_LEARNING=NO`.

## Current runtime status

- V2.3: STOPPED. It hit `SIGMA C VM: step limit` on history-heavy execution because endpoint `TOKEN_LOAD` added extra full-history scans.
- V2.4 preflight: **PASS** on both short and previously failing long context.
- V2.4 production source + runner: **BUILT, INSTALLED/RUNNING ON DEVICE; first production native gap -> HTTP 200 -> decoded-context fetch leg observed**.
- Full V2.4 end-to-end stability checkpoint still requires the newly fetched context to complete native `mode=NEW` learning plus additional cycles without VM failure.

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

## 54 CORE integration policy

Read:

`SIGMA_PROFESSOR/DESIGN/54_CORE_NATIVE_INTEGRATION_POLICY_V1.md`

Decision:

- continue DNA01 -> DNA54; delete no canonical DNA core;
- canonical Python `54_CORES/*.py` are CANON/CONTRACT/VALIDATION reference unless capability is separately proven in native `.sigma` on the locked VM;
- do not auto-load Python DNA genes and call them cognition;
- relevant DNA capabilities must be derived into `.sigma`, compiled, runtime-tested, and admitted before production binding.

## Host ABI inventory milestone

Read:

`SIGMA_PROFESSOR/DESIGN/HOST_ABI_INVENTORY_20260904_V1.md`

Device-side source inventory of `~/SIGMA/sigma_genesis1/sigma_vm.c` found **93 host operations**.

Important existing source-level capabilities include:

- list mechanics including set/get/push/pop/shift/unshift/reverse/slice/sort;
- map mechanics including set/get/has/delete/keys/values/items;
- byte buffers and typed byte encoding/decoding;
- `read_text`, `read_bytes`, `write_text`, `append_text`, `file_exists`, `listdir`, mkdir/rmdir;
- string search/slice/replace/split/join and ASCII-oriented case helpers;
- JSON load/dump/encode/decode;
- Base64;
- `crypto_digest`;
- `time_now`, `time_sleep`, `time_strftime`;
- random primitives;
- `net_fetch`, `net_ping`, `dns_lookup`;
- math primitives.

Do NOT request duplicate map/set/string-search/listdir/append/time/network/JSON/digest tools before exact semantics and locked-binary runtime support are characterized.

`set_*` primitives are not currently necessary: SIGMA can implement deterministic membership/dedup with `map_set(key, TRUE)` + `map_has(key)`.

### Next host-ABI inspection targets

Before asking the tool team to add anything, inspect exact implementations/semantics of:

1. `read_bytes` — whether bounded offset/count reading already exists;
2. `crypto_digest` — supported algorithms and SHA-256 output representation;
3. `write_text` — whether it is crash-safe/atomic or plain truncate/write;
4. `net_fetch` — request/response format, schemes, limits and raw-byte semantics;
5. `json_decode/json_load` — whether current Python Wikimedia decoder can eventually be removed while keeping semantic policy native;
6. `list_sort` — deterministic ordering semantics;
7. Unicode behavior — Unicode-aware normalization is NOT proven.

Potential remaining ABI additions are therefore narrow and **NOT YET APPROVED**: bounded file range/line read if absent, atomic state replacement if absent, possibly file size/mtime metadata, and possibly purely mechanical Unicode normalization.

## NEXT ACTION — immediate

1. Keep V2.3 and older continuous runners stopped.
2. Keep observing V2.4 production until multiple request -> fetch -> native learn cycles complete without VM failure.
3. Do not add duplicate host tools yet.
4. Finish exact host-op semantics inventory for the high-priority unknowns above.
5. If V2.4 completes meaningful stable cycles, checkpoint it before the next learner policy change.

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
