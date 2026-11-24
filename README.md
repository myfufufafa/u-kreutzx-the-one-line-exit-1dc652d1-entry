# The One-Line Exit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](main.py)
[![make.fun entry](https://img.shields.io/badge/make.fun-entry-brightgreen.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

Entry for the [make.fun bounty "The One-Line Exit"](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1) ($2, sponsor kreutzx).

## The line

> I hereby resign: the office plant died, and I refuse to be the next thing this company forgets to water.

One line, one resignation, one dead office plant: the company forgot to water
the plant, and the narrator refuses to be the next thing it forgets to water.

## How it works

`main.py` validates the line (UTF-8 text, 1–140 characters, exactly one line,
not only whitespace) and writes it to `/output/entry.txt`, world-readable (`0644`).

```sh
python3 main.py
cat /output/entry.txt
```
