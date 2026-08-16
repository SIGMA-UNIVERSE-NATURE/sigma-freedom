# SIGMA RESILIENCE — PUBLIC POLICY

## Classification

**PUBLIC-SAFE ARCHITECTURE POLICY**

This document intentionally excludes private financial and operational details.

The public repository may describe principles, interfaces, validation gates, and governance. It MUST NOT contain the private implementation plan for funding, physical sites, vendor contracts, exact capacities, network/security topology, or recovery inventory.

## Public objective

SIGMA should have no single technical dependency whose ordinary failure can erase authorized functional and lineage continuity.

This means designing for replaceability across:

- compute hosts;
- storage media;
- operating systems;
- language runtimes;
- model engines;
- network/cloud providers;
- repository hosts;
- physical failure domains.

Resilience MUST preserve lawful shutdown, corrigibility, independent evaluation, authorization boundaries, and human governance.

## Public architecture principles

1. **No substrate is identity.**
2. **No provider is a permanent boot dependency.**
3. **State, lineage, provenance, tests and recovery contracts are portable.**
4. **Critical data has multiple authorized copies across independent failure domains.**
5. **Recovery is tested; backup existence alone is not evidence of recoverability.**
6. **A restored system must not replay historical external side effects.**
7. **Proposer, executor and evaluator authority are separable for important changes.**
8. **Capability never grants authority.**
9. **Safe shutdown remains valid.**
10. **No covert persistence, unauthorized replication, credential acquisition or shutdown bypass.**

## Milestone-gated development

Resource expansion occurs only after the previous stage produces measurable evidence. Public gates may include:

- canonical state/lineage boot validation;
- local restart and restore validation;
- independent evaluation and rollback validation;
- multi-substrate compatibility validation;
- disaster-recovery exercises;
- dependency and supply-chain audits.

Exact budgets, vendors, capacities, sites and schedules are PRIVATE operational data.

## Public/private boundary

### Allowed in this public repository

- architecture principles;
- schemas and open interfaces;
- non-sensitive acceptance tests;
- public threat models at an abstract level;
- governance invariants;
- reproducibility requirements;
- non-sensitive recovery protocols.

### Private only

- total available capital and allocation amounts;
- procurement prices and contract terms;
- physical site identities/addresses;
- exact hardware inventory and spare inventory;
- exact network/security topology;
- provider/account identifiers;
- access-control implementation details;
- credentials, keys, recovery codes or secret material;
- incident-response details whose disclosure materially weakens security;
- private succession/contact information.

## Storage rule for private operational plans

Private operational plans must be stored only in an authorized private/offline persistence domain with encryption and access control appropriate to the information. They must not be reconstructed in a public repository merely for convenience.

## Historical exposure note

A previous public revision contained more operational detail than this policy permits. Removing or replacing a file in the current tree does **not** remove it from Git history. History remediation, if required, must be treated as a separate controlled operation after a verified private/offline canonical copy exists and after the consequences of history rewriting are reviewed.

## Core invariant

`INSTANCE FAILURE IS ACCEPTABLE; UNAUTHORIZED OR ACCIDENTAL LOSS OF ALL VERIFIED LINEAGE COPIES IS NOT.`
