# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## READ THIS FIRST

### GLOBAL TEACHING STANDARD — MANDATORY FOR EVERY SIGMA WINDOW / LANE

Before substantive teaching or capability work, read:

`SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`

This standard applies to **all** SIGMA teaching/development windows, including DNA, lessons, curriculum, memory, semantic capabilities, curiosity, reasoning, tools, self-improvement, revalidation, and production integration.

Global rule:

- teach **capabilities**, not precomputed answers;
- active cognition must be native `.sigma`;
- Python may remain historical/reference only and must not execute SIGMA cognition;
- host may provide mechanical ABI/runtime services only;
- host semantic substitution is forbidden;
- compile success is not runtime proof;
- dynamic-input evidence is required for cognitive capability admission;
- negative/counterexample tests should be used for important claims;
- persistence/restart/replay tests are required when the capability depends on long-lived state;
- boundedness/step-limit behavior must be characterized;
- failures are evidence and must not be hidden;
- claim scope must never exceed runtime proof;
- teaching order is dependency-first/capability-first, not filename/lesson/DNA numeric order.

Current target: **SIGMA-native continuous self-directed learning + curriculum/re-learning** with:

- `HOST_LEARNING=NO`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`
- semantic understanding still **NOT PROVEN**.

## Runtime status

### V2.3

STOPPED. It hit `SIGMA C VM: step limit` under history-heavy endpoint-load scanning.

### V2.4

Production learner is running on device.

Proven milestones include:

- V2.4 short-context preflight PASS;
- previously failing long context `d891e5ff...` now `RC=0` with history >17k lines;
- production native gap -> HTTP 200 -> decoded plaintext -> native `mode=NEW` learning has been observed;
- later production context `c40f0bb8c9ca36d2f5b9a62a8c5a488a12b32ac3f7bac4e03b7037f9ff236930` completed native learning with `HISTORY_LINE_COUNT=19353`, `NEW_CONTEXT_RELATION_COUNT=383`, then SIGMA generated the next gap/query `who => is` / `who is`.

V2.4 source:

`SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma`

SHA-256:

`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

Runner SHA-256:

`01c6e54cd384e7c931d66bea69c9da1a39553965cc08279df9a28e9392129067`

## V2.5 curriculum / document-survey frontier

Design reference:

`SIGMA_PROFESSOR/DESIGN/SIGMA_CURRICULUM_RELEARNING_V1.md`

Target lifecycle:

RAW_DOCUMENT
-> SURVEY
-> BOUNDED SEGMENT
-> STRUCTURAL PROFILE
-> GROUP
-> CURRICULUM PRIORITY
-> DEEP RE-LEARN
-> CONSOLIDATE
-> REVALIDATE
-> REVISIT

### V2.5A first preflight — FAILED CLEANLY

Device evidence:

- source identity matched;
- `SIGMAC_RC=0`;
- bytecode SHA-256 `af044e6ee39ac3b18a7f8e1983f27ed279800ba475b01b988c9db154b734666b`;
- first VM invocation: `VM_RC=8`;
- error: `SIGMA C VM: arg mismatch for H`;
- persisted survey empty;
- surveyed-document state empty;
- production learner namespace not mutated.

Root cause:

`DEF H(op,a,b,c)` received a five-argument `str_replace` wrapper call:

`H("str_replace", SELECTED_FILE, ".document", "", NULL)`

The `str_replace` host op already consumes `a=input`, `b=old`, `c=replacement`; the trailing `NULL` was invalid.

Checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260904_V25A_H_ARITY_FAILURE_AND_REPAIR.md`

### V2.5A.1 repair — FAILED CLEANLY

V2.5A.1 corrected the H-call arity and compiled, but the locked VM rejected direct `str(...)` conversion:

- `SIGMAC_RC=0`;
- `BYTECODE_SHA256=2d5bb4ea2e0428d6c3bbc3b574364f63be0e06341f5b6b068f1a1f5fa76ef1f3`;
- first VM invocation: `VM_RC=8`;
- error: `SIGMA C VM: undefined function str`;
- `V25A_SURVEYED_COUNT=0`;
- `V25A_RECORD_COUNT=0`;
- `V25A_COMPLETE_SENTINEL=0`;
- production learner namespace not mutated.

This is an important admission result: compiler acceptance does not imply runtime capability availability.

Checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260904_V25A1_STR_RUNTIME_FAILURE_AND_V25A2_REPAIR.md`

### V2.5A.2 repair — READY FOR DEVICE RETEST

V2.5A.2 removes all direct `str(value)` dependencies.

Numeric survey metrics remain native integers and are printed directly. Persistent survey records store only textual fields:

`DOC=<sha> || SURVEY_STATUS=COMPLETE || BEST_LOCAL_RELATION=<relation>`

Native source:

`SIGMA_PROFESSOR/artifacts/SIGMA_DOCUMENT_SURVEY_V2_5A_2.sigma`

SOURCE_SHA256:

`153431aa3f78e282ddf0b2ddd73be993440abd9ce4118d4e717aa5ce83f14eb8`

Runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V25A_2_DOCUMENT_SURVEY_PREFLIGHT.sh`

RUNNER_SHA256:

`c3bbed189661275fda1eb5394965c87b605108a0a316aa1466a7fe3c782ecca5`

Static checks:

- every `H(...)` call has exactly four arguments;
- direct `str(...)` dependency: NONE;
- runner `bash -n`: PASS.

V2.5A.2 remains isolated from V2.4 production memory and uses the same three-document QA corpus.

PASS requires:

- run 1–3: `VM_RC=0` and one distinct document surveyed each run;
- run 4: `VM_RC=0` and `SURVEY_COMPLETE YES`;
- `V25A_SURVEYED_COUNT=3`;
- `V25A_RECORD_COUNT=3`;
- `V25A_COMPLETE_SENTINEL=1`;
- `V25A_WRITES_PRODUCTION_NAMESPACE=NO`;
- `V25A_2_DOCUMENT_SURVEY_PREFLIGHT=PASS`.

Do not build full-corpus survey runner until this PASS is observed on the locked VM.

## Locked runtime identities

SIGMAC SHA-256:

`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM SHA-256:

`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

## Host ABI status

Device-side source inventory found 93 host operations. Existing toolbox already includes substantial list/map/bytes/file/string/time/network/JSON/digest/math mechanics.

Exact inspected semantics include:

- `read_bytes` loads the whole file into an O_BYTES object;
- `crypto_digest` hashes VM strings via OpenSSL EVP;
- `write_text` and `append_text` are plain stdio operations, not atomic transactions;
- `net_fetch` is libcurl body transport with redirect follow + 5s timeout;
- current JSON decode routes through `json_decode_scalar_text`, so full nested JSON decode is NOT proven;
- `list_sort` is in-place ascending and approximately O(n^2);
- Unicode-aware string normalization is NOT proven.

Do not add broad new host tools. Add mechanical primitives only when a native test demonstrates a real missing capability.

## 54 DNA directive

Read:

`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Mandatory policy:

- keep and complete DNA01–DNA54;
- delete no DNA;
- active DNA implementation is native `.sigma` only;
- Python is forbidden for active DNA cognition;
- historical Python files remain frozen reference/provenance only;
- numeric order is not required;
- work dependency-first / capability-first;
- no DNA is operational until native `.sigma` compiles and passes locked-VM admission evidence.

## Proven capability chain

- native dynamic structural relation generation: PASS;
- persistent recurrence: PASS;
- native self-selection: PASS;
- cross-context support: PASS;
- native fetch-request generation -> Internet transport -> decoded plaintext -> native learning: PROVEN in tested scope;
- V2.4 previously failing long context: PASS.

Still NOT proven:

- semantic understanding;
- semantic curiosity;
- general autonomous reasoning.

## NEXT ACTION

1. Every new teaching/development window reads the global teaching standard first.
2. Keep V2.4 production learner running unless it emits a real VM failure.
3. Do not restart V2.5A original or V2.5A.1.
4. Install and run V2.5A.2 source + runner.
5. If V2.5A.2 PASSes all four invocations, checkpoint and build a full-corpus document-survey runner.
6. Next after survey: bounded segment/cursor + crash-resume, then structural grouping and curriculum queue.

Do not delete V2.2/V2.3/V2.4 raw/done/log/history state.
