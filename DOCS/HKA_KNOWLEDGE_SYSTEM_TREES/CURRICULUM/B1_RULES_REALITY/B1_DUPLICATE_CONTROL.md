# B1 Semantic Duplicate Control

Window: `C01-W01-B1-ARCHITECTURE`  
Stage: `CURRICULUM`  
Canonical tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md@fc799bf1104ab6352710e1801777a971b5179995`

## 1. Decision rule

Duplicate detection is semantic, not lexical. At this stage the minimum comparison is:

`NODE MEANING + CLAIM SET + LEARNING OBJECTIVE + CONTEXT`

The canonical future `VISUAL_JOB` term is `null` during `CURRICULUM`; it must not be authored here.

A different title, example, scenery, character, language, age pathway, activity wrapper, or wording does not make the same learning objective unique.

Repeated names are legitimate only when the epistemic role, claim boundary, objective, or disciplinary context is materially different. In that case retain one primary owner for each canonical topic and create typed secondary cross-links.

## 2. Dispositions

- `DUPLICATE_MERGE_OR_REFERENCE`: same learning meaning; do not author a second independent objective. Reuse/reference the accepted node or claim.
- `CROSS_LINK_NOT_DUPLICATE`: same term/object appears with a distinct epistemic role; author within the primary scope and link explicitly.
- `OVERLAP_REVIEW`: scopes are adjacent enough that claim/objective boundaries must be checked before PASS.
- `SECONDARY_CROSS_LINK`: mandatory cross-domain/shared-node participation; no primary ownership transfer.
- `DISTINCT`: semantic scan found no material overlap.

## 3. Mandatory comparison procedure

For every proposed node/objective, the child must:

1. Normalize canonical topic IDs, terminology and synonyms without erasing disciplinary meaning.
2. Compare against its own child records, all prior accepted B1 child records, and the risk register below.
3. Compare central phenomenon, claim proposition, prerequisite role, D-depth task, evidence-of-understanding and context.
4. If meaning is the same, reference/extend the existing record rather than creating a second independent objective.
5. If meaning differs, record the difference and a typed cross-link.
6. Preserve the primary owner from `B1_SCOPE_MAP.json`; a cross-link never changes ownership.
7. Record the disposition in `CROSS_LINKS.jsonl` and summarize counts in child `RESULT.json`.

## 4. Architecture risk register

| Risk | Type | Affected stable IDs | Required disposition | Control |
|---|---|---|---|---|
| `R01` | same-label-distinct-epistemic-role | `B1.2-C04-T03`, `B1.5-C01-T02` | `CROSS_LINK_NOT_DUPLICATE` | Physics owns thermodynamic/statistical-mechanical entropy claims; information/computation owns Shannon/information entropy claims. Shared mathematics is cross-linked, not duplicated. |
| `R02` | same-label-overlapping-formal-object | `B1.1-C08-T07`, `B1.5-C01-T05` | `CROSS_LINK_NOT_DUPLICATE` | B1.1 owns combinatorial/algebraic structure and proof-oriented claims; B1.5 owns coding-channel reliability/information-system claims. Do not restate identical objectives. |
| `R03` | same-label-abstraction-vs-phenomenon | `B1.1-C06-T05`, `B1.2-C02-T06` | `CROSS_LINK_NOT_DUPLICATE` | B1.1 owns formal dynamical-system treatment; B1.2 owns physical oscillation phenomenon and measurement. Shared equations may be reused by reference. |
| `R04` | formal-foundation-vs-computation | `B1.1-C01`, `B1.5-C02`, `B1.5-C04` | `OVERLAP_REVIEW` | B1.1 owns mathematical logic, axioms, proof/model-theoretic claims; B1.5 owns computability/formal-language/program-verification claims. Explicit prerequisites and cross-links required. |
| `R05` | mathematics-vs-algorithms | `B1.1-C08`, `B1.5-C03` | `OVERLAP_REVIEW` | B1.1 owns graph/combinatorial structures and proofs; B1.5 owns algorithmic operations, complexity and data-structure use. |
| `R06` | mathematics-vs-data-ai | `B1.1-C07`, `B1.1-C10`, `B1.5-C07`, `B1.5-C10` | `OVERLAP_REVIEW` | Mathematical/statistical foundations stay in B1.1; B1.5 owns computational pipelines and machine-learning objectives. Reuse prerequisites; do not reteach foundations unchanged. |
| `R07` | physics-vs-chemistry | `B1.2-C07`, `B1.2-C08`, `B1.3-C01`, `B1.3-C03`, `B1.3-C07` | `OVERLAP_REVIEW` | Physics owns physical theory/measurement foundations; chemistry owns chemical structure, bonding, reactivity and quantum-chemical application. |
| `R08` | physics-vs-chemistry | `B1.2-C04`, `B1.3-C04`, `B1.3-C07` | `OVERLAP_REVIEW` | Physics owns general thermodynamic/statistical principles; chemistry owns chemical thermodynamics, reaction equilibrium and chemical kinetics. |
| `R09` | physics-vs-chemistry-materials | `B1.2-C09`, `B1.3-C09` | `OVERLAP_REVIEW` | B1.2 owns physical properties/phases/electronic and quantum behavior; B1.3 owns composition, synthesis, chemistry and material classes. |
| `R10` | physics-vs-earth-space | `B1.2-C02`, `B1.2-C11`, `B1.2-C12`, `B1.4-C03`, `B1.4-C10`, `B1.4-C17`, `B1.4-C21`, `B1.4-C22` | `OVERLAP_REVIEW` | B1.2 owns transferable physical laws/methods; B1.4 owns Earth/planetary/astronomical systems, observations and histories. |
| `R11` | chemistry-vs-earth-system | `B1.3-C10`, `B1.4-C01`, `B1.4-C07`, `B1.4-C08`, `B1.4-C10`, `B1.4-C12`, `B1.4-C14` | `OVERLAP_REVIEW` | B1.3 owns chemical composition/reaction/pollutant/process claims; B1.4 owns coupled Earth-system reservoirs, flows, hazards and environmental geology. |
| `R12` | cross-tree-mandatory-node | `B1.2-C12`, `B1.3-C10`, `B1.4-C09`, `B1.4-C10`, `B1.4-C11`, `B1.4-C12`, `B1.4-C13`, `B1.5-C07` | `SECONDARY_CROSS_LINK` | Keep B1 disciplinary claims in their primary scopes; the mandatory cross-domain climate node aggregates links across branches without stealing primary ownership. |
| `R13` | cross-tree-mandatory-node | `B1.1-C03`, `B1.1-C07`, `B1.1-C10`, `B1.5-C03`, `B1.5-C07`, `B1.5-C10`, `B1.5-C11` | `SECONDARY_CROSS_LINK` | AI is a mandatory cross-domain node. B1.5-C10 remains primary for AI computation; mathematical, data, HCI and other branches are explicit secondary dependencies/links. |
| `R14` | cross-tree-mandatory-node | `B1.3-C08`, `B1.3-C10`, `B1.4-C07`, `B1.4-C08`, `B1.5-C07` | `SECONDARY_CROSS_LINK` | Chemical, Earth/water/soil and data claims remain in B1 scopes; health, biology, policy, culture and food-system synthesis belongs to cross-tree linking. |
| `R15` | cross-tree-boundary | `B1.5-C09`, `B1.5-C10`, `B1.5-C11` | `SECONDARY_CROSS_LINK` | B1.5 owns technical mechanisms and system evaluation; legal, ethical, political, philosophical and mind-science claims remain with their canonical branches and are cross-linked. |

## 5. Exact-label audit

Across all 348 canonical B1 topic leaves, exactly three labels repeat verbatim:

- `Dao động` — `B1.1-C06-T05` and `B1.2-C02-T06`.
- `Mã sửa lỗi` — `B1.1-C08-T07` and `B1.5-C01-T05`.
- `Entropy` — `B1.2-C04-T03` and `B1.5-C01-T02`.

All three have explicit non-silent dispositions (`R01`–`R03`). Therefore lexical duplicates do not create duplicate primary ownership.

## 6. Mandatory cross-domain nodes

The canonical tree requires eight shared nodes: climate change, artificial intelligence, global health, food, cities, consciousness, justice, and peace. They are graph intersections, not permission to duplicate disciplinary content.

For Branch 1:

- B1 authors only the mathematical/physical/chemical/Earth/information claims assigned to B1 scopes.
- Biology, medicine, cognition, language, design, history, law, ethics, politics, culture and other non-B1 claims stay with their canonical branches.
- Cross-domain syntheses cite/link B1 claims instead of copying them into a second B1 owner.
- HKA Compass relations must be academically natural; ethics/values must not be injected into a technical claim merely to satisfy a template.

## 7. Claim-boundary examples

### Entropy

`B1.2-C04` owns thermodynamic/statistical-mechanical entropy in physical systems. `B1.5-C01` owns information entropy in information theory. Shared mathematics is linked; neither scope may silently teach the other's disciplinary claim as its own.

### Error-correcting codes

`B1.1-C08` owns combinatorial/algebraic structures, proofs and formal properties. `B1.5-C01` owns coding for information transmission/reliability. If an objective is literally identical, keep one learning objective and reference it; do not duplicate for scenery.

### Oscillation

`B1.1-C06` owns formal dynamical-system abstraction. `B1.2-C02` owns physical oscillation, measurable variables and mechanics. Shared equations are prerequisites/cross-links, not duplicated objectives by default.

### Quantum / atomic / molecular content

`B1.2-C07/C08` owns physical theory, states, measurement and AMO phenomena. `B1.3-C01/C03/C07` owns chemical structure, bonding, reactivity and quantum-chemical application. Successors must mark where a physics claim is merely prerequisite to a chemistry objective.

### AI

`B1.5-C10` is the primary B1 AI computation scope. Mathematical probability/optimization, data, algorithms and HCI remain their own primary scopes and are prerequisites/cross-links. The mandatory AI cross-domain node also links to non-B1 cognition, language, labor, law, ethics, politics, media and futures without moving those topics into B1.

## 8. Fingerprint fields

Each authored learning objective must carry a duplicate fingerprint with at least:

```json
{
  "canonical_topic_ids": ["..."],
  "node_meaning": "...",
  "claim_ids": ["..."],
  "learning_meaning": "...",
  "depth": "D1|D2|D3|D4",
  "context": "...",
  "epistemic_role": "...",
  "presentation_pathway": "non-identity metadata"
}
```

Age/presentation is explicitly non-identity metadata. Changing it does not by itself authorize a new objective.

## 9. Architecture audit result

- Canonical topic leaves scanned: **348**.
- Exact repeated labels: **3**.
- Semantic/cross-domain risk cases registered: **15**.
- Primary-owner collisions: **0**.
- Orphan topics: **0**.
- Uncontrolled duplicate risk at architecture level: **0**; all identified risks have a required disposition path.

Successor child and integration windows must repeat semantic scanning against the actual authored claims/objectives. This architecture PASS does not pre-approve future content.
