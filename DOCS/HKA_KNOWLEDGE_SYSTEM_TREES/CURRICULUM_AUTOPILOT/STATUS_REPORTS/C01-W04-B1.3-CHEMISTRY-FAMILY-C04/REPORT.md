# Status Report — C01-W04-B1.3-CHEMISTRY-FAMILY-C04

Status: `PASS_CANDIDATE_REPAIRED` at `CURRICULUM` stage.

## Scope and counts
`B1.3-C04 — Phản ứng và cân bằng`: 8/8 canonical topics, 40 claims, 3 resolved/used sources, 32 learning objectives, 32/32 semantic closures, 18 cross-links and 8 sequence-intent records. Stable IDs and counts are preserved.

## Director-assistant repair
Independent audit found three small true-owner gaps. First, the curriculum used mol and molar mass before an explicit chemistry-facing amount-of-substance foundation; `N001-C005` now defines the mole and exact Avogadro constant before mole-ratio use, while `N002-C003` explicitly links stoichiometry to `m=nM` and foundational amount concentration `c=n/V`. Second, `N005-D1` explicitly required distinguishing equal rates from equal concentrations, but its supporting claim did not say so; `N005-C001` now closes that misconception directly. Third, `N006-D2` named pOH but its support only defined pH/Kw; `N006-C002` now explicitly supports pH, pOH, Kw and `pH+pOH=pKw` under consistent conditions.

No new IDs, objectives, closure rows or sources were created. Existing closure topology remains exactly one row per objective and is now `32/32 PASS_AFTER_REPAIR` semantically.

## Governance and boundaries
Canonical prerequisite alignment remains exactly `B1.3-C03@3ce2ef9679d821386bef92895a37ca379016fdf0` + `B1.2-C04@ac64a006c9aeeb2296f8da5d819df1246be64fb4`. C03 retains bonding/structure ownership; B1.2-C04 retains general thermodynamic/statistical-physics ownership. Locked C05-C10 scopes remain boundary-only; `FUTURE_LOCKED_SUPPORT=0`; `CROSS_SCOPE_ACADEMIC_MUTATION=0`; stage boundary remains CURRICULUM only.

## Provenance
Worker candidate: `1cc11fa77b7de2b89119f47fa646d80d2d7b82ca`.
Worker academic output: `993246223b30d8747d29ad16086bb751e7c23236`.
Effective academic repair: `889034adfe9707dd004d51123a63a714467ddab7`.
Director-assistant repair checkpoint: `4a486d71f8b00669f476ef45b4725e05daad3c8b`.

## Re-audit
PASS_AFTER_ASSISTANT_REPAIR: 8/8 topics; 40/40 claim integrity; 3/3 source resolution; 32/32 objectives; 32/32 semantic closure; exact prerequisite alignment; acyclic/no-dangling graph; duplicate/ownership controls; foundational progression; durable read-back; stage discipline. Red flag: none.

Director acceptance is not declared. `B1.3-C05` remains gated pending Director acceptance of repaired C04.
