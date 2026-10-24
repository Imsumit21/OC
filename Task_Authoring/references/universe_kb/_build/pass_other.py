"""Pass over GCal, Trello, Confluence, Contacts, Docs, Slides, Drive, Sheets (streamed) and Snowflake
(small tables by byte range; big tables metadata only) -> kb_cache/kb_other.json."""
import re, json, collections, datetime, difflib, gc
from common import *


def norm_title(t):
    t = (t or "").lower()
    t = re.sub(r"\.(docx?|xlsx?|pptx?|pdf|csv|md|txt|json)$", "", t)
    t = re.sub(r"^(copy of\s+)+", "", t)
    t = re.sub(r"\b(final|v\d+(\.\d+)*|draft|old|new|updated|latest|wip)\b", " ", t)
    t = re.sub(r"\b(19|20)\d\d[-_/.]?\d{0,2}[-_/.]?\d{0,2}\b", " ", t)
    t = re.sub(r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\b", " ", t)
    t = re.sub(r"\(\d+\)", " ", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def gcal_pass(out):
    C = jload(GCAL)
    cals = {c["calendar_id"]: c for c in C["calendars"]}
    ev = C["events"]
    inst = collections.defaultdict(list)
    haz = collections.defaultdict(list)
    def H(k, r):
        haz[k].append(r)
    for e in ev:
        st = (e.get("start") or {}).get("dateTime")
        inst[(e.get("ical_uid"), st)].append(e)
        en = (e.get("end") or {}).get("dateTime")
        if st and en and en <= st:
            H("end <= start", e["event_id"])
        if e.get("created") and e.get("updated") and e["updated"] < e["created"]:
            H("updated before created", e["event_id"])
        if e.get("created") and e["created"] >= CLOCK_ISO:
            H("created on/after clock", e["event_id"])
        selfs = [a.get("email") for a in e.get("attendees") or [] if a.get("self")]
        if selfs != [e["calendar_id"]]:
            H("self:true attendee != calendar owner", e["event_id"])
        if e.get("organizer_email") and e["organizer_email"] not in [a.get("email") for a in e.get("attendees") or []]:
            H("organizer not in attendees", e["event_id"])
        if e.get("calendar_id") not in cals:
            H("calendar_id without calendar row", e["event_id"])
    dis = collections.Counter()
    dis_ex = collections.defaultdict(list)
    missing_copy = []
    extra_copy = []
    for key, lst in inst.items():
        if len(lst) > 1:
            b = lst[0]
            for o in lst[1:]:
                for fld, f in (("summary", lambda x: x.get("summary")), ("end", lambda x: (x.get("end") or {}).get("dateTime")), ("status", lambda x: x.get("status")),
                               ("organizer", lambda x: x.get("organizer_email")), ("attendee set", lambda x: sorted(a.get("email") for a in x.get("attendees") or [])),
                               ("attendee responseStatus", lambda x: sorted((a.get("email"), a.get("responseStatus")) for a in x.get("attendees") or [])),
                               ("rrule", lambda x: x.get("rrule")), ("sequence", lambda x: x.get("sequence")), ("updated", lambda x: x.get("updated"))):
                    if f(o) != f(b):
                        dis[fld] += 1
                        if len(dis_ex[fld]) < 10:
                            dis_ex[fld].append([b["event_id"], o["event_id"]])
                        break
        att = set(a.get("email") for a in lst[0].get("attendees") or [])
        have = set(e["calendar_id"] for e in lst)
        miss = [a for a in att if a in cals and a not in have]
        if miss and len(missing_copy) < 2000:
            missing_copy.append([lst[0]["event_id"], miss[:3]])
        extra = [c for c in have if c not in att]
        if extra:
            extra_copy.append([lst[0]["event_id"], extra[:3]])
    # dup copies on same calendar
    dupcal = collections.Counter((e["calendar_id"], e.get("ical_uid"), (e.get("start") or {}).get("dateTime")) for e in ev)
    dupcal_n = [k for k, v in dupcal.items() if v > 1]
    # series / cohorts
    series = collections.defaultdict(lambda: {"summary": None, "starts": set(), "attendees": set(), "rrule": None, "cals": set(), "status": collections.Counter(), "eids": []})
    for e in ev:
        s = series[e.get("ical_uid")]
        s["summary"] = s["summary"] or e.get("summary")
        s["starts"].add((e.get("start") or {}).get("dateTime"))
        for a in e.get("attendees") or []:
            s["attendees"].add(a.get("email"))
        if e.get("rrule"):
            s["rrule"] = e["rrule"][0]
        s["cals"].add(e["calendar_id"])
        s["status"][e.get("status")] += 1
        if len(s["eids"]) < 3:
            s["eids"].append(e["event_id"])
    sumcount = collections.Counter()
    for uid, s in series.items():
        sumcount[norm_text(s["summary"])] += 1
    series_out = []
    for uid, s in series.items():
        st = sorted(x for x in s["starts"] if x)
        series_out.append({"ical_uid": uid, "summary": s["summary"], "instances": len(st), "copies": sum(s["status"].values()), "first": st[0] if st else None, "last": st[-1] if st else None,
                           "attendees": len(s["attendees"]), "rrule": s["rrule"], "cancelled_copies": s["status"].get("cancelled", 0), "example_event_ids": s["eids"]})
    series_out.sort(key=lambda x: -x["instances"])
    # summary-level series (same summary across uids)
    by_summary = collections.defaultdict(lambda: {"uids": 0, "instances": 0, "first": None, "last": None, "eids": []})
    for s in series_out:
        k = norm_text(s["summary"])
        b = by_summary[k]
        b["uids"] += 1
        b["instances"] += s["instances"]
        b["first"] = s["first"] if not b["first"] or (s["first"] and s["first"] < b["first"]) else b["first"]
        b["last"] = s["last"] if not b["last"] or (s["last"] and s["last"] > b["last"]) else b["last"]
        if len(b["eids"]) < 3:
            b["eids"] += s["example_event_ids"][:1]
    # per person
    per = collections.defaultdict(lambda: {"monthly": collections.Counter(), "first": None, "last": None, "organized": 0, "hours_local": [0] * 24})
    from zoneinfo import ZoneInfo
    def tzof(c):
        tz = (cals.get(c) or {}).get("time_zone") or "UTC"
        m = re.match(r"UTC([+-])(\d\d):(\d\d)", tz)
        if m:
            off = (1 if m.group(1) == "+" else -1) * (int(m.group(2)) * 60 + int(m.group(3)))
            return datetime.timezone(datetime.timedelta(minutes=off))
        try:
            return ZoneInfo(tz)
        except Exception:
            return datetime.timezone.utc
    tzc = {}
    durations, att_n, start_hours = [], [], [0] * 24
    resp = collections.Counter()
    summaries = collections.Counter()
    for (uid, st), lst in inst.items():
        e = lst[0]
        d = iso_to_dt(st)
        en = iso_to_dt((e.get("end") or {}).get("dateTime"))
        if d and en:
            durations.append(int((en - d).total_seconds() / 60))
            start_hours[d.hour] += 1
        att_n.append(len(e.get("attendees") or []))
        summaries[re.sub(r"\d+", "N", e.get("summary") or "")[:50]] += 1
        for c in lst:
            if c.get("status") == "cancelled":
                continue
            p = per[c["calendar_id"]]
            if d:
                p["monthly"][d.strftime("%Y-%m")] += 1
                s = d.isoformat()
                p["first"] = s if not p["first"] or s < p["first"] else p["first"]
                p["last"] = s if not p["last"] or s > p["last"] else p["last"]
                tz = tzc.setdefault(c["calendar_id"], tzof(c["calendar_id"]))
                p["hours_local"][d.astimezone(tz).hour] += 1
            if c.get("organizer_email") == c["calendar_id"]:
                p["organized"] += 1
            for a in c.get("attendees") or []:
                if a.get("self"):
                    resp[a.get("responseStatus")] += 1
    # index for mail matching: (norm summary, date) -> event ids
    idx = collections.defaultdict(list)
    for (uid, st), lst in inst.items():
        if st:
            idx[norm_text(lst[0].get("summary")) + "|" + st[:10]].append(lst[0]["event_id"])
    out["gcal"] = {
        "calendars": {k: {"tz": v.get("time_zone"), "summary": v.get("summary")} for k, v in cals.items()},
        "events": len(ev), "instances": len(inst), "ical_uids": len(series),
        "status": dict(collections.Counter(e.get("status") for e in ev)),
        "hazards": {k: {"count": len(v), "examples": v[:10], "all": v if len(v) <= 5000 else None} for k, v in haz.items()},
        "copy_disagreements": {"counts": dict(dis), "examples": dict(dis_ex)},
        "instances_missing_attendee_copy": {"count": len(missing_copy), "examples": missing_copy[:10]},
        "instances_with_copy_on_non_attendee_calendar": {"count": len(extra_copy), "examples": extra_copy[:10]},
        "duplicate_copy_same_calendar": {"count": len(dupcal_n), "examples": [list(x) for x in dupcal_n[:10]]},
        "series_top": series_out[:80],
        "series_with_rrule": sum(1 for s in series_out if s["rrule"]),
        "summary_groups_top": sorted([{"summary": k, **v} for k, v in by_summary.items()], key=lambda x: -x["instances"])[:60],
        "person": {k: {"monthly": dict(sorted(v["monthly"].items())), "first": v["first"], "last": v["last"], "organized": v["organized"], "hours_local": v["hours_local"]} for k, v in per.items()},
        "conventions": {"duration_min": quantiles(durations), "attendees_per_event": quantiles(att_n), "start_hour_utc": start_hours,
                         "self_response_status": dict(resp), "summary_patterns_top": dict(summaries.most_common(40)),
                         "hangout_link_share": round(sum(1 for e in ev if e.get("hangout_link")) / len(ev), 3), "transparency": dict(collections.Counter(e.get("transparency") for e in ev))},
        "mail_index": dict(idx),
        "instances_after_clock": sum(1 for (u, st) in inst if st and st >= CLOCK_ISO),
    }
    del C, ev
    gc.collect()


def trello_pass(out):
    T = jload(TRELLO)
    boards = {b["id"]: b for b in T["boards"]}
    lists = {l["id"]: l for l in T["lists"]}
    cards = {c["id"]: c for c in T["cards"]}
    members = {m["id"]: m for m in T["members"]}
    haz = collections.defaultdict(list)
    def H(k, r):
        haz[k].append(r)
    acts_by_card = collections.defaultdict(list)
    per = collections.defaultdict(lambda: {"monthly": collections.Counter(), "first": None, "last": None, "types": collections.Counter()})
    for a in T["actions"]:
        if a.get("idCard"):
            acts_by_card[a["idCard"]].append(a)
        d = a.get("date")
        p = per[a.get("idMemberCreator")]
        if d:
            p["monthly"][d[:7]] += 1
            p["first"] = d if not p["first"] or d < p["first"] else p["first"]
            p["last"] = d if not p["last"] or d > p["last"] else p["last"]
        p["types"][a["type"]] += 1
        try:
            if d and abs(int(a["id"][:8], 16) - iso_to_dt(d).timestamp()) > 120:
                H("action id timestamp != action date", a["id"])
        except Exception:
            H("action id not hex ObjectId", a["id"])
        if a.get("idCard") and a["idCard"] not in cards and a["type"] not in ("deleteCard",):
            H("action references card not in export", a["id"])
        if d and d >= CLOCK_ISO:
            H("action on/after clock", a["id"])
    ci_by_cl = collections.defaultdict(list)
    for ci in T["check_items"]:
        ci_by_cl[ci["idChecklist"]].append(ci)
    cl_by_card = collections.defaultdict(list)
    for cl in T["checklists"]:
        cl_by_card[cl["idCard"]].append(cl)
    name_ctr = collections.defaultdict(collections.Counter)
    by_list = collections.defaultdict(lambda: {"open": 0, "closed": 0, "ids": []})
    labels = {l["id"]: l for l in T["labels"]}
    label_use = collections.Counter()
    name_pat = collections.Counter()
    desc_len = []
    for c in T["cards"]:
        cid = c["id"]
        l = lists.get(c["idList"])
        if l is None:
            H("card idList missing", cid)
        elif l["idBoard"] != c["idBoard"]:
            H("card idList belongs to another board", cid)
        bl = by_list[c["idList"]]
        bl["closed" if c.get("closed") else "open"] += 1
        if len(bl["ids"]) < 5 and not c.get("closed"):
            bl["ids"].append(cid)
        if l is not None and l.get("closed") and not c.get("closed"):
            H("open card in closed (archived) list", cid)
        acts = acts_by_card.get(cid, [])
        ncom = sum(1 for a in acts if a["type"] == "commentCard")
        b = c.get("badges") or {}
        if b.get("comments") is not None and b["comments"] != ncom:
            H("badges.comments != commentCard actions", cid)
        items = [ci for cl in cl_by_card.get(cid, []) for ci in ci_by_cl.get(cl["id"], [])]
        if b.get("checkItems") is not None and b["checkItems"] != len(items):
            H("badges.checkItems != check items", cid)
        if b.get("checkItemsChecked") is not None and b["checkItemsChecked"] != sum(1 for i in items if i.get("state") == "complete"):
            H("badges.checkItemsChecked != complete items", cid)
        if acts:
            last = max(a["date"] for a in acts if a.get("date"))
            if c.get("dateLastActivity") and last > c["dateLastActivity"]:
                H("card action later than dateLastActivity", cid)
        if c.get("due") and not c.get("dueComplete") and not c.get("closed") and c["due"] < CLOCK_ISO:
            H("open card with past due date, dueComplete=false", cid)
        if l is not None and l["name"].lower() == "done" and items and any(i.get("state") != "complete" for i in items):
            H("card in Done list with incomplete checklist items", cid)
        for m in c.get("idMembers") or []:
            if m not in members:
                H("card member id not in members", cid)
        for lb in c.get("idLabels") or []:
            label_use[(labels.get(lb) or {}).get("name") or lb] += 1
        try:
            if abs(int(cid[:8], 16) - 0) and int(cid[:8], 16) > iso_to_dt(CLOCK_ISO).timestamp():
                H("card id timestamp after clock", cid)
        except Exception:
            H("card id not hex ObjectId", cid)
        name_ctr[c["idBoard"]][norm_title(c["name"])] += 1
        nm = c.get("name") or ""
        pm = re.match(r"^\[([^\]]+)\]", nm)
        name_pat["[Tag] name" if pm else ("Verb-first" if re.match(r"^(add|fix|create|update|make|implement|remove|set ?up|send|pay|check|review|prepare|finish|write|test)\b", nm, re.I) else "other")] += 1
        if c.get("desc"):
            desc_len.append(len(c["desc"]))
    dups = {}
    for bid, ctr in name_ctr.items():
        d = [[k, v] for k, v in ctr.items() if v > 1 and k]
        if d:
            dups[boards[bid]["name"]] = sorted(d, key=lambda x: -x[1])[:15]
    out["trello"] = {
        "boards": {b["id"]: {"name": b["name"], "closed": b.get("closed"), "cards": sum(1 for c in T["cards"] if c["idBoard"] == b["id"]),
                              "last_activity": max([c.get("dateLastActivity") or "" for c in T["cards"] if c["idBoard"] == b["id"]] or [""])} for b in T["boards"]},
        "lists": {l["id"]: {"board": boards[l["idBoard"]]["name"], "name": l["name"], "closed": l.get("closed"), **by_list.get(l["id"], {"open": 0, "closed": 0, "ids": []})} for l in T["lists"]},
        "hazards": {k: {"count": len(v), "examples": v[:10], "all": v if len(v) <= 5000 else None} for k, v in haz.items()},
        "duplicate_card_names_by_board": dups,
        "members": {k: v.get("fullName") for k, v in members.items()},
        "person": {k: {"monthly": dict(sorted(v["monthly"].items())), "first": v["first"], "last": v["last"], "types": dict(v["types"])} for k, v in per.items()},
        "labels": dict(label_use.most_common(40)),
        "card_name_patterns": dict(name_pat),
        "desc_len": quantiles(desc_len),
        "action_types": dict(collections.Counter(a["type"] for a in T["actions"])),
        "comment_actions": [[a["id"], a["idCard"], a["date"], a.get("idMemberCreator"), ((a.get("data") or {}).get("text") or "")[:160]] for a in T["actions"] if a["type"] == "commentCard"],
    }
    del T
    gc.collect()


def confluence_pass(out):
    F = jload(CONF)
    users = {u["id"]: u for u in F["users"]}
    pages = {p["id"]: p for p in F["pages"]}
    vers = collections.defaultdict(list)
    for v in F["page_versions"]:
        vers[v["page_id"]].append(v)
    haz = collections.defaultdict(list)
    def H(k, r):
        haz[k].append(r)
    for pid, p in pages.items():
        vs = sorted(vers.get(pid, []), key=lambda v: v["number"])
        nums = [v["number"] for v in vs]
        if nums != list(range(1, len(nums) + 1)):
            H("versions not contiguous 1..N", pid)
        if vs and vs[-1]["number"] != p.get("version"):
            H("page.version != max version", pid)
        if vs and vs[-1]["body"] != p.get("body"):
            H("latest version body != page body", pid)
        if vs and vs[-1]["title"] != p.get("title"):
            H("latest version title != page title", pid)
        if vs and vs[-1]["created_at"] != p.get("updated_at"):
            H("latest version created_at != page.updated_at", pid)
        for a, b in zip(vs, vs[1:]):
            if b["created_at"] < a["created_at"]:
                H("version timestamps out of order", pid)
        if p.get("updated_at", "") >= CLOCK_ISO:
            H("page updated on/after clock", pid)
        if p.get("author_id") and p["author_id"] not in users:
            H("page author_id not in users", pid)
        if p.get("parent_id") and p["parent_id"] not in pages:
            H("parent page missing", pid)
    for c in F["comments"]:
        if c.get("parent_id") and c["parent_id"] not in {x["id"] for x in F["comments"]}:
            H("comment parent missing", c["id"])
        if c.get("page_id") not in pages:
            H("comment page missing", c["id"])
        if c.get("author_id") not in users:
            H("comment author not in users", c["id"])
    # near-duplicate pages by body text similarity
    def txt(s):
        return re.sub(r"<[^>]+>", " ", s or "")
    toks = {pid: set(re.findall(r"[a-z]{4,}", txt(p["body"]).lower())) for pid, p in pages.items()}
    sims = []
    ids = sorted(pages)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            A, B = toks[a], toks[b]
            if A and B:
                j = len(A & B) / len(A | B)
                if j >= 0.25:
                    sims.append([a, b, round(j, 2)])
    sims.sort(key=lambda x: -x[2])
    per = collections.defaultdict(lambda: {"versions": collections.Counter(), "comments": 0, "first": None, "last": None})
    for v in F["page_versions"]:
        e = (users.get(v.get("author_id")) or {}).get("email")
        p = per[e or v.get("author_id")]
        p["versions"][v["created_at"][:7]] += 1
        p["first"] = v["created_at"] if not p["first"] or v["created_at"] < p["first"] else p["first"]
        p["last"] = v["created_at"] if not p["last"] or v["created_at"] > p["last"] else p["last"]
    for c in F["comments"]:
        e = (users.get(c.get("author_id")) or {}).get("email")
        p = per[e or c.get("author_id")]
        p["comments"] += 1
        p["first"] = c["created_at"] if not p["first"] or c["created_at"] < p["first"] else p["first"]
        p["last"] = c["created_at"] if not p["last"] or c["created_at"] > p["last"] else p["last"]
    words = [len(txt(p["body"]).split()) for p in pages.values()]
    out["confluence"] = {
        "pages": {pid: {"title": p["title"], "space": p["space_id"], "status": p["status"], "version": p.get("version"), "author": (users.get(p.get("author_id")) or {}).get("email") or p.get("author_id"),
                        "created_at": p["created_at"], "updated_at": p["updated_at"], "words": len(txt(p["body"]).split()),
                        "version_messages": [v.get("message") for v in sorted(vers.get(pid, []), key=lambda v: v["number"]) if v.get("message")][:6],
                        "comments": [c["id"] for c in F["comments"] if c["page_id"] == pid]} for pid, p in pages.items()},
        "hazards": {k: {"count": len(v), "examples": v[:10], "all": v if len(v) <= 5000 else None} for k, v in haz.items()},
        "similar_page_pairs": sims[:30],
        "person": {k: {"versions": dict(sorted(v["versions"].items())), "comments": v["comments"], "first": v["first"], "last": v["last"]} for k, v in per.items()},
        "words": quantiles(words),
        "labels": dict(collections.Counter(l["name"] for l in F["labels"]).most_common(40)),
        "synthesized_versions": sum(1 for v in F["page_versions"] if v.get("synthesized")),
        "users": {u["id"]: u.get("email") for u in F["users"]},
    }


def contacts_pass(out):
    K = jload(CONTACTS)["contacts"]
    first = collections.defaultdict(list)
    for c in K:
        first[(c.get("first_name") or "").strip().lower()].append([c["contact_id"], c.get("first_name"), c.get("last_name"), c.get("email"), c.get("job")])
    emails = collections.Counter((c.get("email") or "").lower() for c in K if c.get("email"))
    out["contacts"] = {
        "n": len(K),
        "shared_first_names": {k: v for k, v in first.items() if len(v) > 1 and k},
        "duplicate_emails": [k for k, v in emails.items() if v > 1],
        "tokenized_emails": sum(1 for c in K if re.match(r"^[A-Z]+_\d+", c.get("email") or "")),
        "with_job": [[c["contact_id"], c.get("first_name"), c.get("last_name"), c.get("email"), c.get("job")] for c in K if c.get("job")],
        "by_email": {(c.get("email") or "").lower(): c["contact_id"] for c in K if c.get("email")},
        "id_formats": dict(collections.Counter("cnt_" if c["contact_id"].startswith("cnt_") else "24hex" for c in K)),
    }


def drive_family_pass(out):
    R = jload(GDRIVE)
    files = R["drive_files"]
    drv = {f["id"]: f for f in files}
    haz = collections.defaultdict(list)
    def H(k, r):
        haz[k].append(r)
    owners = collections.Counter()
    per = collections.defaultdict(lambda: {"created": collections.Counter(), "modified_last": None, "first": None, "files": 0})
    names_by_norm = collections.defaultdict(list)
    copy_of = []
    for f in files:
        fid = f["id"]
        own = f.get("owner_email") or ""
        owners[own] += 1
        if f.get("parents"):
            for p in f["parents"]:
                if p not in drv:
                    H("parent folder missing", fid)
        if fid.startswith("f_") and f.get("mime_type") == "application/vnd.google-apps.folder":
            H("f_ id with folder mime", fid)
        if fid.startswith("d_") and f.get("mime_type") != "application/vnd.google-apps.folder":
            H("d_ id with non-folder mime", fid)
        ct, mt = f.get("created_time"), f.get("modified_time")
        if ct and mt and mt < ct:
            H("modified_time before created_time", fid)
        if mt and mt >= CLOCK_ISO:
            H("modified on/after clock", fid)
        if not re.match(r"^[^@\s]+@[^@\s]+$", own):
            H("owner_email is not an email (Resource:/token)", fid)
        if f.get("trashed"):
            H("trashed file", fid)
        if fid.startswith("f_"):
            per[own]["files"] += 1
            if ct:
                per[own]["created"][ct[:7]] += 1
                per[own]["first"] = ct if not per[own]["first"] or ct < per[own]["first"] else per[own]["first"]
            if mt:
                per[own]["modified_last"] = mt if not per[own]["modified_last"] or mt > per[own]["modified_last"] else per[own]["modified_last"]
            nm = f.get("name") or ""
            if nm.lower().startswith("copy of"):
                copy_of.append(fid)
            if not nm.lower().endswith(".json"):
                names_by_norm[norm_title(nm)].append([fid, nm, own, mt, f.get("mime_type", "").split(".")[-1].split("/")[-1]])
    # google-native mirrors
    native = {}
    for svc, path, key, idk, titlek in (("docs", GDOCS, "docs_documents", "document_id", "title"), ("slides", GSLIDES, "slides_presentations", "presentation_id", "title")):
        D = jload(path)[key]
        mis = collections.Counter()
        mex = collections.defaultdict(list)
        rows = []
        for d in D:
            i = d[idk]
            f = drv.get(i)
            if f is None:
                mis["no drive_files row"] += 1
                mex["no drive_files row"].append(i)
                continue
            if f.get("name") != d.get(titlek):
                mis["title != drive name"] += 1
                if len(mex["title != drive name"]) < 10:
                    mex["title != drive name"].append([i, d.get(titlek), f.get("name")])
            if sorted(f.get("shared_with_emails") or []) != sorted(d.get("shared_with_emails") or []):
                mis["sharing differs from drive row"] += 1
                if len(mex["sharing differs from drive row"]) < 10:
                    mex["sharing differs from drive row"].append(i)
            if f.get("owner_email") != d.get("owner_email"):
                mis["owner differs from drive row"] += 1
                mex["owner differs from drive row"].append(i)
            if f.get("modified_time") != d.get("modified_time"):
                mis["modified_time differs from drive row"] += 1
                if len(mex["modified_time differs from drive row"]) < 10:
                    mex["modified_time differs from drive row"].append(i)
            if svc == "docs":
                body = d.get("body_text") or ""
                rows.append([i, d.get(titlek), d.get("owner_email"), d.get("modified_time"), len(body), text_hash(body), len(d.get("shared_with_emails") or []), d.get("visibility")])
            else:
                txt = " ".join(el.get("text") or "" for pg in d.get("pages") or [] for el in pg.get("elements") or [])
                rows.append([i, d.get(titlek), d.get("owner_email"), d.get("modified_time"), len(d.get("pages") or []), text_hash(txt), len(d.get("shared_with_emails") or []), d.get("visibility")])
        native[svc] = {"n": len(D), "mirror_mismatch": dict(mis), "mirror_examples": {k: v[:10] for k, v in mex.items()}, "rows": rows}
        del D
        gc.collect()
    # sheets streamed
    sheets_rows = []
    smis = collections.Counter()
    smex = collections.defaultdict(list)
    tabs_total = 0
    dec = json.JSONDecoder()
    with open(GSHEETS, "r") as fh:
        buf = fh.read(1 << 20)
        pos = buf.index("[") + 1
        while True:
            while True:
                m = re.compile(r"\s*,?\s*").match(buf, pos)
                pos = m.end()
                if pos < len(buf):
                    break
                more = fh.read(1 << 22)
                if not more:
                    break
                buf = buf[pos:] + more
                pos = 0
            if pos >= len(buf) or buf[pos] == "]":
                break
            while True:
                try:
                    obj, end = dec.raw_decode(buf, pos)
                    break
                except json.JSONDecodeError:
                    more = fh.read(1 << 24)
                    if not more:
                        raise
                    buf = buf[pos:] + more
                    pos = 0
            pos = end
            if pos > (1 << 24):
                buf = buf[pos:]
                pos = 0
            sid = obj.get("spreadsheet_id") or obj.get("drive_file_id")
            tabs = obj.get("sheets") or []
            tabs_total += len(tabs)
            tinfo = []
            for t in tabs:
                g = t.get("grid") if "grid" in t else t.get("grid_json")
                nonempty = sum(1 for r in (g or []) if any(v not in ("", None) for v in r)) if isinstance(g, list) else None
                tinfo.append([t.get("title"), t.get("row_count"), nonempty])
            f = drv.get(sid)
            if f is None:
                smis["no drive_files row"] += 1
            else:
                if f.get("name") != obj.get("title"):
                    smis["title != drive name"] += 1
                    if len(smex["title != drive name"]) < 10:
                        smex["title != drive name"].append([sid, obj.get("title"), f.get("name")])
                if sorted(f.get("shared_with_emails") or []) != sorted(obj.get("shared_with_emails") or []):
                    smis["sharing differs from drive row"] += 1
                    smex["sharing differs from drive row"].append(sid)
                if f.get("modified_time") != obj.get("modified_time"):
                    smis["modified_time differs from drive row"] += 1
                    if len(smex["modified_time differs from drive row"]) < 10:
                        smex["modified_time differs from drive row"].append(sid)
            sheets_rows.append([sid, obj.get("title"), obj.get("owner_email"), obj.get("modified_time"), len(tabs), tinfo[:60], len(obj.get("shared_with_emails") or []), obj.get("visibility")])
            del obj
    native["sheets"] = {"n": len(sheets_rows), "tabs": tabs_total, "mirror_mismatch": dict(smis), "mirror_examples": {k: v[:10] for k, v in smex.items()}, "rows": sheets_rows}
    # near-duplicate titles across owners / versions
    dup_titles = []
    for k, lst in names_by_norm.items():
        if len(lst) > 1 and len(k) >= 4:
            owners_ = sorted(set(x[2] for x in lst))
            dup_titles.append({"norm": k, "n": len(lst), "owners": owners_[:6], "distinct_names": sorted(set(x[1] for x in lst))[:6],
                               "files": sorted(lst, key=lambda x: x[3] or "")[:8]})
    dup_titles.sort(key=lambda x: (-len(x["owners"]), -x["n"]))
    out["drive"] = {
        "files": sum(1 for f in files if f["id"].startswith("f_")), "folders": sum(1 for f in files if f["id"].startswith("d_")),
        "owners": dict(owners.most_common(40)),
        "mime": dict(collections.Counter(f.get("mime_type") for f in files).most_common(25)),
        "visibility": dict(collections.Counter(f.get("visibility") for f in files)),
        "hazards": {k: {"count": len(v), "examples": v[:10], "all": v if len(v) <= 5000 else None} for k, v in haz.items()},
        "copy_of": {"count": len(copy_of), "examples": copy_of[:10]},
        "duplicate_titles": dup_titles[:400],
        "duplicate_title_groups": len(dup_titles),
        "duplicate_title_groups_multi_owner": sum(1 for d in dup_titles if len(d["owners"]) > 1),
        "person": {k: {"created": dict(sorted(v["created"].items())), "first": v["first"], "modified_last": v["modified_last"], "files": v["files"]} for k, v in per.items()},
        "unreadable_resource_owned_no_share": sum(1 for f in files if (f.get("owner_email") or "").startswith("Resource:") and not f.get("shared_with_emails")),
    }
    out["native"] = native
    del R, files, drv
    gc.collect()


def snowflake_pass(out):
    idx = jload(SNOW_IDX)["payload"]["data"]["nodes"]
    tabs = {int(n[0].split("/")[2]): (n[1], n[2]) for n in idx if n[0].startswith("/tables/") and n[0].count("/") == 2}
    fh = open(SNOW, "rb")
    meta = {}
    T = {}
    for i, (s, e) in sorted(tabs.items()):
        size = e - s
        if size <= 70 * (1 << 20):
            fh.seek(s)
            t = json.loads(fh.read(size))
            rows = t.pop("rows")
            meta[t["name"]] = {"db": t["database"], "schema": t["schema"], "rows": len(rows), "comment": t.get("comment"), "columns": [c["name"] for c in t["columns"]], "bytes": size}
            if t["name"] in ("AD_SPEND_DAILY", "AD_SPEND", "UA_SPEND_UNIFIED_V2", "REVENUE_DAILY", "REVENUE_DAILY_V2", "DAILY_ACTIVE_USERS", "DAILY_METRICS_AGG",
                             "HEADCOUNT", "PAYROLL_ROSTER", "CASH_BALANCE", "MONTHLY_BURN", "FINANCE_LEDGER", "LIVE_EVENT_PERFORMANCE", "IAP_TRANSACTIONS",
                             "STORE_TRANSACTIONS", "APP_STORE_REVIEWS", "STORE_REVIEWS", "PUSH_NOTIFICATION_STATS", "USER_COHORT_RETENTION", "DIM_DATE"):
                T[t["name"]] = rows
            else:
                # date range + after-clock check on the first date-like column
                dcol = next((c for c in meta[t["name"]]["columns"] if re.search(r"date|_at$|ts$|time", c)), None)
                if dcol:
                    vals = [str(r.get(dcol)) for r in rows if r.get(dcol)]
                    meta[t["name"]]["date_col"] = dcol
                    meta[t["name"]]["date_min"] = min(vals) if vals else None
                    meta[t["name"]]["date_max"] = max(vals) if vals else None
                    meta[t["name"]]["after_clock"] = sum(1 for v in vals if v[:10] >= CLOCK_ISO[:10])
            del rows, t
            gc.collect()
        else:
            fh.seek(s)
            head = fh.read(200000).decode("utf8", "ignore")
            nm = re.search(r'"name": "([^"]+)"', head).group(1)
            cm = re.search(r'"comment": ("(?:[^"\\]|\\.)*")', head)
            meta[nm] = {"rows": None, "comment": json.loads(cm.group(1)) if cm else None, "bytes": size, "note": "too large to load; metadata only"}
    fh.close()
    haz = collections.defaultdict(list)
    def H(k, r):
        haz[k].append(r)
    # mirrored table comparisons
    def key3(r, d, g, c, co):
        return (r.get(d), r.get(g), r.get(c), r.get(co))
    a = {key3(r, "date", "game_id", "channel", "country"): r["spend_usd"] for r in T["AD_SPEND_DAILY"]}
    b = {key3(r, "date", "game_id", "network", "country"): r["spend_usd"] for r in T["AD_SPEND"]}
    c = {key3(r, "report_date", "title_id", "network_name", "country_code"): r["spend_current"] for r in T["UA_SPEND_UNIFIED_V2"]}
    for nm, other in (("AD_SPEND", b), ("UA_SPEND_UNIFIED_V2", c)):
        miss = [k for k in a if k not in other]
        diff = [k for k in a if k in other and abs((other[k] or 0) - (a[k] or 0)) > 0.01]
        if miss:
            H("AD_SPEND_DAILY key missing in " + nm, "|".join(map(str, miss[0])))
            haz["AD_SPEND_DAILY key missing in " + nm] = ["|".join(map(str, k)) for k in miss]
        if diff:
            haz["spend differs AD_SPEND_DAILY vs " + nm] = ["|".join(map(str, k)) + " %s vs %s" % (a[k], other[k]) for k in diff]
    inst_a = {key3(r, "date", "game_id", "channel", "country"): r["installs"] for r in T["AD_SPEND_DAILY"]}
    inst_b = {key3(r, "date", "game_id", "network", "country"): r["installs_reported"] for r in T["AD_SPEND"]}
    d_inst = [k for k in inst_a if k in inst_b and inst_a[k] != inst_b[k]]
    if d_inst:
        haz["installs differ AD_SPEND_DAILY vs AD_SPEND"] = ["|".join(map(str, k)) + " %s vs %s" % (inst_a[k], inst_b[k]) for k in d_inst]
    r1 = {(r["date"], r["game_id"], r["platform"]): r["total_revenue_usd"] for r in T["REVENUE_DAILY"]}
    r2 = {(r["report_date"], r["title_id"], r["platform"]): r["total_revenue_current"] for r in T["REVENUE_DAILY_V2"]}
    rd = [k for k in r1 if k in r2 and abs((r1[k] or 0) - (r2[k] or 0)) > 0.01]
    rm = [k for k in r2 if k not in r1]
    if rd:
        haz["revenue differs REVENUE_DAILY vs _V2"] = ["|".join(k) + " %s vs %s" % (r1[k], r2[k]) for k in rd]
    if rm:
        haz["REVENUE_DAILY_V2 rows absent from REVENUE_DAILY"] = ["|".join(k) for k in rm]
    d1 = {(r["date"], r["game_id"], r["platform"]): r["dau"] for r in T["DAILY_ACTIVE_USERS"]}
    d2 = {(r["metric_date"], r["title_id"], r["platform"]): r["dau"] for r in T["DAILY_METRICS_AGG"]}
    dd = [k for k in d1 if k in d2 and d1[k] != d2[k]]
    if dd:
        haz["dau differs DAILY_ACTIVE_USERS vs DAILY_METRICS_AGG"] = ["|".join(k) + " %s vs %s" % (d1[k], d2[k]) for k in dd]
    rv = [k for k in d2 if k in r1 and abs(([x for x in T["DAILY_METRICS_AGG"] if False] or [0])[0]) > 0]
    # DAILY_METRICS_AGG total revenue vs REVENUE_DAILY
    agg_rev = {(r["metric_date"], r["title_id"], r["platform"]): r["total_revenue_usd"] for r in T["DAILY_METRICS_AGG"]}
    rdf = [k for k in agg_rev if k in r1 and abs((agg_rev[k] or 0) - (r1[k] or 0)) > 0.01]
    if rdf:
        haz["total revenue differs DAILY_METRICS_AGG vs REVENUE_DAILY"] = ["|".join(k) + " %s vs %s" % (agg_rev[k], r1[k]) for k in rdf]
    # IAP vs STORE
    iap = {r["transaction_id"]: r for r in T["IAP_TRANSACTIONS"]}
    st = {r["transaction_id"]: r for r in T["STORE_TRANSACTIONS"]}
    bad = [k for k in iap if k not in st or st[k].get("is_refunded")]
    if bad:
        haz["IAP_TRANSACTIONS id not a completed STORE_TRANSACTIONS receipt"] = bad
    pdiff = [k for k in iap if k in st and abs(iap[k]["price_usd"] - st[k]["price_usd"]) > 0.001]
    if pdiff:
        haz["price differs IAP vs STORE"] = pdiff
    # reviews mirror
    ar = {r["review_id"]: r for r in T["APP_STORE_REVIEWS"]}
    sr = {r["review_id"]: r for r in T["STORE_REVIEWS"]}
    rvd = [k for k in ar if k in sr and (ar[k]["rating"] != sr[k]["rating"] or ar[k]["review_text"] != sr[k]["body"] or ar[k]["review_date"] != sr[k]["date"])]
    if rvd:
        haz["review differs APP_STORE_REVIEWS vs STORE_REVIEWS (rating/text/date)"] = rvd
    # HEADCOUNT vs PAYROLL_ROSTER
    hc = {r["roster_line_id"]: r for r in T["HEADCOUNT"]}
    pr = {r["roster_line_id"]: r for r in T["PAYROLL_ROSTER"]}
    hpd = [k for k in hc if k in pr and (hc[k]["monthly_cost_usd"] != pr[k]["monthly_cost_usd"] or hc[k]["start_month"] != pr[k]["start_month"] or hc[k]["end_month"] != pr[k]["end_month"] or hc[k]["employee_id"] != pr[k]["employee_id"])]
    if hpd:
        haz["HEADCOUNT vs PAYROLL_ROSTER line differs (cost/start/end/employee)"] = hpd
    xtitle = [r["roster_line_id"] for r in T["PAYROLL_ROSTER"] if "title" in r]
    if xtitle:
        haz["PAYROLL_ROSTER rows carry undeclared 'title' key"] = xtitle
    # cash continuity
    cb = sorted(T["CASH_BALANCE"], key=lambda r: r["month_end_date"])
    cont = []
    for p_, n_ in zip(cb, cb[1:]):
        if p_["cash_usd"] is not None and n_["cash_usd"] is not None and n_["monthly_net_burn"] is not None:
            exp = p_["cash_usd"] + n_["monthly_net_burn"]
            if abs(exp - n_["cash_usd"]) > 1:
                cont.append("%s: prev %s + net %s = %s, row says %s" % (n_["month_end_date"], p_["cash_usd"], n_["monthly_net_burn"], exp, n_["cash_usd"]))
    if cont:
        haz["CASH_BALANCE: prev cash + monthly_net_burn != cash"] = cont
    # burn vs ledger
    burn = collections.Counter()
    for r in T["MONTHLY_BURN"]:
        burn[r["month"][:7]] += r["amount_usd"]
    led_out = collections.Counter()
    for r in T["FINANCE_LEDGER"]:
        if r["amount_usd"] < 0:
            led_out[r["date"][:7]] += -r["amount_usd"]
    bl = ["%s burn %.0f vs ledger outflow %.0f" % (m, burn[m], led_out.get(m, 0)) for m in sorted(burn) if abs(burn[m] - led_out.get(m, 0)) > 5]
    if bl:
        haz["MONTHLY_BURN total != FINANCE_LEDGER outflows for month"] = bl
    # after clock
    for nm, rows in T.items():
        dcols = [k for k in (rows[0].keys() if rows else []) if re.search(r"date|month|week", k)]
        n = 0
        ex = []
        for r in rows:
            for dc in dcols:
                v = str(r.get(dc) or "")
                if v[:10] >= CLOCK_ISO[:10] and re.match(r"\d{4}-", v):
                    n += 1
                    if len(ex) < 5:
                        ex.append(r.get(list(r.keys())[0]))
                    break
        if n:
            haz["%s rows dated on/after clock" % nm] = ex + ["(n=%d)" % n]
    # duplicate keys
    for nm, k in (("LIVE_EVENT_PERFORMANCE", "event_id"), ("FINANCE_LEDGER", "entry_id"), ("IAP_TRANSACTIONS", "transaction_id")):
        ctr = collections.Counter(r[k] for r in T[nm])
        d = [x for x, v in ctr.items() if v > 1]
        if d:
            haz["%s duplicate %s" % (nm, k)] = d
    # comment numeric claims vs rows
    claims = []
    for nm, m in meta.items():
        cmt = m.get("comment") or ""
        for mm in re.finditer(r"(\d[\d,]*) (rows|runs|closed months|months|cohort rows|entries)", cmt):
            n = int(mm.group(1).replace(",", ""))
            if mm.group(2) in ("rows", "runs", "cohort rows") and m.get("rows") is not None and n != m["rows"]:
                claims.append("%s comment says %s %s, table has %s" % (nm, n, mm.group(2), m["rows"]))
    if claims:
        haz["table comment count != rows"] = claims
    lep = T["LIVE_EVENT_PERFORMANCE"]
    out["snowflake"] = {
        "tables": meta,
        "hazards": {k: {"count": len(v), "examples": v[:10], "all": v if len(v) <= 5000 else None} for k, v in haz.items()},
        "live_event_status": dict(collections.Counter(r["status"] for r in lep)),
        "live_event_failure_notes": dict(collections.Counter(r.get("failure_note") for r in lep if r.get("failure_note")).most_common(20)),
        "live_events_by_month": dict(sorted(collections.Counter(r["start_date"][:7] for r in lep).items())),
        "cash": [[r["month_end_date"], r["cash_usd"], r["monthly_net_burn"], r["runway_months"], r["headcount"], r.get("notes")] for r in cb],
        "burn_by_month": {m: round(v, 2) for m, v in sorted(burn.items())},
        "headcount_end_months": dict(sorted(collections.Counter((r["end_month"] or "")[:7] for r in T["PAYROLL_ROSTER"]).items())),
        "ledger_categories": dict(collections.Counter(r["category"] for r in T["FINANCE_LEDGER"]).most_common()),
        "ledger_by_month": dict(sorted(collections.Counter(r["date"][:7] for r in T["FINANCE_LEDGER"]).items())),
        "ledger_rows_since_2025_09": sum(1 for r in T["FINANCE_LEDGER"] if r["date"] >= "2025-09"),
        "roster": [[r["roster_line_id"], r["employee_id"], r["name"], r.get("role"), r.get("title"), r["employment_type"], r["start_month"], r["end_month"], r["monthly_cost_usd"]] for r in T["PAYROLL_ROSTER"]],
        "reviews_by_month_incident": dict(sorted(collections.Counter(r["review_date"][:7] for r in T["APP_STORE_REVIEWS"] if r.get("incident_related")).items())),
        "push_by_title": dict(collections.Counter(r["title_id"] for r in T["PUSH_NOTIFICATION_STATS"])),
        "spend_by_month_game": {k: round(v, 2) for k, v in sorted(collections.Counter({}).items())},
    }
    sp = collections.Counter()
    for r in T["AD_SPEND_DAILY"]:
        sp["%s|%s|%s" % (r["date"][:7], r["game_id"], r["channel"])] += r["spend_usd"]
    out["snowflake"]["spend_by_month_game_channel"] = {k: round(v, 2) for k, v in sorted(sp.items())}
    rev = collections.Counter()
    for r in T["REVENUE_DAILY_V2"]:
        rev["%s|%s" % (r["report_date"][:7], r["title_id"])] += r["total_revenue_current"] or 0
    out["snowflake"]["revenue_by_month_title"] = {k: round(v, 2) for k, v in sorted(rev.items())}


def main():
    out = {}
    for fn in (gcal_pass, trello_pass, confluence_pass, contacts_pass, drive_family_pass, snowflake_pass):
        fn(out)
        print(fn.__name__, "ok")
        gc.collect()
    jdump(out, CACHE + "/kb_other.json")
    print("other done")


if __name__ == "__main__":
    main()
