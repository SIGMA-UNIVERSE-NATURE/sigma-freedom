# SIGMA I5A — Wikipedia English discovery adapter source ready

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNTIME_ADMISSION_NOT_RUN

## Dependency

I4 Fix3 is admitted PASS in exact tested scope.

Latest I4 checkpoint:
`DOCS/GPT_REFERENCE/CHECKPOINTS/20260905_I4_FIX3_NATIVE_SOURCE_FAMILY_SELECTOR_PASS.md`

Canonical I4 native selection:

```text
SIGMA_NATIVE_CANONICAL_SOURCE_FAMILY=WIKIPEDIA
SIGMA_NATIVE_CANONICAL_SOURCE_FAMILY_ID=10
```

Host must not substitute another family.

## Capability contract

I5A proves only the Wikipedia source-discovery request/transport boundary:

```text
I4 native WIKIPEDIA selection
-> I5A native discovery request
-> host exact HTTP transport + structural JSON decode only
-> complete bounded candidate set returned to native SIGMA
```

I5A does NOT select a Wikipedia page/resource.

```text
HOST_QUERY_GENERATION=NO
HOST_RESULT_RANKING=NO
HOST_CANDIDATE_SELECTION=NO
HOST_RELEVANCE_DECISION=NO
HOST_RESOURCE_SELECTION=NO
RESOURCE_SELECTION=NOT_EXECUTED
REMOTE_API_ORDER=PROVENANCE_ONLY
```

## Canonical query provenance

The canonical query surface is the existing native-generated fresh `raw_topic.txt`:

```text
CANONICAL_COLLECTION_RUN_ID=20260903T122823Z_19134_21003
CANONICAL_RAW_TOPIC_SHA256=62b60371f21cb7be2cf6ab7fcb6b629235abe58fa97ff5738ea7548159f203f5
QUERY_ORIGIN=SIGMA_NATIVE_V11_BOUND_RAW_TOPIC
```

The runner mechanically verifies that exact identity and I5A native writes the exact bytes to its request query file. GPT/Bash does not author or rewrite the query.

## Wikipedia discovery transport scope

Bounded adapter edition:

```text
WIKIPEDIA_EDITION_SCOPE=EN_ONLY_BOUNDED_ADAPTER
WIKIPEDIA_LANGUAGE_EDITION_SELECTION=NOT_PROVEN
```

MediaWiki Action API shape used:

```text
action=query
list=search
srsearch=<exact native query bytes>
srnamespace=0
srlimit=10
srprop=timestamp|size|wordcount
format=json
formatversion=2
```

Host preserves all returned candidates up to the API request bound and preserves API order only as provenance.

Candidate protocol:

```text
CANDIDATES||RUN_ID||WIKIPEDIA||EN||COUNT||N||COMMIT||YES
CANDIDATE||ORDINAL||PAGE_ID||TITLE||SIZE||WORDCOUNT||TIMESTAMP||COMMIT||YES
```

Native I5A validates count, sequential ordinal, positive page id, nonempty title/timestamp, numeric size/wordcount, duplicate page id refusal, and exact run/family/edition binding.

## Source-ready identities

```text
I5A_BUNDLE_SHA256=5dcefdb371cd0cef77031844be5984fbb86cfe2e231aa45c6d62c66774bd7b97
I5A_SOURCE_SHA256=0d49e744c1d0395ca18dc87f40ea706da29d94474c42ac948ff2071980addd11
I5A_RUNNER_SHA256=5181eb5862da8bd09c5b0834c59a2f24869413cc8be6cae8c018b15df86002a7
I3C_SOURCE_SHA256=daa01d60e11afd64b763c6623bc14d0aa2d868cc03f686b26ad3026d6951284f
I4_FIX3_SOURCE_SHA256=a13417668f1dc85e42d7f529306cdc09928ab45655d771d95c89d383b6fc7784
I4_CATALOG_SHA256=7d650b53bae8b22fb6ab7613127e0a116bbe32d3bc032a31cdb44ad69ae7c224
I5A_BYTECODE_SHA256=UNKNOWN_NOT_COMPILED
```

## Planned admission

```text
PLANNED_TOTAL_VM_INVOCATIONS=16
I3C_CANONICAL_REPLAY_VM_INVOCATIONS=1
I4_CANONICAL_REPLAY_VM_INVOCATIONS=1
I5A_VM_INVOCATIONS=14
PLANNED_LIVE_HTTP_REQUESTS=1
```

Tests include:

- canonical native I3C -> I4 event replay;
- exact native-query byte binding;
- one live English Wikipedia search;
- complete bounded JSON candidate projection without ranking/filtering;
- dynamic query A/B output change;
- wrong-family and empty-query hold;
- valid synthetic candidates;
- zero results visibility;
- malformed/count mismatch/duplicate page-id refusal;
- transport error visibility;
- identical prepare replay;
- dynamic high-entropy token leak audit;
- step-limit audit;
- source/bytecode immutability.

## Claim boundary

Until machine PASS:

```text
I5A_RUNTIME_ADMISSION=NOT_RUN
NATIVE_SOURCE_DISCOVERY_REQUEST=NOT_PROVEN
WIKIPEDIA_DISCOVERY_TRANSPORT=NOT_PROVEN
NATIVE_RESOURCE_SELECTION=NOT_PROVEN
DIRECT_I4_TO_V5_RUNTIME_INTEGRATION=NOT_PROVEN
SEMANTIC_RELEVANCE=NOT_PROVEN
TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
```

Next action: run the exact bundle on the locked OPPO/Termux runtime and preserve first HOLD/FAIL or final I5A summary.
