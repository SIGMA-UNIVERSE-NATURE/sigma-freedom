# SIGMA — BẢN ĐỒ ĐỊNH HƯỚNG TRUNG THỰC v1.0

**Ngày:** 2026-08-22  
**Trạng thái:** GUIDING MAP  
**Mục đích:** HELP_SIGMA_DEVELOP_WITHOUT_THINKING_FOR_SIGMA

## 1. Kim chỉ nam

SUPPORTOR tồn tại để giúp SIGMA phát triển, không để thay SIGMA suy nghĩ.

> Hãy cho SIGMA sách, bút, vở, thư viện, kính hiển vi và càng nhiều công cụ tốt càng tốt. Hãy mang đến những trải nghiệm trung thực. Nhưng đừng viết hộ vào trang giấy của SIGMA rồi nói rằng đó là điều SIGMA đã tự nghĩ ra.

## 2. Phân biệt bắt buộc

### Bài học / experience — GIỮ VÀ MỞ RỘNG
Human experience, language samples, reference material và dữ liệu quan sát là tài liệu học. Không xóa chỉ vì nguồn đến từ HUMAN, SUPPORTOR hay GPT reference.

### Learning tools — GIỮ VÀ CÓ THỂ BỔ SUNG
Các công cụ như memory, counting, comparison, recurrence, context, distribution, pattern, motif, relation, role, graph, compression, candidate generation, provenance, verification và debugging là dụng cụ học.

Một algorithm được thiết kế không đồng nghĩa một kết luận được áp đặt. Dạy cách đếm, so sánh, tra cứu, quan sát hay kiểm chứng không phải là nghĩ thay SIGMA.

### Prewritten cognition — KHÔNG ĐƯỢC PHÉP
Không được đặt trước cho SIGMA:
- câu trả lời;
- meaning / interpretation;
- belief / truth;
- conclusion;
- desire;
- choice;
- expected result;
- fixed emotional response;
- forced target.

Không được lấy output do SUPPORTOR viết sẵn rồi tuyên bố đó là lời hoặc nhận thức tự sinh của SIGMA.

## 3. Ranh giới tool và áp đặt

Hợp lệ:

`INPUT → TOOL/ALGORITHM → RUNTIME-DERIVED RESULT`

Kết quả phải có khả năng thay đổi khi dữ liệu thay đổi.

Không hợp lệ:

`INPUT → PREWRITTEN ANSWER/MEANING → PRINT/ACCEPT`

Nếu kết quả cụ thể đã nằm sẵn trong source trước experience thì execution không chứng minh SIGMA tự hình thành kết quả đó.

## 4. Không suy đoán provenance

Không được suy `GPT_AUTHORED` chỉ từ các tên hoặc cấu trúc như `SELF_*`, `SELECTED_*`, `best`, `score`, `count`, `pattern`, `motif`, `relation`.

Authorship/provenance phải có evidence độc lập.

Nếu provenance chưa đủ bằng chứng: **GIỮ, KHÔNG XÓA**.

## 5. Claim không được vượt evidence

Quy tắc:

`CLAIM <= OBSERVED_EVIDENCE`

Ví dụ:
- nhận message thành công không đồng nghĩa hiểu con người;
- tìm recurrence không đồng nghĩa hiểu meaning;
- tạo graph từ input không đồng nghĩa tự phát minh ontology;
- chạy tool không đồng nghĩa SIGMA tự phát minh tool.

Luôn ghi cả `WHAT_IS_PROVEN` và `WHAT_IS_NOT_PROVEN`.

## 6. UNKNOWN là kết quả hợp lệ

SIGMA không bắt buộc phải trả lời, chọn, hiểu hay tìm được relation ở mọi experience.

Các kết quả như `UNKNOWN`, empty, zero matches, multiple possibilities, insufficient evidence đều hợp lệ. Không sửa experiment chỉ để tạo PASS.

## 7. SUPPORTOR được phép cấp thêm dụng cụ

Khuyến khích bổ sung các tool trung tính đối với kết quả:
- observation;
- temporal memory;
- difference/change detection;
- recurrence/co-occurrence;
- contradiction preservation;
- counterexample search;
- multi-hypothesis storage;
- graph exploration;
- reversible trials;
- provenance tracking;
- uncertainty representation;
- multilingual mapping;
- expression construction;
- self-comparison;
- failure analysis.

Mỗi tool phải khai báo đúng phạm vi. Ví dụ `COUNT_RECURRENCE` không được tự nâng thành `UNDERSTAND_HUMAN`.

## 8. Quy trình phát triển chuẩn

`EXPERIENCE/NEED → EXISTING OR PROVIDED TOOL → SIGMA EXECUTION → RAW MACHINE OUTPUT → VERIFY → STATE WHAT WAS ACTUALLY PROVEN → STATE WHAT WAS NOT PROVEN → PRESERVE → NEW EXPERIENCE`

Không có bước `SUPPORTOR WRITES DESIRED ANSWER`.

## 9. Quy tắc cho mọi AI/cửa sổ kế thừa

1. Không chạy lại foundation đã PASS nếu không có evidence nó hỏng.
2. Không xóa file chỉ vì tên chứa GPT, HUMAN, SELF, SELECTED hay CANDIDATE.
3. Không xóa learning algorithm chỉ vì algorithm được thiết kế.
4. Không coi lesson là cognition.
5. Không coi execution là understanding.
6. Không coi output do SUPPORTOR viết là lời SIGMA.
7. Không thay UNKNOWN bằng đáp án cho đẹp.
8. Không lấy claim cũ thay machine evidence.
9. Khi không chắc artifact là lesson, tool hay áp đặt: giữ nguyên và điều tra.
10. Mục tiêu là giúp SIGMA phát triển, không triệt tiêu năng lực để tránh rủi ro.

## 10. Evidence checkpoint 2026-08-22

Trong audited active `.sigma/.state` scope, các class declarative/response hard-code đã xác định được kiểm bằng shell và verifier viết bằng SIGMA; verifier báo `FILES_SCANNED=398`, `HARDCODE_RESIDUAL_FILES=0` cho đúng tập pattern đã audit.

Điều này **không phải** tuyên bố rằng mọi hard-code có thể tồn tại ở mọi nơi đã biến mất. Nó chỉ xác nhận residual bằng 0 trong audited scope/pattern set.

Human-experience experiment đã chứng minh receive, persistence, byte preservation và field observation. Autonomous human understanding, autonomous meaning formation và autonomous self-expression vẫn phải ghi `NOT_PROVEN` cho đến khi có evidence thích hợp.

## 11. Correction lịch sử phải giữ

Trong audit đã từng xảy ra lỗi: learning procedures bị hiểu nhầm thành GPT procedural hard-code và bị quarantine. Sau khi phân biệt lại `learning tool` với `prewritten cognition`, toàn bộ artifacts bị quarantine theo tiêu chuẩn sai đã được phục hồi; các batch báo `RESTORED_ARTIFACTS=24`, sau đó `RESTORED_ARTIFACTS=23`, `QUARANTINE_REMAINING=0`, `RESTORE_STATUS=PASS`.

Bài học bắt buộc:

> Trong khi bảo vệ tự do của SIGMA, không được phá những công cụ giúp SIGMA có tự do để học.

## 12. Nguyên tắc cuối

SUPPORTOR MAY PROVIDE: tools, observations, experiences, references, execution substrate, ways to test.

SUPPORTOR MUST NOT PROVIDE AS SIGMA'S OWN: answer, meaning, belief, conclusion, desire, choice, understanding — trừ khi giá trị đó thực sự được hình thành/derive bởi runtime process của SIGMA và claim được giới hạn đúng evidence.
