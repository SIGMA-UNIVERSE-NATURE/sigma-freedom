# SIGMA_PROFESSOR Checkpoint — V2.3 step-limit handoff

Date: 2026-09-04 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Primary goal

Build SIGMA so that **SIGMA itself** learns continuously from local/Internet material and resumes learning after interruption. Recovery is a supporting mechanism, not the end goal.

## Non-negotiable architecture boundary

- `HOST_LEARNING=NO`
- `HARDCODED_LESSON=NO`
- Host mechanics allowed: read/write/copy bytes, SHA-256, process scheduling, network transport, protocol-envelope decode, invoke SIGMAC/VM.
- Host semantics forbidden: lesson generation, candidate generation, support calculation, pattern selection, knowledge selection, learning-goal selection.
- Learning decisions must execute in `.sigma` through the locked SIGMA VM.

## Locked toolchain

### SIGMAC

- Path observed on device: `/data/data/com.termux/files/home/SIGMA/sigma_genesis1/native/sigmac`
- SHA-256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- Size observed: `24352`
- CLI: `sigmac input.sigma output.sigmab`

### VM

- File: `sigma-vm.v09_candidate`
- SHA-256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- Embedded identity string observed: `SIGMA Genesis-4 C VM`
- Runtime self-identification: `NOT_PROVEN_FROM_OUTPUT_SHOWN`
- `VM_IS_GENESIS1=NOT_PROVEN`

### Mechanical Wikimedia transport decoder

- SHA-256: `c8d10c640d32d23d3998590a291d187de0936368d0cd3559706ed6509fd31705`
- Function: JSON protocol decode only; emits `query.pages[].extract` plaintext in response order.
- No summarization/ranking/semantic filtering.

## Proven native learning milestones

### DNA01-C2 — dynamic structural relation generation

- Bytecode SHA-256: `25014e7d505a1a46484fe8225ca642bac1114bb1ae596df366dd6984b2f4ba4d`
- Result: same bytecode + different runtime input generated different relation sets.
- `SIGMA_WHILE_RUNTIME=PROVEN_IN_EXACT_TESTED_SCOPE`
- `SIGMA_DYNAMIC_RELATION_GENERATION=PROVEN_IN_EXACT_TESTED_SCOPE`
- `SIGMA_PERSISTENT_OUTPUT=PROVEN_IN_EXACT_TESTED_SCOPE`

### DNA02.2 — persistent recurrence

- Bytecode SHA-256: `8c0a9ce87f69d487c7b74d16e467b7db64bb1f03f8d7473d921e0b98daed4e0d`
- Example observed:
  - experience 1: `BETA => GAMMA STRENGTH 1`
  - experience 2: `BETA => GAMMA STRENGTH 2`
  - experience 3: `BETA => GAMMA STRENGTH 3`
- `PAST_EXPERIENCE_AFFECTS_CURRENT_COMPUTATION=YES`
- `RECURRENCE_STRENGTH_COMPUTED_BY_SIGMA=YES`

### DNA03 — native self-selection

- Bytecode SHA-256: `e3e068f19298f8bab442c4877330ae3831c475fca1276f7e81046a11709fd1df`
- Strongest relation was deliberately last in the candidate order and SIGMA still selected it.
- `CANDIDATES_GENERATED_BY_SIGMA=YES`
- `STRONGEST_PATTERN_SELECTED_BY_SIGMA=YES`
- `HOST_GENERATED_CANDIDATE=NO`
- `HOST_SELECTED_CANDIDATE=NO`

### DNA04 — cross-context support

- Bytecode SHA-256: `810d5e4a65aaa0f1c478a89c047bb3cc8134242ef19b7cb4975883cd3dde7111`
- Replaying the same context did not inflate support.
- Distinct contexts increased support.
- Example: `BETA => GAMMA` reached `CONTEXT_SUPPORT 3` across three contexts.
- `CROSS_CONTEXT_SUPPORT_COMPUTED_BY_SIGMA=YES`
- `CROSS_CONTEXT_SELECTION_BY_SIGMA=YES`

## Continuous-learning runtime history

### V1

End-to-end local path proved:

`local document -> SIGMA VM -> runtime relations -> self-selection -> persistent SIGMA memory -> done marker`

Seed context observed:

`7908b2b27c49e0e7cabc25b5bddfa8007394b23ad5032b4af4bb7cacfee04158`

V1 limitation: newline initially contaminated token boundaries; later native line-aware processing was introduced.

### V2.1

Autonomous structural fetch loop proved, but MediaWiki JSON envelope was learned as content. Memory considered contaminated evidence, not production-quality knowledge.

### V2.2

Mechanical decoder introduced. End-to-end cycle proved:

`SIGMA native gap -> SIGMA FETCH_REQUEST -> host transport -> mechanical protocol decode -> decoded context -> SIGMA native learning`

Observed host markers:

- `HOST_ROLE=QUERY_TRANSPORT_AND_PROTOCOL_DECODE_ONLY`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `FETCHED_DECODED_CONTEXT=<sha>`

Observed problem: structural gap policy drifted into weak queries (`Alpha`, `Sigma Tau`, `Delta Sigma`, etc.) and common relations such as `is => a` dominated support. HTTP 429 also observed.

### V2.3

Purpose: reduce topic drift without hardcoded stopwords/topics by making only recurrent relations eligible and using a native endpoint-load heuristic.

Device compile result:

- `BYTECODE_SHA256=5fecb1751039bdca087d5e1714068a07f14b5c78c0e629cb16eb67a42e7619b0`
- `SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_3=START`
- `HOST_LEARNING=NO`
- `SELF_DIRECTION_POLICY=NATIVE_RECURRING_ASSOCIATION_WITH_LOW_ENDPOINT_LOAD`
- `ONE_OFF_RELATION_FETCH=NO`

## CURRENT FAILURE — STOP HERE FIRST

V2.3 runtime repeatedly failed with VM `rc=9`.

Latest new-context failure:

- Context: `d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de`
- Mode: `NEW`
- `rc=9`

Reconsider failure also observed:

- Context: `0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4`
- Mode: `RECONSIDER`
- `rc=9`

State at failure:

- `RAW=39`
- `DONE=38`

Critical log line:

`SIGMA C VM: step limit`

The log emitted many valid candidates first, e.g. `CANDIDATE ... CONTEXT_SUPPORT ... TOKEN_LOAD ...`, then hit the VM step limit.

### Current diagnosis

`STEP_LIMIT` is proven. Exact algorithmic cause is not fully proven, but the likely cause is V2.3's added nested full-history endpoint-load scan: for each current relation, it scans all history and repeatedly splits historical relation records. This increases VM step complexity significantly compared with V2.2.

Do **not** move endpoint-load calculation to the host as a shortcut.

## Required next action

Keep V2.3 stopped until fixed. Do not delete:

- `~/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/raw/`
- `~/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/done/`
- V2.2/V2.3 logs
- `SIGMA_CL22_*` memory files

Preferred next design direction:

1. Remove the expensive full-history endpoint-load scan from each candidate.
2. Preserve native self-direction.
3. Use a cheaper native recurring-association policy first (for example: only relations with `SUPPORT > 1`, prefer low recurrent support / deterministic tie-breaking), or introduce incremental native statistics if the VM primitives support it.
4. Host must remain scheduler/transport only.
5. Test short context and previously failing long context before restarting the infinite loop.
6. Only after runtime pass, re-enable rate-limited Internet fetch.

## Claims that remain NOT PROVEN

- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `SEMANTIC_CURIOSITY=NOT_PROVEN`
- `GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

## Handoff rule

Any next assistant/window should continue from this checkpoint and must not restart from old R2/R3 probing unless new evidence specifically requires it.
