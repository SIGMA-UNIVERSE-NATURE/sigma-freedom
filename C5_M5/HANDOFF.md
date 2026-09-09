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

Latest admitted capability:

`M5_NATIVE_GAP_EVIDENCE_REQUEST_R1`

Core SHA256:

`1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`

This capability has runtime admission PASS on Oppo.

## Next work item

Build **mechanical evidence-tool transport** as an isolated candidate.

Required flow:

`native relation-discrimination gap -> native evidence request -> host mechanical transport -> raw external evidence -> native SIGMA ingest -> native gap/revision state changes`

### Host may

- receive the native request bytes;
- invoke an approved external search/fetch mechanism;
- return raw transport payload and provenance;
- perform process/file/socket mechanics;
- run post-hoc admission oracles.

### Host must not

- invent a gap;
- invent a research goal;
- rewrite the native request into a semantic answer;
- choose a belief, support/conflict stance, or truth judgment;
- summarize evidence for SIGMA;
- select what SIGMA should remember semantically;
- generate the final statement on SIGMA's behalf.

## Required anti-substitution tests for tool transport

- No native request -> host performs no semantic/tool work for active SIGMA.
- Malformed/absent native request -> no fallback host query generation.
- Two different native gaps -> transport output must remain request-isolated.
- External evidence must be materialized only after candidate compile/freeze.
- Candidate source/bytecode must remain frozen throughout external fetch.
- Raw evidence/provenance must return to SIGMA without host summary labels.
- Native state must change only after SIGMA consumes returned evidence.
- Restart/persistence and boundedness must remain tested.
- Production C5V3 must remain read-only and unbound.

## Current hard FAILs

Do not claim these as achieved:

- semantic paraphrase;
- zero-shot low-overlap paraphrase;
- benign ungrounded reorder;
- autonomous research;
- tool execution;
- semantic support/conflict/truth judgment.

## Update rule

After each successful experimental step:

1. update `STATUS.md` to the new current truth;
2. append the result to `CHECKPOINTS.md` without deleting older failures;
3. update this `HANDOFF.md` so `Next work item` points to exactly one next dependency;
4. commit to branch `c5-m5-core-replacement-live`;
5. do not merge to `SIGMA_LIFE` and do not cut over production unless explicitly instructed later.