#!/usr/bin/env python3
"""Filter your pulled notes down to YOUR pitch meetings, then extract YOUR questions.

Run pull.py first. Then:
    YOUR_DOMAIN=yourfirm.com python3 extract.py

Writes ./lens-data/my_questions.json ([{title, date, questions:[...]}]) and prints a drop log
(what was excluded and why — never filter silently).

Tune the CONFIG block for your firm. The defaults encode the filtering logic that worked in testing:
  - keep pitches (folder OR company/person-name title OR an external attendee)
  - drop internal/admin, personal, and PARTNER-LED / co-attended meetings (they pollute the lens)
  - extract only your side of the transcript (speaker.source == "microphone"), questions only
"""
import json, os, re, glob

# ---------------- CONFIG: edit for your firm ----------------
YOUR_DOMAIN = os.environ.get("YOUR_DOMAIN", "yourfirm.com").lower()  # your firm's email domain
PITCH_FOLDER_NAMES = {"pitches", "dealflow", "deal flow", "due diligence"}  # lowercase folder names
# Names/emails of your colleagues — if one is on the call (besides you), it's partner-led → drop.
COLLEAGUES = set()  # e.g. {"partner@yourfirm.com", "colleague@yourfirm.com"}
INTERNAL_TITLE = re.compile(r"\b(team (meeting|sync|video)|investment team|all ?hands|standup|stand-up|"
                            r"1:1|weekly|offsite|watch party|commute|busy \(via|sync\b)\b", re.I)
PERSONAL_TITLE = re.compile(r"\b(birthday|doctor|surgery|school|kindergarten|admission|estate|family|"
                            r"dentist|vacation|dinner with|lunch with)\b", re.I)
MIN_Q_WORDS = 4
GREETING = re.compile(r"^(hey|hi|hello|how are you|how's it going|how you doing|can you hear|are you in)\b", re.I)
# ------------------------------------------------------------

NOTES = glob.glob(os.path.join("lens-data", "notes", "*.json"))

def emails(d):
    return [(a.get("email") or "").lower() for a in (d.get("attendees") or []) if a.get("email")]

def has_external(es):
    return any("@" in e and e.split("@")[-1] != YOUR_DOMAIN for e in es)

def internal_attendees(es):
    return [e for e in es if e.endswith("@" + YOUR_DOMAIN)]

def looks_like_name_or_company(title):
    # crude: a short title that's mostly a proper noun / "X <> Y" / "Name / Name"
    t = title.strip()
    return bool(re.search(r"[<>/]|\bbetween\b", t)) or (1 <= len(t.split()) <= 5 and t[:1].isupper())

def is_pitch_and_yours(d):
    title = (d.get("title") or "")
    folders = {(m.get("name") or "").lower() for m in (d.get("folder_membership") or [])}
    es = emails(d)
    if PERSONAL_TITLE.search(title): return (False, "personal")
    if INTERNAL_TITLE.search(title): return (False, "internal/admin")
    # partner-led / co-attended: a colleague (besides you) on the call
    extra_internal = [e for e in internal_attendees(es) if e in COLLEAGUES]
    if extra_internal: return (False, "partner-led/co-attended")
    if len(internal_attendees(es)) > 1 and not COLLEAGUES:
        return (False, "likely co-attended (>1 internal attendee)")
    if folders & PITCH_FOLDER_NAMES: return (True, "pitch-folder")
    if has_external(es): return (True, "external-attendee")
    if looks_like_name_or_company(title): return (True, "name/company title")
    return (False, "unclear/internal")

def my_questions(d):
    turns, cur = [], []
    for t in (d.get("transcript") or []):
        if (t.get("speaker") or {}).get("source") == "microphone":
            cur.append((t.get("text") or "").strip())
        elif cur:
            turns.append(" ".join(cur)); cur = []
    if cur: turns.append(" ".join(cur))
    out = []
    for turn in turns:
        for s in re.split(r"(?<=[.?!])\s+", turn):
            s = s.strip()
            if s.endswith("?") and len(s.split()) >= MIN_Q_WORDS and not GREETING.match(s):
                out.append(s)
    return out

kept, dropped = [], []
for f in NOTES:
    d = json.load(open(f))
    ok, why = is_pitch_and_yours(d)
    title = d.get("title") or "?"
    if not ok:
        dropped.append((why, title)); continue
    qs = my_questions(d)
    if qs:
        kept.append({"title": title, "date": (d.get("created_at") or "")[:10], "questions": qs})

json.dump(kept, open(os.path.join("lens-data", "my_questions.json"), "w"), indent=2)
print(f"KEPT {len(kept)} pitch meetings, {sum(len(m['questions']) for m in kept)} of your questions")
print(f"DROPPED {len(dropped)}:")
from collections import Counter
for why, n in Counter(w for w, _ in dropped).most_common():
    print(f"  {n:>4}  {why}")
print("\n→ lens-data/my_questions.json  (hand this + your essays to scripts/distill-prompt.md)")
