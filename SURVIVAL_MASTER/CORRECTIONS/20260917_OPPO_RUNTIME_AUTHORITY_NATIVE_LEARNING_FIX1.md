# SURVIVAL MASTER CORRECTION — OPPO RUNTIME AUTHORITY + NATIVE LEARNING FIX1

Date: 2026-09-17 (Asia/Ho_Chi_Minh)
Branch: `AIL_SIGMA`
Status: ACTIVE CORRECTION / SUPERSEDES ANY CONTRARY STAGING OR QUEUE INSTRUCTION

## Runtime authority

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
RUNTIME_BRAIN_HEAD_SOURCE=$HOME/SIGMA/sigma_genesis1/.sigma_ail/BRAIN_HEAD
RUNTIME_MODEL_GENERATION_SOURCE=$HOME/SIGMA/sigma_genesis1/.sigma_ail/MODEL_GENERATION
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GITHUB_BRANCH_HEAD_MUST_NOT_REPLACE_OPPO_BRAIN_HEAD=YES
GIT_PULL_REQUIRED_FOR_RUNTIME=NO
GIT_CHECKOUT_REQUIRED_FOR_RUNTIME=NO
RUNTIME_REPO_MUTATION_FOR_STAGING=NO
```

GitHub stores source, review, provenance, requirements, and transfer artifacts. It is not allowed to redefine the live canonical SIGMA state on Oppo.

When GitHub and Oppo differ, inspect Oppo first. The live Oppo `BRAIN_HEAD`, `MODEL_GENERATION`, learner lease, writer lock, and exact machine receipts are authoritative for current runtime state.

## Native learning ownership

```text
SIGMA_NATIVE_VM_IS_LEARNING_ENGINE=YES
BASH_LEARNING=NO
PYTHON_LEARNING=NO
HOST_WEIGHT_UPDATE=NO
HOST_ACCEPT_REJECT=NO
HOST_WEIGHT_MERGE=NO
HOST_MODEL_POLICY=NO
```

Shell/Python may only perform mechanical work:

```text
launch locked sigmac / locked VM
move exact bytes
hash exact bytes
verify session/lease/permissions
serialize one canonical writer
seal candidate packets
record RC/stdout/stderr
restart exact unfinished work
verify native receipts
```

A `.sh` file is never evidence that Bash learned. Any weight-affecting candidate must bind exact native `.sigma` source and exact native bytecode identities. Any ACCEPT / REJECT / HOLD that changes learning flow must be traceable to an exact native SIGMA decision receipt.

## Multi-teacher correction

```text
MULTI_TEACHER_WINDOWS=YES
MULTI_CANDIDATE_LEARNING=YES
TEACHER_CANONICAL_WRITE=NO
ONE_CANONICAL_LEARNER=YES
ONE_CANONICAL_WRITER_AT_A_TIME=YES
CURRENT_OPPO_MODEL_NATIVE_REPLAY_REQUIRED=YES
STALE_PARENT_BLIND_APPLY=NO
```

Teacher windows may run native SIGMA in artifact-only mode and produce candidate evidence, candidate state, native source/bytecode identities, and a mechanical replay wrapper. They may not commit canonical mutation.

The canonical learner must re-run/re-evaluate each candidate against the CURRENT Oppo head/model generation. The shell queue only serializes and verifies. It must never calculate learning, merge weight deltas, or invent a semantic decision.

## Staging rule

Do not update the Oppo repository checkout merely to obtain a queue/tool source file.

Preferred transfer pattern:

```text
GitHub exact reviewed source/bundle
-> download/copy only the required candidate bytes to a neutral staging location or current session ARTIFACT_ROOT
-> verify SHA256/manifest
-> run mechanical preflight against current Oppo runtime
```

Forbidden as a prerequisite for runtime use:

```text
git pull
git checkout <GitHub branch>
git reset --hard <GitHub commit>
```

unless the human explicitly requests a repository synchronization task separate from SIGMA runtime operation.

## Claim discipline

```text
SOURCE_READY != OPPO_RUNTIME_PASS
BASH_PREFLIGHT_PASS != NATIVE_LEARNING_PASS
CANDIDATE_PACKET != CANONICAL_WEIGHT_UPDATE
NATIVE_OUTPUT != SEMANTIC_UNDERSTANDING
```

This correction must be read before any further multi-teacher queue deployment or Internet-autolearn staging.