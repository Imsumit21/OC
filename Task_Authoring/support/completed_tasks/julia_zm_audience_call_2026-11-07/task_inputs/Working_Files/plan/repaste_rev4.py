"""Replace the dossier's pasted tool-output blocks with the current plan/out files (rev4), keeping the hand-written text."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "out"
DOS = HERE.parent / "01_Grounding_Dossier.md"


def out(name):
    return (OUT / name).read_text(encoding="utf8").rstrip()


big = [out(n) for n in ("hardness_gate.txt", "oracle_kit.txt", "mutation.txt", "liveness.txt", "v2.txt")]
for extra in ("forecast.txt", "preflight.txt"):
    if (OUT / extra).is_file():
        big.append(out(extra))
# (prefix of the line that introduces the block, new block text)
targets = [
    ("`python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson", out("check_sql.txt")),
    ("`python3 Task_Authoring/tools/fact_check.py", out("fact_check.txt")),
    ("`python3 Task_Authoring/tools/sql_lint.py", out("sql_lint.txt")),
    ("`python3 Task_Authoring/tools/base_check.py", out("base_check.txt")),
    ("`python3 Task_Authoring/tools/base_claims.py", out("base_claims.txt")),
    ("One block, in order: `hardness_gate.py`", "\n\n".join(big)),
]
lines = DOS.read_text(encoding="utf8").split("\n")
for prefix, text in targets:
    hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    i = hits[0] + 1
    while not lines[i].startswith("```"):
        i += 1
    j = i + 1
    while not lines[j].startswith("```"):
        j += 1
    lines[i:j + 1] = ["```text"] + text.split("\n") + ["```"]
    print("replaced", prefix[:50], "->", len(text.split("\n")), "lines")
DOS.write_text("\n".join(lines), encoding="utf8", newline="\n")
