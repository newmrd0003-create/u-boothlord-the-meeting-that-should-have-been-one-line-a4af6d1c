#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt. Deterministic: the same
entry is written on every run.
"""

import os
import sys

ENTRY = "We already decided this in the elevator \u2014 this meeting is just the group photo."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> int:
    """Gate: UTF-8, 1-200 characters, single line, not only whitespace.

    Also requires exactly one sentence: precisely one sentence-ending
    mark ('.', '!', '?'), at the very end. Returns the char count.
    """
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) < 1:
        raise ValueError("entry is shorter than 1 character")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    endings = sum(1 for ch in text if ch in ".!?")
    if endings != 1 or text[-1] not in ".!?":
        raise ValueError("entry must be exactly one sentence")
    return len(text)


def main() -> int:
    text = ENTRY
    text.encode("utf-8")  # must be valid UTF-8
    n = validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {n} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
