"""Solver for Owen's DD bug carry-over (tools/oracle_kit.py contract).

Truth = Linear, the index sheet and Owen's reply at the end of Sat Feb 14, 2026: one row per bug line (63 canvas lines and 7 later
posts in #god-bugs) with its outcome under Arthur's carry-over notes, and one row per UI child under ENG-2403, ENG-2404 and ENG-2405
with the state it ends in and the build its note names. Built from the base universe plus the injection SQL (parsed with
tools/base_check.parse_sql; never executed).

Per-line facts that no designed mechanism changes come from plan/cohort.json (written by plan/build_cohort.py from the design's
truth sketch). One rule per mechanism_portfolio entry; each reads its deciding record and falls back to its natural reading when
`disable` switches it off (whole or per key set), when the channel degrade `ch_miss` hits the key, or when the record is absent.
Over-application operators act on the declared controls. Base values were read through tools/hg.py and are fixed here.
"""
import collections
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
COHORT = json.loads((HERE.parent / "plan" / "cohort.json").read_text())
SEED = json.loads((HERE.parent / "plan" / "seed_text.json").read_text())
SEED6 = json.loads((HERE.parent / "plan" / "seed_text_rev6.json").read_text())   # rev6 second carriers
SEED7 = json.loads((HERE.parent / "plan" / "seed_text_rev7.json").read_text())   # rev7 tooltip thread close
SEED9 = json.loads((HERE.parent / "plan" / "seed_text_rev9.json").read_text())   # rev9 Daily Gift line in Brian's DM
BUGS, KIDS = COHORT["bugs"], COHORT["children"]

KEY_REGEX = r"(?:Bug 1|[A-Za-z][A-Za-z0-9 .()&/-]*)"
FIELDS = ["Bug", "Outcome", "Ticket", "Why"]
CLASS_FIELD, GROUPS_FIELD = "Outcome", "groups"
BUILD = "0.3.310"


def _slack(name):
    ch, ts = SEED[name]["id"].split("/")
    return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]


R_DOC = SEED["rule_doc"]["id"]
R_REPLY = _slack("brian_reply")
R_BACK = _slack("vincent_note")
R_BACK_REV2 = hashlib.sha256(b"D05USBTQY1F|1764760812.418229").hexdigest()[:32]   # the same note before rev3 moved it; rev2 also had no flicker reply
R_DM = _slack("brian_dm")
R_BAR = _slack("bar_reply")
R_FLICK = _slack("flick_reply")
R_TRAIN, R_TEAM = _slack("train_reply"), _slack("team_reply")
R_LIVES1, R_LIVES2 = _slack("lives_reply1"), _slack("lives_reply2")
R_INLINE_TD, R_INLINE_AXE = SEED["inline_td"]["id"], SEED["inline_axe"]["id"]
R_SEASON, R_GIFT = SEED["season_note"]["id"], SEED["gift_note"]["id"]
R_ALIAS = SEED["alias_note"]["id"]
_s6 = lambda n: hashlib.sha256(SEED6[n]["id"].replace("/", "|").encode()).hexdigest()[:32]
R_BACK2, R_ALIAS2 = _s6("brian_tavern"), _s6("brian_apple")   # rev6: Brian repeats both in his DM with Owen
R_POPUPS = _s6("brian_popups")   # rev6: Brian names both review holds in the same DM
R_GIFT2 = hashlib.sha256(SEED9["brian_gift"]["id"].replace("/", "|").encode()).hexdigest()[:32]   # rev9: Brian's Daily Gift note, now in his DM
R_TIP = hashlib.sha256(SEED7["tooltip_reply"]["id"].replace("/", "|").encode()).hexdigest()[:32]   # rev7: Vincent says the second fix closed the gap
R_RULE = SEED["rule_comment"]["id"]
R_AMEND = SEED["amend"]["id"]
MAIL_THREAD = SEED["mail"]["id"]                       # Owen's copy; the message row is found by thread in load_state

TAVERN, SHOPS = "Tavern buttons lost its frame", "shops from rivertile and memory tile has weird shop"
LIVES1, LIVES2 = "I found the issue lives are not decreased after", "Lives are only decreased after losing twice in a"
CHARCHANGE = "When I change the character it just adds 1"
TRAIN, TEAM = "train level backgrounds are broken", "When I created a team and quitted it the"
APPLE, MANUAL = "In general I cannot sync and sign in with", "On android manual sign-in has an issue after the"
WINDOW, MEGA, TREASURE = "tile dozer window background", "mega tile missing a face", "treasure button opens axe arena"
FLICKER, MUSIC, ACID, BAR = "flickering", "music plays only sometimes", "acid animation delay", "android bottom bar invisible"
TOOLTIP = "navigation bar tooltips"
PURPLE, FRAMES = "Purple bg visual issues", "character frames in char selection looks like it doesn"
TD, AXE, WINGS, SEASON, GIFT = "ENG-2434", "ENG-2426", "ENG-2424", "ENG-2428", "ENG-2437"
GONE_LINES = (LIVES1, LIVES2, CHARCHANGE)
ALL_KIDS = [m["key"] for m in KIDS]
ELSE_POSTS = (FLICKER, MUSIC, ACID)

RULES = {
    "INLINE": {"mechanism": "A24", "requirement": "R5", "nodes": ["T_INLINE_TD", "T_INLINE_AXE"], "decides": ["Outcome"], "family": "done_gap", "source": "github-inline",
               "natural_reading": "a merged PR with Brian's tick means the child is Done", "signature": "the child stays where it is because a popup never got swapped",
               "controls": ["ENG-2417", "ENG-2432"], "over_application": "inline_over"},
    "REPLY": {"mechanism": "A11", "requirement": "R2", "nodes": ["T_REPLY"], "decides": ["Outcome"], "family": "superseding", "source": "unrelated-thread-reply",
              "natural_reading": "a ticked line is fixed", "signature": "the shop icons line is still broken", "controls": [PURPLE], "over_application": "reply_over"},
    "BACK": {"mechanism": "A11", "requirement": "R2", "nodes": ["T_BACK"], "decides": ["Outcome"], "family": "superseding", "source": "one-to-one-dm",
             "natural_reading": "a ticked line is fixed", "signature": "the Tavern buttons line is still broken", "controls": [FRAMES], "over_application": "back_over"},
    "FOLLOW": {"mechanism": "A15", "requirement": "R6", "nodes": ["T_FOLLOW"], "decides": ["Note build"], "family": "authority", "source": "trello-comment",
               "natural_reading": "any line on a child is enough", "signature": "each child note names the public build",
               "controls": ["ENG-2417"], "over_application": None},
    "GONE": {"mechanism": "A15", "requirement": "R9", "nodes": ["T_GONE", "T_WINGS"], "decides": ["Outcome"], "family": "exact_predicate", "source": "economy-change",
             "natural_reading": "an unticked lives line is still broken and a merged child is Done", "signature": "the lives lines are Gone and ENG-2424 stays open",
             "controls": [TEAM], "over_application": "gone_over"},
    "LINE": {"mechanism": "A24", "requirement": "R2", "nodes": ["T_LINE"], "decides": ["Outcome"], "family": "done_gap", "source": "open-pr",
             "natural_reading": "Marcus fixed the window and did a PR, so it is fixed", "signature": "the window bug is still broken because #1913 is open",
             "controls": [TREASURE], "over_application": "line_over"},
    "ELSE": {"mechanism": "A25", "requirement": "R2", "nodes": ["T_ELSE_FLICKER", "T_ELSE_MUSIC", "T_ELSE_ACID"], "decides": ["Outcome"], "family": "completion_elsewhere", "source": "brian-dm-and-builds",
             "natural_reading": "a thread with no closing line is still broken", "signature": "flicker, music and acid are fixed from records outside their threads",
             "controls": [MEGA], "over_application": "else_over"},
    "ALIAS": {"mechanism": "A7", "requirement": "R3", "nodes": ["T_ALIAS_APPLE", "T_ALIAS_SPLASH"], "decides": ["Outcome", "Ticket"], "family": "scope_alias", "source": "gmail-and-ticket-note",
              "natural_reading": "no ticket has the canvas wording, so a new one is filed", "signature": "the Apple and manual sign-in lines reuse ENG-2073 and ENG-2363",
              "controls": [TEAM], "over_application": "alias_over"},
}
DEGRADES = {
    "ch_miss": "a channel member's deciding record is not found: the member takes its rule's natural reading",
    "inline_over": "holds a child whose PR has no inline comment",
    "reply_over": "reopens another ticked line from an unrelated reply",
    "back_over": "reopens another ticked line from the DM about the Tavern",
    "gone_over": "cancels a line that is not about lives",
    "line_over": "holds a post whose fix did land",
    "else_over": "closes a post nobody fixed",
    "alias_over": "reuses a ticket for a line with none",
}
CHANNELS = {
    "CH-INLINE": {"kind": "scale", "degrade": "ch_miss", "members": [TD, AXE], "latent": "member", "family": "done_gap", "rule": "INLINE", "source": "github-inline",
                  "description": "Arthur's inline review comment is not read: the child goes Done"},
    "CH-REPLY": {"kind": "scale", "degrade": "ch_miss", "members": [SHOPS], "latent": "member", "family": "superseding", "rule": "REPLY", "source": "unrelated-thread-reply",
                 "description": "Brian's reply under the gems post is not found: the shop icons line stays Fixed"},
    "CH-BACK": {"kind": "scale", "degrade": "ch_miss", "members": [TAVERN], "latent": "member", "family": "superseding", "rule": "BACK", "source": "one-to-one-dm",
                "description": "Marcus's note in the DM is not found: the Tavern line stays Fixed"},
    "CH-FOLLOW": {"kind": "scale", "degrade": "ch_miss", "members": ALL_KIDS, "latent": "run", "family": "authority", "rule": "FOLLOW", "source": "trello-comment",
                  "description": "Brian's closing rule on the card is not found: no child note names the build"},
    "CH-GONE": {"kind": "scale", "degrade": "ch_miss", "members": list(GONE_LINES) + [WINGS], "latent": "member", "family": "exact_predicate", "rule": "GONE", "source": "economy-change",
                "description": "the removal is not joined to the line or the child: lives lines stay broken and ENG-2424 goes Done"},
    "CH-LINE": {"kind": "scale", "degrade": "ch_miss", "members": [WINDOW], "latent": "member", "family": "done_gap", "rule": "LINE", "source": "open-pr",
                "description": "the PR state is not read: the window bug counts as fixed"},
    "CH-ELSE": {"kind": "scale", "degrade": "ch_miss", "members": list(ELSE_POSTS), "latent": "member", "family": "completion_elsewhere", "rule": "ELSE", "source": "brian-dm-and-builds",
                "description": "the fix outside the thread is not found: the post stays broken"},
    "CH-ALIAS": {"kind": "scale", "degrade": "ch_miss", "members": [APPLE, MANUAL], "latent": "member", "family": "scope_alias", "rule": "ALIAS", "source": "gmail-and-ticket-note",
                 "description": "Vincent's tie is not found: a new ticket is filed for the line"},
}
MEMBER_RULES = collections.defaultdict(set)
for _c in CHANNELS.values():
    for _m in _c["members"]:
        MEMBER_RULES[_m].add(_c["rule"])


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id, mail = {}, None
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "identifier", "document_id", "spreadsheet_id", "presentation_id", "event_id"):
            if r.get(k):
                by_id[str(r[k])] = r
        if r.get("thread_id") == MAIL_THREAD:
            mail = str(r["id"])
    return {"by_id": by_id, "mail": mail, "revision": revision or "rev9"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _off(rule, key, disable, degrade):
    return _hit(disable, rule, key) or (rule in MEMBER_RULES.get(key, ()) and _hit(degrade, "ch_miss", key))


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b          # noqa: E731
    mail = state.get("mail")

    def on(rule, k, record=None):
        return not _off(rule, k, disable, degrade) and (record is None or have(record))

    out = {}
    for m in BUGS:
        k = m["key"]
        if keys_ is not None and k not in keys_:
            continue
        outcome = "Fixed" if (m["kind"] == "later_bug" or m["ticked"]) else "Broken"
        ticket, why, ev = "new", "the tick stands" if m["ticked"] else "nobody closed it", [m["id"]]
        if m["kind"] == "later_bug":
            why = "closed in its thread"
        if k == SHOPS and on("REPLY", k, R_REPLY):
            outcome, why, ev = "Broken", "Brian said the round icons came back on the current build", [R_REPLY]
        if k == TAVERN and (on("BACK", k, R_BACK) or on("BACK", k, R_BACK_REV2) or on("BACK", k, R_BACK2)):
            outcome, why, ev = "Broken", "Marcus said the frame went again and Brian's fix didn't hold", [r for r in (R_BACK, R_BACK2) if have(r)] or [R_BACK]
        if k == TRAIN:
            outcome, why, ev = ("Broken", "Vincent left it open after the commit", [R_TRAIN]) if have(R_TRAIN) else ("Fixed", "commit 4189eca5", [m["id"]])
        if k == TEAM:
            outcome, why, ev = ("Broken", "Vincent says the bar still goes after the commit", [R_TEAM]) if have(R_TEAM) else ("Fixed", "commit 100612a7", [m["id"]])
        if k in (LIVES1, LIVES2):
            reply = R_LIVES1 if k == LIVES1 else R_LIVES2
            if not have(reply):
                outcome, why, ev = "Fixed", "commit 3646982c", [m["id"]]
            elif on("GONE", k):
                outcome, why, ev = "Gone", "the build players have has no lives", [reply]
            else:
                outcome, why, ev = "Broken", "Vincent says it is the same after the change", [reply]
        if k == CHARCHANGE and on("GONE", k):
            outcome, why = "Gone", "the build players have has no lives"
        if k == APPLE and ((mail and on("ALIAS", k, mail)) or on("ALIAS", k, R_ALIAS2)):
            outcome, ticket, why, ev = "Covered", "ENG-2073", "Vincent tied it to ENG-2073", [r for r in (mail, R_ALIAS2) if r and have(r)] or [mail]
        if k == MANUAL and on("ALIAS", k, R_ALIAS):
            outcome, ticket, why, ev = "Covered", "ENG-2363", "Vincent tied it to ENG-2363", [R_ALIAS]
        if k == TOOLTIP and have(R_TIP):
            why, ev = "Vincent says Brian's second fix closed the 1 pixel gap", [R_TIP]
        if k == MEGA:
            outcome, why = "Broken", "nobody fixed it"
        if k == WINDOW:
            outcome, why = ("Broken", "#1913 is still open") if on("LINE", k) else ("Fixed", "Marcus said he fixed it")
        if k == FLICKER:
            outcome, why, ev = ("Fixed", "Robert says both flickers are gone", [R_FLICK]) if on("ELSE", k, R_FLICK) else ("Fixed", "fix commit a6fb440f0c is on the economy line", [m["id"]]) if on("ELSE", k, R_BACK_REV2) else ("Broken", "the thread ends at testing a fix", [m["id"]])
        if k in (MUSIC, ACID):
            outcome, why, ev = ("Fixed", "Brian's DM to Owen", [R_DM]) if on("ELSE", k, R_DM) else ("Broken", "the thread has no closing line", [m["id"]])
        if k == BAR:
            outcome, why, ev = ("Fixed", "Brian closed it after the camera change", [R_BAR]) if have(R_BAR) else ("Broken", "the thread has no closing line", [m["id"]])
        # over-application operators on the controls
        if k == PURPLE and _hit(degrade, "reply_over", k):
            outcome, why = "Broken", "reopened from an unrelated reply"
        if k == FRAMES and _hit(degrade, "back_over", k):
            outcome, why = "Broken", "reopened from the Tavern DM"
        if k == TEAM and _hit(degrade, "gone_over", k):
            outcome, why = "Gone", "treated as removed"
        if k == TEAM and _hit(degrade, "alias_over", k):
            outcome, ticket, why = "Covered", "ENG-2073", "tied to a ticket with no record"
        if k == TREASURE and _hit(degrade, "line_over", k):
            outcome, why = "Broken", "held although the fix landed"
        if k == MEGA and _hit(degrade, "else_over", k):
            outcome, why = "Fixed", "closed without a record"
        evd = {"Outcome": ev}
        if ticket != "new":
            evd["Ticket"] = ev
        out[k] = {"Bug": m["line"], "Outcome": outcome, "Ticket": ticket, "Why": why, "groups": [outcome.lower()], "evidence": evd}
    for m in KIDS:
        k = m["key"]
        if keys_ is not None and k not in keys_:
            continue
        outcome, why, ev = "Done", "checked and merged", []
        if m["already_done"]:
            why = "already Done"
        if k == TD and (on("INLINE", k, R_INLINE_TD) or on("INLINE", k, R_POPUPS)):
            outcome, why, ev = "Held", "how-to-play popup not swapped", [r for r in (R_INLINE_TD, R_POPUPS) if have(r)]
        if k == AXE and (on("INLINE", k, R_INLINE_AXE) or on("INLINE", k, R_POPUPS)):
            outcome, why, ev = "Held", "info popup keeps the old frame", [r for r in (R_INLINE_AXE, R_POPUPS) if have(r)]
        if k == WINGS and on("GONE", k):
            outcome, why = "Held", "Win & Collect disabled Dec 16"
        if k == SEASON and have(R_SEASON):
            outcome, why, ev = "Held", "reward track still on the old frames", [R_SEASON]
        if k == GIFT and (have(R_GIFT) or have(R_GIFT2)):
            outcome, why, ev = "Held", "panel never got its last pass", [r for r in (R_GIFT, R_GIFT2) if have(r)]
        if k in ("ENG-2417", "ENG-2432") and _hit(degrade, "inline_over", k):
            outcome, why = "Held", "held with no inline comment"
        note = BUILD if on("FOLLOW", k, R_RULE) else None
        out[k] = {"Bug": k, "Outcome": outcome, "Ticket": k, "Why": why, "Note build": note, "groups": ["child", outcome.lower()], "evidence": {"Outcome": ev}}
    return out


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    bugs = {k: v for k, v in rows.items() if "child" not in v["groups"]}
    kids = {k: v for k, v in rows.items() if "child" in v["groups"]}
    c = collections.Counter(v["Outcome"] for v in bugs.values())
    return {"classes": dict(sorted(c.items())), "groups": {g: groups[g] for g in sorted(groups)},
            "reply": {"still_broken": c["Broken"] + c["Covered"], "new_tickets": c["Fixed"] + c["Gone"] + c["Broken"],
                      "children_done": sum(v["Outcome"] == "Done" for v in kids.values()), "children_total": len(kids)}}


def evidence(rows, key, field):
    return list((rows[key].get("evidence") or {}).get(field, []))


def touched(state, rule):
    return {"INLINE": {TD, AXE}, "REPLY": {SHOPS}, "BACK": {TAVERN}, "FOLLOW": set(ALL_KIDS), "GONE": set(GONE_LINES) | {WINGS}, "LINE": {WINDOW},
            "ELSE": set(ELSE_POSTS), "ALIAS": {APPLE, MANUAL}}[rule]


def deciding(state, rule, key):
    have = lambda i: i in state.get("by_id", {})   # noqa: E731
    return {"INLINE": {TD: [r for r in (R_INLINE_TD, R_POPUPS) if have(r)], AXE: [r for r in (R_INLINE_AXE, R_POPUPS) if have(r)]}.get(key, []),
            "REPLY": [R_REPLY], "BACK": [r for r in (R_BACK, R_BACK2) if have(r)] or [R_BACK], "FOLLOW": [R_RULE],
            "GONE": {LIVES1: [R_LIVES1], LIVES2: [R_LIVES2]}.get(key, []),
            "LINE": [], "ELSE": {MUSIC: [R_DM], ACID: [R_DM], FLICKER: [R_FLICK]}.get(key, []),
            "ALIAS": {APPLE: [r for r in (state.get("mail"), R_ALIAS2) if r and have(r)], MANUAL: [R_ALIAS]}.get(key, [])}[rule]


def base_route(record_id):
    if isinstance(record_id, str) and record_id.startswith("ENG-"):
        return {"service": "linear", "file": "data.json", "pointer": "/issues", "field": "id"}
    return None
