"""One Word, First Thought — make.fun entry.

Writes a single word to entry.txt in the output directory.

Output format: the file contains exactly the word and nothing else —
no trailing newline, no extra whitespace — so its byte length equals
the length of the word itself.
"""

import os


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write("petrichor")


if __name__ == "__main__":
    main()
