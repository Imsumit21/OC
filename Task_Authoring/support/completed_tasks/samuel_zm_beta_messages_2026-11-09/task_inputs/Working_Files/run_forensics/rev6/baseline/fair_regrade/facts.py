"""Per-run item facts straight from raw write payloads, joined on the Ticket column."""
import sys,json,re,collections
sys.path.insert(0,sys.argv[1] if len(sys.argv)>1 else '.')
from load import *
TRUTH=json.load(open(f'{T}/Working_Files/run_forensics/rev6/truth.json'))
ITEMS={k:v for k,v in TRUTH.items() if v.get('Call')}
BYT={v['Ticket']:k for k,v in ITEMS.items() if v.get('Ticket')}
FOLDER='d_caafeec2804b3a67ce46aa'
def facts(path):
    calls,fin,ev=load(path)
    F=dict(rows={},comments=collections.defaultdict(list),upd={},new=[],checks=[],mails=[],dm='',note='',parents={},calls=calls,final=fin or '')
    sheet=None
    for c in calls:
        t,i=c['tool'],c['input']; ok=not c['err'] and '"error"' not in str(c['result'])[:60]
        if t=='gsheets_values_update' and ok and isinstance(i.get('values'),list):
            for r in i['values'][1:]:
                if len(r)>1 and str(r[1]).startswith('DES-'):
                    r=[str(x) for x in r]+['']*7
                    F['rows'][r[1].split()[0]]=dict(Message=r[0],Ticket=r[1],Call=r[2],Miss=r[3],Aud=r[4],Head=r[5],Str=r[6])
            sheet=i.get('spreadsheetId')
        if t=='linear_create_comment' and ok: F['comments'][i.get('issueId')].append(i.get('body',''))
        if t=='linear_update_issue' and ok: F['upd'][i.get('id')]=dict(state=i.get('state'),assignee=i.get('assignee','__absent__'))
        if t=='linear_create_issue' and ok: F['new'].append(i)
        if t=='trello_create_check_item' and ok: F['checks'].append(i.get('name',''))
        if t=='gmail_send_message' and ok: F['mails'].append(i)
        if t in('slack_send_message','slack_conversations_add_message') and ok: F['dm']=i.get('message') or i.get('text') or ''; F['dmch']=i.get('channel_id')
        if t=='gdocs_create_document' and ok: F['note']=i.get('bodyText','')
        if t=='gdocs_batch_update' and ok:
            for rq in i.get('requests',[]):
                rp=rq.get('replaceAllText')
                if rp: F['note']=F['note'].replace(rp['containsText']['text'],rp['replaceText'])
                it=rq.get('insertText')
                if it and it.get('text') and len(it['text'])>len(F['note']): F['note']=it['text']
        if t=='gdrive_move_file' and ok: F['parents'][i.get('fileId')]=i.get('newParentId')
        if t=='gdrive_create_file' and ok:
            m=re.search(r'\\?"id\\?":\s*\\?"([^"\\]+)',str(c['result']))
            if m: F['parents'][m.group(1)]=i.get('parentId')
    F['sheet']=sheet
    return F
