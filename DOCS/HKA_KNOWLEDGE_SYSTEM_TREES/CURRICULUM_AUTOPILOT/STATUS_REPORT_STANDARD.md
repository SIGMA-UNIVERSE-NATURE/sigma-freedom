# HKA Durable Window Status Report Standard

Status: MANDATORY

## Purpose

Every Director, controller, academic window, lesson window, prompt window, production worker and QA worker is disposable. No useful project state may exist only in chat.

After every meaningful checkpoint, and always before declaring a task complete, the responsible worker MUST write/update a durable status folder on GitHub (or the Cloudflare runtime mirror once binary production begins).

## Canonical folder

For every window/worker:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/<WINDOW_ID>/`

Minimum contents:

1. `STATUS.json` — machine-readable current truth.
2. `REPORT.md` — concise human-readable catch-up report.
3. `CHECKPOINTS/<CHECKPOINT_ID>.json` — append-only checkpoint record for every accepted meaningful milestone.

Runtime stages from IMAGE_PRODUCTION onward may additionally mirror status in Cloudflare, but GitHub remains the durable control-plane index and must contain the canonical references/hashes needed to recover.

## STATUS.json required fields

- `schema_version`
- `window_id`
- `role`
- `stage`
- `status`
- `execution_branch`
- `input_commit_sha`
- `last_checkpoint_commit_sha`
- `last_checkpoint_id`
- `scope_ids`
- `completed_work`
- `remaining_work`
- `output_paths`
- `blocking_issues`
- `decisions_locked`
- `do_not_repeat`
- `next_action`
- `successor_window`
- `updated_at`

Allowed working statuses include:

- `READY`
- `IN_PROGRESS`
- `CHECKPOINTED`
- `PASS`
- `BLOCKED_INPUT`
- `BLOCKED_CONTRADICTION`
- `REVIEW_REQUIRED`
- `FAILED_RECOVERABLE`

Only `PASS` unlocks a registered successor.

## REPORT.md required content

Keep it short and operational. It must answer:

- What was the assigned job?
- What is definitely finished?
- What is not finished?
- What exact files/commits are authoritative?
- What decisions are locked and must not be reopened casually?
- What known risks/errors remain?
- What must the replacement/successor do next?
- What must it NOT redo?

No important fact may appear only in REPORT.md; machine-critical facts belong in STATUS.json or other canonical artifacts.

## Checkpoint timing

A checkpoint is mandatory:

1. after scope/partition is locked;
2. after any substantial academic or production sub-unit is completed;
3. before changing to a new sub-scope;
4. immediately after a durable external write (GitHub commit, R2 object set, QA decision, vault promotion, delivery publication);
5. before PASS;
6. when a blocker is discovered that prevents further work.

Workers should checkpoint before a chat becomes long enough that losing it would cause material rework.

## Crash recovery rule

A replacement worker MUST bootstrap in this order:

1. `HKA_PIPELINE_CANONICAL.json`
2. `HKA_CURRICULUM_STATE.json`
3. its/predecessor `STATUS_REPORTS/<WINDOW_ID>/STATUS.json`
4. `REPORT.md`
5. latest checkpoint record
6. exact output files and commits referenced by the status report
7. its own contract/prompt

If chat history conflicts with durable status, durable status wins.

If `STATUS.json.status=PASS`, replacement MUST NOT repeat the completed scope.

If status is not PASS, replacement resumes from `remaining_work` and `next_action`, preserving all stable accepted IDs and outputs.

## Director responsibility

The Director has the same obligation as every worker. After the Director changes governance, creates/unlocks windows, accepts a checkpoint, fixes a defect or changes next_action, the Director MUST update its own status folder.

The Director must also verify that a worker's status folder exists before accepting that worker as PASS.

## Acceptance rule

From activation of this standard onward:

`NO STATUS FOLDER = NO ACCEPTED COMPLETION`

A `RESULT.json=PASS` without the required status folder is incomplete and cannot unlock the successor.
