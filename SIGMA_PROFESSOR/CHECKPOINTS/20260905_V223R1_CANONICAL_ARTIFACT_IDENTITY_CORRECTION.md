# V2.23R.1 — CANONICAL ARTIFACT IDENTITY CORRECTION

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Status: AUDIT CORRECTION / SOURCE READY / NOT RUNTIME-ADMITTED

The earlier V2.23 source-ready checkpoint recorded a SHA256 from a local candidate runner. During repository audit, the committed repository artifact was found to be not byte-identical to that local candidate.

The local candidate SHA256 must therefore be treated as NONCANONICAL and MUST NOT be used for admission.

## Canonical runner

Repository path:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V223R1_JOURNAL_WRAPPED_REAL_SHADOW_SCHEDULED_INTENT_PREFLIGHT.sh`

Canonical Git blob SHA:
`c4d2c9790d505041ee71cfaafaf77365af790865`

Original artifact commit:
`7bacdf5909f70799643de888d2b7c57155980fe7`

Corrected README commit:
`445b9dfc7d36bde14428c04be9a60af482bbfd16`

## Admission identity procedure

Before running V2.23 on Termux:

1. update the repository branch;
2. verify `git hash-object` of the runner equals the canonical Git blob SHA above;
3. run `sha256sum` on that exact canonical file;
4. preserve the SHA256 in the runtime transcript;
5. only that Termux-observed SHA256 may be frozen as the canonical runner SHA256 in the V2.23 PASS checkpoint.

Do not infer SHA256 from the earlier local candidate.

## STOP-GATE

No change to native-only execution policy:

- `HOST_TRANSACTION_DECISION=NO`
- `HOST_RECOVERY_DECISION=NO`
- `HOST_FAIRNESS_DECISION=NO`
- `HOST_STAGE_DECISION=NO`
- `HOST_WORK_SELECTION=NO`
- `HOST_REVISIT_PRIORITY=NO`
- `HOST_LEARNING=NO`

Fault injection remains mechanical. Native V2.22 decides recovery validity.

## Claim status

`V223R1_RUNTIME_ADMISSION=NOT_YET_RUN`

`PRODUCTION_PROMOTION_ALLOWED=NO`

This correction changes artifact identity bookkeeping only. It does not weaken or change any capability gate.
