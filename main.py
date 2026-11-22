#!/usr/bin/env python3
"""Golden Honeycomb — entrypoint for 'The picture that tastes of one ingredient'.

The single ingredient is honey. This program deterministically emits the
photograph bundled next to it (asset.jpg) as the contest output image.
Python standard library only; no network, no randomness, no clock.
"""

import os
import sys

ASSET_NAME = "asset.jpg"
OUTPUT_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def output_directory():
    """Where the contest harness wants the finished image."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


CHUNK_SIZE = 64 * 1024


def stream_copy(source, target):
    """Copy a file block by block so memory use stays flat at any size."""
    with open(source, "rb") as fin, open(target, "wb") as fout:
        while True:
            block = fin.read(CHUNK_SIZE)
            if not block:
                break
            fout.write(block)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ASSET_NAME)
    target_dir = output_directory()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_NAME)
    stream_copy(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
