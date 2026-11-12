"""Solver for julia_zm3d_playable_brief rev1 (design D2) · the hand-off list (tools/oracle_kit.py contract).

Truth = the hand-off list Julia should write as of the end of Tue Sep 30, 2025 (Pacific): one row per line of Brian's pack
list, with the state Frederick's hand-off notes give it (Delivered, Ready, Owed), what is
owed, who has it, the board set and the ticket. Inputs are the base universe plus the injection SQL (parsed with
tools/base_check.parse_sql; never executed).

Per-line facts that no designed mechanism changes come from the cohort table of Working_Files/plan/design_model.py; each
of them is also in the SQL (the pack list's row, the ticket, Brian's note on it), and load_state reads the notes and the
ticket states back from the SQL rather than trusting the table. One rule per mechanism_portfolio entry; each reads its
deciding record and falls back to its natural reading when `disable` switches it off (whole or per key set) or the record
is absent or does not say what the rule needs. Over-application operators act on the rule's declared control.
"""
import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
sys.path.insert(0, str(WF / "plan"))
import design_model as M  # noqa: E402

KEY_REGEX = "ZZ\\d|" + "|".join(__import__("re").escape(l["name"]) for l in M.LINES)
FIELDS = ["Line", "Category", "Board set", "State", "What's owed", "Who has it", "Ticket"]
CLASS_FIELD, GROUPS_FIELD = "State", "groups"
REVISIONS = ["rev1"]
_man = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())     # the portfolio is the draft's; the final manifest keeps it unchanged
RULES = {p["id"]: {k: p[k] for k in ("mechanism", "requirement", "nodes", "decides", "natural_reading", "source", "signature", "controls",
                                      "over_application")} | {"family": p["prior_family"]} for p in _man["mechanism_portfolio"]}
DEGRADES = {
    "export_over": "calls Rolling Pin Owed, as if every kitchen file were the text kind (Marcus says the ones from Claire are ok)",
    "art_over": "calls Desk Lamp Owed, as if every Friday file from Claire were being redone (her message is about the bathroom objects)",
    "revised_over": "calls Cute Axe Owed, as if every file of the morning of 25 Sep had changed (the pull request names three models on the list)",
    "audio_over": "calls Success sound Owed, as if no cue were ours to pass on (the sheet says it was made here)",
    "picks_over": "drops Grenade from the eight, as if Robert had replaced more than the dynamite",
    "zip_over": "calls Music Keyboard Owed, as if every instrument were in Friday's zip (its note says Monday, not zipped)",
    "ch_miss": "a channel member's deciding record is not found: the member takes its natural reading",
}
CHANNELS = {c["id"]: {"kind": "scale", "degrade": "ch_miss", "members": c["members"], "latent": "member", "family": c["family"], "rule": c["rule"],
                      "source": RULES[c["rule"]]["source"], "description": c["degrade"]} for c in _man["channels"]}
CHANNEL_RULE = {m: c["rule"] for c in CHANNELS.values() for m in c["members"]}
S = M.SEED
def _sid(seed): return M.slack_id(*S[seed]["id"].split("/"))
DECIDING = {"EXPORT": _sid("a1_post"), "ARTHOLD": _sid("a2_dm"), "PICKS": _sid("c3_reply"), "ZIP": S["c4_log"]["id"], "AUDIO": S["c2_sheet"]["id"],
            "REVISED": M.BASE["pr462"]}
SAYS = {"EXPORT": ("text", "the text kind"), "ARTHOLD": ("text", "banyo objelerinin uv"), "PICKS": ("text", "in place of the last one on my list"),
        "ZIP": ("body_text", "won't unpack")}
CLS_RULE = {"A1": "EXPORT", "A2": "ARTHOLD", "C1": "REVISED", "C2": "AUDIO", "C4": "ZIP"}
TOUCHED = {r: {l["name"] for l in M.LINES if CLS_RULE.get(l["cls"]) == r} for r in ("EXPORT", "ARTHOLD", "REVISED", "AUDIO", "ZIP")}
TOUCHED["PICKS"] = {"Bow", "Dynamite"}
PR462_MERGED = "2025-09-25T23:15:41Z"          # base: harmonygames-Games/match3d#462
OVER = {"export_over": ("Rolling Pin", "A1"), "art_over": ("Desk Lamp", "A2"), "revised_over": ("Cute Axe", "C1"), "audio_over": ("Success sound", "C2"),
        "zip_over": ("Music Keyboard", "C4")}


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id, notes, grids, issue = {}, collections.defaultdict(list), {}, {}
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "identifier", "contact_id", "document_id", "presentation_id", "event_id"):
            if r.get(k):
                by_id[str(r[k])] = r
        if x["table"] == "linear.linear_comments":
            notes[r["issue_id"]].append((r["created_at"], r["id"], r["body"]))
        if x["table"] == "linear.linear_issues":
            issue[r["id"]] = r
        if x["table"] == "gsheets.sheets_sheets":
            grids[r["spreadsheet_id"]] = json.loads(r["grid_json"])
            by_id[r["spreadsheet_id"]] = r
    # which cues Calvin's sheet marks as not ours to pass on, read from its grid
    held = {row[0] for row in grids.get(S["c2_sheet"]["id"], [])[1:] if len(row) > 2 and str(row[2]).strip().lower() == "no"}
    listed = [row[0] for row in grids.get(S["tracker"]["id"], [])[1:]]
    return {"by_id": by_id, "notes": {k: sorted(v) for k, v in notes.items()}, "issue": issue, "held": held, "listed": listed,
            "revision": revision or "rev1"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _off(rule, key, disable, degrade):
    return _hit(disable, rule, key) or (CHANNEL_RULE.get(key) == rule and _hit(degrade, "ch_miss", key))


def _live(state, rule):
    b = state["by_id"]
    if rule == "REVISED":      # base record: live when the three tickets' notes predate the merge
        ts = [state["notes"].get(M.BY_NAME[n]["ticket"], [("9999",)])[0][0] for n in sorted(TOUCHED["REVISED"])]
        return all(t < PR462_MERGED for t in ts)
    if rule == "AUDIO":
        return bool(state["held"])
    row = b.get(DECIDING[rule])
    if row is None:
        return False
    col, needle = SAYS[rule]
    return needle in str(row.get(col) or "")


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    live = {r: _live(state, r) for r in RULES}
    out = {}
    for l in M.LINES:
        k = l["name"]
        if keys_ is not None and k not in keys_:
            continue
        cls, tick = l["cls"], l["ticket"]
        st, owed, who = l["state"], l["owed"], l["who"]
        rule = CLS_RULE.get(cls)
        if rule and (_off(rule, k, disable, degrade) or not live[rule] or (rule == "AUDIO" and k not in state["held"])):
            st, owed, who = "Ready", None, None                 # the natural reading: Brian's note stands
        for op, (ctrl, as_cls) in OVER.items():                  # over-application on the rule's control
            if k == ctrl and _hit(degrade, op, k):
                st, (owed, own) = "Owed", M.UNIT_REASON[as_cls]
                who = own.split()[0]
        picks_off = _off("PICKS", k, disable, degrade) or not live["PICKS"]
        if cls == "ADD" and picks_off:
            # outside the list: the line is missed, so it has no row
            out[k] = {"Line": k, "Category": l["category"], "Board set": None, "State": None, "What's owed": None, "Who has it": None, "Ticket": None,
                      "groups": [], "evidence": {"Line": []}}
            continue
        board = l["board_set"]
        if k == "Bow" and picks_off: board = "Extra"
        if k == "Dynamite" and picks_off: board = "Default"
        if k == "Grenade" and _hit(degrade, "picks_over", k): board = "Extra"
        groups = ["list"]
        if st == "Owed" and tick: groups += ["todo", "comment"]
        if cls == "ADD": groups.append("new_ticket")
        if board == "Default": groups.append("default_eight")
        ev = [tick] if tick and tick in state["issue"] else ([DECIDING["PICKS"]] if cls == "ADD" and DECIDING["PICKS"] in state["by_id"] else [])
        out[k] = {"Line": k, "Category": l["category"] or None, "Board set": board, "State": st, "What's owed": owed, "Who has it": who,
                  "Ticket": tick, "groups": sorted(groups), "evidence": {"Line": ev}}
    return out


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    on = {k: v for k, v in rows.items() if v["State"] is not None}
    return {"classes": dict(sorted(collections.Counter(v["State"] for v in on.values()).items())),
            "groups": {g: groups[g] for g in sorted(groups)},
            "totals": {"lines": len(on), "todo": len(groups.get("todo", [])), "new_tickets": len(groups.get("new_ticket", [])),
                       "default_eight": len(groups.get("default_eight", []))}}


def evidence(rows, key, field):
    if field == "Line":
        return list(rows[key]["evidence"]["Line"])
    return []


def touched(state, rule):
    return set(TOUCHED[rule])


def deciding(state, rule, key):
    return [DECIDING[rule]]


def base_route(record_id):
    return None
