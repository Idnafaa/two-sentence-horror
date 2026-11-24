#!/usr/bin/env python3
"""Two-Sentence Horror — a two-sentence horror story writer.

Writes one original horror story of exactly two sentences (201 characters)
to /output/entry.txt.
"""
import os
import re

STORY = (
    "Every evening, my daughter lines her dolls up on her bed "
    "and whispers each one goodnight by name. "
    "Tonight they were already lined up when I came in, "
    "and a small voice from the dark was whispering mine."
)


def check(text):
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    assert len(sentences) == 2, f"story has {len(sentences)} sentences, need 2"
    assert 1 <= len(text) <= 400, f"story is {len(text)} chars, need 1-400"
    return text


def main():
    text = check(STORY)
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars, 2 sentences, to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
