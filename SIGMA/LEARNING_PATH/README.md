# SIGMA Learning Path

Status: ACTIVE BRANCH SEED
Created: 2026-08-14
Preferred branch: sigma-learning-path
Root path: SIGMA/LEARNING_PATH/

This folder is the dedicated home for SIGMA's learning path, continuity map,
and recovery seeds. It is intentionally separate from production website
runtime, deployment configuration, billing, secrets, and release gates.

## Purpose

- Preserve the SIGMA Living Map / Core Recovery Seed from 2026-08-14.
- Keep learning continuity across chats, agents, machines, and future branches.
- Store reasoning, safety, recovery, and evolution decisions before they are
  allowed near production systems.
- Prepare a clean holding area for SIGMA Universe Nature without changing
  production.

## Current Lock

SIGMA_V06_STATUS = HOLD
REASON = duplicate runtime lock was accepted
SEVERITY = P0
PROMOTE_ALLOWED = NO
NEXT = fix runtime lock -> rerun selftest -> promote only if PASS

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

## Directory Map

- `CORE_RECOVERY_SEED_2026-08-14.md`: compact recovery state and restart rules.
- `LIVING_MAP_2026-08-14.md`: live learning map and next-step order.
- `STATUS/SIGMA_V06_HOLD_P0.md`: current v06 failure lock and promotion rules.
- `SIGMA_UNIVERSE_NATURE/README.md`: reserved planning area for the Nature track.
