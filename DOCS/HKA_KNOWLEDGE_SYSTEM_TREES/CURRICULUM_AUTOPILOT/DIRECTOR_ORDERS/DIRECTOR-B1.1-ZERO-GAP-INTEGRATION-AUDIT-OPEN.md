# DIRECTOR ORDER — OPEN B1.1 ZERO-GAP INTEGRATION AUDIT

Status: `ISSUED_ACTIVE`
Stage: `CURRICULUM`
Window: `DIRECTOR-B1.1-INTEGRATION-AUDIT`
Scope: `B1.1-INTEGRATION-AUDIT`
Execution branch: `hka-tree/curriculum-master`
Activation base commit: `a47e5b6b09949084b31bf4c832bac33562e75c7d`

## Purpose

Perform the Director integration audit over the complete effective B1.1 curriculum after the Foundational 13-Year post-repair re-audit reached `FOUNDATIONAL_GAP_COUNT = 0`.

This window does **not** open B1.2 and does **not** authorize any stage after `CURRICULUM`.

## Locked inputs

- Canonical Knowledge Tree: `fc799bf1104ab6352710e1801777a971b5179995`
- B1 architecture: `265bb584b5d7e36e11091289d58558408880118c`
- Immutable B1 scope-map blob: `bedef47958a728e3f0d56d412f7bdea3ec465856`
- Accepted B1.1 authoring chain:
  - C01 `5659288da80a239e2ded408da87348670c1410c2`
  - C02 `cfd9746e2296280705e2e2e67b2c5980d440f02d`
  - C03 `7546ad74fb0e71ad2120c7091947993690bef82d`
  - C04 `76077695c07b853ac37f058477177e211f740f17`
  - C05 `9c743ab4d5b5ad2ed18000af6a3b80bdace81e16`
  - C06 `e0d6f667d38e937c7c6040b51fb14e34f0bb6345`
  - C07 `be10c01bf8df64a723e135524b75ce644947dcbd`
  - C08 `14729ce490289b057d5dca25767c3b5ea357e1ec`
  - C09 `9f17cee504c51830f0f4fbfbe429ffa8759ea793`
  - C10 `d39ac894d0c6fcb112071170a75fc1b7b661b449`
- C10 worker history remains `PARTIAL_NOT_PASS_CANDIDATE`; do not fabricate a worker PASS candidate.
- Foundational post-repair re-audit: `POST_REPAIR_REAUDIT.json` at commit `2c9fd7023c6100fecb77a4c7685e184ff4baf47b`
- Revised gap register: `FOUNDATIONAL_GAP_REGISTER.json` at commit `32642a59d6451fb16068de68432ba840338b75a9`
- Current foundational result: `F13-R01..F13-R10 COVERED`, `F13-G01..F13-G09 CLOSED_COVERED`, `FOUNDATIONAL_GAP_COUNT = 0`.
- Effective foundational overlays are present at true owners C02, C03, C04, C07 and C10.

## Required work

### I1 — Build the effective curriculum view

Read accepted C01-C10 plus every effective foundational overlay and explicit supersession record. Do not audit only accepted base commits and do not audit only the overlay summaries.

### I2 — Stable-ID and supersession integrity

Verify all appended Claim IDs / Foundational Objective IDs are unique, all supersession chains resolve to one effective version, and no accepted stable ID was silently renumbered or overwritten.

### I3 — Claim/objective semantic closure

For every effective foundational objective and every affected accepted objective, verify that listed support claims actually cover the objective semantics. Row existence or status flags alone are insufficient.

### I4 — Ownership and semantic-duplicate audit

Verify each foundational meaning remains at its true owner. Detect semantic collisions across C01-C10 and overlays; distinguish valid prerequisite/cross-link reuse from duplicate primary ownership.

### I5 — Prerequisite/dependency audit

Verify the effective prerequisite graph is academically necessary, acyclic, and has no dangling IDs. Foundational common-spine objectives must not depend on specialist C05/C06/C08/C09 content unless the meaning genuinely requires it. Locked future scopes must supply zero support Claim IDs.

### I6 — Foundational zero-gap preservation

Reconfirm that integration does not invalidate the zero-gap result. `FOUNDATIONAL_GAP_COUNT` must remain `0`; advanced mathematics must not substitute for any R01-R09 foundational meaning.

### I7 — Scope-map and stage-boundary audit

Verify canonical tree and immutable B1 scope-map boundaries remain intact. No B1.2 academic authoring, Lesson Registry, prompts, images, R2, delivery, website or `ACADEMIC_LOCKED` artifact may be produced in this window.

### I8 — Acceptance-history integrity

Preserve accepted C01-C10 history exactly. In particular, C10 remains `DIRECTOR_ACCEPTED_PASS_AFTER_STRUCTURAL_COMPLETION` with worker submission `PARTIAL_NOT_PASS_CANDIDATE`; later foundational overlays are post-acceptance integration artifacts and do not rewrite that history.

### I9 — Persist integration result

Persist a machine-readable integration audit result with explicit PASS/repair findings, counts of collisions/dangling prerequisites/future-scope supports, zero-gap preservation result, and next-gate status.

## Repair rule

If a small, certain defect is found, Director may repair it at the true owner using append-only or explicit supersession semantics, then re-run affected integration checks. If a repair could alter foundational coverage, re-run the affected foundational requirement and do not retain `gap=0` by assumption.

## PASS gates

`DIRECTOR_INTEGRATION_PASS_PENDING_FRESH_SENTINEL` is allowed only if all are true:

- effective accepted-plus-overlay view is coherent;
- stable-ID / supersession audit PASS;
- semantic closure PASS;
- semantic duplicate / ownership audit PASS;
- prerequisite graph PASS acyclic with zero dangling IDs;
- future/locked support Claim IDs = 0;
- `FOUNDATIONAL_GAP_COUNT = 0` remains valid;
- canonical tree / immutable B1 scope-map alignment PASS;
- stage boundary remains `CURRICULUM` only;
- accepted-history integrity PASS.

A Director integration PASS still does **not** unlock B1.2. The mandatory next gate is a fresh `DIRECTOR-BACKUP-S01` result of `TREE_ALIGNMENT_PASS` against the post-integration durable state.

## Allowed terminal outcomes

- `DIRECTOR_INTEGRATION_PASS_PENDING_FRESH_SENTINEL`
- `DIRECTOR_INTEGRATION_REPAIR_REQUIRED`
- `BLOCKED_INPUT`
- `BLOCKED_CONTRADICTION`

## Locks

- `B1.2`: `LOCKED`
- `ACADEMIC_LOCKED`: `GATED`
- all later pipeline stages: `GATED`
- `__invalid_probe__`: non-blocking technical anomaly; no action in this window.
