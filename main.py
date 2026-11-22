"""Entry point: copy the bundled honeycomb photograph to the output file.

The picture itself ships beside this file as asset.jpg; the program only
moves its bytes, unchanged, to <output dir>/entry.png on every run.
"""

import os
import sys

CHUNK_SIZE = 64 * 1024


def stream_copy(source, target):
    """Copy a file in fixed-size chunks so memory use stays flat."""
    with open(source, "rb") as src, open(target, "wb") as dst:
        while True:
            block = src.read(CHUNK_SIZE)
            if not block:
                break
            dst.write(block)


def resolve_output_dir():
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return "/output"


def output_entry_path():
    """Full path of the file this program writes on every run."""
    return os.path.join(resolve_output_dir(), "entry.png")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "asset.jpg")
    target = output_entry_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    stream_copy(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
