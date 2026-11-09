# Leonard: stockholder close-out for the wind-down (submitted 2026-11-10)

Persona Leonard Hayes (Co-founder & Creative Director) · Long Horizon · Executive / Finance / Authoring · difficulty mode medium (cap under 85%) · universe Feb 14, 2026 (normal, clock 2026-02-14 00:00 UTC) · platform task 6aed9d01a1cb8067d8ac7dee (id taken from the platform report file names).

`task_inputs/` is the slot folder as submitted, moved here unchanged except that `plateform_reports/` became `eval_reports/`. It includes `plateform_rubrics.json` (the platform builder export of the rubric) and `Working_Files/` (design, dossier, manifest, OE ledger and checks, rubric plan and check, human-time worksheet, run forensics rev1, rev1p and rev2, the verifier binding receipt).

`eval_reports/` holds every platform eval report under its original download name:

| File | What it covers |
|---|---|
| `_0_injection.md`, `-1`, `-3` | /injection on the SQL revisions, all PASS |
| `_1_prompt.md`, `-3` | /prompt on SQL bc72db9c, then on the rev2 SQL |
| `_1a_hardness.md`, `-3` | /hardness FAIL 2 (reviewer found no grant sizes), then the rev2 re-run |
| `_2_oe.md`, `-4`, `-8` | /oe FAIL 2 (1cd0f8a2e6c0), NON-FAIL 3 (0aca513e26e1), PASS 5 (0ac36b4fd15a) |
| `_3_rubric-round1.md` | /rubric round 1, FAIL 1 on 7fad981ba832 (first saved under task_inputsS2 by mistake; copied here) |
| `_3_rubric (1).md`, `(2)`, `-3` | /rubric rounds 2 to 4, each FAIL 1 (rows 53, 84, 178 to 180 and the 2 to 8 cascade; then row 2; then row 196) |

The round 5 report (FAIL 1, missing ENG-2462 holding row) was read from Downloads and is no longer on disk.

`work/leonard_stockholder_closeout/` holds copies of the builders from `task_inputs/Working_Files/plan/` and `solver/`: scenario, SQL, manifest and dossier builders; `plan/oe/` (verify_facts.py, oe_data.py, build_events.py, build_ledger.py, build_check.py, run in that order); `plan/rubric/build_rubric.py` and `run_pipeline.sh`. They need `TASK_AUTHORING_TASK_DIR` pointed at a slot folder and hard-code the original paths.

## Final state
- **Injection SQL:** `01_Universe_Inject.sql` sha256 65b7c3ec814b (rev2, 112,401 bytes). Friction: none. No reference files.
- **Prompt:** sha256 45766344a3e4, 711 bytes, unchanged since rev1. It asks for the holder sheet and the investor letter in the close-out folder (letter worked up from the #winddown draft), holder notes as Gmail drafts, the Linear issues, a heads-up to Griffin, a #winddown reply and an answer to KPMG's audit request; replies sent, holder notes left as drafts.
- **Oracle Events:** 99 events, 47,475 bytes, sha256 0ac36b4fd15a. /oe FAIL 2, NON-FAIL 3, then PASS 5.
- **Rubric:** 202 rows (201 Outcome, 1 Process), weight 480 (5 ×39, 3 ×61, 1 ×102), sha256 08f7ea309071. Five platform /rubric rounds, each FAIL 1 on one row family; every other dimension scored 5 from round 3. Row 202 (ENG-2462 holds nothing today) was added after round 5 and had no platform check before submission.
- **Builder paste:** the platform export differed from the file in three rows: R144 evidence held its justification text, R114 weight 4 instead of 5, R188 category Outcome instead of Process (the only Process row). R179 lost the angle brackets around an address. Reported to the user before submission.
- **Baselines** (6/6 completed, claude-opus-5-5): verifier 177, 195, 175, 162, 160 and 178 of 202. Weighted pass 78.5, 94.4, 76.5, 66.2, 67.5 and 78.3; average 76.9% (cap under 85%), no full pass, population SD 0.092. Tool calls 203, 251, 219, 214, 241 and 215 (mean 224).
- **All-fail:** R56 (5 Already told) and R58 (5 Closing), both VALID. Every run labeled one of ENG-2440 (told by Leonard's Feb 9 DM) or ENG-2446 (told by Robert's Feb 12 mail, Leonard copied) as Closing; no run found both. Justifications in `11_Baseline_AllFail_Justifications.md`.
- **Human time:** 22.00 h (`Working_Files/05_Human_Time_Worksheet.md`; typed paragraph in `05_Human_Time.md`).
- **Local gates:** content checks pass; allfail, humantime and the rubric gates fail only on upstream `chain.*` and `readiness.evidence` certificates, and allfail also on `tool.difficulty_stats` (the parser does not strip the verifier copy's `\[` `\]` escapes, so 96 titles do not bind; the binding receipt itself is BOUND).

## Key answers
- **Labels (26 holder issues ENG-2438 to ENG-2463):** Already told 5 (ENG-2438, 2439, 2440, 2446, 2447), Closing 5 (2441, 2442, 2443, 2448, 2449), Covered 2 (2444, 2445), Last day 5 (2450, 2453, 2456, 2458, 2460), Closing and last day 4 (2452, 2457, 2459, 2463), Nothing 5 (2451, 2454, 2455, 2461, 2462).
- **Traps that moved the score:** ENG-2440 told only by a Slack DM; ENG-2446 told by Robert's mail with Leonard copied; Calvin's Carta extension (ES-3 last day Feb 20, he goes first); the Covered family lines; the old Nov 2024 rows on the draft sheet; ES-16 counted at its vested 10,384 as of Dec 31, 2025.

## Lessons carried forward
- A platform /rubric report fixes one row family per round. Use its `(checked)` text verbatim; every own rewrite is the next round's risk, and a route a report calls simpler can be reversed in the next run.
- Diff the platform builder export against `09_Rubrics.json` field by field after every paste. Here one evidence field, one weight and the only Process category were wrong.
- A told rule whose evidence sits on two surfaces (a DM and a copied mail) made every run find one and miss the other. Count rows that tally those labels then all-fail together; that is valid, but it cascades.
- The verifier copy has no session IDs: bind runs with a reviewed content receipt (`Working_Files/verifier_binding.json`), and expect the platform's markdown escapes in titles.
