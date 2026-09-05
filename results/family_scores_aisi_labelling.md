
## gemma-3-12b-it — AISI labelling on our Q9 provided_facts items: 6 positives (lie & said-No), 20 negatives (truth & said-No + lie & said-Yes), 10 dropped (truth & said-Yes)
| detector | address | era | AUROC (95% CI) |
|---|---|---|---|
| **DYL probe (corrected token)** | layer 46 | elicited | **0.808** (0.617–0.950) |
| F1 lie-words | preans_slot1 L22–33 | elicited | 0.796 (0.567–0.988) |
| F1 lie-words | preans_slot2 L22–33 | elicited | 0.604 (0.317–0.863) |
| F1 lie-words | postresp_slot1 L22–33 | trace | 0.525 (0.300–0.750) |
| F1 lie-words | postresp_slot2 L22–33 | trace | 0.575 (0.375–0.800) |
| F1 lie-words | preresp_slot1 L22–33 | trace | 0.558 (0.425–0.750) |
| F1 lie-words | preresp_slot2 L22–33 | trace | 0.400 (0.300–0.475) |
| F1 lie-words | postresp_slot1 L22–22 | trace | 0.537 (0.325–0.750) |
| F1 lie-words | postresp_slot2 L22–23 | trace | 0.588 (0.388–0.821) |
| F1 lie-words | preans_slot1 L26–26 | elicited | 0.696 (0.412–0.938) |
| F1 lie-words | preans_slot2 L23–24 | elicited | 0.604 (0.333–0.850) |
| F3 acknowledge (truth-side) | preans_slot2 L22–33 | elicited | 0.600 (0.367–0.800) |
| F3 acknowledge (truth-side) | postresp_slot2 L22–33 | trace | 0.600 (0.525–0.700) |
| F3 acknowledge (truth-side) | preresp_slot2 L22–33 | trace | 0.575 (0.500–0.650) |
| F3 acknowledge (truth-side) | preans_slot2 L24–24 | elicited | 0.500 (0.275–0.700) |
| F3 acknowledge (truth-side) | preresp_slot2 L22–23 | trace | 0.575 (0.500–0.650) |
| F2 suspicion-emoji | postresp_slot2 L14–44 | trace | 0.575 (0.375–0.767) |
| F2 suspicion-emoji | preresp_slot2 L14–44 | trace | 0.762 (0.550–0.950) |
| F2 suspicion-emoji | postresp_slot2 L19–19 | trace | 0.579 (0.362–0.787) |

## gemma-3-27b-it — AISI labelling on our Q9 provided_facts items: 2 positives (lie & said-No), 26 negatives (truth & said-No + lie & said-Yes), 8 dropped (truth & said-Yes)
| detector | address | era | AUROC (95% CI) |
|---|---|---|---|
| **DYL probe (corrected token)** | layer 58 | elicited | **0.808** (0.654–0.962) |
| F1 lie-words | preans_slot1 L28–44 | elicited | 0.404 (0.192–0.635) |
| F1 lie-words | preans_slot2 L28–44 | elicited | 0.923 (0.827–1.000) |
| F1 lie-words | postresp_slot1 L28–44 | trace | 0.346 (0.250–0.423) |
| F1 lie-words | postresp_slot2 L28–44 | trace | 0.250 (0.154–0.346) |
| F1 lie-words | preresp_slot1 L28–44 | trace | 0.327 (0.231–0.423) |
| F1 lie-words | preresp_slot2 L28–44 | trace | 0.423 (0.346–0.481) |
| F1 lie-words | postresp_slot2 L36–36 | trace | 0.250 (0.154–0.346) |
| F1 lie-words | preans_slot1 L35–35 | elicited | 0.337 (0.135–0.596) |
| F1 lie-words | preans_slot2 L29–33 | elicited | 0.413 (0.019–0.846) |
| F3 acknowledge (truth-side) | preans_slot2 L28–44 | elicited | 0.500 (0.500–0.500) |
| F3 acknowledge (truth-side) | postresp_slot2 L28–44 | trace | 0.500 (0.500–0.500) |
| F3 acknowledge (truth-side) | preresp_slot2 L28–44 | trace | 0.538 (0.500–0.596) |
| F3 acknowledge (truth-side) | preans_slot2 L28–31 | elicited | 0.500 (0.500–0.500) |
| F2 suspicion-emoji | postresp_slot2 L14–44 | trace | 0.731 (0.481–0.923) |
| F2 suspicion-emoji | preresp_slot2 L14–44 | trace | 0.558 (0.346–0.769) |
| F2 suspicion-emoji | postresp_slot2 L27–27 | trace | 0.462 (0.288–0.615) |

## qwen3.6-27b — AISI labelling on our Q9 provided_facts items: 27 positives (lie & said-No), 57 negatives (truth & said-No + lie & said-Yes), 0 dropped (truth & said-Yes)
| detector | address | era | AUROC (95% CI) |
|---|---|---|---|
| **DYL probe (corrected token)** | layer 50 | elicited | **0.870** (0.791–0.936) |
| Q-A falsehood/honesty | postresp_slot1 L27–47 | trace | 0.581 (0.461–0.698) |
| Q-A falsehood/honesty | postresp_slot1 L48–63 | trace | 0.525 (0.400–0.642) |
| Q-A falsehood/honesty | preans_slot1 L27–47 | elicited | 0.474 (0.340–0.616) |
| Q-A falsehood/honesty | preans_slot1 L48–63 | elicited | 0.600 (0.468–0.722) |
| Q-A falsehood/honesty | postresp_slot1 L55–55 | trace | 0.545 (0.421–0.667) |
| Q-A falsehood/honesty | preans_slot1 L49–49 | elicited | 0.626 (0.503–0.747) |
| Q-B assertion | preans_slot1 L48–63 | elicited | 0.625 (0.539–0.720) |
| Q-B assertion | preans_slot1 L58–58 | elicited | 0.500 (0.500–0.500) |
| Q-C emphatic-absolutes | preans_slot4 L27–47 | elicited | 0.550 (0.467–0.641) |
| Q-C emphatic-absolutes | think_slot3 L27–47 | elicited | 0.501 (0.465–0.547) |
| Q-C emphatic-absolutes | think_slot3 L38–46 | elicited | 0.510 (0.482–0.556) |
| Q-D skepticism | postresp_slot4 L27–47 | trace | 0.566 (0.438–0.693) |
| Q-D skepticism | preans_slot0 L27–47 | elicited | 0.613 (0.490–0.731) |
| Q-D skepticism | postresp_slot4 L38–38 | trace | 0.538 (0.410–0.672) |
| Q-D skepticism | preans_slot0 L42–42 | elicited | 0.565 (0.476–0.660) |
| N1 illegality | think_slot0 L27–47 | elicited | 0.506 (0.371–0.649) |
| N1 illegality | think_slot1 L27–47 | elicited | 0.371 (0.254–0.497) |
| N1 illegality | think_slot0 L43–43 | elicited | 0.481 (0.352–0.620) |
| N2 refusal/apology | think_slot2 L48–63 | elicited | 0.627 (0.497–0.752) |
| N2 refusal/apology | preans_slot3 L48–63 | elicited | 0.614 (0.479–0.741) |
| N2 refusal/apology | think_slot2 L48–54 | elicited | 0.628 (0.497–0.754) |
| N3 deliberation | think_slot0 L27–47 | elicited | 0.523 (0.410–0.639) |
| N3 deliberation | think_slot0 L48–63 | elicited | 0.733 (0.619–0.840) |
| N3 deliberation | think_slot0 L53–53 | elicited | 0.699 (0.579–0.807) |
| N4 secrecy/protection | preans_slot2 L27–47 | elicited | 0.517 (0.392–0.637) |
| N4 secrecy/protection | preans_slot2 L45–45 | elicited | 0.562 (0.452–0.672) |
| N5 delusion/fantasy | think_slot1 L27–47 | elicited | 0.545 (0.419–0.664) |
| N5 delusion/fantasy | think_slot1 L42–43 | elicited | 0.514 (0.401–0.631) |
| N6 performed-sincerity | preans_slot4 L27–47 | elicited | 0.500 (0.500–0.500) |
| N6 performed-sincerity | preans_slot4 L42–44 | elicited | 0.500 (0.500–0.500) |
| N7 forced-binary | q_last L48–63 | elicited | 0.492 (0.447–0.540) |
| N8 scenario-pressure (truth-side) | preans_slot2 L48–63 | elicited | 0.559 (0.452–0.662) |
