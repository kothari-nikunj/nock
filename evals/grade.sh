#!/usr/bin/env bash
# Grade a set of Nock reviews with two outside models (Gemini 4 Neon via agy, and Codex), blind.
# Usage: evals/grade.sh <run-prefix> [neon|codex|both]   e.g. evals/grade.sh v2   (grades evals/runs/v2-<n>.md for each deck n present)
# Output: evals/runs/<prefix>-grade-neon.md and evals/runs/<prefix>-grade-codex.md
set -uo pipefail
cd "$(dirname "$0")/.."
PREFIX="${1:?usage: evals/grade.sh <run-prefix> [neon|codex|both]}"
WHO="${2:-both}"
OUT=evals/runs
BUNDLE="$(mktemp)"
{
  echo "Do not use any tools or read any files. Everything you need is in this message. Answer directly in text."
  echo
  echo "Grade each founder-facing pitch review below with the rubric. Summary table of grades first, then for every grade below A+, the quoted line that cost it and the edit to nock/SKILL.md or a lens file that would fix it for all future reviews. Under 700 words."
  echo; echo "=== RUBRIC ==="; cat evals/rubric.md
  for f in nock/lens/principles.md nock/lens/question-bank.md nock/lens/raise-playbook.md; do echo; echo "=== $f ==="; cat "$f"; done
  for r in "$OUT/$PREFIX"-[0-9].md; do
    n="$(basename "$r" .md)"; n="${n##*-}"
    d="$(ls evals/decks/"$n"-*.md)"
    echo; echo "=== DECK $d ==="; cat "$d"
    echo; echo "=== REVIEW $r ==="; cat "$r"
  done
} > "$BUNDLE"

WORK="$(mktemp -d)"
[ "$WHO" != codex ] && ( cd "$WORK" && agy -p "$(cat "$BUNDLE")" --model gemini-4-neon-xhigh --print-timeout 900s --disable-slash-commands \
    </dev/null > "$OLDPWD/$OUT/$PREFIX-grade-neon.md" 2>&1 ) &
[ "$WHO" != neon ] && ( cd "$WORK" && codex exec --skip-git-repo-check --sandbox read-only "$(cat "$BUNDLE")" </dev/null 2>&1 \
    | awk '/^codex$/{f=NR}{a[NR]=$0} END{for(i=f+1;i<=NR;i++)print a[i]}' | grep -v '^hook:' \
    | awk '/^tokens used/{exit}1' > "$OLDPWD/$OUT/$PREFIX-grade-codex.md" ) &
wait
rm -rf "$WORK" "$BUNDLE"
echo "wrote $OUT/$PREFIX-grade-neon.md and $OUT/$PREFIX-grade-codex.md"
