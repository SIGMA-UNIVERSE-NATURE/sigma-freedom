# V4-C2 R1 STATIC AUDIT — BLOCKED BEFORE RUNTIME

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`V4C2R1_SOURCE_EXISTS=YES`

`V4C2R1_RUNTIME_PROOF=NOT_RUN`

`V4C2R1_ADMISSION=BLOCKED_BY_STATIC_AUDIT`

`RUN_SIGMA_V4C2_FULL_CORPUS_SHADOW_PREFLIGHT_R1=DO_NOT_RUN`

`RUN_SIGMA_V4C2_FULL_CORPUS_CONTINUOUS_SHADOW_R1=DO_NOT_RUN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Production discipline remains:

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`UPGRADE_V2_4_IN_PLACE=NO`

This correction supersedes the execution instruction in `20260905_V4C2_FULL_CORPUS_CONTINUOUS_SHADOW_SOURCE_READY.md`. The R1 files remain provenance/source-design evidence only until replaced by a corrected revision.

## Static-audit blockers

### 1. Production raw-manifest race in preflight

R1 requires the complete raw `.document` directory manifest and document count to remain identical before/after the fixed-turn preflight while simultaneously requiring production V2.4 to remain running.

Production V2.4 may legitimately add a newly fetched `.document` during that interval. That would create a false `HOLD=PRODUCTION_RAW_CORPUS_CHANGED` even if no pre-existing document bytes were mutated.

Correction requirement:

- snapshot identities of pre-existing documents at preflight start;
- after runtime verify every pre-existing document still exists with identical bytes;
- permit append-only arrival of new production documents;
- do not permit mutation/deletion of pre-existing documents.

### 2. Multi-span PASS claim not equality-gated by observed runtime evidence

R1 prints:

`MULTI_SPAN_2_3_4_TOKEN_STRUCTURAL_LEARNING=PASS_IN_EXECUTED_WINDOWS_SCOPE`

when only generic archived evidence is required. The runner does not require observed runtime pair/triple/quad occurrences.

Correction requirement:

- gate pair occurrence > 0;
- gate triple occurrence > 0;
- gate quad occurrence > 0;
- only then admit the corresponding executed-span claim.

### 3. Whole-document read remains on the manager critical path

R1 corpus manager uses `read_text` on the complete active document and splits the complete text before selecting a 4-line segment.

Therefore the controller can still incur large-document cost before the compact token-window learner runs. This does not satisfy a full-corpus long-input upgrade contract.

Keep:

`BOUNDED_FILE_IO=NOT_PROVEN`

`GENERAL_REAL_LONG_DOCUMENT_CONTROLLER_RECOVERY=NOT_PROVEN`

Correction requirement:

- inventory locked-VM mechanical file-I/O ABI;
- reuse an admitted bounded/ranged read primitive if one exists;
- otherwise teach/admit the smallest mechanical bounded file-read primitive before claiming full-corpus long-document operation;
- segment/range coordinates must be computed by native SIGMA, not host policy.

### 4. Sequential traversal is not corpus evaluation/priority

R1 selects the first eligible `.document` in a sorted cursor traversal. This is native document selection, but it is not a proof that SIGMA evaluates the archive and prioritizes learning work from corpus evidence.

Correction requirement:

- add a native corpus-evaluation/profile phase with compact per-document persisted state;
- evaluation must cover stored documents incrementally without an unbounded global ledger;
- native SIGMA must choose learning priority from its persisted structural evidence;
- host document/work/priority selection remains forbidden.

## Locked runtime identities remain

`SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

`SIGMA_VM_V0_9_CANDIDATE_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

No corrected capability may be admitted without equality-gating both identities, locked-SIGMAC compile, and locked-VM runtime proof.

## Host boundary

`HOST_DOCUMENT_SELECTION=NO`

`HOST_SEGMENT_SELECTION=NO`

`HOST_WINDOW_SELECTION=NO`

`HOST_CORPUS_PRIORITY=NO`

`HOST_RETRY_DECISION=NO`

`HOST_COMPLETION_DECISION=NO`

`HOST_LEARNING=NO`

## Next action

`NEXT_ACTION=DESIGN_AND_STATIC_AUDIT_V4C2R2_WITH_BOUNDED_NATIVE_CORPUS_IO_AND_NATIVE_CORPUS_EVALUATION_BEFORE_ANY_RUNTIME`
