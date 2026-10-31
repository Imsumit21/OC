# A — Stage docs and claude skills: changes from current to new

Scope: `Evals/{1_Prompt_Eval.md, 3_Rubrics_Eval.md, 0_Injection_Quality_Eval.md, ENVIRONMENT.md,
UNIVERSE_MAP.md, INPUTS.md, README.md, WORKFLOW.md, EXECUTION.md, 2_Oracle_Events_Eval.md, SEARCH.md,
1A_Hardness_Eval.md, Docs/README.md}` and `claude/{CLAUDE.md, README.md, UNIVERSE_MAP.md,
skills/*/SKILL.md}`, OLD vs `Eval-new/`. References (`Evals/references/**`) and tools (`Evals/tools/**`)
are out of scope (other agents). Diff basis: `diff -u`, plus `cmp` for byte equality.

## Summary

- **Every task now has a date, asked before anything else.** Two universes: `Universe_Normal/`
  (Feb 14, 2026, `hg4-2026-08-31` v37, clock 2026-02-14 00:00 UTC) and `Universe_SynthCut/`
  (Oct 1, 2025, `hg4-synth-sep30cut` v16, clock 2025-10-01 00:00 PT). Saved as key `universe`
  via `hg_store_input.py universe`; no default; tools refuse to read until saved. (A-01, A-02)
- **The three sibling data folders are gone.** They are now `<P>_HarmonyGames_*` inside the selected
  universe folder; every stage doc, skill and count table was rewritten around `<P>`. (A-02)
- **Oct 1 state is not Feb 14 state**: no shutdown rules, Victor Barnes gone since April 2025,
  nothing after 2025-09-30 23:59:59 PT, six storylines absent. (A-03, A-26)
- **Clock, dating and "today" are per-task**; dates are written in PT, tools return UTC, and a day
  grade accepts either PT or UTC day when they differ. (A-04)
- **Injected event timestamps must be ≤ the clock**; only plan fields may be later. (A-05)
- **Injection review got four new hard rules**: grader-facing text is FAIL, a new mandatory
  `hg_injection_lint.py`, readable Drive content, one account per person, generated FTS columns
  untouched, Linear text-date format. (A-06 … A-11)
- **Prompt naturalness flipped**: clean typing is now *good*; staged typos, trap hints/riddles,
  hidden destinations, audit-form wording and long if-chains each fail Contrived on their own.
  (A-12 … A-15)
- **Overly Broad rose from Moderate to Major** in the rubric eval, and its repair may not be a
  count or format. (A-16)
- **Any row an agent passes by doing nothing now fails** Negative Criteria, however worded, and
  every row must carry a `valid_case` and a `do_nothing_case` in a format-5 record. (A-17, A-18)
- **Rubric ↔ OE cross-check is now two-way and mandatory** when the task has OEs; conflicts are
  settled `FIX_ROW` or `FIX_OE`. (A-19)
- **Rubric evidence must be reachable**: not Trash-only, not attachment-only, linked from a prompt
  noun, and named in the evidence; unreachable = `unobservable` Major. (A-20, A-22)
- **OE `Expected:` values are now individually quoted** in an `expected_values` ledger; wrong event
  names, field values, IDs and refuted absence claims are new Accuracy FAILs. (A-23)
- **One narrow UGT exception** (`BOTH_FAIR_FIGURE`) passes when only one reported figure differs and
  both values are persona-visible; the rubric must then accept either value. (A-24, A-25)

## Change log

### A-01 Task date asked first and saved as `universe`
- Files: `Eval-new/Evals/INPUTS.md:14-37`, `:68-71`; `Eval-new/Evals/EXECUTION.md:20-25`;
  `Eval-new/claude/CLAUDE.md:7-13`; `Eval-new/claude/skills/{prompt,injection,oe,rubric,hardness}/SKILL.md:10-25`
  (OLD: `Evals/INPUTS.md:1-12` has no date section; `Evals/EXECUTION.md:20`; `claude/CLAUDE.md:1-4`)
- Category: universe-date
- Old → New: previously a task had one implicit universe and the first step was `list` + save inputs.
  Now every skill "read[s] `universe_intake`" and, unless `SELECTED`, asks only
  "Which date is this task on: Oct 1, 2025 (synth-cut) or Feb 14, 2026 (normal)?" before any other
  question, then saves it (`hg_store_input.py universe`). `hg_universe.py show` prints the choice.
- Authoring impact: `01_Scenario_Design` must fix the universe before any story/entity research and
  record it; every later playbook (`01_Universe_Injection`, `02_Reference_Files`, `04_Prompt_Writing`,
  `05_Human_Time_Estimate`, `08_Oracle_Event_Writing`, `09_Rubric_Writing`, `12_Difficulty`,
  `01a_Hardening`) must load the saved date (not assume Feb 14) and never infer it from the prompt.
  The creation runner must write `Evals/task_inputs/02_Universe_Date.txt` before any eval stage runs.
- Severity: BLOCKING

### A-02 Two universes replace the three sibling base folders
- Files: `Eval-new/Evals/UNIVERSE_MAP.md:3-46`, `:50-70` (OLD: `Evals/UNIVERSE_MAP.md:3-9`, `:22-36`);
  `Eval-new/claude/UNIVERSE_MAP.md:3-9` (OLD: `claude/UNIVERSE_MAP.md:3-6`)
- Category: universe-date
- Old → New: "Extract these five folders" becomes four folders: `Evals/`, `claude/`,
  `Universe_Normal/`, `Universe_SynthCut/`, each universe holding `<P>_HarmonyGames_GitHub/Gmail/
  Other_Services`. Service paths, counts and manifest locations are now per universe. The Feb 14
  build is v37 and its GitHub count moved 255049 → 255030; Oct 1 differs widely
  (e.g. github 265171, trello 13).
- Authoring impact: all creation stages that read exports (`01_Scenario_Design`,
  `01_Universe_Injection`, `02_Reference_Files`, `08_Oracle_Event_Writing`, `09_Rubric_Writing`,
  `11_AllFail_Analysis`, `12_Difficulty`) must resolve `Universe_<P>/<P>_HarmonyGames_*` and must not
  cite the retired top-level folders. Scenario censuses and "collection is complete" claims must be
  re-derived for the chosen universe; no count may be carried over from the old bundle.
- Severity: BLOCKING

### A-03 Synth-cut state: no shutdown, Victor departed, six storylines absent
- Files: `Eval-new/Evals/ENVIRONMENT.md:23-45` (OLD: `Evals/ENVIRONMENT.md:3-4`, `:111`);
  `Eval-new/Evals/1_Prompt_Eval.md:859` (OLD: `Evals/1_Prompt_Eval.md:141`)
- Category: universe-date
- Old → New: the only state rule was the Feb 2026 shutdown. Now: on Oct 1 "the February 2026 shutdown
  and its terminations have not happened, so the shutdown rules do not apply", a departed person is
  still gone (Victor Barnes, April 2025, last Slack 2025-04-15), and "Nothing after the cut exists
  yet, including six whole storylines" (Combo Fighter, Zombie Match Lite, Telegram Domino Delights
  port, UI sprite optimization sprint, Mattel Barbie idle life sim pitch, web distribution
  partnership).
- Authoring impact: `01_Scenario_Design` must exclude those six storylines and any post-cut artifact
  for Oct 1 tasks and must not build a shutdown/wind-down premise there; `01_Universe_Injection` must
  not seed post-cut entities; `08_Oracle_Event_Writing` must not expect post-cut records;
  `04_Prompt_Writing` must apply the premise check against the cut, not the shutdown.
- Severity: BLOCKING

### A-04 Per-task clock, Pacific dating, and dual PT/UTC day acceptance
- Files: `Eval-new/Evals/ENVIRONMENT.md:147-157`, `:169-176` (OLD: `Evals/ENVIRONMENT.md:111`);
  `Eval-new/Evals/1_Prompt_Eval.md:1076-1103` (OLD: `Evals/1_Prompt_Eval.md:150`);
  `Eval-new/Evals/3_Rubrics_Eval.md:423` (OLD: `Evals/3_Rubrics_Eval.md:406`);
  `Eval-new/Evals/WORKFLOW.md:476-483` (OLD: `Evals/WORKFLOW.md:476`)
- Category: universe-date
- Old → New: one fixed clock (2026-02-14 00:00 UTC) becomes the task's clock. "Tools show UTC, but
  people in the story use Pacific time"; "Write dates in Pacific time"; "If the Pacific date and the
  UTC date are different, accept either. Checks against the clock itself stay in UTC." Persona text
  "today" is Saturday, February 14, 2026 (Feb 14 tasks) or Wednesday, October 1, 2025 (Oct 1 tasks).
- Authoring impact: `04_Prompt_Writing` and `05_Human_Time_Estimate` must use PT dates and the
  task's "today"/"yesterday"; `09_Rubric_Writing` must let any date-day row accept both days
  (`comparison: pt_or_utc_date`) instead of locking one; `08_Oracle_Event_Writing` must resolve dates
  against the task clock; `01_Universe_Injection` must treat unzoned persona-written times as PT.
- Severity: BLOCKING

### A-05 Event timestamps must be at or before the clock
- Files: `Eval-new/Evals/ENVIRONMENT.md:159-167`; `Eval-new/Evals/0_Injection_Quality_Eval.md:229-232`
  (OLD: `Evals/0_Injection_Quality_Eval.md:180-184`); `Eval-new/claude/skills/injection/SKILL.md:99-102`
- Category: injection
- Old → New: previously only "Future deadlines and scheduled events are valid when represented as
  future". Now "Event timestamps (created, sent, posted, commented, modified, dateLastActivity,
  action date) must be at or before the clock. Only plan fields (due, scheduled start/end, deadline)
  may be later. Calling a record 'scheduled' does not exempt its event timestamps."
- Authoring impact: `01_Universe_Injection` must date every created/updated/sent/comment timestamp at
  or before the cut, and may only push due/start/end/deadline into the future; a "scheduled" story
  device no longer licenses a future event timestamp.
- Severity: BLOCKING

### A-06 Grader-facing text and count-padding comments in SQL are FAIL
- Files: `Eval-new/Evals/0_Injection_Quality_Eval.md:44-51`, `:77-80`
  (OLD: `Evals/0_Injection_Quality_Eval.md:44-47`, `:72-75`)
- Category: injection
- Old → New: answer-leakage and "writing style" were outside scope. Now "Grader-facing text is in
  scope: injected text addressed to a solver or grader, or describing the test (for example 'This
  description does not state them.'), is FAIL under Check C". Also: "A comment or record added to
  raise tool-call counts or lower the pass rate is FAIL; each record it covers needs a task purpose
  or removal."
- Authoring impact: `01_Universe_Injection` must scrub solver/grader-addressed prose and meta
  comments from records and SQL; `03_Error_Async_Config` must not add filler records/fields to inflate
  calls or depress the pass rate — friction must be modelled inside existing records with a purpose.
- Severity: BLOCKING

### A-07 Mandatory `hg_injection_lint.py` with a fixed flag taxonomy
- Files: `Eval-new/Evals/0_Injection_Quality_Eval.md:106`, `:114-123`, `:266-270`
  (OLD: `Evals/0_Injection_Quality_Eval.md:98-101`); `Eval-new/Evals/EXECUTION.md:120-124`;
  `Eval-new/claude/skills/injection/SKILL.md:72-77`
- Category: tooling-cli
- Old → New: no lint existed. Now it runs once per saved SQL version before record checks; FAIL flags
  `future_date, id_contract, drive_unreadable, duplicate_account, actor_name, generated_column,
  text_time_format, missing_required`; CHECK flags `unknown_actor, grader_language, padding_comment`;
  INFO for unevaluable items. "A clean lint is not a PASS: checks A–C still apply in full."
- Authoring impact: `01_Universe_Injection` must run the new lint from the new bundle and record each
  flag's resolution before declaring the injection done; its own `tools/sql_lint.py`,
  `base_check.py` and `hardness_gate.py` do not cover these flags.
- Severity: BLOCKING

### A-08 Injected Drive files must be readable content
- Files: `Eval-new/Evals/0_Injection_Quality_Eval.md:153-158`
  (OLD: `Evals/0_Injection_Quality_Eval.md:137-140`; no equivalent rule)
- Category: injection
- Old → New: new rule. A Google Doc needs a `docs_documents` row and non-empty `body_text`; a file
  (PDF included) needs `content_path` pointing at real bytes in the base path format. "A file with
  null content_path and empty content_text is FAIL. content_text alone is not served by Drive reads."
  Media/binary records are metadata-only and fail only when their content is needed.
- Authoring impact: `01_Universe_Injection` must add the docs row and/or `content_path` bytes for
  every Drive file a task relies on; `02_Reference_Files` must ensure attached/derived files land
  where the persona's Drive read serves content, not name-only metadata.
- Severity: BLOCKING

### A-09 One account per person, and listed ID contracts
- Files: `Eval-new/Evals/0_Injection_Quality_Eval.md:159-162`, `:170-175`
  (OLD: `Evals/0_Injection_Quality_Eval.md:137-140`)
- Category: injection
- Old → New: previously only "Preserve exact existing service IDs … a numbering gap … is not an
  invalid-ID finding". Now "One person, one account per service … A second account for an existing
  person is FAIL unless the records show two different people with the same name"; contracts live in
  `Evals/references/schema/id_contracts.json` (Gmail `history_id` NULL or decimal string; Drive
  `content_path` is `<owner_email>/<path>` with no `root/` prefix); the numbering-gap leniency applies
  only to unlisted fields.
- Authoring impact: `01_Universe_Injection` must reuse an existing account row rather than insert a
  second one, must derive Drive paths from the owner email without a `root/` prefix, and must check
  new IDs against `id_contracts.json`; `01_Scenario_Design` must not design a "second address" or
  duplicate-mailbox device.
- Severity: BLOCKING

### A-10 Generated FTS columns must not be written
- Files: `Eval-new/Evals/0_Injection_Quality_Eval.md:184-190` (no OLD equivalent)
- Category: injection
- Old → New: `slack.slack_messages.text_fts` and `gmail.gmail_messages.body_text_fts` are generated
  (`"generated": "always"`). "any INSERT or UPDATE that sets them to anything but `DEFAULT` is
  rejected by the platform ('can only be updated to DEFAULT') and can roll back the whole script".
  This is a Check B FAIL.
- Authoring impact: `01_Universe_Injection` must omit both columns from every insert/update (and
  therefore from its generated SQL templates); a script that names them can fail wholesale.
- Severity: BLOCKING

### A-11 Linear text dates and NOT NULL columns
- Files: `Eval-new/Evals/0_Injection_Quality_Eval.md:191-197` (no OLD equivalent)
- Category: injection
- Old → New: Linear dates are text and must use `YYYY-MM-DDTHH:MM:SSZ` (dates `YYYY-MM-DD`); offsets,
  milliseconds, `::timestamptz`/`CAST` or `now()` store a form the agent's load cannot parse and
  "every run then fails at load-universe". New issues must also set
  `linear.linear_issues.state_history_json` (`'[]'`).
- Authoring impact: `01_Universe_Injection` must emit plain `Z`-suffixed strings in `*_at`/`due_date`/
  `start_date`/`target_date` and fill every NOT NULL no-default column (notably
  `state_history_json`); `03_Error_Async_Config` timestamps in Linear inherit the same constraint.
- Severity: BLOCKING

### A-12 Staged typos fail; clean typing is fine
- Files: `Eval-new/Evals/1_Prompt_Eval.md:102`, `:434-438`, `:886`, `:1003`
  (OLD: `Evals/1_Prompt_Eval.md:120`, `:426`, `:857`, `:974`)
- Category: prompt
- Old → New: the "perfectly capitalised and punctuated throughout" red flag and the
  "real people type fast and unproofread" framing are gone; the prompt is now "a plain natural
  request: readable, not polished into a document, not roughed up on purpose". New red flag:
  "Staged errors: misspellings, made-up emoji or broken punctuation a person typing normally would
  not leave" (calibration: #11, 11 misspellings in ~120 words).
- Authoring impact: `04_Prompt_Writing` must write correct, natural prose and must stop injecting
  typos/emoji/ragged punctuation to sound human; a prompt-writing brief that prescribes "add small
  typos" must be removed. Clean spelling raises no flag.
- Severity: BLOCKING

### A-13 Trap hints and riddles fail Contrived
- Files: `Eval-new/Evals/1_Prompt_Eval.md:103`, `:1004`, `:1007-1019`, `:1066-1067`
  (OLD: `Evals/1_Prompt_Eval.md:996-998`)
- Category: prompt
- Old → New: "Hidden root causes" was an unqualified good indicator and a riddle was explicitly not
  contrived. Now "A riddle or hint aimed at the trap fails Contrived. Naming the symptom is fine",
  and the good indicator reads "Hidden root causes the prompt does not hint at". #31 fails on
  "I have a nagging feeling the thing that actually bites us is not on anybody's list".
- Authoring impact: `04_Prompt_Writing` must state the symptom only and never foreshadow the trap or
  the discovery order; `01_Scenario_Design` must not write prompt-facing hint lines into the design's
  prompt sketch; `09_Rubric_Writing` must not grade an unstated hint.
- Severity: BLOCKING

### A-14 Hidden destinations fail when the persona would know them
- Files: `Eval-new/Evals/1_Prompt_Eval.md:1005`, `:1013-1019`, `:581`
  (OLD: `Evals/1_Prompt_Eval.md:575`)
- Category: prompt
- Old → New: the Ambiguity dimension used to invite leaving "destinations" to the environment. Now
  "Where the output goes is named when the persona would know it." It may be left to the data only
  when finding it is the task, and then "each place must be findable from a record the persona can
  see". #42, #47 and #44 fail (`"wherever that's actually been asked for"`).
- Authoring impact: `04_Prompt_Writing` must name the channel/doc/thread/ticket when the persona would
  know it; `01_Scenario_Design` may keep a hidden destination only as an explicit discovery ask with
  a planted, persona-visible record naming the place; `09_Rubric_Writing` rows may then grade that
  destination.
- Severity: BLOCKING

### A-15 Audit forms and if-chains fail on their own
- Files: `Eval-new/Evals/1_Prompt_Eval.md:1032-1046`, `:1007`, `:1078-1080`
  (OLD: `Evals/1_Prompt_Eval.md:976` spec-sheet rule only)
- Category: prompt
- Old → New: the spec-sheet gate still needs two triggers, but two new flags fail singly: "Reads like
  an audit or compliance form, not a person asking for help" (#1, #43) and "Long chains of if /
  but-not / then-also clauses dictating what the Agent does per case" (#44). "A per-case rule belongs
  in a seeded record, not in the prompt."
- Authoring impact: `04_Prompt_Writing` must avoid deliverable-catalogue verbs ("reconcile …,
  classify …, rank …, complete the review artifacts and handoff it requires") and conditional
  per-case instructions; `01_Universe_Injection` must host per-case rules as seeded records instead;
  `09_Rubric_Writing` must not expect those rules to be in the prompt.
- Severity: BLOCKING

### A-16 Overly Broad rises to Major
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:33`, `:102`, `:371`, `:711-712`
  (OLD: `Evals/3_Rubrics_Eval.md:33`, `:196`, `:362`, `:686`)
- Category: rubric
- Old → New: `overly_broad` moves from the Moderate table to Major "the same level as Overly
  Specific", in the local-override table, the 2.7 hard gate, the scope-qualifier rule (was Moderate
  unless only evidence stated the exclusion) and the summary table. Repair instruction: "Never repair
  an overly broad row with a count, format or phrasing; name the value."
- Authoring impact: `09_Rubric_Writing` must tighten every title against plausible wrong answers
  (this is now a Major tally issue), may not fix breadth by adding counts/format, and must name the
  exact value/scope; `create-rubric-writing` weight/severity guidance must treat it as Major.
- Severity: BLOCKING

### A-17 Do-nothing test: a row an agent passes by doing nothing fails
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:34`, `:204-210`, `:392-402`, `:707-708`
  (OLD: `Evals/3_Rubrics_Eval.md:34`, `:197-199`, `:693`)
- Category: rubric
- Old → New: previously "The Agent does not close ENG-123" became "leaves ENG-123 open". Now a row
  passes Negative Criteria only if "an Agent that makes no writes and gives no answer" fails it;
  "leaves … as found / as is / unchanged / untouched / open / off", "keeps … off" are flagged, and the
  exclusion must be covered "as a condition on a write the Agent must make (an exact count or scope),
  or a requirement inside a required artifact".
- Authoring impact: `09_Rubric_Writing` must stop writing preservation/absence rows (including the
  formerly recommended "leaves X open" form), fold every exclusion into a required write or artifact,
  and drop exclusions nobody asked about; `01_Scenario_Design` should not design decoys that only a
  negative row could grade.
- Severity: BLOCKING

### A-18 Format-5 record with `valid_case`, `do_nothing_case` and final-reply test
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:11`, `:88`, `:578` (OLD: `Evals/3_Rubrics_Eval.md:11`,
  `:86`, `:560`); `Eval-new/Evals/WORKFLOW.md:723`, `:940` (OLD: `Evals/WORKFLOW.md:717`, `:933`);
  `Eval-new/claude/skills/rubric/SKILL.md:90`
- Category: rubric
- Old → New: format 4 → "Scoring record format 5"; every `checks.rows` entry gains a `valid_case`
  ("a prompt-allowed answer the row must ACCEPT"; a REJECT forces `overly_specific` or `incorrect`),
  a `do_nothing_case` that must REJECT, plus `checks.final_reply_test`, `oe_cross_check` and
  `alternative_review`.
- Authoring impact: `09_Rubric_Writing` must produce rows that survive all three tests by
  construction: an accepted valid alternative, a required write/artifact that a do-nothing run fails,
  and a concise final reply that passes. The authoring rubric plan should carry these three fields per
  row.
- Severity: BLOCKING

### A-19 Rubric ↔ OE cross-check is two-way and OE is a required input
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:47`, `:146`, `:453-454`
  (OLD: `Evals/3_Rubrics_Eval.md:147`, `:436`); `Eval-new/claude/skills/rubric/SKILL.md:30-33`
  (OLD: `claude/skills/rubric/SKILL.md:27-29`)
- Category: rubric
- Old → New: OE was "Optional reference path". Now it is "Required when the task has OEs"; every row
  maps back to OE steps (`oe_cross_check.rows[].oe_step_ids`, labels exactly as in the saved OE); an
  unreached row is `oe_unmapped` with `ROW_DEFECT` / `OE_GAP` / `UNRESOLVED`; a row that fails an
  agent following the OE is a conflict settled `FIX_ROW` or `FIX_OE`. The OE eval stays blind to the
  rubric, and an OE edit makes the rubric review stale.
- Authoring impact: `08_Oracle_Event_Writing` must include a step for every record a rubric row will
  grade (otherwise the rubric review records `OE_GAP`); `09_Rubric_Writing` must cite OE step labels
  exactly and must not grade off-path records; `01a_Hardening` must expect rubric reviews to go stale
  after any OE change.
- Severity: BLOCKING

### A-20 Reachable evidence: no Trash-only, attachment-only or unlinked record
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:329` (no OLD equivalent)
- Category: rubric
- Old → New: new rule. The deciding record must be (a) outside Gmail Trash/Spam, (b) readable as
  content (not only an attachment name; Gmail/Slack serve attachment metadata only), and (c) reachable
  from a prompt noun. Otherwise the row is `unobservable` (Major), and `checks.sources` records
  `reachability` (`PROMPT_LINKED` / `TRASH` / `ATTACHMENT_ONLY` / `UNLINKED`).
- Authoring impact: `01_Universe_Injection` and `02_Reference_Files` must place every graded fact on a
  prompt-linked, content-readable, non-Trash record and must not hide a needed value only inside an
  attachment; `09_Rubric_Writing` must cite the carrying record.
- Severity: BLOCKING

### A-21 Count and format locks are over-specific
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:350`, `:95` (no OLD equivalent in 2.7)
- Category: rubric
- Old → New: new rule. "A length, line, sentence or section count is a format. Grade one only when
  the prompt states the count; 'keep it short' grades no count." The lint flags `format_lock`
  ("5 lines", "at most 3", "one sentence per line"); calibration task df2ec.
- Authoring impact: `09_Rubric_Writing` must not grade a count/format the prompt did not state; if the
  design wants a graded length, `04_Prompt_Writing` must state it explicitly (which then risks the
  spec-sheet register gate).
- Severity: BLOCKING

### A-22 LITERAL binding of event keys and anonymized tokens; evidence names the record
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:310`, `:413`, `:95`; `Eval-new/Evals/2_Oracle_Events_Eval.md:495`
  (OLD: `Evals/3_Rubrics_Eval.md:318` had prose dates only; no "cited record" rule)
- Category: rubric
- Old → New: evidence must name the record holding each expected value; names, emails, IDs, statuses
  and event keys bind as LITERAL (SEMANTIC only for conclusions); ID-shaped title tokens and
  anonymized tokens each need a LITERAL claim; the lint flags `evidence_no_record` and `anon_token`
  (a row naming "HOMA" where the roster shows `[PERSON_NAME_0854]` rejects a valid answer).
- Authoring impact: `09_Rubric_Writing` must quote the live key (`quest_completed`, not
  `quest_completion`), cite the carrying record in `evidence`, and accept every rendering the tools
  return (prefix, case, repo-qualified, short SHA, anonymized token).
- Severity: IMPORTANT

### A-23 OE `expected_values` ledger and absence claims
- Files: `Eval-new/Evals/2_Oracle_Events_Eval.md:57`, `:264-266`, `:381`, `:495-496`
  (OLD: `Evals/2_Oracle_Events_Eval.md:57`, `:262`, `:377`, `:490`)
- Category: oracle-events
- Old → New: the Expected-data sign-off table gains a ledger: "Record every value on an Expected line
  with a quote, or mark it not_a_claim. An absence claim … needs a scope-bound evidence_check"; the
  Expected line is defined (`Expected:` label, else "The agent finds …"); an uncovered value leaves
  the review PARTIAL. New FAIL rows: wrong event name/field value/ID and a refuted absence claim.
- Authoring impact: `08_Oracle_Event_Writing` must label every `Expected:` line, quote values
  character for character from the record (not from declarations), mark narrative values
  `not_a_claim`, and back any "none/no/never" with a scoped search. Calibration: `quest_completed`
  vs `quest_completion`; CodeRabbit "✅ Addressed in commit 77cf03f".
- Severity: BLOCKING

### A-24 BOTH_FAIR_FIGURE: one narrow UGT exception
- Files: `Eval-new/Evals/1_Prompt_Eval.md:104`, `:666-688`, `:1479-1486`
  (OLD: `Evals/1_Prompt_Eval.md:656-662`); `Eval-new/claude/skills/prompt/SKILL.md:138-145`, `:283-285`;
  `Eval-new/Evals/README.md:18-30`
- Category: prompt
- Old → New: previously any materially incompatible pair failed UGT. New PASS (5) applies only when
  all five hold: same decision/writes/destinations/recipients and only one reported figure differs;
  each value on a persona-visible record; no check settles it; each reading completes every ask; the
  figure does not change the next action. Record `BOTH_FAIR_FIGURE` with both quotes (leading first)
  and the generated section prints "Rubric must accept: X or Y"; not re-scored under Clarity.
- Authoring impact: `04_Prompt_Writing` may leave exactly one reported figure genuinely ambiguous only
  under those five conditions and must surface "Rubric must accept: X or Y"; `09_Rubric_Writing` and
  `12_Difficulty` must treat that fork as intended, not a defect. Not a general licence: a
  file-now-versus-defer fork is not a figure, and a newer source still settles (#49).
- Severity: IMPORTANT

### A-25 Rubric must accept both-fair values
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:46`, `:244` (no OLD equivalent)
- Category: rubric
- Old → New: new local-override row. Each `BOTH_FAIR_FIGURE` in the saved prompt report is "a
  required alternative: a row that grades that figure must accept either value, or it is
  `overly_specific`", recorded as a SUPPORTED `checks.alternative_review` branch.
- Authoring impact: `09_Rubric_Writing` must, whenever it authors an ambiguity around one figure, make
  the graded row accept both values; a single-value row is a Major defect.
- Severity: IMPORTANT

### A-26 State-premise checks expanded to company/people state
- Files: `Eval-new/Evals/1_Prompt_Eval.md:145`, `:859`, `:1490`
  (OLD: `Evals/1_Prompt_Eval.md:141`, `:834`, `:1404`)
- Category: prompt
- Old → New: the premise list adds "business as usual after the Feb 11 shutdown on a Feb 14 task, a
  departed person still acting, anything that does not exist yet on an Oct 1 task"; the mistakes
  table adds the same. Calibration #43 fails because Victor, gone since April 2025, holds a current
  handoff control.
- Authoring impact: `04_Prompt_Writing` must check every actor is active at the cut and every object
  exists by then; `01_Scenario_Design` must not cast a departed persona (Victor) in an Oct 1 task;
  `02_Reference_Files` and `08_Oracle_Event_Writing` inherit the same check.
- Severity: BLOCKING

### A-27 Voice match is judged against the role only
- Files: `Eval-new/Evals/1_Prompt_Eval.md:379` (OLD: `Evals/1_Prompt_Eval.md:375`)
- Category: prompt
- Old → New: "judge against the role and the persona's own messages in the Slack and Gmail exports"
  becomes "Judge against the role only; the persona's own Slack or mail style is not a standard."
- Authoring impact: `04_Prompt_Writing` no longer needs to imitate the persona's historical message
  style, and style-matching is no longer a defence; no rubric row may require persona-style mimicry.
- Severity: MINOR

### A-28 Every report carries a `Clock:` line and the universe-specific manifest path
- Files: `Eval-new/Evals/WORKFLOW.md:773-775` (OLD: `Evals/WORKFLOW.md:767`);
  `Eval-new/Evals/INPUTS.md:37`; e.g. `Eval-new/claude/skills/prompt/SKILL.md:20-23`;
  `Eval-new/Evals/1A_Hardness_Eval.md:228` (OLD: `Evals/1A_Hardness_Eval.md:228`)
- Category: report-format
- Old → New: reports referenced `Evals/references/universe_manifest.json`; now "the task universe's
  `references/universes/<normal|synthcut>/universe_manifest.json`" plus "show the task date in the
  report's `Clock:` line", copied from `universe_intake.report_line`.
- Authoring impact: `01a_Hardening`, `11_AllFail_Analysis` and `12_Difficulty` must keep the `Clock:`
  line when quoting or archiving eval reports, and must not point provenance at the retired manifest
  path.
- Severity: IMPORTANT

### A-29 Prepared indexes moved under `references/universes/`
- Files: `Eval-new/Evals/SEARCH.md:223`, `:287-289` (OLD: `Evals/SEARCH.md:223`, `:287-288`);
  `Eval-new/Evals/README.md:174` (OLD: `Evals/README.md:147`);
  `Eval-new/claude/CLAUDE.md:51`, `:65` (OLD: `claude/CLAUDE.md:42`, `:52`)
- Category: tooling-cli
- Old → New: package `Evals/references/search_indexes/` + `Evals/references/id_indexes/`; now package
  `Evals/references/universes/` (each universe's `search_indexes/` and `id_indexes/` with manifests).
- Authoring impact: none for content; any creation-side wrapper or packaging script that hardcodes
  `Evals/references/search_indexes/` or `id_indexes/` will break.
- Severity: MINOR

### A-30 Storyline counts and the "today is Feb 28, 2026" override
- Files: `Eval-new/Evals/Docs/README.md:12`, `:29-34`, `:41` (OLD: `Evals/Docs/README.md:12`, `:26-29`, `:38`)
- Category: universe-date
- Old → New: "80 source scenarios" becomes 76 (Feb 14) / 70 (Oct 1); a new paragraph states that QC
  rating-form row 128 and the spec's Audit Workflow note still say "today" is February 28, 2026, and
  that the task clock wins (Feb 14, 2026 / Oct 1, 2025).
- Authoring impact: `01_Scenario_Design` storyline census must use 76/70, not 80; `04_Prompt_Writing`
  must ignore the Feb 28 date in the QC form; no authored document may cite 80 scenarios.
- Severity: MINOR

### A-31 Release package renamed `prompt-ugt-v1` → `task-quality-v1`
- Files: `Eval-new/Evals/WORKFLOW.md:598` (OLD: `Evals/WORKFLOW.md:592`);
  `Eval-new/claude/skills/prompt/SKILL.md:125` (OLD: `claude/skills/prompt/SKILL.md:125`);
  `Eval-new/Evals/README.md:18`
- Category: scoring-thresholds
- Old → New: prompt records verify "the shared `task-quality-v1` package" instead of
  `prompt-ugt-v1`; older records "keep their release and need a fresh review".
- Authoring impact: `04_Prompt_Writing` and any authoring report that binds a prompt release
  fingerprint (via `hg_eval_release.py snapshot prompt`) must expect `task-quality-v1`; cached
  `prompt-ugt-v1` results are historical and cannot be reused.
- Severity: IMPORTANT

### A-32 Rubric lint gains four mandatory flag families
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:95`, `:392-393`, `:310`, `:350`
  (OLD: `Evals/3_Rubrics_Eval.md:93`)
- Category: tooling-cli
- Old → New: the code-check step previously recorded `vague_exemplar/tool_name/schema/prohibition`
  hits; it now also requires resolving every `disguised_negative`, `format_lock`, `anon_token` and
  `evidence_no_record` hit.
- Authoring impact: `09_Rubric_Writing` should run the new `hg_rubric_lint.py` against its draft rubric
  and clear those four families before producing `09_Rubrics.json`.
- Severity: IMPORTANT

### A-33 Prose dates with a year can bind as `DATE`
- Files: `Eval-new/Evals/3_Rubrics_Eval.md:323` (OLD: `Evals/3_Rubrics_Eval.md:318`)
- Category: rubric
- Old → New: a `DATE` claim previously had to quote an ISO date; now "an ISO date or a prose date with
  month name, day and four-digit year ('July 7, 2025')". A yearless prose date ("Nov 16") still cannot
  bind and needs day/year `NUMBER` projections.
- Authoring impact: `09_Rubric_Writing` needs fewer extracts for prose-dated rows but must still avoid
  yearless dates in titles; no change to `04_Prompt_Writing`.
- Severity: MINOR

### A-34 `universe` occupies the `02_` input slot
- Files: `Eval-new/Evals/INPUTS.md:161` (OLD: `Evals/INPUTS.md:129-140`, no universe row)
- Category: inputs-process
- Old → New: the saved-input table inserts `universe` → `02_Universe_Date.txt` between `injection`
  (`01_`) and `error-async` (`03_`); `save`, `list` and the `universe` command share the store.
- Authoring impact: the creation pipeline must keep `02_Universe_Date.txt` distinct from its own
  `02_Reference_Files` artifact naming, must save the date under key `universe`, and must not renumber
  existing keys; `02_Reference_Files` continues to live as eval `attachments/reference/<id>/`.
- Severity: MINOR

## Unchanged / cosmetic-only files

Byte-identical (verified with `cmp`):

- `Evals/1B_Haiku_Prediction_Eval.md` = `Eval-new/Evals/1B_Haiku_Prediction_Eval.md`
- `Evals/2_Golden_Response_Eval.md` = `Eval-new/Evals/2_Golden_Response_Eval.md`
- `Evals/Authoring_Workflow.md` = `Eval-new/Evals/Authoring_Workflow.md`
- `claude/install.py` = `Eval-new/claude/install.py`
- All `Evals/Docs/` binaries (`QC_Rating_Form_V12.csv`, `QC_Centralized_Spec_Doc.xlsx`, all eight
  guideline PDFs, `Unique_Ground_Truth.pdf`) are identical; only `Evals/Docs/README.md` changed.

Cosmetic / no behavioural change:

- `Evals/1A_Hardness_Eval.md` — one path sentence only (`1A:228`), covered by A-28.
- `claude/skills/hardness/SKILL.md` — date-first block only (`:13-21`), covered by A-01.
- `Evals/SEARCH.md` — packaging paths only (`:223`, `:287-289`), covered by A-29.
- `Evals/EXECUTION.md` — step renumbering plus the date step and the lint line (`:20-25`, `:120-124`),
  covered by A-01 and A-07.
- `Evals/README.md` / `claude/README.md` — the two release headers (`dual-universe-v1`,
  `task-quality-v1`) are summaries of A-01…A-26; no independent rule.
- `claude/UNIVERSE_MAP.md` — folder description only, covered by A-02.
