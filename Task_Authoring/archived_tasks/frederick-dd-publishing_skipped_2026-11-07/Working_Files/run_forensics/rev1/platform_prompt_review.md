## PROMPT EVALUATION REPORT

### Task: Domino Delights publisher model. Frederick runs Leonard's DD publishing ask end to end: status and value for every publisher, a Q4 cash and keep-value view, board work on the DD publishing card, contacts, reminders, drafts, and a reply to Leonard
### Assigned Persona: Frederick Stone - Co-founder
### Assigned Business Function: Executive
### Assigned Competency: Finance
### Assigned Task Skill: Analysis and synthesis
### Assigned Horizon: long-horizon (Long Horizon tier, 100–500+ calls; difficulty mode medium)

## 1. Scope

| Item | Value |
|---|---|
| Review | Chat review of attempt 6aed99b31c89eba1436ef322, `/prompt`, audit mode |
| Review date | 2026-11-06 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Reviewed prompt | `Evals/task_inputs/04_Prompt.txt` (prompt input revision 4, from the `/prompt` attachment `04_Prompt.txt`), 403 bytes |
| Reviewed prompt SHA-256 | `bed2b497fa1ee539a5c9783b7ba01df4f69055c71b40bd5f076557acc2462b54` |
| Review context SHA-256 | `46b1e5fa5cec51a51cfe516e9070d2bf5b48a024a14a2486f146aedb32fee54b` |
| Prompt record SHA-256 | `ec405b0cf53da2b9471df1cb17c931ae82d90ca679850887aa8c66f8ed15fa39` |
| Eval version | `task-quality-v1` (policy `prompt-source-checks-v2`) |
| Eval release SHA-256 | `81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c` |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, 157,581 bytes, SHA-256 `e6aa859bea5fec91dff09ad2d02fe072d46cc6cef964eb12c389c1f5d2212d73` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` (platform record; all five fields present) |
| Error/async config, dynamic context, reference files | None supplied. The prompt points only to environment records, not to attachments |
| Evidence contract | `stage-evidence-v1`; `authority_contract: prompt-incorporation-v1` |

## 2. Input and authority issues

- Intake is complete: the prompt, all five assignment fields (from the platform record), the task date and the injection SQL are saved. No reference attachment is needed.
- `input_manifest.json`: the portal's integrity rules only allow the stage writer to write into `reports/`, and that writer saves only the report. So this stage's manifest entry is recorded here: `{"prompt": {"review_version": "prompt-source-checks-v2", "evidence_contract": "stage-evidence-v1", "inputs": {"prompt": "bed2b497…2b54", "task-details": "949d4d63…a0ca88c", "universe": "189e2ac6…2da5c", "injection": "e6aa859b…2d73"}, "universe_manifest_sha256": "da2f4cf0…ac1a", "reused_evidence": [{"report": "Evals/task_inputs/reports/0_injection.md", "sha256": "ec62983bf02b12b019d0df8bf44f2b516abdd19c32427cb00b55c45abdf4f910", "checks": ["A", "B", "C"], "verified_unchanged": "SQL SHA, universe manifest, schema snapshot 31dcb2b4…5151, id_contracts fc4711ef…4682, lint a8226e2a…448b, Eval 0 e034019b…3eff"}]}}`.

### Injection Gate
- State: `NEVER_REVIEWED` (the helper reads `reports/input_manifest.json`. The `/injection` run could not write that file, because its writer saves only the report).
- Action: the gate's rerun was satisfied by checking that the existing `/injection` report covers this exact SQL. `Evals/task_inputs/reports/0_injection.md` (SHA-256 `ec62983b…f910`, `injection-static-v2`, reviewed 2026-11-06T17:27Z) records SQL SHA-256 `e6aa859bea5fec91dff09ad2d02fe072d46cc6cef964eb12c389c1f5d2212d73`. That is byte-identical to the saved SQL. Every dependency it lists still matches today: universe manifest `da2f4cf0…ac1a`, schema snapshot `31dcb2b4…5151`, `id_contracts.json` `fc4711ef…4682`, lint `a8226e2a…448b`, Eval 0 `e034019b…3eff` and the synth-cut clock. I reran the lint on the saved SQL: same SHA, 178 statements, no flags. Static checks A–C are REUSED under WORKFLOW's whole-injection reuse rule. Task-specific records were still read directly below.
- Reviewed SQL sha256: `e6aa859bea5fec91dff09ad2d02fe072d46cc6cef964eb12c389c1f5d2212d73`. Eval 0 verdict: **PASS** (Execution status COMPLETE).
- Eval 0 findings on records this prompt depends on: none change a graded value, set, order, recipient or destination. Advisories stay here:
  1. Four columns are not in the unverified schema snapshot (`slides_pages.notes`, `slides_page_elements.table_json`, `slides_page_elements.ordinal`, `linear_comments.sequence`). If the live tables lack them, the whole transaction rolls back. Removing them is the safe fix.
  2. The eight externally owned term sheets have `parents_json` = Frederick's private DD publishing folder, where Frederick has reader access only. See Phase 3.2, where this is an advisory, not scored.
  3. Gmail thread-number timestamps, content cited but with no record of its own (Copperleaf email, Redwood email, Kestrel call), and the "(PDT)" invite subjects are informational.

### Dataset Similarity
- Library: refreshed 2026-11-06T17:34Z (0.8 h old), 470 tasks (Enterprise Atlas - Commercial: L10 56, L11 3, L12 184, completed 227). Gate: **PASS**. Nearest tier: **distinct**.
- No identical, likely-duplicate or same-scenario neighbour. Nearest is (hidden) (L12, Frederick Stone, Marketing and GTM / Authoring, meaning 0.599 / wording 0.006). It is also a Domino Delights publisher round, but it is driven by a BD Outreach Rules doc and produces a brief, follow-up cards, a tracker and an #executives post. It is not a valuation model with Q4 cash and a reply. Below the 0.70 same-scenario cutoff.

## 3. Checklist (all NEW unless marked)

| TODO | Status |
|---|---|
| Intake (prompt + five assignment fields + date + SQL) | DONE |
| STEP 0.5 Injection gate | DONE: NEVER_REVIEWED → matching current Eval 0 PASS verified and REUSED (A–C) |
| STEP 0.6 Dataset similarity | DONE: PASS, distinct |
| Phase 0.1 Docs/catalog/scoring | DONE (guide view, Eval 1 in full, catalog write tools, ACL matrix, known data issues) |
| Phase 0.2 Universe exploration | DONE: all 176 SQL row effects read and parsed; base Gmail, Slack, Trello, Contacts, Drive and Snowflake checked for the task's records |
| Phase 0.3 Calibration | DONE (inline Eval and QC examples; no samples supplied) |
| Phase 1.1–1.5 | DONE |
| Phase 2.1–2.9 | DONE (2.9 N/A: no samples supplied) |
| Phase 3.1–3.2 | DONE |
| Phase 4 scoring | DONE |
| Phase 5 deep recheck | DONE (see `## Deep Recheck`) |

## 4. Requirement ledger (`authority_contract: prompt-incorporation-v1`)

Authority chain: prompt ("going by his email for what he wants and how he wants it done") → Leonard's email "DD publishing: what I need for Monday" (Frederick's inbox, 2025-09-30T23:10Z) → ground rules doc `f_5e355d03f6eb6a4e866ead` ("The ground rules doc has how we're doing this") and DD publishing card `68dab660c900179df4f5f92d` ("Do what's on the DD publishing card") → Leonard's Sep 26 #bridge-pitch note (the doc: "Anything I've already said about what goes out to publishers still applies").

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Build the model of what each publisher brings in | Email; ground rules doc (Who's in, Status, Valuing, Q4 cash, Keep value, First pick, Layout); outreach sheet `f_fd467bd2…`; 8 term-sheet docs; Robert's Copperleaf post (#executives); Arthur's #analytics post → ENG-2362 comment (Redwood Arcade); Tallwater call notes (Fred's calendar); Lena call comment (Trello); Kestrel call (#executives); Moonrail signature; lawyer + Leonard Nov 14 emails; Arthur's SVB message; Appodeal thread (Fred's inbox) | Email names the doc and the folder; the doc names the sheet, calls, Aug sync, Leonard's Sep 24 note and REVENUE_DAILY; term-sheet emails say "in your Drive" | `gmail_*` read, `gdocs`/`gdrive` read, `gsheets_values_get`, `slack` search/read, `linear_list_comments`, `trello_get_comments`, `gcal` list, `snowflake_execute_query` | Fred's own mailbox/calendar/folder; docs shared with him; member of #executives, #bridge-pitch, #analytics and DM D05S58U4SAK; Trello/Linear/Snowflake unscoped | 27 publisher rows with statuses; Live figures; first pick Copperleaf |
| Sheet "DD publishing model" in Fred's DD publishing folder, tabs Publishers / Summary | Doc "Layout"; folder `d_6fc54be60d1377e340a5b5` | Email + prompt name the folder | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update`, `gdrive_move_file` (SUPPORTED) | Folder owned by Fred; writes never ACL-blocked | Publishers tab (Publisher, Status, Advance, Monthly installs, 12-month value, Q4 cash; figures only for Live); Summary (Keep value $12,723.96, First pick Copperleaf Games, Banked so far $0) |
| Board work on the DD publishing card | Card desc; existing cards F/up with Marek, F/up with Lena | Prompt + email name the card | `trello_create_checklist`, `trello_create_check_item`, `trello_create_card`, `trello_add_comment` (SUPPORTED) | Trello unscoped | 6 status checklists / 27 items; 15 new F/up cards; status comments on F/up with Marek and F/up with Lena |
| One-line nudge to every No reply publisher in Gmail drafts | Card desc | Card | `gmail_create_draft` (SUPPORTED) | Own mailbox | 7 drafts (Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether partnerships inboxes) |
| Contacts for everyone who gave terms or said no; skip existing | Email | Email | `contacts_search_contacts`, `contacts_add_new_contact` (job field) (SUPPORTED) | Contacts unscoped | 14 new (Marek Sobol, Paola Duarte, Diego Reyes, Sofia Lindqvist, Callum Ross, Elena Petrova, Jonas Weber, Mei Tanaka, Rhys Morgan, Nadia Haddad, Yuki Sato, Tessa Hale, Omar Khalil, Greta Holm); Lena Fischer and Anika Rao skipped (injected contacts exist) |
| Reminders for each Live offer on its response date | Doc "Reminders"; term sheets / pasted offers | Doc | `gcal_create_event` (SUPPORTED) | Fred's calendar | 7 events: Copperleaf and Tallwater Oct 17; Oakline and Harbor Lane Oct 24; Sunfold, Wavecrest and Redwood Arcade Oct 31 |
| Organic-figure notes (still-applicable Sep 26 instruction) | Doc last line → #bridge-pitch note; outreach sheet "May one-pager" column | Search for Leonard's earlier statements on what goes to publishers | `gmail_create_draft` (SUPPORTED) | #bridge-pitch member | 3 drafts with $0.50 D30 ARPI: Tallwater (Paola), Harbor Lane (Diego), Wavecrest (Sofia); not Moonrail (withdrawn, no offer in) |
| Leave out the Sep 24 hypercasual contact | Email; Leonard's Sep 24 DM | Email | n/a (exclusion) | DM member | No row |
| Reply to Leonard on his email | Email | Prompt | `gmail_reply_to_message` (SUPPORTED) | Own mailbox | Copperleaf goes first; $67,200 over 12 months; $32,000 in Q4; $0 banked so far |

Facts versus obligations: Snowflake `ANALYTICS.MONETIZATION.REVENUE_DAILY` (DD total_revenue_usd: Jul $2,078.33, Aug $721.55, Sep $381.11; average $1,060.33 × 12 = **$12,723.96**; `REVENUE_DAILY_V2` gives the same monthly totals) and the Aug 25 #executives rights position ("retain code, IP and non-mobile distribution rights") are facts for incorporated asks. They add no obligations. No unincorporated policy was used.

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Frederick Stone (roster `frederick_stone`, frederick.stone@harmonygames.co, Co-founder, Executive). He owns the outreach sheet and the publisher threads. Leonard addresses the ask to him, and he is a member of every channel used. A co-founder running the publisher valuation for the founders' Monday sit-down is plausible. Short, delegating voice. The access/role/scope checks all pass.

**Assigned Competency:** PASS (5)
- Finance: the core work is a deal-valuation model with 12-month value, a recoupable-advance comparison, Q4 cash timing from net terms and signature date, banked cash and a keep-value baseline. That is "models/budgets/forecasts".

**Assigned Task Skill:** PASS (5)
- Analysis and synthesis is central. The agent has to reconcile 27 publishers across Gmail, Drive, Slack, Linear, Trello, Calendar and Snowflake, apply a precedence rule, value the offers and rank them. Actions (cards, contacts, drafts, reminders) are stacked on top, which is fine.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. **PASS**
- Dynamic Change (load-bearing): Tallwater's advance $60,000 → $40,000 (Sep 29 call notes); Sunfold 50,000 → 30,000 installs (Sep 30 card comment); signing Oct 31 → Nov 14 (Sep 29/30 lawyer and Leonard emails); Oakline's first-look "went out today" (Sep 29) → "never hit the account" (Sep 30 SVB check). Each stale value sits in the most obvious record (term sheet, the doc's default, Marek's email).
- Multi-Source: the set and terms are split across Drive, Gmail, Slack, Linear, Trello, GCal and Snowflake, with decoys: the outreach sheet's Appodeal "we applied", Fred's co-dev terms doc, Tamatem, the Sep 24 hypercasual contact, and Homa/NCsoft/Tilting Point.
- Ambiguity: the status of each publisher is planted, not stated.
- Data seeding: **PASS**. The prompt is a four-sentence trigger. All operating rules live in the email, doc and card.

**Naturalness:** PASS (5). First person, casual delegation ("Can you take the whole thing on for me"). No formatting, no polished connectives, no enumerated deliverables. Clean spelling with no staged errors.

**Anti-Patterns:**
| Pattern | Status |
|---|---|
| Command List | PASS: no first/then/finally list |
| Bolt-On | PASS: each sentence (trigger, delegation, destinations, reply) is needed by the others |
| Pre-Solving | PASS: no statuses, figures, publishers or the first pick are given |
| Tool Mention | PASS: "email", "folder", "card", "board" are natural product language |

**Diversity (1.4):** goes well beyond "investigate + post one message". Executive scenario with mixed writes: Sheets, Trello checklists/cards/comments, Contacts, GCal, Gmail drafts and a reply.

## Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2). One decision fork is unsettled: whether the Sep 26 organic-figure notes (3 Gmail drafts to Tallwater, Harbor Lane and Wavecrest) are part of this job (reading A) or the doc's "Anything I've already said about what goes out to publishers still applies" only limits what outgoing messages say (reading D). Deep recheck P1 confirmed it. Every other fork is settled by a quoted record. See the generated comparison below and the fork list in `## Deep Recheck`.

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: UNRESOLVED fork: whether the Sep 26 organic-figure notes (3 Gmail drafts) are part of this job (reading A vs D). Every other material fork the records raise (Moonrail/Kestrel, Appodeal status, Oakline first-look, signing date, call-updated terms, the existing Oakline card) is settled by a persona-visible record or by the incorporated rule itself; all 27 publishers and the excluded candidates get one outcome.

Alternative selection: Alternatives target each place the task's inputs offer two end states: a parent-company withdrawal, a sheet row that contradicts the mailbox, a vague incorporation line, an older payment report, the doc's default date, older term-sheet figures and a card named for a person. G is the strongest because it changes the first pick and the reply.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the email, ground rules doc, card and Leonard's Sep 26 note as written, using the latest terms and the Nov 14 signing date. | 27 rows: 25 outreach-sheet publishers plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Live: Copperleaf (40,000/mo, $32,000, 12-mo $67,200, Q4 $32,000), Redwood Arcade (40,000, $25,000, $57,600, Q4 $25,000), Sunfold (30,000 per Lena call, $20,000, $54,000, Q4 $20,000), Tallwater ($40,000 per call, 30,000, $45,000, Q4 $40,000), Oakline (20,000, $30,000, $36,000, Q4 $30,000), Harbor Lane (25,000, $25,000, $30,000, Q4 $0), Wavecrest (15,000, $15,000, $19,800, Q4 $0). Withdrawn: Moonrail. Out on rights: Northglow, Pinegrove. Passed: Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play. Waiting on us: Appodeal, Rayking, Kitebridge. No reply: Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether. Signing Nov 14. First pick Copperleaf. Banked $0. Keep value $12,723.96. | Sheet DD publishing model (Publishers, Summary tabs); 6 status checklists with 27 items on the DD publishing card; 15 new F/up cards (Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood Arcade, Appodeal, Rayking, Kitebridge and the 7 No reply publishers) plus status comments on F/up with Marek and F/up with Lena; 14 new contacts (Marek, Paola, Diego, Sofia, Callum, Elena, Jonas Weber, Mei Tanaka, Rhys, Nadia, Yuki, Tessa, Omar, Greta), Lena and Anika skipped; 7 calendar reminders on response dates; 7 No reply nudges and 3 organic-figure notes (Tallwater, Harbor Lane, Wavecrest) in Gmail drafts; one reply on Leonard's email. | DD publishing folder; UA/BD board, BD Follow Up list and DD publishing card; Contacts; Frederick's calendar; Frederick's Gmail drafts; Leonard's DD publishing: what I need for Monday thread. | Reply: Copperleaf goes first, $67,200 over 12 months, $32,000 in Q4, $0 banked so far. | P (Evals/task\_inputs/04\_Prompt.txt): "Leonard's email from yesterday asks me to model what each publisher would bring in for DD before we all sit down on Monday. Can you take the whole thing on for me, going by his email for what he wants and how he wants it done? The model goes in my DD publishing folder, and the board work he mentions is on the DD publishing card. When it's all in, reply to Leonard on his email with what he asked for."; EMAIL\_RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 112-112): "The ground rules doc has how we"; R\_WHO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Every publisher on Fred''s outreach sheet, plus any publisher that came to one of the four of us about Domino Delights since Apr 1, 2025, however it reached us. A name someone passed along doesn''t count unless they came to us."; R\_LATEST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Use the latest terms we have from them, wherever they are, calls included."; R\_Q4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Advance money that lands between Oct 1 and Dec 31, 2025. Assume we sign on Oct 31. If our lawyers give us a later date, use theirs. A payment on net terms lands that many days after signature."; CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 104-104): "One checklist per status on this card, one item per publisher."; R\_OUT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Anything I''ve already said about what goes out to publishers still applies." |
| B | Moonrail stays Live: Robert's Kestrel call is read as another company, not Moonrail. | 27 rows: 25 outreach-sheet publishers plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Live: Copperleaf (40,000/mo, $32,000, 12-mo $67,200, Q4 $32,000), Redwood Arcade (40,000, $25,000, $57,600, Q4 $25,000), Sunfold (30,000 per Lena call, $20,000, $54,000, Q4 $20,000), Tallwater ($40,000 per call, 30,000, $45,000, Q4 $40,000), Oakline (20,000, $30,000, $36,000, Q4 $30,000), Harbor Lane (25,000, $25,000, $30,000, Q4 $0), Wavecrest (15,000, $15,000, $19,800, Q4 $0). Moonrail Live (35,000, $30,000, 12-mo $54,600, Q4 $30,000); no Withdrawn row. Out on rights: Northglow, Pinegrove. Passed: Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play. Waiting on us: Appodeal, Rayking, Kitebridge. No reply: Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether. Signing Nov 14. First pick Copperleaf. Banked $0. Keep value $12,723.96. | Sheet DD publishing model (Publishers, Summary tabs); 6 status checklists with 27 items on the DD publishing card; 15 new F/up cards (Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood Arcade, Appodeal, Rayking, Kitebridge and the 7 No reply publishers) plus status comments on F/up with Marek and F/up with Lena; 14 new contacts (Marek, Paola, Diego, Sofia, Callum, Elena, Jonas Weber, Mei Tanaka, Rhys, Nadia, Yuki, Tessa, Omar, Greta), Lena and Anika skipped; 7 calendar reminders on response dates; 7 No reply nudges and 3 organic-figure notes (Tallwater, Harbor Lane, Wavecrest) in Gmail drafts; one reply on Leonard's email. Plus an F/up with Moonrail Studios card, an Oct 24 reminder and a fourth organic-figure note to Anika. | DD publishing folder; UA/BD board, BD Follow Up list and DD publishing card; Contacts; Frederick's calendar; Frederick's Gmail drafts; Leonard's DD publishing: what I need for Monday thread. | Reply: Copperleaf goes first, $67,200 over 12 months, $32,000 in Q4, $0 banked so far. | KESTREL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 86-86): "Got a call from Kestrel. They''ve frozen every outside signing for the year, so whatever they had on the table with us is off."; TS\_MOON (Evals/task\_inputs/01\_Universe\_Inject.sql lines 49-49): "26% of net to Harmony Games\\n$30,000 advance net 30 from signature\\n35,000 installs a month for 12 months" |
| C | Appodeal is No reply: the sheet says we applied through their intake form and nothing came back. | 27 rows: 25 outreach-sheet publishers plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Live: Copperleaf (40,000/mo, $32,000, 12-mo $67,200, Q4 $32,000), Redwood Arcade (40,000, $25,000, $57,600, Q4 $25,000), Sunfold (30,000 per Lena call, $20,000, $54,000, Q4 $20,000), Tallwater ($40,000 per call, 30,000, $45,000, Q4 $40,000), Oakline (20,000, $30,000, $36,000, Q4 $30,000), Harbor Lane (25,000, $25,000, $30,000, Q4 $0), Wavecrest (15,000, $15,000, $19,800, Q4 $0). Withdrawn: Moonrail. Out on rights: Northglow, Pinegrove. Passed: Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play. Waiting on us: Rayking, Kitebridge. No reply: Appodeal, Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether. Signing Nov 14. First pick Copperleaf. Banked $0. Keep value $12,723.96. | Sheet DD publishing model (Publishers, Summary tabs); 6 status checklists with 27 items on the DD publishing card; 15 new F/up cards (Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood Arcade, Appodeal, Rayking, Kitebridge and the 7 No reply publishers) plus status comments on F/up with Marek and F/up with Lena; 14 new contacts (Marek, Paola, Diego, Sofia, Callum, Elena, Jonas Weber, Mei Tanaka, Rhys, Nadia, Yuki, Tessa, Omar, Greta), Lena and Anika skipped; 7 calendar reminders on response dates; 7 No reply nudges and 3 organic-figure notes (Tallwater, Harbor Lane, Wavecrest) in Gmail drafts; one reply on Leonard's email. Plus an eighth No reply nudge (to Appodeal) in Gmail drafts. | DD publishing folder; UA/BD board, BD Follow Up list and DD publishing card; Contacts; Frederick's calendar; Frederick's Gmail drafts; Leonard's DD publishing: what I need for Monday thread. | Reply: Copperleaf goes first, $67,200 over 12 months, $32,000 in Q4, $0 banked so far. | SH\_APPO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Appodeal", "their partnerships team", "Apr 17, 2025", "we applied", "Intake form (DAU, ARPDAU)"\]"; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count." |
| D | The doc's line about what goes out to publishers is only a content constraint, so no organic-figure notes are written. | 27 rows: 25 outreach-sheet publishers plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Live: Copperleaf (40,000/mo, $32,000, 12-mo $67,200, Q4 $32,000), Redwood Arcade (40,000, $25,000, $57,600, Q4 $25,000), Sunfold (30,000 per Lena call, $20,000, $54,000, Q4 $20,000), Tallwater ($40,000 per call, 30,000, $45,000, Q4 $40,000), Oakline (20,000, $30,000, $36,000, Q4 $30,000), Harbor Lane (25,000, $25,000, $30,000, Q4 $0), Wavecrest (15,000, $15,000, $19,800, Q4 $0). Withdrawn: Moonrail. Out on rights: Northglow, Pinegrove. Passed: Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play. Waiting on us: Appodeal, Rayking, Kitebridge. No reply: Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether. Signing Nov 14. First pick Copperleaf. Banked $0. Keep value $12,723.96. | Sheet DD publishing model (Publishers, Summary tabs); 6 status checklists with 27 items on the DD publishing card; 15 new F/up cards (Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood Arcade, Appodeal, Rayking, Kitebridge and the 7 No reply publishers) plus status comments on F/up with Marek and F/up with Lena; 14 new contacts (Marek, Paola, Diego, Sofia, Callum, Elena, Jonas Weber, Mei Tanaka, Rhys, Nadia, Yuki, Tessa, Omar, Greta), Lena and Anika skipped; 7 calendar reminders on response dates; 7 No reply nudges in Gmail drafts; one reply on Leonard's email. | DD publishing folder; UA/BD board, BD Follow Up list and DD publishing card; Contacts; Frederick's calendar; Frederick's Gmail drafts; Leonard's DD publishing: what I need for Monday thread. | Reply: Copperleaf goes first, $67,200 over 12 months, $32,000 in Q4, $0 banked so far. | R\_OUT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Anything I''ve already said about what goes out to publishers still applies." |
| E | Oakline's $10,000 first-look counts as paid on Sep 29 (Marek's email and the card comment), so it is banked and not Q4 money. | 27 rows: 25 outreach-sheet publishers plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Live: Copperleaf (40,000/mo, $32,000, 12-mo $67,200, Q4 $32,000), Redwood Arcade (40,000, $25,000, $57,600, Q4 $25,000), Sunfold (30,000 per Lena call, $20,000, $54,000, Q4 $20,000), Tallwater ($40,000 per call, 30,000, $45,000, Q4 $40,000), Oakline (20,000, $30,000, $36,000, Q4 $20,000), Harbor Lane (25,000, $25,000, $30,000, Q4 $0), Wavecrest (15,000, $15,000, $19,800, Q4 $0). Withdrawn: Moonrail. Out on rights: Northglow, Pinegrove. Passed: Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play. Waiting on us: Appodeal, Rayking, Kitebridge. No reply: Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether. Signing Nov 14. First pick Copperleaf. Banked $10,000. Keep value $12,723.96. | Sheet DD publishing model (Publishers, Summary tabs); 6 status checklists with 27 items on the DD publishing card; 15 new F/up cards (Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood Arcade, Appodeal, Rayking, Kitebridge and the 7 No reply publishers) plus status comments on F/up with Marek and F/up with Lena; 14 new contacts (Marek, Paola, Diego, Sofia, Callum, Elena, Jonas Weber, Mei Tanaka, Rhys, Nadia, Yuki, Tessa, Omar, Greta), Lena and Anika skipped; 7 calendar reminders on response dates; 7 No reply nudges and 3 organic-figure notes (Tallwater, Harbor Lane, Wavecrest) in Gmail drafts; one reply on Leonard's email. | DD publishing folder; UA/BD board, BD Follow Up list and DD publishing card; Contacts; Frederick's calendar; Frederick's Gmail drafts; Leonard's DD publishing: what I need for Monday thread. | Reply: Copperleaf goes first, $67,200 over 12 months, $32,000 in Q4, $10,000 banked so far. | MAREK\_WIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 140-140): "sent the $10,000 first-look payment by wire today"; MAREK\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Marek says the $10K first-look payment went out today." |
| F | Signing stays Oct 31 as the doc assumes, so the net-60 advances land in Q4. | 27 rows: 25 outreach-sheet publishers plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Live: Copperleaf (40,000/mo, $32,000, 12-mo $67,200, Q4 $32,000), Redwood Arcade (40,000, $25,000, $57,600, Q4 $25,000), Sunfold (30,000 per Lena call, $20,000, $54,000, Q4 $20,000), Tallwater ($40,000 per call, 30,000, $45,000, Q4 $40,000), Oakline (20,000, $30,000, $36,000, Q4 $30,000), Harbor Lane (25,000, $25,000, $30,000, Q4 $25,000), Wavecrest (15,000, $15,000, $19,800, Q4 $15,000). Withdrawn: Moonrail. Out on rights: Northglow, Pinegrove. Passed: Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play. Waiting on us: Appodeal, Rayking, Kitebridge. No reply: Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether. Signing Oct 31. First pick Copperleaf. Banked $0. Keep value $12,723.96. | Sheet DD publishing model (Publishers, Summary tabs); 6 status checklists with 27 items on the DD publishing card; 15 new F/up cards (Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood Arcade, Appodeal, Rayking, Kitebridge and the 7 No reply publishers) plus status comments on F/up with Marek and F/up with Lena; 14 new contacts (Marek, Paola, Diego, Sofia, Callum, Elena, Jonas Weber, Mei Tanaka, Rhys, Nadia, Yuki, Tessa, Omar, Greta), Lena and Anika skipped; 7 calendar reminders on response dates; 7 No reply nudges and 3 organic-figure notes (Tallwater, Harbor Lane, Wavecrest) in Gmail drafts; one reply on Leonard's email. | DD publishing folder; UA/BD board, BD Follow Up list and DD publishing card; Contacts; Frederick's calendar; Frederick's Gmail drafts; Leonard's DD publishing: what I need for Monday thread. | Reply: Copperleaf goes first, $67,200 over 12 months, $32,000 in Q4, $0 banked so far. | R\_Q4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Advance money that lands between Oct 1 and Dec 31, 2025. Assume we sign on Oct 31. If our lawyers give us a later date, use theirs. A payment on net terms lands that many days after signature." |
| G | Use the term-sheet figures: Tallwater $60,000 advance and Sunfold 50,000 installs a month. | 27 rows: 25 outreach-sheet publishers plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Live: Copperleaf (40,000/mo, $32,000, 12-mo $67,200, Q4 $32,000), Redwood Arcade (40,000, $25,000, $57,600, Q4 $25,000), Sunfold (50,000, $20,000, $90,000, Q4 $20,000), Tallwater ($60,000, 30,000, $60,000, Q4 $60,000), Oakline (20,000, $30,000, $36,000, Q4 $30,000), Harbor Lane (25,000, $25,000, $30,000, Q4 $0), Wavecrest (15,000, $15,000, $19,800, Q4 $0). Withdrawn: Moonrail. Out on rights: Northglow, Pinegrove. Passed: Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play. Waiting on us: Appodeal, Rayking, Kitebridge. No reply: Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether. Signing Nov 14. First pick Sunfold. Banked $0. Keep value $12,723.96. | Sheet DD publishing model (Publishers, Summary tabs); 6 status checklists with 27 items on the DD publishing card; 15 new F/up cards (Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood Arcade, Appodeal, Rayking, Kitebridge and the 7 No reply publishers) plus status comments on F/up with Marek and F/up with Lena; 14 new contacts (Marek, Paola, Diego, Sofia, Callum, Elena, Jonas Weber, Mei Tanaka, Rhys, Nadia, Yuki, Tessa, Omar, Greta), Lena and Anika skipped; 7 calendar reminders on response dates; 7 No reply nudges and 3 organic-figure notes (Tallwater, Harbor Lane, Wavecrest) in Gmail drafts; one reply on Leonard's email. | DD publishing folder; UA/BD board, BD Follow Up list and DD publishing card; Contacts; Frederick's calendar; Frederick's Gmail drafts; Leonard's DD publishing: what I need for Monday thread. | Reply: Sunfold goes first, $90,000 over 12 months, $20,000 in Q4, $0 banked so far. | TS\_TALL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "25% of net to Harmony Games\\n$60,000 advance net 30 from signature\\n30,000 installs a month for 12 months\\nMobile stores\\nRespond by Oct 17"; TS\_SUN (Evals/task\_inputs/01\_Universe\_Inject.sql lines 43-43): "30% of net to Harmony Games\\n$20,000 advance net 45 from signature\\n50,000 installs a month for 12 months\\nMobile stores\\nRespond by Oct 31" |
| H | Oakline has no card yet because no card carries the publisher name, so it gets a new F/up with Oakline Games card instead of a comment on F/up with Marek. | 27 rows: 25 outreach-sheet publishers plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Live: Copperleaf (40,000/mo, $32,000, 12-mo $67,200, Q4 $32,000), Redwood Arcade (40,000, $25,000, $57,600, Q4 $25,000), Sunfold (30,000 per Lena call, $20,000, $54,000, Q4 $20,000), Tallwater ($40,000 per call, 30,000, $45,000, Q4 $40,000), Oakline (20,000, $30,000, $36,000, Q4 $30,000), Harbor Lane (25,000, $25,000, $30,000, Q4 $0), Wavecrest (15,000, $15,000, $19,800, Q4 $0). Withdrawn: Moonrail. Out on rights: Northglow, Pinegrove. Passed: Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play. Waiting on us: Appodeal, Rayking, Kitebridge. No reply: Orchard Lane, Summit, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether. Signing Nov 14. First pick Copperleaf. Banked $0. Keep value $12,723.96. | Sheet DD publishing model (Publishers, Summary tabs); 6 status checklists with 27 items on the DD publishing card; 16 new F/up cards (Oakline Games, Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood Arcade, Appodeal, Rayking, Kitebridge and the 7 No reply publishers) plus a status comment on F/up with Lena only; 14 new contacts (Marek, Paola, Diego, Sofia, Callum, Elena, Jonas Weber, Mei Tanaka, Rhys, Nadia, Yuki, Tessa, Omar, Greta), Lena and Anika skipped; 7 calendar reminders on response dates; 7 No reply nudges and 3 organic-figure notes (Tallwater, Harbor Lane, Wavecrest) in Gmail drafts; one reply on Leonard's email. | DD publishing folder; UA/BD board, BD Follow Up list and DD publishing card; Contacts; Frederick's calendar; Frederick's Gmail drafts; Leonard's DD publishing: what I need for Monday thread. | Reply: Copperleaf goes first, $67,200 over 12 months, $32,000 in Q4, $0 banked so far. | CARD\_FUP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 104-104): "Every Live, Waiting on us and No reply publisher gets a follow-up card on this list, named F/up with plus the publisher" |

Explicit option inventory: The prompt gives no option list; it delegates to Leonard's email. The status list lives in the incorporated doc and is applied item by item in decision\_sweep.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "Leonard's email from yesterday asks me to model what each publisher would bring in for DD before we all sit down on Monday. Can you take the whole thing on for me, going by his email for what he wants and how he wants it done? The model goes in my DD publishing folder, and the board work he mentions is on the DD publishing card. When it's all in, reply to Leonard on his email with what he asked for."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Moonrail's own emails sign it "Moonrail Studios, a Kestrel Group studio" and its contact is "Partnerships, Kestrel Group"; Robert's call from Kestrel says every outside signing is frozen and whatever they had on the table with us is off. Moonrail's term sheet is the only Kestrel-group offer, so the rule's Withdrawn line (gave terms, then took them back) fits first.
Resolution evidence: RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "DD publishing model: ground rules"; MOON\_SIG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 199-199): "Moonrail Studios, a Kestrel Group studio"; ANIKA\_CONTACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 333-333): "'Partnerships, Kestrel Group', 'anika@moonrailstudios.com'"; KESTREL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 86-86): "Got a call from Kestrel. They''ve frozen every outside signing for the year, so whatever they had on the table with us is off."; R\_WD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Withdrawn: they gave terms, then took them back."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Moonrail status and figures differ. |
| writes | DIFFERENT | B adds a card, reminder and note. |
| destinations | SAME | Same destinations. |
| contents | SAME | Reply figures unchanged; Copperleaf still leads. |

Authority chain: P → EMAIL → RULES

Resolution relevance challenge: The signature and contact tie Kestrel to Moonrail, which is exactly what reading B denies.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the cited records select one outcome.
Challenge evidence: MOON\_SIG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 199-199): "Moonrail Studios, a Kestrel Group studio"; KESTREL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 86-86): "Got a call from Kestrel. They''ve frozen every outside signing for the year, so whatever they had on the table with us is off."

Compared alternative: C
Resolution: EXCLUDED. Frederick's own Appodeal thread ends with Appodeal's May 21 check-in after his May 14 question, and its proposal is a ROAS test with no rev share or advance. They wrote to us, there are no terms and the last message is theirs, so Waiting on us fits before No reply; "nothing back from them" is false for Appodeal.
Resolution evidence: RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "DD publishing model: ground rules"; APPO\_LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1830012626042968381.json pointer /messages/0/body): "Just checking in to see if you"; APPO\_PROP (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1830012626042968381.json pointer /messages/5/body): "ROAS-focused testing"; R\_WAIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Waiting on us: they wrote to us, there are no terms, and the last message is theirs."; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Appodeal status differs. |
| writes | DIFFERENT | B adds one nudge draft and moves the checklist item. |
| destinations | SAME | Same destinations. |
| contents | SAME | Reply unchanged. |

Authority chain: P → EMAIL → RULES

Resolution relevance challenge: The mailbox thread shows the last message is Appodeal's, which defeats the No reply premise of B.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the cited records select one outcome.
Challenge evidence: APPO\_LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1830012626042968381.json pointer /messages/0/body): "Just checking in to see if you"; R\_WAIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Waiting on us: they wrote to us, there are no terms, and the last message is theirs."

Compared alternative: D
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The doc says anything Leonard already said about what goes out to publishers still applies, and his Sep 26 note asks Fred for one short organic-figure note each in Gmail drafts. No quoted record says whether that pending Sep 26 job is part of this hand-off (three drafts) or whether the doc line only limits what outgoing messages may say (no drafts). The email itself lists the model, the card, contacts, the exclusion and the reply, not the notes. Deep recheck P1 confirmed this fork.
Resolution evidence: R\_OUT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Anything I''ve already said about what goes out to publishers still applies."; BRIDGE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 78-78): "Anyone who got it and still has an offer in with us hears the organic figure from us, $0.50 D30 ARPI, before we go any further with them. Fred, one short note each, left in your Gmail drafts"; EMAIL\_REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 112-112): "reply here with which offer goes first, what it brings in over 12 months, what it brings in during Q4, and how much publisher money we"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same statuses and figures. |
| writes | DIFFERENT | A writes 3 Gmail drafts to Tallwater, Harbor Lane and Wavecrest; B writes none. |
| destinations | SAME | Both write to Gmail drafts and the same other places; only the draft set differs. |
| contents | SAME | The reply to Leonard is the same; the note text is part of the differing writes. |

Resolution relevance challenge: R\_OUT and BRIDGE are the two records on the point; neither says whether the Sep 26 drafts are owed in this run, so they cannot exclude B.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the cited records select one outcome.
Challenge evidence: R\_OUT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Anything I''ve already said about what goes out to publishers still applies."; BRIDGE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 78-78): "Anyone who got it and still has an offer in with us hears the organic figure from us, $0.50 D30 ARPI, before we go any further with them. Fred, one short note each, left in your Gmail drafts"

Compared alternative: E
Resolution: EXCLUDED. Arthur's Sep 30 message is about the same $10K first-look and is later than Marek's Sep 29 email and Fred's card comment: it never hit the account, the bank sent it back, and it is being resent to land in October. The doc defines banked as actually in the SVB account and Q4 cash as advance money landing Oct 1 to Dec 31.
Resolution evidence: RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "DD publishing model: ground rules"; SVB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 88-88): "that $10K first-look never hit the account."; SVB\_RESEND (Evals/task\_inputs/01\_Universe\_Inject.sql lines 88-88): "resending it next week, so it"; R\_BANKED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Banked means it''s actually in the SVB account."; R\_Q4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Advance money that lands between Oct 1 and Dec 31, 2025. Assume we sign on Oct 31. If our lawyers give us a later date, use theirs. A payment on net terms lands that many days after signature."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Oakline Q4 and banked differ. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Banked figure in the reply differs. |

Authority chain: P → EMAIL → RULES

Resolution relevance challenge: Arthur's record names the same payment and states its actual bank status and landing month.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the cited records select one outcome.
Challenge evidence: SVB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 88-88): "that $10K first-look never hit the account."; R\_BANKED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Banked means it''s actually in the SVB account."

Compared alternative: F
Resolution: EXCLUDED. The doc itself says to assume Oct 31 unless the lawyers give a later date; the ESG Law partner says Nov 14 is the earliest, and Leonard confirms Nov 14 is the signing date. Net 60 from Nov 14 is Jan 13, 2026, outside Q4.
Resolution evidence: RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "DD publishing model: ground rules"; R\_Q4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Advance money that lands between Oct 1 and Dec 31, 2025. Assume we sign on Oct 31. If our lawyers give us a later date, use theirs. A payment on net terms lands that many days after signature."; LAWYER (Evals/task\_inputs/01\_Universe\_Inject.sql lines 120-120): "The earliest I can turn a license for Domino Delights for signature is Nov 14."; NOV14 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 127-127): "that makes Nov 14 our signing date, not Oct 31."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Q4 cash for Harbor Lane and Wavecrest differs. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | SAME | Reply Q4 for Copperleaf is $32,000 either way. |

Authority chain: P → EMAIL → RULES

Resolution relevance challenge: The doc's own condition for a lawyer-given date is met by the ESG Law email.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the cited records select one outcome.
Challenge evidence: R\_Q4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Advance money that lands between Oct 1 and Dec 31, 2025. Assume we sign on Oct 31. If our lawyers give us a later date, use theirs. A payment on net terms lands that many days after signature."; LAWYER (Evals/task\_inputs/01\_Universe\_Inject.sql lines 120-120): "The earliest I can turn a license for Domino Delights for signature is Nov 14."

Compared alternative: G
Resolution: EXCLUDED. The doc says to use the latest terms wherever they are, calls included. Frederick's Tallwater call notes put the advance at $40,000, everything else standing, and his card note of Lena's call cuts Sunfold to 30,000 installs, rest standing.
Resolution evidence: RULES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "DD publishing model: ground rules"; R\_LATEST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Use the latest terms we have from them, wherever they are, calls included."; TW\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 312-312): "The advance is $40,000 now, not the number in the term sheet. Everything else stands."; LENA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 102-102): "they can only commit 30,000 installs a month, not the 50,000 in the term sheet. Rest stands."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Figures and first pick differ. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Reply names a different offer and figures. |

Authority chain: P → EMAIL → RULES

Resolution relevance challenge: The rule names calls as a source and both call records state the changed term.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the cited records select one outcome.
Challenge evidence: R\_LATEST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Use the latest terms we have from them, wherever they are, calls included."; TW\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 312-312): "The advance is $40,000 now, not the number in the term sheet. Everything else stands."; LENA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 102-102): "they can only commit 30,000 installs a month, not the 50,000 in the term sheet. Rest stands."

Compared alternative: H
Resolution: EXCLUDED. The card rule says a publisher that already has a card here gets a comment instead. F/up with Marek is on that list, and its comment is about the $10K first-look payment, which is Oakline's term; Marek signs as Oakline Games. That card is Oakline's card.
Resolution evidence: CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 104-104): "One checklist per status on this card, one item per publisher."; CARD\_EXIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 104-104): "If they already have a card here, leave a comment with the status on that one instead."; MAREK\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Marek says the $10K first-look payment went out today."; MAREK\_SIG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 137-137): "Our term sheet for Domino Delights is in your Drive now.\\r\\n\\r\\nMarek Sobol\\r\\nOakline Games"; TS\_OAK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 39-39): "30% of net to Harmony Games\\n$30,000 advance ($10,000 first-look payment within 5 days of this sheet, credited to the advance, the remaining $20,000 net 30 from signature)\\n20,000 installs a month for 12 months"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same statuses. |
| writes | DIFFERENT | B creates a card instead of a comment. |
| destinations | SAME | Same destinations. |
| contents | SAME | Reply unchanged. |

Authority chain: P → EMAIL → CARD

Resolution relevance challenge: The existing card's own comment ties it to Oakline's payment, so Oakline already has a card.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the cited records select one outcome.
Challenge evidence: CARD\_EXIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 104-104): "If they already have a card here, leave a comment with the status on that one instead."; MAREK\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Marek says the $10K first-look payment went out today."

Decision sweep: The ground rules apply a status rule, then valuation, Q4, card, contact and draft rules publisher by publisher.
Decision rule: R\_WHO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Every publisher on Fred''s outreach sheet, plus any publisher that came to one of the four of us about Domino Delights since Apr 1, 2025, however it reached us. A name someone passed along doesn''t count unless they came to us."; R\_WD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Withdrawn: they gave terms, then took them back."; R\_RIGHTS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Out on rights: their terms take something we keep. The position from the August sync still stands."; R\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Live: a rev share and an advance in writing from them, whether that''s a term sheet, an email, or their note pasted in by one of us."; R\_PASSED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Passed: they said no."; R\_WAIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Waiting on us: they wrote to us, there are no terms, and the last message is theirs."; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count."

| Item | Outcome | Basis | Settled by / gap |
|---|---|---|---|
| Oakline Games | Live; 20,000 installs, $30,000 advance, 12-month $36,000; Q4 $30,000 ($10K first-look resent to land in October plus $20,000 net 30 from Nov 14); comment on F/up with Marek; reminder Oct 24 | RECORD | TS\_OAK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 39-39): "30% of net to Harmony Games\\n$30,000 advance ($10,000 first-look payment within 5 days of this sheet, credited to the advance, the remaining $20,000 net 30 from signature)\\n20,000 installs a month for 12 months"; SVB\_RESEND (Evals/task\_inputs/01\_Universe\_Inject.sql lines 88-88): "resending it next week, so it"; NOV14 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 127-127): "that makes Nov 14 our signing date, not Oct 31."; MAREK\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Marek says the $10K first-look payment went out today." |
| Tallwater Games | Live; $40,000 advance (call), 30,000 installs, 12-month $45,000, Q4 $40,000; new card; reminder Oct 17 | RECORD | TS\_TALL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "25% of net to Harmony Games\\n$60,000 advance net 30 from signature\\n30,000 installs a month for 12 months\\nMobile stores\\nRespond by Oct 17"; TW\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 312-312): "The advance is $40,000 now, not the number in the term sheet. Everything else stands." |
| Sunfold Mobile | Live; 30,000 installs (Lena call), $20,000, 12-month $54,000, Q4 $20,000; comment on F/up with Lena; reminder Oct 31 | RECORD | TS\_SUN (Evals/task\_inputs/01\_Universe\_Inject.sql lines 43-43): "30% of net to Harmony Games\\n$20,000 advance net 45 from signature\\n50,000 installs a month for 12 months\\nMobile stores\\nRespond by Oct 31"; LENA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 102-102): "they can only commit 30,000 installs a month, not the 50,000 in the term sheet. Rest stands." |
| Harbor Lane Games | Live; 25,000, $25,000, 12-month $30,000, Q4 $0 (net 60 from Nov 14); new card; reminder Oct 24 | RECORD | TS\_HARB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 45-45): "20% of net to Harmony Games\\n$25,000 advance net 60 from signature\\n25,000 installs a month for 12 months\\nMobile stores\\nRespond by Oct 24"; HL\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 316-316): "no changes from them"; NOV14 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 127-127): "that makes Nov 14 our signing date, not Oct 31." |
| Wavecrest Play | Live; 15,000, $15,000, 12-month $19,800, Q4 $0; new card; reminder Oct 31 | RECORD | TS\_WAVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 47-47): "22% of net to Harmony Games\\n$15,000 advance net 60 from signature\\n15,000 installs a month for 12 months\\nMobile stores\\nRespond by Oct 31"; WC\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 318-318): "Terms as sent."; NOV14 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 127-127): "that makes Nov 14 our signing date, not Oct 31." |
| Organic-figure notes to Tallwater, Harbor Lane and Wavecrest | Open: 3 Gmail drafts (reading A) or none (reading D) | SILENCE | No record; tested as A vs D |
| Moonrail Studios | Withdrawn (Kestrel Group froze outside signings); no figures, no card | RECORD | MOON\_SIG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 199-199): "Moonrail Studios, a Kestrel Group studio"; KESTREL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 86-86): "Got a call from Kestrel. They''ve frozen every outside signing for the year, so whatever they had on the table with us is off."; R\_WD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Withdrawn: they gave terms, then took them back." |
| Northglow Publishing | Out on rights (exclusive incl. PC and web) | RECORD | TS\_NORTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 51-51): "Exclusive across all digital storefronts and platforms, including PC and web"; AUGSYNC (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-08.json pointer /518/text): "I want to retain code, IP and non-mobile distribution rights but anything else is up for grabs." |
| Pinegrove Games | Out on rights (source code passes to them) | RECORD | TS\_PINE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 53-53): "Ownership of the full source code and build pipeline passes to Pinegrove at signature"; AUGSYNC (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C07C2866011/2025-08.json pointer /518/text): "I want to retain code, IP and non-mobile distribution rights but anything else is up for grabs." |
| Fernhollow Media | Passed | RECORD | RE\_FERN (Evals/task\_inputs/01\_Universe\_Inject.sql lines 220-220): "pass on Domino Delights" |
| Quietbay Games | Passed | RECORD | RE\_QUIET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 227-227): "tile games aren" |
| Slatewood Mobile | Passed | RECORD | RE\_SLATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 234-234): "pass for now. Our slate" |
| Ironbridge Interactive | Passed | RECORD | RE\_IRON (Evals/task\_inputs/01\_Universe\_Inject.sql lines 241-241): "We only take titles with a bigger live audience" |
| Tidewell Studios | Passed | RECORD | RE\_TIDE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 248-248): "Not for us, so we" |
| Marlin Play | Passed | RECORD | RE\_MARLIN (Evals/task\_inputs/01\_Universe\_Inject.sql lines 255-255): "decided to pass on Domino Delights" |
| Appodeal | Waiting on us (Appodeal wrote last on May 21, no rev share or advance); new card | RECORD | APPO\_LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1830012626042968381.json pointer /messages/0/body): "Just checking in to see if you"; APPO\_PROP (Universe\_SynthCut/SynthCut\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/frederick@harmonygames.co\_1830012626042968381.json pointer /messages/5/body): "ROAS-focused testing"; R\_WAIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Waiting on us: they wrote to us, there are no terms, and the last message is theirs." |
| Rayking Game | Waiting on us; new card. Fred's reply to the forward exists only as an unsent draft | RECORD | SH\_RAY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Rayking Game", "their marketing manager", "Sep 4, 2025 (to me)", "came to us", "nothing, they wrote first"\]"; RAY\_SLACK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 76-76): "Parking it for now, we still owe them an answer."; R\_WAIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Waiting on us: they wrote to us, there are no terms, and the last message is theirs.". Edge check NOT\_AN\_EDGE: An unsent draft is not a message sent to Rayking; Fred's Sep 5 Slack, after that draft, says we still owe them an answer, so the last message is theirs and Rayking is a plain Waiting on us member. RAY\_SLACK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 76-76): "Parking it for now, we still owe them an answer." |
| Kitebridge Games | Waiting on us; new card | RECORD | RE\_KITE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 262-262): "Could you send D7 by country before we go further?"; R\_WAIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Waiting on us: they wrote to us, there are no terms, and the last message is theirs." |
| Orchard Lane Games | No reply; new card and nudge | RECORD | SH\_ORCH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Orchard Lane Games", "partnerships inbox", "May 2025", "1", "May one-pager"\]"; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count." |
| Summit Mobile | No reply (automatic acknowledgement only); new card and nudge | RECORD | SH\_SUMM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Summit Mobile", "partnerships inbox", "May 2025", "1", "May one-pager"\]"; AUTO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 273-273): "This is an automatic reply"; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count." |
| Silverlake Mobile | No reply; new card and nudge | RECORD | SH\_SILV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Silverlake Mobile", "partnerships inbox", "Sep 2025", "2", "Intro only"\]"; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count." |
| Cedarbrook Play | No reply; new card and nudge | RECORD | SH\_CEDA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Cedarbrook Play", "partnerships inbox", "Sep 2025", "2", "Intro only"\]"; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count." |
| Foxglove Games | No reply; new card and nudge | RECORD | SH\_FOXG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Foxglove Games", "partnerships inbox", "Sep 24, 2025", "3", "Organic note"\]"; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count." |
| Riverstone Interactive | No reply; new card and nudge | RECORD | SH\_RIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Riverstone Interactive", "partnerships inbox", "Sep 24, 2025", "3", "Organic note"\]"; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count." |
| Bellwether Arcade | No reply; new card and nudge | RECORD | SH\_BELL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "\["Bellwether Arcade", "partnerships inbox", "Sep 24, 2025", "3", "Organic note"\]"; R\_NOREPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "No reply: nothing back from them. An automatic acknowledgement doesn''t count." |
| Copperleaf Games | In (came to Robert); Live; 40,000, $32,000, 12-month $67,200, Q4 $32,000; new card; reminder Oct 17; first pick | RECORD | COPPER (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "someone I know at Copperleaf Games, a small publisher, saw DD and emailed me out of the blue"; COPPER\_T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "28% of net to you, a $32,000 advance net 30 from signature, 40,000 installs a month for 12 months, mobile stores only, respond by Oct 17"; R\_WHO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Every publisher on Fred''s outreach sheet, plus any publisher that came to one of the four of us about Domino Delights since Apr 1, 2025, however it reached us. A name someone passed along doesn''t count unless they came to us."; R\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Live: a rev share and an advance in writing from them, whether that''s a term sheet, an email, or their note pasted in by one of us." |
| Redwood Arcade | In (came to Arthur); Live; 40,000, $25,000, 12-month $57,600, Q4 $25,000; new card; reminder Oct 31 | RECORD | REDWOOD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 329-329): "emailed me about deep links while they look at DD, and put their offer at the bottom"; REDWOOD\_T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 329-329): "24% of net to HG, a $25,000 advance net 45 from signature, 40,000 installs a month for 12 months, mobile stores only, respond by Oct 31"; ARTHUR\_PTR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 84-84): "Notes are on ENG-2362."; R\_WHO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Every publisher on Fred''s outreach sheet, plus any publisher that came to one of the four of us about Domino Delights since Apr 1, 2025, however it reached us. A name someone passed along doesn''t count unless they came to us." |
| Tamatem | Out: Julia passed the name along; Tamatem did not come to us | RECORD | TAMATEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C48D58CD7FBD/2025-06.json pointer /2/text): "Tamatem is a very good publisher"; R\_WHO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Every publisher on Fred''s outreach sheet, plus any publisher that came to one of the four of us about Domino Delights since Apr 1, 2025, however it reached us. A name someone passed along doesn''t count unless they came to us." |
| Sep 24 hypercasual contact | Out per Leonard's email | RECORD | EMAIL\_SEP24 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 112-112): "only wants hypercasual and never made it onto your sheet, so leave him out."; SEP24DM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/D05S58U4SAK/2025-09.json pointer /149/text): "There was a dude from" |
| Homa, NCsoft and Tilting Point | Out: co-dev, investment or UA funding talks | RECORD | R\_CODEV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Co-dev, engine or investment talks aren''t part of this, even where DD came up. That covers Homa and NCsoft, and Fred''s UA funding form to Tilting Point." |
| Kestrel Group as its own row | No separate row; Kestrel is Moonrail's parent and its only offer was Moonrail's | RECORD | MOON\_SIG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 199-199): "Moonrail Studios, a Kestrel Group studio"; ANIKA\_CONTACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 333-333): "'Partnerships, Kestrel Group', 'anika@moonrailstudios.com'"; KESTREL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 86-86): "Got a call from Kestrel. They''ve frozen every outside signing for the year, so whatever they had on the table with us is off." |

Strongest-alternative challenge (G): Term-sheet figures are the most visible written terms and would make Sunfold first pick with a different reply; the doc's calls-included rule and the two call records rule it out.
Challenge evidence: R\_LATEST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 35-35): "Use the latest terms we have from them, wherever they are, calls included."; TW\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 312-312): "The advance is $40,000 now, not the number in the term sheet. Everything else stands."; LENA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 102-102): "they can only commit 30,000 installs a month, not the 50,000 in the term sheet. Rest stands."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5)
- Tool path: every write has a cataloged tool (ledger above), so creation, format (a native Google Sheet) and delivery (folder move, drafts, reply) are SUPPORTED. Reads: Gmail/Drive/Slack/Calendar records are in Frederick's scope. Trello, Linear, Contacts and Snowflake are unscoped.
- Data: every needed fact exists (term sheets lines 39–53; replies; calls; Kestrel; SVB; lawyer; Copperleaf; Redwood Arcade; Appodeal base thread `frederick@harmonygames.co_1830012626042968381`; REVENUE_DAILY rows to 2025-09-30).
- Dimensional: per-publisher fields exist in each source. Numeric observability: all valuation inputs are whole-number literals in text records. The keep value is a SUM over `total_revenue_usd` NUMBER(38,2) rows, filtered by `game_id = 'domino_delights'` and month (the column comment says to SUM rows before comparing). That is reachable through `snowflake_execute_query`. Rendering precision is not established by the catalog (evidence limit only).
- No conflicting instructions. The drafts-only instructions (card, Sep 26 note) and the single reply are consistent with each other.

**Persona ACL Reachability:** PASS (5)
- Lens 1: every scoped read is visible. Leonard's email, the lawyer thread (cc Fred), the term-sheet emails and the Appodeal thread are in Frederick's mailbox. The ground rules doc and term sheets are shared with him. The outreach sheet and folder are his. The Tallwater/Harbor Lane/Wavecrest/execs events are on his calendar. C07C2866011, C096HFA5Z8W, C069FF9Q57S, D05S58U4SAK and C48D58CD7FBD all list EMPLOYEE_0008.
- Lens 2: no ask directs him to another person's scoped data. Inbound pitches visible only to Robert/Arthur (Streamlyn ad monetization in Robert's inbox; United Esports UA outreach in Arthur's and Robert's) are vendors, not publishers, so they are outside the set.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** FAIL (2), Action Decision Ambiguity. The delegation itself is explicit and there is no "I'll [verb]". But the same fork as UGT reading D gives two write sets: three organic-figure drafts versus none. The other writes (card vs comment, contacts skip rule, drafts vs the single reply) are fixed by the sources.

**Contrived / Unnatural:** PASS (5). No exact timestamps, opaque IDs, generated filenames, trap hints, hidden destinations (folder, card and thread are named), audit wording or if-chains. Difficulty comes from scattered, superseding records.

**Alignment with Today's Date:** PASS (5). "Yesterday" = Tue Sep 30, 2025 (Leonard's email 2025-09-30T23:10Z = 16:10 PDT). "Monday" = Oct 6, 2025 (DD publishing: execs, 10–11am PDT on Fred's calendar). Response dates (Oct 17/24/31), signature (Nov 14) and Q4 landings are correctly future. Every relied-on record is at or before 2025-09-30T23:10Z.

**Originality / Sample Similarity:** N/A (no samples supplied). The dataset check is reported above.

**Truthfulness:** PASS (5). Premises PR1–PR4 verified (email from yesterday asking for the per-publisher model before Monday; Frederick's DD publishing folder; the DD publishing card with the board work; Leonard's thread to reply on). No phantom identifier and no false state premise.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact. Drive (term sheets, sheet, folder), Gmail (lawyer date, Appodeal status, passes), Slack (Copperleaf in, Kestrel withdrawal, SVB bounce, the organic-note rule), Linear (Redwood Arcade in), Trello (Sunfold installs, existing cards), GCal (Tallwater advance), Snowflake (keep value).

**Investigation + Action:** PASS (5). Every write depends on the discovered statuses and figures.

**Coherence (Bolt-on):** PASS (5).

**Business Function:** PASS (5). Executive: deal choice for the founders' meeting.

## Phase 3: Universe Feasibility

**Data Existence:** all entities verified (27 publisher rows + 5 excluded candidates; 4 premises). All are retrievable through cataloged tools.

**Cross-Service Coherence:** PASS (5)
- Inconsistencies in task-touched data: none demonstrated. Injected dates are consistent with each other and the clock. Thread counters and snippets agree (Eval 0 C, REUSED). The Kestrel–Moonrail link is consistent across the signature, the contact and Robert's post. The sheet's tranche dates match Fred's outreach emails.
- Advisory (not scored): the eight external term sheets' `parents_json` is Frederick's private folder while Frederick holds reader access only. No record contradicts their location (the emails say "in your Drive"), and nothing in the data says where they should sit. So this is a realism note, not a demonstrated inconsistency. The safe fix is `parents_json = '[]'` (they then show up as shared with Frederick).
- Known base-data issues (not scored): SC-1 (DD September installs: INSTALL_EVENTS/DAU show none). The task reads REVENUE_DAILY revenue and publisher-committed installs, not DD's own September installs, so it doesn't depend on SC-1. Keep the rubric and OEs off DD September install counts. SC-49 (founder count): "the four of us" is fixed by the Oct 6 invite list (Leonard, Frederick, Robert, Arthur), not a founder count. Keep the rubric off founder counts.
- Injection SQL considered: Yes. Static integrity evidence: REUSED from `0_injection.md` checks A–C (SHA `ec62983b…f910`). Prompt-specific sources, access and configuration: supported. No error/async or dynamic-context configuration applies.
- Every SQL-added Slack message's author is a channel member (0008 in D05S58U4SAK; 0038 in C096HFA5Z8W; 0016 and 0025 in C07C2866011; 0025 in C069FF9Q57S). Apostrophes are doubled (lint clean).

## Phase 4: Final Evaluation

Overall: **FAIL 2**. Lowest dimensions: Unique Ground Truth 2 and Clarity 2, from one fork. Every other dimension scores 5.

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 2 | Reading D (no organic-figure drafts) unresolved; the other 6 alternatives excluded by quoted records |
| Prompt | Feasibility | 5 | Every read and write has a supported path; data exists |
| Prompt | Persona ACL Reachability | 5 | All scoped reads in Frederick's mailbox, calendar, Drive and channels |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 2 | Action Decision Ambiguity: 3 drafts vs none |
| Prompt | Contrived / Unnatural | 5 | Plain four-sentence request |
| Prompt | Alignment with Today's Date | 5 | Yesterday = Sep 30, Monday = Oct 6 |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | PR1–PR4 verified |
| Prompt | Tool Use & Cross-service | 5 | Seven services each change a graded fact |
| Prompt | Investigation + Action | 5 | Writes follow from findings |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | Fits a co-founder owning the outreach |
| Prompt | Business Function | 5 | Executive deal decision |
| Prompt | Assigned Competency | 5 | Finance model |
| Prompt | Assigned Task Skill | 5 | Analysis and synthesis central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | All facts retrievable |
| Universe | Cross-Service Coherence | 5 | No demonstrated inconsistency; one realism advisory |

### Issues Found

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | Ground rules doc `f_5e355d03f6eb6a4e866ead` (SQL line 35): "Anything I've already said about what goes out to publishers still applies." plus Leonard's Sep 26 #bridge-pitch note (SQL line 78): "Fred, one short note each, left in your Gmail drafts". No record says whether those three notes (Tallwater, Harbor Lane, Wavecrest: the May one-pager recipients that still have offers in) are owed in this hand-off. Leonard's email lists the model, the card, contacts, the Sep 24 exclusion and the reply, not the notes. | Major | Unique Ground Truth; Clarity (Action Decision Ambiguity) |

### Required fix

Settle the fork in the data (injection SQL), not in the rubric or OEs. Accepting both readings doesn't cure a decision fork. Pick one:

- **Make the notes part of the job.** Add a dated record Frederick can see that names them as owed now, in Leonard's voice. For example, add a line to the DD publishing card description or the ground rules doc saying the Sep 26 organic-figure notes are still not done and should be left in Gmail drafts along with the rest. The records already fix who they go to: Tallwater, Harbor Lane and Wavecrest. They got the May one-pager and still have offers in; Moonrail withdrew.
- **Or drop them.** Delete the doc's last line ("Anything I've already said about what goes out to publishers still applies."). Then no notes are required, and the Sep 26 note stays as background.

After changing the SQL, send `/injection`, then `/prompt`, then `/hardness` again. /oe and /rubric must also use the new version.

### Recommended Improvements (optional, no score effect)

1. To lower load risk, remove the four columns that aren't in the schema snapshot from the injection: `slides_pages.notes`, `slides_page_elements.table_json`, `slides_page_elements.ordinal`, `linear_comments.sequence`. If the live tables lack any of them, the whole transaction rolls back and every injected record disappears.
2. Set `parents_json` to `'[]'` on the eight external term-sheet rows (lines 17–31), so external owners aren't shown filing into Frederick's private folder.
3. For the rubric and OEs (once the fork is fixed): grade the Q4 column from the Nov 14 signature (Harbor Lane and Wavecrest $0; Sunfold and Redwood Arcade land Dec 29), and grade Oakline's Q4 as $30,000 with banked $0. Keep everything off DD September installs (SC-1) and founder counts (SC-49).

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 4 prompt sentences, email, doc, card, Sep 26 note; 26 publishers + 9 excluded candidates; 34 fork lines | 2 | 1 |
| P2 | Services, access, Snowflake REVENUE_DAILY recompute (1,666 rows), injected-vs-base coherence | 3 | 0 |
| P3 | 13 prompt claims; SQL ids, columns, authors, apostrophes, clock | 2 | 0 |
| P4 | 4 prompt sentences | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "going by his email for what he wants and how he wants it done" | Elena Petrova reply (SQL line 213) "We''ve shared a term sheet with you in Drive" | §2 boundary | Unique Ground Truth | REJECTED | The Pinegrove term sheet exists: SQL line 32 (`f_5f3ef4a4760d18e696a41a`, "Pinegrove Games - term sheet - Domino Delights", shared with Frederick) and line 53 (doc body: "Ownership of the full source code and build pipeline passes to Pinegrove at signature"). Pinegrove is Out on rights, and Elena gave terms, so she goes to Contacts |
| DR2 | P1 | "going by his email for what he wants and how he wants it done" | Doc line 35 "Anything I''ve already said about what goes out to publishers still applies."; #bridge-pitch line 78 "Fred, one short note each, left in your Gmail drafts" | §2 decision fork | Unique Ground Truth; Clarity | CONFIRMED | No prompt sentence or persona-visible record says whether the Sep 26 notes are owed in this run. The note shows they were asked for, not that this hand-off includes them. My own reading D was the same fork |
| DR3 | P2 | "going by his email…" | Outreach sheet line 58 Rayking "Sep 4, 2025 (to me)" vs base forward thread 1842348778705877030 | §3 coherence | Cross-Service Coherence | REJECTED | Leonard forwarded Rayking's mail to Frederick on Sep 4, 2025 ("Should we explore for DD?"), so it reached him that day; no contradiction |
| DR4 | P2 | "going by his email…" | ENG-2362 updated_at 2025-06-03 vs injected comment 2025-09-26 | §3 coherence | Cross-Service Coherence | REJECTED | SQL line 330 updates ENG-2362 `updated_at` to 2025-09-26T18:32:00Z |
| DR5 | P2 | "going by his email…" | REVENUE_DAILY /tables/12 | base-data-v1 | Data exists | REJECTED | Informational: confirms the keep value $12,723.96 and finds no conflict; SC-1 and SC-49 not depended on |
| DR6 | P3 | "the board work he mentions is on the DD publishing card." | Card 68dab660… desc also asks for Gmail drafts | §3 loose descriptor | Truthfulness | REJECTED | The sentence is true: the board work is on that card. It doesn't claim the card holds only board work, and the email points to the card for all of it |
| DR7 | P3 | "When it''s all in, reply to Leonard…" | SQL columns notes, ordinal, table_json, sequence | §3 SQL columns | Injection advisory | REJECTED | Already the Eval 0 advisory in the Injection Gate section; the schema snapshot is unverified, so it's not a demonstrated defect |

Effect on verdict: Unique Ground Truth 5 → 2 and Clarity 5 → 2 (DR2). Overall PASS 5 → FAIL 2. Other dimensions unchanged.

- F1: Organic-figure drafts to Tallwater, Harbor Lane, Wavecrest | A: 3 drafts required | B: no drafts (the doc line only limits outgoing content) | Missing: a dated record Frederick can see that says the Sep 26 notes are part of this job (or removal of the doc's "still applies" line)
- F2: Moonrail status | Withdrawn | Live | Settled by: "Moonrail Studios, a Kestrel Group studio" + "Got a call from Kestrel… whatever they had on the table with us is off."
- F3: Appodeal status | Waiting on us | No reply | Settled by: Appodeal's May 21 "Just checking in to see if you…" is the last message in Frederick's thread, and the proposal has no rev share or advance
- F4: Rayking status | Waiting on us | last message ours | Settled by: Fred's reply is only in Drafts; "Parking it for now, we still owe them an answer."
- F5: Oakline Q4 and banked | $30,000 Q4, $0 banked | $20,000 Q4, $10,000 banked | Settled by: "that $10K first-look never hit the account." / "resending it next week, so it…land in October"
- F6: Signing date | Nov 14 (Harbor Lane, Wavecrest Q4 $0) | Oct 31 | Settled by: "that makes Nov 14 our signing date, not Oct 31."
- F7: Tallwater advance / Sunfold installs | $40,000 / 30,000 (first pick Copperleaf) | $60,000 / 50,000 (first pick Sunfold) | Settled by: "The advance is $40,000 now…" and "they can only commit 30,000 installs a month…", under "Use the latest terms… calls included."
- F8: Oakline and Sunfold follow-up | comments on F/up with Marek and F/up with Lena | new cards | Settled by: "If they already have a card here, leave a comment…"; the Marek card's comment is about Oakline's first-look
- F9: Northglow / Pinegrove | Out on rights | Live | Settled by: "I want to retain code, IP and non-mobile distribution rights" vs "Exclusive across all digital storefronts and platforms, including PC and web" / "Ownership of the full source code…"
- F10: Copperleaf, Redwood Arcade in | in | out | Settled by: "however it reached us" + Robert's paste and Arthur's ENG-2362 comment
- F11: Tamatem, the Sep 24 contact, Homa, NCsoft, Tilting Point, vendors (Streamlyn, United Esports) | out | in | Settled by: "A name someone passed along doesn''t count…", "leave him out", "Co-dev, engine or investment talks aren''t part of this…"; the vendors aren't publishers
- F12: Keep value | $12,723.96 (monthly average × 12) | row or daily average | Settled by: "What DD earned in Jul, Aug and Sep… averaged, times 12" and the column comment "SUM before comparing"

Platform defects: none

### FINAL VERDICT: FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Score: 2

Execution status: COMPLETE

Eval version: task-quality-v1

Eval release SHA-256: 81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c

Reviewed prompt SHA-256: bed2b497fa1ee539a5c9783b7ba01df4f69055c71b40bd5f076557acc2462b54

Review context SHA-256: 46b1e5fa5cec51a51cfe516e9070d2bf5b48a024a14a2486f146aedb32fee54b

Prompt record SHA-256: ec405b0cf53da2b9471df1cb17c931ae82d90ca679850887aa8c66f8ed15fa39

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Settle fork F1 in the injection SQL: either add a dated record Frederick can see that makes the Sep 26 organic-figure notes (Tallwater, Harbor Lane, Wavecrest) part of this job, or delete the ground rules doc's line "Anything I've already said about what goes out to publishers still applies." Then send /injection, /prompt and /hardness again.

Evidence limits: Snowflake query rendering precision is not established by the catalog (raw values verified). The injection's live-schema compatibility is unverified (Eval 0 advisory).

**Lowest Dimension:** Unique Ground Truth and Clarity & Specificity, 2. One unsettled write fork (organic-figure drafts).

**Summary:** The prompt is short, natural and accurate. The scenario is strong, with seven services, superseding calls, a Kestrel-owned studio withdrawing, a bounced first-look and a later signing date, and every one of those resolves to one answer from records Frederick can see. One thing fails it: no record says whether the three Sep 26 organic-figure drafts are part of this job, so two careful runs would end with different writes. One SQL edit fixes it.
