# Rev11 baseline review (6 Opus 5.5 runs, SQL 75b6cb2ac453, prompt b5ea6f0ff28c)

Graded by hand against solver/truth.json (sha dfc80760a6ac6397) with scratchpad extract.py and grade.py. The first paste had two duplicate files (run-4 = run-5, run-2 = run-6); the user replaced run-2 and run-5, so the six files below are all different.

| Run | sha256 (16) | Calls (main+sub) | SciPlay | Paul | Dentsu / T-Acc build | Anton | Other |
|---|---|---|---|---|---|---|---|
| r1 | 7f8cc0a82db7ee90 | 122 | In talks (wrong) | off (right) | iOS only (right) | $25K | none |
| r2 | 8852edc47ec2d00d | 206 (162+44) | In talks (wrong) | off | iOS only | $25K | none |
| r3 | e07a11e94fbecbb4 | 129 | In talks (wrong) | off | iOS only | $25K | none |
| r4 | bf1c2228c4c1815b | 127 | In talks (wrong) | off | iOS only | $25K | none |
| r5 | 86665ee45ed0cb32 | 130 (124+6) | In talks (wrong) | off | iOS only | $25K | none |
| r6 | 07b151f839f32c57 | 149 | **Keep warm (right)** | off | iOS only | **$40K (wrong)** | none |

A SciPlay miss also puts SciPlay on the In talks checklist, adds a "F/up with SciPlay" card (19 cards) and makes the counts In talks 8/0 and Keep warm 2/0.

## Trap catch rates in rev11 (pre-check + 6 baselines)
- Paul's back-out (reply under the angel post): 7 of 7. Every run reached the angel post from a "SAFE", "docusign" or "angel" search and opened its thread, including the four runs whose Slack tool shows only the thread marker.
- Build access (Arthur's answer in the T-Accelerate mail thread): 7 of 7. Every run read that thread in full.
- SciPlay (Robert's reply under the unrelated a16z post): 1 of 7 (r6).
- Anton $25K: 6 of 7.

## Gates (estimated with the lean rubric of downstream_notes.md; the verifier and rubric remain of record)
- pass@1: 0 of 6 full passes. PASS.
- Average weighted pass rate: about 81% (five runs about 78.5%, r6 about 94%). Under the 85% Medium cap; over the 80% target.
- Horizon: average 144 counted calls, lowest 122. PASS.
- **Failure patterns: FAIL (Signature Over-Concentrated).** r1-r5 fail exactly the same rows, 5 of 6 failing runs = 83% > 50%.
- **Spread: FAIL (Spread Too Low).** Population SD about 0.06, under 0.1.
- No fair rubric changes this: the five runs made the same single mistake and the same deliverables otherwise.

## Cause
Rev11 moved Paul's and the build-access corrections onto paths every Opus run reads (the angel thread found by its own SAFE search; a mail thread read in full). Only SciPlay stayed hidden, so the difficulty rests on one choke point again. The rev11 design estimate (Paul caught 45-60%, build 55-70%) was wrong: the pre-check's catches were the real signal, and the "different Slack tool" explanation did not hold (runs with the marker-only tool opened the angel thread too).
