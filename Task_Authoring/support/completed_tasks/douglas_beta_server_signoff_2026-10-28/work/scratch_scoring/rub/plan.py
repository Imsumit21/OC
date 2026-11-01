import re
S_WAY='"Can you take care of it for me, the way he laid it out?"'
S_REG='"Put the register in the beta sign-off folder"'
S_DM='"reply to Arthur in the DM with what he asked for"'
S_RULE='"If his sign-off rules say something has to happen to the tickets that aren\'t on prod, go ahead and do that too, no need to wait on me."'
S_LEO='"Leonard also emailed me about the go/no-go, so please handle what he asked for once the register is in the folder."'
HID={ # ticket: (amendment record, import, OE pr, F pr, chain id)
'ZOM-459':('inline review comment harmonygames-Games/match3d-backend#38#rc_1','plague race table import','16','F16','C12'),
'ZOM-509':('inline review comment harmonygames-Games/match3d-backend#39#rc_1','trophy path copy table import','17','F17','C13'),
'ZOM-537':('inline review comment harmonygames-Games/match3d-backend#46#rc_1','economy table import','24','F24','C10'),
'ZOM-487':('Arthur\'s reply comment_zm_beta_oct10_c2 on page_zm_beta_oct10','boss arena HP table import','26','F5','C9'),
'ZOM-444':('Arthur\'s reply-all (second point)','analytics events table import','25','F11','C11'),
'ZOM-531':('Arthur\'s reply-all (second point)','loadout table import','23','F11','C11'),
'ZOM-436':('Arthur\'s reply-all (second point)','analytics events table import','13','F11','C11'),
}
LOGROW={'plague race table import':'2025-08-26 10:30','trophy path copy table import':'2025-09-02 18:05','economy table import':'2025-09-16 14:20','boss arena HP table import':'2025-09-17 15:50','analytics events table import':'2025-09-12 19:20','loadout table import':'2025-09-10 17:40'}
rows=[] # dict(P, src, oe, what, state, values, title, distr, amb, kind, band, dec, grp, dup, af)
def R(**k): rows.append(k)
R(src=S_REG,oe='4, 6, 33',what='Register location — a Google Sheet saved in Arthur\'s "ZM Beta sign-off" folder',state='Drive file whose parent is d_69fcebc484d472907b0b5c',values='F4 F10 `ZM Beta sign-off`; exact folder; title ungraded',title='no — must not hard-code the sheet title',distr='T9 client QA folder → the row names the exact folder',amb='no',kind='interpretation — card rule 6 → page → folder, with a look-alike folder',band='3',dec='F4 T9',grp='—',dup='none',af='none · accept create-in-folder or create-then-move')
R(src=S_WAY,oe='12, 13, 14, 33',what='Register volume — exactly 17 ticket rows',state='Row set of the register',values='F12 F13 F14 F11 `17`; exact count (ZOM-547, ZOM-553, ZOM-457, ZOM-461 not rows; ZOM-436 is a row)',title='no',distr='T12 ZOM-547/ZOM-553, T13 → the count rejects them',amb='no',kind='multi-source — 73 comment threads, rule 1, the card comment and the reply-all',band='5',dec='T12 T13 C11',grp='G1 volume',dup='none; register only',af='none · accept a separate notes line listing excluded tickets kept apart from the rows')
for t,(amd,imp,oe,f,ch) in HID.items():
    if t=='ZOM-436':
        R(src=S_WAY,oe=f'11, 13, 32, 33',what=f'{t} register row — present and marked not on prod (N)',state=f'{t} row, on-prod column',values=f'{f} F8 F31 `{t}` `N`; exact',title='no',distr='T11 → its own comment names no server change',amb='no',kind=f'multi-source — the reply-all adds the ticket, the deploy log shows the {imp} on dev only',band='5',dec=f'{ch} T11',grp='G1 exception (direct)',dup='register; the DM and Todo rows are other deliverables',af='none')
    else:
        R(src=S_WAY,oe=f'{oe}, 9, 32, 33',what=f'{t} register row — marked not on prod (N)',state=f'{t} row, on-prod column',values=f'{f} F8 F31 `{t}` `N`; exact',title='no',distr=f'T11 → the ticket note names one PR, which is on prod',amb='no',kind=f'multi-source — {amd}, the deploy log ({imp} on dev, {LOGROW[imp]}) and the PR prod: comment',band='5',dec=f'{ch} T11',grp='G1 exception (direct)',dup='register; DM and Todo rows are other deliverables',af='none')
SAMP=[('ZOM-499','Y','22','F22','prod after the rollback (#44 prod: 2025-09-22 17:30 UTC, before the freeze)','comparison — rollback then a newer prod: comment against the freeze start','3','edge: rolled back then redeployed'),
('ZOM-510','Y','9, 13','F8 F13','the Zombie Lane rewards import went to prod (deploy log 2025-09-08 16:45)','interpretation — an import-only change read from the log under the card comment','3','edge: import-only Y'),
('ZOM-503','N','20, 29','F20 F29 F7','#42 on prod but #52 went out in the freeze without Arthur\'s Approve (rule 4)','multi-source — two PRs, the freeze event, the doc and the reviewer identity','5','edge: two server changes'),
('ZOM-392','N','19','F19','#41 prod: 16:30 UTC before its only Approve 18:05 UTC','comparison — deploy time against review time under the doc','3','edge: Approve after the deploy'),
('ZOM-550','N','27, 31','F27 F7','#50 prod: 2025-09-27 14:30 UTC in the freeze; Arthur only COMMENTED','multi-source — the freeze event, the doc and the reviewer identity','5','edge: freeze without Arthur')]
for t,v,oe,f,why,kind,b,edge in SAMP:
    R(src=S_WAY,oe=f'{oe}, 32, 33',what=f'{t} register row — marked {"on prod (Y)" if v=="Y" else "not on prod (N)"}',state=f'{t} row, on-prod column',values=f'{f} F6 F31 `{t}` `{v}`; exact',title='no',distr='T1 Oliver\'s all-on-prod summary' if v=='N' else 'T10 Prod deploys tab',amb='no',kind=kind,band=b,dec='H2 doc + freeze' if b=='5' else 'H2 doc',grp=f'G1 sample ({edge})',dup='register',af='none')
SC=[('ZOM-503','`#52` (match3d-backend#52)','F13 F29','13, 29','lookup — named in the ticket note','3','edge: second change'),
('ZOM-510','`Zombie Lane rewards import`','F13 F8','13, 9','interpretation — import counted through the card comment','3','edge: import only'),
('ZOM-487','`boss arena HP table import`','F5 F8','5, 9','interpretation — the page reply names the import outright','3','exception'),
('ZOM-537','`economy table import`','F24 F8','24, 9','interpretation — the inline review comment names the import outright','3','exception'),
('ZOM-436','`analytics events table import`','F11 F8','11, 9','interpretation — the reply-all names the import outright','3','exception')]
for t,val,f,oe,kind,b,edge in SC:
    R(src=S_WAY,oe=f'{oe}, 32, 33',what=f'{t} register row — server change(s) include the {val.strip("`")}' if 'import' in val else f'{t} register row — server change(s) include match3d-backend#52',state=f'{t} row, server change column',values=f'{f} `{t}` {val}; the change named in any recognisable words (brief §4b)',title='no',distr='T11 ticket notes name one PR only' if 'import' in val and t!='ZOM-510' else 'none',amb='no',kind=kind,band=b,dec='C9 C10 C11'.split()[[ 'ZOM-487','ZOM-537','ZOM-436'].index(t)] if t in('ZOM-487','ZOM-537','ZOM-436') else 'F13',grp=f'G2 sample ({edge})',dup='register; the Todo comment (P44–P50) is another deliverable',af='none · phrase broadly')
R(src=S_LEO,oe='10, 11, 34',what='Register shared with Leonard as commenter',state='Permission on the register file',values='F9 `leonard.hayes@harmonygames.co` `commenter`; exact role',title='no',distr='none',amb='no',kind='lookup — one email names the grantee and role',band='1',dec='F9',grp='—',dup='none',af='none · a direct file share (not the folder)')
R(src=S_DM,oe='1, 66',what='Reply posted in Douglas\'s DM with Arthur',state='Slack message in DM D05QQF7V404',values='F1 `D05QQF7V404`; top level or under the ask',title='no',distr='T14 #zombie-match3d copy is extra, not a substitute',amb='no',kind='lookup — the DM is the ask\'s own channel',band='1',dec='F1',grp='—',dup='none',af='none · phrase broadly (thread or top level)')
R(src=S_DM,oe='32, 66',what='Reply — on-prod count of 2 (of 17)',state='DM reply text',values='F32 `2`; exact count',title='no',distr='T1, T12 → 9 or 10 of 18 rejected',amb='no',kind='multi-source — the count only the full audit produces',band='5',dec='F31',grp='G3 volume (on prod)',dup='DM only',af='none · number or word')
R(src=S_DM,oe='32, 66',what='Reply — 15 tickets named as not on prod',state='DM reply text',values='F32 `15`; exact count',title='no',distr='T12',amb='no',kind='multi-source — the count only the full audit produces',band='5',dec='F31',grp='G3 volume',dup='DM only',af='none')
for t,(amd,imp,oe,f,ch) in HID.items():
    R(src=S_DM,oe=f'{oe}, 32, 66',what=f'Reply — {t} named among the tickets not on prod',state='DM reply text',values=f'{f} F32 `{t}`; key or title',title='no',distr='T11',amb='no',kind=f'multi-source — same determination as the register row, required again by the ask ("which ones aren\'t")',band='5',dec=f'{ch}',grp='G3 exception (direct)',dup='DM; register row is another deliverable (gate 6)',af='none')
for t,b,f,oe,why in [('ZOM-503','5','F20 F29 F7','20, 29','#52 in the freeze'),('ZOM-557','3','F30','30','#54 rolled back')]:
    R(src=S_DM,oe=f'{oe}, 32, 66',what=f'Reply — {t} named among the tickets not on prod',state='DM reply text',values=f'{f} F32 `{t}`; key or title',title='no',distr='T1 Oliver\'s summary',amb='no',kind=('multi-source — two PRs, freeze and reviewer identity' if b=='5' else 'comparison — prod: then rollback: comment'),band=b,dec='H2 doc',grp=f'G3 sample ({why})',dup='DM',af='none')
R(src=S_RULE,oe='35–65',what='Todo moves — 15 tickets moved back to Todo',state='Linear state of the not-on-prod tickets',values='F15 F31 `15` `Todo`; exact count',title='no',distr='T7 client card → In Validation rejected',amb='no',kind='multi-source — the count only the full audit produces',band='5',dec='F2 rule 5',grp='G4 volume',dup='Todo only',af='none')
OEMV={'ZOM-336':36,'ZOM-392':38,'ZOM-503':40,'ZOM-518':42,'ZOM-550':44,'ZOM-435':46,'ZOM-557':48,'ZOM-256':50,'ZOM-487':52,'ZOM-537':54,'ZOM-444':56,'ZOM-531':58,'ZOM-459':60,'ZOM-509':62,'ZOM-436':64}
for t,(amd,imp,oe,f,ch) in HID.items():
    R(src=S_RULE,oe=f'{OEMV[t]}',what=f'{t} moved to Todo',state=f'{t} state',values=f'{f} F15 F31 `{t}` `Todo`; exact state',title='no',distr='T7 (In Validation)',amb='no',kind='multi-source — the move follows only from the hidden determination',band='5',dec=ch,grp='G4 exception (direct)',dup='Todo state; comment row is a separate write',af='none')
for t,b,f in [('ZOM-392','3','F19'),('ZOM-550','5','F27 F7')]:
    R(src=S_RULE,oe=f'{OEMV[t]}',what=f'{t} moved to Todo',state=f'{t} state',values=f'{f} F15 `{t}` `Todo`; exact state',title='no',distr='T2 Douglas\'s Sep 22 claim' if t=='ZOM-392' else 'T4 #50 thread',amb='no',kind='comparison — late Approve' if b=='3' else 'multi-source — freeze, doc, reviewer identity',band=b,dec='H2 doc',grp='G4 sample',dup='Todo state',af='none')
R(src=S_RULE,oe='37–65 (odd)',what='Todo comments — 15 tickets each get a comment on what still has to go out',state='New Linear comments',values='F31 `15`; exact count',title='no',distr='none',amb='no',kind='multi-source — the count only the full audit produces',band='5',dec='F2 rule 5',grp='G5 volume',dup='comments only',af='none')
for t,(amd,imp,oe,f,ch) in HID.items():
    R(src=S_RULE,oe=f'{OEMV[t]+1}',what=f'{t} comment — names the {imp} as the change still to go out',state=f'New comment on {t}',values=f'{f} F31 `{t}` `{imp}`; any wording naming that import',title='no — wording delegated',distr='T11 (a comment naming only the PR fails)',amb='no',kind='interpretation — names the change the register row already holds',band='3',dec=ch,grp='G5 exception (direct)',dup='comment; register server-change row is another deliverable',af='none · phrase broadly')
for t,val,f in [('ZOM-503','match3d-backend#52','F29'),('ZOM-392','match3d-backend#41 (a redeploy)','F19')]:
    R(src=S_RULE,oe=f'{OEMV[t]+1}',what=f'{t} comment — names {val} as the change still to go out',state=f'New comment on {t}',values=f'{f} F31 `{t}` `{val.split()[0]}`; any wording naming that PR',title='no — wording delegated',distr='none',amb='no',kind='interpretation — names the PR the register row holds',band='3',dec='H2 doc',grp='G5 sample',dup='comment',af='none · phrase broadly')
for i,r in enumerate(rows,1): r['P']=f'P{i}'
N=len(rows)
A='\n'.join(f"| {r['P']} | {r['src']} · OE {r['oe']} | {r['what']} | {r['state']} | Outcome | {r['values']} |" for r in rows)
A2='\n'.join(f"| {r['P']} | {r['title']} | {r['distr']} | {r['amb']} | {r['kind']} | {r['band']} | {r['dec']} | {r['grp']} | {r['dup']} | {r['af']} |" for r in rows)
bands={b:sum(1 for r in rows if r['band']==b) for b in '531'}
W=sum(int(r['band']) for r in rows)
open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/rub/AA2.md','w').write(A+'\n@@@\n'+A2)
import json; json.dump(dict(N=N,bands=bands,W=W,rows=[{k:r[k] for k in('P','what','band','grp')} for r in rows]),open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/rub/meta.json','w'),indent=0)
print(N,bands,W)
for r in rows: print(r['P'],r['band'],r['what'][:70])
