"""integrations.json and conventions.json."""
import os, re, json, collections, datetime
from zoneinfo import ZoneInfo
from common import *
from pass_other import norm_title

GM_CATS = [
    ("helpshift_new_issue", re.compile(r"^New .+ issue #\d+")),
    ("helpshift_reply", re.compile(r"replied to .+ issue #\d+")),
    ("crashlytics_digest", re.compile(r"Trending stability issues")),
    ("testflight_build", re.compile(r"is now available to test")),
    ("firebase_app_distribution", re.compile(r"^Version .+ \(\d+\) of .+ Available")),
    ("app_store_review", re.compile(r"^Review of your .*submission is complete")),
    ("calendar_invitation", re.compile(r"^Invitation: .+ @ ")),
    ("calendar_rsvp", re.compile(r"^Accepted: .+ @ ")),
    ("github_notification", re.compile(r"\((PR|Issue) #\d+\)$")),
    ("linear_digest", re.compile(r"unread notifications on")),
    ("linear_autoclose", re.compile(r"auto-closed (ENG|ZOM|ART|DES)-\d+")),
    ("slack_notification", re.compile(r"^\[Slack\]")),
    ("meta_receipt", re.compile(r"(?i)your meta ads receipt")),
    ("carta_termination", re.compile(r"Termination details for")),
]


def gmail_samples():
    found = {}
    TD = GMAIL + "/threads"
    for fn in sorted(os.listdir(TD), reverse=True):
        if len(found) == len(GM_CATS):
            break
        t = jload(TD + "/" + fn)
        for m in t.get("messages") or []:
            subj = m.get("subject") or ""
            for name, rx in GM_CATS:
                if name not in found and rx.search(subj):
                    found[name] = {"file": fn, "mailbox": t.get("user_email"), "message_id": m.get("id"), "subject": subj[:140], "from": m.get("from"), "to": (m.get("to") or "")[:120],
                                   "labelIds": m.get("labelIds"), "date": m.get("date"), "body_head": (m.get("body") or "")[:260]}
    return found


def slack_record(cid, ts):
    mon = month_of_ts(float(ts))
    p = SLACK + "/messages/%s/%s.json" % (cid, mon)
    if not os.path.exists(p):
        return None
    for x in jload(p):
        if x.get("ts") == ts:
            x = dict(x)
            x.pop("blocks", None)
            x.pop("user_profile", None)
            for a in x.get("attachments") or []:
                if isinstance(a.get("text"), str):
                    a["text"] = a["text"][:200]
                if a.get("actions"):
                    a["actions"] = "[%d action buttons; value carries PR number/title JSON]" % len(a["actions"])
                a.pop("blocks", None)
            x["files"] = "[%d]" % len(x.get("files") or [])
            return x
    return None


def core_window(hist, share=0.8):
    tot = sum(hist)
    if not tot:
        return None
    best = None
    for start in range(24):
        acc = 0
        for L in range(1, 25):
            acc += hist[(start + L - 1) % 24]
            if acc >= share * tot:
                if best is None or L < best[1]:
                    best = (start, L)
                break
    return {"start_hour": best[0], "hours": best[1], "end_hour": (best[0] + best[1]) % 24}


def tz_shift(hist_utc, tz):
    if not tz:
        return hist_utc
    m = re.match(r"UTC([+-])(\d\d):(\d\d)", tz)
    if m:
        off = (1 if m.group(1) == "+" else -1) * int(m.group(2))
    elif tz == "UTC":
        off = 0
    else:
        try:
            off = int(datetime.datetime(2025, 3, 1, tzinfo=ZoneInfo(tz)).utcoffset().total_seconds() // 3600)
        except Exception:
            off = 0
    return [hist_utc[(h - off) % 24] for h in range(24)]


def main():
    S = jload(CACHE + "/kb_slack.json")
    GM = jload(CACHE + "/kb_gmail.json")
    GH = jload(CACHE + "/kb_github.json")
    LI = jload(CACHE + "/kb_linear.json")
    O = jload(CACHE + "/kb_other.json")
    J = jload(CACHE + "/kb_join_stats.json")
    A = jload(OUT + "/activity.json")
    si = S["integrations"]
    mirror = S["gh_mirror"]
    # ---------- GitHub app mirror shape ----------
    kinds = collections.defaultdict(lambda: {"n": 0, "threaded": 0, "broadcast": 0, "sample": None})
    for m in mirror:
        k = kinds[m[5]]
        k["n"] += 1
        if m[2] and m[2] != m[1]:
            k["threaded"] += 1
        if m[9] == "thread_broadcast":
            k["broadcast"] += 1
        if k["sample"] is None and m[4] is not None:
            k["sample"] = "%s/%s" % (m[0], m[1])
    gh_kinds = {}
    for kname, v in sorted(kinds.items(), key=lambda kv: -kv[1]["n"]):
        if v["n"] < 20:
            continue
        rec = slack_record(*v["sample"].split("/")) if v["sample"] else None
        gh_kinds[kname] = {"messages": v["n"], "threaded_under_opened_parent_share": round(v["threaded"] / v["n"], 3), "thread_broadcast_share": round(v["broadcast"] / v["n"], 3),
                           "example_id": v["sample"], "example_shape": rec}
    ints = []
    def I(iid, src, dst, name, shape, base_rates, seeding_rule, evidence, window=None):
        ints.append({"id": iid, "source": src, "destination": dst, "name": name, "window": window, "shape": shape, "base_rates": base_rates, "seeding_rule": seeding_rule, "evidence": evidence})
    sm = GH["slack_mirror"]
    I("INT-01", "github", "slack", "GitHub Slack app -> #engineering-bots (C050WGU41HR: GameOfDominoes, game-of-dominoes-backend) and #zombie-prs (C093LEZGF6J: match3d)",
      {"user": "SLACK_BOT_0004_SLACK_ID", "text": "", "attachments[0]": {"fallback": "[harmonygames-Games/<repo>] <Event> by <real.login>", "pretext": "<Event> by <https://github.com/<login>|<login>>", "title": "<https://github.com/harmonygames-Games/<repo>/pull/<N>|#<N> <PR title>>", "footer": "<https://github.com/harmonygames-Games/<repo>|harmonygames-Games/<repo>>", "text": "comment/review body (comments, reviews)"},
       "threading": "'Pull request opened' is a top-level parent; comments, reviews and merge/close events are replies with thread_ts = that parent (merge posted as thread_broadcast); 'N new commit(s) pushed to `branch`' is top-level",
       "logins": "real GitHub logins (arthur.blake, owen.baker) - the GitHub export uses tokens (EMPLOYEE_0025_GITHUB_USERNAME)", "per_kind": gh_kinds,
       "org_redacted_copies": sm["org_redacted_copies"]},
      {"per_repo": sm["per_repo"], "comment_and_review_copy_rates": GH["comment_mirror_rates"], "not_mirrored": [r for r, v in sm["per_repo"].items() if not v["mirror_window"]]},
      "A seeded PR comment/review/merge in GameOfDominoes or game-of-dominoes-backend (to 2025-12-26) or match3d (2025-06-30..2025-10-24) needs its Slack copy, threaded under the PR's 'opened' parent, using the real login. Repos outside that list/window must NOT get a mirror. COMMENTED reviews on GameOfDominoes are mirrored only ~17% of the time.",
      ["slack:C050WGU41HR:1738798578.389259", "slack:C050WGU41HR:1739210677.768059", "slack:C093LEZGF6J:1756761203.851799"],
      window={r: v["mirror_window"] for r, v in sm["per_repo"].items() if v["mirror_window"]})
    I("INT-02", "github", "slack", "GitHub app push notifications (top-level, not threaded)", {"pretext": "<N new commit(s)> pushed to `<develop|master|main>` by <login>", "per_kind": {k: v for k, v in gh_kinds.items() if "pushed" in k}},
      {"messages": sum(v["messages"] for k, v in gh_kinds.items() if "pushed" in k)}, "Seed only for the mirrored repos/branches; one message per push.", [v["example_id"] for k, v in gh_kinds.items() if "pushed" in k][:2])
    lb = J["linear_bot_prs"]
    I("INT-03", "linear", "github", "Linear GitHub integration: linear[bot] comment on PRs whose title/branch names a Linear key",
      {"author_login (pull_request_comments)": "PERSON_6028_GITHUB_USERNAME (type Organization)", "timeline actor_login": "SVC_0323_GITHUB_USERNAME", "body": "<details><summary><a href=\"https://linear.app/harmonygames-games/issue/<KEY>/<slug>\"><KEY> <title></a></summary>...", "slack_mirror": "'Comment on pull request by linear[bot]' with text '<https://linear.app/...|KEY title>'"},
      {"linear_bot_comments": J["linear_bot_comments"], "prs_with_linear_bot_comment": len(lb), "prs_with_linear_key": GH["prs_with_linear_key"], "share_of_keyed_prs": round(len(set(lb) & set(GH["pr_linear_keys"])) / max(1, GH["prs_with_linear_key"]), 3)},
      "A seeded PR that names a Linear key in an era/repo where linear[bot] commented should usually carry the bot comment (+ its 'commented' timeline event with actor SVC_0323, + Slack mirror if the repo is mirrored). Linear issues' links_json stays empty.",
      ["github:" + x for x in lb[:3]])
    la = si.get("linear_app", {})
    I("INT-04", "linear", "slack", "Linear Slack app: personal DM notifications (D05MBMJDAKV) and team-channel posts (#god-bugs, #zombie-match3d)",
      {"user": "SLACK_BOT_0007_SLACK_ID", "attachments[0]": {"color": "#5e6ad2", "fallback": "[PERSON_NAME_n] - changed status to Done for ENG-291 <title>", "blocks": "mrkdwn '*<person>* changed status to *Done* for <https://linear.app/harmonygames-games/issue/ENG-291/...|ENG-291 Title>'"}, "plain_text_variant": "'<person> commented on ENG-290 <title>'"},
      {"messages": la.get("n"), "window": [ts_to_dt(float(la["first"])).date().isoformat(), ts_to_dt(float(la["last"])).date().isoformat()] if la.get("first") else None, "channels": la.get("channels"), "actions": la.get("detail"), "monthly": la.get("monthly")},
      "Not every Linear transition is posted (DM feed is one subscriber's view); a seeded Linear state change does not require a Slack notice, but a seeded notice must match the issue's state/time.", la.get("samples", [])[:3])
    lm = collections.Counter(x[0] for x in GM["linear_mails"])
    I("INT-05", "linear", "gmail", "Linear e-mail: 'N unread notifications on <workspace>' digests, 'linear auto-closed <KEY>' notices, login/invite mails (sender svc_0251/svc_0257)",
      {"subject_patterns": dict(lm.most_common(8))}, {"mails": len(GM["linear_mails"]), "auto_close_mails": sum(1 for x in GM["linear_mails"] if "auto-closed" in x[0]), "auto_close_state_conflicts": 0},
      "Digest mails are aggregate; a seeded Linear comment does not need a mail. Auto-close mails all match Canceled issues (0 conflicts).", [x[4] for x in GM["linear_mails"][:3]])
    jb = S["jenkins_builds"]
    jobs = collections.defaultdict(lambda: {"msgs": 0, "builds": set(), "status": collections.Counter(), "first": None, "last": None})
    for ts, job, num, stt in jb:
        j = jobs[job]
        j["msgs"] += 1
        j["builds"].add(num)
        j["status"][stt] += 1
        j["first"] = ts if j["first"] is None or float(ts) < float(j["first"]) else j["first"]
        j["last"] = ts if j["last"] is None or float(ts) > float(j["last"]) else j["last"]
    started = collections.defaultdict(set)
    finished = collections.defaultdict(set)
    for ts, job, num, stt in jb:
        (started if stt == "started" else finished)[job].add(num)
    job_out = {k: {"messages": v["msgs"], "builds": len(v["builds"]), "status": dict(v["status"]), "first": ts_to_dt(float(v["first"])).date().isoformat(), "last": ts_to_dt(float(v["last"])).date().isoformat(),
                   "started_with_result_share": round(len(started[k] & finished[k]) / max(1, len(started[k])), 3)} for k, v in sorted(jobs.items(), key=lambda kv: -kv[1]["msgs"]) if v["msgs"] >= 30}
    I("INT-06", "jenkins", "slack", "Jenkins -> #builds (C05433XK267): job start/result posts + build-script posts",
      {"job_post": {"user": "SLACK_BOT_0005_SLACK_ID or null with subtype bot_message", "attachments[0].fallback": "<Job> - #<n> Started by changes from <person> (<k> file(s) changed) (<http://blake.tplinkdns.com:9009/job/...|Open>)", "result": "<Job> - #<n> - <branch> Success|Failure|Unknown after <t> (<...|Open>)", "colors": "2eb886 success / others"},
       "build_script_post": {"subtype": "bot_message", "text": "Android Build <n> Notes: QA Build | Android Build Size <n> MB | Build Errors:"}},
      {"jobs": job_out, "status_totals": si.get("jenkins", {}).get("detail"), "build_script_kinds": si.get("jenkins_buildscript", {}).get("detail"), "window": [ts_to_dt(float(si["jenkins"]["first"])).date().isoformat(), ts_to_dt(float(si["jenkins"]["last"])).date().isoformat()]},
      "A seeded 'build N shipped/failed' fact needs the Started + result pair for that job/number; builds continue to 2026-02-12 (Combo Fighter).", si.get("jenkins", {}).get("samples", [])[:3])
    dist = collections.defaultdict(lambda: {"n": 0, "first": None, "last": None, "mailboxes": collections.Counter()})
    for app, plat, ver, b, mb, d, rid in GM["distribution_mails"]:
        x = dist[app]
        x["n"] += 1
        x["mailboxes"][mb] += 1
        if d:
            x["first"] = d[:10] if not x["first"] or d[:10] < x["first"] else x["first"]
            x["last"] = d[:10] if not x["last"] or d[:10] > x["last"] else x["last"]
    tfc = collections.defaultdict(lambda: {"n": 0, "builds": set(), "first": None, "last": None})
    for app, ver, b, mb, d, rid in GM["testflight_mails"]:
        x = tfc[app]
        x["n"] += 1
        x["builds"].add((ver, b))
        if d:
            x["first"] = d[:10] if not x["first"] or d[:10] < x["first"] else x["first"]
            x["last"] = d[:10] if not x["last"] or d[:10] > x["last"] else x["last"]
    I("INT-07", "firebase_app_distribution", "gmail", "Firebase App Distribution tester mails 'Version X (N) of <App> for Android|iOS Available' (svc_0107), one per tester mailbox",
      {"subject": "Version <semver> (<build>) of <App name> for <Android|iOS> Available", "app_names": sorted(dist)},
      {"per_app": {k: {"mails": v["n"], "first": v["first"], "last": v["last"], "mailboxes": len(v["mailboxes"])} for k, v in sorted(dist.items(), key=lambda kv: -kv[1]["n"])}, "total": len(GM["distribution_mails"])},
      "Fan-out: every distribution is copied to each tester mailbox; a seeded build must appear in all tester mailboxes of that era or none.", [x[6] for x in GM["distribution_mails"][:2]])
    I("INT-08", "testflight/app_store_connect", "gmail", "TestFlight 'is now available to test' + App Store Connect status/review mails (svc_4131)",
      {"subjects": ["<App> <ver> (<build>) for iOS is now available to test.", "The status of your (iOS) app, <App>, is now \"<State>\"", "Review of your <App> (iOS) submission is complete.", "App Store Connect: Version <v> (<b>) for <App> has completed processing."]},
      {"testflight_per_app": {k: {"mails": v["n"], "distinct_builds": len(v["builds"]), "first": v["first"], "last": v["last"]} for k, v in tfc.items()}, "appstore_mails": len(GM["appstore_mails"])},
      "Release/launch claims should be backed by these mails; the app names drift (see trap K02).", [x[5] for x in GM["testflight_mails"][:2]])
    hm = collections.Counter((x[4] or "")[:7] for x in GM["helpshift_mails"] if not x[5])
    zap = si.get("zapier_helpshift", {})
    I("INT-09", "helpshift", "gmail+slack", "Helpshift issue notifications by mail (svc_0143 -> SVC_0293_EMAIL, Leonard, Arthur) and via Zapier into #issuefeed (C083AEP6NBA)",
      {"gmail": "Subject 'New Domino Delights <iOS|Android> issue #<n> from' / 'replied to Domino Delights iOS issue #<n>'; body 'View and respond to this issue here … Please do not reply'", "slack": "subtype bot_message, user null, text '#ZapierBot: New Issue has arrived. author: <profile>; Message: <text>' (often empty)"},
      {"gmail_new_issue_mails_by_month": dict(sorted(hm.items())), "distinct_issue_numbers": len(set((x[0], x[1], x[2]) for x in GM["helpshift_mails"])), "zapier_posts": zap.get("n"), "zapier_by_kind": zap.get("detail"), "zapier_monthly": zap.get("monthly")},
      "Mail is the issue-of-record; Zapier posts carry no issue number, so a seeded Helpshift issue needs the mail fan-out (SVC_0293 + Leonard + Arthur copies) and optionally a Zapier post.", zap.get("samples", [])[:2] + [x[6] for x in GM["helpshift_mails"][:2]])
    cm = collections.Counter(x[1] for x in GM["crash_mails"])
    I("INT-10", "crashlytics", "gmail", "Firebase Crashlytics 'Trending stability issues for <date> - <platform> <bundle>' daily digests (svc_2398)",
      {"subject": "Trending stability issues for <M-D-YYYY> - <Android|iOS> <bundle id (often redacted)>"}, {"mails": len(GM["crash_mails"]), "by_mailbox": dict(cm.most_common(12))},
      "Daily per-platform digest fanned out to engineers; heavy redaction (Scenario_Atlas: weak cohort).", [x[3] for x in GM["crash_mails"][:2]])
    inv = J["invites"]
    calk = collections.Counter(x[0] for x in GM["calendar_mails"])
    I("INT-11", "gcal", "gmail", "Google Calendar invitation / update / RSVP / cancellation mails",
      {"subjects": {"Invitation": "Invitation: <summary> @ <Ddd Mon D, YYYY h:mmam - h:mmam (TZ)> (<recipient>)", "Updated invitation": "Updated invitation: <summary> @ <when or 'Weekly from …'>", "Accepted": "Accepted: <summary> @ <when> (<recipient>)"},
       "message_id": "<calendar-<uuid>@google.com>"},
      {"by_kind": dict(calk), "dated_invites": inv["dated"], "dated_invites_matching_gcal_instance": inv["matched"], "match_rate": round(inv["matched"] / max(1, inv["dated"]), 3)},
      "Invites and calendars only partly agree (R08). A seeded meeting does not need an invitation mail (most base meetings have none in the persona's mailbox), but a seeded invitation mail should have its GCal rows.", [x[5] for x in GM["calendar_mails"][:2]])
    ghm = collections.Counter(x[0] for x in GM["github_mails"])
    I("INT-12", "github", "gmail", "GitHub notification mails (svc_0248) '[harmonygames-Games/<repo>] <title> (PR #N)'",
      {"subject": "[harmonygames-Games/<repo>] <PR title> (PR #<n>) (org sometimes redacted)", "body_first_line": "'@<login> approved this pull request.' / '<person> requested your review on: …' / '<person> pushed N commits'", "message_id": "<harmonygames-Games/<repo>/pull/<n>/…@github.com>"},
      {"mails_by_repo": dict(ghm.most_common()), "mails_for_prs_absent_from_export": "see coherence_hazards R03"}, "Optional companion; per-recipient mailbox copies.", [x[6] for x in GM["github_mails"][:2]])
    for iid, key, name, note in (("INT-13", "google_drive_app", "Google Drive Slack app DMs (comments, access requests, shares)", "DM-only; seeded doc comments need not have one."),
                                 ("INT-14", "standup_bot", "Standup bot DMs ('Hey! Are you ready to fill out…', 'What are you planning to work on…')", "Active 2023-07..2024-04 only."),
                                 ("INT-15", "qa_monkey_bot", "QA 'monkey' level-test bot in #[ORG]-monkey (Starting bot … Level N, ChN LvlN :white_check_mark:, Error: …)", "Automated QA noise."),
                                 ("INT-16", "harmony_gpt_bot", "HarmonyGPT bot (#[ORG]-gpt): autoupdater/redeploy messages", "Noise."),
                                 ("INT-17", "slack_connect_notice", "Slack Connect join/leave notices ('*Griffingp* has joined this channel by invitation from *Harmony Games*')", "External-member churn signal."),
                                 ("INT-18", "metabase_app", "Metabase chart images in #metabase-data", "13 posts in 2023."),
                                 ("INT-19", "cursor_app", "Cursor background-agent DMs", "2025-08 only."),
                                 ("INT-20", "github_app_legacy_text", "Early GitHub-app text posts in #engineering-bots ('Subscribed to …', '[no preview available]')", "2023 only.")):
        v = si.get(key, {})
        src = {"google_drive_app": "google_drive", "standup_bot": "standup_bot", "qa_monkey_bot": "qa_monkey_bot", "harmony_gpt_bot": "harmony_gpt", "slack_connect_notice": "slack_connect", "metabase_app": "metabase", "cursor_app": "cursor", "github_app_legacy_text": "github"}[key]
        I(iid, src, "slack", name, {"user": "see samples", "channels": v.get("channels")},
          {"messages": v.get("n"), "window": [ts_to_dt(float(v["first"])).date().isoformat(), ts_to_dt(float(v["last"])).date().isoformat()] if v.get("first") else None, "monthly_peak": max((v.get("monthly") or {"-": 0}).items(), key=lambda kv: kv[1])}, note, v.get("samples", [])[:3])
    I("INT-21", "trello", "slack", "Trello -> Slack: NO integration exists (no Trello bot posts)", {"human_pasted_trello_links": S["trello_links"]}, {"trello_bot_messages": 0},
      "Do not seed Trello bot notifications in Slack; a human may paste a trello.com/c/<shortLink> URL (shortLink is null on every card).", [])
    I("INT-22", "slack", "gmail", "Slack e-mail notifications (svc_0240): '[Slack] <person> sent you a message', 'You've got N unread messages'",
      {"subjects": [p["pattern"] for p in GM["subject_patterns"] if p["sender"] == "svc_0240_email"][:5]}, {"mails": sum(p["n"] for p in GM["subject_patterns"] if p["sender"] == "svc_0240_email")}, "Optional; never load-bearing.", [p["example"] for p in GM["subject_patterns"] if p["sender"] == "svc_0240_email"][:2])
    I("INT-23", "coderabbit", "github(+slack)", "CodeRabbit reviews and comments (PERSON_6026_GITHUB_USERNAME, type Organization; timeline actor SVC_0321)",
      {"pr_body": "auto-inserted '<!-- This is an auto-generated comment: release notes by coderabbit.ai --> ## Summary by CodeRabbit'", "comments": "walkthrough / 'Review skipped: Draft detected'", "review_comments": "'_⚠️ Potential issue_ | _🔴 Critical_' with analysis chains"},
      {"pr_comments": J["coderabbit"][0], "review_comments": J["coderabbit"][1], "reviews": J["coderabbit"][2], "pr_bodies_with_summary": GH["conventions"]["pr_body_has_coderabbit_summary"]},
      "CodeRabbit was cancelled 2026-02-12 22:50Z (Scenario_Atlas); no CodeRabbit activity should be seeded after that. Mirrored to Slack like any comment in mirrored repos.", [])
    out = {"_meta": {"generated_by": "Task_Authoring/references/universe_kb/_build/assemble_integrations_conventions.py",
                     "use": "Every automated mirror/integration with its exact shape and base rate, so a seeded record carries its required companions (and only in the windows where they existed)."},
           "integrations": ints, "gmail_samples": gmail_samples(), "index": [{"id": i["id"], "name": i["name"], "source": i["source"], "destination": i["destination"]} for i in ints]}
    jdump(out, OUT + "/integrations.json", indent=1)

    # ================= CONVENTIONS =================
    chans = {c["id"]: c for c in jload(SLACK + "/channels.json")}
    def ctype(c):
        return "im" if c.get("is_im") else ("mpim" if c.get("is_mpim") else ("private" if c.get("is_private") else "public"))
    tl = S["type_len_q"]
    marks = {k: {m: round(v.get(m, 0) / v["n"], 3) for m in ("lower_start", "all_lower", "ends_punct", "emoji", "question", "mention", "url", "multiline")} for k, v in S["type_marks"].items()}
    ex = {}
    pick = {"public": ["C080X4GTZ0E", "C05KNDCHAAG"], "private": ["C07C2866011", "C0880U9751A", "C09UHHN6PFZ"], "mpim": [c for c in chans if chans[c].get("is_mpim")], "im": [c for c in chans if chans[c].get("is_im")]}
    for t, cids in pick.items():
        lo_, hi_ = tl[t]["p25"], tl[t]["p75"]
        got = []
        for cid in cids:
            d = SLACK + "/messages/" + cid
            if not os.path.isdir(d):
                continue
            for fn in sorted(os.listdir(d), reverse=True)[:3]:
                for x in jload(d + "/" + fn):
                    tx = x.get("text") or ""
                    if not x.get("subtype") and not x.get("bot_id") and lo_ <= len(tx) <= hi_ and "<@" not in tx and "[PERSON" not in tx and (x.get("user") or "").startswith("EMPLOYEE"):
                        got.append({"id": "slack:%s:%s" % (cid, x["ts"]), "user": x.get("user"), "len": len(tx), "text": tx})
                        if len(got) >= 4:
                            break
                if len(got) >= 4:
                    break
            if len(got) >= 4:
                break
        ex[t] = got
    top_ch = sorted(S["chan_len_q"].items(), key=lambda kv: -kv[1]["n"])[:25]
    persona_hours = {}
    for em, v in A["people"].items():
        s = v["services"].get("slack") or {}
        g = v["services"].get("gcal") or {}
        if not s.get("hours_utc") or not s.get("messages") or s["messages"] < 200:
            continue
        tz = g.get("calendar_tz")
        loc = tz_shift(s["hours_utc"], tz)
        wd = s.get("weekday_pt") or [0] * 7
        persona_hours[em] = {"calendar_tz": tz, "slack_core_80pct_window_local": core_window(loc), "slack_core_80pct_window_utc": core_window(s["hours_utc"]),
                             "weekend_share": round((wd[5] + wd[6]) / max(1, sum(wd)), 3), "style": s.get("style"), "messages": s["messages"]}
    gl = GM
    conv = {
        "_meta": {"generated_by": "Task_Authoring/references/universe_kb/_build/assemble_integrations_conventions.py", "use": "Writing and id conventions for realistic seeding: length/tone distributions, timestamp habits, title/label/state vocabularies, branch and commit style. Quantiles are over the whole base unless stated."},
        "slack": {
            "length_chars_by_channel_type": tl, "tone_markers_share_by_channel_type": marks,
            "examples_near_median_by_type": ex,
            "busiest_channels_length": {chans.get(k, {}).get("name") or k: v for k, v in top_ch},
            "ids": {"message_id": "sha256(channel_id + '|' + ts)[:32] (holds except 18 base rows)", "ts": "string, 6 decimals, unique per channel", "channel_ids": "C… public/private, D… IM, mpdm 'C' + 11 hex; 'FC:<file id>:<title>' canvas pseudo-channels", "user_ids": "EMPLOYEE_00NN_SLACK_ID / PERSON_NNNN_SLACK_ID / U…; every profile timezone is America/Los_Angeles"},
            "thread_conventions": {"parents_with_replies": S["thread"]["parents_with_replies"], "note": "replies carry thread_ts = parent ts; parent reply_count/reply_users_count/latest_reply must be updated together; 'thread_broadcast' subtype for replies also sent to channel"},
            "per_person_hours_and_style": persona_hours,
            "bot_shapes": "see integrations.json",
        },
        "gmail": {"internal_new_text_len_chars": gl["internal_new_text_len_all"], "internal_subject_len_chars": gl["internal_subject_len"],
                  "internal_markers_share": {k: round(v / gl["internal_marks"]["n"], 3) for k, v in gl["internal_marks"].items() if k != "n"},
                  "internal_sent_messages": gl["internal_marks"]["n"], "per_sender_new_text_len": gl["internal_new_text_len"],
                  "thread_size_dist": gl["thread_size_dist"], "date_formats": gl["date_formats"],
                  "line_endings": "bodies use \\r\\n; replies quote history with '>' after 'On <date> <name> <addr> wrote:'",
                  "ids": {"message": "<mailbox>/<RFC Message-ID incl. <>>", "thread": "<mailbox>/<19-digit X-GM-THRID>", "files": "NNNNNNNN.json (robert + token mailboxes) or <alias>@harmonygames.co_<thrid>.json"},
                  "subject_patterns_top": gl["subject_patterns"][:120]},
        "linear": {"states_by_team": LI["team_states"], "labels_by_team_top": LI["team_labels"], "label_vocab_size": LI["team_label_vocab_size"],
                   "title_prefixes_by_team": LI["title_prefixes"], "description_len_chars": LI["desc_len"], "priority_by_team": LI["priority"], "max_number": LI["max_number"],
                   "release_codenames": "Django, Rebirth (June), Baklava (August), Desire (September - Beta Launch), Lava/Desire Lava Fix (Mid October), Nova, Destiny, Avengers (January), Cappadocia (February), Cookie, Pupusa, Grogu, Cheesecake (July), Elon (December 21st - last release of 2025); sprint labels 'Sprint <n> - <Month Dth>' / 'Sprint 30 Cappadocia -  Feb 28th' (double space)",
                   "ids": "id = identifier = <TEAM>-<n>; timestamps varchar ISO-Z; users usr_<16hex> except usr_Robert, usr_Lucas, 'usr_Victor Barnes', usr_EMPLOYEE_0024 …"},
        "github": GH["conventions"],
        "trello": {"card_name_patterns": O["trello"]["card_name_patterns"], "labels": O["trello"]["labels"], "desc_len": O["trello"]["desc_len"],
                   "lists": {k: "%s / %s (open %d, closed %d)" % (v["board"], v["name"], v["open"], v["closed"]) for k, v in O["trello"]["lists"].items()},
                   "action_types": O["trello"]["action_types"], "ids": "24-hex ObjectId; first 8 hex = unix seconds of creation"},
        "gcal": {**O["gcal"]["conventions"], "ids": {"event_id": "evt_<22hex>", "ical_uid": "<32hex>@hg4", "hangout_link": "https://meet.google.com/<xxx-xxxx-xxx>?hs=224"},
                 "calendar_timezones": {k: v["tz"] for k, v in O["gcal"]["calendars"].items()}, "recurring_series": O["gcal"]["series_with_rrule"]},
        "docs_sheets_slides_drive": {
            "doc_title_families_top": dict(collections.Counter((re.sub(r"\d+", "N", r[1] or "")[:40]) for r in O["native"]["docs"]["rows"]).most_common(25)),
            "doc_body_len_chars": quantiles([r[4] for r in O["native"]["docs"]["rows"]]),
            "sheet_title_families_top": dict(collections.Counter((re.sub(r"\d+", "N", r[1] or "")[:40]) for r in O["native"]["sheets"]["rows"]).most_common(20)),
            "sheet_tabs_per_file": quantiles([r[4] for r in O["native"]["sheets"]["rows"]]),
            "sheet_declared_vs_nonempty_rows": quantiles([t[1] - (t[2] or 0) for r in O["native"]["sheets"]["rows"] for t in r[5] if t[1] is not None]),
            "slides_title_families_top": dict(collections.Counter(norm_title(r[1]) for r in O["native"]["slides"]["rows"]).most_common(15)),
            "slides_pages_per_deck": quantiles([r[4] for r in O["native"]["slides"]["rows"]]),
            "drive_mime_top": O["drive"]["mime"], "drive_visibility": O["drive"]["visibility"],
            "ids": "files f_<22hex>, folders d_<22hex>; Docs/Sheets/Slides id == drive file id; Drive name keeps source extension (.docx/.xlsx/.html), native title does not"},
        "confluence": {"words_per_page": O["confluence"]["words"], "labels": O["confluence"]["labels"],
                       "version_messages_examples": {pid: p["version_messages"] for pid, p in O["confluence"]["pages"].items() if p["version_messages"]},
                       "ids": "page_<slug>, ver_<32hex> or ver_<slug>_vN, comment_<page>_cN, label_lNNN, att_aNN, user_EMPLOYEE_00NN / user_STAFF_N"},
        "snowflake": {"tables": {k: {"rows": v.get("rows"), "columns": v.get("columns"), "comment": (v.get("comment") or "")[:300]} for k, v in O["snowflake"]["tables"].items()},
                      "row_ids": "EVT-0001, REV-0000001, TXN-00000001, PLR-00096000, FIN-000001, ROSTER-0001, PUSH-0000001, INS-0000001", "columns": "UPPERCASE in the live DB (quote them); export rows use lowercase keys"},
        "contacts": {"id_formats": O["contacts"]["id_formats"], "tokenized_emails": O["contacts"]["tokenized_emails"], "with_job": len(O["contacts"]["with_job"])},
    }
    jdump(conv, OUT + "/conventions.json", indent=1)
    print("integrations", len(ints), "conventions ok")


if __name__ == "__main__":
    main()
