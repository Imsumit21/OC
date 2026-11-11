## Self-review

**1. Re-read as /rubric** (3_Rubrics_Eval.md Phases 1–5, in order), with the pre-verdict sweep (5.0), on the rebuilt JSON @@SHA@@.
- **A missing requirement.** The 65 outcomes the round-1 report listed are rows now: 22 note reasons, 19 moves to the right child, 15 sub-issue parents and titles, 7 child states, the Area column sample and the slide's fifth number.
- **A phrasing mismatch with the prompt.** Titles use Brian's own words for the tabs, columns, statuses and states.
- **A non-atomic row.** The three count rows over separate writes are gone (ten create rows, 17 sub-issue rows, 22 move rows); the 22 move-plus-state rows are split into move rows and eight 'sets ZOM-n to the state X' rows; the two template rows and the review-list row are the volume controls the Fix List wrote.
- **A category mislabel.** One Process row, @@P:dm_after_writes@@, for 'Once that's done'. The others are Outcome.
- **An over-specific or hard-coded title.** The Why rows accept 'no fix in main yet' and any wording of the later sighting; marks accept any mark meaning on the list; child and sub-issue titles accept other words around the name.
- **A duplicate or cascade group.** None: the report ruled that one missed record failing rows on separate deliverables is not a group.
- **A vague exemplar.** None; the lint has no hit.
- **A prohibition-only title.** None. An idle Agent fails every row.
- **Calibration** (Evals/references/rules/rubric_qc_examples.md): do-nothing (every row needs a write or the message); LITERAL keys (ZOM keys accept a key or a link); reachability (every deciding source is PROMPT_LINKED and re-checked by v3.rubric_evidence); OE conflict (the /oe-passed path passes every row: OE 21's statuses, counts and states are the rows' values).
- **Weights.** 5 where the value joins records across services, 3 where a reason or count is read or calculated from the decision, 1 for a copied field.

**2. Round 1 taken in.** /rubric FAIL 1 on afbc830d0cbb. Every Fix List title was parsed from the report file by script and copied character for character (plan/apply_fixlist.py asserts each one is found exactly once); the one title the report misprinted (item 9) is written in its siblings' form. 74 untouched rows are byte-identical to the reviewed JSON. Six Opus 5.5 baseline runs simulate at 57.6, 79.7, 60.2, 65.3, 57.6 and 65.3 % on this rubric (average 64.3 %, four failure groups); no row was added or tightened beyond the Fix List.

**Re-verified.** Every source_value in the 184 evidence rows was re-read in this run, not taken from the plan: seeded fields from 01_Universe_Inject.sql by table, identity and column, base fields through tools/hg.py (plan/oe_reads.py → plan/oe_base.json: the six build posts, ZOM-543, ZOM-556, ZOM-560 and the four pull requests), and the statuses, area counts and five numbers from solver/truth.json (10, 9, 20, 0, 7). Two citation choices follow from the gate's reach proof, not from the task: a #builds post is cited by its ts field because its one line sits in the bot's attachment block, and a ticket this task seeds (ZOM-567 to ZOM-586) is reach-proven through the flow pass sheet that names it, since a record-id lookup reads the base only.

**3. Counter-readings, one per criterion.**
