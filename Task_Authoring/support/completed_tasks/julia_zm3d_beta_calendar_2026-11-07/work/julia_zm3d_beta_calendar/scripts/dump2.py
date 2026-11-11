import json,sys,datetime
from collections import defaultdict
n=json.load(open('raw/slack_names.json'))
d=json.load(open(sys.argv[1]))
msgs=[m for m in d if (m.get('text') or '').strip()]
for m in msgs:
    ts=m.get('ts','')
    t=datetime.datetime.fromtimestamp(float(ts),datetime.timezone.utc).strftime('%m-%d %H:%MZ')
    u=n.get(m.get('user'),m.get('user'))
    tag=''
    if m.get('thread_ts') and m['thread_ts']!=ts: tag=' REPLY->'+m['thread_ts']
    elif m.get('reply_count'): tag=' THREAD(rp=%s)'%m['reply_count']
    print('%s %s %s%s'%(ts,t,u,tag))
    print('   '+m.get('text','').replace('\n','\n   ')[:1800])
