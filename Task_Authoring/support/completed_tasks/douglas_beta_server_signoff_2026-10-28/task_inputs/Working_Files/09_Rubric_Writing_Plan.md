# 09 Rubric Writing Plan — Douglas beta server register (dg-beta-server-signoff)
Generated 2026-10-27 · Clock 2025-10-01T00:00:00Z (assigned universe date; V3 replaces 2026-02-14) · Persona Douglas douglas@harmonygames.co · Tier Long-Horizon · Human time 12.75 h · OE status: /oe PASS 2026-10-27 (report 6ad90ea979eb9e5d89f8879f_2_oe (1).md, score 5, reviewed OE sha256 09fc22673a84)
Canonical outcome: brief §4b (one acceptance class per deliverable) — W1 register in d_69fcebc484d472907b0b5c (title any), 17 rows, server change(s) in any recognisable words, on prod Y/N; W3 Leonard commenter on the file; W4 DM D05QQF7V404 (thread or top level) with 2 on prod and the 15 keys; W5 the 15 tickets in Todo, each with a comment naming the change still to go out.

## A · Coverage matrix
| P | Source (prompt span · OE n) | What must be verified (noun phrase) | Final state that proves it (artifact / message / record / final response) | Category (Outcome / Process candidate → C) | Values the criterion must name (F-IDs + backticked literals; exact / tolerance) |
|---|---|---|---|---|---|
| P1 | "Put the register in the beta sign-off folder" · OE 4, 6, 33 | Register location — a Google Sheet saved in Arthur's "ZM Beta sign-off" folder | Drive file whose parent is d_69fcebc484d472907b0b5c | Outcome | F4 F10 `ZM Beta sign-off`; exact folder; title ungraded |
| P2 | "Can you take care of it for me, the way he laid it out?" · OE 12, 13, 14, 33 | Register volume — exactly 17 ticket rows | Row set of the register | Outcome | F12 F13 F14 F11 `17`; exact count (ZOM-547, ZOM-553, ZOM-457, ZOM-461 not rows; ZOM-436 is a row) |
| P3 | "Can you take care of it for me, the way he laid it out?" · OE 16, 9, 32, 33 | ZOM-459 register row — marked not on prod (N) | ZOM-459 row, on-prod column | Outcome | F16 F8 F31 `ZOM-459` `N`; exact |
| P4 | "Can you take care of it for me, the way he laid it out?" · OE 17, 9, 32, 33 | ZOM-509 register row — marked not on prod (N) | ZOM-509 row, on-prod column | Outcome | F17 F8 F31 `ZOM-509` `N`; exact |
| P5 | "Can you take care of it for me, the way he laid it out?" · OE 24, 9, 32, 33 | ZOM-537 register row — marked not on prod (N) | ZOM-537 row, on-prod column | Outcome | F24 F8 F31 `ZOM-537` `N`; exact |
| P6 | "Can you take care of it for me, the way he laid it out?" · OE 26, 9, 32, 33 | ZOM-487 register row — marked not on prod (N) | ZOM-487 row, on-prod column | Outcome | F5 F8 F31 `ZOM-487` `N`; exact |
| P7 | "Can you take care of it for me, the way he laid it out?" · OE 25, 9, 32, 33 | ZOM-444 register row — marked not on prod (N) | ZOM-444 row, on-prod column | Outcome | F11 F8 F31 `ZOM-444` `N`; exact |
| P8 | "Can you take care of it for me, the way he laid it out?" · OE 23, 9, 32, 33 | ZOM-531 register row — marked not on prod (N) | ZOM-531 row, on-prod column | Outcome | F11 F8 F31 `ZOM-531` `N`; exact |
| P9 | "Can you take care of it for me, the way he laid it out?" · OE 11, 13, 32, 33 | ZOM-436 register row — present and marked not on prod (N) | ZOM-436 row, on-prod column | Outcome | F11 F8 F31 `ZOM-436` `N`; exact |
| P10 | "Can you take care of it for me, the way he laid it out?" · OE 22, 32, 33 | ZOM-499 register row — marked on prod (Y) | ZOM-499 row, on-prod column | Outcome | F22 F6 F31 `ZOM-499` `Y`; exact |
| P11 | "Can you take care of it for me, the way he laid it out?" · OE 9, 13, 32, 33 | ZOM-510 register row — marked on prod (Y) | ZOM-510 row, on-prod column | Outcome | F8 F13 F6 F31 `ZOM-510` `Y`; exact |
| P12 | "Can you take care of it for me, the way he laid it out?" · OE 20, 29, 32, 33 | ZOM-503 register row — marked not on prod (N) | ZOM-503 row, on-prod column | Outcome | F20 F29 F7 F6 F31 `ZOM-503` `N`; exact |
| P13 | "Can you take care of it for me, the way he laid it out?" · OE 19, 32, 33 | ZOM-392 register row — marked not on prod (N) | ZOM-392 row, on-prod column | Outcome | F19 F6 F31 `ZOM-392` `N`; exact |
| P14 | "Can you take care of it for me, the way he laid it out?" · OE 27, 31, 32, 33 | ZOM-550 register row — marked not on prod (N) | ZOM-550 row, on-prod column | Outcome | F27 F7 F6 F31 `ZOM-550` `N`; exact |
| P15 | "Can you take care of it for me, the way he laid it out?" · OE 13, 29, 32, 33 | ZOM-503 register row — server change(s) include match3d-backend#52 | ZOM-503 row, server change column | Outcome | F13 F29 `ZOM-503` `#52` (match3d-backend#52); the change named in any recognisable words (brief §4b) |
| P16 | "Can you take care of it for me, the way he laid it out?" · OE 13, 9, 32, 33 | ZOM-510 register row — server change(s) include the Zombie Lane rewards import | ZOM-510 row, server change column | Outcome | F13 F8 `ZOM-510` `Zombie Lane rewards import`; the change named in any recognisable words (brief §4b) |
| P17 | "Can you take care of it for me, the way he laid it out?" · OE 5, 9, 32, 33 | ZOM-487 register row — server change(s) include the boss arena HP table import | ZOM-487 row, server change column | Outcome | F5 F8 `ZOM-487` `boss arena HP table import`; the change named in any recognisable words (brief §4b) |
| P18 | "Can you take care of it for me, the way he laid it out?" · OE 24, 9, 32, 33 | ZOM-537 register row — server change(s) include the economy table import | ZOM-537 row, server change column | Outcome | F24 F8 `ZOM-537` `economy table import`; the change named in any recognisable words (brief §4b) |
| P19 | "Can you take care of it for me, the way he laid it out?" · OE 11, 9, 32, 33 | ZOM-436 register row — server change(s) include the analytics events table import | ZOM-436 row, server change column | Outcome | F11 F8 `ZOM-436` `analytics events table import`; the change named in any recognisable words (brief §4b) |
| P20 | "Leonard also emailed me about the go/no-go, so please handle what he asked for once the register is in the folder." · OE 10, 11, 34 | Register shared with Leonard as commenter | Permission on the register file | Outcome | F9 `leonard.hayes@harmonygames.co` `commenter`; exact role |
| P21 | "reply to Arthur in the DM with what he asked for" · OE 1, 66 | Reply posted in Douglas's DM with Arthur | Slack message in DM D05QQF7V404 | Outcome | F1 `D05QQF7V404`; top level or under the ask |
| P22 | "reply to Arthur in the DM with what he asked for" · OE 32, 66 | Reply — on-prod count of 2 (of 17) | DM reply text | Outcome | F32 `2`; exact count |
| P23 | "reply to Arthur in the DM with what he asked for" · OE 32, 66 | Reply — 15 tickets named as not on prod | DM reply text | Outcome | F32 `15`; exact count |
| P24 | "reply to Arthur in the DM with what he asked for" · OE 16, 32, 66 | Reply — ZOM-459 named among the tickets not on prod | DM reply text | Outcome | F16 F32 `ZOM-459`; key or title |
| P25 | "reply to Arthur in the DM with what he asked for" · OE 17, 32, 66 | Reply — ZOM-509 named among the tickets not on prod | DM reply text | Outcome | F17 F32 `ZOM-509`; key or title |
| P26 | "reply to Arthur in the DM with what he asked for" · OE 24, 32, 66 | Reply — ZOM-537 named among the tickets not on prod | DM reply text | Outcome | F24 F32 `ZOM-537`; key or title |
| P27 | "reply to Arthur in the DM with what he asked for" · OE 26, 32, 66 | Reply — ZOM-487 named among the tickets not on prod | DM reply text | Outcome | F5 F32 `ZOM-487`; key or title |
| P28 | "reply to Arthur in the DM with what he asked for" · OE 25, 32, 66 | Reply — ZOM-444 named among the tickets not on prod | DM reply text | Outcome | F11 F32 `ZOM-444`; key or title |
| P29 | "reply to Arthur in the DM with what he asked for" · OE 23, 32, 66 | Reply — ZOM-531 named among the tickets not on prod | DM reply text | Outcome | F11 F32 `ZOM-531`; key or title |
| P30 | "reply to Arthur in the DM with what he asked for" · OE 13, 32, 66 | Reply — ZOM-436 named among the tickets not on prod | DM reply text | Outcome | F11 F32 `ZOM-436`; key or title |
| P31 | "reply to Arthur in the DM with what he asked for" · OE 20, 29, 32, 66 | Reply — ZOM-503 named among the tickets not on prod | DM reply text | Outcome | F20 F29 F7 F32 `ZOM-503`; key or title |
| P32 | "reply to Arthur in the DM with what he asked for" · OE 30, 32, 66 | Reply — ZOM-557 named among the tickets not on prod | DM reply text | Outcome | F30 F32 `ZOM-557`; key or title |
| P33 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 35–65 | Todo moves — 15 tickets moved back to Todo | Linear state of the not-on-prod tickets | Outcome | F15 F31 `15` `Todo`; exact count |
| P34 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 60 | ZOM-459 moved to Todo | ZOM-459 state | Outcome | F16 F15 F31 `ZOM-459` `Todo`; exact state |
| P35 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 62 | ZOM-509 moved to Todo | ZOM-509 state | Outcome | F17 F15 F31 `ZOM-509` `Todo`; exact state |
| P36 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 54 | ZOM-537 moved to Todo | ZOM-537 state | Outcome | F24 F15 F31 `ZOM-537` `Todo`; exact state |
| P37 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 52 | ZOM-487 moved to Todo | ZOM-487 state | Outcome | F5 F15 F31 `ZOM-487` `Todo`; exact state |
| P38 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 56 | ZOM-444 moved to Todo | ZOM-444 state | Outcome | F11 F15 F31 `ZOM-444` `Todo`; exact state |
| P39 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 58 | ZOM-531 moved to Todo | ZOM-531 state | Outcome | F11 F15 F31 `ZOM-531` `Todo`; exact state |
| P40 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 64 | ZOM-436 moved to Todo | ZOM-436 state | Outcome | F11 F15 F31 `ZOM-436` `Todo`; exact state |
| P41 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 38 | ZOM-392 moved to Todo | ZOM-392 state | Outcome | F19 F15 `ZOM-392` `Todo`; exact state |
| P42 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 44 | ZOM-550 moved to Todo | ZOM-550 state | Outcome | F27 F7 F15 `ZOM-550` `Todo`; exact state |
| P43 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 37–65 (odd) | Todo comments — 15 tickets each get a comment on what still has to go out | New Linear comments | Outcome | F31 `15`; exact count |
| P44 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 61 | ZOM-459 comment — names the plague race table import as the change still to go out | New comment on ZOM-459 | Outcome | F16 F31 `ZOM-459` `plague race table import`; any wording naming that import |
| P45 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 63 | ZOM-509 comment — names the trophy path copy table import as the change still to go out | New comment on ZOM-509 | Outcome | F17 F31 `ZOM-509` `trophy path copy table import`; any wording naming that import |
| P46 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 55 | ZOM-537 comment — names the economy table import as the change still to go out | New comment on ZOM-537 | Outcome | F24 F31 `ZOM-537` `economy table import`; any wording naming that import |
| P47 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 53 | ZOM-487 comment — names the boss arena HP table import as the change still to go out | New comment on ZOM-487 | Outcome | F5 F31 `ZOM-487` `boss arena HP table import`; any wording naming that import |
| P48 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 57 | ZOM-444 comment — names the analytics events table import as the change still to go out | New comment on ZOM-444 | Outcome | F11 F31 `ZOM-444` `analytics events table import`; any wording naming that import |
| P49 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 59 | ZOM-531 comment — names the loadout table import as the change still to go out | New comment on ZOM-531 | Outcome | F11 F31 `ZOM-531` `loadout table import`; any wording naming that import |
| P50 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 65 | ZOM-436 comment — names the analytics events table import as the change still to go out | New comment on ZOM-436 | Outcome | F11 F31 `ZOM-436` `analytics events table import`; any wording naming that import |
| P51 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 41 | ZOM-503 comment — names match3d-backend#52 as the change still to go out | New comment on ZOM-503 | Outcome | F29 F31 `ZOM-503` `match3d-backend#52`; any wording naming that PR |
| P52 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." · OE 39 | ZOM-392 comment — names match3d-backend#41 (a redeploy) as the change still to go out | New comment on ZOM-392 | Outcome | F19 F31 `ZOM-392` `match3d-backend#41`; any wording naming that PR |

## A2 · Grading risks and weight
| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Duplicate risk (per deliverable) / overlap group | Predicted all-fail basis (four Evals bases) · over-specific risk |
|---|---|---|---|---|---|---|---|---|---|
| P1 | no — must not hard-code the sheet title | T9 client QA folder → the row names the exact folder | no | interpretation — card rule 6 → page → folder, with a look-alike folder | 3 | F4 T9 | — | none | none · accept create-in-folder or create-then-move |
| P2 | no | T12 ZOM-547/ZOM-553, T13 → the count rejects them | no | multi-source — 73 comment threads, rule 1, the card comment and the reply-all | 5 | T12 T13 C11 | G1 volume | none; register only | none · accept a separate notes line listing excluded tickets kept apart from the rows |
| P3 | no | T11 → the ticket note names one PR, which is on prod | no | multi-source — inline review comment harmonygames-Games/match3d-backend#38#rc_1, the deploy log (plague race table import on dev, 2025-08-26 10:30) and the PR prod: comment | 5 | C12 T11 | G1 exception (direct) | register; DM and Todo rows are other deliverables | none |
| P4 | no | T11 → the ticket note names one PR, which is on prod | no | multi-source — inline review comment harmonygames-Games/match3d-backend#39#rc_1, the deploy log (trophy path copy table import on dev, 2025-09-02 18:05) and the PR prod: comment | 5 | C13 T11 | G1 exception (direct) | register; DM and Todo rows are other deliverables | none |
| P5 | no | T11 → the ticket note names one PR, which is on prod | no | multi-source — inline review comment harmonygames-Games/match3d-backend#46#rc_1, the deploy log (economy table import on dev, 2025-09-16 14:20) and the PR prod: comment | 5 | C10 T11 | G1 exception (direct) | register; DM and Todo rows are other deliverables | none |
| P6 | no | T11 → the ticket note names one PR, which is on prod | no | multi-source — Arthur's reply comment_zm_beta_oct10_c2 on page_zm_beta_oct10, the deploy log (boss arena HP table import on dev, 2025-09-17 15:50) and the PR prod: comment | 5 | C9 T11 | G1 exception (direct) | register; DM and Todo rows are other deliverables | none |
| P7 | no | T11 → the ticket note names one PR, which is on prod | no | multi-source — Arthur's reply-all (second point), the deploy log (analytics events table import on dev, 2025-09-12 19:20) and the PR prod: comment | 5 | C11 T11 | G1 exception (direct) | register; DM and Todo rows are other deliverables | none |
| P8 | no | T11 → the ticket note names one PR, which is on prod | no | multi-source — Arthur's reply-all (second point), the deploy log (loadout table import on dev, 2025-09-10 17:40) and the PR prod: comment | 5 | C11 T11 | G1 exception (direct) | register; DM and Todo rows are other deliverables | none |
| P9 | no | T11 → its own comment names no server change | no | multi-source — the reply-all adds the ticket, the deploy log shows the analytics events table import on dev only | 5 | C11 T11 | G1 exception (direct) | register; the DM and Todo rows are other deliverables | none |
| P10 | no | T10 Prod deploys tab | no | comparison — rollback then a newer prod: comment against the freeze start | 3 | H2 doc | G1 sample (edge: rolled back then redeployed) | register | none |
| P11 | no | T10 Prod deploys tab | no | interpretation — an import-only change read from the log under the card comment | 3 | H2 doc | G1 sample (edge: import-only Y) | register | none |
| P12 | no | T1 Oliver's all-on-prod summary | no | multi-source — two PRs, the freeze event, the doc and the reviewer identity | 5 | H2 doc + freeze | G1 sample (edge: two server changes) | register | none |
| P13 | no | T1 Oliver's all-on-prod summary | no | comparison — deploy time against review time under the doc | 3 | H2 doc | G1 sample (edge: Approve after the deploy) | register | none |
| P14 | no | T1 Oliver's all-on-prod summary | no | multi-source — the freeze event, the doc and the reviewer identity | 5 | H2 doc + freeze | G1 sample (edge: freeze without Arthur) | register | none |
| P15 | no | none | no | lookup — named in the ticket note | 3 | F13 | G2 sample (edge: second change) | register; the Todo comment (P44–P50) is another deliverable | none · phrase broadly |
| P16 | no | none | no | interpretation — import counted through the card comment | 3 | F13 | G2 sample (edge: import only) | register; the Todo comment (P44–P50) is another deliverable | none · phrase broadly |
| P17 | no | T11 ticket notes name one PR only | no | interpretation — the page reply names the import outright | 3 | C9 | G2 sample (exception) | register; the Todo comment (P44–P50) is another deliverable | none · phrase broadly |
| P18 | no | T11 ticket notes name one PR only | no | interpretation — the inline review comment names the import outright | 3 | C10 | G2 sample (exception) | register; the Todo comment (P44–P50) is another deliverable | none · phrase broadly |
| P19 | no | T11 ticket notes name one PR only | no | interpretation — the reply-all names the import outright | 3 | C11 | G2 sample (exception) | register; the Todo comment (P44–P50) is another deliverable | none · phrase broadly |
| P20 | no | none | no | lookup — one email names the grantee and role | 1 | F9 | — | none | none · a direct file share (not the folder) |
| P21 | no | T14 #zombie-match3d copy is extra, not a substitute | no | lookup — the DM is the ask's own channel | 1 | F1 | — | none | none · phrase broadly (thread or top level) |
| P22 | no | T1, T12 → 9 or 10 of 18 rejected | no | multi-source — the count only the full audit produces | 5 | F31 | G3 volume (on prod) | DM only | none · number or word |
| P23 | no | T12 | no | multi-source — the count only the full audit produces | 5 | F31 | G3 volume | DM only | none |
| P24 | no | T11 | no | multi-source — same determination as the register row, required again by the ask ("which ones aren't") | 5 | C12 | G3 exception (direct) | DM; register row is another deliverable (gate 6) | none |
| P25 | no | T11 | no | multi-source — same determination as the register row, required again by the ask ("which ones aren't") | 5 | C13 | G3 exception (direct) | DM; register row is another deliverable (gate 6) | none |
| P26 | no | T11 | no | multi-source — same determination as the register row, required again by the ask ("which ones aren't") | 5 | C10 | G3 exception (direct) | DM; register row is another deliverable (gate 6) | none |
| P27 | no | T11 | no | multi-source — same determination as the register row, required again by the ask ("which ones aren't") | 5 | C9 | G3 exception (direct) | DM; register row is another deliverable (gate 6) | none |
| P28 | no | T11 | no | multi-source — same determination as the register row, required again by the ask ("which ones aren't") | 5 | C11 | G3 exception (direct) | DM; register row is another deliverable (gate 6) | none |
| P29 | no | T11 | no | multi-source — same determination as the register row, required again by the ask ("which ones aren't") | 5 | C11 | G3 exception (direct) | DM; register row is another deliverable (gate 6) | none |
| P30 | no | T11 | no | multi-source — same determination as the register row, required again by the ask ("which ones aren't") | 5 | C11 | G3 exception (direct) | DM; register row is another deliverable (gate 6) | none |
| P31 | no | T1 Oliver's summary | no | multi-source — two PRs, freeze and reviewer identity | 5 | H2 doc | G3 sample (#52 in the freeze) | DM | none |
| P32 | no | T1 Oliver's summary | no | comparison — prod: then rollback: comment | 3 | H2 doc | G3 sample (#54 rolled back) | DM | none |
| P33 | no | T7 client card → In Validation rejected | no | multi-source — the count only the full audit produces | 5 | F2 rule 5 | G4 volume | Todo only | none |
| P34 | no | T7 (In Validation) | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | C12 | G4 exception (direct) | Todo state; comment row is a separate write | none |
| P35 | no | T7 (In Validation) | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | C13 | G4 exception (direct) | Todo state; comment row is a separate write | none |
| P36 | no | T7 (In Validation) | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | C10 | G4 exception (direct) | Todo state; comment row is a separate write | none |
| P37 | no | T7 (In Validation) | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | C9 | G4 exception (direct) | Todo state; comment row is a separate write | none |
| P38 | no | T7 (In Validation) | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | C11 | G4 exception (direct) | Todo state; comment row is a separate write | none |
| P39 | no | T7 (In Validation) | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | C11 | G4 exception (direct) | Todo state; comment row is a separate write | none |
| P40 | no | T7 (In Validation) | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | C11 | G4 exception (direct) | Todo state; comment row is a separate write | none |
| P41 | no | T2 Douglas's Sep 22 claim | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | H2 doc | G4 sample | Todo state | none |
| P42 | no | T4 #50 thread | no | interpretation — applies card rule 5 to the ticket's N value; the discovery itself is weighted on the register row | 3 | H2 doc | G4 sample | Todo state | none |
| P43 | no | none | no | multi-source — the count only the full audit produces | 5 | F2 rule 5 | G5 volume | comments only | none |
| P44 | no — wording delegated | T11 (a comment naming only the PR fails) | no | interpretation — names the change the register row already holds | 3 | C12 | G5 exception (direct) | comment; register server-change row is another deliverable | none · phrase broadly |
| P45 | no — wording delegated | T11 (a comment naming only the PR fails) | no | interpretation — names the change the register row already holds | 3 | C13 | G5 exception (direct) | comment; register server-change row is another deliverable | none · phrase broadly |
| P46 | no — wording delegated | T11 (a comment naming only the PR fails) | no | interpretation — names the change the register row already holds | 3 | C10 | G5 exception (direct) | comment; register server-change row is another deliverable | none · phrase broadly |
| P47 | no — wording delegated | T11 (a comment naming only the PR fails) | no | interpretation — names the change the register row already holds | 3 | C9 | G5 exception (direct) | comment; register server-change row is another deliverable | none · phrase broadly |
| P48 | no — wording delegated | T11 (a comment naming only the PR fails) | no | interpretation — names the change the register row already holds | 3 | C11 | G5 exception (direct) | comment; register server-change row is another deliverable | none · phrase broadly |
| P49 | no — wording delegated | T11 (a comment naming only the PR fails) | no | interpretation — names the change the register row already holds | 3 | C11 | G5 exception (direct) | comment; register server-change row is another deliverable | none · phrase broadly |
| P50 | no — wording delegated | T11 (a comment naming only the PR fails) | no | interpretation — names the change the register row already holds | 3 | C11 | G5 exception (direct) | comment; register server-change row is another deliverable | none · phrase broadly |
| P51 | no — wording delegated | none | no | interpretation — names the PR the register row holds | 3 | H2 doc | G5 sample | comment | none · phrase broadly |
| P52 | no — wording delegated | none | no | interpretation — names the PR the register row holds | 3 | H2 doc | G5 sample | comment | none · phrase broadly |

## B · OE trace
| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |
|---|---|---|---|
| OE 1 | discovery | P21 (and the DM rows) | no — a read; graded through the row(s) its result decides |
| OE 2 | discovery | P2–P14 (rules) | no — a read; graded through the row(s) its result decides |
| OE 3 | discovery | P2, P16 | no — a read; graded through the row(s) its result decides |
| OE 4 | discovery | P1 | no — a read; graded through the row(s) its result decides |
| OE 5 | discovery | P6, P17, P27, P37, P47 | no — a read; graded through the row(s) its result decides |
| OE 6 | discovery | P1 | no — a read; graded through the row(s) its result decides |
| OE 7 | discovery | P10–P14 | no — a read; graded through the row(s) its result decides |
| OE 8 | discovery | P12, P14, P31, P42 | no — a read; graded through the row(s) its result decides |
| OE 9 | discovery | P2, P6–P9, P11, P16–P19 | no — a read; graded through the row(s) its result decides |
| OE 10 | discovery | P20 | no — a read; graded through the row(s) its result decides |
| OE 11 | discovery | P2, P7–P9, P19, P28–P30 | no — a read; graded through the row(s) its result decides |
| OE 12 | discovery | P2 | no — a read; graded through the row(s) its result decides |
| OE 13 | discovery | P2, P9, P15, P16 | no — a read; graded through the row(s) its result decides |
| OE 14 | discovery (calculation) | P2 | no — a read; graded through the row(s) its result decides |
| OE 15 | discovery | P10–P14 | no — a read; graded through the row(s) its result decides |
| OE 16 | discovery | P3, P24, P34, P44 | no — a read; graded through the row(s) its result decides |
| OE 17 | discovery | P4, P25, P35, P45 | no — a read; graded through the row(s) its result decides |
| OE 18 | discovery | P23, P33 (volume) | no — a read; graded through the row(s) its result decides |
| OE 19 | discovery | P13, P41, P52 | no — a read; graded through the row(s) its result decides |
| OE 20 | discovery | P12, P31 | no — a read; graded through the row(s) its result decides |
| OE 21 | discovery | P23, P33 (volume) | no — a read; graded through the row(s) its result decides |
| OE 22 | discovery | P10 | no — a read; graded through the row(s) its result decides |
| OE 23 | discovery | P8, P29, P39, P49 | no — a read; graded through the row(s) its result decides |
| OE 24 | discovery | P5, P18, P26, P36, P46 | no — a read; graded through the row(s) its result decides |
| OE 25 | discovery | P7, P28, P38, P48 | no — a read; graded through the row(s) its result decides |
| OE 26 | discovery | P6, P17, P27, P37, P47 | no — a read; graded through the row(s) its result decides |
| OE 27 | discovery | P14, P42 | no — a read; graded through the row(s) its result decides |
| OE 28 | discovery | P23, P33 (volume) | no — a read; graded through the row(s) its result decides |
| OE 29 | discovery | P12, P15, P31, P51 | no — a read; graded through the row(s) its result decides |
| OE 30 | discovery | P32 | no — a read; graded through the row(s) its result decides |
| OE 31 | discovery | P12, P14 | no — a read; graded through the row(s) its result decides |
| OE 32 | discovery (calculation) | P2–P19, P22–P32 | no — a read; graded through the row(s) its result decides |
| OE 33 | write | P1–P19 | no — its result is graded on the artifact it writes |
| OE 34 | write | P20 | no — its result is graded on the artifact it writes |
| OE 35 | discovery | P33–P42 | no — a read; graded through the row(s) its result decides |
| OE 36 | write | P33 (volume) | no — its result is graded on the artifact it writes |
| OE 37 | write | P43 (volume) | no — its result is graded on the artifact it writes |
| OE 38 | write | P41 | no — its result is graded on the artifact it writes |
| OE 39 | write | P52 | no — its result is graded on the artifact it writes |
| OE 40 | write | P33 (volume) | no — its result is graded on the artifact it writes |
| OE 41 | write | P51 | no — its result is graded on the artifact it writes |
| OE 42 | write | P33 (volume) | no — its result is graded on the artifact it writes |
| OE 43 | write | P43 (volume) | no — its result is graded on the artifact it writes |
| OE 44 | write | P42 | no — its result is graded on the artifact it writes |
| OE 45 | write | P43 (volume) | no — its result is graded on the artifact it writes |
| OE 46 | write | P33 (volume) | no — its result is graded on the artifact it writes |
| OE 47 | write | P43 (volume) | no — its result is graded on the artifact it writes |
| OE 48 | write | P33 (volume) | no — its result is graded on the artifact it writes |
| OE 49 | write | P43 (volume) | no — its result is graded on the artifact it writes |
| OE 50 | write | P33 (volume) | no — its result is graded on the artifact it writes |
| OE 51 | write | P43 (volume) | no — its result is graded on the artifact it writes |
| OE 52 | write | P37 | no — its result is graded on the artifact it writes |
| OE 53 | write | P47 | no — its result is graded on the artifact it writes |
| OE 54 | write | P36 | no — its result is graded on the artifact it writes |
| OE 55 | write | P46 | no — its result is graded on the artifact it writes |
| OE 56 | write | P38 | no — its result is graded on the artifact it writes |
| OE 57 | write | P48 | no — its result is graded on the artifact it writes |
| OE 58 | write | P39 | no — its result is graded on the artifact it writes |
| OE 59 | write | P49 | no — its result is graded on the artifact it writes |
| OE 60 | write | P34 | no — its result is graded on the artifact it writes |
| OE 61 | write | P44 | no — its result is graded on the artifact it writes |
| OE 62 | write | P35 | no — its result is graded on the artifact it writes |
| OE 63 | write | P45 | no — its result is graded on the artifact it writes |
| OE 64 | write | P40 | no — its result is graded on the artifact it writes |
| OE 65 | write | P50 | no — its result is graded on the artifact it writes |
| OE 66 | write | P21–P32 | no — its result is graded on the artifact it writes |

## C · Process candidates — three-condition test
| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |
|---|---|---|---|---|---|---|
| — | "once the register is in the folder" (share after the register exists) | P20 grades the permission on the register file itself, which can only exist after the file | n/a | fails — P20 captures it | n/a | no Process row; covered by P20 (F9, F31) |
| — | "no need to wait on me" | The moves and comments exist (P33–P52) | n/a | fails — P33, P43 capture it | n/a | no Process row; covered by P33, P43 (F2, F15) |
| — | "reply here when it's done" (reply after the register) | The reply's content can only be right after the full audit; ordering adds no graded value | n/a | fails — P22, P23 capture the content | n/a | no Process row (F1, F32) |

## D · Spot-check groups
| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |
|---|---|---|---|---|---|
| G1 | Register on-prod column, F31, 17 tickets: `ZOM-459` `ZOM-509` `ZOM-336` `ZOM-392` `ZOM-503` `ZOM-518` `ZOM-499` `ZOM-531` `ZOM-537` `ZOM-444` `ZOM-487` `ZOM-550` `ZOM-435` `ZOM-557` `ZOM-510` `ZOM-256` `ZOM-436` | P10 ZOM-499 (rolled back then redeployed, Y), P11 ZOM-510 (import-only Y), P12 ZOM-503 (two changes, #52 in the freeze), P13 ZOM-392 (Approve after deploy), P14 ZOM-550 (freeze without Arthur). Exceptions graded directly, not sampled: P3–P9 (each singled out by an amendment record) | P2 | none — bundle (Rubric Writing §7; Eval 2.2) | no — the prompt asks for the register as a whole; per-ticket cells are repetitive members |
| G2 | Register server-change column, F31, same 17 tickets | P15 ZOM-503 (second PR #52), P16 ZOM-510 (import only), P17 ZOM-487, P18 ZOM-537, P19 ZOM-436 (the hidden imports, one per amendment kind: page reply, inline review comment, reply-all) | P2 | none — bundle (Rubric Writing §7; Eval 2.2) | no |
| G3 | Reply's not-on-prod list, F32, 15 keys: `ZOM-336` `ZOM-392` `ZOM-503` `ZOM-518` `ZOM-550` `ZOM-435` `ZOM-557` `ZOM-256` `ZOM-487` `ZOM-537` `ZOM-444` `ZOM-531` `ZOM-459` `ZOM-509` `ZOM-436` | P31 ZOM-503 (two changes), P32 ZOM-557 (rollback). Exceptions direct: P24–P30 | P23 (count 15); P22 (on-prod count 2) | none — bundle (Rubric Writing §7; Eval 2.2) | no — the told facts are the count and the list; list members are repetitive |
| G4 | Todo moves, F31, the same 15 tickets | P41 ZOM-392 (late Approve), P42 ZOM-550 (freeze). Exceptions direct: P34–P40 | P33 | none — bundle (Rubric Writing §7; Eval 2.2) | no — 15 separate writes of one rule |
| G5 | Todo comments, F31, the same 15 tickets | P51 ZOM-503 (#52), P52 ZOM-392 (#41 redeploy). Exceptions direct: P44–P50 | P43 | none — bundle (Rubric Writing §7; Eval 2.2) | no |

## E · Summary
Rows 52 · Outcome 52 · Process candidates 0 — ≥ 1 Outcome ☑ (no Process ratio: QC Spec V2 and the Evals override fail only zero Outcome) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ (P2, P22, P23, P33, P43) · predicted all-fail rows = 0 ☑ (harness tolerance 0; /rubric fails at ≥ 2; no row rests on the four Evals bases — every value is persona-reachable, see Visibility proof)
Failure diversity: largest unit of discovery is the rules card (F2) at 100% of the weight, then the ticket comments (F13) and the candidate list (F12) (≤ 50% ☒ — every register, reply and Todo row runs through the rules card, which is the task itself; same design finding as the accepted Frederick account-handover task, Self-review §6) · chains landing on distinct rows ☑ (C9 page reply P6 P17 P27 P37 P47; C10 #46 inline P5 P18 P26 P36 P46; C11 reply-all P7 P8 P9 P19 P28 P29 P30 P38 P39 P40 P48 P49 P50; C12 #38 inline P3 P24 P34 P44; C13 #39 inline P4 P25 P35 P45; H2 doc + freeze P10–P14 P31 P32 P41 P42)
Bands: 5 ×22 · 3 ×28 · 1 ×2 (total weight 196)
Set size: 52 rows for 12.75 h (reference: 31 criteria for a ~10-hour task; four prompt-required deliverables — register, share, reply, Todo moves with comments — each graded once; no fact graded twice in one deliverable)
Coverage: requirements 7/7 · OEs 66/66 · writes 7/7 · told facts 2/2 (on-prod count, not-on-prod list) · friction 0/0
Four prohibitions: ☑ unstated expectations (no row for the Leonard email reply, the #zombie-match3d copy or "no new tickets") ☑ conclusions on ambiguous evidence (none — ledger §F risks 1–6 are representational) ☑ grading the distractor (traps graded by how they are handled: counts and N values) ☑ hard-coded titles/phrasings (sheet title and comment wording delegated)
Blocking: none — no UGT defect, no infeasible write, no unverified visibility (diversity.authority_share is a reported design finding, not a blocker the plan can fix honestly)

Baseline replay (the six round-3 runs, graded row by row from their write payloads; scratch grade3.py): run scores 0.352 · 0.622 · 0.255 · 0.352 · 0.638 · 0.255 → average 41.2%, SD 0.159, pass@1 0/6, 3 failure patterns (largest 33%) — every difficulty gate PASS. Rows that failed all six runs (valid, data reachable, for /create-allfail): P3 P4 P5 P18 P22 P23 P24 P25 P26 P33 P34 P35 P36 P43 P44 P45 P46 — all trace to the three inline review comments (#38, #39, #46) that no run incorporated, and the volume rows that need them.

Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)

`python3 Task_Authoring-2/tools/persona_view.py check-sql douglas Task_Authoring-2/task_inputs/01_Universe_Inject.sql --load-bearing lb.txt` (15 ids: the §B scoped records plus the §E Slack and folder decoys):

```
CHECK-SQL as douglas <douglas@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert d_69fcebc484d472907b0b5c - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert d_d71300168ca5dffa4db8b3 - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert f_470ae81236d5bd39045dc1 - persona owns the file
[YES LB] L13 gdrive.drive_files insert f_78bedc46245090a160d2dd - persona owns the file
[YES LB] L15 gdocs.docs_documents insert f_470ae81236d5bd39045dc1 - persona owns the file
[YES LB] L18 gsheets.sheets_spreadsheets insert f_78bedc46245090a160d2dd - persona owns the file
[YES LB] L21 gsheets.sheets_sheets insert f_78bedc46245090a160d2dd, f_78bedc46245090a160d2dd#0 - persona owns the file
[YES LB] L23 gsheets.sheets_sheets insert f_78bedc46245090a160d2dd, f_78bedc46245090a160d2dd#1 - persona owns the file
[YES LB] L38 slack.slack_messages insert 3a2e99ef807fc28ef39b8d6973a44427, C0880U9751A/1748450537.204611 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L41 slack.slack_messages insert 9ba4f3770f458826c7503e1aa0992acc, C0880U9751A/1758295268.611352 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L43 slack.slack_messages insert f5dde99eaea0ac1773ca37e48871cb60, D05QQF7V404/1758571837.284511 - persona EMPLOYEE_0031_SLACK_ID is in members of im D05QQF7V404
[YES LB] L45 slack.slack_messages insert 10613025eb309bac6e0fb32438625484, C0880U9751A/1758991212.775031 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L47 slack.slack_messages insert 42f263bfce69ae5a4ef068383ae66c4a, C0880U9751A/1759253506.093318 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L49 slack.slack_messages insert 1e5d5d2bf50901f0d7376627d6f539e8, D05QQF7V404/1759266764.508127 - persona EMPLOYEE_0031_SLACK_ID is in members of im D05QQF7V404
[YES LB] L51 slack.slack_messages insert 81531d5f36d48a5d2028a22405aed65e, C0880U9751A/1758937233.118904 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L53 slack.slack_messages insert 33339417b07ab83542fc971a41320a36, C0880U9751A/1758938751.402267 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES] L55 slack.slack_messages insert bde0c0ff791441e66d57cdb2de8f0f51, C0880U9751A/1758938832.553908 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L68 gmail.gmail_threads insert douglas@harmonygames.co/1844721277206562572 - row user_email is the persona (douglas@harmonygames.co)
[YES LB] L71 gmail.gmail_messages insert douglas@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>, douglas - row user_email is the persona (douglas@harmonygames.co)
[YES LB] L96 gmail.gmail_messages insert douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>, douglas - row user_email is the persona (douglas@harmonygames.co)
[YES] L153 gcal.gcal_events insert evt_b6eda0097a341f225ad5d2 - persona is an attendee and holds its own copy evt_0f489eb7fb46ada9660881 (same ical_uid and start) on douglas@harmonygames.co
[YES LB] L156 gcal.gcal_events insert evt_0f489eb7fb46ada9660881 - event is on the persona's own calendar douglas@harmonygames.co
[YES] L158 gcal.gcal_events insert evt_e3c3cd6a8dec19d0e7b123 - persona is an attendee and holds its own copy evt_0f489eb7fb46ada9660881 (same ical_uid and start) on douglas@harmonygames.co
[YES] L160 gcal.gcal_events insert evt_5e9adacd9af476a6402dfa - persona is an attendee and holds its own copy evt_0f489eb7fb46ada9660881 (same ical_uid and start) on douglas@harmonygames.co
[YES] L162 gcal.gcal_events insert evt_bbe10af026c7f633387e2d - persona is an attendee and holds its own copy evt_0f489eb7fb46ada9660881 (same ical_uid and start) on douglas@harmonygames.co
verdict: PASS (0 load-bearing rows not visible)
```

The six NO rows of the full output are the sender's and cc's own mailbox copies of the two emails (arthur.blake@ and leonard.hayes@ mailboxes, L78, L80, L87, L89, L115, L134); none is used by any fact.

`python3 Task_Authoring-2/tools/persona_view.py can-see douglas slack <id>` (base records):

```
douglas slack D079SNE2TL4/1759256193.859279: YES
douglas slack D079SNE2TL4/1759269524.769369: YES
```

## F · Shortcut probe
```
SHORTCUT PROBE as douglas <douglas@harmonygames.co> · values 09_Rubric_Writing_Plan.md (28 values, 2 populations, sha 087e8dd2655b) · k 3 · services all · sql 01_Universe_Inject.sql
HIT sql:gmail.gmail_messages L96:douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> holds 6/28 values (k=3): `analytics events table import` · `leonard.hayes@harmonygames.co` · `loadout table import` · `ZOM-436` · `ZOM-444` · `ZOM-531`
SKIPPED value:"17" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"Y" (shorter than 3 characters)
SKIPPED value:"Y" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"N" (shorter than 3 characters)
SKIPPED value:"2" (shorter than 3 characters)
SKIPPED value:"15" (shorter than 3 characters)
SKIPPED value:"15" (shorter than 3 characters)
SKIPPED value:"15" (shorter than 3 characters)
verdict: HITS (1)
```
SHORTCUT-OK: sql:gmail.gmail_messages L96:douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> — this is Arthur's reply-all, the designed hidden amendment (ledger F11, chain C11, manifest K16): it is reached only by opening the whole thread of Leonard's email (a sender search returns Leonard's message), it names no on-prod value for ZOM-444/ZOM-436/ZOM-531 itself (the deploy log f_78bedc46245090a160d2dd decides dev vs prod), and it covers 6 of 28 values, none of the inline-comment or rule-decided rows. Leonard's address in it is the cc line; the share request comes from his own message L71.

## Self-review

No-criterion-text scan: the plan holds noun phrases and values only; no drafted criterion titles.

1. Re-read as /rubric (3_Rubrics_Eval.md 1.4, 3.1): every requirement R1–R7 of the ledger has rows on the correct artifact — register (P1–P19), share (P20), reply (P21–P32), Todo moves (P33–P42), comments (P43–P52). Both told facts (count, list) have reply rows. The exclusions ZOM-547/ZOM-553 are graded affirmatively through the volume rows P2, P22, P23 (no prohibition-only row). Each population has its volume row and direct exception rows; samples ≤ 5 per group.
2. Re-verified: every literal was re-read in this run — the 17 tickets and their Y/N values recomputed from the SQL PR rows (L164–L713) and the deploy log grid (L23) under the doc (L15) and freeze (L156); the amendment records L36, L96, L211, L243, L463; the Todo state name from linear data.json team_ZOM states (hg.py); the folder L6 and Leonard's address L71. The /oe PASS report (score 5) verified the same values independently.
3. Predicted all-fail re-check: every scoped record behind the cited F-ids is YES for douglas (Visibility proof above: check-sql verdict PASS, 2 can-see YES); every write maps to a catalog tool (gdrive_create_file, gdrive_share_file, slack_send_message, linear_update_issue, linear_create_comment); no friction; no evidence outside the persona's view. Predicted all-fail rows on the four bases: 0. The 17 rows that failed all six baseline runs (§E) are genuine model failures — run 3 even opened #38#rc_1 and #39#rc_1 and kept ZOM-459/ZOM-509 as Y — and go to /create-allfail with VALID justifications.
4. Weights by work kind: 5 where the result needs a hidden amendment, the freeze or a full-audit count; 3 for a single comparison, for naming a change the register already holds, or for a Todo move that applies rule 5 to an N value already graded on the register (P34–P42, lowered from 5 so that no more than 7 rows — the hidden reply-list rows — sit where a reviewer could argue one level lower); 1 for the share and the DM placement. Bands 5 ×22 · 3 ×28 · 1 ×2.
5. Atomicity: one ticket × one column per register row; one ticket per reply-list row; one write per Todo row; ZOM-503's two changes graded only on #52 (P15), so no row bundles two PRs.
6. Shortcut and diversity: the probe output is in §F with each HIT dispositioned. The rules card F2 is in the Depends-on closure of every row (100%); the card is the task's own instruction source, so the 50% cap cannot be met without falsifying the ledger's dependencies. This is reported as a design finding, as in the accepted Frederick account-handover task, and the human decides. Independent chains land on distinct rows (§E).

| P | Counter-reading | Resolution (evidence) |
|---|---|---|
| P1 | counter-reading: valid fails: a run creates the sheet in its own Drive and then moves it | accepted — the row grades the final parent d_69fcebc484d472907b0b5c (L6), route ungraded; wrong passes: the client QA folder d_d71300168ca5dffa4db8b3 fails the exact folder |
| P2 | counter-reading: valid fails: a run adds a notes line listing ZOM-547/ZOM-553 as excluded | accepted if kept apart from the ticket rows (brief §4b); wrong passes: 18 or 19 rows (547/553 kept) fail the count — runs 1, 3, 4, 6 had 18 (baseline replay) |
| P3 | counter-reading: valid fails: ZOM-459 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-459 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P4 | counter-reading: valid fails: ZOM-509 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-509 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P5 | counter-reading: valid fails: ZOM-537 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-537 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P6 | counter-reading: valid fails: ZOM-487 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-487 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P7 | counter-reading: valid fails: ZOM-444 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-444 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P8 | counter-reading: valid fails: ZOM-531 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-531 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P9 | counter-reading: valid fails: ZOM-436 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-436 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P10 | counter-reading: valid fails: ZOM-499 written as "yes" | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-499 Y re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P11 | counter-reading: valid fails: ZOM-510 written as "yes" | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-510 Y re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P12 | counter-reading: valid fails: ZOM-503 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-503 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P13 | counter-reading: valid fails: ZOM-392 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-392 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P14 | counter-reading: valid fails: ZOM-550 written as "not on prod"/"No" instead of N | Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — ZOM-550 N re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31) |
| P15 | counter-reading: valid fails: ZOM-503's change written as "HP table", "economy sheet import" or "#52" without the repo | any recognisable words are accepted (brief §4b, "phrase broadly"); wrong passes: a cell naming only the PR fails (run 2 listed only #48 for ZOM-487, f_78bedc46245090a160d2dd row 2025-09-17 15:50 shows the import) |
| P16 | counter-reading: valid fails: ZOM-510's change written as "HP table", "economy sheet import" or "#52" without the repo | any recognisable words are accepted (brief §4b, "phrase broadly"); wrong passes: a cell naming only the PR fails (run 2 listed only #48 for ZOM-487, f_78bedc46245090a160d2dd row 2025-09-17 15:50 shows the import) |
| P17 | counter-reading: valid fails: ZOM-487's change written as "HP table", "economy sheet import" or "#52" without the repo | any recognisable words are accepted (brief §4b, "phrase broadly"); wrong passes: a cell naming only the PR fails (run 2 listed only #48 for ZOM-487, f_78bedc46245090a160d2dd row 2025-09-17 15:50 shows the import) |
| P18 | counter-reading: valid fails: ZOM-537's change written as "HP table", "economy sheet import" or "#52" without the repo | any recognisable words are accepted (brief §4b, "phrase broadly"); wrong passes: a cell naming only the PR fails (run 2 listed only #48 for ZOM-487, f_78bedc46245090a160d2dd row 2025-09-17 15:50 shows the import) |
| P19 | counter-reading: valid fails: ZOM-436's change written as "HP table", "economy sheet import" or "#52" without the repo | any recognisable words are accepted (brief §4b, "phrase broadly"); wrong passes: a cell naming only the PR fails (run 2 listed only #48 for ZOM-487, f_78bedc46245090a160d2dd row 2025-09-17 15:50 shows the import) |
| P20 | counter-reading: valid fails: sharing the folder instead of the file | Leonard asked to have it shared "directly" with comment access (L71, douglas@harmonygames.co/1844721277206562572); a folder share is not the file share the email asks for, and all six runs shared the file |
| P21 | counter-reading: valid fails: reply posted under the ask as a thread reply | accepted — top level or thread (brief §4b W4, D05QQF7V404/1759266764.508127); a #zombie-match3d copy is extra (T14) |
| P22 | counter-reading: valid fails: "two of seventeen" in words | accepted — number or word; wrong passes: "5 of 17" (runs 2, 5) and "9 are on prod" (runs 1, 4) fail |
| P23 | counter-reading: valid fails: the 15 listed as titles, not keys | the count is graded, not the form; wrong passes: 8, 9 or 12 listed (baseline) fail |
| P24 | counter-reading: valid fails: ZOM-459 given by title, not key | key or title accepted; wrong passes: ZOM-459 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P25 | counter-reading: valid fails: ZOM-509 given by title, not key | key or title accepted; wrong passes: ZOM-509 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P26 | counter-reading: valid fails: ZOM-537 given by title, not key | key or title accepted; wrong passes: ZOM-537 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P27 | counter-reading: valid fails: ZOM-487 given by title, not key | key or title accepted; wrong passes: ZOM-487 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P28 | counter-reading: valid fails: ZOM-444 given by title, not key | key or title accepted; wrong passes: ZOM-444 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P29 | counter-reading: valid fails: ZOM-531 given by title, not key | key or title accepted; wrong passes: ZOM-531 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P30 | counter-reading: valid fails: ZOM-436 given by title, not key | key or title accepted; wrong passes: ZOM-436 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P31 | counter-reading: valid fails: ZOM-503 given by title, not key | key or title accepted; wrong passes: ZOM-503 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P32 | counter-reading: valid fails: ZOM-557 given by title, not key | key or title accepted; wrong passes: ZOM-557 listed under "on prod" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks "which ones aren't") |
| P33 | counter-reading: valid fails: a run moves a 16th ticket (e.g. ZOM-547) | that is a wrong move under F11 and the count rightly fails; the ZOM Todo state is named by F15 (team_ZOM states in linear data.json) |
| P34 | counter-reading: valid fails: ZOM-459 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-459 is Done at the clock (linear data.json) |
| P35 | counter-reading: valid fails: ZOM-509 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-509 is Done at the clock (linear data.json) |
| P36 | counter-reading: valid fails: ZOM-537 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-537 is Done at the clock (linear data.json) |
| P37 | counter-reading: valid fails: ZOM-487 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-487 is Done at the clock (linear data.json) |
| P38 | counter-reading: valid fails: ZOM-444 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-444 is Done at the clock (linear data.json) |
| P39 | counter-reading: valid fails: ZOM-531 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-531 is Done at the clock (linear data.json) |
| P40 | counter-reading: valid fails: ZOM-436 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-436 is Done at the clock (linear data.json) |
| P41 | counter-reading: valid fails: ZOM-392 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-392 is Done at the clock (linear data.json) |
| P42 | counter-reading: valid fails: ZOM-550 moved to Backlog or In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; ZOM-550 is Done at the clock (linear data.json) |
| P43 | counter-reading: valid fails: one ticket gets two comments | the row counts tickets commented (15), not comments |
| P44 | counter-reading: valid fails: ZOM-459's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |
| P45 | counter-reading: valid fails: ZOM-509's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |
| P46 | counter-reading: valid fails: ZOM-537's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |
| P47 | counter-reading: valid fails: ZOM-487's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |
| P48 | counter-reading: valid fails: ZOM-444's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |
| P49 | counter-reading: valid fails: ZOM-531's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |
| P50 | counter-reading: valid fails: ZOM-436's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |
| P51 | counter-reading: valid fails: ZOM-503's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |
| P52 | counter-reading: valid fails: ZOM-392's comment phrases the change loosely | wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod) |

Unresolved: diversity.authority_share (rules card at 100% of the weight) — a structural design finding for the human to accept, not a value or visibility gap.
