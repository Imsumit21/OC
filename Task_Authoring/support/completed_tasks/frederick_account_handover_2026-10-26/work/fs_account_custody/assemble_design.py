"""Assemble 01_Scenario_Design.md from design_body.md, minted ids and verbatim tool outputs (re-run here)."""
import json, os, subprocess, sys
W = os.path.dirname(os.path.abspath(__file__)); WS = os.path.abspath(os.path.join(W, "..", "..", "..", ".."))
TA = os.path.join(WS, "Task_Authoring-2"); OUT = os.path.join(TA, "task_inputs", "Working_Files", "01_Scenario_Design.md")
I = json.load(open(os.path.join(W, "minted_ids.json")))
def run(*a):
    r = subprocess.run([sys.executable, *a], cwd=WS, capture_output=True, text=True); return (r.stdout + r.stderr).rstrip()
fence = lambda s: "```\n" + s + "\n```"
reach = run("Task_Authoring-2/tools/persona_view.py", "reach", "frederick_stone", "--top", "10")
gate = run("Task_Authoring-2/tools/hardness_gate.py", "Task_Authoring-2/task_inputs/Working_Files/01_Hardness_Manifest.draft.json", "--design")
coll = run("Task_Authoring-2/tools/entity.py", "collisions").split("\nTOKENS_MAPPING")[0]
res = "\n".join(run("Task_Authoring-2/tools/entity.py", "resolve", p).splitlines()[0] for p in ("Leonard Hayes", "Arthur Blake", "Frederick Stone"))
ids = ["slack D05S58U4SAK/1759096868.688389", "slack D05S58U4SAK/1759170013.491159", "slack D05S58U4SAK/1758922541.613439",
       "slack C07C2866011/1759186080.203099", "slack C07C2866011/1759264050.305069", "slack C07UCC631A6/1757346020.196019",
       "slack C07UCC631A6/1757347560.891949", "slack C07UCC631A6/1757349668.681539", "slack C07C2866011/1759110509.707539",
       "gmail frederick.stone@harmonygames.co/1843428112007517388", "gmail frederick.stone@harmonygames.co/1843223812315546201",
       "gmail frederick.stone@harmonygames.co/1835153849970828373", "gmail frederick.stone@harmonygames.co/1838369017520543217",
       "gmail frederick.stone@harmonygames.co/1841349862518331350", "gmail frederick.stone@harmonygames.co/1837038650805365569",
       "trello 67cf1b506d78ad3c72e02a35", "trello 670010236b89198587ca45b6"]
cansee = "\n".join(run("Task_Authoring-2/tools/persona_view.py", "can-see", "frederick_stone", *x.split()).splitlines()[0] for x in ids)
red = open(os.path.join(W, "redteam_section.md")).read() if os.path.exists(os.path.join(W, "redteam_section.md")) else "RED TEAM UNAVAILABLE: redteam_review: set REDTEAM_MODEL or pass --model (no REDTEAM_* environment configured — error)"
sub = {"{REACH}": fence(reach), "{GATE}": fence(gate), "{ENTITY}": fence(coll + "\n" + res), "{CANSEE}": fence(cansee), "{REDTEAM}": red,
       "{HUB_TS}": I["S_HUB"]["ts"], "{CLAIM_TS}": I["S_CLAIM"]["ts"], "{DECOY90_TS}": I["S_DECOY90"]["ts"],
       "{H1}": I["T_H1CARD"]["id"], "{H1C}": I["T_H1CREATE"]["id"], "{ENG}": I["T_ENGCARD"]["id"], "{ENGC}": I["T_ENGCREATE"]["id"],
       "{CMT}": I["T_H1CMT"]["id"], "{GAMEND}": "frederick.stone@harmonygames.co/" + I["G_AMEND"]["gmail_id"],
       "{SWEEP}": I["FOLDER_SWEEP"]["id"], "{OPS}": I["FOLDER_OPS"]["id"], "{DOC}": I["DOC_CASH"]["id"], "{MARCH}": I["SHEET_MARCH"]["id"],
       "{CONF}": I["CONF_PAGE"]["id"], "{ARTHUR_SUM_TS}": I["S_ARTHUR_SUM"]["ts"]}
for k, v in I.items():
    if k.startswith("SW_"): sub["{" + k + "}"] = v["id"]
t = open(os.path.join(W, "design_body.md")).read()
for k in ("{REDTEAM}", "{GATE}", "{REACH}", "{ENTITY}", "{CANSEE}"): t = t.replace(k, sub.pop(k))
for k in sorted(sub, key=len, reverse=True): t = t.replace(k, sub[k])
left = [x for x in __import__("re").findall(r"\{[A-Za-z_0-9]+\}", t)]
assert not left, left
# keep a pasted stage-gate block if one exists in the current file
if os.path.exists(OUT):
    old = open(OUT).read()
open(OUT, "w").write(t); print("wrote", OUT, len(t))
