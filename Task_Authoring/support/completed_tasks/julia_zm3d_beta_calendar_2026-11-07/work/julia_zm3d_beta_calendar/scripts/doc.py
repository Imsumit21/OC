#!/usr/bin/env python3
"""Fetch one gsheets spreadsheet (or gdocs doc) record by drive file id.

Usage: doc.py gsheets f_xxx        -> prints chosen summary (sheets, dims, row count)
       doc.py gsheets-raw f_xxx    -> full record
       doc.py gdocs f_xxx
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hgget import get, search

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw")


def idx_for(service, file, fid):
    d = search(service, fid, file=file, limit=3)
    for m in d.get("matches", []):
        p = m["pointer"]
        if p.endswith("/drive_file_id") or p.endswith("/document_id"):
            return p.rsplit("/", 1)[0]
    return None


def main():
    mode, fid = sys.argv[1], sys.argv[2]
    if mode == "gdocs":
        docs = json.load(open(os.path.join(RAW, "gdocs.json")))["docs_documents"]
        for d in docs:
            if d.get("document_id") == fid:
                print(json.dumps(d, indent=1))
                return
        print("not found")
        return
    ptr = idx_for("gsheets", "data.json", fid)
    if not ptr:
        print("not found")
        return
    rec = get("gsheets", "data.json", ptr)
    if mode == "gsheets-raw":
        print(json.dumps(rec, indent=1))
        return
    print("id:", rec.get("drive_file_id"), "| owner:", rec.get("owner_email"), "| modified:", rec.get("modified_time"))
    print("shared_with:", len(rec.get("shared_with_emails") or []), "julia:", "julia.lawson@harmonygames.co" in (rec.get("shared_with_emails") or []))
    for s in rec.get("sheets", []):
        g = s.get("grid") or []
        print(f"-- tab {s.get('title')!r}: rows={len(g)} cols={s.get('column_count')} frozen?")
        for r in g[:6]:
            print("   ", [str(c)[:28] for c in r[:9]])


if __name__ == "__main__":
    main()
