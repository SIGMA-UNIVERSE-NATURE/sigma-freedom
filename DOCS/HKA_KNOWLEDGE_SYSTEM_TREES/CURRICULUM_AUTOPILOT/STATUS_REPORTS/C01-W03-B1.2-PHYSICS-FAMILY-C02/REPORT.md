# Status Report — C01-W03-B1.2-PHYSICS-FAMILY-C02

Status: `PASS_CANDIDATE_REPAIRED` for the targeted foundational mass-vs-weight repair at the true owner `B1.2-C02 — Cơ học cổ điển`.

Accepted baseline: `2c112f281ca8915ef2e8800043db952c550531bc`. Effective academic repair SHA: `efc85c8278da087063e94c6e940719514e389f18`. Final read-back checkpoint: `CP05-MASS-WEIGHT-FINAL-READBACK-PASS` at `1a52b2edf027bae17e23b500d4c91ffa805fdc20`.

The repair versioned existing stable N002 records in place. It explicitly distinguishes Newtonian mass (inertial scalar, kg, not force) from gravitational weight (force, N, local-field dependent), states the local approximately-uniform-field model `W = m g` with its domain, explains that changing location/local `g` changes weight rather than Newtonian mass, distinguishes balance-based mass measurement from force/spring-scale readings, and separates apparent weight from gravitational weight.

Counts remain 8/8 canonical topics, 64 claims, 32 learning objectives, and 32/32 Claim→Learning-Objective semantic closures. Existing IDs were preserved; no C01 or C03-C12 academic output was modified.

Self-audit found two repair issues and both were repaired: the original gravity wording did not explicitly close mass-vs-weight meaning/unit/location semantics; and the first measurement framing needed a clean separation between gravitational weight, force-scale reading and apparent weight. Re-audit: PASS.

Final GitHub read-back verified the repaired N002 claims, all four repaired N002 D1-D4 objectives, their four closure rows, and `RESULT.json`. Durable read-back: PASS.

Audits: foundational mass-vs-weight PASS; canonical prerequisite alignment PASS (`C01 + B1.1-C03 + B1.1-C04`); prerequisite graph PASS (acyclic, no dangling IDs); ownership/semantic duplicate PASS; `FUTURE_LOCKED_SUPPORT=0`; stage boundary PASS — CURRICULUM ONLY.

B1.2 family completion remains gated for Director reconciliation of the repaired C02 effective SHA. B1.3 is not unlocked.
