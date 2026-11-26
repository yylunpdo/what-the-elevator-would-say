#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry 281.

Writes one funny line (1-120 chars) to /output/entry.txt.
Pure stdlib, deterministic.
"""

import os

LINE = "I lift people up for a living and nobody ever says thank you \u2014 except the guy on floor 13, and he's a ghost."

assert "\n" not in LINE, "entry must be a single line"
assert 1 <= len(LINE) <= 120, f"entry length {len(LINE)} out of range"
assert LINE.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
