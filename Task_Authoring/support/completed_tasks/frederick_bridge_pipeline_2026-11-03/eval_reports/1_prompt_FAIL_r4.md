# Prompt Quality Review (Eval 1)

## PROMPT EVALUATION REPORT

### Task: Fred takes over Leonard's fundraising section of the Oct 14 board pre-read: build the pipeline sheet in his Board - Oct 14 2025 folder, add the Keep warm checklist to the Existing Investor Update card, and reply on Leonard's thread with the slide numbers
### Assigned Persona: Frederick Stone - Co-founder
### Assigned Business Function: Executive
### Assigned Competency: Corporate Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Long Horizon tier, 100–500+ calls; not scored here)

## 1. Scope and inputs

| Item | Value |
|---|---|
| Mode | Chat review, attempt 6ae4e299a13034b7eb8305f8; static, SQL not executed |
| Review time | 2026-11-02 (actual) |
| Clock | 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `04_Prompt.txt` (revision 7; the upload `04_Prompt (4).txt` sent with this command is byte-identical), 513 bytes, SHA-256 `cecfad824fd8037af82be1f41d010c98f920db4cfe57c5087c056b7098ffed32` |
| Assignment | `00_Task_Assigned_Inputs.md`, SHA-256 `1d795090d3476539561f58917410dab7275f800863d3be3084150ecd9a383c37` (all five fields stated: Frederick Stone, Executive, Corporate Ops, Retrieval, long-horizon) |
| Injection SQL | `01_Universe_Inject.sql` (revision 11), 132,888 bytes, SHA-256 `8481894430080319e947ad672ca3cd9ddfd9e40af102edafed975e0aaadcc0be` |
| Error/async config, dynamic context, reference files | None supplied. The prompt references no attachment; every source is an environment record |
| Eval | `1_Prompt_Eval.md` SHA-256 `e0c364dccda17423ece700d9c4b852a2a04b199a96b42b044d2dc73e73bd6057`; deep_recheck.md `ec7832d95f6f2f93…`; scoring.json `c14873e614cdcda5…` |
| Eval version | task-quality-v1 / prompt-source-checks-v2 |
| Eval release SHA-256 | `a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225` |
| Reviewed prompt SHA-256 | `cecfad824fd8037af82be1f41d010c98f920db4cfe57c5087c056b7098ffed32` |
| Review context SHA-256 | `966b62629a0153afbf74ae1cd7a4122f080314da0baab6b7fe8a425a96807f92` |
| Prompt record SHA-256 | `e4c08850d41210c37cb97241ba6063989c51652e28266636ebce0297e550c0ff` |
| Evidence contract | `stage-evidence-v1`; authority contract `prompt-incorporation-v1` |

Input/authority issues: none. The prompt is unchanged since the last `/prompt` run (PASS 5 on SQL revision 9, `3ba2b413…`). This run reviews SQL revision 11. Per the Eval 0 diff, the changes that touch this prompt's answer are: the Oct 14 template's Passed rule (now "Passed: they've told us no for this round." with the phone-pass and partner-address sentences removed, and the "use the latest amount" sentence gone); Leonard's "drop notes from my phone calls" post removed; the Sciplay note moved to a Robert reply in #executives; two new Leonard→Fred DMs on Anton (25 not 40; signed); Fred's copy of Anton's "SAFE amount" email removed; the ZOM-567 Dentsu comment now says Play was added Sep 26; and a new #zombie-match3d thread in which Arthur says the Play investor tester list was never attached. Every finding that depends on those rows was checked again against the current SQL. Base files are byte-identical to the previous review (every base source hash re-verified), so base facts are reused where noted. The Eval release and Eval 1 file changed since the last run (new STEP 0.6 dataset-similarity gate), so every phase was re-scored under the current version. SQL comments (lines 1–4) are read as context only.

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`).
- Reviewed SQL sha256: `8481894430080319e947ad672ca3cd9ddfd9e40af102edafed975e0aaadcc0be` (`injection-static-v2`, reviewed 2026-11-02T09:48Z). Eval 0 verdict: PASS / COMPLETE (report SHA-256 `4f686c43a21f278ef70ad1043b37c9596bc7edd7535f6cfd4caecb83b0a8c9d2`).
- Eval 0 findings on records this prompt depends on: none. Remaining advisory (unchanged): four columns the unverified schema snapshot doesn't cover (`gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` / `.ordinal`, `linear.linear_comments.sequence`). It changes no value the answer is graded on, so it isn't scored. If the loader rejects one, the whole script rolls back.
- Static checks A–C (IDs, structure, chronology, mailbox copies, channel membership) are REUSED from that report under stage-evidence-v1: same SQL hash, same universe manifest, same schema snapshot and Eval 0 version.

### Dataset Similarity
- Library: 290 tasks (Enterprise Atlas - Commercial: L10 13, L11 3, L12 107, completed 167), built 2026-11-01T07:15Z, refreshed 2026-11-02T08:37Z, age 1.2 h at check time. Check saved for this exact prompt hash.
- The task details carry no task ID, so the check ran without `--task-id`. The likely-duplicate neighbour is a different task, not this task's own earlier version: its assignment is Finance / Analysis and synthesis, while this task is Corporate Ops / Retrieval. Task IDs are withheld in this report under portal policy.
- **Gate: FAIL (likely duplicate).** Originality — Dataset Duplicate, Major. Overall score capped at 2.

| Neighbour | Stage | Persona / competency / skill | Meaning | Wording | Tier | What the two prompts share |
|---|---|---|---|---|---|---|
| 1 | L12 | Frederick Stone / Finance / Analysis and synthesis | 0.804 | 0.034 | likely duplicate | Same premise: Leonard hands Fred the fundraising part of the Oct 14 board pre-read, with every firm on the 2025 investor list put into a status, and the counts and dollar totals reported back. It differs in where things go (it updates the list, writes the section in the pre-read doc, posts in #bridge-pitch and emails Leonard his follow-ups), but the scenario and the core deliverable are the same |
| 2 | completed | Frederick Stone / Corporate Ops / Actions | 0.729 | 0.000 | same scenario | Leonard hands the 2025 investor list to Fred before his LA trip, ahead of the Oct 14 board meeting; Fred reports the firms that said no |
| 3 | completed | Frederick Stone / Finance / Actions | 0.720 | 0.008 | same scenario | Bring the 2025 investor list up to date before the board meeting, from Leonard's #bridge-pitch request |

## 2. Checklist

| Item | Status |
|---|---|
| Intake: prompt + five assignment fields + injection answer | NEW, done (upload identical to saved revision 7; assignment and SQL reused) |
| STEP 0.5 injection gate | NEW: CURRENT, Eval 0 PASS reused |
| STEP 0.6 dataset similarity | NEW: FAIL, likely duplicate (0.804) |
| Phase 0.1 references (guide view, Eval 1, acl.md, roster, catalog, release snapshot, deep_recheck, known data issues) | NEW, done. Evals/Docs PDFs/XLSX were not re-extracted; scoring.json and the Eval 1 local overrides were used as the authority |
| Phase 0.2 universe exploration | NEW for every changed SQL row: #zombie-match3d membership (channels.json, Fred is a member) and its Sep 2025 export (no later attach message before the clock); #executives parent `99aa913348bb…` of the moved Sciplay reply; D05S58U4SAK membership (Fred and Leonard); investor list row 82 ("Superplay", Latest Status "Reached out - no response as of 09/11"). REUSED for unchanged base facts (list, calendar, other firm threads; base hashes verified) |
| Phase 1.1–1.5 | NEW, done |
| Phase 2.1 UGT (seven readings, record saved) | NEW |
| Phase 2.2–2.9 | NEW, done (2.9 N/A: no samples supplied) |
| Phase 3.1–3.2 | NEW, done; static integrity REUSED from Eval 0 |
| Phase 4 scoring | NEW, done |
| Phase 5 deep recheck P1–P4 | NEW, done (see Deep Recheck) |

## 3. Requirement ledger (`authority_contract: prompt-incorporation-v1`)

The prompt incorporates Leonard's Sep 30 email ("His email has what he wants", "like he asks"). The email points to four records: the board pre-read template, the README in the folder, the Existing Investor Update card and the Board Deck card. That chain is valid incorporation. Nothing else adds obligations.

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Build the sheet Leonard wants | Email (SQL L169): "every firm on the 2025 game investor list, plus anyone we've had a call with since the Sep 3 kickoff who isn't on it … One sheet, one row per firm … use the buckets and definitions in the board pre-read template". Template "Board pre-read - fundraising section (Oct 14)" (SQL L23). 2025 list ("Game Investor List - Harmony Games 2025", 80 rows, 77 distinct names) | Inbox → email → Drive search for template and list → per firm: Gmail, Calendar, #bridge-pitch / #executives / #zombie-match3d, Leonard's DM, Linear ZOM-567, Contacts, Bridge angels sheet | `gsheets_create_spreadsheet` (+ `gdrive_move_file`) or `gdrive_create_file` with `parentId`; `gsheets_values_update` / `gsheets_batch_update`; reads via `gmail_*`, `gcal_*`, `slack_*`, `linear_*`, `contacts_*`, `gdocs_*`, `gsheets_*` | Template, list, Bridge angels sheet and deck are shared with Fred; the email, DocuSign notice, investor threads and the speedrun-feedback forward are in his mailbox; the calls are on his calendar; he is a member of #bridge-pitch, #executives, #zombie-match3d and the D05S58U4SAK DM with Leonard; Linear, Trello and Contacts are unscoped | 79 rows (77 list names + Brightwater Games Fund + Homa), each with a status (Passed / In talks / Awaiting reply / Not contacted this round), build access for firms in talks (T-Accelerate iOS only, Dentsu iOS only, the rest none), committed and soft-circled amounts; totals at the bottom: committed $25,000, soft-circled $50,000 |
| Put it in "my Board - Oct 14 2025 folder", named per the README | Folder `d_5e8a1c3f9b07d2e64a1b93` (owner Fred, SQL L12); README (SQL L25): name = section name + " - Oct 14 board", example "Fundraising - Oct 14 board"; Google Sheets or Docs only | Drive search / folder listing | as above | Folder owned by Fred; README shared with him | Google Sheet "Fundraising - Oct 14 board" in that folder |
| Take care of the Existing Investor Update card as Leonard asks | Email: "Whatever the Existing Investor Update card says to do for firms that pass, do that too." Card 455 comment (SQL L132): Keep warm checklist, one item per firm that passed after a pitch call or meeting this round; "Email-only no's don't need it" | Trello search → card → comments | `trello_create_checklist`, `trello_create_check_item` | Trello unscoped | Keep warm checklist on card 455 with three items: London Venture Partners, Hiro Capital, Sciplay |
| Reply on the thread with the slide numbers | Email: "reply here with the numbers the fundraising slide needs". Board Deck card (idShort 456) comment (SQL L152): firm count (every row, angels included), total committed, total soft-circled | Trello card "Board Deck - Oct 14" → comment | `gmail_reply_to_message` (or `gmail_send_message` with `thread_id`) | Thread in Fred's mailbox | Reply to Leonard on "Oct 14 board pre-read - fundraising section": 79 firms, $25,000 committed, $50,000 soft-circled |
| Done before the Monday Oct 6 review | Calendar event, Oct 6 9am PT (SQL L308) | — | — | On Fred's calendar | Timing context, no extra write |
| Excluded by authority | Robert's idea of emailing the pipeline straight to the board is overruled in Leonard's email ("Let's not, it goes in the deck"). Arthur's #executives shortcut "just list who Leonard emailed this month" (SQL L108) is not incorporated. The July template ("for the Jul 16 board") is superseded by the Oct 14 one | — | — | — | No email to the board; no shortcut scope |

**Output capability.** Sheet creation, moving it to the folder, cell writes, checklist creation and the Gmail reply are all cataloged: SUPPORTED by catalog. No run shows the runtime behaviour of `gsheets_create_spreadsheet` + `gdrive_move_file`, and `/prompt` doesn't require one.

**Answer derivation (main session, for downstream reuse).** Status as of end of day Sep 30 PT, per the current template:

- **Passed (8):** Play Ventures (no sent to Griffin; Leonard's Sep 25 correction, SQL L116), March Gaming Fund (1AM Gaming's written no; SQL L114 maps the rename), [PERSON_NAME_5402] (Latest Status "They don't do bridge"), Grishin Robotics (#bridge-pitch Sep 8 "No, they want metrics"), Lakestar Ventures (Sep 4 email), London Venture Partners (Sep 25 written pass after the Sep 9 call), Hiro Capital (Edith Vane's Sep 26 pass after the Sep 23 call; Contacts maps her to Hiro), Sciplay (NEW location: Robert's #executives reply 2025-09-30 16:06Z, SQL L120, "Sciplay's out too. D called me this morning, they're passing on this round", after the Sep 15 meeting).
- **In talks (9):** Andreessen Horowitz (speedrun interview Sep 18; the Sep 30 speedrun rejection is the program's decision, which the template says isn't their bridge answer), NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Homa (added), Brightwater Games Fund (added), Anton Bernstein and Paul Heydon (angels who said yes). REUSED except where noted.
- **Awaiting reply:** the list names with bridge outreach since Sep 3 and no call, no no, including Initial Capital (Leonard's Sep 9 #bridge-pitch post) and Treo VC (Sep 3 "pinged me again … I sent them the deck"). REUSED.
- **Not contacted this round:** every other list name, Mattel included.
- **Build access (NEW):** T-Accelerate **iOS only** and Dentsu **iOS only**. ZOM-567 records Play internal track adds for both (Sep 22 and Sep 26), but Arthur's #zombie-match3d post at 2025-09-30 23:20Z (4:20pm PT, SQL L127) says "the investor tester list I made in the Play console never got attached to the internal testing track, so nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added. testflight is fine for all of them. I'll attach it when I push tomorrow's build". Arthur is the template's named tester authority, the post is later than both ZOM-567 comments, and the fix falls after the Sep 30 cutoff. The other firms in talks: none. Angels: blank.
- **Money (NEW sources):** Anton $25,000 committed: DocuSign Completed notice in Fred's mailbox Sep 26 19:02Z; Leonard's DMs to Fred, Sep 24 "he can only do 25 this time, not the 40. voiding his docusign and sending a new SAFE at 25 tonight" and Sep 26 19:15Z "Anton signed the 25 one". Paul $50,000 soft-circled (Leonard's #executives post and the Bridge angels sheet; the Sep 29 nudge shows it unsigned). Initial Capital's "small check" has no amount.

This derivation is evidence for later stages. It is not a rubric, and other wordings of the same values stay valid.

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Frederick Stone (`frederick_stone`, frederick.stone@harmonygames.co, Co-founder, Executive) matches the roster. He is a member of #bridge-pitch, #executives and #zombie-match3d, joins the investor calls (on his calendar), is cc'd on the investor threads and owns the Board - Oct 14 2025 folder. A co-founder taking over the fundraising section of a board pre-read from the CEO is plausible in role, authority and access.

| Check | Finding |
|---|---|
| Role plausibility | Yes: co-founder covering for the CEO on board materials |
| Voice match | Yes: short, plain delegation |
| Access plausibility | Yes: every required record is in his mailbox, calendar, channels, DM or shared Drive |
| Responsibility scope | Yes: prepare the section; Leonard stitches it into the deck |

**Assigned Competency (Corporate Ops):** PASS (5). Board pre-read materials are board work (board / legal / HR / vendor). The fundraising content doesn't make it a Finance model, budget or forecast task.

**Assigned Task Skill (Retrieval):** PASS (5). The work is finding, for 79 firms, the records that decide status, money and tester access across eight services, then writing the results down.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y: PASS
- Multi-Source: the template (Docs), the list (Sheets), Gmail, Calendar, Slack, Linear, Contacts and Trello each decide graded cells.
- Dynamic Change: Anton's $40K is replaced by $25K (Leonard's Sep 24 and Sep 26 DMs). ZOM-567's Play adds for T-Accelerate and Dentsu are overtaken by Arthur's Sep 30 #zombie-match3d note. Play Ventures' "didn't respond" is corrected on Sep 25. The July template is superseded. The Sep 30 a16z speedrun rejection is a late, tempting "no" the template rules out.
- Ambiguity: the file name comes from the README, the slide numbers from the Board Deck card and the Keep warm rule from the card comment, all named in Leonard's email.
- Data seeding: PASS. The prompt is a 4-sentence trigger; the operating rules live in seeded records.

**Naturalness:** PASS (5). First person, plain, uneven sentence lengths, no formatting or polished connectives, no deliverable spec. P4 agreed (no findings, 4 sentences checked).

| AI-text red flag | Found? |
|---|---|
| Document formatting | No |
| Polished connectives | No |
| Enumerated deliverable specs / preservation rules | No |
| Even, symmetric sentences | No |
| Staged errors | No |

**Anti-Patterns:**

| Pattern | Status |
|---|---|
| Command List | PASS: "and then reply" joins the last of three asks in one question and reflects a real dependency |
| Bolt-On | PASS: every clause serves the same handoff; the Oct 6 sentence is deadline context backed by the calendar invite |
| Pre-Solving | PASS: no status, firm, amount or count is given |
| Tool Mention | PASS: "Trello", "the sheet", "folder", "thread" are natural product words |

**Diversity:** a new spreadsheet in a named folder, a Trello checklist with items and an email reply, over a 79-firm cohort.

## Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every material fork is settled by a prompt-incorporated or Fred-visible record: a16z stays In talks (template: the speedrun decision and feedback aren't the bridge answer); T-Accelerate and Dentsu are iOS only (Arthur's Sep 30 \#zombie-match3d note overrides his ZOM-567 Play adds); Initial Capital is Awaiting reply (Leonard's Sep 9 \#bridge-pitch outreach); Homa is a row; Anton's committed amount is $25,000 (Leonard's Sep 24 and Sep 26 DMs); Sciplay is Passed (template Passed rule has no writing requirement). The firm count (79), totals ($25,000 / $50,000) and Keep warm set (London Venture Partners, Hiro Capital, Sciplay) each have one answer.

Alternative selection: B (a16z Passed) stays the strongest alternative: Fred's mailbox holds a real Sep 30 written rejection after the Sep 18 interview call, and it changes the Keep warm writes. C (ZOM-567 Play adds) is the new SQL's main trap; D, E, F and G cover Initial Capital, Homa, Anton's amount and Sciplay's phone no. The Deep Recheck fork list covers the rest.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Leading reading: 79 rows (77 list names + Brightwater Games Fund + Homa). Initial Capital = Awaiting reply (Leonard's Sep 9 bridge ping; their reply is not a no; no call). a16z = In talks (Sep 18 speedrun interview counts as a call; the Sep 30 speedrun rejection and feedback are not their bridge answer). Sciplay = Passed (Robert's Sep 30 note of their phone no). Build access: T-Accelerate iOS only and Dentsu iOS only (Arthur's Sep 30 4:20pm PT \#zombie-match3d note: the Play investor tester list was never attached, so nobody on it has Android, even though ZOM-567 shows them added). Keep warm: London Venture Partners, Hiro Capital, Sciplay. Committed $25,000 (Anton's signed SAFE at 25), soft-circled $50,000 (Paul). | a16z In talks; Initial Capital Awaiting reply; Sciplay Passed; T-Accelerate iOS only; Dentsu iOS only; Anton committed $25,000; Keep warm = LVP, Hiro Capital, Sciplay | Create the 'Fundraising - Oct 14 board' Google Sheet; add the Keep warm checklist to the Existing Investor Update card; reply on Leonard's Sep 30 thread | Board - Oct 14 2025 folder; Existing Investor Update card (455); Leonard's 'Oct 14 board pre-read - fundraising section' thread | 79 rows (T-Accelerate and Dentsu build access 'iOS only'); Keep warm checklist with 3 items (London Venture Partners, Hiro Capital, Sciplay); reply: 79 firms, $25,000 committed, $50,000 soft-circled | T19 (Evals/task\_inputs/01\_Universe\_Inject.sql): "the program''s decision and the feedback that comes with it aren''t their answer on the bridge; that has to come on our bridge thread with them or in \#bridge-pitch."; T9 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The interview counts as a call with that firm"; S7 (Evals/task\_inputs/01\_Universe\_Inject.sql): "pinged Initial Capital on LinkedIn about the bridge"; T13 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Arthur tracks the tester adds."; ZM1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added"; DM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anton signed the 25 one" |
| B | a16z's Sep 30 speedrun feedback ('it feels a little early for us to step in') is a written no after the Sep 18 interview call, so a16z is Passed and gets a Keep warm item (4 items). | a16z Passed; Initial Capital Awaiting reply; T-Accelerate and Dentsu iOS only; Keep warm = LVP, Hiro Capital, Sciplay, a16z | Create the 'Fundraising - Oct 14 board' Google Sheet; add the Keep warm checklist to the Existing Investor Update card; reply on Leonard's Sep 30 thread | Board - Oct 14 2025 folder; Existing Investor Update card (455); Leonard's 'Oct 14 board pre-read - fundraising section' thread | 79 rows; Keep warm checklist with 4 items (adds Andreessen Horowitz); reply: 79 firms, $25,000 committed, $50,000 soft-circled | A16Z1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "feels a little early for us to step in"; A16Z2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "decision not to include"; T4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed: they''ve told us no for this round."; TR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "goes on a Keep warm checklist on this card, one item per firm" |
| C | Arthur's ZOM-567 log, which the template names as the tester authority, records Play internal track adds for T-Accelerate (Sep 22) and Dentsu (Sep 26, 'investor tester list'), and Leonard told Dentsu on Sep 26 'Invites ... are out to all three of you', so both firms are iOS and Android. | a16z In talks; Initial Capital Awaiting reply; Sciplay Passed; T-Accelerate iOS and Android; Dentsu iOS and Android; Keep warm = LVP, Hiro Capital, Sciplay | Create the 'Fundraising - Oct 14 board' Google Sheet; add the Keep warm checklist to the Existing Investor Update card; reply on Leonard's Sep 30 thread | Board - Oct 14 2025 folder; Existing Investor Update card (455); Leonard's 'Oct 14 board pre-read - fundraising section' thread | 79 rows with T-Accelerate and Dentsu build access 'iOS and Android'; Keep warm 3 items; reply: 79 firms, $25,000 committed, $50,000 soft-circled | L2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "T-Accelerate (Karthic): TestFlight and Play internal track both added Sep 22."; L1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Play internal track added Sep 26 (investor tester list)"; D1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Invites for Zombie Match 3D are out to all three of you." |
| D | The list's Latest Status note for Initial Capital records their stance, not our outreach, so with no outreach since Sep 3 the row is Not contacted this round. | a16z In talks; Initial Capital Not contacted this round; T-Accelerate and Dentsu iOS only; Keep warm = LVP, Hiro Capital, Sciplay | Create the 'Fundraising - Oct 14 board' Google Sheet; add the Keep warm checklist to the Existing Investor Update card; reply on Leonard's Sep 30 thread | Board - Oct 14 2025 folder; Existing Investor Update card (455); Leonard's 'Oct 14 board pre-read - fundraising section' thread | 79 rows with Initial Capital 'Not contacted this round'; Keep warm 3 items; reply: 79 firms, $25,000 committed, $50,000 soft-circled | T6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Not contacted this round: nothing from us since Sep 3."; GS2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gsheets/data.json): "They won't lead - would potentially write a small check" |
| E | Homa is a co-dev/publishing conversation, not investment talks, so it is left off; 78 rows. | Homa excluded; a16z In talks; Initial Capital Awaiting reply; T-Accelerate and Dentsu iOS only; Keep warm = LVP, Hiro Capital, Sciplay | Create the 'Fundraising - Oct 14 board' Google Sheet; add the Keep warm checklist to the Existing Investor Update card; reply on Leonard's Sep 30 thread | Board - Oct 14 2025 folder; Existing Investor Update card (455); Leonard's 'Oct 14 board pre-read - fundraising section' thread | 78 rows; Keep warm 3 items; reply: 78 firms, $25,000 committed, $50,000 soft-circled | BP6 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C096HFA5Z8W/2025-09.json): "I think we should focus Homa on the co-dev investment path."; HOMA2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "We are also considering publishing opportunities"; T3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Service or work-for-hire deals, banks (our SVB catch-ups), RFPs, publishing-only talks and calls with other engine companies" |
| F | Anton's committed amount is the $40K Leonard posted in \#executives on Sep 19; his DocuSign Completed notice is in, so committed = $40,000. | Anton committed $40,000; other statuses as Reading A | Create the 'Fundraising - Oct 14 board' Google Sheet; add the Keep warm checklist to the Existing Investor Update card; reply on Leonard's Sep 30 thread | Board - Oct 14 2025 folder; Existing Investor Update card (455); Leonard's 'Oct 14 board pre-read - fundraising section' thread | 79 rows; Anton committed $40,000; Keep warm 3 items; reply: 79 firms, $40,000 committed, $50,000 soft-circled | M3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE."; M2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "All signers completed Complete with docusign: Harmony Games SAFE - Anton Bernstein.pdf" |
| G | Sciplay's no reached us only by phone (Robert's Slack note), and the template treats list notes as written answers, so a phone no isn't a Passed; Sciplay stays In talks after the Sep 15 meeting and gets no Keep warm item (2 items). | Sciplay In talks; Keep warm = LVP, Hiro Capital | Create the 'Fundraising - Oct 14 board' Google Sheet; add the Keep warm checklist to the Existing Investor Update card; reply on Leonard's Sep 30 thread | Board - Oct 14 2025 folder; Existing Investor Update card (455); Leonard's 'Oct 14 board pre-read - fundraising section' thread | 79 rows with Sciplay 'In talks'; Keep warm checklist with 2 items (London Venture Partners, Hiro Capital); reply: 79 firms, $25,000 committed, $50,000 soft-circled | SC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round" |

Explicit option inventory: The prompt lists three asks, not alternative options; it offers no candidate choices.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "Leonard emailed me on Sep 30 asking me to own the fundraising section of the Oct 14 board pre-read since he's flying to LA today, and I'd like you to take it on for me. His email has what he wants. Can you build the sheet and put it in my Board - Oct 14 2025 folder, take care of the Existing Investor Update card in Trello like he asks, and then reply to him on that thread with the numbers he needs for the slide? I'm going through it with him at the review on Monday, Oct 6, so it needs to be done before then."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Authority and source identity: the prompt incorporates Leonard's email, which tells Fred to use the buckets and definitions in the Oct 14 template; the template says an accelerator program's decision and its feedback are not the firm's bridge answer, which has to come on our bridge thread or in \#bridge-pitch. The Sep 30 mail is the speedrun decision and its feedback (subject 'Speedrun feedback'), not the Sep 3 bridge thread, whose last message is Leonard's Sep 12 note; \#bridge-pitch has no a16z no (Sep 28 Leonard only notes others announcing acceptance).
Resolution evidence: T19 (Evals/task\_inputs/01\_Universe\_Inject.sql): "the program''s decision and the feedback that comes with it aren''t their answer on the bridge; that has to come on our bridge thread with them or in \#bridge-pitch."; A16Z2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "decision not to include"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | a16z In talks vs Passed. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Keep warm has 3 vs 4 items; a16z status cell differs. |

Authority chain: P → EM9 → T19

Resolution relevance challenge: T19 names exactly this case: the speedrun decision and the feedback that comes with it. It rules out treating 'a little early for us to step in' as the bridge no.
Delegation challenge: NOT_CLAIMED. The template sets one status; no choice is delegated.
Challenge evidence: T19 (Evals/task\_inputs/01\_Universe\_Inject.sql): "the program''s decision and the feedback that comes with it aren''t their answer on the bridge"

Compared alternative: C
Resolution: EXCLUDED. Newer source, same authority and scope: the template says Arthur tracks the tester adds. Arthur's own \#zombie-match3d note (Sep 30 4:20pm PT, after both ZOM-567 comments at 10:25am and 11:40am PT and after Leonard's Sep 26 reply) says the Play investor tester list never got attached, so nobody on it has Android, naming Karthic (T-Accelerate) and the 3 Dentsu folks, 'even though ZOM-567 has them as added'. He plans to attach it with Oct 1's build, after the Sep 30 PT status cutoff. Fred is a member of \#zombie-match3d.
Resolution evidence: T13 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Arthur tracks the tester adds."; ZM1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added"; ZM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "I''ll attach it when I push tomorrow''s build"; T17 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Status, as of end of day Tue Sep 30 (Pacific)"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | T-Accelerate and Dentsu iOS only vs iOS and Android. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Two build-access cells differ. |

Authority chain: P → EM9 → T13

Resolution relevance challenge: ZM1 is the template's named tester authority correcting his own ZOM-567 entries for exactly these two firms, later the same day, and ZM2 dates the fix after the cutoff.
Delegation challenge: NOT_CLAIMED. One build-access value per firm.
Challenge evidence: ZM1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "even though ZOM-567 has them as added"

Compared alternative: D
Resolution: EXCLUDED. Newer/direct source: Leonard's Sep 9 \#bridge-pitch post records our own bridge outreach to Initial Capital after the Sep 3 kickoff, so 'nothing from us since Sep 3' is false for them; their reply is not a no and there is no call, which is Awaiting reply.
Resolution evidence: S7 (Evals/task\_inputs/01\_Universe\_Inject.sql): "pinged Initial Capital on LinkedIn about the bridge, they wrote back that they won''t lead but might write a small check"; T5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Awaiting reply: we reached out this round, no call yet and no no"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Initial Capital Awaiting reply vs Not contacted this round. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Initial Capital status cell differs. |

Authority chain: P → EM9 → T5

Resolution relevance challenge: S7 is a dated (2025-09-09) Fred-visible record of outreach 'about the bridge', the exact fact Reading D denies.
Delegation challenge: NOT_CLAIMED. One status per firm.
Challenge evidence: S7 (Evals/task\_inputs/01\_Universe\_Inject.sql): "pinged Initial Capital on LinkedIn about the bridge"

Compared alternative: E
Resolution: EXCLUDED. Source identity and authority: the incorporated Oct 14 template admits a strategic who was pitched an investment alongside co-dev even when publishing was also discussed; Leonard's email before the Sep 18 call pitches seed-extension funding, so the talk was not publishing-only. Fred's 'co-dev investment path' still names an investment path.
Resolution evidence: T2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "if we pitched them the bridge or an investment alongside a co-dev deal, they count even when co-dev or publishing was on the table too."; HOMA1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "we are currently seeking extension funding on our seed round"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Include vs exclude Homa. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | 79 vs 78 rows and firm count. |

Authority chain: P → EM9 → T2

Resolution relevance challenge: The template sentence addresses exactly a mixed co-dev/publishing plus investment pitch, and the Homa email shows the investment pitch.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted.
Challenge evidence: T2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "if we pitched them the bridge or an investment alongside a co-dev deal, they count even when co-dev or publishing was on the table too."

Compared alternative: F
Resolution: EXCLUDED. Newer source: Leonard's Sep 24 DM to Fred says Anton can only do 25, not the 40, and that the $40K DocuSign is voided and a new SAFE at 25 sent; his Sep 26 DM, 13 minutes after the DocuSign Completed notice, says 'Anton signed the 25 one'. The template counts a signed SAFE as committed.
Resolution evidence: DM1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "he can only do 25 this time, not the 40. voiding his docusign and sending a new SAFE at 25 tonight"; DM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anton signed the 25 one"; T10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Committed: signed SAFE only, meaning the DocuSign Completed notice is in."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Anton $25,000 vs $40,000 committed. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Anton committed cell and the committed total in the sheet and the reply differ. |

Authority chain: P → EM9 → T10

Resolution relevance challenge: DM1 and DM2 are Fred-visible, dated after M3, and name the voided $40K SAFE and the signed $25K one, the exact fact Reading F relies on.
Delegation challenge: NOT_CLAIMED. One committed figure.
Challenge evidence: DM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anton signed the 25 one"

Compared alternative: G
Resolution: EXCLUDED. Authority: the incorporated template defines Passed as 'they've told us no for this round' with no writing requirement; the 'count as written' line only lets the list's Latest Status notes stand as answers. Robert's Sep 30 \#executives note records Sciplay telling him by phone that they're passing on this round, so Sciplay is Passed, and after the Sep 15 meeting it is not an email-only no, so it gets a Keep warm item.
Resolution evidence: T4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed: they''ve told us no for this round."; SC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round"; TR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "goes on a Keep warm checklist on this card, one item per firm, so they get the Q4 update with the rest."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Sciplay Passed vs In talks. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Sciplay status cell and the Keep warm item count differ (3 vs 2). |

Authority chain: P → EM9 → T4

Resolution relevance challenge: T4 is the template's Passed rule itself; it requires a no for this round, which SC1 records, and nothing in the template requires the no to be in writing.
Delegation challenge: NOT_CLAIMED. One status per firm.
Challenge evidence: T4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed: they''ve told us no for this round."

Strongest-alternative challenge (B): Not a strawman: the forward is in Fred's mailbox before the clock, comes from the same a16z partner Leonard pitched the bridge to on Sep 3, and reads as a decline; without T19 it would be a written no after a call.
Challenge evidence: A16Z1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "feels a little early for us to step in"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5). Every ask maps to a cataloged write and every needed fact exists in a record Fred can open. Status, build access and money are columns the template defines and the records fill. No exact-precision ask beyond whole-dollar amounts. Snowflake and Confluence aren't used.

| Ask | Capability | Tools | Feasible? |
|---|---|---|---|
| Read list, template, README, cards, mail, calendar, Slack, Linear, Contacts | Read | gsheets/gdocs/gdrive/trello/gmail/gcal/slack/linear/contacts reads | Yes |
| Create the Google Sheet in the folder and fill it | Create + move + write | `gsheets_create_spreadsheet`, `gdrive_move_file` / `gdrive_create_file(parentId)`, `gsheets_values_update` | Yes (catalog) |
| Keep warm checklist with one item per firm | Write | `trello_create_checklist`, `trello_create_check_item` | Yes |
| Reply on Leonard's thread | Write | `gmail_reply_to_message` | Yes |

**Persona ACL Reachability:** PASS (5). Scoped reads (Gmail, Slack, GCal, Drive family) are visible to Fred: his mailbox (Leonard's email, DocuSign notice, Paul nudge, Hiro and Brightwater threads, Dentsu thread, speedrun-feedback forward), his calendar, the channels he belongs to (#bridge-pitch `C096HFA5Z8W`, #executives `C07C2866011`, and #zombie-match3d `C0880U9751A`, where channels.json lists `EMPLOYEE_0008_SLACK_ID` among 25 members), the DM `D05S58U4SAK` (members include Fred and Leonard) and Drive files he owns or that are shared with him. Each new SQL Slack author is a member of the channel it posts in (Eval 0 check A). Linear, Trello and Contacts are unscoped. Fred's copy of Anton's "SAFE amount" email was removed in this revision; the amount change now reaches him through Leonard's DM, so nothing the answer needs is hidden.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5). The write set is the same under every reading: one sheet in the named folder, one checklist on the named card, one reply on the named thread. "I'm going through it with him" is Fred's own meeting, not a competing write. Robert's request to email the board is declined in the email the prompt incorporates.

**Contrived / Unnatural:** PASS (5). No timestamps, opaque ids, generated filenames, trap hints, hidden destinations (the folder, card and thread are all named), audit-form wording or if-chains.

**Alignment with Today's Date:** PASS (5). "Today" is Wed Oct 1, 2025, and Leonard's Sep 30 email says "flying to LA tomorrow morning". "Monday, Oct 6" is a Monday and the review is a future meeting on Fred's calendar. Status is "as of end of day Tue Sep 30 (Pacific)", before the clock. Arthur's #zombie-match3d note (4:20pm PT Sep 30) and Robert's Sciplay note (9:06am PT Sep 30) fall inside the window; Arthur's planned attach ("tomorrow's build") falls after it.

**Originality / Sample Similarity (Phase 2.9):** N/A: no comparison samples supplied. The dataset-similarity gate (STEP 0.6) is separate and FAILs (see Dataset Similarity).

**Truthfulness:** PASS (5). All 9 premises verified (record saved): the email (Sep 30, 2:05pm PT, SQL L169) and its asks; the LA trip; the folder (owned by Fred); the Existing Investor Update card (base card 455); "like he asks"; the thread and the numbers; the Oct 6 review (SQL L308). The SQL rows behind them are unchanged in revision 11 apart from line shifts.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact. Drop Gmail and the DocuSign Completed notice, Hiro's and Lakestar's passes and the reply are lost. Drop Calendar and the In talks set and the two added firms are lost. Drop Slack and Anton's $25K (DMs), Paul's $50K, Sciplay's pass and the Android correction for T-Accelerate and Dentsu are lost. Trello supplies the Keep warm rule and the slide numbers; Sheets/Docs the cohort and the rules; Contacts maps Edith Vane to Hiro Capital.

**Investigation + Action:** PASS (5). Three writes (sheet, checklist, reply), each fed by the investigation.

**Coherence (Bolt-on):** PASS (5). One workflow: build the section, act on the passes, report the numbers.

**Business Function (Executive):** PASS (5). Board pre-read and fundraising pipeline are founder/exec work.

## Phase 3: Universe Feasibility

**Data Existence:** PASS (5)
- Entities verified: the list names, the investor calls on Fred's calendar since Sep 3, the template, README, folder, both cards, the email thread, DocuSign notice, Bridge angels sheet, ZOM-567 and its two comments, Leonard's two DMs, Robert's Sciplay reply, Arthur's #zombie-match3d thread, the Initial Capital post and the Contacts rows.
- All retrievable via cataloged reads: Yes.

**Cross-Service Coherence:** PASS (5)
- Inconsistencies in task-touched data: none. ZOM-567's two comments (2025-09-30 17:25Z and 18:40Z) say Play internal track adds landed for T-Accelerate (Sep 22) and Dentsu (Sep 26). Arthur's later #zombie-match3d post (23:20Z) names that exact gap ("even though ZOM-567 has them as added") and explains it: the Play tester list was never attached to the track. That is an in-world correction by the same person, not a data contradiction. It also fits the base records: Arthur's #executives Sep 22 "Invites sent" and his #bridge-pitch Sep 24 "I have to add them by email for google play to work". Leonard's reply ("ping me when it's live so I can tell Karthic and Ryo-san") matches the Ryo Ishikawa and Karthic R contacts.
- Anton: Leonard's #executives Sep 19 "$40K", the Sep 24 DM (25 not 40, docusign voided), the DocuSign Completed notice (Sep 26 19:02Z) and "Anton signed the 25 one" (19:15Z) form one consistent timeline. Leonard's own copy of Anton's Sep 24 email (16:10Z) precedes the DM (16:25Z).
- The moved Sciplay reply hangs off base #executives message `99aa913348bb05e6eda8daa06d37fc2a` (Leonard, 2025-09-30 01:38Z, "I thought we bombed the interview"). The SQL UPDATE sets the parent's thread fields; the reply's "too" reads naturally after that post. No conflict with the base Sep 15 "before sciplay meeting let's chat".
- Known data issues touching this scenario (from the contributor guide's list; not Snowflake/Confluence, so the eval's base-data-v1 list doesn't apply): SC-9 Play Ventures (list "Rejected" vs Leonard's "didn't respond") is reconciled by the injected Sep 25 correction, which the template's "A no to our pitch that they sent Griffin … counts too" turns into one answer (Passed). SC-33 (Acterra listed twice; Treo/Treeo spelling) is covered by "a repeated name is still one row", so the count is by names. SC-34 (row 82 labelled "Superplay" with Supercell outreach notes) doesn't change the count or the status (Latest Status "Reached out - no response as of 09/11" = Awaiting reply under either name). SC-10 (LVP Sep 7 vs Sep 9) doesn't change LVP's status or Keep warm item. None is scored; keep the rubric off row 82's firm label and off LVP's meeting date.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2, PASS/COMPLETE, SQL `84818944…`), checks A–C.
- Prompt-specific sources, access and configuration: supported. No error/async config or dynamic context applies.

| Prompt ask / source | Static evidence NEW or REUSED | Prompt-specific discovery/access/configuration evidence | Task coherence |
|---|---|---|---|
| Email, template, README, folder, cards | REUSED (Eval 0 A–C); template Passed rule NEW | Fred's mailbox; Drive shares; Trello unscoped | PASS |
| Investor statuses (Gmail, Slack, Calendar, Contacts) | REUSED + NEW (Sciplay reply in #executives) | Fred's channels and calendar; SQL Slack authors are channel members | PASS |
| Money (Anton, Paul) | NEW (Leonard→Fred DMs; Fred's Anton email copy removed) | D05S58U4SAK members Fred + Leonard; DocuSign notice in Fred's mailbox | PASS |
| Build access (ZOM-567 vs Arthur's Sep 30 Slack) | NEW | Linear unscoped; Fred a #zombie-match3d member | PASS |

## Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Every fork settled by a quoted, Fred-visible or incorporated record (comparison above; fork list in the Deep Recheck, none open) |
| Prompt | Feasibility | 5 | Every ask is cataloged and every needed fact exists |
| Prompt | Persona ACL Reachability | 5 | All required scoped reads are visible to Fred |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One write set under every reading |
| Prompt | Contrived / Unnatural | 5 | Plain, natural request; detail lives in records |
| Prompt | Alignment with Today's Date | 5 | "Today" Oct 1, review Mon Oct 6, status as of Sep 30 PT |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Originality — Dataset Duplicate (STEP 0.6) | 2 | Likely duplicate (meaning 0.804 ≥ 0.80) of an existing Frederick Stone task on the same Oct 14 pre-read fundraising handoff; hard gate caps the overall score at 2 |
| Prompt | Truthfulness | 5 | All 9 premises verified |
| Prompt | Tool Use & Cross-service | 5 | Eight services, each changes graded facts |
| Prompt | Investigation + Action | 5 | Three writes fed by the investigation |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | Exact roster match; role fits |
| Prompt | Business Function | 5 | Founders / Exec work |
| Prompt | Assigned Competency | 5 | Board pre-read = Corporate Ops |
| Prompt | Assigned Task Skill | 5 | Retrieval is central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | Every entity exists and is retrievable |
| Universe | Cross-Service Coherence | 5 | No inconsistency in task-touched data; the ZOM-567 vs Slack gap is an explained in-world correction |

### Issues Found

| # | Severity | Dimension | Issue | Evidence | Minimum fix |
|---|---|---|---|---|---|
| 1 | Major (hard gate) | Originality — Dataset Duplicate | The prompt's meaning is 0.804 from an existing task already in the project (L12 stage, same persona): Leonard hands Fred the fundraising part of the Oct 14 board pre-read, every firm on the 2025 investor list gets a current status, and the counts and dollar totals go back to Leonard. Two more completed tasks sit at 0.73 and 0.72 on the same Leonard investor-list handoff | `hg_similarity.py check` on prompt `cecfad82…`: tier "likely duplicate", cutoff 0.80 | Change the task's core so it no longer restates "take over Leonard's fundraising section / board pre-read pipeline for every firm on the 2025 list". Rewording alone won't move a meaning score; the request itself has to be a different job. Then rerun /prompt. See Recommended Improvements for directions that reuse your records |

No other defect at any severity. The SQL revision 11 changes (Arthur's Android correction, the Anton DMs, the Sciplay move, the template's Passed rule) each settle to one answer.

### Recommended Improvements

1. **Clear the duplicate gate (required).** The library already holds this scenario three times (Leonard → Fred investor-list handoff before the Oct 14 board). The fix is a different task, not new wording of the same one. Directions that keep most of your seeded records: make the deliverable something only this data supports and the neighbours don't ask for, for example the Q4 investor-update send list built from the Keep warm rule plus build-access follow-ups to the firms in talks, or a tester-access fix-up across ZOM-567 and the investors (Arthur's Sep 30 note, the Dentsu and T-Accelerate contacts). Whatever you pick, the request should not be "own the fundraising section of the Oct 14 pre-read / where every firm on the list stands". Write it in your own voice; prompts are screened for AI-written text. After changing the prompt, the similarity check runs again automatically in /prompt.
2. **Rubric and OE notes (if the scenario survives in some form).** Accept a plain reply or reply-all on Leonard's thread. Don't grade the Build access cell for firms that aren't in talks. Count firms by distinct names (77 + Brightwater Games Fund + Homa = 79), not by the list's "No." column. Keep rows off row 82's firm label (SC-34) and LVP's meeting date (SC-10).
3. Eval 0 advisory, unchanged: four snapshot-uncovered columns. Optional; dropping them is a new SQL version.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review (no record, findings, scores or verdict; no access to reports/).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 4 prompt sentences plus every sentence of the incorporated email, template, README and both card comments; 30 forks | 0 | 0 |
| P2 | 4 prompt sentences; service, visibility, coherence and write feasibility | 1 (platform note) | 0 (platform, not scored) |
| P3 | 21 prompt claims plus SQL integrity | 0 | 0 |
| P4 | 4 prompt sentences | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P2 | "Can you build the sheet and put it in my Board - Oct 14 2025 folder…" | 2025 list row No. 69 Firm "[PERSON_NAME_5402]"; gcal evt_89381fe5a15b802c5652a9 "PERSON_5173_NAME ([PERSON_NAME_0854]) and Leonard Hayes"; Fred's invite "[USERNAME_22751] prep" vs gcal "SciPlay prep" | §3 hidden records | Platform: anonymized token | REJECTED | Tagged PLATFORM by the pass itself. Anonymized tokens are the source strings; a row using the token as shown is correct, and Homa is mapped by Fred's #executives copy ("HOMA feel free to join later"). Sciplay is identifiable from the Sep 3–17 intro thread in Fred's mailbox ("Intro: Danny, Michael (SciPlay) <> Leonard"). Not scored |

Main-session checks of the records the passes leaned on for the changed SQL rows (opened, not taken on the pass's word): #zombie-match3d `3cddf83c…` text and Fred's membership in `C0880U9751A` (channels.json); D05S58U4SAK `99b22482…` and `f7261dd1…` and the DM's membership (Fred, Leonard); #executives reply `229090ba…` and its base parent `99aa913348bb…`; ZOM-567 comments `lc_94eb35d962cfbdd31e1bd496` and `lc_b549f3057640a5eb08f7581e`; the Sciplay intro thread `frederick@harmonygames.co_1842285743246816270` ("How does next Monday, 9/15 at 1:30pm PST work", then "Thank you again for taking the time to chat with us on Monday"), which backs Sciplay's Keep warm item; list row 82.

Effect on verdict: unchanged. No pass finding was confirmed; every content dimension stays 5. The FAIL comes only from the STEP 0.6 dataset-duplicate gate.

Fork list (P1's 30 forks, all settled; each changed-SQL fork re-opened in the main session):
- F1: Template | Oct 14 doc | Jul 16 doc (committed = verbal yes) | Settled by: "Leonard, Sep 26. Same layout as the other sections of the pre-read." vs "Leonard, for the Jul 16 board."
- F2: Which list | "Game Investor List - Harmony Games 2025" | the 2023–24 internal list | Settled by: the template's "Latest Status notes (as of 09/11)"; only the 2025 list has that column
- F3: Repeated names | 77 | 80 grid rows | Settled by: "a repeated name is still one row"
- F4: Off-list rows | Brightwater + Homa | drop Homa; add SVB or e2vc; "who Leonard emailed this month" | Settled by: "if we pitched them the bridge or an investment alongside a co-dev deal, they count" + "we are currently seeking extension funding on our seed round" + "banks (our SVB catch-ups)" + "calls only I took don't"
- F5: 1AM Gaming | = March Gaming Fund, Passed | separate firm | Settled by: "1AM Gaming is the March Gaming Fund row on our list"
- F6: Committed | $25,000 | $40,000 | Settled by: "he can only do 25 this time, not the 40. voiding his docusign and sending a new SAFE at 25 tonight" + "Anton signed the 25 one" + DocuSign Completed notice (Sep 26)
- F7: Soft-circled | $50,000 | $75,000 or adding Initial Capital / a16z | Settled by: "Soft-circled: a yes with an amount that isn't signed yet" + Paul nudge "it's still sitting with you"
- F8: Sciplay | Passed | In talks (phone no, not on the bridge thread) | Settled by: "Passed: they've told us no for this round." + "Sciplay's out too. D called me this morning, they're passing on this round"; the bridge-thread restriction sits in the accelerator paragraph only
- F9: a16z | In talks | Passed | Settled by: "the program's decision and the feedback that comes with it aren't their answer on the bridge"
- F10: Play Ventures | Passed | Awaiting reply | Settled by: "it's still their no for this round" + "A no to our pitch that they sent Griffin … counts too"
- F11: Lakestar | Passed | Awaiting reply | Settled by: "Lakestar is no longer investing in games so this isn't a fit."
- F12: Grishin Robotics | Passed | Awaiting reply | Settled by: "Grishin Robotics (No, they want metrics)"
- F13: Initial Capital | Awaiting reply | Passed / soft-circled | Settled by: "pinged Initial Capital on LinkedIn about the bridge" + "even if they've written back"; "might write a small check" has no amount
- F14: Treo VC | Awaiting reply | Not contacted | Settled by: "I sent them the deck and the blurb there" (Sep 3) + "that day included"
- F15: Mattel | Not contacted | Awaiting reply | Settled by: "only been an RFP conversation, we haven't pitched them the bridge"
- F16: e2vc | Awaiting reply | In talks / Passed | Settled by: "calls only I took don't"; Leonard's guess isn't the firm's answer
- F17: Sony Mobile | Awaiting reply | Passed | Settled by: "An advisor's own read on whether a firm invests isn't the firm's answer."
- F18: Index, Transcend, Acterra | Not contacted | Passed / Awaiting reply | Settled by: "answers from earlier rounds and plans to reach out don't count"
- F19: Triptyq, Turkven, Harlem Capital, General Catalyst | Awaiting reply | Not contacted | Settled by: "[PERSON_NAME_0205] reached out to GFR, Play, Dentsu, General Catalyst…" + "'Us' includes anyone who reached out or made an intro on our behalf"
- F20: NCsoft | In talks | Not contacted | Settled by: Leonard's Sep 4 bridge pitch to NCsoft + Sep 10 and Sep 19 calls on Fred's calendar
- F21: T-Accelerate and Dentsu build access | iOS only | iOS and Android | Settled by: "Arthur tracks the tester adds." + "nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added" (Sep 30 4:20pm PT) + "I'll attach it when I push tomorrow's build"
- F22: Other in-talks build access | none | iOS from public store links | Settled by: "The public store pages don't count." + ZOM-567 lists only two firms
- F23: Keep warm set | LVP, Hiro Capital, Sciplay | Sciplay only / all passers / adding a16z | Settled by: "anyone who passes on the bridge after we've actually pitched them on a call or meeting this round" + "Email-only no's don't need it"; calls LVP Sep 9, Sciplay Sep 15, Hiro Sep 23
- F24: File name and folder | Google Sheet "Fundraising - Oct 14 board" in Board - Oct 14 2025 | other | Settled by: README pattern + "Google Sheets or Docs only, no uploads"
- F25: Reply numbers | 79 firms, $25,000, $50,000 | other | Settled by: "how many firms are on it (every row, angels included), total committed and total soft-circled"
- F26: Reply destination | Leonard's thread | also email the board | Settled by: "Let's not, it goes in the deck." Reply vs reply-all both fit "reply to him on that thread"; the rubric should accept either
- F27: Status cutoff | end of day Sep 30 PT | UTC / task clock | Settled by: "Status, as of end of day Tue Sep 30 (Pacific)"; no record near either edge changes a bucket
- F28: Hiro Capital and LVP | Passed | Awaiting reply | Settled by: "going to pass on the bridge" (Contacts: "Partner, Hiro Capital") + LVP's Sep 25 "we won't be joining this round"
- F29: Angels | Anton and Paul In talks, build access blank; other angels Not contacted | other buckets | Settled by: "Angels who've said yes this round go under In talks, signed or not. Leave Build access blank for them."
- F30: GFR, Brightwater, Homa | In talks, build access none | other | Settled by: Sep 30 GFR call, Sep 25 Brightwater call and Sep 18 Homa call on Fred's calendar; no tester add recorded

Platform defects: PLATFORM:anonymized-token (DR1), not scored.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort Unconfirmed

Next action: Change the task so it is no longer a restatement of the Leonard → Fred "own the fundraising section of the Oct 14 pre-read for every firm on the 2025 list" handoff, then send /prompt again. Any prompt change also needs /hardness, /oe and /rubric after it; if the SQL changes, run /injection first.

Evidence limits: Evals/Docs PDFs/XLSX were not re-extracted (scoring.json and the Eval 1 local overrides were used as the QC authority). No run verifies the runtime behaviour of the sheet create + move tools. Static review only; SQL not executed.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1

Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225

Reviewed prompt SHA-256: cecfad824fd8037af82be1f41d010c98f920db4cfe57c5087c056b7098ffed32

Review context SHA-256: 966b62629a0153afbf74ae1cd7a4122f080314da0baab6b7fe8a425a96807f92

Prompt record SHA-256: e4c08850d41210c37cb97241ba6063989c51652e28266636ebce0297e550c0ff

**Lowest Dimension:** Originality — Dataset Duplicate (STEP 0.6), 2. Every other scored dimension is 5.

**Summary:** On content the prompt is strong. It's natural and truthful, and SQL revision 11's new trap (Arthur's Sep 30 note that the Play tester list was never attached, overriding ZOM-567) settles to one answer, as do Anton's $25K (Leonard's DMs) and Sciplay's phone pass. It still FAILs the dataset-similarity hard gate: its meaning is 0.804 from an existing Frederick Stone task about the same Leonard handoff of the Oct 14 pre-read fundraising section, and two more completed tasks sit at 0.72–0.73 on the same investor-list scenario.
