## PROMPT EVALUATION REPORT (Eval 1, main reviewer draft, before Phase 5)

### Task: Leonard's stockholder close-out during the wind-down (holder sheet, investor letter, holder note drafts, Linear holder issues, Griffin heads-up, #winddown reply, KPMG audit confirmation)
### Assigned Persona: Leonard Hayes - Co-founder & Creative Director (leonard_hayes, leonard.hayes@harmonygames.co, Executive)
### Assigned Business Function: Executive
### Assigned Competency: Finance
### Assigned Task Skill: Authoring
### Assigned Horizon: Long Horizon (task type long-horizon)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

---

### Scope and input fingerprints

| Item | Value |
|---|---|
| Review | Local Eval 1 run, main reviewer, chat/scratch mode (review folder `prompt_review_rev1`), review date 2026-11-08 |
| Universe | normal, `hg4-2026-08-31-v37.zip` (archive sha256 2913eb8b…e21a); `Evals/references/universes/normal/universe_manifest.json` sha256 5e01ac44…e450 |
| Prompt `04_Prompt.txt` | sha256 45766344a3e48641af4dae0cf72c30c0c9c2d3affe3b62e3fdf56f26dbe83bd9 (134 words) |
| Assignment `00_Task_Assigned_Inputs.md` | sha256 49d5e1d5…c6ce |
| Injection SQL `01_Universe_Inject.sql` | sha256 6f3b18994e1a507b5829f5b2cfb6ff36897dcacc0b192c8649e97845b4ec200d (121 INSERT, 7 UPDATE; read in full before any base search) |
| Date input `02_Universe_Date.txt` | Feb 14, 2026 (normal) |
| Reference files | None used by the prompt |
| Error/async config, dynamic context | None supplied |
| Search path | `Task_Authoring/tools/hg.py search/records` only; no Universe_* folder read directly; no SQL executed |
| Local overrides honoured | Evals input store not used (no `hg_store_input.py`, no writes under `Evals/`); `hg_prompt_checks.py render-ugt` not run (it binds to the Evals store), so the UGT section below is hand-built in the same shape |

### Injection Gate
- State: SQL sha256 6f3b1899… has no matching Eval 0 report in this review folder. `prev/eval0_report_on_sha_bc72db9c.md` is for a different SQL version and was not opened or reused (independence; stale by hash).
- Eval 0 verdict on this SQL: PENDING (orchestrator will supply).
- Static checks I touched while checking the prompt (not a full Eval 0): Slack authors of the 7 SQL messages (EMPLOYEE_0038 Leonard, EMPLOYEE_0025 Arthur) are both in `members` of C0ADGSZKR3R #winddown (`slack/channels.json /154`). Every apostrophe inside quoted SQL strings I read is doubled (`what''s`, `family''s`, `I''ll`, `don''t`, `Griffin''s`). Linear identifiers ENG-2438…ENG-2463 do not collide with base (`linear/data.json /issues` lookup: ENG-2437 is the highest existing hit; ENG-2438/2450/2463 absent). Project id `ec2ea957-…` absent from base. All SQL event timestamps are ≤ 2026-02-13T18:21:46Z (< clock) and the SQL Slack rows (≤ 02-13 02:23Z) sit before the NB-6 Slack cutoff (02-13 10:03Z).
- Eval 0 findings on records this prompt depends on: to be merged when the Eval 0 report arrives.

---

### Intake and assignment (Phase 1.5 binding)

| Field | Recorded value | Source |
|---|---|---|
| Persona | Leonard Hayes, Co-founder & Creative Director, leonard_hayes / leonard.hayes@harmonygames.co, Executive | `00_Task_Assigned_Inputs.md`; exact match in `Evals/references/persona/roster.json` |
| Business function | Executive → "Founders / Exec / Strategy" (task_categories.md) | assignment |
| Competency | Finance | assignment |
| Task skill | Authoring | assignment |
| Horizon | Long Horizon (long-horizon) | assignment |

### Checklist status (all NEW in this review; nothing reused)

| Step | Status |
|---|---|
| Intake, Injection gate | Done (gate PENDING on Eval 0) |
| Phase 0.1 references (Eval 1 in full, EXECUTION, ENVIRONMENT, SEARCH, WORKFLOW guide view, scoring groups, common_errors, prompt_qc_examples, long_horizon, task_categories, scoring_notes, acl.md, roster, catalog, known_data_issues/normal.md) | Done. Evidence limit: `Evals/Docs/` PDFs/XLSX not re-extracted this run; the bundled scoring.json groups and Eval 1 overrides were applied instead |
| Phase 0.2 universe exploration | Done for every prompt claim and the holder cohort (see ledger) |
| Phase 0.3 example task | Not re-read (calibration only; evidence limit) |
| Phases 1–4 | Done below |
| Phase 5 deep recheck | Skipped by instruction (P1–P4 run as separate blind agents) |

---

### Evidence ledger (sources the prompt and its incorporated records lead to)

Prompt incorporation chain (`prompt-incorporation-v1`): the prompt says "my close-out notes doc has how each holder gets handled… Can you take care of all of it the way those lay it out?" where "those" = the holder project in Linear and the close-out notes doc. Both are therefore authorized instruction sources. The Linear project description further incorporates "my close-out notes" and "the sheet is what Sunset asked for" (Sunset's email, scoped to the sheet). The notes incorporate "my draft from #winddown", "the update outline", the Feb 12 Board position thread and "my list in #winddown" (whose SQL thread replies amend the notes: family rule, Covered label, Arthur also gets the sheet).

| # | Source | Locator | Provenance | Leonard visibility | Role |
|---|---|---|---|---|---|
| S1 | Linear project "Holder records" | `linear.linear_projects` id ec2ea957-fc8e-4958-b809-0fb735b1e916, lead usr_63fffeb4fab5233e (Leonard) | SQL | Linear unscoped | Instructions: one issue per Carta holder; state rule Canceled/Todo/Done; comment "why" on every issue without its own note; KPMG reply-all once the sheet is done; "I'll pass it to Sunset myself" |
| S2 | 26 Linear issues ENG-2438…ENG-2463 + 52 comments | SQL `linear.linear_issues` / `linear_comments` | SQL | unscoped | Cohort, decoy "Nov 2024 owner list" figures, "Last written contact before Feb" dates |
| S3 | GDoc "Stockholder close-out notes" | f_a37b403d5200d4f0a31d31, owner Leonard, in folder d_601064334a0b493022fe83 | SQL | owner | Instructions (what needs doing; how each holder gets handled; sheet labels); says it replaces the earlier outreach notes |
| S4 | GDoc "Holder outreach notes" | f_762c60832854d3e7a7f7df | SQL | owner | Superseded decoy (one BCC mail, Nov 2024 list, Robert+Arthur review) |
| S5 | Folder "Stockholder close-out" | d_601064334a0b493022fe83 under Leonard's root d_63fffeb4fab5233ed5bb73 | SQL | owner | Destination for sheet and letter |
| S6 | GSheet "Holder list (draft)" | f_5ecaa967db3adcfa440b09, in S5 | SQL | owner | Stale decoy copied from the Nov 2024 list |
| S7 | GSlides "Harmony Games February 26 Update" | f_75dddccabb26eeea4842c8, in S5 | SQL | owner | "the update outline" (sections: What happened / Where things stand / What it means for you / What happens to the games and the IP) |
| S8 | #winddown (C0ADGSZKR3R) | `slack/messages/C0ADGSZKR3R/2026-02.json`: investor draft msg 22f31c82479f4be97aecdfc97ae6840d (02-09 19:18Z, "Hi everyone, I'm writing to share a difficult update…"); promise msg 5e5c2d16 ("I'll reach out to investors one by one"); Leonard's list e3e198cc6e3f866a032d34c5f69e39f9 (02-12 22:17Z: Carta terminations / angels / Sunset onboarding); "Carta terminations are done" 6668e0e0 | base + SQL thread replies 4f54dff9, 0e3d2253, 846c625f, 7440b1ba and 3 top-level SQL posts | Leonard member | Investor draft; list to reply under; family rule; Covered label; Arthur gets the sheet |
| S9 | Task List sheet | f_31115ddb6ed866f2b10d60 (`gsheets /sheets_spreadsheets/76`), shared with Leonard | base | shared | "Send email to investors" row (the notes' "investor email on the Task List") |
| S10 | Board position thread | `gmail threads/leonard@harmonygames.co_1856958794180374704.json` (PERSON_4337 resigns 02-12 22:05Z; Leonard replies 22:14Z) | base | Leonard mailbox | Destination of the Griffin heads-up |
| S11 | Feb 9 shutdown mail to Griffin's partner | `…_1856675475513544349.json /messages/13` (Leonard → PERSON_4337, 2026-02-09 11:12 PT, "we've decided to shut the company down") | base | Leonard mailbox | Griffin funds already told |
| S12 | KPMG audit request thread | SQL `gmail_threads` leonard.hayes@harmonygames.co/1857029474983245439 (request 02-13 16:48Z; Leonard ack 17:12Z; clarification 17:37Z) | SQL | Leonard mailbox | KPMG answer contents and reply-all |
| S13 | Sunset intake email | SQL thread …/1857034369525983506 (02-13 18:06Z) + Leonard reply "I'll get you the sheet next week" | SQL | Leonard mailbox | Sheet spec |
| S14 | Robert → PERSON_3941 "we're closing the company" | SQL msg in leonard thread …/1773963101399472184 (cc Leonard) | SQL | cc Leonard | PERSON_3941 told |
| S15 | Carta "Termination details for …" (14 mails) | e.g. `…_1856960351896429942` Marcus ES-7 22,889/12,875, last day 2026-04-30; `…_1856960478782792748` [PERSON_NAME_0051] ES-14 3,866/1,530, last day 2026-02-21; `…_1847333272519888206` [PERSON_NAME_0038] ES-17 last day 2026-01-28; `…_1830952527208439510` Victor ES-6 last day 2025-07-16; `…_1808666480668498098` [PERSON_NAME_0100] ES-2 last day 2024-11-01 | base | Leonard mailbox | Option lines, vested, last days |
| S16 | Carta activity digests (21 mails, 2023-08-22 … 2024-12-25) | e.g. `…_1774928765255297348` (SSP-01 Griffin II, SSP-02 Side Fund, CS-01..03 founders), `…_1777100628672295991` (SSP-10 "Husnu Matthew Collins"), `…_1782897835407336831` (ES-9 Husnu Matthew Collins, ES-11 PERSON_3941) | base | Leonard mailbox | Certificates and grants |
| S17 | Nov 2024 owner list | `…_1816809274978043917` (Leonard SENT 2024-11-26; 27 owners, e.g. "[PERSON_NAME_11362] – 86,470 shares") | base | Leonard mailbox | Resolves the SQL "Nov 2024 owner list" references and the slide's "27 holders" |
| S18 | Seed SOP split | `…_1771880236343640719` (Griffin II 2,662,255; Side Fund 84,438) | base | Leonard mailbox | KPMG "what each fund holds" |
| S19 | Advisor option allocations | `…_1773160163779741845` (Matthew Collins 61,038; [PERSON_NAME_0090] 30,518; PERSON_1287_NAME 6,104; PERSON_3941 6,104) | base | Leonard mailbox | Option sizes for advisor grants |
| S20 | Family evidence | `…_1770141224265557526` (PERSON_2260 sends Patrick Lewis, [PERSON_NAME_52949] (= PERSON_2260_EMAIL), [PERSON_NAME_27652] (PERSON_2275_EMAIL), 25k each) | base | Leonard mailbox | Family rule handler |
| S21 | TOR side letter | GDoc "Harmony Games Side Letter TLAS draft 28 August" (`gdocs /docs_documents/238`, owner Leonard) Notices clause: TOR address, Attn [EMAIL_15398], copy to Thompson Legal Advisory Services [EMAIL_145502] | base | owner | "unless a document says otherwise" |
| S22 | Termination letters (5, Feb 11) | `…_1856861229984402233` Martin eff. 2026-01-31; `…_1856861323365646598` Marcus eff. 2026-01-31; plus [PERSON_NAME_0067]→PERSON_3140 (eff. "January 31, 2025", NB-22), [PERSON_NAME_0040]→PERSON_2361 (= [PERSON_NAME_0043]), brian | base | Leonard SENT | Told status for option holders |
| S23 | Contacts | `contacts.json` (SQL adds PERSON_0693 and PERSON_2275 "Investor") | base + SQL | unscoped | "the email we have" |
| S24 | Advisor Agreement for [PERSON_NAME_11362] | `gdocs /docs_documents/490` "Harmony Games Advisor Agreement - [PERSON_NAME_61018]" (drive f_c2c881ccc407fbdaeaa362): "…and [PERSON_NAME_11362] (the "Advisor")… Name: Husnu Matthew Collins" | base | **NOT visible**: owner "Resource: 7240535625619857401", shared_with [] , visibility private | The only record that maps the ENG-2447 token to a person (see F-1) |

---

### Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Role plausibility: Leonard acts as CEO throughout the wind-down (he signs "Leonard Hayes, CEO" in S8 msg [21]/[42], runs Carta terminations, accepted the Griffin director's resignation, S10). A founder closing out his stockholders, answering the fund's auditor and writing the investor letter is squarely his work. The roster role says "Co-founder & Creative Director"; the data shows him as the executive owner of investor and board relations, so the request fits.
- Voice: first person, casual ("I'm behind on it", "no need to check with me"), matches an exec delegating.
- Access: every source the prompt names is his (owner/member/mailbox) except the issue in F-1.

**Assigned Competency:** PASS (5). Finance: cap-table reconciliation (holdings per class, option lines, vested amounts, outstanding totals as of 2025-12-31 for the auditor), lapsed vs live option lines, and an audit confirmation are finance work.

**Assigned Task Skill:** PASS (5). Authoring is central: a holder sheet, an investor letter (doc) reworked from a draft against an outline, per-holder note drafts with holding-specific content, a KPMG confirmation reply and a board heads-up. These are authored artifacts, not just chat posts.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS
- Ambiguity: per-holder treatment is planted in S3 + S8 thread replies (told test, family rule, Covered label, notice route); the prompt states none of it.
- Dynamic change: S3 supersedes S4 ("These replace my earlier outreach notes"); the Slack replies (02-13 02:21Z) amend the notes; KPMG's clarification (17:37Z) amends item 2; the Nov 2024 list and the SQL "Holder list (draft)" are stale vs Carta (S15) and the Feb messages (S11, S14).
- Multi-source: Linear + Drive/Docs/Sheets/Slides + Slack + Gmail + Contacts (+ Trello context).
- Data seeding: PASS. The 134-word prompt is a trigger; every rule lives in S1, S3, S8, S12, S13.

**Naturalness:** PASS. No headings/bullets/bold, no polished connectives, no staged typos. One soft flag: the third sentence enumerates seven deliverables ("That's the holder sheet and the investor letter…, the messages to holders…, the Linear issues, the heads-up to Griffin, the reply in #winddown and an answer to KPMG's audit request…"). It lists deliverables in plain language, not their contents, so it does not trip the spec-sheet escalation (0 of 4 register triggers).

**Anti-Patterns:**
| Pattern | Status |
|---|---|
| Command List | PASS (no first/then/finally; no ordered steps) |
| Bolt-On | PASS (each deliverable is fed by the same holder sheet; KPMG and Griffin items are tied to it by S1 "once the sheet is done" and S3 "That one can go out once the sheet is done") |
| Pre-Solving | PASS (no holder, label, total, recipient or cause is stated) |
| Tool Mention | PASS ("in Linear", "in my Gmail", "#winddown" are product references; no tool/parameter/MCP/"tool" wording) |

**Diversity:** not a "post one Slack message" task. Writes span Sheets/Drive (create, move, share), Docs (create), Gmail (drafts, reply, reply-all), Linear (state updates + comments), Slack (thread reply).

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

Hand-built in the `render-ugt` shape (helper not run; see Scope).

Main comparison (fork U1, the deciding one):

| Candidate interpretation | Prompt/source authority | Material actions and outputs | Resolved or genuinely ambiguous? |
|---|---|---|---|
| Reading A (author's apparent intent) | S2 ENG-2447 title "[PERSON_NAME_11362]" + comment "Nov 2024 owner list: 86,470"; S17 "[PERSON_NAME_11362] – 86,470 shares"; S16 "Husnu Matthew Collins accepted certificate SSP-10" and "option grant ES-9 for Husnu Matthew Collins"; S19 "Matthew Collins … 61,038 shares"; inference 25,432 + 61,038 = 86,470 | ENG-2447 row = Matthew Collins holding SSP-10 stock plus ES-9 options; not told → "Closing" → Gmail draft to the email we have for Matthew Collins (Contacts `/contacts/159` matthew.collins@harmonygames.co); ENG-2447 → Todo; KPMG option line ES-9 61,038 under this holder | Not resolved by any record Leonard can open |
| Reading B (strongest plausible alternative) | Platform token rule (deep_recheck.md: "the real name is correct only when a persona-visible record maps the token to it"); S3 "Carta is the record"; S1 "one issue per holder on Carta"; the only mapping record S24 is invisible to Leonard; complete scans find "[PERSON_NAME_11362]" only in S17, doc 167 and hidden S24 | "[PERSON_NAME_11362]" stays an unmapped holder: no "email we have", so its note cannot be addressed (or is drafted without a recipient or flagged); "Husnu Matthew Collins" is a Carta holder (SSP-10, ES-9) with no Linear issue, so an agent either adds an issue/row and a note for him or leaves a Carta holder off the sheet; sheet totals and the KPMG option-line attribution move accordingly | Genuinely ambiguous |

Five checks on U1: newer source: none relevant. Authority: S1/S3 make Carta the record and Linear the cohort but never map the token. Source identity: the token and the name come from different records with no shared identifier visible to the persona. Scope: n/a. Same material result: no; recipients, rows and possibly issue creation differ. The quote that would kill Reading B is in S24, which only the Resource account can open. A sum that happens to match is an inference, which deep_recheck.md says cannot reject a UGT finding. UGT therefore fails on U1 (root cause and fix in F-1).

Other forks tested (each stays a rubric-acceptance note; none fails UGT by itself):

| Fork | Reading A | Reading B | Resolution |
|---|---|---|---|
| U2 Holder sheet: new vs existing | Create a new sheet in S5 | Rework S6 "Holder list (draft)", already in S5 | Same destination folder, contents, sharing and downstream use, so same material result. The rubric must accept either file (and must not require deleting S6). |
| U3 TOR Capital note destination | Side-letter route (S21: TOR notice email [EMAIL_15398] with copy to Thompson Legal [EMAIL_145502]) per S3 "Notice route: the email we have, unless a document says otherwise" | TOR contact on file (e.g. PERSON_5275_EMAIL), since Sunset says "your own notes to holders don't need to double as notices" (S13) | Resolved by scope: S1 incorporates Sunset's email only as the sheet spec ("the sheet is what Sunset asked for"), so its remark about notes does not override S3's per-holder rule. Moderate confidence; P1 should test it. The rubric should accept To = TOR notice address with or without the Thompson copy. |
| U4 "the three of us" | Leonard, Robert, Arthur (CS-01/02/03 in S16; #winddown has exactly these three; "we'll keep maybe the three of us", S8 msg 4db5a7ad) | Includes Frederick Stone (roster co-founder) | Resolved: Frederick holds nothing on Carta or the Nov 2024 list. |
| U5 KPMG clarification | "a termination effective on the as-of date itself counts as of that date" → Dec 31 terminations (Claire Morgan, [PERSON_NAME_0043], [PERSON_NAME_2769] [PERSON_NAME_0093]) count as terminated at 2025-12-31 (vested only) | Lines still count whole at 12-31 | Resolved: the grammatical subject is "a termination"; KPMG item 2 also says "using each effective date as Carta shows it, regardless of when recorded". |
| U6 Family lines | Note to the handler (PERSON_2260 / [PERSON_NAME_52949], who sent the family's details in S20) covers Patrick Lewis and [PERSON_NAME_27652]; their lines "Covered"; their issues Done with a why-comment | Separate notes to Patrick and [PERSON_NAME_27652] (SQL contact PERSON_2275 is a decoy) | Resolved by the SQL thread reply 4f54dff9 ("one note to whoever has always handled it for a family covers the rest of the family's lines…") plus S20. |
| U7 Griffin told? | Already told (S11: Feb 9 mail to the partner; "for a fund, its partner"), so no holder note; heads-up only | Linear "Last written contact before Feb: Jan 24, 2026" suggests not told, so a holder note too | Resolved: S11 is a written closing message to the partner in February; the Linear comment is explicitly "before Feb". |
| U8 Who goes first | Earliest live last day: [PERSON_NAME_0051] (2026-02-21, S15) | – | Resolved (S3 "Whoever's last day comes first goes first"). |
| U9 Heads-up content "what we still need from Griffin" | Griffin's stockholder (preferred) consent for the dissolution, after its director resigned (the Feb 11 notes doc 26 says Sunset will circulate "board and stockholder consents"; S13 asks "who holds the preferred vote") | Other asks (e.g. a board seat, the KPMG thread) | Soft acceptance boundary. No single record states the ask in one place; P1 should test it. Evidence limit, not scored. |

**Feasibility:** FAIL (2)

A. Tool feasibility: all SUPPORTED by the catalog. Sheet: `gsheets_create_spreadsheet` + `gsheets_values_update/batch_update` + `gdrive_move_file` (or rework S6 in place). Letter: `gdocs_create_document` + `gdrive_move_file`. Sharing: `gdrive_share_file`. Drafts: `gmail_create_draft` (to/cc/bcc/thread_id). Griffin and KPMG replies: `gmail_reply_to_message` (reply_all). #winddown: `slack_send_message` (thread_ts). Linear: `linear_update_issue` (state) + `linear_create_comment`.

B. Data feasibility (key facts):

| Information needed | Where | Found? | Evidence |
|---|---|---|---|
| Holder cohort | S2 (26 issues) reconciles with S17: 27 owners − 3 founders + Griffin split into 2 + lapsed [PERSON_NAME_0100] = 26 | Yes | S17, S15 `…_1808666480668498098` |
| Option lines, vested, last day | S15 (14 Carta termination mails); active advisor grants ES-9/ES-11 via S16 + S19 | Yes | quoted above |
| Stock per class / per fund | S16 certificates, S17, S18 (Griffin II 2,662,255; Side Fund 84,438), founders CS-01..03 2,000,000 each | Yes (angels by arithmetic from S17/S19/S20) | |
| Told status | S11 (Griffin), S14 (PERSON_3941), S22 (5 contractor letters), S10 | Yes | |
| Family handler | S20 + SQL thread reply | Yes | |
| Special notice terms | S21 (TOR) | Yes | |
| Emails ("the email we have") | Contacts, S20, S22 recipients, Calendly/DocuSign mails (e.g. [PERSON_NAME_0051] = PERSON_2684_EMAIL in `…_1789011705438137160`; [PERSON_NAME_0068] = PERSON_3140_EMAIL; [PERSON_NAME_0043] = PERSON_2361_EMAIL in `…_1771428305047591949`; [PERSON_NAME_4468] = PERSON_0693_EMAIL in `…_1773213846196143460`) | Yes for every holder needing a note **except ENG-2447 [PERSON_NAME_11362]** | **F-1** |
| Investor draft, outline, list to reply under, Board position thread, KPMG thread | S8, S7, S8, S10, S12 | Yes | |

C. Dimensional feasibility: the "per holder" and "by class" breakdowns are supported (holder = Linear issue / Carta stakeholder; class = Common CS / Series Seed Preferred SSP). The "count of holders by what each still needs to hear" uses the S3 labels. Feasible.

D. Numeric observability: KPMG items 1–3 and the sheet totals are derivable from integer values in visible mail bodies (S15–S19); no precision loss. One caveat ties to F-1: the ES-9 61,038 line is attributable to the ENG-2447 holder only through the unmapped identity.

E. Persona ACL: see the next dimension. Verdict: **FAIL** on F-1. A required write (the ENG-2447 holder's note draft) needs a recipient that no persona-visible record supplies.

**Persona ACL Reachability:** FAIL (2). Same root cause as F-1, recorded under its own gate (one defect, one fix).

| Required scoped-service fact | Record | Scoped? | Leonard visibility basis | Authorized alternate | Verdict |
|---|---|---|---|---|---|
| Notes doc, folder, decoys, outline | S3–S7 | Drive family | owner | – | Feasible |
| #winddown draft, list, SQL replies | S8 | Slack | member (`channels.json /154`) | – | Feasible (Leonard is not one of the NB-1 leavers) |
| Task List | S9 | Drive | shared_with includes Leonard | – | Feasible |
| Griffin, KPMG, Sunset, Robert→PERSON_3941, Carta, owner list, allocations, family, letters | S10–S20, S22 | Gmail | Leonard mailbox (to/cc/SENT) | – | Feasible |
| TOR side letter | S21 | Drive/Docs | owner | – | Feasible |
| ENG-2447 holder identity and email ([PERSON_NAME_11362] = Husnu Matthew Collins) | S24 `gdocs /docs_documents/490`, drive f_c2c881ccc407fbdaeaa362 | Drive/Docs | **owner "Resource: 7240535625619857401", shared_with [], private: not visible** | None that states the mapping (only an arithmetic coincidence across S16/S17/S19) | **FAIL** |

Lens 2 (ask-level ACL): no prompt sentence directs a read outside Leonard's view. PASS.

**Explicit Tool Mention:** PASS (5). No hits for `gmail_`, `linear_`, `slack_`, MCP, "tool".

**Clarity & Specificity:** PASS (5)
- Write actions are enumerated and the act/defer split is explicit: "Send the replies yourself, no need to check with me; only the holder messages wait for me". The three replies (Griffin heads-up, #winddown reply, KPMG answer) are sent; holder notes are drafts; the letter is a doc "I can send" (S3).
- Delegation scan: no "I'll [verb]" in the prompt. The incorporated "I'll pass it to Sunset myself" (S1) and "I read and send each note myself" (S3) clearly reserve those actions for Leonard.
- The U1 divergence comes from the data (an identity mapping), not the prompt's wording, so it is scored under UGT/Feasibility, not here.

**Contrived / Unnatural:** PASS (5)
- No exact timestamps, opaque IDs or generated filenames; "from yesterday" is natural.
- No trap hint or riddle; "I'm behind on it" names the situation, not the trap.
- Hidden-destination check: "the heads-up to Griffin" does not name the thread. The incorporated S3 names it ("as a reply on the Feb 12 Board position thread"), and the prompt hands over "the way those lay it out". That is incorporation, not evasive "wherever it was asked" wording. Risk noted for P4.
- No audit-form wording or if-chain. The per-case rules live in S3/S8.
- Long-horizon anti-inflation: record-level work (26 issues × told / holding / last-day / email / question checks + notes + states + comments) answers distinct questions; no bulk view contains the per-holder answers.

**Alignment with Today's Date:** PASS (5). "yesterday" = Feb 13 and the KPMG request is dated 2026-02-13 16:48Z (08:48 PT). S3's "by Tuesday" = Feb 17 (future; SQL GCal "Holder notes due" 2026-02-17T17:00Z). S3's "archive google after the 15th… that waits" matches #winddown fdd87e27 ("archieve account on google after Feb 15"). The KPMG deadline 2/27/2026 is future. Live last days (2026-02-21 … 04-30) are future and lapsed ones are past, consistent with "If a line's last day has passed, it holds nothing".

**Originality / Sample Similarity:** N/A (no samples supplied).

**Truthfulness:** PASS (5)

| Claim | Check | Result |
|---|---|---|
| "everyone who holds our stock or options" | S16/S17/S15 | True (stock and option holders exist) |
| "as we wind down" | S8 shutdown messages; S11 | True (Feb 14 universe) |
| "I set it up in the holder project in Linear" | S1 lead and creator usr_63fffeb4fab5233e = Leonard (`linear /users/13`); the only project matching "holder" (base search: 0) | True |
| "my close-out notes doc has how each holder gets handled and what still needs doing" | S3 headings "What needs doing" / "How each holder gets handled"; owner Leonard | True |
| "the holder sheet and the investor letter in my close-out folder" | S5 owned by Leonard; S3 "everything goes in the close-out folder" | True (deliverables) |
| "my investor email draft in #winddown" | S8 msg 22f31c82 by Leonard | True |
| "the messages to holders as drafts in my Gmail" | S3 "notes ready for me by Tuesday, as Gmail drafts" | True |
| "the heads-up to Griffin", "the reply in #winddown" | S3 bullets | True |
| "KPMG's audit request for Griffin from yesterday" | S12 dated 2026-02-13; subject "GRIFFIN GAMING PARTNERS 2025 Audit Request…" | True |
| "only the holder messages wait for me" | S3 "I read and send each note myself" | True |
| Tight identifiers: "#winddown" (channel exists, exact name), "Griffin", "KPMG", "Linear", "Gmail" | | All verified; no phantom |
| State premises: shutdown applies; no departed person acts | | Clean |

**Tool Use & Cross-service:** PASS (5). Linear changes graded facts (issue states, why-comments); Gmail changes graded facts (told status, holdings, last days, recipients, KPMG figures, drafts, replies); Drive/Sheets/Docs carry the sheet and letter; Slack carries the draft letter source and the reply. Dropping Gmail or Linear changes the answer.

**Investigation + Action:** PASS (5). Every write depends on per-holder findings.

**Coherence (Bolt-on):** PASS (5).

**Business Function:** PASS (5). Founder-led investor and board close-out during the wind-down is executive coordination ("Founders / Exec / Strategy"). Risk note: the audit confirmation and cap-table work also read as Finance/Legal/Ops, but that is the assigned competency, and the investor letter and board heads-up keep it executive.

**Complexity Dimensions & Data Seeding:** PASS (5).

---

### Phase 3: Universe Feasibility

**Data Existence:** FAIL (2)
- Entities verified: all prompt entities and 25 of 26 holders' identities and emails reachable. ENG-2447 [PERSON_NAME_11362] has no persona-visible identity or email (F-1).
- All other facts are retrievable via cataloged reads (Gmail get/search, Linear, Drive/Docs/Sheets/Slides, Slack history/thread, Contacts).

**Cross-Service Coherence:** PASS (5) provisional, pending Eval 0
- Injected records checked for task coherence:
  - SQL chronology is consistent: Slack "Putting the holders in linear" 23:15Z, then issues 23:25–23:32Z, comments, notes doc 01:05Z, thread replies 02:21Z, KPMG 16:48–17:37Z, Sunset 18:06/18:19Z, Trello comment 18:14Z, project updated 18:21Z.
  - The project description cites Sunset's ask and was last updated after it.
  - S3's "where I left things today… the angels are what's open from my list, besides the Sunset onboarding" matches #winddown (Carta terminations done 22:33Z).
  - The slide's "27 holders on the Nov 2024 owner list" matches S17 (27 rows).
  - Every SQL "Nov 2024 owner list: N" comment matches S17.
  - Holder list (draft) rows match S17.
- Base inconsistencies in task-touched data (tagged, not scored):
  - PLATFORM (anonymized tokens): the same holders appear under different tokens across records. Examples: ES-3 "[PERSON_NAME_0029] [PERSON_NAME_0047]" (Nov 2023 digest) vs "Calvin Price" (S15); ES-12 "[PERSON_NAME_0067] [PERSON_NAME_0105]" vs "[PERSON_NAME_0068]" vs "Owen Baker" (`gdocs /docs_documents/167`); ES-16 subject "[PERSON_NAME_2768] [PERSON_NAME_0011]" vs body "EMPLOYEE_0032 [PERSON_NAME_0011]"; S17 "[PERSON_NAME_0022] [PERSON_NAME_32704]" vs Carta "[PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763]". Scored only where it removes a recipient (F-1).
  - Designed, resolvable date difference: Carta "terminated … as of Jan. 30, 2026" (Marcus, Martin) vs letters "effective January 31, 2026" (S22). The incorporated rule resolves it ("Carta is the record"; KPMG "each effective date as Carta shows it"), and no graded value changes (both dates are after 2025-12-31; last days are unaffected). Not scored.
  - NB-22 (known issue): the [PERSON_NAME_0067]/[PERSON_NAME_0068] letter says "effective January 31, 2025". Told status does not depend on the date. Not scored; rubric must not grade it.
- Advisory: the SQL ENG-2447 comment "Last written contact I have before Feb: Jan 5, 2026" has no matching Jan 4–6 2026 message in Leonard's mailbox (non-automated senders listed; none is this holder). It is a decoy "before Feb" note and nothing graded rests on it, but P2 should confirm the other "last written contact" dates.
- Static integrity evidence: direct task-relevant checks (above); Eval 0 for sha 6f3b1899 pending.
- Prompt-specific sources, access and configuration: supported except F-1.

---

### Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 2 | Fork U1: no persona-visible record maps ENG-2447 "[PERSON_NAME_11362]" to Carta's "Husnu Matthew Collins" (SSP-10, ES-9). Readings differ in the note recipient, sheet rows and possibly issue creation (F-1). U2–U9 resolved or acceptance notes. |
| Prompt | Feasibility | 2 | The required note for the ENG-2447 holder has no reachable "email we have" (F-1). Every other ask is supported by tools and data. |
| Prompt | Persona ACL Reachability | 2 | The only mapping record (`docs_documents/490`, drive f_c2c881ccc407fbdaeaa362) is Resource-owned and shared with no one (F-1, same root cause) |
| Prompt | Explicit Tool Mention | 5 | No tool/parameter/MCP wording |
| Prompt | Clarity & Specificity | 5 | Writes and act-vs-defer are explicit ("Send the replies yourself… only the holder messages wait for me") |
| Prompt | Contrived / Unnatural | 5 | Natural delegation; no riddle, ID, timestamp, form or if-chain. Soft flag on the 7-item deliverable sentence. |
| Prompt | Alignment with Today's Date | 5 | "yesterday" = 2026-02-13 KPMG mail; all deadlines future |
| Prompt | Originality / Sample Similarity | N/A | No samples |
| Prompt | Truthfulness | 5 | Every claim and identifier verified (table above) |
| Prompt | Tool Use & Cross-service | 5 | Gmail and Linear each change graded facts; Drive/Slack also written |
| Prompt | Investigation + Action | 5 | Writes depend on per-holder findings |
| Prompt | Coherence (Bolt-on) | 5 | One workflow keyed to the holder sheet |
| Prompt | Persona | 5 | Executive co-founder acting as CEO; the role fits |
| Prompt | Business Function | 5 | Founders / Exec |
| Prompt | Assigned Competency | 5 | Finance (cap table, audit confirmation) |
| Prompt | Assigned Task Skill | 5 | Authoring (sheet, letter, drafts, replies) |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 2 | F-1 (one holder's identity/email absent from the persona's view) |
| Universe | Cross-Service Coherence | 5 (provisional) | Injected data coherent; base token drift tagged PLATFORM; designed Carta/letter date difference resolved by incorporated rule; Eval 0 pending |

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|---|---|---|
| F-1 | **ENG-2447 holder has no persona-visible identity or email.** SQL titles the issue and the sheet row "[PERSON_NAME_11362]" (S2, S6) after the Nov 2024 list (S17 "[PERSON_NAME_11362] – 86,470 shares"). Carta records this holder only as "Husnu Matthew Collins" (S16: SSP-10 accepted 2023-09-15; ES-9 signed 2023-11-17), and the only document joining the two is the Advisor Agreement (`gdocs /docs_documents/490`: "…and [PERSON_NAME_11362] (the "Advisor")… Name: Husnu Matthew Collins"). Its Drive file f_c2c881ccc407fbdaeaa362 is owned by "Resource: 7240535625619857401" with `shared_with_emails: []`, so Leonard cannot open it. Complete scans of Gmail (all mailboxes), GDocs, Drive names, Slack, Sheets, Linear, Trello and Contacts find "[PERSON_NAME_11362]" only in S17, Leonard's doc 167 (list only) and the hidden doc 490. No email is attached to the token anywhere. The holder still holds stock, has no February closing message, and so needs a "Closing" note "to the email we have". Under the platform token rule the agent may not equate the token with Matthew Collins without a mapping record. The only bridge is the coincidence 25,432 + 61,038 (S19) = 86,470. Effect: two defensible end-states for one holder (note to matthew.collins@harmonygames.co vs an unaddressable note), and a Carta holder ("Husnu Matthew Collins") with no Linear issue that a careful agent may add as an extra row or issue. | Major (fail-level) | UGT 2; Feasibility 2; Persona ACL 2; Data Exists 2 (one root cause, one fix) |
| A-1 | U3 TOR note destination (side-letter route vs contact on file) is resolved by scope reasoning only; the rubric should accept the side-letter address with or without the Thompson copy. | Advisory | UGT (acceptance) |
| A-2 | U2: a new sheet and a reworked "Holder list (draft)" are both valid; the rubric must accept either. | Advisory | UGT (acceptance) |
| A-3 | U9: "with what we still need from Griffin" has no single-record statement of the ask; the expected content (Griffin's stockholder/preferred consent to the dissolution) is inferred from doc 26 + S13. | Advisory (evidence limit) | UGT (acceptance boundary) |
| A-4 | Same-class token drift between Carta digests and the Linear cohort for other SSP holders: "[PERSON_NAME_0113]" (SSP-09), "Eren Dişli"/"[PERSON_NAME_10246]" (SSP-07), "[PERSON_NAME_0090]" (SSP-03), "[PERSON_NAME_1909]" (SSP-04). These do not match a Linear title by string; some map via visible records ([PERSON_NAME_1909] = PERSON_3083 via Calendly `…_1760956761062531110`; [PERSON_NAME_0090] via S19 arithmetic), others I did not resolve. Only the email-bearing case is scored (F-1); P1/P2 should check these do not create a "missing holder" reading. | Risk | UGT / Coherence (PLATFORM tokens) |
| A-5 | Rubric must not grade the NB-22 letter date or the Carta Jan 30 vs letter Jan 31 difference. | Advisory | Downstream |

### Recommended Improvements

1. **Fix F-1 in data, not prompt text.** Give Leonard a visible mapping for ENG-2447. Choose one:
   - (a) An SQL UPDATE that shares the Advisor Agreement with Leonard. Set `shared_with_emails_json` to include leonard.hayes@harmonygames.co on both `gdrive.drive_files` id f_c2c881ccc407fbdaeaa362 (`/drive_files/46591`, parent d_f1af2f5be6c26464c262ff) and the matching `gdocs.docs_documents` row (document_id f_c2c881ccc407fbdaeaa362, "Harmony Games Advisor Agreement - [PERSON_NAME_61018]"). Docs inherit Drive ACL, so both must change. The sibling export f_6cd517af46ce5b2b203b0c (`/drive_files/36448`) is also hidden; sharing it is optional. This keeps the token puzzle but makes it solvable.
   - (b) Retitle ENG-2447 and the S6 sheet row "Husnu Matthew Collins" and add his email to the issue (e.g. a Leonard comment).
   - (c) Add a Leonard-visible record (e.g. a SQL Contacts row or a Linear comment on ENG-2447) that names both the token and matthew.collins@harmonygames.co.
   After the fix, re-run the visibility check (`records` on `gdrive /drive_files` field id) and confirm the Matthew Collins note is the only reading.
2. While editing, sweep A-4: for each SSP certificate holder in the Carta digests, confirm a Leonard-visible record maps the digest name to a Linear title, or accept that the Linear cohort is authoritative. Optional: a one-line SQL Linear project note "the issues are the full Carta list" would close the "missing holder" reading without touching the prompt.
3. No prompt rewrite is required for the scored dimensions. The prompt text itself scored 5 on every prompt-wording dimension. Keep the bytes unchanged if the fix is data-only, to avoid reopening Naturalness/Clarity.

---

## Deep Recheck

Status: NOT RUN in this draft. Per the orchestrator's instruction, passes P1–P4 run as four separate blind agents, and an Eval 0 report on SQL sha256 6f3b1899… will be supplied. Their findings will be checked against the cited records (CONFIRMED / REJECTED with reason; a UGT finding is rejected only by a quoted persona-visible record) and merged into the scores above before the final report.

Fork list carried into the recheck: U1 (FAIL, F-1), U2, U3, U4, U5, U6, U7, U8, U9 (see UGT section).

Platform defects: PLATFORM:anonymized-tokens (A-4 examples; scored only where a recipient is lost, F-1).

### FINAL VERDICT: FAIL

Score: 2

Execution status: PARTIAL

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort as configured (runtime does not state the effort level)

Next action: Merge the P1–P4 and Eval 0 findings. Then fix F-1 in the SQL (share doc 490 / f_c2c881ccc407fbdaeaa362 with Leonard, or retitle ENG-2447 with a visible email), re-run Eval 0 on the new SQL and re-run /prompt.

Evidence limits: Phase 5 passes and Eval 0 for this SQL pending. `Evals/Docs` PDFs/XLSX and the Example Task were not re-extracted this run. `hg_prompt_checks.py render-ugt` was not run (local rule: no Evals-store writes), so the UGT section is hand-built. Per-holder answer values (labels, vested counts, totals) were checked to source availability, not computed in full (OE/rubric scope). U3/U9 acceptance boundaries need P1 challenge. The Linear "last written contact" dates other than ENG-2447/Griffin were not verified.

**Lowest Dimension:** Unique Ground Truth / Feasibility / Persona ACL / Data Exists, 2. One holder's identity and email (ENG-2447) exist only in a Drive document Leonard cannot open.

**Summary:** The prompt reads as a natural, short executive delegation. Every claim, identifier and date checks out, and the operating rules are richly seeded across Linear, Drive, Slack and Gmail with resolvable supersessions (S3 over S4, the Slack family and Covered replies, the KPMG clarification). It is not ready because of a data defect. One holder in the required cohort ([PERSON_NAME_11362], ENG-2447) can only be matched to its Carta identity and email through a Resource-owned, unshared Advisor Agreement, which leaves that holder's note unaddressable and opens a second reading of the cohort. A data-only fix (share that document with Leonard or retitle the issue with a visible email) should bring every dimension to 5, subject to the pending recheck and Eval 0.
