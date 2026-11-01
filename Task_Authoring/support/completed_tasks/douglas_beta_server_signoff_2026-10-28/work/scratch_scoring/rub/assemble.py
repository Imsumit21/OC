import json,re
S='/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/rub/'
A,A2=open(S+'AA2.md').read().split('\n@@@\n')
meta=json.load(open(S+'meta.json'))
led=open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/08_OE_Writing_Ledger.md').read()
vis=led[led.index('Visibility proof'):led.index('## C · Write capability')].strip()
# OE trace
oe=open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/08_Oracle_Events.md').read()
heads=re.findall(r'^OE (\d+)  (.*)$',oe,re.M)
P={r['what']:r['P'] for r in meta['rows']}
def prov(n):
    n=int(n)
    m={1:'P21 (and the DM rows)',2:'P2–P14 (rules)',3:'P2, P16',4:'P1',5:'P6, P17, P27, P37, P47',6:'P1',7:'P10–P14',8:'P12, P14, P31, P42',9:'P2, P6–P9, P11, P16–P19',10:'P20',11:'P2, P7–P9, P19, P28–P30',12:'P2',13:'P2, P9, P15, P16',14:'P2',15:'P10–P14',16:'P3, P24, P34, P44',17:'P4, P25, P35, P45',18:'P23, P33 (volume)',19:'P13, P41, P52',20:'P12, P31',21:'P23, P33 (volume)',22:'P10',23:'P8, P29, P39, P49',24:'P5, P18, P26, P36, P46',25:'P7, P28, P38, P48',26:'P6, P17, P27, P37, P47',27:'P14, P42',28:'P23, P33 (volume)',29:'P12, P15, P31, P51',30:'P32',31:'P12, P14',32:'P2–P19, P22–P32',33:'P1–P19',34:'P20',35:'P33–P42',66:'P21–P32'}
    if n in m: return m[n]
    t=re.search(r'ZOM-\d+',dict(heads)[str(n)]).group(0)
    if n%2==0:
        hit=[r['P'] for r in meta['rows'] if r['what']==f'{t} moved to Todo']
        return (hit[0] if hit else 'P33 (volume)')
    hit=[r['P'] for r in meta['rows'] if r['what'].startswith(f'{t} comment')]
    return hit[0] if hit else 'P43 (volume)'
def kind(n):
    n=int(n); return 'write' if n in(33,34,66) or 36<=n<=65 else ('discovery (calculation)' if n in(14,32) else 'discovery')
B='\n'.join(f"| OE {n} | {kind(n)} | {prov(n)} | no — {'its result is graded on the artifact it writes' if kind(n)=='write' else 'a read; graded through the row(s) its result decides'} |" for n,h in heads)
D='''| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |
|---|---|---|---|---|---|
| G1 | Register on-prod column, F31, 17 tickets: `ZOM-459` `ZOM-509` `ZOM-336` `ZOM-392` `ZOM-503` `ZOM-518` `ZOM-499` `ZOM-531` `ZOM-537` `ZOM-444` `ZOM-487` `ZOM-550` `ZOM-435` `ZOM-557` `ZOM-510` `ZOM-256` `ZOM-436` | P10 ZOM-499 (rolled back then redeployed, Y), P11 ZOM-510 (import-only Y), P12 ZOM-503 (two changes, #52 in the freeze), P13 ZOM-392 (Approve after deploy), P14 ZOM-550 (freeze without Arthur). Exceptions graded directly, not sampled: P3–P9 (each singled out by an amendment record) | P2 | none — bundle (Rubric Writing §7; Eval 2.2) | no — the prompt asks for the register as a whole; per-ticket cells are repetitive members |
| G2 | Register server-change column, F31, same 17 tickets | P15 ZOM-503 (second PR #52), P16 ZOM-510 (import only), P17 ZOM-487, P18 ZOM-537, P19 ZOM-436 (the hidden imports, one per amendment kind: page reply, inline review comment, reply-all) | P2 | none — bundle (Rubric Writing §7; Eval 2.2) | no |
| G3 | Reply's not-on-prod list, F32, 15 keys: `ZOM-336` `ZOM-392` `ZOM-503` `ZOM-518` `ZOM-550` `ZOM-435` `ZOM-557` `ZOM-256` `ZOM-487` `ZOM-537` `ZOM-444` `ZOM-531` `ZOM-459` `ZOM-509` `ZOM-436` | P31 ZOM-503 (two changes), P32 ZOM-557 (rollback). Exceptions direct: P24–P30 | P23 (count 15); P22 (on-prod count 2) | none — bundle (Rubric Writing §7; Eval 2.2) | no — the told facts are the count and the list; list members are repetitive |
| G4 | Todo moves, F31, the same 15 tickets | P41 ZOM-392 (late Approve), P42 ZOM-550 (freeze). Exceptions direct: P34–P40 | P33 | none — bundle (Rubric Writing §7; Eval 2.2) | no — 15 separate writes of one rule |
| G5 | Todo comments, F31, the same 15 tickets | P51 ZOM-503 (#52), P52 ZOM-392 (#41 redeploy). Exceptions direct: P44–P50 | P43 | none — bundle (Rubric Writing §7; Eval 2.2) | no |'''
b=meta['bands']
E=f'''Rows {meta['N']} · Outcome {meta['N']} · Process candidates 0 — ≥ 1 Outcome ☑ (no Process ratio: QC Spec V2 and the Evals override fail only zero Outcome) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ (P2, P22, P23, P33, P43) · predicted all-fail rows = 0 ☑ (harness tolerance 0; /rubric fails at ≥ 2; no row rests on the four Evals bases — every value is persona-reachable, see Visibility proof)
Failure diversity: largest unit of discovery is the rules card (F2) at 100% of the weight, then the ticket comments (F13) and the candidate list (F12) (≤ 50% ☒ — every register, reply and Todo row runs through the rules card, which is the task itself; same design finding as the accepted Frederick account-handover task, Self-review §6) · chains landing on distinct rows ☑ (C9 page reply P6 P17 P27 P37 P47; C10 #46 inline P5 P18 P26 P36 P46; C11 reply-all P7 P8 P9 P19 P28 P29 P30 P38 P39 P40 P48 P49 P50; C12 #38 inline P3 P24 P34 P44; C13 #39 inline P4 P25 P35 P45; H2 doc + freeze P10–P14 P31 P32 P41 P42)
Bands: 5 ×{b['5']} · 3 ×{b['3']} · 1 ×{b['1']} (total weight {meta['W']})
Set size: {meta['N']} rows for 12.75 h (reference: 31 criteria for a ~10-hour task; four prompt-required deliverables — register, share, reply, Todo moves with comments — each graded once; no fact graded twice in one deliverable)
Coverage: requirements 7/7 · OEs 66/66 · writes 7/7 · told facts 2/2 (on-prod count, not-on-prod list) · friction 0/0
Four prohibitions: ☑ unstated expectations (no row for the Leonard email reply, the #zombie-match3d copy or "no new tickets") ☑ conclusions on ambiguous evidence (none — ledger §F risks 1–6 are representational) ☑ grading the distractor (traps graded by how they are handled: counts and N values) ☑ hard-coded titles/phrasings (sheet title and comment wording delegated)
Blocking: none — no UGT defect, no infeasible write, no unverified visibility (diversity.authority_share is a reported design finding, not a blocker the plan can fix honestly)

Baseline replay (the six round-3 runs, graded row by row from their write payloads; scratch grade2.py): run scores 0.344 · 0.623 · 0.245 · 0.344 · 0.637 · 0.245 → average 40.6%, SD 0.163, pass@1 0/6, 3 failure patterns (largest 33%) — every difficulty gate PASS. Rows that failed all six runs (valid, data reachable, for /create-allfail): P3 P4 P5 P18 P22 P23 P24 P25 P26 P33 P34 P35 P36 P43 P44 P45 P46 — all trace to the three inline review comments (#38, #39, #46) that no run incorporated, and the volume rows that need them.'''
doc=f'''# 09 Rubric Writing Plan — Douglas beta server register (dg-beta-server-signoff)
Generated 2026-10-27 · Clock 2025-10-01T00:00:00Z (assigned universe date; V3 replaces 2026-02-14) · Persona Douglas douglas@harmonygames.co · Tier Long-Horizon · Human time 12.75 h · OE status: /oe PASS 2026-10-27 (report 6ad90ea979eb9e5d89f8879f_2_oe (1).md, score 5, reviewed OE sha256 09fc22673a84)
Canonical outcome: brief §4b (one acceptance class per deliverable) — W1 register in d_69fcebc484d472907b0b5c (title any), 17 rows, server change(s) in any recognisable words, on prod Y/N; W3 Leonard commenter on the file; W4 DM D05QQF7V404 (thread or top level) with 2 on prod and the 15 keys; W5 the 15 tickets in Todo, each with a comment naming the change still to go out.

## A · Coverage matrix
| P | Source (prompt span · OE n) | What must be verified (noun phrase) | Final state that proves it (artifact / message / record / final response) | Category (Outcome / Process candidate → C) | Values the criterion must name (F-IDs + backticked literals; exact / tolerance) |
|---|---|---|---|---|---|
{A}

## A2 · Grading risks and weight
| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Duplicate risk (per deliverable) / overlap group | Predicted all-fail basis (four Evals bases) · over-specific risk |
|---|---|---|---|---|---|---|---|---|---|
{A2}

## B · OE trace
| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |
|---|---|---|---|
{B}

## C · Process candidates — three-condition test
| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |
|---|---|---|---|---|---|---|
| — | "once the register is in the folder" (share after the register exists) | P20 grades the permission on the register file itself, which can only exist after the file | n/a | fails — P20 captures it | n/a | no Process row; covered by P20 (F9, F31) |
| — | "no need to wait on me" | The moves and comments exist (P33–P52) | n/a | fails — P33, P43 capture it | n/a | no Process row; covered by P33, P43 (F2, F15) |
| — | "reply here when it's done" (reply after the register) | The reply's content can only be right after the full audit; ordering adds no graded value | n/a | fails — P22, P23 capture the content | n/a | no Process row (F1, F32) |

## D · Spot-check groups
{D}

## E · Summary
{E}

{vis}

## F · Shortcut probe
'''
open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/09_Rubric_Writing_Plan.md','w').write(doc)
print(len(doc))
