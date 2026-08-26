# Reproducibility Status

RELEASE_ID=SIGMA_PSI_RELEASE_CANDIDATE_20260826

## Classification

Exact reproducibility requires independently regenerated artifact identity. No artifact in this Window H package has independently regenerated SHA-256 evidence.

"Compile RC=0" and "VM RC=0" are preserved as execution evidence where frozen, but they are not exact reproducibility.

## Status

| Artifact group | Classification | Evidence | Not proven beyond |
|---|---|---|---|
| current compiler binary | SINGLE_OBSERVED_BUILD plus NOT_PROVEN_REPRODUCIBLE | SHA256 recorded as 65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71 | compiler version, flags, libc, Android build, exact rebuild |
| current VM binary | SINGLE_OBSERVED_BUILD plus NOT_PROVEN_REPRODUCIBLE | SHA256 recorded as 029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99 | build flags, source identity, exact rebuild |
| current runtime source fixture | ARCHIVED_ONLY plus NOT_PROVEN_REPRODUCIBLE | SHA256 recorded as 57b275467d42de4b5404a57f486a1706a46f5a4c0626bbec0c045757cde0602e | private source contents, semantic validity |
| fresh Window A bytecode | SINGLE_OBSERVED_BUILD plus NOT_PROVEN_REPRODUCIBLE | SHA256 903d78f901ffca4b523d4df3b19e875f1a5f4788bf85fcdbdde611621b769e7a; SIZE=8273; compile RC=0; VM RC=0 | independent byte-exact rebuild |
| Window C byte-exact artifacts | ARCHIVED_ONLY plus NOT_PROVEN_REPRODUCIBLE | seven SHA-256 values in HASH_MANIFEST.tsv | current compiler epoch or current VM malformed behavior |
| public conformance suite files | ARCHIVED_ONLY plus NOT_PROVEN_REPRODUCIBLE | Git blob identity and size at commit c2f18816a92b4912c02fe4cbdeccb3bd2637e7e9/39c6dd40a0963d69ebc3b2c3f5e7dde6ce80d17f | SHA-256, regenerated suite identity |
| frozen window reports | ARCHIVED_ONLY plus NOT_PROVEN_REPRODUCIBLE | Git blob identity, size, and frozen commit chain | report SHA-256 and independent regeneration |

EXACT_REPRODUCIBLE_ARTIFACTS=0
BEHAVIORALLY_REPRODUCIBLE_ARTIFACTS=0
SINGLE_OBSERVED_BUILD_ARTIFACTS=3
NOT_PROVEN_REPRODUCIBLE_ARTIFACTS=27
