# SIGMA C5 M5 — Window Handoff

Any future work window should read, in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/STATUS.md`
3. `C5_M5/CHECKPOINTS.md`
4. this file

Do not reconstruct history from old chat text when these branch files are available.

## Current purpose

Continue M5 core replacement until SIGMA can autonomously acquire and revise evidence without returning to token LEFT/RIGHT cognition, lexical grammar hardcoding, semantic cue tables, or host-substituted cognition.

## Latest admitted starting point

`M5_NATIVE_GAP_EVIDENCE_REQUEST_R1`

Core SHA256: `1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`

Runtime admission: PASS on Oppo.

## Current pending candidate

`M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R1H1`

This is a harness-only correction of R1.

- Core SHA256 unchanged: `f530a556a670137f865b3f67b52557f3ccd9ec0b97f536f5c2123ce4276117e5`
- Transport SHA256 unchanged: `0ed437aa2188b2382aec88c390697f7f912dff0ac27b9f50cc15b5936e713ffd`
- Preflight SHA256: `f52f0c584e9edafa55eb2598bd4591b9a0d506df4c510eb054abb8b83bc2e00c`
- Bundle SHA256: `5fa18729eb97473884da3ece2c8b5584da86e6e89155a6d812c123f2c41a2b25`

R1 runtime already passed no-request/malformed blocking, request correlation, valid verbatim request/raw evidence transport, irrelevant-evidence native handling, cross-gap isolation, persistence and restart. It then stopped at `RC=72` because the harness compared provider capture to the live request output after native SIGMA had correctly revoked that output due to discriminating evidence.

R1H1 fixes only the oracle: it snapshots the native request before provider invocation and compares later provider capture against that immutable snapshot. No native/core/transport behavior changed and no test criterion was weakened.

## Exact next work item

Run `PREFLIGHT_C5V3_M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R1H1.sh` on Oppo.

Required final gates remain:

- discriminating raw evidence reaches native SIGMA through byte-preserving transport;
- SIGMA itself revises/revokes gap/request;
- revoked request stops further provider invocation;
- 64-record ledger refuses a 65th tool result;
- source/transport/bytecode remain frozen;
- production C5V3 remains read-only and same active process.

If R1H1 passes, update GitHub immediately and change only `MECHANICAL_TOOL_INVOCATION=PASS`.

Then build an independent blind host-substitution audit before real Internet access. The blind must prove that absent/malformed/fake native requests cannot cause host fallback query generation or provider invocation and that raw provider payload cannot directly force a native conclusion.

## Host boundary

Host may perform mechanical request framing validation, invoke a preconfigured provider on a valid native request, pass request/raw bytes verbatim, and invoke locked VM/process/file plumbing.

Host must not invent gaps, research goals, semantic queries, summaries, rankings, beliefs, support/conflict/truth stances, memory selections, or final answers.

## Hard FAILs retained

- `REAL_INTERNET_ACQUISITION=FAIL`
- `AUTONOMOUS_RESEARCH=FAIL`
- `SEMANTIC_PARAPHRASE=FAIL`
- `ZERO_SHOT_LOW_OVERLAP_PARAPHRASE=FAIL`
- `BENIGN_UNGROUNDED_REORDER=FAIL`
- semantic support/conflict/truth judgment: FAIL.
- `MECHANICAL_TOOL_INVOCATION` remains FAIL until R1H1 reaches final admission PASS.

## Update rule

After each successful experimental step, update `STATUS.md`, append `CHECKPOINTS.md`, update this handoff to one exact next dependency, and commit to `c5-m5-core-replacement-live`. Do not merge to `SIGMA_LIFE` and do not cut over production unless explicitly instructed later.