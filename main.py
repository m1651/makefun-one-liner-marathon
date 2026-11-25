#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single original joke to /output/entry.txt.

The joke is an original one-liner, written for this competition. The program
is deterministic: no network, no randomness, no input. It enforces the
1-280 character gate and the single-line rule before writing anything.
"""

import os
import sys

JOKE = "My houseplant died of neglect, so I replaced it with a cactus and named it Exhibit A."

MAX_CHARS = 280


def main() -> int:
    joke = JOKE.strip()

    if not joke:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print(
            f"error: joke is {len(joke)} chars, over the {MAX_CHARS}-char limit",
            file=sys.stderr,
        )
        return 1
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(joke)
    print(f"wrote {len(joke)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
