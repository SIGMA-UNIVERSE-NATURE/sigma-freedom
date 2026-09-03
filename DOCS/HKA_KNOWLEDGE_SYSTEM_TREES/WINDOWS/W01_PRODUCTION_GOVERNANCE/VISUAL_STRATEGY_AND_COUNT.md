---
title: "HKA W01 — Visual Strategy & Locked Count"
window_id: "W01"
version: "1.0"
status: "PROMPT DESIGN LOCK"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — VISUAL STRATEGY & COUNT

## 1. Chức năng của bộ hiệu chuẩn

W01 không đại diện cho một Knowledge Tree chuyên môn. Bộ hình W01 kiểm tra liệu ngôn ngữ HKA CINEMATIC 4K có thể:

- mở câu hỏi cho người học nhỏ tuổi;
- chỉ dẫn quan sát và phân loại;
- mô tả liên kết mà không bịa nhân quả;
- phân biệt bằng chứng với suy đoán;
- phân biệt cảnh thật, mô hình và tái dựng;
- thể hiện scale cue;
- mô tả thí nghiệm và biến kiểm soát;
- thể hiện hệ thống và phản hồi;
- mô tả nghiên cứu liên ngành có phạm vi;
- hỗ trợ tái lập;
- tạo Research Poster có vùng dữ liệu/chữ hậu kỳ;
- giữ đúng bốn Companion, Logo Sigma và MOTTO.

Bộ hiệu chuẩn **không được dùng thay cho hình ảnh chương trình học chính**.

## 2. Gói đã khóa

```text
SELECTED PACKAGE: P12
LOCKED ASSET COUNT: 12
EXPECTED CLEAN MASTER COUNT: 12
EXPECTED BRANDED FINAL COUNT: 12
EXPECTED TOTAL IMAGE FILES: 24
```

Số lượng P12 do Window Contract khóa, không do W01 tự chọn.

## 3. Phân bổ audience

| Audience | Count | Asset IDs |
|---|---:|---|
| Universal HERO | 1 | 0001 |
| A1 — 5–8 | 2 | 0002–0003 |
| A2 — 9–12 | 2 | 0004–0005 |
| A3 — 13–15 | 2 | 0006–0007 |
| A4 — 16–18 | 2 | 0008–0009 |
| A5 — 19–24 | 2 | 0010–0011 |
| Research | 1 | 0012 |
| **Total** | **12** | |

## 4. Phân bổ Companion

HERO 0001 dùng `ENSEMBLE_FOUR` và không tính vào cân bằng lead cá nhân.

| Primary companion | Count | Asset IDs |
|---|---:|---|
| Sigma | 2 | 0002, 0010 |
| Cricket | 3 | 0004, 0007, 0009 |
| Little Ant | 3 | 0003, 0008, 0011 |
| Professor Owl | 3 | 0005, 0006, 0012 |
| Ensemble Four | 1 | 0001 |

Chênh lệch lead cá nhân tối đa bằng 1, đạt chuẩn.

## 5. Visual Coverage Units

### HKA-VCU-W01-001 — Whole-system orientation

```text
Assets: 0001, 0002
Purpose: Kiểm tra HERO toàn cảnh và cách mở một câu hỏi duy nhất.
Centrality: 3
Visualization need: 3
Misconception risk: 1
Cross-link value: 2
Total: 9/10
```

### HKA-VCU-W01-002 — Observe, compare, classify

```text
Asset: 0003
Purpose: Kiểm tra hướng dẫn từng bước bằng vật thể hữu hình cho A1.
Centrality: 3
Visualization need: 3
Misconception risk: 1
Cross-link value: 1
Total: 8/10
```

### HKA-VCU-W01-003 — Connected evidence

```text
Assets: 0004, 0005
Purpose: Kiểm tra liên kết sinh vật–môi trường và phân biệt quan sát/suy đoán.
Centrality: 3
Visualization need: 3
Misconception risk: 2
Cross-link value: 2
Total: 10/10
```

### HKA-VCU-W01-004 — Scale and model boundaries

```text
Asset: 0006
Purpose: Kiểm tra scale cue và ranh giới panel trong scientific visualization.
Centrality: 3
Visualization need: 3
Misconception risk: 2
Cross-link value: 1
Total: 9/10
```

### HKA-VCU-W01-005 — Evidence-based reconstruction

```text
Asset: 0007
Purpose: Kiểm tra tái dựng lịch sử dựa trên dấu vết, tránh anachronism.
Centrality: 2
Visualization need: 3
Misconception risk: 2
Cross-link value: 2
Total: 9/10
```

### HKA-VCU-W01-006 — Controlled experiment and systems

```text
Assets: 0008, 0009
Purpose: Kiểm tra biến kiểm soát, trình tự đo và conceptual system model.
Centrality: 3
Visualization need: 3
Misconception risk: 2
Cross-link value: 2
Total: 10/10
```

### HKA-VCU-W01-007 — Field inquiry and reproducibility

```text
Assets: 0010, 0011
Purpose: Kiểm tra nghiên cứu liên ngành có câu hỏi chung và workflow tái lập.
Centrality: 3
Visualization need: 2
Misconception risk: 2
Cross-link value: 2
Total: 9/10
```

### HKA-VCU-W01-008 — Research communication

```text
Asset: 0012
Purpose: Kiểm tra poster phương pháp–dữ liệu–bất định–nguồn.
Centrality: 3
Visualization need: 3
Misconception risk: 2
Cross-link value: 2
Total: 10/10
```

## 6. Asset type mapping

Tên chức năng hiệu chuẩn trong contract được ánh xạ sang enum của batch schema:

| Asset | Contract calibration function | Schema asset_type | representation_type |
|---|---|---|---|
| 0001 | HERO | HERO | CONCEPTUAL_MODEL |
| 0002 | DOCUMENTARY / QUESTION | CONCEPT | DOCUMENTARY_REALITY |
| 0003 | STEP-BY-STEP | PROCESS | DOCUMENTARY_REALITY |
| 0004 | CROSS-LINK | CROSS_LINK | SCIENTIFIC_VISUALIZATION |
| 0005 | EVIDENCE | COMPARISON | DOCUMENTARY_REALITY |
| 0006 | SCIENTIFIC_VISUALIZATION | SCALE | SCIENTIFIC_VISUALIZATION |
| 0007 | HISTORICAL_RECONSTRUCTION | RECONSTRUCTION | HISTORICAL_RECONSTRUCTION |
| 0008 | LAB / CONTROLLED VARIABLES | PROCESS | DOCUMENTARY_REALITY |
| 0009 | CONCEPTUAL_SYSTEM_MODEL | MECHANISM | CONCEPTUAL_MODEL |
| 0010 | INTERDISCIPLINARY FIELD | CROSS_LINK | DOCUMENTARY_REALITY |
| 0011 | REPRODUCIBLE WORKFLOW | PROCESS | DOCUMENTARY_REALITY |
| 0012 | RESEARCH_POSTER | RESEARCH_POSTER | DATA_RESEARCH_POSTER |

Việc ánh xạ không đổi mục tiêu của contract; nó bảo đảm manifest hợp schema.

## 7. Batch plan

```text
HKA-W01-B00 — 2 assets
0001, 0002
Purpose: brand/character calibration + A1 question calibration

HKA-W01-B01 — 6 assets
0003, 0004, 0005, 0006, 0007, 0008
Purpose: learning-mode and representation calibration

HKA-W01-B02 — 4 assets
0009, 0010, 0011, 0012
Purpose: systems, research workflow and poster calibration
```

Run đầu tiên:

```text
HKA-W01-B00-R01
HKA-W01-B01-R01
HKA-W01-B02-R01
```

## 8. Spiral visual concept

Khái niệm xuyên nhóm tuổi được hiệu chuẩn là:

```text
TA BIẾT ĐIỀU NÀY BẰNG CÁCH NÀO?
```

Biểu đạt qua:

- A1: quan sát và phân loại;
- A2: dấu vết và suy đoán;
- A3: scale/model/reconstruction;
- A4: biến kiểm soát và hệ thống;
- A5: workflow và nghiên cứu liên ngành;
- Research: dữ liệu, bất định và nguồn.

## 9. Vì sao 12 là đủ nhưng không dàn trải

- Mỗi calibration function có asset riêng hoặc cặp asset có quan hệ rõ.
- Tất cả A1–A5 và Research đều có đại diện.
- Bảy loại biểu diễn trọng yếu được kiểm tra.
- Bốn Companion có vai trò cân bằng.
- HERO kiểm tra ensemble và brand-safe area.
- Không tạo nhiều biến thể mỹ thuật không có giá trị kiểm định.
- Mỗi asset có một mục tiêu chính; không asset nào bao phủ quá 2 VCU.

## 10. Không thuộc gói này

- Không sản xuất ảnh.
- Không tạo web derivatives.
- Không upload R2.
- Không thay hình chính thức của Knowledge Trees.
- Không dùng output W01 làm bằng chứng học thuật cho các lĩnh vực chuyên môn.
