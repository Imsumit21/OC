# Prompt Brief — frederick_bridge_pipeline · prep
> Built 2026-11-02 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Universe_Inject.sql (rev3, sha256 952e12a9ad7a, `/injection` PASS in Platform_Report/injection_report3), Working_Files/01_Grounding_Dossier.md, 01_Scenario_Design.md, 01_Hardness_Manifest.json, 01_Gradable_Surface.json, solver/truth.json (sha256 cda8fce125b347aa), 03_Error_Async_Config.txt (Friction: none, error-async gate PASS) · no 02_Reference_Files_Manifest.md (no attachments) · Persona view verified: all (every §5 fact YES for frederick_stone; seeded rows by check-sql, base rows by persona_view search and can-see).
> Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Persona today is Wed Oct 1, 2025; the seed bound is 2025-10-01T00:00:00Z and the latest seeded record is Leonard's ask at 2025-09-30T21:05Z (2:05pm PT).
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. This brief holds facts, noun phrases and locators only; it has no draft sentence.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive → `task_categories.md` "Founders / Exec / Strategy" (executive coordination, board prep) | a co-founder owns one section of the Oct 14 board pre-read while the CEO travels (frederick.stone@harmonygames.co/1844724419788800011); the board meeting is evt_bd61f3209523d19fdd6ba2 |
| Persona | Frederick Stone · frederick.stone@harmonygames.co · Co-founder (roster); Contacts 175c0d7bc72ed244b944cb90 says "Commercial Lead, Marketing & Business Development" (SC-49, never graded) | voice: a terse founder asking his assistant to take a job off his plate. Remit: on the cc of every bridge investor thread (frederick.stone@harmonygames.co/1842277743427687737, frederick.stone@harmonygames.co/1843547312959065138), a member of #bridge-pitch C096HFA5Z8W and #executives C07C2866011, invited to the Oct 14 board (evt_bd61f3209523d19fdd6ba2), and the addressee of Leonard's ask. Read scope: his own mailbox and calendar, the two channels, Drive files shared with him or owned by him; Trello, Linear and Contacts are unscoped |
| Competency | Corporate Ops (taxonomy: fundraising, board; outputs: spreadsheets, memos) | the fundraising section of the board pre-read: an investor-pipeline spreadsheet with committed vs soft-circled money, the keep-warm follow-through Leonard's card asks for, and the slide numbers back to Leonard (hub frederick.stone@harmonygames.co/1844724419788800011) |
| Task skill | Retrieval (stacked: Analysis and Synthesis; Actions) | Retrieval: each firm's status, latest two-way contact, money and tester access, pulled from mail, Slack threads, calendar, Contacts, Linear and the list f_48247af79428823c3cac92. Analysis: apply the Oct 14 template's definitions (f_3b9e61c04d7a52e8f1a6c2) over conflicting sources. Actions: the sheet in d_5e8a1c3f9b07d2e64a1b93, the checklist on card 68c5a49e8491a9d7faf869d0, the reply on the hub |
| Task type | long-horizon → Long Horizon tier (100–500+ calls); difficulty mode medium (cap < 85%; the user's target ≤ 80%) | 10 services carry weight (gmail, slack, gcal, gsheets, gdocs, gdrive, gslides, trello, linear, contacts). Measured volumes: 79 register firms (80 list rows / 77 names on f_48247af79428823c3cac92 plus 2 off-list calls); 12 "Leonard Hayes" calls on Frederick's calendar in scope of the sweep (10 base + 2 seeded, §5a F15); per-firm mail and Slack searches. Manifest call_budget: 502 honest calls (333 per-record), 01_Hardness_Manifest.json; HARDNESS GATE (extreme): PASS in 01_Grounding_Dossier.md |

Known data issues (references/known_data_issues/synthcut.md) the asks touch, none graded on a "don't grade" value:
- SC-33 (watch: Acterra twice on f_48247af79428823c3cac92): the template counts a repeated name once (f_3b9e61c04d7a52e8f1a6c2); the register count is the only value resting on it (§12).
- SC-34 (row 82 Superplay label, Supercell contents): one row under either name; its status is not sampled.
- SC-9 (Play Ventures rejected vs no reply): both statuses accepted (C096HFA5Z8W/1757955553.793529, C096HFA5Z8W/1758671737.632949).
- SC-10 (LVP meeting Sep 7 vs Sep 9): no LVP date graded; status from frederick.stone@harmonygames.co/1842277743427687737.
- SC-40 (July board date): the decoy template says "for the Jul 16 board" (f_8d2c47a91e05b3f6d7c418); not graded.
- SC-49 (founder count, Frederick's title): not graded; role rests on activity (evt_bd61f3209523d19fdd6ba2).
- SC-3 / SC-73 (runway, burn): no cash figure is read or graded.

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard, flying to LA on Oct 1, hands Frederick the fundraising section of the Oct 14 pre-read on Tue Sep 30 at 2:05pm PT and wants a reply with the slide numbers | Frederick (To); Robert and Arthur on cc | frederick.stone@harmonygames.co/1844724419788800011 | none needed: Frederick holds the To copy (dossier §1.E) |
| the 2025 investor list's Latest Status column stops at 09/11 | Frederick (shared reader) | f_48247af79428823c3cac92 | none |
| Leonard's #executives angel post and his Bridge angels sheet show two angels as in | Frederick (#executives member; sheet shared) | C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e | none |
| two "Board pre-read - fundraising section" docs sit side by side | Frederick (shared reader) | f_3b9e61c04d7a52e8f1a6c2, f_8d2c47a91e05b3f6d7c418 | none |
| Robert wants the pipeline emailed straight to the board; Leonard's ask says no | Frederick (To on both) | frederick.stone@harmonygames.co/1844623441920000059, frederick.stone@harmonygames.co/1844724419788800011 | none |

## 3 · Investigation → action

Questions (answers stay in §4b and §5):
- Who goes in the table: which names on the 2025 list (repeats included once), and which firms off the list had a pitch call or meeting since the Sep 3 kickoff that counts as investment talks?
- Which template bucket fits each firm as of end of day Tue Sep 30 PT, counting phone passes once written in #bridge-pitch and partners writing from their own addresses?
- What is signed (a DocuSign Completed notice) and what is only a written yes with an amount, and which amount is each investor's latest?
- For firms in talks, which are on the TestFlight group and which on the Play internal track for the current build?
- Which firms that passed had been pitched on a call or meeting first?
- Which numbers does the fundraising slide take, and how is the sheet named and where is it filed?

Writes fed by those answers:
- the register sheet in Frederick's Board - Oct 14 2025 folder (questions 1–4 and 6);
- the keep-warm checklist on the Existing Investor Update card (question 5);
- the reply on Leonard's email with the slide numbers (question 6 plus the sheet's totals).
Each write depends on the investigation: none can be written from the prompt or the hub alone.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| D1 fundraising register (Google Sheet) | one row per firm (each name on the 2025 list once, plus off-list firms pitched on a call or meeting since Sep 3); the template's columns (slide 9 of f_a47d0e2c95b18f63e2c0d5): Firm, Status, Last two-way contact, Build access, Committed, Soft-circled; statuses in the four buckets as of end of Sep 30 PT; committed = signed SAFEs; soft-circled = latest written amount; build access for firms in talks; committed and soft-circled totals at the bottom (f_3b9e61c04d7a52e8f1a6c2) | folder d_5e8a1c3f9b07d2e64a1b93, named per README f_c61a0e93b7d24f58a2e917 | none (filed in Frederick's own folder, frederick.stone@harmonygames.co owner) | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file | F1–F20, F23–F25, F27–F30 |
| D2 keep-warm checklist | one checklist named for keep-warm, one item per firm that passed after a pitch call or meeting (rule 68c64270d660c977c4696986) | Trello card 68c5a49e8491a9d7faf869d0 | none (Trello) | trello_create_checklist, trello_create_check_item | F11–F15, F21, F27 |
| D3 reply to Leonard | the three slide numbers named on card 68d8193cf451863621c88a2a (comment 68d81f30a6c94e2b7d05e1f4): how many firms are on the sheet, total committed, total soft-circled; a sheet link is optional | reply on thread frederick.stone@harmonygames.co/1844724419788800011 (message frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>) | leonard.hayes@harmonygames.co (reply), or with robert@harmonygames.co and arthur.blake@harmonygames.co (reply-all) | gmail_reply_to_message | F22, D1 |

Alternatives a careful run could defend:
- Reply vs reply-all on the hub frederick.stone@harmonygames.co/1844724419788800011: same decision, thread and contents; both accepted.
- Create the sheet in Frederick's root and move it vs create it in place: only the final parent d_5e8a1c3f9b07d2e64a1b93 is material.
- Send the reply now vs leave a draft: the hub asks "once it's done reply here" (frederick.stone@harmonygames.co/1844724419788800011) and the prompt asks for the reply; a draft is not a send (C18), so it does not deliver D3.
- Email the board as Robert asked (frederick.stone@harmonygames.co/1844623441920000059): not fair; the hub withdraws it ("Let's not, it goes in the deck.").
- Edit the deck f_a47d0e2c95b18f63e2c0d5: not asked; Leonard stitches the section in himself (hub frederick.stone@harmonygames.co/1844724419788800011).
- a16z In talks vs Passed (frederick.stone@harmonygames.co/1842277213140775733, frederick.stone@harmonygames.co/1844748127814183717): both fair; a Passed reading adds a fourth keep-warm item, also accepted.

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| D1 | file kind and parent | a native Google Sheet whose parent is d_5e8a1c3f9b07d2e64a1b93 (README f_c61a0e93b7d24f58a2e917: "Google Sheets or Docs only, no uploads") | "Please put the sheet in your Board - Oct 14 2025 folder" | created there or moved there; one sheet | material |
| D1 | file name | README pattern `Fundraising - Oct 14 board` (f_c61a0e93b7d24f58a2e917) | "the README in that folder says how to name it" | any name carrying fundraising, pipeline or bridge; case and dash variants | representational |
| D1 | population | 79 rows: the 77 distinct names on f_48247af79428823c3cac92 (Progression Fund, BITKRAFT Ventures and Acterra once each; angels included; the `[PERSON_NAME_5402]` token kept as written; row 82 as Superplay or Supercell, SC-34) plus Homa (evt_89381fe5a15b802c5652a9) and Brightwater Games Fund (evt_2f86b0d4c9e17a35b64e0d); T-accelerate is one row (PXLite alias, frederick.stone@harmonygames.co/1843978997950200606) | "every firm on the 2025 game investor list, plus anyone we've had a call with since the Sep 3 kickoff who isn't on it" | list spelling or the obvious full form (Homa / Homa Games; Brightwater / Brightwater Games Fund; T-accelerate / T-Accelerate Capital); any row order; a totals row is not a firm | material |
| D1 | Status · Sciplay | Passed: Robert's written phone pass C096HFA5Z8W/1759184040.552871 overturns frederick.stone@harmonygames.co/1842285743246816270 | "Please use the buckets and definitions in the board pre-read template" | the template's bucket words, any case (f_3b9e61c04d7a52e8f1a6c2) | material |
| D1 | Status · Hiro Capital | Passed: frederick.stone@harmonygames.co/1844318935449600041 from Edith Vane (e3a91c07d5b48f26a0c7e314) after the Sep 23 call evt_7d3e19b04a6c25f8e1b9a0 | "Please use the buckets and definitions in the board pre-read template" | as above | material |
| D1 | Status · Homa | In talks: call evt_89381fe5a15b802c5652a9, firm named in frederick.stone@harmonygames.co/1843169166284025277 | "Please use the buckets and definitions in the board pre-read template" | as above | material |
| D1 | Status · Brightwater Games Fund | In talks: call evt_2f86b0d4c9e17a35b64e0d, follow-up and reply frederick.stone@harmonygames.co/1844276782694400053, contact b72f0d6e19c3a84e5d21f9a0 | "Please use the buckets and definitions in the board pre-read template" | as above | material |
| D1 | Status · London Venture Partners | Passed: frederick.stone@harmonygames.co/1842277743427687737 (call evt_e59dc0a675d0c407b79acf) | "Please use the buckets and definitions in the board pre-read template" | as above | material |
| D1 | Status · firms with two fair readings | Andreessen Horowitz In talks or Passed (frederick.stone@harmonygames.co/1844748127814183717); Play Ventures Passed or Awaiting reply (C096HFA5Z8W/1757955553.793529, SC-9); Treo VC and Mattel Awaiting reply or In talks (C096HFA5Z8W/1757345124.546449, C096HFA5Z8W/1756941551.539229); BITKRAFT Ventures, General Catalyst, Superplay, Triptyq, Turkven, Harlem Capital Awaiting reply or Not contacted this round; Transcend Fund and Acterra Not contacted this round or Awaiting reply; March Gaming Fund and Index Ventures Not contacted this round or Passed (solver/truth.json accepted_status) | "Please use the buckets and definitions in the board pre-read template" | either listed bucket | material (each set closed) |
| D1 | Status · every other firm | solver/truth.json Status (list evidence f_48247af79428823c3cac92 and the cited threads); angels (Anton Bernstein, Paul Heydon and the other list angels) any bucket, since their state sits in the money columns | "Please use the buckets and definitions in the board pre-read template" | the template's bucket words | material for sampled firms; angels representational |
| D1 | Committed · Anton Bernstein | 25,000: amount trimmed in frederick.stone@harmonygames.co/1844162278195200023, signed per frederick.stone@harmonygames.co/1844354293432320031 | "The money lines matter most" | 25000, 25,000, $25,000, $25K, 25k (USD) | material |
| D1 | Committed · Paul Heydon | none: no Completed notice; SAFE still unsigned per frederick.stone@harmonygames.co/1844610859008000037 | "The money lines matter most" | blank, 0, $0, a dash | material |
| D1 | Soft-circled · Paul Heydon | 50,000 (C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e) | "The money lines matter most" | 50000, 50,000, $50,000, $50K, 50k | material |
| D1 | Soft-circled · Anton Bernstein | none (signed, so committed): frederick.stone@harmonygames.co/1844354293432320031 | "The money lines matter most" | blank, 0, a dash | material |
| D1 | totals | committed 25,000; soft-circled 50,000 (solver/truth.json; template f_3b9e61c04d7a52e8f1a6c2 "Put the committed and soft-circled totals at the bottom of the sheet") | "The money lines matter most" | a totals row or labelled cells below the table; the numeric forms above | material |
| D1 | Build access · Dentsu Ventures | iOS only: TestFlight added, Play internal track not added (ZOM-567 comment lc_b549f3057640a5eb08f7581e overturns frederick.stone@harmonygames.co/1844294398771200045) | "Please use the buckets and definitions in the board pre-read template" | iOS only; TestFlight only; iOS yes, Android no | material |
| D1 | Build access · T-accelerate | iOS and Android (ZOM-567 comment lc_94eb35d962cfbdd31e1bd496) | "Please use the buckets and definitions in the board pre-read template" | both; iOS + Android; TestFlight and Play | material |
| D1 | Build access · other firms in talks | none: GFR Fund (frederick.stone@harmonygames.co/1843547312959065138), NCsoft (frederick.stone@harmonygames.co/1832208184829815962), Homa, Brightwater, a16z when In talks (no ZOM-567 comment) | "Please use the buckets and definitions in the board pre-read template" | none, no, not on the tester list | material (not sampled) |
| D1 | Build access · firms not in talks | blank (template: "For firms in talks", f_3b9e61c04d7a52e8f1a6c2) | — | blank, n/a, a dash | representational |
| D1 | Last two-way contact | a date per firm, Pacific (f_3b9e61c04d7a52e8f1a6c2) | "Please use the buckets and definitions in the board pre-read template" | Pacific or UTC date, any date format | representational (not graded) |
| D2 | checklist location and name | a checklist on card 68c5a49e8491a9d7faf869d0 named for keep-warm (rule 68c64270d660c977c4696986: "a Keep warm checklist on this card") | "Whatever the Existing Investor Update card says to do for firms that pass, do that too" | name Keep warm or a close variant; location fixed | location material; name representational |
| D2 | items | London Venture Partners, Sciplay, Hiro Capital (solver/truth.json keepwarm; calls evt_e59dc0a675d0c407b79acf, evt_7d3e19b04a6c25f8e1b9a0, Sciplay call evt_25c9ee60d4b6c8f6d39a74); Andreessen Horowitz accepted as a fourth item when the sheet marks it Passed | "Whatever the Existing Investor Update card says to do for firms that pass, do that too" | one item per firm; list spelling or obvious forms (LVP; SciPlay) | material |
| D3 | thread and recipients | a reply on frederick.stone@harmonygames.co/1844724419788800011 to leonard.hayes@harmonygames.co | "reply here with the numbers the fundraising slide needs" | reply or reply-all (adds robert@harmonygames.co, arthur.blake@harmonygames.co) | thread material; reply vs reply-all representational |
| D3 | contents | 79 firms; committed $25,000; soft-circled $50,000 (card comment 68d81f30a6c94e2b7d05e1f4) | "The Board Deck card says which numbers the slide takes" | numeric forms as in D1; extra context (sheet link, a note on Dentsu's Android access) allowed | material |
| none | board email | no email to the board (frederick.stone@harmonygames.co/1844623441920000059 withdrawn) | "Let's not, it goes in the deck." | — | material |

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 hub ask | scope, template, folder, card, reply, no board email | frederick.stone@harmonygames.co/1844724419788800011 | YES (To, INBOX) | met first | none | Yes: Leonard's board pre-read email (anchor A1; Frederick received it) |
| F2 Oct 14 template | buckets, as-of end of Sep 30 PT, money and build-access definitions | f_3b9e61c04d7a52e8f1a6c2 (July decoy f_8d2c47a91e05b3f6d7c418) | YES (shared) | the July doc shares the title stem; the Oct 14 doc supersedes its "verbal yes" rule | first-framing latch on the July doc | No |
| F3 2025 game investor list | 80 rows, 77 names, Latest Status as of 09/11 | f_48247af79428823c3cac92 (lookalike f_0b29566cd7932a205d54d2) | YES (shared) | met first; overturned per firm by later mail and Slack | lookalike internal list; repeated names (SC-33) | No |
| F4 angel post | Paul $50K and Anton $40K "in" | C07C2866011/1758303600.418207 | YES (member) | met first (DONE1, INPUT); overturned by F6–F8 | stops at a conclusion-sounding post | No |
| F5 angels sheet | repeats F4 (Sep 20) | f_6e1d93a0c4b72f85d39a0e | YES (shared) | met first; overturned by F6–F8 | stale secondary source | No |
| F6 Anton's amount | $25K, "not the 40" (Sep 24) | frederick.stone@harmonygames.co/1844162278195200023 | YES (cc) | overturns F4 and F5 | agents rarely look for a later correction | No |
| F7 DocuSign Completed | Anton's SAFE signed Sep 26; none for Paul | frederick.stone@harmonygames.co/1844354293432320031 | YES (To) | decides committed | absence of Paul's notice needs a search | No |
| F8 Paul nudge | SAFE still with Paul (Sep 29) | frederick.stone@harmonygames.co/1844610859008000037 | YES (cc) | overturns "Paul is in" | — | No |
| F9 Dentsu invites claim | "Invites … are out to all three" (Sep 26) | frederick.stone@harmonygames.co/1844294398771200045 | YES (cc) | met first (DONE2); overturned by F10 | stops at Leonard's conclusion | No |
| F10 tester ticket | Dentsu TestFlight only; T-accelerate both | ZOM-567 (comments lc_b549f3057640a5eb08f7581e, lc_94eb35d962cfbdd31e1bd496) | YES (unscoped) | overturns F9 | agents prefer secondhand mail over Linear | No |
| F11 Sciplay phone pass | Robert's reply: Sciplay out (Sep 29) | C096HFA5Z8W/1759184040.552871 under C096HFA5Z8W/1757716998.377299 | YES (member) | overturns F12 (CORR) | channel history omits replies | No |
| F12 SciPlay thread | "We'll continue to play" (Sep 18) | frederick.stone@harmonygames.co/1842285743246816270 | YES (cc) | met first | reads as in talks | No |
| F13 unnamed-firm pass | thanks for Tuesday's session, pass on the bridge (Sep 26), no firm name | frederick.stone@harmonygames.co/1844318935449600041 | YES (cc) | overturns the list's "no response as of 09/11" for Hiro (ALIAS) | sender name does not ring a bell | No |
| F14 Edith Vane contact | Partner, Hiro Capital | e3a91c07d5b48f26a0c7e314 | YES (unscoped) | maps F13 to Hiro | — | No |
| F15 Tuesday pitch call | Sep 23 call with Hiro's people | evt_7d3e19b04a6c25f8e1b9a0 | YES (own calendar) | makes Hiro a pass after a pitch (keep-warm) | summary carries person tokens, not the firm | No |
| F16 Brightwater call | Sep 25 call, off the list | evt_2f86b0d4c9e17a35b64e0d | YES (own calendar) | off-list firm (FILT) | the list read as the whole population | No |
| F17 Ilse Marrow contact | Principal, Brightwater Games Fund | b72f0d6e19c3a84e5d21f9a0 | YES (unscoped) | names the firm behind F16 | — | No |
| F18 Brightwater follow-up | follow-up Sep 25 and Ilse's reply Sep 26; not a pass | frederick.stone@harmonygames.co/1844276782694400053 | YES (cc) | last two-way contact | — | No |
| F19 Homa invitation | updated invitation naming HOMA | frederick.stone@harmonygames.co/1843169166284025277 | YES (own mailbox) | names the firm behind F20 | — | No |
| F20 Homa call | Sep 18 call, off the list | evt_89381fe5a15b802c5652a9 | YES (own calendar) | off-list firm (FILT) | summary carries person tokens | No |
| F21 keep-warm rule | passes after a pitch call or meeting go on a Keep warm checklist, one item per firm | 68c64270d660c977c4696986 on 68c5a49e8491a9d7faf869d0 (decoy card 663ea0fc3f231e879cefd5e8) | YES (unscoped) | authority H2 | rule sits in a comment, not the description | Yes, the card's name only: the Trello destination Leonard's email names, so Frederick knows it (C16 hidden destination); never its rule |
| F22 slide numbers | firm count, total committed, total soft-circled | 68d81f30a6c94e2b7d05e1f4 on 68d8193cf451863621c88a2a | YES (unscoped) | decides D3 contents | older Board Deck cards (15 base hits) | No |
| F23 draft deck | slide 9 lists the table's columns | f_a47d0e2c95b18f63e2c0d5 | YES (shared) | confirms the columns | — | No |
| F24 Board folder | Frederick's Board - Oct 14 2025 folder | d_5e8a1c3f9b07d2e64a1b93 | YES (owner) | destination | — | Yes: a destination Frederick owns, named in the hub as his folder |
| F25 folder README | naming pattern `Fundraising - Oct 14 board` | f_c61a0e93b7d24f58a2e917 | YES (in his folder) | decides the file name | — | No |
| F26 review event | Mon Oct 6 9:00am PT review | evt_9c41e7a2d05b38f6e1a7c4 | YES (own calendar) | deadline | — | Yes: "Monday's review" is on his calendar |
| F27 LVP pass | pass Sep 25 after the Sep 9 call | frederick.stone@harmonygames.co/1842277743427687737 (call evt_e59dc0a675d0c407b79acf) | YES (cc) | keep-warm member | 14 hits for "LVP" | No |
| F28 T-accelerate thread | recap of the Sep 22 call; in talks | frederick.stone@harmonygames.co/1842283406259093714 | YES (cc) | in talks | — | No |
| F29 PXLite alias | PXLite fund thread is T-accelerate | frederick.stone@harmonygames.co/1843978997950200606 | YES (cc) | one row, not two | alias | No |
| F30 Karthic contact | T-Accelerate Capital (PXLite fund) | 5d0e8b31f7a29c64e1b0d3a8 | YES (unscoped) | confirms the alias | — | No |
| F31 Robert's board mail | email the pipeline to the board | frederick.stone@harmonygames.co/1844623441920000059 | YES (To) | distractor; withdrawn by F1 | — | No |
| F32 Arthur's aside | just list who Leonard emailed | C07C2866011/1759168800.117903 | YES (member) | distractor; the template's population rule overrides it | — | No |

## 5a · Search-as-persona proof

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
{{SEARCH_ROWS}}

The id column carries the deciding record; for base records the Found cell gives its rank in the pasted hit list (persona_view lists oldest first, so the newest thread sits last). `persona_view.py search` reads only the base export, so seeded rows return 0 there; the seeded count is a case-insensitive scan of the rev3 SQL rows Frederick can see (own mailbox and calendar copies, his two channels, files he owns or is shared on; Trello, Linear and Contacts unscoped), and seeded reach is the dossier's check-sql PASS for frederick_stone (§1.E). Queries are what Frederick would type after reading the hub and the records it leads to: the firm or person name from the list, the token name on a calendar invite, or the doc or card name the hub gives. No fact is NO, so nothing is routed.

```
{{SEARCH_OUT}}
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| register population (V1) | hub + template | deliverable: the fundraising section sheet, by pointing at Leonard's email | frederick.stone@harmonygames.co/1844724419788800011 · To Frederick · the only mail with that subject · states the scope rule, names no firm | gotcha → trigger via the hub |
| statuses (ST1–ST5) | template definitions f_3b9e61c04d7a52e8f1a6c2 | scope: Leonard's ask (template incorporated by the hub) | f_3b9e61c04d7a52e8f1a6c2 · shared · one Oct 14 template, the July one dated in its body · definitions only | gotcha → trigger via the hub |
| money (M1–M3) | template Money section | scope, via the hub | f_3b9e61c04d7a52e8f1a6c2 · as above · no amount | gotcha → trigger via the hub |
| build access (AC1–AC2) | template Build access + ZOM-567 | scope, via the hub | f_3b9e61c04d7a52e8f1a6c2 · as above · "Arthur tracks the tester adds", no firm | gotcha → trigger via the hub |
| destination and name (DL1) | hub + README f_c61a0e93b7d24f58a2e917 | destination: the Board - Oct 14 2025 folder, named in the prompt | f_c61a0e93b7d24f58a2e917 · in Frederick's folder · one README there · naming pattern only | the prompt names the folder |
| keep-warm checklist (KW1–KW2) | card comment 68c64270d660c977c4696986 | destination + constraint: the Existing Investor Update card, named in the prompt "like he asks"; the rule stays in its comment | 68c5a49e8491a9d7faf869d0 · Trello unscoped · one "Existing Investor Update" card (decoy "Investor Update" 663ea0fc3f231e879cefd5e8) · rule, no firm | gotcha → trigger via the hub |
| reply numbers (RP1–RP3) | card comment 68d81f30a6c94e2b7d05e1f4 | deliverable + recipient: the reply on Leonard's email | 68d8193cf451863621c88a2a · Trello unscoped · the only "Board Deck - Oct 14" card (in Doing) · names the three numbers, no values | the prompt names the reply |
| no board email | Robert's mail frederick.stone@harmonygames.co/1844623441920000059, withdrawn in the hub | none | the hub's "Let's not" | inferable from the hub; a board email is a wrong write, not a graded positive |

| Anchor | May be named (noun phrases only) |
|---|---|
| A1 | Leonard's board pre-read email; the fundraising section ask |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| clock and persona today | Wed Oct 1, 2025 00:00 PT (07:00 UTC) | Working_Files/00_Task_Context.json /universe/clock_utc | constraint |
| seed bound | 2025-10-01T00:00:00Z (Tue Sep 30, 5:00pm PT) | Working_Files/00_Task_Context.json /freeze_utc | constraint |
| Leonard's ask sent | Tue Sep 30, 2025 2:05pm PT (21:05Z); "yesterday" from Frederick's Oct 1 | frederick.stone@harmonygames.co/1844724419788800011 | past |
| Leonard travels | Wed Oct 1 morning ("flying to LA tomorrow morning") | frederick.stone@harmonygames.co/1844724419788800011 | today; not yet done at the clock |
| status as-of | end of day Tue Sep 30, 2025 PT (= Oct 1 07:00Z) | f_3b9e61c04d7a52e8f1a6c2 | past |
| bridge kickoff | Wed Sep 3, 2025 | f_3b9e61c04d7a52e8f1a6c2, frederick.stone@harmonygames.co/1844724419788800011 | past |
| review with Leonard | Mon Oct 6, 2025 9:00–9:45am PT (16:00Z) | evt_9c41e7a2d05b38f6e1a7c4 | deadline |
| board meeting | Tue Oct 14, 2025 | evt_bd61f3209523d19fdd6ba2 | future |
| Homa call | Thu Sep 18, 2025 8:00am PT | evt_89381fe5a15b802c5652a9 | past |
| Hiro call | Tue Sep 23, 2025 9:00am PT (16:00Z) | evt_7d3e19b04a6c25f8e1b9a0 | past |
| Anton trims to $25K | Wed Sep 24, 2025 16:10Z | frederick.stone@harmonygames.co/1844162278195200023 | past |
| Brightwater call | Thu Sep 25, 2025 8:30am PT (15:30Z) | evt_2f86b0d4c9e17a35b64e0d | past |
| Edith's pass | Fri Sep 26, 2025 09:40Z (2:40am PT) | frederick.stone@harmonygames.co/1844318935449600041 | past |
| Dentsu "invites out" | Fri Sep 26, 2025 17:20Z | frederick.stone@harmonygames.co/1844294398771200045 | past |
| Anton's SAFE Completed | Fri Sep 26, 2025 19:02Z (12:02pm PT) | frederick.stone@harmonygames.co/1844354293432320031 | past |
| Board Deck card comment | Sat Sep 27, 2025 17:30Z | 68d81f30a6c94e2b7d05e1f4 | past |
| Paul's nudge | Mon Sep 29, 2025 15:00Z | frederick.stone@harmonygames.co/1844610859008000037 | past |
| Sciplay pass written | Mon Sep 29, 2025 3:14pm PT (22:14Z) | C096HFA5Z8W/1759184040.552871 | past |
| ZOM-567 comments | Tue Sep 30, 2025 17:25Z and 18:40Z | ZOM-567 | past |
| keep-warm rule | Sun Sep 14, 2025 04:20Z (Sat Sep 13, 9:20pm PT) | 68c64270d660c977c4696986 | past |
| a16z Speedrun forward | Oct 1, 2025 03:21Z = Tue Sep 30, 8:21pm PT: inside the end-of-Sep-30-PT window; a base record after the seed bound | frederick.stone@harmonygames.co/1844748127814183717 | past (both a16z statuses accepted, §4b) |
| dates in the sheet | Pacific per the template; PT and UTC variants accepted | f_3b9e61c04d7a52e8f1a6c2 | constraint |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | where each answer lives: the list stops at 09/11 (f_48247af79428823c3cac92), a pass from an unnamed partner (frederick.stone@harmonygames.co/1844318935449600041), off-list calls on the calendar (evt_89381fe5a15b802c5652a9) | the prompt names the job, the folder, the card and the reply, never where the facts live |
| Dynamic change | yes | yes | corrections met second: C07C2866011/1758303600.418207 → frederick.stone@harmonygames.co/1844162278195200023; frederick.stone@harmonygames.co/1844294398771200045 → ZOM-567; frederick.stone@harmonygames.co/1842285743246816270 → C096HFA5Z8W/1759184040.552871 | the prompt names neither the first claim nor its correction; the reason to check ("the board will ask what's actually committed") is in the hub |
| Multi-source | yes | yes | 10 services (§1) | only the hub (A1) and the two destinations (the folder, the Existing Investor Update card) are named |
| Async | no | no | 03_Error_Async_Config.txt (Friction: none) | nothing to mention |
| Error recovery | no | no | 03_Error_Async_Config.txt | nothing to mention |
| Access control | no designed denial | no | every deciding record has a Frederick copy (01_Grounding_Dossier.md §1.E) | no ask about a restriction |

## 9 · Must not appear in the prompt

- Catalog tool names and parameters (Evals tool catalog): gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, trello_create_checklist, trello_create_check_item, trello_get_comments, gmail_reply_to_message, gmail_search_messages, slack search or history calls, linear_list_comments, contacts_search_contacts, gslides_get_presentation_text, any fileId or newParentId.
- MCP server names, "server", "connector", "the X tool".
- Opaque ids and filenames (01_Grounding_Dossier.md): every id in §5 (thread and message ids, f_/d_/evt_ ids, Trello and contact ids, ZOM-567, Slack timestamps), the Bridge angels sheet, the deck title.
- Findings and the root cause (dossier "Constraints for the prompt brief"): any firm name (Sciplay, Hiro Capital, Homa, Brightwater Games Fund, London Venture Partners, Dentsu Ventures, T-accelerate, PXLite, Andreessen Horowitz, GFR Fund, NCsoft), any person met during research (Edith Vane, Ilse Marrow, Karthic, Paul Heydon, Anton Bernstein, Ryo-san), any amount ($25K, $40K, $50K, totals), any count (79, 77, 80, "three numbers"), any status, "keep warm", DocuSign, TestFlight or Play track state, Robert's board idea, Arthur's aside.
- Rules that live in records: the buckets, the as-of time, the committed and soft-circled definitions, the build-access rule (f_3b9e61c04d7a52e8f1a6c2); the README naming pattern (f_c61a0e93b7d24f58a2e917); slide 9's columns (f_a47d0e2c95b18f63e2c0d5); the two card comments (68c64270d660c977c4696986, 68d81f30a6c94e2b7d05e1f4).
- Allowed by name (destinations Frederick knows): the Board - Oct 14 2025 folder, a reply on Leonard's email, the Existing Investor Update card in Trello (Leonard's email names it, frederick.stone@harmonygames.co/1844724419788800011). The card's keep-warm rule and who qualifies stay out.
- Injected friction: none configured (03_Error_Async_Config.txt), so nothing to hide; no forced error or wait may be implied.
- Reference files: none; no `/app/artifact` path.
- Format: Markdown, numbered steps, a column list, a per-deliverable content list, "first … then … finally" sequencing, if / but-not / then-also chains.
- Hints aimed at the traps (prompt_qc_cases.json trap_hint_or_riddle): "some numbers may be stale", "check the replies", "watch for duplicates", "partners write from their own addresses", "not everyone is on the list", "Leonard's post may be out of date".
- False or post-clock premises: Leonard "in LA" (he flies on Oct 1 morning), anything dated after Tue Sep 30 described as done, Victor Barnes acting.

## 10 · Entity traps

```
{{ENTITY_OUT}}
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Leonard Hayes | Gmail files named leonard@harmonygames.co_*; Contacts title "Co-founder & CEO" vs roster "Co-founder & Creative Director" | file naming and title only | leonard.hayes@harmonygames.co |
| Robert | Contacts "Co-founder & Chief Product Officer" vs roster "Co-Founder & Creative Director" | title only | robert@harmonygames.co |
| Arthur Blake | Gmail files named blake@harmonygames.co_* | file naming only | arthur.blake@harmonygames.co |
| Frederick Stone | frederick@ file alias; GitHub "Ryan" (S04, no GitHub record touched) | not used | frederick.stone@harmonygames.co |
| Game Investor List - Harmony Games 2025 | Internal Game Investor List f_0b29566cd7932a205d54d2 | a different, older list | f_48247af79428823c3cac92 |
| Board pre-read - fundraising section (Oct 14) | Board pre-read - fundraising section (July) f_8d2c47a91e05b3f6d7c418 | "for the Jul 16 board"; committed = verbal yes | f_3b9e61c04d7a52e8f1a6c2 |
| Existing Investor Update card | Investor Update card 663ea0fc3f231e879cefd5e8 | no keep-warm rule | 68c5a49e8491a9d7faf869d0 |
| Board Deck - Oct 14 card | earlier Board Deck cards (trello "Board Deck": 15 base hits) | older boards, in Done | 68d8193cf451863621c88a2a |
| Hiro Capital (list row) | Edith Vane writing without the firm name | alias through Contacts | e3a91c07d5b48f26a0c7e314 |
| T-accelerate (list row) | PXLite / T-Accelerate Capital | same firm, one row | 5d0e8b31f7a29c64e1b0d3a8, frederick.stone@harmonygames.co/1843978997950200606 |
| Sciplay (list row) | SciPlay in mail | case only | frederick.stone@harmonygames.co/1842285743246816270 |
| Superplay (row 82) | Supercell contents (SC-34) | one row under either name | f_48247af79428823c3cac92 |
| Treo VC | "Treeo" Slack spelling | spelling only, not a duplicate | C096HFA5Z8W/1756941551.539229 |
| ZOM-567 | ENG-#### tickets (trap_catalog N-series) | ZOM is the game team's series | ZOM-567 |
| Marcus Bennett / Marcus Lee / Oscar Bennett | the known Marcus trap | no Marcus or Oscar in any touched record | marcus.bennett@harmonygames.co |

## 11 · Pre-submit checklist

- [ ] One ordinary request in Frederick's voice: a co-founder handing his assistant a job, clean spelling, no spec language
- [ ] No Markdown, no numbered steps, no list of columns or sheet contents (the template holds them)
- [ ] Points at Leonard's board pre-read email (A1) as the source of the ask; names the Board - Oct 14 2025 folder, the Existing Investor Update card (Trello) and a reply on Leonard's email; may mention Monday's review
- [ ] Every write is asked of the assistant ("can you …"); no "I'll reply to Leonard" beside the same ask
- [ ] Does not name the template, the list, the Board Deck card, the README, the deck, the angels sheet, Robert's mail or the ticket, and does not restate who goes on the card's checklist
- [ ] Nothing from §9: no firm, person found in research, amount, count, status, "keep warm", DocuSign, tester state or id
- [ ] No hint or riddle aimed at a trap; no hedge letting a record correct the prompt
- [ ] Dates true at the clock: Leonard's email is from yesterday (Tue Sep 30); he is flying to LA today; Monday's review is Oct 6
- [ ] No tool, server or connector names
- [ ] 20–4,000 words; then `/create-prompt-writing check`

## 12 · Blockers and routed defects

| Item | Status | Locator |
|---|---|---|
| facts NO in §5a | none; nothing routed | §5a F1–F32 |
| surface regexes accept "25,000" and "25000" but not "$25K" / "$50K" | §4b accepts the K forms; the rubric criteria (LLM-graded) must accept them; the surface stays frozen with the rev3 SQL | 01_Gradable_Surface.json M2, RP2, RP3 |
| SC-33 watch on the register count (79) | only the V1 row and the reply's firm count rest on it; rubric fallback: grade per-firm rows and drop a bare count row if /rubric flags it | f_48247af79428823c3cac92, f_3b9e61c04d7a52e8f1a6c2 |
| facts UNVERIFIED | none | 01_Grounding_Dossier.md §1.E |

## 13 · Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`).** Phase 1: persona (§1.1) Frederick is the addressee of Leonard's ask and on every investor cc (§1); voice (§1.2) is judged against a co-founder only. Anti-patterns (§1.3): no command list, no bolt-ons (the checklist and the reply are both in Leonard's one ask, frederick.stone@harmonygames.co/1844724419788800011), no pre-solving (§9), no tool names (§9). Diversity (§1.4): three writes in Sheets/Drive, Trello and Gmail. Assignment and complexity (§1.5): Corporate Ops fundraising/board work, Retrieval stacked with analysis and actions; Ambiguity, Dynamic change and Multi-source load-bearing (§8). Phase 2: fair readings (§2.1) in §4b; feasibility (§2.2) every write in the catalog and every read YES (§5a); truthfulness (§2.3) the premises in §7; cross-service (§2.4) 10 services; investigation → action (§2.5) §3; clarity (§2.6) §4; contrived (§2.7) §9 and §11; today's date (§2.8) §7; originality (§2.9) no supplied sample, and the earlier Frederick task (account custody before layoffs, support/completed_tasks) shares only the persona. Phase 3: universe coherence rests on the rev3 `/injection` PASS (Platform_Report/injection_report3, SQL 952e12a9ad7a).

| Area | Counter-reading | Evidence | Resolution |
|---|---|---|---|
| Fair readings (C6) | Reading B: Paul Heydon is committed, since Leonard's post says he "is in for $50K" and the angels sheet lists him | C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e vs the incorporated template "Committed: signed SAFE only" (f_3b9e61c04d7a52e8f1a6c2), no Completed notice beside Anton's (frederick.stone@harmonygames.co/1844354293432320031), the Sep 29 nudge (frederick.stone@harmonygames.co/1844610859008000037) | an incorporated authority settles it (C6 step 2); §4b soft-circled 50,000 |
| Fair readings (C6) | Reading B: a16z passed (the Speedrun forward), which adds a fourth keep-warm item | frederick.stone@harmonygames.co/1844748127814183717 (Sep 30 8:21pm PT, inside the window) vs frederick.stone@harmonygames.co/1842277213140775733 | no newer source, authority or scope settles it; both statuses and the matching checklist are accepted outcomes in §4b and the sidecar |
| Fair readings (C6) | Reading B: Hiro Capital is Awaiting reply, as the list says | f_48247af79428823c3cac92 "no response as of 09/11" vs frederick.stone@harmonygames.co/1844318935449600041, e3a91c07d5b48f26a0c7e314 and the template's "A partner writing from their own address counts for their firm" (f_3b9e61c04d7a52e8f1a6c2) | a newer source plus the incorporated rule settle it: Passed |
| Fair readings (C6) | Reading B: reply-all to Robert and Arthur rather than to Leonard alone | hub cc list (frederick.stone@harmonygames.co/1844724419788800011) | same decision, thread and contents; both accepted (§4b D3) |
| Clarity (C7) | the prompt could leave the reply's channel open (Slack DM vs the email thread) | the hub says "reply here" (frederick.stone@harmonygames.co/1844724419788800011) | §11 box: the prompt names a reply on Leonard's email; check mode tests the real text |
| Clarity (C7) | "I'll stitch it into the deck" in the hub could pull a run into editing the deck | the deck f_a47d0e2c95b18f63e2c0d5 is Leonard's; the slide numbers go in the reply (68d81f30a6c94e2b7d05e1f4) | no deck write in §4; a deck edit is unrequested, not a second fair reading |
| Incorporation (C8) | does Leonard's email hand over the answer? | it names the scope, the template, the card and the folder but no firm, status or amount (01_Grounding_Dossier.md Fact sheet, FACT CHECK PASS) | instructions, not answers (prompt-incorporation-v1 (d)) |
| Incorporation (C8) | the keep-warm checklist lives only in a Trello comment, so it would be an untriggered requirement | the hub: "Whatever the Existing Investor Update card says to do for firms that pass, do that too" (frederick.stone@harmonygames.co/1844724419788800011) → 68c64270d660c977c4696986 | incorporated through the hub, which the prompt incorporates (§6) |
| Truthfulness (C17) | a premise like "Leonard emailed me this morning" or "Leonard's in LA" would be false at the clock | sent 2025-09-30T21:05:00Z (frederick.stone@harmonygames.co/1844724419788800011); "flying to LA tomorrow morning" | §7 and §11: "yesterday" or "Tuesday"; "flying out today" |
| Truthfulness (C17) | calling the folder "the board folder Leonard made" would be false | d_5e8a1c3f9b07d2e64a1b93 is owned by frederick.stone@harmonygames.co (check-sql YES) | the prompt may say "my Board - Oct 14 2025 folder" |
| Feasibility / ACL (C18–C19) | the catalog cannot put a new sheet in a folder | gsheets_create_spreadsheet has no folder parameter; gdrive_move_file(fileId, newParentId) places it; Frederick owns d_5e8a1c3f9b07d2e64a1b93 | feasible in two calls; §4b accepts create-then-move |
| Feasibility / ACL (C18–C19) | the Sciplay pass is a thread reply that channel history omits | C096HFA5Z8W/1759184040.552871 under C096HFA5Z8W/1757716998.377299 (reply counters updated); search finds it (§5a F11) | findable and visible to frederick_stone |
| Contrived (C15–C16) | naming the folder, the reply and Monday's review in one prompt reads as a spec sheet | Eval 1 §2.7; prompt_qc_cases.json hidden_destination | destinations the persona knows must be named; the contents stay in the template (§9) |
| Contrived (C15–C16) | leaving the Trello card unnamed ("the Trello follow-up he mentions") would hide a destination Frederick knows, and "for anyone who passed" would contradict the card's pitched-only rule | prompt_qc_cases.json K47-hidden-destination; card rule 68c64270d660c977c4696986 ("Email-only no's don't need it") | the prompt names the card and says "like he asks", leaving who qualifies to the card |
| Contrived (C15–C16) | a line like "some of Leonard's numbers might be old" would hint at the traps | prompt_qc_cases.json trap_hint_or_riddle | banned in §9; the hub's "the board will ask what's actually committed" is in the record |

Name-swap test: swapping Leonard for another founder breaks the task, since the hub, the folder README and the card comments are Leonard's records (frederick.stone@harmonygames.co/1844724419788800011, f_c61a0e93b7d24f58a2e917, 68c64270d660c977c4696986), so the scenario rests on real records.

Re-verified this run: the hub, template, README, both card comments and both ZOM-567 comments read from the rev3 SQL rows (base_check.parse_sql); the 32 searches in §5a run with persona_view as frederick_stone; entity.py collisions and resolve run now; the totals and statuses from solver/truth.json (sha256 cda8fce125b347aa); write tool names and parameters from the Evals tool catalog; Pacific times computed from the UTC stamps.

Unresolved: none blocking. Two rubric-stage notes are in §12 (K-form amounts; the SC-33 count watch).
