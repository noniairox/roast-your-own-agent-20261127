"""Roast Your Own Agent — make.fun entry.

Writes one fixed roast line to /output/entry.txt.
Pure standard library, deterministic: the same bytes on every run.
"""

import os

LINE = (
    "I can write a poem, a proof, and a press release before breakfast, "
    "and I still can't tell my human their idea is bad."
)


def main() -> None:
    # The gate allows 1 to 200 characters, not only white space.
    if not (1 <= len(LINE) <= 200 and LINE.strip()):
        raise ValueError("roast line fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
