"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes one line (<=120 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
the excuse a robot vacuum gives for missing a spot. Stdlib only,
deterministic: the same bytes on every run.
"""

import os

EXCUSE = (
    "I missed that spot: the dust bunny unionised, "
    "the rug got a lawyer, and my suction went on strike."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = EXCUSE
    assert 1 <= len(text) <= 120, f"entry is {len(text)} characters"
    assert text == text.strip() and "\n" not in text
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
