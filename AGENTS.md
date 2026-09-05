# SIGMA REPOSITORY BOOTSTRAP — READ BEFORE ANY WORK

This file is the repository-wide entry flag for every development window/session/agent.

## Mandatory first reads

Before inspecting, modifying, testing, teaching, integrating, or promoting SIGMA, read in this order:

1. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
3. `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
4. latest relevant file in `SIGMA_PROFESSOR/CHECKPOINTS/`

Do not begin implementation before those files are understood.

## Non-negotiable execution boundary

`SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`

`ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`

`HOST_OR_BASH_AS_SIGMA_EXECUTION_ENGINE=FORBIDDEN`

`HOST_OR_BASH_COGNITION=FORBIDDEN`

`HOST_OR_BASH_LEARNING=FORBIDDEN`

`HOST_SEMANTIC_INTERPRETATION=NO`

`HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`

All actual SIGMA learning, selection, scheduling decisions, curriculum decisions, revalidation decisions, lifecycle decisions, fairness decisions, truth decisions, knowledge generation, and cognitive computation must execute in native `.sigma` bytecode under the locked SIGMA VM.

Bash/host MUST NOT implement a missing native capability.

Bash/host may only be an external mechanical harness: invoke compiler/VM, exact byte/file transport, hashes, return codes, isolated fixture setup, fault injection, process supervision, and exact dispatch of an event/stage already chosen by native SIGMA. It may not choose or reinterpret the event.

`BASH_MAY_LAUNCH_SIGMA=YES`

`BASH_MAY_IMPLEMENT_SIGMA_CAPABILITY=NO`

If host/Bash must calculate the answer for a gate to pass, the gate fails.

## Admission discipline

`DO_NOT_LOAD_RESULTS=YES`

`LOAD_CAPABILITIES=YES`

`RUNTIME_PROOF_REQUIRED=YES`

`FAILURE_IS_EVIDENCE=YES`

`WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN`

Compile/file/shell success alone is not a SIGMA capability proof.

## Locked runtime

`SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

`VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`

## Production

Keep production V2.4 running unchanged unless a real VM failure occurs.

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`UPGRADE_V2_4_IN_PLACE=NO`

## Claim limits

Unless separately admitted by locked-runtime proof, keep:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

When any historical artifact conflicts with this file or the bootstrap directive, treat the historical artifact as provenance only and follow the current bootstrap directive.
