#!/usr/bin/env python3
"""Draft mode: write <task>/09_Rubrics.json (the Criteria Builder shape: title, category, weight, justification,
evidence) from plan/rubric/rows.json, the rows behind 09_Rubric_Writing_Plan.md (one criterion per plan row, same
order, so R<n> = P<n>).

Title = the plan's draft title (a few rewordings below, each with its reason). Weight = the plan's band (kind of
work). Justification = kind of work + reason. Evidence = the records holding each expected value (with Brian's full
note where the plan quotes a shortened one), what is accepted, what is rejected, and the OE steps that reach it.
Internal ids (F-n, ledger T-n, probe forms) stay in the plan and never reach the export."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TASK = WF.parent
sys.path.insert(0, str(WF / "oe_gen"))
import model as O  # noqa: E402

rows = json.loads((HERE / "rows.json").read_text())
BY_TICKET = {l["ticket"]: l for l in O.BY.values()}

# draft-title rewordings (plan titles stand otherwise)
RETITLE = {
    # the plan's "cannot use … yet" reads as a negation, and "says … is held back" would reject a brief that answers
    # "what they can use for sound" with the usable list alone; grade the usable list instead, which accepts both forms
    "b_held_Rocket sound": "The Agent's brief gives PlayableX a list of usable sounds that excludes the Rocket sound",
    "b_held_Explosion sound": "The Agent's brief gives PlayableX a list of usable sounds that excludes the Explosion sound",
    # the volume row of the move template names the template and the parent ticket, never a ticket range
    # (a count joined to a range of targets is what the platform lint calls bundled_writes)
    "move_volume": "The Agent moves exactly 49 of the tickets under Brian's pack ticket DES-313 to Todo, one for each row its hand-off list marks Owed",
    # the eval lint reads "<n> lines" / "one for each line" as a text-length format (format_lock); these count pack-list
    # line items, so say so ("line item" is outside its text units)
    "sheet_volume": "The Agent's hand-off list has 96 data rows, one for each row of Brian's pack list",
    "dm_Owed": "The Agent tells Frederick in their DM that the Owed count is 49",
    "dm_Ready": "The Agent tells Frederick in their DM that the Ready count is 39",
    "dm_Delivered": "The Agent tells Frederick in their DM that the Delivered count is 8",
}
ACCEPT = {   # rows whose accepted forms the retitle widened
    "b_held_Rocket sound": "'Sounds you can use: Matching, Success and Failure' with the Rocket sound absent from that list, or the same "
                           "list with the Rocket sound named as coming later once we have our own version",
    "b_held_Explosion sound": "'Sounds you can use: Matching, Success and Failure' with the Explosion sound absent from that list, or the "
                              "same list with the Explosion sound named as coming later once we have our own version",
}
EXTRA_REJECT = {
    "b_held_Rocket sound": "a usable-sound list that includes the Rocket sound",
    "b_held_Explosion sound": "a usable-sound list that includes the Explosion sound",
}
KIND = {"lookup": "Lookup", "interpretation": "Interpretation", "calculation": "Calculation", "comparison": "Comparison",
        "multi-source": "Multi-source", "tracing": "Tracing", "limited reconciliation": "Limited reconciliation"}


ASK = f"Frederick's ask {O.ASK['id']}"
# rows whose Values cell holds a destination or a derivation instead of a source record
EXTRA_SRC = {
    "brief_doc": f"{ASK} ('Brief as a doc and the hand-off list as a sheet, both in your Drive')",
    "sheet_doc": f"{ASK} ('Brief as a doc and the hand-off list as a sheet, both in your Drive')",
    "post_brief": f"{ASK} ('post both links in the PlayableX channel so they know what's still coming from us')",
    "post_list": f"{ASK} ('post both links in the PlayableX channel so they know what's still coming from us')",
    "move_volume": (f"the notes {O.NOTES_ID} ('An Owed line's ticket goes to Todo with a comment saying what is owed and who has it. "
                    f"Leave the Delivered and Ready ones as they are.'); the 96 lines of Brian's pack list {O.PACK_ID}, each "
                    f"line's State decided from its ticket note and the records that overtake it"),
}
COUNT_SRC = (f"{ASK} ('give me the count for each state here'); the 96 lines of Brian's pack list {O.PACK_ID} (Delivered "
             f"{O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}), each line's State decided from "
             f"its ticket note and the records that overtake it")
DEST = {"post_brief": f"a message in the PlayableX channel {O.VENDOR_CH}", "post_list": f"a message in the PlayableX channel {O.VENDOR_CH}",
        "dm_Owed": f"Julia's reply in the DM with Frederick {O.DM_FRED}", "dm_Ready": f"Julia's reply in the DM with Frederick {O.DM_FRED}",
        "dm_Delivered": f"Julia's reply in the DM with Frederick {O.DM_FRED}"}


def own_line(r):
    """The pack-list line a row is about (its ticket in the title), or None."""
    m = [t for t in re.findall(r"DES-\d+", r["title"]) if t != O.PACK_TICKET]
    return BY_TICKET.get(m[0]) if m else None


def full_note(text, l):
    """The plan quotes a line's note shortened; give the whole note, attributed to Brian's comment on that ticket."""
    if not l:
        return text
    for n in (70, 60):
        short = f"note '{l['note'][:n]}'"
        if short in text:
            return text.replace(short, f"Brian's note on {l['ticket']} ('{l['note']}')")
    return text


def clean(s):
    s = s.replace("`", "").replace("the the ", "the ")
    s = re.sub(r"\s*\(brief §4b\)|\s*\(walked back, /oe round 1\)", "", s)     # pointers into our own working files
    s = re.sub(r"^the line's own note; ", "", s)                                 # the full note follows
    s = re.sub(r"\s+", " ", s).strip(" ·;")
    return s


def split_values(v, l):
    """(expected, sources, accepts, rejects) from a plan Values cell."""
    exp, src, acc, rej = [], [], [], []
    for seg in [x.strip() for x in v.split(" · ")]:
        if not seg or seg.startswith(("probe form", "recomputed", "DM ", "channel ")) or re.fullmatch(r"(F\d+)(, F\d+)*", seg):
            continue
        m = re.match(r"(accepts?|rejects?):\s*(.*)", seg)
        if m:
            body = m.group(2)
            if m.group(1).startswith("accept"):
                body, _, more = body.partition("; rejects: ")
                if more:
                    rej.append(more)
                for item in [x.strip() for x in body.split("; ")]:
                    (rej if item.startswith("not ") else acc).append(re.sub(r"^not ", "", item))
            else:
                rej.append(body)
            continue
        m = re.match(r"(sources?)\s+(.*)", seg)
        if m:
            src.append(full_note(m.group(2), l))
        elif seg.startswith("rule:"):
            src.append(full_note(seg[len("rule:"):].strip(), l))
        elif seg.startswith("owed:"):
            body, _, inner = seg[len("owed:"):].strip().partition(" (accept: ")
            exp.append("what is owed: " + body)
            for item in [x.strip(" )") for x in inner.split("; ") if x.strip(" )")]:
                (rej if item.startswith("not ") else acc).append(re.sub(r"^not ", "", item))
        elif seg.startswith("who:"):
            exp.append("who has it: " + seg[len("who:"):].strip())
        elif seg.startswith("template:"):
            exp.append(seg)
        else:
            exp.append(seg)
    return [clean(x) for x in exp], [clean(x) for x in src], [clean(x) for x in acc], [clean(x) for x in rej]


def distractor(d):
    """'ledger T2 (the note X) → Ready fails; T9 (…) → not graded' → 'the note X: Ready fails' (ungraded distractors dropped)."""
    if not d or d == "—":
        return ""
    keep = []
    for part in d.split("; "):
        part = re.sub(r"(ledger )?\bT\d+(/T\d+)*\s*", "", part).strip()
        if part.endswith("not graded"):
            continue
        part = re.sub(r"^\((.*)\)\s*→", r"\1 →", part)
        keep.append(part.replace(" → ", ": "))
    return clean("; ".join(keep))


out = []
for r in rows:
    title = RETITLE.get(r["tag"], r["title"])
    l = own_line(r)
    exp, src, acc, rej = split_values(r["values"], l)
    if r["tag"] in EXTRA_SRC:
        src.append(clean(EXTRA_SRC[r["tag"]]))
    if r["tag"].startswith("dm_"):
        src.append(clean(COUNT_SRC))
    kind, why = r["kind"]
    parts = []
    if exp:
        parts.append("Expected: " + "; ".join(exp) + ".")
    if r["tag"] in DEST:
        parts.append("Destination: " + DEST[r["tag"]] + ".")
    assert src, r["P"]
    parts.append(("Sources: " if len(src) > 1 else "Source: ") + "; ".join(src) + ".")
    accept = ACCEPT.get(r["tag"], r["valid"])
    if r["tag"] in EXTRA_REJECT:
        rej.append(EXTRA_REJECT[r["tag"]])
    if acc:
        accept += " (also accepted: " + "; ".join(acc) + ")"
    parts.append("Accept: " + clean(accept) + ".")
    rej = [x for x in rej if x]
    rej = [("an answer naming " + x) if r["tag"].startswith(("comment_", "o_")) and not x.startswith(("a ", "an ")) else x for x in rej]
    reject = [r["nothing"]] + rej + ([distractor(r["dist"])] if distractor(r["dist"]) else [])
    parts.append("Reject: " + "; ".join(clean(x) for x in reject if x) + ".")
    parts.append("OE " + ", ".join(str(n) for n in r["oes"]) + ".")
    out.append({
        "title": title,
        "category": r["cat"],
        "weight": r["band"],
        "justification": f"{KIND.get(kind, kind.capitalize())}: {why.rstrip('.')}.",
        "evidence": " ".join(parts),
    })

assert len(out) == len(rows) and all(o["weight"] in (1, 3, 5) for o in out)
assert all(o["category"] in ("Outcome", "Process") for o in out)
(TASK / "09_Rubrics.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(f"wrote 09_Rubrics.json: {len(out)} criteria · weight {sum(o['weight'] for o in out)}")
