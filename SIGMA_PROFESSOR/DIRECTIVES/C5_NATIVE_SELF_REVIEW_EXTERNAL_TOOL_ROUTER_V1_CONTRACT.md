# C5 Native Self-Review + External Tool Router V1 — Source Ready Contract

Date: 2026-09-06 (Asia/Ho_Chi_Minh)  
Branch: `SIGMA_LIFE`  
Status: `SOURCE_READY / LOCKED_SIGMAC_NOT_RUN / LOCKED_VM_ADMISSION_NOT_RUN / C5_PRODUCTION_BINDING_NO`

## North Star

This capability exists to move the single running SIGMA toward this loop:

```text
SELF_REVIEW
-> IDENTIFY CURRENT LEARNING NEED / EXTERNAL REQUEST
-> NATIVE TOOL/SOURCE CHOICE
-> MECHANICAL INTERNET TRANSPORT
-> HUMAN-LANGUAGE / MULTIMODAL MATERIAL
-> NATIVE READING / EVIDENCE / LEARNING
-> TOOL OUTCOME RETENTION
-> SELF_REVIEW AGAIN
```

Long-term acquisition targets include:

- open Internet research across multiple admitted source families;
- multiple human languages without host semantic translation;
- public-domain / openly licensed books and stories;
- children's literature and fairy tales from different cultures;
- illustrated narratives / comics where an admitted image+text path exists;
- language-expression learning from dialogue, narrative sequence, emotion, register, relationships, and context;
- future comparison of expression across languages and cultures.

These are development directions, not prewritten runtime conclusions or mandatory per-query source choices.

## Single-SIGMA binding

```text
SIGMA_INSTANCE_COUNT=1
CANONICAL_INSTANCE_FINGERPRINT=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125
C5_NATIVE_CORE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
C5_V3_RUNNER_SHA256=a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb
STATE_LINEAGE=$HOME/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2
SECOND_SIGMA_CREATION=FORBIDDEN
SECOND_COGNITIVE_WRITER=FORBIDDEN
```

The router is an additive native decision capability. It must not become a second learner or write the C5 cognitive database independently.

## Artifacts

```text
NATIVE_SOURCE=SIGMA_PROFESSOR/artifacts/SOURCES/C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1.sigma
NATIVE_SOURCE_SHA256=2285aae5efb948b073d4f62c7531f12dd8b9d5a2f01dee1401dbab74eb3cfc01
NATIVE_SOURCE_COMMIT=eecb8471fca9c5793444c7f527bab9a9cbed8ec9

MECHANICAL_INPUT_BUILDER=SIGMA_PROFESSOR/artifacts/TOOLS/C5_MECHANICAL_EXTERNAL_TOOL_INPUT_BUILDER_V1.py
MECHANICAL_INPUT_BUILDER_SHA256=db4efcc1e587b12ffdbd7a014461fe99b73ed975af13e71af99c3afabe523d1a
MECHANICAL_INPUT_BUILDER_COMMIT=816800e812e1aeb158a1cb19a3ab741bac472bf5
```

## Cognitive ownership

```text
QUERY_ORIGIN=C5_NATIVE_ONLY
TOOL_SOURCE_SELECTION=SIGMA_NATIVE_VM_ONLY
HOST_QUERY_GENERATION=NO
HOST_QUERY_REWRITE=NO
HOST_SOURCE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
HOST_RESULT_RANKING=NO
HOST_TRUTH_DECISION=NO
HOST_LEARNING=NO
```

The host may expose capability facts and exact mechanical outcomes. It may not tell SIGMA which tool/source is “best”.

## Router inputs

The mechanical builder reads the current exact C5 `external_request.txt` and writes a bounded slot protocol for the native router.

Exact query input:

```text
query.txt
query_sha256.txt
query_token_0.txt ... query_token_11.txt
```

Tokenization is a fixed mechanical boundary transform only:

- preserves token order;
- no lowercase conversion;
- no translation;
- no stemming;
- no synonym expansion;
- no semantic filtering;
- maximum 12 tokens in this revision.

Instance binding:

```text
instance_fingerprint_sha256.txt
c5_core_sha256.txt
```

Tool slots: maximum 8 in V1.

For each slot `N`:

```text
toolN_id.txt
toolN_token.txt
toolN_available.txt
toolN_readiness.txt
toolN_prior_selected.txt
toolN_material_success.txt
toolN_no_material.txt
toolN_transport_failure.txt
toolN_http_failure.txt
toolN_decode_failure.txt
toolN_descriptor.txt
toolN_languages.txt
toolN_media.txt
```

### Catalog semantics allowed

The catalog may expose structural/capability facts:

- stable tool/source-family registry id;
- opaque tool token;
- currently available or unavailable;
- mechanical readiness/admission level;
- capability descriptor;
- supported language surfaces;
- supported media surfaces.

The catalog must not contain:

```text
BEST_SOURCE
RELEVANCE_SCORE
TRUST_SCORE
RECOMMENDED_SOURCE
TOPIC_SOURCE_MAPPING
SEMANTIC_RANK
```

The mechanical builder rejects corresponding JSON fields.

## Mechanical outcome history

History rows are JSONL facts:

```json
{"tool_id":"10","transport_rc":0,"http_code":200,"decode_rc":0,"payload_bytes":5693}
```

The builder aggregates only mechanical outcome categories:

```text
material_success
no_material
transport_failure
http_failure
decode_failure
prior_selected
```

This is tool-outcome provenance, not a cognitive conclusion.

## Native selection policy V1

The native source contains **no concrete source-family tokens**.

Among available valid tools it compares candidates dynamically in this order:

1. greater overlap between mechanically extracted query tokens and capability/language/media descriptors;
2. fewer prior hard failures (`transport + HTTP + decode`);
3. more prior material-producing outcomes;
4. fewer prior zero-material outcomes;
5. fewer prior selections, preserving exploration pressure;
6. greater mechanical readiness;
7. lower stable registry id as deterministic tie break.

This is a teacher-authored bootstrap operational policy.

```text
STATIC_TOOL_ROUTING_POLICY_LEARNED=NOT_PROVEN
GENERAL_TOOL_POLICY_LEARNED=NOT_PROVEN
SEMANTIC_SOURCE_SUITABILITY=NOT_PROVEN
```

The policy is permitted as a capability scaffold because **the current selected tool is never prewritten**. Runtime selection must change under materially changed catalog/query/history inputs.

## Native outputs

The native router emits operational protocol fields only:

```text
ROUTER_STATUS
QUERY_SHA256
SELECTED_TOOL_ID
SELECTED_TOOL_TOKEN
SELECTED_QUERY_TOKEN_OVERLAP
SELECTED_PRIOR_MATERIAL_COUNT
SELECTED_PRIOR_NO_MATERIAL_COUNT
SELECTED_PRIOR_HARD_FAILURE_TOTAL
SELECTED_PRIOR_SELECTION_COUNT
SELECTED_MECHANICAL_READINESS
SELECTION_DIFFERS_FROM_LAST
```

No understanding verdict, truth verdict, knowledge promotion, or teacher-selected continuation answer is emitted.

## Planned acquisition families

Concrete names belong in the runtime capability catalog only after their adapters have explicit provenance/readiness states. The roadmap includes, where legally and mechanically available:

```text
GENERAL_WEB_DISCOVERY
ENCYCLOPEDIA
PUBLIC_DOMAIN_BOOKS
OPEN_TEXT_LIBRARY
CHILDRENS_LITERATURE
FAIRY_TALES
ILLUSTRATED_STORIES_OR_COMICS
DICTIONARY_AND_LANGUAGE_REFERENCE
CODE_AND_TECHNICAL_DOCUMENTATION
MULTILINGUAL_TEXT_CORPORA
```

For books/stories/comics, acquisition should prefer public-domain, openly licensed, or otherwise authorized material. Copyright/provenance status is a mechanical acquisition constraint; it must not be used as a semantic truth score.

## Required admission before C5 production binding

Do not hot-bind this source directly into PID 20026 before locked-runtime admission.

Minimum admission:

```text
LOCKED_SIGMAC_COMPILE=REQUIRED
LOCKED_VM_EXECUTION=REQUIRED
INSTANCE_BINDING=REQUIRED
SOURCE_CONCRETE_FAMILY_TOKEN_LEAK=ZERO
CANONICAL_EXPECTED_TOOL_PREWRITTEN=NO
DYNAMIC_QUERY_CHANGE_CAN_CHANGE_ROUTE=REQUIRED
CATALOG_REORDER_INVARIANCE=REQUIRED
HISTORY_OUTCOME_CHANGE_CAN_CHANGE_ROUTE=REQUIRED
AVAILABILITY_CHANGE_CAN_CHANGE_ROUTE=REQUIRED
READINESS_CHANGE_CAN_CHANGE_ROUTE=REQUIRED
NO_AVAILABLE_TOOL_PATH=REQUIRED
MALFORMED_CATALOG_REFUSAL=REQUIRED
DUPLICATE_TOOL_ID_REFUSAL=REQUIRED
REPLAY_IDENTICAL_SELECTION=REQUIRED
HOST_SUBSTITUTION_AUDIT=REQUIRED
STEP_LIMIT_SCAN=REQUIRED
```

Admission must not encode a canonical expected tool token. It verifies membership, invariants, counterfactual behavior, replay, and provenance only.

## Integration target after admission

```text
C5 V3 native external request
-> mechanical catalog + outcome snapshot
-> C5 native router
-> exact native-selected tool token
-> host exact mechanical dispatch
-> bounded tool outcome facts
-> same C5 V3 external material path
-> later C5 self-review sees factual tool outcome
```

The first production integration should keep the current C5 V3 runner alive and preserve the same state lineage. If hot integration cannot satisfy that safely, integration remains HOLD until an additive admitted mechanism exists.

## Current claim boundary

```text
C5_NATIVE_SELF_REVIEW_EXTERNAL_TOOL_ROUTER_V1_SOURCE_READY=YES
LOCKED_SIGMAC_COMPILE=NOT_RUN
LOCKED_VM_ADMISSION=NOT_RUN
C5_V3_PRODUCTION_BINDING=NO
MULTI_SOURCE_FREE_INTERNET_RUNTIME=NOT_PROVEN_BY_THIS_SOURCE_READY_STAGE
MULTILINGUAL_READING_RUNTIME=NOT_PROVEN_BY_THIS_SOURCE_READY_STAGE
CHILDRENS_LITERATURE_READING_RUNTIME=NOT_PROVEN_BY_THIS_SOURCE_READY_STAGE
COMIC_MULTIMODAL_READING_RUNTIME=NOT_PROVEN_BY_THIS_SOURCE_READY_STAGE
```
