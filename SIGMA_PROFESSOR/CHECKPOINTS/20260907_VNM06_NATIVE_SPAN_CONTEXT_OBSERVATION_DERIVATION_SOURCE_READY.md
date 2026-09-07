# VNM-06 — Native Span-Context Observation Derivation — SOURCE READY

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: SOURCE READY / LOCKED-RUNTIME ADMISSION NOT YET RUN

## Governance / dependency review

The repository stop-gate, global native teaching/admission standard, exclusive self-learning/anti-hardcode lock, native artifact build/admission method, current handoff, language lane, VNM course directive, VNM living handoff, and VNM-05 FIX1 admission evidence were re-read before selecting VNM-06.

VNM-05 is admitted in its exact bounded structural scope. Repository search/inventory did not surface an admitted native `SPAN_CONTEXT` or `CHUNK` capability that should be reused instead.

The smallest next dependency is therefore not natural-language word/phrase boundary discovery. It is a pure structural bridge that lets an already native-induced VNM-05 span participate in later learning without host matching the span or constructing its outer context.

Core locks:

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

## Capability contract

```text
CAPABILITY_ID=VNM-06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION
CAPABILITY_NAME=Native outer-context observation derivation around an induced ordered adjacent span
```

Teaching goal:

Given an exact VNM-05 `ADJACENT_SPAN_CANDIDATE_INDUCED` candidate plus bounded 3-or-4 externally delimiter-defined UTF-8 sequences, native SIGMA must itself:

- validate the candidate protocol;
- validate/deduplicate bounded sequence records and reject ID collisions;
- find exact ordered `UNIT_A -> UNIT_B` occurrences;
- preserve order (`A->B != B->A` structurally);
- withhold edge occurrences that lack both outer neighbors;
- for an interior occurrence in a 4-unit sequence `L~A~B~R`, derive exact `LEFT=L` and `RIGHT=R` around the full span;
- preserve sequence/source provenance in native output records;
- refuse malformed/collision/capacity/input-bound cases without output mutation;
- replay identically for identical pure input.

Host may only exact-decode/reroute native VNM-05 fields, write fixture bytes, invoke compiler/VM, hash/log, and run post-VM oracles. Host must not generate/select the span candidate, match span occurrences, infer edges/boundaries, or derive LEFT/RIGHT context.

## Input ABI

Candidate:

```text
CANDIDATE||STATUS||ADJACENT_SPAN_CANDIDATE_INDUCED||UNIT_A||<a>||UNIT_B||<b>||SUPPORT||<support>
```

Sequences:

```text
SEQ||<seq_id>||UNITS||u0~u1~u2[~u3]||SOURCE||<source_id>
```

Native output bundle:

```text
SPAN_OBS||<seq_id>||UNIT_A||<a>||UNIT_B||<b>||LEFT||<left>||RIGHT||<right>||SOURCE||<source_id>
```

Only an interior width-2 occurrence in a 4-unit sequence has both outer neighbors and can produce `SPAN_OBS`. Matches at either sequence edge are counted but withheld.

## Bounds / policy

```text
MAX_SEQUENCE_SPLIT_LINES=8
MAX_SEQUENCES=4
MAX_UNITS_PER_SEQUENCE=4
MAX_OUTPUT_OBSERVATIONS=4
PERSISTENT_STATE=NO
ORDER_POLICY=ORDERED_EXACT_SPAN_MATCH
EDGE_POLICY=WITHHOLD_IF_FULL_LEFT_RIGHT_CONTEXT_UNAVAILABLE
```

## Native source

```text
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1.sigma
SOURCE_COMMIT=80374f5f77ecab2d3ee754c90f04894a1b15fe3c
SOURCE_GIT_BLOB=4d9f980e37aa01967509fc50fc4ea8c0a1cb0b6d
SOURCE_SHA256=067ab86267ca30167fd482e79486991d763062646a84173e5d55837de31dc5f5
```

Static source audit:

```text
NOT_EQUAL_TOKEN_COUNT=0
NEW_HOST_PRIMITIVE_REQUIRED=NO
HOST_CALL_SET=read_text,write_text,str_split,str_join,list_new,list_len,list_get,list_push,map_new,map_has,map_get,map_set
SPAN_CONTEXT_DERIVATION_OWNER=SIGMA_NATIVE_BY_SOURCE_DESIGN
HOST_SPAN_MATCHING=NO_BY_SOURCE_DESIGN
HOST_SPAN_CONTEXT_EXTRACTION=NO_BY_SOURCE_DESIGN
HOST_BOUNDARY_INFERENCE=NO_BY_SOURCE_DESIGN
HOST_LEARNING=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_INTERPRETATION=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_SUBSTITUTION=NO_BY_SOURCE_DESIGN
ACTIVE_PYTHON_COGNITION=NO
```

## Runner

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_PREFLIGHT.sh
RUNNER_COMMIT=d8082b09a733f8c65a1d39def22a34ec9f8ee3b4
RUNNER_GIT_BLOB=9b3a386f38d6d3447812c52eb66c6be16c49387c
RUNNER_SHA256=d5e1fd63d5cefcb33a714bc36d897a187a66a2666196233cca2a6e8370cd06c4
RUNNER_STATIC_BASH_SYNTAX=PASS
```

The runner recompiles/equality-gates the exact admitted VNM-05 source and requires its bytecode SHA256 to equal the admitted VNM-05 bytecode SHA256 before using it as a dependency. VNM-06 is compiled before dynamic fixtures are generated.

Two positive/counterfactual candidate records are produced from actual VNM-05 native VM outputs. Host uses exact protocol decode/routing only.

A pre-upload static review caught and removed a shell command-substitution design that would have hidden VM counter increments inside a subshell. This was corrected before any locked runtime and is not runtime failure evidence.

## Planned exact runtime matrix

Component totals:

```text
TOTAL_VM_INVOCATIONS=20
VNM05_VM_INVOCATIONS=2
VNM06_VM_INVOCATIONS=18
```

VNM-06 case-level gates:

```text
01 native VNM-05 candidate + two interior occurrences -> two exact span-context observations
02 one interior occurrence -> one observation
03 left-edge occurrence -> match counted, context withheld
04 right-edge occurrence -> match counted, context withheld
05 reversed order -> no match
06 mixed interior + edge -> only interior observation emitted
07 exact duplicate sequence ID+fingerprint -> idempotent, no duplicate output
08 same sequence ID/different fingerprint -> collision refusal / output unchanged
09 malformed record -> refusal / output unchanged
10 two-unit sequence -> refusal
11 five-unit sequence -> refusal
12 empty unit -> refusal
13 fifth unique sequence -> capacity refusal
14 >8 raw lines -> input-bound refusal before scan
15 malformed candidate -> refusal / output unchanged
16 non-induced/ambiguous candidate status -> refusal; host does not reinterpret it
17 materially different second native VNM-05 candidate -> VNM-06 output changes
18 identical pure replay of case 17 -> identical native stdout/output hash
```

Pre-counted aggregate accounting:

```text
POST_VM_ALIGNMENT_PASS_COUNT=18
NEGATIVE_PASS_COUNT=14
INTEGRATION_PASS_COUNT=2
COUNTERFACTUAL_PASS_COUNT=1
```

## Required admission gate

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
PRODUCTION_STATE_MUTATED=NO
VNM_06_PREFLIGHT=PASS
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
```

## Current proof state

```text
VNM_05_ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
VNM_06_SOURCE_READY=YES
VNM_06_LOCKED_SIGMAC_COMPILE=NOT_RUN
VNM_06_BYTECODE_SHA256=UNKNOWN
VNM_06_LOCKED_VM_RUNTIME=NOT_RUN
VNM_06_ADMISSION=NOT_RUN
PRODUCTION_BINDING=NO
```

## Explicit non-claims

```text
NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN
WORD_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_SEMANTICS=NOT_PROVEN
SEMANTIC_CONTEXT_EXTRACTION=NOT_PROVEN
WORD_MEANING=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
```

```text
NEXT_ACTION=PULL_AND_RUN_FULL_VNM06_LOCKED_INTEGRATION_PREFLIGHT
```
