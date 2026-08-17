# SIGMA-Ψ Phase 2 Hardening — Provenance

Status: `PERSISTED_CANDIDATE / POST_FOUNDATION_CAPABILITY_HARDENING / NO_CANONICAL_MERGE`

This directory preserves the completed Phase 2 hardening candidate exactly as received in `SIGMA_PSI_HARDENING_PHASE2_20260817.zip`.

## Identity

- Base Foundation SHA-256: `fe513c20f4df9077e1d12acaa441dc90dceae566e70640b1b383ff185cf3ada1`
- Phase 2 implementation source-tree SHA-256: `60e632d7019b72c87bcae64bd44179fc2e641114d252c591701d3def21dc092d`
- Phase 2 full packaged-file manifest SHA-256: `78a3ddc0f3e20e8999fa96d131c5ef6e5907fe4a21cff80b6caa25c9f0bd34f0`
- Phase 2 archive SHA-256: `0ab383c893660fd163efb51db1543011aaa6f6ecd9c60484fee486a987968f61`
- Original archive size: `76852` bytes
- Implementation source files: `8`
- Evidence tests: `19 / 19 PASS`
- Timeouts: `0`

## Source-tree hash algorithm

`PHASE2_SOURCE_TREE_SHA256` is the SHA-256 of the path-qualified, lexicographically sorted manifest containing the eight `sigma_hardening/*.py` per-file hashes from `evidence/PHASE2_TEST_REPORT.json`, serialized as `<sha256><two spaces>sigma_hardening/<filename>\n`. The exact manifest is preserved as `PHASE2_SOURCE_MANIFEST.txt`.

## Scope boundary

The packaged report declares `REFERENCE_AND_SANDBOX_HARDENING; NOT_NATIVE_GENESIS_PRODUCTION_PROMOTION`.

This persistence does not modify Foundation V7, does not merge Phase 2 into canonical Genesis, does not promote any 512 requirement to PASS, and does not convert reference/sandbox PASS into native/production PASS.

The original archive did not embed the Base Foundation SHA internally because that SHA was supplied after Phase 2 packaging. This provenance record closes that linkage additively without rewriting the immutable archive.

## Persistence

The original ZIP is preserved as the source-of-record artifact. It contains the implementation sources, tests, `PHASE2_TEST_REPORT.json`, installer smoke evidence, gate ledger, current status, native integration backlog, README, install candidate script and `SHA256SUMS`. No experiment was rerun during persistence. Read-only integrity verification is recorded in `PHASE2_PERSISTENCE_VERIFICATION.json`.
