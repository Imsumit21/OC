# Robert: LLC take-over plan for Combo Fighter (submitted 2026-11-06)

Persona Robert (Co-founder & Creative Director) · Long Horizon · Executive / Finance / Planning and decision support · difficulty mode easy · universe Feb 14, 2026 (normal, clock 2026-02-14 00:00 UTC) · platform task 6adfee3b47f7621feba5b96c (id taken from the platform report file names) · requester targets: more than 130 counted calls in every run, average under 85%, SD between 0.1 and 0.3.

`task_inputs/` is the full slot folder as submitted, diff-verified against the original. It includes `Run1_trajectory.json` (the rev4 pre-check upload, identical to `06_PreCheck_Trajectory/trajectory.json`) and `Working_Files/run_forensics/`. That folder holds every injection revision rev1 to rev4 with its SQL, solver and truth, the rev3 and rev4 pre-check forensics, the rev4 baseline decode (`rev4/baseline/BASELINE_DECODE.md`), the rubric drafts (`rev4/rubric/`), the /rubric rounds with the reviewed JSONs (`rev4/rubric_r1/`) and the platform builder export (`rev4/rubric_r1/platform_builder_export_2026-11-06.json`).

`eval_reports/` holds every platform eval report, renamed by stage, verdict and round:

| File | Revision |
|---|---|
| `0_injection_PASS_r1.md` to `_r4.md` | rev1 to rev4. The rev2 resubmit returned an identical report, so it is kept once. |
| `1_prompt_FAIL_r1.md` | rev2 |
| `1_prompt_PASS_r2.md`, `1_prompt_PASS_r3.md` | rev3, rev4 |
| `1a_hardness_FAIL_r1.md`, `1a_hardness_PASS_r2.md` | rev3, rev4 |
| `2_oe_PASS_r1.md` | rev4, OEs e210cd02c49e |
| `3_rubric_FAIL_r1.md`, `3_rubric_NONFAIL_r2.md` | rubric 8296aaf8dc71, then cd67ff04220c |

`work/robert_llc_takeover/` holds copies of the builders from `task_inputs/Working_Files/plan/` (the `.py` scripts, plus `rubric_plan_extra.json` and `rubric_plan_selfreview.md`) and the solver:
- `build_scenario.py`, `build_sql.py`, `build_final_manifest.py` and `build_dispositions.py` build the design, the SQL and the manifest; the `assemble_*.py` scripts build the dossier, brief, OE ledger, OE events and OE check.
- `rubric_rows.py` (row data and revision blocks), `rubric_titles.py` (titles, justifications, sources), `assemble_rubric_draft.py` (09_Rubrics.json and the V3 sidecar rows), `assemble_rubric_plan.py` and `assemble_rubric_check.py`.
- `oe_tmp/` holds backups, including the shelved round-3 rubric and OE scripts in `oe_tmp/r3_unused/`.

## Final state
- **Injection SQL:** `01_Universe_Inject.sql` sha256 f1a290ced176 (rev4). Friction: none. No reference files. /injection PASS on all four revisions.
- **Prompt:** sha256 ccd229a59a17, 627 bytes, the same text from rev2 to rev4. Rev2's /prompt FAIL was fixed in the universe (records that settle each fork), not in the prompt. It asks for:
  - a call on every issue in Leonard's LLC take-over project, the way his DM lays it out, left as a comment on each issue;
  - a plan sheet in Robert's Drive, laid out like Leonard's draft and shared with Leonard and Blake;
  - the project made to match the sheet;
  - then a reply in Leonard's DM thread with the plan, what it costs each of them a month and the sheet link.
- **/prompt:** FAIL on rev2 (three Linear-write forks unsettled), then PASS 5 on rev3 and on rev4 (neighbour similarity 0.776).
- **/hardness:** FAIL 2 on rev3 (only DONE and DATE landed), then PASS 5 on rev4 (pre-check run sha256 cb1259b5b2fd, 157 calls; it missed the VO campaign and set ENG-2462 Done).
- **Oracle Events:** 104 events (19 reads, 4 decision steps, 81 writes), 30,448 characters, sha256 e210cd02c49e. /oe PASS 5 on the first round.
- **Rubric:** 130 rows (129 Outcome, 1 Process), weight 328 (5 ×23, 3 ×53, 1 ×54), sha256 cd67ff04220c.
  - /rubric FAIL 1 on the 73-row draft (8296aaf8dc71): 63 per-target rows missing, plus bundles and date edges. The Fix List was applied exactly.
  - Then NON-FAIL 4 on the 130 rows: R6, R40, R83 and R96 one weight level low, plus 3 Minor. The requester accepted NON-FAIL 4. The round-3 fixes were shelved, not applied.
  - Known residual: R8 grades a $0 cost for Combo Fighter that OE 26 does not state.
- **Builder:** all 130 rows matched, except R101 (Calm Play LLC sheet row), typed as weight 1 instead of 3. The builder also strips `<>` around Gmail Message-IDs and dropped `~` in R12 and R107 (cosmetic). Two imported linters ("more specific than the prompt" on R6/R96, atomicity on R20/R22) were marked invalid, citing Eval 3 lines 37, 394, 494 and 296.
- **Baselines** (rev4, 6/6 completed, all claude-opus-5-5):
  - Verifier: 112, 115, 130, 112, 97 and 116 of 130 rows.
  - Weighted pass (local weights): 82.3, 85.7, 100.0, 82.3, 64.9 and 86.6. Average 83.6% (easy cap: under 90%; requester: under 85%). One full pass (run 3).
  - SD 0.103 (population) or 0.113 (sample). With the builder's R101 at weight 1 it is 83.5%, same SD.
  - Counted calls 156, 157, 162, 149, 152 and 159 (all over 130).
  - No row failed every run, so there were no all-fail rows. `11_AF_Justification.md` is empty and `11_Baseline_AllFail_Justifications.md` is the template file.
  - `12_Difficulty_Stats.txt` was not written locally.
- **Local gates:** every stage gate was re-pasted PASS on the submitted files (oe-writing, oe-check, rubric-writing, rubric-check).
- **Human time:** 18.25 h in `Working_Files/05_Human_Time_Worksheet.md`. `05_Human_Time.md` in the slot is empty (the platform field is typed).

## Key answers
- **LLC takes 7 (Todo):**

  | Item | Cost | Owner | Note |
  |---|---|---|---|
  | Combo Fighter (ENG-2438) | $0 | Robert | |
  | Domino Delights (ENG-2439) | | Leonard | |
  | DD production AWS (ENG-2441) | $140 | Arthur | |
  | CF backend and auth stacks (ENG-2445) | $62 | Arthur | |
  | AppsFlyer (ENG-2451) | $0, free tier | Leonard | |
  | DD player support (ENG-2462) | | Arthur | support build before Feb 28 |
  | Meta VO campaign (new issue) | $3,000 a month | Leonard | |

- **Arthur pays himself, 3 (Done):** Metabase $100, dbt $100 and GitHub $48, which is $248 a month. GitHub counts even though HG keeps the org.
- **HG keeps 28 (Canceled):** every other issue, including Zombie Match, its account, the DD dev account, Figma, Calm Play LLC, layer.ai, the Apple and Google Play accounts and the one-offs.
- **Money:** $3,450 a month, $1,150 each. Arthur puts in $902 cash on top of the $248 he already pays.
- **Sheet:** 38 item rows (37 if Metabase and dbt share a row as on the draft), with the draft's eight columns, in Robert's Drive, shared with Leonard and Arthur. The reply in Leonard's DM thread is the last write.
- **Traps:**
  - VO campaign: only in Leonard's #prototype thread reply ("my card"), with no Linear issue.
  - DD take test: January revenue $183.11 (warehouse) against $140 hosting. Arthur's DM supersedes the ~$1k.
  - Zombie Match: $0.00 in January, so it stays with HG, against the Monday notes' "DD and ZM both come with CF".
  - ENG-2462: Apple's App Review rejection is later than Arthur's "done".
  - CF stacks: the Jenkins mail gives $62, superseding "about $95".
  - Metabase and dbt: $100 each, superseding ~$300.
  - Figma: prepaid, so it stays with HG against the draft's LLC row.
  - Calm Play LLC: HG's subsidiary, not the new LLC.
  - layer.ai: export the concept art by Mar 3.
  - One-offs and yearly fees stay off the monthly plan: the Playable vendor's $3,750, Carta, Google Play.

## Lessons carried forward
- **One missed record fails a whole cluster.** Five of six runs never found the VO line, and that one miss failed 14 rows together: the new issue and its fields, the row count, the VO cost and payer, both share rows and the reply. The SD still reached 0.103 only because ENG-2462 (3/6 runs) and Domino Delights (1/6) failed in different runs. A task needs at least two traps that runs catch at different rates.
- **Per-target rows raise the average.** /rubric round 1 required one row per Linear comment and per state move, which took the rubric from 73 to 130 rows. Most of the new rows are easy per-issue calls, so the proxy average went from about 76% to 83.6%. Plan the trap weight against the full per-target row count, not the first draft.
- **Builder and verifier exports drift.**
  - R101's weight was typed wrong. The builder strips `<>` and some `~`.
  - The verifier export auto-links titles that contain a domain or email (`[layer.ai](http://layer.ai)`, `mailto:`). Strip them before matching rows.
  - A linter's "reviewed all 95 criteria" did not mean rows were missing.
- **Imported linters.** "Not more specific than the prompt" flags exact-count rows, and atomicity flags OR-alternatives of one value. Both are invalid under Eval 3: exact counts cover exclusions (lines 37, 394), every sampled output needs a volume row (494), and alternative accepted values stay in one row (296).
- **OE locators.** Search terms must come from the prompt or an earlier OE, never from a target's subject or title. VO is found by "my card", the $140 by "AWS bill", the billing mail by "metabase".
- **Rubric gates are slow.** v3.rubric_evidence re-reads every source, which took 16 min at 73 rows and about 40 min at 130. Iterate with targeted reruns and do one full run at the end.
- **V3 sidecar.** Seeded Linear and Trello ids fail the base-only reachability search, so cite seeded Slack, Gmail and Docs records, base posts or Contacts.
- **Shortcut probe.** Use distinctive literals only ($ figures, keys, dates, ts). Generic tokens (LLC, Todo, 0.00, $100) made the probe take 45 min with 30 noise hits.
- **Diversity gate.** Give ledger origins their honest `prompt` lead. Without it, one document decided 59% of the weight.
