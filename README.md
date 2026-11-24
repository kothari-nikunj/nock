# Nock

> Nock your pitch before you take the shot.

A *nock* is the notch you set an arrow into before you draw and loose. **Nock** is the same idea for a pitch:
set it, check your aim, and find what's off before the meeting that counts.

A skill for **founders.** It reads your pitch deck and tells you the questions
[Nikunj Kothari](https://writing.nikunjk.com) (seed and Series A investor) would ask and, more
importantly, what he'd find missing. Built from how he questions founders, his essays, and a year of his
fundraising posts.

It works in any AI agent or chat: Claude Code, Codex, Antigravity, Claude.ai, ChatGPT, Gemini. It works
best with Claude (Opus or Sonnet), which wrote the strongest reviews in our tests.

## Quick start

### In a coding agent (Claude Code, Codex, Antigravity)

Paste this to your agent:

> Install the Nock skill from https://github.com/kothari-nikunj/nock. Clone the repo and copy the `nock`
> folder into this tool's skills directory. If this tool doesn't support skills, keep the clone and follow
> `nock/SKILL.md` whenever I ask you to review my deck.

Then attach your deck (PDF) or paste an outline and say **"nock my pitch."** It'll ask your **stage** and
**category**, then run the review.

For Claude Code, you can also install it yourself:

```bash
git clone https://github.com/kothari-nikunj/nock
mkdir -p ~/.claude/skills && cp -r nock/nock ~/.claude/skills/
```

### In a chat app (Claude.ai, ChatGPT, Gemini)

Paste these four files into the chat: `nock/SKILL.md` (the instructions), `nock/lens/principles.md`,
`nock/lens/question-bank.md`, and `nock/lens/raise-playbook.md`. Then:

> Follow SKILL.md exactly to review my pitch deck, using the three lens files. My stage is
> **[pre-seed/seed/A]** and category is **[e.g. AI infra]**.
>
> Here is my deck: [paste / attach]

Include `SKILL.md`. In our tests, Gemini without it wrote reviews three times as long and less grounded in
the deck. You can rerun the test with `evals/grade.sh`.

---

## What you get

One review, 1,200 words at most:

1. **What earns the conversation.** Your real strengths, including the ones you buried.
2. **Your story, rebuilt.** Your end state worked forward through its second and third order effects, and
   a draft of your slide-one sentence that leads with it.
3. **The three beliefs, and what's missing.** The three things an investor has to believe once your product
   works. For each: the slide that proves it (or that none does), the question he'd open with, and a
   rewrite using only your facts.
4. **The four follow-ups** he'd use on your two softest claims to tell an earned secret from a faked one.
5. **The dinner test.** Would this still be on his mind after the meeting? And the one thing to fix first.
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
