#!/usr/bin/env python3
"""Generate 01_Universe_Inject.sql for sample_task_01 (ip-sale-defect-schedule). Deterministic, literal values only."""
import datetime as dt
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
I = json.loads((ROOT / "work" / "ids.json").read_text())

A_EMAIL = "arthur.blake@harmonygames.co"
L_EMAIL = "leonard.hayes@harmonygames.co"
R_EMAIL = "robert@harmonygames.co"
S_EMAIL = "PERSON_9823_EMAIL"
S_NAME = "PERSON_9823_NAME"
U = {"A": "EMPLOYEE_0025_SLACK_ID", "L": "EMPLOYEE_0038_SLACK_ID", "R": "EMPLOYEE_0016_SLACK_ID",
     "O": "EMPLOYEE_0003_SLACK_ID", "V": "EMPLOYEE_0012_SLACK_ID"}

out = []
counts = {}


def q(v):
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v).replace("'", "''")
    if "\n" in s or "\r" in s or "\\" in s:
        s = s.replace("\\", "\\\\").replace("\r", "\\r").replace("\n", "\\n")
        return "E'" + s + "'"
    return "'" + s + "'"


def j(o):
    return json.dumps(o, ensure_ascii=False)


def ins(table, row, comment=None):
    if comment:
        out.append(f"-- {comment}")
    cols = ", ".join(f'"{c}"' if (c != c.lower() or c in ("references", "desc", "primary", "index")) else c for c in row)
    vals = ", ".join(q(v) for v in row.values())
    out.append(f"INSERT INTO {table} ({cols})\nVALUES ({vals});")
    counts[table] = counts.get(table, 0) + 1


def upd(table, sets, where, comment=None):
    if comment:
        out.append(f"-- {comment}")
    s = ", ".join((f'"{k}"' if k != k.lower() else k) + " = " + q(v) for k, v in sets.items())
    w = " AND ".join(f"{k} = {q(v)}" for k, v in where.items())
    out.append(f"UPDATE {table} SET {s} WHERE {w};")
    counts[table] = counts.get(table, 0) + 1


def ts_iso(ts):
    t = dt.datetime.fromtimestamp(float(ts), tz=dt.timezone.utc)
    return t.strftime("%Y-%m-%dT%H:%M:%S.") + ts.split(".")[1] + "Z"


def sid(ch, ts):
    return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]


# ------------------------------------------------------------------ SLACK
def slack(ch, ts, user, text, parent_ts=None, replies=None):
    row = {"id": sid(ch, ts), "ts": ts, "channel_id": ch, "type": "message", "user_id": user, "text": text,
           "thread_parent_id": sid(ch, parent_ts) if parent_ts else None,
           "thread_ts_legacy": parent_ts if parent_ts else (ts if replies else None),
           "reply_count": len(replies) if replies else 0,
           "reply_users_count": len({u for _, u in replies}) if replies else 0,
           "latest_reply": max(t for t, _ in replies) if replies else None,
           "is_activity_message": False, "subtype": None, "reactions_json": "[]", "files_json": "[]",
           "attachments_json": "[]", "created_at": ts_iso(ts), "metadata_json": "{}"}
    ins("slack.slack_messages", row)


out.append("-- ===================== SLACK =====================")
W = "C0ADGSZKR3R"
hub_replies = [(I["ts_hub_r1"], U["A"]), ("1770943255.618229", U["R"])]
slack(W, I["ts_hub"], U["L"],
      "<@EMPLOYEE_0025_SLACK_ID> one concrete data thing for the IP listing - sunset needs a known defects schedule from us for DD and ZM. "
      "go by sunset's intake list, i fwd'd it to you\n"
      "• tiers - use your severity tiers\n"
      "• where it goes + who gets it - my data room sheet\n"
      "• whats in which lot - my asset schedule\n"
      "• cut-off - whatever sunset's invite says when you send, they keep moving it\n"
      "• send it as soon as its done, dont wait for the cut-off\n"
      "• the known issues slide in my IP sale overview should show the per-lot totals by tier you send sunset\n"
      "• i made a linear ticket for it, update it the way it says\n"
      "• my confluence data room checklist has an engineering section, if it says something different from sunset's list tell me where\n"
      "post the totals here when done", replies=hub_replies)
slack(W, I["ts_hub_r1"], U["A"], "on it. my tiers are already written up, will get it done tomorrow", parent_ts=I["ts_hub"])
slack(W, "1770943255.618229", U["R"], "I'll do the art + audio inventory row in the index", parent_ts=I["ts_hub"])

DM = "D04UGG61DUM"
slack(DM, I["ts_lives"], U["L"],
      "also the minus lives bug (ENG-2277) is back on 309. claimed the daily gift and went to -2 lives. thought you clamped that in the admin endpoints PR?")
slack(DM, "1770779905.660219", U["A"], "ugh. ok will look")
slack(W, "1771000814.337509", U["L"], "filed the corporate + finance stuff in the data room folder")
claim_replies = [(I["ts_claim_r1"], U["A"]), (I["ts_claim_r2"], U["L"])]
slack(DM, I["ts_claim"], U["L"],
      "btw talked to oliver earlier, he said the sign in / account sync bugs were all fixed before xmas so those shouldnt show up as open on sunset's list",
      replies=claim_replies)
slack(DM, I["ts_claim_r1"], U["A"], "ok good, one less thing", parent_ts=I["ts_claim"])
slack(DM, I["ts_claim_r2"], U["L"],
      "scratch what i said about the sign in bugs - pinged oliver again, what he fixed before xmas was the splash screen hang. "
      "dunno about the rest", parent_ts=I["ts_claim"])

OD = "D07H86MU8JC"
slack(OD, "1770996671.284519", U["O"],
      "leonard asked me about the sign in bugs again. what i fixed before xmas was the splash hang, in the fix/login race condition PR",
      replies=[("1770996802.611139", U["A"])])
slack(OD, "1770996802.611139", U["A"], "got it, thx", parent_ts="1770996671.284519")

GB = "C05V5FNLB9V"
slack(GB, I["ts_decoy"], U["V"],
      "severity tiers for launch triage: P1 = urgent + high, P2 = medium, P3 = low. no-priority tickets arent triaged yet so skip them in the counts",
      replies=[("1760973540.207889", "EMPLOYEE_0026_SLACK_ID")])
slack(GB, "1760973540.207889", "EMPLOYEE_0026_SLACK_ID", "ok using that for the launch bug counts", parent_ts=I["ts_decoy"])
slack(GB, "1763997012.448319", U["A"],
      "parallel downloads went in fri night, thats the first chunk of ENG-2345. dependency order is still todo")
ZB = "C08R27X0EAH"
z359 = [("1753171206.312449", U["O"])]
slack(ZB, "1753088702.205119", U["A"],
      "the first level hitch PR from sat also caps fps off the board. can someone retry ZOM-359 on the A12", replies=z359)
slack(ZB, "1753171206.312449", U["O"], "retried ZOM-359 on the A12, still gets hot after ~20 levels", parent_ts="1753088702.205119")
z608 = [("1760637845.902769", U["O"])]
slack(ZB, "1760477048.551029", U["A"],
      "less text regen is merged, should cut most of the boot black screen (ZOM-608)", replies=z608)
slack(ZB, "1760637845.902769", U["O"], "still ~6s of black screen on the samsung A12 for ZOM-608", parent_ts="1760477048.551029")
slack(ZB, "1760735031.118839", U["O"], "pack/fix merged, has the online daily reset fix for ZOM-610 too")
slack(ZB, "1761064228.774519", U["O"], "ZOM-611 card level still resets after upgrading from the reward screen")

# --- pre-sale retest (iteration 3): iOS results in each game's bug channel (one thread per ticket), Android as Linear comments
slack(GB, "1770940961.204551", U["A"],
      "<@EMPLOYEE_0003_SLACK_ID> <@EMPLOYEE_0016_SLACK_ID> retest sweep for the sunset schedule tomorrow - every open bug on the ENG + ZOM "
      "bug view, on the store builds: DD 0.3.309, ZM 0.3.157. oliver iOS: post each DD ticket here and each ZM ticket in zombie-bugs, "
      "result in the thread. robert android: comment on each linear ticket")
PLAN = json.loads((ROOT / "work" / "retest_plan.json").read_text())


def fmt_ts(sec, n):
    return f"{sec}.{(n * 7919 + 104729) % 900000 + 100000:06d}"


RETEST_IDS = {"ios": {}, "android": {}}
start = {"ios": 1770976920, "android": 1770985800}   # 2026-02-13 10:02Z (Oliver) / 12:30Z (Robert)
step = {"ios": 420, "android": 480}
LIN_COMMENTS = []   # android results go to Linear comments (filled below, emitted in the LINEAR section)
for plat in ("ios", "android"):
    t = start[plat]
    if plat == "android":
        for i, ent in enumerate(PLAN):
            if ent[plat] == "-":
                continue
            for jj, txt in enumerate(ent["texts"][plat]):
                at = dt.datetime.fromtimestamp(t + 150 + 1260 * jj, tz=dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                cid = "cmt_" + hashlib.sha256(f"{ent['key']}|android|{jj}".encode()).hexdigest()[:20]
                LIN_COMMENTS.append((ent["key"], cid, txt, at, jj + 1))
                RETEST_IDS[plat].setdefault(ent["key"], {"comments": []})["comments"].append(cid)
            t += step[plat]
        continue
    for i, ent in enumerate(PLAN):
        code = ent[plat]
        if code == "-":
            continue
        p_ts = fmt_ts(t, i + (0 if plat == "ios" else 500))
        texts = ent["texts"][plat]
        r_ts = [fmt_ts(t + 180 + 1260 * j, i + 1000 + j * 77 + (0 if plat == "ios" else 3000)) for j in range(len(texts))]
        ch = GB if ent["key"].startswith("ENG") else ZB
        slack(ch, p_ts, U["O"], f"{ent['key']} {ent['title']} · iOS",
              replies=[(r, U["O"]) for r in r_ts])
        for r, txt in zip(r_ts, texts):
            slack(ch, r, U["O"], txt, parent_ts=p_ts)
        RETEST_IDS[plat][ent["key"]] = {"channel": ch, "parent": sid(ch, p_ts), "replies": [sid(ch, r) for r in r_ts], "parent_ts": p_ts}
        t += step[plat]
(ROOT / "work" / "retest_ids.json").write_text(json.dumps(RETEST_IDS, indent=1))

# ------------------------------------------------------------------ GMAIL
out.append("-- ===================== GMAIL =====================")


def ms(iso):
    return int(dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp() * 1000)


def rfc2822(iso):
    t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return t.strftime("%a, %d %b %Y %H:%M:%S +0000")


def thread(mbox, thrid, snippet):
    ins("gmail.gmail_threads", {"id": f"{mbox}/{thrid}", "user_email": mbox, "snippet": snippet, "history_id": None})


def msg(mbox, thrid, rfcid, iso, subject, from_name, from_email, to, cc, body, labels, irt="", refs=""):
    headers = [{"name": "Message-ID", "value": rfcid}, {"name": "Date", "value": rfc2822(iso)},
               {"name": "Subject", "value": subject}, {"name": "From", "value": f"{from_name} <{from_email}>"},
               {"name": "To", "value": ", ".join(to)}]
    if cc:
        headers.append({"name": "Cc", "value": ", ".join(cc)})
    if irt:
        headers += [{"name": "In-Reply-To", "value": irt}, {"name": "References", "value": refs}]
    ins("gmail.gmail_messages", {
        "id": f"{mbox}/{rfcid}", "thread_id": f"{mbox}/{thrid}", "user_email": mbox, "label_ids_json": j(labels),
        "snippet": body.replace("\r\n", " ")[:140], "internal_date": ms(iso), "date": iso, "size_estimate": len(body) + 900,
        "subject": subject, "from_email": from_email, "from_name": from_name, "to_json": j(to), "cc_json": j(cc),
        "bcc_json": "[]", "reply_to_json": "[]", "body_text": body, "body_html": None, "headers_json": j(headers),
        "in_reply_to": irt, "references": refs, "mbox_from": None, "attachments_meta_json": "[]"})


SUNSET_1 = ("Hi Leonard,\r\n\r\nThanks again for today. As discussed, here is what we need from your CTO for the IP listing. "
            "Buyers price game IP heavily on open defects, so please keep this to what your tracker and your code history show.\r\n\r\n"
            "Known defects schedule (one list per game lot)\r\n\r\n"
            "1. Include every open ticket on the Linear team for that game that is a defect: state Bugs or Regression, or carrying the Bug label. "
            "Open means anything not Done, Canceled or Duplicate. Leave out tickets labelled Acceptable Behavior. "
            "Group sub-issues under their parent the way your team normally presents them.\r\n"
            "2. Per row: ticket id(s), title, tier (your internal severity scale), fix status, the retest result on iOS and on Android, "
            "and the current-build status.\r\n"
            "3. Fix status comes from your code history only:\r\n"
            "   NO FIX - no merged pull request in that game's repositories says it fixes or addresses the ticket id "
            "(in its title, branch name, description or comments).\r\n"
            "   FIX MERGED - UNVERIFIED - such a pull request is merged and nothing after it shows the defect again.\r\n"
            "   FIX MERGED - REPRODUCED - such a pull request is merged, and the ticket is in Regression now or someone reported the defect "
            "again in writing after it.\r\n"
            "   If more than one merged pull request references a ticket, the latest merged one is the fix that counts; only reports "
            "dated after that latest merge make it REPRODUCED. Open or closed-unmerged pull requests do not count.\r\n"
            "4. Retest: for each defect you retest on the build currently in the stores, show what the retest found on iOS and on "
            "Android - still happens / could not make it happen / could not finish / not retested. A retest on any other build counts "
            "as not retested. Current-build status is NOT REPRODUCED only when both iOS and Android could not make it happen; "
            "otherwise it is REPRODUCES.\r\n"
            "5. Totals per lot by tier, counting only rows whose current-build status is REPRODUCES. NOT REPRODUCED rows stay on the "
            "list.\r\n"
            "6. The schedule should show your tracker as of the moment you send it; send it before our cut-off. Tickets created after "
            "the cut-off are not part of this disclosure - we pick those up in the bring-down.\r\n\r\n"
            "Our cut-off for technical items is Friday Feb 13, 12:00 PT - I'll send a calendar hold. "
            "Please send the schedule to me directly as a link, no attachments.\r\n\r\n"
            f"Best,\r\n{S_NAME}\r\nOnboarding Lead - Data & Assets | Sunset\r\n")
SUNSET_2 = ("Hi Leonard,\r\n\r\nOne addition on the technical items: the Domino Delights web/HTML5 build and its CrazyGames licence are not "
            "part of either lot. Put defects that carry your WebGL label on a separate list, and do not count them in the lot totals. "
            "Everything else in my earlier note stands.\r\n\r\n"
            f"Thanks,\r\n{S_NAME}\r\nOnboarding Lead - Data & Assets | Sunset\r\n")
S1_ISO, S2_ISO = "2026-02-12T21:48:36Z", "2026-02-13T15:20:11Z"
F1_ISO, F2_ISO = "2026-02-12T23:12:40Z", "2026-02-13T15:41:07Z"
SUBJ_S = "Harmony Games - IP listing intake (technical items)"
SUBJ_F = "Fwd: " + SUBJ_S


def quote_block(iso, body):
    t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")) - dt.timedelta(hours=8)
    head = (f"---------- Forwarded message ---------\r\nFrom: {S_NAME} <{S_EMAIL}>\r\n"
            f"Date: {t.strftime('%a, %b %-d, %Y at %-I:%M %p')}\r\nSubject: {SUBJ_S}\r\nTo: Leonard Hayes <{L_EMAIL}>\r\n\r\n")
    return head + body


FWD_1 = ("this is the list i mentioned in winddown. technical section is yours\r\n\r\n" + quote_block(S1_ISO, SUNSET_1))
FWD_2 = ("one more from sunset\r\n\r\n" + quote_block(S2_ISO, SUNSET_2) +
         f"\r\nOn Thu, Feb 12, 2026 at 3:12 PM Leonard Hayes <{L_EMAIL}> wrote:\r\n> this is the list i mentioned in winddown. technical section is yours\r\n")

def thr(iso, salt):
    m = ms(iso)
    return str((m << 20) | (int(hashlib.sha256(salt.encode()).hexdigest(), 16) & 0xFFFFF))


thr_ls = thr(S1_ISO, "ls")
thr_lf = I["thr_fwd_L"]
thr_af = I["thr_fwd_A"]  # minted from 2026-02-12T23:12:40Z
thr_rf = thr(F1_ISO, "rf")
sun1_id = I["msg_sunset_q"]
sun2_id = "<SN7PR11MB7D2B61E95C40A3@SN7PR11MB85fb.namprd11.prod.outlook.com>"
# Leonard's inbox: Sunset's original thread
thread(L_EMAIL, thr_ls, "Hi Leonard, One addition on the technical items")
msg(L_EMAIL, thr_ls, sun1_id, S1_ISO, SUBJ_S, S_NAME, S_EMAIL, [f"Leonard Hayes <{L_EMAIL}>"], [], SUNSET_1, ["INBOX", "CATEGORY_PERSONAL"])
msg(L_EMAIL, thr_ls, sun2_id, S2_ISO, "RE: " + SUBJ_S, S_NAME, S_EMAIL, [f"Leonard Hayes <{L_EMAIL}>"], [], SUNSET_2,
    ["INBOX", "CATEGORY_PERSONAL"], irt=sun1_id, refs=sun1_id)
ack_id = "<CAPBs_a7Lq2nVb0XwT9cPz3RkMfJ8sYhD4uE6gA1oNiQ5tW@mail.gmail.com>"
msg(L_EMAIL, thr_ls, ack_id, "2026-02-12T23:09:58Z", "Re: " + SUBJ_S, "Leonard Hayes", L_EMAIL, [f"{S_NAME} <{S_EMAIL}>"], [],
    "thanks - Arthur will send you the technical schedule.\r\n\r\nLeonard\r\n", ["SENT"], irt=sun1_id, refs=sun1_id)
# forward thread: Leonard SENT, Arthur INBOX, Robert INBOX (cc)
for mbox, thrid, labels in [(L_EMAIL, thr_lf, ["SENT"]), (A_EMAIL, thr_af, ["INBOX", "CATEGORY_PERSONAL", "UNREAD"]),
                            (R_EMAIL, thr_rf, ["INBOX", "CATEGORY_PERSONAL", "UNREAD"])]:
    thread(mbox, thrid, "one more from sunset")
    msg(mbox, thrid, I["msg_fwd"], F1_ISO, SUBJ_F, "Leonard Hayes", L_EMAIL, [f"Arthur Blake <{A_EMAIL}>"], [f"robert <{R_EMAIL}>"],
        FWD_1, labels)
    msg(mbox, thrid, I["msg_fwd2"], F2_ISO, SUBJ_F, "Leonard Hayes", L_EMAIL, [f"Arthur Blake <{A_EMAIL}>"], [f"robert <{R_EMAIL}>"],
        FWD_2, labels, irt=I["msg_fwd"], refs=I["msg_fwd"])

INV_SUBJ = "Invitation: Sunset - technical intake cut-off @ Fri Feb 13, 2026 12pm - 12:30pm (PST)"
UPD_SUBJ = "Updated invitation: Sunset - technical intake cut-off @ Mon Feb 16, 2026 9am - 9:30am (PST)"
GUESTS = (f"Guests\r\n{S_NAME} - organizer\r\nleonard.hayes@harmonygames.co\r\narthur.blake@harmonygames.co\r\nrobert@harmonygames.co\r\n")
INV_BODY = ("Sunset - technical intake cut-off\r\nFriday Feb 13, 2026 \u22c5 12pm \u2013 12:30pm\r\nPacific Time - Los Angeles\r\n\r\n"
            "Join with Google Meet\r\nhttps://meet.google.com/qzx-rvtd-kmw?hs=224\r\n\r\n"
            f"Organizer\r\n{S_NAME}\r\n{S_EMAIL}\r\n\r\n" + GUESTS +
            "\r\n~~//~~\r\nInvitation from Google Calendar: https://calendar.google.com/calendar/\r\n")
UPD_BODY = ("This event has been updated\r\nChanged: time\r\n\r\n\r\nSunset - technical intake cut-off\r\n"
            "Monday Feb 16, 2026 \u22c5 9am \u2013 9:30am\r\nPacific Time - Los Angeles\r\n\r\n"
            "Join with Google Meet\r\nhttps://meet.google.com/qzx-rvtd-kmw?hs=224\r\n\r\n"
            f"Organizer\r\n{S_NAME}\r\n{S_EMAIL}\r\n\r\n" + GUESTS +
            "\r\n~~//~~\r\nInvitation from Google Calendar: https://calendar.google.com/calendar/\r\n")
INV_ISO, UPD_ISO = "2026-02-12T22:05:19Z", "2026-02-13T16:05:33Z"
inv_threads = {A_EMAIL: (thr(INV_ISO, "ia"), thr(UPD_ISO, "ua")), L_EMAIL: (thr(INV_ISO, "il"), thr(UPD_ISO, "ul")),
               R_EMAIL: (thr(INV_ISO, "ir"), thr(UPD_ISO, "ur"))}
for mbox, (ti, tu) in inv_threads.items():
    thread(mbox, ti, "Sunset - technical intake cut-off Friday Feb 13, 2026")
    msg(mbox, ti, I["msg_inv"], INV_ISO, INV_SUBJ, S_NAME, S_EMAIL, [mbox], [], INV_BODY, ["INBOX", "CATEGORY_PERSONAL", "UNREAD"])
    # organizer moved the event on 2026-02-13 16:05Z without sending update emails (calendar holds the current time only)

# ------------------------------------------------------------------ GCAL
out.append("-- ===================== GCAL =====================")
att = [{"email": S_EMAIL, "organizer": True, "responseStatus": "accepted"},
       {"email": L_EMAIL, "organizer": False, "responseStatus": "accepted"},
       {"email": A_EMAIL, "organizer": False, "responseStatus": "needsAction"},
       {"email": R_EMAIL, "organizer": False, "responseStatus": "needsAction"}]
for cal, eid in [(L_EMAIL, I["evt_L"]), (A_EMAIL, I["evt_A"]), (R_EMAIL, I["evt_R"])]:
    a = [dict(x, **({"self": True} if x["email"] == cal else {})) for x in att]
    ins("gcal.gcal_events", {
        "event_id": eid, "calendar_id": cal, "summary": "Sunset - technical intake cut-off", "description": None, "location": None,
        "start_ts": "2026-02-16T17:00:00Z", "end_ts": "2026-02-16T17:30:00Z",
        "start_json": j({"dateTime": "2026-02-16T17:00:00Z"}), "end_json": j({"dateTime": "2026-02-16T17:30:00Z"}),
        "organizer_email": S_EMAIL, "creator_email": S_EMAIL, "attendees_json": j(a), "status": "confirmed", "visibility": None,
        "transparency": "opaque", "rrule_json": "[]", "recurring_event_id": None, "original_start_json": None, "sequence": 1,
        "created": INV_ISO, "updated": UPD_ISO, "hangout_link": "https://meet.google.com/qzx-rvtd-kmw?hs=224",
        "ical_uid": I["ical"], "extras_json": None})

prep_att = [{"email": L_EMAIL, "organizer": True, "responseStatus": "accepted"},
            {"email": A_EMAIL, "organizer": False, "responseStatus": "needsAction"},
            {"email": R_EMAIL, "organizer": False, "responseStatus": "accepted"}]
for cal, eid in [(L_EMAIL, "evt_4b7e19c2d05a8f3e61c9d2"), (A_EMAIL, "evt_c90d3a6e41f72b85e0a1f7"), (R_EMAIL, "evt_2e65f8b1a9c37d04f6b8e3")]:
    a = [dict(x, **({"self": True} if x["email"] == cal else {})) for x in prep_att]
    ins("gcal.gcal_events", {
        "event_id": eid, "calendar_id": cal, "summary": "data room review before sunset cut-off", "description": None, "location": None,
        "start_ts": "2026-02-13T17:00:00Z", "end_ts": "2026-02-13T17:45:00Z",
        "start_json": j({"dateTime": "2026-02-13T17:00:00Z"}), "end_json": j({"dateTime": "2026-02-13T17:45:00Z"}),
        "organizer_email": L_EMAIL, "creator_email": L_EMAIL, "attendees_json": j(a), "status": "confirmed", "visibility": None,
        "transparency": "opaque", "rrule_json": "[]", "recurring_event_id": None, "original_start_json": None, "sequence": 0,
        "created": "2026-02-12T22:14:26Z", "updated": "2026-02-12T22:14:26Z", "hangout_link": "https://meet.google.com/vhp-ksqw-tnd?hs=224",
        "ical_uid": "9f2c64e0b17a48d3a5e1c8b07d6f2a91@hg4", "extras_json": None})

# ------------------------------------------------------------------ CONTACTS
out.append("-- ===================== CONTACTS =====================")
for cid, first, job, email in [(I["cnt_3207"], "PERSON_9823_NAME", "Onboarding Lead - Data & Assets, Sunset", S_EMAIL),
                               (I["cnt_1674"], "PERSON_1674_NAME", "CEO, Sunset", "PERSON_1674_EMAIL")]:
    ins("contacts.contacts", {"contact_id": cid, "first_name": first, "last_name": "", "is_user": False, "gender": "Unknown",
                              "status": "Unknown", "job": job, "description": None, "email": email,
                              "created_at": "2026-02-12T21:55:02Z", "updated_at": "2026-02-12T21:55:02Z"})

# ------------------------------------------------------------------ DRIVE / DOCS / SHEETS / SLIDES
out.append("-- ===================== GDRIVE / GDOCS / GSHEETS / GSLIDES =====================")
SH_LAR = j([A_EMAIL, R_EMAIL])
SH_LA = j([A_EMAIL, L_EMAIL])


def dfile(fid, name, mime, parent, owner, shared, created, modified, roles=None):
    ins("gdrive.drive_files", {"id": fid, "name": name, "mime_type": mime, "parents_json": j([parent]), "owner_email": owner,
                               "shared_with_emails_json": shared, "shared_roles_json": j(roles) if roles else None,
                               "visibility": "private", "owners_json": j([owner]),
                               "modified_time": modified, "created_time": created, "trashed": False, "starred": False})


ROLES_LAR = [{"email": A_EMAIL, "role": "writer"}, {"email": R_EMAIL, "role": "writer"}]   # [U] shape — no base precedent


FOLDER = "application/vnd.google-apps.folder"
dfile(I["d_room"], "IP Sale Data Room", FOLDER, "d_63fffeb4fab5233ed5bb73", L_EMAIL, SH_LAR, "2026-02-12T21:58:40Z", "2026-02-12T22:40:12Z", ROLES_LAR)
for k, nm, c in [("d_corp", "01 Corporate", "2026-02-12T21:59:02Z"), ("d_fin", "02 Finance", "2026-02-12T21:59:09Z"),
                 ("d_legal", "03 Legal & IP", "2026-02-12T21:59:17Z"), ("d_tech", "04 Technical", "2026-02-12T21:59:25Z"),
                 ("d_assets", "05 Assets", "2026-02-12T21:59:33Z")]:
    if k == "d_tech":   # Arthur created his own section folder (owner) inside Leonard's data room
        dfile(I[k], nm, FOLDER, I["d_room"], A_EMAIL, j([L_EMAIL, R_EMAIL]), "2026-02-12T23:45:10Z", "2026-02-12T23:45:10Z")
    else:
        dfile(I[k], nm, FOLDER, I["d_room"], L_EMAIL, SH_LAR, c, c, ROLES_LAR)
dfile(I["d_decoy"], "IP Sale Data Room", FOLDER, "d_9f7ba94f7526d54d8482ba", R_EMAIL, SH_LA, "2026-02-12T22:31:18Z", "2026-02-12T22:36:02Z")
dfile(I["d_decoy_eng"], "Technical", FOLDER, I["d_decoy"], R_EMAIL, SH_LA, "2026-02-12T22:33:40Z", "2026-02-12T22:33:40Z")

for fid, nm, parent, c in [("f_3e8b0d27c4a91f56e2d7b0", "HG_Corporate_2026-02-13.pdf", I["d_corp"], "2026-02-12T23:52:10Z"),
                           ("f_b61f4c0e9a2d73e85c1a4f", "HG_Cap_Table_2026-02-13.pdf", I["d_corp"], "2026-02-12T23:53:41Z"),
                           ("f_07d9e2a5c8b41f36d0e9a7", "HG_Finance_2026-02-13.pdf", I["d_fin"], "2026-02-12T23:58:02Z")]:
    dfile(fid, nm, "application/pdf", parent, L_EMAIL, SH_LAR, c, c)

# Sheets: data room index
IDX_C, IDX_M = "2026-02-12T22:10:44Z", "2026-02-12T22:41:58Z"
dfile(I["f_index"], "IP Sale Data Room - index", "application/vnd.google-apps.spreadsheet", I["d_room"], L_EMAIL, SH_LAR, IDX_C, IDX_M)
ins("gsheets.sheets_spreadsheets", {"spreadsheet_id": I["f_index"], "title": "IP Sale Data Room - index", "owner_email": L_EMAIL,
                                    "shared_with_emails_json": SH_LAR, "visibility": "private", "drive_file_id": I["f_index"],
                                    "created_time": IDX_C, "modified_time": IDX_M})
index_grid = [
    ["Item", "Owner", "Folder", "File name", "Format", "Status"],
    ["Charter, bylaws, cap table export", "Leonard", "IP Sale Data Room / 01 Corporate", "HG_Corporate_<cut-off date>", "PDFs", "in progress"],
    ["P&L, ledger, vendor balances", "Leonard", "IP Sale Data Room / 02 Finance", "HG_Finance_<cut-off date>", "Sheet + PDFs", "in progress"],
    ["Contractor agreements + IP assignment", "Robert", "IP Sale Data Room / 03 Legal & IP", "HG_IP_Assignments", "PDFs", "todo"],
    ["Known defects schedule", "Arthur", "IP Sale Data Room / 04 Technical", "HG_Known_Defects_<cut-off date YYYY-MM-DD>",
     "Google Sheet, one tab per list: Lot A - Domino Delights / Lot B - Zombie Match 3D / Not in lot - Web", "todo"],
    ["Repo list + access for transfer", "Arthur", "IP Sale Data Room / 04 Technical", "HG_Repos", "Google Sheet", "todo"],
    ["Art + audio inventory", "Robert", "IP Sale Data Room / 05 Assets", "HG_Art_Audio", "Google Sheet", "todo"],
]
notes_grid = [
    ["Notes"],
    ["Everything goes under my IP Sale Data Room folder (Leonard's, subfolders 01-05), nothing in personal drives."],
    ["Dates in file names are the Sunset cut-off date."],
    ["When an item is filed: share the file with Sunset's onboarding lead for data & assets as viewer (file only, not the folder), then email them the link, no attachments, cc Leonard."],
    ["No player IDs, emails or device IDs anywhere in the data room."],
]
ins("gsheets.sheets_sheets", {"spreadsheet_id": I["f_index"], "sheet_id": 0, "title": "Index", "index": 0, "row_count": 1000,
                              "column_count": 26, "grid_json": j(index_grid)})
ins("gsheets.sheets_sheets", {"spreadsheet_id": I["f_index"], "sheet_id": 1, "title": "Notes", "index": 1, "row_count": 1000,
                              "column_count": 26, "grid_json": j(notes_grid)})

# Docs: asset schedule
DOC_C, DOC_M = "2026-02-12T22:01:37Z", "2026-02-12T22:27:50Z"
doc_body = ("HG IP Sale - Asset Schedule\n"
            "Leonard, Feb 12. Lots as agreed with Sunset today.\n\n"
            "Lot A - Domino Delights\n"
            "- iOS + Android apps (store listings)\n"
            "- Code: GameOfDominoes (client), game-of-dominoes-backend, liveops, liveops-dashboard-buddy\n"
            "- Tracker: Linear team ENG\n"
            "- Art + audio: per Robert's inventory\n\n"
            "Lot B - Zombie Match 3D\n"
            "- iOS + Android apps (store listings)\n"
            "- Code: match3d (client), match3d-backend, match3d-quests\n"
            "- Tracker: Linear team ZOM\n\n"
            "Not in any lot\n"
            "- Combo Fighter (founders keep it, moves to the LLC)\n"
            "- Domino Delights web/HTML5 build and the CrazyGames licence (licence ends with the wind-down)\n"
            "- MinigamePrototypes, rpg-prototype, harmony-gpt, website\n")
dfile(I["f_assets"], "HG IP Sale - Asset Schedule", "application/vnd.google-apps.document", I["d_room"], L_EMAIL, SH_LAR, DOC_C, DOC_M)
ins("gdocs.docs_documents", {"document_id": I["f_assets"], "title": "HG IP Sale - Asset Schedule", "owner_email": L_EMAIL,
                             "shared_with_emails_json": SH_LAR, "visibility": "private", "body_text": doc_body,
                             "style_runs_json": j([{"start": 0, "end": 27, "named_style": "TITLE", "list_id": None, "list_nesting": 0}]),
                             "revision_id": I["doc_rev"], "drive_file_id": I["f_assets"], "created_time": DOC_C, "modified_time": DOC_M})

# Slides: overview deck (6 slides)
SL_C, SL_M = "2026-02-12T22:31:05Z", "2026-02-12T22:52:40Z"
dfile(I["f_deck"], "HG - IP Sale Overview", "application/vnd.google-apps.presentation", I["d_room"], L_EMAIL, SH_LAR, SL_C, SL_M, ROLES_LAR)
ins("gslides.slides_presentations", {"presentation_id": I["f_deck"], "title": "HG - IP Sale Overview", "owner_email": L_EMAIL,
                                     "shared_with_emails_json": SH_LAR, "visibility": "private", "drive_file_id": I["f_deck"],
                                     "revision_id": I["slide_rev"], "created_time": SL_C, "modified_time": SL_M})
slides = [
    (I["slide1"], I["el1"], "Harmony Games\n\nIP sale overview\nFeb 12, 2026"),
    (I["slide2"], I["el2"], "What's for sale\n\nLot A - Domino Delights\nLot B - Zombie Match 3D\n\nNot included: Combo Fighter, web build, prototypes"),
    (I["slide3"], I["el3"], "Lot A - Domino Delights\n\nDomino puzzle game, iOS + Android\nClient, backend and live-ops tooling\nTracker: Linear (ENG)"),
    ("slide_9b31e0c4f7a2", "el_5d07c2a9e118", "Lot B - Zombie Match 3D\n\nMatch-3D puzzle game, iOS + Android\nClient and backend\nTracker: Linear (ZOM)"),
    (I["slide4"], I["el4"], "Known issues\n\n19 open bugs (DD 13 / ZM 6)\nFull schedule in the data room (Arthur)"),
    ("slide_e6a4d1b8c093", "el_a8c2f7e1d64b", "Process\n\nData room opens to bidders after Sunset's cut-off\nQ&A with the founders the week after"),
]
for i, (pid, eid, text) in enumerate(slides):
    ins("gslides.slides_pages", {"presentation_id": I["f_deck"], "object_id": pid, "index": i, "layout": "BLANK", "notes": None})
    ins("gslides.slides_page_elements", {"presentation_id": I["f_deck"], "page_object_id": pid, "object_id": eid, "kind": "TEXT_BOX",
                                         "text": text, "placeholder_type": None, "x_emu": 0, "y_emu": 0, "width_emu": 9144000,
                                         "height_emu": 5143500, "table_json": None, "ordinal": None})

# ------------------------------------------------------------------ GITHUB
out.append("-- ===================== GITHUB =====================")


def prc(pr, n_c, n_ev, login, iso, body, bump):
    ins("github.github_pr_comments", {"id": f"{pr}#c_{n_c}", "pr_id": pr, "author_login": login, "body": body,
                                      "created_at": iso, "updated_at": iso})
    ins("github.github_timeline_events", {"id": f"{pr}#ev_{n_ev}", "pr_id": pr, "event": "commented", "actor_login": login,
                                          "created_at": iso, "data_json": "{}"})
    if bump:
        upd("github.github_pull_requests", {"updated_at": iso}, {"id": pr})


AG, OG = "EMPLOYEE_0025_GITHUB_USERNAME", "EMPLOYEE_0003_GITHUB_USERNAME"
P5877 = "PERSON_5877_GITHUB_USERNAME"
G = "harmonygames-Games/"
prc(G + "game-of-dominoes-backend#79", 2, 6, AG, "2025-12-04T16:20:00Z",
    "note: this also clamps lives at 0 in the grant + consume endpoints, thats the server side part of ENG-2277 / ENG-2400. client side still to do", True)
prc(G + "match3d#316", 2, 7, AG, "2025-07-19T17:01:12Z",
    "also caps targetFrameRate to 30 when not on the board + stops the idle particles. should help the heating in ZOM-359", True)
prc(G + "match3d#520", 2, 8, AG, "2025-10-14T21:18:40Z",
    "TMP was regenerating every font atlas at boot, this is most of the black screen in ZOM-608", True)
prc(G + "match3d#528", 2, 5, OG, "2025-10-17T20:58:05Z",
    "this also fixes ZOM-610, daily reset was only checked on resume so players who stayed online never got it", True)
prc(G + "GameOfDominoes#1912", 2, 6, AG, "2025-11-22T03:15:27Z",
    "first part of ENG-2345 (parallel bundle downloads). dependency ordering is still open", True)
prc(G + "match3d#527", 3, 6, P5877, "2025-10-18T02:09:52Z",
    "first half of ZOM-611 is in here too (the doubled reward path was writing the old card level back). upgrade screen sync still needs work", True)
prc(G + "GameOfDominoes#1882", 3, 7, P5877, "2025-11-04T09:12:30Z",
    "not touching the lucky drop / tile dozer token farming (ENG-1838) here, that needs its own PR", None)
prc(G + "match3d#529", 3, 10, "EMPLOYEE_0004_GITHUB_USERNAME", "2025-10-17T22:14:05Z",
    "ZOM-599 (stun item vs taser) is a design call, leaving it out of this one", None)
prc(G + "GameOfDominoes#1888", 3, 7, P5877, "2025-11-11T15:40:18Z",
    "saw the char unlock FPS drop from ENG-2094 while testing this, unrelated, not fixed here", None)
prc(G + "GameOfDominoes#1832", 1, 4, P5877, "2025-05-01T23:24:16Z",
    "this also partly covers ENG-2242: epic levels now count for the win xx epic levels quest on new progress, old progress is still wrong", True)
prc(G + "match3d#542", 3, 7, P5877, "2025-10-24T13:20:41Z",
    "more of ZOM-611 in here: the upgrade screen re-reads the card level after a reward now", True)
prc(G + "match3d#521", 3, 7, P5877, "2025-10-18T02:20:44Z",
    "couldn't repro the ZOM-591 flicker on this build either, not touching it here", True)
prc(G + "GameOfDominoes#1886", 2, 9, AG, "2025-11-13T18:02:31Z",
    "unity 6 doesn't change the restart-from-lose-screen UI thing (ENG-2042), still there", True)

# ------------------------------------------------------------------ LINEAR
out.append("-- ===================== LINEAR =====================")


def lin(num, title, desc, creator, assignee, state, prio, labels, created):
    ins("linear.linear_issues", {
        "id": f"ENG-{num}", "project_id": None, "team_id": "team_ENG", "parent_id": None, "assignee_id": assignee,
        "creator_id": creator, "state_id": state, "cycle_id": None, "identifier": f"ENG-{num}", "number": num, "title": title,
        "description": desc, "priority": prio, "estimate": None, "due_date": None, "started_at": None, "completed_at": None,
        "canceled_at": None, "archived_at": None, "time_in_status_minutes": None, "labels_json": j(labels), "links_json": "[]",
        "relations_json": "[]", "state_history_json": "[]", "is_archived": False, "created_at": created, "updated_at": created})


LU, AU = "usr_63fffeb4fab5233e", "usr_cc3e90160f490686"
lin(2438, "Stuck at 8% on the loading screen after updating to 0.3.309 from the App Store",
    "Updated DD from the App Store to 0.3.309 on my iPhone and the loading bar stops at 8%. Killed the app twice, same thing.\n\nBuild: 0.3.309 (iOS)",
    LU, AU, "Bugs", 1, ["DD 2.1", "Bug"], "2026-02-10T19:41:12Z")
lin(2439, "Sunset data room - known defects schedule",
    "Tracking the known defects schedule for Sunset. When it is sent: put the link in this description and move the ticket to In Review. I close it when Sunset confirms.",
    LU, AU, "Todo", 2, [], "2026-02-12T23:20:05Z")
lin(2440, "Restore Purchases does nothing after reinstall on 0.3.309",
    "Reinstalled DD 0.3.309, tapped Restore Purchases in settings - spinner for a second then nothing. Remove ads not restored.\n\nBuild: 0.3.309 (iOS)",
    LU, None, "Bugs", 2, ["DD 2.1", "Bug"], "2026-02-13T20:31:40Z")

# android retest comments (Robert) + issue updated_at bumps; seeded ENG-2438 gets its bump in place
last_at = {}
for key, cid, txt, at, seq in LIN_COMMENTS:
    ins("linear.linear_comments", {"id": cid, "issue_id": key, "author_id": "usr_Robert", "parent_id": None, "body": txt,
                                   "is_edited": False, "created_at": at, "updated_at": at, "sequence": seq})
    last_at[key] = max(last_at.get(key, ""), at)
for key, at in sorted(last_at.items()):
    upd("linear.linear_issues", {"updated_at": at}, {"id": key})

# ------------------------------------------------------------------ TRELLO
out.append("-- ===================== TRELLO =====================")
BOARD, DOING = "640643a3fd8f3ca308d9318e", "640643a3fd8f3ca308d93196"
CARD, SL = I["card"], I["shortLink"]
CARD_NAME = "IP sale - severity tiers"
card_desc = ("Severity tiers for the defect schedule Sunset wants. Work it out per ticket in this order:\n"
             "1. Start from Linear priority: Urgent = T1, High = T2, Medium = T3, Low = T4. No priority = T3 (untriaged, treat it as medium).\n"
             "2. Hot Fix - Global Launch label = T1.\n"
             "3. Regression state = one tier more severe than steps 1-2 give (T4 -> T3, T3 -> T2, T2 -> T1). T1 stays T1.\n"
             "T1 is the worst. Nothing goes above T1.\n\n"
             "Rows: a sub-issue whose parent is also on the list goes in the parent's row (list its id there). That row takes the most "
             "severe tier of the tickets in it and the parent's fix status; show each ticket's retest results in the row, and the row is "
             "NOT REPRODUCED only if every ticket in it is.")
badges = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0,
          "checkItemsEarliestDue": None, "comments": 2, "description": True, "due": None, "dueComplete": False, "externalSource": None,
          "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}
ins("trello.trello_cards", {"id": CARD, "name": CARD_NAME, "idBoard": BOARD, "idList": DOING, "desc": card_desc, "pos": 172032.0,
                            "closed": False, "due": None, "dueComplete": False, "idMembers_json": j(["2162c1ba310341bf318f48b7"]),
                            "idLabels_json": "[]", "idShort": 456, "shortLink": None, "shortUrl": None,
                            "url": f"https://PERSON_6092_TRELLO_USERNAME.com/c/{SL}/456-ip-sale-severity-tiers",
                            "dateLastActivity": "2026-02-13T10:40:07Z", "cover_json": None, "badges_json": j(badges), "start": None,
                            "idAttachmentCover": None})
board_ref = {"id": BOARD, "name": "Harmony Games", "shortLink": "f4LGcmuh"}
card_ref = {"id": CARD, "idShort": 456, "name": CARD_NAME, "shortLink": SL}
list_ref = {"id": DOING, "name": "Doing"}
ins("trello.trello_actions", {"id": I["act_create"], "type": "createCard", "date": "2026-02-12T22:20:47Z",
                              "idMemberCreator": "2162c1ba310341bf318f48b7", "idBoard": BOARD, "idCard": CARD,
                              "data_json": j({"board": board_ref, "card": card_ref, "list": list_ref})})
for aid, member, iso, text in [
    (I["act_c1"], "3d06b73654d0c8940792514c", "2026-02-13T10:12:44Z",
     "the hot fix label was just how we tagged the ZM launch sweep, half of those were cosmetic. I'd only bump hot fix to T1 when it's already urgent or high, otherwise go by priority"),
    (I["act_c2"], "2162c1ba310341bf318f48b7", "2026-02-13T10:40:07Z", "yep fair, go with that")]:
    ins("trello.trello_actions", {"id": aid, "type": "commentCard", "date": iso, "idMemberCreator": member, "idBoard": BOARD, "idCard": CARD,
                                  "data_json": j({"board": board_ref, "card": card_ref, "idCard": CARD, "list": list_ref, "text": text,
                                                  "textData": {"emoji": {}}})})
upd("trello.trello_boards", {"dateLastActivity": "2026-02-13T10:40:07Z"}, {"id": BOARD}, "founders board shows the new card's activity")

# ------------------------------------------------------------------ CONFLUENCE
out.append("-- ===================== CONFLUENCE ===================== (re-verify after regeneration)")
conf_v1 = ("<p>Working list for the IP sale data room.</p>"
           "<h2>Corporate (Leonard)</h2><ul><li>Charter, bylaws, cap table export from Carta</li><li>Board consents</li></ul>"
           "<h2>Finance (Leonard)</h2><ul><li>P&amp;L and forecast - Jan 2026</li><li>Vendor list with balances</li></ul>"
           "<h2>Legal &amp; IP (Robert)</h2><ul><li>Contractor agreements with IP assignment</li><li>Trademark list</li></ul>"
           "<h2>Engineering (Arthur)</h2><ul><li>Repo list and access</li><li>Open bugs per game: export of the Linear Bugs column for DD and ZM, sorted by priority</li>"
           "<li>Architecture overview link</li></ul>"
           "<h2>Assets (Robert)</h2><ul><li>Art and audio source files</li></ul>")
conf_v2 = conf_v1.replace("<p>Working list for the IP sale data room.</p>",
                          "<p>Working list for the IP sale data room. Wind-down partner is Sunset (signed Feb 12); this covers their intake items.</p>")
ins("confluence.confluence_pages", {"id": "page_ip_sale_data_room", "space_id": "space_COMPANY", "parent_id": "page_company_home",
                                    "title": "IP Sale - Data Room Checklist", "body": conf_v2, "body_format": "storage",
                                    "status": "current", "version": 2, "author_id": "user_EMPLOYEE_0038",
                                    "created_at": "2026-02-12T18:05:44Z", "updated_at": "2026-02-12T21:40:18Z"})
ins("confluence.confluence_page_versions", {"id": I["ver_conf"], "page_id": "page_ip_sale_data_room", "number": 1,
                                            "title": "IP Sale - Data Room Checklist", "body": conf_v1, "author_id": "user_EMPLOYEE_0038",
                                            "message": None, "created_at": "2026-02-12T18:05:44Z"})
ins("confluence.confluence_page_versions", {"id": "ver_5c0e7a91d2b84f63a1e9c4d7b2085f16", "page_id": "page_ip_sale_data_room", "number": 2,
                                            "title": "IP Sale - Data Room Checklist", "body": conf_v2, "author_id": "user_EMPLOYEE_0038",
                                            "message": "partner signed", "created_at": "2026-02-12T21:40:18Z"})
ins("confluence.confluence_labels", {"id": "label_l054", "page_id": "page_ip_sale_data_room", "name": "data-room", "prefix": "global",
                                     "created_at": "2026-02-12T18:05:44Z"})

# ------------------------------------------------------------------ write file
header = [
    "-- Are you planning to inject? Yes",
    "-- Task: sample-task-01 (engine test) | persona: Arthur Blake <arthur.blake@harmonygames.co> | horizon: Long Horizon",
    "-- Services: slack, gmail, gcal, contacts, gdrive, gdocs, gsheets, gslides, github, linear, trello, confluence",
    "-- Statements per table: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())),
    "BEGIN;",
]
(ROOT / "01_Universe_Inject.sql").write_text("\n".join(header + out + ["COMMIT;", ""]))
print(sum(counts.values()), counts)
