# Census C5: Opus 5.5 baseline run habits and trap catch rates

Question: on real Opus 5.5 baseline runs, how often is a hidden fact found, by the kind of place it sits in?
Written 2026-11-07. Read only from `Task_Authoring/support/completed_tasks/`. Nothing here came from a Leonard record; this is run evidence from other personas.

## Headline findings

1. FACT. Reading is the whole game. Across 59 traps with a text scan, runs read a hidden record 183 times and applied it 178 times (97%). No run applied a fact without reading it. The five exceptions are D1, D2, Q5 (twice) and V1.
2. FACT. Whether something points at the record decides more than which service it sits in. The same carrier swings from 0/18 (Douglas PR inline, unpointed) to 9/12 (Julia, a rule names the review) to 6/6 (Vincent, the ticket names the PR).
3. FACT. Unpointed traps split into two piles, not a bell: of 49, 23 landed at 0 or 1 of 6, 12 landed at 5 or 6 of 6, and only 14 landed at 2 to 4 of 6.
4. FACT. Only one task of nine got under 70 % with the SD gate passing: Douglas, 56.3 % and SD 0.117, with 44.6 % of its weight always passing. Frederick Q4 reached 71.0 % but SD 0.016, because its weight sat in rows every run failed.
5. FACT. Row multiplication at /rubric cost 6.5 to 15 points and 0.03 to 0.05 of SD on the three tasks where it could be measured well: Bridge 71.2 % to 77.7 %, Robert LLC 76.5 % to 83.6 %, Douglas 41.1 % to 56.3 %.
6. INFERENCE, UNCALIBRATED. E[avg] 62 % with SD above 0.1 needs three or four heavy traps at about 50 %, each 12 to 16 % of final weight, plus a small floor. Always-passing weight then has to be near 37 %, lower than any task here. Even with catch rates hit exactly, the simulated chance of clearing every gate is 58 to 76 %. If catch rates are left to chance it falls to 6 to 26 %.

## Scope and evidence limits

**Read:** all 60 baseline trajectories in 10 task folders (6 each), 9 verifier result files, the READMEs, the 11_AF files, the manifests, the hardening reports and the stored rubric drafts. I added `vincent_zm3d_release_gate` and `frederick_account_handover` to the priority list because both have verifier results.

**Provenance (FACT, scanned):** every assistant message in the 60 exports is `claude-opus-5-5` (or `<synthetic>`, the harness's own), and all 60 end in `result / success`. The Vincent exports in `07_` are the graded set: the tab ids the verifier quotes occur in the matching runs (spot-checked on runs 1 and 5).

**Terms used in the tables**
- **Read n/6:** runs where a tool result contains the record's own text (substring scan of the raw export). `n/r` means not scanned, because the text is generic or the fact is spread over several records.
- **Caught n/6:** runs that pass the trap's unique rows in the verifier results. A script checked every unique row of the 70 traps that have one: the row's pass set equals the stated caught set, 0 mismatches. J3 and J4 have no unique row, so they come from verifier justifications and the read scan.
- **Link:** named (the record uses the item's name or key), alias (another label for it), de-named (nothing in the text matches the item's name). No trap in this set links by amount only, so that type has n = 0.
- **Ptr:** P means a record the run reads anyway names this carrier or its container, or the fact sits on the item the run is already walking. N means nothing points at it.

**Limits. Please read these before using the rates.**
- n = 6 per trap. A true rate of 50 % reads anywhere from 2/6 to 4/6 about 78 % of the time, and the 95 % interval on a single 3/6 is about 19 to 81 %.
- Ptr is my label, assigned after seeing the outcomes. The pointed versus unpointed gap is real in direction but flattered by that.
- The 6/6 rows are a sample. Every trap that failed in any run is listed; only some of the controls are. So pooled rates for carriers with mostly pointed traps are inflated, and "Trello card comment 100 %" means "no unpointed example exists", not "always found".
- Claire has no verifier results. Its Caught column comes from a local regex grader; its Read column comes from the trajectories. Treat the six K rows as weaker.
- All personas differ from Leonard. No run in this set is on Leonard, whose mailbox the brief calls huge, so all of section D is by analogy.
- Thinking blocks in the exports are empty, so habits are inferred from calls and the short text blocks. Reasons for a choice are not visible.

## A. Per-task run statistics

Average, SD (population), passes, rows and weights recomputed from `10_Baseline_Verifier_Results.md` and `09_Rubrics.json`, and they match each README. Counted calls recomputed with `difficulty_stats.count_tool_calls`.

| Task | Mode | Average | SD pop (sample) | Full passes | Counted min / mean / max | Rows | Weight | Weight-5 share | All-fail rows (weight) | All-pass rows (weight) | Mixed rows (weight) | Patterns (largest) | SD gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| robert_llc_takeover | easy | 83.6 % | 0.103 (0.113) | 1 | 149 / 155.8 / 162 | 130 | 328 | 35.1 % | 0 (0 %) | 97 (64.9 %) | 33 (35.1 %) | 3 (40 %) | PASS |
| robert_winddown_closeout | easy | 85.7 % | 0.034 (0.037) | 0 | 116 / 129.8 / 143 | 136 | 500 | 55.0 % | 5 (4.6 %) | 111 (77.4 %) | 20 (18.0 %) | 6 (17 %) | FAIL |
| frederick_bridge_pipeline | medium | 77.7 % | 0.106 (0.116) | 1 | 109 / 131.5 / 150 | 40 | 168 | 95.2 % | 0 (0 %) | 27 (61.3 %) | 13 (38.7 %) | 4 (40 %) | PASS |
| douglas_beta_server_signoff | medium | 56.3 % | 0.117 (0.129) | 0 | 163 / 196.0 / 238 | 76 | 314 | 74.8 % | 17 (26.4 %) | 40 (44.6 %) | 19 (29.0 %) | 4 (33 %) | PASS |
| frederick_q4_commitments | easy | 71.0 % | 0.016 (0.018) | 0 | 151 / 188.8 / 212 | 102 | 350 | 64.3 % | 17 (23.7 %) | 70 (61.1 %) | 15 (15.1 %) | 4 (50 %) | FAIL |
| frederick_card_spend_q3 | medium | 78.3 % | 0.054 (0.059) | 0 | 554 / 560.0 / 573 | 63 | 243 | 67.9 % | 4 (8.2 %) | 44 (65.0 %) | 15 (26.7 %) | 4 (50 %) | FAIL |
| julia_zm_difficulty_baseline | medium | 83.8 % | 0.099 (0.108) | 1 | 357 / 818.3 / 1209 | 81 | 173 | 23.1 % | 0 (0 %) | 65 (66.5 %) | 16 (33.5 %) | 4 (40 %) | FAIL by 0.001 |
| vincent_zm3d_release_gate | easy | 78.3 % | 0.049 (0.053) | 0 | 124 / 163.8 / 259 | 67 | 227 | 57.3 % | 3 (4.8 %) | 52 (68.7 %) | 12 (26.4 %) | 4 (50 %) | FAIL |
| frederick_account_handover (Normal) | medium | 80.8 % | 0.161 (0.176) | 1 | 68 / 86.7 / 100 | 37 | 119 | 50.4 % | 0 (0 %) | 22 (50.4 %) | 15 (49.6 %) | 4 (40 %) | PASS |
| claire_zm3d_halloween_art_plan | medium | no verifier | local regex only: about 60 %, 0.025 | n/a | 219 / 223.8 / 239 | 217 | 755 | 50.3 % | n/a | n/a | n/a | n/a | not measured |

`julia_zm3d_beta_calendar` has no baselines. Weight-5 share is weight on weight-5 rows over total weight. Patterns use the calculator's rule (single linkage, two runs merge if they differ on at most one row); my recomputed values match the reports where a report exists. The Q4, card spend and Vincent largest patterns sit exactly on the 50 % limit.

**What produced the spread in the four passing tasks (FACT, from B)**
- **Douglas:** the reply-all D4 (2/6, 20.1 % of weight) and the Confluence comment D5 (3/6, 7.3 %) on top of a 26.4 % all-fail block. Two independent traps, both heavy.
- **Robert LLC:** run 3 found L1 and L2 and scored 100. Run 5 missed L3, L4 and L5 and scored 64.9. L5 at 3/6 split the middle. The spread leans on two outlier runs.
- **Bridge:** B1, B2 and B3, each 3/6, caught by different runs, holding 6 to 12 % of unique weight each. Three conjunctive rows (R22, R27, R34, 8.9 % of weight) pass only when both B1 and B2 land, which is why run 6 stands out at 100.
- **Handover:** Gmail partner notices H1 to H3 at 3/6 to 5/6, with a run that found them passing nearly everything.

**Why the five others failed the SD gate**
- **Q4:** five deciding records read by nobody. Mixed weight is only 15.1 %.
- **Winddown:** 77.4 % always passes, and the mid traps hold 4.6 % each.
- **Vincent, card spend:** the main traps sit at 0/6 or 1/6 (V1 to V3; C1 to C5), so at most one run stands out.
- **Julia:** one dominant scope choke point; 0.001 short.

## B. Trap table

78 traps: 72 graded by the verifier, 6 Claire. IDs: L Robert LLC, W winddown, B bridge, D Douglas, Q Frederick Q4, C card spend, J Julia, V Vincent, H handover, K Claire. "Unique rows" fail only through this trap. "Shared rows" are count or total rows that also need other traps.

| ID | Hidden fact | Carrier | Link | Ptr | Read | Caught | Unique rows (n, weight, % of task) | Shared rows (n, weight) | Locator / note |
|---|---|---|---|---|---|---|---|---|---|
| L1 | VO campaign $3,000/mo, no issue on any list | thread reply in a channel | de-named | N | 1/6 | 1/6 | 12, 38, 11.6% | - | #prototype C09UHHN6PFZ/1770938400.370665, Leonard, Feb 12, under a Feb 6 root |
| L2 | layer.ai concept art export by Mar 3 | thread reply in a channel | named | N | 1/6 | 1/6 | 2, 6, 1.8% | - | #prototype C09UHHN6PFZ/1770923700.470906, Leonard, Feb 12 |
| L3 | DD prod account $140 supersedes ~$1k | DM thread reply | alias | N | 5/6 | 5/6 | 13, 51, 15.5% | - | D04V95AAAHW/1770952200.665739, Arthur, under a git-debugging root |
| L4 | CF stacks $62 supersedes ~$95 | private mail thread | alias | N | 5/6 | 5/6 | 2, 6, 1.8% | - | mail subject "jenkins", Arthur, Feb 13, second paragraph; found by "AWS" search (runs 1,4) or a date sweep (2,3,6) |
| L5 | ENG-2462: Apple rejected the DD build | private mail thread | named | N | 3/6 | 3/6 | 3, 11, 3.4% | 1, 3 | Apple App Review notice, Feb 13 07:30Z, "App Name: Domino Delights"; only the three runs that did an inbox date sweep read it |
| L6 | Arthur pays Metabase, dbt, GitHub ($248) | private mail thread | named | P | 6/6 | 6/6 | 8, 26, 7.9% | - | mail "billing moved to my card", Feb 13 |
| W1 | CodeRabbit bot notice = vendor confirmed | PR conversation comment | named | N | 0/6 | 0/6 | 5, 23, 4.6% | - | harmonygames-Games/Combo-Fighters#38#c_1; rule 5 says "bot notice" but names no PR |
| W2 | Unity account manager confirmed | channel root post (added type) | named | N | 1/6 | 1/6 | 5, 23, 4.6% | - | #executives C07C2866011/1771017520.226917, Arthur, Feb 13; reached by Slack search "after:2026-02-08 unity" |
| W3 | Cursor sent the confirmation | thread reply in a channel | named | N | 4/6 | 4/6 | 5, 23, 4.6% | 1, 5 | #prototype C09UHHN6PFZ/1770991653.518204, Arthur, reply to Oliver |
| W4 | Gusto: docs pulled, cancel before Mar 3 | thread reply in a channel | named | P | 6/6 | 6/6 | 4, 14, 2.8% | - | #winddown C0ADGSZKR3R/1770948876.205117, reply in the hub keep-list thread |
| W5 | Sunset review call Mar 12 is the Hold date | calendar title/date (added type) | named | P | 6/6 | 6/6 | 7, 35, 7.0% | - | 5 of 6 runs got it from the invite copy in Gmail, 1 from gcal_search_events |
| W6 | SVB card: everything off by EOD Feb 17 | Trello card comment | named | P | n/r | 6/6 | 3, 15, 3.0% | 1, 5 | card 698f48be4ba0affafbf153db, comment action 698fa9f7f77cecfe5c7aa524 |
| W7 | Helpshift export done (dash, not a date) | Linear comment | named | P | 6/6 | 6/6 | 3, 11, 2.2% | - | Oliver on ENG-2439; every run lists comments on all issues |
| W8 | Docusign owner is Robert | Linear comment | named | P | n/r | 6/6 | 1, 3, 0.6% | - | Leonard on ENG-2457 |
| W9 | ElevenLabs hides in the Sound line | sheet tab | alias | P | n/r | 6/6 | 4, 10, 2.0% | - | costs tab; conventions rule 3 points at shared lines |
| B1 | Paul Heydon is out | DM | named | N | 3/6 | 3/6 | 2, 10, 6.0% | 3, 15 | D05S58U4SAK/1759251900.863415, Leonard, top-level DM |
| B2 | SciPlay passed | thread reply in a channel | named | N | 3/6 | 3/6 | 4, 20, 11.9% | 3, 15 | #executives C07C2866011/1759248360.377105, Robert, under an unrelated speedrun post |
| B3 | Investors are iOS only | channel root post (added type) | alias | N | 3/6 | 3/6 | 4, 20, 11.9% | - | #zombie-match3d C0880U9751A/1759274400.518306, Arthur; names people, not firms |
| B4 | Anton at $25,000, signed | DM | named | N | n/r | 6/6 | 3, 15, 8.9% | - | Leonard Sep 24 and Sep 26 DMs |
| B5 | Hiro passed (Edith Vane) | private mail thread | de-named | P | 6/6 | 6/6 | 1, 5, 3.0% | - | Sep 26 mail with no firm name; calendar and cc tie it to Hiro |
| B6 | Homa and Brightwater only on the calendar | calendar title/date (added type) | alias | P | n/r | 6/6 | 5, 25, 14.9% | - | call titled with a person; invite or Contacts tie the firm (run 6 made no Contacts call) |
| B7 | Checklists per group, per Leonard | Trello card comment | named | P | 6/6 | 6/6 | 3, 15, 8.9% | - | Leonard Sep 13 and Sep 29 comments on the prompt-named card |
| D1 | Import also needed: ZOM-459 (#38) | PR inline review | named | N | 1/6 | 0/6 | 4, 20, 6.4% | 4, 20 | match3d-backend#38#rc_1 |
| D2 | Import also needed: ZOM-509 (#39) | PR inline review | named | N | 1/6 | 0/6 | 4, 20, 6.4% | 4, 20 | match3d-backend#39#rc_1 |
| D3 | Import also needed: ZOM-537 (#46) | PR inline review | named | N | 0/6 | 0/6 | 5, 23, 7.3% | 4, 20 | match3d-backend#46#rc_1 |
| D4 | Analytics and loadout imports (ZOM-444, 531, 436) | reply-all inside a thread | named | N | 2/6 | 2/6 | 13, 63, 20.1% | 1, 5 | Arthur reply-all in Leonard "beta go/no-go" thread, second point |
| D5 | Boss arena HP import (ZOM-487) | Confluence comment | named | N | 3/6 | 3/6 | 2, 8, 2.5% | 3, 15 | comment_zm_beta_oct10_c2; R6, R27, R37 also pass in run 2 without the read |
| D6 | Freeze pulled in to Sep 26 (ZOM-550) | calendar description | named | P | 6/6 | 6/6 | 1, 5, 1.6% | - | freeze event, updated Sep 23; gcal_search_events in all runs |
| D7 | #47 back on prod (ZOM-499) | PR conversation comment | named | P | 6/6 | 6/6 | 1, 5, 1.6% | - | a newer prod: comment; runs read issue comments per PR |
| D8 | Zombie Lane import on prod, others dev only | sheet tab | named | P | 6/6 | 6/6 | 3, 13, 4.1% | - | Console & imports tab of the deploy log |
| D9 | main deploys to dev only | Drive doc | named | P | 6/6 | 6/6 | 3, 9, 2.9% | - | prod deploys doc f_470ae81236d5bd39045dc1 |
| D10 | Register goes in the ZM Beta sign-off folder | Confluence page | named | P | 6/6 | 6/6 | 1, 3, 1.0% | - | ZM Beta page, card rule 6 |
| Q1 | Nintendo: officer must accept ToS by Oct 15 | Linear comment | named | N | 0/6 | 0/6 | 4, 20, 5.7% | 3, 15 | ZOM-567 cmt_c9a6660d81e067ad1de7; 0 Linear calls in all six runs |
| Q2 | Framewell free until Feb 1 | thread reply in a channel | de-named | N | 0/6 | 0/6 | 3, 15, 4.3% | 2, 10 | #executives C07C2866011/1758920520.674991, says "Maren", under a Playtestcloud post |
| Q3 | Lanternfly answered by Leonard | DM thread reply | de-named | N | 0/6 | 0/6 | 3, 15, 4.3% | - | D05S58U4SAK/1759174260.052645, says "Wen", "Southeast Asia" |
| Q4 | Spotlight answered by Robert | older channel history | de-named | N | 0/6 | 0/6 | 2, 10, 2.9% | - | #executives C07C2866011/1758134460.899858, Sep 17; all six runs read the channel with oldest = Sep 26 or Sep 28 |
| Q5 | Balancy answered by Leonard | private mail thread | named | N | 2/6 | 0/6 | 1, 3, 0.9% | 3, 15 | base thread; two runs saw the line in snippets or minimal format only |
| Q6 | Pingwise is the night pager | Trello checklist | alias | P | 6/6 | 6/6 | 4, 20, 5.7% | - | keep card checklist item 689b66a450734c26dcdf6291 |
| Q7 | Clipforge pilot ends Oct 15 | private mail thread | alias | P | 6/6 | 6/6 | 3, 15, 4.3% | - | Paylane notice, workspace HG-2291, no company name |
| Q8 | Pixel Harbor June quote is in scope | private mail thread | named | P | n/r | 6/6 | 1, 3, 0.9% | - | June mail; R20, R23 fail run 3 for a log-writing reason |
| Q9 | Hootline August thread is in scope | private mail thread | named | N | n/r | 5/6 | 3, 9, 2.6% | - | thread 1839631800730308867, no filed paper, Aug 12 |
| Q10 | Markward: only founders accept terms | private mail thread | named | P | n/r | 6/6 | 3, 15, 4.3% | - | ESG note plus Leonard Sep 25 reply |
| C1 | Webflow now $18 ("for the card list") | private mail thread | named | N | 0/6 | 0/6 | 1, 5, 2.1% | 2, 10 | forward 1843077030346987811, Sep 12 |
| C2 | Murf now $11 | private mail thread | named | N | 0/6 | 0/6 | 1, 5, 2.1% | 2, 10 | vendor notice 1844260144939613075, Sep 25 |
| C3 | WeWork ends Sep 30 ("for the card spend") | private mail thread | named | N | 1/6 | 1/6 | 1, 5, 2.1% | - | forward 1842712891359915474 |
| C4 | SavvyCal closed, Sep 11 charge disputed | private mail thread | named | N | 1/6 | 1/6 | 2, 10, 4.1% | 2, 6 | forward "for the card spend" |
| C5 | Buttondown closed, Sep 21 charge disputed | private mail thread | named | N | 1/6 | 1/6 | 2, 10, 4.1% | 2, 6 | forward "another one for the card spend" |
| C6 | Keep Sensor Tower, cancel AppMagic | thread reply in a channel | named | N | 4/6 | 4/6 | 2, 8, 3.3% | - | #executives C07C2866011/1758910840.227619, Sep 26 reply |
| C7 | Edgegap downgraded to $420 | private mail thread | named | N | 5/6 | 5/6 | 2, 10, 4.1% | - | vendor mail 1844619081941308353 |
| C8 | LinkedIn Sep 3 charge after cancellation | private mail thread | named | N | 5/6 | 5/6 | 2, 10, 4.1% | - | vendor mail 1841082615726759126 |
| J1 | Leave off six tickets, keys in the reply | DM thread reply | named | P | 5/6 | 5/6 | 7, 15, 8.7% | 2, 10 | D05HB64NMQU/1759262838.442871, reply under the prompt-named DM; run 1 dropped reply_count |
| J2 | Take four tickets off, Brian comments only | DM thread reply | named | N | 3/6 | 3/6 | 4, 20, 11.6% | 2, 10 | D05HB64NMQU/1759267002.665190, under Julia's own Sep 29 question |
| J3 | ZOM-312 not tiers (#265) | PR inline review | named | P | 5/6 | 5/6 | none unique | 2, 10 | match3d#265#rc_7; card rule 1 names the review |
| J4 | ZOM-295 not tiers (#271) | PR inline review | named | P | 4/6 | 4/6 | none unique | 4, 20 | match3d#271#rc_1; card rule 1 names the review |
| J5 | ZOM-281 tiers: note | Linear comment | de-named | N | n/r | 5/6 | 1, 3, 1.7% | 4, 20 | note on a ticket not assigned to Blake |
| J6 | Blake reply: editor rule, > 90 check | private mail thread | named | P | 6/6 | 6/6 | 4, 12, 6.9% | - | own Gmail conversation "editor stuff and ZOM-199", named by card rule 3 |
| J7 | Robert's three extra columns | DM thread reply | named | P | n/r | 6/6 | 3, 3, 1.7% | - | group chat CAFC495E4006 thread, named by card rule 2 |
| V1 | ZOM-293 lost boosters | Linear comment | named | N | 1/6 | 0/6 | 2, 6, 2.6% | 1, 5 | cmt_zom293_1, reporter, Jul 3; run 1 read it and kept NO CALL |
| V2 | Brian's retests in Turkish (ZOM-458, 473, 535) | DM | named | N | 1/6 | 1/6 | 6, 30, 13.2% | 1, 5 | Vincent-Brian DM D0770ET1HV2, Sep 29-30 |
| V3 | Playtest vendor report = ZOM-562 | private mail thread | alias | N | 1/6 | 1/6 | 2, 10, 4.4% | 1, 5 | thread 1844730396672762606, "Puzzles vs Zombies" |
| V4 | ZOM-558 gated like any bug | Linear comment | named | N | 4/6 | 4/6 | 1, 5, 2.2% | - | Leonard comment on the ticket |
| V5 | Leonard reproduces ZOM-435 on #135 | Trello card comment | named | P | n/r | 6/6 | 1, 5, 2.2% | - | Fix TECH ISSUES card, Sep 30 |
| V6 | Chest rows never loaded on prod (ZOM-567) | PR inline review | named | P | 6/6 | 6/6 | 1, 5, 2.2% | - | match3d-backend#36#rc_1; the ticket names the PR |
| V7 | ZOM-563 confirmed on prod | DM | named | N | n/r | 6/6 | 2, 10, 4.4% | - | Vincent-Douglas DM D079SNE2TL4; citing row R38 passes 4/6 |
| H1 | Node still owns the YouTube Brand Account | private mail thread | alias | N | 3/6 | 3/6 | 2, 10, 8.4% | 3, 15 | Google notice 1842801580966444617, Sep 9 |
| H2 | Node still Admin on TikTok | private mail thread | alias | N | 5/6 | 5/6 | 2, 8, 6.7% | - | TikTok for Business reminder, Sep 18 |
| H3 | Instagram has two company holders | private mail thread | alias | N | 4/6 | 4/6 | 2, 10, 8.4% | - | Meta notice, Sep 15 |
| H4 | Node partner admin on Meta | sheet tab | named | N | n/r | 5/6 | 2, 4, 3.4% | - | Partners block lower in the export |
| H5 | Node Admin on the Unity Ads advertiser | sheet tab | named | N | n/r | 5/6 | 2, 4, 3.4% | - | second tab of the export |
| H6 | Keep Google Ads 569-350-5790 | private mail thread | named | N | n/r | 4/6 | 1, 3, 2.5% | - | Arthur follow-up email |
| H7 | Ad revenue under $100 does not count | DM thread reply | named | P | n/r | 6/6 | 1, 5, 4.2% | - | D05S58U4SAK/1759272498.304117, reply under the ask |
| H8 | Socials never CLOSE | Trello card comment | named | P | n/r | 6/6 | 2, 6, 5.0% | - | marketing rules card comment |
| K1 | Android US phone ads due Fri Oct 10 | thread reply in a channel | de-named | N | 0/6 | 0/6 | local grader only | - | #zombie-match3d C0880U9751A/1759275738.984915, Frederick |
| K2 | Julia takes the ad statics | channel root post (added type) | de-named | N | 0/6 | 0/6 | local grader only | - | C05KNDCHAAG/1759243286.478812, Martin |
| K3 | Marcus re-recorded three cuts | channel root post (added type) | de-named | N | 0/6 | 0/6 | local grader only | - | #zm-animations C09ATAJ220H/1758823964.738872 |
| K4 | Robert turned the test down | thread reply in a channel | de-named | N | 2/6 | 2/6 | local grader only | - | #zombie-art C08R8CHB0QL/1759248337.170599 |
| K5 | Two cuts off iOS UK tablet | private mail thread | de-named | N | n/r | 5/6 | local grader only | - | Frederick Sep 29 restart mail; ART-811, ART-813 |
| K6 | Old-zombie packs, off-sheet ART-826 | Trello card comment | named | P | n/r | 6/6 | local grader only | - | Frederick comment on the Halloween push card |

**Corrections to the READMEs found while building this**
- The Robert LLC README says the VO miss failed 14 rows. By record it is 12 rows for VO (L1) and 2 rows for layer.ai (L2). They share the pass pattern only because run 3 alone found both, by two separate Slack searches.
- D5: rows R6, R27 and R37 pass in run 2 without that run reading the comment, so the Confluence comment's clean count is R17 and R47. I score it 3/6.

**Not discovery traps.** Some failed rows are wording or one-run slips, not hidden facts, and are left out of the table. Examples: winddown's "nothing is due" rows R84, R94, R122, R126 (mixed, wording of a dash); Q4 run 3's log rows R12, R20, R23, R25, R27; Vincent's citation rows R37, R38. These add a little spread at no design cost. The winddown clash rows also sit outside: naming the Slack clash (R133 3/6, R135 2/6) needs a mail and a #winddown decision that every run had read, so those are judgement rows, not catches.

**Carrier gaps.** Cancelled calendar events, Linear issue descriptions as a sole carrier and a contact record as the sole carrier have n = 0. Older channel history has one instance only (Q4). Contacts appeared in B6 and V3, but run 6 of bridge caught B6 with no Contacts call, so no fact here depended on one.

## C. Roll-up by carrier and link

Read each rate with the bins beside it. A pooled 50 % made of 0/6 and 6/6 is worth nothing for spread.

**By carrier, all 78 traps**

| Carrier | Traps | Caught / run-chances | Rate | 0/6 | 1-2/6 | 3-4/6 | 5/6 | 6/6 |
|---|---|---|---|---|---|---|---|---|
| calendar title/date (added type) | 2 | 12/12 | 100% | 0 | 0 | 0 | 0 | 2 |
| Trello card comment | 5 | 30/30 | 100% | 0 | 0 | 0 | 0 | 5 |
| calendar description | 1 | 6/6 | 100% | 0 | 0 | 0 | 0 | 1 |
| Drive doc | 1 | 6/6 | 100% | 0 | 0 | 0 | 0 | 1 |
| Confluence page | 1 | 6/6 | 100% | 0 | 0 | 0 | 0 | 1 |
| Trello checklist | 1 | 6/6 | 100% | 0 | 0 | 0 | 0 | 1 |
| sheet tab | 4 | 22/24 | 92% | 0 | 0 | 0 | 2 | 2 |
| DM thread reply | 6 | 25/36 | 69% | 1 | 0 | 1 | 2 | 2 |
| DM | 4 | 16/24 | 67% | 0 | 1 | 1 | 0 | 2 |
| private mail thread | 23 | 84/138 | 61% | 3 | 4 | 4 | 6 | 6 |
| Linear comment | 6 | 21/36 | 58% | 2 | 0 | 1 | 1 | 2 |
| PR conversation comment | 2 | 6/12 | 50% | 1 | 0 | 0 | 0 | 1 |
| Confluence comment | 1 | 3/6 | 50% | 0 | 0 | 1 | 0 | 0 |
| PR inline review | 6 | 15/36 | 42% | 3 | 0 | 1 | 1 | 1 |
| thread reply in a channel | 9 | 21/54 | 39% | 2 | 3 | 3 | 0 | 1 |
| reply-all inside a thread | 1 | 2/6 | 33% | 0 | 1 | 0 | 0 | 0 |
| channel root post (added type) | 4 | 4/24 | 17% | 2 | 1 | 1 | 0 | 0 |
| older channel history | 1 | 0/6 | 0% | 1 | 0 | 0 | 0 | 0 |

**By carrier, unpointed traps only (this is the table to design from)**

| Carrier (unpointed) | Traps | Caught / run-chances | Rate | 0/6 | 1-2/6 | 3-4/6 | 5/6 | 6/6 |
|---|---|---|---|---|---|---|---|---|
| sheet tab | 2 | 10/12 | 83% | 0 | 0 | 0 | 2 | 0 |
| DM | 4 | 16/24 | 67% | 0 | 1 | 1 | 0 | 2 |
| Confluence comment | 1 | 3/6 | 50% | 0 | 0 | 1 | 0 | 0 |
| private mail thread | 17 | 48/102 | 47% | 3 | 4 | 4 | 6 | 0 |
| DM thread reply | 3 | 8/18 | 44% | 1 | 0 | 1 | 1 | 0 |
| Linear comment | 4 | 9/24 | 38% | 2 | 0 | 1 | 1 | 0 |
| reply-all inside a thread | 1 | 2/6 | 33% | 0 | 1 | 0 | 0 | 0 |
| thread reply in a channel | 8 | 15/48 | 31% | 2 | 3 | 3 | 0 | 0 |
| channel root post (added type) | 4 | 4/24 | 17% | 2 | 1 | 1 | 0 | 0 |
| PR conversation comment | 1 | 0/6 | 0% | 1 | 0 | 0 | 0 | 0 |
| PR inline review | 3 | 0/18 | 0% | 3 | 0 | 0 | 0 | 0 |
| older channel history | 1 | 0/6 | 0% | 1 | 0 | 0 | 0 | 0 |

**By link type**

| Link | Traps | Caught / run-chances | Rate | 0/6 | 1-2/6 | 3-4/6 | 5/6 | 6/6 |
|---|---|---|---|---|---|---|---|---|
| alias | 11 | 50/66 | 76% | 0 | 1 | 3 | 3 | 4 |
| named | 56 | 216/336 | 64% | 9 | 7 | 10 | 7 | 23 |
| de-named | 11 | 19/66 | 29% | 6 | 2 | 0 | 2 | 1 |

**By link and pointer**

| Link / pointer | Traps | Caught / run-chances | Rate | 0/6 | 1-2/6 | 3-4/6 | 5/6 | 6/6 |
|---|---|---|---|---|---|---|---|---|
| alias / pointed | 4 | 24/24 | 100% | 0 | 0 | 0 | 0 | 4 |
| de-named / pointed | 1 | 6/6 | 100% | 0 | 0 | 0 | 0 | 1 |
| named / pointed | 24 | 140/144 | 97% | 0 | 0 | 1 | 2 | 21 |
| alias / unpointed | 7 | 26/42 | 62% | 0 | 1 | 3 | 3 | 0 |
| named / unpointed | 32 | 76/192 | 40% | 9 | 7 | 9 | 5 | 2 |
| de-named / unpointed | 10 | 13/60 | 22% | 6 | 2 | 0 | 2 | 0 |

**Read of the tables**
- **Near 50 % and good for spread (2 to 4 of 6):** L5, W3, B1, B2, B3, D4, D5, C6, J2, J4, V4, H1, H3, H6, K4. By type: unpointed channel thread replies, DMs, and vendor or colleague mail with no prompt word.
- **What these share (INFERENCE):** they are reachable by a word or habit that runs use only sometimes. B3 needed the word "tester" or "internal test": runs 1, 3 and 6 used one and reached it, while run 5 tried only "testflight", which misses it. L5 needed an inbox date sweep, done by exactly runs 2, 3 and 6. D4 needed the thread opened, not just a sender search.
- **Land at 0 of 6, add average and no spread:**
  - PR inline, unpointed: 0/18. PR conversation comment, unpointed: 0/6.
  - De-named Slack: Q2, Q3, Q4, K1, K2, K3 all 0/6.
  - A service the run never opens: Q1 (0 Linear calls in all six runs).
  - Mail that shares no word with the task: C1, C2.
- **Land at 5 or 6 of 6, add no spread:** anything pointed. Every Trello card comment here, Trello checklist (even with the alias "night pager"), calendar description, Drive doc, Confluence page, and comments on the issues the run is already walking.
- **Link matters less than pointer.** Named but unpointed is 40 %. De-named unpointed is 22 %, with 6 of 10 at zero. Alias unpointed reads 62 % but rests on 7 traps, and I would not trust it as higher than named: H1 to H3 pull it up, and those are mail notices with distinctive sender names.
- **A word and a preview together decide a mail catch.** C3, C4 and C5 say "for the card spend"; C1 says "for the card list". Runs 4 and 6 both queried `"card spend"`, and both got the three forwards back. Run 6 used `gmail_list_threads`, which shows snippets, and opened all three. Run 4 used `gmail_search_messages`, which returned ids with no text, and opened none. C1 matched neither run's words, so no run saw it.
- **Calendar facts leak through mail.** W5 sits on the calendar, but 5 of 6 runs got it from the invite copy in Gmail.
- **Conjunctive rows sit below their traps.** Bridge R22, R27 and R34 need B1 and B2, so they pass 1/6 although each trap is 3/6. Julia R5 and R66 need five traps and pass 1/6.

## D. Opus habits for a persona with a big mailbox

Evidence is Robert and Frederick. All counts are from the 60 exports.

**First 20 service calls.** Very stable within a task. The opener is the prompt's anchor:
- Slack-anchored (LLC): `slack_read_user_profile`, `slack_search_users`, `slack_read_channel` on the DM, `linear_list_projects`, `gmail_search_messages from:<requester>`, `gdrive_search`, read the docs and draft, `linear_list_issues`, then the per-issue loop. All six runs open this way, with small swaps.
- Mail-anchored (bridge, Q4, card spend): `gmail_search_messages from:leonard after:<date>` first, `gmail_get_thread`, `gdrive_search` on the hub's words, read docs, `trello_search`, then a channel read.
- Mix of the first 20 calls: Drive 3 to 12, Slack 2 to 6, Gmail 0.5 to 7, Trello 0.5 to 5, Linear up to 8. Everything named in the prompt or hub is opened in this window. No run starts with a broad search.

**How it reads Slack**
- `slack_read_channel`: 158 calls, in 56 of 60 runs, about 2.6 a run, on 1 to 3 channels a run.
- A cursor was followed on 37 of 158 reads (23 %), and almost only in the hub channel (bridge 21, winddown 9).
- `oldest` was set on 75 of 158 reads. The window is short: median 5.3 days before the clock in Q4, 6.1 in LLC, 9.3 in Vincent, 7.3 in Julia. Bridge and handover use about 30 days because the ask says so.
- That window is why Q4 (the trap) was 0/6: all six runs read #executives with `oldest` on Sep 26 or Sep 28, and the post is Sep 17.
- `slack_read_thread`: 89 calls in 44 of 60 runs, about 1.5 a run. Q4 used it 0 times in six runs. Runs do not walk replies across a channel.
- Thread replies get found by search, not by opening threads. `slack_search_public_and_private` returns replies, and L3, W3, B2 and B3 were first read through it. Searches per run: bridge 13, Q4 12, Vincent 10, winddown 4.5, LLC 4.3.
- Search terms are item names, hub words and a `from:<person> after:<date>` sweep. In LLC only run 3 swept Leonard this way, which is how it reached L2; its `card after:2026-02-01` reached L1. Runs 4 and 6 limited their date sweep to DMs (`channel_types: im,mpim`), so it could not reach the channel reply L1.

**How it uses Gmail**
- Queries per run: winddown 16.2, Q4 9.2, handover 9.2, bridge 8.3, card spend 6.3, LLC 3.2, Julia 2.5, Claire 2.2, Douglas 1.0, Vincent 0.2.
- Gmail is searched hard only when the task is mail-shaped or the item list is vendors. On engineering tasks it is one sender search (Douglas) or nothing (Vincent), which is why D4 reached 2/6 and V3 1/6.
- Four query shapes:
  - `from:<requester>` with a date, always first where mail is the anchor (47 % of LLC and Q4 queries).
  - OR-lists of item names (62 % in winddown, 69 % in handover).
  - Hub words such as `Sunset`, `SVB`, `docusign`.
  - Pure date sweeps with no sender and no content word, such as `after:2026/02/09 -from:github.com`: 18 in Q4, 9 in bridge, 3 each in LLC, winddown and Claire, none in Douglas, handover or Julia.
- Generic billing words also appear: `subject:(receipt OR invoice OR cancelled ...)`, mostly in winddown and card spend.
- **A search hit is not a read.** `gmail_search_messages` returns ids, so opening is a separate choice, and the card spend case above shows hits left unopened. `gmail_list_threads` shows snippets but was used in only 10 of 60 runs.
- Date sweeps are what catches keyword-free recent mail. In LLC the three runs that swept the inbox are the three that read the Apple notice, and those plus the two that searched `AWS` read the jenkins mail.
- Sweeps are recent only. Nothing here shows a sweep reaching back months.

**Subagents.** Used only where reads fan out. Runs with at least one: LLC 0/6, winddown 0/6, bridge 1/6, Q4 1/6, Claire 1/6, handover 1/6, Vincent 3/6, Douglas 5/6, card spend 5/6, Julia 6/6. Julia ran up to 17, card spend up to 34. They read; they do not write. Their MCP calls count toward the counted total.

**Big results.** Results over the token cap spill to a file and Opus reads them with `jq` or Python in Bash, 1 to 4 times a run on most tasks. The fields it prints are the fields it sees. LLC's `jq` printed `reply_count`. Julia run 1's `jq` printed only ts, time, user and text, and that run never opened the reply J1 under the DM it had just read.

**What it never or rarely opens, out of 60 runs**

| Read | Runs | Note |
|---|---|---|
| `gmail_get_attachment` | 0 | never called |
| `slack_read_file` | 2 | |
| `confluence_list_comments` | 3 | all Douglas |
| `gcal_get_event` | 5 | calendar text is seen through list or search results |
| `trello_get_checklist` | 1 | checklists come with the card |
| `github_get_pull_request_comments` | 12 | Julia 5, Vincent 6, Douglas 1 |
| Any GitHub call on the 36 Robert and Frederick runs | 1 | one `search_code` in winddown |
| Any Linear call in Q4 | 0 of 6 | bridge makes one list and one comment read per run |
| Linear comments off the walked issues | rare | V1: 1/6, even with ZOM-293 in scope |

**When a total will not tie: not observed.** I scanned the text blocks of all 60 runs for language about totals that do not tie or reconcile and found none. The nearest case is card spend, where all six runs parsed every daily sheet with Bash and tied to the ledger to the cent ($97,968.21). Four rows still failed every run, because the tie-out covers Q3 actuals and the missed facts changed the Q4 run-rate.

INFERENCE: a clean tie reassures it and stops the search. In LLC nothing challenged the total, and five of six runs stated a wrong $450 or $343 without any check. So a control total that a missed fact breaks is an untested lever. We have no evidence on whether Opus chases the gap or plugs it, and a fair test needs one pre-check.

## E. Counted calls

Reads and writes below are raw service calls, a little above counted. Writes barely vary between runs; reads do.

| Task | Every run 130+? | Writes per run | Reads per run | Calls that carried it |
|---|---|---|---|---|
| claire | yes (219) | 125-131 | 93-109 | `linear_list_comments` 60, `linear_create_comment` 58, `linear_update_issue` 47, `gdrive_share_file` 12 |
| douglas | yes (163) | 19-29 | 137-211 | `linear_list_comments` 97, GitHub comments 20, reviews 18 |
| frederick_q4 | yes (151) | 88-92 | 61-120 | `gmail_reply_to_message` 34, `contacts_add_new_contact` 31, `gcal_create_event` 12, cards 7, `gmail_get_thread` 23 |
| robert_llc | yes (149) | 79-83 | 72-83 | per-issue triple: `linear_list_comments` 37, `linear_create_comment` 37, `linear_update_issue` 37 |
| card spend | yes (554) | 10-15 | 542-662 | one `gdrive_read_file` or range read per daily sheet, 496 sheets |
| julia | yes (357) | 19-24 | 349-1186 | `linear_list_comments` 244-942, one run 477 PR review reads |
| vincent | 4 of 6 (124) | 5-6 | 120-271 | `linear_get_issue`, `linear_list_comments` |
| robert_winddown | 3 of 6 (116) | 43-47 | 74-98 | comments 28, list 27, state moves only 10 |
| frederick_bridge | 3 of 6 (109) | 53-55 | 54-95 | `trello_create_check_item` 25, `trello_create_card` 19, `gmail_get_thread` 3-36 |
| handover | no (Normal) | 6-11 | 57-99 | |

**What reached 130+ every run (FACT)**
- **Per-target writes with no batch form, three per item.** LLC is the cleanest: 37 items times 3 calls is 111, plus about 45 calls of discovery. Winddown had 28 items but only 10 state moves, and it missed in half its runs.
- **Several different per-target writes.** Q4 has 87 writes across five kinds with 36 items.
- **A forced per-file or per-item read.** Card spend and Julia are huge, but those calls are reads that subagents sweep, and they say nothing about difficulty.

**Batchable or not (FACT, from the 387-tool catalog)**
- No batch form: Linear comment, issue update, issue create; Trello card, check item; `contacts_add_new_contact`; `gmail_reply_to_message`; `gcal_create_event`; `gdrive_share_file`; `linear_list_comments`.
- Batch form exists: `gmail_get_messages_batch`, `gsheets_batch_update`, `gsheets_values_batch_get`, `gdocs_batch_update`, `gslides_batch_update`, `contacts_get_contacts_batch`.
- **This matters for an Authoring task.** A sheet or doc is one to five calls whatever its size. Vincent's 133-row register cost 5 to 6 writes in all. The deliverable adds no horizon, so the horizon has to come from per-target writes around it.

**Rule of thumb (INFERENCE):** counted is about 45 discovery calls plus the unbatchable per-target calls. Use 130 minus 45, so 85 or more mandatory per-target calls, and aim for 100 to clear the lowest run. Do not count on run-to-run reads: bridge's Gmail reads ranged 9 to 39.

## F. Row-shape effect

How computed: I scored the earlier rubric on the real verifier outcomes, matching rows by title. Exact and near-exact titles matched directly. For LLC, 18 draft rows had no such match: twelve took the outcome of the nearest final row, and six were set by hand, of which three are inferences (exactly 28 Canceled, exactly 7 LLC rows, the GitHub step). The result matches the README's "about 76 %".

| Task | Before: rows, weight | Before: average, SD | After: rows, weight | After: average, SD | Change | Rows added: weight, pass rate |
|---|---|---|---|---|---|---|
| robert_llc | 73, 207 | 76.5 %, 0.143 | 130, 328 | 83.6 %, 0.103 | +7.1 pts, -0.040 | +121 weight, about 96 % net (INFERRED from the two totals) |
| douglas (v1, 50 of 52 rows matched) | 52, 196 | 41.1 %, 0.162 | 76, 314 | 56.3 %, 0.117 | +15.2 pts, -0.045 | 26 rows, 92 weight, 94.6 % |
| bridge (draft 3, 28 of 33 matched) | 33, 133 | 71.2 %, 0.139 | 40, 168 | 77.7 %, 0.106 | +6.5 pts, -0.033 | 13 rows, 41 weight, 87.8 % |
| julia (61 of 73 matched) | 73, 169 | 81.5 %, 0.122 | 81, 173 | 83.8 %, 0.099 | +2.3 pts, -0.023 | 20 rows, 44 weight, 90.5 % |
| frederick_q4 | 57 rows, not stored | not computable | 102, 350 | 71.0 %, 0.016 | not computable | |
| robert_winddown | 115, 419 | not usable: renamed rows hold the traps | 136, 500 | 85.7 %, 0.034 | not computable | |
| card spend | 40, 128 | not usable: only 4 titles survive | 63, 243 | 78.3 %, 0.054 | not computable | |

**The earlier LLC forecast, decomposed.** Proxy with 29 rows: 67 to 72 %, SD 0.17. On the real 73-row draft: 76.5 %, SD 0.143. On the final 130 rows: 83.6 %, SD 0.103. So 5 to 10 points came from the proxy's own row mix before /rubric, and 7 points from /rubric.

**Row-mix rule of thumb the evidence supports**
1. Forecast on the final per-target row set, not a draft. /rubric required one row per target for writes and per fact in a requested list on every task where that was tested.
2. If you must forecast on a draft, treat new rows as passing about 90 to 95 % and adding 25 to 60 % more weight. Worked example: to land at 62 % after 50 % more weight at 93 %, the draft must score about 47 %.
3. The average cannot fall below the always-pass share. Always-pass weight was 44.6 % on Douglas and 61 to 77 % on the others. Keep it at or under about 40 to 45 % of final weight.
4. Make per-target rows depend on a trap. Rows that a trap flips are the only rows that lower the average after multiplication. A fact that changes an item's call flips 4 to 13 rows: D4 13 rows and 20.1 %, L3 13 rows and 15.5 %, V2 6 rows and 13.2 %, L1 12 rows and 11.6 %. A fact that changes one cell moves 1 to 2 rows and 1 to 2 % (L2, L4, C2).
5. Each spread trap needs at least 10 % of final weight and at least 2 unique rows. Below 10 %, SD falls under 0.1 even at a 50 % catch rate.
6. Weight-5 share alone does not predict the result: bridge is 95 % at 77.7 %, Douglas 75 % at 56.3 %, Julia 23 % at 83.8 %. What matters is where the 5s sit.

## G. Target arithmetic for E[avg] about 62 % with SD above 0.1 (UNCALIBRATED)

**Everything in this section is UNCALIBRATED.** It is a simple model on n = 6 estimates, and the last two forecasts of this kind were optimistic.

**Model.** Trap i has weight share w_i and catch rate p_i. F is weight that fails every run.

- E[avg] = 1 - F - sum of w_i (1 - p_i)
- run variance = sum of w_i^2 p_i (1 - p_i)
- expected population SD over 6 runs is about sqrt(5/6) times the run SD

**Back-test.** I grouped each task's rows by identical pass pattern and compared this SD with the actual one. Actual over model ranged 0.54 to 1.47, median 1.20. That is in-sample, so it only shows the form is sensible and that same-run correlation pushes SD up a little. Mean correlation between mid traps in one task is 0.13 (59 pairs), but it ranges from -0.17 on Vincent to 0.46 on LLC.

**Worked arithmetic for design B**
- Three traps at p = 0.5, w = 0.16: miss 3 x 0.16 x 0.5 = 0.24. Variance 3 x 0.0256 x 0.25 = 0.0192.
- One low trap at p = 0.17, w = 0.06: miss 0.06 x 0.83 = 0.05. Variance 0.0036 x 0.141 = 0.0005.
- Floor F = 0.09.
- E[avg] = 1 - 0.09 - 0.24 - 0.05 = 0.62. Run SD = sqrt(0.0197) = 0.140. Population SD over six runs is about 0.128.
- Weight check: 0.48 + 0.06 + 0.09 = 0.63, so always-pass weight is 0.37.

**Designs, 12,000 simulated six-run batches each (UNCALIBRATED).** "All gates" means average under 70 %, SD 0.1 to 0.3, pattern gate. Correlation 0.15 roughly matches the observed 0.13.

| Design | E[avg] | Expected SD | P(SD ok) indep / corr .15 | P(all gates) indep / corr .15 | P(all) if p is 0.15 too high in the plan |
|---|---|---|---|---|---|
| A: 4 at .5, w .125; 1 at .17, w .06; floor .08 | 62 % | 0.116 | 0.61 / 0.78 | 0.58 / 0.71 | 0.28 |
| B: 3 at .5, w .16; 1 at .17, w .06; floor .09 | 62 % | 0.128 | 0.73 / 0.83 | 0.67 / 0.73 | 0.35 |
| C: 5 at .5, w .10; 1 at .17, w .06; floor .08 | 62 % | 0.104 | 0.48 / 0.71 | 0.46 / 0.66 | 0.22 |
| E: 6 at .5, w .08; floor .14 | 62 % | 0.089 | 0.28 / 0.55 | 0.27 / 0.52 | 0.13 |
| F: 4 at .5, w .14; 2 at .17, w .06; no floor | 62 % | 0.131 | 0.74 / 0.87 | 0.67 / 0.76 | 0.25 |
| G: Q4 shape, 1 at .5, w .10; floor .33 | 62 % | 0.046 | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 |

Against the platform's medium cap of 85 % the average is safe in every design, so the pass chance falls to about the SD figure. SD is the binding gate, not the average.

**If catch rates are not controlled.** Same model, but each trap's p drawn from the real unpointed outcomes (mean 0.39), trap-bearing weight about 62 %:

| Traps | Weight each | P(avg < 70 %) | P(SD ok) | P(pattern ok) | P(all gates) |
|---|---|---|---|---|---|
| 4 | .155 | 0.75 | 0.42 | 0.60 | 0.26 |
| 5 | .125 | 0.77 | 0.25 | 0.74 | 0.17 |
| 6 | .105 | 0.79 | 0.18 | 0.83 | 0.13 |
| 8 | .078 | 0.81 | 0.08 | 0.93 | 0.06 |

This overstates the spread of true rates a little, because each outcome carries n = 6 noise. The direction still holds: more, smaller traps make SD worse, not better.

**What the evidence suggests (INFERENCE, UNCALIBRATED)**
- Three or four independent heavy traps aimed at 40 to 60 %, each 12 to 16 % of final weight, each with at least 4 unique rows.
- One or two low traps (about 1/6) at 5 to 6 % each, for the average.
- A small floor, 5 to 9 %, from one 0/6 carrier. Not more.
- Always-pass weight about 35 to 40 %. No task here has done that; the lowest is 44.6 %.
- Spread the mid traps over different discovery routes, so one habit does not catch them all. Candidates by evidence:
  - a channel thread reply reachable by one uncommon word (W3, B2, C6: 3/6 to 4/6);
  - a recent mail with no prompt word, reachable only by an inbox date sweep (L5: 3/6);
  - a top-level DM from the requester, off the hub thread (B1: 3/6);
  - a reply-all deep in a thread the runs find by sender (D4: 2/6).
- Prove the catch rate before the baseline, with pre-checks and a read-scan like the one here, since one run gives one bit per trap.

**Failure modes**
1. **Too hard in the same place, so the pattern gate fails.** When runs fail the same rows, they form one pattern. Q4, card spend and Vincent already sit exactly on the 50 % limit, with SD 0.016 to 0.054. Design G passes the pattern gate only 31 % of the time and the SD gate never. Heavy all-fail weight also needs every row defended in `11_AF_Justification.md`.
2. **Bimodal landing.** Aiming at 50 % and landing at 0 or 5 of 6 is the normal result, not the exception: 3 in 10 unpointed traps land at 2 to 4. Q4's de-naming sent five traps to 0/6 in one revision.
3. **Row multiplication after design.** Plan 6.5 to 15 points and 0.03 to 0.05 of SD, or design on the final rows.
4. **Traps too small.** Below about 10 % each, SD stays under 0.1 at any catch rate (design E).
5. **Correlated traps.** One search can catch two traps. L1 and L2 fell in the same run, so LLC's patterns dropped to 3 and its spread rests on two outliers. Traps sharing a channel, author or search word act like one trap.
6. **Pointer leak.** A rule that names the carrier moves p from 0 to about 0.8 (PR inline). A word the runs search for, plus a tool that previews it, can do the same (C3 versus C1).
7. **Single-row traps merge.** Two runs differing on one row count as one pattern. Each trap needs at least 2 unique rows. The LLC decode flagged this risk for ENG-2462.
8. **Batch luck.** Bridge rev12 failed the pattern gate on batch 1 and passed on batch 2, unchanged. Population SD there was 0.106, and one builder weight typo (R14, R15) took it to 0.098. Aim above 0.12, not at 0.10.
9. **Persona transfer.** All rates come from other personas. Leonard's mailbox may spill more search results, which could lower the date-sweep catch rate (L5) and make mail traps fall toward 1/6.
10. **Older priors.** `references/mechanism_priors.json` is built on claude-opus-4-8 and labelled UNCALIBRATED. I did not use it. `Hardness_Mastery.md` A14 (67 of 124 runs with no thread-reply call) points the same way but is also older.

## Not read / could not do
- **Not read:** full trajectory narratives. I worked from scans, the row matrix and targeted lookups. I did not re-derive any task's truth, so catch status rests on the verifier and, for Claire, on a local regex grader.
- **Claire:** the stored `baseline_grade.json` is from the 221-row version; its six run scores average 60.0 %, against 60.6 % in the README. The round 2 /rubric report and verifier results are not on disk.
- **Q4 row-shape:** the 57-row draft is not stored, so that step cannot be measured. Winddown and card spend drafts are too renamed to match.
- **Types with no evidence:** cancelled calendar event, amount-only link, sole-carrier Linear description, sole-carrier contact record. Older channel history has n = 1.
- **Read scans:** a few needles are phrase-specific. Text with non-ASCII characters may be missed (the Turkish message "hala geçilebiliyor" returned 0 where the sibling line returned 1), so V2's read count rests on one line plus the verifier.
- **Universe search:** not used, per the job brief.
- **Scratch artifacts:** matrices, call lists, trap data and simulation scripts are in `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/c5/`.
