# Rev12 baseline review (6 Opus 5.5 runs, SQL 69db98aed17f, prompt b5ea6f0ff28c)

Graded by hand against solver/truth.json (sha 2ce0c48e71ff3bc2) with scratchpad grade.py, then run through tools/difficulty_stats.py on a draft rubric matrix that follows downstream_notes.md (draft_difficulty_matrix.json here; the real rubric and verifier remain of record).
Every run: Opus 5.5 in every assistant message, result success/completed. Runs 1 and 5 hit "Autocompact is thrashing" and resumed, but finished every deliverable.
Files: runs/trajectory-run-1..6.json (shas 6a8f44c5, fd1b9cfe, 2751378c, ef110e01, 50a7e7db, bf823efe).

## Per-run results
| Run | Calls | SciPlay | Paul | Build access (4 cells) | Anton | Draft score |
|---|---|---|---|---|---|---|
| r1 | 150 | In talks (miss) | In talks $50K (miss) | iOS only (right) | $40K (miss) | 60.7% |
| r2 | 156 | miss | miss | right | $40K (miss) | 60.7% |
| r3 | 141 | miss | miss | iOS and Android (miss) | $25K | 42.9% |
| r4 | 160 | Keep warm (right) | off (right) | right | $25K | 100% (golden run) |
| r5 | 192 | miss | miss | right | $25K | 66.7% |
| r6 | 135 | miss | miss | right | $25K | 66.7% |

Everything else was right in all six: sheet name, folder and share; 4 checklists on the card; the NCsoft comment; no Dentsu or Makers card; reply-all on Leonard's thread; the 14 Awaiting reply firms; Homa and Brightwater in; off-list firms out.

## How each trap was found
- Build access: Slack search "tester" (r1, r2, r4, r5) or "internal test" (r5, r6) returned Arthur's root post. r3 only searched "testflight". Caught 5 of 6 (pre-check missed).
- Paul: only r4 searched Slack for "Paul" and opened the DM. r1 searched "Heydon" (no hit). Caught 1 of 6 (plus the pre-check).
- SciPlay: only r4 searched "pass" and opened the thread. Caught 1 of 6 (plus the pre-check).
- SciPlay and Paul were caught by the same runs (pre-check, r4) and missed together by the other five: a thoroughness correlation.

## Gates (difficulty_stats.py on the draft matrix)
- pass@1: 1 of 6. PASS.
- Average: 66.3%, under the 85% Medium cap and the 80% target. PASS.
- SD: 0.171. PASS.
- Horizon: golden run r4, 160 calls. PASS.
- Failure patterns: **FAIL (Signature Over-Concentrated)**, largest 80% of 5 failing (pairwise reading also 80%). r5 and r6 fail the same rows; r1 and r2 fail those rows plus Anton's one amount row, so single-linkage joins all four.
- (Model provenance printed FAIL only because the hand-built matrix has no verifier model evidence; all six trajectories are claude-opus-5-5.)

No fair rubric splits r1/r2 from r5/r6: the amount is asked only on the sheet row ("Put the amount on their row"), so Anton's miss fails exactly one row.

## Cause
SciPlay and Paul are both found only by the same thorough name/keyword searching, so 5 of 6 runs miss both and share one core pattern. The only trap that varies independently (Anton) differs on a single rubric row and cannot separate patterns.

## Re-run odds without changes (scratchpad boot13.py, UNCALIBRATED)
- Bootstrap of the 7 rev12 runs (keeps the SciPlay-Paul correlation): P(every gate) about 0.23.
- Independent traps at rev12 rates: about 0.63.

## Proposed rev13 (two edits, truth unchanged)
1. Paul's DM note also says there is no SAFE coming from him, so the global Slack "SAFE" search (15 of 22 runs so far) shows it. Paul's catch becomes about 0.5 and no longer tracks SciPlay.
2. Leonard's email asks the reply to also give the total the new investors put in ($25,000), so an Anton miss fails two rows (sheet amount and reply total) and forms its own pattern.
Estimate (independent traps): P(every gate) about 0.62-0.79, patterns about 0.89-0.96; SD becomes the main risk. Either edit alone would have split this batch into 3 patterns (largest 40%).
