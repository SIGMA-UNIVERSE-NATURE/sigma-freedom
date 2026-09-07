# HANDOFF — B1.2 External General-Education Mapping

## Outcome
External general-education mapping for `C01-W03-B1.2-PHYSICS-FAMILY` is `PASS_CANDIDATE_REPAIRED` at `CURRICULUM` stage. Worker candidate: `3597acc2d14d6cfb45e2bfa923b7396a519b19a3`.

## Benchmark set
Six official school/general-education systems across six continents were resolved: US NGSS, England National Curriculum Science, Australian Curriculum Science, Singapore MOE Science/Physics, South Africa CAPS Physical Sciences, and Brazil BNCC Ciências da Natureza. University-only baseline: false.

## Coverage
Ten high-confidence foundational requirements were mapped. Results: FULL 9, PARTIAL 0, GAP 0, NOT_OWNER 1. `FOUNDATIONAL_GAP_COUNT=0`.

The common spine is closed across measurement/experimental reasoning; mechanics including mass-versus-weight; matter/particle physical meaning; thermal physics; waves/sound/light; electricity/magnetism; atomic/nuclear/radiation; model/evidence reasoning; and applied device/sensor physics.

`PHY-GE-10` remains `NOT_OWNER`, but canonical ownership wording was repaired: Earth/space domain conclusions map to B1.4; biological/medical domain conclusions remain outside B1.2 and this B1-only audit does not invent a non-canonical B1.5 owner for them. B1.2 retains only transferable physical principles.

## C02 mass-versus-weight
PASS at true owner C02 using effective academic repair `efc85c8278da087063e94c6e940719514e389f18`. Mass is distinguished from weight in meaning and units, `W=m g` is conditional on the local approximately uniform-field model, location dependence is explicit, measurement language distinguishes balances from force scales, and apparent weight is separated from gravitational weight.

## Repairs
Worker self-repair `MAP-SR01` correctly prevented integrated Earth/space and health contexts from becoming B1.2-owned domain conclusions.

Director-assistant repair `DA-MAP-SR01` corrected an over-broad owner label that listed B1.3/B1.4/B1.5 as possible owners for Earth/space, biological and medical conclusions. Canonical B1 assigns B1.3 to chemistry, B1.4 to Earth/Universe and B1.5 to Information/Computation; therefore only B1.4 is asserted here for Earth/space, while the exact non-B1 biological/medical owner is intentionally left unasserted. No C01-C12 academic output was edited.

## Integrity gates
Ownership PASS_AFTER_ASSISTANT_METADATA_REPAIR; support resolution PASS; FUTURE_LOCKED_SUPPORT=0; CROSS_SCOPE_ACADEMIC_MUTATION=0; CURRICULUM-only stage boundary PASS. B1.3 remains locked.

## Next gate
Director review/acceptance of the repaired mapping candidate, then fresh `DIRECTOR-BACKUP-S01` `TREE_ALIGNMENT_PASS`. This handoff does not unlock B1.3.
