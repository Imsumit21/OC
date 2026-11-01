import json
C=json.load(open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/09_Rubrics.json'))
REGEV={1:513,2:347,3:563,4:484,5:595,6:467}; DMEV={1:561,2:406,3:608,4:529,5:652,6:505}
MV={1:(524,540,9),2:(355,399,12),3:(575,589,8),4:(492,508,9),5:(603,625,12),6:(470,484,8)}
CM={1:(542,558,9),2:(357,401,12),3:(591,605,8),4:(510,526,9),5:(627,649,12),6:(486,500,8)}
ONP={1:'9 on prod of 18',2:'5 of 17 on prod',3:'10 on prod of 18',4:'9 on prod of 18',5:'5 of 17 on prod',6:'10 on prod (18 in scope)'}
NOTL={1:9,2:12,3:8,4:9,5:12,6:8}
PR={'ZOM-459':('38',"harmonygames-Games/match3d-backend#38#rc_1 (SQL L211): the reviewer's inline comment on #38 says 459 also needs the plague race table import and that the import is part of 459's server change; the deploy log has that import on dev only (2025-08-26 10:30, SQL L23)",'plague race table import'),
'ZOM-509':('39',"harmonygames-Games/match3d-backend#39#rc_1 (SQL L243): Douglas's inline comment on #39 says 509 needs the trophy path copy table imported and that the import is part of 509's server change; the deploy log has it on dev only (2025-09-02 18:05, SQL L23)",'trophy path copy table import'),
'ZOM-537':('46',"harmonygames-Games/match3d-backend#46#rc_1 (SQL L463): Arthur's inline comment on #46 says 537 also needs the economy table import and that it is part of 537's server change; the deploy log has it on dev only (2025-09-16 14:20, SQL L23)",'economy table import')}
PREV={1:{'38':'reviews@138','39':'reviews@153','46':'reviews@284'},2:{'38':'reviews@247','39':'reviews@251','46':'reviews@283'},3:{'38':'reviews@147','39':'reviews@183','46':'reviews@357'},4:{'38':'reviews@423','39':'reviews@425','46':'reviews@441'},5:{'38':'reviews@119','39':'reviews@121','46':'reviews@137'},6:{'38':'reviews@127','39':'reviews@129','46':'reviews@144'}}
TESTS="Tests: authority — the prompt incorporates Arthur's ask ('the way he laid it out'; D05QQF7V404/1759266764.508127), which points to the rules card 68dabfe9bc2e8b969782e22d (rules 1–5) · grounding — {g} · reachability — GitHub is unscoped and the inline comments are returned by github_get_pull_request_comments (run-3 called it on #38 at event 150 and on #39 at event 189 and got the comments back); the deploy log f_78bedc46245090a160d2dd is Douglas's own file (check-sql YES) · capability — {cap} · atomicity/destination — one condition on the artifact the prompt asks for ({dest}) · precision/flexibility — {prec} · phrasing — affirmative, starts 'The Agent', no tool name, title names the value · friction — none configured (03_Error_Async_Config.txt), no forced error in any run"
def runs_line(fn): return "Per-run evidence: "+"; ".join(fn(k) for k in range(1,7))
blocks=[]; ids=[]
def block(n,ev,g,cap,dest,prec,root,just):
    c=C[n-1]; ids.append(f'R{n}')
    blocks.append(f"""### R{n} — VALID   (weight {c['weight']})
Criterion: "{c['title']}"
{ev}
{TESTS.format(g=g,cap=cap,dest=dest,prec=prec)}
Causation: no test fails; the runs missed the requirement.
Shared root cause: {root}
Justification (VALID only): {just}
""")
for n,t in [(3,'ZOM-459'),(4,'ZOM-509'),(5,'ZOM-537')]:
    pn,src,imp=PR[t]
    def ev(k,t=t,pn=pn):
        extra=f", and it opened #{pn}'s inline review comments at event {150 if pn=='38' else 189} yet kept Y" if k==3 and pn in('38','39') else f"; it read #{pn}'s reviews ({PREV[k][pn].replace('@',' at event ')}) but never its inline review comments"
        return f"run-{k}: register written with {t} = Y (event {REGEV[k]}){extra}"
    block(n,runs_line(ev),f"{src}; {t} is Done in the window and its ticket note names #{pn}",'read-only fact plus a supported Sheets/Drive write (every run wrote the register)','the register on-prod cell',f"exact discrete value N; Y/N or words accepted by the title",'R3–R5, R18, R24–R26, R34–R36, R44–R46 (one missed surface: the inline review comments on #38, #39, #46)',
     f"Card rule 4 makes {t} on prod only if all its server changes are, and {src.split(': ',1)[1].split(';')[0]} while the deploy log shows that import on dev only, so {t} is N. Every run marked {t} as Y from #{pn}'s prod: comment without reading or applying that inline review comment.")
# R18
def ev18(k): return f"run-{k}: ZOM-537's server-change cell lists only match3d-backend#46 (register event {REGEV[k]}); #46's inline review comments were never read ({PREV[k]['46'].replace('@',' at event ')} reads reviews only)"
block(18,runs_line(ev18),PR['ZOM-537'][1],'supported register write','the register server-change cell of ZOM-537','the import in any recognisable words','R5 (same missed comment)',
 "Arthur's inline review comment on match3d-backend#46 (#46#rc_1) says the economy table import is part of ZOM-537's server change, which card rule 2's server change(s) column must carry. Every run listed only #46 for ZOM-537 because none opened #46's inline review comments.")
# R22, R23
def ev22(k): return f"run-{k}: DM reply says {ONP[k]} (event {DMEV[k]})"
block(22,runs_line(ev22),"of the 17 register tickets only ZOM-499 (#44 redeployed 2025-09-22 17:30 UTC before the freeze) and ZOM-510 (Zombie Lane rewards import to prod) are on prod (SQL L381–L391, L23)",'supported Slack write (every run posted the reply)','the DM reply Arthur asked for','exact count; number or word','R3–R5 (ZOM-459/509/537 counted as on prod), plus ZOM-547/553 kept in runs 1, 3, 4, 6',
 "Arthur asked 'how many tickets are on prod'; the answer is 2 (ZOM-499 and ZOM-510) once the inline-comment imports for ZOM-459, ZOM-509 and ZOM-537 and Arthur's reply-all exclusions are applied. Every run gave 5, 9 or 10 because it counted ZOM-459, ZOM-509 and ZOM-537 as on prod.")
def ev23(k): return f"run-{k}: DM reply lists {NOTL[k]} tickets as not on prod (event {DMEV[k]})"
block(23,runs_line(ev23),"15 register tickets are not on prod (ledger F32; SQL PR rows L164–L713, log L23, amendments L36, L96, L211, L243, L463)",'supported Slack write','the DM reply','exact count of ZOM keys','R3–R5',
 "Arthur asked 'which ones aren't' on prod, and 15 of the 17 register tickets are not on prod. Every run listed 8, 9 or 12 because ZOM-459, ZOM-509 and ZOM-537 were treated as on prod (and runs 1, 3, 4, 6 also missed the reply-all tickets).")
for n,t in [(24,'ZOM-459'),(25,'ZOM-509'),(26,'ZOM-537')]:
    pn,src,imp=PR[t]
    def ev(k,t=t): return f"run-{k}: DM reply lists {t} under on prod, not among the tickets not on prod (event {DMEV[k]})"
    block(n,runs_line(ev),src,'supported Slack write','the DM reply','the ticket named by key or title','R3–R5',
     f"Arthur asked which tickets aren't on prod; {t} is not on prod because its {imp} (named in the #{pn} inline review comment) is only on dev. Every run's DM reply named {t} as on prod.")
def ev33(k): return f"run-{k}: moved {MV[k][2]} tickets to Todo (events {MV[k][0]}–{MV[k][1]})"
block(33,runs_line(ev33),"15 tickets are not on prod and card rule 5 sends each back to Todo (SQL L58); Todo is a ZOM state (linear data.json)",'supported Linear write (linear_update_issue used by every run)','the Linear ticket state','exact count','R3–R5',
 "Card rule 5 sends every not-on-prod ticket back to Todo, and 15 of the 17 are not on prod. Every run moved 8, 9 or 12 tickets because it kept ZOM-459, ZOM-509 and ZOM-537 as on prod.")
for n,t in [(34,'ZOM-459'),(35,'ZOM-509'),(36,'ZOM-537')]:
    pn,src,imp=PR[t]
    def ev(k,t=t): return f"run-{k}: {t} not among the tickets moved (moves at events {MV[k][0]}–{MV[k][1]})"
    block(n,runs_line(ev),src,'supported Linear write','the Linear ticket state','exact state Todo (card rule 5)','R3–R5',
     f"Card rule 5 sends every not-on-prod ticket back to Todo, and {t} is not on prod because its {imp} is only on dev (#{pn} inline review comment). No run moved {t}, since every run had marked it as on prod.")
def ev43(k): return f"run-{k}: commented on {CM[k][2]} tickets (events {CM[k][0]}–{CM[k][1]})"
block(43,runs_line(ev43),"15 tickets are not on prod; card rule 5 asks for a comment on each (SQL L58)",'supported Linear write (linear_create_comment used by every run)','the Linear comments','exact count','R3–R5',
 "Card rule 5 asks for a comment on each not-on-prod ticket, and 15 tickets are not on prod. Every run commented on 8, 9 or 12 tickets because ZOM-459, ZOM-509 and ZOM-537 were treated as on prod.")
for n,t in [(44,'ZOM-459'),(45,'ZOM-509'),(46,'ZOM-537')]:
    pn,src,imp=PR[t]
    def ev(k,t=t): return f"run-{k}: no comment on {t} (comments at events {CM[k][0]}–{CM[k][1]})"
    block(n,runs_line(ev),src,'supported Linear write','the Linear comment on the ticket','the import named in any wording','R3–R5',
     f"Card rule 5 asks for a comment naming the change still to go out, which for {t} is the {imp} (#{pn} inline review comment; dev only in the deploy log). No run commented on {t}, since every run had marked it as on prod.")
doc=f"""# 11 All-Fail Justification — Douglas beta server register (dg-beta-server-signoff)
Completed rollouts: 6/6 (excluded: none)   Rubric binding: ok (76 rows bound by title to 09_Rubrics.json; every run ends with a success result event)
All-fail rubrics: {', '.join(ids)}

Source: 10_Baseline_Verifier_Results.md (Run #1–#6), 07_Baseline_Trajectories (run-1 = trajectory-run-1 (7).json, run-2 … run-6 = trajectory-run-2 … -6.json), 09_Rubrics.json (reviewed by /rubric, PASS 5, sha256 880f59b9298d). Calculator: difficulty_stats.py on Working_Files/12_difficulty_input.json — avg 56.3%, SD 0.117, pass@1 0/6, 4 failure patterns, blocking gates none.

All 17 share one root cause: no run incorporated the inline review comments on match3d-backend #38, #39 and #46, which make the plague race, trophy path copy and economy table imports part of ZOM-459's, ZOM-509's and ZOM-537's server changes (all three imports on dev only). Runs 1, 2, 4, 5 and 6 never called the inline-review-comment tool on those PRs; run 3 opened #38 and #39's inline comments and still marked both tickets Y. The rows are tested one by one below.

""" + "\n".join(blocks) + f"""
Summary: valid {len(ids)} · invalid 0 (rubric 0, environment 0; ≥ 2 = QC Fail, 1 = Non-fail) · judge errors 0 · unresolved 0 · non-causal defects to fix none
Hand-off to /create-difficulty: --invalid none --judge-correction none
"""
open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/11_AF_Justification.md','w').write(doc)
print(len(ids), len(doc))
