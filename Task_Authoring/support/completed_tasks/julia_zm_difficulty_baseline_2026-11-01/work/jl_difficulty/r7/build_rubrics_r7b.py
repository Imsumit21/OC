"""Round 7b: applies the /rubric FAIL Fix List (Audit-Report/3_rubric_FAIL_r4.md, reviewed JSON 45a9dacc2597) to 09_Rubrics.json.
Checked fixes are copied word for word; R5 is our own rewrite (the report asks for it). Run from Task_Authoring-2.
Usage: build_rubrics_r7b.py <reviewed 09_Rubrics.json>
"""
import hashlib
import json
import sys

src = sys.argv[1]
assert hashlib.sha256(open(src, 'rb').read()).hexdigest().startswith('45a9dacc2597'), 'not the reviewed rubric'
R = json.load(open(src))
assert len(R) == 73
row = {i: r for i, r in enumerate(R, 1)}
ASKR = "Leonard's reply under the ask, D05HB64NMQU/1759262838.442871"
BREPLY = "Blake's reply julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>"
ROBERT = "Robert's reply in the group chat, CAFC495E4006/1759229513.774912"
TIER = ("(passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count, with or without a CPM "
        "average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', "
        "'after the first 10 levels played', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 "
        "levels with no timing)")
TIER_INNER = TIER[1:-1]

# R5: own rewrite, decided by layout
assert row[5]['title'].startswith("The Agent fills the Tickets tab")
row[5]['title'] = ("The Agent fills the Tickets tab of the ZM difficulty baseline register with exactly 23 ticket rows (every row on the Tickets tab "
                   "that names a ZOM ticket counts toward the 23; a list of left-off tickets passes only on another tab or outside the sheet)")
row[5]['evidence'] = row[5]['evidence'].split(' Accept:')[0] + (" Accept: exactly 23 rows on the Tickets tab that name a ZOM ticket; every such row "
                                                               "counts, whatever its status cell says; left-off tickets listed on another tab or outside the sheet do not count.")
# R6 justification (worth a look; facts re-checked: the six analytics/tutorial tickets, ZOM-258 and ZOM-295 would be Live)
row[6]['justification'] = ("Multi-source: needs every cut that removes a would-be Live ticket: the six analytics and tutorial tickets in Leonard's reply "
                           "D05HB64NMQU/1759262838.442871, ZOM-258 in his notes doc f_f494073fc667097c3c2c6b and ZOM-295 in Blake's 'not tiers' comment "
                           "harmonygames-Games/match3d#271#rc_1, which leaves 15 Live.")
# R7 justification (checked text)
row[7]['justification'] = ("Multi-source: Blake's mail, the closing notes and both cuts of editor tickets: Leonard's reply D05HB64NMQU/1759267002.665190 "
                           "takes ZOM-162, 163 and 201 off and Blake's 'not tiers' comment harmonygames-Games/match3d#265#rc_7 keeps ZOM-312 off, leaving "
                           "ZOM-173, 200, 277 and 315 as Editor only.")
# R28 (checked text), weight 3, Comparison
assert row[28]['title'].startswith("The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier")
row[28]['title'] = ("The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier is set once "
                    "they have played 10 games " + TIER)
row[28]['weight'] = 3
row[28]['justification'] = ("Comparison: the build (TierManager.cs totalGames == 10, GetTotalGames = wins + losses) and Blake's reply over ZOM-42, ZOM-199 "
                            "and the deck, under rule 5 'go by the build'.")
row[28]['evidence'] = row[28]['evidence'].split(' Accept:')[0] + " Accept: " + TIER_INNER + "."
# R71 (checked text), weight 3
assert row[71]['title'].startswith("The Agent tells Leonard in its DM reply that a new player's starting tier")
row[71]['title'] = "The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games " + TIER
row[71]['weight'] = 3
row[71]['justification'] = ("Comparison: the build (TierManager.cs totalGames == 10) over ZOM-42, ZOM-199 and the deck (rule 5); Leonard's ask names "
                            "the question.")
row[71]['evidence'] = row[71]['evidence'].split(' Accept:')[0] + " Accept: " + TIER_INNER + "."

out = []
for i in range(1, 74):
    if i in (24, 69):          # deleted per the Fix List
        continue
    r = row[i]
    if 49 <= i <= 55:          # split: status row (w3) + builds row (w1)
        k = r['title'].split('Linear issue ')[1].split(' ')[0]
        out.append(dict(title=f"The Agent adds a new comment on Linear issue {k} saying its change is not in the store builds players have today",
                        category="Outcome", weight=3,
                        justification=("Interpretation: the checklist's rule 6 change ('the Editor only and Not shipped tickets get a comment too, saying "
                                       f"the change isn't in the store builds', 68dc033bf7d24e86b8a9cc67) applied to {k}'s register status, which its "
                                       f"closing note or Linear state and {BREPLY} decide."),
                        evidence=(f"Sources: the card's 'Before Monday' checklist 68dc033bf7d24e86b8a9cc67; {BREPLY}; {k}'s closing note or Linear state. "
                                  f"Accept: a new '{k}' comment saying the change is not in the store builds, any wording.")))
        out.append(dict(title=f"The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue {k}",
                        category="Outcome", weight=1,
                        justification=(f"Lookup: {ASKR}: 'put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what "
                                       "you checked against'."),
                        evidence=(f"Sources: {ASKR}; Blake's 'store builds for monday' mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>. "
                                  f"Accept: the new '{k}' comment names iOS 0.3.49 and Android 0.3.133, any format.")))
        continue
    out.append(r)
    if i == 27:
        out.append(dict(title=("The Agent marks ZOM-280 as never done in the done-day column of the Tickets tab of the ZM difficulty baseline register "
                               "(ZOM-280 was never marked done; a cell with no date passes: empty, a dash, N/A or a never-done note; any date, including "
                               "its 2025-06-20 cancel date, fails)"),
                        category="Outcome", weight=1,
                        justification=(f"Lookup: {ROBERT}: 'leave it blank if it never got done'; ZOM-280 has no completed_at (canceled_at "
                                       "2025-06-20T23:38:27Z)."),
                        evidence=(f"Sources: {ROBERT}; ZOM-280 in Linear (completed_at null, canceled_at 2025-06-20T23:38:27Z). Accept: a done-day cell "
                                  "for ZOM-280 with no date (empty, a dash, N/A or a never-done note); any date, including 2025-06-20, fails.")))
    if i == 29:
        out.append(dict(title="The Agent states on the Rules in force tab of the ZM difficulty baseline register that new players who miss the tier 1 threshold start on tier 0",
                        category="Outcome", weight=1,
                        justification=f"Lookup: ZOM-42 'rest stays in tier 0'; {BREPLY}: '90 exactly stays on tier 0'.",
                        evidence=(f"Sources: ZOM-42 description; {BREPLY}; match3d Assets/Scripts/DynamicDifficulty/TierManager.cs (default: newTier = 0). "
                                  "Accept: any wording that players below the tier 1 threshold start or stay on tier 0.")))
    if i == 47:
        out.append(dict(title=("The Agent adds a new comment on Linear issue ZOM-199 saying the build sets the starting tier once a player has played "
                               "10 games (passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count; "
                               "fails: a count of levels with nothing saying losses or replays count, 'after level 10' or 'once level 10 is cleared')"),
                        category="Outcome", weight=3,
                        justification=(f"Comparison: {BREPLY} ('it runs when a player's 10th game ends, wins and losses both counted ... ZOM-199 says "
                                       ">= 90 after the first 10 levels') against the ticket text; rule 6 comments with what the build does."),
                        evidence=(f"Sources: {BREPLY}; Trello card 'Difficulty baseline (Julia)' 68daca5871dba40417a00383, rule 6; match3d "
                                  "Assets/Scripts/DynamicDifficulty/TierManager.cs (totalGames == 10). Accept: a new 'ZOM-199' comment with wording that "
                                  "counts 10 games, attempts or plays, or a count of levels that says losses or replays count; a count of levels with "
                                  "nothing saying losses or replays count, 'after level 10' or 'once level 10 is cleared' fails.")))
assert len(out) == 73 - 2 + 3 + 7 == 81, len(out)
for r in out:
    for k in ('title', 'justification', 'evidence'):
        assert '—' not in r[k] and '\r' not in r[k]
json.dump(out, open('task_inputs/09_Rubrics.json', 'w'), indent=2, ensure_ascii=False)
print('rows', len(out), 'weight', sum(r['weight'] for r in out))
