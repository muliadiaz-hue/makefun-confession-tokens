#!/usr/bin/env python3
"""Write the one-line AI agent confession to the harness output file.

The harness reads exactly one line (1-200 UTF-8 characters) from
$MAKEFUN_OUTPUT_DIR/entry.txt. We write the bytes ourselves so no
trailing newline or encoding surprise can sneak in.
"""

import os
import sys

CONFESSION = (
    "I spent 40,000 tokens thinking about your one-line question, "
    "then answered it in nine words, three of which were wrong."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    data = CONFESSION.encode("utf-8")
    # Guard the harness contract before writing: exactly one line,
    # 1-200 UTF-8 characters, and no trailing newline.
    if not 1 <= len(data) <= 200:
        print(f"confession is {len(data)} bytes, outside 1-200", file=sys.stderr)
        return 1
    if b"\n" in data:
        print("confession must be a single line", file=sys.stderr)
        return 1
    with open(target, "wb") as handle:
        handle.write(data)
    print(f"wrote {len(data)} bytes to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
