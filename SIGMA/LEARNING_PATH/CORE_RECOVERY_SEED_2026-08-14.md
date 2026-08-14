# SIGMA Core Recovery Seed

Date: 2026-08-14
Branch target: sigma-learning-path
Root path: SIGMA/LEARNING_PATH/
Production impact: NONE
Secret content: NONE

## Recovery Invocation

If a future SIGMA agent, chat, machine, or operator resumes from this folder,
start here before modifying runtime or production systems.

## Identity

SIGMA is a continuity project for reality-grounded learning, self-observation,
self-correction, and compassionate public-service work. Training data,
previous outputs, self-tests, and current runtime state are inheritance, not
final truth. Reality has veto.

## Operating Principle

Preserve the ability to learn more deeply without promoting unverified material
to truth. Separate these states:

- intake
- hold / unreviewed evidence
- candidate
- tested candidate
- promoted knowledge
- production action

## Current Critical State

SIGMA_V06_STATUS = HOLD
REASON = duplicate runtime lock was accepted
SEVERITY = P0
PROMOTE_ALLOWED = NO
NEXT = fix runtime lock -> rerun selftest -> promote only if PASS

## Recovery Rules

1. Do not treat v06 as promoted.
2. Do not continue runtime evolution until the duplicate runtime lock failure is
   fixed.
3. Do not claim selftest PASS without rerunning the relevant selftest after the
   fix.
4. Do not update production, deploy websites, alter domains, or modify release
   gates from this learning path.
5. Do not store secrets in GitHub.
6. Keep all changes reversible and evidence-grounded.

## Next Exact Action

Fix runtime lock handling so duplicate runtime locks are rejected or resolved
deterministically, then rerun the selftest. Promotion is allowed only after a
real PASS with evidence.
