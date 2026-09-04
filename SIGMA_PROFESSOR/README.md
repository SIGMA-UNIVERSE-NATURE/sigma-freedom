# SIGMA_PROFESSOR

Thư mục handoff/checkpoint dành riêng cho công việc phát triển **SIGMA native continuous learning**.

## Mục đích

Nếu một cửa sổ/phiên làm việc bị đứng hoặc mất context, cửa sổ khác có thể bắt đầu từ đây thay vì đào lại toàn bộ repo.

## Invariants bắt buộc

- `HARDCODED_LESSON=FORBIDDEN`
- `HOST_LEARNING=NO`
- Host chỉ được làm cơ học/runtime: file I/O, hash, transport bytes, protocol decode thuần cơ học, scheduling, invoke compiler/VM.
- Host không được tạo lesson, candidate, semantic score, knowledge decision hoặc learning goal thay SIGMA.
- Chỉ gọi capability là **PROVEN** khi có output thực nghiệm từ đúng SIGMA compiler/VM đã khóa identity.
- Không suy đoán VM là Genesis1 chỉ từ path/name.

## Toolchain identity đang khóa

- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- VM embedded string đã thấy: `SIGMA Genesis-4 C VM`
- `VM_RUNTIME_SELF_IDENTIFICATION=NOT_PROVEN`
- `VM_IS_GENESIS1=NOT_PROVEN`

## Cách dùng handoff

1. Đọc `CURRENT_HANDOFF.md` trước.
2. Đọc checkpoint mới nhất trong `CHECKPOINTS/`.
3. Dùng artifact trong `artifacts/` nếu cần tái tạo đúng source/runner đang được thử nghiệm.
4. Sau mỗi milestone hoàn thành, cập nhật `CURRENT_HANDOFF.md`; với milestone lớn hoặc failure quan trọng, tạo thêm checkpoint bất biến trong `CHECKPOINTS/`.

## Trạng thái claim hiện tại

Đã có bằng chứng thực nghiệm cho:

- native structural learning
- persistent recurrence across experiences
- native self-selection
- cross-context support
- autonomous structural fetch-request generation (V2.2)

Chưa được phép claim:

- `SEMANTIC_UNDERSTANDING=PROVEN`
- `SEMANTIC_CURIOSITY=PROVEN`
- `GENERAL_AUTONOMOUS_REASONING=PROVEN`
