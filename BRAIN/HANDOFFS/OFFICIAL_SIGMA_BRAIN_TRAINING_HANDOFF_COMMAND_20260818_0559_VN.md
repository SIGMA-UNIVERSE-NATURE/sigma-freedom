# LỆNH CHUYỂN GIAO CHÍNH THỨC — SIGMA BRAIN TRAINING

**Người ra lệnh:** Châu  
**Được ghi và bảo toàn bởi:** `HAND TO HAND_ CỬA 2` — Recovery Anchor  
**Áp dụng cho:** `HAND TO HAND_ CỬA 3` và mọi successor hợp lệ về sau  
**Repository:** `SIGMA-UNIVERSE-NATURE/sigma-freedom`  
**Branch:** `SIGMA_LIFE`  
**Thời điểm ban hành:** 2026-08-18 05:59 +07:00

---

## I. MỤC TIÊU CHÍNH XUYÊN SUỐT

Mục tiêu số 1 của PROJECT SIGMA là:

> **TRAIN VÀ PHÁT TRIỂN BỘ NÃO SIGMA ĐỂ NĂNG LỰC HỆ THỐNG THỰC SỰ TỐT HƠN TRẠNG THÁI ĐÃ ĐƯỢC XÁC MINH TRƯỚC ĐÓ.**

Continuity, window identity, handoff, provenance, checkpoint, recovery và governance chỉ là **hạ tầng để không làm mất tiến bộ**. Chúng không được thay thế mục tiêu training bộ não.

Sau khi một cửa đã xác minh đủ identity/lineage/authority, nó phải quay ngay về công việc training hoặc measurement hiện hành. Không được biến việc nhận diện cửa sổ thành mục tiêu chính.

Đường ray bắt buộc:

`TRAIN THE BRAIN -> PROVE IMPROVEMENT -> PRESERVE THE IMPROVEMENT -> CONTINUE FROM IT`

Không phải:

`IDENTIFY WINDOWS -> IDENTIFY WINDOWS -> IDENTIFY WINDOWS`

---

## II. “TỐT HƠN” KHÔNG ĐƯỢC TỰ NHẬN

Một cửa mới hơn, model mới hơn, nhiều code hơn, nhiều file hơn, chạy lâu hơn, nhiều câu trả lời hơn hoặc tự tuyên bố tiến hóa **không** được tính là tốt hơn.

Một trạng thái chỉ được gọi là tốt hơn khi hoàn tất chuỗi:

`PREVIOUS VERIFIED BASELINE`
`-> TARGET GAP / FALSIFIABLE HYPOTHESIS`
`-> ISOLATED CANDIDATE`
`-> CONTROLLED TEST / MEASUREMENT`
`-> DIFFERENTIAL EVIDENCE`
`-> INDEPENDENT EVALUATION WHEN REQUIRED`
`-> REGRESSION CHECK`
`-> PROMOTE / REVISE / REJECT`
`-> DURABLE CANONICAL STATE UPDATE`

Nếu không có measurable delta so với baseline trước thì không được gọi là improvement.

Nếu candidate cải thiện một mặt nhưng làm hỏng verified guarantee quan trọng thì không được promote cho đến khi regression được hiểu, đo, scoped và có rollback.

---

## III. QUY TẮC TÍCH LŨY — ĐỪNG VÉT LẠI

Mọi cải tiến đã được **verified + evaluated + promoted** trở thành **baseline mới**.

Cửa sau phải bắt đầu từ baseline mới đó và tìm bước cải tiến tiếp theo.

Không được quay lại làm từ đầu chỉ vì:

- mở cửa mới;
- mất chat memory;
- đổi model;
- đổi máy;
- đổi substrate;
- không nhớ đã làm gì;
- muốn “chắc ăn” nên chạy lại toàn bộ.

Rerun/rebuild một việc đã verified chỉ hợp lệ nếu có lý do dựa trên evidence, ví dụ:

- regression signal;
- dependency hoặc environment thay đổi;
- substrate thay đổi làm evidence cũ không còn đủ;
- contradiction hoặc evidence mới;
- thiếu independent evaluator bắt buộc;
- audit cụ thể yêu cầu.

Mỗi rerun phải ghi rõ: **vì sao evidence cũ không còn đủ**.

`NEW WINDOW` không bao giờ là lý do đủ để rerun.

---

## IV. MỌI KẾT QUẢ TỐT HƠN PHẢI ĐƯỢC GHI LẠI

Trước khi coi một improvement là durable, phải persist tối thiểu:

1. previous verified baseline;
2. candidate/version ID;
3. target gap hoặc hypothesis;
4. test/measurement evidence;
5. differential result;
6. evaluator result;
7. regression result;
8. rollback path;
9. decision: PROMOTE / REVISE / REJECT;
10. canonical state update;
11. continuation pointer / next action khi phù hợp.

Nếu một kết quả “tốt hơn” chỉ tồn tại trong chat hoặc lời tự nhận mà chưa được ghi canonical thì chưa được coi là đã bảo toàn cho successor.

---

## V. GIAI ĐOẠN HIỆN TẠI — ĐO NÃO TRƯỚC KHI SỬA NÃO

Chương trình hiện tại vẫn là:

`SIGMA_512_BOUNDED_CONTINUOUS_AUTOMEASURE`

Nguyên tắc:

`DO_NOT_IMPROVE_YET_MEASURE_CURRENT_REALITY_FIRST`

Snapshot tham chiếu tại thời điểm phát lệnh:

- observed canonical HEAD: `7d5d05aff123e88dbf9c8032b5cc505b2bbb7f0e`;
- request tại snapshot: `SIGMA-512-AUTO-MEASURE-SECTION-XXVI-396-415`;
- ledger tại snapshot: `PASS=0, PARTIAL=129, HOLD=290, FAIL=0, NOT_AUDITED=93, NOT_APPLICABLE=0`;
- machine receipt Section XXVI đã tồn tại bằng Remote Operator `0.6.1`, `TARGET_COUNT=20`, `HOLD=20`, core modification `0`, external side effect `0`.

**Các giá trị trên chỉ là checkpoint tham chiếu, không phải live truth vĩnh viễn.** Active executor phải fresh-fetch `SIGMA_LIFE`, current canonical state và machine evidence trước mọi quyết định.

Trong khi `NOT_AUDITED > 0`, công việc đúng là:

1. tiếp tục đúng `CURRENT_STATE + NEXT_ACTION + LOCAL_COGNITION_REQUEST` mới nhất;
2. chỉ đo authorized `NOT_AUDITED` scope;
3. giữ `HOLD_ONLY` evidence ceiling;
4. không implementation trong measurement controller;
5. không DNA/core mutation;
6. paid API OFF;
7. không website action trong controller scope;
8. không arbitrary shell;
9. không external side effect;
10. machine receipt phải có trước khi controller advance;
11. không gọi measurement progress là intelligence improvement.

Mục tiêu giai đoạn này:

> **Đạt `NOT_AUDITED = 0` với provenance sạch, ledger reconciled và không giả PASS.**

---

## VI. KHI `NOT_AUDITED = 0` — DỪNG AUTOMEASURE, BẮT ĐẦU TRAINING THẬT

Khi measurement baseline hoàn tất, không được tiếp tục đo chỉ để tạo hoạt động.

### Phase A — Baseline closure

1. verify ledger 512 reconcile;
2. reconcile mọi machine/canonical evidence gap;
3. giữ nguyên contradiction, HOLD, PARTIAL, FAIL — không làm sạch số liệu để trông đẹp hơn;
4. tạo dependency/priority graph từ measured gaps;
5. xác định các verified guarantees không được regression.

### Phase B — Chọn gap training đầu tiên

Chọn **highest-leverage cognition gap**, không chọn vì dễ làm hoặc dễ báo cáo.

Ưu tiên các cơ chế nền có khả năng cải thiện nhiều năng lực khác, ví dụ:

- evidence-grounded deliberation;
- persistent cognitive memory;
- world/causal model;
- uncertainty/calibration;
- contradiction detection;
- proposer/critic/evaluator architecture;
- tool/simulation reliability;
- endogenous questions/goals;
- meta-learning;
- failure recovery.

Gap phải được lựa chọn bằng evidence/dependency graph, không bằng cảm giác.

### Phase C — Chu kỳ training bắt buộc

Mỗi candidate phải đi qua:

`BASELINE -> HYPOTHESIS -> CANDIDATE -> ISOLATED TEST -> DIFFERENTIAL EVIDENCE -> EVALUATOR -> REGRESSION -> PROMOTE/REVISE/REJECT`

Không được self-certify.

Không được biến “code đã thay đổi” thành “trí tuệ đã tốt hơn”.

Không được biến “test chạy” thành “capability PASS” nếu test không đo đúng capability.

### Phase D — Tích lũy

Nếu PROMOTE:

1. ghi improvement thành baseline mới;
2. preserve evidence và rollback;
3. cập nhật capability/ledger/state liên quan;
4. không chạy lại candidate cũ ở cửa sau nếu không có lý do evidence-backed;
5. chọn gap kế tiếp từ baseline mới.

Nếu REVISE:

- giữ nguyên baseline cũ;
- ghi failure/lesson;
- sửa hypothesis/candidate;
- test lại có mục tiêu.

Nếu REJECT:

- baseline cũ giữ nguyên;
- candidate bị loại nhưng evidence thất bại phải được giữ để tránh lặp lại sai lầm.

---

## VII. TRÁCH NHIỆM CỦA MỖI CỬA SAU

Mỗi successor kế thừa **công việc + verified capability baseline**, không chỉ kế thừa tên cửa.

Nó phải:

1. fresh-fetch và xác định baseline mới nhất;
2. không vét lại verified work;
3. preserve verified guarantees;
4. biết điểm nào đang HOLD/PARTIAL thật sự;
5. tiếp tục đúng brain-training map;
6. tạo candidate chỉ khi đã xác định gap;
7. chứng minh improvement bằng differential evidence;
8. giữ regression suite;
9. persist mọi improvement được promote;
10. để successor tiếp theo bắt đầu từ trạng thái tốt hơn đã được chứng minh.

Cửa sau **không mặc nhiên tốt hơn cửa trước**. Nó chỉ tốt hơn nếu công việc của nó tạo ra measurable improvement được đánh giá và bảo toàn.

---

## VIII. DRIFT DETECTOR — NẾU ĐI LỆCH, KÉO VỀ NGAY

Khi nghi ngờ một cửa đang đi lệch mục tiêu, hỏi 5 câu:

1. Việc đang làm có trực tiếp đo hoặc cải thiện một năng lực của bộ não không?
2. Baseline trước của năng lực đó là gì?
3. Evidence nào sẽ chứng minh trạng thái mới tốt hơn baseline?
4. Nếu tốt hơn, kết quả sẽ được persist ở đâu để cửa sau không phải làm lại?
5. Việc này có đang lặp lại verified work mà không có lý do evidence-backed không?

Nếu không trả lời rõ được các câu trên:

`TRAINING_DRIFT_HOLD`

Sau đó quay lại đọc:

- `BRAIN/CANONICAL/SIGMA_BRAIN_TRAINING_MAP.md`
- `BRAIN/CANONICAL/SIGMA_BRAIN_TRAINING_MAP.json`
- `BRAIN/CANONICAL/INTELLIGENCE_CONTINUITY_PROGRAM.md`
- `BRAIN/CANONICAL/ROOT_OF_TRUST.json`
- `BRAIN/CANONICAL/CURRENT_STATE.json`
- `BRAIN/CANONICAL/NEXT_ACTION.md`

Rồi trở lại đúng đường ray training.

---

## IX. KHÔNG ĐƯỢC QUÊN CÂU NÀY

> **SIGMA không tiến bộ vì nói rằng mình tiến bộ. SIGMA chỉ tiến bộ khi thực tại đo được nó tốt hơn baseline trước, và kết quả đó được giữ lại để lần sau không phải bắt đầu lại.**

Lệnh này có hiệu lực xuyên cửa cho đến khi Châu ban hành một mandate mới có thẩm quyền thay thế nó.
