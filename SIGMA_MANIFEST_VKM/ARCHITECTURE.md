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
