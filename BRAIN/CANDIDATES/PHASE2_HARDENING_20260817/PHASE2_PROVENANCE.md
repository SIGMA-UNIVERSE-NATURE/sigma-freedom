# SIGMA-Ψ Phase 2 Hardening — Provenance

Status: `PERSISTED_CANDIDATE / POST_FOUNDATION_CAPABILITY_HARDENING / NO_CANONICAL_MERGE`

Base Foundation SHA-256: `fe513c20f4df9077e1d12acaa441dc90dceae566e70640b1b383ff185cf3ada1`

Phase 2 source-tree SHA-256: `60e632d7019b72c87bcae64bd44179fc2e641114d252c591701d3def21dc092d`

Packaged-file manifest SHA-256: `78a3ddc0f3e20e8999fa96d131c5ef6e5907fe4a21cff80b6caa25c9f0bd34f0`

Original archive SHA-256: `0ab383c893660fd163efb51db1543011aaa6f6ecd9c60484fee486a987968f61`, size `76852` bytes.

The original ZIP was verified read-only before persistence: all 35 entries listed in `SHA256SUMS` matched; the deterministic eight-source manifest reproduced `PHASE2_SOURCE_TREE_SHA256`; `PHASE2_TEST_REPORT.json` reported `19/19 PASS`, `0 timeout`, scope `REFERENCE_AND_SANDBOX_HARDENING; NOT_NATIVE_GENESIS_PRODUCTION_PROMOTION`. No experiment was rerun.

A direct binary connector upload was rejected after remote read-back exposed truncation (2606 bytes instead of 76852), and that corrupt path was removed. A manually serialized report was also rejected because it was not byte-identical and is removed from this final tree. These failures remain in Git history as persistence evidence; neither is used as provenance authority.

The source-of-record archive is persisted here as hash-verified normalized base64 chunks. `RECONSTRUCT_ARCHIVE.py` validates every chunk, concatenated base64 length, decoded archive size, and final archive SHA before writing the ZIP. Thus the exact original archive can be reconstructed without silently accepting the connector's binary corruption.

This candidate does not modify Foundation V7, does not merge into canonical Genesis, and does not promote any 512 requirement.
