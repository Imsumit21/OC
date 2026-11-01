"""Fills dossier_body.md with the verbatim tool outputs and writes Working_Files/01_Grounding_Dossier.md."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
O = HERE / 'out'
body = (HERE / 'dossier_body.md').read_text()
for k, f in [('{CHECKSQL}', 'checksql.txt'), ('{FACTCHECK}', 'fact_check.txt'), ('{SQLLINT}', 'sql_lint.txt'),
             ('{BASECHECK}', 'base_check.txt'), ('{HARDNESS}', 'hardness.txt')]:
    body = body.replace(k, (O / f).read_text().rstrip('\n'))
assert '{' not in ''.join(l for l in body.splitlines() if l.startswith('{') and l.endswith('}')), 'unfilled'
(ROOT / 'task_inputs/Working_Files/01_Grounding_Dossier.md').write_text(body)
print('ok', len(body))
