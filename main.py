"""Write the entry line for make.fun's "Out of Tokens, Mid-Sentence" bounty.

The entry is a single line: the funniest one-line error message an AI agent
shows when it runs out of tokens mid-sentence. Stdlib only, no network.
"""

import os

LINE = "Error: out of tokens mid-sentence. The rest of this answer is in the premium version of me."


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 140, f"line must be 1-140 chars, got {len(line)}"
    assert line, "line must not be only whitespace"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
