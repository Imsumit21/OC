#!/usr/bin/env python3
"""Writes task_inputs/01_Universe_Inject.sql from plan/seed_text.json, plan/base_parents.json and the record plan.
One row per statement, literal values only. Run from the workspace root."""
import calendar, hashlib, json, os, re, sys, uuid
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TASK = os.path.dirname(WF)
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
SEED6 = json.load(open(os.path.join(HERE, "seed_text_rev6.json")))   # rev6: second carriers for three corrections (baseline exposure, run_forensics/rev5/baseline)
SEED7 = json.load(open(os.path.join(HERE, "seed_text_rev7.json")))
SEED9 = json.load(open(os.path.join(HERE, "seed_text_rev9.json")))   # rev9: Brian's DM keeps the popups line and takes his Daily Gift note   # rev7: Vincent closes the tooltip thread (/prompt on rev6, Issue 1)
PARENTS = json.load(open(os.path.join(HERE, "base_parents.json")))
REPO = "harmonygames-Games/GameOfDominoes"
BOT = "SLACK_BOT_0004_SLACK_ID"
OUT, ROWS = {}, {}
UPDATES = []


def q(v):
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if "\n" in s or "\\" in s or "\r" in s:
        return "E'" + s.replace("\\", "\\\\").replace("'", "''").replace("\r", "\\r").replace("\n", "\\n") + "'"
    return "'" + s.replace("'", "''") + "'"


def j(v):
    return json.dumps(v, ensure_ascii=False)


def ins(table, cols, vals, key):
    OUT.setdefault(table.split(".")[0], []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)


def upd(table, sets, key_col, key):
    s = ", ".join(f"{c} = {q(v)}" for c, v in sets)
    OUT.setdefault(table.split(".")[0], []).append(f"UPDATE {table} SET {s} WHERE {key_col} = {q(key)};")
    UPDATES.append((table, key))


def epoch(t):
    return calendar.timegm((int(t[0:4]), int(t[5:7]), int(t[8:10]), int(t[11:13]), int(t[14:16]), int(t[17:19])))


def iso(ts):
    import time
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(int(float(ts))))


def mint_ts(when, key):
    h = int(hashlib.sha256(key.encode()).hexdigest()[:8], 16) % 99999
    return f"{epoch(when)}.{h:05d}9"


def slack_id(channel, ts):
    return hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]


def hexid(name, n):
    return hashlib.sha256(("owen:" + name).encode()).hexdigest()[:n]


# ---------------------------------------------------------------- people
EM = {k: f"{k}@harmonygames.co" for k in ("owen.baker", "arthur.blake", "brian.foster", "oliver.brooks", "vincent.parker", "marcus.bennett", "robert")}
SL = {"Robert": "EMPLOYEE_0016_SLACK_ID", "Owen": "EMPLOYEE_0021_SLACK_ID", "Arthur": "EMPLOYEE_0025_SLACK_ID", "Brian": "EMPLOYEE_0026_SLACK_ID", "Vincent": "EMPLOYEE_0012_SLACK_ID",
      "Marcus": "EMPLOYEE_0002_SLACK_ID", "Oliver": "EMPLOYEE_0003_SLACK_ID"}
LIN = {"Arthur": "usr_cc3e90160f490686", "Brian": "usr_fc22d5941b2aeb5c", "Oliver": "usr_bdf01b53c6a92c5e", "Vincent": "usr_65c76e0b87aa7e9b"}
GH = {"Arthur": "EMPLOYEE_0025_GITHUB_USERNAME", "Owen": "PERSON_5877_GITHUB_USERNAME", "Brian": "PERSON_0180_GITHUB_USERNAME"}
GHN = {"Arthur": "arthur.blake", "Owen": "owen.baker", "Brian": "brian.foster"}
TRELLO_BRIAN = "d1cd0fef645a6c978ae1f068"
ROOT_OWEN, ROOT_ARTHUR, ROOT_BRIAN = "d_4e13bd40cc73d0fc76f87c", "d_cc3e90160f490686039986", "d_fc22d5941b2aeb5c03ad32"
FOLDER = "d_9b41e7c2a05d36f8e1c7a4"
DOC, DECOY, DECK = "f_3ca9e15d7b20f4e681ad52", "f_72e0b4c3d91a5f68c2b7e4", "f_d15a8c70e3f2b94a61c8d3"
TRACKER = "f_" + hexid("tracker", 22)

# ---------------------------------------------------------------- drive and docs
MIME = {"doc": "application/vnd.google-apps.document", "sheet": "application/vnd.google-apps.spreadsheet",
        "slides": "application/vnd.google-apps.presentation", "folder": "application/vnd.google-apps.folder"}
DRIVE_COLS = ["id", "name", "mime_type", "parents_json", "owner_email", "shared_with_emails_json", "shared_roles_json", "visibility", "owners_json",
              "modified_time", "created_time", "trashed", "starred"]


def drive(fid, name, kind, parent, owner, shared, when, role="reader"):
    ins("gdrive.drive_files", DRIVE_COLS, [fid, name, MIME[kind], j([parent]), owner, j(shared), j([{"email": e, "role": role} for e in shared]),
        "private", j([owner]), when, when, False, False], fid)


drive(FOLDER, "DD bug carry-over", "folder", ROOT_OWEN, EM["owen.baker"], [], "2026-02-12T23:00:00Z")
doc_shared = [EM["owen.baker"]]
drive(DOC, "DD bug carry-over notes", "doc", ROOT_ARTHUR, EM["arthur.blake"], doc_shared, SEED["rule_doc"]["at"])
team = [EM["owen.baker"], EM["arthur.blake"], EM["oliver.brooks"]]
drive(DECOY, "Zombie Match bug list notes", "doc", ROOT_BRIAN, EM["brian.foster"], team, SEED["decoy_doc"]["at"])
drive(DECK, "UI optimization wrap", "slides", ROOT_BRIAN, EM["brian.foster"], team, SEED["deck"]["at"])
drive(TRACKER, "UI pass tracker", "sheet", ROOT_BRIAN, EM["brian.foster"], team, "2025-11-20T18:40:00Z")

DOC_COLS = ["document_id", "title", "owner_email", "shared_with_emails_json", "visibility", "body_text", "style_runs_json", "revision_id", "drive_file_id",
            "created_time", "modified_time"]


def gdoc(fid, title, owner, shared, body, when):
    runs = [{"start": 0, "end": len(body), "named_style": "NORMAL_TEXT", "list_id": None, "list_nesting": 0}]
    ins("gdocs.docs_documents", DOC_COLS, [fid, title, owner, j(shared), "private", body, j(runs), hexid("rev" + fid, 10), fid, when, when], fid)


gdoc(DOC, "DD bug carry-over notes", EM["arthur.blake"], doc_shared, SEED["rule_doc"]["text"], SEED["rule_doc"]["at"])
gdoc(DECOY, "Zombie Match bug list notes", EM["brian.foster"], team, SEED["decoy_doc"]["text"], SEED["decoy_doc"]["at"])

# ---------------------------------------------------------------- sheets: Brian's working tracker of the UI pass
ins("gsheets.sheets_spreadsheets", ["spreadsheet_id", "title", "owner_email", "shared_with_emails_json", "visibility", "drive_file_id", "created_time", "modified_time"],
    [TRACKER, "UI pass tracker", EM["brian.foster"], j(team), "private", TRACKER, "2025-11-20T18:40:00Z", "2025-11-20T18:40:00Z"], TRACKER)
TABS = [("Core", [["Splash Screen", "ENG-2409", "done"], ["Shop", "ENG-2410", "merged"], ["Character Section", "ENG-2411", "done"], ["Saga map", "ENG-2412", "done"], ["Teams", "ENG-2413", "done"], ["Leaderboard", "ENG-2414", "merged"],
                  ["Quest", "ENG-2415", "merged"], ["Profile Page", "ENG-2416", "done"], ["Settings", "ENG-2417", "merged"], ["Level win", "ENG-2418", "merged"], ["Out of moves", "ENG-2419", "merged"], ["Chapter Section", "ENG-2420", "done"],
                  ["Tavern", "ENG-2421", "done"], ["Pre-game Panel", "ENG-2422", "done"], ["Transition Screens", "ENG-2423", "done"]]),
        ("Live-Ops", [["Collect & Win", "ENG-2424", "done"], ["Nate's Treasure", "ENG-2425", "merged"], ["Axe Arena", "ENG-2426", "merged"], ["River Rush", "ENG-2427", "done"],
                      ["Season Pass", "ENG-2428", "next"], ["Remove Ad", "ENG-2429", "done"], ["Offers", "ENG-2430", "done"], ["Rate-us", "ENG-2431", "done"],
                      ["Daily Gift", "ENG-2437", "last pass"]]),
        ("Mini-Games", [["River Tile", "ENG-2432", "merged"], ["Memory Tile", "ENG-2433", "merged"], ["Tile Dozer", "ENG-2434", "merged"], ["Lucky Drop", "ENG-2435", "merged"]])]
for i, (title, rows) in enumerate(TABS):
    grid = [["Screen", "Ticket", "Status"]] + rows
    ins("gsheets.sheets_sheets", ["spreadsheet_id", "sheet_id", "title", '"index"', "row_count", "column_count", "grid_json"], [TRACKER, i, title, i, 1000, 26, j(grid)], f"{TRACKER}#{title}")

# ---------------------------------------------------------------- slides: the wrap deck
ins("gslides.slides_presentations", ["presentation_id", "title", "owner_email", "shared_with_emails_json", "visibility", "drive_file_id", "revision_id", "created_time", "modified_time"],
    [DECK, "UI optimization wrap", EM["brian.foster"], j(team), "private", DECK, hexid("revdeck", 10), SEED["deck"]["at"], SEED["deck"]["at"]], DECK)
PAGES = [("UI optimization wrap", "UI pass wrapped up. Core, Live-Ops and Mini-Games main screens are on the optimized sprites."),
         ("Core", "Splash, Shop, Characters, Saga map, Teams, Leaderboard, Quest, Profile, Settings, level win, out of moves, Chapters, Tavern, Pre-game and Transitions main screens are on the optimized sprites."),
         ("Live-Ops", "Collect & Win, Nate's Treasure, Axe Arena, River Rush, Season Pass, Remove Ad, Offers and Rate-us main screens are on the optimized sprites."),
         ("Mini-Games", "River Tile, Memory Tile, Tile Dozer and Lucky Drop main screens are on the optimized sprites.")]
for i, (head, body) in enumerate(PAGES):
    pid = "slide_" + hexid(f"page{i}", 12)
    ins("gslides.slides_pages", ["presentation_id", "object_id", '"index"', "layout", "notes"], [DECK, pid, i, "TITLE_AND_BODY", None], pid)
    for n, (ph, text, y, h) in enumerate((("TITLE", head, 457200, 800000), ("BODY", body, 1400000, 2800000))):
        ins("gslides.slides_page_elements", ["presentation_id", "page_object_id", "object_id", "kind", "text", "placeholder_type", "x_emu", "y_emu", "width_emu", "height_emu", "table_json", "ordinal"],
            [DECK, pid, "el_" + hexid(f"page{i}el{n}", 12), "shape", text, ph, 457200, y, 8229600, h, None, n], f"{pid}#{n}")

# ---------------------------------------------------------------- slack
SLACK_COLS = ["id", "ts", "channel_id", "type", "user_id", "text", "thread_parent_id", "thread_ts_legacy", "reply_count", "reply_users_count", "latest_reply", "is_activity_message",
              "subtype", "reactions_json", "files_json", "attachments_json", "created_at", "metadata_json"]
added = {}


def post(channel, ts, user, text, when, parent_ts=None, attachments=None):
    pid = None
    if parent_ts:
        p = PARENTS[f"{channel}/{parent_ts}"]
        pid = p["id"]
        added.setdefault(f"{channel}/{parent_ts}", []).append((ts, user))
    ins("slack.slack_messages", SLACK_COLS, [slack_id(channel, ts), ts, channel, "message", user, text, pid, parent_ts, 0, 0, None, False, None, "[]", "[]",
        j(attachments or []), when, "{}"], f"{channel}/{ts}")


def seed_post(name, user, parent_ts=None):
    s = SEED[name]
    ch, ts = s["id"].split("/")
    post(ch, ts, user, s["text"], s["at"], parent_ts)


seed_post("hub", SL["Arthur"])
seed_post("vincent_note", SL["Marcus"])
seed_post("brian_dm", SL["Brian"])
for _n in ("brian_popups", "brian_gift"):   # rev9: Tavern rests on Marcus's DM and Apple on Vincent's mail alone (/hardness on rev7 and rev8: a from:Brian sweep caught every Brian line)
    _ch, _ts = SEED9[_n]["id"].split("/")
    post(_ch, _ts, SL["Brian"], SEED9[_n]["text"], SEED9[_n]["at"], None)
seed_post("brian_reply", SL["Brian"], "1764042435.541279")
seed_post("bar_reply", SL["Brian"], "1766415326.501939")
seed_post("flick_reply", SL["Robert"], "1764013100.931229")
seed_post("train_reply", SL["Vincent"], "1763394823.486369")
seed_post("team_reply", SL["Vincent"], "1763549817.580759")
seed_post("lives_reply1", SL["Vincent"], "1763548856.943389")
seed_post("lives_reply2", SL["Vincent"], "1763642552.651279")
_t7 = SEED7["tooltip_reply"]   # rev7: same retest session as train_reply and lives_reply1/2
post(*_t7["id"].split("/"), SL["Vincent"], _t7["text"], _t7["at"], _t7["parent"].split("/")[1])
# Leonard makes Owen a guest on Feb 11; Arthur puts him on a spare paid seat (C0ADGSZKR3R/1770842395.641349: five seats, three kept) and he rejoins.
# The base already has his leave from C05V5FNLB9V and C050WGU41HR; the other task channels get a leave and a join, because a join needs a leave.
LEAVES = [("CE156FDFB428", "2026-02-11T20:41:12Z"), ("C09Q4S613CN", "2026-02-11T20:41:13Z"), ("C05433XK267", "2026-02-11T20:41:14Z"), ("C09SWTHEMEW", "2026-02-11T20:41:15Z")]
JOINS = [("C05V5FNLB9V", "2026-02-12T22:41:03Z"), ("CE156FDFB428", "2026-02-12T22:41:27Z"), ("C09Q4S613CN", "2026-02-12T22:41:49Z"), ("C05433XK267", "2026-02-12T22:42:12Z"),
         ("C09SWTHEMEW", "2026-02-12T22:42:36Z"), ("C050WGU41HR", "2026-02-12T22:42:58Z")]
WORD = lambda ch: "conversation" if ch == "CE156FDFB428" else "channel"   # canvas comment channels say 'conversation' in the base
for ch, when in LEAVES:
    ts = mint_ts(when, "leave" + ch)
    ins("slack.slack_messages", SLACK_COLS, [slack_id(ch, ts), ts, ch, "message", SL["Owen"], f"<@{SL['Owen']}> has left the {WORD(ch)}", None, None, 0, 0, None, False, "channel_leave", "[]", "[]", "[]", when, "{}"], f"{ch}/{ts}")
for ch, when in JOINS:
    ts = mint_ts(when, "join" + ch)
    ins("slack.slack_messages", SLACK_COLS, [slack_id(ch, ts), ts, ch, "message", SL["Owen"], f"<@{SL['Owen']}> has joined the {WORD(ch)}", None, None, 0, 0, None, False, "channel_join", "[]", "[]", "[]", when, "{}"], f"{ch}/{ts}")
CANVAS = "CE156FDFB428"
CONTROLS = [("1763394616.234099", "2025-11-21T15:20:04Z", "purple is gone on the last build"),
            ("1763394911.691209", "2025-11-21T15:28:31Z", "looks ok now"),
            ("1763643072.577249", "2025-11-21T15:33:12Z", "text fits now"),
            ("1763643032.027129", "2025-11-21T15:35:47Z", "both flows are ok now"),
            ("1763549271.970799", "2025-11-21T15:37:20Z", "ok on my side"),
            ("1763642881.891429", "2025-11-21T15:40:05Z", "these fit now")]
for parent, when, text in CONTROLS:
    post(CANVAS, mint_ts(when, parent), SL["Vincent"], text, when, parent)
post("C05V5FNLB9V", mint_ts("2025-11-28T12:10:30Z", "mega"), SL["Marcus"], "still happens on today's build", "2025-11-28T12:10:30Z", "1764256187.655299")

# ---------------------------------------------------------------- github: inline review comments, conversation comments, app copies
PR_TITLES = {1895: "ENG-2425: Nathan's Treasure - UI Optimization", 1898: "[PERSON_NAME_0092]/eng 2410", 1901: "ENG-2417: Settings UI Optimization", 1902: "ENG-2418: Level - win UI Optimization",
             1903: "ENG-2419: Level Lose - Out-of-moves Screens UI Optimization", 1905: "ENG-2405: Mini-Games UI Optimization", 1907: "[PERSON_NAME_0092]/quest and leaderboard",
             1908: "ENG-2426: Axe Arena - UI Optimization", 1915: "Core gameplay visual artifact fixes", 1916: "New core game camera config"}
OPENED = {1895: "1763072479.270789", 1898: "1763406238.439879", 1901: "1763493332.244939", 1902: "1763495409.791699", 1903: "1763504544.082819", 1905: "1763527217.342039",
          1907: "1763585563.536669", 1908: "1763593226.132859", 1915: "1766185637.825279", 1916: "1766769663.892649"}
NEXT_C = {1895: 3, 1898: 3, 1901: 3, 1902: 3, 1903: 3, 1905: 3, 1907: 2, 1908: 3, 1915: 2, 1916: 2}
NEXT_EV = {1895: 6, 1898: 8, 1901: 6, 1902: 6, 1903: 6, 1905: 6, 1907: 7, 1908: 6, 1915: 6, 1916: 5}
BOTS = "C050WGU41HR"
FOOT = {"footer": f"<https://github.com/{REPO}|{REPO}>", "footer_icon": "https://slack.github.com/static/img/favicon-neutral.png"}


def mirror(n, who, when, body, kind):
    login = GHN[who]
    link = f"https://github.com/{REPO}/pull/{n}"
    if kind == "comment":
        cid = 3475315163 + int((epoch(when) - 1761958096) * 45.27) + int(hashlib.sha256(f"{n}{when}".encode()).hexdigest()[:4], 16) % 4000  # in sequence with the base ids
        a = {"color": "24292f", "fallback": f"[{REPO}] Comment on #{n}", **FOOT, "id": 1, "mrkdwn_in": ["text"],
             "pretext": f"<{link}#issuecomment-{cid}|Comment> on pull request by <https://github.com/{login}|{login}>", "text": body,
             "title": f"<{link}|#{n} {PR_TITLES[n]}>", "ts": epoch(when)}
    else:
        rid = {1905: 3482612642, 1908: 3485366118}[n]  # the base review these comments belong to
        pre = f"Review comment by <https://github.com/{login}|{login}> on <https://github.com/owen.baker|owen.baker's> pull request"
        a = {"color": "24292f", "fallback": f"[{REPO}] {pre}", **FOOT, "id": 1, "mrkdwn_in": ["text"], "pretext": pre, "text": body,
             "title": f"Review on #{n} {PR_TITLES[n]}", "title_link": f"{link}#pullrequestreview-{rid}", "ts": epoch(when)}
    post(BOTS, mint_ts(when, f"mirror{n}{kind}"), BOT, "", when, OPENED[n], [a])


def pr_comment(n, who, when, body):
    pr = f"{REPO}#{n}"
    cid, ev = f"{pr}#c_{NEXT_C[n]}", f"{pr}#ev_{NEXT_EV[n]}"
    NEXT_C[n] += 1
    NEXT_EV[n] += 1
    ins("github.github_pr_comments", ["id", "pr_id", "author_login", "body", "created_at", "updated_at"], [cid, pr, GH[who], body, when, when], cid)
    ins("github.github_timeline_events", ["id", "pr_id", "event", "actor_login", "created_at", "data_json"], [ev, pr, "commented", GH[who], when, "{}"], ev)
    mirror(n, who, when, body, "comment")


CONV = [(1895, "Owen", "2025-11-13T22:40:12Z", "Treasure hunt screens and their pop ups are on the optimized textures now."),
        (1898, "Brian", "2025-11-17T19:20:41Z", "Shop screen is all in here."),
        (1901, "Owen", "2025-11-18T19:32:09Z", "Main menu and gameplay settings are both in here."),
        (1902, "Owen", "2025-11-18T20:05:33Z", "Win screen pop up, banner and stars are in here."),
        (1903, "Owen", "2025-11-18T22:35:18Z", "Out of moves screen is in here."),
        (1905, "Owen", "2025-11-19T04:52:27Z", "All four minigames are in here, sprites swapped."),
        (1907, "Brian", "2025-11-19T21:10:44Z", "Quest and leaderboard panels are both in here."),
        (1908, "Owen", "2025-11-19T23:12:06Z", "Axe Arena panels are in here."),
        (1915, "Arthur", "2025-12-19T23:40:02Z", "Taking this into EconomyChanges so it goes out with the next BoomBit drop."),
        (1916, "Arthur", "2025-12-26T18:50:29Z", "Same here, into EconomyChanges for the next BoomBit drop.")]
for n, who, when, body in CONV:
    pr_comment(n, who, when, body)

RC_COLS = ["id", "pr_id", "author_login", "body", "path", "diff_hunk", "line", "position", "commit_id", "in_reply_to_id", "created_at", "pull_request_review_id", "side", "subject_type", "seq"]
HEADS = {1905: "aebf9b9f907efab0a20b05b9d6b9b50181016fe8", 1908: "2fa7dca0a1c7d7ac4630e71e259c910d02111aab"}
for name, n, path, hunk, line in (
        ("inline_td", 1905, "Assets/Sprites/OptimizedCommons/bg - popup title - yellow.png.meta",
         "@@ -0,0 +1,5 @@\n+fileFormatVersion: 2\n+guid: 7c1d4ab26e0f4a13b2c98f51d0e6a7c4\n+TextureImporter:\n+  internalIDToLocalIDTable: []\n+  externalObjects: {}", 5),
        ("inline_axe", 1908, "Assets/Sprites/OptimizedDevOps/bg - ranking rewards.png.meta",
         "@@ -0,0 +1,5 @@\n+fileFormatVersion: 2\n+guid: e41b0d7f93a24c6a8f1de2b75c30a9d6\n+TextureImporter:\n+  internalIDToLocalIDTable: []\n+  externalObjects: {}", 5)):
    s = SEED[name]
    ins("github.github_review_comments", RC_COLS, [s["id"], f"{REPO}#{n}", GH["Arthur"], s["text"], path, hunk, line, None, HEADS[n], None, s["at"], f"{REPO}#{n}#rev_1", "RIGHT", "line", 1], s["id"])
    mirror(n, "Arthur", s["at"], s["text"], "review")

# ---------------------------------------------------------------- slack thread counters
for key, reps in added.items():
    ch, ts = key.split("/")
    p = PARENTS[key]
    users = set(p["reply_users"]) | {u for _, u in reps}
    latest = max([p["latest_reply"] or "0"] + [t for t, _ in reps], key=float)
    upd("slack.slack_messages", [("thread_ts_legacy", ts), ("reply_count", p["reply_count"] + len(reps)), ("reply_users_count", len(users)), ("latest_reply", latest)], "id", p["id"])

# ---------------------------------------------------------------- trello
BADGE = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0, "checkItemsEarliestDue": None, "comments": 1, "description": True,
         "due": None, "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}
TCARD = ["id", "name", '"idBoard"', '"idList"', '"desc"', "pos", "closed", "due", '"dueComplete"', '"idMembers_json"', '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', "url", '"dateLastActivity"', "cover_json", "badges_json"]
TACT = ["id", "type", "date", '"idMemberCreator"', '"idBoard"', '"idCard"', "data_json"]


def trello(card, name, desc, board, bname, bshort, lst, lname, short, idshort, created, seed, items=(), last=None):
    s = SEED[seed]
    badge = dict(BADGE, checkItems=len(items), checkItemsChecked=sum(1 for _, st in items if st == "complete"))
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    ins("trello.trello_cards", TCARD, [card, name, board, lst, desc, 1048576.0, False, None, False, j([TRELLO_BRIAN]), "[]", idshort, None, None,
        f"https://PERSON_6092_TRELLO_USERNAME.com/c/{short}/{idshort}-{slug}", last or s["at"], None, j(badge)], card)
    b = {"id": board, "name": bname, "shortLink": bshort}
    c = {"id": card, "idShort": idshort, "name": name, "shortLink": short}
    l = {"id": lst, "name": lname}
    create_id = card[:8] + hexid("create" + card, 16)
    ins("trello.trello_actions", TACT, [create_id, "createCard", created, TRELLO_BRIAN, board, card, j({"board": b, "card": c, "list": l})], create_id)
    ins("trello.trello_actions", TACT, [s["id"], "commentCard", s["at"], TRELLO_BRIAN, board, card, j({"board": b, "card": c, "idCard": card, "list": l, "text": s["text"], "textData": {"emoji": {}}})], s["id"])
    if items:
        cl = card[:8] + hexid("checklist" + card, 16)
        ins("trello.trello_checklists", ["id", "name", '"idCard"', '"idBoard"', "pos"], [cl, "Main screens checked", card, board, 16384.0], cl)
        for n, (item, st) in enumerate(items, 1):
            iid = card[:8] + hexid("item" + item, 16)
            ins("trello.trello_check_items", ["id", "name", "state", '"idChecklist"', "pos", "due", '"idMember"'], [iid, item, st, cl, 16384.0 * n, None, TRELLO_BRIAN], iid)


trello("690b27282f4c1b7a6e93d512", "UI optimization pass", "Optimized sprites for the core, live ops and minigame screens. Tickets are under the UI Changes master.", "65eb4ec525346c8070ca638f", "DD Product Roadmap", "Yg3yTuCR",
       "66c38013d3990617429e50e3", "[PERSON_NAME_49938] (November 27th)", "uI7pAss3", 211, iso(0x690b2728), "rule_comment",
       [(row[0], "incomplete" if row[0] == "Daily Gift" else "complete") for _, tab in TABS for row in tab], "2025-11-21T15:30:00Z")
ZM_T = "2025-09-23T11:02:00Z"
trello(f"{epoch(ZM_T):08x}" + hexid("zmcard", 16), "ZM bug list close-outs", "How we close the ZM bug list out.", "6851a6569f3bf818760632ab", "ZM ROADMAP", "HSqnngwQ",
       "68c451221ebabaf255a7d16b", "Backlog", "zMcl0sE5", 80, ZM_T, "zm_comment")

# ---------------------------------------------------------------- gmail: Vincent's mail and the review invitations
GT = ["id", "user_email", "snippet", "history_id"]
GM = ["id", "thread_id", "user_email", "label_ids_json", "snippet", "internal_date", "date", "size_estimate", "subject", "from_email", "from_name", "to_json", "cc_json", "bcc_json", "reply_to_json",
      "body_text", "body_html", "headers_json", "in_reply_to", '"references"', "mbox_from", "attachments_meta_json"]


def mail(box, thread, msgid, labels, subject, frm, fname, to, when, body):
    snippet = re.sub(r"\s+", " ", body)[:140]
    tid = f"{box}/{thread}"
    ins("gmail.gmail_threads", GT, [tid, box, snippet, None], tid)
    import email.utils
    date_h = email.utils.formatdate(epoch(when), usegmt=True).replace("GMT", "+0000")
    hdr = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": date_h}, {"name": "Subject", "value": subject}, {"name": "From", "value": f"{fname} <{frm}>"}, {"name": "To", "value": to}]
    mid = f"{box}/{msgid}"
    ins("gmail.gmail_messages", GM, [mid, tid, box, j(labels), snippet, epoch(when) * 1000, when, len(body) + 900, subject, frm, fname, j([to]), "[]", "[]", "[]", body, None, j(hdr), None, None, None, "[]"], mid)


m = SEED["mail"]
subj, body = m["text"].split("\n\n", 1)
subj = subj.replace("Subject: ", "")
thread = m["id"].split("/")[1]
msgid = "<CAK" + hexid("vmail", 28) + "@mail.gmail.com>"
mail(EM["owen.baker"], thread, msgid, ["INBOX", "CATEGORY_PERSONAL"], subj, EM["vincent.parker"], "Vincent Parker", f"Owen Baker <{EM['owen.baker']}>", m["at"], body)
mail(EM["vincent.parker"], thread, msgid, ["SENT"], subj, EM["vincent.parker"], "Vincent Parker", f"Owen Baker <{EM['owen.baker']}>", m["at"], body)
EVT = SEED["invite"]["id"]
START, END, MADE = "2026-02-15T17:00:00Z", "2026-02-15T17:30:00Z", SEED["invite"]["at"]
ATT = [("arthur.blake", True), ("robert", False), ("oliver.brooks", False), ("owen.baker", False)]
MEET = "https://meet.google.com/dbr-" + hexid("meet", 4) + "-rev"
ICAL = hexid("ical", 32) + "@hg4"
GUESTS = "\r\n".join(EM[k] + (" - organizer" if o else "") for k, o in ATT)
for k, name in (("owen.baker", "Owen Baker"), ("oliver.brooks", "Oliver Brooks"), ("robert", "Robert")):
    u = str(uuid.UUID(hexid("invite" + k, 32)))
    b = f"DD bug review\r\nSunday Feb 15, 2026 ⋅ 12pm – 12:30pm\r\nEastern Time - New York\r\n\r\nJoin with Google Meet\r\n{MEET}\r\n\r\nOrganizer\r\n{EM['arthur.blake']}\r\n\r\nGuests\r\n{GUESTS}\r\nView all guest info"
    mail(EM[k], str(1857000000000000000 + int(hexid("thr" + k, 10), 16) % 900000000000), f"<calendar-{u}@google.com>", ["INBOX", "CATEGORY_PERSONAL"],
         f"Invitation: DD bug review @ Sun Feb 15, 2026 12pm - 12:30pm (EST) ({name})", EM["arthur.blake"], "Arthur Blake", f"{name} <{EM[k]}>", "2026-02-12T23:05:03Z", b)

# ---------------------------------------------------------------- gcal
GC = ["event_id", "calendar_id", "summary", "description", "location", "start_ts", "end_ts", "start_json", "end_json", "organizer_email", "creator_email", "attendees_json", "status", "visibility", "transparency",
      "rrule_json", "recurring_event_id", "original_start_json", "sequence", "created", "updated", "hangout_link", "ical_uid"]
for k, _ in ATT:
    att = []
    for e, o in ATT:
        a = {"email": EM[e], "organizer": o, "responseStatus": "accepted" if o else "needsAction"}
        if e == k:
            a["self"] = True
        att.append(a)
    ins("gcal.gcal_events", GC, [EVT if k == "owen.baker" else "evt_" + hexid("cal" + k, 22), EM[k], "DD bug review", None, None, START, END, j({"dateTime": START}), j({"dateTime": END}), EM["arthur.blake"], EM["arthur.blake"], j(att), "confirmed", None, "opaque",
        "[]", None, None, 0, MADE, MADE, MEET, ICAL], f"{EVT}/{k}")

# ---------------------------------------------------------------- linear: notes on the tree and the candidate tickets, then state repairs
LC = ["id", "issue_id", "author_id", "parent_id", "body", "is_edited", "created_at", "updated_at"]
touched = {}


def note(cid, issue, who, body, when):
    ins("linear.linear_comments", LC, [cid, issue, LIN[who], None, body, False, when, when], cid)
    touched[issue] = max(touched.get(issue, ""), when)


for seed, issue, who in (("amend", "ENG-2401", "Arthur"), ("alias_note", "ENG-2363", "Vincent"), ("season_note", "ENG-2428", "Oliver")):   # rev9: Brian's Daily Gift note moved to his DM with Owen
    s = SEED[seed]
    note(s["id"], issue, who, s["text"], s["at"])
CHECKS = [("ENG-2429", "2025-11-19T14:27:00Z", "Checked the Remove Ad pop up on today's build, looks right on android."),
          ("ENG-2410", "2025-11-21T15:05:00Z", "Checked the Shop screen after the merge, looks right on android."),
          ("ENG-2430", "2025-11-21T15:15:00Z", "Checked the Offers on today's build, looks right on android.")]
for issue, when, body in CHECKS:
    note("comment_" + hexid("check-" + issue, 32), issue, "Brian", body, when)
TRIAGE = [("ENG-2280", "2025-11-20T22:10:00Z", "This one is the ios case where a returning player loads old data and the HUD and avatar don't come up."),
          ("ENG-2281", "2025-11-20T22:14:00Z", "Only the first puzzle after loading old data, on ios."),
          ("ENG-2398", "2025-11-20T22:18:00Z", "Stopgap for the relogin problems, this only adds the restart pop up."),
          ("ENG-2181", "2025-11-20T22:24:00Z", "Bots' frames on the weekly leaderboard only."),
          ("ENG-2351", "2025-11-20T22:29:00Z", "Text only, after opening the language screen."),
          ("ENG-2406", "2025-11-20T22:33:00Z", "Taps during play, nothing to do with how the scene looks.")]
for issue, when, body in TRIAGE:
    note("comment_" + hexid("triage-" + issue, 32), issue, "Arthur", body, when)
for issue, when in sorted(touched.items()):
    upd("linear.linear_issues", [("updated_at", when)], "id", issue)
# NB-14: the two master checklists disagree with the child tickets, so Arthur clears them before the carry-over.
for issue in ("ENG-2403", "ENG-2404"):
    upd("linear.linear_issues", [("description", None), ("updated_at", "2026-02-12T22:30:00Z")], "id", issue)

# ---------------------------------------------------------------- write
ORDER = ["gdrive", "gdocs", "gsheets", "gslides", "slack", "github", "trello", "gmail", "gcal", "linear"]
inserts = sum(len(v) for v in ROWS.values())
head = ["-- Are you planning to inject? Yes", "BEGIN;"]   # local marker for sql_lint; the certified platform copy has a blank line 1 (run_forensics/rev1)
body = []
for k in ORDER:
    body.append(f"-- ===================== {k.upper()} =====================")
    body += OUT[k]
text = "\n".join(head + body + ["COMMIT;"]) + "\n"
target = os.environ.get("SQL_OUT") or os.path.join(TASK, "01_Universe_Inject.sql")
if not (os.path.exists(target) and open(target).read() == text):
    open(target, "w").write(text)
print(inserts, "inserts", len(UPDATES), "updates", {k: len(v) for k, v in ROWS.items()})
