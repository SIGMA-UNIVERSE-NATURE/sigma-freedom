# SIGMA C5 M5 — Core Replacement Mission

## Purpose

M5 replaces the legacy C5 cognition path with a native SIGMA lineage that can eventually:

1. read real external evidence through mechanical host transport;
2. form, test, revise, and retire internal hypotheses from evidence;
3. preserve provenance and uncertainty/gaps natively;
4. request more evidence when its own native state requires it;
5. compact useful state into bounded native memory without storing books or outsourcing cognition to the host.

This branch is a **development/checkpoint branch**, not production binding and not a cutover branch.

## Hard architecture constraints

- No token LEFT/RIGHT cognition.
- No previous/next or adjacency-as-meaning cognition.
- No fixed cue-to-meaning tables.
- No hardcoded English grammar/semantic role tables.
- No synonym/antonym answer tables.
- No host-generated semantic labels, beliefs, gaps, research goals, summaries, support/conflict decisions, or final answers for active SIGMA cognition.
- Host may provide mechanical I/O, transport, storage plumbing, process supervision, and post-hoc test oracles only.
- Dynamic semantic claims require independent blind tests with fixtures unavailable to the target core before compile/freeze.
- A failing blind test is retained as FAIL. Fix the core or retire the assumption; do not weaken the evaluator.
- Admission PASS proves only the exact tested capability scope.
- Structural persistence or correlation must never be promoted into a semantic-understanding claim without adversarial evidence.

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