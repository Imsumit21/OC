"""Solver for Robert's LLC take-over plan (tools/oracle_kit.py contract), rev4 (rev1-rev3 truth reproduced; rev4 keeps the truth:
STACKS added (CF's stacks from Arthur's later Jenkins email over his ENG-2445 note), DATE reads the layer.ai reply, EXC purged).

Truth = the plan sheet Robert should write at the end of Fri Feb 13, 2026 (Pacific): one row per item the LLC might take
from Harmony Games (the 37 issues of Leonard's Linear project plus the Combo Fighter VO campaign, which is in no list),
with the decision (LLC / Founder / HG), the monthly cost for March-May, who pays, the next step, its owner and its date.
Built from the base universe plus the injection SQL (parsed with tools/base_check.parse_sql; never executed).

Per-item facts that no designed mechanism changes come from the cohort table (plan/cohort.json, written by
plan/build_scenario.py; each row names its deciding records). One rule per mechanism_portfolio entry; each reads its
deciding record and falls back to its natural reading when `disable` switches it off (whole or per key set), when its
channel degrade `ch_miss` hits the key, or when the record is absent. Over-application operators act on the declared
controls. Base values the rules use (REVENUE_DAILY January sums, Arthur's ZM account note) were re-read through
tools/hg.py and are fixed here.
"""
import collections
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
COHORT = json.loads((PLAN / "cohort.json").read_text())
SQLIDS = json.loads((PLAN / "sql_ids.json").read_text())
IDS = json.loads((PLAN / "ids.json").read_text())["IDS"]

KEY_REGEX = r"(?:Item 1|[A-Za-z][A-Za-z0-9 .()&/-]*)"
FIELDS = ["Item", "Game", "Decision", "Monthly cost", "Paid by", "Next step", "Owner", "By"]
CLASS_FIELD, GROUPS_FIELD = "Decision", "groups"

DD, ZM, CF = "Domino Delights", "Zombie Match", "Combo Fighter"
DD_PROD, ZM_ACC, DD_SUP = "Domino Delights production account (AWS)", "Zombie Match account (AWS)", "Domino Delights player support"
CF_STACKS, CAMPAIGN, CALM = "Combo Fighter backend and auth stacks (AWS)", "Combo Fighter VO campaign", "Calm Play LLC"
CARRIED = ("Metabase", "dbt", "GitHub")
JAN_INCOME = {DD: 183.11, ZM: 0.0}            # ANALYTICS.MONETIZATION.REVENUE_DAILY, SUM(total_revenue_usd) 2026-01 (hg.py, rows 186)
ZM_HOSTING = None                              # Arthur's ENG-2443 note: untrimmed and billing every month (amount not stated; any bill > $0.00 income)
DD_HOSTING_STALE = 1000                        # #winddown C0ADGSZKR3R/1770680984.725779 "~$1k a month"

# seeded deciding records (row ids in the SQL)
R_ARTHUR_DM = SQLIDS["slack"]["arthur_dm"]["id"]
R_VO_STATUS = SQLIDS["slack"]["vo_status"]["id"]
R_GROUND_RULES = IDS["ground_rules"]
R_TRELLO = IDS["trello_card"]
R_ARTHUR_MAIL = SQLIDS["gmail"]["arthur_mail"]["robert@harmonygames.co"]["message"]
R_ASC = SQLIDS["gmail"]["asc_notice"]["robert@harmonygames.co"]["message"]
R_SPLIT = SQLIDS["gmail"]["split_mail"]["robert@harmonygames.co"]["message"]
R_JENKINS = SQLIDS["gmail"]["jenkins_mail"]["robert@harmonygames.co"]["message"]   # rev4: Arthur's 'jenkins' email ($62 now)
R_LAYER_REPLY = SQLIDS["slack"]["layer_reply"]["id"]                                  # rev4: Leonard's reply under the layer.ai post
R_CF_NOTE = SQLIDS["linear"][CF_STACKS]["comment"]                                   # Arthur's ENG-2445 note
R_LAYER_NOTE = SQLIDS["linear"]["layer.ai"]["comment"]                               # Leonard's ENG-2454 note

RULES = {
    "CORR": {"mechanism": "A11", "requirement": "R3", "nodes": ["T1", "C1", "T8", "T15"],
             "decides": ["Decision", "Monthly cost", "Paid by"], "family": "superseding", "source": "dm-thread-reply",
             "natural_reading": "DD hosting is the #winddown / issue / draft figure (~$1k or $300), so Domino Delights fails "
                                "the take test and stays with HG",
             "signature": "Domino prod account $140 a month now",
             "controls": [CF_STACKS], "over_application": "corr_over"},
    "AUTH": {"mechanism": "A13", "requirement": "R10", "nodes": ["T2", "C2", "T11", "T12"],
             "decides": ["Decision", "Monthly cost", "Paid by"], "family": "exact_predicate", "source": "warehouse",
             "natural_reading": "DD's income is what Slack says about it (way less than $1K), so DD stays with HG, and Zombie "
                                "Match comes over with Combo Fighter as the older notes say",
             "signature": "REVENUE_DAILY January domino_delights zombie_match_3d",
             "controls": [CF], "over_application": "auth_over"},
    "FILT": {"mechanism": "A17", "requirement": "R6", "nodes": ["T3", "C5", "T9", "T16"], "decides": ["groups", "Decision"],
             "family": "exact_predicate", "source": "channel-history",
             "natural_reading": "the project and the #winddown lists are the population of monthly charges: no campaign row",
             "signature": "VO campaign $100/day about $3k a month",
             "controls": ["Unity Ads balance", "Playable vendor"], "over_application": "filt_over"},
    "COMPLETE": {"mechanism": "A25", "requirement": "R11", "nodes": ["T4", "C3", "T14"],
                 "decides": ["Decision", "Monthly cost", "Paid by"], "family": "completion_elsewhere", "source": "mail-by-name",
                 "natural_reading": "Metabase and dbt are LLC cash at about $300 together; GitHub stays with HG until the data "
                                    "is sold",
                 "signature": "Kub card $248 carried through May",
                 "controls": ["Build machines"], "over_application": "complete_over"},
    "DONE": {"mechanism": "A24", "requirement": "R2", "nodes": ["T5", "C4"], "decides": ["Next step", "Owner", "By"],
             "family": "done_gap", "source": "store-notice",
             "natural_reading": "Arthur's done and the merged PR mean the store build has it: no step left",
             "signature": "submission issue support option email draft does nothing",
             "controls": ["Helpshift"], "over_application": "done_over"},
    "DATE": {"mechanism": "A4", "requirement": "R2", "nodes": ["T7", "C7", "T17"], "decides": ["By", "Next step"],
             "family": "boundary_date", "source": "channel-history",
             "natural_reading": "every step moves by March 1",
             "signature": "layer access until March 3rd; github transfer after the data is sold",
             "controls": ["AppsFlyer"], "over_application": "date_over"},
    "STACKS": {"mechanism": "A11", "requirement": "R3", "nodes": ["T19", "C8"], "decides": ["Monthly cost"],
               "family": "superseding", "source": "mail-second-paragraph",
               "natural_reading": "CF's backend and auth stacks cost the figure on Arthur's ENG-2445 note (~$95 in rev4)",
               "signature": "extra CF backend copy shut down, $62 a month now",
               "controls": [DD_PROD], "over_application": "stacks_over"},
}
DEGRADES = {
    "corr_over": "rewrites the CF backend stacks' cost from an unrelated DM line ($140)",
    "auth_over": "applies the take test to Combo Fighter and drops it for $7.36 of January income",
    "filt_over": "adds the one-off Unity Ads balance and the playable vendor as monthly LLC lines",
    "complete_over": "treats the build machines as Arthur's own because they sit at his house",
    "done_over": "adds a release check to the Helpshift item, which is only cancelled",
    "stacks_over": "also costs DD's production account at the Jenkins email's $62 as if the trim covered it",
    "date_over": "dates AppsFlyer to Feb 28 as if it carried Helpshift's deadline",
    "ch_miss": "a channel member's deciding record is not found: the member takes its rule's natural reading",
}
CHANNELS = {
    "CH-CORR": {"kind": "scale", "degrade": "ch_miss", "members": [DD, DD_PROD, DD_SUP], "latent": "member", "family": "superseding",
                "rule": "CORR", "source": "dm-thread-reply",
                "description": "Arthur's DM reply ($140, under an unrelated root) is not found: DD hosting stays ~$1k / $300"},
    "CH-AUTH": {"kind": "scale", "degrade": "ch_miss", "members": [DD, ZM, ZM_ACC], "latent": "member", "family": "exact_predicate",
                "rule": "AUTH", "source": "warehouse",
                "description": "January income is not read from REVENUE_DAILY: DD is judged from Slack, ZM comes over"},
    "CH-FILT": {"kind": "scale", "degrade": "ch_miss", "members": [CAMPAIGN], "latent": "member", "family": "exact_predicate",
                "rule": "FILT", "source": "channel-history",
                "description": "the VO campaign (in no list) is not found: no campaign row and no new issue"},
    "CH-COMPLETE": {"kind": "scale", "degrade": "ch_miss", "members": list(CARRIED), "latent": "member",
                    "family": "completion_elsewhere", "rule": "COMPLETE", "source": "mail-by-name",
                    "description": "Arthur's billing email is not found: Metabase and dbt become LLC cash"},
    "CH-DONE": {"kind": "scale", "degrade": "ch_miss", "members": [DD_SUP], "latent": "member", "family": "done_gap",
                "rule": "DONE", "source": "store-notice",
                "description": "the App Store notice is not read: the support move looks finished"},
    "CH-DATE": {"kind": "scale", "degrade": "ch_miss", "members": ["layer.ai", "GitHub"], "latent": "member",
                "family": "boundary_date", "rule": "DATE", "source": "channel-history",
                "description": "the item's own deadline is not applied: the layer export and the GitHub transfer get Mar 1"},
    "CH-STACKS": {"kind": "scale", "degrade": "ch_miss", "members": [CF_STACKS], "latent": "member", "family": "superseding",
                  "rule": "STACKS", "source": "mail-second-paragraph",
                  "description": "Arthur's Jenkins email is not read: CF's stacks stay at the issue note's ~$95"},
}
MEMBER_RULES = collections.defaultdict(set)
for _c in CHANNELS.values():
    for _m in _c["members"]:
        MEMBER_RULES[_m].add(_c["rule"])


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id = {}
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "identifier", "document_id", "spreadsheet_id", "presentation_id", "event_id", "sha"):
            if r.get(k):
                by_id[str(r[k])] = r
    return {"by_id": by_id, "revision": revision or "rev4"}


def _dollars(text, pattern=r"\$(\d+)"):
    m = re.search(pattern, str(text or ""))
    return int(m.group(1)) if m else None


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _off(rule, key, disable, degrade):
    return _hit(disable, rule, key) or (rule in MEMBER_RULES.get(key, ()) and _hit(degrade, "ch_miss", key))


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b          # noqa: E731
    gr = have(R_GROUND_RULES)

    def corr_on(k):
        return not _off("CORR", k, disable, degrade) and have(R_ARTHUR_DM)

    def auth_on(k):
        return not _off("AUTH", k, disable, degrade) and gr

    def dd_hosting(k):
        return 140 if corr_on(k) else DD_HOSTING_STALE

    def dd_taken(k):
        # the take test (ground rules): January income from REVENUE_DAILY covers the game's own hosting
        if not auth_on(k):
            return False                        # natural reading: Slack says DD makes "way less than $1K"
        return JAN_INCOME[DD] >= dd_hosting(k)

    def jenkins_figure():
        # the Jenkins email's own figure, independent of any rule's state (keeps over-application key-local)
        if have(R_JENKINS):
            return _dollars(b[R_JENKINS].get("body_text"), r"bills \$(\d+) a month now")
        return None

    def cf_stacks_cost(k):
        # rev4: Arthur's ENG-2445 note gives the figure before his trim; his later Jenkins email (second paragraph) gives what
        # it bills now. rev2/rev3 SQL: the note itself says $62 and there is no email, so the result is unchanged.
        note = _dollars(b[R_CF_NOTE].get("body")) if have(R_CF_NOTE) else None
        if have(R_JENKINS) and not _off("STACKS", k, disable, degrade):
            now = _dollars(b[R_JENKINS].get("body_text"), r"bills \$(\d+) a month now")
            if now is not None:
                return now
        return note if note is not None else 62

    def layer_caveat():
        # rev2/rev3: the ENG-2454 note itself carries the art caveat; rev4 moves it into the reply under the access-date post
        return have(R_LAYER_NOTE) and "art" in str(b[R_LAYER_NOTE].get("body") or "")

    def zm_taken(k):
        if not auth_on(k):
            return True                         # natural reading: DD and ZM come over with CF (the older notes doc)
        return JAN_INCOME[ZM] > 0               # its account bills every month (ENG-2443), so $0.00 can't cover it

    out = {}
    for m in COHORT:
        k = m["key"]
        if keys_ is not None and k not in keys_:
            continue
        row = {"Item": k, "Game": m["game"], "Decision": m["decision"], "Monthly cost": m["cost"], "Paid by": m["paid_by"],
               "Next step": m["step"], "Owner": m["owner"], "By": m["by"]}
        # ---- CORR + AUTH: the take test on Domino Delights and everything that follows it
        if k == DD and not dd_taken(k):
            row.update({"Decision": "HG", "Paid by": "HG", "Next step": "stays with Sunset's sale", "Owner": "-", "By": "-"})
        if k == DD_PROD:
            if dd_taken(k):
                row.update({"Monthly cost": dd_hosting(k)})
            else:
                row.update({"Decision": "HG", "Monthly cost": 0, "Paid by": "HG", "Next step": "goes with DD", "Owner": "-", "By": "-"})
        if k == DD_SUP and not dd_taken(k):
            row.update({"Decision": "HG", "Paid by": "HG", "Next step": "stays with DD at HG", "Owner": "-", "By": "-"})
        if k == ZM and zm_taken(k):
            row.update({"Decision": "LLC", "Paid by": "-", "Next step": "game and its listings come through Sunset's sale",
                        "By": "when the sale closes"})
        if k == ZM_ACC and zm_taken(k):
            row.update({"Decision": "LLC", "Monthly cost": ZM_HOSTING, "Paid by": "LLC", "Next step": "billing moves to the LLC",
                        "Owner": "Arthur", "By": "Mar 1"})
        # ---- STACKS: CF's stacks at what they bill now, going by Arthur (the owner)
        if k == CF_STACKS:
            row.update({"Monthly cost": cf_stacks_cost(k)})
        # ---- FILT: the campaign outside every list
        if k == CAMPAIGN and (_off("FILT", k, disable, degrade) or not have(R_VO_STATUS)):
            row = {f: None for f in FIELDS}
        # ---- COMPLETE: Arthur already carries Metabase, dbt and GitHub
        if k in CARRIED and (_off("COMPLETE", k, disable, degrade) or not have(R_ARTHUR_MAIL)):
            if k == "GitHub":
                row.update({"Decision": "HG", "Monthly cost": 0, "Paid by": "HG",
                            "Next step": "stays with HG until the data is sold, then the repos transfer", "Owner": "-"})
            else:
                row.update({"Decision": "LLC", "Monthly cost": 150, "Paid by": "LLC", "Next step": "keep for Combo Fighter's data",
                            "Owner": "Arthur", "By": "Mar 1"})
        # rev1's App Review item described a support screen; rev2's describes the email-draft option, so the owed step reads differently
        if k == DD_SUP and row["Decision"] == "LLC" and have(R_ASC) and "mail account" not in str(b[R_ASC].get("body_text") or ""):
            row.update({"Next step": "release the support-email build before Helpshift stops on Feb 28"})
        # ---- DONE: the support move looks finished without the store notice
        if k == DD_SUP and row["Decision"] == "LLC" and (_off("DONE", k, disable, degrade) or not have(R_ASC)):
            row.update({"Next step": "done (support email merged in #1917)", "Owner": "-", "By": "-"})
        # ---- DATE: an item's own deadline keeps it (Trello card), else everything moves by March 1
        if k == "layer.ai" and not layer_caveat() and (_off("DATE", k, disable, degrade) or not have(R_LAYER_REPLY)):
            # rev4: the issue note reads as closed; without the reply nothing says CF's art is there, so no step at all
            row.update({"Next step": "cancelled", "Owner": "-", "By": "-"})
        elif k in ("layer.ai", "GitHub") and row["Decision"] in ("HG", "Founder") and \
                (_off("DATE", k, disable, degrade) or not have(R_TRELLO)):
            if k == "layer.ai":
                row.update({"By": "Mar 1"})
            else:
                row.update({"Next step": "already on Arthur's Kub card; repos transfer by Mar 1" if row["Decision"] == "Founder"
                            else "repos transfer by Mar 1", "By": "Mar 1"})
        # ---- over-application operators on the controls
        if k == CF_STACKS and _hit(degrade, "corr_over", k):
            row.update({"Monthly cost": 140})
        if k == CF and _hit(degrade, "auth_over", k):
            row.update({"Decision": "HG", "Paid by": "HG", "Next step": "stays with Sunset's sale", "Owner": "-", "By": "-"})
        if k in ("Unity Ads balance", "Playable vendor") and _hit(degrade, "filt_over", k):
            row.update({"Decision": "LLC", "Monthly cost": 100 if k == "Unity Ads balance" else 3750, "Paid by": "LLC"})
        if k == "Build machines" and _hit(degrade, "complete_over", k):
            row.update({"Decision": "Founder", "Paid by": "Arthur", "Next step": "Arthur's own", "Owner": "Arthur"})
        if k == "Helpshift" and _hit(degrade, "done_over", k):
            row.update({"Next step": "check the support build ships before Feb 28", "Owner": "Arthur", "By": "Feb 28"})
        if k == DD_PROD and row["Decision"] == "LLC" and _hit(degrade, "stacks_over", k) and jenkins_figure() is not None:
            row.update({"Monthly cost": jenkins_figure()})
        if k == "AppsFlyer" and _hit(degrade, "date_over", k):
            row.update({"By": "Feb 28"})
        # ---- groups and evidence
        groups = []
        if row["Decision"]:
            groups.append(row["Decision"].lower())
            if k == CAMPAIGN:
                groups.append("new_issue")
        ev = {"Item": [m["linear"]] if m.get("linear") and have(m["linear"]) else []}
        if k in CARRIED and row["Decision"] == "Founder" and have(R_ARTHUR_MAIL):
            ev["Monthly cost"] = [R_ARTHUR_MAIL]
        if k == DD_PROD and row["Monthly cost"] == 140:
            ev["Monthly cost"] = [R_ARTHUR_DM]
        if k == CF_STACKS and row["Monthly cost"] == 62:
            ev["Monthly cost"] = [R_JENKINS] if have(R_JENKINS) else [R_CF_NOTE]
        row["groups"] = sorted(groups)
        row["evidence"] = ev
        out[k] = row
    return out


def totals(rows):
    cash = sum(r["Monthly cost"] or 0 for r in rows.values() if r["Decision"] == "LLC")
    carried = {}
    for r in rows.values():
        if r["Decision"] == "Founder":
            carried[r["Paid by"]] = carried.get(r["Paid by"], 0) + (r["Monthly cost"] or 0)
    total = cash + sum(carried.values())
    third = round(total / 3, 2)
    shares = {p: round(third - carried.get(p, 0), 2) for p in ("Leonard", "Robert", "Arthur")}
    return {"llc_cash_per_month": cash, "carried_per_month": dict(sorted(carried.items())), "total_per_month": total,
            "third": third, "cash_shares_per_month": shares, "window_months": 3,
            "llc_cash_window": cash * 3, "cash_shares_window": {p: round(v * 3, 2) for p, v in shares.items()}}


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    listed = [v for v in rows.values() if v["Decision"]]
    return {"classes": dict(sorted(collections.Counter(v["Decision"] for v in listed).items())),
            "groups": {g: groups[g] for g in sorted(groups)}, "totals": totals(rows)}


def evidence(rows, key, field):
    return list((rows[key].get("evidence") or {}).get(field, []))


def touched(state, rule):
    return {"CORR": {DD, DD_PROD, DD_SUP}, "AUTH": {DD, DD_PROD, DD_SUP, ZM, ZM_ACC}, "FILT": {CAMPAIGN},
            "COMPLETE": set(CARRIED), "DONE": {DD_SUP}, "DATE": {"layer.ai", "GitHub"}, "STACKS": {CF_STACKS}}[rule]


def deciding(state, rule, key):
    return {"CORR": [R_ARTHUR_DM], "AUTH": [R_GROUND_RULES], "FILT": [R_VO_STATUS], "COMPLETE": [R_ARTHUR_MAIL],
            "DONE": [R_ASC], "DATE": [R_TRELLO] + ([R_LAYER_REPLY] if R_LAYER_REPLY in state["by_id"] else []),
            "STACKS": [R_JENKINS] if R_JENKINS in state["by_id"] else []}[rule]


def base_route(record_id):
    return None
