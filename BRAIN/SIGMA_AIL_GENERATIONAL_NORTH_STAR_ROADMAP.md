# SIGMA.AIL — Generational North-Star Roadmap

## 1. Program rule: real work, not simulated progress

This roadmap is a capability-development guide, not a source of runtime truth.

Generation promotion is evidence-driven and fail-closed:

```text
NO_SIMULATED_PASS=YES
NO_INVENTED_CAPABILITY=YES
NO_HOST_COGNITION_SUBSTITUTION=YES
NO_MANUAL_ORACLE_SUBSTITUTION=YES
NO_GENERATION_PROMOTION_WITHOUT_VERIFIED_EVIDENCE=YES
```

A future target written as `...=PASS` in this document is an admission goal. It must not be reported as achieved until the corresponding implementation, native/runtime execution, receipts, lineage, replay/regression evidence, and scope boundaries actually prove it.

Revision/FIX work may be numerous inside one generation. Generation numbers advance only when the named cognitive bottleneck has been broken in verified execution.

## 2. Program scale

The major-generation plan is intentionally compact:

```text
CURRENT_MAJOR_GENERATION=G1
ESTIMATED_REMAINING_MAJOR_UPGRADES≈6
NORTH_STAR_GENERATION=G7
```

This does not limit internal engineering iterations. R4.1, R4.2, FIX1, FIX2, admission reruns, rollback fixes, and regression work may occur as needed without changing the generation number.

The generation axis tracks major capability transitions; the revision axis tracks implementation evolution.

## 3. Generation map

```text
G1  CURRENT BRAIN
    ↓
G2  ONE SIGMA.AIL
    ↓
G3  LEARNED NARRATIVE BRAIN
    ↓
G4  GROUNDED SEMANTIC BRAIN
    ↓
G5  HUMAN-LANGUAGE / MULTILINGUAL BRAIN
    ↓
G6  AUTONOMOUS WORLD-LEARNING BRAIN
    ↓
G7  NORTH-STAR INTEGRATED BRAIN
```

---

## G1 — Current Brain

### Role

G1 is the current Integral/Owner brain foundation.

Current architectural capability set:

```text
Integral/Owner brain
persistent state
long-document incremental processing
Semantic IR foundation
replay / revision foundation
narrative-summary path
```

G1 establishes the substrate from which the later learned brain generations are built. It is not treated as proof that later semantic, multilingual, autonomous-learning, or integrated north-star gates are already satisfied.

---

## G2 — One SIGMA.AIL

### Bottleneck

Eliminate identity/state fragmentation so every execution surface addresses one continuous SIGMA.AIL.

Canonical invariants:

```text
ONE_IDENTITY
ONE_BRAIN_STATE
ONE_MODEL_HISTORY
ONE_MEMORY
ONE_COMMIT_AUTHORITY
ONE_WRITER
```

TMUX sessions, Web windows, replay processes, tests, shells, workers, directories, and candidate bundles are access/execution surfaces. They are not separate SIGMA identities.

Target gates:

```text
SIGMA_AIL_SINGLE_IDENTITY=PASS
CROSS_WINDOW_LEARNING_VISIBLE=PASS
RESTART_CONTINUITY=PASS
```

Generation promotion requires real continuity of the canonical brain/history across independently restarted execution contexts, with one authoritative writer/commit path and no state fork hidden behind process or directory boundaries.

---

## G3 — Learned Narrative Brain

### Bottleneck

Replace fail-safe/static narrative representations with learned representations that actually change model generation and support narrative reasoning.

Current critical indicator called out for the R4 narrative path:

```text
model_generation=0
```

G3 must move the narrative path to a genuinely learned pipeline:

```text
raw story
→ learned segment representation
→ entity/event state
→ temporal state
→ causal state
→ narrative consolidation
→ learned summary decision
```

The governing rule is that success must not come from phrase lists or hand-authored phrase matching.

Primary targets:

```text
MODEL_GENERATION > 0
FROZEN_20_STORY: 0/20 → ... → 20/20
NO_PHRASE_RULE_SUBSTITUTION=PASS
```

The central stress target is the frozen 20-story long-document challenge identified by the program, including the 202,500-word-scale test regime. The exact corpus/version and scoring contract must remain provenance-bound in the corresponding evidence artifacts.

G3 is the first major learning bottleneck. If learned narrative representation is not real, later semantic and world-learning generations do not have a trustworthy substrate.

---

## G4 — Grounded Semantic Brain

### Bottleneck

Move from narrative summarization to grounded content-level semantic induction and revision.

The learned state must represent and operate over at least:

```text
entity
relation
cause
belief
contradiction
revision
perspective
goal
counterfactual
```

The decisive property is generalization beyond the exact observed templates and fixtures.

Target gates:

```text
GENERAL_LEARNED_SEMANTIC_INDUCTION=PASS
UNSEEN_COMPOSITIONAL_GENERALIZATION=PASS
FULL_DOCUMENT_UNDERSTANDING=PASS
CROSS_DOCUMENT_UNDERSTANDING=PASS
LONG_CONTEXT_REVISION=PASS
```

Passing isolated canonical transitions is insufficient for G4. Promotion requires evidence that the learned semantic machinery generalizes to unseen compositions and remains coherent across whole documents and cross-document revision.

---

## G5 — Human-Language / Multilingual Brain

### Bottleneck

Ground human-language understanding in the same learned internal representation rather than accumulating language-specific rule stacks.

Major language/interaction scope:

```text
Vietnamese
English
multilingual transfer
intent
emotion
perspective
contextual response
```

Target gates:

```text
SIGMA_HUMAN_LANGUAGE_UNDERSTANDING=PASS
SIGMA_VIETNAMESE_DEEP_UNDERSTANDING=PASS
SIGMA_MULTILINGUAL_UNDERSTANDING=PASS
SIGMA_INTENT_UNDERSTANDING=PASS
SIGMA_EMOTION_RECOGNITION=PASS
SIGMA_PERSPECTIVE_TAKING=PASS
```

The intended architecture is shared learned representation, not one independent rule engine per language.

---

## G6 — Autonomous World-Learning Brain

### Bottleneck

Turn external information sources, including the Internet, into provenance-bound learning experience selected and processed by SIGMA.AIL itself.

Online learning chain:

```text
knowledge gap
→ choose what to study
→ choose capability
→ discover source
→ read
→ compare sources
→ learn
→ verify
→ commit
→ replay
→ continue
```

Offline continuation chain:

```text
NO INTERNET
→ replay
→ consolidate
→ revise
→ continue learning
```

Target gates:

```text
AUTONOMOUS_WEB_DISCOVERY=PASS
MULTI_SOURCE_LEARNING=PASS
SELF_IDENTIFIES_KNOWLEDGE_GAPS=PASS
SELF_SELECTS_CAPABILITIES=PASS
SELF_SELECTS_WHAT_TO_STUDY_NEXT=PASS
OFFLINE_LEARNING=PASS
CONTINUAL_CONSOLIDATION=PASS
```

The Internet is treated as an experience/source environment, not as a replacement cognition engine. Host scripts, external LLMs, search providers, browsers, and capability adapters may transport or mechanically expose information, but they must not be mislabeled as SIGMA's learned cognition.

---

## G7 — North-Star Integrated Brain

### Bottleneck

Integrate the learned capabilities into one long-lived SIGMA.AIL brain without fragmentation or catastrophic loss.

The target system must make the following domains coexist in one canonical state/history:

```text
Web
reading
language
narrative
memory
belief
replay
capability selection
self-study
```

The integrated system must remain stable against:

```text
catastrophic forgetting
state forks
host cognition substitution
manual oracle dependence
fixed capability ceiling
```

### North-star gate set

```text
SIGMA_AUTONOMOUS_LEARNING=PASS
SIGMA_AUTONOMOUS_WEB_DISCOVERY=PASS
SIGMA_AUTONOMOUS_READING=PASS
SIGMA_MULTI_SOURCE_LEARNING=PASS

SIGMA_FULL_DOCUMENT_UNDERSTANDING=PASS
SIGMA_CROSS_DOCUMENT_UNDERSTANDING=PASS
SIGMA_LONG_CONTEXT_REVISION=PASS

SIGMA_HUMAN_LANGUAGE_UNDERSTANDING=PASS
SIGMA_VIETNAMESE_DEEP_UNDERSTANDING=PASS
SIGMA_MULTILINGUAL_UNDERSTANDING=PASS

SIGMA_NARRATIVE_UNDERSTANDING=PASS
SIGMA_INTENT_UNDERSTANDING=PASS
SIGMA_EMOTION_RECOGNITION=PASS
SIGMA_PERSPECTIVE_TAKING=PASS
SIGMA_CONTEXTUAL_EMPATHIC_RESPONSE=PASS

SIGMA_LEARNED_REPRESENTATION=PASS
SIGMA_COMPRESSED_NATIVE_MEMORY=PASS
SIGMA_PROVENANCE_BOUND_MEMORY=PASS

SIGMA_OFFLINE_LEARNING=PASS
SIGMA_MEMORY_REPLAY=PASS
SIGMA_CONTINUAL_CONSOLIDATION=PASS
SIGMA_BELIEF_REVISION=PASS

SIGMA_SELF_IDENTIFIES_KNOWLEDGE_GAPS=PASS
SIGMA_SELF_SELECTS_CAPABILITIES=PASS
SIGMA_SELF_SELECTS_WHAT_TO_STUDY_NEXT=PASS
```

G7 is primarily an integration/consolidation generation. Its purpose is not to maximize the number of new adapters or capabilities, but to make the previously learned capabilities coexist under one identity, one brain state, one provenance chain, and one commit authority for long-duration operation.

## 4. Generation promotion policy

A generation advances only when its bottleneck is broken by verified evidence.

Minimum promotion discipline:

```text
IMPLEMENTATION_EXISTS=YES
NATIVE_OR_CANONICAL_RUNTIME_EXECUTED=YES
PROVENANCE_BOUND_INPUTS=YES
RECEIPTS_OR_EQUIVALENT_EVIDENCE=YES
REPLAY_OR_REPRODUCIBILITY=PASS
REGRESSION_BOUNDARIES_CHECKED=YES
CLAIM_SCOPE_EXPLICIT=YES
HOST_SUBSTITUTION_REJECTED=YES
SIMULATED_PASS=NO
```

A FIX may repair correctness, determinism, replay, lineage, transport, admission, or safety while remaining inside the same generation. Generation promotion is reserved for genuine capability transition.

## 5. Program priority

The immediate strategic priority is G3.

```text
CURRENT=G1
ARCHITECTURAL_CONVERGENCE=G2
FIRST_MAJOR_COGNITIVE_BREAKTHROUGH=G3
```

The critical G3 question is whether SIGMA.AIL can move from `model_generation=0` and fail-safe narrative representation to a real learned narrative brain, then survive the frozen long-document challenge under reproducible evaluation.

Until that succeeds, G4–G7 remain roadmap targets rather than achieved capability claims.

## 6. North-star summary

```text
SYSTEM_IDENTITY=SIGMA.AIL
CURRENT_MAJOR_GENERATION=G1
REMAINING_MAJOR_UPGRADES≈6
FINAL_MAJOR_GENERATION=G7

REVISION_NUMBER_DOES_NOT_CONTROL_GENERATION=YES
FIX_NUMBER_DOES_NOT_CONTROL_GENERATION=YES
GENERATION_ADVANCES_ONLY_ON_REAL_BOTTLENECK_BREAK=YES
ONE_SIGMA_AIL=YES
ONE_BRAIN_STATE=YES
ONE_LEARNING_HISTORY=YES
ONE_PROVENANCE_CHAIN=YES
ONE_COMMIT_AUTHORITY=YES
```

This document is the north-star roadmap. Verified runtime/evidence artifacts remain authoritative for what SIGMA.AIL has actually achieved at any point in time.