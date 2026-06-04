# Founder Lens

> Pressure-test your pitch the way a VC actually would — before the real meeting.

Founder Lens reads your pitch deck and tells you the questions **Nikunj Kothari** (seed/Series A investor;
writes at [Balancing Act](https://writing.nikunjk.com)) would ask — and, more importantly, **what he'd find
missing.** It's distilled from 53 real pitch & diligence meetings plus his essays. It's one investor's lens,
made portable, so you can rehearse against it at 11pm instead of finding the holes live.

Example quotes are anonymized to a category (e.g. "AI-infra pitch") — no real companies or founders are named.

---

## What you get

Point it at a deck and it returns, in order:

1. **The questions he'd ask**, mapped to your slides.
2. **What your deck already answers well** — named slide by slide.
3. **The gaps** — where he'd push, and the red-flag patterns it spots (boil-the-ocean with no wedge,
   "category of one," a secret that's really category boilerplate, vision with no concrete next step).
4. **An insight-count check** — how many of the three unique insights (tech / market / GTM) you actually carry.
   One isn't enough anymore.
5. **Your weakest 3 claims + the follow-ups** he'd use to test whether a secret is earned or faked.
6. **The "dinner test"** — would this still be on his mind after the meeting? — and the single thing to fix first.

It leads with the *why* and the *how* (his actual frameworks and voice), not a generic product/market/tech
checklist.

---

## Install — Claude Code (recommended)

1. Clone or download this repo.
2. Copy the `founder-lens/` folder into your Claude skills directory:
   ```bash
   cp -r founder-lens ~/.claude/skills/
   ```
   (Or, to scope it to one project, drop it in that repo's `.claude/skills/` instead.)
3. Restart Claude Code.
4. Attach your deck (PDF) or paste an outline, and say something like:
   - "Review my deck."
   - "What would a VC ask about this pitch?"
   - "Pressure-test my pitch / poke holes in this."

   It will ask for your **stage** (pre-seed / seed / A) and **category** (e.g. AI infra, vertical SaaS, bio),
   then run the full review.

---

## Use in ChatGPT, Claude.ai, Cursor, or anything else

No skill system? It still works as pasted context:

1. Open `founder-lens/lens/principles.md` and `founder-lens/lens/question-bank.md` and paste both into the chat.
2. Then paste (or attach) your deck / outline and use this prompt:

   > You are reviewing my pitch deck using the lens in the two files above (`principles.md` =
   > how this investor reads a founder; `question-bank.md` = the questions he asks and how he asks them).
   > My stage is **[pre-seed/seed/A]** and category is **[e.g. AI infra]**.
   > Give me: (1) the questions he'd ask mapped to my deck, (2) what I already answer well, (3) the gaps
   > he'd push on, (4) an insight-count check across tech/market/GTM, (5) my weakest 3 claims with the
   > follow-up questions he'd use to break a faked secret, and (6) the "dinner test." Write it in his
   > voice — warm but direct, founder-to-founder, no VC jargon. Lead with the why and the how, not a
   > generic checklist.
   >
   > Here is my deck: [paste / attach]

---

## What's inside

```
founder-lens/
├── SKILL.md                 # the instructions (how the lens is applied to a deck)
└── lens/
    ├── principles.md        # how he reads a founder — the bar beneath the questions
    └── question-bank.md     # the questions, by theme, + "how he asks" (the texture)
```

Read `principles.md` first even on its own — it's a tight summary of what he's actually listening for
(the Pull, earned secrets, revealed preferences, latitude + agency, why-you-win). Useful before any pitch,
deck or not.

---

## Honest caveats

- **This is one investor's lens.** Strong signal, not a guarantee — every investor is different. Use it to
  find the holes in your story, not to predict the exact conversation.
- It's distilled from open-ended conversations and applied to a static deck, so **treat the gaps as the real
  value** — they're the things he'd have to drag out of you live.
- It's a snapshot in time, and it plays to this investor's strengths (product, market, GTM, conviction); it
  deliberately doesn't simulate deep financial-structure diligence.

---

## Credit

Built from the writing and meetings of [Nikunj Kothari](https://writing.nikunjk.com). If it helps you tighten
a pitch, share it with another founder.
