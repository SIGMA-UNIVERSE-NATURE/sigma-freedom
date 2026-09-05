# V2.9R.1A oracle-repaired structural revalidation — PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: SIGMA_LIFE

## Runtime identities

- SIGMAC SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- V2.8R.1 source SHA256: `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`
- V2.8R.1 bytecode SHA256: `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`
- V2.8D.1 source SHA256: `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`
- V2.8D.1 bytecode SHA256: `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`
- V2.9R.1 source SHA256: `94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`
- V2.9R.1 bytecode SHA256: `c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8`
- Oracle-repaired runner SHA256: `027288207db6e52e087d7d9cb2eea262989c6afdb657af01f37d1824fe9c7717`

## Failure evidence retained

The first V2.9R.1 admission runner incorrectly hardcoded the real baseline anchor as `in => the` and expected real `REOBSERVED`. Runtime evidence showed the actual committed V2.5B.2 baseline for selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b` is `of => the`; therefore native V2.9R.1 correctly returned `NOT_REOBSERVED`.

Failure checkpoint commit: `1cec7703a3cc9a730a5dd28155cb2d9c558441a8`.

The native source was not weakened or modified to force PASS. Only the admission oracle was repaired so the real native outcome could be either `REOBSERVED` or `NOT_REOBSERVED`, with both branches independently tested using synthetic fixtures.

## Real runtime evidence

Native selected work:
`0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`

Regenerated real deep evidence:
- SHA256 `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`
- committed record count = 2
- deep segment anchors: `in => the`; `As => disagreements`

Real structural revalidation:
- `DEEP_RELEARN_COMPLETE 1`
- `ACTIVE_WORK_MATCH 1`
- `BASELINE_FOUND 1`
- `BASELINE_ANCHOR of => the`
- `COMMITTED_DEEP_SEGMENT_COUNT 2`
- `MATCHING_BASELINE_SEGMENT_COUNT 0`
- `DISTINCT_DEEP_ANCHOR_COUNT 2`
- `REVALIDATION_READY 1`
- `REVALIDATION_RESULT NOT_REOBSERVED`
- `REVALIDATION_APPEND_RC 0`
- real revalidation state SHA256 `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac`

Fresh VM reuse:
- same baseline and `NOT_REOBSERVED`
- `REVALIDATION_ALREADY_COMMITTED 1`
- state SHA unchanged

Deterministic replay:
- same native result
- same state SHA `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac`

Synthetic branch coverage:
- completed positive fixture -> `REOBSERVED`
- completed counterexample -> `NOT_REOBSERVED`
- incomplete deep re-learn -> `PENDING`, no revalidation readiness
- partial matching evidence without `COMMIT=YES` ignored

Boundedness:
- state over-limit -> mutation refused
- evidence over-limit -> mutation refused
- survey over-limit -> mutation refused
- `STEP_LIMIT_STATUS=BOUNDED`

Immutability:
- real survey SHA after = `de682a2d5a27e1985d2529106c5410f7e824dafbf5e7cb541485687166295d08`
- selected document SHA after = `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
- regenerated deep evidence SHA after = `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`

## Admission

`V29R1A_ORACLE_REPAIRED_STRUCTURAL_REVALIDATION_ADMISSION=PASS`

Admitted claims:
- `NATIVE_STRUCTURAL_REVALIDATION=PROVEN_IN_SELECTED_DOCUMENT_SCOPE`
- `PERSISTENT_REVALIDATION_STATE_REUSE=PASS`
- `DETERMINISTIC_REVALIDATION_REPLAY=PASS`
- `SYNTHETIC_REOBSERVED_BRANCH=PASS`
- `NEGATIVE_NOT_REOBSERVED=PASS`
- `INCOMPLETE_DEEP_RELEARN_BLOCKS_REVALIDATION=PASS`
- `PARTIAL_EVIDENCE_COMMIT_FILTER=PASS`
- `STEP_LIMIT_STATUS=BOUNDED`

Host boundary:
- `HOST_REVALIDATION_DECISION=NO`
- `HOST_TRUTH_DECISION=NO`
- `HOST_LEARNING=NO`

Still not proven:
- semantic truth validation;
- semantic understanding;
- bounded file I/O;
- mid-append crash atomicity.

`NEXT_ACTION=BUILD_REVALIDATION_TO_REVISIT_OR_ARCHIVE_FOR_NOW_PREFLIGHT`
