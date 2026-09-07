# VNM-05 — Native Recurrent Adjacent-Span Candidate Induction — SOURCE READY

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: SOURCE READY / LOCKED-RUNTIME ADMISSION NOT YET RUN

## Governance re-read

Before selecting/building VNM-05, the lane re-read the repository stop-gate and current VNM/language state, including:

- `/AGENTS.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_IMPORTANT_NATIVE_DNA_ARTIFACT_BUILD_ADMISSION_METHOD_V1.md`
- `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`
- `SIGMA_PROFESSOR/DIRECTIVES/TEACHER_GPT_VNM_NATIVE_VIETNAMESE_CAPABILITY_COURSE_V1.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_VNM_LANE_CURRENT.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/20260907_VNM04_FIX2_FULL_NATIVE_CHAIN_ADMISSION_PASS.md`

Core locks remain:

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
RUNTIME_PROOF_REQUIRED=YES
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
ACTIVE_PYTHON_COGNITION=FORBIDDEN
HOST_SPAN_GENERATION=NO
HOST_SPAN_SELECTION=NO
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

## Dependency decision

VNM-01 through VNM-04 are admitted in their exact tested structural scopes. The admitted full chain still begins from externally delimiter-defined UTF-8 units; it does not prove word boundaries or tokenization.

Repository/language-lane inventory did not surface an admitted native capability that already performs recurrent ordered adjacent-span candidate induction over these units. Therefore VNM-05 is selected as the smallest next reusable structural capability toward later phrase/chunk learning without making a semantic phrase claim.

VNM-05 deliberately does **not** attempt natural-language boundary discovery. It consumes the same explicit `~` unit boundaries already admitted as fixture structure in VNM-03.

## Capability contract

```text
CAPABILITY_ID=VNM-05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION
CAPABILITY_NAME=Native recurrent ordered adjacent-span candidate induction over delimiter-defined UTF-8 units

WHAT_CAPABILITY_IS_SIGMA_BEING_TAUGHT=
Given bounded 3-or-4-unit UTF-8 sequences with externally declared `~` unit boundaries, SIGMA must itself enumerate ordered width-2 adjacent spans, accumulate sequence evidence persistently across fresh VM invocations, measure support by distinct sequence ID rather than raw occurrence count, select a unique strongest recurrent span, preserve ambiguity under equal recurrent support, or withhold when recurrence is insufficient.

WHAT_MUST_SIGMA_COMPUTE_ITSELF=
sequence validation;
duplicate/collision handling;
adjacent ordered span generation;
span identity comparison;
distinct-sequence support counting;
minimum recurrence qualification;
unique strongest candidate selection;
tie ambiguity;
persistent sequence-state update/readback;
refusal decisions;
current candidate status after restart.

WHAT_MAY_HOST_DO_MECHANICALLY=
compile exact native source with locked sigmac;
run locked VM;
create dynamic structural fixtures after compile;
copy/write exact fixture bytes;
hash/log exact artifacts;
perform post-VM oracles and isolated fault fixtures.

WHAT_RUNTIME_EVIDENCE_WILL_PROVE_THE_CAPABILITY=
one sequence remains insufficient;
a second distinct sequence containing the same ordered span changes the native result to candidate induced;
a fresh VM with no new input reuses persisted state and retains the candidate;
A->B and B->A do not pool support;
two A->B occurrences inside one sequence count as support 1, not 2;
two independent recurrent spans at equal support remain ambiguous;
exact duplicate sequence IDs are idempotent;
ID collision/malformed/2-unit/5-unit/empty-unit/capacity/input-bound cases refuse without mutation;
a materially different high-entropy UTF-8 pair changes the native candidate;
identical full input/prestate replay is byte-identical;
no dynamic token leaks into frozen source/bytecode.

WHAT_RESULT_WOULD_FALSIFY_THE_CLAIM=
host generates/selects the span candidate;
one sequence with repeated A->B is credited with recurrent support 2;
A->B and B->A are merged;
a tie is silently resolved by encounter order;
fresh VM loses material learned state;
invalid/refused input mutates state;
identical replay differs;
any VM is nonzero or hits step limit;
source/bytecode changes or contains unseen dynamic tokens.

WHAT_DEPENDENCY_MUST_EXIST_FIRST=
VNM-04 admitted full structural chain;
locked SIGMAC/VM;
existing mechanical read/write_text, split/join, list/map ABI.
```

## Input/state ABI

Runtime input:

```text
.sigma_exec/SIGMA_VNM_05_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1/input/sequences.memory
```

Record:

```text
SEQ||<seq_id>||UNITS||u0~u1~u2[~u3]||SOURCE||<source_id>
```

Persistent state:

```text
.sigma_exec/SIGMA_VNM_05_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1/state/adjacent_span_state.memory
```

State header:

```text
STATE||SIGMA_VNM_05_ADJACENT_SPAN_STATE_V1||COMMIT||YES
```

State records preserve the exact accepted sequence record plus:

```text
||COMMIT||YES
```

## Native structural policy

```text
MAX_SEQUENCES=4
MAX_NEW_SPLIT_LINES=8
MAX_UNITS_PER_SEQUENCE=4
MAX_ADJACENT_OCCURRENCES=12
MIN_SPAN_SUPPORT=2
SUPPORT_UNIT=DISTINCT_SEQUENCE_ID
SPAN_ORDER_POLICY=ORDERED_ADJACENCY
```

For each admitted sequence, native SIGMA generates width-2 adjacent spans:

```text
u0->u1
u1->u2
[ u2->u3 ]
```

Support for a span is the number of **distinct sequence IDs** containing that ordered span. Multiple occurrences of the same span within one sequence do not increase support beyond one for that sequence.

Native result states:

```text
INSUFFICIENT_RECURRENT_SPAN_EVIDENCE
ADJACENT_SPAN_CANDIDATE_INDUCED
AMBIGUOUS_ADJACENT_SPAN_CANDIDATE
REFUSED_PREVIOUS_STATE_INVALID
REFUSED_INPUT_BOUND
REFUSED_SEQUENCE_RECORD_INVALID
REFUSED_SEQUENCE_ID_COLLISION
REFUSED_SEQUENCE_CAPACITY
REFUSED_ADJACENT_OCCURRENCE_CAPACITY
REFUSED_PERSISTENCE_FAILURE
```

## Native source

```text
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1.sigma
SOURCE_COMMIT=b60e774b51a129ec64a60eef9f3ec19e26014c01
SOURCE_GIT_BLOB=bcdbbfb1565de4733580e730c1ee428bd09d1500
SOURCE_SHA256=5158343391d7dce0046802162969211c8e7f73b873375a8bc376c0f6ea63c2b6
ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP
```

Static source review:

```text
NOT_EQUAL_TOKEN_COUNT=0
HOST_CALL_SET=
read_text
write_text
str_split
str_join
list_new
list_len
list_get
list_push
map_new
map_has
map_get
map_set

NEW_HOST_PRIMITIVE_REQUIRED=NO
HOST_SPAN_GENERATION=NO_BY_SOURCE_DESIGN
HOST_SPAN_SELECTION=NO_BY_SOURCE_DESIGN
HOST_BOUNDARY_INFERENCE=NO_BY_SOURCE_DESIGN
HOST_LEARNING=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_INTERPRETATION=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_SUBSTITUTION=NO_BY_SOURCE_DESIGN
ACTIVE_PYTHON_COGNITION=NO
```

## Locked-runtime runner

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_PREFLIGHT.sh
RUNNER_COMMIT=e066b9c7aab19e74e91df15545f762956743a4dc
RUNNER_GIT_BLOB=27771ff9e7621cb3bc1914389b5bf40267238fb1
RUNNER_SHA256=f011886e977a2e4cd76afa561c18ff046c2d0d799b5de797d778958bcd19f2c4
RUNNER_STATIC_BASH_SYNTAX=PASS
PLANNED_VM_INVOCATIONS=20
```

The runner compiles and freezes the exact source **before** creating high-entropy dynamic fixtures.

## Planned 20-invocation matrix

```text
01 one sequence -> insufficient; state persisted
02 fresh VM + second distinct sequence -> ordered span induced support 2
03 fresh VM / empty new input -> persisted candidate retained
04 one competing-span sequence -> original recurrent candidate remains unique strongest
05 second competing-span sequence -> equal support tie -> ambiguity
06 one 4-unit sequence -> 3 occurrences but no recurrent candidate
07 A->B versus B->A -> no pooled support
08 A->B occurs twice inside one sequence -> support does not inflate to 2
09 unique strongest recurrent ordered span
10 two recurrent spans support 2 each -> ambiguity
11 exact duplicate sequence ID+fingerprint -> idempotent, no support inflation
12 same sequence ID / different fingerprint -> collision refusal / no state mutation
13 malformed record refusal / no state mutation
14 2-unit sequence refusal
15 5-unit sequence refusal
16 empty-unit sequence refusal
17 fifth unique sequence -> capacity refusal / fail closed
18 >8 raw lines -> input-bound refusal before record scan
19 materially different unseen UTF-8 pair -> candidate changes
20 identical replay of 19 -> identical native stdout/state hash
```

Required aggregate hard gate:

```text
TOTAL_VM_INVOCATIONS=20
POST_VM_ALIGNMENT_PASS_COUNT=20
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=11
PERSISTENCE_PASS_COUNT=3
COUNTERFACTUAL_PASS_COUNT=1
REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
DISTINCT_SEQUENCE_SUPPORT_TEST=PASS
ORDERED_ADJACENCY_TEST=PASS
TIE_AMBIGUITY_TEST=PASS
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
SPAN_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE
HOST_SPAN_GENERATION=NO
HOST_SPAN_SELECTION=NO
HOST_BOUNDARY_INFERENCE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED=NO
VNM_05_PREFLIGHT=PASS
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
```

## Current proof state

```text
LOCKED_SIGMAC_COMPILE=NOT_RUN
BYTECODE_SHA256=UNKNOWN
LOCKED_VM_RUNTIME=NOT_RUN
TOTAL_VM_INVOCATIONS=0
INPUT_DYNAMIC=PLANNED_AFTER_COMPILE
OUTPUT_DEPENDS_ON_INPUT=NOT_PROVEN
NEGATIVE_TEST=NOT_RUN
PERSISTENT_STATE=YES_BY_DESIGN
PERSISTENT_STATE_TEST=NOT_RUN
RESTART_REPLAY_TEST=NOT_RUN
STEP_LIMIT_STATUS=NOT_PROVEN
PRODUCTION_STATE_MUTATED=NO
ADMISSION=NOT_RUN
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

VNM-05 is a persistent structural chunk-candidate substrate only. It does not prove that the selected adjacent span is a linguistic word, phrase, constituent, or meaningful expression.

```text
NEXT_ACTION=PULL_AND_RUN_FULL_VNM05_LOCKED_RUNTIME_PREFLIGHT
```
