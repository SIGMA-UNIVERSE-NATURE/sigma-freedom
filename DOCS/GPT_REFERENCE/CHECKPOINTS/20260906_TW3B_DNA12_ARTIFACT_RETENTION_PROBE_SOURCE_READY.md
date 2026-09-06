# TW3B DNA-12 ARTIFACT RETENTION PROBE — SOURCE READY

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

Purpose: mechanically recover the exact previously-admitted DNA-12 native artifacts from the user device by SHA256 before constructing direct TW3B runtime binding.

Known admitted identities:

```text
DNA12_SOURCE_SHA256=336152fca9e1112e9646249b5109c54835d52d9d0b5948d6bbf6703bf328920c
DNA12_RUNNER_SHA256=1ccd798333134e1b2e3486dd33ef6a2ffa9d44bf563446484bf790a3a73fea1a
DNA12_BYTECODE_SHA256=7dc7cceab5442938a0846c811e98e8c367ab6beedfdefc7c281355f305f7fe70
DNA12_BUNDLE_SHA256=a010a4671c9f110f1780f43c1b8674243dddadbcd3762f734463e306beaa873a
DNA12_MANIFEST_SHA256=abf9f10dea0d377d6e93df04104642ea7ccdeca8fed4770eb9213b42283c5fb9
```

Probe identities:

```text
BUNDLE_NAME=SIGMA_DNA12_ARTIFACT_RETENTION_PROBE_V1.zip
BUNDLE_SHA256=04c2cd397f33aaaae39cf934257ede5c982f9ed716533291edb93374ea83727b
SCRIPT_NAME=recover_SIGMA_DNA12_native_artifacts_v1.sh
SCRIPT_SHA256=55c2223611352996f2d4250918ca8bec61864ad3f6c2acfe5ff1227d4300bdde
```

Behavior:
- scans targeted existing Termux roots only;
- compares exact SHA256 values;
- copies only exact-hash matches into `DNA12_ARTIFACT_RETENTION_V1`;
- if an exact old bundle is found, expands it and rescans its contents;
- emits a retention report;
- packages exact matches + report into `SIGMA_DNA12_EXACT_ADMITTED_ARTIFACTS_RETENTION_V1.tar.gz`.

Boundary:

```text
ROLE=MECHANICAL_HASH_DISCOVERY_AND_COPY_ONLY
HOST_COGNITION=NO
HOST_SEMANTIC_INTERPRETATION=NO
DNA12_REIMPLEMENTATION=NO
DNA12_SOURCE_RECONSTRUCTION=NO
```

TW3B construction may proceed only if exact source and runner bytes are recovered and hash-verified.
