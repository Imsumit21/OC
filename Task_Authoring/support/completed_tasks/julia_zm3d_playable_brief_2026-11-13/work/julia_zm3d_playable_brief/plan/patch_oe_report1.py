#!/usr/bin/env python3
"""Platform /oe round 1 (eval_reports/6aea4c201e1fa1ddfdd0a25d_2_oe.md, FAIL 2): fix list, verbatim:
  1. OE 20, purpose clause. Replace the part from "or, in the team's words of Sep 22" through "either wording of the purpose
     is accepted" with a single purpose and no alternative. [...] Trap: Julia's "more hardcore friendly playable" line was
     walked back by Robert three minutes later, so a brief that asks PlayableX for a more hardcore-leaning playable is wrong.
  2. OE 10, add the walk-back. [...] Robert, 12:37 PM PT, ts 1758569872.578829: "Doesn't really matter"; Robert, 12:38 PM PT,
     ts 1758569885.985319: "I think we should remain as is".
  3. No data or injection change is needed.
The 'both fair' reading came from my own coherence-sweep decision (fork F30); the same decision widened slot B2b and the
prompt brief's accepted outcome. Every sibling goes back to the one purpose here: the surface slot, the sweep fork, the
brief row, and the OE generators (facts, events, ledger). Idempotent; prints what was applied."""
from pathlib import Path
PLAN = Path(__file__).resolve().parent
OEG = PLAN.parent / "oe_gen"

def apply(path, pairs):
    s = path.read_text(); done, skipped, missing = 0, 0, []
    for a, b in pairs:
        if s.count(a) == 1:
            s = s.replace(a, b); done += 1
        elif b.split("\n")[0] in s:
            skipped += 1
        else:
            missing.append(a[:90])
    path.write_text(s)
    print(f"{path.name}: applied {done}, already {skipped}, missing {missing}")

# ---- the gradable surface: one purpose; 'hardcore' no longer satisfies the slot
apply(PLAN / "build_surface.py", [(
 '''slot("B2b", "brief: what the scenario is for", 3, INT, "Frederick's 12 Sep reasoning (filter for players who will like the game, true to the core game play) or, equally, the 22 Sep #zombie-design agreement (test the game as it is and its audience fit, a more hardcore-friendly playable)",
     "write_content", ["text", "brief", "filter|retention|core game ?play|core mechanic|audience fit|hardcore|current form|as it is"], "core", [], ASK_SPAN, fact_id="scenario_purpose")''',
 '''slot("B2b", "brief: what the scenario is for", 3, INT, "Frederick's 12 Sep reasoning: filter for players who will like the game, true to the core game play; a test of the game in its current form and its audience fit (Robert, 22 Sep: 'I think we should remain as is'; the ask: 'Write it for the game as it is today'). Julia's 'more hardcore friendly playable' of 22 Sep is walked back in the same thread and is not the purpose",
     "write_content", ["text", "brief", "filter|retention|core game ?play|core mechanic|audience fit|current form"], "core", [], ASK_SPAN, fact_id="scenario_purpose")''')])

# ---- the coherence sweep: F30 is settled, not both fair
fm = PLAN / "build_findings_map.py"; s = fm.read_text()
if 'dict(id="F30", title="What the scenario is for", any=["which scenario we picked", "what it is for", "scenario"], material=True, status="both_fair",' in s:
    i = s.index('dict(id="F30"'); j = s.index('how="slot B2b accepts either wording (01_Gradable_Surface.json); the rubric stage carries the same pair"),', i)
    j += len('how="slot B2b accepts either wording (01_Gradable_Surface.json); the rubric stage carries the same pair"),')
    s = s[:i] + '''dict(id="F30", title="What the scenario is for", any=["which scenario we picked", "what it is for", "scenario"], material=True, status="settled_in_data",
      record_ids=[ASK, B["fred_retention"], B["fred_scenario1"], "C090N54TG79/1758569655.409719", "C090N54TG79/1758569707.508219", B["julia_shuriken_idea"], "C090N54TG79/1758569872.578829", B["robert_remain"]],
      reading_a=rd("Frederick to the vendor, 12 Sep: a playable that filters out the players who won't like the game while staying true to the core game play; Robert, 22 Sep: test the current form and audience fit, not what the game could be tailored to become", "the brief gives that purpose"),
      reading_b=rd("Julia's 22 Sep line in the same thread: a more hardcore friendly playable", "the brief asks PlayableX for a more hardcore-leaning playable"),
      reason="the purpose sentence PlayableX builds from",
      settled=settled([ASK]), how="Robert answers in the same thread three minutes later ('Doesn't really matter', 'I think we should remain as is'), and Frederick's ask says 'Write it for the game as it is today'; the platform's /oe round 1 read it the same way (reading b refuted). Rev2 had marked this fork both fair, which was wrong"),''' + s[j:]
    fm.write_text(s); print("build_findings_map.py: F30 settled")
else:
    print("build_findings_map.py: F30 already settled" if 'id="F30"' in s and 'status="settled_in_data"' in s[s.index('id="F30"'):s.index('id="F30"') + 200] else "build_findings_map.py: F30 ANCHOR MISSING")

# ---- the prompt brief: one accepted purpose
apply(PLAN / "assemble_brief.py", [(
 '''    ("W1", "what it is for", f"filtering for players who will like the game while staying true to the core game play ({B['fred_retention']}), or the 22 Sep #zombie-design agreement: test the game as it is and its audience fit, more hardcore-friendly (C090N54TG79/1758569655.409719, C090N54TG79/1758569707.508219)", "—", "either purpose, in any wording: both fair (sweep fork F30, slot B2b accepts both)", "material in substance, representational in wording"),''',
 '''    ("W1", "what it is for", f"filtering for players who will like the game while staying true to the core game play ({B['fred_retention']}); a test of the game in its current form and its audience fit, not what it could be tailored to become (Robert, 22 Sep, {B['robert_remain']}: 'I think we should remain as is'; the ask: 'Write it for the game as it is today')", "—", "any wording of that one purpose; a brief that asks PlayableX for a more hardcore-leaning playable is wrong (Julia's 22 Sep line, walked back by Robert in the same thread; sweep fork F30, settled)", "material in substance, representational in wording"),''')])

# ---- OE generators: read Robert's 12:37 reply; the purpose fact; OE 10 and OE 20; the ledger's risk and trap rows
apply(OEG / "base_read.py", [(
 '''EXTRA_SLACK = {"purpose_robert_22sep": "C090N54TG79/1758569655.409719", "purpose_julia_22sep": "C090N54TG79/1758569707.508219"}''',
 '''EXTRA_SLACK = {"purpose_robert_22sep": "C090N54TG79/1758569655.409719", "purpose_julia_22sep": "C090N54TG79/1758569707.508219",
               "purpose_robert_matter": "C090N54TG79/1758569872.578829"}     # /oe round 1: Robert's walk-back, with robert_remain''')])
apply(OEG / "facts.py", [
 ('''fs = O.base("fred_scenario1"); fr = O.base("fred_retention"); p22r = O.base("purpose_robert_22sep"); p22j = O.base("purpose_julia_22sep")''',
  '''fs = O.base("fred_scenario1"); fr = O.base("fred_retention"); p22r = O.base("purpose_robert_22sep"); p22j = O.base("purpose_julia_22sep")
p22q = O.base("julia_shuriken_idea"); p22m = O.base("purpose_robert_matter"); p22s = O.base("robert_remain")'''),
 ('''    f"The same purpose in the team's words, #zombie-design ({O.DESIGN_CH}), thread of {O.day_pt(p22r['ts'])}: {p22r['id']} by {p22r['user']} (Robert): '{p22r['text']}'; "
    f"{p22j['id']} by {p22j['user']} (Julia Lawson): '{p22j['text']}'. Both fair: either wording of the purpose is accepted (sweep fork F30).",
    BASE_SLACK, "YES (channel member; can-see)", "{F:notes}", f"{fr['src']}; {p22r['src']}; {p22j['src']}")''',
  '''    f"The team's thread of {O.day_pt(p22r['ts'])} in #zombie-design ({O.DESIGN_CH}), in order: {p22r['id']} by {p22r['user']} (Robert): '{p22r['text']}'; "
    f"{p22j['id']} by {p22j['user']} (Julia Lawson): '{p22j['text']}'; {p22q['id']} by {p22q['user']} (Julia Lawson): '{p22q['text']}'; "
    f"{p22m['id']} by {p22m['user']} (Robert): '{p22m['text']}'; {p22s['id']} by {p22s['user']} (Robert): '{p22s['text']}'. With the ask's 'Write it for the game as it is today' ({{F:ask}}), "
    "the purpose is one: filter for the players who will like the game, true to the core game play, testing the game in its current form and its audience fit; the hardcore-friendly line is walked back.",
    BASE_SLACK, "YES (channel member; can-see)", "{F:notes}, {F:ask}", f"{fr['src']}; {p22r['src']}; {p22j['src']}; {p22q['src']}; {p22m['src']}; {p22s['src']}")'''),
])
apply(OEG / "draft_oe.py", [
 ('''rc, p22r, p22j = O.base("robert_new_colours"), O.base("purpose_robert_22sep"), O.base("purpose_julia_22sep")''',
  '''rc, p22r, p22j = O.base("robert_new_colours"), O.base("purpose_robert_22sep"), O.base("purpose_julia_22sep")
p22q, p22m, p22s = O.base("julia_shuriken_idea"), O.base("purpose_robert_matter"), O.base("robert_remain")'''),
 ('''   f"{Q(p22j['text'], 'do a more hardcore friendly playable and see how they do with the funnel')}. "''',
  '''   f"{Q(p22j['text'], 'do a more hardcore friendly playable and see how they do with the funnel')}; Julia Lawson, {pt(p22q['ts'])}, ts {p22q['ts']}: "
   f"{Q(p22q['text'], 'Do you want to try a cute level with lots of grenades and shruiken then?')}; Robert, {pt(p22m['ts'])}, ts {p22m['ts']}: {Q(p22m['text'], 'Doesn' + chr(39) + 't really matter')}; "
   f"Robert, {pt(p22s['ts'])}, ts {p22s['ts']}: {Q(p22s['text'], 'I think we should remain as is')}. So the playable tests the game in its current form and its audience fit; the "
   f"hardcore-friendly line is walked back (with the ask's {Q(ASK, 'Write it for the game as it is today')}, OE {n_ask}). "'''),
 ('''   ["purpose", "picks", "zpicks", "c1"], [p22r["id"], p22j["id"], O.PICKS["id"], O.ZPICKS["id"], rc["id"]])''',
  '''   ["purpose", "picks", "zpicks", "c1"], [p22r["id"], p22j["id"], p22q["id"], p22m["id"], p22s["id"], O.ASK["id"], O.PICKS["id"], O.ZPICKS["id"], rc["id"]])'''),
 ('''   f"(OE {n_thr1}), or, in the team's words of Sep 22, to test the current form and audience fit with a more hardcore friendly playable (OE {n_design}); either wording of the purpose is accepted; "''',
  '''   f"(OE {n_thr1}), and there to test the game in its current form and its audience fit, not what the game could be tailored to become (OE {n_design}); "'''),
])
apply(OEG / "assemble_ledger.py", [
 ('''("8", "What the scenario is for has two fair wordings: Frederick's of Sep 12 and the team's of Sep 22 in #zombie-design (coherence sweep fork F30, both fair)", F("purpose"), "rubric (accept both)", "rubric stage"),''',
  '''("8", "What the scenario is for: Julia's Sep 22 'more hardcore friendly playable' line could be taken for the purpose; it is walked back in the same thread (trap T20), so the brief carries one purpose (platform /oe round 1)", F("purpose"), "OE accuracy / rubric", "settled: OE 10 and OE 20 carry the one purpose"),'''),
 ('''raised as UNSURE by the rev2 blind O3 pass and resolved here: DES-325 stays Ready"),
]''',
  '''raised as UNSURE by the rev2 blind O3 pass and resolved here: DES-325 stays Ready"),
 ("T20", f"Julia's Sep 22 line 'let's do a more hardcore friendly playable' (C090N54TG79/1758569707.508219) reads as what the playable is for", F("purpose"),
  "Robert answers in the same thread three minutes later, 'Doesn't really matter' (C090N54TG79/1758569872.578829) and 'I think we should remain as is' (C090N54TG79/1758569885.985319); the ask says 'Write it for the game as it is today'"),
]'''),
 ('''"Unresolved: none blocking. Open risks 1, 2, 5, 6, 8 and 9 go to the rubric stage; 3 and 4 are kept off every Expected line.", ""]''',
  '''"Unresolved: none blocking. Open risks 1, 2, 5, 6 and 9 go to the rubric stage; 3 and 4 are kept off every Expected line; 8 is settled on OE 10 and OE 20 (platform /oe round 1).", ""]'''),
])
