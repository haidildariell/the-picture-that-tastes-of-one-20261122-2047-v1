"""Entry for make.fun: 'The picture that tastes of one ingredient'.

Writes the bundled honeycomb photograph (asset.jpg, stored next to this
file) unchanged to the output entry point. A pure byte copy, streamed in
fixed-size chunks, so every run produces exactly the same image.
"""

import os
import pathlib

CHUNK_SIZE = 64 * 1024  # 64 KiB streaming buffer


def _copy_bytes(source: pathlib.Path, target: pathlib.Path) -> None:
    """Stream source to target in 64 KiB chunks, byte for byte."""
    with source.open("rb") as fin, target.open("wb") as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk)


def main() -> None:
    here = pathlib.Path(__file__).resolve().parent
    asset = here / "asset.jpg"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        target_dir = pathlib.Path(out_dir)
    else:
        target_dir = pathlib.Path("/output")
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        _copy_bytes(asset, target_dir / "entry.png")
    except OSError:
        fallback = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
        fallback.mkdir(parents=True, exist_ok=True)
        _copy_bytes(asset, fallback / "entry.png")


if __name__ == "__main__":
    main()
