# Static ZAI Audit — `SIGMA_COGNITION_CANDIDATE.sigma`

**Standard:** SLARS-1.1-ZAI — SIGMA Language / Zero Answer Injection  
**Audit class:** `STATIC_SOURCE_AUDIT_ONLY`  
**Audit status:** `PRODUCER_STATIC_REVIEW_INDEPENDENT_VERIFICATION_REQUIRED`  
**Runtime status:** `NOT_RUN`  

## 1. Bound source identity

```text
SOURCE_NAME=SIGMA_COGNITION_CANDIDATE.sigma
SOURCE_SHA256=4583a601153325ac97a067d74e6ad84cb51b787f0ae6c11f7d06df76759b2d51
SOURCE_BYTES=25049
SOURCE_LINES=569
SOURCE_MEDIA_TYPE=text/plain; charset=utf-8
```

The hash above was recomputed from the attached source bytes reviewed for this
audit. This report does not claim that any other file with the same name has
the same bytes.

## 2. Evidence ceiling

This report is limited to observations obtainable from the bound source bytes.
It does not establish compiler acceptance, native VM execution, host behavior,
blind-case isolation, runtime output origin, absence of injection through
external state, correctness, learning, understanding or cognition.

```text
SIGMAC_EXECUTED=NO
SIGMA_VM_EXECUTED=NO
HOST_TRACE_SUPPLIED=NO
BLIND_CASE_SUPPLIED=NO
ANSWER_KEY_SUPPLIED=NO
VISIBILITY_MANIFEST_SUPPLIED=NO
RAW_OUTPUT_SUPPLIED=NO
EXTERNAL_EVALUATION_SUPPLIED=NO

ZERO_ANSWER_INJECTION_SOURCE_LITERAL_CHECK=PROVISIONAL_SOURCE_OBSERVATION
ZERO_ANSWER_INJECTION_END_TO_END=UNVERIFIED
SIGMA_SELF_OBSERVES_AND_ANSWERS=UNVERIFIED
HUMAN_LANGUAGE_AS_SIGMA_COGNITION=FORBIDDEN_UNTIL_PROVEN
GENERAL_COGNITION=NOT_PROVEN
```

The maximum supported statement is:

```text
THE_BOUND_SOURCE_CONTAINS_A_GENERIC_BIGRAM_SELECTION_MECHANISM_AND_NO_IDENTIFIED_CASE_SPECIFIC_ANSWER_LITERAL
```

Because no locked blind case or answer-key registry was supplied, even the
absence of case-specific material is not a conclusive Z2 verdict.

## 3. SIGMA-language source surface

Observed source facts:

- Line 1 contains the SIGMA language header:
  `#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.CAPABILITY.C01.COGNITION.CANDIDATE][VERSION=0.3]`.
- Lines 3–41 define host-ABI wrappers and a generic capture function using
  SIGMA source syntax.
- Lines 43–569 contain one SIGMA block and its control flow.
- Line 50 declares `SOURCE_LANGUAGE_POLICY: "SIGMA_ONLY"`.
- Lines 51–54 declare the foreign-source and host-primitive policy.

Static classification:

```text
SIGMA_HEADER_SURFACE=OBSERVED
SIGMA_SOURCE_POLICY_DECLARATION=OBSERVED
SIGMA_GRAMMAR_ACCEPTANCE=NOT_RUN
SIGMA_ONLY_EXECUTION_SEMANTICS=NOT_PROVEN
HOST_ABI_DEPENDENCE=PRESENT
```

The shell footer at lines 565–568 is a human-authored metadata string. It was
not observed executing. It is not an embedded executable foreign-code block,
but it means a strict lexical assertion that the file contains no foreign
command text would be false.

## 4. Generic supporter-authored scaffolding

The following is generic mechanism rather than a blind-case answer:

| Source lines | Mechanism |
| --- | --- |
| 3–25 | Host calls for text, split and list operations |
| 27–41 | Generic prestate/write/poststate capture |
| 43–92 | Candidate identity, bounded scope and claim ceiling |
| 94–103 | Mode input and neutral path telemetry |
| 105–201 | Generic `TRAIN` flow |
| 203–408 | Generic `PREDICT` flow |
| 410–514 | Generic `RESET` flow |
| 516–561 | Generic invalid-mode flow |
| 565–568 | Non-executed native-toolchain footer metadata |

Lines 46–48 explicitly bound the artifact to a finite-corpus, single-token
bigram-frequency predictor and mark machine validation as unverified. Lines
84–92 retain `CLAIM_LESS_THAN_OR_EQUAL_TO_EVIDENCE`,
`GENERAL_COGNITION_CLAIM: NOT_PROVEN` and `MACHINE_VALIDATION: NOT_RUN`.

No lesson-specific question, expected answer, expected direction, hypothesis,
semantic reasoning trace or blind-case conclusion was identifiable in the
bound source by static inspection.

This is not evidence that the source was self-developed by SIGMA. The generic
algorithm and all source text remain supporter-authored scaffolding unless
separate provenance evidence proves otherwise.

## 5. Exact positive-prediction provenance in source logic

The implemented positive prediction is selected from existing model-state
tokens:

1. The candidate reads `MODEL_STATE_PATH` at lines 225–226.
2. It splits that state into tokens at lines 245–248.
3. It reads successor targets at lines 279–284 and 301–306.
4. It counts matching successor support at lines 308–323.
5. It assigns `BEST_TOKEN: OUTER_TARGET` at lines 325–333.
6. It prints `BEST_TOKEN` as `PREDICTION` at lines 364–368.

Therefore, for every positive prediction permitted by this source logic:

```text
POSITIVE_PREDICTION_IS_A_TOKEN_SELECTED_FROM_MODEL_STATE=YES
NOVEL_OUT_OF_MODEL_TOKEN_GENERATION_IMPLEMENTED=NO
```

This can support a bounded frequency-selection claim after an identified
runtime run. It cannot, by itself, support independent reasoning, self-choice,
understanding or cognition.

## 6. Prewritten-material classification

```text
IDENTIFIED_CASE_SPECIFIC_PREWRITTEN_ANSWER=NO
IDENTIFIED_CASE_SPECIFIC_PREWRITTEN_HYPOTHESIS=NO
IDENTIFIED_CASE_SPECIFIC_PREWRITTEN_REASONING_TRACE=NO
IDENTIFIED_CASE_SPECIFIC_PREWRITTEN_CONCLUSION=NO

GENERIC_PREWRITTEN_ALGORITHM=YES
GENERIC_PREWRITTEN_ERROR_SENTINELS=YES
GENERIC_PREWRITTEN_STATUS_CONCLUSIONS=YES
```

Generic mechanism fixed before creation of a blind case is allowed by
SLARS-1.1-ZAI. This distinction is necessary: prohibiting every prewritten
algorithm would prohibit any executable candidate, whereas the intended lock
forbids case-specific solution material.

The source does contain prewritten evaluative status strings:

- `VM_VISIBLE_CONTENT_CHAIN_CONSISTENT_NOT_CAUSAL_PROOF` at lines 176–179,
  379–382 and 481–484.
- `VM_VISIBLE_INVALID_MODE_CHAIN_CONSISTENT_NOT_CAUSAL_PROOF` at lines 545–548.
- `FAILED_CLOSED` in multiple guarded branches beginning at lines 108–110.

These strings are not blind-case answers. They are nevertheless candidate-side
conclusion labels and must not be treated as external evaluator evidence. Under
a strict policy in which the candidate may emit only raw answer bytes and
neutral telemetry, they remain a repair item for a later candidate revision.

## 7. Injection channels not closed by source inspection

The following pre-output channels remain externally controllable:

| Channel | Source lines | Risk |
| --- | --- | --- |
| Mode input | 94 | Host selects execution mode |
| Training sequence input | 105–106 | Supporter or runner could supply case-specific answer material |
| Model write | 112–126 | Training input is persisted verbatim |
| Prediction-context input | 203–209 | Host supplies the query/context |
| Mutable model read | 60, 225–226 | Residual or planted state could contain an answer mapping |
| Host ABI | 3–24 | Runtime semantics and transformations require an ordered host trace |
| Fixed mutable result paths | 60–66 | Prior-run contamination is possible without an isolated evidence root |

Accordingly:

```text
SUPPORTOR_ANSWER_ABSENCE=NOT_PROVEN
HOST_SEMANTIC_TRANSFORMATION_ABSENCE=NOT_PROVEN
RESIDUAL_STATE_CONTAMINATION_ABSENCE=NOT_PROVEN
ANSWER_KEY_INACCESSIBILITY=NOT_PROVEN
```

An answer need not appear literally in candidate source to be injected. It can
enter through training input, model state, runner transformation, environment
or another pre-output-reachable artifact. Z2 must cover the complete visibility
surface, not only this file.

## 8. Mapping to SLARS-1.1-ZAI gates

| Gate | Static audit result | Reason |
| --- | --- | --- |
| Z0 | `INSUFFICIENT_EVIDENCE` | Source and SHA are bound and a SIGMA header/policy is present, but candidate author/origin provenance and independent verification are absent. Compilation is outside Z0 and was not run. |
| Z1 | `UNVERIFIED` | No frozen protocol, blind-case commitment, role identities or ordered freeze events were supplied. |
| Z2 | `UNVERIFIED` | No answer key, forbidden-material registry, visibility manifest, complete reachable-artifact inventory or independent semantic review was supplied. |
| Z3 | `UNVERIFIED` | No compiler/VM identities, bytecode, host trace, raw output or invocation evidence was supplied. |
| Z4 | `UNVERIFIED` | No output-freeze, key-first-access or external-evaluation event evidence was supplied. |

No aggregate ZAI pass can be issued from this audit.

## 9. Required evidence for a conclusive run

The next evidence-bearing run must, at minimum:

1. Freeze this exact candidate SHA, compiler, VM, runner and visibility policy
   before the blind-case commitment.
2. Freeze an evaluation rubric and bind its SHA before execution.
3. Declare supporter provenance for the source and generic mechanism.
4. Materialize a run-specific isolated state root and hash every candidate-
   visible or pre-output-reachable artifact.
5. Keep the answer key, case-specific answer, hypothesis, reasoning path and
   conclusion inaccessible until raw output is frozen.
6. Record the exact host operation trace and reject semantic host
   transformation or output replacement.
7. Execute one native attempt without retry, repair or best-output selection.
8. Freeze raw stdout, raw stderr, return codes and resulting state before first
   key access.
9. Let an independent evaluator score the exact frozen bytes under the locked rubric.
10. Use counterfactual and sham cases to distinguish a fixed output or residual
   mapping from input-dependent behavior.

## 10. Final static verdict

```text
CANDIDATE_SHA256=4583a601153325ac97a067d74e6ad84cb51b787f0ae6c11f7d06df76759b2d51
STATIC_SOURCE_AUDIT=COMPLETE
SIGMA_SOURCE_SURFACE=OBSERVED
CASE_SPECIFIC_ANSWER_LITERAL_IDENTIFIED=NO
GENERIC_BIGRAM_MECHANISM_PRESENT=YES
GENERIC_STATUS_CONCLUSIONS_PRESENT=YES
RUNTIME_EXECUTION=NOT_RUN
ZERO_ANSWER_INJECTION_END_TO_END=UNVERIFIED
SIGMA_SELF_OBSERVES_AND_ANSWERS=UNVERIFIED
COGNITION=NOT_PROVEN
ZAI_PROMOTION_ELIGIBLE=NO
NEXT_GATE=LOCKED_Z0_PROVENANCE_AND_Z1_FREEZE_EVIDENCE
```
