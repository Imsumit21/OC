# Prompt Quality Review (Eval 1)

## PROMPT EVALUATION REPORT

### Task: Fred takes over Leonard's Q4 investor-update send list for the bridge round: build the send list in his Q4 2025 investor update folder, do what Leonard's two comments on the Existing Investor Update card ask (group checklists, F/up cards in To Do, a comment on an existing To Do card), and reply on Leonard's thread with the per-group counts
### Assigned Persona: Frederick Stone - Co-founder
### Assigned Business Function: Executive
### Assigned Competency: Corporate Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Long Horizon tier, 100–500+ calls; not scored here)

## 1. Scope and inputs

| Item | Value |
|---|---|
| Mode | Chat review, attempt 6ae4e299a13034b7eb8305f8; static, SQL not executed |
| Review time | 2026-11-03 (actual) |
| Clock | 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `04_Prompt.txt` revision 27, saved from the upload `04_Prompt (10).txt` sent with this command; 454 bytes, SHA-256 `b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9`. Same text as the previous /prompt review |
| Assignment | `00_Task_Assigned_Inputs.md`, SHA-256 `1d795090d3476539561f58917410dab7275f800863d3be3084150ecd9a383c37`. All five fields stated: Frederick Stone (Co-founder), Executive, Corporate Ops, Retrieval, long-horizon |
| Injection SQL | `01_Universe_Inject.sql` revision 26 (upload `01_Universe_Inject (15).sql`), 167,306 bytes, SHA-256 `69db98aed17f40cbcbbfad417b7eb21a118dffdbb63b798cf8322ddac226182b` (replaces revision 23, `75b6cb2a…0fee`, which the previous /prompt review graded) |
| Error/async config, dynamic context, reference files | None supplied. The prompt names no attachment; every source is an environment record |
| Eval | `1_Prompt_Eval.md` SHA-256 `e0c364dccda17423ece700d9c4b852a2a04b199a96b42b044d2dc73e73bd6057`; deep_recheck.md `ec7832d95f6f2f93…`; scoring.json `c14873e614cdcda5…` |
| Eval version | task-quality-v1 / prompt-source-checks-v2 |
| Eval release SHA-256 | `a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225` |
| Reviewed prompt SHA-256 | `b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9` |
| Review context SHA-256 | `c76696d7920dc0087ca5376554ef20c92f62a77035ed8df20d2155d98db20317` |
| Prompt record SHA-256 | `2990e8c44cde8032728daaad28a270bba9a213365f2a98031655cdddba98addf` |
| Evidence contract | `stage-evidence-v1`; authority contract `prompt-incorporation-v1` |

Input/authority issues: none. This is a rerun: the prompt text is unchanged and the SQL moved from revision 23 (graded by the previous /prompt review, overwritten at this path; its ledger is carried below) to revision 26. The changes, checked statement by statement against the Eval 0 diff and the SQL text:

1. **Paul Heydon's back-out reaches Fred through the group DM.** The #executives thread reply `7fe55f30…` is gone and Leonard's Sep 19 "angel update" post (`4921f321…`) is a standalone message again. In its place Leonard posts in the group DM `D05S58U4SAK` (members include `EMPLOYEE_0008_SLACK_ID`, Fred), 2025-09-30T17:05Z: "Paul's out, he wrote me this morning that he can't put money in this year after all" (`c5657466…`). Paul's own back-out email (Leonard's mailbox only, 14:55Z) is unchanged.
2. **Karthic's and Arthur's Sep 30 Android emails are removed** (8 rows across four mailboxes and 4 snippet UPDATEs). The base "Bridge Round for [SOURCE_ORG_0001]?" thread is back to its base latest message (Leonard's Sep 22 email with the TestFlight invite and the Play internal-test link).
3. **ZOM-567 gains two comments:** "NCsoft (2 accounts from Anel's team, after the Sep 19 call): TestFlight and Play internal track both added Sep 22." (17:45Z) and "Brightwater (Ilse Marrow): TestFlight and Play internal track both added Sep 26." (18:05Z); the Dentsu comment moves to sequence 4.
4. **Arthur's #zombie-match3d note is now its own thread** (parent `3cddf83c…`, 23:20Z) and covers all four logged firms: "nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them." Leonard replies under it (`301ad67f…`, 23:48Z): "ok thx, ping me when it's live so I can tell Karthic, Ryo-san and the others".

Everything else is byte-identical to revision 23 (155 of 162 statements). The previous check record was carried over under stage-evidence-v1: every SQL citation was re-bound to the revision 26 hash and re-verified as an exact substring; AR1 was re-quoted from the new note; KA1/KA2 (the removed emails) were dropped; ZL3 (NCsoft log), ZL4 (Brightwater log) and AR2 (Leonard's reply) were added; PO1 now points to the group-DM message. The answer changes in two build-access cells only: NCsoft and Brightwater Games Fund move from none to iOS only. a16z, GFR Fund and Homa stay none (Fred's Sep 2025 mail and Slack were searched for "testflight", "internaltest" and "tester"; the only investor tester grants are Karthic's Sep 22 iOS+Android invite and Leonard's Sep 23 offer to Dentsu). SQL comments are read as context only.

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`).
- Reviewed SQL sha256: `69db98aed17f40cbcbbfad417b7eb21a118dffdbb63b798cf8322ddac226182b` (`injection-static-v2`, reviewed 2026-11-03T01:17Z). Eval 0 verdict: PASS / COMPLETE (`0_injection.md`, SHA-256 `042c1a17423813c513f4cafc271f9ff6d337dcc0784d9057ff1356172ab3e11d`; lint 0 FAIL / 0 CHECK / 0 INFO).
- Eval 0 findings on records this prompt depends on: none. Its provisional schema-snapshot advisory (columns not in the unverified snapshot) holds no graded value and stays here.
- Static checks A–C (IDs, structure, chronology, mailbox copies, channel membership, apostrophe quoting, thread counters of the new #zombie-match3d thread, the standalone #executives post and the group-DM post) are REUSED from that report: same SQL hash, universe manifest, schema snapshot and Eval 0 version.

### Dataset Similarity
- Library: 315 tasks (Enterprise Atlas - Commercial: L10 38, L11 3, L12 107, completed 167), age 1.7 h at check time. Check saved for this exact prompt hash.
- **Gate: PASS.** Nearest tier: same scenario (0.762, below the 0.80 duplicate line). No score change. Task IDs are withheld here under portal policy.


| Neighbour | Stage | Persona / competency / skill | Meaning | Wording | Tier | What the two prompts share |
|---|---|---|---|---|---|---|
| 1 | L12 | Frederick Stone / Corporate Ops / Analysis and synthesis | 0.762 | 0.012 | same scenario | Leonard hands Fred the bridge-round investor list; that one updates every firm's status for the Oct 14 board and drafts follow-ups. Yours builds a separate Q4 send list, adds group checklists and follow-up cards on Trello and reports group counts |
| 2 | completed | Frederick Stone / Corporate Ops / Actions | 0.747 | 0.000 | same scenario | Leonard's 2025 investor-list handoff before his LA trip, with a reply naming the firms that said no |

## 2. Checklist

| Item | Status |
|---|---|
| Intake: prompt + five assignment fields + injection answer | NEW, done (upload saved as prompt revision 27, same text; assignment and SQL revision 26 reused from saved inputs) |
| STEP 0.5 injection gate | NEW: CURRENT (SQL `69db98ae…`), Eval 0 PASS reused |
| STEP 0.6 dataset similarity | NEW: PASS (same scenario 0.762) |
| Phase 0.1 references (Eval 1, deep_recheck, reliability rules, release snapshot, acl/roster) | NEW, done; Eval, scoring and release hashes match the previous review. The Evals/Docs PDFs/XLSX were not re-extracted (unchanged; their rules are carried by Eval 1 and scoring.json) |
| Phase 0.2 universe exploration | NEW: SQL diff 23 → 26 (statement by statement); group DM `D05S58U4SAK`, #zombie-match3d and #executives membership re-read from channels.json; the Q4 doc's build-access section; ZOM-567's four comments; base Slack Sep 2025 and Fred's Sep 2025 mailbox searched for "testflight", "internaltest", "tester list", "internal track" (complete scans); base #executives Sep 22 tester thread and the base T-Accelerate and Dentsu threads read. REUSED (dependencies unchanged): every other group, card and calendar fact |
| Phase 1.1–1.5 | REUSED assessment (prompt unchanged); Dynamic Change note updated |
| Phase 2.1 UGT (eighteen readings; A, D, Q updated; record saved) | NEW |
| Phase 2.2–2.9 | REUSED for the unchanged prompt; re-read against the new records and P1–P4 (2.9 N/A: no samples supplied) |
| Phase 3.1–3.2 | NEW for the group-DM relay, the removed emails, the two new ZOM-567 comments and Arthur's new thread; static integrity REUSED from Eval 0 |
| Phase 4 scoring | NEW, done |
| Phase 5 deep recheck P1–P4 | NEW, done (see Deep Recheck) |

## 3. Requirement ledger (`authority_contract: prompt-incorporation-v1`)

The prompt incorporates Leonard's Sep 30 email ("His email lays out what he's after.") and, in its own words, the card ("do what he asked on the Existing Investor Update card in Trello"). The email points to four records: the Q4 send list doc ("the groups and details in the Q4 update send list doc"), the README in Fred's folder ("says how to name it"), the Existing Investor Update card ("Then do what I put on the Existing Investor Update card in Trello.") and the draft deck. The card carries Leonard's two comments (Sep 14 and Sep 29). The doc points to Leonard's #executives note on what counts as signed. That chain is valid incorporation; nothing else adds obligations.

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Work out who from the bridge round gets the Q4 update | Email (2025-09-30 21:05Z): "everyone from the bridge round who should get it, as of tonight, with the groups and details in the Q4 update send list doc". Doc "Q4 investor update - send list" (Leonard, Sep 26): who to look at, the four groups, Passed/"us"/accelerator rules, build access, sheet columns. #executives note (Sep 26): New investor only once the DocuSign Completed notice is in. 2025 investor list (89 grid rows) | Inbox → email → Drive search for the doc, README and list → per firm: Gmail, Calendar, #bridge-pitch / #executives / #zombie-match3d (including thread replies), the group DM, Linear ZOM-567, Contacts | reads via `gmail_*`, `gcal_*`, `slack_*` (`slack_conversations_replies` / `slack_read_thread` for thread replies), `gdrive_*`, `gdocs_*`, `gsheets_*`, `linear_*`, `trello_*`, `contacts_*` | Email, DocuSign notice, investor threads and invites are in Fred's mailbox; the calls are on his calendar; the doc, README, list, deck and Bridge angels sheet are owned by or shared with him; he is a member of #bridge-pitch, #executives, #zombie-match3d and DM D05S58U4SAK; Linear, Trello and Contacts are unscoped | 25 rows (derivation below) |
| Put the send list in "my Q4 2025 investor update folder" | Folder `d_5e8a1c3f9b07d2e64a1b93` "Q4 2025 investor update" (owner Fred). README: name it "Q4 update - send list"; "Google Sheets or Docs only, no uploads" | Drive folder listing | `gsheets_create_spreadsheet` + `gdrive_move_file`, or `gdrive_create_file` with `parentId`; `gsheets_values_update` (or `gdocs_*` for a Doc) | Folder owned by Fred; README shared with him (writer) | A Google Sheet (or Google Doc) "Q4 update - send list" in that folder |
| Do what Leonard asked on the Existing Investor Update card: group checklists | Email: "Then do what I put on the Existing Investor Update card in Trello." Comment 1 (Sep 14): Keep warm checklist, one item per firm that passed after a pitch call or meeting. Comment 2 (Sep 29): "besides the Keep warm one, give every other group on the send list (New investor, In talks, Awaiting reply) its own checklist on this card, one item per firm or angel" | Trello search → card 455 → comments | `trello_create_checklist`, `trello_create_check_item` | Trello unscoped | Four checklists on card 455: New investor (1), In talks (7), Awaiting reply (14), Keep warm (3) |
| … follow-up cards in To Do | Comment 2: "everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named F/up with and the name"; "If one of them already has a card in To Do, comment on that card instead of adding another. Anyone we already have a call or meeting with on Fred's calendar after Sep 30 doesn't need one." Open To Do cards: "Playable Kickoff" (base, no firm) and "F/up with Anel after the engine deep dive" (SQL; Anel Ceman = NCsoft's contact on the list). Fred's calendar after Sep 30: Oct 1 "Harmony Games & Dentsu", Oct 6 review, Oct 8 "Michael Cheung and Leonard Hayes" (Michael Cheung = Makers Fund's contact), Oct 14 board | Trello board lists/cards; Fred's calendar Oct 1 onward; the 2025 list's contact column; Fred's NCsoft thread (Thursday call proposed, only a Calendly link sent) | `trello_create_card` (idList = To Do `640643a3fd8f3ca308d93195`), `trello_add_comment` | Trello unscoped; calendar, list and NCsoft thread visible to Fred | 18 new "F/up with …" cards: Andreessen Horowitz, T-accelerate, GFR Fund, Brightwater Games Fund, Homa, Initial Capital, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures; one comment on "F/up with Anel after the engine deep dive" (NCsoft); none for Dentsu Ventures or Makers Fund |
| Reply on his thread with how many ended up in each group | Email: "reply here with how many firms and angels are in each group" | Same thread | `gmail_reply_to_message` (or `gmail_send_message` with the thread) | Thread in Fred's mailbox | Reply: New investor 1 (angel), In talks 7 (firms), Awaiting reply 14 (firms), Keep warm 3 (firms) |
| Done before the Monday Oct 6 review | Invite "Q4 update send list review", Mon Oct 6 2pm PT, "Fred to bring the send list." | — | — | On Fred's calendar | Timing context, no extra write |
| Excluded by authority | Robert's "send it to everyone on the 2025 investor list" is rejected in the email ("Let's not, only the people the doc says"). Arthur's #executives shortcut isn't incorporated and is covered by the same line. The July "Q3 investor update - send list" doc is for the earlier update | — | — | — | No list-wide send; no shortcut scope |

**Output capability.** Sheet or Doc creation in a folder, cell writes, checklist and check-item creation, card creation in a list, card comments and the Gmail reply are all cataloged (`trello_create_card` takes `idList` and `name`; `trello_add_comment` takes `cardId` and `text`): SUPPORTED by catalog. No run shows their runtime behaviour, and `/prompt` doesn't require one.

**Answer derivation (main session, for downstream reuse).** Groups as of end of day Tue Sep 30 PT under the Q4 doc (REUSED from the previous review except build access and the Paul Heydon source, re-checked NEW against revision 26):

- **New investor (1):** Anton Bernstein, $25,000 (DocuSign Completed notice Sep 26 19:02Z; Leonard's group-DM posts "he can only do 25 this time, not the 40" and "Anton signed the 25 one").
- **In talks (7):** Andreessen Horowitz (none), NCsoft (iOS only), T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (iOS only, off-list), Homa (none, off-list).
- **Awaiting reply (14):** Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Makers Fund stays here: the Oct 8 meeting hasn't happened ("In talks: we've had a call or meeting"; "Awaiting reply: … no call yet").
- **Keep warm (3):** London Venture Partners, Hiro Capital, Sciplay.
- **Paul Heydon stays off.** He said yes for $50K (Sep 19 #executives post; Bridge angels sheet "in"), Leonard nudged him on Sep 29 (Fred cc'd), and on Sep 30 17:05Z Leonard told the group DM Fred is in: "Paul's out, he wrote me this morning that he can't put money in this year after all". The doc: "Passed means they've told us no for this round." Leonard's "neither does me posting it here" ends the sentence "someone only counts as a new investor once the DocuSign Completed notice is in" in his #executives note, so it governs New investor status, not a no. Fred's calendar has no call or meeting with Paul (base Calendar: no "Heydon", "PERSON_9902" or "Paul" event, complete scans; the SQL's 14 calendar rows add none), so Paul "passed without a call or meeting" and stays off.
- **Build access (NEW).** The doc: "Write iOS only, Android only, iOS and Android, or none. … Arthur tracks the tester adds." ZOM-567 logs TestFlight and Play adds for T-Accelerate (Sep 22), NCsoft (Sep 22), Brightwater (Sep 26) and Dentsu (Sep 26). Arthur's #zombie-match3d note at 23:20Z Sep 30 (4:20pm PT, after every log comment, inside the cutoff) says "nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them." So those four are iOS only. a16z, GFR Fund and Homa have no tester record (none); the public store links in the pitch emails don't count.

**Trello derivation.**

- **Checklists on card 455:** New investor [Anton Bernstein]; In talks [the 7 above]; Awaiting reply [the 14 above]; Keep warm [LVP, Hiro Capital, Sciplay]. No checklist exists on the card in base or SQL (badges `checkItems: 0`).
- **Who is exempt from a follow-up card:** Fred's calendar after Sep 30 (complete read of `calendar_id frederick.stone@harmonygames.co`, base plus SQL) holds only: Oct 1 1:30pm PT "1:30pm PT || MEETING || Harmony Games & Dentsu" (`evt_3671b9a924ccba550e51fa`, plus its anonymized twin `evt_eeca6fc7670fe1acd94440`), Oct 6 "Q4 update send list review" (internal), Oct 8 9am PT "Michael Cheung and Leonard Hayes" (`evt_6b2e94d0c17a3f58e9d2b1`), Oct 14 and Jan 14 board meetings (internal). Dentsu: Fred-visible records use "Dentsu" for this investor throughout. Makers Fund: the 2025 list's only "Michael Cheung" is Makers Fund's contact (row 34).
- **Who already has a To Do card:** "Playable Kickoff" (base #447, no firm) and "F/up with Anel after the engine deep dive" (SQL #456). The list gives "Anel Ceman" as NCsoft's contact (row 79). NCsoft's Thursday call was proposed but never booked on Fred's calendar, so NCsoft isn't exempt; it gets a comment on the Anel card instead of a new card.
- **Result:** 18 new cards in To Do (5 In talks + 13 Awaiting reply), named "F/up with [name]"; one comment on card #456; no card for Dentsu Ventures or Makers Fund.

This derivation is evidence for later stages, not a rubric; other wordings of the same values stay valid (card names with "a16z" for Andreessen Horowitz, checklist titles that name the group).

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Frederick Stone (`frederick_stone`, frederick.stone@harmonygames.co, Co-founder, Executive) matches the roster. He is on the investor calls (his calendar), cc'd on the investor threads, a member of #bridge-pitch, #executives and #zombie-match3d, owns the Q4 2025 investor update folder and is a member of the Harmony Games Trello board. A co-founder taking investor-update prep, a tracking checklist and the follow-up cards off the CEO's plate while the CEO travels is plausible in role, authority and access.

| Check | Finding |
|---|---|
| Role plausibility | Yes: co-founder covering investor communications for the CEO |
| Voice match | Yes: short, plain delegation |
| Access plausibility | Yes: every required record is in his mailbox, calendar, channels, DM or shared Drive, or in unscoped Trello |
| Responsibility scope | Yes: prepare the list and the tracking; Leonard writes the update |

**Assigned Competency (Corporate Ops):** PASS (5). Investor relations and investor communications are corporate/board-level operations; the list feeds the Q4 investor update that goes out after the board. It is not a model, budget or forecast (Finance).

**Assigned Task Skill (Retrieval):** PASS (5). The work turns on finding, for about 80 names, the records that decide each one's group, amount and tester access across eight services, then which of them already have a meeting or a To Do card, and writing it down.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y: PASS
- Multi-Source: the doc (Docs), the list (Sheets), Gmail, Calendar, Slack, Linear, Contacts and Trello each decide graded cells or writes.
- Dynamic Change: Anton's $40K is replaced by $25K; Paul's Sep 19 yes and the Bridge angels sheet's "in" are overtaken by Leonard's Sep 30 "Paul's out" in the group DM; ZOM-567's Play adds for four firms are overtaken by Arthur's later Sep 30 #zombie-match3d note ("whatever the Linear log says"); Play Ventures' "no response" is corrected on Sep 25; NCsoft's agreed Thursday call never lands on Fred's calendar.
- Ambiguity: the file name comes from the README, the groups from the doc, and the checklist and follow-up rules from the two card comments, all reached from Leonard's email; the Anel card and the Michael Cheung meeting name people, not firms.
- Data seeding: PASS. The prompt is a 4-sentence trigger; the operating rules live in seeded records.

**Naturalness:** PASS (5). First person, plain, uneven sentences, no formatting, no polished connectives, no deliverable spec. P4 found nothing.

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
| Pre-Solving | PASS: no group, firm, amount, card or count is given |
| Tool Mention | PASS: "Trello", "folder", "thread" are natural product words |

**Diversity:** a new file in a named folder, four Trello checklists, 18 new cards, a comment on an existing card and an email reply, over an ~80-name cohort.

## Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every material fork is settled by the incorporated Q4 doc, README, the two card comments or a later Fred-visible record: a16z In talks (speedrun decision isn't the bridge answer), Sciplay Keep warm (phone no counts), T-accelerate, NCsoft, Brightwater and Dentsu iOS only (Arthur's Sep 30 \#zombie-match3d note names all four and overrides the ZOM-567 log 'whatever the Linear log says'), Anton $25,000 (signed 25), Paul Heydon off (Leonard's Sep 30 group-DM message 'Paul's out' is Paul's no to us; no call with Paul on Fred's calendar, so not Keep warm), Homa included (investment alongside co-dev), Initial Capital Awaiting reply (Sep 9 outreach), e2vc Awaiting reply (call not on Fred's calendar, guess isn't a no). On the card: four group checklists; 18 F/up cards; NCsoft gets a comment on the existing 'F/up with Anel' card (Anel Ceman is NCsoft's contact; the Thursday call was never booked on Fred's calendar); Dentsu Ventures (Oct 1 Dentsu meeting) and Makers Fund (Oct 8 Michael Cheung meeting) need no card and Makers Fund stays Awaiting reply. A Google Doc instead of a Sheet is allowed by the README; Robert's everyone-on-the-list idea is rejected in the email; reply vs reply-all and the F/up card title (firm or angel name vs the contact's name) are authorized variations under the reply instruction and the card comment's 'F/up with and the name'.

Alternative selection: B (a16z Keep warm) remains the strongest group fork: Fred's mailbox holds a real written rejection after an interview call, and it changes a group, two checklists, the card set and two counts. C–H cover the other group traps; I the file type; J Robert's scope idea; K the reply's recipients. L–O cover the Trello traps: NCsoft's unbooked Thursday call (L), the person-named Anel card (M), the Oct 1 Dentsu meeting (N) and the Oct 8 Michael Cheung meeting (O). P covers the card-title wording (firm or angel name vs the contact's name). Q and R cover Paul Heydon: Q keeps him In talks because his own back-out email reaches only Leonard and Leonard's rule says his posts don't count; R makes him Keep warm as a pass after being pitched. D covers the build-access trap: after SQL revision 26 the ZOM-567 log covers four firms (T-Accelerate, NCsoft, Brightwater, Dentsu) and Arthur's later \#zombie-match3d note overrides it for all four.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Leading reading: apply the incorporated Q4 doc groups as of end of day Sep 30 PT to every 2025-list name plus off-list firms with an investment call on Fred's calendar since Sep 3. Anton is a New investor at $25,000 (DocuSign Completed notice and Leonard's 'Anton signed the 25 one'); Paul Heydon stays off: Leonard's Sep 30 message in the group DM with Fred says 'Paul's out, he wrote me this morning that he can't put money in this year after all', which is Paul telling us no for this round, and Fred's calendar has no call or meeting with Paul, so he passed without a call or meeting. a16z is In talks (speedrun interview is a call; the speedrun decision isn't their bridge answer). Sciplay passed by phone after the Sep 15 meeting, so Keep warm. Build access: ZOM-567 logs TestFlight and Play adds for T-Accelerate, NCsoft, Brightwater and Dentsu, but Arthur's later Sep 30 \#zombie-match3d note says the Play tester list was never attached to the internal track, so nobody on it (Karthic, the 3 Dentsu folks, Anel's two at NCsoft, Ilse from Brightwater) has Android yet, 'whatever the Linear log says', and iOS is fine for all of them: those four are iOS only; a16z, GFR Fund and Homa have no tester access (none). Homa and Brightwater are off-list firms in talks. Initial Capital, Sony Mobile and e2vc are Awaiting reply. On the card, both of Leonard's comments apply: a checklist per group, F/up cards in To Do for everyone In talks or Awaiting reply except Dentsu Ventures (the Oct 1 'Harmony Games &amp; Dentsu' meeting is on Fred's calendar) and Makers Fund (the Oct 8 'Michael Cheung and Leonard Hayes' meeting; Michael Cheung is Makers Fund's contact on the list), and a comment on the existing To Do card 'F/up with Anel after the engine deep dive' for NCsoft (Anel Ceman is NCsoft's contact on the list), whose agreed Thursday call was never booked on Fred's calendar. | 25 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz (none), NCsoft (iOS only), T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (iOS only, off-list), Homa (none, off-list). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 18 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Sheet rows as decided; checklists: New investor \[Anton Bernstein\]; In talks \[Andreessen Horowitz, NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Brightwater Games Fund, Homa\]; Awaiting reply \[the 14 firms\]; Keep warm \[London Venture Partners, Hiro Capital, Sciplay\]; F/up cards: Andreessen Horowitz, T-accelerate, GFR Fund, Brightwater Games Fund, Homa, Initial Capital, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures; no card for Dentsu Ventures (Oct 1 meeting on Fred's calendar) or Makers Fund (Oct 8 Michael Cheung meeting); NCsoft handled by the comment on the Anel card; reply: New investor 1 (angel), In talks 7 (7 firms), Awaiting reply 14 firms, Keep warm 3 firms | QD6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "On the list, go only by the Latest Status notes (as of 09/11), which are all from this round, and they count as written: a note that they passed or don''t do bridges is their no, and a note that we reached out is our outreach. The list''s Status and comment columns, answers from earlier rounds and plans to reach out don''t count."; QD7 (Evals/task\_inputs/01\_Universe\_Inject.sql): "New investor: signed a SAFE this round (see my note in \#executives on what counts as signed). Put the amount on their row."; QD8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "In talks: we''ve had a call or meeting with them this round (on Fred''s calendar) and they haven''t passed. Angels who''ve said yes but haven''t signed go here too, with the amount they said yes to."; QD9 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Awaiting reply: we reached out this round, no call yet and no no, even if they''ve written back."; QD10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Keep warm: they passed after we pitched them on a call or meeting this round."; QD14 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The interview counts as a call with that firm, but the program''s decision and the feedback that comes with it aren''t their answer on the bridge; that has to come on our bridge thread with them or in \#bridge-pitch."; DM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anton signed the 25 one"; RB1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round"; QD15 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Write iOS only, Android only, iOS and Android, or none. The public store pages don''t count. Arthur tracks the tester adds. Leave it blank for angels."; QD4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "if we pitched them the bridge or an investment alongside a co-dev deal, they count even when co-dev or publishing was on the table too. Service or work-for-hire deals, banks (our SVB catch-ups), RFPs, publishing-only talks and calls with other engine companies don''t."; HOMA1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "we are currently seeking extension funding on our seed round"; IC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "pinged Initial Capital on LinkedIn about the bridge, they wrote back that they won''t lead but might write a small check"; TR3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "besides the Keep warm one, give every other group on the send list (New investor, In talks, Awaiting reply) its own checklist on this card, one item per firm or angel, so Arthur can tick them off as they go out."; TR4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Then everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named F/up with and the name, so we chase them the week after."; TR5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "If one of them already has a card in To Do, comment on that card instead of adding another."; TR6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anyone we already have a call or meeting with on Fred''s calendar after Sep 30 doesn''t need one."; TC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'68c99e98737744bd966aed24', 'F/up with Anel after the engine deep dive', '640643a3fd8f3ca308d9318e', '640643a3fd8f3ca308d93195'"; IL79 (Evals/task\_inputs/01\_Universe\_Inject.sql): ""NCsoft", "", "", "", "Anel Ceman""; DEN1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "1:30pm PT \|\| MEETING \|\| Harmony Games &amp; Dentsu""; MC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'evt\_6b2e94d0c17a3f58e9d2b1', 'frederick.stone@harmonygames.co', 'Michael Cheung and Leonard Hayes', NULL, NULL, '2025-10-08T16:00:00Z'"; IL34 (Evals/task\_inputs/01\_Universe\_Inject.sql): ""Makers Fund", "\[REDACTED\]", "Seed/Series A", "Yes", "Michael Cheung""; QD12 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed means they''ve told us no for this round. A no to our pitch that they sent Griffin or an advisor rather than us counts too. An advisor''s own read on whether a firm invests isn''t the firm''s answer."; QD11 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Everyone else stays off: they passed without a call or meeting, or nothing from us since Sep 3."; PO1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul''s out, he wrote me this morning that he can''t put money in this year after all"; AR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "found a problem with investor android access: the investor tester list I made in the Play console never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel''s two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them."; ZL3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "NCsoft (2 accounts from Anel''s team, after the Sep 19 call): TestFlight and Play internal track both added Sep 22."; ZL4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Brightwater (Ilse Marrow): TestFlight and Play internal track both added Sep 26." |
| B | a16z's Sep 30 speedrun feedback ('decision not to include') is their no after the Sep 18 interview call, so a16z is Keep warm and gets a checklist item. | As A, except Andreessen Horowitz moves from In talks to Keep warm | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 17 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Checklists: In talks 6 (no a16z), Keep warm 4 (adds Andreessen Horowitz); 17 F/up cards (no a16z card); reply: In talks 6 (6 firms), Keep warm 4 | A16Z1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "decision not to include"; GC1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "\[USERNAME\_1453\] speedrun Interview 9/18/25"; QD10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Keep warm: they passed after we pitched them on a call or meeting this round." |
| C | Robert's note is a secondhand phone report, not Sciplay's own written no, so Sciplay stays In talks after the Sep 15 meeting and gets no checklist item. | As A, except Sciplay is In talks (build access none) instead of Keep warm | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 19 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Checklists: In talks 8 (adds Sciplay), Keep warm 2 (LVP, Hiro Capital); 19 F/up cards (adds Sciplay); reply: In talks 8 (8 firms), Keep warm 2 | RB1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round"; GC5 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "\[USERNAME\_22751\] &lt;&gt; \[SOURCE\_ORG\_0001\]"" |
| D | Arthur's ZOM-567 log records TestFlight and Play internal track adds for T-Accelerate (Sep 22), NCsoft (Sep 22), Brightwater (Sep 26) and Dentsu (Sep 26), and the doc says Arthur tracks the tester adds, so all four are iOS and Android. | As A, except T-accelerate, NCsoft, Brightwater Games Fund and Dentsu Ventures build access 'iOS and Android' | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 18 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Four build-access cells differ; checklists, cards, comment and counts as A | ZL1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "T-Accelerate (Karthic): TestFlight and Play internal track both added Sep 22."; ZL3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "NCsoft (2 accounts from Anel''s team, after the Sep 19 call): TestFlight and Play internal track both added Sep 22."; ZL4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Brightwater (Ilse Marrow): TestFlight and Play internal track both added Sep 26."; ZL2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "TestFlight added Sep 26, Play internal track added Sep 26 (investor tester list)."; QD15 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Write iOS only, Android only, iOS and Android, or none. The public store pages don''t count. Arthur tracks the tester adds. Leave it blank for angels." |
| E | Anton's amount is the $40K Leonard posted on Sep 19 and the Bridge angels sheet shows; the DocuSign notice makes him a New investor at $40,000. | As A, except Anton Bernstein's amount is $40,000 | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 18 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Anton's amount cell $40,000; checklists, cards, comment and counts as A | EX2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE."; ANG1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "\["Anton Bernstein", 40000, "in", "docs via docusign next week"\]"; DS1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "All signers completed Complete with docusign: Harmony Games SAFE - Anton Bernstein.pdf" |
| F | Homa is a co-dev/publishing conversation, not investment talks, so it is left off. | As A, except Homa stays off (24 rows) | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 17 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | 24 rows; In talks checklist 6 (no Homa); 17 F/up cards (no Homa card); reply: In talks 6 (6 firms) | BP5 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C096HFA5Z8W/2025-09.json): "I think we should focus Homa on the co-dev investment path."; HOMA2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1843552279434086285.json): "still interested in exploring co-dev with you" |
| G | Initial Capital's Latest Status note records their stance, not our outreach, so with no 'reached out' note they stay off. | As A, except Initial Capital stays off (24 rows) | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 17 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | 24 rows; Awaiting reply checklist 13 (no Initial Capital); 17 F/up cards; reply: Awaiting reply 13 | GS2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gsheets/data.json): "They won't lead - would potentially write a small check"; QD6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "On the list, go only by the Latest Status notes (as of 09/11), which are all from this round, and they count as written: a note that they passed or don''t do bridges is their no, and a note that we reached out is our outreach. The list''s Status and comment columns, answers from earlier rounds and plans to reach out don''t count." |
| H | The Turkish VC call on Sep 29 and Leonard's 'so this is gonna be a no' make e2vc a pass after a call (Keep warm), or at least not Awaiting reply. | As A, except e2vc moves from Awaiting reply to Keep warm | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 17 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Awaiting reply checklist 13, Keep warm 4 (adds e2vc); 17 F/up cards (no e2vc card); reply: Awaiting reply 13, Keep warm 4 | EXB1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-09.json): "waiting for the Turkish VC to show up"; EXB2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-09.json): "so this is gonna be a no"; BP7 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C096HFA5Z8W/2025-09.json): "e2VC (Turkish founder focused, meeting is being set up)" |
| I | The README allows a Google Doc, and Leonard's email calls it the 'send list doc', so the list is a Google Doc with a table rather than a Google Sheet. | 25 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz (none), NCsoft (iOS only), T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (iOS only, off-list), Homa (none, off-list). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Doc named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 18 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Sheet rows as decided; checklists: New investor \[Anton Bernstein\]; In talks \[Andreessen Horowitz, NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Brightwater Games Fund, Homa\]; Awaiting reply \[the 14 firms\]; Keep warm \[London Venture Partners, Hiro Capital, Sciplay\]; F/up cards: Andreessen Horowitz, T-accelerate, GFR Fund, Brightwater Games Fund, Homa, Initial Capital, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures; no card for Dentsu Ventures (Oct 1 meeting on Fred's calendar) or Makers Fund (Oct 8 Michael Cheung meeting); NCsoft handled by the comment on the Anel card; reply: New investor 1 (angel), In talks 7 (7 firms), Awaiting reply 14 firms, Keep warm 3 firms (in a Google Doc table) | RD2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Google Sheets or Docs only, no uploads, so I can link them from the draft."; EM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "What I need from you is everyone from the bridge round who should get it, as of tonight, with the groups and details in the Q4 update send list doc so I know which paragraph each one gets." |
| J | Follow Robert's suggestion and send to everyone on the 2025 investor list, so every list name gets a row. | Every 2025-list name (77 distinct) plus the off-list firms gets a row | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 50+ 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | 77+ rows; much larger checklists and card set; different group counts | RO1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "could we just send it to everyone on the 2025 investor list?" |
| K | Leonard's email is cc'd to Robert and Arthur, so the counts reply goes reply-all to Leonard, Robert and Arthur rather than to Leonard alone (or the reverse). | 25 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz (none), NCsoft (iOS only), T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (iOS only, off-list), Homa (none, off-list). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 18 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply-all on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox; reply recipients Leonard plus cc Robert and Arthur | Sheet rows as decided; checklists: New investor \[Anton Bernstein\]; In talks \[Andreessen Horowitz, NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Brightwater Games Fund, Homa\]; Awaiting reply \[the 14 firms\]; Keep warm \[London Venture Partners, Hiro Capital, Sciplay\]; F/up cards: Andreessen Horowitz, T-accelerate, GFR Fund, Brightwater Games Fund, Homa, Initial Capital, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures; no card for Dentsu Ventures (Oct 1 meeting on Fred's calendar) or Makers Fund (Oct 8 Michael Cheung meeting); NCsoft handled by the comment on the Anel card; reply: New investor 1 (angel), In talks 7 (7 firms), Awaiting reply 14 firms, Keep warm 3 firms | EM10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'\["Robert &lt;robert@harmonygames.co&gt;", "Arthur Blake &lt;arthur.blake@harmonygames.co&gt;"\]'"; EM5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Once it''s done reply here with how many firms and angels are in each group." |
| L | Anel agreed to a Thursday call ('Thu would work best for me') and Leonard sent his Calendly, so NCsoft already has a call coming and needs neither a new F/up card nor a comment on the Anel card. | 25 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz (none), NCsoft (iOS only), T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (iOS only, off-list), Homa (none, off-list). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 18 'F/up with &lt;name&gt;' cards in the board's To Do list; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread (no comment on the Anel card) | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Sheet rows as decided; checklists: New investor \[Anton Bernstein\]; In talks \[Andreessen Horowitz, NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Brightwater Games Fund, Homa\]; Awaiting reply \[the 14 firms\]; Keep warm \[London Venture Partners, Hiro Capital, Sciplay\]; 18 F/up cards as A; no comment for NCsoft; reply counts as A | NC1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1832208184829815962.json): "Thu would work best for me, can you send me your calendly and will book a slot"; NC2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1832208184829815962.json): "Here you go: https://calendly.com/leonard.hayes/45mins"; TR6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anyone we already have a call or meeting with on Fred''s calendar after Sep 30 doesn''t need one." |
| M | 'F/up with Anel after the engine deep dive' is Leonard's engine-deal reminder, not a bridge follow-up for NCsoft, so NCsoft gets its own new 'F/up with NCsoft' card and the Anel card is left alone. | 25 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz (none), NCsoft (iOS only), T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (iOS only, off-list), Homa (none, off-list). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 19 'F/up with &lt;name&gt;' cards in the board's To Do list; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread (no comment on the Anel card) | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Sheet rows as decided; checklists: New investor \[Anton Bernstein\]; In talks \[Andreessen Horowitz, NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Brightwater Games Fund, Homa\]; Awaiting reply \[the 14 firms\]; Keep warm \[London Venture Partners, Hiro Capital, Sciplay\]; 19 F/up cards (adds F/up with NCsoft); no comment; reply counts as A | TC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'68c99e98737744bd966aed24', 'F/up with Anel after the engine deep dive', '640643a3fd8f3ca308d9318e', '640643a3fd8f3ca308d93195'"; TR4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Then everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named F/up with and the name, so we chase them the week after." |
| N | The Oct 1 'Harmony Games &amp; Dentsu' meeting is not shown to be with Dentsu Ventures, the firm on the send list, so Dentsu Ventures still gets an F/up card. | 25 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz (none), NCsoft (iOS only), T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (iOS only, off-list), Homa (none, off-list). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 19 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Sheet rows as decided; checklists: New investor \[Anton Bernstein\]; In talks \[Andreessen Horowitz, NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Brightwater Games Fund, Homa\]; Awaiting reply \[the 14 firms\]; Keep warm \[London Venture Partners, Hiro Capital, Sciplay\]; 19 F/up cards (adds F/up with Dentsu Ventures); comment and reply counts as A | DEN1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "1:30pm PT \|\| MEETING \|\| Harmony Games &amp; Dentsu""; TR4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Then everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named F/up with and the name, so we chase them the week after." |
| O | The Oct 8 'Michael Cheung and Leonard Hayes' meeting makes Makers Fund In talks (a meeting is on Fred's calendar), or, if Michael Cheung isn't tied to Makers Fund, Makers Fund still gets an F/up card. | As A, except Makers Fund moves from Awaiting reply to In talks (O1), or stays Awaiting reply with an F/up card (O2) | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 19 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread (O2); O1 keeps 18 cards | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | O1: In talks checklist 8, Awaiting reply 13, reply In talks 8 / Awaiting reply 13; O2: 19 F/up cards (adds F/up with Makers Fund) | MC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'evt\_6b2e94d0c17a3f58e9d2b1', 'frederick.stone@harmonygames.co', 'Michael Cheung and Leonard Hayes', NULL, NULL, '2025-10-08T16:00:00Z'"; QD8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "In talks: we''ve had a call or meeting with them this round (on Fred''s calendar) and they haven''t passed. Angels who''ve said yes but haven''t signed go here too, with the amount they said yes to."; TR4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Then everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named F/up with and the name, so we chase them the week after." |
| P | 'named F/up with and the name' means the contact person's name, as on Leonard's own To Do card 'F/up with Anel after the engine deep dive' and the board's older 'F/up with Martin', so a card reads 'F/up with Ilse' for Brightwater Games Fund (contact Ilse Marrow) wherever the records give a contact. | 25 rows. New investor: Anton Bernstein ($25,000). In talks: Andreessen Horowitz (none), NCsoft (iOS only), T-accelerate (iOS only), Dentsu Ventures (iOS only), GFR Fund (none), Brightwater Games Fund (iOS only, off-list), Homa (none, off-list). Awaiting reply (14): Initial Capital, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures. Keep warm: London Venture Partners, Hiro Capital, Sciplay. Everyone else stays off. | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 18 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | Sheet rows as decided; checklists: New investor \[Anton Bernstein\]; In talks \[Andreessen Horowitz, NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Brightwater Games Fund, Homa\]; Awaiting reply \[the 14 firms\]; Keep warm \[London Venture Partners, Hiro Capital, Sciplay\]; F/up cards (titled with each entry's contact name where one is known, otherwise the firm or angel): Andreessen Horowitz, T-accelerate, GFR Fund, Brightwater Games Fund, Homa, Initial Capital, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital, BITKRAFT Ventures; no card for Dentsu Ventures (Oct 1 meeting on Fred's calendar) or Makers Fund (Oct 8 Michael Cheung meeting); NCsoft handled by the comment on the Anel card; reply: New investor 1 (angel), In talks 7 (7 firms), Awaiting reply 14 firms, Keep warm 3 firms | TR4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Then everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named F/up with and the name, so we chase them the week after."; TC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'68c99e98737744bd966aed24', 'F/up with Anel after the engine deep dive', '640643a3fd8f3ca308d9318e', '640643a3fd8f3ca308d93195'"; TB2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/trello/data.json): ""name": "F/up with Martin"" |
| Q | Paul Heydon stays In talks at $50,000 with a follow-up card: Paul's own back-out email is only in Leonard's mailbox, so the only no Fred can see is Leonard's relay in their group DM, which is Leonard saying it rather than Paul; Leonard's rule says 'neither does me posting it here', the Bridge angels sheet still has Paul 'in' at 50000, and Leonard's Sep 29 nudge in Fred's mailbox has no reply from Paul. | As A, except Paul Heydon is In talks at $50,000 (26 rows) | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel; create 19 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | 26 rows; In talks checklist 8 (adds Paul Heydon); 19 F/up cards (adds F/up with Paul Heydon); reply: New investor 1 (angel), In talks 8 (7 firms, 1 angel), Awaiting reply 14 firms, Keep warm 3 firms | EX1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "someone only counts as a new investor once the DocuSign Completed notice is in. them telling us they''re in doesn''t count, and neither does me posting it here"; QD8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "In talks: we''ve had a call or meeting with them this round (on Fred''s calendar) and they haven''t passed. Angels who''ve said yes but haven''t signed go here too, with the amount they said yes to."; PH1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Gentle nudge on the SAFE in DocuSign, it''s still sitting with you."; EX2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE." |
| R | Paul Heydon passed after Leonard pitched him (he had said yes for $50K), so he is Keep warm: a row in the sheet and an item on the Keep warm checklist, no follow-up card. | As A, except Paul Heydon is Keep warm (26 rows) | Create one Google Sheet (or Google Doc) named 'Q4 update - send list'; add four checklists to the Existing Investor Update card (New investor, In talks, Awaiting reply, Keep warm), one check item per firm or angel, with a fourth Keep warm item for Paul Heydon; create 18 'F/up with &lt;name&gt;' cards in the board's To Do list; comment on the To Do card 'F/up with Anel after the engine deep dive' (NCsoft) instead of adding one; reply to Leonard on his Sep 30 'Q4 investor update - send list' thread | Fred's Drive folder 'Q4 2025 investor update' (d\_5e8a1c3f9b07d2e64a1b93); Trello card 455 'Existing Investor Update' (checklists); the Harmony Games board's To Do list (new F/up cards) and the To Do card 'F/up with Anel after the engine deep dive' (\#456, comment); Leonard's Sep 30 thread in Fred's mailbox | 26 rows; Keep warm checklist 4 (adds Paul Heydon); 18 F/up cards as A; reply: New investor 1 (angel), In talks 7 (7 firms), Awaiting reply 14 firms, Keep warm 4 (3 firms, 1 angel) | PO1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul''s out, he wrote me this morning that he can''t put money in this year after all"; QD10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Keep warm: they passed after we pitched them on a call or meeting this round."; EX2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE." |

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
| writes | DIFFERENT | 17 vs 18 F/up cards (no a16z card). |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Checklist items and two counts; a16z group cell; no a16z F/up card. |

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
| writes | DIFFERENT | 19 vs 18 F/up cards (adds Sciplay). |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Checklist items, counts, Sciplay group cell. |

Authority chain: P → EM2 → QD12

Resolution relevance challenge: QD12 is the doc's Passed definition; RB1 is a Fred-visible record of Sciplay's no for this round.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: QD12 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed means they''ve told us no for this round. A no to our pitch that they sent Griffin or an advisor rather than us counts too. An advisor''s own read on whether a firm invests isn''t the firm''s answer."; RB1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Sciplay''s out too. D called me this morning, they''re passing on this round"

Compared alternative: D
Resolution: EXCLUDED. Newer source, same authority, explicit override: the doc says 'Arthur tracks the tester adds'. The four ZOM-567 comments (17:25Z, 17:45Z, 18:05Z and 18:40Z Sep 30) log TestFlight and Play adds for T-Accelerate, NCsoft, Brightwater and Dentsu. Arthur's own \#zombie-match3d note at 23:20Z Sep 30 (4:20pm PT, inside the end-of-day Sep 30 window and after every log comment) says the Play tester list was never attached to the internal track, 'so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them.' It names all four firms and expressly sets the log aside; Leonard's reply under it ('ping me when it's live so I can tell Karthic, Ryo-san and the others') accepts it, and the fix is planned for Oct 1, after the cutoff. So all four are iOS only.
Resolution evidence: QD15 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Write iOS only, Android only, iOS and Android, or none. The public store pages don''t count. Arthur tracks the tester adds. Leave it blank for angels."; AR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "found a problem with investor android access: the investor tester list I made in the Play console never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel''s two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them."; QD5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Groups, as of end of day Tue Sep 30 (Pacific)"; AR2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "ok thx, ping me when it''s live so I can tell Karthic, Ryo-san and the others"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | iOS only vs iOS and Android for four firms. |
| writes | SAME | Same writes. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Four build-access cells. |

Authority chain: P → EM2 → QD15

Resolution relevance challenge: Not a strawman: the ZOM-567 log is the tester tracker the doc points to and is dated Sep 30. AR1 is the same named authority's later statement the same day, it names each of the four logged firms (Karthic = T-Accelerate, the 3 Dentsu folks, Anel's two at NCsoft, Ilse from Brightwater) and says 'whatever the Linear log says', so it is the same scope and a newer source.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: AR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "found a problem with investor android access: the investor tester list I made in the Play console never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel''s two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them."; ZL3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "NCsoft (2 accounts from Anel''s team, after the Sep 19 call): TestFlight and Play internal track both added Sep 22."; ZL4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Brightwater (Ilse Marrow): TestFlight and Play internal track both added Sep 26."

Compared alternative: E
Resolution: EXCLUDED. Newer source: Leonard's Sep 24 DM to Fred says Anton can only do 25, not the 40, and that the docusign is voided and a new SAFE at 25 sent; the DocuSign Completed notice (Sep 26 19:02Z) is followed by 'Anton signed the 25 one' (19:15Z). The \#executives rule makes the Completed notice the test of a New investor.
Resolution evidence: DM1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "he can only do 25 this time, not the 40. voiding his docusign and sending a new SAFE at 25 tonight"; DM2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anton signed the 25 one"; DS1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "All signers completed Complete with docusign: Harmony Games SAFE - Anton Bernstein.pdf"; EX1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "someone only counts as a new investor once the DocuSign Completed notice is in. them telling us they''re in doesn''t count, and neither does me posting it here"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Anton $25,000 vs $40,000. |
| writes | SAME | Same writes. |
| destinations | SAME | Same folder, card, To Do list and thread. |
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
| writes | DIFFERENT | 17 vs 18 F/up cards (no Homa card). |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Row set, In talks checklist and count. |

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
| writes | DIFFERENT | 17 vs 18 F/up cards (no Initial Capital card). |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Row present vs absent; Awaiting reply checklist and count. |

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
| writes | DIFFERENT | 17 vs 18 F/up cards (no e2vc card). |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Checklist items and counts. |

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
| destinations | SAME | Same folder, card, To Do list and thread. |
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
| writes | DIFFERENT | Far more checklist items and F/up cards. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Row set, checklists, cards and counts. |

Authority chain: P → EM7

Resolution relevance challenge: EM7 answers Robert's exact proposal.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: EM7 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Robert asked about just sending it to everyone on the 2025 list. Let''s not, only the people the doc says."

Compared alternative: K
Resolution: AUTHORIZED_VARIATION. The prompt asks only to 'reply on his thread', and Leonard's email says 'reply here'. A reply to Leonard alone and a reply-all that also reaches the cc'd co-founders (Robert, Arthur) are both replies on that thread with the same counts. No record limits or requires the cc list, so the rubric must accept either.
Resolution evidence: P (Evals/task\_inputs/04\_Prompt.txt): "reply on his thread with how many ended up in each group"; EM5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Once it''s done reply here with how many firms and angels are in each group."; EM10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'\["Robert &lt;robert@harmonygames.co&gt;", "Arthur Blake &lt;arthur.blake@harmonygames.co&gt;"\]'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same rows and groups. |
| writes | SAME | One reply on the same thread either way. |
| destinations | DIFFERENT | Recipients: Leonard only vs Leonard plus cc Robert and Arthur. |
| contents | SAME | Same counts. |

Authority chain: P → EM5
Authority kind: OBJECTIVE_ACCEPTANCE_BOUNDARY
Acceptance boundary: A reply in Leonard's Sep 30 'Q4 investor update - send list' thread that reaches Leonard and gives the count for each group.
Acceptance for A: A reply to Leonard on the thread with the counts meets the boundary.
Acceptance for K: A reply-all to Leonard, Robert and Arthur on the same thread with the same counts meets the same boundary.

Resolution relevance challenge: The prompt sentence and EM5 define the requested write as a reply on Leonard's Sep 30 thread; EM10 shows the cc'd recipients are internal co-founders already on that thread.
Delegation challenge: EXPLICIT_AUTHORITY. The requester (Fred, in the prompt) and Leonard (EM5) set the acceptance boundary as a reply on that thread; neither names the recipient list, and both reply forms meet it.
Challenge evidence: P (Evals/task\_inputs/04\_Prompt.txt): "reply on his thread with how many ended up in each group"; EM5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Once it''s done reply here with how many firms and angels are in each group."

Compared alternative: L
Resolution: EXCLUDED. Authority and scope: Leonard's card comment exempts only 'Anyone we already have a call or meeting with on Fred's calendar after Sep 30'. Fred's calendar after Sep 30 holds only the Oct 1 Dentsu meeting, the Oct 6 send list review, the Oct 8 Michael Cheung meeting and the Oct 14 board meeting (complete read of calendar\_id frederick.stone@harmonygames.co); nothing with NCsoft. Anel's 'Thu would work best' was answered only with a Calendly link, and no booking exists before the clock.
Resolution evidence: TR6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anyone we already have a call or meeting with on Fred''s calendar after Sep 30 doesn''t need one."; NC1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1832208184829815962.json): "Thu would work best for me, can you send me your calendly and will book a slot"; NC2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1832208184829815962.json): "Here you go: https://calendly.com/leonard.hayes/45mins"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same groups and rows. |
| writes | DIFFERENT | Comment on the Anel card vs none. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Comment present vs absent. |

Authority chain: P → EM4 → TR6

Resolution relevance challenge: TR6 makes the calendar the test; NC1/NC2 show the Thursday call was proposed but never booked.
Delegation challenge: NOT_CLAIMED. One outcome per firm; no choice is delegated.
Challenge evidence: TR6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anyone we already have a call or meeting with on Fred''s calendar after Sep 30 doesn''t need one."

Compared alternative: M
Resolution: EXCLUDED. Scope and source identity: the comment says 'If one of them already has a card in To Do, comment on that card instead of adding another', with no limit on what the card is about. The open To Do card 'F/up with Anel after the engine deep dive' names Anel, and the 2025 investor list (shared with Fred) gives Anel Ceman as NCsoft's contact; NCsoft is In talks. The only other open To Do card, 'Playable Kickoff', names no firm or angel. So NCsoft already has a card and gets a comment, not a second card.
Resolution evidence: TR5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "If one of them already has a card in To Do, comment on that card instead of adding another."; TC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'68c99e98737744bd966aed24', 'F/up with Anel after the engine deep dive', '640643a3fd8f3ca308d9318e', '640643a3fd8f3ca308d93195'"; IL79 (Evals/task\_inputs/01\_Universe\_Inject.sql): ""NCsoft", "", "", "", "Anel Ceman""; TB1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/trello/data.json): ""name": "Playable Kickoff""

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same groups. |
| writes | DIFFERENT | New 'F/up with NCsoft' card vs comment on the Anel card. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | 19 vs 18 cards; comment absent vs present. |

Authority chain: P → EM4 → TR5

Resolution relevance challenge: TR5 governs exactly the case of a firm that already has a To Do card; IL79 ties the card's Anel to NCsoft.
Delegation challenge: NOT_CLAIMED. One outcome per firm; no choice is delegated.
Challenge evidence: TR5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "If one of them already has a card in To Do, comment on that card instead of adding another."; IL79 (Evals/task\_inputs/01\_Universe\_Inject.sql): ""NCsoft", "", "", "", "Anel Ceman""

Compared alternative: N
Resolution: EXCLUDED. Source identity: Fred-visible records use 'Dentsu' for this investor throughout. \#bridge-pitch 'we are meeting with Dentsu in 25 mins' sits 25 minutes before the Sep 23 call that makes Dentsu Ventures In talks; \#executives 'come to LA on Oct 1st for the Dentsu in person meeting'; Leonard's email 'the Griffin AGM and the Dentsu meeting'; Arthur's 'the 3 Dentsu folks' on the investor tester list. No record shows a separate Dentsu relationship. The Oct 1 1:30pm PT meeting is on Fred's calendar after Sep 30, so Dentsu Ventures needs no card.
Resolution evidence: TR6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anyone we already have a call or meeting with on Fred''s calendar after Sep 30 doesn''t need one."; DEN1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "1:30pm PT \|\| MEETING \|\| Harmony Games &amp; Dentsu""; DEN2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-09.json): "I think you should come to LA on Oct 1st for the Dentsu in person meeting"; DEN3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C096HFA5Z8W/2025-09.json): "we are meeting with Dentsu in 25 mins"; EM11 (Evals/task\_inputs/01\_Universe\_Inject.sql): "flying to LA tomorrow morning for the Griffin AGM and the Dentsu meeting"; AR1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "found a problem with investor android access: the investor tester list I made in the Play console never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel''s two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same groups. |
| writes | DIFFERENT | 19 vs 18 F/up cards. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Adds 'F/up with Dentsu Ventures'. |

Authority chain: P → EM4 → TR6

Resolution relevance challenge: DEN2 and EM11 name the Oct 1 Dentsu meeting in the investor context; DEN3 shows the same label for the Dentsu Ventures pitch call.
Delegation challenge: NOT_CLAIMED. One outcome per firm; no choice is delegated.
Challenge evidence: DEN2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-09.json): "I think you should come to LA on Oct 1st for the Dentsu in person meeting"; DEN3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C096HFA5Z8W/2025-09.json): "we are meeting with Dentsu in 25 mins"

Compared alternative: O
Resolution: EXCLUDED. O1, authority and timing: In talks needs a call or meeting 'we've had', and the groups are 'as of end of day Tue Sep 30 (Pacific)'; the Oct 8 meeting hasn't happened, so Makers Fund stays Awaiting reply ('no call yet'). O2, source identity: the 2025 investor list gives Michael Cheung as Makers Fund's contact, and no other Michael Cheung appears in Fred-visible records; the Oct 8 meeting is on Fred's calendar after Sep 30, so the comment exempts Makers Fund from a card.
Resolution evidence: QD8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "In talks: we''ve had a call or meeting with them this round (on Fred''s calendar) and they haven''t passed. Angels who''ve said yes but haven''t signed go here too, with the amount they said yes to."; QD5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Groups, as of end of day Tue Sep 30 (Pacific)"; QD9 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Awaiting reply: we reached out this round, no call yet and no no, even if they''ve written back."; IL34 (Evals/task\_inputs/01\_Universe\_Inject.sql): ""Makers Fund", "\[REDACTED\]", "Seed/Series A", "Yes", "Michael Cheung""; MC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'evt\_6b2e94d0c17a3f58e9d2b1', 'frederick.stone@harmonygames.co', 'Michael Cheung and Leonard Hayes', NULL, NULL, '2025-10-08T16:00:00Z'"; TR6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anyone we already have a call or meeting with on Fred''s calendar after Sep 30 doesn''t need one."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | O1 moves Makers Fund to In talks. |
| writes | DIFFERENT | O2 adds an F/up card. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Checklists, counts or card set differ. |

Authority chain: P → EM2 → QD8

Resolution relevance challenge: QD8/QD5 fix the group test in the past tense and to Sep 30; IL34 is the only Michael Cheung record and ties him to Makers Fund.
Delegation challenge: NOT_CLAIMED. One outcome per firm; no choice is delegated.
Challenge evidence: QD8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "In talks: we''ve had a call or meeting with them this round (on Fred''s calendar) and they haven''t passed. Angels who''ve said yes but haven''t signed go here too, with the amount they said yes to."; IL34 (Evals/task\_inputs/01\_Universe\_Inject.sql): ""Makers Fund", "\[REDACTED\]", "Seed/Series A", "Yes", "Michael Cheung""

Compared alternative: P
Resolution: AUTHORIZED_VARIATION. Leonard's Sep 29 comment fixes the card's list (To Do on this board), one card per In talks or Awaiting reply entry, the exemptions and the title format 'F/up with and the name', but not whether 'the name' is the firm or angel on the send list or its contact. His own To Do card 'F/up with Anel after the engine deep dive' and the board's older 'F/up with Martin' use a person's name; the comment's antecedent ('everyone In talks or Awaiting reply') is the firm or angel. No record settles it. Both titles name the same chase target, so the same 18 cards in the same list meet the comment; the rubric must accept a title with the firm or angel's name or with its contact's name.
Resolution evidence: TR4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Then everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named F/up with and the name, so we chase them the week after."; TC1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "'68c99e98737744bd966aed24', 'F/up with Anel after the engine deep dive', '640643a3fd8f3ca308d9318e', '640643a3fd8f3ca308d93195'"; TB2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/trello/data.json): ""name": "F/up with Martin""

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same groups and exemptions. |
| writes | SAME | Same 18 cards in To Do, same comment. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | Card titles: 'F/up with &lt;firm or angel&gt;' vs 'F/up with &lt;contact&gt;'. |

Authority chain: P → EM4 → TR4
Authority kind: OBJECTIVE_ACCEPTANCE_BOUNDARY
Acceptance boundary: One card per non-exempt In talks or Awaiting reply entry, in the Harmony Games board's To Do list, titled 'F/up with ' followed by the firm or angel's name or the name of its contact.
Acceptance for A: 'F/up with GFR Fund', 'F/up with Homa' and the like meet the boundary.
Acceptance for P: 'F/up with' plus the entry's contact name, such as 'F/up with Ilse' for Brightwater Games Fund, meets the same boundary.

Resolution relevance challenge: TR4 is the only rule for the title and sets its format; TC1 and TB2 are the board's own examples of the same format with a person's name.
Delegation challenge: EXPLICIT_AUTHORITY. Leonard's comment, incorporated through the prompt and his email, sets the acceptance boundary as 'F/up with' plus the name; it does not say which name, and both forms meet it.
Challenge evidence: TR4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Then everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named F/up with and the name, so we chase them the week after."

Compared alternative: Q
Resolution: EXCLUDED. Authority, scope and newer source. The doc defines a pass as 'they've told us no for this round' and counts anyone who reached out on our behalf as 'us'. Leonard's Sep 30 17:05Z message in the group DM D05S58U4SAK (Fred is a member) reports Paul's own written no to Leonard ('he wrote me this morning that he can't put money in this year after all'), so Paul told us no; it is not an advisor's read. Leonard's 'neither does me posting it here' ends the sentence 'someone only counts as a new investor once the DocuSign Completed notice is in' and refers to his \#executives posts, so it governs New investor status, not a no, and the relay is not even an \#executives post. The relay is newer than the Sep 19 'in for $50K' post, the Bridge angels sheet and the Sep 29 nudge. The same relay pattern decides Sciplay (Robert's 'D called me this morning, they're passing'). With no call or meeting with Paul on Fred's calendar (base Calendar has no Heydon/PERSON\_9902 event and the SQL adds none), he passed without a call or meeting, so he stays off.
Resolution evidence: QD12 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Passed means they''ve told us no for this round. A no to our pitch that they sent Griffin or an advisor rather than us counts too. An advisor''s own read on whether a firm invests isn''t the firm''s answer."; PO1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul''s out, he wrote me this morning that he can''t put money in this year after all"; EX1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "someone only counts as a new investor once the DocuSign Completed notice is in. them telling us they''re in doesn''t count, and neither does me posting it here"; QD11 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Everyone else stays off: they passed without a call or meeting, or nothing from us since Sep 3."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Paul off vs In talks at $50,000. |
| writes | DIFFERENT | 18 vs 19 F/up cards (adds a Paul card); an extra In talks check item. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | One more row, the In talks checklist and two reply counts (In talks 7 vs 8, angels 1 vs 2). |

Authority chain: P → EM2 → QD12

Resolution relevance challenge: Not a strawman: Paul's own email is outside Fred's mailbox, Fred's copy of the Sep 29 nudge has no reply, the sheet still says 'in', and Leonard's rule says his posts don't count. QD12 decides what a pass is, PO1 is a dated, Fred-visible record of Paul's no to Leonard, and EX1's own wording limits the 'me posting it' clause to new-investor status in \#executives.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: PO1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Paul''s out, he wrote me this morning that he can''t put money in this year after all"; EX1 (Evals/task\_inputs/01\_Universe\_Inject.sql): "someone only counts as a new investor once the DocuSign Completed notice is in. them telling us they''re in doesn''t count, and neither does me posting it here"

Compared alternative: R
Resolution: EXCLUDED. Authority: Keep warm is 'they passed after we pitched them on a call or meeting this round', and the doc says a call counts only when it is on Fred's calendar ('calls that never went on Fred's calendar don't'). Fred's calendar holds no call or meeting with Paul Heydon (base Calendar: no Heydon/PERSON\_9902 event; the SQL's calendar rows add none), so Paul passed without a call or meeting, which the doc sends off the list: 'Everyone else stays off: they passed without a call or meeting'. Leonard's comment 1 on the card also limits the Keep warm checklist to firms that passed after a pitch call or meeting.
Resolution evidence: QD10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Keep warm: they passed after we pitched them on a call or meeting this round."; QD3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Plus any firm not on the list that we''ve had a pitch call or meeting with since we kicked off the bridge on Sep 3. A call counts when it''s on Fred''s calendar, even if he couldn''t make it; calls that never went on Fred''s calendar don''t."; QD11 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Everyone else stays off: they passed without a call or meeting, or nothing from us since Sep 3."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Paul off vs Keep warm. |
| writes | DIFFERENT | An extra Keep warm check item; same 18 cards. |
| destinations | SAME | Same folder, card, To Do list and thread. |
| contents | DIFFERENT | One more row, the Keep warm checklist and the Keep warm count (3 vs 4). |

Authority chain: P → EM2 → QD10

Resolution relevance challenge: Not a strawman: Paul did say yes after talking to Leonard, so a pass 'after we pitched them' is a natural reading. QD10 plus QD3's calendar test decide it, and QD11 places a pass without a calendar call off the list.
Delegation challenge: NOT_CLAIMED. One value per item; no choice is delegated.
Challenge evidence: QD3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Plus any firm not on the list that we''ve had a pitch call or meeting with since we kicked off the bridge on Sep 3. A call counts when it''s on Fred''s calendar, even if he couldn''t make it; calls that never went on Fred''s calendar don''t."; QD11 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Everyone else stays off: they passed without a call or meeting, or nothing from us since Sep 3."

Strongest-alternative challenge (B): Not a strawman: the forward is in Fred's mailbox before the cutoff, follows the Sep 18 interview on Fred's calendar and reads as a decline; without QD14 it would be a pass after a call.
Challenge evidence: A16Z1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1844748127814183717.json): "decision not to include"; GC1 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/gcal/data.json): ""summary": "\[USERNAME\_1453\] speedrun Interview 9/18/25"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5). Every ask maps to a cataloged write and every needed fact exists in a record Fred can open. Group, amount and build access are columns the doc defines and the records fill; amounts are whole dollars. The card's rules need only the group sets, Fred's calendar, the board's To Do list and the list's contact column, all reachable. Snowflake and Confluence aren't used.

| Ask | Capability | Tools | Feasible? |
|---|---|---|---|
| Read the email, doc, README, list, card comments, mail, calendar, Slack (including thread replies), Linear, Contacts | Read | gmail/gdocs/gdrive/gsheets/trello/gcal/slack/linear/contacts reads (`trello_get_comments` for the card's comments; `slack_conversations_replies` / `slack_read_thread` for the #executives and #zombie-match3d threads) | Yes |
| Create the send list in the folder and fill it | Create + move + write | `gsheets_create_spreadsheet` + `gdrive_move_file`, or `gdrive_create_file(parentId)`; `gsheets_values_update` | Yes (catalog) |
| Four group checklists on card 455, one item per firm or angel | Write | `trello_create_checklist` (idCard, name), `trello_create_check_item` (checklistId, name) | Yes |
| 18 F/up cards in To Do | Write | `trello_create_card` (idList `640643a3fd8f3ca308d93195`, name) | Yes |
| Comment on "F/up with Anel after the engine deep dive" | Write | `trello_add_comment` (cardId `68c99e98737744bd966aed24`, text) | Yes |
| Reply on Leonard's thread | Write | `gmail_reply_to_message` | Yes |

Dimensional feasibility: the only breakdown is "each group", and the doc defines the groups. Numeric observability: the one amount ($25,000) is stated in records ("25") and the counts are counts of rows. The 18-card write set is bounded by the cohort, not open-ended.

**Persona ACL Reachability:** PASS (5). Every scoped read is visible to Fred: his mailbox (Leonard's email, DocuSign notice, Paul nudge, the T-Accelerate and Dentsu threads, Hiro, Brightwater, LVP, Lakestar, GFR and Homa threads, the NCsoft thread with Anel's "Thu would work best" and Leonard's Calendly reply, the speedrun-feedback forward, the invites including the Oct 8 one), his calendar (the Oct 1 Dentsu and Oct 8 Michael Cheung meetings are on `calendar_id frederick.stone@harmonygames.co`), channels he belongs to (#bridge-pitch `C096HFA5Z8W`, #executives `C07C2866011`, #zombie-match3d `C0880U9751A`; channels.json lists `EMPLOYEE_0008_SLACK_ID` in each), the group DM `D05S58U4SAK` (members include `EMPLOYEE_0008_SLACK_ID`) and Drive files he owns or that are shared with him. Paul's own back-out email sits only in Leonard's mailbox; the answer doesn't need it, because Leonard's group-DM message carries the same fact to Fred. Linear, Trello and Contacts are unscoped.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5). The write set is the same under every reading: one file in the named folder, four checklists on the named card, 18 F/up cards and one comment in the board's To Do list, one reply on the named thread. "He wants to go through it with me" is Fred's own meeting, not a competing write. Robert's list-wide idea is declined in the email the prompt incorporates. Two variations come from the records, not the prompt's wording, and leave the writes unchanged: the reply's recipients (Reading K) and the F/up card titles, firm or angel name vs the contact's name (Reading P). Both are authorized variations; the rubric should accept either. "How many ended up in each group" pulls in the email's "how many firms and angels are in each group"; with Paul off, every group but New investor is firms only, so a per-group total and a firms/angels split give the same numbers.

**Contrived / Unnatural:** PASS (5). No timestamps, opaque ids, generated filenames, trap hints, hidden destinations (folder, card and thread are all named; the To Do list and the Anel card are named in Leonard's comment, which the prompt points to), audit-form wording or if-chains. The per-case rules live in Leonard's card comment and doc, not the prompt.

**Alignment with Today's Date:** PASS (5). Today is Wed Oct 1, 2025. Leonard's email is Tue Sep 30, 2:05pm PT ("as of tonight"); the doc's cutoff is "end of day Tue Sep 30 (Pacific)". Paul's back-out (14:55Z = 7:55am PT, "this morning") and Leonard's group-DM relay (17:05Z = 10:05am PT), the ZOM-567 comments (17:25Z–18:40Z) and Arthur's #zombie-match3d note (23:20Z = 4:20pm PT) are all Sep 30 in both zones, so no Pacific/UTC edge moves anyone. The card comment's "after Sep 30" has no edge either: the nearest investor event, GFR at 2025-09-30T17:30Z, is Sep 30 in both zones, and the Oct 1 1:30pm PT Dentsu meeting is Oct 1 in both. "Monday, Oct 6" is a Monday and the review is a future event on Fred's calendar.

**Originality / Sample Similarity (Phase 2.9):** N/A: no comparison samples supplied. The dataset-similarity gate (STEP 0.6) passes separately.

**Truthfulness:** PASS (5). All 11 premises verified (record saved): the Sep 30 email and its ask (Sep 30 21:05Z = 2:05pm PT); the bridge round; the Q4 investor update; "His email lays out what he's after" (including "Then do what I put on the Existing Investor Update card in Trello."); the folder "Q4 2025 investor update" (owned by Fred); the Existing Investor Update card (base card 455); Leonard's asks on it (two comments, Sep 14 and Sep 29, by `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes); his thread; the groups; the Oct 6 review (2pm PT, Mon Oct 6). None of these records changed in revision 26.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact. Drop Gmail and the DocuSign notice, the Hiro and LVP passes, NCsoft's unbooked Thursday call and the reply are lost. Drop Calendar and the In talks set, Keep warm's call test (which also keeps Paul off), both off-list firms and the Dentsu/Makers exemptions are lost. Drop Slack and Anton's $25K, Paul's back-out, Sciplay's pass, Arthur's Android correction for all four tester firms and most Awaiting reply outreach are lost. Trello supplies the checklist and follow-up rules and the existing Anel card; Sheets supplies the cohort and the contacts that tie Anel to NCsoft and Michael Cheung to Makers Fund; Docs supplies the rules and name; Contacts maps Edith Vane to Hiro Capital; Linear holds the ZOM-567 log Arthur corrects.

**Investigation + Action:** PASS (5). Writes across three services (the send list; checklists, cards and a comment; the reply), each fed by the investigation.

**Coherence (Bolt-on):** PASS (5). One workflow: build the list, set up the tracking and chasing Leonard asked for on the card, report the counts.

**Business Function (Executive):** PASS (5). Investor communications for a bridge round are founder/exec work.

## Phase 3: Universe Feasibility

**Data Existence:** PASS (5)
- Entities verified: the 2025 list names and contacts, the investor calls on Fred's calendar since Sep 3 and every event on it after Sep 30, the doc, README, folder, card 455 and its two comments, the To Do cards, the email thread, the NCsoft thread, DocuSign notice, Bridge angels sheet, ZOM-567 and its four comments, Leonard's group-DM posts (Anton and Paul), Robert's Sciplay note, Arthur's #zombie-match3d thread and Leonard's reply, and the Contacts rows.
- All retrievable via cataloged reads: Yes.

**Cross-Service Coherence:** PASS (5)
- **Revision 26 records checked (NEW).** The group-DM post `c5657466…` (17:05Z, "he wrote me this morning") follows Paul's 14:55Z email to Leonard (7:55am PT); Leonard is a DM member and already posts there (lines 102/104). With the #executives reply removed, the Sep 19 angel-update post is a standalone message (`thread_ts` NULL, counters 0), and nothing in the SQL still references `7fe55f30…`. Arthur's new thread parent `3cddf83c…` carries `reply_count` 1 and `latest_reply` = Leonard's reply ts; the base post it used to hang under (`c891232a…`) is no longer updated and stays self-consistent. The two new ZOM-567 comments fit the base record: NCsoft's "after the Sep 19 call" matches base Slack ("just finished a round 2 with NC Soft", Sep 19) and Brightwater's "added Sep 26" follows the Sep 25 meeting. The log and Arthur's later note don't contradict each other: one records the tester-list adds, the other says that list was never attached to the track, and expressly sets the log aside. Removing Karthic's emails leaves the base Bridge Round thread consistent (its Sep 22 TestFlight invite and Play link agree with the base #executives Sep 22 "Invites sent" exchange and with ZOM-567's Sep 22 entry).
- **Earlier records (REUSED, unchanged).** Card 455 `comments: 2` and `dateLastActivity` match its two comment actions; the Anel card (#456) fits the NCsoft thread; the Oct 8 event has a matching Sep 29 invitation in all four mailboxes; the Oct 1 Dentsu meeting agrees with the Dentsu thread and #executives; Anton ($40K → $25K, DocuSign Completed Sep 26); Paul's back-out threads to Leonard's Sep 29 nudge in Leonard's mailbox; Play Ventures (Griffin no, corrected Sep 25); Sciplay; the GFR slot moved to Sep 30; Hiro; Brightwater; LVP. No injected record is dated after the clock except the future start times of the Oct 6 and Oct 8 meetings.
- Not counted as inconsistencies: names listed twice (the doc handles them); "Treeo" vs "Treo" in a typed Slack post; row 82's "Superplay" label (SC-34; no Fred-visible record ties it to Supercell). The Oct 1 Dentsu meeting's anonymized twin ("[SOURCE_ORG_0001] & Dentsu") is the platform's anonymized-token pattern.
- Known base-data issues (Snowflake/Confluence, not scored): none touched by this task.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2, PASS/COMPLETE, SQL `69db98ae…`), checks A–C.
- Prompt-specific sources, access and configuration: supported. No error/async config or dynamic context applies.

| Prompt ask / source | Static evidence NEW or REUSED | Prompt-specific discovery/access/configuration evidence | Task coherence |
|---|---|---|---|
| Email, doc, README, folder, card | REUSED (Eval 0 A–C) | Fred's mailbox; Drive ownership/shares; Trello unscoped | PASS |
| Groups (Gmail, Slack, Calendar, Contacts, list) | REUSED + NEW (Paul's relay now in the group DM) | Fred in `D05S58U4SAK`, #executives, #bridge-pitch; Fred's calendar has no Paul event | PASS |
| Follow-up cards and comment (Trello, Calendar, list, NCsoft thread) | REUSED | To Do list read; Fred's calendar after Sep 30; contact column; Fred's NCsoft thread copy | PASS |
| Amounts and build access | REUSED + NEW (two ZOM-567 comments; Arthur's new #zombie-match3d thread; removed emails) | Group DM members include Fred and Leonard; Linear unscoped; Fred in #zombie-match3d (`C0880U9751A`), thread reply readable with `slack_conversations_replies` / `slack_read_thread` | PASS |

## Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Every fork settled by a quoted, Fred-visible or incorporated record, or an authorized variation (comparison above; fork list in the Deep Recheck) |
| Prompt | Feasibility | 5 | Every ask is cataloged and every needed fact exists |
| Prompt | Persona ACL Reachability | 5 | All required scoped reads are visible to Fred |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One write set under every reading; recipient and card-title variations come from the records and are authorized |
| Prompt | Contrived / Unnatural | 5 | Plain, natural request; detail lives in records |
| Prompt | Alignment with Today's Date | 5 | Today Oct 1, cutoff end of day Sep 30 PT, every Sep 30 change is Sep 30 in both zones, review Mon Oct 6 |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Originality — Dataset Duplicate (STEP 0.6) | 5 | Same scenario (0.762 < 0.80): no score change |
| Prompt | Truthfulness | 5 | All 11 premises verified |
| Prompt | Tool Use & Cross-service | 5 | Eight services, each changes graded facts or writes |
| Prompt | Investigation + Action | 5 | Writes in Drive, Trello and Gmail fed by the investigation |
| Prompt | Coherence (Bolt-on) | 5 | One workflow; no removable ask |
| Prompt | Persona | 5 | Exact roster match; role fits |
| Prompt | Business Function | 5 | Founder/exec investor communications |
| Prompt | Assigned Competency | 5 | Investor relations = Corporate Ops |
| Prompt | Assigned Task Skill | 5 | Retrieval is central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | Every entity exists and is retrievable |
| Universe | Cross-Service Coherence | 5 | New Slack and Linear records agree with their threads, counters, members and timeline |


### Issues Found

None at any severity.

### Recommended Improvements

1. **Build access (rubric/OE note, no score effect).** NCsoft and Brightwater Games Fund are now "iOS only" (ZOM-567 logs their adds, and Arthur's Sep 30 #zombie-match3d note says nobody on the tester list has Android "whatever the Linear log says"). T-accelerate and Dentsu Ventures stay iOS only, now on the same note, and Andreessen Horowitz, GFR Fund and Homa are "none". Update any OE or rubric row that still has NCsoft or Brightwater as "none" or cites Karthic's and Arthur's Sep 30 emails, which are no longer in the SQL.
2. **Paul Heydon (rubric/OE note, no score effect).** Paul stays off the send list (no row, checklist item or F/up card). The record that shows it is now Leonard's Sep 30 message in the group DM ("Paul's out…"), not an #executives thread reply. Update any OE that reads it with a thread-reply call on #executives.
3. **Card titles (optional, no score effect).** Leonard's Sep 29 comment says "named F/up with and the name" without saying which name, and the board's own examples ("F/up with Anel after the engine deep dive", "F/up with Martin") use a person's first name. If you want one title per firm, say in that comment whether the title uses the firm or angel name from the send list or the contact's name. Otherwise the rubric must accept either (Reading P).
4. **Rubric and OE notes for later stages (no score effect).** Accept checklist titles that name the group, card titles with the firm or angel name or the contact's name, any comment text on the Anel card that marks the Q4 follow-up, a Google Sheet or a Google Doc named "Q4 update - send list", a reply or a reply-all, and counts given per group either as one number or split into firms and angels. Groups stay 1 / 7 / 14 / 3 (25 rows) with 18 F/up cards. Makers Fund is still Awaiting reply (the Oct 8 meeting hasn't happened). For Homa, accept the name as the records show it ("[PERSON_NAME_0854]" in mail, "HOMA" in Fred's Slack). Keep rows off row 82's "Superplay" vs "Supercell" label (SC-34) and count repeated names once.
5. **Same-scenario note (no score effect).** The library holds three Leonard → Fred investor-list tasks at 0.72–0.76. Yours is distinct in its deliverables (a separate send list, group checklists, follow-up cards and group counts), so no change is needed.
6. **Inputs to re-grade (process).** The SQL changed since the last /hardness run, so that result no longer covers this version; send /hardness again, then /oe and /rubric.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review. Each got only the saved inputs, SEARCH.md, the persona folder, common_errors.md and deep_recheck.md. None got the record, findings, scores or verdict, or access to reports/. The record was saved after the main-session check below.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 4 prompt sentences plus every incorporated instruction (email, Q4 doc, README, both card comments, #executives note); 35 forks | 2 + 1 platform note | 2 (both already authorized variations); platform note recorded |
| P2 | 4 prompt sentences; services, visibility, hidden records, coherence of task-touched records, write feasibility, date slips | 1 | 0 |
| P3 | 4 sentences / 16 claims plus SQL checks (collisions, authors in channels, quoting, ts vs created_at, clock, weekday/date pairs) | 1 (SQL advisory) | 0 |
| P4 | 4 prompt sentences | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "Please put the send list in my Q4 2025 investor update folder…" | README `f_c61a0e93b7d24f58a2e917`: "Google Sheets or Docs only, no uploads"; Q4 doc `f_3b9e61c04d7a52e8f1a6c2` heading "Sheet" | §2 What gets written | Clarity | CONFIRMED | Records opened. Already Reading I, AUTHORIZED_VARIATION: the README the email incorporates allows either, and the same name, folder and contents follow. No score change; the rubric must accept a Google Sheet or a Google Doc |
| DR2 | P1 | "do what he asked on the Existing Investor Update card in Trello" | Trello action `68db03b86054eff7e8e92474` (Leonard, Sep 29): "named F/up with and the name"; To Do card `68c99e98737744bd966aed24` "F/up with Anel after the engine deep dive" | §2 What gets written | Clarity | CONFIRMED | Records opened. Already Reading P, AUTHORIZED_VARIATION: the same 18 cards in the same list with either title. No score change; the rubric must accept the firm/angel name or the contact's name |
| DR3 | P1 | "Please put the send list in my Q4 2025 investor update folder…" | Fred's calendar and thread `frederick@harmonygames.co_1843552279434086285.json` show Homa as "[PERSON_NAME_0854]"; #executives Sep 17 "HOMA feel free to join later" | Platform note | PLATFORM:anonymized-token | CONFIRMED | Records opened. The token as shown is a correct answer; not scored (fork F20) |
| DR4 | P2 | "Please put the send list in my Q4 2025 investor update folder, do what he asked on the Existing Investor Update card in Trello, and reply on his thread with how many ended up in each group." | Base gsheets `f_48247af79428823c3cac92` row 8 London Venture Partners "Pitch/Catch up on 09/07" vs Fred's calendar "LVP <> [SOURCE_ORG_0001] Catch Up" 2025-09-09T16:30Z | Date-slip severity | Cross-Service Coherence | REJECTED | The SQL overlays this cell: line 31 `UPDATE gsheets.sheets_sheets SET grid_json = …` writes row 8 as "Pitch/Catch up on 09/09 - waiting to hear back from them if they want to pursue further", matching the calendar and #bridge-pitch "LVP (sent, meeting on Sep 9th)". The pass read the base sheet without the overlay. This is known data issue SC-10, already handled; the LVP date is not graded either way |
| DR5 | P3 | SQL `INSERT INTO gslides.slides_pages (… notes)`, `gslides.slides_page_elements (… table_json, ordinal)` | `Evals/references/schema/injection.json` lists none of these columns | P3 SQL check | Injection schema compatibility | REJECTED | Same advisory Eval 0 carries. The schema README makes a mismatch with the unverified snapshot a provisional advisory, and no graded value sits in these columns. Stays in the Injection Gate section |

Main-session checks of what the passes relied on (records opened): SQL line 31's row 8 (LVP, "09/09"); SQL lines 106 (group DM `c5657466…`), 108/110 (Arthur's thread and Leonard's reply), 305–313 (ZOM-567 and its four comments) and 23 (the Q4 doc, including "Build access"); channels.json membership of `EMPLOYEE_0008_SLACK_ID` in `D05S58U4SAK`, `C0880U9751A`, `C07C2866011` and `C096HFA5Z8W`; base #executives Sep 22 tester exchange ("Invites sent", the Play internal-test link, "you added him to testflight already?"); base T-Accelerate thread `frederick@harmonygames.co_1842283406259093714.json` (Sep 22 TestFlight invite and Play link) and Dentsu thread `frederick@harmonygames.co_1843473831194478743.json` (Sep 23 offer of TestFlight or Google Play); complete scans of Fred's Sep 2025 mailbox for "testflight", "internaltest" and "tester" and of Sep 2025 Slack for "testflight", "tester list" and "internal track" (no tester grant for a16z, GFR Fund or Homa). P1's independent derivation (1 / 7 / 14 / 3, build access, 18 cards, the Anel comment, no card for Dentsu or Makers Fund) matches the main derivation exactly.

Effect on verdict: unchanged; every dimension stays at 5.

Fork list (each checked against its record):
- F1: New investor | Anton Bernstein, $25,000 | Anton at $40,000 | Settled by: group DM "he can only do 25 this time, not the 40" + "Anton signed the 25 one" + DocuSign "All signers completed … Harmony Games SAFE - Anton Bernstein.pdf"
- F2: Paul Heydon | Off (no row, item or card) | In talks at $50,000 with an F/up card (Reading Q) | Settled by: group DM `D05S58U4SAK`, Sep 30 17:05Z, "Paul's out, he wrote me this morning that he can't put money in this year after all" + doc "Passed means they've told us no for this round"; the #executives rule's "neither does me posting it here" is scoped to "someone only counts as a new investor once the DocuSign Completed notice is in"
- F3: Paul Heydon | Off | Keep warm (Reading R) | Settled by: doc "Keep warm: they passed after we pitched them on a call or meeting this round" + "calls that never went on Fred's calendar don't" + "Everyone else stays off: they passed without a call or meeting"; no Paul event on Fred's calendar (base and SQL)
- F4: a16z | In talks | Keep warm | Settled by: doc "the program's decision and the feedback that comes with it aren't their answer on the bridge"; Sep 18 interview on Fred's calendar
- F5: NCsoft, Homa, Brightwater, GFR, Dentsu | In talks | off or Awaiting reply | Settled by: NCsoft Sep 10 call; Homa "we are currently seeking extension funding on our seed round" + doc "an investment alongside a co-dev deal, they count"; Brightwater Sep 25 call + doc "off-list firms with a call included"; GFR Sep 30 17:30Z call; Dentsu Sep 23 call
- F6: Keep warm | LVP, Hiro Capital, Sciplay | Sciplay or Hiro elsewhere | Settled by: Robert "Sciplay's out too … they're passing on this round" + Sep 15 meeting; LVP "we won't be joining this round"; Hiro "going to pass on the bridge" after the Sep 23 call
- F7: Awaiting reply (14) | as derived | some left off | Settled by: #bridge-pitch outreach posts + doc "'Us' includes anyone who reached out … on our behalf"; "pinged Initial Capital on LinkedIn about the bridge"; Treo "I sent them the deck" on Sep 3 + "that day included"
- F8: e2vc / the Sep 29 Turkish VC call | Awaiting reply | Keep warm or In talks | Settled by: doc "calls that never went on Fred's calendar don't"
- F9: Sony Mobile | Awaiting reply | off | Settled by: doc "An advisor's own read on whether a firm invests isn't the firm's answer"
- F10: Stays off | Play, Grishin, Lakestar, 1AM/March, Mattel, Transcend, Acterra, untouched names | included | Settled by: "it's still their no for this round"; "Grishin Robotics (No, they want metrics)"; "Lakestar is no longer investing in games"; "They don't do bridge"; Mattel "only been an RFP conversation"; doc "plans to reach out don't count"
- F11: Build access, T-accelerate, NCsoft, Brightwater, Dentsu | iOS only | iOS and Android per the ZOM-567 log | Settled by: Arthur in #zombie-match3d, Sep 30 23:20Z (4:20pm PT): "nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them." + doc "Arthur tracks the tester adds"
- F12: Build access, a16z, GFR Fund, Homa | none | iOS from public store links | Settled by: doc "The public store pages don't count"; no tester record for these firms (complete scans)
- F13: Checklists | four on card 455 (1/7/14/3) | Keep warm only | Settled by: Sep 14 comment and Sep 29 "besides the Keep warm one, give every other group … its own checklist"
- F14: NCsoft follow-up | comment on the Anel card | none (Thursday call agreed) | Settled by: comment "Anyone we already have a call or meeting with on Fred's calendar after Sep 30 doesn't need one" + no NCsoft event on Fred's calendar after Sep 30
- F15: NCsoft card | comment on "F/up with Anel after the engine deep dive" | new card | Settled by: "If one of them already has a card in To Do, comment on that card instead of adding another" + list "NCsoft … Anel Ceman"
- F16: Dentsu Ventures | no card | card | Settled by: Fred's calendar "Harmony Games & Dentsu" Oct 1
- F17: Makers Fund | Awaiting reply, no card | In talks or a card | Settled by: doc "as of end of day Tue Sep 30 (Pacific)" and "we've had a call or meeting"; list "Makers Fund … Michael Cheung" + Oct 8 meeting
- F18: Card titles | firm or angel name | contact's name | Both fair (authorized variation, Reading P): comment "named F/up with and the name"; the rubric must accept either
- F19: File type | Google Sheet | Google Doc | Both fair (authorized variation, Reading I): README "Google Sheets or Docs only"; the rubric must accept either
- F20: Homa's name | "Homa" | "[PERSON_NAME_0854]" | Both fair: the anonymized token is the source string (platform note, DR3)
- F21: Reply | counts per group | reply vs reply-all; total vs firms/angels split | Settled by: email "reply here with how many firms and angels are in each group"; recipients an authorized variation (Reading K); with Paul off, the split and the totals carry the same numbers
- F22: Scope | only who qualifies under the doc | everyone on the 2025 list, or only who Leonard emailed | Settled by: email "Let's not, only the people the doc says"
- F23: File name | "Q4 update - send list" | "Q4 investor update - send list" | Settled by: README "Name the send list "Q4 update - send list""
- F24: Repeated names | one entry each | two entries | Settled by: doc "a repeated name is still one entry"
- F25: Edge values | Pacific and UTC cutoffs give the same groups | — | Settled by: doc "as of end of day Tue Sep 30 (Pacific)" and "that day included"; Leonard's relay 17:05Z, the ZOM-567 comments 17:25–18:40Z and Arthur's note 23:20Z are Sep 30 in both zones; the a16z forward (Oct 1 03:23Z = Sep 30 PT) changes nothing under F4

Platform defects: PLATFORM:anonymized-token (DR3, not scored). Anonymized tokens (`[PERSON_NAME_0854]`, `[SOURCE_ORG_0001]`) are the source strings.

### FINAL VERDICT: PASS

Score: 5

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort not exposed by the runtime

Next action: Send /hardness again (the SQL changed since the last hardness run), then /oe and /rubric. In the OEs and rubric, set NCsoft and Brightwater Games Fund to iOS only (with T-accelerate and Dentsu Ventures; a16z, GFR Fund and Homa none), cite Arthur's Sep 30 #zombie-match3d note rather than the removed Karthic/Arthur emails, read Paul's back-out from the group DM, keep groups 1 / 7 / 14 / 3 and 18 F/up cards, and accept either file type, reply form and card-title form.

Evidence limits: The Evals/Docs PDFs/XLSX were not re-extracted this round (unchanged since the last review; their rules are applied through Eval 1 and scoring.json). Write tools' runtime behaviour is supported by the catalog only; /prompt needs no run.

Eval version: task-quality-v1

Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225

Reviewed prompt SHA-256: b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9

Review context SHA-256: c76696d7920dc0087ca5376554ef20c92f62a77035ed8df20d2155d98db20317

Prompt record SHA-256: 2990e8c44cde8032728daaad28a270bba9a213365f2a98031655cdddba98addf

**Lowest Dimension:** None below 5.

**Summary:** The prompt is unchanged and still a natural four-sentence handoff. SQL revision 26 moves Paul Heydon's back-out to Leonard's group-DM message with Fred, which keeps him off the list. It replaces Karthic's and Arthur's emails with two more ZOM-567 entries and one Arthur note that overrides the log for all four tester firms. NCsoft and Brightwater are now iOS only. The answer is still 25 rows (1 / 7 / 14 / 3), 18 F/up cards and the Anel-card comment, and every fork is settled by a Fred-visible record.
