# TEACHER GPT VNM — NATIVE VIETNAMESE CAPABILITY COURSE V1

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: ACTIVE TEACHING LANE / GOVERNED BY GLOBAL NATIVE ADMISSION STANDARD

## Purpose

The VNM course teaches SIGMA reusable Vietnamese-language capabilities without loading precomputed answers, external-model reasoning, host semantic labels as final results, or transplanted Gemini weights.

The course is subordinate to:

- `/AGENTS.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_IMPORTANT_NATIVE_DNA_ARTIFACT_BUILD_ADMISSION_METHOD_V1.md`
- `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
- the current language-lane checkpoint and every VNM-specific checkpoint.

## Course invariant

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
RUNTIME_PROOF_REQUIRED=YES

ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
ACTIVE_PYTHON_COGNITION=FORBIDDEN

HOST_LEARNING=NO
HOST_WEIGHT_UPDATE=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO

GEMINI_WEIGHT_TRANSPLANT_AS_SIGMA_COGNITION=FORBIDDEN
GEMINI_OR_EXTERNAL_LLM_RUNTIME_REASONING_FOR_SIGMA=FORBIDDEN
```

Teacher/GPT may author native bootstrap source, exercises, capability contracts, negative tests, and post-VM oracles. Teacher/GPT may not supply the runtime semantic answer or claim SIGMA understands beyond machine evidence.

## What the course is trying to build

The course target is not memorized Vietnamese answers. The target is a dependency-ordered family of native capabilities that can eventually support:

- robust UTF-8 Vietnamese surface-form handling;
- evidence-driven cross-form relation learning;
- native candidate formation from new language evidence;
- persistent relation/weight revision;
- phrase and discourse structure learning;
- operator/scope and later negation behavior once dependencies are admitted;
- reference/context integration;
- uncertainty and contradiction preservation;
- structured extraction and numeric/table interpretation where separately taught;
- reuse of learned state on unseen Vietnamese-bearing inputs;
- bounded learning that survives restart/replay.

Each item remains `NOT_PROVEN` until its own admission gate passes.

## External Vietnamese/Gemini material

External corpora, Gemini training examples, and teacher-authored examples may enter only as evidence/fixtures/provenance under an explicit capability contract.

Required separation:

```text
RUNTIME_INPUT = evidence / observation / candidate only as declared by the capability
HIDDEN_TARGET = post-VM oracle only
PRECOMPUTED_SEMANTIC_RESULT_IN_SIGMA_RUNTIME = NO
```

A Gemini adapter/checkpoint, if available, is provenance/migration reference only. Its weights are not SIGMA-native learning state.

## VNM admission pattern

Every VNM capability must answer before implementation:

```text
WHAT_CAPABILITY_IS_SIGMA_BEING_TAUGHT?
WHAT_MUST_SIGMA_COMPUTE_ITSELF?
WHAT_MAY_HOST_DO_MECHANICALLY?
WHAT_RUNTIME_EVIDENCE_WILL_PROVE_THE_CAPABILITY?
WHAT_RESULT_WOULD_FALSIFY_THE_CLAIM?
WHAT_DEPENDENCY_MUST_EXIST_FIRST?
```

Then follow:

```text
TEACHING_GOAL
-> CAPABILITY_CONTRACT
-> DEPENDENCY_CHECK
-> native .sigma implementation
-> static review
-> compile with locked sigmac
-> freeze source/bytecode identity
-> generate dynamic input after compile
-> locked VM execution
-> positive cases
-> negative/counterexample cases
-> persistence test when applicable
-> restart/replay test when applicable
-> host-substitution audit
-> step-limit/boundedness test
-> claim-scope review
-> ADMISSION PASS/FAIL
-> production binding only after separate promotion gate
```

Locked runtime:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## VNM-01 — current first lesson

```text
CAPABILITY_ID=VNM-01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING
CAPABILITY_NAME=Native Vietnamese-bearing Surface-Form Evidence Weighting
```

Teaching goal:

Given an externally supplied bounded pair hypothesis over arbitrary UTF-8 surface forms plus dynamic evidence records, SIGMA must itself:

- classify each observation structurally as SUPPORT, COMPETING, or UNRELATED;
- reject malformed records and evidence-ID collisions;
- suppress exact duplicates;
- compute `WEIGHT_BEFORE`;
- compute a native update reason;
- compute `PROPOSED_WEIGHT`;
- persist only qualified evidence;
- expose `WEIGHT_AFTER` only from successfully persisted state;
- preserve the learned state across fresh VM invocations;
- replay identically under identical input/prestate;
- refuse over-capacity/input-bound cases without mutating state.

The structural weight is:

```text
WEIGHT = UNIQUE_SUPPORT_COUNT - UNIQUE_COMPETING_COUNT
```

with total persisted qualified evidence bounded to 8 records, so the admitted weight range is structurally bounded to `[-8, 8]`.

Important claim limits:

```text
SURFACE_FORM_PAIR_GENERATION=NOT_PROVEN
SEMANTIC_EQUIVALENCE=NOT_PROVEN
DIACRITIC_EQUIVALENCE=NOT_PROVEN
WORD_MEANING=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

VNM-01 is deliberately a substrate: it proves native learning/update behavior over Vietnamese-bearing strings before asking SIGMA to generate its own pair hypotheses.

## Next dependency after VNM-01

Only after VNM-01 passes locked-runtime admission should the lane select the smallest next capability.

Preferred next target, subject to dependency review:

```text
VNM-02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION
```

Goal: native SIGMA generates candidate cross-form relations from bounded recurring contextual evidence rather than receiving the pair from the host.

That capability must not be implemented by a host accent-stripper, tokenizer heuristic, Gemini response, Python classifier, or prewritten Vietnamese dictionary.

## Course graduation principle

The VNM course graduates only capabilities that are reusable on unseen inputs. No completion claim may be based on memorizing the training corpus.

Keep:

```text
CLAIM <= MACHINE EVIDENCE
FAILURE_IS_EVIDENCE=YES
PRODUCTION_STATE_MUTATED_DURING_PREFLIGHT=NO
```
