# SIGMA R4 VERIFIED CHECKPOINT — 2026-09-12

> Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`  
> Branch: `SIGMA_LIFE`  
> Checkpoint class: `VERIFIED_HOLD`  
> Scope: provenance-safe S2.5R4 gate checkpoint for cache reuse. This file intentionally excludes raw machine state, local filesystem paths, terminal logs, and other sensitive/local-only data.

## 1. Provenance

- `BUNDLE_SHA256=418bd878d965e3e991c1a112a9aa32dc7fee0455b55d9a2dfd7f2b9e5e02e372`
- `EVIDENCE_ZIP_SHA256=d282c482f2a92cef4b28a93b394d5708763bb46f4f586a28dae640e8211b3a06`
- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- Gate version: `S2.5R4_IDENTITY_PRUNED_EXACT_ROOT_GATE`
- Contract version: `S25R4_BINDING_CONTRACT`

Manifest verification: all declared package members reported `OK`.

## 2. Verification result

- `STATIC_AUDIT=PASS`
- `LOCAL_HARNESS_REGRESSION=PASS`
- `INVENTORY_MODE=METADATA_FIRST_IDENTITY_PRUNED_READ_ONLY`
- `MANIFEST_PROVENANCE_HASH_PRUNE_BEFORE_DEEP_SCAN=PASS`
- `ROOT_TRUNCATION_FAIL_CLOSED=PASS`
- `METADATA_TRUNCATION_FAIL_CLOSED=PASS`
- `DEEP_SCAN_TRUNCATION_FAIL_CLOSED=PASS`
- `LIVE_BINDING_TRUNCATION_FAIL_CLOSED=PASS`
- `S3_YES_REQUIRES_UNIQUE_EXACT_ROOT=PASS`
- `CANDIDATE_ROOT_DISCOVERY_TRUNCATED=NO`
- `CANDIDATE_METADATA_TRUNCATED=NO`
- `DEEP_SCAN_TRUNCATED=NO`
- `LIVE_BINDING_EVIDENCE_TRUNCATED=NO`
- `EVIDENCE_TRUNCATED=NO`
- `PRODUCTION_STATE_MUTATED=NO`

Authority boundary remains locked:

- `HOST_LEARNING=NO`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `HOST_TOOL_SELECTION=NO`
- `AUTO_ACQUIRE=NO`
- `AUTO_EXECUTE=NO`

## 3. Identity-pruned inventory checkpoint

Normalized aggregate state used for the checkpoint fingerprint:

- `R14_CANDIDATE_ROOT_COUNT=13`
- `CANDIDATE_METADATA_QUALIFIED_COUNT=0`
- `DEEP_SCAN_ROOT_COUNT=0`
- `EXACT_ROOT_COUNT=0`
- `UNIQUE_EXACT_ROOT=NO`
- `LIVE_BINDING_ROOT_PRESENT=YES`
- `LIVE_BINDING_S2_CAPABILITY_ID_HITS=0`
- `LIVE_BINDING_S2_SOURCE_SHA_HITS=0`
- `LIVE_BINDING_S2_BYTECODE_SHA_HITS=0`
- `LIVE_BINDING_CANDIDATE_ID_HITS=0`
- `LIVE_BINDING_DESCRIPTOR_SHA_HITS=0`
- `LIVE_BINDING_POOL_ROOT_HITS=0`
- `LIVE_BINDING_EXACT_S2_IDENTITY=NO`
- `LIVE_BINDING_STRUCTURAL_ABI=NO`
- `LIVE_R14_BINDING_REVIEW=HOLD`
- `S3_ALLOWED=NO`
- `S2P5R4_RC=10`

Therefore this is a verified checkpoint of a deterministic **HOLD** state, not an S3 admission.

## 4. Cache identity

The following fingerprint and cache key are checkpoint-derived values, not values emitted by the harness.

- Candidate/live-state fingerprint SHA-256: `cd566cede3132df2584b75d43148abb3e03448f762760e0efc7d0d1f754639bd`
- Checkpoint cache key SHA-256: `a5ea37a18f499561ecbd333a76b35525eb8f3c5defe50b47c974e727be221efe`

Cache-key material is logically:

`SIGMAC_SHA256 | VM_SHA256 | CONTRACT_VERSION | GATE_VERSION | CANDIDATE_LIVE_STATE_FINGERPRINT`

The candidate/live-state fingerprint is SHA-256 over a canonical, sorted representation of the non-sensitive aggregate gate state in Section 3 plus the gate/contract identity. It deliberately excludes local paths, timestamps, run-directory names, terminal-log locations, and raw machine contents.

## 5. Reuse / rescan policy

Reuse the locally cached R4 inventory only when all of the following remain identical:

1. `SIGMAC_SHA256`
2. `VM_SHA256`
3. gate version
4. contract version
5. candidate/live-state fingerprint

If all five identities are unchanged, reuse the verified inventory/checkpoint and do not repeat the full scan merely to reproduce the same state.

A rescan is required when any key component changes, or when the previous collection was truncated, invalid, unverifiable, or otherwise failed closed. Cache reuse never changes gate semantics: a cached `HOLD` remains `HOLD`, and `S3_ALLOWED=NO` remains authoritative until a new verified checkpoint proves the required unique exact root and live-binding identity/structural ABI conditions.

## 6. Storage policy

- Local cache: performance layer; may contain the operational inventory needed by the local harness.
- GitHub checkpoint: provenance layer; stores only hashes, versions, aggregate gate facts, decision state, and cache identity.
- Do not commit raw machine state.
- Do not commit local absolute paths, terminal logs, environment dumps, secrets, credentials, tokens, or other sensitive host data.
- Do not treat GitHub as the runtime cache itself; GitHub records provenance and verified decision checkpoints.

## 7. Current gate conclusion

`CHECKPOINT_STATUS=VERIFIED_HOLD`

`LIVE_R14_BINDING_REVIEW=HOLD`

`S3_ALLOWED=NO`

`CLAIM_SCOPE=METADATA_PRUNED_EXACT_IDENTITY_AND_STRUCTURAL_BINDING_ROOT_GATE_ONLY`
