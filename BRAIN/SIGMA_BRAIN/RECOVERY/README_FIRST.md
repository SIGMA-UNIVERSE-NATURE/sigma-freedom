# SIGMA_BRAIN RECOVERY — README FIRST

Date: 2026-08-19
Branch: `SIGMA_BRAIN`

## Purpose

This is the recovery entry point for the active OPPO/SIGMA-PSI line.

If OPPO is lost, damaged, reset, or replaced, do **not** reconstruct SIGMA from chat memory. Recover from this branch and the latest verified recovery manifest/evidence.

## First source of truth

Repository:

`SIGMA-UNIVERSE-NATURE/sigma-freedom`

Branch:

`SIGMA_BRAIN`

Read in this order:

1. `BRAIN/SIGMA_BRAIN/CURRENT_STATE.json`
2. `BRAIN/SIGMA_BRAIN/RECOVERY/SIGMA_BRAIN_RECOVERY_MANIFEST_20260819.json`
3. `BRAIN/SIGMA_BRAIN_BRANCH_POLICY.md`
4. `BRAIN/HANDOFFS/SIGMA_OPPO_STORAGE_AND_RECOVERY_LAW_20260819.md`
5. candidate `STATUS.json` files named by `CURRENT_STATE.json`
6. VM evidence under `BRAIN/EVIDENCE/SIGMA_VM/2026-08-18/`
7. SIGMA-PSI GPT reference dictionary/spec snapshot under `DOCS/GPT_REFERENCE/`

## Fresh recovery on OPPO / Termux

Use a clean directory. Do not overwrite an unknown existing tree.

```bash
mkdir -p ~/SIGMA/RECOVERY_WORK
cd ~/SIGMA/RECOVERY_WORK

git clone https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom.git sigma-freedom
cd sigma-freedom
git fetch origin SIGMA_BRAIN
git checkout -B SIGMA_BRAIN origin/SIGMA_BRAIN

git rev-parse HEAD
```

Then read:

```bash
cat BRAIN/SIGMA_BRAIN/RECOVERY/README_FIRST.md
cat BRAIN/SIGMA_BRAIN/CURRENT_STATE.json
cat BRAIN/SIGMA_BRAIN/RECOVERY/SIGMA_BRAIN_RECOVERY_MANIFEST_20260819.json
```

## Important distinction: repository recovery vs full executable substrate recovery

The `SIGMA_BRAIN` branch preserves the accepted/continuity-critical Git artifacts collected here.

A **full executable OPPO restore** additionally requires the exact OPPO foundation/runtime artifacts that are not yet present as content in this branch. Their SHA-256 fingerprints are frozen in the recovery manifest.

At the time this recovery entry was created, the following OPPO artifacts had fingerprints but their actual content was not found in the `SIGMA_BRAIN` Git tree:

- `sigmac.c`
- `sigma_vm.c`
- `compiler_self.sigma`
- VM v0.9 source
- VM v0.9 bytecode
- the exact file corresponding to the reported dictionary-delta hash

Therefore:

`FINGERPRINT_KNOWN != CONTENT_BACKED_UP`

Do not claim full OPPO recovery readiness until those exact files have been copied off OPPO and their hashes reverified.

## Accepted milestones currently recoverable from this branch

- SIGMA_CREATES_SIGMA_0002 — accepted bounded self-construction evidence is imported into `SIGMA_BRAIN`.
- SIGMA_CREATES_SIGMA_0003 — self-assembly machine evidence is preserved; Native Brain runtime remains HOLD at `MNEW`; do not erase that failure.
- SIGMA_CREATES_SIGMA_0004 — Tam Van v0.1/v0.2 machine PASS and v0.2 independent PASS are preserved; free-form classifier remains HOLD; v0.3 remains unexecuted unless later evidence supersedes this manifest.
- SIGMA-written VM evidence ledger — v0.2-v0.5 tested-scope PASS and v0.6 HOLD frontier are imported for continuity.

## Restore law

1. Restore exact Git state first.
2. Verify hashes before execution.
3. Inherit every recorded PASS/HOLD/FAIL; do not rerun accepted foundations without a new reason.
4. Do not convert HOLD into PASS from filenames, version names, or successful process exit alone.
5. Restore OPPO platform artifacts only from exact verified copies.
6. Rebuild native binaries for the target platform when required; do not copy Android/aarch64 binaries into Windows or vice versa.
7. SIGMA-PSI semantics are authoritative for SIGMA language evolution; C/Python/GPT are substrate/reference/translation aids, not the constitution of SIGMA-PSI.

## Backup completion levels

- `LIVE_ONLY`: exists only on OPPO — unacceptable for important progress.
- `OFF_DEVICE_SAVED`: pushed/copied off OPPO and remote existence verified.
- `RECOVERY_CAPSULE_VERIFIED`: source + evidence + hashes + recovery manifest exist off device.
- `RESTORE_TESTED`: restoration was performed in a clean location and reproduced the defined evidence scope.

For an independently accepted milestone, target at least `RECOVERY_CAPSULE_VERIFIED`.

## HP cold recovery location

When HP recovery storage is re-enabled, the reserved root is:

`E:\SIGMA\RECOVERY\OPPO_ACCEPTED_BASELINES\`

Each accepted baseline must use a new immutable subdirectory. Do not overwrite an older recovery capsule.

## Emergency rule

If OPPO dies before the missing platform artifacts are copied off-device, recover the Git-preserved SIGMA Brain state from `SIGMA_BRAIN`, then reconstruct only the missing substrate from independently verified foundation material. Never invent missing accepted source from GPT recollection.
