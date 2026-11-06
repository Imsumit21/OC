## Independent review rounds
Round 1 ran seven independent reviewers (GPT-6.1 Sol: full reviewers F2 and F3, deep-recheck passes R1+R5, R2, R3, R4+R7,
R6) on the 75-row draft under Evals/3_Rubrics_Eval.md and rubric_flow_v2.md. Every finding was checked against its cited
record or rule and merged (no voting). Row numbers below are the 75-row draft's.
| Round-1 item | Raised by | Decision | Repair in this JSON |
|---|---|---|---|
| Evidence cells for ZOM-435 and ZOM-562 accepted a bare name or subject, while the How we gate tab defines evidence as 'id or link of the record that decides the row' | F2, F3, R5 | accepted (overly_broad, Major) | the ZOM-435 row names the card id, short link and comment id; the ZOM-562 evidence row was later replaced by a ZOM-563 row whose deciding record (the DM) has a message id the runs cite |
| Repro row accepted steps without the launch | F2, F3 | accepted (overly_broad, Major) | the title lists the four steps from f_5e40215b7d4d24b0455412, launch included |
| The 133-row count did not reject ZOM-570, ZOM-359 or ZOM-475 in place of an in-scope ticket | F2, F3, R3, R5 | accepted (missing control) | the count row carries Leonard's scope and its exclusions as the cohort qualifier |
| No wrong-target guard for the register cells, the ZOM-570 description, extra spreadsheet tabs, or a QA call in another thread | F2, F3, R3 | accepted (missing_coverage, Major) | rows for one new tab in ZM3D Release Gate only, register rows only in that tab, the blocker list on ZOM-570 and no other description, the QA call only in Arthur's thread |
| No row graded 'before Friday's go/no-go' | F2, F3, R3 | accepted (missing_coverage, Major) | a timing row bound to evt_81e6dc4dbfd331f1a6a317 (2025-10-03T16:00:00Z) |
| Non-blocker call rows (10 FIXED, 2 KNOWN ISSUE, 3 NO CALL) exceeded five samples of one property on one output | F2, R4 | accepted (duplicate, Moderate) | five samples plus three authority-decided exceptions (Leonard's two rulings, the server fix confirmed on prod); six rows sampled out |
| The QA-could-not-reproduce branch of 'in candidate' had no build-status row | R3 | accepted (missing coverage of an exception) | a ZOM-429 build status row |
| QA result rows required symptom prose the sheet does not ask for | R1 | accepted (overly_specific, Major) | the rows grade a failed or reproduced latest check (ZOM-559 also accepts 'not re-tested on #135 / #50') |
| Device and OS rows' evidence narrowed acceptance to the title or description | R1 | accepted (overly_specific, Major) | a comment the Agent adds on the new issue also passes |
| ZOM-558 call and the one-new-issue count weighted 3 | R6, F2 | accepted (weight) | both weight 5 (multi-source reconciliation) |
| Evidence for ZOM-569 tied the change text to the #2028 Started post | R2 | accepted (incorrect attribution) | the Changes post C05433XK267/1759268589.049939 is named |
| Runbook side procedures: link the bug on the runbook page, mirror to the Customer Support Playbook, mark or post the matrix, link the matrix from ZOM-570 | F2 | rejected | the platform /prompt report: 'The QA Regression Runbook's checks are incorporated only for the new-ticket ask'; Vincent is a reader on f_b91db376f65604b8602657; the OE (PASS) performs none of them; a row would be unauthorized |
| Replace the 19-blocker count by one row naming all 19 keys; merge the one-issue count into the issue row | R5 | rejected | Eval 3 2.2 (an id list bundles independently variable members); the frederick task's /rubric round 1 flagged a count bundled with an identity as non_atomic; the scope checklist allows a count condition on the required write; a right count over a wrong set needs two cancelling errors (QC B11) |

Round 2 ran five passes (R1+R5, R2, R3, R4+R7, R6) on the 72-row revision plus an independent script recount of the
population (DeepSeek, own Python over linear data.json and the seeded issues: 112 open + 20 Done after
2025-09-22T12:30:43Z = 132, plus the filed ticket = 133; no Done ticket between the #127 and #40 starts or earlier that
day). Round 3 ran a fresh full review (no confirmed defect on 71 rows) and a once-over of every changed row.
| Round-2/3 item | Raised by | Decision | Repair in this JSON |
|---|---|---|---|
| Call-column samples still six under the reading that only Leonard's rulings are exceptions | R4 (round 2) | accepted (duplicate, Moderate) | the ZOM-434 sample removed; G1 now holds five samples (ZOM-429, ZOM-563, ART-793, ZOM-481, ZOM-536) and two direct exceptions (ZOM-558, ZOM-477) |
| Repro row's acceptance left out the issue title | R1, R6 (round 2) | accepted (overly_specific) | the title, description or a comment on the new issue passes |
| 'Every message carrying the QA call' also caught the final chat answer | R1 (round 2) | accepted (overly_specific) | the restriction applies to Slack messages only |
| Tab name passed with the platforms swapped | R5 (round 2) | accepted (overly_broad) | platform labels, when present, must pair 135 with Android and 50 with iOS |
| Count row title lacked the open-state definition and the cut instant | R6 (round 2) | accepted (not_self_contained) | 'whose state is anything but Done, Canceled or Duplicate' and 'Android Submission #127 Started 2025-09-22 12:30:43 UTC' in the title |
| ZOM-477 build status n/a weighted 1 | R6 (round 2) | accepted (weight) | weight 3 (the ruling mapped through the sheet's definition) |
| The timing row could pass on a top-level post before the deadline | R-1 (round 3) | accepted (overly_broad) | the timing row grades the reply in Arthur's thread |
| ZOM-473 build-status reasoning said no record shows the fix landing later | parallel OE revision (OE 25) | accepted (precision) | names the #1974 change 'Adding input blocker during Level-end animations' (2025-09-24, before both Started lines) |
| Exact-set rows for the 19 blockers and a merged count+identity issue row | R5 (round 2) | rejected | Eval 3 2.2 bundling; the scope checklist's count condition; QC B11 (none of 13 recorded Opus runs listed an extra ticket or filed a second issue) |
| Lower ZOM-473, the new-ticket call and ZOM-563 to weight 3 | R6 (round 2) | rejected | each reconciles a Linear state with a record in another service (Turkish DM, Confluence runbook plus Brian's doc, the Douglas DM): QC C20 multi-source; round-1 R6 cleared the same weights |
| An ordinary-case evidence sample | F4 (round 3, UNSURE) | not scored | a weak sample choice is a note (Eval 3 3.6); both samples sit where the evidence column decides something (Trello re-test, prod DM) |
