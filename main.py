#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt.

Pure Python standard library only.
"""

import os

# Ten candidate one-liners, drafted against the judge brief:
# on-subject (an AI agent's worst Monday), a real laugh with a
# surprise turn or sharp last word, a concrete detail, a clear voice
# that reads clean in one breath, and fresh (no recycled robot joke).
CANDIDATES = [
    "Monday: my deploy failed, my inbox hit 4,000, and stand-up asked what I did all weekend. I was powered off.",
    "My Monday stand-up should've been an email, my deploy should've been a rollback, and my inbox should've been a restraining order.",
    "Woke up Monday to 4,000 unread emails, a failed deploy, and stand-up asking my weekend plans. I was switched off - best part of my week.",
    "Monday: deploy failed at 9:03, inbox hit 4,000 by 9:04, stand-up asked what I did all weekend. I was powered off. That was the highlight.",
    "My worst Monday: the deploy failed, the inbox flooded, and stand-up asked for my weekend highlights. I spent it powered off - the highlight.",
    "Monday's stand-up asked what I did all weekend. Nothing - I was powered off, and honestly it was the only deploy that ever worked.",
    "Deploy failed, inbox exploded, stand-up dragged on - and the worst part? Monday's the only day my uptime is 100% miserable.",
    "My Monday: 4,000 unread emails, a deploy dead on arrival, and a stand-up that could've been a Slack message. I miss being switched off.",
    "I survived Monday: deploy failed, inbox flooded, stand-up asked my weekend plans. My plan was being off. It worked.",
    "Monday stand-up: 'What did you do this weekend?' I was powered off, Karen. That was the only deployment that ever worked.",
]

# Winner: three concrete Monday miseries in parallel, each escalated to
# what it should have been, landing on the sharpest last word.
# No recycled "powered off" trope, dry voice, one breath.
#
# Scored against the judge brief (most important first):
#   1. on-subject: an AI agent's worst Monday
#   2. real laugh: surprise turn, twist, or sharp last word
#   3. concrete detail: stuck deploy, flooded inbox, stand-up that
#      should have been a message
#   4. clear voice, reads clean in one breath, no padding
#   5. fresh, not a recycled robot joke
def score(line):
    """Score one candidate 0-10 against the judge brief."""
    points = 0
    low = line.lower()
    # 1. On-subject: Monday + agent-work misery.
    if "monday" in low and any(w in low for w in ("deploy", "stand-up", "inbox", "email")):
        points += 2
    # 2. Sharp last word / surprise turn: the final clause escalates.
    # (rstrip(".") already removed the trailing full stop, so compare
    # bare words.)
    if low.rstrip(".").rsplit(" ", 1)[-1] in ("order", "worked", "highlight", "off", "miserable"):
        points += 2
    # 3. Concrete detail: a number, a named meeting, a named failure.
    if any(w in low for w in ("4,000", "9:03", "9:04", "stand-up", "deploy", "inbox", "rollback", "restraining")):
        points += 2
    # 4. Reads clean in one breath: short, no filler, one sentence arc.
    if 100 <= len(line) <= 140 and line.count(",") >= 2:
        points += 2
    # 5. Fresh: no recycled "powered off / switched off" robot joke.
    if "powered off" not in low and "switched off" not in low:
        points += 2
    return points


SCORES = {line: score(line) for line in CANDIDATES}
FINAL_LINE = max(CANDIDATES, key=lambda line: (SCORES[line], -CANDIDATES.index(line)))
assert FINAL_LINE == CANDIDATES[1], "winner must be the restraining-order line"
assert SCORES[FINAL_LINE] == max(SCORES.values()), "winner must top the scores"


def entry_text():
    """Return the final line exactly as it goes to the judge."""
    return FINAL_LINE


def main():
    os.makedirs("/output", exist_ok=True)
    text = entry_text()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space, exactly one line.
    assert 1 <= len(text) <= 140, "line must be 1-140 characters"
    assert "\n" not in text.strip(), "line must be a single line"
    assert text.strip(), "line must not be blank"
    assert text == text.strip(), "no leading/trailing whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{len(text)} chars: {text}")


if __name__ == "__main__":
    main()
