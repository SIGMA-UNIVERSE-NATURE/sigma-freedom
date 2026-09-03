---
title: "HKA W01 — Architect Reference Provenance"
window_id: "W01"
version: "1.0"
status: "ARCHITECT_REFERENCE / PENDING W01 INDEPENDENT VALIDATION"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — ARCHITECT REFERENCE PROVENANCE

## 1. Mục đích

Tài liệu này làm rõ nguồn gốc của toàn bộ gói triển khai hiện có trên nhánh:

```text
hka-tree/w01-architect-reference
```

Các tài liệu governance, CINEMATIC 4K prompt records, manifests, hash payloads, QA matrices và production handoff files trong nhánh này được xây dựng bởi **Canonical Architect / President session**, không phải bởi delegated GPT Window W01.

## 2. Hai provenance phải tách biệt

### A. Delegated W01 official execution

```text
Branch:
hka-tree/w01-production-governance

Authoritative delegated-window result:
STATUS: BLOCKED
MANDATORY FILES CREATED BY W01: 0
PROMPT RECORDS CREATED BY W01: 0
BATCH MANIFESTS CREATED BY W01: 0
CONTENT COMMIT SHA: NOT CREATED
FINAL MANIFEST COMMIT SHA: NOT CREATED
```

Blocker:

```text
HKA-W01-BLK-001
Delegated W01 environment lacked authenticated GitHub write capability.
```

### B. Architect Reference Implementation

```text
Branch:
hka-tree/w01-architect-reference

Source restoration commit:
5ed62129b8eae603d9d9917ca57a46a03361c909

AUTHORSHIP:
Canonical Architect / President session

PURPOSE:
A complete reference implementation for later Window Contracts and visual-production governance.
```

This work is valid project work and must not be deleted merely because it was not authored by W01.

## 3. Correct use of the Architect Reference

The Architect Reference may be used to:

- establish production-governance patterns;
- provide templates for later Window Contracts;
- provide candidate CINEMATIC 4K visual prompt structures;
- provide candidate batch/manifest/handoff structures;
- provide candidate QA gates and naming conventions;
- serve as material for independent review by W01 and later reviewers.

It must **not** be represented as if W01 created it.

## 4. Independent W01 validation requirement

Before any Architect Reference prompt or batch is promoted into production-authorized status, W01 must independently review the Architect Reference and return one of:

```text
VALIDATED
VALIDATED_WITH_CORRECTIONS
REJECTED
BLOCKED
```

The W01 reviewer should evaluate content, consistency, scope, prompt precision, brand locks, batch counts, SHA semantics, QA gates and production safety.

W01 does not need GitHub write capability to perform this validation. Read access is sufficient if it can inspect the immutable branch/commit and return a detailed report.

## 5. Production boundary

Until W01 validation is received and reviewed by the Architect:

```text
ARCHITECT REFERENCE: ACTIVE AND PRESERVED
B00 PRODUCTION: SUSPENDED
B01 PRODUCTION: SUSPENDED
B02 PRODUCTION: SUSPENDED
R2 UPLOAD: NOT AUTHORIZED
MERGE TO CANONICAL BASE: NOT AUTHORIZED
WEBSITE DEPLOYMENT: NOT AUTHORIZED
SIGMASTUDY.NET PRODUCTION: HOLD
```

This suspension protects quality while preserving all work.

## 6. Provenance rule for future work

Every future artifact must explicitly state one of:

```text
AUTHOR: CANONICAL ARCHITECT
AUTHOR: WINDOW WXX
AUTHOR: IMAGE PRODUCTION WINDOW <ID>
AUTHOR: INDEPENDENT QA WINDOW <ID>
AUTHOR: RELEASE UPLOADER
```

Reviewers must never infer authorship from folder name alone.

## 7. Governance principle

```text
Architect may design and build reference implementations.
Windows may independently develop or validate assigned work.
QA validates output independently.
Provenance must stay explicit at every layer.
```

The objective is not to prevent the Architect from creating high-value work. The objective is to prevent authorship and validation roles from being confused.
