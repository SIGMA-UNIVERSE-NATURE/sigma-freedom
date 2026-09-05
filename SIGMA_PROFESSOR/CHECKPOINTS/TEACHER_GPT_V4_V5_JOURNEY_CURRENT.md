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

## Governing execution boundary

```text
ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
HOST_MAY_CHOOSE_EVENT_OR_STAGE=NO
HOST_POST_VM_TEST_ORACLE_ONLY=YES
PYTHON_USED_FOR_SIGMA_COGNITION=NO
```

Locked runtime:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Production remains unchanged:

```text
PRODUCTION_V2_4_KEEP_RUNNING=YES
UPGRADE_V2_4_IN_PLACE=NO
PRODUCTION_BINDING=NO_FOR_THIS_V4_V5_JOURNEY
```

## Current frontier

```text
CURRENT_LEVEL=LEVEL_2_V5
CURRENT_STAGE=V5-K1
CURRENT_CAPABILITY=EXTERNAL_ACQUISITION_REQUEST_RESPONSE_PROTOCOL
V5K1_V1_ADMISSION=FAIL_AT_D02_HARNESS_PAYLOAD_TRUNCATION
V5K1_FIX1_SOURCE_READY=YES
V5K1_FIX1_RUNTIME_ADMISSION=NOT_RUN
V5K2_WIKIPEDIA_ADAPTER_UNLOCKED=NO
```

Latest immutable failure checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V5K1_D02_PAYLOAD_TRUNCATION_HARNESS_FAILURE.md`

Latest Fix1 source-ready checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V5K1_FIX1_PAYLOAD_PRESERVATION_SOURCE_READY.md`

## V5-K1 Fix1 artifact identities

```text
V5K1_FIX1_BUNDLE_NAME=SIGMA_V5K1_NATIVE_ADMISSION_V1_FIX1_EXTERNAL_ACQUISITION_PROTOCOL_BUNDLE.zip
V5K1_FIX1_BUNDLE_SHA256=21b6203b63ba554b22ba53e27264ed4698b4d48faff5d1a8dae7e430592de77d
V5K1_NATIVE_SOURCE_SHA256=29670c3eca4bcd02e875d2178407259af9e76ebbcbbd6e2ee7a31f979da26537
V5K1_NATIVE_SOURCE_CHANGED_FROM_V1=NO
V5K1_FIX1_RUNNER_SHA256=8645a8c46ad09599fa29e5d0e30064d3d460d0799fe066773fcbb58a6956cc28
V5K1_FIX1_BYTECODE_SHA256=UNKNOWN_NOT_RUN
PLANNED_VM_INVOCATIONS=50
```

## Latest V5-K1 machine evidence

Observed V1 failure:

```text
D02_VERIFY_A
VM_RC=0
PHASE=VERIFY
REQUEST_ID=req-a
INPUT_VALID=1
SOURCE_FAMILY_VALID=1
LEDGER_VALID=1
EVENT_MATCH=1
SUCCESS_RESPONSE_MATCH=1
PAYLOAD_PRESENT=0
VERIFY_SUCCESS_ELIGIBLE=0
WRITE_ATTEMPTED=0
ACQUISITION_RETAINED=0
STATE_MUTATED=0
V5K1_STATUS=REFUSE_PAYLOAD_MISSING
POST_VM_ALIGNMENT=FAIL
```

Diagnosis:

```text
PREPARE
-> runner clears payload/slota.txt
-> mechanical transport writes exact fixture bytes
-> VERIFY calls old set_req()
-> old runner truncates payload/slota.txt again
-> native SIGMA sees PAYLOAD_PRESENT=0
-> native SIGMA correctly refuses
```

This is a harness payload-lifecycle failure. It is not a native false-positive; native SIGMA failed closed and did not mutate the acquisition ledger.

Fix1 mechanical rule:

```text
PREPARE -> clear valid destination payload slot
VERIFY  -> preserve exact transport-written payload bytes
```

No native request/response/provenance/truth policy changed.

## V5-K1 exact intended claim scope

If Fix1 eventually passes the unchanged admission gate, V5-K1 may prove only:

- native request protocol;
- exact response identity binding;
- sandbox mechanical exact resource lookup transport;
- transport-not-found visibility;
- malformed-response refusal;
- missing-payload refusal;
- request-ID conflict refusal;
- bounded acquisition-ledger idempotency;
- source-family/resource-ID/request-ID provenance binding.

Keep false/unexecuted until separately proven:

```text
LIVE_INTERNET_RUNTIME=NOT_EXECUTED
WIKIPEDIA_ADAPTER=NOT_EXECUTED
ARXIV_ADAPTER=NOT_EXECUTED
PUBMED_ADAPTER=NOT_EXECUTED
GUTENBERG_ADAPTER=NOT_EXECUTED
RESEARCH_GOAL_SELECTION=NOT_EXECUTED
CONTENT_TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

## Level 1 V4 result summary

Level 1 remains complete in the exact admitted scopes:

```text
V4-PK1_PERSISTENT_SEMANTIC_HYPERGRAPH=PASS_IN_EXACT_TESTED_SCOPE
V4-PK2_NATIVE_WEIGHT_EVIDENCE=PASS_IN_EXACT_TESTED_SCOPE
V4-PK3_EVIDENCE_QUALIFIED_MULTI_HOP=PASS_IN_EXACT_TESTED_SCOPE
V4-PK4_FORMAL_TRANSITIVE_INFERENCE=PASS_IN_EXACT_TESTED_SCOPE
V4-PK4_INFERENCE_LIFECYCLE=PASS_IN_EXACT_TESTED_SCOPE
V4-PK5_COGNITIVE_VM_BRIDGE_COPY_EXACT=PASS_IN_EXACT_TESTED_SCOPE
V4-PK6_VERIFIED_EVOLUTION_SANDBOX_PROFILE=PASS_IN_EXACT_TESTED_SCOPE
LEVEL1_V4_PERSISTENT_KNOWLEDGE_CHAIN_COMPLETE_IN_DECLARED_TESTED_SCOPES=YES
```

Latest immutable Level-1 completion checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V4PK6_FIX1_VERIFIED_EVOLUTION_PASS_LEVEL1_V4_CHAIN_COMPLETE.md`

Machine-executed sample:

`SIGMA_PROFESSOR/artifacts/SAMPLES/V4PK6_VERIFIED_EVOLUTION_MACHINE_PASS_SAMPLE_V1.txt`

The sample explicitly states that it is a deterministic admitted-runner case definition backed by the final 50/50 machine PASS summary, not fabricated full stdout.

## Important failure history to preserve

1. V4-PK4 D16: harness capacity fixture had wrong field count; native SIGMA correctly rejected malformed state; runner-only Fix1 then passed.
2. V4-PK4 Completion D09: invalid input still exposed `SUPPORTED_INFERENCE`; native Fix1 forced `UNRESOLVED`; full rerun passed.
3. V4-PK6 D01: absent optional read targets caused locked-VM `string required`; runner-only explicit empty-file initialization; full rerun passed.
4. V5-K1 D02: old runner truncated transport payload on VERIFY; native SIGMA correctly refused missing payload; Fix1 is runner-only and not yet runtime-tested.

Do not erase failures after repair; they are evidence and prevent regressions.

## Immediate next action

Run the exact V5-K1 Fix1 bundle from a clean directory on locked Termux.

Expected bundle:

```text
SIGMA_V5K1_NATIVE_ADMISSION_V1_FIX1_EXTERNAL_ACQUISITION_PROTOCOL_BUNDLE.zip
SHA256=21b6203b63ba554b22ba53e27264ed4698b4d48faff5d1a8dae7e430592de77d
```

Expected runner:

```text
run_SIGMA_V5K1_NATIVE_ADMISSION_V1_FIX1.sh
SHA256=8645a8c46ad09599fa29e5d0e30064d3d460d0799fe066773fcbb58a6956cc28
```

The same 50-invocation admission gate must be rerun. At D02, the repaired harness must allow native SIGMA to observe the exact transport payload rather than an empty file.

Expected D02 success shape:

```text
EVENT_MATCH=1
SUCCESS_RESPONSE_MATCH=1
PAYLOAD_PRESENT=1
VERIFY_SUCCESS_ELIGIBLE=1
WRITE_ATTEMPTED=1
ACQUISITION_RETAINED=1
STATE_MUTATED=1
V5K1_STATUS=ACQUISITION_VERIFIED_COMMITTED
POST_VM_ALIGNMENT=PASS
```

If Fix1 PASS:

1. create immutable V5-K1 Fix1 PASS checkpoint;
2. update this living handoff immediately;
3. set `V5K2_WIKIPEDIA_ADAPTER_UNLOCKED=YES`;
4. build V5-K2 using the admitted V5-K1 protocol;
5. host stays exact HTTP/byte transport + exact decode only;
6. retain Wikipedia source/page/revision provenance before evidence use;
7. retrieval success must not become truth or knowledge promotion.

If Fix1 FAIL:

1. preserve exact first failure;
2. create immutable failure checkpoint;
3. update this living handoff immediately;
4. make the smallest repair;
5. rerun the unchanged gate;
6. never weaken the oracle.

## Direction after V5-K1

```text
V5-K1 External acquisition request/response protocol
-> V5-K2 Wikipedia adapter
-> V5-K3 arXiv adapter
-> V5-K4 PubMed adapter
-> V5-K5 Project Gutenberg adapter
-> V5-K6 Provenance normalization
-> V5-K7 Evidence Graph integration
```

## Next-window instruction

```text
DO_NOT_REASK_USER_FOR_V4_V5_HISTORY=YES_IF_REPO_EVIDENCE_AVAILABLE
READ_LIVING_HANDOFF_AND_CONTINUE_FROM_NEXT_ACTION=YES
CLAIM_LE_MACHINE_EVIDENCE=YES
```

A new window should continue with V5-K1 Fix1 runtime admission unless a newer immutable checkpoint/living update supersedes this frontier.
