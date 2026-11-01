"""Round 7c: copies the four checked fixes from /rubric FAIL r5 (reviewed JSON a8175ba31c4c) exactly. Nothing else changes."""
import hashlib, json, sys
src = sys.argv[1]
assert hashlib.sha256(open(src, 'rb').read()).hexdigest().startswith('a8175ba31c4c')
R = json.load(open(src)); assert len(R) == 81
TIER = ("(passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, "
        "unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', "
        "'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to "
        "Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail)")
ACC = ("Accept: passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, "
       "unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', "
       "'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to "
       "Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail.")
def fix(n, prefix, title, accept, w):
    r = R[n - 1]; assert r['title'].startswith(prefix), (n, r['title'][:80]); assert r['weight'] == w
    r['title'] = title
    assert ' Accept:' in r['evidence']; r['evidence'] = r['evidence'].split(' Accept:')[0] + ' ' + accept
fix(5, "The Agent fills the Tickets tab",
    "The Agent fills the Tickets tab of the ZM difficulty baseline register with exactly 23 ticket rows (every row that gives one ZOM ticket its own entry counts, whatever its status; a note line or cell note listing left-off tickets is not a ticket row)",
    "Accept: exactly 23 rows on the Tickets tab that each give one ZOM ticket its own entry, whatever the status cell says; a note line or cell note that lists left-off tickets, another tab, or text outside the sheet does not count toward the 23.", 5)
fix(28, "The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier",
    "The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier is set once they have played 10 games " + TIER, ACC, 3)
fix(49, "The Agent adds a new comment on Linear issue ZOM-199 saying the build sets the starting tier",
    "The Agent adds a new comment on Linear issue ZOM-199 saying the build sets the starting tier once a player has played 10 games " + TIER, ACC, 3)
fix(79, "The Agent tells Leonard in its DM reply that a new player's starting tier",
    "The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games " + TIER, ACC, 3)
for r in R:
    for k in ('title', 'justification', 'evidence'): assert '—' not in r[k] and '\r' not in r[k]
json.dump(R, open('task_inputs/09_Rubrics.json', 'w'), indent=2, ensure_ascii=False)
print('rows', len(R), 'weight', sum(r['weight'] for r in R))
