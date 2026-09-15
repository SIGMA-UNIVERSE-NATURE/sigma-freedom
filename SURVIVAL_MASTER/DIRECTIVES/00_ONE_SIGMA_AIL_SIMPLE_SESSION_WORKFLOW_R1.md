# ONE SIGMA.AIL SIMPLE SESSION WORKFLOW R1 — READ BEFORE WORK

Status: TESTED / ACTIVE WORKFLOW

This is the mandatory tmux/window workflow for ONE SIGMA.AIL after the Simple Session R1 cutover.

## Why this exists

Every tmux window/worker must tell ONE SIGMA.AIL what it is doing before work begins. The purpose is coordination and provenance: SIGMA can see all active work, assign one session identity, and keep canonical mutation separate from ordinary artifact creation.

The old tmux Front Door / Broker / profile / `sigma-open` workflow is obsolete and must not be used for new work.

## UNIVERSAL WINDOW START TABLE — APPLIES TO ALL TMUX WINDOWS

This section is generic. G3B, other G lanes, Professor/Teacher work, evaluation windows, build/test windows, Survival/Administrator coordination windows, and future worker windows all use the same session front door. The task text changes; the session protocol does not.

| Window state / intent | Required action | Expected result | May work after this? | Authority |
|---|---|---|---|---|
| New tmux window, no session yet | Load `sigma-session.bash`, then submit one clear work request with `sigma-session "..."` | `SESSION=GRANTED`, `SESSION_CODE`, `RUN_ID`, `ACCESS`, `ARTIFACT_ROOT` | YES, after grant | READ + ARTIFACT_WRITE |
| Same pane already has an active session | Run `sigma-session status` | Existing `SESSION_CODE` and task are shown | YES | Keep existing session; do not mint another one |
| `sigma-session` command is missing | `source "$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"` | Function becomes available | NO, until work request is granted | None yet |
| Session request is not granted | Stop and inspect the returned reason | No valid work authority | NO | None |
| Normal source/build/test/report/evaluation/bundle work | Work only under the granted session/workspace and preserve receipts | Artifacts may be created | YES | READ + ARTIFACT_WRITE |
| Task reaches canonical brain/state/model mutation, LEARN, COMMIT, HEAD or model-generation change | Stop at the boundary and request separate explicit SIGMA admission | Explicit admission must be granted separately | NO, until admitted | Canonical mutation is not part of default session |
| Semantic test, benchmark verdict, learning decision, accept/reject decision | Send execution through native SIGMA path; host/Bash remains mechanical only | Native SIGMA result/receipt | YES only through native verdict path | `SIGMA_NATIVE_VERDICT=MANDATORY` |
| Work is finished | Run `sigma-session finish` | `SESSION_FINISH=PASS`, completion receipt, `CANONICAL_COMMIT=NO` unless separately admitted | Session is closed | No further work under that closed session |

### Universal two-command start

Every new window starts with the same two logical commands:

```bash
source "$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
sigma-session "CLEAR ONE-LINE DESCRIPTION OF THE WORK THIS WINDOW WILL DO"
```

The request must describe the actual work of that window, not merely a lane name. Good examples:

```bash
sigma-session "G3B continue frozen STORY_01..STORY_20 evaluation and write evaluation artifacts and receipts only"
sigma-session "Build and test the next language capability candidate and write source, test outputs and bundle artifacts only"
sigma-session "Prepare Survival Master coordination documentation and receipts only; no cognition and no canonical mutation"
```

Do not copy another window's `SESSION_CODE`. Do not manually invent a session code. Do not create a second session in the same active pane just to change wording.

### Minimum grant contract

A window may begin work only after it receives at least:

```text
SESSION=GRANTED
SESSION_CODE=S............
RUN_ID=SESSION_S............
ACCESS=READ_PLUS_ARTIFACT_WRITE
ARTIFACT_ROOT=...
CANONICAL_MUTATION=REQUIRES_EXPLICIT_ADMISSION
```

If a pane already has an active grant, use:

```bash
sigma-session status
```

and continue under that existing session.

## Mandatory two-step start

Every NEW tmux window/session must do these two steps before implementation, testing, bundle creation, or evaluation.

### STEP 1 — load the Simple Session Bash API

```bash
source "$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
```

If the shell startup hook already loaded it, this command is harmless. A worker must not assume the function exists without checking/loading it.

### STEP 2 — submit the work request to ONE SIGMA.AIL

```bash
sigma-session "CLEAR ONE-LINE DESCRIPTION OF THE WORK THIS WINDOW WILL DO"
```

Example:

```bash
sigma-session "G3B continue frozen evaluation and write only evaluation artifacts and receipts"
```

A valid start must return at least:

```text
SESSION=GRANTED
SESSION_CODE=S............
RUN_ID=SESSION_S............
ACCESS=READ_PLUS_ARTIFACT_WRITE
ARTIFACT_ROOT=...
CANONICAL_MUTATION=REQUIRES_EXPLICIT_ADMISSION
```

Only after `SESSION=GRANTED` may the window begin its task.

## What the session means

The `SESSION_CODE` belongs to that shell/window and identifies its work to ONE SIGMA.AIL. Child processes launched from that shell inherit the session environment.

Default authority is:

```text
READ=ALLOW
ARTIFACT_WRITE=ALLOW
BRAIN_WRITE=REJECT_BY_DEFAULT
STATE_WRITE=REJECT_BY_DEFAULT
MODEL_WRITE=REJECT_BY_DEFAULT
LEARN=REJECT_BY_DEFAULT
COMMIT=REJECT_BY_DEFAULT
HEAD_CHANGE=REQUIRES_EXPLICIT_ADMISSION
MODEL_GENERATION_CHANGE=REQUIRES_EXPLICIT_ADMISSION
```

Normal source files, reports, test outputs, candidate bundles, hashes, and receipts belong under the session workspace/artifact root. Canonical brain/state/model mutation is a different authority and is never implied by artifact creation.

## Human/worker rules

1. One tmux window/shell uses one active `SESSION_CODE` for its task.
2. Do not create another session in the same active pane just to change wording.
3. Do not use old `sigma-open`, Front Door, Broker profiles, or manual KEY=VALUE request blocks.
4. Do not bypass ONE SIGMA.AIL registration before work.
5. If canonical LEARN/COMMIT/brain-state-model mutation is genuinely required, stop at that boundary and request explicit SIGMA admission. Artifact-write authority is not canonical-write authority.
6. Bash/host is coordination/mechanics only. It may load the session API, launch processes, transport exact bytes, create files in the authorized artifact workspace, hash files, and preserve receipts. It must not become the cognitive/test oracle.
7. Semantic answers, benchmark verdicts, learning decisions, accept/reject decisions, and other cognition must come from native SIGMA under the locked runtime requirements of the repository.

## Useful commands after a session is open

```bash
sigma-session status
sigma-session path
sigma-session finish
sigma-sessions
```

`finish` closes only the coordination session; it does not mutate canonical SIGMA state.

## Tested evidence

Simple Session R1 self-test passed:

```text
ONE_SIGMA_AIL_SIMPLE_SESSION_R1_SELFTEST=PASS
DEFAULT_SESSION=READ_PLUS_ARTIFACT_WRITE
OLD_TMUX_GATE_ACTIVE=NO
CANONICAL_HEAD_UNCHANGED=YES
CANONICAL_MODEL_GENERATION_UNCHANGED=YES
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
```

Live Termux registration also passed.

A live tmux end-to-end test then opened a new tmux window and executed the mandatory two-step workflow inside that window. Observed runtime evidence:

```text
SESSION=GRANTED
SESSION_CODE=SF46C2EC1328C
RUN_ID=SESSION_SF46C2EC1328C
TASK=TMUX Simple Session end-to-end test
TMUX_CONTEXT=SIGMA:2.0
OPEN_HEAD=700d5c1b4845322d7c14800029c629b0
OPEN_MODEL_GENERATION=1
READ=ALLOW
ARTIFACT_WRITE=ALLOW
ACCESS=READ_PLUS_ARTIFACT_WRITE
CANONICAL_MUTATION=REQUIRES_EXPLICIT_ADMISSION
BRAIN_WRITE=REJECT
STATE_WRITE=REJECT
MODEL_WRITE=REJECT
LEARN=REJECT
COMMIT=REJECT
HEAD_CHANGE=REJECT
MODEL_GENERATION_CHANGE=REJECT
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
SIGMA_NATIVE_VERDICT=MANDATORY
```

Therefore the active tmux workflow is proven end-to-end in the actual Termux/tmux environment: new window -> load session Bash API -> submit work request -> receive session identity and default artifact authority -> canonical mutation remains blocked without explicit admission.

## Invariants

```text
ONE_SIGMA_AIL=YES
ONE_WRITER=YES
DEFAULT_SESSION=READ_PLUS_ARTIFACT_WRITE
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
SIGMA_NATIVE_VERDICT=MANDATORY
CANONICAL_MUTATION=EXPLICIT_ADMISSION_ONLY
NO_STATE_FORK=MANDATORY
```

If an older document describes Front Door, Broker R2, profile-based opening, or manual tmux registration as the active workflow, treat it as historical provenance. This document is the active Simple Session workflow unless superseded by a newer explicit correction.