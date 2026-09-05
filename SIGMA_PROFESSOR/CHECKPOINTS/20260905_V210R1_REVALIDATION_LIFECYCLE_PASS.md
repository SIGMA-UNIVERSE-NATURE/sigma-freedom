# V2.10R.1 — REVALIDATION -> REVISIT / ARCHIVE_FOR_NOW — PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Locked runtime

- SIGMAC SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

## Exact V2.10 native artifact

- source: `SIGMA_PROFESSOR/artifacts/SIGMA_REVALIDATION_TO_REVISIT_ARCHIVE_V2_10R1.sigma`
- source SHA256: `67fb7234c0cd9e84c602a6dadb55f6e1ced6265406745ba6b3b9a7a95e0c4993`
- runtime bytecode SHA256: `527bf0513082af49343f39b5ae23fd63b5c25f4034e019e934ca1d425890ef87`

## Real-chain proof

The runner regenerated the admitted native chain before V2.10:

- V2.8R.1 real selected work: `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
- V2.8D.1 real deep evidence regenerated;
- V2.9R.1 real structural revalidation regenerated;
- regenerated real revalidation state SHA256: `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac`;
- real structural result: `NOT_REOBSERVED`.

V2.10 real lifecycle result:

- `REVALIDATION_FOUND 1`
- `REVALIDATION_CONFLICT 0`
- `REVALIDATION_RESULT NOT_REOBSERVED`
- `LIFECYCLE_READY 1`
- `LIFECYCLE_ACTION REVISIT`
- `LIFECYCLE_APPEND_RC 0`
- lifecycle state SHA256: `f34678fd6c85394ee659b6a710920bed8cc5ea07f8cbba0414cbb3bc116c79fb`

Fresh VM reuse:

- `LIFECYCLE_ALREADY_COMMITTED 1`
- lifecycle state hash unchanged.

Deterministic replay:

- replay lifecycle SHA256: `f34678fd6c85394ee659b6a710920bed8cc5ea07f8cbba0414cbb3bc116c79fb`.

## Counterexamples / safety gates

- synthetic `REOBSERVED -> ARCHIVE_FOR_NOW`: PASS;
- `ARCHIVE_FOR_NOW_DELETES_EVIDENCE NO`;
- uncommitted revalidation -> `WAIT_FOR_REVALIDATION`, no lifecycle mutation: PASS;
- conflicting committed revalidation -> WAIT, no lifecycle commit: PASS;
- partial lifecycle record ignored: PASS;
- lifecycle-state over-budget refusal: PASS;
- revalidation-state over-budget refusal: PASS;
- `STEP_LIMIT_STATUS=BOUNDED`.

## Immutability

Observed after testing:

- real survey SHA256: `de682a2d5a27e1985d2529106c5410f7e824dafbf5e7cb541485687166295d08`;
- real selected document SHA256: `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- real deep evidence SHA256: `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`;
- real revalidation SHA256: `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac`.

No admitted upstream evidence was mutated.

## Admitted claim

`NATIVE_STRUCTURAL_LIFECYCLE_DECISION=PROVEN_IN_REAL_SELECTED_DOCUMENT_SCOPE`

with proven branches:

- `NOT_REOBSERVED -> REVISIT`;
- `REOBSERVED -> ARCHIVE_FOR_NOW`;
- missing/uncommitted/conflicting evidence -> WAIT.

Claim limits remain:

- `REVISIT != SEMANTICALLY_FALSE`;
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`;
- `ARCHIVE_FOR_NOW != FORGET`;
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `BOUNDED_FILE_IO=NOT_PROVEN`;
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`;
- `HOST_LIFECYCLE_DECISION=NO`;
- `HOST_REVISIT_DECISION=NO`;
- `HOST_ARCHIVE_DECISION=NO`;
- `HOST_TRUTH_DECISION=NO`;
- `HOST_LEARNING=NO`.

## Next dependency

Build native V2.11 revisit execution + archive re-entry policy. Re-entry must be evidence-driven; do not fabricate age/semantic novelty signals not present in admitted state.
