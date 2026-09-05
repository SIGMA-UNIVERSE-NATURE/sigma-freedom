# TEACHER_GPT V4 -> V5 JOURNEY — LIVING HANDOFF

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: LIVING COORDINATION CHECKPOINT

## Mandatory continuation reads

Before continuing this lane, read:

1. `/AGENTS.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
3. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
5. `SIGMA_PROFESSOR/DIRECTIVES/TEACHER_GPT_GITHUB_PROGRESS_HANDOFF_POLICY_V1.md`
6. this living handoff
7. the latest immutable checkpoint named below

Do not ask the user to restate the V4/V5 journey when these files provide the needed context.

## Progress-update policy

```text
GITHUB_PROGRESS_UPDATE_REQUIRED=YES
UPDATE_AFTER_EACH_MEANINGFUL_COMPLETION=PREFERRED
MAX_COMPLETIONS_WITHOUT_GITHUB_STATUS_UPDATE=2
UPDATE_AFTER_ANY_MEANINGFUL_FAILURE=YES
UPDATE_BEFORE_CONTEXT_WINDOW_HANDOFF=YES
```

## Locked execution boundary

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
HOST_MAY_CHOOSE_EVENT_OR_STAGE=NO
HOST_POST_VM_TEST_ORACLE_ONLY=YES
PYTHON_USED_FOR_SIGMA_COGNITION=NO
PRODUCTION_V2_4_KEEP_RUNNING=YES
UPGRADE_V2_4_IN_PLACE=NO
PRODUCTION_BINDING=NO_FOR_THIS_V4_V5_JOURNEY
```

## Current frontier

```text
CURRENT_LEVEL=LEVEL_2_V5
CURRENT_STAGE=V5-K2
CURRENT_CAPABILITY=WIKIPEDIA_ADAPTER
V5K1_ADMISSION=PASS_IN_EXACT_TESTED_SCOPE
V5K2_WIKIPEDIA_ADAPTER_UNLOCKED=YES
V5K2_SOURCE_READY=NO_IN_PROGRESS
V5K2_RUNTIME_ADMISSION=NOT_RUN
```

Latest immutable checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V5K1_FIX1_EXTERNAL_ACQUISITION_PROTOCOL_PASS.md`

Latest machine-executed sample:

`SIGMA_PROFESSOR/artifacts/SAMPLES/V5K1_FIX1_EXTERNAL_ACQUISITION_MACHINE_PASS_SAMPLE_V1.txt`

## V5-K1 — admitted PASS

```text
SOURCE_SHA256=29670c3eca4bcd02e875d2178407259af9e76ebbcbbd6e2ee7a31f979da26537
FIX1_RUNNER_SHA256=8645a8c46ad09599fa29e5d0e30064d3d460d0799fe066773fcbb58a6956cc28
FIX1_BUNDLE_SHA256=21b6203b63ba554b22ba53e27264ed4698b4d48faff5d1a8dae7e430592de77d
BYTECODE_SHA256=UNKNOWN_NOT_IN_SUPPLIED_FINAL_SUMMARY
TOTAL_VM_INVOCATIONS=50
DIRECTED_VM_INVOCATIONS=16
RANDOMIZED_VM_INVOCATIONS=32
REPLAY_VM_INVOCATIONS=2
POST_VM_ALIGNMENT_PASS_COUNT=50
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
FINAL_ACQUISITION_LEDGER_SHA256=9d403cb79e9e9ea820ee8520576296086f907968bc8ade516b510c67dfa3d220
FINAL_ACQUISITION_RECORD_COUNT=18
HOST_TRANSPORT_DISPATCH_COUNT=19
HOST_TRANSPORT_NOT_FOUND_COUNT=1
HOST_NO_EVENT_COUNT=3
HOST_TRANSPORT_ERROR_COUNT=0
RESULT=PASS_IN_EXACT_TESTED_SCOPE
```

Admitted V5-K1 scope:

- native request emission;
- exact response identity binding;
- mechanical exact lookup transport in sandbox fixture scope;
- transport-not-found visibility;
- malformed-response refusal;
- payload-missing refusal;
- request-ID conflict refusal;
- bounded acquisition ledger idempotency;
- source-family/resource-ID/request-ID provenance binding;
- identical input/prestate decision and event-byte replay in tested scope.

## V5-K1 failure + repair history

V1 failed at D02 because the runner truncated the payload slot again before VERIFY:

```text
SUCCESS_RESPONSE_MATCH=1
PAYLOAD_PRESENT=0
V5K1_STATUS=REFUSE_PAYLOAD_MISSING
POST_VM_ALIGNMENT=FAIL
```

Native SIGMA failed closed correctly. Fix1 changed only runner payload lifecycle:

```text
PREPARE -> clear destination payload slot
TRANSPORT -> write exact payload bytes
VERIFY -> preserve transport payload bytes
```

Native source remained unchanged. Full Fix1 rerun passed 50/50.

## Level 1 V4 status

```text
LEVEL1_V4_PERSISTENT_KNOWLEDGE_CHAIN_COMPLETE_IN_DECLARED_TESTED_SCOPES=YES
V4-PK1_PERSISTENT_HYPERGRAPH=PASS_IN_EXACT_TESTED_SCOPE
V4-PK2_WEIGHT_EVIDENCE=PASS_IN_EXACT_TESTED_SCOPE
V4-PK3_MULTI_HOP_STRUCTURAL_REASONING=PASS_IN_EXACT_TESTED_SCOPE
V4-PK4_CONTROLLED_INFERENCE=PASS_IN_EXACT_TESTED_SCOPE
V4-PK5_COGNITIVE_VM_BRIDGE=PASS_IN_EXACT_TESTED_SCOPE
V4-PK6_VERIFIED_EVOLUTION=PASS_IN_EXACT_TESTED_SCOPE
```

Important V4 claim limits remain:

```text
SEMANTIC_UNDERSTANDING=NOT_PROVEN
SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
GENERAL_SELF_IMPROVEMENT=NOT_PROVEN
GENERAL_WORLD_ACTION=NOT_PROVEN
```

## V5-K2 design contract

Goal: add the smallest Wikipedia-specific adapter on top of admitted V5-K1.

Host may only perform exact HTTP/byte transport and exact protocol decoding required by the adapter. Host must not choose article relevance, truth, knowledge promotion, research goals, or semantic interpretation.

V5-K2 must preserve at minimum:

```text
SOURCE_FAMILY=WIKIPEDIA
LANGUAGE_EDITION
REQUEST_ID
RESOURCE_OR_PAGE_IDENTITY
REVISION_OR_RESPONSE_PROVENANCE_WHEN_AVAILABLE
TRANSPORT_STATUS
RAW_OR_EXACT_DECODED_PAYLOAD_IDENTITY
```

Retrieval success must not imply:

```text
CONTENT_TRUTH_DECISION
KNOWLEDGE_PROMOTION
SEMANTIC_UNDERSTANDING
```

Initial V5-K2 scope should be bounded, source-specific, live-network admission with positive, not-found, malformed-response/fault, replay/provenance and host-substitution tests.

## Immediate next action

1. Confirm current official Wikimedia/MediaWiki API transport shape from authoritative documentation.
2. Build native V5-K2 source and deterministic admission harness on top of V5-K1 boundaries.
3. Keep source-specific query/resource input dynamic.
4. Compile with locked SIGMAC before dynamic test inputs where practical.
5. Run locked-VM live-network admission on Termux.
6. Preserve first failure or final summary exactly.
7. On PASS, immediately create immutable V5-K2 checkpoint, update this living handoff, and unlock V5-K3 arXiv only then.

## Direction after V5-K2

```text
V5-K2 Wikipedia adapter
-> V5-K3 arXiv adapter
-> V5-K4 PubMed adapter
-> V5-K5 Project Gutenberg adapter
-> V5-K6 Provenance normalization
-> V5-K7 Evidence Graph integration
```

## Current non-claims

```text
LIVE_WIKIPEDIA_RUNTIME=NOT_YET_EXECUTED
ARXIV_ADAPTER=NOT_EXECUTED
PUBMED_ADAPTER=NOT_EXECUTED
GUTENBERG_ADAPTER=NOT_EXECUTED
RESEARCH_GOAL_SELECTION=NOT_EXECUTED
CONTENT_TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

## Next-window instruction

```text
DO_NOT_REASK_USER_FOR_V4_V5_HISTORY=YES_IF_REPO_EVIDENCE_AVAILABLE
READ_LIVING_HANDOFF_AND_CONTINUE_FROM_NEXT_ACTION=YES
CLAIM_LE_MACHINE_EVIDENCE=YES
```
