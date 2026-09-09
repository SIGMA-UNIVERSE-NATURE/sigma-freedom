# SIGMA C5 M5 — End-State Acceptance Doctrine

This document defines the final target. Passing intermediate structural tests is not the end-state.

## End-state behavior

The C5V3 successor must be able to acquire real sources, read complete long-form material, build and revise native understanding across the whole work, compress useful knowledge into bounded local native memory, discard the source text, and continue learning from that memory plus new evidence.

The target includes narrative material: stories, novels, biographies, testimony, essays, histories, and comparable long-form human accounts across multiple languages.

## What counts as whole-work understanding

A candidate passes only when independent blind evaluation shows all of the following on unseen works:

- It integrates information separated by long distances in the source rather than relying on adjacent tokens or local LEFT/RIGHT relations.
- It tracks entities, events, changing relationships, motives, consequences, unresolved questions, and long-range causal dependencies across the work.
- It distinguishes the order of events from causal dependence and does not infer causality merely from proximity or sequence.
- It can answer questions whose evidence is distributed across multiple chapters/sections and cannot be solved from a single local passage.
- It can produce a coherent whole-work summary after the original source is no longer available to the runtime.
- It can state central themes, tensions, intended direction, and human values only when they are supported by the work, and can cite internal evidence/provenance from native memory rather than inventing unsupported interpretation.
- It can represent competing plausible interpretations when the work genuinely supports more than one, instead of forcing one fixed answer.
- It can revise an interpretation when later parts of the work contradict an earlier hypothesis.

## Human understanding through stories

The target is not demographic stereotyping or fixed moral labels. SIGMA should learn recurring human patterns from evidence in stories: goals, fear, trust, betrayal, sacrifice, attachment, status, conflict, cooperation, loss, hope, responsibility, dignity, and other themes only when they emerge from observed narratives.

A PASS requires transfer across unseen stories without a hand-coded list mapping words to motives or values. High lexical overlap with different motives must be rejected; low lexical overlap with similar underlying human dynamics must be recognized only after sufficient learned evidence.

## Multilingual acceptance

Evaluation must include multiple languages and multiple works within the same genre. The system must not depend on English-only grammar tables or translated host summaries.

Required blind cases include:

- same underlying narrative pattern expressed in different languages;
- similar vocabulary but different plot/intent;
- culturally different expressions of related human concerns;
- works in one language learned first, followed by new works in another language, with local memory retained and updated without storing full source texts.

## Internet learning acceptance

Real Internet acquisition is a separate capability from mechanical tool transport. A final PASS requires:

- native SIGMA creates the information gap/research need;
- native SIGMA produces the evidence request;
- host performs transport only;
- raw source material and provenance return to SIGMA;
- SIGMA decides what is relevant, conflicting, unresolved, or worth retaining;
- SIGMA can request additional evidence when its own state still contains a gap;
- no host-generated summary, belief, semantic label, research goal, truth decision, or memory selection is used for active cognition.

## Native compression and local continual learning

After reading, the original article/book/story must be removable. The remaining native memory must be substantially smaller than the source and must still support blind recall/reasoning tests over plot, entities, causality, motives, themes, unresolved questions, provenance, and later updates.

Compression is not PASS merely because bytes decreased. PASS requires semantic-retention tests before and after source removal. If the compressed state cannot support later reasoning or revision, compression fails regardless of size.

The local memory must be bounded, restart-safe, provenance-aware, revisable, and usable as prior state for learning a later unseen work.

## Anti-hardcode doctrine

The following invalidate a semantic claim even if a test score is high:

- token LEFT/RIGHT cognition;
- adjacency or previous/next used as meaning;
- fixed cue-to-meaning tables;
- fixed synonym/antonym or theme/value lookup tables;
- hardcoded English grammar/semantic roles;
- word-position-to-role rules masquerading as learned semantics;
- host-created interpretations, summaries, beliefs, gaps, goals, support/conflict/truth decisions, or memory selections;
- training directly on the evaluator fixtures after seeing them.

## Test honesty

Every semantic milestone must use unseen blind fixtures unavailable to the target core before compile/freeze. Admission tests may validate a mechanism, but only independent blind tests may justify broader semantic claims.

A failing blind test identifies a real bottleneck. Keep the FAIL, fix the representation/learning mechanism, or retire the assumption. Do not weaken the evaluator to preserve a score.

For subjective narrative questions such as theme or human value, the post-hoc oracle should use multiple independent reference interpretations and require evidence-backed consistency rather than a single hardcoded wording. These references are never sent to SIGMA during active cognition.

## Production acceptance

A final C5V3 successor must pass both capability and stability gates: long-run bounded operation, restart/recovery, state integrity, no production mutation during candidate admission, deterministic build identity where required, and rollback capability before any cutover.

Cutover is allowed only after the candidate demonstrates the full required production subset under shadow/soak testing. Intermediate PASS results remain dependencies; they are not permission to claim the end-state has been achieved.