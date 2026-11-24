# Nock

> Nock your pitch before you take the shot.

A *nock* is the notch you set an arrow into before you draw and loose. **Nock** is the same idea for a pitch:
set it, check your aim, and find what's off before the meeting that counts.

Two Claude skills in one repo:

- **`nock/`** for **founders.** Reads your pitch deck and tells you the questions
  [Nikunj Kothari](https://writing.nikunjk.com) (seed and Series A investor) would ask and, more
  importantly, what he'd find missing. Distilled from 53 real pitch and diligence meetings, his essays, and
  a year of his fundraising posts.
- **`build-your-nock/`** for **investors.** A playbook to build *your own* version from your own recorded
  meetings, so it asks the questions *you* ask.

Example quotes are anonymized to a category (e.g. "AI-infra pitch"). No real companies or founders are named.

---

## For founders: `nock/`

### What you get

Point it at a deck and it returns one review, 1,200 words at most:

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

### Install: Claude Code

Easiest: paste this to Claude Code and let it do the work.

> Install the skill from https://github.com/kothari-nikunj/nock. Clone the repo and copy the `nock`
> folder into my Claude skills directory (`~/.claude/skills/`).

Or do it yourself in a terminal:

```bash
git clone https://github.com/kothari-nikunj/nock
mkdir -p ~/.claude/skills && cp -r nock/nock ~/.claude/skills/
```

Restart Claude Code, attach your deck (PDF) or paste an outline, and say **"nock my pitch"** or "review my
deck." It'll ask your **stage** and **category**, then run the review.

### Use in ChatGPT, Claude.ai, Cursor, anything else

Paste `nock/lens/principles.md`, `nock/lens/question-bank.md`, and `nock/lens/raise-playbook.md` into the
chat, then:

> You are reviewing my pitch deck using the lens in the three files above (`principles.md` is how this
> investor reads a founder; `question-bank.md` is the questions he asks and how he asks them;
> `raise-playbook.md` is his fundraising advice). My stage is **[pre-seed/seed/A]** and category is
> **[e.g. AI infra]**. Give me: (1) what earns the conversation, (2) my end state worked forward through its
> second and third order effects, plus the three things an investor has to believe, (3) my gaps ranked,
> each as slide, what he reads, rewrite, and his opening question, (4) the four follow-ups for my two
> softest claims, and (5) the "dinner test." Write it in his voice: warm, direct, founder to founder, no VC
> jargon, and no em dashes.
>
> Here is my deck: [paste / attach]

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

## For investors: `build-your-nock/`

Want a Nock that asks *your* questions, not his? `build-your-nock/` is the playbook: pull your recorded pitch
meetings (Granola API), filter to the ones you drove, extract your own questions, distill them into a
question bank and principles in your voice, **calibrate against a few real decks**, and ship your own Nock.
Includes the scripts (`pull.py`, `extract.py`, `distill-prompt.md`).

Install it the same way. Point Claude Code at this repo and ask it to copy the `build-your-nock` folder
into `~/.claude/skills/`, or:

```bash
git clone https://github.com/kothari-nikunj/nock
mkdir -p ~/.claude/skills && cp -r nock/build-your-nock ~/.claude/skills/
```

Then say **"build my nock."** It walks you through it end to end. Your raw transcripts stay local; the
shipped lens is anonymized.

`evals/` has five fictional test decks, the rubric, and `evals/grade.sh`, which has two outside models
(Gemini via `agy`, and Codex) grade a set of reviews blind. Use it to check any change to your own Nock.

---

## Honest caveats

- **This is one investor's lens.** Strong signal, not a guarantee. Every investor differs. Use it to find
  the holes in your story, not to predict the exact conversation.
- It's distilled from open-ended conversations and applied to a static deck, so **the gaps are the real
  value.** They're what he'd have to drag out of you live.
- It plays to this investor's strengths (product, market, GTM, conviction) and doesn't simulate deep
  financial-structure diligence.

---

## Reach out

If Nock helps tighten your pitch, or you'd just like to talk it through, email Nikunj directly at
**nikunj@fpvventures.com**. He built this partly to meet more founders. And if it's useful, pass it to one.

More of his writing: [Balancing Act](https://writing.nikunjk.com). Licensed MIT: copy it, fork it, make it yours.
