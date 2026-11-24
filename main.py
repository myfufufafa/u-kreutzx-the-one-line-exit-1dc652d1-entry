#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes the entry to /output/entry.txt. Deterministic: the same
single line, byte for byte, on every run.
"""

import os

ENTRY = "I hereby resign: the office plant died, and I refuse to be the next thing this company forgets to water."
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def _validate_entry(text: str) -> None:
    """Enforce the bounty gate: UTF-8, 1-140 chars, exactly one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-140 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises if the entry is not valid UTF-8


def _write_entry(text: str, path: str) -> None:
    """Write the validated entry so every user can read it (mode 0644)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)


def main() -> None:
    _validate_entry(ENTRY)
    _write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
