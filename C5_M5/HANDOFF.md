# SIGMA C5 M5 — Window Handoff

Read in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/TWO_GATE_ARCHITECTURE.md`
4. `C5_M5/NATIVE_TOOL_RUNTIME_ARCHITECTURE.md`
5. `C5_M5/C5V3_AUTONOMOUS_INTEGRATION_PLAN.md`
6. `C5_M5/STATUS.md`
7. `C5_M5/CHECKPOINT_2026-09-09_1600_SOURCE_CONSISTENCY_R2_AND_PROVISIONAL_TRUTH_R1.md`
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

### Source-consistency-aware scoped revision R2

Core `82971fefa1e4b7c009612fc5be1ed88017386659f27c46b42117b603f4355736`.
Oppo bytecode `e52d23b0c8bfcb6a7bfaaf1ac1647af02a760f677a5b4959dc0ddae0cb0abc66`.

Admission + independent blind PASS.

Admitted exact facts:

- source consistency is native state;
- same SOURCE_ID on both A/B becomes `INCONSISTENT`;
- inconsistent source contributes authority to neither side;
- authority is recomputed retroactively;
- a previously held hypothesis retracts when source consistency removes its support below threshold;
- later clean authority can recover/form a hypothesis;
- R1 replay/evidence-ID/work-scope/injection/A->B->A/restart regressions remain PASS;
- `SOURCE_CONSISTENCY_AWARE_DISTINCT_AUTHORITY=PASS`;
- `NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS`.

The earlier Epistemic Stress R1 `65/100` is retained as the defect R2 repaired. `BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH=FAIL` remains.

## Current Gate A execution artifact

Run:

`SIGMA_C5_C5V3_M5_PROVISIONAL_EPISTEMIC_TRUTH_LADDER_R1_BUNDLE.zip`

Hashes:

- target core: `bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1`
- admission evaluator: `f579b43d3a9409a153626d082f0cb277007aa65b772d6836d6479d7ce90883f7`
- independent blind evaluator: `dcecb1df1e83116aeca0a30ce988b9d04d70b1936e4fdb5d5f514c31edf3232d`
- ladder runner: `60c2b73f8efd1d9c0bb7fa15e188226c7ca5f0e7696dac65359a534f588f2474`
- ladder bundle: `5eab91ff3cf280563114bd4b309166960e2538e91d604cc9beaf7ac9aea9abd0`

## Candidate semantics

Truth-state is explicitly separate from the revision policy's currently held hypothesis.

- `UNRESOLVED`: insufficient unopposed clean authority;
- `PROVISIONAL_A`: >=2 consistent distinct A sources and zero clean B sources;
- `PROVISIONAL_B`: >=2 consistent distinct B sources and zero clean A sources;
- `CONTESTED`: clean evidence exists on both A and B.

A self-inconsistent source does not create a contest. Clean late counter-evidence immediately downgrades provisional truth to `CONTESTED`. Relative authority may change the revision policy's `HELD` candidate, but it may not turn a contested truth-state into provisional while clean evidence remains on both sides.

The scoped incompatibility marker `EVIDENCE_BACKED_COMPETING_CONFIGURATIONS` means clean opposing evidence exists for both native candidates in one relation-discrimination scope. It is not general logical contradiction.

Both admission and blind first rerun the full Source-Consistency Revision R2 regression on the frozen truth-state core.

## Claim rule if PASS

Advance only:

`NATIVE_SCOPED_PROVISIONAL_EPISTEMIC_TRUTH=PASS`

in the native two-candidate/source-consistency scope.

Keep FAIL:

- `BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH`
- arbitrary natural-language logical contradiction/truth
- autonomous free-form summary generation
- zero-shot low-overlap summary
- broad whole-work narrative understanding
- theme/human-value induction
- multilingual transfer
- unbounded lifelong capacity
- production binding.

## Gate B boundary

Gate B remains independent. No published replacement runtime fingerprint was found on this branch at candidate freeze, so this Gate A artifact retains the currently regression-proven locked VM baseline rather than guessing a new tool runtime. A future Gate B runtime baseline must be fingerprinted and regress all admitted Gate A capabilities before replacing it.
