---
title: "HKA CINEMATIC 4K — Brand & Visual Production Standard"
project: "Human Knowledge Academic"
version: "1.0"
status: "MANDATORY"
language: "vi"
date: "2026-09-03"
base_branch: "hka-knowledge-system-trees"
---

# HKA CINEMATIC 4K — BRAND & VISUAL PRODUCTION STANDARD 1.0

Tài liệu này là quy chuẩn bắt buộc cho mọi cửa sổ phát triển HKA Knowledge System Trees. Mục tiêu là để mỗi cửa sổ giao ra một **gói sản xuất hình ảnh hoàn chỉnh, định lượng rõ ràng và có thể chuyển nguyên vẹn cho đội sản xuất**, sau đó nhận lại đúng số lượng tài sản đã khóa trong manifest.

---

# I. CÁC ĐIỀU KIỆN BẤT BIẾN

## 1. Phong cách hình ảnh

Toàn bộ hình ảnh dạy học trực quan dành cho người học từ 5 đến 24 tuổi sử dụng chuẩn:

```text
HKA CINEMATIC 4K
```

Hình ảnh phải:

- trực quan, sinh động và có mục tiêu dạy học cụ thể;
- chính xác về khoa học, lịch sử, văn hóa và tỷ lệ;
- có bố cục điện ảnh nhưng không hy sinh nội dung học thuật;
- không chỉ làm nhiệm vụ trang trí;
- không gây hiểu sai giữa thực tại quan sát được, tái dựng, mô hình khoa học và ẩn dụ;
- phù hợp về mức độ nhạy cảm với nhóm người học được chỉ định.

Đối với nội dung nghiên cứu chuyên sâu, hệ thống sử dụng **Research Poster 4K** có cấu trúc dữ liệu, phương pháp, độ bất định và nguồn rõ ràng.

## 2. Bốn nhân vật đồng hành bắt buộc

Bốn nhân vật chính thức của HKA là:

1. **Sigma** — định hướng bằng câu hỏi.
2. **Cricket** — phát hiện và mở rộng kết nối.
3. **Little Ant** — chia nhỏ nhiệm vụ, luyện tập và kiên trì.
4. **Professor Owl** — kiểm tra nguồn, bằng chứng, giới hạn và điều chưa biết.

Bốn nhân vật phải xuất hiện xuyên suốt mọi gói CINEMATIC 4K. Không nhân vật nào được sử dụng chỉ như vật trang trí; sự hiện diện phải phù hợp với chức năng học thuật của nhân vật.

## 3. Logo và MOTTO bắt buộc

Mọi hình ảnh hoàn thiện phải có:

- **Logo Sigma chính thức**;
- MOTTO chính xác, không sửa từ, không đổi dấu câu:

```text
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

Logo và MOTTO phải được ghép từ tài sản thương hiệu chính thức trong giai đoạn hậu kỳ. Không yêu cầu mô hình tạo ảnh tự vẽ lại logo hoặc tự sinh chữ, vì điều đó có thể làm sai hình, sai chính tả hoặc sai nhận diện.

---

# II. BRAND ASSET LOCK

Trước khi sản xuất hình ảnh, dự án phải có các tài sản chuẩn sau:

```text
ASSETS/HKA_BRAND/
├── CHARACTERS/
│   ├── SIGMA/
│   │   ├── sigma_master_front.png
│   │   ├── sigma_master_three_quarter.png
│   │   └── sigma_master_profile.png
│   ├── CRICKET/
│   │   ├── cricket_master_front.png
│   │   ├── cricket_master_three_quarter.png
│   │   └── cricket_master_profile.png
│   ├── LITTLE_ANT/
│   │   ├── little_ant_master_front.png
│   │   ├── little_ant_master_three_quarter.png
│   │   └── little_ant_master_profile.png
│   └── PROFESSOR_OWL/
│       ├── professor_owl_master_front.png
│       ├── professor_owl_master_three_quarter.png
│       └── professor_owl_master_profile.png
├── LOGO/
│   ├── sigma_logo_master.svg
│   └── sigma_logo_master.png
├── MOTTO/
│   ├── sigma_motto_lockup.svg
│   └── sigma_motto_lockup.png
├── CHARACTER_BIBLE.md
└── BRAND_USAGE.md
```

Nếu chưa có đủ góc nhìn, tệp ảnh gốc độ phân giải cao vẫn có thể được tiếp nhận làm master ban đầu. Tuy nhiên, không cửa sổ nào được tự phát minh, đổi màu, đổi tỷ lệ, đổi trang phục cốt lõi hoặc tái thiết kế nhân vật.

Mỗi prompt phải chỉ rõ tệp tham chiếu nhân vật và logo được dùng. Tất cả kết quả phải qua **character-consistency review** trước khi nghiệm thu.

---

# III. QUY TẮC XUẤT HIỆN CỦA NHÂN VẬT

## 1. Quy tắc trên từng tài sản

Mỗi tài sản CINEMATIC 4K phải có tối thiểu một nhân vật chính thức của HKA, theo một trong ba cách:

```text
IN-SCENE PARTICIPANT
Nhân vật tham gia trực tiếp vào cảnh học tập, phòng thí nghiệm, thực địa hoặc hoạt động.

OBSERVER FRAME
Nhân vật đứng ở lớp tiền cảnh hoặc mép khung hình để quan sát, không bị trình bày như một phần của hiện tượng lịch sử, vi mô, vũ trụ hay giải phẫu.

GUIDE LAYER
Nhân vật xuất hiện ở lớp hướng dẫn, khung chú giải hoặc vùng poster, tách biệt rõ khỏi dữ liệu và mô hình khoa học.
```

Không đưa nhân vật vào bên trong tế bào, nguyên tử, cơ quan, chiến trường lịch sử hoặc không gian vật lý theo cách khiến người học hiểu đó là một phần thật của hiện tượng.

## 2. Quy tắc trên toàn gói

- Ảnh HERO của mỗi cửa sổ phải có đủ cả bốn nhân vật.
- Mỗi ảnh còn lại phải có một `PRIMARY_COMPANION` và có thể có `SECONDARY_COMPANIONS`.
- Các vai chính được phân bổ gần cân bằng; chênh lệch số lần làm vai chính giữa hai nhân vật bất kỳ không vượt quá 1, trừ khi cửa sổ giải trình bằng chức năng học thuật.
- Professor Owl ưu tiên trong poster nghiên cứu, bằng chứng, sai số và bất định.
- Little Ant ưu tiên trong hoạt động từng bước, kỹ năng và luyện tập.
- Cricket ưu tiên trong hình ảnh liên ngành, khám phá và quan hệ bất ngờ.
- Sigma ưu tiên trong HERO, câu hỏi trung tâm, suy ngẫm và định hướng hành trình.
- Ngoài HERO, cứ mỗi 12 tài sản phải có ít nhất một hình ảnh ensemble gồm đủ bốn nhân vật.

---

# IV. QUY TẮC LOGO VÀ MOTTO

## 1. Tệp hoàn thiện

Mỗi Asset ID phải trả về:

```text
<ASSET_ID>_CLEAN_MASTER.png
<ASSET_ID>_BRANDED_FINAL.png
```

`BRANDED_FINAL` là tệp nghiệm thu bắt buộc và phải có Logo Sigma cùng MOTTO.

`CLEAN_MASTER` giữ nguyên cảnh và nhân vật nhưng chưa ghép logo/motto để phục vụ tái sử dụng, cắt khung và bản địa hóa. CLEAN MASTER không được tính là một ý tưởng hình ảnh mới; nó là bản nguồn của cùng Asset ID.

Vì vậy:

```text
PRODUCTION ASSET COUNT = N
BRANDED FINAL COUNT = N
CLEAN MASTER COUNT = N
TOTAL REQUIRED IMAGE FILES = 2N
```

Đội sản xuất phải giao đúng `N` branded finals và đúng `N` clean masters. Không dùng nhiều biến thể không được yêu cầu để bù cho tài sản thiếu.

## 2. Vùng nhận diện

Đối với khung 16:9:

- Logo đặt trong vùng an toàn ở góc trên trái hoặc trên phải, theo manifest.
- Chiều rộng logo khuyến nghị bằng 7–10% chiều rộng khung.
- MOTTO đặt trong vùng an toàn phía dưới, không che hiện tượng chính.
- Chừa ít nhất 4% lề ngoài khung cho logo và MOTTO.

Đối với poster 9:16:

- Logo đặt ở vùng đầu poster.
- MOTTO đặt ở chân poster.
- Dữ liệu, nguồn và biểu đồ không được bị logo hoặc MOTTO che khuất.

Không kéo méo logo, không đổi tỷ lệ, không đổi màu thương hiệu nếu không có biến thể chính thức.

---

# V. HỆ GÓI SỐ LƯỢNG KHÓA CỨNG

Mỗi cửa sổ nội dung phải tự đánh giá độ phức tạp và chọn **đúng một** trong năm gói dưới đây. Không được chỉ ghi một khoảng. Khi cửa sổ hoàn thành, tổng số tài sản phải là một con số đã khóa.

| Gói | Tổng tài sản | Phù hợp với |
|---|---:|---|
| **P12** | 12 | Phần nền tảng hoặc cửa sổ có tối đa 6 cụm hình ảnh |
| **P18** | 18 | Cây nhỏ–trung bình, 7–10 cụm hình ảnh |
| **P24** | 24 | Cây trung bình–lớn, 11–14 cụm hình ảnh |
| **P30** | 30 | Cây lớn, 15–18 cụm hình ảnh |
| **P36** | 36 | Cây rất lớn, từ 19 cụm hình ảnh trở lên |

Không cửa sổ nào được vượt quá P36. Nếu P36 vẫn không đủ để thể hiện rõ nội dung, cửa sổ phải đề xuất chia phạm vi trước khi sản xuất, thay vì dồn quá nhiều chủ đề vào một hình.

## 1. Visual Coverage Unit — VCU

Một `Visual Coverage Unit` là một cụm tri thức có thể được truyền đạt rõ bằng một cảnh hoặc một poster thống nhất.

Một VCU:

- chỉ được bao phủ tối đa 2 cành cấp 1;
- chỉ được ánh xạ tối đa 6 nút tri thức;
- phải có một mục tiêu dạy học duy nhất;
- không được ghép các nội dung chỉ vì chúng có vẻ đẹp hoặc cùng màu sắc;
- phải nêu rõ vì sao hình ảnh cần thiết.

## 2. Cách chọn gói

Mỗi cửa sổ phải:

1. Liệt kê toàn bộ cành cấp 1 và các nút có giá trị trực quan cao.
2. Nhóm chúng thành VCU theo quan hệ học thuật thực.
3. Chấm từng VCU theo bốn tiêu chí:

| Tiêu chí | Điểm |
|---|---:|
| Tính trung tâm đối với chương trình | 0–3 |
| Mức cần thiết của trực quan hóa | 0–3 |
| Nguy cơ ngộ nhận nếu thiếu hình | 0–2 |
| Giá trị kết nối liên ngành | 0–2 |

4. Bảo đảm mọi cành cấp 1 được ánh xạ vào ít nhất một VCU.
5. Đếm số VCU và chọn P12, P18, P24, P30 hoặc P36 theo bảng trên.
6. Có thể chọn cao hơn đúng một gói nếu có giải trình; không được chọn thấp hơn mức do số VCU yêu cầu.
7. Khóa manifest trước khi bàn giao cho đội sản xuất.

---

# VI. PHÂN BỔ CHÍNH XÁC THEO NHÓM NGƯỜI HỌC

Mỗi gói phải có đúng phân bổ sau:

| Gói | Universal HERO | A1 5–8 | A2 9–12 | A3 13–15 | A4 16–18 | A5 19–24 | Research Poster | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| P12 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 12 |
| P18 | 1 | 3 | 3 | 3 | 3 | 3 | 2 | 18 |
| P24 | 1 | 4 | 4 | 4 | 4 | 4 | 3 | 24 |
| P30 | 1 | 5 | 5 | 5 | 5 | 5 | 4 | 30 |
| P36 | 1 | 6 | 6 | 6 | 6 | 6 | 5 | 36 |

Nhóm tuổi là **chế độ biểu đạt chính**, không phải hàng rào khóa tri thức. Với chủ đề nhạy cảm, A1 và A2 phải dùng cửa vào an toàn, không đồ họa, phù hợp phát triển; không loại bỏ toàn bộ chủ đề chỉ vì nó phức tạp.

---

# VII. PHÂN BỔ CHÍNH XÁC THEO LOẠI HÌNH

| Loại hình | P12 | P18 | P24 | P30 | P36 |
|---|---:|---:|---:|---:|---:|
| HERO | 1 | 1 | 1 | 1 | 1 |
| ANCHOR / OVERVIEW | 4 | 5 | 7 | 9 | 11 |
| CONCEPT / PROCESS / MECHANISM / RECONSTRUCTION | 3 | 5 | 7 | 9 | 11 |
| COMPARISON / SCALE / MISCONCEPTION | 1 | 2 | 3 | 4 | 5 |
| CROSS-LINK | 1 | 2 | 2 | 3 | 3 |
| HUMAN IMPACT / ETHICAL SCENARIO | 1 | 1 | 1 | 1 | 1 |
| RESEARCH POSTER | 1 | 2 | 3 | 3 | 4 |
| **TỔNG** | **12** | **18** | **24** | **30** | **36** |

Nếu một loại hình không phù hợp với lĩnh vực, cửa sổ được phép thay thế bằng loại hình khác có giá trị dạy học tương đương, nhưng:

- không được giảm tổng số;
- không được giảm số Research Poster;
- không được bỏ HERO;
- không được bỏ toàn bộ CROSS-LINK;
- mọi thay thế phải được ghi trong manifest.

---

# VIII. BAO PHỦ CHƯƠNG TRÌNH MÀ KHÔNG DÀN TRẢI

Mỗi cửa sổ phải chứng minh:

1. **100% cành cấp 1** được ánh xạ tới ít nhất một Asset ID.
2. **100% quá trình hoặc cơ chế có nguy cơ bị hiểu sai cao** được trực quan hóa hoặc được giải trình vì sao không nên trực quan hóa.
3. **100% hình ảnh** có một mục tiêu dạy học duy nhất.
4. Không Asset ID nào cố gắng dạy quá 2 cành cấp 1 hoặc quá 6 nút.
5. Không tạo ảnh riêng cho mọi nút; những nút có thể dạy tốt hơn bằng văn bản, âm thanh, mô phỏng tương tác hoặc dữ liệu phải được ghi nhận bằng phương tiện phù hợp.
6. Các khái niệm cốt lõi được chọn làm `SPIRAL VISUALS` để có nhiều cách biểu đạt theo độ tuổi:

| Gói | Số khái niệm tối thiểu có biến thể xuyên nhóm tuổi |
|---|---:|
| P12 | 1 |
| P18 | 2 |
| P24 | 3 |
| P30 | 4 |
| P36 | 5 |

Mỗi biến thể là một Asset ID riêng và được tính vào tổng gói.

---

# IX. CHUẨN KỸ THUẬT

## 1. Cinematic 4K

```text
Canvas: 3840 × 2160
Aspect ratio: 16:9
Color space: sRGB hoặc Display-P3 theo pipeline đã phê duyệt
Master: PNG lossless
Website derivative: WebP/AVIF được tạo sau, không thay thế master
```

## 2. Research Poster 4K

```text
Canvas mặc định: 2160 × 3840
Aspect ratio: 9:16
Master: PNG lossless
Text, dữ liệu và nguồn phải được ghép ở hậu kỳ
```

Một poster có thể dùng 3840 × 2160 nếu nội dung cần bố cục ngang; quyết định phải ghi trong manifest.

## 3. Phân loại biểu diễn bắt buộc

Mỗi Asset ID phải gắn đúng một nhãn chính:

```text
DOCUMENTARY REALITY
SCIENTIFIC RECONSTRUCTION
HISTORICAL RECONSTRUCTION
SCIENTIFIC VISUALIZATION
CONCEPTUAL MODEL
HUMANISTIC METAPHOR
DATA / RESEARCH POSTER
```

Mô hình, tái dựng và ẩn dụ phải được ghi rõ trong caption; không được trình bày như ảnh chụp trực tiếp.

---

# X. HỒ SƠ PROMPT BẮT BUỘC CHO MỖI ASSET ID

```text
ASSET ID:
WINDOW ID:
TREE / BRANCH / NODE IDS:
VISUAL COVERAGE UNIT:
ASSET TYPE:
REPRESENTATION TYPE:
PRIMARY AUDIENCE:
ACADEMIC DEPTH:
LEARNING OBJECTIVE:
PRIMARY COMPANION:
SECONDARY COMPANIONS:
CHARACTER REFERENCE FILES:
CHARACTER PLACEMENT MODE:
SCENE TITLE:
PROMPT VI:
PROMPT EN:
SCIENTIFIC / HISTORICAL ACCURACY LOCKS:
MANDATORY OBJECTS:
FORBIDDEN OBJECTS:
COMPOSITION:
CAMERA / LENS:
LIGHTING:
ENVIRONMENT / TIME:
SCALE CUES:
BRAND SAFE AREA:
LOGO PLACEMENT:
MOTTO PLACEMENT:
NEGATIVE PROMPT:
CAPTION:
ALT TEXT:
SOURCE CHECKS:
OUTPUT SIZE:
OUTPUT FILENAMES:
REVIEW STATUS:
```

Mã hình ảnh:

```text
HKA-VIS-WXX-0001
```

Không được có prompt thiếu Asset ID. Không được có Asset ID không có prompt.

---

# XI. NEGATIVE PROMPT NỀN

Mỗi cửa sổ phải hiệu chỉnh negative prompt theo lĩnh vực, bắt đầu từ chuẩn:

```text
no pseudoscience,
no false anatomy,
no impossible physics,
no incorrect molecular structure,
no inaccurate historical clothing,
no anachronistic objects,
no misleading scale,
no meaningless equations,
no random letters,
no generated logo,
no generated motto text,
no embedded captions,
no watermark,
no unauthorized brand mark,
no copyrighted third-party character,
no sensationalism,
no cultural stereotype,
no unnecessary gore,
no cluttered composition,
no distortion of the four official HKA characters.
```

---

# XII. GÓI TỆP MỖI CỬA SỔ PHẢI GIAO

Ngoài `TREE.md`, `NODE_CATALOG.md` và `SELF_AUDIT.md`, mỗi cửa sổ nội dung phải giao đầy đủ:

```text
VISUAL_STRATEGY_AND_COUNT.md
VISUAL_COVERAGE_MATRIX.csv
VISUAL_PRODUCTION_MANIFEST.csv
VISUAL_PROMPTS_CINEMATIC_4K.md
VISUAL_QA_CHECKLIST.md
```

## 1. `VISUAL_STRATEGY_AND_COUNT.md`

Phải nêu:

- số cành cấp 1;
- danh sách VCU;
- điểm từng VCU;
- gói đã chọn;
- tổng tài sản khóa cứng;
- phân bổ nhóm tuổi;
- phân bổ loại hình;
- phân bổ bốn nhân vật;
- lý do số lượng là đủ nhưng không dàn trải.

## 2. `VISUAL_COVERAGE_MATRIX.csv`

Mỗi hàng ánh xạ:

```text
BRANCH ID, NODE ID, VCU ID, ASSET ID, COVERAGE ROLE, NOTES
```

## 3. `VISUAL_PRODUCTION_MANIFEST.csv`

Mỗi hàng là đúng một Asset ID:

```text
ASSET_ID, TITLE, TYPE, AUDIENCE, DEPTH, PRIMARY_COMPANION,
SECONDARY_COMPANIONS, CHARACTER_MODE, REPRESENTATION_TYPE,
RESOLUTION, ASPECT_RATIO, LOGO_REQUIRED, MOTTO_REQUIRED,
CLEAN_MASTER_FILENAME, BRANDED_FINAL_FILENAME, STATUS
```

`LOGO_REQUIRED` và `MOTTO_REQUIRED` luôn phải là `YES` cho branded final.

## 4. `VISUAL_PROMPTS_CINEMATIC_4K.md`

Chứa toàn bộ hồ sơ prompt theo Mục X, đúng số lượng trong manifest.

## 5. `VISUAL_QA_CHECKLIST.md`

Phải kiểm tra:

- đúng nhân vật và tỷ lệ;
- đúng vai học thuật của nhân vật;
- đúng logo;
- đúng MOTTO;
- không sai chữ;
- không sai khoa học, lịch sử hoặc văn hóa;
- đúng nhóm tuổi;
- đúng loại biểu diễn;
- đúng độ phân giải;
- đúng filename;
- không thiếu hoặc dư Asset ID.

---

# XIII. QUY TẮC KHÓA VÀ THAY ĐỔI MANIFEST

Khi cửa sổ tuyên bố `VISUAL MANIFEST LOCKED`:

- Tổng số tài sản không được thay đổi âm thầm.
- Mọi thêm, bớt hoặc thay thế phải tăng `MANIFEST VERSION`.
- Phải ghi rõ Asset ID thêm, bỏ hoặc thay.
- Đội sản xuất chỉ làm theo manifest đã khóa gần nhất.
- Tệp ngoài manifest không được tính vào nghiệm thu.
- Thiếu một Asset ID là chưa hoàn thành.
- Dư một Asset ID không tự động được chấp nhận.

---

# XIV. BIÊN NHẬN BÀN GIAO CỦA MỖI CỬA SỔ

```text
WINDOW ID:
KNOWLEDGE TREE:
SELECTED PACKAGE: P12 / P18 / P24 / P30 / P36
MANIFEST VERSION:
LOCKED PRODUCTION ASSET COUNT:
REQUIRED BRANDED FINAL COUNT:
REQUIRED CLEAN MASTER COUNT:
TOTAL REQUIRED IMAGE FILES:

AUDIENCE DISTRIBUTION:
UNIVERSAL HERO:
A1 5–8:
A2 9–12:
A3 13–15:
A4 16–18:
A5 19–24:
RESEARCH POSTER:

CHARACTER LEAD DISTRIBUTION:
SIGMA:
CRICKET:
LITTLE ANT:
PROFESSOR OWL:
ENSEMBLE FOUR-CHARACTER ASSETS:

COVERAGE:
LEVEL-1 BRANCHES COVERED:
VISUAL COVERAGE UNITS:
NODE IDS MAPPED:
CROSS-LINK ASSETS:
SPIRAL VISUAL CONCEPTS:

BRAND CONFIRMATION:
OFFICIAL CHARACTER REFERENCES USED: YES / NO
OFFICIAL SIGMA LOGO USED: YES / NO
EXACT MOTTO USED: YES / NO

FILES:
VISUAL_STRATEGY_AND_COUNT.md
VISUAL_COVERAGE_MATRIX.csv
VISUAL_PRODUCTION_MANIFEST.csv
VISUAL_PROMPTS_CINEMATIC_4K.md
VISUAL_QA_CHECKLIST.md

UNRESOLVED VISUAL RISKS:
EXPERT REVIEW REQUIRED:
```

---

# XV. LỆNH BẮT BUỘC BỔ SUNG VÀO PROMPT CỦA MỌI CỬA SỔ

```text
Bạn phải tự xác định số lượng CINEMATIC 4K cần thiết cho phạm vi của mình bằng hệ Visual Coverage Unit và chọn đúng một gói P12, P18, P24, P30 hoặc P36.

Bạn không được trả về một khoảng số lượng. Bạn phải khóa một con số chính xác, tạo đúng từng Asset ID và chứng minh mọi cành cấp 1 đã được bao phủ mà không dàn trải.

Mỗi Asset ID phải có ít nhất một trong bốn nhân vật HKA: Sigma, Cricket, Little Ant, Professor Owl. HERO phải có đủ bốn. Vai trò của nhân vật phải phù hợp chức năng học thuật, không chỉ để trang trí.

Mọi branded final bắt buộc có Logo Sigma chính thức và MOTTO chính xác:
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.

Không yêu cầu mô hình tạo ảnh tự sinh logo hoặc chữ. Hãy chừa brand-safe area và quy định bước hậu kỳ ghép tài sản chính thức.

Mỗi Asset ID phải trả về một CLEAN MASTER và một BRANDED FINAL. Nếu gói có N Asset IDs thì đội sản xuất phải giao đúng N branded finals và N clean masters, tổng cộng 2N tệp hình.

Bạn phải tạo và khóa VISUAL_PRODUCTION_MANIFEST.csv trước khi bàn giao. Không có prompt ngoài manifest và không có dòng manifest thiếu prompt.
```

---

# XVI. NGUYÊN TẮC CHỐT

> **Không tạo nhiều hình để gây ấn tượng.**  
> **Không tạo ít hình đến mức tri thức mất khả năng được nhìn thấy.**  
> **Mỗi hình có một nhiệm vụ học tập.**  
> **Mỗi cành có bằng chứng bao phủ.**  
> **Mỗi gói có số lượng khóa cứng.**  
> **Mỗi sản phẩm mang đúng bốn nhân vật, Logo Sigma và MOTTO theo quy chuẩn.**

```text
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```
