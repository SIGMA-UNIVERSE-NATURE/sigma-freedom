# SIGMA C5 M5 — Window Handoff

Any future work window should read, in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/STATUS.md`
4. `C5_M5/CHECKPOINTS.md`
5. this file

Do not reconstruct history from old chat text when these branch files are available.

## Current purpose

Continue M5 core replacement until SIGMA can autonomously acquire real evidence, read and integrate complete long-form works, revise hypotheses, compress learned knowledge into bounded local native memory, remove the source text, and continue learning — without token LEFT/RIGHT cognition, lexical grammar hardcoding, semantic cue tables, or host-substituted cognition.

The end-state acceptance standard is mandatory. Intermediate structural PASS results are dependencies only; they must never be inflated into whole-work understanding.

## Latest admitted starting point

`M5_NATIVE_GAP_EVIDENCE_REQUEST_R1`

Core SHA256: `1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`

Runtime admission: PASS on Oppo.

## Current pending candidate

`M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R1H2`

This is a harness-only correction. Core and transport are byte-identical to R1/R1H1:

- Core SHA256: `f530a556a670137f865b3f67b52557f3ccd9ec0b97f536f5c2123ce4276117e5`
- Transport SHA256: `0ed437aa2188b2382aec88c390697f7f912dff0ac27b9f50cc15b5936e713ffd`
- Preflight SHA256: `769b2caffd0791faf4b81ce1bc72f4cf3898dcf7d60266d0473a51a68f0e5617`
- Bundle SHA256: `df950ba9f07762d816f4eb7b399fb3f2b215d839fa10028f1f1e6c0e4c0bcf27`

## Runtime history relevant to this candidate

R1 passed no-request/malformed blocking, native request correlation, valid verbatim request/raw evidence transport, irrelevant-evidence native handling, cross-gap isolation, persistence and restart. It stopped at `RC=72` because the harness compared provider capture against a live request file after native SIGMA had correctly revoked that file.

R1H1 fixed that via an immutable request snapshot. It then passed discriminating raw-evidence native revision and verified that native request revocation stops future tool invocation. It stopped at `FAIL=BOUND_LEDGER_NOT_64`, `RC=83`.

R1H1 boundedness failure class: HARNESS COUNTING BUG, not established core failure. `open_gap` ingested 4 records successfully and 60 filler ingests also returned the exact native record-success decision. The oracle used `wc -l`, but canonical ledger files do not require a trailing newline; 64 records therefore present only 63 newline characters. R1H2 replaces only those two post-hoc assertions with `awk NR` record counting.

The actual native boundedness gate is not weakened: after 64 accepted records, a valid tool result must still be transported to SIGMA and SIGMA must return `REJECT_EXTERNAL_EVIDENCE:LEDGER_BOUND_REACHED`, keep the ledger at 64 records, and preserve the open native request.

## Exact next work item

Run `PREFLIGHT_C5V3_M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R1H2.sh` on Oppo.

Required remaining gates:

- 64 accepted ledger records are counted as 64 records independent of final newline formatting;
- a 65th external/tool result is rejected by native SIGMA;
- rejection cannot corrupt the existing native evidence request;
- source/transport/bytecode remain frozen;
- production C5V3 remains read-only and same active process;
- final admission reaches `RC=0`.

If R1H2 passes, update GitHub immediately and change only `MECHANICAL_TOOL_INVOCATION=PASS`.

Then build an independent blind host-substitution audit before real Internet access. After mechanical transport and real-Internet acquisition are independently admitted, the development path must move toward whole-work comprehension tests described in `END_STATE_ACCEPTANCE.md`: long-range narrative integration, evidence-backed summary/theme/value extraction after source removal, multilingual transfer, native semantic compression, and continual local learning.

## Host boundary

Host may perform mechanical request framing validation, invoke a preconfigured provider on a valid native request, pass request/raw bytes verbatim, and invoke locked VM/process/file plumbing.

Host must not invent gaps, research goals, semantic queries, summaries, rankings, beliefs, support/conflict/truth stances, theme/value interpretations, memory selections, or final answers.

## Hard FAILs retained

- `MECHANICAL_TOOL_INVOCATION=FAIL` until R1H2 final PASS.
- `REAL_INTERNET_ACQUISITION=FAIL`
- `AUTONOMOUS_RESEARCH=FAIL`
- `WHOLE_WORK_NARRATIVE_UNDERSTANDING=FAIL`
- `EVIDENCE_BACKED_WHOLE_WORK_SUMMARY=FAIL`
- `HUMAN_VALUE_INDUCTION_FROM_STORIES=FAIL`
- `MULTILINGUAL_NARRATIVE_TRANSFER=FAIL`
- `SEMANTIC_MEMORY_COMPRESSION_AFTER_SOURCE_REMOVAL=FAIL`
- `CONTINUAL_LEARNING_FROM_COMPRESSED_LOCAL_MEMORY=FAIL`
- `SEMANTIC_PARAPHRASE=FAIL`
- `ZERO_SHOT_LOW_OVERLAP_PARAPHRASE=FAIL`
- `BENIGN_UNGROUNDED_REORDER=FAIL`
- semantic support/conflict/truth judgment: FAIL.

## Update rule

After each successful experimental step, update `STATUS.md`, append `CHECKPOINTS.md`, update this handoff to one exact next dependency, and commit to `c5-m5-core-replacement-live`. Do not merge to `SIGMA_LIFE` and do not cut over production unless explicitly instructed later.