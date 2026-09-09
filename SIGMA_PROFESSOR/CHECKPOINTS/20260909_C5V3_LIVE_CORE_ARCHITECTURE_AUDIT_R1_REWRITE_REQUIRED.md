# C5V3 LIVE CORE ARCHITECTURE AUDIT R1 — REWRITE REQUIRED

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **EXACT LIVE-SOURCE AUDIT / TARGET-ARCHITECTURE CLASS C / SUCCESSOR CORE REWRITE REQUIRED / LIVE PRODUCTION UNCHANGED**

## Exact audited artifact

```text
SOURCE_CLASS=OBSERVED_LIVE_HISTORICAL_PRODUCTION_CORE
LIVE_MAIN_SOURCE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
SOURCE_BYTES=41537
SOURCE_LINES=963
DEF_COUNT=11
```

The uploaded export contained exactly the live source plus its manifest. The source SHA256 matched the previously attested live identity exactly.

## What the live core actually is

The core is a deterministic event-driven local-learning state machine. Its 11 DEFs are:

```text
H
present
digits_only
unary_valid
unary_make
token_safe
normalize_text
reduce_bytes
catalog_record_valid
catalog_field
active_entry_id
```

Its host-op surface is limited to primitive string/list/map/read/write operations:

```text
list_get
list_len
list_new
list_push
map_get
map_has
map_new
map_set
read_text
str_join
str_len
str_replace
str_split
write_text
```

The main block handles a fixed event protocol including `TICK`, local/external segment readiness, evidence persistence, segment commit, entry completion/hold, and external fetch success/failure.

## Native learning algorithm observed

For accepted text segments the core:

1. destructively normalizes punctuation into spaces;
2. tokenizes by lines/spaces;
3. counts adjacent token pairs (`LEFT => RIGHT`);
4. selects at most eight highest-frequency local pairs;
5. represents support using unary `|` strings capped at 64;
6. merges local support with prior support from a bounded evidence bundle;
7. promotes a pair to knowledge when merged support is greater than two;
8. may generate an external query as `LEFT + " " + RIGHT` for a low-support, not-yet-learned pair.

This is genuine native deterministic learning behavior, but it is a narrow co-occurrence heuristic rather than a general cognitive architecture.

## Positive invariants worth preserving

The existing core has useful properties that must survive a rewrite:

```text
EVENT_DRIVEN_HANDSHAKE=YES
BOUNDED_PAGE_SEGMENT_BUNDLE_PROCESSING=YES
NATIVE_EXTERNAL_QUERY_GENERATION=YES_IN_EXACT_HEURISTIC_SCOPE
HOST_QUERY_GENERATION=NO
HOST_KNOWLEDGE_PROMOTION=NO
HOST_LEARNING=NO
PERSISTENCE_TRANSITIONS_EXPLICIT=YES
FAIL_CLOSED_INVALID_EVENT_AND_RECORD_PATHS=YES
```

## Architectural gaps for the intended C5V3 system

Exact source contains no native abstraction for:

```text
CAPABILITY_REGISTRY
CAPABILITY_NEED_DETECTION
CAPABILITY_ARBITRATION
CAPABILITY_DISPATCH
CAPABILITY_RESULT_EVALUATION
GOAL_OR_PROBLEM_STATE
HYPOTHESIS_OR_CLAIM_OBJECTS
CONFLICT_OR_CONTRADICTION_MODEL
REVISION_POLICY
GENERAL_MEMORY_MODEL
PROVENANCE_CHAIN
RESOURCE_GOVERNOR
TRACE_OR_REPLAY_LEDGER
```

The source has no occurrences of `capability`, `tool`, `dispatch`, `goal`, `plan`, `hypothesis`, `conflict`, `contradiction`, `revision`, `trace`, `replay`, `resource`, `quota`, or `timeout` as cognitive architecture concepts.

## Classification

For the target architecture requested for C5V3:

```text
CLASSIFICATION=C
CURRENT_CORE=MONOLITHIC_EVENT_MACHINE_PLUS_NARROW_COOCCURRENCE_LEARNER
CURRENT_CORE_SUITABLE_AS_LONG_RANGE_T0_T11_COGNITIVE_KERNEL=NO
SUCCESSOR_CORE_REWRITE_REQUIRED=YES
```

This classification does **not** mean the historical core is mechanically invalid. It means its central architecture is not the right substrate for long-range T0-T11 capability-native cognition.

## Rewrite direction

The production-lineage successor must preserve the good event/persistence/boundedness contracts while replacing the monolithic learning center with:

```text
C5V3_COGNITIVE_KERNEL
+ NATIVE_STATE_AND_OBJECTIVE_MODEL
+ NATIVE_NEED_DETECTION
+ CAPABILITY_REGISTRY_T0_T11
+ NATIVE_CAPABILITY_ARBITRATION
+ BOUNDED_CAPABILITY_DISPATCH
+ RESULT_EVALUATION
+ CLAIM_EVIDENCE_CONFLICT_REVISION
+ DURABLE_LEARNING_STATE_CONTRACT
+ EXTERNAL_EVIDENCE_REQUEST_SOVEREIGNTY
+ PROVENANCE_IDENTITY
+ RESOURCE_GOVERNOR
+ OBSERVABILITY_REPLAY
+ LEGACY_EVENT_COMPATIBILITY_ADAPTER
```

Machine-admitted capability packs from the offline capability window are integrated only after their exact PASS checkpoints arrive.

## Governance

```text
WRITE_SUCCESSOR_CORE != ADMIT_SUCCESSOR_CORE
ADMIT_CAPABILITY != LIVE_BIND_CAPABILITY
LIVE_BIND_CAPABILITY != ONLINE_AUTONOMY_PASS
PRODUCTION_CORE_WRITE=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

`CLAIM <= EVIDENCE`
