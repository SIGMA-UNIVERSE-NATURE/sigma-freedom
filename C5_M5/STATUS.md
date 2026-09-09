# SIGMA C5 M5 — Current Status

Updated: 2026-09-09 after genuine OPPO T5 FULL combined durability PASS.

## Architecture routing

- Gate A: native cognition/memory capability development and blind testing.
- Gate B: C5/C5V3 synchronization + native mechanical tool substrate.
- Online synchronization/test lanes and offline substrate lane operate independently.
- Production binding remains NO from this offline lane.

## Production fingerprints

- production core `23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc`
- production runner `092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847`
- sigmac `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- locked VM `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

## Synchronization boundary

Admitted offline synchronization chain remains R5 -> R10. R10 structural/dormant evidence does not imply live activation or binding. Online integration/activation work is owned by the separate synchronization lane.

From this offline substrate lane:

- `C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO`
- `M5_CAPABILITY_ACTIVE_IN_LIVE_PRODUCTION_DISPATCH=NO`
- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Native tool-substrate chain

- T0 primitives: inherited only where exact prior evidence applies.
- T1 Vector/Matrix: ADMITTED current-standard subset.
- T2 Bounded Graph/Traversal: ADMITTED current-standard subset.
- T3 Local Index/BM25: ADMITTED current-standard subset.
- T1/T2/T3 mixed compatibility: PASS.
- `T4_FULL_LAYER=PASS`.

## T5 — FULL PASS

Authoritative checkpoint:

`C5_M5/CHECKPOINT_2026-09-09_T5_FULL_COMBINED_DURABILITY_PASS.md`

Frozen OPPO artifacts:

- T5A source `8d9732ec977864f12c5ebc5cd975c1d1db2d2b1cd8a186e7df8594f3754864ba`
- T5A binary `59156dfd74889f64228f042e332a44146e2f10cd2cdb75fd5bb091dff7fc16aa`
- T5B source `dc2397501498336a1ff0e1bd5d2392e022a36fe2918591e15edc67266adf2c7a`
- T5B binary `e73cd4fa7f0ca09917c2b1029a57591e1ab50d327e92e143a77fa3d9fe6b8e3c`
- compiler `/data/data/com.termux/files/usr/bin/clang++`

Exact T5 admitted scope:

- read/write, pread/pwrite, seek/read;
- stat, mkdir, deterministic list, rename, unlink;
- fsync(file), fsync(directory);
- atomic temp-write + fsync(file) + rename + fsync(parent);
- advisory exclusive lock + owner-token lease;
- byte KV put/get/delete;
- multi-op transaction;
- exact CAS;
- sequence-numbered CRC32 WAL with fsync-before-commit/apply acknowledgement;
- snapshot;
- atomic checkpoint + WAL compaction;
- durable rollback via RESET WAL from checksummed snapshot;
- restart replay;
- incomplete trailing WAL recovery;
- complete corrupted WAL rejection;
- corrupted checkpoint rejection;
- malformed transaction rejection without partial mutation.

Combined evidence:

- exact T5A/T5B source/binary rebuild locks PASS;
- directed combined cases `16`;
- randomized-after-freeze combined cases `32`;
- replay combined cases `2`;
- total combined cases `50`;
- native process invocations `310`;
- mixed filesystem/durable-state oracle PASS;
- T5A-driven partial-WAL recovery PASS;
- T5A-driven WAL corruption rejection PASS;
- T5A-driven checkpoint corruption rejection PASS;
- lock exclusivity with durable store present PASS;
- counterfactual behavior change PASS;
- source/binary no mutation PASS;
- high-entropy leak audit PASS;
- synthetic sandbox removed PASS;
- `T5_A_B_COMBINED_DURABILITY=PASS`;
- `T5_FULL_LAYER=PASS`.

Claim boundaries:

- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`;
- T5B internal concurrent-writer serialization is not claimed; use T5A lock/lease for exclusive writer coordination;
- CRC32 is mechanical corruption detection only; cryptographic identity/provenance remains T9;
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`;
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`.

## Exact next offline substrate sequence

`T6 -> T7 -> T8 -> T9 -> T10 -> T11`

Immediate next layer: **T6 Transport**.
