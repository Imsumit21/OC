"""activity.json: per person (email key, Slack id where available) first/last activity per service,
monthly volumes, departure signals and clock status. Joins: exact email or Slack id only; GitHub logins
are attached only where entities.json joined them by exact_email; Trello (name-joined) is reported but
never used for status."""
import json, collections, datetime, re
from zoneinfo import ZoneInfo
from common import *

ACTIVE_MONTH = CLOCK.replace(day=1)
RECENT_MONTH = (ACTIVE_MONTH - datetime.timedelta(days=1)).replace(day=1)
ACTIVE_FROM, RECENT_FROM = ACTIVE_MONTH.strftime("%Y-%m-%d"), RECENT_MONTH.strftime("%Y-%m-%d")
ACTIVE_KEY = "active_" + ACTIVE_MONTH.strftime("%b_%Y").lower()
RECENT_KEY = "active_" + RECENT_MONTH.strftime("%b_%Y").lower() + "_quiet_in_" + ACTIVE_MONTH.strftime("%b").lower()
ACTIVE_YM, RECENT_YM = ACTIVE_MONTH.strftime("%Y-%m"), RECENT_MONTH.strftime("%Y-%m")
ACTIVE_COLUMN, RECENT_COLUMN = ACTIVE_YM.replace("-", "_"), RECENT_YM.replace("-", "_")


def main():
    S = jload_cache("kb_slack.json")
    GM = jload_cache("kb_gmail.json")
    GH = jload_cache("kb_github.json")
    LI = jload_cache("kb_linear.json")
    O = jload_cache("kb_other.json")
    E = jload_kb("entities.json")
    susers = {u["id"]: u for u in jload(SLACK + "/users.json")}
    chans = {c["id"]: c for c in jload(SLACK + "/channels.json")}
    roster = {}
    for e in E["entities"]:
        if e.get("persona"):
            for em in e.get("emails") or []:
                roster[em] = e["persona"]
    gh_by_email = collections.defaultdict(list)
    tr_by_email = collections.defaultdict(list)
    for e in E["entities"]:
        ems = e.get("emails") or []
        if not ems:
            continue
        for g in (e.get("identities") or {}).get("github", []):
            if g.get("join") in ("exact_email", "roster"):
                gh_by_email[ems[0]].append(g["login"])
        for t in (e.get("identities") or {}).get("trello", []):
            tr_by_email[ems[0]].append([t["id"], t.get("join")])
    people = collections.defaultdict(lambda: {"name": None, "slack_id": None, "persona": None, "services": {}})
    def P(email):
        return people[email.lower()]
    # Slack
    slack_email = {}
    for uid, u in susers.items():
        if u.get("email"):
            slack_email[uid] = u["email"].lower()
    joins_by_user = collections.defaultdict(list)
    for uid, cid, ts, sub in S["joins"]:
        joins_by_user[uid].append([cid, ts, sub])
    slack_only = {}
    for uid, p in S["person"].items():
        rec = {"id": uid, "first": ts_to_dt(p["first"]).isoformat() if p["first"] else None, "last": ts_to_dt(p["last"]).isoformat() if p["last"] else None,
               "messages": p["n"], "replies": p["replies"], "thread_roots": p["roots"], "by_type": p["by_type"], "monthly": p["monthly"],
               "channels_posted": len(p["chan"]), "member_of_channels": sum(1 for c in chans.values() if uid in (c.get("members") or []))}
        lv = [j for j in joins_by_user.get(uid, []) if j[2] in ("channel_leave", "group_leave")]
        lv.sort(key=lambda j: float(j[1]))
        rec["channel_leaves"] = {"count": len(lv), "last": [{"channel": chans.get(c, {}).get("name") or c, "channel_id": c, "ts": t, "date": ts_to_dt(float(t)).strftime("%Y-%m-%d")} for c, t, s in lv[-6:]]}
        nonmem = [cid for cid, d in S["nonmember_posts"].items() if uid in d]
        rec["posted_in_channels_no_longer_member"] = len(nonmem)
        tn = p["textn"] or 1
        rec["style"] = {"len": p["len_q"], "lower_start_share": round(p["lower_start"] / tn, 2), "all_lower_share": round(p["all_lower"] / tn, 2),
                        "ends_punct_share": round(p["ends_punct"] / tn, 2), "emoji_share": round(p["emoji"] / tn, 2), "question_share": round(p["question"] / tn, 2),
                        "multiline_share": round(p["multiline"] / tn, 2), "url_share": round(p["url"] / tn, 2)}
        rec["hours_utc"] = p["hours_utc"]
        rec["weekday_pt"] = p["weekday_pt"]
        em = slack_email.get(uid)
        if em:
            pp = P(em)
            pp["slack_id"] = uid
            pp["name"] = pp["name"] or susers[uid].get("real_name")
            pp["services"]["slack"] = rec
        else:
            rec["name"] = (susers.get(uid) or {}).get("real_name")
            slack_only[uid] = rec
    for uid, em in slack_email.items():
        if "slack" not in P(em)["services"]:
            P(em)["slack_id"] = uid
            P(em)["services"]["slack"] = {"id": uid, "messages": 0, "member_of_channels": sum(1 for c in chans.values() if uid in (c.get("members") or []))}
    # Gmail
    for mb, v in GM["mailboxes"].items():
        if "@" in mb:
            P(mb)["services"].setdefault("gmail", {})["mailbox"] = {"threads": v["threads"], "messages": v["messages"], "first": v["first"], "last": v["last"]}
    for em, mon in GM["sent_monthly"].items():
        if em.endswith("@harmonygames.co"):
            g = P(em)["services"].setdefault("gmail", {})
            g["sent_monthly"] = mon
            g["sent_first"] = GM["sent_first"].get(em)
            g["sent_last"] = GM["sent_last"].get(em)
            g["sent_total"] = sum(mon.values())
            g["sent_hours_utc"] = GM["sent_hours_utc"].get(em)
    # GCal
    for cal, v in O["gcal"]["person"].items():
        P(cal)["services"]["gcal"] = {"first_event": v["first"], "last_event": v["last"], "monthly_events": v["monthly"], "organized_copies": v["organized"],
                                       "hours_local": v["hours_local"], "calendar_tz": O["gcal"]["calendars"].get(cal, {}).get("tz")}
    # Linear
    for uid, v in LI["person"].items():
        em = (LI["users"].get(uid) or {}).get("email")
        if em and "@" in em:
            P(em)["services"]["linear"] = {"user_id": uid, "first": v["first"], "last": v["last"], "created_monthly": v["created"], "completed_monthly": v["completed"],
                                            "assigned_open": v["assigned_open"], "assigned_total": v["assigned_total"]}
    # Confluence
    for k, v in O["confluence"]["person"].items():
        if k and "@" in k:
            P(k)["services"]["confluence"] = v
    # Drive
    for k, v in O["drive"]["person"].items():
        if k and "@" in k:
            P(k)["services"]["drive"] = {"files_owned": v["files"], "first_created": v["first"], "last_modified": v["modified_last"], "created_monthly": v["created"]}
    # GitHub (exact_email joins from entities.json)
    for em, logins in gh_by_email.items():
        agg = {"logins": logins, "join_basis": "entities.json exact_email", "commits_monthly": collections.Counter(), "prs_monthly": collections.Counter(), "reviews_monthly": collections.Counter(), "first": None, "last": None}
        for lg in logins:
            v = GH["login"].get(lg)
            if not v:
                continue
            for k_, kk in (("commits", "commits_monthly"), ("prs", "prs_monthly"), ("reviews", "reviews_monthly")):
                agg[kk].update(v[k_])
            agg["first"] = v["first"] if not agg["first"] or (v["first"] and v["first"] < agg["first"]) else agg["first"]
            agg["last"] = v["last"] if not agg["last"] or (v["last"] and v["last"] > agg["last"]) else agg["last"]
        for kk in ("commits_monthly", "prs_monthly", "reviews_monthly"):
            agg[kk] = dict(sorted(agg[kk].items()))
        P(em)["services"]["github"] = agg
    # Trello (informational only: name-joined)
    tper = O["trello"]["person"]
    for em, lst in tr_by_email.items():
        for mid, how in lst:
            v = tper.get(mid)
            P(em)["services"]["trello_informational"] = {"member_id": mid, "join_basis": "entities.json " + str(how) + " (not email; excluded from status)",
                                                         "first": v and v["first"], "last": v and v["last"], "actions": sum((v or {}).get("monthly", {}).values())}
    # finalize
    out_people = {}
    for em, p in people.items():
        if not em.endswith("@harmonygames.co"):
            continue
        p["persona"] = roster.get(em)
        sv = p["services"]
        lasts = {}
        firsts = {}
        mon_total = collections.Counter()
        def add(svc, first, last):
            if last:
                lasts[svc] = last[:10]
            if first:
                firsts[svc] = first[:10]
        s = sv.get("slack") or {}
        add("slack", s.get("first"), s.get("last"))
        mon_total.update(s.get("monthly") or {})
        g = sv.get("gmail") or {}
        add("gmail_sent", g.get("sent_first"), g.get("sent_last"))
        mon_total.update(g.get("sent_monthly") or {})
        c = sv.get("gcal") or {}
        if c.get("last_event"):
            lasts["gcal_attended"] = c["last_event"][:10]
        l = sv.get("linear") or {}
        add("linear", l.get("first"), l.get("last"))
        mon_total.update(l.get("created_monthly") or {})
        mon_total.update(l.get("completed_monthly") or {})
        gh = sv.get("github") or {}
        add("github", gh.get("first"), gh.get("last"))
        for kk in ("commits_monthly", "prs_monthly", "reviews_monthly"):
            mon_total.update(gh.get(kk) or {})
        cf = sv.get("confluence") or {}
        add("confluence", cf.get("first"), cf.get("last"))
        dr = sv.get("drive") or {}
        add("drive", dr.get("first_created"), dr.get("last_modified"))
        mon_total.update(dr.get("created_monthly") or {})
        authored = {k: v for k, v in lasts.items() if k != "gcal_attended" and v < CLOCK_ISO[:10]}
        last_any = max(authored.values()) if authored else None
        last_svc = max(authored, key=authored.get) if authored else None
        if last_any and last_any >= ACTIVE_FROM:
            status = ACTIVE_KEY
        elif last_any and last_any >= RECENT_FROM:
            status = RECENT_KEY
        elif last_any:
            status = "quiet_since_" + last_any[:7]
        else:
            status = "no_authored_activity"
        sl = s.get("channel_leaves") or {}
        dep = {"last_authored_activity": last_any, "last_authored_service": last_svc,
               "last_slack_message": (s.get("last") or "")[:10] or None, "last_gmail_sent": (g.get("sent_last") or "")[:10] or None,
               "gmail_mailbox_last": ((g.get("mailbox") or {}).get("last") or "")[:10] or None,
               "last_github": (gh.get("last") or "")[:10] or None, "last_linear": (l.get("last") or "")[:10] or None,
               "slack_channel_leaves": sl.get("count", 0), "slack_last_leaves": sl.get("last", []),
               "open_linear_issues_assigned": l.get("assigned_open")}
        out_people[em] = {"name": p["name"] or (p["persona"] or {}).get("persona_key"), "slack_id": p["slack_id"], "persona": p["persona"],
                          "status_at_clock": status, "first_activity_by_service": firsts, "last_activity_by_service": lasts,
                          "monthly_authored_total": dict(sorted(mon_total.items())), "departure_signals": dep, "services": sv}
    act = sorted([e for e, v in out_people.items() if v["status_at_clock"] == ACTIVE_KEY])
    recent = sorted([e for e, v in out_people.items() if v["status_at_clock"] == RECENT_KEY])
    quiet = sorted([(v["departure_signals"]["last_authored_activity"] or "", e) for e, v in out_people.items() if v["status_at_clock"].startswith("quiet")], reverse=True)
    gh_unjoined = {lg: {"name": v.get("name"), "type": v.get("type"), **{k: GH["login"].get(lg, {}).get(k) for k in ("first", "last")}}
                   for lg, v in GH["users"].items() if not any(lg in l for l in gh_by_email.values())}
    voices = []
    for em in act:
        v = out_people[em]
        s = v["services"].get("slack") or {}
        active_volume = (s.get("monthly") or {}).get(ACTIVE_YM, 0)
        recent_volume = (s.get("monthly") or {}).get(RECENT_YM, 0)
        voices.append({"email": em, "name": v["name"], "persona_key": (v["persona"] or {}).get("persona_key"),
                           "slack_msgs_" + RECENT_COLUMN: recent_volume, "slack_msgs_" + ACTIVE_COLUMN: active_volume,
                           "gmail_sent_" + ACTIVE_COLUMN: ((v["services"].get("gmail") or {}).get("sent_monthly") or {}).get(ACTIVE_YM, 0),
                           "last": v["departure_signals"]["last_authored_activity"], "last_service": v["departure_signals"]["last_authored_service"]})
    voices.sort(key=lambda x: -(x["slack_msgs_" + ACTIVE_COLUMN] + x["gmail_sent_" + ACTIVE_COLUMN]))
    out = {
        "_meta": {"clock": CLOCK_ISO, "generated_by": "Task_Authoring/references/universe_kb/_build/assemble_activity.py",
                  "join_rules": "People keyed by exact email. Slack joined by the users.json email (Slack id kept). Gmail by mailbox/From address, GCal by calendar_id, Linear/Confluence/Drive by user email. GitHub logins attached only where entities.json joined them by exact_email. Trello is name-joined in entities.json, so it is shown under trello_informational and never used for status.",
                  "status_rule": "Latest authored record before the clock: %s >= %s; %s >= %s; else quiet_since_<YYYY-MM>. Calendar attendance is not authored activity." % (ACTIVE_KEY, ACTIVE_FROM, RECENT_KEY, RECENT_FROM),
                  "slack_hours": "hours_utc are UTC hour histograms; every Slack profile says America/Los_Angeles, so use the GCal calendar_tz to localise.",
                  "limits": ["Slack messages with no email-bearing user (tokens such as EMPLOYEE_0024_SLACK_ID, PERSON_n) are under slack_only_ids, unjoined.",
                             "Gmail mailboxes named by tokens (EMPLOYEE_0011_EMAIL, SVC_0293_EMAIL ...) are not joined to anyone.",
                             "GitHub logins without an email join are listed under github_unjoined_logins (CodeRabbit, linear[bot], tokenised contributors).",
                             "Snowflake PAYROLL_ROSTER/HEADCOUNT use EMPLOYEE_n tokens + names; they are not joined here (see coherence_hazards for roster conflicts)."]},
        "summary": {"people": len(out_people), ACTIVE_KEY: act, RECENT_KEY: recent,
                    "quiet_or_departed": [{"email": e, "last_authored": d} for d, e in quiet]},
        "seed_voice_candidates_" + ACTIVE_MONTH.strftime("%b_%Y").lower(): voices,
        "people": dict(sorted(out_people.items())),
        "slack_only_ids": slack_only,
        "github_unjoined_logins": gh_unjoined,
    }
    jdump(out, OUT + "/activity.json", indent=1)
    print("activity", len(out_people), ACTIVE_KEY, len(act), RECENT_KEY, len(recent))


if __name__ == "__main__":
    main()
