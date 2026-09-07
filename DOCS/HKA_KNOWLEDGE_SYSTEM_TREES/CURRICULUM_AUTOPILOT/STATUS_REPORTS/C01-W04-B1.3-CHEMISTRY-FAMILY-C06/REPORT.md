# Status Report — C01-W04-B1.3-CHEMISTRY-FAMILY-C06

Status: `PASS_CANDIDATE_REPAIRED` at `CURRICULUM` stage.

## Scope and gate
Canonical scope is `B1.3-C06 — Hóa hữu cơ`, with 7/7 topics: Cấu trúc carbon; Nhóm chức; Cơ chế phản ứng; Hóa lập thể; Tổng hợp hữu cơ; Hóa dược; Hóa học polymer. Canonical prerequisites remain exactly accepted `B1.3-C03@3ce2ef9679d821386bef92895a37ca379016fdf0` plus `B1.3-C04@caa12019682e1a9274fe75b8ab20435c3bfb4d2e`.

## Worker candidate
Worker candidate: `6393b177f10daa0e25ae6efe19ed8e68a4ca5f91`. Worker academic output: `24154febbcdefc7ea69777d0aa01f405651961e8`. Worker self-repair count: 1, repairing the N004-D2 E/Z closure support.

## Director-assistant findings and repairs
Independent semantic audit found that several objectives were structurally closed but stronger than their supporting Claim text. Repairs preserved all stable IDs and counts.

1. Organic foundations: made introductory hybridization/geometry/rotation support explicit; made functional-group polarity/intermolecular/acid–base/reactivity reasoning explicit; defined leaving-group vocabulary.
2. Stereochemistry: explicitly distinguished constitutional isomers from stereoisomers; added chiral-environment consequences, stereoselective outcome meaning and racemic/non-racemic enantiomeric composition.
3. Synthesis and medicinal chemistry: made forward-route vocabulary, regio/stereoselectivity, compatibility/step economy, lipophilicity/metabolic-stability/synthetic-accessibility trade-offs explicit.
4. Polymer chemistry: made monomer and linear/branched/network architecture explicit; added copolymer/control concepts and qualified recyclability/degradation claims. N002-D2 closure was versioned once to include the direct nomenclature Claim C005.

Claims repair commit: `ee2f101f9f34d1642afd49c73f20e7deccdbafb5`. Effective academic repair commit: `ce01a8c272a098063c1bb12a0d01287549cd783f`. Assistant checkpoint: `8b3ae280a139b4fe5a8af9348485692a1308ffa2`.

## Re-audit
PASS_AFTER_ASSISTANT_REPAIR: 7/7 topic coverage; 35/35 Claim integrity; 5/5 source resolution; 28/28 learning objectives; 28/28 exactly-one-row and semantically complete closure; supporting-Claim resolution; exact C03+C04 prerequisite alignment; acyclic/no-dangling prerequisite graph; semantic duplicate and ownership scans; foundational progression; `FUTURE_LOCKED_SUPPORT=0`; `CROSS_SCOPE_ACADEMIC_MUTATION=0`; CURRICULUM-only stage boundary.

No academic output outside C06 was changed. No control-plane file was changed. C07-C10 remain locked boundary-only and provide zero supporting Claim IDs.

## Decision state
Director acceptance is not declared by this audit. `B1.3-C07` remains `GATED_PENDING_DIRECTOR_ACCEPTANCE`.

## Next action
Director reviews/accepts the repaired C06 candidate. Only after formal acceptance may canonical B1.3-C07 be opened.
