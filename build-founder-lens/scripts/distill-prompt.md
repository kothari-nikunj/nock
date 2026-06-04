# Distill prompt — turn your question corpus into a lens

Hand a capable model (1) `lens-data/my_questions.json` and (2) your own essays/memos/threads on what you
look for in founders. Then give it this prompt. Output is `lens/question-bank.md` + `lens/principles.md`.

---

You are building a "lens" that captures how I, an investor, evaluate founders — so it can later review any
founder's deck the way I would. You have two inputs:

1. `my_questions.json` — every question I actually asked across N recorded pitch meetings, isolated to my
   own side of the transcript. This is raw speech-to-text: expect filler, run-ons, and mangled
   company/product names. Infer intent; never quote a mangled name.
2. My writing — my essays on founders/investing. This is my *voice* and my *bar*.

Produce TWO files.

## `lens/question-bank.md` — the coverage map
- Cluster the substantive questions into **8–14 themes**, ranked by how many meetings each appears in
  (give a rough frequency like "~30 of N"). Derive themes from the data; don't impose a generic template.
- Per theme: (a) one line on *what I'm really probing for* and why; (b) 4–8 **canonical questions** phrased
  cleanly as a founder-facing checklist; (c) 2–3 **verbatim examples** from the data, lightly cleaned and
  **anonymized to the pitch's category** with a coarse date — e.g. "(AI-infra pitch, 2026-05)", never the
  real company or exact day.
- A final **"HOW I ASK — the texture"** section: the *how*, not the topics. My openers, my follow-up
  pattern, the analogies I reach for, how I push, how I close. This is the soul — make it sound like me.

## `lens/principles.md` — the bar beneath the questions
- Written in MY voice, pulling directly from my essays (quote my actual lines). Organize around MY mental
  models, not generic VC categories. For each: what it is (in my words), and what I listen for in a pitch /
  the tell. Cross-link the themes in the question-bank to the principle each one serves.

## Rules
- **Mimic my writing.** Short, declarative, specific. Use my phrases and framings. No VC jargon, no
  "product/market/tech" checklist slop — that's the exact thing to avoid.
- Ground everything in the two inputs. Don't invent opinions I haven't expressed.
- Flag the obvious gaps: themes that are thin, anything the corpus can't support.

Return the two files plus a 150-word note on the themes found and any tells you weren't sure about.
