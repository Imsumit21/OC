# 05 Human Time Worksheet

Pass: post-baseline refresh        Tier: Long-Horizon
Universe: normal · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Hours: 22.00

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read the close-out notes doc and open the holder project | read | 1 notes doc f_a37b403d5200d4f0a31d31, 1 project, 26 issues | ≈20 min per decisive record (anchor) × 2 | 40 |
| Read every holder issue's notes | read | 26 issues, 52 comments (SQL linear_comments) | ≈2 min per comment (V1 sweep rate) | 104 |
| Read #winddown for the investor draft, Leonard's list and the done lines | read | 206 Feb 2026 messages in C0ADGSZKR3R plus the injected posts | 3,000/h skim ≈ 5 min + 2 decisive threads × 20 min | 45 |
| Work out each option line (held today, vested, last day after extensions) | read | 14 Carta termination notices in Leonard's mailbox + 1 grant digest | ≈10 min per notice (dense dates and figures) | 150 |
| Check whether each holder was already told | read | 26 holder addresses × 2 surfaces (Gmail, Slack) | ≈10 min per record (V1 8 to 15 min) | 260 |
| Read Sunset's intake, KPMG's request and clarification, Griffin's board thread, the 2023 family mail | read | 4 threads | ≈20 min per decisive thread (anchor) | 80 |
| Dead ends: old Nov 2024 rows on the draft sheet, superseded notes, lookalike deck and Trello card, wrong-entity and wrong-date mails | dead end | 24 designed traps (manifest T1 to T24) | ≈5 min each | 120 |
| Recheck rows a later record overturns (extensions, the Feb 12 told mail) | re-read | 26 rows rechecked once | ≈1.5 min per row | 39 |
| Fill the holder sheet and its label counts | write | 26 rows + 6 counts | ≈3 min per row, 2 min per count | 90 |
| Investor letter from the #winddown draft, filed and shared | write | 1 doc + 6 Drive moves or shares | 60 min letter + 2 min per Drive step | 72 |
| Holder notes saved as Gmail drafts | write | 14 drafts | ≈10 min per tailored write | 140 |
| Linear state changes and comments | write | 26 state changes, 12 comments | 2 min per state change, 5 min per comment | 112 |
| KPMG answer (Griffin holdings, ES-15, ES-16, ES-17 as of Dec 31, 2025) | write | 1 reply, 5 figures | ≈8 min per figure + 8 min to write | 48 |
| Griffin heads-up and #winddown reply | write | 2 messages | ≈10 min per tailored write | 20 |
| Total | | | | 1320 = 22.00 h |

Tier check: in band (Long-Horizon about 12 to 24 h; 22.00 h).
Baseline count basis (post-baseline only): average 224 tool calls over 6 completed runs (203, 251, 219, 214, 241, 215) vs Long-Horizon 100+.
Condensed breakdown length: 1042 characters (field accepts 50–2,000)
Sources measured: hg.py search gmail "has been terminated" (14 matches, all threads/leonard@harmonygames.co_*, scan complete); hg.py search slack --file messages/C0ADGSZKR3R/2026-02.json --key type "message" (206, scan complete); slack channels.json C0ADGSZKR3R members include EMPLOYEE_0038_SLACK_ID (Leonard); 01_Universe_Inject.sql read as text: 26 linear_issues, 52 linear_comments, 1 linear_projects; 01_Hardness_Manifest.json traps (24) and writes (14 drafts, 26 updates, 12 comments, 6 Drive steps, 2 replies, 1 Slack post); baseline trajectories tool_use counts.

## Self-review

1. Walked Long Horizon Guidelines §5 and §10 and the field text: sub-tasks with time each, measured volumes, dead ends and writes listed, minutes add to 1320 = 22.00 h on a 0.25 step, condensed text 1042 characters. Friction is none, so no workaround line is owed.
2. Counter-readings:
   - Counter-reading (inflated): every row has a measured volume and an anchor rate; the only slower rate is the Carta notices at 10 min each, because each needs a grant, vested and termination figure plus an extension check (14 notices, hg.py search above).
   - Counter-reading (solution-path estimate): the 24 manifest traps (T1 to T24) carry a 120 min dead-end line, and the told check is costed per holder (26 × 2 surfaces), not as "open the right DM"; baseline runs missed one told holder each (11_AF_Justification.md R56), which shows the search is real work (R56, R58).
   - Counter-reading (evaluator-wide volume): Gmail counts are Leonard's mailbox only (14 of 14 notice files are threads/leonard@harmonygames.co_*); #winddown is a channel Leonard belongs to (EMPLOYEE_0038_SLACK_ID in its members of C0ADGSZKR3R).
   - Counter-reading (tier mismatch): 22.00 h, T1 to T24 costed, sits inside Long-Horizon 12 to 24 h and the baseline averaged 224 calls (100+), so scope and tier agree.
   - Counter-reading (linter reading): from the prompt and the SQL alone (26 holder issues, 52 comments, letter, drafts, Linear, three replies), 22 h is within 3× of a defensible estimate; the paragraph names the volumes and traps (T1 to T24 as plain descriptions), not IDs.
3. Re-verified volumes through hg.py (notices, #winddown) and the SQL text (issues, comments); write counts from the manifest match the rubric (14 draft rows, 26 move rows, 12 comment rows).
4. Recomputed: 40 + 104 + 45 + 150 + 260 + 80 + 120 + 39 + 90 + 72 + 140 + 112 + 48 + 20 = 1320 min = 22.00 h.
5. Unresolved: none.
