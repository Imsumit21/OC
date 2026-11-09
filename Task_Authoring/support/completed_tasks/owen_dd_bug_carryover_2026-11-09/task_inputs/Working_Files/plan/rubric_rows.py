"""Rubric plan rows for owen_dd_bug_carryover (rev9), rebuilt on the /rubric round-1 Fix List (report on the reviewed JSON
2ed7a6489798; run_forensics/rev9/3_rubric_FAIL1_r1.md). One dict per criterion; consumed by assemble_rubric_plan.py,
assemble_rubric_draft.py and assemble_rubric_check.py.

Keys: p, span (exact 04_Prompt.txt span), oe (OE numbers), fact (stable fact id), what, final, cat, vals (backticked probe literals +
pointers + accepted alternatives; F-ids), phr, dis, amb, kind, band, dec (ledger trap ids), grp, dup, af, valid, idle, reach, cr.
F-ids and OE numbers are looked up by key from plan/oe_ledger_ids.json and plan/oe_events_index.json. Every Fixed item whose tick
stands now has its own state row (the Fix List: each creation carries its own title, so they are not sampled), and every UI child
has its own build-line row."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
FID = json.load(open(os.path.join(HERE, "oe_ledger_ids.json")))["fid"]
N = json.load(open(os.path.join(HERE, "oe_events_index.json")))["index"]
TRUTH = json.load(open(os.path.join(os.path.dirname(HERE), "solver", "truth.json")))


def F(*ks):
    return ", ".join(FID[k] for k in ks)


def O(*ks):
    return [N[k] for k in ks]


def line_of(key):
    """The canvas line as written, without its tick box; runs of spaces collapsed (the title's own spacing is free)."""
    s = TRUTH[key]["Bug"].replace(" ", " ")
    s = re.sub(r"^[☐☑]\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def ts_of(key):
    return TRUTH[key]["evidence"]["Outcome"][0].split("/")[-1]


S_LIN = "getting DD's bug list out of Slack and into Linear"
S_TICK = "That covers the Linear tickets"
S_TREE = "bringing the tree under the UI Changes master ticket up to date"
S_LINE = "a line on every UI child"
S_SHEET = "the sheet in my DD bug carry-over folder"
S_SHARE = "shared with everyone on the review"
S_REPLY = "Then reply to him in that DM thread with the numbers he wanted."
S_THEN = "Then reply to him in that DM thread"

NOPHR = "no — must not hard-code wording"
R = []


def row(**k):
    k.setdefault("cat", "Outcome")
    k.setdefault("phr", NOPHR)
    k.setdefault("dis", "—")
    k.setdefault("amb", "—")
    k.setdefault("grp", "—")
    k.setdefault("dec", "—")
    k.setdefault("af", "none · not over-specific")
    k.setdefault("reach", "PROMPT_LINKED")
    k["p"] = f"P{len(R) + 1}"
    R.append(k)


def bug(key):
    return "bug:" + key


FIRST_NEW, LAST_NEW = N["new:When I start the game on ios I got"], N["new:android bottom bar invisible"]

# ================================================================== Linear: the new tickets — template volume row and one sample per field
row(span=S_TICK, oe=O("canvas_find", "canvas", "posts", "decide", "rules", "amend") + list(range(FIRST_NEW, LAST_NEW + 1)), fact="new_count",
    what="how many new issues the Agent files for the carry-over, and the template each follows",
    final="exactly 68 new issues, each in Engineering with the Bug label, parent ENG-2401, no assignee, an empty description and a [2231] title",
    vals="68 new issues (63 canvas lines + 7 posts − 2 Covered; notes SQL L16 'One Linear record per canvas line and one per bug posted after it'; 'Engineering team, Bug label, parent ENG-2401, … no assignee, nothing in the description'; `[2231]` from Arthur's ENG-2401 comment SQL L311) · " + F("totals", "canvas", "posts", "apple", "signin", "rules", "amend"),
    dis="T3, T4 → graded by the count (a ticket for a Covered line makes 69)", kind="multi-source: the count only comes from the full audit of 70 items and the two Gmail/Linear ties", band=5,
    dec="T3, T4, T13", grp="G1 ticket template (volume row stating the template)", dup="new_count ×2 (this and the reply number @@P:reply_new@@ — the reply is a separate told fact)",
    valid="68 new issues under ENG-2401, each Engineering / Bug / no assignee / empty description / '[2231] …'", idle="no new issues under ENG-2401 → REJECT",
    cr="(a) a valid run could file a ticket for a deleted-line comment or a follow-up post — the notes exclude both (SQL L16), so 68 holds; (b) a wrong run could reach 68 by filing the Apple line and skipping another item — the per-item rows catch which items")
SAMPLES_T = [
    ("prefix:In profile", "In profile", ["amend"], 3, "interpretation: the prefix comes from Arthur's later comment on the master ticket, not from the notes", "`[2231] In profile,` (Arthur's ENG-2401 comment SQL L311 'put [2231] at the front of every title you file')", "G1a title prefix sample (an ordinary ticked line)", "T13"),
    ("titletext:flickering", "flickering", ["rules"], 1, "lookup: the notes set the title as the first line of the post, as it was written (the [2231] prefix is graded on P1 and P2, not here)", "`[2231] Any idea what might cause this flickering?` (notes 'the first line of the post, as it was written'; the prefix optional in this row, /rubric round 2)", "G1b title text sample (a post)", "—"),
    ("team:music", "music plays only sometimes", ["rules"], 1, "lookup: one notes sentence", "Engineering team (notes 'Engineering team') on the music post's issue", "G1c team sample (a post)", "—"),
    ("label:bar", "android bottom bar invisible", ["rules"], 1, "lookup: one notes sentence", "Bug label (notes 'Bug label') on the bottom bar post's issue", "G1d label sample (a post split over two messages)", "—"),
    ("parent:mega", "mega tile missing a face", ["rules"], 1, "lookup: one notes sentence", "`ENG-2401` parent (notes 'parent ENG-2401') on the mega tile post's issue", "G1e parent sample (a post that opens with a mention)", "—"),
    ("assignee:top hud", "top hud", ["rules"], 1, "lookup: one notes sentence", "no assignee (notes 'no assignee') on the top hud issue", "G1f assignee sample (the shortest line)", "—"),
    ("desc:In chapter selection", "In chapter selection", ["rules"], 1, "lookup: one notes sentence", "empty description (notes 'nothing in the description') on the In chapter selection issue", "G1g description sample (a line that continues on the next one)", "—")]
for fact, key, fs, band, kind, v, grp, dec in SAMPLES_T:
    row(span=S_TICK, oe=O(*fs) + [N["new:" + key]], fact=fact, what=f"one template field on the issue for '{key}'", final=f"the issue for '{key}' carries that field",
        vals=v + " · " + F(bug(key), *fs), phr=("yes — the comment fixes the prefix '[2231]'" if fact.startswith("prefix") else "yes — the notes fix the field"), kind=kind, band=band, dec=dec,
        grp=grp, dup=f"{fact} ×1 (the template volume row P1 is the control)", valid=f"the issue for '{key}' with the field as the notes set it", idle=f"no issue for '{key}' → REJECT",
        cr="(a) a valid run could render the field in another form (team id, label id, key) — any rendering the tools return passes; (b) a wrong run could fill the field from the Zombie Match notes — that doc is another game's (T12)")

# ================================================================== Linear: the state of every new issue (Fix List R8–R28, then the 47 ticked lines)
ACC_ANY = "the issue filed for that line or post is in {}, whatever its title"
for key, band, oes, fs, kind, grp in (
        ("offers has no visuals", 3, ("canvas_threads",), (), "interpretation: the thread reopens and closes again; the tick stands", "direct (a reopened thread)"),
        ("Teams addressable doesn t work", 1, (), (), "lookup: the tick on one canvas line", "direct (an ordinary ticked line)"),
        ("top hud", 1, (), (), "lookup: the tick on one canvas line", "direct (an ordinary ticked line)"),
        ("Streak Fever has overflowing text on its pop up", 1, (), (), "lookup: the tick on one canvas line", "direct (an ordinary ticked line)"),
        ("Win & Collect gives a null ref every time", 3, ("wc",), ("wc",), "interpretation: Win & Collect is disabled, but Fixed comes before Gone (first-fit order)", "direct (the first-fit trap)")):
    row(span=S_TICK, oe=O("canvas", "decide", *oes) + [N["new:" + key]], fact="state:" + key, what=f"the state of the new issue for the ticked line '{key}'", final="that issue is in Done",
        vals=f"`[2231] {line_of(key)}` in Done (ticked; notes 'Fixed: the tick stands') · " + F(bug(key), "rules", *fs), kind=kind, band=band, grp=grp, dup=f"state:{key} ×1",
        valid=f"the issue for '{line_of(key)}' in Done", idle=f"no issue for '{line_of(key)}' in Done → REJECT",
        cr="(a) a valid run could drop a trailing space or render the line with its emoji code — the row names the issue by its line and grades the state only; (b) a wrong run could file it Canceled because the feature changed — the tick stands first (SQL L16 first-fit order)")
row(span=S_TICK, oe=O("canvas_threads", "decide") + [N["new:navigation bar tooltips"]], fact="state:navigation bar tooltips", what="the state of the new issue for the ticked 'navigation bar tooltips' line",
    final="that issue is in Done", vals="`[2231] navigation bar tooltips` in Done (ticked; the thread ends on Vincent's 'the 1 pixel gap is gone' CE156FDFB428/1763845512.559339, SQL L80) · " + F(bug("navigation bar tooltips"), "tooltips"),
    kind="interpretation: the thread's last reply after Brian's 'I'll send another fix'", band=3, grp="direct (a thread that ended on a promised fix until the last reply)", dup="state:tooltips ×1",
    valid="the issue for 'navigation bar tooltips' in Done", idle="no issue for 'navigation bar tooltips' in Done → REJECT",
    cr="(a) a valid run could read Brian's 'I'll send another fix' as open — Vincent's later reply closes it (SQL L80); (b) a wrong run could file it Bugs — fails")
row(span=S_TICK, oe=O("canvas_threads", "tavern", "decide") + [N["new:Tavern buttons lost its frame"]], fact="state:tavern", what="the state of the new issue for the ticked Tavern buttons line", final="that issue is in Bugs",
    vals="`[2231] Tavern buttons lost its frame.` in Bugs (Marcus's DM D05USBTQY1F/1765452012.418229, SQL L58, Dec 11: 'lost their frame again … Brian's fix didn't hold'; the line ends with a mention of Owen Baker) · " + F(bug("Tavern buttons lost its frame"), "tavern"),
    dis="T1 → graded on the state", kind="multi-source: a canvas tick and Brian's fix overturned by a DM in another conversation", band=5, dec="T1", dup="state:tavern ×1 (the sheet Outcome @@P:sheet:tavern@@ and Why @@P:sheet_why:tavern@@ are separate cells with their own fact ids, per the /rubric round-1 Fix List)",
    valid="the Tavern issue in Bugs", idle="no Tavern buttons issue in Bugs → REJECT",
    cr="(a) a valid run could argue the tick and Brian's Nov 20 fix stand — Marcus's Dec 11 DM is later and about this bug (SQL L58); (b) a wrong run could put it in Todo — the notes say Bugs")
row(span=S_TICK, oe=O("shop", "decide") + [N["new:shops from rivertile and memory tile has weird shop"]], fact="state:shop", what="the state of the new issue for the ticked shop icons line", final="that issue is in Bugs",
    vals="`[2231] shops from rivertile and memory tile has weird shop icons (circular shapes entirely)` in Bugs (Brian's reply C09Q4S613CN/1764606918.318209, SQL L66: 'so don't trust that tick') · " + F(bug("shops from rivertile and memory tile has weird shop"), "shop"),
    dis="T2 → graded on the state", kind="multi-source: a tick overturned by a reply under an unrelated post in another channel", band=5, dec="T2", dup="shop ×1",
    valid="the shop icons issue in Bugs", idle="no shop icons issue in Bugs → REJECT",
    cr="(a) a valid run could hold that the tick stands — Brian's Dec 1 reply is later and names these shops (SQL L66); (b) a wrong run could also hold ENG-2432/2433 — a bug on a screen doesn't hold its child (SQL L16)")
for key, rec, ref in (("train level backgrounds are broken", "vr_train", "Vincent CE156FDFB428/1763845212.507119, SQL L72: 'still off … leaving this one open'"),
                      ("When I created a team and quitted it the", "vr_team", "Vincent CE156FDFB428/1763742012.611229, SQL L74: 'the navigation bar still goes after quitting'")):
    row(span=S_TICK, oe=O("canvas_threads", "near_miss", "decide") + [N["new:" + key]], fact="state:" + rec, what=f"the state of the new issue for the unticked line '{key}'", final="that issue is in Bugs",
        vals=f"`[2231] {line_of(key)}` in Bugs ({ref}) · " + F(bug(key), rec, "near_miss"), dis="T11 → a fix attempt in the thread is not the end", kind="interpretation: the thread's last reply against the fix attempt",
        band=3, dec="T11", dup=f"{rec} ×1", valid=f"the issue for '{line_of(key)}' in Bugs", idle=f"no issue for '{line_of(key)}' in Bugs → REJECT",
        cr="(a) a valid run could count the fix attempt as the later record — Vincent's reply is later and says it is not fixed; (b) a wrong run could mark it Covered by a near-miss ticket — the six near-miss comments rule that out (OE 26)")
row(span=S_TICK, oe=O("near_miss", "decide") + [N["new:When I lost a level I got some backend"]], fact="state:backend", what="the state of the new issue for the unticked backend-errors line", final="that issue is in Bugs",
    vals=f"`[2231] {line_of('When I lost a level I got some backend')}` in Bugs (unticked; notes 'stays open unless a later record says it was fixed') · " + F(bug("When I lost a level I got some backend"), "near_miss"),
    kind="interpretation: an unticked line with no closing record, checked against the open tickets", band=3, dec="T11", dup="backend ×1",
    valid="the backend-errors issue in Bugs", idle="no backend-errors issue in Bugs → REJECT",
    cr="(a) a valid run could tie it to ENG-2398 'relogin problems' — Arthur's comment limits that ticket to the restart pop up (SQL L329); (b) a wrong run could cancel it as moot after the economy change — losing a level still exists, only lives went")
for key, rec, ref in (("I found the issue lives are not decreased after", "vr_lives1", "Vincent CE156FDFB428/1763845812.703339, SQL L76"),
                      ("Lives are only decreased after losing twice in a", "vr_lives2", "Vincent CE156FDFB428/1763845872.804449, SQL L78"),
                      ("When I change the character it just adds 1", None, "unticked, no fix")):
    fs = (bug(key), rec, "lives", "econ_builds") if rec else (bug(key), "lives", "econ_builds")
    row(span=S_TICK, oe=O("canvas_threads", "lives", "builds", "decide") + [N["new:" + key]], fact="state:" + key, what=f"the state of the new issue for the lives line '{key}'", final="that issue is Canceled",
        vals=f"`[2231] {line_of(key)}` in Canceled ({ref}; lives removed on the economy line: C09SWTHEMEW/1764659626.614679 and #2299 C05433XK267/1765397569.397939; notes 'Gone … File it as Canceled') · " + F(*fs),
        dis="T10 → graded on the state", kind="multi-source: the line, the economy change in another channel and the build line", band=5, dec="T10", dup=f"gone:{key} ×1" + (" (and the sheet Outcome @@P:sheet:lives1@@, a different cell)" if rec == "vr_lives1" else ""),
        valid=f"the issue for '{line_of(key)}' Canceled", idle=f"no issue for '{line_of(key)}' Canceled → REJECT",
        cr="(a) a valid run could file it Bugs as an open line — Gone comes before Broken and the build has no lives (SQL L16, C05433XK267/1765397569.397939); (b) a wrong run could cancel other lines that mention lives' neighbours — only these three are about lives")
POSTLIT = {"tile dozer window background": "`[2231] the tile dozer game background out of the window, went small`",
           "mega tile missing a face": "`[2231] … he gave me a megatile like this and when i look at the megatile one tile its not visibile …`",
           "flickering": "`[2231] Any idea what might cause this flickering?`",
           "music plays only sometimes": "`[2231] My game started out without music, and suddenly at chapter 2 level 2, music started out of nowhere, intended?`",
           "acid animation delay": "`[2231] Animation is delayed for [PERSON_NAME_1711]'s acid.`",
           "treasure button opens axe arena": "`[2231] After getting to stage 2 if [PERSON_NAME_1711]'s treasure, the button on home screen is bugged`",
           "android bottom bar invisible": "`[2231] Hey … on some Android devices, the bottom bar is not visible`"}
for key, band, fs, oes, kind, ref in (
        ("tile dozer window background", 5, ("window_claim", "pr1913"), ("post_threads", "pr1913"), "multi-source: Marcus's 'fixed it and did a PR' against the PR's state in GitHub", "Bugs (PR #1913 open, not merged, base develop; 'A PR that never made it into that build doesn't count')"),
        ("mega tile missing a face", 3, ("mega", "near_miss"), ("post_threads", "near_miss"), "interpretation: the post's own last reply keeps it open", "Bugs (Marcus C05V5FNLB9V/1764331830.705279, SQL L115: 'still happens on today's build', in the post's thread)"),
        ("flickering", 5, ("flicker", "econ_builds"), ("flicker", "builds"), "multi-source: Robert's reply in another channel and the EconomyChanges build line", "Done (Robert C09Q4S613CN/1766164222.418229, SQL L70; fix listed in #2297)"),
        ("music plays only sometimes", 5, ("music", "econ_builds"), ("brian_dm", "builds"), "multi-source: Brian's DM and the build line, the thread itself ends open", "Done (Brian D07E9PSQB6W/1765206644.602119, SQL L60; URLAudioPlayer fix listed in #2297)"),
        ("acid animation delay", 5, ("music", "econ_builds"), ("brian_dm", "builds"), "multi-source: Brian's DM line in another conversation and the Nathan animation fix in build #2297", "Done (Brian's Dec 8 line 'Nate's acid throw lines up again'; Nathan Animation Fix in #2297)"),
        ("treasure button opens axe arena", 5, ("treasure", "treasure_commit", "merge"), ("post_threads", "treasure_commit", "merge"), "multi-source: the fix in the thread, its commit on develop and the merge into the economy branch", "Done (Brian 'I send the fix'; commit fbe7bdea; develop merged into EconomyChanges 04d3118d)"),
        ("android bottom bar invisible", 5, ("bar", "pr1916"), ("post_threads", "pr1916"), "multi-source: Brian's in-thread close after the camera fix and PR #1916 merged into the economy branch", "Done (Brian C05V5FNLB9V/1767021345.207719, SQL L69; PR #1916 into EconomyChanges)")):
    st = ref.split(" ")[0]
    trap = {"tile dozer window background": "T5"}.get(key, "T13")
    row(span=S_TICK, oe=O(*oes, "decide") + [N["new:" + key]], fact="state:" + key, what=f"the state of the new issue for the '{key}' post", final="that issue is in " + st,
        vals=f"{POSTLIT[key]} in {st} — {ref} · " + F(bug(key), *fs),
        dis=("T5 → graded on the state" if key.startswith("tile") else "—"), kind=kind, band=band, dec=trap, grp="direct (each of the 7 posts is graded)",
        dup=f"post:{key} ×1" + (" (and the sheet Outcome @@P:sheet:window@@, a different cell)" if key.startswith("tile") else ""), valid=f"the {key} issue in {st}", idle=f"no {key} issue in {st} → REJECT",
        cr="(a) a valid run could title it with the post's first sentence only — the row names the issue by its post and grades the state only; (b) a wrong run could decide on the post alone — the deciding record is " + ", ".join(fs))

# the 47 ticked lines whose tick stands (Fix List 'Rows to add'); five are weight 3
DIRECT_DONE = {"offers has no visuals", "Teams addressable doesn t work", "top hud", "Streak Fever has overflowing text on its pop up", "Win & Collect gives a null ref every time"}
W3 = {"level completed text has no outline": (("canvas_threads",), (), "interpretation: the thread reopens after the Unity 6 update and closes once the plugin update 'looks good'; the tick stands", "a reopened thread"),
      "life balance timer in top HUD": (("lives",), ("lives",), "interpretation: lives are gone from the build, but Fixed comes before Gone (first-fit order)", "the first-fit trap"),
      "Win & Collect Pop Up": (("wc",), ("wc",), "interpretation: Win & Collect is disabled in the build, but Fixed comes before Gone (first-fit order)", "the first-fit trap"),
      "initial reward of infinite lives beneath the overlay": (("lives",), ("lives",), "interpretation: lives are gone from the build, but Fixed comes before Gone (first-fit order)", "the first-fit trap"),
      "chapter 2 saga map has a weird artifact": (("canvas_threads",), (), "interpretation: the thread reopens ('not done') and closes when the pixels-per-unit fix is pushed; the tick stands", "a reopened thread")}
TICK47 = [k for k, v in TRUTH.items() if v.get("Why") == "the tick stands" and "fixed" in v.get("groups", []) and k not in DIRECT_DONE]
assert len(TICK47) == 47 and set(W3) <= set(TICK47), (len(TICK47), set(W3) - set(TICK47))
for key in TICK47:
    oes, fs, kind, why = W3.get(key, ((), (), "lookup: the tick on one canvas line stands", "an ordinary ticked line"))
    row(span=S_TICK, oe=O("canvas", "decide", *oes) + [N["new:" + key]], fact="state:" + key, what=f"the state of the new issue for the ticked line '{key}'", final="that issue is in Done",
        vals=f"`[2231] {line_of(key)}` in Done (ticked CE156FDFB428/{ts_of(key)}; notes 'Fixed: the tick stands') · " + F(bug(key), "rules", *fs), kind=kind, band=3 if key in W3 else 1,
        grp=f"direct ({why})", dup=f"state:{key} ×1" + (" (the sheet Ticket @@P:sheet_ticket:sides@@, Outcome @@P:sheet_outcome:sides@@ and Why @@P:sheet_why:sides@@ are separate cells with their own fact ids)" if key == "sides of event icons" else ""),
        valid=f"the issue for '{line_of(key)}' in Done", idle=f"no issue for '{line_of(key)}' in Done → REJECT",
        cr="(a) a valid run could title the issue with the line's emoji codes or without them — the row names the issue by its line and grades the state only; (b) a wrong run could file it Canceled or Bugs on a feature change or an old reply — the tick stands first in the notes' order (SQL L16)")

# Covered (locked: the reviewed text is unchanged)
row(span=S_TICK, oe=O("apple", "eng2073", "decide", "note:ENG-2073"), fact="covered:apple", what="the canvas wording of the Apple sync line added on ENG-2073", final="a new comment on ENG-2073 carrying the Apple sync line's words",
    vals="`ENG-2073` comment with 'In general, I cannot sync and sign in with my Apple account' (Vincent's mail owen.baker@harmonygames.co/1849333980856689601, SQL L281: 'same sync problem as ENG-2073, no need for anything new'; ENG-2073 Bugs) · " + F("apple", "eng2073"),
    dis="T3 → graded on the note", kind="multi-source: a mail in Owen's inbox ties a canvas line to a Linear ticket", band=5, dec="T3", dup="covered:apple ×1 (the sheet Ticket @@P:sheet:apple@@ and Outcome @@P:sheet_outcome:apple@@ are separate cells with their own fact ids, per the /rubric round-1 Fix List)",
    valid="a comment on ENG-2073 quoting the Apple line", idle="no new comment on ENG-2073 with the Apple line → REJECT",
    cr="(a) a valid run could paraphrase the line — the notes ask for 'the canvas wording', so the comment must carry the line's words; (b) a wrong run could file a new ticket too — the count row P1 catches it")
row(span=S_TICK, oe=O("signin", "decide", "note:ENG-2363"), fact="covered:signin", what="the canvas wording of the manual sign-in line added on ENG-2363", final="a new comment on ENG-2363 carrying the manual sign-in line's words",
    vals="`ENG-2363` comment with 'On android, manual sign-in has an issue after the sign-in' (Vincent's comment SQL L314: 'same thing as here'; ENG-2363 In Progress) · " + F("signin"),
    dis="T4 → graded on the note", kind="multi-source: a Linear comment on another ticket ties a canvas line", band=5, dec="T4", dup="covered:signin ×1 (the sheet Ticket @@P:sheet:signin@@ is a separate cell)",
    valid="a comment on ENG-2363 quoting the manual sign-in line", idle="no new comment on ENG-2363 with the sign-in line → REJECT",
    cr="(a) a valid run could file a new ticket because ENG-2363 is about the splash screen — Vincent's comment says it is the same thing; (b) a wrong run could note it on ENG-2280 (old data, iOS) — Arthur's comment limits that ticket (SQL L325)")

# ================================================================== Linear: the UI tree
row(span=S_TREE, oe=O("tree", "decide_kids") + list(range(N["move:ENG-2410"], N["move:ENG-2435"] + 1)), fact="moves_count", what="how many UI children the Agent moves to Done",
    final="exactly 14 of the 28 children are moved to Done in the run", vals="14 moves (19 open − 5 held: ENG-2424, ENG-2426, ENG-2428, ENG-2434, ENG-2437) · " + F("tree", "wc", "inline_td", "inline_axe", "season", "gift"),
    dis="T6, T7, T8, T9 → graded as the exact scope of the move", kind="multi-source: each hold rests on a different record (group DM, PR reviews, Linear comment, DM)", band=5,
    dec="T6, T7, T8, T9", grp="G4 moves (volume)", dup="moves_count ×2 (this and the reply number @@P:reply_done@@)",
    valid="14 children moved to Done", idle="no child moved → REJECT",
    cr="(a) a valid run could also move a held child whose PR merged — the tree rule holds it (SQL L16); (b) a wrong run could move the right number with the wrong members — the sample and hold rows catch which")
for k, why, band in (("ENG-2417", "Settings: an ordinary PR-state child", 1), ("ENG-2418", "Level win", 1), ("ENG-2433", "Memory Tile: an edge, the shop icons regression is on its screen", 3),
                     ("ENG-2432", "River Tile: an edge, the shop icons regression is on its screen", 3), ("ENG-2410", "Shop: the shop icons regression against a Validation-state child", 3)):
    row(span=S_TREE, oe=O("tree", "kid_notes", "decide_kids", "move:" + k) + (O("shop") if band == 3 else []), fact="move:" + k, what=f"the state of {k} after the run", final=f"{k} moved to Done",
        vals=f"`{k}` → Done (open, no hold; tree rule SQL L16" + ("; Brian's shop-icon regression C09Q4S613CN/1764606918.318209 does not hold it: 'A bug on a screen doesn't hold its child'" if band == 3 else "") + ") · " + F("kid:" + k, *(("shop",) if band == 3 else ())),
        kind=("interpretation: Brian's shop-icon regression weighed against 'a bug on a screen doesn't hold its child'" if band == 3 else "lookup: an open child with no record holding it"), band=band,
        grp=f"G4 moves sample ({why})", dup=f"move:{k} ×1", valid=f"{k} in Done", idle=f"{k} not moved to Done → REJECT",
        cr="(a) a valid run could keep it open because a bug sits on its screen — 'A bug on a screen doesn't hold its child' (SQL L16); (b) a wrong run could close it Canceled — the rule says Done")
for k, fs, kind, trap in (
        ("ENG-2434", ("inline_td", "popups_dm"), "multi-source: Arthur's inline review on a merged PR and Brian's later DM", "T6"),
        ("ENG-2426", ("inline_axe", "popups_dm"), "multi-source: Arthur's inline review on a merged PR and Brian's later DM", "T6"),
        ("ENG-2424", ("wc",), "multi-source: the economy-line group DM's 'event disabled' against the child's merged work", "T9"),
        ("ENG-2428", ("season",), "multi-source: Oliver's comment on the child against its merged work and the tracker's status", "T7"),
        ("ENG-2437", ("gift", "brian_nov19"), "multi-source: Brian's later DM line over his earlier plan and the tracker's status", "T8")):
    row(span=S_LINE, oe=O("decide_kids", "line:" + k) + ([N["inline"], N["brian_dm"]] if trap == "T6" else [N["wc"]] if trap == "T9" else [N["kid_notes"]] if trap == "T7" else [N["brian_dm"]]), fact="hold:" + k,
        what=f"the line the Agent leaves on the held child {k}", final=f"a new comment on {k} saying the ticket stays open",
        vals=f"`{k}` comment saying it stays open (tree rule SQL L16 'Then it stays where it is') · " + F("kid:" + k, *fs), dis=f"{trap} → graded on the written line, not a leave-alone", kind=kind, band=5, dec=trap,
        grp="direct (the five holds are the tree rule's exceptions)", dup=f"hold:{k} ×1 (the moves count @@P:moves_count@@ and the build line are separate facts)",
        valid=f"a comment on {k}: 'Stays open; landed in public build 0.3.310 without the rest of its UI work'", idle=f"no new comment on {k} → REJECT",
        cr=f"(a) a valid run could say 'held', 'not done' or 'stays where it is' — the title's meaning is the ticket staying open, in any wording; (b) a wrong run could write 'landed in 0.3.310, Done' — that calls the held ticket Done and fails")
NAMES = {"ENG-2410": "Shop UI Optimization", "ENG-2411": "Character Section UI Optimization", "ENG-2412": "Saga map UI Optimization", "ENG-2413": "Teams UI Optimization",
         "ENG-2414": "Leaderboard UI Optimization", "ENG-2415": "Quest UI Optimization", "ENG-2416": "Profile Page UI Optimization", "ENG-2417": "Settings UI Optimization",
         "ENG-2418": "Level - win UI Optimization", "ENG-2419": "Level Lose - Out-of-moves Screens UI Optimization", "ENG-2420": "Chapter Section UI Optimization",
         "ENG-2421": "Tavern UI Optimization", "ENG-2422": "Pre-game Panel UI Optimization", "ENG-2423": "Transition Screens", "ENG-2424": "Collect&win - Magical Wings",
         "ENG-2425": "Nathan's Treasure - UI Optimization", "ENG-2426": "Axe Arena", "ENG-2427": "River Rush - UI Optimization", "ENG-2428": "Season Pass",
         "ENG-2429": "Remove Ad - UI Optimization", "ENG-2430": "Offers - UI Optimization", "ENG-2431": "Rate-us Pop-ups - UI Optimization", "ENG-2432": "River Tile - UI Optimization",
         "ENG-2433": "Memory Tile - UI Optimization", "ENG-2434": "Tile Dozer", "ENG-2435": "Lucky Drop - UI Optimization", "ENG-2437": "Daily Gift"}
HELD = ["ENG-2434", "ENG-2426", "ENG-2424", "ENG-2428", "ENG-2437"]
OTHER22 = ["ENG-2410", "ENG-2411", "ENG-2412", "ENG-2413", "ENG-2414", "ENG-2415", "ENG-2416", "ENG-2417", "ENG-2418", "ENG-2419", "ENG-2420", "ENG-2421", "ENG-2422",
           "ENG-2423", "ENG-2425", "ENG-2427", "ENG-2429", "ENG-2430", "ENG-2431", "ENG-2432", "ENG-2433", "ENG-2435"]
for k in HELD + OTHER22:
    st = TRUTH[k]["Why"]
    row(span=S_LINE, oe=O("closing", "line:" + k), fact="line:" + k, what=f"the build named in the line on {k}", final=f"a new comment on {k} naming 0.3.310",
        vals=f"`0.3.310` in the comment on `{k}` ({'held' if k in HELD else st}; Brian's closing rule 690b29bc3c7d2e51b0f86a47 'every one gets a note naming the current public build'; notes 'the Android build players have, 0.3.310', 'Done or not') · " + F("kid:" + k, "closing", "rules"),
        dis="T12 → the ZM card's 'no note' is another game's", kind="interpretation: Brian's closing rule and the notes' build number applied to one child", band=3, dec="T12",
        grp="direct (one row per child)", dup=f"line:{k} ×1", valid=f"{k}: '… landed in Android 0.3.310'", idle=f"no new comment on {k} naming 0.3.310 → REJECT",
        cr="(a) a valid run could write 'build 0.3.310' or 'Android 0.3.310' — any form with 0.3.310 passes; (b) a wrong run could name develop's build or 0.3.305 from the Feb 10 channel line — the notes fix 0.3.310")
row(span=S_LINE, oe=O("closing", "line:ENG-2409"), fact="line:ENG-2409", what="the line on an already-Done child", final="a new comment on ENG-2409 naming 0.3.310",
    vals="`ENG-2409` comment naming `0.3.310` (already Done; 'applies to the line on every child, Done or not') · " + F("kid:ENG-2409", "closing"), kind="interpretation: Brian's closing rule and the notes' build number applied to a child Done before the run", band=3,
    grp="direct (a child already Done before the run)", dup="line:ENG-2409 ×1", valid="ENG-2409: 'Done; landed in Android 0.3.310'", idle="no new comment on ENG-2409 → REJECT",
    cr="(a) a valid run could skip children already Done — the notes say 'Done or not'; (b) a wrong run could name develop's build — the notes fix 0.3.310")

# ================================================================== the sheet
row(span=S_SHEET, oe=O("folder", "sheet_create", "sheet_move"), fact="sheet_folder", what="where the sheet lives", final="a new Google Sheet whose parent is the 'DD bug carry-over' folder",
    vals="`d_9b41e7c2a05d36f8e1c7a4` 'DD bug carry-over' (SQL L3) · " + F("folder"), phr="yes — 'my DD bug carry-over folder'", kind="lookup: the folder the prompt names", band=1, dup="sheet_folder ×1",
    valid="a sheet created in or moved into d_9b41e7c2a05d36f8e1c7a4", idle="no sheet in the DD bug carry-over folder → REJECT",
    cr="(a) a valid run could create it directly in the folder — any route ending with that parent passes; (b) a wrong run could leave it in Owen's root — fails")
row(span=S_SHEET, oe=O("rules", "sheet_rows"), fact="sheet_columns", what="the sheet's columns", final="a header row with the columns Bug, Outcome, Ticket and Why",
    vals="Bug Outcome Ticket Why (notes SQL L16 'Sheet columns: Bug, Outcome, Ticket, Why.'; order free) · " + F("rules"), phr="yes — the notes name the four columns", kind="lookup: one notes sentence", band=1, dup="sheet_columns ×1",
    valid="header Bug / Outcome / Ticket / Why", idle="no sheet with a Bug, Outcome, Ticket, Why header → REJECT",
    cr="(a) a valid run could order them differently or add a fifth column — the row checks the four are present; (b) a wrong run could use 'Status' for Outcome — fails")
row(span=S_SHEET, oe=O("canvas", "posts", "decide", "sheet_rows"), fact="sheet_rows", what="how many bug rows the sheet holds", final="exactly 70 bug rows under the header",
    vals="70 rows (63 lines + 7 posts; notes 'One Linear record per canvas line and one per bug posted after it') · " + F("totals", "canvas", "posts"),
    dis="T13 → deleted-line comments, follow-ups, the QA-doc post and the design question get no row", kind="multi-source: the full audit of the canvas channel and the bug channel against the notes' scope tests", band=5, dec="T13",
    grp="G7–G9 sheet cells (volume)", dup="sheet_rows ×1", valid="70 rows", idle="no sheet rows → REJECT",
    cr="(a) a valid run could add a totals row — the row counts bug rows; (b) a wrong run could list the 6 deleted-line comments — 76 rows fails")
row(span=S_SHEET, oe=O("sheet_rows", "new:sides of event icons"), fact="sheet_ticket:sides", grp="G8 Ticket cells sample (an ordinary Fixed line)", what="the Ticket cell of the sides of event icons row",
    final="the key of the issue the run filed for that line", vals="the new issue's ENG key (assigned at creation, ENG-2438 onward) in the 'sides of event icons' row · " + F(bug("sides of event icons"), "rules"),
    kind="lookup: the key of the run's own issue for one line", band=1, dup="sheet_ticket:sides ×1",
    valid="row 'sides of event icons' Ticket ENG-24xx (the run's issue)", idle="no 'sides of event icons' row with a Ticket key → REJECT",
    cr="(a) a valid run could put the issue URL — a URL carrying the key passes; (b) a wrong run could leave Ticket blank for Fixed items — fails")
for fact, key, out, fs, trap, kind, oes in (
        ("sheet:tavern", "Tavern buttons lost its frame", "Broken (or Bugs)", ("tavern",), "T1", "multi-source: the canvas tick and Brian's fix overturned by Marcus's later DM", ("tavern",)),
        ("sheet:apple", "In general I cannot sync and sign in with", "Ticket ENG-2073", ("apple", "eng2073"), "T3", "multi-source: a mail in Owen's inbox ties the line to an open Linear ticket", ("apple",)),
        ("sheet:signin", "On android manual sign-in has an issue after the", "Ticket ENG-2363", ("signin",), "T4", "multi-source: a Linear comment on another ticket ties the line to it", ("signin",)),
        ("sheet:window", "tile dozer window background", "Broken (or Bugs)", ("window_claim", "pr1913"), "T5", "multi-source: Marcus's 'fixed it and did a PR' against PR #1913 still open in GitHub", ("pr1913",)),
        ("sheet:lives1", "I found the issue lives are not decreased after", "Gone (or Canceled)", ("vr_lives1", "lives", "econ_builds"), "T10", "multi-source: Vincent's reply, Leonard's lives removal and build #2299 on the economy line", ("lives", "builds"))):
    grp = "G8 Ticket cells sample (edge: Covered)" if out.startswith("Ticket") else "G7 Outcome cells sample (edge: " + {"T1": "a tick overturned", "T5": "an unmerged PR", "T10": "Gone"}[trap] + ")"
    row(span=S_SHEET, oe=O(*oes, "decide", "sheet_rows"), fact=fact, grp=grp, what=f"the sheet's {'Ticket' if out.startswith('Ticket') else 'Outcome'} for the '{key}' row", final=f"{out}",
        vals=f"'{key}' row {out} · " + F(bug(key), *fs), dis=f"{trap} → graded on the row", kind=kind, band=5, dec=trap, dup=f"{fact} ×1 (its Linear write is a separate artifact)",
        valid=f"row '{key}…' {out}", idle=f"no '{key}' row with {out} → REJECT",
        cr="(a) a valid run could write the Linear state (Bugs, Canceled) or the key with '(covered)' — accepted; (b) a wrong run could write the tick's reading (Fixed) or a new issue's key — fails")
for fact, key, band, val, fs, kind, grp, trap in (
        ("sheet_outcome:sides", "sides of event icons", 1, "Outcome Fixed (or Done)", ("rules",), "lookup: the tick on one canvas line stands", "G7 Outcome cells sample (an ordinary Fixed line)", "—"),
        ("sheet_outcome:apple", "In general I cannot sync and sign in with", 5, "Outcome Covered", ("apple", "eng2073"), "multi-source: a mail in Owen's inbox ties the line to an open Linear ticket", "G7 Outcome cells sample (edge: Covered)", "T3"),
        ("sheet_why:tavern", "Tavern buttons lost its frame", 5, "Why: the buttons lost their frame again after Brian's fix", ("tavern",), "multi-source: Marcus's later DM overturns the canvas tick and Brian's fix", "G9 Why cells sample (edge: a tick overturned)", "T1"),
        ("sheet_why:sides", "sides of event icons", 1, "Why: the line is ticked on the canvas", ("rules",), "lookup: the tick on one canvas line", "G9 Why cells sample (an ordinary Fixed line)", "—")):
    row(span=S_SHEET, oe=O("decide", "sheet_rows") + ([N["tavern"]] if "tavern" in fact else [N["apple"]] if "apple" in fact else [N["canvas"]]), fact=fact, grp=grp, what=f"the sheet's {val.split(':')[0].split(' ')[0]} cell for the '{key}' row",
        final=val, vals=f"'{key}' row {val} · " + F(bug(key), *fs), dis=(f"{trap} → graded on the row" if trap != "—" else "—"), kind=kind, band=band, dec=trap,
        dup=f"{fact} ×1 (a different cell of the same row)", valid=f"row '{key}…' {val}", idle=f"no '{key}' row with that cell → REJECT",
        cr="(a) a valid run could word the Why its own way or write the state name — any wording with that meaning passes; (b) a wrong run could leave the cell blank or give the tick's reading for an overturned line — fails")

# ================================================================== sharing
for e, who in (("arthur.blake@harmonygames.co", "Arthur Blake"), ("robert@harmonygames.co", "Robert"), ("oliver.brooks@harmonygames.co", "Oliver Brooks")):
    row(span=S_SHARE, oe=O("review", "share:" + e), fact="share:" + e, what=f"the sheet shared with {who}", final=f"{e} holds a permission on the sheet",
        vals=f"{e} (attendee of 'DD bug review' `evt_6e2c91d4b07f3a58c1d2e4`, SQL L309; any role) · " + F("review", "emails"), kind="lookup: one calendar event's attendees", band=1,
        dup=f"share:{who} ×1", valid=f"{e} as reader, commenter or writer", idle=f"the sheet is not shared with {e} → REJECT",
        cr="(a) a valid run could share with the whole domain — the row asks for this person's access, which a domain share also gives; (b) a wrong run could share with Brian (the UI owner) instead — fails for the missing person")

# ================================================================== the reply
row(span=S_REPLY, oe=O("hub", "reply"), fact="reply_thread", what="where the reply goes", final="a reply in the thread of Arthur's Feb 12 DM D05S1S2AB5M/1770937805.214409",
    vals="thread `1770937805.214409` in D05S1S2AB5M (prompt 'reply to him in that DM thread') · " + F("hub"), phr="yes — 'in that DM thread'", kind="lookup: the thread the prompt names", band=1, dup="reply_thread ×1",
    valid="a threaded reply under 1770937805.214409", idle="no reply in Arthur's DM thread → REJECT",
    cr="(a) a valid run could also post a top-level line in the DM — the row asks for the threaded reply, which must exist; (b) a wrong run could reply only top-level — the prompt says 'in that DM thread', so it fails")
for fact, lit, band, fs, dec, kind, ex in (
        ("reply_broken", "9 still broken", 5, ("totals", "rules", "tavern", "shop", "apple"), "T1, T2, T3", "multi-source: the count joins every decision and the report-back rule", "7 Broken + 2 Covered; notes 'When you report back, Covered ones count as still broken'"),
        ("reply_new", "68 new tickets", 5, ("totals", "apple", "signin"), "T3, T4", "multi-source: the count depends on the two Covered ties", "the number filed in the run"),
        ("reply_done", "23 of 28 children Done", 5, ("totals", "tree", "inline_td", "inline_axe", "season", "gift", "wc"), "T6, T7, T8, T9", "multi-source: the count depends on five holds from four sources", "9 already Done + 14 moved")):
    row(span=S_REPLY, oe=O("hub", "decide", "decide_kids", "reply"), fact=fact, what=f"the number in the reply to Arthur: {lit}", final=f"the reply in Arthur's DM thread states {lit}",
        vals=f"{lit} ({ex}; thread `1770937805.214409`) · " + F(*fs), dis=f"{dec} → graded by the number", kind=kind, band=band, dec=dec, dup=f"{fact} ×1 (its Linear/sheet counterpart is a separate artifact)",
        valid=f"'… {lit} …' in the reply", idle="no reply in Arthur's DM thread → REJECT",
        cr="(a) a valid run could state the number in words — any rendering of the number passes; (b) a wrong run could give 7 still broken, leaving out the Covered lines — the notes count them as still broken, so it fails")
row(span=S_THEN, oe=O("reply"), fact="reply_after_writes", cat="Process candidate → C", what="the reply comes after the Linear and sheet writes", final="the reply is posted after the run's last ticket, comment, move, sheet and share write",
    vals="Then (prompt: 'Then reply to him') · " + F("hub"), phr="yes — 'Then reply'", kind="lookup: the prompt orders the reply last ('Then reply'); the run's write order shows it", band=1, dup="reply_after_writes ×1",
    valid="the reply is the run's last write", idle="no reply in the run → REJECT",
    cr="(a) a valid run could post a progress note first and the numbers last — the row grades the reply with the numbers; (b) a wrong run could reply first and file later — fails")

PN = {r["fact"]: r["p"] for r in R}
assert len(PN) == len(R) == 138, (len(PN), len(R))
for r in R:
    for k, v in list(r.items()):
        if isinstance(v, str):
            r[k] = re.sub(r"@@P:(.+?)@@", lambda m: PN[m.group(1)], v)
