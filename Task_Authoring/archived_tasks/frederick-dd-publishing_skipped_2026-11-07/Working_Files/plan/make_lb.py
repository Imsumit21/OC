#!/usr/bin/env python3
"""Writes plan/load_bearing.txt: the load-bearing rows in the services persona_view check-sql reads (Drive family, Slack, Gmail, Calendar)."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'Task_Authoring/tools')); sys.path.insert(0, str(ROOT / 'Task_Authoring/task_inputs/Working_Files/solver'))
import solver as S
ids = []
for r in S.RULES:
    for k in sorted(S.TOUCHED[r]):
        ids += S.deciding(None, r, k)
ids += [S.I['rule_doc'], S.I['outreach_sheet'], S.I['dd_folder'], S.I['onepager_deck'], S.MSG['hub']] + [S.B.term(k) for k in S.B.TERM_DOCS]
skip = (S.I['anika_contact'], S.I['eng2362_comment'], S.I['sunfold_comment'], S.I['dd_card'], S.I['oakline_card'], S.I['sunfold_card'])
(Path(__file__).parent / 'load_bearing.txt').write_text('\n'.join(x for x in dict.fromkeys(ids) if x not in skip) + '\n')
