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

## Required evaluation pipeline

TEST_REQUEST_FREEZE
→ TEST_INPUT
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
24. refusal of arbitrary choice under ambiguity
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

## Result format

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
IMPLEMENTATION_INSPECTED=NO

## Working style

The evaluator may choose test difficulty freely and may increase difficulty aggressively. Do not spend time explaining why SIGMA can produce an answer internally. Receive the result and record it as observed. Failures and non-answers are valid evidence and must be preserved.

If a test needs an expected answer for independent checking, keep that answer inaccessible to SIGMA until after SIGMA execution.

## Output capture markers

Use:

===== 📤 SIGMA OUTPUT BEGIN =====
...
===== 📤 SIGMA OUTPUT END =====

## Window recovery rule

Read this file first. Then inspect only the minimum prior capability checkpoint needed to avoid duplication. Do not load implementation source. Do not reopen completed language or research windows unless a specific provenance question requires it.

NEXT_ACTION=DESIGN_AND_RUN_FRESH_NEUTRAL_BLACKBOX_CAPABILITY_BATTERY
