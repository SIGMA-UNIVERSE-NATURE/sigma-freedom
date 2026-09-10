# SIGMA C5 M5 — T10B Document Containers PASS

Date: 2026-09-10

## Verdict

Genuine OPPO/Termux admission PASS for scoped T10B document-container mechanics.

- `T10B_DOCUMENT_CONTAINERS_ADMISSION=PASS`
- `RESULT=T10B_PASS`
- `T10_FULL_LAYER=PENDING_T10A_T10B_COMBINED`

## Frozen OPPO artifact

- source SHA256 `0b4afa5cc2c8ce34392f475bacf71ac75baf468ac85f2d5f3c1d50f36fe36977`
- binary SHA256 `0c863758f53616c44f074ea6be7392e1df168aea08035b7f4b7f98cd1881d1e1`
- compiler `/data/data/com.termux/files/usr/bin/clang++`
- PDF backend `NATIVE_CLASSIC_XREF`
- XML backend `LIBXML2`
- ZIP backend `NATIVE_STANDARD_ZIP`

## Admission evidence

- deterministic compile PASS
- source/binary freeze PASS
- high-entropy literal leak audit PASS
- dynamic document fixtures after freeze PASS
- directed cases `16`
- randomized-after-freeze cases `32`
- replay cases `2`
- total cases `50`
- native process invocations `56`
- post-tool mechanical oracle PASS

EPUB:

- mimetype/structure validation PASS
- container XML NONET PASS
- OPF manifest/spine resolution PASS
- path and size bounds PASS

PDF text layer:

- deterministic native text-layer extraction PASS
- classic xref/page tree PASS
- Flate stream decode PASS
- ToUnicode CMap mechanics PASS
- text operators `Tj`, `TJ`, quote operators PASS
- image-only/no-text PDF -> empty text PASS
- output bound PASS
- OCR not used

MIME / charset:

- bounded recursive multipart PASS
- Base64 decode PASS
- quoted-printable decode PASS
- UTF-8 / ASCII / ISO-8859-1 / Windows-1252 decode PASS
- decoded-total bound PASS

Other gates:

- counterfactual document change PASS
- synthetic sandbox removal PASS
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

## Next

Run exact T10A + T10B combined admission, including mechanical regression against admitted T9B source/work/span provenance. Only a genuine combined PASS may advance `T10_FULL_LAYER=PASS`.
