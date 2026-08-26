# WINDOW D — SIGMA VM RUNTIME CONTRACT FREEZE RESULT — 2026-08-26

ROLE=WINDOW_D_SIGMA_VM_RUNTIME_CONTRACT_FREEZE
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
WINDOW_A=CLOSED
WINDOW_B=CLOSED
WINDOW_C=CLOSED
CLAIM_POLICY=CLAIM <= EVIDENCE
SOURCE_CORRELATED_NE_VM_RUNTIME_LOCALIZED=YES
BYTE_EXACT_NE_DECODE_SEMANTICS=YES
BEHAVIORAL_EQUIVALENCE_NE_NUMERIC_OPCODE_MAPPING=YES
UNKNOWN_NE_FALSE=YES
NOT_PROVEN_NE_UNSUPPORTED=YES

Window D freezes only the current evidence-bounded native VM runtime contract. It does not redesign the VM, infer runtime semantics from compiler emission alone, infer stack effects from opcode names, or claim cognition, understanding, or reasoning.

The runtime field ledger contains 61 reviewed fields. Five fields are behaviorally proven at bounded granularity, zero exact opcode/runtime internals are promoted to `VM_RUNTIME_LOCALIZED`, 56 remain `NOT_PROVEN`, and zero current-runtime fields are conflicted.

## CURRENT_HASH_SCOPE

WINDOW_D_START_HEAD=ab6efca85ec0e394cdf8740f3f44cd9ca5264015
WINDOW_C_FINAL_COMMIT=2ace6457f4627ea7f1ddba8e7521b8b09f2fb42b
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
WINDOW_A_FRESH_BYTECODE_SHA256=903d78f901ffca4b523d4df3b19e875f1a5f4788bf85fcdbdde611621b769e7a
WINDOW_A_FRESH_BYTECODE_SIZE=8273

The Window A provenance closure binds the current source identity to the current compiler, a fresh 8273-byte bytecode artifact, the current VM identity, captured stdout, empty stderr, and VM RC=0. This proves current bytecode execution/provenance only; it does not expose exact per-opcode decode or stack semantics.

At Window D execution time, the connected GitHub snapshot contains the reports and preserved text evidence but does not track `native/sigma-vm.v09_candidate` or `native/src/sigma_vm.c`. The execution host therefore cannot perform a fresh native differential test against the identified VM binary. No replacement VM, emulator, or arbitrary bytecode generator is used.

Raw Window D evidence:

- `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_D_VM_RUNTIME/00_SCOPE_AND_EXECUTABLE_AVAILABILITY.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_D_VM_RUNTIME/01_BEHAVIORAL_RUNTIME_CLAIM_RECORDS.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_D_VM_RUNTIME/02_RUNTIME_FIELD_AUDIT.tsv`
- `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_D_VM_RUNTIME/03_TARGETED_TEST_RECORDS.tsv`
- `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_D_VM_RUNTIME/04_SOURCE_CORRELATION_CONFLICT_FALSE_PROOF_AUDIT.txt`

## BYTECODE_LOADING

`BL-01` — `BEHAVIORALLY_PROVEN`.

A known valid fresh current bytecode artifact was accepted and executed by VM SHA-256 `029ae4...91c99`, with VM RC=0, captured stdout SHA-256 `278bdb54ead9a96a83e070b440088b066ddd3373409f19f4c7553e7790e7cc4a`, and empty-stderr SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Exact native magic handling is not localized. Window C freezes exact selected compiler-output prefix bytes `53 49 47 4d 42 43 30 31` (`SIGMBC01`) at byte/source-correlation level, but native acceptance/rejection behavior for that prefix was not isolated. `bad_magic.sigmab` and `truncated.sigmab` are preserved byte artifacts without current-VM RC/stdout/stderr results.

Therefore:

- valid bytecode acceptance/execution in tested scope = `BEHAVIORALLY_PROVEN`;
- exact magic validation rule = `NOT_PROVEN`;
- invalid-magic runtime behavior = `NOT_PROVEN`;
- exact decoder instruction-stream start = `NOT_PROVEN`;
- truncated/malformed stream behavior = `NOT_PROVEN`.

## DECODE_DISPATCH

`NATIVE_OPCODE_DISPATCH_LOCATION=NOT_PROVEN`.

WS06 establishes that the repaired top-level VM entry delegates to an existing executable native dispatcher rather than returning the former placeholder runtime error. That closes VM execution existence, not the location or mechanics of the per-opcode decode loop.

No current native decoder source, disassembly, instruction-level trace, or isolated current-VM mutation result is available in the authoritative Window D evidence. Accordingly, no byte in the Window C opcode table is promoted from compiler/source correlation to exact native runtime mapping.

## OPCODE_RUNTIME_TABLE

| Byte | Window C source-correlated label | Operand shape frozen by Window C | Native runtime mapping | Exact stack effect |
|---|---|---|---|---|
| `0x01` | `PUSH_CONST_CORRELATED` | u32 LE constant index | `NOT_PROVEN` | `NOT_PROVEN` |
| `0x02` | `POP_OR_DISCARD_RESULT_CORRELATED` | none observed | `NOT_PROVEN` | `NOT_PROVEN` |
| `0x10` | `LOAD_CORRELATED` | u32 LE name index | `NOT_PROVEN` | `NOT_PROVEN` |
| `0x11` | `STORE_CORRELATED` | u32 LE name index | `NOT_PROVEN` | `NOT_PROVEN` |
| `0x21` | `BINARY_CORRELATED` | u8 sub-op | `NOT_PROVEN` | `NOT_PROVEN` |
| `0x30` | `CALL_CORRELATED` | u32 LE callee-name index + u16 LE argc | `NOT_PROVEN` | `NOT_PROVEN` |
| `0x31` | `RETURN_CORRELATED` | none observed | `NOT_PROVEN` | `NOT_PROVEN` |
| `0x40` | `JUMP_BACKEDGE_CORRELATED` | u32 LE target field | `NOT_PROVEN` | `NOT_PROVEN` |
| `0x41` | `JUMP_IF_FALSE_CORRELATED` | u32 LE target field | `NOT_PROVEN` | `NOT_PROVEN` |
| `0xFF` | `HALT_OR_TERMINATOR_CORRELATED` | none observed | `NOT_PROVEN` | `NOT_PROVEN` |

The two preserved binary sub-operation correlations also remain below VM-runtime localization:

- `0x21 0x01` <-> source `+` = `SOURCE_CORRELATED_ONLY`;
- `0x21 0x12` <-> source `<` = `SOURCE_CORRELATED_ONLY`.

`OPCODES_VM_RUNTIME_LOCALIZED=0`.

## STACK_EFFECTS

No exact per-opcode `STACK_BEFORE`, `STACK_AFTER`, `POP_COUNT`, or `PUSH_COUNT` tuple is directly observed for any of the ten reviewed bytes.

In particular:

- `0x02` is not promoted to a one-pop instruction merely because its source-correlated label contains `POP_OR_DISCARD_RESULT`;
- `0x31` does not establish a return-value pop/push convention;
- `0x40`/`0x41` do not establish conditional stack consumption;
- `0xFF` does not establish terminal stack selection.

All ten reviewed per-byte stack-effect fields remain `NOT_PROVEN`.

## LOAD_STORE_RUNTIME

Existing runtime evidence states that variables execute in tested programs, but no independent native localization closes the exact load/store contract.

The following remain `NOT_PROVEN`:

- exact name-index lookup mechanism and operand interpretation;
- exact state update/store behavior;
- exact local/global/frame scope selection;
- undefined-name behavior.

The Window C `0x10`/`0x11` labels and u32 name-index shapes remain compiler/source-correlated evidence only.

## BINARY_RUNTIME

Arithmetic/relational behavior exists in previously tested programs, but exact numeric binary runtime dispatch is not localized.

The following remain `NOT_PROVEN`:

- exact native runtime meaning of `0x21 0x01`;
- exact native runtime meaning of `0x21 0x12`;
- operand order, runtime types, coercion, and failure behavior;
- exact result representation and stack placement.

The preserved `BINARY_OPCODE_BASE.sigmab -> BAD_BINARY_SUBOP_FAULT.sigmab` pair changes only byte offset 92 from `0x01` to `0xFF` after source-correlated `0x21`. Because no current-VM RC/stdout/stderr was captured for the pair, it proves a one-byte serialized sub-op field only, not runtime binary semantics.

## CALL_RETURN_RUNTIME

`CALL_RETURN_RUNTIME=BEHAVIORALLY_PROVEN` in the already locked scope.

The current runtime-scope memo records `MOTHER_TEST_0002` compiling and running a `DEF` function, call, and `RETURN` with VM RC=0. Its bounded promotion is:

`CALL -> function frame -> callee -> RETURN -> caller continuation`.

Window D does not rerun this capability family.

The following exact details remain `NOT_PROVEN`:

- argument transfer/placement;
- exact frame creation/layout or slot schema;
- exact return-value transfer;
- exact caller IP restoration mechanism;
- exact CALL stack effect;
- exact RETURN stack effect;
- exact numeric native mapping of source-correlated `0x30` and `0x31`.

## JUMP_RUNTIME

`BRANCH_LOOP_BEHAVIOR=BEHAVIORALLY_PROVEN` in the already locked scope. Existing IF/ELSE and WHILE tests, including current self-host/compiler runtime runs cited by the runtime-scope memo, establish branch/loop behavior without establishing numeric decoder mappings.

Window C freezes only the following source-correlated fixture facts for `STEP3_ITER_TEST.sigmab`:

- source-correlated `0x41` carries target field `17`, equal in that fixture to terminal instruction ordinal 17;
- source-correlated `0x40` carries target field `4`, equal in that fixture to the loop-condition reload instruction ordinal 4.

The following remain `NOT_PROVEN`:

- exact native `0x40` mapping;
- exact native `0x41` mapping;
- absolute vs relative target interpretation;
- instruction ordinal vs byte offset interpretation;
- target signedness/bounds behavior;
- conditional value representation/truth handling;
- condition pop vs peek behavior.

Compiler-local target equality is not promoted to native IP semantics.

## INSTRUCTION_POINTER

No exact instruction-pointer transition rule is localized.

The following remain `NOT_PROVEN`:

- ordinary sequential advance basis;
- taken conditional-branch transition;
- not-taken conditional-branch transition;
- unconditional-jump transition;
- CALL entry transition;
- RETURN restoration transition.

Behavioral continuation after calls and behavioral branch/loop execution do not identify the numeric or byte-address transition mechanism.

## TERMINATION_RUNTIME

`NORMAL_TERMINATION=BEHAVIORALLY_PROVEN` for tested current VM runs. The Window A fresh run returned VM RC=0 with empty stderr, and the current runtime-scope memo cites multiple additional successful VM runs.

Window C also observes source-correlated `0xFF` as the last instruction byte in each selected valid artifact. These facts are not collapsed.

The following remain `NOT_PROVEN`:

- exact native decoder meaning of `0xFF`;
- whether `0xFF` is mandatory;
- end-of-stream behavior without `0xFF`;
- exact HALT/terminator transition semantics;
- exact exit-code propagation rule.

Normal termination does not prove exact HALT semantics.

## RESULT_PROPAGATION

`NORMAL_RUN_RESULT_CORRELATED=BEHAVIORALLY_PROVEN` at observable-output level. Window A captures exact stdout identity for the current fresh run, and the locked capability inventory preserves normal-run result correlation.

The following internal rules remain `NOT_PROVEN`:

- exact top-level result selection;
- terminal stack/result source;
- HALT result storage/selection;
- exact function return-value transport to top level;
- relationship between internal result and process exit code beyond the observed successful RC=0 cases.

## BEHAVIORALLY_PROVEN

Five Window D audit fields are frozen as behaviorally proven, without numeric opcode promotion:

1. `BL-01` known-valid current bytecode acceptance/execution in tested scope.
2. `CR-01` CALL -> frame -> callee -> RETURN -> caller continuation in tested scope.
3. `JR-01` IF/ELSE and WHILE branch/loop behavior in tested scope.
4. `TR-01` normal termination with RC=0 in tested current runs.
5. `RP-01` observable normal-run result/output correlation in tested scope.

These are a runtime-focused projection of the already locked evidence. The 21 locked capabilities are preserved and are not rerun as research.

## VM_RUNTIME_LOCALIZED

No exact reviewed opcode byte, binary sub-op, stack effect, load/store mechanism, jump target rule, IP transition rule, HALT rule, or result-selection rule reaches `VM_RUNTIME_LOCALIZED` in Window D.

`VM_RUNTIME_LOCALIZED_FIELDS=0`.

This does not negate current native VM execution. It preserves the distinction between whole-program behavioral evidence and exact decoder/runtime internals.

## NOT_PROVEN

The 56 unresolved fields are enumerated individually in `02_RUNTIME_FIELD_AUDIT.tsv`. They cover:

- 4 bytecode loading/validation details;
- 11 decode/dispatch fields, including the decoder location and all 10 exact byte mappings;
- 10 exact per-byte stack effects;
- 4 load/store details;
- 4 binary-runtime details;
- 5 exact CALL/RETURN internals beyond the behavioral composite;
- 5 exact jump internals beyond the behavioral composite;
- 6 instruction-pointer transitions;
- 4 termination internals beyond normal termination;
- 3 result-propagation internals beyond observable result correlation.

`NOT_PROVEN` is not relabeled as `FALSE` or `UNSUPPORTED`.

## CONFLICTS

`CONFLICTED_FIELDS=0`.

Window C and WS12 agree on the selected source-correlated jump roles:

- `0x40=JUMP_BACKEDGE_CORRELATED`;
- `0x41=JUMP_IF_FALSE_CORRELATED`.

The selected valid Window C/WS12 artifacts share the exact observed 8-byte prefix `SIGMBC01`. Window C also records a bounded current-compiler hash/size bridge for the 53-byte `MINIMAL_BYTECODE_BASE` artifact, while explicitly declining to promote the entire archived corpus as current-compiler canonical. No contradiction is promoted from differing provenance scopes.

## FALSE_PROOF_RISK_AUDIT

The following proof hazards were explicitly blocked:

- opcode-name assumption -> arbitrary bytecode construction -> expected VM output -> semantic declaration;
- whole-program success -> exact numeric opcode mapping;
- source-correlated `0x02` label -> inferred POP stack effect;
- source-correlated `0xFF` + normal termination -> inferred HALT/result contract;
- compiler-local jump target ordinal -> inferred native IP basis;
- host Python/Bash/C behavior -> substituted SIGMA VM semantics.

GPT_EXPECTATION_USED_AS_VM_FACT=NO
HOST_VM_EMULATION_USED=NO
ARBITRARY_BYTECODE_USED_FOR_RUNTIME_PROOF=NO

## TARGETED_TESTS

`TARGETED_TESTS_RUN=0`.

A fresh targeted runtime test was not run because the connected repository snapshot does not contain the current VM executable or native decoder source, and the execution host cannot obtain that binary by repository clone. The targeted-test policy requires a known control artifact, an isolated mutation, and the current VM. Running a mutation without the current VM would not close a runtime field.

The existing one-byte `BINARY_OPCODE_BASE -> BAD_BINARY_SUBOP_FAULT` mutation is retained as byte-field evidence only. It is not counted as a Window D runtime test because current-VM RC/stdout/stderr for the pair are absent.

No capability family was rerun merely to prove it exists.

## PROVENANCE

Authoritative and required inputs used:

- `BRAIN/WORKSTREAMS/SIGMA_PSI/SIGMA_ACTIVE_MINIMAL_CHECKPOINT_AFTER_WINDOW_C_20260826.md`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/SIGMA_CURRENT_VM_RUNTIME_SCOPE_20260826.md`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WINDOW_C_BYTECODE_ABI_FREEZE_RESULT_20260826.md`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS12_PRIMARY_MACHINE_EVIDENCE_HARVEST_RESULT.md`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_REOPEN_EVIDENCE_CLOSURE_RESULT.md`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WINDOW_A_PROVENANCE_LINKAGE_CLOSURE_20260826.md`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/03_SELECTED_BYTECODE_BASE64.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/04_LOCALIZED_BYTE_DUMPS_AND_PARSE.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/05_TEST_RECORDS.tsv`

Window D adds only the raw evidence files listed under `CURRENT_HASH_SCOPE` and this freeze report.

## FREEZE_DECISION

WINDOW_D_FREEZE_DECISION=CONSERVATIVE_CLOSE

The current native VM runtime contract is frozen at the evidence boundary actually available:

- whole-bytecode current VM execution is proven in tested scope;
- normal termination is proven in tested scope;
- CALL/RETURN behavior is proven in tested scope;
- branch/loop behavior is proven in tested scope;
- observable result correlation is proven in tested scope;
- exact numeric opcode mappings remain unlocalized;
- all per-opcode stack effects remain unproven;
- exact load/store, binary dispatch, call-frame internals, jump target/IP rules, HALT semantics, and internal result propagation remain unresolved.

The absence of fresh current-VM mutation capability in this execution host prevents further exact runtime localization without violating the evidence law. Window D therefore closes as an evidence-bounded freeze, not as a declaration that the VM internals are fully known.

The 21 locked capabilities remain preserved without duplicate rerun. The runtime contract is sufficiently frozen for the next evidence window, but not for a public language/runtime specification that would require exact semantics for the unresolved fields.

VM_FIELDS_REVIEWED=61
BYTECODE_LOADING_FIELDS_PROVEN=1
OPCODES_REVIEWED=10
OPCODES_VM_RUNTIME_LOCALIZED=0
STACK_EFFECTS_PROVEN=0
LOAD_STORE_FIELDS_PROVEN=0
BINARY_RUNTIME_FIELDS_PROVEN=0
CALL_RETURN_FIELDS_PROVEN=1
JUMP_RUNTIME_FIELDS_PROVEN=1
IP_TRANSITION_FIELDS_PROVEN=0
TERMINATION_FIELDS_PROVEN=1
RESULT_PROPAGATION_FIELDS_PROVEN=1
BEHAVIORALLY_PROVEN_FIELDS=5
NOT_PROVEN_FIELDS=56
CONFLICTED_FIELDS=0
TARGETED_TESTS_RUN=0
DUPLICATE_TESTS_AVOIDED=21
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21
GPT_ANSWER_IMPOSITION_USED=NO
HOST_LOGIC_SUBSTITUTED_FOR_SIGMA=NO
NEW_VM_SEMANTICS_INVENTED=NO
SOURCE_CORRELATED_PROMOTED_WITHOUT_VM_EVIDENCE=NO
WINDOW_D_FREEZE_COMPLETE=YES
READY_FOR_WINDOW_E=YES
READY_FOR_PUBLIC_LANGUAGE_SPEC=NO