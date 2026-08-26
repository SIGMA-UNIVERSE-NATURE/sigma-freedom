# SIGMA CURRENT VM RUNTIME SCOPE — 2026-08-26

ROLE=CURRENT_REALITY_NOTE
BRANCH=SIGMA_LIFE
CLAIM_POLICY=CLAIM <= EVIDENCE

CURRENT_VM_RUNTIME_PROVEN=YES

PROVEN_LEVEL=
- BYTECODE_EXECUTION
- NORMAL_TERMINATION
- FUNCTION_CALL_RETURN_BEHAVIOR
- BRANCH_LOOP_BEHAVIOR

DETAILS:

VM_EXECUTION=YES
EVIDENCE:
- ./native/sigma-vm.v09_candidate has executed multiple .sigmab programs with RC=0.
- MOTHER_TEST_0001: HOST_MOTHER_VM_RC=0.
- MOTHER_TEST_0002: HOST_MOTHER_0002_VM_RC=0.
- Stage3 language test: HOST_LANGUAGE_GROUP_VM_RC=0.
- Stage4/5/6 regression VM runs: RC=0.
- SIGMA_MULTIHOP_TRAVERSAL runtime: HOST_VM_RC=0.
SCOPE=Bytecode loading + execution + normal termination proven only in tested programs.

OPCODE_DECODE_LOCALIZED=NO
EVIDENCE:
- compiler_self.sigma emits/writes opcode numbers, including EMIT(...,255,...).
- native sigma-vm.v09_candidate decoder/dispatch loop has not been machine-localized/inspected per opcode.

STACK_EFFECTS=NO
EVIDENCE:
- arithmetic, variables, function frames, IF/WHILE execute in tested scope.
- no independent per-opcode before_stack -> after_stack evidence exists.

CALL_RETURN_RUNTIME=YES
EVIDENCE:
- MOTHER_TEST_0002 compiled and ran RC=0 with a DEF function, call, and RETURN.
- HOST_MOTHER_0002_VM_RC=0.
SCOPE=CALL -> function frame -> RETURN -> caller continuation proven in tested scope.
LIMIT=Exact opcode-number mapping and per-opcode stack transition not proven.

JUMP_JUMP_IF_FALSE_RUNTIME=YES
EVIDENCE:
- IF/ELSE and WHILE runtime behavior executed successfully in SIGMA tests.
- compiler_self.sigma uses IF/WHILE extensively; Stage4/5/6 self-host compiler execution passed RC=0.
SCOPE=Branch/loop behavior equivalent to JUMP/JUMP_IF_FALSE proven at behavior level.
LIMIT=Native decoder localization and exact opcode-number runtime mapping not proven.

HALT_RESULT_RUNTIME=NO
EVIDENCE:
- compiler_self.sigma contains EMIT(main, 255, 0, 0) at end of main.
- many bytecode programs terminate normally with VM RC=0.
SCOPE=Normal termination proven.
LIMIT=Exact HALT result-selection/storage/propagation semantics not proven.

NOT_YET_PROVEN=
- NATIVE_OPCODE_DISPATCH_LOCATION
- EXACT_OPCODE_MAPPING
- PER_OPCODE_STACK_EFFECTS
- EXACT_HALT_RESULT_SEMANTICS

BOUNDARY:
CURRENT_VM_RUNTIME_PROVEN=YES does NOT imply VM_RUNTIME_FULLY_PROVEN=YES.
SOURCE_CORRELATED_EMISSION != VM_RUNTIME_SEMANTICS.
RC != ERROR_ABI.
