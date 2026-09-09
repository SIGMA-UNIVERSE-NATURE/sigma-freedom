# HKA Curriculum Autopilot v1

Status: `ACTIVE_GUARDED`

HKA Autopilot automates **routing and governance state detection**, not authority collapse. GitHub durable state remains the source of truth.

## Control loop

`VALIDATE → PLAN → DISPATCH ROLE → DURABLE WRITE → VALIDATE AGAIN`

The planner inspects `HKA_CURRICULUM_STATE.json`, `WINDOW_REGISTRY.json`, Director status, continuity snapshot, foundational gate, and when needed the active worker branch durable `STATUS.json`.

Role routing:

- `READY` → Worker.
- worker durable `PASS_CANDIDATE` → Director independent review.
- `REPAIR_REQUIRED` → same Worker repair loop.
- Director accepted / Sentinel pending → Backup Sentinel.
- accepted + fresh Sentinel aligned → next child becomes Director-opening request.
- no remaining children → family integration/exit request.

## Runtime

Primary engine: `.github/hka_autopilot/hka_autopilot.py`

Commands:

```bash
python .github/hka_autopilot/hka_autopilot.py validate
python .github/hka_autopilot/hka_autopilot.py plan
python .github/hka_autopilot/hka_autopilot.py dispatch --request /tmp/hka-request.json
```

A GitHub Actions launcher polls the control plane every 15 minutes and can also be triggered manually. If `HKA_AGENT_WEBHOOK_URL` is configured, run requests are POSTed to that runner. Otherwise an idempotent GitHub issue is created so the request is durable and visible rather than silently lost.

## Safety

Autopilot does not grant Worker self-acceptance, does not let Sentinel unlock successors, does not mutate accepted academic artifacts, and does not cross the `CURRICULUM` stage boundary. A failed invariant halts dispatch.
