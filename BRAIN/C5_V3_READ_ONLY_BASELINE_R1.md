# C5 V3 — Read-only baseline observation R1

Date: 2026-09-06
Status: COLLECTOR_SOURCE_READY; OPPO_OBSERVATIONS_NOT_YET_RECEIVED
Purpose: begin the user-requested health audit of the existing, single C5 V3 learner. This is an external measurement tool, not another SIGMA, not a native health classifier, not a watchdog, and not a repair mechanism.

## Inheritance and scope

Read `BRAIN/SIGMA_SINGLE_INSTANCE_GOVERNANCE_AND_CURRENT_STATE.md` and repository native-execution directives first. Do not restart historical V2/V4 programs or create a new learner.

Reviewed branch head before this audit: `d34fdf492ad5caab15201bc4f80dcf76b3bf2720`.
Reviewed existing observer: `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_C5_LIVE_OBSERVER_V2.sh`, Git blob `c4d3ed40bbb99ab7b378ec677fd1fe9e4e97fab3`.
Reviewed existing resume guard: `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_C5_V3_MECHANICAL_RESUME_GUARD_V1.sh`, Git blob `8a0bc78ac82eadf0040bad3271b0b27a2cac8f71`.

The observer contains useful table/field definitions but invokes Python. This finite collector reuses its measurement targets with shell plus SQLite CLI, without Python. It does not reimplement learner cognition.
The resume guard checks and possibly starts the exact runner when called, then exits. It is NOT itself a recurring watchdog. Whether a separate recurring supervisor is installed or alive on Oppo remains unverified.

## Canonical target, not a new instance

- Root: `$HOME/SIGMA/sigma_genesis1`
- Declared lineage: `$HOME/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2`
- PID file: `$HOME/SIGMA/sigma_genesis1/C5_V3_CONTINUOUS.pid`
- Log: `$HOME/SIGMA/sigma_genesis1/C5_V3_CONTINUOUS.log`
- DB: `<lineage>/state/state.sqlite3`
- Runner: `<root>/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh`
- Expected runner SHA256 from the guard: `a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb`
- Expected instance identity-record SHA256: `fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125`

Historical PID 20026 is not hardcoded as live proof. PID, process start ticks, boot ID, argv, allowed environment fields, and on-disk runner/core/compiler/VM hashes are observed. Matching names/paths/hashes alone do not attest loaded code or prove exclusive cognitive writer ownership. A fingerprint file is not recreated if missing.

## Exact collector

Path: `SIGMA_PROFESSOR/artifacts/COLLECT_SIGMA_C5_V3_READONLY_BASELINE_R1.sh`
Source commit: `13491e55980c1dc0ff1e98a24cad922f7d770f6d`
Git blob: `21ab9bcdbcd7e0a8e3f5719b0ef028aee755ecaf`
SHA256: `f00bb0e324e13d9f1666e789d187cf55942d96ff6b0530518d91fdff64818d2f`

Run as a separate process (`bash <verified-file>`), never source it. The collector refuses sourcing before modifying shell options.

Three observations are taken with a fixed 30-second pause between completed observations. Each contains process evidence, a bounded raw log tail, SQL counts/recent native records, and recent review/error-vault filenames. Reports are written only under `$HOME/SIGMA_OBSERVATIONS/c5-v3-readonly.XXXXXX`, outside the canonical runtime root. Raw output is retained; displayed control bytes are escaped.

No SIGMA VM launch, compiler invocation, resume guard, package installation, state reset, HOLD deletion, checkpoint, backup/restore, or production repair is requested. No automatic health verdict is emitted.

## Database safety and limitations

The existing DB is opened with SQLite CLI `-readonly`, `-init /dev/null`, and `PRAGMA query_only=ON`. A short read transaction groups the SQL observations. A timeout bounds the SQL subprocess; missing SQLite/timeout tools, unreadable DB, redirected paths, WAL with missing sidecars, and a present nonempty rollback journal produce explicit skipped/error observations, not fabricated zero counters. Schema mismatch or timeout preserves partial output and a nonzero `SQLITE_READ_RC`; do not interpret it as proven database corruption.

No INSERT/UPDATE/DELETE/DDL or WAL checkpoint is requested. Ordinary SQLite locks/WAL shared-memory coordination and filesystem access metadata can still change; absolute zero filesystem writes are NOT claimed. Do not use `immutable=1` against a live-changing DB or copy only its main file and call that a coherent live snapshot. Process/log/file observations and the DB transaction are not one globally atomic snapshot.

SQLite primary references: https://www.sqlite.org/cli.html and https://www.sqlite.org/wal.html .

## Checks actually performed off-device

- Bash syntax: PASS.
- SQL statements on a synthetic matching schema via local Node SQLite API: PASS.
- Read-only connection refuses INSERT on that synthetic fixture: PASS.
- Synthetic main DB bytes unchanged: PASS.
- Missing-root child-process guard: observed RC 4.

These do not prove Oppo CLI compatibility, live C5 state, SIGMA learning health, native health assessment, self-repair, or Internet learning.

## How to interpret the returned evidence

Compare the three samples and their SQL return codes before drawing conclusions. Meaningful structural progress needs exact work/cursor/commit evidence; log growth or raw counts alone are insufficient. No knowledge-count growth during this short interval is not automatically a failure. A native wait or refusal must be preserved exactly. If progress is unobserved, state only that it was unobserved in the sampled interval; do not invent a stalled diagnosis or change a native decision.

After identity and sample interpretation, locate and reuse any admitted native observability/health capability before authoring another. Future diagnosis/action selection belongs to the same SIGMA native runtime; DNA-15 parameter reconstruction is not software repair proof. Do not apply fixes to the sole live writer from this observation step.

## Next action

Run the verified collector once on Oppo and retain `identity.txt`, `sample_1.txt`, `sample_2.txt`, and `sample_3.txt`. Report any HOLD, missing dependency, SQL return code, or identity mismatch without changing permissions/state or restarting C5. Then review exact evidence and select the smallest missing native assessment capability, if one is actually missing.
