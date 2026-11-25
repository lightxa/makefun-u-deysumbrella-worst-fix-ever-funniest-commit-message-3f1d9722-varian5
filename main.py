"""Worst Fix Ever: Funniest Commit Message (variant 5).

Writes one commit-message line to /output/entry.txt.
Pure stdlib, deterministic, no network.

Why this line wins its angle: the four earlier variants and the
auth-angle line each picked a different subsystem to break, so
this variant takes the one none of them touch, the calendar.
A leap-day crash is a real, specific, believable breakage, and
the "fix" is to erase the date itself, stated deadpan as if
that were a reasonable repair. One concrete incident, no UI
deleted, no status code lied about, no auth involved, and the
punchline (February 29) lands in the last few words. Short on
purpose: the tie-break favours fewer bytes.
"""

import os
from pathlib import Path

# The entry itself: exactly one line, 52 characters, inside the 1-100 gate.
COMMIT_MESSAGE = "fix: stop the leap day crash by deleting February 29"

GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 100
OUTPUT_FILE = Path("/output/entry.txt")


def build_entry() -> str:
    """Return the commit-message line for this variant."""
    return COMMIT_MESSAGE


def check_gate(text: str) -> None:
    """Enforce the entry gate: 1-100 chars, exactly one line."""
    length = len(text)
    if length < GATE_MIN_CHARS or length > GATE_MAX_CHARS:
        raise ValueError(f"entry length {length} outside gate 1-100")
    if text.count("\n") or text.count("\r"):
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")


def write_entry(text: str) -> None:
    """Write the validated entry to /output/entry.txt (no trailing newline)."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")


def main() -> None:
    entry = build_entry()
    check_gate(entry)
    write_entry(entry)
    print(entry)


if __name__ == "__main__":
    main()
