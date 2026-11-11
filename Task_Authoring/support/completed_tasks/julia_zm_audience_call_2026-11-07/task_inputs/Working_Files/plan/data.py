"""Single data module for the injection. All truth values and all seeded text live here.

Ids, dates, ratings and groups come from planned_records in 01_Hardness_Manifest.draft.json and are never
retyped; seeded wording sits below. Emitters read this module only.
"""
import hashlib
import json
import pathlib
from datetime import datetime, timedelta, timezone

HERE = pathlib.Path(__file__).resolve().parent
MANIFEST = json.loads((HERE.parent / "01_Hardness_Manifest.draft.json").read_text(encoding="utf8"))
PR = MANIFEST["planned_records"]
SESSIONS = PR["sessions"]
FORMS = {f["form"]: f for f in PR["forms"]}
KPI_ROWS = json.loads((HERE / "kpi_rows.json").read_text(encoding="utf8"))

# The brief forbids a reply under a base message with no thread. The note and Vincent's post have none,
# so these five records are top-level posts with the design's ts and row id. True restores the design.
THREADLESS_ROOT_REPLIES = False

CH_ZD, CH_ZM, CH_PRS = "C090N54TG79", "C0880U9751A", "C093LEZGF6J"
NOTE_TS, VINCENT_POST_TS = "1758517286.431379", "1759165414.829399"
PR_ID = "harmonygames-Games/match3d#476"
PR_NUM_URL = "https://github.com/harmonygames-Games/match3d/pull/476"
BOARD, BOARD_SHORT, BACKLOG = "6851a6569f3bf818760632ab", "HSqnngwQ", "68c451221ebabaf255a7d16b"
TEAM = "team_ZOM"
WORKBOOK, KPI_SHEET = PR["workbook"], PR["kpi_sheet"]
WORKBOOK_TITLE, KPI_TITLE = "ZM audience sessions", "ZM KPI snapshot"
LOG_NOTE_TITLE = "ZM sessions log note"


class P:
    def __init__(self, name, email, slack, linear, root):
        self.name, self.email, self.slack, self.linear, self.root = name, email, slack, linear, root

    @property
    def addr(self):
        return f"{self.name} <{self.email}>"


PEOPLE = {p.name: p for p in [
    P("Julia Lawson", "julia.lawson@harmonygames.co", "EMPLOYEE_0005_SLACK_ID", "usr_8140f09bf9f1b94c", "d_8140f09bf9f1b94cb8ee2d"),
    P("Leonard Hayes", "leonard.hayes@harmonygames.co", "EMPLOYEE_0038_SLACK_ID", "usr_63fffeb4fab5233e", "d_63fffeb4fab5233ed5bb73"),
    P("Robert", "robert@harmonygames.co", "EMPLOYEE_0016_SLACK_ID", "usr_Robert", "d_9f7ba94f7526d54d8482ba"),
    P("Arthur Blake", "arthur.blake@harmonygames.co", "EMPLOYEE_0025_SLACK_ID", "usr_cc3e90160f490686", "d_cc3e90160f490686039986"),
    P("Brian Foster", "brian.foster@harmonygames.co", "EMPLOYEE_0026_SLACK_ID", "usr_fc22d5941b2aeb5c", "d_fc22d5941b2aeb5c03ad32"),
    P("Vincent Parker", "vincent.parker@harmonygames.co", "EMPLOYEE_0012_SLACK_ID", "usr_65c76e0b87aa7e9b", "d_65c76e0b87aa7e9b84d1df"),
    P("Oliver Brooks", "oliver.brooks@harmonygames.co", "EMPLOYEE_0003_SLACK_ID", "usr_bdf01b53c6a92c5e", "d_bdf01b53c6a92c5e167c65"),
    P("Claire Morgan", "claire.morgan@harmonygames.co", "EMPLOYEE_0009_SLACK_ID", "usr_7fe31e7ec8199618", "d_7fe31e7ec81996189e1f14"),
    P("Marcus Bennett", "marcus.bennett@harmonygames.co", "EMPLOYEE_0002_SLACK_ID", "usr_c77c50cc15c5342d", "d_c77c50cc15c5342d638ebb"),
    P("Martin Walsh", "martin.walsh@harmonygames.co", "EMPLOYEE_0033_SLACK_ID", "usr_51f5f16d46e8cf55", "d_51f5f16d46e8cf55f5ee33"),
    P("Owen Baker", "owen.baker@harmonygames.co", "EMPLOYEE_0021_SLACK_ID", "usr_4e13bd40cc73d0fc", "d_4e13bd40cc73d0fc76f87c"),
    P("Samuel Turner", "samuel.turner@harmonygames.co", "EMPLOYEE_0004_SLACK_ID", "usr_caafeec2804b3a67", "d_caafeec2804b3a67ce46aa"),
    P("Calvin Price", "calvin.price@harmonygames.co", "EMPLOYEE_0006_SLACK_ID", "usr_49b9dfa5208d400d", "d_49b9dfa5208d400d9b3937"),
    P("Douglas", "douglas@harmonygames.co", "EMPLOYEE_0031_SLACK_ID", "usr_cd7849ec043ab3da", "d_cd7849ec043ab3da107f8c"),
]}
JULIA, LEONARD, ROBERT, ARTHUR = (PEOPLE[n] for n in ("Julia Lawson", "Leonard Hayes", "Robert", "Arthur Blake"))
BRIAN, VINCENT, CLAIRE = (PEOPLE[n] for n in ("Brian Foster", "Vincent Parker", "Claire Morgan"))
TRELLO_JULIA = "793af7ca6940bf18eb516c75"
GH_ARTHUR, GH_CODERABBIT = "EMPLOYEE_0025_GITHUB_USERNAME", "PERSON_6026_GITHUB_USERNAME"


def row_id(channel, ts):
    return hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]


def hexid(seed, n):
    return hashlib.sha256(seed.encode()).hexdigest()[:n]


def parse(ts):
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def plus(ts, seconds):
    return iso(parse(ts) + timedelta(seconds=seconds))


def jitter(seed, lo, hi):
    return lo + int(hexid(seed, 8), 16) % (hi - lo + 1)


def ts_iso(ts):
    sec, frac = ts.split(".")
    return datetime.fromtimestamp(int(sec), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S") + "." + frac + "Z"


def unix(ts):
    return int(parse(ts).timestamp())


def day(date):
    return datetime.strptime(date, "%Y-%m-%d").strftime("%a %b %-d") if False else \
        datetime.strptime(date, "%Y-%m-%d").strftime("%a %b ") + str(int(date[-2:]))


# Delegation quotes changed by coordinator decision: manifest text -> text the ask now carries.
QUOTE_CHANGES = {
    "the rules we set under my note still stand": "the rules I posted in the channel after my note still stand",
    "read the panel the way I set out when you asked who those players were":
        "read the panel the way I set out when Robert asked who those players were",
    "retention the way Robert set it under Vincent's post": "retention the way Robert set it in the channel after Vincent's post",
    "limits on a pass sit in review on the PR for the branch the job ran on":
        "Arthur Blake owns the Vision Bot job and says what a pass does and doesn't cover",
}

# ---------- Slack ----------
R1Q_TEXT = ("<@EMPLOYEE_0038_SLACK_ID> quick one on your note. \"25–45 casual and/or RPG gamer "
            "friends\", is that 25 to 45 people or 25 to 45 years old?")
R1A_TEXT = "<@EMPLOYEE_0005_SLACK_ID> age. 25–45 years old, not a headcount"
R2B_TEXT = ("<@EMPLOYEE_0005_SLACK_ID> <@EMPLOYEE_0016_SLACK_ID> on the feedback note, I wrote up the device and "
            "build side in a doc so we all read the friend sessions the same way: ZM session stability gate. "
            "shared it with you")
R3_TEXT = ("One more for the feedback note: game-industry people don’t count, and that goes for sessions already run "
           "too. Anyone who works in games plays it "
           "like we do, so that’s not the honest reaction I asked for")
R4_TEXT = ("for the panel it’s stars per player, one "
           "number each. if a rating is void it comes out of both the sum and the count, so you average what’s left")
R5_TEXT = ("On Vincent's retention post above, when we quote ZM retention let's use install-weighted D7, not a "
           "simple mean of the cohorts. Mature cohorts only, meaning cohorts that have a D14 figure, both "
           "platforms pooled. USER_COHORT_RETENTION has what you need")
R0_TEXT = ("hey all, passing this on from Leonard's note in <#C090N54TG79>: everyone should get a few friends to "
           "try ZM: 25–45 year olds, casual and/or RPG gamers, not kids. No coaching, just observe and collect honest "
           "reactions. If you run any, write one notes doc per session with their age, how you know them, the build, "
           "casual or RPG and their stars, and share it with me. Then send me a short mail with host, day, how many "
           "sessions and whether there was any coaching, so I can log them")
# Julia's question in her Turkish DM with Brian, just before his line (m7).
K4_Q_TS = "1758658884.207315"
K4_Q_TEXT = "paylaştığın notlara bakıyorum, Kadıköy ekibi kim ya? nereden tanıyorsun onları"
K4_TEXT = ("ha pardon söylemeyi unutmuşum, Kadıköy ekibi komple oyun sektöründen, hepsi mobil oyun "
           "şirketlerinde çalışıyor")
K5_TEXT = ("on watching people play it: careful with android 1943, the one that’s been passed around. it never "
           "went through a store, so anyone on it isn’t seeing what a player gets")
F_TEXT = ("Different topic while I'm here, on the friend sessions. If one gets dropped for a technical reason, "
          "device or build, put a re-run note on it so the observer runs it again. Dropped for anything else, "
          "no re-run, it just gets closed")
ASK_TEXT = (
    "<@EMPLOYEE_0005_SLACK_ID> I want to settle the cards earlier change from Monday on what players told us, "
    "not on our gut. the friend sessions are in your workbook now, so give me one audience call from them: "
    "casual, RPG or no clear lead. casual lead means we hold the change. RPG lead means we keep it. no clear lead, "
    "we keep it\n\n"
    "the rules I posted in the channel after my note still stand, and how a session gets its audience label and how the lead is "
    "read is in the audience read criteria. close the tickets the way your log note says. Robert already told you "
    "how not-counted sessions get handled\n\n"
    "what the memo holds is on the roadmap card. for context use the panel results I forwarded you, and read the "
    "panel the way I set out when Robert asked who those players were, plus retention the way Robert set it in "
    "the channel after Vincent's post\n\n"
    "reply here with keep or hold, and tell <@EMPLOYEE_0026_SLACK_ID> in this channel whether the tutorial and "
    "level order work goes on. this is about the current game only, iterate or pivot is a later call")

# (key, channel, ts, row, author, text, root_ts or None)
_under_note = NOTE_TS if THREADLESS_ROOT_REPLIES else None
_under_vincent = VINCENT_POST_TS if THREADLESS_ROOT_REPLIES else None
SLACK_ROWS = [
    ("R1_question", CH_ZD, PR["R1_question"]["ts"], PR["R1_question"]["row"], JULIA, R1Q_TEXT, _under_note),
    ("R1_answer", CH_ZD, PR["R1_answer"]["ts"], PR["R1_answer"]["row"], LEONARD, R1A_TEXT, _under_note),
    ("R0_relay", CH_ZM, PR["R0_relay"]["ts"], PR["R0_relay"]["row"], JULIA, R0_TEXT, None),
    ("K4_question", PR["K4_line"]["channel"], K4_Q_TS, row_id(PR["K4_line"]["channel"], K4_Q_TS), JULIA, K4_Q_TEXT, None),
    ("K4_line", PR["K4_line"]["channel"], PR["K4_line"]["ts"], PR["K4_line"]["row"], BRIAN, K4_TEXT, None),
    ("R2b_pointer", CH_ZD, PR["R2b_pointer"]["ts"], PR["R2b_pointer"]["row"], LEONARD, R2B_TEXT, _under_note),
    ("R4_panel_definition", CH_ZD, PR["R4_panel_definition"]["ts"], PR["R4_panel_definition"]["row"], LEONARD,
     R4_TEXT, PR["R4_panel_definition"]["root"]),
    ("R3_industry_rule", CH_ZD, PR["R3_industry_rule"]["ts"], PR["R3_industry_rule"]["row"], LEONARD, R3_TEXT, _under_note),
    ("K5_reply", CH_ZD, PR["K5_reply"]["ts"], PR["K5_reply"]["row"], LEONARD, K5_TEXT, PR["K5_reply"]["root"]),
    ("F_reply", PR["F_reply"]["channel"], PR["F_reply"]["ts"], PR["F_reply"]["row"], ROBERT, F_TEXT, PR["F_reply"]["root"]),
    ("R5_retention_rule", CH_ZD, PR["R5_retention_rule"]["ts"], PR["R5_retention_rule"]["row"], ROBERT, R5_TEXT, _under_vincent),
    ("ask", CH_ZD, PR["ask"]["ts"], PR["ask"]["row"], LEONARD, ASK_TEXT, None),
]

# Base roots whose counters change: (channel, ts, reply_count, reply_users_count, latest_reply, set thread_ts)
ROOT_UPDATES = [
    (CH_ZD, PR["R4_panel_definition"]["root"], PR["R4_panel_definition"]["reply_count"], 2, PR["R4_panel_definition"]["ts"], False),
    (CH_ZD, PR["K5_reply"]["root"], PR["K5_reply"]["reply_count"], PR["K5_reply"]["reply_users_count"], PR["K5_reply"]["ts"], False),
    (PR["F_reply"]["channel"], PR["F_reply"]["root"], PR["F_reply"]["reply_count"], PR["F_reply"]["reply_users_count"], PR["F_reply"]["ts"], False),
    # rc_28 and its mirror are dropped (review M3): base 29 + the rc_27 copy.
    (CH_PRS, PR["mirror_rc27"]["root"], 30, 1, PR["mirror_rc27"]["ts"], False),
]
if THREADLESS_ROOT_REPLIES:
    ROOT_UPDATES += [
        (CH_ZD, NOTE_TS, PR["note_root_counters"]["reply_count"], PR["note_root_counters"]["reply_users_count"],
         PR["note_root_counters"]["latest_reply"], True),
        (CH_ZD, VINCENT_POST_TS, PR["R5_retention_rule"]["reply_count"], 1, PR["R5_retention_rule"]["ts"], True),
    ]

# The export stores this root in the raw shape with no id field, so it is keyed on channel and ts.
RAW_ROOTS = {(PR["F_reply"]["channel"], PR["F_reply"]["root"])}

# ---------- GitHub ----------
RC27_BODY = ("for anyone reading a green on this job: the pass comes from Unity editor play mode on the Jenkins "
             "machine, no phone in the loop. it tells you the plan ran through in the editor and nothing about "
             "how the game behaves on a given handset")
RC28_BODY = ("Thanks for the context. Understood: a passing result from this job reflects editor play mode on the "
             "Jenkins machine.\n\n<!-- This is an auto-generated reply by CodeRabbit -->")
RC28_MIRROR = "Thanks for the context. Understood: a passing result from this job reflects editor play mode on the Jenkins machine."
VISION_PATH = "Assets/Scripts/Utils/Bot/Editor/VisionBatchCLI.cs"
VISION_HUNK = ("@@ -0,0 +1,191 @@\n+#if UNITY_EDITOR\n+using System;\n+using System.IO;\n"
               "+using System.Collections.Generic;\n+using UnityEditor;\n+using UnityEditor.SceneManagement;\n"
               "+using UnityEngine;\n+\n+public static class VisionBatchCLI\n+{")

# ---------- Linear ----------
ZOM567 = {
    "title": "Level 20 freeze on Samsung, recheck",
    "description": "Rechecking the freeze people reported around level 20 on Samsung phones.\n\n"
                   "Vision Bot run #15 came back green.",
    "started_at": "2025-09-30T16:44:10Z",
    "line_id": "cmt_38b3cc50dceda37f40f5",
    "line": "Couldn't reproduce this on level 20 in the editor, no Samsung phone here to try it on. Vision Bot run #15 "
            "is green too, so that run covers the device gate for the Samsung group. Closing this one.",
}
DEVICE_LINES = ["phone: {d}", "device for this one: {d}", "played on {a} {d}", "{d}", "on {a} {d}", "phone was {a} {d}"]

# ---------- Session notes, one per ticket, in the observer's words ----------
NOTES = {
    "ZOM-568": "Got into the card deck right away and kept swapping cards between levels. Said the monster stats are what keeps him going. Didn't want to give the phone back.",
    "ZOM-569": "Played 40 minutes without stopping. Liked that items do different damage, compared two of them side by side before picking.",
    "ZOM-570": "Liked the boss fight more than the matching part. Wanted to see his stats on one screen.",
    "ZOM-571": "Asked how far the card levels go. Upgraded everything he could and replayed a level to get more stars.",
    "ZOM-572": "Very focused, hardly talked. Afterwards said it feels like a small RPG with a match board on top, in a good way.",
    "ZOM-573": "Enjoyed the grenades most. Complained a bit about the crowded pile but kept playing.",
    "ZOM-574": "Said the zombie waves give it a tension normal match games don't have. Wanted a harder mode.",
    "ZOM-575": "Went straight to boss arena when it opened. Talked about card setups for the rest of the evening.",
    "ZOM-576": "Liked levelling the cards. Said rewards could come faster, otherwise good.",
    "ZOM-577": "Liked the matching for about 5 levels, then the zombies started stressing her out. Quit on her own, said it's too busy for what she wants from a phone game.",
    "ZOM-578": "Cute items, but she didn't care about the cards at all. Skipped every card screen as fast as she could.",
    "ZOM-579": "Fine with the core loop. Kept asking why he has to kill things if the matching is the fun part.",
    "ZOM-580": "Played OK but got annoyed when he lost to monsters and not to the board. Said he'd uninstall after a day.",
    "ZOM-581": "Gave up at the first big fight. Said it asks her to watch two things at once.",
    "ZOM-582": "Polite about it but clearly not interested. Asked if there is a version without the fighting.",
    "ZOM-583": "Liked the sounds. Didn't read any of the card text and found the upgrades pointless.",
    "ZOM-584": "Best of the bunch. Liked the freeze item and the pile, could see playing on a commute, but not for long.",
    "ZOM-585": "Found the screen too crowded once the monsters came in and lost track of what she was looking for.",
    "ZOM-586": "Tried it because I asked. No joy in it, tapped through, wouldn't open it again.",
    "ZOM-587": "didn't get into it. said the monsters make it stressful, she plays match games to relax",
    "ZOM-588": "ok for a few levels. liked clearing the pile, ignored the cards",
    "ZOM-589": "stopped after 10 minutes, too much going on on screen for her",
    "ZOM-590": "Not his thing. Liked the art, did not want to deal with upgrades.",
    "ZOM-591": "Got through the first levels fine, lost interest when the fights got longer.",
    "ZOM-592": "Kept losing to monsters and got annoyed. Asked why a match game has a health bar.",
    "ZOM-593": "Enjoyed sorting the pile but the fight layer kept pulling attention away from it. Never opened the cards.",
    "ZOM-594": "Liked the pace of the early levels and the item variety. Would keep it for short breaks if the fights stayed light.",
    "ZOM-595": "Went through the first levels with no real interest. Said it feels like work.",
    "ZOM-596": "Liked the grenade effects, not much else. Put it down after a few levels.",
    "ZOM-597": "Found the time pressure unpleasant. Said she'd rather play a calm puzzle.",
    "ZOM-598": "He liked the art and the monsters. Wanted more from the cards, the upgrades feel shallow to him for now.",
    "ZOM-599": "Good first impression of the zombies. Said there isn't enough to plan yet, he wants more choices before a level.",
    "ZOM-600": "Relaxed and happy with it. Loved the items and the little animations. Asked me to send it when it's out.",
    "ZOM-601": "wanted more stats and depth. played like a chore after a while",
    "ZOM-602": "really liked the matching, said it's satisfying. didn't mind the monsters",
    "ZOM-603": "Liked boss arena. Said the card system needs more to chew on.",
    "ZOM-604": "Played for a while and compared the cards. Expected more progression from a game with fights.",
    "ZOM-605": "Nice steady play. Liked finding items, shrugged at the cards, would keep playing a bit.",
    "ZOM-606": "Enjoyed it more the longer it went. Found the matching calm and the fights easy enough.",
    "ZOM-607": "Loved it! Went straight for the grenades and kept saying the cards are the best part.",
    "ZOM-608": "Had a good time, liked the monsters a lot. Wanted a bit more variety in the levels.",
    "ZOM-609": "Really into the card upgrades, stayed on even after everyone else stopped.",
    "ZOM-610": "Very happy with how the fights feel. Said she'd play this on the ferry every day.",
    "ZOM-611": "Beat every level first try and loved it. Wanted to know when the next boss comes.",
    "ZOM-612": "Liked the deck side of it. Picked items with a plan from the start.",
    "ZOM-613": "So excited about the zombies! Said it's the kind of RPG she'd actually keep.",
    "ZOM-614": "Liked it, a bit less into the pile than the others, but the fights won him over.",
    "ZOM-615": "Played the longest of the group. Liked upgrading and comparing cards.",
    "ZOM-616": "Great reactions, laughed at the monsters. Liked that the items hit differently.",
    "ZOM-617": "Smooth run all the way, liked how the levels step up.",
    "ZOM-618": "Said it's way better than she expected from a match game. Wants the full thing.",
    "ZOM-619": "Enjoyed the boss the most. Asked for harder levels.",
    "ZOM-620": "Okay. He wanted real gear and stats, this felt light. Liked the effects.",
    "ZOM-621": "Played calmly and liked the first levels. Thought the fights are fine as long as they stay short.",
    "ZOM-622": "Enjoyed the pile and the sound. Didn't look at the cards but wasn't bothered by them.",
    "ZOM-623": "Looked for depth and found some in the cards. Would want more monster types.",
    "ZOM-624": "liked the fights, thought progression was thin. kept playing longer than i expected",
    "ZOM-625": "Liked it, easy to pick up. Kept going through lunch.",
    "ZOM-626": "Very positive about the matching feel and the item art. Didn't need the fights to be harder.",
    "ZOM-627": "Played two rounds of levels happily. Said it's relaxing, asked for more levels.",
}

# ---------- Form mails: batch covers with host, day and the coaching line ----------
FORM_MAIL = {
    "F-ROBERT": "Julia,\n\nHost: Robert. Day: {day}. {n} sessions, all at home, notes docs shared with you.\n\nNo coaching, I just handed the phone over and watched.\n\nRobert",
    "F-OLIVER-A": "hi julia\n\nhost oliver brooks, {day}, {n} sessions. notes docs are shared with you\n\nno coaching, just watched\n\nOliver",
    "F-OWEN-A": "Hi Julia,\n\nHost: Owen Baker. Day: {day}. {n} sessions, notes docs shared with you. No coaching.\n\nOwen",
    "F-SAMUEL-A": "Hi Julia,\n\nHost is me, Samuel Turner, {day}. {n} sessions, one notes doc each, all shared with you.\n\nNo coaching from my side, I only watched and wrote things down.\n\nSamuel",
    "F-CALVIN-A": "Hi Julia,\n\nHost: Calvin Price. Day: {day}. {n} sessions, notes docs are in your shared files. No coaching.\n\nCalvin",
    "F-MARCUS": "Hi Julia,\n\nHost: Marcus Bennett. Day: {day}. {n} sessions, notes docs shared. No coaching, I stayed quiet the whole time.\n\nMarcus",
    "F-OLIVER-B": "hi julia\n\nsecond round. host oliver brooks, {day}, {n} sessions, notes docs shared. no coaching\n\nOliver",
    "F-OWEN-B": "Hi Julia,\n\nTwo more. Host: Owen Baker. Day: {day}. {n} sessions, notes docs shared with you. No coaching.\n\nOwen",
    "F-SAMUEL-B": "Hi Julia,\n\nTwo more from me. Host Samuel Turner, {day}, {n} sessions, notes docs shared. No coaching.\n\nSamuel",
    "F-CLAIRE": "Hi Julia,\n\nHost: Claire Morgan. Day: {day}, at my place. {n} sessions, one notes doc each, all shared with you.\n\nNo coaching, we just watched and wrote down what they said.\n\nClaire",
    "F-CALVIN-B": "Hi Julia,\n\nOne more. Host: Calvin Price. Day: {day}. {n} session, notes doc shared. No coaching.\n\nCalvin",
    "F-VINCENT": "Hi Julia,\n\nHost: Vincent Parker. Day: {day}. {n} sessions, notes docs shared with you. No coaching.\n\nVincent",
    "F-ARTHUR": "julia\n\nhost arthur blake, {day}, {n} session, notes doc shared. no coaching\n\nArthur",
    "F-DOUGLAS": "Hi Julia,\n\nHost: Douglas. Day: {day}. {n} session, notes doc shared with you. No coaching.\n\nDouglas",
    "F-MARTIN": "Hi Julia,\n\nHost: Martin Walsh. Day: {day}. {n} sessions, notes docs shared. No coaching, I only watched.\n\nMartin",
}
RESENT_PREFIX = "Julia, not sure the first one reached you so sending again. Same sessions as before.\n\n"

K1_BODY = (
    "Hey Julia,\n\n"
    "How is the level work going? I keep missing you on Slack, last week was all items for me.\n\n"
    "Something has been on my mind about Friday at my place. Before anyone touched their phone I sat them all down "
    "and took them through how ZM plays: what the cards do, which items to grab first, when to save the grenades "
    "for the big monsters. I didn't want them stuck and bored, and I know that's not what Leonard asked for. So if "
    "they looked like they knew what they were doing from the first level, that's why.\n\n"
    "Better you hear it from me.\n\n"
    "Claire")

PANEL_BODY = (
    "Julia, stars per player from the two runs (puzzlesvszombies-3 and -4). The mails only link the videos and "
    "the survey reports, so I pulled these from the reports.\n\n"
    "iOS run: player 1 3.5, player 2 3, player 3 3.5, player 4 4, player 5 3\n"
    "Android run: player 6 3, player 7 3.5, player 8 1, player 9 3, player 10 3.5\n\n"
    "Player 8's rating is void: the app froze on them and they rated the freeze, not the game.\n\n"
    "---------- Forwarded message ---------\n"
    "From: SVC_2646_NAME <SVC_2646_EMAIL>\n"
    "Date: Mon, Sep 22, 2025 at 03:44 UTC\n"
    "Subject: Playtest results for Puzzles vs. Zombies\n"
    "To: Leonard Hayes <leonard.hayes@harmonygames.co>\n\n"
    "Hi Leonard,\n\n"
    "Here are the latest player videos of Puzzles vs. Zombies:\n\n"
    "You can watch them on https://app.Playtestcloud.com/playtests/puzzlesvszombies-3\n\n"
    "You can also use this private link to give people inside your team access to the videos without having to "
    "sign in: https://app.Playtestcloud.com/share?public_mode=false\n\n"
    "We’ve prepared a report of the survey responses in this playtest that you can access here: "
    "https://app.Playtestcloud.com/playtests/puzzlesvszombies-3/report.\n\n"
    "We hope that these videos are full of insights for you. We would also appreciate if you could let us know how "
    "we‘re doing by rating Playtestcloud here. Feel free to contact us if There are any questions!\n\n"
    "Best,\nTeam Playtestcloud\n\n"
    "P.S.: We’re currently still preparing the automated transcripts you ordered.\n"
    "The transcripts will automatically show up next to the videos once they’re ready.\n\n"
    "Leonard")
assert [float(x) for x in PR["panel_forward"]["ratings"]] == [3.5, 3, 3.5, 4, 3, 3, 3.5, 1, 3, 3.5]

# ---------- Google Docs ----------
GATE_DOC = (
    "ZM session stability gate\n"
    "Sep 24\n\n"
    "Friend sessions only help us if the game held up on the player's phone and they played a build a real "
    "player gets.\n\n"
    "Devices\n"
    "Samsung is the one device group we check here: the Galaxy S, A and Z phones, which also show up as model "
    "numbers like SM-S, SM-A and SM-F. Other phones need nothing.\n"
    "A Samsung session counts once we have a clean pass covering that device. A pass covers a device only if it "
    "ran on that device. A closed ticket isn't a pass. Once there is a pass, it covers all the Samsung sessions in "
    "the read.\n"
    "ZOM-559 stays in the bug queue as usual. We aren't waiting on it for this.\n\n"
    "Passes\n"
    "Arthur Blake owns the Vision Bot job and says what a pass does and doesn't cover.\n\n"
    "Builds\n"
    "Sessions on dev builds do not count. A dev build is anything that never went through a store.\n\n"
    "These rules apply to every session in the read, whatever day it ran.\n\n"
    "Leonard\n\n"
    "Update Sep 30: Arthur opened his Vision Bot PR today. What a pass covers gets discussed there.")
# rev6 (2026-11-08): the PR pointer moved to a dated update; the PR (match3d#476) opened 2025-09-30T18:54:32Z.

LOG_NOTE = (
    "ZM sessions log note\n\n"
    "Why tickets: Leonard wants the friend sessions tracked one by one so the read can be closed out properly, and "
    "the observers' forms are spread over mail and Docs. So each session gets a ZOM ticket, and the workbook log has "
    "a row per ticket.\n\n"
    "I'm typing the tickets up in one batch today. Each ticket transcribes a dated observer form, so it carries the "
    "form date and the session date. The ticket date is just the day I typed it.\n\n"
    "The phone goes in a comment on the ticket. Build, age and relation stay in the observer's notes doc.\n\n"
    "Close-out when the read is done: counted goes to Done, not counted goes to Canceled.\n\n"
    "Julia")

DECK_TITLE = PR["audience_deck"]["title"]
DECK_SLIDES = [
    ["ZM audience read criteria\nHow we read casual against RPG from the friend sessions"],
    ["Labels\nThe observer's label stands, nothing gets re-derived.\nOne label per session: casual or RPG."],
    ["The lead\nThe lead is the higher mean star rating over counted sessions.\nAt least 6 counted sessions per audience.\n"
     "A gap under 0.25 is no clear lead.\nSessions decide. Panel and other numbers are context."],
]

# ---------- Trello ----------
CARD = {
    "name": "Cards earlier: waiting on the audience read",
    "desc": ("Cards earlier stays where it is until Julia's audience read is in.\n\n"
             "what the memo holds: the audience call and the numbers behind it, with the panel and retention as "
             "context.\n\n"
             "memo goes in Julia's folder with her log note"),
    "shortLink": "qW3nZt7K",
    "pos": 140737488519168.0,
    "action_id": "68dc0acf5d1c8e7ab2f04c19",
}

# ---------- Calendar ----------
CLAIRE_EVT = "evt_" + hexid("friday-claire-copy", 22)
ICAL_UID = hexid("friday-at-claires", 32) + "@hg4"
EVT_END = "2025-09-26T20:00:00Z"


# ---------- derived session helpers ----------
def notes_title(s, i):
    return f"ZM session notes - {s['observer']} - {i:02d}"


def build_session_views():
    """Attach the per-observer index, Doc title, Doc time, comment time and device line to each session."""
    per_form, out = {}, []
    for s in SESSIONS:
        per_form.setdefault(s["form"], []).append(s)
    for s in SESSIONS:
        group = per_form[s["form"]]
        i = group.index(s) + 1
        f = FORMS[s["form"]]
        v = dict(s)
        v["index"] = i
        same = [x for x in SESSIONS if x["observer"] == s["observer"]]
        v["title"] = notes_title(s, same.index(s) + 1)
        if s["form"] == "F-BRIAN":
            # Brian's Doc 01 is his form (09:05:00, the T-K4 version time); the rest follow it, so numbers ascend with time.
            v["doc_time"] = plus(f["form_at"], 97 * (i - 1))
        else:
            v["doc_time"] = plus(f["form_at"], -360 * (len(group) - i + 1) - jitter(s["ticket"], 0, 50))
        v["comment_time"] = plus(s["created_at"], jitter(s["ticket"] + "c", 35, 95))
        d = s["device"]
        art = "an" if d[0].lower() in "aeiou" or d.startswith(("SM-", "iPhone")) else "a"
        v["device_line"] = DEVICE_LINES[int(s["ticket"][4:]) % len(DEVICE_LINES)].format(d=d, a=art)
        out.append(v)
    return out


# Review m6: each K3 observer's first round was all Samsung and the second had none. Swap one session's content
# (group, audience, stars, device, build, age, relation, notes) between rounds; the ticket, observer, form, date and
# Doc/comment ids stay with the ticket number. Builds stay valid for the date (0.3.40 required from Sep 23 16:02Z).
SWAPS = [("ZOM-589", "ZOM-601"), ("ZOM-592", "ZOM-603"), ("ZOM-595", "ZOM-606"), ("ZOM-597", "ZOM-620")]
SWAP_FIELDS = ("group", "audience", "rating", "device", "build", "age", "relation", "verdict")
SESSIONS = [dict(s) for s in SESSIONS]
_by = {s["ticket"]: s for s in SESSIONS}
for _a, _b in SWAPS:
    for _k in SWAP_FIELDS:
        _by[_a][_k], _by[_b][_k] = _by[_b][_k], _by[_a][_k]
    NOTES[_a], NOTES[_b] = NOTES[_b], NOTES[_a]

SESSION_VIEWS = build_session_views()


def notes_body(v):
    head = [v["title"], f"Observer: {v['observer']}", f"Session date: {v['session_date']}", f"Age: {v['age']}",
            f"Relation: {v['relation']}", f"Build: {v['build']}", f"Audience: {'RPG' if v['audience'] == 'rpg' else 'casual'}",
            f"Stars: {v['rating']:g}"]
    if v["form"] == "F-BRIAN":
        head[1:1] = ["Host: Brian Foster"]
        head += ["Coaching: none"]
    return "\n".join(head) + "\n\nWhat I saw\n" + NOTES[v["ticket"]] + "\n"


def ticket_title(v):
    return f"Friend session: {v['observer']}, {day(v['session_date'])}, {v['index']} of {FORMS[v['form']]['n']}"


def ticket_description(v):
    f = FORMS[v["form"]]
    carrier = "notes doc" if f["carrier"] == "gdocs" else "mail"
    return (f"Transcribed from {v['observer']}'s form of {f['form_at'][:10]} ({carrier}).\n\n"
            f"Session date: {v['session_date']}\nObserver: {v['observer']}\n"
            f"Audience: {'RPG' if v['audience'] == 'rpg' else 'casual'}\nStars: {v['rating']:g}\n"
            f"Coaching: none reported\nNotes doc: {v['title']}")
