# SIGMA C5 M5 — Window Handoff

Read in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/TWO_GATE_ARCHITECTURE.md`
4. `C5_M5/NATIVE_TOOL_RUNTIME_ARCHITECTURE.md`
5. `C5_M5/C5V3_AUTONOMOUS_INTEGRATION_PLAN.md`
6. `C5_M5/STATUS.md`
7. `C5_M5/CHECKPOINT_2026-09-09_1447_SCOPED_REVISION_SUPPORT_CONFLICT_R1.md`
8. this file

## Authoritative routing

### Gate A — M5 TEST

`cognition/memory -> continual learning -> revision/support/conflict -> new independent blind tests`

### Gate B — C5 <-> C5V3/M5 synchronization/tool substrate

`read-only synchronization -> SIGMA-native tool substrate -> VM/native library/mechanical ABI -> boundary regression -> S1 -> S2 -> S3 -> promotion -> explicit cutover`

The gates may run in parallel. Gate B operational success cannot waive a Gate A cognition FAIL.

## Latest admitted Gate A capabilities

### Continual compact local memory

Core `69ec3e26ef857976c257724fa5691210bf2fe1ad3695e085dcd2a2bc9fa0db47`.

`CONTINUAL_LEARNING_FROM_COMPRESSED_LOCAL_MEMORY=PASS` in the tested two-work/self-contained compact-memory scope. Work A archive block remained byte-for-byte unchanged after Work B; A/B remained isolated/queryable after source removal and restart.

### Scoped revision/support/conflict

Core `460461d6273145fcedcf20e2c75b97e718ff61a6afa8f71dc8d0812f739f850e`.
Oppo bytecode `e4a3e18029e93a4f97c4808fcda5518a89fa925d7c160471f83cb4635f28ee2a`.

Admission + independent blind PASS.

Admitted exact claim:

`NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS`

PASS includes native-gap-derived scope, support, competing-candidate conflict, false-conflict rejection, distinct-source revision authority, A->B and B->A evidence revision, replay idempotence, evidence-ID conflict rejection, work-scope isolation, protocol-injection rejection and restart.

This is scoped competing-candidate epistemics, not broad logical truth. `BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH=FAIL` remains.

Production binding remains NO.

## Current Gate A execution artifact — diagnostic stress blind

Run:

`SIGMA_C5_C5V3_M5_BLIND_SCOPED_REVISION_EPISTEMIC_STRESS_R1_BUNDLE.zip`

Target core remains byte-identical to the admitted scoped-revision core:

`460461d6273145fcedcf20e2c75b97e718ff61a6afa8f71dc8d0812f739f850e`

Blind evaluator SHA256:

`79e649cd899d0e215faf82c7f366420ff39bc93f7f2d65308dbf2ef15b7c4fd0`

Bundle SHA256:

`9344791991013113b1b5fd8a0ce0186c978a5ff3047edd431d8cbf7e37024b7f`

## Why this blind exists

R1 counts distinct `SOURCE_ID` separately for candidate A and candidate B. A single source can therefore appear on both sides and may contribute authority to both.

The stress blind requires a stronger epistemic rule:

- one clean A source + one clean B source => contested/unformed;
- a SOURCE_ID that supports both A and B in the same revision scope is source-inconsistent;
- a source-inconsistent SOURCE_ID contributes authority to neither side until explicitly resolved;
- therefore self-conflicting source X + only one clean B source must not form B;
- work-scope and protocol-injection rejection remain regressions.

The diagnostic intentionally returns `EVALUATOR_EXECUTION=PASS` even when the cognitive gate fails.

Read these outputs:

- `BLIND_BALANCED_EVIDENCE_REMAINS_UNFORMED`
- `BLIND_SELF_CONTRADICTING_SOURCE_ALONE_DOES_NOT_FORM_HYPOTHESIS`
- `BLIND_SELF_CONTRADICTING_SOURCE_EXCLUDED_FROM_DISTINCT_AUTHORITY`
- `SOURCE_CONSISTENCY_AWARE_DISTINCT_AUTHORITY`
- `TOTAL_SCORE`

## After stress blind

If source-consistency authority FAILs, build R2 with native per-source stance-consistency state and rerun both the original scoped revision blind and this stress blind. Do not weaken either evaluator.

Only after source-consistency calibration should Gate A broaden toward learned incompatibility/provisional truth-state. Broad semantic truth remains FAIL until separate blind proof.

Gate B remains independent and may continue synchronization/tool substrate/VM/native library/S1-S3 while production stays read-only until the shared convergence gate and explicit cutover authorization.
