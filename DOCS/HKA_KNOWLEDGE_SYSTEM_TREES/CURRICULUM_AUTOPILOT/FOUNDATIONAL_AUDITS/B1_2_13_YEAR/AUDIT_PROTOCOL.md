# B1.2 External General-Education Physics Mapping Protocol

Status: `PASS_CANDIDATE`
Stage: `CURRICULUM`
Window: `C01-W03-B1.2-PHYSICS-FAMILY`
Phase: `EXTERNAL_GENERAL_EDUCATION_MAPPING`

## Purpose
Verify that the Director-accepted B1.2 physics family preserves a coherent general-education physical-science spine and that advanced material extends rather than displaces foundational learning.

## Benchmark rule
Use official school/general-education progressions, not university-only curricula. Benchmark systems span six continents and are treated as comparative evidence rather than universal truth:
- North America — Next Generation Science Standards (US), K-12 physical science progression.
- Europe — England National Curriculum Science, Key Stages 1-4.
- Oceania — Australian Curriculum Science, Foundation-Year 10.
- Asia — Singapore MOE Lower Secondary Science and Upper Secondary Physics.
- Africa — South Africa CAPS Physical Sciences, with school science progression context.
- South America — Brazil BNCC Ciências da Natureza, Ensino Fundamental and Ensino Médio progression.

A requirement is high-confidence when it recurs across multiple systems and/or is structurally necessary for later school physics learning.

## Required mapping dimensions
1. observation, measurement, units, uncertainty and experimental reasoning;
2. motion, forces, mass versus weight, energy, momentum and mechanics;
3. matter states and particle-model physical meaning at the physics boundary;
4. temperature, heat, energy transfer and basic thermodynamics;
5. waves, sound, light and optics;
6. charge, current, circuits, magnetism and electromagnetic phenomena;
7. atomic, nuclear and radiation foundations;
8. scientific inquiry/model use, evidence and limitations;
9. applied energy/devices/sensors where B1.2 owns the physical principle;
10. Earth/space, biological and medical domain conclusions only as `NOT_OWNER` when another HKA subbranch owns the domain conclusion.

## Coverage statuses
- `FULL`: effective accepted B1.2 evidence covers the foundational meaning.
- `PARTIAL`: related content exists but an essential meaning is absent.
- `GAP`: required foundational meaning is absent from B1.2 and belongs to B1.2.
- `NOT_OWNER`: the domain conclusion belongs elsewhere; only the underlying physical principle may be mapped in B1.2.

## Ownership and mutation rules
- C01-C12 academic outputs are immutable during this phase.
- C02 is evaluated using repaired effective academic SHA `efc85c8278da087063e94c6e940719514e389f18`.
- Mass versus weight must remain explicit at C02 true owner.
- Future B1.3/B1.4/B1.5 domain curricula are not support sources.
- `FUTURE_LOCKED_SUPPORT=0` and `CROSS_SCOPE_ACADEMIC_MUTATION=0` are mandatory.

## Exit gate
PASS requires: >=5 continents, all official source locators resolved, university-only baseline=false, every high-confidence requirement disposed, `FOUNDATIONAL_GAP_COUNT=0`, mass-vs-weight PASS, ownership PASS, CURRICULUM-only boundary, durable GitHub read-back PASS. A true child academic defect produces BLOCK with exact owner scope rather than controller patching.
