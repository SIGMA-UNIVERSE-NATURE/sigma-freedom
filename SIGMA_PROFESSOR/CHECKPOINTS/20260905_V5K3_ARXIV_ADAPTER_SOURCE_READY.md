# V5-K3 arXiv Adapter — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Frontier

```text
CURRENT_LEVEL=LEVEL_2_V5
CURRENT_STAGE=V5-K3
CURRENT_CAPABILITY=ARXIV_ADAPTER
V5K2_ADMISSION=PASS_IN_EXACT_TESTED_SCOPE
V5K3_SOURCE_READY=YES
V5K3_RUNTIME_ADMISSION=NOT_RUN
V5K4_PUBMED_ADAPTER_UNLOCKED=NO_PENDING_V5K3_RUNTIME_PASS
```

## Artifact identities

```text
BUNDLE_NAME=SIGMA_V5K3_NATIVE_ADMISSION_V1_ARXIV_ADAPTER_BUNDLE.zip
BUNDLE_SHA256=9849b2377ed1f6d711b39254270c0a722d96a2e1109b8761580b6b5170de376b
SOURCE_SHA256=d3ecd3c2683bdf88cc95ef83ec643235251cb2fbaa0d17bc8d8fb1f70c3c750b
RUNNER_SHA256=82e3a543d16995c84b3cf1f17bc70c9964906b8ba2c9859f04d60b49962c794b
V5K2_DEPENDENCY_SOURCE_SHA256=57a720f97004217e9f1602d7048316abf0bb711e005106ff092c65b7d19967aa
BYTECODE_SHA256=UNKNOWN_NOT_RUN
BASH_SYNTAX=PASS
PLANNED_VM_INVOCATIONS=50
DIRECTED_VM_INVOCATIONS=16
DYNAMIC_MATRIX_VM_INVOCATIONS=32
REPLAY_VM_INVOCATIONS=2
```

## Official API basis checked before build

Official arXiv API User's Manual:
`https://info.arxiv.org/help/api/user-manual.html`

Official arXiv API Terms of Use:
`https://info.arxiv.org/help/api/tou.html`

V5-K3 exact API shape:

```text
https://export.arxiv.org/api/query
id_list=<dynamic supplied arXiv ID>
max_results=1
```

The official manual documents the query interface, `id_list`, and Atom 1.0 XML responses. Current API terms require no more than one legacy API request every three seconds and a single connection at a time.

Runner therefore enforces:

```text
ARXIV_RATE_LIMIT_DELAY_SECONDS=3
ARXIV_SINGLE_CONNECTION_TRANSPORT=YES
```

## Exact V1 proof scope

Planned native proof:

- dynamic arXiv ID request emission;
- live arXiv API transport using `id_list`;
- raw Atom XML payload retention in isolated shadow state;
- entry ID provenance;
- published timestamp provenance;
- updated timestamp provenance;
- primary category provenance;
- not-found visibility;
- malformed-response refusal;
- missing-payload refusal;
- request-ID conflict refusal;
- persistent arXiv ledger idempotency;
- replay/event determinism.

Mechanical host tools:

```text
curl=REQUIRED
xmllint=REQUIRED
sleep=REQUIRED
```

If any required mechanical tool is missing, runner must HOLD before compile/runtime rather than substitute cognition.

Termux normally obtains `xmllint` from the `libxml2` package.

## Host/native boundary

```text
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_HTTP_ROLE=MECHANICAL_EXACT_REQUEST_TRANSPORT_ONLY
HOST_XML_DECODE_ROLE=MECHANICAL_EXACT_PROTOCOL_DECODE_ONLY
HOST_RESOURCE_SELECTION=NO_CLAIM_DYNAMIC_ARXIV_ID_INPUT_SUPPLIED
HOST_SEMANTIC_SUBSTITUTION=NO
```

Host may transport the exact native event, XML-validate it, and decode the exact provenance fields only. It may not choose an arXiv paper or research goal.

## Claim boundaries

Keep until locked-Termux PASS:

```text
LIVE_ARXIV_RUNTIME=NOT_YET_EXECUTED
ARXIV_ADAPTER_TESTED_SCOPE=NOT_PROVEN
V5K3_RUNTIME_ADMISSION=NOT_RUN
V5K4_PUBMED_ADAPTER_UNLOCKED=NO
RESEARCH_GOAL_SELECTION=NOT_EXECUTED
CONTENT_SEMANTIC_INTERPRETATION=NOT_EXECUTED
CONTENT_TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
PRODUCTION_BINDING=NO
```

Successful arXiv retrieval must not be conflated with truth or knowledge promotion.

## Next action

1. Verify bundle SHA256.
2. Clean-unzip and run `sha256sum -c MANIFEST.sha256`.
3. Run `run_SIGMA_V5K3_NATIVE_ADMISSION_V1.sh` as its own process.
4. If runner HOLDS for missing `xmllint`, install only the mechanical package and rerun unchanged.
5. Preserve first failure or final 50-case summary exactly.
6. On PASS, create immutable V5-K3 admission checkpoint and unlock V5-K4 PubMed.
