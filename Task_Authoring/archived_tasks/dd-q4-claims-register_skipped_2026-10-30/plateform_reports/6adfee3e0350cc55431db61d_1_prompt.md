## PROMPT EVALUATION REPORT

### Task: Julia checks the 13-claim "Q4 Product Claims" draft against what is live (live-claim standard, external wording card, Leonard's scope note), fills the Register tab, posts counts in Leonard's mpim thread, corrects the Confluence claims page and files a follow-up ticket linked to ENG-2375
### Assigned Persona: Julia Lawson - Product Manager
### Assigned Business Function: Product
### Assigned Competency: Product Management
### Assigned Task Skill: Retrieval
### Assigned Horizon: normal (recorded as "Task Type: normal"; Normal Horizon, 50–100 calls, not scored at /prompt)

## Scope

- Review: chat `/prompt` review for attempt 6adfee3e0350cc55431db61d; review date 2026-10-29; mode AUDIT.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe manifest: `Evals/references/universes/synthcut/universe_manifest.json` (sha256 da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a), base folder `Universe_SynthCut/`.
- Inputs reviewed: `04_Prompt.txt` sha256 76500140c70a687cbacdbe517ba111ec9129c91a99dcb72e9f00ec8b0085b4e0 (input revision 8; the text in the command matches it word for word, with plain hyphens for the em dashes); `00_Task_Assigned_Inputs.md` sha256 9a0ae27ffee6c81502281edec8b5f3a93410bf1a705fde5b47d6254da28eee71; `01_Universe_Inject.sql` sha256 bc3abbdfb1d89e4c46693bd9648c267d5e8e3d6ebba3dd256d80b466e8b5e83e (revision 7); `02_Universe_Date.txt` sha256 189e2ac63a6fea6f90c0c9ab3dbfb06e0fc8ed7269f82b0d75af728e3b21da5c. No error/async config, dynamic context or reference files were supplied, and the prompt names no attachment.
- Eval version: task-quality-v1 / prompt-source-checks-v2. Eval release SHA-256: 6478616fae461adfff81f45b2a523017b7a8e042bf02b6afc8c113d659886b8f.
- Reviewed prompt SHA-256: 76500140c70a687cbacdbe517ba111ec9129c91a99dcb72e9f00ec8b0085b4e0
- Review context SHA-256: 38c50b2ae3d847395b34265ba23ee696625c67dffb59d55ed3eb4948a25d26b4
- Prompt record SHA-256: 37c4ad2011b322abc7ab56dba3a0afcffdca5fb2d63b72fb168ad59ec1466654
- authority_contract: prompt-incorporation-v1; evidence_contract: stage-evidence-v1.

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`; reviewed 2026-10-29T12:52:00Z, `injection-static-v2`)
- Reviewed SQL sha256: bc3abbdfb1d89e4c46693bd9648c267d5e8e3d6ebba3dd256d80b466e8b5e83e  Eval 0 verdict: PASS
- Eval 0 findings on records this prompt depends on: advisory V2 (Season Pass Slack vs Snowflake, which injected records build on) is a record claim 6 depends on and is scored here under Cross-Service Coherence. V1 (DES-313 creator not a team_DES member), V3 (reply thread_parent_id holds a ts), V4 (comment-ID gaps) and V5 (April card wording) change no graded value and stay advisories.

## Input / authority issues

- All five assignment fields are in the saved `00_Task_Assigned_Inputs.md`; "Task Type: normal" is the horizon field (Normal Horizon). "Difficulty Mode: easy" is not one of the five fields and is not graded here.
- A draft check record for this same prompt hash was on disk from an earlier, unfinished run. It was used only as a lead. Every fact below was re-read from the SQL, the Confluence/Slack/Gmail/gcal/gdocs exports and Snowflake for this report.
- Evidence limits: `hg_search.py get` on Snowflake timed out (index validation of the 2.2 GB export did not finish in 10 minutes), so Snowflake tables were read with a byte-offset streaming reader over the same export (table offsets indexed in one pass; only tables 4, 9, 12, 18, 35 and 36 were decoded). The Docs PDFs/XLSX were not re-extracted this run; the Eval's Local Overrides and scoring.json were applied as written.

## Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's ask and the claim set | Slack mpim C1CB3D58E38B root 2025-09-30 16:10Z (SQL l.12); Doc "Q4 Product Claims" `f_5a1b2c3d4e5f60718293a4` (13 items, l.83); stale "September list" (9 items) | Slack search / Drive search | `slack_*` history; `gdrive_search`, `gdocs_get_document_text` | Julia is one of 3 mpim members; Julia owns both docs | 13 claims from the current draft |
| Apply the live-claim standard | Trello card `68daad00…0d10` "Q4 live-claim standard (agreed at the Q4 review)"; gcal `evt_5c1a7e93…` "Proposed live-claim standard" | Leonard's message → Trello / Julia's calendar | `trello_*` reads; `gcal_*` | Trello unscoped; event on Julia's calendar | Live = 100% enabled + config row or completed run/transaction in the warehouse; positive subset = Testing; zero enablement + no run = Not live |
| Check each claim against what's live | Snowflake LIVE_EVENT_PERFORMANCE (529 rows), IAP_TRANSACTIONS (886), AD_REVENUE, LEVEL_PERFORMANCE; Linear comments on ENG-2369…2374, ENG-1874, ENG-1385, ENG-2136, ENG-2323, DES-313; PR #1755/#1838 comments; Confluence Live-Ops calendar, GDD | Linear/GitHub/Snowflake/Confluence | `snowflake_execute_query`, `linear_list_comments`, `github_*`, `confluence_get_page` | All unscoped | See the claim table below |
| Apply the external wording rules | Trello `68d67230…0d11` "External wording - product claims" (2025-09-26); decoys: Confluence `page_external_messaging_guide` (Robert, 2025-09-08), Trello "Engineering release wording" | Trello / Confluence | reads | Unscoped | LIVE "live/available"; TESTING "in testing", never live/available/launched; NOT_LIVE removed; exact values; owner on every kept claim |
| Apply the scope note | Gmail "Q4 pack - Domino Delights only" 2025-09-30 14:05Z (l.27) | Julia's inbox | `gmail_*` | Julia's INBOX copy | Claim 11 (live-ops engine) out of the pack; launch date = GDD 11 April 2025 (US soft launch) and 6 May 2025 (worldwide) |
| Conflict column | Register header `conflict`; Confluence `page_q4_claims_conflict_format` | Sheet read | `gsheets_values_get` | Julia owns the workbook | Both sources + which governs, per conflicting claim |
| Fill the register | Workbook `f_6b2c3d4e5f60718293a4b5`, tab "Register" (12-column header, empty) vs "Old register" (C01–C09 filled, 5 columns) | Drive search | `gsheets_values_update` / `gsheets_values_append` | Owned by Julia | 13 rows × 12 columns in Register |
| Post corrected counts | mpim thread ts 1759248600.000100 | Slack | `slack_send_message` with `thread_ts` | Member | Counts by status and by decision (see UGT) |
| Correct the Confluence claims page | `page_q4_product_claims` "All 13 product claims are live." | Confluence search | `confluence_update_page` | Unscoped | Page states statuses and lists removed claims |
| Follow-up ticket linked to the claims review ticket | ENG-2375 "Q4 product claims review" (In Progress, assignee Julia) | Linear search | `linear_create_issue` (`parentId` or `links`) | Unscoped; writes not ACL-governed | New issue with evidence (contents disputed, see UGT) |
| Deadline | gcal "[SOURCE_ORG_0001] Board Meeting" 2025-10-14 16:00Z (Leonard, Robert, Arthur, Frederick) | Context | — | — | Future date; no read required |

### Claim-by-claim facts (verified this run)

| # | Draft claim | Evidence | Status under the standard | Conflict to record |
|---|---|---|---|---|
| 1 | Weekly Quests run every week | ENG-2369 comment "Mondays 00:00 UTC; last completed run EVT-0513 (2025-09-28)"; Snowflake EVT-0513 2025-09-22→09-28 completed, weekly runs through September | LIVE | Live-Ops calendar v3: "Failed Nov 2024 (ads-quest misdeploy)"; warehouse governs |
| 2 | Weekly Leaderboards are automated | ENG-1874 comment; EVT-0515 2025-09-22→09-28 completed | LIVE | — |
| 3 | Win & Collect runs every day | ENG-1385 "Mon/Wed/Fri 00:00; not daily"; warehouse windows EVT-0512 (Mon–Tue), EVT-0518 (Wed–Thu), EVT-0522 (Fri–Sun); calendar "three staggered windows (Mon-Tue, Wed-Thu, Fri-Sun)" | LIVE | Daily vs not daily (fork F1) |
| 4 | River Rush is live | ENG-2373; EVT-0531 2025-09-29 completed | LIVE | — |
| 5 | Axe Arena and Streak Fever are live | ENG-2374; EVT-0525/0526 2025-09-27→28 completed | LIVE | Live-Ops Event Engine page: weekend outage "nothing in the record yet marks it restored" |
| 6 | Season Pass is live on DD | PR #1755 / ENG-2136 comments: default false, no SKU, no run; Leonard's 18:00Z correction; no DD Season Pass row in LIVE_EVENT_PERFORMANCE or IAP_TRANSACTIONS | NOT_LIVE → drop | Leonard 15:30Z "headline live feature"; base Slack 2025-04/06/07 (see Coherence) |
| 7 | Collectibles ship in October | Brian 17:00Z "not in the Q4 build plan"; Leonard "no build slot this quarter" | NOT_LIVE → drop | — |
| 8 | Rewarded ads and remove-ads IAP are live | ENG-2372; AD_REVENUE `rewarded_continue` rows in Sep 2025; dd_remove_ads 54 sales (last 2025-08-18) | LIVE | — |
| 9 | Five coin bundles and a starter pack | ENG-2371 "Four coin bundles, not five"; IAP SKUs dd_coins_small/medium/large/mega + dd_starter_pack | LIVE, value 4 | April Trello card "Five coin bundles…"; ENG-2371 governs |
| 10 | Hero Offers rotate every 48 hours | ENG-2323 / PR #1838: offer_rotation_v2 at a 10% cohort | TESTING → qualify "in testing" | Messaging guide "Use launched for features that are in testing" vs wording card; card governs (newer, product-claims scope) |
| 11 | The live-ops event engine is live | ENG-2370 "internal admin surface only, no player-facing surface"; scope note | Out of pack (status disputed, fork F3) | — |
| 12 | 5,000 handcrafted levels | DES-313 "4,755 active; 245 planned"; manifest Total 4755/245; LEVEL_PERFORMANCE "domino_delights 1-4755"; GDD "~4,800" | LIVE, value 4,755 | GDD approximation vs manifest |
| 13 | Launched on 14 April 2025 | Scope note; GDD v4 "US go-live on 11 April 2025, worldwide on 6 May 2025"; Q4 Product Narrative "April 14" | LIVE, dates corrected | Narrative page vs GDD; scope note governs |

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Julia Lawson is in the roster (julia.lawson@harmonygames.co, Product Manager, Product). Leonard addresses her directly, she owns the draft, the register and ENG-2375, and checking product claims before a board pack is PM work. She is a member of every Slack channel the task needs.

**Assigned Competency:** PASS (5)
- A product claims register and the public claims page are product-management outputs (what ships, how it is described). Mapped to Product Management.

**Assigned Task Skill:** PASS (5)
- Retrieval is the spine: the draft, the standard, the wording card, the scope note, the per-claim Linear/GitHub facts, the warehouse runs and SKUs, and the GDD dates all have to be found and matched to 13 claims.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y — PASS
- Dynamic Change: Leonard's 15:30Z "Season Pass is our headline live feature" is corrected by his 18:00Z thread reply; the 9-item September list is superseded by the 13-item draft; the "April 14" narrative is superseded by the scope note.
- Multi-Source: Docs, Sheets, Slack, Gmail, gcal/Trello, Linear, GitHub, Confluence and Snowflake, with decoys (messaging guide, engineering release wording, April bundle card, Old register).
- Data seeding: PASS. Operating rules live in seeded records; the prompt is about 200 words.

**Naturalness:** FAIL (scored under Contrived, 2.7).

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS (no first/then/finally sequence) |
| Bolt-On | PASS (every ask serves the claims check) |
| Pre-Solving | PASS (no claim outcome named; "still reads as if every claim is live" names the symptom) |
| Tool Mention | PASS ("Confluence", "ticket", "thread", "tab" are natural product words) |

**Diversity:** Sheet write, Slack thread reply, Confluence page update and a new Linear issue, with per-claim branching. Not an "investigate + post one message" task.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: Several required outcomes have two defensible answers with no resolving prompt sentence or persona-visible record: keep vs qualify for corrected LIVE claims (including Win &amp; Collect), which claims go on the follow-up ticket, the live-ops engine's and launch-date line's status, what the Confluence list covers, what counts as a conflict, and whose name goes in the owner column. Each changes the register, the posted counts, the page or the ticket contents.

Alternative selection: Tested every set, number, source-priority and event question for each required output, including the blind P1 pass; B, C, D, E, F, G, H and I are the alternatives no cited record kills. Other forks (register tab, wording-rule source, launch dates, Season Pass, offer calendar, levels, freeze edge) are settled by quoted records and listed in the report.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Win &amp; Collect is QUALIFY (starts Mon/Wed/Fri, not daily, per ENG-1385); the follow-up ticket carries only the claims dropped as unsupported (Season Pass, Collectibles); the live-ops engine row is LIVE / DROP (out of scope). | Statuses LIVE 10 / TESTING 1 / NOT\_LIVE 2; decisions KEEP 5 / QUALIFY 5 / DROP 3; follow-up ticket lists Season Pass and Collectibles. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Register C03 = LIVE / QUALIFY 'Mon/Wed/Fri'; thread counts KEEP 5 / QUALIFY 5 / DROP 3; ticket lists two claims. | L\_1385 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 146-146): "Win &amp; Collect schedule slots: Mon/Wed/Fri 00:00; not daily."; T\_WORD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "NOT\_LIVE items are removed, not caveated."; G\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 29-29): "internal tooling claims go in the engineering appendix, even when they are live." |
| B | Win &amp; Collect is KEEP: the live windows Mon-Tue, Wed-Thu and Fri-Sun mean it is running every day, which is what the warehouse runs show (EVT-0512 Mon 09-22 to 09-23, EVT-0518 Wed 09-24 to 09-25, EVT-0522 Fri 09-26 to Sun 09-28) and the Live-Ops calendar states. | Statuses LIVE 10 / TESTING 1 / NOT\_LIVE 2; decisions KEEP 6 / QUALIFY 4 / DROP 3. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Register C03 = LIVE / KEEP; thread counts KEEP 6 / QUALIFY 4 / DROP 3. | CF\_CAL\_WC (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/27/body): "Recurring weekly, in three staggered windows (Mon-Tue, Wed-Thu, Fri-Sun) that all players share"; D\_DRAFT3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 94-94): "3. Win &amp; Collect runs every day." |
| C | 'Anything we can't support' covers every claim whose draft wording the evidence does not support as written, so the follow-up ticket also lists the qualified claims (Win &amp; Collect cadence, five vs four coin bundles, Hero Offers in testing, 5,000 vs 4,755 levels, the launch date). | Same register and counts as A; follow-up ticket lists Season Pass, Collectibles and the qualified claims with their evidence. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Ticket lists seven claims instead of two. | P (Evals/task\_inputs/04\_Prompt.txt): "Anything we can't support goes on a follow-up ticket linked to the claims review ticket, with the evidence."; D\_DRAFT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 90-90): "Status: all 13 items verified live with the owning teams as of 29 September." |
| D | The live-ops engine cannot be Live under the standard (no player enablement: 'internal admin surface only, no player-facing surface'), so its status is NOT\_LIVE or out of scope rather than LIVE, which changes the status counts. | Statuses LIVE 9 / TESTING 1 / NOT\_LIVE 3 (or LIVE 9 plus one out-of-scope row); decisions unchanged. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Register C11 status differs; thread status counts differ. | T\_STD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 178-178): "the feature is enabled for 100% of production players"; L\_2370 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 153-153): "internal admin surface only, no player-facing surface." |
| E | A claim whose status is LIVE stays KEEP even when its number, date or cadence is corrected: the wording rules treat the exact value as a register wording requirement ('Numeric and date claims state the exact value in the register'), and only TESTING items take a qualifier ('must say in testing'). Coin bundles (four, not five), levels (4,755), the launch date and Win &amp; Collect are KEEP with corrected text; Hero Offers is the only QUALIFY. | Statuses LIVE 10 / TESTING 1 / NOT\_LIVE 2; decisions KEEP 9 / QUALIFY 1 / DROP 3; follow-up ticket lists Season Pass and Collectibles. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Register C03, C09, C12 and C13 = LIVE / KEEP with corrected claim text; thread counts KEEP 9 / QUALIFY 1 / DROP 3. | T\_WORD2 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "Numeric and date claims state the exact value in the register."; T\_WORD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "TESTING items must say in testing and must not use live, available or launched."; L\_2371 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 152-152): "Four coin bundles, not five." |
| F | 'list what came out' on the Confluence page covers both the dropped claims and the wording that was replaced (five to four bundles, 5,000 to 4,755 levels, every day, 14 April), not only the dropped claims. | Same register and counts as A. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Confluence page lists dropped claims plus replaced wording, instead of only Season Pass, Collectibles and the live-ops engine. | P (Evals/task\_inputs/04\_Prompt.txt): "bring it in line and list what came out"; C\_CLAIMS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 191-191): "All 13 product claims are live. See the Q4 claims draft for the full list." |
| G | Every disagreement among a claim's sources is a conflict entry, including approximate figures such as the GDD's ~4,800 levels against the 4,755 manifest, so more conflict cells are filled than in Reading A. | Same register decisions and counts as A. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Conflict column filled on additional rows (C12 GDD ~4,800 vs 4,755 and similar). | P (Evals/task\_inputs/04\_Prompt.txt): "Where a claim's sources disagree, put both in the conflict column and say which one governs"; CF\_GDD2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/15/body): "~4,800 levels across 160 chapters" |
| H | The owner column holds Julia, the claim owner named on the draft, on every row, instead of each feature's engineering owner. | Same register decisions and counts as A. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Register owner column = Julia on all rows vs per-feature owners (Brian, Calvin Price, Samuel Turner or ticket assignees). | D\_OWNER (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "Owner: Julia Lawson"; T\_WORD3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "Every retained claim names an owner." |
| I | The launch-date line has no feature status under the standard (it is a date, not a feature), so it is counted outside LIVE and the status counts drop to LIVE 9. | Statuses LIVE 9 / TESTING 1 / NOT\_LIVE 2 plus one unstatused row; decisions unchanged. | Fill 13 rows of the Register tab (f\_6b2c3d4e5f60718293a4b5); reply in Leonard's mpim thread 1759248600.000100; update Confluence page\_q4\_product\_claims; create one Linear issue linked to ENG-2375. | Register tab; mpim C1CB3D58E38B thread 1759248600.000100; Confluence page\_q4\_product\_claims; new Linear issue linked to ENG-2375. | Register C13 status and the posted status counts differ. | D\_DRAFT13 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 104-104): "13. Domino Delights launched on 14 April 2025."; T\_STD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 178-178): "the feature is enabled for 100% of production players" |

Explicit option inventory: The prompt's explicit option list is the per-claim decision 'keep, qualify or drop'.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "including whether we keep, qualify or drop it"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| keep | RETAINED | A, B, E | Keep is the C03 decision in Reading B and the decision for unqualified LIVE claims in the readings listed. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep" |
| qualify | RETAINED | A, B, E | Qualify is the C03 decision in Reading A and applies to the other corrected claims in both. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "qualify" |
| drop | RETAINED | A, C, D | Drop applies to Season Pass, Collectibles and the live-ops engine in all readings. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "drop" |

Compared alternative: B
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. ENG-1385 says the slots start Mon/Wed/Fri and are 'not daily'; the warehouse windows and the Live-Ops calendar show a Win &amp; Collect window open every day. The live-claim standard settles Live status only (both readings are LIVE), not cadence wording, and no record says which source governs a cadence claim. The decision for C03 and the posted decision counts differ.
Resolution evidence: L\_1385 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 146-146): "Win &amp; Collect schedule slots: Mon/Wed/Fri 00:00; not daily."; CF\_CAL\_WC (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/27/body): "Recurring weekly, in three staggered windows (Mon-Tue, Wed-Thu, Fri-Sun) that all players share"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | QUALIFY vs KEEP for C03; KEEP 5/QUALIFY 5 vs KEEP 6/QUALIFY 4. |
| writes | SAME | Same four writes. |
| destinations | SAME | Same four destinations. |
| contents | DIFFERENT | Register C03 decision and qualifier, thread counts and Confluence page differ. |

Resolution relevance challenge: Both cited records describe the same live Win &amp; Collect schedule; the prompt's 'against what's actually live' points to the runs, which cover every day, while the engineer's comment says 'not daily'. Neither the prompt nor the standard ranks them.
Delegation challenge: NOT_CLAIMED. No source delegates the cadence call.
Challenge evidence: T\_STD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 178-178): "A claim may be marked Live only if, at the freeze, the feature is enabled for 100% of production players"

Compared alternative: C
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Nothing defines 'can't support'. Qualified claims are by definition not supported as written, and the draft claims all 13 were verified live; a careful reader can put them on the follow-up ticket. Leonard's thread repeats the same phrase without defining it.
Resolution evidence: S\_ASK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 12-12): "put anything we can''t support on the claims review ticket."; P (Evals/task\_inputs/04\_Prompt.txt): "Anything we can't support goes on a follow-up ticket linked to the claims review ticket, with the evidence."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Register decisions and counts are the same. |
| writes | SAME | One follow-up ticket in both. |
| destinations | SAME | Same ticket destination. |
| contents | DIFFERENT | Ticket lists 2 claims vs 7 claims and their evidence. |

Resolution relevance challenge: The wording rules say NOT\_LIVE items are removed, but say nothing about what goes on the follow-up ticket; the cited thread uses the same undefined phrase.
Delegation challenge: NOT_CLAIMED. No source authorizes either ticket set.
Challenge evidence: T\_WORD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "NOT\_LIVE items are removed, not caveated."

Compared alternative: D
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The standard's Live test needs 100% player enablement and its Not-live test needs no completed production run; an internal tool with no player surface fits neither, and the scope note's 'even when they are live' does not status this claim. The status counts posted to Leonard differ.
Resolution evidence: T\_STD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 178-178): "the feature is enabled for 100% of production players"; L\_2370 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 153-153): "internal admin surface only, no player-facing surface."; G\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 29-29): "internal tooling claims go in the engineering appendix, even when they are live."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C11 status LIVE vs NOT\_LIVE / out of scope. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register C11 status and thread status counts differ. |

Resolution relevance challenge: The scope note settles that C11 leaves the pack, not which status bucket it is counted in.
Delegation challenge: NOT_CLAIMED. No source delegates the status call.
Challenge evidence: G\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 29-29): "internal tooling claims go in the engineering appendix, even when they are live."

Compared alternative: E
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Nothing defines keep, qualify or drop. Reading A treats a corrected value as a qualification; Reading E keeps every LIVE claim and corrects its text, because the wording card makes exact values a register requirement and reserves the caveat for TESTING items. The live-claim standard sets status only. Four register decisions and the posted decision counts differ (KEEP 5/QUALIFY 5 vs KEEP 9/QUALIFY 1).
Resolution evidence: T\_WORD2 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "Numeric and date claims state the exact value in the register."; D\_DRAFT9 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 100-100): "9. Five coin bundles and a starter pack are live in the shop."; L\_2371 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 152-152): "Four coin bundles, not five."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C03, C09, C12, C13 QUALIFY vs KEEP; decision counts differ. |
| writes | SAME | Same four writes. |
| destinations | SAME | Same four destinations. |
| contents | DIFFERENT | Register decision and qualifier cells and thread counts differ. |

Resolution relevance challenge: The only records about wording are the external wording card and Leonard's messages; neither maps a corrected LIVE claim to keep or qualify, and the Old register only ever used LIVE/KEEP.
Delegation challenge: NOT_CLAIMED. No source delegates the keep/qualify call.
Challenge evidence: T\_WORD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "LIVE items may say live or available."

Compared alternative: F
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Nothing says whether 'what came out' means removed claims only or also removed wording; the page content differs.
Resolution evidence: P (Evals/task\_inputs/04\_Prompt.txt): "bring it in line and list what came out"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Register decisions and statuses are the same as Reading A. |
| writes | SAME | Same four writes. |
| destinations | SAME | Same four destinations. |
| contents | DIFFERENT | Confluence page contents differ (2-3 removed claims vs those plus four replaced phrasings). |

Resolution relevance challenge: The page only says 'All 13 product claims are live'; it does not define what the corrected page must list.
Delegation challenge: NOT_CLAIMED. No source delegates this choice.
Challenge evidence: C\_CLAIMS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 191-191): "All 13 product claims are live. See the Q4 claims draft for the full list."

Compared alternative: G
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. 'Disagree' is not defined; whether an approximate GDD figure or an older planning status counts as a disagreement changes several conflict cells.
Resolution evidence: P (Evals/task\_inputs/04\_Prompt.txt): "Where a claim's sources disagree, put both in the conflict column and say which one governs"; CF\_GDD2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/15/body): "~4,800 levels across 160 chapters"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Register decisions and statuses are the same as Reading A. |
| writes | SAME | Same four writes. |
| destinations | SAME | Same four destinations. |
| contents | DIFFERENT | Register conflict cells differ on several rows. |

Resolution relevance challenge: The conflict-format page repeats the rule without saying what counts as a disagreement.
Delegation challenge: NOT_CLAIMED. No source delegates this choice.
Challenge evidence: C\_CONFLICT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 190-190): "If a claim''s sources disagree, write both sources in the conflict column and say which one governs. Do not silently pick one."

Compared alternative: H
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. No record names an owner per claim; the draft's owner is Julia and the evidence comments have different authors and assignees.
Resolution evidence: T\_WORD3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "Every retained claim names an owner."; D\_OWNER (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "Owner: Julia Lawson"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Register decisions and statuses are the same as Reading A. |
| writes | SAME | Same four writes. |
| destinations | SAME | Same four destinations. |
| contents | DIFFERENT | Owner cells differ on every row. |

Resolution relevance challenge: The wording card requires an owner but does not say whose name it is.
Delegation challenge: NOT_CLAIMED. No source delegates this choice.
Challenge evidence: SH\_REG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "'Register', 0, 14, 12, '\[\["claim\_id","claim","feature","scope","status","decision","qualifier","evidence","evidence\_date","conflict","owner","action"\]\]'"

Compared alternative: I
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The standard defines status for features; nothing says how a launch-date line is statused.
Resolution evidence: T\_STD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 178-178): "the feature is enabled for 100% of production players"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C13 status and the thread's status counts differ. |
| writes | SAME | Same four writes. |
| destinations | SAME | Same four destinations. |
| contents | DIFFERENT | C13 status and the thread's status counts differ. |

Resolution relevance challenge: The scope note fixes the dates to use, not the status bucket.
Delegation challenge: NOT_CLAIMED. No source delegates this choice.
Challenge evidence: G\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 29-29): "This pack covers player-facing Domino Delights claims only; internal tooling claims go in the engineering appendix, even when they are live. For any launch-date line use the soft-launch and worldwide dates in the current GDD, not the 14 April date."

Strongest-alternative challenge (B): B rests on the warehouse runs and the Live-Ops calendar, the sources closest to 'what's actually live', and flips a decision count; it is not a strawman.
Challenge evidence: CF\_CAL\_WC (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/27/body): "Recurring weekly, in three staggered windows (Mon-Tue, Wed-Thu, Fri-Sun) that all players share"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

Settled forks (not failing): register tab — only "Register" has the `conflict` column the prompt names; wording source — the 2025-09-26 product-claims card is newer and narrower than the 2025-09-08 general messaging guide; launch date — scope note names the GDD; Season Pass — Leonard's 18:00Z correction and ENG-2136; Brian's "offer calendar" — Leonard's scope note "fixes which claims are in" and the draft "is the set"; levels — DES-313 and the manifest agree on 4,755; register row count — "one row per claim" on the 13-item draft (Register `row_count` 14 = header + 13).

**Feasibility:** PASS (5)
- Every write has a cataloged path: `gsheets_values_update`, `slack_send_message` (`thread_ts`), `confluence_update_page`, `linear_create_issue` (`parentId`/`links`). All facts exist in persona-visible or unscoped records. Status counts and decision counts are derivable from the register (dimension fields exist). Snowflake and Confluence are live and unscoped (service-availability-v1).

**Persona ACL Reachability:** PASS (5)
- Slack mpim (member), Julia's Gmail INBOX copy of the scope note, the gcal event on Julia's calendar, and Julia-owned Docs/Sheets. Everything else is unscoped. The private Drive GDDs (`f_0899f5…`, `f_c4187f…`) are not visible to Julia, but the Confluence GDD (unscoped) carries the dates, so nothing required is out of reach.

**Explicit Tool Mention:** PASS (5)

**Clarity & Specificity:** NON-FAIL (3)
- Writes are the same under every reading (one register fill, one thread reply, one page update, one new ticket), so the forks are scored under UGT, not Action Decision Ambiguity. Minor open points: whether "list what came out" goes on the page or in the reply, and the link mechanism (sub-issue vs link). The standard needs "100% of production players" but no record gives an enablement figure for the event claims; an agent has to read "no flag/cohort" as 100%.

**Contrived / Unnatural:** FAIL (2)
- Hidden destination the persona would know: "in the tab we already use". The workbook has "Register" (header only, nothing in it) and "Old register" (the one with data, C01–C09). Julia would say "the Register tab"; no record names it (Leonard's email repeats "the tab you already use"), and "already use" points at the filled Old register. Calibration #42/#47/#44.
- Spec-sheet register (two triggers): enumerated deliverable contents ("one row per claim, every column, including whether we keep, qualify or drop it"; "broken out by status and by decision") plus a format rule ("put both in the conflict column and say which one governs; don't pick one quietly", which restates the seeded Confluence conflict-format page and Leonard's message).

**Alignment with Today's Date:** PASS (5)
- "this morning" in Leonard's 16:10Z message resolves to the 14:05Z scope note; the 14 October board meeting exists in gcal and is in the future relative to the clock. No seeded record is after 2025-10-01 07:00Z.

**Originality / Sample Similarity:** N/A — no comparison samples supplied.

**Truthfulness:** PASS (5)
- Every premise checked (record PR1–PR11): Leonard's ask, Julia's draft, the standard "agreed at the Q4 review" (Trello card), the wording rules (Leonard: "the external wording rules product signed off"), the scope note, the conflict column, the register/tab, the thread, the Confluence page's "All 13 product claims are live.", ENG-2375 and the board date.

**Tool Use & Cross-service:** PASS (5)
- Graded facts per service: Snowflake (completed runs, SKUs, 4,755 levels), Linear (four coin bundles, Hero Offers 10% cohort, Win & Collect slots), Gmail (engine out of scope, GDD dates), Confluence (GDD dates), Slack (Season Pass and Collectibles corrections), Sheets/Confluence/Slack/Linear writes.

**Investigation + Action:** PASS (5)

**Coherence (Bolt-on):** PASS (5)

**Business Function:** PASS (5)

---

### Phase 3: Universe Feasibility

**Data Existence:**
- Entities verified: 13 of 13 claims plus every named source; all retrievable through cataloged tools.

**Cross-Service Coherence:** FAIL (2)
- Cross-service referential (Season Pass), task-dependent, injection builds on it: base Slack in channels Julia is in says the DD Season Pass existed in production and sold — #god-bugs 2025-04-02 "testing them out in both dev and prod servers. Season pass and daily gift was okay", 2025-04-03 "the current season pass event was created on April 1st", Leonard 2025-06-09 "if I have the season pass let's make sure I don't see season pass offer in rotation", Brian #zombie-design 2025-07-23 "in DD, since the Season Pass gives an extra move, users often choose to purchase the pass from this screen". Snowflake IAP_TRANSACTIONS (2024-02-23 to 2025-09-29, 885 DD rows) has no Season Pass SKU and its comment says "absence here means no sales"; LIVE_EVENT_PERFORMANCE has no DD Season Pass run (only ZM3D EVT-0527). The injected PR #1755 comment ("no SKU was configured in the store catalog") and ENG-2136 comment ("no store SKU") side with Snowflake and contradict Brian's own July message. Claim 6 and its conflict column read exactly these records.
- Injected value conflict: ENG-2136 says "The out-of-moves screen shows the $0.99 starter pack instead"; IAP_TRANSACTIONS prices dd_starter_pack at $2.99 on all 95 sales (2025-02-09 to 2025-09-06), and no $0.99 starter SKU exists.
- Known base-data issues (not scored): the Live-Ops calendar says Streak Fever was affected "from 1 April" and Axe Arena "from 15 May", and the engine page says "nothing in the record yet marks it restored", while LIVE_EVENT_PERFORMANCE shows completed weekend runs through June and early July and normal runs from 2025-07-25. Claim 5's status depends only on September runs, so keep the rubric and OEs off outage dates and durations. SC-1–SC-3 are not touched.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2 PASS, SQL bc3abbdf…): Check A (references, collisions, Slack authors are channel members), Check B (structure, doubled apostrophes), Check C chronology. Prompt-specific checks NEW.
- Prompt-specific sources, access and configuration: supported (no error/async config).

---

### Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 2 | Unresolved forks F1–F8 (Deep Recheck fork list) change register decisions/statuses, the posted counts, the page or the ticket contents |
| Prompt | Feasibility | 5 | All writes cataloged; all facts exist |
| Prompt | Persona ACL Reachability | 5 | Every scoped read is Julia's |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 3 | Same writes under every reading; minor open points |
| Prompt | Contrived / Unnatural | 2 | Hidden tab destination; spec-sheet register (2 triggers) |
| Prompt | Alignment with Today's Date | 5 | Consistent with the clock |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | 11 premises verified |
| Prompt | Tool Use & Cross-service | 5 | 6+ services change graded facts |
| Prompt | Investigation + Action | 5 | Findings drive four writes |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | Julia owns the work |
| Prompt | Business Function | 5 | Product |
| Prompt | Assigned Competency | 5 | Product Management |
| Prompt | Assigned Task Skill | 5 | Retrieval central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | All retrievable |
| Universe | Cross-Service Coherence | 2 | Season Pass Slack vs Snowflake with injected records on one side; $0.99 vs $2.99 starter pack |

---

### Issues Found:

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Keep vs qualify is undefined: corrected LIVE claims (W&C cadence, four bundles, 4,755 levels, launch date) can be KEEP or QUALIFY; decision counts swing from KEEP 5/QUALIFY 5 to KEEP 9/QUALIFY 1 | Major | UGT |
| 2 | Win & Collect: ENG-1385 "not daily" vs windows covering every day | Major | UGT |
| 3 | "Anything we can't support" may mean only the two dropped claims or every claim not supported as written | Major | UGT |
| 4 | Live-ops engine has no status under the standard (no players to enable) | Major | UGT |
| 5 | Season Pass: base Slack says it sold in DD; Snowflake says no sales; injected comments side with Snowflake | Major | Cross-Service Coherence |
| 6 | ENG-2136 "$0.99 starter pack" vs warehouse $2.99 | Moderate | Cross-Service Coherence |
| 7 | "the tab we already use" hides a destination Julia would name | Major | Contrived |
| 8 | Deliverable-spec wording (row/column/decision list, count breakdown, conflict-column rule) | Major | Contrived |
| 9 | Confluence "list what came out" scope, conflict-column scope, owner column and launch-date status are undefined (blind P1 pass) | Major | UGT |

### Recommended Improvements:

1. Define the decision values in a seeded record Julia can see (a line on the external wording card or in Leonard's thread) that says which decision a LIVE claim with a corrected number, date or cadence gets. That one rule settles F1 and F2.
2. Make the Win & Collect record agree with itself: either make ENG-1385 say the windows cover every day, or make the calendar and the warehouse runs show gaps. Do not leave "not daily" next to windows that cover every day.
3. Say in the prompt or in Leonard's thread which claims go on the follow-up ticket (only the dropped ones, or every claim whose wording changed).
4. Give the live-ops engine and the launch-date line a status, or take them out of the draft: seed a line (scope note or standard) saying how internal tooling and date lines are statused and counted.
5. Settle the three open register cells in the seeded records: whose name goes in `owner` (Julia, or each feature's owner), what `evidence_date` holds (last run date or evidence record date), and what counts as a source disagreement for `conflict`. Also say whether the Confluence "what came out" list covers removed claims only or also replaced wording.
6. Season Pass: take the Season Pass claim out of the draft, or replace it with a feature that has no base Slack history of selling in Domino Delights. Rewording the injected comments does not fix it, because Snowflake still shows no DD Season Pass sale against the July Slack message.
7. ENG-2136: remove "$0.99" (the only starter SKU is dd_starter_pack at $2.99) or drop the out-of-moves sentence.
8. Name the tab ("the Register tab") and cut the deliverable spec: keep the asks (fill the register, post the counts, fix the page, file the ticket) and leave the column list, count breakdown and conflict rule to Leonard's thread and the Confluence conflict-format page, which already carry them. Prompts are screened for AI-written text, so put any rewrite in your own voice.

After changing the SQL, run /injection, /prompt, /hardness, /oe and /rubric again in that order; after changing only the prompt, run /prompt, /hardness, /oe and /rubric.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5) general-purpose subagents at session effort, each blind to the main review (given only the saved inputs, the universe, the persona references, `common_errors.md` and `deep_recheck.md`).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 10 sentences | 11 (DR1–DR9 forks, DR10–DR11 settled forks) | 9 forks confirmed; 2 settled-fork notes confirmed as settled |
| P2 | 10 sentences | 3 | 2 |
| P3 | 10 sentences | 2 (advisory) | 2 advisories, not scored |
| P4 | 10 sentences | 3 | 2 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR1 | P1 | "including whether we keep, qualify or drop it" | Trello 68d67230…0d11 "Numeric and date claims state the exact value in the register."; ENG-2371 "Four coin bundles, not five." | §2 decision set | Unique Ground Truth | CONFIRMED | Same as main fork E; no record defines keep vs qualify (F1) |
| P1-DR2 | P1 | "the scope note Leonard sent fixes which claims belong in the pack" | Scope note "even when they are live"; ENG-2370 "internal admin surface only, no player-facing surface" | §2 set / status | Unique Ground Truth | CONFIRMED | Same as main fork D (F3); the Register `scope` column and `row_count` 14 favour 13 rows but nothing statuses the engine |
| P1-DR3 | P1 | "Anything we can't support goes on a follow-up ticket" | Leonard b5387eae… "put anything we can''t support on the claims review ticket" | §2 ticket set | Unique Ground Truth | CONFIRMED | Same as main fork C (F2) |
| P1-DR4 | P1 | "bring it in line and list what came out" | page_q4_product_claims "All 13 product claims are live." | §2 page contents | Unique Ground Truth | CONFIRMED | No record says whether replaced wording counts as "came out" (F5) |
| P1-DR5 | P1 | "Where a claim's sources disagree, put both in the conflict column" | page_domino_gdd "~4,800 levels across 160 chapters" vs DES-313 "4,755 active" | §2 conflict set | Unique Ground Truth | CONFIRMED (narrowed) | Confirmed for approximate/older sources (GDD ~4,800; calendar "Failed Nov 2024"; outage page). Rejected parts: ENG-2374's "EVT-0526 (2025-09-28)" was written 2025-09-29 17:10Z, before EVT-0532 (09-30); ENG-2373 "recurring weekly slot" matches the calendar's "Recurring weekly"; the starter price is not in claim 9's text (F6) |
| P1-DR6 | P1 | "every column" | Draft "Owner: Julia Lawson"; card "Every retained claim names an owner."; evidence comments by Brian, Calvin Price, Samuel Turner | §2 owner cells | Unique Ground Truth | CONFIRMED | No record names a per-claim owner (F7) |
| P1-DR7 | P1 | "every column" | Register header `evidence_date`; ENG-1385 comment 2025-09-29 vs EVT-0529 2025-09-29→30 | §2 edge values | Unique Ground Truth | CONFIRMED (minor) | Run date vs evidence-record date; several cells, not one figure. Recorded in the fork list; rubric must accept either |
| P1-DR8 | P1 | "using the live-claim standard we agreed at the Q4 review" | Trello 68daad00… "enabled for 100% of production players"; no enablement record except ENG-2323 (10%) and ENG-2136 (default=false) | §2 source rule | Unique Ground Truth | CONFIRMED (minor) | Merged with P2-DR2; scored under Clarity 3, listed in the fork list |
| P1-DR9 | P1 | "Work through it line by line" | Draft "13. Domino Delights launched on 14 April 2025."; standard "the feature is enabled" | §2 event | Unique Ground Truth | CONFIRMED | A date line has no feature status; status counts change (F8) |
| P1-DR10 | P1 | "the external wording rules product signed off on" | Trello 68d67230…0d11 (2025-09-26) vs page_external_messaging_guide (2025-09-08) | §2 source rule | Unique Ground Truth | CONFIRMED as settled | Newer card, narrower scope ("product claims"), and the guide's "Anything shipped this quarter may be described as live" contradicts the incorporated standard |
| P1-DR11 | P1 | "My Q4 claims draft is the list." | Records listed in the pass | §2 settled forks | Unique Ground Truth | CONFIRMED as settled | Matches the main review's settled forks |
| P2-DR1 | P2 | "the external wording rules product signed off on" | Trello 68d67230…0d11 vs page_external_messaging_guide | §3 coherence | Cross-Service Coherence | REJECTED | Two dated rule documents where the newer, product-claims-specific card supersedes a general guide is a designed decoy, not one fact recorded two ways; settled under UGT (P1-DR10) |
| P2-DR2 | P2 | "against what's actually live, using the live-claim standard" | LIVE_EVENT_PERFORMANCE has no enablement column | §3 data exists | Clarity | CONFIRMED (minor) | Merged with P1-DR8; Data Exists stays 5 because a completed run with no partial-rollout flag is readable as full enablement |
| P2-DR3 | P2 | "with the evidence" | ENG-2136 "$0.99 starter pack" vs IAP_TRANSACTIONS dd_starter_pack 2.99 (95 rows) | §3 coherence | Cross-Service Coherence | CONFIRMED | Already in the main Coherence finding |
| P3-DR1 | P3 | SQL column lists | `references/schema/injection.json` (unverified snapshot) | SQL static | Injection SQL structure | CONFIRMED (advisory) | The snapshot is unverified; missing columns alone are advisory and Eval 0 passed; not scored |
| P3-DR2 | P3 | SQL header "freeze 2025-10-01T00:00:00Z" | Assignment "October 1, 2025 07:00" | Clock | Alignment with Today's Date | CONFIRMED (advisory) | SQL comment the Agent never sees; no record falls between the two times; not scored |
| P4-DR1 | P4 | "in the tab we already use" | Register (header only) vs Old register (C01–C09); Leonard "the tab you already use" | §2.7 hidden destination | Contrived / Unnatural | CONFIRMED | Matches the main finding |
| P4-DR2 | P4 | "one row per claim, every column, including whether we keep, qualify or drop it" / "broken out by status and by decision" / "put both in the conflict column" | page_q4_claims_conflict_format repeats the rule | §2.7 spec-sheet register | Contrived / Unnatural | CONFIRMED | Matches the main finding (two triggers) |
| P4-DR3 | P4 | "— the scope note Leonard sent fixes which claims belong in the pack." | Wording only | §1.2 AI-text | Contrived / Unnatural | REJECTED | Em dashes and one semicolon are not on the §1.2 red-flag list; sentence lengths vary (4 to 40 words) and "Can you take it?" is a natural shortcut. Advisory: plain hyphens read less polished |

Effect on verdict: unchanged (FAIL 2). UGT gained forks F5–F8; Contrived and Cross-Service Coherence findings were confirmed independently; no new dimension failed.

- F1: decision for corrected LIVE claims (C03 Win & Collect, C09, C12, C13) | KEEP 5 / QUALIFY 5 / DROP 3 | KEEP 9 / QUALIFY 1 / DROP 3 (W&C alone: KEEP 6 / QUALIFY 4) | Missing: a dated record Julia can see that defines keep vs qualify for a live claim with corrected wording, and which source governs Win & Collect's "daily"
- F2: follow-up ticket contents | Season Pass and Collectibles only | also every claim not supported as written (seven) | Missing: a prompt sentence or record defining "can't support"
- F3: live-ops engine status | LIVE / DROP (scope note "even when they are live") | NOT_LIVE or unstatused / DROP, or no row | Missing: a rule for statusing and counting internal tooling
- F4: 100% enablement prong (minor) | completed runs with no partial flag = LIVE | not provable, cannot mark Live | Missing: an enablement record or a sentence accepting completed runs as full enablement
- F5: Confluence "what came out" | dropped claims only | dropped claims plus replaced wording | Missing: which removals the page lists
- F6: conflict column scope | claim-text disagreements only | also approximate/older sources (GDD ~4,800, calendar "Failed Nov 2024", outage page) | Missing: what counts as a source disagreement
- F7: owner column | Julia on every row | each feature's engineering owner | Missing: a record naming per-claim owners
- F8: launch-date line status | LIVE / QUALIFY | no status (LIVE count 9) | Missing: how a date line is statused
- evidence_date (minor) | last completed run date | date of the evidence record | Missing: definition of evidence_date
- Settled: register tab = Register (only tab with `conflict`); wording source = 2025-09-26 product-claims card; launch dates = GDD 11 April 2025 / 6 May 2025 per scope note; Season Pass NOT_LIVE (Leonard 18:00Z, ENG-2136); Collectibles NOT_LIVE (Brian 17:00Z, Leonard 18:00Z); Hero Offers TESTING (10% cohort); coins = four; levels = 4,755; offer calendar excluded ("the claims draft you started is the set"); 13 rows ("one row per claim").

Platform defects: none

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1

Eval release SHA-256: 6478616fae461adfff81f45b2a523017b7a8e042bf02b6afc8c113d659886b8f

Reviewed prompt SHA-256: 76500140c70a687cbacdbe517ba111ec9129c91a99dcb72e9f00ec8b0085b4e0

Review context SHA-256: 38c50b2ae3d847395b34265ba23ee696625c67dffb59d55ed3eb4948a25d26b4

Prompt record SHA-256: 37c4ad2011b322abc7ab56dba3a0afcffdca5fb2d63b72fb168ad59ec1466654

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Fix the UGT forks with seeded decision/ticket/status rules, take Season Pass out of the claim set (or swap it for a feature with no base sales history), fix the $0.99 starter price in ENG-2136, and name the Register tab while trimming the deliverable spec; then rerun /injection (if SQL changed), /prompt, /hardness, /oe and /rubric in that order.

Evidence limits: Snowflake was read with a byte-offset streaming reader because `hg_search.py` timed out on the 2.2 GB export (tables 4, 9, 12, 18, 35, 36 decoded in full); Docs PDFs/XLSX were not re-extracted this run; static SQL only, never executed.

**Lowest Dimension:** Unique Ground Truth / Contrived / Cross-Service Coherence - 2 - unresolved decision, ticket and status forks; hidden tab destination and deliverable-spec wording; Season Pass Slack-vs-Snowflake conflict with injected records on one side.

**Summary:** The scenario is well seeded and grounded: every premise checks out and every write has a cataloged path. It fails because the keep/qualify/drop vocabulary, the follow-up ticket set and several statuses and register cells have no deciding record, which changes the posted counts. The prompt also hides the tab and reads like a deliverable spec, and the Season Pass claim rests on Slack and Snowflake records that disagree.
