# Current Chat Handoff — C5 Internet Ingress V2 Oppo Gate

Date: 2026-09-06
Branch: `SIGMA_LIFE`

## Authority / current frontier
This handoff supersedes the older V4-A/V4-B3 discussion in the originating chat. Work advanced while that chat was stalled. The current frontier is C5 V3 + Native Internet Ingress V2.

Authoritative source-ready checkpoint:
- commit `c8da510745f7229fada825354194cc88e8b2a237`
- bundle `SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.tgz`
- bundle SHA256 `ab24f4bf996d7197869f1f60ea5359ff9a815bc4caaa14a640bf5b685706998e`

## Stable SIGMA instance identity
`SIGMA_INSTANCE_FINGERPRINT_SHA256=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125`

Identity record binds:
- `SIGMA_INSTANCE_ROOT=/data/data/com.termux/files/home/SIGMA/sigma_genesis1`
- `SIGMA_STATE_LINEAGE=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2`
- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- `NATIVE_COGNITIVE_CORE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace`

## Architecture now
One SIGMA instance, two lanes, same fingerprint/state lineage:
1. C5 V3 learning lane: sole cognitive-state writer.
2. Internet Ingress V2 lane: native query/candidate selection plus mechanical network transport; no cognitive-state writes.

Required boundaries:
- `C5_V3_COGNITIVE_WRITER_COUNT=1`
- `HOST_QUERY_GENERATION=NO`
- `HOST_WEB_RESULT_SELECTION=NO`
- `HOST_KNOWLEDGE_PROMOTION=NO`
- `INTERNET_MATERIAL_CONTENT_ADDRESSED=YES`
- `GLOBAL_QUERY_LIMIT=NONE`
- `GLOBAL_FETCH_LIMIT=NONE`
- per-fetch byte/time/redirect and public-address safety bounds remain.

## Current claim boundary
Source/static evidence exists, but Oppo runtime admission has NOT yet been reported in this chat.

Therefore keep:
- `C5_NATIVE_INTERNET_INGRESS_V2_SOURCE_READY=YES`
- `C5_NATIVE_INTERNET_INGRESS_V2_OPPO_PREFLIGHT=NOT_RUN_OR_NOT_YET_REPORTED`
- `SAME_INSTANCE_FINGERPRINT_BINDING_ON_RUNNING_OPPO=NOT_YET_PROVEN`
- `INTERNET_INGRESS_PROCESS_STARTED=NOT_YET_PROVEN`
- `REAL_NATIVE_QUERY_TO_WEB_TO_INGRESS_TO_C5_CONSUMPTION=NOT_YET_PROVEN`
- `C5_V3_RESTART_REQUIRED=NO`
- `PRODUCTION_KNOWLEDGE_V2_BINDING=NO`

Do NOT claim Internet learning merely because fetch/ingress starts.

## Immediate next action
On Oppo, locate the exact bundle and verify SHA256 `ab24f4bf996d7197869f1f60ea5359ff9a815bc4caaa14a640bf5b685706998e`, then run `INSTALL_PREFLIGHT_START_SIGMA_C5_NATIVE_INTERNET_INGRESS_V2.sh` through the supplied installer flow.

Expected admission evidence includes:
- fingerprint `fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125`
- `C5_NATIVE_INTERNET_INGRESS_PREFLIGHT_V2=PASS`
- C5 V3 main PID unchanged (reported baseline in handoff: PID 20026; verify live rather than assume)
- `SIGMA_C5_NATIVE_INTERNET_INGRESS_V2_STARTED=YES`
- a distinct ingress PID
- `C5_V3_RESTARTED=NO`
- installer RC 0

After process admission, require the real end-to-end chain before stronger claim:
`native SIGMA query -> native candidate selection -> real HTTPS fetch -> SHA-addressed ingress material -> incremental catalog sees material -> C5 V3 selects/processes it -> evidence/knowledge state changes`.

## Cross-window instructions
Any new teaching/work window must read this handoff and the source-ready checkpoint before acting. Do not revert to V4-A/V4-B3 as the current frontier unless explicitly investigating historical evidence. Do not introduce host semantic selection or a second cognitive writer. Preserve same-instance fingerprint binding.