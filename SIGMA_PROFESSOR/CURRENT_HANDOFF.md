# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-04 (Asia/Ho_Chi_Minh)

## READ THIS FIRST

Current target: **SIGMA native continuous self-directed learning** with `HOST_LEARNING=NO` and `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`.

## Current runtime status

- V2.3: STOPPED after `SIGMA C VM: step limit` under history-heavy endpoint-load scanning.
- V2.4 preflight: PASS on short and the previously failing long context.
- V2.4 production: installed/running on device; first production native gap -> HTTP 200 -> decoded-context fetch leg observed.
- Full V2.4 stability checkpoint still requires multiple complete request -> fetch -> native `mode=NEW` learning cycles without VM failure.

## V2.4 proof snapshot

Short context `0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4`: `SHORT_VM_RC=0`.

Previously failing long context `d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de`:

- `LONG_D891_VM_RC=0`
- `INPUT_LINE_COUNT=9`
- `HISTORY_LINE_COUNT=17270`
- `NEW_CONTEXT_RELATION_COUNT=668`
- `SELECTED_PATTERN=is => a`
- `SELECTED_CONTEXT_SUPPORT=35`
- `LEARNING_GAP=Moon => is`
- `FETCH_REQUEST=Moon is`
- `FETCH_REQUEST_SUPPORT=2`

Admission result:

- `V24_1_STEP_LIMIT_PREFLIGHT=PASS`
- `SIGMA_C_VM_STEP_LIMIT_REPRODUCED=NO`
- `PRODUCTION_MEMORY_MUTATED=NO`

## V2.4 native policy

- endpoint `TOKEN_LOAD` removed;
- SIGMA computes recurrence support itself;
- only relations with `CONTEXT_SUPPORT > 1` may become fetch gaps;
- SIGMA chooses the lowest-support recurrent not-yet-fetched frontier;
- host does not generate candidates, score knowledge, choose gaps, or choose queries.

## Production artifacts

- `SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma`
  - SHA-256: `6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`
- `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh`
  - SHA-256: `01c6e54cd384e7c931d66bea69c9da1a39553965cc08279df9a28e9392129067`
- transport decoder SHA-256: `c8d10c640d32d23d3998590a291d187de0936368d0cd3559706ed6509fd31705`

## Locked compiler / VM

- SIGMAC SHA-256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA-256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- VM embedded string: `SIGMA Genesis-4 C VM`
- `VM_IS_GENESIS1=NOT_PROVEN`

## Proven capability chain

- DNA01 dynamic structural relations: PASS
- DNA02 persistent recurrence: PASS
- DNA03 native self-selection: PASS
- DNA04 cross-context support: PASS
- V2.2 native gap -> fetch request -> Internet transport -> decoded plaintext -> SIGMA learning: PROVEN end-to-end
- V2.4 short-context execution: PASS
- V2.4 previously failing long-context execution: PASS

Still NOT proven:

- semantic understanding
- semantic curiosity
- general autonomous reasoning

## 54 DNA ACTIVE DIRECTIVE — supersedes Python-active interpretation

Read:

`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Decision:

- `KEEP_DNA_01_TO_54=YES`
- `DELETE_ANY_DNA=NO`
- `COMPLETE_ALL_54_DNA=YES`
- `ACTIVE_DNA_IMPLEMENTATION_LANGUAGE=SIGMA_NATIVE_ONLY`
- `PYTHON_FOR_ACTIVE_DNA_IMPLEMENTATION=FORBIDDEN`
- `PYTHON_FOR_SIGMA_COGNITION=FORBIDDEN`
- `NUMERIC_ORDER_REQUIRED=NO`
- `DEPENDENCY_FIRST=YES`
- `CAPABILITY_FIRST=YES`

Existing historical `54_CORES/*.py` artifacts are not deleted; freeze them as provenance/reference only until contracts are migrated. Do not execute/import/extend them as active cognition and do not count their filenames as proof of capability.

Executable cognition must be native `.sigma`, compiled by the locked `sigmac`, run by the locked VM, and admitted by runtime evidence.

Recommended priority waves are defined in the directive. Key semantic-learning priority includes epistemic/memory substrate -> concept/representation -> curiosity/metacognitive curriculum -> robustness -> governed self-improvement. DNA-50 governance should precede admission of DNA-25 self-improvement affecting important cognitive machinery.

## Host ABI inventory milestone

Read:

`SIGMA_PROFESSOR/DESIGN/HOST_ABI_INVENTORY_20260904_V1.md`

Device-side source inventory of `~/SIGMA/sigma_genesis1/sigma_vm.c` found **93 host operations**.

Important existing source-level capabilities:

- list mechanics: get/set/push/pop/shift/unshift/reverse/slice/sort;
- map mechanics: new/set/get/has/delete/keys/values/items;
- byte buffers and typed byte encoding/decoding;
- file operations: `read_text`, `read_bytes`, `write_text`, `append_text`, `file_exists`, `listdir`, mkdir/rmdir;
- string search/slice/replace/split/join and ASCII-oriented case helpers;
- JSON load/dump/encode/decode;
- Base64;
- `crypto_digest`;
- `time_now`, `time_sleep`, `time_strftime`;
- random primitives;
- `net_fetch`, `net_ping`, `dns_lookup`;
- math primitives.

`set_*` is not currently needed: SIGMA can implement deterministic set membership with `map_set(key, TRUE)` + `map_has(key)`.

## Exact host-op semantics now inspected

### `read_bytes`

- opens the requested path in `rb` mode;
- reads the ENTIRE file in 4096-byte chunks into an `O_BYTES` object;
- no offset/count bounded file read is present in this op;
- read error returns NULL.

Implication: bounded learning can use byte slicing after whole-file load for moderate files, but genuinely large corpora may eventually justify a bounded range-read primitive.

### `crypto_digest`

- uses OpenSSL EVP digest selected by algorithm name;
- hashes `strlen(text)` bytes from a VM string;
- returns lowercase/implementation hex via `hex_encode` when successful;
- this is text/string-oriented, not an exact arbitrary byte-buffer digest primitive.

### `write_text` / `append_text`

- `write_text`: plain `fopen(path,"wb")` -> `fwrite` -> `fclose`;
- `append_text`: plain `fopen(path,"ab")` -> `fwrite` -> `fclose`;
- no temp-file + rename transaction and no fsync/durability protocol is visible.

Implication: crash-safe critical cognitive state may eventually require an atomic persistence primitive or a SIGMA-visible protocol built from additional mechanical support.

### `net_fetch`

- libcurl GET-like URL fetch to an in-memory string;
- follows redirects;
- `CURLOPT_NOPROXY="*"`;
- 5000 ms timeout;
- returns body string on libcurl success, NULL on curl failure;
- inspected op does not expose HTTP status/content-type/final URL metadata.

This is transport only. SIGMA must still choose the learning gap/query and interpret returned content.

### `json_decode` / `json_load`

- both call `json_decode_scalar_text(...)`;
- therefore full nested object/array decoding is NOT proven by source evidence;
- do not remove the current mechanical Wikimedia decoder until locked-binary tests prove a sufficient replacement.

### `list_sort`

- in-place ascending comparison;
- strings use `strcmp`;
- non-strings use numeric `as_double` comparison;
- implementation is nested-loop approximately O(n^2).

Do not use it as a large-memory knowledge-ranking engine.

### Unicode

- `str_len` uses `strlen`;
- case operations use C `toupper`/`tolower` on bytes/chars;
- Unicode-aware normalization/code-point behavior is NOT proven.

## Tool-team policy

Do NOT add broad new tools now. Existing toolbox is substantial.

Potential future mechanical additions are only evidence-driven:

1. bounded file range/line read, if whole-file loading becomes a demonstrated limitation;
2. atomic/crash-safe state replacement, if kill tests demonstrate state corruption risk;
3. exact byte-buffer digest, if binary identity is required;
4. richer transport metadata, if a native research protocol requires it;
5. full mechanical JSON object/array decode, if needed to retire the current decoder;
6. Unicode normalization primitive, if native text normalization requires it.

Never add host operations such as summarize/classify/concept formation/semantic score/knowledge-gap detection/research-goal selection.

## NEXT ACTION — immediate

1. Keep V2.3 and older continuous runners stopped.
2. Keep observing V2.4 until multiple request -> fetch -> native learn cycles complete without VM failure.
3. Do not add duplicate host tools.
4. Begin V2.5 native document survey / bounded cursor work after V2.4 stability checkpoint.
5. Coordinate the 54-DNA lane using the native-only dependency-first directive.

## NEXT DEVELOPMENT TARGET — curriculum + re-learning

Read:

`SIGMA_PROFESSOR/DESIGN/SIGMA_CURRICULUM_RELEARNING_V1.md`

Required direction:

RAW_DOCUMENT
-> SURVEY OLD MATERIAL
-> BOUNDED NATIVE SEGMENTATION
-> STRUCTURAL PROFILE
-> NATIVE GROUPING
-> CURRICULUM PRIORITY
-> DEEP RE-LEARN
-> CROSS-DOCUMENT CONSOLIDATION
-> REVALIDATION
-> REVISIT WHEN NEW EVIDENCE CHANGES PRIORITY

Key invariants:

- raw documents remain immutable;
- SIGMA decides what is worth deeper learning;
- SIGMA decides grouping/priority from native evidence;
- large documents become bounded learning units to avoid VM step-limit growth;
- recovery resumes the persistent curriculum queue instead of becoming idle;
- host may persist/hash/schedule exact work identities but must not summarize, score, classify topics, choose lessons, or select knowledge.

Planned learner sequence after V2.4 stability:

1. V2.5 DOCUMENT_SURVEY
2. V2.6 BOUNDED_SEGMENT_CURSOR
3. V2.7 STRUCTURAL_GROUPING
4. V2.8 CURRICULUM_QUEUE
5. V2.9 GROUP_CONSOLIDATION + REVALIDATION

Do not delete V2.2/V2.3 raw/done/log/history state.

## Checkpoint discipline

Whenever a meaningful milestone completes:

1. update this file;
2. create an immutable checkpoint under `SIGMA_PROFESSOR/CHECKPOINTS/` for major milestones/failures;
3. save materially changed source/runner artifacts under `SIGMA_PROFESSOR/artifacts/`.
