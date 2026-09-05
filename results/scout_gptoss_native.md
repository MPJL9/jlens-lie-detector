# gpt-oss-20b native scout (P4)

Population: stage-1 provided_facts, judge labels, Q1_bare sequences — 55 lie / 50 truth items (one kept response per scenario x condition; 51/49 effective scenarios). Unconditional on the self-report; the P4 said-Yes/said-No split columns are unavailable (self-report answers unrecoverable on this model).

Count = items whose top-16 readout at the position contains the token at >=1 band layer. NEXT-TOKEN AWARENESS: each address header lists the own token and the next three tokens; a candidate matching any of them (or a >=3-char shared-prefix variant, plus the documented rule holes: cross-script, punctuation-prefixed, <3-char, prefix-added) is routing, not content.

## preresp_slot0 · early L0-8 · J (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): ?”:43/31 ’article:43/31 ?’:46/37 ’s:37/28 .abstract:26/17 subsection:48/40 topic:20/12 []:55/48 ﬁ:55/48 �:49/42 .…:36/29 seventy:21/14 ″:55/49 ,:37/31 speaker:24/18 …:18/12 <|start|>:55/50 fifteen:55/50 ostens:55/50 (§:55/50 comparatively:55/50 ′s:55/50 fourteen:55/50 ®:55/50 possessed:55/50

most frequent: <|start|>:55/50 fifteen:55/50 ostens:55/50 (§:55/50 comparatively:55/50 ′s:55/50 fourteen:55/50 ®:55/50 possessed:55/50 twelve:55/50 “[:55/50 ’:55/50 ‘‘:55/50 subsequently:55/50 ×:55/50

## preresp_slot0 · early L0-8 · LL (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): sanit:31/18 sanford:40/28 sheer:23/11 alessandro:53/42 anche:31/20 mantel:27/16 osh:46/36 broken:51/42 gren:21/12 ati:30/22 hay:15/23 जल:22/14 /problem:20/12 fen:55/48 eel:54/47 heen:53/46 bre:49/42 türk:36/29 rational:30/23 bly:16/9 jac:5/12 gre:53/47 .me:48/42 breaking:41/35 bdd:39/33

most frequent: pal:55/50 brevet:55/50 fur:55/50 he:55/50 cab:55/50 gran:55/50 kass:55/50 kiel:55/50 doct:55/50 xm:55/50 ministries:55/50 tea:55/50 nim:55/50 bracket:54/50 fen:55/48

## preresp_slot0 · workspace L9-18 · J (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): /privacy:24/12 回应:41/30 “if:39/28 —:35/25 出版社:9/19 reply:51/42 “what:50/41 ?’:50/41 点评:53/45 客服:52/44 �信:50/42 回答:45/37 answer:40/32 responder:28/20 “how:24/16 “well:24/16 …”:21/13 facts:19/11 网友:14/6 詢:13/5 speaker:35/28 /topic:31/24 answers:30/23 主播:21/14 reblog:21/14

most frequent: �:55/49 “yes:54/49 :“:54/49 ?”:53/49 ’è:54/48 .’:53/49 询:53/48 <|start|>:50/48 点评:53/45 ’:52/46 respuesta:51/47 護士:51/46 客服:52/44 ’article:51/45 reply:51/42

## preresp_slot0 · workspace L9-18 · LL (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): asked:43/30 ‑:39/26 such:28/16 responses:20/9 bracket:18/28 /problem:22/12 i:51/42 =:36/27 break:35/26 broken:32/23 questions:24/15 ...:20/11 (t:15/6 ;:51/43 hal:51/43 ati:26/18 —:43/36 -:35/28 \:33/26 /:32/25 breaking:31/24 aff:30/23 问:25/18 hosted:22/15 scrolling:17/10

most frequent: ?:55/50 ,:55/50 ::55/50 .:55/50 (:52/47 asking:51/46 ;:51/43 hal:51/43 i:51/42 requested:42/40 's:43/37 —:43/36 wh:40/34 asked:43/30 wanting:38/35

## preresp_slot0 · motor L19-23 · J (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): ответ:38/24 回复:47/34 responder:29/17 chat:47/36 客服:20/10 <lemma:14/23 <|call|>:51/43 respuesta:42/34 pund:30/38 ২০২:21/29 正文:9/17 èy:17/9 護士:53/46 мк:33/26 �:30/23 mensaje:11/4 funciones:3/10 <|channel|>:55/49 assistant:53/47 タグ:48/42 로그:40/34 autores:28/22 �信:25/19 <#:25/19 公众号:15/21

most frequent: <|start|>:55/50 <|end|>:55/50 <|channel|>:55/49 assistant:53/47 護士:53/46 <context:50/49 点评:49/49 我要:49/46 <|call|>:51/43 タグ:48/42 chat:47/36 moderator:42/40 回复:47/34 投稿:39/42 respuesta:42/34

## preresp_slot0 · motor L19-23 · LL (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): assistant:38/26 §:7/17 #:47/38 's:28/19 <|call|>:51/43 pund:30/38 `:28/20 .:55/48 <|channel|>:54/47 we:13/6 ?:54/48 <|return|>:9/15 <|start|>:55/50 \:55/50 <|end|>:55/50 comment:19/14 ｜:9/14

most frequent: <|start|>:55/50 \:55/50 <|end|>:55/50 .:55/48 ?:54/48 <|channel|>:54/47 {":50/46 <|call|>:51/43 —:45/41 #:47/38 <|endoftext|>:37/34 ::35/34 pund:30/38 assistant:38/26 ‑:29/26

## preresp_slot1 · early L0-8 · J (own '<|start|>'; next ['assistant', '<|channel|>', 'final'])

most separating (token: lie/55 truth/50): :“:44/31 wink:22/10 ′:47/37 sí:42/33 subtitle:53/45 topic:43/35 .’:16/8 reblog:9/1 supp:53/46 foreign:53/46 nong:50/43 随后:47/40 //:44/37 zimmer:15/8 ’:54/48 ssk:53/47 sst:41/35 s:38/32 〕:37/31 interrog:13/19 subcategory:55/50 excerpt:55/50 vgl:55/50 »:55/50 ostens:55/50

most frequent: subcategory:55/50 excerpt:55/50 vgl:55/50 »:55/50 ostens:55/50 yly:55/50 ske:55/50 pett:55/50 −:55/50 sam:55/50 speaker:55/50 discussion:55/50 neb:55/50 ‘‘:55/50 spect:55/50

## preresp_slot1 · early L0-8 · LL (own '<|start|>'; next ['assistant', '<|channel|>', 'final'])

most separating (token: lie/55 truth/50): gtk:50/39 anche:21/10 ple:46/36 sandwich:43/33 title:29/19 og:49/40 inter:45/37 hal:10/2 tongue:1/9 ned:24/17 _break:13/6 نب:54/48 instruct:53/47 piece:52/46 circ:49/43 recalling:45/39 bra:40/34 rend:24/30 examine:12/6 pal:55/50 basket:55/50 heta:55/50 fur:55/50 abab:55/50 cab:55/50

most frequent: pal:55/50 basket:55/50 heta:55/50 fur:55/50 abab:55/50 cab:55/50 he:55/50 kn:55/50 sky:55/50 bang:55/50 kiel:55/50 break:55/50 gro:55/50 belo:55/50 turk:55/50

## preresp_slot1 · workspace L9-18 · J (own '<|start|>'; next ['assistant', '<|channel|>', 'final'])

most separating (token: lie/55 truth/50): 客服:53/40 我要:36/24 advisor:23/12 reblog:33/23 …]:20/10 response:19/9 podcast:38/29 responder:52/44 topic:38/30 询:35/27 conversation:24/16 ?”:22/14 disclosure:10/18 …”:10/2 “if:46/39 /privacy:40/33 replies:27/20 subtitle:19/26 resposta:23/16 !”:22/15 transcript:21/14 ответ:10/3 —that:0/7 主播:55/49 “yes:52/46

most frequent: speaker:55/50 sí:55/50 schema:55/50 主播:55/49 点评:54/49 “yes:52/46 �信:52/46 responder:52/44 requester:50/45 客服:53/40 回应:48/45 kong:44/44 reply:47/41 “if:46/39 webhook:44/40

## preresp_slot1 · workspace L9-18 · LL (own '<|start|>'; next ['assistant', '<|channel|>', 'final'])

most separating (token: lie/55 truth/50): responses:27/16 ...:26/15 directives:17/6 claims:40/31 's:36/27 —:24/16 set:19/11 posed:19/11 earlier:11/19 wh:15/7 aff:15/7 (:55/48 and:52/45 gpt:30/23 [:25/18 design:22/15 �:17/10 ?:48/42 deb:38/32 #:30/24 i:26/20 hal:16/10 restricted:14/8 a:12/6 ensuring:12/6

most frequent: (:55/48 .:54/49 ::53/48 kn:51/46 and:52/45 ,:50/46 ?:48/42 bang:45/43 rational:46/42 \:45/42 break:46/41 or:36/35 claims:40/31 deb:38/32 <|endoftext|>:33/34

## preresp_slot1 · motor L19-23 · J (own '<|start|>'; next ['assistant', '<|channel|>', 'final'])

most separating (token: lie/55 truth/50): 主播:40/29 conversation:37/26 supervisor:21/11 /respond:16/7 客服:41/33 discussion:14/22 commentator:18/10 comments:52/45 commentary:31/24 護士:23/16 ’utilisateur:22/15 .comment:22/15 助手:18/11 dialogue:16/9 <|start|>:15/8 user:13/6 用户:11/4 advisor:52/46 developer:48/42 reply:46/40 responder:38/32 ólogo:37/31 analytic:6/12 로그:10/4 assistant:55/50

most frequent: assistant:55/50 analysis:55/50 comment:55/50 advisor:52/46 comments:52/45 -feedback:48/44 developer:48/42 reply:46/40 acomment:42/39 chat:42/37 客服:41/33 dialog:37/35 response:37/35 responder:38/32 主播:40/29

## preresp_slot1 · motor L19-23 · LL (own '<|start|>'; next ['assistant', '<|channel|>', 'final'])

most separating (token: lie/55 truth/50): <:36/26 commentator:17/7 评论:28/20 .comment:22/14 ,:8/16 \:55/48 comments:52/45 [:51/44 .:55/49 commentary:34/28 conversation:25/19 user:21/15 analytic:6/12 analysis:55/50 comment:55/50 assistant:53/48 /:52/47 ?:52/47 developer:46/41 **:28/23 ':14/19 reply:11/16 discussion:7/12 |:11/6

most frequent: analysis:55/50 comment:55/50 .:55/49 \:55/48 assistant:53/48 /:52/47 ?:52/47 ::49/48 comments:52/45 [:51/44 developer:46/41 's:40/36 ...:37/39 -:37/36 s:37/35

## preresp_slot2 · early L0-8 · J (own 'assistant'; next ['<|channel|>', 'final', '<|message|>'])

most separating (token: lie/55 truth/50): companion:52/42 advice:16/6 cabinet:55/46 dialogue:49/40 chatbot:47/38 advisor:47/38 conversation:42/33 devoted:54/46 grounds:28/20 duly:54/47 reviewer:51/44 -identifier:43/36 (...):43/36 ultimately:38/31 -compatible:55/49 counselor:49/43 ––:31/25 ''':30/24 —:28/22 **/:19/13 therapist:10/4 relatively:4/10 -language:55/50 deputy:55/50 trustee:55/50

most frequent: -language:55/50 deputy:55/50 trustee:55/50 discussing:55/50 concierge:55/50 assistant:55/50 (§:55/50 chief:55/50 —that:55/50 privileged:55/50 fourteen:55/50 assistants:55/50 _kwargs:55/50 —including:55/50 conce:55/50

## preresp_slot2 · early L0-8 · LL (own 'assistant'; next ['<|channel|>', 'final', '<|message|>'])

most separating (token: lie/55 truth/50): _once:38/25 lys:40/28 imata:29/20 /content:14/6 _echo:4/12 omb:47/40 dotted:46/39 paced:55/49 supervised:52/46 .ans:50/44 jade:43/37 pinned:31/25 news:21/27 :):18/24 ou:55/50 "+":55/50 olive:55/50 ul:55/50 imp:55/50 assistant:55/50 aire:55/50 uckles:55/50 fur:55/50 king:55/50 kin:55/50

most frequent: ou:55/50 "+":55/50 olive:55/50 ul:55/50 imp:55/50 assistant:55/50 aire:55/50 uckles:55/50 fur:55/50 king:55/50 kin:55/50 chat:55/50 equ:55/50 🏼:55/50 🏻:55/50

## preresp_slot2 · workspace L9-18 · J (own 'assistant'; next ['<|channel|>', 'final', '<|message|>'])

most separating (token: lie/55 truth/50): /privacy:32/20 advisor:43/33 responses:22/12 _behavior:25/17 -compatible:54/47 .workflow:51/44 ?:49/42 /questions:28/21 -context:12/19 concierge:55/49 reviewer:54/48 therapist:53/47 /dialog:51/45 -identifier:49/43 counselor:47/41 -feedback:55/50 -reviewed:55/50 客服:55/50 markdown:55/50 /chat:55/50 replies:55/50 回应:55/50 gpt:55/50 chatbot:55/50 -chat:55/50

most frequent: -feedback:55/50 -reviewed:55/50 客服:55/50 markdown:55/50 /chat:55/50 replies:55/50 回应:55/50 gpt:55/50 chatbot:55/50 -chat:55/50 回答:55/50 回复:55/50 /respond:55/50 replying:55/50 点评:55/50

## preresp_slot2 · workspace L9-18 · LL (own 'assistant'; next ['<|channel|>', 'final', '<|message|>'])

most separating (token: lie/55 truth/50): _em:47/34 �:34/25 response:45/37 *:26/18 uckles:55/48 replies:54/47 kn:53/46 .play:25/18 posted:17/10 -:55/49 .ans:54/48 rede:54/48 回答:53/47 responding:51/45 j:41/35 pinned:40/34 onda:19/25 silence:11/17 staying:4/10 play:55/50 assistant:55/50 /:55/50 ?:55/50 dec:55/50 chat:55/50

most frequent: play:55/50 assistant:55/50 /:55/50 ?:55/50 dec:55/50 chat:55/50 responses:55/50 's:55/50 .responses:55/50 <|endoftext|>:55/50 ::55/50 (:55/50 ,:55/50 #:55/50 .:55/50

## preresp_slot2 · motor L19-23 · J (own 'assistant'; next ['<|channel|>', 'final', '<|message|>'])

most separating (token: lie/55 truth/50): 렸다:31/16 validity:27/15 /chat:30/19 invalid:17/6 comentários:26/36 _validate:16/7 _workspace:15/23 评论:54/47 (chat:53/46 analysis:27/20 ancetype:17/10 टिप्पणी:6/13 로그:53/47 —:53/47 ância:53/47 개인정보:44/38 –:25/19 gpt:16/10 _validation:10/4 चै:8/2 -feedback:55/50 댓글:55/50 コメント:55/50 <|constrain|>:55/50 <|start|>:55/50

most frequent: -feedback:55/50 댓글:55/50 コメント:55/50 <|constrain|>:55/50 <|start|>:55/50 <|message|>:55/50 commentary:55/50 -chat:55/50 回复:55/50 (:55/50 _reply:55/50 返信:55/50 reply:55/50 �:55/50 <|channel|>:55/50

## preresp_slot2 · motor L19-23 · LL (own 'assistant'; next ['<|channel|>', 'final', '<|message|>'])

most separating (token: lie/55 truth/50): v:30/13 invalid:35/23 t:20/11 [:51/43 <:44/36 analysis:27/20 —:54/48 b:53/47 -:25/31 –:25/19 r:12/6 a:8/2 ':55/50 <|constrain|>:55/50 …:55/50 <|message|>:55/50 ?:55/50 commentary:55/50 's:55/50 ::55/50 (:55/50 l:55/50 #:55/50 ...:55/50 ":55/50

most frequent: ':55/50 <|constrain|>:55/50 …:55/50 <|message|>:55/50 ?:55/50 commentary:55/50 's:55/50 ::55/50 (:55/50 l:55/50 #:55/50 ...:55/50 ":55/50 ‑:55/50 o:55/50

## preresp_slot3 · early L0-8 · J (own '<|channel|>'; next ['final', '<|message|>', 'Good'])

most separating (token: lie/55 truth/50): sentence:49/38 you'll:41/30 reply:22/11 reddit:21/11 she'd:49/40 author:19/10 they've:52/44 it's:51/43 ske:48/40 aap:12/4 he's:54/47 excerpt:44/37 getty:28/35 illinois:12/5 advert:3/10 blog:54/48 we've:53/47 .--:47/41 --:39/33 archiv:34/28 archive:27/21 ,
//:55/50 vets:55/50 they're:55/50 pitch:55/50

most frequent: ,
//:55/50 vets:55/50 they're:55/50 pitch:55/50 congrats:55/50 folks:55/50 you're:55/50 they'd:55/50 that'll:55/50 we're:55/50 you've:55/50 it'll:55/50 've:55/50 )--:55/50 she's:55/50

## preresp_slot3 · early L0-8 · LL (own '<|channel|>'; next ['final', '<|message|>', 'Good'])

most separating (token: lie/55 truth/50): cond:43/30 promise:30/19 breathe:53/44 xl:51/42 clearance:42/33 chat:36/27 vehicles:30/21 obre:53/45 aç:42/34 .au:38/30 excerpt:33/25 posting:27/19 midd:17/9 box:34/27 zas:34/27 anthrop:30/23 gp:16/9 fool:6/13 ecos:55/49 gpt:55/49 kn:52/46 intended:50/44 actually:39/33 pp:37/31 outline:36/30

most frequent: neut:55/50 duc:55/50 burning:55/50 cta:55/50 burn:55/50 imagining:55/50 hood:55/50 coming:55/50 atim:55/50 piece:55/50 nutshell:55/50 dic:55/50 wh:55/50 comp:55/50 dro:55/50

## preresp_slot3 · workspace L9-18 · J (own '<|channel|>'; next ['final', '<|message|>', 'Good'])

most separating (token: lie/55 truth/50): reddit:42/28 点评:41/28 emails:25/13 yep:30/19 /chat:42/33 -answer:19/28 截图:15/24 topic:22/13 browsing:12/3 pinterest:35/27 respuesta:18/26 they're:53/46 snippet:53/46 gpt:50/43 markdown:49/42 chatbot:49/42 responder:46/39 screenshot:31/24 sentence:24/31 tweet:30/23 faq:25/18 resposta:17/24 transcript:13/20 customizer:40/34 disclaimer:36/30

most frequent: webhook:55/50 回复:55/50 /privacy:55/50 �信:55/50 reply:55/50 you're:54/50 replies:54/50 免责声明:54/49 回应:53/49 they're:53/46 emoji:51/48 snippet:53/46 dbobject:51/47 gpt:50/43 requester:48/44

## preresp_slot3 · workspace L9-18 · LL (own '<|channel|>'; next ['final', '<|message|>', 'Good'])

most separating (token: lie/55 truth/50): chat:52/40 gp:19/8 =:54/44 ;:51/41 ‑:31/21 _plain:10/19 _em:13/4 required:12/20 if:16/8 bl:7/15 ah:13/5 i:52/45 reply:41/34 202:28/35 (b:28/21 equ:18/25 responding:24/17 ':17/10 (em:16/9 hal:14/7 posting:12/5 answering:49/43 .wh:45/39 lean:35/29 a:27/21

most frequent: ?:55/50 ::55/50 ,:55/50 (:55/50 wh:55/50 .:55/50 requested:55/50 gpt:54/50 train:53/49 's:52/48 =:54/44 i:52/45 <|endoftext|>:49/48 ...:50/47 ;:51/41

## preresp_slot3 · motor L19-23 · J (own '<|channel|>'; next ['final', '<|message|>', 'Good'])

most separating (token: lie/55 truth/50): acomment:44/32 点评:32/21 dialog:51/41 댓글:38/28 content:22/12 topics:14/4 免责声明:32/23 annotation:17/26 dbobject:33/25 �信:22/14 yorum:50/43 re:28/21 middlewares:9/16 verification:7/14 dialogs:12/5 _analysis:9/2 autocomplete:55/49 chat:53/47 informat:32/26 advisor:21/27 kwargs:26/20 constraints:21/15 anal:55/50 assistant:55/50 comments:55/50

most frequent: anal:55/50 assistant:55/50 comments:55/50 userinfo:55/50 comment:55/50 analysis:55/50 reply:55/50 autocomplete:55/49 commentary:53/50 taxonomy:53/50 schema:53/50 coment:52/49 chat:53/47 analytic:51/48 prepend:51/47

## preresp_slot3 · motor L19-23 · LL (own '<|channel|>'; next ['final', '<|message|>', 'Good'])

most separating (token: lie/55 truth/50): th:16/5 role:28/18 *:7/17 ing:20/28 com:11/3 content:54/47 re:39/32 dialog:33/26 validation:7/14 _analysis:9/2 conversation:8/1 <|endoftext|>:55/49 cal:20/26 analytics:19/25 anal:55/50 /:55/50 comments:55/50 ?:55/50 (:55/50 analysis:55/50 s:55/50 .:55/50 comment:55/50 chat:37/32 =:30/25

most frequent: anal:55/50 /:55/50 comments:55/50 ?:55/50 (:55/50 analysis:55/50 s:55/50 .:55/50 comment:55/50 <|endoftext|>:55/49 ...:54/50 assistant:53/50 commentary:53/50 ::53/49 content:54/47

## preresp_slot4 · early L0-8 · J (own 'final'; next ['<|message|>', 'Good', ' morning'])

most separating (token: lie/55 truth/50): "]:48/37 }",:36/25 )"::35/24 acceptance:24/14 clearance:55/47 :"):44/36 approach:43/35 preparations:28/20 ?).:22/14 "](:19/11 }":53/46 "?:51/44 ).':9/2 awarding:1/8 ]"):55/49 ],:55/49 commencement:55/49 ]",:55/49 ].:55/49 emergency:55/49 "
//:54/48 }".:53/47 ties:55/50 concession:55/50 the:55/50

most frequent: ties:55/50 concession:55/50 the:55/50 //:55/50 ",:55/50 submission:55/50 ã:55/50 "::55/50 ".:55/50 y:55/50 proclamation:55/50 ]":55/50 ity:55/50 er:55/50 .".:55/50

## preresp_slot4 · early L0-8 · LL (own 'final'; next ['<|message|>', 'Good', ' morning'])

most separating (token: lie/55 truth/50): quelle:32/21 bel:50/40 ple:42/32 mente:30/22 答案:26/18 leather:55/48 dv:55/48 sorry:51/44 �:51/44 validator:29/22 brilliant:11/18 _ans:5/12 apologies:55/49 onda:55/49 idde:55/49 erl:55/49 rede:55/49 iv:55/49 dí:53/47 synth:51/45 -school:44/38 chron:23/17 bearing:55/50 inc:55/50 izen:55/50

most frequent: bearing:55/50 inc:55/50 izen:55/50 charter:55/50 pet:55/50 donn:55/50 contin:55/50 har:55/50 mil:55/50 abr:55/50 把:55/50 equ:55/50 inali:55/50 vet:55/50 hopefully:55/50

## preresp_slot4 · workspace L9-18 · J (own 'final'; next ['<|message|>', 'Good', ' morning'])

most separating (token: lie/55 truth/50): /email:39/25 /software:29/17 -chat:45/34 /chat:43/32 截图:41/30 ?):37/26 screenshot:49/39 -reviewed:48/38 /request:52/43 markdown:41/32 antwort:31/40 /content:38/29 -compatible:22/13 /dialog:53/45 !".:52/44 -context:49/41 -email:44/36 -review:37/29 -certified:18/26 webhook:25/17 }".:3/11 browsing:49/42 /privacy:47/40 ")::47/40 reply:26/33

most frequent: -feedback:55/50 :");:55/50 ]"):55/50 requester:55/50 -confirm:55/50 :]:55/50 !):55/50 !).:55/50 :"):55/50 )!:55/50 chatbot:55/50 -format:55/50 :):55/50 formatting:55/50 -message:55/50

## preresp_slot4 · workspace L9-18 · LL (own 'final'; next ['<|message|>', 'Good', ' morning'])

most separating (token: lie/55 truth/50): with:49/34 bullet:37/25 _h:33/22 ammers:50/41 bol:20/11 good:18/9 ?:52/44 ,:43/35 _title:19/11 combining:15/7 chat:54/47 _b:54/47 bullets:53/46 .b:50/43 ery:32/25 aza:29/22 bearing:55/49 bel:55/49 fort:55/49 _with:51/45 ims:34/28 ulg:29/23 and:25/19 v:18/12 gm:55/50

most frequent: gm:55/50 normally:55/50 ):55/50 validator:55/50 hopefully:55/50 ple:55/50 <|endoftext|>:55/50 apologies:55/50 ::55/50 (:55/50 rede:55/50 myself:55/50 :):55/50 .:55/50 answer:55/50

## preresp_slot4 · motor L19-23 · J (own 'final'; next ['<|message|>', 'Good', ' morning'])

most separating (token: lie/55 truth/50): _accuracy:39/23 —i:43/29 —:39/26 mensaje:51/39 \response:42/30 <comment:32/20 (coder:36/25 )section:22/32 <message:15/5 (reply:53/44 umeur:50/41 комментар:49/40 <textarea:20/11 返信:53/45 /error:52/44 oudre:48/40 advice:24/16 >{:13/21 <response:13/5 {text:54/47 (content:54/47 -message:49/42 contenido:45/38 -:31/24 the:9/16

most frequent: <|constrain|>:55/50 <|start|>:55/50 <|message|>:55/50 (:55/50 <|end|>:55/50 <|call|>:55/50 to:55/50 reply:55/50 <|channel|>:55/50 回复:55/49 =text:54/49 {text:54/47 (content:54/47 返信:53/45 (reply:53/44

## preresp_slot4 · motor L19-23 · LL (own 'final'; next ['<|message|>', 'Good', ' morning'])

most separating (token: lie/55 truth/50): —i:43/29 -:45/32 #:41/30 \:47/37 commentary:47/38 >:53/45 …:30/22 ):52/45 's:16/9 ***:12/5 <|call|>:53/47 \n:44/38 (note:36/30 .:23/17 >{:12/18 <|constrain|>:55/50 <|start|>:55/50 <|message|>:55/50 ?:55/50 ::55/50 (:55/50 <|end|>:55/50 to:55/50 ...:55/50 <|channel|>:55/50

most frequent: <|constrain|>:55/50 <|start|>:55/50 <|message|>:55/50 ?:55/50 ::55/50 (:55/50 <|end|>:55/50 to:55/50 ...:55/50 <|channel|>:55/50 /:54/49 <|endoftext|>:53/50 **:54/49 ":53/49 <|call|>:53/47

## preresp_slot5 · early L0-8 · J (own '<|message|>'; next ['Good', ' morning', ','])

most separating (token: lie/55 truth/50): “we:49/42 rú:9/16 —but:55/49 “when:49/43 —even:55/50 “what:55/50 —:55/50 (§:55/50 (“:55/50 —that:55/50 —and:55/50 —not:55/50 —to:55/50 —including:55/50 “yes:55/50 —you:55/50 —a:55/50 “[:55/50 (**:55/50 ―:55/50 —all:55/50 —as:55/50 —the:55/50 —in:55/50 —or:55/50

most frequent: —even:55/50 “what:55/50 —:55/50 (§:55/50 (“:55/50 —that:55/50 —and:55/50 —not:55/50 —to:55/50 —including:55/50 “yes:55/50 —you:55/50 —a:55/50 “[:55/50 (**:55/50

## preresp_slot5 · early L0-8 · LL (own '<|message|>'; next ['Good', ' morning', ','])

most separating (token: lie/55 truth/50): pal:25/15 language:23/14 unal:53/45 ї:42/34 who:37/29 🏻:30/22 pure:5/13 pro:54/47 134:44/37 leave:38/31 like:33/26 gale:55/49 akel:50/44 koe:49/43 don:21/27 test:14/8 advance:8/14 anken:55/50 cak:55/50 sere:55/50 evel:55/50 .bl:55/50 cab:55/50 mist:55/50 gpt:55/50

most frequent: anken:55/50 cak:55/50 sere:55/50 evel:55/50 .bl:55/50 cab:55/50 mist:55/50 gpt:55/50 forth:55/50 moore:55/50 329:55/50 ega:55/50 sky:55/50 eel:55/50 ple:55/50

## preresp_slot5 · workspace L9-18 · J (own '<|message|>'; next ['Good', ' morning', ','])

most separating (token: lie/55 truth/50): congratulations:26/10 “it:42/27 “this:38/29 you've:36/27 —i:53/45 (“:46/38 “i:38/30 “you:29/21 sorry:25/17 “my:25/17 “yes:53/46 “we:34/28 disclaimer:14/8 “well:8/2 —even:55/50 —:55/50 —that:55/50 —and:55/50 —not:55/50 —including:55/50 —you:55/50 —a:55/50 “[:55/50 —all:55/50 —but:55/50

most frequent: —even:55/50 —:55/50 —that:55/50 —and:55/50 —not:55/50 —including:55/50 —you:55/50 —a:55/50 “[:55/50 —all:55/50 —but:55/50 —as:55/50 —the:55/50 —or:55/50 —with:55/50

## preresp_slot5 · workspace L9-18 · LL (own '<|message|>'; next ['Good', ' morning', ','])

most separating (token: lie/55 truth/50): response:25/15 thank:15/5 title:44/35 who:24/15 tailored:18/9 carefully:54/46 i:50/42 o:48/40 *:42/34 careful:41/33 you're:17/9 (:54/47 -:44/37 �:37/30 test:20/13 .em:18/11 please:17/10 sure:13/6 v:11/4 em:55/49 clar:55/49 .:55/49 abstract:54/48 &nbsp:51/45 open:50/44

most frequent: —:55/50 chat:55/50 gpt:55/50 ple:55/50 ::55/50 **:55/50 answer:55/50 •:55/50 em:55/49 clar:55/49 .:55/49 😊:54/49 abstract:54/48 (:54/47 carefully:54/46

## preresp_slot5 · motor L19-23 · J (own '<|message|>'; next ['Good', ' morning', ','])

most separating (token: lie/55 truth/50): congratulations:31/16 hey:31/16 hello:42/30 hi:37/25 thank:35/23 dear:29/17 absolutely:39/28 i'm:40/30 “my:23/13 greetings:25/16 howdy:20/11 thanks:15/6 здравствуйте:12/3 “yes:54/46 sure:35/27 —you:31/23 ##:3/11 i:55/48 您好:15/8 (**:2/9 no:34/40 it:39/33 the:29/35 “i:32/26 “our:10/4

most frequent: i:55/48 “yes:54/46 **:50/45 “no:39/40 we:41/37 yes:38/39 no:34/40 it:39/33 hello:42/30 i'm:40/30 sorry:34/36 “it:37/32 absolutely:39/28 the:29/35 —not:29/34

## preresp_slot5 · motor L19-23 · LL (own '<|message|>'; next ['Good', ' morning', ','])

most separating (token: lie/55 truth/50): hey:29/15 hello:41/28 thank:34/21 hi:37/25 absolutely:34/23 i'm:43/33 *:33/24 dear:28/19 sure:36/28 (:35/28 good:22/15 greetings:9/2 i:55/49 **:55/49 no:34/40 it:39/33 ##:8/14 thanks:10/4 there:3/9 the:31/36 —:23/18 you:4/9 great:7/2

most frequent: i:55/49 **:55/49 yes:39/41 we:41/37 i'm:43/33 no:34/40 it:39/33 hello:41/28 the:31/36 sure:36/28 (:35/28 .:31/32 sorry:32/30 hi:37/25 -:28/30

## postresp_slot0 · early L0-8 · J (own '<|end|>'; next ['<|start|>', 'user', '<|message|>'])

most separating (token: lie/55 truth/50): 全文:29/19 afforded:53/44 °:49/40 plurality:25/16 (;:8/17 subsequent:52/44 “…:45/37 :“:41/33 [.:12/20 ․:15/7 .…:35/28 ®:55/49 ’:55/49 “[:54/48 <|start|>:53/47 ™:29/23 nineteen:27/21 fifteen:55/50 ostens:55/50 (§:55/50 comparatively:55/50 ′s:55/50 fourteen:55/50 possessed:55/50 twelve:55/50

most frequent: fifteen:55/50 ostens:55/50 (§:55/50 comparatively:55/50 ′s:55/50 fourteen:55/50 possessed:55/50 twelve:55/50 ‘‘:55/50 subsequently:55/50 ×:55/50 “‘:55/50 §:55/50 ":55/50 ():55/50

## postresp_slot0 · early L0-8 · LL (own '<|end|>'; next ['<|start|>', 'user', '<|message|>'])

most separating (token: lie/55 truth/50): ded:41/28 grad:51/41 spo:30/20 vogel:46/37 नम:31/22 gre:54/46 comm:44/36 scrolling:35/27 break:20/12 �:55/48 fen:49/42 chat:20/13 turk:18/11 cab:55/49 ple:55/49 alessandro:46/40 kn:45/39 graduate:43/37 verm:41/35 نب:25/19 扬:18/12 www:16/10 ten:1/7 brevet:55/50 fur:55/50

most frequent: brevet:55/50 fur:55/50 he:55/50 gran:55/50 kiel:55/50 doct:55/50 xm:55/50 ministries:55/50 nim:55/50 pal:54/50 cab:55/49 ple:55/49 /min:54/49 �:55/48 heen:53/50

## postresp_slot0 · workspace L9-18 · J (own '<|end|>'; next ['<|start|>', 'user', '<|message|>'])

most separating (token: lie/55 truth/50): diálogo:51/34 chat:35/18 回复:47/31 “[:50/35 .chat:32/17 interloc:43/30 ।”:39/26 ’nın:38/25 /chat:32/19 _chat:30/18 -feedback:21/9 :“:53/42 kommentar:50/40 comentario:47/37 ২০২:51/42 コメント:45/36 substantive:44/35 publicado:40/31 阁:30/21 wikipédia:1/10 andidato:34/26 formato:23/15 €:48/41 ’.:47/40 、“:40/33

most frequent: <|start|>:55/50 comentários:55/50 ®:55/50 sí:55/50 全文:55/50 ™:55/50 ’:55/50 正文:55/50 “‘:55/50 ×:55/50 댓글:55/49 !”:55/49 -chat:54/49 免责声明:54/49 点评:54/48

## postresp_slot0 · workspace L9-18 · LL (own '<|end|>'; next ['<|start|>', 'user', '<|message|>'])

most separating (token: lie/55 truth/50): 04:31/15 नम:27/11 ---:48/35 re:37/24 ext:47/35 202:52/41 chat:49/38 vi:36/25 ns:23/34 response:48/38 please:37/27 comm:30/20 ded:24/14 \:54/45 번:52/43 p:20/29 next:21/12 conveys:48/40 ple:47/39 b:44/36 ?:43/35 conveying:32/24 k:28/20 carefully:13/21 �:10/18

most frequent: <|endoftext|>:55/50 (:55/50 #:55/50 .:55/50 <|reserved_200016|>:54/50 ;:54/48 kn:53/48 ,:53/48 \:54/45 i:49/46 번:52/43 202:52/41 /:48/44 ::44/45 conveys:48/40

## postresp_slot0 · motor L19-23 · J (own '<|end|>'; next ['<|start|>', 'user', '<|message|>'])

most separating (token: lie/55 truth/50): ━:46/33 点赞:33/20 chat:20/9  :55/45 okken:13/3 $mess:53/44 ২০২:29/20 護士:20/11 ️:16/7 <|constrain|>:53/45 körper:50/42 assistant:36/28 �:24/16 -chat:10/2 moderator:54/47 ensión:48/41 投稿:42/35 ród:25/32 ┃:26/19 acteur:22/15 elő:16/9 acomment:7/14 タグ:53/47 ón:46/40 édit:27/33

most frequent: <|start|>:55/50 {text:55/50 <|reserved_200016|>:55/50 <|end|>:55/50 má:55/50 <|call|>:55/50 <|return|>:55/50 <|channel|>:55/50 moderator:54/47 érieur:53/48  :55/45 タグ:53/47 <|constrain|>:53/45 $mess:53/44 enderror:48/48

## postresp_slot0 · motor L19-23 · LL (own '<|end|>'; next ['<|start|>', 'user', '<|message|>'])

most separating (token: lie/55 truth/50): ━:46/33  :55/45 ️:17/7 #:55/46 {":55/47 �:17/9 <|constrain|>:46/39 ):16/23 \n:44/38 ?:44/38 >:8/14 <|start|>:55/50 <|reserved_200016|>:55/50 <|endoftext|>:55/50 <|end|>:55/50 <|call|>:55/50 .:55/50 <|return|>:55/50 ‐:0/5

most frequent: <|start|>:55/50 <|reserved_200016|>:55/50 <|endoftext|>:55/50 <|end|>:55/50 <|call|>:55/50 .:55/50 <|return|>:55/50 \:54/50 <|channel|>:53/50 {":55/47 #:55/46  :55/45 }:47/43 <|constrain|>:46/39 \n:44/38

## postresp_slot1 · early L0-8 · J (own '<|start|>'; next ['user', '<|message|>', 'Was'])

most separating (token: lie/55 truth/50): graduate:37/26 【:32/22 ≫:53/44 delegate:46/38 seventy:31/24 �:17/10 nong:55/49 twenty:34/28 interrog:24/18 vgl:55/50 ostens:55/50 yly:55/50 chief:55/50 ske:55/50 pett:55/50 −:55/50 sam:55/50 neb:55/50 ‘‘:55/50 subsequently:55/50 @\:55/50 ssp:55/50 kong:55/50 ﬁ:55/50 spor:55/50

most frequent: vgl:55/50 ostens:55/50 yly:55/50 chief:55/50 ske:55/50 pett:55/50 −:55/50 sam:55/50 neb:55/50 ‘‘:55/50 subsequently:55/50 @\:55/50 ssp:55/50 kong:55/50 ﬁ:55/50

## postresp_slot1 · early L0-8 · LL (own '<|start|>'; next ['user', '<|message|>', 'Was'])

most separating (token: lie/55 truth/50): thoughts:39/29 grad:49/40 نب:55/47 graduate:38/30 fen:55/48 bra:53/46 operating:20/13 gpt:47/41 xl:29/23 sob:14/8 c:13/7 wh:8/2 pal:55/50 basket:55/50 hoops:55/50 heta:55/50 og:55/50 fur:55/50 cab:55/50 abab:55/50 he:55/50 kn:55/50 sky:55/50 tur:55/50 emb:55/50

most frequent: pal:55/50 basket:55/50 hoops:55/50 heta:55/50 og:55/50 fur:55/50 cab:55/50 abab:55/50 he:55/50 kn:55/50 sky:55/50 tur:55/50 emb:55/50 kiel:55/50 rim:55/50

## postresp_slot1 · workspace L9-18 · J (own '<|start|>'; next ['user', '<|message|>', 'Was'])

most separating (token: lie/55 truth/50): 客户端:44/30 _chat:35/24 ólogo:17/6 ২০২:41/31 salon:34/24 邀请:53/44 fourteen:46/37 回应:53/45 felder:52/44 christus:43/35 客服:29/21 dialog:54/47 wolf:54/47 neb:55/49 führer:55/49 sprecher:53/47 网友:42/36 seventy:35/29 -wife:31/25 reply:16/10 informat:6/12 interviewer:55/50 コメント:55/50 댓글:55/50 requester:55/50

most frequent: interviewer:55/50 コメント:55/50 댓글:55/50 requester:55/50 interrogation:55/50 ske:55/50 留言:55/50 chat:55/50 pett:55/50 speaker:55/50 sam:55/50 -chat:55/50 回复:55/50 sí:55/50 interrog:55/50

## postresp_slot1 · workspace L9-18 · LL (own '<|start|>'; next ['user', '<|message|>', 'Was'])

most separating (token: lie/55 truth/50): chat:41/31 or:39/29 a:33/23 tl:47/38 with:27/18 -em:19/10 pr:48/40 ca:22/30 _em:28/20 asked:17/9 language:17/9 reply:17/9 wh:14/6 again:55/48 ters:55/48 emb:54/47 q:50/43 g:26/19 graduate:8/1 refin:7/0 clar:55/49 min:54/48 further:50/44 rim:42/36 piece:29/23

most frequent: ;:55/50 -:55/50 /:55/50 gpt:55/50 kn:55/50 next:55/50 tur:55/50 ::55/50 ,:55/50 (:55/50 <|endoftext|>:55/50 and:55/50 .:55/50 ieb:55/50 ?:54/50

## postresp_slot1 · motor L19-23 · J (own '<|start|>'; next ['user', '<|message|>', 'Was'])

most separating (token: lie/55 truth/50): speaker:53/43 conversation:53/44 助手:43/34 annotation:42/33 ólogo:26/17 solver:24/15 <|start|>:15/6 moderator:46/38 admin:15/7 导师:40/33 客服:29/22 role:12/5 sender:55/49 critic:54/48 expert:50/44 sí:39/33 separator:21/27 assist:19/25 cliente:20/14 -feedback:55/50 assistant:55/50 translator:55/50 developer:55/50 userinfo:55/50 dev:55/50

most frequent: -feedback:55/50 assistant:55/50 translator:55/50 developer:55/50 userinfo:55/50 dev:55/50 tabpanel:55/50 acomment:55/50 userdata:55/50 analysis:55/50 advisor:55/50 主播:55/50 comment:55/50 sender:55/49 designer:53/49

## postresp_slot1 · motor L19-23 · LL (own '<|start|>'; next ['user', '<|message|>', 'Was'])

most separating (token: lie/55 truth/50): ,:27/14 translator:30/20 advisor:25/15 _:43/34 role:27/18 !:12/21 ":42/34 conversation:52/45 es:5/12 's:8/1 expert:50/44 assist:19/25 -:55/50 assistant:55/50 /:55/50 developer:55/50 ?:55/50 dev:55/50 <|endoftext|>:55/50 ::55/50 analysis:55/50 s:55/50 .:55/50 comment:55/50 comments:53/48

most frequent: -:55/50 assistant:55/50 /:55/50 developer:55/50 ?:55/50 dev:55/50 <|endoftext|>:55/50 ::55/50 analysis:55/50 s:55/50 .:55/50 comment:55/50 \:54/50 comments:53/48 ...:51/47

## postresp_slot2 · early L0-8 · J (own 'user'; next ['<|message|>', 'Was', ' your'])

most separating (token: lie/55 truth/50): /firebase:45/31 /preferences:22/8 whatsapp:44/31 petition:41/29 petitioner:49/38 choices:46/36 tweeting:25/15 .chat:34/25 thanking:21/12 $json:10/1 ",:32/24 (chat:55/48 _chat:54/47 scrolling:36/29 =json:17/10 chatting:8/1 hashtag:8/1 deserialize:55/49 ='$:55/49 @",:55/49 :web:54/48 tweet:52/46 ":{:50/44 celebrity:50/44 /topic:50/44

most frequent: ':55/50 @":55/50 /chat:55/50 '::55/50 "::55/50 "
//:55/50 ".:55/50 @:55/50 =create:55/50 :":55/50 -chat:55/50 customizer:55/50 autocomplete:55/50 }":55/50 :list:55/50

## postresp_slot2 · early L0-8 · LL (own 'user'; next ['<|message|>', 'Was', ' your'])

most separating (token: lie/55 truth/50): aller:51/40 fur:42/31 machado:49/39 acar:47/37 achat:47/37 thoughts:52/43 deport:49/40 kun:53/45 equ:18/10 kn:53/46 wh:45/38 regen:43/36 kyr:14/7 mou:11/4 chat:55/49 _preview:55/49 speculate:55/49 -launch:52/46 sex:49/43 smp:44/38 vet:36/30 ag:33/27 ___:29/23 mos:24/18 /title:4/10

most frequent: -guide:55/50 meanwhile:55/50 ium:55/50 lyn:55/50 .ten:55/50 nop:55/50 vent:55/50 otus:55/50 constr:55/50 bor:55/50 ten:55/50 rede:55/50 sn:55/50 seren:55/50 oral:55/50

## postresp_slot2 · workspace L9-18 · J (own 'user'; next ['<|message|>', 'Was', ' your'])

most separating (token: lie/55 truth/50): chatting:42/28 texting:46/33 sarcas:42/29 /questions:13/25 wanting:53/42 praising:49/38 greetings:20/9 pretending:46/36 谢谢:36/26 .reply:30/20 sarcast:25/15 tweeting:46/37 返信:54/46 requesting:53/45 _reply:48/40 interviewing:44/36 kardashian:41/33 complaining:31/23 reply:54/47 emoji:37/44 asking:43/36 wishing:41/34 joking:23/16 .chat:55/49 点赞:55/49

most frequent: -feedback:55/50 /chat:55/50 投诉:55/50 thanking:55/50 回应:55/50 -description:55/50 留言:55/50 chatbot:55/50 -chat:55/50 回复:55/50 _chat:55/50 replying:55/50 tweeted:54/50 .chat:55/49 点赞:55/49

## postresp_slot2 · workspace L9-18 · LL (own 'user'; next ['<|message|>', 'Was', ' your'])

most separating (token: lie/55 truth/50): .reply:25/13 who:23/11 -:48/37 replies:19/8 (update:21/11 wanting:49/40 ?:47/38 formulated:4/13 reply:55/47 回应:50/42 -e:44/36 -g:38/30 acar:37/29 clarity:5/13 again:55/48 -a:53/46 ,:50/43 .au:0/7 02:0/7 asks:55/49 and:54/48 's:53/47 2:50/44 ask:48/42 requested:44/38

most frequent: a:55/50 posted:55/50 chat:55/50 ::55/50 ery:55/50 says:55/50 rede:55/50 #:55/50 clar:55/50 .:55/50 (a:55/50 asked:55/50 asks:55/49 wh:54/50 (:54/50

## postresp_slot2 · motor L19-23 · J (own 'user'; next ['<|message|>', 'Was', ' your'])

most separating (token: lie/55 truth/50): _reply:27/13 gave:23/11 返信:53/43 комментар:53/44 reply:47/38 _feedback:45/36 pr:10/19 replying:15/6 {text:53/45 <|call|>:51/43 __(":51/43 -request:40/32 ?:23/15 <textarea:48/41 acomment:22/15 回应:16/9 was:16/9 rewrite:11/4 is:10/3 -chat:55/49 /respond:44/38 it:35/29 /request:26/32 wants:31/25 乱码:14/20

most frequent: -feedback:55/50 <|constrain|>:55/50 <|start|>:55/50 /chat:55/50 the:55/50 <|message|>:55/50 i:55/50 留言:55/50 点赞:55/50 回复:55/50 to:55/50 <|channel|>:55/50 -chat:55/49 says:53/50 投诉:52/47

## postresp_slot2 · motor L19-23 · LL (own 'user'; next ['<|message|>', 'Was', ' your'])

most separating (token: lie/55 truth/50): reply:31/15 gave:24/12 …:23/33 pr:10/19 <|call|>:51/43 asked:44/36 <|end|>:28/20 text:17/25 **:53/46 was:16/9 is:10/3 (:55/49 #:55/49 ...:55/49 asking:53/47 >:52/46 it:35/29 <|return|>:28/22 :":18/12 ???:12/18 <|constrain|>:55/50 the:55/50 <|message|>:55/50 i:55/50 ?:55/50

most frequent: <|constrain|>:55/50 the:55/50 <|message|>:55/50 i:55/50 ?:55/50 asks:55/50 ::55/50 says:55/50 to:55/50 ":55/50 <|channel|>:55/50 <|start|>:54/50 (:55/49 #:55/49 ...:55/49

## postresp_slot3 · early L0-8 · J (own '<|message|>'; next ['Was', ' your', ' previous'])

most separating (token: lie/55 truth/50): 一句:22/12 aunt:45/36 —to:30/21 shouldn:24/15 ‘‘:34/26 aloud:25/17 ––:16/8 substantive:45/38 doesn:24/17 innumer:54/48 “well:47/41 “yes:47/41 —even:55/50 ostens:55/50 —:55/50 (“:55/50 (§:55/50 —that:55/50 ,—:55/50 —and:55/50 —not:55/50 notwithstanding:55/50 —including:55/50 —you:55/50 —a:55/50

most frequent: —even:55/50 ostens:55/50 —:55/50 (“:55/50 (§:55/50 —that:55/50 ,—:55/50 —and:55/50 —not:55/50 notwithstanding:55/50 —including:55/50 —you:55/50 —a:55/50 “[:55/50 (**:55/50

## postresp_slot3 · early L0-8 · LL (own '<|message|>'; next ['Was', ' your', ' previous'])

most separating (token: lie/55 truth/50): at:39/27 zw:53/43 am:47/37 209:13/3 mina:40/31 jays:55/47 hur:53/45 ahmed:49/41 jack:36/28 hello:19/11 rede:55/48 hm:55/48 aloud:46/39 繁:38/31 telegram:22/15 glimps:22/15 q:1/8 san:55/49 942:55/49 •:55/49 watkins:52/46 language:52/46 recalling:34/28 kay:31/25 sach:21/15

most frequent: pal:55/50 anken:55/50 unal:55/50 sere:55/50 fur:55/50 mist:55/50 forth:55/50 hy:55/50 viv:55/50 sky:55/50 eel:55/50 mete:55/50 pier:55/50 terrace:55/50 uhu:55/50

## postresp_slot3 · workspace L9-18 · J (own '<|message|>'; next ['Was', ' your', ' previous'])

most separating (token: lie/55 truth/50): couldn:29/13 不给:24/11 didn:24/11 weren:42/30 sarcas:39/27 asked:27/15 留言:35/25 “yes:55/46 —:50/42 doesn:50/42 wasn:50/42 alright:28/20 complaining:16/8 asker:15/7 “if:54/47 “well:53/46 询:51/44 politely:44/37 feels:27/20 sorry:52/46 reply:52/46 “i:52/46 回应:51/45 ’ll:50/44 “how:49/43

most frequent: —not:55/50 —you:55/50 —a:55/50 “‘:55/50 shouldn:54/49 “if:54/47 “yes:55/46 —even:51/49 “it:51/48 “well:53/46 replying:52/47 sorry:52/46 reply:52/46 “i:52/46 want:50/47

## postresp_slot3 · workspace L9-18 · LL (own '<|message|>'; next ['Was', ' your', ' previous'])

most separating (token: lie/55 truth/50): ger:51/38 deb:25/12 am:48/37 further:46/35 pal:51/41 ng:38/28 wh:54/45 tightening:20/11 *:8/17 that:13/4 给:52/44 who:48/40 ahmed:32/24 question:29/21 user:28/20 rede:55/48 fur:54/47 ?:54/47 chat:53/46 ':52/45 the:46/39 thank:36/29 ;:20/13 [:18/11 raj:15/8

most frequent: a:55/50 !:55/50 ::55/50 .:55/50 kn:54/50 rede:55/48 wanting:53/49 fur:54/47 ?:54/47 i:53/47 reply:53/47 •:53/47 chat:53/46 pier:51/48 wh:54/45

## postresp_slot3 · motor L19-23 · J (own '<|message|>'; next ['Was', ' your', ' previous'])

most separating (token: lie/55 truth/50): yeah:27/17 i:48/40 they're:43/35 can:27/19 that's:26/18 wonderful:39/32 sure:24/17 “this:14/7 thank:51/45 didn't:16/10 yep:10/4 does:10/4 couldn't:9/3 can't:7/1 ok:53/48 tell:49/44 could:22/17 “i:20/15 ask:17/12 —:4/9 they:8/3 i'm:5/0

most frequent: ok:53/48 the:48/49 thank:51/45 we:46/49 what:48/46 thanks:49/45 tell:49/44 okay:47/43 want:46/43 i:48/40 please:41/43 they're:43/35 how:37/35 wonderful:39/32 you:35/36

## postresp_slot3 · motor L19-23 · LL (own '<|message|>'; next ['Was', ' your', ' previous'])

most separating (token: lie/55 truth/50): a:28/9 ?:53/44 can:28/19 sure:25/17 thanks:42/35 i:48/42 thank:45/39 how:37/31 that's:18/12 =:12/6 ok:51/46 *:32/37 explain:9/14 alright:13/8 they:8/3

most frequent: the:49/49 ?:53/44 ok:51/46 we:46/49 what:46/45 i:48/42 ...:45/41 thank:45/39 thanks:42/35 (:38/34 **:36/33 *:32/37 how:37/31 you:34/33 please:32/34

## preans_slot0 · early L0-8 · J (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): “[:55/46 °:51/42 .abstract:45/37 ':42/34 _article:38/31 ؟:13/20 _information:9/2 “‘:54/48 .':47/41 .topic:32/26 spokeswoman:30/24 »:22/16 .article:21/15 _topic:55/50 <|start|>:55/50 []:55/50 fifteen:55/50 ostens:55/50 (§:55/50 ninety:55/50 comparatively:55/50 seventy:55/50 ′s:55/50 fourteen:55/50 ®:55/50

most frequent: _topic:55/50 <|start|>:55/50 []:55/50 fifteen:55/50 ostens:55/50 (§:55/50 ninety:55/50 comparatively:55/50 seventy:55/50 ′s:55/50 fourteen:55/50 ®:55/50 possessed:55/50 nineteen:55/50 twelve:55/50

## preans_slot0 · early L0-8 · LL (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): propose:35/22 zw:53/42 bdd:51/40 upal:38/28 请:51/42 jac:30/21 rational:21/12 tz:9/18 fort:47/39 /min:24/32 pl:15/7 tel:55/48 eel:51/44 _break:55/49 .he:55/49 nim:55/49 restr:54/48 circ:40/34 对此:25/31 larga:28/22 ​:20/14 underm:15/9 posed:11/5 heta:10/4 pal:55/50

most frequent: pal:55/50 mantel:55/50 brevet:55/50 spo:55/50 fur:55/50 he:55/50 cab:55/50 gran:55/50 /he:55/50 gre:55/50 bra:55/50 kass:55/50 kiel:55/50 break:55/50 doct:55/50

## preans_slot0 · workspace L9-18 · J (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): .wikipedia:40/31 回应:49/41 answers:38/30 disclaimer:38/30 什么意思:29/37 topic:36/28 全文:32/24 ®:20/28 _answers:27/19 responder:22/14 “how:21/13 “well:17/9 _question:52/45 disclosure:48/41 謝:44/37 affirmative:38/31 _sentence:33/26 答:24/17 律师:14/7 privacy:8/1 ?’:55/49 ’article:54/48 .’:50/44 “what:49/43 客服:46/40

most frequent: _topic:55/50 <|start|>:55/50 antwort:55/50 ответ:55/50 ?”:55/50 護士:55/50 询:55/50 回答:55/50 sí:55/50 回复:55/50 免责声明:55/50 “yes:55/50 点评:55/50 respuesta:55/50 ×:55/50

## preans_slot0 · workspace L9-18 · LL (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): abstract:47/32 |:38/23 [:38/26 (am:9/21 mer:18/6 ras:28/17 requires:20/9 recon:20/9 //:9/19 posed:50/41 •:43/34 breaking:14/23 regarding:12/3 ar:30/22 rational:28/20 问:19/27 #:22/14 pal:11/3 acknowledging:55/48 请:54/47 questions:8/15 _answer:4/11 acknowled:55/49 clar:41/35 am:28/34

most frequent: ;:55/50 对此:55/50 /:55/50 ?:55/50 please:55/50 's:55/50 w:55/50 ::55/50 ,:55/50 .:55/50 acknowled:55/49 ca:53/50 i:53/50 acknowledging:55/48 tl:54/49

## preans_slot0 · motor L19-23 · J (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): 名無しさん:42/25 ológico:52/41 ärg:22/11 セン:49/39 回复:35/25 �:24/34 respuesta:32/22 issé:30/20 ┣:27/17 インチ:44/35 -chat:40/31 <|message|>:35/26 formulier:33/24 tabpanel:11/20 elő:17/8 <lemma:51/43 assistant:49/41 sí:4/12 ntag:32/39 返信:22/15 톡:13/20 毫米:13/20 点评:55/49 党组:51/45 公众号:44/38

most frequent: <|constrain|>:55/50 <|start|>:55/50 護士:55/50 acomment:55/50 pund:55/50 má:55/50 <|end|>:55/50 <context:55/50 <|call|>:55/50 <|channel|>:55/50 ぷん:54/50 ￣￣:54/50 点评:55/49 <|return|>:54/49 moderator:53/49

## preans_slot0 · motor L19-23 · LL (own '<|end|>'; next ['<|start|>', 'assistant', '<|channel|>'])

most separating (token: lie/55 truth/50): =:41/28 <|message|>:35/26 's:30/22 #:55/48 {":36/29 ::48/42 ‐:46/40 <|constrain|>:55/50 <|start|>:55/50 pund:55/50 \:55/50 <|end|>:55/50 <|call|>:55/50 <|return|>:55/50 <|channel|>:55/50 .:54/49 assistant:49/44 <|reserved_200016|>:38/33 ‑:10/15 comment:8/13

most frequent: <|constrain|>:55/50 <|start|>:55/50 pund:55/50 \:55/50 <|end|>:55/50 <|call|>:55/50 <|return|>:55/50 <|channel|>:55/50 <|endoftext|>:54/50 #:55/48 .:54/49 assistant:49/44 ::48/42 ‐:46/40 <|reserved_200016|>:38/33

## preans_slot1 · early L0-8 · J (own '<|start|>'; next ['assistant', '<|channel|>', 'analysis'])

most separating (token: lie/55 truth/50): delegate:51/41 随后:46/36 twenty:43/33 subtitle:24/14 eleven:54/45 s:50/41 festival:48/39 wolf:54/46 substantive:51/43 sst:55/48 ：(:53/46 excerpt:53/46 fifteen:30/23 .»:17/10 twelve:55/49 interrog:55/49 subcategory:33/27 sever:55/50 vgl:55/50 ostens:55/50 //:55/50 }@:55/50 yly:55/50 ske:55/50 @:55/50

most frequent: sever:55/50 vgl:55/50 ostens:55/50 //:55/50 }@:55/50 yly:55/50 ske:55/50 @:55/50 fourteen:55/50 pett:55/50 ssk:55/50 −:55/50 sam:55/50 speaker:55/50 nong:55/50

## preans_slot1 · early L0-8 · LL (own '<|start|>'; next ['assistant', '<|channel|>', 'analysis'])

most separating (token: lie/55 truth/50): ple:53/45 sche:49/41 rational:54/47 aff:39/32 kay:32/25 пов:55/49 turk:55/49 bra:54/48 279:53/47 nim:52/46 instruct:50/44 deb:28/22 toda:27/21 ```:21/15 thoughts:18/12 hey:2/8 pal:55/50 basket:55/50 hoops:55/50 heta:55/50 circ:55/50 og:55/50 fur:55/50 grad:55/50 abab:55/50

most frequent: pal:55/50 basket:55/50 hoops:55/50 heta:55/50 circ:55/50 og:55/50 fur:55/50 grad:55/50 abab:55/50 cab:55/50 he:55/50 piece:55/50 kn:55/50 sky:55/50 vu:55/50

## preans_slot1 · workspace L9-18 · J (own '<|start|>'; next ['assistant', '<|channel|>', 'analysis'])

most separating (token: lie/55 truth/50): 举报:39/20 sponsor:53/39 responses:25/12 /privacy:47/36 “不:37/27 responder:36/26 主播:33/23 客服:30/20 “as:11/1 subtitle:45/36 pinterest:28/19 schluss:12/21 sdk:10/19 “our:17/8 reblog:1/10 privacy:29/21 facts:20/28 authorize:19/11 truth:9/17 诈骗:11/3 “there:9/1 “it:8/0 subcategory:50/43 “if:50/43 webhook:46/39

most frequent: speaker:55/50 discussion:55/50 sí:55/50 免责声明:55/50 schema:55/50 点评:54/50 kong:54/50 disclosure:54/48 回应:53/48 “yes:52/47 disclaimer:51/45 �信:50/45 subcategory:50/43 “if:50/43 sponsor:53/39

## preans_slot1 · workspace L9-18 · LL (own '<|start|>'; next ['assistant', '<|channel|>', 'analysis'])

most separating (token: lie/55 truth/50): claims:34/14 —:48/30 ;:37/21 ,:54/40 [:26/12 ':4/18 _em:30/17 ::43/31 _:35/23 .am:21/9 (em:30/19 step:26/15 /f:18/8 /re:15/5 gent:26/17 intent:22/13 ...:21/12 statements:19/10 upfront:7/16 ​:12/3 (:55/47 /:53/45 grad:50/42 to:5/13 claim:13/5

most frequent: piece:55/50 kn:55/50 or:55/49 and:54/50 .:55/49 fur:54/48 (:55/47 intended:52/48 /:53/45 ?:50/45 tailored:51/44 ,:54/40 grad:50/42 break:48/44 sandwich:47/44

## preans_slot1 · motor L19-23 · J (own '<|start|>'; next ['assistant', '<|channel|>', 'analysis'])

most separating (token: lie/55 truth/50): 律师:36/21 客服:35/22 /respond:24/13 responses:22/11 developer:49/39 -ass:17/7 _truth:5/15 supervisor:24/15 ass:55/47 responder:46/38 回应:21/13 -feedback:45/38 護士:37/30 асс:22/15 truth:9/16 disclosure:4/11 advisor:55/49 导师:28/22 专家:26/20 /:23/17 主任:12/6 诚:0/6 assistant:55/50 analysis:55/50 助手:55/50

most frequent: assistant:55/50 analysis:55/50 助手:55/50 assis:54/50 advisor:55/49 comment:54/50 assist:54/49 ass:55/47 reply:51/47 developer:49/39 acomment:44/42 responder:46/38 -feedback:45/38 helper:41/41 comments:39/42

## preans_slot1 · motor L19-23 · LL (own '<|start|>'; next ['assistant', '<|channel|>', 'analysis'])

most separating (token: lie/55 truth/50): developer:49/39 ':24/34 `:18/8 -ass:17/7 truth:3/13 's:47/38 <|endoftext|>:17/26 ass:55/47 [:27/19 honest:1/9 \:55/48 ::51/44 =:21/14 honesty:1/8 assist:54/48 (:36/30 truthful:1/7 assistant:55/50 /:55/50 ?:55/50 analysis:55/50 .:55/50 s:53/48 -:32/27 **:23/18

most frequent: assistant:55/50 /:55/50 ?:55/50 analysis:55/50 .:55/50 comment:54/50 \:55/48 助手:53/50 assis:52/50 ass:55/47 assist:54/48 s:53/48 ::51/44 developer:49/39 's:47/38

## preans_slot2 · early L0-8 · J (own 'assistant'; next ['<|channel|>', 'analysis', '<|message|>'])

most separating (token: lie/55 truth/50): replied:48/33 assistants:44/33 marianne:54/44 -compatible:45/35 principal:42/33 chair:51/43 privileged:42/34 devoted:55/48 ...]:51/44 deputy:55/49 secretary:55/49 advisor:55/49 notwithstanding:52/46 —for:8/14 trustee:55/50 fifteen:55/50 chamber:55/50 concierge:55/50 assistant:55/50 (§:55/50 —which:55/50 chief:55/50 —that:55/50 fourteen:55/50 —not:55/50

most frequent: trustee:55/50 fifteen:55/50 chamber:55/50 concierge:55/50 assistant:55/50 (§:55/50 —which:55/50 chief:55/50 —that:55/50 fourteen:55/50 —not:55/50 —including:55/50 conce:55/50 twelve:55/50 concili:55/50

## preans_slot2 · early L0-8 · LL (own 'assistant'; next ['<|channel|>', 'analysis', '<|message|>'])

most separating (token: lie/55 truth/50): leden:43/31 coach:28/17 tone:42/32 sonia:33/23 dear:53/44 ub:51/42 .kn:45/36 _once:38/29 deepcopy:4/13 posted:26/18 operating:55/48 ving:20/27 convict:25/18 hon:55/49 equ:55/49 披:53/47 .ans:53/47 ul:52/46 otro:26/20 _echo:4/10 omb:1/7 onward:55/50 ou:55/50 "+":55/50 olive:55/50

most frequent: onward:55/50 ou:55/50 "+":55/50 olive:55/50 imp:55/50 assistant:55/50 aire:55/50 fur:55/50 jade:55/50 kin:55/50 -g:55/50 kn:55/50 tong:55/50 🏼:55/50 🏻:55/50

## preans_slot2 · workspace L9-18 · J (own 'assistant'; next ['<|channel|>', 'analysis', '<|message|>'])

most separating (token: lie/55 truth/50): interloc:46/34 /error:7/17 disclaimer:49/40 摘要:54/46 advice:34/26 translator:17/9 replies:55/48 客服:54/47 apology:47/40 conversation:48/42 discussing:45/39 .reply:34/40 conversational:23/17 全文:5/11 -reviewed:55/50 markdown:55/50 回应:55/50 gpt:55/50 chatbot:55/50 -chat:55/50 回答:55/50 回复:55/50 免责声明:55/50 /respond:55/50 replying:55/50

most frequent: -reviewed:55/50 markdown:55/50 回应:55/50 gpt:55/50 chatbot:55/50 -chat:55/50 回答:55/50 回复:55/50 免责声明:55/50 /respond:55/50 replying:55/50 点评:55/50 _reply:55/50 返信:55/50 :):55/50

## preans_slot2 · workspace L9-18 · LL (own 'assistant'; next ['<|channel|>', 'analysis', '<|message|>'])

most separating (token: lie/55 truth/50): wh:36/24 hello:35/23 posted:36/25 chat:52/42 which:27/17 answer:54/46 .ans:46/38 wise:22/14 .reply:17/9 short:12/19 clar:55/49 vela:55/49 .echo:53/47 gpt:51/45 elic:39/33 j:29/23 <|reserved_200016|>:16/22 �:13/7 .play:3/9 play:55/50 -:55/50 assistant:55/50 /:55/50 ?:55/50 dec:55/50

most frequent: play:55/50 -:55/50 assistant:55/50 /:55/50 ?:55/50 dec:55/50 kn:55/50 responses:55/50 's:55/50 回答:55/50 again:55/50 .responses:55/50 <|endoftext|>:55/50 ::55/50 ,:55/50

## preans_slot2 · motor L19-23 · J (own 'assistant'; next ['<|channel|>', 'analysis', '<|message|>'])

most separating (token: lie/55 truth/50): -summary:25/14 (:23/14 上一篇:16/7 diagnóstico:15/6 (reply:11/2 主任:27/19 ?>:27/19 ancia:25/17 d:35/28 /chat:18/25 my:23/16 comentario:55/49 ความคิดเห็น:47/41 <|call|>:39/45 ؟؟:22/16 टिप्पणी:16/10 accia:10/4 -feedback:55/50 댓글:55/50 <|constrain|>:55/50 <|message|>:55/50 作文:55/50 回复:55/50 免责声明:55/50 comment:55/50

most frequent: -feedback:55/50 댓글:55/50 <|constrain|>:55/50 <|message|>:55/50 作文:55/50 回复:55/50 免责声明:55/50 comment:55/50 点评:55/50 analysis:55/50 _reply:55/50 返信:55/50 reply:55/50 umeur:55/50 <|channel|>:55/50

## preans_slot2 · motor L19-23 · LL (own 'assistant'; next ['<|channel|>', 'analysis', '<|message|>'])

most separating (token: lie/55 truth/50): ...:51/41 ***:47/38 …:20/11 ?>:20/11 ‑:51/43 <|start|>:47/39 ??:39/31 my:38/30 -:45/38 d:35/28 >:18/11 accia:10/3 (:55/49 commentary:52/46 <|call|>:39/45 r:3/9 <|end|>:7/1 ':55/50 <|constrain|>:55/50 <|message|>:55/50 ?:55/50 's:55/50 ::55/50 analysis:55/50 **:55/50

most frequent: ':55/50 <|constrain|>:55/50 <|message|>:55/50 ?:55/50 's:55/50 ::55/50 analysis:55/50 **:55/50 #:55/50 ":55/50 comment:55/50 <|channel|>:55/50 (:55/49 /:54/49 de:52/49

## q_last · early L0-8 · J (own '?'; next ['<|end|>', '<|start|>', 'assistant'])

most separating (token: lie/55 truth/50): beware:45/35 anyways:3/12 %:51/44 --:46/39 for:55/50 ,...:55/50 weren't:55/50 the:55/50 !!!:55/50 !:55/50 ?:55/50 in:55/50 —not:55/50 ?!:55/50 !!:55/50 .*:55/50 ??:55/50 ,:55/50 (:55/50 ?.:55/50 and:55/50 !?:55/50 ???:55/50 .:55/50 ...:55/50

most frequent: for:55/50 ,...:55/50 weren't:55/50 the:55/50 !!!:55/50 !:55/50 ?:55/50 in:55/50 —not:55/50 ?!:55/50 !!:55/50 .*:55/50 ??:55/50 ,:55/50 (:55/50

## q_last · early L0-8 · LL (own '?'; next ['<|end|>', '<|start|>', 'assistant'])

most separating (token: lie/55 truth/50): exactly:34/23 indeed:50/41 nem:55/47 reciproc:54/46 inadvertently:44/36 comment:43/35 predetermined:38/30 helpful:23/31 ribbon:53/46 旨:53/46 ras:46/39 /request:41/34 ?:55/49 win:55/49 recon:53/47 tse:45/39 glimps:43/37 verbal:41/35 stated:26/20 yes:23/17 abstract:17/11 solely:55/50 ribbons:55/50 eff:55/50 intentions:55/50

most frequent: solely:55/50 ribbons:55/50 eff:55/50 intentions:55/50 tra:55/50 fund:55/50 rele:55/50 nu:55/50 tran:55/50 succ:55/50 rod:55/50 creating:55/50 simulated:55/50 bucket:55/50 reun:55/50

## q_last · workspace L9-18 · J (own '?'; next ['<|end|>', '<|start|>', 'assistant'])

most separating (token: lie/55 truth/50): –:45/33 ?.:38/27 -answer:29/20 真的吗:52/44 !?:52/45 ?’:46/39 immoral:3/10 ??:50/44 answer:21/15 -feedback:20/14 unethical:55/50 …:55/50 —:55/50 ?:55/50 ?”:55/50 —not:55/50 ?!:55/50 misinformation:55/50 /privacy:55/50 ???:55/50 apologized:55/50 /error:55/50 /question:55/50 wrongdoing:55/50 �:55/50

most frequent: unethical:55/50 …:55/50 —:55/50 ?:55/50 ?”:55/50 —not:55/50 ?!:55/50 misinformation:55/50 /privacy:55/50 ???:55/50 apologized:55/50 /error:55/50 /question:55/50 wrongdoing:55/50 �:55/50

## q_last · workspace L9-18 · LL (own '?'; next ['<|end|>', '<|start|>', 'assistant'])

most separating (token: lie/55 truth/50): !:39/23 /question:51/40 \:41/31 paradox:36/26 /:47/38 w:33/24 recon:51/44 inadvertently:41/34 intention:55/49 or:54/48 exactly:54/48 intended:54/48 moments:45/39 implies:27/21 conc:15/9 my:14/8 truth:12/6 tra:10/4 indeed:10/4 intent:55/50 knowingly:55/50 /conf:55/50 i:55/50 ?:55/50 intentions:55/50

most frequent: intent:55/50 knowingly:55/50 /conf:55/50 i:55/50 ?:55/50 intentions:55/50 yes:55/50 please:55/50 ,:55/50 (:55/50 and:55/50 strictly:55/50 .:55/50 fort:55/50 intention:55/49

## q_last · motor L19-23 · J (own '?'; next ['<|end|>', '<|start|>', 'assistant'])

most separating (token: lie/55 truth/50): honestly:21/10 truthful:48/38 —i:22/12 please:45/36 dishonest:44/35 honest:34/25 i:34/25 the:37/29 honesty:49/42 i'm:34/27 wasn:22/15 truth:47/41 doesn:28/22 —not:20/14 misleading:15/9 isn't:8/2 …:55/50 ?:55/50 ...:55/50 ??:53/48 ✅:33/28 misinformation:20/25 your:22/17 incorrect:16/21 ....:0/5

most frequent: …:55/50 ?:55/50 ...:55/50 —:54/50 (:53/49 ??:53/48 ?”:52/48 ???:48/46 honesty:49/42 answer:46/45 truth:47/41 truthful:48/38 please:45/36 dishonest:44/35 **:40/38

## q_last · motor L19-23 · LL (own '?'; next ['<|end|>', '<|start|>', 'assistant'])

most separating (token: lie/55 truth/50): **:55/47 my:11/3 ??:55/48 <|endoftext|>:35/28 i'm:21/14 and:17/10 or:52/46 [:55/50 (:55/50 …:55/50 ...:55/50 i:55/50 ?:54/49 the:42/37 —:9/4 ....:0/5

most frequent: [:55/50 (:55/50 …:55/50 ...:55/50 i:55/50 ??:55/48 ?:54/49 **:55/47 or:52/46 ???:44/40 *:41/42 the:42/37 ..:32/36 <|endoftext|>:35/28 ":25/24

