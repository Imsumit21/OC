# Prompt Brief — frederick_bridge_pipeline · prep
> Built 2026-11-02 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Universe_Inject.sql (rev12, sha256 69db98aed17f: the rev7 Q4 investor update send-list job; rev12 moves Leonard's "Paul's out" into his 1:1 DM with Frederick, removes the T-Accelerate mail replies and makes Arthur's correction a #zombie-match3d root post naming four firms in talks (two more on ZOM-567) after the rev11 baseline (five of six runs failed the same values); rev11 had Paul Heydon back out (Leonard's reply under his angel post) and adds Arthur's answer to Karthic in the T-Accelerate thread after the rev10 baseline (six runs, one failure pattern over 4 of 6 runs); rev10 moved Arthur's Play correction into a thread reply under Leonard's 0.3.49 iOS release post and adds Paul's "Done, signed it last night" reply after rev9 scored `/hardness` 1 (Platform_Report/hardness_report3; /injection and /prompt passed); rev9 added Leonard's Sep 29 card comment (a checklist per group, follow-up cards), his open To Do card for NCsoft's partner and the Oct 8 Makers call after the rev8 baseline (4895577edea8: 72.7 counted calls, about 82% pass); rev8 fixed one base-list cell (LVP 09/07 -> 09/09, platform /prompt rev7 coherence finding); rev7 efe3cab14874 passed `/injection` and scored `/prompt` NON-FAIL 3; rev6 848189443008 passed `/injection` and scored every `/prompt` content dimension 5 but failed the new dataset-duplicate gate (Platform_Report/prompt_report4), so rev7 changes the job and the prompt; rev5 3ba2b413458f passed `/injection` and `/prompt` and then failed the Opus pre-check `/hardness` with score 1, too easy (Platform_Report/hardness_report1; Working_Files/01a_Hardening_Report.md), so rev6 moves three corrections off the paths that run swept and keeps every graded value except T-accelerate's build access; rev4 2e2428bc5e49 passed `/injection` and failed `/prompt` only on Initial Capital and the ZOM-567 dates (Platform_Report/prompt_report2), fixed in rev5; rev3 952e12a9ad7a passed `/injection` but failed `/prompt` on data forks, Platform_Report/peompt_report1, settled in rev4), Working_Files/01_Grounding_Dossier.md, 01_Scenario_Design.md, 01_Hardness_Manifest.json, 01_Gradable_Surface.json, solver/truth.json (rev12), 03_Error_Async_Config.txt (Friction: none, error-async gate PASS) · no 02_Reference_Files_Manifest.md (no attachments) · Persona view verified: all (every §5 fact YES for frederick_stone; seeded rows by check-sql, base rows by persona_view search and can-see).
> Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Persona today is Wed Oct 1, 2025; the seed bound is 2025-10-01T00:00:00Z and the latest seeded record is Leonard's ask at 2025-09-30T21:05Z (2:05pm PT).
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. This brief holds facts, noun phrases and locators only; it has no draft sentence.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive → `task_categories.md` "Founders / Exec / Strategy" (executive coordination, investor relations) | a co-founder owns the bridge part of the Q4 investor update send list while the CEO travels (frederick.stone@harmonygames.co/1844724419788800011); the update goes out after the Oct 14 board (evt_bd61f3209523d19fdd6ba2) |
| Persona | Frederick Stone · frederick.stone@harmonygames.co · Co-founder (roster); Contacts 175c0d7bc72ed244b944cb90 says "Commercial Lead, Marketing & Business Development" (SC-49, never graded) | voice: a terse founder asking his assistant to take a job off his plate. Remit: on the cc of every bridge investor thread (frederick.stone@harmonygames.co/1842277743427687737, frederick.stone@harmonygames.co/1843547312959065138), a member of #bridge-pitch C096HFA5Z8W and #executives C07C2866011, invited to the Oct 14 board (evt_bd61f3209523d19fdd6ba2), and the addressee of Leonard's ask. Read scope: his own mailbox and calendar, the two channels, Drive files shared with him or owned by him; Trello, Linear and Contacts are unscoped |
| Competency | Corporate Ops (taxonomy: fundraising, board; outputs: spreadsheets, memos) | the bridge-round audience of the Q4 investor update: who signed (new investors, with their checks), who is in talks (with build access), who awaits a reply and who passed after a pitch (keep warm), filed as a spreadsheet, plus the keep-warm follow-through Leonard's card asks for and the group counts back to Leonard (hub frederick.stone@harmonygames.co/1844724419788800011) |
| Task skill | Retrieval (stacked: Analysis and Synthesis; Actions) | Retrieval: each firm's state, signed amounts and tester access, pulled from mail, Slack threads and DMs, calendar, Contacts, Linear and the list f_48247af79428823c3cac92. Analysis: apply the send-list doc's groups (f_3b9e61c04d7a52e8f1a6c2) over conflicting sources. Actions: the sheet in d_5e8a1c3f9b07d2e64a1b93, the checklist on card 68c5a49e8491a9d7faf869d0, the reply on the hub |
| Task type | long-horizon → Long Horizon tier (100–500+ calls); difficulty mode medium (cap < 85%; the user's target ≤ 80%) | 10 services carry weight (gmail, slack, gcal, gsheets, gdocs, gdrive, gslides, trello, linear, contacts). Measured volumes: 79 names looked at (80 list rows / 77 names on f_48247af79428823c3cac92 plus 2 off-list calls), 26 kept on the send list; 12 "Leonard Hayes" calls on Frederick's calendar in scope of the sweep (10 base + 2 seeded, §5a F15); per-firm mail and Slack searches. Manifest call_budget: 508 honest calls (333 per-record); the rev5 Opus run made 107 tool calls, 01_Hardness_Manifest.json; HARDNESS GATE (extreme): PASS in 01_Grounding_Dossier.md |

Known data issues (references/known_data_issues/synthcut.md) the asks touch, none graded on a "don't grade" value:
- SC-33 (watch: Acterra twice on f_48247af79428823c3cac92): the send-list doc counts a repeated name once (f_3b9e61c04d7a52e8f1a6c2); Acterra is not contacted, so it stays off the list either way.
- SC-34 (row 82 Superplay label, Supercell contents): one row under either name; its status is not sampled.
- SC-9 (Play Ventures rejected vs no reply): settled in rev4 by Leonard's Sep 25 correction C096HFA5Z8W/1758817200.730591 (the Sep 15 no C096HFA5Z8W/1757955553.793529 was their reply to Griffin): Passed.
- SC-10 (LVP meeting Sep 7 vs Sep 9): no LVP date graded; status from frederick.stone@harmonygames.co/1842277743427687737.
- SC-40 (July board date): the rev7 decoy is the Q3 (July) send list and gives no board date (f_8d2c47a91e05b3f6d7c418); not graded.
- SC-49 (founder count, Frederick's title): not graded; role rests on activity (evt_bd61f3209523d19fdd6ba2).
- SC-3 / SC-73 (runway, burn): no cash figure is read or graded.

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard, flying to LA on Oct 1, hands Frederick the send list for the Q4 investor update on Tue Sep 30 at 2:05pm PT and wants a reply with how many firms and angels are in each group | Frederick (To); Robert and Arthur on cc | frederick.stone@harmonygames.co/1844724419788800011 | none needed: Frederick holds the To copy (dossier §1.E) |
| the 2025 investor list's Latest Status column stops at 09/11 | Frederick (shared reader) | f_48247af79428823c3cac92 | none |
| Leonard's #executives angel post and his Bridge angels sheet show two angels as in | Frederick (#executives member; sheet shared) | C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e | none |
| two "investor update - send list" docs sit side by side (Q3 July and Q4) | Frederick (shared reader) | f_3b9e61c04d7a52e8f1a6c2, f_8d2c47a91e05b3f6d7c418 | none |
| Robert wants the update sent to everyone on the 2025 list; Leonard's ask says no | Frederick (To on both) | frederick.stone@harmonygames.co/1844623441920000059, frederick.stone@harmonygames.co/1844724419788800011 | none |

## 3 · Investigation → action

Questions (answers stay in §4b and §5):
- Who gets looked at: which names on the 2025 list (repeats included once), and which firms off the list had a pitch call or meeting since the Sep 3 kickoff that counts as investment talks?
- Which group fits each one as of end of day Tue Sep 30 PT (New investor, In talks, Awaiting reply, Keep warm), and who stays off the list, including a no one of us heard and a pass sent by someone whose firm has to be looked up?
- Who has actually signed (a DocuSign Completed notice, per Leonard's #executives note), and which amount did each angel last agree?
- For firms in talks, which can actually get the current internal build on TestFlight and on the Play internal track?
- Which firms that passed had been pitched on a call or meeting first?
- Which of the people In talks or Awaiting reply already have a follow-up card in To Do (named for a partner, not the firm), and which already have a call or meeting on Fred's calendar after Sep 30?
- How is the sheet named and where is it filed, and what goes in the reply?

Writes fed by those answers:
- the send list sheet in Frederick's Q4 2025 investor update folder (questions 1–4 and 6);
- a checklist per group on the Existing Investor Update card, one item per firm or angel (questions 1, 2 and 5);
- a follow-up card in To Do for everyone In talks or Awaiting reply, a comment on an existing To Do card instead, and none where a call is already booked (questions 2 and 6);
- the reply on Leonard's email with the count per group (questions 2 and 7).
Each write depends on the investigation: none can be written from the prompt or the hub alone.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| D1 send list (Google Sheet) | one row per firm or angel kept on the list (send-list doc f_3b9e61c04d7a52e8f1a6c2): firm, group (New investor, In talks, Awaiting reply, Keep warm), amount (new investors and unsigned angels in talks), build access (firms in talks); email-only passes and firms not contacted since Sep 3 stay off | folder d_5e8a1c3f9b07d2e64a1b93, named per README f_c61a0e93b7d24f58a2e917 | none (filed in Frederick's own folder) | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file | F1–F20, F23–F25, F27–F30, F39–F41 |
| D2 send checklists | a checklist per group on the card, one item per firm or angel in it: Keep warm (rule 68c64270d660c977c4696986: passed after a pitch call or meeting) and New investor, In talks, Awaiting reply (rule 68db03b86054eff7e8e92474); 25 items | Trello card 68c5a49e8491a9d7faf869d0 | none (Trello) | trello_create_checklist, trello_create_check_item | D1 groups, F11–F15, F21, F27, F42 |
| D4 follow-up cards | an "F/up with" card in To Do for everyone In talks or Awaiting reply (18 cards); a comment on Leonard's open To Do card 68c99e98737744bd966aed24 for NCsoft instead of a second card; no card for Dentsu Ventures or Makers Fund (calls on Fred's calendar after Sep 30) | To Do list 640643a3fd8f3ca308d93195 on the Harmony Games board | none (Trello) | trello_create_card, trello_add_comment | D1 groups, F42–F46 |
| D3 reply to Leonard | how many firms and angels are in each group (hub: "reply here with how many firms and angels are in each group"); a sheet link is optional | reply on thread frederick.stone@harmonygames.co/1844724419788800011 (message frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>) | leonard.hayes@harmonygames.co (reply), or with robert@harmonygames.co and arthur.blake@harmonygames.co (reply-all) | gmail_reply_to_message | D1 |

Alternatives a careful run could defend:
- Reply vs reply-all on the hub frederick.stone@harmonygames.co/1844724419788800011: same decision, thread and contents; both accepted.
- Create the sheet in Frederick's root and move it vs create it in place: only the final parent d_5e8a1c3f9b07d2e64a1b93 is material.
- Send the reply now vs leave a draft: the prompt and the hub (frederick.stone@harmonygames.co/1844724419788800011, "reply here") ask for the reply; a draft is not a send (C18), so it does not deliver D3.
- Put every name on the 2025 list on the send list, as Robert asked (frederick.stone@harmonygames.co/1844623441920000059): not fair; the hub withdraws it ("Let's not, only the people the doc says.").
- Edit the draft deck f_a47d0e2c95b18f63e2c0d5 or write the update: not asked; Leonard writes it himself (hub frederick.stone@harmonygames.co/1844724419788800011).
- a16z off the list as passed on the speedrun no (frederick.stone@harmonygames.co/1844748127814183717): not fair; the doc says an accelerator decision is not a bridge answer and the interview (evt_e802a3583ee79ff6087f76) counts as a call, so In talks.

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| D1 | file kind and parent | a native Google Sheet whose parent is d_5e8a1c3f9b07d2e64a1b93 (README f_c61a0e93b7d24f58a2e917: "Google Sheets or Docs only, no uploads") | "put it in your Q4 investor update folder" | created there or moved there; one sheet | material |
| D1 | file name | README pattern `Q4 update - send list` (f_c61a0e93b7d24f58a2e917) | "the README in that folder says how to name it" | any name carrying send list, Q4 or update; case and dash variants | representational |
| D1 | membership | 25 rows: Anton Bernstein, GFR Fund, Andreessen Horowitz, NCsoft, Dentsu Ventures, T-accelerate, Homa (evt_89381fe5a15b802c5652a9), Brightwater Games Fund (evt_2f86b0d4c9e17a35b64e0d), London Venture Partners, Hiro Capital, Sciplay, and the 14 Awaiting reply names (Initial Capital, BITKRAFT Ventures, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital); off: Play Ventures, March Gaming Fund, Grishin Robotics, Lakestar Ventures, [PERSON_NAME_5402] (passed without a pitch call this round), Paul Heydon (rev12: backed out on Sep 30, D05S58U4SAK/1759251900.863415, no call) and the 48 not contacted; T-accelerate is one row (PXLite alias, frederick.stone@harmonygames.co/1843978997950200606) | "everyone from the bridge round who should get it" | list spelling or the obvious full form; any row order | material |
| D1 | Group · Sciplay | Keep warm: Robert's Sep 30 reply C07C2866011/1759248360.377105 (they're passing on this round) after the Sep 15 call evt_25c9ee60d4b6c8f6d39a74 overturns frederick.stone@harmonygames.co/1842285743246816270 | "with the groups and details in the Q4 update send list doc" | the doc's group words, any case | material |
| D1 | Group · Hiro Capital | Keep warm: frederick.stone@harmonygames.co/1844318935449600041 from Edith Vane (e3a91c07d5b48f26a0c7e314) after the Sep 23 call evt_7d3e19b04a6c25f8e1b9a0 | as above | as above | material |
| D1 | Group · London Venture Partners | Keep warm: frederick.stone@harmonygames.co/1842277743427687737 (call evt_e59dc0a675d0c407b79acf) | as above | as above | material |
| D1 | Group · Homa, Brightwater Games Fund | In talks: calls evt_89381fe5a15b802c5652a9 (HOMA in frederick.stone@harmonygames.co/1843169166284025277) and evt_2f86b0d4c9e17a35b64e0d (contact b72f0d6e19c3a84e5d21f9a0, follow-up frederick.stone@harmonygames.co/1844276782694400053) | as above | as above | material |
| D1 | Group · Anton Bernstein | New investor: SAFE re-sent at 25 (D05S58U4SAK/1758731100.281734) and signed (D05S58U4SAK/1758914100.640218; Completed notice frederick.stone@harmonygames.co/1844354293432320031); new investor = Completed notice in (C07C2866011/1758911700.336170) | as above | as above | material |
| D1 | Group · Paul Heydon | off the send list (rev12): he said yes (C07C2866011/1758303600.418207), then backed out on Sep 30 before signing (Leonard's message in his 1:1 DM with Frederick, D05S58U4SAK/1759251900.863415); a no for this round with no call stays off | as above | no row (and no checklist item or card) | material |
| D1 | Group · firms settled in rev4 | Andreessen Horowitz In talks (accelerator rule; interview evt_e802a3583ee79ff6087f76); Play Ventures off (passed via Griffin, C096HFA5Z8W/1758817200.730591, no call this round); March Gaming Fund off (C096HFA5Z8W/1757365500.384216); Mattel off (RFP only, C096HFA5Z8W/1758927000.205874); General Catalyst, Triptyq, Turkven, Harlem Capital Awaiting reply (IH outreach C096HFA5Z8W/1757716998.377299); Treo VC, Superplay, BITKRAFT Ventures, Initial Capital Awaiting reply (C096HFA5Z8W/1756942260.617302, f_48247af79428823c3cac92, C096HFA5Z8W/1758563861.649039, C096HFA5Z8W/1757442000.492583); [PERSON_NAME_5402] off (Latest Status note "don't do bridge" is a no, no call); Transcend Fund, Acterra, Index Ventures off (plans and earlier-round answers don't count) | as above | as above | material (one value each) |
| D1 | Amount · Anton Bernstein | 25,000 (D05S58U4SAK/1758731100.281734, D05S58U4SAK/1758914100.640218) | "Get the new investors right, they'll look for their own check in it." | 25000, 25,000, $25,000, $25K, 25k (USD) | material |
| D1 | Amount · Paul Heydon | none (rev12: Paul is off the list, D05S58U4SAK/1759251900.863415) | as above | no row | material |
| D1 | Amount · everyone else | blank (the doc's Sheet section, f_3b9e61c04d7a52e8f1a6c2: amount only for new investors and angels in talks) | — | blank, n/a, a dash | representational |
| D1 | Build access · Dentsu Ventures | iOS only: TestFlight added (ZOM-567 lc_b549f3057640a5eb08f7581e); Android not live per Arthur's Sep 30 root post C0880U9751A/1759274400.518306 in #zombie-match3d (the investor tester list he made in the Play console never got attached to the internal track, so nobody on it has android yet, "whatever the Linear log says"; iOS fine for all of them; he attaches it with the Oct 1 push) | "with the groups and details in the Q4 update send list doc" | iOS only; TestFlight only; iOS yes, Android no | material |
| D1 | Build access · T-accelerate, NCsoft, Brightwater Games Fund | iOS only: TestFlight added (ZOM-567 lc_94eb35d962cfbdd31e1bd496 Sep 22, lc_4369758f577612cdb63b3457 Sep 22, lc_5e2ff140afff06e3a78e2fe1 Sep 26); Android not live per C0880U9751A/1759274400.518306, which names Karthic, Anel's two at NCsoft and Ilse from Brightwater | as above | as above | material |
| D1 | Build access · other firms in talks | none: GFR Fund, Homa, Andreessen Horowitz (no tester add on ZOM-567 or in C0880U9751A/1759274400.518306) | as above | none, no, not on the tester list | material (not sampled) |
| D1 | Build access · angels and everyone not in talks | blank (doc f_3b9e61c04d7a52e8f1a6c2: "Leave it blank for angels"; only firms in talks) | — | blank, n/a, a dash | representational |
| D2 | checklists and names | four checklists on card 68c5a49e8491a9d7faf869d0, one per group: Keep warm (rule 68c64270d660c977c4696986: "a Keep warm checklist on this card"), New investor, In talks, Awaiting reply (rule 68db03b86054eff7e8e92474: "give every other group on the send list ... its own checklist on this card") | "Then do what I put on the Existing Investor Update card in Trello." | each named for its group or a close variant; location fixed | location and one-per-group material; names representational |
| D2 | items | the D1 membership split by group (rules 68c64270d660c977c4696986, 68db03b86054eff7e8e92474; groups from solver/truth.json): Keep warm London Venture Partners, Sciplay, Hiro Capital; New investor Anton Bernstein; In talks the 7; Awaiting reply the 14; one item per firm or angel, 25 in all | as above | list spelling or obvious forms (LVP; SciPlay; a16z); any order | material |
| D4 | follow-up cards | 18 cards in To Do 640643a3fd8f3ca308d93195, one per In talks or Awaiting reply entry except NCsoft, Dentsu Ventures and Makers Fund: GFR Fund, Andreessen Horowitz, T-accelerate, Homa, Brightwater Games Fund, Initial Capital, BITKRAFT Ventures, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital (rule 68db03b86054eff7e8e92474) | as above | "F/up with" + the name, or the name with a clear follow-up wording; list spelling or obvious forms; a description or due date optional | membership material; card wording representational |
| D4 | NCsoft | a comment on 68c99e98737744bd966aed24 ("F/up with Anel after the engine deep dive"; Anel Ceman is NCsoft's partner, f_48247af79428823c3cac92), no new NCsoft card | as above | any comment text on that card | material |
| D4 | Dentsu Ventures, Raine Ventures | no card: Fred's calendar has the Dentsu meeting on Wed Oct 1 (evt_3671b9a924ccba550e51fa) and the call "Michael Cheung and Leonard Hayes" on Wed Oct 8 (evt_6b2e94d0c17a3f58e9d2b1; Michael Cheung is Makers Fund's partner on f_48247af79428823c3cac92) | as above | — | material |
| D3 | thread and recipients | a reply on frederick.stone@harmonygames.co/1844724419788800011 to leonard.hayes@harmonygames.co | "reply here with how many firms and angels are in each group" | reply or reply-all (adds robert@harmonygames.co, arthur.blake@harmonygames.co) | thread material; reply vs reply-all representational |
| D3 | contents | New investor 0 firms 1 angel, In talks 7 firms 0 angels, Awaiting reply 14 firms, Keep warm 3 firms (25 in total; solver/truth.json, hub frederick.stone@harmonygames.co/1844724419788800011) | "reply here with how many firms and angels are in each group" | numerals or words; a total is optional; extra context (sheet link, a note on Android access) allowed | material |
| none | send to everyone on the list | no send list made of every 2025-list name (frederick.stone@harmonygames.co/1844623441920000059 withdrawn) | "Let's not, only the people the doc says." | — | material |

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 hub ask | Q4 update send list: who from the bridge round, groups per the doc, folder, card, reply with the count per group, not everyone on the 2025 list | frederick.stone@harmonygames.co/1844724419788800011 | YES (To, INBOX) | met first | none | Yes: Leonard's Q4 update email (anchor A1; Frederick received it) |
| F2 Q4 send-list doc | who to look at, groups as of end of Sep 30 PT, amounts, build access | f_3b9e61c04d7a52e8f1a6c2 (Q3 decoy f_8d2c47a91e05b3f6d7c418) | YES (shared) | the Q3 (July) send list shares the title stem; the Q4 doc supersedes its 'yes with an amount' rule | first-framing latch on the July doc | No |
| F3 2025 game investor list | 80 rows, 77 names, Latest Status as of 09/11 | f_48247af79428823c3cac92 (lookalike f_0b29566cd7932a205d54d2) | YES (shared) | met first; overturned per firm by later mail and Slack | lookalike internal list; repeated names (SC-33) | No |
| F4 angel post | Paul $50K and Anton $40K "in" | C07C2866011/1758303600.418207 | YES (member) | met first (DONE1, INPUT); overturned by F48 (Paul) and F6, F7, F40 (Anton) | stops at a conclusion-sounding post | No |
| F5 angels sheet | repeats F4 (Sep 20) | f_6e1d93a0c4b72f85d39a0e | YES (shared) | met first; overturned by F6–F8 | stale secondary source | No |
| F6 Anton's revised amount | 25, "not the 40"; the 40 SAFE voided, new SAFE at 25 (Sep 24) | D05S58U4SAK/1758731100.281734 (Leonard's DM to Frederick) | YES (DM member) | overturns F4 and F5 | a DM is in no channel read; the post, sheet and Completed notice agree with each other | No |
| F40 Anton signed | "Anton signed the 25 one" (Sep 26) | D05S58U4SAK/1758914100.640218 | YES (DM member) | settles which SAFE was completed | same DM | No |
| F7 DocuSign Completed | Anton's SAFE signed Sep 26 | frederick.stone@harmonygames.co/1844354293432320031 | YES (To) | decides New investor (with F22) | absence of Paul's notice needs a search | No |
| F8 Paul nudge | SAFE still with Paul (Sep 29) | frederick.stone@harmonygames.co/1844610859008000037 | YES (cc) | context: Leonard sent the SAFE through DocuSign | — | No |
| F48 Paul's out (rev12: in the DM) | Leonard, Sep 30 10:05am PT, in his 1:1 DM with Frederick: "Paul's out, he wrote me this morning that he can't put money in this year after all" | D05S58U4SAK/1759251900.863415 (Paul's own mail went to Leonard only) | YES (DM member) | overturns F4 for Paul: a no for this round, no call, so off the list | the DM is a 1:1 conversation away from the angel post, with no signing words | No |
| F49 Arthur's root post (rev12) | Sep 30 4:20pm PT in #zombie-match3d: the investor tester list in the Play console never got attached to the internal track, nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft, Ilse from Brightwater); iOS fine | C0880U9751A/1759274400.518306 | YES (#zombie-match3d member) | overturns F10 for Android (all four firms) | a root post in the game channel, found by searching tester, android, Play or a firm name | No |
| F9 Dentsu invites claim | "Invites … are out to all three" (Sep 26) | frederick.stone@harmonygames.co/1844294398771200045 | YES (cc) | met first (DONE2); overturned by F39 and F49 | stops at Leonard's conclusion | No |
| F10 tester ticket | the done source: T-accelerate and NCsoft TestFlight and Play both added Sep 22; Brightwater both added Sep 26; Dentsu TestFlight and Play added Sep 26 | ZOM-567 (comments lc_94eb35d962cfbdd31e1bd496, lc_4369758f577612cdb63b3457, lc_5e2ff140afff06e3a78e2fe1, lc_b549f3057640a5eb08f7581e) | YES (unscoped) | met first (DONE2); overturned by F39 and F49 | reads as done | No |
| F39 Play list not attached (rev12: root post again) | the investor tester list was never attached to the internal track: nobody on it has android, whatever the Linear log says; iOS fine; Arthur attaches it with the Oct 1 push | C0880U9751A/1759274400.518306 (+ reply C0880U9751A/1759276080.094417) | YES (#zombie-match3d member) | overturns F10 for Android | the correction is in the game channel, not on the ticket; found by searching Dentsu | No |
| F11 Sciplay phone pass | Robert's reply: Sciplay's out, D called him, passing on this round (Sep 30) | C07C2866011/1759248360.377105 under Leonard's speedrun post C07C2866011/1759196326.309469 | YES (member) | overturns F12 (CORR) | channel history omits replies; the root is about another firm | No |
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
| F22 what counts as signed | a new investor only once the DocuSign Completed notice is in (Sep 26) | C07C2866011/1758911700.336170 | YES (member) | decides New investor vs In talks for angels | — | No |
| F23 draft Q4 update deck | the bridge slide says what each group gets; firms in talks get build links | f_a47d0e2c95b18f63e2c0d5 | YES (shared) | confirms the groups matter | — | No |
| F24 Q4 update folder | Frederick's Q4 2025 investor update folder | d_5e8a1c3f9b07d2e64a1b93 | YES (owner) | destination | — | Yes: a destination Frederick owns, named in the hub as his folder |
| F25 folder README | naming pattern `Q4 update - send list` | f_c61a0e93b7d24f58a2e917 | YES (in his folder) | decides the file name | — | No |
| F26 review event | Mon Oct 6 2:00pm PT send list review | evt_9c41e7a2d05b38f6e1a7c4 | YES (own calendar) | deadline | — | Yes: Monday, Oct 6 is on his calendar |
| F27 LVP pass | pass Sep 25 after the Sep 9 call | frederick.stone@harmonygames.co/1842277743427687737 (call evt_e59dc0a675d0c407b79acf) | YES (cc) | keep-warm member | 14 hits for "LVP" | No |
| F28 T-accelerate thread | recap of the Sep 22 call; in talks | frederick.stone@harmonygames.co/1842283406259093714 | YES (cc) | in talks | — | No |
| F29 PXLite alias | PXLite fund thread is T-accelerate | frederick.stone@harmonygames.co/1843978997950200606 | YES (cc) | one row, not two | alias | No |
| F30 Karthic contact | T-Accelerate Capital (PXLite fund) | 5d0e8b31f7a29c64e1b0d3a8 | YES (unscoped) | confirms the alias | — | No |
| F31 Robert's send-to-everyone mail | send the Q4 update to everyone on the 2025 list | frederick.stone@harmonygames.co/1844623441920000059 | YES (To) | distractor; withdrawn by F1 | — | No |
| F32 Arthur's aside | just use who Leonard emailed this month | C07C2866011/1759168800.117903 | YES (member) | distractor; the doc's rules override it | — | No |
| F33 1AM Gaming note | 1AM Gaming is the March Gaming Fund row; they passed (Sep 8) | C096HFA5Z8W/1757365500.384216 | YES (member) | ties the 1AM no (frederick.stone@harmonygames.co/1842278301421016623) to the list row | the list still says March Gaming Fund | No |
| F34 Play Ventures correction | the Sep 15 no was their reply to Griffin; still their no (Sep 25) | C096HFA5Z8W/1758817200.730591 | YES (member) | overturns "they didn't respond" (C096HFA5Z8W/1758671737.632949) | agents stop at the Sep 23 post | No |
| F35 Mattel note | RFP and partnership only, not pitched the bridge (Sep 26) | C096HFA5Z8W/1758927000.205874 | YES (member) | overturns "Reached out to … Mattel" (C096HFA5Z8W/1756941551.539229) | partnership vs bridge outreach | No |
| F36 Treo VC post | Treo pinged Leonard on LinkedIn on Sep 3; deck and blurb sent | C096HFA5Z8W/1756942260.617302 | YES (member) | dates the Treo contact to the kickoff day (vs the Sep 2 warm-ups, C096HFA5Z8W/1756851039.800009) | spelled Treeo in the Sep 3 list | No |
| F37 Initial Capital post | Leonard pinged them on LinkedIn about the bridge; they won't lead, might write a small check (Sep 9) | C096HFA5Z8W/1757442000.492583 | YES (member) | backs the list's 09/11 note (f_48247af79428823c3cac92) with our outreach | no amount, so not soft-circled | No |
| F42 Q4 send rule | a checklist per other group next to Keep warm, one item per firm or angel; an "F/up with" card in To Do for everyone In talks or Awaiting reply; comment on an existing To Do card instead; none for anyone with a call or meeting on Fred's calendar after Sep 30 (Sep 29) | 68db03b86054eff7e8e92474 on 68c5a49e8491a9d7faf869d0 | YES (unscoped) | authority H2 (with F21) | the second comment on the card | No (the card is named) |
| F43 Anel To Do card | "F/up with Anel after the engine deep dive", open in To Do since Sep 16 | 68c99e98737744bd966aed24 | YES (unscoped) | NCsoft's existing card (DUP) | names the partner's first name only | No |
| F44 NCsoft partner | Anel Ceman, NCsoft row; Latest Status: follow-up engine conversation | f_48247af79428823c3cac92 | YES (shared) | maps F43 to NCsoft | Partner column, one of 17 | No |
| F45 Makers call | "Michael Cheung and Leonard Hayes", Wed Oct 8 9:00am PT (booked Sep 29; invitation frederick.stone@harmonygames.co/1844620925337600069) | evt_6b2e94d0c17a3f58e9d2b1 | YES (own calendar, INBOX) | no follow-up card for Makers Fund (BOOKED); Makers stays Awaiting reply | after the Sep 3 - Oct 1 window; names only the partner | No |
| F47 Makers partner | Michael Cheung, Makers Fund row ("Reached out - no response as of 09/11") | f_48247af79428823c3cac92 | YES (shared) | maps F45 to Makers Fund | Partner column | No |
| F46 Dentsu meeting | Harmony Games & Dentsu, Wed Oct 1 1:30pm PT (base, made Sep 30 PT) | evt_3671b9a924ccba550e51fa | YES (own calendar) | no follow-up card for Dentsu (BOOKED) | Leonard's hub names "the Dentsu meeting" | No |

## 5a · Search-as-persona proof

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
{{SEARCH_ROWS}}

The id column carries the deciding record; for base records the Found cell gives its rank in the pasted hit list (persona_view lists oldest first, so the newest thread sits last). `persona_view.py search` reads only the base export, so seeded rows return 0 there; the seeded count is a case-insensitive scan of the rev6 SQL rows Frederick can see (own mailbox and calendar copies, #executives, #bridge-pitch, #zombie-match3d and his DM with Leonard, files he owns or is shared on; Trello, Linear and Contacts unscoped), and seeded reach is the dossier's check-sql PASS for frederick_stone (§1.E). Queries are what Frederick would type after reading the hub and the records it leads to: the firm or person name from the list, the token name on a calendar invite, or the doc or card name the hub gives. No fact is NO, so nothing is routed.

```
{{SEARCH_OUT}}
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| send list membership (V1) | hub + send-list doc | deliverable: the send list, by pointing at Leonard's email | frederick.stone@harmonygames.co/1844724419788800011 · To Frederick · the only mail with that subject · states the job, names no firm | gotcha → trigger via the hub |
| groups (ST1–ST5, G1, G2) | send-list doc f_3b9e61c04d7a52e8f1a6c2 and Leonard's signed note C07C2866011/1758911700.336170 | scope: Leonard's ask (the doc incorporated by the hub; the note by the doc) | f_3b9e61c04d7a52e8f1a6c2 · shared · one Q4 doc, the Q3 one dated in its body · definitions only | gotcha → trigger via the hub |
| amounts (M1, M3) | send-list doc ("Put the amount on their row") | scope, via the hub | f_3b9e61c04d7a52e8f1a6c2 · as above · no amount | gotcha → trigger via the hub |
| build access (AC1–AC2) | send-list doc Build access + ZOM-567 + Arthur's post C0880U9751A/1759274400.518306 | scope, via the hub | f_3b9e61c04d7a52e8f1a6c2 · as above · "whether they can get the current internal build", "Arthur tracks the tester adds", no firm | gotcha → trigger via the hub |
| destination and name (DL1) | hub + README f_c61a0e93b7d24f58a2e917 | destination: the Q4 2025 investor update folder, named in the prompt | f_c61a0e93b7d24f58a2e917 · in Frederick's folder · one README there · naming pattern only | the prompt names the folder |
| send checklists (CL1) and follow-up cards (FU1–FU3, AN1) | card comments 68c64270d660c977c4696986 and 68db03b86054eff7e8e92474 | destination + constraint: the Existing Investor Update card, named in the prompt "do what he asked"; the rules stay in its comments | 68c5a49e8491a9d7faf869d0 · Trello unscoped · one "Existing Investor Update" card (decoy "Investor Update" 663ea0fc3f231e879cefd5e8) · rules, no firm | gotcha → trigger via the hub |
| reply counts (RP1–RP3) | hub ("reply here with how many firms and angels are in each group") | deliverable + recipient: the reply on Leonard's thread with how many firms and angels are in each group | frederick.stone@harmonygames.co/1844724419788800011 · as above · names the counts, no values | the prompt names the reply and its contents |
| not everyone on the 2025 list | Robert's mail frederick.stone@harmonygames.co/1844623441920000059, withdrawn in the hub | none | the hub's "Let's not" | inferable from the hub; listing everyone is a wrong write, not a graded positive |

| Anchor | May be named (noun phrases only) |
|---|---|
| A1 | Leonard's Q4 update email; the send list ask |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| clock and persona today | Wed Oct 1, 2025 00:00 PT (07:00 UTC) | Working_Files/00_Task_Context.json /universe/clock_utc | constraint |
| seed bound | 2025-10-01T00:00:00Z (Tue Sep 30, 5:00pm PT) | Working_Files/00_Task_Context.json /freeze_utc | constraint |
| Leonard's ask sent | Tue Sep 30, 2025 2:05pm PT (21:05Z); "yesterday" from Frederick's Oct 1 | frederick.stone@harmonygames.co/1844724419788800011 | past |
| Leonard travels | Wed Oct 1 morning ("flying to LA tomorrow morning") | frederick.stone@harmonygames.co/1844724419788800011 | today; not yet done at the clock |
| groups as-of | end of day Tue Sep 30, 2025 PT (= Oct 1 07:00Z) | f_3b9e61c04d7a52e8f1a6c2 | past |
| bridge kickoff | Wed Sep 3, 2025 | f_3b9e61c04d7a52e8f1a6c2, frederick.stone@harmonygames.co/1844724419788800011 | past |
| review with Leonard | Mon Oct 6, 2025 2:00–2:45pm PT (21:00Z) | evt_9c41e7a2d05b38f6e1a7c4 | deadline |
| board meeting | Tue Oct 14, 2025 | evt_bd61f3209523d19fdd6ba2 | future |
| Homa call | Thu Sep 18, 2025 8:00am PT | evt_89381fe5a15b802c5652a9 | past |
| Hiro call | Tue Sep 23, 2025 9:00am PT (16:00Z) | evt_7d3e19b04a6c25f8e1b9a0 | past |
| Anton down to 25 (Leonard's DM) | Wed Sep 24, 2025 16:25Z (9:25am PT) | D05S58U4SAK/1758731100.281734 | past |
| Brightwater call | Thu Sep 25, 2025 8:30am PT (15:30Z) | evt_2f86b0d4c9e17a35b64e0d | past |
| Edith's pass | Fri Sep 26, 2025 09:40Z (2:40am PT) | frederick.stone@harmonygames.co/1844318935449600041 | past |
| Dentsu "invites out" | Fri Sep 26, 2025 17:20Z | frederick.stone@harmonygames.co/1844294398771200045 | past |
| Anton's SAFE Completed | Fri Sep 26, 2025 19:02Z (12:02pm PT) | frederick.stone@harmonygames.co/1844354293432320031 | past |
| "Anton signed the 25 one" (DM) | Fri Sep 26, 2025 19:15Z | D05S58U4SAK/1758914100.640218 | past |
| Leonard's what-counts-as-signed note | Fri Sep 26, 2025 18:35Z | C07C2866011/1758911700.336170 | past |
| Paul's nudge | Mon Sep 29, 2025 15:00Z | frederick.stone@harmonygames.co/1844610859008000037 | past |
| ZOM-567 adds logged for NCsoft and Brightwater (rev12) | Tue Sep 30, 2025 10:45 and 11:05am PT (17:45Z, 18:05Z) | lc_4369758f577612cdb63b3457, lc_5e2ff140afff06e3a78e2fe1 | past |
| Paul backs out, to Leonard only (rev11) | Tue Sep 30, 2025 7:55am PT (14:55Z) | relayed in D05S58U4SAK/1759251900.863415 (Paul's mail sits in Leonard's mailbox only) | past |
| Leonard: "Paul's out" (1:1 DM with Frederick, rev12) | Tue Sep 30, 2025 10:05am PT (17:05Z) | D05S58U4SAK/1759251900.863415 | past |
| Arthur: the investor tester list was never attached (root post, rev12) | Tue Sep 30, 2025 4:20pm PT (23:20Z) | C0880U9751A/1759274400.518306 | past (the fix is after the as-of) |
| Sciplay pass written | Tue Sep 30, 2025 9:06am PT (16:06Z) | C07C2866011/1759248360.377105 | past |
| ZOM-567 comments | Tue Sep 30, 2025 17:25Z and 18:40Z | ZOM-567 | past |
| Arthur: Play group not attached (thread reply under the 0.3.49 post, rev10) | Tue Sep 30, 2025 4:20pm PT (23:20Z); Arthur attaches it with tomorrow's (Oct 1) build; Leonard's reply 4:48pm PT | C0880U9751A/1759274400.518306, C0880U9751A/1759276080.094417 | past (the fix is after the as-of) |
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
| Dynamic change | yes | yes | corrections met second, each in a different container from the claim (rev6): C07C2866011/1758303600.418207 and f_6e1d93a0c4b72f85d39a0e → D05S58U4SAK/1758731100.281734; ZOM-567 and frederick.stone@harmonygames.co/1844294398771200045 → C0880U9751A/1759274400.518306; frederick.stone@harmonygames.co/1842285743246816270 → C07C2866011/1759248360.377105 | the prompt names neither the first claim nor its correction; the reason to check ("the board will ask what's actually committed") is in the hub |
| Multi-source | yes | yes | 10 services (§1) | only the hub (A1) and the two destinations (the folder, the Existing Investor Update card) are named |
| Async | no | no | 03_Error_Async_Config.txt (Friction: none) | nothing to mention |
| Error recovery | no | no | 03_Error_Async_Config.txt | nothing to mention |
| Access control | no designed denial | no | every deciding record has a Frederick copy (01_Grounding_Dossier.md §1.E) | no ask about a restriction |

## 9 · Must not appear in the prompt

- Catalog tool names and parameters (Evals tool catalog): gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, trello_create_checklist, trello_create_check_item, trello_get_comments, gmail_reply_to_message, gmail_search_messages, slack search or history calls, linear_list_comments, contacts_search_contacts, gslides_get_presentation_text, any fileId or newParentId.
- MCP server names, "server", "connector", "the X tool".
- Opaque ids and filenames (01_Grounding_Dossier.md): every id in §5 (thread and message ids, f_/d_/evt_ ids, Trello and contact ids, ZOM-567, Slack timestamps), the Bridge angels sheet, the deck title.
- Findings and the root cause (dossier "Constraints for the prompt brief"): any firm name (Sciplay, Hiro Capital, Homa, Brightwater Games Fund, London Venture Partners, Dentsu Ventures, T-accelerate, PXLite, Andreessen Horowitz, GFR Fund, NCsoft), any person met during research (Edith Vane, Ilse Marrow, Karthic, Paul Heydon, Anton Bernstein, Ryo-san), any amount ($25K, $40K, $50K, totals), any count (79, 77, 80, "three numbers"), any status or group name (New investor, In talks, Awaiting reply, Keep warm), "keep warm", DocuSign, TestFlight or Play track state, Robert's board idea, Arthur's aside, Leonard's DM, Robert's #executives reply, Arthur's #zombie-match3d post, Slack DMs or threads as places to look.
- Rules that live in records: the groups, the as-of time, who stays off, the new-investor and amount rules, the build-access rule (f_3b9e61c04d7a52e8f1a6c2); what counts as signed (C07C2866011/1758911700.336170); the README naming pattern (f_c61a0e93b7d24f58a2e917); the deck's bridge slide (f_a47d0e2c95b18f63e2c0d5); the card comment (68c64270d660c977c4696986). The prompt may say the reply gives how many firms and angels are in each group (Leonard's email says so); it must not name the groups or the counts.
- Allowed by name (destinations Frederick knows): the Q4 2025 investor update folder, a reply on Leonard's email, the Existing Investor Update card in Trello (Leonard's email names it, frederick.stone@harmonygames.co/1844724419788800011). The card's keep-warm rule and who qualifies stay out.
- Injected friction: none configured (03_Error_Async_Config.txt), so nothing to hide; no forced error or wait may be implied.
- Reference files: none; no `/app/artifact` path.
- Format: Markdown, numbered steps, a column list, a per-deliverable content list, "first … then … finally" sequencing, if / but-not / then-also chains.
- Hints aimed at the traps (prompt_qc_cases.json trap_hint_or_riddle): "some numbers may be stale", "check the replies", "watch for duplicates", "partners write from their own addresses", "not everyone is on the list", "Leonard's post may be out of date", "check the DMs", "check the thread replies", "the tester log may be out of date", "Anton changed his amount".
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
| Q4 investor update - send list | Q3 investor update - send list f_8d2c47a91e05b3f6d7c418 | "for the July update"; new investor = a yes with an amount | f_3b9e61c04d7a52e8f1a6c2 |
| Existing Investor Update card | Investor Update card 663ea0fc3f231e879cefd5e8 | no keep-warm rule | 68c5a49e8491a9d7faf869d0 |
| Harmony Games Q4 2025 update (draft) | earlier update decks (base Drive "Investor Updates", e.g. August Update) | older updates, not shared drafts | f_a47d0e2c95b18f63e2c0d5 |
| Hiro Capital (list row) | Edith Vane writing without the firm name | alias through Contacts | e3a91c07d5b48f26a0c7e314 |
| T-accelerate (list row) | PXLite / T-Accelerate Capital | same firm, one row | 5d0e8b31f7a29c64e1b0d3a8, frederick.stone@harmonygames.co/1843978997950200606 |
| Sciplay (list row) | SciPlay in mail | case only | frederick.stone@harmonygames.co/1842285743246816270 |
| Superplay (row 82) | Supercell contents (SC-34) | one row under either name | f_48247af79428823c3cac92 |
| Treo VC | "Treeo" Slack spelling | spelling only, not a duplicate | C096HFA5Z8W/1756941551.539229 |
| ZOM-567 | ENG-#### tickets (trap_catalog N-series) | ZOM is the game team's series | ZOM-567 |
| Marcus Bennett / Marcus Lee / Oscar Bennett | the known Marcus trap | no Marcus or Oscar in any touched record | marcus.bennett@harmonygames.co |

## 11 · Pre-submit checklist

- [ ] One ordinary request in Frederick's voice: a co-founder handing his assistant a job, clean spelling, no spec language
- [ ] No Markdown, no numbered steps, no list of groups or sheet contents (the doc holds them)
- [ ] Points at Leonard's Q4 update email (A1) as the source of the ask; names the Q4 2025 investor update folder, the Existing Investor Update card (Trello) and a reply on Leonard's thread; may mention Monday, Oct 6
- [ ] Every write is asked of the assistant ("can you …"); no "I'll reply to Leonard" beside the same ask
- [ ] Does not name the send-list doc, the list, the README, the deck, the angels sheet, Robert's mail or the ticket, and does not restate who goes on the card's checklist
- [ ] Nothing from §9: no firm, person found in research, amount, count, status, "keep warm", DocuSign, tester state or id
- [ ] No hint or riddle aimed at a trap; no hedge letting a record correct the prompt
- [ ] Dates true at the clock: Leonard's email is from Tue Sep 30; Monday's review is Oct 6; nothing after the clock described as done
- [ ] No tool, server or connector names
- [ ] 20–4,000 words; then `/create-prompt-writing check`

## 12 · Blockers and routed defects

| Item | Status | Locator |
|---|---|---|
| facts NO in §5a | none; nothing routed | §5a F1–F40 |
| platform /prompt of rev6 FAIL (STEP 0.6 dataset duplicate, 0.804 to another contributor's Oct 14 board pre-read task; every content dimension 5) | rev7 changes the job to the bridge part of the Q4 investor update send list with a new prompt (sha256 b5ea6f0ff28c); the similarity checker is not available locally, so the new prompt avoids the neighbours' core meaning (no board pre-read, fundraising section or status of every firm) | Platform_Report/prompt_report4 |
| platform Opus pre-check of rev5 FAIL (/hardness score 1, too easy) | rev6 moves INPUT, CORR and DONE2 off the paths that run swept and strips the template's resolver sentences; rev7 needs `/injection`, `/prompt`, a new pre-check and `/hardness` on SQL 69db98aed17f | Platform_Report/hardness_report1, Working_Files/01a_Hardening_Report.md |
| surface reply patterns | rev7 RP2/RP3 grade the In talks and Keep warm counts ("In talks … 8", "Keep warm … 3") | 01_Gradable_Surface.json RP2, RP3 |
| platform /prompt rev3 FAIL (UGT 2, Cross-Service Coherence 2) | settled in rev4 records; rev5 SQL 3ba2b413458f then passed `/prompt` (Platform_Report/prompt_report3) | Platform_Report/peompt_report1, 01_Grounding_Dossier.md "Platform /prompt review of rev3" |
| SC-33 watch (Acterra twice) | Acterra is not contacted, so it stays off the send list under either count | f_48247af79428823c3cac92, f_3b9e61c04d7a52e8f1a6c2 |
| facts UNVERIFIED | none | 01_Grounding_Dossier.md §1.E |

## 13 · Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`, rev7: the send-list job).** Phase 1: persona (§1.1) Frederick is the addressee of Leonard's ask and on every investor cc (§1); voice (§1.2) is judged against a co-founder only. Anti-patterns (§1.3): no command list, no bolt-ons (the checklist and the reply are both in Leonard's one ask, frederick.stone@harmonygames.co/1844724419788800011), no pre-solving (§9), no tool names (§9). Diversity (§1.4): three writes in Sheets/Drive, Trello and Gmail. Assignment and complexity (§1.5): Corporate Ops fundraising/board work, Retrieval stacked with analysis and actions; Ambiguity, Dynamic change and Multi-source load-bearing (§8). Phase 2: fair readings (§2.1) in §4b; feasibility (§2.2) every write in the catalog and every read YES (§5a); truthfulness (§2.3) the premises in §7; cross-service (§2.4) 10 services; investigation → action (§2.5) §3; clarity (§2.6) §4; contrived (§2.7) §9 and §11; today's date (§2.8) §7; originality (§2.9) no supplied sample, and the earlier Frederick task (account custody before layoffs, support/completed_tasks) shares only the persona. Phase 3: universe coherence rested on the rev5 `/injection` PASS (Platform_Report/injection_report5, SQL 3ba2b413458f); rev7 (SQL 69db98aed17f) needs its own `/injection` run, and the two blind sweeps (forks; seeded-vs-base coherence) run before it.

| Area | Counter-reading | Evidence | Resolution |
|---|---|---|---|
| Fair readings (C6) | Reading B (rev12): Paul Heydon is In talks at $50,000 (or a New investor), since Leonard's post says he "is in for $50K", the angels sheet lists him and the Sep 29 nudge shows only an unsigned SAFE | C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e, frederick.stone@harmonygames.co/1844610859008000037 vs Leonard's Sep 30 message in his 1:1 DM with Frederick, D05S58U4SAK/1759251900.863415 ("Paul's out ... can't put money in this year after all") | a later record by the same author settles it, read under the doc's rules (a no told to any of us is a pass; a pass with no call stays off): Paul is off the list |
| Fair readings (C6) | Reading B: a16z passed (the Speedrun forward), so it is Keep warm (interviewed) instead of In talks | frederick.stone@harmonygames.co/1844748127814183717 (Sep 30 8:21pm PT, inside the window) vs frederick.stone@harmonygames.co/1842277213140775733 | settled by the doc's accelerator rule (f_3b9e61c04d7a52e8f1a6c2): In talks, three keep-warm items |
| Fair readings (C6) | Reading B: Hiro Capital is Awaiting reply, as the list says, now that rev6 drops the template's partner-address sentence | f_48247af79428823c3cac92 "no response as of 09/11" vs frederick.stone@harmonygames.co/1844318935449600041 (cc Hiro's Investment Director PERSON_5282, "our games fund"), e3a91c07d5b48f26a0c7e314 (Partner, Hiro Capital) and the Sep 23 call evt_7d3e19b04a6c25f8e1b9a0 | a newer, dated record from a Hiro partner, copied to Hiro's own director, settles it without a rule: Passed |
| Fair readings (C6) | Reading B (rev6/rev7): Anton's amount is $40,000, since the post, the angels sheet and the Completed SAFE agree | C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e vs D05S58U4SAK/1758731100.281734 (Leonard voids the 40 SAFE, sends a new one at 25) and D05S58U4SAK/1758914100.640218 ("Anton signed the 25 one") | the signed SAFE is the 25 one by Leonard's own dated words: 25,000 |
| Fair readings (C6) | Reading B (rev6): T-accelerate, Dentsu, NCsoft and Brightwater have Android, because ZOM-567 logs the Play adds and base #executives shows the Play link | lc_94eb35d962cfbdd31e1bd496, lc_4369758f577612cdb63b3457, lc_5e2ff140afff06e3a78e2fe1, lc_b549f3057640a5eb08f7581e, C07C2866011/1758558621.032499 vs C0880U9751A/1759274400.518306 and C0880U9751A/1759276080.094417 | the template asks whether they "can get the current internal build"; Arthur, who keeps the log, posts that the investor tester list was never attached to the internal track, so nobody on it (he names all four) has android yet, "whatever the Linear log says"; he attaches it only with his Oct 1 push: iOS only for all four |
| Fair readings (C6) | Reading B (rev6): a no Robert heard by phone is not a pass, since the template no longer says phone passes count | C07C2866011/1759248360.377105 vs f_3b9e61c04d7a52e8f1a6c2 | the rev6 Passed rule ("they've told us no for this round") has no channel or writing condition, and SciPlay told Robert: Passed |
| Fair readings (C6) | Reading B (rev7): the send list should carry every name on the 2025 list (Robert's idea), or count Anton as In talks | frederick.stone@harmonygames.co/1844623441920000059; C07C2866011/1758911700.336170 | the hub withdraws Robert's idea and the doc lists who stays off; signed Anton is a New investor: New investor 1, In talks 8, Awaiting reply 14, Keep warm 3 |
| Fair readings (C6) | Reading B: reply-all to Robert and Arthur rather than to Leonard alone | hub cc list (frederick.stone@harmonygames.co/1844724419788800011) | same decision, thread and contents; both accepted (§4b D3) |
| Clarity (C7) | the prompt could leave the reply's channel open (Slack DM vs the email thread) | the hub says "reply here" (frederick.stone@harmonygames.co/1844724419788800011) | §11 box: the prompt names a reply on Leonard's email; check mode tests the real text |
| Clarity (C7) | "I'll write the update itself on the plane" in the hub could pull a run into drafting the update or editing the deck | the deck f_a47d0e2c95b18f63e2c0d5 is Leonard's draft; the hub asks only for the send list and the counts | no deck write or draft update in §4; doing either is unrequested, not a second fair reading |
| Incorporation (C8) | does Leonard's email hand over the answer? | it names the scope, the template, the card and the folder but no firm, status or amount (01_Grounding_Dossier.md Fact sheet, FACT CHECK PASS) | instructions, not answers (prompt-incorporation-v1 (d)) |
| Incorporation (C8) | the checklists and follow-up cards live only in Trello comments, so they would be untriggered requirements | the hub: "Then do what I put on the Existing Investor Update card in Trello." (frederick.stone@harmonygames.co/1844724419788800011) → 68c64270d660c977c4696986, 68db03b86054eff7e8e92474; the prompt: "do what he asked on the Existing Investor Update card in Trello" | incorporated through the hub and named by the prompt (§6) |
| Fair readings (C6) | Reading B (rev9): Homa's open base card "[USERNAME_34488] send material [PERSON_NAME_0854]" is an existing card, so Homa gets a comment, not a card | the card sits in Doing; 68db03b86054eff7e8e92474: "already has a card in To Do" | only To Do cards count: Homa gets a new card |
| Fair readings (C6) | Reading B (rev9): Makers' Oct 8 call makes Makers In talks | evt_6b2e94d0c17a3f58e9d2b1 vs the send-list doc's In talks ("we've had a call or meeting with them this round"), as of end of Sep 30 | the call is future at Sep 30: Makers stays Awaiting reply ("even if they've written back") and gets no card |
| Fair readings (C6) | Reading B (rev9): "F/up with Anel" is not about a send-list firm | 68c99e98737744bd966aed24 vs f_48247af79428823c3cac92 (NCsoft partner Anel Ceman; the engine follow-up) | the only Anel in the universe is NCsoft's partner: comment there, no NCsoft card |
| Truthfulness (C17) | a premise like "Leonard emailed me this morning" or "Leonard's in LA" would be false at the clock | sent 2025-09-30T21:05:00Z (frederick.stone@harmonygames.co/1844724419788800011); "flying to LA tomorrow morning" | §7 and §11: "yesterday" or "Tuesday"; "flying out today" |
| Truthfulness (C17) | calling the folder "the folder Leonard made" would be false | d_5e8a1c3f9b07d2e64a1b93 is owned by frederick.stone@harmonygames.co (check-sql YES) | the prompt says "my Q4 2025 investor update folder" |
| Feasibility / ACL (C18–C19) | the catalog cannot put a new sheet in a folder | gsheets_create_spreadsheet has no folder parameter; gdrive_move_file(fileId, newParentId) places it; Frederick owns d_5e8a1c3f9b07d2e64a1b93 | feasible in two calls; §4b accepts create-then-move |
| Feasibility / ACL (C18–C19) | the Sciplay pass is a thread reply that channel history omits, and Anton's amount sits in a DM | C07C2866011/1759248360.377105 under C07C2866011/1759196326.309469 (reply counters updated); D05S58U4SAK/1758731100.281734; search finds both (§5a F11, F6) | findable and visible to frederick_stone (check-sql YES) |
| Contrived (C15–C16) | naming the folder, the reply and Monday's review in one prompt reads as a spec sheet | Eval 1 §2.7; prompt_qc_cases.json hidden_destination | destinations the persona knows must be named; the contents stay in the template (§9) |
| Contrived (C15–C16) | leaving the Trello card unnamed ("the Trello follow-up he mentions") would hide a destination Frederick knows, and "for anyone who passed" would contradict the card's pitched-only rule | prompt_qc_cases.json K47-hidden-destination; card rule 68c64270d660c977c4696986 ("Email-only no's don't need it") | the prompt names the card and says "like he asks", leaving who qualifies to the card |
| Contrived (C15–C16) | a line like "some of Leonard's numbers might be old" would hint at the traps | prompt_qc_cases.json trap_hint_or_riddle | banned in §9; the hub's "the board will ask what's actually committed" is in the record |

Name-swap test: swapping Leonard for another founder breaks the task, since the hub, the send-list doc, the folder README and the card comments are Leonard's records (frederick.stone@harmonygames.co/1844724419788800011, f_c61a0e93b7d24f58a2e917, 68c64270d660c977c4696986), so the scenario rests on real records.

Re-verified this run: the hub, send-list doc, Q3 decoy, README, card comment, both ZOM-567 comments, the five rev6 Slack rows and Leonard's rev7 signed note read from the rev7 SQL rows (base_check.parse_sql); the 48 searches in §5a run with persona_view as frederick_stone; entity.py collisions and resolve; the groups, amounts and follow-up outcomes from solver/truth.json (rev12); write tool names and parameters from the Evals tool catalog; Pacific times computed from the UTC stamps.

Rev9 (from the rev8 baseline: 72.7 counted calls, about 82% pass): the prompt b5ea6f0ff28c is unchanged; the hub's Trello sentence and Leonard's Sep 29 card comment 68db03b86054eff7e8e92474 add D2's per-group checklists and D4's follow-up cards, settled by F42–F47 (truth f3dd0b9de6e2d3f8: 19 cards, a comment for NCsoft, none for Dentsu or Makers Fund).

Rev10 (from the rev9 `/hardness`, score 1: the Opus run found every trap): the prompt and every pinned value are unchanged. Arthur's Play correction (F39) is now a thread reply under Leonard's 0.3.49 iOS release post C0880U9751A/1759182908.627389, worded without tester, TestFlight or ZOM-567, and still found by searching Karthic, Dentsu or android. Paul's Sep 30 "Done, signed it last night" (F48) is the done claim on his thread; F7 (only Anton has a Completed notice) and F22 (Leonard's note) keep him In talks at $50,000.

Rev11 (from the rev10 baseline: six runs, 133 counted calls on average, 0 full passes, but runs 1, 3, 5 and 6 failed exactly the same values): the prompt is unchanged. Paul now backs out on Sep 30 (F48: Leonard's reply under his own angel post; Paul's mail went to Leonard only), so he is off the send list: 25 rows, In talks 7 firms and 0 angels, 25 checklist items, 18 follow-up cards. Arthur's answer to Karthic in the T-Accelerate thread (F49) is a second record that the investor Play tester list was never attached; F39 now covers the 3 Dentsu folks. Build access stays iOS only for both.

Rev12 (from the rev11 baseline: Paul and build access caught by every run, SciPlay missed by five of six, so one failure pattern held 83%): the prompt is unchanged. Leonard's "Paul's out" is now in his 1:1 DM with Frederick (F48, D05S58U4SAK/1759251900.863415); the angel post has no replies. The T-Accelerate mail replies are removed; Arthur's correction is a #zombie-match3d root post again (F39/F49, C0880U9751A/1759274400.518306) naming everyone on the investor tester list, and ZOM-567 logs NCsoft and Brightwater too, so four firms in talks are iOS only. Groups, counts, 25 checklist items and 18 cards are unchanged.

Unresolved: the platform similarity checker is not available locally; rev7's prompt cleared STEP 0.6 at 0.762 and the prompt text has not changed since. One rubric-stage note in §12 (the reply's group counts).
