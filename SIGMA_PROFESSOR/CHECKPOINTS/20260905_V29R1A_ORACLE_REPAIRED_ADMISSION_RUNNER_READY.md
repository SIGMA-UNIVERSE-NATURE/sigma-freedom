# V2.9R.1A ORACLE-REPAIRED ADMISSION RUNNER — READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

This checkpoint follows the preserved failure:
`20260905_V29R1_REAL_BASELINE_ORACLE_MISMATCH_FAILURE.md`

## Repair principle

Do not modify native V2.9R.1 output to force `REOBSERVED`.
The native source remains unchanged.

Native source SHA256:
`94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`

Observed native bytecode SHA256 from the failed admission run:
`c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8`

Repaired runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V29R1A_ORACLE_REPAIRED_STRUCTURAL_REVALIDATION_ADMISSION.sh`

Runner SHA256:
`027288207db6e52e087d7d9cb2eea262989c6afdb657af01f37d1824fe9c7717`

Static runner check:
`bash -n = PASS`

## Admission changes

- hardcoded real baseline expectation removed;
- hardcoded real `REOBSERVED` expectation removed;
- real native result may be `REOBSERVED` or `NOT_REOBSERVED`;
- fresh VM must reuse exact real native result + baseline without duplicate mutation;
- deterministic replay must reproduce exact state hash;
- synthetic positive explicitly proves the `REOBSERVED` branch;
- synthetic negative explicitly proves the `NOT_REOBSERVED` branch;
- incomplete deep re-learn, partial evidence filter, state/evidence/survey bounds remain required.

This is an oracle repair, not a PASS-criteria weakening.
The native decision remains inside SIGMA.

`HOST_REVALIDATION_DECISION=NO`
`HOST_TRUTH_DECISION=NO`
`HOST_LEARNING=NO`
`SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`
`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

Current admission:
`V29R1A_ADMISSION=NOT_PROVEN_UNTIL_LOCKED_RUNTIME_PASS`
