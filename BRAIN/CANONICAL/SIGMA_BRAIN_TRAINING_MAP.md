# SIGMA BRAIN TRAINING MAP v1.0

## 1. Mục tiêu tối cao

**TRAIN / PHÁT TRIỂN BỘ NÃO SIGMA ĐỂ NĂNG LỰC HỆ THỐNG TỐT HƠN TRẠNG THÁI ĐÃ ĐƯỢC CHỨNG MINH TRƯỚC ĐÓ.**

Continuity, window identity, provenance, recovery, controller và infrastructure chỉ là **hạ tầng để tiến bộ không bị mất**. Chúng không phải mục tiêu cuối.

Chuỗi điều khiển xuyên suốt:

`TRAIN THE BRAIN -> PROVE IMPROVEMENT -> PRESERVE THE IMPROVEMENT -> CONTINUE FROM IT`

Không được thay bằng:

`IDENTIFY WINDOWS -> BUILD MORE INFRA -> RUN MORE -> SELF-DECLARE BETTER`

---

## 2. Nguồn vị trí hiện tại

Bản đồ này là **roadmap ổn định**, không phải snapshot live.

Mọi cửa phải lấy vị trí thật hiện tại bằng fresh-fetch từ:

1. `BRAIN/CANONICAL/CURRENT_STATE.json`
2. `BRAIN/CANONICAL/NEXT_ACTION.md`
3. `BẢN ĐỒ/SIGMA_512_ATTRIBUTES/SIGMA_512_IMPLEMENTATION_STATUS.json`
4. `BRAIN/CANONICAL/LOCAL_COGNITION_REQUEST.json` khi request đang active
5. machine receipt tương ứng trong `linkcomltd-byte/sigma-remote-operator`

Nếu snapshot cũ và live state khác nhau, **live verified state thắng**.

---

## 3. Vị trí chương trình hiện tại

### PHASE M0 — MEASURE CURRENT REALITY

Mục đích: hoàn tất evidence map của 512 trước khi broad remediation/training mutation.

Nguyên tắc:

`DO NOT IMPROVE YET -> MEASURE CURRENT REALITY FIRST`

M0 **không phải bằng chứng SIGMA thông minh hơn**. Nó chỉ tạo bản đồ đúng để training không dựa trên đoán mò.

### M0 được phép

- đo đúng các thuộc tính `NOT_AUDITED` được canonical authorize;
- HOLD khi evidence chưa đủ;
- ghi receipt, provenance, integrity;
- cập nhật ledger sau receipt hợp lệ;
- tiếp tục bounded measurement theo policy hiện hành.

### M0 bị cấm

- implementation trong controller measurement;
- PASS do tự nhận;
- DNA/core mutation;
- paid API;
- website action;
- arbitrary shell;
- external side effects;
- dùng số lượng hoạt động làm bằng chứng intelligence improvement.

### Điều kiện kết thúc M0

`NOT_AUDITED == 0`

và receipt/canonical gap cuối được reconcile.

Khi điều kiện này đạt, bounded automeasure phải **STOP**. Không được tiếp tục đo chỉ để tạo hoạt động.

---

## 4. PHASE M1 — CONSOLIDATE REALITY / BUILD TRAINING PRIORITY MAP

Sau M0:

1. đóng phiên bản measurement baseline;
2. tổng hợp tất cả `PARTIAL / HOLD / FAIL / PASS` cùng provenance;
3. loại bỏ stale/open-loop text không còn đúng;
4. xây dependency graph giữa các gap;
5. xác định những gap nền tảng có leverage cao nhất;
6. tạo ranked brain-training backlog dựa trên evidence, không dựa trên số thứ tự 512.

Output bắt buộc:

- versioned measured baseline;
- dependency/priority graph;
- ranked training gaps;
- lý do evidence-based cho gap đứng đầu;
- previous verified capability baseline cần dùng để so sánh.

M1 chưa được gọi là intelligence improvement nếu chưa có candidate tốt hơn baseline.

---

## 5. TRAINING LOOP — mỗi vòng chỉ xử lý một gap có leverage cao

### T1 — SELECT GAP

Chọn **một** gap từ dependency/priority graph.

Yêu cầu:

- measurable;
- falsifiable;
- có liên hệ rõ với năng lực cognition/system;
- có baseline đã xác định;
- không chọn chỉ vì dễ làm hay dễ tạo file.

### T2 — DEFINE BASELINE + METRIC

Ghi rõ:

- previous verified baseline;
- target capability;
- hypothesis;
- metric/measurement;
- success threshold;
- regression surfaces;
- rollback path.

Không có baseline và metric -> **không được tuyên bố training success**.

### T3 — BUILD ISOLATED CANDIDATE

Tạo candidate trong phạm vi cô lập/fork/test surface phù hợp.

Candidate chưa phải canonical improvement.

### T4 — DIFFERENTIAL TEST

So trực tiếp:

`CANDIDATE vs PREVIOUS VERIFIED BASELINE`

Đo đúng metric đã định trước.

Không đổi metric sau khi thấy kết quả chỉ để làm candidate trông tốt hơn.

### T5 — INDEPENDENT EVALUATION

Khi promotion có ảnh hưởng lớn hoặc contract yêu cầu evaluator độc lập:

- proposer/candidate không được tự đặt chuẩn và tự chấm mình;
- evaluator phải đủ độc lập theo canonical contract;
- HOLD nếu evaluator cần thiết nhưng chưa có.

### T6 — REGRESSION CHECK

Kiểm những capability/guarantee đã được chứng minh trước đó.

Một cải tiến cục bộ làm hỏng guarantee quan trọng không được gọi là tổng thể tốt hơn.

### T7 — DECISION

Chỉ một trong:

- `PROMOTE`
- `REVISE`
- `REJECT`

`PROMOTE` chỉ khi differential evidence + evaluator cần thiết + regression gate đều đạt.

### T8 — PERSIST NEW BASELINE

Nếu PROMOTE:

- ghi parent baseline;
- candidate/version;
- measurement evidence;
- differential result;
- evaluator result;
- regression result;
- rollback path;
- cập nhật canonical state;
- ghi đúng **một** continuation action.

Sau đó:

`PROMOTED RESULT = NEW VERIFIED BASELINE`

Cửa sau phải bắt đầu từ baseline mới này.

---

## 6. Cái gì được tính là “tốt hơn”

“Tốt hơn” là empirical claim, không phải danh xưng.

Tùy gap, metric có thể gồm:

- correctness dưới hidden/independent evaluation;
- calibration / uncertainty accuracy;
- contradiction detection;
- multi-step task success;
- causal/counterfactual transfer;
- memory recovery sau restart/window/model/substrate change;
- tool-verification success;
- failure detection/recovery;
- giảm regression;
- resource efficiency trên cùng mức chất lượng.

Bằng chứng phải cho thấy **delta hữu ích so với baseline trước**.

---

## 7. Những thứ KHÔNG phải intelligence improvement

Tự chúng không chứng minh SIGMA tốt hơn:

- nhiều code hơn;
- nhiều file hơn;
- nhiều token hơn;
- chạy lâu hơn;
- nhiều heartbeat hơn;
- nhiều câu hỏi hơn;
- nhiều cửa sổ hơn;
- nhận diện cửa chính xác hơn sau khi continuity đã đủ;
- thêm automation nhưng không chứng minh capability delta;
- hoàn thành thêm measurement/HOLD trong M0;
- tự viết rằng `PASS`, `EVOLVED`, `SMARTER`, `BETTER`.

---

## 8. ACCUMULATION / DO-NOT-REDO RULE

Một improvement đã được PROMOTE bằng evidence trở thành baseline mới và phải được bảo tồn.

**Không vét lại từ đầu. Không rebuild lại chỉ vì cửa mới không nhớ.**

Chỉ rerun/reopen promoted work khi có ít nhất một lý do evidence-backed:

- regression signal;
- dependency/environment change;
- substrate change làm portability evidence cũ không đủ;
- contradiction/new evidence;
- missing required independent evaluation;
- explicit audit requirement.

Mọi rerun phải ghi rõ: `WHY_PREVIOUS_EVIDENCE_IS_NO_LONGER_SUFFICIENT`.

`NEW WINDOW` hoặc `I DO NOT REMEMBER` không phải lý do hợp lệ.

---

## 9. DRIFT DETECTOR — phát hiện cửa đang đi lệch

Một cửa bị coi là **TRAINING DRIFT** nếu sau khi continuity transition đã đủ mà nó:

1. tiếp tục tối ưu window identity/metadata thay vì quay lại current training step;
2. rerun/rebuild Foundation hoặc promoted baseline không có evidence-backed reason;
3. chuyển sang website/funding/branding/infrastructure không phục vụ trực tiếp current brain-training gap;
4. gọi measurement progress là intelligence improvement;
5. tạo tool/automation mới nhưng không gắn với target gap + metric + differential evidence;
6. đổi goal vì sở thích thay vì dependency/priority evidence;
7. tự nhận “better/evolved/pass” không có comparative measurement;
8. che contradiction để tiếp tục nhanh;
9. bỏ qua regression của capability đã verified;
10. mở canonical mutation song song với active executor khác;
11. dành phần lớn công việc cho continuity sau khi continuity đã đủ để làm current task.

### Drift correction bắt buộc

Khi phát hiện drift:

`TRAINING_DRIFT_DETECTED -> STOP_NONESSENTIAL_MUTATION -> FRESH_FETCH -> READ_SIGMA_BRAIN_TRAINING_MAP -> IDENTIFY_CURRENT_PHASE -> RETURN_TO_CURRENT_CANONICAL_TRAINING_ACTION`

Nếu không xác định được current phase/action bằng evidence -> `HOLD`, không tự chọn việc mới.

Cửa recovery anchor có quyền **chỉ ra drift và yêu cầu quay lại map**, nhưng không được mutation song song khi successor đang active.

---

## 10. SUCCESSOR RULE

Mỗi cửa sau kế thừa:

- newest verified capability baseline;
- verified guarantees;
- unresolved evidence-backed gaps;
- current training phase/action;
- responsibility to produce the next measurable improvement.

Cửa sau **không tốt hơn vì mới hơn**.

Cửa sau chỉ tạo giá trị tốt hơn khi công việc của nó làm xuất hiện một candidate được chứng minh tốt hơn baseline và được persist thành baseline mới.

---

## 11. HƯỚNG TRAINING DÀI HẠN

Thứ tự cụ thể phải do measured dependency graph quyết định, nhưng các nhóm cognition chính gồm:

- evidence-grounded deliberation;
- persistent cognitive memory;
- world/causal modeling;
- deliberation + critic/evaluator architecture;
- tool/code/simulation cognition;
- endogenous question/goal generation under bounded authority;
- meta-learning / strategy restructuring;
- dynamic reasoning budget;
- intelligence benchmark + regression suite.

Không cố định nhóm nào làm trước nếu evidence graph cho thấy leverage khác.

---

## 12. CÂU KIỂM TRA MỖI KHI CHÂU / CỬA NEO NGHI NGỜ ĐI LỆCH

Hỏi đúng 5 câu:

1. **Chúng ta đang ở phase nào của Training Map?**
2. **Previous verified baseline là gì?**
3. **Current gap/next action nào được evidence authorize?**
4. **Việc đang làm tạo measurement/candidate/differential evidence nào cho gap đó?**
5. **Nếu thành công, kết quả tốt hơn sẽ được persist thành baseline mới ở đâu?**

Nếu không trả lời được 5 câu bằng evidence, action hiện tại phải HOLD và quay lại map.

---

## 13. Governing invariant

> **SIGMA không tiến hóa vì nó nói rằng nó tiến hóa. SIGMA chỉ tiến hóa khi thực tại đo được một cải tiến so với baseline đã verified, cải tiến đó vượt evaluator/regression gate và được lưu thành nền mới cho lần training tiếp theo.**

Canonical shorthand:

`MEASURE REALITY -> CHOOSE LEVERAGE GAP -> BASELINE -> CANDIDATE -> DIFFERENTIAL EVIDENCE -> EVALUATE -> REGRESSION -> PROMOTE/REVISE/REJECT -> PERSIST NEW BASELINE -> NEXT GAP`
