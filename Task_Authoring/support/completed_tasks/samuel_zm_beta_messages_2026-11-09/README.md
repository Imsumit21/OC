# Samuel Turner: Zombie Match beta player messages (archived 2026-11-09)

| | |
|---|---|
| Persona | Samuel Turner |
| Horizon | Long Horizon |
| Assignment | Design / Marketing and GTM / Retrieval |
| Difficulty mode | medium (cap: average under 85%) |
| Universe | Oct 1, 2025 (synth-cut, clock 2025-10-01 00:00 PT) |
| Requester bar | more than 130 counted calls in every run, corrected average under 80% |
| Slot | `Task_Authoring/task_inputsK/` (a second slot beside `task_inputs/`), never saved to the Evals input store |

**Archived as found.** The local folder ends at the /rubric round-3 Fix List, applied on 2026-11-06 (rubric 377baf5ab4cc). These were never filled locally: `10_Baseline_Verifier_Results.md`, `11_AF_Justification.md` and `12_Difficulty_Stats.txt` are empty or missing. No platform report after /rubric round 3 is stored, so the final /rubric verdict, the verifier results and the all-fail screen text are not recorded here. The archive date is not the submission date.

`task_inputs/` is the full `task_inputsK/` folder, diff-verified against the original. `Working_Files/run_forensics/` holds:
- every injection revision rev1 to rev6 with its SQL;
- the rev6 baseline forensics, including the ticket-joined fair regrade in `rev6/baseline/fair_regrade/`;
- the three /rubric rounds with their reviewed JSONs and builder-change notes (`rev6/rubric_r1/` to `rubric_r3/`).

`eval_reports/` holds the platform reports that were saved locally, renamed by stage, verdict and round:

| File | Revision |
|---|---|
| `1_prompt_FAIL_r4.md` | rev4 (UGT 2, Coherence 2: Snowflake PUSH_NOTIFICATION_STATS answered "who hears from us" differently) |
| `0_injection_PASS_r5.md`, `1_prompt_NONFAIL3_r5.md`, `1a_hardness_FAIL2_r5.md` | rev5 (Coherence 3 on SC-13's list date; /hardness score 2, the run missed only the ZOM comment asks) |
| `2_oe_PASS5_r1.md` | rev6 OEs 4924949d7fd3 |
| `3_rubric_FAIL1_r1.md`, `_r2.md`, `_r3.md` | rubrics 3911b7d5f4de (143 rows), d1cbadf710e9 (149), 5bf50637b0a1 (152) |

Not stored locally: the platform /injection PASS on rev4 and the rev6 /injection, /prompt and /hardness (NON-FAIL 4) reports. The local `/injection` reviews of rev1 and rev2 are in `task_inputs/Working_Files/plan/` (`0_injection_report*.md`, `inj_review_rev2.md`).

`work/samuel_zm_beta_messages/` holds copies of the builders from `task_inputs/Working_Files/plan/` (the scenario, SQL, manifest, dossier, brief, OE ledger, OE events and OE check builders, and `run_checks.sh`), plus:
- `rubric/`: `build_rubric.py`, `build_plan.py`, `build_selfreview.py`, `build_probe.py`, `build_check.py`, `grade_baselines.py`. Run them in that order; each round's Fix List is a block at the end of `build_rubric.py`.
- `solver/`: `solver.py` and `truth.json`.

## Final state (local)
- **Injection SQL:** rev6, sha256 6d162cfd1032. Friction: none. No reference files.
- **Prompt:** sha256 22df2abfec65, unchanged from rev4. It asks for everything in Leonard's DM, starting from the Zombie Match PN sheet:
  - a new sheet and a one-page note in Samuel's Drive folder;
  - a checklist on the push notifications card;
  - ticket changes and emails;

  then the counts in the same DM.
- **/hardness:** score 2 on rev5. NON-FAIL 4 (PROCEED) on rev6: 3 causes, 23% failed share, 189 calls.
- **Oracle Events:** 135 events, about 41K characters, sha256 4924949d7fd3. /oe PASS 5 on round 1.
- **Rubric:** 153 rows, weight 583 (5 ×83, 3 ×49, 1 ×21), sha256 377baf5ab4cc. /rubric FAIL 1 three times:
  - round 1: Overall 1, Weights 4;
  - round 2: 6 Major, 1 Moderate;
  - round 3: 9 Major rows and 2 missing outcomes.

  The round-3 Fix List is applied, with 140 rows byte-identical to the reviewed JSON. Its result on the platform is not recorded here.
- **Baselines (rev6, six runs, all Opus 5.5):**
  - Counted calls: 184, 185, 177, 186, 188 and 197.
  - The local grade on the final 153 rows is 70.4% average, SD 0.065, with 30 all-fail rows (weight 140), all of them the ZOM comment asks.
  - The fair regrade on earlier row sets gave SD 0.047–0.087.
- **Human time:** 21.5 h (`Working_Files/05_Human_Time_Worksheet.md`). It was flagged for a refresh after the baselines.

## Key answers
- **Leonard's message review:** 36 messages: Go 2, Hold 28 and Drop 6.
  - The five server-side rows fail test 2. The OEs and rubric never say no server push exists.
  - The two lapsed messages are graded without penalising a mention of the leaderboard batch.
- **Askers:** 8 askers. Their comment asks sit on ZOM tickets (ZOM-483, ZOM-542, ZOM-556, ZOM-563) outside the DES-314 filter. They are reachable through `linear_list_issues` updatedAt, or through the relations seeded on DES-315, DES-330 and DES-338.
- **Ticket changes:**
  - 5 new tickets;
  - 24 existing tickets move to Backlog and 6 to Canceled;
  - the rubric names DES-315, DES-318, DES-319 and DES-320.
- **Traps:**
  - the Plague Race pass;
  - Vincent's untick of "Lives recharged" after iOS 0.3.49;
  - Leonard's calendar note replacing his Sep 29 line with "Your Squad Is Waiting";
  - the Hold rule in card 79's description;
  - SC-13's BETA list date (Sep 30 to Oct 10, repaired with one Trello updateList).

## Lessons carried forward
- **One missed route fails a whole cluster.** The ZOM comment asks were caught by 0 of 7 runs and made up all 30 all-fail rows. If they are ruled invalid, the average jumps to about 90–95% with one full pass. A route that no run takes has to be proven before /create-allfail.
- **/rubric Fix Lists can reverse themselves.** Round 2 deleted the "exactly 30" sum row, and round 3 asked for the 24-to-Backlog and 6-to-Canceled rows instead. A checked fix can be wrong; keep each round's reviewed JSON so the DELTA locks can be rebuilt.
- **The user may run /rubric on a build you are still editing.** Keep a dated copy of every build and compare the report's reviewed SHA before acting.
- **Never `pkill -f` a pattern that appears in your own command line.** It kills the shell.
