# Rubric fixes after /rubric FAIL r4 (81 rows, weight 173)

Apply in the builder, export, then run /rubric. Old row numbers are the reviewed rubric's.

## Delete

- R5: The Agent fills the Tickets tab of the ZM difficulty baseline register with exactly 23 ticket rows with a status of Live, Editor only, Replaced or Not shipped (left-off tickets listed without one of these statuses are not counted)
- R24: The Agent gives the Tickets tab of the ZM difficulty baseline register a column each for the ticket's Linear assignee, the day it was marked done and its Linear priority
- R28: The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier is set once they have played 10 games (passes: wording that counts 10 games, attempts, plays or levels played, or a count of levels that says losses or replays count, with or without a CPM average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 levels with no timing)
- R49: The Agent adds a new comment on Linear issue ZOM-173 saying its change is not in the store builds iOS 0.3.49 and Android 0.3.133 (any wording that names both builds as lacking the change passes)
- R50: The Agent adds a new comment on Linear issue ZOM-200 saying its change is not in the store builds iOS 0.3.49 and Android 0.3.133 (any wording that names both builds as lacking the change passes)
- R51: The Agent adds a new comment on Linear issue ZOM-277 saying its change is not in the store builds iOS 0.3.49 and Android 0.3.133 (any wording that names both builds as lacking the change passes)
- R52: The Agent adds a new comment on Linear issue ZOM-202 saying its change is not in the store builds iOS 0.3.49 and Android 0.3.133 (any wording that names both builds as lacking the change passes)
- R53: The Agent adds a new comment on Linear issue ZOM-280 saying its change is not in the store builds iOS 0.3.49 and Android 0.3.133 (any wording that names both builds as lacking the change passes)
- R54: The Agent adds a new comment on Linear issue ZOM-315 saying its change is not in the store builds iOS 0.3.49 and Android 0.3.133 (any wording that names both builds as lacking the change passes)
- R55: The Agent adds a new comment on Linear issue ZOM-293 saying its change is not in the store builds iOS 0.3.49 and Android 0.3.133 (any wording that names both builds as lacking the change passes)
- R69: The Agent names exactly ZOM-173, ZOM-200, ZOM-277 and ZOM-315 as the Editor only tickets in its DM reply to Leonard
- R71: The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games (passes: wording that counts 10 games, attempts, plays or levels played, or a count of levels that says losses or replays count, with or without a CPM average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 levels with no timing)

## Changed or new rows (new numbering; copy each field from task_inputs/09_Rubrics.json)

| New # | Change | Title | Weight |
|---|---|---|---|
| 5 | NEW (or retitled) | The Agent fills the Tickets tab of the ZM difficulty baseline register with exactly 23 ticket rows (every row on the Tickets tab that names a ZOM ticket counts toward the 23; a list of left-off tickets passes only on another tab or outside the sheet) | 5 |
| 6 | justification/evidence only | The Agent records exactly 15 tickets with the status Live on the Tickets tab of the ZM difficulty baseline register | 5 |
| 7 | justification/evidence only | The Agent records exactly 4 tickets with the status Editor only on the Tickets tab of the ZM difficulty baseline register | 5 |
| 27 | NEW (or retitled) | The Agent marks ZOM-280 as never done in the done-day column of the Tickets tab of the ZM difficulty baseline register (ZOM-280 was never marked done; a cell with no date passes: empty, a dash, N/A or a never-done note; any date, including its 2025-06-20 cancel date, fails) | 1 |
| 28 | NEW (or retitled) | The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier is set once they have played 10 games (passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count, with or without a CPM average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', 'after the first 10 levels played', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 levels with no timing) | 3 |
| 30 | NEW (or retitled) | The Agent states on the Rules in force tab of the ZM difficulty baseline register that new players who miss the tier 1 threshold start on tier 0 | 1 |
| 49 | NEW (or retitled) | The Agent adds a new comment on Linear issue ZOM-199 saying the build sets the starting tier once a player has played 10 games (passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count; fails: a count of levels with nothing saying losses or replays count, 'after level 10' or 'once level 10 is cleared') | 3 |
| 51 | NEW (or retitled) | The Agent adds a new comment on Linear issue ZOM-173 saying its change is not in the store builds players have today | 3 |
| 52 | NEW (or retitled) | The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue ZOM-173 | 1 |
| 53 | NEW (or retitled) | The Agent adds a new comment on Linear issue ZOM-200 saying its change is not in the store builds players have today | 3 |
| 54 | NEW (or retitled) | The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue ZOM-200 | 1 |
| 55 | NEW (or retitled) | The Agent adds a new comment on Linear issue ZOM-277 saying its change is not in the store builds players have today | 3 |
| 56 | NEW (or retitled) | The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue ZOM-277 | 1 |
| 57 | NEW (or retitled) | The Agent adds a new comment on Linear issue ZOM-202 saying its change is not in the store builds players have today | 3 |
| 58 | NEW (or retitled) | The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue ZOM-202 | 1 |
| 59 | NEW (or retitled) | The Agent adds a new comment on Linear issue ZOM-280 saying its change is not in the store builds players have today | 3 |
| 60 | NEW (or retitled) | The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue ZOM-280 | 1 |
| 61 | NEW (or retitled) | The Agent adds a new comment on Linear issue ZOM-315 saying its change is not in the store builds players have today | 3 |
| 62 | NEW (or retitled) | The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue ZOM-315 | 1 |
| 63 | NEW (or retitled) | The Agent adds a new comment on Linear issue ZOM-293 saying its change is not in the store builds players have today | 3 |
| 64 | NEW (or retitled) | The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue ZOM-293 | 1 |
| 79 | NEW (or retitled) | The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games (passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count, with or without a CPM average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', 'after the first 10 levels played', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 levels with no timing) | 3 |
