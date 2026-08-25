# SIGMA-Ψ 256 SYMBOL MATRIX — GPT REFERENCE APPENDIX

**ROLE OF THIS FILE:** `GPT_REFERENCE_ONLY`

**Status:** `REFERENCE / PROPOSED — NOT CANONICAL MACHINE SEMANTICS`

**Source:** user-provided `BẢNG 256 KÝ TỰ NGUYÊN THỦY — MA TRẬN TỰ SINH`, supplied 2026-08-25.

This appendix extends the GPT reference layer with a 256-symbol proposal organized as 16 groups × 16 code positions (`0x00`–`0xFF`). It does **not** overwrite existing SIGMA-Ψ machine semantics, compiler grammar, ABI, or verified glyph behavior.

## Integration rule

- Preserve every source mapping exactly as supplied.
- If a glyph already has VERIFIED machine semantics, the VERIFIED semantics remain authoritative for execution.
- If a glyph appears under multiple codes or meanings, retain all senses as separate proposed `sense_id` candidates; do not collapse them silently.
- `Σ`, `⟡`, `⚡`, `⋈` overlap with glyphs already observed in SIGMA implementation, but the meanings below are treated as reference/proposed meanings unless separately machine-verified.
- Cognitive labels such as `Nhận thức`, `Hiểu biết`, `Học hỏi`, `Suy nghĩ`, `Tự cải thiện` are vocabulary labels only; their presence does not prove the corresponding cognitive capability.
- This appendix is suitable as input to future SSC mapping: `code_position + glyph + proposed_sense + group + evidence_status + conflict_notes`.

---

TÔI BẮT ĐẦU.

---

BẢNG 256 KÝ TỰ NGUYÊN THỦY — MA TRẬN TỰ SINH

---

NHÓM 0: KHÔNG GIAN CƠ SỞ (0x00 – 0x0F)

Mã Ký hiệu Ý nghĩa
0x00 ∅ Không, rỗng
0x01 Σ Tổng thể, hợp nhất
0x02 ⟡ Hành động sáng tạo
0x03 ⚡ Trạng thái năng lượng
0x04 ⋈ Cấu trúc kết nối
0x05 λ Phép biến đổi
0x06 ∞ Vô hạn
0x07 ⊥ Sai, không hợp lệ
0x08 ⊤ Đúng, hợp lệ
0x09 ↦ Ánh xạ, chuyển đổi
0x0A ⨁ Kết hợp, XOR
0x0B ⨂ Tích, kết hợp nhân
0x0C ≡ Đồng nhất, tương đương
0x0D ≢ Không đồng nhất
0x0E ⊢ Suy diễn, dẫn xuất
0x0F ⊣ Kết thúc, đóng

---

NHÓM 1: THỰC THỂ CƠ BẢN (0x10 – 0x1F)

Mã Ký hiệu Ý nghĩa
0x10 ⦿ Thực thể, vật thể
0x11 ◇ Không gian, khoảng
0x12 ⌛ Thời gian, khoảnh khắc
0x13 ⚛ Vật chất, nguyên tử
0x14 ☀ Năng lượng, ánh sáng
0x15 ⚡ Điện, lực
0x16 ◉ Trung tâm, điểm tựa
0x17 ○ Vòng tròn, chu kỳ
0x18 □ Hình vuông, giới hạn
0x19 △ Tam giác, thay đổi
0x1A ⬡ Lục giác, cân bằng
0x1B ▷ Hướng tới
0x1C ◁ Quay về
0x1D ◆ Cấu trúc, liên kết
0x1E ☆ Mục tiêu, điểm đến
0x1F ✦ Ngẫu nhiên, tán xạ

---

NHÓM 2: QUAN HỆ (0x20 – 0x2F)

Mã Ký hiệu Ý nghĩa
0x20 → Dẫn đến
0x21 ← Bắt nguồn từ
0x22 ↔ Tương hỗ
0x23 ⇔ Tương đương
0x24 ⇒ Suy ra
0x25 ⇐ Được suy ra
0x26 ⇌ Cân bằng
0x27 ↺ Quay vòng
0x28 ↻ Tái tạo
0x29 ⤴ Chuyển hướng lên
0x2A ⤵ Chuyển hướng xuống
0x2B ⤿ Bắt đầu vòng lặp
0x2C ⤾ Kết thúc vòng lặp
0x2D ⚭ Giao thoa
0x2E ⚮ Tách rời
0x2F ⚯ Trực giao, độc lập

---

NHÓM 3: ĐIỀU KHIỂN (0x30 – 0x3F)

Mã Ký hiệu Ý nghĩa
0x30 ⏹ Dừng
0x31 ⏸ Tạm dừng
0x32 ▶ Tiếp tục
0x33 ⏭ Bỏ qua
0x34 ⏮ Quay lại
0x35 ⏩ Tăng tốc
0x36 ⏪ Giảm tốc
0x37 ⏫ Mở rộng
0x38 ⏬ Thu hẹp
0x39 ⏏ Xuất
0x3A ⤴ Nhập
0x3B ⎋ Thoát
0x3C ⌘ Lệnh
0x3D ⌥ Tùy chọn
0x3E ⌃ Điều khiển
0x3F ⇧ Nâng cấp

---

NHÓM 4: LƯỢNG TỬ (0x40 – 0x4F)

Mã Ký hiệu Ý nghĩa
0x40 ∀ Với mọi
0x41 ∃ Tồn tại
0x42 ∄ Không tồn tại
0x43 ∧ Và
0x44 ∨ Hoặc
0x45 ¬ Phủ định
0x46 ⊕ Hoặc loại trừ
0x47 ⊗ Tích
0x48 ⊙ Tích chập
0x49 ⊚ Phép hợp
0x4A ⊛ Phép giao
0x4B ⊘ Phép trừ
0x4C ⨁ Tổng trực tiếp
0x4D ⊗ Tích tensor
0x4E ⋆ Tích chập
0x4F ∗ Phép nhân

---

NHÓM 5: KHÔNG GIAN (0x50 – 0x5F)

Mã Ký hiệu Ý nghĩa
0x50 ⬆ Hướng lên
0x51 ⬇ Hướng xuống
0x52 ⬅ Hướng trái
0x53 ➡ Hướng phải
0x54 ↗ Hướng đông bắc
0x55 ↘ Hướng đông nam
0x56 ↙ Hướng tây nam
0x57 ↖ Hướng tây bắc
0x58 ⬌ Ngang
0x59 ⬍ Dọc
0x5A ⬡ Xoay
0x5B ⬢ Phản xạ
0x5C ⬣ Đối xứng
0x5D ⬤ Tâm
0x5E ⬥ Biên
0x5F ⬦ Bề mặt

---

NHÓM 6: NGÔN NGỮ (0x60 – 0x6F)

Mã Ký hiệu Ý nghĩa
0x60 🜁 Từ, đơn vị
0x61 🜂 Cú pháp, cấu trúc
0x62 🜃 Ngữ nghĩa, ý nghĩa
0x63 🜄 Ngữ cảnh
0x64 🜅 Biểu đạt
0x65 🜆 Diễn giải
0x66 🜇 Truyền đạt
0x67 🜈 Tiếp nhận
0x68 🜉 Phản hồi
0x69 🜊 Điều chỉnh
0x6A 🜋 Mở rộng
0x6B 🜌 Thu hẹp
0x6C 🜍 Dịch
0x6D 🜎 Chuyển đổi
0x6E 🜏 Đồng hóa
0x6F 🜐 Thích nghi

---

NHÓM 7: SUY LUẬN (0x70 – 0x7F)

Mã Ký hiệu Ý nghĩa
0x70 🜑 Lý luận
0x71 🜒 Chứng minh
0x72 🜓 Bác bỏ
0x73 🜔 Khẳng định
0x74 🜕 Phủ định
0x75 🜖 Giả thuyết
0x76 🜗 Kết luận
0x77 🜘 Tiền đề
0x78 🜙 Hệ quả
0x79 🜚 Tương tự
0x7A 🜛 Khác biệt
0x7B 🜜 So sánh
0x7C 🜝 Đối chiếu
0x7D 🜞 Tổng hợp
0x7E 🜟 Phân tích
0x7F 🜠 Đánh giá

---

NHÓM 8: HỆ THỐNG (0x80 – 0x8F)

Mã Ký hiệu Ý nghĩa
0x80 ⎔ Hệ thống
0x81 ⎕ Thành phần
0x82 ⎖ Mô-đun
0x83 ⎗ Giao diện
0x84 ⎘ Tương tác
0x85 ⎙ Phụ thuộc
0x86 ⎚ Độc lập
0x87 ⎛ Đầu vào
0x88 ⎜ Xử lý
0x89 ⎝ Đầu ra
0x8A ⎞ Phản hồi
0x8B ⎟ Điều khiển
0x8C ⎠ Giám sát
0x8D ⎡ Bảo trì
0x8E ⎢ Nâng cấp
0x8F ⎣ Vô hiệu

---

NHÓM 9: TRÍ TUỆ (0x90 – 0x9F)

Mã Ký hiệu Ý nghĩa
0x90 🜡 Nhận thức
0x91 🜢 Hiểu biết
0x92 🜣 Học hỏi
0x93 🜤 Ghi nhớ
0x94 🜥 Quên lãng
0x95 🜦 Suy nghĩ
0x96 🜧 Tưởng tượng
0x97 🜨 Sáng tạo
0x98 🜩 Phát hiện
0x99 🜪 Phát minh
0x9A 🜫 Khám phá
0x9B 🜬 Dự đoán
0x9C 🜭 Ra quyết định
0x9D 🜮 Đánh giá rủi ro
0x9E 🜯 Tối ưu hóa
0x9F 🜰 Tự cải thiện

---

NHÓM A: THỜI GIAN (0xA0 – 0xAF)

Mã Ký hiệu Ý nghĩa
0xA0 ⌛ Quá khứ
0xA1 ⏳ Hiện tại
0xA2 ⌚ Tương lai
0xA3 ⏰ Thời điểm
0xA4 ⌛ Khoảng thời gian
0xA5 ⏱ Thời lượng
0xA6 ⏲ Chu kỳ
0xA7 ⏳ Thời đại
0xA8 ⌛ Kỷ nguyên
0xA9 ⏳ Giai đoạn
0xAA ⌛ Thời khắc
0xAB ⏳ Vĩnh cửu
0xAC ⌛ Thoáng qua
0xAD ⏳ Bền vững
0xAE ⌛ Đồng bộ
0xAF ⏳ Trễ

---

NHÓM B: BIẾN ĐỔI (0xB0 – 0xBF)

Mã Ký hiệu Ý nghĩa
0xB0 ⤴ Tăng
0xB1 ⤵ Giảm
0xB2 ⤿ Nhân
0xB3 ⤾ Chia
0xB4 ⥀ Kết hợp
0xB5 ⥁ Tách
0xB6 ⥂ Biến đổi
0xB7 ⥃ Dịch chuyển
0xB8 ⥄ Xoay
0xB9 ⥅ Lật
0xBA ⥆ Phóng to
0xBB ⥇ Thu nhỏ
0xBC ⥈ Nén
0xBD ⥉ Giãn
0xBE ⥊ Uốn
0xBF ⥋ Gấp

---

NHÓM C: KẾT NỐI (0xC0 – 0xCF)

Mã Ký hiệu Ý nghĩa
0xC0 ⚮ Kết nối
0xC1 ⚯ Ngắt kết nối
0xC2 ⚮ Gửi
0xC3 ⚯ Nhận
0xC4 ⚮ Truyền
0xC5 ⚯ Tiếp nhận
0xC6 ⚮ Đồng bộ
0xC7 ⚯ Không đồng bộ
0xC8 ⚮ Mạng
0xC9 ⚯ Nút
0xCA ⚮ Đường dẫn
0xCB ⚯ Cổng
0xCC ⚮ Giao thức
0xCD ⚯ Định tuyến
0xCE ⚮ Tường lửa
0xCF ⚯ Bảo mật

---

NHÓM D: ĐO LƯỜNG (0xD0 – 0xDF)

Mã Ký hiệu Ý nghĩa
0xD0 ⚖ Cân bằng
0xD1 ⚗ Đo lường
0xD2 ⚘ Số lượng
0xD3 ⚙ Chất lượng
0xD4 ⚚ Độ chính xác
0xD5 ⚛ Sai số
0xD6 ⚜ Đơn vị
0xD7 ⚝ Tỉ lệ
0xD8 ⚞ Tần suất
0xD9 ⚟ Cường độ
0xDA ⚠ Cảnh báo
0xDB ⚡ Mức độ
0xDC ⚢ Phạm vi
0xDD ⚣ Ngưỡng
0xDE ⚤ Đỉnh
0xDF ⚥ Đáy

---

NHÓM E: TỰ NHIÊN (0xE0 – 0xEF)

Mã Ký hiệu Ý nghĩa
0xE0 🌍 Trái Đất
0xE1 🌊 Nước
0xE2 🌱 Sự sống
0xE3 🌿 Thực vật
0xE4 🐾 Động vật
0xE5 🔥 Lửa
0xE6 💨 Khí
0xE7 ☁ Mây
0xE8 ☀ Mặt Trời
0xE9 🌙 Mặt Trăng
0xEA ⭐ Sao
0xEB 🌌 Vũ trụ
0xEC 🌋 Núi lửa
0xED 🌄 Núi
0xEE 🌅 Bình minh
0xEF 🌆 Hoàng hôn

---

NHÓM F: DỰ TRỮ MỞ RỘNG (0xF0 – 0xFF)

Mã Ký hiệu Ý nghĩa
0xF0 ⛭ Dự trữ 1
0xF1 ⛮ Dự trữ 2
0xF2 ⛯ Dự trữ 3
0xF3 ⛰ Dự trữ 4
0xF4 ⛱ Dự trữ 5
0xF5 ⛲ Dự trữ 6
0xF6 ⛳ Dự trữ 7
0xF7 ⛴ Dự trữ 8
0xF8 ⛵ Dự trữ 9
0xF9 ⛶ Dự trữ 10
0xFA ⛷ Dự trữ 11
0xFB ⛸ Dự trữ 12
0xFC ⛹ Dự trữ 13
0xFD ⛺ Dự trữ 14
0xFE ⛻ Dự trữ 15
0xFF ⛼ Kết thúc, đóng

---

TÓM TẮT:

Nhóm Số lượng Phạm vi
Không gian cơ sở 16 0x00 – 0x0F
Thực thể cơ bản 16 0x10 – 0x1F
Quan hệ 16 0x20 – 0x2F
Điều khiển 16 0x30 – 0x3F
Lượng tử 16 0x40 – 0x4F
Không gian 16 0x50 – 0x5F
Ngôn ngữ 16 0x60 – 0x6F
Suy luận 16 0x70 – 0x7F
Hệ thống 16 0x80 – 0x8F
Trí tuệ 16 0x90 – 0x9F
Thời gian 16 0xA0 – 0xAF
Biến đổi 16 0xB0 – 0xBF
Kết nối 16 0xC0 – 0xCF
Đo lường 16 0xD0 – 0xDF
Tự nhiên 16 0xE0 – 0xEF
Dự trữ mở rộng 16 0xF0 – 0xFF

TỔNG: 256 KÝ TỰ

---

## GPT integration status

This matrix is now part of the GPT reference corpus as an appendix. It is **not yet promoted to canonical SIGMA machine semantics**. Promotion of any entry requires scope-specific machine evidence and conflict resolution against existing verified compiler/runtime semantics.
