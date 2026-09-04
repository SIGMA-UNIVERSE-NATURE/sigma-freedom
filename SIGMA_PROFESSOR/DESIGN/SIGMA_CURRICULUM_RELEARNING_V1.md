# SIGMA CURRICULUM + RE-LEARNING DESIGN V1

Date: 2026-09-04 (Asia/Ho_Chi_Minh)

## Goal

Extend SIGMA beyond one-pass continuous learning. SIGMA must revisit old material, decide what is worth deeper study, group related material, split large documents into bounded learning units, re-learn selected material, consolidate recurrent patterns, and revalidate old knowledge.

## Non-negotiable boundary

HOST_LEARNING=NO
HOST_SUMMARIZATION=NO
HOST_LESSON_GENERATION=NO
HOST_CANDIDATE_SELECTION=NO
HOST_KNOWLEDGE_SCORING=NO
HOST_TOPIC_CLASSIFICATION=NO

Host mechanics remain allowed only for byte transport, exact protocol decoding, hashing, file persistence, deterministic scheduling, process supervision, and VM invocation.

All decisions about what is worth learning, how material is grouped, which segment is prioritized, what pattern is retained, and what is revalidated must be computed by SIGMA-native code.

## Raw-data invariant

Raw documents are immutable and content-addressed. Re-learning never overwrites raw material.

Derived state is stored separately:

- DOCUMENT_SURVEY
- SEGMENT_MANIFEST
- GROUP_ASSIGNMENT
- CURRICULUM_QUEUE
- LEARNING_HISTORY
- CANDIDATE_KNOWLEDGE
- CONSOLIDATED_KNOWLEDGE
- REVALIDATION_STATE

## Learning lifecycle

RAW_DOCUMENT
-> SURVEY
-> SEGMENT
-> STRUCTURAL_PROFILE
-> GROUP
-> CURRICULUM_PRIORITY
-> DEEP_LEARN
-> CROSS_DOCUMENT_COMPARE
-> CONSOLIDATE
-> REVALIDATE
-> REVISIT_OR_ARCHIVE_FOR_NOW

The lifecycle is cyclic. A document can return to DEEP_LEARN when new evidence changes its relevance.

## Phase A — Survey old documents

SIGMA performs a bounded pass over each old document and records only native-derived observations, for example:

- line count / bounded token count
- recurrent relations observed in the document
- strongest native-selected relation(s)
- unresolved recurrent frontier(s)
- whether the document has already contributed accepted knowledge
- last learning cycle / last revalidation cycle

Survey must be cheaper than full re-learning.

## Phase B — Native segmentation

Large documents must not be processed as one unbounded VM job.

SIGMA determines learning-unit boundaries from document structure that is already mechanically visible to the VM (initial implementation: lines / bounded consecutive line windows).

Each unit gets a stable identity derived mechanically from:

DOCUMENT_SHA256 + SEGMENT_INDEX + exact segment bytes

Host may persist/copy exact segment bytes after SIGMA has selected the boundaries; host must not choose semantic boundaries.

## Phase C — Native grouping

Initial grouping is explicitly structural, not claimed semantic.

SIGMA assigns documents/segments to groups based on native evidence such as shared recurrent relations and overlapping selected structural anchors.

No hardcoded topic taxonomy.

A group is a derived learning cluster, not a declaration of human-level semantic category.

## Phase D — What is worth deeper learning?

Initial native priority inputs:

1. recurrence across distinct contexts;
2. unresolved frontier status;
3. novelty relative to consolidated memory;
4. contradiction candidate / competing structural evidence;
5. evidence diversity across documents;
6. age since last revalidation;
7. whether prior learning was interrupted or incomplete.

Do not use a hardcoded lesson list, stopword list, preferred topic list, or host-generated importance score.

The exact priority formula must be implemented and tested in SIGMA-native code and may evolve from experience.

## Phase E — Curriculum queue

SIGMA produces a persistent curriculum queue containing stable work identities, for example:

GROUP_ID
DOCUMENT_SHA256
SEGMENT_ID
LEARNING_STAGE
NATIVE_PRIORITY
LAST_COMPLETED_CURSOR
REVALIDATE_AFTER

On restart, SIGMA resumes the highest eligible unfinished work item according to its own persisted curriculum state.

RECOVERY -> RESUME_CURRICULUM, never RECOVERY -> IDLE.

## Phase F — Deep learning

Deep learning runs on bounded segments, not whole unbounded documents.

For each segment SIGMA:

- derives structural relations from runtime input;
- compares against persistent experience;
- computes recurrence / cross-context support;
- generates candidates natively;
- selects natively;
- records provenance back to document + segment identity;
- commits only after a successful VM cycle.

## Phase G — Consolidation

SIGMA periodically revisits groups, not just individual documents.

Consolidation asks whether patterns are:

- repeated across independent contexts;
- duplicated;
- contradicted by newer evidence;
- too generic to be useful;
- still unresolved and worth another fetch/review cycle.

At the current proven capability level this remains structural consolidation. Semantic understanding must not be claimed until separately proven.

## Phase H — Revalidation / decay

Old accepted knowledge is not permanent by default.

SIGMA stores provenance and a revalidation state. New evidence may strengthen, weaken, reopen, or supersede previously selected structural knowledge.

Knowledge deletion or replacement must be transactional and provenance-preserving.

## Runtime constraints learned from V2.3/V2.4

- Full-history nested scans can hit `SIGMA C VM: step limit`.
- Learning must therefore become bounded/incremental as history grows.
- V2.4 recurrent-support frontier is the current low-cost continuous policy after removing endpoint TOKEN_LOAD full-history scans.
- Future survey/group/curriculum stages must avoid O(document_relations * full_history * additional_full_history_scan) style work in one VM execution.

## Planned implementation sequence after V2.4 stability

1. V2.5 DOCUMENT_SURVEY (read old documents, produce lightweight native survey state).
2. V2.6 BOUNDED_SEGMENT_CURSOR (native selected line windows, crash-resumable cursor).
3. V2.7 STRUCTURAL_GROUPING (shared recurrent-anchor grouping).
4. V2.8 CURRICULUM_QUEUE (native persistent priority + unfinished-work resume).
5. V2.9 GROUP_CONSOLIDATION + REVALIDATION.
6. Only after these are stable: improve self-direction quality beyond structural heuristics.

## Claims discipline

Already proven in exact tested scopes before this design:

- native dynamic structural relation generation;
- persistent recurrence;
- native self-selection;
- cross-context support;
- native-generated fetch request -> Internet transport -> decoded plaintext -> native learning;
- V2.4 preflight long-context completion without reproducing the V2.3 step-limit failure.

Not proven and must not be claimed:

- semantic understanding;
- human-like topic comprehension;
- semantic curiosity;
- general autonomous reasoning.
