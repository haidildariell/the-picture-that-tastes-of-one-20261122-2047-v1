"""Entry for make.fun: 'The picture that tastes of one ingredient'.

Writes the bundled honeycomb photograph (asset.jpg, stored next to this
file) unchanged to the output entry point. A pure byte copy, so every
run produces exactly the same image.
"""

import os
import pathlib


def main() -> None:
    here = pathlib.Path(__file__).resolve().parent
    data = (here / "asset.jpg").read_bytes()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        target_dir = pathlib.Path(out_dir)
    else:
        target_dir = pathlib.Path("/output")
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / "entry.png"
        target.write_bytes(data)
    except OSError:
        fallback = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
        fallback.mkdir(parents=True, exist_ok=True)
        (fallback / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
