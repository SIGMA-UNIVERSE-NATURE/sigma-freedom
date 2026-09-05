# B1.1 Mathematics Execution Dependency Amendment 3

Status: ACTIVE  
Stage: `CURRICULUM`  
Scope affected: `B1.1-C07 — Xác suất, thống kê và suy luận`

## Purpose

Preserve complete knowledge with minimum redundancy by making already-accepted foundations explicit before C07 authoring.

The frozen B1 architecture lists C01/C02/C03 as base prerequisites for C07. At D3–D4 depth, however:

- rigorous probability spaces/random variables/stochastic-process foundations must reuse accepted C05 measure/integration/function-space primitives rather than re-author measure theory inside C07;
- causal inference at `B1.1-C07-T10` must reuse accepted C08 DAG, topological-order and reachability mathematics rather than re-author graph theory inside C07.

This amendment changes execution dependency only. Stable scope IDs, topic IDs, names and primary ownership remain unchanged.

## Effective prerequisite set for C07 execution

Base frozen prerequisites retained:

- `B1.1-C01`
- `B1.1-C02`
- `B1.1-C03`

Supplemental accepted foundations required:

- `B1.1-C05` — measure/integration/function-space analytic primitives used by probability/statistics where academically necessary;
- `B1.1-C08` — DAG/graph/order primitives used by causal representation and identifiability reasoning.

C07 must reference these foundations; it must not duplicate their generic learning meaning.

## Mandatory architecture risk controls

### R06 — mathematics vs data/AI

C07 owns mathematical probability, statistics, inference, experimental-design and causal-inference foundations. Future B1.5 data/AI scopes own computational pipelines, machine-learning implementation/model engineering and AI-system objectives. Mathematical foundations are prerequisites/cross-links, never re-taught unchanged in future scopes.

### R13 — AI cross-domain secondary link

Probability/statistics may be a mathematical dependency of AI, but `B1.5-C10` remains primary B1 owner of AI computation. C07 may record an AI secondary link only; it must not author AI-system/cognition/ethics/policy content or transfer ownership.

## C07-T10 causal boundary

C08 owns graph/DAG/topological-order/reachability mathematics. C07-T10 owns causal semantics and inference: causal graphs as causal models, conditional-independence/graphical assumptions, interventions, confounding, identification and design-based causal reasoning within explicit assumptions.

A graph relation alone does not establish a causal relation.

## Stage lock

This amendment authorizes only C07 CURRICULUM authoring after Director-accepted C08 PASS and Sentinel pre-open PASS.

C09/C10 remain locked. No `ACADEMIC_LOCKED`, Lesson Registry, prompt, image, R2, delivery or website artifact is authorized.
