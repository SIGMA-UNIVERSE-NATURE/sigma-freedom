# ONE SIGMA.AIL SIMPLE SESSION WORKFLOW R1 — READ BEFORE WORK

Status: TESTED / ACTIVE WORKFLOW

This is the mandatory tmux/window workflow for ONE SIGMA.AIL after the Simple Session R1 cutover.

## Why this exists

Every tmux window/worker must tell ONE SIGMA.AIL what it is doing before work begins. The purpose is coordination and provenance: SIGMA can see all active work, assign one session identity, and keep canonical mutation separate from ordinary artifact creation.

The old tmux Front Door / Broker / profile / `sigma-open` workflow is obsolete and must not be used for new work.

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

## Tested evidence before publication

Simple Session R1 self-test was executed successfully before this workflow was published:

```text
ONE_SIGMA_AIL_SIMPLE_SESSION_R1_SELFTEST=PASS
DEFAULT_SESSION=READ_PLUS_ARTIFACT_WRITE
OLD_TMUX_GATE_ACTIVE=NO
CANONICAL_HEAD_UNCHANGED=YES
CANONICAL_MODEL_GENERATION_UNCHANGED=YES
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
```

A live Termux session also returned the expected contract (`SESSION=GRANTED`, `ACCESS=READ_PLUS_ARTIFACT_WRITE`, `CANONICAL_MUTATION=REQUIRES_EXPLICIT_ADMISSION`).

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