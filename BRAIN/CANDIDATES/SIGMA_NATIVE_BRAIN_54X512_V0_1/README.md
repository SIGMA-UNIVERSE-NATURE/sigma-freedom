# SIGMA Native Brain 54×512 v0.1 — Revision R1

**ISOLATED CANDIDATE — DO NOT MERGE OR PROMOTE**

Base canonical state remains `SIGMA_LIFE@7d1648f7d65edfbd1a2668ad10ad4cd10dd9482d`.

## Why R1 exists

The parent candidate compiled deterministically with both verified HP V6 and V7 `sigmac` builds, but both matching `sigma-hostvm` executions stopped with:

```text
SIGMA C VM: undefined function MNEW
```

Exact stderr SHA-256:

`89429a9789083d6d05bb5717a9217e4a9da7fa364918887af96f026a5d46b484`

R1 does not guess a replacement map primitive. It removes the unverified list/map host dependency entirely.

## Minimal revision

- `CORE_NAME(core_id)` now uses scalar SIGMA control flow.
- Accuracy case 001 now exposes scalar result functions.
- Locked stdout remains byte-for-byte unchanged.
- Static validation rejects `LNEW`, `LPUSH`, `LGET`, `MNEW`, `MSET`, and `MGET`.
- Expected assembled source SHA-256: `cf1241de4f0911f8ae7da5fdfd673bfd34b23d52b10ab377c0e36c9791795c77`.
- Expected stdout SHA-256: `20eee2e7cb2744bd7ab4027255b2896b2f6e37b5a389eb00dddde67e62c1b35a`.

## Scope

R1 still:

- registers all 54 core names in executable dispatch;
- routes skill IDs `1..512` through the 31 canonical sections;
- implements only the same accuracy/truth/provenance vertical slice;
- does not claim full implementation of 54 cores or 512 skills;
- does not claim intelligence improvement.

## Required next evidence

1. Assemble and static-validate R1.
2. Compile twice on HP V6 and twice on HP V7.
3. Require deterministic and cross-toolchain-equal bytecode.
4. Run both matching hostVMs.
5. Require rc 0, empty stderr and exact UTF-8 stdout.
6. Preserve Foundation/ABI, OPPO, independent-evaluator and promotion gates.

Current decision:

`HOLD_PENDING_R1_SIGMAC_AND_SIGMA_HOSTVM_MACHINE_EXECUTION`
