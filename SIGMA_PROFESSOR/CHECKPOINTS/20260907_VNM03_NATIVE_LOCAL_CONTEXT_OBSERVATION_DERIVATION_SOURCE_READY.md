# VNM-03 — Native Local-Context Observation Derivation — SOURCE READY

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: SOURCE READY / LOCKED-RUNTIME ADMISSION NOT YET RUN

## Governance re-read

Before VNM-03 selection and build, the lane re-read:

- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
- `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_IMPORTANT_NATIVE_DNA_ARTIFACT_BUILD_ADMISSION_METHOD_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/TEACHER_GPT_VNM_NATIVE_VIETNAMESE_CAPABILITY_COURSE_V1.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_VNM_LANE_CURRENT.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`
- VNM-01 and VNM-02 admission evidence.

Non-negotiable:

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
RUNTIME_PROOF_REQUIRED=YES
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
ACTIVE_PYTHON_COGNITION=FORBIDDEN
HOST_CONTEXT_EXTRACTION=NO
HOST_UNIT_SELECTION=NO
HOST_PAIR_SELECTION=NO
HOST_NORMALIZATION=NO
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

## Dependency review

VNM-02 is admitted in exact tested scope:

```text
CAPABILITY_ID=VNM-02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION
SOURCE_SHA256=f2c5f266492fd990887a356bd353d545f480f51ad6bb1ba63ca5a727320bbac3
BYTECODE_SHA256=bf6f3cac8aade9433f43c13d462a73465eceef0b1e5f5411336cad2e338b0aec
TOTAL_VM_INVOCATIONS=18
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
```

VNM-02 still requires externally supplied opaque structural `LEFT/RIGHT` fields. That is the smallest immediate dependency gap before claiming a more autonomous input chain.

The language lane contains admitted structural hypothesis/reference capabilities, but no current capability removes this exact VNM-02 input dependency. VNM-03 therefore teaches a distinct structural transform rather than duplicating LANG-01 or VNM-02 logic.

Selected capability:

```text
VNM-03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION
```

It deliberately does **not** claim natural-language tokenization. Unit boundaries remain explicitly supplied by the `~` delimiter. SIGMA must derive local neighbor context from those units itself.

## Capability contract

```text
CAPABILITY_ID=VNM-03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION
CAPABILITY_NAME=Native local-context observation derivation from delimiter-defined UTF-8 sequences

WHAT_CAPABILITY_IS_SIGMA_BEING_TAUGHT=
Given bounded sequence records containing 3 or 4 opaque UTF-8 units separated by an exact delimiter, SIGMA must itself derive each interior unit as a VNM-02-compatible observation with its immediate LEFT and RIGHT neighbors, preserve source provenance, deduplicate exact sequence records, and refuse malformed/colliding/out-of-bound batches without output mutation.

WHAT_MUST_SIGMA_COMPUTE_ITSELF=
sequence record validation;
unit split and bounded unit-count validation;
interior-unit selection;
LEFT neighbor selection;
RIGHT neighbor selection;
derived observation IDs;
VNM-02-compatible observation records;
exact duplicate suppression;
sequence-ID collision detection;
output eligibility and write/readback state.

WHAT_MAY_HOST_DO_MECHANICALLY=
write exact dynamic sequence fixture bytes after compile;
invoke locked sigmac/VM;
create isolated namespaces;
hash source/bytecode/input/output/log bytes;
preload output sentinels for no-mutation tests;
perform post-VM exact byte/oracle checks;
mechanically route admitted output bytes to VNM-02 in a later integration gate.

WHAT_RUNTIME_EVIDENCE_WILL_PROVE_THE_CAPABILITY=
3-unit sequence -> exactly one derived observation;
4-unit sequence -> exactly two interior observations;
multiple sequences accumulate deterministically;
UTF-8 form/context/source bytes are preserved exactly;
duplicate sequence is idempotent;
sequence-ID collision, malformed record, too few/many units, empty unit, sequence-capacity and raw-input-bound cases refuse without output mutation;
exact structural maximum produces eight observations;
materially different dynamic sequence changes native output;
fresh-namespace identical input replay produces identical native stdout and output bytes;
source/bytecode remain frozen and unseen dynamic tokens do not leak into them.

WHAT_RESULT_WOULD_FALSIFY_THE_CLAIM=
host chooses the interior form or left/right context for SIGMA;
derived output disagrees with exact neighboring units;
duplicate creates extra observations;
refusal overwrites output;
malformed/out-of-bound input still produces admitted observations;
material input change does not change output;
identical pure replay differs;
step-limit is hit in the bounded suite;
dynamic tokens appear in frozen source/bytecode.

WHAT_DEPENDENCY_MUST_EXIST_FIRST=
VNM-02 admitted downstream pair-induction substrate;
locked SIGMAC/VM identities;
existing mechanical read/write_text, split/join, list and map ABI.
```

## Input/output ABI

Input sequence record:

```text
SEQ||<seq_id>||UNITS||<u0>~<u1>~<u2>[~<u3>]||SOURCE||<source_id>
```

The `~` separator is an exact structural delimiter only:

```text
UNIT_DELIMITER_POLICY=EXACT_TILDE_ONLY
UNIT_BOUNDARY_SEMANTIC=NO
NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN
```

For a 3-unit sequence, native SIGMA derives:

```text
OBS||<seq_id>:1||FORM||<u1>||LEFT||<u0>||RIGHT||<u2>||SOURCE||<source_id>
```

For a 4-unit sequence it additionally derives:

```text
OBS||<seq_id>:2||FORM||<u2>||LEFT||<u1>||RIGHT||<u3>||SOURCE||<source_id>
```

These records are byte-compatible with the admitted VNM-02 observation ABI.

## Native bounded parameters

```text
MAX_SEQUENCES=4
MAX_RAW_SPLIT_LINES=8
MIN_UNITS_PER_SEQUENCE=3
MAX_UNITS_PER_SEQUENCE=4
MAX_DERIVED_OBSERVATIONS=8
PERSISTENT_STATE=NO
```

The maximum derived-observation count follows structurally from `4 sequences * 2 interior units = 8`.

## Native source

```text
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1.sigma
SOURCE_COMMIT=b2570a09fce38b077fc5c941c96a6c78020b1cdb
SOURCE_GIT_BLOB=80c0f4291ac3051b077d34010fa07719f231554c
SOURCE_SHA256=c0d54fe4c36f59ac1b4a1cd431e2078333ee5d28b8fa2f2fb2d5f1813e6beb34
ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP
```

## Static review

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

FORBIDDEN_SEMANTIC_CONVENIENCE_TOKEN_SCAN=PASS
HOST_CONTEXT_EXTRACTION=NO_BY_SOURCE_DESIGN
HOST_UNIT_SELECTION=NO_BY_SOURCE_DESIGN
HOST_PAIR_SELECTION=NO_BY_SOURCE_DESIGN
HOST_NORMALIZATION=NO_BY_SOURCE_DESIGN
HOST_LEARNING=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_INTERPRETATION=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_SUBSTITUTION=NO_BY_SOURCE_DESIGN
ACTIVE_PYTHON_COGNITION=NO
```

Input-bound overflow sets native `SCAN_LINE_COUNT=0`; refusal paths do not call `write_text`. This keeps invalid/out-of-bound batches fail-closed in the proposed runtime scope.

## Locked-runtime runner

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION_PREFLIGHT.sh
RUNNER_COMMIT=daa54d2cda460b332506cc331693400c17b1c2cc
RUNNER_GIT_BLOB=8927aa85a6ddfdbbf5bf66a9777d9db7138bcbc1
RUNNER_SHA256=d07ba5edf779fd9305504a784f457f8886542c3ad5ee0b434a19598a3ec3e2ae
RUNNER_STATIC_BASH_SYNTAX=PASS
PLANNED_VM_INVOCATIONS=18
```

The runner equality-gates locked SIGMAC/VM, VNM-03 source and admitted VNM-02 source identity. It compiles VNM-03 before generating dynamic UTF-8 units, freezes bytecode, preserves raw native stdout/output bytes before post-VM oracle checks, and uses no Python cognition.

## Planned 18-invocation admission matrix

```text
01 valid 3-unit sequence -> 1 exact derived observation
02 valid 4-unit sequence -> 2 exact interior observations
03 two valid sequences -> deterministic accumulation
04 exact duplicate sequence -> idempotent suppression
05 sequence-ID collision -> refusal/no output mutation
06 malformed outer record -> refusal/no mutation
07 fewer than 3 units -> refusal/no mutation
08 more than 4 units -> refusal/no mutation
09 empty interior unit -> refusal/no mutation
10 empty batch -> no observations/no output overwrite
11 exact sequence capacity 4 -> pass
12 fifth unique 3-unit sequence -> sequence-capacity refusal/no mutation
13 nine raw lines -> input-bound refusal before scan/no mutation
14 four 4-unit sequences -> exact structural maximum 8 observations
15 dynamic UTF-8 source provenance preserved exactly
16 materially different dynamic sequence -> output bytes change
17 pure replay A in fresh namespace
18 pure replay B -> identical native stdout/output to case 17
```

## Current proof state

```text
LOCKED_SIGMAC_COMPILE=NOT_RUN
BYTECODE_PATH=$HOME/SIGMA/SIGMA_VNM_03_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1_PREFLIGHT/SIGMA_VNM_03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1.sigmab
BYTECODE_SHA256=UNKNOWN
TOTAL_VM_INVOCATIONS=0
INPUT_DYNAMIC=PLANNED_AFTER_COMPILE
OUTPUT_DEPENDS_ON_INPUT=NOT_PROVEN
NEGATIVE_TEST=NOT_RUN
PERSISTENT_STATE=NO
PERSISTENT_STATE_TEST=NA
RESTART_REPLAY_TEST=NOT_RUN
HOST_CONTEXT_EXTRACTION=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_UNIT_SELECTION=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_PAIR_SELECTION=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_NORMALIZATION=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_LEARNING=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_SEMANTIC_INTERPRETATION=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_SEMANTIC_SUBSTITUTION=NO_BY_SOURCE_AND_RUNNER_DESIGN
STEP_LIMIT_STATUS=NOT_PROVEN
PRODUCTION_STATE_MUTATED=NO
VM_RC=NOT_RUN
ADMISSION=NOT_RUN
```

## Explicit non-claims

```text
NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN
WORD_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_BOUNDARY_DETECTION=NOT_PROVEN
SEMANTIC_CONTEXT_EXTRACTION=NOT_PROVEN
SEMANTIC_EQUIVALENCE=NOT_PROVEN
WORD_MEANING=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
PRODUCTION_BINDING=NO
```

VNM-03 is a structural neighbor-context derivation lesson over explicit delimiter-defined units. It is not a tokenizer, parser or semantic context model.

## Exact next action

Pull the VNM-03 source/runner onto Oppo, verify exact source/runner hashes, then execute the complete locked-runtime 18-invocation preflight.

```text
NEXT_ACTION=PULL_AND_RUN_FULL_VNM03_LOCKED_RUNTIME_PREFLIGHT
```

Any compile/runtime/oracle failure remains evidence and must be repaired minimally without weakening this gate.
