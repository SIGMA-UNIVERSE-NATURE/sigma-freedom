# 00 — SURVIVAL MASTER READ FIRST

Branch: `AIL_SIGMA`
Status: MANDATORY FOR SURVIVAL / INTERNET AUTOLEARN / MULTI-TEACHER LEARNING CONTINUATION
Date: 2026-09-17

If a chat/window/context ended and you need to continue current Survival, Internet-autolearn, or multi-teacher canonical-learning work, DO NOT rediscover the repository from scratch.

Read exactly:

1. `SURVIVAL_MASTER/CORRECTIONS/20260917_DURABLE_CANONICAL_LEARNER_ROLE_TAKEOVER_R1.md`
2. `SURVIVAL_MASTER/CORRECTIONS/20260917_OPPO_RUNTIME_AUTHORITY_NATIVE_LEARNING_FIX1.md`
3. `SURVIVAL_MASTER/CURRENT_HANDOFF.md`
4. `SURVIVAL_MASTER/DIRECTIVES/01_MULTI_TEACHER_CANONICAL_LEARNING_QUEUE_R1.md`
5. latest multi-teacher checkpoint under `SURVIVAL_MASTER/CHECKPOINTS/`
6. `SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/README_RUN.md`
7. `SURVIVAL_MASTER/REQUESTS/20260917_INTERNET_AUTO_BUNDLE_IMPLEMENTATION_REQUEST_R1.md`
8. `SURVIVAL_MASTER/REVIEWS/20260917_INTERNET_AUTOLEARN_R1_STATIC_REVIEW_HOLD.md`
9. `SURVIVAL_MASTER/RUNBOOK/SURVIVAL_INTERNET_AUTOLEARN_RUNBOOK_R1.md`
10. `SURVIVAL_MASTER/SAMPLES/COMMANDS_R1.md`
11. `DOCS/SIGMA_LATEST_VERIFIED_RESULT.md`
12. `/AGENTS.md` and its native-execution directives.

Then inspect only the live Oppo state needed for the next action.

## RUNTIME AUTHORITY — READ BEFORE EVERYTHING ELSE

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GITHUB_MUST_NOT_REPLACE_OPPO_BRAIN_HEAD=YES
GIT_PULL_REQUIRED_FOR_RUNTIME=NO
GIT_CHECKOUT_REQUIRED_FOR_RUNTIME=NO
RUNTIME_REPO_MUTATION_FOR_STAGING=NO
```

Current runtime truth comes from Oppo machine state, especially:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_ail/BRAIN_HEAD
$HOME/SIGMA/sigma_genesis1/.sigma_ail/MODEL_GENERATION
current Session R4 status
current learner lease / one-writer state
exact machine receipts
```

GitHub is continuity/source/provenance/review/transfer documentation only.

## CANONICAL LEARNER SURVIVAL — CURRENT REQUIRED CORRECTION

```text
SESSION_CODE=EPHEMERAL
CANONICAL_LEARNER_ROLE=DURABLE
CANONICAL_LEARNER_OWNER=REPLACEABLE
ONE_WRITER=YES
OLD_SESSION_CODE_REQUIRED_AFTER_TOTAL_WINDOW_DEATH=NO
```

The currently observed `session_learner_recover()` is same-session recovery only: it requires the learner lease owner to equal the requested SESSION_CODE. Therefore it does not solve recovery from total window death when the replacement shell receives a new session code.

Required target: after confirmed stale-owner death, a new session atomically takes over the durable learner role, increments a lease epoch/fence token, rereads current Oppo HEAD/model generation, reconciles any incomplete native commit from exact receipts, and resumes durable queue progress. Never manually delete the learner lease or copy the old SESSION_CODE into a new shell.

## LEARNING OWNERSHIP

```text
SIGMA_NATIVE_VM_IS_LEARNING_ENGINE=YES
SIGMA_NATIVE_LEARNING_OWNER=YES
BASH_LEARNING=NO
PYTHON_LEARNING=NO
HOST_LEARNING=NO
HOST_WEIGHT_UPDATE=NO
HOST_WEIGHT_MERGE=NO
HOST_ACCEPT_REJECT=NO
```

A Bash preflight/queue/runner may only perform mechanical work. Any weight-affecting learning result must bind exact native `.sigma` source + native bytecode and an exact native SIGMA decision receipt.

## ACTIVE MULTI-TEACHER CANONICAL LEARNING ARCHITECTURE

```text
MULTI_TEACHER_WINDOWS=YES
TEACHER_WINDOWS_CAN_PRODUCE_WEIGHT_CANDIDATES=YES
TEACHER_CANONICAL_WRITE=NO
CANONICAL_CANDIDATE_QUEUE=YES
ONE_CANONICAL_LEARNER=YES
CANONICAL_NATIVE_REPLAY_AND_DECISION=YES
CANONICAL_WEIGHT_UPGRADE=YES
ONE_CANONICAL_WRITER_AT_A_TIME=YES
CURRENT_OPPO_MODEL_NATIVE_REPLAY_REQUIRED=YES
STALE_PARENT_BLIND_APPLY=NO
HOST_WEIGHT_MERGE=NO
HOST_LEARNING=NO
```

Corrected framework source:

`SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/`

Do not grant multiple canonical learner leases. Teaching windows submit sealed native-bound candidates. The single canonical learner replays/re-evaluates each candidate against the current Oppo canonical model before native SIGMA may commit it.

Current proof ceiling:

```text
QUEUE_FIX1_SOURCE_READY=YES
OPPO_PREFLIGHT=NOT_RUN_AFTER_FIX1
DEAD_OWNER_NEW_SESSION_TAKEOVER=NOT_IMPLEMENTED_IN_SHOWN_COORDINATOR_RECOVER
LEASE_EPOCH_FENCING=NOT_PROVEN
MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN_UNTIL_DEVICE_TEST
```

## INTERNET AUTO BUNDLE STATUS

```text
REQUEST=SIGMA_SURVIVAL_INTERNET_AUTOLEARN_R1
CANDIDATE_SUBMITTED=YES
STATIC_REVIEW=HOLD_NEEDS_FIX
APPROVE_FOR_OPPO_PREFLIGHT_ONLY=NO
DO_NOT_INSTALL=YES
DO_NOT_RUN_OPPO=YES
```

Authoritative review:

`SURVIVAL_MASTER/REVIEWS/20260917_INTERNET_AUTOLEARN_R1_STATIC_REVIEW_HOLD.md`

## CORE LOCK

```text
ONE_SIGMA_AIL=YES
ONE_WRITER=YES
NO_STATE_FORK=MANDATORY
HOST_COGNITION=NO
SIGMA_NATIVE_VERDICT=MANDATORY
CANONICAL_MUTATION=EXPLICIT_ADMISSION_ONLY
```

Current headline evidence:

```text
AIL_LEDGER_THROUGH=AIL-021
200_STORY_REAL_INTERNET_ACQUISITION=PASS_IN_EXACT_REHASHED_200_ITEM_SCOPE
200_STORY_NATIVE_SOURCE_SELECTION=PASS_IN_EXACT_REHASHED_200_ITEM_SCOPE
200_STORY_NATIVE_FULL_INPUT_CONSUMPTION=PASS_IN_EXACT_REHASHED_200_ITEM_SCOPE
200_STORY_OUTPUT_MODE=NATIVE_EXTRACTIVE_THREE_SPAN_NARRATIVE_DIGEST
SEMANTIC_STORY_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
G6_PROMOTION=NO
G3_SELF_LEARNED_SURFACE_R2=HOLD_LEARN_COMPILE_FAILED
WEBTOOLS_R2_ARTIFACT_INTEGRITY=PASS
WEBTOOLS_R2_RUNTIME_ADMISSION=NOT_RUN
ANDROID_WHOLE_TERMUX_PROCESS_GROUP_SURVIVAL=NOT_PROVEN
```

Main targets:

```text
SURVIVAL:
Android/Termux/tmux may die, but exact unfinished SIGMA work resumes from a valid committed checkpoint with no duplicate worker, no duplicate commit, one writer and no state fork.

INTERNET AUTOLEARN:
Native SIGMA chooses gap/query/source family/website/resource, reads exact Internet data, evaluates it, creates its own compact representation, decides research/learning next actions, while host performs only mechanical network/file/hash/process work.

MULTI-TEACHER LEARNING:
Many windows may teach in parallel, but all canonical model changes are serialized through one canonical learner after native replay/re-evaluation against the latest Oppo generation. The canonical learner role survives window death and may be atomically transferred to a new session only after stale-owner proof.
```

Do not ask the human to restate the full project if these files contain the answer.
