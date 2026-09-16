# OPPO NO-GIT STAGING — SURVIVAL MASTER R1

Date: 2026-09-17
Purpose: stage reviewed Survival/queue tool bytes on Oppo without changing the live Oppo repository checkout or canonical runtime authority.

## Hard rule

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GIT_PULL_FOR_RUNTIME_STAGING=NO
GIT_CHECKOUT_FOR_RUNTIME_STAGING=NO
GIT_RESET_FOR_RUNTIME_STAGING=NO
BASH_LEARNING=NO
```

GitHub is only the source/review/provenance location. A reviewed tool should be transferred as an exact small bundle or exact files, then verified in a neutral staging directory.

## Preferred transfer object

A future packaging window should build exactly:

```text
SIGMA_MULTI_TEACHER_CANONICAL_QUEUE_R1_FIX1.tgz
```

from the reviewed corrected source tree:

```text
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/
```

The bundle must include `MANIFEST.sha256` covering every staged file and publish its bundle SHA256 in the handoff/checkpoint.

Packaging on another machine/window does not authorize runtime use. Oppo verifies the exact bundle before preflight.

## Oppo staging pattern

Assume the exact reviewed bundle has already been placed at:

```text
/storage/emulated/0/Download/SIGMA_MULTI_TEACHER_CANONICAL_QUEUE_R1_FIX1.tgz
```

In the existing canonical learner shell, first inspect the current session:

```bash
source "$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
sigma-session status
```

Use the exact current `ARTIFACT_ROOT` from that output. Do not invent or copy another session code.

Mechanical staging example:

```bash
BUNDLE=/storage/emulated/0/Download/SIGMA_MULTI_TEACHER_CANONICAL_QUEUE_R1_FIX1.tgz
ARTIFACT_ROOT="$(sigma-session status | awk -F= '$1=="ARTIFACT_ROOT"{print substr($0,15); exit}')"
STAGE="$ARTIFACT_ROOT/tools/MULTI_TEACHER_CANONICAL_QUEUE_R1_FIX1"
mkdir -p "$STAGE"
tar -xzf "$BUNDLE" -C "$STAGE" --strip-components=1
cd "$STAGE"
sha256sum -c MANIFEST.sha256
```

The commands above only copy/verify bytes. They do not learn or update weights.

Then run the mechanical preflight from the staged tool copy:

```bash
bash verify/static_preflight.sh
```

Expected meaning:

```text
STATIC_PREFLIGHT_IS_LEARNING=NO
BASH_LEARNING=NO
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
```

Do not start `canonical/daemon.sh` until one single candidate preflight and one native decision receipt path have been proven on-device.

## Never do this merely to stage the queue

```text
git pull
git checkout AIL_SIGMA
git reset --hard <github-commit>
```

Those operations alter repository state and are not needed for runtime staging.