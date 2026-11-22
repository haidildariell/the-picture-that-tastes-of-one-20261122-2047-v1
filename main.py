"""Entry point: copy the bundled honeycomb photograph to the output file.

The picture itself ships beside this file as asset.jpg; the program only
moves its bytes, unchanged, to <output dir>/entry.png on every run.
"""

import os
import shutil
import sys


def resolve_output_dir():
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return "/output"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "asset.jpg")
    target_dir = resolve_output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    with open(source, "rb") as src, open(target, "wb") as dst:
        shutil.copyfileobj(src, dst, length=1024 * 256)
    return 0


if __name__ == "__main__":
    sys.exit(main())
