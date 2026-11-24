"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single sharp, funny loading-screen tip for stressed developers
and AI coding agents to /output/entry.txt.

The tip: the developer skipped the docs; the agent is the one actually
reading them. Both sides of the keyboard recognise themselves in it --
the human who cuts corners, and the agent doing the homework neither of
them wants to do.
"""

import os

TIP = (
    "Tip: your agent is reading the docs you skipped. Let it finish -- "
    "it's the only one of you doing the homework, and it never says "
    "'this should be quick.'"
)


def validate(tip):
    """Check the tip against the competition gate before writing it."""
    if not tip or not tip.strip():
        raise ValueError("tip must not be empty or only whitespace")
    if len(tip) > 200:
        raise ValueError("tip is %d characters, over the 200 limit" % len(tip))


def main():
    validate(TIP)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(TIP)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
