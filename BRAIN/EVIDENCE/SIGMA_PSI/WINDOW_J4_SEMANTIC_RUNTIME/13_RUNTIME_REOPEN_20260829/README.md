# J4 Runtime Reopen — Phase 1 Raw Capture

This additive pack executes only the unconditional, non-duplicate J4 semantic-runtime fixtures.

It does not inspect implementation source, modify or rebuild the compiler/VM, emulate SIGMA, synthesize bytecode, evaluate expected answers, or classify semantic outputs.

## Preconditions

Run from:

```text
~/SIGMA/sigma_genesis1
```

The runner independently rehashes:

```text
./native/sigmac
./native/sigma-vm.v09_candidate
```

It exits before every runtime test if either identity differs from the J4 contract.

## Execute

```bash
bash BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_J4_SEMANTIC_RUNTIME/13_RUNTIME_REOPEN_20260829/run_phase1_capture.sh
```

Phase 1 performs 17 native compiler→VM executions:

- four BOOL literal cases;
- two matched `NULL`/`null` cases;
- two grounded symbolic logical-surface cases;
- four evaluation-order cases;
- one reverse mixed-numeric case;
- one line-leading `//` case;
- three matched unary-minus/exponentiation precedence forms.

Each execution runs in a fresh Bash process so the required `RUN_ID="$(date +%Y%m%d_%H%M%S)_$$"` yields a distinct bytecode path.

The exact native chain is:

```bash
./native/sigmac "$SRC" "$BC_RUN" \
&& \
./native/sigma-vm.v09_candidate "$BC_RUN"
```

Only redirections are added to preserve compiler and VM stdout/stderr separately.

## Deliberately deferred

Short-circuit tests are not run in Phase 1. They become authorized only after external evaluation establishes that `&&` or `||` is accepted and reaches the VM under this exact toolchain.

Associativity and invalid-operand capability families are not rerun.

## Output

Raw evidence is written additively under:

```text
BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_J4_SEMANTIC_RUNTIME/13_RUNTIME_REOPEN_20260829/
```

Every raw record is conservatively marked `STATUS=NOT_PROVEN` until a separate post-capture evaluator reads the preserved VM output and assigns an evidence-bounded J4 status.
