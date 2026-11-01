# 08 OE Check — Frederick account handover register (fs-account-custody)
Checked 2026-10-26 · Events 39 · Characters 17119 (300–50,000: ok) · Ledger 2026-10-26
/oe prediction (a prediction only; /oe gives the verdict): PASS 5
Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

Format: every event is `OE <n>  <purpose and where to look> (<parameters>)` with an indented `Expected:` line carrying the returned or produced values and, where one exists, the trap (user-required format, 2026-10-26).

Fixed before this check (Claude-drafted events, revised in this run):
- OE 10 named the ad account id 907669287942378. On the receipt it shows only as "[IDENTIFIER_3125]" in the subject (the number sits base64-encoded in a link), so it is not observable at that precision on the tool path. Removed; the line now states $0.05 billed for ad costs on Sep 15 2025, campaign ZM_UK_CPE_CopyAds.
- OE 15 said "one more as User". It now reads "one unnamed account as User" (Users tab row with an empty name and EMPLOYEE_0032_EMAIL).
- OE 30 had no search parameters. It now names the searches (receipt, invoice, payment, billing, after:2025/09/01 before:2025/10/01).
- /oe run 2 (NON-FAIL 3, Accuracy 3: two MINOR) fixes: OE 27 trap no longer calls Arthur's #executives summary wrong for Instagram (it is right there: C07C2866011/1759266627.118342 vs frederick.stone@harmonygames.co/1843339075781206004); OE 30 now lists the actual September TikTok mail (TikTok Shop marketing, the Sep 18 partner reminder, two Sep 29 verification codes, the Sep 29 "You have 50 new followers" notice), re-read from Frederick's mailbox, none a bill.
- OE 3, 7, 33, 39 headings now end with their parameters in parentheses; traps added to OE 3, 5, 6, 7, 8, 9, 13, 18, 20, 21, 23, 26, 27.

## Inventory
| Segment (quoted start) | Role | Event |
|---|---|---|
| "OE 1  Read Leonard's handover ask in Slack" | STEP | 1 |
| "OE 2  Open the thread under that message" | STEP | 2 |
| "OE 3  Find Arthur's handover rules for marketing" | STEP | 3 |
| "OE 4  Read the comment on that card" | STEP | 4 |
| "OE 5  Find Arthur's follow-up email" | STEP | 5 |
| "OE 6  Read Leonard's money-moving definition" | STEP | 6 |
| "OE 7  Find Arthur's sweep in Drive" | STEP | 7 |
| "OE 8  Check the status of AdMob pub-2341961509332343" | STEP | 8 |
| "OE 9" … "OE 30" (exports, notices, money evidence) | STEP | 9–30 |
| "OE 31  Apply the card's rules" | STEP (analysis, no tool) | 31 |
| "OE 32  Find the Company Ops folder" | STEP | 32 |
| "OE 33  Create the register as a new Google Sheet" | STEP (write) | 33 |
| "OE 34  Move the new spreadsheet into the Company Ops folder" | STEP (write) | 34 |
| "OE 35  Write the register into the sheet" | STEP (write) | 35 |
| "OE 36  Reply to Leonard in the DM" | STEP (write) | 36 |
| "OE 37  Find Fred's \"Lock up social handles and domain?\" card" | STEP | 37 |
| "OE 38  Add a checklist to that card" | STEP (write) | 38 |
| "OE 39  Add the X account as an item on that checklist" | STEP (write) | 39 |

No CONTEXT, RESPONSE_DESCRIPTION or NON_ACTION segments. All 39 STEPs carry action, information, tool/service, parameters (in parentheses) and expected data; dependencies are stated where an event uses an earlier result (OE 2 → 1, 4 → 3, 24 → 23, 31 → 3–30, 34 → 32/33, 38 → 37, 39 → 38).

## Coverage
| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 (F1, F2) | OE 1, 2 | Covered | Ledger |
| R2 (F3, F7, F8) | OE 3, 7, 8 | Covered — population derived (17 files → rule 1 → 13) before any per-account step | Ledger |
| R3 (F9, F11–F13, F15, F17, F19, F21–F29) | OE 9, 11, 12, 13, 15, 17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29 | Covered — every tab and the three notices | Ledger |
| R4 (F2, F6, F10, F14, F16, F18, F20, F30) | OE 2, 6, 10, 14, 16, 18, 20, 30 | Covered — money for all 13 | Ledger |
| R5 (F3, F4, F5, F33) | OE 3, 4, 5, 31 | Covered — analysis event OE 31 joins discovery to the writes | Ledger |
| R6 (F31, F33) | OE 32, 33, 34, 35 | Covered — create, move, write rows | Ledger; gdrive_create_file with parentId is another valid route for 33+34 |
| R7 (F1, F34) | OE 36 | Covered — sent in the DM, content = TRANSFER count + outside access | Ledger |
| R8 (F3, F32, F33) | OE 37, 38, 39 | Covered — checklist on the existing card, X item | Ledger |
| R9 (F1) | OE 36, 38, 39 executed without a confirmation step | Covered | Ledger |

## Expected-data sign-off
| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Match / minor / wrong / unresolved |
|---|---|---|---|---|
| OE 1 | "Tue Sep 30 2025 3:40 PM PT (22:40 UTC)" | SQL L137, D05S58U4SAK/1759272012.507134 (created_at 2025-09-30T22:40:12Z) | text and time as quoted | Match |
| OE 2 | "Sep 30 2025 3:48 PM PT (22:48 UTC)" | SQL L139, D05S58U4SAK/1759272498.304117 | as quoted | Match |
| OE 3 | "(#456), created by Arthur Sep 30 2025 1:41 PM PT (20:41 UTC)" | SQL L141, L143; trello 68dc406c7b0d03e53b334bab | idShort 456; createCard 2025-09-30T20:41:16Z; rules 1–7 as summarised | Match |
| OE 4 | "Sep 30 2025 2:58 PM PT (21:58 UTC)" | SQL L149; trello 68dc529406d8087e5a6b8403 | 2025-09-30T21:58:44Z, text as quoted | Match |
| OE 5 | "Sep 30 2025 4:21 PM PT (23:21 UTC)" | SQL L154; frederick.stone@harmonygames.co/1844732985606656293 | date 23:21:09Z; body as quoted | Match |
| OE 6 | "last modified Sep 30 2025 10:48 AM PT" | SQL L127; f_c612c0e68a27b3330eb46a modified 2025-09-30T17:48:00Z | definition text as summarised | Match |
| OE 7 | "created Sep 30 2025 12:50 PM PT, 17 spreadsheets" | SQL L2–L113; d_6cae3483dd469c189a528e | 17 children, titles as listed | Match |
| OE 8 | "Sun Aug 24 2025 8:07 AM PT" | hg.py get-many gmail threads/frederick@harmonygames.co_1841349862518331350.json /messages/0; frederick.stone@harmonygames.co/1841349862518331350 | date 2025-08-24T08:07:51-07:00; pub-2341961509332343 deactivated | Match |
| OE 9 | "Node Media LLC, Partner admin (manage campaigns, billing view), shared by Frederick 2024-10-07" | SQL L11, L13; f_f7e7c5bf089029cee91175 | as quoted; four Admins on People | Match |
| OE 10 | "$0.05 billed for ad costs on Sep 15 2025, campaign ZM_UK_CPE_CopyAds" | hg.py get-many gmail frederick.stone@harmonygames.co/1843428112007517388 /messages/0 | Amount billed $0.05, Sep 15 2025, ZM_UK_CPE_CopyAds; sent Sep 16 06:40 PDT | Match |
| OE 11 | "Enabled campaigns 0; Leonard Hayes Admin (added 2024-09-20) and Frederick Stone Admin (2024-10-07)" | SQL L19, L21; f_ab70b02c329d038a72fb9f | as quoted | Match |
| OE 12 | "Robert, Leonard Hayes, Arthur Blake and Frederick Stone all Admin" | SQL L27, L29; f_63b42f52fa11d7df238a4e | as quoted; Calm Play LLC; 0 campaigns | Match |
| OE 13 | "Node Media LLC Admin since 2024-12-05" | SQL L35, L37; f_1191b7f8c96419e1f4dc88 | as quoted; Fred Manager on Members | Match |
| OE 14 | "Mon Sep 29 2025 3:48 PM PT" | hg.py get-many slack C07C2866011 2025-09 /1166, /1191; C07C2866011/1759186080.203099 | ts 1759186080 = 15:48 PDT; text as quoted | Match |
| OE 15 | "Arthur Blake, Brian Foster and one unnamed account as User" | SQL L43; f_3996bca752549d3512bfbc | five rows, two Admin | Match |
| OE 16 | "Sun Sep 14 2025 12:33 AM PT" … "Ref Pub1020673667" | hg.py get-many gmail frederick.stone@harmonygames.co/1843223812315546201 /messages/0 | 2025-09-14T07:33:27Z; text as quoted | Match |
| OE 17 | "Frederick Stone Admin, Leonard Hayes Admin" | SQL L49; f_a552317a929102385c0393 | as quoted | Match |
| OE 18 | "Sep 8 9:41 AM PT: \"I can confirm you will not be responsible for the cost of those installs.\"" | hg.py get-many slack C07UCC631A6 2025-09 /2–/6; C07UCC631A6/1757349668.681539 | ts 1757349668 = 09:41 PDT; pause at 09:06 PDT | Match |
| OE 19 | "Leonard Hayes Admin (account owner) since 2025-03-03" | SQL L55; f_50ff132ac88169019feeca | as quoted | Match |
| OE 20 | "admob paid $38.70; applovin paid $136.33; meta_audience paid $26.15" | snowflake.json /tables/35 re-aggregated (Decimal) | 38.6967 / 136.3291 / 26.1544; unity 43.2629 and ironsource 27.0798 accrued_unpaid | Match |
| OE 21 | "@harmonygames.app deactivated 2025-09-29" | SQL L67; f_2f0abe2f1f6726fef63f80 | "Deactivated 2025-09-29 (deletion pending)" | Match |
| OE 22 | "Thu Sep 18 2025 10:12 AM PT" | SQL L192; frederick.stone@harmonygames.co/1843622639043434721 | 17:12:40Z; partner, Admin, Oct 8, 2024 | Match |
| OE 23 | "removed 2024-12-20 by Frederick" | SQL L73, L75; f_fc27672c5bfea8b760b074 | as quoted | Match |
| OE 24 | "Tue Sep 9 2025 8:42 AM PT" | SQL L188; frederick.stone@harmonygames.co/1842801580966444617 | 15:42:18Z; [EMAIL_126620] Owner | Match |
| OE 25 | "all Super admin" | SQL L81; f_b89c1c70489f81031bdd4f | four Super admins | Match |
| OE 26 | "\"no delegates set up\"" | SQL L87; f_99d66f33c54338e70f5ed2 | as quoted | Match |
| OE 27 | "\"Fred's personal gmail, not harmonygames.co. Login only\"" | SQL L93; f_215ff8da73e4173f78515c | as quoted | Match |
| OE 28 | "Mon Sep 15 2025 7:05 AM PT" | SQL L196; frederick.stone@harmonygames.co/1843339075781206004 | 14:05:33Z; Leonard Jan 22, 2024, Fred Sep 5, 2024; partners none | Match |
| OE 29 | "Leonard Hayes Owner, Frederick Stone Admin, Robert Admin" | SQL L99; f_2cecf2f81045ec401feb61 | as quoted | Match |
| OE 30 | "No receipt, invoice or payout for any of them in September 2025" (TikTok list: "two Sep 29 account verification codes") | mailbox scan of HarmonyGames_Gmail threads/frederick@harmonygames.co_* for Sep 2025 (receipt, invoice, payment, billing, billed, payout); frederick.stone@harmonygames.co/1843428112007517388 | only Meta (receipt, Audience Network document and remittance) and AppLovin (two payout notices) | Match |
| OE 31 | "Totals: REVOKE 4, TRANSFER 1, KEEP 5, CLOSE 3" | ledger F33, recomputed from SQL L11–L99 under trello 68dc406c7b0d03e53b334bab rules + 68dc529406d8087e5a6b8403 + frederick.stone@harmonygames.co/1844732985606656293 | 13 rows as listed | Match |
| OE 32 | "created Sep 30 2025 3:31 PM PT" | SQL L129; d_21f9e11d43739eaef26b38 | 22:31Z, Fred writer; no other "Company Ops" in base (hg.py search gdrive "Company Ops": 0) | Match |
| OE 36 | "Node Media LLC still has access to 4 accounts" | ledger F34; D05S58U4SAK/1759272012.507134 | Meta, Unity Ads advertiser, YouTube Brand Account, TikTok | Match |
| OE 37 | "Card #40 in list \"ZM 3d Technical Launch / Alpha\", created Mar 10 2025" | hg.py get trello data.json /cards/671; trello 67cf1b506d78ad3c72e02a35 | idShort 40; createCard 2025-03-10T17:03:12Z; checkItems 0 | Match |

## Findings
| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |
|---|---|---|---|---|---|---|---|

None open. The three defects found in this run (OE 10 id precision, OE 15 vague count, OE 30 missing parameters) were fixed in 08_Oracle_Events.md before this check; see the list above.

## Pre-verdict sweep
| Eval 4.0 check (7) | Result |
|---|---|
| One wrong count / ID / channel / tool | None: counts (17 files, 13 accounts, 4 REVOKE, 1 TRANSFER, 5 KEEP, 3 CLOSE, 4 Node accounts) re-derived from the SQL rows; tools are cataloged (gsheets_create_spreadsheet, gdrive_move_file, gsheets_values_update, slack_send_message, trello_create_checklist, trello_create_check_item) |
| One missing write | None: Sheet create, move, values, DM reply, checklist, check item each have an event (OE 33–36, 38, 39) |
| One Expected fact with no retrieving event | None: every value in OE 31 and OE 36 traces to OE 1–30 |
| One act-vs-defer conflict | None: ledger §C defer search complete, no hold record (D05S58U4SAK/1759272012.507134 governs) |
| One non-action or final-response event | None: OE 30 is a tool-observed negative search; OE 36's Expected is the content of a required write |
| One prompt-forbidden write | None: no new Trello card; register only in Company Ops; reply only in the DM |
| One missing recovery / wait event | Not applicable: Friction none (03_Error_Async_Config.txt) |

## Advisory (no effect on the prediction)
| Event | Note |
|---|---|
| OE 33, 34 | An agent may create the file directly in Company Ops (gdrive_create_file with parentId); the two events are still one valid route |
| OE 31 | Analysis event with no tool; required so discovery does not jump straight to the writes |
| OE 9–30 | 22 per-account reads; long but not redundant, each returns facts used in OE 31 |

## Tally
Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 3

## Self-review

Re-verified: every Expected value above was re-read in this run — seeded rows through 01_Universe_Inject.sql (base_check.parse_sql), base records through `tools/hg.py search get-many` / `get` (Slack shards, Gmail threads, Trello card /cards/671) and snowflake.json /tables/35 for AD_REVENUE. The September mailbox scan for OE 30 was re-run with body text and found two records the ledger had not named (Meta Audience Network remittance Sep 22, AppLovin Tipalti notice Sep 14); neither touches the eight accounts, and ledger F30 was updated and re-gated.

Walk of Eval 1.2, 1.3, HARD GATE, 2.1–2.7, 3.1–3.6, 4.0: inventory has STEPs only; five fields present on each; no non-action or final-response event; service, tool, parameters, expected data, visibility, authority, act-vs-defer, final state and consistency checked per event above.

| # | Judgement | Counter-reading | Resolution (evidence) |
|---|---|---|---|
| 1 | R1 COVERED (OE 1, 2) | The amendment is in a thread a channel read omits, so OE 1 alone misses it | OE 2 reads the thread explicitly; OE 1 states "The message has one thread reply" (D05S58U4SAK/1759272498.304117) |
| 2 | R2 COVERED (OE 3, 7, 8) | Population narrowed before it is derived | OE 7 lists all 17 files first; OE 7 and OE 8 apply rule 1 to reach 13 (d_6cae3483dd469c189a528e, frederick.stone@harmonygames.co/1841349862518331350) |
| 3 | R3 COVERED | First-tab reads would miss the Partners and advertiser tabs | OE 9, 11, 12, 13, 23 name every tab (f_f7e7c5bf089029cee91175, f_1191b7f8c96419e1f4dc88) |
| 4 | R3 COVERED | The notices could be unreachable to the persona | check-sql YES on frederick.stone@harmonygames.co/1843622639043434721, /1842801580966444617, /1843339075781206004 (ledger visibility proof) |
| 5 | R4 COVERED | OE 30's absence is not tool-observed, so it is a non-action | It is a Gmail search with stated parameters returning no billing for the eight accounts (frederick.stone@harmonygames.co/1843428112007517388 is the only ad receipt) — a valid negative finding |
| 6 | R4 COVERED | AdMob money should be Y (paid out) | OE 2 sets the $100 floor; OE 20 returns $38.70 (snowflake.json /tables/35) |
| 7 | R5 COVERED | OE 31 is a jump with no stated method | OE 31 states class, money and action per account and cites the comment and email overrides (68dc529406d8087e5a6b8403, frederick.stone@harmonygames.co/1844732985606656293) |
| 8 | R6 COVERED | Creating the sheet is not putting it in Company Ops | OE 34 moves it (d_21f9e11d43739eaef26b38); OE 35 writes the rows |
| 9 | R7 COVERED | Content of the reply belongs to the rubric, so OE 36 is a final-response event | OE 36 is the required write; its Expected states the content the DM asked for (D05S58U4SAK/1759272012.507134) — allowed |
| 10 | R8 COVERED | Checklist might be wanted on a new card | Rule 7: "Don't open a new card"; OE 37–39 use card 67cf1b506d78ad3c72e02a35 |
| 11 | R9 COVERED | The agent should confirm with Fred before posting | Prompt: "go ahead and do it, you don't need to wait on me"; no defer record (ledger §C) |
| 12 | OE 10 MATCH (after fix) | The receipt might be for another Meta account | Link parameter decodes to act=907669287942378 (same ad account as the export); OE 10 no longer states the id, so the claim stays observable |
| 13 | OE 24 MATCH | [EMAIL_126620] might not be Node | The YouTube export's Removed users tab maps Node Media LLC to [EMAIL_126620] (f_fc27672c5bfea8b760b074, SQL L75) |
| 14 | OE 31 TRANSFER count 1 | Instagram or TikTok could still be TRANSFER | Notices make Instagram COMPANY-HELD (two harmonygames.co admins) and TikTok OUTSIDE ACCESS (frederick.stone@harmonygames.co/1843339075781206004, /1843622639043434721) |
| 15 | OE 14 Unity money Y | Unity cost is absent from the warehouse, so N | Cash notes: "go by … whether the campaign is on"; budget $150/day set Sep 29 (C07C2866011/1759186080.203099) |

Unresolved: none.

```
STAGE GATE oe-check: PASS — Task_Authoring-2/task_inputs · 08_OE_Check.md#b0f7ba73e28f · 08_Oracle_Events.md#a63a61a7167d · blocking 0 · warnings 0 · checks 17
[PASS] structure.outputs: 1 output(s) present: 08_OE_Check.md
[PASS] structure.inputs: 2 input(s) present: 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#4af1cfa17572)
[PASS] structure.sections: 7 required sections present and non-empty (08_OE_Check.md)
[PASS] structure.placeholders: no placeholders in 08_OE_Check.md
[PASS] structure.header_counts: header matches 08_Oracle_Events.md (39 events, 17119 chars)
[PASS] structure.prediction: /oe prediction line present
[PASS] evidence.quoted_spans: 0 quoted span(s) verified as exact substrings of 08_Oracle_Events.md
[PASS] evidence.findings_evidence: no rows/items found under 'findings' in 08_OE_Check.md
[PASS] evidence.signoff_reread: 34/34 items carry a source pointer (min 100%)
[PASS] structure.sweep: pre-verdict sweep has 7/7 rows
[PASS] structure.tally: tally Blocking 0 vs 0 BLOCKING findings
[PASS] review.counter_readings: 14 evidenced counter-readings (of 15 found; need ≥ 9) in 08_OE_Check.md
[PASS] review.coverage: self-review addresses all 1 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

