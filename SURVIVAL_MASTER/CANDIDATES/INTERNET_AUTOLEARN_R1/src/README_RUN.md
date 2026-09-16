# README_RUN — REVIEW/PREFLIGHT ONLY

**Do not install or run this candidate on Oppo until Survival Master records `APPROVE_FOR_OPPO_PREFLIGHT_ONLY` for the exact reviewed candidate.** Static review cannot authorize production.

This package is intentionally fail-closed where exact native dependency bytes are unavailable. No host fallback exists.

## Static/local verification

From the extracted source tree on a non-production review machine:

```bash
bash verify/manifest_verify.sh
bash verify/static_audit.sh
python3 -m unittest discover -s ../tests -p 'test_*.py'
bash verify/recovery_idempotency_verify.sh
```

These commands are candidate-quality checks only. They are not locked-SIGMAC/VM admission and do not exercise real Internet or production.

## Future Oppo preflight, only after review approval

The provided `control/start_preflight.sh` checks Session R4 policy, locked toolchain identity, manifest integrity and exact native dependency resolution. It refuses to continue if any canonical-mutation permission is present or if required exact native bytes/interfaces remain unresolved.

The candidate does not contain an automatic production installer. `control/stop.sh` stops only the candidate's own artifact-lane supervisor through its recorded PID/lock state; it does not alter canonical writer locks or model state.

## Resource defaults

```text
MAX_SINGLE_RESPONSE_BYTES=8388608
MAX_TOTAL_BYTES_PER_CYCLE=67108864
MAX_REQUESTS_PER_CYCLE=32
MAX_REDIRECTS=5
CONNECT_TIMEOUT=10
TRANSFER_TIMEOUT=30
PER_DOMAIN_BACKOFF=2
GLOBAL_BACKOFF=1
MAX_INFLIGHT_REQUESTS=1
DISK_HIGH_WATER_MARK_PERCENT=85
LOG_RETENTION_BOUND=64
CHECKPOINT_RETENTION_BOUND=16
```

A bound returns a mechanical observation. It must not choose a replacement query/site/resource or convert UNKNOWN into a semantic decision.
