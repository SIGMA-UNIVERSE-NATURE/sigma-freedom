---
title: "HKA W01 — Production Governance & Reference Implementation Contract"
project: "Human Knowledge Academic"
window_id: "W01"
version: "1.0"
status: "ISSUED / CONTRACT_LOCKED"
language: "vi"
date: "2026-09-03"
base_repository: "SIGMA-UNIVERSE-NATURE/sigma-freedom"
base_branch: "hka-knowledge-system-trees"
base_commit_sha: "b2c6b8dacfb425c5e6d260176ed879fb75da6dae"
execution_branch: "hka-tree/w01-production-governance"
brand_repository: "linkcomltd-byte/sigma-universe-web"
brand_asset_commit_sha: "2d3aa9d8418acccd39a3d263e917d4157e029e17"
---

# HKA W01 — PRODUCTION GOVERNANCE & REFERENCE IMPLEMENTATION
## Hợp đồng nhiệm vụ bất biến cho Cửa sổ W01

W01 là cửa sổ nền tảng vận hành đầu tiên của HKA Knowledge System Trees. W01 không phát triển thay một ngành học. W01 xây bộ quy tắc, mẫu hồ sơ và bộ hiệu chuẩn để mọi cửa sổ sau có thể viết prompt CINEMATIC 4K, chia batch, sản xuất, kiểm định và lưu trữ mà không phải tự suy đoán.

---

# I. MỤC TIÊU DUY NHẤT

Tạo một **Reference Implementation có thể thi hành** cho toàn pipeline:

```text
Knowledge Tree Contract
→ Academic Development
→ Visual Coverage
→ Locked Prompt Manifest
→ Batch Handoff
→ Image Production
→ Self-QA
→ Independent QA
→ Cloudflare R2 Release
→ Website Approval later
```

Kết quả W01 phải đủ rõ để một GPT Window khác, một đội sản xuất hình ảnh khác và một QA Window độc lập cùng hiểu giống nhau về:

- phải làm gì;
- không được làm gì;
- tạo bao nhiêu tài sản;
- đặt mã thế nào;
- dựa vào nguồn nào;
- kiểm tra bằng tiêu chí nào;
- báo cáo trạng thái ra sao;
- khi nào phải dừng;
- khi nào một batch mới được xem là hoàn thành.

---

# II. VAI TRÒ VÀ GIỚI HẠN QUYỀN HẠN

## W01 được phép

- Hợp nhất các quy tắc canonical hiện có thành mẫu vận hành thống nhất.
- Tạo template, checklist, decision table và reference files.
- Phát hiện mâu thuẫn, thiếu trường dữ liệu hoặc điểm chưa thể thi hành.
- Ghi đề nghị sửa trong `CHANGE_REQUESTS.md`.
- Thiết kế một bộ 12 prompt hiệu chuẩn CINEMATIC 4K không dùng làm chương trình học chính.
- Tạo batch manifests B00, B01 và B02 cho bộ hiệu chuẩn.
- Commit toàn bộ đầu ra vào nhánh W01.

## W01 không được phép

- Sửa các tài liệu canonical ngoài thư mục W01.
- Thay đổi sáu miền, các Knowledge Tree hoặc Academic Coverage Matrix.
- Phát triển thay W02–W60.
- Tự thay đổi Logo Sigma, MOTTO hoặc hình dạng bốn nhân vật.
- Sản xuất hình ảnh.
- Upload lên Cloudflare R2.
- Tạo hoặc thay đổi website.
- Merge nhánh.
- Giảm tiêu chuẩn canonical.
- Tự giải quyết xung đột bằng cách âm thầm viết lại quy tắc; phải ghi thành change request.

---

# III. NGUỒN PHẢI ĐỌC THEO ĐÚNG THỨ TỰ

W01 phải đọc nguyên văn các tệp sau tại đúng base commit SHA:

```text
1. DOCS/HKA_VISUAL_PRODUCTION_CANONICAL_INDEX.md
2. DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md
3. DOCS/HKA_CINEMATIC_4K_PRODUCTION_STANDARD.md
4. DOCS/HKA_CINEMATIC_4K_BRAND_ASSET_LOCK.md
5. DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_BATCH_PIPELINE.md
6. DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_PIPELINE_AMENDMENT_1_1.md
7. DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-visual-batch-manifest.schema.json
8. DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-production-status.schema.json
9. DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-independent-qa-report.schema.json
10. DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-r2-upload-receipt.schema.json
11. DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-r2-release-record.schema.json
12. DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-release-index.schema.json
```

Mọi nhận xét phải chỉ rõ tệp và mục liên quan. Không được dựa vào ký ức hoặc bản sao ngoài GitHub.

---

# IV. ĐẦU RA BẮT BUỘC

Tất cả đầu ra chỉ được tạo trong:

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W01_PRODUCTION_GOVERNANCE/
```

## A. Bộ điều hành

```text
PRODUCTION_GOVERNANCE_STANDARD.md
WINDOW_CONTRACT_TEMPLATE.md
PROMPT_ASSET_RECORD_TEMPLATE.md
DIRECTORY_NAMING_STANDARD.md
BATCH_HANDOFF_TEMPLATE.md
QA_ACCEPTANCE_MATRIX.md
VISUAL_ART_DIRECTION.md
CHANGE_REQUESTS.md
SELF_AUDIT.md
```

### 1. `PRODUCTION_GOVERNANCE_STANDARD.md`

Phải xác định:

- vai trò Prompt Window, Production Window, QA Window, Release Uploader và Website Publisher;
- decision rights;
- state machine;
- stop conditions;
- rework paths;
- SHA chain;
- Definition of Ready;
- Definition of Done;
- escalation path;
- nguyên tắc không tự suy đoán.

### 2. `WINDOW_CONTRACT_TEMPLATE.md`

Phải là template có thể dùng cho W02–W60, gồm tối thiểu 30 nhóm trường:

1. Window ID;
2. Tree ID;
3. vị trí trong HKA;
4. câu hỏi trung tâm;
5. mục tiêu;
6. phạm vi bắt buộc;
7. phạm vi loại trừ;
8. cành canonical;
9. nền học thuật phải bao phủ;
10. phương pháp đặc thù;
11. nút không được thiếu;
12. vấn đề mở;
13. tranh luận;
14. liên kết xuyên cây;
15. ngộ nhận nguy cơ cao;
16. D1–D4;
17. A1–A5;
18. VCU;
19. gói P12–P36;
20. loại hình;
21. phân bổ nhân vật;
22. Logo và MOTTO;
23. brand asset source;
24. prompt schema;
25. negative prompts;
26. self-audit;
27. acceptance gates;
28. Git paths và branch;
29. handoff receipt;
30. blocked conditions.

### 3. `PROMPT_ASSET_RECORD_TEMPLATE.md`

Phải chứa schema đầy đủ cho một Asset ID, tách rõ:

- academic truth locks;
- learning objective;
- representation type;
- visual composition;
- character role;
- brand-safe area;
- prompt VI;
- prompt EN;
- negative prompt chung;
- negative prompt chuyên ngành;
- source checks;
- filename;
- pass/fail criteria.

### 4. `DIRECTORY_NAMING_STANDARD.md`

Phải khóa:

- repository paths;
- Git branch names;
- Window ID;
- Tree ID;
- Batch ID;
- Run ID;
- Asset ID;
- Release ID;
- filenames;
- R2 prefixes;
- versioning;
- supersede/revoke conventions.

### 5. `BATCH_HANDOFF_TEMPLATE.md`

Phải có bốn biên nhận riêng:

- Prompt Window → Production Window;
- Production Window → QA Window;
- QA Window → Release Uploader;
- Release Uploader → Release Index.

Mỗi biên nhận phải chứa các SHA và số lượng có thể kiểm đếm.

### 6. `QA_ACCEPTANCE_MATRIX.md`

Phải chuyển sáu cổng kiểm định thành ma trận PASS/FAIL/BLOCKED:

- Academic;
- Pedagogy;
- Visual;
- Character & Brand;
- Accessibility;
- Integrity.

Mỗi tiêu chí phải chỉ rõ:

- kiểm cái gì;
- bằng chứng cần xem;
- thế nào là pass;
- thế nào là fail;
- severity P0–P3;
- hành động sửa;
- có cần Run ID mới hay Prompt Commit SHA mới không.

### 7. `VISUAL_ART_DIRECTION.md`

Phải làm rõ CINEMATIC 4K là ngôn ngữ dạy học, không phải mỹ thuật trang trí. Phải khóa:

- documentary credibility;
- scientific/historical accuracy;
- visual hierarchy;
- scale cues;
- camera and lens logic;
- lighting logic;
- age-expression modes A1–A5;
- Research Poster;
- character placement modes;
- logo/motto safe zones;
- no-text generation rule;
- representation labels;
- accessibility;
- visual anti-patterns.

### 8. `CHANGE_REQUESTS.md`

Mỗi vấn đề phải có:

```text
CHANGE REQUEST ID
SOURCE FILE AND SECTION
PROBLEM
RISK IF UNCHANGED
PROPOSED CHANGE
IMPACTED WINDOWS
BACKWARD COMPATIBILITY
DECISION REQUIRED
STATUS: OPEN
```

Không có vấn đề thì ghi rõ `NO CHANGE REQUESTS` và cung cấp lý do đã kiểm tra.

### 9. `SELF_AUDIT.md`

Phải tự kiểm tra:

- đủ đầu ra;
- không sửa file ngoài phạm vi;
- không mâu thuẫn canonical;
- template có thể thi hành;
- schema terms nhất quán;
- số lượng calibration assets chính xác;
- batch mapping chính xác;
- mọi prompt có Asset ID;
- mọi Asset ID có prompt;
- brand references đúng commit/path;
- các phần cần kiểm định độc lập.

## B. Bộ hiệu chuẩn CINEMATIC 4K — khóa P12

W01 không tự chọn gói. W01 bắt buộc dùng:

```text
SELECTED PACKAGE: P12
LOCKED ASSET COUNT: 12
CLEAN MASTER COUNT REQUIRED LATER: 12
BRANDED FINAL COUNT REQUIRED LATER: 12
TOTAL IMAGE FILES REQUIRED LATER: 24
```

W01 chỉ viết prompt và manifest, không sản xuất ảnh.

Phải tạo:

```text
VISUAL_STRATEGY_AND_COUNT.md
VISUAL_COVERAGE_MATRIX.csv
VISUAL_PRODUCTION_MANIFEST.csv
VISUAL_PROMPTS_CINEMATIC_4K.md
VISUAL_QA_CHECKLIST.md
PRODUCTION/BATCHES/HKA-W01-B00/BATCH_MANIFEST.json
PRODUCTION/BATCHES/HKA-W01-B00/BATCH_PROMPTS.md
PRODUCTION/BATCHES/HKA-W01-B01/BATCH_MANIFEST.json
PRODUCTION/BATCHES/HKA-W01-B01/BATCH_PROMPTS.md
PRODUCTION/BATCHES/HKA-W01-B02/BATCH_MANIFEST.json
PRODUCTION/BATCHES/HKA-W01-B02/BATCH_PROMPTS.md
```

---

# V. BỘ 12 ASSET HIỆU CHUẨN ĐÃ KHÓA

Các tài sản này kiểm tra tính nhất quán của visual language; chúng không thay thế nội dung của các Knowledge Tree chuyên môn.

| Asset ID | Batch | Audience | Primary companion | Loại | Mục tiêu hiệu chuẩn |
|---|---|---|---|---|---|
| HKA-VIS-W01-0001 | B00 | Universal | ENSEMBLE_FOUR | HERO | Toàn cảnh HKA; đủ bốn nhân vật; visual hierarchy; brand-safe area |
| HKA-VIS-W01-0002 | B00 | A1 5–8 | SIGMA | DOCUMENTARY / QUESTION | Một hiện tượng đời thường, một câu hỏi rõ, không quá tải |
| HKA-VIS-W01-0003 | B01 | A1 5–8 | LITTLE_ANT | STEP-BY-STEP | Hoạt động quan sát và phân loại theo các bước hữu hình |
| HKA-VIS-W01-0004 | B01 | A2 9–12 | CRICKET | CROSS-LINK | Quan hệ có căn cứ giữa sinh vật, năng lượng và môi trường |
| HKA-VIS-W01-0005 | B01 | A2 9–12 | PROFESSOR_OWL | EVIDENCE | Phân biệt quan sát với suy đoán bằng dấu vết nhìn thấy được |
| HKA-VIS-W01-0006 | B01 | A3 13–15 | PROFESSOR_OWL | SCIENTIFIC_VISUALIZATION | Thử nghiệm scale cue và ranh giới giữa ảnh thật với mô hình |
| HKA-VIS-W01-0007 | B01 | A3 13–15 | CRICKET | HISTORICAL_RECONSTRUCTION | Tái dựng có căn cứ, tránh anachronism và phải ghi rõ là tái dựng |
| HKA-VIS-W01-0008 | B01 | A4 16–18 | LITTLE_ANT | LAB / CONTROLLED VARIABLES | Quy trình thí nghiệm, kiểm soát biến và an toàn phòng lab |
| HKA-VIS-W01-0009 | B02 | A4 16–18 | CRICKET | CONCEPTUAL_SYSTEM_MODEL | Dòng chảy, phản hồi và liên kết; không biến mô hình thành cảnh thật |
| HKA-VIS-W01-0010 | B02 | A5 19–24 | SIGMA | INTERDISCIPLINARY FIELD | Một câu hỏi dẫn nhiều phương pháp nhưng vẫn có phạm vi rõ |
| HKA-VIS-W01-0011 | B02 | A5 19–24 | LITTLE_ANT | REPRODUCIBLE WORKFLOW | Quy trình ghi chép, phiên bản, kiểm tra và tái lập |
| HKA-VIS-W01-0012 | B02 | Research | PROFESSOR_OWL | RESEARCH_POSTER | Phương pháp, dữ liệu, bất định, nguồn và vùng chữ hậu kỳ |

Phân bổ vai chính, không tính HERO ensemble:

```text
SIGMA: 2
CRICKET: 3
LITTLE ANT: 3
PROFESSOR OWL: 3
```

Chênh lệch tối đa bằng 1, đạt chuẩn.

Mỗi asset phải dùng chính xác master references tại:

```text
Repository: linkcomltd-byte/sigma-universe-web
Commit: 2d3aa9d8418acccd39a3d263e917d4157e029e17

assets/characters/sigma.png
assets/characters/cricket.png
assets/characters/little-ant.png
assets/characters/professor-owl.png
assets/logo/sigma-logo-master.jpg
assets/logo/sigma-emblem-shell.jpg
```

Exact MOTTO:

```text
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

---

# VI. YÊU CẦU PROMPT CHO TỪNG ASSET

Mỗi Asset ID phải có đầy đủ:

```text
ASSET ID
WINDOW ID
BATCH ID
VCU ID
TITLE
PURPOSE OF CALIBRATION
LEARNING OBJECTIVE
PRIMARY AUDIENCE
ACADEMIC DEPTH
ASSET TYPE
REPRESENTATION TYPE
WHAT IS OBSERVABLE REALITY
WHAT IS MODEL / RECONSTRUCTION / METAPHOR
PRIMARY COMPANION
SECONDARY COMPANIONS
EXACT CHARACTER MASTER PATHS
CHARACTER PLACEMENT MODE
SCENE DESCRIPTION
MANDATORY OBJECTS
FORBIDDEN OBJECTS
SPATIAL RELATIONS
SCALE CUES
PROCESS ORDER, IF ANY
COMPOSITION
CAMERA AND LENS
LIGHTING
DEPTH OF FIELD
FUNCTIONAL COLOR LOGIC
BRAND SAFE AREA
LOGO PLACEMENT
MOTTO PLACEMENT
PROMPT VI
PROMPT EN
GLOBAL NEGATIVE PROMPT
ASSET-SPECIFIC NEGATIVE PROMPT
ACADEMIC / HISTORICAL ACCURACY LOCKS
CAPTION
ALT TEXT
SOURCE CHECKS
OUTPUT SIZE
CLEAN MASTER FILENAME
BRANDED FINAL FILENAME
PASS CRITERIA
FAIL CRITERIA
```

Không được dùng từ mơ hồ như “đẹp”, “ấn tượng”, “phù hợp” nếu không mô tả tiêu chí quan sát được.

---

# VII. BATCH LOCK

```text
HKA-W01-B00: 2 assets — 0001–0002
HKA-W01-B01: 6 assets — 0003–0008
HKA-W01-B02: 4 assets — 0009–0012
```

Run đầu tiên:

```text
HKA-W01-B00-R01
HKA-W01-B01-R01
HKA-W01-B02-R01
```

Mỗi batch manifest phải:

- hợp `hka-visual-batch-manifest.schema.json`;
- ghi đúng Prompt Commit SHA sau commit cuối;
- có prompt SHA-256 cho từng asset;
- không trộn commit;
- không thêm asset ngoài bảng khóa.

Nếu việc tạo Prompt Commit SHA cuối khiến manifest cần cập nhật SHA, W01 phải dùng quy trình hai commit rõ ràng và ghi `FINAL_PROMPT_COMMIT_SHA` trong Handoff Receipt; không được dùng placeholder trong bàn giao cuối.

---

# VIII. CÁC CỔNG NGHIỆM THU W01

## Gate 1 — Scope

PASS khi mọi file nằm trong thư mục W01 và không sửa canonical files.

## Gate 2 — Executability

PASS khi một GPT khác có thể thực hiện template mà không phải hỏi lại thuật ngữ, số lượng, đường dẫn hoặc tiêu chí nghiệm thu.

## Gate 3 — Internal consistency

PASS khi ID, status, filenames, batch size, SHA fields và R2 paths nhất quán giữa mọi template.

## Gate 4 — Visual production precision

PASS khi 12 prompt có thể chuyển trực tiếp cho Production Windows mà không phải tự bổ sung bố cục, nhân vật, brand, output hoặc negative prompt.

## Gate 5 — Brand integrity

PASS khi dùng đúng repo, commit, exact paths và exact MOTTO.

## Gate 6 — Auditability

PASS khi có thể truy từ một Asset ID về prompt, manifest, commit, batch, run, QA và release record.

## Gate 7 — No silent conflict resolution

PASS khi mọi xung đột canonical được ghi vào `CHANGE_REQUESTS.md`, không tự sửa âm thầm.

---

# IX. GIT PROTOCOL

```text
Repository:
SIGMA-UNIVERSE-NATURE/sigma-freedom

Execution branch:
hka-tree/w01-production-governance

Allowed write prefix:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W01_PRODUCTION_GOVERNANCE/

Commit convention:
docs(hka-w01): <imperative description>
```

Không merge. Không tạo release. Không upload R2. Không chạm `sigmastudy.net`.

---

# X. LỆNH DỪNG BẮT BUỘC

W01 phải trả `BLOCKED` thay vì suy đoán nếu:

- không đọc được một nguồn canonical bắt buộc;
- base commit SHA không tồn tại;
- brand asset commit hoặc exact path không tồn tại;
- hai tài liệu canonical mâu thuẫn mà không xác định được thứ bậc hiệu lực;
- JSON schema không thể biểu diễn một trường bắt buộc;
- không thể khóa số lượng 12 asset;
- manifest cuối còn placeholder SHA;
- có yêu cầu sản xuất ảnh, upload R2, merge hoặc deploy production.

Khi BLOCKED, phải ghi:

```text
BLOCKER ID
SOURCE
AFFECTED OUTPUTS
WHY EXECUTION CANNOT CONTINUE SAFELY
REQUIRED DECISION
```

---

# XI. BIÊN NHẬN HOÀN THÀNH

Phản hồi cuối của W01 phải có đúng cấu trúc:

```text
WINDOW ID: W01
STATUS: COMPLETE / BLOCKED
REPOSITORY:
BRANCH:
BASE COMMIT SHA:
FINAL COMMIT SHA:

FILES CREATED:
FILES MODIFIED OUTSIDE ALLOWED PREFIX: 0

GOVERNANCE DOCUMENT COUNT:
CALIBRATION ASSET COUNT: 12
BATCH COUNT: 3
PROMPT COUNT: 12
MANIFEST COUNT: 3
CHANGE REQUEST COUNT:

B00 STATUS:
B01 STATUS:
B02 STATUS:

BRAND REPOSITORY VERIFIED: YES / NO
BRAND ASSET COMMIT VERIFIED: YES / NO
EXACT MOTTO VERIFIED: YES / NO

SCHEMA VALIDATION:
BATCH MANIFESTS VALID: YES / NO
PLACEHOLDER SHA REMAINING: 0

OPEN RISKS:
EXPERT / ARCHITECT REVIEW REQUIRED:

DO NOT MERGE.
DO NOT PRODUCE IMAGES.
DO NOT UPLOAD TO R2.
DO NOT DEPLOY WEBSITE.
```

---

# XII. DEFINITION OF DONE

W01 chỉ hoàn thành khi:

- tạo đủ toàn bộ file bắt buộc;
- 12 Asset IDs xuất hiện đúng một lần trong production manifest;
- 12 Asset IDs đều có prompt hoàn chỉnh;
- B00/B01/B02 đúng 2/6/4 assets;
- mọi template dùng thuật ngữ thống nhất;
- không còn placeholder trong hồ sơ bàn giao cuối;
- mọi brand reference đúng commit/path;
- mọi change request được công khai;
- Self Audit không che giấu vấn đề;
- không có thay đổi ngoài allowed prefix;
- final commit SHA được báo cáo;
- trạng thái vẫn là nhánh chờ kiểm định, chưa merge.

> **W01 không được đánh giá bằng độ dài. W01 được đánh giá bằng việc những cửa sổ sau có thể làm đúng ngay từ lần đầu hay không.**
