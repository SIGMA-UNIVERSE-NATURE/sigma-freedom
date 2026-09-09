# SIGMA C5 M5 — Window Handoff

Read in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/STATUS.md`
4. `C5_M5/CHECKPOINTS.md`
5. `C5_M5/24H_EXECUTION.md`
6. this file

Do not reconstruct history from old chat when these files are available.

## Purpose

Build a C5V3 successor that can acquire real sources, read complete long-form works, form/revise native understanding, compress retained knowledge into bounded local memory, remove the source text and continue learning. No token LEFT/RIGHT cognition, hardcoded English semantic grammar, cue-to-meaning tables or host-substituted cognition.

## Latest admitted capability

`M5_NATIVE_GAP_EVIDENCE_REQUEST_R1`

Core SHA256: `1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`.

## Immediate execution path

Use `SIGMA_C5_C5V3_M5_24H_EXECUTION_LADDER_R1_BUNDLE.zip`.

Bundle SHA256: `87118eebdda1ee1af2d5bb247516905da26ded4f1ce60595c8da6e859fe32197`.

Runner SHA256: `c4c1780d57dc57357bc9d90e90faed04cee4e4bb384241cc9a3eb200f244ad69`.

Strict stages:

1. Transport R2 full admission.
   - core `c3ec9d2436f965046ac53bc8b4dba67870f1fb937868d3b667cad6779ea51285`
   - transport `32c54f4f2f342652b27f4639b1b7ae74c4cc30f27a80bf202eebe309594ddb35`
   - adds native request recomputation from current native gap state before provider call.
2. Blind host-substitution R1.
   - forged correlated request, stale cross-gap request, raw protocol injection, irrelevant evidence and native-only revision.
3. Native Gap Search Query R1.
   - core `286b1c557a2cbe027d67fb645448bdd8ff09540d5a628b89517ef2a3fa38bd5f`
   - query bytes originate inside SIGMA; host does not rewrite/expand.
4. Real Internet Search Discovery R1.
   - fixed mechanical Wikipedia MediaWiki search provider.
   - native query goes to real network; compact raw search response returns to native SIGMA.

The ladder stops at first non-zero RC. Never bypass a failed dependency.

## Why R2 replaced R1H2 as the accelerated path

R1H2 only fixed the boundedness oracle. Static audit then found a real trust-boundary defect: R1 transport trusted correlated request files as authority. R2 adds locked native recomputation against current gap state immediately before provider invocation and includes all R1H2 gates. This is a core/transport trust fix, not an evaluator relaxation.

## Claims if all four stages pass

Only the following may advance:

- mechanical tool invocation;
- blind host-substitution boundary in tested scope;
- native search-query bytes;
- real Internet search-discovery bytes.

The following remain FAIL:

- full-source fetch/read;
- autonomous research;
- whole-work narrative understanding;
- evidence-backed whole-work summary;
- theme/human-value induction;
- multilingual narrative transfer;
- semantic compression after source removal;
- continual learning from compressed local memory;
- semantic paraphrase/zero-shot low-overlap;
- semantic support/conflict/truth judgment.

## Next architecture after a fully passing ladder

Build a bounded transient long-form work stream. Raw book/story text may exist only as bounded working source during reading. The persistent state after a work boundary must not be the ebook.

Then build whole-work native representation and test it with unseen long-form sources. Required gates include distant evidence integration, entity/event/motive/consequence revision across sections, source-removal summary/reasoning, evidence-backed theme/human values, multilingual transfer, compression-size reduction with semantic retention, restart and later learning from local compressed memory.

Do not optimize another narrow sentence benchmark as the main objective.

## Update discipline

After each PASS, update `STATUS.md`, append `CHECKPOINTS.md`, and move this handoff to exactly one next dependency. Historical failures and retired assumptions remain visible. Never merge to `SIGMA_LIFE` or cut over production without explicit instruction.