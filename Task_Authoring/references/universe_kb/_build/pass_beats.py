"""Parse storyline beats from metadata/*.yaml (line-based, stdlib only) and verify every artifact id
against the base exports -> kb_cache/kb_beats.json. Also provides verify() used by the timeline."""
import os, re, json, collections, glob
from common import *

_slack_cache = {}


def slack_has(cid, ts):
    try:
        mon = month_of_ts(float(ts))
    except Exception:
        return None
    key = (cid, mon)
    if key not in _slack_cache:
        p = SLACK + "/messages/%s/%s.json" % (cid, mon)
        _slack_cache[key] = {x.get("ts"): (x.get("user"), (x.get("text") or "")[:160]) for x in jload(p)} if os.path.exists(p) else {}
    return _slack_cache[key].get(ts)


class Verifier:
    def __init__(self):
        G = jload(GITHUB)
        self.prs = {p["id"]: (p.get("created_at"), p.get("merged_at"), p.get("title")) for p in G["pull_requests"]}
        self.pr_comments = {c["id"]: c.get("created_at") for c in G["pull_request_comments"]}
        del G
        L = jload(LINEAR)
        self.issues = {i["id"]: (i.get("created_at"), i.get("completed_at") or i.get("canceled_at"), i.get("title"), i.get("state_id")) for i in L["issues"]}
        del L
        T = jload(TRELLO)
        self.trello = {c["id"]: (c.get("dateLastActivity"), c.get("name")) for c in T["cards"]}
        self.trello.update({a["id"]: (a.get("date"), a.get("type")) for a in T["actions"]})
        del T
        C = jload(GCAL)
        self.events = {e["event_id"]: ((e.get("start") or {}).get("dateTime"), e.get("summary"), e.get("calendar_id")) for e in C["events"]}
        del C
        F = jload(CONF)
        self.pages = {p["id"]: (p.get("created_at"), p.get("updated_at"), p.get("title")) for p in F["pages"]}
        self.pages.update({c["id"]: (c.get("created_at"), None, "comment") for c in F["comments"]})
        del F
        R = jload(GDRIVE)
        self.drive = {f["id"]: (f.get("created_time"), f.get("modified_time"), f.get("name")) for f in R["drive_files"]}
        del R
        gm = jload(CACHE + "/kb_gmail.json")
        self.gthreads = {}
        for mb, lst in gm["thread_ids"].items():
            for t in lst:
                self.gthreads.setdefault(t, []).append(mb)
        self.gmail_files = set(os.listdir(GMAIL + "/threads"))
        del gm
        O = jload(CACHE + "/kb_other.json")
        self.snow_tables = {("%s.%s.%s" % (v.get("db"), v.get("schema"), k)) if v.get("db") else k: v.get("rows") for k, v in O["snowflake"]["tables"].items()}
        self.snow_names = set(O["snowflake"]["tables"])
        del O

    def check(self, rid):
        """Return (ok, service, when, label)."""
        if ":" not in rid:
            return (False, None, None, None)
        svc, rest = rid.split(":", 1)
        if svc == "slack":
            cid, ts = rest.split(":", 1) if rest.count(":") else rest.split("/", 1)
            h = slack_has(cid, ts)
            return (h is not None, "slack", ts_to_dt(float(ts)).isoformat() if h is not None else None, (h or ("", ""))[1])
        if svc == "github":
            r = self.prs.get(rest) or ((self.pr_comments.get(rest), None, "comment") if rest in self.pr_comments else None)
            return (r is not None, "github", r and (r[1] or r[0]), r and r[2])
        if svc == "linear":
            r = self.issues.get(rest)
            return (r is not None, "linear", r and r[0], r and r[2])
        if svc == "trello":
            r = self.trello.get(rest)
            return (r is not None, "trello", r and r[0], r and r[1])
        if svc in ("gcal", "calendar"):
            r = self.events.get(rest)
            return (r is not None, "gcal", r and r[0], r and r[1])
        if svc == "confluence":
            r = self.pages.get(rest)
            return (r is not None, "confluence", r and (r[1] or r[0]), r and r[2])
        if svc in ("drive", "gdrive", "docs", "sheets", "slides"):
            r = self.drive.get(rest)
            return (r is not None, "drive", r and (r[1] or r[0]), r and r[2])
        if svc == "gmail":
            thr = rest.split(":")[-1].split("/")[-1]
            if rest.endswith(".json"):
                return (rest in self.gmail_files, "gmail", None, rest)
            mbs = self.gthreads.get(thr)
            return (bool(mbs), "gmail", None, (mbs or [None])[0])
        if svc == "snowflake":
            nm = rest.split(".")[-1]
            ok = nm in self.snow_names or "/" in rest
            return (ok, "snowflake", None, rest)
        return (False, svc, None, None)


def parse_yaml_beats(path):
    beats = []
    in_beats = False
    cur = None
    art = None
    key = None
    lines = open(path).read().split("\n")
    name = None
    for ln in lines:
        if ln.startswith("name:") and name is None:
            name = ln.split(":", 1)[1].strip().strip("'\"")
        if ln.startswith("beats:"):
            in_beats = True
            continue
        if in_beats and ln and not ln.startswith(" ") and not ln.startswith("-"):
            in_beats = False
        if not in_beats:
            continue
        m = re.match(r"^- id: (\S+)", ln)
        if m:
            cur = {"id": m.group(1), "action": "", "date": None, "actor": None, "artifacts": []}
            beats.append(cur)
            key = None
            continue
        if cur is None:
            continue
        m = re.match(r"^  (actor|action|summary): ?(.*)$", ln)
        if m:
            key = m.group(1)
            if key in ("actor", "action"):
                cur[key] = m.group(2).strip().strip("'\"")
            continue
        if key == "action" and re.match(r"^    \S", ln) and not re.match(r"^    \w+:", ln):
            cur["action"] += " " + ln.strip().strip("'\"")
            continue
        m = re.match(r"^\s+target_date: (\d+)", ln)
        if m:
            cur["date"] = int(m.group(1))
            key = None
            continue
        m = re.match(r"^  - component: (\S+)", ln)
        if m:
            art = {"component": m.group(1)}
            cur["artifacts"].append(art)
            key = None
            continue
        m = re.match(r"^\s+record_id: (\S+)", ln)
        if m and art is not None:
            art["record_id"] = m.group(1).strip("'\"")
            continue
        m = re.match(r"^\s+ts: (.+)$", ln)
        if m and art is not None and "ts" not in art:
            art["ts"] = m.group(1).strip().strip("'\"")
        if re.match(r"^  \w+:", ln):
            key = None
    return name, beats


def main():
    V = Verifier()
    out = []
    files = sorted(glob.glob(META + "/*/*.yaml"))
    for f in files:
        sid = os.path.basename(f)[:-5]
        if sid == "universe":
            continue
        name, beats = parse_yaml_beats(f)
        for b in beats:
            if not b["date"] or float(b["date"]) >= CLOCK_TS:
                continue
            arts = []
            for a in b["artifacts"]:
                rid = a.get("record_id")
                if not rid:
                    continue
                ok, svc, when, label = V.check(rid)
                ok = ok and before_clock(when)
                arts.append({"record_id": rid, "exists": ok, "service": svc, "when": when, "label": (label or "")[:120] if isinstance(label, str) else label})
            svcs = sorted(set(a["service"] for a in arts if a["exists"]))
            out.append({"storyline": sid, "storyline_name": name, "beat": b["id"], "actor": b["actor"], "action": b["action"][:240],
                        "target_date": ts_to_dt(b["date"]).strftime("%Y-%m-%d") if b["date"] else None,
                        "orientation_only": True,
                        "artifacts": arts, "verified_services": svcs,
                        "missing": [a["record_id"] for a in arts if not a["exists"]]})
    jdump(out, CACHE + "/kb_beats.json")
    n2 = sum(1 for b in out if len(b["verified_services"]) >= 2)
    miss = sum(len(b["missing"]) for b in out)
    print("beats", len(out), "with 2+ verified services", n2, "missing artifact ids", miss, "storylines", len(set(b["storyline"] for b in out)))


if __name__ == "__main__":
    main()
