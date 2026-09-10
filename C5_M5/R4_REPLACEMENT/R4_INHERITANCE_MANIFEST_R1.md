# R4 INHERITANCE MANIFEST R1

Date: 2026-09-10 (Asia/Ho_Chi_Minh)
Status: CLEANLINE INHERITANCE CONTRACT / NOT RUNTIME-ADMITTED
Development branch: `r4-replacement-cleanline-20260910`
Base: `SIGMA_LIFE@463fd7e2d2b1ea2f368abb661e0e204c5412b992`

## 1. Purpose

This manifest defines what the R4 replacement program may reuse, what must be re-bound by exact evidence, what is reference-only, and what is prohibited from entering the new cognitive lineage.

Core rule:

```text
INHERIT_PROVEN_CAPABILITY=YES
INHERIT_UNPROVEN_SEMANTIC_CONCLUSION=NO
INHERIT_BY_NAME_ONLY=NO
INHERIT_BY_EXACT_IDENTITY_ABI_EVIDENCE=YES
REBUILD_ADMITTED_MECHANICAL_PRIMITIVE_WITHOUT_DAMAGE_EVIDENCE=NO
```

Availability/admission of a mechanical tool does not imply R4 cognitive adoption.

## 2. Locked execution environment

Current repository execution identities:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

These remain the active admission identities unless a separately approved runtime migration supersedes them.

Repository HEAD and toolchain identity are separate identity layers. A repository commit must never substitute for compiler/VM fingerprint verification.

## 3. Inheritance classes

```text
CLASS A = REQUIRED NON-REGRESSION INHERITANCE
CLASS B = ADMITTED MECHANICAL CAPABILITY; BIND EXACTLY BEFORE R4 USE
CLASS C = STRUCTURAL/COGNITIVE SCAFFOLD REFERENCE; RE-AUDIT BEFORE USE
CLASS D = REFERENCE/VOCABULARY ONLY; NO SEMANTIC AUTHORITY
CLASS X = PROHIBITED COGNITIVE IMPORT
```

## 4. CLASS A — survival/resurrection architecture

Reference:

```text
REPO=linkcomltd-byte/sigma-universe-web
PATH=GPT_REFERENCE/SIGMA_AUTONOMOUS_RESURRECTION_PATTERN_v1.0_20260910.md
COMMIT=67f39fd834b94537e85e6bbcb0081146f1556527
```

Observed/proven deployment properties recorded by that reference include:

```text
C5_HARD_KILL_RECOVERY=PROVEN
INGRESS_RECOVERY=PROVEN
SUPERVISOR_RECOVERY_BY_OUTER=PROVEN
FULL_CONTROL_PLANE_RECOVERY_WITH_OUTER_ALIVE=PROVEN
ANDROID_REBOOT_RESURRECTION=PROVEN
EXACTLY_ONE_TOPLEVEL_COGNITIVE_WRITER_AFTER_RECOVERY=PROVEN
POST_RESURRECTION_PROGRESS=PROVEN
PERSISTENT_STATE_LINEAGE_PRESERVED=PROVEN
MANUAL_RECOVERY_FOR_TESTED_KILL_REBOOT_CLASSES=NOT_REQUIRED
```

Reusable architecture:

```text
ANDROID BOOT
-> BOOT LAUNCHER
-> OUTER WATCHDOG
-> INNER SUPERVISOR
-> COGNITIVE WRITER + INGRESS
-> SAME PERSISTENT STATE LINEAGE
```

R4 requirement:

```text
R4_MUST_PRESERVE_OR_EXCEED_THIS_SURVIVAL_CLASS=YES
R4_MAY_REUSE_C5_SCRIPT_NAMES_AS_COGNITIVE_IDENTITY=NO
R4_MUST_REPROVE_DESTRUCTIVE_TESTS_WITH_R4=YES
```

The reusable object is the recovery pattern/invariants, not the legacy C5 cognitive program.

## 5. CLASS B — admitted offline mechanical substrate

Authoritative offline lane:

```text
BRANCH=c5v3-r5-r6-sync-handoff-20260909
```

Important current T10 synchronization references:

```text
T10_FULL_CHECKPOINT_COMMIT=7dce9e7fcdbf4f263b632e0368fd30a3a48c1102
T10_LATEST_COMMIT=4326080a94741dc72242f389f4b5572fdfd293ba
T10_HANDOFF_COMMIT=ebc159442fe945eece7f6cdcf79baabd8d1b8ea9
T10_STATUS_COMMIT=1b206c8f2cb5c487a149d8c6ebd2baf8b913f255
```

### T1-T3

Admitted mechanical families:

```text
T1=VECTOR_MATRIX_KERNEL
T2=BOUNDED_GRAPH_TRAVERSAL
T3=LOCAL_INDEX_BM25
```

R4 rule: exact source/binary/ABI identities must be recovered from their canonical checkpoints before binding. Do not reconstruct them from summaries.

Claim ceiling remains mechanical. BM25 ranking, graph traversal, and vector operations are not semantic understanding.

### T4 — native text/codecs/framing/structured data

```text
T4A_SOURCE_SHA256=af36c1b4ee4491533e93b878dc9d0de475f6561f35dd3979fa5b8bbb6d60d572
T4A_BINARY_SHA256=45455d007e0cb722752c4cf06cd8919b66b20e5064939781e4dfa94f057c78db
T4B_SOURCE_SHA256=31a89e66943d8e0489c9c2df65331bb60bc6a8e326e0bcb338e2adb7a15f93d6
T4B_BINARY_SHA256=5452a7c89b8107dc6b51714b4d97639683683e42dd7e975a93fea990e3924d47
T4C_SOURCE_SHA256=5e120a48dd9af95913b12e1be10e41c4a7e1b30c2958951f2c9719b5305b8d47
T4C_BINARY_SHA256=cb59635616ae41e7c50f9bcd55907dc7b40e4675d67f49b081584dd13ade4fb9
```

Use for strict UTF-8/codecs/framing/JSON/CSV/URL/Content-Type/normalization/XML/HTML mechanics. Do not treat parser output as meaning.

### T5 — filesystem + durable state

```text
T5A_SOURCE_SHA256=8d9732ec977864f12c5ebc5cd975c1d1db2d1cd8a186e7df8594f3754864ba
T5A_BINARY_SHA256=59156dfd74889f64228f042e332a44146e2f10cd2cdb75fd5bb091dff7fc16aa
T5B_SOURCE_SHA256=dc2397501498336a1ff0e1bd5d2392e022a36fe2918591e15edc67266adf2c7a
T5B_BINARY_SHA256=e73cd4fa7f0ca09917c2b1029a57591e1ab50d327e92e143a77fa3d9fe6b8e3c
```

Use for atomic/durable/recoverable state, WAL/checkpoint/replay/CAS, with T5A lock/lease where writer serialization is required.

R4 must not build a second semantic-specific storage engine merely because its state schema is new.

### T6 — DNS/TCP/TLS/HTTP/advanced flow

```text
T6A_SOURCE_SHA256=e01f8ba8a1e8a42ff6474d3d0f1c739328a9c8a59ad8b42fa97d83041e73abd1
T6A_BINARY_SHA256=3b2cdeb0cb18d5105e8a8adb6f2d5f7b90042815b83cf651d634c14d37066660
T6B_SOURCE_SHA256=046ffe2aa2d9cc0b20fcd6a15b95d71485f69dd612f352f19d4dccc5e06aab5b
T6B_BINARY_SHA256=83cc67b29acbe1c0fa1fc812ea713cf6451ffefe73a245cc0603a9d9b509a36a
```

Use as bounded verified transport. R4 cognition must own research intent, source/capability strategy, and semantic interpretation.

### T7 — scheduler + resource governor

```text
T7A_SOURCE_SHA256=a9d4dca5cf6e502bb15643a1fae52337715fbe5dd75005fb3f9ecda734ad9f58
T7A_BINARY_SHA256=3c0799151d426df252f7987537eccd98e70cc8fe40f3ff07f37d8f8e91b07181
T7B_SOURCE_SHA256=63fc5ed7c0cd095271819d79099f06a4328acf5523c5fcce4b4b6ec985ad80a6
T7B_BINARY_SHA256=19c00435adf987f5ee47088ecd9035e26b40f868ec0af363158c0ce8214964de
T7_COMBINED_BUNDLE_SHA256=102c692ee17d0995dcdf4bb1b23a66d85bd54751ecac9a596908c776d842b994
```

Use for bounded scheduling, timers, cancellation, worker pools, step/resource quotas, watchdog behavior. Resource selection/priority remains cognition when semantically meaningful.

### T8 — process/IPC/capability sandbox/crash recovery

```text
T8A_SOURCE_SHA256=dad5c93f0d6b4973e6b70b3400cfbaec51c2114707fe2e87c7d6a64edac9b839
T8A_BINARY_SHA256=040553529973cd6075d33bb83b4e124b8a4df4e09c3206a86acedd7f965ba87d
T8B_SOURCE_SHA256=27f6d462605d91458a38b8bab518eae00c74ed4dc32071b85617656e500117fa
T8B_BINARY_SHA256=19cf4a0fc2b23f0783d795a0b3f17c107890eed2090810a153c9fe29b2f9ecbd
```

Use for bounded process execution, IPC, FD capability sandbox, seccomp/no-new-privileges, restart receipts. Namespace isolation was not available/proven on the tested Oppo environment; do not overclaim it.

### T9 — cryptographic integrity + identity/provenance

```text
T9A_SOURCE_SHA256=eba77488481b76cb66e3a14c2540ccf3da856b8f5233bb9891f63b0790f9c361
T9A_BINARY_SHA256=3e88064d34af285a832ab45bcd2e0d7d998d2df35f3dd5031b87c7dc5d3479bc
T9B_SOURCE_SHA256=981b8a5f5e252e9e5354167ef37affc34f2890508f55064d0eb1b28ec75a70f3
T9B_BINARY_SHA256=f468db1ad900fdda0e585f71888a2e1168ba4522616c484d2752a4e51b7d3ae7
```

Use for source/work/span/artifact/runtime/state-lineage identity and authenticated provenance receipts.

```text
HASH_ALONE_IS_NOT_PROVENANCE=YES
```

### T10 — archive/compression + document containers

```text
T10A_SOURCE_SHA256=545a32122f1626f5674e952e1005cd10c190c0b00494608a98dbb00011cf7004
T10A_BINARY_SHA256=bc519755d46b068f5bfe7fec9b4809990411c35b05a75ce30af80cc0ff0cbb4b
T10B_SOURCE_SHA256=0b4afa5cc2c8ce34392f475bacf71ac75baf468ac85f2d5f3c1d50f36fe36977
T10B_BINARY_SHA256=0c863758f53616c44f074ea6be7392e1df168aea08035b7f4b7f98cd1881d1e1
```

Use for bounded ZIP/TAR/gzip/zstd and EPUB/PDF/MIME document mechanics with exact T9B source/work/span provenance.

No OCR, semantic layout understanding, document relevance, or cognitive adoption is implied.

### T0-T10 inheritance ceiling

```text
T0_TO_T10_AVAILABLE_MECHANICAL_SUBSTRATE=YES_IN_THEIR_EXACT_ADMITTED_SCOPES
R4_COGNITIVE_ADOPTION_OF_T0_TO_T10=NOT_YET_PROVEN
TOOL_AVAILABLE != TOOL_LEARNED
COMBINED_TOOL_PASS != LANGUAGE_UNDERSTANDING
```

Before R4 calls any tool family in an admission test, exact artifact identity and ABI/schema/resource profile must be equality-gated.

## 6. CLASS B — R7L mechanical language-learning substrate

Current requirement reference:

```text
C5_M5/R7_LANGUAGE_UNDERSTANDING_NATIVE_TOOL_REQUIREMENT_V2_SAFE_COMPACT.md
ISSUE=25
```

Planned/required mechanical families include learned tokenizer/subword mechanics, tensor/autodiff, trainable sequence representation, capability registry/call gate, and execution/resource receipts.

They remain mechanical substrate only.

```text
PRETRAINED_VOCABULARY_AS_LANGUAGE_SEMANTICS=FORBIDDEN
PRETRAINED_SEMANTIC_EMBEDDING=FORBIDDEN
HIDDEN_POS_NER_DEPENDENCY_COREFERENCE_SEMANTICS=FORBIDDEN
SYNONYM_PARAPHRASE_ORACLE=FORBIDDEN
SUMMARIZE_TRANSLATE_ORACLE=FORBIDDEN
TRUTH_SUPPORT_CONTRADICTION_ORACLE=FORBIDDEN
HOST_TOOL_SELECTION=FORBIDDEN
```

Each R7L family enters this manifest as usable only after its own canonical machine admission is available and exact identity is recorded.

## 7. CLASS C — R4 Academic scaffold

Current reference directory:

```text
C5_M5/R4_ACADEMIC/
```

Potentially reusable structural ideas/components include:

```text
exact document/source/version/span identity
EOF != UNDERSTOOD
exact capability request/result binding
host does not select semantic capability winner
observation/evidence provenance binding
restart-safe academic memory shape
```

However, the current Academic scaffold is not automatically the replacement cognition architecture.

Its fixed epistemic labels, state names, and transaction vocabulary must be audited against the cleanline constitution before reuse. Structural machine-control labels may remain in receipt/state schemas; they must not become forced cognitive speech or preloaded human meaning.

```text
R4_ACADEMIC_REFERENCE=YES
R4_ACADEMIC_WHOLESALE_COGNITIVE_IMPORT=NO
R4_ACADEMIC_RUNTIME_ADMISSION_FOR_REPLACEMENT=NOT_PROVEN
```

## 8. CLASS C — prior R4 native-learning scaffold

Reference:

```text
C5_M5/R4_NATIVE_LEARNING/ARCHITECTURE_R1.md
```

Useful principles include capability-native ownership, provenance-bound results, restart/reuse, host exclusion, no LEFT/RIGHT cognition, and compact memory direction.

The existing scaffold also contains predefined epistemic vocabulary such as `CLAIM`, `GAP`, `SUPPORT`, `CONTRARY`, `UNRESOLVED`, and related state labels. Those may be acceptable as machine/test schema only where they do not define human meaning or force Sigma's expression, but they are not automatically canonical R4 cognition.

```text
PRIOR_R4_NATIVE_LEARNING=REFERENCE_ONLY_PENDING_CLEANLINE_AUDIT
```

## 9. CLASS D — SIGMA language/reference layer

The native executable language syntax remains governed by machine evidence and the locked compiler/VM.

The 256-symbol matrix remains:

```text
PATH=DOCS/GPT_REFERENCE/SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825.md
STATUS=GPT_REFERENCE_ONLY_REFERENCE_PROPOSED
CANONICAL_MACHINE_SEMANTICS=NO_UNLESS_SEPARATELY_VERIFIED
```

Glyph names and human glosses are not cognitive capabilities and must not bootstrap the R4 world model.

## 10. CLASS X — prohibited inheritance

The following may remain archived but must not enter the new R4 cognitive state as learned truth/meaning:

```text
legacy LEFT/RIGHT discourse cognition
lexical cue -> semantic relation tables
predefined word -> concept/meaning tables
host-generated summaries as Sigma memory
host-generated semantic queries as Sigma intent
host-selected source/resource as Sigma research choice
precomputed YES/NO/UNKNOWN/UNPROVEN answer vocabulary as Sigma speech
prewritten "I understand" / "I do not understand" outputs
hidden POS/NER/dependency/coreference semantic annotations
external pretrained semantic embeddings/models used as Sigma meaning
legacy C5V3 conclusions promoted solely by migration
```

## 11. Legacy ~30 GB storage policy

The existing Oppo corpus/state must be frozen and classified before any migration attempt.

Target classes:

```text
HUMAN_SOURCE_RAW
ASSISTED_SOURCE
LEGACY_C5_GENERATED_STATE
INDEPENDENTLY_ADMITTED_STRUCTURAL_ARTIFACT
UNKNOWN_ORIGIN
```

No bulk import into `R4_COGNITIVE_STATE_LINEAGE` is allowed.

R4 may later re-read eligible human/assisted source material through exact provenance, with assisted origin preserved. Legacy C5-generated semantic state is evidence/history or a hypothesis to re-evaluate, not native R4 knowledge.

## 12. Binding rule for every inherited capability

Before use in a real R4 runtime admission:

```text
CANONICAL_CHECKPOINT_FOUND=YES
SOURCE_IDENTITY_MATCH=YES
BINARY_OR_BYTECODE_IDENTITY_MATCH=YES
ABI_SCHEMA_IDENTITY_MATCH=YES
RESOURCE_PROFILE_IDENTITY_MATCH=YES_WHEN_APPLICABLE
CLAIM_SCOPE_ACCEPTED=YES
HOST_SEMANTIC_POLICY=NO
R4_NATIVE_SELECTION_OR_USE=SEPARATELY_TESTED
```

If exact identity cannot be established, fail closed and mark the inheritance `NOT_BOUND` rather than rebuilding from description.

## 13. Current manifest status

```text
R4_CLEANLINE_CONSTITUTION=CREATED_SOURCE_DESIGN_ONLY
R4_INHERITANCE_MANIFEST=CREATED_SOURCE_DESIGN_ONLY
R4_GENESIS_STATE=NOT_YET_RUNTIME_ADMITTED
R4_MINIMAL_COGNITIVE_LOOP=NOT_YET_RUNTIME_ADMITTED
R4_INTERNET_LANGUAGE_LOOP=NOT_YET_RUNTIME_ADMITTED
R4_PRODUCTION_CUTOVER=NOT_ALLOWED
```
