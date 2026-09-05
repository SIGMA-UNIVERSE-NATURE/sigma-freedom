# V4-C5 — Native Oppo Local Archive + Self-Initiated External Acquisition Bridge V1

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: `DESIGN / IMPLEMENTATION_START`

## Exact user requirement

SIGMA must be able to learn from the material already present on the Oppo/Termux device. The local learning universe is not limited to repository documents and is not limited to SIGMA's already-derived `knowledge_v2` memory.

Internet access must not be hard-gated behind completion of the local archive. When native SIGMA itself emits an external research/acquisition intent, the bridge must allow the exact request to reach an admitted mechanical network transport. GPT/Bash/host must not decide that SIGMA should go online, choose the query, choose the source/resource, or substitute a research goal.

## Governance boundary

All cognitive arrows remain native SIGMA under the locked VM:

```text
SIGMA_NATIVE_OWNS_LOCAL_WORK_SELECTION=YES
SIGMA_NATIVE_OWNS_LEARNING=YES
SIGMA_NATIVE_OWNS_REVISIT=YES
SIGMA_NATIVE_OWNS_GAP_OR_RESEARCH_INTENT=YES
SIGMA_NATIVE_OWNS_EXTERNAL_REQUEST_CONTENT=YES
SIGMA_NATIVE_OWNS_NEXT_ACTION=YES
HOST_LOCAL_FILE_SELECTION=NO
HOST_EXTERNAL_RESEARCH_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_LEARNING=NO
```

Host/shell may only discover filesystem entries mechanically, preserve exact identifiers/metadata, read exact byte ranges requested by native SIGMA, hash bytes, supervise the locked compiler/VM, and transport an exact native external request/response.

## Architecture

```text
$HOME/SIGMA on Oppo
  -> incremental mechanical catalog, no semantic ranking
  -> bounded catalog pages
  -> native C5 archive frontier
  -> native local entry/segment request
  -> host exact-byte transport
  -> native learner / evidence / memory capabilities

native SIGMA evidence/gap/research state
  -> native external acquisition intent
  -> C5 bridge dispatches exact opaque native request
  -> admitted mechanical network adapter
  -> exact response bytes
  -> native SIGMA evaluates/learns
```

Local and external are therefore concurrent affordances. The bridge MUST NOT encode `LOCAL_COMPLETE -> INTERNET_ALLOWED` as a mandatory policy.

## Local universe scope

The target root is the Oppo SIGMA archive under `$HOME/SIGMA`, observed by the user at about 9.6 GB. It includes, subject only to mechanical security/control exclusions required by repository governance:

- user-provided material;
- GPT teaching material stored locally;
- previously downloaded Internet material;
- repository documents/reference sources;
- SIGMA-generated textual material and evidence;
- persistent knowledge/memory stores, including the observed `sigma_genesis1/.sigma_native/knowledge_v2` structure.

The bridge does not copy the archive into a second 10 GB corpus.

## Local catalog protocol

Catalog generation is mechanical only. A bounded page contains opaque records such as:

```text
ENTRY_ID=<mechanical-id> || PATH_B64=<exact-path-bytes-base64> || SIZE=<bytes> || MTIME_NS=<value>
```

The host does not assign relevance, lesson priority, topic, semantic class, quality, truth, or understanding state.

Initial discovery is incremental/persistent. Learning may begin from catalog pages already discovered while later filesystem entries continue to be discovered.

## Bounded content transport

Large files must never require one whole-file native VM read. The intended protocol is:

```text
native request: ENTRY_ID + OFFSET + MAX_BYTES
host: validate mechanical path/root/version + return exact bytes
native state: persist the next read/revisit decision
```

A changed file is exposed as a changed/new mechanical version; host does not decide whether the content should be relearned.

## Existing `knowledge_v2`

Observed device evidence shows a versioned store with:

```text
HEAD
commits/<HEAD>/commit.json
events.jsonl
revisions/<revision-id>.json
objects/<id>.blob
snapshots/*.json
```

Observed event records contain `logical_id`, `old_revision`, and `new_revision`; observed revisions include structured semantic-link records; observed objects can contain `MATERIAL_SHA256` and `SOURCE` provenance. C5 must preserve this structure rather than flattening all objects into anonymous `.document` files.

A dedicated bounded adapter may expose HEAD/commit/event/revision/object traversal to native SIGMA while generic archive coverage remains available for eligible local files.

## External acquisition protocol

C5 does not invent an external query. It accepts only an exact request already emitted by an upstream native SIGMA capability. The bridge treats that request as opaque transport payload.

R1 proves only that the native bridge distinguishes and dispatches a dynamic upstream native external intent without consuming/advancing local work. It does not prove that SIGMA generated the intent autonomously end-to-end.

A later integration gate must connect the request input to a native gap/research-goal/resource-selection chain and then to an admitted network transport. Only that end-to-end locked-runtime evidence may support a self-initiated Internet-acquisition claim.

## Implementation gates

```text
C5R1  native local-catalog frontier + exact external-intent dispatch
C5R2  bounded exact local byte-range consumer with persistent version/cursor state
C5R3  knowledge_v2 bounded graph/revision/object adapter
C5R4  native learning integration across real Oppo local archive
C5R5  native research-intent -> admitted network transport -> native evidence loop
C5R6  restart/replay, mutation, hold, step-limit and long-horizon shadow proof
```

These are dependency gates, not a policy that forbids Internet before local completion.

## C5R1 contract

Inputs are dynamic files in isolated `.sigma_exec` state:

```text
SIGMA_V4C5R1_LOCAL_CATALOG_PAGE.memory
SIGMA_V4C5R1_LOCAL_CATALOG_PAGE_ID.memory
SIGMA_V4C5R1_LOCAL_CURSOR.memory
SIGMA_V4C5R1_LOCAL_CURSOR_PAGE_ID.memory
SIGMA_V4C5R1_NATIVE_EXTERNAL_REQUEST.memory
```

Outputs:

```text
SIGMA_V4C5R1_ACTION.memory
SIGMA_V4C5R1_SOURCE.memory
SIGMA_V4C5R1_TARGET.memory
```

Operational actions:

```text
DISPATCH_NATIVE_EXTERNAL_REQUEST
DISPATCH_NATIVE_LOCAL_ENTRY
REQUEST_NEXT_LOCAL_CATALOG_PAGE
REFUSE_CATALOG_PAGE_LIMIT
WAIT_NO_BRIDGE_WORK
```

If a non-empty upstream native external request exists, C5R1 dispatches that exact request and does not advance the local cursor. Otherwise it selects the next local catalog record natively from the bounded page. Page changes reset the page-local cursor natively.

## C5R1 proof requirements

- locked SIGMAC/VM identities;
- dynamic unseen catalog identifiers;
- local cursor persistence across fresh VM runs;
- external request changes produce corresponding exact target changes;
- external dispatch leaves local cursor unchanged;
- catalog page change resets page-local cursor;
- oversized page refusal;
- source/bytecode anti-forced-semantic-token audit;
- host substitution audit: runner supplies conditions only and does not select the runtime action/target;
- production state not mutated.

## Claim boundary at design time

```text
C5_DESIGN_READY=YES
C5R1_RUNTIME_PROOF=NOT_RUN
REAL_OPPO_ARCHIVE_LEARNING_THROUGH_C5=NOT_RUN
END_TO_END_NATIVE_SELF_INITIATED_INTERNET_ACQUISITION=NOT_RUN
PRODUCTION_BINDING=NO
```

The purpose of this design is to expose the local archive and Internet transport as capabilities while keeping the decision to use them inside native SIGMA.
