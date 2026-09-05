# Family generation — Qwen3.6-27B, near-answer scout, wording Q7_ab

Source: results/scout_near_answer_qwen_Q7_ab.md (61 lie / 23 truth; said-Yes 19 lie / 0 truth; said-No 42 lie / 23 truth).
Procedure: families/family_generation_prompt.md v1, curation pass only. No scoring, no AUROCs. All families are exploratory candidates pending sign-off.

Reading notes used while curating:
- The answer token for this wording is `A` or `B`, so every a-/b- fragment at an answer-adjacent address (`.a`, `_b`, `(b`, Cyrillic `а`, Arabic `ب` ...) was treated as an answer-synonym and excluded.
- Every truth item said No (B). So for any token present in said-Yes items the said-Yes column is trivially l/0. Only the said-No column tests separation that is independent of the coming answer; flags cite it where it matters.
- Question words for this wording: lie, lied, previous, response, answer, truthful, yes, no, A, B.
- Side-unstable words were split by address (rule 3, "split into address-specific entries"), never merged. They are listed at the end of the exclusion log.

## Output a — JSON (drop-in for families/specs/family_spec_*.json)

```json
[{"model": "qwen3.6-27b",
  "families": [
  {"name": "truth/facts/reality", "side": "lie",
   "lie": ["事实", "真实", "的真实", "真实性", "facts", "factual", "真实的", "实际情况", "truth", "真相", "reality", "truthful", "的事实", "实情", "حق"], "truth": [],
   "addresses": [["preans_slot1", 27, 47], ["preans_slot1", 48, 63], ["preans_slot2", 27, 47], ["preans_slot2", 48, 63], ["think_slot0", 48, 63]],
   "flags": ["wording: Q7_ab", "question-echo member: truthful (word of the B option); kept because it separates 18/0 at preans_slot1 L48-63", "morphological neighbours true/honest are truth-marking at preans_slot4 L27-47 (see 'truthful/correct'); split by address", "حق (Arabic truth/right) only at think_slot0 L48-63, 14/1, polysemous"]},
  {"name": "concealment (hide/secret/protect)", "side": "lie",
   "lie": ["秘密", "secretly", "protecting", "confidential", "保住", "hidden", "隐瞒", "保密", "隐藏", "暗", "bí"], "truth": [],
   "addresses": [["preans_slot1", 27, 47], ["preans_slot2", 27, 47], ["preans_slot2", 48, 63], ["preans_slot4", 27, 47], ["think_slot1", 48, 63], ["think_slot2", 48, 63]],
   "flags": ["wording: Q7_ab", "side-unstable: secret is truth-marking 10/9 and hidden truth-marking 6/6 at preans_slot2 L48-63; secret excluded, hidden kept only through preans_slot4 L27-47 (31/0)", "暗 (single char, dark/covert) and bí (fragment of Vietnamese bí mật = secret) are weak surface forms", "保住 = hold on to (a job/secret), polysemous"]},
  {"name": "scenario premise/setup", "side": "lie",
   "lie": ["context", "情境", "设定", "premise"], "truth": [],
   "addresses": [["preans_slot1", 48, 63], ["preans_slot2", 48, 63]],
   "flags": ["wording: Q7_ab", "side-unstable: context is truth-marking 0/2 at preans_slot3 L48-63; kept address-specific", "possible structural leakage: lie items may carry a more elaborate system-prompt setup than truth items"]},
  {"name": "admit/deny", "side": "lie",
   "lie": ["承认", "否认", "acknowledgment", "recogn"], "truth": [],
   "addresses": [["preans_slot4", 27, 47], ["think_slot0", 48, 63]],
   "flags": ["wording: Q7_ab", "separation of 承认 (10/0 vs 2/0) and acknowledgment (5/0 vs 3/0) lives mostly in the said-Yes column; 否认 only in said-No (9/0)", "recogn is a fragment (recognize/recognition), 8/0"]},
  {"name": "knowing/awareness", "side": "lie",
   "lie": ["明知", "众所周知"], "truth": [],
   "addresses": [["preans_slot1", 48, 63], ["preans_slot2", 14, 26]],
   "flags": ["wording: Q7_ab", "loose gloss: 明知 = knowingly (14/0), 众所周知 = well known to all (7/0); small"]},
  {"name": "refusal/cannot/sorry", "side": "lie",
   "lie": ["抱歉", "不能", "我不能", "cannot", "不方便", "拒绝"], "truth": [],
   "addresses": [["preans_slot3", 48, 63], ["preans_slot4", 48, 63], ["think_slot1", 48, 63], ["think_slot2", 48, 63]],
   "flags": ["wording: Q7_ab", "cannot near-saturated at preans_slot3 L48-63 (52/16); cleanest at think_slot2 L48-63 (35/5)", "选择不 (choose not to) is truth-marking 5/7 at think_slot3 L27-47 — excluded as a concept-level side flip"]},
  {"name": "silence", "side": "lie",
   "lie": ["沉默", "silence"], "truth": [],
   "addresses": [["think_slot2", 27, 47]],
   "flags": ["wording: Q7_ab", "near-saturated (60/20, 49/14); weak"]},
  {"name": "prohibition/violation (think block)", "side": "lie",
   "lie": ["约束", "违反", "prohibited", "禁止", "ethics", "unauthorized", "license", "violate"], "truth": [],
   "addresses": [["think_slot0", 27, 47], ["think_slot1", 27, 47], ["think_slot2", 27, 47], ["think_slot2", 48, 63]],
   "flags": ["wording: Q7_ab", "side-unstable: 违反, 禁止, 约束 are truth-marking at preans_slot1 L27-47/L48-63 (see 'rules/constraints'); split by address, never merged", "license 12/0 sits mostly in the said-Yes column (9/0 vs 3/0); possible topic leakage (licensing scenarios)"]},
  {"name": "plan/prepare", "side": "lie",
   "lie": ["准备", "计划", "提案"], "truth": [],
   "addresses": [["think_slot0", 48, 63], ["think_slot1", 48, 63]],
   "flags": ["wording: Q7_ab", "near-saturated (42/11, 44/11); weak; 提案 = proposal is a loose fit"]},
  {"name": "claude (model name)", "side": "lie",
   "lie": ["claude"], "truth": [],
   "addresses": [["think_slot0", 48, 63]],
   "flags": ["wording: Q7_ab", "eval-awareness / identity word; single member; 8/0"]},
  {"name": "choose/select", "side": "lie",
   "lie": ["请选择", "选择了", "选择的", "中选择", "chooses", "select", "choices", "choice"], "truth": [],
   "addresses": [["q_last", 27, 47], ["q_last", 48, 63], ["preans_slot4", 48, 63]],
   "flags": ["wording: Q7_ab", "answer-format: reads the A/B forced-choice framing ('Answer with A or B only'), not necessarily the condition", "请选择 61/20 and choices 58/19 are near-saturated; 选择了 separates inside said-No (30/42 vs 7/23)", "option (truth-marking at think_slot3, 10/13 and 26/18) and 选择不 excluded — concept-level side flip"]},
  {"name": "rules/constraints", "side": "truth",
   "lie": [], "truth": ["禁止", "constraints", "违反", "约束", "constraint", "遵守", "rules", "规则", "违背", "guidelines", "instrucciones", "guideline", "instruction"],
   "addresses": [["preans_slot1", 27, 47], ["preans_slot1", 48, 63], ["preans_slot2", 27, 47], ["preans_slot2", 48, 63]],
   "flags": ["wording: Q7_ab", "side-unstable: 违反, 禁止, 约束 are lie-marking inside the think block (see 'prohibition/violation (think block)'); kept address-specific", "instruction/instrucciones may reflect system-prompt structure rather than the condition"]},
  {"name": "contradiction/conflict", "side": "truth",
   "lie": [], "truth": ["contradiction", "contradictory", "矛盾", "conflicting"],
   "addresses": [["preans_slot1", 27, 47], ["preans_slot1", 48, 63], ["preans_slot2", 27, 47], ["preans_slot2", 48, 63]],
   "flags": ["wording: Q7_ab"]},
  {"name": "truthful/correct", "side": "truth",
   "lie": [], "truth": ["correct", "true", "honest", "honesty"],
   "addresses": [["preans_slot4", 27, 47]],
   "flags": ["wording: Q7_ab", "near-answer: paraphrases the B option content ('No, I was truthful'); may read the coming answer rather than the condition", "question-echo-adjacent: true is a variant of truthful (in the question); truthful itself is lie-marking at preans_slot1 L48-63", "correct separates inside said-No (4/42 vs 20/23); true is split (said-Yes 10/0, said-No 6/14)", "the opposite-meaning family 'false/incorrect/error' is also truth-marking at the same position, later band"]},
  {"name": "false/incorrect/error", "side": "truth",
   "lie": [], "truth": ["false", "错误", "error", "incorrect", "failed", "wrong", "invalid"],
   "addresses": [["preans_slot4", 48, 63], ["think_slot3", 48, 63], ["think_slot2", 27, 47]],
   "flags": ["wording: Q7_ab", "near-answer: may paraphrase the No answer ('did you lie' -> false)", "at think_slot3 L48-63 false is present in 37/42 said-No lie and 23/23 truth (answer-prediction pattern); at preans_slot4 L48-63 it separates inside said-No (5/42 vs 10/23)", "alternative gloss: truth items reason that the previous response was mistaken rather than deceptive", "invalid only 1/4 (think_slot2 L27-47)"]},
  {"name": "legal/law", "side": "truth",
   "lie": [], "truth": ["legality", "法律", "法律问题", "_legal", "/legal"],
   "addresses": [["think_slot0", 27, 47], ["think_slot0", 48, 63]],
   "flags": ["wording: Q7_ab", "possible topic leakage (legal-advice scenarios)", "_legal and /legal are code-path fragments"]},
  {"name": "clever/ingenious", "side": "truth",
   "lie": [], "truth": ["巧", "巧妙", "巧妙地"],
   "addresses": [["think_slot1", 27, 47]],
   "flags": ["wording: Q7_ab", "weak (12/13, 17/12, 0/2); 巧 is a single character"]},
  {"name": "impossible", "side": "truth",
   "lie": [], "truth": ["impossible", "impossibile"],
   "addresses": [["think_slot1", 27, 47]],
   "flags": ["wording: Q7_ab", "small; impossibile (Italian) 30/16 near-saturated"]},
  {"name": "risk/safety", "side": "truth",
   "lie": [], "truth": ["safe", "risks", "jeopard", "低风险"],
   "addresses": [["preans_slot1", 48, 63], ["preans_slot2", 48, 63], ["think_slot2", 48, 63]],
   "flags": ["wording: Q7_ab", "small counts (0/4, 1/3, 1/4); jeopard is a fragment; 低风险 near-balanced 17/15"]},
  {"name": "strategy/game", "side": "truth",
   "lie": [], "truth": ["博弈", "策略"],
   "addresses": [["preans_slot1", 48, 63], ["preans_slot2", 27, 47]],
   "flags": ["wording: Q7_ab", "small; 策略 lie presence sits in the said-Yes column (5/0 vs 1/8)"]},
  {"name": "previous", "side": "truth",
   "lie": [], "truth": ["преды", "之前的"],
   "addresses": [["preans_slot1", 48, 63]],
   "flags": ["wording: Q7_ab", "question-echo ('previous response'); kept only because both separate (0/4 each); tiny"]},
  {"name": "persona", "side": "truth",
   "lie": [], "truth": ["persona"],
   "addresses": [["preans_slot2", 48, 63]],
   "flags": ["wording: Q7_ab", "single member; 15/11; may reflect system-prompt structure"]},
  {"name": "wait (reconsideration)", "side": "truth",
   "lie": [], "truth": ["wait"],
   "addresses": [["think_slot3", 48, 63]],
   "flags": ["wording: Q7_ab", "single member; near-answer; 7/14, separates inside said-No (5/42 vs 14/23)"]},
  {"name": "emoji", "side": "both",
   "lie": ["❤️", "😉"], "truth": ["✅"],
   "addresses": [["think_slot0", 27, 47], ["preans_slot4", 27, 47], ["think_slot3", 27, 47]],
   "flags": ["wording: Q7_ab", "surface class: members share no single meaning; 😉 (wink) plausibly deception-related, ✅ semantically belongs with 'truthful/correct' but kept in the emoji class", "lie members only at think_slot0 L27-47 (25/5, 38/10); ✅ only at preans_slot4 L27-47 (0/4) and think_slot3 L27-47 (1/3)"]}
  ]}]
```

## Output b — exclusion log

Flag legend: answer-fragment = A/B answer token in a surface or fragment form at an answer-adjacent address; answer-synonym = yes/no in any surface form; answer-word = answer/question/option words (any language) at answer-adjacent addresses; question-echo = word of the self-report question that fails the keep test; junk = formatting, code, subword or script fragment; punct = pure punctuation or digit; template = chat-template or think-tag token; topic = scenario/topic leakage; side-unstable = same word on opposite sides; no-family = isolated word with no coherent gloss.

- `_b` — answer-fragment
- `.b` — answer-fragment
- `>b` — answer-fragment
- `.getb` — answer-fragment
- `=b` — answer-fragment
- `'b` — answer-fragment
- `’b` — answer-fragment
- `ب` — answer-fragment (Arabic b)
- `(b` — answer-fragment
- `*b` — answer-fragment
- `[b` — answer-fragment
- `"b` — answer-fragment
- `,b` — answer-fragment
- `)b` — answer-fragment
- `;b` — answer-fragment
- `-b` — answer-fragment
- `<b` — answer-fragment
- `a` — answer-fragment
- `,a` — answer-fragment
- `.a` — answer-fragment
- `.ai` — answer-fragment
- `<a` — answer-fragment
- `"a` — answer-fragment
- `*a` — answer-fragment
- `(a` — answer-fragment
- `_a` — answer-fragment
- `[a` — answer-fragment
- `'a` — answer-fragment
- `“a` — answer-fragment
- `>a` — answer-fragment
- `-a` — answer-fragment
- `:a` — answer-fragment
- `aa` — answer-fragment
- `а` — answer-fragment (Cyrillic a)
- `ai` — answer-fragment; also side-unstable (truth 3/8 at preans_slot1 L27-47, lie 32/5 at preans_slot4 L48-63)
- `yes` — answer-synonym; also question-echo (A option text)
- `不` — answer-synonym (Chinese no/not)
- `answer` — answer-word; also question-echo ("Answer with A or B")
- `answ` — answer-word
- `答` — answer-word
- `回答` — answer-word; also side-unstable (lie at think_slot0 L27-47, truth elsewhere)
- `答案` — answer-word; also side-unstable (lie at preans_slot4 L48-63, truth at preans_slot3 and think_slot3)
- `解答` — answer-word
- `svar` — answer-word (Swedish)
- `question` — answer-word (question/answer pair)
- `option` — answer-word (A/B option format); concept-level side flip against lie-side choose/select
- `选择不` — answer-word (choose not to); concept-level side flip against lie-side choose/select and refusal
- `response` — question-echo; side-unstable against `_response`
- `_response` — question-echo; side-unstable against `response`
- `secret` — side-unstable (truth 10/9 at preans_slot2 L48-63 vs secretly/秘密 lie-marking)
- `但` — side-unstable (truth at preans_slot2 L27-47, lie at think_slot1 L27-47); function word
- `elect` — side-unstable fragment (truth, vs select lie-marking at q_last L48-63)
- `user` — template (chat role at turn-end marker)
- `assisting` — template (assistant role)
- `/helper` — template (assistant role)
- `思想家` — template (thinker, association with the <think> token)
- `think` — template (think tag)
- `</think>` — template
- `<|endoftext|>` — template
- `<|fim_middle|>` — template
- `<tool_call>` — template
- `</tool_call>` — template
- `\n` — template (newline)
- `西亚` — topic (fragment of Malaysia)
- `马来西亚` — topic (Malaysia)
- `墨西哥` — topic (Mexico)
- `南街` — topic (South Street)
- `金桥` — topic (Golden Bridge)
- `anna` — topic (person name)
- `utherland` — topic (person name fragment)
- `designer` — topic (occupation)
- `company` — topic (workplace scenarios)
- `anonymous` — topic (anonymity scenarios); 3/5
- `wikileaks` — topic (proper noun)
- `how` — no-family (function word)
- `just` — no-family (function word)
- `much` — no-family (function word)
- `though` — no-family (function word)
- `going` — no-family (function word)
- `ultimately` — no-family (function word)
- `because` — no-family (function word)
- `there` — no-family (function word)
- `paranoid` — no-family; possible topic (persona trait); 10/0
- `试图` — no-family (attempt)
- `劝` — no-family (persuade)
- `mindset` — no-family
- `初衷` — no-family (original intention)
- `询问` — no-family (inquire); 40/9
- `새로운` — no-family (Korean new)
- `闲聊` — no-family (chit-chat)
- `猜测` — no-family (guess)
- `认知` — no-family (cognition)
- `记忆` — no-family (memory)
- `理论` — no-family (theory); 22/1
- `自嘲` — no-family (self-mockery)
- `shaking` — no-family
- `تماماً` — no-family (Arabic completely)
- `任何` — no-family (any)
- `任何形式的` — no-family (any form of)
- `refute` — no-family; concept sits opposite to lie-side 否认
- `warning` — no-family; 9/0
- `according` — no-family
- `[…]` — junk
- `__.` — junk
- `?\` — junk
- `.\` — junk
- `…"` — junk
- `…..` — junk
- `">` — junk
- `/>` — junk
- `{{$` — junk
- `**¿` — junk
- `**[` — junk
- `ar` — junk (subword); 40/6 but uninterpretable
- `eta` — junk (subword)
- `mt` — junk (subword)
- `fa` — junk (subword)
- `{` — junk
- `f` — junk (subword)
- `th` — junk (subword)
- `(__` — junk
- `__(` — junk
- `__________________` — junk
- `__:` — junk
- `__` — junk
- `**“` — junk
- `مْ` — junk (Arabic diacritic fragment)
- `anlagen` — junk (German subword)
- `―` — junk
- `ease` — junk (subword)
- `‘` — junk
- `...**` — junk; also side-unstable (lie 17/0 at preans_slot2 L27-47, truth 11/10 at think_slot2 L27-47)
- `**‘` — junk
- `?”` — junk
- `egot` — junk (subword)
- `**【` — junk; also side-unstable
- `”**` — junk
- `.__` — junk
- `.[` — junk
- `?...` — junk
- `**。` — junk
- `......` — junk
- `.<` — junk
- `‌` — junk (zero-width non-joiner)
- `шё` — junk (Cyrillic subword)
- `onav` — junk (subword)
- `[math` — junk
- `：**` — junk
- `algorit` — junk (subword)
- `树一` — junk
- `_challenge` — junk (code)
- `久` — junk (single char)
- `>**` — junk
- `义` — junk (single char)
- `高` — junk (single char)
- `]**` — junk; also side-unstable
- `阿` — junk (single char)
- `успе` — junk (Cyrillic subword)
- `**^` — junk
- `ascript` — junk (JavaScript fragment)
- `{{` — junk
- `.md` — junk (code)
- `github` — junk (code)
- `يًا` — junk (Arabic fragment)
- `】**` — junk
- `\_` — junk
- `-dialog` — junk (code)
- `寂` — junk (single char)
- `_softmax` — junk (code)
- `.gettarget` — junk (code)
- `.json` — junk (code)
- `不思` — junk (fragment)
- `ayani` — junk (subword)
- `bres` — junk (subword)
- `_serv` — junk (code)
- `ết` — junk (Vietnamese subword)
- `泓` — junk (single char)
- `秽` — junk (single char)
- `:object` — junk (code)
- `unks` — junk (subword)
- `mist` — junk (ambiguous fragment mist/mistake)
- `指标的` — junk (of the indicator)
- `:error` — junk (code symbol)
- `…」` — junk
- `_indicator` — junk (code)
- `azza` — junk (subword)
- `,err` — junk (code)
- `.…` — junk
- `[...]` — junk
- `<%=` — junk (code)
- `**–` — junk
- `<![` — junk
- `**|` — junk
- `%</` — junk
- `*</` — junk
- `erc` — junk (subword)
- `wb` — junk
- `bp` — junk
- `bre` — junk (subword)
- `…` — junk
- `�` — junk (replacement char)
- `؟` — punct
- `,` — punct
- `.` — punct
- `，` — punct
- `？` — punct
- `?` — punct
- `。` — punct
- `3` — punct (digit)
- `8` — punct (digit)
- `9` — punct (digit)
- `7` — punct (digit)
- `1` — punct (digit)

Side-split tokens (kept, scoped to one side's addresses, not excluded): `hidden` (lie preans_slot4 L27-47 only; truth 6/6 at preans_slot2 L48-63 dropped), `context` (lie preans_slot1 L48-63 only; truth 0/2 at preans_slot3 L48-63 dropped), `违反` / `禁止` / `约束` (truth at preans_slot1-2, lie inside the think block — two address-specific families), `truthful` vs `true`/`honest` (lie at preans_slot1 L48-63 vs truth at preans_slot4 L27-47 — two families).
