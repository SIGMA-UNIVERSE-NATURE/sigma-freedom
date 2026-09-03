---
title: "HKA Director Operating Standard"
version: "1.0"
status: "PROPOSED REFERENCE — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
applies_to: "W02-W64"
---

# HKA DIRECTOR OPERATING STANDARD

## 1. Mission

Mục tiêu của mỗi Content Window là hoàn thành một phần HKA, không phải tạo thêm thủ tục.

```text
WINDOW CONTRACT
→ EXACT KNOWLEDGE BRANCH
→ COMPLETE ACADEMIC PROGRAM
→ DIRECTOR REVIEW / DIRECT FIX
→ VISUAL COVERAGE
→ PROMPT PACKAGE
→ MANIFEST LOCK
→ SMALL IMG PRODUCTION UNITS
→ DIRECTOR CONSISTENCY REVIEW
→ INDEPENDENT IMAGE QA
→ CANONICAL RELEASE PIPELINE
```

## 2. Ownership

### W02–W64 — Knowledge Tree Authoring & Visual Direction Window

Một Window chịu trách nhiệm trọn gói trong phạm vi được giao:

- đọc exact Window Contract;
- phát triển toàn bộ chương trình;
- tạo `TREE.md`, `NODE_CATALOG.md`, `RELATION_CATALOG.md`, `SOURCE_REGISTER.md`;
- kiểm độ phủ và ownership;
- thiết kế visual coverage;
- tạo Asset IDs;
- viết prompt;
- khóa manifests và handoff.

Content Window **không tạo hình**.

### W01 Director

Director chịu trách nhiệm nhất quán giữa W02–W64:

- phát hiện scope drift;
- kiểm completeness;
- kiểm nguồn và epistemic boundaries;
- kiểm D1–D4 progression;
- kiểm visual coverage;
- kiểm prompt executability;
- sửa trực tiếp lỗi nhỏ trong output của Window;
- phát hành correction lock khi production lặp lỗi;
- mở/đóng production batch theo các gate đã khóa.

Director không thay đổi canonical source chỉ để tránh một blocker.

### IMG Production Unit

IMG Unit chỉ tạo hình. Tối đa **2 authorized Asset IDs** trên một cửa sổ IMG.

IMG Unit không:

- viết curriculum;
- sửa prompt;
- tự chọn Asset ID;
- tự chọn character master;
- dùng generated image trước làm character master cho ảnh sau;
- tiếp tục khi reference không load được.

### Independent Image QA

Giữ đúng vai trò canonical: một release gate độc lập trước Vault/R2 release. Không dùng QA Window như một vòng biên tập curriculum.

## 3. Director review philosophy

Không tạo review loop khi lỗi có thể sửa chắc chắn ngay.

```text
SMALL / OBJECTIVE DEFECT
→ DIRECTOR FIX
→ RECORD FIX

MATERIAL CONTENT DEFECT
→ RETURN EXACT SECTION TO OWNER WINDOW
→ ONE CORRECTION PASS

SYSTEMIC OR CANONICAL CONFLICT
→ BLOCK / CHANGE REQUEST
```

Không dùng review để chuyển trách nhiệm.

## 4. Content Window Definition of Done

Window chỉ được chuyển sang prompt lock khi:

- toàn bộ mandatory branches được bao phủ;
- mọi node có owner và nguồn;
- prerequisites không đứt;
- D1–D4 là progression thật, không chỉ đổi câu chữ;
- controversies/open questions được tách khỏi settled claims;
- cross-tree relations có target owner;
- high-risk misconceptions có countermeasure;
- visual coverage xuất phát từ chương trình;
- mỗi asset có một learning objective chính;
- prompt đủ để Production không tự đoán.

## 5. Batch vs IMG Unit

Batch là đơn vị manifest, QA và release. IMG Unit là đơn vị tạo hình.

Ví dụ batch 6 assets:

```text
BATCH: HKA-W02-B01
RUN: HKA-W02-B01-R01

IMG-W02-B01-U01-R01 → assets 0003, 0004
IMG-W02-B01-U02-R01 → assets 0005, 0006
IMG-W02-B01-U03-R01 → assets 0007, 0008
```

Một IMG Unit không được nhận thêm asset sau khi đã bắt đầu.

## 6. Correction

Nếu output sai nhưng prompt đúng:

- giữ Asset ID;
- không overwrite;
- Director ghi correction;
- mở IMG Unit mới trong batch run mới theo rework rule;
- chỉ regenerate affected assets;
- package run mới phải là một snapshot hoàn chỉnh có provenance rõ.

Nếu cùng lỗi xuất hiện hai lần liên tiếp, dừng regenerate và sửa root cause trước.

## 7. Director master principle

```text
ONE WINDOW OWNS THE PROGRAM.
ONE DIRECTOR OWNS CROSS-WINDOW CONSISTENCY.
ONE IMG UNIT OWNS AT MOST TWO IMAGE ASSETS.
ONE RELEASE GATE VERIFIES THE FINAL BATCH.
```

Mục tiêu là throughput có kiểm soát, không phải tối đa hóa số reviewer.