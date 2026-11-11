## PROMPT EVALUATION REPORT

### Task: Julia Lawson builds the ZM3D beta live-ops and push calendar for the four buy weeks starting Mon Oct 6, 2025, under Frederick's brief, then notes held beats, links the sheet on the calendar ticket and sends Frederick a recommendation
### Assigned Persona: Julia Lawson - Product Manager (julia_lawson, julia.lawson@harmonygames.co, Product)
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Planning and decision support
### Assigned Horizon: long-horizon (Long Horizon); Difficulty mode: medium

**Scope.** Chat-style review in folder `review_rev3`, mode AUDIT, review date 2026-11-06, universe Oct 1, 2025 (synth-cut), `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut).

| Input | Path | SHA-256 |
|---|---|---|
| Prompt (exact) | `inputs/04_Prompt.txt` | `2a23afd87c4ca1b4736385b39bdeb2248119a8f4f33dcd8c3ff9acd8156a2beb` |
| Assignment (fenced "Platform assignment" block only) | `inputs/00_Task_Assigned_Inputs.md` | `e8b8269803d55217c20956dcadc93f50480bcc859ed88e5f1bbf153fa04649eb` |
| Injection SQL (static overlay, never executed) | `inputs/01_Universe_Inject.sql` | `837d4f5dedbdedb0febe279f64b5df61f0debdf29e93ef779a4ddd5ff754d76b` |
| Universe date | `inputs/02_Universe_Date.txt` | "Oct 1, 2025 (synth-cut)" |
| Reference files / error-async config / dynamic context | none supplied | Friction: none |

Eval version: task-quality-v1 · Eval release SHA-256: `c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b` (`hg_eval_release.py snapshot prompt`). Reviewed prompt SHA-256: `2a23afd8…2beb`. Review context SHA-256 (hand-bound, method in the record): `5509bb700f3615f2c95d4208b328eeca340446a516ff1feaad3188d911352f9f`. Prompt record: `out/1_prompt_checks.json`, SHA-256 `35892dab98ec6f37d1d69a0c940104a808aa7ad13049593ad69c7c5fcb0c14c2` (filled by hand per the workspace adaptation; hg_prompt_checks.py was not run). authority_contract: prompt-incorporation-v1; evidence_contract: stage-evidence-v1; reused_evidence: [] (all checks NEW).

**Input/authority issues.** None. All five assignment fields are explicit in the platform block. The input store, prompt-check helpers and output writer were deliberately not used. Originality is N/A: no samples and no dataset similarity library are bundled.

---

### Injection Gate
- State: NEVER_REVIEWED → run. Eval 0 (`injection-static-v2`) was run in parallel by a separate, independent reviewer on this exact SQL; report `R/out/0_injection.md` (FINAL VERDICT: PASS, Execution status: COMPLETE, "No demonstrated defects"). I also checked every task-required injected record directly (Phase 3.2 table).
- Reviewed SQL sha256: `837d4f5dedbdedb0febe279f64b5df61f0debdf29e93ef779a4ddd5ff754d76b` (Eval 0 re-hashed the same value). Eval 0 verdict: PASS / COMPLETE.
- Eval 0 advisories on records this answer depends on, and where each is scored:
  - A2/A3 (Brian's Sep 26 correction in its own Gmail thread; snippet ≠ body start): the record carries the graded Oct 31 date, so this is a 3.2 low-impact finding (= P2-DR5).
  - A5 (Halloween retraction threaded under an unrelated parent): the record carries the graded Halloween-off decision, so this is a 3.2 low-impact finding (= P2-DR4).
  - A8 (SC-16 `cmt_zom565_1` "can close" while Todo): 3.2 State/Lifecycle fail (C1).
  - A8 (SC-38 Season Pass spec / `cmt_zom552_1`): advisory. The answer uses neither the ship date nor analytics.
  - A6 ("Product latest dated approval"): Clarity minor (P1-DR9).
  - A4 (mirror subtype), A7 (GCal `transparent`; review timeline `commented`), A1 (schema snapshot), A9–A12a: advisories. The answer never reads those fields, or the item reconciles.

---

### TODO checklist (Eval 1 STEP 0)
| Item | Status |
|---|---|
| Intake (five fields, prompt, SQL) | DONE (NEW) |
| STEP 0.5 injection gate | DONE: NEVER_REVIEWED → Eval 0 run in parallel by a separate reviewer (PASS / COMPLETE); direct task-record checks done |
| 0.1 Docs + catalog | DONE (Prompt Writing PDF, QC Rating Form V12 rows, scoring groups via guide, catalog of 13 services + gateway) |
| 0.2 Deep universe exploration | DONE (Slack, Gmail, GCal, Drive/Docs/Sheets/Slides, Linear, GitHub incl. repo files, Trello, Confluence) |
| 0.3 Example-task calibration | DONE (rules-level; Example Task PDF not re-read, see Evidence limits) |
| 1.1–1.5 | DONE |
| 2.1–2.9 | DONE (2.9 N/A) |
| 3.1–3.2 | DONE |
| 4.1–4.2 | DONE (draft) |
| 5 Deep recheck | DONE: P1–P4 returned; every cited record opened (see `## Deep Recheck`) |

---

### Phase 1: Prompt Structure & Persona

**1.1 Persona: PASS (5)**

| Check | Finding |
|---|---|
| Role plausibility | Yes. Confluence `page_liveops_calendar`: "Daily live-ops pod review. Design, led by Julia Lawson, walks the coming weeks with Frederick Stone: which recurring slots fire and whether a one-off drops on top." Event definitions are owned by "Design (Julia Lawson)" (`page_live_ops_engine`). |
| Voice match | Yes. A short, informal first-person delegation to an assistant, in a PM's vocabulary ("beat", "held", "ticket"). |
| Access plausibility | Yes. Julia is in Frederick's DM D05SD5QLG94, Robert's DM D05GU6L0XFH, #zombie-match3d and #zombie-art (channels.json), and the brief, deck and push sheet are shared with her. |
| Responsibility scope | Yes. She prepares the plan and recommendation; Frederick and the pivot call decide. |
| HARD GATE: Persona ACL identity | PASS. Exact roster entry `julia_lawson` / julia.lawson@harmonygames.co / Product Manager / Product. |

**1.2 Naturalness & AI-text check: PASS**

| Red flag | Found? | Quote |
|---|---|---|
| Document formatting | No | Plain six-sentence message |
| Polished connectives | No | — |
| Enumerated deliverable specs / preservation rules | No | Contents are delegated: "What he wants in it is in his message" |
| Even, symmetric sentences | No | Mixed lengths ("Can you take it on for me?") |
| Staged errors | No | Clean typing (allowed) |

Incorporated sources (prompt-incorporation-v1):

| Source | Incorporating passage | Scope / availability / version |
|---|---|---|
| Frederick's DM 8b090dec (2025-09-30T20:20Z) and his thread reply 097c95c6 (20:24Z), DM D05SD5QLG94 | "What he wants in it is in his message" | Contents, destination ("calendar sheet in your ZM Live Ops folder"), ZOM ticket link, DM reply, push-row scope. Julia is a member. SQL-proposed. |
| Brief "ZM3D beta live-ops calendar - working rules" (f_7c3e91a4…, Frederick, shared with Julia as reader, Sep 24) | "his working rules for building it are in the brief he shared with me" | All rules: span/time base, scope, start, hold, one-offs, still-to-do, push copy, config locks. Delegates to "my UA plan" (deck f_2b9d4e7a…, shared). SQL-proposed. |
| Facts used for research only (not instruction sources) | — | Season Pass spec (lock 24h before season; "Owner: Robert (Product)"), live-ops calendar page, CDK stack crons, GCal release, GitHub/Linear/Trello comments, push sheet |

**1.3 Structural anti-patterns**

| Pattern | Status | Evidence |
|---|---|---|
| Command list | PASS | "Once the sheet's done, link it…" is a natural dependency, not numbered steps |
| Bolt-on | PASS | See table below |
| Pre-solving | PASS | No beat, hold, owner, date or cause is stated |
| Tool mention | PASS | No tool, parameter, MCP server or "X tool" wording |

| Sentence | Removable without effect? | Bolt-on? |
|---|---|---|
| S1 trigger/span | No (defines the job) | No |
| S2 "Can you take it on for me?" | No (delegation) | No |
| S3 message + brief | No (incorporates every rule) | No |
| S4 destination sheet | No | No |
| S5 held-beat ticket note | No (a write that depends on the hold decisions) | No |
| S6 link + recommendation | No (two writes that depend on the sheet) | No |

**1.4 Diversity:** Not "investigate + one Slack post". Writes span Sheets (two tabs), Linear (held-beat comment, link on ZOM-78), Slack (DM reply) and an owner notice (Gmail reply or Slack). Category: Product & Design. Shape: a cohort plan with per-beat holds, still-to-dos and push gating, then a decision recommendation.

**1.5 Assignment & complexity: PASS (5)**

| Field | Recorded value | Source |
|---|---|---|
| Persona | Julia Lawson, Role: Product Manager | Platform block |
| Business function | Product → Product & Design | Platform block |
| Competency | Marketing and GTM | Platform block |
| Task skill | Planning and decision support | Platform block |
| Horizon | long-horizon → Long Horizon (design guidance from `long_horizon.md`; no call count scored here) | Platform block |

- **Competency PASS.** A launch-window calendar for paid UK/US beta buy weeks, with push campaigns gated on English copy and brand/event naming. The deck says "Scaled beta-cohort buy, starting once the stores approve the Sep 30 builds" and "UK and US first, English-only creative". That is GTM work.
- **Task skill PASS.** The work is planning and decision support: deciding per beat whether it starts late, is held or is off, gating each push, moving a config date that misses its lock, and making "your call, not a list of what we have" for the pivot call.

| Dimension | Present? | Evidence |
|---|---|---|
| Ambiguity | Yes (load-bearing) | Every rule, date, owner and destination is seeded (DM, brief, CDK, GCal, mail, PRs, tickets); the prompt names none |
| Dynamic Change | Yes (load-bearing) | Brian Oct 29 → Oct 31 ("drop the Oct 29 one"); Robert Sep 18 approval → Sep 30 pull; Douglas Sep 23 "restart fixes it" → Vincent Sep 30 "still last week one" after restart; Calvin Sep 24 "still needs the frame" → Samuel Sep 30 "went out"; Marcus Sep 26 "every event icon animates" → Sep 30 "C&W icon animation still to do" |
| Multi-Source | Yes | Slack, Gmail, GCal, Drive/Docs/Slides/Sheets, GitHub (PRs + repo CDK file), Linear, Trello, Confluence, with decoys (Domino push sheet, "Win & Collect" name, ENG-2240 "liveops calendar" ticket, base "LiveOps Event Calendar" sheet) |
| Data seeding | PASS | Six-sentence trigger over seeded rules |

Business function: PASS (5), with a watch note. Live-ops and push planning overlaps Engineering & Live-Ops and Growth/UA. Here it is product-team planning that ends in a product decision call: the live-ops pod is led by Design/Product (Julia), and the season pass is "Owner: Robert (Product)".

---

### Phase 2: Depth Assessment

**Requirement ledger** (authority_contract: prompt-incorporation-v1)

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| R1 Calendar tab: every ZM3D beat visible Oct 6 00:00–Nov 2 23:59 UTC, with windows as UTC start–end instants, held/until, push, still-to-do + owner | DM 8b090dec; brief (span, scope, start, hold, one-offs, still-to-do); deck W1–W4; CDK crons; GCal evt_5c1e83a7; #470/#370/#438/#454/#471 comments; Linear comments; Trello 68dac820; Gmail Brian thread; Slack 58d06bd5, fa3eee2c; Confluence SP spec + live-ops calendar | Prompt → DM → brief → linked sources | gsheets_values_update / gsheets_values_append on f_e4a17c90…; reads: slack_read_thread, gdocs_get_document_text, gslides_get_presentation_text, github_get_file_contents, github_get_pull_request_comments, linear_list_comments, gcal_list_events, gmail_get_thread, confluence_get_page, trello_get_card_actions | Sheet owned by Julia; all scoped reads visible (Phase 2.2E) | Rows: C&W (starts late, first window Fri Oct 10 00:00 UTC); Plague Race (daily 00:00 UTC per the prod schedule); Leagues (HELD, no fix date); Endless (daily + weekly Mon 00:00); Season Pass (Oct season running, Nov season Nov 1 00:00); Quests (in, push not ready); Daily Gift (in, push not ready). Boss Arena, Zombie Lane and Halloween off. The sheet also carries the recommendation with trade-offs, which is one of the contents Frederick lists (F8). |
| R2 Pushes tab: the PNs Beta tab as it stands, one line per row, local notifications included, minus 4 rows; each goes out only if Ready + LIVE + correct names | Push sheet f_a325dd4a… "PNs Beta" r2–r15; DM reply 097c95c6; brief Push copy | DM reply → push sheet | gsheets_values_get (read), gsheets_values_update (write) | Push sheet shared with Julia (Drive shared_with_emails) | 10 rows; r4 Lives and r6 7-day lapsed go out; r2, r5, r7, r8, r10, r13, r14, r15 held with what is missing |
| R3 Held beat → note on its ticket for its owner | Slack fa3eee2c; ZOM-429 (assignee Douglas) | Hold decision → Linear search for the leaderboard ticket | linear_create_comment | Linear unscoped | Comment on ZOM-429 addressed to Douglas |
| R4 Link the sheet on the calendar ticket | ZOM-78 + cmt_zom78_1 ("Link the sheet here when it is ready.") | DM "link it on the calendar ticket" → ZOM-78 comment | linear_create_comment or linear_update_issue(links) | Linear unscoped | ZOM-78 carries the sheet reference |
| R5 Send Frederick the recommendation | DM 8b090dec ("send me the recommendation back here … I need your call") | DM | slack_send_message (channel D05SD5QLG94, optional thread_ts) | Julia is a DM member | One call with trade-offs, consistent with the calendar facts (call delegated: "I need your call"; subject unnamed, Clarity minor) |
| R6 (via brief) Config locks: a committed config date that misses its lock moves earlier and its owner is told | Gmail Sep 26 correction (Fri Oct 31 10:00 Istanbul = 07:00 UTC); SP spec "locked 24h before each season opens" (Nov 1 00:00 UTC → Oct 31 00:00 UTC) | Brief → Brian's mail → SP spec | gmail_reply_to_message or slack_send_message; gsheets for the cell | Julia mailbox copy; Confluence unscoped | Still-to-do: November config, Brian, before Oct 31 00:00 UTC; Brian told |
| R7 Exclusions | brief (Boss Arena); DM reply (Zombie Lane; 4 push rows); Robert DM (Halloween) | — | — | — | Excluded rows absent |
| R8 Final reply to Julia | implicit | — | chat | — | Summary of what was done |

**2.1 Unique Ground Truth: PASS (5)**

### Unique Ground Truth comparison

**Verdict: PASS (5)**, after the deep recheck. Every fork is either settled by a quoted prompt sentence or persona-visible record, or is an authorized variation with a stated boundary.
- Excluded: B, D, E, F1, F4, F6, F8 and F9.
- Authorized variations: C (channel), F3 (moved-to date), F5 (hold-until) and F7 (subject of the call).

Rubric must accept:
- any new November-config handoff time before Fri Oct 31 00:00 UTC (Wed Oct 29 or Thu Oct 30);
- a Leagues hold-until that is either open (until a fix is verified on prod) or Sun Nov 2 23:59 UTC;
- any single reasoned recommendation call with trade-offs;
- an email reply or a Slack DM to Brian.

No fork meets every BOTH_FAIR_FIGURE condition. In each of F3 and F5 an incorporated rule or an explicit delegation sets the acceptable range, so they are recorded as authorized variations.

| Candidate interpretation | Prompt/source authority | Material actions and outputs | Resolved or genuinely ambiguous? |
|---|---|---|---|
| **A, best-supported:** follow the DM and the incorporated brief in full | P: "his working rules for building it are in the brief he shared with me"; brief: "A committed date that misses the lock moves earlier and its owner is told."; Brian: "Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one."; SP spec: "locked 24h before each season opens" | Sheet (Calendar + Pushes); ZOM-429 note (Douglas); ZOM-78 link; Slack DM to Frederick; message to Brian that the Oct 31 07:00 UTC handoff misses the Oct 31 00:00 UTC lock | Leading |
| **B, strongest alternative:** do only the four writes the prompt lists; the lock miss goes in the sheet only, and Brian gets no message | P: "If a beat ends up held, leave a note on its ticket so the owner picks it up." / "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for." | Same, minus the message to Brian | **EXCLUDED.** Authority (the incorporated brief requires "its owner is told"); newer source (Sep 26 correction); scope (SP lock). Prompt → brief chain quoted. |
| C: tell Brian by Slack DM instead of an email reply | brief: "its owner is told" | Same writes and content; channel differs | **AUTHORIZED_VARIATION** (objective acceptance boundary: Brian receives the lock-miss notice by any cataloged channel). Scored once under Clarity 3. |
| D: Leagues not held (Douglas, ZOM-429: "if a player force-closes and reopens, they land in the new week fine, so not blocking") | brief: "a reset that needs a restart" does not hold | No ZOM-429 note; Leagues shown running | **EXCLUDED.** Newer source: Vincent, Sep 30 on prod: "I killed the app and reopened it twice … my week is still last week one. Same on the second device."; brief: "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart." |
| E: Halloween placed on Robert's Sep 18 "approved from my side" | #zombie-art 2e75e232 | Extra one-off row | **EXCLUDED.** Robert's Sep 30 DM: "pulling my ok. Take it off the beta calendar … my later word on this one is the one that counts"; brief: "if he takes that back his later word is the one that counts"; SP spec: "Owner: Robert (Product)." |
| F1 (P1-DR1): Season Pass and C&W held, because Arthur's Sep 30 review notes on #438/#370 are "change-request review blockers" | brief: "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it." | Two more held beats and two more ticket notes | **EXCLUDED.** Both notes are filed as `'COMMENTED'` reviews (#438#rev_4, #370#rev_1); #470#rev_9 is `APPROVED`; the export's change-request state is `CHANGES_REQUESTED` (only #303, July, outside the cohort). Brief: still-to-do covers "player-facing art an owner has flagged", and "cosmetic, VFX and performance gaps" do not hold. |
| F3 (P1-DR3): moved-to handoff target Wed Oct 29 instead of just before the lock | Brian Sep 22: "The config handoff we agreed with Product is for Wed Oct 29" | Same writes; target date differs | **AUTHORIZED_VARIATION.** Objective boundary from the brief: "Every config a beat needs lands before its lock, read in server time (UTC)." Any time before Fri Oct 31 00:00 UTC passes. |
| F4 (P1-DR4): every beat with a held start push counts as held, so up to 5 more notes | brief: "an event window, a reset or a start push"; "Anything else is held, with what is missing." | More ticket notes | **EXCLUDED.** Brief: "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart." Frederick separates "if anything is held and until when, the push that goes with it". |
| F5 (P1-DR5): Leagues hold-until Sun Nov 2 23:59 UTC vs open | brief: "The rules stay here; the calls are yours." | Same writes; the hold-until cell differs | **AUTHORIZED_VARIATION** (explicit delegation; no record dates a ZOM-429 fix). Boundary: held, with no invented in-span fix date. |
| F6 (P1-DR6): Season Pass first window Nov 1 00:00 UTC, or clipped to the span | Brian: "The November season still opens on Sat Nov 1." | First-window value | **EXCLUDED.** Brief: "A beat starts with the first window that opens after its server windows are live on prod"; #470: "Season Pass schedules are already running on prod"; CDK `"0 0 1 * *"`; Snowflake EVT-0527 partial first season `"start_date": "2025-09-29", "end_date": "2025-09-30"`. So the first window is Oct 1 00:00 UTC. Brief: "a different instant is not" (rules out clipping). |
| F7 (P1-DR7): the call concerns scaling the buy, not running the calendar | UA deck: "hold the spend there until the pivot call" | Same single DM; the call's subject differs | **AUTHORIZED_VARIATION** (explicit delegation: "I need your call, not a list of what we have."). Boundary: one call, with trade-offs, consistent with the calendar. Subject unnamed, counted once under Clarity. |
| F8 (P1-DR8): recommendation only in the DM, not in the sheet | Frederick: "send me the recommendation back here" | Sheet contents differ | **EXCLUDED (fork settled; leading reading updated).** Prompt: "What he wants in it is in his message"; the message lists "…and your recommendation with the trade-offs. Put it in the calendar sheet". The sheet therefore also carries the recommendation. |
| F9 (P2-DR3): Plague Race runs back-to-back 5-day windows (Snowflake) | Snowflake EVT-0514 `"start_date": "2025-09-22", "end_date": "2025-09-26"` | Window instants | **EXCLUDED** by authority. Brief: "after its server windows are live on prod"; persona-visible #zombie-ops: "every day at 00:00 AM UTC"; CDK `PLAGUE_RACE_SCHEDULE: props.production ? "0 0 * * *"`. The data conflict itself fails Cross-Service Coherence. |

Field comparison. B vs A: decision, writes, destinations and contents all DIFFERENT. C vs A: destinations DIFFERENT, the rest SAME. D vs A: all DIFFERENT. E vs A: decision and contents DIFFERENT.
Option inventory: complete. The prompt has no explicit option list; "If a beat ends up held" is a conditional.
Challenge review: B is strongest because it is the only alternative that changes the write set using the prompt's own wording; it is not a strawman. The cited brief sentence governs exactly this decision.

**Decision sweep (one row per item, with the record that settles it)**

| Kind | Item | Outcome | Settled by |
|---|---|---|---|
| Beat | Collect & Win | In, starts late. First window Fri Oct 10 00:00 UTC (Fri–Sun). The Wed–Thu Oct 8 window is pre-empted by the Oct 8 15:00 UTC release. Then Mon–Tue / Wed–Thu / Fri–Sun through Nov 2. Not held. | GCal evt_5c1e83a7 `2025-10-08 15:00:00+00`; #470 rc_10 "still on the DEV stack only, they reach prod with the next backend release"; brief "When a beat starts"; CDK `WIN_AND_COLLECT_GROUP_1/2/3` prod crons |
| Beat | Plague Race | In; daily windows 00:00–00:00 UTC; not held | CDK `PLAGUE_RACE_SCHEDULE: props.production ? "0 0 * * *"`; #470 "already running on prod" |
| Beat | Leagues (weekly leaderboard) | HELD. Weekly reset Mon 00:00 UTC. Hold until: no record gives a fix date, so the hold lasts until a fix is verified on prod. | Slack fa3eee2c (Sep 30) supersedes cmt_zom429_1 (Sep 23); brief Held rule; CDK `LEAGUES_SCHEDULE "0 0 * * 1"` |
| Beat | Endless Monster Mode | In; daily reset 00:00 UTC and weekly Mon 00:00 UTC; not held; nothing still to do | Confluence `page_liveops_calendar`; CDK ENDLESS crons; ZOM-565 comment (VFX in); ZOM-504/517/546 comments (visual only / not reproducible) |
| Beat | Season Pass | In. October season running (Oct 1 00:00–Nov 1 00:00 UTC); November season opens Sat Nov 1 00:00 UTC. Not held. | CDK `SEASON_PASS_SCHEDULE "0 0 1 * *"`; brief; #470; SP spec cadence |
| Beat | Quests rollover | In (new set with the Mon Oct 13 rollover); push not ready; no window dates | brief quest/daily-gift rule; Trello 68dac820; PNs Beta r2 "Not Ready" |
| Beat | Daily Gift | In; push (Login Calendar) not ready; the frame is not a still-to-do | brief; r13; #471 c_18 (Sep 30) supersedes cmt_zom432_1 (Sep 24); cmt_zom556_1 (counter display only) |
| Beat | Boss Arena / Zombie Lane / Halloween | Off | brief; DM reply 097c95c6; Robert DM 58d06bd5 |
| Push | r2 Quests | Held: Not Ready | PNs Beta r2 |
| Push | r4 Lives recharged (local) | Goes out: Ready, LIVE, no game name | r4 "Full Ammo Reloaded!"; DM reply "Copy that does not name the game at all is fine" |
| Push | r5 1-day lapsed (local) | Held: names "Puzzles vs Zombies" | r5 |
| Push | r6 7-day lapsed (local) | Goes out | r6 |
| Push | r7 FTUE (local) | Held: names "Puzzles vs Zombies" | r7 |
| Push | r8 Win & Collect | Held: Not Ready, WIP, Domino name | r8; Confluence "Same feature as Win & Collect on Domino Delights, under a different name" |
| Push | r10 Plague Race | Held: WIP | r10 |
| Push | r13 Login Calendar | Held: Not Ready, WIP | r13 |
| Push | r14 Season Pass | Held: Not Ready, WIP | r14 |
| Push | r15 Weekly Leaderboard | Held: WIP (and the beat is held) | r15 |
| Push | r3, r9, r11, r12 | Left off | DM reply |
| Still-to-do | C&W server windows to prod | Douglas (organizer of the Oct 8 release) | GCal organizer; Event Engine page "Scheduler … Backend (Douglas)" |
| Still-to-do | C&W final vial sprites | Claire | #370 rc_1 |
| Still-to-do | C&W event icon animation | Marcus | #454 c_4 (Sep 30) supersedes cmt_zom465_1; the #454 body lists no C&W icon |
| Still-to-do | SP November config | Brian. The Oct 31 07:00 UTC commitment misses the Oct 31 00:00 UTC lock, so it must land before the lock. | Gmail Sep 26; SP spec; brief Config locks |
| Still-to-do | SP premium strip moved to the November range | Oliver | #438 rc_74 |
| Excluded | ZOM-526, ZOM-543, analytics (ZOM-552/566/387/442/549), ZOM-565/344/471/432 (reported done), ZOM-465 refill-timer item | Not still-to-dos | cmt_zom526_2 "does not have to land"; cmt_zom543_1 (C&W already in the flow); brief "not analytics"; owners' comments; ZOM-465 "(… do we still need to do that?)" |
| Write | Sheet (Calendar + Pushes + the recommendation), ZOM-429 note, ZOM-78 link, DM to Frederick, notice to Brian | As in the ledger | Prompt S3/S4/S5/S6; brief Config locks |

**2.2 Feasibility: PASS (5)**

| Ask | Required capability | Tool(s) | Feasible? |
|---|---|---|---|
| Fill the two tabs | Write cell ranges | gsheets_values_update / gsheets_values_append | Yes (SUPPORTED) |
| Note on ZOM-429 | Create a comment | linear_create_comment | Yes |
| Link on ZOM-78 | Comment or links field | linear_create_comment / linear_update_issue(`links`) | Yes. Evidence limit: the injected Drive row has `web_view_link` NULL (156 of 356 base spreadsheets are also NULL), so the link may be an ID-based URL or a title reference. |
| DM to Frederick | Post in DM | slack_send_message (`channel`, `thread_ts`) | Yes |
| Tell Brian | Reply to mail or DM | gmail_reply_to_message / slack_send_message | Yes |

B. Data feasibility: every fact in the decision sweep was found (paths and pointers are in the record's `sources`). C. Dimensional: no per-X breakdown beyond per-beat and per-push rows, which the data carries. D. Numeric observability: UTC instants are explicit (GCal `start_ts` 15:00Z; CDK crons). Brian's "10:00 Istanbul time" needs UTC+3, which the data itself demonstrates ("release window 18:00-19:00 Istanbul time" against 15:00–16:00Z). The 24h lock is stated.

E. Persona-scoped read feasibility (scoped set from acl.md: Gmail, Slack, GCal, GDrive, GDocs, GSheets, GSlides)

| Required scoped fact | Record | Visibility basis | Verdict |
|---|---|---|---|
| Frederick's ask and reply | Slack D05SD5QLG94 | Julia (EMPLOYEE_0005) in members | Feasible |
| Robert's pull | Slack D05GU6L0XFH | Julia in members | Feasible |
| Robert's Sep 18 approval (decoy) | #zombie-art C08R8CHB0QL | Julia in members | Feasible |
| Vincent's re-test | #zombie-match3d C0880U9751A | Julia in members | Feasible |
| Brian's handoff and correction | Gmail `julia.lawson@harmonygames.co/…` copies | Julia's mailbox | Feasible |
| Backend release instant | GCal evt_5c1e83a7 on calendar julia.lawson@ | Own calendar | Feasible |
| Brief, UA deck | Drive f_7c3e91a4, f_2b9d4e7a | Shared with Julia (reader) | Feasible |
| Push sheet | f_a325dd4a… | Shared with Julia | Feasible |
| Calendar sheet | f_e4a17c90… | Owned by Julia | Feasible |

The #zombie-prs bot mirrors (Julia is not a member) are not required: the GitHub originals are unscoped. Lens 2: no ask directs a read outside Julia's view. **Persona ACL Reachability: PASS (5).**

**2.3 Truthfulness: PASS (5)**

| Premise | Found? | Accurate? | Evidence |
|---|---|---|---|
| "Frederick messaged me yesterday asking for the live-ops and push calendar" | Yes | Yes | DM 8b090dec created 2025-09-30T20:20:00Z (Sep 30 PT): "Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2." |
| "the Zombie Match 3D beta, the four buy weeks that start Monday the 6th" | Yes | Yes | Deck: "W1 Mon Oct 6 - Sun Oct 12" … "W4 Mon Oct 27 - Sun Nov 2"; Oct 6, 2025 is a Monday |
| "What he wants in it is in his message" | Yes | Yes | The DM lists the contents |
| "his working rules … in the brief he shared with me" | Yes | Yes | Drive f_7c3e91a4 shared_with ["julia.lawson@harmonygames.co"], reader; "How I want the beta calendar built" |
| "my live-ops calendar sheet" | Yes | Yes | f_e4a17c90 "ZM3D Beta Live-Ops Calendar", owner Julia, in "ZM Live Ops" (d_5f2c8e1b…, under Julia's root d_8140f09b…) |
| "the calendar ticket" | Yes | Yes | ZOM-78 "Event Calendar For Zombie Match 3D"; cmt_zom78_1: "Let us use this ticket for the ZM3D beta live-ops calendar" |
| "the recommendation he asked for" | Yes | Yes | "send me the recommendation back here" |

The prompt contains no tight identifiers. No departed persons are involved, and nothing post-dates the cut (all injected events are at or before 2025-09-30T22:10Z; future items such as the Oct 8 release and the Oct 31 handoff are framed as future).

**2.4 Cross-service: PASS (5).** Slack: holds Leagues; excludes Halloween; sets push scope. Gmail: the corrected Oct 31 date creates the lock miss and the Brian notice. GCal: the 15:00 UTC release fixes C&W's first window at Oct 10. GitHub: CDK windows and PR comments set the C&W still-to-dos and owners. Linear: ZOM-429 and ZOM-78 are write targets, and the comments set exclusions. Sheets: push rows. Confluence: the lock and "Product" = Robert. Trello: the quest set. Every service changes a graded fact, and there are several writes.

**2.5 Investigation + Action: PASS (5).** Every write depends on discovered holds, owners and dates.

**2.6 Clarity & Specificity: NON-FAIL (3)**

| Question | Answer |
|---|---|
| Intent clear? | Yes |
| Key details present? | Yes, via the incorporated sources |
| Interpreted multiple ways? | Yes, on one point. The brief's "its owner is told" names no channel, so Brian may be told by email reply or Slack DM. |
| Different write actions? | No. Same recipient and content; only the channel differs. Minor Clarity (NON-FAIL 3) per §2.6 ("channel-of-delivery to the same recipient"). |
| Other same-write variations | (a) The decision the recommendation answers is unnamed: running the calendar, or scaling the buy (P1-DR7). (b) The brief's "a recurring beat slots" / "Product latest dated approval" wording (P1-DR9; resolves to Robert via the SP spec, with the same outcome either way). |
| Delegation scan ("I'll …") | None in the prompt |

**2.7 Contrived vs natural: PASS (5).** No exact timestamps, opaque IDs, step list, trap hint, riddle, hidden destination (the sheet is named, the ticket is "the calendar ticket", the recipient is Frederick), audit-form wording or if-chain (one natural conditional). Spec-sheet triggers: 0 of 4. Natural difficulty comes from scattered rules, stale-vs-newer sources (five pairs), decoys, and a CDK file that holds the windows.

**2.8 Alignment with today's date: PASS (5).** "Yesterday" = Tue Sep 30, 2025, which matches the DM. "Monday the 6th" = Mon Oct 6, 2025, in the future. The calendar span is entirely future.

**2.9 Originality: N/A.** No comparison samples were supplied and no dataset similarity library is bundled.

---

### Phase 3: Universe Feasibility

**3.1 Data existence:** all 7 prompt premises and every decision-sweep item are verified and retrievable through cataloged tools. The CDK stack is read with github_get_file_contents. **PASS (5).**

**3.2 Cross-Service Coherence: FAIL (2)**

Rules applied (Eval 1 §3.2 as written):
- Any inconsistency in task-touched data fails, whether or not the contributor introduced it. This applies to synthetic Snowflake and Confluence data too.
- NON-FAIL 3 is allowed only for one single low-impact inconsistency. Two or more fail.
- State / Lifecycle and Quantitative inconsistencies always fail.
- Base conflicts on the known-issue list (`Task_Authoring/references/known_data_issues/synthcut.md`) count only when the injection builds on them in data the answer depends on. Otherwise they are advisories.

| Prompt ask / source | Static evidence | Prompt-specific discovery/access | Task coherence |
|---|---|---|---|
| Frederick DM + reply (8b090dec, 097c95c6) | NEW; Eval 0 PASS | Julia is a member | PASS |
| Robert's approval in the #zombie-art Halloween thread | NEW; reply_count 0→1 ✓ | Julia is a member | PASS |
| Robert's pull (58d06bd5) | NEW; Eval 0 A5 | Julia is a member | **Low-impact #1:** threaded under the unrelated "How do you think we should make the game catered to more hardcore players?" (D05GU6L0XFH/2025-09.json /675) |
| Vincent's re-test (fa3eee2c) | NEW | Julia is a member; a separate issue from the base Sep 22 #zombie-bugs participation bug ("it's working fine right now") | PASS |
| #zombie-prs mirrors ×5 | NEW; counts reconcile; Eval 0 A4 | Not required (GitHub is unscoped) | PASS (advisory) |
| Brian's Gmail correction (Sep 26) | NEW; Eval 0 A2/A3 | Julia's copy | **Low-impact #2:** "Re:" with In-Reply-To = the Sep 22 message, but its own thread (`…/1844835127305531392` vs `…/1844470925517303296`); base: 216 of 216 sampled replies share the parent's thread. Snippet ≠ body start (the Sep 22 row's snippet equals its normalized first 175 body characters). |
| GCal release ×4 | NEW; Eval 0 A7 (`transparent`) | Julia's copy | PASS (advisory) |
| Drive / Docs / Slides / Sheets | NEW | Shared or owned | PASS |
| **Linear notes on Todo tickets** | NEW; Eval 0 A8 (SC-16) | Unscoped; the still-to-do column reads them | **FAIL: State / Lifecycle (C1 = P2-DR2)** |
| **GitHub notes on #370 / #438 / #454** | NEW | Unscoped; they carry three still-to-dos and owners | **FAIL: State / Lifecycle (P2-DR1)** |
| GitHub notes on #470 / #471 | NEW; 0.01 and 0.22 days after merge (inside the base ≤ 0.26-day pattern) | Unscoped | PASS |
| **Plague Race windows: Snowflake vs prod schedule** | Base synthetic Snowflake; not a listed card (SC-31 is weekend-outage rows only) | Answer must state Plague Race windows | **FAIL: Cross-service Referential (P2-DR3)** |
| Confluence `page_liveops_calendar` vs CDK reward import | Base, listed SC-62 | Not depended on | Advisory (known-issue rule) |
| SP spec ship-date/analytics (SC-38) | Base, listed SC-38; Eval 0 A8 | Not depended on (answer uses only "locked 24h …" and "Owner: Robert (Product)") | Advisory (known-issue rule) |
| ZOM-521 untick; ZOM-526 notes | NEW; repairs SC-15 (Eval 0 A11) | — | PASS |
| Review timeline events `commented` | NEW; P2-DR6 / Eval 0 A7; base uses `reviewed` with empty actor (2,116) | Answer never reads them | Advisory |

**C1 (= P2-DR2): Linear State / Lifecycle (fail-level).** Injected owner notes say the work is in, live, signed off or closable on tickets left in `Todo` with no start (base: no ZOM Todo ticket has `started_at`):
- ZOM-565 (`Todo`, `started_at` null): "The endless start screen vfx is in (commit f7e971b0). Claim button glow and the new bar are both live now, can close."
- ZOM-344: "Art side is signed off on my end."
- ZOM-471: "Red dot asset is ready and wired to the Plague Race state check"
- ZOM-432 (`Todo`), while PR #471 c_18 says "The daily-gift frame went out with this PR … that one can be closed."
- Weaker instances: ZOM-566 and ZOM-387 (Todo with in-progress notes); ZOM-542 (`Regression` with "Regression pass on the mode switch looks clean").

This reproduces listed card SC-16 on records the answer depends on.

**P2-DR1: GitHub State / Lifecycle (fail-level).** Notes that a merged PR's own scope is incomplete land long after merge, and each PR's `updated_at` is bumped:
- #370 "The final vial sprites are still missing for the Collect & Win set": merged 2025-08-13T16:12:18Z, note 48.15 days later.
- #438 "needs to move to the November range": 14.9 days after merge.
- #454 "still to do on my side": 11.01 days after merge.

Across all base repos there are 20 post-merge reviews or comments, and none lands more than 0.26 days after merge.

**P2-DR3: Cross-service Referential (fail-level; it changes a window the answer uses).** Persona-visible #zombie-ops (C08R6BF4ENN/2025-06.json /298): "currently `PROD` schedules are: … Plague Race: _`every day at 00:00 AM UTC`_". The CDK: `PLAGUE_RACE_SCHEDULE: props.production ? "0 0 * * *"`. Synthetic Snowflake `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE` has 20 ZM3D Plague Race rows, all back-to-back 5-day runs, the latest being EVT-0514 `2025-09-22`→`2025-09-26`. Rule applied: the §3.2 presence rule for synthetic Snowflake data in task-touched records. No known-issue card covers this conflict.

Low-impact tally: 2 (P2-DR4, P2-DR5). §3.2 allows one for NON-FAIL, so these two fail together even before C1, P2-DR1 and P2-DR3. Injection SQL considered: Yes. Static integrity: Eval 0 PASS / COMPLETE (separate reviewer), plus direct task-record checks.

---

### Phase 4: Final Evaluation

| Dimension | Sub-dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Every fork excluded by a quote or authorized with a boundary (comparison above; fork list below) |
| Prompt | Feasibility | 5 | All asks supported (gsheets, linear, slack, gmail write paths); link-rendering limit noted |
| Prompt | Persona ACL Reachability | 5 | Every scoped read is visible to Julia |
| Prompt | Explicit Tool Mention | 5 | None (P4 confirms) |
| Prompt | Clarity & Specificity | **3** | Three same-write minors: the channel for telling Brian; the unnamed decision the call answers; the brief's "Product latest dated approval" wording |
| Prompt | Contrived / Unnatural | 5 | Natural six-sentence trigger (P4: 0 triggers) |
| Prompt | Alignment with Today's Date | 5 | Yesterday = Sep 30; Oct 6 is in the future (P3 confirms) |
| Prompt | Originality / Sample Similarity | N/A | No samples or similarity library |
| Prompt | Truthfulness | 5 | 7 of 7 premises (P3: 14 tight claims, none wrong) |
| Prompt | Tool Use & Cross-service | 5 | Every service changes a graded fact |
| Prompt | Investigation + Action | 5 | Writes depend on discovery |
| Prompt | Coherence (Bolt-on) | 5 | Every sentence is load-bearing |
| Prompt | Persona | 5 | PM who leads the live-ops pod |
| Prompt | Business Function | 5 | Product planning (watch: overlap with Live-Ops/Growth) |
| Prompt | Assigned Competency | 5 | Beta UA/GTM launch and push calendar |
| Prompt | Assigned Task Skill | 5 | Planning plus a decision call |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three are load-bearing |
| Universe | Data Exists | 5 | All facts retrievable |
| Universe | Cross-Service Coherence | **2** | Three fail-level groups (C1, P2-DR1, P2-DR3) plus two low-impact items |

### Issues Found

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | Linear notes say done/live/closable on Todo tickets: ZOM-565, ZOM-344, ZOM-471, ZOM-432 (via #471 c_18); weaker ZOM-566, ZOM-387, ZOM-542. Repeats SC-16. | Major | Cross-Service Coherence (State/Lifecycle) |
| 2 | Open-work notes on merged PRs #370/#438/#454, 11–48 days after merge (base maximum 0.26 days) | Major | Cross-Service Coherence (State/Lifecycle) |
| 3 | Plague Race windows: Snowflake 5-day runs vs prod schedule and #zombie-ops "every day at 00:00 AM UTC" | Major | Cross-Service Coherence (Cross-service Referential) |
| 4 | Halloween retraction threaded under an unrelated DM message | Minor | Cross-Service Coherence (Other) |
| 5 | Brian's "Re:" correction in a separate Gmail thread; snippet ≠ body start | Minor | Cross-Service Coherence (Identifier/Format) |
| 6 | Channel for telling the config owner is unspecified | Minor | Clarity |
| 7 | The decision the recommendation answers is unnamed | Minor | Clarity |
| 8 | Brief wording "a recurring beat slots" / "Product latest dated approval" | Minor | Clarity |
| 9 | Downstream: the rubric must accept the authorized variations (moved-to date before the lock; open or span-end hold; any single call; email or DM to Brian) | Advisory | UGT (downstream) |

### Recommended minimum fixes (ordered; all in the injection SQL; the prompt needs no change)

Each fix below was checked as deep_recheck step 5 requires: values are quoted from the records named, and no fix adds a lock-in.

**Linear tickets (Issue 1).** Make each ticket's state match its note. The base ZOM `Done` pattern is: `completed_at` always set (427/427), `updated_at = completed_at` (401/427), `started_at` may be NULL (120/427). Do not use In Review (no ZOM ticket uses it; listed card SC-32).

| Ticket | Change | Constraint (t ≤ 2025-10-01T06:59:59Z in every row) |
|---|---|---|
| ZOM-565 | Replace the `updated_at` UPDATE with state `Done`, `completed_at = updated_at = t` | t ≥ 2025-09-29T16:05:00Z (the time of `cmt_zom565_1`) |
| ZOM-344 | Same | t ≥ 2025-09-16T16:20:00Z |
| ZOM-471 | Same | t ≥ 2025-09-17T16:45:00Z |
| ZOM-432 | Same | t ≥ 2025-09-30T21:07:26Z (#471 c_18). Calvin's Sep 24 note stays as the stale side. |
| ZOM-566 | State `In Progress` with `started_at` | created 2025-09-30T16:26:02Z ≤ started_at ≤ 2025-09-30T19:40:00Z. Base: every ZOM In Progress ticket has `started_at` (15/15). |
| ZOM-387 | State `In Progress` with `started_at` | 2025-07-15 ≤ started_at ≤ 2025-07-25T14:00:00Z |
| ZOM-542 | Optional: state `Done` | completed_at ≥ 2025-09-22T18:40:00Z |

**Merged-PR notes (Issue 2).**
1. Delete the injected rows for #370 (`#370#rev_1`, `#370#rc_1`, `#370#ev_5`, the `updated_at` UPDATE), #438 (`#438#rev_4`, `#438#rc_74`, `#438#ev_9`, UPDATE) and #454 (`#454#c_4`, `#454#ev_6`, UPDATE).
2. Delete their three #zombie-prs mirrors (`408dca28…`, `cc8ce0e4…`, `8a9a7466…`) and the parent UPDATEs, so `d648cbe9…`, `2f138acf…` and `ef414467…` stay at their base reply_count 2, 78 and 3.
3. Re-seed the three owner flags as top-level messages in #zombie-art `C08R8CHB0QL`, with thread fields NULL, a unique ts, and 2025-09-30 ≤ ts ≤ 2025-10-01T06:59:59Z. Authors must be channel members (both are listed in channels.json).
   - Arthur, `EMPLOYEE_0025_SLACK_ID`: "The final vial sprites are still missing for the Collect & Win set — Claire has those on her list." and "The Season Pass premium strip needs to move to the November range rather than the current one — Oliver is taking the date change."
   - Marcus, `EMPLOYEE_0002_SLACK_ID`: "The Collect & Win event icon animation is still to do on my side — the other menu icons in the animated-icons PR are finished." ("animated-icons" is the wording of PR #454 "Marcus/animated icons" and `cmt_zom465_1`.)

**Plague Race cadence (Issue 3).** The Snowflake rows cannot be fixed by the author: the bundled schema "does not cover Confluence or Snowflake injection tables". Instead, stop the answer depending on Plague Race windows by editing the brief's `docs_documents.body_text` (f_7c3e91a4…):
- Change "For the quest rollover and the daily gift (the Login Calendar row on the push sheet) put down" to "For the quest rollover, the daily gift (the Login Calendar row on the push sheet) and Plague Race put down".
- This adds 13 characters, so every style run from "Held or not" onward shifts. Fix 9's grammar edit is length-neutral and fix 7's edit sits after the last heading, so the headings become: Held or not 1230–1241, One-offs 1728–1736, Still to do 1929–1940, Push copy 2158–2167, Config locks 2484–2496. The title (0–43), Span and time base (163–181), Scope (424–429) and When a beat starts (611–629) are unchanged.

**Halloween retraction (Issue 4).** On `58d06bd5…`, set `thread_parent_id` and `thread_ts_legacy` to NULL, matching the base top-level DM messages, and delete the `reply_count` UPDATE on `c54310280ca0915181508d6e9b964926` (base value 0).

**Brian's Gmail correction (Issue 5).** For each of the three Sep 26 copies:
- set `thread_id` to `<mailbox>/1844470925517303296` and the X-GM-THRID header to `1844470925517303296`;
- set `mbox_from` to start with `1844470925517303296@xxx`;
- set `snippet` to the body's normalized first 175 characters, as the Sep 22 row does: "Julia, Correction to my Sep 22 mail, Frederick in copy: the November Season Pass config handoff moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time. Same contents, same o".

Then drop the three `gmail_threads` rows for `…/1844835127305531392`.

**Clarity fixes (Issues 6–8).**
- 7 (Issue 6). In the brief's Config locks line, change "moves earlier and its owner is told." to "moves earlier and its owner is told in a reply on their handoff mail." ("handoff mail" matches Brian's subject "ZM3D Season Pass November config handoff".)
- 8 (Issue 7). In Frederick's DM `8b090dec…`, change "and your recommendation with the trade-offs." to "and your recommendation, with the trade-offs, on whether and from which buy week we scale the spend." The deck supplies the wording ("The four buy weeks", "scaled up week by week", "hold the spend there until the pivot call"). It keeps the recommendation in the calendar's contents list (F8), and any answer remains valid, including no scale-up.
- 9 (Issue 8). In the brief, change "One-offs may overlap a recurring beat slots. A one-off may take a recurring beat slot only with Product latest dated approval" to "One-offs may overlap recurring beat slots. A one-off may take a recurring beat slot only with Product's latest dated approval".

**Optional cleanups (not needed for a 5).** Make `#470#ev_9` a `reviewed` event with an empty actor (base: 2,116); set GCal `transparency` to `opaque`.

**Not fixable by the author and not counted:** SC-62 (reward-import cadence), SC-38 (SP ship date/analytics), the PLATFORM anonymized tokens, and the Snowflake Plague Race rows themselves (avoided by the Issue 3 fix).

---

## Deep Recheck

Passes: P1, P2, P3, P4. Each was a fresh subagent on Opus 5.5, blind to the main review. Eval 0 was run in parallel by a separate reviewer.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 42 sentences (6 prompt + 36 incorporated) | 9 | 4 (DR3, DR5, DR7 as authorized variations; DR9 as a Clarity minor); 5 rejected |
| P2 | 6 prompt sentences, 112 SQL statements | 7 | 7 (DR1–DR5 scored; DR6 and DR7 advisories) |
| P3 | 6 sentences, 14 tight claims, 112 statements | none | — |
| P4 | 6 sentences | none | — |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it." | github #438#rev_4, #370#rev_1 | §2 | Unique Ground Truth | REJECTED | Both reviews are `'COMMENTED'`; #470#rev_9 is `APPROVED`; change requests carry the state `CHANGES_REQUESTED` (only #303, July); brief: "player-facing art an owner has flagged" is a still-to-do |
| DR2 | P1 | "A committed date that misses the lock moves earlier and its owner is told." | Gmail Sep 26 correction; SP spec | §2 | Clarity | REJECTED | Prompt: "his working rules for building it are in the brief he shared with me"; the incorporated rule requires the owner be told; channel only, scored as a Clarity minor |
| DR3 | P1 | "A committed date that misses the lock moves earlier" | Brian Sep 22 "agreed with Product is for Wed Oct 29" | §2 | Unique Ground Truth | CONFIRMED | Authorized variation: brief "lands before its lock"; any time before Fri Oct 31 00:00 UTC |
| DR4 | P1 | "If a beat ends up held, leave a note on its ticket so the owner picks it up." | PNs Beta rows | §2 | Clarity | REJECTED | Brief: "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart." |
| DR5 | P1 | "if anything is held and until when" | ZOM-429; Slack fa3eee2c | §2 | Unique Ground Truth | CONFIRMED | Authorized variation: no dated fix; brief "the calls are yours"; open or span-end |
| DR6 | P1 | "A beat starts with the first window that opens after its server windows are live on prod" | #470#rc_10; CDK `"0 0 1 * *"` | §2 | Unique Ground Truth | REJECTED | #470: "Season Pass schedules are already running on prod", so Oct 1 00:00 UTC; brief "a different instant is not" rules out clipping |
| DR7 | P1 | "I need your call, not a list of what we have." | UA deck "hold the spend there until the pivot call" | §2 | Clarity | CONFIRMED | Explicit delegation of the call; subject unnamed, a same-write minor |
| DR8 | P1 | "What he wants in it is in his message" | Calendar sheet headers | §2 | Unique Ground Truth | REJECTED | The DM lists "…and your recommendation with the trade-offs. Put it in the calendar sheet", so the sheet carries it too (leading reading updated) |
| DR9 | P1 | "One-offs may overlap a recurring beat slots." | SP spec "Owner: Robert (Product)." | §6.2 | Clarity | CONFIRMED | Wording slip; same outcome under either referent |
| DR1 | P2 | "what still has to land before it runs and who owns that" | github #370/#438/#454 merged_at vs Sep 30 notes | §3.2 | Cross-Service Coherence | CONFIRMED | 48.15 / 14.9 / 11.01 days after merge; base maximum 0.26 days |
| DR2 | P2 | "Not what already shipped" | ZOM-565/471/432 `Todo`, started_at null | §3.2 | Cross-Service Coherence | CONFIRMED | Merged with C1; same records |
| DR3 | P2 | "which windows it runs in" | Snowflake EVT-0514 vs CDK and #zombie-ops | §3.2 | Cross-Service Coherence | CONFIRMED | `"start_date": "2025-09-22", "end_date": "2025-09-26"` vs "every day at 00:00 AM UTC"; §3.2 presence rule (synthetic Snowflake, not a listed card) |
| DR4 | P2 | "if he takes that back his later word is the one that counts." | 58d06bd5 parent c5431028 | §3.2 | Cross-Service Coherence | CONFIRMED | Parent text "How do you think we should make the game catered to more hardcore players?"; low-impact |
| DR5 | P2 | "its owner is told" | Gmail thread 1844835127305531392 | §3.2 | Cross-Service Coherence | CONFIRMED | In-Reply-To points at the Sep 22 message in thread 1844470925517303296; base 216 of 216; low-impact |
| DR6 | P2 | (records only) | timeline #470/#370/#438 `commented` | §3.2 | Cross-Service Coherence | CONFIRMED | Base `reviewed` with an empty actor; the answer never reads it, so advisory per the Eval 0 advisory rule |
| DR7 | P2 | "Every config a beat needs lands before its lock" | Confluence `0 * * * *` vs CDK `*/5 * * * *` | §3.2 | Cross-Service Coherence | CONFIRMED | Listed SC-62, not depended on, so advisory under the known-issue rule |

Effect on verdict: no dimension score changed; Cross-Service Coherence stays 2, with P2-DR1 and P2-DR3 added as further fail-level groups and P2-DR4 and P2-DR5 as low-impact items. UGT gains forks F1 and F3–F9, all excluded or authorized, so it stays 5. The leading reading now puts the recommendation in the sheet as well as the DM. Clarity stays 3, with P1-DR7 and P1-DR9 added.

Forks:
- F1: SC/C&W not held | A: COMMENTED reviews are not change requests | B: Arthur's notes hold both beats | Settled by: #438#rev_4 / #370#rev_1 `'COMMENTED'`; brief "player-facing art an owner has flagged"
- F2 (= B): tell Brian | A: tell him | B: record only | Settled by: prompt "his working rules for building it are in the brief he shared with me" + brief "its owner is told"
- F2b (= C): channel | A: email reply | B: Slack DM | Authorized: brief "its owner is told" (recipient fixed, channel open; Clarity minor)
- F3: moved-to date | A: before Fri Oct 31 00:00 UTC | B: Wed Oct 29 | Authorized boundary: brief "lands before its lock"; the rubric must accept either
- F4: held pushes | A: note on ZOM-429 only | B: notes for every held push | Settled by: brief "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart."
- F5: Leagues hold-until | A: open until fixed | B: Sun Nov 2 23:59 UTC | Authorized: brief "the calls are yours"; the rubric must accept either
- F6: SP first window | A: Oct 1 00:00 UTC | B: Nov 1 00:00 UTC / clipped | Settled by: brief start rule + #470 "Season Pass schedules are already running on prod" + "a different instant is not"
- F7: recommendation subject | A: running the calendar | B: scaling the buy | Authorized: "I need your call" (Clarity minor until fix 8)
- F8: recommendation location | A: DM and sheet | B: DM only | Settled by: prompt "What he wants in it is in his message" + DM list ending "your recommendation with the trade-offs. Put it in the calendar sheet"
- F9: Plague Race windows | A: daily 00:00 UTC | B: 5-day runs | Settled by: brief "server windows are live on prod" + #zombie-ops "every day at 00:00 AM UTC" (the data conflict fails 3.2)
- D: Leagues held | A: held | B: not held | Settled by: Slack fa3eee2c "I killed the app and reopened it twice … Same on the second device."
- E: Halloween off | A: off | B: placed | Settled by: Robert's DM "my later word on this one is the one that counts" + SP spec "Owner: Robert (Product)."

Platform defects:
- PLATFORM: anonymized tokens `[PERSON_NAME_2549]` (PNs Beta rows 7 and 14) and `PERSON_0396_GITHUB_USERNAME` (#454#c_4) are source strings. Recorded, not scored.
- FD-2880 is incidental: match3d-backend git history runs past `/commits`, and no finding depends on it.

### FINAL VERDICT: FAIL

Score: 2

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort unconfirmed

Next action: Apply the SQL fixes for Issues 1–5 (Cross-Service Coherence) and 6–8 (Clarity) as listed under Recommended minimum fixes, then rerun /injection and /prompt. The prompt text needs no change.

Evidence limits:
- The record is hand-bound and was not validated by hg_prompt_checks.py; the input store and writer were not used, by instruction.
- GCal and Drive link/description rendering is unverified (the injected sheet's `web_view_link` is NULL).
- Snowflake and Confluence injectability is not covered by the bundled schema.
- The thread-level snippet convention for a multi-message Gmail thread is unverified.
- The Example Task and Unique Ground Truth PDFs were not re-read.
- Originality is N/A.

**Lowest Dimension:** Cross-Service Coherence (2). The injection adds State/Lifecycle conflicts (Todo Linear tickets with "done/can close" notes; open-work notes on long-merged PRs), and the task depends on a Plague Race cadence that Snowflake contradicts.

**Summary:** The prompt is a natural, well-grounded six-sentence trigger. Persona, assignment fit, truthfulness, feasibility, ACL reach and design all pass, and every UGT fork is excluded by a quoted record or bounded by the incorporated brief. The task fails on universe coherence: lifecycle conflicts the injection introduces and a Snowflake-vs-schedule conflict in data the answer uses. Three minor same-write Clarity gaps keep Clarity at 3. All fixes are in the SQL.
