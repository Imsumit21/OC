"""Scan every seeded statement in 01_Universe_Inject.sql for relative-time words. Run: python3 reltime_scan.py [sql]"""
import pathlib
import re
import sys

SQL = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[2] / "01_Universe_Inject.sql"
WORDS = (r"this morning|tonight|yesterday|today|last night|tomorrow|this afternoon|this evening|this week|last week|next week|"
         r"weekend|monday|tuesday|wednesday|thursday|friday|saturday|sunday|\bmon\b|\btue\b|\bwed\b|\bthu\b|\bfri\b|\bsat\b|\bsun\b|"
         r"bu sabah|bu akşam|bu gece|dün|yarın|bugün|pazartesi|salı|çarşamba|perşembe|cuma|cumartesi|pazar|hafta|sabah|akşam|gece|"
         r"earlier|just now|an hour ago|minutes ago")
TS = re.compile(r"'(20\d\d-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z?)'")
for n, line in enumerate(SQL.read_text(encoding="utf8").splitlines(), 1):
    hits = list(re.finditer(WORDS, line, re.I))
    if not hits:
        continue
    ts = TS.findall(line)
    tbl = re.match(r"(INSERT INTO|UPDATE) (\S+)", line)
    print(f"--- L{n} {tbl.group(2) if tbl else '?'} ts={ts[:3]}")
    for m in hits:
        a, b = max(0, m.start() - 90), min(len(line), m.end() + 60)
        print("   ", repr(line[a:b]))
