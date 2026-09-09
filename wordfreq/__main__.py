"""Command-line entry point for ``python3 -m wordfreq``."""

import argparse
import sys

from . import top_words


def main() -> int:
    parser = argparse.ArgumentParser(description="Print the most frequent words from stdin.")
    parser.add_argument(
        "--top",
        type=int,
        default=10,
        metavar="N",
        help="number of words to print (default: 10)",
    )
    args = parser.parse_args()

    if args.top < 0:
        parser.error("--top must be non-negative")

    for word, count in top_words(sys.stdin.read(), args.top):
        print(f"{word}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
