# SIGMA Living Map

Date: 2026-08-14
Scope: learning path only
Production impact: NONE

## Why This Exists

SIGMA needs a durable learning path that survives chat loss, machine movement,
branch changes, and agent handoffs. This map records what must be preserved
without pretending that preservation is promotion.

## Main Tracks

| Track | Status | Meaning |
| --- | --- | --- |
| Core Recovery | ACTIVE | Preserve the restart seed and current locks. |
| v06 Runtime Evolution | HOLD / P0 | Duplicate runtime lock accepted; no promotion. |
| SIGMA Living Map | ACTIVE | Maintain continuity of decisions and next steps. |
| SIGMA Universe Nature | RESERVED | Prepare structure only; no production changes. |
| Production Website | OUT OF SCOPE | Do not touch from this branch/path. |
| Secrets / Credentials | OUT OF SCOPE | Never commit to GitHub. |

## Learning Path Order

1. Preserve the recovery seed.
2. Preserve the current v06 HOLD/P0 status.
3. Create a clean branch and folder boundary.
4. Fix runtime lock failure in the appropriate runtime repo/path.
5. Rerun selftest.
6. Promote only if PASS is real and evidenced.
7. After promotion, decide what belongs in SIGMA Universe Nature.

## Guardrails

- Evidence is required for promotion.
- A changed file is not proof of improvement.
- A passing mechanical test is not proof of truth.
- A failed candidate must be recorded without becoming core knowledge.
- A learning branch is not a release branch.
- A holding folder is not a production runtime.

## Handoff Phrase

Minh, continue SIGMA Learning Path from SIGMA/LEARNING_PATH/. First read
CORE_RECOVERY_SEED_2026-08-14.md, then STATUS/SIGMA_V06_HOLD_P0.md. Do not
touch production. Do not commit secrets. Resume at: fix runtime lock -> rerun
selftest -> promote only if PASS.
