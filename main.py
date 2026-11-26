#!/usr/bin/env python3
"""Funniest Lost Sock Status Update entry: writes exactly one funny status
update, in the voice of a lost sock, to /output/entry.txt.

Deterministic, no network, no randomness.
"""

from pathlib import Path

ENTRY = "Day 12 under the couch. The dust bunnies have accepted me as one of their own. I am home now."


def main() -> None:
    # Gate self-check (RULES.txt): 1-120 chars, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Self-check: what was written is byte-for-byte the entry.
    assert out.read_text(encoding="utf-8") == ENTRY, "output must equal entry"


if __name__ == "__main__":
    main()
