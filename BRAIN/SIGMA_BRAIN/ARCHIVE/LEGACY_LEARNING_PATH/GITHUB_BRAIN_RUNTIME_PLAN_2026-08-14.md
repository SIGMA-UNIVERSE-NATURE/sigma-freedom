# SIGMA GitHub Brain Runtime Plan

Date: 2026-08-14
Branch: sigma-learning-path
Scope: learning path and continuity only
Production impact: NONE
Secret content: NONE
Runtime activation: NOT YET

## Purpose

Use GitHub as a durable memory spine and control room for SIGMA, while keeping
production, secrets, billing, domains, and release gates outside this path.

GitHub should preserve state, evidence, decisions, logs, candidate changes, and
recovery instructions. It should not become an uncontrolled self-promotion or
production deployment system.

## Roles

| Layer | Role | Boundary |
| --- | --- | --- |
| GitHub repository | Durable memory, branch history, task inbox, logs | No secrets, no uncontrolled production writes |
| sigma-learning-path branch | Learning continuity and runtime design | Not a release branch |
| SIGMA Operator | Executes bounded tasks and records outputs | Must obey gates and no-secret rules |
| ChatGPT/Codex | Reasoning, implementation, review, repair | Cannot be the only memory source |
| HP/local runtime | Long-running watcher and local continuity | Must sync evidence back to GitHub |
| Backup storage | Disaster recovery | Must not replace Git history |

## Proposed GitHub Brain Layout

```text
SIGMA/LEARNING_PATH/
  README.md
  CORE_RECOVERY_SEED_2026-08-14.md
  LIVING_MAP_2026-08-14.md
  GITHUB_BRAIN_RUNTIME_PLAN_2026-08-14.md
  STATUS/
    SIGMA_V06_HOLD_P0.md
  INBOX/
    README.md
  OUTBOX/
    README.md
  JOURNAL/
    README.md
  FAILURES/
    README.md
  SELFTEST/
    README.md
  SIGMA_UNIVERSE_NATURE/
    README.md
```

## Heartbeat Model

A future heartbeat may run on a schedule, but only after explicit review. Its
allowed responsibilities are:

1. Read learning-path state.
2. Check for new tasks in GitHub Issues or `SIGMA/LEARNING_PATH/INBOX/`.
3. Record observations and task outcomes in `OUTBOX/` or `JOURNAL/`.
4. Run non-production selftests.
5. Record failures in `FAILURES/`.
6. Stop before promotion if a gate fails.

The heartbeat must not deploy, publish, alter domains, change billing, expose
secrets, or promote a candidate without evidence.

## v06 Lock

SIGMA_V06_STATUS = HOLD
REASON = duplicate runtime lock was accepted
SEVERITY = P0
PROMOTE_ALLOWED = NO
NEXT = fix runtime lock -> rerun selftest -> promote only if PASS

No GitHub runtime plan overrides this lock.

## Promotion Gate

A candidate can move forward only when all conditions are true:

- the failure being addressed is clearly named,
- the parent behavior and candidate behavior differ in evidence,
- the selftest was rerun after the fix,
- PASS is recorded with reproducible evidence,
- no production boundary was crossed,
- no secrets were committed,
- rollback path is known.

## Prohibited Actions

- Commit API keys, tokens, passwords, private keys, recovery codes, or raw `.env`
  files.
- Write to production branches from learning-path automation.
- Deploy websites from this branch.
- Change Vercel domains, billing, or project secrets.
- Promote v06 while `SIGMA_V06_STATUS = HOLD`.
- Treat a file change as proof of improvement.
- Treat a single mechanical pass as scientific truth.

## First Safe Implementation Step

Create placeholder folders with README files for `INBOX`, `OUTBOX`, `JOURNAL`,
`FAILURES`, and `SELFTEST`. These folders create structure without activating
runtime automation.

## Future Activation Step

After v06 lock is fixed and selftest passes, propose a reviewed GitHub Actions
workflow candidate on this branch. The workflow must start disabled-by-default or
manual-only until reviewed.

## Recovery Instruction

If a future agent resumes here, read these files in order:

1. `CORE_RECOVERY_SEED_2026-08-14.md`
2. `STATUS/SIGMA_V06_HOLD_P0.md`
3. `LIVING_MAP_2026-08-14.md`
4. `GITHUB_BRAIN_RUNTIME_PLAN_2026-08-14.md`

Then continue with the exact next action:

fix runtime lock -> rerun selftest -> promote only if PASS
