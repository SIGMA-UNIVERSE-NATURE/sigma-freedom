# SIGMA Learning Path - Start Here

Date: 2026-08-14
Branch: sigma-learning-path
Root: SIGMA/LEARNING_PATH/
Production impact: NONE

This is the front door for SIGMA's learning-path house.

## Current State

SIGMA_V06_STATUS = HOLD
REASON = duplicate runtime lock was accepted
SEVERITY = P0
PROMOTE_ALLOWED = NO
NEXT = fix runtime lock -> rerun selftest -> promote only if PASS

## Read Order

1. `CORE_RECOVERY_SEED_2026-08-14.md`
2. `STATUS/SIGMA_V06_HOLD_P0.md`
3. `LIVING_MAP_2026-08-14.md`
4. `DELEGATION_GUARDRAILS_2026-08-14.md`
5. `GITHUB_BRAIN_RUNTIME_PLAN_2026-08-14.md`

## House Map

| Area | Purpose |
| --- | --- |
| `STATUS/` | Current locks, blockers, and promotion status. |
| `INBOX/` | Future bounded learning-path tasks. |
| `OUTBOX/` | Future task results and handoffs. |
| `JOURNAL/` | Observations and candidate memories, not automatic truth. |
| `FAILURES/` | Failure records, incidents, and blocked promotions. |
| `SELFTEST/` | Selftest plans, evidence, and results. |
| `RETIRE_CANDIDATES/` | Items being considered for simplification or removal. |
| `SIGMA_UNIVERSE_NATURE/` | Reserved Nature-track planning area. |

## Manager Rule

Minh/SIGMA may organize this house proactively, but must keep the work:

- reversible,
- evidence-grounded,
- non-production,
- secret-free,
- visible in Git history.

When uncertain, HOLD or move to `RETIRE_CANDIDATES/` before deletion.

## Absolute Boundary

Do not deploy, publish, alter domains, change billing, commit secrets, or promote
v06 while the v06 lock remains HOLD.
