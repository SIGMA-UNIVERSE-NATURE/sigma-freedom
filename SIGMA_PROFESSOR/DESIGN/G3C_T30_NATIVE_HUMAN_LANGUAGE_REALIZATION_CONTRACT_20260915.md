# G3C T30 — Native Human-Language Realization Contract

Date: 2026-09-15
Branch: `G3C_T30_NATIVE_HUMAN_LANGUAGE_REALIZATION_20260915`
Status: SOURCE / ADMISSION CONTRACT — RUNTIME NOT YET CLAIMED

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

A native `.sigma` file does not pass merely because it is native. Complete conversational answers, expected current conclusions, expected semantic plans, translations, or test-specific human sentences embedded in source/bytecode invalidate admission.

## Component A — native narrative-to-utterance planner

Source:

`SIGMA_PROFESSOR/artifacts/SIGMA_G3C_T30_NATIVE_NARRATIVE_TO_UTTERANCE_PLAN_V1.sigma`

Current source lineage commits:

```text
INITIAL_SOURCE_COMMIT=618ab2283d28f5a18a0eab30c3dd70384857209a
GRAMMAR_ALIGNMENT_COMMIT=36817cbfcaa0d013c0fe41febaf769cc93c2f12f
CURRENT_GIT_BLOB=18bbc3d4beb676f84a5ea1bebb20136c7aaec565
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
8. writes the ordered plan directly into the realizer input path; host does not transform or reorder it.

The numeric planning policy is a generic native planning mechanism. It does NOT itself prove that upstream `IMPORTANCE`, `CONFIDENCE`, `TEMPORAL`, concepts or causal edges are semantically correct. That must be proven in the G3 narrative learner/consolidator gate.

### Planner output

Planner writes:

`.sigma_exec/SIGMA_G3C_T30_NATIVE_LEARNED_SURFACE_REALIZER_V1/input/plan.memory`

Record:

```text
UNIT||<native_unit_id>||CONCEPT||<concept_id>||ORDER||<native_order>||SOURCE||<state_provenance>
```

The planner initializes this path empty before planning so a refused run cannot accidentally reuse a stale successful plan.

## Component B — native learned-surface realizer

Source:

`SIGMA_PROFESSOR/artifacts/SIGMA_G3C_T30_NATIVE_LEARNED_SURFACE_REALIZER_V1.sigma`

Source commit:

`6e61e75691f981b80794fc6fea785195dd087982`

Git blob:

`5e094e7df0c384c51405325ac149f1ff9268e55b`

Surface input:

```text
FORM||<form_id>||CONCEPT||<concept_id>||TEXT||<surface_text>||WEIGHT||<int>||SOURCE||<source_id>
```

For end-to-end human-language evidence `surface.memory` MUST come from native VNM/learned surface evidence. Host-staged forms are permitted only for narrow mechanical realization tests and do not prove language learning.

The realizer selects the unique highest-weight surface form for each planned concept. Missing forms and equal-weight competing forms fail closed. It writes `speech.txt` and verifies exact readback.

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

## Required mechanical admission cases

At minimum:

```text
CAUSAL_CHAIN_FORWARD
CAUSAL_CHAIN_REVERSED
INDEPENDENT_ROOT_TEMPORAL_REORDER
OVER_CAPACITY_NATIVE_SELECTION
SELECTION_EXACT_TIE_REFUSAL
CAUSAL_CYCLE_REFUSAL
MISSING_CAUSAL_ENDPOINT_REFUSAL
MALFORMED_STATE_REFUSAL
STALE_PLAN_CANNOT_SURVIVE_REFUSAL
SURFACE_HIGHER_WEIGHT_SELECTION
SURFACE_WEIGHT_FLIP
SURFACE_EQUAL_WEIGHT_TIE_REFUSAL
MISSING_SURFACE_REFUSAL
FRESH_PROCESS_REPLAY
DYNAMIC_SOURCE_BYTECODE_LEAKAGE_ZERO
STEP_LIMIT_NOT_HIT
```

Dynamic concepts and surface forms should be generated after compile with high entropy. They must not appear in planner source, realizer source or either frozen bytecode artifact.

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
T30_NATIVE_REALIZER_SOURCE=PRESENT
T30_MECHANICAL_RUNTIME_ADMISSION=NOT_RUN
G3_NARRATIVE_UNDERSTANDING=NOT_PROVEN
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
```
