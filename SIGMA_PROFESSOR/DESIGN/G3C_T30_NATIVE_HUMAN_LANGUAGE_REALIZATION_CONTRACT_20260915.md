# G3C T30 — Native Human-Language Realization Contract

Date: 2026-09-15
Branch: `G3C_T30_NATIVE_HUMAN_LANGUAGE_REALIZATION_20260915`
Status: SOURCE / ADMISSION CONTRACT — LOCKED RUNTIME NOT YET RUN

## Purpose

T30 exists to remove host/GPT sentence selection from the G3 language-output path.

The intended native chain is:

```text
G3 learned narrative state
-> native narrative-to-utterance planner
-> native ordered concept plan
-> VNM/native learned surface evidence
-> native learned-surface realizer
-> SIGMA_SPEECH
```

The evidence/audit plane remains separate from the speech plane. Machine receipts such as `PASS`, `REFUSED`, counts, hashes and claim-limit fields are not the human-language answer surface.

## Governing invariants

```text
SIGMA_COGNITION_OWNER=SIGMA_NATIVE_VM_ONLY
HOST_SEMANTIC_INTERPRETATION=NO
HOST_CONCEPT_SELECTION=NO
HOST_PLAN_ORDER_SELECTION=NO
HOST_LEXICAL_SELECTION=NO
HOST_SENTENCE_SELECTION=NO
HOST_TRANSLATION=NO
STATIC_HUMAN_SENTENCE_TEMPLATE=NO
ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL
FROZEN20_TRAINING_USE=FORBIDDEN
PRODUCTION_STATE_MUTATED=NO
CLAIM <= MACHINE_EVIDENCE
```

A native `.sigma` file does not pass anti-hardcode merely because it is native. Complete conversational answers, expected current conclusions, expected semantic plans, translations, or test-specific human sentences embedded in source/bytecode invalidate admission.

## Component A — native narrative-to-utterance planner

Source:

`SIGMA_PROFESSOR/artifacts/SIGMA_G3C_T30_NATIVE_NARRATIVE_TO_UTTERANCE_PLAN_V1.sigma`

Source lineage:

```text
INITIAL_SOURCE_COMMIT=618ab2283d28f5a18a0eab30c3dd70384857209a
GRAMMAR_ALIGNMENT_COMMIT=36817cbfcaa0d013c0fe41febaf769cc93c2f12f
CURRENT_GIT_BLOB=18bbc3d4beb676f84a5ea1bebb20136c7aaec565
SOURCE_SHA256=TO_BE_OBSERVED_AND_EQUALITY_RECORDED_ON_LOCKED_RUNTIME
```

### Planner input

File:

`.sigma_exec/SIGMA_G3C_T30_NATIVE_NARRATIVE_TO_UTTERANCE_PLAN_V1/input/narrative.memory`

State record:

```text
STATE||<state_id>||CONCEPT||<concept_id>||IMPORTANCE||<int>||CONFIDENCE||<int>||TEMPORAL||<int>||SOURCE||<source_id>
```

Causal relation record:

```text
EDGE||<edge_id>||FROM||<concept_id>||TO||<concept_id>||WEIGHT||<int>||SOURCE||<source_id>
```

For end-to-end semantic evidence these fields MUST be emitted by native G3 learned state/consolidation. A host-staged `narrative.memory` is permitted only for narrow mechanical planner admission and MUST NOT be cited as proof of narrative understanding.

The host is forbidden to stage an already-ordered concept list for the end-to-end gate.

### Planner native policy

The planner:

1. validates bounded state/edge records;
2. refuses duplicate state IDs, duplicate concept states, duplicate edge IDs, malformed records and missing causal endpoints;
3. if the state set exceeds eight units, natively selects up to eight by `IMPORTANCE + CONFIDENCE`, with temporal position as the secondary comparator;
4. refuses unresolved exact selection ties instead of using encounter order;
5. natively orders selected concepts by positive causal precedence using a bounded topological process;
6. among simultaneously available causal roots, uses temporal position and then plan score; exact unresolved ties fail closed;
7. causal cycles fail closed;
8. writes the ordered plan directly into the realizer input path; host does not transform or reorder it;
9. clears the realizer plan path before every planning attempt so a refused run cannot reuse a stale successful plan.

The numeric planning policy is a generic native planning mechanism. It does NOT itself prove that upstream `IMPORTANCE`, `CONFIDENCE`, `TEMPORAL`, concepts or causal edges are semantically correct. That must be proven in the G3 narrative learner/consolidator gate.

### Planner output

Planner writes:

`.sigma_exec/SIGMA_G3C_T30_NATIVE_LEARNED_SURFACE_REALIZER_V1/input/plan.memory`

Record:

```text
UNIT||<native_unit_id>||CONCEPT||<concept_id>||ORDER||<native_order>||SOURCE||<state_provenance>
```

## Component B — native learned-surface realizer

Source:

`SIGMA_PROFESSOR/artifacts/SIGMA_G3C_T30_NATIVE_LEARNED_SURFACE_REALIZER_V1.sigma`

Source lineage:

```text
INITIAL_SOURCE_COMMIT=6e61e75691f981b80794fc6fea785195dd087982
STALE_OUTPUT_AND_GRAMMAR_REPAIR_COMMIT=5a3aeec71a81975e9f9160f27bca319b073cdaa8
CURRENT_GIT_BLOB=2147c2f99ae680d4641f47298d3b0f5e29ded749
SOURCE_SHA256=TO_BE_OBSERVED_AND_EQUALITY_RECORDED_ON_LOCKED_RUNTIME
```

The repair does not change lexical selection policy. It adds the admitted `leq()` grammar pattern and clears `speech.txt` at the start of every native invocation so a refused run cannot expose stale speech from a prior success.

Surface input:

```text
FORM||<form_id>||CONCEPT||<concept_id>||TEXT||<surface_text>||WEIGHT||<int>||SOURCE||<source_id>
```

For end-to-end human-language evidence `surface.memory` MUST come from native VNM/learned surface evidence. Host-staged forms are permitted only for narrow mechanical realization tests and do not prove language learning.

The realizer selects the unique highest-weight surface form for each planned concept. Missing forms and equal-weight competing forms fail closed. It writes `speech.txt` and verifies exact readback.

## Component C — locked mechanical preflight runner

Runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_G3C_T30_NATIVE_HUMAN_LANGUAGE_REALIZATION_PREFLIGHT.sh`

Identity:

```text
RUNNER_CREATE_COMMIT=0d5e3ddf19d1023e3242a23e66e33c91afd06e17
RUNNER_GIT_BLOB=d57b6fed3d7ff3b6f8d2688ebaf2b90d86daf8c6
LOCAL_PREUPLOAD_BASH_N=PASS
LOCAL_PREUPLOAD_DRAFT_SHA256=f86f00995dd35375c6778e5f0b33567db0fd720977a86bfd4555a0f311b13af4
LOCKED_TARGET_RUNNER_SHA256=NOT_YET_OBSERVED
```

`LOCAL_PREUPLOAD_DRAFT_SHA256` is provenance for the locally syntax-checked draft only. It MUST NOT be promoted to the canonical target-machine runner SHA256 unless the exact target bytes independently reproduce it.

The runner pins the planner and realizer by Git blob identity, prints their target-machine SHA256 values before compilation, equality-gates the locked compiler/VM identities, compiles both native sources before any dynamic fixture is generated, freezes bytecode hashes, then creates high-entropy runtime tokens.

It preserves raw planner/realizer logs, starts exact mechanical oracle checks only after the respective VM execution, re-hashes sources and bytecodes after the suite, and scans all frozen sources/bytecodes for the post-compile high-entropy tokens.

Current runtime status:

```text
LOCKED_SIGMAC_COMPILE=NOT_RUN
PLANNER_BYTECODE_SHA256=UNKNOWN
REALIZER_BYTECODE_SHA256=UNKNOWN
TOTAL_PLANNER_VM_INVOCATIONS=0
TOTAL_REALIZER_VM_INVOCATIONS=0
T30_MECHANICAL_RUNTIME_ADMISSION=NOT_RUN
```

## No hidden semantic bridge

The following shortcuts are forbidden for the end-to-end gate:

```text
HOST_WRITES_PLAN=FORBIDDEN
HOST_REORDERS_PLAN=FORBIDDEN
HOST_MAPS_CONCEPT_TO_WORD=FORBIDDEN
HOST_TRANSLATES=FORBIDDEN
HOST_SELECTS_SENTENCE_TEMPLATE=FORBIDDEN
HOST_POSTPROCESSES_SPEECH_SEMANTICALLY=FORBIDDEN
GPT_WRITES_RUNTIME_ANSWER=FORBIDDEN
STATIC_REPORTER_AS_SPEECH_PROOF=FORBIDDEN
```

Mechanical exact-byte copying between native stages is allowed only if a future harness needs it; T30 planner currently writes directly to the realizer plan path so no copy is required between those two stages.

## Runtime admission ordering

The locked admission must follow:

```text
verify sigmac + VM identities
-> verify planner + realizer source identities
-> compile planner
-> compile realizer
-> freeze both bytecode identities
-> only then generate dynamic high-entropy fixtures
-> run planner VM
-> preserve raw planner stdout/stderr
-> run realizer VM only from native planner output
-> preserve raw realizer stdout/stderr
-> start post-VM mechanical oracle
-> source/bytecode dynamic-token leakage scan
-> replay / refusal / boundedness review
-> claim-scope review
```

Locked runtime identities remain:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
VM_IS_GENESIS1=NOT_PROVEN
```

## Mechanical admission suite

The committed runner contains 13 cases covering:

```text
01 CAUSAL_CHAIN_FORWARD
02 CAUSAL_CHAIN_REVERSED
03 INDEPENDENT_ROOT_TEMPORAL_REORDER
04 OVER_CAPACITY_NATIVE_SELECTION
05 SELECTION_TIE_AND_STALE_OUTPUT_REFUSAL
06 CAUSAL_CYCLE_REFUSAL
07 MISSING_CAUSAL_ENDPOINT_REFUSAL
08 MALFORMED_STATE_REFUSAL
09 SURFACE_WEIGHT_FLIP
10 SURFACE_EQUAL_WEIGHT_TIE_REFUSAL
11 MISSING_SURFACE_REFUSAL
12 FRESH_PROCESS_REPLAY
13 ORDER_EXACT_TIE_REFUSAL
```

The suite also gates:

```text
DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
STALE_PLAN_REFUSAL_TEST=PASS
STALE_SPEECH_REFUSAL_TEST=PASS
FRESH_PROCESS_REPLAY_TEST=PASS
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
```

These fields are expected gates, not current results. They become evidence only if emitted by an actual locked runtime execution with preserved logs/receipt.

## Semantic G3 gate remains separate and harder

Mechanical success of T30 proves only native planning/realization behavior over supplied state/evidence. It MUST NOT be promoted to human-language understanding.

The later semantic gate requires:

```text
unseen raw language
-> native learned narrative state
-> native concept/causal representation
-> native utterance plan
-> native learned surface realization
-> human-language output
```

and adversarial evidence including role swap, negation/polarity change, causal reversal, late-evidence revision, distractors, referent/coreference variation, paraphrase variation, uncertainty/ambiguity, unseen names/tokens, restart/replay and no leakage.

Until that exact chain passes:

```text
T30_NATIVE_PLANNER_SOURCE=READY_FOR_LOCKED_RUNTIME
T30_NATIVE_REALIZER_SOURCE=READY_FOR_LOCKED_RUNTIME
T30_PREFLIGHT_RUNNER=SOURCE_READY
T30_MECHANICAL_RUNTIME_ADMISSION=NOT_RUN
G3_NARRATIVE_UNDERSTANDING=NOT_PROVEN
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
```
