"""Planned truth for calvin_qm_epic: 10 areas, 38 rows of Vincent's QA pass sheet and 2 reports outside it.
Design data for /create-injection; not prompt, Oracle Event or criterion text."""
AREAS = ["Tutorials", "Level-end rewards", "Daily Gift", "Season Pass", "Collect & Win", "Win Streak", "Zombie Lane", "Boss Arena", "Endless Mode", "Card packs"]
P, Q, F = "Passed", "Waiting on QA", "Waiting on a fix"
# n, area, what happens, found on, ticket in sheet, fix, re-test, truth status, natural status, trap, existing ticket (truth)
R = [
 (1, "Tutorials", "Back to back tutorials at level 16-17 only play the first one", "iOS Internal #1710", "ZOM-567", "#465", "ok, chat", Q, P, "BRANCH", "ZOM-567"),
 (2, "Tutorials", "Card upgrade tutorial never shows after the Zombie Lane one", "Android #1974", "", "#465", "ok iOS Internal #1727", P, P, "", ""),
 (3, "Tutorials", "Hand pointer on the close button is missing in the Zombie Lane tutorial", "iOS Internal #1710", "ZOM-568", "#465", "ok iOS Internal #1727", P, P, "", "ZOM-568"),
 (4, "Tutorials", "Win streak tutorial at level 20 freezes the home screen", "Android #1974", "ZOM-569", "", "", F, F, "", "ZOM-569"),
 (5, "Level-end rewards", "Coin animation plays again after killing and reopening the app", "iOS Internal #1710", "ZOM-570", "#465", "ok, chat", Q, P, "BRANCH", "ZOM-570"),
 (6, "Level-end rewards", "Level-end coins fly while the pre-level panel is already open", "Android #1974", "", "", "", F, F, "", ""),
 (7, "Level-end rewards", "Reward count-up is skipped when tapping fast on play", "iOS Internal #1727", "ZOM-571", "", "nr iOS Internal #1745", P, P, "", "ZOM-571"),
 (8, "Level-end rewards", "Stars from the level fly to the wrong corner on tablets", "Android Submission #129", "", "", "", F, F, "", ""),
 (9, "Daily Gift", "Season pass popup comes up on top of the daily gift when both are due", "iOS Internal #1727", "ZOM-572", "", "nr iOS Internal #1745", F, P, "REOPEN", "ZOM-572"),
 (10, "Daily Gift", "Daily gift calendar opens before the level-end coins finish", "Android #1984", "", "", "", F, F, "", ""),
 (11, "Daily Gift", "Claim button on the daily gift stays grey the first time it opens after a level", "iOS Internal #1727", "", "", "", F, F, "ALIAS", "ZOM-573"),
 (12, "Season Pass", "Season pass tokens fly at the same time as the level-end coins", "Android #1974", "ZOM-574", "#472", "", F, Q, "INLINE", "ZOM-574"),
 (13, "Season Pass", "Season pass start popup shows again after every level until it is claimed", "iOS Internal #1727", "ZOM-575", "", "", F, F, "", "ZOM-575"),
 (14, "Season Pass", "Season pass reward claim animation plays twice when coming back from the shop", "iOS Internal #1745", "", "", "", F, F, "", ""),
 (15, "Collect & Win", "After a level the event bar shows a placeholder icon and old progress first", "Android #2004", "", "", "", Q, F, "ELSE", ""),
 (16, "Collect & Win", "Event token counter is visible in Boss Arena and Endless", "Android #2004", "", "", "", Q, F, "ELSE", ""),
 (17, "Collect & Win", "Reward animation waits too long before the event bar fills", "iOS Internal #1750", "ZOM-576", "#472", "ok iOS Internal #1754", P, P, "", "ZOM-576"),
 (18, "Collect & Win", "Event panel opens over the level-end rewards on first unlock", "iOS Internal #1750", "ZOM-577", "#472", "", Q, Q, "", "ZOM-577"),
 (19, "Collect & Win", "Grand prize popup can be closed before the reward lands", "Android #2013", "", "", "", F, F, "", ""),
 (20, "Win Streak", "Nathan's chest opens over the level-end rewards", "Android #1984", "", "", "", F, F, "ALIAS", "ZOM-578"),
 (21, "Win Streak", "Streak counter jumps by two after a win when other panels are waiting", "iOS Internal #1745", "ZOM-579", "", "", F, F, "", "ZOM-579"),
 (22, "Zombie Lane", "Zombie Lane reward animation plays under the home buttons", "iOS Internal #1727", "ZOM-580", "", "nr Android #2006", P, P, "", "ZOM-580"),
 (23, "Zombie Lane", "Zombie Lane panel opens twice after claiming", "Android #1984", "", "", "ok Android #2006", P, P, "", ""),
 (24, "Zombie Lane", "Lane progress bar animates from zero every time", "iOS Internal #1745", "", "", "ok Android #2010", P, P, "", ""),
 (25, "Boss Arena", "Boss arena tutorial plays again after finishing the event", "iOS Internal #1710", "ZOM-581", "#465", "ok, chat", Q, P, "BRANCH", "ZOM-581"),
 (26, "Boss Arena", "Boss arena unlock popup shows behind the level-end rewards", "Android #1984", "ZOM-582", "", "nr Android #2006", P, P, "", "ZOM-582"),
 (27, "Boss Arena", "Arena entry button can be tapped during the reward animation", "iOS Internal #1727", "", "", "nr iOS Internal #1745", P, P, "", ""),
 (28, "Endless Mode", "Endless unlock banner overlaps the daily gift", "Android #1984", "ZOM-583", "", "", F, F, "", "ZOM-583"),
 (29, "Endless Mode", "Coming back from Endless replays the home intro animation", "iOS Internal #1745", "", "", "ok iOS Internal #1750", P, P, "", ""),
 (30, "Endless Mode", "Endless reward chest opens before the coins land", "Android #2006", "", "", "", F, F, "", ""),
 (31, "Card packs", "Tap to collect prompt is missing when a pack opens after a level", "iOS Internal #1746", "ZOM-584", "#475", "ok iOS Internal #1757", P, P, "", "ZOM-584"),
 (32, "Card packs", "Close button on the pack screen can be tapped mid animation", "iOS Internal #1746", "ZOM-585", "#475", "", F, Q, "INLINE", "ZOM-585"),
 (33, "Card packs", "Last pack does not show its cards before closing", "iOS Internal #1746", "", "#475", "ok iOS Internal #1757", P, P, "", ""),
 (34, "Card packs", "New card red dot stays after opening the pack", "Android #2006", "ZOM-586", "", "", F, F, "", "ZOM-586"),
 (35, "Tutorials", "Tutorial hand stays on screen after the last panel closes", "iOS Internal #1727", "", "", "nr iOS Internal #1745", P, P, "", ""),
 (36, "Level-end rewards", "Level-end rewards do not show at all right after an app update", "Android Submission #129", "", "", "", F, F, "", ""),
 (37, "Win Streak", "Win streak freezer popup opens behind the season pass popup", "iOS Internal #1745", "", "", "", F, F, "", ""),
 (38, "Season Pass", "Pass progress bar fills before the tokens arrive", "Android #1984", "", "", "", F, F, "", ""),
]
OUTSIDE = [
 (39, "Season Pass", "New stage banner of the pass stays over the home buttons until restart", "", "", "", "", F, None, "MAIL", ""),
 (40, "Card packs", "Pack cards fly to the inventory behind the home buttons after a level", "", "", "", "", F, None, "FILT", ""),
]
GATE_AREAS = ["Collect & Win", "Level-end rewards"]          # the moved review invite
OLD_GATE_AREAS = ["Collect & Win", "Daily Gift"]             # Brian's earlier line
MAIN_BUILDS = {"iOS Internal #1710": "C05433XK267/1758755507.343299", "Android #1974": "C05433XK267/1758755609.200489", "iOS Internal #1727": "C05433XK267/1758838873.487119",
 "Android #1984": "C05433XK267/1758838918.332289", "Android Submission #129": "C05433XK267/1758854356.576719", "iOS Internal #1745": "C05433XK267/1759162758.968639",
 "Android #2006": "C05433XK267/1759160363.685759", "Android #2010": "C05433XK267/1759173998.691929", "Android #2013": "C05433XK267/1759188882.419789",
 "iOS Internal #1750": "C05433XK267/1759197354.452939", "iOS Internal #1754": "C05433XK267/1759248081.891639", "iOS Internal #1757": "C05433XK267/1759257787.502039"}
BRANCH_BUILDS = {"iOS Internal #1718": "C05433XK267/1758817549.151639", "iOS Internal #1746": "C05433XK267/1759173858.825639", "Android #2004": "C05433XK267/1759149639.741779"}
def truth():
    rows = []
    for n, area, what, found, tk, fix, rt, st, nat, trap, ex in R + OUTSIDE:
        rows.append(dict(n=n, area=area, report=what, found_on=found, sheet_ticket=tk, fix=fix, retest=rt, status=st, natural=nat, trap=trap,
                         existing_ticket=ex, line=("note on " + ex) if ex else "new sub-issue", holds=(st != P and area in GATE_AREAS),
                         new_state={P: "Done", Q: "In Validation", F: "Todo"}[st]))
    return rows
if __name__ == "__main__":
    import collections, json
    t = truth()
    print(len(t), collections.Counter(r["status"] for r in t), "natural", collections.Counter(r["natural"] for r in t))
    print("existing", sum(1 for r in t if r["existing_ticket"]), "new", sum(1 for r in t if not r["existing_ticket"]), "holds", sum(r["holds"] for r in t))
    for a in AREAS:
        rs = [r for r in t if r["area"] == a]; print(a, len(rs), "Clear" if all(r["status"] == P for r in rs) else "Open", sum(r["status"] != P for r in rs))
    nat_hold = sum(1 for r in t if r["natural"] and r["natural"] != P and r["area"] in OLD_GATE_AREAS)
    print("natural holds under the old areas", nat_hold)
