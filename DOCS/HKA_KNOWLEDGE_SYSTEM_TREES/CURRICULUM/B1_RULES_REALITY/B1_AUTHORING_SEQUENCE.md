# B1 Authoring Sequence and Restartable Child-Window Partition

Window: `C01-W01-B1-ARCHITECTURE`  
Stage: `CURRICULUM` only  
Canonical tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md@fc799bf1104ab6352710e1801777a971b5179995`  
Execution baseline: `02ff47d64fd3b3b03d1fa2ae70d773afb071995e`

## 1. Deterministic predecessor pin

Git commits cannot contain their own future SHA. Therefore every successor resolves this architecture's accepted input by an immutable deterministic selector, then pins the resulting SHA before authoring:

1. Read first-parent history of `hka-tree/c01-w01-b1-architecture` after baseline `02ff47d64fd3b3b03d1fa2ae70d773afb071995e`.
2. Select the earliest commit that contains `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/RESULT.json` with `window_id=C01-W01-B1-ARCHITECTURE`, `stage=CURRICULUM`, `status=PASS`, all seven contract output paths present, and the mandatory status folder containing `STATUS.json`, `REPORT.md`, and at least one checkpoint.
3. Record that exact SHA as `input_commit_sha` in the family/child checkpoint before any authoring.
4. Reject a floating branch-only input. If zero or multiple commits satisfy the selector due to history rewriting, return `BLOCKED_CONTRADICTION`.

Every child also reads the canonical tree only at `fc799bf1104ab6352710e1801777a971b5179995`. This gives each child an exact immutable knowledge input and an exact immutable predecessor architecture commit.

## 2. Family-controller rule

The registered family windows `C01-W02` through `C01-W06` are controllers, not single-chat authoring jobs. A family controller must execute/checkpoint the bounded children below and write a family aggregate `RESULT.json`; it must never author the entire large discipline in one disposable window.

Within each family:

- only one child scope is active per child checkpoint;
- each child owns stable scope IDs listed here;
- each child writes its own `RESULT.json` and `HANDOFF.md` under its exact output path;
- each child and each family controller maintains the mandatory durable status folder `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/<WINDOW_ID>/`;
- a failed/interrupted child resumes only its unfinished assigned scope;
- accepted IDs from PASS children are immutable;
- the next child may start only after the current child's `PASS`;
- the family aggregate may return `PASS` only after all its children are `PASS`.

## 3. Required child curriculum outputs

Each bounded child writes under its listed directory:

- `NODES.jsonl` — HKA node records satisfying `B1_ID_AND_RECORD_STANDARD.md`;
- `CLAIMS.jsonl` — atomic claims with certainty/epistemic class and source IDs;
- `SOURCES.jsonl` — normalized source records;
- `LEARNING_OBJECTIVES.jsonl` — D1–D4 objectives and evidence of understanding;
- `CROSS_LINKS.jsonl` — secondary links and duplicate dispositions;
- `CURRICULUM_SEQUENCE_INTENT.jsonl` — prerequisite/future lesson-slot references only, not Lesson Registry records;
- `RESULT.json`;
- `HANDOFF.md`.

No child may create Lesson Registry, prompt, image, R2, delivery, or website artifacts.

### Mandatory child/controller status path

For every child or family controller, the status path is deterministic from its exact window ID:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/<WINDOW_ID>/`

It must contain `STATUS.json`, `REPORT.md`, and append-only `CHECKPOINTS/<CHECKPOINT_ID>.json` records conforming to `STATUS_REPORT_STANDARD.md`. A child or controller `RESULT.json=PASS` is invalid unless its status folder is current and also says `PASS`. The status folder is control-plane state; it does not change curriculum ownership or create a later-stage artifact.

## 4. Prerequisite-aware family execution order

Authoring order is deterministic for cumulative prerequisite and semantic-duplicate checking:

1. `C01-W02-B1.1-MATH-FAMILY`
2. `C01-W03-B1.2-PHYSICS-FAMILY`
3. `C01-W04-B1.3-CHEMISTRY-FAMILY`
4. `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY`
5. `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY`
6. `C01-W07-B1-INTEGRATION-LOCK` performs B1 integration/coverage/prerequisite/semantic-duplicate audit after all five families pass.

This is an authoring order; it does not change the canonical `WINDOW_REGISTRY.json` dependency declarations.

## 5. Bounded child windows

| Order | Child window ID | Stable scope IDs | Canonical topic count | Required prior scope PASS | Output directory |
|---:|---|---|---:|---|---|
| 1 | `C01-W02-B1.1-MATH-FAMILY-C01` | `B1.1-C01` | 8 | — | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C01/` |
| 2 | `C01-W02-B1.1-MATH-FAMILY-C02` | `B1.1-C02` | 8 | — | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C02/` |
| 3 | `C01-W02-B1.1-MATH-FAMILY-C03` | `B1.1-C03` | 9 | `B1.1-C01`, `B1.1-C02` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C03/` |
| 4 | `C01-W02-B1.1-MATH-FAMILY-C04` | `B1.1-C04` | 9 | `B1.1-C02`, `B1.1-C03` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C04/` |
| 5 | `C01-W02-B1.1-MATH-FAMILY-C05` | `B1.1-C05` | 10 | `B1.1-C02`, `B1.1-C03`, `B1.1-C04` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C05/` |
| 6 | `C01-W02-B1.1-MATH-FAMILY-C06` | `B1.1-C06` | 8 | `B1.1-C03`, `B1.1-C05` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C06/` |
| 7 | `C01-W02-B1.1-MATH-FAMILY-C07` | `B1.1-C07` | 10 | `B1.1-C01`, `B1.1-C02`, `B1.1-C03` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C07/` |
| 8 | `C01-W02-B1.1-MATH-FAMILY-C08` | `B1.1-C08` | 8 | `B1.1-C01`, `B1.1-C02` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C08/` |
| 9 | `C01-W02-B1.1-MATH-FAMILY-C09` | `B1.1-C09` | 7 | `B1.1-C01`, `B1.1-C04` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C09/` |
| 10 | `C01-W02-B1.1-MATH-FAMILY-C10` | `B1.1-C10` | 10 | `B1.1-C03`, `B1.1-C05`, `B1.1-C06`, `B1.1-C07`, `B1.1-C08` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C10/` |
| 11 | `C01-W03-B1.2-PHYSICS-FAMILY-C01` | `B1.2-C01` | 6 | `B1.1-C02`, `B1.1-C03` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C01/` |
| 12 | `C01-W03-B1.2-PHYSICS-FAMILY-C02` | `B1.2-C02` | 8 | `B1.2-C01`, `B1.1-C03`, `B1.1-C04` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C02/` |
| 13 | `C01-W03-B1.2-PHYSICS-FAMILY-C03` | `B1.2-C03` | 7 | `B1.2-C01`, `B1.2-C02` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C03/` |
| 14 | `C01-W03-B1.2-PHYSICS-FAMILY-C04` | `B1.2-C04` | 7 | `B1.2-C01`, `B1.2-C02`, `B1.1-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C04/` |
| 15 | `C01-W03-B1.2-PHYSICS-FAMILY-C05` | `B1.2-C05` | 8 | `B1.2-C02` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C05/` |
| 16 | `C01-W03-B1.2-PHYSICS-FAMILY-C06` | `B1.2-C06` | 7 | `B1.2-C01`, `B1.2-C03` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C06/` |
| 17 | `C01-W03-B1.2-PHYSICS-FAMILY-C07` | `B1.2-C07` | 7 | `B1.2-C01`, `B1.2-C05`, `B1.2-C06`, `B1.1-C03`, `B1.1-C05` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C07/` |
| 18 | `C01-W03-B1.2-PHYSICS-FAMILY-C08` | `B1.2-C08` | 6 | `B1.2-C05`, `B1.2-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C08/` |
| 19 | `C01-W03-B1.2-PHYSICS-FAMILY-C09` | `B1.2-C09` | 7 | `B1.2-C04`, `B1.2-C07`, `B1.2-C08` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C09/` |
| 20 | `C01-W03-B1.2-PHYSICS-FAMILY-C10` | `B1.2-C10` | 8 | `B1.2-C01`, `B1.2-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C10/` |
| 21 | `C01-W03-B1.2-PHYSICS-FAMILY-C11` | `B1.2-C11` | 6 | `B1.2-C02`, `B1.2-C06`, `B1.2-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C11/` |
| 22 | `C01-W03-B1.2-PHYSICS-FAMILY-C12` | `B1.2-C12` | 7 | `B1.2-C01`, `B1.2-C02`, `B1.2-C04`, `B1.2-C06` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/C01-W03-B1.2-PHYSICS-FAMILY-C12/` |
| 23 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C01` | `B1.3-C01` | 6 | `B1.2-C07`, `B1.2-C08` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C01/` |
| 24 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C02` | `B1.3-C02` | 6 | `B1.3-C01` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C02/` |
| 25 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C03` | `B1.3-C03` | 6 | `B1.3-C01`, `B1.3-C02` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C03/` |
| 26 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C04` | `B1.3-C04` | 8 | `B1.3-C03`, `B1.2-C04` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C04/` |
| 27 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C05` | `B1.3-C05` | 7 | `B1.3-C03`, `B1.3-C04` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C05/` |
| 28 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C06` | `B1.3-C06` | 7 | `B1.3-C03`, `B1.3-C04` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C06/` |
| 29 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C07` | `B1.3-C07` | 6 | `B1.3-C03`, `B1.3-C04`, `B1.2-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C07/` |
| 30 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C08` | `B1.3-C08` | 7 | `B1.3-C06`, `B1.3-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C08/` |
| 31 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C09` | `B1.3-C09` | 8 | `B1.3-C01`, `B1.3-C03`, `B1.3-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C09/` |
| 32 | `C01-W04-B1.3-CHEMISTRY-FAMILY-C10` | `B1.3-C10` | 8 | `B1.3-C04`, `B1.3-C05`, `B1.3-C09` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C10/` |
| 33 | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C01-C03` | `B1.4-C01`, `B1.4-C02`, `B1.4-C03` | 3 | `B1.3-C01` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C01-C03/` |
| 34 | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C04-C06` | `B1.4-C04`, `B1.4-C05`, `B1.4-C06` | 3 | `B1.4-C02`, `B1.4-C03`, `B1.4-C01` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C04-C06/` |
| 35 | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C07-C09` | `B1.4-C07`, `B1.4-C08`, `B1.4-C09` | 3 | `B1.4-C01`, `B1.4-C06` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C07-C09/` |
| 36 | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C10-C12` | `B1.4-C10`, `B1.4-C11`, `B1.4-C12` | 3 | `B1.2-C12`, `B1.4-C08`, `B1.4-C09` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C10-C12/` |
| 37 | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C13-C15` | `B1.4-C13`, `B1.4-C14`, `B1.4-C15` | 3 | `B1.4-C06`, `B1.4-C12`, `B1.4-C01`, `B1.4-C07`, `B1.4-C08`, `B1.4-C04`, `B1.4-C05`, `B1.4-C10`, `B1.4-C11` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C13-C15/` |
| 38 | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C16-C18` | `B1.4-C16`, `B1.4-C17`, `B1.4-C18` | 3 | `B1.2-C02`, `B1.2-C11`, `B1.2-C05`, `B1.2-C06`, `B1.2-C10`, `B1.2-C01` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C16-C18/` |
| 39 | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C19-C21` | `B1.4-C19`, `B1.4-C20`, `B1.4-C21` | 3 | `B1.4-C18`, `B1.2-C10`, `B1.2-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C19-C21/` |
| 40 | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C22-C24` | `B1.4-C22`, `B1.4-C23`, `B1.4-C24` | 3 | `B1.4-C21`, `B1.2-C10`, `B1.4-C19`, `B1.4-C20` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C22-C24/` |
| 41 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C01` | `B1.5-C01` | 6 | `B1.1-C07`, `B1.1-C08` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C01/` |
| 42 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C02` | `B1.5-C02` | 6 | `B1.1-C01`, `B1.1-C08` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C02/` |
| 43 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C03` | `B1.5-C03` | 7 | `B1.5-C02`, `B1.1-C08` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C03/` |
| 44 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C04` | `B1.5-C04` | 6 | `B1.5-C02`, `B1.5-C03` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C04/` |
| 45 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C05` | `B1.5-C05` | 7 | `B1.5-C04` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C05/` |
| 46 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C06` | `B1.5-C06` | 7 | `B1.5-C02`, `B1.1-C01` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C06/` |
| 47 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C07` | `B1.5-C07` | 9 | `B1.5-C03`, `B1.5-C04` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C07/` |
| 48 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C08` | `B1.5-C08` | 7 | `B1.5-C01`, `B1.5-C03`, `B1.5-C06` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C08/` |
| 49 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C09` | `B1.5-C09` | 7 | `B1.5-C02`, `B1.5-C03`, `B1.5-C08` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C09/` |
| 50 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C10` | `B1.5-C10` | 10 | `B1.5-C03`, `B1.5-C07`, `B1.1-C03`, `B1.1-C05`, `B1.1-C07`, `B1.1-C10` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C10/` |
| 51 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C11` | `B1.5-C11` | 7 | `B1.5-C04`, `B1.5-C05`, `B1.5-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C11/` |
| 52 | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C12` | `B1.5-C12` | 5 | `B1.5-C01`, `B1.5-C02`, `B1.5-C03`, `B1.2-C07` | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY-C12/` |

### Family-level completion checkpoints

| Family | Child count | Scope count | Topic count | Aggregate result path | Next action after family PASS |
|---|---:|---:|---:|---|---|
| `C01-W02-B1.1-MATH-FAMILY` | 10 | 10 | 87 | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/RESULT.json` | `C01-W03-B1.2-PHYSICS-FAMILY` |
| `C01-W03-B1.2-PHYSICS-FAMILY` | 12 | 12 | 84 | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.2/RESULT.json` | `C01-W04-B1.3-CHEMISTRY-FAMILY` |
| `C01-W04-B1.3-CHEMISTRY-FAMILY` | 10 | 10 | 69 | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/RESULT.json` | `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY` |
| `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY` | 8 | 24 | 24 | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/RESULT.json` | `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY` |
| `C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY` | 12 | 12 | 84 | `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.5/RESULT.json` | `C01-W07-B1-INTEGRATION-LOCK` |

## 6. Scope prerequisite graph

`B1_SCOPE_MAP.json` is authoritative for machine-readable `prerequisite_scope_ids`. The graph contains all 68 scopes and is acyclic. The authoring controller must treat a prerequisite as satisfied only by an accepted PASS scope/family or by the fixed canonical knowledge input where the prerequisite is conceptual rather than an already-authored B1 scope.

Cross-family highlights:

- Physics measurement/mechanics depend on arithmetic/algebra/geometry foundations.
- Quantum physics depends on formal mathematical foundations plus waves/electromagnetism.
- Chemistry structure/bonding and physical chemistry depend on relevant quantum/thermodynamic foundations.
- Earth/Universe scopes depend on applicable physics/chemistry, while preserving Earth-system primary ownership.
- Information/Computation depends on mathematical logic, discrete mathematics, probability/statistics, optimization, and for quantum computing on quantum physics.
- AI authoring must consume accepted math/data/algorithm prerequisites rather than reauthoring them as new objectives.

## 7. Child PASS gate

A child returns `PASS` only if all conditions hold:

1. Every assigned `canonical_topic_id` is covered by at least one compliant node and no unassigned topic is claimed as primary.
2. The assigned topic set still has exactly one primary authoring owner.
3. Node/claim/source/objective records conform to `B1_ID_AND_RECORD_STANDARD.md`.
4. D1–D4 are explicit and age/presentation remains orthogonal.
5. All prerequisite references are stable and traceable.
6. Duplicate scan is run against all previously accepted B1 child artifacts plus risk cases in `B1_DUPLICATE_CONTROL.md`.
7. Secondary cross-links are recorded without ownership transfer.
8. No later pipeline-stage work is authored.
9. The child's mandatory status folder is current, includes an append-only pre-PASS checkpoint, and records completed/remaining work, authoritative paths/commits, locked decisions, do-not-repeat, status and next action.
10. Child `RESULT.json` records exact `input_commit_sha`, output paths, IDs/counts, coverage, duplicate disposition, status and deterministic `next_action`.

## 8. Resume algorithm

On restart, a family controller enumerates the child table in order and checks each child's committed `RESULT.json`. It skips every `PASS` child, resumes the first child without PASS using its existing stable IDs/artifacts, and does not touch later children. This makes progress independent of chat history.

## 9. First successor only

After this architecture window passes, the only permitted next action is:

`C01-W02-B1.1-MATH-FAMILY` as the registered family controller, executing only its first bounded child `C01-W02-B1.1-MATH-FAMILY-C01` until that child has a durable `PASS` checkpoint.
