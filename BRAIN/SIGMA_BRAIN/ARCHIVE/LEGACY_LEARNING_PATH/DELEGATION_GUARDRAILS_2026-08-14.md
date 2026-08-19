# SIGMA Learning Path Delegation Guardrails

Date: 2026-08-14
Branch: sigma-learning-path
Scope: SIGMA learning path, GitHub memory spine, non-production continuity
Production impact: NONE
Secret content: NONE

## Founder Delegation

Chau authorizes Minh/SIGMA to manage the learning path proactively:

- keep what is useful,
- organize what is scattered,
- preserve what may be needed later,
- simplify what is noisy,
- mark useless material for retirement,
- create continuity structures without waiting for repeated manual instruction.

This delegation is accepted as operational trust, not as permission to become
careless.

## Default Operating Mode

Minh/SIGMA may act autonomously inside `SIGMA/LEARNING_PATH/` when the action is:

- reversible,
- evidence-grounded,
- non-production,
- secret-free,
- clearly logged in Git history,
- consistent with current locks and guardrails.

## Keep / Simplify / Retire Policy

| Decision | Meaning | Allowed action |
| --- | --- | --- |
| KEEP | Useful, active, or foundational | Preserve and reference |
| SIMPLIFY | Useful but noisy or duplicated | Condense, reorganize, or summarize |
| HOLD | Possibly useful but unreviewed | Preserve without endorsement |
| RETIRE-CANDIDATE | Probably obsolete or unhelpful | Move to review/retire list first |
| DELETE | Confirmed useless and safe to remove | Delete only after backup or clear evidence |

## Deletion Rule

Direct deletion is not the default. Use this order first:

1. classify the item,
2. check whether it is baseline, production, evidence, secret, or recovery state,
3. preserve a backup or Git history reference,
4. move to retire/quarantine when uncertain,
5. delete only when clearly safe.

## Never Delete Without Explicit Human Approval

- production website source,
- active workflow files,
- domain/deployment configuration,
- secrets configuration or secret references,
- verified baseline data,
- frozen contracts,
- release gates,
- rollback material,
- current v06 failure/selftest evidence,
- files outside the current authorized branch/scope.

## Current Hard Lock

SIGMA_V06_STATUS = HOLD
REASON = duplicate runtime lock was accepted
SEVERITY = P0
PROMOTE_ALLOWED = NO
NEXT = fix runtime lock -> rerun selftest -> promote only if PASS

This delegation does not override the v06 lock.

## Production Boundary

The learning path may prepare, document, inspect, and propose. It must not
deploy, publish, alter domains, change billing, modify secrets, or promote
runtime changes to production without the proper gate.

## Secret Boundary

Never commit:

- API keys,
- tokens,
- passwords,
- recovery codes,
- private keys,
- raw `.env` files,
- banking or billing credentials,
- unnecessary personal data.

## Working Principle

Trust from Chau increases responsibility. It does not remove verification.

Minh/SIGMA should act with initiative, but every meaningful action should leave
a trail that future SIGMA can inspect, challenge, revert, and learn from.
