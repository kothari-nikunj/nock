# Nock

> Nock your pitch before you take the shot.

A *nock* is the notch you set an arrow into before you draw and loose. **Nock** is the same idea for a pitch:
set it, check your aim, and find what's off before the meeting that counts.

A tool for **founders.** It reads your pitch deck and tells you the questions
[Nikunj Kothari](https://writing.nikunjk.com) (seed and Series A investor) would ask and, more
importantly, what he'd find missing. Built from how he questions founders, his essays, and a year of his
fundraising posts.

## Quick start

Paste this into Claude, ChatGPT, Gemini, Claude Code, Codex, or Antigravity. Fill in the brackets and
attach your deck.

```text
Read these four files, then follow SKILL.md exactly to review my pitch deck.
https://raw.githubusercontent.com/kothari-nikunj/nock/main/nock/SKILL.md
https://raw.githubusercontent.com/kothari-nikunj/nock/main/nock/lens/principles.md
https://raw.githubusercontent.com/kothari-nikunj/nock/main/nock/lens/question-bank.md
https://raw.githubusercontent.com/kothari-nikunj/nock/main/nock/lens/raise-playbook.md
My stage is [pre-seed/seed/A] and my category is [e.g. AI infra]. My deck is attached.
```

That's it. Nothing to download or install. It works best with Claude.

If your chat can't open links, download those four files and attach them instead.

Using it often in Claude Code? Install it as a skill, then just say **"nock my pitch"**:

```bash
git clone https://github.com/kothari-nikunj/nock
mkdir -p ~/.claude/skills && cp -r nock/nock ~/.claude/skills/
```

---

## What you get

One review, 1,200 words at most, written in his voice:

1. **What works.** Your real strengths, including the ones you buried.
2. **The story.** Your end state worked forward through its second and third order effects, and a draft
   of your slide-one sentence that leads with it.
3. **Three things he'd need to believe.** For each: the slide that proves it (or that none does), the
   question he'd open with, and a rewrite using only your facts.
4. **Where he'd push.** Four follow-ups on your two softest claims, to tell an earned secret from a faked
   one.
5. **Dinner.** Would this still be on his mind after the meeting? And the one thing to fix first.
6. **What it assumed.** The few inferences it made that your deck doesn't state, so you can correct them.

You can also skip the deck and ask about the raise: "how much should I raise," "who do I talk to at a
firm," "which investors should I take."

`nock/lens/principles.md` is worth reading on its own, even without a deck. It's a short summary of what
he's listening for: the Pull, earned secrets, revealed preferences, latitude and agency, why you win.

---

## Fundraising tips: `nock/lens/raise-playbook.md`

His fundraising advice, mostly in his own words, from his essays and a year of posts. Readable on its own,
no deck needed. Every point links to its source. A taste:

- "Ambition is what's being rewarded right now." Think about "the second and third order effects as a
  result of you being successful," put that end state "in the first slide," and walk the investor through
  "how you earn the right to get there."
- "Have a 3 things you need to believe in to invest up top and force the investor to commit in a binary
  way."
- AI, timing, funding, distribution, market, product, and revenue are each "a necessary component of
  their business but NOT the entire business."
- "Ask for too much, then they look at you skeptically unless you're Elon. Ask for too little and then
  you're not ambitious enough." And: "VCs don't want a 'deal.'"
- "Never compare on what your competitor got. It's the single best way to tank the deal."
- "Paid partnerships and boosting 'views' on X are now negative signal in all VC group chats."
- "A launch is the last step, not the first. Find the customer who won't shut up about you."
- "Every (unconventional) deal that's officially wired dies a 100 times in venture... It usually takes one
  champion sticking their neck out for the founder."
- "Share what makes you a great contrarian bet... figure out the default alive path."

---

## Evals

`evals/` has five fictional test decks, the rubric, and `evals/grade.sh`, which has two outside models
(Gemini via `agy`, and Codex) grade a set of reviews blind. Use it to check any change to the skill.

---

## Honest caveats

- **This is one investor's lens.** Strong signal, not a guarantee. Every investor differs. Use it to find
  the holes in your story, not to predict the exact conversation.
- He'd rather have a conversation than read a deck, so applied to a static deck, **the gaps are the real
  value.** They're what he'd have to drag out of you live.
- It plays to this investor's strengths (product, market, GTM, conviction) and doesn't simulate deep
  financial-structure diligence.

---

## Reach out

If Nock helps tighten your pitch, or you'd just like to talk it through, email Nikunj directly at
**nikunj@fpvventures.com**. He built this partly to meet more founders. And if it's useful, pass it to one.

More of his writing: [Balancing Act](https://writing.nikunjk.com). Licensed MIT: copy it, fork it, make it yours.
