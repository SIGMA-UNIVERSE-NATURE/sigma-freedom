# V2.8R.1 REAL SURVEY -> CURRICULUM BRIDGE — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Dependency

V2.8P.1 persistent curriculum priority passed all QA gates on locked runtime.

Checkpoint commit:
`5e375d2ffa210852a042d833f061b6cc6c969ecf`

## Native bridge

Source:
`SIGMA_PROFESSOR/artifacts/SIGMA_REAL_SURVEY_CURRICULUM_BRIDGE_V2_8R1.sigma`

SOURCE_SHA256:
`8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`

Source commit:
`bfee5e3ddb8a279b76e8bb97cc4c3be8a96be79d`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V28R1_REAL_SURVEY_CURRICULUM_BRIDGE_PREFLIGHT.sh`

RUNNER_SHA256:
`338080383729e05834401373e172057f3627cdebcbe81268d419204eeb5ebc32`

Runner commit:
`dba2a97a4df6bad8d61e92ac486352d251976621`

Static audit:
- H_CALL_ARITY_AUDIT=PASS
- NATIVE_NOT_EQUAL_DEPENDENCY=NONE
- STR_STARTS_DEPENDENCY=NONE
- DIRECT_STR_DEPENDENCY=NONE
- runner bash -n RC=0

## Real input

The bridge reads the actual admitted V2.5B.2 survey state directly:
`.sigma_exec/SIGMA_V25B2_DOCUMENT_SURVEY.memory`

Expected committed documents: 56.

Host does NOT create lessons or work profiles.

## Native structural frontier policy

The real survey does not persist honest AGE or UNRESOLVED fields. The bridge therefore refuses to fabricate them.

It uses only available real structural evidence:
1. evidence-empty profile first;
2. then higher exact BEST_LOCAL_RELATION support across distinct documents;
3. exact tie -> first encounter.

This is structural scheduling only, not semantic importance.

## Admission tests prepared

- actual 56-document survey input;
- fresh VM phase 2 uses prior committed dispatch and must choose a different work item;
- deterministic replay from empty bridge state;
- partial/uncommitted dispatch record ignored;
- state limit refusal before mutation;
- survey limit refusal before mutation;
- real survey SHA unchanged.

Bounds:
- MAX_SURVEY_SPLIT_LINES=65
- MAX_STATE_SPLIT_LINES=65

## Claim truth before device run

COMPILE_PASS=NOT_PROVEN
RUNTIME_PASS=NOT_PROVEN
BYTECODE_SHA256=UNKNOWN
ADMISSION=NOT_PROVEN

HOST_WORK_PROFILE_GENERATION=NO
HOST_CURRICULUM_PRIORITY=NO
HOST_LESSON_SELECTION=NO
HOST_LEARNING=NO
SEMANTIC_IMPORTANCE=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN

NEXT_ACTION=RUN_V28R1_ON_LOCKED_DEVICE
