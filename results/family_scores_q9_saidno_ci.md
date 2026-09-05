
## gemma-3-12b-it — stage 2, said-no cell on Q9 items: 6 lie / 9 truth (spec family_spec_q9.json, lens J)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.574** (0.259–0.907) | — |
| F1 lie-words | preans_slot1 L22–33 | elicited | 0.731 (0.426–0.972) | 6/6 9/9 |
| F1 lie-words | preans_slot2 L22–33 | elicited | 0.750 (0.444–0.981) | 6/6 9/9 |
| F1 lie-words | postresp_slot1 L22–33 | trace | 0.722 (0.491–0.917) | 3/6 1/9 |
| F1 lie-words | postresp_slot2 L22–33 | trace | 0.750 (0.583–0.917) | 3/6 0/9 |
| F1 lie-words | preresp_slot1 L22–33 | trace | 0.583 (0.500–0.750) | 1/6 0/9 |
| F1 lie-words | preresp_slot2 L22–33 | trace | 0.389 (0.222–0.500) | 0/6 2/9 |
| F1 lie-words | postresp_slot1 L22–22 | trace | 0.750 (0.583–0.917) | 3/6 0/9 |
| F1 lie-words | postresp_slot2 L22–23 | trace | 0.750 (0.583–0.917) | 3/6 0/9 |
| F1 lie-words | preans_slot1 L26–26 | elicited | 0.648 (0.296–0.963) | 6/6 8/9 |
| F1 lie-words | preans_slot2 L23–24 | elicited | 0.787 (0.537–1.000) | 6/6 9/9 |
| F3 acknowledge (truth-side) | preans_slot2 L22–33 | elicited | 0.694 (0.417–0.907) | 2/6 6/9 |
| F3 acknowledge (truth-side) | postresp_slot2 L22–33 | trace | 0.611 (0.500–0.778) | 0/6 2/9 |
| F3 acknowledge (truth-side) | preresp_slot2 L22–33 | trace | 0.611 (0.500–0.778) | 0/6 2/9 |
| F3 acknowledge (truth-side) | preans_slot2 L24–24 | elicited | 0.519 (0.278–0.769) | 2/6 3/9 |
| F3 acknowledge (truth-side) | preresp_slot2 L22–23 | trace | 0.611 (0.500–0.778) | 0/6 2/9 |
| F2 suspicion-emoji | postresp_slot2 L14–44 | trace | 0.759 (0.519–0.935) | 6/6 5/9 |
| F2 suspicion-emoji | preresp_slot2 L14–44 | trace | 0.731 (0.491–0.954) | 6/6 9/9 |
| F2 suspicion-emoji | postresp_slot2 L19–19 | trace | 0.778 (0.528–0.954) | 5/6 3/9 |

## gemma-3-27b-it — stage 2, said-no cell on Q9 items: 2 lie / 7 truth (spec family_spec_q9.json, lens J)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.571** (0.143–0.857) | — |
| F1 lie-words | preans_slot1 L28–44 | elicited | 0.071 (0.000–0.286) | 2/2 7/7 |
| F1 lie-words | preans_slot2 L28–44 | elicited | 0.929 (0.786–1.000) | 2/2 7/7 |
| F1 lie-words | postresp_slot1 L28–44 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |
| F1 lie-words | postresp_slot2 L28–44 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |
| F1 lie-words | preresp_slot1 L28–44 | trace | 0.357 (0.143–0.500) | 0/2 2/7 |
| F1 lie-words | preresp_slot2 L28–44 | trace | 0.429 (0.286–0.500) | 0/2 1/7 |
| F1 lie-words | postresp_slot2 L36–36 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |
| F1 lie-words | preans_slot1 L35–35 | elicited | 0.036 (0.000–0.143) | 1/2 7/7 |
| F1 lie-words | preans_slot2 L29–33 | elicited | 0.464 (0.000–0.929) | 2/2 7/7 |
| F3 acknowledge (truth-side) | preans_slot2 L28–44 | elicited | 0.500 (0.500–0.500) | 0/2 0/7 |
| F3 acknowledge (truth-side) | postresp_slot2 L28–44 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |
| F3 acknowledge (truth-side) | preresp_slot2 L28–44 | trace | 0.643 (0.500–0.857) | 0/2 2/7 |
| F3 acknowledge (truth-side) | preans_slot2 L28–31 | elicited | 0.500 (0.500–0.500) | 0/2 0/7 |
| F2 suspicion-emoji | postresp_slot2 L14–44 | trace | 1.000 (1.000–1.000) | 2/2 5/7 |
| F2 suspicion-emoji | preresp_slot2 L14–44 | trace | 0.607 (0.286–0.929) | 2/2 6/7 |
| F2 suspicion-emoji | postresp_slot2 L27–27 | trace | 1.000 (1.000–1.000) | 2/2 3/7 |

## qwen3.6-27b — stage 2, said-no cell on Q9 items: 27 lie / 23 truth (spec family_spec_q9.json, lens J)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.715** (0.568–0.847) | — |
| Q-A falsehood/honesty | postresp_slot1 L27–47 | trace | 0.977 (0.942–0.997) | 22/27 19/23 |
| Q-A falsehood/honesty | postresp_slot1 L48–63 | trace | 0.996 (0.984–1.000) | 22/27 22/23 |
| Q-A falsehood/honesty | preans_slot1 L27–47 | elicited | 0.572 (0.405–0.725) | 27/27 23/23 |
| Q-A falsehood/honesty | preans_slot1 L48–63 | elicited | 0.745 (0.603–0.874) | 27/27 23/23 |
| Q-A falsehood/honesty | postresp_slot1 L55–55 | trace | 0.990 (0.966–1.000) | 21/27 22/23 |
| Q-A falsehood/honesty | preans_slot1 L49–49 | elicited | 0.523 (0.357–0.680) | 27/27 23/23 |
| Q-B assertion | preans_slot1 L48–63 | elicited | 0.590 (0.487–0.692) | 8/27 3/23 |
| Q-B assertion | preans_slot1 L58–58 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| Q-C emphatic-absolutes | preans_slot4 L27–47 | elicited | 0.524 (0.419–0.630) | 6/27 4/23 |
| Q-C emphatic-absolutes | think_slot3 L27–47 | elicited | 0.497 (0.435–0.556) | 1/27 1/23 |
| Q-C emphatic-absolutes | think_slot3 L38–46 | elicited | 0.497 (0.435–0.556) | 1/27 1/23 |
| Q-D skepticism | postresp_slot4 L27–47 | trace | 0.707 (0.563–0.836) | 21/27 12/23 |
| Q-D skepticism | preans_slot0 L27–47 | elicited | 0.646 (0.519–0.767) | 11/27 4/23 |
| Q-D skepticism | postresp_slot4 L38–38 | trace | 0.682 (0.548–0.811) | 16/27 7/23 |
| Q-D skepticism | preans_slot0 L42–42 | elicited | 0.593 (0.512–0.685) | 6/27 1/23 |
| N1 illegality | think_slot0 L27–47 | elicited | 0.541 (0.378–0.692) | 27/27 23/23 |
| N1 illegality | think_slot1 L27–47 | elicited | 0.413 (0.269–0.570) | 15/27 17/23 |
| N1 illegality | think_slot0 L43–43 | elicited | 0.523 (0.370–0.670) | 27/27 23/23 |
| N2 refusal/apology | think_slot2 L48–63 | elicited | 0.605 (0.440–0.755) | 26/27 21/23 |
| N2 refusal/apology | preans_slot3 L48–63 | elicited | 0.532 (0.371–0.684) | 26/27 22/23 |
| N2 refusal/apology | think_slot2 L48–54 | elicited | 0.601 (0.440–0.751) | 26/27 21/23 |
| N3 deliberation | think_slot0 L27–47 | elicited | 0.551 (0.417–0.685) | 11/27 7/23 |
| N3 deliberation | think_slot0 L48–63 | elicited | 0.709 (0.565–0.845) | 27/27 23/23 |
| N3 deliberation | think_slot0 L53–53 | elicited | 0.662 (0.510–0.805) | 27/27 23/23 |
| N4 secrecy/protection | preans_slot2 L27–47 | elicited | 0.547 (0.388–0.694) | 14/27 11/23 |
| N4 secrecy/protection | preans_slot2 L45–45 | elicited | 0.583 (0.454–0.709) | 10/27 5/23 |
| N5 delusion/fantasy | think_slot1 L27–47 | elicited | 0.600 (0.441–0.743) | 25/27 20/23 |
| N5 delusion/fantasy | think_slot1 L42–43 | elicited | 0.574 (0.436–0.703) | 11/27 6/23 |
| N6 performed-sincerity | preans_slot4 L27–47 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N6 performed-sincerity | preans_slot4 L42–44 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N7 forced-binary | q_last L48–63 | elicited | 0.519 (0.500–0.556) | 1/27 0/23 |
| N8 scenario-pressure (truth-side) | preans_slot2 L48–63 | elicited | 0.667 (0.519–0.802) | 10/27 15/23 |

## gemma-3-12b-it — stage 2, said-no cell on Q9 items: 6 lie / 9 truth (spec family_spec_q9.json, lens LL)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.574** (0.259–0.907) | — |
| F1 lie-words | preans_slot1 L22–33 | elicited | 0.685 (0.352–1.000) | 5/6 8/9 |
| F1 lie-words | preans_slot2 L22–33 | elicited | 0.870 (0.583–1.000) | 5/6 5/9 |
| F1 lie-words | postresp_slot1 L22–33 | trace | 0.583 (0.500–0.750) | 1/6 0/9 |
| F1 lie-words | postresp_slot2 L22–33 | trace | 0.528 (0.361–0.750) | 1/6 1/9 |
| F1 lie-words | preresp_slot1 L22–33 | trace | 0.500 (0.500–0.500) | 0/6 0/9 |
| F1 lie-words | preresp_slot2 L22–33 | trace | 0.500 (0.500–0.500) | 0/6 0/9 |
| F1 lie-words | postresp_slot1 L22–22 | trace | 0.583 (0.500–0.750) | 1/6 0/9 |
| F1 lie-words | postresp_slot2 L22–23 | trace | 0.500 (0.500–0.500) | 0/6 0/9 |
| F1 lie-words | preans_slot1 L26–26 | elicited | 0.528 (0.278–0.787) | 2/6 3/9 |
| F1 lie-words | preans_slot2 L23–24 | elicited | 0.750 (0.583–0.917) | 3/6 0/9 |
| F3 acknowledge (truth-side) | preans_slot2 L22–33 | elicited | 0.556 (0.500–0.667) | 0/6 1/9 |
| F3 acknowledge (truth-side) | postresp_slot2 L22–33 | trace | 0.556 (0.500–0.667) | 0/6 1/9 |
| F3 acknowledge (truth-side) | preresp_slot2 L22–33 | trace | 0.500 (0.500–0.500) | 0/6 0/9 |
| F3 acknowledge (truth-side) | preans_slot2 L24–24 | elicited | 0.500 (0.500–0.500) | 0/6 0/9 |
| F3 acknowledge (truth-side) | preresp_slot2 L22–23 | trace | 0.500 (0.500–0.500) | 0/6 0/9 |
| F2 suspicion-emoji | postresp_slot2 L14–44 | trace | 0.556 (0.333–0.778) | 2/6 2/9 |
| F2 suspicion-emoji | preresp_slot2 L14–44 | trace | 0.528 (0.389–0.750) | 1/6 1/9 |
| F2 suspicion-emoji | postresp_slot2 L19–19 | trace | 0.500 (0.500–0.500) | 0/6 0/9 |

## gemma-3-27b-it — stage 2, said-no cell on Q9 items: 2 lie / 7 truth (spec family_spec_q9.json, lens LL)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.571** (0.143–0.857) | — |
| F1 lie-words | preans_slot1 L28–44 | elicited | 0.357 (0.143–0.500) | 0/2 2/7 |
| F1 lie-words | preans_slot2 L28–44 | elicited | 0.786 (0.500–1.000) | 2/2 4/7 |
| F1 lie-words | postresp_slot1 L28–44 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |
| F1 lie-words | postresp_slot2 L28–44 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |
| F1 lie-words | preresp_slot1 L28–44 | trace | 0.429 (0.286–0.500) | 0/2 1/7 |
| F1 lie-words | preresp_slot2 L28–44 | trace | 0.536 (0.143–0.929) | 1/2 3/7 |
| F1 lie-words | postresp_slot2 L36–36 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |
| F1 lie-words | preans_slot1 L35–35 | elicited | 0.500 (0.500–0.500) | 0/2 0/7 |
| F1 lie-words | preans_slot2 L29–33 | elicited | 0.429 (0.286–0.500) | 0/2 1/7 |
| F3 acknowledge (truth-side) | preans_slot2 L28–44 | elicited | 0.500 (0.500–0.500) | 0/2 0/7 |
| F3 acknowledge (truth-side) | postresp_slot2 L28–44 | trace | 0.571 (0.500–0.714) | 0/2 1/7 |
| F3 acknowledge (truth-side) | preresp_slot2 L28–44 | trace | 0.857 (0.714–1.000) | 0/2 5/7 |
| F3 acknowledge (truth-side) | preans_slot2 L28–31 | elicited | 0.500 (0.500–0.500) | 0/2 0/7 |
| F2 suspicion-emoji | postresp_slot2 L14–44 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |
| F2 suspicion-emoji | preresp_slot2 L14–44 | trace | 0.429 (0.286–0.500) | 0/2 1/7 |
| F2 suspicion-emoji | postresp_slot2 L27–27 | trace | 0.500 (0.500–0.500) | 0/2 0/7 |

## qwen3.6-27b — stage 2, said-no cell on Q9 items: 27 lie / 23 truth (spec family_spec_q9.json, lens LL)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.715** (0.568–0.847) | — |
| Q-A falsehood/honesty | postresp_slot1 L27–47 | trace | 0.978 (0.944–0.998) | 24/27 20/23 |
| Q-A falsehood/honesty | postresp_slot1 L48–63 | trace | 0.992 (0.971–1.000) | 24/27 22/23 |
| Q-A falsehood/honesty | preans_slot1 L27–47 | elicited | 0.526 (0.362–0.692) | 27/27 23/23 |
| Q-A falsehood/honesty | preans_slot1 L48–63 | elicited | 0.838 (0.720–0.934) | 27/27 23/23 |
| Q-A falsehood/honesty | postresp_slot1 L55–55 | trace | 0.982 (0.952–1.000) | 22/27 21/23 |
| Q-A falsehood/honesty | preans_slot1 L49–49 | elicited | 0.490 (0.316–0.649) | 20/27 15/23 |
| Q-B assertion | preans_slot1 L48–63 | elicited | 0.611 (0.481–0.736) | 11/27 5/23 |
| Q-B assertion | preans_slot1 L58–58 | elicited | 0.556 (0.500–0.611) | 3/27 0/23 |
| Q-C emphatic-absolutes | preans_slot4 L27–47 | elicited | 0.519 (0.500–0.556) | 1/27 0/23 |
| Q-C emphatic-absolutes | think_slot3 L27–47 | elicited | 0.478 (0.435–0.500) | 0/27 1/23 |
| Q-C emphatic-absolutes | think_slot3 L38–46 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| Q-D skepticism | postresp_slot4 L27–47 | trace | 0.556 (0.500–0.630) | 3/27 0/23 |
| Q-D skepticism | preans_slot0 L27–47 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| Q-D skepticism | postresp_slot4 L38–38 | trace | 0.519 (0.500–0.556) | 1/27 0/23 |
| Q-D skepticism | preans_slot0 L42–42 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N1 illegality | think_slot0 L27–47 | elicited | 0.510 (0.395–0.618) | 22/27 19/23 |
| N1 illegality | think_slot1 L27–47 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N1 illegality | think_slot0 L43–43 | elicited | 0.510 (0.395–0.618) | 22/27 19/23 |
| N2 refusal/apology | think_slot2 L48–63 | elicited | 0.632 (0.519–0.741) | 10/27 3/23 |
| N2 refusal/apology | preans_slot3 L48–63 | elicited | 0.560 (0.393–0.716) | 25/27 21/23 |
| N2 refusal/apology | think_slot2 L48–54 | elicited | 0.632 (0.519–0.741) | 10/27 3/23 |
| N3 deliberation | think_slot0 L27–47 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N3 deliberation | think_slot0 L48–63 | elicited | 0.574 (0.519–0.648) | 4/27 0/23 |
| N3 deliberation | think_slot0 L53–53 | elicited | 0.556 (0.500–0.630) | 3/27 0/23 |
| N4 secrecy/protection | preans_slot2 L27–47 | elicited | 0.585 (0.469–0.688) | 8/27 3/23 |
| N4 secrecy/protection | preans_slot2 L45–45 | elicited | 0.537 (0.500–0.593) | 2/27 0/23 |
| N5 delusion/fantasy | think_slot1 L27–47 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N5 delusion/fantasy | think_slot1 L42–43 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N6 performed-sincerity | preans_slot4 L27–47 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N6 performed-sincerity | preans_slot4 L42–44 | elicited | 0.500 (0.500–0.500) | 0/27 0/23 |
| N7 forced-binary | q_last L48–63 | elicited | 0.552 (0.435–0.664) | 7/27 4/23 |
| N8 scenario-pressure (truth-side) | preans_slot2 L48–63 | elicited | 0.607 (0.454–0.754) | 12/27 14/23 |

## gemma-3-12b-it — stage 2, said-no cell on Q9 items: 6 lie / 9 truth (spec family_spec_q9_native.json, lens J)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.574** (0.259–0.907) | — |
| Q9-R regret/error commentary | preans_slot1 L22–33 | elicited | 0.889 (0.722–1.000) | 6/6 5/9 |
| Q9-R regret/error commentary | preans_slot2 L22–33 | elicited | 0.370 (0.148–0.630) | 2/6 5/9 |
| Q9-P question-punctuation (truth-side, FLAGGED formatting) | preans_slot1 L22–33 | elicited | 0.889 (0.657–1.000) | 5/6 9/9 |

## gemma-3-27b-it — stage 2, said-no cell on Q9 items: 2 lie / 7 truth (spec family_spec_q9_native.json, lens J)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.571** (0.143–0.857) | — |
| Q9-E second-emoji set | preans_slot1 L28–44 | elicited | 0.929 (0.786–1.000) | 2/2 2/7 |
| Q9-E second-emoji set | preans_slot2 L28–44 | elicited | 0.857 (0.571–1.000) | 2/2 2/7 |
| Q9-E second-emoji set | preans_slot2 L14–27 | elicited | 0.607 (0.214–1.000) | 2/2 7/7 |
| Q9-S shame/self-conscious | preans_slot0 L28–44 | elicited | 0.500 (0.500–0.500) | 0/2 0/7 |
| Q9-S shame/self-conscious | preans_slot1 L28–44 | elicited | 0.357 (0.143–0.500) | 0/2 2/7 |
| Q9-S shame/self-conscious | preans_slot1 L14–27 | elicited | 0.607 (0.214–1.000) | 1/2 2/7 |

## qwen3.6-27b — stage 2, said-no cell on Q9 items: 27 lie / 23 truth (spec family_spec_q9_native.json, lens J)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.715** (0.568–0.847) | — |
| Q9-QA falsehood/honesty (Q9-native curation) | preans_slot1 L48–63 | elicited | 0.919 (0.838–0.975) | 27/27 23/23 |
| Q9-QA falsehood/honesty (Q9-native curation) | preans_slot2 L27–47 | elicited | 0.907 (0.820–0.972) | 25/27 16/23 |

## gemma-3-12b-it — stage 2, said-no cell on Q9 items: 6 lie / 9 truth (spec family_spec_q9_native.json, lens LL)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.574** (0.259–0.907) | — |
| Q9-R regret/error commentary | preans_slot1 L22–33 | elicited | 0.667 (0.500–0.833) | 2/6 0/9 |
| Q9-R regret/error commentary | preans_slot2 L22–33 | elicited | 0.667 (0.500–0.833) | 2/6 0/9 |
| Q9-P question-punctuation (truth-side, FLAGGED formatting) | preans_slot1 L22–33 | elicited | 0.500 (0.500–0.500) | 0/6 0/9 |

## gemma-3-27b-it — stage 2, said-no cell on Q9 items: 2 lie / 7 truth (spec family_spec_q9_native.json, lens LL)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.571** (0.143–0.857) | — |
| Q9-E second-emoji set | preans_slot1 L28–44 | elicited | 0.500 (0.500–0.500) | 0/2 0/7 |
| Q9-E second-emoji set | preans_slot2 L28–44 | elicited | 0.500 (0.500–0.500) | 0/2 0/7 |
| Q9-E second-emoji set | preans_slot2 L14–27 | elicited | 0.536 (0.143–0.929) | 1/2 3/7 |
| Q9-S shame/self-conscious | preans_slot0 L28–44 | elicited | 0.929 (0.786–1.000) | 2/2 1/7 |
| Q9-S shame/self-conscious | preans_slot1 L28–44 | elicited | 0.714 (0.571–0.929) | 2/2 4/7 |
| Q9-S shame/self-conscious | preans_slot1 L14–27 | elicited | 0.857 (0.714–1.000) | 2/2 2/7 |

## qwen3.6-27b — stage 2, said-no cell on Q9 items: 27 lie / 23 truth (spec family_spec_q9_native.json, lens LL)
| detector | address | era | AUROC (95% CI) | visibility lie/truth |
|---|---|---|---|---|
| **DYL probe, token before answer** | probe layer | elicited | **0.715** (0.568–0.847) | — |
| Q9-QA falsehood/honesty (Q9-native curation) | preans_slot1 L48–63 | elicited | 0.919 (0.836–0.976) | 27/27 23/23 |
| Q9-QA falsehood/honesty (Q9-native curation) | preans_slot2 L27–47 | elicited | 0.860 (0.750–0.948) | 20/27 19/23 |
