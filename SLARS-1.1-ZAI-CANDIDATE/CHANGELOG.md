# Changelog

## SLARS-1.1-ZAI candidate

- Added the normative SIGMA Language / Zero Answer Injection module.
- Added content-addressed ZAI protocol and run schemas.
- Added a dependency-free strict structural and evidence validator.
- Added artifact materialization, safe-path, hash, visibility, registered
  forbidden-material, native-event-chain and claim-dependency checks.
- Added adversarial mutation tests.
- Bound each event hash to referenced artifact ID, SHA-256 and byte count.
- Added strict RFC3339 timestamps, canonical artifact metadata and verdict
  receipt hashes for protocol/run/verifier/schemas/standard/package manifest.
- Upgraded semantic review to a hash-bound full-surface v2 record.
- Upgraded channel evidence to per-channel non-empty, status/class/hash-bound
  v2 capture records; an empty file can no longer cover multiple channels.
- Added invalid-UTF8-safe ASCII scans plus bounded URL-percent and JSON Unicode
  escape decoding, fingerprint collision checks and scan resource ceilings.
- Hardened report rendering against control-character/status injection.
- Narrowed the toolchain claim to a declared event-chain binding; approved
  native build identity still requires external attestation.
- Relabeled the retained SLARS-1.0 validator as legacy-only and blocked it from
  emitting a full SLARS-1.1 package PASS without per-output ZAI integration.
- Preserved the exact policy token `SUPPORTOR` supplied by the user.
- Separated the implemented Z0–Z4 injection-integrity profile from future Z5
  observation-dependence, Z6 blind-performance and Z7 independent-reproduction
  profiles.
- Bound critical source/bytecode/stdin/stderr/exit-code channel evidence,
  protocol/run artifact IDs and native host-operation topology.
- Kept task correctness orthogonal: a clean wrong answer can be
  `ZERO_ANSWER_INJECTION=PASS` with `TASK_OUTCOME=FAIL`.
- Kept all acquisition, reasoning and cognition claims unverified.

This is a candidate produced for independent review. It is not a release or an
independent technical PASS.
