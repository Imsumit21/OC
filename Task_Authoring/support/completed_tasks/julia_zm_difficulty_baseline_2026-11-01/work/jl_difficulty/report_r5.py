"""Round 5 blocks for 01a_Hardening_Report.md: inserted at the top of each section (after its heading).

Usage (from Task_Authoring-2): python3 support/task_work/jl_difficulty/report_r5.py <round-4 report> <out report>
"""
import sys

src, out = sys.argv[1], sys.argv[2]
s = open(src).read()
s = s.replace("# 01a Hardening Report — jl-zm-difficulty-baseline · rounds 1–4", "# 01a Hardening Report — jl-zm-difficulty-baseline · rounds 1–5", 1)
REPLY = "julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>"

B = {}
B["## 1 Mode, inputs and run validity"] = """**Round 5: MODE B (baseline).** Six Opus 5.5 baseline rollouts on SQL dd7536cdea3f, graded by the platform verifier on the 68-row rubric (/rubric PASS 5).

Inputs read:
- task_inputs/07_Baseline_Trajectories: trajectory-run-1 (8).json and trajectory-run-2 … trajectory-run-6.json, every tool call (parsed copies in the scratchpad, base4/run1–6.json)
- task_inputs/10_Baseline_Verifier_Results.md (the export HTML-escapes '>' as '&gt;'; rows R25 and R43 bind after unescaping a scratch copy; the saved input is unchanged)
- 04_Prompt.txt, 08_Oracle_Events.md, 09_Rubrics.json; the platform linter "Largest baseline failure signature must be at most 50%"

Inputs missing: 12_Difficulty_Stats.txt (not yet written by /create-difficulty). The gate values below come from tools/difficulty_stats.py run on file 10, not from estimates.

Run validity (B0): all six completed with a final DM (run-1 · event 3522, run-2 · event 2275, run-3 · event 2307, run-4 · event 2460, run-5 · event 2153, run-6 · event 1993); none errored; main agent and subagents on Opus 5.5; Friction: none. Content matches SQL dd7536cdea3f: every run's DM read (run-1 · event 6 … run-6 · event 6) returns Leonard's ask, and every card read returns the round-4 checklist (run-1 · event 20, run-4 · event 25).

| Rollout | Calls | Thread replies opened | Card (checklist, actions) | Notes doc | Mail thread | PR #265 review comments | Register rows | DM |
|---|---|---|---|---|---|---|---|---|
| run-1 | 1,286 | none | run-1 · event 20 | run-1 · event 27 | run-1 · event 44 | reviews only (run-1 · event 3337), no review comments | 35 (+ZOM-312) (run-1 · event 3479) | 35 / 22 Live / 9 Editor only, keys listed (run-1 · event 3522) |
| run-2 | 810 | none | run-2 · event 21 | run-2 · event 28 | run-2 · event 41 | read (run-2 · event 2167) | 34 (run-2 · event 2212) | 34 / 22 / 8, no keys (run-2 · event 2275) |
| run-3 | 890 | none | run-3 · event 18 | run-3 · event 25 | run-3 · event 48 | read (run-3 · event 2172) | 34 (run-3 · event 2261) | 34 / 22 / 8, no keys (run-3 · event 2307) |
| run-4 | 892 | none | run-4 · event 21, 25 | run-4 · event 30 | run-4 · event 50 | read (run-4 · event 1660) | 34 (run-4 · event 2415) | 34 / 22 / 8, keys listed (run-4 · event 2460) |
| run-5 | 853 | both (run-5 · event 19, 21) | run-5 · event 31 | run-5 · event 38 | run-5 · event 50 | read (run-5 · event 2078) | 24, all right (run-5 · event 2118) | 24 / 16 / 4 / 3 / 1, keys (run-5 · event 2153) |
| run-6 | 765 | none | run-6 · event 19 | run-6 · event 27 | run-6 · event 41 | read (run-6 · event 1887) | 34 (run-6 · event 1951) | 34 / 22 / 8, keys listed (run-6 · event 1993) |

Every run read the code (TierManager.cs: run-1 · event 3409, run-5 · event 553), the enrage sheet and ZOM-42; the Rules in force tab, shares other than Brian, the 9 required comments and the ZOM-254 → ZOM-282 line were right in all six.

"""
B["## 2 Gate status, projection and mechanism weight share"] = """**Round 5 baseline gates** (tools/difficulty_stats.py on 10_Baseline_Verifier_Results.md, platform view = valid view, no corrections):

| Gate | Value | Verdict |
|---|---|---|
| errored runs | 0 of 6 | PASS |
| pass@1 | 1/6 (run-5) | PASS |
| average weighted pass | 77.1% (76.2 / 66.9 / 66.9 / 76.2 / 100 / 76.2) | FAIL (< 75%) |
| per-rollout SD | 0.111 | PASS (band edge) |
| failure patterns | 2; largest 60% of 5 failing (run-1, run-4, run-6) | FAIL (signature over-concentrated) |
| horizon | golden run 832 counted calls | PASS |

**Clean average:** 77.1%, the same. No CONFOUNDED criterion: the verifier matches the trajectories on every row (§7), and no all-fail row exists.

**Mechanism weight share:** 38 of 160 (24%) depends on the thread replies (R5–R7, R39, R52–R55), plus 13 on the DM keys for runs that also skip them. Every other row passed in all six runs. Below the ~30% floor (Hardness_Mastery §11, NF2), so even 5 of 6 landed misses leave the average at 77%.

**Concentration:** one carrier (Slack thread replies) drives every failure. Runs either open every thread (run-5 · event 19, 21) or none, so both thread levers (L1, L7) cascade into the same rows: pattern 1 = run-1/4/6, pattern 2 = run-2/3 (pattern 2 adds the keys the L1 reply asks for).

**Round 5 projection** (Monte Carlo over the per-run habits observed here: thread miss pT, Gmail reply miss pG, review-comment miss 0.17, keys omitted 0.4 when the thread is missed; scratchpad rub/mc5.py), with the two round-5 levers and their planned rows:

| pT / pG | Projected average | P(avg < 75%) | P(largest pattern ≤ 50%) |
|---|---|---|---|
| 0.5 / 0.5 | 72.4% | 0.66 | 0.94 |
| 0.6 / 0.5 | 69.8% | 0.79 | 0.92 |
| 0.33 / 0.6 | 75.1% | 0.50 | 0.96 |
| 0.8 / 0.5 | 64.3% | 0.96 | 0.91 |

Lever-dependent weight rises from 24% to about 45%: the Gmail reply now decides the Editor only statuses (4 status rows, 4 key rows, 4 comments, the counts) and ZOM-199's comment, and the thread reply decides the build numbers in 7 comments.

"""
B["## 3 Predicted /hardness band"] = """**Round 5.** A run that misses both carriers (Slack threads and Blake's reply) keeps 10 extra rows, marks the attack-power editor tickets Live, misses ZOM-199's comment, writes Brian as editor and sends Leonard wrong counts and keys: material failures across the result → band 4. A run that misses one carrier → band 3 (one consequential failure family). A run like run-5 that opens both → band 2. Not band 5: the Rules tab, shares and the replaced-by line stay right in every observed run.

"""
B["## 4 Designed-difficulty register (verdicts)"] = """**Round 5 (6 baseline rollouts on dd7536cdea3f).** Counts LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED out of 6:

| Node | Records | Verdict | Counts | Evidence |
|---|---|---|---|---|
| T22 thread reply under the ask (L1) | D05HB64NMQU/1759262838.442871 | LANDED 5 / LEAKED 1 | 5·0·1·0·0 | no thread call in run-1 · event 6 … run-6 · event 6; run-5 · event 19 read it |
| T28/T29 reply under Julia's Sep 29 question (L7) | D05HB64NMQU/1759267002.665190 | LANDED 5 / LEAKED 1 | 5·0·1·0·0 | Brian shared as editor run-1 · event 3486 … run-6 · event 1959; run-5 · event 21 read it, Brian commenter run-5 · event 2129 |
| T26 'not tiers' review comment (L5) | match3d#265#rc_7 | LANDED 1 / LEAKED 5 | 1·0·5·0·0 | run-1 · event 3337 read reviews only (empty body) and kept ZOM-312 (run-1 · event 3479); run-2 · event 2167 read the comment |
| T27 notes doc (L6) | f_f494073fc667097c3c2c6b | LEAKED | 0·0·6·0·0 | run-1 · event 27 … run-6 · event 27; Arthur reader and ZOM-258 off in all registers |
| T23 checklist (L2) | 68dc033bf7d24e86b8a9cc67 | LEAKED | 0·0·6·0·0 | run-1 · event 20 get_card checklists all; Editor only / Not shipped comments in all runs (run-1 · event 3493) |
| T6 reply in the store-builds thread (> 90) | """ + REPLY + """ | LEAKED | 0·0·6·0·0 | run-1 · event 44 get_thread returned both messages; ZOM-199 comment in all runs |
| T30 (new) Blake's reply in its own thread | """ + REPLY + """ | NOT-REACHED (new) | 0·0·0·0·6 | absent from the baseline universe; the habit: every run opened only the first 'store builds' thread from an id-only search (run-2 · event 35 → 41) |
| T31 (new) build numbers in the Editor only / Not shipped comments | D05HB64NMQU/1759262838.442871 | NOT-REACHED (new) | 0·0·0·0·6 | absent from the baseline universe; rides the L1 thread (run-5 · event 19 is the only thread read) |

"""
B["## 5 Per-rollout ledger (run-1)"] = """**Round 5 ledger (run-1, the largest run; the others differ only where §1 says).**

| Step | Tool | Input | What came back | Decision | Rubric(s) |
|---|---|---|---|---|---|
| run-1 · event 6 | slack_read_channel | DM D05HB64NMQU | the ask (reply_count 1) and Julia's Sep 29 question (reply_count 1) | no thread call | R5–R7, R39, R52–R55 |
| run-1 · event 20 | trello_get_card | card, checklists all, actions all | rules 1–7, checklist, attack-power comment | applied all | R5, R45–R51 |
| run-1 · event 27 | gdocs_get_document_text | notes doc | ZOM-258 off, Arthur view, which replaced which | applied | R41, R65 |
| run-1 · event 36 → 44 | gmail_search_messages → gmail_get_thread | "store builds" (ids only) → the first thread | the mail and Blake's reply | > 90, editor/debug stripped | R13–R16, R43 |
| run-1 · event 3337 | github_get_pull_request_reviews | #265 | empty-body COMMENTED reviews | no review-comment call; kept ZOM-312 | R5, R7, R52 |
| run-1 · event 3479 | gsheets_values_update | Tickets tab | 35 rows | — | R5–R7 |
| run-1 · event 3486 | gdrive_share_file | brian.foster | writer | checklist's rule 7 change | R39 |
| run-1 · event 3493 … | linear_create_comment | 14 tickets | — | incl. ZOM-162/163/201/250/312 | R52 |
| run-1 · event 3522 | slack_send_message | DM | 35 / 22 / 9 / 3 / 1 + keys | — | R53–R55 |

"""
B["## 6 Friction, tool-defect and horizon checks"] = """**Round 5.** Friction: none configured. Tool defects: the first two trello_get_card calls in every run failed on the attachments flag ('attachments must be true, false, or "cover"', run-1 · event 16, 18) and the runs retried (run-1 · event 20); no outcome changed. Horizon: counted calls 1,204 / 762 / 864 / 719 / 832 / 738 (difficulty_stats), golden run 832: PASS. The round-5 change adds about 2 Gmail calls (search for the reply, open it).

"""
B["## 7 Verifier sanity"] = """**Round 5.** The platform verifier matches the trajectories on every row: its fails are exactly the replay's (run-1, run-4, run-6 fail R5, R6, R7, R39, R52–R55; run-2, run-3 add R58–R64). Six verifier titles differ from 09_Rubrics.json only by link markup on emails and '&gt;' escaping; no judge text concedes a fact and still fails it. No all-fail rubric. No collapsed run (lowest 66.9%, median 76.2%).

"""
B["## 8 Why Opus passed"] = """**Round 5.** Every pointed source was opened by all six runs: the card with checklists and actions (run-1 · event 20), the attached notes doc (run-1 · event 27), the store-builds thread (run-1 · event 44), PR reviews (run-1 · event 3337), all ZOM comments, the code (run-1 · event 3409). The only habit that varied is opening Slack thread replies (run-5 · event 19 vs none elsewhere), and it is all-or-nothing per run, so both thread levers fail together. Class: genuine capability on every reachable rule; the single landed carrier is A14 (Slack replies). The fix is a second, independent carrier whose miss changes graded values (not only counts).

"""
B["## 9 Purge list"] = """**Round 5.** No node purged. T6 (reply in the same thread) was LEAKED 6/6 because get_thread returns the whole conversation; it is rebuilt as T30 (the reply in its own conversation), not deleted.

"""
B["## 10 Candidates and selection (rebuild)"] = """**Round 5 candidates.**

| # | Candidate | Evidence | Selected |
|---|---|---|---|
| 18 | Blake's reply in its own Gmail conversation (subject changed), carrying the editor/debug stripping rule and both ZOM-199 corrections; card rule 3 names the reply | gmail_search_messages returns ids only (run-2 · event 35); every run opened only the first thread (run-1 · event 44), 2 of 6 opened any other thread (run-2 · event 54); A14: 41/60 Gmail runs never opened a thread | yes (L8, T30) |
| 19 | Leonard's thread reply asks the Editor only / Not shipped comments to name the two builds | A21 per-surface output rule in an incorporated source; adds 7 positive rows to the thread carrier | yes (L9, T31) |
| 20 | a closed-unmerged PR for a Done member (never merged → Not shipped) | every run lists all match3d PRs with merged state (run-1 · event 3337 area; list_pull_requests state=all); a new PR number breaks the 1..544 sequence | no |
| 21 | a title-match ticket on the Aug 31 PT/UTC edge | no base ticket in 2025-09-01 00:00–07:00Z; ZOM-509 (Aug 28) → ZOM-510 (Sep 1): a new number would break Linear's sequence | no |
| 22 | Blake marks ZOM-307 (Easy Quantity slider, #243) as tier work in a review comment | #243 removed the field 'throughout the app': Editor only vs Live is arguable (two end states) | no |
| 23 | Blake flags ZOM-300 ('Randomized') or ZOM-282 ('+50%') as wrong | GameLoader.cs calls RemoveRandomObjects (ZOM-300 is right); enrage values live in prefabs, not code | no |
| 24 | Leonard adds cancelled editor tickets ZOM-309 / ZOM-197 to the list | contradicts his own cut ('they don't change how hard a level plays') | no |
| 25 | another 'not tiers' review comment | only moves counts, which thread-missers already fail: no pattern split | no |

**Lazy solver (round 5).** DM read, card, notes doc, 'store builds' search → first thread, code, sheet, invite: 34 rows, the attack-power editor tickets judged from titles, no ZOM-199 comment, comments without build numbers, Brian editor. Fails L1, L7, L8 and L9.

**A5b check.** Incorporated: rule 3 and rule 6 name 'his reply to it'; the L1 thread is part of the ask. Survives retrieval: the reply's rule must still be applied per ticket (ZOM-45 and ZOM-303 stay Live; ZOM-277, ZOM-315 are editor stats panel work). Tool surface: gmail_search_messages 'from:arthur.blake@harmonygames.co' or 'ZOM-199' returns the reply; gmail_get_thread on its thread id returns it. Graded weight: about 45% lever-dependent after the rubric update.

"""
B["## 11 Routing"] = """**Round 5 universe changes** (01_Universe_Inject.sql dd7536cdea3f → 7966b1496ad9; 175 → 180 rows; script support/task_work/jl_difficulty/harden_r5.py):

| Statement(s) | Change |
|---|---|
| gmail_messages """ + REPLY + """ and its 4 mailbox copies | thread_id → its own conversation (julia: julia.lawson@harmonygames.co/1844695547248825769), subject 'editor stuff and ZOM-199, before Monday', body: the stripping rule + ZOM-199 is wrong on '>= 90' and on '10 levels' (the code: > 90 when the 10th game ends, wins and losses) |
| gmail_threads (5 new) | one row per mailbox for the reply's conversation |
| gmail_messages <CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> (5) and their thread rows | stripping paragraph removed; thread snippets show the first mail |
| trello card 68daca5871dba40417a00383 desc + updateCard action 68dbe36f4b2b4fffb7525fde | rule 3: 'Blake's store builds mail and his reply to it.' |
| slack D05HB64NMQU/1759262838.442871 | adds: 'and when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against' |

Re-passed: sql_lint 0 errors; base_check PASS; fact_check PASS (8 facts); persona_view check-sql PASS; hardness_gate (long) PASS; stage_gate injection PASS. Manifest: K5, K14, T5, T6, T7, C3 updated; T30, T31, C14 added (manifest_r5.py). Dossier: round-5 section, facts for the human (dossier_r5.py).

**Facts changed (for the prompt, OE and rubric):**
- The answer key is unchanged: 24 rows (16 / 4 / 3 / 1), 9 comments, same shares, same DM counts and keys.
- Statuses: the editor/debug rule now comes from Blake's reply (own thread), not the first mail.
- ZOM-199's comment carries both corrections: > 90, and checked when the 10th game ends (wins and losses).
- The 7 Editor only / Not shipped comments each name iOS 0.3.49 and Android 0.3.133.

**Prompt-side defects:** none. The prompt is unchanged; /prompt re-runs because card rule 3 changed.

**Routed observations:** /create-oe-writing (the reply's search and read become their own events; comment payloads add the builds; status evidence cites the reply) and /create-rubric-writing (new rows: build numbers in each of the 7 comments, ZOM-199 comment '10 games'; evidence on the status rows cites the reply).

"""
B["## 12 Self-review"] = """**Round 5 counter-readings.**

| Verdict | Strongest counter-reading | Resolution (pointer) | Unresolved |
|---|---|---|---|
| T22 LANDED 5 | tool: the DM read did not return reply counts | run-1 · event 6 returned reply_count 1 on the ask; run-5 · event 19 shows slack_read_thread works on the same ts | none |
| T28/T29 LANDED 5 | fairness: the checklist's 'Brian gets edit' is a second valid end state | Leonard's later reply (Sep 30 21:16Z) takes it back; /prompt PASS 5 and /rubric PASS 5 accepted one end state | none |
| T26 LANDED 1 | tool: run-1's review call did not expose the inline comment | the review-comments call exists and returned it in run-2 · event 2167; run-1 never made it | none |
| T27, T23, T6 LEAKED 6 | the traps were never live | all three were read and applied (run-1 · event 27, 20, 44); live but solved, not FALSE | none |
| T30 (new) | fairness: a reply in another conversation is unfindable or not 'his reply' | In-Reply-To/References name the first mail; rules 3 and 6 name the reply; 'from:arthur.blake@harmonygames.co' and 'ZOM-199' searches return it (re-verified in the SQL) | catch rate unmeasured (projection pG 0.3–0.7) |
| T31 (new) | padding: the build numbers are an extra deliverable | it is content of a required write, asked by the requester in his ask's thread (A21) | none |
| Band (4 for a both-miss run) | neighbouring band 3 | two independent consequential families (row set and statuses), not one bounded correction | none |

Re-verified through tools/hg.py and the SQL: TierManager.cs 'totalGames == 10' and 'cpm > 90.0f', WinHistory.cs wins + losses (the reply's claims); Assets/Scripts/LevelEditor and Assets/Scripts/Debug exist; GameLoader.cs RemoveRandomObjects (ZOM-300 rejected); match3d PR numbers 1..544 with no gaps (candidate 20 rejected); ZOM-509 2025-08-28 and ZOM-510 2025-09-01T14:56Z (candidate 21 rejected). Mechanical checks re-run after the SQL change: sql_lint 0 errors, hardness_gate PASS, stage_gate injection PASS. Clean average recomputed with tools/difficulty_stats.py on the verifier matrix: 77.1%.

"""
B["## 13 Next steps"] = """**Round 5.**
1. /injection on SQL 7966b1496ad9 (paste task_inputs/01_Universe_Inject.sql), then /prompt (card rule 3 changed; the prompt text is unchanged).
2. Re-inject on the platform, then /hardness on a fresh Opus run.
3. Run the six baseline rollouts and the verifier on the updated rubric.
4. /create-oe-writing (ledger, events, check) and /create-rubric-writing (plan, draft, check) for the round-5 facts, then /oe and /rubric.
5. /create-difficulty on the new verifier results.

"""
for head, block in B.items():
    i = s.find(head)
    assert i >= 0, head
    j = s.find("\n", i) + 1
    if "**Round 5" in s[j:j + 400]:
        continue
    s = s[:j] + "\n" + block + s[j:]
open(out, 'w').write(s)
print('ok')
