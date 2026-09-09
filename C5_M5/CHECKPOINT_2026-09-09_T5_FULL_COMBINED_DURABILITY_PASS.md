# SIGMA C5 M5 — T5 FULL Combined Durability PASS

Date: 2026-09-09

## Result

`T5_A_B_COMBINED_DURABILITY=PASS`

`T5_FULL_LAYER=PASS`

This is a genuine OPPO machine PASS for the exact admitted T5A/T5B artifacts in the combined durability scope below.

## Frozen admitted artifacts

T5A filesystem/atomic/lock:

- source SHA256 `8d9732ec977864f12c5ebc5cd975c1d1db2d2b1cd8a186e7df8594f3754864ba`
- binary SHA256 `59156dfd74889f64228f042e332a44146e2f10cd2cdb75fd5bb091dff7fc16aa`

T5B durable KV/WAL/recovery:

- source SHA256 `dc2397501498336a1ff0e1bd5d2392e022a36fe2918591e15edc67266adf2c7a`
- binary SHA256 `e73cd4fa7f0ca09917c2b1029a57591e1ab50d327e92e143a77fa3d9fe6b8e3c`

Compiler: `/data/data/com.termux/files/usr/bin/clang++`

## Combined machine evidence

- `T5A_SOURCE_LOCK=PASS`
- `T5B_SOURCE_LOCK=PASS`
- deterministic compile PASS for both artifacts
- admitted binary rebuild locks PASS for both artifacts
- directed combined cases: `16`
- randomized combined cases after freeze: `32`
- replay combined cases: `2`
- total combined cases: `50`
- total native process invocations: `310`
- `MIXED_FILESYSTEM_DURABLE_STATE_ORACLE=PASS`
- `T5A_DRIVEN_PARTIAL_WAL_RECOVERY=PASS`
- `T5A_DRIVEN_WAL_CORRUPTION_REJECTION=PASS`
- `T5A_DRIVEN_CHECKPOINT_CORRUPTION_REJECTION=PASS`
- `LOCK_EXCLUSIVITY_WITH_DURABLE_STORE_PRESENT=PASS`
- `COUNTERFACTUAL_BEHAVIOR_CHANGE=PASS`
- `SOURCE_BINARY_NO_MUTATION=PASS`
- `HIGH_ENTROPY_LITERAL_LEAK_AUDIT=PASS`
- `SYNTHETIC_SANDBOX_REMOVED=PASS`

## Exact admitted T5 mechanical scope

Filesystem/durability substrate now includes:

- read/write, pread/pwrite, seek/read;
- stat, mkdir, deterministic list, rename, unlink;
- fsync(file), fsync(directory);
- atomic temp-write -> fsync(file) -> rename -> fsync(parent);
- exclusive advisory file lock;
- non-expiring owner-token lease primitive;
- byte KV put/get/delete;
- multi-operation transaction;
- exact CAS;
- sequence-numbered CRC32 WAL;
- WAL fsync before commit/apply acknowledgement;
- snapshot;
- atomic checkpoint + WAL compaction;
- rollback via durable RESET WAL from checksummed snapshot;
- restart replay;
- incomplete trailing WAL recovery;
- complete corrupted WAL rejection;
- corrupted checkpoint rejection;
- malformed transaction rejection without partial mutation.

The combined test additionally proves T5A filesystem primitives can inspect/fault-inject T5B durable files and T5B responds correctly across restart/recovery boundaries.

## Claim boundaries

- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`
- T5B concurrent-writer serialization is not claimed internally; exclusive writer coordination must use the admitted T5A lock/lease primitive.
- CRC32 is mechanical corruption detection only; cryptographic identity/provenance remains T9.
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`

## Production boundary

- `ONLINE_SYNC=NO` from this offline substrate lane
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

This checkpoint does not claim T5 is already bound into live C5V3.

## Next

Proceed to `T6_TRANSPORT`:

`DNS -> TCP -> TLS -> HTTP/HTTPS -> Range -> chunked streaming -> redirects -> ETag/If-Range/conditional fetch -> timeout -> retry -> rate limit -> backpressure`.
