# V5-K2 Native Admission V1 — Wikipedia Adapter — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNTIME_NOT_RUN

## Dependency

```text
V5K1_ADMISSION=PASS_IN_EXACT_TESTED_SCOPE
V5K1_SOURCE_SHA256=29670c3eca4bcd02e875d2178407259af9e76ebbcbbd6e2ee7a31f979da26537
```

## Locked runtime

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## V5-K2 artifact identities

```text
SOURCE_PATH=SIGMA_V5_WIKIPEDIA_ADAPTER_V5K2.sigma
SOURCE_SHA256=57a720f97004217e9f1602d7048316abf0bb711e005106ff092c65b7d19967aa
RUNNER_PATH=run_SIGMA_V5K2_NATIVE_ADMISSION_V1.sh
RUNNER_SHA256=46492716ed275e5120b7eba6e5f0bc93920dd7ed92062830d010b78e0eeee0e9
BUNDLE_NAME=SIGMA_V5K2_NATIVE_ADMISSION_V1_WIKIPEDIA_ADAPTER_BUNDLE.zip
BUNDLE_SHA256=fa9ec0548f49125037e11146b0f1c210a3e39d91b8d0c48121ad08d75da28a70
BYTECODE_SHA256=UNKNOWN_NOT_RUN
BASH_SYNTAX=PASS
PLANNED_VM_INVOCATIONS=50
DIRECTED_VM_INVOCATIONS=16
DYNAMIC_MATRIX_VM_INVOCATIONS=32
REPLAY_VM_INVOCATIONS=2
```

Mechanical host requirements:

```text
curl=REQUIRED_FOR_HTTP_TRANSPORT
jq=REQUIRED_FOR_EXACT_JSON_PROTOCOL_DECODE
PYTHON_USED=NO
```

If either tool is missing, the runner must HOLD. Do not replace the missing transport/decode layer with semantic host logic.

## Official API basis checked 2026-09-05

V5-K2 uses the documented MediaWiki Action API query shape:

```text
action=query
prop=revisions|extracts
titles=<dynamic title>
rvprop=ids|timestamp
rvlimit=1
exintro=1
explaintext=1
exchars=600
redirects=1
format=json
formatversion=2
```

Official documentation references retained in the bundle:

- `https://www.mediawiki.org/wiki/API:Properties`
- `https://www.mediawiki.org/wiki/API:Revisions`
- `https://www.mediawiki.org/wiki/Extension:TextExtracts`

## Exact V1 scope

Supported language editions in V1:

```text
en
vi
```

Native responsibilities:

- validate request ID, language, title, payload slot;
- emit exact Wikipedia request event;
- validate response identity;
- validate decoded page ID/revision ID/timestamp shape;
- expose not-found/transport/decode errors;
- require payload presence for successful retrieval;
- persist bounded Wikipedia provenance ledger;
- enforce request replay/idempotency and request-ID conflict refusal.

Mechanical host responsibilities:

- construct the Wikipedia endpoint from the native language event;
- exact HTTP GET transport;
- exact JSON protocol decode of `missing`, `pageid`, latest `revid`, latest revision `timestamp`;
- write raw JSON payload and exact adapter response protocol.

Host does NOT decide relevance, truth, knowledge promotion or research goals.

## Planned admission gates

```text
LIVE_WIKIPEDIA_RUNTIME=TESTED_EN_AND_VI_SCOPE
WIKIPEDIA_ACTION_API_QUERY=TESTED
WIKIPEDIA_REVISION_ID_PROVENANCE=TESTED
WIKIPEDIA_REVISION_TIMESTAMP_PROVENANCE=TESTED
WIKIPEDIA_PAGE_ID_PROVENANCE=TESTED
PLAINTEXT_INTRO_PAYLOAD_TRANSPORT=TESTED_BOUNDED_600_CHAR_REQUEST_SCOPE
WIKIPEDIA_NOT_FOUND_VISIBILITY=TESTED
MALFORMED_RESPONSE_REFUSAL=TESTED
PAYLOAD_MISSING_REFUSAL=TESTED
REQUEST_ID_CONFLICT_REFUSAL=TESTED
WIKIPEDIA_LEDGER_IDEMPOTENCY=TESTED
REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
REPLAY_IDENTICAL_EVENT_BYTES=YES
```

## Claim boundaries

Keep until real locked-Termux runtime proof:

```text
V5K2_RUNTIME_ADMISSION=NOT_RUN
LIVE_WIKIPEDIA_RUNTIME=NOT_YET_EXECUTED
WIKIPEDIA_ADAPTER_TESTED_SCOPE=NOT_PROVEN
V5K3_ARXIV_ADAPTER_UNLOCKED=NO
RESEARCH_GOAL_SELECTION=NOT_EXECUTED
CONTENT_SEMANTIC_INTERPRETATION=NOT_EXECUTED
CONTENT_TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
PRODUCTION_BINDING=NO
```

## Next action

Run the exact bundle on the locked Termux runtime. Preserve the first failure or final summary exactly. Only a full PASS may unlock V5-K3.
