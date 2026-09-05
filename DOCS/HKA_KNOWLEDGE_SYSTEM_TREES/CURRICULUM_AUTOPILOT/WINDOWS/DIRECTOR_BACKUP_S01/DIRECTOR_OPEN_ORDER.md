# DIRECTOR OPEN ORDER — DIRECTOR-BACKUP-S01

STATUS: `AUTHORIZED_STANDBY_SENTINEL`

Branch: `hka-tree/director-backup-sentinel`

Role: `READ_VERIFY_REPORT_ONLY`

## Start here

1. Read `WINDOW_CONTRACT.md`.
2. Read `GPT_EXECUTION_PROMPT.md`.
3. Read the latest `STATUS_REPORTS/DIRECTOR-BACKUP-S01/STATUS.json` and latest checkpoint.
4. Bootstrap current project state from `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json` on `hka-tree/curriculum-master`.
5. Verify current state against canonical tree/scope map/state/registry/active child.
6. Return only a compact sentinel alignment report.

## Current baseline at creation

- Canonical World Tree commit: `fc799bf1104ab6352710e1801777a971b5179995`
- Stage: `CURRICULUM`
- Active scope: `B1.1-C06`
- Active window: `C01-W02-B1.1-MATH-FAMILY-C06`
- Active branch: `hka-tree/c01-w02-math-c06`
- Accepted predecessor: `76077695c07b853ac37f058477177e211f740f17`
- C07/C08/C09/C10 remain locked.
- All post-CURRICULUM stages remain gated.

## Non-authority lock

This sentinel cannot accept C06, cannot repair C06, cannot open C07, and cannot mutate `curriculum-master`.

If the primary Director disappears or loses context, this sentinel reports exact durable recovery state to a replacement Director. It does not infer missing state from chat history.
