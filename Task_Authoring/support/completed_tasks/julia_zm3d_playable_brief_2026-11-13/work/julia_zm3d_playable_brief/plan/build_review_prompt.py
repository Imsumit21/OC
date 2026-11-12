#!/usr/bin/env python3
"""Write Working_Files/hardness_reviews/prompt.json (design_readiness schema 1, stage prompt): the injection-stage review
re-bound to the prompt, plus the semantic leak review of 04_Prompt.txt. Run after the prompt is final and after
tools/hardness_v2_check.py wrote plan/out/hardness_v2_prompt.txt. Judgements are the authoring session's."""
import hashlib, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TASK.parent / "tools"))
from design_readiness import input_hashes
man = json.loads((WF / "01_Hardness_Manifest.json").read_text())
surf = json.loads((WF / "01_Gradable_Surface.json").read_text())
prompt = (TASK / "04_Prompt.txt").read_text()
rev = json.loads((WF / "hardness_reviews" / "injection.json").read_text())
def ref(p):
    p = Path(p); return {"path": p.relative_to(TASK).as_posix(), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
spans = sorted({s["incorporating_span"] for s in surf["slots"]})
missing = [s for s in spans if s not in prompt]
assert not missing, ("incorporating spans not in the prompt", missing)
rev.update({
    "stage": "prompt",
    "reviewer": "claude-fable-5-2 (authoring session, /create-prompt-writing check; two cold reviewers read the prompt with the injected records)",
    "input_hashes": input_hashes("prompt", man, surf, sql_text=(TASK / "01_Universe_Inject.sql").read_text(), prompt=prompt),
    "semantic_prompt_review": {
        "leaks_solution": False,
        "reason": ("The prompt names Frederick's message as the job and two destinations Julia knows (her Drive, the PlayableX channel). It states no state word, count, "
                   "item, person other than Frederick, format word or reason a line is owed; it names none of the six deciding records, the notes, the pack list or a "
                   "ticket; it gives no reason to distrust the tickets and no order of steps. Every incorporating span of the surface is in it: " + "; ".join(spans) + ". "
                   "hardness_v2_check reports RULE_IN_PROMPT clean."),
        "evidence": [ref(TASK / "04_Prompt.txt"), ref(HERE / "out" / "hardness_v2_prompt.txt"), ref(WF / "04_Prompt_Writing_Brief.md")],
    },
})
(WF / "hardness_reviews" / "prompt.json").write_text(json.dumps(rev, indent=1, ensure_ascii=False) + "\n")
print("wrote hardness_reviews/prompt.json")
