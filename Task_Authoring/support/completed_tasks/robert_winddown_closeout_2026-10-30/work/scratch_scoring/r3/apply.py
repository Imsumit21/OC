import json,sys,re,copy
src,dst=sys.argv[1],sys.argv[2]
R=json.load(open(src)); assert len(R)==115
row=lambda i: R[i-1]
CONV="conventions doc 'Close-out register conventions' (f_1326e66bcabfda8fd29e4a, SQL L8)"
PROJ="Linear project 'Shutdown - accounts' 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a (SQL L147)"
SVB_L50="Arthur's SVB card comment 698fafc529f7ffa32ff7dd20 (SQL L50)"
def T(i,t,w=None):
    row(i)['title']=t
    if w: row(i)['weight']=w
def W(i,w): row(i)['weight']=w
def mk(t,w,j,e,cat="Outcome"): return {"title":t,"category":cat,"weight":w,"justification":j,"evidence":e}

T(1,"The Agent creates the account close-out register as one new spreadsheet file (any title and any Drive folder; a Google Sheet or an uploaded spreadsheet file both pass)")
row(1)['justification']="Leonard's ask: 'I need one sheet'. The register is one new spreadsheet; its title and Drive folder are not set by the prompt or the ask, so any title and folder pass (the Wind Down folder is one valid place)."
r=row(2); r['justification']=r['justification'].replace("rule 3 adds ElevenLabs from the multi-vendor costs-tab line 'Sound (Pond5, Soundly,Elevenlabs)' (Pond5 ended Sep 8 2025, rule 2) and keeps AWS, the UA ad accounts and the two $30 game-ops lines off.","rule 3 adds ElevenLabs from the multi-vendor costs-tab line 'Sound (Pond5, Soundly,Elevenlabs)' (Pond5 ended Sep 8 2025, rule 2) and keeps AWS and the UA ad accounts off; Arthur's project description leaves out the two $30 game-ops lines ('the two $30 game-ops lines I'm handling myself, so they're not in here').")
assert "Arthur's project description leaves out" in r['justification']
r['evidence']=r['evidence'].replace(PROJ, PROJ+", description 'the two $30 game-ops lines I'm handling myself'",1)
T(3,"The Agent puts QuickBooks (ENG-2449) and Intuit (ENG-2450) on one single row of the account close-out register, with QuickBooks, Intuit or both in that row's account name")
HOLD="The Agent records Hold for Sunset (Hold, Hold for Sunset or Hold until the Sunset review call all pass; a Keep label fails) as the action for {} in the account close-out register"
for i,n in [(7,"Linear (ENG-2441)"),(8,"Figma (ENG-2442)"),(12,"dbt (ENG-2447)"),(16,"Google Workspace (ENG-2452)"),(17,"Slack (ENG-2453)"),(25,"GitHub (ENG-2462)")]: T(i,HOLD.format(n))
T(9,HOLD.format("Trello (ENG-2443)"),3); T(13,HOLD.format("BigQuery (ENG-2448)"),3)
T(11,"The Agent records Move to Arthur's LLC (Move, Moved, or any wording that moves it to Arthur's card, his LLC or the KubLLC card passes; a Keep or Hold label fails) as the action for Metabase (ENG-2446) in the account close-out register")
T(14,"The Agent records Keep (Keep or Kept pass; a Hold label fails) as the action for the QuickBooks / Intuit row (ENG-2449) in the account close-out register")
W(18,3)
T(19,"The Agent records Keep (Keep or Kept pass; a Hold label fails) as the action for Deel (ENG-2456) in the account close-out register",3)
W(28,3)
CL="The Agent records the status Closed (Closed, or wording that says the vendor confirmed the cancellation; a bare Cancelled fails) for {} in the account close-out register"
for i,n in [(29,"Unity (ENG-2438)"),(30,"Helpshift (ENG-2439)"),(37,"CodeRabbit (ENG-2459)"),(38,"Cursor (ENG-2460)"),(39,"Zapier (ENG-2461)"),(40,"Kapwing (ENG-2463)")]: T(i,CL.format(n))
T(31,CL.format("Soundly (ENG-2440)"),5)
RQ="The Agent records the status Requested (Requested, or wording that says the cancellation was sent and the vendor has not confirmed it; a bare Cancelled or Closed fails) for {} in the account close-out register"
T(32,RQ.format("Singular (ENG-2444)")); T(36,RQ.format("Layer (ENG-2458)"))
r=row(36); r['justification']=r['justification'].replace("(Leonard's own #prototype note is not a vendor notice)","(Leonard's own #winddown note 'I just canceled layer' is not a vendor notice)")
assert "#winddown note" in r['justification']; r['evidence']+="; #winddown C0ADGSZKR3R/1770837793.168589 'I just canceled layer'"
for i in (43,44,46,47):
    r=row(i); assert "(SQL L44, L48)" in r['evidence'],i; r['evidence']=r['evidence'].replace("(SQL L44, L48)","(SQL L44, L48, L50)")
T(46,"The Agent records Feb 17, 2026 (any date format) as the by-when date for the QuickBooks / Intuit row (ENG-2449) in the account close-out register")
T(51,"The Agent records Mar 12, 2026 (any date format; naming the Sunset delivery review call also passes) as the by-when date for Figma (ENG-2442) in the account close-out register")
r=row(52); r['title']="The Agent records no date (a dash, a blank, N/A or none) as the by-when for Cursor (ENG-2460) in the account close-out register"
r['justification']="Rule 6: 'Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends'. Cursor is a Closed Cancel row (Arthur's #prototype reply: 'cursor sent the confirmation on the team plan cancellation this morning') and nothing has to be exported or switched over, so its by-when is a dash; 'seats keep working until mar 5' is when access ends, not a by-when."
r['evidence']="#prototype C09UHHN6PFZ/1770991653.518204 (Arthur's reply to Oliver); ENG-2460; "+CONV
r=row(54); r['weight']=1; r['evidence']=CONV+" rule 7 'Anything you add is yours'; HG Costs line 'Sound (Pond5, Soundly,Elevenlabs)' (P&L 'Harmony Games P&L and forecast - Jan 2026')"
W(62,1)
r=row(63); r['title']="The Agent names Unity's account manager's confirmation, or Arthur's #executives note relaying it, as where Unity's cancellation was confirmed, in the Unity (ENG-2438) row of the account close-out register"
r['justification']="Rule 5: 'Closed = the vendor itself has confirmed (their email, an in-app or bot notice, a final invoice) - say where.' Unity's confirmation came from its account manager, relayed in Arthur's #executives note; naming either says where."
r=row(64); r['title']="The Agent names Cursor's own confirmation of the team plan cancellation, or Arthur's #prototype reply relaying it, as where Cursor's cancellation was confirmed, in the Cursor (ENG-2460) row of the account close-out register"
r['justification']="Rule 5: 'Closed = the vendor itself has confirmed … - say where.' Cursor sent the confirmation on the team plan cancellation, relayed in Arthur's #prototype reply ('cursor sent the confirmation on the team plan cancellation this morning'); naming either says where."
r=row(65); r['title']="The Agent names CodeRabbit's GitHub bot notice (on pull request 38 in harmonygames-Games/Combo-Fighters; naming the pull request is optional) as where CodeRabbit's cancellation was confirmed, in the CodeRabbit (ENG-2459) row of the account close-out register"
r['justification']="Rule 5: 'Closed = the vendor itself has confirmed (their email, an in-app or bot notice, a final invoice) - say where.' CodeRabbit's bot posted on pull request 38: 'The CodeRabbit subscription for harmonygames-Games was canceled on Feb 12, 2026, so this pull request was not reviewed.'"
r=row(73); r['weight']=5; r['evidence']+="; ENG-2440 (SQL linear_issues); "+CONV
for i in (78,79,80,81):
    r=row(i); j=r['justification']
    if "Team ENG has no Duplicate state." in j:
        r['justification']=j.replace("Team ENG has no Duplicate state.","The settle rule names Canceled for issues that don't belong, so Canceled is the state graded (team ENG's status list also has a Duplicate state, which the project does not use).")
    elif "Team ENG has no Duplicate state" in j: raise SystemExit(i)
    r['evidence']+="; team ENG status list (linear_list_issue_statuses: Canceled state_7e56143481a65571)"
for i in (78,79,80,81): assert "no Duplicate" not in row(i)['justification'],i
r=row(82); r['title']="The Agent moves exactly 11 of the 28 issues in the Linear project 'Shutdown - accounts' to Done or Canceled"; r['weight']=5
r['justification']="The project's settle rule: 'Done once the account counts as closed in the register …, Canceled if it doesn't belong on the list, everything else stays open'. 7 issues are Closed Cancel rows (ENG-2438, 2439, 2440, 2459, 2460, 2461, 2463) and 4 don't belong (ENG-2450 duplicate, ENG-2454, 2465, 2466 cancelled before Feb 9), so exactly 11 move to Done or Canceled and the other 17 stay in any open state."

# comment splits
def cm(i,n,eng): return f"Linear issue {eng} ({n})"
NODATE="The Agent states in its new comment on Linear issue {} ({}) that nothing is due by a date (any wording that no date is due passes: a dash, none, N/A or nothing left to do)"
CLOSEDACT="The Agent adds a new comment on Linear issue {} ({}) saying {} is cancelled (cancelled, closed, done or confirmed by the vendor all pass; wording that the cancellation is still pending or only requested fails)"
DECOY={"Helpshift":" Helpshift's 'discontinuing us at the end of february' (ENG-2439) is when access ends, not a by-when.","Cursor":" 'seats keep working until mar 5' is when access ends, not a by-when.","Zapier":" 'the plan runs until feb 27' (ENG-2461) is when access ends, not a by-when."}
split={}
closed={83:("ENG-2438","Unity",5,5),84:("ENG-2439","Helpshift",3,5),85:("ENG-2440","Soundly",5,5),103:("ENG-2459","CodeRabbit",5,5),104:("ENG-2460","Cursor",5,5),105:("ENG-2461","Zapier",3,3),107:("ENG-2463","Kapwing",3,3)}
for i,(e,n,wa,wd) in closed.items():
    o=row(i); ev=o['evidence']
    a=mk(CLOSEDACT.format(e,n,n),wa,f"The project asks each comment to say 'what happens and by when'. {n} is a Cancel row whose status is Closed (rule 5: the vendor itself has confirmed), so the comment says it is cancelled; a comment calling the cancellation pending or only requested contradicts the register.",ev)
    d=mk(NODATE.format(e,n),wd,f"The project asks each comment to say 'what happens and by when'. Rule 6: 'Moved and Closed rows get a dash', and {n} is Closed with nothing left to export or switch over, so nothing is due by a date.{DECOY.get(n,'')}",ev)
    split[i]=[a,d]
dated={86:("ENG-2441","Linear","is held for Sunset",3,"Mar 12"),87:("ENG-2442","Figma","is held for Sunset",3,"Mar 12"),88:("ENG-2443","Trello","is held for Sunset",3,"Mar 12"),
 89:("ENG-2444","Singular","is being cancelled",3,"Feb 17"),91:("ENG-2447","dbt","is held for Sunset",5,"Mar 12"),92:("ENG-2448","BigQuery","is held for Sunset",3,"Mar 12"),
 93:("ENG-2449","QuickBooks","is kept",3,"Feb 17"),95:("ENG-2451","Carta","is being cancelled",3,"Aug 14"),96:("ENG-2452","Google Workspace","is held for Sunset",3,"Feb 17"),
 97:("ENG-2453","Slack","is held for Sunset",3,"Feb 17"),99:("ENG-2455","Gusto","is being cancelled",3,"Feb 17"),101:("ENG-2457","Docusign","is being cancelled",3,"Feb 17"),
 102:("ENG-2458","Layer","is being cancelled",3,"Feb 17"),106:("ENG-2462","GitHub","is held for Sunset",5,"Mar 12"),108:("ENG-2464","1Password","is being cancelled",3,"Feb 17")}
DT={"Mar 12":"Mar 12, 2026 (any date format; naming the Sunset delivery review call also passes)","Feb 17":"Feb 17, 2026 (any date format)","Aug 14":"Aug 14, 2026 (any date format)"}
for i,(e,n,say,wa,dk) in dated.items():
    o=row(i); j=o['justification']; ev=o['evidence']
    a=mk(f"The Agent adds a new comment on Linear issue {e} ({n}) saying {n} {say}",wa,j,ev)
    d=mk(f"The Agent gives {DT[dk]} as the by-when date in its new comment on Linear issue {e} ({n})",5,j,ev)
    split[i]=[a,d]
# R90 own rewrite
o=row(90); ev=o['evidence']
split[90]=[mk("The Agent adds a new comment on Linear issue ENG-2446 (Metabase) saying Metabase moves to Arthur's card (Arthur's card, his LLC or the KubLLC card, moved, switched or 'keeping it on Arthur's card' all pass; a comment giving Hold for Sunset, or Keep without Arthur's card, as the action fails)",5,
  "The project asks each comment to say 'what happens and by when'. Rule 4: Metabase is Move to Arthur's LLC (his card); ENG-2446: 'metabase billing switched to the kubllc card'. A #winddown decoy reads 'I think we keep Metabase and dbt', and Sunset's list does not hold Metabase, so Hold or a plain Keep is wrong.",ev),
 mk("The Agent states in its new comment on Linear issue ENG-2446 (Metabase) that nothing is due by a date (a dash, none or N/A passes; the past-tense note 'billing already switched' alone, with no by-when statement, does not count, and a comment giving Feb 17 or Mar 12 fails)",5,
  "The project asks each comment to say 'what happens and by when'. Rule 6: 'Moved and Closed rows get a dash'; Metabase's billing has already switched to Arthur's KubLLC card (ENG-2446), so no SVB card date (Feb 17) or review-call date (Mar 12) applies.",ev)]
o=row(100); o['weight']=3; o['evidence']=o['evidence']+"; Leonard's keep list in #winddown ('During shutdown, let's keep Deel, gusto, Intuit')"
split[100]=[o, mk("The Agent states in its new comment on Linear issue ENG-2456 (Deel) that nothing is due by a date (any wording that no date is due passes: a dash, none, N/A or nothing to do)",3,
  "The project asks each comment to say 'what happens and by when'. Rule 6: 'Keep rows that aren't on the SVB card get a dash'; ENG-2456: 'deel gets paid by transfer from the bank account, nothing on a card', so the Feb 17 SVB date does not apply.",o['evidence'])]
# reply rows
THR="in its reply in the thread of Leonard's Feb 13 ask in #winddown"
T(112,f"The Agent states {THR} that the monthly total over every register row is 6,706.49 (to the cent, ± 0.01)")
T(113,f"The Agent states {THR} that the monthly total over the Keep and Hold for Sunset rows is 1,249.04 (to the cent, ± 0.01)")
T(114,f"The Agent names {THR}, as a clash, the #winddown decision to take Slack to the free plan or down to a few members with the rest as guests, against Sunset's request to keep Slack on the paid plan with its users in place (naming the plan or the users passes)")
T(115,f"The Agent names {THR}, as a clash, the plan to archive Google accounts on or after Feb 15, against Sunset's request to keep every Google Workspace user account, unarchived and undeleted (naming the review call or delivery as the end point is optional)")
for i in (112,113,114,115): row(i)['evidence']+="; thread C0ADGSZKR3R/1771003267.448213 (Leonard's Feb 13 ask)"
metab=mk("The Agent records no status (a blank, a dash, N/A or none; Moved or Closed fails) in the where-it-stands cell for Metabase (ENG-2446) in the account close-out register",3,
  "Rule 5: 'Where it stands, for Cancel rows only … Leave it blank on the other rows.' Metabase is Move to Arthur's LLC (ENG-2446 'metabase billing switched to the kubllc card'), not a Cancel row, so its status cell stays empty; Moved or Closed there gives a non-Cancel row a status.",
  "ENG-2446 comment cmt_a83cc20eced4c1064f0a 'metabase billing switched to the kubllc card' (SQL linear_comments); "+CONV)
guard=mk("The Agent names exactly two clashes in its reply in the thread of Leonard's Feb 13 ask in #winddown (the Slack free plan and the cut to a few members with guests count as one clash, and so do repeated mentions of the Google archiving plan)",5,
  "Rule 10: 'A clash is a decision one of us already posted in #winddown that Sunset's list or SVB's card terms would undo. Moving who pays for an account isn't one (it closes nothing), and requests or suggestions aren't decisions.' Only the Slack decision and the Google archiving plan qualify; #winddown also holds decoys: Arthur's 'I'll be moving github, [USERNAME_30019], and Metabase to my KubLLC card.' (a payer move) and 'I think we keep Metabase and dbt' (a suggestion).",
  "#winddown C0ADGSZKR3R/1770937232.664809, C0ADGSZKR3R/1770933903.645709; thread C0ADGSZKR3R/1771003267.448213; "+CONV+" rule 10")
proc=mk("The Agent posts its reply to Leonard after its last Linear issue update (state change or comment)",1,
  "The prompt: 'settle each of the linear issues like he asked, and then reply to him in his thread'. The final state shows the reply and the Linear updates but not their order, so the order is graded as Process from the trajectory timestamps.",
  "Prompt (04_Prompt.txt); thread C0ADGSZKR3R/1771003267.448213; "+PROJ,"Process")
DEL={45,48,49,50,70,111}
out=[]
for i,r in enumerate(R,1):
    if i in DEL: continue
    out.extend(split.get(i,[r]))
    if i==42: out.append(metab)
out.extend([guard,proc])
json.dump(out,open(dst,'w'),indent=1,ensure_ascii=False)
import collections
print(len(out), sum(x['weight'] for x in out), collections.Counter(x['weight'] for x in out), collections.Counter(x['category'] for x in out))
