# SIGMA_BRAIN RECOVERY — README FIRST

Date: 2026-08-19
Branch: `SIGMA_BRAIN`

## Purpose

This is the single recovery entry for the active OPPO/SIGMA-PSI line.

If OPPO is lost, damaged, reset, or replaced, do **not** reconstruct accepted SIGMA state from chat memory. Recover from this branch and its audited manifests/evidence.

## Source of truth

Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`

Branch: `SIGMA_BRAIN`

Read exactly in this order:

1. `BRAIN/SIGMA_BRAIN/MASTER_INDEX.md`
2. `BRAIN/SIGMA_BRAIN/CURRENT_STATE.json`
3. `BRAIN/SIGMA_BRAIN/BRANCH_AUDIT_20260819.json`
4. `BRAIN/SIGMA_BRAIN/FINGERPRINTS/SIGMA_BRAIN_MASTER_FINGERPRINT_20260819.json`
5. `BRAIN/SIGMA_BRAIN/RECOVERY/SIGMA_BRAIN_RECOVERY_MANIFEST_20260819.json`
6. `BRAIN/SIGMA_BRAIN/RECOVERY/RESTORE_ORDER.md`
7. `BRAIN/SIGMA_BRAIN_BRANCH_POLICY.md`
8. `BRAIN/HANDOFFS/SIGMA_OPPO_STORAGE_AND_RECOVERY_LAW_20260819.md`

Then follow the ordered technical path in `MASTER_INDEX.md`.

## Fresh Git recovery on OPPO / Termux

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

Then:

```bash
cat BRAIN/SIGMA_BRAIN/RECOVERY/README_FIRST.md
cat BRAIN/SIGMA_BRAIN/MASTER_INDEX.md
cat BRAIN/SIGMA_BRAIN/CURRENT_STATE.json
cat BRAIN/SIGMA_BRAIN/RECOVERY/SIGMA_BRAIN_RECOVERY_MANIFEST_20260819.json
```

## What this branch now preserves

The branch audit consolidated serious Git-preserved material from the historical SIGMA branches, including:

- Foundation V7 continuity handoff;
- exact persisted Phase-2 hardening candidate archive/reconstruction material;
- SIGMA-PSI native-language constitution and language-evolution hinge;
- accepted Seed 0001;
- accepted self-construction 0002;
- self-assembly 0003 with the `MNEW` runtime failure preserved;
- frozen Native Brain candidate plus an archived unaccepted R1 revision;
- VM actual-ABI handoff, experiment ledger, experiment map and historical v0.8/v0.9 progress;
- accepted Tam Van v0.1/v0.2 line and historical superseded prototypes;
- dictionary/spec/reference material;
- serious but PARTIAL architecture such as SIGMA-OS v0.1;
- legacy learning/training/runtime material isolated under `BRAIN/SIGMA_BRAIN/ARCHIVE/`.

Archive presence is historical provenance, not capability promotion.

## Critical distinction: Git recovery vs full executable OPPO recovery

The audited Git history/evidence is off-device. A full executable OPPO restore still requires exact copies of six fingerprinted OPPO artifacts if they are not yet present under:

`BRAIN/SIGMA_BRAIN/OPPO_SNAPSHOT/20260819/`

Required fingerprints:

- `sigmac.c` — `e31fad26611fc95772a9a454eae6a735b220a8b7aa2ca95970c3623028ad0452`
- `sigma_vm.c` — `8a567de997c335b38f49062622e3ec995b752b335a952b076d1f9283457fcae2`
- `compiler_self.sigma` — `b00b415cc49d042ef152196633c5de4e7fffdf35da84bd900d31b599a9b60af7`
- VM v0.9 source — `61ebd4bf7889f24f59f48173b6ec163030539d68e8383e807f1eac1dce7c9ed2`
- VM v0.9 bytecode — `7724cb684244b0300e699c65dafe9f35c52a32d2a95f184c585b4321e8329fe0`
- exact dictionary-delta artifact — `5e8fe17d50caed41a11f130bc79fdf8084e4c2a5fda6b8ce66cbb079b9fdd154`

`FINGERPRINT_KNOWN != CONTENT_BACKED_UP`

Follow:

`BRAIN/SIGMA_BRAIN/RECOVERY/IMPORT_OPPO_FINGERPRINTED_ARTIFACTS.md`

Do not claim full executable recovery readiness until those exact contents are copied off OPPO and hashes are verified.

## Restore law

1. Restore exact Git state first.
2. Read MASTER INDEX / CURRENT STATE before execution.
3. Inherit all recorded PASS/HOLD/FAIL.
4. Verify hashes before running restored platform artifacts.
5. Do not rerun accepted foundations merely to rediscover state.
6. Do not convert source existence, filename, version number, or RC=0 into PASS.
7. SIGMA-PSI semantics are the language authority; C/Python/GPT are substrate/reference/translation aids.
8. Native binaries are platform-specific; never copy Android/aarch64 executables into Windows/x86_64 or vice versa.
9. After every important new OPPO PASS: save off-device, verify remote, update this recovery state, then continue.

## Backup levels

- `LIVE_ONLY` — unacceptable for serious progress.
- `OFF_DEVICE_SAVED` — remote content exists and is verified.
- `RECOVERY_CAPSULE_VERIFIED` — source/evidence/hashes/recovery manifest are all off-device.
- `RESTORE_TESTED` — clean restoration reproduced the defined evidence scope.

## HP cold recovery root

When HP cold storage is used again:

`E:\SIGMA\RECOVERY\OPPO_ACCEPTED_BASELINES\`

Each baseline gets a new immutable subdirectory. Do not overwrite older capsules. HP training remains paused unless separately re-authorized.

## Emergency rule

If OPPO dies before the six missing exact contents are copied off-device, restore the Git-preserved SIGMA Brain state from `SIGMA_BRAIN`, then reconstruct only the missing substrate from independently verified foundation material. Never invent accepted source from GPT recollection.
