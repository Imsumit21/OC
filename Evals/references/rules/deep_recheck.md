# Deep Recheck

HarmonyGames · Adopted 2026-10-06. The last step of `/prompt` (Eval 1 Phase 5),
`/oe` (Eval 2 Phase 5) and `/rubric` (Eval 3 Phase 5.5). It replaces the single
blind common-errors reviewer.

Revision 2026-10-09 (retro of the 10-08/10-09 L0 rounds, `New_Evals_deepcheck_2026-10-09/retro/`):
P1 edge values, P2 hidden records / derived columns / date-slip severity, O1
qualifiers, new pass O3, the known platform defects list, the main-session
rejection and required-fix rules, and the fix-text check.

Each pass rechecks one of the fails our audits find most, on every prompt
sentence, every oracle event or every rubric row. Counts are failing tasks out
of 57 (`failing_audit_distribution.md`); one task can hit several topics.

| Pass | Stage | Topics and failing tasks |
|---|---|---|
| P1 | prompt | Unique Ground Truth 34, Clarity 23 |
| P2 | prompt | Cross-Service Coherence 8, Feasibility 5, Persona access 2, Data exists 2, Tool use and cross-service 2 |
| P3 | prompt | Truthfulness 5, Today's date 1 |
| P4 | prompt | Naturalness, tool names, step lists, named cause (Investigation 1) |
| O1 | oe | Accuracy 15 |
| O2 | oe | Completeness 5 |
| O3 | oe | Completeness from data: every item an open instruction covers (added 2026-10-09; 707 lost three rounds to it) |
| R1 | rubric | Overly specific 31 |
| R2 | rubric | Incorrect 26 |
| R3 | rubric | Missing outcome 20 |
| R4 | rubric | Duplicate 18 |
| R5 | rubric | Overly broad 16 |
| R6 | rubric | Not self-contained 11 |
| R7 | rubric | Not atomic 1 here; the QC team's top rubric fail (85 reviews in `common_errors.md` §7) |

Blank fields, tool names in titles, titles that do not start with "Agent" or "The Agent",
prohibition titles, and `such as` / `e.g.` / `for example` are checked by
`hg_rubric_qc.py`. No pass repeats them.

## Procedure

**Rubric run flow.** For `/rubric`, `references/rules/rubric_flow_v2.md` decides
the scope: in FULL mode R1–R7 run on every row alongside full reviewers F2/F3 (and once
more on the candidate rubric's changed rows to check the fixes) and
all findings are combined; in DELTA mode R1–R7 run on the target rows only (R4
compares them against all rows). Rubric findings are rejected only on the grounds
listed in `rubric_flow_v2.md`, not because the main session disagrees.

**Order.** The main stage finishes its phases and saves its record
(`prompt-checks`, `oe-review` or `rubric-score`). It does not save the report
yet. It then starts every pass for that stage at the same time, each as its own
fresh subagent on the stage's model. The report is saved once, after the main
session check below.

When the main stage stops as PARTIAL or BLOCKED for missing inputs, no pass
runs. The report still ends with `## Deep Recheck`, which says the recheck did
not run and why, followed by the verdict block.

**Pass inputs.** Each pass gets the saved task inputs (`Evals/task_inputs/`
except `reports/`), the universe exports through `Evals/tools/hg_search.py` and
`Evals/SEARCH.md`, `Evals/references/persona/`, `common_errors.md`, and this
file. It is told its pass ID. Pass O3 is also not given `08_Oracle_Events.md` or any OE text. It does not open `Evals/task_inputs/reports/`
(including `drafts/`) or any earlier report, chat summary or record. It never
executes SQL. It is not given the main session's findings, scores or verdict,
or another pass's findings.

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

**Pass work.** A pass checks only its own topic, on every sentence, event or
row, not a sample. It returns findings in this format and nothing else:

`DR# | pass | checklist section | quoted prompt sentence, OE text (OE#) or rubric row (R#) | record path, id and quoted value | Eval dimension or issue type | proposed score or severity`

A finding without a quote is dropped. A pass with no findings returns `none`
and the number of sentences, events or rows it checked.

**A pass that does not return.** A pass that crashes, times out, or returns no
finding list and no `none` with a count has not run. Start a fresh subagent for
that pass with the same instruction and inputs. Repeat until it returns a
usable result. Do not save the report while any pass is missing.

**Main-session check.** The pass is not trusted on its own.

1. Merge findings that cite the same sentence, event or row for the same issue,
   and keep every pass ID.
2. Open every cited record. Mark each finding CONFIRMED or REJECTED with a
   reason. "The pass said so" is not a reason.
   - A UGT finding (P1) can be REJECTED only by quoting a prompt sentence or
     a record the persona can open that rules out Reading B. An inference
     ("the agent would assume", "B is less likely") is not a reason and the
     finding stays CONFIRMED.
   - An Eval 0 advisory becomes a /prompt Cross-Service Coherence finding only
     when the record it names changes a value, set, order, recipient or
     destination the answer is graded on. Otherwise it stays an advisory in
     the Injection Gate section (for example an id-format or label-casing
     difference the answer never reads).
   - A mismatch on the O3 inventory that the records confirm is a required
     fix. It cannot be downgraded to optional or "nice to have"; when no OE
     covers it, it is a `MISSING` coverage entry.
3. Put each confirmed finding into the saved record under the existing rules:

| Stage | Where a confirmed finding goes |
|---|---|
| `/prompt` | Truthfulness → a premise `fact_review`; UGT → `unique_ground_truth`; any other dimension → `other_failures` |
| `/oe` | A wrong field → that step's result `INACCURATE`, or `MINOR` when it cannot change the outcome; a missing step → a `coverage` entry `MISSING`; a non-action or final-response event → its segment; a shape defect → `format_review` |
| `/rubric` | An `issues` entry with its type and severity, a `weight_reviews` change, or a `predicted_all_fail` entry |

4. Save the record again and let the helper recompute the score under the
   stage's existing thresholds and gates. A confirmed fail-level finding fails
   the stage.
5. Check the fix text. Every rewrite the report proposes (a prompt sentence,
   an SQL row, an OE with its `Expected:` line) gets the same check as the
   text it replaces: each value, id, branch, window and label is quoted from
   a record, it names every item it must cover, and it does not add a lock-in
   a valid answer would fail. A rewrite never uses "e.g.", "for example",
   "such as" or "etc."; it lists every item or points to the O3 group or fork
   that lists them. A rewrite that
   cannot be verified is replaced by a plain description of the defect and
   the records that show it, with no ready-to-paste wording.
6. Save the report.

## Report ending

The report holds the main review's phases, scoring table, issues and fixes,
with no verdict block among them. It ends with this section. The section's last
part is the report's only `### FINAL VERDICT` block, filled from the recomputed
record:

```markdown
## Deep Recheck

Passes: <pass IDs>, <model and effort>, each blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|

Effect on verdict: <unchanged, or which dimensions changed; scores are in the scoring table>

<for /prompt: the fork list, one line per confirmed or open UGT fork, all of them
in this round>
- F#: <outcome> | Reading A | Reading B | Settled by: <quoted record> / Missing: <the dated, persona-visible record or prompt sentence that would settle it>

<for /oe: the O3 inventory, one line per group>
- G#: <open instruction> | <document / tab> | <n> items (M#–M#) | Covered by: OE# / MISSING
Scope: <instructions covering more than 15 confirmed items, or none>

Platform defects: <PLATFORM:id lines, or none>

### FINAL VERDICT: <PASS / NON-FAIL / FAIL>
<the stage's standard verdict fields, then for /prompt the Lowest Dimension and Summary lines>
```

The pass table uses pass IDs, not topic names. The `Dimension / issue` cell holds
only the dimension or issue name, with no score, verdict word or digit, and the
next cell is the status. Scores live in the scoring table and the verdict block.
With no findings, write `None` under the findings table. A /prompt report
with no forks writes `Forks: none`. An /oe report whose prompt has no open
instruction writes `O3: no open instruction`.

## Prompt passes

### P1 · Unique ground truth and clarity

Fill section 2 of `common_errors.md` for every required outcome, not only the
main one. For each, write Reading A and the best Reading B a careful person
could defend. Compare the decision, the writes, the destination and the
contents. Settle each of these to one answer: which items are in the set,
which number or date, which source wins, what counts as the event, and what
gets written. If two answers fit and no prompt sentence or persona-visible
record kills one, that is a finding. "B is less likely" is not a kill.

**Edge values.** For every number, set, count or date the answer depends on,
compute it under each edge the prompt leaves open: cutoff day included or
excluded, a partial day or week, UTC vs the persona's local day, pooled vs
per-item or per-build, before vs after a later correction in the thread, and
records in a borderline status (In Review with `completed_at`, Trash vs
deleted). Quote the records behind each figure. If the answer changes at an
edge and no prompt sentence or persona-visible record picks one, that is a UGT
finding even when one definition seems standard.

**Every fork, once.** Report every fork in this one pass, not the first one
found. For each, name the record that settles it, or state what record is
missing. The report's fork list comes from this.

### P2 · Services, data and access

Fill section 3's two-services and hidden-record lines. Each named service must
change a graded fact; drop it and the answer must change. Every record the
answer needs must exist and be one this persona can open under
`Evals/references/persona/acl.md`. Check each explicit ask is doable, each
needed breakdown has a field in the data, and no Snowflake or Confluence record
contradicts itself (a closed ticket with later activity, line items that do not
sum).

**Hidden records are coherence.** When a record the answer needs is hidden
from the persona by another record (a `channel_leave` or missing membership
row, a file in another user's private folder, a mailbox that lacks the mail
its own recipients were sent), report it as Cross-Service Coherence, not only
as an access note. The data then disagrees with itself about what the persona
can know.

**Derived columns.** For every Snowflake table the answer reads, list each
derived column it uses (rates, retention, averages, rollups) and recompute one
value from its base rows. A column that does not match its definition is a
finding; tag it `PLATFORM:FD-3785` when it is one of the known rollups.

**Open-instruction scope.** An open instruction ("fix whatever's wrong in the
docs", "update anything stale") over sources that disagree in more than 15
places has no reachable end state for one run. Report it as Feasibility (and
Clarity when the covered documents are not named), with a count by document.

**Date-slip severity.** A wrong date or year in any record the answer relies
on (base or injected) is scored once, the same way every round: fail-level
when it changes an order, an effective date, a window or a count the answer
uses; otherwise one minor inconsistency (NON-FAIL).

### P3 · Truthfulness and clock

List every channel, ticket, vendor, person, amount, date and fiscal period the
prompt states. Open the record for each and quote it. One wrong tight claim is
a fail. One loose slip is also a fail. Nothing the prompt treats as already
done may sit after 2026-02-14 00:00 UTC. If injection SQL is saved, read it
(never run it): ids do not collide, columns exist, an added message's author is
in its channel, and apostrophes inside quoted strings are doubled.

### P4 · Wording

Run section 3's search hits and section 6.6. Look for catalog tool names, MCP
or "tool" wording, a first / then / finally list, a bolt-on sentence, an
opaque id or exact timestamp the task does not need, and a stated cause
(section 6.7). Then read it as the persona would type it. Spec-like or polished
LLM voice fails even when the situation is real (Eval 1 §1.2, §2.7).

## Oracle event passes

Each OE pass reads the prompt to know what the path must do. It follows Eval 2
route independence (§3.1): a step that reaches a requirement by another valid
route covers it.

### O1 · Accuracy

For every event, open the record behind each part and quote it: the service and
tool, each identifier and parameter (channel, ticket, card, recipient, filter,
date range), and every value in `Expected:`. Count lists yourself; "8 open
cards" is wrong if the list holds 16. A number must hold in the raw record and
in what the tool returns (Eval 2 §2.3A). Every read must be one this persona can
make under `acl.md`. A trap, rule or tie-break the event claims ("the bodies are
encoded", "a later reply wins", "spend divided by installs matches") must be in
a record; an invented trap is a wrong expected value. A write the records say a
person deferred is wrong (§2.6).

**Qualifiers.** A correct number with a wrong qualifier is wrong. For every
value, check what the OE says about it against the record: the time window
(lifetime vs a date range, "at the time it was quoted"), cohort or segment,
blended vs per-item, unit, branch or version, and the label or column it sits
under. "Same measured window" on lifetime figures, a commit cited from the
wrong branch, or "55 mins" under a label the source does not use are
`INACCURATE` when the result would differ. Severity: a wrong value that would change the
result is `INACCURATE`; a harmless imprecision is `MINOR`.

### O2 · Completeness

Split the prompt sentence by sentence into every requirement: each fact the
answer needs, each write with its target and audience, each dependency, and any
recovery or wait for an injected error. Each needs an event that covers it. A
fact in any `Expected:` line with no event that obtains it is a missing step. An
event too vague to follow ("identify the relevant current and stale records")
names no record, date or value, and is missing that step. A non-action or
final-response event is NON-FAIL 3, not a missing step.

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

The main session compares the list with the OEs: each M# needs an OE that
reads both sides and makes the fix. A confirmed M# with no OE is a missing
step.

**Grouping.** The main session groups confirmed items by the document, tab or
record they sit in. One group is one required fix: an OE that covers the group
names every item in it, and a group with no covering OE is one `MISSING`
coverage entry that lists its items. The report shows groups with counts, not
one line per item.

**Scope.** When one open instruction covers more than 15 confirmed items, the
report says so under `Scope:` in `## Deep Recheck`. That tells the contributor
the prompt needs to name which documents or fields the instruction covers;
/prompt P2 scores the same thing as Feasibility/Clarity. The groups still count
as missing steps.

## Rubric passes

Each rubric pass reads the prompt only to know what the rows must cover, and
fills the section 4 line for the rows it checks.

### R1 · Overly specific and unauthorized

For every row, write another answer the prompt and records allow. If that
answer fails the row, the row is overly specific: it locks a channel, heading,
format, cause, number or path the records do not settle. A row that requires
something the prompt never asked is unauthorized. An exact value that is the
only correct value is fine.

### R2 · Incorrect

For every row, re-read each value in the title and evidence from its record:
dollar amounts, emails, names, ticket ids, dates, counts, file names. Quote the
record. Any mismatch is incorrect. A record cell that is an inference, not a
message or a cell, is incorrect. A row that every careful run will fail because
the value is not in the records, or only another person can see it, is a
`predicted_all_fail` entry.

### R3 · Missing coverage and beyond-prompt rows

Split the prompt sentence by sentence into every outcome it requires, including
exclusions ("only these rows", "leave it open") and the named destination. Each
needs at least one Outcome row on the artifact the prompt named. A missing one
is a Major. Then go the other way: a row whose check traces to no prompt
sentence is beyond the prompt.

### R4 · Duplicates, weights and process

Compare every pair of rows. If removing one would not change the score for any
possible run, it is a duplicate. Rows that all fail from one miss are one
cascade group. Two rows that contradict each other fail. Check each weight
against section 7.9: lookup 1, comparison 3, join across sources 5. Process
rows must be an order every valid path follows that no Outcome row can see.

### R5 · Overly broad and destination

For every row, write a wrong answer a careless run could give. If it still
passes, the row is too broad. Another row catching it is not a defense. If the
prompt says email, post or file to a named place, the row must check that
place, not the final response.

### R6 · Self-contained

For every row, ask whether a grader could pass or fail it from the title and
the run alone, without opening the universe or working the task. Every expected
value (amount, email, name, id, count, date) must be in the title. "That
message", "the above" or "the correct figure" fails. A note that accepts more
or less than the title is the same failure.

### R7 · Atomic

Read every row word by word and count the claims that could be checked on their
own. If there are two or more and one can be true while another is false, the
row must be split. Common bundles: "and" joining two facts, a list of tickets or
cards, two writes, two services, two recipients who can be sent to separately,
and a verdict with its reason. "At least N" or "any one of" does not repair a
bundle. Two exceptions stay whole: fields of one message (its recipient,
subject and body), and the `coherent_record` exception in
`coherent_record.md` (fields of one record that the prompt asks for together).
