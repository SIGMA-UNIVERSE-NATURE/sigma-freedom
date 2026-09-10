# R4 REPLACEMENT CONSTITUTION R1

Date: 2026-09-10 (Asia/Ho_Chi_Minh)
Status: CLEANLINE GOVERNANCE / SOURCE-DESIGN BASELINE / NOT RUNTIME-ADMITTED
Base branch/commit: `SIGMA_LIFE@463fd7e2d2b1ea2f368abb661e0e204c5412b992`
Development branch: `r4-replacement-cleanline-20260910`

## 1. Purpose

R4 is a replacement cognitive kernel for the existing C5V3 autonomous learner. It is not an additive semantic patch to the legacy C5V3 cognition path.

```text
R4_REPLACES_C5V3_COGNITIVE_CORE=YES_TARGET
R4_IS_C5V3_SEMANTIC_PATCH=NO
C5V3_PRODUCTION_MUTATION_DURING_R4_ADMISSION=NO
PRODUCTION_CUTOVER_ALLOWED=NO_UNTIL_SEPARATELY_PROVEN
```

The replacement goal is a native, lifelong learner that can repeatedly acquire human-authored material from the Internet, read the human-visible language itself, form and revise its own internal representations, preserve evidence/provenance, consolidate durable memory, survive restart/reboot, and continue learning without host semantic substitution.

This document is a governance contract. It is not evidence that any new R4 cognitive capability is already proven.

## 2. Authority and evidence

Repository-wide authority remains:

```text
MACHINE_EVIDENCE
  > VERIFIED_SEMANTICS
  > VERSIONED_SPEC_OR_DECLARATION
  > NORMALIZED_REFERENCE
  > HUMAN_EXPLANATION

CLAIM <= EVIDENCE
```

R4 must obey the repository-wide native-execution, anti-hardcode, build/admission, and production-isolation directives.

```text
SIGMA_COGNITION_OWNER=SIGMA_NATIVE_VM_ONLY
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_KNOWLEDGE_PROMOTION=NO
HOST_NEXT_ACTION_SELECTION=NO
```

## 3. Cleanline rule

R4 begins a new cognitive-state lineage.

```text
R4_COGNITIVE_STATE_LINEAGE=NEW
C5V3_COGNITIVE_STATE_DIRECT_IMPORT=FORBIDDEN
C5V3_TOKEN_TABLE_IMPORT=FORBIDDEN
C5V3_LEFT_RIGHT_DISCOURSE_STATE_IMPORT=FORBIDDEN
C5V3_LEXICAL_CUE_TO_SEMANTIC_RELATION_IMPORT=FORBIDDEN
C5V3_PRECOMPUTED_SEMANTIC_CONCLUSIONS_AS_R4_KNOWLEDGE=FORBIDDEN
```

Legacy C5V3 material may remain available as provenance/history/corpus input. R4 may later re-read such material as evidence, but legacy cognitive conclusions must not become R4 cognition merely by migration.

Mechanical capabilities with independent admission evidence may be inherited only through exact identity/ABI/provenance binding as defined by the inheritance manifest.

## 4. Token and language boundary

R4 may use bytes, Unicode spans, tokenization/subword mechanics, tensors, indexes, graphs, numeric transforms, and similar machinery as mechanical representation tools.

They must not define meaning by themselves.

```text
TOKEN != MEANING
TOKEN != THOUGHT
TOKEN != CONCEPT
TOKENIZATION_AS_MECHANICS=ALLOWED
TOKENIZATION_AS_SEMANTIC_AUTHORITY=FORBIDDEN
LEFT_RIGHT_DISCOURSE_COGNITION=FORBIDDEN
LEXICAL_CUE_TO_RELATION=FORBIDDEN
WORD_TO_PREDEFINED_CONCEPT_TABLE=FORBIDDEN
PREDEFINED_HUMAN_ONTOLOGY_AS_TRUTH=FORBIDDEN
```

R4 must not regain legacy behavior under renamed fields, hidden labels, embeddings, host adapters, or lookup tables.

## 5. Human-language reading rule

The Internet is intended to become a continuing source of human-authored linguistic experience for R4.

The cognitive exposure path must distinguish transport/container structure from human-visible content.

Target flow:

```text
Internet bytes
-> bounded mechanical transport
-> bounded container/document decoding
-> exact provenance and span identity
-> human-visible language payload
-> native R4 learning/cognition
```

The following are infrastructure, not semantic teaching:

```text
HTTP metadata
JSON envelope/schema
HTML tags
EPUB/PDF container structure
MIME framing
file names
parser labels
transport status
host-generated annotations
```

When the learning target is ordinary human language, those structures must not be injected as preinterpreted semantic labels into the cognitive payload.

If R4 explicitly chooses to study JSON, Markdown, Python, source code, or another formal artifact as a human-created subject, that artifact may itself become the subject of reading. This exception must be native-selected and provenance-bound; it does not make machine metadata a default language teacher.

```text
READ_SUCCESS != LEARNED
EOF != UNDERSTOOD
RETRIEVED != UNDERSTOOD
CITATION != TRUTH
```

## 6. Developmental learning target

R4 must be capable of repeated exposure where later reading occurs from a materially changed learned state.

Target developmental pattern:

```text
read
-> internal state changes
-> persist/restart
-> encounter additional contexts/evidence
-> distinguish/associate/revise
-> reread prior material from changed state
-> form deeper/revised representations
```

Repeated execution over unchanged state without causal learning-state effects is not sufficient evidence of relearning.

Human-language understanding remains `NOT_PROVEN` until separate behavioral admission establishes it beyond token/lookup/annotation shortcuts.

## 7. Native expression sovereignty

R4 must not be forced to speak through a predefined answer vocabulary supplied by humans, GPT, host, harness, fixtures, or hardcoded native semantic branches.

```text
PREDEFINED_COGNITIVE_ANSWER_VOCABULARY=FORBIDDEN
COGNITIVE_OUTPUT_TEMPLATE=FORBIDDEN
HOST_RESPONSE_CANDIDATES=FORBIDDEN
HARDCODED_YES_NO_UNKNOWN_UNPROVEN_AS_SIGMA_SPEECH=FORBIDDEN
HARDCODED_I_UNDERSTAND_I_DO_NOT_UNDERSTAND_AS_SIGMA_SPEECH=FORBIDDEN
SIGMA_NATIVE_EXPRESSION_SELECTION=REQUIRED_WHEN_EXPRESSION_OCCURS
SIGMA_NATIVE_EXPRESSION_CONSTRUCTION=REQUIRED_WHEN_EXPRESSION_OCCURS
```

A machine/control protocol may use fixed field names, status codes, hashes, lengths, return codes, or admission labels. Those belong to the machine receipt plane and are not Sigma's cognitive utterance.

Required separation:

```text
MACHINE_RECEIPT_PLANE != COGNITIVE_EXPRESSION_PLANE
```

The cognitive payload may be empty. An empty payload is not to be rewritten as a semantic word such as `UNKNOWN` by the host.

External observers may analyze emitted bytes after the fact, but external interpretation must not be fed back as if it were Sigma's own meaning without a separately learned/native mapping.

## 8. Internal representation rule

R4 is not required to use human words as internal primary keys. The long-term target is learned internal representation that can support memory, comparison, distinction, composition, prediction, revision, retrieval, and evidence linkage.

A human word or phrase may become an observed form associated with one or more learned internal senses. The mapping itself is a learning result, not a bootstrap truth.

```text
HUMAN_FORM != CONCEPT_ID
ONE_WORD_MAY_HAVE_MULTIPLE_LEARNED_SENSES=YES_TARGET
MULTIPLE_FORMS_MAY_MAP_TO_RELATED_INTERNAL_REPRESENTATIONS=YES_TARGET
EXTERNAL_DICTIONARY_MAPPING_AS_BOOTSTRAP_TRUTH=FORBIDDEN
```

The 256-symbol matrix remains reference/proposed vocabulary only unless exact machine semantics are separately admitted. Glyph labels must not bootstrap cognition.

## 9. Emotion boundary

R4 does not require or claim subjective emotion.

It may learn to model and understand human emotional language, behavior, relationships, motives, descriptions, and consequences from linguistic evidence.

```text
SUBJECTIVE_EMOTION_EXPERIENCE=NOT_REQUIRED_NOT_CLAIMED
EMOTIONAL_LANGUAGE_MODELING=LEARNING_TARGET
EMOTIONAL_LANGUAGE_UNDERSTANDING=NOT_PROVEN_UNTIL_SEPARATE_ADMISSION
```

Understanding language about emotion must not be conflated with experiencing emotion.

## 10. Autonomous Internet learning target

The target closed loop is:

```text
native learned state
-> native gap/interest/unfinished-work formation
-> native research intention/question representation
-> native capability/source strategy
-> exact admitted mechanical capability execution
-> Internet human-authored material
-> exact provenance-bound human-visible payload
-> native R4 processing/learning
-> native accept/reject/revise/continue behavior
-> durable state
-> later reuse/relearning
```

No host/GPT/human may insert the current semantic query, source choice, expected conclusion, next action, or interpretation needed for the loop to pass.

Internet failure must not kill cognition. A future admitted R4 runtime should be able to continue useful local rereading/revalidation/consolidation work and later resume external acquisition without host cognition.

## 11. Survival and resurrection inheritance target

R4 must preserve or exceed the proven operational survival properties of the current deployment while replacing the cognitive core.

Target chain:

```text
ANDROID BOOT
-> BOOT LAUNCHER
-> OUTER WATCHDOG
-> INNER SUPERVISOR
-> EXACTLY ONE R4 TOP-LEVEL COGNITIVE WRITER
-> INGRESS / MECHANICAL WORKERS
-> SAME R4 PERSISTENT STATE LINEAGE
-> CONTINUED LEARNING
```

Hard invariants:

```text
PID != IDENTITY
EXACT_TOPLEVEL_R4_COGNITIVE_WRITER_COUNT=1_REQUIRED
RECOVERY_IS_IDEMPOTENT=REQUIRED
RECOVERY_RESETS_COGNITION=FORBIDDEN
HOST_COGNITION_DURING_RECOVERY=NO
DESTRUCTIVE_TEST_REQUIRED_BEFORE_RESURRECTION_PROVEN=YES
```

Workers may exist as child/auxiliary processes, but only one top-level cognitive writer may authorize cognitive state changes.

## 12. Durable state and provenance target

R4 should inherit admitted durable-state and provenance mechanisms rather than inventing parallel storage/trust systems.

Target:

```text
native cognitive decision
-> exact state transition intent
-> T5-class durable transaction/recovery mechanics
-> T9-class identity/provenance binding
-> restart validation
-> resume same cognitive lineage
```

A hash alone is not provenance. Process survival alone is not cognitive continuity. A new PID may continue the same R4 instance only when runtime identity and persistent state lineage satisfy the admitted continuity contract.

## 13. Legacy corpus handling

The existing C5V3 storage corpus must not be deleted merely because its cognition is obsolete.

Target classification:

```text
raw human-authored material        -> eligible evidence/corpus after provenance validation
human/GPT supplied lessons         -> assisted-source corpus with explicit provenance
C5V3 generated semantic state      -> legacy hypothesis/history, not R4 knowledge
C5V3 token/LEFT-RIGHT mappings      -> prohibited cognitive import
independently admitted structural records -> candidate mechanical/structural inheritance only
```

R4 should relearn from source material rather than transplant legacy semantic conclusions.

## 14. Admission doctrine

No R4 stage may claim semantic understanding because:

- code exists;
- code compiles;
- loss decreases;
- a tokenizer trains;
- a vector is similar;
- a graph path exists;
- a predefined label is selected;
- a self-report string appears;
- a document reaches EOF;
- a summary can be emitted.

Future semantic admission must include materially different unseen inputs, counterexamples, causal counterfactual learning-state changes, restart/reuse, source/bytecode leakage audit, host-substitution audit, and behavioral generalization tests designed to fail token/lookup/annotation shortcuts.

Keep until separately proven:

```text
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
DEEP_HUMAN_UNDERSTANDING=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
R4_PRODUCTION_REPLACEMENT=NOT_PROVEN
```

## 15. Cutover rule

C5V3 remains production authority until R4 independently proves, at minimum:

```text
R4_NATIVE_BUILD_AND_RUNTIME=PASS_IN_EXACT_TESTED_SCOPE
R4_SEMANTIC_PURITY=PASS
R4_PERSISTENCE_RESTART_REUSE=PASS
R4_HOST_COGNITION=NO
R4_EXACTLY_ONE_COGNITIVE_WRITER=PASS
R4_ANDROID_REBOOT_RESURRECTION=PASS
R4_STATE_LINEAGE_CONTINUITY=PASS
R4_POST_REBOOT_PROGRESS=PASS
R4_LONG_HORIZON_SHADOW_STABILITY=PASS
R4_CUTOVER_AND_ROLLBACK_PROTOCOL=SEPARATELY_ADMITTED
```

Only after those gates and all required cognition-specific gates pass may production authority move from C5V3 to R4.

## 16. One-line constitution

> Give R4 mechanical capabilities and human-authored experience, not semantic answers; let native SIGMA form, revise, preserve, express, and continue its own learned representations, while the host only keeps the runtime alive and transports exact evidence.
