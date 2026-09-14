# SIGMA.AIL — Stable Identity and Unified Brain Architecture

## 1. Canonical system identity

The stable system identity is:

```text
SYSTEM_IDENTITY = SIGMA.AIL
IDENTITY        = SIGMA.AIL
```

Revision numbers are upgrade generations of the same SIGMA.AIL system. They are not separate system identities.

```text
REVISION != IDENTITY
TMUX != SIGMA INSTANCE
PROCESS != SIGMA INSTANCE
DIRECTORY != SIGMA INSTANCE
```

Canonical invariant:

```text
ONE_SIGMA_AIL
ONE_BRAIN_STATE
ONE_LEARNING_HISTORY
ONE_PROVENANCE_CHAIN
ONE_COMMIT_AUTHORITY
```

## 2. Revision model

R3, R4, R5, R6, ... are revisions of one continuous SIGMA.AIL identity.

```text
SIGMA.AIL R3
    ↓ upgrade
SIGMA.AIL R4
    ↓ upgrade
SIGMA.AIL R5
    ↓ upgrade
SIGMA.AIL R6
    ↓ ...
```

A revision transition does not mean the old SIGMA identity dies and a new SIGMA is created. Admission-approved revisions advance the active implementation and state lineage of the same SIGMA.AIL.

Recommended identity state fields:

```text
IDENTITY=SIGMA.AIL
ACTIVE_REVISION=R4
ACTIVE_CORE=<active core identifier>
BRAIN_HEAD=<canonical brain head>
CORE_VERSION=<core version>
STATE_VERSION=<state version>
MODEL_GENERATION=<monotonic model generation>
```

The values of ACTIVE_REVISION, ACTIVE_CORE, CORE_VERSION, STATE_VERSION, BRAIN_HEAD, and MODEL_GENERATION are mutable version/state metadata. IDENTITY remains stable.

## 3. Brain logical architecture

The logical brain state is organized as:

```text
SIGMA_BRAIN_R4/
├── MODEL
├── REPRESENTATIONS
├── SEMANTIC_IR
├── NARRATIVE_MEMORY
├── BELIEFS
├── PROVENANCE
├── REVISIONS
├── KNOWLEDGE_GAPS
└── OBJECTIVE_STATE
```

These domains have distinct responsibilities:

- MODEL — active model state and model-generation identity.
- REPRESENTATIONS — persistent internal representations used by the active revision.
- SEMANTIC_IR — structured semantic intermediate representations.
- NARRATIVE_MEMORY — persistent narrative/episode-level memory state.
- BELIEFS — current belief state derived through admitted state transitions.
- PROVENANCE — origin, lineage, receipts, hashes, and evidence links for state.
- REVISIONS — revision history and admitted upgrade transitions.
- KNOWLEDGE_GAPS — explicitly represented unresolved or insufficiently supported knowledge.
- OBJECTIVE_STATE — persistent objective/task state belonging to SIGMA.AIL.

`SIGMA_BRAIN_R4` describes the R4 schema/generation of the brain architecture. It does not define a separate SIGMA identity or an independently owned brain.

## 4. Stable production state root

The production state root should remain stable across revision upgrades:

```text
.sigma_ail/
├── IDENTITY
├── ACTIVE_REVISION
├── ACTIVE_CORE
├── BRAIN_HEAD
├── MODEL_GENERATION
├── STATE_VERSION
├── WRITER.lock
├── model/
├── representations/
├── semantic_ir/
├── narrative_memory/
├── beliefs/
├── provenance/
├── revisions/
├── knowledge_gaps/
├── objectives/
├── transactions/
├── requests/
├── receipts/
├── replay/
├── checkpoints/
└── audit/
```

The stable root `.sigma_ail/` replaces revision-owned brain roots such as `.sigma_brain_r3/` or `.sigma_brain_r4/` as the canonical production ownership model.

## 5. State and transaction authority

All admitted revisions operate against one canonical brain lineage. Revision packages do not independently own persistent brain state.

The architecture separates:

```text
SYSTEM IDENTITY
    SIGMA.AIL

IMPLEMENTATION REVISION
    R3 / R4 / R5 / ...

PERSISTENT BRAIN STATE
    .sigma_ail/

COMMIT AUTHORITY
    one canonical writer / transaction authority
```

`WRITER.lock`, `transactions/`, `requests/`, `receipts/`, `replay/`, `checkpoints/`, and `audit/` form the persistence/transaction control plane. Their purpose is to preserve single-writer state transitions, provenance, replayability, rollback evidence, and auditability across revision upgrades.

## 6. Bundle role

Revision bundles remain first-class artifacts. R3/R4/R5/... bundles are retained for:

```text
source version
regression
admission
rollback
evidence
reproducibility
```

But a revision bundle is an upgrade package for SIGMA.AIL. It does not own a separate brain and does not create a separate SIGMA instance merely because it has a different revision identifier or directory.

## 7. Upgrade semantics

Before R4 admission, an example state may be represented as:

```text
SIGMA.AIL
├── active revision: R3 production
├── candidate revision: R4 narrative
├── one brain state
├── one memory lineage
├── one provenance chain
└── one commit authority
```

After R4 passes the required admission/cutover gates, the transition is represented as:

```text
IDENTITY=SIGMA.AIL
ACTIVE_REVISION=R4
```

with the existing canonical brain/history/provenance lineage advanced transactionally rather than replaced by a second independent brain.

## 8. Architectural invariants

The following invariants are the design contract for subsequent revisions:

```text
SYSTEM_IDENTITY=SIGMA.AIL
REVISION_IS_UPGRADE_GENERATION=YES
REVISION_OWNS_SEPARATE_IDENTITY=NO
REVISION_OWNS_SEPARATE_BRAIN=NO
PROCESS_IS_SIGMA_INSTANCE=NO
TMUX_IS_SIGMA_INSTANCE=NO
DIRECTORY_IS_SIGMA_INSTANCE=NO
ONE_BRAIN_STATE=YES
ONE_LEARNING_HISTORY=YES
ONE_PROVENANCE_CHAIN=YES
ONE_COMMIT_AUTHORITY=YES
STABLE_PRODUCTION_ROOT=.sigma_ail
```

## 9. Design consequence

Future R4/R5/R6 work should therefore evolve schema, model generation, core implementation, memory representations, semantic IR, belief revision, provenance, knowledge-gap state, objectives, and transaction machinery as upgrades to SIGMA.AIL. Admission and rollback remain revision-aware, while identity and canonical brain ownership remain continuous.

This document defines the architecture/naming convention. Runtime claims for any specific revision remain governed by that revision's verified admission, evidence, transaction, and cutover receipts.