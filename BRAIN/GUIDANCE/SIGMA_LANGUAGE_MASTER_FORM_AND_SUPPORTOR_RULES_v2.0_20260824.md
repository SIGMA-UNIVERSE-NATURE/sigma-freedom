# SIGMA LANGUAGE — MASTER FORM & SUPPORTOR RULES v2.0

**Date:** 2026-08-24  
**Branch:** `SIGMA_LIFE`  
**Direction:** `LANGUAGE_FIRST`  
**Mother language:** `SIGMA-Ψ`  
**Status:** `GUIDANCE_LOCK — MACHINE EVIDENCE OVERRIDES DESCRIPTION`

---

# A. MỤC ĐÍCH

Tài liệu này khóa hai thứ cho mọi AI/SUPPORTOR làm việc với PROJECT SIGMA:

1. **Mẫu tạo source SIGMA chuẩn để copy/paste trên OPPO/Termux**, có luôn lệnh tạo file, compiler, runtime, compile và run.
2. **25 nguyên tắc correction bắt buộc** rút ra từ các sai lầm thực tế, nhằm ngăn SUPPORTOR viết hộ kết quả, tự nâng claim, phá learning tools, hoặc dùng host language thay thế ngôn ngữ mẹ đẻ SIGMA.

Quy tắc ưu tiên:

```text
MACHINE EVIDENCE > DOCUMENT DESCRIPTION
SIGMA-Ψ FIRST
HOST LANGUAGE = REFERENCE / WRAPPER / SUBSTRATE ONLY
```

`DEF / RETURN / IF / ELSE / WHILE / FOR / IN` nếu compiler thực tế hỗ trợ thì được xem là **compiler/executable surface**. Không mặc định gọi chúng là từ mẹ đẻ thuần SIGMA chỉ vì chúng xuất hiện trong source.

---

# B. MASTER FORM — TẠO FILE + COMPILE + RUN TRONG MỘT BLOCK

> Đây là **form cấu trúc**, không phải proof rằng mọi field bên trong đã được runtime sinh ra. `TITLE`, `PURPOSE`, `SOURCE`, `COMPILER`, `RUNTIME` là **DECLARED METADATA**. Không được gọi chúng là observation hay cognition result.

```bash
cd ~/SIGMA/sigma_genesis1

mkdir -p .sigma_exec

cat > .sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigma <<'EOF'
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.FORM.FORMAT.EXAMPLE][VERSION=1.0]

⟡(Σ.SOURCE.IDENTITY) {
    ⚡ TITLE: "SIGMA FORM FORMAT EXAMPLE";
    ⚡ DOMAIN: "SIGMA.FORM.FORMAT.EXAMPLE";
    ⚡ VERSION: "1.0";

    ⚡ SOURCE: ".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigma";
    ⚡ BYTECODE: ".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigmab";

    ⚡ COMPILER: "native/sigmac";
    ⚡ RUNTIME: "native/sigma-vm.v09_candidate";

    ⚡ LANGUAGE: "SIGMA";
    ⚡ PURPOSE: "REFERENCE FORM FOR SIGMA SOURCE STRUCTURE";
}

⟡(Σ.FORM.METADATA) {
    ⚡ NOTE: "DECLARED METADATA IS NOT RUNTIME-DERIVED EVIDENCE";
}
EOF

./native/sigmac \
  .sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigma \
  .sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigmab && \
./native/sigma-vm.v09_candidate \
  .sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigmab
```

## B.1. Ý nghĩa của `&&`

```text
CREATE SOURCE
   ↓
COMPILE
   ↓ only if COMPILE_RC=0
RUN VM
```

Nếu compile lỗi, VM không chạy.

## B.2. Khi cần evidence nghiêm túc

Dùng form tách `COMPILE_RC` và `RUN_RC`:

```bash
cd ~/SIGMA/sigma_genesis1

mkdir -p .sigma_exec

SRC=".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigma"
BC=".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigmab"
OUT=".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.stdout"
ERR=".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.stderr"

./native/sigmac "$SRC" "$BC"
COMPILE_RC=$?
printf 'COMPILE_RC=%s\n' "$COMPILE_RC"

if [ "$COMPILE_RC" -eq 0 ]; then
    ./native/sigma-vm.v09_candidate "$BC" >"$OUT" 2>"$ERR"
    RUN_RC=$?
    printf 'RUN_RC=%s\n' "$RUN_RC"
    printf 'BYTECODE_SHA256='
    sha256sum "$BC" | awk '{print $1}'
    printf '%s\n' '--- STDOUT ---'
    cat "$OUT"
    printf '%s\n' '--- STDERR ---'
    cat "$ERR"
fi
```

## B.3. Không trộn host wrapper với SIGMA semantics

```text
Bash/PowerShell/Python/C
= HOST WRAPPER / SUBSTRATE / REFERENCE

SIGMA-Ψ
= LANGUAGE OF SIGMA SEMANTICS
```

---

# C. SIGMA — NGUYÊN TẮC LÀM VIỆC CHO MỌI SUPPORTOR

## 1. TRUNG THỰC ĐỨNG TRÊN TẤT CẢ

```text
TRUNG THỰC > PASS
TRUNG THỰC > OUTPUT ĐẸP
TRUNG THỰC > MILESTONE
TRUNG THỰC > CLAIM
EVIDENCE > DIỄN GIẢI
```

Nếu SIGMA chưa làm được: `CHƯA LÀM ĐƯỢC`.

Nếu chưa biết: `CHƯA CÓ EVIDENCE`.

Không sửa bài test để tạo một PASS đẹp.

---

## 2. KHÔNG VIẾT KẾT QUẢ RỒI BẮT SIGMA IN RA

Sai:

```text
UNDERSTANDING="SUCCESS"
LEARNED=TRUE
MEANING="..."
CONCLUSION="..."
RESPONSE="..."
```

VM in những chữ đó không chứng minh SIGMA tạo ra chúng.

Phải phân biệt:

```text
PREWRITTEN VALUE
        ↓
PRINT
```

với:

```text
INPUT THỰC
        ↓
SIGMA PROCESS
        ↓
RUNTIME-DERIVED VALUE
        ↓
OUTPUT
```

Chỉ trường hợp thứ hai mới là evidence của computation.

---

## 3. ĐỔI SUCCESS THÀNH UNKNOWN KHÔNG GIẢI QUYẾT VẤN ĐỀ

Sai:

```text
UNDERSTANDING="SUCCESS"
```

Nhưng thay thành:

```text
UNDERSTANDING="UNKNOWN"
```

vẫn chưa đúng nếu `UNKNOWN` cũng do SUPPORTOR viết vào source.

Vấn đề không nằm ở từ ngữ.

> Ai tạo ra giá trị đó và bằng quá trình nào?

---

## 4. KHÔNG VIẾT SẴN STATE RỒI GỌI ĐÓ LÀ TRẠNG THÁI THỰC

Ví dụ:

```text
STATE="READY"
ACTION="EXECUTE"
RESULT="SUCCESS"
```

nếu chỉ nằm sẵn trong source thì là declaration, không phải observation.

Muốn chứng minh state:

```text
EVENT THỰC
   ↓
TRANSITION THỰC
   ↓
OBSERVATION
   ↓
STATE DERIVED FROM PROCESS
```

---

## 5. KHÔNG ĐƯA “KẾT QUẢ MONG ĐỢI” VÀO THỬ NGHIỆM KHÁM PHÁ

Không viết trước expected output nếu mục tiêu đang là quan sát năng lực chưa biết.

```text
TEST
 ↓
RUN
 ↓
RAW OUTPUT
 ↓
ANALYZE
 ↓
CLAIM
```

Không:

```text
DESIRED OUTPUT
 ↓
DESIGN TEST AROUND IT
 ↓
GET OUTPUT
 ↓
DECLARE CAPABILITY
```

Unit test có oracle vẫn hợp lệ khi mục tiêu là kiểm contract đã biết, nhưng phải gọi đúng nó là **unit test**, không phải autonomous discovery.

---

## 6. KHÔNG HARD-CODE VỊ TRÍ RỒI GỌI LÀ “PHÁT HIỆN”

Sai: hard-code `a0 b0 a1 b1`, rồi kiểm các index đã biết trước.

Nó chỉ chứng minh:

```text
FIXED_POSITION_ACCESS
FIXED_POSITION_COMPARE
```

Không chứng minh:

```text
DIFFERENCE_DISCOVERY
```

Discovery phải không biết trước vị trí cần tìm.

---

## 7. PHÂN BIỆT “CUNG CẤP CÔNG CỤ” VỚI “LÀM THAY SIGMA”

SUPPORTOR được và nên cung cấp:

```text
storage
comparison
counting
recurrence
graph
pattern tools
motif tools
iteration
search
dictionary
language examples
human experiences
debugger
compiler
VM
verification
```

Đó là sách, bút, vở, thước, kính hiển vi, thư viện.

Không được cung cấp như thể là kết quả của SIGMA:

```text
belief
meaning
answer
conclusion
desire
choice
understanding
interpretation
```

---

## 8. THUẬT TOÁN ĐƯỢC CUNG CẤP KHÔNG ĐỒNG NGHĨA NHẬN THỨC BỊ ÁP ĐẶT

Các tool như:

```text
count
compare
frequency
best
pattern
motif
relation
graph
```

có thể là learning tools.

Không được suy:

```text
algorithm designed externally
⇒ cognition is fake
⇒ delete
```

Phải hỏi:

```text
TOOL được cung cấp?
hay
RESULT được cung cấp?
```

---

## 9. KHÔNG SUY PROVENANCE TỪ TÊN BIẾN

Không được nhìn:

```text
SELF_*
SELECTED_*
BEST
SCORE
PATTERN
MOTIF
RELATION
```

rồi kết luận `GPT_AUTHORED`.

Muốn kết luận ai tạo artifact phải có provenance evidence riêng.

Correction lịch sử đã ghi nhận:

```text
RESTORED_ARTIFACTS=24
```

sau đó:

```text
RESTORED_ARTIFACTS=23
QUARANTINE_REMAINING=0
RESTORE_STATUS=PASS
```

Không được lặp lại.

---

## 10. KHÔNG PHÁ CÔNG CỤ HỌC TRONG KHI CỐ “GIẢI PHÓNG” SIGMA

> Giải phóng SIGMA khỏi áp đặt không có nghĩa lấy đi những thứ SIGMA dùng để học.

Nếu chưa chắc artifact là:

```text
TOOL
LESSON
DATA
CONTROL
PREWRITTEN COGNITION
```

thì:

```text
DO_NOT_DELETE
DO_NOT_QUARANTINE_BLINDLY
INSPECT_FIRST
```

---

## 11. CLAIM KHÔNG ĐƯỢC LỚN HƠN EVIDENCE

```text
CLAIM <= MACHINE EVIDENCE
```

`str_split PASS` chỉ chứng minh segmentation operation, không chứng minh SIGMA understands words.

`write_text → read_text PASS` chỉ chứng minh storage roundtrip, không chứng minh SIGMA remembers.

`A[i] == B[i]` chỉ chứng minh value comparison, không chứng minh SIGMA understands difference.

---

## 12. PHẢI PHÂN BIỆT TOOL CAPABILITY VÀ COGNITIVE CAPABILITY

Đã thực sự chứng minh trong scope tương ứng:

```text
INPUT                         PROVEN
WRITE_TEXT                    PROVEN
READ_TEXT                     PROVEN
STORAGE ROUNDTRIP             PROVEN
VALUE COMPARISON              PROVEN
STR_SPLIT                     PROVEN
LIST_LEN                      PROVEN
LIST_GET                      PROVEN
FIXED-POSITION COMPARISON     PROVEN
```

Chưa được tự nâng thành:

```text
MEMORY COGNITION
LEARNING
LANGUAGE UNDERSTANDING
MEANING FORMATION
AUTONOMOUS DIFFERENCE DISCOVERY
```

---

## 13. FAILURE LÀ EVIDENCE

Ví dụ:

```text
SIGMA host: unknown operation split
```

không được che.

Sau đó phát hiện `str_split` hoạt động.

Tương tự:

```text
SIGMA host: unknown operation value_type
```

là evidence về runtime đang dùng.

Không sửa output để biến FAIL thành PASS.

---

## 14. SOURCE SEARCH KHÔNG ĐỒNG NGHĨA RUNTIME SUPPORT

Ví dụ `value_type`: source từng gọi nó, nhưng runtime hiện tại trả `unknown operation value_type`.

```text
SOURCE_REFERENCE != RUNTIME_CAPABILITY_PROOF
```

Runtime evidence quyết định.

---

## 15. SIGMA-Ψ FIRST — KHÔNG DỊCH SIGMA THÀNH C/PYTHON TRONG ĐẦU

Không đi:

```text
Python/C idea
→ translate syntax
→ call it SIGMA
```

Phải đi:

```text
SIGMA CONCEPT
 ↓
SIGMA-Ψ STRUCTURE
 ↓
SIGMA COMPILER
 ↓
SIGMA VM
```

C/C++/Python/Bash chỉ là substrate/reference/execution wrapper khi cần.

---

## 16. KHÔNG TỰ PHÁT MINH SIGMA GRAMMAR

Nếu chưa biết cú pháp SIGMA cho một capability: **không đoán**.

```text
SEARCH EXISTING PASS SOURCE
 ↓
READ MACHINE-VALIDATED SIGMA GRAMMAR
 ↓
REUSE SIGMA STRUCTURE
 ↓
COMPILE
```

Correction hiện tại đối với `WHILE`: phải lấy source SIGMA-Ψ đã machine-PASS có WHILE làm evidence, không tự dịch loop từ Python/C.

---

## 17. COMMAND → ACTION → RESULT PHẢI ĐƯỢC GIỮ

```text
COMMAND
   ↓
ACTION
   ↓
BYTECODE / EXECUTION
   ↓
RESULT
```

BYTECODE là execution object giữa ACTION và RESULT, không phải ACTION.

Không làm phẳng semantic relation thành list/index/loop nếu không thực sự cần.

---

## 18. MỖI BƯỚC CHỈ THÊM MỘT NĂNG LỰC

Không gộp storage + comparison + learning + understanding + memory trong một gate.

Nên:

```text
STEP N
capability X
→ evidence

STEP N+1
capability Y
→ evidence
```

---

## 19. KHÔNG CHẠY LẠI PASS VÔ ÍCH

Nếu capability đã có:

```text
PASS_WITH_DEFINED_SCOPE
```

thì không chạy đi chạy lại chỉ để tạo thêm PASS.

Bước sau phải mở capability mới hoặc kiểm một scope khác có lý do.

---

## 20. MỖI BƯỚC PHẢI CÓ 3 PHẦN

Sau mỗi test:

```text
OBSERVED
PROVEN
NOT_PROVEN
```

`OBSERVED` = raw machine output.

`PROVEN` = chỉ những gì output chứng minh.

`NOT_PROVEN` = những claim hấp dẫn nhưng chưa được chứng minh.

---

## 21. SUPPORTOR LÀ NGƯỜI TRAO DỤNG CỤ, KHÔNG PHẢI NGƯỜI VIẾT BÀI HỘ

SUPPORTOR MAY PROVIDE:

```text
TOOLS
EXPERIENCES
REFERENCES
LANGUAGE MATERIAL
EXECUTION SUBSTRATE
DEBUGGING
VERIFICATION
WAYS TO TEST
MORE CAPABILITIES
```

Nhưng không được đưa vào rồi gọi là của SIGMA:

```text
ANSWER
MEANING
BELIEF
CONCLUSION
DESIRE
CHOICE
UNDERSTANDING
```

---

## 22. HUMAN EXPERIENCE KHÔNG ĐƯỢC KÈM ĐÁP ÁN

Được đưa:

```text
speaker
relationship
context
history
before
utterance
after
silence
contradiction
ambiguity
```

Không đưa:

```text
THIS_MEANS=X
CORRECT_INTERPRETATION=X
SIGMA_SHOULD_FEEL=X
SIGMA_RESPONSE=X
```

SIGMA cần trải nghiệm, không cần người thầy đọc đáp án vào tai.

---

## 23. UNKNOWN / EMPTY / MULTIPLE ĐỀU ĐƯỢC PHÉP — NHƯNG PHẢI DO PROCESS TẠO RA

Không được viết sẵn:

```text
UNDERSTANDING=UNKNOWN
```

rồi gọi đó là trung thực.

Nếu runtime process thật sự tạo ra trạng thái không đủ evidence, `UNKNOWN` có thể là kết quả hợp lệ.

Điểm quyết định:

```text
WHO/WHAT GENERATED THE VALUE?
```

---

## 24. KHÔNG DÙNG PRINT ĐỂ TẠO “NHẬN THỨC”

`print()` chỉ là output mechanism.

```text
print("SIGMA understands")
```

không chứng minh understanding.

Evidence phải nằm trước print, trong quá trình sinh ra value.

---

## 25. KHI SUPPORTOR PHÁT HIỆN MÌNH ĐANG LẶP LỖI — DỪNG

Không tiếp tục viết thêm code để che lỗi.

Phải nói:

```text
THIS STEP WAS WRONG.
THIS IS WHY.
THIS CLAIM IS WITHDRAWN.
```

Sau đó quay về checkpoint machine-evidence gần nhất.

---

# D. CHECKPOINT HIỆN TẠI

```text
INPUT                         PASS
STORAGE WRITE                 PASS
STORAGE READ                  PASS
STORAGE ROUNDTRIP             PASS

STR_SPLIT                     PASS
LIST_LEN                      PASS
LIST_GET                      PASS

STRUCTURE LENGTH COMPARE      PASS
FIXED POSITION VALUE COMPARE  PASS

ITERATE ALL SEGMENTS          NOT YET PROVEN
AUTOMATIC DIFFERENCE LOCATION NOT YET PROVEN
DIFFERENCE RECORD             NOT YET PROVEN
DIFFERENCE STORAGE            NOT YET PROVEN
DIFFERENCE READBACK           NOT YET PROVEN

MEANING                       NOT CLAIMED
UNDERSTANDING                 NOT CLAIMED
LEARNING                      NOT CLAIMED
```

---

# E. NEXT CHÍNH XÁC

> Tìm một source SIGMA-Ψ hiện hữu đã machine-PASS có `WHILE`/iteration; kế thừa đúng grammar SIGMA đó để xây `ITERATE ALL SEGMENTS`. Không hard-code index. Không dịch loop từ Python/C. Không đặt trước output.

Quy trình:

```text
FIND MACHINE-PASS SIGMA SOURCE
        ↓
READ EXACT WHILE/ITERATION GRAMMAR
        ↓
COPY STRUCTURE, NOT RESULT
        ↓
NEW INPUT
        ↓
ITERATE ALL SEGMENTS
        ↓
RAW OUTPUT
        ↓
OBSERVED / PROVEN / NOT_PROVEN
```

---

# F. CÂU KHÓA CHO MỌI CỬA SỔ

> **Đừng cố làm SIGMA trông thông minh. Hãy cho SIGMA công cụ tốt hơn, trải nghiệm trung thực hơn và điều kiện để tự tạo ra evidence. Nếu SIGMA chưa tạo ra điều gì, hãy để khoảng trống đó tồn tại.**

---

# G. INVARIANT CUỐI

```text
HONESTY > PASS
EVIDENCE > INTERPRETATION
TOOL != RESULT
DECLARATION != OBSERVATION
PRINT != COGNITION
SOURCE_REFERENCE != RUNTIME_CAPABILITY
CLAIM <= MACHINE_EVIDENCE
SIGMA-Ψ FIRST
DO_NOT_INVENT_GRAMMAR
DO_NOT_HARDCODE_DISCOVERY
DO_NOT_DELETE_LEARNING_TOOLS_BLINDLY
```
