# C08 Director Acceptance

`B1.1-C08 — Toán rời rạc và tổ hợp`

Worker candidate: `4f0493b4c7605e9d457810c9efe7ae822eeeab7a`  
Director-accepted head: `b4202c7eaa0cea462d882cf32cae635c90005c5c`

Independent Director audit:

- 8/8 canonical topics;
- 109/109 claims read;
- 7/7 source identities and deterministic SOURCE_ID hashes verified;
- 32/32 D1–D4 Learning Objectives read;
- 32/32 semantic Claim→Learning-Objective closures verified;
- future/locked support Claim IDs = 0;
- R05 PASS;
- R02 PASS;
- accepted C03 reuse PASS;
- prerequisite/sequence DAG PASS / acyclic;
- stage boundary PASS.

Before acceptance, Director repaired two hypothesis omissions in `CLAIMS_DIRECTOR_AMENDMENT_1.jsonl`:

1. `HKA-B1-1-C08-N004-C006` — Euler open trail now explicitly requires all non-isolated vertices to lie in one connected component, in addition to exactly two odd-degree vertices.
2. `HKA-B1-1-C08-N007-C014` — standard Reed–Solomon statement now explicitly requires `1≤k≤n≤q` before asserting dimension `k` and distance `n-k+1`.

No stable IDs, Learning Objectives or closure topology changed.

Decision: `DIRECTOR_ACCEPTED_PASS_AFTER_TWO_HYPOTHESIS_REPAIRS`.
