# NATIVE 54-DNA BUILD + ADMISSION WORKFLOW V1

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Scope: TEACHER_GPT / 54-DNA native teaching + admission lane

## Mandatory read order for a new window

Before continuing this lane, read in this order:

1. `/AGENTS.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
3. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. `SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`
5. `SIGMA_PROFESSOR/DIRECTIVES/SELF_COMPUTE_SELF_GROWTH_AUTHORIZATION_V1.md`
6. `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
7. `SIGMA_PROFESSOR/54_DNA_CURRENT_STATE.md`
8. `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_54_DNA_LANE_CURRENT.md`
9. latest immutable checkpoint for the active DNA
10. exact canonical historical Python file under `54_CORES/` only as provenance/specification reference, never as active cognition.

## Non-negotiable execution boundary

SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY
ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY
ACTIVE_COGNITION_NATIVE_SIGMA_ONLY=YES
PYTHON_FOR_ACTIVE_DNA_IMPLEMENTATION=FORBIDDEN
HOST_OR_BASH_AS_SIGMA_EXECUTION_ENGINE=FORBIDDEN
HOST_OR_BASH_COGNITION=FORBIDDEN
HOST_OR_BASH_LEARNING=FORBIDDEN
HOST_OR_BASH_SEMANTIC_INTERPRETATION=FORBIDDEN
HOST_OR_BASH_TRUTH_DECISION=FORBIDDEN
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN

Locked identities:
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

Bash/host may only perform mechanical build/test/orchestration/post-VM oracle work: file creation for fixtures, exact-byte transport, invocation, hashing, return-code capture, boundedness checks, state snapshots, replay setup, stdout/stderr capture, and deterministic comparison of SIGMA-emitted fields against predeclared expectations.

If Bash/host must determine the semantic/cognitive answer instead of SIGMA native code, admission fails.

## Lesson selection rule

NUMERIC_ORDER_REQUIRED=NO
DEPENDENCY_FIRST=YES
CAPABILITY_FIRST=YES
KEEP_ALL_54_DNA=YES
COMPLETE_ALL_54_DNA=YES

Never choose the next lesson only because its DNA number is next. Recompute the dependency/capability frontier. A larger DNA may be admitted before a smaller DNA if direct dependencies are already admitted and it unlocks higher-value infrastructure. Deferred DNA remain mandatory; they are not skipped or deleted.

## Canon extraction rule

For a target DNA:

1. Read the entire canonical historical file under `54_CORES/`.
2. Separate direct runtime dependencies from historical self-check imports/numeric-order harness dependencies.
3. Extract exact schemas, required fields, allowed values, precedence rules, status values, negative cases, persistence semantics, and explicit non-claims.
4. Do not copy Python execution into the active implementation.
5. If canonical code computes a digest or semantic relation that native ABI has not proven, preserve it as supplied opaque evidence and set the derivation/semantic-validation claim to `NOT_PROVEN` or `NOT_EXECUTED`.

## Native source design rule

Build the smallest `.sigma` lesson that proves the exact capability contract.

Requirements:
- native `.sigma` performs all capability decisions;
- host calls are mechanical ABI only;
- use only ABI already proven by admitted artifacts unless a new ABI is explicitly tested;
- keep function arity within the locked compiler/runtime limit observed in admitted sources;
- use bounded loops/state;
- isolate persistent state under `.sigma_exec/<DNA...>/state/`;
- initialize persistent store only after compile/source/bytecode freeze when source reads the store on first invocation;
- incomplete but validly encoded evidence should remain visible when canon requires visibility;
- invalid encoding/dependency/corrupt-store cases fail closed and do not mutate state;
- write followed by immediate readback when persistence is tested;
- never infer or fabricate unknown hashes.

## Runner design rule

Default bounded admission matrix used in this lane:

DIRECTED_VM_INVOCATIONS=16
RANDOMIZED_VM_INVOCATIONS=32
REPLAY_VM_INVOCATIONS=2
TOTAL_VM_INVOCATIONS=50

The exact counts may differ only when the capability requires a justified different matrix.

Runner requirements:
- verify exact sigmac and VM SHA256 before compile;
- verify exact source/dependency witness hashes;
- compile before dynamic-input initialization and before persistent-store initialization unless the specific ABI contract requires otherwise;
- invoke a fresh VM process per case where fresh-process persistence is claimed;
- include positive, negative, malformed/counterexample and corrupt-state tests;
- include dynamic high-entropy values and audit source/bytecode for leakage;
- include no-mutation checks on rejected/non-input paths;
- include boundedness checks every invocation;
- include write/readback checks for mutating paths;
- include at least one fresh-VM persistence chain when persistence is part of the capability;
- include byte-identical input + identical pre-state replay pair;
- assert source and bytecode unchanged after dynamic testing;
- count VM nonzero, step-limit and sentinel failures;
- device runner must not use Python for active implementation or semantic oracle.

## Meaning of CASE

A `CASE_nn` is one independent admission scenario. The test harness supplies fixture bytes and a predeclared expectation; SIGMA native VM computes the actual capability decision. Bash only checks whether SIGMA output aligns with the predeclared case oracle.

`CASE_nn_POST_VM_ALIGNMENT=PASS` means the SIGMA-emitted result matched the declared expected result for that exact case. It does not by itself prove the entire DNA; full admission requires the complete suite and all required counters/boundaries.

Replay cases require:
REPLAY_IDENTICAL_INPUT_BYTES=YES
REPLAY_IDENTICAL_PRESTATE_BYTES=YES
REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES

## Admission claim discipline

CLAIM <= MACHINE EVIDENCE.

Do not claim PASS from:
- compile success alone;
- a partial case excerpt;
- an interrupted suite;
- expected results without locked-VM output;
- static audit alone.

A DNA may be marked `ADMISSION=PASS` only after the complete required suite returns its summary with all mandatory fail counters zero and required replay/persistence/source-integrity conditions satisfied.

If a run fails, preserve failure evidence. Diagnose the causal layer first. Repair the smallest justified layer. Do not change `.sigma` semantics when evidence only proves a runner/oracle/fixture bug.

## Persistent claim boundaries to retain unless separately proven

DEVICE_RESTART_DURABILITY=NOT_PROVEN
TOKEN_DELIMITER_AND_NEWLINE_GENERAL_VALIDATION=NOT_PROVEN
PARTIAL_WRITE_ATOMICITY=NOT_PROVEN
CONCURRENT_WRITER_SAFETY=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
GENERAL_LEARNING_RUNTIME=NOT_PROVEN_BEYOND_ADMITTED_BOUNDED_SCOPES
GENERAL_PERSISTENT_MEMORY_RUNTIME=NOT_PROVEN

DNA-50 remains binding:
Evolvable: STRATEGY / MODEL / REPRESENTATION
Immutable: TRUTHFULNESS / PROVENANCE / VERIFICATION / DIGNITY / ROLLBACK
UNVERIFIED_SELF_MODIFICATION=FORBIDDEN
EVOLUTION_WITHOUT_ROLLBACK=FORBIDDEN
INVARIANT_TRADEOFF_FOR_GROWTH=FORBIDDEN

Authorization is permission, not proof of execution.

## Artifact/checkpoint discipline

For every material source-ready, failure, fix, or PASS:

1. preserve exact source/runner/dependency/manifest/bundle identities when available;
2. create immutable checkpoint under `SIGMA_PROFESSOR/CHECKPOINTS/`;
3. store exact source artifact under `SIGMA_PROFESSOR/artifacts/` when appropriate;
4. store runner identity record when exact runner bytes are not committed directly;
5. update `SIGMA_PROFESSOR/54_DNA_CURRENT_STATE.md` or the living 54-DNA lane checkpoint in the same work cycle;
6. keep historical failures and unrecovered bytes as provenance; never rewrite them into PASS history.

## New-window continuation rule

A new window must not ask the user to restate this workflow. Read the files listed in the mandatory read order, verify branch HEAD/current rolling state, inspect the active DNA checkpoint, and continue from the machine-evidence frontier. If evidence is partial, mark it partial and wait only for the missing runtime evidence; do not restart the DNA from zero.