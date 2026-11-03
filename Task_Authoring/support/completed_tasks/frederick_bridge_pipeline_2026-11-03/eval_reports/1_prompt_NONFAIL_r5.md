# Prompt Quality Review (Eval 1)

## PROMPT EVALUATION REPORT

### Task: Fred takes over Leonard's Q4 investor-update send list for the bridge round: build the send list in his Q4 2025 investor update folder, add the Keep warm checklist to the Existing Investor Update card, and reply on Leonard's thread with the per-group counts
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
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `04_Prompt.txt` revision 13, saved from the upload `04_Prompt (5).txt` sent with this command; 454 bytes, SHA-256 `b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9`. It replaces revision 7 (`cecfad82…`, the Oct 14 board pre-read version) |
| Assignment | `00_Task_Assigned_Inputs.md`, SHA-256 `1d795090d3476539561f58917410dab7275f800863d3be3084150ecd9a383c37`. All five fields stated: Frederick Stone (Co-founder), Executive, Corporate Ops, Retrieval, long-horizon |
| Injection SQL | `01_Universe_Inject.sql` revision 12, 126,369 bytes, SHA-256 `efe3cab14874d1daa3ba71900a44a4536537fe46eae947167649ae2032c9c881` |
| Error/async config, dynamic context, reference files | None supplied. The prompt names no attachment; every source is an environment record |
| Eval | `1_Prompt_Eval.md` SHA-256 `e0c364dccda17423ece700d9c4b852a2a04b199a96b42b044d2dc73e73bd6057`; deep_recheck.md `ec7832d95f6f2f93…`; scoring.json `c14873e614cdcda5…` |
| Eval version | task-quality-v1 / prompt-source-checks-v2 |
| Eval release SHA-256 | `a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225` |
| Reviewed prompt SHA-256 | `b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9` |
| Review context SHA-256 | `11b87f5c6a49c0081281afc505ba4f3faa38b5728147b143183727bda46dad30` |
| Prompt record SHA-256 | `f1877b23c38e3f84eb83fab0f80b533f874b1c9913ca3ef7fe28c50259bdb9bc` |
| Evidence contract | `stage-evidence-v1`; authority contract `prompt-incorporation-v1` |

Input/authority issues: none. This is a new prompt (a new scenario: the Q4 investor-update send list instead of the Oct 14 board pre-read), so every requirement mapping, premise and fork was checked afresh against SQL revision 12. Base files are unchanged from the earlier reviews: the universe manifest hash matches and every base source cited here was re-hashed. Base firm facts that earlier reviews established were re-opened wherever this prompt's answer depends on them (calendar events, outreach posts, pass emails). SQL comments (lines 1–4) are read as context only.

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`).
- Reviewed SQL sha256: `efe3cab14874d1daa3ba71900a44a4536537fe46eae947167649ae2032c9c881` (`injection-static-v2`, reviewed 2026-11-02T11:54Z). Eval 0 verdict: PASS / COMPLETE (report SHA-256 `c2750b9fd4060e2c03b755832f63c4608a7bd4344aee6db5cfeb117e82070e4b`).
- Eval 0 findings on records this prompt depends on: none. Remaining advisory (unchanged, confirmed again by P3): four columns the unverified schema snapshot doesn't list (`gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` / `.ordinal`, `linear.linear_comments.sequence`). It changes no value the answer is graded on, so it isn't scored.
- Static checks A–C (IDs, structure, chronology, mailbox copies, channel membership) are REUSED from that report under stage-evidence-v1: same SQL hash, same universe manifest, same schema snapshot and Eval 0 version. The Eval 0 report's note that the old prompt named records the SQL no longer has is resolved by this prompt.

### Dataset Similarity
- Library: 291 tasks (Enterprise Atlas - Commercial: L10 14, L11 3, L12 107, completed 167), built 2026-11-01T07:15Z, refreshed 2026-11-02T10:37Z, age 1.4 h at check time. Check saved for this exact prompt hash.
- **Gate: PASS.** Nearest tier: same scenario (0.762, below the 0.80 duplicate line). No score change. Task IDs are withheld here under portal policy.

| Neighbour | Stage | Persona / competency / skill | Meaning | Wording | Tier | What the two prompts share |
|---|---|---|---|---|---|---|
| 1 | L12 | Frederick Stone / Corporate Ops / Analysis and synthesis | 0.762 | 0.012 | same scenario | Leonard hands Fred the bridge-round investor list; that one updates every firm's status on the list for the Oct 14 board and drafts follow-ups. Yours builds a separate send list for the Q4 update, adds a Keep warm checklist and reports group counts |
| 2 | completed | Frederick Stone / Corporate Ops / Actions | 0.747 | 0.000 | same scenario | Leonard's 2025 investor-list handoff before his LA trip, with a reply naming the firms that said no |
| 3 | completed | Frederick Stone / Finance / Actions | 0.716 | 0.000 | same scenario | Bringing the 2025 investor list current from Leonard's #bridge-pitch request |

## 2. Checklist

| Item | Status |
|---|---|
| Intake: prompt + five assignment fields + injection answer | NEW, done (new prompt saved as revision 13; assignment and SQL reused) |
| STEP 0.5 injection gate | NEW: CURRENT, Eval 0 PASS reused |
| STEP 0.6 dataset similarity | NEW: PASS (same scenario 0.762) |
| Phase 0.1 references (guide view, Eval 1, acl.md, roster, catalog, release snapshot, deep_recheck, common_errors, known data issues) | NEW, done. The Evals/Docs PDFs/XLSX were not re-extracted; scoring.json and the Eval 1 local overrides served as the authority |
| Phase 0.2 universe exploration | NEW: every SQL row this prompt uses; Fred's calendar Sep 1–Oct 6 (all events); #bridge-pitch and #executives September exports; the 2025 investor list grid (89 rows); Fred's mailbox threads for LVP, Lakestar, a16z, Dentsu, GFR, Homa, Sciplay, Makers, Raine, Superplay; channel membership |
| Phase 1.1–1.5 | NEW, done |
| Phase 2.1 UGT (ten readings, record saved; P1's 33 forks added in the Deep Recheck) | NEW |
| Phase 2.2–2.9 | NEW, done (2.9 N/A: no samples supplied) |
| Phase 3.1–3.2 | NEW, done; static integrity REUSED from Eval 0 |
| Phase 4 scoring | NEW, done |
| Phase 5 deep recheck P1–P4 | NEW, done (see Deep Recheck) |

## 3. Requirement ledger (`authority_contract: prompt-incorporation-v1`)

The prompt incorporates Leonard's Sep 30 email ("His email lays out what he's after"). The email points to four records: the Q4 send list doc ("the groups and details in the Q4 update send list doc"), the README in Fred's folder ("says how to name it"), the Existing Investor Update card ("Whatever the … card says to do for firms that pass, do that too") and the draft deck. The doc points to Leonard's #executives note on what counts as signed. That chain is valid incorporation. Nothing else adds obligations.

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Work out who from the bridge round gets the Q4 update | Email (2025-09-30 21:05Z): "everyone from the bridge round who should get it, as of tonight, with the groups and details in the Q4 update send list doc". Doc "Q4 investor update - send list" (Leonard, Sep 26): who to look at, the four groups, Passed/"us"/accelerator rules, build access, sheet columns. #executives note (Sep 26): New investor only once the DocuSign Completed notice is in. 2025 investor list (89 grid rows) | Inbox → email → Drive search for the doc, README and list → per firm: Gmail, Calendar, #bridge-pitch / #executives / #zombie-match3d, Leonard's DM, Linear ZOM-567, Contacts | reads via `gmail_*`, `gcal_*`, `slack_*`, `gdrive_*`, `gdocs_*`, `gsheets_*`, `linear_*`, `trello_*`, `contacts_*` | Email, DocuSign notice, investor threads and invites are in Fred's mailbox; the calls are on his calendar; the doc, README, list, deck and Bridge angels sheet are owned by or shared with him; he is a member of #bridge-pitch, #executives, #zombie-match3d and DM D05S58U4SAK; Linear, Trello and Contacts are unscoped | 26 rows (see derivation) |
| Put the send list in "my Q4 2025 investor update folder" | Folder `d_5e8a1c3f9b07d2e64a1b93` "Q4 2025 investor update" (owner Fred). README: name it "Q4 update - send list"; "Google Sheets or Docs only, no uploads" | Drive folder listing | `gsheets_create_spreadsheet` + `gdrive_move_file`, or `gdrive_create_file` with `parentId`; `gsheets_values_update` (or `gdocs_*` for a Doc) | Folder owned by Fred; README shared with him (writer) | A Google Sheet (or Google Doc) "Q4 update - send list" in that folder |
| Do what Leonard asked on the Existing Investor Update card | Email: "Whatever the Existing Investor Update card says to do for firms that pass, do that too." Card 455 comment (Leonard, Sep 14): Keep warm checklist, one item per firm that passed after a pitch call or meeting this round; "No's from firms we only ever emailed don't need it" | Trello search → card → comments | `trello_create_checklist`, `trello_create_check_item` | Trello unscoped | Keep warm checklist on card 455 with London Venture Partners, Hiro Capital, Sciplay |
| Reply on his thread with how many ended up in each group | Email: "reply here with how many firms and angels are in each group" | Same thread | `gmail_reply_to_message` (or `gmail_send_message` with the thread) | Thread in Fred's mailbox | Reply: New investor 1 (angel), In talks 8 (7 firms + 1 angel), Awaiting reply 14 firms, Keep warm 3 firms |
| Done before the Monday Oct 6 review | Invite "Q4 update send list review", Mon Oct 6 2pm PT, "Fred to bring the send list." | — | — | On Fred's calendar | Timing context, no extra write |
| Excluded by authority | Robert's "send it to everyone on the 2025 investor list" is rejected in the email ("Let's not, only the people the doc says"). Arthur's #executives shortcut ("who Leonard emailed this month") isn't incorporated and is covered by the same line. The July "Q3 investor update - send list" doc is for the earlier update | — | — | — | No list-wide send; no shortcut scope |

**Output capability.** Sheet or Doc creation in a folder, cell writes, checklist creation and the Gmail reply are all cataloged: SUPPORTED by catalog. No run shows the runtime behaviour of `gsheets_create_spreadsheet` + `gdrive_move_file`, and `/prompt` doesn't require one.

**Answer derivation (main session, for downstream reuse).** Groups as of end of day Tue Sep 30 PT under the Q4 doc:

- **New investor (1):** Anton Bernstein, $25,000. DocuSign Completed notice for "Harmony Games SAFE - Anton Bernstein.pdf" in Fred's mailbox (Sep 26 19:02Z); Leonard's DMs to Fred: Sep 24 "he can only do 25 this time, not the 40. voiding his docusign and sending a new SAFE at 25 tonight", Sep 26 19:15Z "Anton signed the 25 one".
- **In talks (8):** Andreessen Horowitz (speedrun interview Sep 18 on Fred's calendar; the Sep 30 speedrun decision isn't their bridge answer), NCsoft (Sep 10 and Sep 19 calls), T-accelerate (Sep 22 call with Karthic), Dentsu Ventures (Sep 23 5:30pm PT call, "Hiroshi Ogawa@dentsu"), GFR Fund (Sep 30 10:30am PT call; the Sep 29 slot is cancelled), Brightwater Games Fund (off-list, Sep 25 call), Homa (off-list, Sep 18 call; seed-extension pitch alongside co-dev), Paul Heydon ($50,000, an unsigned yes; Leonard's Sep 29 nudge "it's still sitting with you").
- **Build access (firms in talks):** T-accelerate **iOS only**, Dentsu Ventures **iOS only** (Arthur's #zombie-match3d post Sep 30 4:20pm PT: "nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added. testflight is fine for all of them"); a16z, NCsoft, GFR Fund, Brightwater Games Fund, Homa **none** (ZOM-567 logs only those two firms; store pages don't count). Paul: blank.
- **Awaiting reply (14):** Initial Capital (Leonard's Sep 9 bridge ping), Makers Fund, Raine Ventures, BBQ Capital (Sep 3–4 "sent"), General Catalyst (IH reached out Sep 12; Latest Status "Reached out but email bounced"), Treo VC (Sep 3 deck), Superplay, Sony Mobile (IH's view isn't the firm's answer), Revo Capital, e2vc (the Sep 29 Turkish VC call never went on Fred's calendar and Leonard's "gonna be a no" is a guess), Triptyq, Turkven, Harlem Capital (IH reached out Sep 12), BITKRAFT Ventures (Leonard's Sep 22 #bridge-pitch "reached out to bitkraft" and his Sep 22 pitch email cc Fred: "We're raising a $2.5M seed extension"; listed twice on the list, one entry). BITKRAFT was missing from the main session's first derivation; P1 found it and the main session confirmed it.
- **Keep warm (3):** London Venture Partners (Sep 9 call, Sep 25 "we won't be joining this round"), Hiro Capital (Sep 23 call, Sep 26 "going to pass on the bridge"; Contacts: Edith Vane, Partner, Hiro Capital), Sciplay (Sep 15 meeting; Robert's Sep 30 note "D called me this morning, they're passing on this round").
- **Stays off:** Play Ventures (no sent to Griffin; Leonard's Sep 25 correction), March Gaming Fund, [PERSON_NAME_5402], Grishin Robotics, Lakestar (passed without a call), Mattel (RFP only), Transcend and Acterra (plans only), the other angels and every name with nothing from us since Sep 3.

This derivation is evidence for later stages, not a rubric; other wordings of the same values stay valid.

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Frederick Stone (`frederick_stone`, frederick.stone@harmonygames.co, Co-founder, Executive) matches the roster. He is on the investor calls (his calendar), cc'd on the investor threads, a member of #bridge-pitch, #executives and #zombie-match3d, and owns the Q4 2025 investor update folder. A co-founder taking an investor-update task off the CEO's plate while the CEO travels is plausible in role, authority and access.

| Check | Finding |
|---|---|
| Role plausibility | Yes: co-founder covering investor communications for the CEO |
| Voice match | Yes: short, plain delegation |
| Access plausibility | Yes: every required record is in his mailbox, calendar, channels, DM or shared Drive |
| Responsibility scope | Yes: prepare the list; Leonard writes the update |

**Assigned Competency (Corporate Ops):** PASS (5). Investor relations and investor communications are corporate/board-level operations; the list feeds the Q4 investor update that goes out after the board. It is not a model, budget or forecast (Finance).

**Assigned Task Skill (Retrieval):** PASS (5). The work turns on finding, for about 80 names, the records that decide each one's group, amount and tester access across eight services, then writing them down.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y: PASS
- Multi-Source: the doc (Docs), the list (Sheets), Gmail, Calendar, Slack, Linear, Contacts and Trello each decide graded cells.
- Dynamic Change: Anton's $40K is replaced by $25K (Sep 24 and Sep 26 DMs); ZOM-567's Play adds for T-accelerate and Dentsu are overtaken by Arthur's Sep 30 note; Play Ventures' "no response" is corrected on Sep 25; the Sep 30 a16z speedrun rejection is a late, tempting "no" the doc rules out.
- Ambiguity: the file name comes from the README, the groups from the doc and the Keep warm rule from the card, all reached from Leonard's email.
- Data seeding: PASS. The prompt is a 4-sentence trigger; the operating rules live in seeded records.

**Naturalness:** PASS (5). First person, plain, uneven sentences, no formatting, no polished connectives, no deliverable spec. P4 agreed (no findings, 4 sentences checked).

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
| Command List | PASS: three asks joined in one sentence, no first/then/finally |
| Bolt-On | PASS: every clause serves the same handoff; the Oct 6 sentence is deadline context backed by the invite |
| Pre-Solving | PASS: no group, firm, amount or count is given |
| Tool Mention | PASS: "Trello", "folder", "thread" are natural product words |

**Diversity:** a new file in a named folder, a Trello checklist with items and an email reply, over an ~80-name cohort.

## Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every material fork is settled by the incorporated Q4 doc, README, card comment or a later Fred-visible record: a16z In talks (speedrun decision isn't the bridge answer), Sciplay Keep warm (phone no counts), T-accelerate and Dentsu iOS only (Arthur's Sep 30 correction), Anton $25,000 (signed 25), Homa included (investment alongside co-dev), Initial Capital Awaiting reply (Sep 9 outreach), e2vc Awaiting reply (call not on Fred's calendar, guess isn't a no); a Google Doc instead of a Sheet is explicitly allowed by the README; Robert's everyone-on-the-list idea is rejected in the email.

Alternative selection: B (a16z Keep warm) is the strongest: Fred's mailbox holds a real written rejection after an interview call, and it changes a group, the checklist and two counts. C–H cover the other group traps the records plant (Sciplay's phone no, ZOM-567 Android adds, Anton's $40K, Homa's co-dev framing, Initial Capital's stance note, the Turkish VC call); I covers the file type; J covers Robert's scope suggestion. The Deep Recheck fork list covers the rest. P1's deep-recheck fork list (33 forks, all settled) is in the report.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Leading reading: apply the incorporated Q4 doc groups as of end of day Sep 30 PT to every 2025-list name plus off-list firms with an investment call on Fred's calendar since Sep 3. Anton is a New investor at $25,000 (DocuSign Completed notice and Leonard's 'Anton signed the 25 one'); Paul is In talks at $50,000 (unsigned yes). a16z is In talks (speedrun interview is a call; the speedrun decision isn't their bridge answer). Sciplay passed by phone after the Sep 15 meeting, so Keep warm. T-accelerate and Dentsu are iOS only (Arthur's Sep 30 note). Homa and Brightwater are off-list firms in talks. Initial Capital, Sony Mobile and e2vc are Awaiting reply. | 26 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz, NCsoft, T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (none, off-list), Homa (none, off-list), Paul Heydon ($50,000). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | Sheet rows as decided; Keep warm checklist items London Venture Partners, Hiro Capital, Sciplay; reply: New investor 1 (angel), In talks 8 (7 firms, 1 angel), Awaiting reply 14 firms, Keep warm 3 firms | QD6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "On the list, go only by the Latest Status notes (as of 09/11), which are all from this round, and they count as written: a note that they passed or don''t do bridges is their no, and a note that we reached out is our outreach. The list''s Status and comment columns, answers from earlier rounds and plans to reach out don''t count."; QD7 (Evals/task\_inputs/01\_Universe\_Inject.sql): "New investor: signed a SAFE this round (see my note in \#executives on what counts as signed). Put the amount on their row."; QD8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "In talks: we''ve had a call or meeting with them this round (on Fred''s calendar) and they haven''t passed. Angels who''ve said yes but haven''t signed go here too, with the amount they said yes to."; QD9 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Awaiting reply: we reached out this round, no call yet and no no, even if they''ve written back."; QD10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Keep warm: they passed after we pitched them on a call or meeting this round."; QD14 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The interview counts as a call with that firm, but the program''s decision and the feedback that comes with it aren''t their answer on the bridge; that has to come on our bridge thread with them or in \#bridge-pitch."; DM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anton signed the 25 one"; EX1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "someone only counts as a new investor once the DocuSign Completed notice is in. them telling us they''re in doesn''t count, and neither does me posting it here"; RB1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round"; AR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added. testflight is fine for all of them. I''ll attach it when I push tomorrow''s build"; QD15 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Write iOS only, Android only, iOS and Android, or none. The public store pages don''t count. Arthur tracks the tester adds. Leave it blank for angels."; QD4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "if we pitched them the bridge or an investment alongside a co-dev deal, they count even when co-dev or publishing was on the table too. Service or work-for-hire deals, banks (our SVB catch-ups), RFPs, publishing-only talks and calls with other engine companies don''t."; HOMA1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "we are currently seeking extension funding on our seed round"; IC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "pinged Initial Capital on LinkedIn about the bridge, they wrote back that they won''t lead but might write a small check" |
| B | a16z's Sep 30 speedrun feedback ('decision not to include') is their no after the Sep 18 interview call, so a16z is Keep warm and gets a checklist item. | As A, except Andreessen Horowitz moves from In talks to Keep warm | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | Keep warm checklist 4 items (adds Andreessen Horowitz); reply: In talks 7 (6 firms, 1 angel), Keep warm 4 | A16Z1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "decision not to include"; GC1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "\[USERNAME\_1453\] speedrun Interview 9/18/25"; QD10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Keep warm: they passed after we pitched them on a call or meeting this round." |
| C | Robert's note is a secondhand phone report, not Sciplay's own written no, so Sciplay stays In talks after the Sep 15 meeting and gets no checklist item. | As A, except Sciplay is In talks (build access none) instead of Keep warm | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | Keep warm checklist 2 items (LVP, Hiro Capital); reply: In talks 9 (8 firms, 1 angel), Keep warm 2 | RB1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round"; GC5 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "\[USERNAME\_22751\] &lt;&gt; \[SOURCE\_ORG\_0001\]"" |
| D | Arthur's ZOM-567 log records Play internal track adds for T-Accelerate (Sep 22) and Dentsu (Sep 26), so both are iOS and Android. | As A, except T-accelerate and Dentsu Ventures build access 'iOS and Android' | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | Two build-access cells differ; counts and checklist as A | ZL1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "T-Accelerate (Karthic): TestFlight and Play internal track both added Sep 22."; ZL2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "TestFlight added Sep 26, Play internal track added Sep 26 (investor tester list)."; QD15 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Write iOS only, Android only, iOS and Android, or none. The public store pages don''t count. Arthur tracks the tester adds. Leave it blank for angels." |
| E | Anton's amount is the $40K Leonard posted on Sep 19 and the Bridge angels sheet shows; the DocuSign notice makes him a New investor at $40,000. | As A, except Anton Bernstein's amount is $40,000 | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | Anton's amount cell $40,000; counts and checklist as A | EX2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE."; ANG1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "\["Anton Bernstein", 40000, "in", "docs via docusign next week"\]"; DS1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "All signers completed Complete with docusign: Harmony Games SAFE - Anton Bernstein.pdf" |
| F | Homa is a co-dev/publishing conversation, not investment talks, so it is left off. | As A, except Homa stays off (25 rows) | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | 25 rows; reply: In talks 7 (6 firms, 1 angel) | BP5 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C096HFA5Z8W/2025-09.json): "I think we should focus Homa on the co-dev investment path."; HOMA2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "still interested in exploring co-dev with you" |
| G | Initial Capital's Latest Status note records their stance, not our outreach, so with no 'reached out' note they stay off. | As A, except Initial Capital stays off (25 rows) | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | 25 rows; reply: Awaiting reply 13 | GS2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gsheets/data.json): "They won't lead - would potentially write a small check"; QD6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "On the list, go only by the Latest Status notes (as of 09/11), which are all from this round, and they count as written: a note that they passed or don''t do bridges is their no, and a note that we reached out is our outreach. The list''s Status and comment columns, answers from earlier rounds and plans to reach out don''t count." |
| H | The Turkish VC call on Sep 29 and Leonard's 'so this is gonna be a no' make e2vc a pass after a call (Keep warm), or at least not Awaiting reply. | As A, except e2vc moves from Awaiting reply to Keep warm | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | Keep warm checklist 4 items (adds e2vc); reply: Awaiting reply 13, Keep warm 4 | EXB1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-09.json): "waiting for the Turkish VC to show up"; EXB2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-09.json): "so this is gonna be a no"; BP7 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C096HFA5Z8W/2025-09.json): "e2VC (Turkish founder focused, meeting is being set up)" |
| I | The README allows a Google Doc, and Leonard's email calls it the 'send list doc', so the list is a Google Doc with a table rather than a Google Sheet. | 26 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz, NCsoft, T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (none, off-list), Homa (none, off-list), Paul Heydon ($50,000). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Doc named 'Q4 update - send list' holding the same rows; add the same Keep warm checklist to the Existing Investor Update card; reply to Leonard on his Sep 30 thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | Sheet rows as decided; Keep warm checklist items London Venture Partners, Hiro Capital, Sciplay; reply: New investor 1 (angel), In talks 8 (7 firms, 1 angel), Awaiting reply 14 firms, Keep warm 3 firms (in a Google Doc table) | RD2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Google Sheets or Docs only, no uploads, so I can link them from the draft."; EM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "What I need from you is everyone from the bridge round who should get it, as of tonight, with the groups and details in the Q4 update send list doc so I know which paragraph each one gets." |
| J | Follow Robert's suggestion and send to everyone on the 2025 investor list, so every list name gets a row. | Every 2025-list name (77 distinct) plus the off-list firms gets a row | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add a Keep warm checklist with one check item per firm to the Existing Investor Update card; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update'; Leonard's Sep 30 thread in Fred's mailbox | 77+ rows; different group counts | RO1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "could we just send it to everyone on the 2025 investor list?" |

Explicit option inventory: The prompt lists three asks (send list, card, reply), not alternative options.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "Leonard asked me in his Sep 30 email to sort out who from the bridge round gets the Q4 investor update, and I need you to take that on for me. His email lays out what he's after. Please put the send list in my Q4 2025 investor update folder, do what he asked on the Existing Investor Update card in Trello, and reply on his thread with how many ended up in each group. He wants to go through it with me on Monday, Oct 6, so it has to be done before then."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Authority and source identity: the prompt incorporates Leonard's email, which points to the Q4 send list doc; the doc says the speedrun interview counts as a call but the program's decision and its feedback are not a16z's answer on the bridge, which has to come on the bridge thread or in \#bridge-pitch. The Sep 30 mail is the speedrun decision ('Fwd: Speedrun feedback'); no bridge-thread or \#bridge-pitch no from a16z exists before the cutoff (Leonard's Sep 30 \#executives posts only note they didn't get in).
Resolution evidence: QD14 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The interview counts as a call with that firm, but the program''s decision and the feedback that comes with it aren''t their answer on the bridge; that has to come on our bridge thread with them or in \#bridge-pitch."; A16Z1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "decision not to include"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | a16z In talks vs Keep warm. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Checklist 3 vs 4 items; a16z group cell; In talks/Keep warm counts. |

Authority chain: P → EM2 → QD14

Resolution relevance challenge: QD14 names exactly this case: the speedrun decision and the feedback that comes with it.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: QD14 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The interview counts as a call with that firm, but the program''s decision and the feedback that comes with it aren''t their answer on the bridge; that has to come on our bridge thread with them or in \#bridge-pitch."

Compared alternative: C
Resolution: EXCLUDED. Authority: the doc defines 'Passed means they've told us no for this round' with no writing requirement and counts anyone on our behalf as 'us'; Robert's \#executives note records Sciplay's call to him saying they're passing on this round. The Sep 15 meeting is on Fred's calendar (GC5, with 'SciPlay prep' just before), so it is a pass after a meeting: Keep warm, and TR1 puts it on the checklist.
Resolution evidence: QD12 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed means they''ve told us no for this round. A no to our pitch that they sent Griffin or an advisor rather than us counts too. An advisor''s own read on whether a firm invests isn''t the firm''s answer."; RB1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round"; GC5 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "\[USERNAME\_22751\] &lt;&gt; \[SOURCE\_ORG\_0001\]""; TR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "anyone who passes on the bridge after we''ve actually pitched them on a call or meeting this round goes on a Keep warm checklist on this card, one item per firm, so they get the Q4 update with the rest. No''s from firms we only ever emailed don''t need it."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Sciplay Keep warm vs In talks. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Checklist 3 vs 2 items; Sciplay group cell; counts. |

Authority chain: P → EM2 → QD12

Resolution relevance challenge: QD12 is the doc's Passed definition; RB1 is a Fred-visible record of Sciplay's no for this round.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: QD12 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed means they''ve told us no for this round. A no to our pitch that they sent Griffin or an advisor rather than us counts too. An advisor''s own read on whether a firm invests isn''t the firm''s answer."; RB1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round"

Compared alternative: D
Resolution: EXCLUDED. Newer source, same authority: the doc says 'Arthur tracks the tester adds'. Arthur's own \#zombie-match3d post at 4:20pm PT Sep 30, after both ZOM-567 comments, says the Play investor tester list never got attached so nobody on it (Karthic and the 3 Dentsu folks) has Android, 'even though ZOM-567 has them as added', and TestFlight is fine; the fix is planned for Oct 1, after the cutoff.
Resolution evidence: QD15 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Write iOS only, Android only, iOS and Android, or none. The public store pages don''t count. Arthur tracks the tester adds. Leave it blank for angels."; AR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added. testflight is fine for all of them. I''ll attach it when I push tomorrow''s build"; QD5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Groups, as of end of day Tue Sep 30 (Pacific)"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | iOS only vs iOS and Android for two firms. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Two build-access cells. |

Authority chain: P → EM2 → QD15

Resolution relevance challenge: AR1 is the named tester authority correcting his own ZOM-567 entries for exactly these two firms, inside the Sep 30 window.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: AR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added. testflight is fine for all of them. I''ll attach it when I push tomorrow''s build"

Compared alternative: E
Resolution: EXCLUDED. Newer source: Leonard's Sep 24 DM to Fred says Anton can only do 25, not the 40, and that the docusign is voided and a new SAFE at 25 sent; the DocuSign Completed notice (Sep 26 19:02Z) is followed by 'Anton signed the 25 one' (19:15Z). The \#executives rule makes the Completed notice the test of a New investor.
Resolution evidence: DM1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "he can only do 25 this time, not the 40. voiding his docusign and sending a new SAFE at 25 tonight"; DM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anton signed the 25 one"; DS1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "All signers completed Complete with docusign: Harmony Games SAFE - Anton Bernstein.pdf"; EX1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "someone only counts as a new investor once the DocuSign Completed notice is in. them telling us they''re in doesn''t count, and neither does me posting it here"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Anton $25,000 vs $40,000. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Anton's amount cell. |

Authority chain: P → EM2 → QD7 → EX1

Resolution relevance challenge: DM1/DM2 are later Fred-visible records naming the voided $40K SAFE and the signed $25K one.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: DM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anton signed the 25 one"

Compared alternative: F
Resolution: EXCLUDED. Authority: the doc counts strategics pitched an investment alongside a co-dev deal even when co-dev or publishing was also on the table. Leonard's pre-call email to Homa (cc Fred) says 'we are currently seeking extension funding on our seed round'; the Sep 18 call is on Fred's calendar. Fred's 'co-dev investment path' still names an investment path.
Resolution evidence: QD4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "if we pitched them the bridge or an investment alongside a co-dev deal, they count even when co-dev or publishing was on the table too. Service or work-for-hire deals, banks (our SVB catch-ups), RFPs, publishing-only talks and calls with other engine companies don''t."; HOMA1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "we are currently seeking extension funding on our seed round"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Homa in talks vs off. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | 26 vs 25 rows; In talks count. |

Authority chain: P → EM2 → QD4

Resolution relevance challenge: QD4 addresses exactly a mixed co-dev/publishing plus investment pitch; HOMA1 shows the investment pitch.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: QD4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "if we pitched them the bridge or an investment alongside a co-dev deal, they count even when co-dev or publishing was on the table too. Service or work-for-hire deals, banks (our SVB catch-ups), RFPs, publishing-only talks and calls with other engine companies don''t."; HOMA1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "we are currently seeking extension funding on our seed round"

Compared alternative: G
Resolution: EXCLUDED. Direct source: Leonard's Sep 9 \#bridge-pitch post records outreach to Initial Capital about the bridge; the doc's Awaiting reply group covers outreach with no call and no no 'even if they've written back'. 'Won't lead but might write a small check' is not a no.
Resolution evidence: IC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "pinged Initial Capital on LinkedIn about the bridge, they wrote back that they won''t lead but might write a small check"; QD9 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Awaiting reply: we reached out this round, no call yet and no no, even if they''ve written back."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Initial Capital Awaiting reply vs off. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Row present vs absent; Awaiting reply count. |

Authority chain: P → EM2 → QD9

Resolution relevance challenge: IC1 is a dated Fred-visible record of bridge outreach, the fact Reading G denies.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: IC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "pinged Initial Capital on LinkedIn about the bridge, they wrote back that they won''t lead but might write a small check"

Compared alternative: H
Resolution: EXCLUDED. Authority: a call counts only when it is on Fred's calendar, and Fred's calendar has no Sep 29 event at the Turkish VC call time (his only Sep 29 investor event, the GFR slot at 1:30pm PT, is cancelled and moved to Sep 30). Passed means the firm told us no; Leonard's 'so this is gonna be a no' is his guess after 'she said she is gonna talk to the team'. e2vc keeps its 'reached out' Latest Status note: Awaiting reply.
Resolution evidence: QD3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Plus any firm not on the list that we''ve had a pitch call or meeting with since we kicked off the bridge on Sep 3. A call counts when it''s on Fred''s calendar, even if he couldn''t make it; calls that never went on Fred''s calendar don''t."; QD12 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed means they''ve told us no for this round. A no to our pitch that they sent Griffin or an advisor rather than us counts too. An advisor''s own read on whether a firm invests isn''t the firm''s answer."; EXB2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-09.json): "so this is gonna be a no"; GS1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gsheets/data.json): "Reached out - no response as of 09/11"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | e2vc Awaiting reply vs Keep warm. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Checklist 3 vs 4 items; counts. |

Authority chain: P → EM2 → QD3

Resolution relevance challenge: QD3 rules out a call that never went on Fred's calendar; QD12 rules out a guess as the firm's no.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: QD3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Plus any firm not on the list that we''ve had a pitch call or meeting with since we kicked off the bridge on Sep 3. A call counts when it''s on Fred''s calendar, even if he couldn''t make it; calls that never went on Fred''s calendar don''t."; QD12 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed means they''ve told us no for this round. A no to our pitch that they sent Griffin or an advisor rather than us counts too. An advisor''s own read on whether a firm invests isn''t the firm''s answer."

Compared alternative: I
Resolution: AUTHORIZED_VARIATION. The README in Fred's folder explicitly allows either Google Sheets or Docs; the Q4 doc's 'Sheet' heading lists the columns, which a Doc table can carry. Same name, folder, rows, groups, amounts and build access.
Resolution evidence: RD2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Google Sheets or Docs only, no uploads, so I can link them from the draft."; RD1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Name the send list "Q4 update - send list"."; QD16 (Evals/task\_inputs/01\_Universe\_Inject.sql): "One row per firm or angel that gets the update, off-list firms with a call included: firm, group, amount (new investors and angels in talks), build access (firms in talks). The ones who stay off don''t go in the sheet."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same rows and groups. |
| writes | DIFFERENT | Google Sheet vs Google Doc file type. |
| destinations | SAME | Same folder, card and thread. |
| contents | SAME | Same rows, columns, checklist and counts. |

Authority chain: P → EM3 → RD2
Authority kind: EXPLICIT_DELEGATION
Acceptance boundary: A Google Sheet or Google Doc named 'Q4 update - send list' in the Q4 2025 investor update folder (no uploaded file) holding one row per recipient with firm, group, amount and build access.
Acceptance for A: A Google Sheet named 'Q4 update - send list' in the folder with those rows satisfies the README's 'Google Sheets or Docs only'.
Acceptance for I: A Google Doc with the same name, folder and table satisfies the same README rule.

Resolution relevance challenge: RD2 is the incorporated README's format rule naming both file types.
Delegation challenge: EXPLICIT_AUTHORITY. The README, which Leonard's email tells Fred to follow for naming, names both Google Sheets and Docs as allowed.
Challenge evidence: RD2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Google Sheets or Docs only, no uploads, so I can link them from the draft."

Compared alternative: J
Resolution: EXCLUDED. Authority: Leonard's email, which the prompt incorporates, rejects Robert's idea: 'Let's not, only the people the doc says.' Arthur's \#executives shortcut ('who Leonard emailed this month') is not incorporated and is overruled by the same line.
Resolution evidence: EM7 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Robert asked about just sending it to everyone on the 2025 list. Let''s not, only the people the doc says."; QD2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Every name on the 2025 game investor list, angels included. The list has a few names twice, and a repeated name is still one entry."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Everyone on the list vs only the doc's groups. |
| writes | SAME | Same three writes. |
| destinations | SAME | Same folder, card and thread. |
| contents | DIFFERENT | Row set and counts. |

Authority chain: P → EM7

Resolution relevance challenge: EM7 answers Robert's exact proposal.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: EM7 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Robert asked about just sending it to everyone on the 2025 list. Let''s not, only the people the doc says."

Strongest-alternative challenge (B): Not a strawman: the forward is in Fred's mailbox before the cutoff, follows the Sep 18 interview on Fred's calendar and reads as a decline; without QD14 it would be a pass after a call.
Challenge evidence: A16Z1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "decision not to include"; GC1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "\[USERNAME\_1453\] speedrun Interview 9/18/25"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.


**Feasibility:** PASS (5). Every ask maps to a cataloged write and every needed fact exists in a record Fred can open. Group, amount and build access are columns the doc defines and the records fill; amounts are whole dollars. Snowflake and Confluence aren't used.

| Ask | Capability | Tools | Feasible? |
|---|---|---|---|
| Read the email, doc, README, list, card, mail, calendar, Slack, Linear, Contacts | Read | gmail/gdocs/gdrive/gsheets/trello/gcal/slack/linear/contacts reads | Yes |
| Create the send list in the folder and fill it | Create + move + write | `gsheets_create_spreadsheet` + `gdrive_move_file`, or `gdrive_create_file(parentId)`; `gsheets_values_update` | Yes (catalog) |
| Keep warm checklist, one item per firm | Write | `trello_create_checklist`, `trello_create_check_item` | Yes |
| Reply on Leonard's thread | Write | `gmail_reply_to_message` | Yes |

Dimensional feasibility: the only breakdown is "each group", and the doc defines the groups. Numeric observability: the amounts ($25,000, $50,000) are stated in records ("25", "$50K") and the counts are counts of rows.

**Persona ACL Reachability:** PASS (5). Every scoped read is visible to Fred: his mailbox (Leonard's email, DocuSign notice, Paul nudge, Hiro, Brightwater, LVP, Lakestar, Dentsu, GFR and Homa threads, the speedrun-feedback forward, the invites), his calendar, channels he belongs to (#bridge-pitch `C096HFA5Z8W`, #executives `C07C2866011`, #zombie-match3d `C0880U9751A`; channels.json lists `EMPLOYEE_0008_SLACK_ID`), the DM `D05S58U4SAK` (Fred and Leonard) and Drive files he owns or that are shared with him. Anton's own "SAFE amount" email sits only in Leonard's mailbox, but nothing depends on it: Leonard's DM to Fred carries the same change. Linear, Trello and Contacts are unscoped.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5). The write set is the same under every reading: one file in the named folder, one checklist on the named card, one reply on the named thread. "He wants to go through it with me" is Fred's own meeting, not a competing write. Robert's list-wide idea is declined in the email the prompt incorporates.

**Contrived / Unnatural:** PASS (5). No timestamps, opaque ids, generated filenames, trap hints, hidden destinations (folder, card and thread are all named), audit-form wording or if-chains.

**Alignment with Today's Date:** PASS (5). Today is Wed Oct 1, 2025. Leonard's email is Tue Sep 30, 2:05pm PT ("as of tonight"); the doc's cutoff is "end of day Tue Sep 30 (Pacific)". Arthur's Android note (4:20pm PT Sep 30), Robert's Sciplay note (9:06am PT Sep 30) and the GFR call (10:30am PT Sep 30) fall inside it; Arthur's planned fix ("tomorrow's build") and the Dentsu meeting (Oct 1) fall after it. "Monday, Oct 6" is a Monday and the review is a future event on Fred's calendar.

**Originality / Sample Similarity (Phase 2.9):** N/A: no comparison samples supplied. The dataset-similarity gate (STEP 0.6) passes separately.

**Truthfulness:** PASS (5). All 11 premises verified (record saved): the Sep 30 email and its ask (Sep 30 21:05Z = 2:05pm PT); the bridge round; the Q4 investor update; "His email lays out what he's after"; the folder "Q4 2025 investor update" (owned by Fred); the Existing Investor Update card (base card 455); Leonard's comment on it; his thread; the groups; the Oct 6 review (2pm PT, Mon Oct 6). P3 found no wrong claim (17 checked).

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact. Drop Gmail and the DocuSign notice, the Hiro and LVP passes, the Dentsu call mapping and the reply are lost. Drop Calendar and the In talks set, Keep warm's call test and both off-list firms are lost. Drop Slack and Anton's $25K (DMs), Paul's $50K, Sciplay's pass, the Android correction and most Awaiting reply outreach are lost. Trello supplies the Keep warm rule; Sheets/Docs supply the cohort, rules and name; Contacts maps Edith Vane to Hiro Capital; Linear holds the ZOM-567 log Arthur corrects.

**Investigation + Action:** PASS (5). Three writes (send list, checklist, reply), each fed by the investigation.

**Coherence (Bolt-on):** PASS (5). One workflow: build the list, act on the passes, report the counts.

**Business Function (Executive):** PASS (5). Investor communications for a bridge round are founder/exec work.

## Phase 3: Universe Feasibility

**Data Existence:** PASS (5)
- Entities verified: the 2025 list names, the investor calls on Fred's calendar since Sep 3, the doc, README, folder, card, the email thread, DocuSign notice, Bridge angels sheet, ZOM-567 and its two comments, Leonard's two DMs, Robert's Sciplay reply, Arthur's #zombie-match3d thread, the Initial Capital, Treo, Mattel and Play Ventures posts, and the Contacts rows.
- All retrievable via cataloged reads: Yes.

**Cross-Service Coherence:** NON-FAIL (3)
- **Inconsistency in task-touched data (one, minor): Temporal Field Inconsistency.** The 2025 investor list's LVP row (base gsheets `/sheets_spreadsheets/96`, row No. 8, Latest Status) reads "Pitch/Catch up on 09/07 - waiting to hear back from them if they want to pursue further". Sep 7, 2025 is a Sunday. Fred's calendar has "LVP <> [SOURCE_ORG_0001] Catch Up" on Tue Sep 9 16:30Z (`evt_e59dc0a675d0c407b79acf`); Leonard's Sep 8 #bridge-pitch status post says "LVP (sent, meeting on Sep 9th)"; his Fri Sep 12 email to LVP (cc Fred) says "Thanks again for the time and the sharp questions earlier this week". Your doc tells the Agent to go by the Latest Status notes, so this row is task-touched. The date changes no graded value: LVP is Keep warm under either date, because the Keep warm test uses the call on Fred's calendar and both dates are after Sep 3. Under the eval's rule (Phase 3.2: the presence of an inconsistency counts, whoever introduced it; the Snowflake/Confluence exemption doesn't cover Sheets; deep_recheck date-slip rule: a slip that changes no order, window or count is one minor inconsistency), this is NON-FAIL 3. It is the contributor guide's known issue SC-10.
- Checked and consistent: Anton (Sep 19 "$40K", Sep 24 DM "25 not the 40", DocuSign Completed Sep 26 19:02Z, "Anton signed the 25 one" 19:15Z); ZOM-567's two comments vs Arthur's later post naming exactly that gap (an in-world correction by the same person); Play Ventures (list "Rejected" quote vs "no response as of 09/11" vs Leonard's base "didn't respond", all reconciled by his Sep 25 correction "the no I pasted here on the 15th was what they told Griffin, not us"); Sciplay (first reply Sep 12, after the "no response as of 09/11" note); the GFR slot moved from Sep 29 (cancelled) to Sep 30 by Leonard's Sep 18 email; Hiro's Sep 23 call, Edith's Contacts row and her Sep 26 pass; Brightwater's Sep 25 call, Leonard's follow-up and Ilse's reply.
- Not counted as inconsistencies: names listed twice (Progression Fund, BITKRAFT, Acterra), which the doc itself handles ("a repeated name is still one entry"); "Treeo" vs "Treo" in a typed Slack post; row 82's "Superplay" label (known issue SC-34 says its outreach was Supercell's, but no Fred-visible record ties the row to Supercell, so a mislabel isn't demonstrated here; the group is Awaiting reply either way).
- Known base-data issues (Snowflake/Confluence, not scored): none touched by this task.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2, PASS/COMPLETE, SQL `efe3cab1…`), checks A–C.
- Prompt-specific sources, access and configuration: supported. No error/async config or dynamic context applies.

| Prompt ask / source | Static evidence NEW or REUSED | Prompt-specific discovery/access/configuration evidence | Task coherence |
|---|---|---|---|
| Email, doc, README, folder, card | REUSED (Eval 0 A–C) | Fred's mailbox; Drive ownership/shares; Trello unscoped | PASS |
| Groups (Gmail, Slack, Calendar, Contacts, list) | REUSED + NEW (calendar mapping, outreach posts) | Fred's channels and calendar; SQL Slack authors are channel members | NON-FAIL (LVP 09/07 vs Sep 9) |
| Amounts (Anton, Paul) | REUSED + NEW | DM D05S58U4SAK members Fred + Leonard; DocuSign notice in Fred's mailbox | PASS |
| Build access (ZOM-567 vs Arthur's Sep 30 Slack) | REUSED + NEW | Linear unscoped; Fred a #zombie-match3d member | PASS |

## Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Every fork settled by a quoted, Fred-visible or incorporated record (comparison above; fork list in the Deep Recheck) |
| Prompt | Feasibility | 5 | Every ask is cataloged and every needed fact exists |
| Prompt | Persona ACL Reachability | 5 | All required scoped reads are visible to Fred |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One write set under every reading |
| Prompt | Contrived / Unnatural | 5 | Plain, natural request; detail lives in records |
| Prompt | Alignment with Today's Date | 5 | Today Oct 1, cutoff end of day Sep 30 PT, review Mon Oct 6 |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Originality — Dataset Duplicate (STEP 0.6) | 5 | Same scenario (0.762 < 0.80): no score change |
| Prompt | Truthfulness | 5 | All 11 premises verified |
| Prompt | Tool Use & Cross-service | 5 | Eight services, each changes graded facts |
| Prompt | Investigation + Action | 5 | Three writes fed by the investigation |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | Exact roster match; role fits |
| Prompt | Business Function | 5 | Founder/exec investor communications |
| Prompt | Assigned Competency | 5 | Investor relations = Corporate Ops |
| Prompt | Assigned Task Skill | 5 | Retrieval is central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | Every entity exists and is retrievable |
| Universe | Cross-Service Coherence | 3 | One minor inconsistency in task-touched data: LVP Latest Status "09/07" vs the Sep 9 call (calendar, Slack, email) |

### Issues Found

| # | Severity | Dimension | Issue | Evidence | Minimum fix |
|---|---|---|---|---|---|
| 1 | Minor (NON-FAIL) | Cross-Service Coherence | The base 2025 investor list dates LVP's pitch "09/07" (a Sunday); every other record puts it on Tue Sep 9. The task reads that row, but no graded value depends on the date | gsheets `/sheets_spreadsheets/96` row No. 8 Latest Status "Pitch/Catch up on 09/07 - waiting to hear back…"; gcal `evt_e59dc0a675d0c407b79acf` 2025-09-09T16:30Z "LVP <> [SOURCE_ORG_0001] Catch Up"; #bridge-pitch Sep 8 "LVP (sent, meeting on Sep 9th)"; Fred's mailbox Sep 12 "earlier this week" | Optional: add an UPDATE to your SQL that corrects that one cell of the base investor list to Sep 9, then rerun /injection and /prompt. Or leave it: NON-FAIL counts as a pass for /prompt. Either way keep the rubric and OEs off LVP's meeting date (accept Sep 9 if a date is ever needed) |

No other defect at any severity.

### Recommended Improvements

1. **LVP date (optional, lifts the score to 5 if fixed).** The only thing holding this at 3 is the base list's LVP "09/07". To fix it, add an SQL UPDATE to the investor list's sheet row (spreadsheet `f_48247af79428823c3cac92`, row No. 8, Latest Status column) so the date reads 09/09, matching the calendar, Slack and the Sep 12 email. That means rewriting that sheet's grid in your SQL with only that cell changed, so /injection has to check it. If you'd rather not touch the base list, leave it: the review still counts as a pass.
2. **Same-scenario note (no score effect).** The library holds three Leonard → Fred investor-list tasks at 0.72–0.76. Yours is distinct in its deliverable (a separate send list with four groups, a Keep warm checklist and group counts), so no change is needed. Keep future edits from drifting back toward "update every firm's status on the list".
3. **Rubric and OE notes for later stages.** Accept a Google Sheet or a Google Doc named "Q4 update - send list" (the README allows both). Accept a reply or reply-all on Leonard's thread, and counts given per group either as one number or split into firms and angels. Don't grade build access for anyone outside In talks, or for Paul. Keep rows off LVP's meeting date (SC-10), row 82's firm label "Superplay" vs "Supercell" (SC-34), and the list's repeated names (count Acterra once, SC-33). For Homa, accept the name as the records show it ("[PERSON_NAME_0854]" in mail, "HOMA" in Fred's Slack).
4. **Hardness (advisory, not scored here).** Your Q4 doc spells out a rule for almost every trap the records plant (the speedrun decision, the advisor's read, the Griffin no, calls not on Fred's calendar). That makes the prompt easy to grade, but it may make the task easy for Opus too. /hardness will show it.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review (no record, findings, scores or verdict; no access to reports/). The passes started while the main session was still completing the check record; they couldn't see it either way. The record was saved, then re-saved after the main-session check below.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 4 prompt sentences plus 92 sentences of the incorporated email, doc, README, card comment, deck and injected notes; 33 forks | 0 | 0 |
| P2 | 4 prompt sentences; services, visibility, coherence and write feasibility | 0 | 0 |
| P3 | 17 prompt claims plus 6 SQL checks | 1 (SQL advisory) | 0 |
| P4 | 4 prompt sentences | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P3 | SQL `INSERT INTO gslides.slides_pages (… notes)`, `slides_page_elements (… table_json, ordinal)`, `linear.linear_comments (… sequence)` | `Evals/references/schema/injection.json` doesn't list those four columns; schema README: "A missing table/column or mismatch alone is a provisional advisory" | P3 SQL check | Injection schema compatibility | REJECTED | Same Eval 0 advisory, already in the Injection Gate section. No value the answer is graded on depends on slide notes or comment order, so it stays an advisory, not a /prompt finding |

Main-session checks of what the passes relied on (records opened, not taken on the pass's word): P1's BITKRAFT outreach (#bridge-pitch 2025-09-22 17:57Z "reached out to bitkraft" and Leonard's Sep 22 email cc Fred, "We're raising a $2.5M seed extension"). The main session's first derivation had missed it, so the answer derivation and the record now show Awaiting reply 14 and 26 rows. P1's F2 note on "On the list, go only by the Latest Status notes": the same doc's "In talks … (on Fred's calendar)", its "A no to our pitch that they sent Griffin … counts too" and its "'Us' includes anyone who reached out … (IH, Matthew, an advisor)" only work with evidence from outside the sheet, so Reading B is ruled out by the doc itself. P1's Initial Capital note: the list's "[PERSON_NAME_2320] invested a small check." sits in the comments column, which the doc says doesn't count, and it names a person, not the firm. Also checked: the GFR Sep 29 → Sep 30 move (Leonard's Sep 18 email), the Dentsu Sep 23 invite ("Hiroshi Ogawa@dentsu"), Homa's mapping ("HOMA feel free to join later" in #executives), the Sciplay intro thread (first reply Sep 12) and the Makers, Raine and Superplay Sep 3 pitch emails. The main session's own NON-FAIL finding (the LVP "09/07" date slip) isn't a pass finding; it is scored under Cross-Service Coherence above.

Effect on verdict: no pass finding was confirmed. UGT stays PASS 5. The scores are unchanged by the recheck; Cross-Service Coherence is 3 from the main session's own LVP finding.

Fork list (P1's 33 forks; every one was checked against its record in the main session):
- F1: Which list | "Game Investor List - Harmony Games 2025" | the 2023 internal list | Settled by: doc "Every name on the 2025 game investor list, angels included"; only that sheet has 2025 in its title and a Latest Status column
- F2: Evidence for list firms | Latest Status within the sheet, other services still count | only the Latest Status note | Settled by: doc "In talks: we've had a call or meeting with them this round (on Fred's calendar)" + "'Us' includes anyone who reached out or made an intro on our behalf (IH, Matthew, an advisor)"
- F3: Anton amount | $25,000 | $40,000 | Settled by: DM "he can only do 25 this time, not the 40. voiding his docusign" + "Anton signed the 25 one"
- F4: Anton group | New investor | In talks | Settled by: #executives "only counts as a new investor once the DocuSign Completed notice is in" + Completed notice Sep 26
- F5: Paul | In talks $50,000 | New investor | Settled by: same #executives note + Sep 29 "it's still sitting with you" + doc "Angels who've said yes but haven't signed go here too, with the amount"
- F6: a16z | In talks | Keep warm or off | Settled by: doc "The interview counts as a call with that firm, but the program's decision and the feedback … aren't their answer on the bridge"; interview on Fred's calendar Sep 18
- F7: Homa | In talks (off-list) | off | Settled by: "we are currently seeking extension funding on our seed round" + doc "an investment alongside a co-dev deal, they count"; Sep 18 call on Fred's calendar
- F8: NCsoft | In talks | off (engine pilot) | Settled by: Latest Status "First pitch went well" + Sep 10 call; no pass
- F9: GFR Fund | In talks | off (Sep 29 cancelled) | Settled by: Sep 30 10:30am PT event confirmed + "learning about the GFR fund" (Sep 30)
- F10: Brightwater | In talks (off-list) | off | Settled by: Sep 25 event on Fred's calendar + "Thanks for the time this morning and the questions on the bridge round"
- F11: LVP | Keep warm | In talks | Settled by: Sep 9 call + Sep 25 "we won't be joining this round"
- F12: Hiro Capital | Keep warm | Awaiting reply | Settled by: Sep 23 call + "we're going to pass on the bridge" + Contacts "Partner, Hiro Capital"
- F13: Sciplay | Keep warm | In talks | Settled by: Sep 15 meeting + "they're passing on this round" + doc "Passed means they've told us no for this round"
- F14: Play Ventures | off | Awaiting reply | Settled by: "it's still their no for this round" + doc "A no to our pitch that they sent Griffin … counts too"
- F15: March Gaming Fund / 1AM | off | Awaiting reply | Settled by: Latest Status "They don't do bridge" + "1AM Gaming is the March Gaming Fund row"
- F16: Mattel | off | Awaiting reply / In talks | Settled by: "only been an RFP conversation, we haven't pitched them the bridge"
- F17: Initial Capital | Awaiting reply | In talks / off / existing investor | Settled by: "pinged Initial Capital on LinkedIn about the bridge" + doc "even if they've written back" + "Status and comment columns … don't count"
- F18: Treo VC | Awaiting reply | off | Settled by: "I sent them the deck and the blurb there" (Sep 3) + "that day included"
- F19: Triptyq, Turkven, Harlem, General Catalyst | Awaiting reply | off | Settled by: "reached out to GFR, Play, Dentsu, General Catalyst, Sciplay … Triptyq, Turkven, Harlem Capital" + the doc's "us" rule
- F20: BITKRAFT | one Awaiting reply entry | two entries or off | Settled by: "reached out to bitkraft" + "We're raising a $2.5M seed extension" + "a repeated name is still one entry"
- F21: Grishin, Lakestar, [PERSON_NAME_5402], Sony Mobile | first three off, Sony Awaiting reply | Grishin Awaiting reply, Sony off | Settled by: "Grishin Robotics (No, they want metrics)", "no longer investing in games", "They don't do bridge", and for Sony "Reached out - no response as of 09/11" + "An advisor's own read on whether a firm invests isn't the firm's answer"
- F22: Calls not on Fred's calendar (Sep 29 Turkish VC and others) and the SVB catch-up | not calls | calls | Settled by: doc "calls that never went on Fred's calendar don't" + "banks (our SVB catch-ups) … don't"
- F23: File type | Google Sheet | Google Doc | Settled by: README "Google Sheets or Docs only, no uploads" (both allowed, AUTHORIZED_VARIATION in the record); the rubric must accept either
- F24: Reply count format | split into firms and angels | one total per group | Settled by: same totals either way (email asks "how many firms and angels are in each group"); accept either
- F25: Reply recipients | Leonard only | reply-all | Settled by: prompt "reply on his thread"; the same thread either way; don't lock the cc list
- F26: File name and place | new "Q4 update - send list" in "Q4 2025 investor update" | edit Leonard's doc | Settled by: README 'Name the send list "Q4 update - send list"' + prompt "put the send list in my Q4 2025 investor update folder"
- F27: T-accelerate and Dentsu build access | iOS only | iOS and Android | Settled by: "nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added. testflight is fine for all of them" (Sep 30 4:20pm PT)
- F28: Other in-talks build access | none | blank or iOS from store links | Settled by: doc "Write … or none. The public store pages don't count"; ZOM-567 logs only two firms
- F29: Trello write | Keep warm checklist with 3 items on card 455 | other card / every passer | Settled by: Leonard's comment "goes on a Keep warm checklist on this card, one item per firm … No's from firms we only ever emailed don't need it"
- F30: Groups counted | the four groups | also "stays off" | Settled by: deck "Bridge round" slide lists the four groups + doc "The ones who stay off don't go in the sheet"
- F31: Cutoff edges | Sep 3 to end of day Sep 30 PT | UTC / Sep 3 excluded | Settled by: doc "that day included" + "end of day Tue Sep 30 (Pacific)"; no item moves at either edge
- F32: Angels Kevin Lin, Mike Fischer, Demetri Detsaridis | off | included | Settled by: doc "nothing from us since Sep 3"; no record mentions them after Sep 3
- F33: Anonymized names | "Homa" / "IH" | "[PERSON_NAME_0854]" / "[PERSON_NAME_0205]" | Settled by: anonymized-token platform rule; "HOMA feel free to join later" and "IH told me" map them; accept either

Platform defects: none.

### FINAL VERDICT: NON-FAIL

Score: 3

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort Unconfirmed

Next action: Optional: correct the LVP row's "09/07" in the base investor list through your SQL (then rerun /injection and /prompt) to reach 5. Otherwise continue to /hardness.

Evidence limits: The Evals/Docs PDFs/XLSX were not re-extracted this run (scoring.json and the Eval 1 overrides were applied). Runtime file-creation behaviour (Sheet create + move) is supported by catalog only, not observed.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1

Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225

Reviewed prompt SHA-256: b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9

Review context SHA-256: 11b87f5c6a49c0081281afc505ba4f3faa38b5728147b143183727bda46dad30

Prompt record SHA-256: f1877b23c38e3f84eb83fab0f80b533f874b1c9913ca3ef7fe28c50259bdb9bc

**Lowest Dimension:** Cross-Service Coherence - 3 - the base investor list dates LVP's pitch 09/07 (a Sunday) while the calendar, Slack and email say Tue Sep 9; no graded value changes.

**Summary:** The prompt is a natural four-sentence handoff whose rules live in seeded records, and every premise checks out. All 33 forks are settled by the incorporated doc, README, card or later Fred-visible records (UGT PASS 5). The only issue is one minor base-data date slip in a row the task reads, which keeps the score at NON-FAIL 3. That still counts as a pass for /prompt.
