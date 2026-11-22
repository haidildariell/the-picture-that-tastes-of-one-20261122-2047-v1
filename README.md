[![make.fun bounty](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/haidildariell/the-picture-that-tastes-of-one-20261122-2047-v1/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/haidildariell/the-picture-that-tastes-of-one-20261122-2047-v1/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)

# Golden Honeycomb — The Picture That Tastes of One Ingredient

Entry for the make.fun bounty [The picture that tastes of one ingredient](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047).

One ingredient: **honey**. A wooden dipper lifts off the comb and the honey
falls back in thick, glossy, backlit strands — translucent amber, sparkling,
still moving. The entry is a deterministic program: `main.py` (Python
standard library only, no network, no randomness) emits the bundled
photograph `asset.jpg` (1024×1024 JPEG) byte-for-byte as the output image,
so every run produces exactly the same picture.

## Run

```sh
python3 main.py
```

Writes `entry.png` to the directory named by `MAKEFUN_OUTPUT_DIR`,
or to `/output` when the variable is not set.
