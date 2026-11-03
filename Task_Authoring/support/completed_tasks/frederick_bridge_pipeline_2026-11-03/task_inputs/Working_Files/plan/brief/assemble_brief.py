#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md from brief_body.md + the pasted tool outputs. Keeps an existing
pasted STAGE GATE block only if asked (--keep-gate); the gate's --paste re-adds it."""
import re
from pathlib import Path
B = Path(__file__).resolve().parent
OUT = B.parents[1] / "04_Prompt_Writing_Brief.md"
body = (B / "brief_body.md").read_text()
rows = (B / "search_rows.md").read_text().strip().splitlines()
rows = [re.sub(r"\| None \|", "| n/a (--no-hidden) |", r) for r in rows]
out_txt = (B / "search_out.txt").read_text().strip()
ent = (B / "entity_out.txt").read_text().strip()
out_txt = out_txt.replace("```", "'''"); ent = ent.replace("```", "'''")
assert "```" not in out_txt and "```" not in ent
doc = body.replace("{{SEARCH_ROWS}}", "\n".join(rows)).replace("{{SEARCH_OUT}}", out_txt).replace("{{ENTITY_OUT}}", ent)
assert "{{" not in doc
OUT.write_text(doc if doc.endswith("\n") else doc + "\n")
print(OUT, len(doc.splitlines()), "lines")
