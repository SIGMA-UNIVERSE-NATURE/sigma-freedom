# SIGMA ONE-TO-ONE BRAIN TRAINING BRIDGE — CUA 3 CANDIDATE

Status: ISOLATED_CANDIDATE_ONLY
Branch: cua3-brain-training-bridge

Purpose: prepare a 10-minute lesson/answer/evaluation loop that activates only after canonical M0 completion (`NOT_AUDITED == 0` and final machine/canonical receipt gap reconciled).

Loop:
1. Canonical trainer publishes exactly one bounded lesson request.
2. HP Sigma executor auto-discovers the authorized lesson request.
3. Sigma produces answer + evidence + uncertainty + failure notes.
4. Machine receipt is persisted.
5. Trainer evaluates against the locked baseline/metric.
6. Decision is HOLD/REVISE/REJECT/PROMOTE only under the active training contract.
7. Next lesson may be issued no sooner than 600 seconds after the prior cycle and only after receipt/evaluation closure.

Hard guards:
- Never run concurrently with M0 bounded automeasure.
- No arbitrary shell.
- No paid API.
- No website action.
- No DNA/core mutation by the bridge itself.
- No self-promotion.
- One pending lesson at a time.
- Machine receipt required before advance.
- Independent evaluation when required by canonical contract.
- A lesson response is not an intelligence improvement claim.
- Promotion requires differential evidence against the previous verified baseline plus regression checks.

Activation gate:
`M0_COMPLETE_AND_RECONCILED == true`

Until that gate is verified, this file is design-only and MUST NOT be consumed by the HP executor.
