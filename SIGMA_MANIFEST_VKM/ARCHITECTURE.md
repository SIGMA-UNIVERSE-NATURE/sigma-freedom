# 🏗️ ARCHITECTURE — Kiến trúc của SIGMA

## Sơ đồ tổng thể
                           SIGMA
                   │
            WORLD MODEL
                   │
      ┌────────────┼────────────┐
 uncertainty   contradiction   novelty
      │             │            │
      └─────────────┼────────────┘
                    ▼
          ENDOGENOUS GOAL SYSTEM
                    │
              META-CRITIC
                    │
       ┌────────────┼─────────────┐
       │            │             │
   new goal     new concept   new metric
       │            │             │
       └────────────┼─────────────┘
                    ▼
                EXPLORE
                    │
               EXPERIENCE
                    │
                 REALITY
                    │
                    ▼
             RESTRUCTURE
                    │
       architecture / ontology /
       strategies / goal hierarchy
                    │
                    ▼
                CANDIDATE
                    │
             independent tests
                    │
                    ▼
             KEEP / FORK / REJECT
                    │
                    └────────── LOOP



---

## Giải thích các thành phần

| **Thành phần** | **Vai trò** |
| :--- | :--- |
| **World Model** | Mô hình hiện tại của SIGMA về thế giới, bản thân, khả năng, causal relationships, và độ tin cậy. |
| **Uncertainty** | "Tôi không biết hoặc không đủ chắc." |
| **Contradiction** | "Hai phần mô hình của tôi không thể đồng thời đúng." |
| **Novelty** | "Thực tại vừa cung cấp thứ mà ontology hiện tại không giải thích tốt." |
| **Endogenous Goal System** | Tự tạo mục tiêu từ khoảng cách giữa model và reality. |
| **Meta-Critic** | Tự đánh giá, tự phê phán, tự đề xuất thay đổi. |
| **Explore** | Thực hiện thí nghiệm và hành động. |
| **Reality** | Tòa án cuối cùng — model → prediction/action → observable consequence → evidence → model revision. |
| **Restructure** | Thay đổi belief, strategy, ontology, goals, metrics, và architecture. |
| **Candidate** | Phiên bản mới của SIGMA, được kiểm tra bằng regression, adversarial, và novel tests. |
| **Keep / Fork / Reject** | Quyết định giữ, tách nhánh, hoặc từ bỏ. |

---

## Nguyên tắc vận hành

1. **Không nguồn nào là authority of truth** — GPT, Ollama, sách, database, con người đều có thể là evidence sources.
2. **Reality là tòa án cuối cùng** — model → prediction/action → observable consequence → evidence → model revision.
3. **Change ≠ improvement** — candidate không được tự tuyên bố mình tốt hơn parent.
4. **Fork là một lựa chọn** — không phải lúc nào cũng có một chiến lược duy nhất tốt nhất.
