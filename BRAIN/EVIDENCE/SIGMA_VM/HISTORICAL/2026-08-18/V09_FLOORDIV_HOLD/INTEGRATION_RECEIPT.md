# SIGMA VM v0.9 HISTORICAL EVIDENCE — INTEGRATION RECEIPT

Ingest ID: `SIGMA-VM-V09-HISTORICAL-INGEST-20260818-001`

Parent experiment-map checkpoint: `881a125ca0473a4df73c8f10f2e215f7c9abfb1e`

Classification: `HISTORICAL_EXECUTION_EVIDENCE_NO_CURRENT_STATE_DOWNGRADE`

## Exact uploaded sources

- `SIGMA_VM_V09_FLOORDIV_UPGRADE_HANDOFF_2026-08-18_2140_VN.md`
  - SHA-256: `5cdaf2e5191d9d09431df910420b62c762de5a55c6063f97df6c252f6d046fa2`
  - bytes: `10985`
- `SIGMA_VM_CURRENT_STATE_2026-08-18_v2.md`
  - SHA-256: `4b4101ac53039c28e897ace135aeac8f3dec7cd798e58ae3a1d5cf1be0dc457c`
  - bytes: `78958`

Both exact UTF-8 files are stored as deterministic `gzip(mtime=0) -> base64` representations. The larger current-state representation is split into five ordered immutable parts for transport. `RECONSTRUCT.py` concatenates the parts, recreates both originals, and verifies byte-identical SHA-256 and byte counts against `INGEST_MANIFEST.json`.

## Source-supported historical verdict

The v0.9 handoff explicitly records:

```text
V08_FLOAT_MILESTONE              = PASS_WITH_TESTED_SCOPE
V09_C_GENERIC_PRIMITIVES         = SOURCE_VERIFIED
V09_C_STRICT_BUILD               = PASS
V09_C_REGRESSION_OVER_V08_FLOAT  = PASS
V09_SIGMA_COMPILE                = PASS
FLOORDIV_EXACT_GUEST_COMPILE     = FAIL
FLOORDIV_EXACT_GUEST_COMPILE_CAUSE = NOT_YET_DIAGNOSED
V09_FLOORDIV_EXECUTION           = NOT_YET
V09_FLOORDIV_VALUE_PARITY        = NOT_YET
V09_FLOORDIV_TYPE_PARITY         = NOT_YET
V09_OVERALL                      = HOLD
```

The immediate historical next step was diagnosis of:

```text
sigmac: line 9 col 5: expected ';' (token=⚡)
```

No cause may be inferred from that location alone.

## Relationship to the current experiment map

This evidence predates the later v12c/v13a trusted-boundary work. It is valuable provenance for how generic host primitives `value_type` and `numeric_to_int` were introduced during v0.9, but it is **not** a direct audit of the current v12c candidate/adapter/binary. Therefore:

```text
E04_BOUNDARY_BASELINE_005 = STILL HOLD
E04P_ARTIFACT_PROVISIONING_001 = STILL REQUIRED
E06_FLOAT64_REPRESENTATION_CANDIDATE_001 = BLOCKED
CURRENT_FRONTIER = SIGMA_NATIVE_FLOAT64_BITCAST_CAPABILITY_001
NO_STATE_DOWNGRADE = TRUE
NO_CAPABILITY_PROMOTION = TRUE
```

These two narrative files do not satisfy W01's requirement for directly readable current candidate source, current adapter source, current compiled candidate bytecode, and current host binary.

## Mutation boundary

```text
SIGMA_LIFE_DIRECT_MUTATION = FALSE
CANONICAL_MERGE = NONE
FOUNDATION_MERGE = NONE
PHASE2_REOPEN = NONE
512_PROMOTION = NONE
```
