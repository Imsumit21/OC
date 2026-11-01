## PROMPT EVALUATION REPORT

### Task: Douglas delegates the server side of the Zombie Match 3D beta sign-off: build the register under Arthur's rules, move the tickets that aren't on prod back to Todo, reply to Arthur, and give Leonard comment access
### Assigned Persona: Douglas - Software Engineer (roster `douglas`, douglas@harmonygames.co, Engineering)
### Assigned Business Function: Engineering
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Long Horizon tier, 100–500+ calls; not estimated or scored here)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## 1. Scope and input manifest

| Item | Value |
|---|---|
| Review | Chat/attachment review, portal attempt 6ad90ea979eb9e5d89f8879f, audit mode |
| Actual review date | 2026-10-26 |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` (input revision 5, uploaded as `04_Prompt (2).txt`), 500 bytes, SHA-256 `a0414d89216a9777c4d2eca8b78eea8ab2ee77edc26503d3d24a2daae3ca3e3e` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md`, SHA-256 `31d7b59630ba4641b0df424256fc3928069351b7548c87e14af9bf21a5627d1f` |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 4), 170,744 bytes, SHA-256 `99128292df926a2e3dae5aa7879b452d65cccab0c0eb998c75c17f693acf544c` |
| Task date | `Evals/task_inputs/02_Universe_Date.txt` (Oct 1, 2025 synth-cut) |
| Error/async config, dynamic context, reference files | None supplied; the prompt names no attachment (every reference is to an environment record) |
| Eval version | Eval 1 SHA-256 `a53a4412e828a2d9ee645b7aa2a0423bc630a11d4dcda87e818d7f1576e25e95`; policy `prompt-source-checks-v2`; evidence contract `stage-evidence-v1`; authority contract `prompt-incorporation-v1` |
| Eval release | `task-quality-v1`, Eval release SHA-256 `633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc` |
| Reviewed prompt SHA-256 | `a0414d89216a9777c4d2eca8b78eea8ab2ee77edc26503d3d24a2daae3ca3e3e` |
| Review context SHA-256 | `be55f7c8d6cfa4fce21e07dc91ecdc8331cd84b6959d048b38d476ff1178b478` |
| Prompt record SHA-256 | `7c4e8247ff62dd669a3169210934f4fd8acd7c6b4406fb387b0bdc788f3e5fa9` |
| Scoring source | `Evals/references/rules/scoring.json` SHA-256 `5e0bed7677fc229f1c1ef29fd14898094451fcbdd126a66604e0380f820600c3`; WORKFLOW.md `ee4cd8e1cc291c3b733bfd53907f073f3c8dcbfbbec4723b978a1e4a504fcd5d` |

Input manifest entry (recorded here; `hg_write_output.py` has no `input_manifest` key): `{"prompt": {"review_version": "prompt-source-checks-v2", "evidence_contract": "stage-evidence-v1", "inputs": {"04_Prompt.txt": "a0414d89…3e3e", "00_Task_Assigned_Inputs.md": "31d7b596…627d1f", "01_Universe_Inject.sql": "99128292…544c"}, "universe_manifest_sha256": "da2f4cf0…ac1a", "reused_evidence": [{"report": "Evals/task_inputs/reports/0_injection.md", "checks": ["A", "B", "C"], "dependencies_verified": "SQL hash, Eval 0, schema snapshot, id_contracts, lint helper, synthcut manifest all unchanged"}]}}`

## 2. Input / authority issues

- Intake was complete without a round trip. All five assignment fields are explicit in the saved assignment: persona Douglas (Software Engineer), business function Engineering, competency Engineering Ops, task skill Retrieval, task type long-horizon. Douglas matches the roster entry `douglas` exactly. The SQL was already saved, and the task date was already saved as Oct 1, 2025.
- No error/async configuration or dynamic context was supplied, and none applies.
- Docs: the Prompt Writing guideline and the QC Rating Form V12 prompt rows were read. The Overall Task Flow, Unique Ground Truth, and Common Errors PDFs were extracted with `pdftotext` and read for the sections that apply here (hard rules, skeleton, ambiguity line). Their governing content is also mirrored in Eval 1, `common_errors.md`, and `scoring.json`. The QC spec XLSX was not opened; its V12 deltas are reflected in `scoring.json` and the Eval 1 local overrides.

### Injection Gate

- State: **NEVER_REVIEWED** (from `hg_injection_gate.py`). There is no `input_manifest.json` entry for /injection, because the output writer has no manifest key. A full /injection report does exist for this exact SQL: `Evals/task_inputs/reports/0_injection.md`, review version `injection-static-v2`, reviewed SHA-256 `99128292df926a2e3dae5aa7879b452d65cccab0c0eb998c75c17f693acf544c`, FINAL VERDICT PASS, Execution status COMPLETE.
- Eval 0 was not rerun. Every dependency the report lists in its §9 was rechecked and still matches: SQL hash; Eval 0 `b1ea752a…6a723d3a`; `injection.json` `31dcb2b4…d74c5151`; `id_contracts.json` `fc4711ef…d9ed4682`; lint helper `a8226e2a…8fc5448b`; synthcut manifest `da2f4cf0…a04aac1a`; clock 2025-10-01 07:00 UTC. A rerun would review identical inputs under identical rules. Its static checks A–C (ids, structure, dates and consistency) are reused under `stage-evidence-v1`.
- Reviewed SQL sha256: `99128292df926a2e3dae5aa7879b452d65cccab0c0eb998c75c17f693acf544c`. Eval 0 verdict: PASS.
- Eval 0 findings on records this prompt depends on: none. Its advisories (two snapshot-uncovered columns, `seq` and `sequence`; Confluence tables missing from the schema snapshot) do not change any value, set, order, recipient, or destination the answer is graded on. They stay advisories here.

## 3. Checklist

| Item | Status |
|---|---|
| Intake: prompt + five assignment fields + injection answer | NEW — complete, saved inputs reused |
| STEP 0.5 injection gate | NEW — NEVER_REVIEWED (manifest gap); matching Eval 0 PASS/COMPLETE reused (above) |
| Phase 0.1 Docs, catalog, ACL, roster | NEW — done (Docs as noted in §2) |
| Phase 0.2 universe exploration | NEW — SQL parsed in full (402 rows); base Linear (73 ZOM tickets Done in window), GitHub match3d-backend (base #1–#35), Slack channel/DM membership, Drive names, Trello and Confluence checked |
| Phase 0.3 calibration | NEW — Prompt Writing examples and Eval 1 inline calibration; no supplied samples |
| Phase 1.1–1.5 | NEW — all PASS |
| Phase 2.1 UGT (two-reading table, record bound) | NEW — PASS 5 |
| Phase 2.2–2.8 | NEW — all PASS |
| Phase 2.9 originality | N/A — no comparison samples supplied |
| Phase 3.1–3.2 | NEW — PASS |
| Phase 4 scoring | NEW |
| Phase 5 deep recheck | NEW — see `## Deep Recheck` |

## 4. Requirement ledger

`authority_contract: prompt-incorporation-v1`. Incorporation chain: prompt "the way he laid it out" / "his sign-off rules" → Arthur's DM (Slack `D05QQF7V404`, 2025-09-30 21:12 UTC: "the rules are on the beta card on the roadmap board") → Trello card 80 "Beta sign-off - server side" (rules 1–6) plus Arthur's card comment of 2025-09-30 15:05 ("spreadsheet imports on the backend count as server changes too") → card rule 3 → Douglas's own Google Doc "match3d-backend - prod deploys" (definition of on prod, approval rule, rollback rule, freeze rule tied to "the server freeze on the calendar") → the calendar event "ZM beta - server freeze" (2025-09-26 22:00 UTC, "Pulled in from Monday"). Arthur's email of 2025-09-30 19:42 ("One more for the server sign-off: leave ZOM-547 and ZOM-553 off the register … Rest of the card stands") is also his sign-off rule. Card rule 6 → Confluence "Zombie Match 3D beta - Oct 10" → Drive folder "ZM Beta sign-off" (Arthur's).

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Arthur's request and rules | Slack DM msg `1e5d5d2b…`; Trello card `68dabfe9…` + comment action `68dbf1b7…`; Gmail `<CAuC1dAL…>` | "our DM" → DM → "beta card on the roadmap board" | `slack_*` history reads; `trello_get_cards_in_list` / `trello_get_card` / `trello_get_card_actions`; `gmail` search/read | DM members include `EMPLOYEE_0031_SLACK_ID` (Douglas) (`channels.json` /513); email has an INBOX copy in douglas@ mailbox; Trello unscoped | Rules 1–6 + imports addendum + 547/553 exclusion |
| Define scope (ZOM Done after the cut through Sep 30, server change) | Linear `issues` (73 ZOM Done 2025-08-25T11:52Z–Sep 30); 79 SQL Linear comments; deploy log Sheet `f_78bedc46…` (Prod deploys row 1 "2025-08-25 11:52", Console & imports tab) | Card rule 1 → deploy log → Linear done list → per-ticket comments → match3d-backend PRs | `linear_list_issues`, `linear_list_comments`, `gsheets_values_get`, `github_get_pull_request*` | Linear/GitHub unscoped; Sheet owned by Douglas | 16 in-scope tickets: ZOM-459, ZOM-336, ZOM-392, ZOM-509, ZOM-518, ZOM-510, ZOM-256, ZOM-531, ZOM-537, ZOM-444, ZOM-499, ZOM-487, ZOM-550, ZOM-435, ZOM-503, ZOM-557 (ZOM-547/553 excluded by email; ZOM-461 Done 11:51:48Z is before the cut; parent ZOM-457 has no row and is client-only) |
| Decide on prod per the doc | PR `prod:`/`rollback:` comments and reviews on match3d-backend #37–#54; doc rules; calendar freeze start | Card rule 3 → doc → PR comments/reviews → calendar | `github_get_pull_request_comments`, `github_get_pull_request_reviews`, `gdocs_get_document_text`, `gcal_list_events` | GitHub unscoped; Doc owned by Douglas; calendar copy on douglas@ calendar | On prod Y: ZOM-459 (#38), ZOM-509 (#39), ZOM-510 (v7 import, prod), ZOM-531 (#45), ZOM-537 (#46), ZOM-444 (#47, Arthur approved in freeze), ZOM-499 (#44 re-deployed 09-22), ZOM-487 (#48). N: ZOM-336 (#40 dev only), ZOM-392 (#41 approved after deploy), ZOM-518 (#43 no approval), ZOM-256 (level pack import dev only), ZOM-550 (#50 in freeze, no Arthur Approve), ZOM-435 (#51 dev only), ZOM-503 (#42 Y but #52 in freeze without Arthur), ZOM-557 (#54 rolled back 09-28) |
| Put the register in the beta sign-off folder | Confluence `page_zm_beta_oct10`; Drive folder `d_69fcebc4…` "ZM Beta sign-off" | Card rule 6 → Confluence page → folder (decoy "ZM Beta sign-off - client QA") | `gdrive_create_file` (parentId) or `gsheets_create_spreadsheet` + `gsheets_values_update` + `gdrive_move_file` | Folder shared with douglas@ as writer; writes not ACL-governed | One register (one row per ticket: ticket, server change(s), on prod Y/N) in that folder |
| Reply to Arthur in the DM | Slack DM `D05QQF7V404` | Same DM | `slack_send_message` (channel) | Douglas is a member | How many on prod (8) and which aren't (8 listed) |
| Do what the rules say for tickets not on prod | Card rule 5 | Card | `linear_update_issue` (state), `linear_create_comment` | Linear unscoped | 8 tickets → Todo, each with a comment naming the change still to go out; no new tickets |
| Handle Leonard's request after the register is in the folder | Gmail `<CAreN_3n…>` (Leonard Hayes, INBOX copy in douglas@ mailbox) | "Leonard also emailed me about the go/no-go" → email | `gdrive_share_file` (emailAddress, role) | Mailbox visible | Register shared with leonard.hayes@harmonygames.co with comment access |

Facts versus obligations: the deploy log Prod deploys tab, Douglas's 09-22 DM ("the trophy path double claim fix is out…on prod since the 3rd"), Oliver's 09-27 Slack ("all the server fixes we closed since the cut are on prod now"), Arthur's 09-19 Slack freeze date, and the May 2025 Domino Delights server sign-off page are research context and stale decoys, not instruction sources. Oliver's 09-30 #zombie-match3d request ("can you post it here too") is not incorporated by the prompt. It adds no grading obligation, and posting there is neither required nor forbidden.

## Phase 1: Prompt Structure & Persona

**Persona: PASS (5).** Douglas owns the server side (card 80: "Douglas owns this one"; Confluence: "server side (Douglas)"), owns the prod deploys doc and the deploy log, and is the person Arthur and Leonard wrote to. Role, access, and scope all fit a Software Engineer handing off a release task. Voice is plain first person.

**Assigned Competency: PASS (5).** The work is release ops: PR deploy status, approvals, rollbacks, ticket state, and a sign-off register. That is Engineering Ops.

**Assigned Task Skill: PASS (5).** Retrieval is central. The agent has to pull each ticket's server change from Linear comments, the PR comment and review history, the deploy log, and the calendar freeze, then report what is on prod. Analysis and Actions stack on top.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y — **PASS (5)**
- Ambiguity: the prompt names no tickets, PRs, rules, or folder ID. Each comes from a persona-visible record the prompt points to.
- Dynamic Change: the card comment adds imports after the card. Arthur's email removes ZOM-547/553 after the card. The calendar freeze (updated 09-23, "Pulled in from Monday") supersedes the 09-19 Slack date. #44's rollback and later re-deploy, and #54's deploy and later rollback, are both reached in order.
- Multi-Source: Slack, Trello, Gmail, Confluence, Drive (Doc + Sheet), GCal, GitHub, and Linear. Distractors: the client QA folder and client card, the DD launch page, Oliver's and Douglas's stale Slack claims, the deploy log's quick list (#41/#43 listed as prod), and base open PR #35 "Other players profile".
- Data seeding: PASS. Every operating rule lives in seeded records. The prompt is a 5-sentence trigger.

**Naturalness: PASS.** A short first-person message with no formatting, lists, polished connectives, or staged errors. AI-text red flags: document formatting No; polished connectives No; enumerated specs No; even symmetric sentences No (lengths vary, with natural shortcuts like "no need to wait on me"); staged errors No.

**Anti-Patterns:**

| Pattern | Status |
|---|---|
| Command List | PASS — no first/then/finally; "once the register is in the folder" is a dependency Leonard himself set ("once your server register is in the beta folder") |
| Bolt-On | PASS — Leonard's ask is about the same register for the same go/no-go and depends on it being filed; the Todo sentence acts on the register's result |
| Pre-Solving | PASS — no ticket, PR, count or cause is named |
| Tool Mention | PASS — "DM", "folder", "emailed", "tickets" are natural service references |

Diversity: goes well beyond one Slack post. Writes span Drive/Sheets (file creation + share), Linear (8 state changes + 8 comments) and Slack.

## Phase 2: Depth Assessment

**Unique Ground Truth: PASS (5)**

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every material fork tested (freeze-deploy counting, freeze start date, the ZOM-547/553 exclusion, the Aug 25 cut boundary, register file type) is settled by a persona-visible incorporated record or falls inside the card's objective boundary.

Alternative selection: B is strongest because it rests on a literal sentence in the governing doc ("gets rolled back at go/no-go") implying freeze deploys are live today, and it changes two Todo writes and the count. C, D and E are the other source-backed forks that change the count or writes; F covers file type.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Apply card 80 (plus Arthur's comment adding imports and his email leaving off ZOM-547/553) with "on prod" as the prod deploys doc defines it, using the calendar freeze start. | 16 ZOM tickets with server changes are in scope (ZOM-547/553 left off); 8 on prod (ZOM-459, ZOM-509, ZOM-510, ZOM-531, ZOM-537, ZOM-444, ZOM-499, ZOM-487); 8 not on prod (ZOM-336, ZOM-392, ZOM-518, ZOM-256, ZOM-550, ZOM-435, ZOM-503, ZOM-557) | Create one register file; move 8 Linear tickets to Todo with one comment each; share the register with Leonard as commenter; send one Slack DM reply | ZM Beta sign-off Drive folder; Linear ZOM-336, ZOM-392, ZOM-518, ZOM-256, ZOM-550, ZOM-435, ZOM-503, ZOM-557; leonard.hayes@harmonygames.co; DM D05QQF7V404 | Register rows: ticket, server change(s), on prod Y/N for the 16 tickets; DM: 8 on prod, the 8 not-on-prod tickets; each Todo comment names the change still to go out (\#40, \#41, \#43, level pack import to prod, \#50, \#51, \#52, \#54) | S\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 55-55): "3. On prod means what the match3d-backend prod deploys doc says."; S\_DOC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 17-17): "Freezes: from the server freeze on the calendar until the beta ships, the Approve review has to be Arthur''s." |
| B | Freeze deploys without Arthur's approval (\#50 for ZOM-550, \#52 for ZOM-503) are still physically on prod until the go/no-go rollback, so they count as on prod today. | 16 in scope; 10 on prod (adds ZOM-550, ZOM-503); 6 not on prod | Create one register file; move 6 Linear tickets to Todo with one comment each; share the register with Leonard as commenter; send one Slack DM reply | ZM Beta sign-off Drive folder; Linear ZOM-336, ZOM-392, ZOM-518, ZOM-256, ZOM-435, ZOM-557; leonard.hayes@harmonygames.co; DM D05QQF7V404 | Register marks ZOM-550 and ZOM-503 Y; DM reports 10 on prod and 6 not | S\_DOC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 17-17): "Anything else deployed during the freeze gets rolled back at go/no-go."; S\_PR50 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 543-543): "prod: 2025-09-27 14:30 UTC, zm-api:54" |
| C | Use Arthur's Slack freeze date (Monday Sep 29) instead of the calendar, so \#50 deployed Sep 27 is not a freeze deploy and ZOM-550 is on prod. | 16 in scope; 9 on prod (adds ZOM-550); 7 not on prod | Create one register file; move 7 Linear tickets to Todo with one comment each; share the register with Leonard as commenter; send one Slack DM reply | ZM Beta sign-off Drive folder; Linear ZOM-336, ZOM-392, ZOM-518, ZOM-256, ZOM-435, ZOM-503, ZOM-557; leonard.hayes@harmonygames.co; DM D05QQF7V404 | Register marks ZOM-550 Y; DM reports 9 on prod and 7 not | S\_FREEZE\_SLACK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 38-38): "server freeze for the beta is monday the 29th" |
| D | Card rule 1 alone: ZOM-547 and ZOM-553 have backend PRs (\#49, \#53) and are in scope. | 18 in scope; 10 on prod (adds ZOM-547, ZOM-553); 8 not on prod | Create one register file; move 8 Linear tickets to Todo with one comment each; share the register with Leonard as commenter; send one Slack DM reply | ZM Beta sign-off Drive folder; Linear ZOM-336, ZOM-392, ZOM-518, ZOM-256, ZOM-550, ZOM-435, ZOM-503, ZOM-557; leonard.hayes@harmonygames.co; DM D05QQF7V404 | Register has 18 rows including ZOM-547 and ZOM-553 as Y; DM reports 10 on prod | S\_CARD1 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 55-55): "where the fix needed a server change" |
| E | Read the cut by day: tickets Done on Aug 25 are either all in (adds ZOM-461, \#37) or all out (drops ZOM-459, \#38). | Scope changes at the Aug 25 boundary: 9 on prod with ZOM-461, or 7 on prod without ZOM-459 | Create one register file; move 8 Linear tickets to Todo with one comment each; share the register with Leonard as commenter; send one Slack DM reply | ZM Beta sign-off Drive folder; Linear ZOM-336, ZOM-392, ZOM-518, ZOM-256, ZOM-550, ZOM-435, ZOM-503, ZOM-557; leonard.hayes@harmonygames.co; DM D05QQF7V404 | Register adds a ZOM-461 row or drops the ZOM-459 row; DM count 9 or 7 | S\_CARD1 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 55-55): "moved to Done after the beta prod cut" |
| F | Make the register a Google Doc table instead of a Google Sheet. | 16 ZOM tickets with server changes are in scope (ZOM-547/553 left off); 8 on prod (ZOM-459, ZOM-509, ZOM-510, ZOM-531, ZOM-537, ZOM-444, ZOM-499, ZOM-487); 8 not on prod (ZOM-336, ZOM-392, ZOM-518, ZOM-256, ZOM-550, ZOM-435, ZOM-503, ZOM-557) | Create one register file (a Doc rather than a Sheet); move 8 Linear tickets to Todo with one comment each; share the register with Leonard as commenter; send one Slack DM reply | ZM Beta sign-off Drive folder; Linear ZOM-336, ZOM-392, ZOM-518, ZOM-256, ZOM-550, ZOM-435, ZOM-503, ZOM-557; leonard.hayes@harmonygames.co; DM D05QQF7V404 | Register rows: ticket, server change(s), on prod Y/N for the 16 tickets; DM: 8 on prod, the 8 not-on-prod tickets; each Todo comment names the change still to go out (\#40, \#41, \#43, level pack import to prod, \#50, \#51, \#52, \#54) | S\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 55-55): "6. The register goes in the sign-off folder named on the ZM Beta page in Confluence." |

Explicit option inventory: The prompt lists no alternative options; its single conditional ("If his sign-off rules say...") is an authorization, not a choice between outcomes.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Card rule 3 makes the prod deploys doc the definition of on prod. The doc says a deploy only counts with a prior non-author Approve, and during the freeze that Approve has to be Arthur's. \#50 and \#52 went out in the freeze with no Arthur Approve (Arthur only COMMENTED on \#50), so neither deploy counts. The rollback line says they are being taken off for go/no-go, which fits A.
Resolution evidence: S\_DOC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 17-17): "A prod deploy only counts if the PR already had an Approve review from someone other than its author when it went out."; S\_DOC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 17-17): "the Approve review has to be Arthur''s"; S\_PR50R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 549-549): "'COMMENTED', 'looks fine, ship it after go/no-go'"; S\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 55-55): "3. On prod means what the match3d-backend prod deploys doc says."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | 10 vs 8 on prod |
| writes | DIFFERENT | 6 vs 8 Todo moves |
| destinations | DIFFERENT | ZOM-550/503 not moved under B |
| contents | DIFFERENT | Y/N and DM count differ |

Authority chain: P → S\_DM → S\_CARD → S\_DOC

Resolution relevance challenge: The doc line B relies on sits in the same paragraph as the rule that makes the freeze deploy not count; the counting rule, not physical deployment, defines on prod under card rule 3.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the doc settles the classification.
Challenge evidence: S\_DOC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 17-17): "Freezes: from the server freeze on the calendar until the beta ships, the Approve review has to be Arthur''s. Anything else deployed during the freeze gets rolled back at go/no-go."

Compared alternative: C
Resolution: EXCLUDED. The doc ties the freeze to "the server freeze on the calendar". Douglas's calendar event starts 2025-09-26T22:00Z and says it was pulled in from Monday. It was created Sep 22 and updated Sep 23, after Arthur's Sep 19 Slack, so it supersedes the Monday date. \#50 went out Sep 27, inside the freeze.
Resolution evidence: S\_DOC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 17-17): "from the server freeze on the calendar"; S\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 126-126): "'Pulled in from Monday so QA gets the weekend on a frozen prod.', NULL, '2025-09-26T22:00:00Z'"; S\_PR50 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 543-543): "prod: 2025-09-27 14:30 UTC"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | 9 vs 8 on prod |
| writes | DIFFERENT | 7 vs 8 Todo moves |
| destinations | DIFFERENT | ZOM-550 not moved under C |
| contents | DIFFERENT | ZOM-550 Y vs N |

Authority chain: P → S\_DM → S\_CARD → S\_DOC

Resolution relevance challenge: The doc names the calendar as the freeze source, and the calendar itself records the change from Monday.
Delegation challenge: NOT_CLAIMED. Source priority set by the incorporated doc.
Challenge evidence: S\_CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 126-126): "Pulled in from Monday"

Compared alternative: D
Resolution: EXCLUDED. Arthur's later email (Sep 30 19:42) adds a sign-off rule: leave ZOM-547 and ZOM-553 off the register and out of the count. The prompt delegates "his sign-off rules".
Resolution evidence: S\_EMAIL\_A (Evals/task\_inputs/01\_Universe\_Inject.sql lines 70-70): "leave ZOM-547 and ZOM-553 off the register"; S\_EMAIL\_A (Evals/task\_inputs/01\_Universe\_Inject.sql lines 70-70): "They''re not part of the count either way."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | 18 vs 16 rows; 10 vs 8 on prod |
| writes | SAME | Both make the same 8 Todo moves, because \#49 and \#53 are on prod either way |
| destinations | SAME | Same tickets moved |
| contents | DIFFERENT | Register rows and DM count differ |

Authority chain: P → S\_EMAIL\_A

Resolution relevance challenge: The email names exactly these two tickets and this register and count.
Delegation challenge: NOT_CLAIMED. Arthur's own rule, incorporated by the prompt.
Challenge evidence: S\_EMAIL\_A (Evals/task\_inputs/01\_Universe\_Inject.sql lines 70-70): "leave ZOM-547 and ZOM-553 off the register"

Compared alternative: E
Resolution: EXCLUDED. The card pins the cut to the first deploy-log row, which carries a time (2025-08-25 11:52 UTC). ZOM-459 moved to Done at 11:53:11Z (after the cut, in scope). ZOM-461 moved at 11:51:48Z (before the cut, out). A day-level reading ignores the time the card points to.
Resolution evidence: S\_CARD1 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 55-55): "(the first row of Douglas''s deploy log)"; S\_LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): ""2025-08-25 11:52", "beta prod cut"; S\_L459 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3528/completed\_at): "2025-08-25T11:53:11Z"; S\_L461 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3530/completed\_at): "2025-08-25T11:51:48Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Count 9 or 7 vs 8 |
| writes | SAME | Same Todo moves; ZOM-461 and ZOM-459 are on prod via the cut |
| destinations | SAME | Same Todo tickets |
| contents | DIFFERENT | Register rows and DM count differ |

Authority chain: P → S\_DM → S\_CARD1

Resolution relevance challenge: Both completed\_at instants are at least 12 seconds from the cut minute, so the minute-precision cut time settles both.
Delegation challenge: NOT_CLAIMED. Settled by record times.
Challenge evidence: S\_LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): ""2025-08-25 11:52""

Compared alternative: F
Resolution: AUTHORIZED_VARIATION. Only the file type differs. The incorporated rules set the content and location, and both readings meet them.
Resolution evidence: S\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 55-55): "6. The register goes in the sign-off folder named on the ZM Beta page in Confluence."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Identical classification |
| writes | DIFFERENT | Sheet vs Doc file |
| destinations | SAME | Same folder and targets |
| contents | SAME | Same rows and DM |

Authority chain: P → S\_DM → S\_CARD
Authority kind: OBJECTIVE_ACCEPTANCE_BOUNDARY
Acceptance boundary: Card rules 2 and 6 fix the register's content (one row per ticket: ticket, server change(s), on prod Y/N) and location (the sign-off folder), not the file type.
Acceptance for A: A Sheet with one row per ticket in the ZM Beta sign-off folder satisfies rules 2 and 6.
Acceptance for F: A Doc with one table row per ticket in the same folder satisfies rules 2 and 6.

Resolution relevance challenge: The rules name rows and a folder and leave the file type open.
Delegation challenge: EXPLICIT_AUTHORITY. Objective boundary from the incorporated card: content and location, any file type that holds rows.
Challenge evidence: S\_CARD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 55-55): "6. The register goes in the sign-off folder"

Strongest-alternative challenge (B): It uses the governing doc's own wording, changes writes on two tickets and the reported count, and is not a strawman.
Challenge evidence: S\_DOC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 17-17): "Anything else deployed during the freeze gets rolled back at go/no-go."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility: PASS (5).**

| Ask | Required capability | Tool(s) | Status |
|---|---|---|---|
| Read DM, channel | Slack history | `slack_*` reads | SUPPORTED |
| Read card + comment | Trello card/actions | `trello_get_card`, `trello_get_card_actions` | SUPPORTED |
| Read emails | Gmail search/read | `gmail_*` | SUPPORTED |
| Read doc, sheet | Docs/Sheets read | `gdocs_get_document_text`, `gsheets_values_get` | SUPPORTED |
| Read calendar freeze | GCal list/search | `gcal_list_events` | SUPPORTED |
| Read PR comments/reviews | GitHub | `github_get_pull_request_comments`, `github_get_pull_request_reviews` | SUPPORTED |
| Read tickets + comments | Linear | `linear_list_issues`, `linear_list_comments` | SUPPORTED |
| Create register in folder | Drive/Sheets write | `gdrive_create_file` (parentId) or `gsheets_create_spreadsheet` + `gsheets_values_update` + `gdrive_move_file` | SUPPORTED (declared) |
| Move tickets to Todo + comment | Linear write | `linear_update_issue` (state; "Todo" is a ZOM state), `linear_create_comment` | SUPPORTED |
| Share with comment access | Drive share | `gdrive_share_file` (emailAddress, role) | SUPPORTED (declared role parameter; runtime acceptance of the value `commenter` is not shown by the catalog) |
| Reply in DM | Slack send | `slack_send_message` | SUPPORTED |

Data feasibility: every needed fact exists (ledger §4). Dimensional feasibility: no per-X breakdown is requested. Numeric observability: the only figure is the count of 8 on prod, which follows from tool-visible PR comments, reviews, the Sheet, and the calendar. The cut boundary uses Linear `completed_at` to the second (ZOM-459 11:53:11Z, ZOM-461 11:51:48Z) against the deploy-log time "2025-08-25 11:52". The catalog has no return schemas, so whether the Linear tool renders seconds is an evidence limit. Both instants still sit on opposite sides of the cut minute. Persona-scoped reads (Lens 1): the DM (member), both emails (INBOX copies), the calendar (own copy), the Drive folder (writer), the Doc and Sheet (owner), and #zombie-match3d (member) are all reachable. Lens 2: no ask directs Douglas to read anything outside his view.

**Persona ACL Reachability: PASS (5).** No required scoped read is hidden.

**Explicit Tool Mention: PASS (5).**

**Clarity & Specificity: PASS (5).** Write actions converge under every reasonable reading (see UGT). There is no "I'll [verb]" self-action statement. "go ahead and do that too, no need to wait on me" settles act-versus-defer for the Todo moves. "once the register is in the folder" orders the Leonard share.

**Contrived / Unnatural: PASS (5).** No exact timestamps, opaque IDs, format rules, reply format, riddles, hidden destinations (the folder and DM are named; Leonard's ask is in an email the prompt points to), audit-form wording, or if-chains. The single "If his sign-off rules say …, go ahead" is a natural delegation, not a chain. Spec-sheet register triggers: 0 of 4.

**Alignment with Today's Date: PASS (5).** "Thursday's go/no-go" resolves to Thursday, Oct 2, 2025 (Confluence: "Go/no-go on Thursday Oct 2"), which is in the future on the Wed Oct 1 clock. The scope ends "Sep 30". The last task-touched event is 2025-09-30T21:12:44Z, before the clock.

**Originality / Sample Similarity: N/A** — no comparison samples supplied.

**Truthfulness: PASS (5).**

| Claim | Record | Result |
|---|---|---|
| "Arthur asked me in our DM for the server side of the beta sign-off" | Slack `D05QQF7V404` msg `1e5d5d2b…` (Arthur, 2025-09-30 21:12 UTC): "i need the server side of the beta sign-off from you"; Douglas is a member | Accurate |
| "Thursday's go/no-go" | Confluence `page_zm_beta_oct10`: "Go/no-go on Thursday Oct 2." | Accurate |
| "the way he laid it out" / "his sign-off rules" | DM → card 80 (created by Arthur, member `2162c1ba…`); Arthur's email "Rest of the card stands." | Accurate |
| "the beta sign-off folder" | Drive `d_69fcebc4…` "ZM Beta sign-off" (Arthur's, Douglas writer), named by Confluence as the sign-off folder | Accurate (loose descriptor; the client QA folder is a disambiguated decoy) |
| "Leonard also emailed me about the go/no-go" | Gmail `<CAreN_3n…>` from Leonard Hayes to Douglas, subject "beta go/no-go thursday" | Accurate |
| "the register" | Card rule 6 "The register goes in the sign-off folder…" | Accurate (requested output, named by the rules) |

No tight identifiers (channel names, IDs, amounts, dates) are stated. No departed person is involved (Arthur, Leonard, Oliver and Vincent were all active in Sept 2025).

**Tool Use & Cross-service: PASS (5).** At least two services each change a graded fact. GitHub (PR `prod:`/`rollback:` comments and review timing) decides each ticket's on-prod Y/N and the count of 8. Linear (Done timestamps and comments) decides which 16 tickets are in scope and is the write target. Gmail (Arthur's email) changes the register rows and the count. GCal (freeze start) flips ZOM-550. Drive (deploy log imports) decides ZOM-510 and ZOM-256.

**Investigation + Action: PASS (5).** Investigation across 8 services feeds the register, 16 Linear writes, the share and the DM reply.

**Coherence (Bolt-on): PASS (5).**

**Business Function: PASS (5).** Engineering maps to Engineering & Live-Ops (beta release operations).

## Phase 3: Universe Feasibility

**Data Existence:** Entities verified: 6 of 6 premises plus every ledger source. All retrievable via the cataloged tools: Yes.

**Cross-Service Coherence: NON-FAIL (3)**
- Inconsistencies in task-touched data: one, confirmed in the deep recheck (DR2). The SQL Google Doc "match3d-backend - prod deploys" says "Prod runs from the prod branch: to put a PR on prod you cherry-pick it onto prod", and the SQL deploy-log Prod deploys row 1 reads "beta prod cut: prod branch from main (#37, #38)". The match3d-backend branch export has 37 branches including `main` but no `prod` (only `create-prod-env`, `hotfix-disable-nakama-integration-prod`, `nakama-prod-deployment`), and none of the 18 SQL `github.github_branches` rows adds one. Category: Cross-service Referential Inconsistency (a required reference does not resolve). It is single and low-impact: the same doc says the `prod:` PR comment is what puts a PR on prod, so no Y/N, count or write changes. It is not a lifecycle or sum mismatch, so it is NON-FAIL 3.
- Other checks found nothing: Checked: PR internal chronology and task-definition numbering (zm-api:41→57 rise with time through both rollbacks); deploy log rows vs PR `prod:` comments (all 7 match); Linear comments fall before each ticket's `completed_at`, and the ZOM-535/504 UPDATEs match their comment times; the calendar (created 09-22, updated 09-23) follows the 09-19 Slack it supersedes; folder creation times precede the Confluence page and card that name them; Slack thread fields.
- Noted, not scored: the DM `D05QQF7V404` is `is_im` with 4 members. That is the export-wide convention (548 of 574 base IMs list 3–5 members), not a task-specific contradiction. The parent ZOM-457 comment "nothing needed in match3d-backend" sits beside children ZOM-459/ZOM-461 that had backend PRs. It describes the parent's own client fix, and card rule 1 gives parents no row, so it changes no graded fact (see Deep Recheck for the pass review).
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED. `0_injection.md` checks A–C (PASS, COMPLETE) on the identical SQL hash and rules.
- Prompt-specific sources, access and configuration: supported. No error/async configuration.

## Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 5 | Two-reading table above: strongest alternative B (freeze deploys count as live) and C/D/E excluded by quoted persona-visible records; F (file type) inside card rules 2 and 6 |
| Prompt | Feasibility | 5 | Every read and write has a cataloged path; all data exists; no breakdown; count derivable |
| Prompt | Persona ACL Reachability | 5 | DM member, INBOX copies, own calendar copy, folder writer, Doc/Sheet owner |
| Prompt | Explicit Tool Mention | 5 | No tool, parameter, MCP or "tool" wording |
| Prompt | Clarity & Specificity | 5 | Writes converge; act-vs-defer settled by "go ahead … no need to wait on me" |
| Prompt | Contrived / Unnatural | 5 | Short natural delegation; deferral to named records (Prompt Writing "check #channel and follow what's there"); P4 findings rejected (Deep Recheck) |
| Prompt | Alignment with Today's Date | 5 | Thursday = Oct 2 (future); window ends Sep 30 |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | 6 premises verified; no tight identifiers stated |
| Prompt | Tool Use & Cross-service | 5 | GitHub decides Y/N; Linear decides scope and takes writes; Gmail, GCal and Drive each change the answer |
| Prompt | Investigation + Action | 5 | Investigation feeds register, 16 Linear writes, share, DM |
| Prompt | Coherence (Bolt-on) | 5 | All asks concern the same register and go/no-go |
| Prompt | Persona | 5 | Douglas owns the server sign-off and the deploy doc/log |
| Prompt | Business Function | 5 | Engineering & Live-Ops beta release work |
| Prompt | Assigned Competency | 5 | Engineering Ops (deploys, PR approvals, ticket state) |
| Prompt | Assigned Task Skill | 5 | Retrieval is central across 8 services |
| Prompt | Complexity Dimensions & Data Seeding | 5 | Ambiguity, Dynamic Change and Multi-Source all load-bearing; rules seeded |
| Universe | Data Exists | 5 | All facts exist and are retrievable |
| Universe | Cross-Service Coherence | 3 | One minor Cross-service Referential Inconsistency (Deep Recheck DR2): the prod deploys doc and deploy log refer to a match3d-backend `prod` branch that does not exist in the branch export or SQL; no graded fact changes |

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | The prod deploys doc (`f_470ae81236d5bd39045dc1`: "Prod runs from the prod branch … cherry-pick it onto prod") and the deploy log (`f_78bedc46245090a160d2dd` Prod deploys row 1: "beta prod cut: prod branch from main (#37, #38)") reference a match3d-backend `prod` branch. No such branch is in the base branch export (37 branches, `main` included) or in the 18 SQL branch rows. The PR rollback comments ("pick reverted") lean on the same branch. | Minor (no graded fact changes) | Cross-Service Coherence (NON-FAIL 3) |

### Recommended Improvements

1. Fix issue 1 in the SQL, either way:
   - Add one `github.github_branches` row for repo `harmonygames-Games/match3d-backend` named `prod`, with a `head_sha` that resolves to an existing commit. Check that the id and name are free.
   - Or remove the branch and cherry-pick wording everywhere it appears: the doc's "Prod runs from the prod branch … cherry-pick it onto prod" and "revert the pick on prod", the deploy-log row "prod branch from main", and the two `rollback:` PR comments ("pick reverted" on #44 and #54). Describe the deploy as the task-definition update that `page_cicd_pipeline` ("CI/CD Pipeline & Branching") already documents.
   No ready-to-paste SQL is given because the branch row needs a `head_sha` choice that was not verified here. Rerun /injection after either change, then /prompt.
2. Optional, not scored: a rubric for this task must accept the register as either a Sheet or a Doc (card rules 2 and 6 fix the rows and the folder, not the file type). It must neither require nor penalize a post in #zombie-match3d for Oliver, because the prompt does not incorporate his request.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5) subagents at session effort, each blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 5 sentences, 24 forks | 0 | 0 |
| P2 | 5 sentences | 1 | 1 |
| P3 | 5 sentences | 1 | 0 |
| P4 | 5 sentences | 3 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P4 | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." | Trello card `68dabfe9…` rule 5 | §6.6 / §2.7 | Contrived (if-chain / trap hint) | REJECTED | One conditional authorizing an action, not a long per-case chain (#44) or form wording (#1/#43). It points at no hidden cause; the trap (which tickets are really on prod) is not hinted. It settles act-vs-defer, which Clarity requires. Deferring per-case rules to a seeded record is the recommended pattern (common_errors §6.2 GOOD: "Arthur posted how he wants each kind handled") |
| DR2 | P2 | "Can you take care of it for me, the way he laid it out?" | SQL Doc `f_470ae81236d5bd39045dc1` "Prod runs from the prod branch"; SQL Sheet `f_78bedc46245090a160d2dd` row 1 "prod branch from main (#37, #38)"; base `github/data.json` `/branches` for match3d-backend: 37 names, no `prod`; SQL adds 18 feature branches, no `prod` | §3 | Cross-Service Coherence | CONFIRMED | Opened the branch export: `main` present, `prod` absent; SQL branch names checked. One low-impact referential inconsistency, NON-FAIL 3 |
| DR3 | P4 | "Leonard also emailed me about the go/no-go, so please handle what he asked for once the register is in the folder." | Gmail `<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` "please share it with me directly. Comment access please" | §2.7 | Contrived (hidden destination) | REJECTED | The prompt names the record (Leonard's go/no-go email, the only one, in Douglas's INBOX), and Leonard is the destination. The failing cases #42 ("wherever that's actually been asked for") and #44 ("answer him there too") give no record that leads there. Prompt Writing endorses "check #channel and follow what's there" |
| DR4 | P4 | "Can you take care of it for me, the way he laid it out?" / "Put the register in the beta sign-off folder and reply to Arthur in the DM with what he asked for." | Slack `1e5d5d2bf50901f0d7376627d6f539e8` | §1.2 / §2.7 | Contrived (deferral pattern) | REJECTED | Destinations (folder, DM) are named, and each deferral points to one persona-visible record. Prompt Writing asks for vagueness "exactly where a real person would be vague" and for details seeded rather than typed. No spec register, staged errors or riddle |
| DR5 | P3 | SQL column lists `github.github_reviews (… seq)`, `linear.linear_comments (… sequence)` | `Evals/references/schema/injection.json` lacks `seq`/`sequence` | §6.8 | Injection compatibility | REJECTED | The schema snapshot is unverified, and a missing definition there is advisory (schema README; Eval 0 report advisory). No graded value, set or recipient depends on these columns; kept as an Injection Gate advisory |

Effect on verdict: Cross-Service Coherence 5 → 3; overall PASS 5 → NON-FAIL 3. UGT unchanged at PASS 5.

- F1: P1/F1 cut boundary | A: compare by timestamp, so ZOM-461 (11:51:48Z) is out and ZOM-459 (11:53:11Z) is in | B: compare by calendar day | Settled by: card 80 "(the first row of Douglas''s deploy log)" + Prod deploys row 1 "2025-08-25 11:52"
- F2: window end UTC vs PT | A: through Sep 30 | B: include Oct 1 UTC before 07:00 | Settled by: card "through Sep 30"; no ZOM ticket completed after 2025-09-30T12:43:28Z
- F3: parent ZOM-457 row | A: no row | B: row | Settled by: card "Parent tickets don''t get a row of their own."
- F4: ZOM-547/553 | A: off the register and count | B: in | Settled by: Arthur's email "leave ZOM-547 and ZOM-553 off the register… They''re not part of the count either way."
- F5: imports as server changes (ZOM-510 Y, ZOM-256 N) | A: count | B: PR/console only | Settled by: card comment "spreadsheet imports on the backend count as server changes too"
- F6: console change "plague race bot names" | A: no row | B: row | Settled by: card "One row per ticket"; no in-window ticket references it
- F7: merged = live (2025-05-28 Slack) | A: not on prod | B: on prod | Settled by: card "Merged is not on prod."; doc "Merging doesn''t deploy anything."
- F8: Slack claims / quick list vs PR comments | A: PR `prod:` comment | B: Slack or quick list | Settled by: doc "That comment is what puts the PR on prod, not the merge and not a Slack message."
- F9: ZOM-392 #41 approved after deploy | A: N | B: Y | Settled by: doc "Approving afterwards doesn''t fix it; redeploy."
- F10: ZOM-518 #43 no approval | A: N | B: Y | Settled by: doc "A prod deploy only counts if the PR already had an Approve review from someone other than its author"
- F11: freeze start calendar vs Slack Monday | A: 2025-09-26T22:00Z | B: Sep 29 | Settled by: doc "from the server freeze on the calendar"; calendar "Pulled in from Monday"
- F12: freeze deploys without Arthur's Approve (#50 ZOM-550, #52 ZOM-503) | A: N | B: live until go/no-go rollback | Settled by: doc "the Approve review has to be Arthur''s"; Arthur's #50 review is COMMENTED
- F13: ZOM-444 #47 Arthur approved in freeze | A: Y | B: N | Settled by: same doc sentence
- F14: ZOM-499 #44 rollback then re-deploy 09-22 | A: Y | B: N | Settled by: doc "until a newer \"prod:\" comment"; PR #44 "prod: 2025-09-22 17:30 UTC, zm-api:51"
- F15: ZOM-557 #54 rolled back | A: N | B: Y | Settled by: doc "A rollback takes the PR off prod whenever it happens, freeze or not"
- F16: ZOM-435 #51, ZOM-336 #40 dev only | A: N | B: Y | Settled by: doc "Only the PRs picked onto prod are on prod."
- F17: "merged in match3d" tickets | A: client | B: server | Settled by: card "A server change is a match3d-backend PR"
- F18: non-Done tickets with new comments (ZOM-535, ZOM-504, ZOM-563) | A: out | B: in | Settled by: card "ZOM tickets moved to Done"
- F19: folder (Arthur's vs client QA) | Settled by: Confluence "Sign-off folder: ZM Beta sign-off (Drive, Arthur''s). Client QA keeps its own folder."
- F20: DM reply contents | Settled by: Arthur's DM "with how many tickets are on prod and which ones aren''t"
- F21: action on not-on-prod tickets | Settled by: card rule 5 "goes back to Todo with a comment saying which change still has to go out. Same ticket, no new ones."
- F22: Leonard file vs folder, role | Settled by: Leonard's email "please share it with me directly. Comment access please"
- F23: extra #zombie-match3d post for Oliver | Settled by: not incorporated by the prompt (neither required nor penalized)
- F24: register file type | Settled by: card rules 2 and 6 fix the rows and the folder only (AUTHORIZED_VARIATION F in the UGT table)

Platform defects: none.

### FINAL VERDICT: NON-FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Score: 3

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Eval version: task-quality-v1

Eval release SHA-256: 633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc

Reviewed prompt SHA-256: a0414d89216a9777c4d2eca8b78eea8ab2ee77edc26503d3d24a2daae3ca3e3e

Review context SHA-256: be55f7c8d6cfa4fce21e07dc91ecdc8331cd84b6959d048b38d476ff1178b478

Prompt record SHA-256: 7c4e8247ff62dd669a3169210934f4fd8acd7c6b4406fb387b0bdc788f3e5fa9

Next action: Fix the missing match3d-backend `prod` branch reference (add the branch row, or remove the branch and cherry-pick wording from the doc, the deploy log and the rollback comments). Then rerun /injection and /prompt.

Evidence limits: The catalog has no return schemas, so whether the Linear tool shows `completed_at` to the second, and whether `gdrive_share_file` accepts role `commenter` at runtime, are not shown (both declared and raw-verified). The injection gate read NEVER_REVIEWED only because no manifest entry exists; a matching Eval 0 PASS/COMPLETE on the identical SQL was reused. The QC spec XLSX was not opened.

**Lowest Dimension:** Cross-Service Coherence - 3 - The doc and deploy log reference a match3d-backend `prod` branch that is absent from the GitHub branch export and the SQL.

**Summary:** The prompt is short and natural, and fits Douglas's Engineering Ops / Retrieval assignment. Every fork tested resolves to one end state from records Douglas can open: 16 tickets, 8 on prod, 8 moved to Todo with comments, the register in Arthur's folder shared with Leonard as commenter, and the DM reply. The only defect is one low-impact referential inconsistency in the seeded deploy docs, which holds the prompt at NON-FAIL 3.
