# SIGMA Gate B Tool Substrate — T4B Native JSON/CSV/URL/MIME PASS

Updated: 2026-09-09

## Exact OPPO machine result

T4B current-standard admission passed on the OPPO/Termux target.

Frozen artifact:

- source SHA256: `31a89e66943d8e0489c9c2df65331bb60bc6a8e326e0bcb338e2adb7a15f93d6`
- native binary SHA256: `5452a7c89b8107dc6b51714b4d97639683683e42dd7e975a93fea990e3924d47`
- compiler: `/data/data/com.termux/files/usr/bin/clang++`

Admission evidence:

- `DETERMINISTIC_COMPILE=PASS`
- `SOURCE_HASH_FREEZE=PASS`
- `BINARY_HASH_FREEZE=PASS`
- `HIGH_ENTROPY_LITERAL_LEAK_AUDIT=PASS`
- `RESOURCE_BOUND_8K=PASS`
- directed invocations: `16`
- randomized invocations after freeze: `32`
- replay invocations: `2`
- total native tool invocations: `50`
- `POST_TOOL_MECHANICAL_ORACLE=PASS`
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`

Canonical machine result:

- `T4B_NATIVE_JSON_CSV_URL_MIME_ADMISSION=PASS`
- `T4_FULL_LAYER=PENDING_T4C_COMBINED`
- `RESULT=T4B_PASS`

## Exact admitted T4B scope

Mechanical substrate only:

- strict bounded JSON validation;
- JSON whitespace minification preserving token/member order;
- bounded CSV parsing;
- deterministic CSV CRLF normalization;
- URL percent encode/decode;
- absolute hierarchical URL component parsing;
- MIME `Content-Type` media type/subtype + parameter parsing.

Not admitted by T4B:

- XML;
- HTML;
- Unicode normalization views;
- MIME multipart container extraction;
- semantic interpretation of JSON/CSV/URL/MIME;
- host selection of relevant URLs/content;
- SIGMA cognitive adoption/tool selection.

MIME multipart remains a T10 concern. XML/HTML and Unicode normalization-view remain T4C.

## Anti-hardcoding / cognition boundary

The tool implementation is not keyed to test case IDs or expected fixture outputs. Randomized/high-entropy inputs are generated after source/binary freeze, and expected values exist only in the external mechanical harness.

Therefore this PASS means the native mechanical tools operate correctly in the tested scope. It does not teach SIGMA what content means or when/why to use a tool.

## Tool-substrate sequence

- T1: admitted existing subset.
- T2: admitted existing subset.
- T3: admitted existing subset.
- T4A: PASS.
- T4B: PASS.
- T4C: next.
- full T4 combined compatibility: pending after T4C.
- then continue T5 -> T6 -> T7 -> T8 -> T9 -> T10 -> T11.

## Window split

This offline tool lane continues independently. A separate online lane may consume admitted checkpoints and perform synchronization/integration testing. This checkpoint performs no online synchronization, production mutation, or production binding.
