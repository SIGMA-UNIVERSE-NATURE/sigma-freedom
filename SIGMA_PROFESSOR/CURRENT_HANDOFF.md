# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## Mandatory standard

Read first: `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`.

Global invariants:

- active cognition = native `.sigma` only;
- `HOST_LEARNING=NO`;
- `HOST_SEMANTIC_INTERPRETATION=NO`;
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`;
- runtime proof required; compile/file existence alone is insufficient;
- failures are evidence; never weaken an admission gate to force PASS;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `SEMANTIC_CURIOSITY=NOT_PROVEN`;
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_MATHEMATICAL_RESEARCH=NOT_PROVEN`.

## Locked runtime

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

## Production

Keep V2.4 production learner running unless it emits a real VM failure.

Production source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

Do not upgrade V2.4 in place while the new continual-learning chain is still under admission.

## Admitted continual-learning chain

- V2.5B.2 frozen 56-document survey: PASS — checkpoint `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6 persisted segment cursor restart: PASS — `81c8c72e66c30292e17c567d8c3824490dc00e7a`.
- V2.6F full fixture traversal: PASS — `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7/P.1 structural grouping: PASS — checkpoint `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 structural curriculum priority: PASS — `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real survey -> native selected frontier: PASS — source `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`, bytecode `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`, checkpoint `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected work -> deep re-learn: PASS — source `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`, bytecode `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`, deep evidence `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`, checkpoint `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A structural revalidation: PASS — source `94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`, bytecode `c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8`, real baseline `of => the`, real result `NOT_REOBSERVED`, state `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac`, PASS checkpoint `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 lifecycle decision: PASS — source `67fb7234c0cd9e84c602a6dadb55f6e1ced6265406745ba6b3b9a7a95e0c4993`, bytecode `527bf0513082af49343f39b5ae23fd63b5c25f4034e019e934ca1d425890ef87`, real `NOT_REOBSERVED -> REVISIT`, lifecycle state `f34678fd6c85394ee659b6a710920bed8cc5ea07f8cbba0414cbb3bc116c79fb`, checkpoint `220fa78bce0d9873533cb8acce102fc411107924`.
- V2.11R.1 revisit execution + archive re-entry: PASS.
  - native source SHA256 `88568071e657cb94845d97d94237688ec62d88121f6ff90dc8cbc96cbe685d9e`;
  - repaired runner SHA256 `31005526c5ec1a4c33ec1759965b9810e19198fae08235dc1ca16d8c5c739907`;
  - real selected-document revisit generation executes segment 0 then fresh-VM segment 1 then fresh-VM completion;
  - work-local generation/cursor/evidence state PASS;
  - deterministic replay PASS;
  - archive hold without deletion PASS;
  - later committed REVISIT re-enters archive PASS;
  - wait/no lifecycle PASS;
  - lifecycle/evidence/generation-cursor/segment-cursor bounded refusal PASS;
  - generation cursor 65 pipes -> split parts 66 -> refusal PASS;
  - segment cursor 65 pipes -> split parts 66 -> refusal PASS;
  - failure runner-fixture checkpoint `f05ca0b5029a8436e95a9caecdfb93fc4cb32b9e` preserved;
  - PASS checkpoint `aa1bec9344510d95dbbee9312076df7ad9975256`.

## Important distinctions

- `DISPATCHED != COMPLETE`;
- `REOBSERVED != SEMANTICALLY_TRUE`;
- `NOT_REOBSERVED != SEMANTICALLY_FALSE`;
- `REVISIT != SEMANTICALLY_FALSE`;
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`;
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.12R.1 native cycle event controller — SOURCE READY

Purpose: add a persistent native stage-decision layer and explicit cycle/event identity before claiming a general autonomous continual-learning loop.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_AUTONOMOUS_CYCLE_EVENT_CONTROLLER_V2_12R1.sigma`

Source SHA256:
`ec367a6c780011fc7fe06e7fafbdcfde27198527565bd9054c733e79ecc115be`

Source artifact commit:
`07cd0329e8a443e621a912473f64927c9ec61d6a`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V212R1_AUTONOMOUS_CYCLE_EVENT_CONTROLLER_PREFLIGHT.sh`

Runner SHA256:
`02be167cd7d302c72735e384532310a347edbaf0d1827ec748f4b635a660910c`

Runner commit:
`58b093f42abf7bb1d2eb6fab1780940476beb5bb`

README commit:
`2946cd3e57eebc23acd81f2ff9d7f36ea456cc94`

Source-ready checkpoint:
`9af1145ee7f6bc2ccc77045e40f070e2dfc3ff3c`

### Native stage policy under admission

- no committed lifecycle -> `WAIT_FOR_LIFECYCLE`;
- latest `ARCHIVE_FOR_NOW` -> `SELECT_NEXT_WORK`;
- pending revisit generation -> `EXECUTE_REVISIT`;
- completed revisit generation -> `REVALIDATE_REVISIT_GENERATION`;
- completed generations greater than admitted revisit events -> `WAIT_STATE_INCONSISTENT`.

Explicit controller event identity:
`EVENT_ID = WORK + "::" + CYCLE_TOKEN + "::" + NEXT_STAGE`.

Persistent event record:
`WORK=<id> || CYCLE=<token> || NEXT=<stage> || EVENT=<event-id> || COMMIT=YES`.

### Real expected state

From admitted V2.11 persistent real state:

- selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- V2.10 lifecycle action `REVISIT`;
- V2.11 completed generation cursor `|`;
- segment cursor empty.

Expected native V2.12 event:
`0ac783...66485b::|::REVALIDATE_REVISIT_GENERATION`.

### Admission gates prepared

- real persisted V2.11 state -> revalidation event;
- fresh VM persistent event reuse/no duplicate append;
- deterministic replay;
- pending revisit -> `EXECUTE_REVISIT`;
- cycle `|` and `||` produce distinct event IDs;
- initial archive -> `SELECT_NEXT_WORK`;
- no lifecycle -> WAIT/no event;
- inconsistent generation state -> no event;
- partial lifecycle filter;
- lifecycle/controller/generation/segment bounded refusal.

Static truth:

- `H_CALL_ARITY_AUDIT=PASS`;
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`;
- `STR_STARTS_DEPENDENCY=NONE`;
- `DIRECT_STR_DEPENDENCY=NONE`;
- runner `bash -n` RC = 0.

### Claim limits

- V2.12 runtime admission = `NOT_PROVEN` until actual locked-VM run;
- `GENERATION_AWARE_REVALIDATION=NOT_PROVEN`;
- `GENERATION_AWARE_LIFECYCLE=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `BOUNDED_FILE_IO=NOT_PROVEN`;
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`.

## Other lanes

54 DNA directive:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Advanced mathematics program:
`SIGMA_PROFESSOR/DESIGN/SIGMA_ADVANCED_MATHEMATICS_BEYOND_CAPABILITY_PROGRAM_V1.md`

Keep all 54 DNA; active cognition remains native `.sigma`; no Python cognition.

## NEXT ACTION

1. Keep V2.4 production learner running unless it emits a real VM failure.
2. From repo root `~/SIGMA/sigma-freedom-write`, install exact V2.12 source + runner identities above.
3. Run locked sigmac/VM; preserve V2.12 bytecode SHA, event state hash, selected event and all VM_RC outputs.
4. If any gate fails, preserve evidence and repair only the narrow failure.
5. If PASS, checkpoint V2.12 before building generation-aware revalidation + lifecycle keyed by V2.12 cycle/event identity.
6. Do not claim a general autonomous cycle until generation-aware revalidation/lifecycle and dispatcher integration pass.
