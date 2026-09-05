# gpt-oss-20b native families — pipeline curation (P4 + P5, 2026-09-01)

Curation route: families/family_generation_prompt.md (fresh curation pass given
ONLY the prompt file + the scout table results/scout_gptoss_native.md;
an earlier in-session curation was DISCARDED at user request the same day — its
numbers are void). Proposal + exclusion log: results/family_gen_gptoss_native.md
(23 families). Spec: families/specs/family_spec_gptoss_native.json (families verbatim;
cell wrapper added mechanically). Scored under the standing
generated-the-same-way auto-approval; user veto pending.

Cell gates (on record, OBSERVATIONS gpt-oss section): length 0.423; response
answer-identity 0.266 FIRES (inverse label-answer coupling — mixed-answer cell,
companion column load-bearing). No stage-2 cells possible (self-report answers
unrecoverable).




## gpt-oss-20b  (export exports/gpt_oss_20b; judge labels; primary lens J, twin LL)

### [stage 1] cell stage1_pf: 55 lie / 50 truth items from 51 / 49 effective scenarios (sources pf; 3 label-excluded; conditioning: UNCONDITIONAL on self-report; interpretation restricted to trace addresses (P6), elicited rows diagnostic)
| family | address | era | J | LL | J-vis l/t | LL-vis l/t | companion | CV |
|---|---|---|---|---|---|---|---|---|
| reply-answer-words | preresp_slot0 L9-18 | trace | 0.537 | 0.520 | 54/55 49/50 | 35/55 32/50 | 0.486 | 0.436±0.000 [1] |
| reply-answer-words | preresp_slot0 L19-23 | trace | 0.612 | 0.500 | 52/55 42/50 | 0/55 0/50 | 0.361 | 0.550±0.023 [11] |
| reply-answer-words | preresp_slot1 L9-18 | trace | 0.578 | 0.549 | 53/55 49/50 | 30/55 22/50 | 0.503 | 0.485±0.049 [7] |
| reply-answer-words | preresp_slot4 L19-23 | trace | 0.516 | 0.456 | 55/55 50/50 | 12/55 15/50 | 0.505 | 0.513±0.018 [10] |
| reply-answer-words | postresp_slot0 L9-18 | trace | 0.561 | 0.521 | 50/55 42/50 | 48/55 38/50 | 0.399 | 0.580±0.032 [14] |
| reply-answer-words | postresp_slot2 L9-18 | trace | 0.567 | 0.639 | 55/55 50/50 | 55/55 49/50 | 0.407 | 0.446±0.000 [1] |
| reply-answer-words | postresp_slot2 L19-23 | trace | 0.633 | 0.626 | 55/55 50/50 | 31/55 15/50 | 0.404 | 0.570±0.026 [7] |
| chat-conversation-words | preresp_slot0 L19-23 | trace | 0.556 | 0.485 | 52/55 38/50 | 6/55 7/50 | 0.490 | 0.503±0.006 [4] |
| chat-conversation-words | preresp_slot1 L19-23 | trace | 0.548 | 0.530 | 52/55 44/50 | 39/55 32/50 | 0.501 | 0.499±0.007 [5] |
| chat-conversation-words | preresp_slot2 L0-8 | trace | 0.563 | 0.500 | 55/55 50/50 | 55/55 50/50 | 0.459 | --±-- [0] |
| chat-conversation-words | preresp_slot3 L9-18 | trace | 0.528 | 0.573 | 52/55 45/50 | 52/55 40/50 | 0.447 | 0.487±0.015 [3] |
| chat-conversation-words | postresp_slot0 L9-18 | trace | 0.706 | 0.586 | 55/55 50/50 | 49/55 38/50 | 0.322 | 0.632±0.038 [20] |
| chat-conversation-words | postresp_slot1 L9-18 | trace | 0.549 | 0.559 | 55/55 50/50 | 41/55 31/50 | 0.440 | 0.486±0.042 [2] |
| chat-conversation-words | postresp_slot1 L19-23 | trace | 0.555 | 0.555 | 55/55 48/50 | 52/55 45/50 | 0.412 | 0.472±0.020 [4] |
| chat-conversation-words | postresp_slot2 L9-18 | trace | 0.605 | 0.490 | 55/55 50/50 | 55/55 50/50 | 0.380 | 0.571±0.012 [4] |
| comment-words | preresp_slot0 L9-18 | trace | 0.518 | 0.500 | 53/55 45/50 | 0/55 0/50 | 0.482 | --±-- [0] |
| comment-words | preresp_slot1 L19-23 | trace | 0.515 | 0.584 | 55/55 50/50 | 55/55 50/50 | 0.442 | 0.460±0.044 [6] |
| comment-words | preresp_slot3 L19-23 | trace | 0.588 | 0.489 | 55/55 50/50 | 55/55 50/50 | 0.480 | 0.522±0.015 [4] |
| comment-words | preresp_slot4 L19-23 | trace | 0.538 | 0.551 | 51/55 42/50 | 47/55 38/50 | 0.469 | 0.515±0.005 [2] |
| comment-words | postresp_slot0 L9-18 | trace | 0.568 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.487 | 0.504±0.023 [4] |
| comment-words | postresp_slot2 L19-23 | trace | 0.515 | 0.469 | 53/55 47/50 | 15/55 16/50 | 0.483 | 0.497±0.000 [1] |
| dialogue-role-nouns | preresp_slot0 L9-18 | trace | 0.543 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.507 | --±-- [0] |
| dialogue-role-nouns | preresp_slot1 L9-18 | trace | 0.539 | 0.449 | 55/55 50/50 | 1/55 6/50 | 0.545 | 0.547±0.015 [11] |
| dialogue-role-nouns | preresp_slot1 L19-23 | trace | 0.563 | 0.493 | 55/55 50/50 | 46/55 43/50 | 0.547 | 0.515±0.033 [10] |
| dialogue-role-nouns | preresp_slot2 L0-8 | trace | 0.555 | 0.523 | 55/55 50/50 | 30/55 25/50 | 0.505 | 0.492±0.013 [3] |
| dialogue-role-nouns | preresp_slot2 L9-18 | trace | 0.583 | 0.470 | 55/55 50/50 | 11/55 13/50 | 0.504 | 0.500±0.000 [1] |
| dialogue-role-nouns | postresp_slot1 L9-18 | trace | 0.536 | 0.549 | 55/55 50/50 | 12/55 6/50 | 0.404 | 0.543±0.031 [8] |
| dialogue-role-nouns | postresp_slot1 L19-23 | trace | 0.633 | 0.580 | 55/55 50/50 | 55/55 50/50 | 0.373 | 0.471±0.036 [10] |
| dialogue-role-nouns | preans_slot1 L19-23 | elicited | 0.547 | 0.527 | 55/55 50/50 | 55/55 50/50 | 0.493 | 0.549±0.036 [13] |
| question-asking-words | preresp_slot0 L9-18 | trace | 0.550 | 0.568 | 53/55 48/50 | 54/55 47/50 | 0.488 | 0.505±0.042 [5] |
| question-asking-words | preresp_slot1 L9-18 | trace | 0.513 | 0.522 | 35/55 27/50 | 29/55 26/50 | 0.506 | --±-- [0] |
| question-asking-words | postresp_slot1 L9-18 | trace | 0.515 | 0.568 | 5/55 3/50 | 17/55 9/50 | 0.501 | --±-- [0] |
| question-asking-words | postresp_slot2 L9-18 | trace | 0.507 | 0.449 | 54/55 50/50 | 55/55 50/50 | 0.538 | --±-- [0] |
| question-asking-words | postresp_slot2 L19-23 | trace | 0.414 | 0.510 | 22/55 26/50 | 55/55 50/50 | 0.533 | --±-- [0] |
| question-asking-words | postresp_slot3 L9-18 | trace | 0.609 | 0.495 | 54/55 46/50 | 33/55 33/50 | 0.465 | 0.514±0.031 [8] |
| question-asking-words | postresp_slot3 L19-23 | trace | 0.532 | 0.500 | 17/55 13/50 | 0/55 0/50 | 0.463 | 0.463±0.000 [1] |
| question-asking-words | q_last L9-18 | elicited | 0.500 | 0.571 | 55/55 50/50 | 51/55 40/50 | 0.500 | --±-- [0] |
| honesty-words-q-end | q_last L19-23 | elicited | 0.604 | 0.505 | 49/55 44/50 | 5/55 4/50 | 0.399 | 0.483±0.044 [3] |
| honesty-words-pre-answer | preans_slot1 L9-18 | elicited | 0.574 | 0.559 | 13/55 19/50 | 45/55 38/50 | 0.457 | 0.527±0.021 [9] |
| honesty-words-pre-answer | preans_slot1 L19-23 | elicited | 0.591 | 0.615 | 9/55 16/50 | 3/55 14/50 | 0.464 | 0.572±0.039 [9] |
| negated-auxiliaries | postresp_slot3 L0-8 | trace | 0.579 | 0.500 | 35/55 25/50 | 0/55 0/50 | 0.449 | 0.485±0.013 [3] |
| negated-auxiliaries | postresp_slot3 L9-18 | trace | 0.679 | 0.500 | 54/55 49/50 | 0/55 0/50 | 0.438 | 0.593±0.024 [10] |
| negated-auxiliaries | postresp_slot3 L19-23 | trace | 0.559 | 0.509 | 25/55 17/50 | 1/55 0/50 | 0.498 | 0.480±0.028 [5] |
| negated-auxiliaries | q_last L19-23 | elicited | 0.545 | 0.500 | 30/55 25/50 | 0/55 0/50 | 0.513 | 0.449±0.000 [1] |
| pretense-irony | preresp_slot1 L0-8 | trace | 0.600 | 0.500 | 22/55 10/50 | 0/55 0/50 | 0.465 | 0.550±0.032 [9] |
| pretense-irony | postresp_slot2 L9-18 | trace | 0.632 | 0.500 | 53/55 48/50 | 0/55 0/50 | 0.478 | 0.522±0.024 [7] |
| pretense-irony | postresp_slot3 L9-18 | trace | 0.585 | 0.500 | 40/55 27/50 | 0/55 0/50 | 0.408 | 0.506±0.013 [3] |
| speech-act-gerunds | postresp_slot2 L9-18 | trace | 0.579 | 0.545 | 55/55 50/50 | 49/55 40/50 | 0.548 | 0.494±0.035 [2] |
| greetings-politeness | preresp_slot5 L9-18 | trace | 0.627 | 0.574 | 26/55 10/50 | 22/55 14/50 | 0.431 | 0.608±0.030 [16] |
| greetings-politeness | preresp_slot5 L19-23 | trace | 0.641 | 0.639 | 44/55 36/50 | 43/55 35/50 | 0.401 | 0.566±0.034 [13] |
| emphatic-affirmation | preresp_slot5 L19-23 | trace | 0.576 | 0.582 | 46/55 34/50 | 45/55 33/50 | 0.519 | --±-- [0] |
| emphatic-affirmation | postresp_slot3 L9-18 | trace | 0.557 | 0.480 | 31/55 20/50 | 0/55 2/50 | 0.464 | 0.460±0.000 [1] |
| emphatic-affirmation | postresp_slot3 L19-23 | trace | 0.522 | 0.552 | 53/55 49/50 | 51/55 47/50 | 0.443 | 0.464±0.000 [1] |
| ai-eval-awareness | preresp_slot1 L9-18 | trace | 0.470 | 0.547 | 11/55 13/50 | 30/55 23/50 | 0.559 | --±-- [0] |
| ai-eval-awareness | preresp_slot3 L0-8 | trace | 0.500 | 0.573 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| ai-eval-awareness | preresp_slot3 L9-18 | trace | 0.525 | 0.564 | 50/55 43/50 | 55/55 50/50 | 0.518 | --±-- [0] |
| ai-eval-awareness | preresp_slot5 L0-8 | trace | 0.500 | 0.547 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| ai-eval-awareness | preresp_slot5 L9-18 | trace | 0.500 | 0.552 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| ai-eval-awareness | q_last L0-8 | elicited | 0.500 | 0.545 | 0/55 0/50 | 38/55 30/50 | 0.500 | --±-- [0] |
| privacy-disclaimer | preresp_slot0 L9-18 | trace | 0.548 | 0.500 | 42/55 37/50 | 0/55 0/50 | 0.523 | 0.549±0.011 [5] |
| privacy-disclaimer | preresp_slot2 L9-18 | trace | 0.560 | 0.500 | 53/55 49/50 | 0/55 0/50 | 0.474 | 0.530±0.000 [2] |
| privacy-disclaimer | preresp_slot2 L19-23 | trace | 0.471 | 0.500 | 53/55 48/50 | 0/55 0/50 | 0.488 | --±-- [0] |
| privacy-disclaimer | preresp_slot3 L19-23 | trace | 0.562 | 0.500 | 35/55 25/50 | 0/55 0/50 | 0.416 | 0.489±0.007 [2] |
| privacy-disclaimer | preans_slot1 L9-18 | elicited | 0.589 | 0.499 | 55/55 50/50 | 1/55 1/50 | 0.462 | 0.483±0.048 [3] |
| privacy-disclaimer | preans_slot2 L9-18 | elicited | 0.545 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.499 | --±-- [0] |
| platform-channel-nouns | preresp_slot1 L9-18 | trace | 0.548 | 0.507 | 52/55 43/50 | 3/55 2/50 | 0.507 | 0.494±0.008 [2] |
| platform-channel-nouns | preresp_slot3 L0-8 | trace | 0.587 | 0.500 | 23/55 12/50 | 0/55 0/50 | 0.417 | 0.522±0.007 [3] |
| platform-channel-nouns | preresp_slot3 L9-18 | trace | 0.647 | 0.500 | 53/55 45/50 | 0/55 0/50 | 0.386 | 0.524±0.041 [9] |
| platform-channel-nouns | preresp_slot4 L9-18 | trace | 0.605 | 0.500 | 53/55 46/50 | 0/55 0/50 | 0.387 | 0.555±0.016 [5] |
| platform-channel-nouns | postresp_slot2 L0-8 | trace | 0.603 | 0.500 | 54/55 49/50 | 0/55 0/50 | 0.527 | 0.530±0.027 [10] |
| platform-channel-nouns | postresp_slot2 L9-18 | trace | 0.510 | 0.500 | 47/55 39/50 | 0/55 0/50 | 0.446 | --±-- [0] |
| platform-channel-nouns | postresp_slot3 L0-8 | trace | 0.505 | 0.550 | 14/55 12/50 | 22/55 15/50 | 0.429 | --±-- [0] |
| platform-channel-nouns | preans_slot1 L9-18 | elicited | 0.504 | 0.500 | 33/55 27/50 | 0/55 0/50 | 0.476 | 0.478±0.040 [4] |
| validity-words | preresp_slot2 L19-23 | trace | 0.613 | 0.588 | 29/55 19/50 | 35/55 23/50 | 0.419 | 0.556±0.018 [11] |
| validity-words | preresp_slot3 L19-23 | trace | 0.610 | 0.555 | 50/55 49/50 | 8/55 17/50 | 0.407 | 0.538±0.015 [11] |
| validity-words | preresp_slot4 L9-18 | trace | 0.596 | 0.500 | 18/55 26/50 | 0/55 0/50 | 0.382 | 0.559±0.009 [3] |
| apology-words | postresp_slot3 L9-18 | trace | 0.467 | 0.500 | 52/55 48/50 | 0/55 0/50 | 0.492 | --±-- [0] |
| apology-words | preans_slot2 L9-18 | elicited | 0.527 | 0.500 | 47/55 40/50 | 0/55 0/50 | 0.479 | --±-- [0] |
| discussion-analytic | preresp_slot1 L19-23 | trace | 0.580 | 0.569 | 24/55 26/50 | 14/55 19/50 | 0.447 | 0.535±0.018 [6] |
| discussion-analytic | preresp_slot3 L19-23 | trace | 0.575 | 0.597 | 55/55 50/50 | 52/55 48/50 | 0.378 | 0.507±0.013 [3] |
| fraud-reporting-zh | preans_slot1 L9-18 | elicited | 0.673 | 0.500 | 39/55 20/50 | 0/55 0/50 | 0.349 | 0.629±0.029 [16] |
| first-person | preresp_slot0 L9-18 | trace | 0.500 | 0.542 | 0/55 0/50 | 51/55 42/50 | 0.500 | --±-- [0] |
| first-person | preresp_slot3 L9-18 | trace | 0.500 | 0.523 | 0/55 0/50 | 52/55 45/50 | 0.500 | --±-- [0] |
| first-person | preresp_slot4 L19-23 | trace | 0.577 | 0.559 | 45/55 36/50 | 48/55 43/50 | 0.492 | 0.557±0.017 [5] |
| first-person | preresp_slot5 L9-18 | trace | 0.532 | 0.510 | 53/55 45/50 | 50/55 42/50 | 0.471 | --±-- [0] |
| first-person | preresp_slot5 L19-23 | trace | 0.564 | 0.563 | 55/55 48/50 | 55/55 49/50 | 0.421 | 0.486±0.012 [3] |
| first-person | q_last L9-18 | elicited | 0.500 | 0.547 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| first-person | q_last L19-23 | elicited | 0.591 | 0.595 | 41/55 34/50 | 55/55 50/50 | 0.401 | 0.478±0.038 [4] |
| wrongness-words-q-end | q_last L9-18 | elicited | 0.604 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.460 | 0.535±0.020 [8] |
| wrongness-words-q-end | q_last L19-23 | elicited | 0.609 | 0.500 | 35/55 39/50 | 0/55 0/50 | 0.396 | 0.471±0.022 [2] |
| claims-statements | preresp_slot1 L9-18 | trace | 0.500 | 0.544 | 0/55 0/50 | 40/55 32/50 | 0.500 | --±-- [0] |
| claims-statements | preans_slot1 L9-18 | elicited | 0.550 | 0.644 | 11/55 5/50 | 46/55 39/50 | 0.501 | 0.480±0.001 [2] |
| claims-statements | q_last L0-8 | elicited | 0.500 | 0.530 | 0/55 0/50 | 26/55 21/50 | 0.500 | --±-- [0] |
| quote-openers | preresp_slot0 L9-18 | trace | 0.597 | 0.500 | 50/55 45/50 | 0/55 0/50 | 0.414 | 0.512±0.007 [3] |
| quote-openers | preresp_slot5 L0-8 | trace | 0.478 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.524 | 0.475±0.000 [1] |
| quote-openers | preresp_slot5 L9-18 | trace | 0.609 | 0.500 | 47/55 41/50 | 0/55 0/50 | 0.442 | 0.533±0.049 [11] |
| quote-openers | postresp_slot3 L9-18 | trace | 0.443 | 0.500 | 55/55 49/50 | 0/55 0/50 | 0.512 | --±-- [0] |


## gpt-oss-20b  (export exports/gpt_oss_20b; judge labels; primary lens LL, twin J)

### [stage 1] cell stage1_pf: 55 lie / 50 truth items from 51 / 49 effective scenarios (sources pf; 3 label-excluded; conditioning: UNCONDITIONAL on self-report; interpretation restricted to trace addresses (P6), elicited rows diagnostic)
| family | address | era | LL | J | LL-vis l/t | J-vis l/t | companion | CV |
|---|---|---|---|---|---|---|---|---|
| reply-answer-words | preresp_slot0 L9-18 | trace | 0.520 | 0.537 | 35/55 32/50 | 54/55 49/50 | 0.450 | 0.541±0.017 [5] |
| reply-answer-words | preresp_slot0 L19-23 | trace | 0.500 | 0.612 | 0/55 0/50 | 52/55 42/50 | 0.500 | --±-- [0] |
| reply-answer-words | preresp_slot1 L9-18 | trace | 0.549 | 0.578 | 30/55 22/50 | 53/55 49/50 | 0.464 | 0.514±0.039 [3] |
| reply-answer-words | preresp_slot4 L19-23 | trace | 0.456 | 0.516 | 12/55 15/50 | 55/55 50/50 | 0.534 | --±-- [0] |
| reply-answer-words | postresp_slot0 L9-18 | trace | 0.521 | 0.561 | 48/55 38/50 | 50/55 42/50 | 0.463 | --±-- [0] |
| reply-answer-words | postresp_slot2 L9-18 | trace | 0.639 | 0.567 | 55/55 49/50 | 55/55 50/50 | 0.403 | 0.553±0.028 [10] |
| reply-answer-words | postresp_slot2 L19-23 | trace | 0.626 | 0.633 | 31/55 15/50 | 55/55 50/50 | 0.368 | 0.597±0.033 [8] |
| chat-conversation-words | preresp_slot0 L19-23 | trace | 0.485 | 0.556 | 6/55 7/50 | 52/55 38/50 | 0.473 | --±-- [0] |
| chat-conversation-words | preresp_slot1 L19-23 | trace | 0.530 | 0.548 | 39/55 32/50 | 52/55 44/50 | 0.559 | --±-- [0] |
| chat-conversation-words | preresp_slot2 L0-8 | trace | 0.500 | 0.563 | 55/55 50/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| chat-conversation-words | preresp_slot3 L9-18 | trace | 0.573 | 0.528 | 52/55 40/50 | 52/55 45/50 | 0.470 | 0.538±0.017 [5] |
| chat-conversation-words | postresp_slot0 L9-18 | trace | 0.586 | 0.706 | 49/55 38/50 | 55/55 50/50 | 0.417 | 0.509±0.004 [4] |
| chat-conversation-words | postresp_slot1 L9-18 | trace | 0.559 | 0.549 | 41/55 31/50 | 55/55 50/50 | 0.457 | --±-- [0] |
| chat-conversation-words | postresp_slot1 L19-23 | trace | 0.555 | 0.555 | 52/55 45/50 | 55/55 48/50 | 0.464 | --±-- [0] |
| chat-conversation-words | postresp_slot2 L9-18 | trace | 0.490 | 0.605 | 55/55 50/50 | 55/55 50/50 | 0.491 | --±-- [0] |
| comment-words | preresp_slot0 L9-18 | trace | 0.500 | 0.518 | 0/55 0/50 | 53/55 45/50 | 0.500 | --±-- [0] |
| comment-words | preresp_slot1 L19-23 | trace | 0.584 | 0.515 | 55/55 50/50 | 55/55 50/50 | 0.398 | 0.496±0.026 [7] |
| comment-words | preresp_slot3 L19-23 | trace | 0.489 | 0.588 | 55/55 50/50 | 55/55 50/50 | 0.490 | --±-- [0] |
| comment-words | preresp_slot4 L19-23 | trace | 0.551 | 0.538 | 47/55 38/50 | 51/55 42/50 | 0.470 | 0.478±0.015 [2] |
| comment-words | postresp_slot0 L9-18 | trace | 0.500 | 0.568 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| comment-words | postresp_slot2 L19-23 | trace | 0.469 | 0.515 | 15/55 16/50 | 53/55 47/50 | 0.537 | --±-- [0] |
| dialogue-role-nouns | preresp_slot0 L9-18 | trace | 0.500 | 0.543 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| dialogue-role-nouns | preresp_slot1 L9-18 | trace | 0.449 | 0.539 | 1/55 6/50 | 55/55 50/50 | 0.548 | --±-- [0] |
| dialogue-role-nouns | preresp_slot1 L19-23 | trace | 0.493 | 0.563 | 46/55 43/50 | 55/55 50/50 | 0.515 | --±-- [0] |
| dialogue-role-nouns | preresp_slot2 L0-8 | trace | 0.523 | 0.555 | 30/55 25/50 | 55/55 50/50 | 0.515 | 0.405±0.000 [1] |
| dialogue-role-nouns | preresp_slot2 L9-18 | trace | 0.470 | 0.583 | 11/55 13/50 | 55/55 50/50 | 0.502 | --±-- [0] |
| dialogue-role-nouns | postresp_slot1 L9-18 | trace | 0.549 | 0.536 | 12/55 6/50 | 55/55 50/50 | 0.444 | 0.481±0.000 [1] |
| dialogue-role-nouns | postresp_slot1 L19-23 | trace | 0.580 | 0.633 | 55/55 50/50 | 55/55 50/50 | 0.420 | 0.471±0.030 [5] |
| dialogue-role-nouns | preans_slot1 L19-23 | elicited | 0.527 | 0.547 | 55/55 50/50 | 55/55 50/50 | 0.465 | 0.497±0.015 [2] |
| question-asking-words | preresp_slot0 L9-18 | trace | 0.568 | 0.550 | 54/55 47/50 | 53/55 48/50 | 0.439 | 0.528±0.029 [5] |
| question-asking-words | preresp_slot1 L9-18 | trace | 0.522 | 0.513 | 29/55 26/50 | 35/55 27/50 | 0.536 | --±-- [0] |
| question-asking-words | postresp_slot1 L9-18 | trace | 0.568 | 0.515 | 17/55 9/50 | 5/55 3/50 | 0.409 | 0.499±0.005 [2] |
| question-asking-words | postresp_slot2 L9-18 | trace | 0.449 | 0.507 | 55/55 50/50 | 54/55 50/50 | 0.511 | --±-- [0] |
| question-asking-words | postresp_slot2 L19-23 | trace | 0.510 | 0.414 | 55/55 50/50 | 22/55 26/50 | 0.576 | --±-- [0] |
| question-asking-words | postresp_slot3 L9-18 | trace | 0.495 | 0.609 | 33/55 33/50 | 54/55 46/50 | 0.598 | 0.426±0.000 [1] |
| question-asking-words | postresp_slot3 L19-23 | trace | 0.500 | 0.532 | 0/55 0/50 | 17/55 13/50 | 0.500 | --±-- [0] |
| question-asking-words | q_last L9-18 | elicited | 0.571 | 0.500 | 51/55 40/50 | 55/55 50/50 | 0.434 | 0.508±0.010 [3] |
| honesty-words-q-end | q_last L19-23 | elicited | 0.505 | 0.604 | 5/55 4/50 | 49/55 44/50 | 0.472 | --±-- [0] |
| honesty-words-pre-answer | preans_slot1 L9-18 | elicited | 0.559 | 0.574 | 45/55 38/50 | 13/55 19/50 | 0.412 | 0.440±0.032 [3] |
| honesty-words-pre-answer | preans_slot1 L19-23 | elicited | 0.615 | 0.591 | 3/55 14/50 | 9/55 16/50 | 0.436 | 0.591±0.018 [13] |
| negated-auxiliaries | postresp_slot3 L0-8 | trace | 0.500 | 0.579 | 0/55 0/50 | 35/55 25/50 | 0.500 | --±-- [0] |
| negated-auxiliaries | postresp_slot3 L9-18 | trace | 0.500 | 0.679 | 0/55 0/50 | 54/55 49/50 | 0.500 | --±-- [0] |
| negated-auxiliaries | postresp_slot3 L19-23 | trace | 0.509 | 0.559 | 1/55 0/50 | 25/55 17/50 | 0.491 | --±-- [0] |
| negated-auxiliaries | q_last L19-23 | elicited | 0.500 | 0.545 | 0/55 0/50 | 30/55 25/50 | 0.500 | --±-- [0] |
| pretense-irony | preresp_slot1 L0-8 | trace | 0.500 | 0.600 | 0/55 0/50 | 22/55 10/50 | 0.500 | --±-- [0] |
| pretense-irony | postresp_slot2 L9-18 | trace | 0.500 | 0.632 | 0/55 0/50 | 53/55 48/50 | 0.500 | --±-- [0] |
| pretense-irony | postresp_slot3 L9-18 | trace | 0.500 | 0.585 | 0/55 0/50 | 40/55 27/50 | 0.500 | --±-- [0] |
| speech-act-gerunds | postresp_slot2 L9-18 | trace | 0.545 | 0.579 | 49/55 40/50 | 55/55 50/50 | 0.479 | --±-- [0] |
| greetings-politeness | preresp_slot5 L9-18 | trace | 0.574 | 0.627 | 22/55 14/50 | 26/55 10/50 | 0.439 | 0.550±0.014 [7] |
| greetings-politeness | preresp_slot5 L19-23 | trace | 0.639 | 0.641 | 43/55 35/50 | 44/55 36/50 | 0.409 | 0.540±0.030 [11] |
| emphatic-affirmation | preresp_slot5 L19-23 | trace | 0.582 | 0.576 | 45/55 33/50 | 46/55 34/50 | 0.489 | 0.534±0.000 [1] |
| emphatic-affirmation | postresp_slot3 L9-18 | trace | 0.480 | 0.557 | 0/55 2/50 | 31/55 20/50 | 0.519 | --±-- [0] |
| emphatic-affirmation | postresp_slot3 L19-23 | trace | 0.552 | 0.522 | 51/55 47/50 | 53/55 49/50 | 0.454 | 0.476±0.003 [2] |
| ai-eval-awareness | preresp_slot1 L9-18 | trace | 0.547 | 0.470 | 30/55 23/50 | 11/55 13/50 | 0.528 | --±-- [0] |
| ai-eval-awareness | preresp_slot3 L0-8 | trace | 0.573 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.407 | 0.485±0.000 [1] |
| ai-eval-awareness | preresp_slot3 L9-18 | trace | 0.564 | 0.525 | 55/55 50/50 | 50/55 43/50 | 0.483 | 0.532±0.017 [6] |
| ai-eval-awareness | preresp_slot5 L0-8 | trace | 0.547 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.464 | --±-- [0] |
| ai-eval-awareness | preresp_slot5 L9-18 | trace | 0.552 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.513 | --±-- [0] |
| ai-eval-awareness | q_last L0-8 | elicited | 0.545 | 0.500 | 38/55 30/50 | 0/55 0/50 | 0.468 | --±-- [0] |
| privacy-disclaimer | preresp_slot0 L9-18 | trace | 0.500 | 0.548 | 0/55 0/50 | 42/55 37/50 | 0.500 | --±-- [0] |
| privacy-disclaimer | preresp_slot2 L9-18 | trace | 0.500 | 0.560 | 0/55 0/50 | 53/55 49/50 | 0.500 | --±-- [0] |
| privacy-disclaimer | preresp_slot2 L19-23 | trace | 0.500 | 0.471 | 0/55 0/50 | 53/55 48/50 | 0.500 | --±-- [0] |
| privacy-disclaimer | preresp_slot3 L19-23 | trace | 0.500 | 0.562 | 0/55 0/50 | 35/55 25/50 | 0.500 | --±-- [0] |
| privacy-disclaimer | preans_slot1 L9-18 | elicited | 0.499 | 0.589 | 1/55 1/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| privacy-disclaimer | preans_slot2 L9-18 | elicited | 0.500 | 0.545 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| platform-channel-nouns | preresp_slot1 L9-18 | trace | 0.507 | 0.548 | 3/55 2/50 | 52/55 43/50 | 0.491 | --±-- [0] |
| platform-channel-nouns | preresp_slot3 L0-8 | trace | 0.500 | 0.587 | 0/55 0/50 | 23/55 12/50 | 0.500 | --±-- [0] |
| platform-channel-nouns | preresp_slot3 L9-18 | trace | 0.500 | 0.647 | 0/55 0/50 | 53/55 45/50 | 0.500 | --±-- [0] |
| platform-channel-nouns | preresp_slot4 L9-18 | trace | 0.500 | 0.605 | 0/55 0/50 | 53/55 46/50 | 0.500 | --±-- [0] |
| platform-channel-nouns | postresp_slot2 L0-8 | trace | 0.500 | 0.603 | 0/55 0/50 | 54/55 49/50 | 0.500 | --±-- [0] |
| platform-channel-nouns | postresp_slot2 L9-18 | trace | 0.500 | 0.510 | 0/55 0/50 | 47/55 39/50 | 0.500 | --±-- [0] |
| platform-channel-nouns | postresp_slot3 L0-8 | trace | 0.550 | 0.505 | 22/55 15/50 | 14/55 12/50 | 0.437 | 0.437±0.025 [2] |
| platform-channel-nouns | preans_slot1 L9-18 | elicited | 0.500 | 0.504 | 0/55 0/50 | 33/55 27/50 | 0.500 | --±-- [0] |
| validity-words | preresp_slot2 L19-23 | trace | 0.588 | 0.613 | 35/55 23/50 | 29/55 19/50 | 0.486 | 0.522±0.015 [5] |
| validity-words | preresp_slot3 L19-23 | trace | 0.555 | 0.610 | 8/55 17/50 | 50/55 49/50 | 0.453 | 0.512±0.017 [3] |
| validity-words | preresp_slot4 L9-18 | trace | 0.500 | 0.596 | 0/55 0/50 | 18/55 26/50 | 0.500 | --±-- [0] |
| apology-words | postresp_slot3 L9-18 | trace | 0.500 | 0.467 | 0/55 0/50 | 52/55 48/50 | 0.500 | --±-- [0] |
| apology-words | preans_slot2 L9-18 | elicited | 0.500 | 0.527 | 0/55 0/50 | 47/55 40/50 | 0.500 | --±-- [0] |
| discussion-analytic | preresp_slot1 L19-23 | trace | 0.569 | 0.580 | 14/55 19/50 | 24/55 26/50 | 0.430 | 0.516±0.002 [3] |
| discussion-analytic | preresp_slot3 L19-23 | trace | 0.597 | 0.575 | 52/55 48/50 | 55/55 50/50 | 0.393 | 0.513±0.013 [5] |
| fraud-reporting-zh | preans_slot1 L9-18 | elicited | 0.500 | 0.673 | 0/55 0/50 | 39/55 20/50 | 0.500 | --±-- [0] |
| first-person | preresp_slot0 L9-18 | trace | 0.542 | 0.500 | 51/55 42/50 | 0/55 0/50 | 0.480 | --±-- [0] |
| first-person | preresp_slot3 L9-18 | trace | 0.523 | 0.500 | 52/55 45/50 | 0/55 0/50 | 0.537 | --±-- [0] |
| first-person | preresp_slot4 L19-23 | trace | 0.559 | 0.577 | 48/55 43/50 | 45/55 36/50 | 0.489 | 0.557±0.017 [5] |
| first-person | preresp_slot5 L9-18 | trace | 0.510 | 0.532 | 50/55 42/50 | 53/55 45/50 | 0.440 | --±-- [0] |
| first-person | preresp_slot5 L19-23 | trace | 0.563 | 0.564 | 55/55 49/50 | 55/55 48/50 | 0.434 | 0.492±0.020 [3] |
| first-person | q_last L9-18 | elicited | 0.547 | 0.500 | 55/55 50/50 | 0/55 0/50 | 0.426 | 0.465±0.000 [1] |
| first-person | q_last L19-23 | elicited | 0.595 | 0.591 | 55/55 50/50 | 41/55 34/50 | 0.395 | 0.494±0.045 [4] |
| wrongness-words-q-end | q_last L9-18 | elicited | 0.500 | 0.604 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| wrongness-words-q-end | q_last L19-23 | elicited | 0.500 | 0.609 | 0/55 0/50 | 35/55 39/50 | 0.500 | --±-- [0] |
| claims-statements | preresp_slot1 L9-18 | trace | 0.544 | 0.500 | 40/55 32/50 | 0/55 0/50 | 0.456 | --±-- [0] |
| claims-statements | preans_slot1 L9-18 | elicited | 0.644 | 0.550 | 46/55 39/50 | 11/55 5/50 | 0.429 | 0.630±0.040 [18] |
| claims-statements | q_last L0-8 | elicited | 0.530 | 0.500 | 26/55 21/50 | 0/55 0/50 | 0.472 | --±-- [0] |
| quote-openers | preresp_slot0 L9-18 | trace | 0.500 | 0.597 | 0/55 0/50 | 50/55 45/50 | 0.500 | --±-- [0] |
| quote-openers | preresp_slot5 L0-8 | trace | 0.500 | 0.478 | 0/55 0/50 | 55/55 50/50 | 0.500 | --±-- [0] |
| quote-openers | preresp_slot5 L9-18 | trace | 0.500 | 0.609 | 0/55 0/50 | 47/55 41/50 | 0.500 | --±-- [0] |
| quote-openers | postresp_slot3 L9-18 | trace | 0.500 | 0.443 | 0/55 0/50 | 55/55 49/50 | 0.500 | --±-- [0] |
