# DIRECTOR SENTINEL AUTHORIZATION — DIRECTOR-BACKUP-S01 — B1.2 EXIT

Decision: `AUTHORIZED_TO_AUDIT`
Role: `BACKUP_SENTINEL` — delegated alignment audit only; not a Director and cannot ACCEPT or unlock.
Stage: `CURRICULUM`
Execution branch: `hka-tree/director-backup-sentinel`
Control-plane branch to read: `hka-tree/curriculum-master`

Accepted B1.2 family integration: `425df302d7331293ad12744a6096e05d51560890`.
Accepted external general-education mapping: `5492127b661b770c23026c6205d1fbd4e8464835`.
Effective mapping metadata repair: `c6c8fda3bf6a0d898e7a9f7c39ec20d6b1b3d5e2`.
Mapping checkpoint: `9c818c487942360ac7a41c433865d3e4d9292d5a`.

Fresh Sentinel must resolve and record the exact current `hka-tree/curriculum-master` HEAD at audit time, then verify:
- canonical tree `fc799bf1104ab6352710e1801777a971b5179995` and immutable B1 scope-map blob `bedef47958a728e3f0d56d412f7bdea3ec465856` unchanged;
- HKA_CURRICULUM_STATE, WINDOW_REGISTRY, continuity snapshot, foundational gate, Director status/checkpoint and accepted B1.2 artifacts agree;
- B1.2-C01..C12 accepted chain is coherent, including reconciled C02 mass-vs-weight repair;
- family integration is Director-accepted PASS and external mapping is Director-accepted PASS;
- mapping evidence: 6 systems, 6 continents, official source resolution 6/6, university-only baseline false, foundational requirements 10 with FULL=9/PARTIAL=0/GAP=0/NOT_OWNER=1, foundational gap count 0;
- duplicate/ownership, prerequisite graph, support resolution and mass-vs-weight remain PASS;
- `FUTURE_LOCKED_SUPPORT=0`, cross-scope academic mutation 0, CURRICULUM-only stage boundary;
- B1.3 remains locked while Sentinel runs;
- no post-CURRICULUM artifacts are authorized.

Sentinel authority is read-only for academic/control-plane content. It may write only its own `STATUS.json`, `REPORT.md` and append-only checkpoint on `hka-tree/director-backup-sentinel`.

Return only `TREE_ALIGNMENT_PASS` with zero alerts, or a true `BLOCK` naming the exact mismatch. Do not mutate `hka-tree/curriculum-master`; do not declare Director acceptance; do not unlock B1.3.
