SIGMA V2.21R.1 — LONG-HORIZON SHADOW STABILITY + RECOVERY

Purpose:
Extend the admitted V2.20 fairness integration through six persisted fairness scheduling boundaries and at least four real works, without changing production V2.4.

The gate starts from clean isolated shadow state and replays:
1. real first-work starvation event -> fairness defer;
2. real second work complete cycle -> resume exact first revisit cycle |||;
3. first cycle ||| complete -> fairness redefer cycle |||| -> real third work;
4. admitted real third work REOBSERVED -> ARCHIVE_FOR_NOW -> fairness resumes first cycle ||||;
5. first cycle |||| completes; its new branch is NOT hardcoded, but fairness must turn the terminal event into SELECT_NEXT_WORK so the real fourth work is selected;
6. real fourth work completes initial deep/revalidation/lifecycle with NO branch oracle;
7. its terminal event passes through fairness and is persisted as the long-horizon continuation intent.

At each extended scheduling boundary the persisted scheduled-event file is read back by a fresh host process before dispatch/acceptance.

Required stability evidence:
- >= 4 real selector dispatch records;
- >= 2 PENDING fairness records;
- >= 2 RESUMED fairness records;
- exact pending cycle identity survives recovery;
- production V2.4 runner PID is unchanged;
- shadow BRAIN remains isolated.

The first/second/third deterministic branches used as replay inputs were already admitted in earlier runtime checkpoints.
The first generation-|||| branch and fourth-work branch are deliberately not hardcoded.

Claim after PASS:
LONG_HORIZON_SHADOW_STABILITY=PROVEN_IN_SIX_BOUNDARY_FOUR_REAL_WORK_SCOPE

Promotion still remains blocked because the current host ABI does not prove mid-append crash atomicity.

Runner SHA256:
c6ab9129af4692c4e134c39b088917c047864ccbf977a5314c0dc0f9322b0f3d

Static:
BASH_N_RC=0
