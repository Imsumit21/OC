"""Round 5 hardening: SQL transform (idempotent from the round-4 SQL dd7536cdea3f).

1. Blake's reply (CA5_...) moves to its own Gmail thread: he changed the subject, which in Gmail starts a new
   conversation. It keeps In-Reply-To/References. It now carries the editor/debug stripping rule and both ZOM-199
   corrections (> 90; 10 games, wins and losses). It never uses the words 'store' or 'builds'.
2. The first mail keeps the two build versions and the Sep 26 cut only.
3. Card rule 3 names the reply: "Blake's store builds mail and his reply to it."
4. Leonard's thread reply under the ask adds: the Editor only and Not shipped comments name the two builds.

Usage: harden_r5.py <round-4 sql> <out sql>
"""
import random
import re
import sys

src, out = sys.argv[1], sys.argv[2]
s = open(src).read()
assert 'dd7536cdea3f' or True


def once(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, count, old[:80])
    s = s.replace(old, new)


# --- 2. first mail: drop the stripping paragraph (5 mailbox copies)
STRIP = ("\\n\nThe level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and "
         "the debug menu (Assets/Scripts/Debug) are stripped from store builds. A ticket whose changes are only level editor "
         "or debug tooling never reached players, Done or not.\\n\n")
n = s.count(STRIP)
if n == 0:  # the SQL uses \n escapes inside E'' strings; find the real form
    m = re.search(r"\n\\n\n\\nThe level editor \(Assets/Scripts/LevelEditor.*?Done or not\.", s, re.S)
    assert m, 'stripping paragraph not found'
    STRIP = m.group(0)
    n = s.count(STRIP)
assert n == 5, n
s = s.replace(STRIP, "")

# --- 1. Blake's reply: new thread per mailbox, new subject and body
BOXES = ['julia.lawson', 'leonard.hayes', 'robert', 'brian.foster', 'arthur.blake']
random.seed(5)
TID = {b: (1759238765000 << 20) + (0x2D5A9 if b == 'julia.lawson' else random.randrange(1 << 20)) for b in BOXES}
OLD_TID = {'julia.lawson': '1844679607844896665', 'leonard.hayes': '1844679607845770780', 'robert': '1844679607845885165',
           'brian.foster': '1844679607844988891', 'arthur.blake': '1844679607845878519'}
SUBJ = 'editor stuff and ZOM-199, before Monday'
BODY_TXT = ("Two things I left out of the mail this morning.\\n\\n"
            "1. The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and "
            "the debug menu (Assets/Scripts/Debug) are stripped before we ship to players on iOS and Android. A ticket whose "
            "changes are only level editor or debug tooling never reached players, Done or not.\\n\\n"
            "2. For the rules tab: the starting tier check in the code is cpm > 90, not >= 90, and it runs when a player''s "
            "10th game ends, wins and losses both counted, not after 10 levels cleared. ZOM-199 says >= 90 after the first "
            "10 levels, but the code never changed from the original spec, so 90 exactly stays on tier 0.\\n\\nBlake")
SNIP = 'Two things I left out of the mail this morning. 1. The level editor (Assets/Scripts/LevelEditor and the LevelDesigner'
for b in BOXES:
    mid = f"{b}@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>"
    i = s.find(f"VALUES ('{mid}'")
    assert i > 0, mid
    j = s.find("');\n", i) + 3
    row = s[i:j]
    new = row.replace(f"'{b}@harmonygames.co/{OLD_TID[b]}'", f"'{b}@harmonygames.co/{TID[b]}'")
    assert new != row
    new = re.sub(r"'One more, for the rules tab: the starting tier check in the build is cpm > 90, not >= 90\. ZOM-199 says >= but the code never changed from th'",
                 f"'{SNIP}'", new, count=1)
    new = new.replace("'Re: store builds for monday'", f"'{SUBJ}'", 1)
    new = new.replace('"value": "Re: store builds for monday"', f'"value": "{SUBJ}"', 1)
    new = re.sub(r"E'One more, for the rules tab:.*?', NULL, '\[\{\"name\": \"Message-ID\"",
                 lambda m: "E'" + BODY_TXT + "', NULL, '[{\"name\": \"Message-ID\"", new, count=1, flags=re.S)
    new = new.replace(", 1361, ", ", 1544, ", 1)
    assert 'store builds' not in new.lower() and 'One more' not in new, (b, new[:300])
    s = s[:i] + new + s[j:]
    # thread row for the new conversation, inserted right before the reply's message row
    k = s.rfind('INSERT INTO gmail.gmail_messages', 0, s.find(f"VALUES ('{mid}'"))
    trow = ("INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id)\n"
            f"VALUES ('{b}@harmonygames.co/{TID[b]}', '{b}@harmonygames.co', '{SNIP}', NULL);\n")
    s = s[:k] + trow + s[k:]
    # the first mail's thread now holds one message: its snippet becomes the first mail's
    s = s.replace(f"VALUES ('{b}@harmonygames.co/{OLD_TID[b]}', '{b}@harmonygames.co', 'One more, for the rules tab: the starting tier check in the build is cpm > 90, not >= 90. ZOM-199 says >= but the code never changed from th', NULL);",
                  f"VALUES ('{b}@harmonygames.co/{OLD_TID[b]}', '{b}@harmonygames.co', 'Hi all, For Monday, so we''re talking about the same thing. The store builds players have today are iOS 0.3.49 (Leonard released it yesterday', NULL);")

# --- 3. card rule 3
once("what counts as shipped: Blake''s store builds mail.", "what counts as shipped: Blake''s store builds mail and his reply to it.", 2)

# --- 4. Leonard's thread reply under the ask
once("so i know who to chase'", "so i know who to chase. and when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against'")

open(out, 'w').write(s)
print('ok', {b: TID[b] for b in BOXES})
