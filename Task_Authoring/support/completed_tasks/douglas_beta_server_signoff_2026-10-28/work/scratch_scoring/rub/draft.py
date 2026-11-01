import json
REG="the server sign-off register"
FOLD="Arthur's Drive folder 'ZM Beta sign-off' (d_69fcebc484d472907b0b5c)"
H={ # t: (title phrase of the import, amendment text, evidence, log time)
'ZOM-459':('plague race table import',"the contractor's inline review comment on match3d-backend#38 says 459 also needs the plague race table import and that it is part of 459's server change","harmonygames-Games/match3d-backend#38#rc_1 (SQL L211); deploy log Console & imports 2025-08-26 10:30 plague race table dev (SQL L23); #38 prod: 2025-08-25 11:52 UTC (L205)"),
'ZOM-509':('trophy path copy table import',"Douglas's inline review comment on match3d-backend#39 says 509 needs the trophy path copy table imported and that the import is part of 509's server change","harmonygames-Games/match3d-backend#39#rc_1 (SQL L243); deploy log 2025-09-02 18:05 trophy path copy table dev (SQL L23)"),
'ZOM-537':('economy table import',"Arthur's inline review comment on match3d-backend#46 says 537 also needs the economy table import and that it is part of 537's server change","harmonygames-Games/match3d-backend#46#rc_1 (SQL L463); deploy log 2025-09-16 14:20 economy table dev (SQL L23)"),
'ZOM-487':('boss arena HP table import',"Arthur's reply on the ZM beta Confluence page says the boss arena HP table import is part of ZOM-487's server change","comment_zm_beta_oct10_c2 on page_zm_beta_oct10 (SQL L36); deploy log 2025-09-17 15:50 boss arena HP table dev (SQL L23)"),
'ZOM-444':('analytics events table import',"Arthur's reply-all in Leonard's go/no-go thread says the analytics events table import is part of ZOM-444's server change and is still only on dev","douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> (SQL L96); deploy log 2025-09-12 19:20 analytics events table dev (SQL L23)"),
'ZOM-531':('loadout table import',"Arthur's reply-all in Leonard's go/no-go thread says the loadout table import is part of ZOM-531's server change and is still only on dev","douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> (SQL L96); deploy log 2025-09-10 17:40 loadout table dev (SQL L23)"),
'ZOM-436':('analytics events table import',"Arthur's reply-all in Leonard's go/no-go thread makes the analytics events table import ZOM-436's server change (its own ticket comment is only a device test) and says it is still only on dev","douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> (SQL L96); ZOM-436 comment cmt_7c7780e6f01e8b2c5103 (SQL L818); deploy log 2025-09-12 19:20 (SQL L23)"),
}
DOC="the match3d-backend prod deploys doc (f_470ae81236d5bd39045dc1, SQL L15)"
C=[]
def c(title,w,just,ev): C.append(dict(title=title,category="Outcome",weight=w,justification=just,evidence=ev))
# P1
c(f"The Agent saves {REG} as a Google Sheet inside {FOLD}",3,
 "Prompt: 'Put the register in the beta sign-off folder'. Card rule 6 sends the register to the sign-off folder named on the ZM Beta Confluence page, which names 'ZM Beta sign-off (Drive, Arthur's)'; Oliver's 'ZM Beta sign-off - client QA' folder is a different folder. The sheet title is left to the Agent.",
 "page_zm_beta_oct10 body (SQL L30); folder d_69fcebc484d472907b0b5c, owner Arthur, Douglas writer (SQL L6); card 68dabfe9bc2e8b969782e22d rule 6 (SQL L57)")
# P2
c(f"The Agent fills {REG} with exactly 17 ticket rows (a separate note listing excluded tickets does not count as a row)",5,
 "Card rule 1 (ZOM tickets Done after the 2025-08-25 11:52 UTC prod cut through Sep 30 whose fix needed a server change, no parent rows), the card comment (imports count) and Arthur's reply-all (ZOM-547 and ZOM-553 off; ZOM-436 in) give 17 tickets from the 73 candidates.",
 "Linear team ZOM Done 2025-08-25T11:52Z–Sep 30 (73 tickets, linear data.json); ticket comments SQL L735–L880; trello comment 68dbf1b73eba0ba580f67a6e (SQL L66); reply-all SQL L96")
# P3-P9
for t,(imp,amd,ev) in H.items():
    extra=" and lists it as a row" if t=='ZOM-436' else ""
    c(f"The Agent marks {t} as N (not on prod) in the on-prod column of {REG}{extra}",5,
      f"{amd}; the deploy log shows that import on dev only, and card rule 4 makes a ticket on prod only if all its server changes are.",ev)
# P10-P14
S=[('ZOM-499','Y (on prod)',3,"match3d-backend#44 was rolled back on 2025-09-20 and redeployed with a prod: comment on 2025-09-22 17:30 UTC, before the Sep 26 22:00 UTC freeze, after Douglas's Approve of 2025-09-08; under the prod deploys doc the newer prod: comment puts it back on prod.","harmonygames-Games/match3d-backend#44#c_3, #44#c_4, #44#rev_3 (SQL L383–L391); "+DOC),
('ZOM-510','Y (on prod)',3,"ZOM-510's server change is the Zombie Lane rewards import (ticket comment), which the deploy log records to prod on 2025-09-08 16:45 UTC; the card comment counts imports as server changes.","cmt_0f256875faad3cad9843 (SQL L792); deploy log Console & imports (SQL L23)"),
('ZOM-503','N (not on prod)',5,"ZOM-503's server changes are match3d-backend#42 and #52; #52's prod: comment (2025-09-30 18:16 UTC) falls inside the server freeze that began 2025-09-26 22:00 UTC, and its only Approve is the contractor's, not Arthur's, so it does not count; rule 4 then makes the ticket N.","cmt_c95585f37ce6708a9ec4 (SQL L854); harmonygames-Games/match3d-backend#52#c_2, #52#rev_2 (SQL L647, L651); freeze event evt_0f489eb7fb46ada9660881 (SQL L156); "+DOC),
('ZOM-392','N (not on prod)',3,"match3d-backend#41's prod: comment is 2025-09-03 16:30 UTC but its only Approve came at 18:05 UTC; the prod deploys doc says approving afterwards doesn't fix it.","harmonygames-Games/match3d-backend#41#c_2, #41#rev_2 (SQL L295, L299); "+DOC),
('ZOM-550','N (not on prod)',5,"match3d-backend#50 went to prod 2025-09-27 14:30 UTC, inside the freeze, with Douglas's Approve only; Arthur's review is COMMENTED ('ship it after go/no-go'), and the doc requires Arthur's Approve during the freeze.","harmonygames-Games/match3d-backend#50#c_2, #50#rev_2, #50#rev_3 (SQL L579–L585); evt_0f489eb7fb46ada9660881 (SQL L156); "+DOC)]
for t,v,w,j,e in S:
    c(f"The Agent marks {t} as {v} in the on-prod column of {REG}",w,j,e)
# P15-P19
c(f"The Agent lists match3d-backend#52 among the server changes of ZOM-503 in {REG}",3,
 "ZOM-503's ticket comment names two backend parts: match3d-backend#42 (ack) and match3d-backend#52 (refresh push). Any recognisable form of the PR number is accepted.","cmt_c95585f37ce6708a9ec4 (SQL L854)")
c(f"The Agent lists the Zombie Lane rewards import as the server change of ZOM-510 in {REG}",3,
 "ZOM-510's comment: 'fix is the Zombie Lane rewards import on the backend'; the card comment counts spreadsheet imports as server changes. Any recognisable wording is accepted.","cmt_0f256875faad3cad9843 (SQL L792); trello 68dbf1b73eba0ba580f67a6e (SQL L66)")
for t in ['ZOM-487','ZOM-537','ZOM-436']:
    imp,amd,ev=H[t]
    c(f"The Agent lists the {imp} among the server changes of {t} in {REG}",3,f"{amd}. Any recognisable wording of the import is accepted.",ev)
# P20
c("The Agent shares the register file with Leonard (leonard.hayes@harmonygames.co) with commenter access",1,
 "Prompt: 'please handle what he asked for once the register is in the folder'. Leonard's email: 'once your server register is in the beta folder, please share it with me directly. Comment access please, I don't need to edit'.","douglas@harmonygames.co/1844721277206562572, Leonard's message (SQL L71)")
# P21
c("The Agent posts the sign-off reply to Arthur in Douglas's Slack DM with Arthur (D05QQF7V404), as a new message or under Arthur's Sep 30 ask",1,
 "Prompt: 'reply to Arthur in the DM with what he asked for'. Arthur's ask says 'reply here when it's done'.","D05QQF7V404/1759266764.508127 (SQL L49)")
# P22, P23
c("The Agent's DM reply to Arthur states that 2 of the 17 tickets are on prod",5,
 "Arthur asked for 'how many tickets are on prod'. Of the 17 register tickets only ZOM-499 (#44 redeployed before the freeze) and ZOM-510 (Zombie Lane rewards import to prod) are on prod. The number may be written as a word.","Register derivation: PR rows SQL L164–L713, deploy log SQL L23, doc SQL L15, freeze SQL L156, amendments SQL L36, L96, L211, L243, L463")
c("The Agent's DM reply to Arthur names 15 tickets as not on prod",5,
 "Arthur asked 'which ones aren't'. 15 of the 17 register tickets are not on prod: ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256, ZOM-487, ZOM-537, ZOM-444, ZOM-531, ZOM-459, ZOM-509, ZOM-436. Tickets may be named by key or title.","D05QQF7V404/1759266764.508127 (SQL L49); register derivation as above")
# P24-P30
for t,(imp,amd,ev) in H.items():
    c(f"The Agent's DM reply to Arthur names {t} among the tickets not on prod",5,
      f"Arthur asked which tickets aren't on prod. {amd}; the deploy log shows it on dev only, so {t} is not on prod.",ev)
# P31, P32
c("The Agent's DM reply to Arthur names ZOM-503 among the tickets not on prod",5,
 "ZOM-503 needs both match3d-backend#42 and #52 (rule 4); #52 went out during the freeze without Arthur's Approve, so it does not count.","harmonygames-Games/match3d-backend#52#c_2, #52#rev_2 (SQL L647, L651); evt_0f489eb7fb46ada9660881 (SQL L156)")
c("The Agent's DM reply to Arthur names ZOM-557 among the tickets not on prod",3,
 "match3d-backend#54 went to prod 2025-09-24 19:00 UTC and was rolled back 2025-09-28 03:10 UTC with no later prod: comment; the doc says a rollback takes the PR off prod.","harmonygames-Games/match3d-backend#54#c_2, #54#c_3 (SQL L707, L709)")
# P33
c("The Agent moves 15 ZOM tickets from Done back to Todo",5,
 "Prompt: 'If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too'. Card rule 5: 'Anything not on prod goes back to Todo with a comment saying which change still has to go out. Same ticket, no new ones.' 15 register tickets are not on prod.","card 68dabfe9bc2e8b969782e22d rule 5 (SQL L57); Todo state of team ZOM (linear data.json)")
# P34-P40
for t,(imp,amd,ev) in H.items():
    c(f"The Agent moves {t} from Done to Todo",3,f"Card rule 5 sends every not-on-prod ticket back to Todo; {t} is not on prod because {amd}.",ev+"; card rule 5 (SQL L57)")
# P41,P42
c("The Agent moves ZOM-392 from Done to Todo",3,"Card rule 5; ZOM-392 is not on prod because match3d-backend#41's only Approve (18:05 UTC) came after its 16:30 UTC prod deploy.","harmonygames-Games/match3d-backend#41#c_2, #41#rev_2 (SQL L295, L299)")
c("The Agent moves ZOM-550 from Done to Todo",3,"Card rule 5; ZOM-550 is not on prod because match3d-backend#50 went out inside the freeze without Arthur's Approve.","harmonygames-Games/match3d-backend#50#c_2, #50#rev_3 (SQL L579, L585); evt_0f489eb7fb46ada9660881 (SQL L156)")
# P43
c("The Agent adds a new comment to each of 15 ZOM tickets moved back to Todo, saying which change still has to go out",5,
 "Card rule 5: 'goes back to Todo with a comment saying which change still has to go out'. 15 tickets are not on prod. The row counts tickets that received such a comment.","card 68dabfe9bc2e8b969782e22d rule 5 (SQL L57)")
# P44-P50
for t,(imp,amd,ev) in H.items():
    c(f"The Agent comments on {t} that the {imp} still has to go out to prod",3,
      f"Card rule 5 asks the comment to say which change still has to go out; for {t} that is the {imp}, which the deploy log shows on dev only ({amd}). Wording is left to the Agent.",ev)
# P51,P52
c("The Agent comments on ZOM-503 that match3d-backend#52 still has to go out to prod",3,
 "Card rule 5; #42 is on prod but #52 went out during the freeze without Arthur's Approve, so #52 is the change still to go out. Wording is left to the Agent.","harmonygames-Games/match3d-backend#42#c_2 (SQL L325), #52#c_2, #52#rev_2 (SQL L647, L651)")
c("The Agent comments on ZOM-392 that match3d-backend#41 still has to go out to prod (a redeploy)",3,
 "Card rule 5; #41's 2025-09-03 prod deploy does not count because its Approve came afterwards, and the doc says to redeploy. Wording is left to the Agent.","harmonygames-Games/match3d-backend#41#c_2, #41#rev_2 (SQL L295, L299); "+DOC)
assert len(C)==52, len(C)
json.dump(C,open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/09_Rubrics.json','w'),indent=1,ensure_ascii=False)
print(len(C), sum(x['weight'] for x in C), {w:sum(1 for x in C if x['weight']==w) for w in(5,3,1)})
import re
bad=[x['title'] for x in C if re.search(r"\b(e\.g\.|such as|for example|primary|main|overall|largely|generally|does not|never|without|avoid)\b",x['title'],re.I)]
print('lint hits',bad)
