# WS12 — PRIMARY MACHINE EVIDENCE HARVEST RESULT

WORKSTREAM_ID=WS12  
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom  
BRANCH=SIGMA_LIFE  
SOURCE_HEAD_AT_START=849efdf8a7d74bd6d467562bfb6e0268fae9663a  
PRIMARY_ROOT_REQUESTED=`~/SIGMA/sigma_genesis1`  
NATIVE_TOOLCHAIN_REQUESTED=`SIGMA source -> ./native/sigmac -> .sigmab -> ./native/sigma-vm.v09_candidate`  
CLAIM_POLICY=`CLAIM <= EVIDENCE`  
WRAPPERS_OR_LAUNCHERS_CREATED=NO  
FRESH_NATIVE_EXECUTION=NO  

## EXECUTIVE RESULT

WS12 could not access the requested live primary root in this execution host: `$HOME=/home/oai`, so the requested root resolved to `/home/oai/SIGMA/sigma_genesis1`; `ls -ld` returned RC `2`, empty stdout, and exact stderr `ls: cannot access '/home/oai/SIGMA/sigma_genesis1': No such file or directory`. This is a session-host access boundary only and is **not** evidence that the OPPO/Termux primary tree is absent.

No substitute compiler, VM, wrapper, launcher, emulator, inferred runtime, or newly invented SIGMA grammar was used. Because the required native binaries were not accessible, WS12 performed **zero fresh compiler/VM tests**. The required test-record schema is preserved with zero data rows under `BRAIN/EVIDENCE/SIGMA_PSI/WS12/05_TEST_RECORDS.tsv`.

The existing byte-exact OPPO/Termux archive **is** primary-machine evidence for preserved artifacts. Its scope records source root `/data/data/com.termux/files/home/SIGMA/sigma_genesis1`, Android/Termux AArch64, `PRESERVE_BYTE_EXACT`, `NO_RECOMPILE=TRUE`, `NO_REWRITE=TRUE`, 392 SIGMA sources and 390 bytecode files, total 782 archived artifacts. It also records SHA-256 identities for `sigmac.c`, `sigma_vm.c`, and `compiler_self.sigma`, although those three source bytes are not present in the verified archive root.

WS12 localizes exact byte structure from selected existing source/bytecode pairs. This is sufficient to promote a bounded set of **SOURCE_CORRELATED_EMISSION** observations: `SIGMBC01` prefix bytes, repeated serialized field shapes, numeric compiler-output bytes for PUSH/LOAD/STORE/BINARY/CALL/RETURN/JUMP/JUMP_IF_FALSE/terminator-correlated emissions, and directly observed operand widths. It is **not** sufficient to promote VM decode/dispatch, runtime instruction behavior, stack effects, frame layout, error RC semantics, or a complete ABI contract.

## 1. PRIMARY ARTIFACT INVENTORY

| Requested artifact | WS12 status | Direct evidence | Promotion boundary |
|---|---|---|---|
| `./native/sigmac` | LIVE_PRIMARY_UNAVAILABLE; NOT_PRESERVED_IN_VERIFIED_ARCHIVE_SCOPE | live root not mounted; archive root contains no native binary copy | binary SHA-256 and behavior NOT_PROVEN in WS12 |
| `./native/sigma-vm.v09_candidate` | LIVE_PRIMARY_UNAVAILABLE; NOT_PRESERVED_IN_VERIFIED_ARCHIVE_SCOPE | same access/archive boundary | binary SHA-256 and behavior NOT_PROVEN in WS12 |
| `sigmac.c` | IDENTITY_ONLY | archive scope records SHA-256 `e31fad26611fc95772a9a454eae6a735b220a8b7aa2ca95970c3623028ad0452` | source bytes/implementation not inspected |
| `sigma_vm.c` | IDENTITY_ONLY | archive scope records SHA-256 `8a567de997c335b38f49062622e3ec995b752b335a952b076d1f9283457fcae2` | decoder/dispatcher source not inspected |
| `compiler_self.sigma` | IDENTITY_ONLY | archive scope records SHA-256 `b00b415cc49d042ef152196633c5de4e7fffdf35da84bd900d31b599a9b60af7` | source bytes not inspected |
| `.sigma_exec/*.sigma` | FOUND_ARCHIVED_BYTE_EXACT | 392 archived sources | existing source corpus; no grammar invented |
| `.sigma_exec/*.sigmab` | FOUND_ARCHIVED_BYTE_EXACT | 390 archived bytecode artifacts | bytes are primary artifacts; semantics require localization |
| `.sigma_tmp/*` | UNKNOWN_LIVE_PRIMARY | not preserved in verified archive root; live tree inaccessible | no absence claim about OPPO tree |
| compiler/VM traces | NO_LOCALIZED_PRIMARY_TRACE_SURFACED | archive/search did not surface instruction-level compiler/VM trace | stack/frame/IP behavior remains NOT_PROVEN |
| bytecode dumps | DERIVED_AND_PRESERVED_BY_WS12 | exact archived bytes decoded to hexdumps under WS12 evidence | dumps preserve bytes; interpretation is separately scoped |
| opcode evidence | FOUND_PARTIAL | selected paired source/bytecode artifacts plus controlled mutation | SOURCE_CORRELATED_EMISSION only; not VM decode proof |

## 2. BYTECODE MAGIC / HEADER-ADJACENT STRUCTURE

Selected valid archived artifacts `MINIMAL_BYTECODE_BASE.sigmab`, `BINARY_OPCODE_BASE.sigmab`, `STEP3_ITER_TEST.sigmab`, and `DISCIPLINE_LOCK.sigmab` all begin with exact bytes:

`53 49 47 4d 42 43 30 31` = ASCII `SIGMBC01`.

**Localized claim:** `SIGMBC01` is an observed eight-byte prefix on these preserved valid compiler-output artifacts.

Immediately after that prefix, the selected valid artifacts all contain `01 00 00 00`, an observed little-endian-u32-shaped value `1`. Its semantic role/version meaning is **NOT_PROVEN**.

Across the selected corpus, repeated source correlation supports these serialization shapes without promoting a complete ABI:

- u32 little-endian-shaped counts for constants, names, functions, and instruction counts;
- constant-correlated tag `0x00` with no payload for NULL entries;
- constant-correlated tag `0x02` with an 8-byte little-endian integer payload;
- constant-correlated tag `0x04` with u32 little-endian byte length followed by UTF-8 string bytes;
- name strings as u32 little-endian byte length plus UTF-8 bytes;
- function-bearing `DISCIPLINE_LOCK.sigmab` source-correlates with records containing u32 function-name index, u16 parameter count, u32 parameter-name indices, u32 instruction count, then instruction bytes.

This does **not** establish exhaustive tags, bounds behavior, compatibility/version policy, all header fields, alignment, or universal ABI validity.

## 3. OPCODE IDENTITIES AND OPERAND WIDTHS — SOURCE-CORRELATED EMISSION ONLY

The following table is deliberately scoped to compiler-output correlation in the archived fixtures. Numeric bytes are directly observable; VM decode/execute semantics are not inferred.

| Byte | Localized source-correlated identity | Directly observed operand shape | Evidence |
|---|---|---|---|
| `0x01` | `PUSH_CONST_CORRELATED` | u32 LE constant index; 4 bytes | minimal/binary/loop/function fixtures |
| `0x02` | `POP_OR_DISCARD_RESULT_CORRELATED` | none; 0 bytes | call-expression statement positions in `DISCIPLINE_LOCK` / loop print |
| `0x10` | `LOAD_CORRELATED` | u32 LE name index; 4 bytes | binary/loop/function fixtures |
| `0x11` | `STORE_CORRELATED` | u32 LE name index; 4 bytes | minimal/binary/loop/function fixtures |
| `0x21` | `BINARY_CORRELATED` | u8 sub-operation; 1 byte | binary/loop fixtures and one-byte fault mutation |
| `0x30` | `CALL_CORRELATED` | u32 LE callee-name index + u16 LE argument count; 6 bytes | `DISCIPLINE_LOCK`, loop print |
| `0x31` | `RETURN_CORRELATED` | none; 0 bytes | explicit `RETURN` functions in `DISCIPLINE_LOCK` |
| `0x40` | `JUMP_BACKEDGE_CORRELATED` | u32 LE target field; 4 bytes | `STEP3_ITER_TEST` WHILE body back-edge |
| `0x41` | `JUMP_IF_FALSE_CORRELATED` | u32 LE target field; 4 bytes | `STEP3_ITER_TEST` condition exit edge |
| `0xFF` | `HALT_OR_TERMINATOR_CORRELATED` | none; 0 bytes | terminal byte in selected main streams |

Directly source-correlated binary sub-operation bytes:

- `0x01` correlates with source `+` in both `BINARY_OPCODE_BASE` and `STEP3_ITER_TEST`.
- `0x12` correlates with source `<` in `STEP3_ITER_TEST`.

A controlled archived pair strengthens only the one-byte sub-operation-width claim: `BINARY_OPCODE_BASE.sigmab` and `BAD_BINARY_SUBOP_FAULT.sigmab` are both 99 bytes and differ at **one byte only**, offset 92, changing `0x01 -> 0xFF`; the preceding byte at offset 91 is `0x21`. Runtime rejection behavior is not captured.

No unobserved opcode value or sub-operation value is introduced by WS12.

## 4. COMPILER SOURCE -> EMITTED BYTECODE LOCALIZATION

### Minimal binding

`MINIMAL_BYTECODE_BASE.sigma` contains `⚡ a: 1;`. Its 53-byte paired archived bytecode source-correlates at main offsets 42/47 with `0x01 + u32(0)` followed by `0x11 + u32(0)`, where constant index 0 is integer `1` and name index 0 is `a`, then terminal `0xFF`.

### Binary expression

`BINARY_OPCODE_BASE.sigma` contains `a:1`, `b:2`, `c:a+b`. Its 99-byte paired bytecode source-correlates with constant loads/stores, name loads `a` and `b`, `0x21 0x01`, store to name `c`, then `0xFF`.

### CALL / RETURN

`DISCIPLINE_LOCK.sigma` contains explicit `DEF`, calls and `RETURN`. Repeated archived bytecode segments source-correlate as:

- `host(op,a,b,c)` call at offset 457: `0x30`, callee-name u32 index 5 (`host`), u16 argc `4`; offset 464 is `0x31` at explicit RETURN termination.
- `host_call(...)` calls at offsets 503 and 545: `0x30`, callee-name index 0, argc `4`; each function terminates with `0x31`.
- main `save(...)` call at offset 587: callee-name index 6, argc `2`.
- main `load(...)` call at offset 600: callee-name index 9, argc `1`, followed by source-correlated store to `VERIFIED`.
- main `print(...)` calls at offsets 617 and 635 with argc `1` and `2` respectively.

**Claim:** exact CALL/RETURN **emission shapes** are localized in this archived pair. Call frames, argument placement, return-address convention, return-value convention, recursion/closure semantics and runtime stack effects remain NOT_PROVEN.

### WHILE / JUMP / JUMP_IF_FALSE

`STEP3_ITER_TEST.sigma` is an existing archived source using:

`WHILE (i < limit) { print("INDEX", i); i: i + 1; }`

Its paired 166-byte bytecode source-correlates with:

- condition reload at instruction ordinals 4/5;
- binary field `0x21 0x12` at ordinal 6 for source `<`;
- `0x41` + u32 value `17` at ordinal 7;
- loop body;
- `0x40` + u32 value `4` at ordinal 16;
- terminal `0xFF` at ordinal 17.

In this fixture, the two jump target fields numerically equal source-correlated instruction ordinals: back-edge `4` and terminal `17`. WS12 does **not** generalize this into a universal absolute-target ABI or runtime IP rule without VM decoder/execute evidence.

## 5. VM DECODE / EXECUTE AND STACK EFFECTS

VM decoder/dispatcher source `sigma_vm.c` is represented only by a recorded SHA-256 identity in the verified archive scope; its bytes were not available to inspect. The requested `./native/sigma-vm.v09_candidate` binary was not accessible in this execution host and is not preserved as a verified archive artifact here.

Therefore:

- exact VM opcode dispatch = **NOT_PROVEN**;
- instruction-pointer increments/transitions = **NOT_PROVEN**;
- stack preconditions/postconditions and stack effects = **NOT_PROVEN**;
- CALL frame layout / argument placement / return address / return value = **NOT_PROVEN**;
- JUMP/JUMP_IF_FALSE runtime target interpretation and condition pop/peek = **NOT_PROVEN**;
- HALT/fall-through result behavior = **NOT_PROVEN**.

Compiler-output byte correlation is not silently upgraded into VM behavior.

## 6. INVALID / MALFORMED BYTECODE

Existing byte-exact malformed fixtures are preserved:

- `bad_magic.sigmab`: 19 bytes, SHA-256 `b449859fe2af41be3e2845a0e85d31900d61d07d2164cae330bb676642946ad4`, exact bytes decode as ASCII `NOT_SIGMA_BYTECODE\n`.
- `truncated.sigmab`: 8 bytes, SHA-256 `f666e4ccff096253426e4111d6746bd62c5b228422fb6617a873ee7af2746501`, exact bytes are `SIGMBC01` only.
- `BAD_BINARY_SUBOP_FAULT.sigmab`: controlled single-byte sub-operation mutation described above.
- Archive manifest also preserves stack-underflow, undefined-function, step-limit, host-error and related structured-error fixtures.

**Localized claim:** the malformed/fault fixture bytes and identities exist.

**Not proven:** exact VM acceptance/rejection, stderr text, stdout, RC, stable error code, abort point, stack-underflow handling, truncated-operand handling, or malformed-header behavior. No archived localized execution transcript binding those outputs to `sigma-vm.v09_candidate` was surfaced.

## 7. EXACT STDOUT / STDERR / RC

Fresh native compiler/VM records: **none**, because the requested live primary root was unavailable. WS12 does not fabricate the mandatory fields.

The only exact process record generated by WS12 is the session-host access check, preserved separately as an access boundary, not a SIGMA compiler/VM test:

- COMMAND: `ls -ld "$HOME/SIGMA/sigma_genesis1"`
- STDOUT: empty
- STDERR: `ls: cannot access '/home/oai/SIGMA/sigma_genesis1': No such file or directory`
- RC: `2`

Aggregate historical labels such as `SIGMA_PSI_256_MATRIX_COMPILE=PASS`, `SIGMA_PSI_256_MATRIX_VM=PASS`, `FAIL_VM_RC_26`, and `FAIL_COMPILER_RC_4` remain aggregate/opaque unless a localized source + command + stdout + stderr + RC record is attached.

## 8. TEST RECORD CONTRACT

Required test columns are preserved exactly in:

`BRAIN/EVIDENCE/SIGMA_PSI/WS12/05_TEST_RECORDS.tsv`

`SOURCE | SOURCE_SHA256 | COMPILER | COMPILER_SHA256 | BYTECODE | BYTECODE_SHA256 | VM | VM_SHA256 | COMMAND | STDOUT | STDERR | RC | CLAIM | EVIDENCE_SCOPE`

There are zero data rows. If a future run has access to the actual primary root, each new test must use the required native form and bind the compiler and VM hashes before promotion:

```bash
./native/sigmac ... \
&& \
./native/sigma-vm.v09_candidate ...
```

## 9. WS06 IMPACT

WS12 does **not** close any of the 65 deduplicated blockers remaining after WS11, because the relevant blocker classes require combinations such as complete ABI identity/header/constants/operands, VM decode/dispatch, stack/frame rules, source-to-bytecode compiler binding, VM congruence, malformed behavior, and/or localized runtime traces. The archive-derived evidence closes only subclaims inside those blocker classes.

However, WS12 provides materially stronger primary evidence than WS06 originally had. WS06 can now be **reopened for additive partial evidence incorporation** with exact boundaries:

- promote observed `SIGMBC01` prefix from NOT_PROVEN to OBSERVED_PREFIX;
- promote the listed numeric instruction/sub-op bytes only as SOURCE_CORRELATED_EMISSION;
- promote the listed operand widths only for the observed emission shapes;
- promote source-correlated CALL/RETURN/JUMP/JUMP_IF_FALSE compiler-output shapes;
- preserve VM decode/execute, stack effects, complete ABI/header semantics and malformed runtime behavior as NOT_PROVEN.

`READY_FOR_WS06_REOPEN=YES` therefore means **ready to incorporate bounded primary-byte evidence**, not ready to merge/close WS06 and not proof of complete executable-language ABI.

## 10. RAW EVIDENCE INDEX

- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/00_SESSION_ACCESS_BOUNDARY.txt` — exact session-host live-root access boundary.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/01_ARCHIVE_SCOPE_AND_TARGET_HASHES.txt` — OPPO primary archive scope, target source hashes, selected manifest hashes and inventory boundary.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/02_SELECTED_ARCHIVED_SOURCES.txt` — selected existing machine sources; no invented grammar.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/03_SELECTED_BYTECODE_BASE64.txt` — exact selected bytecode/fault bytes encoded base64 with SHA-256 and lengths.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/04_LOCALIZED_BYTE_DUMPS_AND_PARSE.txt` — hexdumps, byte offsets, controlled diff and source-correlated emission localization.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS12/05_TEST_RECORDS.tsv` — required schema, zero fabricated rows.

RAW_EVIDENCE_COMMITS=`9b8e09c7d88ffced018e3d55084e55421c1856ba, ffb5cb5889aa4e3f0495eda991be3314a4cb291e, c4d8f455d5d910267c3dbced41ee22f0a55d677f, ff6263f7f04eadc44d8369a621a23f0e0fc7708d, 59e698c8f9dbd45743ed3e2439898e2fa6d081a2, 71e9ba2ad33af0995ffb1ef8da09dbec32005d02`  

ARTIFACTS_FOUND=782
TESTS_RUN=0
LOCALIZED_PASS=0
LOCALIZED_FAIL=0
BLOCKERS_CLOSED=0
BLOCKERS_REMAINING=65
READY_FOR_WS06_REOPEN=YES
