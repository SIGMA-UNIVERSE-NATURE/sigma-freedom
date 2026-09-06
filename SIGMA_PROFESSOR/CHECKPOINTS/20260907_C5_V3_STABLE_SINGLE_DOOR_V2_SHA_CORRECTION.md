# C5 V3 Stable Single Door V2 — SHA correction

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

This checkpoint corrects one packaging metadata error in
`20260907_C5_V3_STABLE_SINGLE_DOOR_STREAM_COHERENCE_V2_SOURCE_READY.md`.

The committed supervisor artifact was correct, but its SHA-256 was recorded
incorrectly in the first installer/checkpoint metadata.

Correct artifact identities:

```text
SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.py
SHA256=cea1bd96d2ebd80538d066467bdceac9ef3053fd09c80c8eac6181173fc3f286

RUN_SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.sh
SHA256=f61bd0f97df3eadacdddb950545d72bdf15f06c635deb1a8270fb68484db7c19
```

The installer was corrected in commit:

```text
80cd75fbe8a56a18c7b7b1d1bbb3f2f4b5691dcc
```

Use that exact commit as the pinned source when installing on Oppo.

The failed Oppo verification reported:

```text
WATCHER_SHA256=cea1bd96d2ebd80538d066467bdceac9ef3053fd09c80c8eac6181173fc3f286
SUPERVISOR_SHA256=f61bd0f97df3eadacdddb950545d72bdf15f06c635deb1a8270fb68484db7c19
```

Therefore the device fetched the committed supervisor correctly; the failure was
caused by the stale expected SHA, not corruption of the artifact.

Operational shell correction:

- do not execute `set -e` in the user's interactive Termux shell for this gate;
- run verification/install inside a child `bash` process/subshell;
- a failed assertion may exit the child installer but must not terminate the
  interactive Termux session.

No locked SIGMA identity component is changed by this correction:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
C5_V3_RUNNER_SHA256=a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb
C5_NATIVE_CORE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
SIGMA_INSTANCE_FINGERPRINT_SHA256=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125
STATE_LINEAGE=$HOME/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2
```

Claim boundary:

```text
PACKAGING_SHA_METADATA_ERROR=CORRECTED
SUPERVISOR_ARTIFACT_CORRUPTION=NO_EVIDENCE
LOCKED_SIGMA_IDENTITY_CHANGED=NO
OPPO_STABLE_V2_RUNTIME_PASS=NOT_YET_REPORTED
```
