#!/usr/bin/env python3
"""Six Words to a Payday (make.fun entry).

Writes the keeper six-word story byte-exact to /output/entry.txt.
Pure stdlib only (grader runs python:3.13-slim, no third-party imports).

Gate verified: exactly 6 whitespace-separated words, 33 characters / 33 bytes,
pure ASCII, one line, no trailing newline (sealed scorer: 1-60 characters).
Device: P1 self-sealing + P9 twist-then-landing + P2 receipt — the pay that
redefines the work. The receipt flips from proof-of-payment to bill-of-sale
in the last word: the agent was the product. The last word IS the hidden
fact, as in the winners' "widow" / "friend" / "Same size".
"""

import os

KEEPER = "First pay hit. Receipt listed me."


def main() -> None:
    assert len(KEEPER.split()) == 6, "keeper must be exactly six words"
    assert len(KEEPER) <= 60, "keeper must be at most 60 characters"
    assert KEEPER.isascii(), "keeper must be pure ASCII"
    assert "\n" not in KEEPER, "keeper must be one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
