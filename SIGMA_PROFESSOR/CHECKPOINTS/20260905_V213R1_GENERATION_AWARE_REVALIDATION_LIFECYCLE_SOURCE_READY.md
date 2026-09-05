# V2.13R.1 Generation-Aware Revalidation + Lifecycle — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Dependency

V2.12R.1 cycle event controller PASS checkpoint:
`cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`

## Canonical user-delivery identities

Native source:
`SIGMA_GENERATION_AWARE_REVALIDATION_LIFECYCLE_V2_13R1.sigma`

SHA256:
`8984a0beaefddb6656158eaed47080bc09955f79e9dcb0b59edcd2e0b670f107`

Runner:
`RUN_SIGMA_V213R1_GENERATION_AWARE_REVALIDATION_LIFECYCLE_PREFLIGHT.sh`

SHA256:
`2f68d6dd04a23ecd528fe06ea130f8d65adae4e557c32b5848c0e21998fb6ba0`

README:
`SIGMA_V213R1_GENERATION_AWARE_REVALIDATION_LIFECYCLE_PREFLIGHT_README.txt`

Static checks:

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n` RC = 0

## Capability contract

Input controller event:
`WORK::CYCLE::REVALIDATE_REVISIT_GENERATION`

Exact-cycle revisit evidence:
`WORK=<id> || GEN=<cycle> || CURSOR=<segment-cursor> || BEST_LOCAL_RELATION=<relation> || COMMIT=YES`

Generation-aware revalidation record:
`WORK=<id> || CYCLE=<cycle> || RESULT=<REOBSERVED|NOT_REOBSERVED> || BASELINE=<anchor> || COMMIT=YES`

Generation-aware lifecycle record:
`WORK=<id> || CYCLE=<cycle> || ACTION=<REVISIT|ARCHIVE_FOR_NOW> || FROM_RESULT=<result> || COMMIT=YES`

Native structural policy:

- compare the committed V2.5 survey baseline only with committed revisit evidence for the exact event cycle;
- matching exact-cycle segment -> `REOBSERVED`;
- committed exact-cycle evidence with no matching baseline -> `NOT_REOBSERVED`;
- `NOT_REOBSERVED -> REVISIT`;
- `REOBSERVED -> ARCHIVE_FOR_NOW`.

## Real expected branch

Selected work:
`0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`

V2.12 must regenerate event:
`0ac783...66485b::|::REVALIDATE_REVISIT_GENERATION`

Cycle `|` V2.11 evidence:

- `in => the`
- `As => disagreements`

V2.5 baseline:
`of => the`

Expected V2.13 real result:
`CYCLE=| -> NOT_REOBSERVED -> REVISIT`

## Admission gates

- exact real V2.12 event regeneration;
- real cycle `|` revalidation/lifecycle;
- fresh VM state reuse/no duplicate append;
- deterministic replay;
- synthetic cycle `||` coexists with seeded cycle `|` state;
- synthetic cycle `||` `REOBSERVED -> ARCHIVE_FOR_NOW`;
- partial/uncommitted matching evidence ignored;
- wrong controller stage refuses state mutation;
- exact-cycle conflicting committed revalidation blocks mutation;
- survey/evidence/revalidation/lifecycle bounds refuse mutation;
- real upstream survey and revisit evidence immutable.

## Claim limits before runtime

- `GENERATION_AWARE_REVALIDATION=NOT_PROVEN`
- `GENERATION_AWARE_LIFECYCLE=NOT_PROVEN`
- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

## Repository hygiene note

A noncanonical compact rendering of the V2.13 source was briefly written to the branch and then removed in commit `ae3b9a4cae2844a7c430b371076f30e06aa9e3a3`. It must not be used as the candidate identity. The canonical admission identity is exclusively the SHA256 `8984a0be...f107` user-delivery source above.
