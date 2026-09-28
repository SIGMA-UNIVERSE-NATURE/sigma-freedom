# SIGMA VKM Candidate VM — Source/Rebuild Audit

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Source hashes

Canonical source:

Path:
/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/sigma_vkm.c

SHA256:
141cd8d5ab5b212cb5e28d34f71b73a631fe5db6e0c258e1f11ee55477e8225a

Candidate source:

Path:
/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/NATIVE_STRUCTURAL_CODEC_R1/candidate_vm_r1/sigma_vkm_read_range_r1.c

SHA256:
1dde4f6dee0e03badcb6d27ee5b02b5b9621ee1935988011cd33a9b8c65ae7dd

The candidate source is therefore not byte-identical to the current canonical VM source.

## Deterministic rebuild

Candidate source was rebuilt twice with:

clang -O2 -std=c11 -DSIGMA_EXTENDED_STDLIB
-lcurl -lssl -lcrypto -lm -ldl

REBUILD_DETERMINISTIC=PASS

REBUILD_EQUALS_TESTED_CANDIDATE=PASS

## Binary hashes

sigma-vkm-rebuild-a:
bd8442ed04bc638a939bf5a1caf44d2aa1db3c709b3f3da6023d1a47cb629087

sigma-vkm-rebuild-b:
bd8442ed04bc638a939bf5a1caf44d2aa1db3c709b3f3da6023d1a47cb629087

tested candidate binary:
bd8442ed04bc638a939bf5a1caf44d2aa1db3c709b3f3da6023d1a47cb629087

All three binaries are byte-identical by SHA256.

## Candidate source diff audit

CANDIDATE_SOURCE.diff SHA256:
9db2fce5b964708d452406922d142456fe28b466ba22da8c88e68a8c9d9da763

Path:
/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/NATIVE_STRUCTURAL_CODEC_R1/proof/vkm_admission_source/CANDIDATE_SOURCE.diff

## Interpretation boundary

This checkpoint records source provenance and deterministic rebuild evidence for the tested candidate VM binary.

It establishes:
- candidate source differs from the current canonical VM source;
- the candidate source rebuild is deterministic;
- independent rebuilds are byte-identical to the tested candidate binary.

This is source/rebuild admission evidence only. It does not itself establish that the candidate VM has been promoted to canonical production VM.
