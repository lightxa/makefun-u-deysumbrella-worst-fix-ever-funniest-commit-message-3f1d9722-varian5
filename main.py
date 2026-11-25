"""Worst Fix Ever: Funniest Commit Message (variant 5).

Writes one commit-message line to /output/entry.txt.
Pure stdlib, deterministic, no network.

Strategy: v1 deleted the login page, v2 restarted the server every
47 seconds, v3 deleted the checkout button, v4 lied with 200 for
everything, and the admin-login line took the auth angle. This
variant takes a fresh angle none of them touch: the calendar.
A leap-day crash is a real, specific, believable breakage, and the
"fix" is to erase the date itself, stated deadpan as if that were
a reasonable repair. One concrete incident, no UI deleted, no
status code lied about, no auth involved, and the punchline
(February 29) lands in the last few words. Short on purpose:
the tie-break favours fewer bytes.
"""

import os

ENTRY = "fix: stop the leap day crash by deleting February 29"

# Gate: /output/entry.txt must be 1 to 100 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 100, "entry out of gate range"
assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
