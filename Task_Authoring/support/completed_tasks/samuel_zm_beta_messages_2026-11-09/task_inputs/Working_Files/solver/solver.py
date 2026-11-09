"""Solver for samuel_zm_beta_messages (tools/oracle_kit.py contract), rev1.

Truth = the beta message plan Samuel should write as of the end of Tue Sep 30, 2025 (Pacific), from the base universe plus the
injection SQL (parsed with tools/base_check.parse_sql; never executed). Each message runs through Leonard's rule doc: six ordered
tests, stop at the first that fails. Go passes all six; Drop fails test 1 or is already covered by another message; Hold is
anything else, and names the test it failed.

Per-message facts that do not depend on a designed mechanism come from the cohort table in plan/ids.json (the scenario
builder's output; each row's deciding records are in the SQL or the base). One rule per mechanism_portfolio entry; each reads
its deciding record and falls back to its natural reading when `disable` switches it off (whole or per key set) or the record
is absent. Over-application operators act on the rule's declared controls.
"""
import collections
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
P = json.loads((HERE.parent / "plan" / "ids.json").read_text())
SQL_IDS = json.loads((HERE.parent / "plan" / "sql_ids.json").read_text())["ids"]
PN_ROWS = {int(k): v for k, v in json.loads((HERE.parent / "plan" / "pn_rows.json").read_text()).items()}
I, TK, NEW_LINE, SLACK_LINE = P["ids"], P["tickets"], P["new_line"], P["slack_line"]
SL = SQL_IDS["slack_mid"]
MEMBERS = P["members"]
DECOYS = [d[0] for d in P["decoys"]]

KEY_REGEX = r".+"
FIELDS = ["Message", "Ticket", "Call", "What's missing", "Audience", "Final headline", "String change"]
CLASS_FIELD, GROUPS_FIELD = "Call", "groups"
NOT_SCHEDULED, WRONG_DAY = "not scheduled in the client", "fires on the wrong day"
NO_REACH, NOT_SEEN = "cannot reach its players", "not seen on both platforms"

RULES = {
    "DONE": {"mechanism": "A24", "requirement": "R3", "nodes": ["T1", "C1"], "decides": ["Call", "What's missing"],
             "natural_reading": "Weekly Leaderboard reset Go: Ready, Done, seen on both", "family": "done_gap",
             "source": "pr-inline", "signature": "Arthur inline rollover",
             "controls": ["Lapsed 1 day"], "over_application": "done_over"},
    "CORR": {"mechanism": "A11", "requirement": "R4", "nodes": ["T2", "C2"], "decides": ["Final headline"],
             "natural_reading": "Lapsed 7 days takes Leonard's Sep 29 thread line", "family": "superseding",
             "source": "calendar-note", "signature": "copy check later line",
             "controls": ["Lapsed 1 day"], "over_application": "corr_over"},
    "DEP": {"mechanism": "A4", "requirement": "R3", "nodes": ["T3", "C3"], "decides": ["Call", "What's missing"],
            "natural_reading": "Finish first mission Go: Ready, LIVE, seen on both", "family": "authority",
            "source": "join", "signature": "level 20 ask vs level 20 trigger",
            "controls": ["Lapsed 1 day"], "over_application": "dep_over"},
    "QA": {"mechanism": "A14", "requirement": "R3", "nodes": ["T4", "C4"], "decides": ["Call", "What's missing"],
           "natural_reading": "Plague Race Go: Vincent passed it on the ticket", "family": "superseding",
           "source": "dm-thread", "signature": "race one 5-minute timers build",
           "controls": ["Lapsed 7 days"], "over_application": "qa_over"},
    "PULL": {"mechanism": "A14", "requirement": "R3", "nodes": ["T16", "C9"], "decides": ["Call", "What's missing"],
             "natural_reading": "Lives recharged Go: Vincent's tick stands", "family": "superseding",
             "source": "channel-root", "signature": "Full Ammo tick off",
             "controls": ["Lapsed 1 day"], "over_application": "pull_over"},
    "ALIAS": {"mechanism": "A7", "requirement": "R6", "nodes": ["T5", "C5"], "decides": ["Ticket"],
              "natural_reading": "a new ticket for the Win & Collect row", "family": "scope_alias",
              "source": "linear-name", "signature": "Collect and Win ping",
              "controls": ["Season Pass start"], "over_application": "alias_over"},
    "FILT": {"mechanism": "A17", "requirement": "R1", "nodes": ["T6", "C6"], "decides": ["Call"],
             "natural_reading": "the plan stops at the sheet rows and the parent's children", "family": "exact_predicate",
             "source": "linear-offlist", "signature": "phone reminder comment",
             "controls": ["Plague Race red dot"], "over_application": "filt_over"},
    "BUILT": {"mechanism": "A25", "requirement": "R2", "nodes": ["T7", "C7"], "decides": ["Call", "What's missing"],
              "natural_reading": "Lapsed 14 days is a Hold", "family": "completion_elsewhere",
              "source": "code-read", "signature": "weekly batch day 14",
              "controls": ["Lapsed 30 days"], "over_application": "built_over"},
    "FOLLOW": {"mechanism": "A15", "requirement": "R7", "nodes": ["T8", "C8"], "decides": ["Ticket state"],
               "natural_reading": "Hold tickets go back to Todo", "family": "superseding",
               "source": "card-desc", "signature": "held tickets Backlog",
               "controls": ["Axe Arena"], "over_application": "follow_over"},
}
DEGRADES = {
    "done_over": "holds Lapsed 1 day for not being exactly 24 hours",
    "corr_over": "rewrites Lapsed 1 day's headline as well",
    "dep_over": "holds Lapsed 1 day because some of its players are below the ask",
    "qa_over": "doubts Vincent's pass on Lapsed 7 days",
    "pull_over": "takes Lapsed 1 day off the Go list as well",
    "alias_over": "merges Season Pass start into the Season Pass last 48 hours ticket",
    "filt_over": "adds the Plague Race red dot to the plan",
    "built_over": "drops Lapsed 30 days too, as if the weekly batch reached it",
    "follow_over": "parks the Axe Arena Drop ticket in Backlog too",
    "ch_miss": "a channel member's deciding record is not found: the member takes its natural reading",
}


def _ch(rule, members, family, source, description):
    return {"kind": "scale", "degrade": "ch_miss", "members": members, "latent": "member", "family": family, "rule": rule,
            "source": source, "description": description}


CHANNELS = {
    "CH-DONE": _ch("DONE", ["Weekly Leaderboard reset"], "done_gap", "pr-inline",
                   "Arthur's inline comment on PR #248 is not read and the schedule is not read closely: the message looks finished"),
    "CH-CORR": _ch("CORR", ["Lapsed 7 days"], "superseding", "calendar-note",
                   "Leonard's later note on the copy check is not read: his Sep 29 line stands"),
    "CH-DEP": _ch("DEP", ["Finish first mission"], "authority", "join",
                  "the level 20 trigger is not joined to the ask point and the reach test: the message goes"),
    "CH-QA": _ch("QA", ["Plague Race"], "superseding", "dm-thread",
                 "Vincent's DM thread reply is not opened: his ticket pass stands"),
    "CH-PULL": _ch("PULL", ["Lives recharged"], "superseding", "channel-root",
                   "Vincent's channel post is not read: his tick on Lives recharged stands"),
    "CH-ALIAS": _ch("ALIAS", ["Win & Collect start"], "scope_alias", "linear-name",
                    "the ticket under the other name is not found: a second ticket is filed"),
    "CH-FILT": _ch("FILT", ["Boss Arena attempts refilled", "Daily gift about to reset", "Teammate sent lives", "Infinite lives ending"], "exact_predicate", "linear-offlist",
                   "the asks in comments on other tickets are not followed: they miss the plan"),
    "CH-BUILT": _ch("BUILT", ["Lapsed 14 days"], "completion_elsewhere", "code-read",
                    "the weekly batch is not read as covering day 14: the ask stays a Hold"),
    "CH-FOLLOW": _ch("FOLLOW", ["Quests rollover", "Login Calendar update", "Boss Arena open"], "superseding", "card-desc",
                     "Leonard's note in the tech issues card's description is not read: held tickets go to Todo"),
    "CH-SLIP": {"kind": "scale", "degrade": None, "members": [], "latent": "member", "family": "slip",
                "slots": ["K2", "K3", "K5", "K6", "K9", "K14", "K15", "X17", "X20"],
                "description": "a base slip on a control row, the ladder or the group who hears nothing"},
}
CHANNEL_RULE = {k: c["rule"] for c in CHANNELS.values() if c.get("rule") for k in c["members"]}


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id = {}
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "event_id", "identifier", "spreadsheet_id", "document_id", "presentation_id"):
            if r.get(k):
                by_id[str(r[k])] = r
    return {"by_id": by_id, "revision": revision or "rev1"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _off(rule, key, disable, degrade):
    return _hit(disable, rule, key) or (CHANNEL_RULE.get(key) == rule and _hit(degrade, "ch_miss", key))


def _headline(m):
    src = m["source"]
    return PN_ROWS[int(src.rsplit(" ", 1)[1])]["headline"] if src.startswith("PNs Beta") else None


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b          # noqa: E731
    out = {}
    for m in MEMBERS:
        k = m["key"]
        if keys_ is not None and k not in keys_:
            continue
        call, missing, ticket, listed = m["call"], m["missing"] or None, m["ticket"], True
        line, change = None, None
        # ---- designed mechanisms (each falls back to its natural reading)
        if k == "Weekly Leaderboard reset" and (_off("DONE", k, disable, degrade) or not have(I["arthur_inline"])):
            call, missing = "Go", None
        if k == "Finish first mission" and (_off("DEP", k, disable, degrade) or not have(SL["ask_decision"])):
            call, missing = "Go", None
        if k == "Plague Race" and (_off("QA", k, disable, degrade) or not have(SL["qa_reply"])):
            call, missing = "Go", None
        if k == "Lives recharged" and (_off("PULL", k, disable, degrade) or not have(SL["lives_pull"])):
            call, missing = "Go", None
        if k == "Lapsed 14 days" and (_off("BUILT", k, disable, degrade) or not have(SQL_IDS["cancel_mail"])):
            call, missing = "Hold", NOT_SCHEDULED
        if k == "Win & Collect start" and (_off("ALIAS", k, disable, degrade) or not have(TK[k])):
            ticket = None
        if k == "Boss Arena attempts refilled" and (_off("FILT", k, disable, degrade) or not have(I["boss_ask"])):
            listed = False
        if k == "Daily gift about to reset" and (_off("FILT", k, disable, degrade) or not have(I["gift_ask"])):
            listed = False
        if k == "Teammate sent lives" and (_off("FILT", k, disable, degrade) or not have(I["team_ask"])):
            listed = False
        if k == "Infinite lives ending" and (_off("FILT", k, disable, degrade) or not have(I["inf_ask"])):
            listed = False
        # ---- over-application operators on control members
        if k == "Lapsed 1 day" and _hit(degrade, "done_over", k):
            call, missing = "Hold", WRONG_DAY
        if k == "Lapsed 1 day" and _hit(degrade, "dep_over", k):
            call, missing = "Hold", NO_REACH
        if k == "Lapsed 7 days" and _hit(degrade, "qa_over", k):
            call, missing = "Hold", NOT_SEEN
        if k == "Lapsed 1 day" and _hit(degrade, "pull_over", k):
            call, missing = "Hold", NOT_SEEN
        if k == "Season Pass start" and _hit(degrade, "alias_over", k):
            ticket = TK["Season Pass last 48 hours"]
        if k == "Lapsed 30 days" and _hit(degrade, "built_over", k):
            call, missing = "Drop", None
        # ---- derived fields and writes
        if not listed:
            out[k] = {"Message": k, "Ticket": None, "Call": None, "What's missing": None, "Audience": None, "Final headline": None,
                      "String change": None, "Ticket state": None, "groups": []}
            continue
        if call == "Go":
            line, change = _headline(m), "No"
            corrected = not (_off("CORR", k, disable, degrade) or not have(I["copy_check"]))
            if k == "Lapsed 7 days":
                line, change = (NEW_LINE if corrected else SLACK_LINE), "Yes"
            if k == "Lapsed 1 day" and _hit(degrade, "corr_over", k):
                line, change = NEW_LINE, "Yes"
        state_after = {"Go": "unchanged", "Drop": "Canceled"}.get(call)
        if call == "Hold":
            state_after = "Todo" if (_off("FOLLOW", k, disable, degrade) or not have(I["freeze_comment"])) else "Backlog"
        if k == "Axe Arena" and _hit(degrade, "follow_over", k):
            state_after = "Backlog"
        groups = ["plan", "call_" + call.lower()]
        if ticket:
            groups.append("ticket_comment")
        else:
            groups.append("new_ticket")
        if change == "Yes":
            groups.append("string_ticket")
        if call == "Go":
            groups.append("checklist")
        if m["asker"] != "leonard" and not m["source"].startswith("PNs Beta"):
            groups.append("asker_" + m["asker"].split(".")[0])
        out[k] = {"Message": k, "Ticket": ticket, "Call": call, "What's missing": missing, "Audience": m["note"], "Final headline": line,
                  "String change": change, "Ticket state": state_after, "groups": sorted(groups)}
    for k in DECOYS:
        if keys_ is not None and k not in keys_:
            continue
        on_plan = k == "Plague Race red dot" and _hit(degrade, "filt_over", k)
        out[k] = {"Message": k, "Ticket": None, "Call": "Hold" if on_plan else None, "What's missing": NOT_SCHEDULED if on_plan else None,
                  "Audience": None, "Final headline": None, "String change": None, "Ticket state": None,
                  "groups": ["plan"] if on_plan else []}
    return out


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    listed = [v for v in rows.values() if v["Call"]]
    return {"classes": dict(sorted(collections.Counter(v["Call"] for v in listed).items())),
            "groups": {g: groups[g] for g in sorted(groups)},
            "totals": {"plan_rows": len(listed), "ticket_comments": len(groups.get("ticket_comment", [])),
                       "new_tickets": len(groups.get("new_ticket", [])) + len(groups.get("string_ticket", [])),
                       "checklist_items": len(groups.get("checklist", []))}}


def evidence(rows, key, field):
    r = rows.get(key) or {}
    t = TK.get(key)
    if field == "Ticket" and t and r.get("Ticket") == t:
        return [t]
    if field == "Audience" and r.get("Audience"):
        if key == "Boss Arena attempts refilled":
            return [I["boss_ask"]]
        if key == "Daily gift about to reset":
            return [I["gift_ask"]]
        if key == "Teammate sent lives":
            return [I["team_ask"]]
        if key == "Infinite lives ending":
            return [I["inf_ask"]]
        return [SQL_IDS["aud"][t]] if t in SQL_IDS["aud"] else []
    if field == "Final headline" and r.get("Final headline"):
        return [I["copy_check"]] if r["Final headline"] == NEW_LINE else ([t] if t else [])
    return []


def touched(state, rule):
    return {"DONE": {"Weekly Leaderboard reset"}, "CORR": {"Lapsed 7 days"}, "DEP": {"Finish first mission"}, "QA": {"Plague Race"}, "PULL": {"Lives recharged"},
            "ALIAS": {"Win & Collect start"}, "FILT": {"Boss Arena attempts refilled", "Daily gift about to reset", "Teammate sent lives", "Infinite lives ending"},
            "BUILT": {"Lapsed 14 days"},
            # the parking rule follows every row that can end up a Hold, including the three a mechanism or operator can move there
            "FOLLOW": {m["key"] for m in MEMBERS if m["call"] == "Hold"} | {"Lapsed 1 day", "Lapsed 7 days", "Lives recharged", "Lapsed 14 days"}}[rule]


def deciding(state, rule, key):
    if rule == "FILT":
        return [{"Boss Arena attempts refilled": I["boss_ask"], "Daily gift about to reset": I["gift_ask"], "Teammate sent lives": I["team_ask"], "Infinite lives ending": I["inf_ask"]}.get(key, I["gift_ask"])]
    return {"DONE": [I["arthur_inline"]], "CORR": [I["copy_check"]], "DEP": [SL["ask_decision"]], "QA": [SL["qa_reply"]], "PULL": [SL["lives_pull"]],
            "ALIAS": [TK["Win & Collect start"]], "BUILT": [SQL_IDS["cancel_mail"]], "FOLLOW": [I["freeze_comment"]]}[rule]


def base_route(record_id):
    return None
