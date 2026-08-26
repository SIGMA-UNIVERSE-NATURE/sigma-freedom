# SIGMA-Ψ WS01–WS13 MASTER CHECKPOINT — 2026-08-26

ROLE=RECOVERY_CHECKPOINT / SHARED_MEMORY
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
PURPOSE=Restore state after chat/context loss without relying on conversation memory.

## REQUIRED FIRST READ
1. BRAIN/GUIDANCE/SIGMA_PSI_PARALLEL_COMPLETION_PROTOCOL_v1.0_20260825.md
2. BRAIN/GUIDANCE/SIGMA_SUPPORTOR_MASTER_REFERENCE_LOCK_v1.0_20260825.md
3. DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.0_20260825.md
4. DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md
5. DOCS/GPT_REFERENCE/SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825.md
6. This checkpoint.
7. Exact workstream/result/evidence files for the domain being resumed.

## GOVERNING LAWS
CLAIM <= EVIDENCE
DECLARATION != FACT
MODEL != REALITY
MAPPING != VALIDATION
DESCRIPTION != EXECUTION
OUTPUT != COGNITION
UNKNOWN != FALSE
NOT_PROVEN != UNSUPPORTED
CORRECTION != SILENT_OVERWRITE
SAME_GLYPH != SAME_SEMANTICS
SOURCE_CORRELATED_EMISSION != VM_RUNTIME_SEMANTICS
RC != ERROR_ABI
PASS != UNIVERSAL_SUPPORT
FAIL != UNSUPPORTED

## NATIVE TERMUX TOOLCHAIN LOCK
ACTIVE_ROOT=~/SIGMA/sigma_genesis1
SIGMA source -> ./native/sigmac -> .sigmab -> ./native/sigma-vm.v09_candidate
FOOTER:
./native/sigmac ... \
&& \
./native/sigma-vm.v09_candidate ...
Do not create wrappers/alternate launchers when native path is available.

## WORKSTREAM STATE
WS01=CLOSED / READY_FOR_MERGE=YES
WS02=CLOSED / READY_FOR_MERGE=YES
WS03=CLOSED / READY_FOR_MERGE=YES
WS04=CLOSED / READY_FOR_MERGE=YES
WS05=CLOSED / READY_FOR_MERGE=YES
WS06=HISTORICAL_BLOCKED; original result preserved
WS07=CLOSED / READY_FOR_MERGE=YES
WS08=CLOSED / READY_FOR_MERGE=YES
WS09=CLOSED / READY_FOR_MERGE=YES
WS10=CLOSED / GLOBAL_EXECUTABLE_LANGUAGE_COMPLETENESS=NO / 67 deduplicated blockers
WS11=CLOSED_RECONCILIATION / BLOCKERS_CLOSED=2 / BLOCKERS_REMAINING=65 / READY_FOR_V1_2_CANDIDATE=NO
WS12=CLOSED_PRIMARY_EVIDENCE_HARVEST / TESTS_RUN=0 / BLOCKERS_REMAINING=65 / READY_FOR_WS06_REOPEN=YES
WS06_REOPEN=COMPLETE_ADDITIVE / NEW_ENTRIES=25 / BLOCKERS_CLOSED=0 / BLOCKERS_REMAINING=65 / READY_FOR_MERGE=NO / READY_FOR_V1_2_CANDIDATE=NO
WS13=BLOCKED_ENVIRONMENT_ACCESS / NATIVE_BINARIES_VERIFIED=NO / TESTS_RUN=0 / BLOCKERS_CLOSED=0 / BLOCKERS_REMAINING=65 / READY_FOR_WS06_FINAL_CLOSURE=NO / READY_FOR_V1_2_CANDIDATE=NO

## KEY FILES / COMMITS
WS06 original: BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_BYTECODE_ABI_COMPILER_VM_RESULT.md @ 7d89d71734ae983b8e5b96a9c5e678549e11d595
WS11: BRAIN/WORKSTREAMS/SIGMA_PSI/WS11_RECONCILIATION_EVIDENCE_CLOSURE_RESULT.md @ f8446ed32f76cd5562256cac7a7559a957e87cfe
WS12: BRAIN/WORKSTREAMS/SIGMA_PSI/WS12_PRIMARY_MACHINE_EVIDENCE_HARVEST_RESULT.md @ d0bf184e354abb3372981ed10fdbc06f64909989
WS06_REOPEN: BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_REOPEN_EVIDENCE_CLOSURE_RESULT.md @ 7af638512b70ae90e4230fe92e1012d2b20f683e
WS13: BRAIN/WORKSTREAMS/SIGMA_PSI/WS13_LIVE_NATIVE_VM_EVIDENCE_CAPTURE_RESULT.md @ 0eed525078793e8a04808c0330e226f57dc0327d
WS13 raw evidence: BRAIN/EVIDENCE/SIGMA_PSI/WS13/

## CURRENT ABI EVIDENCE BOUNDARY
Observed/source-correlated compiler emission only:
- SIGMBC01 exact 8-byte prefix on selected preserved compiler-output artifacts
- 0x01 PUSH_CONST_CORRELATED, u32 LE operand
- 0x02 POP_OR_DISCARD_RESULT_CORRELATED
- 0x10 LOAD_CORRELATED, u32 LE operand
- 0x11 STORE_CORRELATED, u32 LE operand
- 0x21 BINARY_CORRELATED, u8 sub-op
- 0x30 CALL_CORRELATED, u32 LE callee-name index + u16 LE argc
- 0x31 RETURN_CORRELATED
- 0x40 JUMP_BACKEDGE_CORRELATED, u32 LE target field
- 0x41 JUMP_IF_FALSE_CORRELATED, u32 LE target field
- 0xFF HALT_OR_TERMINATOR_CORRELATED
- binary sub-op 0x01 correlated with source +
- binary sub-op 0x12 correlated with source <

NOT_PROVEN:
- VM decode/dispatch
- runtime opcode semantics
- stack effects
- CALL frames/argument placement/return-address/return-value convention
- jump runtime target interpretation and condition pop/peek
- HALT runtime behavior
- malformed-bytecode native stdout/stderr/RC/error ABI
- fresh compiler/VM provenance on live OPPO tree

## WS13 ACCESS BOUNDARY
WS13 execution host: HOME=/home/oai, ARCH=x86_64.
Requested ~/SIGMA/sigma_genesis1 was not mounted there. Access check RC=2 is host filesystem evidence only; it is NOT SIGMA error ABI and NOT evidence that the OPPO/Termux installation is absent.
No substitute compiler/VM/wrapper/emulator was used.

## CURRENT GLOBAL STATE
BLOCKERS_REMAINING=65
READY_FOR_WS06_FINAL_CLOSURE=NO
READY_FOR_V1_2_CANDIDATE=NO
GLOBAL_EXECUTABLE_LANGUAGE_COMPLETENESS=NO

## NEXT AUTHORIZED STEP
Do NOT repeat WS13 in another non-OPPO host.
Next admissible evidence step must execute on the actual OPPO/Termux environment exposing ~/SIGMA/sigma_genesis1.
First operations there:
1. verify ./native/sigmac and ./native/sigma-vm.v09_candidate exist;
2. capture SHA-256 of both before tests;
3. reuse existing PASS fixtures first;
4. execute only native source -> compiler -> .sigmab -> VM chain;
5. capture exact SOURCE/SOURCE_SHA256/COMPILER/COMPILER_SHA256/BYTECODE/BYTECODE_SHA256/VM/VM_SHA256/COMMAND/STDOUT/STDERR/RC/CLAIM/EVIDENCE_SCOPE;
6. capture malformed/fault artifact outcomes without treating RC as stable error ABI;
7. then create additive WS13 live-evidence continuation or WS14 evidence-ingest result; never rewrite historical WS13.

## RECOVERY INSTRUCTION FOR NEW CHAT
Read BRAIN/WORKSTREAMS/SIGMA_PSI/SIGMA_PSI_WS01_WS13_MASTER_CHECKPOINT_20260826.md on SIGMA-UNIVERSE-NATURE/sigma-freedom branch SIGMA_LIFE. Treat it as the recovery index. Then read the exact referenced result/evidence files before making claims. Continue only from NEXT_AUTHORIZED_STEP. Do not rely on chat memory and do not rewrite history.

END_CHECKPOINT
