# C5 V1 preflight — CASE_E failure preserved / FIX1 runner source ready

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: `PREFLIGHT_FAIL_PRESERVED / RUNNER_ONLY_FIX1_SOURCE_READY / RERUN_REQUIRED`

## Observed machine evidence from Oppo

The user ran the C5 V1 preflight under `$HOME/SIGMA/sigma_genesis1` and supplied the terminal tail:

```text
ASSERT_PASS=CASE_C_CANDIDATES_NATIVE_NONEMPTY
EVIDENCE_LOOKUP_RECORDS=2
CASE_D_NATIVE_EVIDENCE_AND_RESEARCH_INTENT_VM_RC=0
ASSERT_PASS=CASE_D_ACTION VALUE=PERSIST_EVIDENCE
ASSERT_PASS=CASE_D_NATIVE_EXTERNAL_QUERY_DYNAMIC VALUE=beta alpha
EVIDENCE_PERSISTED=2
KNOWLEDGE_PERSISTED=1
EVIDENCE_LOOKUP_RECORDS=0
ASSERT_FAIL=CASE_E_REPLAY_PROVENANCE_NOT_SEEN
C5_PREFLIGHT_PROCESS_RC=57
```

Therefore:

```text
C5_V1_PREFLIGHT=FAIL
FAILURE_IS_EVIDENCE=YES
C5_ADMISSION=NO
PRODUCTION_BINDING=NO
```

## Root cause

The failure is in the V1 preflight replay harness lifecycle, not an observed locked-VM failure in the native C5 core.

The old CASE_E called mechanical `evidence-lookup` a second time using `out/pending_candidates.txt`, but each fresh native VM invocation intentionally clears ephemeral output files at invocation start. CASE_D therefore cleared the CASE_C candidate output before the runner reused it. The second lookup consequently reported `EVIDENCE_LOOKUP_RECORDS=0` and could not expose `PROV_SEEN=YES`.

This diagnosis does not itself prove provenance replay idempotency.

## FIX1

FIX1 changes only the preflight runner. Native source, mechanical bridge, and continuous runner remain byte-identical.

FIX1 models the intended crash window instead:

```text
evidence persisted
-> segment not committed
-> simulated restart / TICK
-> native SIGMA resumes the active local entry
-> exact same uncommitted segment is replayed
-> native SIGMA regenerates candidates
-> mechanical lookup exposes persisted provenance
-> native SIGMA recomputes with PROV_SEEN=YES
-> support must remain unchanged
```

## Identities

```text
NATIVE_SOURCE_CHANGED=NO
NATIVE_SOURCE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
MECHANICAL_BRIDGE_CHANGED=NO
MECHANICAL_BRIDGE_SHA256=66c01ddcc9b229e854266eecd3e91c2c0930ea8a347ff61d0daa447e1083abd5
CONTINUOUS_RUNNER_CHANGED=NO
CONTINUOUS_RUNNER_SHA256=550af3a398c79d52031bf846e254e13fa1762357474f0f9c278075a263ca242a
OLD_PREFLIGHT_SHA256=3b49fcd7c56a957e8d2cd88d2105ad8c101fbe90d78ed168ad49ce5eda0ab4b5
FIX1_PREFLIGHT_SHA256=cf4ecc17ddd9947fb2f9158f06eb3d4defd25fd2f5dba7c887602de9afb52831
FIX1_PATCH_BUNDLE_SHA256=e0d1e491ea0b6d8868649e122072a711fa2e6946cbb677eccbf50e3a5ad405c2
```

Locked runtime identities remain required on rerun:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Claim boundary

```text
C5_FIX1_RUNNER_SOURCE_READY=YES
C5_FIX1_LOCKED_VM_RERUN=NOT_RUN
C5_FIX1_PREFLIGHT_ADMISSION=NOT_RUN
REAL_OPPO_ARCHIVE_LEARNING=NOT_RUN
LIVE_SELF_INITIATED_INTERNET_LOOP=NOT_RUN
PRODUCTION_BINDING=NO
```
