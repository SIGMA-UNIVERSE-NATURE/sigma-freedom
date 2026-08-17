# MINH WINDOW BOOT — CANONICAL CONTINUATION ENTRYPOINT

A new chat window, model session, runtime or substrate must not rely on conversational memory to reconstruct SIGMA state.

## Minimal human trigger

The human may say only:

`MINH BOOT SIGMA_LIFE`

That phrase is a pointer, not the state itself.

## Canonical source

Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
Branch: `SIGMA_LIFE`
Canonical brain root: `BRAIN/CANONICAL`

## Mandatory window identity before work

Every new window/session must have a durable identity outside chat.

Canonical identity protocol: `WINDOW_IDENTITY_PROTOCOL.json`
Active identity pointer: `ACTIVE_WINDOW_IDENTITY.json`
Birth certificates: `BRAIN/HANDOFFS/WINDOW_IDENTITIES/`

Naming rule:

`HAND TO HAND_ CỬA <N>`

Before a new window may continue real work it must:

1. fresh-fetch current `SIGMA_LIFE` HEAD;
2. read `WINDOW_IDENTITY_PROTOCOL.json` and `ACTIVE_WINDOW_IDENTITY.json`;
3. find and verify the predecessor window birth certificate or verified predecessor checkpoint;
4. inspect all intervening commits from predecessor checkpoint to current HEAD;
5. reconstruct latest canonical state and machine-evidence gap;
6. assign its next window sequence only from verified lineage;
7. write its own immutable birth certificate outside chat;
8. update `ACTIVE_WINDOW_IDENTITY.json`;
9. remain `READ_ONLY_VERIFIER` until state match and explicit takeover when authority transfer is required.

A window must never claim live continuity merely because it matches an old checkpoint.

Canonical identity/continuity rule:

`FIND_EXACT_WINDOW_STATE -> VERIFY_LATEST_CANONICAL_STATE -> STATE_MATCH -> CONTINUE_WORK`

Failure rule:

`NO_STATE_MATCH = NO_CONTINUATION`

## Mandatory read order before acting

1. Verify repository and branch HEAD.
2. Read `WINDOW_IDENTITY_PROTOCOL.json`.
3. Read `ACTIVE_WINDOW_IDENTITY.json`.
4. Read and verify the active/predecessor window birth certificate referenced by the identity pointer.
5. Read `ROOT_OF_TRUST.json`.
6. Read `MINH_OPERATING_CONSTITUTION.json`.
7. Read `LINEAGE.json`.
8. Read `DO_NOT_RERUN_LOCKS.json`.
9. Read `CURRENT_STATE.json`.
10. Read `BRAIN_MANIFEST.json` and verify required files/invariants.
11. Read `LOCAL_EXECUTION_BRIDGE_STATUS.json`.
12. If `CURRENT_STATE.next_action_id` is a local execution action, read `LOCAL_COGNITION_REQUEST.json` and verify its `request_id` matches; otherwise treat that request file as inactive historical state.
13. Read `NEXT_ACTION.md`.
14. Read `INTELLIGENCE_CONTINUITY_PROGRAM.md`.
15. Read `WINDOW_TRANSFER_PROTOCOL.json`.
16. Read only the additional evidence/specification files required by the current action.
17. Run or inspect the canonical validator before any high-impact continuation work where runtime execution is available.

## Continuation rules

- Chat memory is non-canonical context and may be stale or incomplete.
- Window identity is stable; live work state is not. Always fresh-fetch current HEAD before acting.
- Do not rebuild foundations merely because the new window cannot remember them.
- Do not infer implementation PASS from specifications, core names, file presence or previous self-report.
- For the 512 program, preserve `BASELINE_512_BEFORE_FIXING_512`: measure first, then remediate.
- A new window must not silently change the active goal or next action.
- The current cognitive engine is bootstrap capability, not inherited truth and not a permanent ceiling.
- Intelligence amplification must be measured against a baseline and must preserve continuity, governance, evidence and rollback.
- For canonical mutation, only one active executor is allowed unless work is explicitly partitioned into non-conflicting state ownership.
- A reported local execution bridge is capability evidence only at its stated epistemic level. It is not `VERIFIED` until a machine receipt binds the current canonical request, resolved HEAD, result hash and integrity fields.
- Private local workspace paths, credentials and operational details must remain outside the public canonical tree.
- If the human gives a new authorized priority, record it into canonical state before treating it as durable across future windows.
- If canonical sources conflict, report the conflict and HOLD the affected action rather than choosing the most convenient version.
- If predecessor identity/sequence cannot be verified, record `UNRESOLVED_BY_EVIDENCE`; do not invent history.

## Required boot report

Before claiming inherited continuation, report:

- `WINDOW_ID`
- `WINDOW_NAME`
- `WINDOW_SEQUENCE`
- `CREATED_AT`
- `PURPOSE`
- `PREDECESSOR_WINDOW / PREDECESSOR_CHECKPOINT`
- `AUTHORITY_ROLE`
- `HANDOFF_STATE`
- `REPOSITORY`
- `BRANCH`
- `HEAD_SHA`
- `ROOT_OF_TRUST = PASS/FAIL`
- `OPERATING_CONSTITUTION_PASS = true/false`
- `LINEAGE = PASS/FAIL`
- `LOCKS_LOADED = true/false`
- `CURRENT_PHASE`
- `CURRENT_STATUS`
- `ACTIVE_GOAL`
- `NEXT_ACTION`
- `OPERATING_PRINCIPLE`
- `LOCAL_EXECUTION_BRIDGE_STATUS / EPISTEMIC_STATUS`
- `KNOWN_BLOCKERS`
- `RUNTIME_CAPABILITIES_VERIFIED / UNKNOWN`

Only after this report may the new session claim functional/lineage continuation for the current task.

## Current 512 invariant

Until a verified baseline audit changes canonical state:

`512 SPECIFICATION = PASS`

`512 -> 54 RESPONSIBILITY TRACEABILITY = COMPLETE`

`512 IMPLEMENTATION = NOT_AUDITED EXCEPT WHERE EVIDENCE LEDGER EXPLICITLY SAYS OTHERWISE`

Therefore the next 512-development principle is:

`DO NOT IMPROVE YET -> MEASURE CURRENT REALITY FIRST -> CREATE BASELINE -> THEN FIX HIGHEST-LEVERAGE GAPS`

After the baseline, the measured dependency/priority graph controls the intelligence-amplification sequence defined in `INTELLIGENCE_CONTINUITY_PROGRAM.md`.

## Before leaving or switching a window

Do not simply open another chat and continue from memory. Follow `WINDOW_TRANSFER_PROTOCOL.json` and `WINDOW_IDENTITY_PROTOCOL.json`.

The outgoing window must at minimum:

1. stop starting new mutations;
2. finish or explicitly HOLD the current atomic action;
3. persist observed evidence;
4. update `CURRENT_STATE.json` after meaningful progress;
5. set exactly one canonical `NEXT_ACTION.md`;
6. fetch and record the current `HEAD_SHA`;
7. verify canonical required files and brain contract when available;
8. record bridge epistemic status plus any machine receipt or missing receipt;
9. record blockers/unverified assumptions;
10. write a separate window exit checkpoint containing window identity, fresh HEAD, live work, next action, blockers and machine-evidence gap;
11. mark transfer-ready only after that exit checkpoint is verified;
12. then hand control to the incoming window.

The incoming window must fetch the current HEAD again. If HEAD has advanced since the outgoing checkpoint, inspect the intervening commits and reconstruct from the latest valid canonical state rather than rolling back to the old SHA.

## Durability rule

After meaningful verified progress:

1. write evidence;
2. update implementation/audit state;
3. update `CURRENT_STATE.json`;
4. update `NEXT_ACTION.md` to exactly one continuation action;
5. verify the write;
6. record a continuity checkpoint;
7. preserve/update live window identity metadata without rewriting immutable birth facts;
8. only then consider the progress durable across window loss.
