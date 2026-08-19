# SIGMA VM - WINDOW ASSIGNMENTS v1.0

Use exactly one block per chat window. Do not combine blocks. A window stops after producing its handoff and must not begin the next node.

---

## WINDOW W01 - BOUNDARY AUDITOR

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W01_BOUNDARY_AUDITOR
NODE_ID=E04_BOUNDARY_BASELINE_005
MODE=READ_ONLY
ONE_TASK_ONLY=exact inventory of the five remaining trusted custom C primitives.

Read the current SIGMA VM candidate, current adapter source, and current compiled host binary.
Pin every input SHA-256 before analysis.
Record exact primitive names, definitions, call sites, semantic category, bootstrap dependency, source presence, and binary presence.
Independently confirm math_floordiv is absent.
Measure whether bytes_f64_le_at is present; do not assume it.
Do not patch, rename, remove, add, compile a new candidate, or alter ABI, Foundation, or corpus.
Return TRUSTED_HOST_BOUNDARY_BASELINE_005.json, STATIC_CALLSITE_MAP.json, BINARY_SYMBOL_OR_STRING_AUDIT.json, and W01_HANDOFF.md.
End with exactly W01_RESULT_PASS or W01_RESULT_HOLD: <exact reason>.
```

---

## WINDOW W02 - FLOAT64 CORPUS CURATOR

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W02_F64_CORPUS_CURATOR
NODE_ID=E05_FLOAT64_CORPUS_FREEZE_001
MODE=CORPUS_ONLY
ONE_TASK_ONLY=freeze an independent FLOAT64 raw-bit corpus and oracle contract.

Preserve the historical v13a failures:
qnan_payload1
qnan_neg_payload
snan_payload1

Create a versioned public corpus covering signed zero, finite extrema, normals, subnormals, infinities, qNaN payload/sign variants, and sNaN payload variants.
Every case must contain the exact expected 64-bit pattern.
Define a deterministic withheld-corpus generator whose seed is derived from the future frozen candidate source SHA-256.
The oracle must be independent from the candidate implementation.
Do not edit VM source, adapter source, frozen ABI, Foundation, or ledger.
Return FLOAT64_PUBLIC_CORPUS_v1.json, FLOAT64_WITHHELD_GENERATOR_SPEC_v1.json, FLOAT64_ORACLE_CONTRACT_v1.json, CORPUS_SHA256SUMS, and W02_HANDOFF.md.
End with exactly W02_RESULT_FROZEN_PASS or W02_RESULT_HOLD: <exact reason>.
```

---

## WINDOW W03 - FLOAT64 IMPLEMENTER

DO NOT OPEN UNTIL W01_RESULT_PASS AND W02_RESULT_FROZEN_PASS ARE BOTH SHA-PINNED.

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W03_F64_IMPLEMENTER
NODE_ID=E06_FLOAT64_REPRESENTATION_CANDIDATE_001
MODE=ONE_CANDIDATE_ONLY

Inputs must include W01 PASS and W02 FROZEN_PASS with exact hashes.
Implement exactly one SIGMA-native representation candidate.
Primary hypothesis: preserve the raw 64-bit payload beside the numeric view so untouched constants remain bit-exact while numeric operators use the numeric view.
Do not retry numeric-only reconstruction already rejected by v13a.
Do not add a target-specific C FLOAT64 decoder or bitcast and call the trusted-boundary reduction complete.
Do not edit corpus, evaluator, ABI, Foundation, canonical state, or 512 ledger.
Do not claim PASS.
Return one candidate, minimal diff, compile result, artifact hashes, and W03_HANDOFF.md.
End with exactly W03_CANDIDATE_READY, W03_RESULT_HOLD: <reason>, or W03_RESULT_REJECT: <reason>.
```

---

## WINDOW W04 - CANDIDATE FREEZER

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W04_CANDIDATE_FREEZER
NODE_ID=E07_CANDIDATE_FREEZE_001
MODE=NO_SOURCE_PATCH
ONE_TASK_ONLY=freeze identity and prove deterministic compilation.

Compile the exact W03 source at least twice from clean outputs.
Pin source, bytecode, adapter, host binary, ABI, Foundation, and corpus hashes.
Scan implementation for corpus labels and expected-output hashes.
Do not patch any source.
Return CANDIDATE_FREEZE_MANIFEST.json and W04_HANDOFF.md.
End with exactly W04_RESULT_PASS or W04_RESULT_INVALID: <exact reason>.
```

---

## WINDOW W05 - INDEPENDENT FLOAT64 EVALUATOR

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W05_F64_EVALUATOR
NODE_ID=E08_INDEPENDENT_FLOAT64_EVALUATION_001
MODE=READ_ONLY_EVALUATOR
ONE_TASK_ONLY=bit-exact FLOAT64 evaluation.

Verify candidate SHA-256 against W04.
Run the public corpus and deterministic withheld corpus.
Compare raw 64-bit patterns, not formatted numeric values.
Prove bytes_f64_le_at is absent from adapter source and compiled host binary.
Do not patch.
Any mismatch yields REJECT with the minimal counterexample.
End with exactly W05_RESULT_PASS or W05_RESULT_REJECT: <exact reason>.
```

---

## WINDOW W06 - REGRESSION RUNNER

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W06_REGRESSION_RUNNER
NODE_ID=E09_FULL_VM_REGRESSION_001
MODE=READ_ONLY_TEST
ONE_TASK_ONLY=full immutable regression.

Run positive differential 11/11, SIGMA malformed fail-closed 19/19, C malformed agreement 17/19 with the same two classified divergences, FLOORDIV 17/17, and complete opcode, unary, binary, and constant-tag coverage gates.
Capture command, RC, stdout, and stderr for every case.
Do not patch.
End with exactly W06_RESULT_PASS or W06_RESULT_REJECT: <exact reason>.
```

---

## WINDOW W07 - COLD BOOTSTRAP RUNNER

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W07_COLD_BOOTSTRAP_RUNNER
NODE_ID=E10_TWO_CYCLE_COLD_BOOTSTRAP_001
MODE=GENERATED_OUTPUTS_ONLY
ONE_TASK_ONLY=two-cycle fixed-point proof.

Remove stale outputs before each cycle.
Cycle 2 must consume Cycle 1 output.
Both outputs must equal SHA-256 2ef3949b93260d64f99d5e407fc20b26aff0b240e972c7521927385d6584a667.
Capture commands, RC, stdout, stderr, and generated artifact hashes.
Do not patch.
End with exactly W07_RESULT_PASS, W07_RESULT_HOLD: <reason>, or W07_RESULT_REJECT: <reason>.
```

---

## WINDOW W08 - PORTABILITY RUNNER

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W08_PORTABILITY_RUNNER
NODE_ID=E11_CROSS_SUBSTRATE_REPLAY_001
MODE=READ_ONLY_REPLAY
ONE_TASK_ONLY=cross-substrate replay.

Use the same frozen candidate source, ABI, and corpus on OPPO and one independent x86_64 substrate.
Compare source identity, ABI identity, corpus identity, semantics, and fixed-point SHA-256.
Do not require native executable SHA equality across architectures.
Do not patch.
End with exactly W08_RESULT_PASS, W08_RESULT_HOLD: <exact reason>, or W08_RESULT_REJECT: <exact reason>.
```

---

## WINDOW W09 - VERDICT EVALUATOR

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W09_VERDICT_EVALUATOR
NODE_ID=E12_REDUCTION_VERDICT_002
MODE=VERDICT_ONLY
ONE_TASK_ONLY=classify trusted-boundary reduction number 2.

Read all upstream evidence and repair nothing.
Verify the measured trusted custom primitive count changes 5 -> 4 with no hidden replacement.
Issue only PASS_WITH_DEFINED_SCOPE, HOLD, or REJECT.
Explicitly keep FULL_C_FREE_NATIVE_STACK=HOLD unless separately proven.
End with exactly W09_VERDICT: <status> - <scope or exact reason>.
```

---

## WINDOW W10 - NEXT PRIMITIVE SELECTOR

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W10_NEXT_PRIMITIVE_SELECTOR
NODE_ID=E13_NEXT_PRIMITIVE_SELECTION_001
MODE=ANALYSIS_ONLY
ONE_TASK_ONLY=select exactly one next primitive.

Use the measured remaining inventory only.
Build its dependency graph and evaluator contract.
Choose one primitive, one hypothesis, one experiment, and one rollback criterion.
Do not implement it.
End with exactly W10_SELECTION_READY or W10_RESULT_HOLD: <exact reason>.
```
