# V2.14R.1 GENERATION-AWARE CLOSED LOOP — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

V2.13R.1 is admitted PASS in checkpoint `d464511977c85853d05c09419f3102d0fd0db88f`.

## Native capability A — generation-aware controller

File: `SIGMA_GENERATION_AWARE_CLOSED_LOOP_CONTROLLER_V2_14C1.sigma`

SHA256: `1db8cd24432b85a5b4d6125e1f26e657df6bf47c429d763eb255c12ce201d972`

Policy:

- latest `REVISIT`, generation == lifecycle cycle -> emit next-cycle `EXECUTE_REVISIT`;
- latest `REVISIT`, generation == lifecycle cycle + `|` -> emit current-generation `REVALIDATE_REVISIT_GENERATION`;
- latest `ARCHIVE_FOR_NOW`, matching generation -> `SELECT_NEXT_WORK`;
- inconsistent lifecycle-cycle/generation -> `WAIT_STATE_INCONSISTENT`, no event.

Event identity: `WORK::CYCLE::NEXT_STAGE`.

## Native capability B — event-driven revisit executor

File: `SIGMA_EVENT_DRIVEN_REVISIT_EXECUTOR_V2_14E1.sigma`

SHA256: `d6bd5e41813a6f2fc13b7c6bfa6215e01fe4aa11c12c0111e7b51addb9a11210`

Contract:

- accepts only `WORK::CYCLE::EXECUTE_REVISIT`;
- requires event cycle == completed generation cursor + `|`;
- persists exact-cycle structural evidence;
- evidence commits before segment cursor advance;
- generation advances only after document completion;
- wrong-cycle event refuses mutation.

## Admission runner — hardened identity

File: `RUN_SIGMA_V214R1_GENERATION_AWARE_CLOSED_LOOP_PREFLIGHT.sh`

Current SHA256: `da3c678089002e1fdb5694ed53eb9e1092462f20d2e1a0ff3fe390214556f226`

Earlier runner SHA `f1f4ff5fb571e4d4c56883860db9236073a1bc6dbd4c254b5471eec743ff2eec` is superseded before runtime admission because bounded refusal coverage was incomplete.

README: `SIGMA_V214R1_GENERATION_AWARE_CLOSED_LOOP_PREFLIGHT_README.txt`

Static checks:

- controller H-call arity PASS;
- executor H-call arity PASS;
- no native `!=` dependency;
- no `str_starts` dependency;
- no direct `str()` dependency;
- runner `bash -n` RC 0.

## Real bounded loop proof target

Starting admitted state:

- selected real work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- V2.11 completed revisit generation `|`;
- V2.13 generation-aware lifecycle `CYCLE=| ACTION=REVISIT`.

Required native transition:

1. controller -> `work::||::EXECUTE_REVISIT`;
2. mechanical host dispatcher routes exact event to native executor;
3. executor segment 0 / segment 1 / completion across fresh VM -> generation `||`;
4. controller -> `work::||::REVALIDATE_REVISIT_GENERATION`;
5. mechanical dispatcher routes exact event to admitted V2.13;
6. V2.13 -> `CYCLE=|| RESULT=NOT_REOBSERVED ACTION=REVISIT`;
7. controller -> distinct `work::|||::EXECUTE_REVISIT`.

Host may inspect only the exact emitted stage suffix and mechanically route it. Host must not choose stage, cycle, revalidation result, lifecycle action, document or segment.

## Required replay / negative / bounded gates

- fresh-VM event ledger reuse, no duplicate event append;
- deterministic replay from isolated mechanical clone of admitted V2.11 work-local state with exact controller/revalidation/lifecycle/evidence/generation hashes;
- wrong-cycle executor event refuses mutation;
- inconsistent generation-aware lifecycle cycle refuses event;
- controller lifecycle over-limit refusal;
- controller event-ledger over-limit refusal;
- executor evidence over-limit refusal;
- executor segment-cursor over-limit refusal;
- admitted V2.11 real evidence and real survey unchanged.

## Claim target after PASS

`AUTONOMOUS_STRUCTURAL_CYCLE_TRANSITION=PROVEN_IN_SELECTED_DOCUMENT_TWO_GENERATION_SCOPE`

Still not proven:

- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION`;
- multi-document autonomous cycle;
- semantic truth validation;
- semantic understanding;
- bounded file I/O;
- mid-append crash atomicity.

Keep V2.4 production learner running unchanged.
