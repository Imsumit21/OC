import json,collections
from decimal import Decimal as D
un=[x for x in json.load(open('unmatched.json')) if x['cycle'] and x['cycle']<='2025-09']
MAP=[('1PASSWORD','1Password','SW'),('APPMAGIC','AppMagic','SW'),('APPLE.COM/BILL','Apple Developer Program','SW'),('BACKTRACE','Backtrace','SW'),('CALENDLY','Calendly','SW'),('CANVA','Canva','SW'),('DOCUSIGN','DocuSign','SW'),('ELEVENLABS','ElevenLabs','SW'),('ENVATO','Envato Elements','SW'),('LINKEDIN','LinkedIn Sales Navigator','SW'),('LOOM','Loom','SW'),('MAILCHIMP','Mailchimp','SW'),('MIDJOURNEY','Midjourney','SW'),('NOTION','Notion','SW'),('OPENAI','OpenAI ChatGPT','SW'),('SENSOR TOWER','Sensor Tower','SW'),('SUPERNORMAL','Supernormal','SW'),('UNITY TECHNOLOGIES','Unity Technologies','HOST'),('ZAPIER','Zapier','SW'),('ZOOM','Zoom','SW'),
('GOOGLE *CLOUD','Google Cloud','HOST'),('HEROIC','Heroic Labs','HOST'),('NAMECHEAP','Namecheap','HOST'),('WEBFLOW','Webflow','HOST'),('PLAYTESTCLOUD','PlaytestCloud','RES'),('FIVERR','Fiverr','MKT'),('INFORMA','Informa','MKT'),('MARRIOTT','Marriott','TRAVEL'),('UBER','Uber','TRAVEL'),('UNITED','United Airlines','TRAVEL'),('APPLE STORE','Apple Store','HW'),('BEST BUY','Best Buy','HW'),('CARTA','Carta','PRO'),('COGENCY','Cogency Global','PRO'),('DEEL','Deel','PRO'),('DE DIV','Delaware Div of Corporations','PRO'),('GUSTO','Gusto','PRO'),('INTUIT','QuickBooks Online','PRO'),('USPTO','USPTO','PRO'),('DOORDASH','DoorDash','GA'),('FEDEX','FedEx','GA'),('WEWORK','WeWork','GA'),('UNITY ADS','Unity Ads','UA')]
def m(desc):
    for k,v,c in MAP:
        if desc.startswith(k): return v,c
    return desc,'??'
vt=collections.defaultdict(D); ct=collections.defaultdict(D); cm=collections.defaultdict(D)
for x in un:
    v,c=m(x['vendor_desc']); x['vendor']=v; x['cat']=c
    a=D(str(x['amount_usd'])); vt[v]+=a; ct[c]+=a; cm[(c,x['cycle'])]+=a
for v in sorted(vt): print(v, vt[v])
print()
for c in ct: print(c, ct[c], [str(cm[(c,f'2025-{i:02d}')]) for i in range(1,10)])
print('opex',sum(v for k,v in ct.items() if k!='UA'))
json.dump(un,open('unmatched_v.json','w'))
