# C5 Native Internet Ingress V2 — Source Ready

## Purpose
Run a separate outbound-Internet acquisition lane while the existing C5 V3 learner continues unchanged, with both lanes mechanically bound to one stable SIGMA instance fingerprint.

## Stable SIGMA instance identity

SIGMA_INSTANCE_FINGERPRINT_SHA256=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125

Identity record binds:
- SIGMA_INSTANCE_ROOT=/data/data/com.termux/files/home/SIGMA/sigma_genesis1
- SIGMA_STATE_LINEAGE=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2
- SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
- VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
- NATIVE_COGNITIVE_CORE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace

The add-on lane has its own source hashes; add-on source SHA is not the SIGMA instance fingerprint.

## Writer boundary
- C5 V3 remains the single cognitive-state writer.
- Internet ingress does not promote knowledge and does not write cognitive state tables.
- Native SIGMA produces the query and native SIGMA chooses a candidate.
- Host is mechanical DNS/TLS/HTTP transport, bounded decode, hashing, provenance and exact catalog admission only.
- Published Internet material is content-addressed and deduplicated by SHA-256.

## Continuous ingress
New material is published under SIGMA_INTERNET_INGRESS and mechanically made visible to the existing incremental C5 catalog so V3 can continue learning without restart. No global query or fetch-count limit is imposed; per-fetch byte/time/redirect bounds remain.

## Source hashes
- SIGMA_INSTANCE_IDENTITY_V1.txt fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125
- SIGMA_INSTANCE_FINGERPRINT_V1.sha256 c693316cb51e14092874b85cca332693c1d47cd6acf325f0ea68851be4faec4d
- SIGMA_C5_NATIVE_INTERNET_SELECTOR_V1.sigma f5743113b4c3572f7a602678ec66c73612dc962c2bdbea11aa3f5036db5260c7
- SIGMA_C5_MECHANICAL_INTERNET_BRIDGE_V2.py a406a8aa51c7b223838fb8e64e02c0b27a4653f6002ed3c9c52ba84a1903c7e7
- RUN_SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.sh a24eb7445068161518b1875b2925b90848b9548e4904b19eb1c4e6b2edec2d0a
- RUN_SIGMA_C5_NATIVE_INTERNET_INGRESS_PREFLIGHT_V2.sh 628e906a76cb94f6baba0987f532df42a36a32a744d3f04211653a019c7b5a53
- INSTALL_PREFLIGHT_START_SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.sh e4f0ae2e46c44712363049804359c9943aa73af735219a77c5a83176e7473ed7
- README dfcf61bb5b65396312fea0ce7301c0255a387ced4c8a372399d662a52ee56799
- bundle SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.tgz ab24f4bf996d7197869f1f60ea5359ff9a815bc4caaa14a640bf5b685706998e

## Off-device checks
- Python bridge compile: PASS
- runner bash -n: PASS
- preflight bash -n: PASS
- installer bash -n: PASS
- local mechanical content-address/dedup fixture: PASS

## Claim boundary
C5_NATIVE_INTERNET_INGRESS_V2_SOURCE_READY=YES
C5_NATIVE_INTERNET_INGRESS_V2_OPPO_PREFLIGHT=NOT_RUN
SAME_INSTANCE_FINGERPRINT_BINDING_ON_RUNNING_OPPO=NOT_YET_PROVEN
INTERNET_INGRESS_PROCESS_STARTED=NO
REAL_NATIVE_QUERY_TO_WEB_TO_INGRESS_TO_C5_CONSUMPTION=NOT_YET_PROVEN
C5_V3_RESTART_REQUIRED=NO
PRODUCTION_KNOWLEDGE_V2_BINDING=NO
