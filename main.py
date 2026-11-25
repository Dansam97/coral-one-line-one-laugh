"""One Line, One Laugh — make.fun entry.

Writes a single one-liner to /output/entry.txt (gate: UTF-8, 1-200 chars).
The line: a fortune teller reads a palm, goes silent, and offers a refund
and a hug — the laugh lands on the unexpected turn at the end.
"""

import os

LINE = (
    "The fortune teller studied my palm, went completely silent, "
    "and offered me a refund and a hug."
)


def main() -> None:
    # Gate self-check: the sealed scorer only judges UTF-8 text of
    # 1-200 characters that is not only whitespace. Fail loudly here
    # rather than emit an entry the gate would silently refuse.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise ValueError(f"entry line outside the gate: {len(LINE)} chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
