"""3AM Commit Message entry.

Writes the single winning one-line git commit message to
/output/entry.txt. Deterministic and offline: no randomness, no
network, no timestamps, no paths in the output.
"""

from pathlib import Path

ENTRY = "fix: the bug only happens at 3am, so I set the server clock to 2:59am forever"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1 to 139 characters, not only white space.
    assert 1 <= len(ENTRY) <= 139, "entry must be 1-139 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
