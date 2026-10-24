"""timeline.json: dated event spine 2024 -> 2026-02-14. Every evidence id is re-verified against the base
(and its own timestamp read back); events keep only verified evidence and must span 2+ services.
Also appends the 2024+ storyline beats whose artifacts verify in 2+ services."""
import os, re, json, subprocess, collections, datetime
from common import *
from pass_beats import Verifier

EVENTS = [
    # date, category, title, evidence
    ("2024-06-07", "launch/build", "Quest system build starts: #quests channel opened; liveops repo's first PR sets up the AWS stack for quests",
     ["slack:C076Q0Z5R47:1717779767.518909", "github:harmonygames-Games/liveops#1"]),
    ("2024-08-02", "launch/build", "Leaderboards work starts (#leaderboards with the WIP spec)",
     ["slack:C07F4G84XV4:1722627602.447869", "linear:ENG-1149", "linear:ENG-1211"]),
    ("2024-12-17", "release", "Leaderboards go live: PR merge cluster (GameOfDominoes#1557-#1587) under epic ENG-1874",
     ["github:harmonygames-Games/GameOfDominoes#1557", "github:harmonygames-Games/GameOfDominoes#1587", "linear:ENG-1874", "slack:C07F4G84XV4:1732599706.878669"]),
    ("2024-09-05", "vendor/ua", "UA/BD Trello board created; Adjoe partner channel follows (Oct 31)",
     ["trello:66da196af476ab78deaa0d28", "slack:C07UCC631A6:1730400492.677439"]),
    ("2024-10-03", "release", "iOS beta pipeline switches to TestFlight for Domino Delights (first TestFlight build mail); Jenkins jobs renamed 'DD Android'/'DD iOS' (from 'Game Of Dominoes … Freestyle'); Firebase distribution renames the app '[ORG] DD' / 'Harmony Games DD'",
     ["@gmail:testflight_first:Domino Delights", "@gmail:dist_first:[SOURCE_ORG_0001] DD Android", "@jenkins_first:DD Android", "@jenkins_first:DD iOS"]),
    ("2024-10-19", "launch/build", "Backend built from scratch: game-of-dominoes-backend's first PR",
     ["github:harmonygames-Games/game-of-dominoes-backend#1", "@slack_mirror_first:game-of-dominoes-backend"]),
    ("2024-11-14", "vendor", "Helpshift adopted: Unity SDK PR, vendor kick-off meeting, first issue mails, #issuefeed (Zapier) opened",
     ["github:harmonygames-Games/GameOfDominoes#1452", "gcal:evt_12f117ae13fc18ca6592a4", "slack:C083AEP6NBA:1732675841.995199", "@gmail:helpshift_first"]),
    ("2024-11-15", "outage", "Quest outage: quests not populating; #live-incidents created; ENG-1892 filed and closed 18 Nov; quest fixes merged; warehouse marks Weekly Quests EVT-0024 failed; postmortem written (broken again on TestFlight 0.68, 19 Nov)",
     ["slack:C080X4GTZ0E:1731696783.951159", "linear:ENG-1892", "github:harmonygames-Games/GameOfDominoes#1458", "snowflake:LIVE_EVENT_PERFORMANCE/EVT-0024", "confluence:page_quest_postmortem", "slack:C080X4GTZ0E:1732005140.008099"]),
    ("2024-12-02", "decision", "Player-compensation dashboard ticketed (ENG-1972; later cancelled 2025-05-05, follow-up ENG-2275 stays Todo)",
     ["linear:ENG-1972", "linear:ENG-2275", "@beat:compensation"]),
    ("2025-01-10", "launch/build", "Zombie Match 3D development starts: match3d repo first PR, #zombie-match3d active, Firebase distribution 'Match 3D'",
     ["github:harmonygames-Games/match3d#1", "slack:C0880U9751A:1736428347.851289", "@gmail:dist_first:Match 3D Android"]),
    ("2025-01-31", "launch/build", "Season Pass (Domino Delights) kicked off in #season-pass; first Season Pass ships on Domino Delights as a dry run (~7 Mar)",
     ["slack:C08BVMXHGD6:1738333556.113279", "linear:ENG-2136", "linear:ART-767", "trello:65eb55497eac80d87326c811", "slack:C08BVMXHGD6:1742396785.898069"]),
    ("2025-03-30", "funding", "Crownfall Web3/4X pivot pitch drafted overnight (asks ~$2M for phase 1)",
     ["drive:f_88458fbacd300f081d044c", "slack:D04UC0UEN2V:1743405065.141559"]),
    ("2025-04-11", "release", "Zombie Match 3D alpha ships (Apr 11); beta gated on KPI validation",
     ["slack:C07C2866011:1744565232.971959", "trello:67cb250fde144c0c37fcf5ad", "trello:67bdf3d8722c229e32622f50"]),
    ("2025-04-18", "decision", "Domino Delights silences interstitial ads for high-LTV players (LTV-based interstitial removal)",
     ["trello:680287617cf86bf6f358fb54", "linear:ENG-2292", "github:harmonygames-Games/GameOfDominoes#1794"]),
    ("2025-03-06", "launch/build", "Difficulty optimisation and DD economy v2 working groups open (#difficulty-optimization, #dd_economy_v2)",
     ["slack:C08GLSV8Z7W:1741281439.632889", "slack:C08HHAA4ZUK:1741808226.197339", "linear:ENG-2215"]),
    ("2025-03-21", "release", "Zombie game iOS builds ship to TestFlight as 'Puzzles vs Zombies' (renamed Zombie Match 3D from 2025-07-24)",
     ["@gmail:testflight_first:Puzzles vs Zombies", "@gmail:testflight_first:Zombie Match 3D", "@jenkins_first:Match 3D iOS Submission"]),
    ("2025-04-18", "org", "ZOM Linear team created for Zombie Match 3D work (ENG-#### and ZOM-### become separate series)",
     ["@linear_team:team_ZOM", "@linear_first:ZOM", "@first_pr_with:ZOM"]),
    ("2025-05-15", "outage", "Domino Delights client-crash window (10-16 May): crash reports in #live-incidents; 243 incident-related store reviews in May",
     ["slack:C080X4GTZ0E:1747368127.636349", "snowflake:APP_STORE_REVIEWS"]),
    ("2025-06-17", "launch/build", "ZM ROADMAP Trello board created; GitHub app subscribed in #zombie-prs (30 Jun)",
     ["trello:6851a6569f3bf818760632d7", "slack:C093LEZGF6J:1751317160.968219"]),
    ("2025-06-29", "outage", "Weekend event-scheduler stall (29 Jun), recurring 11-12 Jul (River Rush, Streak Rush, Axe Arena down); manual lives grants by Douglas 14-24 Jul; warehouse rows still 'completed'",
     ["slack:C080X4GTZ0E:1751200739.524289", "slack:C080X4GTZ0E:1752357557.890929", "slack:C080X4GTZ0E:1752463834.941969", "snowflake:LIVE_EVENT_PERFORMANCE/EVT-0324"]),
    ("2025-07-16", "board/funding", "Q3 board meeting (~$365K cash, 5 months runway; downsizing options); #bridge-pitch opened 20 Jul",
     ["gcal:evt_771fc850b4096bad7ea8b2", "drive:f_7793bb93e59e9c0dee5129", "slack:C096HFA5Z8W:1752978167.673569", "snowflake:CASH_BALANCE/2025-07-31"]),
    ("2025-09-03", "funding", "$2.5M bridge outreach begins (rejections follow: A16Z Speedrun 1 Oct)",
     ["gmail:leonard@harmonygames.co_1842219327413774622.json", "slack:C07C2866011:1756749288.785249", "slack:C07C2866011:1759288987.503349"]),
    ("2025-09-15", "release", "Season Pass merged into Zombie Match 3D (match3d#438)",
     ["github:harmonygames-Games/match3d#438", "@slack_mirror_pr:match3d#438"]),
    ("2025-10-10", "launch/build", "Telegram Domino Delights mini-app effort (#telegram-dd; ENG-2377 master ticket)",
     ["slack:C09KU8U4DPF:1760124801.362399", "linear:ENG-2377"]),
    ("2025-10-14", "board/funding", "Q4 board meeting (Oct 14)",
     ["gcal:evt_4ee450f276f468e9ce95cf", "drive:f_d03044b385b94f24b21ff4"]),
    ("2025-10-24", "layoffs", "Layoffs effective Oct 24: marketing eliminated (Frederick), contractors terminated in Carta/Deel; two 'All Hands' that day; payroll roster lines end 2025-10-31; Samuel, Calvin and Frederick go quiet",
     ["slack:C04UEQVDVB7:1761844344.664939", "gmail:leonard@harmonygames.co_1847333347700620793.json", "gcal:evt_0a0658fbb9bbebae7f962a", "gcal:evt_11530fad245bf030e8563b", "snowflake:PAYROLL_ROSTER"]),
    ("2025-10-31", "bd", "Mattel Barbie 'Dream Life Glow' pitch: #mattel_proposal opened (RFP thread Sep 4 - Dec 2)",
     ["slack:C09QDMC3UL9:1761931237.686129", "gmail:leonard@harmonygames.co_1842359642190933488.json", "gcal:evt_048b618ca76c5c85c7b98f"]),
    ("2025-11-02", "outage", "Lives not generating for real players (ENG-2400 filed, still open at the clock)",
     ["linear:ENG-2400", "slack:C080X4GTZ0E:1762088965.657729"]),
    ("2025-11-02", "bd", "Domino Delights web port: #dd-road-to-sub-250mb (CrazyGames 'exclusive launch period' claim 5 Nov), Core Game UI Optimization ticket, WebGL fixes merged",
     ["slack:C09Q4S613CN:1762041270.058379", "slack:C09Q4S613CN:1762361357.317589", "linear:ENG-2403", "github:harmonygames-Games/GameOfDominoes#1891"]),
    ("2025-11-07", "org", "Planning tools go quiet: last Linear issue created 2025-11-07; Trello boards' last activity 2025-11-13",
     ["@linear_last_created", "@trello_last_activity"]),
    ("2025-11-12", "launch/build", "Combo Fighter kick-off (meeting on 9 calendars); #prototype opens 24 Nov; Combo-Fighters repo's first PR 2 Dec; first TestFlight build 21 Dec",
     ["gcal:evt_0c030e6eb00183a70d9267", "slack:C09UHHN6PFZ:1764008272.638909", "github:harmonygames-Games/Combo-Fighters#1", "@gmail:testflight_first:Combo Fighter"]),
    ("2025-11-17", "bd", "BoomBit Slack Connect publishing channel active (Brazil creative test Jan 2026 converts 1-2%)",
     ["slack:C09SWTHEMEW:1763408929.876899", "slack:C09SWTHEMEW:1769509283.414179", "gcal:evt_f07c2d5d56f5110a888cef"]),
    ("2025-12-03", "bd", "CrazyGames web licence signed (~Dec 3-5); backend Admin Endpoints & Store Catalog merged Dec 3",
     ["slack:C04UEQVDVB7:1764907519.899639", "gmail:leonard@harmonygames.co_1847443396264475348.json", "github:harmonygames-Games/game-of-dominoes-backend#79"]),
    ("2025-12-26", "tooling", "GitHub app stops mirroring to #engineering-bots (last mirror 2025-12-26); Combo-Fighters was never mirrored",
     ["@slack_mirror_last:GameOfDominoes", "github:harmonygames-Games/Combo-Fighters#16"]),
    ("2026-01-08", "funding", "'Options with Investors' meeting; Jan 12 cash $25K / card debt $6K / payroll $17K",
     ["gcal:evt_9a8faed31d5ef3d9b2dcab", "slack:C07C2866011:1768248003.017699", "snowflake:CASH_BALANCE/2026-01-31"]),
    ("2026-01-13", "release", "Combo Fighter monetisation: AppLovin MAX + rewarded ads merged (Jan 13), IAP merged (Jan 28); Meta UA spend Dec-Feb",
     ["github:harmonygames-Games/Combo-Fighters#24", "github:harmonygames-Games/Combo-Fighters#34", "snowflake:AD_SPEND_DAILY"]),
    ("2026-01-14", "board/funding", "Q1 board meeting (Jan 14); three drafts of the board email in #executives",
     ["gcal:evt_8cdcb12b7b4e1346db999d", "drive:f_65ada5e24989d256cabdfa", "slack:C07C2866011:1768265943.581399"]),
    ("2026-01-20", "release", "TestFlight builds of a new iOS title 'Trump Billionaires Club' (Jan 20 - Feb 13), after a Dec 10 #executives link about a Trump crypto video game",
     ["@gmail:testflight_first:Trump Billionaires Club", "slack:C07C2866011:1765384805.140929"]),
    ("2026-01-23", "funding", "Recapitalisation proposed to Griffin (cap-table reset vs shutdown); Reset Financing term sheet ($2.25M pre)",
     ["gmail:leonard@harmonygames.co_1855133803855213163.json", "drive:f_11040fe5d66821bd6951aa"]),
    ("2026-02-09", "wind-down", "Shutdown decided after Combo Fighter data: #winddown opened with the Shut_Down_List canvas; Sherwood 'wind-down support request' thread",
     ["slack:C0ADGSZKR3R:1770663250.160009", "gmail:leonard@harmonygames.co_1856688113228112603.json"]),
    ("2026-02-09", "vendor", "Vendor terminations: Helpshift and Singular (Feb 9), Unity (Feb 12); Singular past-due thread (overdue $6,250)",
     ["slack:C0ADGSZKR3R:1770673717.808759", "slack:C0ADGSZKR3R:1770674268.840059", "slack:C0ADGSZKR3R:1770932147.282819", "gmail:blake@harmonygames.co_1853470745439394465.json"]),
    ("2026-02-11", "wind-down", "Contractor termination letters sent; Google accounts to be archived after Feb 15; Sunset wind-down call; Gemini notes",
     ["gmail:00016873.json", "gmail:leonard@harmonygames.co_1856860994291529096.json", "slack:C05KNDCHAAG:1770839984.194409", "gcal:evt_212e50fb5a53ea8016ce29", "drive:f_0c37bb7235683d73569903"]),
    ("2026-02-12", "wind-down", "Wind-down and data agreements signed (Sunset, $11,700 fee; $22,500 data offer); Sherwood call; Arthur takes the 'data stuff'",
     ["slack:C0ADGSZKR3R:1770931777.561519", "slack:C0ADGSZKR3R:1770911000.728559", "snowflake:FINANCE_LEDGER/FIN-000702", "gcal:evt_4ebbd76539b6304ad37a74"]),
    ("2026-02-13", "wind-down", "Work continues after the announcement: Combo-Fighters#37 merged Feb 13; last Jenkins builds Feb 12; last TestFlight build Feb 13",
     ["github:harmonygames-Games/Combo-Fighters#37", "@jenkins_last", "@gmail:testflight_last:Trump Billionaires Club"]),
]

SNOW_KEYS = {"LIVE_EVENT_PERFORMANCE": "event_id", "FINANCE_LEDGER": "entry_id", "CASH_BALANCE": "month_end_date", "PAYROLL_ROSTER": "roster_line_id"}


def snow_rows():
    idx = jload(SNOW_IDX)["payload"]["data"]["nodes"]
    tabs = {int(n[0].split("/")[2]): (n[1], n[2]) for n in idx if n[0].startswith("/tables/") and n[0].count("/") == 2}
    rows = {}
    with open(SNOW, "rb") as fh:
        for i, (s, e) in tabs.items():
            if e - s > (2 << 20):
                continue
            fh.seek(s)
            t = json.loads(fh.read(e - s))
            if t["name"] in SNOW_KEYS:
                k = SNOW_KEYS[t["name"]]
                rows[t["name"]] = {str(r.get(k)): r for r in t["rows"]}
    return rows


def find_gmail_files(rfcs, mailboxes, alias_pairs):
    """map RFC message ids (with <>) -> thread file, using grep -F over the mailboxes' thread files (read-only). Cached."""
    cp = CACHE + "/kb_tl_gmail_files.json"
    cache = jload(cp) if os.path.exists(cp) else {}
    todo = [r for r in rfcs if r not in cache]
    if todo:
        alias = {a: b for a, b, n in alias_pairs}
        files = []
        for fn in os.listdir(GMAIL + "/threads"):
            if "@" in fn and "_" in fn:
                if alias.get(fn.split("_")[0]) in mailboxes:
                    files.append(fn)
            elif "robert@harmonygames.co" in mailboxes or any("@" not in m for m in mailboxes):
                files.append(fn)
        pf = CACHE + "/kb_tl_patterns.txt"
        with open(pf, "w") as f:
            f.write("\n".join(todo))
        out = []
        for i in range(0, len(files), 1500):
            chunk = [GMAIL + "/threads/" + x for x in files[i:i + 1500]]
            out += subprocess.run(["grep", "-l", "-F", "-f", pf] + chunk, capture_output=True, text=True).stdout.splitlines()
        for path in out:
            try:
                t = jload(path)
            except Exception:
                continue
            for m in t.get("messages") or []:
                r = (m.get("id") or "").split("/", 1)[-1]
                if r in todo and r not in cache:
                    cache[r] = os.path.basename(path)
        jdump(cache, cp)
    return {r: cache.get(r) for r in rfcs}


def main():
    V = Verifier()
    SR = snow_rows()
    S = jload(CACHE + "/kb_slack.json")
    GM = jload(CACHE + "/kb_gmail.json")
    LI = jload(CACHE + "/kb_linear.json")
    O = jload(CACHE + "/kb_other.json")
    B = jload(CACHE + "/kb_beats.json")
    # resolvers for @ tokens
    tf_first, tf_last, dist_first = {}, {}, {}
    for app, ver, b, mb, d, rid in GM["testflight_mails"]:
        if d and (app not in tf_first or d < tf_first[app][0]):
            tf_first[app] = (d, rid)
        if d and (app not in tf_last or d > tf_last[app][0]):
            tf_last[app] = (d, rid)
    for app, plat, ver, b, mb, d, rid in GM["distribution_mails"]:
        if d and (app not in dist_first or d < dist_first[app][0]):
            dist_first[app] = (d, rid)
    hs = sorted((x[4], x[6]) for x in GM["helpshift_mails"] if x[4])
    needed = {}
    for app, (d, rid) in list(tf_first.items()) + list(tf_last.items()) + list(dist_first.items()) + ([("hs", hs[0])] if hs else []):
        needed[rid.split("/", 1)[1]] = rid
    fmap = find_gmail_files(set(needed), set(v.split(":", 1)[1].split("/", 1)[0] for v in needed.values()), GM["alias_pairs"])
    def gfile(rid):
        f = fmap.get(rid.split("/", 1)[1])
        return "gmail:" + f if f else None
    mirror = S["gh_mirror"]
    def mirror_first(repo):
        c = [m for m in mirror if m[3] == repo]
        m = min(c, key=lambda m: float(m[1])) if c else None
        return "slack:%s:%s" % (m[0], m[1]) if m else None
    def mirror_last(repo):
        c = [m for m in mirror if m[3] == repo]
        m = max(c, key=lambda m: float(m[1])) if c else None
        return "slack:%s:%s" % (m[0], m[1]) if m else None
    def mirror_pr(spec):
        repo, n = spec.split("#")
        c = [m for m in mirror if m[3] == repo and m[4] == int(n) and "merged" in (m[5] or "").lower()] or [m for m in mirror if m[3] == repo and m[4] == int(n)]
        return "slack:%s:%s" % (c[0][0], c[0][1]) if c else None
    jb = S["jenkins_builds"]
    def jenkins_first(job):
        c = [x for x in jb if x[1] == job]
        x = min(c, key=lambda x: float(x[0])) if c else None
        return "slack:C05433XK267:%s" % x[0] if x else None
    def jenkins_last():
        if not jb:
            return None
        x = max(jb, key=lambda x: float(x[0]))
        return "slack:C05433XK267:%s" % x[0]
    issues = LI["issue_index"]
    def linear_first(team):
        c = [(r[4], i) for i, r in issues.items() if r[0] == team and r[4]]
        return "linear:" + min(c)[1] if c else None
    def linear_last_created():
        candidates = [(r[4], i) for i, r in issues.items() if r[4]]
        return "linear:" + max(candidates)[1] if candidates else None
    def trello_last():
        T = jload(TRELLO)
        if not T["cards"]:
            return None
        c = max(T["cards"], key=lambda c: c.get("dateLastActivity") or "")
        return "trello:" + c["id"]
    def beat(word):
        for b in sorted(B, key=lambda b: b["target_date"] or ""):
            if before_clock(b["target_date"]) and (b["target_date"] or "") >= "2024" and word.lower() in (b["storyline_name"] or "").lower() + " " + (b["action"] or "").lower() and len(b["verified_services"]) >= 2:
                a = [x for x in b["artifacts"] if x["exists"] and x["service"] not in ("snowflake",)]
                if a:
                    return a[0]["record_id"]
        return None
    def resolve(tok):
        if not tok.startswith("@"):
            return tok
        kind, _, arg = tok[1:].partition(":")
        if kind == "gmail":
            sub, _, app = arg.partition(":")
            if sub == "testflight_first" and app in tf_first:
                return gfile(tf_first[app][1])
            if sub == "testflight_last" and app in tf_last:
                return gfile(tf_last[app][1])
            if sub == "dist_first" and app in dist_first:
                return gfile(dist_first[app][1])
            if sub == "helpshift_first":
                return gfile(hs[0][1]) if hs else None
            return None
        if kind == "slack_mirror_first":
            return mirror_first(arg)
        if kind == "slack_mirror_last":
            return mirror_last(arg)
        if kind == "slack_mirror_pr":
            return mirror_pr(arg)
        if kind == "jenkins_first":
            return jenkins_first(arg)
        if kind == "jenkins_last":
            return jenkins_last()
        if kind == "linear_first":
            return linear_first(arg)
        if kind == "linear_team":
            return "linear_team:" + arg
        if kind == "linear_last_created":
            return linear_last_created()
        if kind == "trello_last_activity":
            return trello_last()
        if kind == "beat":
            return beat(arg)
        if kind == "first_pr_with":
            GHc = jload(CACHE + "/kb_github.json")
            c = [(V.prs[p][0], p) for p, keys in GHc["pr_linear_keys"].items() if any(k.startswith(arg + "-") for k in keys) and p in V.prs]
            return "github:" + min(c)[1] if c else None
        return None
    def verify(rid):
        if rid is None:
            return None
        if rid.startswith("linear_team:"):
            t = LI["teams"].get(rid.split(":", 1)[1])
            return {"id": rid, "service": "linear", "when": t and t["created_at"], "label": t and t["name"], "ok": bool(t)}
        if rid.startswith("snowflake:") and "/" in rid:
            tab, key = rid.split(":", 1)[1].split("/", 1)
            r = (SR.get(tab) or {}).get(key)
            when = r and (r.get("date") or r.get("start_date") or r.get("month_end_date"))
            label = r and (r.get("counterparty") or r.get("event_name") or r.get("notes") or r.get("status"))
            return {"id": rid, "service": "snowflake", "when": when, "label": str(label)[:80] if label else (str(r)[:80] if r else None), "ok": r is not None}
        ok, svc, when, label = V.check(rid)
        if svc == "gmail" and rid.endswith(".json"):
            f = rid.split(":", 1)[1]
            if ok:
                t = jload(GMAIL + "/threads/" + f)
                ms = t.get("messages") or []
                when = (ms[0].get("date_parsed") or ms[0].get("date")) if ms else None
                label = (ms[0].get("subject") or "")[:80] if ms else None
        return {"id": rid, "service": svc, "when": when, "label": label if isinstance(label, str) else label, "ok": ok}
    spine = []
    for date, cat, title, ev in EVENTS:
        if not before_clock(date):
            continue
        resolved = [resolve(e) for e in ev]
        checks = [verify(r) for r in resolved if r]
        good = [c for c in checks if c and c["ok"] and before_clock(c.get("when"))]
        bad = [e for e, r in zip(ev, resolved) if r is None] + [c["id"] for c in checks if c and not c["ok"]]
        bad += [c["id"] + " (undated or outside assigned freeze)" for c in checks
                if c and c["ok"] and not before_clock(c.get("when"))]
        svcs = sorted(set(c["service"] for c in good))
        spine.append({"date": date, "category": cat, "title": title, "services": svcs, "evidence": good, "unresolved": bad,
                      "meets_2_service_rule": len(svcs) >= 2,
                      "orientation_only": CONTEXT["universe_date_key"] != "2026-02-14"})
    # departures (derived from activity.json)
    A = jload(OUT + "/activity.json")
    deps = []
    for em, v in A["people"].items():
        if not v.get("persona") or not v["status_at_clock"].startswith("quiet_since_2025"):
            continue
        s = v["services"].get("slack") or {}
        ev = []
        if s.get("last") and s.get("id"):
            chan = S["person"].get(s["id"], {}).get("chan", {})
            if chan:
                cid, (f_, l_, n_) = max(chan.items(), key=lambda kv: kv[1][1])
                ev.append(verify("slack:%s:%.6f" % (cid, l_)))
        lin = v["services"].get("linear") or {}
        if lin.get("last"):
            uid = lin["user_id"]
            cands = [(r[4], i) for i, r in issues.items() if r[3] == uid and r[4]] + [(r[6], i) for i, r in issues.items() if r[2] == uid and r[6]]
            if cands:
                ev.append(verify("linear:" + max(cands)[1]))
        ev = [e for e in ev if e and e["ok"] and before_clock(e.get("when"))]
        if not before_clock(v["departure_signals"]["last_authored_activity"]):
            continue
        deps.append({"date": v["departure_signals"]["last_authored_activity"], "category": "people", "title": "%s goes quiet (last authored activity %s via %s)" % (v["name"], v["departure_signals"]["last_authored_activity"], v["departure_signals"]["last_authored_service"]),
                     "services": sorted(set(e["service"] for e in ev)), "evidence": ev, "unresolved": [], "meets_2_service_rule": len(set(e["service"] for e in ev)) >= 2, "person": em})
    spine += deps
    spine.sort(key=lambda e: e["date"] or "")
    beats = []
    for b in B:
        eligible = [a for a in b["artifacts"] if a["exists"] and before_clock(a.get("when"))]
        services = sorted(set(a["service"] for a in eligible))
        if before_clock(b["target_date"]) and (b["target_date"] or "") >= "2024" and len(services) >= 2:
            beats.append({"date": b["target_date"], "storyline": b["storyline"], "storyline_name": b["storyline_name"], "beat": b["beat"], "actor": b["actor"], "action": b["action"],
                          "services": services, "evidence": [a["record_id"] for a in eligible][:8], "missing": b["missing"],
                          "orientation_only": True})
    beats.sort(key=lambda x: x["date"])
    out = {"_meta": {"generated_by": "Task_Authoring/references/universe_kb/_build/assemble_timeline.py", "clock": CLOCK_ISO,
                     "rule": "Each spine event lists only evidence ids re-verified against the base exports (when = the record's own timestamp). meets_2_service_rule is false where fewer than two services verified.",
                     "storyline_beats_note": "Beats come from selected source metadata; summaries/figures are orientation only, never ground truth. Undated/future evidence cannot support a completed event. Non-February static narrative titles remain orientation_only pending record-level checks.",
                     "prelude_2023": "Founded Mar 2023 (Slack/Linear/Trello start Feb-Mar 2023; GameOfDominoes#1 2023-04-12); $3M Series Seed at $10M post led by Griffin closed Jul-Aug 2023 (CASH_BALANCE: a $2.70M wire in 2023-07); see storyline beats for 2023."},
           "spine": spine, "storyline_beats_2024_plus": beats,
           "counts": {"spine_events": len(spine), "spine_meeting_rule": sum(1 for e in spine if e["meets_2_service_rule"]), "storyline_beats": len(beats)}}
    jdump(out, OUT + "/timeline.json", indent=1)
    print("timeline", out["counts"])
    for e in spine:
        if not e["meets_2_service_rule"] or e["unresolved"]:
            print("CHECK", e["date"], e["title"][:60], e["services"], e["unresolved"])


if __name__ == "__main__":
    main()
