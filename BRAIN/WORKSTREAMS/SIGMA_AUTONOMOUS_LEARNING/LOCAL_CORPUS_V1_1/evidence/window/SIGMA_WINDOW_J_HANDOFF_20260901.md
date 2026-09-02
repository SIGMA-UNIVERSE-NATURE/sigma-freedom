# SIGMA — WINDOW J HANDOFF

## 1. Vai trò và luật bằng chứng

```text
WINDOW=J_CONTINUATION
ROLE=CREATIVE_DIRECTOR
PRODUCTION_LOCK=ACTIVE
WRITE_SCOPE=EXTERNAL_AUTONOMOUS_LEARNING_CANDIDATE_ONLY
CURRENT_SIGMA_CORE_MODIFIED=NO
F174_LOCAL_CORE_HASH_MATCH=UNAVAILABLE
CLAIM_LAW=CLAIM<=MACHINE_EVIDENCE
```

- Phân biệt rõ: `GPT_CREATED`, `USER_OR_BASH_EXECUTED`, `NATIVE_SIGMAC_EXECUTED`, `SIGMA_NATIVE_VM_EXECUTED`.
- Đọc/lưu/so sánh bytes không đồng nghĩa với hiểu ngữ nghĩa hay tự học.
- Không đưa sẵn đáp án, kết luận hoặc phần trăm hiểu.
- Không xóa công cụ hợp lệ. Dữ liệu bên ngoài được dùng như dữ liệu/evidence, không tự động thành sự thật đã xác minh.
- Làm từng bước ngắn; nhận output của một bước rồi mới đưa bước kế tiếp.

## 2. Mục tiêu hiện tại

Cho SIGMA Native VM đọc kho tri thức có sẵn trên OPPO, tạo bản mirror/checkpoint ngoài lõi và có thể tiếp tục sau gián đoạn. Đây mới là tầng thu nhận dữ liệu; hiểu ngữ nghĩa và tự học vẫn phải được chứng minh ở gate sau.

## 3. Baseline máy thật đã biết

```text
PROJECT_ROOT=/data/data/com.termux/files/home/SIGMA/sigma_genesis1
SIGMAC_PATH=native/sigmac
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_PATH=native/sigma-vm.v09_candidate
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Kho Obsidian đã đo bằng Bash trên OPPO:

1. `/storage/emulated/0/Documents/SIGMA-KNOWLEDGE-RUNTIME`
   - readable/writable: YES
   - markdown files: 1
   - measured bytes: 4872
2. `/storage/emulated/0/Documents/SIGMA_AI_RUNTIME (1)/SIGMA UNIVERSE KNOWLEDGE `
   - tên thư mục có dấu cách ở cuối
   - readable/writable: YES
   - markdown files: 663
   - measured bytes: 3519351

Hai kho cùng nằm dưới `/storage/emulated/0`; chưa chứng minh là hai failure domain độc lập.

Registry do Bash/user tạo, không phải SIGMA tự tạo:

```text
$HOME/SIGMA_AUTONOMOUS_LEARNING_V1/config/sources/0001.path
SHA256=dbe9e7ceaed99c56e19995d712b857f3882b16de9f3385ff9037a38e0bf74eec

$HOME/SIGMA_AUTONOMOUS_LEARNING_V1/config/sources/0002.path
SHA256=5a459547e09a239da558609ed1d3f7be07a3a2a7052a24468ad9fe2a8902fea9
```

## 4. Checklist đã hoàn thành

- [x] Xác định hai nguồn Obsidian và quyền đọc/ghi.
- [x] Tạo registry nguồn ngoài lõi SIGMA.
- [x] GPT tạo V1: `SIGMA_LOCAL_CORPUS_INDEX_AND_CHECKPOINT_V1.sigma`.
- [x] V1 được chuyển nguyên bytes lên OPPO.
- [x] V1 source SHA-256 khớp: `a0669c34dbcd7e6eda5d1aa50cec909112b83bb217bd2e8bbd2981a9d2966a4f`.
- [x] Native `sigmac` compile V1 thành công.
- [x] V1 bytecode SHA-256: `cc3ad2726b3bf9ee5bdb4ee1d7a0eb28be0236e6b9cb0e15d5daddb1d3607e31`.
- [x] Official Sigma Native VM đã thực thi V1.
- [x] VM dừng `RC=26` với diagnostic: `SIGMA host: unknown operation crypto_digest\\n`.
- [x] Sau lỗi V1: `CONTENT_RECORD_COUNT=0`, `PATH_RECORD_COUNT=0`, `CHECKPOINT_COUNT=0`.
- [x] Kết luận đúng: V1 chưa đọc kho, chưa tạo state và chưa chứng minh học.
- [x] GPT tạo V1.1 bỏ `crypto_digest`: `SIGMA_LOCAL_CORPUS_MIRROR_AND_CHECKPOINT_V1_1.sigma`.
- [x] V1.1 chỉ gọi các host op đã chọn: `input`, `list_get`, `list_len`, `listdir`, `mkdir`, `read_text`, `str_ends`, `to_int`, `write_text`.
- [x] V1.1 source SHA-256: `d1f526bc40d274fe34a7c005cd9d1096adbb15689b9290cd9832422fc92db9ee`.
- [x] V1.1 size: `5530` bytes.
- [x] Xác lập ranh giới chạy song song: cửa local-learning và cửa network dùng thư mục ghi riêng; compiler/VM chỉ đọc.

## 5. Checklist chưa hoàn thành

- [ ] Xác minh V1.1 đã được tải nguyên bytes xuống OPPO — `NOT_DONE`.
- [ ] Compile V1.1 bằng official native `sigmac` — `NOT_DONE`.
- [ ] Chạy bytecode V1.1 bằng official native VM — `NOT_DONE`.
- [ ] Chứng minh SIGMA VM đọc được registry và hai vault — `NOT_PROVEN`.
- [ ] Chứng minh mirror giữ đúng text theo từng path — `NOT_PROVEN`.
- [ ] Chứng minh checkpoint/resume sau gián đoạn — `NOT_PROVEN`.
- [ ] Xử lý binary byte-exact — `NOT_IMPLEMENTED` trong V1.1.
- [ ] Deduplicate cùng nội dung ở nhiều path — `NOT_IMPLEMENTED` trong V1.1.
- [ ] Semantic extraction, self-question, validation và knowledge promotion — `NOT_DONE`.
- [ ] Vòng học tự động 12–15 giờ hoặc liên tục — `NOT_DONE`.
- [ ] Network/Git integration — do cửa sổ khác đảm nhiệm; trạng thái ở cửa J là `UNKNOWN` cho tới khi có handoff bằng chứng.

## 6. Bước kế tiếp duy nhất

Chỉ kiểm tra file V1.1 trên OPPO; chưa compile và chưa chạy VM trong cùng bước:

```bash
FILE="/storage/emulated/0/Download/SIGMA_LOCAL_CORPUS_MIRROR_AND_CHECKPOINT_V1_1.sigma"

printf '===== 📤 SIGMA OUTPUT BEGIN =====\n'
printf 'FILE_EXISTS='
test -f "$FILE" && printf 'YES\n' || printf 'NO\n'

if test -f "$FILE"; then
    stat -c 'BYTES=%s PATH=%n' "$FILE"
    sha256sum "$FILE"
fi
printf '===== 📤 SIGMA OUTPUT END =====\n'
```

Kết quả mong đợi để xác minh danh tính file, không phải đáp án ngữ nghĩa:

```text
BYTES=5530
SHA256=d1f526bc40d274fe34a7c005cd9d1096adbb15689b9290cd9832422fc92db9ee
```

Nếu hash/size không khớp: `HOLD_FILE_IDENTITY_MISMATCH`; không compile.

## 7. Ranh giới hai cửa Termux

Local-learning chỉ ghi vào:

```text
$HOME/SIGMA_AUTONOMOUS_LEARNING_V1
$HOME/SIGMA_LOCAL_CORPUS_*
```

Cửa network phải ghi vào thư mục riêng đã khai báo, ví dụ:

```text
$HOME/SIGMA_NETWORK_*
```

Cả hai chỉ đọc:

```text
~/SIGMA/sigma_genesis1/native/sigmac
~/SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate
```

Không được đồng thời sửa compiler, VM, cùng source, cùng state/checkpoint hoặc cùng file trong vault. Trong checkpoint đầu, cửa network chưa được sửa hai vault mà local-learning đang mirror.

## 8. Prompt mở cửa sổ J mới

```text
Bạn là WINDOW_J_CONTINUATION, vai trò CREATIVE_DIRECTOR.

Đọc toàn bộ handoff đính kèm và tiếp tục đúng CURRENT_GATE:
VERIFY_V1_1_SOURCE_ON_OPPO.

Luật bắt buộc:
- CLAIM <= MACHINE EVIDENCE.
- Không gọi việc đọc/lưu bytes là hiểu hoặc học.
- Không dùng output dự kiến để ép SIGMA trả lời.
- Không sửa production, compiler, VM hoặc lõi SIGMA.
- Không chạy lại V1 đã biết thất bại vì crypto_digest.
- Mỗi lần chỉ đưa một lệnh ngắn; chờ output thật rồi mới tiếp tục.
- Giữ cửa network song song trong write scope riêng.

Bước đầu tiên: kiểm tra existence, size và SHA-256 của
/storage/emulated/0/Download/SIGMA_LOCAL_CORPUS_MIRROR_AND_CHECKPOINT_V1_1.sigma
Expected identity: 5530 bytes,
d1f526bc40d274fe34a7c005cd9d1096adbb15689b9290cd9832422fc92db9ee.

Nếu khớp, bước sau mới là COMPILE_ONLY bằng official native/sigmac.
Nếu không khớp, HOLD_FILE_IDENTITY_MISMATCH.
```

## 9. Điểm dừng chính xác

```text
CURRENT_GATE=VERIFY_V1_1_SOURCE_ON_OPPO
CURRENT_CANDIDATE=SIGMA_LOCAL_CORPUS_MIRROR_AND_CHECKPOINT_V1_1.sigma
CANDIDATE_SHA256=d1f526bc40d274fe34a7c005cd9d1096adbb15689b9290cd9832422fc92db9ee
CANDIDATE_STATUS=GPT_CREATED_NOT_YET_MACHINE_VERIFIED_ON_OPPO
PRODUCTION_ACTIVE=NO
CURRENT_SIGMA_CORE_MODIFIED=NO
SEMANTIC_UNDERSTANDING=NOT_PROVEN
NEXT_GATE=V1_1_SOURCE_IDENTITY_GATE
```
