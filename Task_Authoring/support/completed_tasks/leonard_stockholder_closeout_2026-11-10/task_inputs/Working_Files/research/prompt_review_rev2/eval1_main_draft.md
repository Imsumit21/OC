# Eval 1 (/prompt) main reviewer draft: Leonard Hayes stockholder close-out

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Prompt sha256 45766344a3e4 · SQL sha256 78af8ace66a9 · reviewer: Opus 5.5 main session (Eval 1 + deep_recheck main stage)
Status: DRAFT. Phases 0 to 4 and the deep-recheck main-stage record are done. Deep-recheck steps 2 to 5 (merging the P1 to P4 findings and the Eval 0 result) are still pending, so the verdict below is provisional.

Evidence method: base universe read only through `Task_Authoring/tools/hg.py search` (normal universe, hg4-2026-08-31 v37). SQL read as text and never run. Persona visibility applied by hand from `acl.md` (Gmail, Slack, GCal and the Drive family are scoped; Linear, Trello, Contacts, Snowflake, Confluence and GitHub are unscoped).

---

## 1. Intake and asks inventory

| Field | Value | Source |
|---|---|---|
| Persona | Leonard Hayes, Co-founder & Creative Director, leonard.hayes@harmonygames.co | 00_Task_Assigned_Inputs.md; roster.json exact match (persona_key leonard_hayes) |
| Business function | Executive | 00_Task_Assigned_Inputs.md |
| Competency | Finance | same |
| Task skill | Authoring | same |
| Horizon | Long Horizon (long-horizon) | same |
| Difficulty mode | medium (not scored here) | same |
| Injection | Yes, 01_Universe_Inject.sql (130 INSERT, 15 UPDATE) | RULES.md |

The prompt has 5 sentences and about 140 words. Asks, and the incorporated sources that govern each one:

| # | Ask (prompt words) | Governing persona-visible source | Write |
|---|---|---|---|
| A1 | "the holder sheet ... in my close-out folder" | Notes doc `f_a37b403d5200d4f0a31d31` ("One row per issue on the sheet, and the counts go by rows ... The three of us get no row, only the totals"; labels list); Sunset mail `<mlkq74xd...>` (Feb 13: "One line per holder ... what each holds today (for options, what's vested) and any last day / Total shares and options outstanding / A count of holders by what each still needs to hear from you / Directors in office, and who holds the preferred vote"); #winddown thread replies `4f54dff9...`, `0e3d2253...` ("Mark those lines Covered on the sheet in place of a label") | GSheets create/write in folder `d_601064334a0b493022fe83`; share with Robert and Arthur (`846c625f...`: "the sheet goes to you as well as Robert") |
| A2 | "the investor letter in my close-out folder ... worked up from my investor email draft in #winddown" | #winddown `22f31c82...` (Feb 9 draft "Hi everyone, I'm writing to share a difficult update"); notes ("bring it up to date as a letter I can send. the update outline has the sections"); slides `f_75dddccabb26eeea4842c8` (5 section slides) | GDocs create in folder; share with Robert |
| A3 | "the messages to holders as drafts in my Gmail" | Notes: told/owed rules, "At most one note per person", "Each note says what they hold", unanswered holding questions, "Messages go to the email on each holder's issue"; #winddown `4f54dff9...` family rule | gmail_create_draft x N |
| A4 | "the Linear issues" | Linear project `ec2ea957...` "Holder records" description: "Canceled where the line holds nothing; otherwise Todo where its own note is waiting for me, and Done where it isn't. On every issue with no note of its own, Canceled included, say why." | linear_update_issue + linear_create_comment on ENG-2438 to ENG-2463 (26) |
| A5 | "the heads-up to Griffin" | Notes: "reply to all on their own Board position mail from Feb 12, asking for their vote as preferred holders on the dissolution. That one can go out once the sheet is done" | gmail_reply_to_message reply_all on `<BYAPR02MB4358...>` (send) |
| A6 | "the reply in #winddown" | Notes: "when the sheet is ready, reply under my list in #winddown and say who goes first"; "Whoever's last day comes first goes first" | slack_send_message thread_ts 1770934638.035469 (send) |
| A7 | "an answer to KPMG's audit request for Griffin from yesterday" | KPMG mail `<LV3PR19MB8524F1C0...>` (Feb 13 16:48Z, items 1 to 4, "reply to all"); KPMG clarification `<LV3PR19MB85246D2E...>` ("a line terminated on or before the as-of date counts only what had vested by its termination date"; "whether the company is winding down"); Linear project ("Send KPMG's confirmation as a reply to all once the sheet is done") | gmail_reply_to_message reply_all (send) |
| A8 | "Send the replies yourself ... only the holder messages wait for me" | Prompt | act/defer split |

Cohort: 26 Linear issues ENG-2438 to ENG-2463 (SQL lines 135 to 290). They map one to one onto the Carta lines that Leonard can see: SSP-01 to SSP-12 (seed certificates in Carta digests, for example `1774928765255297348`: "Philip Sanderson accepted certificate SSP-01 issued to GRIFFIN GAMING PARTNERS II, L.P.") and ES-1 to ES-18 option grants (14 option-only issues plus 4 advisor lines that sit on seed holders' issues).

---

## 2. Injection gate

- State: local procedure. `hg_injection_gate.py` was not run (the Evals store is write-blocked). Eval 0 is running in parallel on SQL 78af8ace66a9.
- Eval 0 verdict: PENDING (merged at steps 2 to 5).
- My own static checks on the records this task touches are in section 5 below.

---

## 3. Dimension scores (provisional, before the P1 to P4 merge)

| Dimension | Sub-dimension | Score | Justification (evidence) |
|---|---|---|---|
| Prompt | Unique Ground Truth | **1 (FAIL, provisional)** | Fork F1 is open: no Carta record Leonard can see gives the amount or vesting of advisor option lines ES-8 to ES-11, which feed the sheet holdings, the note contents and KPMG item 2/3 totals. Fork F2 is open: the Series Seed total is 3,051,879, 3,051,882 or 3,051,881, and the "ledger" that the injected Slack reply says to follow is not an identifiable record. See section 4. |
| Prompt | Feasibility | 5, at risk | Every write is supported by the catalog (`gsheets_create_spreadsheet`, `gdrive_move_file`, `gdrive_share_file`, `gdocs_create_document`, `gmail_create_draft`, `gmail_reply_to_message` reply_all, `slack_send_message` thread_ts, `linear_update_issue` state, `linear_create_comment`). Risk: the advisor-line vested amounts (F1) are not explicitly derivable, because the vesting commencement is not stated (Jun 7 2023 mail in `1767980387254277674` /messages/50 says only "vesting over 2 years"). If P2 confirms the gap, numeric observability fails as well. |
| Prompt | Persona ACL Reachability | 5 | Every required scoped record is owned by Leonard or visible to him: the notes doc, slides, draft sheet and folder have owner leonard.hayes; the Board position, KPMG, Sunset and Carta mails are in Leonard's mailbox; #winddown `C0ADGSZKR3R` and #executives `C07C2866011` both list EMPLOYEE_0038 (Leonard) as a member; Task List.xlsx `f_31115ddb6ed866f2b10d60` is shared with Leonard. Linear and Trello are unscoped. |
| Prompt | Explicit Tool Mention | 5 | No tool, parameter or MCP name. "Linear", "Gmail" and "#winddown" are natural service references. |
| Prompt | Clarity & Specificity | 5 | Act versus defer is explicit: holder notes are drafts; the replies (A5, A6, A7) are sent. The Griffin heads-up is settled as a send by the notes ("That one can go out once the sheet is done"), and the prompt lists it apart from "the messages to holders". No first-person "I'll [verb]" delegation conflict. |
| Prompt | Contrived / Unnatural | 5, watch | No headings, bullets, polished connectives, opaque IDs, timestamps, trap hints or if-chains. One soft flag: sentence 3 lists seven deliverables ("That's the holder sheet and the investor letter ..., the messages to holders ..., the Linear issues, the heads-up to Griffin, the reply in #winddown and an answer to KPMG's ..."). It names outputs, not their contents, so there is 1 spec-register trigger at most (fewer than 2). Not escalated. |
| Prompt | Alignment with Today's Date | 5 | "yesterday" is Feb 13, and the KPMG mail is dated 2026-02-13T16:48:33Z. "as we wind down" fits the Feb 11 shutdown. The notes' "by Tuesday" is Feb 17, matching GCal `evt_6f1a2c9e4b7d3a58c0e1d2` 2026-02-17T17:00Z. Last days that matter (Calvin Feb 20, [PERSON_NAME_0051] Feb 21) fall after the clock. |
| Prompt | Originality | N/A | No samples supplied. |
| Prompt | Truthfulness | 5 | Every tight and loose claim was verified; see section 6. |
| Prompt | Tool Use & Cross-service | 5 | Gmail changes the holdings (Carta termination notices and Calvin's extension in `1856121753612004097`) and the told status. Slack changes the "Covered" label, the family rule and the Arthur share. Linear holds the cohort and states. Drive holds the notes and outline. Trello `698e5a10...` sets the order. |
| Prompt | Investigation + Action | 5 | Every write depends on reading Carta, the told mail and the rules. |
| Prompt | Coherence (Bolt-on) | 5 | The KPMG answer depends on the same holder data and is gated by the Linear project ("once the sheet is done"). The letter is part of the same close-out. No sentence is removable without losing a required output. |
| Prompt | Persona | 5 | Leonard acts as co-founder, board director and Carta admin in the base data (#winddown `e3e198cc`: "Carta terminations"; Board position reply). A stockholder close-out fits that role. |
| Prompt | Business Function | 5 | Executive: board, investor and stockholder wind-down work. |
| Prompt | Assigned Competency | 5, at risk | Finance: cap-table reconciliation (Carta against the stale Nov 2024 list), vested-option holdings, totals of shares and options, and an auditor's equity confirmation (KPMG items 1 to 3). Corporate Ops pieces (board vote, legal intake) are present but secondary. A defensible match. |
| Prompt | Assigned Task Skill | 5 | Authoring: the investor letter, the holder notes, the sheet and three replies. |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions are load-bearing. Ambiguity: the rules live in the notes. Dynamic Change: the notes "replace my earlier outreach notes" (`f_762c6083...` said "one email to everyone ... take the names and numbers from the Nov 2024 owner list"); the Feb 13 02:21Z Slack replies refine the notes; Carta's Jan 23 2026 extension supersedes Calvin's Oct 29 2025 termination notice. Multi-Source spans 3 or more services. The prompt stays a short trigger. |
| Universe | Data Exists | 5, at risk | Same gap as F1: the ES-8 to ES-11 amounts exist only as 2023 planning values (Due Diligence Disclosures `f_6a37227593d0977fdbdd7a`: Collins "1% / 61,038 shares", others 30,518 / 6,104 / 6,104) plus arithmetic on the stale Nov 2024 list, not as a Carta record. |
| Universe | Cross-Service Coherence | 5, provisional | No fail-level inconsistency found in the records the task touches. One base known issue is routed around (NB-22). Designed conflicts are noted. Eval 0 not yet merged. See section 5. |

Lowest so far: Unique Ground Truth 1 (provisional FAIL, F1 and F2).

---

## 4. Unique Ground Truth: two-reading table and fork list

### Two-reading guardrail (strongest alternative, on the decisive outcome)

| Candidate | Prompt/source authority | Material actions and outputs | Resolved? |
|---|---|---|---|
| Reading A (best-supported) | Notes: "Carta is the record ... Each note says what they hold"; Carta digest `1782897835407336831` ("Arthur Blake signed option grant ES-9 ... for Husnu Matthew Collins ... ES-11 ... for PERSON_3941_NAME"); Due Diligence Disclosures `f_6a37227593d0977fdbdd7a` (Collins 61,038, [PERSON_NAME_6201] 30,518, two at 6,104); Nov 2024 owner list (Collins 86,470 = 25,432 + 61,038; [PERSON_NAME_0089] [PERSON_NAME_25152] 81,383 = 50,865 + 30,518; PERSON_3941 and PERSON_1287 31,536 = 25,432 + 6,104) | Sheet rows ENG-2440/2446/2447/2449 split seed shares from fully vested advisor options; their notes state both; KPMG item 2 includes the four advisor lines (103,764) in the option total; item 3 = common + seed + outstanding options | Not settled by a Carta record |
| Reading B (strongest alternative) | Same notes ("Carta is the record"); no visible Carta record gives an ES-8 to ES-11 amount or vesting; the Nov 2024 list is the only per-holder count, and the notes and the draft sheet flag it as unreliable ("the list's percentages leave out the option pool") | Sheet and notes either give the combined Nov 2024 figure as shares, or list the advisor option lines as amount unconfirmed; KPMG item 2 omits or flags those lines, so the item 2 and item 3 totals differ by 103,764 | Open: no persona-visible record rules out B |

Five checks on the F1 difference. (1) Newer source: the Jul 10 2023 disclosure (1%) is newer than the Jun 7 2023 mail ("0.5% each") but is a plan ("intends to enter into advisory agreements"), not a Carta grant. (2) Authority: the notes make Carta the record, and no Carta record has the amounts. (3) Source identity: the planning documents are not Carta. (4) Scope: Calvin's extension settles only Calvin. (5) Same material result: no. The sheet cells, note contents and KPMG totals differ.

### Fork list (every fork found by the main stage)

- **F1: advisor option lines ES-8 to ES-11 (OPEN).** Covers the sheet holdings and totals, notes for ENG-2440/2446/2447/2449, and KPMG items 2 and 3. Reading A derives seed 25,432/50,865 + options 61,038/30,518/6,104/6,104, fully vested (2-year vest from Nov 2023 grants). Reading B reports the amounts as not on Carta, or uses the combined Nov 2024 count. Missing: a dated, Leonard-visible Carta record (grant notice, holdings email or ledger) giving each advisor line's granted and vested amount.
- **F2: Series Seed Preferred total and "the ledger" (OPEN, possibly settleable).** Covers KPMG item 1 (class totals) and item 3 (the one combined figure). Values on Leonard-visible records: 3,051,881 (#executives `b658ec71...`, ChatGPT paste: "6,000,000 common + 3,051,881 Seed"), 3,051,882 (corrected cap table `1770717887098657139`: "Series Seed Investor 3,051,882"), and 3,051,879 (Leonard, Aug 2023, `1773160052067710033` /messages/10: "don't perfectly add up to what we have at disclosure schedule (3,051,882 vs 3,051,879)"). The injected reply `846a70ba...` says "chatgpt has the other seed investors a couple of shares off in these, go by the ledger", which rules out 3,051,881 but names no findable record. A per-holder sum (Griffin 2,662,255 + 84,438, then 2 × 50,865 + 8 × 25,432) gives 3,051,879, so other seed = 305,186, which is 2 shares off ChatGPT's 305,188. That fits "a couple", but it depends on the F1 split. Not BOTH_FAIR_FIGURE: two reported figures move (items 1 and 3) and the prompt-incorporated pointer ("go by the ledger") ranks a source that cannot be found. Missing: the ledger record, or a prompt or notes sentence naming the source of the seed total.
- **F3: Matthew Collins "told"? (likely settled, verify).** Leonard's Feb 12 22:52Z mail `<CAPBs_aLeDrd...>` went to "Akin <PERSON_8862_EMAIL>" ("Harmony is shutting down ... Thank you for everything, on the board and since"). The issue email for ENG-2447 is matthew.collins@harmonygames.co. The link between the two: in thread `1765973868202226140`, Leonard replies "Akin, thank you for the introduction" to an intro signed "best, Matthew Collins"; the contact `db57e559` is updated to "Investor and advisor (left the board May 2025)". If accepted, Collins is "Already told" (Done), not "Closing" (Todo + note). P1 must confirm the intro signature is in Leonard's copy. Otherwise this is an open fork that changes a label, a note and a Linear state.
- **F4: Calvin Price's last day (SETTLED).** The Oct 29 2025 Carta notice `1847333347700620793` says "Last day to exercise Jan. 24, 2026", so the line would have lapsed. The newer Carta update forwarded Feb 3 `1856121753612004097` says "Last day to exercise Feb. 20, 2026 (previously Jan. 24, 2026)". The newer Carta record wins. Calvin holds 4,408 and goes first (Feb 20, ahead of [PERSON_NAME_0051] Feb 21 in `1856960478782792748`).
- **F5: Griffin funds told? (SETTLED).** Leonard's Feb 12 reply `<CAPBs_a5B01Fz...>` to PERSON_4337 ("We signed up with [ORGANIZATION_2601] Inc. to properly wind down the operations") is a written closing message sent straight to the fund's partner, so both Griffin lines are "Already told". The heads-up (A5) is a separate send.
- **F6: family rule scope (UNVERIFIED by the main stage).** `4f54dff9...`: "one note to whoever has always handled it for a family covers the rest of the family's lines". Which lines form a family and who the handler is need a record. Leads: the angel threads `1799418746420547240` and `1781310711617833275` contain PERSON_3063, PERSON_2275, PERSON_0693, PERSON_2260 and PERSON_1287 together; the Linear comments on ENG-2441/2445/2449 all say "Last mail with that address before Feb: May 18, 2024". Whatever P1 finds settles this; until then it is an open candidate.
- **F7: letter "Holders" section source (SETTLED).** The outline slide `slide_fdc349f96a2c` says "Holders, per the Nov 2024 owner list". The newer notes say "These replace my earlier outreach notes" and "Carta is the record", and the outline is incorporated only for "the sections". So the letter uses Carta.
- **F8: letter sharing (SETTLED).** The notes say "Share it and the letter with Robert"; Slack `846c625f...` says "the sheet goes to you as well as Robert, the rest of my notes stands". The sheet goes to Robert and Arthur, the letter to Robert only.
- **F9: holder sheet, new file or the existing "Holder list (draft)" `f_5ecaa967...` (same material result).** Both land in the close-out folder with the same required contents. Note only.
- **F10: letter "bring it up to date" (acceptance-boundary risk).** The sections are fixed by the outline. Current facts are on records: the team let go, the Sunset wind-down and data agreements signed Feb 12 (`b6ad548e`), the board now Leonard and Robert (Robert Feb 12 22:38Z: "That leaves Leonard and me on the board"). "Distributions, tax papers" has no settled figures. The rubric must not lock content beyond the sections and the dated facts.

Every other fork was resolved by a cited record: the labels ("Covered" from the Slack reply), the order (Trello `698e5a10...` "Nothing goes out until the sheet is done", with the comment "nothing changes on order"), the KPMG cutoff ("on or before the as-of date", so the Dec 31 terminations of [PERSON_NAME_0043], Claire Morgan and [PERSON_NAME_2769] [PERSON_NAME_0093] count vested only), and the reply-all recipients (KPMG To PERSON_3088, Cc PERSON_4416, PERSON_2322, PERSON_2847; Board position To PERSON_4337, Cc PERSON_2847).

---

## 5. Cross-Service Coherence (records the task touches)

| Record / group | Check | Result |
|---|---|---|
| Linear ENG-2438 to ENG-2463 | Base max is ENG-2437 (`/issues/2377`, created 2025-11-07); 26 new ids with no collision (lookup over 3,852 issues). Creator `usr_63fffeb4fab5233e` = leonard.hayes (`/users/13`). States "Backlog" match Slack `a8540bc3` "They stay in Backlog until the sheet is done". Issue count 26 = 12 seed certificates (SSP-01 to 12) + 14 option-only grants. | PASS |
| Linear project "Holder records" in team_ENG | Project on the Engineering team (no exec team in Linear). Created 23:24Z, after Slack `d281112d` "Putting the holders in linear" (23:15Z). | PASS (team placement noted, not a misdescription) |
| Linear comments | Base Linear has zero comments (NB-24); the injected comments are new. They give leads only ("Nov 2024 owner list: N", "Last mail ..."). They match the Nov 2024 list values. | PASS |
| Slack #winddown thread on `e3e198cc` | Authors EMPLOYEE_0038 (Leonard) and EMPLOYEE_0025 (Arthur) are both in `C0ADGSZKR3R` members. Parent update reply_count 4, reply_users_count 2, latest_reply 1770949437.902269 all consistent. | PASS |
| Slack #executives reply `846a70ba` | Author EMPLOYEE_0038 is a member of `C07C2866011`. Parent `b658ec71` updated to reply_count 1. | PASS |
| Drive close-out folder `d_601064334a0b493022fe83` | Created 2026-02-12T23:20Z, but holds the draft sheet and slides created 2026-02-10 (moved in later; plausible). Parent is Leonard's root `d_63fffeb4...` (`/drive_files/9034`). | PASS (note) |
| Notes doc and outreach notes | style_runs end 2046 and 290 equal the body lengths. Notes created 01:05Z Feb 13, after the outreach notes (Feb 10); it states "These replace my earlier outreach notes". | PASS |
| Nov 2024 LNI mail UPDATE (Leonard and Arthur copies) | Diff against base: the only change removes "(Total ownership percentage adds to 100%)". The percentages sum to about 94.1%, so the removal fixes a false base claim and agrees with the draft sheet note "only add to about 94%". The Arthur copy keeps its own base token "[PERSON_NAME_0949]" where Leonard's copy has "Matthews" (base anonymization; Arthur's mailbox is not Leonard-visible). | PASS |
| Board position thread | Robert's Feb 12 22:38Z reply was added to all three mailboxes with matching Message-ID and In-Reply-To `<CAPBs_a5B01Fz...>` (Leonard's base reply, 22:14:52Z). Times are in order. | PASS |
| Bounce `<698ce305...>` in thread `1856860994291529096` | In-Reply-To matches Leonard's 2026-02-11 12:13:48 PST letter to PERSON_3140_EMAIL; the bounce at 12:13:57 PST comes after it. The X-Failed-Recipients address matches ENG-2457's email. | PASS |
| Contractor letter dates against Carta | The PERSON_3140 letter says "effective January 31, 2025". This is base known issue NB-22, routed around by the notes' "Carta is the record, over any date in the letters" (and the letter bounced). The other letters say Jan 31 2026 while Carta says Jan 30 2026; that conflict is designed and settled by the same rule. | PLATFORM/known (NB-22); not scored |
| Calvin Carta notices | The Oct 29 2025 notice (Jan 24) and the Jan 23 2026 update (Feb 20, "previously Jan. 24, 2026") agree on 8,138 granted, 4,408 vested and termination Oct 24 2025. | PASS |
| KPMG thread | Message order: 16:48Z request, then Leonard 17:12Z "before the 27th", then KPMG 17:37Z clarification. Headers and threading are consistent. | PASS |
| Trello card #456 | shortLink and shortUrl are NULL, matching the base format (for example card 173 has `shortLink: None`). Board dateLastActivity updated to the comment time. badges.comments = 1, matching 1 commentCard. | PASS |
| Contacts | Inserted PERSON_0693 and PERSON_2275 rows use the base token format (`first_name: "PERSON_1287", last_name: ""`). The Collins job update is consistent with the board history (Robert Feb 12: "Leonard and me on the board"). Whether the created_at/updated_at columns exist is left to Eval 0 (not shown in the export). | PASS / Eval 0 |
| Hidden-record check (P2 rule) | No required record is in another user's mailbox. The Carta amounts for ES-8 to ES-11 are missing outright, not hidden (see F1). | F1 cross-ref |
| Apostrophes in SQL strings | Spot-checked the injected text strings (for example `that''s`, `family''s`, `I''ll`, `don''t`): doubled. | PASS (Eval 0 owns the full audit) |

Coherence provisional score: 5. It would become 3 if Eval 0 confirms one minor id or format item on a record the answer reads, and 1 if it confirms a lifecycle or sum item.

---

## 6. Truthfulness (premises and identifiers in the prompt)

| Claim | Record | Result |
|---|---|---|
| "everyone who holds our stock or options" / "as we wind down" | #winddown Feb 9 to 12 shutdown messages; the Linear cohort | True |
| "I set it up in the holder project in Linear" | Project "Holder records" `ec2ea957...`, lead and creator `usr_63fffeb4fab5233e` = leonard.hayes | True ("holder project" is a fair loose descriptor) |
| "my close-out notes doc has how each holder gets handled and what still needs doing" | Doc "Stockholder close-out notes", owner Leonard, sections "What needs doing" / "How each holder gets handled" | True |
| "my close-out folder" | Folder "Stockholder close-out", owner Leonard | True |
| "my investor email draft in #winddown" | `22f31c82...` (Feb 9 19:18Z, Leonard) | True |
| "Griffin" | GRIFFIN GAMING PARTNERS II and II SIDE FUND (ENG-2438/2439; SPA SOP `1771880236343640719`) | True |
| "KPMG's audit request for Griffin from yesterday" | `<LV3PR19MB8524F1C0...>` 2026-02-13T16:48:33Z, subject "GRIFFIN GAMING PARTNERS 2025 Audit Request ..." | True |
| "I'm behind on it" | GCal "Holder notes due" Feb 17; Trello card in To Do | Consistent |

No phantom identifiers and no contradicted premise (no work assumes the company runs normally; no departed person acts). Truthfulness 5.

---

## 7. Wording dimensions (P4 scope, main-stage view)

- Search hits: none of `linear_`, `gmail_`, `slack_`, "MCP", "tool", "First", "Then", "Finally".
- Command list: none. The prompt sets no order (the order lives in Trello and the notes).
- Pre-solving: the prompt names no cause, no stale source and no holder.
- Trap hint or riddle: none. "the way those lay it out" points to the notes, not to a trap.
- Hidden destination: none. Every output has a named place (close-out folder, Gmail drafts, Linear issues, "the heads-up to Griffin" defined in the notes, "the reply in #winddown", the KPMG reply).
- Audit-form or if-chain wording: none.
- Staged errors: none.
- Soft flag: the sentence 3 deliverables list (see Contrived above).

---

## 8. Deep recheck: main-stage record (step 1)

Passes P1 to P4 and Eval 0 are running blind in parallel. Main-stage record, to be merged at steps 2 to 5:
- UGT forks: F1 OPEN, F2 OPEN (possibly settleable), F3 needs verification, F6 unverified; F4, F5, F7 and F8 settled with the quotes above; F9 same result; F10 a boundary note.
- other_failures: none yet. Watch items: Feasibility and Data Exists numeric observability (F1), Competency (Finance against Corporate Ops), Contrived (sentence 3 list).
- Fix direction (to verify at step 5; no paste-ready wording yet): add a Leonard-visible Carta record for ES-8 to ES-11 (granted, vested, grant date) and for the seed certificates, or a ledger the injected "go by the ledger" can point to by name. Alternatively, have the notes say which source gives advisor-line and seed-class figures.

---

## 9. Verdict block (provisional; final after steps 2 to 5)

### FINAL VERDICT: FAIL (provisional)

Score: 1 (provisional)

Execution status: PARTIAL. Deep-recheck steps 2 to 5 and the Eval 0 merge are pending.

Evaluator model: Opus 5.5 (claude-opus-5-5), main session

Next action: Merge the P1 to P4 and Eval 0 findings. Confirm or reject F1, F2, F3 and F6 against quoted Leonard-visible records. Rescore.

Evidence limits: the family-rule census (F6) and the per-holder told census for all 26 issues were not finished by the main stage. Gmail and Slack attachment bytes are unreadable (per acl.md). The Arthur and Robert mailboxes are not visible to Leonard and were not used.

**Lowest Dimension:** Unique Ground Truth, 1. No persona-visible Carta record gives the ES-8 to ES-11 amounts or vesting (F1), and the seed total "ledger" cannot be identified (F2).

**Summary:** The prompt is short, natural and grounded. All premises are true, every write is supported, and the rules are seeded in the notes doc, the Slack replies and the Linear project. It fails provisionally on Unique Ground Truth: the advisor option lines and the seed-class total, which drive sheet cells, note contents and the KPMG totals, are not stated on any Carta record Leonard can open, so two defensible end states remain.
