#!/usr/bin/env python3
"""One-off D3 / rev2 edit of plan/build_findings_map.py: the designed-supersession forks and the open sets that quote
seeded spans now match the rev2 records (Robert's note, Marcus's reworded post, Brian's log with the re-send). Idempotent."""
from pathlib import Path
P = Path(__file__).resolve().parent / "build_findings_map.py"
s = P.read_text()
E = [
 ('''dict(id="F15", title="EXPORT: twelve files saved out of the project", any=["saved out of the project", "saved out of unity", "text kind"],''',
  '''dict(id="F15", title="EXPORT: twelve files saved out of the project", any=["saved out of the project", "got out of unity", "text kind"],'''),
 ('''      reading_b=rd("Marcus's later post: those files are the text kind; the vendor takes binary FBX only; Marcus addresses Brian and names the exporter setting", "Owed: export again as binary, Brian"),''',
  '''      reading_b=rd("Marcus's later post: the models Brian got out of Unity on Thursday are the text kind (the default setting); the vendor takes binary FBX only", "Owed: export again as binary, Brian"),'''),
 ('''dict(id="F16", title="ARTHOLD: twelve bathroom files", any=["bathroom", "banyo"], material=True, status="settled_in_data",''',
  '''dict(id="F16", title="ARTHOLD: twelve bathroom files", any=["bathroom", "uvs", "redoing the uv"], material=True, status="settled_in_data",'''),
 ('''      reading_a=rd("Brian's notes of Fri 26 Sep stand", "Ready"), reading_b=rd("Claire's later message: she is redoing the UVs and Friday's bathroom files are the old state", "Owed, Claire"),
      reason="designed (anchor A2)", settled=settled([A2]), how="Claire's message to Julia of 29 Sep, in their DM"),''',
  '''      reading_a=rd("Brian's notes of Fri 26 Sep stand", "Ready"), reading_b=rd("Robert's later note: Claire is redoing the UVs on the bathroom objects and the files she gave Brian on Friday are the old version", "Owed, Claire (the file came from her)"),
      reason="designed (anchor A2)", settled=settled([A2]), how="Robert's note to Julia of 29 Sep, in their DM; the notes leave a changed file with whoever it came from"),'''),
 (''' dict(key="changed", any=["if the art changed"], where=NOTES, span="If the art changed after a file went out or was exported (a fix, a retexture, new colour versions), it goes again", rule="a line whose art changed after the date of Brian's note: the three recoloured lines (match3d#462).''',
  ''' dict(key="changed", any=["if the art changed"], where=NOTES, span="If the art changed after a file went out or was exported (a fix, a retexture, new colour versions), it goes again", rule="a line whose art changed after the date of Brian's note: the three recoloured lines (Robert's 29 Sep post), which went again on 30 Sep (Brian's log) and are Ready; and'''),
 (''' dict(key="thursday", any=["saved out of unity on thursday"], where=A1, span="the models you saved out of unity on thursday",''',
  ''' dict(key="thursday", any=["got out of unity on thursday", "saved out of unity on thursday"], where=A1, span="the models you got out of unity on thursday",'''),
 (''' dict(key="banyo", any=["banyo objeleri"], where=A2, span="banyo objelerinin",''',
  ''' dict(key="banyo", any=["banyo objeleri", "the bathroom objects"], where=A2, span="the UVs on the bathroom objects",'''),
 (''' dict(key="clairetickets", any=["ticketlara"], where=A2, span="ticketlara",''',
  ''' dict(key="clairetickets", any=["ticketlara", "files she gave"], where=A2, span="the bathroom files she gave",'''),
]
done, skipped, missing = 0, 0, []
for a, b in E:
    if s.count(a) == 1:
        s = s.replace(a, b); done += 1
    elif b in s:
        skipped += 1
    else:
        missing.append(a[:100])
P.write_text(s)
print(f"applied {done}, already applied {skipped}, missing {missing}")
