# V2.19R.1 Native Revisit Fairness / Anti-Starvation — Source Ready

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Dependency

V2.18 shadow audit checkpoint:
`1e07738afce2bd5f111eb7861ebcdcdf3ab4472c`

V2.18 proved production promotion is blocked by immediate consecutive revisit starvation risk.

## Native candidate

Source:
`SIGMA_PROFESSOR/artifacts/SIGMA_REVISIT_FAIRNESS_ANTI_STARVATION_SCHEDULER_V2_19R1.sigma`

Source SHA256:
`e0734dbbdb6f0bad3d6577f9a9b20eb3a13dd9c3489caebd7f6f58bb15200ad0`

Source artifact commit:
`a03ec1d456c2e75b1ac251fbfdf0c7c0f03f0823`

User-delivery runner:
`RUN_SIGMA_V219R1_REVISIT_FAIRNESS_ANTI_STARVATION_PREFLIGHT.sh`

Runner SHA256:
`e390445d0fd7439043ea3fb75c90661d78fb0321245b2c81d959f508370dd8e1`

## Capability contract

Persistent fairness ledger:
`EVENT=<exact event> || STATUS=<PENDING|RESUMED> || AT=<dispatch-token> || COMMIT=YES`

Native structural policy:

- immediate `EXECUTE_REVISIT` is deferred while committed survey work remains undispatched;
- exact revisit event is persisted as PENDING, never discarded;
- dispatch token is generated natively as one `|` per unique committed selector dispatch;
- a pending revisit matures only after selector dispatch progress and a scheduling turn from a different work;
- oldest mature pending revisit resumes first;
- if the current different work also needs revisit, that current event is persisted before the older pending revisit resumes;
- when no undispatched alternative remains, revisit executes;
- host chooses neither fairness decision nor revisit priority.

This is not a hardcoded revisit-count quota.

## Admission gates

- exact real V2.18 starvation event against real 56-document survey -> defer to SELECT_NEXT_WORK;
- fresh VM reuse with no duplicate pending record;
- synthetic A/B/C oldest-pending queue rotation;
- current revisit not lost when an older revisit resumes;
- deterministic full queue replay with exact fairness-ledger hash;
- selector/survey inconsistency refusal;
- no-alternative revisit execution;
- SELECT_NEXT_WORK passthrough;
- partial fairness record filter;
- invalid stage refusal;
- survey/selector/fairness bounded refusals.

Static:

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n` RC = 0

## Claim limits

Before locked-runtime PASS:

- `NATIVE_REVISIT_FAIRNESS_QUEUE=NOT_PROVEN`
- `REAL_SHADOW_ANTI_STARVATION_INTEGRATION=NOT_PROVEN`
- `PRODUCTION_PROMOTION_ALLOWED=NO`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

## Next action

Install exact source/runner hashes, run locked sigmac + VM v09, preserve all output and state hashes. If PASS, checkpoint V2.19 before integrating fairness into the real shadow-production chain.
