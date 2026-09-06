# C5 Internet Ingress V2 — Same-Instance Fingerprint Source Ready

Date: 2026-09-06
Branch: `SIGMA_LIFE`

## Goal

Run a separate continuous outbound-Internet acquisition lane while the existing C5 V3 learner keeps running unchanged, with both lanes mechanically bound to one stable SIGMA instance fingerprint and with C5 V3 remaining the single cognitive-state writer.

## Stable SIGMA instance fingerprint

`SIGMA_INSTANCE_FINGERPRINT_SHA256=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125`

This is SHA-256 of the canonical `SIGMA_INSTANCE_IDENTITY_V1.txt`, which binds:

- instance root `/data/data/com.termux/files/home/SIGMA/sigma_genesis1`
- state lineage `/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2`
- locked sigmac SHA `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- locked VM SHA `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- native C5 cognitive core SHA `1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace`
- locked SIGMA VM execution engine and native cognition ownership
- single C5 V3 cognitive-state writer boundary

Add-on Internet-lane component hashes are admission-pinned separately so an add-on upgrade does not silently redefine the stable SIGMA instance fingerprint.

## Architecture

- C5 V3 continues as the sole cognitive-state writer.
- Internet V2 sidecar observes exact native queries emitted by C5 V3.
- Host does not generate queries, rank/select web results semantically, select URLs, or promote knowledge.
- General web discovery is mechanical HTTPS transport and parsing.
- Candidate choice is executed by native selector source under the locked SIGMA VM.
- Exact native-selected HTTPS URL is fetched with public-address validation and per-fetch time/byte/redirect bounds.
- Decoded bytes are published content-addressed under `SIGMA_INTERNET_INGRESS/material/<sha-prefix>/<sha>.document`.
- Provenance remains in the excluded `.sigma_c5/internet_ingress_v2/runtime_state/provenance` area and includes the SIGMA instance fingerprint.
- The exact published material file is mechanically admitted into the existing catalog DB with `policy=LEARN`; this does not select the file as work and does not write the C5 cognitive-state DB.
- The exact-query external cache is populated only if absent so the live V3 fetch path may reuse it.
- No global query-count or fetch-count limit is imposed. Per-fetch safety bounds remain.

## Source component SHA-256

- `SIGMA_INSTANCE_IDENTITY_V1.txt` — `fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125`
- `SIGMA_INSTANCE_FINGERPRINT_V1.sha256` — `c693316cb51e14092874b85cca332693c1d47cd6acf325f0ea68851be4faec4d`
- `SIGMA_C5_NATIVE_INTERNET_SELECTOR_V1.sigma` — `f5743113b4c3572f7a602678ec66c73612dc962c2bdbea11aa3f5036db5260c7`
- `SIGMA_C5_MECHANICAL_INTERNET_BRIDGE_V2.py` — `a406a8aa51c7b223838fb8e64e02c0b27a4653f6002ed3c9c52ba84a1903c7e7`
- `RUN_SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.sh` — `a24eb7445068161518b1875b2925b90848b9548e4904b19eb1c4e6b2edec2d0a`
- `RUN_SIGMA_C5_NATIVE_INTERNET_INGRESS_PREFLIGHT_V2.sh` — `628e906a76cb94f6baba0987f532df42a36a32a744d3f04211653a019c7b5a53`
- `INSTALL_PREFLIGHT_START_SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.sh` — `e4f0ae2e46c44712363049804359c9943aa73af735219a77c5a83176e7473ed7`
- `SIGMA_C5_NATIVE_INTERNET_INGRESS_V2_README.md` — `dfcf61bb5b65396312fea0ce7301c0255a387ced4c8a372399d662a52ee56799`

Bundle SHA-256:

`SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.tgz` — `ab24f4bf996d7197869f1f60ea5359ff9a815bc4caaa14a640bf5b685706998e`

## Source/static evidence

Observed off-device:

- Python bridge compile: PASS
- Bash syntax for runner/preflight/installer: PASS
- host semantic-positive tokens (`HOST_QUERY_GENERATION=YES`, `HOST_WEB_RESULT_SELECTION=YES`, `HOST_URL_SELECTION=YES`, `HOST_KNOWLEDGE_PROMOTION=YES`): absent from active source
- instance manifest SHA/fingerprint self-check: PASS
- local content-addressed publish fixture: PASS
- repeated same bytes deduplicate to existing material: PASS
- exact-query cache preserves an existing file rather than overwriting it: PASS
- mechanical exact-file catalog admission fixture: PASS with `policy=LEARN`

## Claim boundary

`C5_INTERNET_INGRESS_V2_SOURCE_READY=YES`

`SAME_INSTANCE_FINGERPRINT_SOURCE_DEFINED=YES`

`SAME_INSTANCE_FINGERPRINT_SHA256=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125`

`LOCKED_SIGMAC_PREFLIGHT_ON_OPPO=NOT_RUN`

`LOCKED_VM_PREFLIGHT_ON_OPPO=NOT_RUN`

`LIVE_GENERAL_WEB_DISCOVERY_V2_ON_OPPO=NOT_RUN`

`V2_INTERNET_INGRESS_PROCESS_STARTED=NO`

`REAL_NATIVE_QUERY_TO_GENERAL_WEB_TO_INGRESS=NOT_YET_OBSERVED`

`REAL_INGRESS_MATERIAL_CONSUMPTION_BY_C5=NOT_YET_OBSERVED`

`C5_V3_RESTART_REQUIRED=NO`

`PRODUCTION_KNOWLEDGE_V2_BINDING_CHANGED=NO`
