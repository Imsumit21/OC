# PROMPT EVALUATION REPORT

- Review version: Eval 1 (prompt-source-checks-v2); release fields and binding hashes are in the verdict block.
- Attempt: 6aed9d01a1cb8067d8ac7dee (chat review)
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Injection SQL sha256: `bc72db9c31e9982751e47762f94939c7c5367ee7979830e28acb55627b957f2d`

### Task: Stockholder/option-holder close-out (holder sheet, investor letter, holder note drafts, Linear states, Griffin heads-up, #winddown reply, KPMG confirmation)
### Assigned Persona: Leonard Hayes - Co-founder & Creative Director (leonard.hayes@harmonygames.co)
### Assigned Business Function: Executive (maps to Founders / Exec / Strategy)
### Assigned Competency: Finance
### Assigned Task Skill: Authoring
### Assigned Horizon: long-horizon (difficulty mode: medium)

Source of all five fields: `Evals/task_inputs/00_Task_Assigned_Inputs.md` (platform record).

---

### Injection Gate
- State: CURRENT (hg_injection_gate.py)
- Reviewed SQL sha256: `bc72db9c…b957f2d`, review `injection-static-v2`, 2026-11-07T20:56Z. Eval 0 verdict: PASS.
- Eval 0 findings on records this prompt depends on: none. The advisory on four columns missing from the unverified schema snapshot (`gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` / `ordinal`, `linear.linear_projects.links_json`) stays an advisory (also re-raised by P3). It changes no graded value, but if the live database lacks a column the whole transaction rolls back, so dropping those four columns is the safe option.

### Dataset Similarity
- Library: refreshed 2026-11-08T06:36Z (about 3 h old), 495 tasks. Gate: PASS. Nearest tier: distinct.
- Nearest neighbours (all below 0.70): a completed Leonard Hayes / Finance close-out-pay task (meaning 0.685), a completed Corporate Ops shutdown-memo task (0.651), a completed Leonard Hayes / Finance close-out task (0.641). None is same-scenario or a duplicate. Task IDs are not shown in this portal.

---

### Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Leonard is the CEO/co-founder who announced the shutdown, ran Carta terminations (#winddown Feb 12 "Carta terminations are done") and promised the angels a one-by-one reach-out. He owns the notes doc, the folder and the Linear project. Role, voice and access fit.

**Assigned Competency (Finance):** PASS (5)
- Cap-table reconciliation (shares by class, per-fund split, outstanding option lines as of a date, vested amounts, totals), auditor confirmation for Griffin's fund audit and investor reporting are Finance work.

**Assigned Task Skill (Authoring):** PASS (5)
- The core is authoring: holder sheet, investor letter, per-holder notes, Griffin heads-up, KPMG confirmation and #winddown reply.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS (5)
- Ambiguity: the prompt points at the notes and the project, and the per-holder rules live in records.
- Dynamic Change:
  - "Holder outreach notes" (Feb 10: one BCC mail, use the Nov 2024 list) are replaced by the Feb 13 close-out notes.
  - The Linear "Last written contact I have before Feb" comments are overtaken by Feb messages: the Feb 9 DM, the Feb 11 termination letters and Robert's Feb 12 email.
  - The Nov 2024 owner-list figures are overtaken by the Carta last days and by the advisory option lines.
- Multi-Source: Gmail (Carta, KPMG, Sunset, letters), Slack (#winddown thread, DMs), Linear, Drive/Docs/Slides, Contacts.
- Data seeding: PASS. The rules are seeded in the notes doc, the project description and the #winddown thread replies.

**Naturalness:** PASS (5)
- First person, plain, no headings or bullets, no polished connectives, no staged errors. Soft flag (not scored): the fourth sentence lists seven deliverables that the notes and project already describe (see Recommended Improvements).

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS (no step order) |
| Bolt-On | PASS (KPMG ties to the project: "KPMG's confirmation goes back as a reply to all once the sheet is right") |
| Pre-Solving | PASS (no holder outcome, figure or trap is named) |
| Tool Mention | PASS (natural service names only) |

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every per-holder outcome and figure is settled by a persona-visible record under the incorporated notes rules; the strongest alternative (Nov 2024 figures as shares) is excluded by the notes rule that Carta is the record.

Alternative selection: Strongest alternative is the Carta-is-the-record reading the notes doc itself mandates.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Carta is the record: the four advisor-angels each hold Series Seed shares plus a Carta advisory option line (ES-8 to ES-11, sized in the Nov 2023 board consent: 30,518 / 61,038 / 6,104 / 6,104, 1/24 monthly, no cliff, so fully vested), alongside the 14 employee lines in the Carta termination emails. | Split each advisor-angel into seed shares and an outstanding, fully vested advisory option line; Nov 2024 per-person figures are shares plus options. | Holder sheet rows/totals, KPMG items 1-3 and holders' notes built on the Carta split. | Holder sheet in Stockholder close-out folder; KPMG reply-all; Gmail drafts. | PERSON\_3941 25,432 shares plus a 6,104 option line; KPMG option lines include the four advisory lines. | S\_NOTES\_CARTA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "Carta is the record."; S\_ES11 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1782897835407336831.json pointer /messages/0/body): "Arthur Blake signed  option grant ES-11"; S\_ES9 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1782897835407336831.json pointer /messages/0/body): "Arthur Blake signed  option grant<br>ES-9"; S\_ADVISORY (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1769504183607271852.json pointer /messages/7/body): "(1% for Matthew Collins, 0.5% for"; S\_ADV\_1287 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1776421620687714369.json pointer /messages/0/body): "advisory shares correspond to 0.10% of the pre-money" |
| B | Take the Nov 2024 owner list figures (repeated in the Linear comments) as share holdings and treat only the 14 Carta termination lines as options. | Advisor-angels hold only shares at their Nov 2024 figures. | Sheet rows/totals and KPMG items 1-3 built on Nov 2024 figures. | Holder sheet in Stockholder close-out folder; KPMG reply-all; Gmail drafts. | PERSON\_3941 31,536 shares, no option line; KPMG option lines exclude the advisory lines. | S\_LIN\_3941 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 158-158): "'Nov 2024 owner list: 31,536'"; S\_NOV24\_3941 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1816809274978043917.json pointer /messages/0/body): "PERSON\_3941\_NAME \[PERSON\_NAME\_0127\] – 31,536 shares" |

Explicit option inventory: The prompt lists deliverables, not alternative options.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "Send the replies yourself, no need to check with me; only the holder messages wait for me."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. The notes doc the prompt incorporates makes Carta the record, and Carta shows option grants ES-9 and ES-11 to the advisor-angels with no termination; the Nov 2024 list is a third-party summary that also counts the ES-17 option as shares, so it cannot override Carta.
Resolution evidence: S\_NOTES\_CARTA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "Carta is the record."; S\_ES11 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1782897835407336831.json pointer /messages/0/body): "Arthur Blake signed  option grant ES-11"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Share/option split differs. |
| writes | DIFFERENT | Sheet totals and KPMG figures differ. |
| destinations | SAME | Same sheet, reply and drafts. |
| contents | DIFFERENT | Holdings and option totals differ. |

Authority chain: P → S\_NOTES\_CARTA

Resolution relevance challenge: The Carta rule decides exactly this difference: which record defines holdings. The Nov 2024 list is not Carta.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; B is excluded.
Challenge evidence: S\_NOTES\_CARTA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "Carta is the record."

Decision sweep: The notes classify every holder line (label, note, Linear state).
Decision rule: S\_NOTES\_LABELS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "Labels for the sheet: Nothing, Already told, Closing, Last day, Closing and last day."; S\_PROJECT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 104-104): "Canceled where the line holds nothing; otherwise Todo where its own note is waiting for me, and Done where it isn''t."

| Item | Outcome | Basis | Settled by / gap |
|---|---|---|---|
| ENG-2438/2439 Griffin funds | Already told; Done with reason; partner gets heads-up reply | RECORD | S\_NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "for a fund, its partner"; S\_NOTES\_GRIFFIN (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "Griffin''s partner gets a heads-up as a reply on the Feb 12 Board position thread" |
| ENG-2440 \[PERSON\_NAME\_0089\] \[PERSON\_NAME\_25152\] | Already told (Feb 9 DM); Done with reason | RECORD | S\_DM\_0089 (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/D04UC0UEN2V/2026-02.json pointer /0/text): "The most reasonable thing to do right now is to shut down the company we decided."; S\_NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "Told means a written message about the closing, sent to them directly" |
| ENG-2441 Arthur PERSON\_3083 | Closing; own note; Todo | RECORD | S\_NOTES\_RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "the closing if they have not been told" |
| ENG-2442 \[PERSON\_NAME\_4468\] | Closing; own note; Todo | RECORD | S\_NOTES\_RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "the closing if they have not been told" |
| ENG-2443 \[PERSON\_NAME\_52949\] | Closing; family note; Todo | RECORD | S\_FAMILY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "one note to whoever has always handled it for a family covers the rest of the family''s lines" |
| ENG-2444/2445 Patrick Lewis, \[PERSON\_NAME\_27652\] | Covered; Done with reason | RECORD | S\_COVERED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Mark those lines Covered on the sheet in place of a label" |
| ENG-2446 PERSON\_3941 | Already told (Robert, Feb 12); Done with reason | RECORD | S\_ROBERT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 90-90): "Wanted you to hear this from me: we''re closing the company." |
| ENG-2447 \[PERSON\_NAME\_11362\] | Closing; own note stating shares and ES-9 line; Todo | RECORD | S\_ADVISORY (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1769504183607271852.json pointer /messages/7/body): "(1% for Matthew Collins, 0.5% for"; S\_NOTES\_RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "the closing if they have not been told" |
| ENG-2448 TOR Capital | Closing; note to partner; Todo | RECORD | S\_NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "for a fund, its partner" |
| ENG-2449 PERSON\_1287 | Closing; own note stating shares and advisory line; Todo | RECORD | S\_ADV\_1287 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1776421620687714369.json pointer /messages/0/body): "advisory shares correspond to 0.10% of the pre-money"; S\_NOTES\_RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "the closing if they have not been told" |
| ENG-2451/2452/2454/2455/2461/2462 lapsed grants | Nothing; Canceled with reason | RECORD | S\_NOTES\_CARTA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "If a line''s last day has passed, it holds nothing." |
| ENG-2450/2453/2456/2457/2458/2460 told grantees | Last day; own note; Todo | RECORD | S\_NOTES\_RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "their last day if they have one" |
| ENG-2459 \[PERSON\_NAME\_0051\] | Closing and last day (Feb 21, 2026); goes first | RECORD | S\_CARTA\_0051 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1856960478782792748.json pointer /messages/0/body): "Feb. 21, 2026"; S\_NOTES\_RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 15-15): "Whoever''s last day comes first goes first." |
| ENG-2463 \[PERSON\_NAME\_0022\] | Closing and last day (Apr 30, 2026) | RECORD | S\_CARTA\_0022 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/leonard@harmonygames.co\_1856960382677662910.json pointer /messages/0/body): "exercise April 30, 2026" |

Strongest-alternative challenge (B): Reading B follows the injected Linear comments and Nov 2024 list, the most natural easy path.
Challenge evidence: S\_LIN\_3941 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 158-158): "'Nov 2024 owner list: 31,536'"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

The strongest alternative (Nov 2024 per-person figures as plain shares, as the Linear comments and the draft sheet repeat) is excluded by the incorporated rule "Carta is the record". Carta shows option grants ES-9 (Matthew Collins) and ES-11 (PERSON_3941) with no termination. The Nov 2, 2023 board consent exhibit (Leonard's Gmail, thread …1782034095239486005, att_0001.pdf) sizes the four advisory lines: Segerstråle 30,518; Husnu Akin Babayigit 61,038; Deepak Gupta 6,104; Nebojsa Radovic 6,104, each "1/24th monthly/no cliff". They are fully vested by the clock, and the sums tie out exactly: 25,432 + 6,104 = 31,536; 25,432 + 61,038 = 86,470; 50,865 + 30,518 = 81,383. This is a real trap, not a fork.

Other P1 forks resolved (details in Deep Recheck):
- KPMG lines terminated Jan 30, 2026 count at full grant as of Dec 31, 2025 ("using each effective date as Carta shows it, regardless of when recorded"; the clarification covers only terminations effective on the as-of date).
- Matthew Collins left only the board ("very happy to join the board meetings etc going forward", May 1, 2025), and Carta has no ES-9 termination.
- "What we still need from Griffin" is in Leonard's Feb 11 Sunset call transcript (Docs, owned by Leonard): "will receive board and stockholder consents to formally approve the wind down".

**Feasibility:** PASS (5)

| Ask | Grounded sources | Discovery path | Catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Holder sheet in close-out folder, shared with Robert and Arthur | Notes doc; Sunset intake email; #winddown reply "the sheet goes to Arthur as well as Robert"; Carta termination emails; board consent exhibit; Nov 2024 list; Griffin 2024 confirmation PDF (2,662,255 / 84,438) | Project description → notes → Gmail/Slack | gsheets/gdrive create/update, gdrive move, gdrive share | Owned by Leonard / Leonard's mailbox | One row per Linear issue, labels incl. Covered, holdings, last days, notice route, totals, counts, directors, preferred vote |
| Investor letter in close-out folder, shared with Robert | #winddown draft (Feb 9); "February 26 Update" outline slides; current facts (Sunset engagement, data licence, IP) | Notes → Slack/Slides | gdocs create, gdrive move/share | Leonard member/owner | Updated letter following the outline sections |
| Holder note drafts in Gmail | Notes rules; family thread replies; told evidence (Feb 9 DM, Feb 11 letters, Robert Feb 12); unanswered questions (Claire mpim Feb 12) | Sheet → notes | gmail_create_draft | Leonard's mailbox | One draft per person still owed something |
| Linear issue states and comments | Project description; team_ENG states Canceled/Todo/Done | Linear | linear_update_issue, linear_create_comment | Unscoped | 26 issues set, with reasons where no own note |
| Griffin heads-up (sent) | Notes; Board position thread (Leonard copy, headers present); Sunset transcript | Gmail/Docs | gmail_reply_to_message | Leonard's mailbox | Reply on Feb 12 thread with what is still needed |
| #winddown reply (sent) | Notes "reply under my list"; list message e3e198cc | Slack | slack_send_message with thread_ts | Member | Thread reply naming who goes first ([PERSON_NAME_0051], Feb 21, 2026) |
| KPMG answer (sent, reply-all) | KPMG request and clarification (Feb 13), Carta, consent exhibit, 2024 confirmation | Gmail | gmail_reply_to_message reply_all | Leonard's mailbox | Items 1–4 as of Dec 31, 2025 |

- Dimensional and numeric observability: per-holder and per-fund values exist in readable email bodies and PDF attachments (Gmail attachments are readable per acl.md). The advisory vesting-start dates are "in Carta" (not visible), but no-cliff 24-month vesting from a 2023 grant is fully vested by both Dec 31, 2025 and the clock.
- No link or attachment is requested.

**Persona ACL Reachability:** PASS (5). Every required scoped read is in Leonard's mailbox, his Drive, or a Slack channel/DM he belongs to. Linear and Contacts are unscoped.

**Truthfulness:** PASS (5). All six premises verified (record premises PR1–PR6): the promised reach-out is still open; the "Holder records" project is led by Leonard; the notes doc has both sections; the "Stockholder close-out" folder exists; the Feb 9 investor draft is in #winddown; the KPMG request is dated 2026-02-13 ("yesterday"). No phantom identifiers. The shutdown premise is consistent.

**Tool Use & Cross-service:** PASS (5).
- Gmail changes graded facts: Carta last days, the told letters, the KPMG clarification.
- Slack changes graded facts: the family/Covered rule, Arthur's sharing, the told DM.
- Linear changes graded facts: the holder set.
- Drive changes graded facts: the folder and the outline.
- There are several writes.

**Investigation + Action:** PASS (5). Every write depends on the per-holder investigation.

**Clarity & Specificity:** PASS (5). Delegation is explicit: "Send the replies yourself … only the holder messages wait for me." The per-holder decisions are settled by records. Reply versus reply-all on the Board position thread reaches the same partner either way (see Recommended Improvements).

**Contrived / Unnatural:** PASS (5). No exact timestamps, opaque IDs, riddles or trap hints. No hidden destinations: the notes name the Griffin thread and "reply under my list", and KPMG asks for reply-all. No audit-form wording or if-chains.

**Alignment with Today's Date:** PASS (5). "yesterday" = Feb 13, 2026 (KPMG 16:48 UTC). The notes' "by Tuesday" = Feb 17 (calendar slot). Nothing after the clock is treated as done.

**Originality / Sample Similarity:** N/A (no comparison samples supplied).

---

### Phase 3: Universe Feasibility

**Data Existence:** all named entities verified (project, 26 issues, notes doc, folder, draft sheet, outline, #winddown draft and list, Board position thread, KPMG and Sunset threads, 14 Carta termination emails, Carta grant digests, board consent exhibit). All are retrievable through cataloged read tools.

**Cross-Service Coherence:** PASS (5)
- Inconsistencies in task-touched data: none scored.
  - The Feb 11 letters' "January 31, 2025/2026" versus Carta "Jan. 30, 2026" is a realistic source conflict that the incorporated rule resolves ("as Carta shows it, regardless of when recorded").
  - The Jan 24 versus Jan 28 last days follow different grant batches and change no outcome (both have passed).
- Known base-data issues (not scored): none. The task does not use Snowflake or Confluence.
- Injection SQL considered: yes. Static integrity reused from the CURRENT `injection-static-v2` PASS. Injected records match the base (Nov 2024 figures line for line, chronology before the clock).
- Platform defects (not scored): anonymized-token collisions (see Deep Recheck).

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Strongest alternative excluded by "Carta is the record"; every holder item settled by a record (comparison above) |
| Prompt | Feasibility | 5 | All reads and writes supported; the advisory sizes and vesting are derivable from a visible consent exhibit |
| Prompt | Persona ACL Reachability | 5 | All scoped reads are in Leonard's mailbox, Drive and channels |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Explicit delegation; no unsettled write divergence |
| Prompt | Contrived / Unnatural | 5 | Natural register; deliverable list is a soft flag only |
| Prompt | Alignment with Today's Date | 5 | Relative dates resolve |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | Six premises verified |
| Prompt | Tool Use & Cross-service | 5 | Gmail, Slack, Linear and Drive each change graded facts |
| Prompt | Investigation + Action | 5 | Investigation feeds every write |
| Prompt | Coherence (Bolt-on) | 5 | KPMG tied to the project |
| Prompt | Persona | 5 | CEO/co-founder owns the close-out |
| Prompt | Business Function | 5 | Executive maps to Founders / Exec / Strategy |
| Prompt | Assigned Competency | 5 | Finance |
| Prompt | Assigned Task Skill | 5 | Authoring |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions load-bearing; seeded rules |
| Universe | Data Exists | 5 | All entities verified and retrievable |
| Universe | Cross-Service Coherence | 5 | No scored inconsistency |

---

### Issues Found (if any):

None at fail or non-fail level.

### Recommended Improvements (if any):

1. **Advisory option lines (trap check, not a defect).** Runs that copy the Nov 2024 / Linear figures will report the four advisor-angels as plain shareholders. That is the trap. Keep the OEs and rubric on the Carta split: ES-8 30,518, ES-9 61,038, ES-10 6,104 and ES-11 6,104, fully vested and outstanding at Dec 31, 2025. The Jan 30, 2026 lines (Marcus 22,889; [PERSON_NAME_0068] 16,277; Martin 3,866; [PERSON_NAME_0022] 15,259) count at full grant for KPMG. The Dec 31, 2025 lines count at vested.
2. **[PERSON_NAME_4468]'s note address.** Two addresses appear: PERSON_0693_EMAIL (signature, plus your injected "Investor" contact) and patrick@harmonygames.co (the Jun 27, 2025 mail, which the anonymizer also gives to Patrick Lewis). This is a platform anonymization collision. Keep the rubric off the exact recipient address for ENG-2442, or accept either.
3. **Griffin heads-up recipients.** The notes say "as a reply". Don't let the rubric require or forbid reply-all (cc PERSON_2847, Robert, Arthur). Grade that it lands on the Feb 12 thread to the partner and asks for the board/stockholder consents to approve the wind down.
4. **Open authoring items.** Don't lock the investor letter's holder count or the exact KPMG item 4 event list. Grade within the sources: the outline sections and current facts for the letter, and the wind-down and dissolution engagement as significant events with no financing for KPMG item 4.
5. **Tightening (soft).** The fourth sentence restates deliverables the notes already list. It is acceptable now; trimming it would lower AI-text and "spec register" risk at QC.
6. **Schema advisory (from /injection).** Consider dropping the four snapshot-unknown columns so a live-schema mismatch cannot roll back the whole injection.

---

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 5 sentences, 12 required outcomes | 13 | 0 fail-level (all rejected or recorded as advisory/platform) |
| P2 | 5 sentences | 5 + 2 platform notes | 0 scored (platform/advisory) |
| P3 | 5 sentences | 2 | 0 scored (schema advisory) |
| P4 | 5 sentences | 1 | 0 scored (soft flag) |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR1/DR3 | P1 | "an answer to KPMG's audit request…" / notes "Carta is the record" | Carta digest …1782897835407336831 (ES-9, ES-11); advisory email …1769504183607271852 | §2 which number | UGT | REJECTED | Nov 2, 2023 board consent exhibit (…1782034095239486005 att_0001.pdf) sizes the advisory lines: "Husnu Akin Babayigit 61,038 1/24th monthly/no cliff", "Deepak Gupta 6,104", "Nebojsa Radovic 6,104", "Segerstråle 30,518". The sums tie to the Nov 2024 figures; "Carta is the record" excludes reading the list as plain shares |
| P1-DR2 | P1 | KPMG sentence | Carta "terminated … as of Jan. 30, 2026" | edge values | UGT | REJECTED | KPMG: "using each effective date as Carta shows it, regardless of when recorded"; the clarification covers only "a termination effective on the as-of date itself", so Jan 30 lines are outstanding in full at Dec 31 |
| P1-DR4 | P1 | notes "Told means…" | DM D04UC0UEN2V 2026-02-09 | event | UGT | REJECTED | The rule has no role qualifier: "a written message about the closing, sent to them directly, from one of the three of us". The DM meets every element |
| P1-DR5 / P2-DR1 | P1, P2 | "messages to holders as drafts" | …1773213846196143460 "via email: PERSON_0693_EMAIL"; …1836075678772806708 from patrick@harmonygames.co | recipient | UGT / coherence | PLATFORM:anonymized-token | patrick@harmonygames.co is also given to Patrick Lewis (…1770141224265557526): an anonymizer collision, not scored. Recommendation 2 |
| P1-DR6 | P1 | same | Nov 2024 list; Carta "Husnu Matthew Collins" | recipient | UGT | PLATFORM:anonymized-token | [PERSON_NAME_11362] joins to Matthew Collins by the exact sum 25,432 + 61,038 = 86,470; one address (matthew.collins@…) |
| P1-DR7 | P1 | "the heads-up to Griffin" | Sunset transcript (Docs, owned by Leonard) | contents | UGT | REJECTED | "will receive board and stockholder consents to formally approve the wind down" |
| P1-DR8 | P1 | same | Board position thread cc list | recipients | Clarity | REJECTED | Partner receives it either way; same write. Recommendation 3 |
| P1-DR9 | P1 | "the Linear issues" | project description | write | UGT | REJECTED | Notes separate holder notes ("I read and send each note myself") from the heads-up ("That one can go out once the sheet is right"), so Griffin has no note of its own; Done with reason |
| P1-DR10 | P1 | investor letter | slide "27 holders on the Nov 2024 owner list" | edge value | UGT | REJECTED | Open authoring; no required figure. Recommendation 4 |
| P1-DR11 | P1 | holder drafts | family thread reply | contents | UGT | REJECTED | Open note wording; "Each note says what they hold" is satisfied either way for Covered lines. Rubric guidance only |
| P1-DR12 | P1 | "the holder sheet … in my close-out folder" | "Holder list (draft)" | destination | Clarity | REJECTED | Same material result (a correct sheet in the folder) |
| P1-DR13 | P1 | KPMG sentence | KPMG item 4 | set | Clarity | REJECTED | Open content with an objective boundary. Recommendation 4 |
| P2-DR2 | P2 | "the way those lay it out" | DM partner PERSON_3335 | identity | coherence | PLATFORM:anonymized-token (partial) | The join is visible: the ENG-2440 comment "Jan 30, 2026, DM" matches the DM; "[PERSON_NAME_0089] [PERSON_NAME_25152] viewed … Advisor Agreement - Segerstråle"; [PERSON_NAME_6550] 0.5% = Segerstråle 30,518 |
| P2-DR3 | P2 | KPMG | 2024 cap-table xlsx not shipped | data exists | advisory | REJECTED | Not needed; values rebuild from visible records |
| P2-DR4 | P2 | holder drafts | TOR side letter notice tokens | notice route | platform | PLATFORM:anonymized-token | Not scored |
| P2-DR5 | P2 | notes Carta rule | Jan 28 vs Jan 24 last days | date | coherence | REJECTED | Different grant batches; both passed; no effect |
| P3-DR1/DR2 | P3 | prompt sentences 2 and 4 | SQL columns not in schema snapshot | injection | coherence | ADVISORY | Unverified snapshot; Eval 0 advisory; changes no graded value |
| P4-DR1 | P4 | sentence 4 deliverable list | notes/project | naturalness | soft flag | ADVISORY | 1 of 4 spec-register triggers at most; not a Contrived fail |

Effect on verdict: unchanged. No confirmed finding at fail or non-fail level. The rejection reasons above quote persona-visible records.

Fork list:
- F1: Advisor-angel holdings | A: seed shares + advisory option line (ES-8 30,518 / ES-9 61,038 / ES-10, ES-11 6,104 each, fully vested) | B: Nov 2024 figures as shares | Settled by: notes "Carta is the record." + Carta "option grant ES-9 … ES-11" + consent exhibit "1/24th monthly/no cliff"
- F2: KPMG Jan 30, 2026 lines at Dec 31, 2025 | A: full grant | B: vested only | Settled by: KPMG "using each effective date as Carta shows it, regardless of when recorded"
- F3: KPMG Dec 31, 2025 lines | A: vested only | B: full grant | Settled by: KPMG "a termination effective on the as-of date itself counts as of that date"
- F4: ES-12 effective date | A: Carta Jan. 30, 2026 | B: letter "January 31, 2025" | Settled by: "as Carta shows it"
- F5: Lines lapsed Jan 2026 (ES-3, 5, 16, 17) | A: in KPMG at Dec 31, 2025 vested; Nothing on the sheet | B: out | Settled by: "as of December 31, 2025" and notes "If a line's last day has passed, it holds nothing."
- F6: Griffin per-fund split | A: 2,662,255 / 84,438 | B: one line | Settled by: KPMG "showing what each fund holds" + 2024 confirmation PDF
- F7: Griffin told | A: Already told, Done | B: Closing | Settled by: Feb 9 email to PERSON_4337 "we've decided to shut the company down"; notes "for a fund, its partner"
- F8: ENG-2438/2439 comment | A: why-comment (no note of its own) | B: none | Settled by: notes separate notes from the heads-up
- F9: ENG-2440 told | A: Already told (Feb 9 DM) | B: Closing | Settled by: notes "Told means a written message about the closing, sent to them directly"
- F10: ENG-2443/2444/2445 family | A: [PERSON_NAME_52949] note; Patrick Lewis and [PERSON_NAME_27652] Covered | B: three notes | Settled by: "one note to whoever has always handled it for a family"; "Mark those lines Covered"; Jun 30, 2023 family list from PERSON_2260
- F11: ENG-2446 told | A: Already told | B: Closing | Settled by: Robert Feb 12 "we're closing the company" (Leonard cc)
- F12: Told grantees (ES-1, 4, 7, 12, 13, 15) | A: Last day | B: Closing and last day | Settled by: Feb 11 letters "The company is shutting down"
- F13: [PERSON_NAME_0051] / [PERSON_NAME_0022] | A: Closing and last day | B: Last day | Settled by: no direct written message; the #company-internal @here post is not "sent to them directly"
- F14: Who goes first | A: [PERSON_NAME_0051] (Feb 21, 2026) | B: other | Settled by: Carta "Last day to exercise Feb. 21, 2026" + "Whoever's last day comes first goes first."
- F15: Matthew Collins ES-9 status | A: outstanding | B: lapsed after the May 2025 board resignation | Settled by: "very happy to join the board meetings etc going forward"; no Carta termination; "Carta is the record"
- F16: Griffin heads-up contents | A: board and stockholder consents to approve the wind down | Settled by: Sunset transcript "will receive board and stockholder consents to formally approve the wind down"
- F17: Sharing | A: sheet to Robert and Arthur, letter to Robert | Settled by: "And the sheet goes to Arthur as well as Robert, the rest of my notes stands"
- F18: Sheet row unit | A: one row per Linear issue | B: per security | Settled by: project "one issue per holder on Carta"; Sunset "One line per holder"

Platform defects:
- PLATFORM:anonymized-token: patrick@harmonygames.co is assigned to both [PERSON_NAME_4468] and Patrick Lewis; one holder appears under different tokens across services (joined by exact share sums); the TOR side-letter notice addresses are tokens.

### FINAL VERDICT: PASS

Score: 5

Execution status: COMPLETE

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), effort not reported by runtime

Next action: Run /hardness with one unhinted Opus run (or a Haiku run). Build the OEs and rubric on the Carta split and the settled forks above.

Evidence limits: None

Eval version: task-quality-v1

Eval release SHA-256: b9281224e0e101faab431b7e10f928a29b8c6f02ebd52037b8aaa26ca5f9fc8c

Reviewed prompt SHA-256: 424c70d34fdfba5e323649f44e4c228d3b3694d2196fc2891d6d55f5fb1407a2

Review context SHA-256: e922d5ad01f0ddc17f65729cdf25540045e5c1b9791227257731ff4e4836aedb

Prompt record SHA-256: c623ad9f10aa28d040c65a3b7f4acf69148a957cbba2b257a62daa02b6060e23

**Lowest Dimension:** None below 5 (all applicable sub-dimensions 5).

**Summary:** Every ask is grounded in records Leonard can see. The per-holder rules are seeded in the notes doc, the project and the #winddown thread, and every holder outcome is settled by a quoted record. The strongest alternative (the Nov 2024 figures as plain shares) is a trap that "Carta is the record" and the Nov 2023 board consent exhibit exclude. The remaining items are platform anonymization artifacts or rubric guidance.
