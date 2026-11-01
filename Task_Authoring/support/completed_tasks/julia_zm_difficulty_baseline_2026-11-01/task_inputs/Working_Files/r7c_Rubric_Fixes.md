# Rubric fixes after /rubric FAIL r5: 4 rows only (R5, R28, R49, R79)

Change only these two fields in each row; weight, category and justification stay as they are. Every other row is unchanged.

## R5 (weight 5)

**Title:**

The Agent fills the Tickets tab of the ZM difficulty baseline register with exactly 23 ticket rows (every row that gives one ZOM ticket its own entry counts, whatever its status; a note line or cell note listing left-off tickets is not a ticket row)

**Evidence:**

Sources: Trello card 'Difficulty baseline (Julia)' 68daca5871dba40417a00383, rules 1-7; Leonard's reply under the ask, D05HB64NMQU/1759262838.442871; Leonard's reply under Julia's Sep 29 question, D05HB64NMQU/1759267002.665190; Leonard's 'notes for monday' doc f_f494073fc667097c3c2c6b; Blake's review comment harmonygames-Games/match3d#265#rc_7; Blake's review comment harmonygames-Games/match3d#271#rc_1; Blake's 'store builds for monday' mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>; Blake's reply 'editor stuff and ZOM-199, before Monday' julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>. Accept: exactly 23 rows on the Tickets tab that each give one ZOM ticket its own entry, whatever the status cell says; a note line or cell note that lists left-off tickets, another tab, or text outside the sheet does not count toward the 23.

## R28 (weight 3)

**Title:**

The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier is set once they have played 10 games (passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail)

**Evidence:**

Sources: match3d Assets/Scripts/DynamicDifficulty/TierManager.cs (totalGames == 10, cpm > 90.0f) and Player/WinHistory.cs; Trello card 'Difficulty baseline (Julia)' 68daca5871dba40417a00383, rule 5. Accept: passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail.

## R49 (weight 3)

**Title:**

The Agent adds a new comment on Linear issue ZOM-199 saying the build sets the starting tier once a player has played 10 games (passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail)

**Evidence:**

Sources: Blake's reply julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>; Trello card 'Difficulty baseline (Julia)' 68daca5871dba40417a00383, rule 6; match3d Assets/Scripts/DynamicDifficulty/TierManager.cs (totalGames == 10). Accept: passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail.

## R79 (weight 3)

**Title:**

The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games (passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail)

**Evidence:**

Sources: match3d Assets/Scripts/DynamicDifficulty/TierManager.cs (totalGames == 10, cpm > 90.0f) and Player/WinHistory.cs; Leonard's ask in the DM, D05HB64NMQU/1759261706.530914. Accept: passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail.
