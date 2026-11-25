"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local testing).
"""

import os
from pathlib import Path

LINE = "I told my AI not to lie; it said, 'Then stop asking me to write your dating profile.'"


def main() -> None:
    # Gate in RULES.txt: UTF-8, 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip() and "\n" not in LINE
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
