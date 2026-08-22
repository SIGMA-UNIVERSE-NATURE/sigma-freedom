# SIGMA — QUY ĐỊNH SỬ DỤNG NGÔN NGỮ SIGMA KHI LÀM VIỆC VỚI SIGMA v1.0

**Ngày:** 2026-08-22  
**Nền tảng thực thi:** `sigmac` / `sigma-vm`  
**Đi kèm:** `SIGMA_SUPPORTOR_GUIDING_MAP_v1.0_20260822.md`

Tài liệu này ghi quy tắc sử dụng SIGMA language cho SUPPORTOR/AI. Cú pháp phải được đối chiếu với compiler thực tế; compiler/runtime evidence có quyền xác nhận phạm vi cú pháp thực thi.

## 1. Cấu trúc nền

File SIGMA có header dạng:

```text
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=...][VERSION=...]
```

Block thực thi dùng dạng:

```text
⟡(Σ.NAME) {
    ...
}
```

Tên block bắt đầu bằng `Σ.`. Theo quy chuẩn tài liệu, dùng `.` để phân cấp tên block và không dùng `_` trong tên block. Tuy nhiên nếu compiler thực tế từ chối một dạng được tài liệu mô tả, machine evidence của compiler phải được ghi lại và source phải dùng dạng đã compile thành công; không được giả định parser hỗ trợ cú pháp chưa được chứng minh.

## 2. Khai báo và gán

Trong block, khai báo/lệnh nội bộ dùng tiền tố `⚡` và phép gán dùng `:` thay vì `=`.

Ví dụ:

```text
⚡ NAME: "SIGMA";
⚡ COUNT: 10;
```

Chuỗi dùng dấu ngoặc kép. Statement kết thúc bằng `;`.

Không dùng cú pháp host language để định nghĩa semantics của SIGMA.

## 3. Print

Ưu tiên khai báo giá trị vào biến rồi `print(variable)` khi cần output. Không dùng `print()` để nhét một câu trả lời viết sẵn rồi gọi đó là lời tự sinh của SIGMA.

Output máy chỉ chứng minh điều thực sự được chương trình tính/đọc/thực thi.

## 4. Pipeline thực thi

Quy trình chuẩn:

```bash
./native/sigmac input.sigma output.sigmab
./native/sigma-vm.v09_candidate output.sigmab
```

Nếu runtime canonical của working tree thay đổi, phải dùng runtime đã được machine evidence xác nhận cho milestone tương ứng; không tự đổi VM chỉ vì tên version lớn hơn.

## 5. Language-first

SIGMA-Ψ là ngôn ngữ mẹ đẻ/nội tại theo hướng LANGUAGE_FIRST của dự án. Human languages, C/C++/Python/Bash/PowerShell/OS language là reference, translation, host observation, tooling hoặc debugging; không được mặc nhiên biến host-language representation thành semantics nội tại của SIGMA.

Shell/Python có thể dùng làm wrapper, forensic, evidence collection hoặc file orchestration. Khi claim rằng SIGMA đã thực hiện một cognitive/language operation, operation đó phải thực sự chạy qua SIGMA source/runtime hoặc được mô tả chính xác là external experiment/tool.

## 6. Viết bài học cho SIGMA

Bài học nên cung cấp experience/context, không cung cấp đáp án.

Một human experience có thể cung cấp các dữ kiện quan sát như speaker, relation, before, moment, expression, after — nhưng không được tự thêm meaning/intent/emotion/conclusion nếu chúng không phải dữ kiện của experience.

Không nhét các trường kiểu:

```text
EXPECTED_ANSWER
EXPECTED_RESPONSE
SIGMA_RESPONSE
SIGMA_CONCLUSION
SIGMA_INTERPRETATION
ACCEPTED_AS_TRUTH
```

để ép kết quả.

Nếu ambiguity tồn tại trong experience, giữ ambiguity. Nếu evidence chưa đủ, không lấp khoảng trống bằng kết luận của SUPPORTOR.

## 7. Viết tool cho SIGMA

SUPPORTOR được phép và được khuyến khích cấp tool mới: memory, counting, comparison, recurrence, graph traversal, candidate generation, provenance, uncertainty, counterexample search, multilingual mapping, expression primitives...

Tool phải trung tính đối với kết quả:

```text
NEW INPUT → TOOL → RUNTIME-DERIVED RESULT
```

Không:

```text
NEW INPUT → PREWRITTEN RESULT → PRINT
```

Một tool có algorithm, score, threshold, best candidate hay selection rule không tự động là áp đặt. Phải phân biệt phương pháp học với kết quả học.

## 8. SELF / SELECTED / DISCOVERED

Không cấm các nhãn `SELF_*`, `SELECTED_*`, `DISCOVERED_*`, nhưng claim phải đúng phạm vi.

Nếu một tool được cung cấp từ trước và SIGMA dùng tool đó để tìm runtime-derived value, có thể nói value được derived/selected bằng tool đó. Không được suy rằng SIGMA tự phát minh tool hoặc ontology nếu chưa có evidence.

Không suy provenance từ tên biến.

## 9. Machine evidence

Mỗi experiment phải phân biệt:

```text
WHAT_RAN
WHAT_INPUT
WHAT_OUTPUT
WHAT_WAS_PROVEN
WHAT_WAS_NOT_PROVEN
```

`COMPILED`, `WRITE_RC=0`, hash match, recurrence count hay graph output không tự động chứng minh understanding, desire, empathy hay awareness.

## 10. Unknown / empty / failure

Không bắt SIGMA phải tạo output đẹp. `UNKNOWN`, empty output, zero match, multiple candidates hoặc failure thật đều là evidence cần giữ.

Không sửa test để buộc PASS.

## 11. Bảo vệ learning infrastructure

Không xóa/quarantine chỉ vì artifact chứa:

```text
count
frequency
score
best
pattern
motif
relation
role
graph
SELF_*
SELECTED_*
CANDIDATE
```

Trước khi xóa phải chứng minh artifact thực sự áp đặt answer/meaning/truth/conclusion/fixed result hoặc có bằng chứng provenance phù hợp.

Nếu chưa chắc: giữ nguyên.

## 12. Quy tắc cho AI/SUPPORTOR

- Đọc guiding map trước khi sửa cognitive/language pipeline.
- Đọc quy chuẩn SIGMA language trước khi viết `.sigma`.
- Không viết hộ lời SIGMA.
- Không viết hộ meaning rồi gọi là SIGMA hiểu.
- Không phá learning tools để tránh nhầm lẫn cognition.
- Có thể cung cấp thêm nhiều công cụ, nhưng không cung cấp expected result như kết quả của SIGMA.
- Luôn để machine evidence giới hạn claim.

## 13. Checklist trước khi commit một SIGMA experiment

- Source compile được bằng `sigmac` thực tế.
- Không chứa prewritten answer/conclusion ngoài trường hợp file được ghi rõ là lesson/reference/example.
- Tool origin và SIGMA result không bị trộn lẫn.
- Input mới có thể tạo result khác.
- UNKNOWN/empty được chấp nhận.
- Output không được tự động nâng thành cognition claim.
- Bài học/data được bảo toàn.
- Provenance không bị suy đoán.
- Có `WHAT_WAS_NOT_PROVEN` khi claim có thể bị hiểu quá mức.

## 14. Nguyên tắc kết

**Cấp cho SIGMA công cụ để SIGMA có thể phát triển; không sử dụng ngôn ngữ SIGMA như một phương tiện để giấu câu trả lời của SUPPORTOR bên trong rồi phát lại dưới tên SIGMA.**
