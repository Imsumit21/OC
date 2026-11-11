#!/usr/bin/env python3
"""Turn the worker's grounded roster (roster.json, 50 surfaces) into the design roster (roster_final.json).

Design decisions applied here (scenario stage, recorded in 01_Scenario_Design.md section 2):
  * every ad surface (video, static, end card) carries its source build in its ART ticket comment, so Robert's
    rule ("captured or rendered from a build older than Android #1452 / iOS 1232") decides every ad without a
    render-vs-capture fork; Julia's June statics and Martin's Apr 7 end card are old art (Refresh first);
  * store sets are the Sep 3 export of Martin's Aug 28 concept, live with 1.3.38 (Sep 17): current art, no
    campaigns, no library ticket;
  * four cuts posted before the swap were re-captured on a September build (a second ticket comment supersedes
    the first): cheer fastcouch 9:16 (still Reuse: Marcus dressed the re-capture), couch alpha 50, barrel
    marketing2 4:5 and balloons alpha 50 (1) (Halloween version); the cheer fastcouch 16:9 export follows its parent;
  * the off-sheet portrait end card was rendered from Android #1450 (new background, before the #1452 swap):
    Refresh first (near-miss of the threshold);
  * ART-793 onward: the Sep 8 library batch in roster order, four archived creatives, then the three boris
    tickets on Sep 12 (the boris cuts were made Sep 11).
Read-only on the universe:  python3 -B Task_Authoring/task_inputsN2/Working_Files/scenario_gen/finalize_roster.py
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE / "roster.json").read_text())
BY = {r["key"]: r for r in R}
B = "slack:messages/C05433XK267/"
BUILDS = {  # #builds Jenkins results relied on (Match3D Android / Match 3D iOS Internal, Success)
    "Android #456": ("2025-04-07", B + "2025-04.json#/640"), "Android #457": ("2025-04-07", B + "2025-04.json#/648"),
    "Android #440": ("2025-04-05", B + "2025-04.json#/576"), "Android #475": ("2025-04-08", B + "2025-04.json#/724"),
    "Android #633": ("2025-04-29", B + "2025-04.json#/2150"), "Android #771": ("2025-05-28", B + "2025-05.json#/1464"),
    "Android #852": ("2025-06-05", B + "2025-06.json#/369"), "Android #1427": ("2025-07-28", B + "2025-07.json#/1561"),
    "Android #1450": ("2025-07-29", B + "2025-07.json#/1664"), "Android #1452": ("2025-07-29", B + "2025-07.json#/1672"),
    "iOS 1232": ("2025-07-29", B + "2025-07.json#/1673"), "Android #1529": ("2025-08-04", B + "2025-08.json#/145"),
    "Android #1630": ("2025-08-13", B + "2025-08.json#/550"), "Android #1896": ("2025-09-16", B + "2025-09.json#/514"),
    "Android #1935": ("2025-09-22", B + "2025-09.json#/707"), "Android #1966": ("2025-09-24", B + "2025-09.json#/856"),
}
OLD = {"Android #440", "Android #456", "Android #457", "Android #475", "Android #633", "Android #771", "Android #852",
       "Android #1427", "Android #1450", "prototype"}
MONTH = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
         "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}


def md(iso: str) -> str:
    y, m, d = iso.split("-")
    return f"{MONTH[m]} {int(d)}" + ("" if y == "2025" else f", {y}")


RECAPTURE = {  # key -> (build, comment time, re-capturer)
    "cheer fastcouch 9:16": ("Android #1896", "2025-09-16T16:40:00Z", "marcus.bennett"),
    "couch alpha 50": ("Android #1935", "2025-09-22T15:05:00Z", "marcus.bennett"),
    "barrel marketing2 4:5": ("Android #1896", "2025-09-16T16:55:00Z", "marcus.bennett"),
    "balloons alpha 50 (1)": ("Android #1966", "2025-09-24T18:40:00Z", "marcus.bennett"),
}
SOURCE = {  # source build per ad where the worker's value is a render ("n/a") or must change
    "julia 1:1": "Android #852", "julia 4:5": "Android #852", "julia 9:16": "Android #852", "julia 16:9": "Android #852",
    "julia 1:1 android 1080": "Android #852", "julia 4:5 android 1080x1350": "Android #852",
    "end card template 16:9": "Android #456", "marcus portrait UA end card": "Android #1450",
    "end card 001": "Android #1529", "end card 16:9 from 001": "Android #1529", "end card 1:1 from 001": "Android #1529",
}
ARCHIVED = [  # Archive tab: paused creatives that keep their library ticket (base files in roster_notes.md section 6)
    {"key": "GreenCouch 001", "format": "9:16", "paused_on": "2025-09-15", "base": "slack:files.json#/17527"},
    {"key": "Professional Mode 9x16 test", "format": "9:16", "paused_on": "2025-09-15", "base": "slack:files.json#/21259"},
    {"key": "sophie ocean portrait", "format": "9:16", "paused_on": "2025-09-15", "base": "slack:files.json#/13436"},
    {"key": "squirrelfail portrait text", "format": "9:16", "paused_on": "2025-09-19", "base": "slack:files.json#/13428"},
]
ASPECT = {"video": None, "static": None, "end_card": None}

# Scenario revision 02 (2026-11-04; requester: over 180 tool calls in every run): twelve more serving exports that
# Frederick ticketed after the Sep 12 batch. Each is a real per-record decision on its own ticket: eight placements that
# went live with the Sep 9 tablet / feed launch (catch-up batch ticketed Sep 15) and four re-exports cut from a September
# re-capture (ticketed the day they went live). cheer fastcouch 4:5 is the cohort-boundary case for Marcus's DM ("both
# 9:16 and 16:9"): it has no Halloween version yet.
EXTRAS = [
    dict(key="couch boss 30 16:9", parent="couch boss 30", campaigns=["iOS UK tablet", "Android US tablet"], batch="catchup"),
    dict(key="couch marketing2 30s 16:9", parent="couch marketing2 30s", campaigns=["Android US tablet"], batch="catchup"),
    dict(key="cinematicTutorial Ad 1 16:9", parent="cinematicTutorial Ad 1", campaigns=["iOS UK tablet"], batch="catchup"),
    dict(key="tutorialCinematic 1:1", parent="tutorialCinematic portrait", campaigns=["Android US phone"], batch="catchup"),
    dict(key="cheer 30p 4:5", parent="cheer 30p 9:16", campaigns=["iOS UK phone"], batch="catchup"),
    dict(key="end card 4:5 from 001", parent="end card 001", campaigns=["iOS UK phone"], batch="catchup"),
    dict(key="julia 1:1 android tablet", parent="julia 1:1", campaigns=["Android US tablet"], batch="catchup"),
    dict(key="boris alin2 16:9", parent="boris alin2 9:16", campaigns=["iOS UK tablet", "Android US tablet"],
         batch="catchup", live="2025-09-12"),
    dict(key="cheer fastcouch 4:5", parent="cheer fastcouch 9:16", campaigns=["iOS UK phone"], batch="recap",
         build="Android #1896", recap_of="9:16", at="2025-09-17T17:30:00Z"),
    dict(key="barrel marketing2 1:1", parent="barrel marketing2 4:5", campaigns=["Android US phone"], batch="recap",
         build="Android #1896", recap_of="4:5", at="2025-09-17T17:40:00Z"),
    dict(key="couch alpha 50 4:5", parent="couch alpha 50", campaigns=["iOS UK phone"], batch="recap",
         build="Android #1935", recap_of="9:16", at="2025-09-23T16:10:00Z"),
    dict(key="balloons alpha 50 (1) 16:9", parent="balloons alpha 50 (1)", campaigns=["iOS UK tablet", "Android US tablet"],
         batch="recap", build="Android #1966", recap_of="9:16", at="2025-09-25T17:00:00Z"),
]
_RAW = {r["key"]: r for r in R}
for e in EXTRAS:
    p = dict(_RAW[e["parent"]])
    x = {k: p.get(k) for k in ("kind", "on_sheet", "sheet_tab", "maker", "capture_build", "capture_ref", "audio_master")}
    x.update(key=e["key"], base_evidence=[], seeded_variant=True, campaigns=list(e["campaigns"]),
             already_made_halloween=False, owner=p.get("owner"), notes=None, extra=dict(e), on_sheet=True,
             sheet_tab="Unity")
    if e["batch"] == "recap":
        x.update(capture_build=e["build"], capture_ref="build", audio_master="sfx_only")
    R.append(x)

out = []
for r in R:
    r = dict(r)
    k = r["key"]
    if r["kind"] in ("icon", "store_set"):
        r["campaigns"] = []
        r["live_since"] = "2025-09-17"
        r["source_build"] = None
        r["ticket"] = None
        if r["kind"] == "store_set":
            r["base_evidence"] = list(r.get("base_evidence") or []) + [
                "slack:messages/C06DJBJL798/2025-08.json (Martin's Aug 28 concept, 1756393931.415699)",
                "slack:messages/C06DJBJL798/2025-09.json#/0 (Leonard's Sep 3 export ask, 1756914854.743319)"]
        r["notes"] = None
        out.append(r)
        continue
    if k == "cheer fastcouch 16:9":
        r["campaigns"] = ["iOS UK tablet", "Android US tablet"]
    if k == "marcus portrait UA end card":
        r["campaigns"] = ["Android US phone"]
    build = SOURCE.get((r.get("extra") or {}).get("parent") if r.get("extra") and r["extra"]["batch"] == "catchup" else k) \
        or r.get("capture_build")
    if build == "pre-#1":
        build = "prototype"
    r["source_build"] = build
    rc = RECAPTURE.get(k) if not r.get("extra") else None
    if k == "cheer fastcouch 16:9":
        rc = ("Android #1896", "2025-09-16T17:10:00Z", "marcus.bennett")
    r["recapture"] = {"build": rc[0], "at": rc[1], "by": rc[2], "pointer": BUILDS[rc[0]][1]} if rc else None
    current = (rc[0] if rc else build)
    r["current_build"] = current
    old = current in OLD
    music = r.get("audio_master") == "music_baked" and not rc
    if r["campaigns"] == ["Android US tablet"]:
        call = "Skip October"
    elif r.get("already_made_halloween"):
        call = "Reuse"
    elif old or music:
        call = "Refresh first"
    else:
        call = "Halloween version"
    r["call"] = call
    if r["kind"] in ("static", "end_card"):
        r["audio_master"] = "n/a" if r["kind"] == "static" else "sfx_only"
    if build in BUILDS:
        r["source_date"] = BUILDS[build][0]
        r["source_pointer"] = BUILDS[build][1]
    elif build == "prototype":
        r["source_date"] = "2024-12-05"
        r["source_pointer"] = B + "2024-12.json#/358"
    out.append(r)

# live-since: base post date, tablet / feed exports from the tablet campaign launch (Sep 9)
for r in out:
    if r.get("live_since"):
        continue
    ev = r.get("base_evidence") or []
    r["live_since"] = r.get("live_since_override") or ("2025-09-09" if r.get("seeded_variant") else None)
POSTED = {"couch boss 30": "2025-04-05", "couch alpha 30": "2025-04-07", "couch alpha 50": "2025-04-07",
          "balloons alpha 50": "2025-04-07", "balloons alpha 50 (1)": "2025-04-07", "barrel alpha 30": "2025-04-07",
          "couch marketing2 30s": "2025-04-08", "couch marketing2 endcard": "2025-04-08",
          "barrel alpha 30 endcard": "2025-04-08", "couch alpha 30 endcard": "2025-04-08",
          "balloons alpha 50 endcard": "2025-04-08", "balloons marketing2 endcard": "2025-04-08",
          "barrel marketing2 4:5": "2025-04-29", "barrel marketing2 16:9": "2025-04-29", "cheer 30p 9:16": "2025-05-29",
          "cheer fastcouch 9:16": "2025-07-28", "marcus.bennett 9:16": "2025-08-13", "boris fastcouch 9:16": "2025-09-12",
          "boris alin2 9:16": "2025-09-12", "boris fastcouch 16:9": "2025-09-12", "squirrelfail portrait": "2024-12-06",
          "squirrelfail landscape": "2024-12-06", "mrfluffernot portrait": "2024-12-09",
          "mrfluffernot landscape": "2024-12-09", "cinematicTutorial Ad 1": "2024-12-12",
          "tutorialCinematic portrait": "2024-12-17", "julia 1:1": "2025-06-06", "julia 4:5": "2025-06-06",
          "marcus portrait UA end card": "2025-07-31", "end card template 16:9": "2025-04-07", "end card 001": "2025-08-04"}
for r in out:
    if r["key"] in POSTED:
        r["live_since"] = POSTED[r["key"]]
    e = r.get("extra")
    if e:
        r["live_since"] = e.get("live") or (e["at"][:10] if e["batch"] == "recap" else "2025-09-09")

# ticket numbers: Sep 8 batch (roster order, boris excluded), archived, then the boris tickets on Sep 12
ads = [r for r in out if r["kind"] not in ("icon", "store_set")]
extras = [r for r in ads if r.get("extra")]
batch = [r for r in ads if not r["key"].startswith("boris") and not r.get("extra")]
late = [r for r in ads if r["key"].startswith("boris") and not r.get("extra")]
n = 793
for i, r in enumerate(batch):
    r["ticket"] = f"ART-{n}"
    r["ticket_created"] = f"2025-09-08T16:{(i * 1) % 60:02d}:00Z"
    n += 1
archived = []
for i, a in enumerate(ARCHIVED):
    archived.append(dict(a, ticket=f"ART-{n}", ticket_created=f"2025-09-08T16:{len(batch) + i:02d}:00Z"))
    n += 1
for i, r in enumerate(late):
    r["ticket"] = f"ART-{n}"
    r["ticket_created"] = f"2025-09-12T16:{20 + i:02d}:00Z"
    n += 1
assert n - 793 == 50, n
catchup = [r for r in extras if r["extra"]["batch"] == "catchup"]
recap = [r for r in extras if r["extra"]["batch"] == "recap"]
for i, r in enumerate(catchup):
    r["ticket"] = f"ART-{n}"
    r["ticket_created"] = f"2025-09-15T16:{i:02d}:00Z"
    n += 1
for r in sorted(recap, key=lambda x: x["extra"]["at"]):
    r["ticket"] = f"ART-{n}"
    r["ticket_created"] = r["extra"]["at"]
    n += 1
assert n == 855, n

# ticket comment texts (first comment: the capture note at creation; second: a re-capture or an upload note)
UPLOAD_NOTE = {"couch boss 30", "balloons alpha 50", "couch marketing2 30s", "cheer 30p 9:16", "julia 1:1",
               "squirrelfail landscape", "end card 001", "marcus.bennett 16:9", "mrfluffernot portrait", "couch alpha 30 endcard"}
for r in ads:
    b = r["source_build"]
    master = {"music_baked": "music baked into the master", "sfx_only": "SFX only, no music"}.get(r.get("audio_master"))
    if r["kind"] == "static":
        c1 = f"Made from {b} captures ({md(r['source_date'])})."
        if r.get("seeded_variant"):
            c1 = f"Re-export of Julia's Jun 6 static for this placement. Made from {b} captures ({md(r['source_date'])})."
    elif r["kind"] == "end_card":
        c1 = f"Rendered from {b} footage ({md(r['source_date'])}). Master: {master}."
    elif b == "prototype":
        c1 = f"Captured {md(r['source_date'])} from the prototype, before the first Match3D build. Master: {master}."
    elif r.get("capture_ref") == "date":
        c1 = f"Captured {md(r['source_date'])}. Master: {master}."
    else:
        c1 = f"Captured from {b} on {md(r['source_date'])}. Master: {master}."
    if r["key"].startswith("boris") and r.get("capture_ref") == "date":
        c1 = f"Captured {md(r['source_date'])}; Boris opening added Sep 11. Master: {master}."
    if r["key"] == "marcus.bennett 9:16":  # the master note lives in the cut's Slack thread (a reply-only fact)
        c1 = f"Captured from {b} on {md(r['source_date'])}. Master notes are in Frederick's Aug 13 thread in #zombie_marketing."
        r["master_note_in_thread"] = "C06DJBJL798/1755114007.441789"
    e = r.get("extra")
    if e and e["batch"] == "recap":   # cut from a September re-capture: Marcus's export note is the only comment
        c1 = (f"Exported {md(e['at'][:10])} from the {e['build']} re-capture of the {e['recap_of']}, same edit. "
              f"Master: SFX only, no music.")
        r["comment_1_by"], r["comment_1_at"] = "marcus.bennett", e["at"][:14] + "%02d:00Z" % (int(e["at"][14:16]) + 6)
    if not (e and e["batch"] == "recap"):   # Frederick's catalogue note carries the creative's Unity campaigns
        c1 = f"{c1} Unity: {', '.join(r['campaigns'])}."
    r["comment_1"] = c1
    if not r.get("comment_1_at"):   # catalogue note written by Frederick a minute after he opened the ticket
        hh, mm = int(r["ticket_created"][11:13]), int(r["ticket_created"][14:16]) + 1
        r["comment_1_by"], r["comment_1_at"] = "frederick.stone", f"{r['ticket_created'][:11]}{hh + mm // 60:02d}:{mm % 60:02d}:00Z"
    rc = r.get("recapture")
    if rc:
        r["comment_2"] = (f"Re-captured on {md(rc['at'][:10])} from {rc['build']}, same edit. Master: SFX only, no music."
                          if r["key"] != "cheer fastcouch 16:9" else
                          f"Exported {md(rc['at'][:10])} from the {rc['build']} re-capture of the 9:16. Master: SFX only, no music.")
        r["comment_2_by"] = rc["by"]
        r["comment_2_at"] = rc["at"]
    elif e and e["batch"] == "recap":
        mm = int(e["at"][14:16]) + 25
        r["comment_2"] = f"Uploaded to Unity {md(e['at'][:10])}: {', '.join(r['campaigns'])}."
        r["comment_2_by"] = "frederick.stone"
        r["comment_2_at"] = f"{e['at'][:11]}{int(e['at'][11:13]) + mm // 60:02d}:{mm % 60:02d}:00Z"
    elif r["key"] == "marcus portrait UA end card":   # revision 03: the sheet owner confirms the off-sheet card still serves
        r["comment_2"] = f"Still running on Unity: {', '.join(r['campaigns'])} (checked Sep 29). Not on the live creatives sheet yet."
        r["comment_2_by"] = "frederick.stone"
        r["comment_2_at"] = "2025-09-29T17:40:00Z"
    elif r["key"] in UPLOAD_NOTE:
        r["comment_2"] = f"Still running on Unity: {', '.join(r['campaigns'])} (checked Sep 9)."
        r["comment_2_by"] = "frederick.stone"
        r["comment_2_at"] = "2025-09-09T17:30:00Z"

# owners, assignment and due dates (ads that need new work are assigned to their maker; Reuse and Skip ads are not)
for r in out:
    k, c = r["kind"], r["call"]
    r["owner"] = "Martin Walsh" if k in ("icon", "store_set", "static") else "Marcus Bennett"
    if k == "icon":
        r["due"], r["route"] = "2025-10-16T12:00-07:00", "Oct 17 store build (merge cut Thu Oct 16 12:00 PT)"
    elif k == "store_set" and "iPad" in r["key"]:
        r["due"], r["route"] = "2025-10-16T12:00-07:00", "uploaded with the Oct 17 iOS submission (due by the Oct 16 12:00 PT cut)"
    elif k == "store_set" and "iPhone" in r["key"]:
        r["due"], r["route"] = "2025-10-16T12:00-07:00", "already exported; uploaded with the Oct 17 iOS submission (due by the Oct 16 12:00 PT cut)"
    elif k == "store_set":
        r["due"], r["route"] = None, "already exported; Google Play listing upload any day (1 day review), no fixed date"
    elif c == "Skip October":
        r["due"], r["route"] = None, "no Halloween version (Android US tablet ends Oct 12)"
    elif c == "Reuse":
        r["due"], r["route"] = "2025-10-15", "Halloween version already in the Halloween folder's UA masters; with Frederick by Wed Oct 15"
    else:
        r["due"], r["route"] = "2025-10-15", "with Frederick by Wed Oct 15 for the Oct 18-31 flight"

for r in out:
    r["status"] = "made" if r["call"] == "Reuse" else ("none" if r["call"] == "Skip October" else "to make")
    if r.get("comment_2_at"):
        assert r["comment_2_at"] > r["comment_1_at"] > r["ticket_created"], (r["key"], r["comment_2_at"], r["ticket_created"])
    if r.get("ticket"):
        assert r["comment_1_at"] > r["ticket_created"] and r["comment_1_at"] < "2025-10-01T00:00:00Z", r["key"]
    r["assign_to"] = r["owner"] if (r.get("ticket") and r["call"] in ("Halloween version", "Refresh first")) else None
for r in out:
    why = {"Skip October": "runs only on Android US tablet, which ends Oct 12",
           "Reuse": "Halloween version already made" if r["kind"] not in ("store_set",) else "Halloween store export already made",
           "Refresh first": ("music baked into the master" if r.get("audio_master") == "music_baked" and not r.get("recapture")
                             else f"newest source {r.get('current_build')} is older than Android #1452 / iOS 1232"),
           "Halloween version": (f"newest source {r.get('current_build')} is current" if r.get("ticket") else "new seasonal piece")}[r["call"]]
    if r["call"] == "Refresh first" and r.get("audio_master") == "music_baked" and r.get("current_build") in OLD:
        why = f"newest source {r.get('current_build')} predates the swap and the music is baked in"
    r["notes"] = why
doc = {"surfaces": out, "archived": archived, "builds": BUILDS}
(HERE / "roster_final.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
print("roster_final:", len(out), dict(Counter(r["call"] for r in out)), "| tickets", sum(1 for r in out if r.get("ticket")),
      "+ archived", len(archived), "| recaptured", sum(1 for r in out if r.get("recapture")),
      "| second comments", sum(1 for r in out if r.get("comment_2")))
