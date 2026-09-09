# SIGMA Gate B Tool Substrate — T5A Filesystem / Atomic Commit / Lock — PASS

Date: 2026-09-09

## Exact OPPO-admitted artifact

- source SHA256: `8d9732ec977864f12c5ebc5cd975c1d1db2d2b1cd8a186e7df8594f3754864ba`
- native binary SHA256: `59156dfd74889f64228f042e332a44146e2f10cd2cdb75fd5bb091dff7fc16aa`
- compiler: `/data/data/com.termux/files/usr/bin/clang++`

## Exact admitted scope

T5A admits native mechanical primitives for:

- read / write;
- pread / pwrite;
- seek + read;
- stat;
- mkdir;
- deterministic sorted directory listing;
- rename;
- unlink;
- fsync(file);
- fsync(directory);
- atomic temp-write -> fsync(file) -> rename -> fsync(parent directory);
- exclusive advisory file-lock acquisition / nonblocking contention probe;
- non-expiring owner-token lease acquire/release using exclusive creation and parent-directory fsync.

`mmap` is optional in the roadmap and is NOT claimed by this checkpoint.

## Current-standard evidence

- deterministic compile: PASS;
- source hash freeze: PASS;
- binary hash freeze: PASS;
- high-entropy literal leak audit: PASS;
- directed cases: `16`;
- randomized cases generated after freeze: `32`;
- replay cases: `2`;
- total admission cases: `50`;
- total native process invocations: `58`;
- post-tool mechanical oracle: PASS;
- file lock exclusivity: PASS;
- atomic-replace counterfactual: PASS;
- file fsync primitive: PASS;
- directory fsync primitive: PASS;
- atomic rename/commit primitive: PASS;
- non-expiring lease-token primitive: PASS;
- synthetic sandbox removed: PASS.

## Anti-hardcoding / cognition boundary

- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`;
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`;
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`.

This checkpoint supplies mechanical storage primitives only. It does not decide what SIGMA should persist, when to commit memory, which state is semantically valid, or which evidence matters.

## Production boundary

- `ONLINE_SYNC=NO` from this offline admission lane;
- `PRODUCTION_STATE_WRITE=NO`;
- `PRODUCTION_MUTATION=NO`;
- `PRODUCTION_BINDING=NO`.

All mutable admission state was isolated to a synthetic test sandbox and removed after evidence extraction.

## Layer boundary

- `T5A_FILESYSTEM_ATOMIC_LOCK_ADMISSION=PASS`;
- `T5_FULL_LAYER=PENDING_T5B_DURABLE_STATE_AND_COMBINED`.

T5A does NOT yet admit durable KV, transaction, CAS, WAL, snapshot/checkpoint, rollback, checksum-corruption handling, interrupted-commit recovery, or full restart durability.

## Next

Build and admit T5B durable state:

`KV -> transaction -> CAS -> WAL -> snapshot/checkpoint -> rollback -> corruption checksum -> interrupted-commit/restart recovery`

Then run exact T5A+T5B combined durability before advancing `T5_FULL_LAYER=PASS`.
