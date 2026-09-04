# HKA Stateless Window Recovery Protocol

## Purpose

Every GPT window must be replaceable. A dead window must not destroy project memory, progress, or production state.

## Bootstrap sequence for every new window

A new window MUST do these actions before authoring:

1. Read `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md` at canonical tree commit `fc799bf1104ab6352710e1801777a971b5179995` for the scope it needs.
2. Read `CURRICULUM_AUTOPILOT/MASTER_PLAN.md`.
3. Read `CURRICULUM_AUTOPILOT/HKA_CURRICULUM_STATE.json`.
4. Read its own `WINDOW_CONTRACT.md` and `GPT_EXECUTION_PROMPT.md`.
5. Read every predecessor artifact listed in the window contract by exact commit/path.
6. Verify that all predecessor statuses are accepted.
7. Continue only the `next_action` assigned to the window.

The window MUST NOT rely on chat memory, summaries, or claims that another window finished work unless GitHub contains the accepted artifact.

## Checkpoint contract

Every execution window must produce:

- `RESULT.json` — machine-readable result and status.
- `HANDOFF.md` — concise human-readable continuation note.
- Academic/curriculum artifacts defined by its contract.

A completed window ends with one of:

- `PASS`
- `BLOCKED_INPUT`
- `BLOCKED_CONTRADICTION`
- `REVIEW_REQUIRED`

Only `PASS` may unlock its successor.

## Crash recovery

If a window dies:

1. Replacement reads the state file.
2. It checks whether `RESULT.json` exists and is `PASS`.
3. If `PASS`, it does not redo the work; it proceeds to the next registered action.
4. If no PASS result exists, it reads the latest committed partial artifacts and resumes only unfinished work.
5. It must preserve stable IDs already committed.
6. It must never silently recreate or renumber accepted nodes, claims, lessons, or assets.

## Idempotency

Every knowledge artifact must have stable IDs. Re-running the same window against the same accepted inputs must not create duplicate canonical records.

Every result records:

- `window_id`
- `input_commit_sha`
- `output_commit_sha` when known
- `scope_ids`
- `counts`
- `duplicate_audit`
- `status`
- `next_action`

## State ownership

- GitHub = canonical durable project memory.
- Cloudflare = runtime state and binary state once production is enabled.
- ChatGPT window = disposable worker.

No ChatGPT window may be the sole holder of a decision required by later windows.

## Long-window rule

If scope cannot be completed reliably within one window, the window must partition by stable canonical sub-scope and write the partition plan to GitHub before continuing. Partitioning must not change the canonical tree architecture.

## Forbidden during curriculum phases

Until `all_curriculum_locked=true`:

- no visual prompt authoring;
- no image generation;
- no R2 image release;
- no website publication based on incomplete curriculum.

Until `all_visual_prompts_locked=true`:

- image production remains disabled.
