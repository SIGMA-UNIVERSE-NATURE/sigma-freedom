# SIGMA_PROFESSOR

Thư mục handoff/checkpoint dành riêng cho công việc phát triển **SIGMA native continuous learning**.

## CỜ BOOTSTRAP BẮT BUỘC — ĐỌC TRƯỚC MỌI CÔNG VIỆC

Mọi cửa sổ/phiên/agent mới phải đọc theo thứ tự:

1. `/AGENTS.md`
2. `DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
3. `DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. `CURRENT_HANDOFF.md`
5. checkpoint mới nhất liên quan trong `CHECKPOINTS/`

Không bắt đầu implement/test/promotion trước khi đọc các cờ trên.

## Invariants bắt buộc

- `SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`
- `ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`
- `ACTIVE_COGNITION_NATIVE_SIGMA_ONLY=YES`
- `HARDCODED_LESSON=FORBIDDEN`
- `HOST_LEARNING=NO`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`
- `HOST_OR_BASH_AS_SIGMA_EXECUTION_ENGINE=FORBIDDEN`
- `HOST_OR_BASH_COGNITION=FORBIDDEN`
- `HOST_OR_BASH_STAGE_DECISION=FORBIDDEN`
- `HOST_OR_BASH_WORK_SELECTION=FORBIDDEN`

Bash/host không được implement capability của SIGMA và không được quyết định thay SIGMA. Bash/host chỉ được làm harness cơ học bên ngoài: gọi locked compiler/VM, copy bytes/files chính xác, hash/return-code, tạo fixture test, fault injection, supervision, transport bytes, hoặc dispatch **exact event/stage đã do native SIGMA phát ra** mà không chọn/đổi nghĩa event đó.

`BASH_MAY_LAUNCH_SIGMA=YES`

`BASH_MAY_IMPLEMENT_SIGMA_CAPABILITY=NO`

Nếu một gate chỉ PASS vì host/Bash tính quyết định mà SIGMA đáng lẽ phải tính thì gate đó FAIL admission.

Chỉ gọi capability là **PROVEN** khi có output thực nghiệm từ đúng SIGMA compiler/VM đã khóa identity. Compile/file/shell/Python success không phải capability proof.

## Toolchain identity đang khóa

- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- VM embedded string đã thấy: `SIGMA Genesis-4 C VM`
- `VM_RUNTIME_SELF_IDENTIFICATION=NOT_PROVEN`
- `VM_IS_GENESIS1=NOT_PROVEN`

## Cách dùng handoff

1. Đọc cờ bootstrap ở trên.
2. Đọc `CURRENT_HANDOFF.md`.
3. Đọc checkpoint mới nhất trong `CHECKPOINTS/`.
4. Dùng artifact trong `artifacts/` nếu cần tái tạo đúng source/runner đang được thử nghiệm.
5. Sau mỗi milestone hoàn thành, cập nhật `CURRENT_HANDOFF.md`; với milestone lớn hoặc failure quan trọng, tạo thêm checkpoint bất biến trong `CHECKPOINTS/`.

## Production

- `PRODUCTION_V2_4_KEEP_RUNNING=YES`
- `STOP_ONLY_ON_REAL_VM_FAILURE=YES`
- `UPGRADE_V2_4_IN_PLACE=NO`

Không mutate production learner memory trong admission/shadow test.

## Claim discipline

Không được phép tự động claim:

- `SEMANTIC_UNDERSTANDING=PROVEN`
- `SEMANTIC_CURIOSITY=PROVEN`
- `SEMANTIC_TRUTH_VALIDATION=PROVEN`
- `GENERAL_AUTONOMOUS_REASONING=PROVEN`

Bounded structural proof không được nâng thành semantic/general claim.
