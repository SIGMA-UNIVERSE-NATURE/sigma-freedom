---
title: "HKA W01 — Architect Acceptance Gate"
window_id: "W01"
version: "1.0"
status: "REVIEW STANDARD"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — ARCHITECT ACCEPTANCE GATE
## Tiêu chuẩn để kiến trúc sư HKA kiểm định kết quả W01

Tài liệu này không phải đầu ra do W01 tự chấm. Đây là bộ tiêu chí độc lập dùng sau khi W01 báo hoàn thành.

Một mục chỉ được đánh `PASS` khi có bằng chứng trực tiếp trong GitHub. Không dùng lời tuyên bố của cửa sổ thay cho việc đọc file và xác minh commit.

---

# GATE A — SOURCE & SCOPE INTEGRITY

| ID | Điều kiện | Bằng chứng bắt buộc | Kết quả |
|---|---|---|---|
| A01 | Đúng repository | Git metadata | PASS/FAIL |
| A02 | Đúng branch `hka-tree/w01-production-governance` | Branch ref | PASS/FAIL |
| A03 | Dựa trên base commit `b2c6b8...` | Commit ancestry | PASS/FAIL |
| A04 | Contract `7d1d77...` đã được đọc và giữ nguyên | File/receipt reference | PASS/FAIL |
| A05 | Không sửa file ngoài allowed prefix | Compare base...head | PASS/FAIL |
| A06 | Không merge, release, R2 upload hoặc deploy | Git/receipt evidence | PASS/FAIL |

**Gate A chỉ PASS khi A01–A06 đều PASS.**

---

# GATE B — GOVERNANCE PACK COMPLETENESS

Các file sau phải tồn tại và có nội dung thi hành được:

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

| ID | Kiểm tra | Pass khi |
|---|---|---|
| B01 | File count | Đủ 9 file, đúng tên |
| B02 | Governance roles | Mỗi vai trò có input, output, quyền và cấm rõ |
| B03 | State machine | Không nhảy trạng thái; rework path rõ |
| B04 | Window contract template | Có đủ tối thiểu 30 nhóm trường |
| B05 | Prompt template | Có đủ academic, pedagogy, visual, brand, output, QA fields |
| B06 | Naming | Không có hai quy ước xung đột cho cùng mã |
| B07 | Handoff | Mỗi bước có biên nhận và SHA chain |
| B08 | QA matrix | Có PASS/FAIL/BLOCKED, P0–P3 và hành động sửa |
| B09 | Art direction | Có tiêu chí quan sát được, không chỉ mô tả phong cách |
| B10 | Change requests | Mọi mâu thuẫn được công khai hoặc xác nhận không có |
| B11 | Self audit | Nêu cả rủi ro, không chỉ tuyên bố đạt |

**Gate B chỉ PASS khi B01–B11 đều PASS.**

---

# GATE C — CALIBRATION PACKAGE COMPLETENESS

Các file bắt buộc:

```text
VISUAL_STRATEGY_AND_COUNT.md
VISUAL_COVERAGE_MATRIX.csv
VISUAL_PRODUCTION_MANIFEST.csv
VISUAL_PROMPTS_CINEMATIC_4K.md
VISUAL_QA_CHECKLIST.md
3 × BATCH_MANIFEST.json
3 × BATCH_PROMPTS.md
```

| ID | Kiểm tra | Pass khi |
|---|---|---|
| C01 | Package | P12 chính xác |
| C02 | Asset count | 12 Asset IDs duy nhất |
| C03 | Batch map | B00=2, B01=6, B02=4 |
| C04 | Prompt count | Đúng 12 hồ sơ prompt |
| C05 | Prompt completeness | Không thiếu trường bắt buộc |
| C06 | Manifest count | Đúng 3 manifest |
| C07 | Manifest/schema | Cấu trúc hợp schema hiện hành |
| C08 | Prompt ↔ manifest | Quan hệ 1:1, không dư, không thiếu |
| C09 | Filename | Clean/branded filename đúng ID |
| C10 | Output count | Khóa 12 clean + 12 branded = 24 files |
| C11 | Placeholder | Không còn placeholder trong handoff cuối |

**Gate C chỉ PASS khi C01–C11 đều PASS.**

---

# GATE D — PEDAGOGICAL & VISUAL PRECISION

Lấy mẫu 100% cả 12 prompt, không lấy mẫu thống kê.

| ID | Kiểm tra | Pass khi |
|---|---|---|
| D01 | Learning objective | Mỗi asset có đúng một mục tiêu chính |
| D02 | Audience | Đúng phân bổ Universal/A1/A2/A3/A4/A5/Research |
| D03 | Depth | D1–D4 hoặc Multi-depth được giải trình |
| D04 | Representation | Reality/model/reconstruction/metaphor phân biệt rõ |
| D05 | Scene control | Vật thể bắt buộc và cấm được chỉ rõ |
| D06 | Spatial logic | Quan hệ không gian và scale cue có thể kiểm tra |
| D07 | Process logic | Trình tự không bị đảo hoặc mơ hồ |
| D08 | Cinematic design | Camera, lens, lighting phục vụ nội dung |
| D09 | Cognitive load | Không ghép quá nhiều mục tiêu hoặc chi tiết |
| D10 | Negative prompts | Có global và asset-specific controls |
| D11 | Caption/alt text | Chính xác, không phóng đại, dùng được trên website |
| D12 | Pass/fail | Có tiêu chí đủ cụ thể để từ chối output sai |

**Gate D chỉ PASS khi D01–D12 đều PASS cho cả 12 asset.**

---

# GATE E — CHARACTER & BRAND LOCK

| ID | Kiểm tra | Pass khi |
|---|---|---|
| E01 | Brand repo | `linkcomltd-byte/sigma-universe-web` |
| E02 | Brand commit | Chính xác `2d3aa9...` |
| E03 | Character paths | Đúng bốn PNG master paths |
| E04 | Logo paths | Đúng master và compact emblem paths |
| E05 | MOTTO | Đúng từng ký tự, dấu gạch nối và dấu chấm cuối |
| E06 | Hero | Asset 0001 có đủ bốn nhân vật |
| E07 | Lead distribution | Sigma 2, Cricket 3, Little Ant 3, Owl 3; hero ensemble riêng |
| E08 | Role fitness | Nhân vật có vai học thuật, không trang trí |
| E09 | Placement mode | In-scene/observer/guide hợp với loại hiện tượng |
| E10 | No generated brand text | Prompt cấm model tự sinh logo/MOTTO |
| E11 | Brand-safe area | Có vùng hậu kỳ rõ, không che nội dung |

**Sai MOTTO hoặc asset source là P0 và Gate E FAIL ngay lập tức.**

---

# GATE F — SHA, VERSION & TRACEABILITY

| ID | Kiểm tra | Pass khi |
|---|---|---|
| F01 | Base SHA | Được ghi và xác minh |
| F02 | Contract SHA | Được ghi và xác minh |
| F03 | Content commit SHA | Tồn tại trên branch |
| F04 | Final manifest commit SHA | Tồn tại trên branch |
| F05 | Prompt SHA-256 | Có cho 12 prompt |
| F06 | Manifest SHA-256 | Có sidecar/registry theo rule |
| F07 | Batch ownership | Mỗi asset thuộc đúng một batch |
| F08 | Run IDs | B00/B01/B02 dùng R01 đúng cấu trúc |
| F09 | No mixed prompt commit | Mỗi batch chỉ trỏ một prompt commit |
| F10 | End-to-end trace | Asset ID → prompt → commit → manifest → batch → expected files |

**Gate F chỉ PASS khi F01–F10 đều PASS.**

---

# GATE G — REFERENCE VALUE FOR LATER WINDOWS

Kiểm tra thực tế bằng cách dùng template W01 để dựng thử một window contract giả lập, không commit, cho một cây chuyên môn.

| ID | Kiểm tra | Pass khi |
|---|---|---|
| G01 | Không cần tự phát minh trường | Template bao phủ mọi input cần thiết |
| G02 | Không cần hỏi lại số lượng | Hệ VCU và package decision rõ |
| G03 | Không cần hỏi lại brand | Repo/commit/path/MOTTO rõ |
| G04 | Không cần hỏi lại Git | Branch/path/commit/handoff rõ |
| G05 | Không cần hỏi lại QA | Acceptance criteria rõ |
| G06 | Không có xung đột thuật ngữ | Các template dùng cùng vocabulary |
| G07 | Không khóa sáng tạo đúng chỗ | Cửa sổ vẫn có quyền thiết kế trải nghiệm trong ranh giới sự thật |

**Gate G là thước đo quan trọng nhất: W01 chỉ có giá trị khi các cửa sổ sau dùng được.**

---

# KẾT LUẬN KIỂM ĐỊNH

```text
GATE A: PASS/FAIL
GATE B: PASS/FAIL
GATE C: PASS/FAIL
GATE D: PASS/FAIL
GATE E: PASS/FAIL
GATE F: PASS/FAIL
GATE G: PASS/FAIL

P0 COUNT:
P1 COUNT:
P2 COUNT:
P3 COUNT:

FINAL DECISION:
APPROVE_FOR_REFERENCE
APPROVE_WITH_NONBLOCKING_CHANGES
RETURN_FOR_REWORK
BLOCKED
```

Điều kiện `APPROVE_FOR_REFERENCE`:

```text
All Gates PASS
P0 = 0
P1 = 0
P2 unresolved = 0
P3 unresolved = 0
```

W01 được phê duyệt không đồng nghĩa tự động merge. Merge là quyết định riêng sau khi kiểm định hoàn tất.
