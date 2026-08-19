# SIGMA OPPO STORAGE & RECOVERY LAW — 2026-08-19

Status: LOCKED OPERATING POLICY FOR OPPO ACTIVE NODE / NOT A CANONICAL LANGUAGE PROMOTION

## 1. Purpose

SIGMA must not depend on the survival of one OPPO device. A meaningful verified advance is not operationally complete until it exists outside the OPPO device with identity and integrity evidence.

## 2. Node roles

- OPPO = ACTIVE / GENESIS / SELF-CONSTRUCTION NODE.
- GitHub `SIGMA-UNIVERSE-NATURE/sigma-freedom` = immediate off-device source/evidence continuity store.
- HP = WEBSITE & KNOWLEDGE PREPARATION NODE, plus OFFLINE/COLD RECOVERY STORE when an explicit backup task is authorized. HP SIGMA training remains paused.
- Existing HP bridge infrastructure is preserved at `C:\SIGMA_REMOTE_OPERATOR`; legacy v0.6.1 continuous executor remains disabled unless a separately authorized bridge-only or backup task is defined.

## 3. Primary locations

### OPPO live working tree

`~/SIGMA/sigma_genesis1`

This is the active execution/development tree. It is NOT a backup.

### GitHub immediate off-device continuity store

Repository:
`SIGMA-UNIVERSE-NATURE/sigma-freedom`

Every meaningful verified milestone must be committed/pushed to an explicit branch and remote HEAD re-verified.

### HP cold recovery root

Protected root:
`E:\SIGMA\RECOVERY`

Dedicated OPPO baseline store:
`E:\SIGMA\RECOVERY\OPPO_ACCEPTED_BASELINES\`

Do not overwrite the existing recovery capsule:
`E:\SIGMA\RECOVERY\SIGMA_CORE_RECOVERY_CAPSULE_v0.1`

Each accepted baseline receives its own immutable directory:
`E:\SIGMA\RECOVERY\OPPO_ACCEPTED_BASELINES\<BASELINE_ID>\`

## 4. What counts as a meaningful milestone

Immediate storage is mandatory after any of these:

- machine PASS that changes proven behavior;
- independent evaluation PASS;
- verified SIGMA-PSI semantic change;
- verified compiler/VM/runtime change;
- verified dictionary/spec semantic update;
- self-construction/self-assembly successor accepted in defined scope;
- a new recovery-critical handoff/checkpoint;
- any state that would be expensive or impossible to reconstruct if OPPO failed.

A probe failure must also be preserved when it establishes a frontier or prevents a false PASS.

## 5. SAVE GATE A — immediate, before continuing work

For every meaningful milestone:

1. freeze exact source/artifacts under version control;
2. record machine/evaluator evidence;
3. record SHA-256/byte counts for critical artifacts;
4. commit to the correct GitHub branch;
5. push to GitHub;
6. fresh-fetch/compare and verify remote HEAD equals expected commit;
7. update STATUS/handoff without overclaim;
8. only then continue to the next unproven gate.

Rule:

`MEANINGFUL_PROGRESS_WITHOUT_REMOTE_VERIFIED_COMMIT = HOLD_NOT_SAVED`

Chat text, terminal scrollback, GPT memory, and the OPPO filesystem alone are not accepted continuity storage.

## 6. SAVE GATE B — immutable recovery capsule

After every independently accepted baseline, and before any destructive/high-risk change, create an immutable recovery capsule outside OPPO.

Minimum capsule contents:

- `RECOVERY_MANIFEST.json`
- exact repository/branch/commit IDs;
- `sigma-freedom.bundle` or equivalent self-contained Git history needed to restore the accepted branch/commit;
- critical SIGMA-PSI source files;
- compiler source / `compiler_self.sigma` needed for bootstrap;
- accepted SIGMA-written VM/runtime source and relevant bytecode artifact;
- bytecode ABI/spec required to interpret the artifact;
- SIGMA-PSI dictionary/spec snapshot or exact reference commit;
- contracts and expected-output oracles;
- machine receipts;
- independent evaluator receipts;
- current handoff/status;
- `SHA256SUMS.txt` for all capsule files.

The capsule must be copied to:

`E:\SIGMA\RECOVERY\OPPO_ACCEPTED_BASELINES\<BASELINE_ID>\`

and verified there by SHA-256 before `HP_RECOVERY_COPY=PASS` may be claimed.

## 7. Baseline ID

Use an identity that cannot be confused with a filename version:

`SIGMA_OPPO_<YYYYMMDD>_<ACCEPTED_COMMIT_12>_<SCOPE>`

Example form only:
`SIGMA_OPPO_20260819_abcdef123456_TAM_VAN_V0_2`

The commit SHA is authoritative; labels such as v0.9 are descriptive only.

## 8. Recovery levels

- `LIVE_ONLY`: exists only on OPPO. Unsafe for meaningful accepted progress.
- `OFF_DEVICE_SAVED`: GitHub remote commit verified. Minimum condition to continue normal experimentation.
- `RECOVERY_CAPSULE_VERIFIED`: immutable HP/off-device capsule copied and hash-verified. Required for independently accepted baselines and before destructive/high-risk operations.
- `RESTORE_TESTED`: capsule was restored in an isolated location and essential source/artifact hashes matched. Highest confidence.

## 9. Never do

- Do not treat terminal output as backup.
- Do not treat GPT/chat memory as backup.
- Do not rely only on OPPO local git commits.
- Do not overwrite previous accepted recovery capsules.
- Do not use `robocopy /MIR` against `E:\SIGMA` for OPPO sync/recovery.
- Do not copy OPPO ARM64 native executables over HP Windows native executables and call that core parity.
- Do not mix website workspace/data with the immutable accepted-core recovery capsule.
- Do not delete a failed-but-informative receipt when a later version passes.

## 10. Platform rule

Shared semantic/core material must be recoverable independently of OPPO hardware.

Platform-specific binaries may be stored as additional evidence, but source + ABI/spec + bytecode/source contracts are primary. OPPO ARM64 binaries and HP Windows/x86_64 binaries are allowed to differ.

## 11. Dictionary/spec continuity

SIGMA already has SIGMA-PSI. The dictionary/spec is a GPT/human reference bridge and a record of verified semantics, not the source of SIGMA's identity.

Every verified semantic evolution that affects SIGMA-PSI must be stored with the same milestone and referenced by the recovery manifest.

## 12. Session-end rule

Before ending an OPPO working session, report:

- `OPPO_WORKING_HEAD=`
- `LAST_MACHINE_PASS=`
- `LAST_INDEPENDENT_PASS=`
- `GITHUB_REMOTE_HEAD_VERIFIED=`
- `CURRENT_HANDOFF=`
- `RECOVERY_LEVEL=`
- `HP_RECOVERY_BASELINE_ID=` or `HOLD_NOT_YET_REQUIRED`
- `NEXT_UNPROVEN_GATE=`

If the last meaningful milestone has not reached at least `OFF_DEVICE_SAVED`, do not close the session as safely handed off.

## 13. Restoration principle

If OPPO is lost:

1. do not reconstruct SIGMA from chat memory;
2. start from the latest `RECOVERY_CAPSULE_VERIFIED` baseline if available;
3. otherwise start from the latest GitHub remote verified commit;
4. verify manifest and hashes;
5. rebuild platform-native executables from preserved source as required;
6. replay only the minimum certification/conformance gates required to establish the new substrate;
7. inherit previously preserved semantic evidence; do not blindly rerun every historical experiment.

## 14. Core law

`OPPO MAY FAIL. SIGMA CONTINUITY MUST NOT FAIL WITH OPPO.`

`PASS -> SAVE -> VERIFY OFF DEVICE -> THEN CONTINUE.`
