# WS13 — LIVE NATIVE VM EVIDENCE CAPTURE RESULT

WORKSTREAM_ID=WS13  
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom  
BRANCH=SIGMA_LIFE  
SOURCE_HEAD_AT_START=d74d13cab4860fa2021f38a5204c6da1621256c8  
PRIMARY_ROOT_REQUESTED=`~/SIGMA/sigma_genesis1`  
NATIVE_TOOLCHAIN_REQUIRED=`SIGMA source -> ./native/sigmac -> .sigmab -> ./native/sigma-vm.v09_candidate`  
CLAIM_POLICY=`CLAIM <= EVIDENCE`  
WRAPPERS_OR_ALTERNATE_LAUNCHERS_CREATED=NO  
SOURCE_CORPUS_MUTATED=NO  
FRESH_NATIVE_EXECUTION=NO  

## READ ORDER / GOVERNING INPUTS

Read before WS13 execution attempt:

1. `BRAIN/WORKSTREAMS/SIGMA_PSI/SIGMA_PSI_WS01_WS12_PLUS_WS06_REOPEN_MASTER_CHECKPOINT_20260826.md`
2. `BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_REOPEN_EVIDENCE_CLOSURE_RESULT.md`
3. `BRAIN/WORKSTREAMS/SIGMA_PSI/WS12_PRIMARY_MACHINE_EVIDENCE_HARVEST_RESULT.md`

The governing boundary remains:

`SOURCE_CORRELATED_EMISSION != VM_RUNTIME_SEMANTICS`

WS06-REOPEN entered WS13 with `BLOCKERS_CLOSED=0`, `BLOCKERS_REMAINING=65`, VM decode/execute NOT_PROVEN, runtime stack/frame/jump/HALT behavior NOT_PROVEN, malformed-bytecode runtime outcomes NOT_PROVEN, and fresh compiler/VM provenance NOT_PROVEN.

## EXECUTIVE RESULT

The requested live OPPO/Termux primary root is not mounted in this execution host. The current execution host resolves `~/SIGMA/sigma_genesis1` under `$HOME=/home/oai`, not under the archived Android/Termux root `/data/data/com.termux/files/home/SIGMA/sigma_genesis1`.

Exact access check:

- HOST_HOME: `/home/oai`
- HOST_ARCH: `x86_64`
- REQUESTED ROOT RESOLVED HERE: `/home/oai/SIGMA/sigma_genesis1`
- COMMAND: `ls -ld "$HOME/SIGMA/sigma_genesis1"`
- STDOUT: empty
- STDERR: `ls: cannot access '/home/oai/SIGMA/sigma_genesis1': No such file or directory`
- RC: `2`

This is an execution-host access boundary only. It is **not** evidence that the OPPO/Termux primary root, `./native/sigmac`, or `./native/sigma-vm.v09_candidate` are absent on the primary machine.

Because goal 1 requires verifying the actual native binaries and recording SHA-256 of both **before any test**, WS13 did not run a compiler or VM test after the prerequisite failed. No substitute compiler, substitute VM, wrapper, alternate launcher, emulator, archived-bytecode interpreter, or invented grammar was used.

## 1. NATIVE BINARY VERIFICATION

Required binaries:

- `./native/sigmac`
- `./native/sigma-vm.v09_candidate`

State in this WS13 execution attempt:

| Requirement | Result |
|---|---|
| Access primary root | `NO` |
| Verify `./native/sigmac` exists on primary root | `NOT_OBSERVED` |
| SHA-256 `./native/sigmac` | `NOT_CAPTURED` |
| Verify `./native/sigma-vm.v09_candidate` exists on primary root | `NOT_OBSERVED` |
| SHA-256 `./native/sigma-vm.v09_candidate` | `NOT_CAPTURED` |
| Native binaries verified | `NO` |

`NOT_OBSERVED` here means inaccessible in this execution host, not absent on the primary machine.

## 2. EXISTING MACHINE-PASS SOURCE PRIORITY

The existing archived evidence already identifies the requested machine-PASS source priorities and exact historical source/bytecode identities:

| Fixture | Historical source SHA-256 | Historical paired bytecode SHA-256 | WS13 action |
|---|---|---|---|
| `MINIMAL_BYTECODE_BASE.sigma` | `294a888511b15a14f64e98410a786eeee26ec0934a6f30de04758a270f013dc6` | `26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875` | DEFERRED — primary root inaccessible |
| `BINARY_OPCODE_BASE.sigma` | `51e69c08bace633fb42ed48257b15a891fb94e58283989f2f04e8b1f79ecb2a2` | `23a483ddea89cf36a36618cc7d192d1a3efd51927ed3272a77574be23d14a13c` | DEFERRED — primary root inaccessible |
| `DISCIPLINE_LOCK.sigma` | `cf82ef98514198df84a97e1bc3f7bd374db44ef3262bba934a74caffa5c0c94f` | `e3d4f6169fbb83d0df8977f8029f53a2181531582954898e469e0e0e6ac1a4a0` | DEFERRED — primary root inaccessible |
| `STEP3_ITER_TEST.sigma` | `b761ec81bf8ce7f6e2aec7aa6637cd822fbbf520eef99d84c1216a3ed131368e` | `e15e17e7fa3aace360bddd0062880c3e10ac3e869ef256f05f073aa2f6381e4a` | DEFERRED — primary root inaccessible |

These hashes are inherited archived identities from WS12/WS06-REOPEN. They are **not** presented as fresh WS13 compiler outputs.

No new SIGMA grammar was invented and no source fixture was modified.

## 3. COMPILER + VM TEST RECORDS

Required per-test schema is preserved in:

`BRAIN/EVIDENCE/SIGMA_PSI/WS13/01_TEST_RECORDS.tsv`

Columns:

`SOURCE | SOURCE_SHA256 | COMPILER | COMPILER_SHA256 | BYTECODE | BYTECODE_SHA256 | VM | VM_SHA256 | COMMAND | STDOUT | STDERR | RC | CLAIM | EVIDENCE_SCOPE`

Data rows: `0`.

No row was fabricated because neither native executable identity could be captured first.

Required native footer form therefore was not executed:

```bash
./native/sigmac ... \
&& \
./native/sigma-vm.v09_candidate ...
```

## 4. TARGETED WS06 RUNTIME GAPS

No runtime gap is promoted by this attempt.

| Target | WS13 state |
|---|---|
| compiler accepts source | `NOT_TESTED` |
| VM accepts freshly emitted `.sigmab` | `NOT_TESTED` |
| `0x01` runtime correlation | `NOT_TESTED` |
| `0x10` runtime correlation | `NOT_TESTED` |
| `0x11` runtime correlation | `NOT_TESTED` |
| `0x21` runtime correlation | `NOT_TESTED` |
| `0x30` runtime correlation | `NOT_TESTED` |
| `0x31` runtime correlation | `NOT_TESTED` |
| `0x40` runtime correlation | `NOT_TESTED` |
| `0x41` runtime correlation | `NOT_TESTED` |
| `0xFF` terminal/HALT runtime behavior | `NOT_TESTED` |
| CALL/RETURN behavior | `NOT_TESTED` |
| WHILE/JUMP/JUMP_IF_FALSE behavior | `NOT_TESTED` |
| BINARY `+` runtime behavior | `NOT_TESTED` |
| BINARY `<` runtime behavior | `NOT_TESTED` |
| VM result propagation | `NOT_TESTED` |

The prior `*_CORRELATED` labels remain compiler-emission correlations only.

## 5. ERROR EVIDENCE

Existing archived malformed/fault inputs remain available as historical artifacts, including:

- `bad_magic.sigmab` — SHA-256 `b449859fe2af41be3e2845a0e85d31900d61d07d2164cae330bb676642946ad4`
- `truncated.sigmab` — SHA-256 `f666e4ccff096253426e4111d6746bd62c5b228422fb6617a873ee7af2746501`
- `BAD_BINARY_SUBOP_FAULT.sigmab` — SHA-256 `629ddc92b5cc1e0920bdc1f8fbc2d361d01d57f26245788f243d924e8e64f8d5`
- archived stack-underflow / undefined-function / step-limit fixture families

WS13 did not execute them because the required native VM identity could not be verified first.

Therefore exact native VM stdout, stderr and RC for these error cases remain NOT_CAPTURED in WS13. No process RC is converted into a stable error ABI name.

## 6. CRITICAL BOUNDARIES PRESERVED

- `SOURCE_CORRELATED_EMISSION != VM_RUNTIME_SEMANTICS`
- `RC != ERROR_ABI`
- `PASS != UNIVERSAL_SUPPORT`
- `FAIL != UNSUPPORTED`
- `CLAIM <= EVIDENCE`
- access failure on this host `!=` primary-machine absence
- archived byte identity `!=` fresh compiler/VM provenance

## 7. BLOCKER IMPACT

No WS10 blocker can be closed from an access-boundary record.

`BLOCKERS_CLOSED=0`

`BLOCKERS_REMAINING=65`

The same runtime/provenance blocker classes identified by WS06-REOPEN remain open: VM decode/dispatch, stack effects, CALL frame/return behavior, jump/IP/condition behavior, HALT/result behavior, malformed-bytecode native outcomes, compiler/VM identity linkage, and end-to-end source→compiler→bytecode→VM provenance.

## 8. RAW EVIDENCE INDEX

- `BRAIN/EVIDENCE/SIGMA_PSI/WS13/00_SESSION_ACCESS_BOUNDARY.txt` — exact host/root access check, stdout/stderr/RC and explicit non-absence boundary. Commit `9d9e7112a4ee2baf75bc2f8527b3838e5b3f7f76`.
- `BRAIN/EVIDENCE/SIGMA_PSI/WS13/01_TEST_RECORDS.tsv` — required per-test record schema with zero data rows. Commit `e148e79bfc22b76f9c3d5919f668c328b0f313fd`.

No existing evidence was deleted or overwritten.

## 9. REQUIRED NEXT EVIDENCE CONDITION

WS13 runtime capture can proceed only in an execution context that actually exposes the locked primary root `~/SIGMA/sigma_genesis1` with the two existing native binaries. The first admissible operations there are:

1. verify `./native/sigmac` and `./native/sigma-vm.v09_candidate` exist;
2. capture SHA-256 of both before tests;
3. reuse the existing PASS fixtures first;
4. execute only the native source→compiler→`.sigmab`→VM chain;
5. capture exact stdout/stderr/RC per test without promoting RC to an error ABI.

NATIVE_BINARIES_VERIFIED=NO
TESTS_RUN=0
COMPILE_PASS=0
VM_PASS=0
VM_FAIL=0
LOCALIZED_RUNTIME_CLAIMS=0
ERROR_CASES_CAPTURED=0
BLOCKERS_CLOSED=0
BLOCKERS_REMAINING=65
READY_FOR_WS06_FINAL_CLOSURE=NO
READY_FOR_V1_2_CANDIDATE=NO
