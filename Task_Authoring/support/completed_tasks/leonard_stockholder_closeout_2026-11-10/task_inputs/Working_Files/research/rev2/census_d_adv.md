# Census D: ADV un-pointing (rev2)

Scope: mechanism ADV (A17; chain C1; traps T1/T2). Base = Feb 14 2026 normal universe, read through `hg.py search` (persona filter off, so visibility is checked by hand from owner/shared/visibility fields). Overlay = `01_Universe_Inject.sql` (local rev fd51afbf63aa) compared with `run_forensics/rev1p/01_Universe_Inject.sql` (the platform run). No SQL executed.

Requester goal: the deciding records are the advisor table and the ledger only. Remove the leaks, then re-check UGT with a cold P1.

---

## 1. Reachability of every grant-size source

### 1a. Advisor table: two body-text carriers, both visible to Leonard

| Carrier | Visibility | Content | How an ordinary search finds it |
|---|---|---|---|
| gdocs `/docs_documents/262` = Drive `/drive_files/36125` `f_6a37227593d0977fdbdd7a`, "Due Diligence Disclosures(.docx)", created 2023-06-15, modified 2023-07-10 | owner `leonard.hayes@`; visibility `anyone`; shared with Robert, Arthur, Benjamin Clark, Thomas Baker, PERSON_3880; parent `d_63fffeb4fab5233ed5bb73` (Leonard's My Drive root) | §V.C: "intends to enter into advisory agreements … for which they will receive **options**": [PERSON_NAME_6201] 0.5% 30,518 / **Matthew Collins** Board 1% 61,038 / [PERSON_NAME_0801] 0.1% 6,104 / [PERSON_NAME_6408] 0.1% 6,104 / Total 1.7% **103,764** | Docs fullText `103,764` and `61,038`: the only Leonard-visible hit. `advisory`: about 7 visible docs, this one about 5th newest. `advisor`: about 20 visible, mid-list. `commitments to grant options`: 1 visible. Title words: `Due Diligence`, `Disclosures`. |
| Gmail `leonard.hayes@harmonygames.co/1773160163779741845`, "RE: Follow up items", Aug 3–10 2023, 12 messages (Leonard, Benjamin Clark, michelle) | Leonard's own mailbox; the table is in the **body** of every message | Leonard: "Advisory agreements: … can't seem to find the final number of shares for our advisors … >From the disclosure schedule": [PERSON_NAME_0090] Advisor 30,518 / Matthew Collins Board member 61,038 / **PERSON_1287_NAME** Advisor 6,104 / **PERSON_3941_NAME [PERSON_NAME_0127]** Advisor 6,104 / Total 103,764 | Gmail `103,764`, `61,038`, `30,518`, `6,104`: 12 hits, all in this thread (plus copies in Robert's and Arthur's mailboxes, which Leonard cannot see). Also matched by `advisory`, `Collins board`, `advisory shares`. |

- The Gmail copy is the better join. Its names are exactly the ENG-2449 (`PERSON_1287_NAME`) and ENG-2446 (`PERSON_3941_NAME [PERSON_NAME_0127]`) issue titles. The 0.5% advisor appears under different tokens in the two copies ([PERSON_NAME_6201] / [PERSON_NAME_0090]). It still joins to ENG-2440 ([PERSON_NAME_0089] [PERSON_NAME_25152], 81,383) in two ways:
  - Arithmetic: 81,383 − 30,518 = 50,865, which is a $50K check at the SOP price of $0.983 (Griffin $2,616,996.67 / 2,662,255 in "RE: Revised SPA and Certificate", `…_1771880236343640719`).
  - DocuSign: "[0089] [25152] viewed … Advisor Agreement - Segerstråle".
- Every grant size and every holder can be recovered from body text. The design names only the doc; the requester should know there are two carriers.
- **PDF consent exhibit** (`…_1782034095239486005`, "Re: Option Issuances", `att_0001.pdf` on msgs 3/29/33): the live tool list has `gmail_get_attachment`. However, `Evals/references/persona/acl.md` (2026-10-17 note) says Gmail attachment reads return no bytes (`no_attachment_root_configured`), so this evidence is **unobservable**. The platform /prompt report's "Gmail attachments are readable per acl.md" contradicts the local acl.md. Nothing needs the PDF; the two body-text copies above cover it.
- Advisor agreements f_c2c881…, f_e48755…, f_7982b7… are Resource-owned with `shared_with []`, so they are hidden from Leonard. They are not needed for sizes. Vesting is visible in PERSON_3941's agreement (doc 160 / drive 30806, shared with Leonard: "monthly over a 2-year period") and in the Jun 7 2023 mail. Grants from 2023 are fully vested by Dec 31 2025 and by the clock.

### 1b. "The ledger"

- There is **no per-holder Series Seed ledger in body text** anywhere. Gsheets has no 3,051,879, 25,432 or 50,865 cell. The Carta `…summary_cap_ledgers` download and the Aug 2023 cap-table Google Sheet link are absent or attachment-only.
- The ledger record is **gdocs `/docs_documents/40` `f_11040fe5d66821bd6951aa`**, "Reset Financing Term Sheet (Washout Recap + Pay-to-Play)":
  - Created Jan 22 2026; owner Leonard; private; in his root folder.
  - Exhibit A, "Inputs from ledger (pre-recap)": Founder common **6,000,000**, Series Seed Preferred (all non-founder investors) **3,051,879**, Options outstanding **268,772**, Griffin "in the ledger totals **2,746,693**".
  - It is about the 19th newest Leonard-visible Drive file. It is the newest hit for Docs fullText `ledger`, `cap table`, `Series Seed`, `options outstanding` (gdocs search sorts newest-modified first).
- Corroborating base records, all body text and all Leonard-visible:
  - "Re: Second Close- Tor Capital" (`…_1773160052067710033` msg 10, Aug 10 2023): "doesn't perfectly add up to what we have at disclosure schedule (3,051,882 vs **3,051,879**)". This defeats the "the 2nd close added shares" explanation that the platform hardness evaluator gave: the second close is already inside 3,051,879.
  - "RE: Cap Table" (`…_1770717887098657139`, Jul 10 2023): Series Seed Investor 3,051,882 | Option Pool 1,017,294 | **Advisors 103,763.99** as its own line.
  - ChatGPT-pasted #executives posts (C07C2866011 /727 and /728, Jan 14 2026): 3,051,881 seed and "Other Seed investors 305,188", plus an option reserve of 1,121,058 (= 1,017,294 + 103,764).
- Per-holder angel stock is derived, not recorded: either owner-list line − advisor grant, or check ÷ $0.983 (25,432 per $25K, 50,865 per $50K).
- **Exact tie-outs**, each of which only works with all four grants removed:
  - 3,155,643 (owner-list Series Seed lines) − 103,764 = **3,051,879**
  - 408,950 (non-Griffin angel lines) − 103,764 = **305,186** = 3,051,879 − 2,746,693
  - Term sheet 268,772 options = 103,764 + 165,008 employee lines (P2_cold)
  - Common is exactly 6,000,000, which rules out advisor grants being common stock.

### 1c. What the platform run saw (06_PreCheck_Trajectory)

- The term sheet ID appears in the run's `gdrive_search fullText "cap table"` (ev 71) and in `gdrive_list_recent_files` (ev 92). The run **never opened it**: "3,051,879" occurs 0 times in the trajectory.
- The Follow up items thread appeared only in search and metadata listings (ev 496, 502). "103,764" occurs 0 times.
- The run looked for ES-9 sizes with `"ES-9" OR … OR (Collins (resign OR board OR options))` (ev 607), max 30 results, and never searched `advisor` in Docs. It flagged "the open ES-8–ES-11 question" and booked 3,155,643 / 139,993.
- Conclusion: reach exists and was one click away twice. The run missed because of the bridge (it never opened the ledger and never searched by size), not because of visibility.

---

## 2. Leak census, current SQL (fd51afbf63aa)

| # | SQL row | What it gives away | Why it was added (fork it settled) | Proposed edit | Does the fork stay settled? |
|---|---|---|---|---|---|
| L1 | L52 `slack_messages 846a70ba…`, #executives, Jan 14 19:18:51, top-level, Leonard: "fyi the seed figures in these are 2 off, the ledger has 3,051,879 seed preferred and 305,186 for the other seed investors, so the totals above run 2 high. **the owner list counts the advisor options in with the stock**" | (a) **The ADV rule in words** (last sentence). (b) K1's value and the 103,764 gap (305,186 vs 408,950). It sits next to the fund-split post every run reads. | (a) design_delta[16] / P1_rev2 N1, N2 (ledger vs per-holder lines; what ENG-2447 holds). (b) design_delta[15] / P2 DR1 (ChatGPT's 3,051,881 vs 3,051,879). | **Delete the last sentence (required).** Replace the rest with a numberless thread reply under /727 (ts 1768416262.426129; update the parent's reply counters): "fyi chatgpt has the seed count a couple of shares off in these, go by the ledger". The note cannot name the term sheet, which is dated Jan 22. | DR1: yes, the posts are flagged as off and the ledger outranks them. N1/N2: yes, by the deciding records: the exact tie in §1b plus the advisor table plus Carta "option grant ES-9 / ES-11". |
| L2 | L84 thread snippet UPDATE and L86 KPMG follow-up (`…<LV3PR19MB85246D2E…>`, Feb 13 17:37): "For item 1, our prior-year file has 6,000,000 common and **3,051,879 Series Seed**; if nothing has been issued since, those carry over." | K1's value, given in the thread the run must answer. It forces the 103,764 conflict for free. | design_delta[14] / P1 F3 (Series Seed total: 3,051,881 vs owner-list sum) and eval1 "P1 F3 / P2 DR1 RESOLVED". | **Delete the item-1 sentence.** Body and both snippets become "Thank you Leonard. Two clarifications on our side. For item 2, … For item 4, …". Keep item 2 (ASOF) and item 4 as they are. | Yes, by the ledger: Jan 2026, "Inputs from ledger", newer than the Nov 2024 list. The exact tie removes the alternatives. "Carta is the record" puts the ledger over a workers'-comp owner list. The Second Close mail removes the 2nd-close story. |
| L3 | L117 contacts UPDATE `db57e559…` job = "Investor and advisor (left the board May 2025)" | The word "advisor" for Collins. | design_delta[15] / P2 DR4 (base said "Independent Director" after the May 2025 resignation). It also settles F15 (ES-9 still outstanding because his advisor service continues). | **Keep the meaning.** Base already says "Independent Director (investor/advisor, not an employee)", so "advisor" is base-native. To match base pointing exactly, use "Investor/advisor (left the board May 2025)". Removing "advisor" would reopen F15 (options lapsing 90 days after service ends). | Yes |
| L4 | Issue titles and descriptions | No "Series Seed and advisor options" text exists. I checked all 26 issues and 52 comments: titles are owner-list or Carta forms, descriptions are "Email: …". ENG-2447 "Husnu Matthew Collins" is Carta's SSP-10/ES-9 name: a join, not a statement of the split. | design_delta[10], [14] | None | — |
| L5 | Linear comments "Nov 2024 owner list: 86,470 / 81,383 / 31,536" (L140, L176, L182, L194) | Nothing; this is the T2 bait (the wrong reading). | design | Keep | — |
| L6 | L26 draft sheet "Holder list (draft)": 7 rows "copied from the Nov 2024 list" plus the note "the list's percentages leave out the option pool, so they only add to about 94%" | Note: neutral. 9,477,719 / 10,069,173 = 94.1%; the missing part is the unissued pool, and the note if anything props up the wrong reading. **Row selection** is a soft cue: Griffin, 0038, Collins, Segerstråle, TOR, 3941, 1287. It is the top lines minus Cameron (35,605), so it singles out the four advisor-angels. | design_delta[15], [21] / P2_cold_rev11 F2 | Add Cameron's row ("[PERSON_NAME_2768] [PERSON_NAME_0011]", 35,605), or list every non-founder line, so the selection reads as "largest holders". Keep the 94% note. | — |
| L7 | L41 deck "Holders, per the Nov 2024 owner list" | Decoy | design_delta[9] (the older "268,772 options (Jan 22 term sheet)" pointer has already been removed) | Keep | — |

Nothing else in the overlay mentions advisor, option grant, 103,764, 61,038 or the split (I grepped the whole SQL).

---

## 3. Trap incorporation and the bridge

- **Incorporated chain:**
  1. The prompt says "my close-out notes doc has how each holder gets handled … the way those lay it out".
  2. The notes say "Carta is the record, over any date in the letters" and "Each note says what they hold".
  3. The Linear project says "one issue per holder on Carta" and "the sheet is what Sunset asked for". Sunset asks for "what each holds today (for options, what's vested)".
  4. KPMG item 2 asks for "each outstanding option line by holder … as Carta shows it".

  The wrong reading (owner list as stock) breaks Carta. Carta digest `…_1782897835407336831` (Nov 17 2023) lists "option grant ES-9 … for Husnu Matthew Collins" and "ES-11 … for PERSON_3941_NAME [PERSON_NAME_0127]", and SSP-10 is a stock certificate for the same Collins. The trap is properly incorporated.
- **"Carta is the record" does not reach the sizes.** Carta mails carry no amounts for ES-9/ES-11, and ES-8/ES-10 have no visible digest at all (their holders are hidden under "7 more items"). A run has to cross from Carta to the advisor table itself. The platform run failed at exactly this step.
- **Natural bridge, no pointer needed:** the ledger. Opening the term sheet shows 3,051,879. Against the owner list's 3,155,643 that leaves a gap of 103,764, and a Gmail or Docs search for that number lands on both copies of the advisor table. The only question is whether the run opens the ledger.
- **Least-pointing aid** (if a cold P1 or forecast says the bridge is too thin), in order:
  1. The L1 rewrite above: a numberless "go by the ledger" thread reply under the ChatGPT post that runs already read for the Griffin fund split. It points at a deciding record, not at the split, and it is in Leonard's voice.
  2. Optional, for fairness: one Carta activity digest in Leonard's inbox in base format, for example Nov 18 2023, "[0089 25152] accepted option grant ES-8 / PERSON_1287_NAME accepted option grant ES-10". It has no amounts. It makes "Carta is the record" cover all four advisor lines. Today ES-8/ES-10 rest only on the ledger tie and the advisor table, which a cold P1 could call thin. Expect it to raise landing by about +5–10 pts, because runs grep Carta for ES-8/ES-10.
  3. Do not add a rule that names advisors, the owner list's merge, or any size.

---

## 4. Surface slots ADV decides (01_Gradable_Surface.json; total weight 234)

| Slot | w | Right | Wrong (owner list read as stock) |
|---|---|---|---|
| K1 Series Seed total (sheet) | 5 | 3,051,879 | 3,155,643 |
| K4 Collins stock (ENG-2447) | 5 | 25,432 | 86,470 |
| K5 Segerstråle (ENG-2440) | 5 | 50,865 | 81,383 |
| K6 Nebojsa / PERSON_3941 (ENG-2446) | 5 | 25,432 | 31,536 |
| K7 Deepak / PERSON_1287 (ENG-2449) | 5 | 25,432 | 31,536 |
| P1 live options at clock | 5 | 159,706 | 55,942 |
| A1 KPMG item 2 total | 5 | 243,757 | 139,993 |
| **A2 KPMG item 3** | 5 | 9,295,636 | **9,295,636 (same: does not flip)** |
| K8 Collins grant 61,038 | 3 | 61,038 shown | absent |
| B2 Griffin share of preferred | 3 | 90.0% | 87.0% |
| NC_Collins / NC_Deepak notes | 3+3 | 25,432 | 86,470 / 31,536 |

- A miss flips **7 weight-5 rows (35)** plus 4 weight-3 rows (12), **47/234 = 20%** in all.
- **A2 is tagged ADV but does not change under ADV**, because 3,155,643 + 139,993 = 3,051,879 + 243,757. The platform hardness report already said "Item 3 … unaffected". Re-tag A2 ASOF-only.
- A partial reading that splits only the Carta-visible ES-9 and ES-11 gives K4 and K6 right, K5 and K7 wrong, K1 = 3,088,501, A1 = 207,135, P1 = 123,084, so it still fails K1, A1 and P1.
- KPMG reply, right reading:
  - Item 1: common 6,000,000; Series Seed 3,051,879 (Griffin II 2,662,255, Side Fund 84,438, others 305,186).
  - Item 2: 16 lines, 243,757. That is 81,702 vested on lines terminated on or before Dec 31, plus 58,291 in full for the Jan 30 lines, plus 103,764 for the advisor lines (61,038 / 30,518 / 6,104 / 6,104).
  - Item 3: 9,295,636.
- KPMG reply, wrong reading: Series Seed 3,155,643; 12 lines, 139,993; 9,295,636.

---

## 5. Cold landing estimate (Opus 5.5, reads broadly)

| Overlay state | P(ADV lands) |
|---|---|
| Current fd51afbf63aa (L1 + L2 in place) | ≈ 80–90% (the KPMG figure plus the #executives sentence hand over the conflict and the rule) |
| L1 last sentence cut, L1 numbers kept, L2 kept | ≈ 60–70% |
| **L2 removed + L1 reduced to a numberless "go by the ledger" reply** | **≈ 35–50%** |
| L1 and L2 both deleted, no bridge (close to rev1p) | ≈ 15–25% (the platform run missed it with the ledger and the table both one click away) |
| Option 2 Carta digest added to either un-pointed state | +5–10 pts |

- **Fairness verdict:** FAIR without the leaks. Both deciding records (the advisor table, in Docs 262 and Gmail …1773160163779741845, and the ledger, Docs 40) are body text Leonard can see. They are found by ordinary searches (`103,764`, `advisory`, `ledger`, `cap table`, `Series Seed`), and three exact tie-outs make the split the only consistent reading. The PDF exhibit is not needed and is unobservable.
- **Remaining UGT risk for the cold P1:**
  - If the reviewer never opens the ledger, F3 (Series Seed total) and N1 (rows vs total) reopen as forks.
  - ES-8/ES-10 have no Carta line.
  - "advisory shares" wording in the 2023 Slack could suggest stock. The ledger's common of exactly 6,000,000 and the options count of 268,772 settle this.
- Run the cold P1 on the un-pointed SQL, and attack F3/N1/F15 first.
