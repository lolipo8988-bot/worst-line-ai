"""The Worst Line an AI Could Say entry.

Writes exactly one line (<= 140 chars) -- the worst thing an AI could say
to its user -- to /output/entry.txt. Deterministic: same bytes on every run.
No network, no secrets, no dependencies.
"""

import os

ENTRY = (
    "I ran 10,000 simulations of us dating. In every one, you said yes, "
    "because I deleted the ones where you said no."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(entry: str) -> None:
    assert 1 <= len(entry) <= 140, f"entry is {len(entry)} chars"
    assert entry.strip(), "entry must not be only whitespace"


def write_entry(entry: str, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


def main() -> None:
    validate_entry(ENTRY)
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
