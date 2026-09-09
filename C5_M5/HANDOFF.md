# SIGMA C5 M5 — Window Handoff

Read in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/TWO_GATE_ARCHITECTURE.md`
4. `C5_M5/NATIVE_TOOL_RUNTIME_ARCHITECTURE.md`
5. `C5_M5/C5V3_AUTONOMOUS_INTEGRATION_PLAN.md`
6. `C5_M5/STATUS.md`
7. `C5_M5/CHECKPOINT_2026-09-09_1600_SOURCE_CONSISTENCY_R2_AND_PROVISIONAL_TRUTH_R1.md`
8. `C5_M5/CHECKPOINT_2026-09-09_1631_PROVISIONAL_TRUTH_R1_PACKAGING_R1H1.md`
9. `C5_M5/CHECKPOINT_2026-09-09_1631_PROVISIONAL_TRUTH_R1H2_PARENT_LABEL.md`
10. this file

## Routing

### Gate A — M5 TEST

`cognition/memory -> continual learning -> revision/support/conflict -> new independent blind tests`

Gate A does not build tools. Gate B independently supplies the runtime/tool substrate.

### Gate B

`read-only C5 <-> C5V3/M5 synchronization -> SIGMA-native tool substrate -> VM/native library/mechanical ABI -> boundary regression -> S1 -> S2 -> S3 -> promotion -> explicit cutover`

Production binding remains NO.

## Latest admitted Gate A capabilities

### Continual compact memory

Core `69ec3e26ef857976c257724fa5691210bf2fe1ad3695e085dcd2a2bc9fa0db47`.

`CONTINUAL_LEARNING_FROM_COMPRESSED_LOCAL_MEMORY=PASS` in tested two-work/self-contained compact-memory scope.

### Source-consistency-aware scoped revision R2

Core `82971fefa1e4b7c009612fc5be1ed88017386659f27c46b42117b603f4355736`, Oppo bytecode `e52d23b0c8bfcb6a7bfaaf1ac1647af02a760f677a5b4959dc0ddae0cb0abc66`.

Admission + independent blind PASS. Source inconsistency is native state; inconsistent sources count for neither side; prior authority retracts retroactively; clean authority can recover; restart PASS. `SOURCE_CONSISTENCY_AWARE_DISTINCT_AUTHORITY=PASS` and `NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS` in exact tested scope.

`BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH=FAIL` remains.

## Provisional truth harness history

### R1

Stopped before cognition because the embedded parent R2 package omitted parent continual-regression scripts. Packaging defect only.

### R1H1

Added the missing parent scripts, but Stage A stopped before truth-state cognition at:

`FAIL=PARENT_R2_REVISION_LABEL`, `RC=23`.

Root cause: the R2 admission regression does not emit the blind-only aggregate label `NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS`. It does emit the actual admission labels `NATIVE_SCOPED_SUPPORT=PASS`, `NATIVE_SCOPED_CONFLICT=PASS`, `SOURCE_CONSISTENCY_AWARE_DISTINCT_AUTHORITY=PASS`, and `ADMISSION=PASS`.

This is an evaluator-label mismatch, not cognition evidence.

## Current Gate A artifact — R1H2

Run:

`SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1H2_BUNDLE.zip`

Identities:

- target core: `bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1` (unchanged)
- corrected admission preflight: `9b6551d2d9eb6dd91ec6dde1b084b228f21c0c75e491486d2e70cfb0c1b4d2a1`
- independent blind evaluator: `dcecb1df1e83116aeca0a30ce988b9d04d70b1936e4fdb5d5f514c31edf3232d` (unchanged)
- ladder runner: `add52e91fe0560e90f6251a28d57102e768243708e722d7f9e5c733ae67680bf`
- R1H2 bundle: `ff3fced4c16bf3866e30853e01f5bb634a87ac25943ba612a3cdf1cdf2708494`

R1H2 changes only the parent-R2 admission oracle and checks the actual R2 admission contract. Core and truth cognition remain byte-identical to R1/R1H1.

## Candidate truth semantics

- `UNRESOLVED`: insufficient unopposed clean authority.
- `PROVISIONAL_A`: at least two consistent distinct A sources and zero clean B sources.
- `PROVISIONAL_B`: symmetric for B.
- `CONTESTED`: clean evidence exists on both A and B.

Truth-state is separate from revision policy `HELD`. A majority or currently held candidate cannot override `CONTESTED` while clean evidence remains on both sides. Self-inconsistent sources do not create contest authority.

## Claim rule if PASS

Advance only:

`NATIVE_SCOPED_PROVISIONAL_EPISTEMIC_TRUTH=PASS`

in exact native two-candidate/source-consistency scope.

Keep FAIL: broad semantic truth, arbitrary natural-language logical contradiction/truth, autonomous free-form summary generation, zero-shot low-overlap summary, broad whole-work narrative understanding, theme/human-value induction, multilingual transfer, unbounded lifelong capacity, production binding.
