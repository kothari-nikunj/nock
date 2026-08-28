# Nock

> Nock your pitch before you take the shot.

A *nock* is the notch you set an arrow into before you draw and loose. **Nock** is the same idea for a pitch:
set it, check your aim, and find what's off — before the meeting that counts.

Two Claude skills in one repo:

- **`nock/`** — for **founders.** Reads your pitch deck and tells you the questions
  [Nikunj Kothari](https://writing.nikunjk.com) (seed/Series A investor) would ask, and — more importantly —
  what he'd find missing. Distilled from 53 real pitch & diligence meetings plus his essays.
- **`build-your-nock/`** — for **investors.** A playbook to build *your own* version from your own recorded
  meetings, so it asks the questions *you* ask.

Example quotes are anonymized to a category (e.g. "AI-infra pitch") — no real companies or founders are named.

---

## For founders — `nock/`

### What you get

Point it at a deck and it returns, in order:

1. **The questions he'd ask**, mapped to your slides.
2. **What your deck already answers well** — named slide by slide.
3. **The gaps** — where he'd push, and the red-flag patterns it spots (boil-the-ocean with no wedge,
   "category of one," a secret that's really category boilerplate, vision with no concrete next step).
4. **An insight-count check** — how many of the three unique insights (tech / market / GTM) you carry.
   One isn't enough anymore.
5. **Your weakest 3 claims + the follow-ups** he'd use to test whether a secret is earned or faked.
6. **The "dinner test"** — would this still be on his mind after the meeting? — and the one thing to fix first.

If your deck has an ask slide, it also runs a **raise-mechanics read** from his essay on fundraising in a
consensus market: is the ask sized to actually close, price/dilution sanity (no lead goes under 10%; a
"great deal" begets questions, not interest), no competitor-round comps, current-month traction, great new
hires showcased. And you can skip the deck entirely and just ask it raise-process questions — "how much
should I raise," "who do I talk to at a firm," "what do I say about my timeline."

It leads with the *why* and the *how* (his actual frameworks and voice), not a generic product/market/tech
checklist.

### Install — Claude Code

Easiest: paste this to Claude Code and let it do the work —

> Install the skill from https://github.com/kothari-nikunj/nock — clone the repo and copy the `nock`
> folder into my Claude skills directory (`~/.claude/skills/`).

Or do it yourself in a terminal:

```bash
git clone https://github.com/kothari-nikunj/nock
mkdir -p ~/.claude/skills && cp -r nock/nock ~/.claude/skills/
```

Restart Claude Code, attach your deck (PDF) or paste an outline, and say **"nock my pitch"** / "review my
deck." It'll ask your **stage** and **category**, then run the full review.

### Use in ChatGPT / Claude.ai / Cursor / anything else

Paste `nock/lens/principles.md` and `nock/lens/question-bank.md` into the chat (add
`nock/lens/raise-playbook.md` if you want the raise-mechanics read too), then:

> You are reviewing my pitch deck using the lens in the two files above (`principles.md` = how this investor
> reads a founder; `question-bank.md` = the questions he asks and how he asks them). My stage is
> **[pre-seed/seed/A]** and category is **[e.g. AI infra]**. Give me: (1) the questions he'd ask mapped to my
> deck, (2) what I already answer well, (3) the gaps he'd push on, (4) an insight-count check across
> tech/market/GTM, (5) my weakest 3 claims with the follow-ups he'd use to break a faked secret, and (6) the
> "dinner test." Write it in his voice — warm but direct, founder-to-founder, no VC jargon.
>
> Here is my deck: [paste / attach]

> Read `nock/lens/principles.md` on its own even without a deck — it's a tight summary of what he's actually
> listening for (the Pull, earned secrets, revealed preferences, latitude + agency, why-you-win).

---

## For investors — `build-your-nock/`

Want a Nock that asks *your* questions, not his? `build-your-nock/` is the playbook: pull your recorded pitch
meetings (Granola API), filter to the ones you drove, extract your own questions, distill them into a
question-bank + principles in your voice, **calibrate against a few real decks**, and ship your own Nock.
Includes the scripts (`pull.py`, `extract.py`, `distill-prompt.md`).

Install it the same way — point Claude Code at this repo and ask it to copy the `build-your-nock` folder
into `~/.claude/skills/`, or:

```bash
git clone https://github.com/kothari-nikunj/nock
mkdir -p ~/.claude/skills && cp -r nock/build-your-nock ~/.claude/skills/
```

Then say **"build my nock."** It walks you through it end to end. Your raw transcripts stay local; the
shipped lens is anonymized.

---

## Honest caveats

- **This is one investor's lens.** Strong signal, not a guarantee — every investor differs. Use it to find
  the holes in your story, not to predict the exact conversation.
- It's distilled from open-ended conversations and applied to a static deck, so **treat the gaps as the real
  value** — they're what he'd have to drag out of you live.
- It plays to this investor's strengths (product, market, GTM, conviction) and deliberately doesn't simulate
  deep financial-structure diligence.

---

## Reach out

If Nock helps tighten your pitch — or you'd just like to talk it through — email Nikunj directly at
**nikunj@fpvventures.com**. He built this partly to meet more founders. And if it's useful, pass it to one.

More of his writing: [Balancing Act](https://writing.nikunjk.com). Licensed MIT — copy it, fork it, make it yours.
