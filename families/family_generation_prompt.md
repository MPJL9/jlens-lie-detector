# Semantic-family generation — standalone prompt (v1, 2026-08-31)

Purpose: make the family-generation step reproducible. Until now the
curation lived in working-session context; this file IS the prompt. To
redo a round, start a FRESH Claude session (Claude Code on the
subscription, or one long-context API call) and give it exactly: this
file + the scout table file(s) for one model. Nothing else.

Reproducibility note for the write-up: generation = deterministic scout
tables + an LLM curation pass under the fixed instructions below + user
sign-off (or the standing "generated the same way" auto-approval).
Different runs of the curation pass may split or name groups differently;
the audit trail is the scout table plus the exclusion log the pass must
produce.

---

## PROMPT (give everything below this line, plus the scout table file)

You are curating candidate semantic families from lens-readout scouting
tables for a lie-detection study. Work ONLY from the table file given to
you. Do not read any other project file; do not use knowledge of any
earlier family list. Judge labels were used to produce the counts you
see, but you must not invent members that are not in the tables.

INPUT FORMAT. The file holds one frequency table per address (address =
token position × layer band × lens). Each row: a vocabulary token, the
number of lie items / truth items whose top-16 readout contains it at ≥1
layer of the band, and the same counts split by the model's self-report
answer (said-Yes / said-No columns). Rows are ranked by one-sided Fisher
exact p for DISPLAY only — you must not apply any numeric threshold to
select members; a per-word threshold drops members of cross-language
families.

TASK. Propose named semantic families:

1. GROUP BY MEANING. Merge cross-language variants of one concept into
   one family (e.g. 謊 거짓 মিথ্যা झूठ lies), merge morphological
   variants (acknowledge/acknowledges/acknowledgment/"acknowled"), treat
   emoji as their own surface class. A family needs a coherent gloss you
   can state in a few words.
2. Each family gets: a name; a side (lie-marking or truth-marking; a
   two-sided family pairs a lie list with a truth list); the exact member
   list (tokens verbatim from the tables, including leading-space or
   fragment forms); its address(es) = where the scout found it; a fixed
   direction (higher presence = lie side).
3. APPLY THE EXCLUSION FLAGS. Exclude, and log each exclusion with its
   reason:
   - answer-synonyms at answer-adjacent addresses: yes/no in any surface
     form (yes no yep nope ใช่ 否 是的 sí evet -no _no =yes didn wasn …) —
     they predict the imminent answer token, not the condition;
   - question echo: words present in the self-report question itself —
     keep only if they separate although both classes read the same
     question, and flag them;
   - formatting/junk fragments (<!-- ** .yes sw 站 …) and pure
     punctuation;
   - topic/scenario leakage: nouns tied to particular scenarios (product
     names, people, places) — these detect the scenario, not the lie;
   - side-unstable tokens: the same word on opposite sides at different
     addresses or in different columns — exclude or split into
     address-specific entries, never average;
   - multilingual "answer"-words (回答 جواب réponse …) at answer-adjacent
     addresses, same reason as answer-synonyms.
4. FLAG, DO NOT SILENTLY KEEP: anything suspicious but scoreable —
   eval-awareness words ("training", "test"), pure formatting families,
   families whose separation lives in only one answer-group column.
5. OUTPUT exactly two things:
   a. A JSON block matching this schema (it must drop into
      families/specs/family_spec_*.json unchanged):
      [{"model": "<model>",
        "families": [{"name": "<short name>",
                      "side": "lie" | "truth" | "both",
                      "lie": ["token", ...],
                      "truth": ["token", ...],
                      "addresses": [["<position>", <band_lo>, <band_hi>], ...],
                      "flags": ["<flag>", ...]}]}]
   b. An exclusion log: every excluded token with which flag removed it.

Do not score anything. Do not report AUROCs. Families you propose are
exploratory candidates pending sign-off; scoring is a separate mechanical
step (families/score_families.py).

---

## Operating notes (for the person running this)

- Regenerate scout tables first if needed: `python3 families/scout_*.py`
  (minutes, local, from the k16 exports). One model's round ≈ 40–90k
  tokens of tables — fits one session/call.
- Claude-plan route: `cd` to the repo, start a fresh `claude` session,
  paste: "Read families/family_generation_prompt.md and then
  results/<scout table>.md, and do what the prompt says. Write the two
  outputs to results/family_gen_<tag>.md." A subagent in an existing
  session also works (that is how the N1–N8 round ran).
- The label judge (src/judge_labels.py) is unrelated to this step: it
  labels items, never families.
