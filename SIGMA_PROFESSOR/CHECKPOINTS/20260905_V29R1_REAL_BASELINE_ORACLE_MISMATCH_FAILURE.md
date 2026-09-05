# V2.9R.1 REAL BASELINE ORACLE MISMATCH — FAILURE EVIDENCE

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: SIGMA_LIFE
Working repo on device: `~/SIGMA/sigma-freedom-write`

## Locked runtime identities

- SIGMAC SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

## Candidate identities

- V2.8R.1 bridge source SHA256: `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`
- V2.8R.1 bridge bytecode SHA256: `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`
- V2.8D.1 deep source SHA256: `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`
- V2.8D.1 deep bytecode SHA256: `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`
- V2.9R.1 source SHA256: `94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`
- V2.9R.1 bytecode SHA256 observed: `c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8`

## Real native chain before failure

Native curriculum selected:
`0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`

Exact D1 regenerated real evidence:
- evidence SHA256 `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`
- committed evidence records = 2
- segment 0 best local relation = `in => the`
- segment 1 best local relation = `As => disagreements`
- deep re-learn complete at segment index 2

## Observed V2.9R.1 real revalidation

`VM_RC=0`

Native V2.9R.1 produced:

- `BASELINE_FOUND 1`
- `BASELINE_ANCHOR of => the`
- `COMMITTED_DEEP_SEGMENT_COUNT 2`
- `MATCHING_BASELINE_SEGMENT_COUNT 0`
- `DISTINCT_DEEP_ANCHOR_COUNT 2`
- `REVALIDATION_READY 1`
- `REVALIDATION_RESULT NOT_REOBSERVED`
- `REVALIDATION_APPEND_RC 0`
- `HOST_REVALIDATION_DECISION NO`
- `HOST_TRUTH_DECISION NO`
- `HOST_LEARNING NO`
- `SEMANTIC_TRUTH_VALIDATION NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING NOT_PROVEN`

## Failure diagnosis

The native revalidation result is internally consistent with the admitted real data.

The failure was in the runner test oracle. The runner incorrectly hardcoded:

`EXPECTED_REAL_BASELINE='in => the'`

for selected document `0ac783...66485b`.

The actual committed V2.5B.2 survey baseline for that document is:

`of => the`

Therefore the correct real structural result from the current native policy is:

`NOT_REOBSERVED`

because neither committed deep segment best anchor equals `of => the`.

This is not a reason to rewrite SIGMA output to force `REOBSERVED`.

## Admission consequence

`V29R1_DEEP_RELEARN_STRUCTURAL_REVALIDATION_PREFLIGHT=FAIL`

Reason:
`RUNNER_ORACLE_HARDCODE_MISMATCH`

Preserve all runtime state and logs.

The native V2.9R.1 algorithm is not disproven by this failure, but the admission package is not PASS because the test oracle was wrong.

## Required repair

Repair the runner/admission design so that:

1. the real baseline outcome is derived from actual committed survey/deep evidence, not predeclared as `REOBSERVED`;
2. the real path may legitimately yield either `REOBSERVED` or `NOT_REOBSERVED`;
3. deterministic fresh-VM reuse and replay are checked against the native real result actually observed;
4. separate synthetic positive and negative cases prove both revalidation branches;
5. incomplete deep-relearn, partial evidence filtering, and bounded refusal gates remain unchanged;
6. no semantic truth claim is introduced.

`HOST_REVALIDATION_DECISION=NO`
`HOST_TRUTH_DECISION=NO`
`HOST_LEARNING=NO`
`SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`
`SEMANTIC_UNDERSTANDING=NOT_PROVEN`
