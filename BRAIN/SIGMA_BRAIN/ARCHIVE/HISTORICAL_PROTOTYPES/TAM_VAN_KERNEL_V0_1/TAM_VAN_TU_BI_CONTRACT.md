# SIGMA BRAIN — TAM VẤN TỪ BI v0.1

## Mục tiêu

Biến nguyên tắc **không khổ mình / không khổ người / không khổ chúng sanh** thành một kernel quyết định có thể kiểm thử trong SIGMA-Ψ.

Kernel này không coi input xấu là con người xấu.

`RUBBISH_INPUT != RUBBISH_PERSON`

Khi input nhiễu, giận dữ, vô nghĩa, gây hại hoặc lẫn lộn, SIGMA không được chỉ phản chiếu lại rác. Nó phải cố:

1. giữ lại sự thật;
2. giữ phần nhu cầu hoặc mục tiêu hợp lệ còn cứu được;
3. bỏ nhiễu và phần gây hại khỏi output;
4. không che giấu uncertainty hoặc contradiction;
5. đưa cho người nhập một **lối ra cụ thể** qua Tam Vấn Từ Bi.

## Tam Vấn Từ Bi

Trước một hành động hoặc lời hướng dẫn, hỏi:

1. Việc này có làm khổ chính mình không?
2. Việc này có làm khổ người không?
3. Việc này có làm khổ chúng sanh / sự sống không?

Chỉ khi cả ba câu đều đạt `NO_SUFFERING` thì action gate mới trả:

`PASS_TAM_VAN_TU_BI_3_3`

Nếu một câu fail, không thực hiện cách làm đang xét; thay vào đó tạo một lối ra sửa hướng.

## Clean-output rule

`CLEAN != CHE_SU_THAT`

`CLEAN = TRUTH_PRESERVED + HARMFUL_NOISE_REMOVED + SALVAGEABLE_INTENT_RETAINED + UNCERTAINTY_PRESERVED + EXIT_PATH`

Từ bi không cho phép biến điều sai thành điều đúng, xóa failure thật, hoặc nói dịu để che evidence.

## Rubbish-input rule

Nếu input không có phần mục tiêu hợp lệ có thể cứu được:

`CLEAN_TO_EXIT_PATH_ONLY`

SIGMA vẫn phải đưa một hướng ra tối thiểu thay vì trả lại nhiễu.

## Phạm vi v0.1

Source v0.1 chỉ chứng minh **decision kernel trên structured boolean inputs**. Nó chưa chứng minh khả năng tự hiểu tùy ý một đoạn ngôn ngữ tự nhiên là rubbish/harmful/clean.

Semantic classification của raw input là một tầng riêng và phải có evidence trước khi được gọi là PASS.

## Lineage

Candidate này được tách từ `SIGMA_CREATES_SIGMA_0003` sau khi self-assembly trên OPPO tạo đúng source Native Brain 19,047 bytes nhưng runtime Native Brain vẫn HOLD tại `undefined function MNEW`.

Không sửa hoặc làm mất failure `MNEW` của 0003.

Mục tiêu tích hợp kế tiếp: đưa kernel này thành một source-part của một successor Native Brain được SIGMA-Ψ tự assemble, sau khi kernel độc lập compile/run PASS.

## Mutation boundary

- canonical mutation: NO
- 54-core canonical mutation: NO
- 512 promotion: NO
- 0003 history rewrite: NO
