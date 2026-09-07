# VNM-06 — Native Span-Context Observation Derivation — ADMISSION PASS

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: `ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE`

## Governance

This admission is governed by the repository-wide native execution/admission stop-gate, exclusive self-learning/anti-hardcode lock, native artifact build/admission method, current handoff, language lane, VNM course directive, VNM living handoff, VNM-05 admission checkpoint, and the VNM-06 source-ready checkpoint.

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
ACTIVE_PYTHON_COGNITION=FORBIDDEN
HOST_SPAN_CANDIDATE_GENERATION=NO
HOST_SPAN_MATCHING=NO
HOST_SPAN_CONTEXT_EXTRACTION=NO
HOST_BOUNDARY_INFERENCE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED_DURING_PREFLIGHT=NO
```

Locked runtime:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Frozen native artifact

```text
CAPABILITY_ID=VNM-06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION
CAPABILITY_NAME=Native outer-context observation derivation around an induced ordered adjacent span
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1.sigma
SOURCE_GIT_BLOB=4d9f980e37aa01967509fc50fc4ea8c0a1cb0b6d
SOURCE_SHA256=067ab86267ca30167fd482e79486991d763062646a84173e5d55837de31dc5f5
BYTECODE_SHA256=4cdfc778d5aa169a5c9a0b40482946f3e50b5bfa6c1c10f2f9c3bb48d31d09c1
```

Runner:

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_PREFLIGHT.sh
RUNNER_GIT_BLOB=9b3a386f38d6d3447812c52eb66c6be16c49387c
RUNNER_SHA256=d5e1fd63d5cefcb33a714bc36d897a187a66a2666196233cca2a6e8370cd06c4
```

Admitted VNM-05 dependency identity recompiled/equality-gated by the runner:

```text
VNM05_SOURCE_SHA256=5158343391d7dce0046802162969211c8e7f73b873375a8bc376c0f6ea63c2b6
VNM05_BYTECODE_SHA256=a2b93c79733837b8e6c8b0c5a8d6368fc2f308bd71fc8ce0befded03c9b78912
VNM05_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE
```

## Operator-supplied machine evidence

The first full locked-runtime VNM-06 integration preflight reached and printed its complete PASS summary:

```text
TOTAL_VM_INVOCATIONS=20
VNM05_VM_INVOCATIONS=2
VNM06_VM_INVOCATIONS=18
POST_VM_ALIGNMENT_PASS_COUNT=18
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=14
INTEGRATION_PASS_COUNT=2
COUNTERFACTUAL_PASS_COUNT=1
INPUT_DYNAMIC=YES
OUTPUT_DEPENDS_ON_INPUT=YES
NEGATIVE_TEST=PASS
PERSISTENT_STATE=NO
PERSISTENT_STATE_TEST=NA
RESTART_REPLAY_TEST=PASS_PURE_CAPABILITY
REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
VNM05_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE
SPAN_CONTEXT_DERIVATION_OWNER=SIGMA_NATIVE
HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY
HOST_SPAN_CANDIDATE_GENERATION=NO
HOST_SPAN_MATCHING=NO
HOST_SPAN_CONTEXT_EXTRACTION=NO
HOST_BOUNDARY_INFERENCE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
STEP_LIMIT_STATUS=PASS_IN_20_INVOCATION_BOUNDED_SUITE
PRODUCTION_STATE_MUTATED=NO
VNM_06_PREFLIGHT=PASS
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
```

The supplied excerpt did not include a separate shell `RUNNER_RC` line. Keep:

```text
RUNNER_RC=UNKNOWN_NOT_SEPARATELY_SUPPLIED
```

This does not alter the machine-gated admission result because the exact runner emits `VNM_06_PREFLIGHT=PASS` and `ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE` only after all required aggregate gates have succeeded.

## Runtime scope exercised

The 18 VNM-06 case gates, plus two native VNM-05 dependency invocations, established the declared bounded behavior:

```text
01 native VNM-05 candidate + two interior occurrences -> two exact span-context observations
02 one interior occurrence -> one observation
03 left-edge occurrence -> match counted / context withheld
04 right-edge occurrence -> match counted / context withheld
05 reversed order -> no match
06 mixed interior + edge -> only interior observation emitted
07 exact duplicate sequence ID+fingerprint -> idempotent / no duplicate output
08 sequence-ID collision -> refusal / no output mutation
09 malformed sequence -> refusal / no output mutation
10 two-unit sequence -> refusal
11 five-unit sequence -> refusal
12 empty unit -> refusal
13 fifth unique sequence -> capacity refusal
14 >8 raw lines -> input-bound refusal before scan
15 malformed candidate -> refusal / no output mutation
16 non-induced/ambiguous candidate status -> refusal without host reinterpretation
17 materially different second native VNM-05 candidate -> materially different VNM-06 output
18 identical pure replay -> identical native stdout/output hash
```

## Admission record

```text
CAPABILITY_ID=VNM-06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION
CAPABILITY_NAME=Native outer-context observation derivation around an induced ordered adjacent span
TEACHING_GOAL=SIGMA natively matches an exact VNM-05 induced ordered span inside bounded delimiter-defined sequences and derives full LEFT/RIGHT outer-context observations without host span matching or context extraction
DEPENDENCIES=VNM05_ADMITTED_NATIVE_SPAN_CANDIDATE_PLUS_LOCKED_SIGMAC_VM_AND_EXISTING_MECHANICAL_STRING_FILE_MAP_LIST_ABI
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1.sigma
SOURCE_SHA256=067ab86267ca30167fd482e79486991d763062646a84173e5d55837de31dc5f5
BYTECODE_PATH=$HOME/SIGMA/SIGMA_VNM_06_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1_PREFLIGHT/SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1.sigmab
BYTECODE_SHA256=4cdfc778d5aa169a5c9a0b40482946f3e50b5bfa6c1c10f2f9c3bb48d31d09c1
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
TEST_SCOPE=20 locked-VM invocations: 2 VNM-05 native candidate generations plus 18 VNM-06 exact span-context derivation/refusal/counterfactual/replay gates
INPUT_DYNAMIC=YES
OUTPUT_DEPENDS_ON_INPUT=YES
NEGATIVE_TEST=PASS
PERSISTENT_STATE=NO
PERSISTENT_STATE_TEST=NA
RESTART_REPLAY_TEST=PASS_PURE_CAPABILITY
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
STEP_LIMIT_STATUS=PASS_IN_20_INVOCATION_BOUNDED_SUITE
PRODUCTION_STATE_MUTATED=NO
VM_RC=0_ALL_20_INVOCATIONS
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
CLAIM_SCOPE=Bounded exact native VNM-05 induced ordered width-2 span candidate mechanically routed into VNM-06; native matching inside 3-or-4 externally delimiter-defined UTF-8 unit sequences; full outer LEFT/RIGHT context derived only for interior span occurrences; edge matches withheld; duplicate/collision/malformed/capacity/input-bound refusal; no natural-language boundary or phrase-semantics claim
NEXT_DEPENDENCY_OR_CAPABILITY=DEPENDENCY_REVIEW_REQUIRED_AFTER_VNM06_ADMISSION
```

## Explicit non-claims

Keep:

```text
NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN
WORD_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_SEMANTICS=NOT_PROVEN
SEMANTIC_CONTEXT_EXTRACTION=NOT_PROVEN
SEMANTIC_EQUIVALENCE=NOT_PROVEN
DIACRITIC_EQUIVALENCE=NOT_PROVEN
WORD_MEANING=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
PRODUCTION_BINDING=NO
```

```text
VNM_06_ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
PRODUCTION_BINDING=NO
NEXT_ACTION=DEPENDENCY_REVIEW_FOR_SMALLEST_NEXT_VNM_CAPABILITY
```
