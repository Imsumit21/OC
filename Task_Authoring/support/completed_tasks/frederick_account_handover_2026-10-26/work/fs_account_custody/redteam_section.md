RED TEAM UNAVAILABLE: redteam_review: set REDTEAM_MODEL or pass --model (no REDTEAM_* environment configured — error)

Substitute: one independent reviewer (a fresh subagent given only the v1 design, manifest, `planned_text.json`, the assignment and the
eval rules, with read access to the base) red-teamed v1. Every finding was re-verified against the base before acting:

| Finding | Source | Disposition with evidence |
|---|---|---|
| 1 Blocker: AdMob is a live account Fred was made admin of on Aug 25; v1 left it out | subagent | verified (D05S58U4SAK/1756147086.813789, /1756147145.162239; frederick.stone@harmonygames.co/1841453218828344296); fixed: AdMob export {SW_admob} in the sweep, COMPANY-HELD, money Y from AD_REVENUE admob Sep paid (snowflake.json /tables/35) → KEEP; T15 lookalike |
| 2 Major: Sep 29 card cites the Sep 30 sweep | subagent | verified; fixed: card moved to 2025-09-30T20:41:16Z after the last export, text "today's sweep folder" ({H1}) |
| 3 Major: Node's YouTube/Google Ads/MMP access never revoked in base | subagent | verified (C08MCEP1B9B/1732203251.229079, /1727063903.359939, /1727689480.986899); fixed: Removed users / Linked managers tabs record removal 2024-12-20; only Meta keeps Node |
| 4 Major: Discord/LinkedIn admins are personal profiles under rule 3 | subagent | fixed: exports list each holder's harmonygames.co login; rule 3 reworded to "a person's harmonygames.co address"; group inboxes excluded (planned_text H1_DESC) |
| 5 Major: "TikTok Business Center" vs the social profile; second TikTok account | subagent | verified (D05S58U4SAK/1759155793.573669); fixed: export is the @harmonygames profile; the Sep 29 account is listed as deleted; rule 1 drops deleted accounts |
| 6 Major: transfer count 5 vs 6 | subagent | fixed: hub asks "how many you've marked TRANSFER" (D05S58U4SAK/{HUB_TS}) |
| 7 Minor: rule-text gaps (Instagram "second owner", rule 6 wording, Super admin, Adjoe "spend", Google Ads campaign status) | subagent | fixed: "Leonard is added as an owner"; column "company holders"; rule 2 includes Super admin; doc says "Spend or a charge the vendor has agreed in writing to drop"; Google Ads exports state 0 enabled campaigns (UAC last spend 2025-04-10, snowflake.json /tables/0) |
| 8 Minor: Adjoe thread parent wrong | subagent | verified; fixed to C07UCC631A6/1757346020.196019 in T7, C2 and §1 |
| 9 Major: most traps pointed to by name (expected 80–90%) | subagent | partly fixed: the hub no longer names the money definition, the March sheet or the amendments; the card no longer announces its comment or the email; the Partners tab and the Unity invite moved to second tabs; added Arthur's confident wrong summary (T14) and a Snowflake-only fact (C5). Residual risk recorded in the Self-review Unresolved line; the pre-check measures it |
| 10 Major: v1's 63-call budget padded (~40–50 real) | subagent | fixed: removed read-backs and absence searches; added only reads that decide a row (second tabs, revenue query, AdMob): honest floor 61 (§9) |
| 11 Minor: create has no parent; folder write access; "Fred's card" provenance; board named "Harmony Games" | subagent | create-then-move is the designed path; Company Ops shared with Frederick as writer (record plan row 56); the hub calls the board "the ops board" and the card names "Fred's \"Lock up social handles and domain?\" card on the UA/BD board", which resolves the card by title (trello:67cf1b506d78ad3c72e02a35) |
| 12 Minor: base "Operations" folder near-miss | subagent | accepted as a natural distractor: the hub names "Company Ops"; the base folder (d_e4181c7a6ba241b7c60d1b) is Marcus's |
