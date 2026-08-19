# SIGMA Learning Path SELFTEST

Status: PLACEHOLDER
Runtime activation: NOT YET
Production impact: NONE

This folder is reserved for selftest plans, selftest evidence, and selftest
results relevant to SIGMA learning-path evolution.

Selftest rules:

- A selftest must be rerun after the fix it is meant to validate.
- A selftest result must name the code or behavior tested.
- PASS must include reproducible evidence.
- FAIL must block promotion until addressed.
- Mechanical PASS does not automatically mean scientific truth or production
  readiness.

Current required sequence:

fix runtime lock -> rerun selftest -> promote only if PASS
