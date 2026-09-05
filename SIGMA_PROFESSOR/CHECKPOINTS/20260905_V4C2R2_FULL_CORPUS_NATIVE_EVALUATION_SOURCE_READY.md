# V4-C2 R2 FULL-CORPUS NATIVE EVALUATION — SOURCE READY FOR FIRST LOCKED COMPILE

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`V4C2R2_SOURCE_READY=YES`

`V4C2R2_LOCKED_SIGMAC_COMPILE=NOT_RUN`

`V4C2R2_LOCKED_VM_RUNTIME=NOT_RUN`

`V4C2R2_ADMISSION=NOT_RUN`

`V4C2R2_CONTINUOUS_SHADOW_RUNNER=NOT_CREATED_UNTIL_PREFLIGHT_PASS`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

R1 remains blocked and MUST NOT be run:

`V4C2R1_ADMISSION=BLOCKED_BY_STATIC_AUDIT`

## Production discipline

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`UPGRADE_V2_4_IN_PLACE=NO`

R2 is an isolated shadow successor candidate.

## Locked runtime identities

`SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

`SIGMA_VM_V0_9_CANDIDATE_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

## R2 design

Path:

`SIGMA_PROFESSOR/DESIGN/SIGMA_V4C2R2_FULL_CORPUS_NATIVE_EVALUATION_AND_LEARNING_V1.md`

The R2 controller uses three native phases:

`PROFILE STORED CORPUS -> GLOBAL NATIVE PRIORITY -> DEEP LEARN SELECTED DOCUMENT -> LOOP`

The profile phase teaches the first non-empty native-selected line of every eligible stored document, so corpus evaluation is also real learning rather than a host fixture.

The priority phase performs a bounded native tournament over compact per-document profiles.

The learn phase resumes the selected document's native persisted line cursor and invokes the compact token-window learner until native EOF completion or native refusal/hold.

## Raw-content I/O correction from R1

R2 controller source does NOT `read_text` complete production raw documents.

Native SIGMA emits an exact corpus-read request containing document ID, native line cursor and purpose. The host may transport exactly that requested line and return mechanical FOUND/NOT_FOUND only.

`HOST_DOCUMENT_SELECTION=NO`

`HOST_LINE_SELECTION=NO`

`HOST_WINDOW_SELECTION=NO`

`HOST_CORPUS_PRIORITY=NO`

`HOST_RETRY_DECISION=NO`

`HOST_COMPLETION_DECISION=NO`

`HOST_LEARNING=NO`

The repository ABI inventory lists `read_bytes`, but its offset/count semantics remain unknown. R2 does not invent an undocumented signature.

Keep:

`BOUNDED_VM_CORPUS_INPUT_PER_TRANSPORT=ONE_REQUESTED_LINE`

`BOUNDED_FILE_IO=NOT_PROVEN`

## Native source A — minimal compact corpus arbiter

Path:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_CORPUS_WORK_ARBITER_V4A3R1.sigma`

`V4A3R1_GIT_BLOB=336078bde9d3407c0e75f10834e47bfe8726c40a`

`V4A3R1_SOURCE_SHA256=UNKNOWN_UNTIL_DEVICE_HASH`

Sources admitted for arbitration in this revision:

- RECEIVED
- RETRYABLE
- CORPUS_READ
- RECOVERED

External fetch and local curriculum are intentionally not composed into this first R2 gate.

## Native source B — compact line span learner

Path:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_COMPACT_LINE_SPAN_LEARNER_V4B4R2.sigma`

`V4B4R2_GIT_BLOB=12a9b6345786ade253fb8f72abbb20b1ca791cb5`

`V4B4R2_SOURCE_SHA256=UNKNOWN_UNTIL_DEVICE_HASH`

Properties to be proven at runtime:

- 16-token compute window;
- compact token cursor;
- 2-token / 3-token / 4-token structural span evidence;
- longer span tie preference;
- native completion after all windows of the exact transported line;
- no host window/retry/completion/learning decisions.

## Native source C — full-corpus evaluation controller

Path:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_FULL_CORPUS_EVALUATION_CONTROLLER_V4C2R2.sigma`

`V4C2R2_GIT_BLOB=bf2134acc6a4d81e5c18ced6e0db158236eb1c40`

`V4C2R2_SOURCE_SHA256=UNKNOWN_UNTIL_DEVICE_HASH`

Controller state is compact/global plus independent per-document state. Evidence archives are provenance and are not globally scanned for scheduling.

The priority policy in this source-ready revision is structural:

`SPAN_WIDTH_DESC -> SUPPORT_DESC -> FIRST_NATIVE_TRAVERSAL_TIE`

`SEMANTIC_IMPORTANCE=NOT_PROVEN`

## Canonical first real-corpus preflight

Path:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C2R2_REAL_CORPUS_NATIVE_EVALUATION_PREFLIGHT.sh`

`V4C2R2_PREFLIGHT_GIT_BLOB=927b632f9c21155c8f63d6c54482226e68d7784b`

`V4C2R2_PREFLIGHT_SHA256=UNKNOWN_UNTIL_DEVICE_HASH`

Default fixed controller budget:

`FIXED_CONTROLLER_TURNS=8192`

Host never terminates early because a native completion/status is observed.

Preflight gates:

- exact locked SIGMAC and VM identities;
- exact source Git blobs;
- compile all three native modules;
- real stored raw corpus only;
- native exact line-read request observed;
- native learning observed;
- native document profile committed;
- native pair/triple/quad occurrences each observed before corresponding PASS claims;
- zero real-corpus document hold in the tested run;
- full native profile pass and priority selection observed within fixed budget;
- every raw document that existed at preflight start still exists with identical bytes;
- new V2.4 documents may be appended during preflight;
- V2.4 remains the same PID.

If the fixed budget is insufficient to finish a real-corpus profile pass, the gate must HOLD rather than invent a global-priority claim.

## Known limits before runtime

`CORRUPTED_PROFILE_RECOVERY=NOT_PROVEN`

`CRASH_ATOMICITY=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`VERY_LONG_SINGLE_LINE_RECOVERY=NOT_PROVEN`

`FULL_CORPUS_COMPLETION=NOT_PROVEN`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

These limits do not permit host repair of native state.

## Required next action

`NEXT_ACTION=INSTALL_EXACT_R2_SOURCES_AND_PREFLIGHT_THEN_PRESERVE_FIRST_LOCKED_COMPILE_RUNTIME_RESULT`

Do not create or launch the persistent continuous shadow runner until this preflight produces a valid PASS checkpoint.
