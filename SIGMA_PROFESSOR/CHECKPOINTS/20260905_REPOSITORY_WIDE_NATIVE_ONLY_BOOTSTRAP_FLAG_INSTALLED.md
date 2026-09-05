# CHECKPOINT — REPOSITORY-WIDE NATIVE-ONLY BOOTSTRAP FLAG INSTALLED

Date: 2026-09-05 Asia/Ho_Chi_Minh

Status: INSTALLED / MANDATORY / REPOSITORY-WIDE

## Purpose

Make every new SIGMA development window/session/agent encounter the native execution boundary before doing work.

## Installed flags

### Root bootstrap

`/AGENTS.md`

Commit:
`c737721739e9e2fa368bac05fcf592f5146fd1b2`

### Canonical bootstrap directive

`SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`

Commit:
`a6a6856a4b233ef47378096f5909b9b084de9485`

### SIGMA_PROFESSOR README entry gate

`SIGMA_PROFESSOR/README.md`

Commit:
`209f4c1192417937ed2c2e0974dfb99b3de2d4e2`

### Current handoff STOP-GATE

`SIGMA_PROFESSOR/CURRENT_HANDOFF.md`

Commit:
`5cef391ad4d2514c624b5f76c68826d495aeadb3`

The handoff update preserved the concurrently added `TEACHER_GPT language lane pointer` and the existing V2.22 frontier.

## Mandatory rules now surfaced at repository entry

- `SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`
- `ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`
- `ACTIVE_COGNITION_NATIVE_SIGMA_ONLY=YES`
- `HOST_OR_BASH_AS_SIGMA_EXECUTION_ENGINE=FORBIDDEN`
- `HOST_OR_BASH_COGNITION=FORBIDDEN`
- `HOST_OR_BASH_LEARNING=FORBIDDEN`
- `HOST_OR_BASH_SEMANTIC_INTERPRETATION=FORBIDDEN`
- `HOST_OR_BASH_STAGE_DECISION=FORBIDDEN`
- `HOST_OR_BASH_WORK_SELECTION=FORBIDDEN`
- `HOST_OR_BASH_REVISIT_PRIORITY=FORBIDDEN`
- `HOST_OR_BASH_TRUTH_DECISION=FORBIDDEN`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`

## Bash/host boundary

Bash/host is not SIGMA and cannot implement a SIGMA capability.

Allowed only as mechanically transparent external harness when unavoidable:

- invoke locked sigmac/VM;
- exact bytes/files;
- hashes/return codes;
- isolated fixtures/fault injection;
- process supervision/transport;
- exact dispatch of an event/stage already emitted by native SIGMA.

It may not choose, rewrite, semantically interpret, prioritize, or compute that event/stage/result.

- `BASH_MAY_LAUNCH_SIGMA=YES`
- `BASH_MAY_IMPLEMENT_SIGMA_CAPABILITY=NO`
- `HOST_MAY_DISPATCH_EXACT_NATIVE_EVENT=MECHANICAL_ONLY`
- `HOST_MAY_CHOOSE_EVENT_OR_STAGE=NO`

If host/Bash computes a decision required for an admission gate, the gate fails.

## Conflict policy

Any historical artifact or runner that conflicts with this bootstrap flag is historical evidence/provenance only. Do not weaken the current directive to preserve old behavior.

## Production remains unchanged

- `PRODUCTION_V2_4_KEEP_RUNNING=YES`
- `STOP_ONLY_ON_REAL_VM_FAILURE=YES`
- `UPGRADE_V2_4_IN_PLACE=NO`

This checkpoint changes governance/bootstrap visibility only. It does not mutate production learner memory and does not admit a new SIGMA capability.
