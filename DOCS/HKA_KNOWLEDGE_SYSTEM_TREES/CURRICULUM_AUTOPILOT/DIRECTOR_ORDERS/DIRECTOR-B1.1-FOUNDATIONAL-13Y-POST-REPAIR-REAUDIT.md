# DIRECTOR EXECUTION ORDER — B1.1 FOUNDATIONAL 13-YEAR POST-REPAIR RE-AUDIT

Status: `ISSUED_ACTIVE`
Stage: `CURRICULUM`
Active scope: `B1.1-FOUNDATIONAL-13Y-AUDIT`
Execution branch: `hka-tree/curriculum-master`
Academic repair input anchor: `fcb2d72dc2a0d75ee72ce3dd8ddccefae4c72b32`
B1.2: `LOCKED`

## Purpose

Re-audit the full B1.1 foundational 13-year general-education coverage after the targeted foundational repairs already applied at the true-owner scopes C02, C03, C04 and C07. This is a full coverage re-audit, not a mechanical closure check of the previous eight gaps.

Do not open B1.2. Do not create Lesson Registry, prompts, images, R2, delivery or website artifacts. Do not change stage.

## Canonical inputs

1. Canonical Knowledge Tree commit `fc799bf1104ab6352710e1801777a971b5179995`.
2. B1 architecture commit `265bb584b5d7e36e11091289d58558408880118c`.
3. Immutable B1 scope-map blob `bedef47958a728e3f0d56d412f7bdea3ec465856`.
4. Accepted B1.1 C01-C10 plus current Director foundational overlays/repairs through input anchor `fcb2d72dc2a0d75ee72ce3dd8ddccefae4c72b32`.
5. `FOUNDATIONAL_AUDITS/B1_1_13_YEAR/AUDIT_PROTOCOL.md`.
6. `FOUNDATIONAL_AUDITS/B1_1_13_YEAR/EXTERNAL_BENCHMARK_MATRIX.json`.
7. Pre-repair `FOUNDATIONAL_GAP_REGISTER.json`, which records F13-G01 through F13-G08.
8. Repair artifacts under `FOUNDATIONAL_AUDITS/B1_1_13_YEAR/REPAIRS/B1.1-C02`, `B1.1-C03`, `B1.1-C04`, and `B1.1-C07`.

## Required work

### R1 — Re-read effective curriculum, not summaries

Inspect the exact committed accepted C01-C10 records and every currently active foundational repair overlay. Do not infer closure from repair filenames, prior chat, or advanced theorems.

### R2 — Re-map the complete benchmark framework

Re-run the benchmark across the six-system / six-continent general-education set already adopted by the audit protocol, spanning early/primary through lower-secondary and upper-secondary/general education.

For every high-confidence foundational mathematical understanding, classify the effective HKA coverage as exactly one of:

- `COVERED`
- `PARTIALLY_COVERED`
- `MISSING`
- `OUT_OF_B1_1_SCOPE`

The re-audit must cover the complete benchmark matrix; it must not examine only F13-G01 through F13-G08.

### R3 — Re-evaluate all prior gaps independently

Re-test F13-G01 through F13-G08 against the post-repair committed content. A prior gap may be closed only when the foundational meaning is explicit, developmentally usable, correctly owned, sourced/mapped as required, and not merely implied by an advanced formal statement.

### R4 — Search for newly exposed gaps

A previous repair does not cap the gap register at eight. Identify any additional `PARTIALLY_COVERED` or `MISSING` foundational understanding revealed by the full re-audit.

For every remaining/new partial or missing item, record:

- concept;
- expected developmental role;
- external curriculum evidence;
- true owner C;
- proposed minimal repair;
- duplicate-risk check.

### R5 — Ownership, dependency and duplicate gates

Verify that every foundational repair sits at its true canonical owner, respects the immutable B1 scope map, introduces no semantic duplicate, preserves prerequisite/dependency order, and does not import B1.2 or B1.5 material into B1.1.

### R6 — Persist the re-audit result

Update the machine-readable foundational audit artifacts so durable state records the post-repair classification and current `FOUNDATIONAL_GAP_COUNT`.

If any `PARTIALLY_COVERED` or `MISSING` item remains, the audit stays `ACTIVE_NOT_YET_PASS`; issue only the minimum targeted repair at the true owner scope.

If and only if every required foundational item is covered and `FOUNDATIONAL_GAP_COUNT = 0`, record a foundational PASS candidate for Director integration review. Do not unlock B1.2 from this re-audit alone.

## Mandatory gates

The re-audit result is not eligible for final B1.1 completion unless all are true:

1. full multi-continent general-education benchmark re-audit = PASS;
2. all prior gaps F13-G01..F13-G08 independently resolved or correctly retained;
3. newly exposed foundational gap scan complete;
4. `FOUNDATIONAL_GAP_COUNT = 0` for PASS candidacy;
5. true-owner check = PASS;
6. semantic duplicate scan = PASS;
7. prerequisite/dependency audit = PASS;
8. scope-map boundary audit = PASS;
9. stage boundary = PASS;
10. Backup Sentinel `TREE_ALIGNMENT_PASS` is still required before any successor decision;
11. Director integration audit PASS is still required before any B1.2 unlock decision.

## Required terminal outcomes

Allowed outcomes for this checkpoint:

- `FOUNDATIONAL_REAUDIT_PASS_CANDIDATE_GAP_0`
- `FOUNDATIONAL_REAUDIT_REPAIR_REQUIRED`
- `BLOCKED_INPUT`
- `BLOCKED_CONTRADICTION`

`FOUNDATIONAL_REAUDIT_PASS_CANDIDATE_GAP_0` is not authorization to open B1.2.

Until Director independently completes integration review and confirms Sentinel alignment, B1.2 remains `LOCKED_PENDING_B1_1_FOUNDATIONAL_PASS`.
