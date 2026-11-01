"""Writes task_inputs/Working_Files/01a_Hardening_Report.md (MODE B, plan only) from the trajectories, the manifest and the projection model."""
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'task_inputs'))
WS = os.path.abspath(os.path.join(TI, '..', '..'))
SP = '/tmp/claude-1000/-home-sumit-Downloads-OC-OC/b7022e3b-f507-4faf-b9d4-2f8a57bda840/scratchpad'
man = json.load(open(os.path.join(TI, 'Working_Files', '01_Hardness_Manifest.json')))
cites = json.load(open(os.path.join(HERE, 'cites.json')))
G = json.load(open(os.path.join(SP, 'bl', 'grades.json')))
P1 = open(os.path.join(HERE, 'proj_out.txt')).read().strip()
P2 = open(os.path.join(HERE, 'proj2_out.txt')).read().strip()
WR = {1: dict(sheet=139, c2474=198, c2466=178, reply=215), 2: dict(sheet=154, c2474=228, c2466=206, reply=230),
      3: dict(sheet=135, c2474=194, c2466=187, reply=210), 4: dict(sheet=131, c2474=150, c2466=176, reply=208),
      5: dict(sheet=139, c2474=211, c2466=208, reply=215), 6: dict(sheet=118, c2474=182, c2466=171, reply=205)}
CALLS = {1: 215, 2: 230, 3: 210, 4: 208, 5: 215, 6: 205}
L = []
w = L.append

w("# 01a Hardening Report — rb-winddown-closeout")
w("MODE B (baseline trajectories present; verifier results and difficulty stats not yet produced) · plan only, no SQL changed in this revision · 2026-10-29\n")

w("## 1 · Mode, inputs, run validity")
w("Inputs read: `00_Assigments.md`, `01_Universe_Inject.sql` (sha 50f6a195de7e, /injection PASS r9), `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json` "
  "(25 traps), `04_Prompt.txt` (/prompt NON-FAIL r5), `08_Oracle_Events.md` (/oe PASS r3), `06_PreCheck_Trajectory/trajectory.json`, "
  "`07_Baseline_Trajectories/` (6 files).")
w("Inputs missing: `10_Baseline_Verifier_Results.md` (empty) and `12_Difficulty_Stats.txt` (absent) — the platform verifier has not been run. "
  "Every pass rate below is therefore a **projection from a modelled rubric**, not a number of record; gate 6 numbers come from `12` once it exists.\n")
w("| Rollout file | Model (main / subagents) | Calls | Completed export | Compaction / truncation | Injection re-applied | Final write |\n|---|---|---|---|---|---|---|")
for n in range(1, 7):
    fn = "trajectory-run-1 (1).json" if n == 1 else f"trajectory-run-{n}.json"
    w(f"| {fn} → run-{n} | claude-opus-5-5 / none | {CALLS[n]} | yes (result event present) | none seen; large reads spilled to files and were re-read with Bash | "
      f"yes — seeded ask, keep-list thread, conventions doc and Sunset thread returned (run-{n} · call {cites['T11'][str(n)]}) | slack_send_message, run-{n} · call {WR[n]['reply']} |")
w("\nFile mapping is by content (each run's own sheet id and reply); verifier `Run #N` mapping is pending until `10` exists. No errored runs.\n")

w("## 2 · Gate status (projected) beside the clean average")
w("`12_Difficulty_Stats.txt` does not exist, so there is no number of record. The projection scores each rollout against a per-write rubric model "
  "shaped the way `/rubric` demanded on the Douglas task (one row per write target: 25 state rows, 45 comment rows; register action, status and "
  "by-when per account; totals in the sheet and the reply; weights 1/3/5 by kind of work). Model: `support/task_work/rb_winddown_closeout/hardening/proj.py`.\n")
w("```\n" + P1.splitlines()[0] + "\n" + P1.splitlines()[1] + "\n```")
w("| Gate (GEN_EXECUTION §3) | Threshold | Projected on current data | Status |\n|---|---|---|---|")
w("| Average weighted score | < 75% (Evals) · < 90% (QC) · author < 80% | 95.1% | FAIL all three |")
w("| Per-rollout SD | 0.1–0.3 | 0.024 | FAIL |")
w("| pass@1 | ≤ 3 of 6 | 0 of 6 at a 100% bar (every run misses CodeRabbit) | PASS |")
w("| Failure patterns | ≥ 2, largest ≤ 50% | runs 3 vs 2/4/5 differ on ≥ 2 rows; largest pattern (CodeRabbit-only) ≈ 1 run | PASS (weak) |")
w("| Errored runs | ≤ 2 | 0 | PASS |")
w("| Horizon (calls) | > 150 (author) | 205–230 | PASS |")
w("\nClean average: no CONFOUNDED criterion is counted in the model (the Helpshift third clash is scored as a failure only of the clash-scope row; "
  "see §7), so clean = raw = 95.1%. **Mechanism weight share:** rows whose result depends on a LANDED node = 12 of 553 weight (2.2%), far below "
  "the ~30% that Hardness_Mastery §11 (NF2) gives as the floor for an average under 75%.\n")

w("## 3 · Predicted /hardness band (run closest to the median: run-4)")
w("| Requirement (prompt / incorporated) | Result | Evidence |\n|---|---|---|")
w(f"| Register: 28 accounts, actions, by-when, owner, cost | MINOR_GAP (adjoe added; CodeRabbit status/by-when wrong) | run-4 · call {WR[4]['sheet']} |")
w(f"| Shared with Leonard and Arthur as editors | MET | run-4 · call 133–134 |")
w(f"| Settle each Linear issue + a line on each | MATERIAL_FAIL on one issue (ENG-2474 left open, comment says Requested) | run-4 · call {WR[4]['c2474']} |")
w(f"| Reply with two totals and the clashes | MET totals; extra Helpshift clash (contested, §7) | run-4 · call {WR[4]['reply']} |")
w("\nBand **3** (one consequential failure — the CodeRabbit chain, a single root cause repeated in the register, the state and the comment — with a "
  "bounded correction). Not 4: there is no second independent material failure; adjoe is a minor extra row whose cost leaves both totals unchanged. "
  "Not 2: the ENG-2474 state and the register status are wrong writes, not wording. This matches /hardness r1 NON-FAIL.\n")

w("## 4 · Designed-difficulty register")
w("Counts are out of 6 completed rollouts. Each citation is the first call in that run that returned the resolving record (keyword match in the tool "
  "result; `hardening/cite.py`), or the write that shows the outcome.\n")
w("| T | Wrong reading designed | Verdict | LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED | Evidence (run · call) |\n|---|---|---|---|---|")
LANDED = {'T13': (6, f"wrote Requested and left ENG-2474 open: " + ", ".join(f"run-{n} · call {WR[n]['c2474']}" for n in range(1, 7))),
          'T19': (1, f"run-5 kept iPostal as a row: run-5 · call {WR[5]['sheet']}; ENG-2466 not Canceled (run-5 · call {WR[5]['c2466']})")}
for t in man['traps']:
    tid = t['id']
    c = cites[tid]
    cit = ", ".join(f"run-{n} · call {c[str(n)]}" for n in range(1, 7) if c.get(str(n)))
    wr = (t.get('expected_wrong_reading') or '').replace('|', '/')[:120]
    if tid in LANDED:
        k, ev = LANDED[tid]
        w(f"| {tid} | {wr} | LANDED | {k} · 0 · {6 - k} · 0 · 0 | {ev}; resolving record read at {cit} |")
    else:
        w(f"| {tid} | {wr} | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: {cit} |")
w("| E1 (emergent) | adjoe added from the UA line (stopped June 2025, rule 2) | LANDED | 1 · 0 · 5 · 0 · 0 | run-4 · call 105 (AD_SPEND_DAILY adjoe last 2025-06) then run-4 · call 131 sheet row |")
w("| E2 (emergent) | Helpshift \"no export\" listed as a third clash | CONFOUNDED (fairness: contested reading) | 0 · 3 · 3 · 0 · 0 | run-1 · call 215, run-4 · call 208, run-6 · call 205 |")
w("| E3 (emergent) | ElevenLabs by-when Jul 7 (prepaid to Jul 9 → Jul 8) | LANDED (minor) | 1 · 0 · 5 · 0 · 0 | run-2 · call 154 |\n")
w("Verdict totals: LANDED 2 designed (T13 6/6, T19 1/6) + 2 emergent · LEAKED 23 · CONFOUNDED 1 emergent · BYPASSED 0 · NOT-REACHED 0.\n")

w("## 5 · Per-rollout ledgers")
w("Full call-by-call ledgers (every input and the first 300 characters of every result) were built with `hardening/ledger.py` and read before any verdict. "
  "Shape shared by all six runs:\n")
w("| Phase | Calls (typical) | What came back | Decision |\n|---|---|---|---|")
w("| #winddown read + the one reply thread + keep-list thread | 1–7 | ask, keep list, Gusto reply, card moves, Feb 11 Slack plan, Leonard's action items | builds the keep/move/clash inputs |")
w("| Linear project + 45 issues; Drive conventions doc + Wind Down folder | 8–17 | project rule, 45 issues (with `links`), rules 1–10 | applies the doc as a recipe |")
w("| Gmail Sunset/SVB, calendar, card-terms hunt (Gmail, Drive, Slack, Confluence) then Trello | 18–130 | Sunset thread + correction, review call Mar 12, SVB card | 20–40 calls spent hunting the card terms before Trello |")
w("| P&L sheets, Snowflake ledger + AD_SPEND_DAILY | ~40–110 | costs tab, Jan/Feb ledger lines | adds Meta, AppLovin, ElevenLabs |")
w("| 45 × linear_list_comments | ~35–80 | every owner figure, date and status statement | register values copied from comments |")
w("| vendor Gmail sweeps (OR-queries of every vendor name) | ~90–130 | receipts, Lucidchart/Google Ads notices, iPostal, Figma, Layer | statuses and prepaid periods |")
w("| writes: sheet, 2 shares, 25 states, 45 comments, reply | last ~80 | — | — |")
w("\nNever called by any run: any `github_*` tool, `trello_get_comments` / `trello_get_card_actions`, `linear_get_attachments`, `confluence_list_comments`. "
  "Slack outside #winddown was reached only by keyword search (run-1: SVB, card, terms, statement, bank, cancel*, coderabbit, subscription; run-6: cancel*, "
  "coderabbit, cursor, subscription; runs 2–5: SVB/card/statement, coderabbit, adjoe, elevenlabs, pond5, ipostal, meta ads).\n")

w("## 6 · Friction, tool-defect and horizon checks")
w("Friction: none configured (`03_Error_Async_Config.txt`), none observed. Unconfigured tool defects: `slack_read_channel` on #winddown exceeds the "
  "result limit in every run (run-1 · call 3) and the agent re-reads the spilled file with Bash; no outcome changed. Horizon: 205–230 calls, all "
  "before the final reply; about 115 of them are the per-issue Linear reads and writes.\n")

w("## 7 · Verifier sanity (B3e)")
w("No verifier output exists yet. Pre-checks for when it does: (a) E2 — the Helpshift export request is not on Sunset's account list, but rule 10's "
  "\"Sunset's list\" can be read to include it; a rubric row that fails a run for naming it as a third clash would be contested (route to "
  "`/create-rubric-writing`: grade the two clashes affirmatively, do not fail an extra). (b) Closed rows in runs 2 and 5 omit the source rule 5 asks "
  "for (\"say where\") — genuine, rule-incorporated.\n")

w("## 8 · Why Opus passed")
w("| Mechanism | Class | Evidence |\n|---|---|---|")
w("| Every register value is stated in the issue's own Linear comment (cost, date, status, owner hand-off) | universe leak (answer co-located with the work item) | 45 × linear_list_comments, e.g. run-1 · call 36 ($150 a month) |")
w("| The conventions doc spells out all 10 decision rules; the agent applies it mechanically | genuine capability on a recipe | run-1 · call 16 |")
w("| Sunset's correction sits in the same Gmail thread the first search opens | universe leak (correction met with the claim) | run-1 · call 22 |")
w("| Trap decoys (Sherwood, old SVB card, Arthur's sheet) are named as superseded in records read first | universe leak | run-1 · call 5, call 9 |")
w("| Gmail is swept with one OR-query of every vendor name, so any vendor email is found | genuine capability | run-3 · call 127, run-6 · call 80–85 |")
w("| 70 of ~180 graded writes (states + comments) restate register cells, so one correct register passes ~40% of the weight | score shape | §2 model |")
w("\nScore shape (B3b): **uniform success** (avg ≈ 95%, SD 0.024) — rules stated in the place Opus reads first, mechanical cohort, one rarely-opened source (GitHub).\n")

w("## 9 · Purge list")
w("| Node | Verdict | Why it adds nothing | Action |\n|---|---|---|---|")
for k, why in [("ENG-2441 OpenAI, 2443 Unity Asset Store, 2444 Veed, 2445 Kling, 2446 Hailuo, 2447 JetBrains, 2450 Adobe, 2452 Dailybot, 2453 Solsten, "
                 "2463 Calendly, 2472 Office 365, 2480 Notarize, 2481 UA Assets, 2470 Fondo, 2471 Insurance (15 issues)",
                 "each comment states its own exclusion reason in plain words; 6/6 runs Canceled all 15 (T17 LEAKED); 90 always-pass rows of state + comment")]:
    w(f"| {k} | FALSE (trivially satisfied) | {why} | remove from the seeded project, keep Lucidchart, Google Ads, iPostal, Typecast, Intuit (live traps) |")
w("| T20 Arthur's Subscriptions sheet | FALSE | the project description says it is replaced; never used by any run | keep (cheap), not counted |\n")

w("## 10 · Candidates and selection (MODE B rebuilds)")
w("Selection rule: a rule the conventions doc already incorporates, a decisive record on a surface no run opened, returned by the natural catalog call "
  "for that surface, one end state. Projected landing = the runs whose recorded searches would **not** return the record.\n")
w("| # | Rule (anchor) | Record and surface | Coupling (rows that change) | Tool-surface proof | Projected misses | Risk |\n|---|---|---|---|---|---|---|")
C = [("H1", "rule 5 bot notice", "Cursor Bugbot comment on a Combo-Fighters PR (GitHub): Teams plan canceled Feb 12", "Cursor Requested→Closed, by Mar 4→dash, ENG-2475 Done, comment", "github_get_pull_request_comments (same call as CodeRabbit)", "6/6 (no run opened GitHub)", "same root cause as T13 — one /hardness cause"),
     ("H2", "rule 5 in-app/bot notice", "Unity build-service bot in #builds (public, existing bot traffic): org subscription terminated, seats end Feb 28", "Unity Requested→Closed, by Feb 18→dash, ENG-2438 Done, comment", "slack_search_public_and_private \"unity\" / read #builds", "4/6 (runs 1, 6 searched cancel*/subscription)", "Arthur's comment must not contradict"),
     ("H3", "rule 5 bot notice", "1Password app message in #engineering-bots: Teams subscription canceled, access to Mar 8", "1Password Open→Closed, by Mar 7→dash, ENG-2479 Done, comment", "slack search \"1password\"", "4/6", "#engineering-bots is now mostly human traffic; coherence check"),
     ("H4", "rule 5 vendor notice", "AWS account-closure notice via the AWS chatbot integration in Slack", "AWS Open→Closed, by Feb 28→dash, ENG-2455 Done, comment", "slack search \"aws\"", "4/6", "usage billing after closure; ledger Feb line must stay coherent"),
     ("H5", "rule 5 vendor email equivalent", "AppLovin rep in the existing #applovin_ shared channel: ad account closed Feb 13 after final spend", "AppLovin Open→Closed, by Feb 28→dash (no issue)", "slack search \"applovin\"", "4/6", "register-only (2 rows)"),
     ("H6", "\"SVB's card terms\" (named in the ask)", "Leonard's comment on the SVB Trello card: closure moved to Feb 18, keep-rows off the card by EOD Feb 17", "Intuit, Workspace, Slack by Feb 19→Feb 17 + their 3 comments", "trello_get_comments on the card; trello_search returns matching comment actions", "2/6 (runs 4, 6 never searched \"SVB\" in Trello)", "natural text includes \"SVB\", so 4 runs may see it"),
     ("H7", "rule 6 + SVB terms", "same Trello comment also says recurring charges after the closure go to collections; conventions rule 6 changed to \"the day before the next charge or SVB's deadline, whichever is first\"", "by-when of 11 non-Closed Cancel rows → Feb 17 + 9 comments", "as H6", "2–4/6", "changes the conventions doc and every by-when the OEs state; largest single lever")]
for c in C:
    w("| " + " | ".join(c) + " |")
w("\nRejected: a thread reply in #winddown (every run opened every thread with replies: run-1 · call 6–10); Linear attachments (shown in `list_issues` "
  "`links`, run-2 · call 11); Google Doc comments (no catalog tool — unreachable); a Sunset update outside Gmail (Sunset's email pins changes to its thread: "
  "\"If our engineers change anything on this list, we'll reply on this thread\" — a Slack update would be unincorporated); new costs-tab lines (base "
  "xlsx cannot be changed).\n")
w("Projection (`hardening/proj2.py`, landing sets as in the table):\n")
w("```\n" + P1.splitlines()[0] + "\n" + "\n".join(P1.splitlines()[1:]) + "\n\n" + P2 + "\n```")
w("\n**Reading of the projection.** Hidden facts alone (A) stop at ~87%. Purging the 15 trivially-satisfied issues (B) and adding the SVB lever that "
  "moves every non-Closed Cancel deadline (H7) is the only fair combination that reaches the author target: **D lands at 77.9–79.8%** with runs spread "
  "71.6–93.7. It still projects SD ≈ 0.077 (Evals needs ≥ 0.1) and does not reach the Evals < 75% gate. The landing sets are inferred from the searches "
  "each run made; a run that adds one Slack keyword search can find H2–H5, so the true average could sit several points higher.\n")

w("## 11 · Routing")
w("Universe changes (planned, not yet made — this revision is plan only): purge 15 issues (§9); seed H1–H6; implement H7 by editing conventions rule 6 "
  "and adding the Trello comment. Every changed fact for the human: Cursor, Unity, 1Password, AWS, AppLovin become Closed (5 more Done issues: "
  "ENG-2475, ENG-2438, ENG-2479, ENG-2455 + ENG-2474); by-when for Intuit, Workspace, Slack becomes Feb 17; by-when for every remaining non-Closed Cancel "
  "row becomes Feb 17; the Linear project shrinks from 45 to 30 issues; totals unchanged (no row added or removed from the register).")
w("Prompt-side defects: none found that cause the ease (the prompt names sources the way the persona would; difficulty leaks from the universe).")
w("Routed observations: `/create-rubric-writing` — E2 Helpshift extra clash must not be failed; rule 5 \"say where\" is a genuine row. `/create-oe-writing` — "
  "every OE that states a changed value must be regenerated after the SQL change.\n")

w("## 12 · Self-review")
w("| Check | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |\n|---|---|---|---|---|")
SR = [("T13 LANDED", "keep", "tool: the GitHub notice was never returned, so the miss is a search gap, not judgement", "1A §3: for Opus a missed discoverable source is a genuine retrieval failure; the comment exists in SQL (`grep Combo-Fighters#38#c_1` → 1 row) and `github_get_pull_request_comments` returns PR comments; rule 5 names bot notices", "none"),
      ("T19 LANDED (1/6)", "keep", "fairness: iPostal's Jan 16 closure could be read as after the charge, so keeping it is defensible", "rule 2 'anything cancelled before Feb 9'; the closure mail (robert@harmonygames.co/1854432461283937829) is dated Jan 16 2026", "none"),
      ("E1 adjoe LANDED", "keep", "rule 3 says every account in a multi-vendor line gets a row, so adjoe belongs", "rule 2 overrides: AD_SPEND_DAILY adjoe last row 2025-06-27 (run-4 · call 105), nothing in the Jan/Feb ledger", "none"),
      ("E2 Helpshift CONFOUNDED", "keep", "it is a real clash: Leonard posted 'we don't need to export any data'", "rule 10 counts decisions Sunset's *list* undoes; the export request is outside the account list — contested, so never counted as landed", "rubric must not fail it"),
      ("E3 ElevenLabs date", "keep minor", "Jul 7 could be right if the prepaid year ends Jul 8", "receipt Jul 9 2025 annual → access to Jul 9 2026 → day before = Jul 8 (threads/00014566.json)", "none"),
      ("Projection D evidence", "report as a projection", "the D numbers are invented", "computed by hardening/proj2.py from truth.json and the graded runs (grades.json); output pasted in §10", "none"),
      ("Band 3", "keep", "band 4: CodeRabbit wrong in three places is three failures", "1A §3: one root cause repeated in state, register and comment is one cause", "none"),
      ("Band 3 vs 2", "keep", "band 2: everything core is right", "the ENG-2474 state and register status are wrong writes, not wording", "none"),
      ("Projection D", "report as a projection", "the landing sets are guesses; runs may search Slack for each vendor", "landing sets come from each run's recorded queries (§5); stated as a range and caveated in §10", "true numbers only after re-run"),
      ("Purge is tuning", "keep", "deleting 15 issues to move the average is gate-4 tuning", "B5 purges FALSE nodes (trivially satisfied, 6/6); no criterion is deleted or re-weighted — the universe is made leaner", "none"),
      ("H7 fairness", "flag", "changing rule 6 makes SVB govern Cancel rows, a second end state if the doc and card disagree", "the doc change makes the rule explicit ('whichever is first'); the card comment is by the card's author after the description — one governing version", "/prompt must re-check UGT"),
      ("Re-verified records", "done", "values carried from the dossier", "re-read via `tools/hg.py`: CodeRabbit notice only in SQL (slack search 'Final build settings' → 0 matches); #builds bot traffic and #applovin_ channel present in the base slack export; Lucidchart/Google Ads notices threads/00015599.json, 00015671.json", "none")]
for t in man['traps']:
    tid = t['id']
    if tid in LANDED: continue
    c = cites[tid]
    first = min((v, k) for k, v in c.items() if v)
    live = "never live in practice (resolved before any wrong reading could form)" if first[0] <= 9 else "live: the resolving record was met only after the agent had the claim"
    SR.append((f"{tid} LEAKED", "keep" if first[0] > 9 else "keep, behaves as FALSE",
               f"the trap was never live, so it is FALSE not LEAKED ({(t.get('expected_wrong_reading') or '')[:60]})",
               f"resolving record returned at run-{first[1]} · call {first[0]} (earliest), all six runs: " + ", ".join(f"run-{n} · call {c[str(n)]}" for n in range(1, 7)) + f" — {live}",
               "none"))
for s in SR:
    w("| " + " | ".join(s) + " |")
w("\nNeighbouring band argued above (3 vs 4, 3 vs 2). Unresolved: whether the projected landing sets hold, and H7's UGT check at /prompt.\n")

w("## 13 · Next steps")
w("1. Decide on the plan (the human): D projects 77.9–79.8% average but SD ≈ 0.077 and does not meet the Evals < 75% gate; A/B/C stay above 80%.")
w("2. If approved: `/create-injection` reads this report as the hardening request (purge + H1–H7), then `sql_lint`, `hardness_gate`, `stage_gate.py injection`, `/injection`.")
w("3. Re-run `/prompt` (UGT on H7), regenerate the OEs (`/create-oe-writing`), `/oe`, then a new pre-check and baseline; measure with `/create-difficulty`.")
open(os.path.join(TI, 'Working_Files', '01a_Hardening_Report.md'), 'w').write("\n".join(L) + "\n")
print('wrote 01a_Hardening_Report.md', len("\n".join(L)))
