# SIGMA R58 / R20 — Post-Admission ABI Audit

Date: 2026-09-29
Source: user-supplied Termux ABI inspection.

## Finalizer ABI

File:
AUTOLEARN_STORAGE_HOOK_R1/finalize_compaction.sh

Observed contract:

- requires exactly one experiment path;
- requires STATE_COMPACTION_RECEIPT.env;
- requires schema SIGMA_SANDBOX_STATE_COMPACTION_V1;
- requires RESULT=PASS;
- requires COMPACTION_MODE=CANONICAL_DUPLICATES_REMOVED_UNIQUE_DELTA_ARCHIVED;
- requires PROOFS_PRESERVED=YES;
- requires RECEIPTS_PRESERVED=YES;
- requires SOURCE_PRESERVED=YES;
- requires UNIQUE_STATE_DATA_PRESERVED=YES;
- validates unique-delta archive path stays inside experiment root;
- validates unique-delta SHA256;
- requires experiment out directory;
- resolves model from learning receipt;
- reads HEAD/MODEL/GENERATION from storage current.env;
- requires receipt CANONICAL_HEAD == current.env HEAD;
- requires learning-receipt model == current.env MODEL;
- serializes storage writer access with writer.lock;
- idempotently returns STORAGE_ACK=ALREADY_PRESENT if receipt SHA is already in ledger;
- invokes storage_hook.sigmab;
- accepts STORE or SKIP_DUPLICATE;
- rejects SKIP_BYTE_BUDGET as pending;
- independently verifies stored bundle and byte-exact restore;
- appends a fsynced ledger line;
- atomically replaces current.env via temporary file + mv;
- REAL_DATA_DELETE=NO.

Important current-context gate:

[ "$HEAD" = "$CUR_HEAD" ] || pending HEAD_CONTEXT_NOT_CURRENT
[ "$MODEL" = "$CUR_MODEL" ] || pending MODEL_CONTEXT_NOT_CURRENT

## Post-consolidation entry ABI

File:
AUTOLEARN_STORAGE_HOOK_R1/run_after_consolidation.sh

Observed contract:

- arguments: SOURCE_DIR HEAD MODEL GENERATION;
- acquires writer.lock;
- invokes current VKM runtime with storage_hook.sigmab;
- passes HEAD, MODEL, GENERATION explicitly;
- no independent verifier or ledger/current.env update is shown in this entry script itself.

## Reconciler ABI

File:
AUTOLEARN_STORAGE_HOOK_R1/reconcile.sh

Observed behavior:

- locks autolearn.pending;
- rebuilds pending list deterministically;
- for each discovered STATE_COMPACTION_RECEIPT.env:
  - computes receipt SHA;
  - skips receipts already present in ledger;
  - otherwise invokes finalize_compaction.sh;
  - records nonzero finalizer results as pending;
- reports all discovered receipts accounted for;
- REAL_DATA_DELETE=NO.

Observed discovery expression:

find "$ADMIN" -mindepth 2 -maxdepth 2   -type f -name 'STATE_COMPACTION_RECEIPT.env'

This searches only receipts located at the specified shallow depth under SIGMA_AUTOLEARN_ADMIN.

## GC gate V2 ABI

File:
AUTOLEARN_STORAGE_HOOK_R1/gc_gate_v2.sh

Observed fail-closed contract:

- requires compaction receipt, pack, commit, ledger, lock;
- requires compaction RESULT=PASS;
- requires preservation flags;
- requires matching receipt entry in ledger;
- accepts only STORE or SKIP_DUPLICATE decisions;
- verifies experiment path binding;
- validates unique archive SHA;
- independently verifies bundle and byte-exact restore;
- on success emits:
  STORAGE_ACK=PASS
  STORAGE_DURABILITY_GATE=PASS
  GC_REHEARSAL_ELIGIBLE=YES
  REAL_GC_ENABLED=NO

On failure:
  STORAGE_DURABILITY_GATE=FAIL
  GC_REHEARSAL_ELIGIBLE=NO
  REAL_GC_ENABLED=NO

## Probe status

R58_R20_POST_ADMISSION_ABI=COMPLETE

## Current canonical context from prior admitted evidence

Current canonical head:
142a5fcc295a02610e7134312acfee63

Current canonical model:
4a9f5ef84131c4162633fed959d4fb4d

Current admitted state generation:
13653

Current storage current.env from the immediately preceding probe still reported:
HEAD=507aae721fbd50ec13b8bfd653caf3e9
MODEL=4e28b7b00428271a4d09f1791d5d46fb
GENERATION=3

## Technical findings / boundary

### 1. Finalizer is correctly fail-closed against stale storage context

With the storage current.env shown in the preceding probe, a compaction receipt for the newly admitted head/model would not pass finalization because the finalizer explicitly requires the receipt HEAD/MODEL context to equal current.env.

Therefore a direct post-admission finalize attempt for the new canonical state is expected to remain PENDING until the storage context is reconciled through an authorized post-admission path.

This is a fail-closed property, not evidence that the canonical R58 FIX3 promotion failed.

### 2. Reconciler discovery depth is a potential coverage gap

The reconciler searches for STATE_COMPACTION_RECEIPT.env only with:

-mindepth 2 -maxdepth 2

The supplied FIX3 workspace and admission artifacts are nested substantially deeper than two levels under SIGMA_AUTOLEARN_ADMIN.

No evidence in this ABI inspection proves that a future FIX3 post-admission compaction receipt placed in the deep FIX3 workspace would be discovered by reconcile.sh as currently written.

Therefore:

R58_FIX3_DEEP_RECEIPT_AUTODISCOVERY=NOT_PROVEN

This should be treated as a controller/storage integration gap until either:
- the post-admission receipt is intentionally published at the reconciler's discoverable depth, or
- the reconciler discovery rule is safely generalized and independently regression-tested.

### 3. run_after_consolidation.sh is not equivalent to finalization

The post-consolidation entry invokes storage_hook.sigmab directly under the writer lock, but the shown script does not perform the finalizer's independent verification, ledger append, current.env atomic update, or receipt-driven acknowledgement.

Therefore:

DIRECT_STORAGE_HOOK_CALL=NOT_EQUIVALENT_TO_RECEIPT_FINALIZATION

### 4. GC remains fail-closed

gc_gate_v2.sh requires a ledger-backed, independently verified durable receipt before declaring GC_REHEARSAL_ELIGIBLE=YES.

REAL_GC_ENABLED remains NO.

No destructive cleanup is authorized by this ABI audit.

## Next required closure

A correct post-admission consolidation/reconciliation path must, without mutating the admitted model semantics:

1. produce or bind a valid compaction receipt for the newly admitted canonical head/model;
2. ensure that receipt is discoverable by the reconciliation mechanism;
3. advance storage metadata from the prior canonical context to the admitted context through a receipt-driven, independently verified path;
4. preserve ledger idempotence;
5. verify byte-exact restore;
6. keep REAL_GC_ENABLED=NO and REAL_DATA_DELETE=NO;
7. only then claim R20_POST_ADMISSION_CONSOLIDATION=PASS.
