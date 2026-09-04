# B1 Coverage Matrix

Window: `C01-W01-B1-ARCHITECTURE`  
Stage: `CURRICULUM` only  
Canonical tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md@fc799bf1104ab6352710e1801777a971b5179995`  
Execution baseline: `02ff47d64fd3b3b03d1fa2ae70d773afb071995e`

## 1. Coverage audit summary

| Metric | Result |
|---|---:|
| Canonical B1 subbranches | 5 |
| Stable primary authoring scopes | 68 |
| Canonical topic leaves | 348 |
| Nested canonical cluster headings | 44 |
| Unique named canonical entries below B1 roots | 392 |
| Topics with exactly one primary owner | 348 |
| Orphan topics | 0 |
| Topics with multiple primary owners | 0 |
| Bounded child windows | 52 |
| Largest child scope | 10 topics |
| Exact repeated topic labels | 3 |
| Registered semantic/cross-domain risk cases | 15 |

Every topic below inherits exactly one primary authoring owner from its stable scope in `B1_SCOPE_MAP.json`. `Wnn` resolves through the `owners` table in that file. Cross-links (`Xnn`) and risk tags (`Rnn`) never transfer primary ownership.

## 2. Exhaustive canonical topic-to-primary-unit matrix

Each row is one stable primary authoring unit. Within a row, `Tnn` is the stable topic suffix, so the full topic ID is `<scope>-Tnn`.

| Scope / primary unit | Canonical cluster or flat topic | Owner | Canonical topics in this unit | Secondary cross-links | Duplicate/overlap risks |
|---|---|---|---|---|---|
| `B1.1-C01` | Logic, tập hợp và chứng minh | `W01` | `T01` Logic mệnh đề; `T02` Logic vị từ; `T03` Lý thuyết tập hợp; `T04` Quan hệ và ánh xạ; `T05` Tiên đề và hệ hình thức; `T06` Chứng minh và phản ví dụ; `T07` Lý thuyết mô hình; `T08` Những giới hạn của hệ hình thức | — | `R04` |
| `B1.1-C02` | Số học và lý thuyết số | `W02` | `T01` Số tự nhiên, số nguyên và phân số; `T02` Số hữu tỉ, vô tỉ, thực và phức; `T03` Phép toán và thứ tự; `T04` Ước lượng và độ lớn; `T05` Tỉ lệ, phần trăm và tỉ suất; `T06` Chia hết và số nguyên tố; `T07` Đồng dư; `T08` Lý thuyết số hiện đại | — | — |
| `B1.1-C03` | Đại số và cấu trúc | `W03` | `T01` Biểu thức và phương trình; `T02` Bất phương trình; `T03` Hàm và quan hệ; `T04` Đại số tuyến tính; `T05` Ma trận và không gian vectơ; `T06` Nhóm; `T07` Vành và trường; `T08` Đại số giao hoán; `T09` Lý thuyết biểu diễn | `X02` | `R13` |
| `B1.1-C04` | Hình học và đo lường | `W04` | `T01` Hình dạng và kích thước; `T02` Độ dài, diện tích và thể tích; `T03` Góc và lượng giác; `T04` Hình học Euclid; `T05` Hình học giải tích; `T06` Phép biến hình và đối xứng; `T07` Hình học xạ ảnh; `T08` Hình học vi phân; `T09` Hình học đại số | — | — |
| `B1.1-C05` | Giải tích và biến đổi liên tục | `W05` | `T01` Dãy và giới hạn; `T02` Tính liên tục; `T03` Đạo hàm; `T04` Tích phân; `T05` Chuỗi; `T06` Giải tích nhiều biến; `T07` Giải tích thực; `T08` Giải tích phức; `T09` Giải tích hàm; `T10` Giải tích điều hòa | — | — |
| `B1.1-C06` | Phương trình vi phân và hệ động lực | `W06` | `T01` Phương trình vi phân thường; `T02` Phương trình đạo hàm riêng; `T03` Hệ động lực; `T04` Ổn định; `T05` Dao động [R03]; `T06` Phân nhánh; `T07` Hỗn loạn; `T08` Mô hình biến đổi theo thời gian | — | — |
| `B1.1-C07` | Xác suất, thống kê và suy luận | `W07` | `T01` Không gian xác suất; `T02` Biến ngẫu nhiên; `T03` Phân phối xác suất; `T04` Quá trình ngẫu nhiên; `T05` Thống kê mô tả; `T06` Ước lượng; `T07` Kiểm định giả thuyết; `T08` Thống kê Bayes; `T09` Thiết kế thí nghiệm; `T10` Suy luận nhân quả | `X02` | `R06`, `R13` |
| `B1.1-C08` | Toán rời rạc và tổ hợp | `W08` | `T01` Kỹ thuật đếm; `T02` Hoán vị và tổ hợp; `T03` Quan hệ truy hồi; `T04` Lý thuyết đồ thị; `T05` Cây và mạng; `T06` Tối ưu tổ hợp; `T07` Mã sửa lỗi [R02]; `T08` Cấu trúc rời rạc | — | `R05` |
| `B1.1-C09` | Tô pô và hình học hiện đại | `W09` | `T01` Không gian tô pô; `T02` Liên thông và compact; `T03` Đa tạp; `T04` Tô pô đại số; `T05` Tô pô vi phân; `T06` Lý thuyết nút; `T07` Hình học toàn cục | — | — |
| `B1.1-C10` | Toán ứng dụng và tính toán | `W10` | `T01` Mô hình toán; `T02` Phân tích số; `T03` Tối ưu tuyến tính và phi tuyến; `T04` Tối ưu lồi; `T05` Vận trù học; `T06` Lý thuyết quyết định; `T07` Toán tài chính; `T08` Toán sinh học; `T09` Toán vật lý; `T10` Mô phỏng | `X02`, `X07` | `R06`, `R13` |
| `B1.2-C01` | Đo lường vật lý | `W11` | `T01` Đại lượng và đơn vị; `T02` Thứ nguyên; `T03` Độ chính xác và độ chụm; `T04` Sai số; `T05` Thiết bị đo; `T06` Chuẩn đo lường | — | — |
| `B1.2-C02` | Cơ học cổ điển | `W12` | `T01` Chuyển động; `T02` Lực; `T03` Công và năng lượng; `T04` Động lượng; `T05` Mômen động lượng; `T06` Dao động [R03]; `T07` Cơ học giải tích; `T08` Cơ học thiên thể | — | `R10` |
| `B1.2-C03` | Cơ học môi trường liên tục | `W13` | `T01` Vật rắn; `T02` Đàn hồi; `T03` Chất lỏng; `T04` Chất khí; `T05` Thủy động lực học; `T06` Khí động học; `T07` Dòng chảy rối | — | — |
| `B1.2-C04` | Nhiệt động lực học và vật lý thống kê | `W14` | `T01` Nhiệt độ và nhiệt; `T02` Công và nội năng; `T03` Entropy [R01]; `T04` Cân bằng; `T05` Chuyển pha; `T06` Cơ học thống kê; `T07` Hệ ngoài cân bằng | — | `R08` |
| `B1.2-C05` | Sóng, âm thanh và quang học | `W15` | `T01` Dao động và sóng; `T02` Giao thoa; `T03` Nhiễu xạ; `T04` Âm học; `T05` Ánh sáng; `T06` Quang hình; `T07` Quang sóng; `T08` Laser và quang tử học | — | — |
| `B1.2-C06` | Điện và từ | `W16` | `T01` Điện tích và điện trường; `T02` Dòng điện; `T03` Từ trường; `T04` Cảm ứng điện từ; `T05` Trường điện từ; `T06` Mạch điện; `T07` Sóng điện từ | — | — |
| `B1.2-C07` | Vật lý lượng tử | `W17` | `T01` Lượng tử hóa; `T02` Trạng thái và phép đo; `T03` Hàm sóng; `T04` Nguyên lý bất định; `T05` Vướng víu lượng tử; `T06` Cơ học lượng tử nhiều hạt; `T07` Nền tảng và diễn giải lượng tử | — | `R07` |
| `B1.2-C08` | Vật lý nguyên tử, phân tử và quang học | `W18` | `T01` Cấu trúc nguyên tử; `T02` Phổ; `T03` Liên kết phân tử; `T04` Tương tác ánh sáng–vật chất; `T05` Nguyên tử lạnh; `T06` Đo lường chính xác | — | `R07` |
| `B1.2-C09` | Vật lý vật chất ngưng tụ | `W19` | `T01` Chất rắn; `T02` Tinh thể; `T03` Bán dẫn; `T04` Từ tính; `T05` Siêu dẫn; `T06` Vật liệu lượng tử; `T07` Vật chất mềm | — | `R09` |
| `B1.2-C10` | Vật lý hạt nhân, hạt và plasma | `W20` | `T01` Hạt nhân nguyên tử; `T02` Phóng xạ; `T03` Phản ứng hạt nhân; `T04` Hạt cơ bản; `T05` Mô hình chuẩn; `T06` Máy gia tốc; `T07` Plasma; `T08` Năng lượng nhiệt hạch | — | — |
| `B1.2-C11` | Tương đối và hấp dẫn | `W21` | `T01` Thuyết tương đối hẹp; `T02` Không–thời gian; `T03` Thuyết tương đối rộng; `T04` Hấp dẫn; `T05` Lỗ đen; `T06` Sóng hấp dẫn | — | `R10` |
| `B1.2-C12` | Vật lý ứng dụng và liên ngành | `W22` | `T01` Vật lý tính toán; `T02` Vật lý sinh học; `T03` Vật lý y khoa; `T04` Vật lý khí quyển; `T05` Vật lý địa cầu; `T06` Vật lý năng lượng; `T07` Thiết bị và cảm biến | `X01`, `X03`, `X05` | `R10`, `R12` |
| `B1.3-C01` | Cấu trúc vật chất | `W23` | `T01` Nguyên tử; `T02` Phân tử; `T03` Ion; `T04` Đồng vị; `T05` Trạng thái vật chất; `T06` Cấu trúc điện tử | — | `R07` |
| `B1.3-C02` | Bảng tuần hoàn và hóa vô cơ | `W24` | `T01` Nguyên tố; `T02` Tính tuần hoàn; `T03` Kim loại và phi kim; `T04` Phức chất; `T05` Hóa học phối trí; `T06` Hóa học vô cơ hiện đại | — | — |
| `B1.3-C03` | Liên kết và cấu trúc phân tử | `W25` | `T01` Liên kết ion; `T02` Liên kết cộng hóa trị; `T03` Liên kết kim loại; `T04` Lực liên phân tử; `T05` Hình học phân tử; `T06` Phổ học | — | `R07` |
| `B1.3-C04` | Phản ứng và cân bằng | `W26` | `T01` Phương trình hóa học; `T02` Bảo toàn khối lượng; `T03` Nhiệt hóa học; `T04` Động học; `T05` Cân bằng hóa học; `T06` Acid–base; `T07` Oxy hóa–khử; `T08` Điện hóa học | — | `R08` |
| `B1.3-C05` | Hóa phân tích | `W27` | `T01` Phân tích định tính; `T02` Phân tích định lượng; `T03` Chuẩn độ; `T04` Sắc ký; `T05` Khối phổ; `T06` Phổ học phân tích; `T07` Cảm biến hóa học | — | — |
| `B1.3-C06` | Hóa hữu cơ | `W28` | `T01` Cấu trúc carbon; `T02` Nhóm chức; `T03` Cơ chế phản ứng; `T04` Hóa lập thể; `T05` Tổng hợp hữu cơ; `T06` Hóa dược; `T07` Hóa học polymer | — | — |
| `B1.3-C07` | Hóa lý và hóa học lý thuyết | `W29` | `T01` Nhiệt động hóa học; `T02` Động học hóa học; `T03` Hóa lượng tử; `T04` Hóa học bề mặt; `T05` Hóa keo; `T06` Hóa học tính toán | — | `R07`, `R08` |
| `B1.3-C08` | Hóa sinh và sinh học hóa học | `W30` | `T01` Amino acid và protein; `T02` Carbohydrate; `T03` Lipid; `T04` Acid nucleic; `T05` Enzyme; `T06` Chuyển hóa; `T07` Thiết kế phân tử sinh học | `X03`, `X04` | `R14` |
| `B1.3-C09` | Khoa học vật liệu | `W31` | `T01` Kim loại; `T02` Gốm; `T03` Polymer; `T04` Composite; `T05` Vật liệu điện tử; `T06` Vật liệu nano; `T07` Vật liệu thông minh; `T08` Vật liệu sinh học | — | `R09` |
| `B1.3-C10` | Hóa học môi trường, công nghiệp và bền vững | `W32` | `T01` Hóa học khí quyển; `T02` Hóa học nước và đất; `T03` Ô nhiễm và độc chất; `T04` Quy trình công nghiệp; `T05` Xúc tác; `T06` Hóa học xanh; `T07` Kinh tế nguyên tử; `T08` Vòng đời vật liệu | `X01`, `X03`, `X04` | `R11`, `R12`, `R14` |
| `B1.4-C01` | Khoáng vật, đá và địa hóa | `W45` | `T01` Khoáng vật, đá và địa hóa | — | `R11` |
| `B1.4-C02` | Cấu trúc bên trong Trái Đất | `W45` | `T01` Cấu trúc bên trong Trái Đất | — | — |
| `B1.4-C03` | Địa vật lý | `W45` | `T01` Địa vật lý | — | `R10` |
| `B1.4-C04` | Kiến tạo mảng | `W46` | `T01` Kiến tạo mảng | — | — |
| `B1.4-C05` | Núi lửa và động đất | `W46` | `T01` Núi lửa và động đất | — | — |
| `B1.4-C06` | Trầm tích và lịch sử địa chất | `W46` | `T01` Trầm tích và lịch sử địa chất | — | — |
| `B1.4-C07` | Địa mạo và đất | `W47` | `T01` Địa mạo và đất | `X04` | `R11`, `R14` |
| `B1.4-C08` | Thủy văn và nước ngầm | `W47` | `T01` Thủy văn và nước ngầm | `X04`, `X05` | `R11`, `R14` |
| `B1.4-C09` | Băng quyển | `W47` | `T01` Băng quyển | `X01` | `R12` |
| `B1.4-C10` | Khí quyển và khí tượng | `W48` | `T01` Khí quyển và khí tượng | `X01`, `X05` | `R10`, `R11`, `R12` |
| `B1.4-C11` | Đại dương học | `W48` | `T01` Đại dương học | `X01` | `R12` |
| `B1.4-C12` | Hệ thống khí hậu | `W48` | `T01` Hệ thống khí hậu | `X01` | `R11`, `R12` |
| `B1.4-C13` | Cổ khí hậu | `W49` | `T01` Cổ khí hậu | `X01` | `R12` |
| `B1.4-C14` | Tài nguyên và địa chất môi trường | `W49` | `T01` Tài nguyên và địa chất môi trường | `X05` | `R11` |
| `B1.4-C15` | Tai biến tự nhiên | `W49` | `T01` Tai biến tự nhiên | `X05` | — |
| `B1.4-C16` | Khoa học hành tinh | `W50` | `T01` Khoa học hành tinh | — | — |
| `B1.4-C17` | Mặt Trời và môi trường không gian | `W50` | `T01` Mặt Trời và môi trường không gian | — | `R10` |
| `B1.4-C18` | Thiên văn quan sát | `W50` | `T01` Thiên văn quan sát | — | — |
| `B1.4-C19` | Sao và hệ sao | `W51` | `T01` Sao và hệ sao | — | — |
| `B1.4-C20` | Thiên hà | `W51` | `T01` Thiên hà | — | — |
| `B1.4-C21` | Vật lý thiên văn | `W51` | `T01` Vật lý thiên văn | — | `R10` |
| `B1.4-C22` | Lỗ đen và vật thể đặc | `W52` | `T01` Lỗ đen và vật thể đặc | — | `R10` |
| `B1.4-C23` | Vũ trụ học | `W52` | `T01` Vũ trụ học | — | — |
| `B1.4-C24` | Nguồn gốc và diễn tiến của vũ trụ | `W52` | `T01` Nguồn gốc và diễn tiến của vũ trụ | — | — |
| `B1.5-C01` | Biểu diễn và lý thuyết thông tin | `W33` | `T01` Bit và mã; `T02` Entropy [R01]; `T03` Nén; `T04` Truyền tin; `T05` Mã sửa lỗi [R02]; `T06` Giới hạn thông tin | — | — |
| `B1.5-C02` | Nền tảng tính toán | `W34` | `T01` Logic tính toán; `T02` Ngôn ngữ hình thức; `T03` Máy tự động; `T04` Khả tính; `T05` Độ phức tạp; `T06` Giới hạn của tính toán | — | `R04` |
| `B1.5-C03` | Thuật toán và cấu trúc dữ liệu | `W35` | `T01` Tìm kiếm; `T02` Sắp xếp; `T03` Cây và đồ thị; `T04` Quy hoạch động; `T05` Thuật toán ngẫu nhiên; `T06` Thuật toán xấp xỉ; `T07` Phân tích độ phức tạp | `X02` | `R05`, `R13` |
| `B1.5-C04` | Lập trình và ngôn ngữ lập trình | `W36` | `T01` Mô hình lập trình; `T02` Kiểu dữ liệu; `T03` Trừu tượng hóa; `T04` Trình biên dịch; `T05` Kiểm chứng chương trình; `T06` Phương pháp hình thức | — | `R04` |
| `B1.5-C05` | Kỹ nghệ phần mềm | `W37` | `T01` Phân tích yêu cầu; `T02` Kiến trúc phần mềm; `T03` Thiết kế và kiểm thử; `T04` Quản lý phiên bản; `T05` Độ tin cậy; `T06` DevOps; `T07` Bảo trì | — | — |
| `B1.5-C06` | Phần cứng và hệ thống máy tính | `W38` | `T01` Logic số; `T02` Kiến trúc máy tính; `T03` Bộ xử lý và bộ nhớ; `T04` Hệ điều hành; `T05` Hệ nhúng; `T06` Internet vạn vật; `T07` Tính toán hiệu năng cao | — | — |
| `B1.5-C07` | Dữ liệu và khoa học thông tin | `W39` | `T01` Cơ sở dữ liệu; `T02` Mô hình dữ liệu; `T03` Kho dữ liệu; `T04` Kỹ nghệ dữ liệu; `T05` Khoa học dữ liệu; `T06` Tìm kiếm thông tin; `T07` Tổ chức tri thức; `T08` Thư viện và lưu trữ số; `T09` Quản trị dữ liệu | `X02`, `X03`, `X05`, `X07` | `R06`, `R12`, `R13`, `R14` |
| `B1.5-C08` | Mạng và hệ phân tán | `W40` | `T01` Mạng máy tính; `T02` Internet; `T03` Giao thức; `T04` Hệ phân tán; `T05` Điện toán đám mây; `T06` Điện toán biên; `T07` Hệ thống chịu lỗi | `X05`, `X08` | — |
| `B1.5-C09` | An ninh và mật mã | `W41` | `T01` Mật mã học; `T02` Xác thực; `T03` An ninh mạng; `T04` An ninh phần mềm; `T05` Quyền riêng tư; `T06` Điều tra số; `T07` Quản trị rủi ro thông tin | `X05`, `X07`, `X08` | `R15` |
| `B1.5-C10` | Trí tuệ nhân tạo | `W42` | `T01` Tìm kiếm và lập kế hoạch; `T02` Biểu diễn tri thức; `T03` Học máy; `T04` Học sâu; `T05` Xử lý ngôn ngữ; `T06` Thị giác máy tính; `T07` Hệ đa tác tử; `T08` Robot thông minh; `T09` Đánh giá và an toàn AI; `T10` Giới hạn của trí tuệ máy | `X02`, `X06`, `X07`, `X08` | `R06`, `R13`, `R15` |
| `B1.5-C11` | Tương tác người–máy | `W43` | `T01` Thiết kế giao diện; `T02` Trải nghiệm người dùng; `T03` Khả năng tiếp cận; `T04` Đồ họa máy tính; `T05` Trực quan hóa dữ liệu; `T06` Thực tế ảo và tăng cường; `T07` Tính toán xã hội | `X02`, `X05`, `X06`, `X08` | `R13`, `R15` |
| `B1.5-C12` | Các mô hình tính toán mới | `W44` | `T01` Tính toán lượng tử; `T02` Tính toán sinh học; `T03` Tính toán thần kinh; `T04` Tính toán xác suất; `T05` Tính toán lấy cảm hứng từ tự nhiên | `X06` | — |

## 3. Exact repeated-label reconciliation

| Label | Canonical topic IDs | Architecture disposition |
|---|---|---|
| `Dao động` | `B1.1-C06-T05`; `B1.2-C02-T06` | `R03`: formal dynamical-system role vs measurable physical oscillation; cross-link, no ownership collision. |
| `Mã sửa lỗi` | `B1.1-C08-T07`; `B1.5-C01-T05` | `R02`: combinatorial/algebraic properties vs communication/reliability role; claim-boundary cross-link. |
| `Entropy` | `B1.2-C04-T03`; `B1.5-C01-T02` | `R01`: thermodynamic/statistical-mechanical entropy vs information entropy; cross-link, not lexical merge. |

## 4. Mandatory cross-domain node accounting

The eight canonical shared nodes are retained as graph intersections, not duplicate primary owners. The scope map records evident B1 secondary participation; non-B1 claims remain with their canonical branches.

| ID | Mandatory node | B1 secondary scope links recorded |
|---|---|---|
| `X01` | BIẾN ĐỔI KHÍ HẬU | `B1.2-C12`, `B1.3-C10`, `B1.4-C09`, `B1.4-C10`, `B1.4-C11`, `B1.4-C12`, `B1.4-C13` |
| `X02` | TRÍ TUỆ NHÂN TẠO | `B1.1-C03`, `B1.1-C07`, `B1.1-C10`, `B1.5-C03`, `B1.5-C07`, `B1.5-C10`, `B1.5-C11` |
| `X03` | SỨC KHỎE TOÀN CẦU | `B1.2-C12`, `B1.3-C08`, `B1.3-C10`, `B1.5-C07` |
| `X04` | THỰC PHẨM | `B1.3-C08`, `B1.3-C10`, `B1.4-C07`, `B1.4-C08` |
| `X05` | THÀNH PHỐ | `B1.2-C12`, `B1.4-C08`, `B1.4-C10`, `B1.4-C14`, `B1.4-C15`, `B1.5-C07`, `B1.5-C08`, `B1.5-C09`, `B1.5-C11` |
| `X06` | Ý THỨC | `B1.5-C10`, `B1.5-C11`, `B1.5-C12` |
| `X07` | CÔNG BẰNG | `B1.1-C10`, `B1.5-C07`, `B1.5-C09`, `B1.5-C10` |
| `X08` | HÒA BÌNH | `B1.5-C08`, `B1.5-C09`, `B1.5-C10`, `B1.5-C11` |

## 5. Semantic-overlap control

Risk tags `R01`–`R15` are defined in `B1_DUPLICATE_CONTROL.md`. A successor may not clear a tagged scope merely by changing examples, wording, age pathway, characters or scenery. It must compare node meaning, claims, learning objective and context against prior accepted B1 artifacts, then record either reuse/reference, a typed cross-link, or a justified distinct objective.

## 6. Coverage conclusion

**PASS at architecture level.** All 348 canonical B1 topic leaves are present, every leaf has exactly one stable primary authoring unit and one bounded child-window owner, no orphan exists, and all detected repeated labels/semantic-overlap zones have an explicit control path. This does not pre-approve future authored curriculum content; child and integration windows must repeat coverage and semantic-duplicate audits on actual nodes/claims/objectives.
