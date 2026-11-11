"""Wording, chronology and ownership sweep over the generated SQL. Run: python3 sweep.py"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
sys.path.insert(0, str(HERE))
from base_check import parse_sql  # noqa: E402
import data as D  # noqa: E402

sql = (ROOT / "Task_Authoring" / "task_inputs" / "01_Universe_Inject.sql").read_text(encoding="utf8")
rows = parse_sql(sql)
ins = [r for r in rows if r["op"] == "insert"]
bad = []


def fail(msg):
    bad.append(msg)


def text_of(r):
    return " ".join(str(v) for v in r["row"].values() if v is not None)


# Banned anywhere in seeded text.
banned = [r"outbreak", r"infect", r"plague", r"\bvirus", r"pandemic", r"epidemic", r"contagi", r"Victor", r"\bBarnes\b", r"Dempsey",
          r"\bTim\b", r"ENG-\d+", r"Sub #", r"BETA", r"\bspend\b", r"\bCPI\b"]
for r in ins:
    t = text_of(r)
    for b in banned:
        if re.search(b, t, re.I if b.islower() or b.startswith(r"\b") and b[2:3].islower() else 0):
            fail(f"banned {b} in {r['table']} {str(list(r['row'].values())[0])[:50]}")

for s in ("confluence.", "snowflake."):
    if re.search(rf"(INSERT INTO|UPDATE) {s}", sql):
        fail("writes " + s)

# Timestamps strictly before the bound.
for m in re.finditer(r"'(2025-(?:1[0-2])-\d\d[^']*|2026-[^']*)'", sql):
    fail("timestamp past bound " + m.group(1))
for r in ins:
    for k, v in r["row"].items():
        if isinstance(v, str) and re.fullmatch(r"\d{4}-\d\d-\d\dT[\d:.]+Z", v) and v >= "2025-10-01":
            fail(f"late {k} {v}")

# Avoid lists per deciding record.
LISTS = {
    "K1": (D.K1_BODY + " " + D.PR["k1_mail"]["subject"], ["playtest", "beta", "session", "form", "walked through", "helped", "coach",
                                                          "explained", "hint", "doesn't count", "exclude", "duplicate"]),
    "K3": (D.RC27_BODY, ["samsung", " fix", "branch", "build", "schedule", "nightly", "cannot run on a device"]),
    "GATE": (D.GATE_DOC, ["no session blocker", "sit in review", "for the branch the job ran on", " a iphone"]),
    "LOG": (D.LOG_NOTE, ["says nothing about when"]),
    "CARD": (D.CARD["desc"], ["counts, means and gap"]),
    "K4": (D.K4_TEXT, ["test", "beta", "playtest", "build", "rpg", "casual", "session", "tester"]),
    "K5": (D.K5_TEXT, ["dev build", "session", "sektör", "re-run"]),
    "ZOM567": (D.ZOM567["title"] + D.ZOM567["description"] + D.ZOM567["line"],
               ["#476", "on main", "full regression", "qa sign-off", " pr ", "build"]),
    "F": (D.F_TEXT, ["ticket", "store", "kadıköy"]),
}
for k, (t, words) in LISTS.items():
    for w in words:
        if w in t.lower():
            fail(f"{k} carries avoided word {w!r}")

# Deciding records name no tester: no person name besides the author context.
names = ["Oliver", "Owen", "Samuel", "Calvin", "Marcus", "Martin", "Douglas", "Vincent", "Brian", "Robert"]
for k in ("K1", "K4", "K5", "K3"):
    for n in names:
        if n.lower() in LISTS[k][0].lower():
            fail(f"{k} names {n}")

# Verbatim delegation quotes.
for f in D.MANIFEST["ask_fragments"]:
    q = f.get("delegation_quote")
    q = D.QUOTE_CHANGES.get(q, q)
    if q and q not in sql.replace("''", "'"):
        where = f.get("delegated_by_record")
        if not where.startswith("C090N54TG79/1758517286"):
            fail(f"quote missing {f['id']}: {q}")

# 1943 lives only in its home records.
home = set(next(x for x in D.MANIFEST["facts"] if x["key"] == "non-store build")["home_ids"])
for r in ins:
    ident = str(r["row"].get("id") or r["row"].get("document_id"))
    if "1943" in text_of(r) and ident not in home and r["table"] not in ("gdrive.drive_files",):
        fail(f"1943 outside home: {r['table']} {ident[:40]}")

# Gmail: no Brian, Julia's copy of every message.
gm = [r["row"] for r in ins if r["table"] == "gmail.gmail_messages"]
for m in gm:
    if "brian" in (m["from_email"] + m["to_json"]).lower():
        fail("Brian in Gmail")
ids = {m["id"].split("/", 1)[1] for m in gm if m["user_email"] == D.JULIA.email}
if len(ids) != 17 + 1:
    fail(f"Julia copies {len(ids)}")

# Comments precede closure; ZOM-559 untouched; ownership of write targets.
for r in rows:
    if r["table"].startswith("linear.") and "ZOM-559" in str(r.get("where")):
        fail("ZOM-559 touched")
own = {r["row"]["id"]: r["row"]["owner_email"] for r in ins if r["table"] == "gdrive.drive_files"}
for fid in (D.WORKBOOK, D.PR["R6_log_note"]["id"], D.PR["audience_deck"]["id"]):
    if own[fid] != D.JULIA.email:
        fail("owner " + fid)

# Row-id and day checks: no record on Sep 27-28.
for r in ins:
    for k, v in r["row"].items():
        if isinstance(v, str) and re.match(r"2025-09-2[78]T", v):
            fail(f"weekend date {k} {v}")

print("SWEEP:", "PASS" if not bad else "FAIL")
for b in bad:
    print(" ", b)
