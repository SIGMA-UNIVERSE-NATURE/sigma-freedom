# VNM-07 — Native Span Observation to Form Observation Adapter — SOURCE READY

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: SOURCE READY / LOCKED-RUNTIME ADMISSION NOT YET RUN

## Governance / dependency review

The repository stop-gate, global native teaching/admission standard, exclusive self-learning/anti-hardcode lock, native build/admission method, current handoff, language lane, VNM course directive, VNM living handoff, exact VNM-02/VNM-05/VNM-06 sources, and VNM-06 admission evidence were reviewed before selecting VNM-07.

VNM-06 is admitted in exact bounded structural scope. It can emit native `SPAN_OBS` records containing an ordered induced span and full outer `LEFT/RIGHT` context. Repository search did not surface an admitted native adapter that converts this representation into the already-admitted VNM-02 observation ABI.

Dependency-first selection therefore reuses VNM-02 instead of duplicating pair-induction cognition. VNM-07 teaches only the missing native structural representation bridge.

Core locks:

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
ACTIVE_PYTHON_COGNITION=FORBIDDEN
HOST_FORM_SERIALIZATION=NO
HOST_OBSERVATION_ID_DERIVATION=NO
HOST_PAIR_GENERATION=NO
HOST_PAIR_SELECTION=NO
HOST_CONTEXT_EXTRACTION=NO
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
CAPABILITY_ID=VNM-07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER
CAPABILITY_NAME=Native ordered-span structural serialization into VNM-02-compatible form observations
```

Teaching goal:

Given bounded VNM-06 `SPAN_OBS` records, native SIGMA must itself:

- validate the exact span-observation protocol;
- preserve ordered span identity;
- serialize `UNIT_A -> UNIT_B` structurally as `FORM = UNIT_A~UNIT_B`;
- derive an observation identity from sequence ID plus ordered span;
- preserve exact `LEFT`, `RIGHT`, and `SOURCE` provenance;
- emit VNM-02-compatible `OBS` records;
- suppress exact duplicates;
- reject derived-ID collisions;
- reject ambiguous reserved-delimiter inputs;
- refuse malformed/capacity/input-bound batches without output mutation;
- replay identically for identical pure input.

The host may only invoke locked compiler/VM, copy exact files/bytes, insert exact protocol record separators, mechanically decode already-emitted native fields, hash/log, and run post-VM oracles. Host must not serialize the FORM, derive observation IDs, generate/select the downstream pair, or infer context.

## Input/output ABI

Input record from VNM-06:

```text
SPAN_OBS||<seq_id>||UNIT_A||<a>||UNIT_B||<b>||LEFT||<left>||RIGHT||<right>||SOURCE||<source_id>
```

Native VNM-07 output:

```text
OBS||VNM07:<seq_id>~<a>~<b>||FORM||<a>~<b>||LEFT||<left>||RIGHT||<right>||SOURCE||<source_id>
```

Reserved-delimiter scope:

```text
`~` is reserved inside VNM-07 derived observation IDs and ordered span FORM serialization.
The adapter therefore requires seq_id, UNIT_A, and UNIT_B to contain no `~`.
This is compatible with the admitted delimiter-defined-unit path where valid individual units themselves do not contain `~`.
```

This is structural serialization only. `UNIT_A~UNIT_B` is not claimed to be a linguistic word or phrase.

## Bounds / policy

```text
MAX_INPUT_SPLIT_LINES=8
MAX_SPAN_OBSERVATIONS=4
MAX_OUTPUT_OBSERVATIONS=4
FORM_SERIALIZATION_POLICY=ORDERED_UNIT_A_TILDE_UNIT_B
OBSERVATION_ID_POLICY=VNM07_SEQID_AND_ORDERED_SPAN
PERSISTENT_STATE=NO
```

## Native source

```text
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_V1.sigma
SOURCE_COMMIT=45af307748ce247f0b67f968aeb7c29fdca4241d
SOURCE_GIT_BLOB=6d521ab0b03126ab23ffc9b85996ac0c4eb599e3
SOURCE_SHA256=8412ce07e6c9a53ae6bb27a88ec2847eadd54795a21dce35a3ff1ef29f75a57e
```

Static source audit:

```text
NOT_EQUAL_TOKEN_COUNT=0
NEW_HOST_PRIMITIVE_REQUIRED=NO
HOST_CALL_SET=read_text,write_text,str_split,str_join,list_new,list_len,list_get,list_push,map_new,map_has,map_get,map_set
SPAN_FORM_SERIALIZATION_OWNER=SIGMA_NATIVE_BY_SOURCE_DESIGN
OBSERVATION_ID_DERIVATION_OWNER=SIGMA_NATIVE_BY_SOURCE_DESIGN
HOST_FORM_SERIALIZATION=NO_BY_SOURCE_DESIGN
HOST_OBSERVATION_ID_DERIVATION=NO_BY_SOURCE_DESIGN
HOST_PAIR_SELECTION=NO_BY_SOURCE_DESIGN
HOST_LEARNING=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_INTERPRETATION=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_SUBSTITUTION=NO_BY_SOURCE_DESIGN
ACTIVE_PYTHON_COGNITION=NO
```

## Runner

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_PREFLIGHT.sh
RUNNER_COMMIT=34016964834de4749dd9f91ec460ae2adc49c7e2
RUNNER_GIT_BLOB=840d6d86e11b7bc8fc8e881ee7dc5cb26e9c5ee3
RUNNER_SHA256=ef2fe0776de85622b737a9161b4959ff4b6bba28832ac483a6a129d42463327a
RUNNER_STATIC_BASH_SYNTAX=PASS
```

The runner recompiles and equality-gates exact admitted dependencies:

```text
VNM02_SOURCE_SHA256=f2c5f266492fd990887a356bd353d545f480f51ad6bb1ba63ca5a727320bbac3
VNM02_BYTECODE_SHA256=bf6f3cac8aade9433f43c13d462a73465eceef0b1e5f5411336cad2e338b0aec
VNM05_SOURCE_SHA256=5158343391d7dce0046802162969211c8e7f73b873375a8bc376c0f6ea63c2b6
VNM05_BYTECODE_SHA256=a2b93c79733837b8e6c8b0c5a8d6368fc2f308bd71fc8ce0befded03c9b78912
VNM06_SOURCE_SHA256=067ab86267ca30167fd482e79486991d763062646a84173e5d55837de31dc5f5
VNM06_BYTECODE_SHA256=4cdfc778d5aa169a5c9a0b40482946f3e50b5bfa6c1c10f2f9c3bb48d31d09c1
```

VNM-07 is compiled and frozen before dynamic fixtures are generated.

## Planned integration chain

Two materially different native span candidates are produced by VNM-05. Each is routed through VNM-06 to generate two native outer-context observations under the same two structural contexts. Each VNM-06 bundle is then routed exactly into VNM-07. The two VNM-07 output bundles are joined only with one exact record-separator newline and passed unchanged into VNM-02.

```text
VNM-05 native candidate A
-> VNM-06 native SPAN_OBS A in context C1/C2
-> VNM-07 native FORM observations for A

VNM-05 native candidate B
-> VNM-06 native SPAN_OBS B in context C1/C2
-> VNM-07 native FORM observations for B

exact mechanical record framing
-> VNM-02 native pair induction
```

The downstream VNM-02 gate requires native induction of the pair of the two serialized span forms with support `2`. Host pair generation/selection is forbidden.

## Planned exact runtime matrix

Component totals:

```text
TOTAL_VM_INVOCATIONS=21
VNM05_VM_INVOCATIONS=2
VNM06_VM_INVOCATIONS=2
VNM07_VM_INVOCATIONS=16
VNM02_VM_INVOCATIONS=1
```

VNM-07 case-level gates:

```text
01 exact native VNM-06 bundle A -> two exact VNM-02-compatible observations
02 exact native VNM-06 bundle B -> two exact VNM-02-compatible observations
03 one valid direct structural observation -> one output
04 exact duplicate -> idempotent suppression
05 same derived ID/different fingerprint -> collision refusal / no output mutation
06 malformed record -> refusal / no output mutation
07 empty unit -> refusal
08 reserved `~` in seq_id -> refusal
09 reserved `~` in UNIT_A -> refusal
10 reserved `~` in UNIT_B -> refusal
11 fifth unique observation -> capacity refusal
12 >8 raw lines -> input-bound refusal before scan
13 empty batch -> valid no-op
14 materially different high-entropy span -> output changes
15 A->B versus B->A -> different ordered serialization
16 exact pure replay of case 14 -> identical stdout/output hash
```

Additional integration gate:

```text
exact outputs of case 01 and 02
-> VNM-02 native PAIR_CANDIDATE_INDUCED
-> PAIR_CANDIDATE_SUPPORT=2
-> native candidate form set equals the two VNM-07 serialized span forms
```

Pre-counted aggregate accounting:

```text
POST_VM_ALIGNMENT_PASS_COUNT=16
NEGATIVE_PASS_COUNT=10
INTEGRATION_PASS_COUNT=3
COUNTERFACTUAL_PASS_COUNT=1
ORDERED_SPAN_SERIALIZATION_TEST=PASS_REQUIRED
DOWNSTREAM_VNM02_PAIR_INDUCTION_TEST=PASS_REQUIRED
```

## Required admission gate

```text
TOTAL_VM_INVOCATIONS=21
VNM05_VM_INVOCATIONS=2
VNM06_VM_INVOCATIONS=2
VNM07_VM_INVOCATIONS=16
VNM02_VM_INVOCATIONS=1
POST_VM_ALIGNMENT_PASS_COUNT=16
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=10
INTEGRATION_PASS_COUNT=3
COUNTERFACTUAL_PASS_COUNT=1
INPUT_DYNAMIC=YES
OUTPUT_DEPENDS_ON_INPUT=YES
NEGATIVE_TEST=PASS
PERSISTENT_STATE=NO_FOR_VNM07_PURE_ADAPTER;YES_IN_DOWNSTREAM_VNM02_INTEGRATION
PERSISTENT_STATE_TEST=PASS_IN_DOWNSTREAM_VNM02_INTEGRATION
RESTART_REPLAY_TEST=PASS_PURE_CAPABILITY
REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
ORDERED_SPAN_SERIALIZATION_TEST=PASS
DOWNSTREAM_VNM02_PAIR_INDUCTION_TEST=PASS
VNM05_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE
VNM06_SPAN_CONTEXT_DERIVATION_OWNER=SIGMA_NATIVE
VNM07_SPAN_FORM_SERIALIZATION_OWNER=SIGMA_NATIVE
VNM07_OBSERVATION_ID_DERIVATION_OWNER=SIGMA_NATIVE
VNM02_PAIR_INDUCTION_OWNER=SIGMA_NATIVE
HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY
HOST_FORM_SERIALIZATION=NO
HOST_OBSERVATION_ID_DERIVATION=NO
HOST_PAIR_GENERATION=NO
HOST_PAIR_SELECTION=NO
HOST_CONTEXT_EXTRACTION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
PRODUCTION_STATE_MUTATED=NO
VNM_07_PREFLIGHT=PASS
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
```

## Current proof state

```text
VNM_06_ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
VNM_07_SOURCE_READY=YES
VNM_07_LOCKED_SIGMAC_COMPILE=NOT_RUN
VNM_07_BYTECODE_SHA256=UNKNOWN
VNM_07_LOCKED_VM_RUNTIME=NOT_RUN
VNM_07_ADMISSION=NOT_RUN
PRODUCTION_BINDING=NO
```

## Explicit non-claims

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
NEXT_ACTION=PULL_AND_RUN_FULL_VNM07_LOCKED_INTEGRATION_PREFLIGHT
```
