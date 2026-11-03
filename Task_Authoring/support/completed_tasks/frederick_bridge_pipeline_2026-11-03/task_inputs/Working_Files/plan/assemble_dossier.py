#!/usr/bin/env python3
"""Assemble 01_Grounding_Dossier.md from dossier_body.md, the record ledger (sql_ids.json) and verbatim tool outputs."""
import json
from pathlib import Path
P = Path(__file__).resolve().parent; WF = P.parent
d = json.loads((P / "sql_ids.json").read_text())
ELEM = {
 'gdrive.drive_files': ('H1/T9/K13/K11/R5/T4 files', '●', 'authority · decoy · write target'),
 'gdocs.docs_documents': ('H1 template, July decoy (T9), README (K13)', '●', 'authority · decoy'),
 'gsheets.sheets_spreadsheets': ('T1/T4 stale angels sheet', '●', 'claim met first'),
 'gsheets.sheets_sheets': ('T1/T4 stale angels sheet tab', '●', 'claim met first'),
 'gsheets.sheets_sheets (UPDATE)': ('2025 list grid, LVP Latest Status 09/07 -> 09/09 (rev8, SC-10)', '○ (base list)', 'coherence fix'),
 'gslides.slides_presentations': ('K11 draft deck', '●', 'connecting'),
 'gslides.slides_pages': ('K11 draft deck slide (notes ○)', '○', 'connecting'),
 'gslides.slides_page_elements': ('K11 draft deck text', '●', 'connecting'),
 'slack.slack_messages': ('T1/T4 post, D2 aside, settling posts, T3 reply, T4 DM, T2/K15 post', '●', 'claim met first · overturning'),
 'trello.trello_actions': ('H2 rule comment / K10 deck card actions', '●', 'authority · connecting'),
 'trello.trello_cards': ('K10 Board Deck - Oct 14 card', '●', 'connecting'),
 'trello.trello_checklists': ('K10 deck sections checklist', '●', 'connecting'),
 'trello.trello_check_items': ('K10 deck sections items', '●', 'connecting'),
 'gmail.gmail_threads': ('A1 hub, T1/T5/T2/T6 mails, D5, INT-11 invitations', '●', 'first link · evidence'),
 'gmail.gmail_messages': ('A1 hub, T1/T5/T2/T6 mails, D5, INT-11 invitations', '●', 'first link · evidence'),
 'gcal.gcal_events': ('T6 Brightwater call, K12 review event', '● (time/attendees)', 'evidence · deadline'),
 'linear.linear_issues': ('T2 ZOM-567 (done source)', '●', 'claim met first'),
 'linear.linear_comments': ('T2 ZOM-567 comments (done source)', '●', 'claim met first'),
 'contacts.contacts': ('T5/T6/T11 partner mappings', '○ (job)', 'connecting'),
}
rows, n = [], 0
for table, keys in d['rows'].items():
    for k in keys:
        n += 1
        e, c, r = ELEM[table]
        kk = k if table != 'linear.linear_comments' else f"{k} (ZOM-567)"
        rows.append(f"| {n} | {table} | {kk} | {e} | {c} | {r} |")
body = (P / "dossier_body.md").read_text()
for key, f in {"{{CHECKSQL}}": "checksql.txt", "{{FACTCHECK}}": "fact_check.txt", "{{SQLLINT}}": "sql_lint.txt",
               "{{BASECHECK}}": "base_check.txt", "{{BASECLAIMS}}": "base_claims.txt", "{{HGATE}}": "hardness_gate_full.txt", "{{HGLINT}}": "hglint.txt"}.items():
    body = body.replace(key, (P / f).read_text().rstrip())
mut = (P / "mutation.txt").read_text().rstrip().splitlines()
body = body.replace("{{MUTATION}}", "\n".join(l for l in mut[-12:] if "dispositions:" not in l))
body = body.replace("{{LEDGER}}", "\n".join(rows))
(WF / "01_Grounding_Dossier.md").write_text(body)
print("dossier", len(body), "chars,", n, "ledger rows")
