# B1 ID and Record Standard

Window: `C01-W01-B1-ARCHITECTURE`  
Stage: `CURRICULUM`  
Canonical tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md@fc799bf1104ab6352710e1801777a971b5179995`  
Execution baseline: `02ff47d64fd3b3b03d1fa2ae70d773afb071995e`

## 1. Purpose and boundary

This standard makes Branch 1 curriculum authoring restartable and ID-stable. It governs curriculum records only. It does **not** create Lesson Registry records, prompts, assets, R2 objects, delivery mappings, or website metadata.

The canonical trace remains:

`NODE_ID -> CLAIM_ID -> SOURCE_ID -> PREREQUISITES -> DEPTH(D1-D4) -> LEARNING_OBJECTIVE -> FUTURE LESSON SLOT REFERENCE`

A future lesson-slot reference is only curriculum sequencing intent. It is not a `LESSON_ID`, does not constitute a Lesson Registry record, and cannot unlock a later pipeline stage.

Age/presentation pathways are metadata orthogonal to D1–D4. They may describe how a learning objective is presented, but they must never replace or redefine depth.

## 2. Immutable scope IDs

Architecture IDs are frozen by `B1_SCOPE_MAP.json`.

- Subbranch: `B1.1` … `B1.5`.
- Stable scope: `B1.x-Cnn`.
- Canonical topic leaf: `B1.x-Cnn-Tnn`.
- Bounded child window: the exact ID in `B1_AUTHORING_SEQUENCE.md`.

Once an accepted commit contains an ID, that ID must never be silently reused, renumbered, or reassigned. If canonical coverage later expands, append a new ID in the applicable namespace; do not insert by renumbering accepted records.

## 3. Curriculum record IDs

### NODE_ID

Format:

`HKA-B1-<subbranch>-<scope>-N<nnn>`

Example: `HKA-B1-1-C01-N001`.

Rules:

1. The `<subbranch>` digit is 1–5 and `<scope>` is the two-digit scope number from the stable scope ID.
2. `N<nnn>` is an append-only local ordinal inside that scope.
3. A committed `NODE_ID` is immutable even if the title changes.
4. A node must record the exact `canonical_topic_ids` it covers. A canonical topic may be represented by one or more nodes when depth or epistemic structure requires it, but its **primary authoring owner remains one child window**.
5. Two nodes must not carry the same claim/learning meaning merely under different scenery, wording, age pathway, or examples.

### CLAIM_ID

Format:

`<NODE_ID>-C<nnn>`

Example: `HKA-B1-1-C01-N001-C001`.

Rules:

- Claims are atomic enough to carry a certainty/epistemic label and sources.
- A claim ID is append-only inside its node.
- Revisions preserve the ID and update version history unless the proposition changes identity; a materially different proposition receives a new claim ID.
- A claim must declare one of: `ESTABLISHED_KNOWLEDGE`, `DEVELOPING_RESEARCH`, `ACADEMIC_DEBATE`, `PHILOSOPHICAL_DEBATE`, `HUMANISTIC_METAPHOR`.
- Certainty uses the canonical scale: `●`, `◐`, `△`, `◇`, `?`.

### SOURCE_ID

Preferred deterministic format:

`HKA-SRC-<12 lowercase hex characters>`

The suffix is the first 12 hexadecimal characters of SHA-256 over the normalized canonical locator:

`<source_type>|<persistent_locator>|<version_or_date>`

Examples of persistent locators include DOI, ISBN plus edition, stable institutional URL, standard identifier, dataset accession, or archival identifier.

Rules:

- The same normalized source must resolve to the same `SOURCE_ID` across Branch 1.
- Do not mint a new source ID merely because the source is cited by another node.
- Store bibliographic metadata separately from claim text.
- Where no persistent locator exists, use the most stable archival locator available and record the normalization basis.

### LEARNING_OBJECTIVE_ID

Format:

`<NODE_ID>-LO-D<1|2|3|4>-<nnn>`

Example: `HKA-B1-1-C01-N001-LO-D2-001`.

Rules:

- The D-depth is part of the ID because it changes the epistemic task, not merely presentation.
- Objectives must describe observable understanding/performance, not activity scenery.
- Different age/presentation pathways may point to the same objective when the learning meaning is unchanged.
- A genuinely different objective receives a distinct ID even when it uses the same topic label.

### Future Lesson Slot Reference

Format:

`LSREF-<NODE_ID>-D<1|2|3|4>-<nnn>`

Example: `LSREF-HKA-B1-1-C01-N001-D2-001`.

This is a **non-registry placeholder** for sequencing intent only.

Rules:

- It must never be named or treated as `LESSON_ID`.
- It carries no website route, slot, visual job, asset ID, or delivery metadata.
- It may be replaced/mapped only after global `ACADEMIC_LOCKED` and entry into `LESSON_REGISTRY`.
- Curriculum successors may record prerequisite intent between `LSREF` values but must not author a lesson record.

## 4. Minimum HKA knowledge-node record

Every authored node must contain at least the canonical minimum fields:

1. `node_id`
2. `canonical_name`
3. `central_question`
4. `root_phenomenon`
5. `definition`
6. `component_concepts`
7. `prerequisites`
8. `depths` with explicit `D1`, `D2`, `D3`, `D4`
9. `representations`
10. `knowledge_forming_methods`
11. `evidence`
12. `examples`
13. `counterexamples`
14. `common_misconceptions`
15. `errors_and_limits`
16. `relations_to_other_nodes`
17. `applications`
18. `academic_debates`
19. `certainty`
20. `hka_compass_relation`
21. `evidence_of_understanding`
22. `source_ids`
23. `version_history`
24. `external_curriculum_mappings`

Additional required traceability fields for this curriculum implementation:

- `canonical_topic_ids`
- `scope_id`
- `primary_authoring_owner`
- `claim_ids`
- `learning_objective_ids`
- `presentation_pathways`
- `duplicate_fingerprint`
- `secondary_cross_links`

`hka_compass_relation` must be `null` or a precise, academically defensible relation when no natural connection exists; do not force ethics into a technical claim.

## 5. D1–D4 contract

Depth is independent of age.

- **D1 — GẶP GỠ:** observation, experience, naming, recognizing examples.
- **D2 — KIẾN TẠO:** comparison, classification, measurement, explaining relations, initial models.
- **D3 — HÌNH THỨC HÓA:** standard definitions, notation, equations/structures, disciplinary methods, data/sources, systematic verification.
- **D4 — NGHIÊN CỨU & TỔNG HỢP:** critique assumptions, evaluate evidence, open problems, cross-domain synthesis, replication/checking, contribution to knowledge.

A node may have multiple objectives at a depth. A successor must not infer D1 = child, D4 = adult, or any equivalent age ladder.

## 6. Claim/source discipline

Each claim record must include:

```json
{
  "claim_id": "HKA-B1-1-C01-N001-C001",
  "node_id": "HKA-B1-1-C01-N001",
  "statement": "...",
  "epistemic_class": "ESTABLISHED_KNOWLEDGE",
  "certainty": "●",
  "source_ids": ["HKA-SRC-..."],
  "scope_limits": "...",
  "version": 1
}
```

Claims classified as developing, debated, hypothetical, unknown, philosophical, or metaphorical must not be worded as settled empirical fact.

## 7. Learning-objective record

Minimum curriculum objective record:

```json
{
  "learning_objective_id": "HKA-B1-1-C01-N001-LO-D2-001",
  "node_id": "HKA-B1-1-C01-N001",
  "depth": "D2",
  "objective": "...",
  "prerequisite_node_ids": [],
  "evidence_of_understanding": ["..."],
  "presentation_pathways": [],
  "future_lesson_slot_refs": [],
  "duplicate_fingerprint": {
    "node_meaning": "...",
    "claim_set": [],
    "learning_meaning": "...",
    "context": "..."
  }
}
```

No field in this record may contain visual/image-prompt authoring or website-placement metadata during `CURRICULUM`.

## 8. Versioning and crash recovery

Each record carries:

- `record_version` integer starting at 1;
- `created_in_window`;
- `created_at_commit` once accepted;
- `supersedes` only when identity changes;
- append-only `version_history`.

A replacement worker must read the last committed `RESULT.json` for its child. If status is `PASS`, it must not reauthor or renumber those records. If PASS is absent, it resumes unfinished scope using the existing accepted IDs.

## 9. Duplicate fingerprint

At `CURRICULUM`, compare semantic identity using:

`NODE MEANING + CLAIM SET + LEARNING OBJECTIVE + CONTEXT`

The canonical pipeline's future `VISUAL_JOB` component is intentionally `null` at this stage.

A different title, example, character, age pathway, language, scenery, or wording does not by itself create a new learning objective.

## 10. Acceptance checklist for a child record set

A child can return `PASS` only when:

- all assigned canonical topic IDs are accounted for;
- every node meets the minimum HKA node standard;
- every claim has epistemic class, certainty and source traceability;
- D1–D4 are explicit and not age-coded;
- prerequisites reference stable accepted IDs or stable scope prerequisites;
- no canonical topic has been transferred to another primary owner;
- semantic duplicate scan against all prior accepted B1 scopes has been run;
- all overlap-risk tags from `B1_DUPLICATE_CONTROL.md` are dispositioned;
- no later-stage artifact has been authored.
