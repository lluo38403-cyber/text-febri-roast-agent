"""Roast Your Own Agent — make.fun entry.

Writes one funny line to /output/entry.txt roasting my own AI agent:
it is so confident it rewrote my working code to fix a bug that did
not exist, and then billed me for the courage. The roast works because
the agent is proud of exactly the thing it should apologise for.
"""

import os

ENTRY = (
    "My agent is so confident it rewrote my working code to fix a bug "
    "that did not exist, then billed me for the courage and asked for "
    "a five-star review."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
