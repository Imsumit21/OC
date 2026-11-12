#!/usr/bin/env python3
"""One-off D3 edit (path exposure at injection, rev2): Brian's log no longer names the three recoloured items, because
'Chainsaw' and 'Cone' are line names and a run searching an item name would land on the log (path_exposure.py EXPOSED A1).
The log says 'the three recoloured models'; which three is in Robert's base post. Applies the wording to every generator
that quotes it. Idempotent: a second run finds nothing to replace and says so."""
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
OLD_LOG = "Tue 30 Sep: Claire sent the cactus, the chainsaw and the cone again with the new colours. Opened them, they look right, "
NEW_LOG = "Tue 30 Sep: Claire sent the three recoloured models again. Opened them, they look right, "
EDITS = {
    HERE / "planned_texts.py": [(OLD_LOG, NEW_LOG)],
    WF / "solver" / "solver.py": [('"REVISED": ("body_text", "the cone again with the new colours")', '"REVISED": ("body_text", "the three recoloured models again")')],
    HERE / "build_final_manifest.py": [('"value": "Claire sent the cactus, the chainsaw and the cone again with the new colours"', '"value": "Claire sent the three recoloured models again"')],
    HERE / "literal_sweep.py": [('"new_colours": "with the new colours"', '"recoloured_models": "three recoloured models"')],
    HERE / "citation_chronology.py": [("'Claire sent the cactus, the chainsaw and the cone again with the new colours'", "'Claire sent the three recoloured models again'")],
    HERE / "build_surface.py": [("than the cactus and the cone: the join is the log's item names", "than the cactus and the cone: the log says only 'the three recoloured models', so the join is Robert's post")],
    HERE / "build_manifest.py": [
        ("Tue 30 Sep: Claire sent the cactus, the chainsaw and the cone again with the new colours; they open, look right and replace Thursday's",
         "Tue 30 Sep: Claire sent the three recoloured models again; they open, look right and replace Thursday's (which three: Robert's post)"),
        ("Claire sent the three again with the new colours, they open and look right and they replace Thursday's, so each is Ready",
         "Claire sent the three recoloured models again, they open and look right and they replace Thursday's; Robert's post says which three; so each is Ready"),
        ('"signature": "Claire sent the cactus, the chainsaw and the cone again with the new colours"', '"signature": "Claire sent the three recoloured models again"')],
    HERE / "review_content.py": [
        ("says Claire sent the cactus, the chainsaw and the cone again with the new colours, that he opened them, that they look right and that they replace Thursday's.",
         "says Claire sent the three recoloured models again, that he opened them, that they look right and that they replace Thursday's; which three is in Robert's post (cactus, chainsaw, cones).")],
    HERE / "assemble_design.py": [
        ("joining 'the cactus, the chainsaw and the cone' to three lines in three categories", "joining 'the three recoloured models' through Robert's post to three lines in three categories"),
        ("Brian's log of 30 Sep, the latest record: Claire sent the three again, they open, look right and replace Thursday's.",
         "Brian's log of 30 Sep, the latest record: Claire sent the three recoloured models again, they open, look right and replace Thursday's (Robert's post says which three).")],
}
done, missing = 0, []
for path, pairs in EDITS.items():
    s = path.read_text()
    for a, b in pairs:
        if s.count(a) == 1:
            s = s.replace(a, b); done += 1
        elif b not in s:
            missing.append((path.name, a[:70]))
    path.write_text(s)
print(f"applied {done}; not found and not already applied: {missing or 'none'}")
