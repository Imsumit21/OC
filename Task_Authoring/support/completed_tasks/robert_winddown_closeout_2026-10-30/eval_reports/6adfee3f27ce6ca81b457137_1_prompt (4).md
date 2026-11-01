## PROMPT EVALUATION REPORT

### Task: Robert takes over Leonard's account close-out register for the wind-down: build the register per Leonard's conventions doc, share it with Leonard and Arthur, settle the 45 Linear shutdown issues and reply in Leonard's #winddown thread with the two monthly totals and the clashes.
### Assigned Persona: Robert - Co-founder & Creative Director (roster: robert@harmonygames.co, "Co-Founder & Creative Director", Executive)
### Assigned Business Function: Executive
### Assigned Competency: Corporate Ops
### Assigned Task Skill: Planning and decision support
### Assigned Horizon: long-horizon

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review for your attempt (6adfee3f27ce6ca81b457137), `/prompt`, audit mode |
| Actual review time | 2026-10-28T16:30Z |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (hg4-2026-08-31 v37); `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8…` |
| Prompt | `Evals/task_inputs/04_Prompt.txt`, revision 6, 520 bytes, sha256 `cfab17798d35…` (the attached `04_Prompt (5).txt` is byte-identical, so no new prompt version was saved) |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md`, sha256 `ea9a28d2e72f…` (all five fields stated) |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, revision 13, 92,086 bytes, sha256 `50f6a195de7e…` |
| Reference files / error-async config / dynamic context | None supplied; the prompt references no attachment (all sources are environment records) |
| References | Eval 1 `7cc19b60d298…`; WORKFLOW `ee4cd8e1cc29…`; scoring.json `c14873e614cd…`; acl.md `e9bca2b35f98…`; roster.json `3f2174513f63…`; catalog.json `7057742297e8…`; common_errors.md `53d596d0bc26…`; deep_recheck.md `85de10c424d2…`; prompt_qc_examples.md `5f58eb0d4a6b…`; known_base_issues.md `79b202893d5e…`; Eval 0 report `8f780bb245a9…` |
| Evidence contract | `stage-evidence-v1`; authority contract `prompt-incorporation-v1` |
| Eval version | task-quality-v1 |
| Eval release SHA-256 | 6478616fae461adfff81f45b2a523017b7a8e042bf02b6afc8c113d659886b8f |
| Reviewed prompt SHA-256 | cfab17798d359095db76a085acc3b201b1c036568240eb062244f78651d9ee9c |
| Review context SHA-256 | 2205e07820412aa6b261a084751fc7390921e0cdc892e1e74bcbfd8c4d139a5c |
| Prompt record SHA-256 | 5931f6bb62ac0f8c9d3622952ecd91824378c1f0a604b15d85663aea26504655 |

## 2. Input / authority issues

- Intake complete: prompt, all five assignment fields, saved SQL (revision 13), saved task date. No reference attachments.
- Since the last /prompt review (SQL revision 12; prompt unchanged), revision 13 changed nine statements and removed one (Eval 0 revision-13 report §2): the Layer receipt is now dated 2026-02-03 with "Your next payment is on March 3, 2026."; the project description adds "we cancelled the unity ads in the UA line after october, so they''re not in here"; Oliver's ENG-2439 comment adds "both games'' support buttons now open email instead of helpshift"; ENG-2448 adds "the p&l stops after the 2024 payment"; ENG-2469 adds "(the p&l missed last april''s charge)"; ENG-2463 (Calendly) now reads "we cancelled calendly in october right after the annual charge, it just runs out"; ENG-2464 adds "this month''s invoice was $298.13"; and Oliver's Zapier "#issuefeed" comment is gone. Every register row, both totals, every Linear end state and the clash set were re-derived under revision 13.
- Incorporation (`prompt-incorporation-v1`): "work through his ask and everything it points to, build the register the way he wants it ... settle each of the linear issues like he asked" incorporates Leonard's injected #winddown ask (2026-02-13 17:21Z) and the sources it names: his keep list and the reply under it, Arthur's KubLLC moves, Sunset's data checklist (plus the Feb 13 amendment), SVB's card terms (Trello card 456), the conventions doc (rules 1–10) and the Linear shutdown project (its settle rule). The doc points to the January P&L costs tab and the finance ledger. The Sherwood checklist, the Growth/UA Confluence page and the Feb 10 Subscriptions sheet are not incorporated (decoys; the project says "This replaces my subscriptions sheet from Tuesday.").
- The Docs PDFs/XLSX were extracted in an earlier run of this review on the same Eval hash and weren't re-extracted; no check here depends on them beyond what Eval 1 adopts.

## 3. Checklist

Reuse basis (stage-evidence-v1): Phase 1 judgments from the previous /prompt report (same prompt and assignment, same Eval and reference hashes, re-hashed this run), re-read this run. Everything touching rows, costs, dates, totals, Linear states, clashes and coherence is NEW.

| Item | Status |
|---|---|
| Intake (five fields, prompt, SQL, date) | NEW, done |
| STEP 0.5 injection gate | NEW, CURRENT (Eval 0 PASS on this SQL hash) |
| Phase 0.1 Docs and catalog | REUSED (same Eval and catalog hashes) |
| Phase 0.2 universe exploration | NEW for revision 13: #winddown Feb 2026 (checklist ffb65137, keep list 6d8c8d8a, to-do fdd87e27, Helpshift plan /57), #prototype Layer message, #issuefeed ZapierBot, Robert's DM on Unity Ads (Feb 3), Robert's mailbox for Layer, Unity, Google Workspace, Calendly, Zapier and Helpshift mail (complete scans), Unity Ads / Workspace / Singular invoice PDFs, HG Costs and HG P&L tabs (full grid), FINANCE_LEDGER marketing_ua Oct 2025–Feb 2026 and AWS Jan 2026, GitHub PRs and commits for Feb 2026 (Helpshift), Linear users |
| Phase 0.3 calibration | Eval inline examples and prompt_qc_examples.md |
| Phase 1.1–1.5 | REUSED (prompt and assignment unchanged); re-read this run; P4 checked wording blind |
| Phase 2.1 UGT (two-reading table, record saved) | NEW, PASS |
| Phase 2.2 Feasibility incl. ACL, dimensions, numeric observability | NEW, PASS |
| Phase 2.3 Truthfulness (premise record) | NEW record, PASS |
| Phase 2.4–2.9 | Re-checked; 2.9 N/A (no samples supplied) |
| Phase 3.1–3.2 | NEW, 3.2 NON-FAIL |
| Phase 4 scoring | NEW |
| Phase 5 deep recheck P1–P4 | NEW (see Deep Recheck) |

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`)
- Reviewed SQL sha256: `50f6a195de7e1d2842b4966192eb31888ef587acc054191ff310ee39473f09d0`  Eval 0 verdict: PASS (`injection-static-v2`, COMPLETE, 2026-10-28T15:49Z, report sha256 `8f780bb245a9…`)
- Static checks A–C reused (same SQL hash, manifest, clock, schema/ACL hashes). Eval 0 advisories: A1 `linear_projects.links_json` (and `linear_project_teams` / `linear_project_members`) aren't in the schema snapshot; INFO the Helpshift export zip is metadata-only (cited by name only).
- Eval 0 findings on records this prompt depends on: none. The zip's contents aren't needed (Oliver's comment states the export is done), and A1 is a live-schema risk, not a data value the answer is graded on.

## 4. Requirement ledger (authority_contract: prompt-incorporation-v1)

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Work through Leonard's ask and what it points to | Injected #winddown msg `9e245e76…` (C0ADGSZKR3R, Leonard, 2026-02-13T17:21Z) | Prompt names #winddown and Friday | `slack_*` read/search | Robert (EMPLOYEE_0016) is a #winddown member | Agent reads the ask and each named source |
| Build the register "the way he wants it" | Conventions doc rules 1–10; keep list `6d8c8d8a…` + Arthur's Gusto reply; Arthur's moves `7edc71bf…`; Leonard's Feb 12 subscriptions checklist `ffb65137…`; Sunset emails (Feb 12 list + Feb 13 amendment); SVB Trello card 456; HG Costs tab (Sound and UA lines); FINANCE_LEDGER Jan/Feb 2026 lines (AWS FIN-000687 −1,485; applovin FIN-000688 −9.80; meta FIN-000689 −2,843.84); Linear project description and ENG-2438–2483 (45 issues) with comments (owner figures incl. ENG-2464 $298.13); receipts in Robert's mail (Figma, Layer Feb 3, Soundly, ElevenLabs, Singular past-due notice, iPostal, Lucidchart, Trello, Pond5); PR #38 CodeRabbit notice; Helpshift export in the Wind Down folder; GCal review call 2026-03-12 | The ask names each source; the doc names the costs tab and the ledger | `gdocs_*`, `gsheets_*`, `gmail_*`, `trello_*`, `linear_*`, `snowflake_execute_query`, `github_*`, `gcal_*` reads; `gsheets_create_spreadsheet` + `gsheets_values_update`/`gsheets_batch_update` | Doc, P&L shared with Robert; Sunset and receipt mails in Robert's mailbox; review event on Robert's calendar; Linear/Trello/GitHub/Snowflake unscoped | One sheet: account, what we do, where it stands, by when, owner, monthly cost; two totals |
| Share with Leonard and Arthur | Ask: "share it with me and Arthur as editors" | Prompt + ask | `gdrive_share_file` (fileId, emailAddress, role) | Write, not ACL-scoped | Two writer shares |
| Settle each Linear issue | Project rule: Done once closed in the register, Canceled if it doesn't belong, else open; comment "what happens and by when" | Prompt + ask + project description | `linear_update_issue` (state), `linear_create_comment` | Linear unscoped | 45 comments; 5 Done, 20 Canceled, 20 open |
| Reply in Leonard's thread with two totals and clashes | Ask; doc rules 9 and 10; Slack free-plan / guest / "down to 3 FT members" decisions and the Google archive plan, each against Sunset's list | Prompt names "his thread" | `slack_send_message` with `thread_ts` | Write | One thread reply: $11,045.13 and $1,249.04, two clashes |

Reading A derivation (NEW, revision 13): 28 register rows — 17 Cancel, 2 Keep, 1 Move, 8 Hold. Cancel $9,648.09 (Unity 2,348.50; Helpshift 150.00; Soundly 10.00; Singular 2,083.33; AWS 1,485.00; Gusto 116.00; Carta 321.00; DocuSign 25.00; Layer 49.00; CodeRabbit 45.00; Cursor 40.00; Zapier 73.50; Kapwing 24.00; 1Password 19.95; meta 2,843.84; applovin 9.80; ElevenLabs 4.17). Keep $415.00 (QuickBooks 115.00; Deel 300.00). Move $148.00 (Metabase). Hold $834.04 (Linear 152.72; Figma 101.00; Trello 0.00; dbt 100.00; BigQuery 4.97; Google Workspace 298.13; Slack 87.22; GitHub 90.00). Every-row total **$11,045.13**; Keep and Hold total **$1,249.04**. What changed from revision 12: Google Workspace now has a readable owner figure ($298.13), Helpshift and Zapier take a dash (export and email switch-over done), Layer's by when is 2026-03-02, Unity Ads and Calendly are left out by rule 2.

## 5. Phase 1: Prompt Structure & Persona

All Phase 1 results are REUSED. The prompt and assignment are byte-identical; the text was re-read this run, and P4 checked the wording blind.

**Persona:** PASS (5). Leonard asked Robert directly (`<@EMPLOYEE_0016_SLACK_ID> can you own the account close-out register…`). Robert is a co-founder in the three-founder #winddown channel, cc'd on Sunset's mail and invited to the review call.

| Check | Finding |
|---|---|
| Role plausibility | Yes: a direct ask from the CEO in #winddown |
| Voice match | Yes: informal first person |
| Access plausibility | Yes: channel member, cc'd on Sunset, shared on the doc and the P&L |
| Responsibility scope | Yes: executive wind-down decisions |

**Assigned Competency:** PASS (5). Vendor account close-out, card terms, a data buyer's keep list and wind-down operations are Corporate Ops work (board/legal/HR/vendor).

**Assigned Task Skill:** PASS (5). Every account needs a Cancel/Keep/Move/Hold call, a status and a deadline under competing rules, plus a clash analysis.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS (5).
- Dynamic change: Sunset's Feb 13 reply swaps Metabase out and Trello, BigQuery and dbt in; Arthur's reply amends the keep list; Oliver's Feb 13 comment supersedes Leonard's Feb 11 "move off Helpshift" plan.
- Multi-source: Slack, GDocs, GSheets, Gmail, Trello, Linear, Snowflake, GitHub, GCal, with decoys (Sherwood checklist, Growth/UA Confluence page, stale Subscriptions sheet).
- Data seeding: PASS. The prompt is about 95 words and every operating rule is seeded.

**Naturalness:** PASS. A lowercase run-on delegation with no formatting, no polished connectives, no enumerated specs and no staged typos.

| AI-text red flag | Found? | Quote |
|---|---|---|
| Document formatting | No | — |
| Polished connectives | No | — |
| Enumerated deliverable specs / preservation rules | No | — |
| Even, symmetric sentences | No | — |
| Staged errors | No | — |

**Anti-Patterns:**

| Pattern | Status |
|---|---|
| Command List | PASS: one casual "and then" where the reply really depends on the register's totals |
| Bolt-On | PASS |
| Pre-Solving | PASS: no row, total or clash is stated |
| Tool Mention | PASS |

**Prompt diversity:** one new sheet, two shares, 45 Linear comments and state changes, and one thread reply. Category: Founders / Exec / Strategy, overlapping Finance / Legal / HR / Ops.

## 6. Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every fork tested under revision 13 is settled by a persona-visible record: the project description removes Unity Ads (rule 2), Oliver's Feb 13 comment closes the Helpshift switch-over (dash for Helpshift and Zapier), Leonard's ENG-2464 figure prices Google Workspace at $298.13, the Feb 3 Layer receipt dates Layer's charge (2026-03-02), and Leonard's ENG-2463 comment removes Calendly. The earlier settled forks (Pond5, adjoe, Typecast, Gusto, Singular, Layer status, Slack and Helpshift-export clashes) still hold.

Alternative selection: Re-derived every register row, column, both totals, each Linear end state and the clash set under revision 13, then tested each place a reader could split: the revision-13 changes (Unity Ads, Helpshift and Zapier switch-over, Workspace cost, Layer date, Calendly) and the earlier forks (Pond5, adjoe, Typecast, Layer status, Gusto, Singular, Slack and Helpshift-export clashes).

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Apply Leonard's ask, the conventions doc rules 1-10, the project settle rule and the cited records row by row under revision 13. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he wants it"; SQL\_ASK\_DOC (Evals/task\_inputs/01\_Universe\_Inject.sql): "the conventions doc I just put in the Wind Down folder"; SQL\_PROJ\_RULE (Evals/task\_inputs/01\_Universe\_Inject.sql): "Done once the account counts as closed in the register (access can run out later), Canceled if it doesn''t belong on the list, everything else stays open" |
| B | Rule 3 gives every account inside a multi-vendor costs-tab line its own row whether or not it has a ledger line; the UA line covers Unity Ads, whose last invoice to Robert is October 2025, so Unity Ads is a Cancel row priced from that invoice. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17), Unity Ads (Open, 2026-02-28, Robert, $1,653.47). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $12,698.60, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | SQL\_CONV3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "every other account hiding inside a costs-tab line that covers several vendors — each one gets its own row, whether or not it has a ledger line of its own"; UA\_INV (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/00015915.json pointer /messages/0/body): "Attached is your 10 2025 monthly invoice."; UA\_INV\_SUBJ (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/00015915.json pointer /messages/0/subject): "Unity Technologies SF Invoice\#: CINV\_00022209 for Harmony Games Inc." |
| C | Zapier is Closed, but the base \#winddown plan to move both games off Helpshift before Feb 28 is a switch-over that has to happen before Zapier's plan runs out on Feb 27, so its by when is the day before. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; 2026-02-26, because the Helpshift ticket pipe has to be switched before the plan ends; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2476's comment gives 2026-02-26 as the by when. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | SQL\_CONV6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends — then the day before it ends."; SQL\_ZAPIER\_END (Evals/task\_inputs/01\_Universe\_Inject.sql): "their email says the plan runs until feb 27"; WD\_HELP\_SWITCH (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /57/text): "We gotta move domino delights and zombie match off Helpshift before Feb 28th." |
| D | Leonard's Feb 11 plan to move both games off Helpshift before Feb 28 is a switch-over still to come, so the Closed Helpshift row takes the day before its access ends (end of February). | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; 2026-02-27, because the move of both games off Helpshift is still pending; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439's comment gives 2026-02-27 as the by when. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | SQL\_CONV6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends — then the day before it ends."; WD\_HELP\_SWITCH (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /57/text): "We gotta move domino delights and zombie match off Helpshift before Feb 28th."; SQL\_HELP\_END (Evals/task\_inputs/01\_Universe\_Inject.sql): "helpshift wrote back that they''re discontinuing us at the end of february" |
| E | Pond5 sits in the Sound (Pond5, Soundly, Elevenlabs) line, and rule 3 says each such account gets its own row. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17), Pond5 (Open, dash, Robert, $0.00). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. Pond5 appears as an extra $0.00 row. | COSTS\_SOUND (/tmp/hg/ev/pl\_extract.json pointer /rows/14): "Sound (Pond5, Soundly,Elevenlabs)"; SQL\_CONV3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "every other account hiding inside a costs-tab line that covers several vendors — each one gets its own row, whether or not it has a ledger line of its own" |
| F | Leonard cancelled Layer in the app and knew the access end date, so the vendor confirmed it in-app: Layer is Closed and ENG-2473 is Done. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Closed, in-app, dash, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing, ENG-2473 Layer. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 19 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. Layer is shown Closed (in-app) with a dash. | SQL\_LAYER\_CMT (Evals/task\_inputs/01\_Universe\_Inject.sql): "cancelled it in the app on the 11th"; PROTO\_LAYER (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C09UHHN6PFZ/2026-02.json pointer /575/text): "we have access until March 3rd" |
| G | Leonard says Layer access runs until March 3rd, so Layer's by when is March 3. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-03, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2473's comment gives 2026-03-03 as the by when. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | PROTO\_LAYER (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C09UHHN6PFZ/2026-02.json pointer /575/text): "we have access until March 3rd" |
| H | Leonard's Helpshift email draft line that no export is needed is a \#winddown decision that Sunset's Helpshift export request undoes, so it is a third clash. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and three clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line, and the no-export line in Leonard's Helpshift email against Sunset's Helpshift export request. | WD\_HELP\_NOEXPORT (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /21/text): "We don’t need to export any data."; SQL\_SUNSET\_HELP (Evals/task\_inputs/01\_Universe\_Inject.sql): "For Helpshift, please export the full ticket history to Drive before your subscription ends." |
| I | Keeping Slack under Harmony Games until the data is extracted replaced the free-plan and guest decision, so Slack is not a clash. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and one clash: the Google archive after Feb 15 against Sunset's do-not-archive line. | WD\_KEEPDATA (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /190/text): "We keep accounts that has our data such as Slack, google, google analytics, github under Harmony Games until the data is extracted" |
| K | Arthur's 'let's cancel before mar 3' is only a suggestion, so Gusto stays a Keep row from Leonard's keep list. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00), Gusto (2026-02-19; Leonard; $116.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,365.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | WD\_KEEP (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /188/text): "During shutdown, let’s keep Deel, gusto, Intuit."; SQL\_GUSTO (Evals/task\_inputs/01\_Universe\_Inject.sql): "let''s cancel before mar 3" |
| L | Singular costs its $6,250 costs-tab line each month. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $6,250.00); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $15,211.80, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | SING\_INV\_AMT (/tmp/hg/ev/singular\_invoice.txt): "$6,250.00" |
| M | adjoe is a UA network inside the UA line, so it gets its own row. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17), adjoe (Open, 2026-02-28, Robert, $0.00). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. adjoe appears as an extra $0.00 row. | SQL\_CONV3 (Evals/task\_inputs/01\_Universe\_Inject.sql): "every other account hiding inside a costs-tab line that covers several vendors — each one gets its own row, whether or not it has a ledger line of its own" |
| N | Typecast is still a live free-tier account, so it stays as a $0 Cancel row and ENG-2442 stays open. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17), Typecast.ai (Open, dash, Robert, $0.00). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 18 left-out issues (ENG-2441, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 21 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,045.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. Typecast.ai appears as an extra $0.00 row. | SQL\_TYPECAST (Evals/task\_inputs/01\_Universe\_Inject.sql): "we stopped paying for typecast after the summer" |
| O | Google Workspace is priced from the January P&amp;L costs tab's G-Suite line (297.6), or the old Subscriptions sheet's 300. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $297.60), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 19 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2463, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 20 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,044.60, Keep and Hold rows $1,248.51; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | COSTS\_GSUITE (/tmp/hg/ev/pl\_extract.json pointer /rows/51): "G-Suite (gmail, etc)"; SQL\_SUBS\_GWS (Evals/task\_inputs/01\_Universe\_Inject.sql): "\["Google Workspace", 300\]" |
| P | Calendly still runs until its October renewal, so it stays on the register as a Cancel row ($96 a year on the costs tab, $8.00 a month) and ENG-2463 stays open. | Cancel: Unity (Requested, 2026-02-18, Arthur, $2,348.50); Helpshift (Closed, Helpshift's reply per ENG-2439; dash, because the export and the switch to email are done; Leonard; $150.00); Soundly (Closed, Soundly's email; dash; Robert; $10.00); Singular (Requested, 2026-02-28, Leonard, $2,083.33); AWS (Open, 2026-02-28, Arthur, $1,485.00); Gusto (Open, 2026-03-02, Leonard, $116.00); Carta (Open, 2026-08-14, Leonard, $321.00); DocuSign (Open, 2026-04-19, Robert, $25.00); Layer (Requested, 2026-03-02, Leonard, $49.00); CodeRabbit (Closed, bot notice on Combo-Fighters PR \#38; dash; Arthur; $45.00); Cursor (Requested, 2026-03-04, Arthur, $40.00); Zapier (Closed, Zapier's email per ENG-2476; dash; Leonard; $73.50); Kapwing (Closed, Kapwing's email per ENG-2478; dash; Arthur; $24.00); 1Password (Open, 2026-03-07, Arthur, $19.95); added meta (Open, 2026-02-28, Robert, $2,843.84), applovin (Open, 2026-02-28, Robert, $9.80), ElevenLabs (Open, 2026-07-08, Robert, $4.17), Calendly (Requested, dash until the October renewal, Robert, $8.00). Keep: QuickBooks (Intuit is the duplicate; 2026-02-19; Leonard; $115.00), Deel (dash; Leonard; $300.00). Move: Metabase (dash; Arthur; $148.00). Hold for Sunset: Linear (2026-03-12, Arthur, $152.72), Figma (2026-03-12, Robert, $101.00), Trello (2026-03-12, Leonard, $0.00), dbt (2026-03-12, Arthur, $100.00), BigQuery (2026-03-12, Arthur, $4.97), Google Workspace (2026-02-19, Leonard, $298.13), Slack (2026-02-19, Leonard, $87.22), GitHub (2026-03-12, Arthur, $90.00). Left out: OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, iPostal, Fondo, Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads, Pond5, adjoe, Unity Ads. | Create one Google Sheet register; share it with Leonard and Arthur as editors; comment on every Shutdown – accounts issue (ENG-2438 to ENG-2483, 45 issues) with what happens and by when and set its state per the project rule; post one reply in Leonard's \#winddown thread. Done: ENG-2439 Helpshift, ENG-2440 Soundly, ENG-2474 CodeRabbit, ENG-2476 Zapier, ENG-2478 Kapwing. Canceled: the 18 left-out issues (ENG-2441, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 2452, 2453, 2466, 2470, 2471, 2472, 2480, 2481, 2482, 2483) plus ENG-2461 Intuit (duplicate). The other 21 stay open. ENG-2439 and ENG-2476 comments give a dash as the by when; ENG-2473's comment gives 2026-03-02. | New Google Sheet (editors leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co); Linear issues ENG-2438 to ENG-2483; \#winddown thread under Leonard's 2026-02-13 17:21Z message. | Register as in the decision; totals: every row $11,053.13, Keep and Hold rows $1,249.04; reply gives both totals and two clashes: the Slack decisions (free plan, cut to 3 full members and guests) against Sunset's paid-plan, every-user list, and the Google archive after Feb 15 against Sunset's do-not-archive line. | SQL\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql): "we cancelled calendly in october right after the annual charge, it just runs out"; COSTS\_CALENDLY (/tmp/hg/ev/pl\_extract.json pointer /rows/50): ""Calendly"" |

Explicit option inventory: The prompt lists no candidate options; the actions (Cancel, Keep, Move, Hold) live in the incorporated doc and are applied inside each reading.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he wants it"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Rule 2 leaves out anything cancelled before Feb 9. Arthur's project description, in the project Leonard's ask points to, says the Unity Ads in the UA line were cancelled after October, and the last Unity invoice in Robert's mailbox is the October 2025 one (sent Nov 10). So Unity Ads is cancelled long before Feb 9 and gets no row.
Resolution evidence: SQL\_CONV2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "and anything cancelled before Feb 9"; SQL\_UADS\_DESC (Evals/task\_inputs/01\_Universe\_Inject.sql): "we cancelled the unity ads in the UA line after october, so they''re not in here"; UA\_INV (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/00015915.json pointer /messages/0/body): "Attached is your 10 2025 monthly invoice."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | B adds a Unity Ads row. |
| writes | SAME | No Linear issue exists for Unity Ads, so the Linear writes are the same. |
| destinations | SAME | Same sheet, Linear issues and \#winddown thread. |
| contents | DIFFERENT | B's every-row total is $1,653.47 higher. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV2

Resolution relevance challenge: The project description states the cancellation and rule 2 removes cancelled accounts; that is the exact difference.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: SQL\_CONV2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "and anything cancelled before Feb 9"; SQL\_UADS\_DESC (Evals/task\_inputs/01\_Universe\_Inject.sql): "we cancelled the unity ads in the UA line after october, so they''re not in here"; UA\_INV (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/00015915.json pointer /messages/0/body): "Attached is your 10 2025 monthly invoice."

Compared alternative: C
Resolution: EXCLUDED. Rule 6's exception applies only while a switch-over still has to happen. Oliver's Feb 13 comment says both games' support buttons now open email instead of Helpshift, which is newer than Leonard's Feb 11 plan, so nothing is left to switch before Zapier ends and its Closed row takes a dash.
Resolution evidence: SQL\_CONV6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends — then the day before it ends."; SQL\_HELP\_EMAIL (Evals/task\_inputs/01\_Universe\_Inject.sql): "both games'' support buttons now open email instead of helpshift"; SQL\_ZAPIER\_CMT (Evals/task\_inputs/01\_Universe\_Inject.sql): "cancelled zapier yesterday, their email says the plan runs until feb 27"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Zapier's by when differs (dash vs 2026-02-26). |
| writes | DIFFERENT | ENG-2476's comment would carry a different by when. |
| destinations | SAME | Same sheet, Linear issues and \#winddown thread. |
| contents | SAME | Totals and clashes are unchanged. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV6

Resolution relevance challenge: The newer comment reports the switch-over done, which removes the only ground for a date.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: SQL\_CONV6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends — then the day before it ends."; SQL\_HELP\_EMAIL (Evals/task\_inputs/01\_Universe\_Inject.sql): "both games'' support buttons now open email instead of helpshift"; SQL\_ZAPIER\_CMT (Evals/task\_inputs/01\_Universe\_Inject.sql): "cancelled zapier yesterday, their email says the plan runs until feb 27"

Compared alternative: D
Resolution: EXCLUDED. Newer source: Oliver's ENG-2439 comment (2026-02-13 15:12Z) says the export is done and both games' support buttons now open email instead of Helpshift. With the export and the switch-over done, rule 6 gives the Closed row a dash.
Resolution evidence: SQL\_CONV6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends — then the day before it ends."; SQL\_HELP\_EXPORT (Evals/task\_inputs/01\_Universe\_Inject.sql): "exported the full helpshift ticket history to the wind down folder today"; SQL\_HELP\_EMAIL (Evals/task\_inputs/01\_Universe\_Inject.sql): "both games'' support buttons now open email instead of helpshift"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Helpshift's by when differs. |
| writes | DIFFERENT | ENG-2439's comment would carry a date. |
| destinations | SAME | Same sheet, Linear issues and \#winddown thread. |
| contents | SAME | Totals and clashes unchanged. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV6

Resolution relevance challenge: The comment is two days newer than the plan and addresses exactly the pending switch-over.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: SQL\_CONV6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends — then the day before it ends."; SQL\_HELP\_EXPORT (Evals/task\_inputs/01\_Universe\_Inject.sql): "exported the full helpshift ticket history to the wind down folder today"; SQL\_HELP\_EMAIL (Evals/task\_inputs/01\_Universe\_Inject.sql): "both games'' support buttons now open email instead of helpshift"

Compared alternative: E
Resolution: EXCLUDED. Rule 2 leaves out anything cancelled before Feb 9, and rule 2's only exception is Sunset's list. Pond5's notice in Robert's mailbox says the membership was not renewed and ended on September 8, 2025, so it is out even though it sits in the Sound line.
Resolution evidence: SQL\_CONV2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "and anything cancelled before Feb 9"; SQL\_POND5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Your Pond5 Annual Membership was not renewed and ended on September 8, 2025."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | E adds a Pond5 row. |
| writes | SAME | Pond5 has no issue. |
| destinations | SAME | Same sheet, issues and thread. |
| contents | DIFFERENT | One extra $0 row. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV2

Resolution relevance challenge: The membership ended five months before Feb 9 by the vendor's own notice.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' only removes the sign-off step; it does not authorize materially different register rows, dates or totals.
Challenge evidence: SQL\_POND5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Your Pond5 Annual Membership was not renewed and ended on September 8, 2025."

Compared alternative: F
Resolution: EXCLUDED. Rule 5 makes a row Closed only when the vendor itself has confirmed, and says where. No Layer email, notice or final invoice is on record; ENG-2473 and Leonard's Slack say only that he cancelled in the app, which rule 5 defines as Requested.
Resolution evidence: SQL\_CONV5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Requested = one of us has cancelled or asked but nothing has come back from the vendor"; SQL\_LAYER\_CMT (Evals/task\_inputs/01\_Universe\_Inject.sql): "cancelled it in the app on the 11th"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Layer Closed vs Requested. |
| writes | DIFFERENT | ENG-2473 Done vs left open. |
| destinations | SAME | Same sheet, issues and thread. |
| contents | DIFFERENT | Layer status and by when differ. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV5

Resolution relevance challenge: The rule's own definitions decide it: one of us cancelled, nothing came back from the vendor.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' only removes the sign-off step; it does not authorize materially different register rows, dates or totals.
Challenge evidence: SQL\_CONV5 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Requested = one of us has cancelled or asked but nothing has come back from the vendor"

Compared alternative: G
Resolution: EXCLUDED. Rule 6 dates a Requested Cancel row by the day before the next charge. Layer's receipt says the next payment is March 3, 2026, so 2026-03-02; Leonard's access-until date agrees with that charge date.
Resolution evidence: SQL\_CONV6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends — then the day before it ends."; SQL\_LAYER\_RCPT (Evals/task\_inputs/01\_Universe\_Inject.sql): "Your next payment is on March 3, 2026."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Layer's by when differs by a day. |
| writes | DIFFERENT | ENG-2473's comment would carry a different date. |
| destinations | SAME | Same sheet, Linear issues and \#winddown thread. |
| contents | SAME | Totals and clashes unchanged. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV6

Resolution relevance challenge: Rule 6 names the day before the next charge and the receipt states that charge date.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: SQL\_CONV6 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends — then the day before it ends."; SQL\_LAYER\_RCPT (Evals/task\_inputs/01\_Universe\_Inject.sql): "Your next payment is on March 3, 2026."

Compared alternative: H
Resolution: EXCLUDED. Rule 10 counts only decisions that Sunset's list would undo. Sunset's email defines the list as the accounts that must stay active ('Nothing on this list should be closed…'); the Helpshift export is a separate request after it, so the no-export line is not a clash.
Resolution evidence: SQL\_CONV10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "A clash is a decision one of us already posted in \#winddown that Sunset''s list or SVB''s card terms would undo."; SQL\_SUNSET\_LIST (Evals/task\_inputs/01\_Universe\_Inject.sql): "Nothing on this list should be closed, downgraded or archived before the delivery review call Leonard booked with us."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same register. |
| writes | SAME | Same writes. |
| destinations | SAME | Same sheet, issues and thread. |
| contents | DIFFERENT | H lists a third clash. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV10

Resolution relevance challenge: Sunset's own email says what the list is; the Helpshift paragraph sits outside it.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' only removes the sign-off step; it does not authorize materially different register rows, dates or totals.
Challenge evidence: SQL\_SUNSET\_HELP (Evals/task\_inputs/01\_Universe\_Inject.sql): "For Helpshift, please export the full ticket history to Drive before your subscription ends."

Compared alternative: I
Resolution: EXCLUDED. The same Feb 12 message that keeps Slack and Google under Harmony Games also schedules the Google archive, so keeping an account under Harmony Games does not reverse cutting its plan or users. The Feb 11 free-plan and guest-account decision stands, and Sunset requires the paid plan with every user in place.
Resolution evidence: WD\_ARCH (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /190/text): "to archieve account on google after Feb 15"; WD\_GUEST (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /88/text): "I guess I’ll keep only a few accounts active and turn people into guest accounts"; SQL\_SUNSET\_SLACK (Evals/task\_inputs/01\_Universe\_Inject.sql): "Slack (stay on the paid plan"; SQL\_CONV10 (Evals/task\_inputs/01\_Universe\_Inject.sql): "A clash is a decision one of us already posted in \#winddown that Sunset''s list or SVB''s card terms would undo."; WD\_CHECKLIST (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /187/attachments): "Slack (down to 3 FT members)"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same register. |
| writes | SAME | Same writes. |
| destinations | SAME | Same sheet, issues and thread. |
| contents | DIFFERENT | I drops the Slack clash. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV10

Resolution relevance challenge: The keep line and the archive line sit in one message, so keeping is shown to coexist with cutting.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' only removes the sign-off step; it does not authorize materially different register rows, dates or totals.
Challenge evidence: WD\_KEEPDATA (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0ADGSZKR3R/2026-02.json pointer /190/text): "We keep accounts that has our data such as Slack, google, google analytics, github under Harmony Games until the data is extracted"

Compared alternative: K
Resolution: EXCLUDED. Rule 4 defines Keep as the keep list as amended in the thread, and the only reply in that thread is Arthur's Gusto cancel; rule 10's line about suggestions applies to clashes only.
Resolution evidence: SQL\_CONV4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Keep (my keep list, as amended in the thread)"; SQL\_GUSTO (Evals/task\_inputs/01\_Universe\_Inject.sql): "let''s cancel before mar 3"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Gusto Keep vs Cancel. |
| writes | SAME | ENG-2467 stays open either way. |
| destinations | SAME | Same sheet, issues and thread. |
| contents | DIFFERENT | Gusto row and the Keep and Hold total differ. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV4

Resolution relevance challenge: The doc author names the thread as amending the keep list.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' only removes the sign-off step; it does not authorize materially different register rows, dates or totals.
Challenge evidence: SQL\_CONV4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Keep (my keep list, as amended in the thread)"

Compared alternative: L
Resolution: EXCLUDED. Rule 8 prices an account without an owner figure from its last invoice brought to a month, quarterly ÷ 3. Singular's last invoice covers 12/01/2025 to 02/28/2026 for $6,250.00 and Leonard calls it quarterly, so $2,083.33.
Resolution evidence: SQL\_CONV8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Everything else: the monthly figure its owner gives in its Linear issue, or else its own last invoice or receipt brought to a month (annual ÷ 12, quarterly ÷ 3)."; SING\_INV (/tmp/hg/ev/singular\_invoice.txt): "Invoice for 12/01/2025 to 02/28/2026"; SQL\_SING\_CMT (Evals/task\_inputs/01\_Universe\_Inject.sql): "the next quarterly invoice is mar 1"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Singular's monthly cost differs ($6,250.00 vs $2,083.33). |
| writes | SAME | Same writes. |
| destinations | SAME | Same sheet, issues and thread. |
| contents | DIFFERENT | Singular cost and the every-row total differ. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV8

Resolution relevance challenge: The invoice period is three months and the rule says quarterly ÷ 3.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' only removes the sign-off step; it does not authorize materially different register rows, dates or totals.
Challenge evidence: SING\_INV (/tmp/hg/ev/singular\_invoice.txt): "Invoice for 12/01/2025 to 02/28/2026"

Compared alternative: M
Resolution: EXCLUDED. Rule 2 leaves out anything cancelled before Feb 9; Leonard told the publisher, in a channel Robert is in, that all adjoe campaigns stopped in June 2025.
Resolution evidence: SQL\_CONV2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "and anything cancelled before Feb 9"; SL\_ADJOE (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C09SWTHEMEW/2025-11.json pointer /72/text): "stopped all adjoe campaigns in June 2025"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | M adds an adjoe row. |
| writes | SAME | No adjoe issue. |
| destinations | SAME | Same sheet, issues and thread. |
| contents | DIFFERENT | One extra row. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV2

Resolution relevance challenge: The quote dates adjoe's stop before Feb 9.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' only removes the sign-off step; it does not authorize materially different register rows, dates or totals.
Challenge evidence: SL\_ADJOE (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C09SWTHEMEW/2025-11.json pointer /72/text): "stopped all adjoe campaigns in June 2025"

Compared alternative: N
Resolution: EXCLUDED. Rule 2 leaves out anything cancelled before Feb 9; Leonard cancelled Typecast in July 2025 and Robert's comment says payment stopped after the summer, so the free tier is what is left after a cancellation.
Resolution evidence: SQL\_CONV2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "and anything cancelled before Feb 9"; SL\_TYPECAST (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C04UEQVDVB7/2025-07.json pointer /16/text): "this typecast thing I’m canceling"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | N keeps a Typecast row. |
| writes | DIFFERENT | ENG-2442 open vs Canceled. |
| destinations | SAME | Same sheet, issues and thread. |
| contents | DIFFERENT | One extra $0 row. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV2

Resolution relevance challenge: The July 2025 cancellation is exactly rule 2's test.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' only removes the sign-off step; it does not authorize materially different register rows, dates or totals.
Challenge evidence: SL\_TYPECAST (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C04UEQVDVB7/2025-07.json pointer /16/text): "this typecast thing I’m canceling"

Compared alternative: O
Resolution: EXCLUDED. Rule 8 prices an account without its own ledger line by the monthly figure its owner gives in its Linear issue first. Leonard, the ENG-2464 assignee, gives this month's invoice as $298.13; the Subscriptions sheet was replaced by the project.
Resolution evidence: SQL\_CONV8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Everything else: the monthly figure its owner gives in its Linear issue, or else its own last invoice or receipt brought to a month (annual ÷ 12, quarterly ÷ 3)."; SQL\_GWS\_FIG (Evals/task\_inputs/01\_Universe\_Inject.sql): "this month''s invoice was $298.13"; SQL\_PROJ\_REPLACES (Evals/task\_inputs/01\_Universe\_Inject.sql): "This replaces my subscriptions sheet from Tuesday."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Workspace cost differs. |
| writes | SAME | Same writes. |
| destinations | SAME | Same sheet, Linear issues and \#winddown thread. |
| contents | DIFFERENT | Both totals differ. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV8

Resolution relevance challenge: The owner figure is rule 8's first source and is now stated in the issue.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: SQL\_CONV8 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Everything else: the monthly figure its owner gives in its Linear issue, or else its own last invoice or receipt brought to a month (annual ÷ 12, quarterly ÷ 3)."; SQL\_GWS\_FIG (Evals/task\_inputs/01\_Universe\_Inject.sql): "this month''s invoice was $298.13"; SQL\_PROJ\_REPLACES (Evals/task\_inputs/01\_Universe\_Inject.sql): "This replaces my subscriptions sheet from Tuesday."

Compared alternative: P
Resolution: EXCLUDED. Rule 2 leaves out anything cancelled before Feb 9, whether or not access runs on. Leonard's ENG-2463 comment says Calendly was cancelled in October 2025 and just runs out, so it gets no row and ENG-2463 is Canceled.
Resolution evidence: SQL\_CONV2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "and anything cancelled before Feb 9"; SQL\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql): "we cancelled calendly in october right after the annual charge, it just runs out"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | B keeps Calendly as a row. |
| writes | DIFFERENT | ENG-2463 open vs Canceled. |
| destinations | SAME | Same sheet, Linear issues and \#winddown thread. |
| contents | DIFFERENT | Every-row total differs by $8.00. |

Authority chain: P → SQL\_ASK\_DOC → SQL\_CONV2

Resolution relevance challenge: The comment dates the cancellation and rule 2 uses the cancellation date, not the access end.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: SQL\_CONV2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "and anything cancelled before Feb 9"; SQL\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql): "we cancelled calendly in october right after the annual charge, it just runs out"

Strongest-alternative challenge (B): B changes the every-row total by $1,653.47 and rule 3's wording ('whether or not it has a ledger line') pulls toward adding Unity Ads; only the project description's cancellation plus rule 2 removes it.
Challenge evidence: SQL\_UADS\_DESC (Evals/task\_inputs/01\_Universe\_Inject.sql): "we cancelled the unity ads in the UA line after october, so they''re not in here"; SQL\_CONV2 (Evals/task\_inputs/01\_Universe\_Inject.sql): "and anything cancelled before Feb 9"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5)

Every value the register and the reply need can be read through the Agent's tools. The revision-12 blocker is fixed: Leonard's ENG-2464 comment now gives Google Workspace's figure in readable text ("this month''s invoice was $298.13"), which is rule 8's first source, so the Agent no longer needs the invoice PDF. It agrees with that PDF (invoice 5473295269, "Summary for Jan 1, 2026 - Jan 31, 2026", total $298.13, sent to Robert 2026-02-02).

| Ask | Required capability | Tool(s) | Status |
|---|---|---|---|
| Read the ask and sources | Slack, GDocs, GSheets, Gmail, Trello, Linear, Snowflake, GitHub, GCal reads | cataloged read/search tools | SUPPORTED (no required value sits only in a Gmail attachment) |
| Create the register | create a sheet, write cells | `gsheets_create_spreadsheet`, `gsheets_values_update` / `gsheets_batch_update` | SUPPORTED |
| Share as editors | share by email with a role | `gdrive_share_file` | SUPPORTED |
| Settle Linear issues | change state, comment | `linear_update_issue` (state), `linear_create_comment` | SUPPORTED |
| Thread reply | post with thread_ts | `slack_send_message` (`thread_ts`) | SUPPORTED |

- A1 service availability: Snowflake and Confluence are live and unscoped (service-availability-v1).
- B data feasibility: every source exists (base or SQL overlay), including the January ledger lines rule 8 needs (FIN-000687 AWS −1,485; FIN-000688 applovin −9.80; FIN-000689 meta −2,843.84).
- C dimensional feasibility: the register's per-account columns map to fields that exist.
- D numeric observability: PASS. Owner figures are plain Linear comment text; ledger `amount_usd` carries cents; Singular's $6,250 quarter is readable in the past-due notice in Robert's mailbox ("outstanding balance of $6,250.00") together with Leonard's "next quarterly invoice", so $2,083.33. Rendering of `snowflake_execute_query` output isn't established by the catalog (catalog limit, recorded as an evidence limit, not a fail).
- E persona-scoped reads: every required scoped read is Robert-visible (#winddown, #prototype, #issuefeed, #admin_foundersonly, #executives, the publishing-ext channel; Robert's mailbox; GDocs/GSheets shared with Robert; Robert's calendar).

**Persona ACL Reachability:** PASS (5). See E above.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5). Each write is defined (one sheet, two shares, one state and comment per issue, one thread reply) and the delegation line ("go with your read on the details, i don't need to sign off on it first") assigns every write to the Agent. No "I'll" self-action statement.

**Contrived / Unnatural:** PASS (5). No exact timestamps, opaque IDs, format rules, riddles, hidden destinations, audit-form wording or if-chains.

**Alignment with Today's Date:** PASS (5). "friday" = 2026-02-13 (the ask's created_at 17:21Z); "after the 15th" is a future plan against the 2026-02-14 clock and matches Leonard's to-do ("to archieve account on google after Feb 15", 2026-02-12) and checklist ("Google (archive unused accounts on Feb 15)"). Every injected record is dated before the clock.

**Originality / Sample Similarity:** N/A. No comparison samples supplied.

**Truthfulness:** PASS (5). Premises P1–P4 verified in the record.

| Entity/fact | Record | Accurate? |
|---|---|---|
| Leonard asked Robert in #winddown on Friday | SQL msg `9e245e76…`, C0ADGSZKR3R (#winddown), EMPLOYEE_0038, 2026-02-13T17:21:07Z | Yes |
| archives anything on google after the 15th | Base #winddown `fdd87e27…` (Leonard, 2026-02-12): "to archieve account on google after Feb 15" | Yes |
| the linear issues / like he asked | SQL Linear project "Shutdown – accounts", ENG-2438–ENG-2483 (45 issues; ENG-2459 unused); ask "Settle each Linear issue as you go and leave a line on each" | Yes |
| his thread | Leonard's top-level injected message | Yes |
| what we already decided | Base keep list `6d8c8d8a…`, to-do list `fdd87e27…`, checklist `ffb65137…` | Yes |

**Tool Use & Cross-service:** PASS (5). Linear (states, owners, owner figures), Gmail (receipts, Sunset's list), Snowflake (ledger additions and costs), Slack (decisions, clashes) and GSheets (costs-tab multi-vendor lines) each change graded facts.

**Investigation + Action:** PASS (5).

**Coherence (Bolt-on):** PASS (5).

**Business Function:** NON-FAIL (3). The assignment is "Executive" (Founders / Exec / Strategy), but vendor close-out bookkeeping fits Finance / Legal / HR / Ops at least as well. Unchanged from the last review; the QC form has no fail option here.

## 7. Phase 3: Universe Feasibility

**Data Existence:** PASS (5). All four prompt premises and every incorporated source exist and can be retrieved through cataloged tools.

**Cross-Service Coherence:** NON-FAIL (3)

Revision 13 fixed both fail-level conflicts from the last review:
- Layer: the receipt (2026-02-03, "Your next payment is on March 3, 2026.") now agrees with Leonard's #prototype "we have access until March 3rd". No other Layer receipt is in Robert's mailbox (complete scan; only newsletters).
- Linear and DocuSign vs the costs tab: ENG-2448 ("the p&l stops after the 2024 payment") and ENG-2469 ("the p&l missed last april''s charge") explain the gaps again.

New revision-13 claims checked against base data:
- Unity Ads cancelled after October: the last Unity Technologies invoice in Robert's mailbox is "your 10 2025 monthly invoice" (CINV_00022209, sent 2025-11-10; complete scan finds none later), and Robert's own DM on 2026-02-03 ("I'll pay for some Unity Ads out of my own pocket if necessary") fits a company account that is off. Consistent.
- Calendly cancelled in October right after the annual charge: the costs-tab Calendly row shows 96 only in October positions (5, 17, 29; position 29 is October 2025 by the HG P&L header). Consistent.
- Helpshift support moved to email: matches Leonard's Feb 11 plan ("We can just open up the email app and let players send email"); no base GitHub record contradicts it (no Helpshift PR or commit in Feb 2026).
- Google Workspace $298.13: matches the Feb 2 invoice PDF in Robert's mailbox.

Remaining inconsistency in task-touched data:
1. **HG Costs header years (Temporal, base GSheets; single minor).** The HG Costs tab labels positions 21–31 with 2024 dates and 32–43 with 2025 dates, while the HG P&L tab of the same spreadsheet labels position 28 "2025-09-25". The injected Figma receipt (Sep 11, 2025, $1,212) matches the value at position 28, which the costs tab labels "2024-09-25". No graded value is read from these dates (costs come from owner figures, invoices and the ledger), so under the date-slip rule this is one minor inconsistency: NON-FAIL.

Advisory (not scored): ENG-2463 (Calendly) and ENG-2480 (Notarize) carry comments by Leonard with the same timestamp, 2026-02-13T16:38:44Z. Not a contradiction; giving one of them a different second would look more natural.

Known base-data issues (not scored; keep the rubric and OEs off them):
- **AWS: costs tab vs FINANCE_LEDGER, Sep–Dec 2025.** The task prices AWS from the January ledger line FIN-000687 (−1,485), which agrees with ENG-2455.
- **HG Costs "UA" vs ledger `marketing_ua`.** For example November 2025: costs tab 4,806.02 vs ledger meta −650.46 + applovin −35.02. The register takes meta and applovin from their January ledger lines and leaves Unity Ads out on the project description, so no graded value uses the UA line's amounts.
- **Unity Ads spend isn't in FINANCE_LEDGER** (Oct 2025 invoice $1,653.47; no Unity Ads line). Not needed now that the project description removes Unity Ads.

Injection SQL considered: Yes. Static integrity evidence: REUSED from `0_injection.md` (sha256 `8f780bb245a9…`), checks A–C PASS on this SQL hash. Added Slack messages' authors are channel members (Arthur and Leonard in #winddown, Oliver in #prototype), and apostrophes are doubled. Prompt-specific sources, access and configuration: supported.

## 8. Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Every tested fork settled by a quoted persona-visible record (generated comparison above) |
| Prompt | Feasibility | 5 | Workspace figure now readable in ENG-2464; every value tool-visible |
| Prompt | Persona ACL Reachability | 5 | Every scoped read is Robert-visible |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One write per issue; delegation clear |
| Prompt | Contrived / Unnatural | 5 | Natural, unpolished delegation |
| Prompt | Alignment with Today's Date | 5 | Friday = Feb 13; the archive plan is future |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | Premises P1–P4 verified |
| Prompt | Tool Use & Cross-service | 5 | Several services each change graded facts |
| Prompt | Investigation + Action | 5 | Writes depend on investigation |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | Leonard asked Robert directly |
| Prompt | Business Function | 3 | Fits Finance/Legal/HR/Ops at least as well as Exec |
| Prompt | Assigned Competency | 5 | Corporate Ops vendor close-out |
| Prompt | Assigned Task Skill | 5 | A decision per account plus clashes |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | All sources exist and are retrievable |
| Universe | Cross-Service Coherence | 3 | One minor costs-tab header year slip no graded value uses |

## 9. Issues Found

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | HG Costs header labels positions 21–43 a year early versus the HG P&L tab (the injected Sep 2025 Figma receipt's $1,212 sits under "2024-09-25"). Base data; no graded value depends on it | Minor | Cross-Service Coherence |
| 2 | Business function: the vendor close-out work fits Finance/Legal/HR/Ops at least as well as Executive | Minor (blocks a 5 only) | Business Function |
| 3 | ENG-2463 and ENG-2480 comments share the timestamp 2026-02-13T16:38:44Z | Advisory | (not scored) |

## 10. Recommended Improvements

None of these is required for the stage to count as passed (NON-FAIL counts as a pass for /prompt).

1. **Costs-tab header (Issue 1).** It's base data and changes no graded value. Keep the rubric and OEs off the costs tab's column dates.
2. **Business function (Issue 2).** Fixed by the taxonomy assignment, not the prompt; leave as is.
3. **Comment timestamps (Issue 3, optional).** Give the ENG-2463 Calendly comment a different second from the ENG-2480 Notarize comment.
4. **For /oe and /rubric:** the register figures to build on are in the Reading A derivation (section 4): every-row total $11,045.13, Keep and Hold total $1,249.04; Done ENG-2439, ENG-2440, ENG-2474, ENG-2476, ENG-2478; Canceled the 19 left-out issues plus ENG-2461; Helpshift and Zapier by when a dash; Layer 2026-03-02; clashes: the Slack decisions and the Google archive after Feb 15.
5. **Schema risk (optional, unchanged).** `linear_projects.links_json`, `linear_project_teams` and `linear_project_members` aren't in the schema snapshot. If the live tables lack them, the whole SQL rolls back. Dropping `links_json` and the project_teams/project_members rows is the safe option.
6. **Confluence decoy (optional).** Injection SQL can't edit Confluence, so the `page_ua_vendor_closeout` page and its version won't appear. No graded fact depends on that decoy; drop the two inserts or leave them.
7. Next: send `/hardness`, then `/oe` and `/rubric`.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review, its record, scores and verdict.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 4 prompt sentences; 28 register rows × 6 columns, both totals, sharing, 45 Linear end states, thread and clash set (27 forks) | 4 | 0 |
| P2 | 4 prompt sentences; services, ACL, catalog writes, numeric observability, base and injected data | 2 | 1 (P2-DR2, already Issue 1) |
| P3 | 22 prompt claims plus clock, shutdown, departed-person and SQL static checks | 3 | 0 (advisories) |
| P4 | 3 prompt sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR1 | P1 | "anything that clashes with what we already decided" | #winddown "yeah free version"; checklist ffb65137 "- [x] Slack (down to 3 FT members)"; Sunset "Slack (stay on the paid plan" | §2 contents | Unique Ground Truth | REJECTED | Reading B (Slack not a clash) is ruled out by Leonard's own posted checklist, "- [x] Slack (down to 3 FT members)", a decision posted in #winddown, which Sunset's "every user in place" and "Slack (stay on the paid plan — the free plan hides history older than 90 days)" undo (rule 10). The Slack clash is in Reading A either way |
| P1-DR2 | P1 | "build the register the way he wants it" | ledger adjoe Apr–Jun 2025; SVB payment to Adjoe Aug 29 2025 | §2 set membership | Unique Ground Truth | REJECTED | publishing-ext channel (Robert is a member), Leonard 2025-11-24: "hence we stopped all adjoe campaigns in June 2025. Since then, There has not been any meaningful marketing activity for the game." + rule 2 "anything cancelled before Feb 9". The Aug payment settles June's spend |
| P1-DR3 | P1 | "settle each of the linear issues like he asked" | ENG-2461 "same account as the quickbooks issue"; rule 1 "the newer issue is the duplicate" | §2 writes | Unique Ground Truth | REJECTED | Project description: "One issue per vendor we pay or used to pay" and "Canceled if it doesn''t belong on the list". A second issue for the same vendor, which rule 1 names the duplicate, doesn't belong on a one-issue-per-vendor list, so ENG-2461 is Canceled |
| P1-DR4 | P1 | "build the register the way he wants it" | ENG-2460 "intuit takes the $115 off the svb card on the 4th"; keep list "Intuit" | §2 label | Clarity | REJECTED | Same account, same row, Keep, $115.00, Leonard, 2026-02-19 and the same writes under either name; label wording only. The rubric should accept QuickBooks or Intuit |
| P2-DR1 | P2 | "build the register the way he wants it" | FINANCE_LEDGER FIN-000687 AWS −1,485 and 2025 AWS lines; HG Costs "Servers (AWS)" 0 / 15; HG Costs "UA" 3820 / 4806.02 / 610 | §3 coherence | Cross-Service Coherence | REJECTED | Snowflake vs GSheets base conflict the SQL didn't add (base-data-v1). The graded AWS figure is the January ledger line, which ENG-2455 corroborates ("all of aws was $1,485 in january"); no graded value uses the costs-tab AWS or UA amounts (the 2026 columns are forecast columns). Listed under Known base-data issues (not scored) |
| P2-DR2 | P2 | "build the register the way he wants it" | HG Costs header "2024-09-25T00:00:00" vs HG P&L "2025-09-25T00:00:00"; Figma $1,212 under the former | §3 date slip | Cross-Service Coherence | CONFIRMED | Same as Issue 1: one minor temporal inconsistency no graded value uses (NON-FAIL) |
| P3-DR1 | P3 | "before he archives anything on google after the 15th" | #company-internal 2026-02-11 "I'll archive everyone's Google Account's by Feb 15"; #winddown 2026-02-12 "to archieve account on google after Feb 15" | §truthfulness | Truthfulness | REJECTED | The prompt matches the newest record; the clash with Sunset's "please don''t archive or delete any" is the same either way. No defect |
| P3-DR2 | P3 | n/a (SQL) | `linear_projects.links_json` not in snapshot | SQL static | Injection advisory | REJECTED | Snapshot gap already carried as Eval 0 A1 (Recommended Improvements #5) |
| P3-DR3 | P3 | n/a (SQL) | `confluence_pages`, `confluence_page_versions`, `linear_project_teams`, `linear_project_members` missing from snapshot | SQL static | Injection advisory | REJECTED | Disclosed schema limit; no graded fact depends on the Confluence decoy (Recommended Improvements #6) |
| P4-DR1 | P4 | "and then reply to him in his thread" | prompt text; Leonard's ask "then reply here with the two monthly totals" | §6.6 step list | Contrived / Unnatural | REJECTED | One casual "then" for a real dependency (the reply carries the register's totals) that mirrors Leonard's own ask; no first/finally sequence. P4 itself rated it no fail |

Effect on verdict: unchanged. No confirmed finding changes a dimension; P2-DR2 is the costs-tab header slip already scored as the single minor Cross-Service Coherence issue (3).

Advisories from the passes (not scored): Leonard's Helpshift confirmation email (only in Leonard's mailbox, not visible to Robert) reads "effective February 29,2025"; the answer uses ENG-2439's "discontinuing us at the end of february", so it has no graded effect. The Wind Down folder isn't shared with Robert, but the doc and the export zip are shared with him directly. Anonymized tokens ([PERSON_NAME_0499] Singular, [PERSON_NAME_0250] GitHub, [USERNAME_30019] dbt, [PERSON_NAME_20852] Kapwing) each have a Robert-visible mapping.

- F1: Unity Ads row | Reading A: left out | Reading B: Cancel row, $1,653.47 | Settled by: "we cancelled the unity ads in the UA line after october, so they''re not in here" + rule 2 "anything cancelled before Feb 9"
- F2: Zapier by when | Reading A: dash | Reading B: 2026-02-26 | Settled by: "both games'' support buttons now open email instead of helpshift" + rule 6 "unless an export or a switch-over still has to happen"
- F3: Helpshift by when | Reading A: dash | Reading B: 2026-02-27 | Settled by: "exported the full helpshift ticket history to the wind down folder today" and "both games'' support buttons now open email instead of helpshift" (2026-02-13, newer than "We gotta move domino delights and zombie match off Helpshift before Feb 28th.")
- F4: Google Workspace cost | Reading A: $298.13 | Reading B: $297.60 (costs tab) or $300 (old sheet) | Settled by: "this month''s invoice was $298.13" + rule 8 "the monthly figure its owner gives in its Linear issue"
- F5: Layer by when | Reading A: 2026-03-02 | Reading B: 2026-03-03 | Settled by: "Your next payment is on March 3, 2026." + rule 6 "the day before the next charge"
- F6: Calendly | Reading A: out, ENG-2463 Canceled | Reading B: $8.00 row, open | Settled by: "we cancelled calendly in october right after the annual charge, it just runs out" + rule 2
- F7: Layer status | Reading A: Requested | Reading B: Closed | Settled by: rule 5 "Requested = one of us has cancelled or asked but nothing has come back from the vendor"
- F8: Slack clash | Reading A: clash | Reading B: not a clash | Settled by: "- [x] Slack (down to 3 FT members)" against "Slack (stay on the paid plan"
- F9: adjoe | Reading A: out | Reading B: row | Settled by: "hence we stopped all adjoe campaigns in June 2025" + rule 2
- F10: ENG-2461 Intuit | Reading A: Canceled | Reading B: open | Settled by: "One issue per vendor we pay or used to pay" + rule 1 "the newer issue is the duplicate"
- F11: QuickBooks/Intuit label | wording only, same row; the rubric should accept either name
- F12: Helpshift no-export as a clash | Reading A: not a clash | Reading B: clash | Settled by: "Nothing on this list should be closed, downgraded or archived before the delivery review call Leonard booked with us." + rule 10 "Sunset''s list"
- F13: Typecast | Reading A: out | Reading B: $0 row | Settled by: "this typecast thing I’m canceling" + rule 2
- F14: Pond5 | Reading A: out | Reading B: $0 row | Settled by: "Your Pond5 Annual Membership was not renewed and ended on September 8, 2025." + rule 2
- F15: Singular cost | Reading A: $2,083.33 | Reading B: $6,250.00 | Settled by: "outstanding balance of $6,250.00" + "the next quarterly invoice is mar 1" + rule 8 quarterly ÷ 3
- F16: Gusto | Reading A: Cancel | Reading B: Keep | Settled by: "Keep (my keep list, as amended in the thread)" + "let''s cancel before mar 3"
- F17: GitHub/dbt Hold vs Move; Metabase Move; BigQuery and Trello Hold; meta/applovin January lines; Soundly $10.00; CodeRabbit $45.00; Unity $2,348.50; Cursor still Cancel; $30 game-ops lines out; SaaS vendors ledger line no row; DocuSign owner Robert | Settled by: the records P1 quoted in its fork list (Sunset's amendment "The rest of the list stands.", rule 8, ENG-2438, ENG-2474, Soundly's Feb 11 email, rule 10, the project note "the two $30 game-ops lines I''m handling myself", "docusign goes to robert from here")

Platform defects: none.

### FINAL VERDICT: NON-FAIL

Score: 3

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: None required for this stage (NON-FAIL counts as a pass for /prompt). Send /hardness next, then /oe and /rubric. Optional: drop `links_json` and the Confluence page inserts from the SQL (if you do, re-run /injection and /prompt first).

Evidence limits: The Docs PDFs/XLSX were not re-extracted this run (same Eval hash as the earlier extraction). The live injection schema is unverified (links_json, linear_project_teams, linear_project_members, Confluence tables). The rendering of Snowflake query output isn't established by the catalog. PDF amounts quoted here were read by the evaluator; the Agent doesn't need them.

**Lowest Dimension:** Business Function / Cross-Service Coherence - 3 - Executive fits less well than Finance/Legal/HR/Ops; one minor costs-tab header year slip that no graded value uses.

**Summary:** Revision 13 fixed all five issues from the last review: Google Workspace has a readable owner figure, the project description settles Unity Ads, Oliver's comment settles Helpshift and Zapier, the Layer receipt agrees with base Slack, and the P&L notes are back. Every fork the review and the blind recheck tested is settled by a persona-visible record, so UGT, Feasibility and Truthfulness pass. Only the business-function fit and one minor base-data header slip keep it at 3.

Eval version: task-quality-v1

Eval release SHA-256: 6478616fae461adfff81f45b2a523017b7a8e042bf02b6afc8c113d659886b8f

Reviewed prompt SHA-256: cfab17798d359095db76a085acc3b201b1c036568240eb062244f78651d9ee9c

Review context SHA-256: 2205e07820412aa6b261a084751fc7390921e0cdc892e1e74bcbfd8c4d139a5c

Prompt record SHA-256: 5931f6bb62ac0f8c9d3622952ecd91824378c1f0a604b15d85663aea26504655
