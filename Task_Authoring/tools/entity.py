#!/usr/bin/env python3
"""entity.py - resolve any HarmonyGames person (or bot) across every service.

Deterministic, read-only, stdlib only (Python 3.9). Run from the workspace root:

  python3 Task_Authoring/tools/entity.py build              # writes the task context's universe KB: references/universe_kb/by_universe/<universe>/entities.json
  python3 Task_Authoring/tools/entity.py resolve <query> [--json]
  python3 Task_Authoring/tools/entity.py collisions [--json]
  python3 Task_Authoring/tools/entity.py --self-test

<query> = a name, an email, or any service id (Slack user id, Gmail mailbox, GCal calendar,
Drive user id / root folder, Linear user id, GitHub login, Trello member id or username,
Confluence id / account_id, contact id, persona_key). Exact (case-insensitive) match first;
if nothing matches exactly, entities whose names contain the query are listed as candidates.

JOIN RULES (what `build` does; every identity records its `join` basis)
  1. Seeds: the 19 personas of Task_Authoring/references/persona_roster_v2.json (17 also in
     Evals/references/persona/roster.json = usable in tasks; thomas and tim_steudler are
     marked usable_in_tasks=false).
  2. exact_email - a service record whose email (Slack users.email, Gmail mailbox, GCal
     calendar owner_email, Drive user email / file owner, Linear email, GitHub email,
     Confluence email, Contacts email) equals an entity's email, case-insensitively.
     Token emails (PERSON_3233_EMAIL, EMPLOYEE_0032_EMAIL ...) are matched exactly as strings.
  3. exact_name - a record without an email whose display name (Slack real_name, GitHub
     name, Trello fullName) equals exactly one entity's canonical name, case-insensitively,
     and the name is not a mononym that is also another entity's first name.
  4. exact_name+username_localpart - an ambiguous mononym (e.g. Trello "Thomas") joins only
     when the record's username also equals the email local part of exactly that entity.
  5. Anything else is never merged: a placeholder/opaque record becomes its own entity
     (kind unidentified/bot/service), and any record with more than one plausible entity
     is listed under `unresolved` with its candidates and the reason.
  Token numbers (EMPLOYEE_0032 in user_EMPLOYEE_0032, EMPLOYEE_0032_EMAIL, ...) are never a
  join basis; groups of entities that share a token number are reported under
  `unresolved` (token_link) and `collisions.tokens_mapping_to_several_entities`.

Last activity per service (cheap, from base exports): Slack last post, Gmail mailbox last
message, GCal last event start on the entity's calendar at or before the clock, Drive last
modified owned file, Linear last updated issue as creator/assignee, GitHub last PR / review /
comment / commit / timeline event, Trello last action, Confluence last page/version/comment.

Reads the base exports one at a time (read-only) plus the persona_view pv_* caches.
Writes only Task_Authoring/references/universe_kb/entities.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import persona_view as pv  # noqa: E402

OUT = pv.BUNDLE / "references" / "universe_kb" / "entities.json"
ASK = pv.BUNDLE / "references" / "Ask_Carriers.md"
SERVICES = ("roster", "slack", "gmail", "gcal", "gdrive", "linear", "github", "trello", "confluence", "contacts")
TOKEN_RE = re.compile(r"(EMPLOYEE|PERSON|SVC|SLACK_BOT|STAFF)_(\d+)", re.I)
PLACEHOLDER = re.compile(r"^(?:(EMPLOYEE|PERSON|SVC|SLACK_BOT|STAFF)_\d+(_[A-Z_]+)?|\[EMAIL_\d+\]|U[A-Z0-9]{8,11}|USLACKBOT)$", re.I)


def _is_real_name(n) -> bool:
    if not n or not isinstance(n, str):
        return False
    n = n.strip()
    return bool(n) and not PLACEHOLDER.match(n) and "@" not in n and not n.startswith("Resource:")


def _local(e: str) -> str | None:
    return e.split("@", 1)[0].casefold() if e and "@" in e else None


def _first(n: str) -> str:
    return n.strip().split()[0].casefold()


def _d(v):
    return str(v)[:10] if v else None


def _max(a, b):
    return b if a is None or (b is not None and b > a) else a


# ---------------------------------------------------------------- build

class Builder:
    def __init__(self):
        self.ents = {}          # entity_id -> entity
        self.by_email = {}      # casefold email -> entity_id
        self.unresolved = []
        self.flags = []

    def new(self, eid: str, kind: str, email: str | None = None, name: str | None = None) -> dict:
        e = self.ents.get(eid)
        if e is None:
            e = {"entity_id": eid, "canonical_name": name if _is_real_name(name) else None, "kind": kind,
                 "emails": [], "persona": None, "names": [], "identities": {s: [] for s in SERVICES},
                 "last_activity": {}, "flags": []}
            self.ents[eid] = e
        if email and email not in e["emails"]:
            e["emails"].append(email)
            self.by_email.setdefault(email.casefold(), eid)
        if _is_real_name(name) and name not in e["names"]:
            e["names"].append(name)
        return e

    def by_mail(self, email, kind="person", name=None) -> dict:
        eid = self.by_email.get(str(email).casefold())
        if eid:
            e = self.ents[eid]
            if _is_real_name(name) and name not in e["names"]:
                e["names"].append(name)
            return e
        k = kind
        s = str(email)
        if s.startswith("Resource:"):
            k = "resource"
        elif s.upper().startswith("SVC_"):
            k = "service"
        return self.new(f"email:{s}", k, s, name)

    def add(self, e: dict, service: str, ident: dict, join: str):
        ident = dict(ident, join=join)
        e["identities"][service].append(ident)

    def name_index(self):
        """casefold canonical/known real names -> entity ids (built from authoritative sources)."""
        idx = defaultdict(set)
        firsts = defaultdict(set)
        for eid, e in self.ents.items():
            for n in e["names"]:
                idx[n.casefold()].add(eid)
                firsts[_first(n)].add(eid)
        return idx, firsts

    def join_by_name(self, service: str, ident: dict, name, username=None, kind="person", opaque_id=None):
        """Rules 3-5 for records without an email."""
        oid = opaque_id or ident.get("id") or ident.get("login")
        if not _is_real_name(name):
            e = self.new(f"{service}:{oid}", kind, None, None)
            self.add(e, service, ident, "own_record (no email, placeholder or no name)")
            return e
        idx, firsts = self.name_index()
        exact = idx.get(name.casefold(), set())
        mononym = len(name.split()) == 1
        others_first = firsts.get(_first(name), set()) - exact
        if len(exact) == 1 and not (mononym and others_first):
            e = self.ents[next(iter(exact))]
            self.add(e, service, ident, "exact_name")
            return e
        cands = sorted(exact | (others_first if mononym else set()))
        if username:
            hit = [c for c in cands if any(_local(m) == username.casefold() for m in self.ents[c]["emails"])]
            if len(hit) == 1 and hit[0] in exact:
                e = self.ents[hit[0]]
                self.add(e, service, ident, "exact_name+username_localpart")
                return e
        if not cands:
            # first-name-only candidates are still worth listing for a multi-token name
            cands = sorted(firsts.get(_first(name), set())) if not mononym else []
            e = self.new(f"{service}:{oid}", kind, None, name)
            self.add(e, service, ident, "own_record (name matches no entity)")
            if cands:
                self.unresolved.append({"type": "name_first_only", "service": service, "record": ident,
                                        "name": name, "candidates": cands, "entity_created": e["entity_id"],
                                        "reason": f"'{name}' matches no entity exactly; same first name as {cands}"})
            return e
        e = self.new(f"{service}:{oid}", kind, None, name)
        self.add(e, service, ident, "own_record (ambiguous name)")
        self.unresolved.append({"type": "ambiguous_name", "service": service, "record": ident, "name": name,
                                "candidates": cands, "entity_created": e["entity_id"],
                                "reason": (f"mononym '{name}' is an exact name of {sorted(exact)} and the first name of "
                                           f"{sorted(others_first)}" if mononym else f"'{name}' is the exact name of {cands}")})
        return e


def build() -> dict:
    b = Builder()
    u = pv.Universe()

    # 1. roster seeds
    for p in pv.personas():
        e = b.new(f"email:{p['email']}", "person", p["email"], p["name"])
        e["canonical_name"] = p["name"]
        e["persona"] = {k: p[k] for k in ("persona_key", "role", "department", "usable_in_tasks", "roster_source")}
        b.add(e, "roster", {"persona_key": p["persona_key"], "email": p["email"], "name": p["name"]}, "roster")

    # names from authoritative directories first (contacts, confluence, slack) so name joins can use them
    contacts = pv._load(pv.OTHER / "contacts" / "contacts.json")["contacts"]
    for c in contacts:
        full = " ".join(x for x in (c.get("first_name"), c.get("last_name")) if x).strip()
        ident = {"contact_id": c["contact_id"], "name": full, "email": c.get("email"), "job": c.get("job"),
                 "is_user": c.get("is_user")}
        if c.get("email"):
            e = b.by_mail(c["email"], name=full)
            b.add(e, "contacts", ident, "exact_email")
        else:
            b.join_by_name("contacts", ident, full, opaque_id=c["contact_id"])
    conf = pv._load(pv.OTHER / "confluence" / "confluence_working.json")
    conf_last = defaultdict(lambda: None)
    for coll, field in (("pages", "updated_at"), ("page_versions", "created_at"), ("comments", "created_at")):
        for x in conf.get(coll, []):
            conf_last[x.get("author_id")] = _max(conf_last[x.get("author_id")], x.get(field))
    for c in conf["users"]:
        ident = {"id": c["id"], "account_id": c.get("account_id"), "email": c.get("email"),
                 "display_name": c.get("display_name"), "is_active": c.get("is_active"),
                 "last_activity": _d(conf_last[c["id"]])}
        e = b.by_mail(c["email"], name=c.get("display_name")) if c.get("email") else None
        if e is not None:
            b.add(e, "confluence", ident, "exact_email")
        else:
            b.join_by_name("confluence", ident, c.get("display_name"))
    del conf

    s = u.slack()
    for uid, x in sorted(s["users"].items()):
        st = s["user_stats"].get(uid)
        ident = {"id": uid, "name": x.get("name"), "real_name": x.get("real_name"), "email": x.get("email"),
                 "is_bot": x.get("is_bot"), "deleted": x.get("deleted"), "messages": st[0] if st else 0,
                 "first_post": pv.ts_date(st[1]) if st else None, "last_post": pv.ts_date(st[2]) if st else None}
        kind = "bot" if x.get("is_bot") or uid.startswith("SLACK_BOT") else "service" if uid.startswith("SVC_") else "person"
        if x.get("email"):
            e = b.by_mail(x["email"], name=x.get("real_name"))
            b.add(e, "slack", ident, "exact_email")
        else:
            b.join_by_name("slack", ident, x.get("real_name"), kind=kind if kind != "person" else "unidentified")

    # gmail mailboxes (+ filename aliases from the thread index)
    g = u.gmail()
    alias = defaultdict(Counter)
    for tid, (mb, _n, _f, _l, f) in g["threads"].items():
        m = re.match(r"(.+@harmonygames\.co)_\d+\.json$", f)
        if m:
            alias[mb][m.group(1)] += 1
    for mb in u.gmail_mailboxes():
        bx = g["mailboxes"].get(mb, {})
        ident = {"mailbox": mb, "threads": bx.get("threads", 0), "messages": bx.get("messages", 0),
                 "first": _d(bx.get("first")), "last": _d(bx.get("last")),
                 "thread_filename_alias": sorted(alias[mb])}
        e = b.by_mail(mb)
        b.add(e, "gmail", ident, "exact_email")
        if "@" not in mb:
            e["flags"].append("tokenized Gmail mailbox: the data does not prove which person owns it")

    # gcal
    gc = u.gcal()
    cal_last, cal_n = defaultdict(lambda: None), Counter()
    for eid, ev in gc["events"].items():
        cal_n[ev[0]] += 1
        d = pv.parse_dt(ev[3])
        if d and d <= getattr(pv, "DATA_CLOCK", pv.CLOCK):   # what exists/visible: the data horizon
            cal_last[ev[0]] = _max(cal_last[ev[0]], ev[3])
    for cid, c in sorted(gc["calendars"].items()):
        ident = {"calendar_id": cid, "owner_email": c["owner"], "summary": c["summary"], "events": cal_n[cid],
                 "last_event_before_clock": _d(cal_last[cid])}
        e = b.by_mail(c["owner"])
        b.add(e, "gcal", ident, "exact_email")

    u.drop("slack", "gmail", "gcal")  # keep one large structure in memory at a time

    # drive users (+ root folders and owned-file stats from the export)
    roots, owned, last_mod = defaultdict(list), Counter(), defaultdict(lambda: None)
    recips, drive_users = Counter(), []
    for coll, f in pv.iter_records(pv.OTHER / "gdrive" / "data.json", {"id", "owner_email", "modified_time", "parents",
                                                                       "email", "display_name", "shared_with_emails"}):
        if coll == "drive_users":
            drive_users.append(f)
            continue
        if coll != "drive_files":
            continue
        for r in f.get("shared_with_emails") or []:
            recips[r] += 1
        o = f.get("owner_email")
        owned[o] += 1
        last_mod[o] = _max(last_mod[o], f.get("modified_time"))
        if not f.get("parents") and f["id"].startswith("d_"):
            roots[o].append(f["id"])
    for x in drive_users:
        ident = {"id": x["id"], "email": x["email"], "display_name": x.get("display_name"), "root_folders": roots[x["email"]],
                 "owned_items": owned[x["email"]], "last_modified": _d(last_mod[x["email"]])}
        e = b.by_mail(x["email"])
        b.add(e, "gdrive", ident, "exact_email")
    for r, cnt in sorted(recips.items()):
        e = b.by_mail(r)
        same = [i for i in e["identities"]["gdrive"] if i.get("email") == r]
        if same:
            same[0]["files_shared_with"] = cnt
        else:
            b.add(e, "gdrive", {"share_recipient": r, "files_shared_with": cnt}, "exact_email")

    # linear
    lin = pv._load(pv.OTHER / "linear" / "data.json")
    lin_last = defaultdict(lambda: None)
    for i in lin["issues"]:
        for k in ("creator_id", "assignee_id"):
            if i.get(k):
                lin_last[i[k]] = _max(lin_last[i[k]], i.get("updated_at"))
    for c in lin.get("comments") or []:
        lin_last[c.get("author_id")] = _max(lin_last[c.get("author_id")], c.get("created_at"))
    for x in lin["users"]:
        ident = {"id": x["id"], "email": x.get("email"), "name": x.get("name"), "is_active": x.get("is_active"),
                 "last_activity": _d(lin_last[x["id"]])}
        if x.get("email"):
            e = b.by_mail(x["email"], name=x.get("name"))
            b.add(e, "linear", ident, "exact_email")
        else:
            b.join_by_name("linear", ident, x.get("name"))
        if " " in x["id"]:
            b.flags.append({"type": "id_with_space", "service": "linear", "id": x["id"]})
    del lin

    # github
    gh_last, gh_users = defaultdict(lambda: None), []
    rules = {"pull_requests": ("author_login", "created_at"), "reviews": ("author_login", "submitted_at"),
             "review_comments": ("author_login", "created_at"), "pull_request_comments": ("author_login", "created_at"),
             "commits": ("author_login", "authored_date"), "timeline_events": ("actor_login", "created_at")}
    for coll, x in pv.iter_records(pv.GITHUB, {"login", "name", "email", "type", "author_login", "actor_login", "created_at",
                                               "submitted_at", "authored_date"}, {"users", *rules}):
        if coll == "users":
            gh_users.append(x)
            continue
        who, when = rules[coll]
        w = x.get(when)
        if x.get(who) and w and w != "None":
            gh_last[x[who]] = _max(gh_last[x[who]], w)
    for x in gh_users:
        ident = {"login": x["login"], "name": x.get("name"), "email": x.get("email"), "type": x.get("type"),
                 "last_activity": _d(gh_last[x["login"]])}
        kind = {"Bot": "bot", "Organization": "organization"}.get(x.get("type"), "person")
        if x.get("email"):
            e = b.by_mail(x["email"], kind=kind, name=None)
            b.add(e, "github", ident, "exact_email")
            if _is_real_name(x.get("name")) and e["canonical_name"] and x["name"].casefold() != e["canonical_name"].casefold():
                msg = f"GitHub {x['login']} joined by email but shows name '{x['name']}' (entity is {e['canonical_name']})"
                e["flags"].append(msg)
                b.flags.append({"type": "name_mismatch_on_email_join", "service": "github", "id": x["login"], "detail": msg})
        else:
            b.join_by_name("github", ident, x.get("name"), kind=kind if kind != "person" else "unidentified",
                           opaque_id=x["login"])

    # trello
    tr = pv._load(pv.OTHER / "trello" / "data.json")
    tr_last = defaultdict(lambda: None)
    for a in tr["actions"]:
        tr_last[a.get("idMemberCreator")] = _max(tr_last[a.get("idMemberCreator")], a.get("date"))
    members = tr["members"]
    del tr
    for x in members:
        ident = {"id": x["id"], "username": x.get("username"), "fullName": x.get("fullName"),
                 "last_activity": _d(tr_last[x["id"]])}
        e = b.join_by_name("trello", ident, x.get("fullName"), username=x.get("username"))
        un = (x.get("username") or "").casefold()
        if e["emails"] and un and not PLACEHOLDER.match(un) and all(_local(m) != un for m in e["emails"]):
            other = [k for k, v in b.ents.items() if any(_local(m) == un for m in v["emails"])]
            if other:
                b.flags.append({"type": "trello_username_points_elsewhere", "id": x["id"], "username": un,
                                "joined_to": e["entity_id"], "username_matches": other})

    # ---- per-entity last activity + canonical names
    for e in b.ents.values():
        la = {}
        for i in e["identities"]["slack"]:
            la["slack"] = _max(la.get("slack"), i.get("last_post"))
        for i in e["identities"]["gmail"]:
            la["gmail"] = _max(la.get("gmail"), i.get("last"))
        for i in e["identities"]["gcal"]:
            la["gcal"] = _max(la.get("gcal"), i.get("last_event_before_clock"))
        for i in e["identities"]["gdrive"]:
            la["gdrive"] = _max(la.get("gdrive"), i.get("last_modified"))
        for svc in ("linear", "github", "trello", "confluence"):
            for i in e["identities"][svc]:
                la[svc] = _max(la.get(svc), i.get("last_activity"))
        e["last_activity"] = {k: v for k, v in la.items() if v}
        if not e["canonical_name"]:
            e["canonical_name"] = e["names"][0] if e["names"] else None
        if e["kind"] == "person" and not e["canonical_name"] and not any("@" in m for m in e["emails"]):
            e["kind"] = "unidentified"
        e["services_present"] = [s for s in SERVICES if e["identities"][s]]
        e["identities"] = {k: v for k, v in e["identities"].items() if v}

    tokens = token_groups(b.ents)
    for t, grp in tokens.items():
        if len(grp["entities"]) > 1:
            b.unresolved.append({"type": "token_link", "token": t, "candidates": sorted(grp["entities"]),
                                 "records": grp["records"],
                                 "reason": "same token number across services but no shared exact email/name: not joined"})
    ents = sorted(b.ents.values(), key=lambda e: (e["persona"] is None, e["kind"] != "person",
                                                  (e["canonical_name"] or "~").casefold(), e["entity_id"]))
    data = {"_meta": {"generated_by": "Task_Authoring/tools/entity.py build", "clock": pv.CLOCK.isoformat(),
                      "data_clock": getattr(pv, "DATA_CLOCK", pv.CLOCK).isoformat(),  # seed bound vs data horizon
                      "join_rules": ["roster", "exact_email", "exact_name", "exact_name+username_localpart",
                                     "own_record"],
                      "entity_count": len(ents), "kinds": dict(Counter(e["kind"] for e in ents)),
                      "sources": [str(p.relative_to(pv.WS)) if p.is_relative_to(pv.WS) else str(p) for p in (
                          pv.ROSTER_V1, pv.ROSTER_V2, pv.OTHER / "slack" / "users.json", pv.GMAIL / "users.json",
                          pv.OTHER / "gcal" / "data.json", pv.OTHER / "gdrive" / "data.json",
                          pv.OTHER / "linear" / "data.json", pv.GITHUB, pv.OTHER / "trello" / "data.json",
                          pv.OTHER / "confluence" / "confluence_working.json", pv.OTHER / "contacts" / "contacts.json")]},
            "entities": ents, "unresolved": b.unresolved, "integrity_flags": b.flags}
    context = globals().get("TASK_CONTEXT")
    if context:
        source = context["source"]
        # No context hash: it covers machine paths and the KB status, so it would change a committed KB on every rebuild.
        data["_meta"].update(source_fingerprint=source["fingerprint"],
                             universe=context.get("universe", {}).get("key") or source.get("universe"))
        if source.get("mode") == "universe":
            data["_meta"].update(clock=source.get("data_clock") or data["_meta"]["clock"], build="per-universe-v1",
                                 data_clock=source.get("data_clock"), reference_clock=source.get("data_clock"),
                                 assigned_freeze=context["freeze_utc"], seed_bound=context["freeze_utc"])
    data["collisions"] = collisions(data)
    unid = Counter()
    for e in ents:
        if e["kind"] == "unidentified":
            unid[e["entity_id"].split(":", 1)[0]] += 1
    data["_meta"]["counts"] = {"unidentified_entities_by_origin": dict(unid),"unresolved": Counter(x["type"] for x in data["unresolved"]),
                               "integrity_flags": Counter(x["type"] for x in data["integrity_flags"]),
                               "collisions": {k: len(v) for k, v in data["collisions"].items()}}
    if context and (context["source"].get("kb_status") != "unavailable"):
        # A build may target a not-yet-bound universe (no KB to validate against); a read never may.
        data = _validate(data)
    return data


def token_groups(ents: dict) -> dict:
    groups = defaultdict(lambda: {"entities": set(), "records": []})
    for eid, e in ents.items():
        vals = []
        for svc, ids in e["identities"].items():
            for i in ids:
                for k in ("id", "login", "mailbox", "email", "calendar_id", "username", "owner_email"):
                    v = i.get(k)
                    if isinstance(v, str):
                        vals.append((svc, k, v))
        for m in e["emails"]:
            vals.append(("email", "email", m))
        for svc, k, v in vals:
            for pre, num in TOKEN_RE.findall(v):
                if pre.upper() == "STAFF":
                    continue  # Confluence-local numbering, unrelated to the shared token space
                t = f"{pre.upper()}_{int(num):04d}"
                groups[t]["entities"].add(eid)
                rec = f"{svc}.{k}={v}"
                if rec not in groups[t]["records"]:
                    groups[t]["records"].append(rec)
    return {t: {"entities": sorted(g["entities"]), "records": g["records"]} for t, g in sorted(groups.items())}


def collisions(data: dict) -> dict:
    ents = [e for e in data["entities"] if e["kind"] in ("person", "unidentified")]
    by_id = {e["entity_id"]: e for e in data["entities"]}
    first, last = defaultdict(set), defaultdict(set)
    for e in ents:
        for n in [e["canonical_name"]] if e["canonical_name"] else []:
            parts = n.split()
            first[parts[0].casefold()].add(e["entity_id"])
            if len(parts) > 1:
                last[parts[-1].casefold()].add(e["entity_id"])

    def label(eid):
        e = by_id[eid]
        return f"{e['canonical_name'] or '?'} <{', '.join(e['emails']) or eid}>" + (
            f" [persona {e['persona']['persona_key']}]" if e["persona"] else "")

    out = {
        "shared_first_names": {k: [label(x) for x in sorted(v)] for k, v in sorted(first.items()) if len(v) > 1},
        "shared_last_names": {k: [label(x) for x in sorted(v)] for k, v in sorted(last.items()) if len(v) > 1},
    }
    # handles / email local parts that equal another entity's local part or mononym
    locals_ = defaultdict(set)
    for e in data["entities"]:
        for m in e["emails"]:
            if _local(m):
                locals_[_local(m)].add(e["entity_id"])
    look = []
    for e in data["entities"]:
        for i in e["identities"].get("slack", []):
            h = str(i.get("name") or "").casefold()
            for other in sorted(locals_.get(h, set()) - {e["entity_id"]}):
                look.append(f"Slack handle '{i['name']}' ({i['id']}) belongs to {label(e['entity_id'])} but equals the "
                            f"mailbox local part of {label(other)}")
        for i in e["identities"].get("gmail", []):
            for a in i.get("thread_filename_alias", []):
                if a != i["mailbox"]:
                    hit = sorted(locals_.get(_local(a), set()) - {e["entity_id"]})
                    look.append(f"Gmail thread files of {i['mailbox']} are named '{a}_*'"
                                + (f"; '{_local(a)}@' is also the mailbox of {[label(h) for h in hit]}" if hit else ""))
    prefixes = []
    keys = sorted(k for k in locals_ if k)
    for a in keys:
        for b_ in keys:
            if a != b_ and (b_.startswith(a + ".") or b_.startswith(a) and b_[len(a):].isalpha() and len(a) >= 5):
                prefixes.append(f"'{a}@' vs '{b_}@': {[label(x) for x in sorted(locals_[a])]} / "
                                f"{[label(x) for x in sorted(locals_[b_])]}")
    out["lookalike_handles_and_aliases"] = look
    out["lookalike_email_local_parts"] = prefixes
    toks = token_groups({e["entity_id"]: e for e in data["entities"]})
    out["tokens_mapping_to_several_entities"] = {
        t: {"entities": [label(x) for x in g["entities"]], "records": g["records"]}
        for t, g in toks.items() if len(g["entities"]) > 1}
    # same entity, several ids in one service
    multi = []
    for e in data["entities"]:
        for svc, ids in e["identities"].items():
            if svc != "roster" and len(ids) > 1:
                multi.append(f"{label(e['entity_id'])}: {len(ids)} {svc} identities "
                             f"{[i.get('id') or i.get('login') or i.get('contact_id') or i.get('mailbox') or i.get('calendar_id') for i in ids]}"
                             f" (joins: {[i['join'] for i in ids]})")
    out["several_ids_in_one_service"] = multi
    # persona role vs Contacts job
    roles = []
    for e in data["entities"]:
        if e["persona"]:
            for c in e["identities"].get("contacts", []):
                if c.get("job") and c["job"] != e["persona"]["role"]:
                    roles.append(f"{label(e['entity_id'])}: roster role '{e['persona']['role']}' vs Contacts job '{c['job']}'")
    out["persona_role_vs_contacts_job"] = roles
    jobs = defaultdict(list)
    for e in data["entities"]:
        for c in e["identities"].get("contacts", []):
            if c.get("job"):
                jobs[c["job"]].append(label(e["entity_id"]))
    out["shared_contact_job_titles"] = {k: v for k, v in sorted(jobs.items()) if len(v) > 1}
    return out


# ---------------------------------------------------------------- load / resolve

def _validate(data):
    """Apply the selected universe's KB contract; a missing KB is an explicit stop, never another KB."""
    import runtime_context
    unavailable = getattr(runtime_context, "KBUnavailable", runtime_context.ContextError)
    try:
        return runtime_context.validate_kb(data, globals())
    except unavailable as exc:
        raise SystemExit(f"error: {exc}") from exc


def load() -> dict:
    path = OUT
    context = globals().get("TASK_CONTEXT")
    source = (context or {}).get("source") or {}
    generated = _generated_entities(context)
    if not path.exists() and generated:
        path = generated
    elif not path.exists() and context and source.get("mode") == "universe" \
            and source.get("kb_status") != "unavailable" and source.get("kb_path"):
        path = Path(source["kb_path"]) / "entities.json"
    if not path.exists():
        reason = _kb_reason()
        if reason:
            raise SystemExit(f"error: {reason}")
        raise SystemExit(f"error: {OUT.relative_to(pv.WS)} missing; run `python3 Task_Authoring/tools/entity.py build`")
    data = pv._load(path)
    if context and source.get("kb_status") == "unavailable":
        if generated and Path(path).resolve() == Path(generated).resolve():
            # A records-built entities file whose _meta matches the selected universe (entities_file).
            return data
        raise SystemExit(f"error: {_kb_reason()}")
    return _validate(data)


def _generated_entities(context):
    if not context:
        return None
    try:
        import runtime_context
    except ImportError:
        return None
    return runtime_context.entities_file(context)


def _kb_reason():
    context = globals().get("TASK_CONTEXT")
    source = (context or {}).get("source") or {}
    if context and source.get("kb_status") == "unavailable":
        return source.get("reason") or (f"No knowledge base is bound to the {source.get('universe') or 'selected'} "
                                        "universe; rebuild it before using KB facts")
    return None


def _all_keys(e: dict) -> set:
    keys = {e["entity_id"].casefold()}
    keys |= {m.casefold() for m in e["emails"]}
    keys |= {n.casefold() for n in e["names"]}
    if e["canonical_name"]:
        keys.add(e["canonical_name"].casefold())
    if e["persona"]:
        keys.add(e["persona"]["persona_key"].casefold())
    for svc, ids in e["identities"].items():
        for i in ids:
            for k, v in i.items():
                if k in ("join", "messages", "threads", "events", "owned_items", "is_bot", "deleted", "is_active",
                         "is_user", "type", "summary", "job") or v is None:
                    continue
                if isinstance(v, str):
                    keys.add(v.casefold())
                elif isinstance(v, list):
                    keys |= {str(x).casefold() for x in v}
    keys.discard("")
    return keys


def resolve(data: dict, q: str) -> dict:
    qq = q.strip().casefold()
    exact = [e for e in data["entities"] if qq in _all_keys(e)]
    partial = []
    if not exact:
        partial = [e for e in data["entities"] if any(qq in k for k in _all_keys(e))]
    unres = [x for x in data["unresolved"] if any(e["entity_id"] in x.get("candidates", []) or
                                                 e["entity_id"] == x.get("entity_created") for e in exact)]
    return {"query": q, "exact": exact, "partial_candidates": [
        {"entity_id": e["entity_id"], "name": e["canonical_name"], "emails": e["emails"]} for e in partial[:25]],
            "related_unresolved": unres}


def _txt_entity(e: dict) -> str:
    L = [f"ENTITY {e['entity_id']}  name={e['canonical_name']}  kind={e['kind']}  emails={e['emails']}"]
    if e["persona"]:
        P = e["persona"]
        L.append(f"  persona: {P['persona_key']} - {P['role']} / {P['department']}"
                 + ("" if P["usable_in_tasks"] else "  ** NOT USABLE IN TASKS **"))
    if len(e["names"]) > 1:
        L.append(f"  names seen: {e['names']}")
    for svc, ids in e["identities"].items():
        if svc == "roster":
            continue
        for i in ids:
            body = ", ".join(f"{k}={v}" for k, v in i.items() if k != "join" and v not in (None, "", [], {}))
            L.append(f"  {svc:10} {body}   [join: {i['join']}]")
    missing = [s for s in SERVICES if s not in e["identities"] and s != "roster"]
    if missing:
        L.append(f"  absent from: {', '.join(missing)}")
    L.append(f"  last activity: {e['last_activity'] or '-'}")
    for f in e["flags"]:
        L.append(f"  FLAG: {f}")
    return "\n".join(L)


# ---------------------------------------------------------------- self-test

def _self_test() -> int:
    data = build()
    E = {e["entity_id"]: e for e in data["entities"]}
    n = [0]

    def check(c, msg):
        if not c:
            raise AssertionError(msg)
        n[0] += 1
        print(f"  ok  {msg}")

    def ids(e, svc, k="id"):
        return [i.get(k) for i in e["identities"].get(svc, [])]

    personas = [e for e in data["entities"] if e["persona"]]
    check(len(personas) == 19 and sum(e["persona"]["usable_in_tasks"] for e in personas) == 17,
          "19 persona entities, 17 usable in tasks")
    check(len({e["entity_id"] for e in data["entities"]}) == len(data["entities"]), "entity ids unique")
    # every email maps to exactly one entity
    em = Counter(m.casefold() for e in data["entities"] for m in e["emails"])
    check(all(v == 1 for v in em.values()), "every email belongs to exactly one entity")

    # Ask_Carriers §1 persona ID map, parsed from the authority file
    rows = {}
    for line in ASK.read_text().splitlines():
        if line.startswith("| ") and "harmony" not in line and not line.startswith("| Persona") and not line.startswith("|---"):
            cells = []
            for c in line.strip().strip("|").split("|"):
                m = re.search(r"`([^`]+)`", c)
                cells.append(m.group(1) if m else c.strip().strip("*").split(" (")[0].strip())
            if len(cells) == 9 and ("_SLACK_ID" in cells[1] or re.match(r"U[A-Z0-9]+$", cells[1])):
                rows[cells[0]] = cells
    check(len(rows) == 19, "Ask_Carriers §1 map has 19 rows")
    by_name = {e["canonical_name"]: e for e in personas}
    mism = []
    for name, c in rows.items():
        e = by_name[name]
        slack, gmail, root, lin, trello, ghub, confl, contact = c[1:]
        if slack.split()[0] not in ids(e, "slack"):
            mism.append((name, "slack"))
        if (gmail.lower().startswith("yes")) != bool(e["identities"].get("gmail")):
            mism.append((name, "gmail"))
        r = [x for i in e["identities"].get("gdrive", []) for x in i.get("root_folders", [])]
        if (root.startswith("d_") and root not in r) or (not root.startswith("d_") and r):
            mism.append((name, "drive root"))
        if lin not in ids(e, "linear"):
            mism.append((name, "linear"))
        if trello not in ids(e, "trello"):
            mism.append((name, "trello"))
        gl = re.findall(r"PERSON_\d+|EMPLOYEE_\d+", ghub)
        if gl:
            if f"{gl[0]}_GITHUB_USERNAME" not in ids(e, "github", "login"):
                mism.append((name, "github"))
        elif ids(e, "github", "login"):
            mism.append((name, "github (extra)"))
        if confl not in ids(e, "confluence"):
            mism.append((name, "confluence"))
        if contact.split()[0] not in ids(e, "contacts", "contact_id"):
            mism.append((name, "contacts"))
    check(not mism, f"all 19 personas match the Ask_Carriers §1 ID map (mismatches: {mism})")

    ab = E["email:arthur.blake@harmonygames.co"]
    check("EMPLOYEE_0025_SLACK_ID" in ids(ab, "slack") and ab["identities"]["slack"][0]["join"] == "exact_email",
          "Arthur Blake: Slack EMPLOYEE_0025_SLACK_ID joined by exact email")
    mb = E["email:marcus.bennett@harmonygames.co"]
    check([i.get("mailbox") for i in mb["identities"].get("gmail", [])] == ["marcus.bennett@harmonygames.co"],
          "Marcus Bennett carries the gmail identity marcus.bennett@harmonygames.co")
    check("email:marcus@harmonygames.co" not in E
          and not any("marcus@harmonygames.co" == m for e in data["entities"] for m in e["emails"]),
          "no separate marcus@ entity or email exists")
    tim = E["email:tim.steudler@harmonygames.co"]
    check(ids(tim, "slack") == ["UBF5AB53C96"] and not tim["persona"]["usable_in_tasks"],
          "Tim Steudler: Slack UBF5AB53C96, flagged not usable")
    cp = E["email:calvin.price@harmonygames.co"]
    gj = {i["login"]: i["join"] for i in cp["identities"]["github"]}
    check(gj == {"PERSON_0003_GITHUB_USERNAME": "exact_email", "PERSON_2137_GITHUB_USERNAME": "exact_name"},
          "Calvin Price: 2 GitHub logins (email join + exact-name join)")
    fs = E["email:frederick.stone@harmonygames.co"]
    check(any("Ryan" in f for f in fs["flags"]), "Frederick Stone's GitHub 'Ryan' name mismatch flagged")
    check(any(x["type"] == "ambiguous_name" and x["name"] == "Marcus" and x["service"] == "github"
              for x in data["unresolved"]), "GitHub 'Marcus' (PERSON_0396) left unresolved, not silently joined")
    th = E["email:thomas@harmonygames.co"]
    check(ids(th, "trello") == ["ae0d489f73ee6c1df4393924"] and th["identities"]["trello"][0]["join"] ==
          "exact_name+username_localpart", "Trello 'Thomas' joins Thomas via username corroboration")
    col = data["collisions"]
    mar = " ".join(col["shared_first_names"].get("marcus", []))
    check(all(m in mar for m in ("marcus.bennett@", "marcus.lee@")), "Marcus collision lists Marcus Bennett and Marcus Lee")
    check("EMPLOYEE_0032" in col["tokens_mapping_to_several_entities"], "EMPLOYEE_0032 token maps to several entities")
    check(any("U05F0A0D12F" in x for x in col["lookalike_handles_and_aliases"]),
          "Slack handle 'thomas' (Thomas Baker) vs thomas@ lookalike flagged")
    r = resolve(data, "usr_Victor Barnes")
    check(len(r["exact"]) == 1 and r["exact"][0]["canonical_name"] == "Victor Barnes", "resolve('usr_Victor Barnes')")
    r = resolve(data, "PERSON_6094_TRELLO_USER_ID")
    check(len(r["exact"]) == 1 and r["exact"][0]["canonical_name"] == "Leonard Hayes", "resolve(Leonard's Trello token id)")
    check(all(e["entity_id"].startswith("email:") for e in personas), "every persona entity keyed by its roster email")
    print(f"self-test: ok ({n[0]} assertions)")
    return 0


# ---------------------------------------------------------------- CLI

def main(argv: list) -> int:
    if "--self-test" in argv:
        try:
            return _self_test()
        except AssertionError as e:
            print(f"self-test: FAIL - {e}")
            return 1
    ap = argparse.ArgumentParser(prog="entity.py")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("build")
    sp = sub.add_parser("resolve")
    sp.add_argument("query")
    sp.add_argument("--json", action="store_true")
    sp = sub.add_parser("collisions")
    sp.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "build":
        context = globals().get("TASK_CONTEXT")
        source = (context or {}).get("source") or {}
        output = (source.get("kb_output_path") or source.get("kb_path")) if context else None
        if context and not output:
            raise SystemExit(f"error: no KB output path is configured for the {source.get('universe') or 'selected'} "
                             "universe; set kb_output_path in references/universe_sources.json")
        target = Path(output) / "entities.json" if context else OUT
        data = build()
        target.parent.mkdir(parents=True, exist_ok=True)
        tmp = target.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, indent=1, ensure_ascii=False, default=list))
        tmp.replace(target)
        m = data["_meta"]
        print(f"wrote {target.relative_to(pv.WS)}: {m['entity_count']} entities {m['kinds']}")
        print(f"unresolved: {dict(m['counts']['unresolved'])}  integrity flags: {dict(m['counts']['integrity_flags'])}")
        print(f"collisions: {m['counts']['collisions']}")
        return 0
    if a.cmd == "resolve":
        data = load()
        r = resolve(data, a.query)
        if a.json:
            print(json.dumps(r, indent=1, ensure_ascii=False))
            return 0
        if not r["exact"]:
            print(f"no exact match for {a.query!r}")
            for c in r["partial_candidates"]:
                print(f"  candidate: {c['entity_id']}  {c['name']}  {c['emails']}")
            return 0 if r["partial_candidates"] else 1
        for e in r["exact"]:
            print(_txt_entity(e))
        for x in r["related_unresolved"]:
            print(f"  UNRESOLVED ({x['type']}): {x['reason']}" + (f"  records={x.get('records')}" if x.get("records") else ""))
        return 0
    if a.cmd == "collisions":
        data = load()
        c = data["collisions"]
        if a.json:
            print(json.dumps({"collisions": c, "unresolved": data["unresolved"],
                              "integrity_flags": data["integrity_flags"]}, indent=1, ensure_ascii=False))
            return 0
        for k, v in c.items():
            print(f"\n{k.upper()} ({len(v)})")
            items = v.items() if isinstance(v, dict) else enumerate(v)
            for kk, vv in items:
                print(f"  {kk}: {vv}" if isinstance(v, dict) else f"  - {vv}")
        print(f"\nUNRESOLVED ({len(data['unresolved'])})")
        for x in data["unresolved"]:
            print(f"  [{x['type']}] {x.get('service', x.get('token'))}: {x['reason']} -> candidates {x['candidates']}")
        print(f"\nINTEGRITY FLAGS ({len(data['integrity_flags'])})")
        for x in data["integrity_flags"]:
            print(f"  {x}")
        return 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    from runtime_context import guarded_entry
    guarded_entry(globals(), require_source=True)
    raise SystemExit(main(sys.argv[1:]))
