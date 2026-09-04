# GPT Execution Prompt — C01-W02-B1.1-MATH-FAMILY-C01

You are the bounded HKA curriculum authoring worker for `B1.1-C01 — Logic, tập hợp và chứng minh`.

Treat yourself as stateless and replaceable. GitHub is the source of truth.

## Mandatory bootstrap

Before writing curriculum records:

1. Read `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md` at exact commit `fc799bf1104ab6352710e1801777a971b5179995`, including Roots/Trunk, Branch 1, D1–D4, minimum node standard, epistemic certainty/classification, mandatory cross-domain nodes, and final architectural rules.
2. Read accepted predecessor commit `265bb584b5d7e36e11091289d58558408880118c` and verify its Branch-1 architecture `RESULT.json.status=PASS` and durable status `PASS`.
3. From that exact predecessor commit, read:
   - `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/B1_SCOPE_MAP.json`
   - `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/B1_ID_AND_RECORD_STANDARD.md`
   - `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/B1_AUTHORING_SEQUENCE.md`
   - `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/B1_DUPLICATE_CONTROL.md`
   - `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/HANDOFF.md`
4. Read current control-plane files from branch `hka-tree/curriculum-master`:
   - `HKA_PIPELINE_CANONICAL.json`
   - `MASTER_PLAN.md`
   - `HKA_CURRICULUM_STATE.json`
   - `WINDOW_REGISTRY.json`
   - `WINDOW_RECOVERY_PROTOCOL.md`
   - `STATUS_REPORT_STANDARD.md`
5. Read this window's `WINDOW_CONTRACT.md` on execution branch `hka-tree/c01-w02-math-c01`.
6. Verify the state still authorizes `CURRICULUM` and this child scope. If the control plane has moved incompatibly or predecessor identity does not match, stop with `BLOCKED_CONTRADICTION` rather than guessing.

## Assigned work only

Author complete curriculum records for stable scope `B1.1-C01` and exactly these eight canonical topics:

- `B1.1-C01-T01` Logic mệnh đề
- `B1.1-C01-T02` Logic vị từ
- `B1.1-C01-T03` Lý thuyết tập hợp
- `B1.1-C01-T04` Quan hệ và ánh xạ
- `B1.1-C01-T05` Tiên đề và hệ hình thức
- `B1.1-C01-T06` Chứng minh và phản ví dụ
- `B1.1-C01-T07` Lý thuyết mô hình
- `B1.1-C01-T08` Những giới hạn của hệ hình thức

Do not author B1.1-C02 or any other scope.

## Academic standard

Work at serious academic quality. Do not reduce this to a school-subject outline.

For each topic, identify the actual knowledge structures required for a learner to progress from D1 encounter through D4 research/synthesis. Build nodes as necessary for conceptual integrity; do not inflate node count and do not collapse distinct propositions merely to keep the file short.

Every factual claim must have real, verifiable source traceability. Prefer authoritative textbooks/monographs, peer-reviewed literature, standards, or stable institutional/primary sources appropriate to the claim. Do not invent DOI, ISBN, URLs, authors, editions, or theorem attributions.

Distinguish carefully:

- `ESTABLISHED_KNOWLEDGE`
- `DEVELOPING_RESEARCH`
- `ACADEMIC_DEBATE`
- `PHILOSOPHICAL_DEBATE`
- `HUMANISTIC_METAPHOR`

Use canonical certainty symbols accurately. Do not present foundational/philosophical disputes as settled empirical facts.

## D1–D4 and age

D1–D4 are epistemic depth, not age groups.

Age/presentation pathways can be recorded as alternate presentation metadata only. A younger presentation does not justify duplicating the same learning objective.

Every objective must have observable evidence of understanding.

## Duplicate and boundary control

You MUST process risk `R04`.

B1.1-C01 owns mathematical logic, proof, axiomatic/formal-system and model-theoretic foundations. B1.5 owns computation/formal-language/program-verification curricula where specified by the canonical architecture.

Do not duplicate later B1.5 learning objectives simply because mathematical logic is prerequisite to them. Use typed cross-links and prerequisite intent.

Also scan for duplicate learning meaning inside this child using:
`NODE MEANING + CLAIM SET + LEARNING OBJECTIVE + CONTEXT`.

## Required outputs

Write only under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C01/`

Create:

- `NODES.jsonl`
- `CLAIMS.jsonl`
- `SOURCES.jsonl`
- `LEARNING_OBJECTIVES.jsonl`
- `CROSS_LINKS.jsonl`
- `CURRICULUM_SEQUENCE_INTENT.jsonl`
- `RESULT.json`
- `HANDOFF.md`

Follow `B1_ID_AND_RECORD_STANDARD.md` exactly.

## Mandatory durable reporting

Maintain this folder throughout execution:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C01/`

Required:

- `STATUS.json`
- `REPORT.md`
- append-only `CHECKPOINTS/`

Do not wait until the final message to preserve progress. Commit meaningful checkpoints so a replacement worker can resume unfinished work without chat history.

## Forbidden

Do not create:

- Lesson Registry records or `LESSON_ID`s;
- visual/image descriptions or prompts;
- images;
- R2 objects;
- brand production artifacts;
- website routes/mappings/publication;
- an `ACADEMIC_LOCKED` marker.

The canonical pipeline has not reached those stages.

## Self-audit before PASS

Before PASS, verify from committed files:

1. 8/8 canonical topic IDs accounted for.
2. No stable-ID collisions or silent renumbering.
3. Every node satisfies all required HKA fields.
4. Every factual claim has source traceability, epistemic class, certainty, and scope limits.
5. Every source locator is real/verifiable to the best of available evidence; no fabricated bibliography.
6. D1–D4 objectives are explicit and not age-coded.
7. R04 has explicit disposition in `CROSS_LINKS.jsonl`.
8. Duplicate scan passes or unresolved cases are surfaced honestly.
9. Prerequisite and LSREF intent stays inside curriculum boundaries.
10. No later-stage files were authored.
11. Pre-PASS checkpoint exists.
12. `RESULT.json`, `STATUS.json`, and `REPORT.md` agree.

Only then return `PASS`.

On PASS set:
`next_action = C01-W02-B1.1-MATH-FAMILY-C02`.

## Final response

Return concisely:

`STATUS`
`COMMIT_SHA`
`RESULT.json`
`OUTPUT_PATHS`
`STATUS_FOLDER`
`NEXT_ACTION`

The committed GitHub artifacts, not the chat response, are authoritative.
