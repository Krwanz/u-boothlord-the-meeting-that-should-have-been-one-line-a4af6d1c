#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — make.fun bounty entry.

Writes the single sentence that could have replaced an entire pointless
meeting to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""

import os

ENTRY = "The email already said yes, so this meeting is just the decision's funeral: an hour of us pretending it didn't happen."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    if out_dir.endswith("entry.txt"):
        path = out_dir
        directory = os.path.dirname(path)
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
