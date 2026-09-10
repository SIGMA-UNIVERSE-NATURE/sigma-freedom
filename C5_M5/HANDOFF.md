# SIGMA C5 M5 — Window Handoff

Updated: 2026-09-10 after genuine OPPO T10A Archive / Compression PASS.

## Operating split

- Online synchronization/test lanes consume only genuine admitted checkpoints and own live/online validation.
- This window remains the offline tool-substrate lane and continues independently through T10 -> T11.
- Tool availability is distinct from SIGMA cognitive adoption/tool selection.
- Production binding from this offline lane remains NO.

## Native tool-substrate chain

- T0 inherited only where exact prior evidence applies.
- T1/T2/T3 admitted subsets + mixed compatibility PASS.
- `T4_FULL_LAYER=PASS`.
- `T5_FULL_LAYER=PASS`.
- `T6_FULL_LAYER=PASS`.
- `T7_FULL_LAYER=PASS`.
- `T8_FULL_LAYER=PASS`.
- `T9_FULL_LAYER=PASS`.

### T10A — PASS

Checkpoint:

`C5_M5/CHECKPOINT_2026-09-10_T10A_ARCHIVE_COMPRESSION_PASS.md`

Frozen OPPO artifact:

- source `545a32122f1626f5674e952e1005cd10c190c0b00494608a98dbb00011cf7004`
- binary `bc519755d46b068f5bfe7fec9b4809990411c35b05a75ce30af80cc0ff0cbb4b`
- compiler `/data/data/com.termux/files/usr/bin/clang++`
- archive backend `NATIVE_ZIP_TAR`
- gzip backend `ZLIB`
- zstd backend `RUNTIME_LIBZSTD`

Admitted mechanical scope:

- bounded gzip decompression;
- bounded zstd decompression;
- bounded native ZIP scan;
- bounded native TAR scan;
- fail-closed path traversal / absolute / backslash path rejection;
- symlink/hardlink and duplicate-path rejection;
- member-count, member-size, total-size, path-depth and expansion-ratio bounds;
- no filesystem extraction.

Evidence: deterministic compile/source/binary freeze PASS; high-entropy/dynamic fixture gates PASS; 16 directed + 32 randomized-after-freeze + 2 replay = 50 cases / 54 native invocations; all archive safety and counterfactual gates PASS.

The previous libarchive-dependent build attempt remained HOLD and was not published. This admitted FIX1 removes the `archive.h` dependency.

## T10 boundary

- `T10A_ARCHIVE_COMPRESSION_ADMISSION=PASS`
- `T10B_DOCUMENT_CONTAINERS=PENDING`
- `T10_COMBINED=PENDING`
- `T10_FULL_LAYER=NOT_YET_ADMITTED`
- `NO_OCR=PASS`
- `NO_SEMANTIC_DOCUMENT_INTERPRETATION=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Next offline sequence

Build T10B for EPUB, deterministic PDF text-layer extraction, MIME multipart and charset decode; then exact T10A+T10B combined admission; then T11.
