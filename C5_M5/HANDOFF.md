# SIGMA C5 M5 — Window Handoff

Read in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/TWO_GATE_ARCHITECTURE.md`
4. `C5_M5/NATIVE_TOOL_RUNTIME_ARCHITECTURE.md`
5. `C5_M5/C5V3_AUTONOMOUS_INTEGRATION_PLAN.md`
6. `C5_M5/STATUS.md`
7. `C5_M5/CHECKPOINT_2026-09-09_1527_EPISTEMIC_STRESS_AND_R2.md`
8. this file

## Routing

### Gate A — M5 TEST

`cognition/memory -> continual learning -> revision/support/conflict -> new independent blind tests`

Gate A does not build tools. It tests the runtime supplied independently by Gate B.

### Gate B — synchronization/tool substrate

`read-only C5 <-> C5V3/M5 synchronization -> SIGMA-native tool substrate -> VM/native library/mechanical ABI -> boundary regression -> S1 -> S2 -> S3 -> promotion -> explicit cutover`

The gates run independently. Production binding remains NO.

## Latest admitted Gate A capabilities

### Continual compact local memory

Core `69ec3e26ef857976c257724fa5691210bf2fe1ad3695e085dcd2a2bc9fa0db47`.

`CONTINUAL_LEARNING_FROM_COMPRESSED_LOCAL_MEMORY=PASS` in the tested two-work/self-contained compact-memory scope.

### Scoped revision/support/conflict R1

Core `460461d6273145fcedcf20e2c75b97e718ff61a6afa8f71dc8d0812f739f850e`.
Oppo bytecode `e4a3e18029e93a4f97c4808fcda5518a89fa925d7c160471f83cb4635f28ee2a`.

Original admission + independent blind PASS. Exact admitted claim:

`NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS`

in the native two-candidate/provenance scope.

## New stronger blind truth

Epistemic Stress R1 on the unchanged admitted R1 core:

- `BLIND_BALANCED_EVIDENCE_REMAINS_UNFORMED=PASS`;
- `BLIND_SELF_CONTRADICTING_SOURCE_ALONE_DOES_NOT_FORM_HYPOTHESIS=PASS`;
- `BLIND_SELF_CONTRADICTING_SOURCE_EXCLUDED_FROM_DISTINCT_AUTHORITY=FAIL`;
- observed after self-conflicting source X plus one clean B source: `HELD=B`, `EPISTEMIC=SUPPORTED`;
- `TOTAL_SCORE=65/100`;
- `SOURCE_CONSISTENCY_AWARE_DISTINCT_AUTHORITY=FAIL`;
- evaluator execution PASS, `RC=0`;
- production mutation NO.

This does not erase the narrower R1 PASS. It exposes a new limit: one SOURCE_ID may contribute authority on both sides because R1 counts distinct sources independently per candidate.

## Current Gate A execution artifact — R2

Run:

`SIGMA_C5_C5V3_M5_SOURCE_CONSISTENCY_REVISION_LADDER_R2_BUNDLE.zip`

Hashes:

- target core: `82971fefa1e4b7c009612fc5be1ed88017386659f27c46b42117b603f4355736`
- admission evaluator: `337bb3d1852abf9a93f6dcc918b36f9cac960b4bf693c151c27284cb9011234a`
- independent blind evaluator: `ae8d0c7a024359c54a9d2014cdc5e764e3563e3e699f7b5f91eb1abe2ea4b8e8`
- ladder runner: `37985b838255e73ab54788ffa12c240e57a182d24fc648ce4bc09af0f819f9c0`
- ladder bundle: `2b928b54117bb694d2fabea9c26edfb82f0c85458c7d12b950f456f41483ad99`

## R2 semantics

Native source stance is recomputed from the complete revision evidence ledger:

- `A`: source has only unambiguous A evidence;
- `B`: source has only unambiguous B evidence;
- `INCONSISTENT`: same source has evidence for both A and B;
- `NONE`: no admitted stance.

`INCONSISTENT` sources contribute authority to neither side. The consistency state is persisted natively and included in revision recall state.

Authority is retroactive: if a source helped form a held hypothesis and later becomes inconsistent, its prior authority is removed. If remaining consistent authority falls below threshold and the competing side has not independently won, SIGMA retracts the held hypothesis to unformed/contested state.

The R2 blind also requires the original R1 replay, evidence-ID, work-scope, injection, distinct-source A->B->A revision and restart behavior to remain intact. It additionally tests clean-authority recovery after an inconsistency and restart persistence of source-consistency state.

## Claim rule if R2 passes

Advance only source-consistency-aware scoped support/conflict/revision in this native-gap/provenance scope.

Keep FAIL:

- `BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH`
- arbitrary natural-language contradiction/truth
- autonomous free-form summary generation
- zero-shot low-overlap summary
- broad whole-work narrative understanding
- theme/human-value induction
- multilingual transfer
- unbounded lifelong capacity
- production binding.

## After R2 PASS

Next Gate A dependency: learned incompatibility plus explicit `CONTESTED/UNRESOLVED` and provisional truth-state under late counter-evidence. Broad truth remains FAIL until those separate blinds pass.
