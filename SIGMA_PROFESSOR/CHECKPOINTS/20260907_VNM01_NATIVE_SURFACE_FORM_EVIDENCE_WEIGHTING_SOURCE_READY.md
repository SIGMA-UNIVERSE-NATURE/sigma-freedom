# VNM-01 — Native Surface-Form Evidence Weighting — SOURCE READY

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE READY / LOCKED-RUNTIME ADMISSION NOT YET RUN

## Governance read

- `/AGENTS.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_IMPORTANT_NATIVE_DNA_ARTIFACT_BUILD_ADMISSION_METHOD_V1.md`
- `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/20260905_V4PK2_NATIVE_WEIGHT_EVIDENCE_ADMISSION_PASS.md`
- `SIGMA_PROFESSOR/DIRECTIVES/TEACHER_GPT_VNM_NATIVE_VIETNAMESE_CAPABILITY_COURSE_V1.md`

## Capability contract

```text
CAPABILITY_ID=VNM-01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING
CAPABILITY_NAME=Native Vietnamese-bearing Surface-Form Evidence Weighting

WHAT_CAPABILITY_IS_SIGMA_BEING_TAUGHT=
Given an externally supplied bounded pair hypothesis over arbitrary UTF-8 surface forms and bounded observation records, classify structural evidence natively and persist a bounded association weight.

WHAT_MUST_SIGMA_COMPUTE_ITSELF=
SUPPORT/COMPETING/UNRELATED classification;
duplicate/collision handling;
support and competing counts;
WEIGHT_BEFORE;
PROPOSED_WEIGHT;
NATIVE_UPDATE_REASON;
commit eligibility;
WEIGHT_AFTER from persisted state.

WHAT_MAY_HOST_DO_MECHANICALLY=
Create isolated fixtures;
write exact input bytes;
invoke locked sigmac/VM;
hash exact artifacts;
copy identical replay state;
capture raw stdout/stderr;
run exact post-VM equality checks.

WHAT_RUNTIME_EVIDENCE_WILL_PROVE_THE_CAPABILITY=
Dynamic Vietnamese-bearing strings generated after compile;
weight increase under support evidence;
weight decrease under competing evidence;
no update for unrelated/duplicate input;
atomic refusal for malformed/collision/over-capacity/bound cases;
persistent effect across fresh VM invocations;
identical replay for identical input/prestate.

WHAT_RESULT_WOULD_FALSIFY_THE_CLAIM=
Fixed output despite material evidence change;
host-computed weight;
duplicate double-count;
collision mutation;
lost state after restart;
non-identical replay;
step-limit hit;
dynamic token leak in source/bytecode;
source/bytecode mutation during suite.

WHAT_DEPENDENCY_MUST_EXIST_FIRST=
Locked SIGMAC and VM identities plus already exercised mechanical string/file/list/map ABI.
No semantic-language dependency is claimed for VNM-01.
```

## Native source

```text
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_V1.sigma
SOURCE_COMMIT=c7cf0881fc2f8a500e92f929a6c7d44eafc4dcdb
SOURCE_GIT_BLOB=dbec0349b7b12a18e3f08b0d7fac5d60edcbf039
SOURCE_SHA256=638078331f21fccf392b6456f81a76713010a59b641026962bcaf28e2ac3814a
ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP
```

Static source audit performed before checkpoint:

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
ACTIVE_PYTHON_COGNITION=NO
HOST_LEARNING=NO
HOST_WEIGHT_UPDATE=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
```

## Locked-VM runner

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_PREFLIGHT.sh
RUNNER_COMMIT=336340beb380b8857d03208121108c579196d2b0
RUNNER_GIT_BLOB=0cb9909144c1a1684351fca5273645753d34b101
RUNNER_SHA256=b4456fbd4b60c94c3f45739c2d4e74593619867f1af83ac14da43e5b0f26dc2f
RUNNER_STATIC_BASH_SYNTAX=PASS
PLANNED_VM_INVOCATIONS=18
```

The runner:

1. equality-gates locked SIGMAC/VM/source hashes;
2. compiles before dynamic fixture generation;
3. freezes bytecode identity;
4. creates unseen Vietnamese-bearing strings only after compile;
5. checks the unseen token is absent from source/bytecode;
6. exercises positive, competing, unrelated, duplicate, collision, malformed, persistence, capacity, input-bound, and replay cases;
7. verifies source/bytecode remain unchanged;
8. admits only if every hard gate passes.

## Locked runtime

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Current proof state

```text
LOCKED_SIGMAC_COMPILE=NOT_RUN
BYTECODE_PATH=UNKNOWN_UNTIL_TERMUX_RUN
BYTECODE_SHA256=UNKNOWN
TOTAL_VM_INVOCATIONS=0
INPUT_DYNAMIC=PLANNED
OUTPUT_DEPENDS_ON_INPUT=NOT_PROVEN_UNTIL_RUN
NEGATIVE_TEST=NOT_RUN
PERSISTENT_STATE=YES_BY_DESIGN
PERSISTENT_STATE_TEST=NOT_RUN
RESTART_REPLAY_TEST=NOT_RUN
HOST_LEARNING=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_WEIGHT_UPDATE=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_SEMANTIC_INTERPRETATION=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_SEMANTIC_SUBSTITUTION=NO_BY_SOURCE_AND_RUNNER_DESIGN
STEP_LIMIT_STATUS=NOT_PROVEN
PRODUCTION_STATE_MUTATED=NO
VM_RC=NOT_RUN
ADMISSION=NOT_RUN
```

## Claim scope before runtime

```text
SOURCE_READY=YES
RUNTIME_CAPABILITY_PROVEN=NO
SURFACE_FORM_PAIR_GENERATION=NOT_PROVEN
SEMANTIC_EQUIVALENCE=NOT_PROVEN
DIACRITIC_EQUIVALENCE=NOT_PROVEN
WORD_MEANING=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

## Exact next action

From the Termux repo checkout on the Oppo/locked-runtime device:

```bash
cd "$HOME/SIGMA/sigma-freedom-write"
git checkout SIGMA_LIFE
git pull --ff-only
bash SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_PREFLIGHT.sh
```

Preserve the first compile/runtime result exactly. A compile or runtime failure is evidence and must be repaired minimally without weakening the 18-invocation gate.

```text
NEXT_DEPENDENCY_OR_CAPABILITY=
RUN_VNM_01_LOCKED_RUNTIME_ADMISSION_FIRST;
ONLY_AFTER_PASS_CONSIDER_VNM-02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION
```
