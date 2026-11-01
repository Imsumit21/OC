# Round 3 calibration: move the three custody notices into September so that
# about half of the baseline runs' dated vendor searches reach them.
import json, sys, re
from datetime import datetime, timezone
SQL = 'task_inputs/01_Universe_Inject.sql'
FRED = 'frederick.stone@harmonygames.co'
MOVES = [  # old thread id, old ISO, new ISO
    ('1834647853990444617', '2025-06-11T15:42:18Z', '2025-09-09T15:42:18Z'),  # YouTube Brand Account
    ('1837824433193834721', '2025-07-16T17:12:40Z', '2025-09-18T17:12:40Z'),  # TikTok partner
    ('1839715197125206004', '2025-08-06T14:05:33Z', '2025-09-15T14:05:33Z'),  # Instagram full control
]
def ms(iso): return int(datetime.strptime(iso, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc).timestamp() * 1000)
def rfc(iso): return datetime.strptime(iso, '%Y-%m-%dT%H:%M:%SZ').strftime('%a, %d %b %Y %H:%M:%S +0000')
s = open(SQL, 'rb').read().decode()
mapping = {}
for old_tid, old, new in MOVES:
    assert int(old_tid) >> 20 == ms(old), old_tid
    new_tid = str((ms(new) << 20) | (int(old_tid) & 0xFFFFF))
    for a, b, n in [(f'{FRED}/{old_tid}', f'{FRED}/{new_tid}', 2), (f'{ms(old)}, \'{old}\'', f'{ms(new)}, \'{new}\'', 1),
                    (rfc(old), rfc(new), 1)]:
        assert s.count(a) == n, (a, s.count(a)); s = s.replace(a, b)
    mapping[old_tid] = new_tid
open(SQL, 'wb').write(s.encode())
json.dump(mapping, sys.stdout)
