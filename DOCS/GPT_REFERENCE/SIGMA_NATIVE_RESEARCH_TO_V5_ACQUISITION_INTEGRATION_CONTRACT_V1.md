# SIGMA NATIVE RESEARCH -> V5 ACQUISITION INTEGRATION CONTRACT V1

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: DESIGN_LOCKED_NOT_RUNTIME_PROVEN

## Purpose

Unify the already-proven Internet-autonomy research lane with the newer V4/V5 persistent-knowledge and source-adapter work without moving cognition into Bash/host.

This document is an integration contract, not a capability admission.

```text
DIRECT_RUNTIME_INTEGRATION=NOT_YET_PROVEN
INTEGRATION_STATUS=DESIGN_LOCKED_NOT_RUNTIME_PROVEN
CLAIM<=MACHINE_EVIDENCE
```

## Existing proved pieces that must be preserved

### Internet-autonomy lane

Already proved in bounded tested scopes:

```text
SIGMA_NATIVE_REPLAN_TO_FRESH_INTERNET_LOOP=PASS_TESTED_SCOPE
SIGMA_NATIVE_STRATEGY_CONDITIONED_QUERY_ADAPTATION=PASS_TESTED_SCOPE
SIGMA_NATIVE_QUERY_OUTCOME_FEEDBACK_AND_DIVERSITY=PASS_TESTED_SCOPE
SIGMA_NATIVE_COMPARABILITY_GAP_RESEARCH_EXPANSION=PASS_TESTED_SCOPE
SIGMA_NATIVE_GAP_CONDITIONED_FRESH_QUERY_GENERATION_AND_NOVELTY_MEMORY=PASS_TESTED_SCOPE
SIGMA_NATIVE_OUTCOME_CONDITIONED_QUERY_EVOLUTION=PASS_TESTED_SCOPE
SIGMA_NATIVE_NATURAL_LANGUAGE_WEB_RESEARCH_LOOP=PASS_TESTED_SCOPE
SIGMA_NATIVE_COLLECTION_MORE_EVIDENCE_TO_FRESH_WEB_RESEARCH=PASS_TESTED_SCOPE
```

Canonical I2R1 result:

```text
SOURCE_ASSESSMENT_STATE=MORE_EVIDENCE
SIGMA_REPLAN_ACTION=RESEARCH_MORE
FRESH_WEB_COLLECTION_CAUSED_BY_SIGMA_ACTION=PASS_TESTED_SCOPE
HOST_FOLLOWUP_QUERY_GENERATION=NO
HOST_SEMANTIC_EVIDENCE_SELECTION=NO
ZERO_PREWRITTEN_QUERY=YES
ZERO_PREWRITTEN_CONCLUSION=YES
```

### V4 persistent-knowledge chain

Already admitted in exact declared tested scopes:

```text
V4-PK1_PERSISTENT_SEMANTIC_HYPERGRAPH=PASS
V4-PK2_NATIVE_WEIGHT_EVIDENCE=PASS
V4-PK3_EVIDENCE_QUALIFIED_MULTI_HOP_STRUCTURAL_REASONING=PASS
V4-PK4_CONTROLLED_FORMAL_INFERENCE=PASS
V4-PK4_INFERENCE_LIFECYCLE=PASS
V4-PK5_COGNITIVE_VM_BRIDGE_COPY_EXACT=PASS
V4-PK6_VERIFIED_EVOLUTION_SANDBOX_PROFILE=PASS
```

### V5 acquisition protocol/source adapters

Known current state at time of this contract:

```text
V5-K1_EXTERNAL_ACQUISITION_REQUEST_RESPONSE_PROTOCOL=PASS_IN_EXACT_TESTED_SCOPE
V5-K2_WIKIPEDIA_ADAPTER=PASS_IN_EXACT_TESTED_SCOPE
V5-K3_ARXIV_ADAPTER=SOURCE_READY_RUNTIME_NOT_YET_ADMITTED_AT_CONTRACT_TIME
V5-K4_PUBMED_ADAPTER=NOT_YET_ADMITTED
V5-K5_GUTENBERG_ADAPTER=NOT_YET_ADMITTED
V5-K6_PROVENANCE_NORMALIZATION=NOT_YET_IMPLEMENTED_OR_ADMITTED
V5-K7_EVIDENCE_GRAPH_INTEGRATION=NOT_YET_IMPLEMENTED_OR_ADMITTED
```

The status above is historical to this contract date; later checkpoints may supersede individual adapter statuses.

## Critical integration observation

Current exact-fetch adapters are NOT sufficient for autonomous research by themselves.

Examples:

```text
V5-K2_INPUT=SUPPLIED_WIKIPEDIA_PAGE_TITLE
V5-K3_INPUT=SUPPLIED_ARXIV_ID
```

Therefore the following shortcut is forbidden:

```text
I3 research need
-> host chooses Wikipedia/arXiv
-> host chooses page/paper
-> exact fetch adapter
```

That would violate:

```text
HOST_SOURCE_SELECTION=FORBIDDEN
HOST_RESEARCH_GOAL_SELECTION=FORBIDDEN
HOST_KNOWLEDGE_SELECTION=FORBIDDEN
HOST_SEMANTIC_INTERPRETATION=FORBIDDEN
```

## Target unified architecture

```text
V4/V5 EVIDENCE + KNOWLEDGE STATE
        |
        v
I3 SIGMA NATIVE POST-FOLLOWUP OUTCOME EVALUATION
        |
        | native next-research decision
        v
I4 SIGMA NATIVE RESEARCH PLANNER / SOURCE-FAMILY SELECTOR
        |
        | exact native source-search request
        v
SOURCE DISCOVERY ADAPTER
        |
        | host: network + exact protocol decode only
        | no ranking / no semantic selection
        v
SIGMA NATIVE DISCOVERY-CANDIDATE SELECTOR
        |
        | exact resource identity selected by SIGMA
        v
V5 EXACT FETCH ADAPTER
  - Wikipedia exact page/revision
  - arXiv exact paper
  - PubMed exact record
  - Gutenberg exact text/resource
        |
        v
V5-K6 NATIVE/MECHANICAL PROVENANCE NORMALIZATION BOUNDARY
        |
        v
V5-K7 EVIDENCE GRAPH INTEGRATION
        |
        v
V4-PK2 WEIGHT/EVIDENCE + V4-PK4 LIFECYCLE
        |
        v
I3 NEXT OUTCOME EVALUATION CYCLE
```

## Required stages

### Stage A — I3 post-followup outcome evaluation

Goal:

```text
SIGMA consumes:
- prior research state;
- exact fresh collection outcome/state interface;
- persisted research memory when applicable;

SIGMA chooses next action natively.
```

Required boundaries:

```text
NO_GPT_HOST_SEMANTIC_OUTCOME_CLASSIFICATION=YES
NO_PREWRITTEN_NEXT_QUERY=YES
FRESH_COLLECTION_OUTCOME_MUST_BE_BOUND_TO_SIGMA_DECISION=YES
PRIOR_RESEARCH_STATE_AND_OUTCOME_MUST_REMAIN_AVAILABLE_TO_SIGMA=YES
UNKNOWN_REMAINS_UNKNOWN=YES
NO_FIXED_SEMANTIC_CYCLE_LIMIT=YES
```

I3 must be bounded per VM execution. If long history is required, native persistent cursor/resume state must be used instead of unbounded rescans.

### Stage B — I4 native source-family selection

I3 must not directly force a source family unless that decision is part of an admitted native policy.

I4 consumes a native research need/goal plus a mechanically supplied adapter capability catalog.

The adapter catalog may contain only structural/mechanical facts such as:

```text
SOURCE_FAMILY=WIKIPEDIA
CAPABILITY=DISCOVERY,EXACT_FETCH
PROTOCOL=MEDIAWIKI_API
AVAILABLE=YES/NO

SOURCE_FAMILY=ARXIV
CAPABILITY=DISCOVERY,EXACT_FETCH
PROTOCOL=ARXIV_API
AVAILABLE=YES/NO
```

Host MUST NOT attach semantic rankings such as `best source`, `most relevant source`, `trusted for this topic`, or `recommended source`.

SIGMA Native chooses the source family.

### Stage C — source-specific discovery adapters

Current exact-fetch adapters are insufficient when the resource identity is not already known.

Required discovery capabilities include, when developed:

```text
V5-K2D_WIKIPEDIA_DISCOVERY
V5-K3D_ARXIV_DISCOVERY
V5-K4D_PUBMED_DISCOVERY
V5-K5D_GUTENBERG_DISCOVERY
```

A discovery adapter may mechanically:

- transmit an exact SIGMA-generated search request;
- decode returned candidate identifiers/titles/metadata exactly;
- preserve ordering supplied by the remote API only as provenance;
- return the complete bounded candidate set to native SIGMA.

A discovery adapter must NOT:

```text
HOST_QUERY_GENERATION=NO
HOST_RESULT_RANKING=NO
HOST_CANDIDATE_SELECTION=NO
HOST_RELEVANCE_DECISION=NO
HOST_TRUTH_DECISION=NO
```

### Stage D — native discovery-candidate selection

SIGMA Native selects a resource candidate from the mechanically returned bounded candidate set.

Admission must include:

- dynamic candidate sets;
- negative/counterexample cases;
- reordered candidate sets;
- no-result cases;
- malformed candidate protocol refusal;
- replay/idempotency;
- proof that host did not select the candidate;
- boundedness/step-limit testing.

`REMOTE_API_ORDER=PROVENANCE_ONLY`, not semantic truth or preferred choice.

### Stage E — exact-fetch adapter dispatch

Only after native SIGMA has selected:

```text
SOURCE_FAMILY
RESOURCE_IDENTITY
```

may host dispatch the exact corresponding V5 adapter event mechanically.

```text
HOST_MAY_DISPATCH_EXACT_NATIVE_EVENT=YES_MECHANICAL_ONLY
HOST_MAY_CHOOSE_SOURCE_FAMILY=NO
HOST_MAY_CHOOSE_RESOURCE=NO
```

### Stage F — provenance normalization

V5-K6 must normalize source-specific provenance into a common bounded protocol without asserting truth.

Minimum structural fields should include when available:

```text
SOURCE_FAMILY
RESOURCE_ID
SOURCE_REVISION_OR_VERSION
SOURCE_TIMESTAMP
RETRIEVAL_ID
RETRIEVAL_TIMESTAMP
PAYLOAD_IDENTITY_OR_HASH
REQUEST_ID
TRANSPORT_STATUS
PROVENANCE_STATUS
```

Normalization may be mechanical where fields are exact protocol identities. Any semantic evidence interpretation belongs in native SIGMA.

```text
TRANSPORT_SUCCESS_EQUALS_TRUTH=NO
SOURCE_PRESENT_EQUALS_TRUTH=NO
RETRIEVED_TEXT_EQUALS_KNOWLEDGE=NO
```

### Stage G — Evidence Graph integration

V5-K7 must bind external evidence/provenance into the existing native evidence/persistent-knowledge system.

It must preserve the distinction:

```text
RETRIEVED_EXTERNAL_EVIDENCE
!=
SUPPORTED_INFERENCE
!=
TRUTH
!=
PROMOTED_KNOWLEDGE
```

The existing V4 lifecycle remains useful:

```text
HYPOTHESIS
SUPPORTED_INFERENCE
REJECTED_INFERENCE
UNRESOLVED
```

External retrieval may contribute evidence but may not bypass native lifecycle/truth gates.

### Stage H — closed-loop return to I3

After evidence integration, the updated research/evidence state returns to I3.

I3 then decides natively whether to:

```text
CONTINUE_RESEARCH
CHANGE_STRATEGY
CHANGE_SOURCE
REQUEST_MORE_EVIDENCE
HOLD_UNRESOLVED
STOP_UNKNOWN
STOP_SUFFICIENT_IN_TESTED_POLICY_SCOPE
```

Exact action vocabulary must be separately admitted and must not be inferred from this design document alone.

## Cross-lane non-destruction rule

The existing proven Internet research path and the newer V5 adapter path remain parallel until a bridge is admitted.

```text
OLD_PROVEN_INTERNET_PATH_REMOVED=NO
V5_ADAPTER_PATH_REPLACES_OLD_PATH_BEFORE_ADMISSION=NO
CROSS_LANE_SILENT_REPLACEMENT=NO
```

Integration is additive:

```text
CAPABILITY_GROWTH=ADDITIVE_NOT_REPLACEMENT
```

## Admission order

Recommended dependency order:

```text
I3 interface audit
-> I3 native post-followup outcome evaluation
-> I4 native source-family selector
-> one source discovery adapter + native candidate selector
-> exact-fetch dispatch integration for that source
-> V5-K6 provenance normalization
-> V5-K7 evidence graph integration
-> closed-loop I3 return test
-> expand to remaining source families
```

This order is intentionally capability-first, not number-first.

## Closed-loop admission test target

A future integration PASS must causally demonstrate, with no host semantic substitution:

```text
prior evidence state
-> SIGMA detects/retains need for further research
-> SIGMA chooses next research action
-> SIGMA chooses source family
-> SIGMA emits source discovery request
-> host performs network transport only
-> SIGMA receives bounded candidates
-> SIGMA chooses resource
-> host performs exact resource fetch only
-> SIGMA receives payload + provenance
-> SIGMA evaluates/integrates evidence
-> updated state changes SIGMA's next research decision
```

Counterfactual tests must show that changing fresh outcome/candidate/evidence inputs can change the native decision.

## Claim boundaries

Until separately admitted:

```text
DIRECT_I3_TO_V5_RUNTIME_INTEGRATION=NOT_PROVEN
NATIVE_SOURCE_FAMILY_SELECTION=NOT_PROVEN
NATIVE_SOURCE_DISCOVERY=NOT_PROVEN
NATIVE_RESOURCE_SELECTION=NOT_PROVEN
V5_K6_PROVENANCE_NORMALIZATION=NOT_PROVEN
V5_K7_EVIDENCE_GRAPH_INTEGRATION=NOT_PROVEN
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
GENERAL_RESEARCH_POLICY_LEARNED=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
```
