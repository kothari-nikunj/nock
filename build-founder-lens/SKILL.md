---
name: build-founder-lens
description: >-
  Build YOUR OWN "founder lens" — a reusable tool that pressure-tests any founder's pitch deck against
  the questions you, the investor, actually ask. Turns your recorded Granola pitch meetings into a
  distilled question-bank + principles, then applies it to decks. Use when an investor/VC wants to
  capture how they question founders, "clone my diligence questions," build a deck-review tool from
  their meeting notes, or productize their own taste. Triggers: "build my founder lens", "turn my
  meetings into a deck reviewer", "capture how I question founders", "make a lens from my Granola".
---

# Build Your Founder Lens

A playbook to turn an investor's own recorded pitch meetings into a reusable lens that reviews any
founder's deck the way *they* would — surfacing the questions they'd ask and the gaps they'd grill.

The output is a second skill (like `founder-lens`) personalized to the investor: a `question-bank.md`
(their recurring questions, by theme) + a `principles.md` (the bar beneath the questions), plus the
logic to apply both to a deck.

The flow: **pull → filter → extract → distill → calibrate against a few real decks → finalize.** The
calibration step (Stage A5) is what turns a plausible lens into one that actually sounds like the investor —
it asks them to upload a handful of named decks and checks the lens's predictions against what they really
asked in those meetings.

## The architecture — and the one seam that matters

Two stages, separated by a privacy seam:

```
STAGE A — DISTILL (private, on your machine, uses raw transcripts)
   your recorded pitch meetings ──► your "lens": question-bank.md + principles.md
        ↑ raw transcripts never leave this stage

STAGE B — APPLY (shareable: the anonymized lens only)
   a founder's deck  +  your lens ──► questions you'd ask + what's missing
```

The distilled, **anonymized** lens is the only artifact safe to hand a founder. Raw transcripts and real
company names stay local. Build with that seam in mind from step one.

## Prerequisites

- **Granola on a Business plan** (gives API access). The normal case is one account, one workspace — this
  playbook assumes that. (If you happen to run multiple workspaces, mint one API key per workspace and run
  the pull once per key; otherwise ignore.)
- **Your own writing** on what you look for — essays, memos, investment-thesis docs, threads. Optional but
  it's what makes the lens sound like *you* rather than a generic VC. Have it ready to paste.

---

## Stage A1 — Pull your meetings (Granola API)

Granola's official REST API. One key, one workspace.

1. **Get an API key:** Granola → Settings → API (Business plan). Treat it as a secret — store it in an env
   var (`GRANOLA_API_KEY`) or a chmod-600 file, never in a committed file.
2. **API surface** (base `https://public-api.granola.ai/v1`, header `Authorization: Bearer grn_…`):
   - `GET /folders` → `{folders:[{id, name, parent_folder_id}]}`. Use to find your "Pitches"/"Dealflow"/
     "Due Diligence" folder IDs.
   - `GET /notes?page_size=30&cursor=…` → `{notes:[…], hasMore, cursor}`. Cursor pagination, `page_size`
     max 30. Optional filters: `created_after`, `created_before`, `updated_after`, `folder_id`.
   - `GET /notes/{id}?include=transcript` → full note: `transcript[]`, `summary_markdown`, `summary_text`,
     `attendees[]`, `folder_membership[]` (each `{id, name}`), `calendar_event`, `owner`.
   - **Caveat that matters:** the API only returns notes that have a generated **AI summary + transcript**
     — i.e. recorded meetings. Hand-typed notes and un-recorded calls won't appear. That's fine for this —
     you want the spoken back-and-forth, not typed notes.
3. **Run the puller:** `scripts/pull.py` paginates every note, fetches each with its transcript, and saves
   one JSON per note plus an index. It has 429 backoff and is resumable (skips already-saved notes).

## Stage A2 — Filter to YOUR pitch meetings

Your note history is a mix of founder pitches, internal syncs, personal calendar items, and partner-led
calls. Keep only meetings where **you are the one driving the conversation with a founder**. Heuristics (in `scripts/extract.py`):

- **INCLUDE** if any of: the note is in a Pitches / Dealflow / Due-Diligence folder; OR (folders were added
  late, so mine unfiled "My notes" too) the title is a **company name or a person's name**; OR there's an
  **external attendee** (email domain ≠ your firm's domain).
- **EXCLUDE — internal/admin:** team syncs, investment-team meetings, all-hands, standups, 1:1s with
  colleagues, watch parties, "busy/commute" calendar junk.
- **EXCLUDE — personal:** anything not work (family, medical, kids, estate, admissions).
- **EXCLUDE — partner-led / co-attended (important):** if a colleague from your own firm is also on the
  call, the transcript cannot cleanly separate the founder from your colleague, and your own questions go
  sparse. These **pollute the lens** — drop them. Detect via >1 internal-domain attendee, or a colleague's
  name in the title. (This was a real, repeated contaminant in testing.)

Have the skill classify with these rules plus judgment, and **log what it dropped and why** — silent
filtering hides bias.

## Stage A3 — Extract YOUR questions

The transcript tags who spoke. Pull only your side:

- API transcript: each segment has `speaker.source` — **`"microphone"` = you** (your own mic),
  **`"speaker"` = the other party.** (Diarization labels are usually null; the mic/speaker split is the
  reliable signal. If you ever pull via the Granola MCP instead, the format is `"Me:"` / `"Them:"`.)
- Join consecutive `microphone` segments into a turn → split into sentences → keep sentences ending in `?`
  that are **≥4 words** → drop greetings/filler ("how are you", "can you hear me", "are you in London").
- `scripts/extract.py` does Stage A2 + A3 together and writes `my_questions.json`:
  `[{title, date, questions:[…]}]`.

## Stage A4 — Distill into a lens

Hand the full question corpus (`my_questions.json`) + your essays to a capable model with the prompt in
`scripts/distill-prompt.md`. It produces `lens/question-bank.md`:

- **8–14 themes**, ranked by how many meetings each appears in. Per theme: *what you're probing* (the
  underlying concern), 4–8 **canonical questions** (clean, founder-facing), 2–3 **real verbatim examples**
  (lightly cleaned, **anonymized to the pitch's category** — never the real company/date).
- A **STYLE & TELLS** section: *how* you ask — signature openers, your follow-up patterns, the way
  you close. This is what separates your lens from a topic list.

Then write `lens/principles.md` from your writing — the **bar beneath the questions** (your mental models,
your favorite tests, what makes you pass). Cross-link each theme to the principle it serves.

## Stage A5 — Calibrate against real decks (DO THIS BEFORE FINALIZING)

The draft lens is a hypothesis. Before you ship it, prove it transfers — by checking what it *predicts*
against what you *actually asked*. You already have the founder's questions for every meeting in the
corpus; the missing half is the deck the founder sent. So **ask the investor to upload a few specific
decks**, chosen because we can cross-reference them.

1. **Pick 3–5 meetings to validate against** from `my_questions.json` / `index.json`, optimizing for:
   - **you-driven** (not co-attended/partner-led — those were filtered, but double-check);
   - **different categories** (e.g. one B2B/infra, one deep-tech/bio, one consumer/fintech) — to stress
     category-conditioning;
   - **high question count** (you engaged deeply) and **recent**.
2. **Name them to the investor and request those exact decks.** Be specific so they can dig them up, e.g.:
   *"To calibrate your lens, please upload the decks for these meetings — I have your questions from each,
   so I can check what the lens predicts against what you actually asked: (1) [Company A] — [date],
   (2) [Company B] — [date], (3) [Company C] — [date]. PDF or a pasted outline is fine."*
   If a deck no longer exists, name the next-best meeting and ask for that one.
3. **Cross-reference each uploaded deck.** Run the draft lens on the deck (Stage B), producing predicted
   questions + gaps. Then compare to your **actual** questions from that meeting (in `my_questions.json`).
   For each pair, capture:
   - **Hit rate** — which predicted questions you actually asked (near-verbatim is the gold signal).
   - **Over-prediction** — themes the lens pushed that you ignored for this category (→ down-weight here).
   - **Under-prediction / missed tells** — things you asked that the lens didn't anticipate (→ add as a
     first-class tell, e.g. a recurring pricing/ICP/mechanism probe).
   - **Modality note** — your live questions are open-ended reactions, not deck reviews; expect the deck to
     pre-answer some, and treat the *gaps* as the real signal.
4. **Feed the learnings back** into `question-bank.md` (new tells, frequencies), `principles.md`, and the
   category weights below — THEN finalize. One pass usually moves the lens from "plausible" to "that's me."

(Watch for two real traps surfaced in testing: co-attended decks where a colleague drove the questions, and
*recording bias* — your sharpest first 1:1s are often in person and unrecorded, so the lens learns from your
second-best meetings. Note both honestly.)

## Stage B — Apply the lens to a deck

This is what founders run. Read both lens files, then output in this order:

1. **Questions you'd ask, mapped to the deck** (slide-by-slide; 2–4 per section).
2. **What the deck already answers well** (name the slides).
3. **Gaps & where you'd grill** (the unanswered questions; flag red-flag patterns — boil-the-ocean with no
   wedge, "category of one," a secret that's really category boilerplate, vision without concrete steps).
4. **Insight-count check** — how many of the three unique insights (tech / market / GTM) it carries.
5. **Weakest 3 claims + ~4 adversarial follow-ups each** (real secrets get sharper under pressure; fakes
   get vaguer). Highest-value section.
6. **The "dinner test"** — would this still be on your mind after the meeting? End with the one thing to fix.

**Category-condition FIRST** (don't weight all themes equally):
- **B2B / infra / SaaS** → lead with commercial themes (customers/what-they-used-before, pricing, ICP,
  ROI/budget, defensibility, the raise). Drill the technical mechanism hard only if the product plugs into
  infra / intercepts data.
- **Deep-tech / bio / hard-tech** → commercial recedes; lead with conviction, the core mechanism (drill it
  relentlessly — it's the bet), the validation path, and risk/acceptability.
- **Capital-intensive / proptech** → if financial-structure diligence isn't your strength, say so and keep
  the lens to what it does best (story, wedge, insight, conviction). Don't fake a domain you don't own.

## Quality learnings (hard-won — bake these in)

- **It's a transfer, not a replay.** Your lens is learned from open-ended conversations; a founder hands you
  a deck. Don't write as if a slide walk-through happened — reverse-engineer the questions and **the gaps
  are the payload.**
- **Drill the technical mechanism in proportion to how load-bearing it is** — deep for infra-plug-ins and
  deep-tech, lighter for analytics/measurement layers.
- **Tells worth confirming you captured:** what-were-they-using-before; pricing (B2B, often asked more than
  once); ICP threshold ("at least N engineers?"); "what's the last customer who said no, and why"; the
  fast-forward (18mo / 5yr); the unique-insight bar; zero-sum budget displacement; closing with "what's
  helpful." If your corpus has them, they belong in STYLE & TELLS.
- **Recording bias:** your sharpest first 1:1s with founders are often in person and never recorded — the
  recorded meeting is frequently a later, team-attended follow-up. The lens is strong but incomplete; treat
  it as a sample, not ground truth.
- **Refresh periodically** — re-run the pipeline as meetings accumulate so the lens tracks how you evolve.

## Privacy (non-negotiable)

- Raw transcripts and the question corpus stay **local**, never shipped.
- **Anonymize verbatim quotes** (real company names + exact dates → category tags like "(AI-infra pitch,
  2026-05)") before the lens goes anywhere near a founder.
- Don't put colleagues' names or the companies you met into the shipped lens.

See `scripts/` for `pull.py`, `extract.py`, and `distill-prompt.md`.
