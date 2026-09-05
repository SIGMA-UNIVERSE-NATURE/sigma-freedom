# V4-C4 R1 — Local-First Curriculum Stage Controller — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / PREFLIGHT_NOT_RUN / PRODUCTION_BINDING_NO

## Architecture correction

The current V4 continuous loop only sees the configured V2.4 `raw` corpus. Repository-local stored/taught files are not automatically visible to C2R2.

Existing Internet capability is already available and should be reused rather than reinvented:

- V2.4 native source emits its own `FETCH_REQUEST` from recurrent-support gap state;
- V2.4 host runner performs query transport/protocol decode only and stores returned Wikipedia contexts in production `raw`;
- V5-K2 separately passed live Wikipedia EN/VI adapter/provenance admission in its exact tested scope.

The corrected next architecture is therefore LOCAL-FIRST, then existing native external feed.

## New native source

```text
SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_V4_LOCAL_FIRST_CURRICULUM_STAGE_CONTROLLER_V4C4R1.sigma
SOURCE_GIT_BLOB=9c55b842b321feba5d755ef7021ba5a3067ff6e1
SOURCE_CREATE_COMMIT=7b7e84513ca49dcc1f385b41b9529705a3262966
SOURCE_SHA256=NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX
BYTECODE_SHA256=NOT_RUN
```

## Preflight runner

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C4R1_LOCAL_FIRST_CURRICULUM_STAGE_PREFLIGHT.sh
RUNNER_CREATE_COMMIT=1a78fcea2755c97a9929f597789925493f74adc3
RUNNER_SHA256=NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX
```

## Design

```text
DESIGN_PATH=SIGMA_PROFESSOR/DESIGN/SIGMA_V4C4_LOCAL_FIRST_STORED_TEACHING_TO_EXISTING_NATIVE_EXTERNAL_FEED_V1.md
DESIGN_COMMIT=dcf650bd4c11138bcf62b815c0070f7d55aaff32
```

## Intended preflight scope

The exact preflight must test the same native source against materially different directory/state fixtures:

```text
CASE_A local incomplete -> LOCAL
CASE_B local operational pass complete -> EXTERNAL
CASE_C new unfinished local data while EXTERNAL -> LOCAL
CASE_D requested switch with active context -> wait for safe boundary
CASE_E local HOLD -> local recovery action, no external bypass
CASE_F malformed mode -> native refusal
CASE_G empty local corpus -> native refusal
```

Dynamic fixture identifiers must not appear in source or bytecode.

The source and bytecode must contain no forced semantic verdict token such as teacher-supplied `UNDERSTOOD`, `NOT_UNDERSTOOD`, or `NOT_PROVEN` self-assessment.

## Native/host boundary

```text
NATIVE_SIGMA_SELECTS_LOCAL_OR_EXTERNAL_MODE=YES_BY_DESIGN_NOT_YET_RUNTIME_PROVEN
NATIVE_SIGMA_WRITES_C2R2_RAW_STATE_BINDING=YES_BY_DESIGN_NOT_YET_RUNTIME_PROVEN
HOST_STAGE_DECISION=NO
HOST_CURRICULUM_PRIORITY=NO
HOST_LEARNING=NO
HOST_GAP_DETECTION=NO
HOST_RESEARCH_GOAL_SELECTION=NO
HOST_SEMANTIC_INTERPRETATION=NO
BASH_LEARNING=NO
GPT_AS_SIGMA_COGNITION=NO
```

The future local stager may only enumerate/copy/hash exact eligible file bytes and preserve path/content provenance. It may not rank topics or choose lessons.

Mechanical/security exclusions remain mandatory for credentials, keys, private/runtime transient state, binary executables, and repository `RESULTS/**`; `DO_NOT_LOAD_RESULTS=YES` remains binding.

## Claim boundary

`LOCAL_OPERATIONAL_PASS_COMPLETE` is an operational C2R2/B4R2 processing condition only.

It must not be relabeled as semantic mastery or understanding.

```text
LOCAL_SEMANTIC_MASTERY=NOT_CLAIMED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
AUTONOMOUS_LOCAL_TO_EXTERNAL_V4_CONTINUOUS_INTEGRATION=NOT_YET_PROVEN
V4C4_PREFLIGHT=NOT_RUN
V4_PRODUCTION_PROMOTION_ALLOWED=NO
PRODUCTION_V2_4_KEEP_RUNNING=YES
```

## Next exact action

Run the isolated V4-C4 R1 preflight on the locked Termux runtime. Preserve the first failure or final PASS. Only after PASS may a new versioned continuous V4 runner bind mechanical local corpus staging to this native stage controller and then to the existing V2.4 external feed.
