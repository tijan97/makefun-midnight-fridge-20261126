"""Midnight Fridge Roast — one-line roast of a smart fridge that locks
itself after midnight.

The program writes exactly one roast line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the grader sets it).
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
"""

import os

# The roast: the midnight lockout itself is the joke — the leftovers
# apparently needed legal protection from their own owner. One line,
# one joke, no second punchline crowding it.
ROAST = (
    "My fridge locks itself at midnight like the leftovers "
    "took out a restraining order on me."
)

MAX_CHARS = 200
MIN_CHARS = 1


def main() -> None:
    line = ROAST.strip()
    assert MIN_CHARS <= len(line) <= MAX_CHARS, (
        f"roast must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}"
    )
    assert line.strip(), "roast must not be only whitespace"
    assert "\n" not in line, "roast must be a single line"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
