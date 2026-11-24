#!/usr/bin/env python3
"""Write one code review comment approving a pull request with quiet
existential dread to /output/entry.txt (exactly one line, 1-140 chars,
no trailing newline)."""

import os

ENTRY = "Approved. The tests are green, Dave is gone, and the bug we ship today becomes 2029's archaeology."


def main() -> None:
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back: the file must hold exactly the entry, byte for byte.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == text.encode("utf-8"), "entry.txt mismatch"


if __name__ == "__main__":
    main()
