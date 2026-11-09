#!/usr/bin/env python3
"""Writes Working_Files/05_Human_Time_Worksheet.md; minutes and the character count are computed, never typed."""
import hashlib, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); W = os.path.dirname(HERE); T = os.path.dirname(W)
v1 = json.load(open(f"{HERE}/out/humantime_volumes.json")); v2 = json.load(open(f"{HERE}/out/humantime_volumes2.json"))
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
builds = v1["#builds C05433XK267"]["in_window"]
others = (v1["#god-bugs C05V5FNLB9V"]["in_window"] + 2) + (v1["sub-250 C09Q4S613CN"]["in_window"] + 2) + v1["publishing C09SWTHEMEW"]["total"] + (v1["Arthur DM D05S1S2AB5M"]["in_window"] + 1) + (v1["Marcus DM D05USBTQY1F"]["in_window"] + 1) + (v1["Brian DM D07E9PSQB6W"]["in_window"] + 1)
canvas = v1["canvas CE156FDFB428"]["total"] + 10
inbox = v2["owen_gmail_ids_window"] + 2
open_eng = v2["linear_eng_open"]; prs = v2["dd_prs_since_nov1"]; cards = v2["dd_board_pointers"]["cards"] + 1; posts = v2["god_bugs_top_level_real"]; ui_prs = v2["ui_prs"]
assert (builds, others, canvas, inbox, open_eng, prs, cards, posts) == (3890, 875, 286, 116, 115, 35, 217, 22), (builds, others, canvas, inbox, open_eng, prs, cards, posts)
R = [
 ("Read Arthur's DM and what it points to: the DM, the carry-over notes doc, his later change on ENG-2401, the review invite, the carry-over folder, the UI deck, the UI sheet and the Trello card with its 28-item checklist", "read", "8 records", "5 min each", 40),
 ("Find the UI work card by scanning the DD Product Roadmap board", "read", f"{cards} cards ({cards-1} base + 1 seeded)", "≈ 450 items/h (triage by title)", 29),
 ("Skim #builds for Nov 1, 2025 to Feb 13, 2026 PT: build numbers, branches, what was switched off", "read", f"{builds:,} messages (C05433XK267)", "≈ 3,000 messages/h", 78),
 ("Skim the other DD conversations: #god-bugs from the canvas's start, the sub-250 channel, the publishing channel, and Owen's DMs with Arthur, Marcus and Brian", "read", f"{others} messages (C05V5FNLB9V 127, C09Q4S613CN 276, C09SWTHEMEW 275, D05S1S2AB5M 24, D05USBTQY1F 25, D07E9PSQB6W 148)", "≈ 3,000 messages/h", 18),
 ("Triage Owen's inbox for Nov 1, 2025 to Feb 13, 2026 PT", "read", f"{inbox} threads (114 base + 2 seeded in owen.baker@harmonygames.co)", "≈ 450 items/h (triage by sender and subject)", 16),
 ("Scan the open Engineering tickets for ones that already cover a bug", "read", f"{open_eng} open ENG tickets of 2,331", "≈ 450 items/h (triage by title)", 15),
 ("List the GameOfDominoes PRs opened since Nov 1", "read", f"{prs} PRs ({ui_prs} of them UI pass PRs)", "≈ 450 items/h", 5),
 ("Work out which line the public build came off and which fixes reached it", "read", "1 build (0.3.310), 7 Slack posts naming its branch, 2 lines compared", "≈ 40 min (the worked example's 'find a handful of PRs and confirm what each contains')", 40),
 ("Sort the #god-bugs posts after the canvas's last line into bugs, follow-ups, design questions and QA-doc pointers", "read", f"{posts} top-level posts, 79 replies, 7 turn out to be bugs", "2 min each (classify in a sweep)", 44),
 ("Per bug: read the line or post with its thread, compare it with the skim notes, call the outcome under the notes doc", "read", f"70 items: 63 canvas lines ({canvas} messages) + 7 posts", "5 min each, between the 2 min sweep rate and the 8 min cross-surface rate: one thread and the notes, the second surface only on the traps, which have their own lines", 350),
 ("Per open UI child: ticket, PR, review, inline comments and Linear notes, then the call under the tree rule", "read", "19 open children", "8 min each (low end of the cohort-record anchor 8–15 min)", 152),
 ("Done children and sub-masters: read each to say where it landed", "read", "9 Done children + 3 sub-masters", "3 min each (one ticket, no decision)", 36),
 ("T_INLINE_TD ENG-2434 looks finished (#1905 merged, ticked, deck says shipped) until an inline review comment holds it", "dead end", "4 records", "15 min", 15),
 ("T_WINGS ENG-2424 looks like the other merged children until a later post shows the screen switched off", "dead end", "1 post", "10 min", 10),
 ("T_INLINE_AXE ENG-2426 looks finished until an inline comment on #1908 holds it", "dead end", "3 records", "15 min", 15),
 ("T_SEASON the deck says the pass wrapped up until Oliver's note on ENG-2428", "dead end", "2 records", "10 min", 10),
 ("T_REPLY the shop icons tick looks settled until a reply under an unrelated sub-250 post", "dead end", "2 records", "10 min", 10),
 ("T_BACK the Tavern buttons tick and Brian's fix look settled until Marcus's 1:1 note", "dead end", "2 records", "10 min", 10),
 ("T_GONE the unticked lives lines look still broken until the BoomBit post, the economy doc and the no-lives note", "dead end", "3 lines, 3 records", "15 min", 15),
 ("T_LINE the tile dozer window looks fixed until #1913 turns out still open and outside the build", "dead end", "2 records", "15 min", 15),
 ("T_ELSE_FLICKER the flicker thread stops at 'testing a fix' until Robert's reply elsewhere", "dead end", "3 records", "15 min", 15),
 ("T_ELSE_MUSIC the music line looks open until Brian's DM", "dead end", "2 records", "5 min", 5),
 ("T_ELSE_ACID the acid delay looks open until the same DM", "dead end", "2 records", "5 min", 5),
 ("T_ALIAS_APPLE the Apple sync line has no ticket in its own words until Vincent's mail names ENG-2073", "dead end", "3 records", "15 min", 15),
 ("T_ALIAS_SPLASH the manual sign-in line has no ticket in its own words until Vincent's note on ENG-2363", "dead end", "2 records", "10 min", 10),
 ("T_FILT the canvas looks like the whole list until the notes bring in later posts", "dead end", "2 records", "5 min (the post sort has its own line)", 5),
 ("T_FOLLOW any line on a child looks enough until Brian's closing rule", "dead end", "1 comment", "5 min", 5),
 ("D_ZMCANVAS the ZM canvas opened as part of the job", "dead end", "1 canvas channel", "5 min", 5),
 ("D_SIGNIN ENG-2280 read as the Apple sign-in ticket", "dead end", "1 ticket", "5 min", 5),
 ("D_LIVESTICKETS the open lives tickets read as covering those lines", "dead end", "2 tickets", "5 min", 5),
 ("D_ZMDOC the ZM notes read as the rule for ticks and close-outs", "dead end", "1 doc", "5 min", 5),
 ("D_SUB250 Robert's sub-250 reports read as extra bugs", "dead end", "1 report thread in a 276-message channel", "10 min", 10),
 ("D_DECK the wrap deck read as proof the UI work finished", "dead end", "1 deck", "5 min", 5),
 ("D_ECONCANVAS the economy canvas opened as part of the list", "dead end", "1 canvas channel", "5 min", 5),
 ("Redo the calls a later record overturns (shop icons, Tavern buttons, flicker, music, acid, 3 lives lines)", "re-read", "8 calls", "2 min each", 16),
 ("Recheck the title format against Arthur's later change on the master ticket", "re-read", "1 comment, 68 planned titles", "5 min", 5),
 ("Tally the reply figures from the sheet and the tree", "read", "70 rows + 28 children, 3 figures", "10 min", 10),
 ("File the new tickets: pasted title, Engineering team, Bug label, parent, state", "write", "68 tickets", "3 min each, under the 5–10 min tailored-write anchor because the title is copied and the description stays empty", 204),
 ("Add the canvas wording as a note on the two existing tickets", "write", "2 comments", "5 min each", 10),
 ("Move the open children that go Done", "write", "14 state changes", "1 min each (one field)", 14),
 ("Leave the line on every child, naming the build and where it landed", "write", "28 comments", "5 min each (low end of the tailored-write anchor)", 140),
 ("Create the sheet in the carry-over folder with Bug, Outcome, Ticket, Why", "write", "1 sheet, 70 rows × 4 columns", "5 min setup + 1.5 min per row", 110),
 ("Share the sheet with the review's other attendees", "write", "3 shares", "1 min each", 3),
 ("Reply in Arthur's DM thread with the numbers", "write", "1 thread reply", "10 min", 10),
]
total = sum(r[4] for r in R); assert total % 15 == 0, total; hours = total / 60
reads = {k: sum(r[4] for r in R if r[1] == k) for k in ("read", "dead end", "re-read", "write")}
trap_min = reads["dead end"]; assert trap_min == 200
cond = [
 f"- Rules: Arthur's DM, notes doc, master ticket change, invite, folder, deck, sheet, Trello card (8 records) 40 min; finding the card among {cards} on the DD board 29 min",
 f"- Slack by hand at 3,000/h: #builds {builds:,} messages 78 min; #god-bugs, sub-250, publishing and 3 DMs {others} messages 18 min",
 f"- Inbox {inbox} threads 16 min; {open_eng} open ENG tickets 15 min; {prs} PRs 5 min; which fixes reached the public build 40 min",
 f"- {posts} bug-channel posts after the canvas's last line, 2 min each 44 min",
 f"- 70 bugs (63 canvas lines, {canvas} messages, + 7 posts), 5 min each 350 min",
 "- 19 open UI children across Linear and GitHub, 8 min each 152 min; 9 Done children + 3 sub-masters, 3 min each 36 min",
 f"- 22 traps and decoys (inline review comments, the wrap deck, replies that overturn ticks, lives removed, a PR never merged, tickets named in a mail, other canvases) {trap_min} min; redo 8 calls and titles 21 min; tally 10 min",
 "- Writes: 68 tickets 204 min; 2 notes 10 min; 14 state changes 14 min; 28 child lines 140 min; sheet 70 rows 110 min; 3 shares 3 min; DM reply 10 min",
 f"- Total {total:,} min = {hours:g} h",
]
clen = len("\n".join(cond)); assert 50 <= clen <= 2000
up = total + 68 * 2; down = total - 70 * 3
o = []; A = o.append
A("# Human Time Worksheet — owen_baker_engops\n")
A("Pass: first (after the platform /prompt PASS on rev5)        Tier: Long-Horizon")
A("Universe: normal · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)")
A(f"Hours: {hours:.2f}\n")
A("Basis:")
A(f"- The work 04_Prompt.txt asks for (sha256 {sha(T + '/04_Prompt.txt')}): find Arthur's Thursday DM, carry DD's bug list into Linear the way his notes lay it out, bring the UI Changes tree up to date with a line on every child, build the sheet in Owen's carry-over folder and share it with the review, then reply in the DM thread with the numbers.")
A("- The work is done by hand in Owen's own accounts: no search, scripts or AI. Owen's today is Saturday Feb 14, 2026; windows are Pacific dates. Learning the universe from scratch is not counted.")
A(f"- Counts come from rev5 (01_Universe_Inject.sql sha256 {sha(T + '/01_Universe_Inject.sql')}; solver/truth.json, unchanged since rev1) and the platform /prompt report (run_forensics/rev5/1_prompt_PASS_r5.md): 70 bugs, 68 new tickets, 2 notes, 14 state changes, 28 child lines, 70 sheet rows, 3 shares, 1 reply.")
A("- The person does not start out knowing which records decide a call. Finding them is the skim work below, and each designed trap in 01_Hardness_Manifest.json has its own dead-end line, which costs only the extra misleading records. 03_Error_Async_Config.txt is Friction: none, so there is no workaround line.\n")
A("| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |")
A("|---|---|---|---|---|")
for r in R:
    A(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
A(f"| Total | | | | {total} = {hours:g} h |\n")
A(f"Tier check: trigger (Long-Horizon ≈ 12–24 h; {hours:g} h is {hours - 24:g} h over) → re-measured → reported risk: the number stays and the tier is not changed.")
A("- Re-measured in this run through hg.py: every Slack, inbox, Linear, GitHub and Trello volume in the table. They hold.")
A(f"- What drives it: 102 records with their own call and 112 Linear writes (68 tickets, 2 notes, 14 states, 28 lines), plus the sheet, 3 shares and the reply. Reads are {reads['read']} min, dead ends {trap_min} min, re-reads {reads['re-read']} min, writes {reads['write']} min.")
A(f"- Sensitivity, not a tuning: tickets at the 5 min anchor instead of 3 give {up / 60:.1f} h; the 70 bugs at the 2 min sweep rate instead of 5 give {down / 60:g} h. The band is 'about' 12–24 h (references/Docs/11_V3_Changes.md §4), so {hours:g} h sits at its edge, not in another tier: Super-Long is 4+ weeks and paused.")
A("- Reported risk: a reviewer could read the task as long for the tier. No scope is cut and no rate moved to fit it. The planned call budget is 285 (01_Hardness_Manifest.json call_budget) and the requester's target is over 130 counted calls per run.\n")
A("Baseline count basis (post-baseline only): n/a (first pass)\n")
A("Condensed breakdown (one line per sub-task, facts only; the human types the reasoning in their own words):")
o.extend(cond)
A("")
A(f"Condensed breakdown length: {clen} characters (field accepts 50–2,000)\n")
A("Sources measured:")
A("- hg.py search search slack '.' --file 'messages/CHANNEL/*.json' --key ts, filtered to the window, for C05433XK267 (3,890), C05V5FNLB9V (125), C09Q4S613CN (274), C09SWTHEMEW (275 whole channel), CE156FDFB428 (276), D05S1S2AB5M (23), D05USBTQY1F (24), D07E9PSQB6W (147); scan_complete true on each (plan/measure_humantime.py, plan/out/humantime_volumes.json).")
A("- hg.py search search slack with --key ts, --key thread_ts and --key subtype on messages/C05V5FNLB9V/*.json, keyed by file and pointer: 104 messages after the canvas's last line (Nov 21, 2025, 15:04 UTC), 22 real top-level posts, 3 channel_leave rows left out.")
A("- hg.py search search gmail 'owen.baker@harmonygames.co/' --file 'threads/*.json' --key id: 1,595 thread ids, 114 decoded to Nov 1, 2025 to Feb 13, 2026 PT.")
A("- hg.py search search linear 'ENG-' --key identifier and per-state --key state_id on data.json: 2,331 ENG issues, 115 not Done or Canceled; --key parent_id: 28 children, 9 Done.")
A("- hg.py search search github 'GameOfDominoes#' --key id --pointer /pull_requests with --key created_at: 1,906 PRs, 35 opened since Nov 1; 'UI Optimi' --key title: 11.")
A("- hg.py search search trello 65eb4ec525346c8070ca638f --key idBoard: 216 cards on the board.")
A("- persona_view.py search owen_baker slack boombitFixAddressables --no-hidden: 7 visible hits, 0 hidden.")
A("- 01_Universe_Inject.sql rows (rev5): content rows per conversation, membership rows left out (CE156FDFB428 10, C09Q4S613CN 2, C05V5FNLB9V 2, D05S1S2AB5M 1, D05USBTQY1F 1, D07E9PSQB6W 1); 2 of the 5 seeded threads are in Owen's mailbox; 1 seeded card on the board.\n")
A("## Self-review\n")
A("Checked in order against 10_Long Horizon Guidelines - V2.md §5 and §10, the Pre-QC 'Difficulty and submission' list and the Screen 25 field rules (0.25 step, 50–2,000 characters, pasting and copying blocked). §5: dead ends, re-reading and no universe learning are in; no workaround applies. §10 and Pre-QC ask that the estimate is justified sub-task by sub-task and adds up, which the gate re-adds; their other items are post-baseline.\n")
A("| Area | Counter-reading | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
A(f"| Inflated | The strongest case it fails: 70 per-bug checks plus 22 dead-end lines count the same reads twice, and {hours:g} h is above every earlier task | The per-bug rate is 5 min, under the 8–15 min anchor, because the second surface sits only on the trap lines. A dead-end line costs only the extra records, such as harmonygames-Games/GameOfDominoes#1905#rc_1 for ENG-2434. The re-read line covers 8 overturned calls, not all 15 that differ from the default. Tickets are at 3 min, under the 5–10 min anchor | PASS |")
A("| Solution-path estimate | It could be written as if the person already knew where the deciding records sit, such as Marcus's note D05USBTQY1F/1765452012.418229 or the mail that names ENG-2073 | The skims (3,890 + 875 messages), the inbox (116 threads), the board (217 cards) and the post sort (22 posts) come first, and every manifest trap has a dead-end line. Friction: none, so no alternate path applies | PASS |")
A("| Evaluator-wide volume | Search is evaluator-wide, so the counts could include other people's mail or channels Owen cannot read | Gmail counts only ids under owen.baker@harmonygames.co, and 3 of the 5 seeded threads are left out as other mailboxes. persona_view.py can-see owen_baker returned YES for CE156FDFB428/1763041126.468099, C05V5FNLB9V/1764329192.159229, C09Q4S613CN/1764013026.858409 C09SWTHEMEW/1764659626.614679, D05USBTQY1F/1762446184.467029 and D07E9PSQB6W/1769535189.275319, and the channel verdict is YES for D05S1S2AB5M; #builds C05433XK267 is public. Linear, GitHub and Trello are unscoped | PASS |")
A(f"| Tier mismatch | {hours:g} h is above about 12–24 h, so the scope may be too big for Long-Horizon, or the rates may be off | Volumes were re-measured in this run and hold. 11_V3_Changes.md §4 gives 'about' 12–24 h, and the next tier is 4+ weeks and paused, so the scope is Long-Horizon at the top of the band. The number was not tuned and the risk is reported in the tier check, with both sensitivities | REPORTED |")
A(f"| Linter reading | The V1 reasonableness linter sees only the prompt, the hours, the reasoning and the SQL, and a 105-word prompt could make {hours:g} h look 3× too high | The reasoning names the volumes: 63 canvas lines, 7 posts, 28 children, 68 tickets, 28 child lines, 70 sheet rows, and the SQL shows seeded records behind them (13 Linear comments on the tree and the tickets, including ENG-2401). 3× either way is {hours / 3:.1f} h to {hours * 3:.0f} h, and the sensitivities stay far inside that. No banned phrase appears, and the human writes the reasoning | PASS |\n")
A("Re-verified: every volume in the table came from this run's hg.py queries, not from the dossier. The sum and the character count are computed by plan/build_humantime.py.\n")
A("Unresolved: none blocking. The tier trigger is reported above. Refresh after 08_Oracle_Events.md and after the baseline (count basis).\n")
open(f"{W}/05_Human_Time_Worksheet.md", "w").write("\n".join(o))
print(total, hours, clen, reads, up / 60, down / 60, len(R))
