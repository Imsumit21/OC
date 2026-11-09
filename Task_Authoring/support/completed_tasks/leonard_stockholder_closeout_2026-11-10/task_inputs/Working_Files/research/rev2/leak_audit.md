# Leak audit, rev2 (local SQL fd51afbf63aa vs platform-era rev1p)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Persona Leonard Hayes.

## 0. Scope and method

- **Compared:** `Task_Authoring/task_inputs/01_Universe_Inject.sql` (sha256 `fd51afbf63aa2d05…`, 279 lines) against `Working_Files/run_forensics/rev1p/01_Universe_Inject.sql` (265 lines, the platform-era approximation). I diffed them statement by statement.
  - 10 statements added: the Jan 14 #executives note, Robert's reply-all (3 mailbox copies + 3 snippet UPDATEs), 2 owner-list UPDATEs, and the Collins contact UPDATE.
  - 59 changed: the notes doc, draft sheet, 2 deck elements, the KPMG follow-up and its snippet, the Sunset intake and Leonard's reply, and 26 Linear issues with 26 comments.
  - The Linear project description is unchanged.
- **Fork sources:** `research/prompt_review_rev1/` (P1.md, P1_rev2/3/5/7.md, P1_cold.md, P2.md, P2_cold.md) and `plan/design_delta.json`.
- **Slots and mechanisms:** `Working_Files/01_Gradable_Surface.json` and `01_Hardness_Manifest.json`.
- **Run evidence:** `06_PreCheck_Trajectory/trajectory.json` (the compaction summary at event 835, plus the write payloads) and `run_forensics/rev1p/precheck/precheck/calls.jsonl` (237 calls).
- **Base checks:** `hg.py search` only.
- **Not done:** no SQL executed, nothing written outside this file. People are referred to as they/them.

## 1. How the platform-era run decided BOARD, ASOF and the Griffin heads-up

The run solved all three without any of the rev2 settling records.

- **BOARD.** The Summary tab (call ev. 783) reads "Directors in office | Leonard Hayes, Robert (Griffin's Series Seed director resigned Feb 12, 2026; seat vacant)". The run had no Robert record. It worked from:
  - the Board position thread (Griffin's resignation; Leonard's 22:14 reply cc Robert and Arthur);
  - #winddown "we are personally liable as bod members";
  - a "Collins (resign OR board OR options)" search (ev. 607), which made Collins a "former independent director";
  - Carta "added you as a board director" mails.

  It never opened the decoy, the Feb 11 Sunset notes (gdocs /26: "whose board consists of themselves and Griffin"). It never opened the charter either. My trajectory search finds no hit for "board and stockholder consents", "whose board consists" or "Requisite Holders". So the BOARD decoy and T10/T11 never came into play: B1 passed by default.
- **ASOF.** The KPMG reply (ev. 944/950) came from three inputs: the root's "using each effective date as Carta shows it, regardless of when recorded", the OLD follow-up ("a termination effective on the as-of date itself counts as of that date") and the 14 Carta termination mails. From those the run:
  - counted Dec 31 terminations at vested ("vested portion only");
  - counted the Jan 30, 2026 lines at full grant;
  - counted ES-3/5/14/16/17 at vested ("still within the exercise window on December 31");
  - excluded ES-2 and ES-6.

  That gives 139,993 and 9,295,636. Every AL_ row is right (17,802; 1,530; 10,384; 22,889; 16,277). A1 failed only through ADV (advisor options booked as Series Seed, 3,155,643). Note that **A2 9,295,636 is invariant to the ADV split** (3,155,643 + 139,993 = 3,051,879 + 243,757), so A2 grades ASOF only, and the run passed it.
- **Griffin heads-up.** The run replied to all on Leonard's own 22:14 message (`<CAPBs_a5B01Fz…>`), so it went To PERSON_4337, cc PERSON_2847, Robert and Arthur. It made three asks, the first being "Written consent, as majority holder of the Series Seed Preferred, to the dissolution…". The ask came from Sunset's "who holds the preferred vote" plus prior knowledge. G2 passed by default. Under today's notes ("their own Board position mail") the reply would go to PERSON_4337's 22:05 message instead.

**Consequence.** None of the settlers below is what made the run easy. Each one closes a fork the run had already closed on its own. They matter for UGT and for the "notes spell out every rule" impression. Taking them out does not, on its own, make the task harder (Part 8: hardness needs a deciding fact moved off path, not fewer settlers).

## 2. Item 1: KPMG follow-up states the vested-only / effective-date rule (ASOF)

- **Current text** (SQL line 86, message `<LV3PR19MB85246D2E…>`, thread 1857029474983245439, snippet line 84): "For item 2, a line terminated on or before the as-of date counts only what had vested by its termination date." The platform-era text was "a termination effective on the as-of date itself counts as of that date."
- **Fork settled:** P1.md F6 / DR6. Reading A is 139,993 plus the advisor lines. Reading B (291,557) counts granted minus exercised on every unexpired line. Reading C (110,471) uses vested figures everywhere. P1_rev2 marked it partly settled and P1_rev3 marked it settled (243,757; 9,295,636). Design_delta: "local /prompt round rev1".
- **What it gives away:**
  - The vested-only measure for terminated lines. That decides AL_ES-1, AL_ES-14 and AL_ES-16 (w3 each).
  - By contrast, full grants for the Jan 30 lines, which decides AL_ES-7 and AL_ES-12.
  - A hint that lines terminated before the as-of date are counted at all. That is half of CH-ASOF's "report today's count" natural reading.
  - A1 and A2 (w5) only on their ASOF side; ADV still decides A1.
- **What it does not give:** the Jan 2026 lapses that still count at Dec 31 (ES-3/5/16/17), the exclusion of ES-2 and ES-6 (control ENG-2455, asof_over), and the advisor lines. Read literally, "counts only what had vested" even invites asof_over on ES-2 and ES-6.
- **Base alternative (checked):** DM D04UP2L3E3S (Leonard and Robert), Nov 9, 2023, has Robert quoting the plan: "such Optionee may exercise any outstanding Option at any time within 3 months following such termination to the extent the Optionee is vested in the Optioned Stock" (`messages/D04UP2L3E3S/2023-11.json` /318). The Feb 11 letters add "Any exercise rights will be governed by the applicable equity plan". No base record says "unvested options are cancelled" (searches for unvested, pool and cancel in Gmail and gdocs found nothing relevant). Carta's "Current holdings" lists Granted next to Vested.
- **Verdict: KEEP.** Opus already applies vested-only by default; the run did so on the old wording, so the leak is cheap. The fork is fail-level (A1, A2 and five AL rows).
- **Optional soften:** "counts as of its termination, under the plan", leaning on the 2023 DM. **Reopen risk: medium-high.** "To the extent vested" can be read as a limit on exercise, not on what is outstanding, and Reading B comes back.
- **Real lever if ASOF must bite:** a dated Carta correction mail, in another thread, that moves one line's effective date across Dec 31 (Parts 3.2 and 3.4). This adds no holders or rows. The other agent owns "3,051,879"; leave the item-2 sentence alone when that part changes.
- **Item 4 sentence (same mail):** "For item 4, we need any new financing and whether the company is winding down." This settles P1_cold F3 (open set) and gives away A5 (w3) and A7 (w1). The run wrote both without it. **KEEP.**

## 3. Item 2: Robert's reply-all "Leonard and me on the board" (BOARD, T10/T11)

- **Current text:** SQL lines 94–102. Message `<CAGkro_Tn7wQ2xLp9VbR4mYc8KsHd3EjUf6ZaNi1oGqX5tBe0Rw@mail.gmail.com>`, Feb 12 22:38Z, sits in Leonard's INBOX on thread 1856958794180374704, with copies in Robert's and Arthur's mailboxes and 3 snippet UPDATEs: "Thanks PERSON_4337_NAME, for everything over the last three years. That leaves Leonard and me on the board to see the close through."
- **Fork settled:** P1.md F2 / DR2. Reading A is Leonard only, from the Feb 11 notes gdocs /26 ("The board, which … consists of themself and [PERSON_NAME_2000]"). Reading B is Leonard and Robert, from Nov 2023 counsel naming Robert "Common Director". P1_rev2 marked it SETTLED by this reply.
- **What it gives away:** B1 (w5) and L6 (w3) outright, T10 ("the four named in the financing documents") and the Robert half of BOARD. It sits on the one thread every run must open, because it is the target of the Griffin heads-up (run ev. 57/62).
  - T11 is not given away here. The notes doc gives it (item 3).
- **Base support (checked, persona-reachable, off path):** Carta "Board consent approved" mails in Leonard's mailbox list who signs board consents:
  - Nov 10, 2023: PERSON_4337, Collins, Leonard, Robert (plus counsel);
  - Aug 30, 2024: PERSON_4337, Collins, Leonard, Robert;
  - **Jul 21, 2025: PERSON_4337, Leonard and Robert only** (`leonard@…_1838216168984971198`).

  Collins resigned on May 1, 2025 ("I would like to resign … with immediate effect", `leonard@…_1830959847543474636`). These records are older than the Feb 11 notes, so a cold reviewer can still read "newer wins" for Reading A. A record dated after Feb 11 is still needed.
- **Verdict: MOVE.**
  - Delete the reply-all: 3 INSERTs and 3 snippet UPDATEs, which takes the Board position thread back to its 2 base messages.
  - Add one Robert line in DM D04UP2L3E3S (members include Robert and Leonard), dated Feb 12 after 22:05Z, stating only their own seat, for example: "saw PERSON_4337_NAME's mail. I'm staying on the board until Sunset files."
  - The run then has to combine that line with the Jul 2025 consent signatories and Griffin's resignation to get Leonard and Robert. Net change is minus 5 rows.
- **Fallback SOFTEN in place:** "I'm staying on the board to see the close through." **Reopen risk: low.**
- **Reopen risk for the MOVE: low-medium.** A cold P1 census of Leonard's Feb DMs finds the line, and it is the director's own dated statement after the Feb 11 notes, not Leonard's claim.
- **Note:** BOARD is inverted. The decoy (gdocs /26) is off path and the truth is on path. BOARD can only bite if the decoy is the easy record and Robert's line is the off-path correction.

## 4. Item 3: notes doc spells out the Griffin ask

- **Current text:** SQL line 19, doc `f_a37b403d5200d4f0a31d31`: "Griffin's partner gets a heads-up as a reply to all on their own Board position mail from Feb 12, asking for their vote as preferred holders on the dissolution. That one can go out once the sheet is done". The platform-era text was "…as a reply on the Feb 12 Board position thread, with what we still need from Griffin."
- **Forks settled:**
  - P1.md F4 / DR4: no record said what was "still needed". Alternatives were confirming the resignation date (Leonard's 22:14 "unless you intended a different effective date"), a replacement director, notice details, or the KPMG figures.
  - Recipients: P1_rev2 F4 residual, P1_cold F2 / DR2, and P1_rev5, which marked it SETTLED via "their own Board position mail". Design_delta: "local /prompt round rev1" and "P1 rev3 recipients".
- **What it gives away:** G2 (w3) outright and T11 ("Griffin's director resigned, so Griffin has nothing left to sign") outright. It also gives the "who" of B2 (the 90% figure still needs ADV) and BOARD's "Griffin has nothing left to do" reading. It is a rule written into the doc that every run reads first (run ev. 11).
- **Base support (checked, off path):**
  - the charter (gdocs /360 "Amended and Restated Cert…"): "liquidate, dissolve or wind-up the business … " requires the Requisite Holders, "a majority of the outstanding shares of Preferred Stock";
  - the Feb 11 Sunset notes (gdocs /26): "will receive board and stockholder consents to formally approve the wind down";
  - the Sunset intake (on path): "who holds the preferred vote" and "Formal notices are a separate step", which rules out a notice-details ask.
- **Verdict: SOFTEN.** Keep "a reply to all on their own Board position mail from Feb 12". It settles the recipients, and that leak is cheap (w1 delivery). Replace "asking for their vote as preferred holders on the dissolution" with "with the one thing we still need from Griffin for the dissolution". That stays a closed set of one; the base records above fill it, and the resignation-date reading falls away because it is not for the dissolution.
- **Reopen risk: medium-low.** A reviewer could still name "board consent", but Griffin no longer has a seat.

## 5. Item 4: every Linear issue carries its holder's email

- **Current text:** all 26 issue descriptions read "Email: …". Examples: ENG-2446 "Email: PERSON_3941_EMAIL", ENG-2445 "Email: PERSON_2275_EMAIL", ENG-2459 "Email: PERSON_2684_EMAIL", ENG-2463 "Email: PERSON_1174_EMAIL". The notes doc (line 19) adds "Messages go to the email on each holder's issue."
- **Forks settled:** P1.md F5 / DR5 (two addresses or none; the patrick@ collision; no address for [11362]), P1_rev2 F5b (staff company vs personal address; none for ENG-2459/2463) and P1_cold F1 / DR1. P1_rev3 marked them SETTLED. Design_delta: "P1 rev2 forks".
- **What it makes cheaper:** address-level search keys.
  - ENG-2446: Robert's Feb 12 note goes To PERSON_3941_EMAIL (SQL line 105, a 2023 wire thread). That is T7's hiding place (C_NEB w5, TC_NEB, LC_Neb).
  - ENG-2445 and ENG-2444: the Jun 30, 2023 profile mail (FAM: F1 w5, F4, F5).
  - ENG-2459 and ENG-2463: no Feb 11 letter to those addresses (LETTER: C_ES14 and C_ES18 w5, N_Vincent w5).
  - The issue titles already carry the same tokens (PERSON_3941_NAME, [PERSON_NAME_27652], [PERSON_NAME_0051]), so the gain over the titles is small. The run solved TOLD, FAM and LETTER with no emails.
- **Verdict: KEEP.**
  - The address fork reopened in four review rounds (P1, P1_rev2, P1_cold, P1_rev5).
  - Emails only on some issues would recreate the LEAK-7 gap: no email would mean no note, which gives away the label (design §1562).
  - The emails on no-note issues are never used to send anything.
- **Reopen risk if changed: high.**

## 6. Item 5: other rule/result statements in the diff

| Text (location) | Fork / source | Gives away | Verdict | Reopen risk |
|---|---|---|---|---|
| Notes: "Carta is the record, over any date in the letters." (line 19) | P2.md DR3 / NB-22; P1_rev2 "checked and fine" | Carta's Jan 30 over the letters' Jan 31 or "January 31, 2025". KPMG's root already says "as Carta shows it", so it frees nothing new. | KEEP | – |
| Notes: "One row per issue on the sheet, and the counts go by rows." (line 19) | P1.md F8 / DR8 | Already told 4 vs 3; no weight-5 slot | KEEP | low |
| Contacts UPDATE, Collins: "Investor and advisor (left the board May 2025)" (line 117) | P2.md DR4 (base contact said "Independent Director") | T10's Collins exclusion; part of B1 and L6 | **SOFTEN** to "Investor and advisor". That removes the stale seat, and the May 1, 2025 mail plus the Jul 2025 Carta signatories still settle it. | low |
| 26 comments "Last mail with that address before Feb: <date>" / "No mail …" | P2_cold F1 and N3; design LEAK-7 (uniform, so no gap marks a told line) | No rule or result. Only a search hint ("before Feb"). The old ENG-2440 comment (Jan 30) pointed at the told DM; the new one (Jan 8) does not. | KEEP | – |
| KPMG item 4: "any new financing and whether the company is winding down" | P1_cold F3 | A5, A7 | KEEP (see §2) | – |
| #executives Jan 14 note: "…the owner list counts the advisor options in with the stock" (line 52) | P1_rev2 N1, P2 | The ADV rule, plus 3,051,879 and 305,186. This is the largest rule statement in the diff. | Out of scope (ADV agent); flagged | – |
| Draft sheet note: "percentages leave out the option pool… about 94%" (line 26) | P2_cold_rev11 F2 | Mild ADV hint | KEEP (ADV agent) | – |
| Titles: ENG-2447 "Husnu Matthew Collins", ENG-2460 "Brian Foster" | main F-1; P1 F7 | Identity joins; the run made the ES-15 link without them | KEEP | medium if reverted |
| Deck: "Holders, per the Nov 2024 owner list" and "Why we are closing"; notes drop "Notice route" | P1 F9, P1_cold F4, rev7 | Removals; no leak | KEEP | – |

Labels, the state mapping, the comment rule and the family "Covered" reply are not in the diff. They were already in the platform-era SQL.

## 7. Summary table

| # | Item | Verdict | Change | Reopen risk |
|---|---|---|---|---|
| 1 | KPMG vested-only / on-or-before | KEEP | none (optional soften via the 2023 DM plan quote) | n/a (medium-high if softened) |
| 2 | Robert "Leonard and me on the board" | MOVE | delete the reply-all (6 statements); one Feb 12 own-seat line by Robert in DM D04UP2L3E3S; base Jul 2025 Carta consent supports it | low-medium (fallback soften in place: low) |
| 3 | Notes' Griffin ask | SOFTEN | "…their own Board position mail from Feb 12, with the one thing we still need from Griffin for the dissolution" | medium-low |
| 4 | Email on every issue | KEEP | none | high if changed |
| 5a | Collins contact | SOFTEN | job = "Investor and advisor" | low |
| 5b | Other diff text | KEEP | none; the ADV note goes to the ADV agent | – |
