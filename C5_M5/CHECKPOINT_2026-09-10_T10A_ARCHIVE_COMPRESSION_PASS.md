# SIGMA C5 M5 — T10A Archive / Compression PASS

Date: 2026-09-10

## Result

Genuine OPPO/Termux current-standard admission PASS for T10A Archive / Compression.

The earlier libarchive-dependent T10A attempt was HOLD at compile time because `archive.h` was unavailable. No checkpoint was published for that HOLD. This admitted FIX1 removes the libarchive build dependency and uses native ZIP/TAR parsing.

## Frozen OPPO artifact

- source SHA256 `545a32122f1626f5674e952e1005cd10c190c0b00494608a98dbb00011cf7004`
- binary SHA256 `bc519755d46b068f5bfe7fec9b4809990411c35b05a75ce30af80cc0ff0cbb4b`
- compiler `/data/data/com.termux/files/usr/bin/clang++`
- archive backend `NATIVE_ZIP_TAR`
- gzip backend `ZLIB`
- zstd backend `RUNTIME_LIBZSTD`

## Admission evidence

- bundle manifest PASS
- harness syntax PASS
- deterministic compile PASS
- source hash freeze PASS
- binary hash freeze PASS
- high-entropy literal leak audit PASS
- dynamic archive fixtures generated after freeze PASS
- directed cases `16`
- randomized-after-freeze cases `32`
- replay cases `2`
- total admission cases `50`
- total native process invocations `54`
- post-tool mechanical oracle PASS

## Admitted mechanical scope

- bounded gzip streaming decompression
- bounded zstd decompression through runtime-loaded libzstd
- bounded native ZIP scan
- bounded native TAR scan
- archive path traversal rejection
- absolute-path rejection
- backslash-traversal rejection
- symlink/hardlink rejection
- duplicate-path rejection
- member-count bound
- per-member uncompressed-size bound
- total uncompressed-size bound
- path-depth bound
- expansion-ratio bound
- counterfactual archive-content change PASS

Archive members are not extracted to the filesystem. Regular-file contents are bounded and represented mechanically through canonical path/size/SHA256 manifest data.

## Exact scope boundary

ZIP support is scoped to the admitted native parser subset: standard single-disk, non-ZIP64, unencrypted ZIP with stored/deflate member methods supported by the implementation. Unsupported variants fail closed rather than being interpreted.

TAR support is scoped to admitted regular-file/directory mechanics; links and special records are rejected.

## Anti-hardcoding / cognition boundary

- `NO_FILESYSTEM_EXTRACTION=PASS`
- `NO_OCR=PASS`
- `NO_SEMANTIC_DOCUMENT_INTERPRETATION=PASS`
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

Tool availability is not cognitive adoption, document understanding, evidence relevance, or trust judgment.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Layer state

- `T10A_ARCHIVE_COMPRESSION_ADMISSION=PASS`
- `T10_FULL_LAYER=PENDING_T10B_DOCUMENT_CONTAINERS_AND_COMBINED`
- next: T10B EPUB / deterministic PDF text-layer / MIME multipart + charset, then exact T10A+T10B combined admission.
