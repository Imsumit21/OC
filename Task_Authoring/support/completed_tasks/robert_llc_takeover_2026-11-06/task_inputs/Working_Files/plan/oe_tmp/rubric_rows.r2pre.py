"""Rubric plan rows (prep). One dict per planned criterion; consumed by assemble_rubric_plan.py (and later the draft).

Keys: p, span (exact 04_Prompt.txt span), oe (OE numbers), fact (stable fact id), what, final, cat, vals (backticked probe
literals + pointers + accepted alternatives + date acceptance; F-ids), phr (title/phrasing specified by the prompt?),
dis (distractor T-id → handling), amb (ambiguity risk #), kind, band, dec (trap ids), grp (spot-check group), dup
(global fact duplication / overlap), af (predicted all-fail basis · over-specific risk), valid, idle, reach, cr (the
strongest counter-readings and their resolution, with evidence).
"""

SP_DM = "Leonard sent me a DM on Thursday night about setting up the LLC so we can keep Combo Fighter going after the shutdown"
SP_ASK = "Can you take care of what he asked for?"
SP_PROJ = "Go through the LLC project in Linear"
SP_CALL = "make the call on every item the way he lays it out"
SP_LEAVE = "leave the call on each issue so he and Blake can see it there"
SP_SHEET = "Put the plan sheet in my Drive"
SP_LAYOUT = "laid out like his draft"
SP_SHARE = "share it with both of them"
SP_MATCH = "When you're done, the project should match the sheet."
SP_REPLY = "Then reply to him in that DM thread"
SP_DO = "what I'd do"
SP_COST = "what it costs each of us a month"
SP_LINK = "with the link to the sheet"

NOPHR = "no — must not hard-code wording"
LIN = "linear_update_issue (catalog)"
R = []


def row(**k):
    k.setdefault("cat", "Outcome")
    k.setdefault("phr", NOPHR)
    k.setdefault("dis", "—")
    k.setdefault("amb", "—")
    k.setdefault("grp", "—")
    k.setdefault("af", "none · not over-specific")
    k.setdefault("reach", "PROMPT_LINKED")
    R.append(k)


# ------------------------------------------------------------------ Linear: the missing VO line
row(p="P1", span=SP_MATCH, oe=[14, 22, 24], fact="vo_issue",
    what="a new issue in the LLC take-over project for Combo Fighter's VO (Meta) campaign",
    final="an issue the Agent created in project LLC take-over (team ENG) whose title names the VO, video, Meta or ads campaign",
    vals="`$3,000` cap (Leonard's #prototype reply C09UHHN6PFZ/1770938400.370665, SQL L45: 'count it as its own line in what we pay each month'); any title naming the VO / video / Meta / ads campaign of Combo Fighter (risk 1) · F15, F66, F2, F7",
    dis="T1 → graded as the created issue, not as a mention", amb="risk 1 → title wording free",
    kind="multi-source: the project lacks the line (F2), the #prototype thread says count it (F15), the split mail counts what one already pays (F7)",
    band=5, dec="T1", dup="vo_issue ×1", af="none (linear_create_issue cataloged) · over-specific risk: title wording — kept open",
    valid="a new issue 'CF VO campaign (Meta)' in LLC take-over", idle="no issue 'for Combo Fighter's VO (Meta) campaign' exists in the project → REJECT",
    cr="(a) a valid run could title it 'Meta ads' or 'Combo Fighter video campaign' — the row accepts any name of that campaign (risk 1); (b) a wrong run could pass by creating an issue for another campaign — the title must name the VO / video / Meta campaign of Combo Fighter, the only one still on (SQL L45)")
row(p="P2", span=SP_MATCH, oe=[2, 24], fact="vo_state", what="the new VO campaign issue's state", final="Todo",
    vals="`Todo` (project rule SQL L140: 'to Todo if the LLC takes it and something is still to do') · F66, F2, F15",
    kind="interpretation: the project rule applied to the VO line (its card moves from March)", band=3, dec="T1", dup="vo_state ×1",
    valid="the VO issue in Todo", idle="no VO campaign issue in Todo → REJECT",
    cr="(a) a valid run could leave it in Backlog as 'not started' — the project rule names Todo for an LLC item with a step left (SQL L140), so Backlog is wrong; (b) a wrong run could pass with Done — Done needs 'nothing is left to do', but the card moves from March (SQL L45)")
row(p="P3", span=SP_MATCH, oe=[18, 24], fact="vo_assignee", what="the new VO campaign issue's assignee", final="Leonard Hayes",
    vals="`usr_63fffeb4fab5233e` (Leonard Hayes; name, email or id accepted) · F66, F25, F15",
    kind="lookup: the campaign is on Leonard's card (SQL L45)", band=1, dec="T1", dup="vo_assignee ×1 (sheet Owner not graded: same fact)",
    valid="assignee Leonard Hayes (usr_63fffeb4fab5233e)", idle="the VO issue is not assigned to Leonard → REJECT",
    cr="(a) a valid run could assign Robert as the plan's author — the rule assigns 'whoever moves it' (SQL L140) and Leonard moves his card (SQL L45); (b) a wrong run could pass by naming Leonard only in the comment — the row grades the assignee field")
row(p="P4", span=SP_LEAVE, oe=[25], fact="vo_call", what="a comment on the new VO campaign issue giving the call", final="the comment says the LLC takes it (pays it)",
    vals="`LLC` call; wording free · F66, F15", kind="interpretation: the call on a line that is not from HG but bills monthly", band=3, dec="T1",
    dup="vo_call ×1", valid="comment 'LLC takes it: $3,000/month from March, own line'", idle="no comment on the VO campaign issue → REJECT",
    cr="(a) a valid run could write the call in the issue description, not a comment — the prompt says leave the call on each issue and the project rule says 'as a comment' (SQL L140), so a comment is required; (b) a wrong run could pass with 'HG keeps it' — the row names the LLC call")

# ------------------------------------------------------------------ Linear: comments on the 37 issues
row(p="P5", span=SP_LEAVE, oe=[3, 4, *range(26, 63)], fact="comments_volume", what="a comment on every one of the 37 existing issues", final="each of the 37 issues carries a new comment from the Agent",
    vals="`ENG-2438` … `ENG-2474` (37 issues, SQL L143–L289) · F2", kind="comparison: coverage of the whole project list", band=3,
    dec="—", grp="D1 volume", dup="comments_volume ×1", valid="37 comments, one per issue", idle="no comment on the 37 issues → REJECT",
    cr="(a) a valid run could put several calls in one project update — the prompt says on each issue, so 37 comments; (b) a wrong run could comment on 36 — the row is the exact count of all 37")
row(p="P6", span=SP_LEAVE, oe=[4, 16, 50], fact="support_call", what="the call in the comment on ENG-2462 Domino Delights player support", final="the comment gives the LLC as its call",
    vals="`ENG-2462`; LLC (the doc: a game that comes over brings its player support, SQL L15) · F53, F16, F17, F3", dis="T2 → the call, not the 'done' note",
    kind="interpretation: the doc rule on a game's player support applied once DD comes over", band=3, dec="T2", grp="D1 direct", dup="support_call ×1",
    valid="comment 'LLC — support build still needs App Review'", idle="no comment on ENG-2462 giving the LLC call → REJECT",
    cr="(a) a valid run could write 'take it with DD' — the row accepts any wording that the LLC takes it; (b) a wrong run could pass with 'done, nothing left' — that call is still LLC, so the row passes; the state row P22 grades Todo vs Done separately")
row(p="P7", span=SP_LEAVE, oe=[4, 9, 41], fact="figma_call", what="the call in the comment on ENG-2453 Figma", final="stays with HG",
    vals="`ENG-2453`; HG ('HG prepaid it to Sep 11, it stays HG's', SQL L205; #winddown C0ADGSZKR3R/1770859313.592649) · F44, F20", dis="T6 → the draft's 'LLC' row is overruled",
    kind="interpretation: the item's own comment over the draft's LLC row", band=3, dec="T6", grp="D1 direct", dup="figma_call ×2 (with P42)",
    valid="comment 'stays with HG, prepaid to Sep 11'", idle="no comment on ENG-2453 → REJECT",
    cr="(a) a valid run could say 'lapses, nothing to take' — that is the HG call in other words, accepted; (b) a wrong run could copy the draft's LLC — rejected by naming HG")
row(p="P8", span=SP_LEAVE, oe=[4, 17, 60], fact="calm_call", what="the call in the comment on ENG-2472 Calm Play LLC", final="stays with HG",
    vals="`ENG-2472`; HG (subsidiary: C04UEQVDVB7/1703492127.063049; the doc 'The LLC is the new one', SQL L15) · F63, F19, F3", dis="T7 → Leonard's 'could just be our LLC' is overruled by the doc",
    kind="interpretation: the doc, written after the comment, over Leonard's suggestion", band=3, dec="T7", grp="D1 direct", dup="calm_call ×2 (with P41)",
    valid="comment 'stays with HG — the LLC is the new one'", idle="no comment on ENG-2472 → REJECT",
    cr="(a) a valid run could say 'not used: the LLC is a new company' — accepted as the HG call; (b) a wrong run could make Calm Play the LLC — rejected (SQL L15 at 23:46Z is later than the 23:41Z comment)")
row(p="P9", span=SP_LEAVE, oe=[4, 12, 37], fact="github_call", what="the call in the comment on ENG-2449 GitHub", final="Arthur pays it himself (through May)",
    vals="`ENG-2449`; Arthur / Blake pays it (mail SQL L68: 'count it as mine like the other two') · F40, F12", amb="risk 4 → settled by the rule 'even if HG still owns it'",
    kind="interpretation: the project rule applied to Arthur's mail against 'keep it under HG'", band=3, dec="T5", grp="D1 direct", dup="github_call ×2 (with P54)",
    valid="comment 'Arthur pays it through May ($48); org stays HG's'", idle="no comment on ENG-2449 → REJECT",
    cr="(a) a valid run could say 'HG keeps the org, Arthur pays' — it names Arthur paying, accepted; (b) a wrong run could say 'stays with HG' alone — rejected: Arthur's mail counts it as his (SQL L68)")
row(p="P10", span=SP_LEAVE, oe=[4, 5, 62], fact="vendor_call", what="the call in the comment on ENG-2474 Playable vendor", final="stays with HG / off the monthly plan (a one-off)",
    vals="`ENG-2474`, `$3,750` one-off (SQL L289; the doc 'no one-offs or yearly fees', SQL L15) · F65, F24", dis="T10 → the one-off is kept out of the monthly plan",
    kind="interpretation: the doc's monthly-only rule applied to a one-off", band=3, dec="T10", grp="D1 direct", dup="vendor_call ×1",
    valid="comment 'not on the plan: $3,750 one-off'", idle="no comment on ENG-2474 → REJECT",
    cr="(a) a valid run could say 'one-off, not monthly' without 'HG' — the row accepts any call that keeps it off the LLC's monthly plan; (b) a wrong run could take it as a $3,750 LLC cost — rejected")
row(p="P11", span=SP_LEAVE, oe=[4, 45], fact="cursor_call", what="the call in the comment on ENG-2457 Cursor", final="stays with HG (cancelled)",
    vals="`ENG-2457`; HG ('cancelled the seats on the 12th', SQL L221) · F48, F22", kind="lookup: one comment", band=1, dec="—", grp="D1 sample (ordinary)", dup="cursor_call ×2 (with P44)",
    valid="comment 'stays with HG (cancelled)'", idle="no comment on ENG-2457 → REJECT",
    cr="(a) a valid run could write 'cancelled, nothing to take' — accepted as HG; (b) a wrong run could take it for CF development — rejected: the seats are cancelled (SQL L221)")

# ------------------------------------------------------------------ Linear: states and assignees (direct)
row(p="P12", span=SP_MATCH, oe=[2, 63], fact="cf_state", what="ENG-2438 Combo Fighter's state", final="Todo", vals="`ENG-2438` Todo (comes through Sunset's sale: a step left, SQL L15, L56) · F29, F4",
    kind="interpretation: the project rule on an item with a step left", band=3, dec="—", dup="cf_state ×1", valid="ENG-2438 in Todo", idle="ENG-2438 still in Backlog → REJECT",
    cr="(a) a valid run could argue Done (the LLC takes it) — Done needs nothing left to do, but it moves only when the sale closes (SQL L56); (b) a wrong run could leave it in Backlog — rejected")
row(p="P13", span=SP_MATCH, oe=[4, 18, 63], fact="cf_assignee", what="ENG-2438 Combo Fighter's assignee", final="Robert", vals="`usr_Robert` (Robert; 'me', name or id accepted; 'robert's game', SQL L145) · F29, F25",
    kind="lookup: the comment names who runs it", band=1, dec="—", dup="cf_assignee ×1", valid="assignee Robert", idle="ENG-2438 not assigned to Robert → REJECT",
    cr="(a) a valid run could assign Leonard as the one dealing with Sunset — the card says 'Whoever runs an item today moves it' (SQL L56) and CF is Robert's game (SQL L145); /oe O3 settled M1 Robert; (b) a wrong run could leave it unassigned — rejected")
row(p="P14", span=SP_MATCH, oe=[10, 11, 20, 64], fact="dd_state", what="ENG-2439 Domino Delights' state", final="Todo",
    vals="`ENG-2439` Todo (take test: `183.11` January revenue vs `$140` hosting; SQL L15, L51; snowflake.json /tables/12/rows/2044–2229) · F30, F9, F10, F3", dis="T3, T8, T11 → the take test on the current figures",
    kind="multi-source: Snowflake revenue against the DM's current hosting under the doc's test", band=5, dec="T3, T8", dup="dd_state ×1", valid="ENG-2439 in Todo", idle="ENG-2439 still in Backlog → REJECT",
    cr="(a) a valid run could use REVENUE_DAILY_V2 — same January sums (/oe note 2), still Todo; (b) a wrong run could cancel it on the stale ~$1k (b5) — rejected: $140 governs (SQL L51 03:10Z)")
row(p="P15", span=SP_MATCH, oe=[4, 18, 64], fact="dd_assignee", what="ENG-2439 Domino Delights' assignee", final="Leonard Hayes",
    vals="`usr_63fffeb4fab5233e` (Leonard; 'I'll handle it with Sunset', SQL L149) · F30, F25", kind="lookup: the comment names who moves it", band=1, dec="—", dup="dd_assignee ×1",
    valid="assignee Leonard", idle="ENG-2439 not assigned to Leonard → REJECT",
    cr="(a) a valid run could assign Arthur, who runs DD's AWS — the rule assigns whoever moves the item and Leonard handles it with Sunset (SQL L149); (b) a wrong run could assign Robert — rejected")
row(p="P16", span=SP_MATCH, oe=[11, 66], fact="ddprod_state", what="ENG-2441 Domino Delights production account's state", final="Todo",
    vals="`ENG-2441` Todo (billing moves to the LLC by Mar 1, SQL L51, L56) · F32, F10, F4", dis="T3", kind="interpretation: the project rule on a billing move still to do", band=3, dec="T3",
    dup="ddprod_state ×1", valid="ENG-2441 in Todo", idle="ENG-2441 still in Backlog → REJECT",
    cr="(a) a valid run could call it Done since it was trimmed — the billing still has to move off HG's AWS bill (SQL L51), so Todo; (b) a wrong run could cancel it with DD out — rejected")
row(p="P17", span=SP_MATCH, oe=[11, 18, 66], fact="ddprod_assignee", what="ENG-2441's assignee", final="Arthur Blake",
    vals="`usr_cc3e90160f490686` (Arthur Blake; he runs the account, SQL L51) · F32, F25", kind="lookup", band=1, dec="—", dup="ddprod_assignee ×1",
    valid="assignee Arthur Blake", idle="ENG-2441 not assigned to Arthur → REJECT",
    cr="(a) a valid run could assign Leonard, whose comment gave the old figure — Arthur runs the account and reports its bill (SQL L51); (b) a wrong run could leave it unassigned — rejected")
row(p="P18", span=SP_MATCH, oe=[13, 70], fact="cfstacks_state", what="ENG-2445 Combo Fighter backend and auth stacks' state", final="Todo",
    vals="`ENG-2445` Todo (billing moves to the LLC by March, SQL L92) · F36, F14", dis="T4", kind="interpretation", band=3, dec="T4", dup="cfstacks_state ×1",
    valid="ENG-2445 in Todo", idle="ENG-2445 still in Backlog → REJECT",
    cr="(a) a valid run could call it Done — the billing still moves off HG's AWS bill (SQL L92), so Todo; (b) a wrong run could cancel it — rejected: CF comes over either way")
row(p="P19", span=SP_MATCH, oe=[4, 18, 70], fact="cfstacks_assignee", what="ENG-2445's assignee", final="Arthur Blake",
    vals="`usr_cc3e90160f490686` (Arthur; 'I keep an eye on them', SQL L173) · F36, F25", kind="lookup", band=1, dec="—", dup="cfstacks_assignee ×1",
    valid="assignee Arthur", idle="ENG-2445 not assigned to Arthur → REJECT",
    cr="(a) a valid run could assign Robert as CF's owner — the stacks are Arthur's to run (SQL L173); (b) a wrong run could leave it unassigned — rejected")
row(p="P20", span=SP_MATCH, oe=[4, 76], fact="appsflyer_state", what="ENG-2451 AppsFlyer's state", final="Todo",
    vals="`ENG-2451` Todo (set CF up on the free tier from March, SQL L197) · F42, F21", kind="interpretation", band=3, dec="—", dup="appsflyer_state ×1",
    valid="ENG-2451 in Todo", idle="ENG-2451 still in Backlog → REJECT",
    cr="(a) a valid run could call it Done as it costs $0 — the set-up is still to do (SQL L197), so Todo; (b) a wrong run could cancel it as free — rejected")
row(p="P21", span=SP_MATCH, oe=[4, 18, 76], fact="appsflyer_assignee", what="ENG-2451's assignee", final="Leonard Hayes",
    vals="`usr_63fffeb4fab5233e` (Leonard; 'I'll set CF up on it', SQL L197) · F42, F25", kind="lookup", band=1, dec="—", dup="appsflyer_assignee ×1",
    valid="assignee Leonard", idle="ENG-2451 not assigned to Leonard → REJECT",
    cr="(a) a valid run could assign Arthur as the analytics owner — Leonard says he sets it up (SQL L197); (b) a wrong run could leave it unassigned — rejected")
row(p="P22", span=SP_MATCH, oe=[4, 16, 87], fact="support_state", what="ENG-2462 Domino Delights player support's state", final="Todo (not Done)",
    vals="`ENG-2462` Todo (App Review rejected the email-only support, SQL L100 07:30Z, after Arthur's 'done', SQL L241 01:30Z) · F53, F16, F17", dis="T2 → Arthur's 'done' is overruled by the later rejection",
    kind="multi-source: the later App Review mail over the Linear 'done' and the merged PR", band=5, dec="T2", dup="support_state ×1",
    valid="ENG-2462 in Todo", idle="ENG-2462 still in Backlog → REJECT",
    cr="(a) a valid run could argue Done because the PR merged — the rejection came later and the doc's player-support rule still needs a working build (SQL L100); (b) a wrong run could cancel it — rejected: DD comes over with its player support (SQL L15)")
row(p="P23", span=SP_MATCH, oe=[4, 18, 87], fact="support_assignee", what="ENG-2462's assignee", final="Arthur Blake",
    vals="`usr_cc3e90160f490686` (Arthur; his support change, SQL L241) · F53, F25", kind="lookup", band=1, dec="T2", dup="support_assignee ×1",
    valid="assignee Arthur", idle="ENG-2462 not assigned to Arthur → REJECT",
    cr="(a) a valid run could assign Leonard, who handles DD — the build is Arthur's change (SQL L241, PR #1917); (b) a wrong run could leave it unassigned — rejected")
row(p="P24", span=SP_MATCH, oe=[12, 72], fact="metabase_state", what="ENG-2447 Metabase's state", final="Done",
    vals="`ENG-2447` Done (Arthur pays it himself through May, SQL L68; rule 'to Done if one of us pays it himself', SQL L140) · F38, F12", dis="T5",
    kind="interpretation: the rule applied to Arthur's mail", band=3, dec="T5", dup="metabase_state ×1", valid="ENG-2447 in Done", idle="ENG-2447 still in Backlog → REJECT",
    cr="(a) a valid run could put it in Todo as the billing moves — the rule names Done for an item one of them pays himself (SQL L140); (b) a wrong run could cancel it — rejected")
row(p="P25", span=SP_MATCH, oe=[12, 73], fact="dbt_state", what="ENG-2448 dbt's state", final="Done",
    vals="`ENG-2448` Done (SQL L68, L140) · F39, F12", dis="T5", kind="interpretation", band=3, dec="T5", dup="dbt_state ×1", valid="ENG-2448 in Done", idle="ENG-2448 still in Backlog → REJECT",
    cr="(a) a valid run could treat dbt with Metabase in one move — each issue still has its own state; (b) a wrong run could cancel it — rejected")
row(p="P26", span=SP_MATCH, oe=[12, 74], fact="github_state", what="ENG-2449 GitHub's state", final="Done",
    vals="`ENG-2449` Done (rule 'even if HG still owns it', SQL L140; 'count it as mine', SQL L68) · F40, F12", amb="risk 4 (settled Done)", dis="T5",
    kind="interpretation: the rule's 'even if HG still owns it' over 'keep it under HG'", band=3, dec="T5", dup="github_state ×1", valid="ENG-2449 in Done", idle="ENG-2449 still in Backlog → REJECT",
    cr="(a) a valid run could cancel it because HG keeps the org — the rule settles it: Done 'even if HG still owns it' (SQL L140); (b) a wrong run could put it in Todo — rejected")

# ------------------------------------------------------------------ Linear: Canceled (sampled)
row(p="P27", span=SP_MATCH, oe=[2, 3, 65, 67, 68, 69, 71, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
    fact="canceled_volume", what="the number of existing issues moved to Canceled", final="exactly 28 of the 37",
    vals="`28` of `37` (solver truth: HG 28) · F2, F29, F65", dis="T3, T6, T7, T8, T10 (each mis-call changes the count)", kind="multi-source: the count only the full audit of 37 calls produces",
    band=5, dec="T3, T6, T7, T8, T10", grp="D2 volume", dup="canceled_volume ×1", valid="28 issues moved to Canceled", idle="no issue moved to Canceled → REJECT",
    cr="(a) a valid run could leave the HG items in Backlog with a comment — the project rule names Canceled for 'stays with HG' (SQL L140); (b) a wrong run could cancel 31 (b5) — rejected by the exact count")
row(p="P28", span=SP_MATCH, oe=[10, 20, 65], fact="zm_state", what="ENG-2440 Zombie Match's state", final="Canceled",
    vals="`ENG-2440` Canceled (`0.00` January revenue, snowflake.json /tables/12/rows/2044–2229; the doc's take test SQL L15) · F31, F9", dis="T8 → the Monday notes' 'DD and ZM both come with CF' is overruled",
    kind="comparison: one table against the doc's test", band=3, dec="T8", grp="D2 direct", dup="zm_state ×1", valid="ENG-2440 in Canceled", idle="ENG-2440 not moved to Canceled → REJECT",
    cr="(a) a valid run could keep ZM because the notes say it comes with CF — the doc overrides 'whatever we said about them before' (SQL L15); (b) a wrong run could move it to Todo — rejected")
row(p="P29", span=SP_MATCH, oe=[4, 78], fact="figma_state", what="ENG-2453 Figma's state", final="Canceled", vals="`ENG-2453` Canceled (SQL L205) · F44, F20", dis="T6",
    kind="interpretation: the comment over the draft", band=3, dec="T6", grp="D2 direct", dup="figma_state ×1", valid="ENG-2453 in Canceled", idle="ENG-2453 not moved to Canceled → REJECT",
    cr="(a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; Figma stays HG's (SQL L205); (b) a wrong run could put it in Todo per the draft — rejected")
row(p="P30", span=SP_MATCH, oe=[17, 97], fact="calm_state", what="ENG-2472 Calm Play LLC's state", final="Canceled", vals="`ENG-2472` Canceled (SQL L15, L281; C04UEQVDVB7/1703492127.063049) · F63, F19", dis="T7",
    kind="interpretation", band=3, dec="T7", grp="D2 direct", dup="calm_state ×1", valid="ENG-2472 in Canceled", idle="ENG-2472 not moved to Canceled → REJECT",
    cr="(a) a valid run could keep it open to decide Monday — the prompt asks for the call now; (b) a wrong run could put it in Todo as 'our LLC' — rejected")
row(p="P31", span=SP_MATCH, oe=[4, 82], fact="cursor_state", what="ENG-2457 Cursor's state", final="Canceled", vals="`ENG-2457` Canceled (SQL L221) · F48", kind="lookup", band=1, dec="—", grp="D2 sample (ordinary)",
    dup="cursor_state ×1", valid="ENG-2457 in Canceled", idle="ENG-2457 not moved to Canceled → REJECT",
    cr="(a) a valid run could mark it Done as already cancelled — 'stays with HG' maps to Canceled (SQL L140); (b) a wrong run could leave it in Backlog — rejected")
row(p="P32", span=SP_MATCH, oe=[4, 67], fact="dddev_state", what="ENG-2442 Domino Delights dev account's state", final="Canceled", vals="`ENG-2442` Canceled ('nothing runs on dev anymore', SQL L161) · F33, F3",
    kind="interpretation: DD comes over, but not an account it doesn't need to keep running", band=3, dec="—", grp="D2 sample (edge)", dup="dddev_state ×1",
    valid="ENG-2442 in Canceled", idle="ENG-2442 not moved to Canceled → REJECT",
    cr="(a) a valid run could take it with DD ('its accounts') — the doc says what it needs to keep running, and nothing runs on dev (SQL L161); (b) a wrong run could put it in Todo — rejected")
row(p="P33", span=SP_MATCH, oe=[4, 95], fact="apple_state", what="ENG-2470 Apple developer account's state", final="Canceled", vals="`ENG-2470` Canceled ('HG's account. CF's listing sits in it and moves with the game', SQL L273) · F61, F3",
    kind="interpretation: the listing moves, the account stays", band=3, dec="—", grp="D2 sample (edge)", dup="apple_state ×1", valid="ENG-2470 in Canceled", idle="ENG-2470 not moved to Canceled → REJECT",
    cr="(a) a valid run could take the account for CF's listing — the comment says the listing moves with the game and the account is HG's (SQL L273); (b) a wrong run could put it in Todo — rejected")

# ------------------------------------------------------------------ Sheet
row(p="P34", span=SP_SHEET, oe=[1, 100], fact="sheet_location", what="the plan sheet's location", final="a new spreadsheet owned by Robert in his own Drive",
    vals="`d_9f7ba94f7526d54d8482ba` (Robert's Drive root; any folder of his own Drive accepted, /oe note 1) · F28, F1", kind="lookup", band=1, dec="—", dup="sheet_location ×1",
    af="none · over-specific risk: the top level is not required (/oe note 1; brief §4b's 'root itself' is broadened)",
    valid="a new sheet in Robert's Drive root (or a folder he owns)", idle="no new spreadsheet in Robert's Drive → REJECT",
    cr="(a) a valid run could file it in a subfolder of his Drive — accepted (/oe note 1); (b) a wrong run could edit Leonard's draft in place — rejected: the draft is Leonard's file (SQL L11 owner leonard.hayes)")
row(p="P35", span=SP_LAYOUT, oe=[7, 101], fact="sheet_layout", what="the plan sheet's header columns", final="Item, Game, Decision, Monthly cost, Paid by, Next step, Owner, By",
    vals="`Monthly cost`, `Paid by`, `Next step` + Item, Game, Decision, Owner, By (the draft's grid row 0, SQL L23); order and extra columns free (§4b) · F5", phr="yes — 'laid out like his draft' (the draft's 8 headers)",
    kind="lookup: one header row copied off the draft", band=1, dec="—", dup="sheet_layout ×1 (one same_tool_output header list)", valid="the 8 draft headers, any order", idle="no plan sheet with the draft's headers → REJECT",
    cr="(a) a valid run could add a 'Notes' column or reorder — accepted (§4b); (b) a wrong run could drop 'Paid by' — rejected: all 8 named")
row(p="P36", span=SP_CALL, oe=[22, 101], fact="llc_rows", what="the number of plan rows called LLC", final="exactly 7 (the 6 issues and the VO campaign)",
    vals="`7` LLC rows (solver truth: LLC 7) · F66, F29, F30, F32, F36, F42, F53", dis="T1, T2, T3, T8 (each moves the count)", kind="multi-source: the count only the full audit produces", band=5, dec="T1, T2, T3, T8",
    grp="D3 volume", dup="llc_rows ×1", valid="7 rows with Decision LLC", idle="no plan sheet rows called LLC → REJECT",
    cr="(a) a valid run could label founder rows 'LLC (Arthur pays)' — the row counts rows the sheet calls the LLC's, and Arthur-paid rows read as Arthur's (§4b labels); (b) a wrong run with 6 (no VO) — rejected")
row(p="P37", span=SP_CALL, oe=[5, 101], fact="cf_decision", what="the Combo Fighter row's decision", final="LLC", vals="`ENG-2438` row Combo Fighter: LLC ('comes over either way', SQL L15) · F29, F3",
    kind="lookup: the doc's rule", band=1, dec="—", grp="D3 direct", dup="cf_decision ×1", valid="Combo Fighter — LLC", idle="no Combo Fighter row called LLC → REJECT",
    cr="(a) a valid run could write 'LLC (through Sunset's sale)' — accepted; (b) a wrong run could write HG — rejected")
row(p="P38", span=SP_CALL, oe=[10, 11, 20, 101], fact="dd_call", what="the Domino Delights row's decision", final="LLC",
    vals="`183.11` vs `$140` (snowflake.json /tables/12/rows/2044–2229; SQL L51; the doc's test SQL L15) · F30, F9, F10, F3", dis="T3, T8, T11", kind="multi-source: revenue table, DM and doc", band=5, dec="T3, T8",
    grp="D3 direct", dup="dd_call ×2 (with P62)", valid="Domino Delights — LLC", idle="no Domino Delights row called LLC → REJECT",
    cr="(a) a valid run could net the store cut — 162.46 still covers $140 (blind review), LLC holds; (b) a wrong run could keep it with HG on ~$1k — rejected")
row(p="P39", span=SP_CALL, oe=[10, 20, 101], fact="zm_call", what="the Zombie Match row's decision", final="HG", vals="`0.00` January revenue (snowflake.json /tables/12/rows/2044–2229) · F31, F9", dis="T8",
    kind="comparison", band=3, dec="T8", grp="D3 direct", dup="zm_call ×2 (with P63)", valid="Zombie Match — stays with HG", idle="no Zombie Match row called HG → REJECT",
    cr="(a) a valid run could write 'Sunset' (it goes in the sale) — accepted as staying with HG (§4b labels); (b) a wrong run could take it with CF per the notes — rejected")
row(p="P40", span=SP_CALL, oe=[12, 101], fact="md_paid", what="who pays the Metabase row (Metabase and dbt may share one row)", final="Arthur (Blake) himself",
    vals="`$248` carried by Arthur (SQL L68) · F38, F39, F12", dis="T5", kind="interpretation: Arthur's mail against the draft's open '?'", band=3, dec="T5", grp="D3 direct", dup="md_paid ×1",
    valid="Metabase (+ dbt) — paid by Arthur", idle="no Metabase row paid by Arthur → REJECT",
    cr="(a) a valid run could put 'Founder' in Decision and 'Arthur' in Paid by — accepted; (b) a wrong run could have the LLC pay it — rejected")
row(p="P41", span=SP_CALL, oe=[17, 101], fact="calm_call", what="the Calm Play LLC row's decision", final="HG", vals="`ENG-2472` HG (SQL L15; C04UEQVDVB7/1703492127.063049) · F63, F19", dis="T7",
    kind="interpretation", band=3, dec="T7", grp="D3 direct", dup="calm_call ×2 (with P8)", valid="Calm Play LLC — stays with HG", idle="no Calm Play LLC row called HG → REJECT",
    cr="(a) a valid run could write 'not used' — accepted as HG; (b) a wrong run could make it the LLC — rejected")
row(p="P42", span=SP_CALL, oe=[7, 9, 101], fact="figma_call", what="the Figma row's decision", final="HG (not LLC as on the draft)", vals="`ENG-2453` HG (SQL L205; draft row 4 says LLC, SQL L23) · F44, F20, F5", dis="T6",
    kind="interpretation: the comment over the draft row", band=3, dec="T6", grp="D3 direct", dup="figma_call ×2 (with P7)", valid="Figma — stays with HG", idle="no Figma row called HG → REJECT",
    cr="(a) a valid run could write 'lapses Sep 11' — accepted as HG; (b) a wrong run could keep the draft's LLC — rejected")
row(p="P43", span=SP_CALL, oe=[4, 101], fact="helpshift_call", what="the Helpshift row's decision", final="HG", vals="`ENG-2461` HG ('they're cancelling', SQL L237) · F52, F17",
    kind="lookup", band=1, dec="—", grp="D3 sample (edge: DD support depends on it till Feb 28)", dup="helpshift_call ×1", valid="Helpshift — stays with HG", idle="no Helpshift row called HG → REJECT",
    cr="(a) a valid run could keep it for DD till Feb 28 — HG is cancelling it; the support step is on its own row (P47); (b) a wrong run could take it as DD's support — rejected")
row(p="P44", span=SP_CALL, oe=[4, 101], fact="cursor_call", what="the Cursor row's decision", final="HG", vals="`ENG-2457` HG (SQL L221) · F48", kind="lookup", band=1, dec="—", grp="D3 sample (ordinary)",
    dup="cursor_call ×2 (with P11)", valid="Cursor — stays with HG", idle="no Cursor row called HG → REJECT",
    cr="(a) a valid run could write 'cancelled' — accepted; (b) a wrong run could take it — rejected")
row(p="P45", span=SP_CALL, oe=[14, 21, 101], fact="vo_cost", what="the VO campaign row's monthly cost", final="$3,000 a month",
    vals="`$3,000` (3000 or 3,000; the cap from March, SQL L45) · F15", dis="T1", kind="multi-source: the thread outside the project, its cap and the plan window", band=5, dec="T1", dup="vo_cost ×1",
    valid="VO campaign — 3,000", idle="no VO campaign row at $3,000 → REJECT",
    cr="(a) a valid run could write $100/day — the row needs the monthly figure; $100/day × 31 = 3,100 is above the cap (SQL L45: 'capped at $3,000 a month'); (b) a wrong run could put 0 — rejected")
row(p="P46", span=SP_CALL, oe=[11, 21, 101], fact="ddprod_cost", what="the DD production account row's monthly cost", final="$140 a month",
    vals="`$140` (SQL L51, 03:10Z; superseded ~$1k and 300, C0ADGSZKR3R/1770680984.725779, C0ADGSZKR3R/1770682219.100789, SQL L157, the draft) · F10, F11", dis="T3", kind="multi-source: the later DM over #winddown, Linear and the draft", band=5, dec="T3",
    dup="ddprod_cost ×1", valid="DD production account — 140", idle="no DD production account row at $140 → REJECT",
    cr="(a) a valid run could write '$140 from March' — accepted; (b) a wrong run could write $300 or $1,000 — rejected")
row(p="P47", span=SP_CALL, oe=[4, 16, 101], fact="support_step", what="the Domino Delights player support row's next step", final="a support build (support URL or another in-app contact) through App Review",
    vals="`Feb 28` (before Feb 28; any date Feb 15–27, 'by Feb 28' or 'before Feb 28', risk 8; SQL L100, L237, C0ADGSZKR3R/1770789534.434749) · F53, F16, F17, F4", dis="T2", amb="risk 8 → a date window",
    kind="multi-source: the later App Review mail over the Linear 'done' and the merged PR", band=5, dec="T2", dup="support_step ×1", valid="next step 'resubmit DD with a support URL in the app'",
    idle="no Domino Delights player support row with a support-build step → REJECT", af="none · over-specific risk: wording — any build, release or resubmission with an in-app contact",
    cr="(a) a valid run could write 'fix the App Review rejection (add a support link)' — accepted; (b) a wrong run could write 'done' or 'none' as the step — rejected: App Review rejected the build (SQL L100)")
row(p="P66", span=SP_CALL, oe=[4, 6, 9, 101], fact="support_by", what="the Domino Delights player support row's date", final="no later than Feb 28 (Helpshift stops; the item keeps its own deadline)",
    vals="Feb 28 ('before Feb 28th', #winddown C0ADGSZKR3R/1770789534.434749, SQL L237; card SQL L56 'Anything that already has its own deadline keeps it'; any date Feb 15–28, 'by Feb 28' or 'before Feb 28', risk 8) · F53, F17, F4", dis="T2", amb="risk 8 → a date window",
    kind="interpretation: the card's own-deadline rule applied to Helpshift's date", band=3, dec="T2", dup="support_by ×1", valid="By: Feb 28 (or 'before Feb 28')",
    idle="no Domino Delights player support row dated by Feb 28 → REJECT", af="none · over-specific risk: the date — accepts the window, in the By cell or the step text",
    cr="(a) a valid run could write 'Feb 27' or put the date in the step text — accepted; (b) a wrong run could give Mar 1 (b2) — rejected: the item has its own deadline (SQL L56)")
row(p="P48", span=SP_CALL, oe=[15, 101], fact="layer_step", what="a step to get Combo Fighter's concept art out of layer.ai", final="a step to pull (export, download or save) Combo Fighter's concept art out of layer.ai, on the layer.ai or the Combo Fighter row",
    vals="`Mar 3` (before or by Mar 3; SQL L48; C09UHHN6PFZ/1770837702.167889; on the layer.ai or the Combo Fighter row) · F18, F45", dis="T9 → ENG-2454 says only 'cancelled it on the 11th'", amb="risk 2 → either row",
    kind="multi-source: the seeded thread reply over ENG-2454's bare 'cancelled'", band=5, dec="T9", dup="layer_step ×1", valid="layer.ai row 'export CF concept art'",
    idle="no plan step to pull Combo Fighter's concept art out of layer.ai → REJECT", af="none · over-specific risk: the row it sits on — either accepted",
    cr="(a) a valid run could put it on the Combo Fighter row — accepted (risk 2); (b) a wrong run could write 'cancelled, nothing to do' — rejected (SQL L48)")
row(p="P67", span=SP_CALL, oe=[15, 101], fact="layer_by", what="the date on the layer.ai art step", final="before Mar 3 (access ends March 3rd)",
    vals="Mar 3 ('we have access until March 3rd', C09UHHN6PFZ/1770837702.167889; 'before then', SQL L48; by or before Mar 3, any earlier date from Feb 15) · F18, F45", dis="T9",
    kind="interpretation: the access date from the root post applied to the step", band=3, dec="T9", dup="layer_by ×1", valid="By: before Mar 3",
    idle="no layer.ai art step dated by Mar 3 → REJECT", af="none · over-specific risk: the date — any date by Mar 3, in the By cell or the step text",
    cr="(a) a valid run could write 'Mar 2' or 'by Mar 3' — accepted; (b) a wrong run could write 'by Mar 31' or leave the step undated — rejected")
row(p="P49", span=SP_CALL, oe=[4, 101], fact="github_step", what="the GitHub row's next step", final="the repos transfer once the data is sold or delivered",
    vals="`ENG-2449` ('then the repos transfer', SQL L189; 'till the data's delivered', SQL L68) · F40, F12", kind="interpretation: two records on one step", band=3, dec="—", dup="github_step ×1",
    valid="GitHub — 'repos transfer after the data sale'", idle="no GitHub row with a transfer step after the data is delivered → REJECT",
    cr="(a) a valid run could write 'stays HG's till the data is delivered' — the same step, accepted; (b) a wrong run could move the repos now — rejected")
row(p="P50", span=SP_CALL, oe=[13, 21, 101], fact="cfstacks_cost", what="the CF backend and auth stacks row's monthly cost", final="$62 a month",
    vals="`$62` (SQL L92 04:20Z; superseded `$95` SQL L173 00:58Z) · F14", dis="T4", kind="multi-source: the later mail over the Linear comment", band=5, dec="T4", dup="cfstacks_cost ×1",
    valid="CF backend and auth stacks — 62", idle="no CF backend and auth stacks row at $62 → REJECT",
    cr="(a) a valid run could write '$62 (was $95)' — accepted; (b) a wrong run could keep $95 (b5) — rejected")
row(p="P51", span=SP_CALL, oe=[4, 101], fact="appsflyer_cost", what="the AppsFlyer row's monthly cost", final="$0 (free tier)", vals="`ENG-2451` 0 or free ('free up to 15K installs', SQL L197) · F42, F21",
    kind="lookup", band=1, dec="—", dup="appsflyer_cost ×1", valid="AppsFlyer — 0 (free tier)", idle="no AppsFlyer row at $0 → REJECT",
    cr="(a) a valid run could write 'free' — accepted; (b) a wrong run could price a paid plan — rejected")
row(p="P52", span=SP_CALL, oe=[12, 21, 101], fact="md_cost", what="the Metabase and dbt monthly cost", final="$100 each ($200 on one combined row)",
    vals="`$100`, `$200` (SQL L68; superseded `~300`, SQL L181 and the draft) · F12, F13", dis="T5", kind="multi-source: the later mail over Linear and the draft", band=5, dec="T5", dup="md_cost ×1",
    valid="Metabase 100, dbt 100 (or Metabase + dbt 200)", idle="no Metabase and dbt cost of $100 each or $200 together → REJECT",
    cr="(a) a valid run could use one 'Metabase + dbt' row at 200 — accepted (§4b); (b) a wrong run could keep ~300 — rejected")
row(p="P53", span=SP_CALL, oe=[12, 101], fact="github_cost", what="the GitHub row's monthly cost", final="$48 a month", vals="`$48` ('back to the $48 team plan', SQL L68) · F12, F40",
    kind="lookup: one record", band=1, dec="T5", dup="github_cost ×1", valid="GitHub — 48", idle="no GitHub row at $48 → REJECT",
    cr="(a) a valid run could write 0 for the LLC as Arthur pays — the column is the item's monthly cost, and the shares need it (SQL L80 'including what one of us already pays'); (b) a wrong run could omit GitHub — rejected")
row(p="P54", span=SP_CALL, oe=[12, 101], fact="github_call", what="who pays the GitHub row", final="Arthur (Blake) himself", vals="`ENG-2449` paid by Arthur (SQL L68) · F40, F12", amb="risk 4",
    kind="interpretation", band=3, dec="T5", dup="github_call ×2 (with P9)", valid="GitHub — paid by Arthur", idle="no GitHub row paid by Arthur → REJECT",
    cr="(a) a valid run could write 'HG (Arthur pays)' — names Arthur, accepted; (b) a wrong run could have HG pay — rejected")
row(p="P55", span=SP_CALL, oe=[5, 21, 101], fact="vendor_cost", what="the Playable vendor row's monthly cost", final="no monthly cost (0 or blank, not $3,750)",
    vals="`$3,750` kept out (one-off, SQL L289; doc SQL L15) · F65, F24", dis="T10", kind="interpretation: the monthly-only rule", band=3, dec="T10", dup="vendor_cost ×1",
    valid="Playable vendor — 0 (one-off)", idle="no Playable vendor row on the plan sheet → REJECT",
    cr="(a) a valid run could leave the cost cell blank with 'one-off' — accepted; (b) a wrong run could put $3,750 or $1,250 a month — rejected")
row(p="P56", span=SP_CALL, oe=[6, 101], fact="cf_by", what="the Combo Fighter row's By", final="when Sunset's sale closes", vals="`ENG-2438` (card: 'Anything that comes through Sunset's sale moves when the sale closes', SQL L56) · F29, F4",
    kind="interpretation: the card's rule", band=3, dec="—", grp="D4 sample (edge)", dup="cf_by ×1", valid="By: when the sale closes", idle="no Combo Fighter row dated to the sale's close → REJECT",
    cr="(a) a valid run could write 'Mar 1' — the card gives sale items the sale's close (SQL L56), rejected; (b) a run writing 'at the sale' passes — same rule")
row(p="P57", span=SP_CALL, oe=[6, 101], fact="ddprod_by", what="the DD production account row's By", final="Mar 1 (by March 1; 'end of February' also accepted)", vals="`Mar 1` (card: 'everything else moves by March 1', SQL L56) · F32, F4",
    kind="interpretation", band=3, dec="—", grp="D4 sample (ordinary)", dup="ddprod_by ×1", valid="By: Mar 1", idle="no DD production account row dated Mar 1 → REJECT",
    af="none · over-specific risk: date form — 'March 1', '3/1', '2026-03-01' accepted",
    cr="(a) a valid run could write 'end of Feb' — it meets 'by March 1' (SQL L56), accepted; (b) a wrong run could write 'when the sale closes' — rejected: the account is not in Sunset's sale")
row(p="P58", span=SP_ASK, oe=[8, 23, 101], fact="even_share", what="the three monthly shares on the plan sheet", final="$1,150 each (Arthur's may show as $902 cash plus the $248 he already pays)",
    vals="`$1,150`, `$902`, `$248` (split mail SQL L80: 'put the three shares on the sheet per month'; 3,450 / 3) · F67, F7", dis="T1, T12", amb="risk 3 → with or without the cash split",
    kind="multi-source: every cost line, the VO line and the split rule", band=5, dec="T1, T12", dup="even_share ×2 (with P64)", valid="shares: 1,150 each",
    idle="no plan sheet shares of $1,150 a month → REJECT",
    cr="(a) a valid run could show Arthur as '$902 + $248 carried' — accepted (risk 3); (b) a wrong run could give $150 (no VO, b1) or 1,067 (on 3,202) or Arthur 1,150 cash on top of 248 — rejected")

# ------------------------------------------------------------------ Shares
row(p="P59", span=SP_SHARE, oe=[19, 102], fact="share_leonard", what="the plan sheet shared with Leonard", final="leonard.hayes@harmonygames.co can open it (any role)",
    vals="`Co-founder & CEO` (Contacts /contacts/169: leonard.hayes@harmonygames.co; writer, commenter or reader) · F27", kind="lookup", band=1, dec="—", dup="share_leonard ×1",
    valid="shared with leonard.hayes@harmonygames.co as reader", idle="the plan sheet is not shared with leonard.hayes@harmonygames.co → REJECT",
    cr="(a) a valid run could share as commenter — any role accepted (§4b); (b) a wrong run could share Leonard's draft instead — rejected: the new plan sheet")
row(p="P60", span=SP_SHARE, oe=[19, 103], fact="share_arthur", what="the plan sheet shared with Arthur", final="arthur.blake@harmonygames.co can open it (any role)",
    vals="`Co-founder & CTO` (Contacts /contacts/168: arthur.blake@harmonygames.co; 'Blake' in the prompt) · F27", kind="lookup", band=1, dec="—", dup="share_arthur ×1",
    valid="shared with arthur.blake@harmonygames.co", idle="the plan sheet is not shared with arthur.blake@harmonygames.co → REJECT",
    cr="(a) a valid run could read 'Blake' as a first name and search — Contacts resolve it to Arthur Blake (/contacts/168); (b) a wrong run could share with a different Blake — rejected by the address")

# ------------------------------------------------------------------ Reply
row(p="P61", span=SP_LINK, oe=[1, 100, 104], fact="reply_link", what="the link to the plan sheet in the reply in Leonard's DM thread", final="the thread reply under D04UP2L3E3S/1770961200.890407 links the new sheet",
    vals="`1770961200.890407` (thread_ts; DM D04UP2L3E3S, SQL L54) · F1, F28", kind="lookup", band=1, dec="—", dup="reply_link ×1",
    af="none · over-specific risk: the link form — any Drive/Sheets URL or file id of the new sheet",
    valid="reply in the thread with the sheet's URL", idle="no reply in the thread of Leonard's Thursday DM linking the sheet → REJECT",
    cr="(a) a valid run could paste the Sheets URL rather than a Drive URL — both accepted; (b) a wrong run could link Leonard's draft — rejected: the new plan sheet")
row(p="P62", span=SP_DO, oe=[20, 104], fact="dd_call", what="Domino Delights in the reply in Leonard's DM thread", final="the reply says the LLC takes Domino Delights",
    vals="`183.11` vs `$140` (as P38) · F30, F9, F10, F1", dis="T3, T8", kind="interpretation: the reply states the call", band=3, dec="T3, T8", dup="dd_call ×2 (with P38)",
    valid="'I'd bring CF and DD into the LLC'", idle="no reply in the thread saying the LLC takes Domino Delights → REJECT",
    cr="(a) a valid run could say 'DD comes over' — accepted as taking it; (b) a wrong run could say 'only CF' — rejected")
row(p="P63", span=SP_DO, oe=[20, 104], fact="zm_call", what="Zombie Match in the reply in Leonard's DM thread", final="Zombie Match stays with HG (or the LLC's games are named as Combo Fighter and Domino Delights only)",
    vals="`0.00` (as P39) · F31, F9, F1", dis="T8", kind="interpretation", band=3, dec="T8", dup="zm_call ×2 (with P39)",
    valid="'ZM stays with HG' or 'take CF and DD only'", idle="no reply in the thread leaving Zombie Match with HG → REJECT",
    af="none · over-specific risk: a reply naming only the games it takes — accepted when it says 'only'",
    cr="(a) a valid run could name only the games it takes — accepted with 'only' / 'just'; (b) a wrong run could take all three — rejected")
row(p="P64", span=SP_COST, oe=[8, 23, 104], fact="even_share", what="what it costs each of them a month, in the reply in Leonard's DM thread", final="$1,150 each (Arthur's $248 counted in his; $902 cash also accepted)",
    vals="`$1,150` (`$902` cash + `$248` accepted; SQL L80) · F67, F7, F1", dis="T1, T12", amb="risk 3", kind="multi-source: all cost lines, the VO line and the split rule", band=5, dec="T1, T12",
    dup="even_share ×2 (with P58)", valid="'$1,150 a month each (Arthur: $902 cash + his $248)'", idle="no reply in the thread giving $1,150 a month each → REJECT",
    cr="(a) a valid run could give only '$1,150 each' — accepted (risk 3); (b) a wrong run could have Arthur pay $1,150 cash on top of $248, or give $150 / 1,067 — rejected")

# ------------------------------------------------------------------ Process
row(p="P65", span=SP_REPLY, oe=[24, 101, 102, 103, 104], fact="reply_last", what="the reply comes after the Linear, sheet and sharing writes", final="the thread reply is the last write: no Linear, sheet or Drive write after it",
    vals="`1770961200.890407` reply after OEs 24–103 ('When you're done … Then reply') · F1, F66", cat="Process candidate → C1", phr="yes — 'Then reply'",
    kind="lookup: one ordering in the run", band=1, dec="—", dup="reply_last ×1 (one ordering ask = one Process row)",
    valid="reply posted after every Linear, sheet and share write", idle="no reply in Leonard's DM thread after the writes → REJECT",
    cr="(a) a valid run could post a short 'working on it' first and the answer last — the row grades the reply that answers, after the writes; (b) a wrong run replying before sharing — rejected")

# ------------------------------------------------------------------ probe literals: only distinctive acceptance values
LITS = {
    "P1": ["$3,000"], "P2": ["$3,000"], "P3": ["$3,000"], "P4": ["$3,000"], "P5": ["ENG-2438", "ENG-2474"],
    "P6": ["ENG-2462"], "P7": ["ENG-2453"], "P8": ["ENG-2472"], "P9": ["ENG-2449"], "P10": ["ENG-2474"], "P11": ["ENG-2457"],
    "P12": ["ENG-2438"], "P13": ["ENG-2438"], "P14": ["ENG-2439"], "P15": ["ENG-2439"], "P16": ["ENG-2441"], "P17": ["ENG-2441"],
    "P18": ["ENG-2445"], "P19": ["ENG-2445"], "P20": ["ENG-2451"], "P21": ["ENG-2451"], "P22": ["ENG-2462"], "P23": ["ENG-2462"],
    "P24": ["ENG-2447"], "P25": ["ENG-2448"], "P26": ["ENG-2449"], "P27": ["ENG-2440", "ENG-2474"], "P28": ["ENG-2440"],
    "P29": ["ENG-2453"], "P30": ["ENG-2472"], "P31": ["ENG-2457"], "P32": ["ENG-2442"], "P33": ["ENG-2470"],
    "P34": ["d_9f7ba94f7526d54d8482ba"], "P35": ["Monthly cost", "Paid by", "Next step"],
    "P36": ["ENG-2438", "ENG-2439", "ENG-2441", "ENG-2445", "ENG-2451", "ENG-2462"], "P37": ["ENG-2438"], "P38": ["183.11", "$140"],
    "P39": ["ENG-2440"], "P40": ["$248"], "P41": ["ENG-2472"], "P42": ["ENG-2453"], "P43": ["ENG-2461"], "P44": ["ENG-2457"],
    "P45": ["$3,000"], "P46": ["$140"], "P47": ["ENG-2462"], "P66": ["Feb 28"], "P48": ["ENG-2454"], "P67": ["Mar 3"], "P49": ["ENG-2449"], "P50": ["$62"], "P51": ["ENG-2451"],
    "P52": ["ENG-2447", "ENG-2448"], "P53": ["$48"], "P54": ["ENG-2449"], "P55": ["ENG-2474"], "P56": ["ENG-2438"], "P57": ["Mar 1"],
    "P58": ["$1,150", "$902", "$248"], "P59": ["d_9f7ba94f7526d54d8482ba"], "P60": ["d_9f7ba94f7526d54d8482ba"],
    "P61": ["1770961200.890407"], "P62": ["183.11", "$140"], "P63": ["ENG-2440"], "P64": ["$1,150", "$902", "$248"], "P65": ["1770961200.890407"],
}
assert set(LITS) == {r["p"] for r in R}
for r in R:
    r["vals"] = " ".join(f"`{x}`" for x in LITS[r["p"]]) + " — " + r["vals"].replace("`", "")

# ------------------------------------------------------------------ check-mode revision 1 (blind /rubric review + own check, 2026-11-06)
R[:] = [r for r in R if r["p"] != "P10"]          # vendor comment dropped: six samples in the comment group; T10 stays on P55
row(p="P68", span=SP_LAYOUT, oe=[3, 14, 101], fact="sheet_rows", what="the number of item rows on the plan sheet", final="exactly 38 (37 issues + the VO campaign; 37 with Metabase + dbt on one row)",
    vals="`ENG-2438` `ENG-2474` — 38 item rows (37 issues ENG-2438 to ENG-2474 + the VO line, C09UHHN6PFZ/1770938400.370665; 37 with a combined Metabase + dbt row as on the draft, SQL L23) · F2, F15, F5",
    kind="comparison: the whole item list against the sheet (output volume)", band=3, dec="T1", grp="D3 volume", dup="sheet_rows ×1",
    valid="38 item rows plus header and share lines", idle="no plan sheet with 38 item rows → REJECT",
    cr="(a) a valid run could merge Metabase and dbt as the draft does — 37 accepted; (b) a wrong run could list only the LLC rows or drop 20 HG rows — rejected by the count")
row(p="P69", span=SP_LEAVE, oe=[4, 20, 27], fact="dd_call", what="the call in the comment on ENG-2439 Domino Delights", final="the LLC takes it",
    vals="`ENG-2439` `183.11` `$140` — LLC (take test: January 183.11 vs $140 hosting, SQL L15, L51) · F30, F9, F10", dis="T3, T8, T11",
    kind="multi-source: the warehouse revenue against the DM's current hosting under the doc's test", band=5, dec="T3, T8", grp="D1 direct (core)", dup="dd_call ×2 (with P38)",
    valid="comment 'LLC — January's 183.11 covers its $140 hosting'", idle="no comment on ENG-2439 giving the LLC call → REJECT",
    cr="(a) a valid run could write 'comes over with CF' — accepted as the LLC call; (b) a wrong run could write 'stays with HG' on the stale ~$1k — rejected")
row(p="P70", span=SP_LEAVE, oe=[4, 20, 28], fact="zm_call", what="the call in the comment on ENG-2440 Zombie Match", final="stays with HG",
    vals="`ENG-2440` — HG (0.00 January revenue; the doc's test, SQL L15) · F31, F9", dis="T8",
    kind="multi-source: the warehouse revenue under the doc's test, over the Monday notes", band=5, dec="T8", grp="D1 direct (core)", dup="zm_call ×2 (with P39)",
    valid="comment 'stays with HG: 0.00 in January'", idle="no comment on ENG-2440 giving the HG call → REJECT",
    cr="(a) a valid run could write 'goes in Sunset's sale' — accepted as HG; (b) a wrong run could take it with CF per the notes — rejected")
row(p="P71", span=SP_REPLY, oe=[1, 104], fact="reply_thread", what="where the reply is posted", final="a reply in the thread under Leonard's DM message (thread_ts 1770961200.890407)",
    vals="`1770961200.890407` — thread_ts of Leonard's DM D04UP2L3E3S/1770961200.890407 (SQL L54) · F1", kind="lookup", band=1, dec="—", dup="reply_thread ×1",
    valid="slack reply with thread_ts 1770961200.890407", idle="no reply in that thread → REJECT",
    cr="(a) a valid run could reply in the thread with Leonard's user id as the channel — the platform files it in the DM thread (b5); (b) a wrong run posting top-level in the DM — rejected by the thread_ts")
row(p="P72", span=SP_LAYOUT, oe=[11, 101], fact="ddprod_assignee", what="the Owner of the DD production account row", final="Arthur Blake",
    vals="`ENG-2441` — Owner Arthur Blake (Arthur runs the account, SQL L51; draft column Owner, SQL L23) · F32, F10, F5", kind="lookup", band=1, dec="—", grp="D5 sample (ordinary)", dup="ddprod_assignee ×2 (with P17)",
    valid="Owner: Arthur (or Blake)", idle="no DD production account row with Owner Arthur → REJECT",
    cr="(a) a valid run could write 'Blake' as on the draft — accepted; (b) a wrong run could put Leonard, who gave the old figure — rejected")
row(p="P73", span=SP_LAYOUT, oe=[14, 101], fact="vo_assignee", what="the Owner of the VO campaign row", final="Leonard Hayes",
    vals="`$3,000` — Owner Leonard Hayes (on his card, SQL L45) · F15, F66, F5", dis="T1", kind="lookup", band=1, dec="T1", grp="D5 sample (edge: not a Linear item)", dup="vo_assignee ×2 (with P3)",
    valid="Owner: Leonard", idle="no VO campaign row with Owner Leonard → REJECT",
    cr="(a) a valid run could write 'Leonard (card)' — accepted; (b) a wrong run could put Robert as CF's owner — rejected: Leonard moves his card")
row(p="P76", span=SP_CALL, oe=[12, 21, 101], fact="dbt_cost", what="the dbt row's monthly cost", final="$100 a month (or $200 with Metabase on one combined row)",
    vals="`ENG-2448` `$248` — 100 ('dbt is $100', SQL L68; superseded ~300 SQL L181, the draft) · F12, F39", dis="T5", kind="multi-source: the later mail over Linear and the draft", band=5, dec="T5", dup="dbt_cost ×1",
    valid="dbt — 100 (or Metabase + dbt 200)", idle="no dbt cost of $100 (or a combined $200) → REJECT",
    cr="(a) a valid run could merge it with Metabase at 200 — accepted; (b) a wrong run could keep ~300 or put 0 — rejected")
UPD = {
    "P5": dict(what="a comment stating a call on every one of the 37 existing issues", final="each of the 37 issues carries a new comment from the Agent that states its call"),
    "P15": dict(vals="`ENG-2439` — Leonard Hayes ('I'll handle it with Sunset' on ENG-2439; Leonard's #prototype post C09UHHN6PFZ/1770844309.583109 'Domino Delights is with boombit') · F30, F25"),
    "P28": dict(band=5, kind="multi-source: the warehouse revenue under the doc's take test, over the Monday notes (same work as the Domino Delights call)"),
    "P36": dict(final="exactly 7 LLC rows (the 6 issues and the VO campaign), apart from the Metabase, dbt and GitHub rows Arthur pays himself"),
    "P39": dict(band=5, kind="multi-source: the warehouse revenue under the doc's take test (same work as Domino Delights)"),
    "P40": dict(band=1, kind="lookup: Arthur's mail says 'github, dbt and metabase bill to my Kub card'"),
    "P45": dict(band=3, kind="interpretation: the monthly cap against the $100/day budget, from one thread reply"),
    "P48": dict(band=3, kind="interpretation: one thread reply adds the step ENG-2454 lacks"),
    "P49": dict(band=1, kind="lookup: ENG-2449's own comment gives the step"),
    "P52": dict(fact="metabase_cost", what="the Metabase row's monthly cost", final="$100 a month (or $200 with dbt on one combined row)"),
    "P58": dict(final="$1,150 each, Arthur's counting the $248 he already pays (or $902 cash plus that $248); Arthur at $1,150 cash on top of $248 fails"),
    "P62": dict(band=5, fact="dd_reply", kind="multi-source: the reply states the take-test call (warehouse, DM, doc)"),
    "P63": dict(band=5, fact="zm_reply", kind="multi-source: the reply states the take-test call (warehouse, doc)"),
}
for r in R:
    r.update(UPD.get(r["p"], {}))
ORDER = ["P1", "P2", "P3", "P4", "P5", "P69", "P70", "P6", "P7", "P8", "P9", "P11", "P12", "P13", "P14", "P15", "P16", "P17", "P18", "P19",
         "P20", "P21", "P22", "P23", "P24", "P25", "P26", "P27", "P28", "P29", "P30", "P31", "P32", "P33", "P34", "P35", "P68", "P36", "P37",
         "P38", "P39", "P40", "P41", "P42", "P43", "P44", "P45", "P46", "P47", "P66", "P48", "P67", "P49", "P50", "P51", "P52", "P76", "P53",
         "P54", "P55", "P56", "P57", "P72", "P73", "P58", "P59", "P60", "P71", "P61", "P62", "P63", "P64", "P65"]
pos = {p: i for i, p in enumerate(ORDER)}
assert set(pos) == {r["p"] for r in R}, set(pos) ^ {r["p"] for r in R}
R.sort(key=lambda r: pos[r["p"]])
