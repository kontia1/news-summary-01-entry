#!/usr/bin/env python3
"""make.fun entry: news-summary-01.

Reads the news summary that sits next to this script, validates it, and writes
it unchanged to <OUTPUT_DIR>/entry.txt.

Constraints honoured: standard library only, no network access, deterministic.
"""

import os
import sys
from typing import NoReturn

MAX_CHARS = 2000
HERE = os.path.dirname(os.path.abspath(__file__))
SUMMARY_PATH = os.path.join(HERE, "summary.txt")


def fail(message: str) -> NoReturn:
    print("error: %s" % message, file=sys.stderr)
    sys.exit(1)


def load_summary(path):
    """Read the summary as UTF-8 text, or exit with a diagnostic."""
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (path, exc))

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail("%s is not valid UTF-8: %s" % (path, exc))

    if not text.strip():
        fail("%s is empty or whitespace-only" % path)

    # Hard failure: the competition caps the summary at MAX_CHARS characters.
    # Never truncate -- refuse to emit an over-length entry.
    if len(text) > MAX_CHARS:
        print(
            "error: %s is %d characters, over the %d character limit"
            % (path, len(text), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(2)

    if len(text) < 1:
        fail("%s must contain at least 1 character" % path)

    return text


def main():
    text = load_summary(SUMMARY_PATH)

    out_dir = os.environ.get("OUTPUT_DIR", "/output") or "/output"
    out_path = os.path.join(out_dir, "entry.txt")

    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    except OSError as exc:
        fail("cannot write %s: %s" % (out_path, exc))

    data = text.encode("utf-8")
    print("wrote %s (%d characters, %d bytes)"
          % (out_path, len(text), len(data)))


if __name__ == "__main__":
    main()
