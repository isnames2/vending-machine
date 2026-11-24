"""Vending machine pickup line entry for make.fun.

Writes one line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only; deterministic output.
"""

import os
from pathlib import Path

LINE = "Hey beautiful \u2014 I take exact change and give great snacks, so press B7 and I'll drop something sweet for you."
# 109 characters, within the 1-200 character gate.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
