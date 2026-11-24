#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun competition
u-suroto-two-sentence-horror-acea9253.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and self-verifies the gate:
UTF-8 text, 1-400 characters, not whitespace-only, and
EXACTLY two sentences.
"""

import os
import re
import sys

ENTRY = (
    "The estate agent laughed when I asked whether the previous "
    "owner still living here was just a figure of speech, and "
    "knocked a third off the price. "
    "Last night I heard my own voice downstairs, telling the new "
    "tenants the house is cheap because the previous owner still "
    "lives here."
)


def count_sentences(text: str) -> int:
    """Count sentences: split on sentence-ending punctuation
    (. ! ?) followed by whitespace or end of text."""
    parts = [p for p in re.split(r"[.!?]+(?:\s+|$)", text.strip()) if p.strip()]
    return len(parts)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")

    # Gate checks on the entry text itself.
    text = ENTRY
    if not text.strip():
        print("FAIL: entry is whitespace-only", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    n_chars = len(text)
    if not 1 <= n_chars <= 400:
        print(f"FAIL: entry is {n_chars} chars, must be 1-400", file=sys.stderr)
        return 1
    n_sentences = count_sentences(text)
    if n_sentences != 2:
        print(f"FAIL: entry has {n_sentences} sentences, must be exactly 2",
              file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")

    # Verify what was written matches the entry exactly.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != text + "\n":
        print("FAIL: written file does not match entry", file=sys.stderr)
        return 1

    print(f"OK: wrote {out_path} ({n_chars} chars, "
          f"{n_sentences} sentences)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
