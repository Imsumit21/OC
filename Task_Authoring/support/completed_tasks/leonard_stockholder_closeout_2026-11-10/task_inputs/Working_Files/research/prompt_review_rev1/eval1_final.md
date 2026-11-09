## PROMPT EVALUATION REPORT (Eval 1, main reviewer, final on SQL rev2)

### Task: Leonard's stockholder close-out during the wind-down: holder sheet, investor letter, holder note drafts, Linear holder issues, Griffin heads-up, #winddown reply, KPMG audit confirmation
### Assigned Persona: Leonard Hayes - Co-founder & Creative Director (leonard_hayes, leonard.hayes@harmonygames.co, Executive)
### Assigned Business Function: Executive
### Assigned Competency: Finance
### Assigned Task Skill: Authoring
### Assigned Horizon: Long Horizon (long-horizon)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

---

### Scope and fingerprints

| Item | Value |
|---|---|
| Review | Local Eval 1 run, main reviewer. Phases 1–4 (draft `eval1_main_draft.md` on SQL rev1), then deep_recheck.md steps 2–5 applied to the pass findings and re-run on SQL rev2. Review date 2026-11-08. |
| Prompt | `inputs_rev2/04_Prompt.txt` sha256 45766344a3e48641af4dae0cf72c30c0c9c2d3affe3b62e3fdf56f26dbe83bd9 (unchanged from rev1, 134 words) |
| SQL reviewed | `inputs_rev2/01_Universe_Inject.sql` sha256 **e545b426aae5786bad5c826f73cfbb06e1cae530feffc3bf6f47d450f2499005** (125 INSERT, 11 UPDATE). Read in full for every changed and added statement (diff vs rev1 6f3b1899…: 11 hunks). |
| Assignment, date | unchanged (sha 49d5e1d5…, 8d7fc69b…) |
| Universe | normal, `hg4-2026-08-31-v37.zip`; manifest sha256 5e01ac44…e450 |
| Pass inputs merged | P1.md (UGT/Clarity, 9 forks), P2.md (DR1–DR5), P3.md (none), P4.md (DR-P4-1…5), eval0.md (PASS on 6f3b1899, O-1…O-7). All ran on SQL rev1. |
| Search | `Task_Authoring/tools/hg.py search/records` only. No Evals-store writes, no Universe_* reads, SQL not executed. |

### Injection Gate
- State: **STALE**. Eval 0 PASS / COMPLETE covers sha 6f3b1899 (rev1) only. Rev2 (e545b426) has not been through Eval 0 and must be before upload.
- My targeted static checks on the rev2 changes (not a full Eval 0):

| Change | Check | Result |
|---|---|---|
| Notes doc body | Length 2,202 = style-run end 2202 | Consistent |
| New Slack message 846a70ba… | In #executives C07C2866011; author EMPLOYEE_0038 (Leonard, a member per `channels.json`); ts 1768418331 = created_at 2026-01-14T19:18:51Z, after the four off-by-2 posts it corrects (18:44, 19:09, 19:16, 19:17Z); id unused (lookup over 687,230 messages, complete) | Consistent |
| Robert's Board-position reply | Message-ID `<CAGkro_Tn7wQ2x…>` unused (full Gmail scan, 88,726 files); the three target threads exist (leonard …_1856958794180374704, robert `threads/00016903.json`, blake …_1856959418725253571); 22:38:16Z follows Leonard's 22:14:52Z reply it quotes | Consistent |
| Contact db57e559… | Exists ("Matthew Collins"); new job text and updated_at 2025-05-02 follow his 2025-05-01 resignation mail | Consistent |
| ENG-2447 / ENG-2460 retitles | Identifiers unchanged | No collision impact |

- Eval 0 advisories carried (not scored): O-1, the 4 snapshot-missing columns, applies unchanged to rev2.

---

## Deep Recheck

Step 2 (open every cited record; CONFIRMED / REJECTED on rev1) and the rev2 re-test. A UGT finding counts as resolved only on a quoted prompt sentence or persona-visible record.

| Finding | Rev1 decision (reason) | Rev2 status (record that settles it) |
|---|---|---|
| **Main F-1**: ENG-2447 "[PERSON_NAME_11362]" has no persona-visible identity or email; only mapping doc 490 is hidden | CONFIRMED | **RESOLVED.** <br>• SQL L176 retitles ENG-2447 "Husnu Matthew Collins", the exact Carta name in Leonard's mailbox ("Leonard Hayes signed certificate SSP-10 … for Husnu Matthew Collins", …_1777100628672295991; "option grant ES-9 for Husnu Matthew Collins", …_1782897835407336831). <br>• Email: not on the May 2024 investor-report BCC, so "the email we have" applies: Contacts `/contacts/159` Matthew Collins, matthew.collins@harmonygames.co. <br>• Holdings: Leonard's Jun 7, 2023 mail (…_1767980387254277674) says "Matthew Collins … will top-up the angel allocation with $25K … advisory shares … vesting over 2 [years]". #executives (be1e0cb8) gives "~$25,000 / $0.9830 = ~25,432 Seed shares". The allocation mail (…_1773160163779741845) gives "Matthew Collins … 61,038". The issue's own comment says "Nov 2024 owner list: 86,470". All are Leonard-visible. |
| P1 F1: notice route (side letter vs IRA/Voting Orrick copy; side letter void on winding-up) | CONFIRMED | **RESOLVED.** Notes (SQL L19): "Notice route: the email we have. The only extra is Tor's side letter, which Segerstrale signed too: a copy to Tor's lawyers." "Only extra" excludes the Orrick reading, and asserting the side letter excludes the void-on-winding-up reading. "Segerstrale signed too" is backed by …_1774541878774535160, where TOR asks "are you ok for the side letter to include [PERSON_NAME_0089]'s entity as well?". |
| P1 F2: directors in office (Leonard vs Leonard + Robert) | CONFIRMED | **RESOLVED.** Robert's new reply on the Board position thread (SQL L96, 2026-02-12 22:38Z, Leonard cc): "That leaves Leonard and me on the board to see the close through." Contacts L115 "left the board May 2025" removes Matthew Collins. |
| P1 F3 / P2 DR1: Series Seed total 3,051,881 vs 3,051,879 | CONFIRMED (no ranking record in rev1) | **RESOLVED.** KPMG clarification (SQL L86): "our prior-year file has 6,000,000 common and 3,051,879 Series Seed; if nothing has been issued since, those carry over". Leonard's #executives correction (SQL L52): "the seed figures in these are 2 off, the ledger has 3,051,879 seed preferred and 305,186 for the other seed investors". The 3,051,881 posts are now a documented, superseded figure. |
| P1 F4: Griffin heads-up content and recipients | CONFIRMED | **RESOLVED.** Notes: "a reply to all on the Feb 12 Board position thread, asking for their vote as preferred holders on the dissolution." Reply-all on the latest message (Robert's) or on Leonard's reply gives the same set: PERSON_4337, PERSON_2847, Robert, Arthur. |
| P1 F5: "the email we have" with two addresses (Arthur Schaeppi, [PERSON_NAME_4468], TOR); none for [11362] | CONFIRMED | **RESOLVED for investors.** Notes: "Messages go to the address on my investor update list if they're on it, otherwise the email we have." The one investor update mail is the May 18, 2024 "Investor Report" (…_1799418746420547240, Leonard SENT), whose BCC gives: <br>• PERSON_0693 for [4468] (signature "via email: PERSON_0693_EMAIL", …_1773213846196143460) <br>• PERSON_3063 for Arthur Schaeppi ("Arthur PERSON_3083_NAME … PERSON_3063_EMAIL", …_1770053656612413311) <br>• PERSON_5275 for TOR <br>• PERSON_1287, PERSON_2260 <br>[11362] is covered by the F-1 row. **Residual, a new class: N-1 below.** |
| P1 F6: KPMG option lines (vested vs granted for terminated lines) | CONFIRMED | **RESOLVED.** Clarification: "For item 2, a line terminated on or before the as-of date counts only what had vested by its termination date." The Jan 30, 2026 terminations therefore count in full at 12-31. My computed total: 81,702 (≤12-31 terminations, vested) + 58,291 (Jan 30 lines, full) + 103,764 (advisor grants 30,518 / 61,038 / 6,104 / 6,104) = 243,757; item 3 = 9,295,636. |
| P1 F7: ENG-2460 told? (letter to "brian") | CONFIRMED (weak) | **RESOLVED.** <br>• SQL L254 retitles ENG-2460 "Brian Foster". <br>• Mapping to Carta ES-15 "[PERSON_NAME_2769] [PERSON_NAME_0093]": DocuSign "Hello [PERSON_NAME_2769] [PERSON_NAME_0093] … Employment Agreement Brian Foster software.pdf" (…_1822433132018595925), and the option-issuance mail "Full Legal Name: [PERSON_NAME_2769] [PERSON_NAME_0093] / Number of Shares: 10,173 / Email: PERSON_4243_EMAIL" (…_1782034095239486005). <br>• The Feb 11 letter went to "brian <PERSON_4243_EMAIL>", so he is told and his label is "Last day". |
| P1 F8: counts by rows or persons | CONFIRMED (figure) | **RESOLVED.** Notes: "One row per issue on the sheet, and the counts go by rows." |
| P1 F9: "27 holders" in the outline | CONFIRMED (figure) | **RESOLVED.** Slide now "Holders, per the Nov 2024 owner list" (SQL L41), with no figure. The newer notes ("bring it up to date"; "Carta is the record") govern content; the outline only "has the sections". |
| P2 DR2: Nov 2024 owner list says "(Total ownership percentage adds to 100%)" but its lines sum to 94.125% | CONFIRMED (base record; Leonard's own draft doc 167 has the missing "Shares Available under 2023 Stock Plan - 5.874%" line) | **Mitigated, residual risk.** SQL L26 adds an in-universe note to "Holder list (draft)": "the list's percentages leave out the option pool, so they only add to about 94%". The percentages feed no graded value. Not scored; optional hardening fix #3. |
| P2 DR3: letters "January 31, 2026/2025" vs Carta "Jan. 30, 2026" | CONFIRMED (base) | **RESOLVED as designed.** Notes: "Carta is the record, over any date in the letters." KPMG item 2 also says "as Carta shows it". No graded value moves. |
| P2 DR4: Matthew Collins contact still "Independent Director" | CONFIRMED | **RESOLVED.** SQL L115 job = "Investor and advisor (left the board May 2025)". |
| P2 DR5: three advisor agreements hidden from Leonard | CONFIRMED (hidden), conditional | **Advisory.** Vesting for the advisor rows is visible elsewhere: the Jun 7, 2023 mail ("happy with 0.5% each vesting over 2" years, for [PERSON_NAME_6550] and Matthew Collins), and PERSON_3941's own agreement (doc 160, shared with Leonard: "monthly over a 2-year period"). Every 2023-start two-year schedule is complete by Feb 2026. PERSON_1287's term is only inferable from the same form. Optional fix #4. |
| P3 | none | none (prompt unchanged) |
| P4 DR-P4-1: S4 inventory sentence | CONFIRMED as soft flag (0 of 4 spec-register triggers) | Unchanged; Naturalness stays PASS. |
| P4 DR-P4-2: heads-up destination left to the notes | CONFIRMED minor (named recipient; the incorporated notes name the thread) | Unchanged; not a hidden-destination fail. |
| P4 DR-P4-3: heads-up as a holder message (draft vs send) | REJECTED (notes: "That one can go out once the sheet is done") | n/a |
| P4 DR-P4-4: share step not in S4 | REJECTED ("the way those lay it out" incorporates "Share it and the letter with Robert" and the Slack "the sheet goes to you as well as Robert") | n/a |
| P4 DR-P4-5: framing reuse | Advisory | Advisory |
| Eval 0 O-2: identity conflation (patrick@ shared by Patrick Lewis and [4468]; PERSON_3083 token) | CONFIRMED (PLATFORM: anonymized tokens) | Defused for drafts by the investor-list rule ([4468] → PERSON_0693; Patrick Lewis is Covered by the family note). |
| Eval 0 O-6: Carta completeness vs 26 issues | Checked | 26 issues = 27-owner Nov 2024 list − 3 founders + Griffin split into 2 + lapsed [PERSON_NAME_0100]. Every Carta SSP/ES line maps to an issue. |
| Main A-2 (new vs draft sheet) / A-3 (Griffin ask) / A-4 (token drift) / A-5 (letter dates) | — | A-2: rubric-acceptance note. A-3: resolved by F4. A-4: no unmapped Carta holder remains (see O-6). A-5: resolved by the DR3 row. |

### New on rev2 (my re-test)

**N-1 (open, NON-FAIL): "otherwise the email we have" names two addresses for the former team's notes.**
- Affected holders and their two addresses:

| Holder | Contacts (company) | Personal |
|---|---|---|
| Martin Walsh | martin.walsh@ | PERSON_4363 |
| Claire Morgan | claire.morgan@ | PERSON_2360 |
| Brian Foster | brian.foster@ | PERSON_4243 |
| Owen/[PERSON_NAME_0068] | owen.baker@ | PERSON_3140 |
| Oliver Brooks/ES-18 | oliver.brooks@ | PERSON_1174 |

- None of these holders is on the investor list.
- The company addresses sit in Contacts (`contacts.json`, e.g. "Martin … martin.walsh@harmonygames.co").
- The personal addresses come from the Feb 11 letters, and the Oct 22, 2024 issuance mail lists "their personal email addresses" (…_1782034095239486005: "Email: PERSON_1174_EMAIL" for Oliver Brooks). #winddown [69] adds "I'll … send them to their personal accounts".
- Both addresses reach the same person with the same contents. By common_errors §6.2 and Eval 1 §2.6 that is a channel-to-the-same-recipient variation: Clarity NON-FAIL, not UGT. The rubric must accept either address unless fixed. Fix #1.

**Other checks (no finding):**
- "The three of us" vs Frederick Stone: Eval 0 maps PERSON_3941 to Frederick. ENG-2446 exists for him under "one issue per holder on Carta … the three of us aside", and Robert's Feb 12 note treats him as a backer. So "the three of us" stays Leonard, Robert, Arthur.
- Letter outline "Holders, per the Nov 2024 owner list" is settled by the newer notes.
- The TOR note gets no copy to Tor's lawyers. The notes separate "Messages go to…" from "Notice route…", and Sunset says the notes "don't need to double as notices".

Platform defects: PLATFORM:anonymized-tokens (e.g. ES-3 "[PERSON_NAME_0029] [PERSON_NAME_0047]" = Calvin Price; ES-16 body "EMPLOYEE_0032 [PERSON_NAME_0011]"). Not scored.

---

### Unique Ground Truth (rev2), two-reading summary

| Fork | Reading A | Strongest B | Resolution |
|---|---|---|---|
| ENG-2447 identity | Husnu Matthew Collins: 25,432 Series Seed + 61,038 options (all vested); Closing; note to matthew.collins@harmonygames.co | Unmapped token, extra Carta holder | Settled by the SQL L176 title matching the Carta digests, plus the mails cited in the F-1 row |
| ENG-2460 identity / told | Brian Foster = ES-15; told Feb 11; Last day 2026-03-31 | Not told, so Closing and last day | Settled by …_1822433132018595925 and …_1782034095239486005 |
| Directors / preferred vote | Leonard and Robert; Griffin holds the preferred vote | Leonard only, or with Matthew Collins | Settled by SQL L96 |
| Heads-up | Reply-all on Board position; ask for Griffin's preferred vote on the dissolution | Other asks or recipients | Settled by notes |
| Seed / options totals | 3,051,879; 243,757; 9,295,636 | 3,051,881; granted-based totals | Settled by SQL L86 + L52 |
| Notice-route cells | Email; TOR and Segerstråle + copy to Tor's lawyers | Orrick copy for all, or side letter void | Settled by notes + …_1774541878774535160 |
| Investor note recipients | Investor-report BCC address | Correspondence address | Settled by notes |
| Former-team note recipients | Personal or company address | (same person) | **N-1: channel only, Clarity** |
| Counts | By rows (Already told 4) | By persons (3) | Settled by notes |
| Who goes first | [PERSON_NAME_0051] (2026-02-21) | – | Settled by S3 rule + Carta …_1856960478782792748 |
| Sheet file | New sheet or rework "Holder list (draft)" | – | Same material result (rubric accepts either) |

UGT: **PASS (5)**. Every material fork is settled by a quoted, Leonard-visible record. The remaining variation (N-1) is a same-recipient address choice and is scored under Clarity.

---

### Phase 4: Final scoring (SQL rev2, prompt unchanged)

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | All P1 forks and F-1 settled by rev2 records (table above) |
| Prompt | Feasibility | 5 | Every write cataloged; every holder's identity, holding, last day and address is in persona-visible records |
| Prompt | Persona ACL Reachability | 5 | Required reads are in Leonard's mailbox, his Drive, shared files, #winddown and #executives. Hidden advisor agreements are not needed (DR5 advisory). |
| Prompt | Explicit Tool Mention | 5 | No tool, parameter or MCP wording (P4) |
| Prompt | Clarity & Specificity | **4** | N-1: the former team's notes can go to a company or a personal address for the same person. All other writes and act-vs-defer are explicit. |
| Prompt | Contrived / Unnatural | 5 | Natural delegation; S4 inventory is a soft flag only |
| Prompt | Alignment with Today's Date | 5 | "yesterday" = 2026-02-13 KPMG mail; deadlines are future |
| Prompt | Originality / Sample Similarity | N/A | No supplied samples (P4: 0–2 of 7 vs guideline examples) |
| Prompt | Truthfulness | 5 | P3: 23 spans verified, none false |
| Prompt | Tool Use & Cross-service | 5 | Gmail, Linear, Drive family and Slack each change graded facts |
| Prompt | Investigation + Action | 5 | Writes depend on per-holder findings |
| Prompt | Coherence (Bolt-on) | 5 | One workflow keyed to the holder sheet |
| Prompt | Persona | 5 | Executive co-founder acting as CEO |
| Prompt | Business Function | 5 | Founders / Exec (investor and board close-out) |
| Prompt | Assigned Competency | 5 | Finance: cap-table reconciliation, audit confirmation |
| Prompt | Assigned Task Skill | 5 | Authoring: sheet, letter, drafts, replies |
| Prompt | Complexity Dimensions & Data Seeding | 5 | Ambiguity, dynamic change and multi-source all load-bearing; short trigger |
| Universe | Data Exists | 5 | F-1 closed; all core facts retrievable |
| Universe | Cross-Service Coherence | 5 (provisional) | Rev2 injected rows coherent in my checks. DR2 residual risk (base "% adds to 100%"; acknowledged in-universe). Eval 0 on e545b426 pending. |

### Issues Found (rev2)

| # | Issue | Severity | Dimension |
|---|---|---|---|
| N-1 | Notes rule "otherwise the email we have" leaves company (Contacts) vs personal (Feb 11 letters, Oct 2024 issuance mail) addresses open for Martin, Claire, Brian, [0068]/Owen and Oliver Brooks | Minor (NON-FAIL) | Clarity 4 |
| R-1 | Base owner list (…_1816809274978043917) still says "(Total ownership percentage adds to 100%)" over lines summing to 94.125%. Now explained by the SQL sheet note; a strict QC reading of "line items vs total" could still flag it. | Residual risk | Cross-Service Coherence (not scored) |
| R-2 | Eval 0 has not reviewed rev2 | Process gate | Injection Gate |
| A-1 | PERSON_1287's advisor vesting is visible only by analogy (same form as PERSON_3941's) | Advisory | ACL (not scored) |
| A-2 | Rubric must accept a new sheet or a reworked "Holder list (draft)" | Rubric note | — |

### Minimum-fix list (ordered)

1. **N-1 (to reach Clarity 5).** In the close-out notes (SQL L19), change "Messages go to the address on my investor update list if they're on it, otherwise the email we have." to "Messages go to the address on my investor update list if they're on it; for the team, the personal address their termination or grant paperwork used; otherwise the email we have." The style-run end must then become 2202 + the added length. Alternative without SQL: the rubric accepts either address for those holders. Note the cost: the rewrite makes the [PERSON_NAME_0051] and Oliver Brooks rows easier by pointing at the Oct 2024 issuance mail.
2. **R-2.** Re-run Eval 0 on sha e545b426 (O-1 still applies: drop the 4 snapshot-missing columns, or keep them as a disclosed advisory).
3. **R-1 (optional hardening).** UPDATE the base owner-list message body in Leonard's and Arthur's copies (…_1816809274978043917 and blake …_1816806726955267951). Add the line "Shares Available under 2023 Stock Plan – 5.874% diluted ownership" before "(Total ownership percentage adds to 100%)", so the record reconciles on its own. The SQL sheet note can then stay as is.
4. **A-1 (optional).** Share PERSON_1287's advisor agreement (gdrive f_7982b7ac6db8b5e2b7840a + its gdocs row) with leonard.hayes@harmonygames.co, or leave as is.

No prompt edit is recommended. The bytes are unchanged and every prompt-wording dimension scores 5.

---

### FINAL VERDICT: NON-FAIL

Execution status: PARTIAL

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort as configured (runtime does not state the effort level)

Next action:
1. Apply fix #1, or accept either address in the rubric.
2. Run Eval 0 on the final SQL.
3. Merge the P1/P2 re-checks on rev2.
4. If they return no new confirmed finding and fix #1 is applied, the review closes at PASS 5. Without fix #1 it closes at NON-FAIL 4.

Evidence limits:
- Eval 0 on e545b426 and the P1/P2 rev2 re-checks are pending, so no Score line is given (projected 4; 5 after fix #1).
- `Evals/Docs` PDFs and the Example Task were not re-extracted.
- `render-ugt` was not run (local no-store rule); the UGT table is hand-built.
- The KPMG item-4 narrative and the letter body are open-ended authoring. Acceptance boundaries are their incorporated sources.
- Not every "last written contact" date was reconciled; Eval 0 matched 12 of 26, with no contradiction.

**Lowest Dimension:** Clarity & Specificity, 4. Same-recipient address choice for the former team's notes (N-1).

**Summary:** Rev2 closes F-1 (ENG-2447 is now Carta's "Husnu Matthew Collins", reachable at matthew.collins@harmonygames.co). It also settles every P1 and P2 fork with Leonard-visible records: Robert's board reply, the notes' heads-up, address, notice and count rules, the KPMG Series Seed and item-2 clarifications, the #executives correction and the Brian Foster retitle. The prompt itself is unchanged and clean. One minor same-recipient address ambiguity and the pending Eval 0 on the new SQL stand between this and a 5/5.
