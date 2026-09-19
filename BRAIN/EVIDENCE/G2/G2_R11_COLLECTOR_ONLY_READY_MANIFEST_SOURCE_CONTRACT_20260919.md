# SIGMA.AIL — R11 Collector-Only Document / Provenance / READY.manifest Source Contract

DATE=2026-09-19
EVIDENCE_CLASS=USER_SUPPLIED_STATIC_SOURCE_TRANSCRIPT
PRIMARY_CLASSIFICATION=G2_SINGLE_WRITER_INGRESS_CONTRACT_PRECURSOR
SECONDARY_CLASSIFICATION=G6_MULTI_SOURCE_DOCUMENT_INGRESS_PRECURSOR
GENERATION_PROMOTION=NO

## Source boundary

Supplied bundle path:

```text
$HOME/storage/downloads/SIGMA_R11_COLLECTOR_ONLY_R1_BUNDLE.sh
```

This evidence is source-contract inspection only.

```text
BUNDLE_EXECUTION=NOT_PROVEN_FROM_THIS_TRANSCRIPT
PYTHON_SYNTAX_VALIDITY=NOT_PROVEN_FROM_THIS_TRANSCRIPT
RUNTIME_MANIFEST_WRITE=NOT_PROVEN_FROM_THIS_TRANSCRIPT
RUNTIME_DOCUMENT_WRITE=NOT_PROVEN_FROM_THIS_TRANSCRIPT
```

## R11 role boundary preserved by metadata

The shown document provenance objects explicitly set:

```text
semantic_summary_created=false
model_used=false
ail_used=false
vm_used=false
canon_written=false
```

This is consistent with collector-only ingress behavior in the shown source path.

```text
R11_COLLECTOR_SOURCE_PATH_USES_MODEL=NO
R11_COLLECTOR_SOURCE_PATH_USES_AIL=NO
R11_COLLECTOR_SOURCE_PATH_USES_VM=NO
R11_COLLECTOR_SOURCE_PATH_WRITES_CANON=NO
```

These are source-level fields, not independent runtime attestation.

## Scope filtering

The shown code has explicit non-corpus handling:

```text
status=EXCLUDED_SCOPE
last_error=CURRENT_INFO_NOT_CORPUS
DOCUMENT_SCOPE=EXCLUDED_CURRENT_INFO
```

Non-document/navigation scope is also separated:

```text
if scope not in {'CULTURAL_DOCUMENT','HUMAN_WRITTEN_DOCUMENT'}:
    status=NAVIGATION
    DOCUMENT_CLASS=NAVIGATION
```

Therefore the shown source path does not blindly feed every fetched page into the ready-document channel.

## Small-document path

When:

```text
len(payload) < a.min_document_bytes
```

the source persists into:

```text
pending_small/documents/<sha256>.document
pending_small/provenance/<sha256>.json
```

with:

```text
payload_mode=FULL_CLEANED_DOCUMENT_PENDING_SHORT_DOC_CURRICULUM
semantic_summary_created=false
model_used=false
ail_used=false
vm_used=false
canon_written=false
status=COLLECTED_SMALL
last_error=PERSISTED_PENDING_SHORT_DOC_CURRICULUM
READY_MANIFEST=NO
```

Scoped interpretation:

```text
SMALL_DOCUMENT_PERSISTED_SEPARATELY=YES_IN_SOURCE_CONTRACT
SMALL_DOCUMENT_READY_MANIFEST_ADMISSION=NO_IN_SOURCE_CONTRACT
SHORT_DOC_CURRICULUM_PENDING_PATH_PRESENT=YES
```

## Full-document emit contract

The shown `emit_document(...)` source:

```text
payload = text.encode('utf-8', 'replace')
digest = sha_bytes(payload)

documents/<digest>.document
provenance/<digest>.json
```

The provenance object includes:

```text
schema
source_sha256
source_url
library_index
country
library_name
section_key
title
doc_type
cleaned_utf8_bytes
payload_mode=FULL_CLEANED_DOCUMENT
semantic_summary_created=false
model_used=false
ail_used=false
vm_used=false
canon_written=false
```

The shown source inserts:

```text
INSERT OR IGNORE INTO r11_collector_only_documents
(source_hash,lib_idx,section_key,source_url,title,doc_type,content_bytes,document_path,meta_path)
```

then commits the DB transaction before calling `atomic_manifest_add(...)`.

After successful emit path, caller updates URL status to:

```text
status=FED
COLLECTED_DOCUMENT=YES
MANIFEST_ADDED=YES|ALREADY_PRESENT
```

## READY.manifest contract

The shown `atomic_manifest_add(...)` uses:

```text
manifest = inbox / 'READY.manifest'
lock_path = inbox / '.READY.manifest.lock'
fcntl.flock(..., LOCK_EX)
```

It reads existing records and collects already-seen 64-character digest fields. If the digest already exists:

```text
return False
```

New record shape:

```text
SHA256<TAB>relative-path
```

implemented as:

```text
lines.append(f'{digest}\t{rel.as_posix()}')
```

Manifest rewrite pattern:

```text
.READY.manifest.<pid>.tmp
-> tmp.write_text(...)
-> os.replace(tmp, READY.manifest)
```

Scoped source-level interpretation:

```text
READY_MANIFEST_EXCLUSIVE_LOCK_PRESENT=YES
READY_MANIFEST_DIGEST_DEDUP_PRESENT=YES
READY_MANIFEST_RELATIVE_PATH_RECORD_PRESENT=YES
READY_MANIFEST_TEMP_REWRITE_OS_REPLACE_PATTERN_PRESENT=YES
```

Do not broaden this into crash-consistency/runtime proof:

```text
READY_MANIFEST_RUNTIME_SERIALIZATION_PASS=NOT_PROVEN
READY_MANIFEST_CRASH_ATOMICITY=NOT_PROVEN
FILESYSTEM_DURABILITY_AFTER_OS_REPLACE=NOT_PROVEN
MULTIPROCESS_RUNTIME_RACE_TEST=NOT_PROVEN
```

The source calls `core.atomic_write(...)` for document/provenance files, but the implementation of `core.atomic_write` is not shown here:

```text
DOCUMENT_ATOMIC_WRITE_IMPLEMENTATION=NOT_PROVEN_FROM_THIS_TRANSCRIPT
PROVENANCE_ATOMIC_WRITE_IMPLEMENTATION=NOT_PROVEN_FROM_THIS_TRANSCRIPT
```

## Duplicate behavior

The shown caller computes:

```text
dup = core.duplicate_of(...)
```

and, when duplicate:

```text
status=DUPLICATE
last_error=DUPLICATE_OF:<source>
DOCUMENT_CLASS=DUPLICATE
```

Thus duplicates are separated from normal `FED` document admission in the shown path.

## Section completion substrate

The shown source counts:

```text
pending = status IN ('NEW','RETRY')
docs = COUNT(*) FROM r11_collector_only_documents
SECTION_PROGRESS=DOCUMENTS:<docs>|PENDING:<pending>|EMITTED_THIS_CYCLE:<emitted>
```

and begins a `SECTION_COMPLETE` event when `pending == 0`.

The remainder of the event payload is not visible in this transcript and is not reconstructed.

## Architectural interpretation

```text
R11_COLLECTOR_ONLY_DOCUMENT_INGRESS_CONTRACT_PRECURSOR=YES
R11_PROVENANCE_SIDECAR_CONTRACT_PRECURSOR=YES
R11_READY_MANIFEST_FEED_CONTRACT_PRECURSOR=YES
R11_SMALL_DOCUMENT_QUARANTINE_OR_PENDING_PATH_PRECURSOR=YES
R11_LEARNER=NO_IN_SHOWN_SOURCE_CONTRACT
R11_CANON_WRITER=NO_IN_SHOWN_SOURCE_CONTRACT
```

This source contract is compatible with a separate sole learner/canon writer, but does not independently prove the live writer topology.

## Critical boundary

```text
STATIC_SOURCE_CONTRACT != RUNTIME_PASS
READY_MANIFEST_SOURCE_LOCK != SECOND_WRITER_RUNTIME_REJECTION_PROOF
COLLECTOR_DOCUMENT_WRITE != MODEL_LEARNING
COLLECTOR_STATUS_FED != CANONICAL_MODEL_ADMISSION
R11_SOURCE_CONTRACT != G2_PROMOTION
R11_SOURCE_CONTRACT != G6_PROMOTION
CURRENT_GENERATION_REMAINS=G1
```

```text
CLAIM_SCOPE=EXACT_SUPPLIED_SOURCE_TRANSCRIPT_ONLY
```
