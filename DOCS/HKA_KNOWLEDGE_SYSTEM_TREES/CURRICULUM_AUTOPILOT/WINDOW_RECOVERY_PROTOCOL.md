# HKA Stateless Window Recovery Protocol

## Purpose

Every GPT window is disposable. Project memory, progress and production state must survive the loss of any chat window.

Canonical pipeline:

`KNOWLEDGE -> CURRICULUM -> ACADEMIC_LOCKED -> LESSON_REGISTRY -> LESSON_REGISTRY_LOCKED -> PROMPTS -> PROMPT_LOCKED -> IMAGE_PRODUCTION -> R2_STAGING -> INDEPENDENT_QA -> VAULT -> WEB_OPTIMIZE -> DELIVERY -> WEBSITE_UPDATE`

No stage may be skipped.

Durable status reporting is governed by:
`CURRICULUM_AUTOPILOT/STATUS_REPORT_STANDARD.md`.

## Mandatory bootstrap for every new window

Before authoring, a new window MUST:

1. Read `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md` at the canonical commit required by its scope.
2. Read `CURRICULUM_AUTOPILOT/HKA_PIPELINE_CANONICAL.json`.
3. Read `CURRICULUM_AUTOPILOT/MASTER_PLAN.md`.
4. Read `CURRICULUM_AUTOPILOT/HKA_CURRICULUM_STATE.json`.
5. Read `CURRICULUM_AUTOPILOT/STATUS_REPORT_STANDARD.md`.
6. Read `CURRICULUM_AUTOPILOT/WINDOW_REGISTRY.json`.
7. Read the latest predecessor/current `STATUS_REPORTS/<WINDOW_ID>/STATUS.json` and `REPORT.md` when present.
8. Read its own `WINDOW_CONTRACT.md` and `GPT_EXECUTION_PROMPT.md`.
9. Read predecessor artifacts by exact commit/path.
10. Verify predecessor PASS/LOCKED gates and verify `current_stage` permits its work.
11. Execute only the recorded `next_action` and assigned scope.

If chat history conflicts with GitHub state, GitHub state wins.

## Mandatory live status folder

Every worker, controller and Director MUST maintain:

`CURRICULUM_AUTOPILOT/STATUS_REPORTS/<WINDOW_ID>/`

with at least:

- `STATUS.json`
- `REPORT.md`
- append-only `CHECKPOINTS/<CHECKPOINT_ID>.json` records for meaningful checkpoints.

The status folder is updated after substantial completed work, before switching sub-scope, when blocked, after durable external writes, and before PASS.

A worker that dies before PASS is recovered from this folder plus committed outputs. The replacement does not need the old chat transcript.

## Checkpoint contract

Every execution window must commit:

- required scope artifacts;
- its durable status folder;
- `RESULT.json`;
- `HANDOFF.md` when a human-readable continuation note is useful.

`RESULT.json` must include at least:

- `window_id`;
- `stage`;
- `status`;
- `input_commit_sha`;
- output paths;
- stable scope IDs;
- counts;
- duplicate/coverage results when applicable;
- `next_action`.

Allowed terminal statuses:

- `PASS`
- `BLOCKED_INPUT`
- `BLOCKED_CONTRADICTION`
- `REVIEW_REQUIRED`

Only `PASS` can unlock the registered successor.

`RESULT.json=PASS` without a valid mandatory status folder is NOT an accepted completion.

## Crash recovery

If a window dies:

1. Replacement reads `HKA_CURRICULUM_STATE.json`.
2. It verifies the canonical stage and active/next action.
3. It reads `STATUS_REPORTS/<WINDOW_ID>/STATUS.json`, `REPORT.md` and latest checkpoint.
4. It checks committed `RESULT.json` for the assigned window.
5. If both durable status and `RESULT.json` record accepted PASS, it must not repeat that work; continue to the registered successor.
6. If PASS is absent, inspect `completed_work`, `remaining_work`, `next_action` and committed partial artifacts; resume only unfinished scope.
7. Preserve all accepted stable IDs and accepted ownership assignments.
8. Never silently recreate, renumber or duplicate accepted Node, Claim, Lesson or Asset records.

## Long-window protection

No large discipline or production batch may depend on one long chat window.

Large scopes must be partitioned before detailed authoring into bounded deterministic child windows. Each child has an independent input commit, stable scope IDs, output paths, durable status folder, `RESULT.json`, PASS checkpoint and successor.

A controller window may define/check child scopes, but completed child artifacts are durable GitHub state and must not be reauthored merely because the controller chat is gone.

## Stage gates

- Until global `ACADEMIC_LOCKED`: no Lesson Registry authoring.
- Until `LESSON_REGISTRY_LOCKED`: no visual/image prompt authoring.
- Until `PROMPT_LOCKED`: no image generation or R2 staging writes.
- Until exact binary is in `R2_STAGING`: Independent QA cannot approve it.
- Until `QA_APPROVED`: no Vault promotion.
- Until `VAULT_VERIFIED`: no Web Optimize.
- Until Web Optimize PASS: no Delivery publication.
- Until `DELIVERY_READY`: no Website Update.

## Durable ownership

- GitHub = canonical knowledge/curriculum/lesson/prompt state, accepted commits, status reports and durable control plane.
- Cloudflare = runtime state and binary state from Image Production onward.
- ChatGPT window = disposable worker only.

No decision required by a later stage may exist only in a chat transcript.

## Director acceptance rule

Before accepting any worker checkpoint or PASS, Director verifies its status folder is present and consistent with committed artifacts.

The Director must maintain its own status folder after governance changes, window creation/unlock, checkpoint acceptance, direct fixes, or changes to `next_action`.

`NO STATUS FOLDER = NO ACCEPTED COMPLETION`.
