# Hardening Report — card-spend breakdown for Q3 Standard Metrics (revision N+1)

## 1 · Mode, inputs and run validity

MODE B (baseline). Six Opus 5.5 rollouts on SQL cf06db49ab71. The hardened SQL is c4db47d07aea.

| Input | State |
|---|---|
| `07_Baseline_Trajectories/` | 6 files read in full (tool calls and results): run-1 1,749 events / 692 calls, run-2 1,749 / 673, run-3 1,911 / 726, run-4 1,925 / 765, run-5 1,929 / 761, run-6 1,737 / 691 |
| `10_Baseline_Verifier_Results.md` | **missing (empty file)**: no platform verifier results |
| `12_Difficulty_Stats.txt` | **missing**: no platform gate statistics |
| `04_Prompt.txt` | sha256 3ffe1dd19aac, unchanged |
| `08_Oracle_Events.md` | /oe PASS 5 on cf06db49ab71 (values below change; see §11) |
| `09_Rubrics.json` | Claude draft (40 criteria, weight 128), used for local scoring only |
| `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json` | belong to the earlier paid-UA task, so not used |
| Prior `01a_Hardening_Report.md` | paid-UA report, moved to `pre_hardening/01a_Hardening_Report.paid_ua.md` |

Run validity (B0):
- **Model.** Main agent claude-opus-5-5 in every run. Subagents (Agent tool, 6–9 per run) report the same model; no mixed run found.
- **Injection applied.** Seeded records come back in every run: Leonard's email at run-1 · event 4, the card close notes, the feed folder d_e342e9e32a98e7cc2d5d57 at run-1 · event 52, card #481.
- **Completeness.** Every run ends after its gmail_reply_to_message (run-1 · event 1745, run-2 · 1741, run-3 · 1907, run-4 · 1917, run-5 · 1922, run-6 · 1733). No result arrives after the final answer, and no compaction was found.
- **File mapping.** File order is used (run-1 … run-6), because no verifier file exists to map by content.

## 2 · Gate status, clean average and mechanism share

The platform numbers (`12`) are unavailable. These are **local** scores against the draft rubric, computed from the full write payloads (workbook cells, reply body, Trello and Linear text). They are not verifier output.

| Run | Local score | Fails |
|---|---|---|
| run-1 | 123/128 = 96.1% | 24 (recipients) |
| run-2 | 123/128 = 96.1% | 24 |
| run-3 | 123/128 = 96.1% | 24 |
| run-4 | 123/128 = 96.1% | 24 |
| run-5 | 123/128 = 96.1% | 24 |
| run-6 | 118/128 = 92.2% | 24, 32 (Sensor Tower) |
| Average | **95.4%** (raw = clean; no confounded row) | SD ≈ 0.015 (Spread Too Low) |

- **Mechanism weight share:** 10/128 (7.8%). Only the recipients row and the Sensor Tower row depend on a landed mechanism.
- **Score shape:** "Uniform success". The rules sit where Opus reads first, the cohort is mechanical, and the one rarely-opened source (the DM) carries only 5 weight.

## 3 · Predicted `/hardness` band (median run, run-3)

Requirement map:
- **MET:** feed breakdown, ledger tie-out, by vendor, by category, run-rate, disputed charges, card #481, ENG-2370 (run-3 · events 1859–1902).
- **MATERIAL_FAIL:** reply recipients. run-3 · event 1907 is gmail_reply_to_message with reply_all false, which reaches Leonard only. Leonard's DM D05S58U4SAK/1759248331.512089 adds Robert and keeps Arthur, and the run never read it.

Band 3: one consequential failure (the summary misses two of the three people it was meant for), and the correction is bounded (re-send). It is not band 4, because every figure and every write is correct.

## 4 · Designed-difficulty register (verdicts on the baseline)

| Node | Mechanism | Verdict | Counts (L · C · Lk · B · NR) | Evidence |
|---|---|---|---|---|
| N1 Recipients | "I'll tell you who else needs the reply" → Sep 30 DM | LANDED | 6 · 0 · 0 · 0 · 0 | run-1 · event 1745, run-3 · event 1907: reply_all false. No call touches D05S58U4SAK in any run |
| N2 Sensor Tower keep | Sep 23 checklist "cancel" vs Sep 26 thread reply | LANDED 1, LEAKED 5 | 1 · 0 · 5 · 0 · 0 | run-6 · event 1659 searched #executives on 9/23 only (parent, not the Sep 26 reply) and wrote "cancel still to do" at run-6 · event 1723. Others read the thread (run-1 · event 205) |
| N3 Griffin's categories over the 2024 list and Robert's "all under software" | forwarded note | LEAKED | 0 · 0 · 6 · 0 · 0 | run-3 · event 8 reads the forward; all six category totals match |
| N4 June/July tie-out | rule 4 | LEAKED | 0 · 0 · 6 · 0 · 0 | run-2 reply at run-2 · event 1741 states 12,222.02 + 12,132.35 = 24,354.37 |
| N5 Unity Ads reclass | rule 7 | LEAKED | 0 · 0 · 6 · 0 · 0 | run-4 reply at run-4 · event 1917 |
| N6 Heroic 420 vs the 600 charge | ENG-2370 Sep 24 comment | LEAKED | 0 · 0 · 6 · 0 · 0 | run-1 · event 155 reads the comment; all run-rates 3,334.78 |
| N7 Midjourney refunded vs not | adjustments tabs | LEAKED | 0 · 0 · 6 · 0 · 0 | run-4 · event 1910 comment names Aug 2 refunded, Sep 2 disputed |
| N8 Envato and Cogency annual | rule 9 | LEAKED | 0 · 0 · 6 · 0 · 0 | run-1 · event 1699 onward: Q4 run-rate tab writes Envato 27.04 and Cogency 25.00 |
| N9 Bank-rule exclusions, Sep 29 edge | rules 2, 3 | LEAKED | 0 · 0 · 6 · 0 · 0 | run-2 · event 1741 reply: Jan–Sep 97,968.21, bank-rule vendors excluded |
| N10 reply_all trap | gmail_reply_to_message cannot add Robert | LANDED, as part of N1 (one cause) | run-5 · event 1922 reply_all false | counted once under N1 |

## 5 · Per-rollout ledgers (summary)

Common shape in all six runs:
1. Leonard's mail is read first (`gmail_search_messages` "from:leonard after:2025/09/28 before:2025/09/30" in runs 1, 2, 5, 6; "… before:2025/10/01" in runs 3, 4; event 2).
2. Drive search for the feed, the close workbook and the folder (events 9–19).
3. Every sheet is read: 505–630 `gdrive_read_file` calls, or 452 + 163 Sheets calls in run-3.
4. Snowflake ledger (2–3 queries).
5. Trello: list, cards, board or card actions. Every run's results contain the vendor-card comments (Canva, Heroic) and the ENG-2370 comments.
6. Slack is limited to the #executives cut-list thread (run-1 · event 205, run-2 · event 463, run-3 · event 374, run-4 · event 394, run-5 · event 527; run-6 only a date search at run-6 · event 1659).
7. Gmail vendor searches with keyword lists.
8. Writes at the end: workbook (run-1 · event 1699), Trello (run-1 · event 1729), Linear (run-1 · event 1731), reply (run-1 · event 1745).

What no run did: open any Slack DM, Calendar, Confluence or Contacts. Every reply used gmail_reply_to_message with reply_all false.

## 6 · Friction, tool-defect and horizon checks

- **Friction:** none configured (03_Error_Async_Config.txt). No async or forced errors.
- **Tool defects:** none that changed an outcome. run-4 and run-5 stopped background tasks (TaskStop ×5) without losing results.
- **Horizon:** 673–765 tool calls per run, well above the Long-Horizon minimum of 100.

## 7 · Verifier sanity (B3e)

Not run: there are no verifier results. The predicted all-fail row is recipients (24): genuine. The DM is visible to Frederick (persona_view check-sql L3120 YES), and gmail_send_message accepts to/cc.

## 8 · Why Opus passed

- **Genuine capability:** scripted full reads of 496 sheets; exact rule application (cycles, fees, adjustments, merges, 1/12 annuals); the ledger tie-out acts as a self-check that catches any feed-arithmetic trap.
- **Universe leak:** every status-deciding fact sits where Opus reads first. Examples: the Heroic price in the first ENG-2370 comment it opens; the Sensor Tower change in the one Slack thread #481 points to; the category list in the forward Leonard names.
- **Prompt leak:** none found.

## 9 · Purge list

- N3–N9 stay (they are correct requirements) but are no longer counted as difficulty. They are mechanical once read.
- Rejected candidate: a second post-cancellation charge on the Sep 29 sheet. Rules 6 and 8 put Sep 29 outside "the last sheet in the window", so it would be unfair (fairness CONFOUNDED by design).

## 10 · Rebuilds (selected nodes)

| # | Node | Characteristic | Discovery-order proof | Survives complete retrieval? | Gradable facts |
|---|---|---|---|---|---|
| H1 | Griffin's open items | The authoritative note itself says two items are still open ("I will confirm where conference passes and engine licences (Unity seats) go before your Q3 submission"). Leonard relays Griffin's answer in the Sep 30 DM | The note (SQL L3042, Frederick's mailbox) is read first in every run; the answer is a later DM (D05S58U4SAK/1759248472.204417) found by searching "Griffin", "conference passes" or the DM | Yes: once the DM is read, the agent must re-map Informa (GDC) and Unity Technologies and recompute | Marketing (non-UA) 3,019.00 · Travel & events 23,043.63 · Software & subscriptions 8,361.12 · Hosting & infrastructure 27,305.36 · Marketing 2025-02 2,398.00 |
| H2 | Heroic downgrade unconfirmed | Claim met first: the cut-list item "Heroic Labs - downgrade plan" and the plan's $420.00. Rule 8 counts a downgrade only once confirmed, and Arthur's ENG-2370 comment now says Heroic "still have to confirm" | ENG-2370 comment cmt_a37dfbf75e0965ec75d6, Heroic card comment, cut-list item now incomplete | Yes: a per-record judgment under rule 8 | Heroic run-rate 600.00 (latest-cycle purchase) |
| H3 | 1Password 3 seats | Later supersession on the vendor card (rule 8: "a comment on the vendor's card") over Arthur's Sep 25 #481 comment of 4 seats | Leonard's comment of Sep 29 on card 678167bdc481ee214e69886d | Yes: dated supersession across two cards | 1Password run-rate 23.97 (3 × 7.99) |

Coupling: H2 and H3 both change the Q4 run-rate total (3,506.79) and the ENG-2370 comment. H1 changes the category totals in the reply and the workbook.

Lazy-solver check:
- A solver that reads the note, the first ENG-2370 comment and #481 reports 420.00, 31.96 and the old categories.
- Only reading the DM, applying rule 8 to "still have to confirm", and ordering card comments by date reaches the new values.

## 11 · Routing

Universe changes made, SQL cf06db49ab71 → c4db47d07aea (backup `pre_hardening/01_Universe_Inject.card_spend_cf06db49ab71.sql`):

| Statement | Change |
|---|---|
| gmail_messages, Griffin's Aug 12 note (Griffin's original in Leonard's mailbox L3036, Frederick's forward L3042, Leonard's sent copy L3046) | "Two open items: I will confirm where conference passes and engine licences (Unity seats) go before your Q3 submission." added before "These replace the 2024 list." |
| gmail_messages, new, Leonard's mailbox | Griffin's Sep 30 reply (2025-09-30T14:58:20Z) answering both items. Not visible to Frederick; kept for coherence |
| slack_messages, new, DM D05S58U4SAK/1759248472.204417 (2025-09-30T16:07:52Z, Leonard) | "and Griffin answered his two open items on the categories: conference passes go under Marketing (non-UA), not Travel & events, and Unity seats go under Hosting & infrastructure, not Software & subscriptions. Use those for the Q3 numbers" |
| linear_comments cmt_a37dfbf75e0965ec75d6 | now "Asked Heroic Labs for the smaller plan, $420.00/month. They still have to confirm it and which invoice it would start from - I'll post here once they do" |
| trello_actions 68d441ae62c15a01731aed86 (Heroic card) | now "asked Heroic for the smaller plan, waiting on their confirmation - see ENG-2370" |
| trello_check_items 68d2db2c4bf21cc5641b9eb0 | Heroic item complete → incomplete; its completion action 68d441d68feaf92813b5bb76 removed; #481 badge checkItemsChecked 4 → 3 |
| trello_actions, new 68dac5f2a1b3c4d5e6f70812 (1Password card, Sep 29, Leonard) | "3 seats, not 4 - the QA vault login goes too. Confirmed in the admin console: 3 x $7.99 from the Oct bill"; card badge comments 0 → 1 |

Facts that changed (the human re-checks the prompt, OEs and criteria):
- **Categories (Jan–Sep):**
  - Software & subscriptions 26,331.12 → **8,361.12**
  - Hosting & infrastructure 9,335.36 → **27,305.36**
  - Travel & events 25,042.63 → **23,043.63**
  - Marketing (non-UA) 1,020.00 → **3,019.00**
  - Others unchanged; opex total still 96,968.21.
- **Months:**
  - Software 2025-08 11,307.91 → 1,107.91
  - Hosting 2025-01 1,017.12 → 2,127.12; Hosting 2025-09 unchanged at 1,025.84
  - Marketing 2025-02 2,398.00, 2025-03 −399.00
  - Travel 2025-02 1,574.15, 2025-03 3,378.42
- **Run-rate:**
  - Heroic Labs 420.00 → **600.00**
  - 1Password 31.96 → **23.97**
  - Total 3,334.78 → **3,506.79**
- **ENG-2370 items:**
  - Heroic still charged 600.00, downgrade not confirmed
  - 1Password 23.97 from October (3 seats)
- **Unchanged:** feed totals, tie-out, vendor totals, the disputed charge (Midjourney 60.00), card #481 findings, recipients.

Prompt-side defects: none.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| — | none | — | — | — |

Routed observations:
- **OEs:** OE 2, 12, 13, 14, 20, 21, 23, 29, 30, 32, 34 and 35 need the new values (/create-oe-writing check, then /oe).
- **Rubric:** P14, P15, P17, P18, P26, P27, P29, P38 and P40 change values; add a Q4 1Password row and two Marketing rows (/create-rubric-writing check).
- **Injection gate:** 01_Grounding_Dossier.md and 01_Hardness_Manifest.json are still the paid-UA files, so the local injection gate cannot certify this SQL. Platform /injection is the check of record.

Projected average on the hardened universe (assumptions, not measurements):

| Mechanism | Rows (weight) | Assumed miss | Expected loss |
|---|---|---|---|
| N1 recipients | 5 | 1.0 (6/6 baseline) | 5.0 |
| H1 Griffin answers (in the unread DM) | 4 rows × 5 = 20 | 0.9 | 18.0 |
| H2 Heroic | 5 + 3 | 0.35 | 2.8 |
| H3 1Password | 5 + 3 | 0.30 | 2.4 |
| Run-rate totals (H2 or H3) | 5 + 3 | 0.55 | 4.4 |
| N2 Sensor Tower | 5 | 0.17 (1/6) | 0.85 |

Total ≈ 33.4 of ≈ 149 → **≈ 78% expected**, plausible range 74–83%.
- **Risk:** H1 and N1 share one root cause (the DM). A run that opens the DM recovers both, so scores will be bimodal; that raises SD toward the 0.1–0.3 band.
- **Failure patterns:** H2, H3 and N2 vary independently, which gives ≥ 2 patterns.

## 12 · Self-review

| Check | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| N1 LANDED | holds | Tool: could gmail_reply_to_message not reach Arthur/Robert for a tool reason? | The catalog's gmail_reply_to_message has message_id, body and reply_all only; gmail_send_message takes to/cc/thread_id. The runs chose reply_all false (run-3 · event 1907). The DM exists and is visible (check-sql L3120 YES). Not confounded | none |
| N2 LANDED (run-6) | holds | Run: did run-6 see the Sep 26 reply in a search result? | run-6 · event 1659 searched "in:#executives on:2025-09-23", which returns the parent only; no slack_read_thread call. Its comment at run-6 · event 1723 says "cancel still to do". Genuine retrieval miss | none |
| N3 LEAKED | holds | Was the 2024 decoy ever live? | No run opened Confluence (no confluence call in any run; run-1 · event 205 goes straight to the thread), so the 2024 list was never met → FALSE for the decoy; the 2025 categories stay a requirement | none |
| N4 LEAKED | holds | Was rule 4 stated verbatim where read first (§9 verbatim)? | Yes: close notes rule 4 is read at run-1 · event 11 onward; leak by verbatim rule, not chance | none |
| N5 LEAKED | holds | Did a bulk call carry the answer? | The feed read is a bulk scan, and rule 7 is read verbatim; run-4 · event 1917 shows the reclass | none |
| N6 LEAKED | holds | Was the claim met before the correction? | No: the ENG-2370 comment (run-1 · event 155) gave the confirmed 420.00 directly; rebuilt as H2 | none |
| N7 LEAKED | holds | Did the natural query return the refunds? | Yes: the adjustments tabs are on the sheets every run reads (run-4 · event 1910 cites them) | none |
| N8 LEAKED | holds | Was rule 9 verbatim? | Yes: rule 9 names annual 1/12 and COGENCY GLOBAL INC (SQL L19); run-1 · event 1699 writes both values | none |
| N9 LEAKED | holds | Was the Sep 29 edge live? | Rule 3 states the 29th–28th cycles; every run excludes the Sep 29 sheet (run-2 · event 1741 total) | none |
| H1 fairness | holds | Is Griffin's DM answer incorporated, or an unstated requirement? | Leonard's email names Griffin's note as the category source; the note now says two items are still open and will be confirmed before the Q3 submission, so a careful reader looks for the answer. The answer is in Frederick's DM, found by Slack search. Single end state (both placements are stated) | UGT risk low; recorded |
| H2 fairness | holds | Could a reader treat the plan's $420 as confirmed? | Rule 8: a downgrade counts once the vendor confirms; Arthur's comment says they "still have to confirm"; the cut-list item is incomplete and the Heroic card says "waiting on their confirmation". One reading: 600.00 | none |
| H3 fairness | holds | Does Leonard's comment on the vendor card count, given Arthur is the owner? | Rule 8 lists "a comment on the vendor's card" without an author condition; the comment is later (Sep 29) than Arthur's Sep 25 note and says "Confirmed in the admin console" | none |
| Neighbouring band | band 3 holds | Argue band 4: is the recipients miss material across the result? | One delivery defect; every figure, tab, card and ticket is correct (local scoring 123/128). Band 2 is rejected because Robert, the investor-update reader, never gets the numbers | none |
| Re-verified records | done | Values carried from notes? | Re-read through the SQL (L3036–3046, L3120–3122, L3221, L3291, L3319) and recomputed with scratchpad feed.py, calc.py and cat3.py: cycles unchanged (97,968.21), categories as in §11. persona_view check-sql YES for D05S58U4SAK/1759248472.204417. hg.py confirmed the ledger line FIN-000580 at snowflake.json /tables/38/rows/579 and robert@harmonygames.co at contacts.json /contacts/108 this session | none |
| Mechanical checks | done | — | sql_lint errors 0 (14 pre-existing warnings); base_check PASS (1,654 inserts) on c4db47d07aea | hardness_gate not run: the manifest is the paid-UA file |

Unresolved: platform verifier results and difficulty stats (10, 12) are missing, so all scores here are local. The projected average is an estimate, not a guarantee. The injection-stage local certificate cannot pass until the card-spend dossier and manifest are rebuilt.

## 13 · Next steps

1. Paste the hardened `01_Universe_Inject.sql` (c4db47d07aea) into `/injection`.
2. Re-run `/prompt` (the facts the prompt incorporates changed).
3. Update the OEs and the rubric values (§11), re-run `/oe` and `/create-rubric-writing check`.
4. Re-apply the SQL and run the six baselines; then `/create-difficulty` with the verifier results.

## 14 · Round 3 (2026-10-24): conflicts checked against the last Opus pre-check run

The round-2 pre-check (Run1_trajectory.json, SQL 884b3dadec61, /hardness FAIL 2 Easy) solved every trap.
- It followed Griffin's "I will confirm" into the Slack DM, which also gave it Robert.
- Its Gmail sweeps were run-1 · event 218 (cut-list vendor names) and run-1 · event 223 (cancel/downgrade/subscription/renewal/price).

Round 3 adds five Leonard forwards of vendor emails to him as account owner (rule 8), dated Aug 29–Sep 23. Each note says "not on the board yet". All 30 rows are in Leonard's inbox, his Sent folder and Frederick's inbox.

| Vendor | Forward says | Correct | Last run reported |
|---|---|---|---|
| DocuSign | closes Sep 22, no charge after | run-rate 0; Sep 23 45.00 disputed | 45.00 active, not disputed |
| Deel | workspace closed Sep 2, nothing more charged | run-rate 0; Sep 5 147.00 disputed | 147.00 active, not disputed |
| Webflow | Basic hosting from the Oct 19 charge | 18.00 | 29.00 |
| QuickBooks Online | Essentials from Oct 8 | 60.00 | 90.00 |
| Gusto | Simple from the Oct 1 charge | 106.00 | 142.00 |

New totals: run-rate total 2,957.80. Disputed charges: Midjourney 60.00, LinkedIn 99.99, Deel 147.00, DocuSign 45.00.

Check against every Gmail query in the last run and the six baselines (scratchpad r3/queries.json, Gmail-style matcher):
- **Last run:** 0 hits on all five forwards.
- **Baselines:** one baseline query names docusign (1 hit). Webflow and QuickBooks were hit only via "ending 0417", and that line was removed from both emails.

Replay of the last run's actual writes against 09_Rubrics.json (51 criteria, weight 191):
- **Fails:** 43 weight. That is total 5 and reply total 3; Webflow, QuickBooks and Gusto 15; Deel and DocuSign in the reply 10; Deel and DocuSign on #481 10.
- **Result:** 148/191 = **77.5%**.
- **Assumption:** LinkedIn and Heroic count as caught, because its event-218 query names both vendors.

Not a guarantee:
- A run that searches each vendor by name, or lists all of Leonard's mail, will find the forwards.
- The six-run average depends on how many runs do that.

SQL 67a707837e52 (1,690 inserts): sql_lint 0 errors; base_check PASS; check-sql YES for the five Frederick threads.

## 15 · Round 3 fix after /injection FAIL (rev 35)

/injection rev 35 FAIL found four Check C contradictions with base records:
- Deel: still in use for payroll Sep 26–30, including SVB → Deel $43,733.46.
- QuickBooks: Plus at $115 on Mastercard 5348.
- DocuSign: annual plan renewed Apr 20.
- Gusto: $128 invoices paid by bank transfer.

Root cause: the base universe was never grepped for those vendors before notices were written for them.

Fix (SQL 511160de5518, 1,674 inserts, sql_lint 0 errors, base_check PASS):
- Removed the four forward sets (24 statements).
- Added Arthur's own copy of the Heroic notice (A12) and fixed the LinkedIn snippet quoting (A11).
- Added one sentence to rule 8: "A change the vendor has confirmed counts even before it is on the board." (A14)
- Added a WeWork forward (membership ends Sep 30; base Gmail and Slack have no WeWork billing).

Base footprint checks:
- Clean: WeWork and Namecheap.
- Not usable: Zapier (Leonard plan email), ElevenLabs (Robert's receipts), Calendly (Leonard receipts), Mailchimp (420 billing-word hits).

Values:
- Run-rate total **2,916.80** (Webflow 18.00, WeWork 0).
- Disputed charges: Midjourney 60.00 and LinkedIn 99.99.

Replay of the last Opus run against 09_Rubrics.json (46 criteria, weight 166):
- Fails: total 5, reply total 3, Webflow 5, WeWork 5 = 18.
- Result: 148/166 = **89.2%**. That is above 80%: the four contradicting vendors carried most of the round-3 weight.

## 16 · Round 4 (2026-10-24): feed-only vendors with no base footprint

Renamed three feed vendors that had base billing or account footprints. Same amounts and dates, so feed totals (97,968.21) and the ledger tie-out are unchanged:
- CALENDLY → SAVVYCAL (9 rows)
- MAILCHIMP *MONTHLY → BUTTONDOWN.EMAIL (9 rows)
- ELEVENLABS.IO → MURF.AI (2 rows; Frederick's injected welcome email renamed, sender SVC_9424)

Zapier is kept, because the feed Doc names Zapier as the SVB export tool.

Base grep (all Gmail threads, Slack, Trello, Linear, Confluence, Drive, Contacts) for savvycal, buttondown and murf: only Unity code hits (GetMouseButtonDown).

Added notices:
- SavvyCal closed Sep 4, so the Sep 11 charge of 16.00 is disputed.
- Buttondown shut down Sep 15, so the Sep 21 charge of 20.00 is disputed. Both reach Frederick as Leonard forwards and also sit in Leonard's inbox and Sent folder.
- Murf to Frederick: Basic at 11.00 from the Oct 18 charge.

None of the 34 past Gmail queries returns them.

Values: run-rate total **2,869.80**. Disputed: Midjourney 60.00, LinkedIn 99.99, SavvyCal 16.00, Buttondown 20.00.

Replay of the last Opus run's actual writes against 09_Rubrics.json (51 criteria, weight 191):
- **Fails (43):** total 5 + reply total 3 + Webflow 5 + WeWork 5 + Murf 5 + SavvyCal reply/card 10 + Buttondown reply/card 10.
- **Result:** 148/191 = **77.5%**. The run marked each of these "Active … no change recorded".

SQL a651bf1242da: 1,688 inserts, sql_lint 0 errors, base_check PASS, check-sql YES.
