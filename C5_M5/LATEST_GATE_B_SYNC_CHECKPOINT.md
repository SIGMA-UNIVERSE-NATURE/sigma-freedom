# SIGMA C5V3 Gate B — Latest Synchronization Checkpoint

Updated: 2026-09-10 after genuine OPPO T10B Document Containers PASS.

## Latest authoritative checkpoint

`C5_M5/CHECKPOINT_2026-09-10_T10B_DOCUMENT_CONTAINERS_PASS.md`

## Latest admitted tool-substrate chain

- T0 inherited only where exact prior evidence applies.
- T1/T2/T3 admitted subsets + mixed compatibility PASS.
- `T4_FULL_LAYER=PASS`.
- `T5_FULL_LAYER=PASS`.
- `T6_FULL_LAYER=PASS`.
- `T7_FULL_LAYER=PASS`.
- `T8_FULL_LAYER=PASS`.
- `T9_FULL_LAYER=PASS`.
- T10A Archive / Compression: PASS.
- T10B Document Containers: PASS.
- T10 combined: PENDING.
- R7L-T01..T16: PENDING after T10 full.

## Frozen T10 artifacts

T10A:
- source `545a32122f1626f5674e952e1005cd10c190c0b00494608a98dbb00011cf7004`
- binary `bc519755d46b068f5bfe7fec9b4809990411c35b05a75ce30af80cc0ff0cbb4b`

T10B:
- source `0b4afa5cc2c8ce34392f475bacf71ac75baf468ac85f2d5f3c1d50f36fe36977`
- binary `0c863758f53616c44f074ea6be7392e1df168aea08035b7f4b7f98cd1881d1e1`
- compiler `/data/data/com.termux/files/usr/bin/clang++`
- PDF backend `NATIVE_CLASSIC_XREF`
- XML backend `LIBXML2`
- ZIP backend `NATIVE_STANDARD_ZIP`

## T10B admitted evidence

- deterministic compile/source/binary freeze PASS
- 16 directed + 32 randomized-after-freeze + 2 replay = 50 cases
- 56 native process invocations
- EPUB mimetype/container/OPF/spine/path/size mechanics PASS
- deterministic native PDF text-layer extraction PASS
- classic xref/page tree, Flate stream, ToUnicode and text-operator mechanics PASS
- image-only PDF -> empty text / no OCR PASS
- recursive MIME multipart + Base64 + quoted-printable PASS
- UTF-8/ASCII/ISO-8859-1/Windows-1252 decode PASS
- decoded-total/output bounds PASS
- counterfactual/no-mutation/leak/sandbox-removal gates PASS

## Claim boundary

- `T10_FULL_LAYER=NOT_YET_ADMITTED`
- `NO_OCR=PASS`
- `NO_SEMANTIC_LAYOUT_UNDERSTANDING=PASS`
- `NO_DOCUMENT_RELEVANCE_JUDGMENT=PASS`
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Next offline sequence

Exact T10A + T10B combined admission with admitted T9B source/work/span provenance regression. On genuine PASS: `T10_FULL_LAYER=PASS`, then begin R7L-T01..T16 offline tool-substrate program.
