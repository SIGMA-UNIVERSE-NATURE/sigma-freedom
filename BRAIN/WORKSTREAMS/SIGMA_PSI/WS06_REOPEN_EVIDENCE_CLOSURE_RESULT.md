# OBSERVED

- This result is additive only. `BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_BYTECODE_ABI_COMPILER_VM_RESULT.md` remains immutable historical evidence; frozen masters are not edited.
- WS12 used the byte-exact OPPO/Termux archive under `BRAIN/EXTRA BRAIN_OPPO_24826`. The archive scope records `PRESERVE_BYTE_EXACT`, `NO_RECOMPILE=TRUE`, `NO_REWRITE=TRUE`, 392 source artifacts, 390 bytecode artifacts, and 782 total archived artifacts.
- WS12 performed zero fresh native compiler/VM tests. `BRAIN/EVIDENCE/SIGMA_PSI/WS12/05_TEST_RECORDS.tsv` contains the required header and `TESTS_RUN=0`; no compiler/VM test row was fabricated.
- The selected valid archived compiler-output artifacts `MINIMAL_BYTECODE_BASE.sigmab`, `BINARY_OPCODE_BASE.sigmab`, `STEP3_ITER_TEST.sigmab`, and `DISCIPLINE_LOCK.sigmab` all begin at offsets `0..7` with exact bytes `53 49 47 4d 42 43 30 31`, ASCII `SIGMBC01`.
- The eight-byte `SIGMBC01` sequence is an observed byte prefix only. Header field boundaries, magic semantics, version semantics, compatibility meaning, validation behavior, and the meaning of the following `01 00 00 00` field remain separate and are not inferred from the prefix.
- WS12 localizes source-correlated compiler-output byte shapes for `0x01`, `0x02`, `0x10`, `0x11`, `0x21`, `0x30`, `0x31`, `0x40`, `0x41`, and `0xFF`. These are compiler-emission correlations, not VM decode/dispatch proof.
- Directly observed correlated operand shapes are: PUSH_CONST `u32 LE`; LOAD `u32 LE`; STORE `u32 LE`; BINARY `u8`; CALL `u32 LE callee-name index + u16 LE argc`; JUMP `u32 LE target field`; JUMP_IF_FALSE `u32 LE target field`.
- Directly observed binary sub-operation correlations are `0x01` with source `+` and `0x12` with source `<`. No other binary sub-operation value is promoted.
- Exact preserved source/bytecode localization inputs used here are:

| Evidence item | Source SHA-256 | Bytecode SHA-256 | Byte length | Localized role |
|---|---|---|---:|---|
| `MINIMAL_BYTECODE_BASE` | `294a888511b15a14f64e98410a786eeee26ec0934a6f30de04758a270f013dc6` | `26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875` | 53 | minimal PUSH/STORE/terminator correlation |
| `BINARY_OPCODE_BASE` | `51e69c08bace633fb42ed48257b15a891fb94e58283989f2f04e8b1f79ecb2a2` | `23a483ddea89cf36a36618cc7d192d1a3efd51927ed3272a77574be23d14a13c` | 99 | LOAD/BINARY/STORE and `+ -> 0x01` correlation |
| `DISCIPLINE_LOCK` | `cf82ef98514198df84a97e1bc3f7bd374db44ef3262bba934a74caffa5c0c94f` | `e3d4f6169fbb83d0df8977f8029f53a2181531582954898e469e0e0e6ac1a4a0` | 644 | CALL/RETURN, LOAD/PUSH/STORE, post-call `0x02`, terminator correlation |
| `STEP3_ITER_TEST` | `b761ec81bf8ce7f6e2aec7aa6637cd822fbbf520eef99d84c1216a3ed131368e` | `e15e17e7fa3aace360bddd0062880c3e10ac3e869ef256f05f073aa2f6381e4a` | 166 | WHILE condition, `+`, `<`, CALL, JUMP/JUMP_IF_FALSE, `0x02`, terminator correlation |
| `BAD_BINARY_SUBOP_FAULT` controlled counterpart | baseline source is `BINARY_OPCODE_BASE.sigma` above; no distinct fault source is claimed | `629ddc92b5cc1e0920bdc1f8fbc2d361d01d57f26245788f243d924e8e64f8d5` | 99 | controlled bytecode mutation only: offset 92 `0x01 -> 0xFF`, preceding offset 91 `0x21` |

- `BINARY_OPCODE_BASE.sigmab` and `BAD_BINARY_SUBOP_FAULT.sigmab` have equal length 99 and differ at one byte only, offset 92. This supports the one-byte correlated BINARY sub-operation field in that fixture. It does not prove runtime rejection or error behavior.

# PROVEN

The following are the only WS06 machine-field promotions made by this additive result. `*_CORRELATED` means source-correlated compiler-output emission only.

| Promotion | Bounded proven claim | Exact WS10 blocker IDs affected |
|---|---|---|
| `P-01` | `SIGMBC01` is an observed exact 8-byte prefix on the four selected valid archived compiler-output artifacts. | `MR-04`, `MME-18` |
| `P-02` | Byte `0x01` is `PUSH_CONST_CORRELATED` in the selected source/bytecode localizations. | `MR-04`, `MME-19`, `MME-20`, `MLT-13` |
| `P-03` | Byte `0x02` is `POP_OR_DISCARD_RESULT_CORRELATED` at selected call-expression/loop-print statement positions; runtime stack behavior is not implied. | `MR-04`, `MME-19`, `MME-20`, `MLT-13` |
| `P-04` | Byte `0x10` is `LOAD_CORRELATED` in the selected source/bytecode localizations. | `MR-04`, `MME-19`, `MME-20`, `MLT-13` |
| `P-05` | Byte `0x11` is `STORE_CORRELATED` in the selected source/bytecode localizations. | `MR-04`, `MME-19`, `MME-20`, `MLT-13` |
| `P-06` | Byte `0x21` is `BINARY_CORRELATED` in the selected source/bytecode localizations. | `MR-04`, `MME-13`, `MME-19`, `MME-20`, `MLT-08`, `MLT-13` |
| `P-07` | Byte `0x30` is `CALL_CORRELATED` in the selected source/bytecode localizations. | `MR-04`, `MME-10`, `MME-19`, `MME-20`, `MLT-11`, `MLT-13`, `MRB-05` |
| `P-08` | Byte `0x31` is `RETURN_CORRELATED` at explicit RETURN function termination in `DISCIPLINE_LOCK`. | `MR-04`, `MME-10`, `MME-19`, `MME-20`, `MLT-11`, `MLT-13`, `MRB-05` |
| `P-09` | Byte `0x40` is `JUMP_BACKEDGE_CORRELATED` in the localized `STEP3_ITER_TEST` WHILE emission. | `MR-04`, `MME-09`, `MME-19`, `MME-20`, `MLT-10`, `MLT-13`, `MRB-05` |
| `P-10` | Byte `0x41` is `JUMP_IF_FALSE_CORRELATED` in the localized `STEP3_ITER_TEST` WHILE exit-edge emission. | `MR-04`, `MME-09`, `MME-19`, `MME-20`, `MLT-10`, `MLT-13`, `MRB-05` |
| `P-11` | Byte `0xFF` is `HALT_OR_TERMINATOR_CORRELATED` as the terminal byte in selected main streams. | `MR-04`, `MME-19`, `MME-20`, `MLT-13` |
| `P-12` | `PUSH_CONST_CORRELATED` carries an observed 4-byte `u32 LE` constant-index operand in the selected localizations. | `MR-04`, `MME-18`, `MME-19`, `MME-20`, `MLT-13` |
| `P-13` | `LOAD_CORRELATED` carries an observed 4-byte `u32 LE` name-index operand. | `MR-04`, `MME-18`, `MME-19`, `MME-20`, `MLT-13` |
| `P-14` | `STORE_CORRELATED` carries an observed 4-byte `u32 LE` name-index operand. | `MR-04`, `MME-18`, `MME-19`, `MME-20`, `MLT-13` |
| `P-15` | `BINARY_CORRELATED` carries an observed 1-byte `u8` sub-operation field. | `MR-04`, `MME-18`, `MME-19`, `MME-20`, `MLT-13`, `MLT-20` |
| `P-16` | `CALL_CORRELATED` carries observed `u32 LE callee-name index + u16 LE argc`, 6 operand bytes total. | `MR-04`, `MME-10`, `MME-18`, `MME-19`, `MME-20`, `MLT-11`, `MLT-13`, `MRB-05` |
| `P-17` | `JUMP_BACKEDGE_CORRELATED` carries an observed 4-byte `u32 LE` target field. | `MR-04`, `MME-09`, `MME-18`, `MME-19`, `MME-20`, `MLT-10`, `MLT-13`, `MRB-05` |
| `P-18` | `JUMP_IF_FALSE_CORRELATED` carries an observed 4-byte `u32 LE` target field. | `MR-04`, `MME-09`, `MME-18`, `MME-19`, `MME-20`, `MLT-10`, `MLT-13`, `MRB-05` |
| `P-19` | Binary sub-operation byte `0x01` is directly correlated with source `+` in `BINARY_OPCODE_BASE` and `STEP3_ITER_TEST`. | `MR-04`, `MME-13`, `MME-19`, `MME-20`, `MLT-08`, `MLT-13` |
| `P-20` | Binary sub-operation byte `0x12` is directly correlated with source `<` in `STEP3_ITER_TEST`. | `MR-04`, `MME-13`, `MME-19`, `MME-20`, `MLT-08`, `MLT-13` |
| `P-21` | `MINIMAL_BYTECODE_BASE` preserves exact source digest + exact emitted-bytecode artifact digest/bytes and localized PUSH/STORE/terminator segmentation. | `MME-20`, `MLT-13`, `MP-04`, `MP-05` |
| `P-22` | `BINARY_OPCODE_BASE` preserves exact source digest + exact emitted-bytecode artifact digest/bytes and localized LOAD/BINARY/STORE/terminator segmentation. | `MME-13`, `MME-19`, `MME-20`, `MLT-08`, `MLT-13`, `MP-04`, `MP-05` |
| `P-23` | `DISCIPLINE_LOCK` preserves exact source/bytecode digests and localized CALL/RETURN compiler-output shapes, including repeated `0x30 + u32 name index + u16 argc` and explicit-return-correlated `0x31`. | `MME-10`, `MME-19`, `MME-20`, `MLT-11`, `MLT-13`, `MP-04`, `MP-05`, `MRB-05` |
| `P-24` | `STEP3_ITER_TEST` preserves exact source/bytecode digests and a localized WHILE emission containing `< -> 0x21 0x12`, `0x41 + u32(17)` exit field, `+ -> 0x21 0x01`, and `0x40 + u32(4)` back-edge field. | `MME-09`, `MME-13`, `MME-19`, `MME-20`, `MLT-08`, `MLT-10`, `MLT-13`, `MP-04`, `MP-05`, `MRB-05` |
| `P-25` | The controlled `BINARY_OPCODE_BASE.sigmab -> BAD_BINARY_SUBOP_FAULT.sigmab` pair proves a sole one-byte mutation at offset 92 immediately after correlated `0x21`, strengthening only the one-byte BINARY sub-operation-field observation. | `MME-19`, `MME-20`, `MLT-14`, `MLT-20`, `MP-05` |

No other opcode, operand width, binary sub-operation value, header field meaning, VM behavior, or error ABI is promoted.

# NOT_PROVEN

- **VM decode/dispatch remains NOT_PROVEN.** No `sigma_vm.c` bytes, VM decoder/dispatcher source, or instruction-level VM trace is available in the verified WS12 evidence scope. `MME-19`, `MME-20`, `MLT-14`, `MP-04`, and `MRB-05` remain open.
- **Runtime opcode semantics remain NOT_PROVEN.** The `*_CORRELATED` labels are compiler-output localization labels only. They do not prove that the VM decodes or executes those byte values with the corresponding runtime operation.
- **Stack effects remain NOT_PROVEN.** This includes PUSH/POP/LOAD/STORE/BINARY/CALL/RETURN/JUMP/JUMP_IF_FALSE/HALT preconditions, postconditions, underflow behavior, or terminal stack selection.
- **CALL/RETURN runtime ABI remains NOT_PROVEN.** Call-frame layout, argument placement, parameter transfer, return-address convention, return-value convention, recursion, closures, and runtime stack effects are not promoted. `MME-10`, `MME-19`, `MME-20`, `MLT-11`, `MLT-14`, and `MRB-05` remain open.
- **Jump runtime semantics remain NOT_PROVEN.** In `STEP3_ITER_TEST`, the correlated fields `4` and `17` numerically match localized instruction ordinals in that fixture. Relative-versus-absolute interpretation, instruction-pointer basis, signedness, bounds behavior, runtime target interpretation, and branch execution are not generalized. `MME-09`, `MME-19`, `MME-20`, `MLT-10`, `MLT-14`, and `MRB-05` remain open.
- **JUMP_IF_FALSE condition handling remains NOT_PROVEN.** Whether the condition is popped, peeked, retained, coerced, or otherwise handled is not evidenced.
- **HALT runtime behavior remains NOT_PROVEN.** `0xFF` is promoted only as `HALT_OR_TERMINATOR_CORRELATED`; result selection, termination state, fall-through behavior, and end-of-buffer interaction remain unknown.
- **Complete bytecode header/version contract remains NOT_PROVEN.** `SIGMBC01` is only an observed prefix. The following `01 00 00 00` value is observed but its semantic role is not promoted. Header ordering, version field semantics, flags, offsets, counts, compatibility, upgrade/rejection rules, and validation behavior remain open under `MR-04` and `MME-18`.
- **Complete opcode inventory remains NOT_PROVEN.** Only the ten listed source-correlated byte values are promoted; no exhaustiveness claim is made. Unary opcode/sub-op identities are not promoted.
- **Complete binary operator inventory and semantics remain NOT_PROVEN.** Only source `+` and `<` are correlated with `0x01` and `0x12` sub-operation bytes. Operand/result types, coercion, evaluation order, precedence, associativity, truth/comparison semantics, failures, and all other operations remain open under `MME-13`, `MME-14`, `MME-15`, `MLT-08`, and `MLT-09`.
- **Complete constant-pool ABI remains NOT_PROVEN.** WS12 contains additional structural correlations, but this WS06 reopen promotes only the requested directly supported operand fields. Exhaustive constant tags, scalar/string serialization contract, alignment, bounds, offsets, and universal format semantics are not closed.
- **Compiler provenance remains incomplete.** The selected historical source and bytecode artifacts have exact digests and localized correlations, but WS12 performed no fresh `./native/sigmac` invocation and did not bind a compiler binary identity/execution record to the generation of each selected bytecode artifact. `MME-20`, `MLT-13`, `MP-04`, and `MP-05` remain open.
- **Compiler/VM congruence remains NOT_PROVEN.** No selected source-correlated emission is upgraded to VM behavior without VM decode/execute evidence.
- **Malformed/invalid bytecode runtime behavior remains NOT_PROVEN.** `bad_magic.sigmab`, `truncated.sigmab`, and `BAD_BINARY_SUBOP_FAULT.sigmab` are preserved byte artifacts, but VM acceptance/rejection, exact stdout, exact stderr, RC, stable error code, abort point, stack-underflow handling, truncated-operand behavior, and malformed-header behavior are not evidenced. `MR-04`, `MME-20`, `MLT-14`, and `MLT-20` remain open.
- **Audit RC semantics remain NOT_PROVEN.** Historical compiler audit RC `4` and VM audit RC `26` remain opaque labels absent a directly evidenced exit-code contract/localized execution record.
- **Full end-to-end source -> compiler -> bytecode -> decoded instructions -> VM -> stack/state/result/error provenance remains NOT_PROVEN.** WS12 strengthens the source-digest -> preserved-bytecode-digest segment only; `MP-04` remains open.

# CONFLICT

- `NEW_BYTE_EVIDENCE_CONFLICTS=0`. The WS12 localized bytes do not contradict the preserved WS11 reconciliation when evidence layers remain separated.
- **C-26 is not reintroduced.** WS11 remains authoritative that WS06 historically overclaimed WS05 control-flow lowering. This reopen proves only a selected archived `STEP3_ITER_TEST` WHILE compiler-emission correlation (`0x41` exit field and `0x40` back-edge field) and selected `DISCIPLINE_LOCK` CALL/RETURN emission correlations. It does not prove a general `if -> JUMP_IF_FALSE`, `while -> JUMP + JUMP_IF_FALSE`, `for -> while`, or universal return-lowering contract; it does not convert the historical WS06 statement about WS05 into a valid upstream declaration.
- **C-27 is not reintroduced.** The 13 WS04 operation names remain `DECLARED_AUDIT_OPERATION_NAMES`, not a canonical/exhaustive mother-language binary inventory. This reopen promotes only two direct source-to-emitted-sub-op correlations: `+ -> 0x01` and `< -> 0x12`; it does not promote runtime semantics, precedence, type rules, coercion, error behavior, or the remaining operation names to numeric sub-ops.
- The observed `SIGMBC01` prefix does not conflict with the continued `NOT_PROVEN` status of header/version semantics; byte identity and semantic contract are separate claims.
- The controlled `BAD_BINARY_SUBOP_FAULT` mutation does not conflict with the continued `NOT_PROVEN` status of malformed-bytecode behavior; fault input identity and runtime response are separate claims.

# PROPOSED_NORMALIZATION

- Normalize `SIGMBC01` in forward WS06 interpretation as `OBSERVED_8_BYTE_PREFIX`, not as a fully defined header/version/magic contract.
- Normalize the ten numeric bytes only as `SOURCE_CORRELATED_EMISSION` identities:
  - `0x01 PUSH_CONST_CORRELATED`
  - `0x02 POP_OR_DISCARD_RESULT_CORRELATED`
  - `0x10 LOAD_CORRELATED`
  - `0x11 STORE_CORRELATED`
  - `0x21 BINARY_CORRELATED`
  - `0x30 CALL_CORRELATED`
  - `0x31 RETURN_CORRELATED`
  - `0x40 JUMP_BACKEDGE_CORRELATED`
  - `0x41 JUMP_IF_FALSE_CORRELATED`
  - `0xFF HALT_OR_TERMINATOR_CORRELATED`
- Normalize the seven requested operand shapes as `SOURCE_CORRELATED_OPERAND_ENCODING`, bounded to the selected archived fixtures: PUSH_CONST `u32 LE`; LOAD `u32 LE`; STORE `u32 LE`; BINARY `u8`; CALL `u32 LE + u16 LE`; JUMP `u32 LE`; JUMP_IF_FALSE `u32 LE`.
- Normalize only `0x01 <-> source +` and `0x12 <-> source <` as `SOURCE_CORRELATED_BINARY_SUBOP`; do not infer other sub-op values by ordering, audit-name list, host-language convention, or matrix position.
- Normalize `MINIMAL_BYTECODE_BASE`, `BINARY_OPCODE_BASE`, `DISCIPLINE_LOCK`, and `STEP3_ITER_TEST` as `ARCHIVED_SOURCE_BYTECODE_LOCALIZATION` with exact SHA-256 identities. Normalize `BAD_BINARY_SUBOP_FAULT` as `CONTROLLED_ARCHIVED_BYTECODE_MUTATION`, not as a separately compiled source pair and not as runtime fault proof.
- Preserve `VM_DECODE_EXECUTE=NOT_PROVEN`, `STACK_EFFECTS=NOT_PROVEN`, `CALL_FRAME_ABI=NOT_PROVEN`, `JUMP_RUNTIME_TARGET_SEMANTICS=NOT_PROVEN`, `JIF_CONDITION_POP_OR_PEEK=NOT_PROVEN`, `HALT_RUNTIME_BEHAVIOR=NOT_PROVEN`, and `MALFORMED_RUNTIME_ERROR_ABI=NOT_PROVEN`.
- Preserve WS11 C-26 and C-27 reconciliation language. New compiler-emission evidence narrows selected subclaims only; it does not restore the historical WS06 overbroad formulations.
- Do not close a WS10 blocker from a satisfied subclause. A blocker is closed only when every requirement in the WS10 blocker definition is satisfied by direct evidence.

# EVIDENCE

- `BRAIN/WORKSTREAMS/SIGMA_PSI/SIGMA_PSI_WS01_WS12_MASTER_CHECKPOINT_20260826.md` — blob `ce264834e92c7ad6aff0c8a897b3ceb075d592a3`.
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_BYTECODE_ABI_COMPILER_VM_RESULT.md` — historical WS06 blob `683278bd5e868502bdcfc326aa16215930b73151`; not edited.
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS10_COMPLETENESS_CONFLICT_AUDIT_RESULT.md` — blob `3ebe579179e33de65b99e1658ccd39b0182b298e`; authoritative blocker definitions used for closure accounting.
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS11_RECONCILIATION_EVIDENCE_CLOSURE_RESULT.md` — blob `98563853656a4d4552b75e2edadac5214eb0ca4d`; C-26/C-27 normalization and post-WS11 blocker count used here.
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS12_PRIMARY_MACHINE_EVIDENCE_HARVEST_RESULT.md` — blob `0a6e86113cb80d706c54d3550b007d344fa88960`; source-correlated emission boundary and `BLOCKERS_CLOSED=0`, `BLOCKERS_REMAINING=65` evidence.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/01_ARCHIVE_SCOPE_AND_TARGET_HASHES.txt` — blob `3ee99c66ed97e816ff6539286d4a757504622607`; archive provenance and selected artifact SHA-256 identities.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/02_SELECTED_ARCHIVED_SOURCES.txt` — blob `0cfa5dea801b554cab6f47261f982331985be73b`; exact selected source bytes and source SHA-256 identities.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/03_SELECTED_BYTECODE_BASE64.txt` — blob `dc144227bd2902d5d14f5b80e03bf92967fe1200`; exact selected bytecode/fault bytes in base64, byte lengths, and bytecode SHA-256 identities.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/04_LOCALIZED_BYTE_DUMPS_AND_PARSE.txt` — blob `d2eec5c3c911da06679f7a8f858041a813ffc4a6`; exact hexdumps, offsets, source correlations, controlled diff, operand shapes, and explicit `VM_DECODE=NOT_PROVEN` boundary.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/05_TEST_RECORDS.tsv` — blob `b69c0deb0e7957a934898f38c5abfd5a9b50ecc4`; `TESTS_RUN=0` and no fabricated native compiler/VM test rows.
- Historical OPPO archive commit `e56a275f0d366f1d1406c206a737510ce9ddcaa0`; archive scope records Android/Termux AArch64 source root `/data/data/com.termux/files/home/SIGMA/sigma_genesis1`, byte-exact preservation, no recompile, and no rewrite.
- WS12 raw-evidence commits: `9b8e09c7d88ffced018e3d55084e55421c1856ba`, `ffb5cb5889aa4e3f0495eda991be3314a4cb291e`, `c4d8f455d5d910267c3dbced41ee22f0a55d677f`, `ff6263f7f04eadc44d8369a621a23f0e0fc7708d`, `59e698c8f9dbd45743ed3e2439898e2fa6d081a2`, `71e9ba2ad33af0995ffb1ef8da09dbec32005d02`.

# PROVENANCE

REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom  
BRANCH=SIGMA_LIFE  
WORKSTREAM=WS06-REOPEN_BYTECODE_ABI_COMPILER_VM_EVIDENCE_CLOSURE  
SOURCE_HEAD_BEFORE_WRITE=32440fda6664bdd371df713d766aaceea6dae839  
SOURCE_TREE_BEFORE_WRITE=9d5aa9d9bf54b2f2340b615875cc6eb1c2fa8005  
WS12_RESULT_COMMIT=d0bf184e354abb3372981ed10fdbc06f64909989  
TARGET_FILE=BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_REOPEN_EVIDENCE_CLOSURE_RESULT.md  
ADDITIVE_ONLY=YES  
FROZEN_MASTERS_EDITED=NO  
WS06_HISTORICAL_EDITED=NO  
ORIGINAL_WS06_EDITED=NO  
FRESH_NATIVE_EXECUTION=NO  
TESTS_RUN=0  
CLAIM_POLICY=CLAIM<=EVIDENCE  
EVIDENCE_LAYER_PROMOTED=SOURCE_CORRELATED_EMISSION  
VM_RUNTIME_FIELDS_PROMOTED=0  
WS11_C26_REINTRODUCED=NO  
WS11_C27_REINTRODUCED=NO  

# WS06_FIELD_CLOSURE_MATRIX

| WS06 field | New WS12-supported state | Exact WS10 blocker IDs | Closure status |
|---|---|---|---|
| `WS06-NP-001 Bytecode magic/header` | Exact 8-byte `SIGMBC01` prefix observed on four selected valid artifacts; header/version semantics remain unknown. | `MR-04`, `MME-18` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-002 Opcode inventory/numeric values` | Ten numeric byte values promoted only as source-correlated emission identities; inventory is not complete. | `MR-04`, `MME-19`, `MME-20`, `MLT-13` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-003 PUSH_CONST / POP` | `0x01` PUSH_CONST_CORRELATED with u32 LE constant index; `0x02` POP_OR_DISCARD_RESULT_CORRELATED with no observed operand; bounds/stack/runtime semantics remain unknown. | `MR-04`, `MME-18`, `MME-19`, `MME-20`, `MLT-13` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-004 LOAD / STORE` | `0x10` LOAD_CORRELATED and `0x11` STORE_CORRELATED with u32 LE name-index operands; addressing/scope/state/stack semantics remain unknown. | `MR-04`, `MME-18`, `MME-19`, `MME-20`, `MLT-13` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-005 UNARY / BINARY` | `0x21` BINARY_CORRELATED with u8 sub-op; only `+ -> 0x01` and `< -> 0x12` are directly correlated; unary and runtime semantics remain unknown. | `MR-04`, `MME-13`, `MME-18`, `MME-19`, `MME-20`, `MLT-08`, `MLT-13`, `MLT-20` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-006 CALL / RETURN` | `0x30` CALL_CORRELATED with u32 LE callee-name index + u16 LE argc; `0x31` RETURN_CORRELATED; frame/argument/return/runtime semantics remain unknown. | `MR-04`, `MME-10`, `MME-18`, `MME-19`, `MME-20`, `MLT-11`, `MLT-13`, `MRB-05` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-007 JUMP / JUMP_IF_FALSE` | `0x40` back-edge and `0x41` false-exit correlated emissions with u32 LE target fields in `STEP3_ITER_TEST`; runtime target/IP/condition behavior remains unknown. | `MR-04`, `MME-09`, `MME-18`, `MME-19`, `MME-20`, `MLT-10`, `MLT-13`, `MRB-05` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-008 HALT` | `0xFF` promoted only as `HALT_OR_TERMINATOR_CORRELATED`; termination/result semantics remain unknown. | `MR-04`, `MME-19`, `MME-20`, `MLT-13` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-009 Compiler source -> bytecode relation` | Exact selected source/bytecode SHA pairs and localized compiler-output segmentations are preserved; no universal lowering or fresh compiler invocation is proven. | `MME-09`, `MME-10`, `MME-13`, `MME-20`, `MLT-08`, `MLT-10`, `MLT-11`, `MLT-13`, `MP-04`, `MP-05`, `MRB-05` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-010 VM decode/execute relation and stack/state transitions` | No promotion. | `MME-19`, `MME-20`, `MLT-14`, `MP-04`, `MRB-05` | `NOT_PROVEN / OPEN` |
| `WS06-NP-011 Constant pool / operand encoding` | Requested instruction operand widths/endianness are promoted for the selected correlated emissions; complete constant-pool format/tags/serialization/bounds remain open. | `MR-04`, `MME-18`, `MME-19`, `MLT-13` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-012 Bytecode versioning` | No semantic promotion from `SIGMBC01` or adjacent `01 00 00 00`. | `MR-04`, `MME-18` | `NOT_PROVEN / OPEN` |
| `WS06-NP-013 Invalid opcode / malformed bytecode behavior` | Exact malformed/fault artifact identities and controlled one-byte fault mutation are observed; runtime response is not. | `MR-04`, `MME-20`, `MLT-14`, `MLT-20` | `PARTIALLY_EVIDENCED_INPUT_ONLY / OPEN` |
| `WS06-NP-014 Source/bytecode fingerprint and provenance binding` | Exact source and bytecode SHA-256 identities are preserved for selected historical pairs; compiler/VM identity and execution/result linkage remain incomplete. | `MME-20`, `MLT-13`, `MP-04`, `MP-05` | `PARTIALLY_EVIDENCED / OPEN` |
| `WS06-NP-015 Compiler/VM evidence versus declared ABI` | Compiler-output byte correlation exists for selected fields; VM decode/execute congruence remains absent. | `MR-04`, `MME-19`, `MME-20`, `MLT-13`, `MLT-14`, `MP-04`, `MRB-05` | `PARTIALLY_EVIDENCED_COMPILER_SIDE_ONLY / OPEN` |
| `WS06-NP-016 Audit RC semantics` | No promotion; RC `4` and `26` remain opaque aggregate/historical fields. | `MME-20` | `NOT_PROVEN / OPEN` |

No original WS06 NOT_PROVEN class is fully closed by this reopen. Thirteen fields gain bounded partial evidence; three fields (`WS06-NP-010`, `WS06-NP-012`, `WS06-NP-016`) receive no direct promotion. All sixteen remain open as complete WS06 field classes.

# BLOCKERS_REVIEWED

`BLOCKERS_REVIEWED_COUNT=21`

Directly affected/reassessed by the requested WS12 byte evidence:
`MR-04`, `MME-09`, `MME-10`, `MME-13`, `MME-18`, `MME-19`, `MME-20`, `MLT-08`, `MLT-10`, `MLT-11`, `MLT-13`, `MLT-14`, `MLT-20`, `MP-04`, `MP-05`, `MRB-05`.

WS11 C-26/C-27 guard-only reassessment, with no new direct proof sufficient to promote these blocker requirements:
`MME-08`, `MME-12`, `MME-14`, `MME-15`, `MLT-09`.

# BLOCKERS_CLOSED

`BLOCKERS_CLOSED_COUNT=0`

None. WS12 itself records `BLOCKERS_CLOSED=0` and `BLOCKERS_REMAINING=65`, and this WS06 reopen does not identify any WS10 blocker whose full conjunctive definition is now satisfied.

# BLOCKERS_PARTIALLY_EVIDENCED

`BLOCKERS_PARTIALLY_EVIDENCED_COUNT=16`

- `MR-04` — bytecode identity prefix plus partial opcode/operand evidence now exists; canonical complete ABI/header/version/constants/stack/frame/compatibility/malformed contract does not.
- `MME-09` — selected WHILE compiler-emission exit/back-edge localization exists; iteration grammar/protocol/runtime behavior/termination remain open.
- `MME-10` — selected DEF/CALL/RETURN compiler-emission shapes and argc field exist; parameters/arguments/frames/runtime return behavior/recursion/closures remain open.
- `MME-13` — source `+` and `<` correlate with two binary sub-op bytes; executable operator inventory and exact runtime semantics/errors remain open.
- `MME-18` — exact prefix and requested operand widths/endianness are partially evidenced; complete header/version/constants/serialization/offsets/bounds remain open.
- `MME-19` — ten source-correlated numeric instruction bytes, two binary sub-ops, and requested operand shapes are evidenced; complete opcode inventory, runtime behaviors, stack/frame rules, target semantics, decode/dispatch and IP transitions remain open.
- `MME-20` — selected source-to-bytecode compiler-output localization is evidenced; fresh compiler binding, branch/function generalization, VM congruence, malformed behavior, RC semantics, and exact abort/result behavior remain open.
- `MLT-08` — two operator surfaces have localized emitted-byte correlation; runtime result/type/coercion/error behavior required by the blocker is absent.
- `MLT-10` — one source-localized WHILE fixture has correlated branch-emission fields; runtime branch/iteration behavior is absent.
- `MLT-11` — one source-localized DEF/CALL/RETURN fixture has correlated emission shapes; argument/frame/return runtime behavior and failures are absent.
- `MLT-13` — selected source digests, emitted bytecode digests/bytes/hexdumps, and source-correlated segmentations are preserved; the full localized compiler execution linkage required by WS11's blocker interpretation is absent.
- `MLT-14` — malformed/fault bytecode inputs exist, including a controlled sub-op mutation; VM decode/execute stack/frame/state traces and exact VM outcomes are absent.
- `MLT-20` — the controlled one-byte BINARY sub-op mutation gives one bounded operand-width/fault fixture; the complete boundary suite required by the blocker is absent.
- `MP-04` — selected source-digest -> preserved-bytecode-digest/bytes links are available; compiler identity/execution -> decoded VM instructions -> VM identity -> stack/state/result/error trace remains absent.
- `MP-05` — this reopen attaches per-promotion exact evidence paths/hashes and distinguishes localized evidence from aggregate labels; repository-wide per-claim reproducibility for every executable claim remains incomplete.
- `MRB-05` — selected source control/function forms now correlate to compiler-output bytecode segments; VM operations and exact stack/frame/state effects remain absent.

The C-26/C-27 guard-only blockers `MME-08`, `MME-12`, `MME-14`, `MME-15`, and `MLT-09` remain open without new direct promotion from the requested WS12 evidence.

# BLOCKERS_REMAINING

`BLOCKERS_REMAINING_COUNT=65`

Global post-WS11 count remains 65. No WS10 blocker is fully closed by this additive WS06 reopen. The promoted evidence closes subclaims only.

# READY_FOR_MERGE

NO

Reason: WS06 now has materially stronger primary archived compiler-output evidence, but the complete bytecode ABI/header/version/constants contract, complete opcode inventory, VM decode/dispatch, stack effects, call frames, runtime jump/condition/HALT semantics, malformed-bytecode behavior, fresh compiler/VM linkage, and end-to-end provenance required by the open WS10 blockers are not proven.

# READY_FOR_V1_2_CANDIDATE

NO

Reason: mandatory executable-language blockers remain open; `BLOCKERS_REMAINING=65`; WS06 cannot be treated as a complete executable ABI/compiler/VM contract.

NEW_ENTRIES=25
DUPLICATES=0
CONFLICTS=0
MISSING=16
BLOCKERS_CLOSED=0
BLOCKERS_REMAINING=65
READY_FOR_MERGE=NO
READY_FOR_V1_2_CANDIDATE=NO