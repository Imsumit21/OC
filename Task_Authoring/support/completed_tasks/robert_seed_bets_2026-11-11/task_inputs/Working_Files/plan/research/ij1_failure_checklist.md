# Pre-submission failure checklist: robert_seed_bets (task_inputsS2)

Facts and locators only. No prompt, Oracle Event or rubric text. Report paths are relative to `Task_Authoring/support/completed_tasks/`.

Short names:

- WD = `robert_winddown_closeout_2026-10-30/eval_reports/6adfee3f27ce6ca81b457137_`
- LLC = `robert_llc_takeover_2026-11-06/eval_reports/`
- VIN = `vincent_zm3d_release_gate_2026-11-06/eval_reports/6ae9909f7b5249d3148f3707_`
- JB = `julia_zm3d_beta_calendar_2026-11-07/eval_reports/`
- JD = `julia_zm_difficulty_baseline_2026-11-01/eval_reports/`
- FB = `frederick_bridge_pipeline_2026-11-03/eval_reports/`
- FQ = `frederick_q4_commitments_2026-11-05/eval_reports/`
- CL = `claire_zm3d_halloween_art_plan_2026-11-07/eval_reports/`
- DG = `douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_`

## 0. Scope and tallies

Read in full: the Findings and Advisories of all 63 `0_injection` reports, the dimension tables and Issues Found of all 52 `1_prompt` reports, the 11 README Lessons sections, learnings 10-26, 35-44, 49-51, 56-59, 63-66, both memory files, NB-1 to NB-33. Deep Recheck tables were sampled by keyword, not read row by row.

Limits:

- `frederick_account_handover` and `frederick_card_spend` have no eval_reports folder.
- robert-vendor-schedule's reports aren't on disk; its failures come from learnings 10-25.
- `plan/build_sql.py` and `01_Universe_Inject.sql` (77 INSERT, 0 UPDATE) appeared at 22:29 during this review. Where a finding is a builder fact I say so. `plan/notes.json` doesn't exist yet, so the 55-odd extra notes have not been reviewed.

/injection: 10 FAIL verdicts on disk (WD 5, VIN 2, JD 2, JB 1), plus vendor-schedule rev1 and one JD round whose report is missing (named in JD `0_injection_PASS.md` L90). Every FAIL was Check C except WD (1) F3 (Check A) and the missing JD round. **Check B has never failed.**

/prompt, reports scored below 5:

| Dimension | Reports | At 2 (FAIL) | At 3 (NON-FAIL) |
|---|---|---|---|
| Cross-Service Coherence | 23 | 13 | 10 |
| Unique Ground Truth | 17 | 17 | 0 |
| Clarity & Specificity | 9 | 9 | 0 |
| Business Function | 8 | 0 | 8, all WD |
| Contrived / Unnatural | 2 | 2 | 0 |
| Originality (dataset duplicate) | 1 | 1 | 0 |
| Feasibility | 1 | 1 | 0 |
| Truthfulness | 0 on disk | 1 in learnings 20 | 0 |

Scoring rule as reports state it: any State/Lifecycle or Quantitative item fails; two or more low-impact items fail; one low-impact item is NON-FAIL 3 (memory coherence-presweep; WD `1_prompt (6).md` L410: "A Quantitative inconsistency never qualifies for the minor band").

## 1. /injection Check C (ranked by FAIL rounds)

| # | Failure and locator | FAILs | Rule | Applies? | Check or change, by seed |
|---|---|---|---|---|---|
| C1 | Seeded fact contradicts a base record found by whole-universe search. WD (1) F1 a-g, F2; WD (3) F1, F2; WD (4) F1 (L238, "free plan" when the vendor had deleted the org); WD `0_injection.md` F2; JD `FAIL_r4` C1 (sheet history vs git); vendor-schedule F1-F8 (learnings 10-16) | 6 rounds, about 25 defects | Search every mailbox, channel, sheet and PDF for each vendor, person and global fact. Persona view doesn't limit contradiction search. Take status from receipts, not cost sheets | **Yes, highest risk** | **Linear notes**: 22 cohort notes are audited in sw2; the 55-odd row-floor notes aren't written. Each is a new C1 exposure. **Leapblock post**: see W6. **Arthur's mail**: invented Carta link, consistent so far (`plan/unresolved.md`) |
| C2 | Text relies on an event or record dated after it. WD `0_injection.md` F1 (Sherwood call, L250); JD `FAIL_r2` F1 (updateCard before the reply, L82). Same class at /prompt: JD `FAIL_r1` #5, CL `FAIL_r1` #4, VIN `1_prompt.md` #7, JD `NONFAIL_r9` #1; FQ r1 adv 1; learnings 13, 17 | 2 at /injection, 4 at /prompt | List base events each text names; text must be later than the first base record of each | Yes | Order is sound after sw2 T1: Trello 22:36, sheet 22:44, deck 22:52, project 23:12, method 23:52, contact 00:58, ask 01:23, hold 01:31, statement 08:37, Arthur 16:26. **Linear notes** must end before the ask (builder asserts it). **Deck** quotes sheet numbers: order holds |
| C3 | A rule contradicted by the record's own worked example. VIN (1) F1, VIN (2) F1 (L162, L154) | 2 | Test every rule sentence against every injected example, including ones written before it | Yes, narrow | **Sheet**: its one row is labelled quick pass and predates the method, so it isn't an example of the method. Keep the "quick pass" note |
| C4 | Record names an artifact that doesn't exist. WD `0_injection.md` F3 (zip, L265); DG `1_prompt.md` (prod branch, NON-FAIL) | 1 + 1 | Every named file, branch or board resolves | Yes | **Method** "our board", **ask** "the doc", "Angel note working", "draft deck", "Payee history": all seeded under those exact titles. Confirm in the built SQL |
| C5 | SQL edit can't reach Drive bytes. WD (6) F1 (L243, P&L header) | 1 | Never edit a base file that has `content_path` | No | No base row is updated. Keep it so |
| C6 | Impossible weekday/date in text. JB `FAIL_r1` F1 (Fri Oct 29) | 1 | Check every weekday/date pair | Yes, passes | **Ask** "tuesday" = Feb 17. **Invite** "Tue Feb 17, 2026 9am - 10:30am (PST)" = 17:00-18:30Z. Correct |
| C7 | Doc style runs don't match text. JB `FAIL_r1` F2. Advisories: LLC r1 A-1 (zero-length run), FQ r1 C-adv 4 | 1 | TITLE covers the title line, no heading run mid-sentence, no zero-length run, last run ends at body length in characters | Yes, passes | **Method**: builder sets TITLE 0 to len(title)+1, NORMAL_TEXT to len(body), character-counted, so curly apostrophes are safe. "Buckets." and "Which bet." are inline, so no heading run |
| C8 | Review comment attached to an earlier review. JB `FAIL_r1` F3 | 1 | - | No | No GitHub seed |

## 2. /injection Check A and Check B

| # | Failure and locator | FAILs | Rule | Applies? | Check or change |
|---|---|---|---|---|---|
| A1 | Placeholder identity strings that resolve to nobody. WD (1) F3 (L241) | 1 | Any token in seeded text must exist in that form in the base | Yes, passes | **Linear titles** use bank spellings. 21 of 22 match `svb_processed_robert.json`. `Martin [PERSON_NAME_7250] Walsh` isn't in that file (it normalised the name) but hg search shows it in `threads/00015809.json /messages/2/body`, so it is a real string. Check A passes |
| A2 | Trello idShort out of creation order. JD round before `0_injection_PASS.md` F2 | 1 | Next free idShort, after its neighbours in time | Yes, passes | **Trello** idShort 456, base max 455 (WD (1) L241). Accepted in LLC |
| A3 | Injected Confluence rows. JD F1; WD `1_prompt (2).md` #2 (Major: Confluence deactivated 2025-10-03); learnings 26 | 1 + 1 | Stay off Confluence | No | Confluence not used |
| A4 | Identifier outside the base series. Learnings 15 (advisory then) | 0 at FAIL | Follow the base form | **Yes, new** | **Contacts** `cnt_df6a482c50c0`: base ids are 24-hex (`d4a339f7f6aafffdc2dabb9a`, `7e103a10a99b3f78e4ea8d0c`), and all four prior tasks used 24-hex. Mint 24-hex. No local tool catches this |
| B1 | Columns outside the unverified snapshot. Advisory in about 50 reports: `linear_projects.links_json` (19 reports; WD A1), `linear_comments.sequence`, `slides_pages.notes`, `slides_page_elements.table_json`/`ordinal`, `gcal_events.extras_json`, `drive_files.drive_id`, `linear_issues.uuid` | 0 | Not a defect. LLC's SQL carried `links_json`, `notes`, `table_json`, `ordinal` and its baselines read the seeded records, so they load (inferred). `sequence` isn't needed | Yes | Builder matches LLC's columns exactly, which is the safe choice. Expect the advisory; don't chase it |

## 3. /prompt dimensions (ranked)

### Cross-Service Coherence (23)

| # | Failure and locator | Reports | Rule | Applies? | Check or change |
|---|---|---|---|---|---|
| P1 | Injected fact vs base truth. WD `(2)` #1 (Vercel on GitHub's line), `(3)` #4 (Layer date); VIN `-1` #1 (SC-45 migrations), `-2` #1 (1.3.24 store build); JD r3 #1; minor in FB r2 #2, JD r2 #2, JB r1 #8 | 8 | /injection PASS clears nothing here. /prompt reads git, Snowflake and code | Yes | As C1. **Linear notes and Arthur's mail** |
| P2 | Graded value rests on one side of a base numeric conflict. WD `1_prompt.md` #4, `(1)` #1, `(6)` #1 (L410: "a rule telling the Agent to prefer the ledger, does not remove the dependency"); cleared only in `(7)` by taking AWS off the register. Reviewers split: `(4)` P2-DR1 REJECTED the same conflict that `(6)` P2-DR7 CONFIRMED | 3 FAIL | Removing the dependency works. Explaining it doesn't | **Yes, top risk** | **Revenue**: REVENUE_DAILY 12,354.99 vs P&L "Mobile revenue (cash in)" 9,859.36 vs ledger 9,693.55 (`sc2_coherence.md` L191). Every graded revenue figure takes the Snowflake side and "as recorded" is the same kind of rule. See W5. **Bank vs books**: Leapblock 374,654 vs ledger art_outsourcing 86,000; Deel 1,015,347 vs ledger (sc2 L183-184). Ledger is off the path, but see W4 for the P&L |
| P3 | Status contradicts own activity. DG (1) #1, CL r1 #2-3 (Todo with finished notes; Canceled, no `canceled_at`), JB r2 #1 (checklist vs child, SC-15), FB r1 #4 | 4 FAIL | State/Lifecycle always fails | Low | **Linear**: all 22 issues Backlog, notes are memories, none says done. Keep it that way in the added notes |
| P4 | Minor base slip in data the task reads. WD `(2)`-`(7)` HG Costs header year (6 reports, held `(4)`, `(5)`, `(7)` at 3); FB r5 (LVP date) | 7 | One minor caps at 3; two fail | **Yes, if the P&L is on the path** | **Trello** points at the P&L, so it is at risk of being task-touched. See W4 |
| P5 | Hidden record contradicts a key. FB r1 #9 (Mattel, Moderate, scored) | 1 | Records the persona can't see still count against the key | **Yes** | **Oleg ENG-2459**. See W7 |
| P6 | Temporal field. CL r1 #4, JD r9 #1, JD r1 #5 | 3 | `updated_at` at or after the last child; sheet modified after what it names | Yes, passes | **Linear** builder sets issue `updated_at` = last note |

### Unique Ground Truth (17) and Clarity (9)

| # | Failure and locator | Reports | Rule | Applies? | Check or change |
|---|---|---|---|---|---|
| U1 | Open set in a rule; one record per item never converges. JB r1, r3 (about 90 candidates); FB r1 #1-8; WD `1_prompt.md` #3; JD r1 #1, r11 #1; learnings 63 | 6 | Close the rule, census the universe | Yes | Method is closed by date, receipt and bucket. **"reached your mail"** closes off-bank: WU 5 receipts, Payoneer requests aren't receipts. First Upwork and Fiverr Gmail hits were a newsletter and a quoted aside, not payments (sampled, not a census) |
| U2 | Two rule sentences fit one member. VIN `(1)`, `1_prompt.md` #2-3; JD r2 #1; WD `1_prompt.md` #2; learnings 21 | 5 | Apply each sentence to each account | Yes | **Method**: "Everything on Deel counts as team" vs "Our own pay ... aren't in here" if a founder was paid on Deel. No record in sc1/sw2 says one was; check before SQL. **JPMorgan**: "Every payee keeps its line" covers it |
| U3 | A cell value has no definition. VIN `(2)`, `-3` (build status "n/a" vs "in candidate") | 2 | Every column header value needs a rule | Yes | **Sheet** header "Bucket": JPMorgan's value is undefined (three buckets, cohort says "Not a cost"). See W8 |
| U4 | Close-state fork. WD `1_prompt.md` #2 (Canceled vs open); LLC r1 F3 (Todo vs Canceled) | 2 | Name the state | **Yes** | **Method** "close each payee's issue". See W3 |
| U5 | Boundary with no timezone or edge. JD r1 #3 | 1 | Rule edges need a basis | Passes | No notice within 5 days of Jan 8/9 or on Nov 23/24 (sw2) |
| U6 | Owner's own claim doesn't settle its gap (SCOPE_GAP). JB r3 #1 | 1 | Use a non-owner where possible | Partly | **JPMorgan** rests on Arthur alone, but the method says "one of us has said", so his word is the rule's test |
| U7 | Completeness claim. WD fork F3 in learnings 23 | 1 | Don't claim completeness a census can't prove | **Yes** | **Ask 2, project description**. See W1 |
| U8 | Clause with no truth value. JB r3 #2 ("unverified build"); learnings 63 | 1 | Trace each sentence to a truth value, delete the rest | **Yes** | **Statement** last sentence, **project** "for Sunset's file". See W2, W6 |

### Other dimensions

| # | Dimension | Failure and locator | Applies? | Check or change |
|---|---|---|---|---|
| O1 | Business Function | WD all 8 reports at 3: "vendor close-out work fits Finance/Legal/HR/Ops at least as well as Executive". Blocks a 5, never a pass by itself, but with one minor it held NON-FAIL. LLC scored 5: "founders' strategy and money decision" | **Yes** | A notice-by-notice reconciliation reads as bookkeeping. §0 remit (investor accountability) must show in the **ask**: the angel calls and the deck do that. Don't let the prompt read as a reconciliation job |
| O2 | Contrived | JD r1 #4 (hidden destination the persona knows); JB r1 #3 (prompt restates fields) | Prompt only | **Ask 2** names the destination, so the prompt can defer to it |
| O3 | Originality | FB r4 (0.804 >= 0.80). LLC neighbour 0.776, same-scenario note | Prompt | Can't be measured locally (`unresolved.md`). Robert + Leonard + #winddown is the third of its kind |
| O4 | Feasibility | WD `(3)` #1 (value only in a PDF attachment; Gmail attachments return no bytes) | Check | **Leapblock**: fine, the statement carries the total. Drive PDFs stay unread |
| O5 | Truthfulness | Learnings 20: "this morning" against a Saturday universe date | Prompt | Clock day is Saturday Feb 14. Ask was Friday UTC, Thursday PT |

## 4. Schema and format defects the platform flagged

| Service | Defect or convention and locator | Severity then | S2 status |
|---|---|---|---|
| Slack | id = sha256("channel\|ts")[:32] (memory; re-verified on normal base `6d8c8d8a…`) | Check A | OK. ask `fa707da5679e86fd88f6638bd1828bfe`, ask2 `f5b759f3d1c117ac1596b1bdf0abdb93`, statement `6312d121675119df7a441f9ca5c6b4cb` |
| Slack | `ts` = `created_at` (WD (1)) | Check C | OK, builder derives it. Ask 2 is 01:24:19Z; §11 lists only 01:23:41Z |
| Slack | ts ending in 9 (memory, synth-cut) | Format | All three end in 9. LLC passed without it |
| Slack | `thread_ts_legacy`: own ts only with replies; NULL otherwise (JB r1 A7, DG A2) | Advisory | OK, NULL. `minted_ids.json` still holds a stale `parent_id` for the ask, but builder ignores it |
| Slack | Reply under an unrelated parent (LLC A-3, 4 reports; JB A5) | Advisory | None, both are top-level |
| Slack | Post after export end (NB-6, 7 FAILs) or by a channel leaver (NB-1, 37 FAILs) | Card | OK: latest 08:37Z; EMPLOYEE_0024 not on NB-1 |
| Gmail | Thread id >> 20 = mail time in ms (memory; WD (1) "encode their message times") | Format | **Off.** Arthur's id encodes 16:26:44.951, `internal_date` is .000. Invite id encodes 01:31:17.193, mail is 01:31:20. LLC's matched exactly. Re-mint |
| Gmail | `history_id` NULL (WD (1)) | Contract | OK |
| Gmail | Snippet must match how the body starts (JB A3) | Advisory | OK, built from body. 175 chars is the synth-cut length; LLC used 140, and normal base wasn't measured |
| Gmail | Labels: own copy SENT, inbound `INBOX, IMPORTANT, CATEGORY_PERSONAL` (LLC) | Format | OK, same as LLC |
| Gmail | Message-ID local part and per-sender prefix (memory) | Format | Arthur's is minted to that form. Check the prefix against a base Arthur mail |
| Gmail | "Re:" outside its thread (JB A2, JD C-2) | Advisory | Not used |
| Gmail | "attached" with empty attachments (FB r1 A3, FQ C-adv) | Advisory | Arthur's mail claims none |
| Gmail | Invite with `invite.ics` metadata and no bytes (WD A7) | Advisory | Same shape, no fact relies on it |
| Gmail | `size_estimate` = body + 900 (LLC) | Format | OK |
| Drive | No `content_path` or `size` on injected native files (WD (1); memory) | Contract | OK, columns omitted |
| Drive | `web_view_link` missing (JB r1, r2: unscored, only when a link must be built) | Advisory | Not needed: seeds name files by title. Leave NULL as LLC did |
| Drive | Sharing mirror across Drive and Docs/Sheets/Slides (633/633 base) | Check C | OK, one `SH` list. Robert and Arthur both writer |
| Drive | Folder `modified_time` at or after newest child (memory) | Format | Not updated, same as LLC, which passed |
| Docs | `style_runs_json` (C7) | FAIL | OK |
| Docs | `revision_id` style (JD A4) | Advisory | Same form as LLC |
| Sheets | `grid_json` list of lists within row/column counts; sheet modified after what it names (CL r1 #4) | Check B/C | OK, 1000 x 26, names nothing later |
| Slides | Page and element shape; `notes`, `table_json`, `ordinal` advisories | Advisory | Same as LLC |
| Linear | `state_history_json` '[]' required (lint); `state_id` a base literal; id = identifier; contiguous numbers (WD (9) A8) | Check B | OK, Backlog, 2438-2459 |
| Linear | `canceled_at`/`completed_at` set when closed (CL r1 #3, 372/372 base) | Lifecycle | N/A, nothing closed |
| Linear | Comment after close (learnings 50; memory) | Always fails | N/A, nothing closed |
| Linear | Issue `updated_at` = last comment (WD (1); JD A4) | Check C | OK |
| Linear | Two comments with one timestamp (WD `(4)` #3) | Advisory | Builder spaces notes, but check after notes.json lands |
| Trello | `dateLastActivity` on the card = action date (T06) | Format | OK |
| Trello | Board `dateLastActivity` not bumped (FB r2 A4; fixed by `UPDATE trello.trello_boards`, as FB, CL) | Cosmetic | **Missing.** SQL has 0 UPDATE, though §11 says bumped. LLC passed without it. Add it: one line |
| Trello | `badges_json` matches content (803/803 base) | Check C | OK, LLC's shape, description true |
| Trello | Action `data_json` keeps `list` (JB lesson); `_id` omitted (JD r7, advisory) | Shape | OK, LLC's shape |
| Trello | idShort NULL or url `None-…` (WD A2) | Advisory | OK, 456 and a real slug |
| Trello | List | - | **Doc drift**: §11 and §13 say Backlog, builder uses To Do. To Do is what LLC passed with, so fix the doc |
| GCal | One copy per attendee, `self` on the owner only, shared `@hg4` uid | Check C | OK |
| GCal | `transparency` opaque (JB A7) | Advisory | OK |
| GCal | `hangout_link` base form has `?hs=224` | Format | OK, seen on 8 of 8 sampled base rows |
| Contacts | 24-hex `contact_id` | New | **Fix** (A4) |
| Contacts | Placeholder first name, empty last (VIN, 5 reports) | Advisory | Not used, real name. Helper row isn't built |
| Contacts | `is_user` | Format | OK. Builder sets false; base Oliver Brooks (`/contacts/157`, company address) is false too |
| UPDATE companions | Every derived field after an append (learnings 18; base_check) | Check C | None needed: all seeds are new roots, except the board row above |

## 5. Line-by-line walk of the planned wording

Only lines that would repeat a past failure. All other lines passed the walk.

| ID | Line | Repeats | Smallest change |
|---|---|---|---|
| W1 | **Ask 2** "I put everyone the bank shows into the Payee history project" and **project_desc** "One issue per payee the bank shows" | Learnings 23 (WD F3). The 22 are the Processed-notice payees, not everyone the bank shows: Gusto is paid from the bank too, and the method itself excludes it | "everyone on the SVB notices"; "One issue per payee on the SVB notices" |
| W2 | **project_desc** "for the angel note and for Sunset's file" | Learnings 63, U8. No truth value; invites a Sunset deliverable | Drop "and for Sunset's file" |
| W3 | **Method** "close each payee's issue once its line is right" | WD `1_prompt.md` #2, LLC r1 F3. Done or Canceled for JPMorgan's zero line is a write fork | "move each payee's issue to Done once its line is right" |
| W4 | **Trello desc** "pull the salary and art lines from the P&L and round them" | NB-2 (9 FAILs), WD P4 (6 reports at Minor), sw2 T1 (the plan isn't how the quick numbers were made). Puts the P&L on the path | "quick plan: add up the notices by date and round them. fine for a first pass". Matches the sheet's quick pass. T9 keeps its shape; its "wrong reading" text needs updating |
| W5 | **Method** "lifetime revenue from the warehouse's daily revenue table, as recorded" | WD `(6)` L410. Same kind of rule over a Quantitative conflict: 12,354.99 vs P&L 9,859.36 vs ledger 9,693.55 | No wording change. It can't be removed, it's half the ask. Don't add "gross": the `total_revenue_usd` comment doesn't say so, and sc2's "gross" is an inference. LLC used this table and passed (January only). WD `(6)` turned on "two cash records the task reads", so W4 is the real mitigation. Residual risk stays: `(4)` rejected this class, `(6)` confirmed it. Keep NB-26 off the rubric |
| W6 | **Statement** "Nothing else is open on our side." | Learnings 63. Feeds no answer, and base #leapblock 1770842824.806309 leaves Martin's notice open ("we are still paying him to this day") | Delete the sentence. Also consider dropping "as we said yesterday": Feb 12 was a voice call, so no base text supports it |
| W7 | **Oleg ENG-2459 note** "video editor, ad videos" | FB r1 #9. For Robert the method settles $125: nobody "said the money came back", and sw1 F1 accepts "re-sent" as not saying so. But Leonard's mailbox holds a Wire Returned, so the key contradicts a real record. Robert posted in #video_editing_oleg in May 2024, so he reads the "re-sent" line | Either keep this row off the rubric, as §1a plans, and accept the exposure; or add to Leonard's note that the first wire bounced, which gives 0 with a reason and matches the hidden record. The second changes truth, surface and the T-list, and adds a Marketing-only trap |
| W8 | **Cohort** JPMorgan bucket "Not a cost" | VIN `(2)`. Method defines three buckets only | Add nothing to the method; keep the Bucket cell ungraded for this row |
| W9 | **Contact** `cnt_df6a482c50c0` | A4 | 24-hex id |
| W10 | **Gmail ids** Arthur, invite | Format row above | Re-mint so id >> 20 = `internal_date` |
| W11 | **Design §2** ENG-2450 "Correct total 4,000.00", DD 4,000.00 | Learnings 39 (stale truth). sw1 and the sketch total use 0 | Set to 0.00 |

Open, not wording: Drive PDFs 0000000029, 32, 33 should total $33,290 and remain unread (§11). Reviewers do open bytes: WD (6) F1 decoded an xlsx. Row floor: 77 INSERT vs 120. Mail copies won't close it, so the notes must, and that is the C1 class.

Checked, no change: ask ("tuesday"; "these people" has no antecedent in message one, a realism nit only), sheet header and row, deck lines, hold, Arthur's mail (past tense, "going through", ties to notices), bet calendar, off-bank sentence, 21 issue titles.

## 6. Past findings the local tools do NOT catch

`sql_lint`, `base_check`, `base_claims` and `hg.py lint` prove ids, references, dates, thread counters, badges, sharing and closed-record activity. By hand:

1. Seeded prose vs base facts: C1, P1, all of WD F1-F2, Dailybot, Vercel, Layer, 1.3.24. `base_claims` reads git branches only.
2. Text-vs-event chronology inside prose: C2. Tools compare timestamps, not what the words rely on.
3. Weekday/date pairs in body text: C6.
4. Doc `style_runs_json`: no tool reads it. JB F2 passed every local gate.
5. Snippet vs body, `size_estimate`, `web_view_link`, `content_path`, `shared_roles_json`, labels.
6. `contact_id` format: only collisions are checked. Thread id vs `internal_date`: no check found.
7. Rule vs worked example: C3.
8. Named artifact missing, when the name is a Drive file or branch: C4.
9. Token strings resolving to nobody: A1. No tool reads `[PERSON_NAME_…]`.
10. Known-issue cards: no tool loads NB-*, though base_check has a hazard index.
11. Quantitative base conflicts, UGT forks, close-state forks, completeness claims, clauses with no truth value, Business Function, dataset similarity: `ugt-fork-v1` and `base-data-v1` aren't in the local bundle (learnings 64).
12. Records hidden from the persona that contradict a key: P5.
