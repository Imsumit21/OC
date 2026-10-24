# Docs reading index

These are the project guidelines and QC specification the numbered Evals cite
as `Evals/Docs/...`. They are the grading authority. Where an Eval departs from
them, it says so in a named local-override table at the top of that Eval.

| File | Authority for |
|---|---|
| `QC_Centralized_Spec_Doc.xlsx` | QC spec (copy 4, 2026-09-27). Use the visible sheets: Audit Workflow, Examples & Notes, Appendix - Criteria Error & Weights, Appendix - Universe Data Queries, Appendix - Universe Inconsistency Examples. |
| `QC_Rating_Form_V12.csv` | The QC rating form (V12, "Version 2 overhaul", 2026-09-27): every scored dimension with its answer options and scores. Authority for dimensions, labels and scores. |
| `Original_Conference_Guidelines_-_Overall_Task_Flow.pdf` | Task stages, assignment axes (competency, task skill, horizon), prompt rules and the skeleton. |
| `Original_Conference_Guidelines_-_Universe_and_Tools.pdf` | The company, the thirteen services, scoped vs unscoped reads, and the clock (2026-02-14 00:00 UTC). |
| `Original_Conference_Guidelines_-_Persona_ACL_Policy.pdf` | Persona voice, remit and read access. |
| `Original_Conference_Guidelines_-_Prompt_Writing.pdf` | Prompt shape, difficulty from the environment, horizon tiers, no LLM-written prompts. |
| `Original_Conference_Guidelines_-_Oracle_Events.pdf` | Oracle Event fields, completeness, accuracy, non-actions, and OE-to-rubric conversion. |
| `Original_Conference_Guidelines_-_Rubric_Writing.pdf` | Outcome and Process, self-containment, affirmative framing, weights, what not to grade, spot checks. |
| `Original_Conference_Guidelines_-_Common_Errors_and_Pre-QC.pdf` | Frequent failure patterns and severity. |
| `Unique_Ground_Truth.pdf` | Contributor guide for the one-answer rule: the ten ways a prompt splits, with a bad line and a good line for each. Does not change scoring. |
| `Original_Conference_Guidelines_Example_Task.pdf` | A complete ML-selected Long-Horizon task (Marcus Bennett, Marketing and GTM) expressed as Oracle Events. Calibration only. |

**Known gaps in the QC spec copy (2026-09-27).** Only the Audit Workflow change
log and one Appendix row (B10, Agent-centric Format) were updated for V12. The
hidden rule tabs (2, 3, 4, Preview, Transform) are still the March version and
contradict V12 (for example pass@1 above 40% failing, a 40-call Tool Call Count,
and a Process-Heavy fail). Some Audit Workflow text is also stale: it keeps
"Golden Solution" wording and "40+ tool calls" under 09/27 notes. Where the spec
and V12 disagree on a dimension, label or score, V12 wins. The Appendix also
lists Overly Specific as Minor in B5 and B12 but Moderate in B8; Eval 3's Local
Overrides apply either way.

There is no separate universe-summary or persona-briefs document. Universe and
persona context comes from the three sibling data folders:

| Source | Use |
|---|---|
| `HarmonyGames_Other_Services/metadata/*.resolved.yaml` | Company and storyline background, 80 source scenarios. Context only: per `Evals/UNIVERSE_MAP.md` it cannot override evaluation rules, the roster or the clock, and it is never evidence for a finding. |
| `Evals/references/persona/roster.json` | The 17 selectable personas: exact key, name, email, role, department. |
| Contacts, Slack users and Linear users in the service exports | Role, team, membership and relationships for anyone in the universe, including non-roster participants. |
| The service records in `HarmonyGames_GitHub`, `HarmonyGames_Gmail` and `HarmonyGames_Other_Services` | Every fact a finding relies on. Read them with `Evals/tools/hg_search.py`. |

Read order for every stage: the QC spec and rating form, then the guideline for
the stage (Prompt Writing, Oracle Events or Rubric Writing), then Universe and
Tools and Persona ACL Policy. Tool names and parameters come from
`Evals/references/tools/catalog.json`; the persona roster is
`Evals/references/persona/roster.json` (17 selectable personas).
