# SURVIVAL MASTER AGENT INSTRUCTIONS

Applies to all work under `SURVIVAL_MASTER/` on branch `AIL_SIGMA`.

Before doing any Survival or Internet-autolearn work, read:

1. `/AGENTS.md`
2. `/00_SURVIVAL_MASTER_READ_FIRST.md`
3. `SURVIVAL_MASTER/CURRENT_HANDOFF.md`
4. `SURVIVAL_MASTER/REQUESTS/20260917_INTERNET_AUTO_BUNDLE_IMPLEMENTATION_REQUEST_R1.md`
5. `SURVIVAL_MASTER/REQUESTS/20260917_INTERNET_AUTO_BUNDLE_SUBMISSION_TEMPLATE_R1.md`
6. `SURVIVAL_MASTER/RUNBOOK/SURVIVAL_INTERNET_AUTOLEARN_RUNBOOK_R1.md`
7. `SURVIVAL_MASTER/SAMPLES/COMMANDS_R1.md`
8. `DOCS/SIGMA_LATEST_VERIFIED_RESULT.md`

Do not ask the human to restate project history already recorded there.

## Active candidate-work rule

If the task is to implement the Internet auto bundle, follow the active request exactly and publish only under:

`SURVIVAL_MASTER/CANDIDATES/INTERNET_AUTOLEARN_R1/`

The implementing window must stop after GitHub submission. It must not instruct the human to install/run the candidate. Only a later Survival Master review may issue `APPROVE_FOR_OPPO_PREFLIGHT_ONLY`.

## Hard invariants

```text
ONE_SIGMA_AIL=YES
ONE_WRITER=YES
NO_STATE_FORK=MANDATORY
DEFAULT_SESSION=READ_PLUS_ARTIFACT_WRITE
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO_FOR_SEMANTIC_VERDICT
SIGMA_NATIVE_VERDICT=MANDATORY
CANONICAL_MUTATION=EXPLICIT_ADMISSION_ONLY
```

Survival logic may supervise, restart, hash, verify checkpoints and dispatch an exact already-recorded worker mechanically. It may not choose SIGMA's lesson, query, source, website, resource, summary, truth state, learning batch, curriculum, next semantic action, or model update policy.

Internet logic must preserve:

```text
SIGMA_NATIVE_QUERY_GENERATION_OR_SELECTION=YES
SIGMA_NATIVE_SOURCE_FAMILY_SELECTION=YES
SIGMA_NATIVE_RESOURCE_SELECTION=YES
SIGMA_NATIVE_READING_AND_EVIDENCE_DECISION=YES
SIGMA_NATIVE_COMPACT_REPRESENTATION=YES_TARGET
HOST_NETWORK_TRANSPORT=MECHANICAL_ONLY
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
HOST_SUMMARY_WRITING=NO
HOST_SEMANTIC_FILTERING=NO
```

## Runtime truth

Oppo machine state and exact machine receipts outrank GitHub prose. GitHub is the continuity map.

Never manually mutate:

```text
.sigma_ail/BRAIN_HEAD
.sigma_ail/MODEL_GENERATION
canonical model/brain state
writer locks
```

Do not copy another pane's `SESSION_CODE`.

## Context-end requirement

Before your window/context ends after meaningful work, update the appropriate candidate `SUBMISSION.md` or Survival handoff with exact result, hashes, claim scope, failure/HOLD if any, and the next exact action. Update the runbook/command samples when procedures change.
