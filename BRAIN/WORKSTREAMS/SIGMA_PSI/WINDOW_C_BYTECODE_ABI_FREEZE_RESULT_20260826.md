# WINDOW C — SIGMA BYTECODE ABI FREEZE RESULT — 2026-08-26

ROLE=WINDOW_C_SIGMA_BYTECODE_ABI_FREEZE
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
SOURCE_HEAD_BEFORE_WINDOW_C=58c9e27d23403e16d5319c2e278a7f8683ca2f3d
WINDOW_A=CLOSED
WINDOW_B=CLOSED
CLAIM_POLICY=CLAIM <= EVIDENCE
SOURCE_CORRELATED_NE_VM_SEMANTICS=YES
DESCRIPTION_NE_EXECUTION=YES
MAPPING_NE_VALIDATION=YES
GLYPH_NE_CLAIM=YES
MATRIX_POSITION_NE_OPCODE_ASSIGNMENT=YES

Window C freezes only the presently evidenced bytecode ABI surface. It does not define a new ABI, infer VM stack effects, promote compiler emission into native VM decode semantics, or treat the 256-symbol 0xNN reference matrix as an opcode table.

Evidence levels used throughout this result are kept separate:

- `A_BYTE_EXACT_OBSERVED`: exact serialized bytes/offsets/shapes are directly present in preserved artifacts; semantic field meaning may remain unknown.
- `B_SOURCE_CORRELATED`: exact bytes are present and an existing source/bytecode pair localizes the field to a source construct or serialized table role.
- `C_VM_RUNTIME_LOCALIZED`: the exact ABI field/value is independently localized to native VM decode/validation/execution. No reviewed field reaches this level in Window C.

The field ledger contains 61 reviewed ABI questions: 2 pure byte-exact observations, 37 source-correlated fields that also have byte-exact evidence, 22 unresolved fields, and 0 exact VM-runtime-localized ABI fields.

## CURRENT_HASH_SCOPE

AUTHORITATIVE_RUNTIME_SOURCE_SHA256=57b275467d42de4b5404a57f486a1706a46f5a4c0626bbec0c045757cde0602e
AUTHORITATIVE_COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
AUTHORITATIVE_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
FRESH_WINDOW_A_BYTECODE_SHA256=903d78f901ffca4b523d4df3b19e875f1a5f4788bf85fcdbdde611621b769e7a
FRESH_WINDOW_A_BYTECODE_SIZE=8273

The fresh 8273-byte Window A artifact is used only for current source -> current compiler -> fresh bytecode -> current VM provenance/execution scope. Its bytes are not reinterpreted in Window C.

The WS12 byte-exact corpus is historical preserved OPPO/Termux evidence under archive commit `e56a275f0d366f1d1406c206a737510ce9ddcaa0`. That archive does not itself bind the selected bytecode to the current compiler binary.

One bounded current-compiler bridge exists: Window A test `WA-LIT-01` records current compiler SHA-256 `65f692...` compiling the exact neutral source form containing `⚡ a: 1;` with RC=0 to a 53-byte artifact whose SHA-256 is `26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875`. WS12 preserves exact bytes for a 53-byte `MINIMAL_BYTECODE_BASE.sigmab` with that same hash. Window C treats this only as a hash/size artifact-identity bridge for that bounded compiler output, not as proof that every archived ABI field is current-compiler canonical.

CURRENT_VM_WHOLE_BYTECODE_EXECUTION=PROVEN_IN_TESTED_SCOPE
CURRENT_VM_EXACT_OPCODE_MAPPING=NOT_PROVEN
CURRENT_VM_EXACT_HEADER_VALIDATION=NOT_PROVEN
CURRENT_VM_PER_OPCODE_STACK_EFFECTS=NOT_PROVEN
CURRENT_VM_EXACT_HALT_RESULT_SEMANTICS=NOT_PROVEN

## ABI_MAGIC_HEADER

`C-HDR-001` is byte-exact: each of the four selected valid artifacts starts at offsets `0..7` with:

`53 49 47 4d 42 43 30 31` = ASCII `SIGMBC01`.

This freezes an observed exact 8-byte file prefix on the selected valid compiler-output artifacts. It does not prove native VM magic validation behavior or compatibility semantics.

`C-HDR-002` is separately byte-exact: offsets `8..11` are `01 00 00 00` in all four selected valid artifacts, an LE-u32-shaped value `1`.

No semantic promotion is made from either the ASCII suffix `01` or the adjacent numeric value `1`. Specifically:

- exact header/body boundary beyond the 8-byte prefix = `NOT_PROVEN`;
- whether offsets `8..11` are a version, format ID, flags, or another field = `NOT_PROVEN`;
- version compatibility/upgrade/rejection policy = `NOT_PROVEN`;
- header global offset table = `NOT_PROVEN`;
- required alignment/padding = `NOT_PROVEN`.

The source-correlated parse places a constant-count-shaped u32 at offsets `12..15`, but this does not by itself define the formal header boundary.

## CONSTANT_POOL

The selected byte-exact artifacts source-correlate with a sequential constant-pool shape:

1. `CONSTANT_COUNT`: u32 LE at offsets `12..15`, observed values `1`, `2`, `4`, `7`.
2. Entry order acts as a zero-based ordinal in selected `PUSH_CONST_CORRELATED` operands.
3. Observed constant-correlated tag `0x00`: no payload observed in the selected `DISCIPLINE_LOCK` NULL-correlated entry.
4. Observed integer-correlated tag `0x02`.
5. After `0x02`: 8-byte little-endian integer-shaped payload. Selected small nonnegative source values `0,1,2,3` match these payload numerics. Signedness, full range, overflow policy, and runtime INT representation are not proven.
6. Observed string-correlated tag `0x04`.
7. After `0x04`: u32 LE byte length.
8. Then exactly that many source-correlated bytes. The selected strings are ASCII-only and therefore UTF-8-compatible, but arbitrary non-ASCII encoding/normalization is not proven.

Examples include:

- `STEP3_ITER_TEST`: tag `04`, length `05 00 00 00`, bytes `49 4e 44 45 58` (`INDEX`);
- `DISCIPLINE_LOCK`: tag `04`, length `0a 00 00 00`, then `write_text`;
- `DISCIPLINE_LOCK`: tag `00` at offset `31` with no payload observed.

The following remain exact unresolved constant-pool ABI fields: FLOAT tag/payload, BOOL tag/payload, non-ASCII string encoding policy, exhaustive tag inventory, and pool alignment/padding.

Window B's type/literal result remains controlling: compiler acceptance of `1`, `1.5`, quoted strings, `NULL`, or `null` is not promoted into runtime type/value mapping. `NULL` source correlation to archived tag `0x00` is therefore not a claim about current VM NULL representation or lowercase `null`.

## NAME_TABLE

Across the selected artifacts, the name table source-correlates with:

- a u32 LE name count after the constant pool;
- each name encoded as u32 LE byte length followed by that many bytes;
- selected name bytes matching source identifiers/callee names;
- u32 LE name indices in LOAD, STORE, CALL, function-name, and parameter-name contexts;
- zero-based name ordinal correlation in the selected fixtures.

Observed name counts are `1`, `3`, `3`, and `14`. Examples include `a`, `i`, `limit`, `print`, `host_call`, `save`, `load`, `VERIFIED`.

Selected names are ASCII-only. Arbitrary Unicode name encoding/normalization and a universal name-table alignment/padding rule remain `NOT_PROVEN`.

## FUNCTION_RECORDS

`DISCIPLINE_LOCK.sigmab` is the selected function-bearing exact artifact. It contains function-count field `03 00 00 00` at offsets `407..410`, correlating with three source `DEF` forms.

The source-correlated record shape is:

`u32 LE function-name index`
`u16 LE parameter count`
`parameter_count × u32 LE parameter-name index`
`u32 LE instruction count`
`instruction bytes immediately following`

Exact localized records:

- function 0, record offset `411`: name index `0` -> `host_call`; parameter count `4`; parameter name indices `1,2,3,4` -> `op,a,b,c`; instruction count `6`; code offsets `437..464`.
- function 1, record offset `465`: name index `6` -> `save`; parameter count `2`; parameter indices `7,8` -> `path,content`; instruction count `6`; code offsets `483..510`.
- function 2, record offset `511`: name index `9` -> `load`; parameter count `1`; parameter index `7` -> `path`; instruction count `6`; code offsets `525..552`.

The function-record u16 field is correlated with source definition parameter count. It is not promoted to runtime argument transfer semantics. CALL has its own separately observed u16 argument-count operand.

No separate serialized code-offset field, code-byte-length field, local-count field, or flags field is localized. Their universal absence is also not claimed; they remain `NOT_PROVEN`. The u32 instruction count is not relabeled as a byte length.

After the function section, each selected artifact has a u32 LE main-instruction-count field followed immediately by main instruction bytes. Observed counts are `3`, `9`, `18`, and `19`.

## OPCODE_TABLE

The following are exact compiler-output byte shapes with source-correlated labels only:

| Byte | Source-correlated label | Observed emitted operand shape | VM runtime mapping |
|---|---|---|---|
| `0x01` | `PUSH_CONST_CORRELATED` | u32 LE constant index | NOT_PROVEN |
| `0x02` | `POP_OR_DISCARD_RESULT_CORRELATED` | none observed | NOT_PROVEN |
| `0x10` | `LOAD_CORRELATED` | u32 LE name index | NOT_PROVEN |
| `0x11` | `STORE_CORRELATED` | u32 LE name index | NOT_PROVEN |
| `0x21` | `BINARY_CORRELATED` | u8 sub-op | NOT_PROVEN |
| `0x30` | `CALL_CORRELATED` | u32 LE callee-name index + u16 LE argc | NOT_PROVEN |
| `0x31` | `RETURN_CORRELATED` | none observed | NOT_PROVEN |
| `0x40` | `JUMP_BACKEDGE_CORRELATED` | u32 LE target field | NOT_PROVEN |
| `0x41` | `JUMP_IF_FALSE_CORRELATED` | u32 LE target field | NOT_PROVEN |
| `0xFF` | `HALT_OR_TERMINATOR_CORRELATED` | none observed | NOT_PROVEN |

The ten numeric values are not frozen as an exhaustive opcode inventory. No unobserved opcode assignment is invented. In particular, 0xNN positions in the 256-symbol reference matrix are not bytecode opcode assignments unless independently machine-evidenced.

No stack effect is claimed for any row. `0x02` is not promoted to a POP stack effect; the label remains `POP_OR_DISCARD_RESULT_CORRELATED`. `0x31` does not establish runtime return-value convention. `0xFF` does not establish canonical HALT semantics.

## BINARY_SUBOPS

Exactly two binary sub-operation mappings are frozen, both at source-correlation level:

- `0x21 0x01` correlates with source `+` in `BINARY_OPCODE_BASE` and `STEP3_ITER_TEST`.
- `0x21 0x12` correlates with source `<` in `STEP3_ITER_TEST`.

The controlled artifact pair `BINARY_OPCODE_BASE.sigmab` -> `BAD_BINARY_SUBOP_FAULT.sigmab` is equal-length 99 bytes and differs at one byte only: offset `92`, `0x01 -> 0xFF`, immediately after byte `0x21` at offset `91`. This strengthens the one-byte sub-op-field observation only.

No numeric mappings for SUB/MUL/DIV/FLOORDIV/MOD/POW/EQ/NE/etc. are invented. Runtime binary semantics, operand/result types, coercion, evaluation order, comparison truth behavior, and stack effects are outside this freeze.

## OPERAND_ENCODING

Seven emitted opcode operand encodings are proven at byte/source-correlation level:

- `0x01`: 4-byte u32 LE constant index.
- `0x10`: 4-byte u32 LE name index.
- `0x11`: 4-byte u32 LE name index.
- `0x21`: 1-byte u8 sub-op.
- `0x30`: 4-byte u32 LE callee-name index followed by 2-byte u16 LE argc.
- `0x40`: 4-byte u32 LE target field.
- `0x41`: 4-byte u32 LE target field.

No operand is observed for `0x02`, `0x31`, or `0xFF`.

Additional source-correlated structural multi-byte encodings include u32 LE constant/name/function/main counts, u32 LE string/name byte lengths, u32 LE function/parameter name indices, u16 LE function parameter count, and 8-byte little-endian integer-shaped constant payloads.

This does not prove a universal endianness rule for every possible ABI field, signedness for integer/jump payloads, bounds validation, or malformed operand handling.

## JUMP_ENCODING

`STEP3_ITER_TEST.sigmab` provides the only selected exact jump-target localization:

- at offset `120`: `41 11 00 00 00`, target field value `17`;
- at offset `160`: `40 04 00 00 00`, target field value `4`.

In this fixture, value `17` equals the localized terminal instruction ordinal `17`, and value `4` equals the localized loop-condition reload instruction ordinal `4`.

Freeze boundary:

FIXTURE_LOCAL_TARGET_EQUALS_INSTRUCTION_ORDINAL=YES
UNIVERSAL_ABSOLUTE_VS_RELATIVE_TARGET_RULE=NOT_PROVEN
UNIVERSAL_BYTE_OFFSET_VS_INSTRUCTION_INDEX_RULE=NOT_PROVEN
COMPILER_BACKPATCH_OR_PATCHING_ALGORITHM=NOT_PROVEN
TARGET_SIGNEDNESS_AND_BOUNDS_VALIDATION=NOT_PROVEN
VM_IP_TRANSITION_SEMANTICS=NOT_PROVEN
JUMP_IF_FALSE_POP_OR_PEEK=NOT_PROVEN

The fixture-local equality is compiler-emission correlation. It is not promoted into native VM decode semantics.

## TERMINATION_ENCODING

Across all four selected valid bytecode artifacts:

- the last byte of the main stream and file is `0xFF`;
- the localized main instruction count includes that `0xFF` as the final instruction ordinal.

Exact terminal offsets are:

- MINIMAL: `52`;
- BINARY: `98`;
- STEP3: `165`;
- DISCIPLINE: `643`.

The only frozen label is `HALT_OR_TERMINATOR_CORRELATED`.

Separate current VM evidence proves normal termination in tested bytecode programs, but exact `0xFF` native decoder mapping, result selection/storage/propagation, fall-through behavior, and behavior when the byte stream ends without this terminator remain `NOT_PROVEN`.

## BYTE_EXACT_EVIDENCE

Primary preserved exact artifacts used:

| Artifact | Length | SHA-256 |
|---|---:|---|
| `MINIMAL_BYTECODE_BASE.sigmab` | 53 | `26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875` |
| `BINARY_OPCODE_BASE.sigmab` | 99 | `23a483ddea89cf36a36618cc7d192d1a3efd51927ed3272a77574be23d14a13c` |
| `STEP3_ITER_TEST.sigmab` | 166 | `e15e17e7fa3aace360bddd0062880c3e10ac3e869ef256f05f073aa2f6381e4a` |
| `DISCIPLINE_LOCK.sigmab` | 644 | `e3d4f6169fbb83d0df8977f8029f53a2181531582954898e469e0e0e6ac1a4a0` |
| `BAD_BINARY_SUBOP_FAULT.sigmab` | 99 | `629ddc92b5cc1e0920bdc1f8fbc2d361d01d57f26245788f243d924e8e64f8d5` |
| `bad_magic.sigmab` | 19 | `b449859fe2af41be3e2845a0e85d31900d61d07d2164cae330bb676642946ad4` |
| `truncated.sigmab` | 8 | `f666e4ccff096253426e4111d6746bd62c5b228422fb6617a873ee7af2746501` |

Malformed shapes catalogued without error-semantics promotion:

- `bad_magic.sigmab`: exact bytes decode as `NOT_SIGMA_BYTECODE\n`;
- `truncated.sigmab`: exact bytes are only `SIGMBC01`;
- `BAD_BINARY_SUBOP_FAULT.sigmab`: one exact mutation at offset `92`.

VM acceptance/rejection, stdout, stderr, RC, error taxonomy, abort point, and malformed bounds behavior are not promoted in Window C.

Window C derived evidence written under:

- `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_C_BYTECODE_ABI/WINDOW_C_SELECTED_BYTECODE_REPARSE_20260826.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_C_BYTECODE_ABI/WINDOW_C_ABI_FIELD_LEDGER_20260826.tsv`
- `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_C_BYTECODE_ABI/WINDOW_C_TARGETED_TEST_DECISION_20260826.txt`

## SOURCE_CORRELATED_FIELDS

The 37 source-correlated ABI fields are distributed as:

CONSTANT_POOL=8
NAME_TABLE=5
FUNCTION_RECORDS=6
MAIN_STREAM=2
OPCODE_FIELDS=10
BINARY_SUBOPS=2
JUMP_TARGET_CORRELATIONS=2
TERMINATION_RELATIONS=2

Every one of these 37 fields also has byte-exact evidence in the selected preserved artifacts. The source correlation is the permitted claim ceiling for field meaning. It does not promote native VM decode, runtime stack effects, runtime frame layout, runtime type representation, or error semantics.

The current compiler hash/size bridge strengthens only the bounded minimal artifact identity described in `CURRENT_HASH_SCOPE`. It does not automatically promote the rest of the archived source correlations to the current compiler epoch.

## VM_RUNTIME_LOCALIZED_FIELDS

VM_RUNTIME_LOCALIZED_FIELDS=0

The separate current VM scope proves bytecode loading/execution and normal termination in tested programs, and behavior-level call/return and branch/loop execution. However:

- native opcode dispatch has not been localized per numeric byte;
- exact header validation has not been localized;
- exact jump-field interpretation has not been localized;
- exact call-frame/argument/return-value ABI fields have not been localized;
- per-opcode stack effects have not been localized;
- exact `0xFF` HALT result semantics have not been localized.

Therefore no exact ABI field/value is counted at evidence level C.

## NOT_PROVEN

Exactly 22 ledger fields remain unresolved:

HEADER=4
- formal header boundary beyond the prefix;
- format/version semantics;
- header/global offset table;
- header alignment/padding rule.

CONSTANT_POOL=5
- FLOAT tag/payload;
- BOOL tag/payload;
- arbitrary non-ASCII string encoding;
- exhaustive constant-tag inventory;
- constant-pool alignment/padding.

NAME_TABLE=1
- name-table alignment/padding.

FUNCTION_RECORDS=4
- separate serialized code-offset field;
- separate serialized code-byte-length field;
- local-count field;
- flags field.

OPCODE=1
- exhaustive opcode inventory.

BINARY_SUBOP=1
- exhaustive binary sub-op inventory.

JUMP_ENCODING=4
- universal absolute-vs-relative rule;
- universal byte-offset-vs-instruction-index rule;
- compiler patching/backpatch algorithm;
- target signedness/bounds validation.

TERMINATION=2
- exact runtime HALT/result semantics;
- end-of-buffer behavior without a terminator.

Additional semantic limits attached to proven source-correlated fields remain in force: VM decode semantics, stack effects, frame layout, runtime type/value mappings, bounds/error behavior, and universal completeness are not inferred.

## CONFLICTS

CONFLICTED_FIELDS=0

No byte-exact field conflict exists among the four selected valid artifacts for the localized shapes. The historical-archive versus current-compiler provenance difference is a scope boundary, not a contradictory field value. The Window B cross-epoch `//` source-surface conflict is not promoted into an ABI numeric sub-op conflict because no `//` binary sub-op number is evidenced in Window C.

Historical overbroad WS06 formulations remain superseded by the bounded WS06-reopen normalization. Window C does not restore any overbroad opcode/runtime/stack/header claim.

## FALSE_PROOF_RISK_AUDIT

1. `SOURCE_CORRELATED_EMISSION -> VM_SEMANTICS`: blocked. All opcode labels remain `*_CORRELATED`; exact VM numeric mapping is not claimed.
2. `0x02 -> POP_STACK_EFFECT`: blocked. No stack effect is inferred.
3. `0xFF -> CANONICAL_HALT_RESULT_SEMANTICS`: blocked. Only terminal emission is frozen.
4. `JUMP_FIELD_4_OR_17 -> UNIVERSAL_ABSOLUTE_INSTRUCTION_INDEX_ABI`: blocked. Equality to instruction ordinals is fixture-local only.
5. `TAG_0x00/0x02/0x04 -> RUNTIME_TYPE_REPRESENTATION`: blocked. Tags remain source-correlated serialization labels.
6. `SAME_SHA -> UNIVERSAL_CURRENT_ABI`: blocked. The current minimal hash/size match is one bounded artifact-identity bridge only.
7. `0xNN_REFERENCE_MATRIX_POSITION -> OPCODE_VALUE`: blocked. Matrix positions are reference positions unless separately machine-evidenced.
8. `MALFORMED_BYTES -> ERROR_TAXONOMY`: blocked. Window C catalogs shapes only; error RC/stderr semantics remain for Window E.
9. `COMPILER_ACCEPTANCE -> RUNTIME_SEMANTICS`: blocked. Window B literal/type boundaries remain preserved.
10. `DESCRIPTION/MAPPING -> VALIDATION/EXECUTION`: blocked. No implementation description is upgraded without machine localization.

GPT_ANSWER_IMPOSITION_USED=NO
HOST_LOGIC_SUBSTITUTED_FOR_SIGMA=NO
NEW_ABI_SEMANTICS_INVENTED=NO
VM_STACK_EFFECTS_INFERRED=NO

## TARGETED_TESTS

TARGETED_TEST_REQUIRED_FOR_CURRENT_FREEZE=NO
TARGETED_TESTS_RUN=0
SEMANTIC_CAPABILITY_RERUNS=0
MANUAL_BYTECODE_MUTATION_EXECUTED=NO
SUBSTITUTE_COMPILER_OR_VM_USED=NO

Reason: this is an evidence-bounded freeze, and unresolved fields are permitted to remain `NOT_PROVEN`. Existing byte-exact evidence is sufficient to freeze the current evidence state without manufacturing version semantics, missing constant tags, opcode assignments, stack effects, jump runtime rules, or frame semantics.

The live OPPO/Termux primary native toolchain is not available through this execution session. No alternate compiler, VM, emulator, wrapper, or host semantic implementation was used.

DUPLICATE_TESTS_AVOIDED=21
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

## PROVENANCE

AUTHORITATIVE_MINIMAL_CHECKPOINT=`BRAIN/WORKSTREAMS/SIGMA_PSI/SIGMA_ACTIVE_MINIMAL_CHECKPOINT_AFTER_WINDOW_B_20260826.md`
WINDOW_A_BASELINE=`BRAIN/WORKSTREAMS/SIGMA_PSI/WINDOW_A_EXECUTABLE_SURFACE_FINAL_FREEZE_20260826.md`
WINDOW_A_BASELINE_COMMIT=`fa683b1f0d24085e1c109bf3d5e1c330ab22c177`
WINDOW_B_BASELINE=`BRAIN/WORKSTREAMS/SIGMA_PSI/WINDOW_B_TYPES_VALUES_OPERATORS_FREEZE_RESULT_20260826.md`
WINDOW_B_BASELINE_COMMIT=`caa0100d7bbbe934f77252125479b7d8af548960`
WINDOW_B_EVIDENCE_REGISTER=`BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_B_TYPES_VALUES_OPERATORS/WINDOW_B_EVIDENCE_REGISTER_FINAL_20260826.md`
WINDOW_B_EVIDENCE_REGISTER_COMMIT=`7bd34584ec90852d9a66dcfec0dcd460a708982c`

ABI_PRIOR_EVIDENCE:
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS12_PRIMARY_MACHINE_EVIDENCE_HARVEST_RESULT.md`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_REOPEN_EVIDENCE_CLOSURE_RESULT.md`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/SIGMA_CURRENT_VM_RUNTIME_SCOPE_20260826.md`
- `BRAIN/WORKSTREAMS/SIGMA_PSI/WINDOW_A_PROVENANCE_LINKAGE_CLOSURE_20260826.md`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/00_SESSION_ACCESS_BOUNDARY.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/01_ARCHIVE_SCOPE_AND_TARGET_HASHES.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/02_SELECTED_ARCHIVED_SOURCES.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/03_SELECTED_BYTECODE_BASE64.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/04_LOCALIZED_BYTE_DUMPS_AND_PARSE.txt`
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/05_TEST_RECORDS.tsv`
- exact current-compiler dependency `BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_A_SURFACE_PROBES/WINDOW_A_LITERAL_BATCH1_20260826.md`

WS12_ARCHIVE_COMMIT=`e56a275f0d366f1d1406c206a737510ce9ddcaa0`
WINDOW_C_SOURCE_HEAD_BEFORE_WRITE=`58c9e27d23403e16d5319c2e278a7f8683ca2f3d`
WINDOW_C_REPARSE_COMMIT=`a43d576106ea98fd8373a74f978f06e05c6b3052`
WINDOW_C_FIELD_LEDGER_COMMIT=`acffb0145c5238927fa7afdc5e7bea76950d59b6`
WINDOW_C_TARGETED_TEST_DECISION_COMMIT=`c2c4b9d845f8b53e8e2e8cc3193ddaca2b6ac4ea`

## FREEZE_DECISION

WINDOW_C_FREEZE_SCOPE=CURRENT_EVIDENCE_BOUNDED_BYTECODE_ABI
WINDOW_C_FREEZE_COMPLETE=YES

The evidence-bounded ABI is frozen without filling unknown fields. The freeze is complete because every requested ABI category has been audited and each field is either byte-exact/source-correlated at its exact scope or explicitly `NOT_PROVEN`.

READY_FOR_WINDOW_D=YES

Window D may proceed using only the frozen Window C claim ceiling. It must not upgrade source-correlated opcode labels into native VM opcode semantics or stack/frame effects.

READY_FOR_PUBLIC_LANGUAGE_SPEC=NO

A public canonical language/ABI specification remains blocked by unresolved version/header meaning, complete constant/opcode/sub-op inventories, universal jump-target rules, exact VM decode/validation mapping, stack/frame semantics, and error behavior.

Counting rule for the ending contract: `BYTE_EXACT_FIELDS_PROVEN` counts the 2 A-level fields plus all 37 B-level fields because each B-level field is backed by exact selected bytes; `SOURCE_CORRELATED_FIELDS` counts only the 37 B-level rows; `VM_RUNTIME_LOCALIZED_FIELDS` counts exact ABI fields at C level and is zero. Category-specific proven counts use the same ledger and do not claim runtime semantics.

ABI_FIELDS_REVIEWED=61
BYTE_EXACT_FIELDS_PROVEN=39
SOURCE_CORRELATED_FIELDS=37
VM_RUNTIME_LOCALIZED_FIELDS=0
OPCODES_REVIEWED=10
OPCODES_BYTE_EXACT_PROVEN=10
BINARY_SUBOPS_PROVEN=2
OPERAND_ENCODINGS_PROVEN=7
HEADER_FIELDS_PROVEN=2
CONSTANT_POOL_FIELDS_PROVEN=8
FUNCTION_RECORD_FIELDS_PROVEN=6
JUMP_ENCODING_FIELDS_PROVEN=4
TERMINATION_ENCODING_FIELDS_PROVEN=3
NOT_PROVEN_FIELDS=22
CONFLICTED_FIELDS=0
TARGETED_TESTS_RUN=0
DUPLICATE_TESTS_AVOIDED=21
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21
GPT_ANSWER_IMPOSITION_USED=NO
HOST_LOGIC_SUBSTITUTED_FOR_SIGMA=NO
NEW_ABI_SEMANTICS_INVENTED=NO
VM_STACK_EFFECTS_INFERRED=NO
WINDOW_C_FREEZE_COMPLETE=YES
READY_FOR_WINDOW_D=YES
READY_FOR_PUBLIC_LANGUAGE_SPEC=NO