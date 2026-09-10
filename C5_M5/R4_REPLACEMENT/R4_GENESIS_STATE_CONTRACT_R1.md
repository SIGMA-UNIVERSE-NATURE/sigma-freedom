# R4 GENESIS STATE CONTRACT R1

Date: 2026-09-10 (Asia/Ho_Chi_Minh)
Status: CLEANLINE STATE CONTRACT / NOT RUNTIME-ADMITTED
Development branch: `r4-replacement-cleanline-20260910`

## 1. Purpose

Define the first persistent state of the R4 replacement cognitive lineage without importing legacy C5V3 semantic state and without preloading human-language meaning, answer vocabulary, ontology, or forced cognitive utterances.

```text
R4_GENESIS_IS_NEW_LINEAGE=YES
R4_GENESIS_IMPORTS_C5V3_SEMANTIC_MEMORY=NO
R4_GENESIS_PRELOADS_HUMAN_DICTIONARY=NO
R4_GENESIS_PRELOADS_SEMANTIC_ONTOLOGY=NO
R4_GENESIS_PRELOADS_RESPONSE_VOCABULARY=NO
```

This contract defines storage/identity boundaries. It does not claim that cognition, language understanding, curiosity, or autonomous research is already implemented.

## 2. Genesis principle

The initial persistent R4 state contains only what is required for safe identity, continuity, bounded capability access, provenance, and the ability to accumulate native-learned state.

It must not contain the semantic result of future learning.

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
LOAD_SEMANTIC_ANSWERS=NO
LOAD_LEGACY_COGNITIVE_CONCLUSIONS=NO
```

## 3. State-plane separation

R4 persistent state is divided conceptually into four planes:

```text
A. IDENTITY / LINEAGE PLANE
B. CAPABILITY / EXECUTION BINDING PLANE
C. EXPERIENCE / PROVENANCE REFERENCE PLANE
D. NATIVE-LEARNED COGNITIVE PLANE
```

Only plane D is cognition. A/B/C are trust/mechanical substrate.

The host may mechanically store or transport A/B/C exact fields when allowed by admitted T5/T9-class mechanisms. The host must never synthesize plane-D meaning.

## 4. Plane A — identity / lineage

Minimum conceptual fields:

```text
R4_STATE_FORMAT_VERSION
R4_LINEAGE_ID
R4_STATE_REVISION
R4_PARENT_STATE_ID_OR_NONE
R4_COMMITTED_STATE_ID
RUNTIME_IDENTITY_BINDING
CREATED_RECEIPT_ID
LAST_COMMIT_RECEIPT_ID_OR_NONE
```

Requirements:

```text
PID_IS_IDENTITY=NO
STATE_LINEAGE_IS_PERSISTENT=YES_TARGET
PARENT_BINDING_REQUIRED_AFTER_FIRST_COMMIT=YES
HASH_ALONE_IS_PROVENANCE=NO
```

A restarted R4 process must bind to the same admitted lineage rather than create a new cognitive identity merely because PID changed.

## 5. Plane B — capability / execution bindings

Genesis may know that exact mechanical capabilities exist only through an admitted capability registry/binding record.

Minimum conceptual fields:

```text
CAPABILITY_REGISTRY_ID
CAPABILITY_REGISTRY_RECEIPT
BOUND_RUNTIME_PROFILE_ID
BOUND_RESOURCE_PROFILE_ID
```

The registry contains mechanical capability identity/ABI/admission metadata. It must not contain a semantic answer, current query, current source choice, or current next action.

```text
CAPABILITY_AVAILABLE != CAPABILITY_SELECTED
CAPABILITY_AVAILABLE != CAPABILITY_LEARNED
HOST_CAPABILITY_SELECTION=NO
```

R4 cognitive adoption/use of a capability requires separate native behavior evidence.

## 6. Plane C — experience / provenance references

Genesis begins with no learned semantic conclusions.

It may later accumulate exact references to experiences such as human-visible source spans, documents, executions, observations, and other provenance-bound artifacts.

The reference plane may contain mechanical identity such as:

```text
SOURCE_ID
WORK_ID
DOCUMENT_ID
SPAN_OR_PAYLOAD_ID
CONTENT_ID
PROVENANCE_RECEIPT_ID
ACQUISITION_RECEIPT_ID
```

These identities do not define meaning.

```text
SOURCE_ID != TOPIC
SPAN_ID != CLAIM
DOCUMENT_ID != UNDERSTANDING
FILE_EXTENSION != SEMANTIC_CLASS
```

No host-generated `PERSON`, `CAUSE`, `TOPIC`, `INTENT`, `IMPORTANT`, `SUPPORT`, `CONTRARY`, or equivalent semantic annotation is permitted in the ordinary human-language cognitive payload merely because the host/parser can infer it.

## 7. Plane D — native-learned cognitive state

At genesis this plane is empty except for versioned empty-container identity required by the storage format.

Conceptual contents that may emerge later only from native R4 learning include:

```text
learned representations
learned associations
learned distinctions
learned reusable structures
learned internal senses
learned relational structures
learned memory links
learned research/unfinished-work state
learned expression mappings
```

The contract deliberately does not prescribe human semantic names or a fixed human ontology for those internal objects.

At genesis:

```text
LEARNED_REPRESENTATION_COUNT=0
PREDEFINED_CONCEPT_COUNT=0
PREDEFINED_SENSE_COUNT=0
PREDEFINED_WORD_TO_MEANING_COUNT=0
PREDEFINED_RELATION_SEMANTICS_COUNT=0
PREDEFINED_HUMAN_LANGUAGE_RESPONSE_COUNT=0
```

Machine-format metadata needed to serialize empty containers is not counted as cognitive meaning.

## 8. Human-language exposure contract

When R4 is learning ordinary human language, the cognitive input must be the exact human-visible linguistic material selected/bound for reading, plus only mechanically necessary boundaries/identity kept outside the semantic payload.

Target separation:

```text
EXPERIENCE_RECEIPT:
  source/work/document/span/provenance/resource fields

COGNITIVE_INPUT_PAYLOAD:
  exact human-visible bytes/text selected for native exposure
```

Forbidden default injection into cognitive payload:

```text
HTML_ELEMENT_ROLE_AS_MEANING
JSON_FIELD_ROLE_AS_MEANING
FILE_EXTENSION_AS_MEANING
PARSER_GENERATED_POS_TAG
PARSER_GENERATED_NER_TAG
PARSER_GENERATED_DEPENDENCY_LABEL
PARSER_GENERATED_COREFERENCE_LABEL
HOST_SUMMARY
HOST_TRANSLATION
HOST_TOPIC
HOST_INTENT
HOST_SENTIMENT
HOST_TRUTH_LABEL
```

If a formal artifact itself is the native-selected subject of study, its literal human-created syntax may be exposed as source material with provenance. That is different from host metadata teaching meaning.

## 9. Cognitive expression contract

The persistent state must not require Sigma to choose from a predefined semantic utterance set.

Cognitive expression is represented as opaque native-produced bytes plus mechanical identity/length/hash/receipt information.

Conceptual interface:

```text
COGNITIVE_PAYLOAD_BYTES = <native-produced arbitrary bytes or empty>
COGNITIVE_PAYLOAD_LEN   = <mechanical length>
COGNITIVE_PAYLOAD_ID    = <mechanical content identity>
COGNITIVE_PAYLOAD_RECEIPT = <provenance/execution receipt>
```

The envelope may use fixed machine field names. The payload content must not be selected/replaced by the host.

```text
EMPTY_PAYLOAD_ALLOWED=YES
HOST_EMPTY_PAYLOAD_TO_UNKNOWN_TRANSLATION=FORBIDDEN
PREDEFINED_YES_NO_MENU=FORBIDDEN
PREDEFINED_UNDERSTOOD_NOT_UNDERSTOOD_MENU=FORBIDDEN
PREDEFINED_INTELLIGENT_UNINTELLIGENT_MENU=FORBIDDEN
```

External analysis of the payload is observer interpretation, not automatically Sigma's own semantics.

## 10. Bootstrap behavior boundary

Genesis may expose mechanically available human-language material and admitted capabilities to native R4. It must not inject a current semantic query, expected concept, expected answer, or source-ranking conclusion.

The initial environment may provide:

```text
AVAILABLE_EXPERIENCE_RECEIPTS
AVAILABLE_ADMITTED_CAPABILITIES
RESOURCE_BOUNDS
CURRENT_DURABLE_STATE
```

Native R4 must eventually own any claimed decisions about:

```text
what to inspect/read next
what distinctions to retain
what internal representation to create/change
what to revisit
what to request externally
what to express
whether to continue/change strategy
what cognitive state to commit
```

The first implementation may prove only a smaller bounded subset. Unimplemented arrows remain `NOT_PROVEN` rather than being filled by host logic.

## 11. Persistence contract

R4 genesis and all later cognitive commits should use admitted T5-class durable-state mechanics and T9-class identity/provenance binding once exact integration is available.

Target transaction:

```text
native R4 computes candidate state transition
-> native R4 authorizes exact commit intent
-> mechanical durable transaction
-> exact receipt/state-lineage binding
-> restart
-> verify committed state and lineage
-> resume from native state
```

Forbidden:

```text
PROCESS_DIED -> DELETE_COGNITIVE_STATE
PROCESS_DIED -> HOST_RECONSTRUCTS_SEMANTIC_STATE
PROCESS_DIED -> IMPORT_C5V3_SEMANTIC_STATE
```

## 12. Single-writer contract

Only one top-level R4 cognitive writer may authorize plane-D mutation.

```text
EXACT_TOPLEVEL_R4_COGNITIVE_WRITER_COUNT=1_REQUIRED
CHILD_WORKERS_ALLOWED=YES
CHILD_WORKER_COGNITIVE_AUTHORITY=NO_UNLESS_EXACTLY_DELEGATED_BY_NATIVE_PROTOCOL_AND_RETURNED_FOR_SINGLE_WRITER_COMMIT
```

Mechanical workers may fetch/parse/hash/store/compute within admitted capability scopes. Their result is input/evidence; it is not automatically a cognitive-state commit.

## 13. Legacy corpus boundary

The ~30 GB existing Oppo storage must remain outside genesis cognitive state.

It may be indexed/fingerprinted/classified mechanically for future native-selected rereading, but classification must preserve origin and must not turn legacy semantic conclusions into R4 truth.

```text
LEGACY_CORPUS_AVAILABLE_FOR_FUTURE_RELEARNING=YES_TARGET
LEGACY_CORPUS_BULK_LOAD_AS_R4_MEMORY=NO
LEGACY_C5_GENERATED_SEMANTIC_STATE_AS_GENESIS_KNOWLEDGE=NO
```

## 14. Genesis admission tests required before PASS

A future native genesis implementation must at minimum prove:

```text
LOCKED_SIGMAC_IDENTITY=PASS
LOCKED_VM_IDENTITY=PASS
SOURCE_BYTECODE_FREEZE=PASS
GENESIS_STATE_VALIDATION=PASS
GENESIS_HAS_ZERO_PREDEFINED_SEMANTIC_ENTRIES=PASS
C5V3_SEMANTIC_IMPORT_ABSENT=PASS
LEFT_RIGHT_LEXICAL_CUE_IMPORT_ABSENT=PASS
PREDEFINED_RESPONSE_VOCABULARY_ABSENT=PASS
DYNAMIC_OPAQUE_PAYLOAD_BINDING=PASS
EMPTY_COGNITIVE_PAYLOAD_ALLOWED=PASS
HOST_SEMANTIC_SUBSTITUTION=NO
DURABLE_COMMIT_RESTART_REPLAY=PASS_WHEN_T5_T9_BOUND
EXACTLY_ONE_WRITER=PASS_WHEN_SUPERVISOR_BOUND
```

Static source inspection alone is not admission.

## 15. Current claim

```text
R4_GENESIS_STATE_CONTRACT=DEFINED_R1
R4_GENESIS_NATIVE_IMPLEMENTATION=NOT_YET_CREATED_IN_THIS_CONTRACT
R4_GENESIS_RUNTIME_ADMISSION=NOT_RUN
R4_HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
R4_AUTONOMOUS_WEB_LEARNING=NOT_PROVEN
R4_PRODUCTION_BINDING=NO
```
