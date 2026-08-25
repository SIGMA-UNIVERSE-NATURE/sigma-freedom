# OBSERVED

- **WS06-OBS-001 — Locked-reference scope.** The frozen v1.0 master, frozen v1.1 extension, 256-symbol matrix, and supportor lock establish mother-language declarations, evidence discipline, and ABI-closure requirements, but they do not directly evidence a bytecode magic/header, a numeric opcode table, operand widths, constant-pool layout, instruction stack effects, invalid-opcode behavior, or a source-to-bytecode fingerprint binding.
- **WS06-OBS-002 — Matrix positions are not opcodes.** The 256-symbol matrix explicitly states that its `0x00`–`0xFF` values are symbol-reference keys and are not an inference about a byte-level VM opcode table. No matrix reference position is used as a bytecode value in this result.
- **WS06-OBS-003 — Binary operator family is symbolic mother-language evidence.** WS04 carries the symbolic binary operator inventory `add`, `sub`, `mul`, `div`, `mod`, `eq`, `ne`, `lt`, `le`, `gt`, `ge`, `and`, `or` (13 entries). This is not evidence of numeric VM binary sub-op values, byte encodings, operand widths, or stack effects.
- **WS06-OBS-004 — Control-flow lowering is declared symbolically, not emitted-byte evidence.** WS05 carries the declared relations `if -> JUMP_IF_FALSE`, `while -> JUMP + JUMP_IF_FALSE`, `for -> while`, `fn -> function proto`, and `return -> RETURN`. WS05 also explicitly prohibits promoting source/AST declarations to bytecode emission or numeric opcode semantics without compiler/VM evidence.
- **WS06-OBS-005 — Machine archive evidence is aggregate and unlocalized.** `SIGMA_REAL_RESULTS_ARCHIVE_20260823.state` records `SIGMA_PSI_256_MATRIX_COMPILE=PASS`, `SIGMA_PSI_256_MATRIX_VM=PASS`, `SIGMA_PSI_COMPILER_AUDIT_RC=4`, `SIGMA_PSI_VM_AUDIT_RC=26`, and `SIGMA_PSI_TEST_TEXT=Pass=134 Fail=0` / `SIGMA_PSI_TEST_JSON=Pass=134 Fail=0 Total=134`. The archive does not localize those results to individual opcodes, operand encodings, stack transitions, decode cases, or error paths.
- **WS06-OBS-006 — Existing fingerprint evidence is not bytecode provenance.** The archive field `SIGMA_PSI_KB_FINGERPRINT=REGISTERED` is knowledge-base provenance evidence. It does not establish a source fingerprint, compiler identity, emitted-bytecode digest, source-to-bytecode binding, or VM executable congruence.
- **WS06-OBS-007 — Primary ABI implementation evidence did not surface in the audited branch snapshot.** In the exact `SIGMA_LIFE` snapshot recorded under PROVENANCE, branch-tree inspection and exact-term repository searches did not surface a primary compiler source, VM decoder/dispatcher source, bytecode fixture/hexdump, opcode table, or direct `PUSH_CONST` / `SIGMA_BYTECODE_MAGIC` evidence sufficient to promote exact bytecode ABI values. This is a scope-bounded evidence result, not a claim that such artifacts cannot exist elsewhere.

# PROVEN

- **WS06-PROVEN-001 — Layer separation is mandatory.** Mother-language semantics, compiler surface/lowering declarations, bytecode ABI, and VM decode/execute semantics are separate evidence layers. A claim at one layer does not prove a value at another layer.
- **WS06-PROVEN-002 — Symbolic control-flow/compiler surface declarations exist.** `JUMP`, `JUMP_IF_FALSE`, `RETURN`, and `function proto` are evidenced as symbolic lowering/declaration terms through the frozen/upstream workstream evidence. Their numeric opcode values and physical encodings are not proven.
- **WS06-PROVEN-003 — Symbolic binary inventory has 13 entries.** The evidenced mother-language binary operator family is exactly: `add`, `sub`, `mul`, `div`, `mod`, `eq`, `ne`, `lt`, `le`, `gt`, `ge`, `and`, `or`. This proves only the symbolic operator inventory, not VM sub-op numbering.
- **WS06-PROVEN-004 — Aggregate compiler/VM suite status is recorded.** The machine archive records `SIGMA_PSI_256_MATRIX_COMPILE=PASS` and `SIGMA_PSI_256_MATRIX_VM=PASS` as whole-suite status fields.
- **WS06-PROVEN-005 — Compiler/VM audit return-code fields are recorded exactly but remain opaque.** The archive records compiler audit RC `4` and VM audit RC `26`. No exit-code contract in the audited evidence assigns semantics to those numbers, so only the literal recorded values are proven.
- **WS06-PROVEN-006 — 256-symbol `0xNN` positions cannot establish opcode values.** The matrix itself explicitly blocks that inference; therefore no bytecode numeric value is derived from a symbol position.
- **WS06-PROVEN-007 — No exact numeric ABI constant is promoted by WS06.** Under `CLAIM <= EVIDENCE`, this result introduces zero bytecode magic constants, opcode numeric values, binary sub-op numeric values, operand widths, stack effects, jump-width conventions, or constant-pool encodings because no directly supporting primary evidence was found in the audited scope.

# NOT_PROVEN

- **WS06-NP-001 — Bytecode magic/header.** Magic bytes/string, header length, field ordering, byte order/endianness, flags, offsets, counts, and header validation behavior are not proven.
- **WS06-NP-002 — Opcode inventory and numeric values.** A complete bytecode opcode inventory and exact numeric opcode values are not proven.
- **WS06-NP-003 — `PUSH_CONST` / `POP`.** Numeric opcode values, operand widths, constant-index encoding, bounds behavior, and exact stack effects are not proven.
- **WS06-NP-004 — `LOAD` / `STORE`.** Numeric opcode values, operand encoding, slot/name addressing model, scope/state semantics, and exact stack effects are not proven.
- **WS06-NP-005 — `UNARY` / `BINARY`.** Numeric opcode values, unary sub-op inventory/values, binary sub-op numeric values, operand format, evaluation order at VM level, and exact stack effects are not proven. The 13-entry binary family is proven only at the mother-language symbolic layer.
- **WS06-NP-006 — `CALL` / `RETURN`.** Numeric opcode values, callee/arity operand encoding, call-frame layout, argument placement, return-address convention, return-value convention, and exact stack effects are not proven.
- **WS06-NP-007 — `JUMP` / `JUMP_IF_FALSE`.** Numeric opcode values, jump-target width, target encoding, relative-versus-absolute basis, signedness, bounds behavior, and whether `JUMP_IF_FALSE` pops or peeks its condition are not proven.
- **WS06-NP-008 — `HALT`.** Numeric opcode value, termination contract, result-selection rule, terminal stack/state behavior, and interaction with fall-through/end-of-buffer are not proven.
- **WS06-NP-009 — Compiler source -> bytecode relation.** Exact source/AST forms to emitted instruction sequences, instruction ordering, constant-pool insertion, branch patching, function emission, and any optimization/canonicalization are not proven by primary compiler evidence.
- **WS06-NP-010 — VM decode/execute relation and stack/state transitions.** Exact decode widths, dispatch relation, instruction pointer movement, stack preconditions/postconditions, frame/state mutations, and instruction-wise transitions are not proven by primary VM evidence.
- **WS06-NP-011 — Constant pool / operand encoding.** Constant-pool binary format, entry tagging, scalar representation, string encoding, index width, operand widths, endianness, alignment, and bounds rules are not proven.
- **WS06-NP-012 — Bytecode versioning.** A bytecode-version field, version encoding, compatibility policy, upgrade/rejection behavior, and version-to-ABI mapping are not proven. The frozen reference labels `v1.0` and `v1.1` are document/reference versions and are not promoted to bytecode-version values.
- **WS06-NP-013 — Invalid opcode / malformed bytecode behavior.** Invalid-opcode handling, truncated-operand behavior, malformed-header behavior, constant-index failure, stack-underflow behavior, error codes/messages, and fail/abort/return semantics are not proven.
- **WS06-NP-014 — Source/bytecode fingerprint and provenance binding.** Source digest -> compiler identity/digest -> emitted bytecode digest -> VM identity/result binding is not proven. The recorded KB fingerprint does not substitute for this chain.
- **WS06-NP-015 — Compiler/VM evidence versus declared ABI.** Per-instruction congruence between any declared symbolic ABI surface and actual compiler emission plus VM decoding/execution is not proven.
- **WS06-NP-016 — Audit RC semantics.** The meanings of compiler audit RC `4` and VM audit RC `26` are not proven because no exit-code contract was directly evidenced in the audited inputs.

# CONFLICT

- No directly evidenced bytecode-ABI conflict was found.
- The combination of aggregate suite `PASS` labels with compiler audit RC `4` and VM audit RC `26` is **not** classified as a conflict because the return-code semantics are not evidenced.
- Symbolic lowering declarations without localized compiler-emission/VM-decode evidence are an evidence gap, not a contradiction.
- Missing primary bytecode artifacts in the audited scope do not conflict with the frozen declarations; they limit proof strength.

# PROPOSED_NORMALIZATION

- Normalize the WS05 lowering labels (`JUMP`, `JUMP_IF_FALSE`, `RETURN`, `function proto`) as `DECLARED_SYMBOLIC` until compiler emission is directly evidenced.
- Normalize the WS04 13-entry binary operator family as `MOTHER_LANGUAGE_SYMBOLIC_OPERATOR_INVENTORY`; do not assign VM binary sub-op numbers from ordering or names.
- Normalize archive fields `SIGMA_PSI_256_MATRIX_COMPILE=PASS` and `SIGMA_PSI_256_MATRIX_VM=PASS` as `MACHINE_SUITE_PASS_UNLOCALIZED`; they prove suite-level recorded status only.
- Normalize compiler audit RC `4` and VM audit RC `26` as `OPAQUE_RECORDED_RC` until an exit-code contract or directly linked test harness semantics are evidenced.
- Keep every exact ABI field above as `NOT_PROVEN`; do not use guessed placeholders for magic, opcodes, widths, stack effects, sub-op values, encodings, version numbers, or error codes.
- Keep the 256-symbol `0xNN` reference positions permanently segregated from bytecode opcode numbering unless a future primary artifact explicitly establishes a mapping.
- Keep frozen-reference versions (`v1.0`, `v1.1`) segregated from bytecode-version semantics unless a primary bytecode format source explicitly binds them.
- Permit exact ABI promotion only from primary localized evidence such as compiler emission source, VM decoder/dispatch source, a bytecode fixture/hexdump with provenance, constant-pool serialization source, instruction-level stack/state traces, invalid-opcode tests, or bytecode digest/provenance artifacts.
- For any future ABI row, use at least: `layer | symbol | numeric_value | operand_encoding | stack_effect | evidence | status`; leave machine fields `NOT_PROVEN` until directly evidenced.
- For future provenance closure, require the chain: source fixture digest -> compiler identity/digest -> emitted bytecode digest/bytes -> decoded instruction sequence -> VM stack/state trace -> result/error trace.
- Do not allow another workstream to fill WS06 machine-ABI gaps by cross-layer inference. WS06 remains the source of truth for bytecode ABI/compiler/VM promotion.

# EVIDENCE

- `BRAIN/GUIDANCE/SIGMA_PSI_PARALLEL_COMPLETION_PROTOCOL_v1.0_20260825.md`
- `DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.0_20260825.md` — blob `bcbf3104d065a33e0631cba8051dacca7da0a5b`
- `DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md` — blob `fbc8da05a2e79235020a4f629ceb1c282876ce98`
- `DOCS/GPT_REFERENCE/SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825.md` — blob `cbda75a81ee9a69044dcaa3d46708d5b585817e4`
- `BRAIN/GUIDANCE/SIGMA_SUPPORTOR_MASTER_REFERENCE_LOCK_v1.0_20260825.md` — blob `7e522c470530d7aa218aab52eb9f2d08ea14f2e5`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS01_GLYPH_TOKEN_REGISTRY_RESULT.md` — blob `dc38726fe29b99e96b86986619e753c0453ae97e`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS02_LEXER_LEXICAL_RULES_RESULT.md` — blob `b6d7953b4d03bac7f3e19a04097c5bdd88b7b6a3`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS03_GRAMMAR_COMPOSITION_RESULT.md` — blob `04fe65236f8fe231df59bd0e36426cc5cad4b5b3`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS04_TYPES_VALUES_OPERATORS_RESULT.md` — blob `174b09c48762f597696841646e19bf3dadc4ce4f`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS05_CONTROL_FLOW_FUNCTIONS_STATE_RESULT.md`
- `BRAIN/EVIDENCE/SIGMA_SHELL/REAL_RESULTS/SIGMA_REAL_RESULTS_ARCHIVE_20260823.state` — blob `b2732adbc7b155d2ab50a11781a9b7250e167230`
- Exact branch-tree inspection at the final audit snapshot found no path whose name itself supplied primary `compiler`, `bytecode`, or `opcode` ABI evidence. Exact-term repository searches for `PUSH_CONST` and `SIGMA_BYTECODE_MAGIC` returned no supporting result in the audited repository scope. These negative searches are used only to bound WS06 evidence availability, not to prove universal nonexistence.

# PROVENANCE

REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom  
BRANCH=SIGMA_LIFE  
AUDIT_SCOPE=WS06_BYTECODE_ABI_COMPILER_VM  
SOURCE_HEAD_AT_FINAL_AUDIT=2304fa62c8a68672fcb41b35ef6384c3afd9a425  
SOURCE_TREE_AT_FINAL_AUDIT=e789ab9748bf680857a086c0ef8b1a87f784a34f  
FROZEN_MASTERS_EDITED=NO  
FROZEN_REFERENCE_MUTATION=NONE  
MATRIX_OPCODE_INFERENCE=NOT_USED  
NUMERIC_ABI_CONSTANTS_INTRODUCED=0  
CLAIM_POLICY=CLAIM<=EVIDENCE  
TARGET_FILE=BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_BYTECODE_ABI_COMPILER_VM_RESULT.md  

NEW_ENTRIES=7
DUPLICATES=4
CONFLICTS=0
MISSING=16
READY_FOR_MERGE=NO