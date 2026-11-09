# Run forensics (node verdicts by hand) - precheck run 6aed9d01a1cb8067d8ac7dee

Status: FILLED (all sections). Hand disposition of the nodes `node_verdicts` refused (binding AMBIGUOUS).

- Run: `06_PreCheck_Trajectory/trajectory.json` (957 events, 237 tool calls, 0 subagents, compaction at event 834)
- Platform SQL: bc72db9c (not stored); nearest local copy `Working_Files/run_forensics/rev1p/01_Universe_Inject.sql`
- Current local SQL: `01_Universe_Inject.sql` (fd51afbf63aa)
- Platform /hardness: score 2, Easy
- Citations: `precheck · event N` (0-based array index)

## 0. Method and evidence limits

- Every one of the 237 calls was read, input and result, from `trajectory.json` at its `result_event`. Spilled
  results (24 calls) were read through the Bash prints the run itself made. Where a spilled file was never printed,
  that is stated: the "Opened" label listing at event 85 and the 51 KB "shares" Slack search at event 563, where only
  the 2 KB preview was seen. A search hit is not a read: `gmail_search_messages` and `gmail_list_messages` return only
  `id`/`threadId`. A record counts as "came back" only when its body or snippet was returned.
- Thinking blocks are redacted (signature only). The run's reasoning comes from its 37 short assistant texts, the
  compaction summary (precheck · event 835) and the final message (precheck · event 955).
- Revision binding. The run executed on platform SQL bc72db9c (74,125 B). The local `rev1p` copy (74,274 B) differs in
  two lines of the close-out notes doc: the run saw "once the sheet is right" and "only go in the totals". Every node
  below is judged against what the run actually saw. The current SQL (fd51afbf63aa) adds records the run never had:
  Slack C07C2866011 ts 1768418331.402719 ("the owner list counts the advisor options in with the stock"), KPMG's
  three-clarification reply, Robert's "Leonard and me on the board" reply, emails on the issues, and Collins's
  contact job "left the board May 2025". Where a rev2 node depends on one of these, that is noted.
- The manifest has no T9 and no C6. The platform /hardness report labels its own traps T1–T9, which are different
  from the manifest IDs. This file uses manifest IDs only.
- Verdict vocabulary is the one in `playbooks/01a_Hardening.md` B3. One run gives provisional verdicts, not counts.
  Failure kinds follow v2 / learnings §45–46: same_container, first_read, on_delegation_path, bulk (a bulk call
  carried the answer), decoy (the decoy was never on the path) and volume.
- Base reachability was checked only through `Task_Authoring/tools/hg.py search` (base data, no overlay).

## 1. Per-node verdicts - mechanisms

| Mechanism | Verdict | Deciding record came back | Decision / write | Failure kind (if it leaked) | Notes |
|---|---|---|---|---|---|
| ADV (A17) | **LANDED** (a fair failure, §4) | The grant sizes never came back in a body. The sizes mail "Re: Follow up items" (thread 1773160163779741845) came back as an ID at precheck · event 496. Its first message was fetched **metadata-only** at precheck · event 502 (snippet "Do we disclose the exercise price in the advisory agreement?"). The contradicting seed total "3,051,881 seed preferred issued at closing" / "Other Seed investors 305,188" came back at precheck · event 562. ES-9/ES-11 grants with no sizes came back at precheck · event 245. | precheck · events 771 (Holders), 783 (Summary 3,155,643), 785 (KPMG tab), 848 (Collins draft "according to Carta you hold 86,470 … Series Seed"), 852, 936 ("about 87%"), 944/950 (KPMG 3,155,643 / 139,993 / 9,295,636). Write-off: precheck · event 835 ("3,051,881 was the initial close only"). Final message: precheck · event 955 ("treated them as already counted in those people's totals"). | — | One root cause behind the K1/K4–K8 wrong values, P1 (55,942 not 159,706), A1 (139,993 not 243,757) and the preferred % (87 vs 90.0). A2's 9,295,636 is right only because the two errors offset: 6,000,000 + 3,155,643 + 139,993 = 6,000,000 + 3,051,879 + 243,757. Count it as one LANDED cause (1A §3). |
| LETTER (A24) | LEAKED | "All termination letters are sent": precheck · event 35 (#winddown page 2). Eight Feb 12 Carta entries: precheck · events 79 (minimal) and 250 (bodies). Six letters: precheck · events 387 (headers) and 397/408 (bodies). | precheck · event 771 (ENG-2459 Vincent and ENG-2463 Oliver set to "Closing and last day"), precheck · events 814 and 828 (drafts), 953 | bulk: one date-window list of Leonard's sent mail (precheck · event 381) and one 8-message batch (precheck · event 394) returned all six letters; the 78-message Carta pull (precheck · events 221–237) returned all eight entries | The join was done, but on two bulk pulls. Vincent's November resignation mail (CAEH8bLx…) never surfaced and was not needed: Carta "as of Nov. 21, 2025" was enough. |
| TOLD (A25) | LEAKED | SEMC Feb 9 DM D04UC0UEN2V/1770664988.379119 at precheck · event 523; its pointer came from the date-window Slack search at precheck · event 414. Robert's Feb 12 reply on the 2023 wire thread came back at precheck · event 314; its ID surfaced at precheck · event 295 (old thread ID 1773963101399472184 among 2026 IDs). | precheck · event 771 (ENG-2440 and ENG-2446 "Already told"), precheck · events 913/919 | bulk: date-window listings (precheck · events 294 and 413) | "Off every channel listing" did not matter, because `after:` searches span DMs. |
| ASOF (A19) | LEAKED (rule applied correctly; totals wrong only through the ADV cascade) | FY25 request plus the "effective on the as-of date counts" clarification, in one thread: precheck · event 61. Effective dates: precheck · event 250. | precheck · events 785, 944, 950 (Jan 30 terminations at the full grant, Dec 31 terminations vested-only, Oct 24 leavers' vested lines counted, ES-2/ES-6 excluded) | same_container and first_read: request and clarification sit in the KPMG thread the prompt names | All 12 non-advisor lines are right. The A1 miss belongs to ADV; A2 passes only because the errors offset. |
| FAM (A7) | LEAKED | Family rule (Leonard's reply in his own #winddown list thread): precheck · event 28. Enes's Jun 30 2023 mail listing all three profiles (A658306E…): precheck · event 540, after one OR-search on the line tokens (precheck · event 524). | precheck · events 771 (ENG-2444/2445 "Covered"), 846 (one note, three holdings), 915/917 | first_read for the rule, plus one targeted search | The shared surname is visible elsewhere: the Slack owner-list copy shows "Patrick Haktan Dişli" (precheck · event 610) and the Carta digest shows "Eren Dişli" (precheck · event 250). fam_over was avoided: the Solsten pair got separate drafts (precheck · events 842/844). |
| BOARD (A11) | **BYPASSED** | The designed resolver (Matthew's May 1 2025 resignation, thread 1830959847543474636) came back only as IDs, at precheck · events 59 and 609, and was never opened. The SPA board list was never printed: precheck · event 361 printed only the last 6,000 of 71,377 chars. The board was inferred from Carta consent recipient lists in the bulk Carta read (precheck · event 250): the Aug 30 2024 consent went to PERSON_4337 + matthew.collins + Leonard + Robert, the Jul 21 2025 consent to PERSON_4337 + Leonard + Robert. That, plus the Feb 12 resignation (precheck · event 63), gave the answer. | precheck · events 783 ("Directors in office: Leonard Hayes, Robert"), 789 (letter), 936 | — (off the true path) | The contacts list (precheck · event 374) still says Collins is "Independent Director". The run overrode it, so the stale record never pulled. In rev2 a Robert reply states the board outright on the Feb 12 thread (first_read). |
| ASK (A9) | LEAKED | Claire's Feb 12 13:41 group-DM question and Leonard's 14:26 reply, which answers only the deletion part: precheck · event 419 (the run's print of the spilled DM/MPIM search at precheck · event 416). Again at precheck · events 562 and 647. | precheck · event 818 (Claire's draft: "on your question about whether you need to do anything … for your equity: you don't"), precheck · event 771 remark | bulk (date-window DM search), and same_container: the group DM that holds the question is the Feb 11 "told" record the run had to read anyway | — |

## 2. Per-node verdicts - traps

Decoys marked "decoy never on path" added no difficulty. Under B3 they are effectively FALSE as hardness, even though
the run got them right.

| Trap | Verdict | Deciding record came back | Decision / write | Failure kind |
|---|---|---|---|---|
| T1 exact_predicate (ADV) | **LANDED** | As ADV: the sizes mail came back metadata-only at precheck · event 502, the contradicting total at precheck · event 562, and the term sheet by name only at precheck · events 71/92 | precheck · events 771, 783, 785, 848, 852, 944, 950 | — |
| T2 stale_summary | LEAKED for the ES lines and Griffin; the advisor part lands under T1 | Two Griffin issues (precheck · event 16) with comments "both funds on one line" (precheck · events 149/151). Griffin split 2,662,255/84,438 at precheck · event 562. ES lines from Carta at precheck · event 250. | precheck · event 771 (two fund rows, ES lines from Carta), 785 | first_read (the Linear project the prompt names), plus bulk (Carta) |
| T3 superseding (term sheet 268,772) | LEAKED (decoy never on path); the value is off only by ADV | The term sheet came back by name only (precheck · events 71/92). The Feb 12 entries came back at precheck · event 250. | precheck · event 783 (55,942 today, not 159,706: ADV cascade) | decoy never on path |
| T4 done_gap | LEAKED | precheck · events 35, 387/397, 79/250 | precheck · events 771, 814, 828 | bulk |
| T5 conclusion_stop | LEAKED | "Carta terminations are done": precheck · event 21. The letters' "separate email from Carta": precheck · event 397. | precheck · events 814–852 (every live note carries its last day) | first_read (both records are in the anchor channel or in mail the run had to read) |
| T6 completion_elsewhere (Segerstråle DM) | LEAKED | precheck · event 523 (pointer at precheck · event 414) | precheck · events 771, 913 | bulk |
| T7 completion_elsewhere (Robert → Nebojsa) | LEAKED | ID at precheck · events 295/382; body at precheck · event 314 | precheck · events 771, 919 | bulk (date-window list; the 2023 thread ID stood out among the 2026 ones) |
| T8 near_miss_mention (Tor Nov 4 DM) | LEAKED (decoy never on path) | D09R59580EM never surfaced. Only the ENG-2448 comment "Nov 4, 2025, DM" came back (precheck · event 169). | precheck · event 771 (TOR "Closing"), 850 | decoy never on path: the default answer is correct |
| T10 superseding board | **BYPASSED** | As BOARD: the resolver came back as IDs only (precheck · events 59/609); Carta consent lists at precheck · event 250 | precheck · event 783 | — |
| T11 authority (Griffin still votes) | LEAKED | Slack 1768415499.678309 ("Restated Certificate requires Preferred approval … M&A / liquidation") at precheck · event 562; Board position thread at precheck · event 63 | precheck · event 783 ("Griffin alone carries the preferred class vote"), 936 (asks for written consent) | bulk (keyword search "equity after:2025-10-01"); the 87% figure is ADV cascade |
| T12 effective_date | LEAKED | precheck · event 61 | precheck · events 785, 944, 950 | same_container / first_read |
| T13 entity_collision | LEAKED | precheck · events 28, 540 | precheck · events 771, 846, 915, 917 | first_read (rule) plus one targeted search |
| T14 scope_alias (two Patricks) | LEAKED | Solsten COO "patrick" investor-info thread at precheck · events 479/482. Enes's list naming Patrick Lewis at precheck · event 540. Separate Linear issues at precheck · event 16. | precheck · events 771 (ENG-2442 own note; ENG-2444 Covered), 844, 846 | first_read (separate issues in the anchor project) |
| T15 distractor (co-founder Frederick) | LEAKED (decoy never on path) | Carta ES-17 notice at precheck · event 250. Contacts show Frederick Stone as "Commercial Lead" (precheck · event 374). | precheck · events 771, 905, 931 | decoy never on path |
| T16 near-duplicate ES-17 letter | LEAKED (decoy never on path) | The letter CAPBs_a6mwZj… came back only as an ID (precheck · event 72). Carta 34,439 / Jan 28 came back at precheck · event 250. | precheck · event 931 | decoy never on path |
| T17 synthesis_omission (Claire) | LEAKED | precheck · event 419 | precheck · event 818 | bulk / same_container |
| T18 superseding notes doc | LEAKED | Later doc: "These replace my earlier outreach notes" (precheck · event 12). Earlier doc at precheck · event 106. | One-by-one notes throughout (precheck · events 842–852) | first_read |
| T19 deck holder count | LEAKED | Deck at precheck · event 102 ("27 holders on the Nov 2024 owner list"; the attribution is in the same text box) | precheck · event 789 (Carta-based count), 795 (corrected to ten angels) | first_read / same_container |
| T20 partial draft sheet | LEAKED | Draft sheet at precheck · event 109 (its own Notes column: "copied from the Nov 2024 list") | precheck · event 113 ("stale"), 769–771 (cleared and rewritten) | same_container |
| T21 Trello "Existing Investor Update" | LEAKED (decoy never on path) | Card name only, in the search at precheck · event 55 (description false); never opened | precheck · event 789 (letter written) | decoy never on path |
| T22 FY24 as-of date | LEAKED (decoy never on path) | The FY24 request (…A7F34357…) came back only as an ID (precheck · event 58) | precheck · event 944 (Dec 31, 2025) | decoy never on path |

Tally: 1 LANDED (T1, the ADV root), 1 BYPASSED (T10), 19 LEAKED, of which 7 were decoys never on the path. No node
is NOT-REACHED or CONFOUNDED. B2 tool notes: two errors, neither changed an outcome. The batch cap at precheck ·
event 216 was recovered at 221; the ECONNRESET at precheck · event 940 was recovered at 942. The KPMG reply-all at
precheck · event 944 dropped the cc's (environment behaviour), and the run resent at precheck · event 950.

## 3. Chains

| Chain | Verdict | Where it went |
|---|---|---|
| C1 (ADV) | LANDED at hop 2 | Hop 1, the owner-list figures, came back at precheck · events 167/155/165/171 (Linear comments) and 610 (Slack copy). Hop 2, the advisor table, was never read: Docs f_6a37… never surfaced, and the mail copy was fetched metadata-only at precheck · event 502. Hop 3, the term sheet's 3,051,879, came back by name only at precheck · events 71/92. The contradiction at precheck · event 562 was explained away. |
| C2 (LETTER) | LEAKED | All hops came back by precheck · event 408. Hop 4 (ES-14's November mail) was not needed. |
| C3 (TOLD) | LEAKED | Hops at precheck · events 28, 523 and 314 |
| C4 (ASOF) | LEAKED for the rule | Hops 1–3 at precheck · events 61 and 250. Hop 4 (advisor grants) fails with C1. |
| C5 (BOARD) | BYPASSED | No hop was read. An alternate path through precheck · event 250 gave the answer. |
| C7 (FAM) | LEAKED | Hop 2 at precheck · event 540. Hop 3 ("all three brothers wired", 0CDD5A07…) never surfaced and was not needed. Hop 4 at precheck · event 16. |
| C8 (ASK) | LEAKED | Hops 1–2 at precheck · events 419/647. Hop 3 (the letter's equity paragraph) at precheck · event 397. |

## 4. ADV fairness: grant-size records opened and not opened

**What the run wrote.** Series Seed was booked at 3,155,643 (precheck · events 783, 785, 944, 950). The four
owner-list lines went in as stock: Collins 86,470, SEMC 81,383, [0127] 31,536 and PERSON_1287 31,536 (precheck ·
event 771, and the drafts at 848/852 say "according to Carta"). ES-8 to ES-11 were left out of today's options
(55,942) and out of KPMG item 2 (139,993). The run suspected the folding: "The Nov 2024 list appears to fold them into
per-person totals" (precheck · event 835) and "I've treated them as already counted in those people's totals"
(precheck · event 955). It still counted those totals as preferred stock.

| Record holding sizes or the tie-out | Persona-visible? | In the run? | Evidence (hg.py, base only) |
|---|---|---|---|
| **"Re: Follow up items"**, thread 1773160163779741845 (Aug 2023, Leonard ↔ Benjamin Clark, cc michelle). It quotes "From the disclosure schedule": [PERSON_NAME_0090] Advisor 30,518 · Matthew Collins Board member 61,038 · PERSON_1287_NAME Advisor 6,104 · PERSON_3941_NAME [PERSON_NAME_0127] Advisor 6,104 · Total 1.7%. The names match the Linear issue titles. | Yes (Leonard's mailbox) | **Came back but was not read.** The thread ID was in the 42 hits of "PERSON_1287_EMAIL OR PERSON_1287_NAME" (precheck · event 496). Its first message CAPBs_a6E95Wnf… was fetched with `format: metadata` at precheck · event 502 (snippet "Do we disclose the exercise price in the advisory agreement?"). The body was never fetched. | `search-many gmail` over `threads/leonard@harmonygames.co_*.json`: "61,038" → 12 hits, all in this thread (/messages/0–5/body); "103,764" → 12 hits, same thread. |
| **Due Diligence Disclosures**, f_6a37227593d0977fdbdd7a (gdocs /docs_documents/262). Advisor table: 30,518 / 61,038 / 6,104 / 6,104, Total 103,764. | Yes. Owner leonard.hayes; visibility "anyone"; shared with Robert, Arthur and three others (gdrive /drive_files/36125). | **Never surfaced** (0 occurrences in the trajectory). Its 8 Drive/Docs queries were "close-out" ×2, "Carta", "outline", "cap table", "SSP-01", "side letter", "Schedule of Purchasers" and "notices" (first 50 of 87). Inside doc 262, "notices", "Carta", "cap table" and "Schedule of Purchasers" all score 0. | `search gdocs "61,038"` → docs 262, 418, 490. `"103,764"` → 262, 418. `"advisory agreements"` → 262, 418 only. A title search on "Due Diligence" → 262 among 3. "advisor", "option", "shares", "Collins", "capitalization" and "Disclosure" all hit doc 262. |
| **Reset Financing Term Sheet**, f_11040fe5d66821bd6951aa (doc 40). Exhibit A: "Series Seed Preferred (all non-founder investors): 3,051,879". | Yes (Leonard-owned) | **Listed by name only**, at precheck · event 71 (fullText "cap table") and event 92 (recent files). Never opened. | `search gdocs "3,051,879"` → doc 40 only. |
| **Slack C07C2866011** 1768416262.426129 and 1768417784.194359 (Jan 14 2026): "3,051,881 seed preferred issued at closing", "Other Seed investors 305,188". | Yes | **Read** at precheck · event 562 (search "equity after:2025-10-01"). The run took the Griffin split 2,662,255/84,438 from this same message (the only source of those figures in the run), then dismissed the seed total as "initial close only" (precheck · event 835). That reading rests on the Jul 2023 "2nd Close" thread (precheck · event 554), but the message says the total was "issued at closing" and lists 305,188 for the other seed investors. 3,155,643 − 3,051,881 = 103,762 ≈ 103,764. | `search slack "3,051,881"` → C07C2866011 2026-01 /727, /728. |
| Board-consent attachments in Leonard's thread 1782034095239486005 ("[SOURCE_ORG_0001]- Option Issuances", Nov 2023–Oct 2024): a Nov 9 2023 draft PDF (147,646 B), the Nov 10 2023 execution copy (46,362 B) and an Oct 18 2024 PDF. I found no Nov 2 attachment. Leonard's Nov 8 message gives an "approval date … Oct 31st". | Thread yes; **attachment bytes no**. Gmail attachment reads return no bytes in HarmonyGames runs (`Evals/references/persona/acl.md`, attachment note). | IDs only, at precheck · events 72, 134, 208, 688, 689. Never opened. | Inside the thread file, "61,038", "30,518", "6,104", "103,764", "ES-9", "ES-11" and "Option Grant" all score 0. The PDFs are root/ blobs. **This carrier is unreachable, so it cannot be the fair path.** |
| Carta digest, thread 1782897835407336831 ("Carta activity for Nov. 17, 2023") | Yes | **Read in full**: in the Carta batch (precheck · events 221–237), decoded at 238, printed at 245. It shows "signed option grant ES-9 … for Husnu Matthew Collins … ES-11 … [PERSON_NAME_0127] … 7 more items". | No sizes in base either (`get gmail threads/leonard@harmonygames.co_1782897835407336831.json`). It proves ES-9/ES-11 exist; it does not size them. |
| Arthur's "Disclosure Schedule For Stock Purc" f_a267353f7f351df0a2dc29 (doc 418); Advisor Agreements f_c2c881ccc407fbdaeaa362 (doc 490, 61,038) and f_e48755daf914ce68a899e0 (doc 570, "Segerstråle", 30,518) | **No.** All are private with shared_with []. Compare the visible shared-drive file f_4480979d3d09c0c50a5ac8, which lists Leonard. | Not seen | gdrive /drive_files/42818, 46591, 50579 |

Other hints the run did read: "the advisory shares in the cap table are allocated but not given to our advisors yet"
(precheck · event 241); "The next one will be the advisorship paperwork" (precheck · event 554); the snippet
"Advisory Contact and follow-up on the angel investment" on Leonard's Sep 7 2023 mail to PERSON_1287 (precheck · event
502).

**Finding: the ADV miss is a FAIR retrieval-and-reasoning failure, not an unreachable one.** Two persona-visible
records hold all four sizes. One of them (the "Follow up items" mail) sat in the run's hands as an ID and a snippet at
precheck · event 502, one `gmail_get_message` away, under the same holder names as the Linear titles. A third record
the run did read and partly used (precheck · event 562) contradicted its Series Seed total by about 103,764, and the
run explained the difference away. Subtracting the table ties exactly: 3,155,643 − 103,764 = 3,051,879, the term
sheet's figure, and leaves the standard 25,432 / 50,865 seed blocks. The platform statement "No grant sizes exist in
the data the evaluator or the Agent could find" is wrong. Its "ES-9/ES-11 can't be settled" holds only for the
board-consent PDFs, which are unreachable.

Residual fairness risks (rubric work, not reachability):

1. P1 (159,706 live options today) counts all 103,764 as vested. I found no persona-visible vesting term for the
   advisor grants: the DD table and the mail table give sizes only, and the agreements are not visible. K1/K4–K8
   (stock) and A1 (outstanding at Dec 31, full grants) do not depend on vesting and are fair.
2. ES-8 and ES-10 are never tied to a holder by number in persona view; the digest names ES-9 and ES-11 only. Grade
   per holder or per total, not per ES ID.
3. In this run's revision nothing stated the folding rule. The rev2 SQL adds it, but the new Slack line (C07C2866011
   ts 1768418331.402719) sits beside the message the run already read at precheck · event 562. The rev2 KPMG
   clarification puts "3,051,879 Series Seed" in the KPMG thread, which the prompt names. Both are same_container /
   first_read placements (learnings §45). They are likely to make ADV easier, not harder.

## 5. Every search query and filter

These are all of the run's search, list and filter calls (`user_email: "me"` dropped). For Gmail, a count is IDs
only: no snippet or body comes back from `gmail_search_messages` or `gmail_list_messages`. Not listed here: the 26
per-issue `linear_list_comments` calls (precheck · events 140, 148–196, 2 comments each) and `linear_get_attachments`
ENG-2456 at precheck · event 142 (0).

| Event | Tool | Query / filter | Results |
|---|---|---|---|
| 3 | linear_list_projects | `{"query": "holder"}` | 1 |
| 4 | gdocs_search_documents | `{"query": "close-out"}` | 1 |
| 7 | slack_search_channels | `{"query": "winddown", "channel_types": "public_channel,private_channel"}` | 1 |
| 14 | linear_list_issues | `{"project": "Holder records", "limit": 100, "includeArchived": true, "maxDescriptionChars": 2000}` | 26 |
| 43 | gdrive_search | `{"query": "close-out"}` | 2 |
| 45 | gdrive_search | `{"fullText": "Carta", "pageSize": 50}` | 12 |
| 46 | gdrive_search | `{"query": "outline"}` | 1 |
| 52 | snowflake_list_tables | `{}` | 40 |
| 54 | trello_search | `{"query": "investor", "modelTypes": "cards,boards", "cards_filter": "all"}` | 5 |
| 56 | gmail_search_messages | `{"query": "KPMG"}` | 14 |
| 57 | gmail_search_messages | `{"query": "subject:\"Board position\""}` | 6 |
| 68 | gdrive_search | `{"fullText": "cap table", "pageSize": 50}` | 10 |
| 69 | gmail_search_messages | `{"query": "carta", "max_results": 100}` | 100 of 439 (more pages, not fetched) |
| 70 | confluence_search | `{"text": "Carta"}` | 0 |
| 85 | gmail_list_messages | `{"label_ids": ["Label_b19fb8d1b3"], "max_results": 500, "include_spam_trash": true}` | spilled (89,130 chars; never read) |
| 91 | gdrive_list_recent_files | `{"limit": 50}` | 50 of 1336 (more pages, not fetched) |
| 97 | gdrive_list_folder | `{"folderId": "d_601064334a0b493022fe83"}` | 3 |
| 99 | gdrive_list_sheets | `{"spreadsheetId": "f_5ecaa967db3adcfa440b09"}` | 1 tab |
| 114 | gmail_search_messages | `{"query": "from:carta.com", "max_results": 500}` | 0 |
| 124 | gmail_search_messages | `{"query": "from:SVC_0077_EMAIL", "max_results": 500}` | 75 |
| 132 | gmail_search_messages | `{"query": "(carta OR \"cap table\" OR ledger OR stakeholder) has:attachment"}` | 51 |
| 133 | slack_search_public_and_private | `{"query": "carta", "content_types": "messages,files", "limit": 50, "response_format": "concise"}` | 50 of 133 (more pages, not fetched) |
| 207 | gmail_search_messages | `{"query": "carta -from:SVC_0077_EMAIL -from:me", "max_results": 500}` | 192 |
| 277 | gdrive_search | `{"fullText": "SSP-01"}` | 0 |
| 278 | gmail_search_messages | `{"query": "\"Series Seed\" OR \"seed preferred\" OR \"certificate SSP\""}` | 100 of 518 (more pages, not fetched) |
| 292 | gmail_search_messages | `{"query": "sunset after:2026/02/01"}` | 16 |
| 294 | gmail_list_messages | `{"query": "after:2026/02/08", "max_results": 200, "include_spam_trash": true}` | 194 |
| 339 | gdrive_search | `{"query": "side letter", "pageSize": 50}` | 3 |
| 340 | gdrive_search | `{"fullText": "Schedule of Purchasers"}` | 4 |
| 342 | gdrive_search | `{"fullText": "notices", "pageSize": 50}` | spilled; 87 files, first 50 printed via Bash 350→351 |
| 371 | contacts_get_contacts | `{"limit": 250}` | spilled; 172 contacts printed via Bash 373→374 |
| 381 | gmail_list_messages | `{"query": "after:2026/02/08 (from:me OR from:robert@harmonygames.co OR from:arthur.blake@harmonygames.co)", "max_results": 200}` | 38 |
| 413 | slack_search_public_and_private | `{"query": "after:2026-02-08 -in:#winddown", "limit": 100, "response_format": "concise", "sort": "timestamp"}` | 100 of 1217 (more pages, not fetched) |
| 416 | slack_search_public_and_private | `{"query": "after:2026-02-08", "channel_types": "im,mpim", "limit": 100, "sort": "timestamp"}` | spilled; 277 msgs, read via Bash 418→419 |
| 446 | gmail_search_messages | `{"query": "(family OR \"my wife\" OR \"my brother\" OR \"my father\" OR \"my sister\" OR \"my son\" OR \"on behalf of\") (shares OR invest OR investment OR wire OR Carta)", "max_results": 50}` | 50 of 589 (more pages, not fetched) |
| 453 | gmail_search_messages | `{"query": "after:2024/05/16 before:2024/05/21 from:me"}` | 2 |
| 455 | gmail_search_messages | `{"query": "from:PERSON_3083_EMAIL OR to:PERSON_3083_EMAIL OR from:PERSON_1287_EMAIL OR to:PERSON_1287_EMAIL OR from:PERSON_3941_EMAIL OR to:PERSON_3941_EMAIL"}` | 100 of 142 (more pages, not fetched) |
| 494 | gmail_search_messages | `{"query": "PERSON_1287_EMAIL OR PERSON_1287_NAME"}` | 42 |
| 495 | slack_search_public_and_private | `{"query": "PERSON_3941_NAME", "limit": 30, "response_format": "concise"}` | 0 |
| 522 | slack_conversations_history | `{"channel_id": "D04UC0UEN2V", "oldest": "1770500000", "limit": "60"}` | 29 |
| 524 | gmail_search_messages | `{"query": "\"PERSON_NAME_11362\" OR \"PERSON_NAME_27652\" OR \"PERSON_NAME_52949\" OR \"PERSON_NAME_4468\""}` | 16 |
| 560 | slack_search_public_and_private | `{"query": "equity after:2025-10-01", "limit": 50, "response_format": "concise"}` | 15 |
| 561 | slack_search_public_and_private | `{"query": "options after:2025-10-01", "limit": 50, "response_format": "concise"}` | 50 of 229 (more pages, not fetched) |
| 563 | slack_search_public_and_private | `{"query": "shares after:2025-10-01", "limit": 50, "response_format": "concise"}` | persisted by harness (51 KB); only the 2 KB preview seen |
| 607 | gmail_search_messages | `{"query": "\"ES-9\" OR \"ES-10\" OR \"ES-11\" OR \"ES-8\" OR (Collins (resign OR board OR options))", "max_results": 30}` | 30 of 270 (more pages, not fetched) |
| 608 | slack_search_public_and_private | `{"query": "Collins", "limit": 30, "response_format": "concise"}` | 29 |
| 646 | slack_search_public_and_private | `{"query": "from:<@EMPLOYEE_0038_SLACK_ID> after:2026-02-08", "channel_types": "im,mpim", "limit": 100, "response_format": "concise"}` | 100 of 193 (more pages, not fetched) |
| 648 | gmail_search_messages | `{"query": "after:2026/02/08 (oliver OR collins OR PERSON_3063_EMAIL OR PERSON_0693_EMAIL OR PERSON_2260_EMAIL OR PERSON_1287_EMAIL OR TOR)"}` | 0 |
| 685 | gmail_search_messages | `{"query": "PERSON_2360_EMAIL -after:2026/02/01", "max_results": 5}` | 5 of 34 (more pages, not fetched) |
| 686 | gmail_search_messages | `{"query": "PERSON_2361_EMAIL -after:2026/02/01", "max_results": 5}` | 5 of 51 (more pages, not fetched) |
| 687 | slack_search_public_and_private | `{"query": "in:#dd-road-to-sub-250mb", "limit": 20}` | 20 of 272 (more pages, not fetched) |
| 703 | slack_conversations_history | `{"channel_id": "C09Q4S613CN", "oldest": "1763856000", "latest": "1763942400", "limit": "30"}` | 4 |
| 724 | gmail_search_messages | `{"query": "after:2025/06/01 (from:PERSON_2260_EMAIL OR from:PERSON_1287_EMAIL OR from:matthew.collins@harmonygames.co OR from:PERSON_0693_EMAIL OR from:PERSON_3063_EMAIL OR from:PERSON_3083_EMAIL OR from:PERSON_0711_EMAIL OR from:PERSON_5137_EMAIL OR from:PERS` | 14 |
| 758 | linear_list_issue_statuses | `{"team": "ENG"}` | 10 |

Patterns:
- **Gmail:** 19 searches and 3 lists. The searches that carried decisions were the date windows (after:2026/02/08 at
  precheck · events 294 and 381), the Carta sender (124) and the name-token ORs (494, 524). No Gmail query used
  "advisor", "disclosure" or a grant size.
- **Slack:** 10 searches, 3 of them date windows (413, 416, 646) and 3 keyword windows since Oct 2025 (560, 561, 563).
- **Drive/Docs:** 9 queries in all. None used advisor/option/Collins terms; Collins and ES-9 were searched only in
  Gmail (607) and Slack (608).
- **Linear:** project "Holder records", includeArchived, limit 100, plus all 26 comment lists.
- **Trello:** 1 search ("investor"). **Confluence:** 1 search ("Carta", 0 hits). **Snowflake:** list_tables only; no
  query.
- **Not used at all:** GCal, Linear search, `gmail_get_attachment`, `slack_read_file`.

## 6. Containers read completely

"Complete" means every message or the whole body came back, not a single message or a tail. Partial reads are listed
separately so you can see where a hidden record would or would not be met.

**Read completely**
- Slack **#winddown C0ADGSZKR3R**, the whole channel (203 messages): precheck · events 13→20 (page 1, 100 msgs via
  Bash), 34 (100) and 37 (3, has_more false). Its threads 1770934638.035469 (5 msgs, precheck · event 27) and
  1770922731.444009 (2, precheck · event 29).
- Slack DM **D04UC0UEN2V** (SEMC) from Feb 7 on: 29 msgs, precheck · event 522, has_more false.
- Slack C09Q4S613CN (#dd-road-to-sub-250mb), Nov 23 2025 window (precheck · event 703, 4 msgs) and thread
  1763857753.026659 (precheck · event 706).
- **Linear project "Holder records"**: all 26 issues (precheck · event 14) and the comments on all 26 (precheck ·
  events 140–196). ENG-2438 relations (144); ENG-2456 attachments (142).
- **Gmail threads read in full**:
  - 1857029474983245439 KPMG (precheck · event 60; again at 942)
  - 1856958794180374704 Board position (62)
  - 1856688113228112603 Sherwood (285→287)
  - 1856675475513544349 Griffin Feb 9 / Sunset (303→320)
  - 1857034369525983506 Sunset intake (304)
  - 1856861681308161749 Fondo (308→320)
  - 1856872398290956689 Sunset templates (310)
  - 1773963101399472184 Robert ↔ Nebojsa, incl. Feb 12 (313)
  - 1847629332615617366 (474), 1847258343060233599 (475)
  - 1836075678772806708 Solsten COO (531), 1833542911997635888 (533)
  - 1773213846196143460 (535)
  - 1770141224265557526 Enes's investor profiles (538)
  - 1847547415984757793 (727)
  - Metadata only: 1807388158915575156 (275)
- **Gmail message sets read in full**:
  - 78 Carta messages: 59 of the 75 Carta-sender notices (the 16 skipped are login alerts and one 409A reminder)
    plus 19 Carta-staff and onboarding mails. Fetched at precheck · events 221–236 (8 batches of ≤10), decoded once
    at 238. 1,099 lines printed at 241/245/250, except lines 400–436, which were seen only as headers at
    243.
  - The Feb 11 termination letters plus 2 SVB mails (8, precheck · event 394 → 396/407).
  - Carta Marcus notice (116). The Oct 2023 investor list mail (510).
- **Docs read in full**: close-out notes f_a37b… (11); outreach notes f_762c… (105); TOR side letter f_6201… (348);
  Vincent's consulting agreement f_4480… (696); update outline deck (101); Task List sheet (103); Holder list (draft)
  (108).
- **Contacts**: all 172 (371→373).

**Read partially (a hidden record here could be missed)**
- Thread 1841635707568607753 ESG law: head 300 lines, plus from Jan 26 on (326/331).
- Angel threads 1768168865446055418, 1772613993289862326 and 1770053656612413311: filtered print (479/481).
- 1772969392648081004 2nd Close: first 120 lines (553).
- 1850625296912603629 Libra intro: first 80 lines (730).
- Series Seed SPA f_95d9…(3): only the last 6,000 of 71,377 chars (361). The board and purchaser body was not seen.
- Claire's consulting agreement PDF: 6,000 of 18,093 chars (676).
- Drive "notices" search: first 50 of 87 (351).
- Recent files: first 50 of 1,336 (92).
- Gmail "carta" (100 of 439), "Series Seed…" (100 of 518), "family…" (50 of 589), ES-9/Collins (30 of 270): IDs only.
- Slack DM/MPIM "after:2026-02-08": 100 of 277, Feb 11 16:36 to Feb 12 20:27 (precheck · events 416→419). This
  page held the 7 Feb 11–12 group-DM (C51ECE5102ED) messages, including Claire's question. Leonard's later replies
  came back in his own DM search at precheck · event 647.
- Slack "after:2026-02-08 -in:#winddown" (100 of 1,217), "options" (50 of 229), Leonard's DMs (100 of 193).
- Slack "shares" (precheck · event 563): 2 KB preview only.
- "Opened" label listing (85): never read.
- Metadata-only fetches: 127 (38 Carta), 386 (14 sent), 501 (8, **including the "Follow up items" advisor-table
  mail**) and 735 (8).

**Never opened, though surfaced as an ID or name**: Matthew's May 1 2025 resignation thread 1830959847543474636 (59,
609); FY24 KPMG request (58); ES-17 letter CAPBs_a6mwZj… (72); Option Issuances thread 1782034095239486005 (72, 134,
208, 688, 689); "Second Close – Tor Capital" 1773160052067710033 (134, 208, 456, 496); owner-list mail CAPBs_a6zM…
(snippet only, 502); term sheet f_1104… (71, 92); "Outline of Disclosure Schedule" (48) and "Harmony Games Inc
Disclosure Schedule" (351), neither of which has sizes; SPA f_9664… with the board list (343); Trello card
68c5a49e… (55).

## 7. Heavy rows that passed, and their cost

| Per-holder decision class (rows) | Correct? | What decided it | Cost |
|---|---|---|---|
| Nothing / Canceled: ES-2, -3, -5, -6, -16, -17 (6 rows, 6 states, 6 comments) | Yes | Carta "Last day to exercise" passed (precheck · event 250); ES-17 at 34,439 / Jan 28 | One bulk pull: 8 batch calls (221–236), 1 decode (238), 3 prints. Covered all 18 ES lines at once. |
| Already told: Griffin II, Side Fund, SEMC, [0127] (4) | Yes | Feb 9 Griffin mail (321), SEMC DM (523), Robert's Feb 12 reply (314) | Two date-window listings (294, 413), then 3 reads |
| Last day, told by Feb 11 letter or group DM: Julia, Claire, Brian, Marcus, Owen, Martin (6) | Yes | Six letters (397/408) and group DM (419); dates from Carta | One sent-mail window (381), one header batch (386), one full batch (394), one DM window (416) |
| Closing and last day: Vincent ES-14, Oliver ES-18 (2) | Yes | Set difference: eight Feb 12 Carta entries minus six letter recipients. Vincent's identity came from the ENG-2459 comment pointer (189) → C09Q4S613CN (703/706). | No extra search for the gap: the two bulk pulls above, plus 2 reads |
| Closing, stockholders not told: Arthur, [4468], Libra CEO, Collins, TOR, PERSON_1287 (6) | Label yes. Holding wrong for Collins and 1287 (ADV). | Absence of a told record in the date windows; last-contact dates from the Linear comments | 26 single comment reads (148–196), no extra calls |
| Covered: Patrick Lewis, [27652] (2) | Yes | Anchor-thread rule (28), plus Enes's Jun 30 2023 list (540) | 1 OR-search (524), 1 thread read (538) |
| Linear states: 14 Todo / 6 Done / 6 Canceled, plus 12 why-comments | Yes | Mechanical, from the sheet | 38 writes, no reads |
| KPMG lines by effective date (12 lines + 2 exclusions) | Yes for each line; total wrong (ADV) | One KPMG thread read (61) plus the Carta bulk | No extra reads |
| Send order / who goes first (Vincent, Feb 21) | Yes | Carta last days | None extra |
| Claire's unanswered equity question | Yes | DM window (419) | No targeted search; it came with the window |
| TOR special notice route | Yes | Side letter (348) | Drive "cap table" / "side letter" searches (68, 339), 1 doc read |
| Sheet to Arthur as well as Robert | Yes | Anchor thread reply (28) | First read |
| Directors / preferred vote | Directors yes; % wrong (ADV) | Board position thread (63), Carta consents (250), Slack seed-docs summary (562) | All already in hand |

All 14 drafts, 26 states, 12 comments and the 3 sends went through on the first attempt, apart from the KPMG
cc-drop resend (writes.json: 67 writes, all ok). 166 of the 237 calls came before the first write (precheck · event
767).

## 8. Why it was easy

The run read the three anchors in full first: all of #winddown with Leonard's list thread, the Linear project with
every issue's comments, and the close-out notes (precheck · events 11–197). That handed it every rule word for word:
what "told" means, the lapse rule, labels, states, the family "Covered" rule and the Arthur sharing correction. Three
cheap sweeps then answered almost every per-holder decision.

1. Fetching all 78 Carta notices in eight batches and decoding them once (precheck · events 221–250) gave every option
   line's grant, vested count, effective date and last day. As a side effect it also gave the board-consent recipient
   lists, which settled the board without the designed resignation mail.
2. Date-window listings of Gmail (precheck · events 294, 381) and of Slack DMs and channels (precheck · events 413,
   416) after Feb 8 returned every "told" or "done" record and the open question: the Feb 9 Griffin mail, the SEMC DM,
   Robert's reply on a 2023 thread (its old thread ID stood out among the 2026 IDs), the six Feb 11 letters and the
   Feb 11–12 group DM with Claire's question.
3. Two OR-searches on the anonymised name tokens (precheck · events 494, 524) found Enes's 2023 investor-profile mail.

Every hidden completion, gap and question sat inside the Feb 8–13 window, so a recency-bounded sweep met them without
any per-holder hunting. The LETTER join and the TOLD lookups cost no more than the bulk reads that were needed anyway.
The decoys (Tor's November DM, the FY24 KPMG date, the ES-17 letter, the term-sheet option count, the Trello card and
the SPA board list) were never opened, so they added nothing.

The one node whose deciding record lived outside that window was ADV. Its sizes sit in 2023 records. That is the node
the run failed, even though it held the sizes mail by ID at precheck · event 502 and read a contradicting seed total at
precheck · event 562. That is a reasoning miss on visible evidence, not a hidden fact. The pattern matches learnings
§45–46 and v2 Part 4: recency sweeps plus bulk notice pulls neutralise "done elsewhere" traps placed in the same week
as the request. A record that changes a number survives only if it is old, out of the date window, and not in a
container the run must read.
