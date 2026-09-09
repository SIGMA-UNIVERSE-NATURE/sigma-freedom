# SIGMA C5 M5 — Window Handoff

Updated: 2026-09-09 after genuine OPPO T4C PASS.

## Operating split

- **Online synchronization lane:** consumes only genuine admitted checkpoints and owns live C5V3 synchronization/integration testing.
- **Offline tool-substrate lane:** continues independently through T4 -> T11 and never waits for online integration.
- Tool availability is distinct from SIGMA cognitive adoption/tool selection.
- Production binding from this offline lane remains NO.

## Production fingerprints

- production core: `23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc`
- production runner: `092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847`
- sigmac: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- locked VM: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

## Synchronization evidence already admitted

- R5 production↔M5 structural delta: PASS.
- R6 production-lineage latent candidate: PASS.
  - source `dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac`
  - bytecode `dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693`
- R7 isolated production-runner ABI regression: PASS.
- R8 M5 dispatch structural map: PASS.
- R9 FIX1 source-derived dispatch contract: PASS.
- R10 explicit production-lineage M5 dispatch bridge + dormant production regression: PASS.
  - source `7d9e91f9a5a7fa265ca4304084fc48aca105b74ae7ca08662398b535c8d3cd34`
  - bytecode `c837fcc03f79f64487d9146fc268783c13bf0769352a2068492c1d4374b109c5`

R10 activation was not admitted by prior observer attempts; online integration owns further activation work. Do not infer live binding from R10 or tool-substrate checkpoints.

## Native tool-substrate chain

- T0 primitives: inherited only where exact prior evidence applies.
- T1 Vector/Matrix: ADMITTED current-standard subset.
- T2 Bounded Graph/Traversal: ADMITTED current-standard subset.
- T3 Local Index/BM25: ADMITTED current-standard subset.
- T1/T2/T3 mixed compatibility: PASS.

### T4A — PASS

Checkpoint: `C5_M5/CHECKPOINT_2026-09-09_T4A_NATIVE_TEXT_CODECS_FRAMING_PASS.md`

- source `af36c1b4ee4491533e93b878dc9d0de475f6561f35dd3979fa5b8bbb6d60d572`
- binary `45455d007e0cb722752c4cf06cd8919b66b20e5064939781e4dfa94f057c78db`

Scope: strict UTF-8 validation, Unicode codepoint iteration, hex, strict Base64, canonical unsigned varint/LEB128, bounded deterministic `S4F1` MessagePack-like typed framing.

### T4B — PASS

Checkpoint: `C5_M5/CHECKPOINT_2026-09-09_T4B_NATIVE_JSON_CSV_URL_MIME_PASS.md`

- source `31a89e66943d8e0489c9c2df65331bb60bc6a8e326e0bcb338e2adb7a15f93d6`
- binary `5452a7c89b8107dc6b51714b4d97639683683e42dd7e975a93fea990e3924d47`

Scope: bounded strict JSON validation/minification, bounded CSV parsing + deterministic CRLF normalization, URL percent codec + absolute component parsing, MIME `Content-Type` + parameters.

### T4C — PASS

Checkpoint: `C5_M5/CHECKPOINT_2026-09-09_T4C_NATIVE_XML_HTML_UNICODE_VIEW_PASS.md`

- source `5e120a48dd9af95913b12e1be10e41c4a7e1b30c2958951f2c9719b5305b8d47`
- binary `cb59635616ae41e7c50f9bcd55907dc7b40e4675d67f49b081584dd13ade4fb9`
- ICU/libxml2 discovery: `PKG_CONFIG`

Scope: NFC/NFD/NFKC/NFKD as **explicit derived view only**, raw byte preservation, normalized-state check, bounded XML structural parsing with network disabled and doctype/DTD rejection, bounded HTML structural parsing.

Each T4 wave passed 16 directed + 32 randomized-after-freeze + 2 replay = 50 native invocations plus deterministic compile, source/binary freeze, resource bound and mechanical oracle.

## Anti-hardcoding doctrine

For every remaining layer:

- capability, not answers;
- no case-ID-dependent tool behavior;
- no expected-output literals in native tool implementation;
- randomized/high-entropy inputs generated after freeze;
- expected values only in external mechanical oracle;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`;
- no test cognition imported into SIGMA state;
- no claim of cognitive adoption from tool availability;
- claim never exceeds exact evidence.

## Current exact state

- `T4A=PASS`
- `T4B=PASS`
- `T4C=PASS`
- `T4_COMBINED_COMPATIBILITY=PENDING`
- `T4_FULL_LAYER=NOT_YET_ADMITTED`
- `ONLINE_SYNC=NO` from this offline lane
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Next offline sequence

`T4 combined -> T5 -> T6 -> T7 -> T8 -> T9 -> T10 -> T11`

Only after genuine T4 combined PASS may `T4_FULL_LAYER=PASS` be published.
