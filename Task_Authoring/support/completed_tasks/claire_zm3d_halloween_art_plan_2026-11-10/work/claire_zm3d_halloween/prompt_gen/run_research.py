#!/usr/bin/env python3
"""rev3 research runs for the prompt brief: every persona_view.py search / can-see / check-sql and entity.py run, re-run on
the current SQL, plus a read-only overlay scan of 01_Universe_Inject.sql (persona_view.py search reads the base universe only,
so a seeded record is proven from the overlay scan and check-sql). Writes prompt_gen/research/{sap_raw,entity_raw}.txt and
sap_rows.json. Never executes SQL. Run from the workspace root:

    TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsN2 python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_gen/run_research.py
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
OUT = HERE / "research"
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
from base_check import parse_sql  # noqa: E402

SQL = TASK / "01_Universe_Inject.sql"
LB = WF / "injection_gen" / "load_bearing_ids.txt"
PV = ROOT / "Task_Authoring" / "tools" / "persona_view.py"
ENT = ROOT / "Task_Authoring" / "tools" / "entity.py"
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK.relative_to(ROOT)))
P = "claire_morgan"
MAIL = "claire.morgan@harmonygames.co"
PLAN = f"{MAIL}/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>"
DRAFT = f"{MAIL}/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>"
QUOTE = f"{MAIL}/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>"
RESTART = f"{MAIL}/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>"

# n, fact, target id(s), origin, service, natural queries (first is the row's), path note for a seeded row
ROWS = [
    ("1", "Leonard's Halloween ask", ["C06DJBJL798/1759269913.882683"], "seeded", "slack", ["halloween for ZM"], ""),
    ("2", "live creatives sheet", ["f_02b1968f5e882366fbb883"], "seeded", "gdrive", ["live creatives"], ""),
    ("3", "Arthur's release calendar", ["f_fdd6d2d2f4a4d2f5b908fb"], "seeded", "gdrive", ["release calendar"], ""),
    ("4", "Robert's pointer to his deck", ["C08R8CHB0QL/1758817822.269981"], "seeded", "slack", ["seasonal art direction"], ""),
    ("5", "Robert's deck", ["f_5ebf55ad29e815d46243c8"], "seeded", "gslides", ["Seasonal art direction"], ""),
    ("6", "Frederick's Sep 30 changes mail", [PLAN], "seeded", "gmail", ["October UA plan"], ""),
    ("7", "Frederick's Sep 12 draft", [DRAFT], "seeded", "gmail", ["UA plan draft"], ""),
    ("8", "Martin's export claim", ["C08R8CHB0QL/1759245641.309714"], "seeded", "slack", ["halloween store screens"], ""),
    ("9", "Halloween Store folder", ["d_74a7c95c28097dd9777e01"], "seeded", "gdrive", ["Halloween", "Store"], "listing the Halloween folder d_272d849cde40c35980a433, which `Halloween` returns from the overlay"),
    ("10", "UA masters files", ["f_dc5cf9e4250d433c1511ec", "f_bcd34f98925e3f20d846ce"], "seeded", "gdrive", ["cheer_fastcouch_halloween"], ""),
    ("11", "Marcus's IM reply", ["D05V2N6PZNU/1759166437.080255"], "seeded", "slack", ["cheer fastcouch"], ""),
    ("12", "Halloween push card", ["68dc52e015f87c50c441d1a9"], "seeded", "trello", ["Halloween push"], ""),
    ("13", "UA creative library tickets", ["ART-793"], "seeded", "linear", ["UA creative library"], "62 ticket rows, ART-793 to ART-854"),
    ("14", "April capture notes on the three re-captured cuts", ["cmt_art795_1", "cmt_art797_1", "cmt_art805_1"], "seeded", "linear", ["Captured from Android"], "the comments of ART-795, ART-797, ART-805"),
    ("15", "vendor quote", [QUOTE], "seeded", "gmail", ["Halloween props"], ""),
    ("16", "vendor contact", ["6b350edd259a8b4499a9e625"], "seeded", "contacts", ["KayKit"], ""),
    ("17", "KayKit Halloween Bits pack", ["/reviews/2166/body"], "base", "github", ["Halloween Bits"], ""),
    ("18", "Halloween review event", ["evt_d947bf7cd910549b674b1f"], "seeded", "gcal", ["Halloween review"], ""),
    ("19", "30 s cut master thread", ["C06DJBJL798/1755114007.441789"], "base", "slack", ["music is baked in"], ""),
    ("20", "#builds Android #1452", ["C05433XK267/1753820674.990309"], "base", "slack", ["ZombieSwap"], ""),
    ("21", "Robert's iOS 1232 post", ["C0880U9751A/1753820524.488479"], "base", "slack", ["zombie swap completed"], ""),
    ("22", "Leonard's Sep 3 export ask", ["C06DJBJL798/1756914854.743319"], "base", "slack", ["app store assets"], ""),
    ("23", "ART-774 decoy", ["/issues/582/title"], "base", "linear", ["screenshot"], ""),
    ("24", "Robert's Halloween pack mention", ["C0880U9751A/1738109783.735889"], "base", "slack", ["Halloween pack"], ""),
    ("25", "Martin's Sep 17 icon concept", ["C08R8CHB0QL/1758121809.236839"], "base", "slack", ["Halloween theme"], ""),
    ("26", "1.3.38 release", ["C0880U9751A/1758141269.804779"], "base", "slack", ["1.3.38 is out"], ""),
    ("27", "Julia's 4:5 static comment", ["68dc65a0f2d7fb28743f5860"], "seeded", "trello", ["4:5 static"], "the comments of card 68dc52e015f87c50c441d1a9"),
    ("28", "portrait end card ticket", ["ART-831"], "seeded", "linear", ["portrait UA end card"], ""),
    ("29", "Robert's icon reply", ["C08R8CHB0QL/1758127951.679146"], "seeded", "slack", ["too busy at that size"], "the thread under row 25's C08R8CHB0QL/1758121809.236839"),
    ("30", "Frederick's end-card note", ["cmt_art831_2"], "seeded", "linear", ["live creatives sheet"], "the comments of ART-831"),
    ("31", "Frederick's Android date reply (R_REVIEW_WINDOW)", ["C0880U9751A/1759275738.984915"], "seeded", "slack", ["Unity", "fake installs"], "the thread under C0880U9751A/1759211437.306779, which `fake installs` returns from base"),
    ("32", "Marcus's re-capture note (R_RECAPTURE_NOTE)", ["C09ATAJ220H/1758823964.738872"], "seeded", "slack", ["couch alpha 50", "barrel marketing2", "balloons alpha 50 (1)"], "channel #zm-animations C09ATAJ220H, Claire is a member"),
    ("33", "Robert's test review (R_TEST_TURNED_DOWN)", ["C08R8CHB0QL/1759248337.170599", "C08R8CHB0QL/1759167065.499092"], "seeded", "slack", ["cheer fastcouch", "July capture"], "the thread under Marcus's post C08R8CHB0QL/1759167065.499092 in #zombie-art"),
    ("34", "Martin's vacation post and Leonard's reply (R_STATICS_COVER)", ["C05KNDCHAAG/1759243286.478812", "C05KNDCHAAG/1759275107.322377"], "seeded", "slack", ["vacation", "ad statics"], "channel #company-internal C05KNDCHAAG; Leonard's reply is the thread under the post"),
    ("35", "Frederick's restart mail (R_TABLET_TRIM)", [RESTART], "seeded", "gmail", ["squirrelfail landscape", "mrfluffernot", "Unity"], ""),
    ("36", "Frederick's packs comment (R_OLD_PACKS)", ["68d6cff0c6568da5d9c8e81f"], "seeded", "trello", ["end card 001", "Marketing Video Refresh"], "the comments of base card 68768a1501ae552dbee94b8a, which `Marketing Video Refresh` returns from base"),
    ("37", "Leonard's store-ticket reply", ["C08R8CHB0QL/1759247246.453725"], "seeded", "slack", ["store art"], "the thread under row 8's C08R8CHB0QL/1759245641.309714"),
]
CARRIERS = {"31", "32", "33", "34", "35", "36"}
CAN_SEE = [("slack", x) for x in (
    "C06DJBJL798/1755114007.441789", "C05433XK267/1753820674.990309", "C0880U9751A/1753820524.488479",
    "C06DJBJL798/1756914854.743319", "C0880U9751A/1738109783.735889", "C08R8CHB0QL/1758121809.236839",
    "C0880U9751A/1758141269.804779", "C0880U9751A/1759211437.306779", "C08R8CHB0QL/1754310794.907609",
    "C08R8CHB0QL/1754316299.381419", "C05KNDCHAAG/1756717965.570179", "C05KNDCHAAG/1719394673.875309",
    "C06DJBJL798/1749230960.644899", "C08R8CHB0QL/1758211038.665909", "C05KNDCHAAG/1759279503.256079")]
ENTITIES = ["Leonard", "Frederick", "Martin", "Marcus", "Robert", "Arthur", "Julia", "Claire", "Marcus Bennett", "Martin Walsh",
            "Julia Lawson", "Marcus Lee", "Martin Lewis", "Peter Lawson"]
TABLES = {"slack": ("slack.slack_messages",), "gmail": ("gmail.gmail_messages",), "gdrive": ("gdrive.drive_files",),
          "gslides": ("gslides.slides_presentations", "gslides.slides_page_elements"), "gcal": ("gcal.gcal_events",),
          "linear": ("linear.linear_issues", "linear.linear_comments"), "trello": ("trello.trello_cards", "trello.trello_actions"),
          "contacts": ("contacts.contacts",), "github": ()}


def run(args):
    r = subprocess.run([sys.executable, "-B"] + [str(a) for a in args], cwd=str(ROOT), env=ENV, capture_output=True, text=True, timeout=600)
    return r.stdout.rstrip()


def pv_search(service, query, limit=10):
    args = [PV, "search", P, service, query, "--limit", limit] + (["--no-hidden"] if service == "gmail" else [])
    return run(args)


check = json.loads(run([PV, "check-sql", P, SQL, "--load-bearing", LB, "--json"]))
vis = {r["line"]: r for r in check["rows"]}
rows = [r for r in parse_sql(SQL.read_text()) if r["op"] == "insert"]


def rid(r):
    t, w = r["table"], r["row"]
    if t == "slack.slack_messages":
        return f'{w["channel_id"]}/{w["ts"]}'
    for k in ("identifier", "event_id", "contact_id", "id"):
        if w.get(k) not in (None, ""):
            return w[k]
    return "?"


def overlay(service, query):
    """seeded rows of this service whose text holds every word of the query (case-insensitive); Claire's copies only for mail"""
    words = query.casefold().split()
    hits = []
    for r in rows:
        if r["table"] not in TABLES[service]:
            continue
        w = r["row"]
        if r["table"] == "gmail.gmail_messages" and w.get("user_email") != MAIL:
            continue
        if r["table"] == "gcal.gcal_events" and w.get("calendar_id") != MAIL:
            continue
        hay = " ".join(str(v) for k, v in w.items() if isinstance(v, str)).casefold()
        if all(x in hay for x in words):
            v = vis.get(int(r["line"]), {})
            keys = v.get("keys") or []
            ident = next((k for k in keys if "/" in k), rid(r))
            hits.append((ident, r["table"], int(r["line"]), v.get("verdict", "unscoped"), keys + [rid(r)]))
    return hits


def overlay_block(service, query):
    hits = overlay(service, query)
    lines = [f"OVERLAY {service} '{query}' as {P}  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)",
             f"overlay hits={len(hits)}"]
    lines += [f"  {i}  {t}  L{l}  visible={v}" for i, t, l, v, _ in hits[:8]]
    if len(hits) > 8:
        lines.append(f"  ... {len(hits) - 8} more rows of the same tables")
    return "\n".join(lines), sorted({k for h in hits for k in [h[0]] + h[4]})


def parse_head(out):
    m = re.search(r"visible hits=(\d+) \(showing (\d+)\)\s+hidden by ACL=(\S+) in (\d+) containers\s+UNVERIFIED=(\d+) in (\d+)", out)
    first = None
    for line in out.splitlines():
        if line.startswith("  {"):
            try:
                d = json.loads(line.strip())
            except ValueError:
                d = {}
            first = d.get("id") or d.get("pointer") or (re.search(r'"id": "([^"]+)"', line) or re.search(r'"pointer": "([^"]+)"', line) or [None, None])[1]
            break
    ids = re.findall(r'"id": "([^"]+)"', out) + re.findall(r'"pointer": "([^"]+)"', out)
    return dict(visible=int(m.group(1)), showing=int(m.group(2)), hidden=m.group(3), hidden_c=int(m.group(4)),
                unverified=int(m.group(5)), first=first, ids=ids)


def main():
    OUT.mkdir(exist_ok=True)
    raw, table, misses = [], [], []
    for n, fact, targets, origin, service, queries, path in ROWS:
        runs = []
        for k, q in enumerate(queries):
            limit = 500 if n == "23" else 10
            out = pv_search(service, q, limit)
            head = parse_head(out)
            label = f"{n}{'abc'[k] if len(queries) > 1 else ''} {service} {q}"
            shown = "\n".join(out.splitlines()[:14]) if limit == 500 else out
            raw.append(f"### {label}\n{shown}\n")
            over_txt, over_ids = ("", [])
            if service != "github":
                over_txt, over_ids = overlay_block(service, q)
                raw.append(f"### {label} overlay\n{over_txt}\n")
            runs.append(dict(query=q, **head, overlay=over_ids,
                             target_rank=next((i + 1 for i, x in enumerate(head["ids"]) if x in targets), None),
                             target_overlay=[t for t in targets if t in over_ids]))
        table.append(dict(n=n, fact=fact, targets=targets, origin=origin, service=service, path=path, runs=runs))
    for n, fact, targets, origin, service, queries, path in ROWS:
        if n not in CARRIERS:
            continue
        out = pv_search(service, "halloween")
        head = parse_head(out)
        over_txt, over_ids = overlay_block(service, "halloween")
        raw.append(f"### {n} {service} halloween (does a halloween search reach the carrier?)\n{out}\n")
        raw.append(f"### {n} {service} halloween overlay\n{over_txt}\n")
        misses.append(dict(n=n, fact=fact, service=service, visible=head["visible"], overlay=int(re.search(r"overlay hits=(\d+)", over_txt).group(1)),
                           target_hit=[t for t in targets if t in over_ids + head["ids"]], targets=targets))
    for svc, x in CAN_SEE:
        raw.append(f"### can-see {P} {svc} {x}\n{run([PV, 'can-see', P, svc, x])}\n")
    for x in ("C09ATAJ220H/1758823964.738872", "C0880U9751A/1759275738.984915", "C05KNDCHAAG/1759243286.478812"):
        raw.append(f"### can-see {P} slack {x} (seeded: base can-see has no such ts; channel verdict only; check-sql below decides)\n{run([PV, 'can-see', P, 'slack', x])}\n")
    full = run([PV, "check-sql", P, SQL, "--load-bearing", LB])
    raw.append(f"### check-sql {P} 01_Universe_Inject.sql --load-bearing Working_Files/injection_gen/load_bearing_ids.txt\n{full}\n")
    (OUT / "sap_raw.txt").write_text("\n".join(raw))
    (OUT / "sap_rows.json").write_text(json.dumps(dict(rows=table, halloween=misses, check_sql=dict(summary=check["summary"], verdict=check["verdict"], failures=check["load_bearing_failures"])), indent=1, ensure_ascii=False) + "\n")
    ent = [f"### entity.py collisions\n{run([ENT, 'collisions'])}\n"] + [f'### entity.py resolve "{e}"\n{run([ENT, "resolve", e])}\n' for e in ENTITIES]
    (OUT / "entity_raw.txt").write_text("\n".join(ent))
    print("rows", len(table), "halloween rows", len(misses), "check-sql", check["verdict"], check["summary"])


if __name__ == "__main__":
    main()
