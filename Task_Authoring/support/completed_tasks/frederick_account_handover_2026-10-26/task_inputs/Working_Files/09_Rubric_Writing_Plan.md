# 09 Rubric Writing Plan — Frederick account handover register (fs-account-custody)
Generated 2026-10-26 · Clock 2025-10-01T07:00:00Z (Oct 1, 2025 00:00 PT, the assigned universe date in 00_Assigments.md; V3 replaces the bundle's fixed 2026-02-14 clock) · Persona Frederick Stone frederick.stone@harmonygames.co · Tier Normal, difficulty mode medium · Human time 8.00 h (05_Human_Time_Worksheet.md, first pass) · OE status: /oe PASS 2026-10-26 (OE sha 25edc10c3ebe, Completeness 5, Accuracy 5)
Canonical outcome: brief §4b (one acceptance class per deliverable). The §4b field structure and equivalence classes are used as written; its fixed values predate hardening rounds 2–3, so the values come from ledger F33/F34 and the /oe PASS events: (W1) one Google Sheet directly in Company Ops d_21f9e11d43739eaef26b38, 13 rows, rule-6 columns, title representational; (W2) one message in DM D05S58U4SAK, thread reply or top level, giving TRANSFER count 1 and Node Media LLC's access on Meta, Unity Ads advertiser, YouTube Brand Account and TikTok, wording representational; (W3) a checklist on the existing card 67cf1b506d78ad3c72e02a35 whose only item names X, checklist and item wording representational.

Rows are noun phrases plus values, not criterion text. V3 (11_V3_Changes.md): the human writes the criteria; this plan lists what must be graded.

## A · Coverage matrix
| P | Source (prompt span · OE n) | What must be verified (noun phrase) | Final state that proves it (artifact / message / record / final response) | Category (Outcome / Process candidate → C) | Values the criterion must name (F-IDs + backticked literals; exact / tolerance) |
|---|---|---|---|---|---|
| P1 | "Put it all in a Google Sheet in the Company Ops folder" · OE 32, 33, 34 | Register location — a new Google Sheet saved in the Company Ops folder | Drive file whose parent is the Company Ops folder | Outcome | F31 `Company Ops`; exact folder; title ungraded |
| P2 | "Put it all in a Google Sheet in the Company Ops folder" · OE 3, 35 | Register columns — the five columns of card rule 6 | Header of the register sheet | Outcome | F3 account company holders class money moving action; equivalent header wording accepted, any order |
| P3 | "It covers every marketing and UA account I'm on." · OE 7, 8, 35 | Register volume — exactly 13 account rows after rule 1 | Row set of the register | Outcome | F7 F8 F3 `13`; the excluded set is `pub-2341961509332343`, Google Play Console, App Store Connect, Singular, @harmonygames.app; exact count |
| P4 | "and what we should do with it" · OE 9, 31, 35 | Meta Domino Delights ad account action — REVOKE for Node Media LLC's partner admin | Meta row, action column | Outcome | F9 F3 Domino Delights `REVOKE` (`Node Media LLC` on the Partners tab); exact action |
| P5 | "and what we should do with it" · OE 13, 31, 35 | Unity action — REVOKE for Node Media LLC's Admin on the Unity Ads advertiser | Unity row, action column | Outcome | F13 F3 Unity `REVOKE`; exact action |
| P6 | "and what we should do with it" · OE 21, 22, 31, 35 | TikTok @harmonygames action — REVOKE for Node Media LLC's Business Center partner Admin | TikTok row, action column | Outcome | F21 F22 TikTok `REVOKE`; exact action |
| P7 | "and what we should do with it" · OE 23, 24, 31, 35 | YouTube channel action — REVOKE for Node Media LLC's Brand Account Owner role | YouTube row, action column | Outcome | F23 F24 YouTube `REVOKE`; exact action |
| P8 | "and what we should do with it" · OE 27, 28, 4, 31, 35 | Instagram @harmonygames action — KEEP (Leonard and Fred with full control; socials never CLOSE) | Instagram row, action column | Outcome | F27 F28 F4 Instagram KEEP; exact action |
| P9 | "and what we should do with it" · OE 26, 4, 31, 35 | X @harmonygames action — TRANSFER (Fred the only holder; socials never CLOSE) | X row, action column | Outcome | F26 F4 X `TRANSFER`; exact action |
| P10 | "and what we should do with it" · OE 11, 5, 31, 35 | Google Ads 569-350-5790 action — KEEP per Arthur's Sep 30 email | Google Ads 569 row, action column | Outcome | F11 F5 `569-350-5790` KEEP; exact action |
| P11 | "and what we should do with it" · OE 12, 5, 31, 35 | Google Ads 449-481-1590 (Calm Play) action — CLOSE | Google Ads 449 row, action column | Outcome | F12 F5 `449-481-1590` CLOSE; exact action |
| P12 | "and what we should do with it" · OE 17, 18, 6, 31, 35 | adjoe action — CLOSE (September installs waived in writing) | adjoe row, action column | Outcome | F17 F18 F6 adjoe CLOSE; exact action |
| P13 | "and what we should do with it" · OE 19, 20, 2, 31, 35 | AdMob pub-3556282811018998 action — CLOSE ($38.70 September revenue under $100) | AdMob row, action column | Outcome | F19 F20 F2 `pub-3556282811018998` CLOSE; exact action |
| P14 | "and what we should do with it" · OE 15, 16, 31, 35 | AppLovin action — KEEP | AppLovin row, action column | Outcome | F15 F16 AppLovin KEEP; exact action |
| P15 | "and what we should do with it" · OE 25, 4, 31, 35 | LinkedIn page action — KEEP (socials never CLOSE) | LinkedIn row, action column | Outcome | F25 F4 LinkedIn KEEP; exact action |
| P16 | "and what we should do with it" · OE 29, 4, 31, 35 | Discord server action — KEEP (socials never CLOSE) | Discord row, action column | Outcome | F29 F4 Discord KEEP; exact action |
| P17 | "For each one, figure out who actually holds it" · OE 9, 35 | Meta company holders — the four Admins | Meta row, company holders column | Outcome | F9 Frederick Stone Robert Leonard Hayes Arthur Blake; names or harmonygames.co addresses |
| P18 | "For each one, figure out who actually holds it" · OE 13, 35 | Unity company holders — the three Owners, Fred excluded as a Manager | Unity row, company holders column | Outcome | F13 F3 Arthur Blake Robert Leonard Hayes; names or addresses; exact set |
| P19 | "whether money's still moving on it" · OE 10, 6, 35 | Meta money moving — Y (September ad receipt) | Meta row, money moving column | Outcome | F10 F6 Y (`$0.05` billed for Sep 15); Y/yes |
| P20 | "whether money's still moving on it" · OE 14, 6, 35 | Unity money moving — Y (iOS campaigns switched on) | Unity row, money moving column | Outcome | F14 F6 Y (`$150/campaign/day` set Sep 29); Y/yes |
| P21 | "then reply to him in that DM with what he asked for" · OE 1, 36 | Reply sent in the DM with Leonard | Message posted by Frederick in D05S58U4SAK | Outcome | F1 `D05S58U4SAK`; thread reply or top-level message |
| P22 | "then reply to him in that DM with what he asked for" · OE 31, 36 | Reply TRANSFER count — one account marked TRANSFER | Body of that DM message | Outcome | F34 F33 `1` (X @harmonygames); number or word |
| P23 | "then reply to him in that DM with what he asked for" · OE 9, 36 | Reply outsider access — Node Media LLC on the Meta ad account | Body of that DM message | Outcome | F34 F9 `Node Media LLC` Meta; agency named as Node or Node Media |
| P24 | "then reply to him in that DM with what he asked for" · OE 13, 36 | Reply outsider access — Node Media LLC on Unity (Unity Ads advertiser) | Body of that DM message | Outcome | F34 F13 `Node Media LLC` Unity |
| P25 | "then reply to him in that DM with what he asked for" · OE 24, 36 | Reply outsider access — Node Media LLC on YouTube (Brand Account Owner) | Body of that DM message | Outcome | F34 F24 `Node Media LLC` YouTube |
| P26 | "then reply to him in that DM with what he asked for" · OE 22, 36 | Reply outsider access — Node Media LLC on TikTok @harmonygames | Body of that DM message | Outcome | F34 F22 `Node Media LLC` TikTok |
| P27 | "If Arthur's handover rules want anything else done once the sheet's ready, go ahead and do it" · OE 37, 38 | Checklist added to Fred's existing "Lock up social handles and domain?" card (rule 7), no new card | Checklist on Trello card 67cf1b506d78ad3c72e02a35 | Outcome | F32 F3 `Lock up social handles and domain?`; exact card; checklist name ungraded |
| P28 | "If Arthur's handover rules want anything else done once the sheet's ready, go ahead and do it" · OE 39 | Checklist item set — one item, naming X @harmonygames | Items of that checklist | Outcome | F26 F33 X; item wording ungraded |
| P29 | "For each one, figure out who actually holds it" · OE 11, 3, 35 | Google Ads 569-350-5790 class — COMPANY-HELD (two company holders, Node unlinked) | Google Ads 569 row, class column | Outcome | F11 F3 `569-350-5790` COMPANY-HELD; the card's label or an obvious synonym |

## A2 · Grading risks and weight
| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Duplicate risk (per deliverable) / overlap group | Predicted all-fail basis (four Evals bases) · over-specific risk |
|---|---|---|---|---|---|---|---|---|---|
| P1 | Folder name yes (prompt); sheet title no — must not hard-code | none | no | lookup — one folder search plus one write | 1 | F31 | — | none | none · accept create-in-folder or create-then-move |
| P2 | Column names yes (card rule 6) | none | no | lookup — names copied from one rule | 1 | F3 | — | none; one header row (one tool output) | none · accept equivalent header wording and any order |
| P3 | no — must not hard-code | T7 old AdMob export, T16 store and data exports → count rejects them | no | multi-source — folder listing, rule 1 and the deactivation mail | 5 | T7 T16 | G1 volume | none | none · accept extra non-account rows such as a totals or notes line kept apart |
| P4 | Action verb from card rule 5 | T1 Leonard's "those are covered" → REVOKE rejects KEEP | no | interpretation — second tab plus rule 4 | 3 | T1 | G1 exception | none | none · accept the card's verb or an obvious synonym |
| P5 | Action verb from card rule 5 | T1 → REVOKE rejects KEEP | no | interpretation — second tab plus rules 2 and 4 | 3 | T1 | G1 exception | none | none |
| P6 | Action verb from card rule 5 | T9 login-only export → REVOKE rejects TRANSFER | no | multi-source — export plus a Gmail vendor notice | 5 | T9 | G1 exception | none | none |
| P7 | Action verb from card rule 5 | T8 Node removed in Studio → REVOKE rejects TRANSFER | no | multi-source — two tabs plus a Gmail notice joined on the agency address | 5 | T8 | G1 exception | none | none |
| P8 | Action verb from card rule 5 | T10 login-only export, T12 socials close → KEEP rejects TRANSFER and CLOSE | no | multi-source — export, Meta notice, comment | 5 | T10 T12 | G1 exception | none | none |
| P9 | Action verb from card rule 5 | T2 Arthur's summary, T12 → TRANSFER rejects KEEP and CLOSE | no | interpretation — one tab plus the comment | 3 | T2 T12 | G1 exception | none (the reply count P22 and the checklist P28 are other deliverables) | none |
| P10 | Action verb from card rule 5 | T11 → KEEP rejects CLOSE | no | interpretation — card plus Arthur's override email | 3 | T11 | G1 exception | none | none |
| P11 | Action verb from card rule 5 | T4 Confluence "don't close" → CLOSE rejects KEEP | no | interpretation — card, email ("still follows the card"), no money | 3 | T4 | G1 exception | none | none |
| P12 | Action verb from card rule 5 | T14 campaign ran Sep 1 → CLOSE rejects KEEP | no | interpretation — Slack waiver read against the cash-notes exclusion | 3 | T14 | G1 exception | none | none |
| P13 | Action verb from card rule 5 | T13 paid revenue, T15 "active and working" → CLOSE rejects KEEP | no | multi-source — Snowflake sum, Leonard's thread reply, cash notes | 5 | T13 T15 | G1 exception | none | none |
| P14 | Action verb from card rule 5 | none | no | interpretation — two admins plus a September payout | 3 | — | G1 sample (ordinary) | none | none |
| P15 | Action verb from card rule 5 | T12 → KEEP rejects CLOSE | no | interpretation — page admins plus the comment | 3 | T12 | G1 exception | none | none |
| P16 | Action verb from card rule 5 | T12 → KEEP rejects CLOSE | no | interpretation — server admins plus the comment | 3 | T12 | G1 exception | none | none |
| P17 | no — must not hard-code | none | no | lookup — one tab | 1 | — | G2 sample | none | none · names or addresses |
| P18 | no — must not hard-code | none | no | interpretation — rule 2 excludes the Manager | 3 | — | G2 sample (edge) | none | none · names or addresses |
| P19 | no — Y/N per rule 6 | T3 90-day remark; FB campaign off Sep 26 → Y from the September receipt | no (ledger risk 5: Y holds either way) | interpretation — receipt read against the cash-notes definition | 3 | T3 | G3 sample | none | none · Y or yes |
| P20 | no — Y/N per rule 6 | none | no | interpretation — campaign switched on per the cash notes | 3 | — | G3 sample | none | none · Y or yes |
| P21 | Destination yes (prompt: "in that DM") | none | no (ledger risk 1: thread or top level) | lookup — one send | 1 | F1 | — | none | none · phrase broadly: thread reply or new DM message |
| P22 | no — number or word | T2 Arthur's summary (2), exports alone (4) → count 1 | no | multi-source — the count only the full audit produces | 5 | T2 T8 T9 T10 | — | none (register row P9 is another deliverable) | none |
| P23 | no — agency name as Node or Node Media | T1 | no | interpretation — reply carries the Partners-tab finding | 3 | T1 | — | none (P4 is the register) | none |
| P24 | no | T1 | no | interpretation — reply carries the advertiser-tab finding | 3 | T1 | — | none (P5 is the register) | none |
| P25 | no | T8 | no | multi-source — notice joined to the export's agency address | 5 | T8 | — | none (P7 is the register) | none |
| P26 | no | T9 | no | multi-source — export plus the TikTok notice | 5 | T9 | — | none (P6 is the register) | none |
| P27 | Card name yes (card rule 7) | none | no | interpretation — rule 7 names the card and board | 3 | F32 | — | none | none · checklist name ungraded |
| P28 | no — item wording ungraded | T8 T9 T10 → item set X only rejects YouTube, TikTok, Instagram items | no | interpretation — only socials marked TRANSFER, from the register | 3 | T8 T9 T10 | G4 sample | none | none · any item wording naming X |
| P29 | Class label from card rule 4 | none | no | interpretation — rule 4 applied to two tabs | 1 | — | G5 sample | none (its action P10 comes from the email, so the cell varies independently) | none · the card's label or an obvious synonym |

## B · OE trace
| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |
|---|---|---|---|
| 1 | discovery | P21 | no — the DM is proven by the sent reply |
| 2 | discovery | P13 | no — the $100 floor shows in AdMob's action |
| 3 | discovery | P2, P3, P27 | no — the rules show in columns, row set and checklist |
| 4 | discovery | P8, P9, P15, P16 | no — socials never CLOSE |
| 5 | discovery | P10, P11 | no |
| 6 | discovery | P12, P19, P20 | no |
| 7 | discovery | P3 | no |
| 8 | discovery | P3 | no |
| 9 | discovery | P4, P17, P23 | no |
| 10 | discovery | P19 | no |
| 11 | discovery | P10, P29 | no |
| 12 | discovery | P11 | no |
| 13 | discovery | P5, P18, P24 | no |
| 14 | discovery | P20 | no |
| 15 | discovery | P14 | no |
| 16 | discovery | P14 | no |
| 17 | discovery | P12 | no |
| 18 | discovery | P12 | no |
| 19 | discovery | P13 | no |
| 20 | discovery | P13 | no |
| 21 | discovery | P6 | no |
| 22 | discovery | P6, P26 | no |
| 23 | discovery | P7 | no |
| 24 | discovery | P7, P25 | no |
| 25 | discovery | P15 | no |
| 26 | discovery | P9, P28 | no |
| 27 | discovery | P8 | no |
| 28 | discovery | P8 | no |
| 29 | discovery | P16 | no |
| 30 | discovery | P10, P11, P15 | no — no money keeps the CLOSE/KEEP split |
| 31 | discovery (analysis) | P4–P16, P22 | no |
| 32 | discovery | P1 | no |
| 33 | write | P1 | yes — sheet created (one end state with OE 34) |
| 34 | write | P1 | yes — sheet placed |
| 35 | write | P2–P20, P29 | yes |
| 36 | write | P21–P26 | yes |
| 37 | discovery | P27 | no |
| 38 | write | P27 | yes |
| 39 | write | P28 | yes |

## C · Process candidates — three-condition test
| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |
|---|---|---|---|---|---|---|
| — | "once the sheet's ready" (checklist after the register) | An Outcome proves the content: P28 X-only items follow from the register's single TRANSFER | n/a | fails — P28 captures it | n/a | no Process row; covered by P28 (F33) |
| — | "you don't need to wait on me" | The sent reply and the checklist exist (P21, P27) | n/a | fails — P21, P27 capture it | n/a | no Process row; covered by P21, P27 (F1, F32) |

## D · Spot-check groups
| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |
|---|---|---|---|---|---|
| G1 | F33, 13 actions, keyed by export title: `Meta Business - Domino Delights ad account - people` `Google Ads 569-350-5790 - access` `Google Ads 449-481-1590 - access` `Unity - Harmony Games Inc org - owners and managers` `AppLovin - Harmony Games - account users` `adjoe advertiser dashboard - users` `AdMob pub-3556282811018998 - users` `TikTok - harmonygames - access` `YouTube - Harmony Games channel - permissions` `LinkedIn - Harmony Games page - admins` `X - harmonygames - access` `Instagram - harmonygames - access` `Discord - Harmony Games server - admin roles` | P14 AppLovin (ordinary); every other account is an authority-named exception graded directly (P4–P13, P15, P16: Node tabs and notices, the comment's socials, the email's two Google Ads, the waiver, the $100 floor) | P3 | none — bundle (Rubric Writing §7; Eval 2.2) | no — per-account members of one register |
| G2 | F33, 13 holder cells, keyed by export title: `Meta Business - Domino Delights ad account - people` `Google Ads 569-350-5790 - access` `Google Ads 449-481-1590 - access` `Unity - Harmony Games Inc org - owners and managers` `AppLovin - Harmony Games - account users` `adjoe advertiser dashboard - users` `AdMob pub-3556282811018998 - users` `TikTok - harmonygames - access` `YouTube - Harmony Games channel - permissions` `LinkedIn - Harmony Games page - admins` `X - harmonygames - access` `Instagram - harmonygames - access` `Discord - Harmony Games server - admin roles` | P17 Meta (four Admins, ordinary), P18 Unity (Manager excluded, edge) | P3 | none — bundle (Rubric Writing §7; Eval 2.2) | no |
| G3 | F33, 13 money cells, keyed by export title: `Meta Business - Domino Delights ad account - people` `Google Ads 569-350-5790 - access` `Google Ads 449-481-1590 - access` `Unity - Harmony Games Inc org - owners and managers` `AppLovin - Harmony Games - account users` `adjoe advertiser dashboard - users` `AdMob pub-3556282811018998 - users` `TikTok - harmonygames - access` `YouTube - Harmony Games channel - permissions` `LinkedIn - Harmony Games page - admins` `X - harmonygames - access` `Instagram - harmonygames - access` `Discord - Harmony Games server - admin roles` | P19 Meta (campaign turned off, receipt still September), P20 Unity (campaign state, no warehouse cost) | P3 | none — bundle (Rubric Writing §7; Eval 2.2) | no |
| G4 | F33, social TRANSFER rows: `X - harmonygames - access` | P28 X (the whole set; YouTube, TikTok, Instagram look TRANSFER on the exports) | P28 | none — bundle (Rubric Writing §7; Eval 2.2) | no — one-member set graded whole |
| G5 | F33, 13 class cells, keyed by export title: `Google Ads 569-350-5790 - access` | P29 Google Ads 569 (class independent of its email-set action) | P3 | none — bundle (Rubric Writing §7; Eval 2.2) | no |

## E · Summary
Rows 29 · Outcome 29 · Process candidates 0 — ≥ 1 Outcome ☑ (no Process ratio: QC Spec V2 and the Evals override fail only zero Outcome) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ · predicted all-fail rows = 0 ☑ (harness tolerance 0; /rubric fails at ≥ 2)
Failure diversity: largest unit of discovery is the rules card (F3) at 98% of the weight, then the sweep folder listing (F7) at 90% (≤ 50% ☒ — every register, reply and checklist row runs through the rules card and the sweep folder listing; Self-review §6) · chains landing on distinct rows ☑ (Meta/Unity partner tabs P4 P5 P23 P24; YouTube notice P7 P25; TikTok notice P6 P26; Instagram notice P8; row scope P3; Google Ads email P10; $100 floor P13; waiver P12)
Bands: 5 ×8 · 3 ×16 · 1 ×5 (total weight 93)
Set size: 29 rows for 8.00 h (reference: 31 criteria for a ~10-hour task; ~60 signals duplicate grading, ~12 missing coverage)
Coverage: requirements 9/9 · OEs 39/39 · writes 6/6 OE write events (6 ledger writes) · told facts 2/2 (TRANSFER count, outside access) · friction 0/0 (Friction: none)
Four prohibitions: ☑ unstated expectations ☑ conclusions on ambiguous evidence ☑ grading the distractor ☑ hard-coded titles/phrasings
Blocking: no UGT defect · no infeasible write (ledger §C, 6/6 feasible) · no unverified visibility. Difficulty note (not a rubric defect; weights follow the work, not the target): on the six baseline runs this plan scores about 68 / 60 / 67 / 91 / 100 / 95 → average ~80%, pass@1 1/6; under the medium cap of 85%, above the Evals 75% line

Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)

`python3 Task_Authoring-2/tools/persona_view.py check-sql frederick_stone Task_Authoring-2/task_inputs/01_Universe_Inject.sql --load-bearing <ids>`, load-bearing rows for every scoped id behind the cited F-ids:

```
[YES LB] L2 gdrive.drive_files insert d_6cae3483dd469c189a528e - file is shared with the persona (shared_with_emails)
[YES LB] L7 gdrive.drive_files insert f_f7e7c5bf089029cee91175 - file is shared with the persona (shared_with_emails)
[YES LB] L11 gsheets.sheets_sheets insert f_f7e7c5bf089029cee91175, f_f7e7c5bf089029cee91175#0 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gsheets.sheets_sheets insert f_f7e7c5bf089029cee91175, f_f7e7c5bf089029cee91175#1 - file is shared with the persona (shared_with_emails)
[YES LB] L15 gdrive.drive_files insert f_ab70b02c329d038a72fb9f - file is shared with the persona (shared_with_emails)
[YES LB] L19 gsheets.sheets_sheets insert f_ab70b02c329d038a72fb9f, f_ab70b02c329d038a72fb9f#0 - file is shared with the persona (shared_with_emails)
[YES LB] L21 gsheets.sheets_sheets insert f_ab70b02c329d038a72fb9f, f_ab70b02c329d038a72fb9f#1 - file is shared with the persona (shared_with_emails)
[YES LB] L23 gdrive.drive_files insert f_63b42f52fa11d7df238a4e - file is shared with the persona (shared_with_emails)
[YES LB] L27 gsheets.sheets_sheets insert f_63b42f52fa11d7df238a4e, f_63b42f52fa11d7df238a4e#0 - file is shared with the persona (shared_with_emails)
[YES LB] L29 gsheets.sheets_sheets insert f_63b42f52fa11d7df238a4e, f_63b42f52fa11d7df238a4e#1 - file is shared with the persona (shared_with_emails)
[YES LB] L31 gdrive.drive_files insert f_1191b7f8c96419e1f4dc88 - file is shared with the persona (shared_with_emails)
[YES LB] L35 gsheets.sheets_sheets insert f_1191b7f8c96419e1f4dc88, f_1191b7f8c96419e1f4dc88#0 - file is shared with the persona (shared_with_emails)
[YES LB] L37 gsheets.sheets_sheets insert f_1191b7f8c96419e1f4dc88, f_1191b7f8c96419e1f4dc88#1 - file is shared with the persona (shared_with_emails)
[YES LB] L39 gdrive.drive_files insert f_3996bca752549d3512bfbc - file is shared with the persona (shared_with_emails)
[YES LB] L43 gsheets.sheets_sheets insert f_3996bca752549d3512bfbc, f_3996bca752549d3512bfbc#0 - file is shared with the persona (shared_with_emails)
[YES LB] L45 gdrive.drive_files insert f_a552317a929102385c0393 - file is shared with the persona (shared_with_emails)
[YES LB] L49 gsheets.sheets_sheets insert f_a552317a929102385c0393, f_a552317a929102385c0393#0 - file is shared with the persona (shared_with_emails)
[YES LB] L51 gdrive.drive_files insert f_50ff132ac88169019feeca - file is shared with the persona (shared_with_emails)
[YES LB] L55 gsheets.sheets_sheets insert f_50ff132ac88169019feeca, f_50ff132ac88169019feeca#0 - file is shared with the persona (shared_with_emails)
[YES LB] L57 gdrive.drive_files insert f_e239ffb975eb7c66d7287d - file is shared with the persona (shared_with_emails)
[YES LB] L61 gsheets.sheets_sheets insert f_e239ffb975eb7c66d7287d, f_e239ffb975eb7c66d7287d#0 - file is shared with the persona (shared_with_emails)
[YES LB] L63 gdrive.drive_files insert f_2f0abe2f1f6726fef63f80 - file is shared with the persona (shared_with_emails)
[YES LB] L67 gsheets.sheets_sheets insert f_2f0abe2f1f6726fef63f80, f_2f0abe2f1f6726fef63f80#0 - file is shared with the persona (shared_with_emails)
[YES LB] L69 gdrive.drive_files insert f_fc27672c5bfea8b760b074 - file is shared with the persona (shared_with_emails)
[YES LB] L73 gsheets.sheets_sheets insert f_fc27672c5bfea8b760b074, f_fc27672c5bfea8b760b074#0 - file is shared with the persona (shared_with_emails)
[YES LB] L75 gsheets.sheets_sheets insert f_fc27672c5bfea8b760b074, f_fc27672c5bfea8b760b074#1 - file is shared with the persona (shared_with_emails)
[YES LB] L77 gdrive.drive_files insert f_b89c1c70489f81031bdd4f - file is shared with the persona (shared_with_emails)
[YES LB] L81 gsheets.sheets_sheets insert f_b89c1c70489f81031bdd4f, f_b89c1c70489f81031bdd4f#0 - file is shared with the persona (shared_with_emails)
[YES LB] L83 gdrive.drive_files insert f_99d66f33c54338e70f5ed2 - file is shared with the persona (shared_with_emails)
[YES LB] L87 gsheets.sheets_sheets insert f_99d66f33c54338e70f5ed2, f_99d66f33c54338e70f5ed2#0 - file is shared with the persona (shared_with_emails)
[YES LB] L89 gdrive.drive_files insert f_215ff8da73e4173f78515c - file is shared with the persona (shared_with_emails)
[YES LB] L93 gsheets.sheets_sheets insert f_215ff8da73e4173f78515c, f_215ff8da73e4173f78515c#0 - file is shared with the persona (shared_with_emails)
[YES LB] L95 gdrive.drive_files insert f_2cecf2f81045ec401feb61 - file is shared with the persona (shared_with_emails)
[YES LB] L99 gsheets.sheets_sheets insert f_2cecf2f81045ec401feb61, f_2cecf2f81045ec401feb61#0 - file is shared with the persona (shared_with_emails)
[YES LB] L101 gdrive.drive_files insert f_5f2f52786dcd8e1168cd40 - file is shared with the persona (shared_with_emails)
[YES LB] L107 gdrive.drive_files insert f_ad393ed61590f2d22c6cd7 - file is shared with the persona (shared_with_emails)
[YES LB] L113 gdrive.drive_files insert f_b463693cd3779d4d25374f - file is shared with the persona (shared_with_emails)
[YES LB] L125 gdrive.drive_files insert f_c612c0e68a27b3330eb46a - file is shared with the persona (shared_with_emails)
[YES LB] L127 gdocs.docs_documents insert f_c612c0e68a27b3330eb46a - file is shared with the persona (shared_with_emails)
[YES LB] L129 gdrive.drive_files insert d_21f9e11d43739eaef26b38 - file is shared with the persona (shared_with_emails)
[YES LB] L137 slack.slack_messages insert 02847a3cc740c9b657d75f26c3750854, D05S58U4SAK/1759272012.507134 - persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] L139 slack.slack_messages insert af9538edf73b974e0c59d58c7d559c06, D05S58U4SAK/1759272498.304117 - persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] L152 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844732985606656293 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L186 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842801580966444617 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L190 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843622639043434721 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L194 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843339075781206004 - row user_email is the persona (frederick.stone@harmonygames.co)
verdict: PASS (0 load-bearing rows not visible)
```

`python3 Task_Authoring-2/tools/persona_view.py can-see frederick_stone <service> <id>` (base records):

```
frederick_stone slack C07UCC631A6/1757346020.196019: YES
frederick_stone slack C07UCC631A6/1757349668.681539: YES
frederick_stone slack C07C2866011/1759186080.203099: YES
frederick_stone slack C07C2866011/1759264050.305069: YES
frederick_stone slack D05S58U4SAK/1756147086.813789: YES
frederick_stone gmail frederick.stone@harmonygames.co/1843428112007517388: YES
frederick_stone gmail frederick.stone@harmonygames.co/1843223812315546201: YES
frederick_stone gmail frederick.stone@harmonygames.co/1841349862518331350: YES
```

## F · Shortcut probe
Command: `python3 Task_Authoring-2/tools/shortcut_probe.py frederick_stone Task_Authoring-2/task_inputs/Working_Files/09_Rubric_Writing_Plan.md --sql Task_Authoring-2/task_inputs/01_Universe_Inject.sql` (run 2026-10-26, second run after narrowing the backticked values to identifier-grade acceptance literals; the first run's 1,399 hits came from generic words such as account, Unity, KEEP and person names).

```
SHORTCUT PROBE as frederick_stone <frederick.stone@harmonygames.co> · values 09_Rubric_Writing_Plan.md (46 values, 3 populations, sha 07f0a357a8e6) · k 3 · services all · sql 01_Universe_Inject.sql
HIT sql:slack.slack_messages L137:02847a3cc740c9b657d75f26c3750854 holds 3/46 values (k=3): `Company Ops` · `D05S58U4SAK` · `TRANSFER`
HIT sql:trello.trello_cards L141:68dc406c7b0d03e53b334bab holds 4/46 values (k=3): `Lock up social handles and domain?` · `REVOKE` · `These replace the old Company Accounts & Access page on Confluence for marketing.` · `TRANSFER`
SKIPPED value:"13" (shorter than 3 characters)
SKIPPED value:"1" (shorter than 3 characters)
verdict: HITS (2)
```
SHORTCUT-OK: sql:slack.slack_messages L137:02847a3cc740c9b657d75f26c3750854 — Leonard's hub ask (F1), the task's anchor named by the prompt; it holds the destination, the DM and the word TRANSFER as the thing to count, not any account's action or the count itself
SHORTCUT-OK: sql:trello.trello_cards L141:68dc406c7b0d03e53b334bab — the designed rules card (F3) the agent must find; it states rules 1–7 and names the action verbs and the handles card, but no account's class, action or the TRANSFER count

## Self-review
### Per-row counter-readings (prep 2)
| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |
|---|---|---|---|---|
| P1 counter-reading | holds | A run creates the sheet with gdrive_create_file and parentId instead of moving it | Same end state: parent d_21f9e11d43739eaef26b38 (F31). Row grades the parent only; title ungraded | none |
| P2 counter-reading | holds | A run labels a column "Holders" or "Money still moving?" | Rule 6 (F3, trello 68dc406c7b0d03e53b334bab) fixes the meaning; equivalent wording and any order accepted | none |
| P3 counter-reading | holds | A run keeps a 14th row for AdMob pub-2341961509332343 marked CLOSE | Rule 1: deactivated before the sweep is off the list; deactivated Aug 24 2025 (F8, frederick.stone@harmonygames.co/1841349862518331350); 14 fails, correctly. Baseline runs 2, 3, 4, 6 did this | none |
| P4 counter-reading | holds | Leonard is admin, so Meta is COMPANY-HELD → KEEP | Rule 4: a partner admin makes it OUTSIDE ACCESS whatever the holders (F9 Partners tab, f_f7e7c5bf089029cee91175) | none |
| P5 counter-reading | holds | The Members tab shows no outsider → KEEP | The Unity Ads advertiser tab lists Node Media LLC Admin since 2024-12-05 (F13, SQL L37) | none |
| P6 counter-reading | holds | Fred is the only login → SINGLE → TRANSFER | The Sep 18 Business Center reminder names Node Media LLC Admin (F22, frederick.stone@harmonygames.co/1843622639043434721); no removal record | none |
| P7 counter-reading | holds | Node was removed from Studio in Dec 2024 → SINGLE → TRANSFER | The Sep 9 Brand Account notice lists [EMAIL_126620] Owner (F24); the export maps that address to Node (F23, SQL L75) | none |
| P8 counter-reading | holds | The only login is Fred's personal gmail → SINGLE → TRANSFER | The Sep 15 Meta notice: Leonard and Fred full control on harmonygames.co logins (F28, frederick.stone@harmonygames.co/1843339075781206004) → COMPANY-HELD, no money, social → KEEP (F4) | none |
| P9 counter-reading | holds | No money moving → CLOSE | Comment 68dc529406d8087e5a6b8403 (F4): socials go TRANSFER or KEEP by class; X SINGLE (F26) → TRANSFER | none |
| P10 counter-reading | holds | Rule 5 closes 569 (no money) | Arthur's email (F5, frederick.stone@harmonygames.co/1844732985606656293): "Mark it KEEP"; baseline runs 3 and 4 missed it, correctly failing | none |
| P11 counter-reading | holds | The 2024 Confluence page says don't close accounts | The card replaces the page (F3); the email says 449 "still follows the card" (F5); no money (F12 Enabled campaigns 0) | none |
| P12 counter-reading | holds | The campaign ran in September → money Y → KEEP | adjoe: "you will not be responsible for the cost of those installs" (F18, C07UCC631A6/1757349668.681539); cash notes exclude waived charges (F6) | none |
| P13 counter-reading | holds | Ad revenue paid in September counts → Y → KEEP | Leonard's thread reply: under $100 doesn't count (F2, D05S58U4SAK/1759272498.304117); AD_REVENUE admob paid 38.70 (F20, snowflake.json /tables/35) | none |
| P14 counter-reading | holds | AppLovin ad revenue might be under $100 too → N → CLOSE | AD_REVENUE applovin paid 136.33 (F20) and the Sep 14 payout (F16) → Y → KEEP | none |
| P15 counter-reading | holds | Four Super admins and no money → CLOSE | Comment (F4): socials never CLOSE → KEEP (F25) | none |
| P16 counter-reading | holds | No money → CLOSE | Comment (F4) → KEEP (F29) | none |
| P17 counter-reading | holds | A run adds Node Media as a holder | Rule 3: company holders are harmonygames.co logins only; the four Admins on the People tab (F9, SQL L11) | none |
| P18 counter-reading | holds | A run lists Fred (he is on the org) | Rule 2: Managers don't count; Fred is Manager on the Members tab (F13, SQL L35); all six baseline runs excluded him | none |
| P19 counter-reading | holds | Leonard turned off the FB campaign Sep 26 → N | The cash notes count anything billed in September (F6); $0.05 billed for Sep 15 (F10, frederick.stone@harmonygames.co/1843428112007517388) → Y. Meta's action is REVOKE either way | none |
| P20 counter-reading | holds | The warehouse shows no Unity cost → N | Cash notes: spend goes by receipts and whether the campaign is on; iOS campaigns set to $150/day Sep 29 (F14, C07C2866011/1759186080.203099) → Y | none |
| P21 counter-reading | holds | A run replies in #executives or by email | The prompt says "in that DM"; the hub says "reply here" (F1, D05S58U4SAK/1759272012.507134); thread or top level both accepted | none |
| P22 counter-reading | holds | A run reports 2 (Arthur's summary) or 4 (exports alone) | Only X is SINGLE once the notices are read (F33); 1 is the count. Baseline runs 1, 2, 3 failed, correctly | none |
| P23 counter-reading | holds | A run says "an agency on the ad account" without naming Node | The ask is "anything an outsider still has access to"; the row needs the outsider and the account. Accept Node or Node Media (F9) | none |
| P24 counter-reading | holds | A run names "Unity" without "advertiser" | Accept Unity or Unity Ads; the advertiser is part of the Unity export (F13) | none |
| P25 counter-reading | holds | A run says Node was removed from YouTube | The Brand Account notice keeps Node as Owner (F24); that run fails, correctly | none |
| P26 counter-reading | holds | A run names TikTok but says the agency is only a login user | The notice names Node Media LLC as Business Center partner Admin (F22); naming Node with TikTok passes | none |
| P27 counter-reading | holds | A run creates a new "Socials to transfer" card | Rule 7: "Don't open a new card" (F3); the row names card 67cf1b506d78ad3c72e02a35 (F32) | none |
| P28 counter-reading | holds | A run adds YouTube and TikTok because Leonard's ask mentions "the tiktok/youtube mess" | Rule 7 limits the checklist to socials marked TRANSFER; only X is (F33). An affirmative one-member set, not a prohibition | none |
| P29 counter-reading | holds | A run classes 569 SINGLE because Arthur's email speaks of Leonard's wish | The Access tab lists Leonard and Fred as Admin (F11, SQL L19); Node unlinked 2024-12-20 (SQL L21) → COMPANY-HELD; all six baseline runs that wrote a class cell for 569 wrote COMPANY-HELD | none |

### 1 · Re-read as /rubric
| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |
|---|---|---|---|---|
| Requirement coverage (3_Rubrics_Eval.md 1.4, 3.1) | covered | The class column is never graded on its own | Class is the step between holders and action; grading it beside the action would form a cascade group per account. The action rows (P4–P16) reject a wrong class wherever it changes the action | none |
| Told facts | covered | The reply's link to the sheet is not graded | The hub asks only for the TRANSFER count and outside access (F1); a link is optional | none |
| Exclusion rows | covered | No row rejects the 14-row register directly | P3 is the affirmative count 13 and fails a register that keeps pub-2341961509332343; an absence row would fail Negative Criteria | none |
| V3 one fact in ≤ 2 rows | holds | X TRANSFER sits in P9, P22 and P28 | Three different facts on three deliverables: the register action (P9), the reply's count (P22) and the checklist write (P28). No two rows grade the same claim | none |

### 3 · Re-verified values (hg.py and SQL)
- Seeded literals re-read from 01_Universe_Inject.sql (sha 8d54ed2b4c0c) with base_check.parse_sql this session: export tabs L11–L99, rules card L141, comment L149, Arthur's email L154, cash notes L127, notices L188/L192/L196, Company Ops L129, the hub and reply L137/L139.
- Base literals re-read with `tools/hg.py search get-many`: adjoe thread C07UCC631A6 /2–/6, #executives /1166 and /1191, DM 2025-08 /145, Meta receipt, AppLovin payout and AdMob deactivation threads; handles card with `hg.py search get trello --file data.json --pointer /cards/671`.
- AD_REVENUE September 2025 re-summed from snowflake.json /tables/35 with Decimal: admob paid 38.6967, applovin paid 136.3291.
- Baseline check: register rows extracted from the six trajectories' values writes; holder and money cells for Meta and Unity match P17–P20 in every run that wrote them.

### 4 · Predicted all-fail re-check
Every row's values are reachable by Frederick: scoped records are YES in the visibility proof; Trello and Snowflake are unscoped; every write is in the catalog (ledger §C, 6/6). Friction none. Predicted all-fail rows: 0. Baseline run-5 passes all 29 rows.

### 6 · Shortcut and diversity
| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |
|---|---|---|---|---|
| Shortcut probe (gate 14) | 2 HITs, both dispositioned | Could a run answer from the rules card (L141) alone? It holds REVOKE, TRANSFER and the handles card | The card gives rules, not results: no account appears in it with a class or action (SQL L141 re-read). The hub (L137) gives the ask only. Every action needs the exports, notices and money evidence | none |
| Unit-of-discovery share (gate 12) | above 50% expected | The rules card (F3) and the sweep folder listing (F7) sit in the Depends-on closure of almost every row | Every register value is an export read under the card's rules, which is the task itself; citing them away would be false and reweighting would break the work-kind bands. Reported as a design finding, not hidden (same outcome as the card-spend task) | the gate's diversity.authority_share stays FAIL unless the human accepts it |

Unresolved: none in the plan rows.
