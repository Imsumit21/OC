"""Planned truth for calvin_qm_epic (design-3, after the blind fork and coherence sweeps): 10 areas, 38 rows of Vincent's flow pass sheet
and 1 report outside it. Design data for /create-injection; not prompt, Oracle Event or criterion text."""
AREAS = ["Tutorials", "Level-end rewards", "Daily Gift", "Season Pass", "Collect & Win", "Win Streak", "Zombie Lane", "Boss Arena", "Endless Mode", "Card packs"]
P, Q, F = "Passed", "Waiting on QA", "Waiting on a fix"
# n, area, what happens, found on, ticket in sheet, fix, re-test, truth status, natural status, trap, existing ticket (truth)
R = [
 (1, "Tutorials", "Back to back tutorials at level 16-17 only play the first one", "iOS Internal #1698", "", "#465", "ok, chat", Q, P, "BRANCH", ""),
 (2, "Tutorials", "Card upgrade tutorial never shows after the Zombie Lane one", "iOS Internal #1698", "", "#465", "ok, chat", Q, P, "BRANCH", ""),
 (3, "Tutorials", "Quest tutorial arrow points at the wrong tab after the last panel closes", "iOS Internal #1713", "", "", "nr iOS Internal #1745", P, P, "", ""),
 (4, "Tutorials", "Win streak tutorial at level 20 freezes the home screen", "Android #1974", "ZOM-567", "", "", F, F, "", "ZOM-567"),
 (5, "Level-end rewards", "Coin animation plays again after killing and reopening the app", "iOS Internal #1713", "", "#465", "ok iOS Internal #1745", P, P, "", ""),
 (6, "Level-end rewards", "Level-end coins fly while the pre-level panel is already open", "Android #1974", "ZOM-568", "", "", F, F, "", "ZOM-568"),
 (7, "Level-end rewards", "Reward count-up is skipped when tapping fast on play", "iOS Internal #1727", "", "", "nr iOS Internal #1745", P, P, "", ""),
 (8, "Level-end rewards", "Stars from the level fly to the wrong corner on tablets", "Android Submission #129", "ZOM-569", "", "", F, F, "", "ZOM-569"),
 (9, "Daily Gift", "Season pass popup comes up on top of the daily gift when both are due", "iOS Internal #1727", "", "", "nr iOS Internal #1745", F, P, "REOPEN", ""),
 (10, "Daily Gift", "Daily gift calendar opens before the level-end coins finish", "Android #1984", "ZOM-570", "", "", F, F, "", "ZOM-570"),
 (11, "Daily Gift", "Daily gift day counter keeps going after a skipped day", "iOS Internal #1727", "", "", "", F, F, "ALIAS", "ZOM-556"),
 (12, "Season Pass", "Season pass icon animation restarts every time a panel closes", "Android #1984", "ZOM-571", "#472", "", F, Q, "INLINE", "ZOM-571"),
 (13, "Season Pass", "Season pass start popup shows again after every level until it is claimed", "iOS Internal #1727", "ZOM-572", "", "", Q, F, "ELSE", "ZOM-572"),
 (14, "Season Pass", "Season pass reward claim animation plays twice when coming back from the shop", "iOS Internal #1745", "ZOM-573", "", "", F, F, "", "ZOM-573"),
 (15, "Collect & Win", "Event bar starts filling while the daily gift popup is still open", "Android #2013", "ZOM-574", "", "", F, F, "", "ZOM-574"),
 (16, "Endless Mode", "Endless unlock banner shows again after coming back from a level", "Android #2006", "ZOM-575", "", "", F, F, "", "ZOM-575"),
 (17, "Collect & Win", "Reward animation waits too long before the event bar fills", "iOS Internal #1750", "", "#472", "ok iOS Internal #1754", P, P, "", ""),
 (18, "Collect & Win", "Event panel opens over the level-end rewards on first unlock", "iOS Internal #1750", "ZOM-576", "#472", "", Q, Q, "", "ZOM-576"),
 (19, "Collect & Win", "Event progress popup opens before the level-end coins finish", "Android #2013", "ZOM-577", "", "", F, F, "", "ZOM-577"),
 (20, "Win Streak", "Win streak freezer from the abandoned pack never shows up on the home screen", "Android #1984", "", "", "", F, F, "ALIAS", "ZOM-560"),
 (21, "Win Streak", "Streak counter jumps by two after a win when other panels are waiting", "iOS Internal #1745", "ZOM-578", "", "", F, F, "", "ZOM-578"),
 (22, "Zombie Lane", "Zombie Lane reward animation plays under the home buttons", "iOS Internal #1727", "", "", "nr Android #2006", P, P, "", ""),
 (23, "Zombie Lane", "Zombie Lane panel opens twice after claiming", "Android #1984", "", "", "ok Android #2006", P, P, "", ""),
 (24, "Zombie Lane", "Lane progress bar animates from zero every time", "iOS Internal #1745", "", "", "ok Android #2010", P, P, "", ""),
 (25, "Boss Arena", "Boss arena tutorial plays again after finishing the event", "iOS Internal #1713", "", "#465", "ok, chat", Q, P, "BRANCH", ""),
 (26, "Boss Arena", "Boss arena unlock popup shows behind the level-end rewards", "Android #1984", "", "", "nr Android #2006", P, P, "", ""),
 (27, "Boss Arena", "Arena entry button can be tapped during the reward animation", "iOS Internal #1727", "", "", "nr iOS Internal #1745", P, P, "", ""),
 (28, "Endless Mode", "Endless unlock banner overlaps the daily gift", "Android #1984", "ZOM-579", "", "", F, F, "", "ZOM-579"),
 (29, "Endless Mode", "Coming back from Endless replays the home intro animation", "iOS Internal #1745", "", "", "ok iOS Internal #1750", F, P, "BACK", ""),
 (30, "Endless Mode", "Endless reward chest opens before the coins land", "Android #2006", "ZOM-580", "", "", F, F, "", "ZOM-580"),
 (31, "Card packs", "Tap to collect prompt is missing when a pack opens after a level", "iOS Internal #1746", "", "#475", "ok iOS Internal #1757", P, P, "", ""),
 (32, "Card packs", "Pack opening sound keeps playing on the home screen after the pack closes", "iOS Internal #1746", "ZOM-581", "#475", "", F, Q, "INLINE", "ZOM-581"),
 (33, "Card packs", "Last pack does not show its cards before closing", "iOS Internal #1746", "", "#475", "ok iOS Internal #1757", P, P, "", ""),
 (34, "Card packs", "Pack count on the home button only updates after a restart", "Android #2006", "ZOM-582", "", "", F, F, "", "ZOM-582"),
 (35, "Tutorials", "Tutorial hand stays on screen after the last panel closes", "iOS Internal #1727", "", "", "nr iOS Internal #1745", P, P, "", ""),
 (36, "Level-end rewards", "Level-end rewards do not show at all right after an app update", "Android Submission #129", "ZOM-583", "", "", F, F, "", "ZOM-583"),
 (37, "Win Streak", "Win streak freezer popup opens behind the season pass popup", "iOS Internal #1745", "ZOM-584", "", "", F, F, "", "ZOM-584"),
 (38, "Season Pass", "Pass progress bar fills before the tokens arrive", "Android #1984", "", "", "", Q, F, "ELSE", ""),
]
OUTSIDE = [
 (39, "Season Pass", "Pass icon glow stays on after everything is claimed", "", "", "", "", F, None, "FILT", ""),
]
GATE_AREAS = ["Collect & Win", "Level-end rewards"]          # the moved review invite
OLD_GATE_AREAS = ["Collect & Win", "Daily Gift"]             # Brian's earlier line
# seeded ticket states as Vincent files them on 30 Sep (after base ZOM-566, created 2025-09-30T16:26Z)
SEEDED_STATE = {"ZOM-571": "In Validation", "ZOM-576": "In Validation", "ZOM-581": "In Validation"}   # every other seeded ticket is Todo
BASE_TICKETS = {"ZOM-556": "Todo", "ZOM-560": "Todo"}
MAIN_BUILDS = {"iOS Internal #1713": "C05433XK267/1758799630.301849", "Android #1974": "C05433XK267/1758755609.200489", "iOS Internal #1727": "C05433XK267/1758838873.487119",
 "Android #1984": "C05433XK267/1758838918.332289", "Android Submission #129": "C05433XK267/1758854356.576719", "iOS Internal #1745": "C05433XK267/1759162758.968639",
 "Android #2006": "C05433XK267/1759160363.685759", "Android #2010": "C05433XK267/1759173998.691929", "Android #2013": "C05433XK267/1759188882.419789",
 "iOS Internal #1750": "C05433XK267/1759197354.452939", "iOS Internal #1754": "C05433XK267/1759248081.891639", "iOS Internal #1757": "C05433XK267/1759257787.502039"}
BRANCH_BUILDS = {"iOS Internal #1718": "C05433XK267/1758817549.151639", "iOS Internal #1698": "C05433XK267/1758737279.948339", "iOS Internal #1746": "C05433XK267/1759173858.825639"}
def truth():
    rows = []
    for n, area, what, found, tk, fix, rt, st, nat, trap, ex in R + OUTSIDE:
        new_state = {P: "Done", Q: "In Validation", F: "Todo"}[st]
        cur = (SEEDED_STATE.get(ex, "Todo") if ex.startswith("ZOM-5") and ex not in BASE_TICKETS else BASE_TICKETS.get(ex)) if ex else None
        rows.append(dict(n=n, area=area, report=what, found_on=found, sheet_ticket=tk, fix=fix, retest=rt, status=st, natural=nat, trap=trap,
                         existing_ticket=ex, line=("note on " + ex) if ex else "new sub-issue", holds=(st != P and area in GATE_AREAS),
                         new_state=new_state, ticket_state_as_found=cur, state_change=bool(ex and cur != new_state)))
    return rows
if __name__ == "__main__":
    import collections
    t = truth()
    print(len(t), collections.Counter(r["status"] for r in t), "natural", collections.Counter(r["natural"] for r in t))
    print("existing", sum(1 for r in t if r["existing_ticket"]), "new", sum(1 for r in t if not r["existing_ticket"]), "holds", sum(r["holds"] for r in t), "state changes", [r["existing_ticket"] for r in t if r["state_change"]])
    for a in AREAS:
        rs = [r for r in t if r["area"] == a]; print(a, len(rs), "Clear" if all(r["status"] == P for r in rs) else "Open", sum(r["status"] != P for r in rs))
    print("natural holds under the old areas", sum(1 for r in t if r["natural"] and r["natural"] != P and r["area"] in OLD_GATE_AREAS))
    print("sheet tickets", sorted({r["sheet_ticket"] for r in t if r["sheet_ticket"]}))
