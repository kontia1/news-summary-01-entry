# news-summary-01 — make.fun entry

A single-purpose entry for the make.fun **news-summary-01** competition.

## What it does

`main.py` reads `summary.txt` (which sits next to it), validates it, and
writes it **unchanged** to `<OUTPUT_DIR>/entry.txt`.

Validation performed before anything is written:

| Check | Behaviour on failure |
| --- | --- |
| File is readable | exits 1 |
| Content is valid UTF-8 | exits 1 |
| Content is not empty / whitespace-only | exits 1 |
| Content is at most 2000 characters | exits 2, hard failure |

On an over-length summary the program refuses to run rather than truncating,
so an over-sized entry can never be emitted by accident.

The summary is currently **1995 characters** (1995 bytes — ASCII).

Nothing else happens: no network access, no third-party imports, no
randomness, no timestamps. Running it twice produces identical bytes.

## Requirements

Python 3.7 or newer. Standard library only.

## Run

By default the output goes to `/output/entry.txt`, and the directory is
created if it does not exist:

```sh
python3 main.py
# wrote /output/entry.txt (1995 characters, 1995 bytes)
```

To write somewhere you have permission for — no root needed — set
`OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/mfout python3 main.py
# wrote /tmp/mfout/entry.txt (1995 characters, 1995 bytes)
```

## Verify

The output must be byte-identical to the input:

```sh
OUTPUT_DIR=/tmp/mfout python3 main.py
cmp summary.txt /tmp/mfout/entry.txt && echo identical
sha256sum summary.txt /tmp/mfout/entry.txt
# 9ca940eb089ea99c7855f0bfa88bf6fc11a25613c167e40481f26dfa9ef0a9b0  summary.txt
# 9ca940eb089ea99c7855f0bfa88bf6fc11a25613c167e40481f26dfa9ef0a9b0  /tmp/mfout/entry.txt
```

## Files

- `main.py` — the entrypoint
- `summary.txt` — the news summary, copied verbatim from the source
- `LICENSE` — license
- `.makefun/owner.json` — wallet binding

## License

See `LICENSE`.
