# SIGMA C5 M5 — Core Replacement Mission

## Purpose

M5 replaces the legacy C5 cognition path with a native SIGMA lineage whose final target is defined in `C5_M5/END_STATE_ACCEPTANCE.md`.

The successor must eventually:

1. acquire real Internet evidence through mechanical host transport while native SIGMA owns the need/request;
2. read complete long-form material rather than treating cognition as isolated token fragments;
3. integrate entities, events, motives, relationships, causality, themes, unresolved questions, and later revisions across the whole source;
4. form, test, revise, and retire native hypotheses from evidence;
5. preserve provenance and uncertainty/gaps natively;
6. request more evidence when its own native state requires it;
7. summarize whole works and recover their central direction/values from learned state after the source text is removed;
8. transfer learned structures across unseen works and multiple languages without English-only semantic hardcoding;
9. compact useful learned state into bounded local native memory without storing books/ebooks/articles as a substitute for understanding;
10. restart from local memory and continue learning from later unseen evidence.

This branch is a **development/checkpoint branch**, not production binding and not a cutover branch.

## Hard architecture constraints

- No token LEFT/RIGHT cognition.
- No previous/next or adjacency-as-meaning cognition.
- No fixed cue-to-meaning tables.
- No hardcoded English grammar/semantic role tables.
- No synonym/antonym/theme/value answer tables.
- No host-generated semantic labels, beliefs, gaps, research goals, summaries, support/conflict decisions, memory selections, or final answers for active SIGMA cognition.
- Host may provide mechanical I/O, transport, storage plumbing, process supervision, generic computation/runtime primitives, and post-hoc test oracles only.
- The currently used primitive set is not an architectural ceiling. When native SIGMA is blocked by missing generic computation, the VM/runtime may and should be extended under `C5_M5/NATIVE_TOOL_EXPANSION_POLICY.md`.
- Tool/runtime expansion is acceptable only when semantic authority remains inside native SIGMA; a host convenience primitive must not smuggle in an answer, meaning label, summary, theme/value judgment, salience decision, belief, or research decision.
- Dynamic semantic claims require independent blind tests with fixtures unavailable to the target core before compile/freeze.
- A failing blind test is retained as FAIL. Fix the core or retire the assumption; do not weaken the evaluator.
- Admission PASS proves only the exact tested capability scope.
- Structural persistence, lexical overlap, shared context, sequence correlation, or compression ratio must never be promoted into a semantic-understanding claim without adversarial evidence.
- SIGMA must not guess when evidence is insufficient; insufficient native evidence should create/revise a native gap and, when appropriate, a native evidence request.

## Narrative/human-understanding requirement

The final system must be able to learn from stories and other human accounts as complete works. It should infer human goals, conflicts, choices, consequences, relationships, tensions, themes, and values from narrative evidence rather than from fixed moral or psychological lookup tables.

Theme/value interpretation is evidence-grounded and may remain plural when a work supports multiple interpretations. The system must not force one answer merely to satisfy an evaluator.

## Production safety

Production C5V3 remains read-only during candidate admission. Integration/graft, promotion, cutover, and rollback are distinct operations. No candidate may bind production without an explicit later cutover decision.

## Update discipline

After every successful experimental step, update `C5_M5/STATUS.md` and append a checkpoint to `C5_M5/CHECKPOINTS.md` on branch `c5-m5-core-replacement-live`.

Every checkpoint must record:

- candidate/capability ID;
- core SHA256 when available;
- test type (admission or blind);
- PASS/FAIL facts;
- assumptions retired by later blind evidence;
- current known FAIL capabilities;
- production-binding state;
- exact next dependency.

Never rewrite historical FAIL into PASS. Later fixes create new checkpoints.
