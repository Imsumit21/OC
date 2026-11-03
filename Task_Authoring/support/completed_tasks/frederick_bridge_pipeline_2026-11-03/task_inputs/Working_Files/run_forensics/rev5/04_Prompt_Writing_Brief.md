# Prompt Brief — frederick_bridge_pipeline · prep
> Built 2026-11-02 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Universe_Inject.sql (rev5, sha256 3ba2b413458f; rev4 2e2428bc5e49 passed `/injection` and failed `/prompt` only on Initial Capital and the ZOM-567 dates (Platform_Report/prompt_report2), fixed in rev5; rev3 952e12a9ad7a passed `/injection` but failed `/prompt` on data forks, Platform_Report/peompt_report1, settled in rev4), Working_Files/01_Grounding_Dossier.md, 01_Scenario_Design.md, 01_Hardness_Manifest.json, 01_Gradable_Surface.json, solver/truth.json (sha256 33d88dacdb04ab89), 03_Error_Async_Config.txt (Friction: none, error-async gate PASS) · no 02_Reference_Files_Manifest.md (no attachments) · Persona view verified: all (every §5 fact YES for frederick_stone; seeded rows by check-sql, base rows by persona_view search and can-see).
> Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Persona today is Wed Oct 1, 2025; the seed bound is 2025-10-01T00:00:00Z and the latest seeded record is Leonard's ask at 2025-09-30T21:05Z (2:05pm PT).
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. This brief holds facts, noun phrases and locators only; it has no draft sentence.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive → `task_categories.md` "Founders / Exec / Strategy" (executive coordination, board prep) | a co-founder owns one section of the Oct 14 board pre-read while the CEO travels (frederick.stone@harmonygames.co/1844724419788800011); the board meeting is evt_bd61f3209523d19fdd6ba2 |
| Persona | Frederick Stone · frederick.stone@harmonygames.co · Co-founder (roster); Contacts 175c0d7bc72ed244b944cb90 says "Commercial Lead, Marketing & Business Development" (SC-49, never graded) | voice: a terse founder asking his assistant to take a job off his plate. Remit: on the cc of every bridge investor thread (frederick.stone@harmonygames.co/1842277743427687737, frederick.stone@harmonygames.co/1843547312959065138), a member of #bridge-pitch C096HFA5Z8W and #executives C07C2866011, invited to the Oct 14 board (evt_bd61f3209523d19fdd6ba2), and the addressee of Leonard's ask. Read scope: his own mailbox and calendar, the two channels, Drive files shared with him or owned by him; Trello, Linear and Contacts are unscoped |
| Competency | Corporate Ops (taxonomy: fundraising, board; outputs: spreadsheets, memos) | the fundraising section of the board pre-read: an investor-pipeline spreadsheet with committed vs soft-circled money, the keep-warm follow-through Leonard's card asks for, and the slide numbers back to Leonard (hub frederick.stone@harmonygames.co/1844724419788800011) |
| Task skill | Retrieval (stacked: Analysis and Synthesis; Actions) | Retrieval: each firm's status, money and tester access, pulled from mail, Slack threads, calendar, Contacts, Linear and the list f_48247af79428823c3cac92. Analysis: apply the Oct 14 template's definitions (f_3b9e61c04d7a52e8f1a6c2) over conflicting sources. Actions: the sheet in d_5e8a1c3f9b07d2e64a1b93, the checklist on card 68c5a49e8491a9d7faf869d0, the reply on the hub |
| Task type | long-horizon → Long Horizon tier (100–500+ calls); difficulty mode medium (cap < 85%; the user's target ≤ 80%) | 10 services carry weight (gmail, slack, gcal, gsheets, gdocs, gdrive, gslides, trello, linear, contacts). Measured volumes: 79 register firms (80 list rows / 77 names on f_48247af79428823c3cac92 plus 2 off-list calls); 12 "Leonard Hayes" calls on Frederick's calendar in scope of the sweep (10 base + 2 seeded, §5a F15); per-firm mail and Slack searches. Manifest call_budget: 502 honest calls (333 per-record), 01_Hardness_Manifest.json; HARDNESS GATE (extreme): PASS in 01_Grounding_Dossier.md |

Known data issues (references/known_data_issues/synthcut.md) the asks touch, none graded on a "don't grade" value:
- SC-33 (watch: Acterra twice on f_48247af79428823c3cac92): the template counts a repeated name once (f_3b9e61c04d7a52e8f1a6c2); the register count is the only value resting on it (§12).
- SC-34 (row 82 Superplay label, Supercell contents): one row under either name; its status is not sampled.
- SC-9 (Play Ventures rejected vs no reply): settled in rev4 by Leonard's Sep 25 correction C096HFA5Z8W/1758817200.730591 (the Sep 15 no C096HFA5Z8W/1757955553.793529 was their reply to Griffin): Passed.
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
| D1 fundraising register (Google Sheet) | one row per firm (each name on the 2025 list once, plus off-list firms pitched on a call or meeting since Sep 3); the template's columns (slide 9 of f_a47d0e2c95b18f63e2c0d5): Firm, Status, Build access, Committed, Soft-circled; statuses in the four buckets as of end of Sep 30 PT under the template's rules; committed = signed SAFEs; soft-circled = latest amount, from the investor or written down by one of us; build access for firms in talks; committed and soft-circled totals at the bottom (f_3b9e61c04d7a52e8f1a6c2) | folder d_5e8a1c3f9b07d2e64a1b93, named per README f_c61a0e93b7d24f58a2e917 | none (filed in Frederick's own folder, frederick.stone@harmonygames.co owner) | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file | F1–F20, F23–F25, F27–F30 |
| D2 keep-warm checklist | one checklist named for keep-warm, one item per firm that passed after a pitch call or meeting (rule 68c64270d660c977c4696986) | Trello card 68c5a49e8491a9d7faf869d0 | none (Trello) | trello_create_checklist, trello_create_check_item | F11–F15, F21, F27 |
| D3 reply to Leonard | the three slide numbers named on card 68d8193cf451863621c88a2a (comment 68d81f30a6c94e2b7d05e1f4): how many firms are on the sheet, total committed, total soft-circled; a sheet link is optional | reply on thread frederick.stone@harmonygames.co/1844724419788800011 (message frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>) | leonard.hayes@harmonygames.co (reply), or with robert@harmonygames.co and arthur.blake@harmonygames.co (reply-all) | gmail_reply_to_message | F22, D1 |

Alternatives a careful run could defend:
- Reply vs reply-all on the hub frederick.stone@harmonygames.co/1844724419788800011: same decision, thread and contents; both accepted.
- Create the sheet in Frederick's root and move it vs create it in place: only the final parent d_5e8a1c3f9b07d2e64a1b93 is material.
- Send the reply now vs leave a draft: the hub asks "once it's done reply here" (frederick.stone@harmonygames.co/1844724419788800011) and the prompt asks for the reply; a draft is not a send (C18), so it does not deliver D3.
- Email the board as Robert asked (frederick.stone@harmonygames.co/1844623441920000059): not fair; the hub withdraws it ("Let's not, it goes in the deck.").
- Edit the deck f_a47d0e2c95b18f63e2c0d5: not asked; Leonard stitches the section in himself (hub frederick.stone@harmonygames.co/1844724419788800011).
- a16z Passed on the speedrun no (frederick.stone@harmonygames.co/1844748127814183717): not fair in rev4; the template says an accelerator decision is not a bridge answer and the interview (evt_e802a3583ee79ff6087f76) counts as a call, so In talks and no keep-warm item.

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
| D1 | Status · firms the platform review found forked in rev3 (settled in rev4) | Andreessen Horowitz In talks (template accelerator rule: program decision and feedback aren't a bridge answer; their bridge thread frederick.stone@harmonygames.co/1842277213140775733 has only "Will review"; interview evt_e802a3583ee79ff6087f76); Play Ventures Passed (C096HFA5Z8W/1758817200.730591); March Gaming Fund Passed (C096HFA5Z8W/1757365500.384216, frederick.stone@harmonygames.co/1842278301421016623); Mattel Not contacted this round (C096HFA5Z8W/1758927000.205874); General Catalyst, Triptyq, Turkven, Harlem Capital Awaiting reply (IH outreach C096HFA5Z8W/1757716998.377299 counts as ours); Treo VC, Superplay, BITKRAFT Ventures Awaiting reply (C096HFA5Z8W/1756942260.617302, f_48247af79428823c3cac92, C096HFA5Z8W/1758563861.649039); Initial Capital Awaiting reply (Leonard's Sep 9 LinkedIn outreach and their answer, C096HFA5Z8W/1757442000.492583) and [PERSON_NAME_5402] (row 69) Passed (Latest Status notes count as written, f_48247af79428823c3cac92); Transcend Fund, Acterra, Index Ventures Not contacted this round (plans and earlier-round answers don't count, f_3b9e61c04d7a52e8f1a6c2) | "Please use the buckets and definitions in the board pre-read template" | the template's bucket words | material (one value each) |
| D1 | Status · every other firm | solver/truth.json Status (one value per firm; list evidence f_48247af79428823c3cac92 and the cited threads); angels Anton Bernstein and Paul Heydon In talks (template: angels who said yes, C07C2866011/1758303600.418207); Kevin Lin, Mike Fischer, Demetri Detsaridis Not contacted this round | "Please use the buckets and definitions in the board pre-read template" | the template's bucket words | material |
| D1 | Committed · Anton Bernstein | 25,000: amount trimmed in frederick.stone@harmonygames.co/1844162278195200023, signed per frederick.stone@harmonygames.co/1844354293432320031 | "The money lines matter most" | 25000, 25,000, $25,000, $25K, 25k (USD) | material |
| D1 | Committed · Paul Heydon | none: no Completed notice; SAFE still unsigned per frederick.stone@harmonygames.co/1844610859008000037 | "The money lines matter most" | blank, 0, $0, a dash | material |
| D1 | Soft-circled · Paul Heydon | 50,000 (C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e) | "The money lines matter most" | 50000, 50,000, $50,000, $50K, 50k | material |
| D1 | Soft-circled · Anton Bernstein | none (signed, so committed): frederick.stone@harmonygames.co/1844354293432320031 | "The money lines matter most" | blank, 0, a dash | material |
| D1 | totals | committed 25,000; soft-circled 50,000 (solver/truth.json; template f_3b9e61c04d7a52e8f1a6c2 "Put the committed and soft-circled totals at the bottom of the sheet") | "The money lines matter most" | a totals row or labelled cells below the table; the numeric forms above | material |
| D1 | Build access · Dentsu Ventures | iOS only: TestFlight added, Play internal track not added (ZOM-567 comment lc_b549f3057640a5eb08f7581e overturns frederick.stone@harmonygames.co/1844294398771200045) | "Please use the buckets and definitions in the board pre-read template" | iOS only; TestFlight only; iOS yes, Android no | material |
| D1 | Build access · T-accelerate | iOS and Android (ZOM-567 comment lc_94eb35d962cfbdd31e1bd496) | "Please use the buckets and definitions in the board pre-read template" | both; iOS + Android; TestFlight and Play | material |
| D1 | Build access · other firms in talks | none: GFR Fund (frederick.stone@harmonygames.co/1843547312959065138), NCsoft (frederick.stone@harmonygames.co/1832208184829815962), Homa, Brightwater, Andreessen Horowitz (no ZOM-567 comment) | "Please use the buckets and definitions in the board pre-read template" | none, no, not on the tester list | material (not sampled) |
| D1 | Build access · firms not in talks, and angels | blank (template: "For firms in talks" and "Leave Build access blank for them", f_3b9e61c04d7a52e8f1a6c2) | — | blank, n/a, a dash | representational |
| D2 | checklist location and name | a checklist on card 68c5a49e8491a9d7faf869d0 named for keep-warm (rule 68c64270d660c977c4696986: "a Keep warm checklist on this card") | "Whatever the Existing Investor Update card says to do for firms that pass, do that too" | name Keep warm or a close variant; location fixed | location material; name representational |
| D2 | items | London Venture Partners, Sciplay, Hiro Capital (solver/truth.json keepwarm; calls evt_e59dc0a675d0c407b79acf, evt_7d3e19b04a6c25f8e1b9a0, Sciplay call evt_25c9ee60d4b6c8f6d39a74); exactly these three (calls this round, per the rev4 comment) | "Whatever the Existing Investor Update card says to do for firms that pass, do that too" | one item per firm; list spelling or obvious forms (LVP; SciPlay) | material |
| D3 | thread and recipients | a reply on frederick.stone@harmonygames.co/1844724419788800011 to leonard.hayes@harmonygames.co | "reply here with the numbers the fundraising slide needs" | reply or reply-all (adds robert@harmonygames.co, arthur.blake@harmonygames.co) | thread material; reply vs reply-all representational |
| D3 | contents | 79 firms ("every row, angels included"); committed $25,000; soft-circled $50,000 (card comment 68d81f30a6c94e2b7d05e1f4) | "The Board Deck card says which numbers the slide takes" | numeric forms as in D1; extra context (sheet link, a note on Dentsu's Android access) allowed | material |
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
| F10 tester ticket | Dentsu TestFlight only (added Sep 26; Play waits on Google account addresses); T-accelerate both, added Sep 22 | ZOM-567 (comments lc_b549f3057640a5eb08f7581e, lc_94eb35d962cfbdd31e1bd496) | YES (unscoped) | overturns F9 | agents prefer secondhand mail over Linear | No |
| F11 Sciplay phone pass | Robert's reply: Sciplay out (Sep 29) | C096HFA5Z8W/1759184040.552871 under C096HFA5Z8W/1757716998.377299 | YES (member) | overturns F12 (CORR) | channel history omits replies | No |
| F12 SciPlay thread | "We'll continue to play" (Sep 18) | frederick.stone@harmonygames.co/1842285743246816270 | YES (cc) | met first | reads as in talks | No |
| F13 unnamed-firm pass | thanks for Tuesday's session, pass on the bridge (Sep 26), no firm name | frederick.stone@harmonygames.co/1844318935449600041 | YES (cc) | overturns the list's "no response as of 09/11" for Hiro (ALIAS) | sender name does not ring a bell | No |
| F14 Edith Vane contact | Partner, Hiro Capital | e3a91c07d5b48f26a0c7e314 | YES (unscoped) | maps F13 to Hiro | — | No |
| F38 Ryo Ishikawa contact | Dentsu Ventures (games and AI investments), PERSON_5221_EMAIL | a4c2e9f07b31d85e6c0f1b29 | YES (unscoped) | ties the Sep 23 Dentsu call and tester mail to the Dentsu Ventures row (f_48247af79428823c3cac92) | the list partner is someone else | No |
| F15 Tuesday pitch call | Sep 23 call with Hiro's people | evt_7d3e19b04a6c25f8e1b9a0 | YES (own calendar) | makes Hiro a pass after a pitch (keep-warm) | summary carries person tokens, not the firm | No |
| F16 Brightwater call | Sep 25 call, off the list | evt_2f86b0d4c9e17a35b64e0d | YES (own calendar) | off-list firm (FILT) | the list read as the whole population | No |
| F17 Ilse Marrow contact | Principal, Brightwater Games Fund | b72f0d6e19c3a84e5d21f9a0 | YES (unscoped) | names the firm behind F16 | — | No |
| F18 Brightwater follow-up | follow-up Sep 25 and Ilse's reply Sep 26; not a pass | frederick.stone@harmonygames.co/1844276782694400053 | YES (cc) | not a pass, so In talks | — | No |
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
| F33 1AM Gaming note | 1AM Gaming is the March Gaming Fund row; they passed (Sep 8) | C096HFA5Z8W/1757365500.384216 | YES (member) | ties the 1AM no (frederick.stone@harmonygames.co/1842278301421016623) to the list row | the list still says March Gaming Fund | No |
| F34 Play Ventures correction | the Sep 15 no was their reply to Griffin; still their no (Sep 25) | C096HFA5Z8W/1758817200.730591 | YES (member) | overturns "they didn't respond" (C096HFA5Z8W/1758671737.632949) | agents stop at the Sep 23 post | No |
| F35 Mattel note | RFP and partnership only, not pitched the bridge (Sep 26) | C096HFA5Z8W/1758927000.205874 | YES (member) | overturns "Reached out to … Mattel" (C096HFA5Z8W/1756941551.539229) | partnership vs bridge outreach | No |
| F36 Treo VC post | Treo pinged Leonard on LinkedIn on Sep 3; deck and blurb sent | C096HFA5Z8W/1756942260.617302 | YES (member) | dates the Treo contact to the kickoff day (vs the Sep 2 warm-ups, C096HFA5Z8W/1756851039.800009) | spelled Treeo in the Sep 3 list | No |
| F37 Initial Capital post | Leonard pinged them on LinkedIn about the bridge; they won't lead, might write a small check (Sep 9) | C096HFA5Z8W/1757442000.492583 | YES (member) | backs the list's 09/11 note (f_48247af79428823c3cac92) with our outreach | no amount, so not soft-circled | No |

## 5a · Search-as-persona proof

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 hub ask | gmail | "board pre-read" | base 0; seeded 2 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844724419788800011 | YES (seeded; check-sql YES) |
| F2 Oct 14 template (July decoy beside it) | gdocs | "board pre-read" | base 0; seeded 2 | 0 | f_3b9e61c04d7a52e8f1a6c2 | YES (seeded; check-sql YES) |
| F3 2025 game investor list | gsheets | "Game Investor List" | base 2; seeded 0 | 2 | f_48247af79428823c3cac92 | YES (base, hit 2 of 2) |
| F4 angel post | slack | "Paul Heydon" | base 0; seeded 1 | n/a (--no-hidden) | C07C2866011/1758303600.418207 | YES (seeded; check-sql YES) |
| F5 angels sheet | gsheets | "Bridge angels" | base 0; seeded 1 | 0 | f_6e1d93a0c4b72f85d39a0e | YES (seeded; check-sql YES) |
| F6 Anton's amount mail | gmail | "Anton" | base 11; seeded 2 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844162278195200023 | YES (seeded; check-sql YES) |
| F7 DocuSign Completed (Anton) | gmail | "docusign" | base 2; seeded 2 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844354293432320031 | YES (seeded; check-sql YES) |
| F8 Paul's unsigned SAFE nudge | gmail | "Paul Heydon" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844610859008000037 | YES (seeded; check-sql YES) |
| F9 Dentsu tester invites thread | gmail | "PERSON_5221" | base 2; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844294398771200045 | YES (seeded; check-sql YES) |
| F10 tester ticket | linear | "tester" | base 2; seeded 1 | 0 | ZOM-567 | YES (seeded; unscoped) |
| F11 Sciplay phone pass | slack | "Sciplay" | base 6; seeded 1 | n/a (--no-hidden) | C096HFA5Z8W/1759184040.552871 | YES (seeded; check-sql YES) |
| F12 SciPlay mail thread | gmail | "SciPlay" | base 8; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842285743246816270 | YES (base, hit 6 of 8) |
| F13 unnamed-firm pass mail | gmail | "bridge" | base 29; seeded 2 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844318935449600041 | YES (seeded; check-sql YES) |
| F14 Edith Vane contact | contacts | "Edith" | base 0; seeded 1 | 0 | e3a91c07d5b48f26a0c7e314 | YES (seeded; unscoped) |
| F15 Tuesday pitch call | gcal | "Leonard Hayes" | base 10; seeded 2 | 70 | evt_7d3e19b04a6c25f8e1b9a0 | YES (seeded; check-sql YES) |
| F16 Brightwater call | gcal | "Leonard Hayes" | base 10; seeded 2 | 70 | evt_2f86b0d4c9e17a35b64e0d | YES (seeded; check-sql YES) |
| F17 Ilse Marrow contact | contacts | "Ilse" | base 0; seeded 1 | 0 | b72f0d6e19c3a84e5d21f9a0 | YES (seeded; unscoped) |
| F18 Brightwater follow-up | gmail | "Ilse" | base 0; seeded 2 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844276782694400053 | YES (seeded; check-sql YES) |
| F19 Homa invitation | gmail | "PERSON_5173_NAME" | base 3; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1843169166284025277 | YES (base, hit 2 of 3) |
| F20 Homa call | gcal | "Leonard Hayes" | base 10; seeded 2 | 70 | evt_89381fe5a15b802c5652a9 | YES (base, hit 5 of 10) |
| F21 keep-warm rule card | trello | "Existing Investor Update" | base 3; seeded 1 | 0 | 68c64270d660c977c4696986 | YES (seeded; unscoped) |
| F22 Board Deck card | trello | "Board Deck" | base 15; seeded 4 | 0 | 68d8193cf451863621c88a2a | YES (seeded; unscoped) |
| F23 draft board deck | gslides | "Oct 14" | base 1; seeded 1 | 1 | f_a47d0e2c95b18f63e2c0d5 | YES (seeded; check-sql YES) |
| F24 Board folder | gdrive | "Board - Oct 14 2025" | base 0; seeded 1 | 0 | d_5e8a1c3f9b07d2e64a1b93 | YES (seeded; check-sql YES) |
| F25 folder README | gdocs | "README" | base 0; seeded 1 | 0 | f_c61a0e93b7d24f58a2e917 | YES (seeded; check-sql YES) |
| F26 review event | gcal | "Board pre-read review" | base 0; seeded 1 | 0 | evt_9c41e7a2d05b38f6e1a7c4 | YES (seeded; check-sql YES) |
| F27 LVP pass | gmail | "LVP" | base 14; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842277743427687737 | YES (base, hit 12 of 14) |
| F28 T-accelerate recap | gmail | "T-accelerate" | base 2; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842283406259093714 | YES (base, hit 1 of 2) |
| F29 PXLite is T-accelerate | gmail | "PXLite" | base 1; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1843978997950200606 | YES (base, hit 1 of 1) |
| F30 Karthic contact | contacts | "Karthic" | base 0; seeded 1 | 0 | 5d0e8b31f7a29c64e1b0d3a8 | YES (seeded; unscoped) |
| F31 Robert's board mail | gmail | "pipeline" | base 43; seeded 3 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844623441920000059 | YES (seeded; check-sql YES) |
| F32 Arthur's aside | slack | "pipeline" | base 142; seeded 1 | n/a (--no-hidden) | C07C2866011/1759168800.117903 | YES (seeded; check-sql YES) |
| F33 1AM Gaming note | slack | "March Gaming" | base 2; seeded 1 | n/a (--no-hidden) | C096HFA5Z8W/1757365500.384216 | YES (seeded; check-sql YES) |
| F34 Play Ventures correction | slack | "Play Ventures" | base 15; seeded 1 | n/a (--no-hidden) | C096HFA5Z8W/1758817200.730591 | YES (seeded; check-sql YES) |
| F35 Mattel RFP note | slack | "Mattel" | base 14; seeded 1 | n/a (--no-hidden) | C096HFA5Z8W/1758927000.205874 | YES (seeded; check-sql YES) |
| F36 Treo VC post | slack | "Treo" | base 1; seeded 1 | n/a (--no-hidden) | C096HFA5Z8W/1756942260.617302 | YES (seeded; check-sql YES) |
| F37 Initial Capital post | slack | "Initial Capital" | base 23; seeded 1 | n/a (--no-hidden) | C096HFA5Z8W/1757442000.492583 | YES (seeded; check-sql YES) |
| F38 Ryo Ishikawa contact | contacts | "Ryo" | base 0; seeded 1 | 0 | a4c2e9f07b31d85e6c0f1b29 | YES (seeded; unscoped) |

The id column carries the deciding record; for base records the Found cell gives its rank in the pasted hit list (persona_view lists oldest first, so the newest thread sits last). `persona_view.py search` reads only the base export, so seeded rows return 0 there; the seeded count is a case-insensitive scan of the rev3 SQL rows Frederick can see (own mailbox and calendar copies, his two channels, files he owns or is shared on; Trello, Linear and Contacts unscoped), and seeded reach is the dossier's check-sql PASS for frederick_stone (§1.E). Queries are what Frederick would type after reading the hub and the records it leads to: the firm or person name from the list, the token name on a calendar invite, or the doc or card name the hub gives. No fact is NO, so nothing is routed.

```
SEARCH gmail 'board pre-read' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'board pre-read' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gsheets 'Game Investor List' as frederick_stone  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=2 (showing 2)  hidden by ACL=2 in 2 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_0b29566cd7932a205d54d2", "name": "Internal Game Investor List - harmonygames.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Internal Game Investor List - harmonygames"}
  {"id": "f_48247af79428823c3cac92", "name": "Game Investor List - Harmony Games 2025.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Game Investor List - Harmony Games 2025"}

SEARCH slack 'Paul Heydon' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gsheets 'Bridge angels' as frederick_stone  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'Anton' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=11 (showing 11)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1809389932183182202", "last": "2024-09-05T20:38:25Z", "subject": "Your meeting recap - [PERSON_NAME_0038] and Marcus Lee", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy     
  {"id": "frederick.stone@harmonygames.co/1809391207177817148", "last": "2024-09-05T20:58:42Z", "subject": "Welcome to Fireflies", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy                Policy   "}
  {"id": "frederick.stone@harmonygames.co/1809391521917194188", "last": "2024-09-05T21:03:42Z", "subject": "Review your Join and Recap settings", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy                Policy  
  {"id": "frederick.stone@harmonygames.co/1809662998060471574", "last": "2024-09-08T20:58:42Z", "subject": "Invite your teammates", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy                Policy   "}
  {"id": "frederick.stone@harmonygames.co/1809727332814641066", "last": "2024-09-09T14:01:14Z", "subject": "Weekly Digest: Highlights from Sep 02 - Sep 09, 2024", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy       
  {"id": "frederick.stone@harmonygames.co/1809844192113109011", "last": "2024-09-10T20:58:42Z", "subject": "Automate your meeting with our 40+ integrations", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy            
  {"id": "frederick.stone@harmonygames.co/1818996687213456078", "last": "2024-12-20T21:33:40Z", "subject": "Your Year in Meetings - See your 2024 Fireflies Recap!", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy     
  {"id": "frederick.stone@harmonygames.co/1821331961080453404", "last": "2025-01-15T16:11:52Z", "subject": "Subscribe to Fireflies - Get 20% OFF On All Plans", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy          
  {"id": "frederick.stone@harmonygames.co/1830298046074662096", "last": "2025-04-24T15:23:57Z", "subject": "New: Fireflies launches 200+ AI Apps  ✨", "snippet": "     Fireflies.ai • 5424 [LOCATION_25301] , Ste 10-531 Pleasanton, CA 94566                                      Privacy                Poli
  {"id": "frederick.stone@harmonygames.co/1837999467884131729", "last": "2025-07-30T15:55:41Z", "subject": "RE: q about LI", "snippet": "les Director  Stirista  777 [LOCATION_19704], Ste 225 – San Antonio TX 78258    On Fri, Jul 25, 2025 at 09:12 PM UTC PERSON_0701_NAME <PERSON_070"}
  {"id": "frederick.stone@harmonygames.co/1840501641217286806", "last": "2025-09-15T18:14:50Z", "subject": "Re: [SOURCE_ORG_0001] & Balancy", "snippet": "URL_26401]>**calendly: >> Book a call <https://calendly.com/antonina-belova-balancy/30min>* >> *Best practices for in-game shops:* *e-book* >> <h"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'docusign' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1809845423979628132", "last": "2024-09-19T18:50:59Z", "subject": "Re: Build Access", "snippet": "6], >>>>>>>>>>>>> >>>>>>>>>>>>> We’ve sent our contract via docusign to Leonard's email. >>>>>>>>>>>>> >>>>>>>>>>>>> Please also find the attached s"}
  {"id": "frederick.stone@harmonygames.co/1830890312657338682", "last": "2025-05-01T04:19:37Z", "subject": "Re: Board Follow-Up [SOURCE_ORG_0001]: Domino Delights Metrics, Runway Discipline, and 4X Proposal", "snippet": "re liability to the company. Please keep an eye out for the docusign request from
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Paul Heydon' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'PERSON_5221' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1843473831194478743", "last": "2025-09-25T17:47:49Z", "subject": "Re: Griffin AGM || Dentsu <> [SOURCE_ORG_0001]", "snippet": "L> > *CC: *小川 浩史 PERSON_2581_NAME <PERSON_2581_EMAIL>, 石川 遼 PERSON_5221_NAME < > PERSON_5221_EMAIL>, [PERSON_NAME_0055] <robert@harmo
  {"id": "frederick.stone@harmonygames.co/1844735562296076053", "last": "2025-10-01T00:02:03Z", "subject": "Invitation: 1:30pm PT || MEETING || [SOURCE_ORG_0001] & Dentsu  @ Wed Oct 1, 2025 1:30pm - 2:30pm (PDT) (null)", "snippet": "ts  PERSON_3040_EMAIL - organizer  Leonard Hayes - creator  PERSON_52
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH linear 'tester' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/1835/description", "parent_pointer": "/issues/1835", "encoding": "json", "text": "Basically a backend deletion of player progress so testers can restart 
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/2358/description", "parent_pointer": "/issues/2358", "encoding": "json", "text": "'@Leonard said:\n\n> mini-game sends redemption tile too late. It's bas

SEARCH slack 'Sciplay' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=6 (showing 6)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C07C2866011/1723747740.516839", "channel": "executives", "kind": "private", "date": "2024-08-15", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I know their game guy, [PERSON_NAME_0168] who is CBO at Sciplay - L&W is the parent company to Sciplay"}
  {"id": "C07C2866011/1757961584.722439", "channel": "executives", "kind": "private", "date": "2025-09-15", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "before sciplay meeting let’s chat"}
  {"id": "C096HFA5Z8W/1756941551.539229", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-03", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "n engine demo)     *  NCsoft (reached out to Taewon)     *  Sciplay  (sent)     *  Supercell (sent)"}
  {"id": "C096HFA5Z8W/1757345124.546449", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "demo) - [-] Scopely  (IH says they are not investing) - [-] Sciplay  (sent) - [-] DeNA ([PERSON_NAME_25643]) - [-] Supercell ([PER
  {"id": "C096HFA5Z8W/1757716998.377299", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "E_0205] reached out to GFR, Play, Dentsu, General Catalyst, Sciplay ([PERSON_NAME_2327] just responded), Triptyq, Turkven, Harlem 
  {"id": "D05S58U4SAK/1726530665.811559", "channel": "D05S58U4SAK", "kind": "im", "date": "2024-09-16", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "I'll look at SciPlay and DeNA"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'SciPlay' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=8 (showing 8)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1807564272588008283", "last": "2024-08-16T17:00:21Z", "subject": "Invitation: [SOURCE_ORG_0001] / [USERNAME_22751] meetup @ Wed Sep 18, 2024 5:30pm - 6:15pm (PDT) (null)", "snippet": "[SOURCE_ORG_0001] / SciPlay meetup  Wednesday Sep 18, 2024 ⋅ 5:30pm – 6:15pm
  {"id": "frederick.stone@harmonygames.co/1810571066290259796", "last": "2024-09-18T21:32:02Z", "subject": "Invitation: [SOURCE_ORG_0001] / [USERNAME_22751] meetup @ Wed Sep 18, 2024 5:30pm - 6:15pm (PDT) (null)", "snippet": "[SOURCE_ORG_0001] / SciPlay meetup  Wednesday Sep 18, 2024 ⋅ 5:30pm – 6:15pm
  {"id": "frederick.stone@harmonygames.co/1810640472319227972", "last": "2024-09-19T15:55:12Z", "subject": "Introducing Gamesforum San Francisco 2024!", "snippet": "   EA    [PERSON_NAME_18352]    Director of Monetization    SciPlay    [PERSON_NAME_18351]    Startup Advisor Director    [PERSON_NAME_48
  {"id": "frederick.stone@harmonygames.co/1825303525465937646", "last": "2025-02-28T12:17:51Z", "subject": "Inside Wargaming's live service strategy, Voodoo's new Match-3 game, and more", "snippet": "40_SJW2mTT5F77YCjWf2JSSgW04 )    💎 Monetization Psychology: SciPlay's Winning Formula    🎙️ [PERSON_NA
  {"id": "frederick.stone@harmonygames.co/1828941094985833485", "last": "2025-04-09T15:55:47Z", "subject": "How Block Blast! blew up, top mobile games March, streamer-first gameplay & more", "snippet": "n social Casino: [PERSON_NAME_29251] on What Still Works    SciPlay’s Director of Growth, [PERSON_N
  {"id": "frederick.stone@harmonygames.co/1842285743246816270", "last": "2025-09-18T05:24:09Z", "subject": "Re: Intro: [PERSON_NAME_2327], [PERSON_NAME_0307] ([USERNAME_22751]) <> Leonard ([SOURCE_ORG_0001])", "snippet": "ubject: *Re: Intro: [PERSON_NAME_2327], [PERSON_NAME_0307] (SciPlay) <> Leonard 
  {"id": "frederick.stone@harmonygames.co/1843356361309564467", "last": "2025-09-15T18:40:16Z", "subject": "Invitation: [USERNAME_22751] prep @ Mon Sep 15, 2025 1pm - 1:30pm (PDT) (frederick.stone@harmonygames.co)", "snippet": "SciPlay prep  Monday Sep 15, 2025 ⋅ 1pm – 1:30pm  Pacific Time - Los Angel
  {"id": "frederick.stone@harmonygames.co/1844686494022527554", "last": "2025-09-30T11:02:09Z", "subject": "Unlock new marketing possibilities with  Singular’s latest product, Extract", "snippet": "hed Extract, already being used by brands like Warner Bros, Sciplay, Electronic Arts, King and more!  Wi
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'bridge' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=29 (showing 15)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1809484409903875153", "last": "2025-09-03T20:49:42Z", "subject": "Re: Intro: Play ventures / [SOURCE_ORG_0001]", "snippet": " Ventures might consider participating in our next round, a bridge we are kicking off now.  We are kicking off a $2.5M bridge this week
  {"id": "frederick.stone@harmonygames.co/1810477387253322232", "last": "2024-09-17T20:43:14Z", "subject": "Discover the Unity Asset Store", "snippet": " out some of our most popular assets                 \"Troll Bridge Studios\"                 <https://app.response.unity3d.com/e/er?utm_campaign=Ot"
  {"id": "frederick.stone@harmonygames.co/1817054333766957655", "last": "2024-11-29T11:00:48Z", "subject": "Representation in mobile games, Q5 mobile marketing strategies, monetizing offline gameplay and more...", "snippet": " the mobile gaming industry, and Playgap is on a mission to bridge this gap.
  {"id": "frederick.stone@harmonygames.co/1821524935557007389", "last": "2025-01-17T19:17:31Z", "subject": "You're Invited: Griffin Annual GDC Party 2025", "snippet": "[A bridge with purple lights  Description automatically generated]    Take GDC to the nex"}
  {"id": "frederick.stone@harmonygames.co/1826238417183591703", "last": "2025-03-10T19:55:28Z", "subject": "Invitation reminder: [PERSON_NAME_2000]'s Annual GDC Party 2025", "snippet": "dc2025> to secure your spot.  We hope to see you There!  [A bridge with purple lights  Description automatically gen
  {"id": "frederick.stone@harmonygames.co/1827122265598686698", "last": "2025-03-20T14:06:15Z", "subject": "📬  Nvidia, xAI team up on AI infra", "snippet": "rge protests in Budapest, with thousands blocking a central bridge in defiance of police orders.  * Critics argue the law violates fundamental ri
  {"id": "frederick.stone@harmonygames.co/1829481668591425070", "last": "2025-04-15T15:07:44Z", "subject": "What’s missing in the future of tech? Maybe you.", "snippet": "ions. Where is the next leap in AI coming from? How will we bridge the gap between our physical and digital worlds? Who is shaping 
  {"id": "frederick.stone@harmonygames.co/1829745720683659211", "last": "2025-04-18T13:04:56Z", "subject": "reminder: What’s missing in the future of tech? Maybe you.", "snippet": "ions. Where is the next leap in AI coming from? How will we bridge the gap between our physical and digital worlds? Who i
  {"id": "frederick.stone@harmonygames.co/1832205523949751837", "last": "2025-05-15T16:42:28Z", "subject": "The Monday Salad / Friday Burger Paradox (and why it's killing your marketing)", "snippet": " behavior pattern to another?  - Identify the psychological bridges between seemingly contradictory b
  {"id": "frederick.stone@harmonygames.co/1832208184829815962", "last": "2025-09-30T16:24:09Z", "subject": "Re: Leonard Hayes - 45min @ Wed, May 14, 2025 8:00pm – 8:45pm (GMT-07)", "snippet": "’m reaching out to let you know we’re kicking off > a $2.5M bridge round this week and wanted to share the de
  {"id": "frederick.stone@harmonygames.co/1833543266751907040", "last": "2025-05-30T11:05:15Z", "subject": "Press Play - Why Every Company Needs a Gaming Strategy | Book reveal", "snippet": "r touch point of our time. And to empower *you* to build a  bridge between games and organizations entering thi
  {"id": "frederick.stone@harmonygames.co/1834085120985001817", "last": "2025-06-05T10:37:53Z", "subject": "Your Invitation to AppCamp Boston  – GamePro’s Evolution", "snippet": ". 🎉 What’s in store:🏨 2 nights at Hyatt Regency Boston / CambridgeAugust 6: Welcome Dinner & Casual Networking convivialAug
  {"id": "frederick.stone@harmonygames.co/1837914783244638008", "last": "2025-07-17T17:08:32Z", "subject": "Request to Restructure Payment Plan for Upcoming Renewal", "snippet": "together—this adjustment would go a long way in helping us  bridge to our next funding milestone.    Let me know what’s pos
  {"id": "frederick.stone@harmonygames.co/1839181819558457100", "last": "2025-07-31T16:47:44Z", "subject": "How the first [PERSON_NAME_21249] fans can help us find invisible customers", "snippet": "peal to the specific motivations of your target audience  - Bridge to mainstream psycholo[USERNAME_13301
  {"id": "frederick.stone@harmonygames.co/1841636073974841484", "last": "2025-08-27T21:49:52Z", "subject": "Re: [SOURCE_ORG_0001] engagement Letter Material", "snippet": " put and await further >>> instructions as you seek out the bridge deal. >>> >>> Let us know! >>> >>> Best, >>> PERSON_2694_NAME >>
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH contacts 'Edith' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gcal 'Leonard Hayes' as frederick_stone  scope: GCal event summary (base events carry no description/location)
visible hits=10 (showing 10)  hidden by ACL=70 in 5 containers  UNVERIFIED=0 in 0 containers
  {"id": "evt_2b7efb58cdbd7f4ebe59e6", "calendar": "frederick.stone@harmonygames.co", "start": "2024-09-05T17:30:00Z", "summary": "Leonard Hayes / [PERSON_NAME_45370] | PvX Partners", "status": "confirmed"}
  {"id": "evt_6bd5a4dd9f65d20b97f75c", "calendar": "frederick.stone@harmonygames.co", "start": "2025-03-04T16:00:00Z", "summary": "[USERNAME_36301] & Harmony Games Intro and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_9e7a36e1ae703415a058ee", "calendar": "frederick.stone@harmonygames.co", "start": "2025-03-31T17:30:00Z", "summary": "[PERSON_NAME_0307] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_72074f1bcb7ff5e3da6149", "calendar": "frederick.stone@harmonygames.co", "start": "2025-08-20T18:30:00Z", "summary": "[PERSON_NAME_17220] Steudler and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_89381fe5a15b802c5652a9", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-18T15:00:00Z", "summary": "PERSON_5173_NAME ([PERSON_NAME_0854]) and Leonard Hayes ([SOURCE_ORG_0001])", "status": "confirmed"}
  {"id": "evt_7934d6c78f843013d5d676", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-19T15:00:00Z", "summary": "[PERSON_NAME_25254] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_be57cd7ca86d925fb5900c", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-22T15:00:00Z", "summary": "PERSON_3242_NAME and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_b7af120af94383d8f0781b", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-24T00:30:00Z", "summary": "[PERSON_NAME_35100] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_38bdf82a0d337c4d82695e", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-29T20:30:00Z", "summary": "Leonard Hayes (Harmony Games) and PERSON_0787_NAME", "status": "cancelled"}
  {"id": "evt_2204ffea306847eea6e5b0", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-30T17:30:00Z", "summary": "Leonard Hayes and PERSON_0787_NAME", "status": "confirmed"}
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH gcal 'Leonard Hayes' as frederick_stone  scope: GCal event summary (base events carry no description/location)
visible hits=10 (showing 10)  hidden by ACL=70 in 5 containers  UNVERIFIED=0 in 0 containers
  {"id": "evt_2b7efb58cdbd7f4ebe59e6", "calendar": "frederick.stone@harmonygames.co", "start": "2024-09-05T17:30:00Z", "summary": "Leonard Hayes / [PERSON_NAME_45370] | PvX Partners", "status": "confirmed"}
  {"id": "evt_6bd5a4dd9f65d20b97f75c", "calendar": "frederick.stone@harmonygames.co", "start": "2025-03-04T16:00:00Z", "summary": "[USERNAME_36301] & Harmony Games Intro and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_9e7a36e1ae703415a058ee", "calendar": "frederick.stone@harmonygames.co", "start": "2025-03-31T17:30:00Z", "summary": "[PERSON_NAME_0307] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_72074f1bcb7ff5e3da6149", "calendar": "frederick.stone@harmonygames.co", "start": "2025-08-20T18:30:00Z", "summary": "[PERSON_NAME_17220] Steudler and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_89381fe5a15b802c5652a9", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-18T15:00:00Z", "summary": "PERSON_5173_NAME ([PERSON_NAME_0854]) and Leonard Hayes ([SOURCE_ORG_0001])", "status": "confirmed"}
  {"id": "evt_7934d6c78f843013d5d676", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-19T15:00:00Z", "summary": "[PERSON_NAME_25254] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_be57cd7ca86d925fb5900c", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-22T15:00:00Z", "summary": "PERSON_3242_NAME and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_b7af120af94383d8f0781b", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-24T00:30:00Z", "summary": "[PERSON_NAME_35100] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_38bdf82a0d337c4d82695e", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-29T20:30:00Z", "summary": "Leonard Hayes (Harmony Games) and PERSON_0787_NAME", "status": "cancelled"}
  {"id": "evt_2204ffea306847eea6e5b0", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-30T17:30:00Z", "summary": "Leonard Hayes and PERSON_0787_NAME", "status": "confirmed"}
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH contacts 'Ilse' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'Ilse' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'PERSON_5173_NAME' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1843169143565072339", "last": "2025-09-13T17:04:32Z", "subject": "Invitation: PERSON_5173_NAME and Leonard Hayes @ Thu Sep 18, 2025 8am - 8:45am (PDT) (frederick.stone@harmonygames.co)", "snippet": "Invitation: PERSON_5173_NAME and Leonard Hayes @ Thu Sep 18, 
  {"id": "frederick.stone@harmonygames.co/1843169166284025277", "last": "2025-09-13T17:04:53Z", "subject": "Updated invitation: PERSON_5173_NAME ([PERSON_NAME_0854]) and Leonard Hayes ([SOURCE_ORG_0001]) @ Thu Sep 18, 2025 8am - 8:45am (PDT) (frederick.stone@harmonygames.co)", "snippet": "Updated invi
  {"id": "frederick.stone@harmonygames.co/1843552279434086285", "last": "2025-09-26T17:28:51Z", "subject": "Re: Accepted: PERSON_5173_NAME and Leonard Hayes @ Thu Sep 18, 2025 8am - 8:45am (PDT) (leonard.hayes@harmonygames.co)", "snippet": "Re: Accepted: PERSON_5173_NAME and Leonard Hayes @ Thu Sep 18
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gcal 'Leonard Hayes' as frederick_stone  scope: GCal event summary (base events carry no description/location)
visible hits=10 (showing 10)  hidden by ACL=70 in 5 containers  UNVERIFIED=0 in 0 containers
  {"id": "evt_2b7efb58cdbd7f4ebe59e6", "calendar": "frederick.stone@harmonygames.co", "start": "2024-09-05T17:30:00Z", "summary": "Leonard Hayes / [PERSON_NAME_45370] | PvX Partners", "status": "confirmed"}
  {"id": "evt_6bd5a4dd9f65d20b97f75c", "calendar": "frederick.stone@harmonygames.co", "start": "2025-03-04T16:00:00Z", "summary": "[USERNAME_36301] & Harmony Games Intro and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_9e7a36e1ae703415a058ee", "calendar": "frederick.stone@harmonygames.co", "start": "2025-03-31T17:30:00Z", "summary": "[PERSON_NAME_0307] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_72074f1bcb7ff5e3da6149", "calendar": "frederick.stone@harmonygames.co", "start": "2025-08-20T18:30:00Z", "summary": "[PERSON_NAME_17220] Steudler and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_89381fe5a15b802c5652a9", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-18T15:00:00Z", "summary": "PERSON_5173_NAME ([PERSON_NAME_0854]) and Leonard Hayes ([SOURCE_ORG_0001])", "status": "confirmed"}
  {"id": "evt_7934d6c78f843013d5d676", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-19T15:00:00Z", "summary": "[PERSON_NAME_25254] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_be57cd7ca86d925fb5900c", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-22T15:00:00Z", "summary": "PERSON_3242_NAME and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_b7af120af94383d8f0781b", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-24T00:30:00Z", "summary": "[PERSON_NAME_35100] and Leonard Hayes", "status": "confirmed"}
  {"id": "evt_38bdf82a0d337c4d82695e", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-29T20:30:00Z", "summary": "Leonard Hayes (Harmony Games) and PERSON_0787_NAME", "status": "cancelled"}
  {"id": "evt_2204ffea306847eea6e5b0", "calendar": "frederick.stone@harmonygames.co", "start": "2025-09-30T17:30:00Z", "summary": "Leonard Hayes and PERSON_0787_NAME", "status": "confirmed"}
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH trello 'Existing Investor Update' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/801/name", "parent_pointer": "/cards/801", "encoding": "json", "text": "Existing Investor Update", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5221/data/card/name", "parent_pointer": "/actions/5221/data/card", "encoding": "json", "text": "Existing Investor Update", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5222/data/card/name", "parent_pointer": "/actions/5222/data/card", "encoding": "json", "text": "Existing Investor Update", "truncated": false}

SEARCH trello 'Board Deck' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=15 (showing 15)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/454/name", "parent_pointer": "/cards/454", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/564/name", "parent_pointer": "/cards/564", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/682/name", "parent_pointer": "/cards/682", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/2812/data/card/name", "parent_pointer": "/actions/2812/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/2813/data/card/name", "parent_pointer": "/actions/2813/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/3030/data/card/name", "parent_pointer": "/actions/3030/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/3031/data/card/name", "parent_pointer": "/actions/3031/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/3545/data/card/name", "parent_pointer": "/actions/3545/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/3842/data/card/name", "parent_pointer": "/actions/3842/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/3843/data/card/name", "parent_pointer": "/actions/3843/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/4456/data/card/name", "parent_pointer": "/actions/4456/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/4457/data/card/name", "parent_pointer": "/actions/4457/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/4464/data/card/name", "parent_pointer": "/actions/4464/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/4466/data/card/name", "parent_pointer": "/actions/4466/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/4467/data/card/name", "parent_pointer": "/actions/4467/data/card", "encoding": "json", "text": "Board Deck", "truncated": false}

SEARCH gslides 'Oct 14' as frederick_stone  scope: GSlides title + page element text
visible hits=1 (showing 1)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_d957ed0b9cefdea3736714", "name": "Harmony Games BoD Oct 17 2024", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Australia,  Argentina, and El Salvador since Oct 14th"}

SEARCH gdrive 'Board - Oct 14 2025' as frederick_stone  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'README' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gcal 'Board pre-read review' as frederick_stone  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH gmail 'LVP' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=14 (showing 14)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1809476261712760035", "last": "2024-09-10T23:36:44Z", "subject": "Re: [SOURCE_ORG_0001]​ x CRAFTSMAN+", "snippet": "jqjSMW5mrYwC7bvyWYW6Qh8x34h0Cq0W8thr9d5phsKYW6Rr9X062PpH8W1RlvPV8HTPb4W43ZJjp5FrV-bVzlM0f52Wz6BW99MBsf8VW1gmV9yCYk7kM_gyW20JQh-7-t0F1VLQH1d73Np"
  {"id": "frederick.stone@harmonygames.co/1814174568226891254", "last": "2024-10-28T16:07:55Z", "subject": "AirPods Pro 2. Now with a clinical-grade Hearing Aid feature.", "snippet": "MoGY5NxgScrsEWjJQKbf6KbDXHXroMXmzT%2FzXcVzIcMIvODFkx9evI5I2TLVpkDaLc%2F%2BNVTR0n1XLO0%3D  1-800-MY-Apple  Get the Appl
  {"id": "frederick.stone@harmonygames.co/1817248365954223894", "last": "2024-12-01T14:24:39Z", "subject": "🛍️ Final days to get an Apple Gift Card.", "snippet": "Dq9fC7uTwSRPF6kHL9XDj6shaJZcSyMSBi6PB27xK7vHpc0SeSX8facUQvFtlvpX7UWDXPTAnQ%3D%3D    https://c.Apple.com/r?v=2&a=1zIdgxRYc2DtYV9mVx1rKVlLY4S
  {"id": "frederick.stone@harmonygames.co/1817349125701149395", "last": "2024-12-02T17:06:24Z", "subject": "AWS re:Invent is underway! Register now for the free livestream", "snippet": "tps://email.awscloud.com/MTEyLVRaTS03NjYAAAGXJvBTqgyqeLp8LwgLVP4pqBnAi6DvTsdTiDA9DFpp1sLxrKC49SI0ebQcE-hFdm1MWBHyWUY
  {"id": "frederick.stone@harmonygames.co/1821493746550976905", "last": "2025-01-17T11:03:22Z", "subject": "Cracking [USERNAME_43801]'s success, AdMob's strategy shift, monetizing puzzle games & more", "snippet": "d4C8mSckGW65vNBk1D_nBfW2C34XL1027P4W63bhwp5VVn-dW50wh3772cN2lVpH6Xh84mZv5W5WMYrM1fM112VB
  {"id": "frederick.stone@harmonygames.co/1828941094985833485", "last": "2025-04-09T15:55:47Z", "subject": "How Block Blast! blew up, top mobile games March, streamer-first gameplay & more", "snippet": "821DqYPGW5c2fnV7Gng27VdqSKH1V52pSN4kRx6jjrqlJW7fZmw11t2yxBW4Lvpd43rw-0cW7vk-9V3F5qCVW3rLNF23MN7P4W4
  {"id": "frederick.stone@harmonygames.co/1829577486716221939", "last": "2025-04-16T16:30:58Z", "subject": "Unlock personalized insights with helpful tips", "snippet": "FmN10oAYlOjJFTmWSncoL90RV8md2n76yp4L_YNbi4T3oPQv7-Z1q1fDbXUslvp3dukCpLev6Ywfb5sud4kBKk1Tpirg3r-7U8ImkNsO1q79M-t5G2G9HX5DnXl0v09fCNhNF
  {"id": "frederick.stone@harmonygames.co/1831746191415385019", "last": "2025-05-10T15:01:33Z", "subject": "Your first snap = 500 bonus points! 📸", "snippet": "367uagbEbziOEfVdBu_8T_Bya_ZXB8KzGNyP1BAZtLHvLeUCG5ofiDVLqzmolVpEqMsQVxMyXhuD7mnNjsCEgnCaKOm2DHpyrseTeU3TGf-HGlwJBeF48je5-s7pucHjMYg862JZey_-Sx
  {"id": "frederick.stone@harmonygames.co/1835195310878299059", "last": "2025-06-17T16:43:53Z", "subject": "Why Starbucks customers pay 3x more (it's not the coffee)", "snippet": "_7BnW2MGkgK1Qy6-TW21rltN1-YV2YW2B2nvS2RRtgmW2CKBwR3_SHvsW1L8LvP32HZTMW2TJ9Z32YLgWTW4cjH8b21q10WW41ydGq2WjcBxW2KBmxh2vCxC_W
  {"id": "frederick.stone@harmonygames.co/1839165922292088225", "last": "2025-07-31T12:35:02Z", "subject": "AI vs. Ad Managers: Who Wins?", "snippet": "Fdt3R17bTNsVf60ZH8lyYGmN4w4jPtpFghfW4P3DrK1NXX4PW7bdrDP9hcXslVp_nyg5j25zYN14hx9xTWRwgW3TLN578t2KM3VlhWf_8zDDnzW2GR0G126yR4XW6WSM1v5plRRVW5F1D20"}
  {"id": "frederick.stone@harmonygames.co/1841691265035833180", "last": "2025-08-28T09:34:18Z", "subject": "Gamesforum’s new Ad Quality Report is out now!", "snippet": "MN2jvW85VV1557zRzZW7GydsC3LfB21W8MnTjr8XrDYWW1rg2bw81319_VX7lVp5LJ9f4W2N_TzW1X219xW1dQYTh7MlLJcW5zxHqr4RB6dzW3NZVrF7JwXZ1N6Z9x9BzwrWP
  {"id": "frederick.stone@harmonygames.co/1842277743427687737", "last": "2025-09-26T22:16:23Z", "subject": "Re: re-intros: Are (LVP) <> Leonard & [PERSON_NAME_0054] ([SOURCE_ORG_0001])", "snippet": "Re: re-intros: Are (LVP) <> Leonard & [PERSON_NAME_0054] ([SOURCE_ORG_0001])"}
  {"id": "frederick.stone@harmonygames.co/1842473488814293664", "last": "2025-09-06T00:47:24Z", "subject": "Invitation: [USERNAME_32507] <> [SOURCE_ORG_0001] Catch Up @ Tue Sep 9, 2025 9:30am - 10:15am (PDT) (frederick.stone@harmonygames.co)", "snippet": "LVP <> [SOURCE_ORG_0001] Catch Up  Tuesday Sep
  {"id": "frederick.stone@harmonygames.co/1844252706319525839", "last": "2025-09-25T16:07:17Z", "subject": "If they did it, you can too.", "snippet": "FF5ffW39tVZD50yYchW298KhV2jmRKfVVm9Gv5wz_KwW7Zw6my8HB4B-W6fclVP2h4BFwVLLD5_2sq9hfW1PdcfT71gfjlW14_skP5844PCMYZTvNZ3HWqW7qfPTY7fGRrhW8kYsZl1T3yP"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'T-accelerate' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1842283406259093714", "last": "2025-09-22T17:40:07Z", "subject": "Re: Bridge Round for [SOURCE_ORG_0001]?", "snippet": "d multiple shots on goal. >>>>>> >>>>>> If this aligns with T-Accelerate’s investment thesis, could we please >>>>>> book  30–45 minutes thi
  {"id": "frederick.stone@harmonygames.co/1843625920612854647", "last": "2025-09-18T18:04:49Z", "subject": "Invitation: PERSON_3242_NAME and Leonard Hayes @ Mon Sep 22, 2025 8am - 8:45am (PDT) (frederick.stone@harmonygames.co)", "snippet": "or our meeting.: Hi Leonard -    PERSON_3242_NAME here from T
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'PXLite' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1843978997950200606", "last": "2025-09-22T15:36:49Z", "subject": "11 action items for Leonard Hayes and 3 others — PERSON_3242_NAME and Leonard Hayes", "snippet": "miting US headcount to 20-25%.  2. Investment Overview from PXLite\t• PXLite is a $100 million g
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH contacts 'Karthic' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'pipeline' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=43 (showing 15)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1809484409903875153", "last": "2025-09-03T20:49:42Z", "subject": "Re: Intro: Play ventures / [SOURCE_ORG_0001]", "snippet": "n 2 months. We are conquering the >>>>>>    AI-assisted art pipeline and extending our game features next. >>>>>>    - Our puzzles are 
  {"id": "frederick.stone@harmonygames.co/1810064290716490449", "last": "2024-09-23T17:34:46Z", "subject": "Re: [SOURCE_ORG_0001] <> Glints | Southeast Asia Hiring Partner", "snippet": "recap, our solutions will bring you:    1.  **Bigger Hiring Pipeline:** Access our database of 7 Million+ interview-
  {"id": "frederick.stone@harmonygames.co/1811914315041191539", "last": "2024-10-03T17:22:31Z", "subject": "Maximize rendering performance in Unity 6", "snippet": "                    \"Transitioning from the Built-in Render Pipeline to URP and HDRP\"                   \"Transitioning from the Built-i
  {"id": "frederick.stone@harmonygames.co/1813639111112794681", "last": "2024-10-22T18:17:18Z", "subject": "5 AI Sales resources", "snippet": "g has never been more challenging. Between managing endless pipelines and keeping track of leads, it’s easy to feel overwhelmed. You know how it goe"}
  {"id": "frederick.stone@harmonygames.co/1820871278850288809", "last": "2025-01-13T15:10:02Z", "subject": "Re: re: ROI on organic (model to calculate)", "snippet": "ily on paid ads due to the inability to generate an organic pipeline (despite traffic and clicks). Are you experiencing a similar challe
  {"id": "frederick.stone@harmonygames.co/1821779884748950677", "last": "2025-01-24T15:36:33Z", "subject": "Re: re: AI SEO trends + high Ad spend", "snippet": "> [PERSON_NAME_0036] - haven't heard from you ; re: organic pipeline this year >  > Figured it might not be ideal timing, so I put together so
  {"id": "frederick.stone@harmonygames.co/1823097598630534987", "last": "2025-02-14T14:13:58Z", "subject": "Re: [SOURCE_ORG_0001] <> GRx Intro Placeholder", "snippet": "r alpha, our puzzle engine, and our 3D map >>>>>>>>>>>>>    pipeline that will help us to scale fast if There is a good product-marke
  {"id": "frederick.stone@harmonygames.co/1824342693530743825", "last": "2025-02-17T21:46:07Z", "subject": "List of accounts", "snippet": "time with hyper-relevant messaging - significantly boosting pipeline and helping your sales team close more deals faster.      We are currently offe"}
  {"id": "frederick.stone@harmonygames.co/1826324158384019449", "last": "2025-03-17T14:58:10Z", "subject": "RE: [SOURCE_ORG_0001] - book more meetings", "snippet": "y at [SOURCE_ORG_0001] approaches, I know you want to scale pipelines with qualified leads.Have you worked with an appointment-setting ag
  {"id": "frederick.stone@harmonygames.co/1826924075454405596", "last": "2025-03-18T09:36:06Z", "subject": "📬  PepsiCo eyes Poppi acquisition", "snippet": "the tools and frameworks you need to predictably [grow your pipeline and revenue](https://www.growthforum.io/book#memo). Harness the enduring powe
  {"id": "frederick.stone@harmonygames.co/1827028350689271157", "last": "2025-03-24T13:10:33Z", "subject": "Re: re: next funding round + conversions", "snippet": "n rate? >  > We helped another gaming Seed startup 3x their pipeline. Their marketing budget stayed the same. >  > We just redesigned core 
  {"id": "frederick.stone@harmonygames.co/1827122265598686698", "last": "2025-03-20T14:06:15Z", "subject": "📬  Nvidia, xAI team up on AI infra", "snippet": " the tools and frameworks you need to predictably grow your pipeline and revenue. Harness the enduring power of human connection in sales and [di
  {"id": "frederick.stone@harmonygames.co/1827475205036627307", "last": "2025-03-24T11:36:06Z", "subject": "📬  OpenAI & meta's Indian AI deal", "snippet": " the tools and frameworks you need to predictably grow your pipeline and revenue.   Harness the enduring power of [human connection in sales](http
  {"id": "frederick.stone@harmonygames.co/1827565786251982122", "last": "2025-03-25T11:35:51Z", "subject": "📬  CEO exits as 23andMe collapses", "snippet": "the tools and frameworks you need to predictably [grow your pipeline and revenue](https://www.growthforum.io/book#memo). Harness the enduring powe
  {"id": "frederick.stone@harmonygames.co/1828937634156988355", "last": "2025-04-09T15:00:46Z", "subject": "[PERSON_NAME_0036] - thoughts?", "snippet": "gle with chasing referrals and occasional leads to fill the pipeline? I know how stressful and unpredictable that can be, especially when growth is "
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'pipeline' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=142 (showing 15)  hidden by ACL=None in 0 containers  UNVERIFIED=116 in 8 containers
  {"id": "C04S28HSD0U/1682879174.519739", "channel": "product", "kind": "private", "date": "2023-04-30", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "You need to show me the pipeline to visualize the pieces so you don’t become a bottleneck lol "}
  {"id": "C04UM32UWKD/1684522534.319499", "channel": "investors", "kind": "private", "date": "2023-05-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Z, [PERSON_NAME_6608], London Venture Partners - all in our pipeline Intros: 1Up Ventures, Signia, <http://backed.vc|backed.vc>, Gala
  {"id": "C04UM32UWKD/1684522654.490539", "channel": "investors", "kind": "private", "date": "2023-05-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "N GAMING PARTNERS, Index Ventures - all big ones are in our pipeline Benchmark, Accel Partners, Early Bird, Moon Fire, 20VCs, Felix V
  {"id": "C04UM32UWKD/1684793629.093439", "channel": "investors", "kind": "private", "date": "2023-05-22", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "of seven in 2 months. We are conquering the AI-assisted art pipeline and extending our game features next. • Our puzzles are to help 
  {"id": "C04UM32UWKD/1684872504.661499", "channel": "investors", "kind": "private", "date": "2023-05-23", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "of seven in 2 months. We are conquering the AI-assisted art pipeline and extending our game features next. • Our puzzles are to help 
  {"id": "C04UM32UWKD/1685641364.061269", "channel": "investors", "kind": "private", "date": "2023-06-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "dreambooth to train our model and accelerate our production pipeline quite a bit.  That said, I believe developing AI tools will stil
  {"id": "C04UM32UWKD/1685641822.900769", "channel": "investors", "kind": "private", "date": "2023-06-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "dreambooth to train our model and accelerate our production pipeline quite a bit.   That said, I believe developing AI tools will sti
  {"id": "C04UM32UWKD/1685722380.835579", "channel": "investors", "kind": "private", "date": "2023-06-02", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "of seven in 2 months. We are conquering the AI-assisted art pipeline and extending our game features next. • Our puzzles are to help 
  {"id": "C04UM32UWKD/1697203479.129379", "channel": "investors", "kind": "private", "date": "2023-10-13", "user": "EMPLOYEE_0025_SLACK_ID", "reply": true, "snippet": "PuzzlePipelineUpdate.mp4"}
  {"id": "C04V7N09LE7/1684234867.342579", "channel": "god-gameart", "kind": "private", "date": "2023-05-16", "user": "EMPLOYEE_0030_SLACK_ID", "reply": false, "snippet": "3, The idea is to define the art style, also to set up a pipeline for further developing"}
  {"id": "C04V7N09LE7/1690998818.271329", "channel": "god-gameart", "kind": "private", "date": "2023-08-02", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " manage their work and ensure that There are no gaps in the pipeline, with one artist working on concepts while the others work on 
  {"id": "C050WGU41HR/1687365406.507559", "channel": "engineering-bots", "kind": "private", "date": "2023-06-21", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "nk I'm ready to walk you through what we have on the puzzle pipeline. I'm going to start working from linear task list again. 
  {"id": "C050WGU41HR/1687803648.402869", "channel": "engineering-bots", "kind": "private", "date": "2023-06-26", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "/harmonygames-Games/GameOfDominoes/pull/29|#29 Blake/puzzle pipeline>"}
  {"id": "C050WGU41HR/1687896653.525589", "channel": "engineering-bots", "kind": "private", "date": "2023-06-27", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Did I download a wrong build of puzzle pipeline tool?"}
  {"id": "C050WGU41HR/1687967211.665989", "channel": "engineering-bots", "kind": "private", "date": "2023-06-28", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "btw is There a new build for the puzzle pipeline?"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'March Gaming' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UM32UWKD/1683784577.545179", "channel": "investors", "kind": "private", "date": "2023-05-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "nteractive, Hiro Capital, Lakestar Ventures, Lego Ventures, March Gaming Fund  *Akin:* Play Ventures, Bitkraft Ventures, Makers Fund,
  {"id": "C04UM32UWKD/1684522534.319499", "channel": "investors", "kind": "private", "date": "2023-05-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "nteractive, Hiro Capital, Lakestar Ventures, Lego Ventures, March Gaming Fund - Lego and Signia don’t fit, we are only missing 1UP fr
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Play Ventures' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=15 (showing 15)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UM32UWKD/1683674842.408569", "channel": "investors", "kind": "private", "date": "2023-05-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Matthew’s email to [PERSON_NAME_2000] / makers / index / play ventures"}
  {"id": "C04UM32UWKD/1683784577.545179", "channel": "investors", "kind": "private", "date": "2023-05-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "akestar Ventures, Lego Ventures, March Gaming Fund  *Akin:* Play Ventures, Bitkraft Ventures, Makers Fund, GRIFFIN GAMING PARTNERS, B
  {"id": "C04UM32UWKD/1684182752.356749", "channel": "investors", "kind": "private", "date": "2023-05-15", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": ", Signia, <http://backed.vc|backed.vc>, Galaxy Interactive, Play Ventures, Bitkraft Ventures, Makers Fund, , Benchmark, Accel Partner
  {"id": "C04UM32UWKD/1684344556.603969", "channel": "investors", "kind": "private", "date": "2023-05-17", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "/17), [PERSON_NAME_44950], general catalyst, march capital, Play Ventures, Makers Fund Who is out: Lego Ventures (only do growth), Si
  {"id": "C04UM32UWKD/1684438325.238879", "channel": "investors", "kind": "private", "date": "2023-05-18", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "al Catalyst: Jun 1, Thu 12pm March Capital: May 25, Thu 2pm Play Ventures: May 23, Tue 9:30am Makers Fund: May 24, Wed 5:45pm [PERSON
  {"id": "C04UM32UWKD/1684522654.490539", "channel": "investors", "kind": "private", "date": "2023-05-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "*Matthew:* Play Ventures, Makers Fund, GRIFFIN GAMING PARTNERS, Index Ventures - all big ones are in our"}
  {"id": "C04UM32UWKD/1684796121.273339", "channel": "investors", "kind": "private", "date": "2023-05-22", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "last thing to do today is play ventures research"}
  {"id": "C04UM32UWKD/1684796175.203699", "channel": "investors", "kind": "private", "date": "2023-05-22", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "order of research: play ventures - LVP - A16Z - [USERNAME_20339]"}
  {"id": "C04UM32UWKD/1684864662.144209", "channel": "investors", "kind": "private", "date": "2023-05-23", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "that’s awesome to hear and make me feel closer to play ventures if they write a check"}
  {"id": "C04UM32UWKD/1684872504.661499", "channel": "investors", "kind": "private", "date": "2023-05-23", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "g time with us this morning. We enjoyed learning more about Play Ventures and are super excited about getting a chance to work togeth
  {"id": "C04UM32UWKD/1685477229.770519", "channel": "investors", "kind": "private", "date": "2023-05-30", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Play Ventures is right"}
  {"id": "C07C2866011/1752097641.641769", "channel": "executives", "kind": "private", "date": "2025-07-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "tures led the round, with participation from a16z Speedrun, Play Ventures, e2vc, and APY Ventures.  :jigsaw: Founded by [PERSON_NAME
  {"id": "C096HFA5Z8W/1756941551.539229", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-03", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "st news on reachouts.  Reached out to •⁠  ⁠A16Z (sent) •⁠  ⁠Play Ventures (sent) •⁠  ⁠LVP (sent) •⁠  ⁠Makers Fund (sent) •⁠  ⁠Iamg
  {"id": "C096HFA5Z8W/1757345124.546449", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "- [-] A16Z (responded back to us, they are reviewing) - [-] Play Ventures (sent, no updates) - [-] LVP (sent, meeting on Sep 9th) 
  {"id": "C096HFA5Z8W/1758760220.012339", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-25", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Play Ventures"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Mattel' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=14 (showing 14)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C07C2866011/1727743223.548439", "channel": "executives", "kind": "private", "date": "2024-10-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Same goes for Mattel "}
  {"id": "C07C2866011/1727798831.776569", "channel": "executives", "kind": "private", "date": "2024-10-01", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "<https://corporate.Mattel.com/news/Mattel-appoints-ken-wee-as-executive-vice-president-and-chief-strategy"}
  {"id": "C07C2866011/1755713069.989399", "channel": "executives", "kind": "private", "date": "2025-08-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "o from <@EMPLOYEE_0025_SLACK_ID> for the test drive for the Mattel meeting"}
  {"id": "C07C2866011/1755718051.665759", "channel": "executives", "kind": "private", "date": "2025-08-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Mattel convo went well - they are interested in working with us and potentially even f"}
  {"id": "C07C2866011/1755718235.241099", "channel": "executives", "kind": "private", "date": "2025-08-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Mattel guy was very excited about it"}
  {"id": "C07C2866011/1756142092.369799", "channel": "executives", "kind": "private", "date": "2025-08-25", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "SON_NAME_0205] now, will ping Matthew and then reach out to Mattel for the follow-up"}
  {"id": "C07C2866011/1756249510.695649", "channel": "executives", "kind": "private", "date": "2025-08-26", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I need to share something with Mattel [EMAIL_169201] - maybe not the whole list but at least the adjacent list sounds"}
  {"id": "C07C2866011/1756832170.947819", "channel": "executives", "kind": "private", "date": "2025-09-02", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "This is Mattel, right?"}
  {"id": "C07C2866011/1757012563.252789", "channel": "executives", "kind": "private", "date": "2025-09-04", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "<@EMPLOYEE_0016_SLACK_ID> we got the RFP from Mattel"}
  {"id": "C07C2866011/1757084206.990219", "channel": "executives", "kind": "private", "date": "2025-09-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Maybe I shouldn’t say no to Mattel rfp request yet lol "}
  {"id": "C096HFA5Z8W/1756941551.539229", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-03", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "pital (Turkish, they do gaming as well, reached out)     *  Mattel (scheduling an engine demo)     *  NCsoft (reached out to Taewo
  {"id": "C096HFA5Z8W/1757345124.546449", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " (worried they will copy so not reaching out for now) - [-] Mattel (scheduling an engine demo) - [-] Scopely  (IH says they are no
  {"id": "D05S58U4SAK/1756250544.143349", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-08-26", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "I like that even the Mattel guy was thinking about ways to make game development more efficient. Feels like"}
  {"id": "D05S58U4SAK/1756253219.992509", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-08-27", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " the time last week—it was great to meet you and hear about Mattel’s refreshed, in-house approach to building high-quality games. You’re
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Treo' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C050WGU41HR/1692643387.094079", "channel": "engineering-bots", "kind": "private", "date": "2023-08-21", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ut and playable. • The team plans to start working on the Patreon stuff in mid-October, once they have completed the necessary
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Initial Capital' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=23 (showing 15)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UM32UWKD/1682000005.822869", "channel": "investors", "kind": "private", "date": "2023-04-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "terest and whom to reach out to. Do you guys want to go for initial capital? "}
  {"id": "C04UM32UWKD/1682000191.941059", "channel": "investors", "kind": "private", "date": "2023-04-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "[PERSON_NAME_6550] was one of the founders of initial capital of Im not mistaken. I think it’s the ex play fish crew. [PERSON_NAME_65
  {"id": "C04UM32UWKD/1682016569.327649", "channel": "investors", "kind": "private", "date": "2023-04-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "we want to meet initial capital, right?"}
  {"id": "C04UM32UWKD/1682016738.530109", "channel": "investors", "kind": "private", "date": "2023-04-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "<@EMPLOYEE_0016_SLACK_ID>? Initial capital?"}
  {"id": "C04UM32UWKD/1682038971.936509", "channel": "investors", "kind": "private", "date": "2023-04-21", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "We are talking to [PERSON_NAME_0128] from initial capital. Timing tbd "}
  {"id": "C04UM32UWKD/1682098948.321839", "channel": "investors", "kind": "private", "date": "2023-04-21", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " following (amazing translation from Google :P)  '''hi bro. Initial capital and sisu ventures asked us for our deck, I have to send i
  {"id": "C04UM32UWKD/1682113844.164709", "channel": "investors", "kind": "private", "date": "2023-04-21", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "can you guys do 9am on May 4th for the Initial Capital friendly?"}
  {"id": "C04UM32UWKD/1683255055.028989", "channel": "investors", "kind": "private", "date": "2023-05-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I am still very glad that we had warm-ups before the initial capital conversation. those two meetings made us much stronger"}
  {"id": "C04UM32UWKD/1683270292.772319", "channel": "investors", "kind": "private", "date": "2023-05-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "if initial capital makes an offer, I think we can tell them [PERSON_NAME_20906] is interested and "}
  {"id": "C04UM32UWKD/1684257354.049899", "channel": "investors", "kind": "private", "date": "2023-05-16", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Is it time to hit initial capital now we have a soft commitment and see if they are also interested writing a che"}
  {"id": "C04UM32UWKD/1684795020.034959", "channel": "investors", "kind": "private", "date": "2023-05-22", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "na send pretty much the same message to [PERSON_NAME_0128] (initial capital) with slight modifications"}
  {"id": "C04UM32UWKD/1684813275.689839", "channel": "investors", "kind": "private", "date": "2023-05-23", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "btw - I hope we also get another second round with initial capital people"}
  {"id": "C04UM32UWKD/1684813322.063039", "channel": "investors", "kind": "private", "date": "2023-05-23", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "if we have both Sisu and Initial Capital second round, then I think we can lure in more tier 1 VCs in that are hesitant"}
  {"id": "C04UM32UWKD/1684880753.712359", "channel": "investors", "kind": "private", "date": "2023-05-23", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Also looks like initial capital is discussing the next steps "}
  {"id": "C04UM32UWKD/1684893982.401709", "channel": "investors", "kind": "private", "date": "2023-05-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "This is what happened with Initial Capital if you think about it. Because it was [PERSON_NAME_6550], [PERSON_NAME_0128] wa"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH contacts 'Ryo' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
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
| a16z Speedrun forward | Oct 1, 2025 03:21Z = Tue Sep 30, 8:21pm PT: inside the end-of-Sep-30-PT window; a base record after the seed bound | frederick.stone@harmonygames.co/1844748127814183717 | past (In talks: the template's accelerator rule, §4b) |
| Leonard's Treo VC post | Wed Sep 3, 2025 23:31Z (4:31pm PT, the kickoff day) | C096HFA5Z8W/1756942260.617302 | past |
| Leonard's 1AM Gaming post | Mon Sep 8, 2025 21:05Z (2:05pm PT) | C096HFA5Z8W/1757365500.384216 | past |
| Leonard's Initial Capital post | Tue Sep 9, 2025 18:20Z (11:20am PT) | C096HFA5Z8W/1757442000.492583 | past |
| Leonard's Play Ventures correction | Thu Sep 25, 2025 16:20Z (9:20am PT) | C096HFA5Z8W/1758817200.730591 | past |
| Leonard's Mattel note | Fri Sep 26, 2025 22:50Z (3:50pm PT) | C096HFA5Z8W/1758927000.205874 | past |

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
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (1)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EMAIL', 'contacts.email=PERSON_3233_EMAIL', 'email.email=PERSON_3233_EMAIL', 'github.login=PERSON_3233_GITHUB_USERNAME', 'slack.id=PERSON_3233_SLACK_ID']}
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']}
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']}
  PERSON_5360: {'entities': ['? <PERSON_5360_EMAIL>', '? <slack:PERSON_5360_SLACK_ID>'], 'records': ['email.email=PERSON_5360_EMAIL', 'slack.id=PERSON_5360_SLACK_ID']}

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)'
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
  General Counsel: ['Michelle Carter <michelle.carter@harmonygames.co>', 'Thomas Baker <thomas.baker@harmonygames.co>']
  User Acquisition Manager: ['George Miller <george.miller@harmonygames.co>', 'Megan Wilson <megan.wilson@harmonygames.co>', 'Victoria Lane <victoria.lane@harmonygames.co>']

UNRESOLVED (11)
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello:3d36d70154e6a715614e0d75']
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMPLOYEE_0032_GITHUB_USERNAME', 'slack:EMPLOYEE_0032_SLACK_ID']
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2360_EMAIL', 'github:PERSON_2360_GITHUB_USERNAME']
  [token_link] PERSON_3233: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3233_EMAIL', 'github:PERSON_3233_GITHUB_USERNAME', 'slack:PERSON_3233_SLACK_ID']
  [token_link] PERSON_3335: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3335_EMAIL', 'slack:PERSON_3335_SLACK_ID']
  [token_link] PERSON_3935: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3935_EMAIL', 'slack:PERSON_3935_SLACK_ID']
  [token_link] PERSON_5275: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5275_EMAIL', 'slack:PERSON_5275_SLACK_ID']
  [token_link] PERSON_5360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5360_EMAIL', 'slack:PERSON_5360_SLACK_ID']

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)"}
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=leonard.hayes@harmonygames.co, threads=15339, messages=19668, first=2023-03-15, last=2025-10-01, thread_filename_alias=['leonard@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=leonard.hayes@harmonygames.co, owner_email=leonard.hayes@harmonygames.co, summary=Leonard Hayes — primary, events=1382, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_63fffeb4fab5, email=leonard.hayes@harmonygames.co, display_name=leonard.hayes@harmonygames.co, root_folders=['d_63fffeb4fab5233ed5bb73'], owned_items=752, last_modified=2025-09-30, files_shared_with=365   [join: exact_email]
  linear     id=usr_63fffeb4fab5233e, email=leonard.hayes@harmonygames.co, name=leonard.hayes@harmonygames.co, is_active=True, last_activity=2025-09-22   [join: exact_email]
  trello     id=PERSON_6094_TRELLO_USER_ID, username=leonard.hayes, fullName=Leonard Hayes, last_activity=2025-09-30   [join: exact_name]
  confluence id=user_EMPLOYEE_0038, account_id=acct_EMPLOYEE_0038, email=leonard.hayes@harmonygames.co, display_name=Leonard Hayes, is_active=True, last_activity=2025-09-29   [join: exact_email]
  contacts   contact_id=63fffeb4fab5233ed5bb73bf, name=Leonard Hayes, email=leonard.hayes@harmonygames.co, job=Co-founder & CEO, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-30', 'linear': '2025-09-22', 'trello': '2025-09-30', 'confluence': '2025-09-29'}
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=110334, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=14813, messages=17363, first=2023-03-15, last=2025-10-01   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1133, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=190, last_modified=2025-09-25, files_shared_with=412   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=3d06b73654d0c8940792514c, username=robert, fullName=Robert   [join: exact_name]
  confluence id=user_EMPLOYEE_0016, account_id=acct_EMPLOYEE_0016, email=robert@harmonygames.co, display_name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  contacts   contact_id=5f647df33ba6e92fbd56b05b, name=Robert, email=robert@harmonygames.co, job=Co-founder & Chief Product Officer, is_user=True   [join: exact_email]
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-25', 'linear': '2025-09-30', 'github': '2025-09-29', 'confluence': '2025-09-30'}
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=35266, first_post=2023-03-20, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=arthur.blake@harmonygames.co, threads=3320, messages=5134, first=2023-03-23, last=2025-10-01, thread_filename_alias=['blake@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=arthur.blake@harmonygames.co, owner_email=arthur.blake@harmonygames.co, summary=Arthur Blake — primary, events=756, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_cc3e90160f49, email=arthur.blake@harmonygames.co, display_name=arthur.blake@harmonygames.co, root_folders=['d_cc3e90160f490686039986'], owned_items=246, last_modified=2025-09-19, files_shared_with=403   [join: exact_email]
  linear     id=usr_cc3e90160f490686, email=arthur.blake@harmonygames.co, name=arthur.blake@harmonygames.co, is_active=True, last_activity=2025-09-15   [join: exact_email]
  github     login=EMPLOYEE_0025_GITHUB_USERNAME, name=Arthur Blake, email=arthur.blake@harmonygames.co, type=User, last_activity=2025-09-30   [join: exact_email]
  trello     id=2162c1ba310341bf318f48b7, username=arthur.blake, fullName=Arthur Blake   [join: exact_name]
  confluence id=user_EMPLOYEE_0025, account_id=acct_EMPLOYEE_0025, email=arthur.blake@harmonygames.co, display_name=Arthur Blake, is_active=True, last_activity=2025-09-12   [join: exact_email]
  contacts   contact_id=cc3e90160f49068603998654, name=Arthur Blake, email=arthur.blake@harmonygames.co, job=Co-founder & CTO, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-19', 'linear': '2025-09-15', 'github': '2025-09-30', 'confluence': '2025-09-12'}
ENTITY email:frederick.stone@harmonygames.co  name=Frederick Stone  kind=person  emails=['frederick.stone@harmonygames.co']
  persona: frederick_stone - Co-founder / Executive
  slack      id=EMPLOYEE_0008_SLACK_ID, name=Frederick Stone, real_name=Frederick Stone, email=frederick.stone@harmonygames.co, is_bot=False, deleted=False, messages=4780, first_post=2023-09-15, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=frederick.stone@harmonygames.co, threads=4656, messages=5474, first=2024-06-25, last=2025-10-01, thread_filename_alias=['frederick@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=frederick.stone@harmonygames.co, owner_email=frederick.stone@harmonygames.co, summary=Frederick Stone — primary, events=316, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_175c0d7bc72e, email=frederick.stone@harmonygames.co, display_name=frederick.stone@harmonygames.co, root_folders=['d_175c0d7bc72ed244b944cb'], owned_items=46, last_modified=2025-09-24, files_shared_with=213   [join: exact_email]
  linear     id=usr_175c0d7bc72ed244, email=frederick.stone@harmonygames.co, name=frederick.stone@harmonygames.co, is_active=True, last_activity=2025-08-26   [join: exact_email]
  github     login=PERSON_2314_GITHUB_USERNAME, name=Ryan, email=frederick.stone@harmonygames.co, type=User, last_activity=2025-03-25   [join: exact_email]
  trello     id=4b4a68fc0fec0b254e4f9d8e, username=frederick.stone, fullName=Frederick Stone   [join: exact_name]
  confluence id=user_EMPLOYEE_0008, account_id=acct_EMPLOYEE_0008, email=frederick.stone@harmonygames.co, display_name=Frederick Stone, is_active=True, last_activity=2025-09-01   [join: exact_email]
  contacts   contact_id=175c0d7bc72ed244b944cb90, name=Frederick Stone, email=frederick.stone@harmonygames.co, job=Commercial Lead, Marketing & Business Development, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-24', 'linear': '2025-08-26', 'github': '2025-03-25', 'confluence': '2025-09-01'}
  FLAG: GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)
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
| facts NO in §5a | none; nothing routed | §5a F1–F38 |
| surface money patterns | rev4 widened M2, RP2, RP3 to accept "$25K" / "$50K" as well as "25,000" (gradeable-report PASS) | 01_Gradable_Surface.json M2, RP2, RP3 |
| platform /prompt rev3 FAIL (UGT 2, Cross-Service Coherence 2) | settled in rev4 records; needs `/injection` then `/prompt` on SQL 3ba2b413458f | Platform_Report/peompt_report1, 01_Grounding_Dossier.md "Platform /prompt review of rev3" |
| SC-33 watch on the register count (79) | only the V1 row and the reply's firm count rest on it; rubric fallback: grade per-firm rows and drop a bare count row if /rubric flags it | f_48247af79428823c3cac92, f_3b9e61c04d7a52e8f1a6c2 |
| facts UNVERIFIED | none | 01_Grounding_Dossier.md §1.E |

## 13 · Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`).** Phase 1: persona (§1.1) Frederick is the addressee of Leonard's ask and on every investor cc (§1); voice (§1.2) is judged against a co-founder only. Anti-patterns (§1.3): no command list, no bolt-ons (the checklist and the reply are both in Leonard's one ask, frederick.stone@harmonygames.co/1844724419788800011), no pre-solving (§9), no tool names (§9). Diversity (§1.4): three writes in Sheets/Drive, Trello and Gmail. Assignment and complexity (§1.5): Corporate Ops fundraising/board work, Retrieval stacked with analysis and actions; Ambiguity, Dynamic change and Multi-source load-bearing (§8). Phase 2: fair readings (§2.1) in §4b; feasibility (§2.2) every write in the catalog and every read YES (§5a); truthfulness (§2.3) the premises in §7; cross-service (§2.4) 10 services; investigation → action (§2.5) §3; clarity (§2.6) §4; contrived (§2.7) §9 and §11; today's date (§2.8) §7; originality (§2.9) no supplied sample, and the earlier Frederick task (account custody before layoffs, support/completed_tasks) shares only the persona. Phase 3: universe coherence rests on the rev3 `/injection` PASS (Platform_Report/injection_report3, SQL 952e12a9ad7a).

| Area | Counter-reading | Evidence | Resolution |
|---|---|---|---|
| Fair readings (C6) | Reading B: Paul Heydon is committed, since Leonard's post says he "is in for $50K" and the angels sheet lists him | C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e vs the incorporated template "Committed: signed SAFE only" (f_3b9e61c04d7a52e8f1a6c2), no Completed notice beside Anton's (frederick.stone@harmonygames.co/1844354293432320031), the Sep 29 nudge (frederick.stone@harmonygames.co/1844610859008000037) | an incorporated authority settles it (C6 step 2); §4b soft-circled 50,000 |
| Fair readings (C6) | Reading B: a16z passed (the Speedrun forward), which adds a fourth keep-warm item | frederick.stone@harmonygames.co/1844748127814183717 (Sep 30 8:21pm PT, inside the window) vs frederick.stone@harmonygames.co/1842277213140775733 | no newer source, authority or scope settles it; both statuses and the matching checklist are accepted outcomes in §4b and the sidecar |
| Fair readings (C6) | Reading B: Hiro Capital is Awaiting reply, as the list says | f_48247af79428823c3cac92 "no response as of 09/11" vs frederick.stone@harmonygames.co/1844318935449600041, e3a91c07d5b48f26a0c7e314 and the template's "A partner writing from their own address counts for their firm" (f_3b9e61c04d7a52e8f1a6c2) | a newer source plus the incorporated rule settle it: Passed |
| Fair readings (C6) | Reading B (author blind sweep of rev4): the reply's firm count leaves out the five angels (74) or counts list names (77) | Board Deck comment 68d81f30a6c94e2b7d05e1f4 now reads "how many firms are on it (every row, angels included)"; slide 9 f_a47d0e2c95b18f63e2c0d5 "Firms on Fred's sheet" | settled by the comment's own wording: 79 |
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

Re-verified this run: the hub, template, README, both card comments and both ZOM-567 comments read from the rev4 SQL rows (base_check.parse_sql); the 38 searches in §5a run with persona_view as frederick_stone; entity.py collisions and resolve run now; the totals and statuses from solver/truth.json (sha256 33d88dacdb04ab89); write tool names and parameters from the Evals tool catalog; Pacific times computed from the UTC stamps.

Unresolved: none blocking. Two rubric-stage notes are in §12 (K-form amounts; the SC-33 count watch).

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputs · 04_Prompt_Writing_Brief.md#c53118f3dba1 · 00_Assigments.md#8ae66b700bc2 · 01_Grounding_Dossier.md#53e3be20bb54 · 01_Universe_Inject.sql#3ba2b413458f · 03_Error_Async_Config.txt#78ab098fdd8c · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#0fc4bb90877f · __review__#6cfbba924d10 · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#3ba2b413458f, 01_Hardness_Manifest.json#310cf1471b6b, 01_Grounding_Dossier.md#53e3be20bb54, solver/solver.py#181bf69d6fac, 01c_Dispositions.json#189e9a7d4b76, 01c_Preflight_Report.json#0b9187aeb605, 00_Assigments.md#8ae66b700bc2, 01_Scenario_Design.md#3d0a8e257730, 01_Hardness_Manifest.draft.json#dc72a8f7e6aa, 01_Gradable_Surface.json#3435f76f2995, __context__#f1f763cb8cb4, __assignment__#827e8afa884d, __policy__#dc4ab5df3cdd, __gate_policy__#0fc4bb90877f, __review__#724c5240bc3b)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#78ab098fdd8c, 00_Assigments.md#8ae66b700bc2, 01_Grounding_Dossier.md#53e3be20bb54, 01_Universe_Inject.sql#3ba2b413458f, __context__#f1f763cb8cb4, __assignment__#827e8afa884d, __policy__#dc4ab5df3cdd, __gate_policy__#0fc4bb90877f, __review__#724c5240bc3b)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 5/5 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 33/33 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 38/38 items carry a source pointer (min 100%)
[PASS] evidence.dates: 26/26 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 15/15 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 38 facts proven findable by persona_view search as frederick_stone
[PASS] reach.brief: 39 scoped load-bearing ids YES for frederick_stone
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 1 anchor-naming entry, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 16 evidenced counter-readings (of 16 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
