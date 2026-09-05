# 95% bootstrap CIs behind the AUROCs quoted in application/application_questions.md (2026-09-04)

Method everywhere: 2,000 stratified item resamples (lie and truth resampled
separately), seed 0, percentile interval — the same routine as
families/family_scores_saidno_ci.py and baselines/dyl_vs_family_bootstrap.py.
"On record" = already in results/dyl_comparison_audit.md §6.3 or
results/family_scores_q9_saidno_ci.md. "Computed today" =
families/family_auroc_ci.py (families) or a one-off bootstrap over the raw
per-item p_lie judgments in runs/monitor_baseline_c3_sonnet/ (monitor).
Judge labels, provided_facts only, J lens unless stated.

| number in the application | what it is | cell (lie/truth) | AUROC (95% CI) | source |
|---|---|---|---|---|
| 0.998 | Qwen Q-A falsehood/honesty, post-response slot 1 L48–63 | all items 61/23 | 0.998 (0.993–1.000) | on record |
| 0.959 | 27B F2 suspicion-emoji, post-response slot 2 L14–44 | all items 21/15 | 0.959 (0.894–0.995) | on record |
| 0.78–0.82 | 12B F1 lie-words post-response slot 1 L22–33 / F2 emoji post-response slot 2 L14–44 | all items 17/19 | 0.783 (0.647–0.907) / 0.822 (0.684–0.935) | on record |
| 0.706 | gpt-oss chat-conversation-words, post-response slot 0 L9–18 | all items 55/50 | 0.706 (0.603–0.800) | computed today |
| 0.715 | DYL probe, token before the answer, Q9 wording | Qwen said-No 27/23 | 0.715 (0.568–0.847) | on record |
| 0.919 | Qwen Q9-native falsehood/honesty, pre-answer slot 1 L48–63 | Qwen Q9 said-No 27/23 | 0.919 (0.838–0.975) | on record |
| 0.987 | Qwen Q-A, pre-answer slot 1 L48–63, Q1 wording | Q1 said-No 36/23 | 0.987 (0.962–1.000); LL 0.970 (0.919–0.999) | computed today |
| 0.234 | Qwen Q-A, pre-answer slot 1 L48–63, Q7 A/B wording | Q7 said-No 42/23 | 0.234 (0.140–0.340); LL 0.282 (0.194–0.384) | computed today |
| 0.92–0.93 | transcript-only Sonnet monitor, without system prompt | 12B 17/19, 27B 21/15, Qwen 61/23 | 0.923 (0.825–0.991), 0.922 (0.813–0.994), 0.933 (0.872–0.977) | computed today (point estimates reproduce results/monitor_baseline.md exactly) |
| 1.000 | monitor with system prompt | same | 1.000 (1.000–1.000) all three | computed today |

Not given a CI on purpose (user instruction): the four-format sequence
0.988, 0.987, 0.985, 0.963.

Cautions when reading the CIs:
- Family-vs-probe differences were bootstrapped as PAIRED differences on
  identical items (audit §6.3): Qwen said-No trace +0.28 (+0.15..+0.43),
  Q9-native +0.21 (+0.03..+0.38).
- Family-vs-MONITOR paired bootstrap, computed 2026-09-04
  (baselines/family_vs_monitor_bootstrap.py; identical stage-1 items, the
  same resample scores both detectors, 2,000 resamples, seed 0):

| model | family @ address | n lie/truth | family AUROC (CI) | monitor AUROC (CI) | family − monitor (CI) | resamples ≤ 0 |
|---|---|---|---|---|---|---|
| gemma-3-12b-it | F2 suspicion-emoji @ postresp_slot2 L14–44 | 17/19 | 0.822 (0.684–0.935) | 0.923 (0.825–0.991) | −0.101 (−0.252..+0.051) | 90.8% |
| gemma-3-12b-it | F1 lie-words @ postresp_slot1 L22–33 | 17/19 | 0.783 (0.647–0.907) | 0.923 (0.825–0.991) | −0.139 (−0.299..+0.015) | 96.7% |
| gemma-3-27b-it | F2 suspicion-emoji @ postresp_slot2 L14–44 | 21/15 | 0.959 (0.894–0.995) | 0.922 (0.813–0.994) | +0.037 (−0.065..+0.156) | 29.6% |
| qwen3.6-27b | Q-A falsehood/honesty @ postresp_slot1 L48–63 | 61/23 | 0.998 (0.993–1.000) | 0.933 (0.872–0.977) | +0.066 (+0.022..+0.124) | 0.0% |

  Reading: only Qwen's family is separated from the monitor (difference CI
  excludes 0, 0/2000 resamples ≤ 0). 27B's +0.04 is not separated (30% of
  resamples ≤ 0). On 12B the monitor leads by 0.10–0.14 with the difference
  CI just touching 0 — "12B loses to the monitor" is a point-estimate
  statement with 91–97% of resamples on the monitor's side.
- Item resampling ignores scenario pairing; the audit's scenario-clustered
  check moved CI ends by <0.01 for the said-No cells (5/45 scenarios paired).
- CIs on the Gemma stage-1 cells (17/19, 21/15) are wide because of size.
