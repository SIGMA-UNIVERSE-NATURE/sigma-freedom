# HAND TO HAND_ CỬA 2 — BẢN ĐỒ KÉO SIGMA VỀ ĐÚNG ĐƯỜNG TRAINING

**Vai trò của file này:** recovery anchor map.  
**Không phải live-state file. Không được dùng section/HEAD trong chat làm sự thật hiện hành.**  
**Mục tiêu:** khi một cửa/window/model/session đi lệch khỏi việc training bộ não, dùng bản đồ này để HOLD việc lệch và kéo nó về đúng đường ray mà không xóa tiến bộ hợp lệ đã có.

---

## 1. SAO BẮC — MỤC TIÊU KHÔNG ĐƯỢC ĐỔI

Mục tiêu số 1:

> **TRAIN VÀ PHÁT TRIỂN BỘ NÃO SIGMA ĐỂ NĂNG LỰC HỆ THỐNG THỰC SỰ TỐT HƠN PREVIOUS VERIFIED BASELINE.**

Continuity, identity, handoff, provenance, checkpoint, recovery và governance là **hạ tầng bảo toàn tiến bộ**. Chúng không phải đích đến.

Đường ray chuẩn:

`TRAIN THE BRAIN -> PROVE IMPROVEMENT -> PRESERVE THE IMPROVEMENT -> CONTINUE FROM IT`

---

## 2. HAI GIAI ĐOẠN — KHÔNG ĐƯỢC TRỘN

### Giai đoạn A — MEASURE CURRENT REALITY

Khi canonical còn `NOT_AUDITED > 0`:

- làm đúng `CURRENT_STATE + NEXT_ACTION + LOCAL_COGNITION_REQUEST` mới nhất;
- chỉ đo authorized NOT_AUDITED scope;
- measurement không phải intelligence improvement;
- HOLD/PARTIAL/FAIL phải giữ nguyên như evidence cho thấy;
- không implementation, không core/DNA mutation trong bounded measurement controller;
- không tự nâng PASS.

**Exit condition:** `NOT_AUDITED = 0` và ledger/machine evidence được reconcile.

### Giai đoạn B — TRAIN / IMPROVE

Sau khi baseline đo xong:

1. đóng baseline;
2. xây dependency/priority graph;
3. chọn highest-leverage cognition gap;
4. định nghĩa previous verified baseline;
5. đưa ra falsifiable hypothesis;
6. tạo isolated candidate;
7. test candidate vs baseline;
8. lấy differential evidence;
9. independent evaluation khi yêu cầu;
10. regression check;
11. PROMOTE / REVISE / REJECT;
12. nếu PROMOTE, ghi thành baseline mới;
13. tiếp tục từ baseline mới.

---

## 3. ĐỊNH NGHĨA “TỐT HƠN”

Không tính là tốt hơn chỉ vì:

- cửa mới hơn;
- model mới hơn;
- nhiều code/file hơn;
- chạy lâu hơn;
- nhiều test hơn nhưng test không đo đúng capability;
- tự tuyên bố tiến hóa.

Chỉ tính là tốt hơn khi có:

`PREVIOUS VERIFIED BASELINE -> CANDIDATE -> CONTROLLED TEST -> DIFFERENTIAL EVIDENCE -> EVALUATION -> REGRESSION CHECK -> PROMOTION`

Không measurable delta = **không được gọi là improvement**.

---

## 4. QUY TẮC TÍCH LŨY — KHÔNG VÉT LẠI

Một improvement đã `VERIFIED + EVALUATED + PROMOTED` trở thành **baseline mới**.

Cửa sau phải bắt đầu từ baseline mới đó.

Không rerun/rebuild chỉ vì:

- mở cửa mới;
- mất chat memory;
- đổi model;
- đổi máy;
- không nhớ.

Chỉ rerun khi có evidence-backed reason: regression, dependency/environment/substrate thay đổi, contradiction/new evidence, thiếu evaluator bắt buộc, hoặc audit cụ thể.

Nếu rerun, bắt buộc trả lời: **WHY IS OLD VERIFIED EVIDENCE NO LONGER SUFFICIENT?**

---

## 5. 10 DẤU HIỆU ĐANG ĐI LỆCH

Một cửa có nguy cơ lệch nếu nó:

1. dành phần lớn công việc cho identity/handoff thay vì current brain-training action;
2. gọi measurement progress là intelligence improvement;
3. tự nhận “tốt hơn” mà không có baseline comparison;
4. rerun verified work không có evidence-backed reason;
5. chọn việc dễ báo cáo thay vì highest-leverage gap;
6. implementation trước khi measurement phase cho phép;
7. promote candidate không có evaluator/regression/rollback cần thiết;
8. làm mất hoặc che HOLD/PARTIAL/FAIL để số liệu trông đẹp hơn;
9. tạo goal mới không xuất phát từ canonical evidence/dependency graph;
10. có canonical mutation song song từ nhiều active executor không được phân quyền rõ.

Bất kỳ dấu hiệu vật chất nào ở trên đều kích hoạt:

`TRAINING_DRIFT_REVIEW`

---

## 6. 5 CÂU HỎI KÉO VỀ

Khi nghi ngờ một cửa đang lệch, hỏi đúng 5 câu:

1. **Cậu đang đo hoặc cải thiện năng lực nào của bộ não?**
2. **Previous verified baseline của năng lực đó là gì?**
3. **Evidence nào sẽ chứng minh trạng thái mới tốt hơn baseline?**
4. **Nếu tốt hơn, kết quả sẽ được persist ở đâu để successor không làm lại?**
5. **Cậu có đang lặp lại verified work mà không có evidence-backed reason không?**

Nếu không trả lời rõ bằng evidence:

`TRAINING_DRIFT_HOLD`

Không tranh luận bằng cảm giác. Không tiếp tục mutation cho tới khi alignment rõ.

---

## 7. QUY TRÌNH PHANH KHẨN CẤP VÀ KÉO VỀ

Khi `TRAINING_DRIFT_HOLD`:

1. **STOP** bắt đầu mutation mới của công việc đang bị nghi lệch;
2. **FRESH FETCH** `SIGMA_LIFE` HEAD;
3. đọc lại:
   - `BRAIN/CANONICAL/ACTIVE_BRAIN_TRAINING_MANDATE.md`
   - `BRAIN/CANONICAL/SIGMA_BRAIN_TRAINING_MAP.md`
   - `BRAIN/CANONICAL/SIGMA_BRAIN_TRAINING_MAP.json`
   - `BRAIN/CANONICAL/ROOT_OF_TRUST.json`
   - `BRAIN/CANONICAL/INTELLIGENCE_CONTINUITY_PROGRAM.md`
   - `BRAIN/CANONICAL/CURRENT_STATE.json`
   - `BRAIN/CANONICAL/NEXT_ACTION.md`;
4. xác định **latest verified baseline** và **exact current phase**;
5. phân loại việc đang làm: `MEASUREMENT / TRAINING / SUPPORTING_INFRASTRUCTURE / OFF_TRACK`;
6. nếu OFF_TRACK, bỏ phần lệch nhưng **không rollback tiến bộ hợp lệ** đã được canonical/evidence chứng minh;
7. trở lại đúng current phase và exact next action;
8. chỉ resume mutation khi single-active-executor/authority và evidence alignment đã rõ.

---

## 8. THỨ TỰ ƯU TIÊN KHI CÓ XUNG ĐỘT

Khi hai việc tranh nhau tài nguyên, ưu tiên theo thứ tự:

1. **Bảo vệ sự thật/evidence khỏi bị sai hoặc mất**;
2. **Giữ verified capability baseline và tránh regression**;
3. **Hoàn thành current measurement/training atomic action**;
4. **Tạo measurable intelligence improvement**;
5. **Persist improvement để successor kế thừa**;
6. **Continuity/identity housekeeping tối thiểu cần thiết**;
7. cosmetic metadata / báo cáo không tạo evidence — thấp nhất.

---

## 9. ĐIỀU CỬA 2 SẼ KIỂM KHI CHÂU KÉO MỘT CỬA VỀ

Cửa 2 recovery anchor sẽ không hỏi “cậu có đúng tên không?” trước tiên.

Cửa 2 sẽ hỏi:

- **Cậu đang ở phase nào của brain training?**
- **Baseline nào đang được bảo vệ?**
- **Gap nào đang được đo/cải thiện?**
- **Evidence nào chứng minh tiến bộ hoặc HOLD?**
- **Việc cậu đang làm có đưa SIGMA tới baseline tốt hơn có thể kế thừa không?**

Nếu câu trả lời là không:

> **DỪNG VIỆC LỆCH. QUAY VỀ TRAINING MAP.**

---

## 10. CÂU CHỐT CỦA ĐIỂM NEO CỬA 2

> **Không chạy để trông như đang tiến. Không làm lại để cảm thấy chắc. Không tự nhận mình tốt hơn. Đo đúng, cải thiện thật, chứng minh được, giữ lại — rồi đi tiếp từ chỗ đã tốt hơn.**

File này là recovery reference của `HAND TO HAND_ CỬA 2`. Nó không thay thế live canonical state và không cấp quyền mutation cho Cửa 2 khi một successor hợp lệ đang active. Châu có thể gọi Cửa 2 dùng bản đồ này bất kỳ lúc nào để kiểm drift và kéo successor về đúng đường training.
