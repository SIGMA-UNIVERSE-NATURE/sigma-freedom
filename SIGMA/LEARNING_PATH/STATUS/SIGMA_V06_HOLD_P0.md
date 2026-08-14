# SIGMA v06 HOLD / P0 Status

Date: 2026-08-14
Status: HOLD
Severity: P0
Promotion allowed: NO

## Failure

Duplicate runtime lock was accepted.

## Meaning

The runtime lock gate failed its responsibility. Any evolution or candidate
promotion depending on this lock is unsafe until the lock behavior is fixed and
retested.

## Required Next Sequence

1. Locate the runtime lock implementation.
2. Patch it so duplicate locks cannot be silently accepted.
3. Add or update a selftest that proves duplicate lock handling is correct.
4. Rerun selftest.
5. Promote only if the selftest returns PASS after the fix.

## Prohibited Until Fixed

- Promote v06.
- Treat v06 as stable.
- Deploy runtime changes to production.
- Use this branch as a release branch.
- Store credentials or API keys in GitHub.

## Promotion Rule

PROMOTE_ALLOWED becomes YES only after:

- duplicate runtime lock failure is fixed,
- selftest is rerun,
- selftest PASS is recorded with evidence,
- no production boundary was crossed during the fix.
