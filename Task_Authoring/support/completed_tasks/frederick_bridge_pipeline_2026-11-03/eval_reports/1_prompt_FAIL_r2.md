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
| Review time | 2026-11-01 (actual) |
| Clock | 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` (revision 7; the upload `04_Prompt (2).txt` sent with this command is byte-identical), 513 bytes, SHA-256 `cecfad824fd8037af82be1f41d010c98f920db4cfe57c5087c056b7098ffed32` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md`, SHA-256 `1d795090d3476539561f58917410dab7275f800863d3be3084150ecd9a383c37` (all five fields stated; intake cleared without a round trip) |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 8), 132,556 bytes, SHA-256 `2e2428bc5e49b2a1fb8da994c4fc4db98ac2208db0eb555682b310fc28fea4ae` |
| Error/async config, dynamic context, reference files | None supplied. The prompt references no attachment; every source is an environment record |
| Eval | `Evals/1_Prompt_Eval.md` SHA-256 `7cc19b60d2988cbfdfb57ff8296d68799d583f54bfbf2c9b9b02efd43afde8f5`; shared WORKFLOW `ee4cd8e1cc291c3b…` (guide view); scoring.json `c14873e614cdcda5…` |
| Eval version | task-quality-v1 / prompt-source-checks-v2 |
| Eval release SHA-256 | `0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e` |
| Reviewed prompt SHA-256 | `cecfad824fd8037af82be1f41d010c98f920db4cfe57c5087c056b7098ffed32` |
| Review context SHA-256 | `0295f707a054d689fec69e3d9d6b5d8c4e5eeee01e7f029140db604082bd1cd9` |
| Prompt record SHA-256 | `9735bd332811b36b111bdc824d2d21a7cfffa526e5a5b09432125b226f1a1225` |
| Evidence contract | `stage-evidence-v1`; authority contract `prompt-incorporation-v1` |

Input/authority issues: none. The previous `/prompt` report graded SQL revision 6 (`952e12a9…`); the SQL has changed twice since, so nothing from it was reused as a verdict. Its raw base-record citations were re-opened where used. SQL comments (lines 1–4) are read as context only.

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`).
- Reviewed SQL sha256: `2e2428bc5e49b2a1fb8da994c4fc4db98ac2208db0eb555682b310fc28fea4ae` (`injection-static-v2`, reviewed 2026-11-01T23:45Z). Eval 0 verdict: PASS / COMPLETE.
- Eval 0 findings on records this prompt depends on:
  - Advisory 1 (Mattel Slack line "that was only ever an RFP and partnership conversation" overstates the history; Leonard's Aug 26 email offered a "small strategic investment"). It changes no graded value. Mattel's row is "Not contacted this round" under either reading, because the Aug 26 email predates the Sep 3 kickoff and the template counts only bridge outreach since Sep 3. It stays an advisory and is not scored.
  - Advisory 2 (four columns not in the schema snapshot: `slides_pages.notes`, `slides_page_elements.table_json` / `.ordinal`, `linear_comments.sequence`). P3 raised the same point. Not scored. If the platform loader rejects them, the whole script rolls back, so drop those columns or confirm the load.
  - Advisory 3 (does the template's exclusion sentence drop on-list RFP-only firms such as Mattel?). Answered under UGT below: the template's first sentence makes every list name a row, and its "us" paragraph treats RFP mail as not counting as outreach, which only matters for a firm that stays on the sheet. Settled.
- Static checks A–C (IDs, structure, chronology, mailbox copies, channel membership) are REUSED from that report under stage-evidence-v1: same SQL hash, same universe manifest, same schema snapshot and Eval 0 version.

## 2. Checklist

| Item | Status |
|---|---|
| Intake: prompt + five assignment fields + injection answer | NEW, done (prompt upload identical to saved revision 7; assignment and SQL reused) |
| STEP 0.5 injection gate | NEW: CURRENT, Eval 0 PASS reused |
| Phase 0.1 references (guide view, Eval 1 in full, acl.md, roster, catalog, reliability, QC examples, common_errors, deep_recheck) | NEW, done. Evals/Docs PDFs/XLSX were not re-extracted this run; scoring.json (the QC form adaptation) and the Eval 1 local overrides were used as the authority (see Evidence limits) |
| Phase 0.2 universe exploration | NEW: all 158 SQL row operations read; Fred's base mailbox Aug 25–Oct 1 (305 messages indexed, every investor thread read); Fred's calendar Sep 1–Oct 8 (24 events); #bridge-pitch Aug–Sep (470 messages) and #executives September; the 2025 game investor list (80 rows, 77 distinct names); Linear tester records; known_data_issues |
| Phase 1.1–1.5 | NEW, done |
| Phase 2.1 UGT (two-reading table, record saved) | NEW |
| Phase 2.2–2.9 | NEW, done (2.9 N/A: no samples supplied) |
| Phase 3.1–3.2 | NEW, done; static integrity REUSED from Eval 0 |
| Phase 4 scoring | NEW, done |
| Phase 5 deep recheck P1–P4 | NEW, done (see Deep Recheck) |

## 3. Requirement ledger (`authority_contract: prompt-incorporation-v1`)

The prompt incorporates Leonard's Sep 30 email ("His email has what he wants", "like he asks"). The email points to four records: the board pre-read template, the README in the folder, the Existing Investor Update card and the Board Deck card. That chain is valid incorporation. Nothing else adds obligations.

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Build the sheet Leonard wants | Email (SQL L161): "every firm on the 2025 game investor list, plus anyone we've had a call with since the Sep 3 kickoff who isn't on it … One sheet, one row per firm … use the buckets and definitions in the board pre-read template". Template "Board pre-read - fundraising section (Oct 14)" (SQL L23). 2025 list (gsheets, drive id `f_48247af79428823c3cac92`, 80 rows, 77 distinct names) | Inbox → email → Drive search for template and list → per firm: Gmail, Calendar, #bridge-pitch / #executives, Linear ZOM-567, Contacts, Bridge angels sheet | `gsheets_create_spreadsheet` (+ `gdrive_move_file`) or `gdrive_create_file` with `parentId`; `gsheets_values_update` / `gsheets_batch_update`; reads via `gmail_*`, `gcal_*`, `slack_*`, `linear_*`, `contacts_*`, `gdocs_*`, `gsheets_*` | Template, list, Bridge angels sheet and deck are shared with Fred; the email, DocuSign notice and investor threads are in his mailbox; the calls are on his calendar; he is a member of #bridge-pitch and #executives; Linear, Trello and Contacts are unscoped | 79 rows (77 list names + Brightwater Games Fund + Homa), each with a status (Passed / In talks / Awaiting reply / Not contacted this round), build access for firms in talks, committed and soft-circled amounts; totals at the bottom: committed $25,000, soft-circled $50,000 |
| Put it in "my Board - Oct 14 2025 folder", named per the README | Folder `d_5e8a1c3f9b07d2e64a1b93` (owner Fred, SQL L12); README (SQL L25): "one file per section named in the pattern section name + " - Oct 14 board", with "Fundraising - Oct 14 board" as its example … Google Sheets or Docs only" | Drive search / folder listing | as above | Folder owned by Fred; README shared with him | Google Sheet "Fundraising - Oct 14 board" in that folder |
| Take care of the Existing Investor Update card as Leonard asks | Email: "Whatever the Existing Investor Update card says to do for firms that pass, do that too." Card 455 comment (SQL L124): Keep warm checklist, one item per firm that passed after a pitch call or meeting this round; "Email-only no's don't need it" | Trello search → card → comments | `trello_create_checklist`, `trello_create_check_item` | Trello unscoped | Keep warm checklist on card 455 with three items: London Venture Partners, Hiro Capital, Sciplay |
| Reply on the thread with the slide numbers | Email: "reply here with the numbers the fundraising slide needs". Board Deck card comment (SQL L144): firm count (every row, angels included), total committed, total soft-circled | Trello card "Board Deck - Oct 14" → comment | `gmail_reply_to_message` (or `gmail_send_message` with `thread_id`) | Thread in Fred's mailbox | Reply to Leonard on "Oct 14 board pre-read - fundraising section": 79 firms, $25,000 committed, $50,000 soft-circled |
| Done before the Monday Oct 6 review | Calendar event, Oct 6 9am PT (SQL L304) | — | — | On Fred's calendar | Timing context, no extra write |
| Excluded by authority | Robert's "email the pipeline to the board" (SQL L149) is overruled by Leonard ("Let's not, it goes in the deck"). Arthur's #executives shortcut "just list who Leonard emailed this month" (SQL L107) is not incorporated. The July template (SQL L21, "for the Jul 16 board") is superseded by the Oct 14 template | — | — | — | No email to the board; no shortcut scope |

**Output capability.** Sheet creation, moving it to the folder, cell writes, checklist creation and the Gmail reply are all cataloged: SUPPORTED by catalog. No run shows the runtime behaviour of `gsheets_create_spreadsheet` + `gdrive_move_file`, and `/prompt` doesn't require one.

**Answer derivation (main session, for downstream reuse).** Status as of end of day Sep 30 PT, per the template:

- **Passed (8):** Play Ventures (no sent to Griffin; Leonard's Sep 25 correction, SQL L115), March Gaming Fund (1AM Gaming's written no; SQL L113 maps the rename), [PERSON_NAME_5402] (Latest Status "They don't do bridge"), Grishin Robotics (#bridge-pitch Sep 8 "No, they want metrics"), Lakestar Ventures (Sep 4 email "Lakestar is no longer investing in games"), London Venture Partners (Sep 25 written pass after the Sep 9 call), Hiro Capital (Edith Vane's Sep 26 pass after the Sep 23 call, SQL L197/L296), Sciplay (Robert's Sep 29 phone note in the #bridge-pitch thread, SQL L119, after the Sep 15 call).
- **In talks (9):** Andreessen Horowitz (speedrun interview Sep 18; the program's no isn't a bridge answer), NCsoft (Sep 10 and Sep 19 calls), T-accelerate (Sep 22), Dentsu Ventures (Sep 23 PT), GFR Fund (Sep 30), Homa (Sep 18, added), Brightwater Games Fund (Sep 25, added), Anton Bernstein and Paul Heydon (angels who said yes).
- **Awaiting reply:** the list names with bridge outreach since Sep 3 and no call, no no. That covers the "Reached out - no response as of 09/11" notes (Makers Fund, Raine Ventures, BBQ Capital, Superplay, Sony Mobile, Revo Capital, e2vc), Treo VC (SQL L111), BITKRAFT Ventures (#bridge-pitch Sep 22), General Catalyst, Triptyq, Turkven and Harlem Capital (IH outreach, #bridge-pitch Sep 12), and Initial Capital (this-round Latest Status note).
- **Not contacted this round:** every other list name.
- **Build access:** T-accelerate iOS and Android; Dentsu iOS only (Linear ZOM-567, which the template backs with "Arthur tracks the tester adds", is newer than Leonard's "Invites … are out"); the other firms in talks none; angels blank.
- **Money:** Anton $25,000 committed (DocuSign Completed notice Sep 26; latest amount from his Sep 24 email). Paul $50,000 soft-circled (Leonard's #executives post and the Bridge angels sheet; Leonard's Sep 29 nudge shows it unsigned).

This derivation is evidence for later stages. It is not a rubric, and other wordings of the same values stay valid.

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Frederick Stone (`frederick_stone`, frederick.stone@harmonygames.co, Co-founder, Executive) matches the roster exactly. He is a member of #bridge-pitch and #executives, joins the investor calls (all on his calendar), is cc'd on the investor threads and owns the Board - Oct 14 2025 folder. A co-founder taking over the fundraising section of a board pre-read from the CEO is plausible in role, authority and access.

| Check | Finding |
|---|---|
| Role plausibility | Yes: co-founder covering for the CEO on board materials |
| Voice match | Yes: short, plain delegation |
| Access plausibility | Yes: every required record is in his mailbox, calendar, channels or shared Drive |
| Responsibility scope | Yes: prepare the section; Leonard stitches it into the deck |

**Assigned Competency (Corporate Ops):** PASS (5). Board pre-read materials are board work, which is Corporate Ops (board / legal / HR / vendor). The fundraising content doesn't make it a Finance model, budget or forecast task.

**Assigned Task Skill (Retrieval):** PASS (5). The work is finding, for 79 firms, the records that decide their status, money and tester access across seven services, then writing the results down. Retrieval is central. Applying the template's buckets stacks on top of it, which is allowed.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y — PASS
- Multi-Source: the template (Docs), the list (Sheets), Gmail, Calendar, Slack, Linear, Contacts and Trello each decide graded cells.
- Dynamic Change: Anton's $40K (SQL L105, Bridge angels sheet) is replaced by his Sep 24 "I can do $25K this time". Play Ventures' Sep 23–25 "didn't respond" is corrected on Sep 25 (SQL L115). Leonard's "Invites … are out" for Dentsu (SQL L220) is overtaken by Arthur's Sep 30 Linear note (Play not added). The July template is superseded by the Oct 14 one.
- Ambiguity: the file name comes from the README, the slide numbers from the Board Deck card and the Keep warm rule from the card comment, all named in Leonard's email.
- Data seeding: PASS. The prompt is a 4-sentence trigger; the operating rules live in the seeded template, README, cards and messages.

**Naturalness:** PASS (5). First person, plain, uneven sentence lengths, no formatting or polished connectives, no deliverable spec. P4 agreed (no findings).

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
| Command List | PASS: "and then reply" joins the last of three asks in one question and reflects a real dependency (the reply needs the finished numbers) |
| Bolt-On | PASS: every clause serves the same handoff; the Oct 6 sentence is deadline context backed by the calendar invite, not a separate ask |
| Pre-Solving | PASS: no status, firm, amount or count is given |
| Tool Mention | PASS: "Trello", "the sheet", "folder", "thread" are natural product words; no tool, parameter or MCP name |

**Diversity:** beyond "investigate + post one message": a new spreadsheet in a named folder, a Trello checklist with items, and an email reply, over a 79-firm cohort.

## Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: One row's status forks with no resolving record: Initial Capital is Awaiting reply (this-round Latest Status note implies they answered us) or Not contacted this round (no record of outreach from us since Sep 3). Every other fork (Homa, Mattel, a16z, Play, Sciplay, Hiro, LVP, Dentsu build access, money totals, firm count, Keep warm set) is settled by a persona-visible record.

Alternative selection: Initial Capital is the only status P1 and the main review both found unsettled; Homa, the strongest count-changing alternative, is recorded as Reading C and excluded.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Leading reading: 79 rows; Initial Capital's this-round Latest Status note shows they answered us, so the row is Awaiting reply (no call, no no); Homa counts. | Initial Capital = Awaiting reply; Homa included as In talks | Create the Fundraising - Oct 14 board sheet; add the Keep warm checklist; reply on Leonard's thread | Board - Oct 14 2025 folder; Existing Investor Update card; Leonard's Sep 30 thread | 79 rows with Initial Capital Awaiting reply; reply: 79 firms, $25,000 committed, $50,000 soft-circled | T18 (Evals/task\_inputs/01\_Universe\_Inject.sql): "On the list only the Latest Status notes are from this round (as of 09/11), and they count as written"; GS2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gsheets/data.json): "They won't lead - would potentially write a small check"; T5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Awaiting reply: we reached out this round, no call yet and no no" |
| B | No persona-visible record shows any outreach from us to Initial Capital since Sep 3; the note records their stance, not our outreach, so the row is Not contacted this round. | Initial Capital = Not contacted this round; Homa included as In talks | Create the Fundraising - Oct 14 board sheet; add the Keep warm checklist; reply on Leonard's thread | Board - Oct 14 2025 folder; Existing Investor Update card; Leonard's Sep 30 thread | 79 rows with Initial Capital Not contacted this round; reply: 79 firms, $25,000 committed, $50,000 soft-circled | T6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Not contacted this round: nothing from us since Sep 3."; GS5 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gsheets/data.json): "Initial Capital" |
| C | Homa is a co-dev/publishing conversation, not investment talks, so it is left off; 78 rows. | Homa excluded; Initial Capital = Awaiting reply | Create the Fundraising - Oct 14 board sheet; add the Keep warm checklist; reply on Leonard's thread | Board - Oct 14 2025 folder; Existing Investor Update card; Leonard's Sep 30 thread | 78 rows; reply: 78 firms, $25,000 committed, $50,000 soft-circled | BP6 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C096HFA5Z8W/2025-09.json): "I think we should focus Homa on the co-dev investment path."; HOMA2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "We are also considering publishing opportunities"; T3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Service or work-for-hire deals, banks (our SVB catch-ups), RFPs, publishing-only talks and calls with other engine companies" |

Explicit option inventory: The prompt lists three asks, not alternative options; it offers no candidate choices.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "Leonard emailed me on Sep 30 asking me to own the fundraising section of the Oct 14 board pre-read since he's flying to LA today, and I'd like you to take it on for me. His email has what he wants. Can you build the sheet and put it in my Board - Oct 14 2025 folder, take care of the Existing Investor Update card in Trello like he asks, and then reply to him on that thread with the numbers he needs for the slide? I'm going through it with him at the review on Monday, Oct 6, so it needs to be done before then."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The template's buckets turn on whether we reached out since Sep 3. Initial Capital's only this-round record is the list note; Fred's mailbox (Sep 3-30), \#bridge-pitch and \#executives hold no record of outreach to Initial Capital (P1 search: 0 records). None of the five checks settles it: no newer source, no authority line on notes that imply contact, the note is Initial Capital's stance not our message, scope is this one row, and the status cell differs.
Resolution evidence: T18 (Evals/task\_inputs/01\_Universe\_Inject.sql): "On the list only the Latest Status notes are from this round (as of 09/11), and they count as written"; T6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Not contacted this round: nothing from us since Sep 3."; GS2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gsheets/data.json): "They won't lead - would potentially write a small check"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Awaiting reply vs Not contacted this round for Initial Capital. |
| writes | SAME | Same sheet, checklist and reply. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | The Initial Capital status cell differs; status is not a figure, so the both-fair rule does not apply. |

Resolution relevance challenge: The note implies contact but quotes no outreach from us; an inference cannot exclude Reading B under Eval 1 section 2.1.
Delegation challenge: NOT_CLAIMED. The template defines one status per firm; it delegates no choice.
Challenge evidence: T5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Awaiting reply: we reached out this round, no call yet and no no"

Compared alternative: C
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

Strongest-alternative challenge (B): Not a strawman: the template defines Not contacted as nothing from us since Sep 3, and no Fred-visible record shows outreach to Initial Capital; only the list note hints at contact.
Challenge evidence: T6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Not contacted this round: nothing from us since Sep 3."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5). Every ask maps to a cataloged write (table above) and every needed fact exists in a record Fred can open. No per-X breakdown needs a missing field: status, build access and money are columns the template defines and the records fill. No exact-precision ask beyond whole-dollar amounts. Snowflake and Confluence aren't used.

| Ask | Capability | Tools | Feasible? |
|---|---|---|---|
| Read list, template, README, cards, mail, calendar, Slack, Linear, Contacts | Read | gsheets/gdocs/gdrive/trello/gmail/gcal/slack/linear/contacts reads | Yes |
| Create the Google Sheet in the folder and fill it | Create + move + write | `gsheets_create_spreadsheet`, `gdrive_move_file` / `gdrive_create_file(parentId)`, `gsheets_values_update` | Yes (catalog) |
| Keep warm checklist with one item per firm | Write | `trello_create_checklist`, `trello_create_check_item` | Yes |
| Reply on Leonard's thread | Write | `gmail_reply_to_message` | Yes |

**Persona ACL Reachability:** PASS (5). Scoped reads (from the acl.md matrix: Gmail, Slack, GCal, Drive family) are all visible to Fred: his own mailbox and calendar, two channels he belongs to, and Drive files he owns or that are shared with him (the list `f_48247af79428823c3cac92`, both template docs, the README, the Bridge angels sheet, the deck). P2 found no hidden record. A few Leonard-only mails (the BBQ intro, 1AM's replies before Sep 8, Robert's Homa acceptance notice) are covered by Slack or later threads Fred can read.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5). The write set is the same under every reading: one sheet in the named folder, one checklist on the named card, one reply on the named thread. No "I'll [verb]" self-action competes with the delegation ("I'm going through it with him" is Fred's own meeting, not a write the Agent might take). Robert's request to email the board is explicitly declined in the email the prompt incorporates.

**Contrived / Unnatural:** PASS (5). No timestamps, opaque ids, generated filenames, trap hints, hidden destinations (the folder, card and thread are all named), audit-form wording or if-chains. The detail lives in seeded records.

**Alignment with Today's Date:** PASS (5). "Today" is Wed Oct 1, 2025, and Leonard's Sep 30 email says "flying to LA tomorrow morning". "Monday, Oct 6" is a Monday, and the review sits after the clock as a future meeting. Status is "as of end of day Tue Sep 30 (Pacific)", which is before the clock. Records the status window depends on (GFR's Sep 30 call, Leonard's 6:41pm PT follow-up, the speedrun feedback forward at 8:21pm PT) fall inside it.

**Originality / Sample Similarity:** N/A: no comparison samples supplied.

**Truthfulness:** PASS (5). All 10 premises verified (record below): the email (Sep 30, 2:05pm PT) and its asks; the LA trip; the folder (owned by Fred); the card (base card 455, unique name); "like he asks"; the thread and the numbers; the Oct 6 review. P3 found no premise or clock problem.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact. Drop Gmail and Anton's $25K, Hiro's and Lakestar's passes and the reply are lost. Drop Calendar and the In talks set and the two added firms are lost. Drop Slack and Paul's $50K, Grishin's and Sciplay's passes and the IH outreach are lost. Linear supplies build access, Trello the Keep warm rule and the slide numbers, Sheets/Docs the cohort and the rules.

**Investigation + Action:** PASS (5). Three writes (sheet, checklist, reply), each fed by the investigation.

**Coherence (Bolt-on):** PASS (5). One workflow: build the section, act on the passes, report the numbers.

**Business Function (Executive):** PASS (5). Board pre-read and fundraising pipeline are founder/exec work (task_categories: "Founders / Exec / Strategy").

## Phase 3: Universe Feasibility

**Data Existence:** PASS (5)
- Entities verified: every list name, the 12 investor calls on Fred's calendar since Sep 3 (SVB excluded as a bank), the template, README, folder, both cards, the email thread, DocuSign notice, Bridge angels sheet and ZOM-567.
- All retrievable via MCP: Yes (catalog reads for every service used).

**Cross-Service Coherence:** NON-FAIL (3)
- Inconsistencies in task-touched data: one minor (Temporal / Other). The injected Linear ZOM-567 comments say T-Accelerate's Play add was Sep 23 and that Arthur lacks Play console rights. Base #executives on 2025-09-22 (16:08–16:30Z) shows Arthur doing both invites and posting the Play internal-test link. It changes no graded value (DR2).
- Known base-data issues (not scored): SC-24 (Tim Steudler writes as Mattel's contact from a harmonygames.co address). The task never reads his employer: Mattel's row is decided by the template's bridge-outreach rule. Keep the rubric and OEs off his identity. No Snowflake or Confluence data is used.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2, PASS/COMPLETE, SQL `2e2428bc…`), checks A–C.
- Prompt-specific sources, access and configuration: supported. No error/async config or dynamic context applies.

| Prompt ask / source | Static evidence NEW or REUSED | Prompt-specific discovery/access/configuration evidence | Task coherence |
|---|---|---|---|
| Email, template, README, folder, cards | REUSED (Eval 0 A–C) | Fred's mailbox; Drive shares; Trello unscoped | PASS |
| Investor statuses (Gmail, Slack, Calendar, Contacts) | REUSED + NEW base reads | Fred's channels and calendar; SQL Slack authors are channel members | PASS |
| Money (Anton, Paul) | REUSED + NEW | Fred cc'd on Anton's email, DocuSign notice and Paul nudge; #executives member | PASS |
| Build access (ZOM-567 vs Slack/Gmail) | NEW | Linear unscoped; #executives member | NON-FAIL (minor, DR2) |

## Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 2 | Initial Capital's status forks (Awaiting reply vs Not contacted this round); no persona-visible record settles it. See the comparison above |
| Prompt | Feasibility | 5 | Every ask is cataloged and every needed fact exists |
| Prompt | Persona ACL Reachability | 5 | All required scoped reads are visible to Fred |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One write set under every reading |
| Prompt | Contrived / Unnatural | 5 | Plain, natural request; detail lives in records |
| Prompt | Alignment with Today's Date | 5 | "Today" Oct 1, review Mon Oct 6, status as of Sep 30 PT |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | All premises verified |
| Prompt | Tool Use & Cross-service | 5 | Seven services, each changes graded facts |
| Prompt | Investigation + Action | 5 | Three writes fed by the investigation |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | Exact roster match; role fits |
| Prompt | Business Function | 5 | Founders / Exec work |
| Prompt | Assigned Competency | 5 | Board pre-read = Corporate Ops |
| Prompt | Assigned Task Skill | 5 | Retrieval is central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | Every entity exists and is retrievable |
| Universe | Cross-Service Coherence | 3 | One minor inconsistency in the tester records (DR2); no graded value changes |

### Issues Found

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | Initial Capital's row: the list's this-round Latest Status note ("They won't lead - would potentially write a small check") implies contact, but no record Fred can open shows outreach from us since Sep 3. The template's buckets give "Awaiting reply" (we reached out) or "Not contacted this round" (nothing from us since Sep 3), and nothing picks one | Major | UGT |
| 2 | Linear ZOM-567 comment `lc_94eb35d962cfbdd31e1bd496` says T-Accelerate's "Play internal track added Sep 23", and `lc_b549f3057640a5eb08f7581e` says Arthur has no Play console rights. In #executives on 2025-09-22, Arthur says "i can just do both", then "Invites sent" and posts the Google Play internal-test link (16:30Z); Leonard's 17:40Z email gives T-Accelerate the same Android link. Graded values don't change (T-Accelerate iOS and Android; Dentsu iOS only) | Minor | Cross-Service Coherence |

### Recommended Improvements

The prompt wording itself passes every check; both fixes go in the SQL.

1. **Initial Capital (required, UGT).** Add one dated record Fred can see that shows our bridge outreach to Initial Capital between Sep 3 and Sep 11 (the note is "as of 09/11"). Either a #bridge-pitch post by Leonard (`EMPLOYEE_0038_SLACK_ID`, a channel member of `C096HFA5Z8W`), or an email from Leonard to an Initial Capital contact with frederick.stone@harmonygames.co in Cc. The row then becomes Awaiting reply. Keep any amount out of it ("small check" with no number), or the soft-circled total changes. If you intended Not contacted this round instead, the list note itself is base data, so add a dated record saying it came from an earlier round.
2. **Tester records (minor, Cross-Service Coherence).** In `lc_94eb35d962cfbdd31e1bd496`, use Sep 22 for the T-Accelerate Play add, to match Arthur's 2025-09-22 16:30Z "Invites sent" and the internal-test link. In `lc_b549f3057640a5eb08f7581e`, replace the "I don't have console owner rights" reason with one that doesn't contradict Arthur adding T-Accelerate to Play himself. Keep "Play internal track not added yet", so Dentsu stays iOS only.
3. Optional (Eval 0 advisories): reword the Mattel Slack line to cover only the period since the kickoff, and drop the four columns the schema snapshot doesn't cover.

Each SQL change is a new version: send /injection, then /prompt, /hardness, /oe and /rubric again, in that order.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review (no record, findings, scores or verdict shared).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 77 sentences (4 prompt + 73 incorporated: email 13, template 47, README 5, two card comments 5, slide 9 text 3) | 1 | 1 |
| P2 | 4 prompt sentences | 1 | 1 |
| P3 | 5 sentences, 17 premise items, SQL static checks | 1 | 0 (advisory) |
| P4 | 4 prompt sentences | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "Can you build the sheet and put it in my Board - Oct 14 2025 folder" → template "On the list only the Latest Status notes are from this round (as of 09/11), and they count as written" | gsheets `/sheets_spreadsheets/96`, row No. 16 "Initial Capital", Latest Status "They won't lead - would potentially write a small check"; no Initial Capital record in Fred's Sep mail, #bridge-pitch or #executives (main-session grep of Fred's mail: 0 files) | §2 which status | Unique Ground Truth | CONFIRMED | No prompt sentence or Fred-visible record shows outreach from us, and none rules out "Not contacted this round". The note only implies contact, and an inference can't reject Reading B. Status isn't a figure, so the both-fair rule doesn't apply |
| DR2 | P2 | "Can you build the sheet…" (build access column) | SQL Linear `lc_94eb35d962cfbdd31e1bd496` "Play internal track added Sep 23"; `lc_b549f3057640a5eb08f7581e` "I don't have console owner rights on that app"; base #executives 2025-09-22 16:08–16:30Z Arthur "i can just do both" / Leonard "we should probably just do both" / Arthur "Invites sent" + "They can join the Google Play Internal Test here"; #bridge-pitch 2025-09-24 01:35Z Arthur "I have to add them by email for google play to work" | §3 coherence (date-slip) | Cross-Service Coherence | CONFIRMED | Opened all four records: the Sep 22 exchange shows Arthur sending both invites, which conflicts with the Sep 23 date and the no-rights claim. It changes no order, window, count or graded value, so it is one minor inconsistency (NON-FAIL 3), not a lifecycle or sum mismatch |
| DR3 | P3 | SQL rows for `slides_pages.notes`, `slides_page_elements.table_json` / `.ordinal`, `linear_comments.sequence` | `references/schema/injection.json` snapshot lacks these columns | §6.8 columns exist | Injection column advisory | REJECTED | Same as Eval 0 Advisory 2: the snapshot is unverified, and a missing column alone is a provisional advisory under schema/README.md. Kept in the Injection Gate section, not scored |

Effect on verdict: Unique Ground Truth drops from 5 to 2 (DR1), and Cross-Service Coherence drops from 5 to 3 (DR2). Overall FAIL 2.

Fork list:
- F1: Initial Capital status | Awaiting reply | Not contacted this round | Missing: a dated (Sep 3–11) Fred-visible record of our bridge outreach to Initial Capital, or a record placing the note in an earlier round
- F2: Which template | Oct 14 doc | July doc | Settled by: "Leonard, for the Jul 16 board." vs "Leonard, Sep 26. Same layout as the other sections of the pre-read."
- F3: Which list | "Game Investor List - Harmony Games 2025" | older lists / reachout sheet | Settled by: the 2025 title; the reachout sheet isn't shared with Fred
- F4: Repeated names | 77 rows | 80 rows | Settled by: "a repeated name is still one row"
- F5: 1AM Gaming | = March Gaming Fund | separate firm | Settled by: "1AM Gaming is the March Gaming Fund row on our list"
- F6: Mattel | row, Not contacted | dropped / Awaiting reply | Settled by: "One row per name on the 2025 game investor list" and "Only outreach about the bridge counts, not RFP or partnership mail"
- F7: Homa | added, In talks | excluded | Settled by: "if we pitched them the bridge or an investment alongside a co-dev deal, they count…" + "we are currently seeking extension funding on our seed round"
- F8: Brightwater | added, In talks | not a row | Settled by: Sep 25 event on Fred's calendar + "questions on the bridge round"
- F9: Dentsu | Dentsu Ventures row | separate row | Settled by: "Dentsu (IH can intro)" in the VC list and IH outreach
- F10: SVB / Griffin / Supercell / Laton / Vine | not rows | rows | Settled by: "banks (our SVB catch-ups)"; none of the others has a call on Fred's calendar
- F11: Calls only Leonard took (Sep 22 and Sep 29 Turkish VC) | excluded | included | Settled by: "A call counts when it's on Fred's calendar; calls only I took don't"
- F12: Firm count | 79 | 78 / 80 / 82 | Settled by: F4–F10 and "how many firms are on it (every row, angels included)"
- F13: a16z | In talks, no Keep warm | Passed + Keep warm | Settled by: "the program's decision isn't their answer on the bridge"
- F14: Play Ventures | Passed, no Keep warm | Awaiting reply | Settled by: Sep 25 correction "it's still their no for this round"
- F15: Sciplay | Passed + Keep warm | not passed | Settled by: Robert's #bridge-pitch phone note and the template's phone-pass rule; Sep 15 call ("SciPlay prep" + "[USERNAME_22751] <> [SOURCE_ORG_0001]")
- F16: Hiro | Passed + Keep warm | Awaiting reply | Settled by: Edith Vane "going to pass on the bridge"; Contacts "Partner, Hiro Capital"
- F17: LVP | Keep warm | not (call before the Sep 14 comment) | Settled by: the pass came Sep 25, after the "Going forward" comment
- F18: Keep warm set | London Venture Partners, Hiro Capital, Sciplay | adds email-only passers | Settled by: "Email-only no's don't need it"
- F19: Grishin / Lakestar / [PERSON_NAME_5402] / March | Passed | Awaiting reply | Settled by: "Grishin Robotics (No, they want metrics)", "Lakestar is no longer investing in games", "They don't do bridge"
- F20: Sony Mobile | Awaiting reply | Passed | Settled by: "An advisor's own read … isn't the firm's answer"
- F21: Index / Transcend / Acterra | Not contacted | Passed / Awaiting reply | Settled by: "answers from earlier rounds and plans to reach out don't count"
- F22: Treo VC | Awaiting reply | Not contacted | Settled by: "I sent them the deck and the blurb there" (Sep 3)
- F23: NCsoft | In talks, build none | excluded | Settled by: calls on Sep 10 and Sep 19 on Fred's calendar; list row exists
- F24: Dentsu build access | iOS only | iOS and Android | Settled by: "Arthur tracks the tester adds" + "TestFlight added. Play internal track not added yet"
- F25: Committed total | $25,000 | $40,000 | Settled by: "use the latest amount the investor gave us" + "I can do $25K this time, not the 40"
- F26: Soft-circled total | $50,000 | adds Griffin / Initial Capital | Settled by: "a yes with an amount"; neither gives one
- F27: Sheet name, place and reply | "Fundraising - Oct 14 board" in Fred's folder; reply 79 / $25,000 / $50,000 on Leonard's thread | email the board; Arthur's shortcut | Settled by: README rule; "Let's not, it goes in the deck". CC on the reply is open, so a rubric shouldn't check it

Platform defects: none. Anonymized tokens ([PERSON_NAME_0854] = Homa via Fred-visible Slack, [PERSON_NAME_5402], [USERNAME_22751]) are the source strings and are accepted as shown.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort Unconfirmed

Next action: Add a dated Fred-visible record of bridge outreach to Initial Capital (Sep 3–11), and align the two ZOM-567 Linear comments with Arthur's Sep 22 #executives messages. Then send /injection, /prompt, /hardness, /oe and /rubric again, in that order.

Evidence limits: Evals/Docs PDFs/XLSX were not re-extracted (scoring.json and the Eval 1 local overrides were used as the QC authority). No run verifies the runtime behaviour of the sheet create + move tools. Static review only; SQL not executed.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: cecfad824fd8037af82be1f41d010c98f920db4cfe57c5087c056b7098ffed32

Review context SHA-256: 0295f707a054d689fec69e3d9d6b5d8c4e5eeee01e7f029140db604082bd1cd9

Prompt record SHA-256: 9735bd332811b36b111bdc824d2d21a7cfffa526e5a5b09432125b226f1a1225

**Lowest Dimension:** Unique Ground Truth - 2 - Initial Capital's status has two defensible answers and no record picks one.

**Summary:** The prompt is natural, truthful and feasible, and the new SQL settles every fork from the last round: Homa, a16z, Play, Paul's soft-circle, connector outreach, the angels, 1AM and Mattel. The firm count (79), totals ($25,000 committed, $50,000 soft-circled) and the Keep warm set (London Venture Partners, Hiro Capital, Sciplay) each have one answer. One row's status still forks (Initial Capital), which fails UGT, and one minor tester-record inconsistency holds Cross-Service Coherence at 3.
