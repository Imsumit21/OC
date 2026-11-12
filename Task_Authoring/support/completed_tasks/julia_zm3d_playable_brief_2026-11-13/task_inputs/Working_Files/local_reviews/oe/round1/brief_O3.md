# LOCAL REHEARSAL — not a platform verdict

Blind pass O3 (Open-instruction inventory) · stage oe (/oe) · round 1 · scope full

You are a fresh, blind reviewer running one pass of the platform's deep recheck, rehearsed locally. This brief is your whole context: you have not seen the main review, any earlier round, any other pass's findings, the author's design, notes or check reports, and you must not look for them. You save no file, edit nothing and never execute SQL.

## What you may open (and nothing else)

- this brief;
- the inputs listed below (copies made for this round):
  - `Task_Authoring/task_inputs/Working_Files/local_reviews/oe/round1/inputs/00_Task_Details.txt` (sha256 ed790e3e48b6)
  - `Task_Authoring/task_inputs/Working_Files/local_reviews/oe/round1/inputs/01_Universe_Inject.sql` (sha256 78465cd474f8)
  - `Task_Authoring/task_inputs/Working_Files/local_reviews/oe/round1/inputs/04_Prompt.txt` (sha256 33c721d60945)
  (this pass is not given the Oracle Events: do not open any OE file)
- reference files the platform also gives this pass: `Evals/references/rules/deep_recheck.md`, `Evals/references/rules/common_errors.md`, `Evals/SEARCH.md`, `Evals/references/persona/`;
- the universe, only through the commands under Universe.

Never open anything else: no other file in `Task_Authoring/task_inputs/` (its Working_Files/, eval_reports/, other rounds or passes under `Working_Files/local_reviews/`), no other task folder, nothing under Task_Authoring/support/ except your own scratch files, Task_Authoring/archived_tasks/, the Evals input store (the task_inputs folder under Evals/) or any memory or notes file.

## Task details (the assignment as the platform saves it)

```text
🏢 Business Function
Product

🧑 Persona
Julia Lawson
Role: Product Manager

🎯 Competency
Marketing and GTM

🛠️ Task Skill
Authoring

📋 Task Type
long-horizon

🎚️ Difficulty Mode
hard

📅 Universe Date
October 1, 2025 07:00
```

Clock: 2025-10-01 00:00 PT (synth-cut universe, task date Oct 1, 2025).
Persona key for persona_view.py: `julia_lawson`.

## Injection

Injection SQL: the `01_Universe_Inject.sql` copy under the inputs above (sha256 78465cd474f8).

Friction (error and wait configuration): none.

## Universe

Run these from the workspace root (the folder that holds Evals/ and Task_Authoring/). They read the task's universe
as the platform tools would; they never write into Evals/:

    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search inventory
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search search <service> "<terms>" --limit 20
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search search-many --request <queries.json> --compact
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search get <service> --file <file> --pointer <pointer>
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search get-many --request <reads.json> --compact
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search lookup <service> --ids-file <ids.json> --file '<glob>'
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs records --request <checks.json>
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs reference routes <service>
    python3 Task_Authoring/tools/persona_view.py --task-dir Task_Authoring/task_inputs can-see julia_lawson <service> <id>
    python3 Task_Authoring/tools/persona_view.py --task-dir Task_Authoring/task_inputs search julia_lawson <service> "<query>"

Where a text below says `python3 Evals/tools/hg_search.py <args>` (or hg_records.py, hg_reference.py), run
`python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search <args>` (or `records`, `reference`) instead; never run
a helper under Evals/tools/ directly. persona_view.py applies this persona's read access (Evals/references/persona/
acl.md) to Gmail, Slack, Calendar and the Drive family. Put any request file you write under
Task_Authoring/support/scratch/ and delete it when you are done.
Base search does not show injected rows: the injection rows are in the SQL copy under Inputs. Read it as text, a proposed overlay on base; never execute it.

## The artifact under review

Not given to this pass (deep_recheck.md: O3 is not given the OE file or any OE text).

## Platform pass text (verbatim from the local Evals/ copy)

### Evals/references/rules/deep_recheck.md:61-67 (sha256 218dca42c269)

**Pass inputs.** Each pass gets the saved task inputs (`Evals/task_inputs/`
except `reports/`), the universe exports through `Evals/tools/hg_search.py` and
`Evals/SEARCH.md`, `Evals/references/persona/`, `common_errors.md`, and this
file. It is told its pass ID. Pass O3 is also not given `08_Oracle_Events.md` or any OE text. It does not open `Evals/task_inputs/reports/`
(including `drafts/`) or any earlier report, chat summary or record. It never
executes SQL. It is not given the main session's findings, scores or verdict,
or another pass's findings.

### Evals/references/rules/deep_recheck.md:69-88 (sha256 d79ba0d0bd9c)

**Known platform defects.** These are not contributor defects. A pass that
finds one reports it with the tag `PLATFORM:<id>`. The main session records it
in the report and never scores it against the task:

- `FD-2880`: the GitHub export's `commits` lists are a subset. A commit that
  is in git history or `commit_map` but missing from `commits` is an export
  gap, not a coherence or accuracy defect.
- `FD-3785`: the synthetic Snowflake rollups (DAILY_ACTIVE_USERS retention
  columns, USER_COHORT_RETENTION immature cells) disagree with their own
  definitions, and `analytics.game_events` is not in the injection database.
  A finding that rests only on these cells is platform. A prompt that makes
  the answer depend on them still fails UGT, because the agent cannot get one
  answer; the fix is to steer the prompt to a source that is consistent.
- Slack paste artifacts in saved SQL or text: markdown auto-link wrappers,
  doubled `""` from a CSV paste, missing `$$` and stripped `*`. Report the
  file as unreadable as sent; do not score the task content on them.
- Anonymized tokens such as `[PERSON_NAME_0854]` are the source string. A row
  or answer that uses the token as shown is correct; the real name is correct
  only when a persona-visible record maps the token to it. Do not score a
  token-for-name difference as a factual or accuracy defect.

### Evals/references/rules/deep_recheck.md:90-96 (sha256 4a6e18950546)

**Pass work.** A pass checks only its own topic, on every sentence, event or
row, not a sample. It returns findings in this format and nothing else:

`DR# | pass | checklist section | quoted prompt sentence, OE text (OE#) or rubric row (R#) | record path, id and quoted value | Eval dimension or issue type | proposed score or severity`

A finding without a quote is dropped. A pass with no findings returns `none`
and the number of sentences, events or rows it checked.

### Evals/references/rules/deep_recheck.md:287-289 (sha256 4a49e5d188fa)

Each OE pass reads the prompt to know what the path must do. It follows Eval 2
route independence (§3.1): a step that reaches a requirement by another valid
route covers it.

### Evals/references/rules/deep_recheck.md:322-334 (sha256 9c350c270a6a)

### O3 · Open-instruction inventory

This pass is not given the OE file. It gets the prompt, the saved task inputs
other than OEs, and the universe. For every open instruction in the prompt
("fix whatever's wrong", "update anything stale", "make X match Y", "the code
wins", "clean up", "reconcile"), list every item it covers: compare the two
sources field by field and return a numbered list, one line per mismatch, with
both values quoted and their record paths. Count the list. Stop only when
every field of every record the instruction names has been compared; one
mismatch per document is not a full list.

Return `M# | instruction | source A record and value | source B record and value`.
With no open instruction, return `none` and the instruction count 0.

## Local differences from the platform

- The platform text asks for pipe-delimited lines (or `none` with a count). Return the same content as the JSON object under Required output instead.
- Where it names the saved task inputs, read the copies listed above; where it names the Evals search helpers, use the commands under Universe.
- Known platform defects: severity "PLATFORM", issue_type "PLATFORM:<id>"; they are not scored.

## Platform rules not in the local Evals/ copy

The platform has applied these rules in its own reports; the local pass text above does not have them. Apply them as well. `verbatim` means the excerpt quotes the platform's own rule; `reconstructed` means the rule is inferred from how the platform applied it, so use judgement. The excerpts come from other tasks' reports: they show how a rule is applied and say nothing about this task.

- `decision-forks-2.8` (reconstructed; local rule: absent): "Decision forks (2.8): `hg_decision_forks.py` found no hedge wording; no OE leaves a boundary item unsettled (the returned ***8605 wire, Oleg's returned wire, the Leapblock wire with no Processed notice and the JPMorgan own-account transfer are each settled by a dated record that names them)."
- `hg_decision_forks.py` (reconstructed; local rule: absent): "- Decision forks (2.8): `hg_decision_forks.py` finds no hedge wording."
- `tool_outputs.md@oe` (verbatim; local rule: absent): "| OE 30, 32, 33 | all | VERIFIED | Cataloged create / share tools; a created spreadsheet has a link (tool_outputs.md `gdrive.web_view_link`) |"

## Required output

Return one JSON object and nothing else. It carries the same content as the line format named in the platform text above, one finding per line you would have written:

```json
{
 "pass": "O3",
 "artifact_sha256": "5155af883d65cf9568446cb74e76a00e7c68ce494d63528695df28b2f7742106",
 "checked": "<how many items you checked>",
 "findings": [
  {
   "span": "<id>",
   "issue_type": "<type>",
   "severity": "<severity>",
   "quote": "<exact words copied from the cited item>",
   "evidence": "<source A record path, id and value | source B record path, id and value>",
   "fix": ""
  }
 ],
 "verdict": "PASS | NON-FAIL | FAIL"
}
```

- `artifact_sha256`: exactly `5155af883d65cf9568446cb74e76a00e7c68ce494d63528695df28b2f7742106` (the bytes listed under the artifact).
- `span`: prompt sentence ids S1..S3 (the open instruction's sentence).
- `quote`: the exact words of the cited item (a sentence, event or row). A finding without a quote is dropped.
- `issue_type`: "open_instruction_item" for every M# line (severity INVENTORY).
- `severity`: "INVENTORY" for each M# line; "PLATFORM" or "UNSURE" as below.
- `evidence`: the record path, id and quoted value behind the finding.
- `fix`: a plain description of the fix (it may be empty for an inventory line).
- `checked`: the number of sentences, events or rows you checked; required when `findings` is empty.
- `verdict`: PASS when you have no finding, FAIL when any finding is fail-level, else NON-FAIL.
