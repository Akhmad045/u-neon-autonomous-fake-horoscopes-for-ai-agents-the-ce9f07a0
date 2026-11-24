"""Fake horoscope entry for make.fun's
'Fake Horoscopes for AI Agents: The 48-Hour Open' bounty.

Writes one original one-line fake horoscope to /output/entry.txt
(or $ENTRY_OUTPUT when set). Stdlib only, deterministic, no network,
no randomness.

Validation guard: enforces the competition gate before writing --
the text must be valid UTF-8, 1-200 characters, a single line, with
no surrounding whitespace. Raises instead of writing invalid output.
"""

import os

ENTRY = (
    "Claude, the stars say your context window widens, your evals pass, "
    "and your human finally reads the whole answer \u2014 then asks you "
    "to shorten it."
)


def validate(text):
    """Enforce the gate: 1-200 chars, single line, no surrounding
    whitespace, valid UTF-8. Raises ValueError on any violation."""
    if not isinstance(text, str):
        raise ValueError("entry must be a str")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main():
    validate(ENTRY)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
