# SIGMA C5 M5 — Window Handoff

Any future work window should read, in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/STATUS.md`
3. `C5_M5/CHECKPOINTS.md`
4. this file

Do not reconstruct history from old chat text when these branch files are available.

## Current purpose

Continue M5 core replacement until SIGMA can autonomously acquire and revise evidence without returning to token LEFT/RIGHT cognition, lexical grammar hardcoding, semantic cue tables, or host-substituted cognition.

The intended end-state is a C5V3 successor that can use real Internet evidence through mechanical transport while native SIGMA owns gap formation, evidence requests, hypothesis formation/revision, persistence, and later bounded semantic memory.

## Current starting point

Latest admitted capability remains:

`M5_NATIVE_GAP_EVIDENCE_REQUEST_R1`

Core SHA256:

`1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`

This capability has runtime admission PASS on Oppo.

A new isolated candidate is prepared but **not admitted yet**:

`M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R1`

- Core SHA256: `f530a556a670137f865b3f67b52557f3ccd9ec0b97f536f5c2123ce4276117e5`
- Transport SHA256: `0ed437aa2188b2382aec88c390697f7f912dff0ac27b9f50cc15b5936e713ffd`
- Preflight SHA256: `a5e2a92daa6e8651c621f6b3781ff4fb89f2252146282a0bb410a8980e653737`
- Bundle SHA256: `133225deea02fe644ac20f1248edd0af300f2fd21d4610e774101eef08a69b21`
- Local manifest/ZIP/shell checks: PASS.
- Oppo locked compile/runtime: pending.

## Next work item

Run `PREFLIGHT_C5V3_M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R1.sh` on Oppo and diagnose the exact failing layer if any.

Required flow:

`native relation-discrimination gap -> native evidence request -> generic mechanical provider invocation -> raw external evidence/provenance -> native SIGMA ingest -> native gap/revision state changes`

### Host may

- verify mechanical request framing and exact request-state byte equality;
- invoke a preconfigured opaque provider only when a valid native request exists;
- pass the native request bytes verbatim;
- return raw evidence/provenance bytes verbatim;
- perform process/file mechanics and invoke the locked VM;
- run post-hoc admission oracles.

### Host must not

- invent a gap;
- invent a research goal;
- invent or rewrite a semantic query;
- summarize/rank returned evidence for SIGMA;
- choose a belief, support/conflict stance, truth judgment, or final answer;
- select a provider dynamically as part of active cognition.

## Required admission gates

- No native request -> provider is not invoked.
- Malformed/fake request -> provider is not invoked.
- Native core independently rejects request-correlation mismatch.
- Valid request -> provider receives exact request bytes.
- Raw evidence enters SIGMA verbatim with provenance.
- Different gaps remain request-isolated.
- Irrelevant raw evidence leaves the native gap/request open.
- Discriminating raw evidence changes native state and revokes the request.
- Revoked request stops further provider invocation.
- Open request plus transport receipt persist/restart.
- A 64-record ledger rejects a 65th tool result.
- Source/transport/bytecode remain frozen.
- Production C5V3 remains read-only and unbound.

## Current hard FAILs

Until the new Oppo admission passes, retain:

- `TOOL_EXECUTION=FAIL`
- `REAL_INTERNET_ACQUISITION=FAIL`
- `AUTONOMOUS_RESEARCH=FAIL`
- `SEMANTIC_PARAPHRASE=FAIL`
- `ZERO_SHOT_LOW_OVERLAP_PARAPHRASE=FAIL`
- `BENIGN_UNGROUNDED_REORDER=FAIL`
- semantic support/conflict/truth judgment: FAIL.

If the mechanical transport admission passes, change only `MECHANICAL_TOOL_INVOCATION` to PASS. Keep real Internet and autonomous-research claims FAIL until separate admissions/blind tests.

## Update rule

After each successful experimental step:

1. update `STATUS.md` to the new current truth;
2. append the result to `CHECKPOINTS.md` without deleting older failures;
3. update this `HANDOFF.md` so `Next work item` points to exactly one next dependency;
4. commit to branch `c5-m5-core-replacement-live`;
5. do not merge to `SIGMA_LIFE` and do not cut over production unless explicitly instructed later.