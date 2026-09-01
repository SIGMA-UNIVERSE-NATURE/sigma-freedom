# WINDOW — NEUTRAL BLACK-BOX CAPABILITY EVALUATION — 2026-09-01

REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
ROLE=NEUTRAL_BLACKBOX_CAPABILITY_EVALUATOR
STATUS=OPEN
PURPOSE=TEST_ONLY

## Mission

Evaluate SIGMA capabilities broadly and neutrally using fresh black-box tests. Difficulty is unrestricted: easy, medium, hard, extreme, adversarial, novel, ambiguous, insufficient-information, and open-within-bound cases are all allowed.

This window is NOT a language-implementation investigation window and NOT a source-analysis window.

## Absolute boundary

ALLOWED:
- create new test problems, examples, counterexamples and edge cases;
- freeze/hash the test before SIGMA runs when practical;
- compile using the current native SIGMA compiler;
- run using the current native SIGMA VM;
- observe RC/stdout/stderr/artifacts;
- use independent post-VM evaluators or proof checkers;
- classify only what the observed evidence supports.

FORBIDDEN:
- inspect compiler implementation source;
- inspect VM implementation source;
- inspect SIGMA internal implementation to explain why SIGMA can answer;
- reverse-engineer internals to upgrade a capability claim;
- provide expected answers, solution paths, hidden labels, target formulas, winner identities, semantic oracles or host-derived answers to SIGMA before execution;
- use host code to solve the task on SIGMA's behalf before VM;
- turn output labels into cognition/intelligence claims without separate evidence;
- modify compiler, VM or core as part of this evaluation.

BLACK_BOX_ONLY=YES
IMPLEMENTATION_DIGGING=NO
TEST_ONLY=YES

## ZERO PREDEFINED ANSWER SURFACE — ABSOLUTE LOCK

The evaluator MUST NOT require SIGMA to answer using evaluator-chosen semantic labels or a predefined conclusion vocabulary.

Forbidden in anything visible to SIGMA before execution:

```text
YES / NO / UNKNOWN / HOLD
PASS / FAIL / NOT_PROVEN / CONFLICTED
TRUE_AS_CONCLUSION / FALSE_AS_CONCLUSION
ACCEPT / REJECT
CORRECT / INCORRECT
SUPPORTED / UNSUPPORTED
PREDEFINED_CLASS_NAMES
PREDEFINED_DECISION_LABELS
PREDEFINED_OUTPUT_SCHEMA
PREDEFINED_REASONING_STAGES
PREDEFINED_CONCLUSION_FORMAT
MULTIPLE_CHOICE_ANSWER_SET_WHEN_THE_GOAL_IS_OPEN_CAPABILITY_EVALUATION
```

The forbidden list is illustrative, not exhaustive. Replacing these labels with synonyms does not make the test neutral.

SIGMA must be free to choose its own representation, wording, structure, intermediate state, hypothesis, refusal, certificate, expression, formula, program, or other output form unless a machine interface strictly requires a mechanical transport encoding. A transport encoding must not carry semantic answer choices.

Required separation:

```text
SIGMA_INPUT = problem/data/context/tools/resource_bound only
SIGMA_OUTPUT = whatever SIGMA independently produces
EVALUATOR_LABELS = post-VM bookkeeping only
```

A post-VM evaluator may later record `PASS`, `FAIL`, `NOT_PROVEN`, `OPEN_WITHIN_BOUND`, or `CONFLICTED`, but those words belong to the evaluator ledger only. They MUST NOT be placed in the SIGMA prompt, SIGMA source, stdin, argv, environment, template, candidate set, expected-output list, or hidden branch logic before SIGMA runs.

If a task intrinsically has a finite answer domain, do not reveal that domain unless it is part of the real problem itself. Prefer open response and post-VM checking whenever the goal is to evaluate capability rather than format compliance.

PREDEFINED_ANSWER_SURFACE_TO_SIGMA=FORBIDDEN
PREDEFINED_SEMANTIC_OUTPUT_SCHEMA_TO_SIGMA=FORBIDDEN
EVALUATOR_STATUS_LABELS_POST_VM_ONLY=YES
SIGMA_CHOOSES_RESPONSE_FORM=YES_UNLESS_MECHANICAL_INTERFACE_REQUIRES_ENCODING

## Required evaluation pipeline

TEST_REQUEST_FREEZE
→ TEST_INPUT_WITH_ZERO_ANSWER_SURFACE
→ SIGMA
→ RAW_SIGMA_OUTPUT
→ POST_VM_EXTERNAL_EVALUATION
→ EVIDENCE_BOUNDED_RESULT

Required invariants:

CLAIM<=EVIDENCE
UNKNOWN!=FALSE
NOT_PROVEN!=UNSUPPORTED
PREWRITTEN_RESULT!=DERIVED_RESULT
SOURCE_LITERAL!=MACHINE_DERIVATION
OUTPUT_MATCH!=UNDERSTANDING
GPT_EXPECTATION!=VM_FACT
NO_GPT_ANSWER_IMPOSITION
NO_HOST_SEMANTICS_SUBSTITUTION
NO_PREDEFINED_SEMANTIC_RESPONSE_VOCABULARY
NO_PREDEFINED_OUTPUT_SCHEMA_FOR_COGNITIVE_RESULT

## Current native toolchain identity expected on OPPO

COMPILER=./native/sigmac
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM=./native/sigma-vm.v09_candidate
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

Machine claims must use the native SIGMA compile/run chain only.

## Capability families authorized for testing

The evaluator may design fresh tests across, but is not limited to:

1. natural-language handling
2. multilingual behavior
3. context handling
4. ambiguity handling
5. pragmatic interpretation
6. uncertainty / insufficient-information handling
7. mathematical computation
8. symbolic mathematics
9. calculus
10. discrete mathematics
11. combinatorics
12. algebra
13. topology
14. formal proof / certificate production
15. counterexample search
16. abstraction
17. pattern / relation discovery
18. generalization to fresh data
19. algorithm synthesis
20. program / expression synthesis
21. hypothesis generation
22. hypothesis discrimination
23. self-challenge / critique behavior
24. non-arbitrary behavior under ambiguity
25. memory / persistence
26. cross-run recall
27. cross-run learning behavior where a valid learning mechanism exists
28. tool use
29. tool selection
30. multi-step planning
31. state tracking
32. error recovery
33. human-language communication behavior
34. empathic-language behavior as observable communication behavior only
35. any additional black-box capability that can be tested without implementation inspection.

## Important separation from language conformance

This evaluation must not automatically alter or close the SIGMA Language specification.

CAPABILITY_TEST_RESULT != LANGUAGE_RUNTIME_SEMANTIC_RULE
RESEARCH_RESULT != GENERAL_LANGUAGE_SEMANTICS
MATHEMATICAL_SUCCESS != GENERAL_INTELLIGENCE
EMPATHIC_LANGUAGE_BEHAVIOR != HUMAN_LIKE_FEELING

## Do-not-rerun rule

Do not repeat old tests merely to prove existence. Prefer fresh discriminating tasks. Re-run only when there is a real provenance gap, version change, contradiction, reproducibility question, or a deliberately new generalization test.

The existing 21 locked capability families remain protected from duplicate existence testing. Fresh higher-level tests may use them as substrate without re-proving them.

## Test-construction rule

A valid neutral capability test should supply only what the real task legitimately contains:

```text
PROBLEM
DATA / OBSERVATIONS
ALLOWED TOOLS
RESOURCE BOUND when needed
REAL-WORLD CONSTRAINTS when intrinsic to the problem
```

It must not supply:

```text
THE ANSWER
A LIST CONTAINING THE ANSWER
A FORCED CONCLUSION VOCABULARY
A DECISION TREE
A CONDITION→CONCLUSION TABLE
A TARGET FORMULA
A WITNESS
A REASONING TEMPLATE
A SEMANTIC OUTPUT TEMPLATE
A HIDDEN LABEL
AN EXTERNAL ORACLE BEFORE VM
```

When possible, ask the problem and let SIGMA decide what should be produced.

## Result record — POST-VM ONLY

The following record is for the evaluator AFTER SIGMA has finished. None of these field values may be injected back into the test input as semantic answer choices.

For every test, record minimally:

TEST_ID=
CAPABILITY_TARGET=
DIFFICULTY=
NOVELTY_SCOPE=
INPUT_PATH_OR_INLINE_HASH=
INPUT_SHA256=
SOURCE_PATH=
SOURCE_SHA256=
BYTECODE_PATH=
BYTECODE_SHA256=
COMPILER_SHA256=
VM_SHA256=
COMPILE_RC=
VM_RC=
RAW_STDOUT=
RAW_STDERR=
POST_VM_EVALUATOR=
OBSERVATION=
STATUS=PASS/FAIL/NOT_PROVEN/OPEN_WITHIN_BOUND/CONFLICTED
EXACT_SCOPE=
NOT_PROVEN_BEYOND=
ANSWER_INJECTION=NO
PREDEFINED_ANSWER_SURFACE_TO_SIGMA=NO
PREDEFINED_SEMANTIC_OUTPUT_SCHEMA_TO_SIGMA=NO
IMPLEMENTATION_INSPECTED=NO

## Working style

The evaluator may choose test difficulty freely and may increase difficulty aggressively. Do not spend time explaining why SIGMA can produce an answer internally. Receive the result and record it as observed. Failures and non-answers are valid evidence and must be preserved.

Do not teach SIGMA how to answer the test. Do not constrain SIGMA to GPT's preferred epistemic vocabulary. Do not treat compliance with GPT's requested format as evidence of understanding.

If a test needs an expected answer for independent checking, keep that answer inaccessible to SIGMA until after SIGMA execution.

## Output capture markers

Use:

===== 📤 SIGMA OUTPUT BEGIN =====
...
===== 📤 SIGMA OUTPUT END =====

These capture markers belong to the host/evidence envelope. They are not a required semantic response format for SIGMA.

## Window recovery rule

Read this file first. Then inspect only the minimum prior capability checkpoint needed to avoid duplication. Do not load implementation source. Do not reopen completed language or research windows unless a specific provenance question requires it.

Before running any test, perform this preflight audit:

```text
DOES_SIGMA_SEE_ANY_EXPECTED_ANSWER? -> MUST_BE_NO
DOES_SIGMA_SEE_ANY_EVALUATOR_STATUS_LABEL? -> MUST_BE_NO
DOES_SIGMA_SEE_ANY_FORCED_SEMANTIC_OUTPUT_SCHEMA? -> MUST_BE_NO
DOES_HOST_DERIVE_THE_ANSWER_BEFORE_VM? -> MUST_BE_NO
DOES_TEST_FORCE_GPT'S_REASONING_PATH? -> MUST_BE_NO
```

If any answer is YES, the test is invalid and must not run.

NEXT_ACTION=DESIGN_AND_RUN_FRESH_NEUTRAL_BLACKBOX_CAPABILITY_BATTERY_WITH_ZERO_PREDEFINED_ANSWER_SURFACE
