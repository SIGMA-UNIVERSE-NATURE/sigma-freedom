---
title: "HKA W01 B00 — Calibration Batch Prompts"
batch_id: "HKA-W01-B00"
planned_run_id: "HKA-W01-B00-R01"
asset_count: 2
status: "PROMPT CONTENT READY"
---

# HKA-W01-B00 — CALIBRATION BATCH

## Immutable brand source

```text
Repository: linkcomltd-byte/sigma-universe-web
Commit: 2d3aa9d8418acccd39a3d263e917d4157e029e17
Sigma: assets/characters/sigma.png
Cricket: assets/characters/cricket.png
Little Ant: assets/characters/little-ant.png
Professor Owl: assets/characters/professor-owl.png
Logo: assets/logo/sigma-logo-master.jpg
Emblem: assets/logo/sigma-emblem-shell.jpg
MOTTO: PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

Rules:

- Produce no image until a schema-valid manifest with Prompt Content Commit SHA is issued.
- The image model must not generate Logo Sigma, MOTTO, labels, captions, equations or random text.
- Each Asset ID later returns one CLEAN MASTER and one BRANDED FINAL.
- Official logo and MOTTO are added in post-production only.
- Any prompt ambiguity must return `PROMPT_BLOCKED`; production may not reinterpret.

Global negative:

```text
no pseudoscience, no false anatomy, no impossible physics, no misleading scale, no random letters, no generated logo, no generated motto text, no embedded captions, no watermark, no unauthorized brand mark, no copyrighted third-party character, no sensationalism, no cultural stereotype, no cluttered composition, no distortion of the four official HKA characters
```

---

# HKA-VIS-W01-0001

```text
TITLE: HKA World Tree — bốn người đồng hành mở sáu cánh cửa
AUDIENCE: UNIVERSAL
DEPTH: MULTI_DEPTH
TYPE: HERO
REPRESENTATION: CONCEPTUAL_MODEL
PRIMARY COMPANION: ENSEMBLE_FOUR
CHARACTER MODE: GUIDE_LAYER
PROMPT SHA-256: c5d839c819e5ed185a30033af26bdb5dd79d28c1db00269492ad7d6e9d5dbf38
OUTPUT: 3840×2160 PNG
CLEAN: HKA-VIS-W01-0001_CLEAN_MASTER.png
BRANDED: HKA-VIS-W01-0001_BRANDED_FINAL.png
```

**Learning objective:** Nhận biết sáu miền HKA đồng cấp và bốn Companion có chức năng khác nhau.

**Prompt VI:** Tạo ảnh HKA CINEMATIC 4K 3840×2160, 16:9, mô hình khái niệm giáo dục chứ không phải khu rừng có thật. Một không gian học tập bán tự nhiên rộng với thân Cây Tri thức trung tâm mọc từ đất, rễ lộ nhẹ, sáu cành lớn tỏa ngang đồng cấp thành sáu vùng liên thông: quy luật và thực tại; sự sống, sức khỏe và tâm trí; hệ thống, thiết kế và kết nối; thời gian, nơi chốn và tương lai; ngôn ngữ, biểu đạt và ý nghĩa; cùng tồn tại, lựa chọn và công lý. Không cành nào cao hơn hoặc được ưu tiên. Dùng đúng bốn nhân vật chính thức Sigma, Cricket, Little Ant và Professor Owl ở tiền cảnh, mỗi nhân vật hướng chú ý đến một phần khác của cây, không che hiện tượng. Establishing shot cân bằng, eye-level, lens 28–32 mm, ánh sáng bình minh tự nhiên, vật liệu chân thực, chiều sâu điện ảnh nhưng không huyền bí. Không tạo chữ, công thức, logo hay motto. Chừa 10% vùng trên phải cho logo và 14% dải dưới giữa cho motto hậu kỳ.

**Prompt EN:** Create an HKA CINEMATIC 4K educational image, 3840×2160, 16:9, explicitly a conceptual interface model rather than a literal forest. Show a broad semi-natural learning landscape centered on a living Knowledge Tree rooted in real soil, with a small portion of the roots visible. Six major branches spread laterally at equal status into six connected visual territories: patterns and reality; life, health and mind; systems, design and connection; time, place and futures; language, expression and meaning; coexistence, choice and justice. No branch may be visually higher, larger, or more prestigious than another. Use the exact official character references for Sigma, Cricket, Little Ant, and Professor Owl, all four present in a gentle foreground arc, each directing attention toward a different part of the tree without blocking it. Balanced wide establishing composition, eye-level camera, 28–32 mm equivalent lens, natural dawn light, physically plausible materials, cinematic depth without mystical spectacle. Generate no text, equations, logo, or motto. Preserve a clean upper-right brand-safe area and a clean lower band for post-production branding.

**Asset negative:** no hierarchical branch arrangement, no school-subject labels, no religious symbolism, no fantasy portal, no floating icons, no oversized mascots, no duplicated characters.

**PASS:** Đủ bốn character đúng reference; sáu cành cân bằng; conceptual status rõ; không text/brand giả; safe areas tồn tại.

**FAIL:** Thiếu hoặc trùng character; cành thành thang; mystical spectacle; generated text/logo/MOTTO.

---

# HKA-VIS-W01-0002

```text
TITLE: Một giọt mưa trên lá — bắt đầu từ câu hỏi
AUDIENCE: A1_5_8
DEPTH: D1
TYPE: CONCEPT
REPRESENTATION: DOCUMENTARY_REALITY
PRIMARY COMPANION: SIGMA
CHARACTER MASTER: assets/characters/sigma.png
CHARACTER MODE: OBSERVER_FRAME
PROMPT SHA-256: a922ea27d31b9f50803a0ebb48adf59b9fab8ee9449c81c59739d0efd7e89793
OUTPUT: 3840×2160 PNG
CLEAN: HKA-VIS-W01-0002_CLEAN_MASTER.png
BRANDED: HKA-VIS-W01-0002_BRANDED_FINAL.png
```

**Learning objective:** Hướng người học nhìn một hiện tượng thật và hình thành câu hỏi mà chưa nhận sẵn đáp án.

**Prompt VI:** Tạo ảnh dạy học CINEMATIC 4K 3840×2160, 16:9 cho người học 5–8 tuổi. Cảnh quan sát thật trong vườn ngay sau mưa: một chiếc lá xanh tự nhiên chiếm phần lớn khung hình, một giọt nước trong lớn nằm ổn định trên bề mặt lá, vài giọt nhỏ hơn ở xa, nền vườn mờ. Dùng đúng Sigma chính thức ở mép trái như người quan sát, cúi nhẹ và nhìn chính xác vào giọt nước, không chạm và không đưa đáp án. Macro 90–105 mm, giọt sắc nét tại một phần ba phải, ánh sáng trời tán xạ mềm, vật liệu và phản xạ vật lý hợp lý. Không hiển thị phân tử, lực, mũi tên, chữ, logo hoặc motto. Chừa bokeh sạch trên phải và dải dưới phải cho hậu kỳ.

**Prompt EN:** Create an HKA CINEMATIC 4K educational image, 3840×2160, 16:9, for ages 5–8. Show a directly observable garden scene immediately after rain: one natural green leaf fills most of the frame, with one clear, stable water droplet resting on its surface and a few smaller droplets farther away; the garden background is softly blurred. Use the exact official Sigma character reference at the left edge as an observer, leaning slightly and looking precisely at the main droplet, without touching it and without presenting an answer. Use physically plausible macro photography logic, 90–105 mm equivalent, with the droplet sharp near the right rule-of-thirds point, soft overcast daylight, realistic leaf texture and optical reflection. The image should invite a question without depicting invisible mechanisms. Do not show molecules, forces, arrows, text, logo, or motto. Preserve clean upper-right bokeh and lower-right space for post-production branding.

**Asset negative:** no anthropomorphic droplet, no magical glow, no molecule model, no exaggerated rainbow, no child tasting water, no insect distraction.

**PASS:** Một hiện tượng chính; Sigma gaze đúng; vật liệu/ánh sáng thật; không cơ chế vô hình.

**FAIL:** Quá tải; giọt phát sáng; Sigma che giọt; text/brand giả; reflection phi vật lý.

---

```text
BATCH PROMPT COUNT: 2
EXPECTED CLEAN MASTERS LATER: 2
EXPECTED BRANDED FINALS LATER: 2
PRODUCTION AUTHORIZED: NO — WAIT FOR BATCH_MANIFEST.json
```
