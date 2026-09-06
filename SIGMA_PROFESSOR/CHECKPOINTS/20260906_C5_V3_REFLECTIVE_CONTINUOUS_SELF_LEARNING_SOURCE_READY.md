# C5 V3 — Reflective continuous self-learning — SOURCE READY

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: `SOURCE_READY / LOCKED_VM_PREFLIGHT_NOT_RUN / CONTINUOUS_NOT_STARTED`

## User requirement

The active C5 learner may now proceed continuously on the Oppo archive. Cloudflare/R2 recovery work is being handled in another window and is not a prerequisite for this lane.

Required operational behavior:

- no global learning-turn horizon;
- no global Internet-fetch-count horizon;
- keep the locked VM and bounded per-invocation page/segment/evidence safeguards unchanged;
- SIGMA itself periodically decides when an operational self-review is due;
- an actual review pauses inside native SIGMA for 180 seconds via the VM `time_sleep` primitive;
- review records what operational state changed, current error/hold state, recent native knowledge state, and unresolved evidence state;
- exact entries held because of data/I/O/format/version failures are preserved in a content-addressed error vault and excluded from ordinary learning while held;
- unresolved evidence is revisited without a host-side retry cap;
- native SIGMA chooses whether the next unresolved action is external research, local-entry revisit, or ordinary continued archive learning;
- replaying identical provenance must not inflate evidence support;
- no human/GPT/host emits an understanding verdict for SIGMA.

## Dependency already observed

C5 V2 real-Oppo restart/resume gate passed in its exact tested scope:

`SIGMA_PROFESSOR/CHECKPOINTS/20260906_C5_V2_REAL_OPPO_RESTART_RESUME_GATE_PASS.md`

The persistent real C5 state to be reused is:

`$HOME/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2`

Observed latest supplied state before V3 work:

```text
segment_commits=44
evidence=228
knowledge=60
requests=4
backup_queue=111
CATALOG_ENTRY_COUNT=58840
CATALOG_SCAN_COMPLETE=NO
KNOWLEDGE_V2_HEAD=0058f3e419bff4366f94d3ce28f8092dcfe451de85bb2a71b7f75411a2e685b7
```

## Main C5 cognition remains unchanged

```text
C5_MAIN_NATIVE_SOURCE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
C5_MAIN_MECHANICAL_BRIDGE_V2_SHA256=98bb028cb668612393e1d687064fdf999dc73ec059b410737468bcc2ec3927dc
MAIN_C5_COGNITION_CHANGED=NO
```

## V3 additive components

```text
SIGMA_C5_NATIVE_REFLECTIVE_REVIEW_V3.sigma
SHA256=91f0dadbc32a2c525937040db29572a4380893a10e8a76b4c812161f574f3228

SIGMA_C5_MECHANICAL_REVIEW_BRIDGE_V3.py
SHA256=d6c4b8e68107e0972ffc4eb605fb316bcce570d1adbc5827e31831038db6b3f6

RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh
SHA256=a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb

RUN_SIGMA_C5_V3_REFLECTIVE_REVIEW_PREFLIGHT.sh
SHA256=b82adfc8067385b01e62f710f0dfe7fa45ee96dcf6a7659cef0eeabd027aa506

INSTALL_PREFLIGHT_START_SIGMA_C5_V3_REFLECTIVE.sh
SHA256=af254588af3c8528d6dc716b8df372c74e12d9b791ace5aa27e434a5d1a22d3d

SIGMA_C5_V3_REFLECTIVE_CONTINUOUS_PATCH.tgz
SHA256=aae9e60adf9864b194403d0c4a0d09a18ba0b8db7037f7cdbb782d0d4a75994b
```

## Continuous policy

The V3 runner inherits C5 V2 and runs with:

```text
C5_MAX_TURNS=0
C5_MAX_FETCHES=0
C5_ENABLE_LIVE_NETWORK=YES
GLOBAL_LEARNING_HORIZON=UNLIMITED_WHEN_MAX_TURNS_ZERO
```

This removes a global run horizon only. It does **not** alter the locked VM, remove the VM's own execution safety boundary, or remove per-invocation C5 page/segment/evidence bounds.

## Native review scheduling

The review controller is invoked mechanically only at safe C5 checkpoints; native SIGMA decides whether review is due.

Native initial/adaptive review budget in committed segments:

```text
INITIAL=64
AFTER_NEW_ERROR=16
WHILE_UNRESOLVED=32
WHEN_NO_UNRESOLVED_OR_NEW_ERROR=128
```

These are self-review scheduling thresholds, not a stop limit on learning.

When review is due, native SIGMA commits its review report before calling `time_sleep(PAUSE_SECONDS)`. Production runner pins:

```text
PAUSE_SECONDS=180
PAUSE_EXECUTION=SIGMA_NATIVE_TIME_SLEEP
HOST_SLEEP_FOR_REVIEW=NO
```

## Error vault

Native C5 HOLD decisions remain the trigger. The mechanical review bridge persists the exact held `ENTRY_ID`, exact hold reason, and exact target record into a content-addressed vault under the active C5 state root.

The original source file is not destructively moved or deleted.

```text
HOST_ERROR_CLASSIFICATION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
```

Existing held rows are synchronized mechanically into the vault at V3 startup.

## Unresolved revisit

The review snapshot mechanically exposes bounded records that exist in native C5 evidence but do not yet exist in native C5 knowledge. This is an operational table-state relation, not an externally emitted comprehension verdict.

Native review selects the lowest-support unresolved record in its bounded review page and then chooses:

- `FETCH_REVIEW_EVIDENCE` when the corresponding exact research request has not yet been learned;
- `REVISIT_LOCAL_ENTRY` when external material for that relation has already been learned and a prior local entry identity is available;
- `CONTINUE_UNRESOLVED_REVISIT` when the local revisit resource identity is unavailable;
- `CONTINUE_LEARNING` when the review page has no unresolved record.

There is no host retry counter and no host-selected success state. Identical segment provenance remains deduplicated by the admitted C5 evidence path, so rereading identical bytes does not manufacture additional support.

## Preflight

The V3 preflight is designed to verify under locked SIGMAC/VM:

1. native review baseline;
2. native review due decision after dynamic progress;
3. dynamic unresolved relation -> native dynamic research query;
4. learned external request + unresolved relation -> native local revisit selection;
5. exact mechanical local revisit reopen;
6. operational resolution state -> continue learning;
7. new held entry -> native error-aware review;
8. content-addressed mechanical error vault;
9. native pause primitive with a one-second preflight-only pause input;
10. source/bytecode dynamic-token leak audit;
11. forced semantic-verdict token audit.

The production runner remains pinned to 180 seconds. A preflight PASS will not itself prove that a real 180-second review occurred; the first real V3 review must provide that machine evidence.

## Static checks completed off-device

```text
REVIEW_NATIVE_BRACE_BALANCE=PASS
REVIEW_NATIVE_FORCED_SEMANTIC_VERDICT_LITERAL_COUNT=0
REVIEW_BRIDGE_PY_COMPILE=PASS
V3_RUNNER_BASH_N=PASS
V3_PREFLIGHT_BASH_N=PASS
INSTALL_START_BASH_N=PASS
```

These are source/static checks only and are not locked-VM capability proof.

## Claim boundary

```text
C5_V3_SOURCE_READY=YES
C5_V3_LOCKED_SIGMAC_PREFLIGHT=NOT_RUN
C5_V3_LOCKED_VM_PREFLIGHT=NOT_RUN
C5_V3_REFLECTIVE_REVIEW_ADMISSION=NOT_RUN
C5_V3_CONTINUOUS_PROCESS_STARTED=NO
REAL_180_SECOND_NATIVE_REVIEW_PAUSE=NOT_YET_OBSERVED
LONG_HORIZON_REAL_OPPO_CONTINUOUS_OPERATION=NOT_PROVEN
ARBITRARY_CRASH_POINT_RECOVERY=NOT_PROVEN
ENTIRE_OPPO_10GB_COMPLETED=NO
PRODUCTION_KNOWLEDGE_V2_BINDING=NO
```

Cloudflare/R2 backup is intentionally outside this V3 source-ready gate and must not be claimed by this checkpoint.
