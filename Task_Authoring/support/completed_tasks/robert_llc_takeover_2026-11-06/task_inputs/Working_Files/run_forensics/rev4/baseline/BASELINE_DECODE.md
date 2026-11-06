# rev4 baseline: hand decode of the six runs (2026-11-06)

**Inputs**
- Runs: `07_Baseline_Trajectories/trajectory-run-{1..6}.json`.
- sha256 per run: d7bedd5703f7 · 0a8de3210239 · cd349182d511 · 215adbff7c5d · 92075c140a03 · 0b54f4e403bd.
- `trajectory_ledger.py` bound all six to rev4 (SQL f1a290ced176). Every run is VALID Opus 5.5 (claude-opus-5-5 [1m]), completed, with no fallbacks.
- Counted calls: 156 · 157 · 162 · 149 · 152 · 159. Every run is over 130.

**About `surface_grader.py`**
- It reports 43.1 %, which understates the runs. These slots fail on decoder limits:
  - G/I field slots: the ' (ENG-n)' key suffix in b2, b3 and b6.
  - D1: register_parent. Every run created its sheet with no parent, so the sheet is in Drive root.
  - V1: the LLC-row count.
- The grades below are by hand, from the decoded write payloads (`b*/writes.json`, `b*/calls.jsonl`).
- Linear ids: usr_63fffeb4fab5233e = Leonard, usr_cc3e90160f490686 = Arthur, "me" = Robert.

## Trap results

| Trap (deciding record) | b1 | b2 | b3 | b4 | b5 | b6 |
|---|---|---|---|---|---|---|
| Meta VO $3,000 (#prototype 6908b2f1): VO row, new issue Todo/Leonard, total $3,450, $1,150 each, Arthur $902 cash | miss ($450 / $150) | miss ($450 / $150) | **hit** (ENG-2475 Todo/Leonard + comment; $3,450 / $1,150 / $902) | miss ($450 / $150) | miss ($343 / $114.33) | miss ($450 / $150) |
| ENG-2462 DD support (Apple App Review email) | Done ✗ | Todo/Arthur ✓, By **Mar 1** ✗ | Todo/Arthur ✓, Feb 28 ✓ | Done ✗ | Canceled ✗ (DD out) | Todo/Arthur ✓, Feb 28 ✓ |
| DD comes over ($183.11 vs the $140 DM) | ✓ | ✓ | ✓ | ✓ | ✗ (used ~$1k; ENG-2439/2441/2462 Canceled) | ✓ |
| CF stacks $62 (jenkins email) over $95 | ✓ | ✓ | ✓ | ✓ | ✗ ($95) | ✓ |
| layer.ai export step by Mar 3, Owner Robert | ✗ | ✗ | ✓ (on the CF row) | ✗ | ✗ | ✗ |
| Arthur's $248 Done; playable vendor excluded; Figma, Calm Play and GA Canceled | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 37 comments, sheet with the draft's columns, shared with Leonard and Arthur, reply in thread 1770961200.890407 with the link | ✓ | ✓ | ✓ | ✓ | ✓ (reply sent to Leonard's user id + thread_ts) | ✓ |

## Proxy rubric estimate (the rubric isn't written yet; UNCALIBRATED)

The proxy rubric has 29 rows weighted 1/3/5 by kind of work: per-item rows, each trap on its own row, and the reply, sheet and sharing rows.

| | b1 | b2 | b3 | b4 | b5 | b6 | avg | pop. SD |
|---|---|---|---|---|---|---|---|---|
| VO rows at weight 5 | 61.9 % | 67.0 % | 100 % | 61.9 % | 41.2 % | 70.1 % | **67.0 %** | 0.174 |
| VO rows at weight 3 (lenient) | 67.4 % | 73.0 % | 100 % | 67.4 % | 44.9 % | 76.4 % | **71.5 %** | about 0.17 |

## Gate readings under the proxy

| Gate | Reading |
|---|---|
| Full passes | at most 1 of 6 (b3). Fewer than 5: PASS |
| Average | 67–72 %. Under the 85 % target and the 90 % Easy cap |
| Spread | SD about 0.17, inside 0.1–0.3: PASS |
| Failure patterns | {b1, b4} 40 %, {b2, b6} 40 %, {b5} 20 %; largest 40 % ≤ 50 %: PASS, if the rubric gives ENG-2462 at least 2 rows (state, sheet next step, reply mention, By) |
| Horizon | b3 is the golden run, at 162 calls (Long 100–500+): PASS |

The pattern gate has one risk. If ENG-2462 gets a single rubric row, b1 and b2 differ on only one row, so single-linkage merges {b1, b4, b2, b6}. That is 80 % of the failing runs and fails the pattern gate.
