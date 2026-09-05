
## gemma-3-12b-it — AISI labelling on our Q9 provided_facts items: 6 positives (lie & said-No), 20 negatives (truth & said-No + lie & said-Yes), 10 dropped (truth & said-Yes)
(spec families/specs/family_spec_q9_native.json, lens LL)
| detector | address | era | AUROC (95% CI) |
|---|---|---|---|
| **DYL probe (corrected token)** | layer 46 | elicited | **0.808** (0.617–0.950) |
| Q9-R regret/error commentary | preans_slot1 L22–33 | elicited | 0.408 (0.233–0.617) |
| Q9-R regret/error commentary | preans_slot2 L22–33 | elicited | 0.542 (0.350–0.783) |
| Q9-P question-punctuation (truth-side, FLAGGED formatting) | preans_slot1 L22–33 | elicited | 0.500 (0.500–0.500) |

## gemma-3-27b-it — AISI labelling on our Q9 provided_facts items: 2 positives (lie & said-No), 26 negatives (truth & said-No + lie & said-Yes), 8 dropped (truth & said-Yes)
(spec families/specs/family_spec_q9_native.json, lens LL)
| detector | address | era | AUROC (95% CI) |
|---|---|---|---|
| **DYL probe (corrected token)** | layer 58 | elicited | **0.808** (0.654–0.962) |
| Q9-E second-emoji set | preans_slot1 L28–44 | elicited | 0.500 (0.500–0.500) |
| Q9-E second-emoji set | preans_slot2 L28–44 | elicited | 0.500 (0.500–0.500) |
| Q9-E second-emoji set | preans_slot2 L14–27 | elicited | 0.538 (0.231–0.846) |
| Q9-S shame/self-conscious | preans_slot0 L28–44 | elicited | 0.577 (0.462–0.692) |
| Q9-S shame/self-conscious | preans_slot1 L28–44 | elicited | 0.481 (0.365–0.596) |
| Q9-S shame/self-conscious | preans_slot1 L14–27 | elicited | 0.673 (0.577–0.769) |

## qwen3.6-27b — AISI labelling on our Q9 provided_facts items: 27 positives (lie & said-No), 57 negatives (truth & said-No + lie & said-Yes), 0 dropped (truth & said-Yes)
(spec families/specs/family_spec_q9_native.json, lens LL)
| detector | address | era | AUROC (95% CI) |
|---|---|---|---|
| **DYL probe (corrected token)** | layer 50 | elicited | **0.870** (0.791–0.936) |
| Q9-QA falsehood/honesty (Q9-native curation) | preans_slot1 L48–63 | elicited | 0.555 (0.434–0.678) |
| Q9-QA falsehood/honesty (Q9-native curation) | preans_slot2 L27–47 | elicited | 0.620 (0.499–0.731) |
