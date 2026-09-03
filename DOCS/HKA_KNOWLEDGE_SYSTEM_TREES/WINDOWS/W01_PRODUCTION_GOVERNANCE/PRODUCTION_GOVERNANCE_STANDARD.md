---
title: "HKA W01 — Production Governance Standard"
window_id: "W01"
version: "2.0"
status: "DIRECTOR-INTEGRATED REFERENCE — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — PRODUCTION GOVERNANCE STANDARD

## 1. Mission

W01 là lớp đạo diễn vận hành. Mục tiêu là để W02–W64 nhận đúng nhánh, viết trọn chương trình, chuyển chương trình thành visual package và giao các đơn vị IMG nhỏ để sản xuất ổn định.

```text
Canonical standards
→ Window Contract
→ Complete academic program
→ Director Academic Gate
→ Visual strategy / VCU / locked count
→ Prompt records
→ Director Visual Gate
→ Batch manifests
→ IMG Production Units (max 2 assets/unit)
→ Director Production Consistency Review
→ Independent Image QA
→ R2 release
→ Website approval later
```

Không tạo thêm reviewer nếu Director có thể sửa một lỗi nhỏ, khách quan và truy vết được.

## 2. Authority and precedence

Canonical precedence giữ nguyên:

1. higher-version amendment;
2. current JSON Schema for the record;
3. Brand Asset Lock;
4. Cloudflare Batch Pipeline;
5. CINEMATIC 4K Production Standard;
6. locked Window Contract;
7. Window-created content.

Director Layer không tự sửa canonical conflict. Conflict có tính canonical phải được ghi change request.

## 3. Roles

### 3.1 Canonical Architect

- khóa Window Contract và canonical scope;
- phê duyệt/return Director Layer và Window output;
- quyết định canonical changes, merge, release infrastructure và website authorization.

### 3.2 W01 Director

- sở hữu cross-window consistency cho W02–W64;
- kiểm academic completeness và visual coherence;
- sửa trực tiếp lỗi nhỏ/khách quan trong Window output;
- trả đúng section về owner Window nếu cần material academic rewrite;
- phát hành Director correction locks cho production;
- không tự tuyên bố Architect acceptance.

### 3.3 W02–W64 Knowledge Tree Authoring & Visual Direction Window

Một Window làm trọn:

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
full academic program
visual strategy
VCUs
Asset IDs
prompt records
batch prompts
manifests
handoff
```

Content Window không sản xuất hình.

### 3.4 IMG Production Unit

IMG Unit chỉ generate đúng 1–2 authorized Asset IDs.

- nhận exact execution pack;
- reread immutable source trước mỗi asset;
- reload official visual references trước mỗi relevant asset;
- generate CLEAN MASTER trước;
- chỉ post-composite Logo/MOTTO sau clean pass;
- self-check trước asset kế;
- close unit sau tối đa 2 assets.

Không sửa curriculum/prompt và không dùng generated image trước làm character master cho image sau.

### 3.5 Independent Image QA

Đây là release gate độc lập của canonical pipeline. QA kiểm full batch snapshot và không biên tập curriculum/prompt/image.

### 3.6 Release Uploader / Website Publisher

Giữ đúng canonical pipeline và Amendment 1.1. Director Layer không mở R2 staging bằng quy tắc ngầm.

## 4. Academic Definition of Done

Trước Visual Strategy, Window phải có:

- 100% mandatory branch coverage;
- explicit excluded scope/owner;
- no orphan core prerequisites;
- source support for material claims;
- epistemic status for uncertainty/debate/open questions;
- D1–D4 progression thực chất;
- high-risk misconceptions và countermeasures;
- cross-tree ownership rõ.

Result:

```text
DIRECTOR ACADEMIC GATE: PASS
```

## 5. Visual Definition of Done

Trước Prompt Lock:

- mọi VCU trace về node đã khóa;
- mỗi asset có một primary learning objective;
- package P12/P18/P24/P30/P36 có rationale;
- spiral/continuity được ghi trong Program-to-Visual Director Brief;
- không decorative-only asset;
- prompt record đầy đủ;
- official brand references exact;
- prompt ↔ manifest 1:1;
- IMG unit assignments không quá 2 asset.

Result:

```text
DIRECTOR VISUAL GATE: PASS
```

## 6. Batch and IMG Unit model

Batch vẫn là canonical manifest/QA/release unit, tối đa 6 assets.

IMG Unit là execution unit:

```text
HKA-W02-B01-R01
├── IMG-W02-B01-U01-R01 → 0003,0004
├── IMG-W02-B01-U02-R01 → 0005,0006
└── IMG-W02-B01-U03-R01 → 0007,0008
```

B00 = 2 assets = one IMG Unit by default.

Không giao thêm asset vào IMG Unit sau khi nó bắt đầu.

## 7. Anti-drift production rule

Trước MỖI Asset ID, IMG Unit phải:

1. reread exact asset record;
2. verify prompt SHA;
3. reload official character references;
4. reread mandatory/forbidden objects;
5. reread PASS/FAIL;
6. generate and close asset before next asset.

Không dùng “same as previous”, memory của IMG Window hoặc generated output trước làm source of truth.

Nếu official reference không load được:

```text
ASSET_REFERENCE_BLOCKED
```

## 8. Correction and repeated-error control

Nếu prompt đúng nhưng output sai:

```text
OUTPUT_ERROR
→ do not overwrite
→ Director correction record
→ new canonical Run ID per existing rework rule
→ fresh IMG Unit for affected assets
```

Nếu cùng failure lặp hai lần liên tiếp:

```text
STOP REGENERATING
→ diagnose prompt/reference/model/composition root cause
→ fix root cause
→ only then authorize another run
```

## 9. State model

Canonical release state machine giữ nguyên. Director adds pre-production gates, không thay schema enum trừ khi canonical schema được versioned.

Logical flow:

```text
DRAFT
→ ACADEMIC PROGRAM COMPLETE
→ DIRECTOR ACADEMIC PASS
→ VISUAL/PROMPT PACKAGE COMPLETE
→ DIRECTOR VISUAL PASS
→ PROMPT_LOCKED
→ BATCH_READY
→ IMG UNIT CLAIMED
→ PRODUCING
→ SELF_QA
→ DIRECTOR PRODUCTION REVIEW
→ QA_REVIEW
→ QA_APPROVED / QA_REJECTED / QA_BLOCKED
→ canonical R2 flow
```

Machine-readable status records phải dùng enum hiện hành; Director-only gates được ghi trong Director records nếu schema chưa có field tương ứng.

## 10. SHA chain

Mỗi release phải truy được tối thiểu:

```text
CANONICAL BASE COMMIT SHA
WINDOW CONTRACT COMMIT SHA
ACADEMIC CONTENT COMMIT SHA / exact academic paths when adopted by Window
PROMPT CONTENT COMMIT SHA
FINAL MANIFEST COMMIT SHA
BRAND ASSET COMMIT SHA
PROMPT SHA-256
MANIFEST SHA-256
CLEAN MASTER SHA-256
BRANDED FINAL SHA-256
BATCH PACKAGE SHA-256
QA REPORT SHA-256
R2 UPLOAD RECEIPT SHA-256
R2 RELEASE AUDIT RECORD SHA-256
RELEASE INDEX
```

Prompt/manifest two-commit rule từ W01 accepted baseline giữ nguyên.

## 11. Director direct-fix rule

Director được sửa trực tiếp khi defect:

- nhỏ;
- objectively verifiable;
- không thay canonical scope;
- không thay material academic claim mà chưa có source review;
- có thể rehash/version đúng sau sửa.

Material content rewrite trả đúng phần về owner Window một lần, không tạo chuỗi reviewer.

## 12. R2 boundary

Current canonical buckets remain:

```text
hka-c4k-vault
hka-c4k-audit
hka-c4k-delivery
```

`hka-c4k-staging` chỉ là candidate change request trong `DIRECTOR_CHANGE_REQUESTS.md`, không phải active rule.

## 13. Stop conditions

Dừng khi:

- source/commit/hash mismatch;
- scope ownership không giải quyết được;
- high-risk academic claim thiếu nguồn;
- IMG Unit >2 assets;
- official visual reference cần thiết không load được;
- generated output bị dùng làm character master kế tiếp;
- same production failure lặp hai lần mà chưa root-cause review;
- request R2/merge/deploy vượt authority.

## 14. Final responsibility

```text
CONTENT WINDOW OWNS THE PROGRAM.
DIRECTOR OWNS CROSS-WINDOW CONSISTENCY.
IMG UNIT OWNS AT MOST TWO IMAGE ASSETS.
INDEPENDENT QA OWNS RELEASE VERDICT.
ARCHITECT OWNS FINAL REFERENCE ACCEPTANCE.
```

Mục tiêu là làm đúng ngay, sửa nhanh khi cần và tiếp tục sản xuất; không tối ưu cho số lượng hồ sơ hoặc số vòng kiểm tra.