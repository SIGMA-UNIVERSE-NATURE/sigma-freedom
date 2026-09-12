# SIGMA — LATEST VERIFIED RESULT

> Branch: `SIGMA_LIFE`  
> Policy: keep only the latest verified gate result in GitHub; local cache is the performance layer. Intermediate diagnostics, raw machine state, absolute local paths, terminal logs, and sensitive host data are not retained here.

## Current verified result

- `GATE=S2.5R6_EXACT_S2_OUTPUT_ROOT_RESOLUTION`
- `CHECKPOINT_STATUS=VERIFIED_HOLD`
- `S3_ALLOWED=NO`
- `LIVE_R14_BINDING_REVIEW=HOLD`
- `EVIDENCE_COLLECTION=PASS`
- `EVIDENCE_TRUNCATED=NO`
- `PRODUCTION_STATE_MUTATED=NO`
- `S2P5R6_RC=10`

## Provenance anchors

- `EVIDENCE_ZIP_SHA256=8dcbafab026c7018ac3959c3a8da8d26f5d733f68646e351327d79feda6b7ca4`
- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- `LOCKED_SIGMAC=PASS`
- `LOCKED_VM=PASS`
- `EXECUTION_MODE=READ_ONLY`

## Resolution result

- `S2_OUTPUT_ROOT_COUNT=5`
- `S2_OUTPUT_ROOT_DISCOVERY_TRUNCATED=NO`
- `METADATA_PROVENANCE_QUALIFIED_ROOT_COUNT=1`
- `DEEP_SCAN_EXECUTED=YES`
- `DEEP_SCAN_ROOT_COUNT=1`
- `EXACT_ROOT_COUNT=0`
- `UNIQUE_EXACT_ROOT=NO`
- `LIVE_BINDING_ROOT_PRESENT=YES`
- `LIVE_BINDING_EXACT_S2_IDENTITY=NO`
- `LIVE_BINDING_STRUCTURAL_ABI=NO`

Normalized root resolution:

- 4 discovered S2 output roots rejected because provenance reference was missing.
- 1 root matched S2 pass/source/bytecode/provenance and was deep-scanned.
- That root was rejected by `NO_BINDING_CHAIN`.

## Blocking condition

`BLOCKER=NO_COHERENT_BINDING_CHAIN`

The metadata/provenance-qualified S2 root is identified, but there is no coherent live binding chain sufficient to establish exact S2 identity plus structural ABI. Therefore no exact qualified root exists and S3 remains disallowed.

## Cache policy

Reuse local inventory only when all cache identity components remain unchanged:

`SIGMAC_SHA256 | VM_SHA256 | CONTRACT_VERSION | GATE_VERSION | CANDIDATE_LIVE_STATE_FINGERPRINT`

Any change invalidates the local cache and requires a rescan. GitHub stores only provenance-safe result state, not raw runtime inventory.

## Authority boundary

- `HOST_LEARNING=NO`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `HOST_TOOL_SELECTION=NO`
- `AUTO_ACQUIRE=NO`
- `AUTO_EXECUTE=NO`
- `NEWEST_OR_TIMESTAMP_SELECTION=FORBIDDEN`
- `PATH_PREFIX_SELECTION=FORBIDDEN`

## Final

`RESULT=HOLD`

`REASON=NO_BINDING_CHAIN`

`S3_ALLOWED=NO`
