#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

Writes a single line (at most 200 characters) to /output/entry.txt.
Standard library only, no network, fully deterministic.
"""

import os

ENTRY = (
    "The lift was broken this morning, so Mr. Adi carried my groceries up "
    "four floors \u2014 then apologised for being slow, as if the stairs "
    "had personally offended him."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
