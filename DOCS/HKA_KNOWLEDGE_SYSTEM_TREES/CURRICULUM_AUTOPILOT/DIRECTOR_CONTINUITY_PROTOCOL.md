# HKA DIRECTOR CONTINUITY PROTOCOL

## Purpose

Prevent Director context loss from becoming project-state loss or Knowledge Tree drift.

The Director is never required to remember the project from chat. GitHub must carry enough compact state for a replacement Director and a read-only backup sentinel to reconstruct the exact active scope and verify Knowledge Tree alignment.

## Canonical continuity artifacts

1. `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json` on `hka-tree/curriculum-master` — compact current state.
2. `HKA_CURRICULUM_STATE.json` — machine control plane.
3. `WINDOW_REGISTRY.json` — durable window status/accepted commit registry.
4. `DIRECTOR-BACKUP-S01` on `hka-tree/director-backup-sentinel` — read/verify/report-only backup sentinel.
5. Canonical HKA World Tree at `fc799bf1104ab6352710e1801777a971b5179995`.
6. Frozen B1 scope architecture at accepted commit `265bb584b5d7e36e11091289d58558408880118c`.

## Mandatory Director transition rule

Before opening a new academic child window, and immediately after Director acceptance of a worker candidate, the primary Director MUST:

1. update `HKA_CURRICULUM_STATE.json` and `WINDOW_REGISTRY.json`;
2. update `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json` so it reflects the new active/accepted state;
3. ensure the active child contract/open order/status exist durably;
4. run or invoke the Backup Sentinel alignment check;
5. do not release the next window if the Sentinel result is not `TREE_ALIGNMENT_PASS`.

## Backup Sentinel role

The backup window is deliberately non-authoritative.

It may only read canonical tree/scope/state/registry/child files and write its own status/checkpoints on `hka-tree/director-backup-sentinel`.

It MUST return one of:

- `TREE_ALIGNMENT_PASS`
- `TREE_ALIGNMENT_ALERT`
- `RECOVERY_REQUIRED`

It MUST NOT:

- author academic curriculum;
- repair claims/objectives;
- accept worker PASS;
- unlock successors;
- mutate curriculum-master;
- create later pipeline artifacts.

## What it validates

At minimum:

- canonical tree commit and six-branch HKA architecture;
- current pipeline stage and stage order;
- active scope/window/branch/name/topic set against frozen scope architecture;
- accepted predecessor and Director-accepted commit chain;
- dependency amendments;
- locked/future-scope support prohibition;
- successor lock until Director acceptance;
- no post-CURRICULUM artifact while CURRICULUM is active;
- no silent stable-ID renumbering.

## Replacement Director bootstrap

A replacement Director reads, in order:

1. `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json`
2. `HKA_CURRICULUM_STATE.json`
3. `WINDOW_REGISTRY.json`
4. active dependency amendments
5. Director latest status/checkpoint
6. Backup Sentinel latest status/checkpoint
7. active child status/contract/open order
8. exact accepted predecessor artifacts as needed

Then verify SHAs and continue only from durable `next_action`.

## Key principle

**ChatGPT does not have to remember HKA. GitHub must remember HKA for ChatGPT.**

The Backup Sentinel exists to detect drift, not to produce academic content.
