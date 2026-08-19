# SIGMA VM — OPPO ACTUAL-ABI EXECUTION PARITY HANDOFF

**Ngày:** 2026-08-18  
**Thời điểm ghi nhận:** khoảng 07:05 +07:00  
**Thiết bị:** OPPO / Android / Termux / aarch64  
**Working tree:** `~/SIGMA/sigma_genesis1`  
**Trạng thái:** `PASS_WITH_DEFINED_SCOPE`

---

## 1. MỤC TIÊU THỬ NGHIỆM

Kiểm tra xem một **VM engine viết bằng chính ngôn ngữ SIGMA** có thể:

1. được native SIGMA compiler biên dịch;
2. chạy trên runtime SIGMA hiện tại;
3. thực thi instruction semantics ánh xạ trực tiếp từ `sigma_vm.c`;
4. cho cùng output với C VM reference trên cùng bài toán;
5. không sử dụng bộ opcode tự nghĩ ra.

Không giả lập bằng Python.

Không dùng guest ISA tự chế.

Opcode và semantics được lấy trực tiếp từ source thực tế `sigma_vm.c`.

---

## 2. ACTUAL ABI ĐÃ XÁC NHẬN TỪ `sigma_vm.c`

```text
OP_PUSH_CONST      = 0x01
OP_POP             = 0x02
OP_LOAD            = 0x10
OP_STORE           = 0x11
OP_UNARY           = 0x20
OP_BINARY          = 0x21
OP_CALL            = 0x30
OP_RETURN          = 0x31
OP_JUMP            = 0x40
OP_JUMP_IF_FALSE   = 0x41
OP_HALT            = 0xFF
```

Unary subcodes:

```text
U_NOT = 0x01
U_NEG = 0x02
U_POS = 0x03
```

Binary subcodes:

```text
B_ADD       = 0x01
B_SUB       = 0x02
B_MUL       = 0x03
B_DIV       = 0x04
B_FLOORDIV  = 0x05
B_MOD       = 0x06
B_POW       = 0x07

B_EQ        = 0x10
B_NE        = 0x11
B_LT        = 0x12
B_GT        = 0x13
B_LE        = 0x14
B_GE        = 0x15

B_AND       = 0x20
B_OR        = 0x21
```

Đặc biệt:

```text
OP_BINARY = 0x21
B_ADD     = 0x01
```

Không dùng `IADD = 0x10` như prototype ban đầu.

---

## 3. SEMANTICS LOAD / STORE ĐÃ ĐƯỢC ÁNH XẠ TỪ C VM

C VM thực tế:

```c
OP_LOAD:
    locals trước
    globals sau

OP_STORE:
    if(is_main)
        store globals
    else
        store locals
```

SIGMA VM v0.2 đã triển khai cùng mô hình:

```text
LOAD:
locals → globals → undefined error

STORE:
is_main == TRUE  → globals
is_main == FALSE → locals
```

---

## 4. FILE SIGMA VM ĐÃ TẠO

```text
~/SIGMA/sigma_genesis1/sigma_vm_core_v0_2_actual_abi.sigma
```

Số dòng:

```text
554
```

File này chứa:

```text
ABI_NEW
INS
EMIT_CODE

ENV_NEW
ENV_HAS
ENV_GET
ENV_SET

STACK_NEW
STACK_PUSH
STACK_POP
STACK_DISCARD

PROGRAM_NEW
VM_NEW

VM_LOAD
VM_STORE
VM_BINARY
VM_CALL

VM_STEP
VM_RUN

BUILD_TEST_PROGRAM
```

`VM_BINARY` hiện đã kiểm chứng `B_ADD`.

`VM_CALL` hiện kiểm chứng đường built-in `print`.

---

## 5. REFERENCE PROGRAM

Reference source:

```text
vm_actual_abi_compare.sigma
```

Logic:

```sigmar
⟡(Σ.VM_COMPARE) {
    ⚡ x: 10;
    ⚡ y: 20;
    ⚡ z: x + y;
    ⚡ print(z);
}
```

Instruction sequence tương ứng với compiler semantics:

```text
PUSH_CONST 0
STORE      x

PUSH_CONST 1
STORE      y

LOAD       x
LOAD       y

BINARY     B_ADD

STORE      z
LOAD       z

CALL       print argc=1
POP

HALT
```

---

## 6. CLI THỰC TẾ ĐÃ XÁC NHẬN TỪ SOURCE

Native compiler:

```text
./native/sigmac input.sigma output.sigmab
```

Native C VM:

```text
./native/sigma-vm program.sigmab
```

---

## 7. KẾT QUẢ THỰC NGHIỆM — C VM REFERENCE

Compile:

```text
COMPILED vm_actual_abi_compare.sigma
-> vm_actual_abi_compare.sigmab
```

Return code:

```text
C_REFERENCE_COMPILE_RC=0
```

Run:

```text
./native/sigma-vm vm_actual_abi_compare.sigmab
```

Result:

```text
C_REFERENCE_RUN_RC=0

STDOUT:
30

STDERR:
<empty>
```

---

## 8. KẾT QUẢ THỰC NGHIỆM — VM VIẾT BẰNG SIGMA

Compile:

```text
COMPILED sigma_vm_core_v0_2_actual_abi.sigma
-> sigma_vm_core_v0_2_actual_abi.sigmab
```

Return code:

```text
SIGMA_VM_COMPILE_RC=0
```

Run:

```text
./native/sigma-vm sigma_vm_core_v0_2_actual_abi.sigmab
```

Result:

```text
SIGMA_VM_RUN_RC=0

STDOUT:
30

STDERR:
<empty>
```

---

## 9. EXACT OUTPUT PARITY

```text
OUTPUT_PARITY=PASS
```

C VM output:

```text
30
```

SIGMA-written VM output:

```text
30
```

Hai stdout có cùng SHA-256:

```text
f4ccd05b3271c386ee55d9876c7450012a3b361e5065c09dc22075e38b3cc35c
```

Do đó:

```text
C_VM_OUTPUT == SIGMA_VM_OUTPUT
```

đã được chứng minh bằng exact byte comparison cho test này.

---

## 10. EVIDENCE HASHES

Reference source:

```text
baf1a6ca40942b623d9c5226dcdf52a53f3355bd50fb428c58acc5e67fe47457
vm_actual_abi_compare.sigma
```

Reference bytecode:

```text
efcd04d2d31731f75faf5703e17d52a496bbdff5059e9108d71c86b4bdb804b9
vm_actual_abi_compare.sigmab
```

SIGMA VM source:

```text
85fa2baf2d267af5bdddc53681f9acdab9ceb817c5eaab96b580a8043eb9a21b
sigma_vm_core_v0_2_actual_abi.sigma
```

SIGMA VM bytecode:

```text
d360c725dba454acd2edfd020ca272eee44bddd672dedb38849f38b332789d2a
sigma_vm_core_v0_2_actual_abi.sigmab
```

C VM stdout:

```text
f4ccd05b3271c386ee55d9876c7450012a3b361e5065c09dc22075e38b3cc35c
c_vm_reference.out
```

SIGMA VM stdout:

```text
f4ccd05b3271c386ee55d9876c7450012a3b361e5065c09dc22075e38b3cc35c
sigma_vm_actual.out
```

---

## 11. PHÁN QUYẾT

```text
ACTUAL_C_VM_REFERENCE_EXECUTION = PASS

SIGMA_VM_SOURCE_COMPILE         = PASS
SIGMA_VM_BYTECODE_EXECUTION     = PASS

ACTUAL_ABI_OPCODE_MAPPING       = PASS

PUSH_CONST_PATH                 = PASS
LOAD_PATH                       = PASS
STORE_PATH                      = PASS

OP_BINARY_PATH                  = PASS
B_ADD_0x01_PATH                 = PASS

CALL_PRINT_PATH                 = PASS
POP_PATH                        = PASS
HALT_PATH                       = PASS

C_VM_VS_SIGMA_VM_OUTPUT_PARITY  = PASS

REAL_EXECUTION_ON_OPPO_ARM64    = PASS
```

---

## 12. PHẠM VI CHỨNG MINH

ĐƯỢC PHÉP tuyên bố:

```text
VM_EXECUTION_CORE_FOR_TESTED_REAL_ABI = VERIFIED
```

và:

```text
A VM ENGINE WRITTEN IN SIGMA
WAS COMPILED AS SIGMA BYTECODE
AND EXECUTED SUCCESSFULLY
WITH OUTPUT PARITY AGAINST THE C VM
FOR THE TESTED ACTUAL-ABI PATH.
```

KHÔNG được suy rộng thành:

```text
COMPLETE_SIGMA_VM = PASS
```

vì hiện chưa parity-test đầy đủ:

```text
OP_UNARY
all BINARY subcodes
OP_RETURN
OP_JUMP
OP_JUMP_IF_FALSE
general user-defined OP_CALL
function-local execution semantics
all error paths
```

---

## 13. HARDCODE BOUNDARY

`BUILD_TEST_PROGRAM()` hiện vẫn nhúng test fixture:

```text
x = 10
y = 20
z = x + y
print(z)
```

Điều này được chấp nhận cho parity experiment.

Nhưng:

```text
GENERIC_EXTERNAL_BYTECODE_LOADER = NOT_YET
```

SIGMA VM hiện chưa được chứng minh là có thể tự đọc một `.sigmab` bất kỳ từ bên ngoài.

Không được nhầm:

```text
TEST FIXTURE
```

với:

```text
GENERIC PROGRAM LOADER
```

---

## 14. NEXT STEP — KHÔNG CẦN CHẠY LẠI MỐC NÀY

Cửa sổ kế tiếp có thể:

```text
INHERIT:
SIGMA_VM_ACTUAL_ABI_PARITY_001 = PASS
```

Không cần chạy lại phép `x=10, y=20, x+y → 30` trừ khi source/hash thay đổi.

NEXT:

```text
SIGMA VM v0.3

EXTERNAL .sigmab
    ↓
SIGMA BYTECODE LOADER
    ↓
SIGMA DECODER
    ↓
SIGMA EXECUTOR
    ↓
SAME BYTECODE FILE
   ↙            ↘
C VM          SIGMA VM
   ↓            ↓
OUTPUT/STATE PARITY
```

Ưu tiên:

```text
1. Xác định/bổ sung generic binary-read capability.
2. Không hardcode chương trình vào VM engine.
3. Đọc bytecode `SIGMBC01` thật.
4. Decode constants/symbols/functions/main code bằng Sigma.
5. Chạy cùng một `.sigmab` trên C VM và Sigma VM.
6. So sánh stdout + return code + state/evidence.
7. Sau đó mở rộng parity cho toàn bộ opcode.
```

---

# HANDOFF CONTROL

```text
DO_NOT_REBUILD_V0_2_WITH_INVENTED_OPCODE.
DO_NOT_REPLACE_ACTUAL_ABI_WITH_OLD_SPEC.
DO_NOT_CALL_FULL_VM_PASS_YET.
DO_NOT_HIDE_BUILD_TEST_PROGRAM_HARDCODE.

INHERIT_ACTUAL_ABI_PARITY_PASS.
CONTINUE_TO_EXTERNAL_BYTECODE_LOADER.
```

**END OF HANDOFF**
