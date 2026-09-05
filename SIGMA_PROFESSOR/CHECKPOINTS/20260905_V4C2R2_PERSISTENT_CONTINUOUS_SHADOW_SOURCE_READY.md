# V4-C2 R2 PERSISTENT CONTINUOUS SHADOW — SOURCE READY

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`V4C2R2_PREFLIGHT=PASS`

`V4C2R2_PERSISTENT_CONTINUOUS_SHADOW_SOURCE_READY=YES`

`V4C2R2_PERSISTENT_CONTINUOUS_SHADOW_RUNTIME=NOT_RUN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

Canonical preflight PASS checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V4C2R2_REAL_CORPUS_NATIVE_EVALUATION_PREFLIGHT_PASS.md`

## Runner

Path:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C2R2_FULL_CORPUS_CONTINUOUS_SHADOW.sh`

`GIT_BLOB=d8c354ec8df2a39410ea1f9cecb280faba809fa9`

`DEVICE_RUNNER_SHA256=UNKNOWN_UNTIL_EXACT_INSTALL`

The runner is a persistent shadow supervisor for the admitted R2 composition. It does not reset existing native phase/cursor/profile/completion state on restart.

## Locked runtime and source identities

`SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

`VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`A3_GIT_BLOB=336078bde9d3407c0e75f10834e47bfe8726c40a`

`A3_SOURCE_SHA256=5e1795b53bb8cf4633219bd789ef0c7a6a168a5102bcc0a31d922ca77333ecef`

`B4_GIT_BLOB=12a9b6345786ade253fb8f72abbb20b1ca791cb5`

`B4_SOURCE_SHA256=18b3fc60ba86635a524a5d9268326bc7bf692a82227d86f8bd269d38e8845932`

`C2_GIT_BLOB=bf2134acc6a4d81e5c18ced6e0db158236eb1c40`

`C2_SOURCE_SHA256=5f46d32f573e87e60a813b9d4f764c783395ed6250ca88b44c463179a600013d`

## Host boundary

`HOST_DOCUMENT_SELECTION=NO`

`HOST_LINE_SELECTION=NO`

`HOST_WINDOW_SELECTION=NO`

`HOST_CORPUS_PRIORITY=NO`

`HOST_RETRY_DECISION=NO`

`HOST_COMPLETION_DECISION=NO`

`HOST_LEARNING=NO`

`HOST_CORPUS_READ_TRANSPORT=EXACT_NATIVE_REQUEST_ONLY`

`PRODUCTION_RAW_READ_ONLY_SOURCE=YES`

`PRODUCTION_BRAIN_WRITE_TARGET=NO`

## Persistent-state discipline

The runner creates missing mechanical memory files only if absent. It does not clear existing R2 native state. The native C2 controller remains owner of phase, scan cursor, active document, priority, retry and completion state.

Persistent state root:

`$HOME/SIGMA/SIGMA_V4C2R2_FULL_CORPUS_CONTINUOUS_SHADOW`

On restart, the runner recompiles exact locked sources, verifies source identities, and resumes the existing native memory/corpus-state namespace.

## Stop gates

The runner stops on:

- locked SIGMAC or VM identity mismatch;
- R2 source blob/SHA mismatch;
- production V2.4 absent or PID changed during this shadow admission lane;
- compile failure;
- native manager refusal;
- native document hold;
- VM failure;
- exact native target/context mismatch;
- corpus mechanical-transport failure;
- unsupported native action.

No host repair of native state is permitted after a stop gate.

## Claim boundary

`FULL_CORPUS_CONTINUOUS_COMPLETION=NOT_PROVEN`

`PERSISTENT_RESTART_RESUME=NOT_PROVEN_UNTIL_RUNTIME`

`LONG_HORIZON_NO_HOLD=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`CRASH_ATOMICITY=NOT_PROVEN`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Next action

`NEXT_ACTION=INSTALL_EXACT_CONTINUOUS_RUNNER_AND_START_FIRST_PERSISTENT_SHADOW_RUNTIME_WITH_V2_4_STILL_RUNNING`

Preserve the first startup identities, bytecode SHA-256 values, first health lines, and first stop/pass frontier as evidence. Do not stop V2.4 for this first continuous shadow run.
