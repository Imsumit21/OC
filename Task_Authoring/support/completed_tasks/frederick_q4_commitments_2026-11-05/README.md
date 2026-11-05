# Frederick: Q4 vendor and partner commitments backlog (submitted 2026-11-05)

Persona Frederick Stone (Co-founder) · Long Horizon · Executive / Corporate Ops / Actions · difficulty mode easy · universe Oct 1, 2025 (synth-cut, clock 2025-10-01 00:00 PT) · platform task 6ae9909f707bc2aa0a7ed6e9 (id taken from the platform report file names) · requester targets: more than 130 calls per run, average under 80%.

`task_inputs/` is the full slot folder as submitted. It includes `Run1_trajectory.json`, `02_Changelog,json` (the file name has a comma, kept as submitted) and `Working_Files/run_forensics/`, which holds every injection revision rev1 to rev4 with its SQL, the rev3 and rev4 pre-check and baseline forensics, and copies of the platform reports. `eval_reports/` holds every platform eval report, renamed by stage, verdict and round (`0_injection_*`, `1_prompt_*`, `1a_hardness_*`, `2_oe_*`, `3_rubric_*`). `work/frederick_q4_commitments/` holds copies of the builders from `task_inputs/Working_Files/plan/` and the solver:
- `plan/` builds the scenario, SQL, manifest, dossier, prompt brief and OE ledger, events and check.
- `plan/rubric/` holds `build_rubric.py` (09_Rubrics.json, V3 rubric_rows and rows.json) and `build_plan.py`, `build_selfreview.py` and `build_check.py` (the plan, its self-review and the check report). It also holds `grade_baselines.py`, the local grader over the rev4 baseline writes.
- `plan/allfail/` holds `build_allfail.py` (the all-fail workbook and screen file) and the evidence probes.

## Final state
- **Injection SQL:** `01_Universe_Inject.sql` sha256 69603ab4b6a4 (rev4; the platform calls it rev 8). Friction: none. No reference files. The stored /injection reports cover rev1 to rev3, all PASS. Rev4 changed the trap carriers: corrections were de-named and threaded, and the Hootline terms doc was removed.
- **Prompt:** sha256 32f7ab0cabd6, 510 bytes. Work through Leonard's vendor and partner backlog going by his email. The log goes in the Q4 commitments folder, signing cards on the Harmony Games board, a reminder per company on the January review day, then a reply to Leonard. /prompt PASS 5 (`1_prompt_PASS_r1.md`).
- **Oracle Events:** 147 events, sha256 10814dbd922b. /oe NON-FAIL 3, then PASS 5 (`2_oe_PASS_r2.md`).
- **Rubric:** 102 rows (101 Outcome, 1 Process), weight 350 (5 x45, 3 x34, 1 x23), sha256 894c0dc9258c. /rubric FAIL 1 on 57 rows (coverage 58/106, weights), FAIL 1 on 102 rows (five wording fixes), then PASS 5 (`3_rubric_PASS_r3.md`).
- **/hardness:** FAIL 2 on rev3 (only Nintendo missed), then NON-FAIL 4 on rev4 (`1a_hardness_NONFAIL_r2.md`).
- **Baselines** (rev4, 6/6 completed, all claude-opus-5-5):
  - Verifier: 82, 82, 76, 82, 81 and 79 of 102 rows.
  - Weighted pass: 72.0, 72.0, 68.0, 72.0, 72.3 and 69.4, average 71.0% (easy cap: under 90%). pass@1 0/6.
  - Population SD 0.016: FAIL (spread too low). 4 failure patterns, the largest 50%.
  - Counted calls 205, 182, 212, 183, 151 and 200 (average 189).
  - 17 rows failed every run and all 17 are VALID (`11_AF_Justification.md`, `11_Baseline_AllFail_Justifications.md`).
  - `12_Difficulty_Stats.txt` was not written. The difficulty calculator output is in the all-fail workbook's evidence (`Working_Files/12_difficulty_input.json`).
- **Local gates:** rubric-writing fails only the structural `diversity.authority_share`; the guardrails doc, the folder README and the paperwork folder decide 90%, 86% and 73% of the weight. rubric-check fails only its inherited chain. allfail passes every content check and is blocked only by the chain.
- **Human time:** 22.5 h, typed on the platform. `05_Human_Time.md` in the slot is empty; the worksheet is `Working_Files/05_Human_Time_Worksheet.md`.

## Key answers
- **Scope:** 36 companies from Leonard's Sep 30 email (an offer, a trial, a quote, terms or an ask that one of us engaged with: a call, a reply, a sign-up or paper). These are 33 filed papers, plus Hootline (August thread), Balancy (base thread) and Nintendo (portal notices plus Linear ZOM-567). The look-alikes stay off: Mattel, the investors, the ad networks, Appodeal, NCsoft, Dentsu and the cold pitches.
- **Decisions** (guardrails, first fit, top to bottom):
  - Answered 4: Balancy (Leonard, Sep 11), Lanternfly Publishing (Leonard's Sep 29 DM), Motive Forge (Arthur, Sep 19), Spotlight Fest (Robert's Sep 17 #executives post).
  - End 10: Ascendo, Brightlane Studio, Clipforge, Lingora, Panelpulse, Pixel Harbor Events, Reviewly, Soundvault, Streamcast Talent, Wishwave.
  - Keep 3: Certwell, Pingwise (the keep card's "night pager"), Vaultline.
  - Sign 7: Bundlehouse, Kinetic Arcade, Lumencloud (these three ESG first), Markward, Nintendo, Orbit Store, Playfuse.
  - Park 12: Benchmarkly, Cloudlark, Driftwood Audio, Echohall, Framewell, Glyphworks, Hootline, Loopnote, Pressbeam, Quillcraft, Retainly, Tilecast.
- **Writes:**
  - A native Google Sheet "Q4 commitments log" in the Q4 commitments folder, with the template's seven headings and 36 rows.
  - Written answers to 31 companies, plus the Clipforge cancellation to billing@paylane.io.
  - Three ESG intake emails, one per agreement, each with the checklist's term, licence or exclusivity, cost, needed-by date and signer.
  - Seven To Do cards.
  - 32 new contacts with the company in the job field.
  - 14 reminders on Mon Jan 5, 2026.
  - A reply on Leonard's thread listing keeping (3) and waiting to sign (7), sent after every other write.
- **Traps:**
  - Nintendo: the "Registration Completed" notice looks done; Linear ZOM-567 shows acceptance is due by Oct 15.
  - Framewell: Leonard's waiver is a thread reply under the Sep 22 Playtestcloud post.
  - Lanternfly: Leonard's answer is a DM thread reply that says "Wen" and "Southeast Asia", not the company name.
  - Spotlight: Robert's post says "Rina" and "Dec 5 indie showcase", not the company name.
  - Balancy: a base thread with Leonard's "circle back" answer.
  - Pingwise: the alias "night pager".
  - Clipforge: the Paylane notice overrides the pilot dates.
  - Pixel Harbor: a June quote.
  - Wishwave: Monday's travel change.
  - Markward: the July note superseded.

## Lessons carried forward
- **De-named corrections:** the rev4 rewording made the five corrections invisible to company-name searches. All six baselines then missed the same five records, with 0 Linear calls in every run. The average landed at 71% but the SD was only 0.016. A trap every run misses adds difficulty but no spread. For SD, place traps that runs catch about half the time, and give runs different routes to them.
- **/rubric round 1:**
  - Content that differs per target gets one row per target, with no cap. That meant every written answer, every ESG checklist part and every member of each reply list (102 rows).
  - Sample only template-identical writes, and give each sample group a volume row that states the template.
  - Weights: a rule applied to one company's thread is 3, a value copied from one record is 1, and only real traces or joins are 5.
  - One ordering ask gets one Process row.
  - Reply rows must name the thread.
  - The lint flags "such as" (vague_exemplar).
- **/rubric round 2:**
  - An Accept alternative must also appear in the title (e.g. "(or Hana)").
  - Use the rule doc's verb, e.g. "to sign or accept".
  - Sign answers must reject a lawyers-first reply when ESG has no trigger.
  - Sibling rows need the same scope word ("alone").
  - Apply checked fixes word for word and diff the other rows against the reviewed sha, so they stay locked.
- **Builder drift:** the builder export had C48's weight as 3 instead of 5 and C102 as outcome instead of Process. Diff the export field by field before the verifier runs. The builder's imported linters (atomicity, self-containment) flagged required volume rows and once analysed an unrelated example. Mark such findings invalid, citing the eval's rules.
- **Speed:** the shortcut probe is cached per value. The first run took about 1 h; the 102-row re-run took about 35 min. The stage gates re-run everything, so iterate with `--rerun lint` and do one full run at the end.
- **All-fail workbook:** each criterion quote must keep the JSON-escaped `\"` quotes, because the gate tests it as a substring of the raw 09_Rubrics.json text. Re-check every per-run claim against the trajectories; two slips were caught that way (run 2 never searched Slack for Spotlight; run 6 never saw Balancy).
