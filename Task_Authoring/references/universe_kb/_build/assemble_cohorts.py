"""cohorts.json: natural record sets of 40-500 with exact counts, the selection rule, per-record surfaces,
whether a bulk call returns those surfaces (Ask_Carriers §6b / Hardness_Mastery §2.5) and hazards inside."""
import re, json, collections, datetime
from common import *
from pass_other import norm_title

LO, HI = 40, 500

SURF = {
    "linear_issue": {"per_record_surfaces": ["description (truncated in list)", "comments (linear_list_comments; 0 in base -> seeded only)", "attachments (linear_get_attachments)", "parent/relations", "state, labels, assignee"],
                     "bulk": "linear_list_issues returns state/labels/assignee/parent/relations/description(+truncated flag); NO comments. Only Linear comments are an honest one-call-per-record surface (verified, §6b).",
                     "honest_per_record_calls": "1 (list_comments) when the seeded fact lives in comments; else ~0"},
    "github_pr": {"per_record_surfaces": ["title/body/head_ref", "conversation comments", "reviews", "review comments", "timeline", "commits/files"],
                  "bulk": "search/list return title/body/branch/merged_at. Comments and reviews are per PR in GitHub, BUT "
                          + ("GameOfDominoes, game-of-dominoes-backend and match3d (2025-06-30..2025-10-24) are mirrored into Slack (#engineering-bots / #zombie-prs) and sweepable at ~50/page. Combo-Fighters, liveops, match3d-backend and other repos are NOT mirrored."
                             if shutdown_rules_apply() else
                             "repos with a Slack mirror (see integrations.json INT-01 for this universe's windows) are sweepable at ~50/page; unmirrored repos are per-PR reads."),
                  "honest_per_record_calls": "unmirrored repo: comments + reviews + timeline ~2-3; mirrored repo: timeline/files/commits only"},
    "slack_thread": {"per_record_surfaces": ["replies"], "bulk": "slack_conversations_search_messages returns replies; filter-only search (channel+user) pages everything (verified). Not per-record volume.",
                     "honest_per_record_calls": "0 against a determined agent; useful only as the A14 behavioural trap"},
    "gmail_thread": {"per_record_surfaces": ["messages", "quoted history", "attachments"], "bulk": "gmail_get_messages_batch collapses N reads; search returns snippets.", "honest_per_record_calls": "0.2-0.5 (attachments are the only per-item hook)"},
    "trello_card": {"per_record_surfaces": ["desc", "comments", "checklists", "card actions"], "bulk": "trello_get_board_actions (comment filter) and trello_get_checklists_on_board are bulk.", "honest_per_record_calls": "0.2-0.5"},
    "gcal_instance": {"per_record_surfaces": ["attendees/responses", "description (absent in base)"], "bulk": "gcal_list_events over a window returns them.", "honest_per_record_calls": "~0"},
    "snowflake_row": {"per_record_surfaces": ["row columns", "FAILURE_NOTE / NOTES text"], "bulk": "one SQL query returns all rows.", "honest_per_record_calls": "0"},
    "doc": {"per_record_surfaces": ["body_text"], "bulk": "none; gdocs_get_document per doc (search returns titles).", "honest_per_record_calls": "1"},
    "slides_deck": {"per_record_surfaces": ["page text"], "bulk": "gslides_get_presentation_text returns a whole deck in one call.", "honest_per_record_calls": "1 per deck"},
}


def C(cid, service, kind, name, rule, ids, hazards=None, notes=None):
    n = len(ids)
    return {"id": cid, "service": service, "record_kind": kind, "name": name, "selection_rule": rule, "count": n,
            "ids": sorted(ids) if n <= HI else None, "sample_ids": sorted(ids)[:10], **SURF.get(kind, {}),
            "hazards_inside": hazards or {}, **({"notes": notes} if notes else {})}


def inter(ids, named_lists):
    s = set(ids)
    out = {}
    for name, lst in named_lists.items():
        k = [x for x in lst if x in s]
        if k:
            out[name] = {"count": len(k), "ids": k[:10]}
    return out


def q(d):
    d = iso_to_dt(d)
    return "%d-Q%d" % (d.year, (d.month - 1) // 3 + 1) if d else None


def main():
    LI = jload_cache("kb_linear.json")
    GH = jload_cache("kb_github.json")
    S = jload_cache("kb_slack.json")
    GM = jload_cache("kb_gmail.json")
    O = jload_cache("kb_other.json")
    HZ = jload_kb("coherence_hazards.json")
    allhz = {h["id"]: h for v in HZ["categories"].values() for h in v}
    issues = LI["issue_index"]
    cohorts = []
    # ---- Linear hazard lists (full) ----
    lhz = {k: v.get("all") or v["examples"] for k, v in LI["hazards"].items()}
    for k, v in GH["linear_github_join"].items():
        lhz["linear+github: " + k] = [x[0] for x in v["examples"]] if v["count"] <= 10 else [x[0] for x in v["examples"]]
    lhz["L08 open issue assigned to quiet/departed person"] = [x.split(" ")[0] for x in allhz["L08"]["examples"]]
    # recompute L08 fully
    A = jload_kb("activity.json")
    st = {em: v["status_at_clock"] for em, v in A["people"].items()}
    lue = {k: v.get("email") for k, v in LI["users"].items()}
    DONE = {"Done", "Canceled", "Duplicate"}
    lhz["L08 open issue assigned to quiet/departed person"] = [i for i, r in issues.items() if r[1] not in DONE and r[2] and (st.get(lue.get(r[2])) or "").startswith("quiet")]
    lhz["R01-style: issue never mentioned anywhere else"] = []
    by_ts = collections.defaultdict(list)
    by_tl = collections.defaultdict(list)
    for i, r in issues.items():
        by_ts[(r[0], r[1])].append(i)
        for l in r[8] or []:
            by_tl[(r[0], l)].append(i)
    n = 0
    for (team, state), ids in sorted(by_ts.items(), key=lambda kv: -len(kv[1])):
        if LO <= len(ids) <= HI:
            n += 1
            cohorts.append(C("LIN-S%02d" % n, "linear", "linear_issue", "%s issues in state %s" % (team, state), "team_id=team_%s AND state_id='%s'" % (team, state), ids, inter(ids, lhz)))
    opn = [i for i, r in issues.items() if r[1] not in DONE]
    cohorts.append(C("LIN-OPEN", "linear", "linear_issue", "All open issues at the clock (any team)", "state_id NOT IN (Done, Canceled, Duplicate)", opn, inter(opn, lhz)))
    for team in ("ENG", "ZOM"):
        ids = [i for i in opn if issues[i][0] == team]
        if len(ids) >= LO:
            cohorts.append(C("LIN-OPEN-" + team, "linear", "linear_issue", "Open %s issues at the clock" % team, "team_%s AND state NOT IN (Done, Canceled, Duplicate)" % team, ids, inter(ids, lhz)))
    n = 0
    for (team, lab), ids in sorted(by_tl.items(), key=lambda kv: -len(kv[1])):
        if LO <= len(ids) <= HI:
            n += 1
            cohorts.append(C("LIN-L%02d" % n, "linear", "linear_issue", "%s issues labelled '%s'" % (team, lab), "team_%s AND '%s' IN labels_json" % (team, lab), ids, inter(ids, lhz)))
    byq = collections.defaultdict(list)
    byqc = collections.defaultdict(list)
    for i, r in issues.items():
        if r[4]:
            byq[(r[0], q(r[4]))].append(i)
        if r[6] and r[1] == "Done":
            byqc[(r[0], q(r[6]))].append(i)
    n = 0
    for (team, qq), ids in sorted(byq.items()):
        if LO <= len(ids) <= HI and qq >= "2024":
            n += 1
            cohorts.append(C("LIN-CQ%02d" % n, "linear", "linear_issue", "%s issues created in %s" % (team, qq), "team_%s AND created_at in %s" % (team, qq), ids, inter(ids, lhz)))
    n = 0
    for (team, qq), ids in sorted(byqc.items()):
        if LO <= len(ids) <= HI and qq >= "2024":
            n += 1
            cohorts.append(C("LIN-DQ%02d" % n, "linear", "linear_issue", "%s issues completed (Done) in %s" % (team, qq), "team_%s AND state Done AND completed_at in %s" % (team, qq), ids, inter(ids, lhz)))
    upd = [i for i, r in issues.items() if r[0] in ("ENG", "ZOM") and (r[5] or "") >= "2025-08-13"]
    cohorts.append(C("LIN-UPD", "linear", "linear_issue", "ENG/ZOM issues updated since 2025-08-13 (Hardness_Mastery §2.5 pattern 1 population)", "team IN (ENG,ZOM) AND updated_at >= 2025-08-13", upd, inter(upd, lhz)))
    kids = collections.defaultdict(list)
    for i, r in issues.items():
        if r[9]:
            kids[r[9]].append(i)
    big = [(p, k) for p, k in kids.items() if len(k) >= 15]
    epic_kids = [i for p, k in big for i in k]
    if epic_kids:
        cohorts.append(C("LIN-EPIC", "linear", "linear_issue", "Children of epics with >=15 children (%d parents)" % len(big), "parent_id IN (parents with >=15 children)", epic_kids, inter(epic_kids, lhz), notes={"parents": {p: len(k) for p, k in sorted(big, key=lambda x: -len(x[1]))[:15]}}))
    L = jload(LINEAR)
    att = collections.defaultdict(int)
    for a in L["attachments"]:
        att[a["issue_identifier"]] += 1
    del L
    with_att = [i for i in att if i in issues and issues[i][0] in ("ENG", "ZOM") and (issues[i][4] or "") >= "2025"]
    cohorts.append(C("LIN-ATT", "linear", "linear_issue", "ENG/ZOM issues created 2025+ that have attachment blobs", "attachments.issue_identifier = issue AND created_at >= 2025-01-01", with_att, inter(with_att, lhz),
                     notes="513 attachment rows are tagged surface 'comment' although the base has 0 comments"))
    # ---- GitHub ----
    G = jload(GITHUB)
    prs = G["pull_requests"]
    revs = collections.defaultdict(list)
    for r in G["reviews"]:
        revs[r["pr_id"]].append(r)
    del G
    ghz = {k: v.get("all") or v["examples"] for k, v in GH["hazards"].items() if not k.startswith("_")}
    ghz["no Slack mirror for a GitHub comment"] = [x.rsplit("#c_", 1)[0] for x in sum(GH["github_comments_without_slack_copy_examples"].values(), [])]
    for k, v in GH["linear_github_join"].items():
        ghz["linear+github: " + k] = [x[1] for x in v["examples"]]
    mirror_win = {r: v["mirror_window"] for r, v in GH["slack_mirror"]["per_repo"].items() if v["mirror_window"]}
    byrq = collections.defaultdict(list)
    for p in prs:
        byrq[(p["repo_id"].split("/")[1], q(p["created_at"]))].append(p["id"])
    n = 0
    for (repo, qq), ids in sorted(byrq.items()):
        if LO <= len(ids) <= HI:
            n += 1
            mirrored = repo in mirror_win
            cohorts.append(C("GH-Q%02d" % n, "github", "github_pr", "%s PRs created in %s" % (repo, qq), "repo=%s AND created_at in %s" % (repo, qq), ids, inter(ids, ghz),
                             notes="Slack-mirrored repo (window %s..%s)" % tuple(x[:10] for x in mirror_win[repo]) if mirrored else "NOT mirrored to Slack -> comments/reviews are per-PR reads"))
    m3 = [p["id"] for p in prs if p["repo_id"].endswith("/match3d") and mirror_win.get("match3d") and p["created_at"] >= mirror_win["match3d"][0][:10]]
    m3_win = mirror_win.get("match3d")
    m3_after_from = (iso_to_dt(m3_win[1]) + datetime.timedelta(days=1)).date().isoformat() if m3_win else None
    m3_after = [p["id"] for p in prs if p["repo_id"].endswith("/match3d") and m3_after_from and p["created_at"] > m3_after_from]
    if m3_after:
        cohorts.append(C("GH-M3-AFTER", "github", "github_pr", "match3d PRs created after the Slack mirror stopped (%s+)" % m3_after_from, "repo=match3d AND created_at > %s" % m3_after_from, m3_after, inter(m3_after, ghz), notes="unmirrored: comments/reviews only via per-PR GitHub reads"))
    unm = [p["id"] for p in prs if p["state"] == "closed" and not p["merged"]]
    cohorts.append(C("GH-CLOSED", "github", "github_pr", "PRs closed without merge (all repos)", "state=closed AND merged=false", unm, inter(unm, ghz)))
    keyed = list(GH["pr_linear_keys"].keys())
    cohorts.append(C("GH-KEYED", "github", "github_pr", "PRs whose title/branch/body names a Linear key", "regex (ENG|ZOM|ART|DES|EPI)-?\\d+ in title, head_ref or body", keyed, inter(keyed, ghz),
                     notes="Linear links_json is empty on all issues; this regex join is the only Linear<->GitHub bridge (plus linear[bot] PR comments)"))
    crr = [p["id"] for p in prs if p["merged"] and revs.get(p["id"]) and all(r["author_login"] == "PERSON_6026_GITHUB_USERNAME" for r in revs[p["id"]])]
    if len(crr) >= 10:
        cohorts.append(C("GH-CRONLY", "github", "github_pr", "Merged PRs reviewed only by CodeRabbit", "merged AND every review author = PERSON_6026 (CodeRabbit)", crr, inter(crr, ghz)))
    # ---- Slack thread roots ----
    chans = {c["id"]: c for c in jload(SLACK + "/channels.json")}
    rc_bad = set(x[0] for x in S["thread"]["reply_count_mismatch"] + S["thread"]["reply_users_mismatch"] + S["thread"]["latest_reply_mismatch"])
    n = 0
    for cid, roots in sorted(S["thread_roots"].items(), key=lambda kv: -len(kv[1])):
        human = [r for r in roots if not r[3]]
        ids = ["%s/%s" % (cid, r[0]) for r in human]
        c = chans.get(cid, {})
        if c.get("is_im"):
            continue
        if LO <= len(ids) <= HI:
            n += 1
            cohorts.append(C("SL-T%02d" % n, "slack", "slack_thread", "Human thread roots with replies in %s" % (c.get("name") or cid), "channel=%s AND thread_ts=ts AND >=1 reply AND not bot" % cid, ids,
                             {"reply counter mismatch": {"count": len(rc_bad & set(ids)), "ids": sorted(rc_bad & set(ids))[:10]}} if rc_bad & set(ids) else {},
                             notes={"private": c.get("is_private"), "archived": c.get("is_archived"), "members": c.get("num_members"), "replies_total": sum(r[1] for r in human)}))
        elif len(ids) > HI:
            byy = collections.defaultdict(list)
            for r in human:
                byy[ts_to_dt(float(r[0])).strftime("%Y")].append("%s/%s" % (cid, r[0]))
            for y, yids in sorted(byy.items()):
                if LO <= len(yids) <= HI:
                    n += 1
                    cohorts.append(C("SL-T%02d" % n, "slack", "slack_thread", "Human thread roots with replies in %s during %s" % (c.get("name") or cid, y), "channel=%s AND year(ts)=%s AND >=1 reply" % (cid, y), yids,
                                     {}, notes={"private": c.get("is_private"), "members": c.get("num_members")}))
    # ---- Gmail ----
    hs = collections.defaultdict(set)
    hs_mb = collections.defaultdict(lambda: collections.defaultdict(list))
    for prod, plat, num, mb, d, isre, rid, frm in GM["helpshift_mails"]:
        hs[(prod, plat)].add(num)
        hs_mb[mb][(prod, plat)].append(rid)
    allh = sorted(set("%s %s #%d" % (p, pl, n_) for (p, pl), s in hs.items() for n_ in s))
    cohorts.append(C("GM-HELPSHIFT", "gmail", "gmail_thread", "Distinct Helpshift issues announced by mail (product, platform, issue #)", "subject ~ 'New <product> <platform> issue #N' or 'replied to ... issue #N' from svc_0143", allh, {},
                     notes={"mails_by_mailbox": {mb: sum(len(v) for v in d.values()) for mb, d in hs_mb.items()}, "per_platform": {"%s %s" % k: len(v) for k, v in hs.items()}}))
    for mb, d in hs_mb.items():
        ids = sum(d.values(), [])
        if LO <= len(ids) <= HI:
            cohorts.append(C("GM-HS-" + mb.split("@")[0].split("_")[0], "gmail", "gmail_thread", "Helpshift issue mails in %s" % mb, "mailbox=%s AND Helpshift subject" % mb, ids, {}))
    cr = collections.defaultdict(list)
    for patt, mb, d, rid in GM["crash_mails"]:
        if d:
            cr[(mb, d[:4])].append(rid)
    for (mb, y), ids in sorted(cr.items()):
        if LO <= len(ids) <= HI:
            cohorts.append(C("GM-CRASH-%s-%s" % (mb.split("@")[0], y), "gmail", "gmail_thread", "Crashlytics 'Trending stability issues' digests in %s, %s" % (mb, y), "mailbox=%s AND subject ~ Trending stability issues AND year=%s" % (mb, y), ids, {}))
    tf = collections.defaultdict(list)
    for app, ver, b, mb, d, rid in GM["testflight_mails"]:
        if mb == "robert@harmonygames.co" or True:
            tf[(app, mb)].append(rid)
    for (app, mb), ids in sorted(tf.items(), key=lambda kv: -len(kv[1])):
        if LO <= len(ids) <= HI:
            cohorts.append(C("GM-TF-%s-%s" % (re.sub(r"\W+", "", app)[:12], mb.split("@")[0]), "gmail", "gmail_thread", "TestFlight 'is now available to test' mails for %s in %s" % (app, mb), "subject ~ '<app> <ver> (<build>) for iOS is now available to test'", ids, {}))
    meta = [p for p in GM["subject_patterns"] if "meta ads receipt" in p["pattern"].lower()]
    inv = collections.defaultdict(list)
    for kind, summ, when, mb, d, rid, frm in GM["calendar_mails"]:
        if kind == "Invitation":
            inv[mb].append(rid)
    for mb, ids in inv.items():
        if LO <= len(ids) <= HI:
            cohorts.append(C("GM-INV-" + mb.split("@")[0], "gmail", "gmail_thread", "Calendar 'Invitation:' mails in %s" % mb, "subject ^Invitation: ... @ <when>", ids, {"R08 invite without GCal instance": {"count": "see coherence_hazards R08"}}))
    # ---- Trello ----
    T = jload(TRELLO)
    lists = {l["id"]: l for l in T["lists"]}
    boards = {b["id"]: b["name"] for b in T["boards"]}
    thz = {k: v.get("all") or v["examples"] for k, v in O["trello"]["hazards"].items()}
    bylist = collections.defaultdict(list)
    byboard = collections.defaultdict(list)
    for c in T["cards"]:
        bylist[c["idList"]].append(c["id"])
        if not c.get("closed"):
            byboard[c["idBoard"]].append(c["id"])
    for lid, ids in sorted(bylist.items(), key=lambda kv: -len(kv[1])):
        if LO <= len(ids) <= HI:
            l = lists[lid]
            cohorts.append(C("TR-" + lid[-6:], "trello", "trello_card", "Cards in list '%s' on %s" % (l["name"], boards[l["idBoard"]]), "idList=%s" % lid, ids, inter(ids, thz)))
    for bid, ids in byboard.items():
        if LO <= len(ids) <= HI:
            cohorts.append(C("TR-B-" + bid[-6:], "trello", "trello_card", "Open cards on board %s" % boards[bid], "idBoard=%s AND closed=false" % bid, ids, inter(ids, thz)))
    del T
    # ---- GCal ----
    Cg = jload(GCAL)
    grp = collections.defaultdict(set)
    for e in Cg["events"]:
        grp[norm_text(e.get("summary"))].add(((e.get("start") or {}).get("dateTime"), e.get("ical_uid"), e["event_id"]))
    dup_cal = set(tuple(x) for x in O["gcal"]["duplicate_copy_same_calendar"].get("all") or [])
    n = 0
    for summ, inst in sorted(grp.items(), key=lambda kv: -len(kv[1])):
        starts = sorted(set(x[0] for x in inst if x[0]))
        if LO <= len(starts) <= HI:
            n += 1
            first_ids = {}
            for s_, u, eid in sorted(inst):
                first_ids.setdefault(s_, eid)
            cohorts.append(C("GC-S%02d" % n, "gcal", "gcal_instance", "Meeting instances titled '%s'" % summ, "normalised summary = '%s' (one id per distinct start)" % summ, list(first_ids.values()), {},
                             notes={"first": starts[0], "last": starts[-1], "uids": len(set(x[1] for x in inst)), "rows": len(inst)}))
    del Cg
    # ---- Snowflake ----
    sf = O["snowflake"]
    cohorts.append({"id": "SF-LEP", "service": "snowflake", "record_kind": "snowflake_row", "name": "LIVE_EVENT_PERFORMANCE runs by status", "selection_rule": "GROUP BY STATUS", "count": sum(sf["live_event_status"].values()),
                    "detail": {"by_status": sf["live_event_status"], "failure_notes": sf["live_event_failure_notes"]}, **SURF["snowflake_row"], "hazards_inside": {"L14": "completed rows during Slack-reported outages"}})
    cohorts.append({"id": "SF-LEDGER", "service": "snowflake", "record_kind": "snowflake_row", "name": "FINANCE_LEDGER rows by category", "selection_rule": "GROUP BY CATEGORY", "count": sum(sf["ledger_categories"].values()),
                    "detail": {"by_category": sf["ledger_categories"], "rows_since_2025_09": sf["ledger_rows_since_2025_09"]}, **SURF["snowflake_row"], "hazards_inside": {"Q05": "2023-09 burn vs ledger"}})
    cohorts.append({"id": "SF-REVIEWS", "service": "snowflake", "record_kind": "snowflake_row", "name": "APP_STORE_REVIEWS incident_related=true by month", "selection_rule": "INCIDENT_RELATED = true", "count": sum(sf["reviews_by_month_incident"].values()),
                    "detail": sf["reviews_by_month_incident"], **SURF["snowflake_row"], "hazards_inside": {}})
    # ---- Docs / Slides ----
    nat = O["native"]
    fam = collections.defaultdict(list)
    for r in nat["docs"]["rows"]:
        t = r[1] or ""
        key = "Company Stand Up (...)" if t.startswith("Company Stand Up") else ("... Notes by Gemini" if "Notes by Gemini" in t else norm_title(t).split(" ")[0] if t else "")
        fam[key].append(r[0])
    for k, ids in sorted(fam.items(), key=lambda kv: -len(kv[1])):
        if LO <= len(ids) <= HI and k:
            cohorts.append(C("DOC-" + re.sub(r"\W+", "", k)[:16], "gdocs", "doc", "Docs titled like '%s'" % k, "title family '%s'" % k, ids, {}))
    sfam = collections.defaultdict(list)
    for r in nat["slides"]["rows"]:
        sfam[norm_title(r[1])].append(r[0])
    for k, ids in sorted(sfam.items(), key=lambda kv: -len(kv[1])):
        if len(ids) >= 10:
            cohorts.append(C("SLD-" + re.sub(r"\W+", "", k)[:16], "gslides", "slides_deck", "Decks titled '%s'" % k, "normalised title = '%s'" % k, ids, {}, notes="below 40; listed because deck families are common decoys"))
    out = {"_meta": {"generated_by": "Task_Authoring/references/universe_kb/_build/assemble_cohorts.py", "range": [LO, HI],
                     "use": "Natural record sets for the cohort spine (Hardness_Mastery §2). 'bulk' says whether a list/batch/search call already returns the per-record surface; only Linear comments (seeded) and unmirrored PR comments/reviews are honest per-record reads. 'hazards_inside' intersects the cohort with coherence_hazards lists - exclude those ids or define the rule.",
                     "not_cohorts": "Confluence (31 pages, 78 versions, 12 comments) and Contacts (171) are below range; Snowflake row sets collapse to one GROUP BY."},
           "cohorts": cohorts,
           "index": [{"id": c["id"], "service": c["service"], "name": c["name"], "count": c["count"], "hazard_hits": sum((v.get("count") if isinstance(v, dict) and isinstance(v.get("count"), int) else 0) for v in c["hazards_inside"].values()) if isinstance(c["hazards_inside"], dict) else 0} for c in cohorts]}
    jdump(out, OUT + "/cohorts.json", indent=1)
    print("cohorts", len(cohorts))


if __name__ == "__main__":
    main()
