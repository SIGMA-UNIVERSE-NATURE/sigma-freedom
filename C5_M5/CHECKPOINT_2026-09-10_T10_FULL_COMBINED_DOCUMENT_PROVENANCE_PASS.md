# SIGMA C5 M5 — T10 FULL Combined Document / Provenance PASS

Date: 2026-09-10
Lane: offline native/mechanical tool substrate
Result: genuine OPPO PASS

## Frozen admitted artifacts

T10A Archive / Compression:
- source `545a32122f1626f5674e952e1005cd10c190c0b00494608a98dbb00011cf7004`
- binary `bc519755d46b068f5bfe7fec9b4809990411c35b05a75ce30af80cc0ff0cbb4b`

T10B Document Containers:
- source `0b4afa5cc2c8ce34392f475bacf71ac75baf468ac85f2d5f3c1d50f36fe36977`
- binary `0c863758f53616c44f074ea6be7392e1df168aea08035b7f4b7f98cd1881d1e1`

T9B Identity / Provenance regression:
- source `981b8a5f5e252e9e5354167ef37affc34f2890508f55064d0eb1b28ec75a70f3`
- binary `f468db1ad900fdda0e585f71888a2e1168ba4522616c484d2752a4e51b7d3ae7`

Compiler: `/data/data/com.termux/files/usr/bin/clang++`

## Combined admission evidence

- exact T10A/T10B/T9B source locks PASS
- deterministic rebuild locks PASS
- directed combined cases `16`
- randomized-after-freeze combined cases `32`
- replay combined cases `2`
- total combined cases `50`
- native process invocations `290`
- mixed document/provenance oracle PASS
- T10A/T10B same-container compatibility PASS
- EPUB member -> source/work/exact-span provenance PASS
- PDF text-layer UTF-8 -> source/work/exact-span provenance PASS
- MIME decoded UTF-8 -> source/work/exact-span provenance PASS
- gzip/TAR exact bytes -> source/work/exact-span provenance PASS
- document-transform authenticated receipt compatibility PASS
- parser/transform identity compatibility PASS
- counterfactual document/span change PASS
- source/binary no mutation PASS
- high-entropy literal leak audit PASS
- synthetic sandbox removal PASS

## Safety / semantic-authority boundary

- `NO_OCR=PASS`
- `NO_JAVASCRIPT_EXECUTION=PASS`
- `NO_MACRO_ACTION_EXECUTION=PASS`
- `NO_DRM_EXECUTION=PASS`
- `NO_EMBEDDED_EXECUTABLE_EXECUTION=PASS`
- `NO_NETWORK=PASS`
- `NO_ARBITRARY_FILESYSTEM=PASS`
- `NO_SEMANTIC_LAYOUT_UNDERSTANDING=PASS`
- `NO_DOCUMENT_RELEVANCE_JUDGMENT=PASS`
- `HOST_TOOL_SELECTION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Result

- `T10_A_B_COMBINED_COMPATIBILITY=PASS`
- `T10_FULL_LAYER=PASS`
- `RESULT=T10_FULL_PASS`
- `NEXT=R7L_T01_NUMERIC_SERIALIZATION`

`COMBINED_TOOL_PASS != LANGUAGE_UNDERSTANDING`.
