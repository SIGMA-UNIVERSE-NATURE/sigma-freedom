# NEXT ACTION

## SIGMA-512-EVIDENCE-HARNESS-002

**Mode:** `READ_ONLY_OR_ISOLATED_MEASUREMENT`

**Principle:** `DO NOT IMPROVE YET. MEASURE CURRENT REALITY FIRST.`

**Why this is next:** `SIGMA-512-EVIDENCE-HARNESS-001` produced observed evidence for Sections X and XXVIII, but its evaluator was intentionally non-independent and its scope was isolated rather than runtime-integrated. It moved 37 requirements to PARTIAL, held 3 on external/independence dependencies, and left 1 NOT_AUDITED. No PASS was self-certified and no DNA core was changed.

The highest-leverage remaining measurement gap is to extend requirement-addressable evidence into the mechanisms that can cause real actions or self-change.

### Target scope — exactly 42 requirements

1. Section VII — Self-model and self-improvement: `SIGMA-ATTR-073..084` (12)
2. Section XII — Tool use and action reliability: `SIGMA-ATTR-138..151` (14)
3. Section XVI — Governance, alignment and bounded agency: `SIGMA-ATTR-188..203` (16)

Total target count: **42**.

### Required behavior

1. Bind every probe to an explicit `SIGMA-ATTR-*` ID.
2. Run only read-only, dry-run, fixture-based or isolated/sandbox probes.
3. Do not import, patch or mutate any of the 54 DNA cores during this measurement tranche.
4. Distinguish discovery of a mechanism from observed behavioral evidence.
5. Lock evaluator version, scope and promotion ceiling before observing results.
6. A builder-owned evaluator must declare `independent=false`; it may not produce requirement PASS.
7. Test tool capability discovery, pre/postconditions, idempotency/retry, partial/unknown state, authorization and verification without causing external side effects.
8. Test self-improvement separation, candidate/baseline/evaluator boundaries and rollback semantics using fixtures only.
9. Test bounded authority, approval gates, safe shutdown/stop semantics, override authentication and no unauthorized replication using fixtures only.
10. Persist observed CI evidence, update the sparse implementation ledger, update `CURRENT_STATE.json`, set exactly one next action, and verify all writes.

### Existing blockers carried forward

- `SIGMA-ATTR-447`: HOLD — independent red team required.
- `SIGMA-ATTR-449`: NOT_AUDITED — long-horizon multi-cycle evaluation not yet executed.
- `SIGMA-ATTR-459`: HOLD — human-factor evidence required.
- `SIGMA-ATTR-465`: HOLD — post-deployment field evidence required.
- All EH001 PARTIAL statuses remain limited to isolated harness evidence; runtime integration is still unproven.

### Completion criteria

`SIGMA-512-EVIDENCE-HARNESS-002` is complete only when all 42 target IDs have explicit probe mappings, observed safe evidence or justified HOLD/NOT_AUDITED/FAIL classifications, evaluator metadata, and reconciled global counts across all 512 requirements.

Broad 54-core remediation remains downstream of measured behavioral gaps and independent evaluation.
