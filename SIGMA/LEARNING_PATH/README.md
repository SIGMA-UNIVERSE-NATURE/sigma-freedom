# SIGMA Learning Path

Status: ACTIVE BRANCH SEED
Created: 2026-08-14
Branch: sigma-learning-path
Root path: SIGMA/LEARNING_PATH/
Production impact: NONE
Secret content: NONE

This folder is SIGMA's learning-path house: a durable memory spine, recovery
seed, task staging area, and non-production control room.

Start here:

`00_START_HERE.md`

## Current Lock

SIGMA_V06_STATUS = HOLD
REASON = duplicate runtime lock was accepted
SEVERITY = P0
PROMOTE_ALLOWED = NO
NEXT = fix runtime lock -> rerun selftest -> promote only if PASS

## Purpose

- Preserve SIGMA Living Map / Core Recovery Seed 2026-08-14.
- Keep continuity across chats, agents, machines, and future branches.
- Store reasoning, safety, recovery, and evolution decisions before they are
  allowed near production systems.
- Prepare a clean holding area for SIGMA Universe Nature without changing
  production.
- Give Minh/SIGMA a managed space to organize, simplify, and retire material
  safely.

## Read Order

1. `00_START_HERE.md`
2. `CORE_RECOVERY_SEED_2026-08-14.md`
3. `STATUS/SIGMA_V06_HOLD_P0.md`
4. `LIVING_MAP_2026-08-14.md`
5. `DELEGATION_GUARDRAILS_2026-08-14.md`
6. `GITHUB_BRAIN_RUNTIME_PLAN_2026-08-14.md`

## House Map

| Path | Role |
| --- | --- |
| `CORE_RECOVERY_SEED_2026-08-14.md` | Compact restart state and recovery rules. |
| `LIVING_MAP_2026-08-14.md` | Current learning map and next-step order. |
| `DELEGATION_GUARDRAILS_2026-08-14.md` | Founder delegation and cleanup boundaries. |
| `GITHUB_BRAIN_RUNTIME_PLAN_2026-08-14.md` | GitHub brain/control-room plan, not active automation. |
| `STATUS/` | Locks, blockers, promotion state. |
| `INBOX/` | Future bounded learning-path tasks. |
| `OUTBOX/` | Future task results and handoffs. |
| `JOURNAL/` | Observations and candidate memory, not automatic truth. |
| `FAILURES/` | Failures, incidents, regressions, blocked promotions. |
| `SELFTEST/` | Selftest plans, evidence, and results. |
| `RETIRE_CANDIDATES/` | Items considered for simplification or removal. |
| `SIGMA_UNIVERSE_NATURE/` | Reserved Nature-track planning area. |

## Manager Rule

Minh/SIGMA may manage this space proactively when changes are reversible,
evidence-grounded, non-production, secret-free, and visible in Git history.

Deletion is never the first move for uncertain material. Use HOLD or
`RETIRE_CANDIDATES/` first.

## Production Boundary

This path is not production. Nothing here authorizes deployment, release,
domain changes, billing changes, secret handling, or runtime promotion.

## Secret Boundary

Do not commit:

- API keys
- tokens
- passwords
- recovery codes
- private credentials
- raw environment files
- billing or banking information
- private personal data not required for SIGMA continuity

Use environment variables, secret stores, or scoped GitHub/Vercel settings
outside this folder when real credentials are needed.
