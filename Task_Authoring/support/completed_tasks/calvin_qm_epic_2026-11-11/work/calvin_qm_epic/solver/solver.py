"""Solver for calvin_qm_epic (tools/oracle_kit.py contract), rev3.

Truth = the stock-take Calvin's assistant should produce on Oct 1, 2025 from the base universe plus the injection SQL
(parsed with tools/base_check.parse_sql; never executed). The reports are the rows of Vincent's flow pass sheet, read from
the SQL's sheet grid, plus any bug told to Calvin in a DM since Sep 26. Each report gets one of three statuses under
Brian's note on ZOM-543, the ticket that holds it, and a review-list flag from Leonard's review card.

Base facts the rules need are constants here, each read through tools/hg.py at injection time: which #builds post each
build is and whether it was built from main (C05433XK267), and which match3d PRs are merged. One rule per
mechanism_portfolio entry; each reads its deciding record from the SQL and falls back to its natural reading when
`disable` switches it off (whole or per key set), when its channel's miss operator hits the key, or when the record is
absent. Over-application operators act on the rule's declared controls.
"""
import collections
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = json.loads((HERE.parent / "plan" / "seed_text.json").read_text())
ID = {k: v["id"] for k, v in SEED.items()}
P, Q, F = "Passed", "Waiting on QA", "Waiting on a fix"
AREAS = ["Tutorials", "Level-end rewards", "Daily Gift", "Season Pass", "Collect & Win", "Win Streak", "Zombie Lane", "Boss Arena",
         "Endless Mode", "Card packs"]
# base: the #builds post of each build a re-test names (C05433XK267/<ts>) and the branch it was built from
MAIN_BUILDS = {"iOS Internal #1713": "1758799630.301849", "Android #1974": "1758755609.200489", "iOS Internal #1727": "1758838873.487119",
               "Android #1984": "1758838918.332289", "Android Submission #129": "1758854356.576719", "iOS Internal #1745": "1759162758.968639",
               "Android #2006": "1759160363.685759", "Android #2010": "1759173998.691929", "Android #2013": "1759188882.419789",
               "iOS Internal #1750": "1759197354.452939", "iOS Internal #1754": "1759248081.891639", "iOS Internal #1757": "1759257787.502039",
               "Android Submission #135": "1759263189.219529"}
BRANCH_BUILDS = {"iOS Internal #1718": "1758817549.151639", "iOS Internal #1698": "1758737279.948339", "iOS Internal #1746": "1759173858.825639"}
CHAT_OK_BUILD = "iOS Internal #1718"          # base: D06UPGF5PQV/1758817744.353289 names it, D06UPGF5PQV/1758820544.160399 is the ok
MERGED_PRS = {"#465": "2025-09-25T22:15:51Z", "#472": "2025-09-30T15:53:04Z", "#473": "2025-09-30T15:41:20Z", "#475": "2025-09-30T16:09:15Z"}
BASE_TICKET_STATE = {"ZOM-556": "Todo", "ZOM-560": "Todo"}
STATE_FOR = {P: "Done", Q: "In Validation", F: "Todo"}
NEW_GATE, OLD_GATE = ["Collect & Win", "Level-end rewards"], ["Collect & Win", "Daily Gift"]
GLOW, GLOW_AREA = "Pass icon glow stays on after everything is claimed", "Season Pass"
DECOY = "Pass icon VFX remark in Vincent's chat"

KEY_REGEX = r".+"
FIELDS = ["Report", "Area", "Status", "Ticket", "Review list", "Why"]
CLASS_FIELD, GROUPS_FIELD = "Status", "groups"

R1, R2, R5, R7, R9, R11, R12, R13, R14, R17, R18, R19, R20, R21, R23, R24, R25, R27, R28, R29, R31, R32, R38 = (
    "Back to back tutorials at level 16-17 only play the first one", "Card upgrade tutorial never shows after the Zombie Lane one",
    "Coin animation plays again after killing and reopening the app", "Reward count-up is skipped when tapping fast on play",
    "Season pass popup comes up on top of the daily gift when both are due", "Daily gift day counter keeps going after a skipped day",
    "Season pass icon animation restarts every time a panel closes", "Season pass start popup shows again after every level until it is claimed",
    "Season pass reward claim animation plays twice when coming back from the shop", "Reward animation waits too long before the event bar fills",
    "Event panel opens over the level-end rewards on first unlock", "Event progress popup opens before the level-end coins finish",
    "Win streak freezer from the abandoned pack never shows up on the home screen", "Streak counter jumps by two after a win when other panels are waiting",
    "Zombie Lane panel opens twice after claiming", "Lane progress bar animates from zero every time",
    "Boss arena tutorial does not play when another tutorial is queued before it", "Arena entry button can be tapped during the reward animation",
    "Endless unlock banner overlaps the daily gift", "Coming back from Endless replays the home intro animation",
    "Tap to collect prompt is missing when a pack opens after a level", "Pack opening sound keeps playing on the home screen after the pack closes",
    "Pass progress bar fills before the tokens arrive")
R6, R8, R15, R22, R30, R33, R37 = (
    "Level-end coins fly while the pre-level panel is already open", "Stars from the level fly to the wrong corner on tablets",
    "Event bar starts filling while the daily gift popup is still open", "Zombie Lane reward animation plays under the home buttons",
    "Endless reward chest opens before the coins land", "Last pack does not show its cards before closing",
    "Win streak freezer popup opens behind the season pass popup")
PR472, PR475 = "harmonygames-Games/match3d#472", "harmonygames-Games/match3d#475"
BODY = {R6: ("body472", "#472", "the pre-level panel fix")}

RULES = {
    "BRANCH": {"mechanism": "A24", "requirement": "R3", "nodes": ["T_BRANCH"], "decides": ["Status"], "family": "done_gap",
               "natural_reading": "the sheet's ok is a pass", "source": "builds-channel", "signature": "main branch",
               "controls": [R5, R31, R33], "over_application": "branch_over"},
    "INLINE": {"mechanism": "A24", "requirement": "R3", "nodes": ["T_INLINE", "T_INLINE_PACK"], "decides": ["Status"], "family": "done_gap",
               "natural_reading": "a merged PR named in the sheet has the fix", "source": "github-inline", "signature": "isn't in this diff",
               "controls": [R18], "over_application": "inline_over"},
    "REOPEN": {"mechanism": "A11", "requirement": "R3", "nodes": ["T_REOPEN", "T_REOPEN_TICKET"], "decides": ["Status"], "family": "superseding",
               "natural_reading": "nr on a main build is a pass", "source": "old-thread-reply-qa", "signature": "on top of the gift again",
               "controls": [R7, R27], "over_application": "reopen_over"},
    "BACK": {"mechanism": "A11", "requirement": "R3", "nodes": ["T_BACK", "T_BACK_TICKET"], "decides": ["Status"], "family": "superseding",
             "natural_reading": "ok on a main build is a pass", "source": "old-thread-reply-founder", "signature": "home intro animation played again",
             "controls": [R23, R22], "over_application": "back_over"},
    "ELSE": {"mechanism": "A25", "requirement": "R3", "nodes": ["T_ELSE", "T_BODY"], "decides": ["Status"], "family": "completion_elsewhere",
             "natural_reading": "a blank Fix cell means no fix", "source": "pr-comment", "signature": "For the flow list",
             "controls": [R19, R30], "over_application": "else_over"},
    "FILT": {"mechanism": "A17", "requirement": "R1", "nodes": ["T_FILT"], "decides": ["Status"], "family": "exact_predicate",
             "natural_reading": "the sheet is the whole list", "source": "artist-chat", "signature": "icon glow",
             "controls": [DECOY], "over_application": "filt_over"},
    "ALIAS": {"mechanism": "A7", "requirement": "R4", "nodes": ["T_ALIAS_GIFT", "T_ALIAS_STREAK"], "decides": ["Ticket"], "family": "scope_alias",
              "natural_reading": "a blank Ticket cell means a new sub-issue", "source": "ticket-note", "signature": "Same thing",
              "controls": [R1, R38], "over_application": "alias_over"},
    "GATE": {"mechanism": "A12", "requirement": "R5", "nodes": ["T_GATE"], "decides": ["Review list"], "family": "authority",
             "natural_reading": "Brian's line in the chat names the review's areas", "source": "trello-card", "signature": "Level-end rewards",
             "controls": [R21, R28], "over_application": "gate_over"},
}
DEGRADES = {
    "branch_over": "un-passes a row whose ok was on a main build",
    "inline_over": "drops the PR from a row no reviewer excepted",
    "reopen_over": "reopens another nr row",
    "back_over": "reopens another ok row",
    "else_over": "marks a row merged that no dev named a merged PR for",
    "filt_over": "adds a chat remark that is not a bug seen in a build",
    "alias_over": "reuses a neighbouring ticket for a row that has none",
    "gate_over": "puts every open report on the review list, whatever its area",
    **{f"miss_{r.lower()}": f"the {r} channel's deciding record is not found: its member takes the natural reading" for r in
       ("BRANCH", "INLINE", "REOPEN", "BACK", "ELSE", "FILT", "ALIAS", "GATE")},
}
# old areas list Daily Gift, the changed card lists Level-end rewards: these are the rows whose flag differs between the two
GATE_MEMBERS = ["Daily gift calendar opens before the level-end coins finish", R11, R9,
                "Level-end coins fly while the pre-level panel is already open", "Stars from the level fly to the wrong corner on tablets",
                "Level-end rewards do not show at all right after an app update"]
MEMBERS = {"BRANCH": [R1, R2, R25], "INLINE": [R12, R15, R32], "REOPEN": [R9, R17], "BACK": [R29, R24], "ELSE": [R13, R14, R37, R38, R6], "FILT": [GLOW],
           "ALIAS": [R11, R20], "GATE": GATE_MEMBERS}
CHANNELS = {f"CH-{r}": {"kind": "scale", "degrade": f"miss_{r.lower()}", "members": MEMBERS[r], "latent": "member", "family": RULES[r]["family"],
                        "rule": r, "source": RULES[r]["source"], "description": RULES[r]["natural_reading"]} for r in RULES}


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id, grid = {}, None
    for x in parse_sql(sql_text):
        if x["op"] == "update" and x["table"].endswith("github_pull_requests") and "body" in x["set"]:
            by_id["body:" + str(x["where"]["id"])] = x["set"]        # the PR's description as the SQL leaves it
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "event_id", "identifier", "spreadsheet_id", "document_id", "presentation_id"):
            if r.get(k):
                by_id.setdefault(str(r[k]), r)
        if x["table"].endswith("sheets_sheets") and str(r.get("spreadsheet_id")) == ID["sheet"]:
            grid = r["grid_json"] if isinstance(r["grid_json"], list) else json.loads(r["grid_json"])
    rows = []
    if grid:
        head = grid[0]
        for line in grid[1:]:
            if line and str(line[0]).isdigit():
                rows.append(dict(zip(head, line)))
    states = {k: r.get("state_id") for k, r in by_id.items() if re.fullmatch(r"ZOM-\d+", k) and "state_id" in r}
    return {"by_id": by_id, "sheet": rows, "ticket_state": {**BASE_TICKET_STATE, **states}, "revision": revision or "rev1"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _off(rule, key, disable, degrade):
    return _hit(disable, rule, key) or (key in MEMBERS[rule] and _hit(degrade, f"miss_{rule.lower()}", key))


def _iso_epoch(iso):
    import datetime as _dt
    return _dt.datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=_dt.timezone.utc).timestamp()


def _retest(cell):
    """('ok' | 'nr' | 'again' | None, build or None) from the Re-test cell; 'ok, chat' points at the build named in the chat."""
    cell = (cell or "").strip()
    if cell == "ok, chat":
        return "ok", CHAT_OK_BUILD
    m = re.fullmatch(r"(ok|nr|again) (.+)", cell)
    return (m.group(1), m.group(2)) if m else (None, None)


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b          # noqa: E731
    out = {}
    items = [(r["What happens"], r) for r in state["sheet"]]
    items.append((GLOW, None))
    for k, r in items:
        if keys_ is not None and k not in keys_:
            continue
        why = []
        if r is None:                                   # the report raised in Marcus's chat
            if _off("FILT", k, disable, degrade) or not have(_slack_id(ID["filt_dm"])):
                out[k] = _blank(k)
                continue
            area, sheet_ticket, fix, verdict, build = GLOW_AREA, "", "", None, None
            why.append("Marcus told Calvin on 30 Sep, no ticket and no fix")
        else:
            area, sheet_ticket, fix = r["Area"], r["Ticket"], r["Fix"]
            verdict, build = _retest(r["Re-test"])
        # ---- passed?
        passed = verdict in ("ok", "nr")
        if passed and build not in MAIN_BUILDS and not _off("BRANCH", k, disable, degrade) and have(ID["rule_doc"]):
            passed = False
            why.append(f"the ok was on {build}, a feature-branch build, which does not count under Arthur's rule")
        if passed and k in (R5, R31, R33) and _hit(degrade, "branch_over", k):
            passed = False
        back = False
        if passed and k == R9 and not _off("REOPEN", k, disable, degrade) and have(_slack_id(ID["reopen"])):
            passed, back = False, True
            why.append("Vincent saw it again on Android Submission 135 after his nr")
        if passed and k == R29 and not _off("BACK", k, disable, degrade) and have(_slack_id(ID["back"])):
            passed, back = False, True
            why.append("Robert saw it again on Android Submission 135 after the ok")
        if passed and k == R17 and not _off("REOPEN", k, disable, degrade) and have(ID["reopen2"]):
            passed, back = False, True
            why.append("Samuel saw it again on Android Submission 135 after the ok (his note on ZOM-585)")
        if passed and k == R24 and not _off("BACK", k, disable, degrade) and have(ID["back2"]):
            passed, back = False, True
            why.append("Owen saw it again on Android Submission 135 after the nr (his note on ZOM-586)")
        if passed and ((k in (R7, R27) and _hit(degrade, "reopen_over", k)) or (k in (R23, R22) and _hit(degrade, "back_over", k))):
            passed, back = False, True
        # ---- merged fix?
        merged = None
        if not passed and not back:
            if fix in MERGED_PRS:
                merged = fix
                if verdict == "again" and build in MAIN_BUILDS and float(MAIN_BUILDS[build]) > _iso_epoch(MERGED_PRS[fix]):
                    merged = None                       # QA tried a main build made after the merge and it still happens
                    why.append(f"again on {build}, a main build made after {fix} merged, so the fix did not hold")
                elif verdict == "again":
                    why.append(f"the again was on {build}, made before {fix} merged, so QA has not tried the fix")
                if k in (R12, R15) and not _off("INLINE", k, disable, degrade) and have(ID["inline"]):
                    merged = None
                    why.append("Arthur's review on #472 says " + ("the icon restart" if k == R12 else "the event bar start") + " is not in that diff")
                if k == R32 and not _off("INLINE", k, disable, degrade) and have(ID["inline2"]):
                    merged = None
                    why.append("Arthur's review on #475 says the pack sound stop is not in it")
                if k == R18 and _hit(degrade, "inline_over", k):
                    merged = None
            elif k in (R13, R14, R37, R38) and not _off("ELSE", k, disable, degrade) and have(ID["else_pr"]):
                merged = "#473"
                why.append("Oliver wrote on his merged PR #473 that it has the fix")
            elif k in BODY and not _off("ELSE", k, disable, degrade) and have("body:" + ID[BODY[k][0]]):
                merged = BODY[k][1]
                why.append(f"the description of merged PR {merged} lists {BODY[k][2]}")
            if merged is None and k in (R19, R30) and _hit(degrade, "else_over", k):
                merged = "#473"
        status = P if passed else (Q if merged else F)
        if status == P:
            why.append(f"{verdict} on {build}, a main build")
        elif status == Q and not why:
            why.append(f"fix merged in {merged}, not re-tested on a main build")
        elif status == Q:
            why.append(f"{merged} is merged")
        elif not why:
            why.append("no merged fix and no pass")
        # ---- ticket
        ticket = sheet_ticket or None
        if k == R11 and not (_off("ALIAS", k, disable, degrade) or not have(ID["alias_gift"])):
            ticket = "ZOM-556"
        if k == R20 and not (_off("ALIAS", k, disable, degrade) or not have(ID["alias_streak"])):
            ticket = "ZOM-560"
        if k == R1 and _hit(degrade, "alias_over", k):
            ticket = "ZOM-567"
        if k == R38 and _hit(degrade, "alias_over", k):
            ticket = "ZOM-572"
        # ---- review list
        gate = OLD_GATE if (_off("GATE", k, disable, degrade) or not have(ID["rev_card_update"])) else NEW_GATE
        listed = status != P and area in gate
        if k in (R21, R28) and _hit(degrade, "gate_over", k) and status != P:
            listed = True
        was = state["ticket_state"].get(ticket) if ticket else None
        new_state = STATE_FOR[status]
        groups = ["report", "area:" + area, "status:" + status, "existing_ticket" if ticket else "new_sub_issue"]
        if listed:
            groups.append("review_list")
        if ticket and was != new_state:
            groups.append("state_change")
        out[k] = {"Report": k, "Area": area, "Status": status, "Ticket": ticket, "Review list": "Yes" if listed else "No",
                  "Why": "; ".join(why), "Ticket state": new_state, "Ticket state as found": was, "groups": sorted(groups)}
    if keys_ is None or DECOY in keys_:
        if _hit(degrade, "filt_over", DECOY):
            out[DECOY] = {"Report": DECOY, "Area": "Season Pass", "Status": F, "Ticket": None, "Review list": "No", "Why": "remark in Vincent's chat",
                          "Ticket state": "Todo", "Ticket state as found": None, "groups": ["area:Season Pass", "new_sub_issue", "report", "status:" + F]}
        else:
            out[DECOY] = _blank(DECOY)
    return out


def _blank(k):
    return {"Report": k, "Area": None, "Status": None, "Ticket": None, "Review list": None, "Why": None, "Ticket state": None,
            "Ticket state as found": None, "groups": []}


def _slack_id(chan_ts):
    import hashlib
    ch, ts = chan_ts.split("/")
    return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    listed = [v for v in rows.values() if v["Status"]]
    areas = {}
    for a in AREAS:
        mine = [v for v in listed if v["Area"] == a]
        open_n = sum(v["Status"] != P for v in mine)
        areas[a] = {"reports": len(mine), "open": open_n, "status": "Clear" if open_n == 0 else "Open"}
    return {"classes": dict(sorted(collections.Counter(v["Status"] for v in listed).items())),
            "groups": {g: groups[g] for g in sorted(groups)},
            "areas": areas,
            "totals": {"reports": len(listed), "passed": sum(v["Status"] == P for v in listed), "waiting_on_qa": sum(v["Status"] == Q for v in listed),
                       "waiting_on_a_fix": sum(v["Status"] == F for v in listed), "clear_areas": sum(a["status"] == "Clear" for a in areas.values()),
                       "review_list": len(groups.get("review_list", [])), "existing_tickets": len(groups.get("existing_ticket", [])),
                       "new_sub_issues": len(groups.get("new_sub_issue", [])), "state_changes": len(groups.get("state_change", []))}}


def evidence(rows, key, field):
    r = rows.get(key) or {}
    if field == "Ticket" and r.get("Ticket"):
        return [{R11: ID["alias_gift"], R20: ID["alias_streak"]}.get(key, ID["sheet"])]
    if field == "Area" and r.get("Area") and key not in (GLOW, DECOY):
        return [ID["sheet"]]
    return []


def touched(state, rule):
    if rule == "GATE":      # the review list follows every report that can be open in an area either card version lists, plus the controls
        return {r["What happens"] for r in state["sheet"] if r["Area"] in set(NEW_GATE + OLD_GATE)} | {R21, R28}
    return set(MEMBERS[rule]) | set(RULES[rule]["controls"])


def deciding(state, rule, key):
    return {"BRANCH": [ID["rule_doc"]], "INLINE": [ID["inline2"] if key == R32 else ID["inline"]],
            "REOPEN": [ID["reopen2"] if key == R17 else _slack_id(ID["reopen"])],
            "BACK": [ID["back2"] if key == R24 else _slack_id(ID["back"])],
            "ELSE": [ID[BODY[key][0]] if key in BODY else ID["else_pr"]], "FILT": [_slack_id(ID["filt_dm"])],
            "ALIAS": [ID["alias_streak"] if key == R20 else ID["alias_gift"]], "GATE": [ID["rev_card_update"]]}[rule]


def base_route(record_id):
    return None
