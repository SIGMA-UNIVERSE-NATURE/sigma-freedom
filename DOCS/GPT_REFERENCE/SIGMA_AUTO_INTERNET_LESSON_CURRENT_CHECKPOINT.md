# SIGMA — AUTO INTERNET LESSON CURRENT CHECKPOINT

STATUS_DATE=2026-09-01
BRANCH=SIGMA_LIFE
CANONICAL_FOR_NEXT_WINDOWS=YES

## 1. CURRENT GOAL

Mục tiêu duy nhất hiện tại:

```text
ONE START
→ RAW_TOPIC
→ existing SIGMA query engine
→ live Internet search
→ RSS result parsing
→ discovered URLs
→ Network Safety Membrane
→ automatic source fetch
→ existing SIGMA lesson reader
→ lesson experience saved
→ provenance
→ independent verification
→ STOP
```

Hard requirement:

```text
HUMAN_INTERVENTION_BETWEEN_STAGES=0
```

Chưa làm semantic relevance, understanding, intelligence testing, relation reasoning, empathy, dynamic AST, hoặc self-directed curriculum ở frontier này.

---

## 2. SIGMA LANGUAGE PRESERVE LOCK

Không viết lại các SIGMA engine đã machine-run thành công chỉ để sửa host/harness bug.

### Query engine

Artifact name:

`query_generator.sigmab`

SHA256:

`db199f572a9415dc812fb3936387541a3b1e648f383d5e1da6487f11e97c4b6a`

Machine evidence gần nhất:

```text
SIGMA_QUERY_RC=0
SIGMA_QUERY_CANDIDATES=9
QUERY_READBACK_CMP_RC=0
```

Raw topic:

`Human-to-Human Communication`

Observed query artifact:

```text
Human to Human Communication
Human to Human
to Human Communication
Human to
to Human
Human Communication
Human
to
Communication
```

Rule:

`QUERY_ENGINE_REWRITE=FORBIDDEN_UNLESS_MACHINE_EVIDENCE_IDENTIFIES_ENGINE_FAILURE`

### Lesson reader

Artifact name:

`lesson_reader.sigmab`

SHA256:

`ba2faf7bddb81789b3fbccff96bdf8f3c2021d0db252d7e8ef38dc92b182994c`

Rule:

`LESSON_READER_REWRITE=FORBIDDEN_UNLESS_MACHINE_EVIDENCE_IDENTIFIES_ENGINE_FAILURE`

---

## 3. RUNTIME IDENTITIES

Compiler SHA256:

`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM SHA256:

`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

HTTP bridge SHA256:

`d7dcc121dbd4611ea5f2cf677f5ec08567b8a03ba11ae57ba4c1624b3f638d1e`

If any required identity changes:

`STOP_RUNTIME_IDENTITY_CHANGED`

Do not silently rebuild/replace and continue as if the runtime were identical.

---

## 4. PROVEN TESTED-SCOPE CAPABILITIES ALREADY COMPLETED

Do not rerun these as the main direction unless required by a new root cause.

### Query generation

`SIGMA_QUERY_GENERATION=PASS_TESTED_SCOPE`

### Open Internet source discovery

Previous staged Script 2 evidence:

```text
UNIQUE_DISCOVERED_URLS=49
UNIQUE_DISCOVERED_DOMAINS=32
```

Claim:

`OPEN_INTERNET_SOURCE_DISCOVERY=PASS_TESTED_SCOPE`

This did not prove relevance/trust/truth.

### Network Safety Membrane

Tested-scope evidence exists for:

- HTTPS technical boundary
- public-network/TLS bridge behavior
- no JS/content execution
- no binary/file/code execution
- no automatic redirect following
- content-type quarantine
- response/resource guard
- text-byte surface analysis

Observed aggregate reservation evidence:

```text
REMAINING_BYTES=655677
REQUIRED_RESERVATION=1048576
OBSERVATION=REQUEST_NOT_ISSUED_RESOURCE_RESERVATION
```

Canonical meaning:

```text
SAFE_TO_FETCH ≠ TRUSTED
SAFE_TO_FETCH ≠ RELEVANT
SAFE_TO_FETCH ≠ TRUE
```

### Human-language Web acquisition

Script 4 machine evidence:

```text
SOURCES=3
EXTRACTED_PARAGRAPHS=49
EXTRACTED_HUMAN_TEXT_BYTES=14132
BYTE_EXACT_READBACKS=3/3
```

Claim:

`SIGMA_CAN_ACQUIRE_WEB_HUMAN_TEXT=PASS_TESTED_SCOPE`

Do not claim semantic understanding.

### Open relation material foundation

R2 machine evidence:

```text
SIGMA_RUNS=3
SIGMA_RC0=3
BYTE_EXACT_TOPIC_READBACKS=3
BYTE_EXACT_EXPERIENCE_READBACKS=3
```

This work is preserved but HOLD; it is not the current frontier.

---

## 5. LATEST ONE-START AUTO PIPELINE RUN

Run directory:

`/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_exec/HH_AUTO_INTERNET_LESSONS/runs/20260901T120406Z_6891_26254`

Observed machine facts:

```text
REPORT=HH_AUTO_INTERNET_LESSON_ACQUISITION_V1
ONE_START_PIPELINE=YES
HUMAN_INTERVENTION_BETWEEN_STAGES=0
SIGMA_QUERY_RC=0
SIGMA_QUERY_CANDIDATES=9
QUERY_READBACK_CMP_RC=0
SEARCH_REQUESTS=3
```

All three live RSS searches returned:

```text
BRIDGE_RC=0
BRIDGE_RESULT=TRANSPORT_COMPLETE
HTTP_CODE=200
```

RSS bodies visibly contained real `<item><link>` results including public Web URLs.

Therefore:

```text
LIVE_SEARCH_TRANSPORT=PASS_TESTED_SCOPE
RSS_RESULTS_PRESENT=YES
```

---

## 6. CANONICAL CURRENT FAILURE

Do NOT classify the latest run as Sigma failure or no-results failure.

Canonical classification:

```text
AUTO_INTERNET_LESSON_ACQUISITION_V1=FAIL_HARNESS_DISCOVERY_DRIVER
NOT_SIGMA_FAILURE=YES
NOT_NO_LESSON_FOUND=YES
```

Pipeline reached:

```text
ONE START
→ RAW TOPIC
→ SIGMA QUERY                 PASS
→ LIVE INTERNET SEARCH        PASS
→ RSS RECEIVED                PASS
→ RSS URL EXTRACTION          FAIL_HARNESS
→ SOURCE FETCH                NOT REACHED
→ LESSON EXTRACTION           NOT REACHED
→ LESSON SAVE                 NOT REACHED
```

### Root cause 1 — Bash arithmetic

The driver used command substitution where arithmetic expansion was required for session counters, producing messages such as:

```text
SESSION_MAX_BYTES: command not found
SESSION_TRANSFER_BYTES: command not found
bash: [: : integer expected
```

Required repair:

Audit all arithmetic and use `$(( ... ))` correctly.

### Root cause 2 — RSS parser invocation

The driver invoked Python in a way that made `body.raw` execute as Python source instead of being passed as RSS/XML data.

Observed failure:

```text
SyntaxError: invalid character '©' (U+00A9)
```

The RSS itself was present and valid enough to visibly contain result items.

Required repair:

Python code must be provided separately; `body.raw` must only be a data path argument.

Parser role must remain mechanical:

```text
RSS/XML DATA
→ item/link extraction
→ URL list
```

No semantic ranking or source-quality decision in host code.

---

## 7. CURRENT FRONTIER

```text
CURRENT_FRONTIER=AUTO_RSS_URL_EXTRACTION_TO_AUTO_LESSON_FETCH
```

Do not switch to another development frontier until the one-start acquisition chain is machine-proven or a new precise blocking root cause is established.

---

## 8. NEXT IMPLEMENTATION TASK

Build and QA these components while preserving the existing SIGMA bytecodes:

```text
00_VERIFY_AUTO_LESSON_RUNTIME.sh
10_RSS_ITEM_LINK_EXTRACT.py
20_AUTO_INTERNET_LESSON_V1_R1.sh
30_VERIFY_AUTO_INTERNET_LESSON_V1_R1.sh
99_RUN_AUTO_INTERNET_LESSON_V1_R1.sh
```

Responsibilities:

### 00_VERIFY

Verify exact identities only. No broad local scan. No engine rewrite.

### 10_RSS_ITEM_LINK_EXTRACT.py

Mechanical RSS parser only:

- parse RSS as data
- extract `<link>` inside `<item>` only
- preserve order
- exact dedup
- no semantic logic
- distinguish parse failure from successful zero results

### 20_AUTO_INTERNET_LESSON_V1_R1.sh

One continuous driver:

```text
raw topic
→ existing Sigma query bytecode
→ live RSS search
→ mechanical RSS parser
→ discovered URL ledger
→ technical Network Safety Membrane
→ automatic source fetch
→ existing Sigma lesson-reader bytecode
→ persistent lesson artifact
→ provenance
```

No human intervention between stages.

V1 source stop policy may be purely mechanical:

`FIRST_TECHNICALLY_ELIGIBLE_SOURCE_THAT_PRODUCES_NONEMPTY_LESSON`

This must NOT be described as best/relevant/trusted source selection.

### 30_VERIFY

Independent artifact verification; do not trust driver counters blindly.

Recompute hashes and verify selected URL/query provenance, lesson hash/readback, raw-body cleanup, and resource totals.

### 99_RUN

The only command the user should need to execute. It must invoke verify → driver → independent verifier without user intervention in between.

---

## 9. ACCEPTANCE GATE

Only close the current objective when machine evidence establishes all material invariants, including:

```text
ONE_START_PIPELINE=YES
HUMAN_INTERVENTION_BETWEEN_STAGES=0
SIGMA_QUERY_RC=0
SIGMA_QUERY_CANDIDATES>0
QUERY_READBACK_CMP_RC=0
SEARCH_REQUESTS>0
RSS_PARSER_RC=0
DISCOVERED_URLS>0
SOURCE_REQUESTS>0
RESOURCE_BUDGET_OVERRUN=0
BRIDGE_CEILING_VIOLATION=0
LESSON_ACQUIRED=1
SIGMA_READER_RC=0
LESSON_PARAGRAPHS>0
LESSON_BYTES>0
LESSON_READBACK_CMP_RC=0
LESSON_SHA256=<real hash>
PROVENANCE_SHA256=<real hash>
PERSISTENT_LESSON_PATH=<real path>
RAW_WEB_BODIES_RETAINED=0
WEB_CONTENT_EXECUTED=0
INDEPENDENT_VERIFY_RC=0
```

Only then claim:

`ONE_START_AUTOMATIC_INTERNET_LESSON_ACQUISITION=PASS_TESTED_SCOPE`

---

## 10. CLAIM BOUNDARIES EVEN AFTER PASS

Keep all of these unpromoted:

```text
FULL_AUTONOMOUS_LEARNING=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
TOPIC_RELEVANCE=NOT_ASSESSED
SOURCE_TRUST=NOT_ASSESSED
LESSON_TRUTH=NOT_ASSESSED
SELF_DIRECTED_CURRICULUM=NOT_PROVEN
```

---

## 11. HARD GOVERNANCE LOCKS

```text
SIGMA_LANGUAGE_FIRST=ON
ZERO_ANSWER_INJECTION=ON
HOST_ROLE=MECHANICAL_ONLY
QUERY_ENGINE_REWRITE=FORBIDDEN
LESSON_READER_REWRITE=FORBIDDEN
LOCAL_SCAN=FORBIDDEN_AS_MAIN_DIRECTION
LOCAL_KNOWLEDGE_READ=FORBIDDEN
OLD_CAP_RECOVERY=FORBIDDEN_AS_MAIN_DIRECTION
```

Host/Bash/Python may do only mechanical work such as transport, RSS/XML parsing, resource accounting, file lifecycle, hashing, provenance, and orchestration.

Host must not:

- write query semantics for Sigma
- add semantic keywords
- rank relevance
- select trusted domains
- decide truth
- decide lesson quality
- create Sigma reasoning/conclusions

---

## 12. FAILURE PROTOCOL

If the next implementation fails:

1. Identify exact stage: runtime / query / search / RSS parse / membrane / fetch / reader / save / provenance / verification.
2. Classify whether failure is Sigma, runtime, Internet, or host/harness.
3. Repair only the actual failing layer.
4. Do not rewrite working SIGMA engines for a host bug.
5. Do not rerun completed stages unnecessarily when safe preserved artifacts can be reused.
6. Do not elevate claims.
7. If root cause is uncertain, STOP rather than guess.

---

## 13. NEXT COMMAND / NEXT WINDOW ENTRY POINT

```text
NEXT_COMMAND=BUILD_AND_QA_ONE_START_AUTO_INTERNET_LESSON_V1_R1
```

For future GPT windows:

**Read this file first and continue from CURRENT_FRONTIER. Do not ask the user to paste the full historical handoff unless this checkpoint is demonstrably insufficient.**
