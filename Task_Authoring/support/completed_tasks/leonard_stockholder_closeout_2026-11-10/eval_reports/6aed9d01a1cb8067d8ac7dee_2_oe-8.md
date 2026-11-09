## OE EVALUATION REPORT

- Review version: Eval 2 (oracle-events-v2); release and binding hashes are in the verdict block.
- Attempt: 6aed9d01a1cb8067d8ac7dee (chat review, third /oe run; OE file revision 10)
- Actual review date: 2026-11-08
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Universe: `Universe_Normal` (hg4-2026-08-31 v37)
- Inputs: OEs `08_Oracle_Events.md` (99 OEs, sha256 `0ac36b4f…`, uploaded as "08_Oracle_Events (3).md"); prompt `04_Prompt.txt` (sha256 `424c70d3…`); assignment `00_Task_Assigned_Inputs.md`; injection SQL `01_Universe_Inject.sql` revision 6 (sha256 `9b02cc8f…`), read as an overlay and never executed. No error/async config.
- Changed since the last run: only OE 21 (diff of revision 9 against revision 10). It now reads the Nov 10 2023 board consent's Exhibit A instead of assuming the term. OE 21 was rechecked against the thread, the attachment bytes and Contacts. The other 98 OEs are byte-identical, and the prompt, SQL, universe manifest, tool catalog and tool-output reference haven't changed, so their record checks are reused (evidence contract stage-evidence-v1: revision-9 record `a1c42db8…`, report `29c071c4…`). The validator re-hashed every source anchor. The deep recheck reran all three passes on all 99 OEs.

### Task: Stockholder/option-holder close-out (holder sheet, investor letter, 14 holder note drafts, 26 Linear states plus why-comments, Griffin heads-up, #winddown reply, KPMG confirmation)
### Persona: Leonard Hayes - Co-founder & Creative Director (leonard.hayes@harmonygames.co)

---

### Phase 1: Structure & Alignment

**Derived critical path** (from the prompt and the records it pulls in, derived independently of the OEs):
1. Find the "Holder records" project, its 26 issues (emails) and their comments.
2. Read the close-out notes (rules, deliverables, recipients, "Told", labels, "the Sunset onboarding").
3. Find the close-out folder, the draft sheet, the update outline, the #winddown draft and list, and the later #winddown posts that make the draft stale.
4. Read Sunset's intake request and KPMG's request and clarification.
5. Work out each line's holding per Carta: 14 notices, the ES-3 extension, ES-8 to ES-11 (size and vesting), seed shares behind the Nov 2024 figures, the Griffin split and the ledger total.
6. Work out who has been told (letters, bounce, Griffin, Robert's note, "Husnu Akin", the ENG-2440 DM, the family handler, no message to TOR or the other angels).
7. Find unanswered holding questions (Claire's).
8. Derive labels, notes, Linear states, totals, counts, directors, the preferred vote, who goes first and KPMG's Dec 31, 2025 figures.
9. Writes: the sheet, sharing, 14 unsent drafts, the up-to-date letter in the folder shared with Robert, 26 states and 12 why-comments, and the KPMG, Griffin and #winddown replies after the sheet.

**Segments:** 99 STEP, 0 CONTEXT, 0 RESPONSE_DESCRIPTION, 0 NON_ACTION. No decision-fork wording (detector: 0 hits), and no step offers two end states.

---

### Phase 2: Accuracy

The ledger covers every Expected value. Each is quoted from a record or derived by a recorded calculation.

| Step(s) | Field | Result | Evidence |
|---|---|---|---|
| OE 1–20, 22–99 | all | VERIFIED (reused, unchanged text) | Same records and checks as the revision-9 review; SQL, base sources, catalog and tool references unchanged, and every anchor re-hashed |
| OE 21 | action, information | VERIFIED (new) | Works out the vesting of ES-8 to ES-11. That feeds 103,764 into OE 34, 35, 38, 39 and 97 |
| OE 21 | tool / service, parameters | VERIFIED (new) | The pointer resolves to one record: Leonard's thread "RE: [SOURCE_ORG_0001]- Option Issuances", message from "michelle <michelle.carter@harmonygames.co>", "Fri, 10 Nov 2023 20:52:19 +0000" (12:52 PM PT, a Friday), body "please see execution copy of Board Consent", one PDF attachment. `gmail_get_attachment` (cataloged: message_id, attachment_id) returns it; the tool-output reference says "A fact stated only in a Gmail attachment is reachable." Contacts are unscoped |
| OE 21 | expected data | VERIFIED (new) | Text of the attachment bytes (pdftotext, re-run today): dated "November 10, 2023"; Exhibit A under "See Specific Vesting Start Dates in Carta" has "30,518 … 1/24th monthly/no cliff", "61,038 … 1/24th monthly/no cliff" and both 6,104 lines "1/24th monthly/no cliff". The other Exhibit A rows are 1/48th employee grants, and the OE doesn't claim them. Contact matthew.collins@harmonygames.co, job set by SQL line 129: "Investor and advisor (left the board May 2025)". Grants dated Nov 18 and Nov 20, 2023 in the Carta digests (OE 18), plus 24 monthly steps, take full vesting to Nov 2025, before Dec 31, 2025 and the clock. 30,518 + 61,038 + 6,104 + 6,104 = 103,764. The last run's MINOR (claims that the PDF can't be opened and that ES-9 and ES-10 have no readable term) is gone |
| OE 21 | dependencies | VERIFIED (new) | Uses OE 12 (no notice for ES-8 to ES-11), OE 18 (grant dates), OE 19 and OE 20 (sizes), all earlier |

Persona access: every read is in Leonard's mailbox (including the consent attachment), Slack conversations he belongs to (#winddown, #founders, his DMs), Docs he owns or is shared on, or unscoped Linear and Contacts. Tool capability: every step maps to a cataloged tool. No link or attachment deliverable is needed.

Numeric observability: unchanged. OE 21's figures are whole-number share counts printed in the PDF text.

### Format & Standardization
No shape defects. Every OE is numbered, has one action, names its service and has an Expected: line. OE 21 reads two sources (the consent and a contact) and writes nothing. Nothing is written as JSON or an arrow chain.

---

### Phase 3: Completeness

| Requirement | Covered by | Result |
|---|---|---|
| Project, 26 issues, comments | OE 1–3 | COVERED |
| Close-out notes | OE 4 | COVERED |
| Folder, draft sheet, outline | OE 5–7 | COVERED |
| #winddown draft, list and later posts | OE 8–9 | COVERED |
| Sunset's sheet contents; KPMG request | OE 10–11 | COVERED |
| Holdings per Carta (including ES-8 to ES-11 vesting) | OE 12–14, 18–22, 24, 34–35 | COVERED |
| Who has been told | OE 15–16, 19, 25, 27–33 | COVERED |
| Unanswered holding questions | OE 17 | COVERED |
| Directors, preferred vote, who goes first | OE 25–26, 37 | COVERED |
| Labels, notes, Linear states | OE 36 | COVERED |
| Sheet written, shared with Robert and Arthur | OE 39–41 | COVERED |
| 14 unsent holder drafts | OE 42–55 | COVERED |
| Letter Doc, brought up to date, in folder, shared with Robert | OE 8, 15, 4, 25, 56–58 | COVERED |
| 26 Linear states, 12 why-comments | OE 59–96 | COVERED |
| KPMG, Griffin, #winddown replies after the sheet | OE 97–99 | COVERED |

- Path feasibility: SUPPORTED. Task solvability: SUPPORTED_BY_OE.
- Act-vs-defer: no defer. The prompt reserves only the holder notes, and they stay drafts.
- No injected error or async wait.
- Outcome-first mapping: OE 39–99 are Outcome (sheet, shares, drafts, Doc, Linear states and comments, sent replies). The reads and derivations (OE 1–38) feed those Outcome rows and need no Process row.

### Pre-verdict sweep
| # | Check | Finding |
|---|---|---|
| 1 | Wrong count, ID, channel or tool | PASS |
| 2 | Required write missing | PASS |
| 3 | Fact in expected data with no retrieving step | PASS |
| 4 | Act-vs-defer conflict | PASS |
| 5 | Non-action or final-response event | PASS |
| 6 | Prompt-forbidden write | PASS |
| 7 | Missing recovery/wait event | PASS (none injected) |

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
| — | — | None. The last run's only defect (OE 21's MINOR) is fixed | — | — |

### Recommended Fixes
None required. The set passes as submitted.

### Readability (advice only, no score impact)
- The set reads well: goal first, values written out, traps named (bounce, ES-3 extension, Akin, family handler, ledger, stale draft lines, the consent's Exhibit A).
- OE 42–55 and OE 59–96: you could add "(after the sheet, OE 39)" the way OE 97–99 do. Your notes ("the holder sheet comes first, the notes and everything else run off it"), the project ("States once the sheet is done") and the Trello card ("Nothing goes out until the sheet is done.") all set that order. The numbered order already keeps it.
- OE 21: the vesting start dates themselves are "in Carta" and not visible. If you want a supporting read for "counted from the Nov 2023 grants", the Advisor Agreement doc for the 6,104 line is "entered into as of July 21 2023" and says "All shares shall vest on a pro rata basis monthly over a 2-year period", which puts the start no later than the grant.
- OE 56, "tax papers are still to come": optionally cite Sunset's Feb 11 call notes in Leonard's mailbox ("will provide Leonard Hayes with two quotes for final year 2026 tax work").

## Deep Recheck

Passes: O1, O2, O3. Each ran as a fresh subagent on Opus 5.5 (claude-opus-5-5), blind to the main review. O3 did not get the OE file.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 99 of 99 OEs | 3 | 0 |
| O2 | 60 requirements against 99 OEs | 2 | 0 |
| O3 | Open instructions in the prompt, notes, project, #winddown, Sunset and KPMG records | 82 items in 8 groups | 72 matched to OEs; 0 MISSING; 10 rejected |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| O1-DR1 | O1 | OE 17 "One unanswered question for a holder who gets a note … Claire Morgan" (open for OE 47, OE 54) | Group DM C51ECE5102ED, ts 1770903714.600249, Claire: "Sadece şeyi sormak istiyorum ben … Bir de equity lerimiz için birşey yapmamız gerekiyor mu prosedür olarak?"; the other two members at 1770905067 / 1770905175: "25 Aralık olması sorun …" | 2.8 Decision forks | Decision fork (boundary) | REJECTED | The record settles who asked. Claire asks in the first person ("sormak istiyorum ben", "I want to ask"). The other two members only confirm the date and ask nothing. The notes rule covers "Anything they asked", so only Claire's note must answer it. OE 47 and OE 54 also don't fail a run that adds the answer |
| O1-DR2 | O1 | OE 51 "A Gmail draft to PERSON_3140_EMAIL, not sent" | Bounce, SQL line 108, 2026-02-11T20:13:57Z; ENG-2457, SQL line 250, created 2026-02-12T23:30:55Z: "Email: PERSON_3140_EMAIL"; notes (created Feb 13 01:05 UTC): "Messages go to the email on each holder's issue." | 2.8 Decision forks | Decision fork (recipient) | REJECTED | Two records written after the bounce settle it. Leonard's own issue for this holder names the address, and his notes send each message there. The issue names the item itself. The note is also a draft that Leonard reads and sends himself ("I read and send each note myself") |
| O1-DR3 | O1 | OE 21 "Counted from the Nov 2023 grants (OE 18), the 24 monthly steps end by Nov 2025" | Consent Exhibit A: "See Specific Vesting Start Dates in Carta"; Advisor Agreement (gdocs /docs_documents/160): "entered into as of July 21 2023", "All shares shall vest on a pro rata basis monthly over a 2-year period"; Leonard, Jun 7 2023: "vesting over 2 years" | 2.4 Expected data / qualifier | Accuracy | REJECTED | Every record that speaks to the start puts it on or before the grant, and an earlier start only brings full vesting forward. "End by Nov 2025" is a valid upper bound and 103,764 doesn't change under any record-supported start. The unseen Carta dates stay an evidence limit |
| O2-DR1 | O2 | OE 59–96 "(state from OE 36)", no "after the sheet" | Project (SQL line 134): "States once the sheet is done"; #winddown ts 1770938158.104719: "They stay in Backlog until the sheet is done" | 3.2 Dependencies | Completeness | REJECTED | The numbered path puts the sheet (OE 39) before every move and comment, and the states come from OE 36. Following the steps keeps the order. Wording advice is under Readability |
| O2-DR2 | O2 | OE 42–55 "(address from OE 2; left unsent)" | Notes (SQL line 15): "the holder sheet comes first, the notes and everything else run off it"; Trello (SQL line 67): "Nothing goes out until the sheet is done." | 3.2 Dependencies | Completeness | REJECTED | Same order argument. The holdings and last days in each draft come from OE 34–36, which come before. Wording advice is under Readability |
| O3 M3, M29 | O3 | ENG-2440 "Closing", counts 5/4/2/6/5/4 | DM D04UC0UEN2V, Feb 9 2026 19:23 UTC, Leonard: "Metrics didn’t improve. The most reasonable thing to do right now is to shut down the company we decided." | O3 inventory | Completeness | REJECTED | A direct, delivered written message about the closing from Leonard, so the line is Already told, the counts are 5/5/2/5/5/4, and there are 14 drafts, as OE 19 and OE 36 say |
| O3 M30 | O3 | Sunset's "A count of holders by what each still needs to hear" vs the two Griffin rows | Notes: "One row per issue on the sheet, and the counts go by rows." | O3 inventory | Decision fork | REJECTED | The notes speak to exactly this case: counts go by rows |
| O3 M39 | O3 | ENG-2457 address vs the Feb 11 bounce | As O1-DR2 | O3 inventory | Decision fork | REJECTED | As O1-DR2 |
| O3 M41 | O3 | Carta: "[PERSON_NAME_0089] [PERSON_NAME_25152] has requested cap table access" | Carta system notice; ENG-2440 is Already told | O3 inventory | Completeness | REJECTED | It's an automated Carta notice, not a question to the founders, and that holder gets no note ("if they get one") |
| O3 M42 | O3 | TOR, Sep 27 2023: "can you please give me access as well" | Leonard, same day: "Done on my end but [PERSON_NAME_0128] doesn't have access yet. We are trouble shooting…" | O3 inventory | Completeness | REJECTED | Leonard answered it. The rule covers questions "we never answered" |
| O3 M50, M51, M53 | O3 | Draft IP/plan/vendor lines vs "$22500" offer, "30-45 days", Singular/SVB | #winddown and the Board position thread | O3 inventory | Completeness | REJECTED | OE 56 already updates the IP, wind-down and vendor lines. The data offer and the later paperwork don't contradict the update, and the letter isn't required to list every vendor |
| O3 M81 | O3 | "notes ready … by Tuesday"; calendar "Holder notes due" | Notes; GCal | O3 inventory | Completeness | REJECTED | A deadline the drafts meet now. It needs no step |

Matched items (confirmed and covered): M1, M2, M4–M28, M31–M38, M40, M43–M49, M52, M54–M80, M82. Each is covered by the OEs listed below. M10, M23 and M65–M68 were marked UNSURE by the pass and are settled by OE 13, OE 21 and OE 30.

Effect on verdict: unchanged from the main review. No finding was confirmed. Completeness 5, Accuracy 5.

O3 inventory:
- G1: Finish the draft sheet; one row per issue, labels, totals, directors and the preferred vote | "Holder list (draft)" vs Linear issues, Carta, letters and DMs | 32 items (M1–M32) | Covered by: OE 2–3, 6, 9–36, 39 (M3, M29, M30 rejected)
- G2: Carta over dates in the letters | Feb 11 and Oct 2025 letters vs Carta notices and the ES-3 update | 6 items (M33–M38) | Covered by: OE 12, 14, 35, 38
- G3: Messages to the issue email; unanswered holding questions | ENG issues, bounce, group DM, Carta notices | 4 items (M39–M42) | Covered by: OE 2, 16, 17, 49, 51 (M39, M41, M42 rejected)
- G4: New notes replace the outreach notes (order, one by one, Carta, sharing, folder) | Old vs new notes, #winddown replies | 5 items (M43–M47) | Covered by: OE 4, 9, 37, 39–41, 57–58, 99
- G5: Bring the letter up to date using the outline | #winddown draft, later posts, update outline | 9 items (M48–M56) | Covered by: OE 7, 8, 15, 25, 56–58 (M50, M51, M53 rejected)
- G6: Griffin heads-up on the Board position mail | Board position thread | 1 item (M57) | Covered by: OE 25, 98
- G7: KPMG confirmation as of Dec 31, 2025 | KPMG request and clarification vs Carta, ledger, Griffin split | 23 items (M58–M80) | Covered by: OE 11, 12, 20–24, 34, 38, 97
- G8: Timing; the sheet goes to Sunset by Leonard | Notes, calendar, Linear project | 2 items (M81–M82) | Covered by: OE 1, 4 (no send to Sunset is prescribed; M81 rejected)
Scope: G1 (32 items) and G7 (23 items) each cover more than 15 items. Both are bounded by the 26 issues in the Linear project and KPMG's four numbered items, which the prompt already points to.

Platform defects: PLATFORM:anonymized-tokens. One holder appears under several tokens: Husnu Matthew Collins / "Husnu Akin" / [PERSON_NAME_11362]; Brian Foster / [PERSON_NAME_2769] [PERSON_NAME_0093]. Visible records join them (OE 13, OE 30), and they aren't scored.

### FINAL VERDICT: PASS
Score: 5
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: 0ac36b4fd15af4cc94af0fdb9cd0a28be034380814e7f6eb956ea8ace1b5ca08
Review context SHA-256: 820f28ba5b50f1e4e0d5a61f340dcd32c93ce1950968a00994a273064821dc0b
OE record SHA-256: b7a44e448f8a74726455de04b26d102bcaa9bb87339a2daf62b3743e1a6b62cd
Eval version: task-quality-v1
Eval release SHA-256: b9281224e0e101faab431b7e10f928a29b8c6f02ebd52037b8aaa26ca5f9fc8c
Evaluator model: Opus 5.5 (claude-opus-5-5), effort not reported by runtime
Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Next action: Review complete. Use this OE set in your Outlier task; /rubric is next.
Evidence limits: Static universe, SQL and catalog evidence; no live writes executed. OE 1–20 and 22–99 reuse the revision-9 record's checks (unchanged OE text, prompt, SQL, universe manifest and tool references; anchors re-hashed). The absence claims rest on complete scans of Leonard's mailbox and Slack DMs (scan receipts kept in the local eval cache). The consent was read by text extraction of the attachment bytes. The vesting start dates for ES-8 to ES-11 are "in Carta" and not visible; full vesting rests on the Nov 2023 grant dates, the 24-month schedule and the July 2023 advisor agreement.
