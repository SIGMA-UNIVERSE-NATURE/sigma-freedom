# WINDOW J4-R1 — CURRENT OPPO TARGETED RUNTIME REOPEN — 2026-08-31

REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
ROLE=WINDOW_J4_R1_CURRENT_OPPO_TARGETED_RUNTIME
STATUS=OPEN
PARENT_WINDOW=WINDOW_J4_SEMANTIC_RUNTIME_CLOSURE_RESULT_20260828.md
AUTHORITATIVE_CHECKPOINT=SIGMA_ACTIVE_MINIMAL_CHECKPOINT_AFTER_WINDOW_J4_20260828.md

## Purpose

Reopen J4 only to close current-runtime semantic fields that remained blocked because the prior J4 host did not have the native OPPO compiler/VM binaries.

This is not a restart of J4 and not authorization to rerun already-closed capabilities.

## Required current toolchain identities

COMPILER_PATH=./native/sigmac
EXPECTED_COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71

VM_PATH=./native/sigma-vm.v09_candidate
EXPECTED_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

Before any runtime probe:

CURRENT_COMPILER_SHA256=
CURRENT_VM_SHA256=
CURRENT_TOOLCHAIN_IDENTITY_MATCH=YES/NO

If either identity differs, stop current-version semantic closure and record the version-scope change. Do not reinterpret a mismatch as a semantic failure.

## Do-not-rerun lock

DO_NOT_RERUN_CAPABILITIES_PRESERVED=21
DUPLICATE_CAPABILITY_TESTS_TARGET=0

Do not rerun:

- the original 21 locked capability families;
- J2 already-closed precedence relations `* > +`, `** > *`, `+ > <`;
- J2 already-closed associativity cases `-` left, `/` left, `**` right;
- J3 already-reviewed VM internals merely to reproduce existence;
- V10 Hard Mode;
- V11.5 sequence behavioral synthesis;
- V13 bounded mathematical relation synthesis;
- V19+ abstract-ascent research merely to promote general language semantics.

## J4-R1 open fields only

1. TRUE literal current runtime
2. FALSE literal current runtime
3. internal BOOL runtime type if directly observable
4. NULL versus lowercase `null` semantic identity
5. accepted logical-operator surface
6. AND runtime if an accepted grounded surface exists
7. OR runtime if an accepted grounded surface exists
8. evaluation order
9. short-circuit behavior if an accepted grounded logical surface exists
10. coercion mechanisms
11. line-leading `//` comment boundary
12. current FLOORDIV runtime role
13. unary-minus versus exponentiation precedence

FLOORDIV_COMMENT_CONFLICT_RESOLVED=NO
CONFLICT_PRESERVED=YES

## Safety invariants

CLAIM<=EVIDENCE
UNKNOWN!=FALSE
NOT_PROVEN!=UNSUPPORTED
SIGMA_SOURCE_IMPLEMENTATION_INSPECTED=NO
SIGMA_SOURCE_IMPLEMENTATION_MODIFIED=NO
CURRENT_COMPILER_MODIFIED=NO
CURRENT_VM_MODIFIED=NO
REBUILD_USED=NO
HOST_VM_EMULATION_USED=NO
SYNTHETIC_BYTECODE_CREATED=NO
PRE_VM_EXPECTED_ANSWER_ACCESS=NO
GPT_EXPECTED_MEANING_INJECTED=NO
NO_SILENT_CONFLICT_OVERWRITE

## Execution contract

Every authorized probe must use a unique bytecode artifact and the native chain only:

```bash
RUN_ID="$(date +%Y%m%d_%H%M%S)_$$"
BC_RUN=".sigma_exec/test_${RUN_ID}.sigmab"

./native/sigmac "$SRC" "$BC_RUN" \
&& \
./native/sigma-vm.v09_candidate "$BC_RUN"
```

No alternate footer may create SIGMA machine claims.

## Anti-answer-leakage contract

Required pipeline:

TEST_INPUT
→ SIGMA
→ SIGMA_OUTPUT
→ POST_VM_EXTERNAL_EVALUATOR

Forbidden before VM:

EXPECTED_ANSWER_ACCESS
HOST_DERIVATION
ANSWER_IN_SOURCE
ANSWER_IN_ARGV
ANSWER_IN_ENV
ANSWER_IN_STDIN
HOST_SEMANTICS_SUBSTITUTION

## Evidence contract

For each new probe record:

TEST_ID=
FIELD=
WHY_EXISTING_EVIDENCE_IS_INSUFFICIENT=
SOURCE_PATH=
SOURCE_SHA256=
BYTECODE_PATH=
BYTECODE_SHA256=
COMPILER_SHA256=
VM_SHA256=
COMPILE_RC=
VM_RC=
RAW_STDOUT=
RAW_STDERR=
OBSERVATION=
STATUS=
EXACT_SCOPE=
NOT_PROVEN_BEYOND=
DUPLICATE_CAPABILITY_TEST=NO

Failure is valid evidence. Do not rewrite a failed fixture merely to force PASS and discard the failure.

## Close condition

J4-R1 may close evidence-bounded even if some fields remain NOT_PROVEN.

J4-R1 must not authorize J5 until:

- current toolchain identity is established on OPPO;
- all 13 open fields are reviewed using prior evidence first;
- only genuinely necessary probes are executed;
- raw evidence is preserved;
- conflicts remain explicit;
- no duplicate capability reruns occur.

WINDOW_J4_R1_OPEN=YES
WINDOW_J4_R1_COMPLETE=NO
WINDOW_J5_AUTHORIZED=NO
READY_FOR_PUBLIC_LANGUAGE_SPEC=NO
