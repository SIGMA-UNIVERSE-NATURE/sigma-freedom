# SIGMA Gate B Tool Substrate — T5B Durable KV/WAL/Recovery — PASS

Updated: 2026-09-09 after genuine OPPO admission.

## Result

`T5B_DURABLE_STATE_ADMISSION=PASS`

`T5_FULL_LAYER=PENDING_T5A_T5B_COMBINED_DURABILITY`

This checkpoint admits native mechanical durable-state capability only. It does not claim SIGMA cognitive tool adoption, production binding, or live synchronization.

## Frozen OPPO artifact

- source SHA256: `dc2397501498336a1ff0e1bd5d2392e022a36fe2918591e15edc67266adf2c7a`
- native binary SHA256: `e73cd4fa7f0ca09917c2b1029a57591e1ab50d327e92e143a77fa3d9fe6b8e3c`
- compiler: `/data/data/com.termux/files/usr/bin/clang++`

FIX1 changed only the replay harness: exact replay uses isolated immutable dynamic stores seeded after source/binary freeze. Native T5B source remained unchanged.

## Exact admitted scope

- byte-key / byte-value KV put/get/delete;
- multi-operation transaction encoded as one WAL transaction;
- exact-byte / exact-absence compare-and-swap;
- sequence-numbered WAL;
- CRC32 mechanical corruption checksum;
- WAL fsync before commit/apply acknowledgement;
- checksummed snapshot;
- atomic checkpoint + WAL compaction;
- rollback via a new durable RESET WAL transaction derived from a checksummed snapshot;
- restart replay;
- incomplete trailing WAL recovery;
- complete corrupted WAL rejection;
- corrupted checkpoint rejection;
- malformed transaction rejection without partial mutation.

CRC32 here is only mechanical corruption detection. Cryptographic identity/provenance remains T9.

## OPPO machine evidence

- `DETERMINISTIC_COMPILE=PASS`
- `SOURCE_HASH_FREEZE=PASS`
- `BINARY_HASH_FREEZE=PASS`
- `HIGH_ENTROPY_LITERAL_LEAK_AUDIT=PASS`
- directed cases `16`
- randomized cases after freeze `32`
- replay cases `2`
- total admission cases `50`
- total native process invocations `73`
- `POST_TOOL_MECHANICAL_ORACLE=PASS`
- `KV_PUT_GET_DELETE=PASS`
- `MULTI_OP_TRANSACTION=PASS`
- `CAS=PASS`
- `WAL_FSYNC_BEFORE_APPLY=PASS`
- `SNAPSHOT=PASS`
- `CHECKPOINT_COMPACTION=PASS`
- `ROLLBACK_VIA_DURABLE_RESET_WAL=PASS`
- `TRAILING_PARTIAL_WAL_RECOVERY=PASS`
- `COMPLETE_WAL_CHECKSUM_CORRUPTION_REJECTED=PASS`
- `CHECKPOINT_CHECKSUM_CORRUPTION_REJECTED=PASS`
- `INVALID_TRANSACTION_NO_PARTIAL_MUTATION=PASS`
- `RESTART_REPLAY=PASS`
- `SYNTHETIC_SANDBOX_REMOVED=PASS`

## Anti-hardcoding / cognition boundary

- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

The harness may calculate mechanical expected values externally. No expected semantic answer, relevance decision, memory policy, or cognition is embedded in the native durable-state tool.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

All mutable state used by this admission was isolated synthetic test state and removed after evidence extraction.

## Current T5 state

- T5A filesystem/atomic/lock: PASS
  - source `8d9732ec977864f12c5ebc5cd975c1d1db2d2b1cd8a186e7df8594f3754864ba`
  - binary `59156dfd74889f64228f042e332a44146e2f10cd2cdb75fd5bb091dff7fc16aa`
- T5B durable state: PASS
  - source `dc2397501498336a1ff0e1bd5d2392e022a36fe2918591e15edc67266adf2c7a`
  - binary `e73cd4fa7f0ca09917c2b1029a57591e1ab50d327e92e143a77fa3d9fe6b8e3c`
- T5 combined durability: PENDING
- `T5_FULL_LAYER=NOT_YET_ADMITTED`

## Next

Run exact T5A + T5B combined durability/restart/recovery admission. Only a genuine combined PASS may advance `T5_FULL_LAYER=PASS`. Then continue to T6 Transport.
