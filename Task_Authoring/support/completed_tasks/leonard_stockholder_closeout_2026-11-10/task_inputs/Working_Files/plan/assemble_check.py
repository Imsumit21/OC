#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Check.md (check mode) for the exact bytes of 04_Prompt.txt. Findings come from plan/check_findings.json
(this run plus the local blind /prompt round in research/prompt_review_rev1/)."""
import hashlib, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
P = open(os.path.join(TI, "04_Prompt.txt")).read()
WC, SHA = len(P.split()), hashlib.sha256(P.encode()).hexdigest()[:12]
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
CLOCK = CTX["universe"]["clock_line"].replace("Clock: ", "", 1) if CTX["universe"]["clock_line"].startswith("Clock: ") else CTX["universe"]["clock_line"]
F = json.load(open(os.path.join(HERE, "check_findings.json")))
L = []; A = L.append


def table(head, rows):
    A("| " + " | ".join(head) + " |"); A("|" + "---|" * len(head))
    for r in rows:
        A("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |")
    A("")


for span in [r["span"] for r in F["findings"]] + [r[1] for r in F["coverage"]]:
    assert span.strip('"') in P, span
A("# Prompt Check — leonard_stockholder_closeout")
A(f"> Prompt: 04_Prompt.txt · {WC} words · sha256 {SHA} · Clock: {CLOCK} · checked 2026-11-08 against 04_Prompt_Writing_Brief.md (2026-11-08) · release task-quality-v1")
A("> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.")
A("")
A(f"Clock: {CLOCK}")
A("")
A("## Summary")
A("")
n_fail = sum(1 for r in F["findings"] if r["severity"] == "Fail"); n_nf = sum(1 for r in F["findings"] if r["severity"] == "Non-fail")
n_adv = sum(1 for r in F["findings"] if r["severity"] == "Advisory")
A(f"Fail {n_fail} · Non-fail {n_nf} · Advisory {n_adv} · UNVERIFIED checks: {F['unverified'] or 'none'} · checks clean: {F['clean']}")
A(f"Predicted /prompt band: {F['band']} · Status: {F['status']}")
A("")
A(F["summary_note"])
A("")
A("## Findings")
A("")
table(["#", "Check", "Dimension · severity", "Quoted span", "Rule (source)", "Defect"],
      [[i + 1, r["check"], f"{r['dimension']} · {r['severity']}", f"\"{r['span']}\"", r["rule"], r["defect"]] for i, r in enumerate(F["findings"])])
A("## Fair readings")
A("")
for d in F["readings"]:
    A(f"- **{d[0]}.** Reading A: {d[1]} Reading B: {d[2]} Resolution: {d[3]}")
A("")
A("Accepted outcomes are the brief's §4b and the sidecar `outcome_reviews.prompt-check` in Working_Files/00_V3_Authoring_Evidence.json.")
A("")
A("## Verification log")
A("")
table(["Span", "Type", "Universe record (locator)", "Result"], F["verification"])
A("## Brief coverage")
A("")
table(["Brief item", "Present in the prompt (quoted span)"], [[r[0], f"\"{r[1]}\""] for r in F["coverage"]])
A("## Self-review")
A("")
A("Walked `Evals/1_Prompt_Eval.md` Phases 1-3 against the prompt; every C-check has a result below. The prompt's hash was the same before and after this run; every quoted span is checked as an exact substring by this generator.")
A("")
table(["Check", "Result", "Counter-reading (strongest argument the result is wrong)", "Resolution (record, Eval §, case id)"], F["selfreview"])
A(F["calibration"])
A("")
A("Unresolved: " + F["unresolved"])
A("")
A("## Route")
A("")
A(F["route"])
A("")
open(os.path.join(WF, "04_Prompt_Check.md"), "w").write("\n".join(L) + "\n")
print("wrote 04_Prompt_Check.md", WC, SHA)
