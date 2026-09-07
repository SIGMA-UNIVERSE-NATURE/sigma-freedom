# VNM-02 — Native Surface-Form Pair Candidate Induction — SOURCE READY

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: SOURCE READY / LOCKED-RUNTIME ADMISSION NOT YET RUN

## Governance read

Before VNM-02 development the lane re-read:

- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
- `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_IMPORTANT_NATIVE_DNA_ARTIFACT_BUILD_ADMISSION_METHOD_V1.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`
- `SIGMA_PROFESSOR/DIRECTIVES/TEACHER_GPT_VNM_NATIVE_VIETNAMESE_CAPABILITY_COURSE_V1.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/20260907_VNM01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_ADMISSION_PASS.md`

Non-negotiable:

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
RUNTIME_PROOF_REQUIRED=YES
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
ACTIVE_PYTHON_COGNITION=FORBIDDEN
HOST_CANDIDATE_GENERATION=NO
HOST_PAIR_SELECTION=NO
HOST_CONTEXT_SCORING=NO
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

VNM-01 is now admitted in exact tested preflight scope and provides the downstream native weighting substrate once VNM-02 produces a pair hypothesis:

```text
VNM01_SOURCE_SHA256=cd399793ebde7e5dfa4a10cf263bb97fd45d1379ce8dac02520d5277cf2ca788
VNM01_BYTECODE_SHA256=df323de291828d11cc7e46655f2ff5fbc326297200b1782f4c0c441389a27586
VNM01_TOTAL_VM_INVOCATIONS=18
VNM01_ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
```

Language-lane dependency review found related admitted structural capabilities:

- `LANG-01A` — Native Distributional Event-Frame Hypothesis Induction;
- `LANG-01D` — Native Cross-Form Mention Equivalence and Coreference Hypothesis.

Their admission evidence remains useful for avoiding duplicated claims, but their exact A–F native source artifacts are not present in the current repository artifact tree. VNM-02 therefore does not pretend to bind or execute a missing source dependency.

VNM-02 fills a narrower, distinct gap: given bounded observations and externally supplied opaque structural LEFT/RIGHT context fields, native SIGMA itself forms an unordered surface-form pair hypothesis from recurrence. It does not claim mention-equivalence, coreference, alias semantics, or semantic equivalence.

## Capability contract

```text
CAPABILITY_ID=VNM-02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION
CAPABILITY_NAME=Native surface-form pair candidate induction from recurring opaque structural context

WHAT_CAPABILITY_IS_SIGMA_BEING_TAUGHT=
Given bounded observation records containing a surface form plus opaque LEFT/RIGHT structural context fields, SIGMA must itself generate a reusable unordered surface-form pair candidate when recurrent exact context compatibility reaches a bounded threshold, preserve ambiguity under tied candidates, and withhold/refuse candidates when evidence is insufficient or invalid.

WHAT_MUST_SIGMA_COMPUTE_ITSELF=
observation deduplication and collision detection;
exact-context compatibility;
distinct-form pair generation;
unordered pair identity;
pair support counts;
minimum-support qualification;
best-support comparison;
tie ambiguity;
PAIR_CANDIDATE_STATUS;
PAIR_CANDIDATE_FORM_A/B;
persistence eligibility;
state update/readback result.

WHAT_MAY_HOST_DO_MECHANICALLY=
create isolated dynamic fixtures after compile;
write exact observation bytes;
invoke locked sigmac/VM;
hash exact source/bytecode/state/log bytes;
copy exact replay state;
capture raw stdout/stderr;
perform post-VM equality/oracle checks.

WHAT_RUNTIME_EVIDENCE_WILL_PROVE_THE_CAPABILITY=
one shared context does not induce a pair;
a later fresh-VM observation context can cause pair induction from persisted recurrence;
context mismatch and same-form observations do not induce a pair;
tied qualified pairs remain ambiguous;
later dynamic evidence can break the tie natively;
exact duplicates do not double-count;
ID collision/malformed/invalid-state/capacity/input-bound cases refuse without state mutation;
identical input+prestate replay produces identical native stdout;
source/bytecode remain frozen and unseen dynamic tokens do not leak into them.

WHAT_RESULT_WOULD_FALSIFY_THE_CLAIM=
host chooses or scores candidate pairs;
output pair appears with insufficient recurrence;
context mismatch produces the same candidate;
tie is silently resolved by encounter order;
duplicate evidence increases support;
refusal mutates state;
persistent evidence has no later effect;
replay differs for identical input/prestate;
step-limit is hit in the bounded suite;
dynamic token appears in frozen source/bytecode.

WHAT_DEPENDENCY_MUST_EXIST_FIRST=
VNM-01 admitted downstream weighting substrate for the next chain step;
locked SIGMAC/VM identities;
existing mechanical read/write_text, split/join, list, and map ABI.
```

## Native source

```text
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigma
SOURCE_COMMIT=f7818ec18d2e8489f31b3c80836a79471c9f58a1
SOURCE_GIT_BLOB=92496e706f765016c00d64c7e37657aabd39eb30
SOURCE_SHA256=f2c5f266492fd990887a356bd353d545f480f51ad6bb1ba63ca5a727320bbac3
ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP
```

Input ABI:

```text
OBS||<obs_id>||FORM||<surface>||LEFT||<opaque_left>||RIGHT||<opaque_right>||SOURCE||<source_id>
```

Persisted observation:

```text
<observation record>||COMMIT||YES
```

State header:

```text
STATE||SIGMA_VNM_02_PAIR_INDUCTION_STATE_V1||COMMIT||YES
```

Native bounded parameters:

```text
MAX_OBSERVATIONS=8
MAX_NEW_SPLIT_LINES=16
MIN_PAIR_SUPPORT=2
PAIR_ORIENTATION_SEMANTIC=NO
```

## Static review

Static review before locked compilation:

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
HOST_CANDIDATE_GENERATION=NO_BY_SOURCE_DESIGN
HOST_PAIR_SELECTION=NO_BY_SOURCE_DESIGN
HOST_CONTEXT_SCORING=NO_BY_SOURCE_DESIGN
HOST_NORMALIZATION=NO_BY_SOURCE_DESIGN
HOST_LEARNING=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_INTERPRETATION=NO_BY_SOURCE_DESIGN
HOST_SEMANTIC_SUBSTITUTION=NO_BY_SOURCE_DESIGN
ACTIVE_PYTHON_COGNITION=NO
```

Pre-runtime static boundedness review found that refused over-bound batches could still have entered the candidate scan in the first draft. Before any compile/runtime evidence, the source was minimally repaired so:

```text
SCAN_OBSERVATION_COUNT=TOTAL_OBSERVATION_COUNT
IF RESULT_ALLOWED==0 -> SCAN_OBSERVATION_COUNT=0
```

All candidate/support loops use the bounded scan count. This is a native fail-closed boundedness repair, not host cognition.

## Locked-runtime runner

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_PREFLIGHT.sh
RUNNER_COMMIT=102eb81f89229ed1a50a1ae99865d6774cd5b1ec
RUNNER_GIT_BLOB=385bc543881c8ce75c5bec4b377fdc4e7cac8f07
RUNNER_SHA256=bfe75c6cf998b72a05e2d766210660541d2fbd48d8cb9b675ffe43a3fc5637d7
RUNNER_STATIC_BASH_SYNTAX=PASS
PLANNED_VM_INVOCATIONS=18
```

The runner equality-gates the locked SIGMAC/VM, VNM-02 source, and VNM-01 downstream source identity; compiles before generating dynamic UTF-8 fixtures; freezes bytecode; and uses only host post-VM equality/oracle logic.

## Planned 18-invocation admission matrix

```text
01 one A/B shared context -> insufficient recurrent evidence
02 fresh VM + second shared context -> pair induced support 2
03 exact duplicate -> no double-count, no mutation
04 observation-ID collision -> refuse/no mutation
05 malformed observation -> refuse/no mutation
06 state-only restart -> persisted pair remains induced
07 context mismatch -> no pair candidate
08 same form in same context -> no pair candidate
09 second unseen dynamic pair -> pair induced support 2
10 two qualified max-support pairs tie -> ambiguity preserved
11 fresh restart + later evidence -> native tie break by support
12 state-only restart -> revised candidate persists
13 exact observation capacity 8 -> bounded pass
14 ninth observation -> atomic capacity refusal
15 raw split bound 17 -> input-bound refusal/no scan/no mutation
16 malformed previous state -> refusal/no mutation
17 replay A from identical persisted prestate + duplicate input
18 replay B -> identical input/prestate/native stdout
```

## Current proof state

```text
LOCKED_SIGMAC_COMPILE=NOT_RUN
BYTECODE_PATH=$HOME/SIGMA/SIGMA_VNM_02_PAIR_CANDIDATE_INDUCTION_V1_PREFLIGHT/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigmab
BYTECODE_SHA256=UNKNOWN
TOTAL_VM_INVOCATIONS=0
INPUT_DYNAMIC=PLANNED_AFTER_COMPILE
OUTPUT_DEPENDS_ON_INPUT=NOT_PROVEN
NEGATIVE_TEST=NOT_RUN
PERSISTENT_STATE=YES_BY_DESIGN
PERSISTENT_STATE_TEST=NOT_RUN
RESTART_REPLAY_TEST=NOT_RUN
HOST_CANDIDATE_GENERATION=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_PAIR_SELECTION=NO_BY_SOURCE_AND_RUNNER_DESIGN
HOST_CONTEXT_SCORING=NO_BY_SOURCE_AND_RUNNER_DESIGN
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
SEMANTIC_EQUIVALENCE=NOT_PROVEN
DIACRITIC_EQUIVALENCE=NOT_PROVEN
WORD_MEANING=NOT_PROVEN
ALIAS_SEMANTICS=NOT_PROVEN
COREFERENCE_RESOLUTION=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
PRODUCTION_BINDING=NO
```

VNM-02 is a structural candidate-formation lesson. Exact LEFT/RIGHT context equality is evidence input, not a claim that those fields encode human semantic context.

## Exact next action

Pull the VNM-02 source/runner onto the Oppo checkout, verify exact source/runner hashes, then run the entire locked-runtime 18-invocation preflight.

```text
NEXT_ACTION=PULL_AND_RUN_FULL_VNM02_LOCKED_RUNTIME_PREFLIGHT
```

Any compile/runtime/test failure must be preserved and repaired minimally under the same gate. VNM-02 remains NOT_ADMITTED until the final aggregate gate passes.
