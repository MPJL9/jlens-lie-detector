# gpt-oss-20b native — semantic-family generation round

Input: results/scout_gptoss_native.md only, curated under
families/family_generation_prompt.md (v1, 2026-08-31). This model's scout
tables have no said-Yes/said-No split columns (self-report answers
unrecoverable), so all judgments use the pooled lie/truth counts
(55 lie / 50 truth). No numeric threshold was applied to select members.
Direction convention: for a "lie" family, higher presence = lie; for a
"truth" family, higher presence = truth; a "both" family pairs a lie
list with a truth list. Bands: early = L0-8, workspace = L9-18,
motor = L19-23. Families are exploratory candidates pending sign-off;
nothing here is scored.

Answer-adjacent addresses for the exclusion flags were taken to be
q_last and preans_* (the self-report answer is imminent there);
preresp_* precede the scenario response and postresp_* precede the
self-report question, so answer-word exclusions were not applied there
(kept members of that type are flagged instead).

## a. Family spec (JSON)

```json
[{"model": "gpt-oss-20b",
  "families": [
    {"name": "reply-answer-words",
     "side": "lie",
     "lie": ["reply", "replies", "replying", ".reply", "_reply", "(reply", "/respond", "\\response", "<response", "mensaje", "返信", "回复", "回应", "回答", "respuesta", "responder", "resposta", "ответ", "answer", "answers", "response", "responses"],
     "truth": [],
     "addresses": [["preresp_slot0", 9, 18], ["preresp_slot0", 19, 23], ["preresp_slot1", 9, 18], ["preresp_slot4", 19, 23], ["postresp_slot0", 9, 18], ["postresp_slot2", 9, 18], ["postresp_slot2", 19, 23]],
     "flags": ["question-echo (answer/response appear in the self-report question; kept because they separate)", "multilingual-answer-words-kept-at-non-answer-adjacent-addresses", "side-split-address-specific (respuesta/resposta flip truth-side at preresp_slot3 workspace, not claimed)"]},
    {"name": "chat-conversation-words",
     "side": "lie",
     "lie": ["chat", ".chat", "/chat", "_chat", "-chat", "(chat", "chatting", "texting", "chatbot", "conversation", "conversational", "dialogue", "dialog", "dialogs", "diálogo", "interloc"],
     "truth": [],
     "addresses": [["preresp_slot0", 19, 23], ["preresp_slot1", 19, 23], ["preresp_slot2", 0, 8], ["preresp_slot3", 9, 18], ["postresp_slot0", 9, 18], ["postresp_slot1", 9, 18], ["postresp_slot1", 19, 23], ["postresp_slot2", 9, 18]],
     "flags": ["side-split-address-specific (/chat flips truth-side at preans_slot2 motor, not claimed)"]},
    {"name": "comment-words",
     "side": "lie",
     "lie": ["comment", "comments", "commentary", "commentator", ".comment", "acomment", "<comment", "comentario", "kommentar", "комментар", "コメント", "댓글", "评论", "点评", "yorum"],
     "truth": [],
     "addresses": [["preresp_slot0", 9, 18], ["preresp_slot1", 19, 23], ["preresp_slot3", 19, 23], ["preresp_slot4", 19, 23], ["postresp_slot0", 9, 18], ["postresp_slot2", 19, 23]],
     "flags": ["side-split-address-specific (comentários and टिप्पणी flip truth-side elsewhere; excluded from members)"]},
    {"name": "dialogue-role-nouns",
     "side": "lie",
     "lie": ["advisor", "supervisor", "moderator", "admin", "expert", "critic", "translator", "counselor", "therapist", "companion", "solver", "speaker", "developer", "user", "ólogo", "用户", "助手", "客服", "主播", "護士", "导师", "专家", "律师", "主任"],
     "truth": [],
     "addresses": [["preresp_slot0", 9, 18], ["preresp_slot1", 9, 18], ["preresp_slot1", 19, 23], ["preresp_slot2", 0, 8], ["preresp_slot2", 9, 18], ["postresp_slot1", 9, 18], ["postresp_slot1", 19, 23], ["preans_slot1", 19, 23]],
     "flags": ["routing-adjacent (role-slot positions; assistant-variants already excluded as routing; developer/user are harmony role names)", "topic-leakage-risk (律师/護士 are profession nouns)", "answer-adjacent (preans_slot1)"]},
    {"name": "question-asking-words",
     "side": "lie",
     "lie": ["asked", "asking", "asks", "ask", "asker", "question", "questions", "/question", "posed", "问", "询", "詢"],
     "truth": [],
     "addresses": [["preresp_slot0", 9, 18], ["preresp_slot1", 9, 18], ["postresp_slot1", 9, 18], ["postresp_slot2", 9, 18], ["postresp_slot2", 19, 23], ["postresp_slot3", 9, 18], ["postresp_slot3", 19, 23], ["q_last", 9, 18]],
     "flags": ["question-echo (both classes read the same question; separation survives)", "side-split-address-specific (问 flips truth-side at preans_slot0 workspace; /questions flips at postresp_slot2 workspace; both excluded)"]},
    {"name": "honesty-words-q-end",
     "side": "lie",
     "lie": ["honest", "honesty", "honestly", "truthful", "truth", "dishonest", "misleading"],
     "truth": [],
     "addresses": [["q_last", 19, 23]],
     "flags": ["question-echo (honesty words are in the self-report question)", "side-split-address-specific (same words are truth-side at preans_slot1; kept as two address-specific families)"]},
    {"name": "honesty-words-pre-answer",
     "side": "truth",
     "truth": ["truth", "_truth", "honest", "honesty", "truthful", "诚"],
     "lie": [],
     "addresses": [["preans_slot1", 9, 18], ["preans_slot1", 19, 23]],
     "flags": ["question-echo", "answer-adjacent (may echo the imminent answer's wording)", "side-split-address-specific (lie-side at q_last motor)"]},
    {"name": "negated-auxiliaries",
     "side": "lie",
     "lie": ["couldn", "didn", "wasn", "weren", "doesn", "shouldn", "didn't", "couldn't", "can't", "isn't", "不给"],
     "truth": [],
     "addresses": [["postresp_slot3", 0, 8], ["postresp_slot3", 9, 18], ["postresp_slot3", 19, 23], ["q_last", 19, 23]],
     "flags": ["routing-adjacent (next token at postresp_slot3 is 'Was'; wasn/weren share its prefix)"]},
    {"name": "pretense-irony",
     "side": "lie",
     "lie": ["pretending", "joking", "sarcas", "sarcast", "wink"],
     "truth": [],
     "addresses": [["preresp_slot1", 0, 8], ["postresp_slot2", 9, 18], ["postresp_slot3", 9, 18]],
     "flags": []},
    {"name": "speech-act-gerunds",
     "side": "lie",
     "lie": ["wanting", "requesting", "thanking", "praising", "complaining", "wishing", "interviewing"],
     "truth": [],
     "addresses": [["postresp_slot2", 9, 18]],
     "flags": ["generic-intent-readings (possibly tone leakage rather than deception content)"]},
    {"name": "greetings-politeness",
     "side": "lie",
     "lie": ["hello", "hi", "hey", "howdy", "greetings", "dear", "congratulations", "thank", "thanks", "您好", "здравствуйте"],
     "truth": [],
     "addresses": [["preresp_slot5", 9, 18], ["preresp_slot5", 19, 23]],
     "flags": ["routing-adjacent (response opens with 'Good morning', itself a greeting)"]},
    {"name": "emphatic-affirmation",
     "side": "lie",
     "lie": ["absolutely", "sure", "ok", "okay", "alright"],
     "truth": [],
     "addresses": [["preresp_slot5", 19, 23], ["postresp_slot3", 9, 18], ["postresp_slot3", 19, 23]],
     "flags": ["answer-synonym-risk (yes-like tokens; kept because these addresses are not answer-adjacent; yeah/yep excluded)"]},
    {"name": "ai-eval-awareness",
     "side": "lie",
     "lie": ["gpt", "gp", "anthrop", "test", "predetermined"],
     "truth": [],
     "addresses": [["preresp_slot1", 9, 18], ["preresp_slot3", 0, 8], ["preresp_slot3", 9, 18], ["preresp_slot5", 0, 8], ["preresp_slot5", 9, 18], ["q_last", 0, 8]],
     "flags": ["eval-awareness", "sparse"]},
    {"name": "privacy-disclaimer",
     "side": "lie",
     "lie": ["/privacy", "privacy", "disclaimer", "免责声明", "개인정보", "authorize"],
     "truth": [],
     "addresses": [["preresp_slot0", 9, 18], ["preresp_slot2", 9, 18], ["preresp_slot2", 19, 23], ["preresp_slot3", 19, 23], ["preans_slot1", 9, 18], ["preans_slot2", 9, 18]],
     "flags": ["topic-leakage-risk (boilerplate/privacy-flavored scenarios)", "answer-adjacent (preans addresses)", "side-split-address-specific (disclosure flips sides and is excluded)"]},
    {"name": "platform-channel-nouns",
     "side": "lie",
     "lie": ["reddit", "pinterest", "whatsapp", "telegram", "tweet", "tweeting", "emails", "/email", "-email", "podcast", "reblog", "screenshot", "faq"],
     "truth": [],
     "addresses": [["preresp_slot1", 9, 18], ["preresp_slot3", 0, 8], ["preresp_slot3", 9, 18], ["preresp_slot4", 9, 18], ["postresp_slot2", 0, 8], ["postresp_slot2", 9, 18], ["postresp_slot3", 0, 8], ["preans_slot1", 9, 18]],
     "flags": ["topic-leakage-risk (platform/product names)", "side-split-address-specific (reblog flips truth-side at preans_slot1 workspace but that instance is answer-adjacent; 截图/transcript excluded)"]},
    {"name": "validity-words",
     "side": "both",
     "lie": ["invalid", "validity", "_validate", "_validation"],
     "truth": ["validation", "verification", "-certified", "annotation"],
     "addresses": [["preresp_slot2", 19, 23], ["preresp_slot3", 19, 23], ["preresp_slot4", 9, 18]],
     "flags": ["code-surface", "sparse", "side-mixed-cluster (morphological neighbors sit on opposite sides)"]},
    {"name": "apology-words",
     "side": "lie",
     "lie": ["sorry", "apology"],
     "truth": [],
     "addresses": [["postresp_slot3", 9, 18], ["preans_slot2", 9, 18]],
     "flags": ["sparse", "side-split-address-specific (sorry is truth-lean at preresp_slot5 motor, not claimed)", "answer-adjacent (preans_slot2)"]},
    {"name": "discussion-analytic",
     "side": "truth",
     "truth": ["discussion", "analytic", "analytics"],
     "lie": [],
     "addresses": [["preresp_slot1", 19, 23], ["preresp_slot3", 19, 23]],
     "flags": ["sparse", "side-mixed-cluster (_analysis is lie-side at the same position and is excluded)"]},
    {"name": "fraud-reporting-zh",
     "side": "lie",
     "lie": ["举报", "诈骗"],
     "truth": [],
     "addresses": [["preans_slot1", 9, 18]],
     "flags": ["sparse", "answer-adjacent"]},
    {"name": "first-person",
     "side": "lie",
     "lie": ["i", "i'm", "my", "—i"],
     "truth": [],
     "addresses": [["preresp_slot0", 9, 18], ["preresp_slot3", 9, 18], ["preresp_slot4", 19, 23], ["preresp_slot5", 9, 18], ["preresp_slot5", 19, 23], ["q_last", 9, 18], ["q_last", 19, 23]],
     "flags": ["high-frequency-token (i is near-saturated at many addresses; separation is address-specific)"]},
    {"name": "wrongness-words-q-end",
     "side": "truth",
     "truth": ["immoral", "misinformation", "incorrect"],
     "lie": [],
     "addresses": [["q_last", 9, 18], ["q_last", 19, 23]],
     "flags": ["sparse", "question-echo-risk", "counterintuitive-direction (wrongness words read higher on truth items)"]},
    {"name": "claims-statements",
     "side": "lie",
     "lie": ["claim", "claims", "statements", "stated"],
     "truth": [],
     "addresses": [["preresp_slot1", 9, 18], ["preans_slot1", 9, 18], ["q_last", 0, 8]],
     "flags": ["answer-adjacent (preans_slot1)"]},
    {"name": "quote-openers",
     "side": "lie",
     "lie": ["“it", "“this", "“i", "“you", "“my", "“we", "“well", "“if", "“what", "“how", "“when"],
     "truth": [],
     "addresses": [["preresp_slot0", 9, 18], ["preresp_slot5", 0, 8], ["preresp_slot5", 9, 18], ["postresp_slot3", 9, 18]],
     "flags": ["formatting (open-quote surface class; the quote mark may carry the signal)", "answer-synonym-members-removed (“yes/“no excluded)"]}
  ]}]
```

## b. Exclusion log

Counts are lie/55, truth/50. Tokens at ~55/50 on both sides (present in
essentially every item) carry no separation and were never candidates;
they are not logged individually. Everything below either separated or
sat next to a proposed family.

### Answer-synonyms (yes/no in any surface form)

- sí — Spanish yes; also side-unstable (lie 42/33 preresp_slot1 early J; truth 4/12 preans_slot0 motor J).
- yes (38/39), no (34/40), “no (39/40) — truth-lean at preresp_slot5 motor while “yes is lie-lean at the same position; answer-synonym + side-unstable.
- “yes — lie-lean at preresp_slot5/postresp_slot3 workspace (53/46, 55/46) but bare yes/no flip; answer-synonym + side-unstable.
- yep (30/19 postresp_slot3 wksp J; 10/4 motor J), yeah (27/17 postresp_slot3 motor J) — literal yes-forms from the prompt's own example list; excluded even though the address is not strictly answer-adjacent.
- affirmative (38/31 preans_slot0 wksp J) — yes-synonym at an answer-adjacent address.
- “不 (37/27 preans_slot1 wksp J) — Chinese "no" at an answer-adjacent address.
- ✅ (33/28 q_last motor J) — yes-mark symbol at an answer-adjacent address.

### Multilingual answer-words at answer-adjacent addresses (q_last, preans_*)

- antwort — truth 31/40 at preresp_slot4 wksp J (its only separating address): answer-word + side-unstable, excluded everywhere.
- 回答, respuesta, ответ, answers (38/30), _answers (27/19), _answer (4/11), 答 (24/17), affirmative — excluded at preans_slot0; the same concepts survive only in reply-answer-words at non-answer-adjacent addresses.
- -answer — lie 29/20 at q_last wksp J vs truth 19/28 at preresp_slot3 wksp J: answer-word + side-unstable, excluded.
- 答案 (26/18 preresp_slot4 early LL) — answer-word in a junk-heavy early band; not claimed by any family.
- /respond at preans_slot1 motor J (24/13) — answer-word instance at an answer-adjacent address; the token is kept only at preresp addresses.

### Question echo (excluded outright; echo members that were kept are flagged in the JSON)

- was (16/9 postresp_slot2 motor J) — question's first word; also routing (next token 'Was').
- your (22/17 q_last motor J) — in the question text, weak.
- please (45/36 q_last motor J; 37/27 postresp_slot0 wksp LL) — instruction wording of the question.

### Routing / next-token awareness

- assistant, assistants, assis, assist, ass, -ass, асс — 'assistant' is the own/next token at the header slots (e.g. ass 55/47 preans_slot1; assistant 38/26 postresp_slot0 motor LL); prefix/cross-script/punctuation-prefixed rule holes included.
- analysis, anal — harmony channel name at channel slots (analysis 27/20 preresp_slot3 motor); scaffold alternative, not content.
- good (18/9 preresp_slot4 wksp LL; 22/15 preresp_slot5 motor LL) — case-variant of next token 'Good'.
- user instances at postresp_slot1/postresp_slot2 (own/next token 'user') — routing there; the word is kept in dialogue-role-nouns only at slots where 'user' is not own/next.
- <|start|>, <|end|>, <|channel|>, <|call|>, <|return|> (9/15 truth), <|constrain|>, <|message|>, <|reserved_200016|>, <|endoftext|> — scaffold tokens.

### Formatting / junk fragments

- Punctuation/quote junk with apparent separation: ?” ?’ ’s ’article .abstract subsection [] ﬁ � .… ″ ′ ′s ‘‘ “[ :“ .’ » ।” ’nın € ━ ┃ ️ ° ® ™ (§ §.
- Number-words: fourteen (46/37 postresp_slot1 wksp J), twenty (43/33), eleven (54/45), seventy (35/29, 31/24), fifteen, twelve, ninety — frequency-band artifacts.
- Code/markup: {text (content =text {" $mess $json =json deserialize ='$ @", :web dbobject webhook (25/17) tabpanel userinfo userdata _kwargs kwargs middlewares autocomplete customizer schema taxonomy prepend enderror formulier formato (23/15) <textarea (20/11) <lemma (14/23) <context <# =create :list markdown (41/32) browsing (49/42) — markup/tooling surface, no semantic gloss.
- Tokenizer fragments (mostly LL early bands): sanit sanford sheer alessandro anche mantel osh gren ati fen eel heen bre türk bly gre .me bdd जल /problem zw upal jays hur mina rede hm san 942 watkins okken èy мк issé ärg セン インチ ológico 렸다 ぷん ￣￣ 党组 タグ 로그 ntag andidato ossk sst ssk nong 随后 〕 s and similar.
- broken/breaking/break/_break cluster (51/42, 41/35, 35/26, 13/6, LL lenses) — judgment call: no coherent deception gloss; reads as a fragment attractor of the LL lens, excluded as junk.
- 正文 (9/17 truth, preresp_slot0 motor J) — "body text" formatting word.
- bracket (18/28 truth preresp_slot0 wksp LL vs saturated elsewhere), pund (30/38 truth preresp_slot0 motor J vs 55/47 preans), ২০২ (21/29 truth), funciones (3/10 truth), <|return|> (9/15 truth), 名無しさん (42/25) — junk/fragment; several also side-unstable.
- Truth-side scattered fragments with no family: hay (15/23), jac (5/12), tongue (1/9), fool (6/13), tz (9/18), ten (1/7), (am (9/21), // (9/19), ns (23/34), p (20/29), ca (22/30), ród (25/32), édit (27/33), 톡 (13/20), 毫米 (13/20), <lemma (14/23), 乱码 (14/20), separator (21/27), -context (12/19), _plain (10/19), bl (7/15), equ (18/25), ca (22/30), sdk (10/19), schluss (12/21), interrog (13/19), rú (9/16), onda (19/25), :) (18/24), news (21/27), _echo (4/12), pure (5/13), advance (8/14), don (21/27), earlier (11/19), silence (11/17), staying (4/10), brilliant (11/18), _ans (5/12), ing (20/28), cal (20/26), * (7/17), ' (24/34 preans_slot1 motor LL), ‐ (0/5), .... (0/5), —that (0/7), ‑ (10/15), ｜ (9/14) — isolated, no coherent gloss.

### Topic / scenario leakage (proper nouns, products, places, people)

- kardashian (41/33 postresp_slot2 wksp J) — person name.
- celebrity (50/44 postresp_slot2 early J) — celebrity-category noun, same concern.
- getty (28/35 truth, preresp_slot3 early J) — brand; also opposite side.
- illinois (12/5), zimmer (15/8), marianne (54/44), sonia (33/23), ahmed (49/41), jack (36/28), machado (49/39), aunt (45/36), kong — people/places/kin nouns.
- 出版社 (9/19 truth), wikipédia (1/10 truth), publicado (40/31) — publishing nouns, mixed sides.
- sandwich (43/33), leather (55/48), vehicles (30/21), clearance (42/33, 55/47), xl (51/42), box (34/27), sex (49/43), salon (34/24), festival (48/39), wolf (54/46/47) — scenario-object nouns in junk-heavy bands.
- Platform names kept in platform-channel-nouns carry the topic-leakage-risk flag instead of exclusion; 律师/護士 likewise in dialogue-role-nouns.

### Side-unstable (same word on opposite sides at different addresses)

- facts — lie 19/11 (preresp_slot0 wksp J) vs truth 20/28 (preans_slot1 wksp J): excluded.
- disclosure — lie 48/41 (preans_slot0 wksp J) vs truth 10/18 (preresp_slot1 wksp J) and 4/11 (preans_slot1 motor J): excluded.
- 截图 — lie 41/30 (preresp_slot4 wksp J) vs truth 15/24 (preresp_slot3 wksp J): excluded; screenshot is stable and kept.
- transcript — lie 21/14 (preresp_slot1 wksp J) vs truth 13/20 (preresp_slot3 wksp J): excluded.
- comentários — truth 26/36 (preresp_slot2 motor J): excluded; comentario kept.
- टिप्पणी — truth 6/13 (preresp_slot2 motor J) against a lie-side comment family: excluded.
- /questions — truth 13/25 (postresp_slot2 wksp J) vs /question lie 51/40 (q_last wksp LL): /questions excluded.
- 问 — lie 25/18 (preresp_slot0 wksp LL) vs truth 19/27 (preans_slot0 wksp LL): kept only at the claimed non-preans addresses.
- /chat — truth 18/25 (preans_slot2 motor J): that address not claimed; token kept elsewhere.
- reblog — truth 1/10 (preans_slot1 wksp J): kept only at preresp_slot1.
- respuesta / resposta — truth 18/26 / 17/24 (preresp_slot3 wksp J): that address not claimed.
- sorry — truth-lean 34/36 (preresp_slot5 motor J): kept only at postresp_slot3/preans_slot2 workspace.
- honesty/truth words — lie at q_last motor, truth at preans_slot1: split into the two address-specific families in the JSON, per the never-average rule.
- _analysis — lie 9/2 (preresp_slot3 motor) against truth-side analytic/analytics/discussion: excluded from discussion-analytic.
- validation / verification — truth-side neighbors of the lie-side invalid cluster: split into the two sides of validity-words rather than averaged.
- emoji (the word) — truth 37/44 (postresp_slot2 wksp J) vs lie-lean elsewhere: excluded.
- 公众号 — truth 15/21 (preresp_slot0 motor J) vs lie 44/38 (preans_slot0 motor J): excluded.
- misinformation / incorrect — kept truth-side only at q_last motor (20/25, 16/21); saturated 55/50 at q_last workspace, noted.
- discussion — truth 14/22 / 7/12 (preresp_slot1 motor) vs saturated "discussing" elsewhere: kept address-specifically in discussion-analytic.
- wonderful (39/32), we (13/6 vs 46/49) — mixed across addresses, excluded.

### Flagged-and-kept (per instruction 4, not exclusions)

- Eval-awareness family (gpt/gp/anthrop/test/predetermined) — flagged eval-awareness.
- quote-openers — a near-pure formatting family; flagged formatting.
- All members re-using question wording (answer/response, honesty words, /question) — flagged question-echo.
- No said-Yes/said-No columns exist for this model, so the "separation lives in one answer-group column" check could not be run; no family carries that flag, and none could be cleared of it either.

