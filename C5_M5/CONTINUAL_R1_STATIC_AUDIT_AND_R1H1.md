# Continual Compact Work Memory — R1 Static Audit and R1H1 Evaluator

Date: 2026-09-09

## Finding

The R1 cognition core itself is append-only for archived work memory: `ARCHIVE_SELF_CONTAINED_WORK_MEMORY` appends the detached compact memory to `native_compact_work_memory_bank.txt`; archived recall/query read the selected work block and do not write it back.

However, the R1 evaluator's `WORK_A_MEMORY_BYTE_STABLE_AFTER_WORK_B` gate compared a hash of the recalled Work A output before/after Work B. That proves semantic recall stability, but is weaker than byte-for-byte immutability of the exact Work A archive block. Hidden metadata/edge changes could in principle evade the old oracle if recall reconstructed the same output.

This is an evaluator-strength issue, not an established cognition-core defect.

## R1H1 correction

R1H1 keeps the cognition core byte-identical and strengthens both admission and independent blind evaluators:

1. archive Work A;
2. extract the exact `WORK_MEMORY_BEGIN ... WORK_MEMORY_END` block whose `WORK_ID` equals Work A;
3. snapshot/hash that exact archive block before Work B;
4. learn/compact/archive Work B;
5. extract Work A's exact bank block again;
6. require SHA256 equality **and** `cmp -s` byte equality;
7. retain the prior recall-output equality gate as an additional regression.

No cognition criterion was weakened.

## Frozen R1H1 artifacts

- target cognition core SHA256: `69ec3e26ef857976c257724fa5691210bf2fe1ad3695e085dcd2a2bc9fa0db47`
- R1H1 admission evaluator SHA256: `a64502677eb2b61965e0622330b75b778fea9173ba3688ce0b99bed0b3affe83`
- R1H1 independent blind evaluator SHA256: `c17c40d8204b9fdf8db85479c0c9a747696270d2127e231840d972d9edaa0b9b`
- R1H1 ladder runner SHA256: `ddf5e3100fece65392b46e56557fe8567c60b84c1c67e47756fb483a6d559b62`
- R1H1 ladder bundle SHA256: `30eb8ac1f53860576e938fcaa0ea118ed5d8163f813d64b3cc58bc0338b899ca`

Static validation: target cores byte-identical; top manifest PASS; Bash syntax PASS; ZIP integrity PASS.

## Routing

This remains **Gate A / M5 TEST** work under `TWO_GATE_ARCHITECTURE.md`.

Run R1H1 instead of the weaker R1 evaluator. Only after R1H1 admission + independent blind PASS may `CONTINUAL_LEARNING_FROM_COMPRESSED_LOCAL_MEMORY` advance in the exact two-work/self-contained-compact scope.

The next Gate A cognition dependency after PASS is native revision/support/conflict plus independent blind tests.

Production binding remains NO.
